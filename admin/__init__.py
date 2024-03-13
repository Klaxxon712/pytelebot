__all__ = ("router")

from aiogram import Router

from .main import router as cmd 

router = Router(name=__name__)

router.include_router(cmd)