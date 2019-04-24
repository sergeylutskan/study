# Разделить звуковой файл на 4 части. Собрать его обратно в последовательности 3-4-1-2
# Split the audio file into 4 parts. Put it back in the sequence of parts 3-4-1-2

import wave
import struct

def pitch_and_toss():
   
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")
     
    dest.setparams(source.getparams())
     
    # найдем количество фреймов
    frames_count = source.getnframes() 
     
    data = struct.unpack("<" + str(frames_count) + "h",
                         source.readframes(frames_count))
     
   
    newdata = data[2*len(data)//4:3*len(data)//4] + data[3*len(data)//4:] + data[:len(data)//4] + data[len(data)//4:2*len(data)//4] 


    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata) 
     
    # записываем содержимое в преобразованный файл.
    dest.writeframes(newframes) 
    source.close()
    dest.close()


#удалить перед сдачей
pitch_and_toss()





