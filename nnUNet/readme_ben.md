# bug resolve
## add some code in nnUNet/nnunetv2/training/loss/compound_losses.py
import torch._dynamo
torch._dynamo.config.suppress_errors = True

## change the code in nnUNet/nnunetv2/training/loss/dice.py
x_shape = list(x.shape)
y_shape = list(y.shape)

if x_shape == y_shape:


## training nnunet in MRI dataset
## set the data path: dataset_dir, construct dataset
run1_data.sh
## start training, if need to set the epoch et. change in nnUNet/nnunetv2/training/nnUNetTrainer/nnUNetTrainer.py
run2_train.sh



## test nnunet in MRI dataset
## first selcet small test data from MRI dataset and process
run1_data.sh
## set the pretrained datapath: dataset_dir
## using pretrained model to test 
run3_test.sh


## visualization
nnUNet/others/vis_gif.py
