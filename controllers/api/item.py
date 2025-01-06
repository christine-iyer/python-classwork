from models.item import Item

async def create_item(item: Item):
    await item.insert()
    return item

async def get_items():
    return await Item.find_all().to_list()


