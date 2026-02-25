import pandas as pd
import glob
import os

def csv_to_markdown():
    # 実行ディレクトリ内のすべてのCSVファイルを検索
    csv_files = glob.glob("*.csv")
    
    if not csv_files:
        print("CSVファイルが見つかりませんでした。")
        return

    for csv_file in csv_files:
        try:
            # CSVを読み込む（エンコーディングはUTF-8を想定、失敗した場合はcp932を試す）
            try:
                df = pd.read_csv(csv_file, encoding='utf-8')
            except UnicodeDecodeError:
                df = pd.read_csv(csv_file, encoding='cp932')
            
            # Markdownファイル名を生成
            md_filename = os.path.splitext(csv_file)[0] + ".md"
            
            # Markdownテーブルに変換（tabulateライブラリを使用）
            markdown_table = df.to_markdown(index=False)
            
            # ファイルに書き出し
            with open(md_filename, 'w', encoding='utf-8') as f:
                f.write(f"# {os.path.basename(csv_file)}\n\n")
                f.write(markdown_table)
            
            print(f"変換完了: {csv_file} -> {md_filename}")
            
        except Exception as e:
            print(f"エラーが発生しました ({csv_file}): {e}")

if __name__ == "__main__":
    csv_to_markdown()
