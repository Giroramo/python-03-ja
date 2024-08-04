import csv
import json
import os
import io

def read_csv(file_path):
    """
    CSVファイルを読み取り、その内容を辞書のリストで返す

    :引数 file_path: 文字列 - CSVファイルへのパス
    :戻り値: リスト - CSVの列を表す辞書のリスト
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def csv_to_json(csv_data):
    """
    CSVデータ (辞書のリスト) を受け取り、それをJSON形式 (文字列) に変換する

    :引数 csv_data: リスト - 辞書のリストで表したCSVデータ
    :戻り値: 文字列 - JSON形式で表したデータ
    """
    return json.dumps(csv_data, ensure_ascii=False, indent=4)

def write_json(json_data, file_path):
    """
    JSONデータをファイルに書き込む

    :param json_data: 文字列 - 書き込むJSONデータ
    :param file_path: 文字列 - JSONファイルへのパス
    """
    with open(file_path, mode='w', encoding='utf-8') as file:
        file.write(json_data)

def read_json(file_path):
    """
    JSONファイルを読み取ってその内容を返す

    :引数 file_path: 文字列 - JSONファイルへのパス
    :戻り値: JSONファイルの内容
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        return json.load(file)

def json_to_csv(json_data):
    """
    JSONデータを受け取り (通常は辞書のリスト)、それをCSV形式 (文字列) に変換する

    :引数 json_data: リスト - 辞書のリストで表したJSONデータ
    :戻り値: 文字列 - CSV形式で表したデータ
    """
    if not json_data:
        return ""
    
    fieldnames = json_data[0].keys()
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(json_data)
    
    return output.getvalue()

def write_csv(csv_data, file_path):
    """
    CSVデータをファイルに書き込む

    :引数 csv_data: 文字列 - 書き込むCSVデータ
    :引数 file_path: 文字列 - CSVファイルへのパス
    """
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        file.write(csv_data)

def validate_data(data, data_type):
    """
    データの整合性を確認する (例: CSVの列数に一貫性があること)

    :引数 data: 検証対象のデータ
    :引数 data_type: 文字列 - データ型 ('CSV' または 'JSON')
    :戻り値: bool - データが有効な場合はTrue、無効な場合はFalse
    """
    if data_type == 'CSV':
        if not data:
            return False
        columns = len(data[0])
        return all(len(row) == columns for row in data)
    
    elif data_type == 'JSON':
        if not isinstance(data, list):
            return False
        if not data:
            return True
        keys = set(data[0].keys())
        return all(set(row.keys()) == keys for row in data)
    
    return False

def process_directory(directory_path):
    """
    指定されたディレクトリにあるすべてのCSVまたはJSONファイルを確認し、適切に変換する

    :引数 directory_path: 文字列 - 処理対象のディレクトリへのパス
    """
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if filename.endswith('.csv'):
            csv_data = read_csv(file_path)
            if not validate_data(csv_data, 'CSV'):
                print(f"Invalid CSV data in file: {filename}")
                continue
            
            json_data = csv_to_json(csv_data)
            json_file_path = file_path.replace('.csv', '.json')
            write_json(json_data, json_file_path)
            print(f"Converted {filename} to JSON")
        
        elif filename.endswith('.json'):
            json_data = read_json(file_path)
            if not validate_data(json_data, 'JSON'):
                print(f"Invalid JSON data in file: {filename}")
                continue
            
            csv_data = json_to_csv(json_data)
            csv_file_path = file_path.replace('.json', '.csv')
            write_csv(csv_data, csv_file_path)
            print(f"Converted {filename} to CSV")

# スクリプトを実行するmain関数
def main():
    # 使用例
    try:
        directory = "."  # 現在のディレクトリ
        process_directory(directory)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
