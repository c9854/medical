import os
import nibabel as nib
import matplotlib.pyplot as plt
from PIL import Image

def save_slices_as_images_and_gif(input_folder, output_folder):
    """
    将 .nii.gz 文件中的所有切片保存为图片，并使用 PIL 生成一个 gif 格式的视频。
    
    Args:
        input_folder (str): 输入 .nii.gz 文件所在的文件夹路径。
        output_folder (str): 输出图片存放的文件夹路径。
    """
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍历输入文件夹中的所有 .nii.gz 文件
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".nii.gz"):
            file_path = os.path.join(input_folder, file_name)
            print(f"Processing {file_name}...")

            # 加载 .nii.gz 文件
            img = nib.load(file_path)
            data = img.get_fdata() * 255  # 获取图像数据 (3D array)
            print(file_path)
            print(data.max())
            
            # 创建对应的子文件夹
            organ_name = file_name.replace(".nii.gz", "")  # 去掉后缀作为文件夹名
            organ_output_folder = os.path.join(output_folder, organ_name)
            if not os.path.exists(organ_output_folder):
                os.makedirs(organ_output_folder)
            
            # 保存每个切片为图片
            image_files = []
            for i in range(data.shape[2]):
                slice_data = data[:, :, i]  # 获取第 i 张切片
                output_file_path = os.path.join(organ_output_folder, f"slice_{i:03d}.png")  # 命名图片
                
                # 保存切片为图片
                plt.imsave(output_file_path, slice_data, cmap="gray")
                image_files.append(output_file_path)
            
            # 使用 PIL 将图像序列转换为 gif
            gif_output_path = os.path.join(organ_output_folder, f"{organ_name}_video.gif")
            
            # 打开第一张图片
            images = [Image.open(image) for image in image_files]
            
            # 保存为 gif，设置帧率（`duration` 以毫秒为单位）
            images[0].save(gif_output_path, save_all=True, append_images=images[1:], duration=100, loop=0)
    
    print("All slices have been saved successfully as images and gifs!")

# 输入和输出文件夹路径
# input_folder = "/root/autodl-tmp/data_CT/s1397/segmentations"  # 替换为 .nii.gz 文件所在的文件夹路径
input_folder ="/root/autodl-tmp/medical/code/gitclone/nnUNet/result/dataset_small_50_51/3d_fullres"
output_folder = "/root/autodl-tmp/medical/code/gitclone/nnUNet/vis/dataset_small_50_51/nnunet/3d_fullres"  # 替换为图片保存的目标文件夹路径

# 执行切片保存和 gif 生成
save_slices_as_images_and_gif(input_folder, output_folder)


