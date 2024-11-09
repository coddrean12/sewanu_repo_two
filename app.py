#!C:\Users\HODEWU\Documents\Web_backend\Python\mysql_env\Scripts\python.exe
print("Content-Type: text/html\n\n")

import mysql.connector, cgi
from mysql.connector import Error

#HTML content

print("""
    <h1>PYTHON MYSQL</h1>
    <hr>
    <body bgcolor = 'orange'>
    <h1>CONTACT FORM</h1>
    <form action = "" method = "post">
        <label for="name">NAME:</label>
        <input type="text" id="name" name="name" required><br><br>
      
        <label for="school">SCHOOL:</label>
        <input type="text" id="school" name="school" required><br><br>
      
        <label for="email">EMAIL:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">PHONE:</label>
        <input type="text" id="phone" name="phone" required><br><br>
      
        <label for="comment">COMMENT:</label>
        <textarea id="comment" name="comment" required></textarea><br><br>
      
        <input type="Submit" value="Submit">
    <hr>
    </form>
    <h1>Action</h1>

    <form action = "" method = "post">
        <label for="id">Record id to Update/Delete: <label>
        <input type="text" id ="id" name="id"><br><br>
      
        <input type="submit" name="action" value="Update">
        <input type="submit" name="action" value="Delete">
        <input type="submit" name="action" value="View">
    </form>
          <hr>
        <h1 color = 'plum'>UPDATE</h1>
       <form action="" method = "post">
        <label for="name">Enter an id to be updated:</label>
      <input type="text" id ="id" name="id"><br><br>

        <label for="name">NAME:</label>
        <input type="text" id="name" name="name" required><br><br>
      
        <label for="school">SCHOOL:</label>
        <input type="text" id="school" name="school" required><br><br>
      
        <label for="email">EMAIL:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">PHONE:</label>
        <input type="text" id="phone" name="phone" required><br><br>
      
        <label for="comment">COMMENT:</label>
        <textarea id="comment" name="comment" required></textarea><br><br>
    
        <input type="submit" name="action" value="Update">
    </form>
    </body>
    """)

#Get form data
form = cgi.FieldStorage()

name = form.getvalue("name")
school = form.getvalue("school")
email = form.getvalue("email")
phone = form.getvalue("phone")
comment = form.getvalue("comment")
record_id = form.getvalue("id")
action = form.getvalue("action")

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="contact_dunis"
    )

    cursor = con.cursor()

    # Create operation
    if name and school and email and phone and comment and not record_id:
        cursor.execute("INSERT INTO contact (name, school, email, phone, comment) VALUES (%s, %s, %s, %s, %s)", (name, school, email, phone, comment))
        con.commit()
        print("<h1> RECORD INSERTED SUCCESFULLY </h1>")

    #Read operation
    elif action == "View" and record_id:
        cursor.execute("SELECT * FROM contact WHERE id = %s", (record_id,))
        result = cursor.fetchone()
        if result: 
            print(f"<h1>Record id {record_id}</h1>")
            print(f"Name: {result[1]}, School: {result[2]}, Email: {result[3]}, Phone: {result[4]}, Comment: {result[5]}")
        else:
                print("<h1>Record not found</h1>")

    #Update operation
    elif action == "Update" and record_id:
        if name or school or email or phone or comment:
            cursor.execute("""Update contact SET name = %s, school = %s, email = %s, phone = %s, comment = %s Where id = %s""", (name, school, email, phone, comment, record_id))
            con.commit()
            print("<h1> RECORD UPDATED SUCCESFULLY </h1>")
        else:
            print("<h1> NO DATA PROVIDED FOR UPDATE </h1>")

    #DELETE operation
    elif action == "Delete" and record_id:
        cursor.execute("DELETE FROM contact WHERE id = %s", (record_id,))
        con.commit()
        print("<h1>RECORED DELETED SUCCESFULLY</h1>")

except Error as e:
    print(f"<h1>Error: {e}</h1>")

except Exception as e:
    print(f"<h1>Error: {e}</h1>")

finally:
    if con.is_connected():
        cursor.close()
        con.close()