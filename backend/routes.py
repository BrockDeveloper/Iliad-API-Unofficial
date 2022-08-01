from fastapi import APIRouter
from backend import endpoints



router = APIRouter()
router.include_router(endpoints.router)