Действующий проект доступен по адресу http://rcstyle.pythonanywhere.com/

<b>Запуск проекта</b>

1. git clone https://github.com/Endorfin86/Menu.git
2. python -m venv venv
3. venv\Scripts\activate
4. cd Menu
5. pip install -r requirements.txt
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver

<b>Создание меню</b>
1. Создать меню в админпанели
2. Создать разделы и подразделы меню в админпанели
3. Разместить код формата {% draw_menu 'name-menu (Имя)' select %} в шаблонах home.html и page.htm
