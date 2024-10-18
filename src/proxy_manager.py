import random
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver

# Lista de proxies
proxies = [
    {"ip": "47.251.70.179", "port": "80"},    # United States
    {"ip": "79.175.189.88", "port": "1080"},   # Iran
    {"ip": "69.197.135.43", "port": "18080"},  # United States
    {"ip": "160.86.242.23", "port": "8080"},   # Japan
    {"ip": "3.126.147.182", "port": "3128"},   # Germany
    {"ip": "3.123.150.192", "port": "3128"}    # Germany
]

def get_random_proxy():
    return random.choice(proxies)

def configure_proxy_for_selenium():
    selected_proxy = get_random_proxy()

    # Configuración del proxy en Selenium
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = f"{selected_proxy['ip']}:{selected_proxy['port']}"
    proxy.ssl_proxy = f"{selected_proxy['ip']}:{selected_proxy['port']}"

    capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    proxy.add_to_capabilities(capabilities)

    return capabilities
