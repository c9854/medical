# import numpy as np
# import matplotlib.pyplot as plt
# import nibabel as nib
# from glob import glob

# num = "008"
# # 加载图像数据
# imgs = [nib.load(f"/root/autodl-tmp/data_GLI/ASNR-MICCAI-BraTS2023-GLI-Challenge-TrainingData/BraTS-GLI-00{num}-000/BraTS-GLI-00{num}-000-{m}.nii.gz").get_fdata().astype(np.float32)[:, :, 75] for m in ["t1n", "t1c", "t2f", "t2w"]]
# lbl = nib.load(f"/root/autodl-tmp/data_GLI/ASNR-MICCAI-BraTS2023-GLI-Challenge-TrainingData/BraTS-GLI-00{num}-000/BraTS-GLI-00{num}-000-seg.nii.gz").get_fdata().astype(np.uint8)[:, :, 75]



# # 创建绘图
# fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(15, 15))
# for i, img in enumerate(imgs):
#     ax[i].imshow(img, cmap='gray')
#     ax[i].axis('off')
# ax[-1].imshow(lbl, vmin=0, vmax=4)
# ax[-1].axis('off')

# # 保存图像到文件
# output_file = "/root/autodl-tmp/nnUNet/gt.png"  # 设置保存的文件路径和文件名
# plt.tight_layout()  # 调整布局，避免图像重叠
# plt.savefig(output_file)  # 保存图像
# plt.close()  # 关闭绘图，释放内存

# print(f"Image saved to {output_file}")









import nibabel as nib
import matplotlib.pyplot as plt

# 文件路径
file_path = "/root/autodl-tmp/nnUNet/dataset/dataset_small_20/nnUNet_raw/Dataset137_BraTS2023/labelsTr/BraTS-GLI-00000-000.nii.gz"

# 加载NIfTI文件
img = nib.load(file_path)
img_data = img.get_fdata()

# 可视化其中一层（例如：第 75 层）
slice_index = 75  # 可以调整切片索引
img_slice = img_data[:, :, slice_index]

# 创建图形并保存
output_file = "/root/autodl-tmp/nnUNet/predict.png"  # 设置保存的文件路径和文件名
plt.imshow(img_slice, cmap='gray')
plt.axis('off')  # 去掉坐标轴
plt.title(f"Slice {slice_index}")
plt.tight_layout()  # 调整布局
plt.savefig(output_file)  # 保存图像
plt.close()  # 关闭图形，释放内存

print(f"Image saved to {output_file}")

