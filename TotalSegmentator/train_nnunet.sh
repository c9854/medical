
input_train_dir="/root/autodl-tmp/medical/data_try/data_CT_test_3"    ## the small dataset path
train_dataset_dir="/root/autodl-tmp/medical/data_try/Dataset102_CT100"      ## the conversion dataset

export nnUNet_raw="$train_dataset_dir/nnUNet_raw"
export nnUNet_preprocessed="$train_dataset_dir/nnUNet_preprocessed"
export nnUNet_results="$train_dataset_dir/nnUNet_results"


step=3


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


## training
## if want to change some training parameters, such as epoch,
## change it in the compile nnunet code before, in nnUNet/nnunetv2/training/nnUNetTrainer/nnUNetTrainer.py

if [ $step -eq 3 ]; then
    cd /root/autodl-tmp/medical/code/gitclone/nnUNet
        
    nnUNetv2_train 102 3d_fullres 0 -tr nnUNetTrainerNoMirroring
fi



if [ $step -eq 4 ]; then


    input_test_dir="/root/autodl-tmp/medical/data_try/data_CT_test_3"   ## the test small dataset path
    test_dataset_dir="/root/autodl-tmp/medical/data_try/Dataset102_test3"   ## the test conversation dataset
    test_dataset_img_dir="/root/autodl-tmp/medical/data_try/Dataset102_test3/nnUNet_raw/Dataset102_test3/imagesTr"  ## the conversation dataset imag path
    test_out="/root/autodl-tmp/medical/results/Tseg/nnunet/Dataset102_test3"  ## output path

    cd /root/autodl-tmp/medical/code/TotalSegmentator/resources

    python convert_dataset_to_nnunet.py \
    $input_test_dir \
    $test_dataset_dir \
    class_map_part_organs


    wait 

    # nnUNetv2_find_best_configuration 102 -c '3d_fullres' -f '0' --disable_ensembling
    nnUNetv2_predict -i $test_dataset_img_dir -o $test_out -d 102 \
    -c 3d_fullres -tr nnUNetTrainerNoMirroring --disable_tta -f 0
fi