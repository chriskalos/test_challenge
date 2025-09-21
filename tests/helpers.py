from playwright.sync_api import Page, expect
import logging

def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        encoding='utf-8',
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler("tests_log.txt", mode="w", encoding="utf-8"),
            logging.StreamHandler()
        ],
        force=True
    )

logger = logging.getLogger(__name__)

def login(page: Page):
    logger.info("Starting login process...")

    logger.info("Going to https://www.saucedemo.com/")
    page.goto("https://www.saucedemo.com/")

    # Login sequence
    logger.info("Filling in username 'standard_user' in field with id 'user-name'")
    page.locator('id=user-name').fill('standard_user')
    logger.info("Filling in password 'secret_sauce' in field with id 'password'")
    page.locator('id=password').fill('secret_sauce')
    logger.info("Clicking login button with id 'login-button'")
    page.locator('id=login-button').click()
    
    # Check that we reached the products page
    expect(page.locator('id=page_wrapper')).to_be_enabled # Note: Each time I need to ensure we're on a new page, my strategy is to find a unique element on that page and check that it is present.
    logger.info("Current location: products")