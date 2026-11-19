from fastapi import FastAPI
from backend.rag import rag_agent
from backend.data_models import Prompt
import logfire

app = FastAPI()

# in .env
# LOGFIRE_TOKEN=...

logfire.configure()
logfire.instrument_pydantic_ai()
logfire.instrument_fastapi(app)


@app.post("/rag/query")
async def query_documentation(query: Prompt):
    result = await rag_agent.run(query.prompt)

    return result.output
