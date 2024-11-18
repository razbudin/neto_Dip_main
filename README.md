[Task.md](./_resources/Task.md) *файл с описанием задания.*

  
Адрес сайта [localhost:8000](localhost:8000) или ваш адрес.  
Далее пути указаны без применения адреса. Например: `/posts/ == localhost:8000/posts/`

### Данный сайт работает только в режиме api вызовов.

В режиме просмотра из браузера можно посмотреть (GET запрос).  
/hosts/ - Все сообщения  
/hosts/id/ - Конкретное сообщение с данным id

## Запросы к api.

Для выполнения запросов потребуется токен авторизации. (Можно получить через админ-панель, либо через администрацию данного хоста).  
Примеры запросов из программы [Postman.](https://www.postman.com/ "Сайт программы Postman")

Для корректной работы в программе Postman, кроме заголовков: Content-type и Authorization, так же необходимо передавать заголовки: Content-Length и Host. Остальные заголовки можно отключить, а можно и не отключать. В данном случае на работу они не влияют.

Авторизацию в программе Postman можно сделать через Authorization > OAuth 2.0 поле Token: *значение токена*, поле Header Prefix: *Token*. 

==<img src="./_resources/auth.png" width="821" height="287">  
==

|     | Параметр | Путь | Headers (Заголовки) | Body (Тело сообшения) |
| --- | --- | --- | --- | --- |
| 1   | **GET** (просмотр всех сообщений) | /hosts/ |     |     |
| 2   | **GET** (просмотр одного сообщения) | /hosts/id/  <br>(id - числовое значение) |     |     |
| 3   | **POST** (Создание сообщения) | /hosts/ | <span style="color: #6b6b6b;">Authorization:</span> <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Token 08bec662132f072596a2dc0a43e2e3c7fa8de467  <br>Content-type:<span style="color: #6b6b6b;">multipart/form-data; boundary=&lt;calculated when request is sent&gt;</span></span></span> | form-data  <br>**key** text : **value** Текст сообщения  <br>**key** image : **value** Полный путь до файла изображения  <br>*\* url ссылки не работают, только локальный файл  <br>\*\* пример после таблицы* |
| 4   | **POST** (Создание комментария) | /hosts/id/comments/  <br>(id - числовое значение id комментария) | <span style="color: #6b6b6b;">Authorization:</span> <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Token 08bec662132f072596a2dc0a43e2e3c7fa8de467  <br>Content-type: application/json</span></span> | {  <br>    "text": "Текст комментария"  <br>} |
| 5   | **POST** (Лайк) | /hosts/id/likes/ | <span style="color: #6b6b6b;">Authorization:</span> <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Token 08bec662132f072596a2dc0a43e2e3c7fa8de467</span></span> |     |
| 6   | **PUT** (Редактирование сообщения) | /posts/id/ | <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Authorization:</span> <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Token 08bec662132f072596a2dc0a43e2e3c7fa8de467  <br>Content-type:<span style="color: #6b6b6b;">multipart/form-data; boundary=&lt;calculated when request is sent&gt;</span></span></span></span> | form-data  <br>**key** text : **value** Текст сообщения  <br>**key** image : **value** Полный путь до файла изображения  <br>*\* url ссылки не работают, только локальный файл  <br>\*\* пример после таблицы*   <br>*\*\*\* как в пункте 3 создание сообщения, только обращаемся к конкретному сообщению* |
| 7   | **PATCH** (Частичное изменение сообщения) | /posts/id/ | <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Authorization:</span> <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Token 08bec662132f072596a2dc0a43e2e3c7fa8de467  <br>либо 1:  <br>Content-type: application/json  <br>либо 2:  <br></span></span></span><span style="color: #6b6b6b;"><span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Content-type:<span style="color: #6b6b6b;">multipart/form-data; boundary=&lt;calculated when request is sent&gt;</span></span></span></span> | {  <br>    "text": "Текст измененного сообщения"  <br>}  <br>Изменение текста сообщения  <br>\___\___\___\___\___\___\___\___\___\___\___\___\__  <br>form-data  <br>**key** image : **value** Полный путь до файла изображения  <br>Изменение изображения в сообщении  <br>*\* url ссылки не работают, только локальный файл  <br>\*\* пример после таблицы  <br>\*\*\* как в пункте 3 и 6  <br>* |
| 8   | **DELETE** (Удаление сообщения) | /posts/id/ | <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Authorization:</span> <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Token 08bec662132f072596a2dc0a43e2e3c7fa8de467</span></span></span> |     |
|     | **DELETE** (Удаление комментария) | /posts/id/comments/ | <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Authorization:</span> <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Token 08bec662132f072596a2dc0a43e2e3c7fa8de467</span></span></span> |     |
|     | **DELETE** (Лайк удаление) | /hosts/id/likes/ | <span style="color: #6b6b6b;">Authorization:</span> <span style="color: #6b6b6b;"><span style="color: #6b6b6b;">Token 08bec662132f072596a2dc0a43e2e3c7fa8de467</span></span> |     |

&nbsp;

\*\* Пример тела сообщения для POST, PUT, PATCH (создание, редактирование или частичное редактирование сообщения) Программа Postman.  
<img src="./_resources/body.png" width="904" height="232">
