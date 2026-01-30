from flask_restful import Resource, reqparse, fields, marshal_with,abort
from models import db, UserModel

#parser for validation
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="User name cannot be blank")
user_args.add_argument('email',type=str,required=True, help="Email cannot be blank")

#patch parser
patch_args = reqparse.RequestParser()
patch_args.add_argument('name', type=str)
patch_args.add_argument('email',type=str)

#output formating
userField={
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String
}

class Users(Resource):
    @marshal_with(userField)
    def get(self):
        users = UserModel.query.all()
        return users
    
    @marshal_with(userField)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args['name'], email=args['email'])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201

class User(Resource):
    @marshal_with(userField)
    def get(self,id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User Not Found")
        return user
        
    @marshal_with(userField)
    def patch(self,id):
        args = patch_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not Found")

        if args['name']:
            user.name = args['name']
            
        if args['email']:
            user.email = args['email']
        
        db.session.commit()
        return user
    
    @marshal_with(userField)
    def delete(self,id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User Not Found")
        
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users
