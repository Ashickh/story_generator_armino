# FastAPI Story Generator

This project is a FastAPI application that allows users to create characters and generate short stories about them using the OpenAI API and Supabase as the backend database.

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Ashickh/story_generator_armino
    ```

2. **Create and activate a virtual environment**:
    ```sh
    pip install pipenv
    pipenv shell
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add your Supabase URL and API keys, as well as your OpenAI API key:
    ```env
    SUPABASE_URL=your_supabase_url
    SUPABASE_KEY=your_supabase_key
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run the FastAPI application**:
    ```sh
    uvicorn main:app --reload
    ```

## API Endpoints

### 1. Create a Character

**Endpoint**: `/api/create_character/`

**Method**: `POST`

**Request Body**:
```json
{
  "name": "Bilbo Baggins",
  "details": "Hobbit lives in the Shire owning a magic ring"
}

**Response 201**:
{
  "message": "Character added successfully",
  "character": {
    "name": "Bilbo Baggins",
    "details": "Hobbit lives in the Shire owning a magic ring"
  }
}



### 2. Fetch Story

**Request Body**:

**Endpoint**: `/api/generate_story/?name=Bilbo Baggins`

**Response 201**:
{
  "story": "Bilbo Baggins, a cheerful Hobbit, lived a quiet life in the peaceful land of the Shire. Unbeknownst to many, he owned a mysterious magic ring, which he stumbled upon during one of his adventures. This ring granted him the ability to become invisible, a secret he kept close to his heart. Though content with his simple life, Bilbo often daydreamed about the adventures the ring could lead him to. Little did he know, destiny had grand plans for him and his magical possession."
}


