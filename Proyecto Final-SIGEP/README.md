# Análisis del capital humano de los municipios de la Sabana, Cundinamarca desde SIGEP: Sistema de Información y Gestión del Empleo Público
[Sebastián Valbuena]
15 - 05 - 2019

---

## Descripción y motivación

Es obligación de las entidades públicas subir a la página del Sistema de Información y Gestión del Empleo Público los perfiles de los funcionarios y servidores públicos. Para este proyecto utilicé los registros que las alcaldías municipales suben de sus funcionarios y contratistas con corte a 15 de mayo de 2019. Se utilizaron exclusivamente la formación educativa, el tipo de contrato o funcionario y el lugar de procedensia, utilizando herramientas de análisis en Python.

Algunas preguntas que motivaron el proyecto son:

- La profesionalización de las actividades públicas son fundamentales para el desarrollo de los servicios que debe brindar el Estado. Entender que las alcaldías municipales requieren de profesionales capacitados e idóneos parte de conocer qué tipo de profesionales deben tener. Por ello, conocer el nivel de formación de los funcionarios de las alcaldías de Cundinamarca es fundamental para tal final.
- Los reportes en el SIGEP no tienen la mejor calidad de parte de las entidades, los datos no reportados también siguen siendo un dato. Saber cuál entidad es la que cuenta con los mejores reportes al Sistema es clave para garantizar rankings de transparencia y de esa manera estimular la buena disposición de los datos ante Función Pública.

## Métodos usados

1. Scraping
    - A partir de la página http://www.sigep.gov.co/ - Directorio de hojas de vida, se puede realizar la búsqueda de las hojas de vida de los funcionarios, permitiendo a su vez filtrar la información por departamento, entidad, municipio o tipo de contrato.
    - La página web del SIGEP realiza consultas a https://www.funcionpublica.gov.co/dafpIndexerBHV, razón por la cual las peticiones se realizan a este dominio, utilizando filtros de búsqueda por entidades (códigos de alcaldías).
    - Se realiza el scraping con ayuda de Scrapy, framework de web scraping, creando un Spider para la página web en cuestión.
    - Se obtienen los elementos de las páginas HTML resultantes de las búsquedas, haciendo uso de búsquedas por CSS y por XPATH dentro del spider.
2. Limpieza de información
    - El texto resultante de las búsquedas no está estandarizado, razón por la cual se decide limpiar la información con respecto a:
        * Espacios
        * Uso de mayúsculas y minúsculas
        * Acentos
        * Dígitos
        * Información adicional
        * Información repetida
3. Uso de la información
    - Los datos son almacenados dentro de una matriz, donde por cada alcaldía se cuenta con un arreglo de tipo de contratos, uno de nivel de estudios y uno de lugar de nacimiento.
    - Se muestra la información en gráficas realizadas con la librería Pandas.

## Hallazgos

Un ejemplo de los resultados obtenidos se muestra a continuación, describiendo para la distribución de funcionarios de la alcaldía de Cajicá, el lugar de nacimiento, el nivel de estudios y el tipo de contrato:

<img src="resources/plots/Alcaldía de Cajicá - Lugar de nacimiento.png">

<img src="resources/plots/Alcaldía de Cajicá - Nivel de estudios.png">

<img src="resources/plots/Alcaldía de Cajicá - Tipo de contrato.png">

La misma información se encuentra en el directorio resources/plots para las alcaldías de Cajicá, Chía, Cogua, Gachancipá, Nemocón, Tocancipá y Zipaquirá, definidos dentro del alcance.

---

## Instalación

Para poder ejecutar el archivo de entrada main.py, es necesario contar con el framework Scrapy instalado.
Esto se puede hacer primero,

1. Instalando BuildTool https://visualstudio.microsoft.com/es/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16#
   Asegurar de marcar la opción C++
2. Correr el comando pip install scrapy
    - En caso de no poder realizar la instalación por pip, se puede realizar utilizando Conda, corriendo el comando conda install -c conda-forge scrapy
3. Finalmente, si es requerido instalar la dependencia de unidecode haciendo uso del comando pip install unidecode

## Ejecución

El programa corre desde el archivo main.py. Las entidades (alcaldías) a filtrar pueden ser definidas con sus respectivos códigos, que se encuentran dentro de la página web de función pública, en el archivo bajo el directorio resources llamado codes.json.