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
        cursor.close()
    
    # add methods here for interacting with the database
    def getCoffeeData(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT name, hour, cups FROM ocean.coffee')
        for (name, hour, cups) in cursor:
            print(name + ' ' + str(hour) + ' ' + str(cups))
        cursor.close()

    def addTemp(self):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO ocean.coffee (name, hour, cups) VALUES("connor", 0, 0)')
        self.connection.commit()
        cursor.close()

#def test():
#    mydb = mysql.connector.connect(host="localhost", user="server", password="Hackathon123%")

def main():
    print('---start---')
    database = db(host = '192.168.1.100')
    database.show_databases()
    database.getCoffeeData()

if __name__ == '__main__':
    main()
