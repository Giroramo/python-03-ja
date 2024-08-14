import sqlite3
import pandas as pd
from datetime import datetime


def transform_date_format(date_str):
    """
    日付文字列の形式を 'YYYY-MM-DD' から 'DD/MM/YYYY' に変換する
    入力が想定された形式と異なる場合は、元の文字列を返す
    
    引数:
    date_str (文字列): 'YYYY-MM-DD' 形式の日付文字列

    戻り値:
    文字列: 'DD/MM/YYYY' 形式に変換した日付文字列、または元の文字列 (形式が無効だった場合)
    """
    # 日付形式を変換するロジックを実装してください
    try:
        # 'YYYY-MM-DD' 形式の日付を 'DD/MM/YYYY' 形式に変換
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except ValueError:
        # 入力が無効な場合は元の文字列を返す
        return date_str

def apply_date_transformation(db_path, table_name, column_name):
    """
    SQLiteテーブルの指定した列にtransform_date_format関数を適用する

    引数:
    db_path (文字列): SQLiteデータベースへのパス
    table_name (文字列): データベース内のテーブル名
    column_name (文字列): 日付形式の変換を適用する列名

    戻り値:
    DataFrame: 変換した列のデータを含むPandas DataFrame
    """
    with sqlite3.connect(db_path) as conn:
        # 指定したテーブルをDataFrameに読み込んでください
        # 指定した列にtransform_date_format関数を適用してください
        # 変更後のDataFrameを返してください
        # テーブルをDataFrameとして読み込む
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        
        # 指定した列にtransform_date_formatを適用
        df[column_name] = df[column_name].apply(transform_date_format)
        
        return df

# 使用例 (受講者はこれを変更してください)
if __name__ == "__main__":
    db_path = '../data/northwind.db'
    table_name = 'Orders' # 受講者はこれを確認するか変更してください
    column_name = 'OrderDate' # 受講者はこれを確認するか変更してください
    transformed_df = apply_date_transformation(db_path, table_name, column_name)
    print(transformed_df.head())
