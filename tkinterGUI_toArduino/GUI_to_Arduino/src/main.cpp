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
float receivedData[MAX_DATA_SIZE]; // Array to store received data
int receivedDataSize = 0; // Variable to keep track of the number of bytes received


int countYellow=1;
int countBlue;


struct __attribute__((packed)) STRUCT {
  
  float input;
} testStruct;

void setup() 
{
  // put your setup code here, to run once:
  pinMode(yellow,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(red,OUTPUT);
  pinMode(white,OUTPUT);
  
  Serial.begin(115200);
  myTransfer.begin(Serial);
  

}
void loop() 
{
  

  if(myTransfer.available())
  {
    digitalWrite(white,HIGH);
    
    // send all received data back to Python
    /*
    for(uint16_t i=0; i < myTransfer.bytesRead; i++)
    {
      receivedData[i] = myTransfer.packet.rxBuff[i];
      
    }
    */
    uint16_t recSize = 0;

    recSize = myTransfer.rxObj(testStruct, recSize);
    //Serial.print(testStruct.z);
    //Serial.print(testStruct.y);
    //Serial.print(" | ");

    recSize = myTransfer.rxObj(receivedData, recSize);
    //Serial.println(arr);
       
      if (receivedData[0]>40)
    {
      digitalWrite(yellow,HIGH);
    }
    else
    {
      digitalWrite(yellow,LOW);
    }
    
    

    if (receivedData[1]>40)
    {
      digitalWrite(blue,HIGH);
    }
    else
    {
      digitalWrite(blue,LOW);
    }
    
  
  }
  delay(100);

}
    
    
  

  





