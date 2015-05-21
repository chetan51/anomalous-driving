using UnityEngine;
using System.Collections;
using System;

public class GPS : MonoBehaviour {

	void Update() {
		double timestamp = (System.DateTime.Now - new DateTime(1970, 1, 1).ToLocalTime()).TotalSeconds;

		API.instance.SetOutput("x", gameObject.transform.position.x);
		API.instance.SetOutput("y", gameObject.transform.position.y);
		API.instance.SetOutput("z", gameObject.transform.position.z);
		API.instance.SetOutput("timestamp", timestamp);
	}

}
