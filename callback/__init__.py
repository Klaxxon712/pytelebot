__all__ = ("router")

from aiogram import Router

from .bomber import router as bom
from .cs import router as cs
from .cfg import router as cfg
from .back import router as back

router = Router(name=__name__)

router.include_router(bom)
router.include_router(cs)
router.include_router(cfg)
router.include_router(back)
