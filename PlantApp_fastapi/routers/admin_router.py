from fastapi import APIRouter
from PlantApp_fastapi.models.models import Plant

router = APIRouter(
    prefix="/management",
    responses={
        401: {"description": "Missing Auth Headers, thus the pettion is forbidden"},
        403: {"description": "Error"},
        404: {"description": "Item not found."},
        500: {"description": "Internal Server Error"}
    })


@router.get("/")
async def return_info():
    return 2


@router.post("/")
async def create_new_plant(plant: Plant):
    return "Post of Admin"


@router.put("/{item_id}")
async def change_attributes(item_id: int, plant: Plant):
    return "Put of Admin"
