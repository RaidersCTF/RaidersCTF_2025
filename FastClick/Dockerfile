# Apacheのベースイメージを使用
FROM httpd:2.4

# 作業ディレクトリを設定
WORKDIR /usr/local/apache2/htdocs/

# HTMLファイルをコンテナにコピー
COPY ./public-html/ /usr/local/apache2/htdocs/

# ポートを指定
EXPOSE 80

