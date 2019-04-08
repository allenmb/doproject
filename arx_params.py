import numpy as np

for i in range(8):
    if i == 0:
        fo = open(r".\arx_params.txt","w")
        fo.write("")
        fo.close()
    else:
        fo = open(r".\trial"+str(i)+"\params.txt","r")
        a = fo.read()
        fo.close()
        fo = open(r".\arx_params.txt","a")
        fo.write("\nTrial"+str(i)+"\n")
        fo.write(a)
        fo.close()
        
fo = open(r".\arx_params.txt","r")
a = fo.read()
print(a)
fo.close()