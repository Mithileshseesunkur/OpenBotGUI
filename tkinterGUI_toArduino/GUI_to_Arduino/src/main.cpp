#include <Arduino.h>

// put function declarations here:
#define yellow 13
#define red 12
#define blue 8
#define white 7


int countYellow=1;
int countBlue;

unsigned long startMillis;
unsigned long millisYellowOn;
unsigned long millisYellowOff;
unsigned long millisBlueOn;
unsigned long millisBlueOff;
unsigned long millisRedOn;
unsigned long millisRedOff;
unsigned long millisWhiteOn;
unsigned long millisWhiteOff;
unsigned long previousMillis=0;
const unsigned long period = 500;

int received_data;

void setup() 
{
  // put your setup code here, to run once:
  pinMode(yellow,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(red,OUTPUT);
  pinMode(white,OUTPUT);
  
  Serial.begin(9600);
  delay(400);

}
void loop() {
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
}

    
    
  

  





