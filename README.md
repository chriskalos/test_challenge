# Test Challenge

## Installation
- Make sure you have Python 3.x installed for your system
- Clone the repo: `git clone https://github.com/chriskalos/test_challenge`
- Navigate to the root directory of the repository
- Create Python virtual environment: `python3 -m venv venv`
- Activate the Python venv: `source ./venv/bin/activate`
- Install requirements: `python3 -m pip install requirements.txt`
- Once the required packages `pytest playwright pytest-playwright` have been installed, run `playwright install`

## How to run
In the root directory of the cloned repo: `python3 -m pytest tests --slowmo 1000 --video on`

### Parameters
#### Enabled by the command above
`--slowmo 1000` ensures Playwright completes actions 1000 milliseconds (1 second) one after another, so that the captured video can be viewed back by humans. **Remove this parameter if you are running this test automatically as part of a test suite, to avoid slowdown.**

`--video on` enables Playwright's default video capture behavior. Videos are stored in the "test-results" directory which is created after each run of the tests.

#### Optional
`--headed` can be used to make the Chromium browser window appear on your screen as Playwright completes the tests. This is opposed to the default "headless" behavior.
`--s

## Language and Libraries

For this assessment, I chose to use Python with the Playwright library.

## Test Plans

## Findings
SauceDemo doesn't check for the Zip/Postal code to be a number/formatted correctly, so the string could be anything.