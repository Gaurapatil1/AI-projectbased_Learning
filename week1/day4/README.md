# Day 4 -- AI Engineering 🤖

## Topic

**Structured JSON Output using Groq + Pydantic**

### 1. Load API Key

``` python
load_dotenv()
api_key=os.getenv('GROQ_API_KEY')
```

Reads API key from `.env`.

### 2. Groq Client

``` python
client=Groq(api_key=api_key)
```

Connects Python to Groq.

### 3. Pydantic Model

``` python
class Ticket(BaseModel):
    name:str
    email:str
    issue:str
```

Defines expected output.

### 4. JSON Schema

``` python
schema=Ticket.model_json_schema()
```

Tells AI the required JSON format.

### 5. Force JSON Output

``` python
response_format={'type':'json_object'}
```

Returns JSON instead of text.

### 6. System Prompt

Gives instructions to the AI.

### 7. Parse JSON

``` python
data=json.loads(answer)
```

Converts JSON string to Python dictionary.

### 8. Validate

``` python
ticket=Ticket(**data)
```

Checks data format.

### 9. Access Values

``` python
print(ticket.name)
print(ticket.email)
print(ticket.issue)
```

## Workflow

``` text
Ticket → Groq AI → JSON → json.loads() → Pydantic → Python Object
```

## Key Learnings

-   Pydantic = Data validation
-   JSON Schema = Output format
-   System Prompt = AI instructions
-   response_format = JSON output
-   json.loads() = JSON → Dictionary
