### Welcome to SliceGAN ###
####### Steve Kench #######

from SliceGAN_util import *

## make directory
Project_name = 'No_transfer' #Creates directory with output images
Project_dir = 'transfer_learning/'

## Data Processing
image_type = 'threephase' # threephase, twophase or colour
data_type = 'tif' # png, jpg, tif, array, array2D
data_path = ['Examples/img_stack_1200_2500_1200_high_reso_biphase_porosity55.tiff'] # path to training data.
isotropic = False
Training = False # Run with False to show an image during training
Project_path = mkdr(Project_name, Project_dir, Training)

## Network Architectures
imsize, nz,  channels = 64, 16, 3
dk, gk = [4,4,4,4,4], [4,4,4,4,4]                                    # kernal sizes
ds, gs = [2,2,2,2,2], [2,2,2,2,2]                                    # strides
df, gf = [channels,64,128,26,512,1], [nz,512,256,128,64,channels]  # filter sizes for hidden layers
dp, gp = [3,2,2,2,2],[2,2,2,2,3]
##Create Networks
netD, netG = Architect(Project_path, Training, dk, ds, df,dp, gk ,gs, gf, gp)

# if Training:
#     data = trainer(Project_path, image_type, data_type, data_path, netD, netG, isotropic, channels, imsize, nz)
#
# ##Save tif/ show full volume
# else:
#     img, raw, netG = test_img(Project_path, image_type, netG(), nz, show = False, lf = 4)