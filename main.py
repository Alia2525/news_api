from fastapi import FastAPI, HTTPException
from models import News
from data import news_list

app = FastAPI()


@app.get("/")
def home():
    return {"message": "News API працює"}


@app.get("/news")
def get_all_news():
    return news_list


@app.get("/news/{news_id}")
def get_news_by_id(news_id: int):
    for news in news_list:
        if news["id"] == news_id:
            return news

    raise HTTPException(status_code=404, detail="Новину не знайдено")


@app.post("/news")
def create_news(news: News):
    for item in news_list:
        if item["id"] == news.id:
            raise HTTPException(status_code=400, detail="Новина з таким ID вже існує")

    news_list.append(news.dict())
    return {
        "message": "Новину успішно додано",
        "news": news
    }


@app.put("/news/{news_id}")
def update_news(news_id: int, updated_news: News):
    for index, news in enumerate(news_list):
        if news["id"] == news_id:
            news_list[index] = updated_news.dict()
            return {
                "message": "Новину успішно оновлено",
                "news": updated_news
            }

    raise HTTPException(status_code=404, detail="Новину не знайдено")


@app.delete("/news/{news_id}")
def delete_news(news_id: int):
    for index, news in enumerate(news_list):
        if news["id"] == news_id:
            deleted_news = news_list.pop(index)
            return {
                "message": "Новину успішно видалено",
                "news": deleted_news
            }

    raise HTTPException(status_code=404, detail="Новину не знайдено")


@app.get("/news/category/{category}")
def get_news_by_category(category: str):
    result = [news for news in news_list if news["category"].lower() == category.lower()]

    if not result:
        raise HTTPException(status_code=404, detail="Новини цієї категорії не знайдено")

    return result


@app.get("/news/author/{author}")
def get_news_by_author(author: str):
    result = [news for news in news_list if news["author"].lower() == author.lower()]

    if not result:
        raise HTTPException(status_code=404, detail="Новини цього автора не знайдено")

    return result


@app.get("/news/published")
def get_published_news():
    result = [news for news in news_list if news["is_published"]]
    return result