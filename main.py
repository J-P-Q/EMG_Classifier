import pyomyo
from collections import deque

WINDOW_SIZE = 40 #assumption only 

ringBuffer = deque(maxlen=WINDOW_SIZE * 2)


def onEmg(emg, movement):
    print("{:5} | {:5} | {:5} | {:5} | {:5} | {:5} | {:5} | {:5} ".format(emg[0], emg[1], emg[2], emg[3], emg[4], emg[5], emg[6], emg[7]))
    ringBuffer.append(emg)
    return

def windowAndMav():
    if len(ringBuffer >= 40):
        window = [ringBuffer.popleft() for i in range(40)]

    # ALGORITHM: 
    mavArray = sum(abs(w) for w in window) / WINDOW_SIZE
    return mavArray

def dataGathering():
    # save to CSV for training models
    return

def predict():
    # lda.predict(mavArray)
    return

def main():
    armband = pyomyo.Myo(mode=pyomyo.emg_mode.RAW)
    armband.connect() #finds dongle
    armband.add_emg_handler(onEmg)

    try:
        while True:
            armband.run()
    except KeyboardInterrupt:
        armband.disconnect()

    return
        

if __name__ == "__main__":
    main()