import serial

ser = serial.Serial('COM3',115200)

while True:

    data = ser.readline().decode().strip()

    try:
        distance = float(data)
        print("Distance:",distance,"m")
    except:
        pass