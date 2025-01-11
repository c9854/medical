dataset_dir="/root/autodl-tmp/medical/code/gitclone/nnUNet/dataset/dataset_small_20_new"


export nnUNet_raw="$dataset_dir/nnUNet_raw"
export nnUNet_preprocessed="$dataset_dir/nnUNet_preprocessed"
export nnUNet_results="$dataset_dir/nnUNet_results"



## training
# if want to change the iteration
# /root/autodl-tmp/nnUNet/nnunetv2/training/nnUNetTrainer/nnUNetTrainer.py
# change some models, such as 2d or 3d_fullres
nnUNetv2_train 137 3d_fullres 0  --npz  