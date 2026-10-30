import pyomyo

samples = []

def onEmg(emg, movement):
    samples.append(emg)
    print(emg)

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