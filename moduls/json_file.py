import json
from personal_information import ID
from aiogram.types import Message

FILENAME = "schedule.json"


def load_schedule():
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_schedule(data):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def is_authorized(message: Message):
    return message.from_user.id == ID
