import pyomyo
import csv
import time
from collections import deque

N_CHANNELS = 8
WINDOW_SIZE = 40 #assumption only 
STRIDE = 20 #assumption only
sampleCounter = 0

ringBuffers = [deque(maxlen=WINDOW_SIZE) for _ in range(N_CHANNELS)]

features = deque(maxlen=5)

recording = False

rawWriter = None
featureWriter = None

def windowAndMav():
    global sampleCounter
    global features
    if (len(ringBuffers[0]) == WINDOW_SIZE) and (sampleCounter >= STRIDE):
        sampleCounter = 0

        channelMav = [ sum(abs(x) for x in ringBuffers[i]) / WINDOW_SIZE for i in range(N_CHANNELS)]
        features.append(channelMav)
        featureWriter.writerow(channelMav)
    return 


def onEmg(emg, movement):
    global sampleCounter

    if not recording:   # Gate Recording
        return

    print("{:5} | {:5} | {:5} | {:5} | {:5} | {:5} | {:5} | {:5} ".format(emg[0], emg[1], emg[2], emg[3], emg[4], emg[5], emg[6], emg[7]))

    for channel in range(N_CHANNELS):
        ringBuffers[channel].append(emg[channel])

    sampleCounter += 1

    rawWriter.writerow(emg)
    windowAndMav()
    return

def predict():
    #ldaInput = features.popleft()
    # lda.predict(ldaInput)
    return

def main():
    armband = pyomyo.Myo(mode=pyomyo.emg_mode.RAW)
    armband.connect() #finds dongle
    armband.add_emg_handler(onEmg)

    global recording
    global rawWriter
    global featureWriter

    rawFile = open("rawEmgTest1.csv", "w", newline="")
    rawWriter = csv.writer(rawFile)

    featureFile = open("featureEmgTest1.csv", "w", newline="")
    featureWriter = csv.writer(featureFile)

    start = time.time()
    try:
        while True:
            elapsed = time.time() - start

            if elapsed < 5:
                recording = False
            elif elapsed < 10:
                recording = True
            else: 
                break

            armband.run()

    except KeyboardInterrupt:
        pass

    finally:
        armband.disconnect()
        rawFile.close()
        featureFile.close()

    return
        

if __name__ == "__main__":
    main()
