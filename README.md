# Sweetviz Runner

Dockerコンテナを使用してSweetvizによるデータ分析レポートを自動生成するツールです。

## 🚀 機能

- CSVファイルの自動読み込み
- Sweetvizによる包括的なデータ分析レポート生成
- Dockerコンテナ化による環境依存の排除
- ターゲット特徴量の指定可能（オプション）

## 📋 前提条件

- Docker
- Docker Compose

## 🛠️ セットアップ

1. リポジトリをクローン
```bash
git clone <repository-url>
cd sweetviz_runner
```

2. 分析したいCSVファイルを`input`ディレクトリに配置
```bash
cp your_data.csv input/
```

## 🚀 使用方法

1. Dockerコンテナをビルドして実行
```bash
docker-compose up --build
```

2. レポートの確認
- 生成されたレポートは`output`ディレクトリに保存されます
- ファイル名: `{元のCSVファイル名}_Sweetviz_report.html`

## ⚙️ 設定

### ターゲット特徴量の変更

`sweetviz_runner.py`の以下の行を編集してください：

```python
TARGET_FEATURE = 'Attrition'  # あなたのターゲット列名に変更
```

## 📁 ディレクトリ構造

```
sweetviz_runner/
├── input/                    # 分析対象のCSVファイルを配置
├── output/                   # 生成されたレポートが保存される
├── sweetviz_runner.py        # メインスクリプト
├── requirements.txt          # Python依存関係
├── Dockerfile               # Dockerイメージ定義
├── docker-compose.yml       # Docker Compose設定
└── README.md               # このファイル
```

## 🔧 カスタマイズ

### 新しい依存関係の追加

`requirements.txt`に必要なパッケージを追加し、コンテナを再ビルドしてください：

```bash
docker-compose build --no-cache
```

### 分析パラメータの調整

`sweetviz_runner.py`内のSweetviz設定を変更することで、分析の詳細度や出力形式を調整できます。

## 📊 出力例

生成されるレポートには以下の情報が含まれます：

- データセット概要
- 特徴量の統計情報
- 相関分析
- ターゲット特徴量との関係性（指定した場合）
- データ品質レポート


## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## ⚠️ 注意事項

- 機密データを含むCSVファイルは`input`ディレクトリに配置しないでください
- 生成されたレポートには元データの情報が含まれる可能性があります
- 本番環境での使用前に、データの機密性を確認してください 