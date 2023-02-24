from fastapi import FastAPI
from .routers import plant_router, admin_router

# Declare the app
app = FastAPI()

# Add the router
app.include_router(plant_router.router)
app.include_router(
    admin_router.router,
    prefix="/admin",
    tags=["admin"]
)


# Add connection to SQL databases

