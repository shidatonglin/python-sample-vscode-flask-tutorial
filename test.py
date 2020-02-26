from selenium import webdriver

#$env:CHROMEWEBDRIVER
driver_path = ''
url = 'www.biying.com'

def test():
    print('This is print from azure pipeline')
    driver = webdriver.Chrome(driver_path)
    driver.get(url)

if __name__ == '__main__':
    test()
