import pandas as pd

from Pass1 import pass1
from Pass2 import pass2


# error in iloc
def hte(pass2):
 df = pd.read_csv(pass2, '\t')
 file = open("hte.txt",'w') # create new file
 startaddress=str(df.iloc[1,0]).zfill(6) # get start adderess
 name=str(df.iloc[0,1]).zfill(6)
 endaddress=str(df.iloc[len(df)-1,0]).zfill(6)
 line='H' + name + startaddress + str((hex(int(endaddress,16)-int(startaddress,16)))[2:]).zfill(6) + '\n'

 file.write(line)

 line=""
 address = startaddress 
 #df.shape return numebr of rows
 for i in range(0, len(df) ):
    INST = str(df.iloc[i,2]).upper().strip()
   
    if INST == 'RESB' or  INST == 'RESW' or len(line) >= 60 :
       leng=hex(int(df.iloc[i,0],16) -int(address,16) )[2:].zfill(2)
       line='T' + address.zfill(6) + leng + line + '\n'
       file.write(line)
       line = ""
       address = df.iloc[i,0] 


    else :
        line+=df.iloc[i,4]   













 file.write('E' + startaddress)
 file.close()