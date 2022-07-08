#from crypt import methods
from flask import Blueprint, jsonify, request
#Entities
from models.entities.Mangas import Manga
# Models
from models.manga_model import MangaModel

main=Blueprint('manga_blueprint',__name__)

@main.route('/')
def get_mangas():
    try:
        mangas=MangaModel.get_mangas()
        return jsonify(mangas)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
@main.route('/<id>')
def get_mangas_by_id(id):
    try:
        mangas=MangaModel.get_mangas_by_id(id)
        return jsonify(mangas)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
@main.route('/add',methods=['POST'])
def add_mangas():
    try:
        #print(request.json)
        name = request.json['title']
        last_read = request.json['last_read']
        manga = Manga(id,None,name,last_read)
        manga_json = MangaModel.add_manga(manga)
        print(manga_json)
        return manga_json
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/update',methods=['POST'])
def update_mangas():
    try:
        name = request.json['title']
        last_read = request.json['last_read']
        id = request.json['id']
        manga = Manga(id,None,name,last_read)
        manga_json = MangaModel.update_manga(manga)
        return manga_json
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/delete',methods=['POST'])
def delete_mangas():
    try:
        name = request.json['title']
        last_read = request.json['last_read']
        id = request.json['id']
        manga = Manga(id,None,name,last_read)
        manga_json = MangaModel.delete_manga(manga)
        return manga_json
    except Exception as ex:
        return jsonify({'message':str(ex)}),500