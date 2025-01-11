

train_dataset_dir="/root/autodl-tmp/medical/data_try/Dataset102_CT100"      ## the conversion dataset

export nnUNet_raw="$train_dataset_dir/nnUNet_raw"
export nnUNet_preprocessed="$train_dataset_dir/nnUNet_preprocessed"
export nnUNet_results="$train_dataset_dir/nnUNet_results"



test_dataset_img_dir="/root/autodl-tmp/medical/data_try/Dataset102_CT_114/nnUNet_raw/Dataset102_CT_114/imagesTr"  ## the conversation dataset imag path
test_out="/root/autodl-tmp/medical/results/Tseg/nnunet/Dataset102_test3"  ## output path


# nnUNetv2_find_best_configuration 102 -c '3d_fullres' -f '0' --disable_ensembling
nnUNetv2_predict -i $test_dataset_img_dir -o $test_out -d 102 \
-c 3d_fullres -tr nnUNetTrainerNoMirroring --disable_tta -f 0