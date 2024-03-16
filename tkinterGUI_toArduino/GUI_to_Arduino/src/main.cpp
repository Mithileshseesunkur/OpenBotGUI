#include <Arduino.h>
#include "SerialTransfer.h"

// put function declarations here:
#define yellow 13
#define red 12
#define blue 8
#define white 7

SerialTransfer myTransfer;
// Define the size of the array to store received data
const int MAX_DATA_SIZE = 10;
byte receivedData[MAX_DATA_SIZE]; // Array to store received data
int receivedDataSize = 0; // Variable to keep track of the number of bytes received
uint16_t dataIndex =0;

int countYellow=1;
int countBlue;


void setup() 
{
  // put your setup code here, to run once:
  pinMode(yellow,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(red,OUTPUT);
  pinMode(white,OUTPUT);
  
  Serial.begin(115200);
  myTransfer.begin(Serial);
  
  //wait a bit..
  
  

}
void loop() 
{


  if(myTransfer.available())
  {
    digitalWrite(white,HIGH);
    
    // send all received data back to Python
    for(uint16_t i=0; i < myTransfer.bytesRead; i++)
    {
      receivedData[i] = myTransfer.packet.rxBuff[i];
      dataIndex++;
    }
       
      if (receivedData[0]>40.0)
    {
      digitalWrite(yellow,HIGH);
    }
    
    

    if (receivedData[1]>40.0)
    {
      digitalWrite(blue,HIGH);
    }
    
    
  
  }
  delay(500);

}
    
    
  

  





