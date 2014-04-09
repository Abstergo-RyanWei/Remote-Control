int pin=3;
void setup() {
  Serial.begin(9600);
  Serial.flush();
}
void loop() {
  while(digitalRead(pin)){
    delay(1);
  }
  delay(3);
  while(!digitalRead(pin)){
    delay(1);
  }
  Serial.println('a');
}
