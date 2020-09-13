from tortoise import fields, models


class User(models.Model):
    """ Model user """
    username = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100, null=True)
    image = fields.CharField(max_length=100, null=True)
    bio = fields.TextField(null=True)
    date_join = fields.DatetimeField(auto_now_add=True)
    last_login = fields.DatetimeField(null=True)

    is_active = fields.BooleanField(default=False)
    is_staff = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)
