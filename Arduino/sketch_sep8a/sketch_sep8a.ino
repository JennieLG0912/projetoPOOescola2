void setup() {
  pinMode(13,OUTPUT);//define o pino 13 como saida
  

}

void loop() {
  digitalWrite(13,HIGH);//acende o led
  delay(1000);
  digitalWrite(13,LOW);
  delay(1000);

  

}
