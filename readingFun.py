#+======================================================================================+
# |Authors          : Kolli Hrudhay,Narendrababu S,Akshat Gupta,Potturi Mourya Chandra
# |Package          : Hospital Emergency
# |Module           : readingFun.py
# |Language         : Python 3.7
# |Description      : This module when called by the Assignment_code.py module, 
#                     will return the path distances between points provided in 
#                     the later module (from the file inputPS6.txt) in the 
#                     required and proper format (without extra spaces,symbols etc) 
#                     for the Assignment_code.py module to correctly identify 
#                     and execute the function.
#
#+======================================================================================+

def readingFun(value):
    ''' This function read values from the input provided by the Assignment_code.py module and return the command
        in the right/required format. 
    ''' 
    elements1=[]
    elements2=[]


    with open(value,'r') as file1:
        for f1 in file1:
            if f1:
                if '/' in f1:
                    f1 = f1.split('/')
                    for i in range(len(f1)):
                        f1[i]=f1[i].strip()
                    elements1.append(f1)

                elif ':' in f1:
                    f1 = f1.split(':')
                    for i in range(len(f1)):
                        f1[i]=f1[i].strip()
                    elements2.append(f1)

    return elements1,elements2