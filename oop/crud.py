import mysql.connector
import datetime

class CRUD:

    def __init__(self):
        self._localhost  = "localhost"
        self._username   = "root"
        self._password   = ""
        self._db_name    = "uts_crud_oop"
        self._table_name = "applicant"
        self.create_connection()

    def create(self):
        print("=== Add New User Data ===\n")
        print("Username:")
        username = input()
        print("Password:")
        passwd = input()
        print("Name:")
        nama = input()
        print("Email:")
        email = input()
        print("Phone:")
        phone_num = input()
        print("Address:")
        address = input()
        print("Apply for:")
        apply = input()
        print("Your Reason for Applying:")
        reason = input()
        print("Your Qualification:")
        qualification = input()
        
        cursor = self._db.cursor()

        current_date = datetime.datetime.now()

        val = (username, passwd, nama, email, phone_num, address, apply, reason, qualification, current_date, "false")
        
        cursor.execute("INSERT INTO " + self._table_name + " (username, passwd, nama, email, phone_num, address, apply, applicant_reason, applicant_qualification, date_applied, accepted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", val)

        self._db.commit()

        print(cursor.rowcount, "record telah berhasil masuk.")

    def read(self):
        print("=== Show All Applicant ===\n")

        cursor = self._db.cursor()

        cursor.execute("SELECT * FROM " + self._table_name + "")

        result = cursor.fetchall()

        for person in result:
            print(person)
            print("")
    
    def update(self):
        print("=== Edit User Data ===")
        print("Search by User ID:")
        user_id = input()
        print("Username:")
        username = input()
        print("Password:")
        passwd = input()
        print("Name:")
        nama = input()
        print("Email:")
        email = input()
        print("Phone:")
        phone_num = input()
        print("Address:")
        address = input()
        
        cursor = self._db.cursor()

        val = (username, passwd, nama, email, phone_num, address, user_id)

        cursor.execute("UPDATE " + self._table_name + " SET username=%s, passwd=%s, nama=%s, email=%s, phone_num=%s, address=%s WHERE user_id=%s", val)

        self._db.commit()

        print(cursor.rowcount, "record telah di update!")
        
    def delete(self):
        print("=== Delete User Data ===\n")
        print("Search by User ID:")
        user_id = input()

        cursor = self._db.cursor()

        cursor.execute("DELETE FROM " + self._table_name + " WHERE user_id = '%s'" % user_id)

        self._db.commit()

        print(cursor.rowcount, "record terhapus!")

    def create_connection(self):
        db = mysql.connector.connect(
            host     = self._localhost,
            user     = self._username,
            passwd   = self._password,
            database = self._db_name,
        )
        
        self._db = db
