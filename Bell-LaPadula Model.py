# ## Teamwork: T2: Bell-LaPadula Model
# ## Author: Ela Jamali, Evan Johnson, Matthew Hurtt



def public(): # this is mainly for Shemp, his access is public

    user_question = input("Hello, Shemp. What do you want to do with file: create, read, write:")
    filename=str(input("Please Enter File Name followed by .txt: "))
    if user_question == "create":
        print("you can only view this file")
    elif user_question == "read":
        print("you can only view this file")
    elif user_question == "write":
        print("you can only view this file")
    else:
        print("Your input is not correct")

def secret():
        # This is mainly for Curly. She can create her own file, cannot write on topsecret.
    user_question = input("Hello, Curly. What do you want to do with file: create, read, write:")
    filename = str(input("Please Enter File Name followed by .txt: "))
    if user_question == "create":
        f = open(filename, "w")
    elif user_question == "read":
        f = open(filename, "r")
    elif user_question == "write":
        print("you cannot write on topsecret.")
    else:
        print("Your input is not correct")


def topsecret():
# This is mainly for Larry. He can create his own file,can only read.
    user_question= input("Hello, Larry. What do you want to do with file: create, read, write:")
    filename=str(input("Please Enter File Name followed by .txt: "))
    if user_question == "create":
        f = open(filename, "w")
    elif user_question == "read":
        f= open(filename, "r")
    elif action == "write":
        print("Sorry, your security level does not let you write")
    else:
        print("Your input is not correct")

def majestyeye():
        # This is mainly for Moe. She has access to write and read.
    user_question= input("Hello, Moe. What do you want to do with file: create, read, write:")
    filename=str(input("Please Enter File Name followed by .txt: "))
    if user_question == "create":
        f = open(filename, "w")
    elif user_question == "read":
        f= open(filename, "r")
    elif user_question == "write":
        f=open(filename, "w")
        text=input("Enter the Text that you want to add on textfile: ")
        f.write(text)
    else:
        print("Your input is not correct")

def main():

    user_input= input("Hello, please enter your name with capital letter.")
    if user_input == "Moe":
        majestyeye()

    elif user_input == "Larry":
        topsecret()

    elif user_input == "Curly":
        secret()

    elif user_input == "Shemp":
        public()

    else:
        print("You are not a valid user")


main()
