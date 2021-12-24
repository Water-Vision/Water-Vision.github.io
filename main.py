import waterdetect as wd

water_mask = wd.DWWaterDetect.run_single(image_folder='D:\Images\Input\Input_Tiete/SENTINEL2A_20190326-132829-354_L2A_T22KGA_C_V2-0',
                                         temp_folder='D:/temp',
                                         shape_file='D:/Shp/Area_Tiete.shp'
                                    )