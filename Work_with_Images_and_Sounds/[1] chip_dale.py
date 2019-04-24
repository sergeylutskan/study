# Сделать звукойо файл с более тонким голосом, путем удаления части фреймов (оставить каждый 2..5 фрейм)
# Make an audio file with a thinner voice, by removing parts of the frames (leave each 2..5 frame)

import wave
import struct

def chip_and_dale(number):
    if number  < 6 and number > 1:
        source = wave.open("in.wav", mode="rb")
        dest = wave.open("out.wav", mode="wb")
         
        dest.setparams(source.getparams())
         
        # найдем количество фреймов
        frames_count = source.getnframes() 
         
        data = struct.unpack("<" + str(frames_count) + "h",
                             source.readframes(frames_count))
         
        
        newdata = []

        for i in range(0, len(data), number):
            newdata.append(data[i])
         
        newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata) 
         
        # записываем содержимое в преобразованный файл.
        dest.writeframes(newframes) 
        source.close()
        dest.close()


#удалить перед сдачей
chip_and_dale(int(input()))
