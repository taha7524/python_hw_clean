import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopPurchase:
    @pytest.fixture(autouse=True)
    def setup(self):

        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        
        yield
        self.driver.quit()
    
    def test_add_items_to_cart(self):
        self.driver.get("https://www.saucedemo.com/")
        
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")
        
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        
        inventory_title = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )
        assert inventory_title.text == "Products", "Авторизация не удалась"

        backpack_add_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        backpack_add_button.click()
        
        tshirt_add_button = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        tshirt_add_button.click()

        onesie_add_button = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        )
        onesie_add_button.click()

        cart_badge = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert cart_badge.text == "3", f"Ожидалось 3 товара, но в корзине {cart_badge.text}"
        
        cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()
        
        cart_title = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )
        assert cart_title.text == "Your Cart", "Переход в корзину не удался"
        
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 3, f"Ожидалось 3 товара, но найдено {len(cart_items)}"

        item_names = [item.find_element(By.CLASS_NAME, "inventory_item_name").text 
                     for item in cart_items]
        
        expected_items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt", 
            "Sauce Labs Onesie"
        ]
        
        for expected_item in expected_items:
            assert expected_item in item_names, f"Товар {expected_item} не найден в корзине"
        
        print("Тест успешно завершен! Все товары добавлены в корзину.")