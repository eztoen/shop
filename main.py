from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

import uvicorn

from products_views import router as products_router
from users.views import router as users_router

app = FastAPI()
app.include_router(products_router)
app.include_router(users_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)