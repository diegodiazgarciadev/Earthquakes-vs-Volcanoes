## Introduction

We will be analyzing 2 datasets from Kaggle; the first one about earthquakes (https://www.kaggle.com/usgs/earthquake-database) and the second one about volcano eruptions (https://www.kaggle.com/jessemostipak/volcano-eruptions).

## Hypothesis
We would like to check if the earthquakes are really along the tectonic plates, then if the volcanic eruptions are following the same distribution as the earthquakes and finally if there is a direct relation between earthquakes and volcano eruptions.

![image](https://user-images.githubusercontent.com/82879300/131387115-2e9b28c1-85b1-4033-8ab0-f257081693cc.png)

## EarthQuakes
First of all we clean our earthquake dataset and we call to google api to get the location of the earthquakes dataseet.

We have our first Map using the coordinates of the earthquakes and this is what we see 

The volcano dataset is divided in 2 csv (there are 5 but we only we will use 2), the volcanoes one and the eruptions. We need to merge both of them to be able to use it correctly.

![image](https://user-images.githubusercontent.com/82879300/131388013-79aaf731-5ccc-4d8a-bd93-478f4ceedd0d.png)

Something that looks like pretty similar to : 

![image](https://user-images.githubusercontent.com/82879300/131388210-b82866a2-da5a-4cc8-9862-c6d433f4badb.png)

## Volcanoes

We need to clean both datasets (Volcanoes, eruptions), then mergin and then show some charts about them:
 * Number of volcanoes and eruptions per country
 * Volcanoes with more number of eruptions
 
![image](https://user-images.githubusercontent.com/82879300/131388875-c7d4c4a6-f7ab-49ab-95fd-f494f7d85718.png)

## Are Volcanic eruptions related with Earthquakes?
Finally we will get the more difficult part. We need to:
  * Reduce the earthquake dataset to fit the same date range as the Volcanoes eruptions
  * Find earthquakes eruptions ocurried the same day or the day before than every volcano eruptions
  * Once we have all the volcano-earthquake susceptible of beeing related, to find the distances between the epicenter of the earthquake and the volcano eruption.
  * Display a histogram of the distances to check if that relation exist
  * Crate a interactive and animated Map showing where is located every volcano and earthquake in every date of possible dates related

![image](https://user-images.githubusercontent.com/82879300/131389735-8c715754-f3c0-4aba-b866-f4e8d8cc7d7c.png)

The distances histogram is folloing a normal distribution what says that in general there is not really a relation between an earthquake and the volcano eruption. We say generally becasue distribution is skewed slightly to the left, so it is poosible that this realion happens in some cases.

Actually after watching for a while the animated map, looks like there are a few times that  volcanoes-earthquakes are close to each other, but this usually happens on East Asia.


![image](https://user-images.githubusercontent.com/82879300/131390327-a3ed8bd4-a4c5-499b-9d63-2036c4a4d32b.png)


Finally I have create a function that calls an API and get news about volcaones ramdonly


![image](https://user-images.githubusercontent.com/82879300/131391069-4c2fe6f0-efc9-4ceb-9243-cdaf466cec69.png)


