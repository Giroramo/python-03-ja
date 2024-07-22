import os
import shutil
from pathlib import Path

# タスク1: 書籍の名前が付いたすべてのファイルを辞書にインポートし、1つのテキストファイルに保存
def import_books_to_dict(directory):
    books = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # ディレクトリをスキップするために、isfile() で確認する
        if os.path.isfile(file_path) and not filename.startswith("Chapter_"):
            with open(file_path, 'r', encoding='utf-8') as file:
                books[filename] = file.read()
    return books

def save_dict_to_file(books, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for title, content in books.items():
            file.write(f"Title: {title}\n\n{content}\n\n")

# タスク2: data フォルダー内に library ディレクトリを作成し、Chapter_x.txt ファイルを移動
def create_library_directory(base_dir):
    library_dir = os.path.join(base_dir, "library")
    os.makedirs(library_dir, exist_ok=True)
    return library_dir

def move_chapters_to_library(base_dir, library_dir):
    for filename in os.listdir(base_dir):
        if filename.startswith("Chapter_"):
            src_path = os.path.join(base_dir, filename)
            dest_path = os.path.join(library_dir, filename)
            shutil.move(src_path, dest_path)

def list_files_and_sizes(directory):
    path = Path(directory)
    for file_path in path.iterdir():
        if file_path.is_file():
            print(f"{file_path.name}: {file_path.stat().st_size} bytes")
            print(f"{directory}に移動しました。")

# メイン処理
base_dir = "./data/text_files"
output_file = "combined_books.txt"

# タスク1の処理
books_dict = import_books_to_dict(base_dir)
save_dict_to_file(books_dict, output_file)

# タスク2の処理
library_dir = create_library_directory(base_dir)
move_chapters_to_library(base_dir, library_dir)
list_files_and_sizes(library_dir)
