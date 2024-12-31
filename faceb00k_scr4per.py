from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Cấu hình trình duyệt Chrome để sử dụng profile người dùng đã đăng nhập
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data\\") # Đường dẫn đến profile của Chrome
options.add_argument("--profile-directory=Default")

# Đường dẫn đến ChromeDriver
chromedriver_path = r"\\192.168.1.22\nam1622share\cao-fb-group\caoFB-python\chromedriver.exe"

# Tạo Service object
service = Service(chromedriver_path)

# Khởi tạo WebDriver với Service
driver = webdriver.Chrome(service=service, options=options)

try:
    # Mở trang nhóm trên Facebook (thay group_url bằng URL của nhóm bạn muốn truy cập)
    group_url = "https://www.facebook.com/groups/620662156508971"
    driver.get(group_url)
    time.sleep(10)  # Chờ trang tải xong

    # Tìm và nhấn nút "Tìm kiếm"
    try:
        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Tìm kiếm']"))
        )
        search_button.click()  # Nhấp vào nút "Tìm kiếm"
        time.sleep(5)  # Chờ giao diện tải xong
    except Exception as e:
        print("Không tìm thấy nút tìm kiếm:", e)

    # Nhập từ khóa và tìm kiếm nếu thanh tìm kiếm xuất hiện
    try:
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Tìm kiếm trong nhóm này']"))
        )
        search_box.send_keys("visa")
        search_box.send_keys(Keys.RETURN)  # Nhấn Enter để tìm kiếm
        time.sleep(10)  # Chờ kết quả tải xong
    except Exception as e:
        print("Không tìm thấy ô nhập từ khóa:", e)

    # Nhấn vào bộ lọc "Gần đây nhất"
    try:
        filter_switch = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Gần đây nhất']"))
        )
        if not filter_switch.is_selected():
            filter_switch.click()  # Bật công tắc "Gần đây nhất"
        time.sleep(10)  # Chờ kết quả cập nhật theo bộ lọc
    except Exception as e:
        print("Không tìm thấy nút bộ lọc 'Gần đây nhất':", e)

    # Tùy chọn: Lấy danh sách các bài viết kết quả và in ra màn hình
    try:
        posts = driver.find_elements(By.XPATH, "//div[@role='article']")
        for post in posts:
            print(post.text)  # In nội dung bài viết
            print("-" * 80)  # Phân cách giữa các bài viết
    except Exception as e:
        print("Không tìm thấy bài viết nào:", e)

finally:
    # Đóng trình duyệt sau khi thực hiện xong
    driver.quit()
