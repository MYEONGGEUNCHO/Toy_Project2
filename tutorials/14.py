'''
uvicorn 14:app --reload
'''
'''
Response Model - Return Type

response_model Parameter
'''

# from typing import List, Union

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: List[str] = []


# @app.post("/items/")
# async def create_item(item: Item) -> Item:
#     return item


# @app.get("/items/")
# async def read_items() -> List[Item]:
#     return [
#         Item(name="Portal Gun", price=42.0),
#         Item(name="Plumbus", price=32.0),
#     ]


'''
Return the same input data
'''
# from typing import Union

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# # Don't do this in production!
# @app.post("/user/")
# async def create_user(user: UserIn) -> UserIn:
#     return user


'''
Add an output model
'''
# from typing import Any, Union

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn) -> Any:
#     return user


'''
Return Type and Data Filtering
'''
# from typing import Union

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()


# class BaseUser(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# class UserIn(BaseUser):
#     password: str


# @app.post("/user/")
# async def create_user(user: UserIn) -> BaseUser:
#     return user


'''
Other Return Type Annotations
'''

# from fastapi import FastAPI, Response
# from fastapi.responses import JSONResponse, RedirectResponse

# app = FastAPI()


# @app.get("/portal")
# async def get_portal(teleport: bool = False) -> Response:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})

'''
Annotate a Response Subclass
'''
# from fastapi import FastAPI
# from fastapi.responses import RedirectResponse

# app = FastAPI()


# @app.get("/teleport")
# async def get_teleport() -> RedirectResponse:
#     return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

'''
Response Model encoding parameters

Use the response_model_exclude_unset parameter
'''
# from typing import List, Union

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: float = 10.5
#     tags: List[str] = []


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }


# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# async def read_item(item_id: str):
#     return items[item_id]


'''
Using lists instead of sets
'''
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include=["name", "description"],
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
async def read_item_public_data(item_id: str):
    return items[item_id]