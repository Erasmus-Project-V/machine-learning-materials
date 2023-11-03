import matplotlib.pyplot as plt
import pandas as pd

df_weather = pd.read_csv("dataframes/weather_2016_2020_daily.csv")
df_weather = df_weather.iloc[:30, :]
df_weather = df_weather.sort_values(by="Day")
print(df_weather)

x_1 = df_weather["Day"].values
y_1 = (df_weather["Temp_max"].values + df_weather["Temp_min"].values)/2

y_2 = df_weather["Precipit"].values

print(y_1)
fig = plt.figure(figsize=(10, 6))
axes = fig.add_axes((0.1, 0.1, 0.8, 0.8))
axes.set_title("Temperature in June 2016, (averaged)")
axes.set_ylabel("Temperature/F",color="r")
axes.set_xlabel("Day of month")
axes.set_ylim(0,100)
axes.plot(x_1,y_1,lw=2,color="red",marker="o",markersize=5,
          markerfacecolor="k")
axes.grid(True,color="0.6",dashes=[3,3])

# instancira axes na istom mjestu kao i prijašnji, ovako
# ćemo dobiti ylabel na desnoj strani
axes_2 = axes.twinx()
axes_2.set_ylim(0,200)
axes_2.set_ylabel("Precipitation/mm",color="b")

#simple bar chart
axes_2.bar(x_1,y_2)


fig.show()
fig.savefig("saved_imgs/weather_data.jpg")