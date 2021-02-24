# import sqlite3
#
#
# cursor = conection.cursor()



# cursor.execute( "CREATE TABLE users ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'username' text NOT NULL,'password' text NOT NULL)")
# cursor.execute( "CREATE TABLE iphones ('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'name' text NOT NULL,'price' INTEGER NOT NULL, 'quantity' INTEGER)")


# cursor.execute( "INSERT INTO users ('username' ,'password' )VALUES( 'admin5',	'passpass123' )")
# cursor.execute( "INSERT INTO iphones ('name' ,'price','quantity' )VALUES( 'Iphone 12 Pro',	999, 55 )")

# conection.commit()
# all_users = cursor.execute( "SELECT * from iphones").fetchall()
#
#
# def add_user(id,username,password):
#     cursor.execute("INSERT INTO users ('id','username' ,'password' )VALUES(?,?,?)",(id,username,password))
#     conection.commit()
#     return 'Yep'
#
#
#
# def add_phone(name, price, quantity):
#     cursor.execute("INSERT INTO iphones ('name','price' ,'quantity' )VALUES(?,?,?)", (name, price, quantity))
#     conection.commit()
#     return 'Yep'
