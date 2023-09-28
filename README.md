# RealEstateScrape-Dashboard

# Description

Welcome to the RealEstateScrape-Dashboard project, developed as part of our Master's program in Data Science at the Faculty of Economics and Management. This project focuses on scraping real estate data from a website, storing it in a CSV format database, and creating an interactive dashboard for data visualization and analysis.

# Project Objectives

**Web Scraping:** We scrape data from a real estate website, extracting essential information from property listings such as price, area, number of rooms, postal code, and more. This data is collected and processed for further analysis.

**Data Enrichment:** We enhance the dataset by adding additional variables, including the price per square meter and the average price per square meter for each region.

**Geo-spatial Integration:** We incorporate a GeoJSON-format database, merging it with a portion of our enriched data. This integration enables us to display a map of France with regional boundaries, providing a clear visual representation of different regions.

**Interactive Dashboard:** Using Streamlit, we create an interactive dashboard that simplifies apartment searches. The dashboard allows users to apply filters and specific criteria, view various trends through charts and histograms, and explore the map displaying regional average prices per square meter. This user-friendly interface enhances data exploration and understanding.

## Project Structure

The project is organized as follows:

- **`IMMO_FINAL.ipynb`**: This file contains the web scraping code used to collect data from the real estate website.('https://www.lesiteimmo.com')

- **`IMMO_NETTOYAGE.ipynb`**: This file contains the code responsible for cleaning the scraped data and augmenting it with additional variables such as price per square meter and regional information.

- **`Data_geojson.ipynb`**: This directory contains code and files used to create a fused dataset that combines region coordinates, geospatial data, and a subset of the scraped data.

- **`streamlit.py`**: This file contains the code for creating the interactive dashboard using Streamlit.
  
- **`config.toml`**: This file contains configuration settings, including background customization and font modifications, for the dashboard.

Feel free to explore these files to gain a better understanding of how the project is organized and functions.


## Getting Started

To run this project, you have two options:

### Method 1: Scraping, Data Cleaning, and GeoJSON Creation

1. **Scraping and Data Collection**:
   - Run the `IMMO_FINAL.ipynb` file to scrape real estate data from the website and save it to CSV files in the `data` directory. Modify the scraping code in `IMMO_FINAL.ipynb` as needed to target specific data.

2. **Data Cleaning and Augmentation**:
   - Use the `IMMO_NETTOYAGE.ipynb` file to clean the scraped data and add variables such as price per square meter and regional information. This will result in an enriched dataset.

3. **GeoJSON Creation**:
   - Run the code in the `Data_geojson.ipynb` Jupyter Notebook to create GeoJSON files that combine region coordinates, geospatial data, and a subset of the enriched data. Save the resulting GeoJSON files in the `geo_data` directory.

4. **Set Up Configuration**:
   - Open the `config.toml` file and specify background settings and font modifications as needed for your dashboard's appearance.

5. **Launch Streamlit Dashboard**:
   - Ensure you have Streamlit installed by running `pip install streamlit`.
   - Place the `streamlit.py` and `config.toml` files in the same directory.
   - Open your terminal or command prompt.
   - Navigate to the directory containing the `streamlit.py` and `config.toml` files.
   - Run the following command to launch the Streamlit dashboard:
     ```
     streamlit run streamlit.py
     ```
6. **Interact with the Dashboard**:
   - Open a web browser and navigate to the URL provided in the terminal after running the Streamlit command. You can now interact with the dashboard, apply filters, explore data trends, and view the map with regional average prices per square meter.


  
To quickly get started with the project using provided datasets, follow these steps:

### Method 2: Downloading Provided Datasets and Running the Interactive Dashboard

1. **Download Provided Datasets**:
   - Obtain the provided datasets containing pre-scraped data and GeoJSON files. You should have CSV files with the scraped data and GeoJSON files for geospatial information.

2. **Set Up Configuration**:
   - Open the `config.toml` file and specify background settings and font modifications as needed for your dashboard's appearance.

3. **Place Files in the Same Directory**:
   - Make sure you have the `streamlit.py` and `config.toml` files in the same directory as the downloaded datasets.

4. **Launch Streamlit Dashboard**:
   - Ensure you have Streamlit installed by running `pip install streamlit`.
   - Open your terminal or command prompt.
   - Navigate to the directory containing the `streamlit.py`, `config.toml`, and downloaded datasets.
   - Run the following command to launch the Streamlit dashboard:
     ```
     streamlit run streamlit.py
     ```

5. **Interact with the Dashboard**:
   - Open a web browser and navigate to the URL provided in the terminal after running the Streamlit command. You can now interact with the dashboard, apply filters, explore data trends, and view the map with regional average prices per square meter.

Feel free to choose the method that suits your needs, whether you want to collect and process data or simply explore the dashboard. Happy analyzing!


## Dashboard Preview

Here's a visual preview of our interactive dashboard:

### Main Dashboard

<img width="1244" alt="Aperçu" src="https://github.com/Mehddi67/RealEstateScrape-Dashboard/assets/125468498/d417819b-a425-47a5-8ca1-b8ee9ab18012">
*Image 1 Description:This provides a glimpse of the main dashboard header.*

### Regional Map

<img width="1234" alt="Map of France" src="https://github.com/Mehddi67/RealEstateScrape-Dashboard/assets/125468498/9d403f09-ef18-485f-a6bc-96c927554a21">
*Image 2 Description: *

### Price Trends Chart

<img width="1238" alt="Chart" src="https://github.com/Mehddi67/RealEstateScrape-Dashboard/assets/125468498/a44e56f8-8f95-4799-9f88-71e2473ab386">
*Image 3 Description: *

### Filter Options

<img width="1196" alt="Filter" src="https://github.com/Mehddi67/RealEstateScrape-Dashboard/assets/125468498/4be4fe43-228a-4fab-86b6-c22ff166b112">
*Image 4 Description:*





