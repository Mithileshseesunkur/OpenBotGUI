#include <Arduino.h>

// put function declarations here:
#define yellow 13
#define red 12
#define blue 8
#define white 7


const byte MAX_NUM_ELEMENTS = 10;  // Maximum number of elements in the array
float received_data[MAX_NUM_ELEMENTS];


int countYellow=1;
int countBlue;


void setup() 
{
  // put your setup code here, to run once:
  pinMode(yellow,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(red,OUTPUT);
  pinMode(white,OUTPUT);
  
  Serial.begin(9600);

  //initializing received_data with zeros
  for (int i = 0; i < MAX_NUM_ELEMENTS; i++) {
    received_data[i] = 0;
  }

  //wait a bit..
  delay(400);
  

}
void loop() {
  
  
  /*
  if (Serial.available() >= sizeof(float)) 
  {
    // Read the incoming bytes into a float variable
    float receivedFloat;
    Serial.readBytes((char*)&receivedFloat, sizeof(float));

    // Print the received value
    Serial.print("Received value: ");
    Serial.println(receivedFloat, 4);  // Print with 4 decimal places

    //arduino commands after reading float value
    if (receivedFloat>12.2)
    {
      digitalWrite(yellow,HIGH);
      digitalWrite(blue,LOW);
      digitalWrite(red,HIGH);
      digitalWrite(white,LOW);
    }
    else
    {
      digitalWrite(yellow,LOW);
      digitalWrite(blue,LOW);
      digitalWrite(red,LOW);
      digitalWrite(white,LOW);
    }
  }
  */
  if (Serial.available() > 0) {  // Check if data is available
    digitalWrite(red,HIGH);
    // Read the number of elements
    byte num_elements = Serial.read();
    delay(500);
    digitalWrite(red,LOW);

    // Ensure the number of elements does not exceed the array size
    if (num_elements <= MAX_NUM_ELEMENTS)//&& Serial.available() >= 4 * num_elements)
    {
      digitalWrite(white,HIGH);
      delay(500);
      // Read and reconstruct each float
      for (int i = 0; i < num_elements; i++) 
      {
        digitalWrite(blue,HIGH);
        byte buffer[4];
        Serial.readBytes(buffer, 4);
        received_data[i] = *((float*)buffer);
        digitalWrite(blue,LOW);

      }
      delay(500);
      digitalWrite(white,LOW);
    }
  }

  if (received_data[0]>40.0)
  {
    digitalWrite(yellow,HIGH);
  }
  

  if (received_data[1]>40.0)
  {
    digitalWrite(blue,HIGH);
  }
  else
  {
    digitalWrite(blue,LOW);
  }
 
}

    
    
  

  





