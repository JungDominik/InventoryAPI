from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str]=None

class UpdateItem(BaseModel):
    name:Optional[str] = None
    price:Optional[float] = None
    brand:Optional[str]=None


inventory_dic = {


}



@app.get("/")
def home():
    return {
        "Data":"Test",
        "Hello": "May You be safe and happy"}


@app.get("/about")
def about():
    return {"data":"about"}


@app.get("/get-all")
def get_all():
    return "Here is the content of InventoryDic: ", inventory_dic



@app.get("/get-item/{item_id}/{price}")
def get_item(item_id:int = Path(
    None,
    description="The ID for the item youd like to view")
    ):
    return inventory_dic[item_id]


@app.get("/get-by-name")
def get_item(*, name:str = None, test:int=None): #Setting it to None makes the URL-Queryparamter "?name=xyz" optional. If it is there it will be searched, if not the query works nevertheless.
    for item_id in inventory_dic:
        if inventory_dic[item_id].name==name:
            return inventory_dic[item_id]
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail =  "ItemID not found in inventory")


# @app.post("/create-item/{item_id}")
# def create_item(item_id: int, my_item:Item):
#     if item_id in inventory_dic:
#         return {"Error": "Item ID already Exists"}
    
#     inventory_dic[item_id] = {"name":my_item.name, "brand":my_item.brand, "price":my_item.price}
#     return inventory_dic[item_id] #Return as confirmation

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory_dic:
        raise HTTPException(status_code = 400, detail =  "Item ID already exists.")
        
    
    inventory_dic[item_id] = item
    return "This was successful",  inventory_dic[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item:UpdateItem):
    
    if item_id not in inventory_dic: 
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail =  "ItemID not found in inventory")
    else:

        if item.name != None:
            inventory_dic[item_id].name = item.name    
        
        if item.price != None:
            inventory_dic[item_id].price = item.price
        
        if item.brand != None:
            inventory_dic[item_id].brand = item.brand
        
        return "Item was updated."

@app.delete("/delete/{item_id}")
def delete_item(item_id:int):
    if item_id not in inventory_dic: 
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail =  "Cannot delete, ItemID is not in inventory")
    else:
        del inventory_dic[item_id]

