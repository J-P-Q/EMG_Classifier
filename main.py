import pyomyo
from collections import deque

N_CHANNELS = 8
WINDOW_SIZE = 40 #assumption only 
STRIDE = 20 #assumption only
sampleCounter = 0

ringBuffers = [deque(maxlen=WINDOW_SIZE) for _ in range(N_CHANNELS)]

features = deque(maxlen=5)

def windowAndMav():
    global sampleCounter
    global features
    if (len(ringBuffers[0]) == WINDOW_SIZE) and (sampleCounter >= STRIDE):
        sampleCounter = 0

        channelMav = [ sum(abs(x) for x in ringBuffers[i]) / WINDOW_SIZE for i in range(N_CHANNELS)]
        features.append(channelMav)
    return 

def dataGathering():
    featureInput = features.popleft()
    with open("testEmg.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(featureInput)
    return


def onEmg(emg, movement):
    print("{:5} | {:5} | {:5} | {:5} | {:5} | {:5} | {:5} | {:5} ".format(emg[0], emg[1], emg[2], emg[3], emg[4], emg[5], emg[6], emg[7]))

    for channel in range(N_CHANNELS):
        ringBuffers[channel].append(emg[channel])

    global sampleCounter
    sampleCounter += 1

    windowAndMav()
    dataGathering()
    return

def predict():
    #ldaInput = features.popleft()
    # lda.predict(ldaInput)
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
