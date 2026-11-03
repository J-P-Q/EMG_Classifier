import pyomyo
from collections import deque

N_CHANNELS = 8
WINDOW_SIZE = 40 #assumption only 

ringBuffers = [deque(maxlen=WINDOW_SIZE*2) for _ in range(N_CHANNELS)]

features = []

def onEmg(emg, movement):
    print("{:5} | {:5} | {:5} | {:5} | {:5} | {:5} | {:5} | {:5} ".format(emg[0], emg[1], emg[2], emg[3], emg[4], emg[5], emg[6], emg[7]))

    for channel in N_CHANNELS:
        ringBuffers[channel].append(emg[channel])
    return

def windowAndMav():
    if len(ringBuffers[0]) >= WINDOW_SIZE:
        for i in range(N_CHANNELS):
            window = [ringBuffers[i].popleft() for _ in range(WINDOW_SIZE)]
            channelMav = sum(abs(x) for x in window) / WINDOW_SIZE
            features.append(channelMav)
    return 

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