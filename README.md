# Test Challenge

## Please install requirements.txt before running!
Once the required packages `pytest playwright pytest-playwright` have been installed, please run `playwright install`.

## How to run
In the root directory: `python3 pytest tests`

## Findings
SauceDemo doesn't check for the Zip/Postal code to be a number/formatted correctly, so the string could be anything.