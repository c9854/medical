
# change the datapath 
nnUNet/nnunetv2/paths.py


# make test dataset
nnUNet/nnunetv2/dataset_conversion/Dataset137_BraTS21.py





nnUNetv2_find_best_configuration 137 -c '2d' -f '0' --disable_ensembling


test_imgdir=/root/autodl-tmp/nnUNet/dataset/dataset_small_5_test1/nnUNet_raw/Dataset137_BraTS2023/imagesTr


nnUNetv2_predict -d 137 -i /root/autodl-tmp/nnUNet/dataset/dataset_small_5_test1/nnUNet_raw/Dataset137_BraTS2023/imagesTr -o /root/autodl-tmp/nnUNet/dataset/test -f  0 -tr nnUNetTrainer -c 2d -p nnUNetPlans