## Files description - Team 4
### Team Members: Yi Xiang, Yichen Wang, Di Kang, Dongyue Xu

- This repo contains our final report pdf, our base project presentation slides and our extention project presentation slides.

- The final report pdf includes both our base project's report and our extention project's report. 

- some other files description:

Fund summary per neighborhood.xlsx: summary statistics of business fund per license category in each neighborhood, I use excel pivot table to aggregate those statistics.

licenses summary group by neighborhood.xlsx: summary statistics of business license in each neighborhood, I use excel pivot table to aggregate those statistics.

RRF_funds_summary and analysis.xlsx: summary of rental assistance fund of individual applicant in each neighborhood, I use excel pivot table to aggregate those statistics.

boston-neighborhood-summary and analysis.xlsx: summary statistics of demographic profiles such as race, housing size, income in each neighborhood, I use excel pivot table to aggregate those statistics.

RRF.ipynb:
In this file we processed the data of RRF funds (RRF_funds.csv). 
For RRF fund we only take approved fund into consideration, so the approved funds are filtered out and processed to the new csv file Approved_update.csv. We get the histogram of fund amount for each ethnicity by using value_counts method in pandas. From the chart, the top three ethnicity are black, Latino and white.
To make it more explicit, we convert it into a pie chart. Apparently, black/African American ethnicity takes nearly a half, while Latino takes about a quarter, and white takes about one fifth.
Then we draw the heatmap of the fund distribution, saved as Approved_heatmap.html. Obviously, Dorchester has the largest amount of fund among all districts, which is reasonable according to population distribution and income level.

MAR.ipynb:
First I renamed some columns, change some data types, numbering, and fill missing numbers, etc, data cleaning work. I also calculated the monthly average RRF. Then, I append the location information based on each neighborhood's numbers to generate heat maps for the number of RRF to each neighborhood, the total owed and the average owed.

SEP.ipynb:
This one also starts with renaming, changing data type, filling empties, etc, and data cleaning work and also calculating the monthly average RRF. Then added associated locations, to generate the total number of RRFs to each neighborhood, the total owed and the average owed.



   
File descriptions:



