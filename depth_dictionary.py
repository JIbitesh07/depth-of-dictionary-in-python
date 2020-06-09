dictionary={"n1":"rudranshu","n2":{"class":"jibitesh","str":{"n1":{}}}}
#assigning counter with value 0 to count the number of braces  
counter=0
#converting dictionary to string
string=str(dictionary)
# using a for loop to iterate through the dictionary and count the number of braces
for i in string:
    if(i=="}"):
        counter=counter+1
#printing the depth of the dictionary 
print("The depth of dictionary is :",counter) 
