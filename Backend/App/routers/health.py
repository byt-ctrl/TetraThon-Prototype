from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
@router.get("/api/health")
def health():
    return {"status": "OK"}
