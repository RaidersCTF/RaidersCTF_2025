FROM php:8.1-apache

# 必要なPHPモジュールのインストール（必要に応じて調整）
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Apacheの設定ファイルをコピー
COPY ./apache/apache.conf /etc/apache2/sites-available/000-default.conf

COPY ./php/php.ini /usr/local/etc/php/php.ini

COPY ./html /var/www/html

# Apacheの設定を有効化
RUN a2enmod rewrite

# ポート80を公開
EXPOSE 80
