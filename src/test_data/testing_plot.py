import matplotlib.pyplot as plt
from matplotlib.dates import HOURLY, DateFormatter, rrulewrapper, RRuleLocator
import pandas as pd
from datetime import datetime

data = pd.read_csv('LLTiOP010_Calcine.csv', skiprows=4)
data['Datetime'] = pd.to_datetime(data['Timestamp'], format='%Y-%m-%d %H:%M:%S.%f')

start = datetime.strptime(data['Timestamp'][0], '%Y-%m-%d %H:%M:%S.%f')

# rule = rrulewrapper(freq=HOURLY, dtstart=start)
# loc = RRuleLocator(rule)
formatter = DateFormatter('%H:%M')

fig = plt.figure()
plt.plot(data['Datetime'], data['Controller Temp'], label='Controller')
plt.plot(data['Datetime'], data['External Temp'], label='External')
ax = plt.gca()

# ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)

labels = ax.get_xticklabels()
plt.setp(labels, rotation=30, fontsize=10)

plt.show()


