import pandas as pd

def pass2(pass2):
    df = pd.read_csv(pass2, '\t')
    Format3 = dict({
        "ADD":"18",
        "AND":"40",
        "COMP":"28",
        "DIV":"24",
        "J":"3C",
        "JEQ":"30",
        "JGT":"34",
        "JLT":"38",
        "JSUB":"48",
        "LDA":"00",
        "LDCH":"50",
        "LDL":"08",
        "LDX":"04",
        "MUL":"20",
        "OR":"44",
        "RD":"D8",
        "RSUB":"4C",
        "STA":"0C",
        "STCH":"54",
        "STL":"14",
        "STSW":"E8",
        "STX":"10",
        "SUB":"1C",
        "TD":"E0",
        "TIX":"2C",
        "WD":"DC",
    })
    Format1 = dict({
        "FIX":"C4","FLOAT":"C0",
        "HIO":"F4","NORM":"C8",
        "SIO":"F0", "TIO":"F8",
        })
   
    OBCODE=[]
    list11 = []
    symbout = {}
    list21=[]
        
    symb = open('symbTable.txt', 'r') #open file and read from it
    list11=symb.readlines()
    for i in list11:
        if i[0] == " ":
         continue
        else:
         list21=i.strip("\n").split("\t")
         symbout.update( {list21[1]:list21[0]} ) 

    print(symbout) 
    print(list(symbout)[0]) 
   

    

    for i in range(0, len(df)  ):
        INST = str(df.iloc[i,2]).upper().strip()
        label=str(df.iloc[i,3]).strip()
        
       




        #CHECK byte C or X
        if INST == 'BYTE':
            CHAR_ = str(df.iloc[i,3])
            if  CHAR_[0].upper() == 'X':
                NEW_OBCODE = CHAR_[2:len(CHAR_)-1].upper()
                OBCODE.append(NEW_OBCODE)
            elif CHAR_[0].upper() == 'C':
                newchar =  CHAR_[2:len(CHAR_)-1].upper()
                
                NEW_OBCODE = newchar.encode('utf-8').hex().upper()
                OBCODE.append(NEW_OBCODE)

  
        #CHECK word
        elif INST == 'WORD':
            NEW_OBCODE = hex(int(df.iloc[i,3]))[2:].zfill(6) #####
            OBCODE.append(NEW_OBCODE)
        #CHECK EXPRESSION 
        elif  INST == "RESB" or INST == 'RESW' or INST == "END":
            OBCODE.append(' ')

       #CHECK FORMAT 3 INDEXING OR IMMDET OR 3ADY
        elif INST in Format3.keys():
            if str(df.iloc[i,3])[0] == "#" :
                 OB = hex(int(Format3[INST],16)+1)[2:]
                 OBCODE.append(OB[:].zfill(2) + hex(int(df.iloc[i,3][1:]))[2:].zfill(4))
            elif len(str(df.iloc[i,3]).split(',')) == 2 :
                 OB=Format3[INST]
                 indexlabel=symbout[df.iloc[i,3][:-2]]
                 OBCODE.append(OB[:].zfill(2) + hex(32768+int(indexlabel,16))[2:].zfill(4)) #-2---. KOL HGA M3ADA A5R 2 FL CHAR


            else :    
                 OB = Format3[INST] 
                 if label in symbout.keys():
                    labelvalue=symbout[label]
                    OBCODE.append(OB + labelvalue) #ques
                 else:
                     OBCODE.append(OB + '0000') #Rsub
        #CHECK FORMAT 1 AND HANDLING
        elif INST in Format1.keys():
            OB = Format1[INST]
            OBCODE.append(OB[:])
       
 
     
     
    #INSERT OBCODE IN DATAFRAME THEN ADD TO PASS2
    df.insert(4,"OBCODE",OBCODE,True)
    df.to_csv('out_pass2.txt','\t', index=False ) #INDEX FALSE ---> NUMRING LINES IS DISABLED
    df = pd.read_csv('out_pass2.txt','\t')


  

