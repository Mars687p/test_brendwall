# Run guide #
1. git clone https://github.com/Mars687p/test_brendwall.git
2. python -m venv env && source env/Scripts/activate.bat
3. Заполнить .env file
4. pip install -r requirements.txt
5. python3 manage.py runserver

Маршруты API:
# 127.0.0.1:8000/api/v1/products/ # - просмотр продуктов
# 127.0.0.1:8000/api/v1/products/create/ #- создание(метод POST)
