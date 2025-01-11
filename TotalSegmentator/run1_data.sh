input_train_dir="/root/autodl-tmp/medical/data_try/data_CT_test_114"    ## the small dataset path
train_dataset_dir="/root/autodl-tmp/medical/data_try/Dataset102_CT_114"      ## the conversion dataset

export nnUNet_raw="$train_dataset_dir/nnUNet_raw"
export nnUNet_preprocessed="$train_dataset_dir/nnUNet_preprocessed"
export nnUNet_results="$train_dataset_dir/nnUNet_results"


step=2


## data conversion 
## if want to change the part of the body, change in convert_dataset_to_nnunet.py
if [ $step -eq 1 ]; then
    cd /root/autodl-tmp/medical/code/TotalSegmentator/resources

    python convert_dataset_to_nnunet.py \
    $input_train_dir \
    $train_dataset_dir \
    class_map_part_organs

fi

#  
if [ $step -eq 2 ]; then
    cd /root/autodl-tmp/medical/code/gitclone/nnUNet

    nnUNetv2_plan_and_preprocess -d 102 -pl ExperimentPlanner -c 3d_fullres -np 2

fi
