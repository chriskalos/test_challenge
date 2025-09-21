from playwright.sync_api import Page, expect
import helpers
import random
import logging

logger = logging.getLogger(__name__)

def test_products(page: Page):
    helpers.login(page)

    # Add two random products to the cart
    # find inventory_list and count all its inventory_item items
    shop_items = page.locator('.inventory_item').all()
    
    # pick two inventory_item at random
    random_items = random.sample(shop_items, 2)

    # Create a list to hold the names and prices of the two items for later comparison
    selected_items = []
    selected_prices = []

    for i in random_items:
        # put each item's relevant data in variables to track
        item_name = i.locator('.inventory_item_name').inner_text()
        item_price = i.locator('.inventory_item_price').inner_text()

        selected_items.append(item_name)
        selected_prices.append(item_price)
        item_button = i.locator('button')

        # and find the <button> within and press it
        item_button.click()

    # Go to the cart page
    page.locator('data-test=shopping-cart-link').click()
    expect(page.locator('id=cart_contents_container')).to_be_enabled()

    # check that two items are in cart and that they are the same items as before
    cart_items = page.locator('.cart_item').all()
    
    for i in range(2):
        expect(cart_items[i].locator('.inventory_item_name')).to_have_text(selected_items[i])
        expect(cart_items[i].locator('.inventory_item_price')).to_have_text(selected_prices[i])

    # Click the Checkout button
    page.locator('id=checkout').click()

    # Complete the form
    count = page.locator('.form_group input').count()
    for i in range(0,count):
        page.locator('.form_group input').nth(i).fill('Test')
   
    # Click the Continue button
    page.locator('id=continue').click()
    
    # Check again that the two items are correct
    expect(page.locator('.cart_item').nth(0).locator('.inventory_item_name')).to_have_text(selected_items[0])
    expect(page.locator('.cart_item').nth(0).locator('.inventory_item_price')).to_have_text(selected_prices[0])
    expect(page.locator('.cart_item').nth(1).locator('.inventory_item_name')).to_have_text(selected_items[1])
    expect(page.locator('.cart_item').nth(1).locator('.inventory_item_price')).to_have_text(selected_prices[1])