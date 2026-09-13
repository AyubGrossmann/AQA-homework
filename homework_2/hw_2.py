import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("1. Запуск Firefox...")
driver = webdriver.Firefox()
driver.maximize_window()

try:
    print("2. Переход на страницу оплаты...")
    driver.get("https://itcareerhub.de")
    time.sleep(5)

    print("3. Проверка баннера Cookie...")
    try:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'AKZEPTIEREN') or contains(text(), 'Принять')]"))
        )
        driver.execute_script("arguments.click();", cookie_button)
        print("-> Баннер Cookie успешно закрыт.")
        time.sleep(2)
    except Exception:
        print("-> Баннер Cookie не найден или не мешает экрану.")

    print("4. Создание скриншота...")
    driver.save_screenshot("payment_methods.png")
    print("\n[УСПЕХ] Скриншот успешно сохранен как 'payment_methods.png'!")

except Exception as e:
    print(f"\n[ОШИБКА] Не удалось выполнить скрипт: {e}")

finally:
    print("5. Закрытие браузера.")
    driver.quit()