import pandas as pd

def pass1(INTERMIDATE):
    df = pd.read_csv(INTERMIDATE, '\t')
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
   
    #print(list(Format1)[0])
    LC=[]
    dataColumns = list(df.columns.values)
    start = str(dataColumns[2]).upper()
    LC.append(start)
    for i in range(0, len(df) -1 ):
        INST = str(df.iloc[i,1]).upper().strip()

        #CHECK FORMAT 3
        if  INST in Format3.keys():
            NEW_LC = hex(int(LC[-1],16) + 3).upper()
            LC.append(NEW_LC[2:])
        #CHECK FORMAT 1
        elif INST in Format1.keys():
            NEW_LC = hex(int(LC[-1],16) + 1).upper()
            LC.append(NEW_LC[2:])
        #CHECK EXPRESSION 
        elif  INST == "RESB":
            VAR_ = int(df.iloc[i,2])
            NEW_LC = hex(int(LC[-1],16) + VAR_).upper()
            LC.append(NEW_LC[2:])

        elif INST == 'RESW':
            VAR_ = int(df.iloc[i,2])
            NEW_LC = hex(int(LC[-1],16)+  (VAR_ *3)).upper()
            LC.append(NEW_LC[2:])
        elif  INST == 'BYTE':
            CHAR_ = str(df.iloc[i,2])
            if  CHAR_[0].upper() == 'X':
                NEW_LC = hex((int(LC[-1],16))+ (int((len(CHAR_)-3)//2))).upper()
                LC.append(NEW_LC[2:])
            elif CHAR_[0].upper() == 'C':
                NEW_LC = hex(int(LC[-1],16)+ (len(CHAR_)-3)).upper()
                LC.append(NEW_LC[2:])

        elif INST == 'WORD':
            NEW_LC = hex(int(LC[-1],16) + 3)
            LC.append(NEW_LC[2:])
       
 
     
     
    #INSERT LC IN DATAFRAME THEN ADD TO PASS1
    df.insert(0,'       ',LC)
    df.to_csv('out_pass1.txt','\t', index=False )


    df = pd.read_csv('out_pass1.txt','\t')
    #REMOVE COL 2 3 
    SYMB = df.drop(df.columns[[2,3]],axis =1)
    SymbolTable = SYMB.dropna() #REMOVE COL WITHOUT LABELS 
    #STORE 
    SymbolTable.to_csv('symbTable.txt','\t', index=False )
list1 = []
output1 = {}
list2=[]
    
symb = open('symbTable.txt', 'r') #open file and read from it
list1=symb.readlines()
for i in list1:
    if i[0] == " ":
     continue
    else:
       list2=i.strip("\n").split("\t")
       output1.update( {list2[0]:list2[1]} ) 

print(list(output1)[0])   

     

   




 



    