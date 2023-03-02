'''
uvicorn 06:app --reload
'''
'''
Path Parameters and Numeric Validations
'''
# from typing import Union

# from fastapi import FastAPI, Path, Query

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(None, title="The ID of the item to get"),
#     q: Union[str, None] = Query(default=None, alias="item-query"),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

'''
Declare metadata
'''
# from typing import Union

# from fastapi import FastAPI, Path, Query

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(None, title="The ID of the item to get"),
#     q: Union[str, None] = Query(default=None, alias="item-query"),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

'''
Order the parameters as you need
'''
# from fastapi import FastAPI, Path

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(*, item_id: int = Path(None, title="The ID of the item to get"), q: str):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

'''
Number validations: greater than or equal
'''
# from fastapi import FastAPI, Path

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     *, item_id: int = Path(None, title="The ID of the item to get", ge=1), q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

'''
Number validations: greater than and less than or equal
'''
# from fastapi import FastAPI, Path

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     *,
#     item_id: int = Path(None, title="The ID of the item to get", gt=0, le=1000),
#     q: str,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

'''
Number validations: floats, greater than and less than
'''
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(None, title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(None, gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
