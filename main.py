import matplotlib as plt
import waterdetect as wd
import rasterio

config = wd.DWConfig(config_file='WaterDetect.ini')
config.clustering_bands, config.detect_water_cluster

b3  = rasterio.open('D:\Images\Input\Input_Tiete\SENTINEL2A_20190326-132829-354_L2A_T22KGA_C_V2-0\SENTINEL2A_20190326-132829-354_L2A_T22KGA_C_V2-0_FRE_B3.tif').read()
nir = rasterio.open('D:\Images\Input\Input_Tiete\SENTINEL2A_20190326-132829-354_L2A_T22KGA_C_V2-0\SENTINEL2A_20190326-132829-354_L2A_T22KGA_C_V2-0_FRE_B8.tif').read()
b3.shape, nir.shape

bands = {'Green': b3.squeeze()/10000, 'Nir': nir.squeeze()/10000}
wmask = wd.DWImageClustering(bands=bands, bands_keys=['Nir', 'ndwi'], invalid_mask=None, config=config)
mask = wmask.run_detect_water()

plt.imshow(wmask.water_mask==1)

plt.imshow(wmask.cluster_matrix)
