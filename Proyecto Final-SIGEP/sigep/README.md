Analisis del capital humano de los municipios de la Sabana, Cundinamarca desde SIGEP: Sistema de Información y Gestión del Empleo Público
Sebastián Valbuena
23/05/2019

Descripción y motivación.

Es obligación de las entidades públicas subir a la página del Sistema de Información y Gestión del Empleo Público los perfiles de los funcionarios y servidores públicos. Para este proyecto utilicé los registros que las alcaldías municipales suben de sus funcionarios y contratistas con corte a 15 de mayo de 2019. Se utilizaron exclusivamente la formación educativa, el tipo de contrato o funcionario y el lugar de procedensia utilizando herramientas de análisis en Python.

Algunas preguntas que motivaron el proyecto son:

La profesionalización de las actividades públicas son fundamentales para el desarrollo de los servicios que debe brindar el Estado. Entender que las alcaldías municipales requieren de profesionales capacitados e idóneos parte de conocer qué tipo de profesionales deben tener. Por ello, conocer el nivel de formación de los funcionarios de las alcaldías de Cundinamarca es fundamental para tal final.

Los reportes en el SIGEP no tienen la mejor calidad de parte de las entidades, los datos no reportados también siguen siendo un dato. Saber cuál entidad es la que cuenta con los mejores reportes al Sistema es clave para garantizar rankings de transparencia y de esa manera estimular la buena disposición de los datos ante Función Pública. # Métodos usados

Scraping

Los registros de los funcionarios de las alcaldías estaban únicamente en un sitio web de la función pública:

Ejemplo
Batch 1: from 08/07/2010 to 08/06/2014 (1,873 speeches): http://wsp.presidencia.gov.co/Discursos Batch 2: from 08/07/2014 to 12/12/2015 (678 speeches): http://wp.presidencia.gov.co/Discursos Batch 3: Most recent ones –last date of scraping: 03/13/2016– (118 speeches): http://es.presidencia.gov.co/discursos

To scrape the two batches of older speeches I used the 'requests' and 'BeautifulSoup' libraries. The recent batch is available in a JavaScript rendered site. I extracted all the available speeches using 'selenium' library and 'webdriver' with Chrome. The Python code is available here for batches 1 and 2 and here for batch 3.

Extracting the data from 'BeatifulSoup' objects: Both to scrape the raw text and to extract the data from it, I wrote helper functions to: get htmls; get urls to speeches; get year, month, and day information from the text; get the title of the speech; remove html tags; get the location of the speech; and get all the elements of a speech in a structured object. Helper functions are available here.

Managing, storing, and further cleaning the data: I used 'Pandas' to create a data frame for each batch of speeches, and exported each to a 'pickle' file for storage. I consolidated the three data frames into one and furthered cleaned the data using 'Pandas' methods, 'string' methods, regular expressions, etc. Using 'string' and 'nltk' libraries I stripped speeches from punctuation, converted to lowercase, tokenized text, dropped stopwords (in Spanish), etc. Code is available in here.

Resultados
