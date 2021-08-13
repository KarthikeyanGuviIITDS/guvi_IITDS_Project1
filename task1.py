from os import path
import re

def registration():
    username = input("Enter email id: ")
    password = input("Enter new password: ")
    validation(username,password)

def validation(emailid,pwd):
    mail_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(mail_regex, emailid)):
        print("Valid Email")
        valid_mail_ind='Y'
    else:
        print("Invalid Email")
        valid_mail_ind='N'

    pwd_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
    pat = re.compile(pwd_regex)               
    mat = re.search(pat, pwd)
      
    # validating conditions
    if mat:
        print("Password is valid.")
        valid_pwd_ind='Y'
    else:
        print("Password invalid !!")
        valid_pwd_ind='N'

    if valid_mail_ind=='Y' and valid_pwd_ind=='Y':
        writefile(emailid,pwd)

def writefile(username,password):
    loc='C:/Users/USER/test/'
    outFileName=loc+username+".txt"
    outFile=open(outFileName, "w")
    outFile.write(username+"|"+password)
    outFile.close()

def login():
    username=input("Enter user name: ")
    password=input("Enter your password: ")
    loc='C:/Users/USER/test/'+username+'.txt'
    if path.exists(loc):
        inFile=open(loc,"r")
        content=inFile.read()
        pwd_content=content.split('|')[1]
        if password==pwd_content:
            print('Logged in')
        else:
            print('Enter correct password or Forget password')
            fgt_pwd=input("Enter Y if want to retrive password: ")
            if fgt_pwd=='Y':
                forget_pwd()
    else:
        print("User doesn't exist, kindly register")

def forget_pwd():
    username=input("Enter user name: ")
    loc='C:/Users/USER/test/'+username+'.txt'
    if path.exists(loc):
        inFile=open(loc,"r")
        content=inFile.read()
        pwd_content=content.split('|')[1]
        print("Your password is: "+pwd_content)
    else:
        print("User doesn't exist, kindly register")

option=int(input("""Choose options as below:
1 - new registration
2 - login
3 - forgot password
"""))

if option==1:
    registration()
elif option==2:
    login()
elif option==3:
    forget_pwd()
else:
    print("Choose correct option")