import pandas as pd
from HTE import hte

from Pass1 import pass1
from Pass2 import pass2


# Reading the file and editing it 
def Cleaninp(string1):
    df= pd.read_csv(string1,'\t')

    
    
    df.drop(df.columns[[0,len(df.columns)-1]],axis =1,inplace = True)


   
    list = []
    #check if line starts with . then delete
    for i in range (0,len(df)): 
        if ((df.iloc[i,0]) == '.' ):  #df.iloc[i-->row, 0-->column] --> specific loction
            #skip this line
            continue
        else:#append full row in list
            list.append(df.iloc[i])            
    #store list in dataframe
    df = pd.DataFrame(list)
    #print(df)
    
    #pass the list to intermidita file to be created

    df.to_csv('intermediate.txt','\t', index=False )

Cleaninp('in.txt')


def main():
      #CALLING FUN AND SENDING ARG
       pass1('intermediate.txt')
       pass2('out_pass1.txt')
       hte('out_pass2.txt')
   
    
  
if __name__=="__main__":
    main()

