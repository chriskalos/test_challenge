from playwright.sync_api import Page, expect
import helpers
import random
import logging

logger = logging.getLogger(__name__)

def test_products(page: Page):
    logger.info("Starting test 2")
    helpers.login(page)

    logger.info("Adding two random products to the cart")
    # Add two random products to the cart
    # find inventory_list and count all its inventory_item items
    shop_items = page.locator('.inventory_item').all()
    logger.debug(f"shop_items: {shop_items}")
    
    # pick two inventory_item at random
    random_items = random.sample(shop_items, 2)
    logger.debug(f"random_items: {random_items}")

    # Create a list to hold the names and prices of the two items for later comparison
    selected_items = []
    selected_prices = []
    logger.debug(f"Lists created: selected_items, selected_prices")

    for i in random_items:
        logger.debug(f"i = {i}")
        logger.info("Putting each item's relevant data in variables to track")

        item_name = i.locator('.inventory_item_name').inner_text()
        item_price = i.locator('.inventory_item_price').inner_text()

        logger.debug(f"Appending {item_name} to selected_items")
        selected_items.append(item_name)
        logger.debug(f"Appending {item_price} to selected_prices")
        selected_prices.append(item_price)

        # Find the <button> within and press it to add to cart
        i.locator('button').click()

    # Go to the cart page
    logger.info("Clicking button with data-test 'shopping-cart-link'")
    page.locator('data-test=shopping-cart-link').click()
    expect(page.locator('id=cart_contents_container')).to_be_enabled()
    logger.info("Current location: shopping cart")

    # Check that two items are in cart and that they are the same items as before
    cart_items = page.locator('.cart_item').all()
    logger.debug(f"{cart_items}")
    
    logger.info("Checking that the two items are still correct")
    for i in range(2):
        logger.debug(f"i = {i}")
        expect(cart_items[i].locator('.inventory_item_name')).to_have_text(selected_items[i])
        logger.debug(f".inventory_item_name = {cart_items[i].locator('.inventory_item_name').text_content}")
        expect(cart_items[i].locator('.inventory_item_price')).to_have_text(selected_prices[i])
        logger.debug(f".inventory_item_price = {cart_items[i].locator('.inventory_item_price').text_content}")

    # Click the Checkout button
    logger.info("Clicking button with id 'checkout'")
    page.locator('id=checkout').click()

    # Check that we reached the next checkout page
    expect(page.locator('.checkout_info')).to_be_enabled
    logger.info("Current location: checkout page")

    # Complete the form
    logger.info("Filling shipping form with 'Test'")
    count = page.locator('.form_group input').count()
    for i in range(0,count):
        page.locator('.form_group input').nth(i).fill('Test')
   
    # Click the Continue button
    page.locator('id=continue').click()

    # Check that we're on the summary page
    expect(page.locator('.summary_info'))
    logger.info("Current location: summary page")
    
    # Check again that the two items are correct
    expect(page.locator('.cart_item').nth(0).locator('.inventory_item_name')).to_have_text(selected_items[0])
    expect(page.locator('.cart_item').nth(0).locator('.inventory_item_price')).to_have_text(selected_prices[0])
    expect(page.locator('.cart_item').nth(1).locator('.inventory_item_name')).to_have_text(selected_items[1])
    expect(page.locator('.cart_item').nth(1).locator('.inventory_item_price')).to_have_text(selected_prices[1])

    logger.info(f"Finished test 2\n")