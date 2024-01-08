# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 23:49:02 2024

@author: Jay

The code produces an infographic report based on the UK Box Office data.
The dataset is sourced from the following link: https://core-cms.bfi.org.uk/media/32211/download.
To use the code, download the dataset and ensure both the Python script and the dataset are in the same directory.
My github repository link is https://github.com/JawadDS/DHV_Assignment

"""
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load data from different sheets
annual_admissions_data = pd.read_excel('bfi-yearbook-2022-uk-box-office-2021.xlsx', sheet_name='F1', skiprows=1, nrows=10)
market_share_data = pd.read_excel('bfi-yearbook-2022-uk-box-office-2021.xlsx', sheet_name='F5', skiprows=1, nrows=10)
isba_tv_region_data = pd.read_excel('bfi-yearbook-2022-uk-box-office-2021.xlsx', sheet_name='T3', skiprows=1, nrows=14)
largest_markets_data = pd.read_excel('bfi-yearbook-2022-uk-box-office-2021.xlsx', sheet_name='T1', skiprows=1, nrows=15)

# Create a subplot with 2 rows and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(22, 20), gridspec_kw={'hspace': 0.2})
fig.suptitle('UK Box Office Insights (2012-2021)', fontsize=25)

# Plot 1: Line Plot for Annual UK Cinema Admissions
axs[0, 0].plot(annual_admissions_data['Year'], annual_admissions_data['Admissions (million)'], marker='o')
axs[0, 0].set_title('Annual UK Cinema Admissions (2012-2021)', fontsize=20, color='red')
axs[0, 0].set_xlabel('Year')
axs[0, 0].set_ylabel('Admissions (million)')
axs[0, 0].grid(True)

# Plot 2: Bar Plot for Market Share of Top 20, 21-50, 51-100, and Rest of Films
market_share_data.plot(x='Year', kind='bar', stacked=True, colormap='viridis', ax=axs[0, 1])
axs[0, 1].set_title('Market Share of Films (2012-2021)', fontsize=20, color='red')
axs[0, 1].set_xlabel('Year')
axs[0, 1].set_ylabel('Percentage Share')
axs[0, 1].legend(title='Film Category', bbox_to_anchor=(1.05, 1), loc='upper left')
axs[0, 1].grid(axis='y')

# Plot 3: Pie Chart for Cinema Admissions by ISBA TV Region
wedges, texts, autotexts = axs[1, 0].pie(
    isba_tv_region_data['Admissions (million)'],
    labels=isba_tv_region_data['Region'],
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(width=0.4, edgecolor='w'),  # Adjust wedge width and edge color
    textprops=dict(color='black'),  # Set text color
)
axs[1, 0].set_title('Cinema Admissions by ISBA TV Region (2021)', fontsize=20, color='red')

# Plot 4: Bar Chart for 15 Largest Markets by Admissions (2021)
largest_markets_data.plot(x='Territory', y=['Admissions 2019 (million)', 'Admissions 2020 (million)', 'Admissions 2021 (million)'], kind='bar', colormap='viridis', ax=axs[1, 1])
axs[1, 1].set_title('15 Largest Markets by Admissions (2019-2021)', fontsize=20, color='red')
axs[1, 1].set_xlabel('Territory')
axs[1, 1].set_ylabel('Admissions (million)')

# Place legend inside the top right
axs[1, 1].legend(title='Year', bbox_to_anchor=(1, 1), loc='upper right')  # Adjusted location

axs[1, 1].grid(axis='y')



# Add space between bottom two plots and text
fig.subplots_adjust(bottom=0.17)

# Text Box
fig.text(0.02, 0.02, 'This dashboard explores the UK cinematic environment from 2012 to 2021 with this informative infographic. The first plot shows the annual box office receipts and reveals a significant drop in 2020, which is probably due to world events. The second plot explores the dynamics of top films market shares and shows how audience tastes have changed over time. The distribution of moviegoers in 2021 is depicted in greater detail in the third plot by examining theater admissions in various locations. The performance of the top 15 markets by admissions in 2019–2020 and 2021 is finally shown in the fourth graphic. When combined, these visualizations provide insightful information about how the UK film industry is changing.',
         ha='left', va='bottom', fontsize=20, wrap=True)

# Your name and student ID
fig.text(0.95, 0.95, 'Name: Jawad Iqbal\nStudent ID: 22093598', ha='right', va='top', fontsize=20)

# Save the entire infographic as an image
plt.savefig("22093598.png", dpi=300)
