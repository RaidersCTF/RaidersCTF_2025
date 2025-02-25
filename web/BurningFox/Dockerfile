# 使用するベースイメージ
FROM nginx:latest

# 作業ディレクトリを指定
WORKDIR /usr/share/nginx/html

# nginxのデフォルト設定を削除（必要に応じて）
RUN rm /etc/nginx/conf.d/default.conf

# カスタムnginx設定ファイルをコンテナにコピー
COPY nginx.conf /etc/nginx/nginx.conf

# ポート80を公開
EXPOSE 80

# nginxをフォアグラウンドで実行
CMD ["nginx", "-g", "daemon off;"]
