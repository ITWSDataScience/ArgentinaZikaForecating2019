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
