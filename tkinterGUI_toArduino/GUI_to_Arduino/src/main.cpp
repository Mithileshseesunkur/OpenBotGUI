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

}
void loop() {
  // put your main code here, to run repeatedly:
  while (!Serial.available());

  received_data=Serial.readString().toInt();

  Serial.print(received_data);
  
  
  
}

    
    
  

  





