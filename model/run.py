import random

import numpy as np
from unity_client.fetcher import Fetcher

from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.algorithms import anomaly_likelihood

import model_params



def calculateRadius(position1, position2, time1, time2, minRadius=5):
  positionDelta = np.linalg.norm(position2 - position1)
  timeDelta = time2 - time1
  speed = positionDelta / timeDelta if timeDelta > 0 else 0
  return max(int(round(speed)), minRadius)



def run():
  params = model_params.MODEL_PARAMS
  model = ModelFactory.create(params)
  model.enableInference({"predictedField": "vector"})

  anomalyLikelihoodHelper = anomaly_likelihood.AnomalyLikelihood(
    claLearningPeriod=100,
    estimationSamples=100
  )

  lastPosition = None
  lastTime = None
  fetcher = Fetcher()

  while True:
    data = fetcher.sync()

    if data is None:
      continue

    if fetcher.skippedTimesteps > 0:
      print "WARNING: Skipped {0} timesteps.".format(fetcher.skippedTimesteps)

    time = data["timestamp"]
    position = np.array([data["x"], data["y"], data["z"]]).astype(int)

    if lastPosition is None:
      lastPosition = position
      lastTime = time

    radius = calculateRadius(lastPosition, position, lastTime, time)
    modelInput = {
      "vector": (position, radius)
    }
    result = model.run(modelInput)

    anomalyScore = result.inferences["anomalyScore"]
    anomalyLikelihood = anomalyLikelihoodHelper.anomalyProbability(
      random.random(), anomalyScore
    )

    fetcher.inputData["anomalyScore"] = anomalyScore
    fetcher.inputData["anomalyLikelihood"] = anomalyLikelihood

    print anomalyScore, anomalyLikelihood

    lastPosition = position
    lastTime = time



if __name__ == "__main__":
  run()
