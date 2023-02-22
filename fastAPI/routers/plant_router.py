from fastapi import APIRouter

router = APIRouter(
    prefix="/plant",
    tags=["plants"],
    responses={
        401: {"description": "Missing Auth Headers, thus the pettion is forbidden"},
        403: {"description": "Error"},
        404: {"description": "Item not found."},
        500: {"description": "Internal Server Error"}
    })


@router.get("/")
async def return_all_plants():
    return 1


@router.get("/{item_id}")
async def return_plant_by_id(item_id: int):
    return "This is the id of the plant -> 1"


@router.get("/{item_name}")
async def return_plant_by_id(item_name: str):
    return "This is the name of the plant -> El Cactus"
