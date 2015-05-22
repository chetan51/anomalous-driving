using UnityEngine;
using System.Collections;

public class AnomalyVisualization : MonoBehaviour {

	public float duration = 10f;

	Vector3 lastPosition;

	void ShowAnamolyLine() {
		if (API.instance.GetInput("anomalyScore") == null) return;

		float anomalyScore = (float)(double)API.instance.GetInput("anomalyScore");
		Debug.Log(anomalyScore);
		Color color = Color.Lerp(Color.green, Color.red, anomalyScore);
		Debug.DrawLine(lastPosition, transform.position, color, duration);
	}

	void Start() {
		lastPosition = transform.position;
	}

	void Update() {
		ShowAnamolyLine();
		lastPosition = transform.position;
	}

}
