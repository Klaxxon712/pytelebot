__all__ = ("router")

from aiogram import Router

from .main import router as usr

router = Router(name=__name__)

router.include_routers(usr)