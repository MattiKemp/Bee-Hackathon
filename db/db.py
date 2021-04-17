import mysql.connector
# link to tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp

class db:
    def __init__(self, host = "localhost", user = "server", password = "Hackathon123%"):
        self.host = host
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host,user=user,password=password)

    def show_databases(self):
        cursor = self.connection.cursor()
        cursor.execute("SHOW DATABASES")
        for x in cursor:
            print(x)
    
    # add methods here for interacting with the database 

#def test():
#    mydb = mysql.connector.connect(host="localhost", user="server", password="Hackathon123%")

def main():
    print('---start---')
    database = db()
    database.show_databases()

if __name__ == '__main__':
    main()
