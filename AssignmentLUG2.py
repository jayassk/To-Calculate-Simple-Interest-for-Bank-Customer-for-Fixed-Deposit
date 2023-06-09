#To Calculate Simple Interest for Bank Customer for Fixed Deposit
str(['Female','SeniorCitizen','Male','NonSeniorCitizen'])
cg=str(input('Enter customer gender as Female or Male ='))
cc=str(input('Enter customer citizenship as SeniorCitizen or NonSeniorCitizen ='))
p=int(input('Enter Initial Principal='))
t=int(input('Enter the Time period of Deposit='))
r=float()
if (cg=='Female' and cc=='SeniorCitizen'):
    r=float(0.08)
    print('R=',r)
    print('Simple Interest=',(p*t*r)/100)
elif (cg=='Female' and cc=='NonSeniorCitizen'):
    r=float (0.06)
    print('R=',r)
    print('Simple Interest=',(p*t*r)/100)
elif (cg=='Male' and cc=='SeniorCitizen'):
    r=float (0.07)
    print('R=',r)
    print('Simple Interest=',(p*t*r)/100)
elif (cg=='Male' and cc=='NonSeniorCitizen'):
    r=float (0.05)
    print('R=',r)
    print('Simple Interest=',(p*t*r)/100)
else:
    print('Enter Correct Details!')


