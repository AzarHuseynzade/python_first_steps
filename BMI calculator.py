#variables 
x=input('weight:')
    
y=input('height (in meters):')

BMI = int(x)/(float(y)**2)

print(BMI)

#conditions 
if 18.5 < BMI < 25:
    print('Normal')

if 25 < BMI <30:
    print('Overweight')

if 30 < BMI < 35:
    print('Obesity Class 1')

if 35 < BMI < 40:
    print('Obesity Class 2')