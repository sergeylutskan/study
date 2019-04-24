# Удалить тишину из звукового файла
# Remove the silence from audio file

import wave
import struct

def break_the_silence():
   
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")
     
    dest.setparams(source.getparams())
     
    # найдем количество фреймов
    frames_count = source.getnframes() 
     
    data = struct.unpack("<" + str(frames_count) + "h",
                         source.readframes(frames_count))
     
    
    newdata = []
    
    for i in data:
        
        if i > 5 or i < -5:
            newdata.append(i)
    
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata) 
    # записываем содержимое в преобразованный файл.
    dest.writeframes(newframes) 
    source.close()
    dest.close()


#удалить перед сдачей
break_the_silence()
