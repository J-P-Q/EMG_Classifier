import pyomyo
from collections import deque

WINDOW_SIZE = 40 #assumption only 

ringBuffer = deque(maxlen=WINDOW_SIZE * 2)


def onEmg(emg, movement):
    samples.append(emg)
    print("{:5} | {:5} | {:5} | {:5} | {:5} | {:5} | {:5} | {:5} ".format(emg[0], emg[1], emg[2], emg[3], emg[4], emg[5], emg[6], emg[7]))
    ringBuffer.append(emg)

def windowAndLda():
    if len(ringBuffer >= 40):
        window = [ringBuffer.popleft() for i in range(40)]

    # ALGORITHM: 
    # mavArray = MAV(window)
    # classification = LDA.predict(mavArray)

def main():
    armband = pyomyo.Myo(mode=pyomyo.emg_mode.RAW)
    armband.connect() #finds dongle
    armband.add_emg_handler(onEmg)

    try:
        while True:
            armband.run()
    except KeyboardInterrupt:
        armband.disconnect()
        

if __name__ == "__main__":
    main()