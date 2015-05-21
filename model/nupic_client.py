import random

import numpy as np
from unity_client.fetcher import Fetcher

from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.algorithms import anomaly_likelihood

import model_params

anomalyLikelihoodHelper = anomaly_likelihood.AnomalyLikelihood(
  claLearningPeriod=100,
  estimationSamples=100
)

def calculate_radius(point1, point2):
  # print "Calculating distance between points:"
  # print point1
  # print point2
  if point1 is None:
    return 5
  p1 = np.array(point1["location"])
  p2 = np.array(point2["location"])
  dist = np.linalg.norm(p1 - p2)
  time_delta = point2["time"] - point1["time"]
  # print "dist: %f" % dist
  # print "time delta: %i" % time_delta
  blocks_per_second = (dist / time_delta)
  # print "blocks per second: %f" % blocks_per_second
  return max(int(round(blocks_per_second)), 5)


def cycle(model):
  last_point = None
  fetcher = Fetcher()

  while True:
    data = fetcher.sync()

    if data is None:
      continue

    if fetcher.skippedTimesteps > 0:
      print "WARNING: Skipped {0} timesteps.".format(fetcher.skippedTimesteps)

    # print "received raw data: {0}".format(data)
    time = data["timestamp"]
    xyz = [data["x"], data["y"], data["z"]]
    vector = np.array(xyz).astype(int)
    this_point = dict(time=time, location=xyz)
    radius = calculate_radius(last_point, this_point)
    last_point = this_point
    modelInput = {
      "vector": (vector, radius)
    }
    result = model.run(modelInput)
    anomalyScore = result.inferences["anomalyScore"]
    anomalyLikelihood = anomalyLikelihoodHelper.anomalyProbability(
      random.random(), anomalyScore
    )
    print time, xyz, radius, anomalyScore, anomalyLikelihood



def run():
  params = model_params.MODEL_PARAMS
  model = ModelFactory.create(params)
  model.enableInference({"predictedField": "vector"})
  cycle(model)


if __name__ == "__main__":
  run()

