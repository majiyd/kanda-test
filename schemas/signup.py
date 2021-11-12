from marshmallow import Schema, fields


class SignupSchema(Schema):
    """Schema for validating signups"""
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
