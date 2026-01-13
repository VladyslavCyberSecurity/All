/*int ledPin = 2;                 цілі
float temperature = 25.3;         дробові
char letter = 'A';                слова
if (temperature > 30) {}          іф стейтмент
else {}                           теж воно
for (int i = 0; i < 10; i++){}    цикл
while (true){}                    безкінечний цикл
void blink(){}                    код, який щось робить
void setup(){}                    виконується один раз при запуску
void loop(){}                     виконується постійно*/


/* програма, яка блимає LED тричі швидко, потім робить паузу 2 секунди і повторює це знову.
int ledPin = 2;
void setup(){
  pinMode(ledPin, OUTPUT);
}
void loop(){
  for (int i = 0; i < 3; i++){
    digitalWrite(ledPin, HIGH);
    delay(300);
    digitalWrite(ledPin, LOW);
    delay(300);
  }   
  digitalWrite(ledPin, LOW);
  delay(2000);
}*/


/* лампа вмикається при натисканні
int ledPin = 2;                               //синя кнопка
int buttonPin = 0;                            //кнопка boot
bool ledState = false;                        //зразу вимкнути контролер
void setup(){                                 // спрацьовує при запуску 
  pinMode(ledPin, OUTPUT);                    // оголосити пін як вихід(сигнал виконати тут)
  pinMode(buttonPin, INPUT_PULLUP);           // кнопка з внутрішнім підтягуванням(щоб кнопка активізувалася)
}
void loop(){                                  // працює постійно
  int buttonState = digitalRead(buttonPin);   // перевіряє чи натиснув я кнопку чи ні
  if (buttonState == LOW){                    // low означає, що кнопка натиснута, а high навпаки
    ledState = !ledState;                     // поміняти стан
    digitalWrite(ledPin, ledState);           // врайт, тобто виконує змінні
    delay(300);                               // 0.3 секунди
  }
}
*/


/*лед вмикається при натискані і вимикається, коли відпускаю
int ledPin = 2;
int buttonPin = 0;
bool ledState = false;

void setup(){
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin,  INPUT_PULLUP);
}

void loop(){
  int buttonState = digitalRead(buttonPin);
  if (buttonState == LOW){
    ledState = !ledState;
    digitalWrite(ledPin, ledState);
  } else{
    ledState = false;
    digitalWrite(ledPin, ledState);
  }
}
*/

/*Завдання №4: Випадкове миготіння LED
int ledPin = 2;
int buttonPin = 0;
bool ledState = false;

void setup(){
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin,  INPUT_PULLUP);
}

void loop(){
  int buttonState = digitalRead(buttonPin);
  if (buttonState == LOW){
    digitalWrite(ledPin, HIGH);
    delay(random(200, 2000));
    digitalWrite(ledPin, LOW);
    delay(random(200, 2000));
  } else {
    digitalWrite(ledPin, LOW);
  }
}*/

int ledPin = 2;
int buttonPin = 0;

unsigned long previousMillis = 0; // коли востаннє змінився стан
int ledState = LOW;
unsigned long blinkInterval = 500; // випадковий інтервал

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  randomSeed(analogRead(0));
}

void loop() {
  int buttonState = digitalRead(buttonPin);
  unsigned long currentMillis = millis(); // час із запуску ESP32

  if (buttonState == LOW) {
    // якщо настав час змінити стан LED
    if (currentMillis - previousMillis >= blinkInterval) {
      previousMillis = currentMillis;
      ledState = !ledState;
      digitalWrite(ledPin, ledState);
      blinkInterval = random(100, 1000); // новий випадковий інтервал
    }
  } 
  else {
    digitalWrite(ledPin, LOW); // коли кнопку відпущено — вимкнути
  }
}


































