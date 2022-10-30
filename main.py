import sqlite3

database_name = 'mydb.sqlite'
connection = sqlite3.connect(database_name)


# -----------------------------------User class
class User:
    def __init__(self, user_id, first_name, last_name, phone_number, email, role):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.role = role

    @staticmethod
    def create_tables():
        drop_is_exist_user = '''DROP table IF EXISTS User'''
        creat_user_table = '''CREATE TABLE User(
                        id INTEGER PRIMARY KEY ,
                        first_name VARCHAR(30),
                        last_name VARCHAR(30),
                        phone_number VARCHAR(30),
                        email VARCHAR(255),
                        role VARCHAR(255)
                        );'''
        connection.execute(drop_is_exist_user)
        connection.execute(creat_user_table)

    @staticmethod
    def get_All_users():
        sql = '''SELECT * FROM  User'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

    @staticmethod
    def insert_user(user):
        sql = ''' INSERT INTO User (first_name, last_name, phone_number, email, role)
                              VALUES(?, ?, ?, ?, ?) '''
        cursor = connection.cursor()
        cursor.execute(sql, (user.first_name, user.last_name, user.phone_number, user.email, user.role))
        fid = cursor.lastrowid
        connection.commit()
        return fid

    @staticmethod
    def delete(id):
        sql = '''DELETE FROM User WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, str(id))
        connection.commit()

    @staticmethod
    def get_user_by_id(id):
        sql = '''SELECT * FROM  User WHERE ID = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, str(id))
        row = cursor.fetchone()
        return row


# --------------------------------------------------Departement class
class Department:
    def __init__(self, department_id, name, access_type):
        self.department_id = department_id
        self.name = name
        self.access_type = access_type

    @staticmethod
    def creat_tables():
        drop_is_exist_user = '''DROP table IF EXISTS Department'''
        creat_user_table = '''CREATE TABLE Department(
                        id INTEGER PRIMARY KEY ,
                        name VARCHAR(30),
                        access_type VARCHAR(30)
                        );'''
        connection.execute(drop_is_exist_user)
        connection.execute(creat_user_table)

    @staticmethod
    def insert_Department(department):
        sql = ''' INSERT INTO Department (id,name ,access_type)
                              VALUES(?, ?, ?) '''
        cursor = connection.cursor()
        cursor.execute(sql, (department.department_id, department.name, department.access_type))
        fid = cursor.lastrowid
        connection.commit()
        return fid

    @staticmethod
    def get_All_Department():
        sql = '''SELECT * FROM  Department'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

    @staticmethod
    def get_departement_by_id(id):
        sql = '''SELECT * FROM  Department WHERE ID = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, str(id))
        row = cursor.fetchone()
        return row

    @staticmethod
    def delete(id):
        sql = '''DELETE FROM Department WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, str(id))
        connection.commit()


# --------------------------------------------------supplier class
class Supplier:
    def __init__(self, supplier_id, name, phone_number, email, address):
        self.supplier_id = supplier_id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    @staticmethod
    def create_tables():
        drop_is_exist_supplier = '''DROP table IF EXISTS Supplier'''
        creat_user_table = '''CREATE TABLE Supplier(
                        id INTEGER PRIMARY KEY ,
                        name VARCHAR(255),
                        phone_number VARCHAR(30),
                        email VARCHAR(255),
                        address VARCHAR(255)
                        );'''
        connection.execute(drop_is_exist_supplier)
        connection.execute(creat_user_table)

    @staticmethod
    def insert_Supplier(supplier):
        sql = ''' INSERT INTO Supplier (id,name ,phone_number , email ,address )
                              VALUES(?, ?, ?,?,?) '''
        cursor = connection.cursor()
        cursor.execute(sql,
                       (supplier.supplier_id, supplier.name, supplier.phone_number, supplier.email, supplier.address))
        fid = cursor.lastrowid
        connection.commit()
        return fid

    @staticmethod
    def get_All_suppliers():
        sql = '''SELECT * FROM  Supplier'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

    @staticmethod
    def get_supplier_by_id(id):
        sql = '''SELECT * FROM  Supplier WHERE ID = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, str(id))
        row = cursor.fetchone()
        return row

    @staticmethod
    def delete(id):
        sql = '''DELETE FROM Supplier WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, str(id))
        connection.commit()


# --------------------------------------------------- Machine Class

class Machine:
    def __init__(self, machine_id, name, mark, machine_type, supplier_id, department_id):
        self.machine_id = machine_id
        self.name = name
        self.mark = mark
        self.machine_type = machine_type
        self.supplier_id = supplier_id
        self.department_id = department_id

    @staticmethod
    def create_table():
        drop_is_exist_machine = '''DROP table IF EXISTS Machine'''
        creat_user_table = '''CREATE TABLE Machine(
                        id INTEGER PRIMARY KEY ,
                        name VARCHAR(30),
                        mark VARCHAR(30),
                        machine_type VARCHAR(30),
                        supplier_id INTEGER ,
                        department_id INTEGER ,
                        FOREIGN KEY (supplier_id) REFERENCES Supplier (id),
                        FOREIGN KEY (department_id) REFERENCES Department (id)
                        );'''
        connection.execute(drop_is_exist_machine)
        connection.execute(creat_user_table)

    @staticmethod
    def insert_machine(machine):
        sql = ''' INSERT INTO Machine (id,name ,mark , machine_type ,supplier_id , department_id  )
                              VALUES(?, ?, ?,?, ?, ?) '''
        cursor = connection.cursor()
        cursor.execute(sql,
                       (machine.machine_id, machine.name, machine.mark, machine.machine_type, machine.supplier_id,
                        machine.department_id))
        fid = cursor.lastrowid
        connection.commit()
        return fid

    @staticmethod
    def get_all_machine():
        sql = '''SELECT * FROM  Machine'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

    @staticmethod
    def get_machine_by_id(id):
        sql = '''SELECT * FROM  Machine WHERE ID = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, str(id))
        row = cursor.fetchone()
        return row

    @staticmethod
    def delete(id):
        sql = '''DELETE FROM Machine WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, str(id))
        connection.commit()


if __name__ == '__main__':
    print('------------------------------Users--------------------------------')
    user1 = User(1, 'anasss', 'Moad', '0615923387', 'test@gmail.com', 'test')
    user2 = User(2, 'test', 'test', '1532468', 'fuckthisshitilout', 'lol')
    User.create_tables()
    User.insert_user(user1)
    User.insert_user(user2)
    print(User.get_All_users())
    User.delete(1)
    print(User.get_All_users())
    print(User.get_user_by_id(2))

    print("**************************************************************")
    print('------------------------------Deparetment--------------------------------')

    deparetment = Department(1, 'BLOC A', 'admins')
    deparetment2 = Department(2, 'BLOC B', 'users')
    Department.creat_tables()
    Department.insert_Department(deparetment)
    Department.insert_Department(deparetment2)
    print(Department.get_All_Department())
    print(Department.get_departement_by_id(2))
    Department.delete(2)
    print(Department.get_All_Department())

    print('***********************************************************************')
    print('------------------------------Machines--------------------------------')

    machine1 = Machine(1, 'alienware', 'DELL', 'laptop', 1, 1)
    machine2 = Machine(2, 'alitetude', 'HP', 'laptop', 2, 1)
    Machine.create_table()
    Machine.insert_machine(machine1)
    Machine.insert_machine(machine2)
    print(Machine.get_all_machine())
    # Machine.delete(2)
    print(Machine.get_all_machine())

    print('***********************************************************************')
    print('------------------------------Suppliers--------------------------------')

    supplier1 = Supplier(1, 'Ahmed Tsouli', '0621518265', 'ahmed@tsouli.com', 'Ntt data Maroc')
    supplier2 = Supplier(2, 'Fredrique sama', '69696969696969', 'GiveMeMoney@Please.now', 'Ntt data CEO')
    supplier3 = Supplier(3, 'Bonito codigo', '911911911911', 'HelpPlease@please.sp', 'Ntt data Spain')
    Supplier.create_tables()
    Supplier.insert_Supplier(supplier1)
    Supplier.insert_Supplier(supplier2)
    Supplier.insert_Supplier(supplier3)
    print(Supplier.get_All_suppliers())
    Supplier.delete(3)
    print(Supplier.get_supplier_by_id(3))


    def get_machine_by_Department(id):
        sql = '''SELECT m.mark FROM  Machine m, Department d WHERE M.department_id = d.id and  d.id =?'''
        cursor = connection.cursor()
        cursor.execute(sql, str(id))
        row = cursor.fetchall()
        return row


    def get_supplier_of_machine(id):
        sql = '''SELECT s.name FROM  Machine m, Supplier s WHERE M.supplier_id = s.id and  s.id =?'''
        cursor = connection.cursor()
        cursor.execute(sql, str(id))
        row = cursor.fetchall()
        return row


    print('**************************************************************')
    print('--------------------------Queries------------------------------')

    print('Machine who are located in the departement BLOC A(id=1) : ', get_machine_by_Department(1))
    print('Supplier of machine with id=2 :', get_supplier_of_machine(2))
