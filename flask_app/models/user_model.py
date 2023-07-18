from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE    # this is sotred in my init.py

# user.py
class User:                        
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at =data['created_at']
        self.updated_at = data['updated_at']

#CRUD METHOD

    @classmethod 
    def get_all(cls):   #Getting all the Users
            query = """
                SELECT *FROM users;
            """
            results = connectToMySQL(DATABASE).query_db(query)
            print(results)
            all_users = []      #This is the user object !IMPORTANT FOR TEST
            for row_from_db in results:
                user_instance = cls(row_from_db)
                all_users.append(user_instance)
            return all_users    #THIS IS RETURNING THE USERS OBJECT



        
    @classmethod
    def create(cls, data):       #CREATE  WILL BE USING "INSERT" FOR THIS METHOD
            query = """
                INSERT into users (first_name, last_name,email)  
                VALUES (%(first_name)s, %(last_name)s, %(email)s);
            """
            return connectToMySQL(DATABASE).query_db(query,data)
            
    

    @classmethod
    def get_one(cls,data):     #Getting one user from the db
        query = """
            SELECT * FROM users WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:        #Asking if results comes back empty i didnt find my results
            user_instance = cls(results[0])    #Telling it to give back user in index[0]
            return user_instance
        return results    


    @classmethod
    def update(cls,data): #Update method.... all updates needs a where to find the information to change
        query = """
            UPDATE users SET first_name = %(first_name)s, last_name= %(last_name)s, email= %(email)s
            WHERE users.id = %(id)s;
        """
        return  connectToMySQL(DATABASE).query_db(query,data)     #updates dont return anything just run the queryand data
    

    @classmethod
    def delete(cls, data):
        query ="""
            DELETE FROM users WHERE id = %(id)s
        """
        return  connectToMySQL(DATABASE).query_db(query,data)     #deletes dont return anything just run the queryand data

