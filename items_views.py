from typing import Annotated

from fastapi import Path, APIRouter

router = APIRouter(prefix="/items")


@router.get("/")
def list_items():
    return [
        "item1",
        "item2",
    ]


@router.get("/latest/")
def get_lastest_item():
    return {
        "item": {"id": "0", "name": "latest"}
    }


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id,
        },
    }
