# Anomalous Driving

A demo of anomaly detection using NuPIC in a Unity simulation.

(Model code adapted from [mine-hack](https://github.com/nupic-community/mine-hack).)

## Requirements

- [Unity](https://unity3d.com/)
- [NuPIC](https://github.com/numenta/nupic)
- [unity-api](https://github.com/chetan51/unity-api)

## Usage

1. Run Unity API proxy server:

        python unity-api/proxy-server/run.py

2. Run anomaly detection model:

        python anomalous-driving/model/run.py

3. Open `simulation` in Unity. Then open `Scenes/Car`, and run.

If you want to see a visualization of the anomalies in the simulation, [enable Gizmos](http://www.attiliocarotenuto.com/83-articles-tutorials/unity/297-unity-3-visual-debugging-using-gizmos) in the editor.
