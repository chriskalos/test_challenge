from playwright.sync_api import Page, expect
from itertools import product
from helpers import configure_logging
import helpers
import logging

logger = logging.getLogger(__name__)

def test_shipping(page: Page):
    logger.info(f"Starting test 1")
    helpers.login(page)

    # Find the backpack, add it to cart
    logger.info("Clicking button with id 'add-to-cart-sauce-labs-backpack'")
    page.locator('id=add-to-cart-sauce-labs-backpack').click()

    # Go to the cart page
    logger.info("Clicking button with id 'shopping-cart-link'")
    page.locator('data-test=shopping-cart-link').click()
    expect(page.locator('id=cart_contents_container')).to_be_enabled()
    logger.info("Current location: shopping cart")
    
    # Check that the item was actually added to the cart
    expect(page.locator('data-test=inventory-item')).to_be_enabled
    logger.info("Item exists in cart")
    expect(page.locator('data-test=inventory-item-name')).to_contain_text('Sauce Labs Backpack')
    logger.debug(f"Item name: {page.locator('data-test=inventory-item-name').text_content}")

    # Press the Checkout button
    logger.info("Clicking button with id 'checkout'")
    page.locator('id=checkout').click()

    # Check that we reached the next checkout page
    expect(page.locator('.checkout_info')).to_be_enabled
    logger.info("Current location: checkout page")

    # Find all the form_group elements and count them
    form_inputs = page.locator('.form_group input')
    logger.debug(f"form_inputs: {form_inputs}")
    count = form_inputs.count()
    logger.debug(f"count: {count}")

    # Fill and unfill fields in a binary manner to test all possible combinations
    logger.info("Trying all possible combinations of filled/unfilled fields...")
    for combo in product([0,1], repeat=count):
        for i, fill_flag in enumerate(combo):
            logger.debug(f"i = {i}, fill_flag = {fill_flag}")
            if fill_flag:
                logger.debug(f"Filling field {form_inputs.nth(i)} with 'Test'")
                form_inputs.nth(i).fill('Test')
            else:
                logger.debug(f"Unfilling field {form_inputs.nth(i)}")
                form_inputs.nth(i).fill('')
        
        # Click the Continue button
        logger.info("Clicking button with id 'continue'")
        page.locator('id=continue').click()

        if all(combo):
            # All fields were filled so we expect the next page to appear
            logger.info("All fields filled with 'Test'")
            expect(page.locator('id=checkout_summary_container')).to_be_enabled
        else:
            # Expect an error message every time an argument is not filled
            expect(page.locator('data-test=error')).to_be_enabled
            logger.debug(f"Error message present. Continuing.")

    # Check that we're on the summary page
    expect(page.locator('.summary_info'))
    logger.info("Current location: summary page")

    # Finish test by completing the whole checkout process
    logger.info("Finishing test - clicking button with id 'finish'")
    page.locator('id=finish').click()

    logger.info(f"Finished test 1\n")