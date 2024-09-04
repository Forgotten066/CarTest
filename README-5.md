# Настройка главной страницы

1. **Создание модели Post:**
   - Создали модель `Post` с полями: `image`, `title`, `created_at` и `updated_at`.
   - В классе `Meta` для модели указаны параметры `verbose_name`, `verbose_name_plural` и `ordering`, чтобы настроить отображение модели в админке и сортировку записей.

2. **Создание представления (views.py):**
   - создали представления `main_page` который бедут отображать главную страницу 

3. **Настройка URL-ов (main/urls.py):**
   - В файле `urls.py` приложения `main` нужно зарегистрировать `main_page` и написать на какой url она будет отображать главную страницу.
   - В нашем случае это `''` пустые кавычки которая обясняет что это главная страница

```python
from django.urls import path
from main.views import main_page


urlpatterns = [
    path('', main_page)
]
```

4. **Настройка шаблонов (settings.py):**
   - В файле `settings.py` проекта в константе `TEMPLATES` добавляем путь к директории с html файлами в ключе DIRS чтобы Django знал, где искать файлы html.
   `BASE_DIR / 'templates'`

```python
   TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

5. **Создание шаблона (templates/index.html):**
   - В директории `templates` создаем файл `index.html`, который был зарегистрировал в `views.py/main_page` 

6. **Основной файл URL-ов (TemplateProject/urls.py):**
   - В гланом urls.py добавляем дополнительные urls из приложения main
    `from django.urls import path, include`
    `path('', include('main.urls')),`

```python
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```




# Как отобразить Image в Admin панели 

**Регистрация модели**
    - Первую очередь нужно зарегистрировать модель в admin.py чтобы она отображалась в admin панели django 

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', 'created_at', 'id', 'view_image']
    list_filter = ['created_at']
    search_fields = ['id', 'title']
    readonly_fields = ['created_at', 'updated_at']
```

После указать пути где будут сохраняться все загруженные фотографии 
из admin панели django в файле `settings.py` нужно добавить дополнительные констаны 

```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Дальше нужно зарегистрировать эти пути в главном `urls.py` проекта 
с перва импортируем <br>
`from django.conf import settings` для получения доступа к константам `MEDIA_URL` и `MEDIA_ROOT`
<br>
`from django.conf.urls.static import static` Для регистрации путей из `MEDIA_URL` и `MEDIA_ROOT`

После добавляем в `urlpatterns` путь медиа папки

```python
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

После в `admin.py` там где вы зарегистрировали model нужно добавить метод для отображения фотографии `view_image`
импортируте `from django.utils.safestring import mark_safe` который добавить тег в admin панель django для отображения `img`

Метод `view_image` должен проверить есть ли у `obj` поле `image` и дольжен довабить тег img с помощью функции `mark_safe` иначе `'No image'`

obj это ваша Model

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', 'created_at', 'id', 'view_image']
    list_filter = ['created_at']
    search_fields = ['id', 'title']
    readonly_fields = ['created_at', 'updated_at']

    def view_image(self, obj: Post):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        else:
            return 'No image'  
```

# Подключить готовые bootstrap стили к html
Чтобы подключить Bootstrap к вашему HTML-документу, выполните следующие шаги:

1. **Подключите Bootstrap CSS:**
   Вставьте ссылку на Bootstrap CSS из сайта [bootstrapcdn](https://www.bootstrapcdn.com/) в секцию `<head>` вашего HTML-файла:
   В сайте нужно выбрать CSS и скопировать от туда вариант для HTML после вставьте ее в любом месте в теге `<head>` 

   ```html
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
   ```
   
   Пример
   ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Main Page</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    </head>
    <body>
        <header>
        </header>
        <main>  
        </main>
        <footer>
        </footer>
    </body>
    </html>
   ```

3. **Используйте Bootstrap компоненты:**<br>
   [Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)<br>
   [Examples](https://getbootstrap.com/docs/5.3/examples/)