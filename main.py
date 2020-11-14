import os
import database.database as dbase
import create, read, update, delete

def header():
    print("==================================")
    print("===   JOB APPLICATION SYSTEM   ===")
    print("==================================")
    print("Author : Andre Suryana")
    print("NIM    : 1908561103")
    print("==================================")

def main():
    # Executing/creating database :
    db = dbase.Database("uts_crud_oop")
    db.set_host("localhost")
    db.set_username("root")
    db.set_password("")
    db.create_database()
    db.set_table_name("applicant")
    db.create_table()

    while True:
        os.system("cls")
        header()
        print("Menu :")
        print("\t[1] Create")
        print("\t[2] Read")
        print("\t[3] Update")
        print("\t[4] Delete")
        print("\t[5] Exit")
        menu = input(">>> ")

        if menu == '1':
            create.crud.create()
        elif menu == '2':
            read.crud.read()
        elif menu == '3':
            update.crud.update()
        elif menu == '4':
            delete.crud.delete()
        elif menu == '5':
            print("Exit")
            break
        else:
            print("Input salah!")

        os.system("pause")

if __name__ == "__main__":
    main()