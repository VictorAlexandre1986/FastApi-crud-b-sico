from fastapi import APIRouter

from controllers import acao_controller


router = APIRouter()

router.include_router(acao_controller.router, prefix='/acao')