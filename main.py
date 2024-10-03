from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

model_name = "facebook/blenderbot-400m-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

app = FastAPI()

origins = [
    "https://elodrigo.com",
    "https://www.elodrigo.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    inputs: str


@app.get("/my_chatbot/")
def read_root():
    return {"Hello": "World"}


@app.post("/my_chatbot/chat")
async def post_msg(item: Item):
    inputs = tokenizer(item.inputs, return_tensors="pt")
    reply_ids = model.generate(**inputs)
    return {"msg": (tokenizer.decode(reply_ids[0], skip_special_tokens=True))}
    # return {"msg": item.inputs}
