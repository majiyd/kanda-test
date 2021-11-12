from os import error
from marshmallow import Schema, fields, validate

fields.Field.default_error_messages["required"] = "This is required"


class SignupSchema(Schema):

    """Schema for validating signups"""
    first_name = fields.Str(required=True, error_messages={
                            "invalid": "Invalid field type"})
    last_name = fields.Str(required=True, error_messages={
        "invalid": "Invalid field type"})
    email = fields.Email(required=True,  error_messages={
        "invalid": "Invalid email format"})

    # looks like test cases did not consider regex
    # password = fields.Str(required=True, validate=[validate.Length(
    #     min=8, error="Password must at least be 8 characters"), validate.Length(max=50, error="Password must not be greater than 50 characters"), validate.Regexp(r"^(?=\D*\d)(?=.*?[a-zA-Z]).*[\W_].*$", error="Password must have at least one letter, number, and special character")])

    password = fields.Str(required=True, validate=[validate.Length(
        min=8, error="Password must at least be 8 characters"), validate.Length(max=50, error="Password must not be greater than 50 characters")])
