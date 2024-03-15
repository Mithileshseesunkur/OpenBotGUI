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
  if (Serial.available()>0) {
    int value;
    Serial.readBytes((char*)&value, 2);
    
    if (value>0)
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

    
    
  

  





