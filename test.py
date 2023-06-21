#providing variables
A='35'
B='60'
C='37'
D='42'
#illustrate available answers
print ('Calculate following example: (5+5)*6')
print ('A).35')
print ('B).60')
print ('C).37')
print ('D).42')
user_answer=input ('Answer:')
#right answer algoritm
if user_answer == 'A':
    if A=='35':
        print("Invalid answer")
    else:
        print("True")

if user_answer == 'B':
    if B=='60':
        print('True')
    else:
        print('Invalid answer')
                
if user_answer == 'C':
    if C=='37':
        print('Invalid answer')
    else:
        print('True')
                    
if user_answer == 'D':
    if D=='42':
        print('Invalid answer')
    else:
        print('True')
