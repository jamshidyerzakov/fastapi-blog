from typing import Optional

from src.app.auth.security import verify_password, get_password_hash

from . import schemas, models
from ..base.base_service import BaseService


class UserService(BaseService):
    model = models.User
    create_schema = schemas.UserCreateInRegistration
    get_schema = schemas.User_G_Pydantic

    async def create_user(self, schema: schemas.UserCreateInRegistration, **kwargs):
        hash_password = get_password_hash(schema.dict().pop("password"))
        return await self.create(
            schemas.UserCreateInRegistration(
                **schema.dict(exclude={"password"}), password=hash_password, **kwargs
            )
        )

    async def authenticate(self, username: str, password: str) -> Optional[models.User]:
        user = await self.model.get(username=username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    async def change_password(self, obj: models.User, new_password: str):
        hashed_password = get_password_hash(new_password)
        obj.password = hashed_password
        await obj.save()

    async def create_user_social(self, user: schemas.UserCreateInRegistration):
        return await self.create_user(schema=user, is_active=True)

    def create_superuser(self, user: schemas.UserCreateInRegistration):
        return self.create_user(schema=user, is_active=True, is_superuser=True)