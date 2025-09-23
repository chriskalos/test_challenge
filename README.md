# Test Challenge

## Installation
- Make sure you have Python 3.x installed on your system
- Clone the repo: `git clone https://github.com/chriskalos/test_challenge`
- Navigate to the root directory of the cloned repository (`cd test_challenge`)
- Create Python virtual environment: `python3 -m venv venv`
- Activate the Python venv: `source ./venv/bin/activate`
- Install requirements: `python3 -m pip install requirements.txt`
- Once the required packages `pytest playwright pytest-playwright` have been installed, run `playwright install`

## How to run
In the root directory of the cloned repo: `python3 -m pytest tests --slowmo 1000 --video on`

### Parameters
#### Enabled by the command above
`--slowmo 1000` ensures Playwright completes actions 1000 milliseconds (1 second) one after another, so that the captured video can be meaningfully viewed back by humans. **Remove this parameter if you are running this test automatically as part of a test suite, to avoid slowdown.**

`--video on` enables Playwright's default video capture behavior. Videos are stored in the "test-results" directory which is created after each run of the tests.

#### Optional
`--headed` can be used to make the Chromium browser window appear on your screen as Playwright completes the tests. This is opposed to the default "headless" behavior.

## Implementation Notes

For this assessment, I chose to use Python, with pytest and Playwright for testing and browser automation respectively. Logs are automatically created in a file called "tests_log.txt", which is created automatically. This behavior can be adjusted by configuring the parameters within `conftest.py`.

### Logging and Monitoring
Both test plans include comprehensive logging mechanisms that capture:
- Test execution steps and progress
- Debug information for troubleshooting
- Validation checkpoints and results
- Error conditions and handling
- Performance timing information

### Framework Integration
The test plans utilize:
- **Pytest:** For test organization and execution
- **Playwright:** For browser automation and interaction
- **Python Logging:** For comprehensive test documentation
- **Helper Functions:** For common operations like login
- **Page Object Model:** For maintainable test code structure

## Test Plans

Check test_plan_1.md and test_plan_2.md

## Extra Findings
SauceDemo doesn't check for the Zip/Postal code to be a number/formatted correctly, so the string could be anything.