from marshmallow import fields, Schema

class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)


