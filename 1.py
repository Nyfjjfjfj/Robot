int E1 = 10;
int M1 = 12;
int E2 = 11;
int M2 = 13;
int command;
int speed = 165;

void setup()
{
pinMode(M1, OUTPUT);
pinMode(M2, OUTPUT);
pinMode(9, OUTPUT);
Serial.begin(9600);
pinMode(4,OUTPUT);

}

void loop()
{
command = Serial.read();
while(true){
  tone(4,500);

}

/* ARM Code */
 if (command == 205) //Gripper Move To Angle 0
{
  for (int i = 0;i < 400;i ++){
    digitalWrite(9,HIGH);
    delayMicroseconds(200);
    digitalWrite(9,LOW);
  }
  
}
else if (command == 207) //gripper move to angle 180
{
  for (int i = 0;i < 240;i ++){
    digitalWrite(9, LOW);
    digitalWrite(9, HIGH);
    delayMicroseconds(2700);
    digitalWrite(9, LOW);
    delayMicroseconds(2700);
  }
}
/* CAR CODE */
else if (command == 200)
{
  digitalWrite(M2, 0);
  digitalWrite(M1, 1);
  analogWrite(E1, speed);
  analogWrite(E2, speed);
}
else if (command == 201)
{
digitalWrite(M1,0);
digitalWrite(M2, 0);
analogWrite(E1, speed);
analogWrite(E2, speed);
}
else if (command == 202)
{
digitalWrite(M1,0);
digitalWrite(M2, 0);
analogWrite(E1, 0);
analogWrite(E2, 0);
}
else if (command == 203)
{
digitalWrite(M1,1);
digitalWrite(M2, 1);
analogWrite(E1, speed);
analogWrite(E2, speed);
}
else if (command == 204)
{
digitalWrite(M1,0);
digitalWrite(M2, 1);
analogWrite(E1, speed);
analogWrite(E2, speed);
}
else if (command == 0)
{
digitalWrite(M1,1);
digitalWrite(M2, 1);
analogWrite(E1, 0);
analogWrite(E2, 0);
}
}




