import time
import botbook_gpio as gpio
 
def measureDistance():
        trigPin = 22                           # указываем номер контакта Raspberry Pi, к которому подключен Trig контакт датчика HC-SR04
        echoPin = 27                           # указываем номер контакта Raspberry Pi, к которому подключен Echo контакт датчика HC-SR04
 
        v=(331.5+0.6*20)                       # скорость звука при температуре 20 градусов Цельсия(вы можете указать свое значение вместо 20) в м/с
 
        gpio.mode(trigPin, "out")              # устанавливаем контакт как выход
 
        gpio.mode(echoPin, "in")               # устанавливаем контакт как вход
        gpio.interruptMode(echoPin, "both")    # режим прерывания, чтобы функция pulseInHigh вычислила длительность перехода сигнала с 0 до 1 и от 1 до 0
 
        gpio.write(trigPin, gpio.LOW)          # устанавливаем низкий уровень сигнала
        time.sleep(0.5)                        # задержка в пол секунда
 
        gpio.write(trigPin, gpio.HIGH)         # устанавливаем высокий уровень сигнала
        time.sleep(1/1000000.0)                # задержка в 1 мкс
        gpio.write(trigPin, gpio.LOW)          # устанавливаем низкий уровень сигнала
 
        t = gpio.pulseInHigh(echoPin)          # вычисляем длительность сигнала
 
        d = t*v*50                             # вычисляем пройденное расстояние
        return d                               # возвращаем значение
 
d = measureDistance()                          # вызываем функцию и сохраняем возвращенное значение в переменную       
print "Distance: %.2f cm" % d         
