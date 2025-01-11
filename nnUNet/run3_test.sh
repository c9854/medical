dataset_dir="/root/autodl-tmp/medical/code/gitclone/nnUNet/dataset/dataset_small_20_new"

test_data_dir="/root/autodl-tmp/medical/code/gitclone/nnUNet/dataset/dataset_small_50_51/nnUNet_raw/Dataset137_BraTS2023/imagesTr"
test_out_dir="/root/autodl-tmp/medical/code/gitclone/nnUNet/result/dataset_small_50_51/2d"

export nnUNet_raw="$dataset_dir/nnUNet_raw"
export nnUNet_preprocessed="$dataset_dir/nnUNet_preprocessed"
export nnUNet_results="$dataset_dir/nnUNet_results"

##if need select the best model
# nnUNetv2_find_best_configuration 137 -c '2d' -f '0' --disable_ensembling


# nnUNetv2_predict -d 137 -i $test_data_dir -o $test_out_dir -f  0 -tr nnUNetTrainer -c 2d -p nnUNetPlans
nnUNetv2_predict -d 137 -i $test_data_dir -o $test_out_dir -f  0 -tr nnUNetTrainer -c 2d -p nnUNetPlans
