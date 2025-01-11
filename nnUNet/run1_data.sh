dataset_dir="/root/autodl-tmp/medical/code/gitclone/nnUNet/dataset/dataset_small_50_51"


export nnUNet_raw="$dataset_dir/nnUNet_raw"
export nnUNet_preprocessed="$dataset_dir/nnUNet_preprocessed"
export nnUNet_results="$dataset_dir/nnUNet_results"


step=1

if [ $step -eq 1 ]; then
    python /root/autodl-tmp/medical/code/gitclone/nnUNet/nnunetv2/dataset_conversion/Dataset137_BraTS21.py
fi

cd /root/autodl-tmp/medical/code/gitclone/nnUNet
#  
if [ $step -eq 2 ]; then
    nnUNetv2_plan_and_preprocess -d 137 --verify_dataset_integrity
fi
