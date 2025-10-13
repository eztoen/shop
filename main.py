from fastapi import FastAPI

import uvicorn

from contextlib import asynccontextmanager

from core.models import Base, async_engine
from products.views import router as products_router
from users.views import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
   
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(products_router)
app.include_router(users_router)



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)