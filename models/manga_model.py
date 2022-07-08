#from psycopg2 import connection
from psycopg2._psycopg import connection
from database.db import get_connection
from .entities.Mangas import Manga

class MangaModel():

    @classmethod
    def get_mangas(self):
        try:
            connection=get_connection()
            mangas=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, log_date, name, last_read FROM public.mangas ORDER BY name")
                result_set=cursor.fetchall()

                for row in result_set:
                    manga=Manga(row[0],row[1],row[2],row[3])
                    mangas.append(manga.to_JSON())
            connection.close()
            return mangas
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_mangas_by_id(self,id):
        try:
            connection=get_connection()
            mangas=[]
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM public.get_manga_by_id({id})")
                result_set=cursor.fetchall()
                for row in result_set:
                    manga=Manga(row[0],row[1],row[2],row[3])
                    mangas.append(manga.to_JSON())
            connection.close()
            return mangas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_manga(self ,manga):
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute(f"CALL public.new_mangas(\'{manga.name}\', {manga.last_read})")
                #cursor.execute(f"INSERT INTO mangas(id, log_date, name,last_read)VALUES (DEFAULT, NOW(), \'{manga.name}\', {manga.last_read})")
                connection.commit()

            connection.close()
            return manga.to_JSON()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_manga(self ,manga):
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute(f"CALL public.upd_mangas({manga.id}, {manga.last_read})")

                connection.commit()

            connection.close()
            return manga.to_JSON()
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def delete_manga(self ,manga):
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute(f"CALL public.del_mangas({manga.id})")

                connection.commit()

            connection.close()
            return manga.to_JSON()
        except Exception as ex:
            raise Exception(ex)