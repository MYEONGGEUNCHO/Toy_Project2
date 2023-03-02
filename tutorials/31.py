"""
uvicorn 31:app --reload

Metadata and Docs URLs
"""
from fastapi import FastAPI

description = """
MgchoApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="MgchoApp",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deondre",
        "url": "https://github.com/MYEONGGEUNCHO/",
        "email": "lightkeun@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/items/")
async def read_items():
    return [{"name": "Deondre"}]