from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from router import router as users_router
from database import delete_tables, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DB cleaned")
    await create_tables()
    print("DB is ready")

    yield
    print("Turning off")


app = FastAPI(lifespan= lifespan)
app.include_router(users_router)

