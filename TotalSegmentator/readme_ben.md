



# test the TotalSegmentator
## prepare the dataset from official link
test_TSeg.sh

# train nnunet in the CT dataset
## first step: select small data
TotalSegmentator/others/make_smalldata.py to make small dataset, need threshold

## second step: construct conversation dataset
## some difference in TotalSegmentator/resources/convert_dataset_to_nnunet.py to construct liver dataset
## if want to use other part of the body, change in the convert_dataset_to_nnunet.py, where class_map = {1:"liver"...}
run1_data.sh

## next: train
run2_train.sh


# test nnunet in the CT dataset
## first construct small raw data 
TotalSegmentator/others/make_smalldata.py
run1_data.sh
## second test
run3_test.sh




## visualization of nii.gz
TotalSegmentator/others/vis.py



