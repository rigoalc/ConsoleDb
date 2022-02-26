import sqlite3

def create_tables(conn, c):
    c.execute("CREATE TABLE IF NOT EXISTS usernameage (name text, age integer)")
    c.execute("INSERT INTO usernameage VALUES ('MrBurns', 81), ('Apu', 41)")
    conn.commit()
def print_usernameage(conn, c):
    print(" -- Current usernameage in db --")
    for row in c.execute("SELECT * FROM usernameage"):
        name = row[0]
        age = row[1]
        print('{}: {}'.format(name, age))
    print(' --')
def get_usernameage(conn, c, usernameage):
    c.execute("SELECT name, age FROM usernameage WHERE name=?", [usernameage])
    row = c.fetchone()
    return row
def lookup_usernameage(conn, c):
    usernameage = input("Please enter the the new user name: ")
    found = get_usernameage(conn, c, usernameage)
    if found:
        name, age = found
        print('{}: {}'.format(name, age))
    else:
        print("Unable to find {}".format(usernameage))
def add_update_usernameage(conn, c):
    usernameage = input("Please enter the usernameage you would like to lookup: ")
    age = input("What is the age? ")
    age = int(age.strip() or '0')
    found = get_usernameage(conn, c, usernameage)
    if found:      
        c.execute("UPDATE usernameage SET age=? WHERE name=?", [age, usernameage])
    else:      
        c.execute("INSERT INTO usernameage VALUES (?, ?)", [usernameage, age]) 
    conn.commit() 
    print("{} has been added with age={}".format(usernameage, age))
def remove_usernameage(conn, c):
    usernameage = input("Please enter the usernameage you would like to remove: ")
    found = get_usernameage(conn, c, usernameage)
    if found:
        c.execute("DELETE FROM usernameage WHERE name=?", [usernameage])
        conn.commit() 
        print("{} has been removed".format(usernameage))
    else:
        print("Unable to find {}".format(usernameage))
def menu(conn, c):
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