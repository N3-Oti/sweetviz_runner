import pandas as pd
import sweetviz as sv
import os
import sys
import glob

# --- 定数定義 ---
INPUT_DIR = '/app/input'
OUTPUT_DIR = '/app/output'
# ターゲット特徴量を指定（不要な場合は None）
# この特徴量がCSVに存在しない場合は、ターゲットなしで分析されます
TARGET_FEATURE = 'Attrition'

# --- メイン処理 ---
print("Sweetvizの処理を開始します...")

# 1. inputディレクトリ内のCSVファイルを検索
print(f"'{INPUT_DIR}' ディレクトリ内のCSVファイルを検索します...")
# globを使ってパターンに一致するファイルパスのリストを取得
csv_files = glob.glob(os.path.join(INPUT_DIR, '*.csv'))

if not csv_files:
    print(f"エラー: '{INPUT_DIR}' 内にCSVファイルが見つかりませんでした。")
    print("ホストマシンの 'input' ディレクトリに分析したいCSVファイルを配置してください。")
    sys.exit(1) # エラーコード1で終了

# 複数見つかった場合は、最初のCSVファイルを使用
target_csv_path = csv_files[0]
print(f"分析対象ファイル: {target_csv_path}")

# 2. CSVファイルを読み込み
try:
    df = pd.read_csv(target_csv_path)
    print("CSVファイルの読み込みが完了しました。")
except Exception as e:
    print(f"エラー: CSVファイルの読み込み中に問題が発生しました。 - {e}")
    sys.exit(1)

# 3. Sweetvizレポートを生成
print("レポートを生成中です...")
if TARGET_FEATURE and TARGET_FEATURE in df.columns:
    report = sv.analyze(df, target_feat=TARGET_FEATURE)
else:
    if TARGET_FEATURE:
        print(f"警告: 指定されたターゲット特徴量 '{TARGET_FEATURE}' はCSVに存在しません。")
    report = sv.analyze(df)
print("レポートの生成が完了しました。")

# 4. レポートをHTMLファイルとして出力
# 出力ファイル名を入力ファイル名に基づいて動的に決定 (例: data.csv -> data_report.html)
input_filename = os.path.basename(target_csv_path)
report_filename = f"{os.path.splitext(input_filename)[0]}_Sweetviz_report.html"
report_path = os.path.join(OUTPUT_DIR, report_filename)

report.show_html(filepath=report_path, open_browser=False)

print("\n--- 完了 ---")
print(f"レポートがコンテナ内のパス '{report_path}' に出力されました。")
print(f"ホストマシンの 'output' ディレクトリに '{report_filename}' が生成されているか確認してください。")