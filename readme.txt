##Опис завддання: 

Створіть Rest Api для новин дані та інше можете обирати довільно.REST API для новин на FastAPI.

## Запуск проєкту

pip install -r requirements.txt
uvicorn main:app --reload
Перейти за посиланням та в пошуковому меню додати docs,
приклад адреси: http://127.0.0.1:8000/docs

Основні маршрути:
GET /news — отримати всі новини
GET /news/{news_id} — отримати одну новину по ID
POST /news — створити новину
PUT /news/{news_id} — оновити новину
DELETE /news/{news_id} — видалити новину
GET /news/category/{category} — пошук по категорії
GET /news/author/{author} — пошук по автору
GET /news/published — тільки опубліковані новини
Наприклад:
Відкрити GET /news
Натиснути кнопку Try it out
Потім Execute
Буде список усіх новин
Cancel - закриє новини