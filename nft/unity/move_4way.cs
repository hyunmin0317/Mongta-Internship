using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 
public class move_4way : MonoBehaviour
{
    public int Speed;
    // Use this for initialization
    void Start()
    {
        
    }
 
    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.LeftArrow))
        {
            transform.Translate(Vector3.left() * Speed * Time.deltaTime);
        }
    }
}
