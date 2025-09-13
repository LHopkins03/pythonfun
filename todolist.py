import sqlite3
conn = sqlite3.connect('todolist.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS todolist (id INTEGER PRIMARY KEY, description TEXT)''')

def additem():
    itemdescription = input('Enter item description:\n')
    c.execute('INSERT INTO todolist (description) VALUES (?)', (itemdescription,))
    conn.commit()

def removeitem():
    itemid = input('Enter item id:\n')
    c.execute('DELETE FROM todolist WHERE id = ?', (itemid,))
    conn.commit()

def display():
    for row in c.execute('SELECT * FROM todolist'):
        print(row)

keepgoing = True
while keepgoing:
    display()
    choice = input('Enter (1) to add a new item, enter (2) to remove an item, enter (q) to quit:\n')
    if choice == '1':
        additem()
    elif choice == '2':
        removeitem()
    elif choice == 'q':
        keepgoing = False