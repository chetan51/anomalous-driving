using UnityEngine;
using System.Collections;
using System;

public class GPS : MonoBehaviour {

	void Update() {
		API.instance.SetOutput("x", gameObject.transform.position.x);
		API.instance.SetOutput("y", gameObject.transform.position.y);
		API.instance.SetOutput("z", gameObject.transform.position.z);
		API.instance.SetOutput("timestamp", System.DateTime.Now);
	}

}
