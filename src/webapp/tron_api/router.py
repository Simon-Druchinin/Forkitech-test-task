from fastapi import APIRouter


router = APIRouter(prefix="tron_api/", tags=["Tron API"])


@router.get("")
async def get_
