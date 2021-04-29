# Automation-Homework
The Automation Home Assignment has two components: 
1. Python - Scrapy webscraping and Google Drive uploader
2. Google App Script - Spreadsheet parsing, Google Forms creation and email sending

## Requirements
The Python part of the automation has been developed with **Python 3.9.2**, so 3.9 is recommended, but theoretically anything above 3.6 should work.

## Installation:
launch command prompt, run below commands:
1. pip install pyquery
2. pip install schedule


Google App script : 
1. Have Gmail account
2. Have access to Google Drive
3. Go to https://script.google.com
4. Create a new project, copy code from code.gs in this repo to your code.gs
5. Enable Google Sheets API by clicking on the plus button next to the Services text on the left side. 
6. Run the job
 
 
## Running the application
If you followed the installation steps correctly, the commands below should scrape IMDB and upload a Google Sheet containing the top5 results 

``` 
python main.py
```


## Setting up the automation
Webscraping is set to run automatically every Thursday at 1:09am
Google App Script is set to run at every Thursday at 2:09am
Or, Click on the alarm clock icon/triggers menu, add a trigger with the following settings: week timer, every Thursday, 2-3 AM
