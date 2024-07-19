import serial
import time
from emotions import detect_emotions

def main():
    try:
        # ser = serial.Serial('COM3', 9600, timeout=1)
        time.sleep(2)  # Allow some time for serial port to initialize

        def callback(x, y):
            print(f"Face detected at ({x}, {y})")
            # ser.write(str(x).encode())
            print(f"Sent to Arduino: {x}")
            time.sleep(3)

        detect_emotions(callback)

    except serial.SerialException as e:
        print(f"Serial port error: {e}")

    finally:
        # if ser.is_open:
        #     ser.close()
        #     print("Serial port closed.")
        print('ok')

if __name__ == "__main__":
    main()