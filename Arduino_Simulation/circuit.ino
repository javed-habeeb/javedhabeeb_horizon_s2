// C++ code
//
#include <Servo.h>

//servo initialization
Servo myServo;
int servoPos = 0;
int potentioRead = 0;
float potentioVal = 0;
int angle = 0;
//pin initialised for potentiometer reads
int analogPin = A2;
double Vpotential = 9.0;

//get the potentio value from analogread
//map it to the servo voltage

void setup()
{
  Serial.begin(9600);
  myServo.attach(5);
  pinMode(12,OUTPUT);
  
}

void loop()
{
  potentioRead = analogRead(analogPin);
  //potentiometer code
  //note:Vpotential is intentionally made 9v to map
  //more angle values obtained
  potentioVal = (Vpotential/1023.0)*potentioRead;
  //Serial.println(potentioVal);
  
  //analog in -> digital out
  angle = map(potentioVal,0,Vpotential,0,180);
  //angles measured -> 0,
  //you can obtain only max 5 distinct values
  //since the input voltage to potentiometer is 5v
  Serial.print("angle: ");
  Serial.println(angle);
  
  delay(10);
  
  //move the servo to angle
  if(angle>68){
  	myServo.write(68);
    digitalWrite(12,HIGH);
  	}
  else{myServo.write(angle);
       digitalWrite(12,LOW);}
  
  
}
