'''
uvicorn 07:app --reload
'''
'''
Body - Multiple Parameters
'''
'''
Mix Path, Query and body parameters
'''
# from typing import Union

# from fastapi import FastAPI, Path
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(None, title="The ID of the item to get", ge=0, le=1000),
#     q: Union[str, None] = None,
#     item: Union[Item, None] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results

'''
Singular values in body
'''
# from typing import Union

# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None


# class User(BaseModel):
#     username: str
#     full_name: Union[str, None] = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User, importance: int = Body(None)):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results

'''
Multiple body params and query
'''
# from typing import Union

# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None


# class User(BaseModel):
#     username: str
#     full_name: Union[str, None] = None


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: int = Body(None, gt=0),
#     q: Union[str, None] = None
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results

'''
Embed a single body parameter
'''
from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(None, embed=True)):
    results = {"item_id": item_id, "item": item}
    return results