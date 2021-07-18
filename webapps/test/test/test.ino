#include "pitches.h"

//7segment
int PIN_Seg[] = {2,3,4,5,6,7,8,9};



//buzzer
int arraySize = 8;
int melody[] = {
  NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4,
  NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5
};
int noteDurations[] = {8,8,6,6,4,4,4,4};



//TMP
int PIN_TMP36 = A0;

void setup() {
  for(int i = 0; i<8; ++i)
  {
    pinMode(PIN_Seg[i], OUTPUT);
    Serial.begin(9600);
  }
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() > 0)
  {
    int input = Serial.read();
    if(input == '1')
    {
      digitalWrite(PIN_Seg[1], HIGH);
      digitalWrite(PIN_Seg[4], HIGH);
      delay(1000);
    }
    else if(input == '2')
    {
      digitalWrite(PIN_Seg[1], LOW);
      digitalWrite(PIN_Seg[4], LOW);



















      
      digitalWrite(PIN_Seg[5], HIGH);
      digitalWrite(PIN_Seg[4], HIGH);
      digitalWrite(PIN_Seg[7], HIGH);
      digitalWrite(PIN_Seg[3], HIGH);
      digitalWrite(PIN_Seg[2], HIGH);
      delay(1000);
    }
    else if(input == '3')
    {
      digitalWrite(PIN_Seg[5], LOW);
      digitalWrite(PIN_Seg[4], LOW);
      digitalWrite(PIN_Seg[7], LOW);
      digitalWrite(PIN_Seg[3], LOW);
      digitalWrite(PIN_Seg[2], LOW);
      digitalWrite(PIN_Seg[5], HIGH);
      digitalWrite(PIN_Seg[4], HIGH);
      digitalWrite(PIN_Seg[7], HIGH);
      digitalWrite(PIN_Seg[1], HIGH);
      digitalWrite(PIN_Seg[2], HIGH);
      delay(1000);
    }
    else if(input == '4')
    {
      for(int note = 0; note < arraySize; note++)
      {
        int duration = 1000/ noteDurations[note];
        tone(10, melody[note], duration);
        delay(duration+30);
      }
    }
    else if(input == '5')
    {
      int Volt1 = analogRead(PIN_TMP36);
      float Volt2 = Volt1 * 5.0 / 1024.0;
      float Cel = (Volt2 - 0.5) * 100;
      Serial.print(Cel);
      Serial.println(" °C");
      delay(500);
    }
  }
}
