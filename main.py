from fastapi import FastAPI
from duckduckgo_search import DDGS
from fastapi.responses import JSONResponse
from fastapi.openapi import openapi_url

app = FastAPI(
    title="Chat API",
    description="API để thực hiện cuộc trò chuyện",
    version="1.0.0",
)

@app.get("/openapi.json")
async def get_openapi():
    return await openapi_url(app)

@app.get("/chat/")
async def chat(query: str):
    """
    Thực hiện cuộc trò chuyện với mô hình GPT-4o-mini

    Args:
        query (str): Câu hỏi hoặc thông điệp để gửi đến mô hình

    Returns:
        JSONResponse: Kết quả của cuộc trò chuyện
    """
    results = DDGS().chat(query, model='gpt-4o-mini')
    return JSONResponse(content={"results": results})
