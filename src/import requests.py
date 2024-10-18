'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Lista de proxies
proxies = [
    {"ip": "47.251.70.179", "port": "80"},    # United States
    {"ip": "79.175.189.88", "port": "1080"},   # Iran
    {"ip": "69.197.135.43", "port": "18080"},  # United States
    {"ip": "160.86.242.23", "port": "8080"},   # Japan
    {"ip": "3.126.147.182", "port": "3128"},   # Germany
    {"ip": "3.123.150.192", "port": "3128"}    # Germany
]



# Iterar sobre cada proxy
for proxy in proxies:
    print(f"Usando el proxy: {proxy['ip']}:{proxy['port']}")

    # Configuración del ChromeDriver con el proxy
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=%s:%s' % (proxy['ip'], proxy['port']))

    service = Service('G:\\Estudio\\Python 3\\Bot-Citas\\chromedriver.exe')# Reemplaza con la ruta correcta de tu chromedriver
    chrome = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Navegar al sitio que muestra la IP pública
        chrome.get("http://checkip.amazonaws.com")
        body_text = chrome.find_element(By.TAG_NAME, 'body').text
        print(f"IP vista desde el servidor: {body_text.strip()}")
    
    except Exception as e:
        print(f"Error al usar el proxy {proxy['ip']}:{proxy['port']}: {e}")
    
    finally:
        chrome.quit()
'''