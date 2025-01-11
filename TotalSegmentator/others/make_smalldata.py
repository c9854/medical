import os
import shutil
import pandas as pd

# 定义源目录和目标目录
source_base = "/root/autodl-tmp/medical/data_all/data_CT"
target_base = "/root/autodl-tmp/medical/data_try/data_CT_test_114"

# 输入开始和结束的数字
start_num = 114
end_num = 114

# 确保目标目录存在
os.makedirs(target_base, exist_ok=True)

# 遍历并复制文件夹
for i in range(start_num, end_num + 1):  # 包括 start_num 到 end_num
    folder_name = f"s{i:04d}"  # 生成文件夹名称
    source_path = os.path.join(source_base, folder_name)
    target_path = os.path.join(target_base, folder_name)

    # 检查源目录是否存在并复制
    if os.path.exists(source_path):
        shutil.copytree(source_path, target_path, dirs_exist_ok=True)
        print(f"Copied: {source_path} -> {target_path}")
    else:
        print(f"Source folder not found: {source_path}")

# 读取 CSV 文件
input_file = os.path.join(source_base, "meta.csv")
output_file = os.path.join(target_base, "meta.csv")

# 读取数据
df = pd.read_csv(input_file, sep=";")

# 提取 'image_id' 中的数字部分并进行比较
df['image_id_num'] = df['image_id'].str.extract(r's(\d+)', expand=False).astype(int)

# 筛选 image_id 数字部分在指定范围内的行
filtered_df = df[(df['image_id_num'] >= start_num) & (df['image_id_num'] <= end_num)]

# 将筛选结果保存到新的 CSV 文件
filtered_df.to_csv(output_file, sep=";", index=False)

# 打印完成信息
print(f"Filtered data (image_id between {start_num} and {end_num}) saved to meta.csv")
