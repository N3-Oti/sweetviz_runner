# ベースイメージ
FROM python:3.9-slim-bookworm

# コンテナ内での作業ディレクトリを設定
WORKDIR /app

# まず依存関係ファイルのみをコピーし、インストールを実行
# → requirements.txtに変更がなければ、このレイヤーはキャッシュが使われビルドが高速化する
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 次に、Pythonスクリプトをコピー
COPY sweetviz_runner.py .

# コンテナ起動時に実行するコマンドはdocker-compose.ymlで指定するため、ここでは不要