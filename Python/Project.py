# PSIV project looking into WSS error from measuring with compliant wall vs a
# rigid wall

# Author: Liam Brosnan
# Date: 22 / 04 / 2022

# inporting the packages for calculations and plotting
import numpy as np                 
import matplotlib.pyplot as plt

# variables
u = 0.0004      # dynamic viscosity (Pa)
vm = 0.1        # maximum veloxity in artery (m/s)
y = 0.006       # location of point respect to centre of artery (m)
artery_elasticity = 2.64e5    # artery elasticity (Pa)
p = 15998.7     # pressure in artery (Pa)          
t = 0.005       # artery thickness (m)
wss_array = np.array ([])   # creating empty array for WSS values
artery_delta_r_array = np.array ([])    # empty array for change in radius
new_wss_array = np.array ([])   # empty array for new WSS values

# radius array, 30 values from 0.012 to 0.048
r_value_array = np.linspace(0.012, 0.048,30)    

# WSS calculation
def wss_calc(r_value_array):    # fucntion setup passing radius value array
    return -(2*u*vm*y) / (r_value_array**2) # calculation for WSS
for i in range(len(r_value_array)): # passing the radius array through the equaiton
    wss_array = np.append(wss_array,wss_calc(r_value_array[i])) # appedning
    # values for WSS to the empty array setup
    
# artery change in diameter calculation
def artery_delta_r_calc(r_value_array): # function for change in radius passing 
# radius values array
    return (p * r_value_array**2) / (t * artery_elasticity) # equation for change in radius
for i in range(len(r_value_array)): # passing radius array through equation
    # appending results of change in radius to the empty array
    artery_delta_r_array = np.append(artery_delta_r_array,artery_delta_r_calc(r_value_array[i]))    

# new radius value array
new_r_array = np.add(r_value_array, artery_delta_r_array)

# new WSS calculation
def new_wss_calc(new_r_array): # fucntion calculating new wss value
    return -(2*u*vm*y) / (new_r_array**2)   # wss equation
for i in range(len(new_r_array)):   # passing new radius value through equation
# appending new wss values found to empty array
    new_wss_array = np.append(new_wss_array, new_wss_calc(new_r_array[i]))

# WSS error calculation
wss_error = np.add(wss_array, new_wss_array)

# WSS calculation plotting
plt.figure()
plt.plot(r_value_array, wss_array)

plt.xlabel('RADIUS (m)')
plt.ylabel('WSS (Pa)')
plt.title('WSS VS RADIUS')

plt.show()

plt.figure()
plt.plot(r_value_array, artery_delta_r_array)

plt.xlabel('RADIUS (m)')
plt.ylabel('DELTA D')
plt.title('DELTA D VS RADIUS')

plt.show()

plt.figure()
plt.plot(r_value_array, wss_error)

plt.xlabel('artery_delta_r_array')
plt.ylabel('wss_error')
plt.title('CHANGE IN RADIUS VS WSS ERROR')

