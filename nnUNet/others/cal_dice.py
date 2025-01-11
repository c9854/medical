import numpy as np
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import os

def dice_coefficient(pred, gt, num_classes):
    dice_scores = []
    for i in range(num_classes):
        pred_i = (pred == i).astype(np.uint8)
        gt_i = (gt == i).astype(np.uint8)
        
        intersection = np.sum(pred_i * gt_i)
        dice = 2 * intersection / (np.sum(pred_i) + np.sum(gt_i))
        dice_scores.append(dice)
        
    return np.mean(dice_scores)  # 宏平均

# 加载预测和真值数据
pred_path = f"/root/autodl-tmp/medical/code/gitclone/nnUNet/result/dataset_small_50_51/2d/BraTS-GLI-00053-001.nii.gz"
pred_path_3d_fullres = "/root/autodl-tmp/medical/code/gitclone/nnUNet/result/dataset_small_50_51/3d_fullres/BraTS-GLI-00053-001.nii.gz"
gt_path = f"/root/autodl-tmp/medical/code/gitclone/nnUNet/dataset/dataset_small_50_51/nnUNet_raw/Dataset137_BraTS2023/labelsTr/BraTS-GLI-00053-001.nii.gz"
output_dir = "/root/autodl-tmp/medical/code/gitclone/nnUNet/vis/dataset_small_50_51/cp"

# 加载 NIfTI 文件
pred_img = nib.load(pred_path).get_fdata()  # 获取预测数据
# print(pred_img.shape)
# print(pred_img.max())
gt_img = nib.load(gt_path).get_fdata()      # 获取真值数据
pred_imgg_3d_fullres = nib.load(pred_path_3d_fullres).get_fdata()      # 获取真值数据


# 获取第 75 层切片
slice_idx = 75
pred_slice = pred_img[:, :, slice_idx]
gt_slice = gt_img[:, :, slice_idx]
pred_imgg_3d_fullres_slice = pred_imgg_3d_fullres[:, :, slice_idx]

# 计算整个数据集的 Dice 系数
depth = pred_img.shape[2]  # 获取数据集的深度（切片数量）
dice_scores = dice_coefficient(pred_img, gt_img,3)



# 创建保存图像的文件夹
os.makedirs(output_dir, exist_ok=True)

# 可视化第 75 层
fig, ax = plt.subplots(1, 3, figsize=(12, 6))

# 显示预测图像
ax[0].imshow(pred_slice, cmap='jet')  # 使用 jet 色图
ax[0].set_title(f"Prediction Slice 2d {slice_idx + 1}")
ax[0].axis('off')

# 显示真值图像（直接使用 jet 色图）
ax[1].imshow(gt_slice, cmap='jet')  # 使用 jet 色图显示真值
ax[1].set_title(f"Ground Truth Slice {slice_idx + 1}")
ax[1].axis('off')

# 显示真值图像（直接使用 jet 色图）
ax[2].imshow(pred_imgg_3d_fullres_slice, cmap='jet')  # 使用 jet 色图显示真值
ax[2].set_title(f"Prediction Slice 3d_fullres {slice_idx + 1}")
ax[2].axis('off')

# 保存图像
output_file = os.path.join(output_dir, f"cp_{slice_idx + 1}.png")
plt.tight_layout()
plt.savefig(output_file)
plt.close()

# 输出 Dice 系数
print(f"Average Dice Coefficient: {dice_scores:.4f}")
