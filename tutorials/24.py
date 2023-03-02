"""
uvicorn 24:app --reload

First Steps
"""
# from typing import Union

# from fastapi import Depends, FastAPI

# app = FastAPI()


# async def common_parameters(
#     q: Union[str, None] = None, skip: int = 0, limit: int = 100
# ):
#     return {"q": q, "skip": skip, "limit": limit}


# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons


# @app.get("/users/")
# async def read_users(commons: dict = Depends(common_parameters)):
#     return commons

"""
Classes as Dependencies
"""
# from typing import Union

# from fastapi import Depends, FastAPI

# app = FastAPI()


# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# class CommonQueryParams:
#     def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
#         self.q = q
#         self.skip = skip
#         self.limit = limit


# @app.get("/items/")
# async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
#     response = {}
#     if commons.q:
#         response.update({"q": commons.q})
#     items = fake_items_db[commons.skip : commons.skip + commons.limit]
#     response.update({"items": items})
#     return response

"""
Sub-dependencies
"""
# from typing import Union

# from fastapi import Cookie, Depends, FastAPI

# app = FastAPI()


# def query_extractor(q: Union[str, None] = None):
#     return q


# def query_or_cookie_extractor(
#     q: str = Depends(query_extractor),
#     last_query: Union[str, None] = Cookie(default=None),
# ):
#     if not q:
#         return last_query
#     return q


# @app.get("/items/")
# async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
#     return {"q_or_cookie": query_or_default}

"""
Dependencies in path operation decorators
"""
# from fastapi import Depends, FastAPI, Header, HTTPException

# app = FastAPI()


# async def verify_token(x_token: str = Header()):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token header invalid")


# async def verify_key(x_key: str = Header()):
#     if x_key != "fake-super-secret-key":
#         raise HTTPException(status_code=400, detail="X-Key header invalid")
#     return x_key


# @app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
# async def read_items():
#     return [{"item": "Foo"}, {"item": "Bar"}]


"""
Global Dependencies
"""
from fastapi import Depends, FastAPI, Header, HTTPException


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

"""
Dependencies with yield
"""