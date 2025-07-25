from sqlalchemy import select, delete

from database import new_session, UsersDB
from schemas import UsersAdd, Users



class UserRepo:
    @classmethod
    async def add_user(cls, data: UsersAdd) -> int:
        async with new_session() as session:
            user_dict = data.model_dump()

            user = UsersDB(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id


    @classmethod
    async def get_all(cls) -> list[Users]:
        async with new_session() as session:
            query = select(UsersDB)
            result = await session.execute(query)
            user_models = result.scalars().all()
            user_schemas = [Users.model_validate(user_model.__dict__) for user_model in user_models]
            return user_schemas

