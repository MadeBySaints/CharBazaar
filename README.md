# Project Overview: Tibia Combat Spreadsheet - CharBazaar

This project offers an innovative approach to analyzing a player's progression in Tibia by leveraging data extracted from their bestiary kills. It streamlines the process of generating a detailed spreadsheet that combines the player's kill counts with a comprehensive database of creatures from the game. This analysis allows players to visualize their advancement and strategic engagement with various mobs.

## Functionality and Process

### Data Extraction
Players can easily copy their bestiary kills from the Tibia Character Trades website. This data is then prepared for processing by saving it into a `kills.txt` file.

### Automated Processing
By running the `Generate_Spreadsheet.bat` batch file, the system automatically initiates a series of scripts that enhance and correlate the provided data with a predefined list of game creatures. This process involves:

- **Generating kills2.txt:** A cleaned and standardized version of the original kills data, removing invalid lines and focusing on relevant entries.
- **Producing list2.txt:** A refined compilation of game creatures, excluding those with unknown experience points (denoted by "??") or undefined values ("--"), ensuring only valid and significant data are considered.
- **Creating merged_dataset.csv:** This final output is a meticulously aggregated spreadsheet that combines the refined player kills data with the creature list, providing insights into the player's interactions and achievements within the game's ecosystem.

## Key Features

- **Accuracy and Relevance:** The scripts are designed to filter out irrelevant data, ensuring the analysis focuses solely on creatures with non-zero experience points. This precision ensures the insights derived are both accurate and applicable to the player's progression strategy.

- **Progression Insights:** The merged dataset offers a comprehensive view of the player's bestiary engagement, highlighting the total experience gained from each creature type. This information is invaluable for understanding the player's journey and identifying potential areas for strategic focus.

- **Extensibility:** While the current implementation prioritizes simplicity by directly utilizing available online data for creature statistics, the project is designed with extensibility in mind. Calculations such as experience-to-hit points ratios can be easily integrated for deeper analytical insights.
