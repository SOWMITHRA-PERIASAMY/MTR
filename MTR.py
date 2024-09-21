 
import mysql.connector 
 
# Replace 'your_database_info' with your actual MySQL database information 
 
db=mysql.connector.connect(host="localhost",user="root",password="1234", database="movieres")
cursor = db.cursor() 
 
# Create a table for movies 
 
cursor.execute("""CREATE TABLE IF NOT EXISTS movies 
(id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) NOT NULL, description TEXT )""") 
db.commit() 
 
# Create a table for users 
 
cursor.execute("""CREATE TABLE IF NOT EXISTS users 
(id INT PRIMARY KEY,username VARCHAR(255) UNIQUE NOT NULL,password_hash VARCHAR(255) NOT NULL)""") 
db.commit() 
 
# Create a table for reservations 
 
cursor.execute("""CREATE TABLE IF NOT EXISTS reservations 
    (id INT AUTO_INCREMENT PRIMARY KEY,         user_id INT, 
        movie_id INT, 
        FOREIGN KEY (user_id) REFERENCES users(id),         FOREIGN KEY (movie_id) REFERENCES movies(id))""")
db.commit() 
 
def display_movies(): 
     
 cursor.execute("SELECT * FROM movies")    
 movies = cursor.fetchall() 
 for movie in movies: 
      print(f"{movie[0]}. {movie[1]} - {movie[2]}") 
 
 
 
 
 
 
def user_login(): 
    
 username = input("Enter your username: ")
 password = input("Enter your password: ") 
 cursor.execute("SELECT * FROM users WHERE username = %s", (username,))    
 user = cursor.fetchone() 
 
if user and user[2] == password: 
        print("Login successful!") 
        #return user[0]      # type: ignore
else: 
        print("Invalid username or password.")      
        #return None          # type: ignore

 
def signin(): 
    username = input("Enter your username: ") 
    password = input("Enter your password: ") 
 
    # Manually specify the user ID  

userid = input("Enter the desired user ID: ") 
password_hash = password 
 
cursor.execute("INSERT INTO users (userid, username, password_hash) VALUES (%s, %s, %s)"
, (user_id, username, password_hash))
db.commit() 

print("USER SIGNIN SUCCESSFULL"); 
 
def make_reservation(user_id): 
    display_movies() 
    movie_id = input("Enter the ID of the movie you want to reserve: ") 
 
    cursor.execute("INSERT INTO reservations (user_id, movie_id) VALUES (%s, %s)", 
(user_id, movie_id)) 
    db.commit() 
 
    print("Reservation successful!") 
 
 
def insert_movie(): 
     
 title = input("Enter the title of the movie: ") 
description = input("Enter the description of the movie: ") 
cursor.execute("INSERT INTO movies (title, description) VALUES (%s, %s)", (title, 
description)) 
db.commit() 
print("Movie added successfully!") 
def main():     
    user_id = None 
while True: 
        print("\n1. Login")      
        print("2. Display Movies")    
        print("3. Make Reservation") 
        print("4. Exit")        
        print("5.Signin") 
        print("6.insert_movie") 
 
        choice = input("Enter your choice: ") 
 
        if choice == "1": 
            user_id = user_login()     
        elif choice == "2":      
             display_movies()    
        elif choice == "3":           
             if user_id:             
                    make_reservation(user_id)
             else: 
                print("Please login first.")          
       
        
      
        elif choice == "5":       
            signin()        
        elif choice == "6":          
             insert_movie()   
        elif choice == "4": 
            break       
        else: 
            print("Invalid choice. Please try again.") 
 
if __name__ == '__main__': 
    main()


