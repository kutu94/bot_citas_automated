from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def start_browser():
    # Configuración del navegador
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--incognito')

    # Ruta al ChromeDriver
    service = Service('G:\Estudio\Python 3\Bot-Citas\chromedriver.exe')  # Cambia esta ruta según tu sistema

    # Inicializar el navegador
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def open_website(driver, url):
    driver.get(url)

def select_province(driver, province_name):
    try:
        # Esperar hasta que el menú desplegable de provincias esté disponible
        province_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'form'))
        )
        Select(province_select).select_by_visible_text(province_name)
        print(f"Provincia seleccionada: {province_name}")

        # Esperar a que el botón "Aceptar" esté disponible y presionarlo
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btnAceptar'))
        )
        accept_button.click()
        print("Botón 'Aceptar' presionado")
    except Exception as e:
        print(f"Error al seleccionar la provincia: {str(e)}")
        driver.save_screenshot('select_province_error.png')

def select_office_and_procedure(driver):
    try:
        # Seleccionar oficina
        office_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'sede'))
        )
        Select(office_select).select_by_visible_text("CNP AVDA POBLADOS, Avda. de los Poblados, S/N")

        # Seleccionar trámite
        procedure_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'tramiteGrupo[0]'))
        )
        Select(procedure_select).select_by_visible_text('ASILO - PRIMERA CITA-provincia de Madrid')

        # Presiona el botón "Aceptar" usando su ID
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btnAceptar'))
        )
        accept_button.click()
        print("Botón 'Aceptar' presionado")
    except Exception as e:
        print(f"Error al seleccionar la oficina y el trámite: {str(e)}")
        driver.save_screenshot('select_office_procedure_error.png')

def accept_information(driver):
    try:
        # Esperar a que aparezca el botón "Aceptar" y hacer clic en él
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btnEntrar'))
        )
        accept_button.click()
        print("Botón 'Entrar' en la pantalla de información presionado")
    except Exception as e:
        print(f"Error al aceptar la información: {str(e)}")
        driver.save_screenshot('accept_information_error.png')

def select_document_type(driver, doc_type):
    try:
        if doc_type == 'PASAPORTE':
            document_type_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'rdbTipoDocPas'))
            )
            document_type_element.click()
        elif doc_type == 'NIE':
            document_type_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'rdbTipoDocNie'))
            )
            document_type_element.click()
        elif doc_type == 'DNI':
            document_type_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'rdbTipoDocDni'))
            )
            document_type_element.click()
        print(f"Tipo de documento seleccionado: {doc_type}")
    except Exception as e:
        print(f"Error al seleccionar el tipo de documento: {str(e)}")
        driver.save_screenshot('select_document_type_error.png')

def enter_document_number(driver, doc_number):
    try:
        # Ingresar número de documento
        doc_number_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'txtIdCitado'))
        )
        doc_number_input.send_keys(doc_number)
        print(f"Número de documento ingresado: {doc_number}")
    except Exception as e:
        print(f"Error al ingresar el número de documento: {str(e)}")
        driver.save_screenshot('enter_document_number_error.png')

def enter_name(driver, name):
    try:
        # Ingresar nombre y apellidos
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'txtDesCitado'))
        )
        name_input.send_keys(name)
        print(f"Nombre y apellidos ingresados: {name}")
    except Exception as e:
        print(f"Error al ingresar el nombre y apellidos: {str(e)}")
        driver.save_screenshot('enter_name_error.png')

def enter_birth_year(driver, birth_year):
    try:
        # Ingresar año de nacimiento
        birth_year_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'txtAnnoCitado'))
        )
        birth_year_input.send_keys(birth_year)
        print(f"Año de nacimiento ingresado: {birth_year}")
    except Exception as e:
        print(f"Error al ingresar el año de nacimiento: {str(e)}")
        driver.save_screenshot('enter_birth_year_error.png')

def select_nationality(driver, nationality):
    try:
        # Seleccionar país de nacionalidad
        nationality_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'txtPaisNac'))
        )
        Select(nationality_select).select_by_visible_text(nationality)
        print(f"País de nacionalidad seleccionado: {nationality}")
    except Exception as e:
        print(f"Error al seleccionar la nacionalidad: {str(e)}")
        driver.save_screenshot('select_nationality_error.png')

def request_appointment(driver):
    try:
        # Esperar a que el botón "Solicitar Cita" esté disponible y hacer clic en él
        request_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btnEnviar'))
        )
        request_button.click()
        print("Botón 'Solicitar Cita' presionado")
    except Exception as e:
        print(f"Error al solicitar la cita: {str(e)}")
        driver.save_screenshot('request_appointment_error.png')

def handle_no_appointments(driver):
    try:
        # Esperar a que aparezca el botón "Salir" y hacer clic en él
        exit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btnSalir'))
        )
        exit_button.click()
        print("No hay citas disponibles. Botón 'Salir' presionado")
    except Exception as e:
        print(f"Error al manejar la no disponibilidad de citas: {str(e)}")
        driver.save_screenshot('handle_no_appointments_error.png')

# Ejemplo de datos de la persona
persona_info = {
    "doc_type": "PASAPORTE",
    "doc_number": "J56667GG",
    "name": "JUAN PEREZ",
    "birth_year": "1997",
    "nationality": "GUATEMALA",
    "province": "Madrid",
    "procedure": "ASILO - PRIMERA CITA-provincia de Madrid"
}

if __name__ == "__main__":
    driver = start_browser()

    # Navegar al sitio
    open_website(driver, "https://icp.administracionelectronica.gob.es/icpplus/index.html")

    # Seleccionar la provincia y hacer clic en "Aceptar"
    select_province(driver, persona_info["province"])

    # Seleccionar la oficina específica y hacer clic en "Aceptar"
    select_office_and_procedure(driver)

    # Aceptar la pantalla de información
    accept_information(driver)

    # Seleccionar el tipo de documento
    select_document_type(driver, persona_info["doc_type"])

    # Ingresar el número de documento, nombre, año de nacimiento, y nacionalidad
    enter_document_number(driver, persona_info["doc_number"])
    enter_name(driver, persona_info["name"])
    enter_birth_year(driver, persona_info["birth_year"])
    select_nationality(driver, persona_info["nationality"])

    # Intentar solicitar la cita
    try:
        request_appointment(driver)
    except:
        handle_no_appointments(driver)

    # Cerrar el navegador al terminar (opcional mientras haces pruebas)
    input("Presiona Enter para cerrar el navegador...")
    driver.quit()
