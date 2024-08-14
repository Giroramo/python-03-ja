import pandas as pd
from sklearn import datasets

## 1.データの読み込みと概要
# アイリスのデータセットを読み込み、DataFrameに変換する
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# 品種の列を追加し、0～2の番号を記入する (各番号が異なる品種を表す)
iris_df['species'] = iris.target

# データの最初の5行を表示
print("アイリスデータセットの最初の5行:")
print(iris_df.head())


## 2. データのクリーニングと検証
# DataFrameに欠損値があるか確認する
has_missing_values = iris_df.isnull().values.any()
# 結果を表示
if has_missing_values:
    print("\nDataFrameに欠損値があります。")
else:
    print("\nDataFrameに欠損値はありません。")

# 各列のデータ型を確認
print("\n各列のデータ型:")
print(iris_df.dtypes)


## 3.基本的な分析と基本統計量
# 基本統計量を計算
statistics_df = iris_df.describe().transpose()

# 各行が1つの特徴量を表し、各列に計算した統計情報を格納
statistics_df['median'] = iris_df.median()

# 統計情報を表示
print("\n数値型特徴量の基本統計量:")
print(statistics_df)

# CSVとしてエクスポート
statistics_df.to_csv('iris_statistics.csv')


## 4.特徴量エンジニアリング
# ガクの面積を計算して新しい列を追加
iris_df['sepal_area'] = iris_df['sepal length (cm)'] * iris_df['sepal width (cm)']

# 花弁の面積を計算して新しい列を追加
iris_df['petal_area'] = iris_df['petal length (cm)'] * iris_df['petal width (cm)']

# 新しい特徴量の基本統計量を算出し、統計情報のDataFrameに追加
new_stats_df = iris_df[['sepal_area', 'petal_area']].describe().transpose()
new_stats_df['median'] = iris_df[['sepal_area', 'petal_area']].median()

# 統計情報のDataFrameを更新
statistics_df = pd.concat([statistics_df, new_stats_df])

# 更新した統計情報を表示
print("\n新しい特徴量(sepal_area, petal_area)の基本統計量:")
print(new_stats_df)

# CSVとしてエクスポート
statistics_df.to_csv('iris_updated_statistics.csv')


## 5.データのフィルタリング
# 例: 花弁の面積が3.0以上の行のみをフィルタリング
filtered_df = iris_df[iris_df['petal_area'] >= 3.0]

# フィルタリングされたデータを表示
print("花弁の面積が3.0cm2以上のデータ:\n")
print(filtered_df.head())

## ６．データのエクスポート
# フィルタリングされたデータをCSVとして保存
filtered_df.to_csv('filtered_iris.csv', index=False)
