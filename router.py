from typing import Annotated

from fastapi import APIRouter, Depends

from repo import UserRepo
from schemas import UsersAdd, Users, UsersID

router = APIRouter(
    prefix="/Users",
    tags = ["Tasks"]
)


@router.post("")
async def add_users(
        user: Annotated[UsersAdd, Depends()]

) -> UsersID:
    user_id = await UserRepo.add_user(user)
    return {"ok": True, "user_id": user_id}


@router.get("")
async def get_user() -> list[Users]:
    users = await UserRepo.get_all()
    return users
