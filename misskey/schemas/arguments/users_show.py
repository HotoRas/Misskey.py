from marshmallow import Schema, fields

__all__ = (
    "UsersShowSchema",
)


class UsersShowSchema(Schema):
    user_id = fields.String(data_key="userId")
    user_ids = fields.List(fields.String(), data_key="userIds")
    username = fields.String()
    host = fields.String(allow_none=True)

    # TODO: validate
