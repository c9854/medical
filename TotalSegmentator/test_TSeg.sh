

## select a data to seg
name=s0114

input_dir=/root/autodl-tmp/medical/data_all/data_CT/$name/ct.nii.gz
out_dir=/root/autodl-tmp/medical/results/Tseg/ct_seg/Dataset102_CT_114

cd /root/autodl-tmp/medical/code/TotalSegmentator

TotalSegmentator -i $input_dir -o $out_dir --task total -rs liver
