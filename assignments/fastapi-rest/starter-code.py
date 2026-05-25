from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# Simple in-memory store
db: Dict[int, Item] = {}


@app.get('/items', response_model=List[Item])
def list_items():
    return list(db.values())


@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int):
    item = db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    return item


@app.post('/items', response_model=Item)
def create_item(item: Item):
    if item.id in db:
        raise HTTPException(status_code=400, detail='ID already exists')
    db[item.id] = item
    return item


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
