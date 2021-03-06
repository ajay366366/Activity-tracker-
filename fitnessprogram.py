print("Welcome to Aj fitness")
a =input("Enter your name to acess or  create  a new account with us \n")

#function to create new files
def text1(b):
    return (b + "exercise.txt")
c = text1(a)
def text2(d):
    return (d+"diet.txt")
e = text2(a)
def getdate():
    import datetime
    return datetime.datetime.now()
m=getdate()
activity_time=str(m)
#create new account for new user
try:
    with open(c,"x") as d:
        d.write("The is exercises you performed  ")
    with open(e,"x") as d:
        d.write("These are  diets you took ")
    print("You have created your account successfully\n")
except Exception as error:
    print ("Ahh You are allready having an account with us\n")
user_response=int(input("Enter 0 if you wants to see your activity 1 if you wants add to your activity\n"))
if user_response==0:
    with open(c,"rt") as c1:
        content=c1.read()
        print(content)
    with open(e,"rt") as e1:
        content2=e1.read()
        print(content2)
elif user_response==1 :
    user_response2=int(input("Enter 1 if you wants to report for exercise  or 0 for diet \n"))
    if user_response2==1:
        with open(c, "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write("  ")
            c1.write(input("Enter which exercise you  did\n"))
    elif user_response2==0:
        with open(e, "a") as e1:
            e1.write("\n")
            e1.write(activity_time)
            e1.write("  ")
            e1.write(input("Enter which diet you took\n"))
    else:
        print("Ouch you entered an invalid response")
else:
    print("You entered invalid response yaar")

end=input("enter a key to logout")



