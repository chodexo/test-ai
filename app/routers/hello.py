from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "Hello, Danilo!"}


@router.get("/hello/{name}")
def hello_name(name: str) -> dict[str, str]:
    return {"message": f"Hello, {name}!"}
