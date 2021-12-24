import waterdetect as wd
from waterdetect import DWWaterDetect

water_mask = wd.DWWaterDetect.run_single(image_folder='C:/Users/user/Desktop/Img',
                                         temp_folder='C:/Temp',
                                         shape_file='C:/Users/user/Desktop/Shape'
                                        )