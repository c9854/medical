input_train_dir="/root/autodl-tmp/medical/data_try/data_CT_test_3"    ## the small dataset path
train_dataset_dir="/root/autodl-tmp/medical/data_try/Dataset102_CT100"      ## the conversion dataset

export nnUNet_raw="$train_dataset_dir/nnUNet_raw"
export nnUNet_preprocessed="$train_dataset_dir/nnUNet_preprocessed"
export nnUNet_results="$train_dataset_dir/nnUNet_results"


cd /root/autodl-tmp/medical/code/gitclone/nnUNet
    
nnUNetv2_train 102 3d_fullres 0 -tr nnUNetTrainerNoMirroring
