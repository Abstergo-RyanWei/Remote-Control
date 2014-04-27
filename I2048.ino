char pin[5]={3,4,5,6,7};
void setup(){
  Serial.begin(9600);
  Serial.flush();
}
void hehe(char a,bool p){
  while(digitalRead(a)==p)
    delay(1);
  delay(1);
}
void mygod(){
  if (digitalRead(pin[0])) {
    Serial.println('u');
    hehe(pin[0], true);
  } else if (digitalRead(pin[1])) {
    Serial.println('l');
    hehe(pin[1], true);
  } else if (digitalRead(pin[2])) {
    Serial.println('d');
    hehe(pin[2], true);
  } else if (digitalRead(pin[3])) {
    Serial.println('r');
    hehe(pin[3], true);
  }else
    delay(1);
}
void nott(){
  Serial.println('n');
  while (digitalRead(pin[4]))
    mygod();
  while (!digitalRead(pin[4]))
    mygod();
}
void cht(){
  Serial.println('c');
  hehe(pin[4], true);
  hehe(pin[4], false);
}
void loop() {
  nott();
  cht();
}
