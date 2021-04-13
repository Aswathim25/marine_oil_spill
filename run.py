
from datetime import datetime, timedelta
from opendrift.readers import reader_netCDF_CF_generic
from opendrift.models.openoil import OpenOil

f=open("file.txt", "r")
fl =f.readlines()	
val=[]
for x in fl:
   val.append(x)	   
lat=float(val[0].rstrip())
lon=float(val[1].rstrip())
oiltype=val[2].rstrip()
seed=int(val[3].rstrip())
f.close()

o = OpenOil(loglevel=0)  # Set loglevel to 0 for debug information
reader_arome = reader_netCDF_CF_generic.Reader(o.test_data_folder() + '16Nov2015_NorKyst_z_surface/arome_subset_16Nov2015.nc')
reader_norkyst = reader_netCDF_CF_generic.Reader(o.test_data_folder() + '16Nov2015_NorKyst_z_surface/norkyst800_subset_16Nov2015.nc')

#reader_arome = reader_netCDF_CF_generic.Reader('http://thredds.met.no/thredds/dodsC/meps25files/meps_det_extracted_2_5km_latest.nc')
#reader_norkyst = reader_netCDF_CF_generic.Reader('http://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')
 

o.add_reader([reader_norkyst, reader_arome])
time = [reader_arome.start_time,
        reader_arome.start_time + timedelta(hours=30)]
o.seed_elements(lon, lat, radius=50, number=seed, time=time,
                wind_drift_factor=.03)
o.set_config('processes:dispersion', True)
o.set_config('processes:evaporation', True)
o.set_config('processes:emulsification', True)
o.set_config('drift:current_uncertainty', .1)
o.set_config('drift:wind_uncertainty', .1)
o.run(end_time=reader_norkyst.end_time,time_step=1800,
      time_step_output=3600, outfile='openoil.nc',
      export_variables=['mass_oil'])
print(o)

o.animation(filename = 'one.gif')
o.plot(filename = 'one.jpg')
