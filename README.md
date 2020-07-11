# todo

# Usage

リポジトリを複製

```git clone git@github.com:hanatsuyo/todo.git```

todoリポジトリでdockerコンテナを起動させる

```docker-compose up -d```

todo_web_1コンテナの中に入る

```docker exec -it todo_web_1 bash``` 

django-cleanup,Pillowをコンテナの中に入れる（おそらくエラーが出ます）

```pip install django-cleanup Pillow```

mysiteディレクトリに移動してマイグレートします

```python manage.py migrate```

ブログ投稿は管理者のみ可能なので管理者の設定をします。ユーザー名、メールアドレス、パスワードを設定します。

```python manage.py createsuperuser```

サーバーを起動します

```python manage.py runserver 0.0.0.0:8000```

# Note
ログインして使用できます。
Postからブログの投稿ができます。
Postは管理者にしか表示されないようになっています。


