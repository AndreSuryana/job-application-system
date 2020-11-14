import os

def header():
    print("============================")
    print("=== JOB APPLICANT SYSTEM ===")
    print("============================")

# def new_applicant():
#     pass

# def login_applicant():
#     pass

def applicant_menu():
    os.system("cls")
    header()
    have_account = input("Do already have an Account? (Y/T) : ")

    if have_account == "Y":
        # login_applicant()
    else:
        # new_applicant()

if __name__ == "__main__":
    os.system("cls")
    header()
    print("[1] Login as Applicant")
    print("[2] Login as HRD")
    print("[3] Exit")
    menu = input("> ")

    if menu == "1":
        applicant_menu()
    elif menu == "2":
        pass
    elif menu == "3":
        exit()
    else:
        print("Wrong Input!")