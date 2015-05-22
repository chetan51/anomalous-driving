using UnityEngine;
using System.Collections;
using System;

public class GPS : MonoBehaviour {

	public float scale = 1.0f;

	void Update() {
		double timestamp = (System.DateTime.Now - new DateTime(1970, 1, 1).ToLocalTime()).TotalSeconds;

		API.instance.SetOutput("x", gameObject.transform.position.x * scale);
		API.instance.SetOutput("y", gameObject.transform.position.y * scale);
		API.instance.SetOutput("z", gameObject.transform.position.z * scale);
		API.instance.SetOutput("timestamp", timestamp);
	}

}
