from fastapi import FastAPI, HTTPException
from models import News, NewsUpdate
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
    new_id = max(item["id"] for item in news_list) + 1 if news_list else 1
    new_news = news.model_dump()
    new_news["id"] = new_id
    news_list.append(new_news)
    return {
        "message": "Новину успішно додано",
        "news": new_news
    }


@app.put("/news/{news_id}")
def update_news(news_id: int, updated_news: News):
    for index, news in enumerate(news_list):
        if news["id"] == news_id:
            updated_news_dict = updated_news.model_dump()
            updated_news_dict["id"] = news_id
            news_list[index] = updated_news_dict
            return {
                "message": "Новину успішно оновлено",
                "news": updated_news_dict
            }
    raise HTTPException(status_code=404, detail="Новину не знайдено")


@app.patch("/news/{news_id}")
def partial_update_news(news_id: int, updated_data: NewsUpdate):
    for news in news_list:
        if news["id"] == news_id:
            update_data = updated_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                news[key] = value
            return {
                "message": "Новину частково оновлено",
                "news": news
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
    return [news for news in news_list if news["is_published"]]


@app.get("/news/unpublished")
def get_unpublished_news():
    return [news for news in news_list if not news["is_published"]]


@app.get("/news/search/{keyword}")
def search_news(keyword: str):
    result = [news for news in news_list
              if keyword.lower() in news["title"].lower() or keyword.lower() in news["content"].lower()]
    if not result:
        raise HTTPException(status_code=404, detail="Нічого не знайдено")
    return result


@app.get("/news/date/{date}")
def get_news_by_date(date: str):
    result = [news for news in news_list if news["created_at"].strftime("%Y-%m-%d") == date]
    if not result:
        raise HTTPException(status_code=404, detail="Новини за цю дату не знайдено")
    return result


@app.get("/news/sorted")
def get_sorted_news(order: str = "desc"):
    sorted_news = sorted(news_list, key=lambda x: x["created_at"], reverse=True if order == "desc" else False)
    return sorted_news
@app.get("/news/stats")
def get_news_stats():
    total_news = len(news_list)
    published_news = len([news for news in news_list if news["is_published"]])
    unpublished_news = len([news for news in news_list if not news["is_published"]])
    return {
        "total_news": total_news,
        "published_news": published_news,
        "unpublished_news": unpublished_news
    }