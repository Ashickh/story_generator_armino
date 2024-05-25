from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
import openai
import os
from dotenv import load_dotenv
from fastapi import status

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Get Supabase and OpenAI credentials from environment variables
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_ANON_KEY = os.getenv('SUPABASE_ANON_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
print(supabase,"supabase")

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY

# Character model for adding new characters
class Character(BaseModel):
    name: str
    details: str

@app.post("/api/create_character/", status_code=status.HTTP_201_CREATED)
def add_character(character: Character):
    response = supabase.table('characters').insert({'name': character.name, 'details': character.details}).execute()
    if 'error' in response:
        raise HTTPException(status_code=400, detail="Error adding character")
    return {"message": "Character added successfully", "character": character}


@app.get("/api/generate_story/", status_code=status.HTTP_201_CREATED)
def generate_story(name: str):
    response = supabase.table('characters').select('*').eq('name', name).execute()
    if len(response.data) == 0:
        raise HTTPException(status_code=404, detail="Character not found")

    character = response.data[0]
    prompt = (
        f"{character['name']}, a cheerful {character['details']}, lived a quiet life in the peaceful land of the Shire. "
        f"Unbeknownst to many, he owned a mysterious magic ring, which he stumbled upon during one of his adventures. "
        f"This ring granted him the ability to become invisible, a secret he kept close to his heart. "
        f"Though content with his simple life, {character['name']} often daydreamed about the adventures the ring could lead him to. "
        f"Little did he know, destiny had grand plans for him and his magical possession."
    )

    openai_response = openai.Completion.create(
        engine="gpt-3.5-turbo-0613",
        prompt=prompt,
        max_tokens=150
    )

    story = openai_response.choices[0].text.strip()
    return {"story": story}


