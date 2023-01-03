# Team Report for Deliverable 1

[Link to repo](https://github.com/BU-Spark/ds-councilor-mejia-city-services/tree/team-5)

[Refined Goals](https://github.com/BU-Spark/ds-councilor-mejia-city-services/blob/team-5/fall22-team-5/deliverables/deliverable1/updated_project_scope.md)

### 1. Where did business assistance go during the pandemic? What were the demographic profiles of the communities where the businesses were located?

#### Answered by: Amy

- In the Demographics Analysis Jupyter Notebook, we analyzed different neighborhoods in Boston as well as their demographic makeups.
- We first analyzed each of the 23 neighborhoods in Boston and visualized their race distribution in a bar chart. With this information, we could easily observe the diversity of each neighborhood, and the most prominent races in their populations. For instance, a majority of Brighton's population idenitifies as "White alone," Dorchester has more residents that identify as "Black or African American alone" compared to the other race groups, and nearly half of East Boston's population identifies as "Hispanic or Latino."
- We then analyzed each race indentifier to see each of their distributions across the 23 neighborhoods. For instance, we saw that those indentifying as "White alone" were almost equally distributed amongst the neighborhoods, compared to those indentifying as "Hispanic or Latino," which are most concentrated in East Boston, Dorchester, and Roxbury.
- As we continue our analysis, we must also consider the significant difference in populations between the neighborhoods, and take that into account.
- We will be using this analysis to identify which neighborhoods have been receiving the most relief and/or business licenses. Afterwards, we will be able to determine if these benefits are being equitably distributed.
- For us to make this conclusion, we must answer these questions first, which may be answered by the client:
	- Where are the equity communities? 
	- Where was the funding intended to go? Is this based on demographic makeup?
	- What is the minimum threshold that must be reached in order to conclude that the city's equity goals can be achieved?


### 3. Where are the city’s economic development licenses? Which communities are benefitting? Which communities are being left out?

#### Answered by: Rithvik, Haowei

- Looking at the Business licenses Jupyter Notebook, we are analyzing food, alcohol, cannabis and general licenses in the GBA.
- In addition, take note of the map displayed that shows the locations for each of those licenses. Red points indicate general licenses, food indicates food, yellow indicates alcohol and lime indicates cannabis. The general licenses overlap with many of the specific licenses. From the map, you can see that many of the licenses are concentrated around the city center of Boston and become more sparse the further away they are from the center.
- As for the number of licenses per city, in each dataset Boston, Dorchester and East Boston have some of the highest amounts of licenses, while Hyde Park, Chestnut Hill and Mattapan have some of the lowest amounts of licenses. It's hard to say whether this gap is due to the difference in population, population density or difference in funding given the limits current dataset, but once we start to merge this information with some of the other provided datasets we may find a clearer reason as to why this is the case.
- We also analyzed the amount of food licenses specific to take out, which is especially relevant given a global pandemic or any future public health emergency. Again, this is consistent with the above findings, suggesting on a surface level that those communities on the lower end may not be prepared for a situation where restaurants are closed for dine-in
- Finally, we have analyzed the relative time periods where licenses are being issued. Liquor licenses and general licenses have seldom been issued since 2014, whereas food licenses are increasingly being issued. As for license expiry dates, they mostly seem to be located about 1-2 years in the future, suggesting that businesses do not have a lot of time to update their licenses.
- Some more questions that can eventually be answered with this data:
	- How do business licenses compare by different "Doing Business As" names in different cities? Do certain businesses dominate certain cities?
	- How do opening and closing times compare across different cities? Does that impact the number of businesses in that area?
	- How are businesses distributed by license category or type?
	- Look further into Cannabis dataset: map out different application statuses, and the split of facilities seeking Boston Equity Program and where they arre respectively located, map out different types of Marijuana Licenses.

- Based on capital budget analysis by categories, we found Boston City spent tremendous amount on education and public work. 
- Based on community, Charlestown seems to be benefit heavily from it for public work and education. Other than Charlestown, Chinatown and Downtown areas gain a lot of city fundings. And fundings dramatically decreases for other communities especially rural areas.
- The estimation for the 2025 budgets skyrocketed and possibly due to inflation from the pandemic.
