from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 3:
            flash("location must be at least 3 characters.")
            is_valid = False
        if len(dojo['language']) < 2:
            flash("language must be 200 or greater.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid

    @classmethod
    def add_dojo( cls , data ):
        query = "INSERT INTO dojos (name, location, language, comment, created_at , updated_at ) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s,NOW(),NOW());"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

    @classmethod
    def get_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)