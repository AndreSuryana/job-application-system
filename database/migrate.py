import database as db

db = db.Database("uts_crud_oop")
db.set_host("localhost")
db.set_username("root")
db.set_password("")
db.create_database()

db.set_table_name("applicant")
db.create_table()