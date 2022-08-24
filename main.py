from flask import Flask, request
from flask_restful import Api, Resource , reqparse

app = Flask(__name__)
api = Api(app)

album_put_arge = reqparse.RequestParser()
album_put_arge.add_argument("name", type=str, help="Name of the album required", required=True)
album_put_arge.add_argument("song", type=str, help="name of the song required", required=True)
album_put_arge.add_argument("streams", type=str, help="streams on the video required", required=True)

album = {}

class album(Resource):
    def get(self, album_id):
        return album[album_id]

    def put(self, album_id):
        args = album_put_arge.parse_args()
        album[album_id] = args
        return album[album_id], 201

api.add_resource(album, "/album/<int:album_id>")

if __name__ == "__main__":
    app.run(debug=True)
