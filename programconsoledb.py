# KVCC 
# CIS-226-23199
# Advanced Python Programming
# 02/27/2022

'''
Design: How will you solve the problem?
I will solve this problem by using the sqlite3 library.  I follow the code example and the lessons to
finish completing a code that in a list it will create a db, add new records, select records, add, update, or delete them.
Develop:
I created a GIT repository, and then in the local folder create a virtual environment, and import the sqlite3 library. 
The code NOT allow SQL Injection for avoid loos data in case the user input a wrong SQL statement.
Test:
To test i created a test file and a function in the code file for asserting a simple calculation using a virtual environment running pytest from the terminal. 
How to use the program:
On the terminal: Follow the prompts to Look, Search, Create, edit or delete usernames and age of the username in a database.
The development time for this assignment is 6hrs. 
'''

'''
RUN THE TEST:
on the terminal:
python3 -m venv venv
. venv/bin/activate
pip install pytest
pytest
'''

# Import SQLite Library
import sqlite3  

#Test Function
def add(x, y):
        return x + y  
if __name__ == '__main__':
     
    
#Create tables
    def create_tables(conn, c):
        c.execute("CREATE TABLE IF NOT EXISTS usernameage (name text, age integer)")
        c.execute("INSERT INTO usernameage VALUES ('MrBurns', 81), ('Apu', 41)")#Instert first 2 values
        conn.commit() #Save the work
    def print_usernameage(conn, c):#Function to print username and age
        print(" -- Current usernameage in db --")
        for row in c.execute("SELECT * FROM usernameage"):#Select all from database 
            name = row[0]
            age = row[1]
            print('{}: {}'.format(name, age))
        print(' --')
    def get_usernameage(conn, c, usernameage):#Function to select up username
        c.execute("SELECT name, age FROM usernameage WHERE name=?", [usernameage])
        row = c.fetchone()
        return row
    def lookup_usernameage(conn, c):#Function to show or not the results
        usernameage = input("Please enter the the user name you would like to lookup:: ")
        found = get_usernameage(conn, c, usernameage)
        if found:
            name, age = found
            print('{}: {}'.format(name, age))
        else:
            print("Unable to find {}".format(usernameage))
    def add_update_usernameage(conn, c):#Function to add a username
        usernameage = input("Please enter the new username: ")
        age = input("What is the age? ")
        age = int(age.strip() or '0')
        found = get_usernameage(conn, c, usernameage)
        if found:      
            c.execute("UPDATE usernameage SET age=? WHERE name=?", [age, usernameage])
        else:      
            c.execute("INSERT INTO usernameage VALUES (?, ?)", [usernameage, age]) 
        conn.commit() 
        print("{} has been added with age={}".format(usernameage, age))
    def remove_usernameage(conn, c):#Function to delete a username if exist
        usernameage = input("Please enter the username you would like to remove: ")
        found = get_usernameage(conn, c, usernameage)
        if found:
            c.execute("DELETE FROM usernameage WHERE name=?", [usernameage])
            conn.commit() 
            print("{} has been removed".format(usernameage))
        else:
            print("Unable to find {}".format(usernameage))
    def menu(conn, c):#Function to prompt a user menu
        running = True
        while running:
            print("    1) Show all user name and age.")
            print("    2) Lookup for user age")
            print("    3) Add/Update user age")
            print("    4) Remove user")
            print("    0) Quit")
            response = input("\n> ")
            if response == '1':
                print_usernameage(conn, c)
            elif response == '2':
                lookup_usernameage(conn, c)
            elif response == '3':
                add_update_usernameage(conn, c)
            elif response == '4':
                remove_usernameage(conn, c)
            elif response.lower() in ['0', 'quit', 'exit']:
                print("Goodbye")
                running = False
            if running:               
                input("Press Enter to see Menu")
    def main():
        with sqlite3.connect(':memory:') as conn:
            c = conn.cursor()
            create_tables(conn, c)
            menu(conn, c)
    main()