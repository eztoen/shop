from fastapi import FastAPI

from core.models import Base, db_helper
from users.views import router as users_router
from products.views import router as products_router

from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
   
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(products_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)