import time 

def led_blinker(blink_count, interval):
    for i in range(blink_count):
        print("ON")
        time.sleep(interval)
        print("OFF")
        time.sleep(interval)
    print("Blinking complete")

output = led_blinker(5, 0.5)
print(output)