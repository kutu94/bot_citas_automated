Bot de Citas Automatizado
Este bot automatiza el proceso de solicitar citas a través de un navegador utilizando Selenium y proxies para navegar con diferentes direcciones IP.

Funcionalidades
Uso de proxies: El bot utiliza una lista de proxies para cambiar la dirección IP en cada solicitud y evitar bloqueos.
Automatización de Selenium: Automatiza la navegación por el sitio web, selecciona provincia, oficina, procedimiento y solicita la cita.
Manejo de errores: Si ocurre algún error durante la navegación, el bot captura una captura de pantalla y maneja los errores para continuar con el proceso.

Requisitos
Selenium: El bot usa Selenium para automatizar la navegación del sitio web.
Chromedriver: Necesitas descargar el archivo chromedriver.exe correspondiente a la versión de tu navegador Chrome y especificar su ruta en el código.
Instalación de dependencias

Para instalar todas las dependencias, ejecuta el siguiente comando:
pip install -r requirements.txt

Estructura del proyecto

/bot_citas_automated
│
├── /scripts               # Carpeta para todos los scripts Python
│   ├── import_requests.py    # Manejo de proxies
│   ├── navigation.py         # Manejo de la navegación con Selenium
│   ├── proxy_manager.py      # Manejo y configuración de proxies en Selenium
│   ├── __init__.py           # Para definir la carpeta como un módulo Python
│
├── /logs                 # Carpeta para guardar logs o errores
├── requirements.txt      # Archivo con dependencias
└── README.md             # Este archivo explicando el proyecto
Configuración del Chromedriver
Descarga la versión adecuada de Chromedriver desde aquí y colócala en la raíz de tu proyecto o ajusta la ruta en navigation.py:

service = Service('./chromedriver.exe')
Asegúrate de que tu navegador Chrome esté actualizado y que chromedriver sea compatible con la versión de Chrome que tienes instalada.

Cómo ejecutar el bot
Clona este repositorio en tu máquina local.

git clone https://github.com/tuusuario/bot_citas_automated.git
Instala las dependencias:

pip install -r requirements.txt
Ejecuta el bot de la siguiente manera:


python scripts/navigation.py
Descripción de los scripts
import_requests.py: (Comentado actualmente) Prepara las solicitudes usando proxies, pero puede expandirse si necesitas manejo adicional de solicitudes HTTP.
navigation.py: Controla la navegación del bot a través del sitio de citas, seleccionando provincia, oficina y solicitando la cita. También maneja la selección de documentos, la entrada de datos del usuario y la gestión de errores.
proxy_manager.py: Selecciona un proxy aleatorio de una lista definida y configura Selenium para usar ese proxy.
Información adicional
Si necesitas configurar más proxies, puedes agregar más IPs en el archivo proxy_manager.py. Asegúrate de que cada proxy esté activo y funcione correctamente antes de usarlo.

Manejo de errores
El bot está configurado para capturar capturas de pantalla en caso de que ocurran errores durante el proceso de navegación. Las capturas de pantalla se almacenarán en la carpeta /logs/.

