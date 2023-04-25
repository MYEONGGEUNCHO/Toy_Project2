"""
Path Operation Advanced Configuration

uvicorn 01:app --reload

OpenAPI operationId
"""

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/", operation_id="some_specific_id_you_define")
# async def read_items():
#     return [{"item_id": "Foo"}]



'''
Using the path operation function name as the operationId
'''
# from fastapi import FastAPI
# from fastapi.routing import APIRoute

# app = FastAPI()


# @app.get("/items/")
# async def read_items():
#     return [{"item_id": "Foo"}]


# def use_route_names_as_operation_ids(app: FastAPI) -> None:
#     """
#     Simplify operation IDs so that generated API clients have simpler function
#     names.

#     Should be called only after all routes have been added.
#     """
#     for route in app.routes:
#         if isinstance(route, APIRoute):
#             route.operation_id = route.name  # in this case, 'read_items'


# use_route_names_as_operation_ids(app)


'''
Exclude from OpenAPI
'''
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/", include_in_schema=False)
# async def read_items():
#     return [{"item_id": "Foo"}]


'''
Advanced description from docstring
'''
# from typing import Set, Union

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: Set[str] = set()


# @app.post("/items/", response_model=Item, summary="Create an item")
# async def create_item(item: Item):
#     """
#     Create an item with all the information:

#     - **name**: each item must have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tag strings for this item
#     \f
#     :param item: User input.
#     """
#     return item


'''
Custom OpenAPI path operation schema
'''
# from fastapi import FastAPI, Request

# app = FastAPI()


# def magic_data_reader(raw_body: bytes):
#     return {
#         "size": len(raw_body),
#         "content": {
#             "name": "Maaaagic",
#             "price": 42,
#             "description": "Just kiddin', no magic here. ✨",
#         },
#     }


# @app.post(
#     "/items/",
#     openapi_extra={
#         "requestBody": {
#             "content": {
#                 "application/json": {
#                     "schema": {
#                         "required": ["name", "price"],
#                         "type": "object",
#                         "properties": {
#                             "name": {"type": "string"},
#                             "price": {"type": "number"},
#                             "description": {"type": "string"},
#                         },
#                     }
#                 }
#             },
#             "required": True,
#         },
#     },
# )
# async def create_item(request: Request):
#     raw_body = await request.body()
#     data = magic_data_reader(raw_body)
#     return data



'''
Custom OpenAPI content type
'''
# from typing import List

# import yaml
# from fastapi import FastAPI, HTTPException, Request
# from pydantic import BaseModel, ValidationError

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     tags: List[str]


# @app.post(
#     "/items/",
#     openapi_extra={
#         "requestBody": {
#             "content": {"application/x-yaml": {"schema": Item.schema()}},
#             "required": True,
#         },
#     },
# )
# async def create_item(request: Request):
#     raw_body = await request.body()
#     try:
#         data = yaml.safe_load(raw_body)
#     except yaml.YAMLError:
#         raise HTTPException(status_code=422, detail="Invalid YAML")
#     try:
#         item = Item.parse_obj(data)
#     except ValidationError as e:
#         raise HTTPException(status_code=422, detail=e.errors())
#     return item



'''

'''
from typing import List

import yaml
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, ValidationError

app = FastAPI()


class Item(BaseModel):
    name: str
    tags: List[str]


@app.post(
    "/items/",
    openapi_extra={
        "requestBody": {
            "content": {"application/x-yaml": {"schema": Item.schema()}},
            "required": True,
        },
    },
)
async def create_item(request: Request):
    raw_body = await request.body()
    try:
        data = yaml.safe_load(raw_body)
    except yaml.YAMLError:
        raise HTTPException(status_code=422, detail="Invalid YAML")
    try:
        item = Item.parse_obj(data)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    return item
