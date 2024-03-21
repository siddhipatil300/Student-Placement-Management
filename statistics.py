import matplotlib.pyplot as plt 
import numpy as np 
  
def plot_statistics():  # Changed function name to plot_statistics
    # create data 
    x = np.arange(3) 
    y1 = [252, 283, 247] 
    y2 = [218, 219, 219] 
    y3 = [17, 35, 31] 
    width = 0.2
    
    # plot data in grouped manner of bar type 
    plt.bar(x-0.2, y1, width, color='cyan') 
    plt.bar(x, y2, width, color='orange') 
    plt.bar(x+0.2, y3, width, color='green') 
    plt.xticks(x, ['2018-19','2017-18','2016-17']) 
    plt.xlabel("Year") 
    plt.ylabel("Number of Students") 
    plt.legend(["Eligible", "Placed", "Higher Studies"]) 
    plt.show()
