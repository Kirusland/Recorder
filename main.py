import sounddevice
from scipy.io.wavfile import write
fs=44100 #sample rate
second = int(input("Введите длительность записи: ")) #в секундах
print("Reconrding...\n")
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()
write("output.wav", fs, record_voice)
print("Запись завершина \n Откройте файл output.wav для прослушивания!")