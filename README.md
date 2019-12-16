# Argentina Zika Forecating

### About

The purpose of this project is to determine if there is a strong correlation between precipitation (specifically rainfall) and the 2016-2017 Zika outbreak

### Files description

#### Python files for data reading and analysis
- **Clean precipitation data.ipynb**: The Jupyter notebook selects the precipitation data that lies within Argentina for a given month and saves it as a CSV file inside the *data* folder.
- **Exploratory Data Analysis and Results.ipynb**: The Jupyter notebook includes all the analysis code such as reading in the data, formulatind various types of visualizations and more.
- **Reading Precipitation Data.ipynb**: The Jupyter notebook reads in all the precipitation raw HDF5 files and makes a combined CSV file to be used for analysis.
- **agg.py**: The Python script aggregates the data for Zika cases.

#### Data
- **Documentation**: This folder includes the final poster for this project as well as visualizations generated as part of this project inside the *Images* folder.
- **raw_data**: It includes the raw precipitation data from GPM in HDF5 format.
- **shapefiles**: It includes the shapefiles for all of Argentina as well as its various provinces.
- **zika_data**: This folder includes all the Zika cases data. Files in the zika_data directory are aggregated by month, and raw files are grouped by month in the subdirectories of the zika_data directory
- **data.zip**: As combined data had a very large file size, it was compressed and uploaded as a zip file.

#### Other files
- **.gitignore**: Includes all the files and directories not to be included as part of this repository
- **README.md**: This markdown file to describe the repository.

### Project workflow
The workflow of the image is described in the image below:
<img src="/Documentation/Images/workflow.png"/>

Figure 1: Project Workflow

### Analysis
<img src="/Documentation/Images/zika_cases_april_2016.png" height="360px" />

Figure 2: The choropleth map depicting the number of Zika cases in each province in Argentina in April, 2016. 

<img src="/Documentation/Images/rainfall_april_2016.png" height="360px" />

Figure 3: Map of Argentina showing average rainfall spread across Argentina during April, 2016

<img src="/Documentation/Images/rainfall_zika_cases_april_2016.png" height="360px" />

Figure 4: Overlay of Precipitation and Zika Data for April 2016

<img src="/Documentation/Images/rainfall_zika_cases_september_2016.png" height="360px" />

Figure 5: Overlay of Precipitation and Zika Data for September 2016

<img src="/Documentation/Images/rainfall_time_series.png" height="360px" />

<img src="/Documentation/Images/zika_cases_time_series.png" height="360px" />

Figure 6: Time series plots showing the overall precipitation in Argentina and the number of Zika cases from March 2016 to June 2017. 

<img src="/Documentation/Images/zika_cases_per_province.png" height="360px" />

Figure 7:  Box plot showing how the Zika disease data is spread across various provinces

Based on the spatial distribution of precipitation levels and the number of Zika cases there does not seem to be a correlation between the two. For example in Figure 3, April 2016 the highest amount of precipitation is seen in the north-eastern region where as the highest number of Zika cases occur in the upper north-western region (Jujuy and Slata) and to the east (Buenos Aires). Although generally, where there is lower precipitation levels, that is, in the southern parts of Argentina there are a lower number of cases. However, through further analysis of the plots such as Figure 4, a direct relationship between the two datasets is not specifically seen.

Looking at the more general trend, from the line plots we see that the highest number of Zika cases corresponds to a high level of precipitation (April 2016). However, again there does not seem to be a correlation between precipitation levels and the total number of Zika cases. That is, the highest and lowest levels of precipitation do not specifically correspond to the highest and lowest number of Zika cases

This tells us that the precipitation is not the only driving factor affecting the number of Zika cases. Other climatic factors such as temperature and humidity can be having an effect. There are also socioeconomic factors that can be considered such as population density, pollution, deforestation, income levels and water supply to name a few. As such, we produced a box plot (Figure 6) to determine which provinces had the highest number of Zika cases to get an idea of what other factors could be playing a role. We see that the highest number of cases are found in Jujuy which is a rural low income region in Argentina (World Bank, 2018) and the second highest number of cases was in Buenos Aires which has the largest population in Argentina. This can signify that factors related to population could be having a higher influence on the number of  Zika cases.

We considered that the non-correlation could have been attributed to a delayed response in the number of cases to the amount of precipitation. This is so because precipitation affects the first stages in the life cycle of the mosquito, that is, its growth and development before it becomes an adult mosquito where it can act as a vector. However, we would have expected a spike in the number of cases after the high levels of precipitation which occurred in February 2017 but this was not the case. Rather, the number of cases stayed relatively low again pointing to another factor being the main driver. 





