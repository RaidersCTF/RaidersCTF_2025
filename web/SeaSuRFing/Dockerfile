FROM python:3.9

# 新しいユーザー作成
RUN adduser --disabled-password --gecos "" appuser

# 作業ディレクトリを指定
WORKDIR /app

# 依存関係のインストール
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . /app

# ユーザーを変更
USER appuser

# ポートを公開
EXPOSE 5656

# uWSGIとFlaskアプリケーションを起動
CMD ["uwsgi", "--http", "0.0.0.0:5656", "--wsgi-file", "app.py", "--callable", "app"]
