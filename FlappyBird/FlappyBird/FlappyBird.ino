void setup() {
  Serial.begin(9600);
  Serial.flush();
}
void loop() {
  Serial.println('a');
  delay(500);
}
