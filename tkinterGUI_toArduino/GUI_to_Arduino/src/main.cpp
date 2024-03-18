#include <Arduino.h>
#include "SerialTransfer.h"
#include <SoftwareSerial.h>

SoftwareSerial mySerial(3,2); //RX TX

// put function declarations here:
#define yellow 11
#define red 12
#define blue 8
#define white 7

SerialTransfer myTransfer;

// Define the size of the array to store received data
const int MAX_DATA_SIZE = 10;
float receivedData[MAX_DATA_SIZE]; // Array to store received data
int i;

//structure of incoming data
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

  mySerial.begin(115200);
  mySerial.println("Print to SoftwareSerial");
  

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
    mySerial.println("receivedData--------");
    recSize = myTransfer.rxObj(receivedData, recSize);

    for (i=0;i<MAX_DATA_SIZE;i++)
    {
      mySerial.println(receivedData[i]);
    }
    mySerial.println("--------");
    
    
    //check some conditions with recivedData   
    if (receivedData[0]>40)
    {
      mySerial.println("yellow");
      digitalWrite(yellow,HIGH);
    }
    else
    {
      digitalWrite(yellow,LOW);
    }

    if (receivedData[1]>40)
    {
      mySerial.println("blue");
      digitalWrite(blue,HIGH);
    }
    else
    {
      digitalWrite(blue,LOW);
    }
    
  
  }
  delay(100);
  
  
  

}
    
    
  

  





