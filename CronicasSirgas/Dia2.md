# Cronica del Simposio SIRGAS 2023: Dia 2

> Las presentaciones para todos los días del simposio están disponibles
> [En este link](https://sirgas.ipgh.org/eventos-sirgas/simposios/symp_2022/)

El segundo día del simposio comenzó como era previsible: ajustando los últimos
detalles para mi exposición. Me hice un apunte de cada diapositiva y qué decir
en cada momento.

No soy muy amigo de las diapositivas --[Por ejemplo, recomiendo siempre este "ensayo"](https://www.inf.ed.ac.uk/teaching/courses/pi/2016_2017/phil/tufte-powerpoint.pdf) [y este video](https://www.youtube.com/watch?v=Iwpi1Lm6dFo), aunque asumo que la verdad debe estar [En algún lugar intermedio](https://kristw.medium.com/edward-tufte-hates-powerpoint-should-i-b6dba13178ee)-- , y no termino de aprender a adaptarme a la
modalidad. El resultado: me quedó un esquema de charla demasiado largo para el
tiempo disponible, espero que la organización me haya perdonado.

Salí del hotel con tiempo esta vez y, sin equivocarme en la combinación del metro,
 llegué antes de que comenzara el encuentro.

La mañana comenzó con dos exposiciones de
[Laura Sanchez](https://www.dgfi.tum.de/en/staff/sanchez-laura/), de DGFI-TUM.
La primera exposición sobre el trabajo que realiza DGFI como parte del procesamiento
rutinario de SIRGAS.

Luego de explicar el esquema general de procesamiento y combinación de
observaciones en SIRGAS, planteó las dificultades que se generan para la
[realización operacional de SIRGAS (procesamiento semanal de coordenadas)](https://sirgas.ipgh.org/red-gnss/coordenadas/coordenadas-semanales/).
El planteo es que, siendo SIRGAS un Marco de Referencia sólo GNSS, existe una
dependencia de un modelo de movimiento "secular" de las estaciones en la
realización del marco. Esto puede producir variaciones en la realización, que
se expresan como transformaciones de similaridad que afectan a toda la red.
Este es un problema sobre el que ya escribí [en la cronica del Día 1](Dia1).  Para
ilustrar estas variaciones, Laura nos mostró las soluciones de una traslación
entre soluciones semanales SIRGAS e IGS. Pudo verse ahí cómo las sucesivas
realizaciones de IGS fueron reduciendo las diferencias -- como consecuencia de
aplicar más modelos para efectos específicos --, mostrando que el modelo secular
de movimiento se beneficia del modelado independiente de los efectos no lineales.

La propuesta de Sanchez para mejorar los resultados es cambiar a una
realización por época del marco de referencia regional a partir de la inclusión
de datos globales --GNSS y también de otras técnicas que permitan determinar el
centro de masas-- junto con los datos regionales, en lugar de realizar una
alineación en el modelo secular sino sólo en la orientación de la red global
GNSS época a época. Estos conceptos están relacionados con
[Este paper publicado por el equipo del DGFI](https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2021JB023880)
, donde se desarrollan estas ideas más en profundidad.

Con está charla quedó abierta el juego a plantear cuál es la estrategia más
conveniente para SIRGAS. Por ejemplo, al final de la segunda charla de Laura se
planteó -- en la ronda de preguntas -- el contraste entre [usar modelos de carga
no-mareal](https://earth-planets-space.springeropen.com/articles/10.1186/s40623-022-01634-1)
o incluir componentes periódicas al modelo secular de movimiento.
Claramente la realización por-epóca con datos globales incluidos en el
procesamiento se presta al modelado de estas variaciones como efectos de carga.

En la segunda charla, Laura nos comentó sobre el trabajo de reprocesamiento de
los datos SIRGAS que realizó el DGFI, para generar un conjunto coherente de
soluciones SIRGAS en [el marco de referencia IGb14](https://lists.igs.org/pipermail/igsmail/2020/007917.html)
mantenido por [IGS](https://igs.org/wg/reference-frame/).
En este procesamiento se incluyeron datos de estaciones distribuidas
globalmente, lo que mitiga los problemas de alineación que Demián Gómez nos
comentaba el día anterior -- y podría anularlos completamente con una
distribución de estaciones ideal --.  El resultado de este procesamiento está
disponible públicamente y mejora en mucho la solución operacional, no sólo por
el uso de IGb14 sino por la inclusión de nuevos datos históricos de estaciones
SIRGAS que contaban con datos históricos anteriores a su incorporación a la
red.

Siguió a continuación la presentación de Sebastián Kollner, de la empresa
chilena Kollner-Labraña, presentándonos el funcionamiento de la red de
receptores instalada por la empresa para prestar servicios RTK y NTRIP. Esta
charla fue la primera en la que se planteó el problema, en Chile, de la
necesidad de actualizar las posiciones de los receptores en caso de
deformación, a partir de uso de un marco de referencia dinámico. La solución
planteada en este caso es pedir la certificación del IGM de Chile para la
posición de cada estación cada vez que el [IGM publica una realización de su
marco de referencia nacional actualizado](https://www.sirgaschile.cl/Referencia_Oficial_RGN_SIRGAS.php).
Se hizo mucho énfasis --acertadamente-- en educar a los usuarios para que
entiendan estos conceptos y puedan hacer un uso coherente de los servicios.

Luego fue el turno de mi charla. Ya les dejé un resumen en
[mi Github](https://github.com/jjclavijo/3ideas2022sirgas#readme), asi que no me
voy a extender en ese punto.

Durante la charla me fui dando cuenta de que el tiempo no me alcanzaba para todo
lo que quería decir, que había ido creciendo porque cada charla que pasaba yo
la veía conectada con la mía. Pasados los 10 minutos (en mi cronómetro) empecé
a apurar el paso, y para los 15 todavía me falta una última idea. Pedí permiso
a la moderadora para redondear y terminé como pude.

Por la expresión de los asistentes pareció que algo se llegó a entender de la
charla, o que mi desesperación por llegar a tiempo era un espectáculo interesante.
El tiempo dirá cual de las dos versiones es verdadera.

Siguió la presentación de los posters, que pueden verse junto con las presentaciones
en la web de SIRGAS. Destaco la idea de la universidad de Bogotá, que presentó
algunas medidas que tomaron para ampliar la participación de la geodesia en
la universidad. Espero que estas actitudes se contagien a todas las universidades
de la región.

Después de un muy breve café retomamos las sesiones para escuchar ahora las
presentaciones sobre el modelado del campo de gravedad terrestre y sistemas de altura.

Comenzó la sesión con una exposición de
[Mike Bevis](https://earthsciences.osu.edu/people/bevis.6), de OSU, que habló
sobre la red de mediciones gravimétricas de Bolivia. Más especificamente habló
sobre la importancia de la redundancia en las mediciones gravimétricas,
ejemplificando cómo la medición ida-vuelta con más de un gravímetro permitió
una redundancia de mediciones que posibilitó estimar mejor las precisiones
alcanzadas. Luego, realizó una validación del modelo EGM08 con los resultados
hallados, y mostró cómo el error del modelo supera la incertidumbre espacial
del mismo, es decir que en Bolivia EGM08 es una descripción pobre del campo
gravitatorio terrestre.

Siguió la charla de
[Gabriela Cordero](http://www.etcg.una.ac.cr/index.php/contacto/personal-academico/4-gabriela-cordero-gamboa)
, de la UNA de Costa Rica.

Gabriela habló sobre cómo se realizó (y se sigue realizando) un trabajo de
actualización de los datos de puntos fijos de nivel de Costa Rica. Este trabajo
consistió en inspecciónes al terreno, revisión de documentación, elaboración
de nuevas monografías, mantenimiento de los puntos, etc.

Me sorprendió el empuje de los impulsores del proyecto, que son sólo dos
personas, y que lograron entusiasmar a muchos alumnos de la universidad para
que colaboren en esta tarea que es tanto o más fundamental que el aspecto
científico de la medición y compensación de una red de nivelación cuando se
trata de poner un sistema de alturas a disposición del usuario final.
La capacidad de coordinar y emprender este tipo de proyectos es fundamental
para mantener a los alumnos de nuestras carreras motivados y comprometidos
con la profesión, ¡Bravo!.

Siguió la charla de
[Dennys Enríquez Hidalgo](https://www.researchgate.net/profile/Dennys-Enriquez-Hidalgo),
del IGM de Ecuador, que hizo una evaluación del error producido al utilizar un
modelo de ondulación geoidal para hacer mediciones de desnivel utilizando GPS.
La propuesta de Dennys es que pueden clasificarse las regiones geográficas en
zonas de mayor o menor gradiente de ondulación geoidal en base a un modelo
global, y con este estimador se podría construir otro del error esperado. Si
bien el trabajo no llega a construir un estimador, sí muestra en forma gráfica
una posible correlación entre los dos estimadores propuestos. La charla cerró
con un comentario sobre el uso de redes sociales que me resultó bastante
acertado, notando la poca presencia de canales sobre geodesia o cartografía en
youtube y tiktok, puede ser importante generarlos, de forma que se difundan
estas ciencias que son muy importantes para la comunidad.

De las tres charlas que siguieron dos fueron sobre la red de nivelación y
gravedad Colombiana.  La primera trató sobre el ajuste en términos de números
geopotenciales, mientras que la segunda trató sobre el establecimiento de la
red de gravedad absoluta.  Ambas presentaciones trataron más que nada sobre
aspectos de logística o rutinas de cómputo, pero no deja de ser importante que
se difundan los trabajos hechos por cada instituto y conocer las diferentes
formas en las que se organizan, financian y gestionan los trabajos. Creo que,
desde mi punto de vista de docente e investigador, le doy demasiada poca
importancia al aspecto de organización y gestión que hace posible que este tipo
de trabajos se lleven a cabo con éxito.

La otra charla, de
[Tiaho Rodrigues](https://www.researchgate.net/profile/Tiago-Lima-Rodrigues),
se basó principalmente en [este paper](https://www.scielo.br/j/bcg/a/Xmq8mCrKhjRvJwTBMQnzZkH/),
donde los autores proponen un método para vincular mediciones de altura elipsoidal
al sistema de alturas oficial de Brasil. La metodolgía propuesta es sumamente interesante
y completa, incluyendo un modelo de gravedad global refinado con datos topográficos
y un modelo paramétrico para incorporar las mediciones comunes de ambos
sistemas de altura a la conversión.

El planteo de Tiago es además de una utilidad práctica importante: hasta que
se implemente el IHRF en todo Brasil y se conviertan todos los datos disponibles
a alturas basadas en números geopotenciales, tener una conversión bien construida
 entre los sistemas de altura a los que el usuario puede acceder es de vital
importancia para gran cantidad de trabajos de campo.

Las Tres charlas que siguieron fueron relativas a modelado de geoide
(o cuasi-geoide), e hicieron mención al experimento del colorado.

No es mi tema, pero me resulta muy interesante el modelado del campo de gravedad
terrestre. No tenía conocimiento del experimento de colorado, pero me resulto
muy interesante y útil para la comunidad en general.

Para los que no conocen el experimento, se trató de una comparación entre métodos
de modelado basada en [un dataset publicado por la NOAA, de Estados Unidos](https://geodesy.noaa.gov/GEOID/research/co-cm-experiment/)
. Los datos fueron analizados por distintos grupos de trabajo, para realizar
[una comparación de metodologías](https://link.springer.com/article/10.1007/s00190-021-01567-9).

La consecuencia de este experimento es sumamente interesante porque se cuenta
al mismo tiempo con un análisis detallado de metodologías, que pueden ser aplicadas
a nuevos datos, y un dataset sobre el que se pueden evaluar metodologías comparando
los resultados con los publicados por otros grupos.

En esta línea, el trabajo de Thiago padilla y Tiago Rodrigues se enfocó en
analizar parte de las metodologías aplicadas al modelado en Brasil.
Lamentablemente no pude captar demasiado los conceptos de este trabajo, mas
allá del uso de un modelo de inhomogeneidades laterales de densidad de las
masas topográficas. Esto quiere decir que se aplicó un modelo de los cambios en
la densidad del terreno al aplicar la corrección topográfica al modelado con la
técnica de Remove-Restore.

Las presentaciones Agustín Gómez y Ana Cristina Oliveira trataron directamente
sobre desarrollos metodológicos aplicados a los datos de colorado con vistas a
poder trasladar los desarrollos a datos regionales. La explicación metodológica
fue muy prolija y detallada, lo cual lo hizo muy interesante. De todos modos,
al no ser tema de mi experiencia no tengo mucho mas para decir que que
recomiendo que se pongan al tanto de este experimento de colorado --
oficialmente "Colorado 1cm Geoid Experiment", de sus resultados y de como una
iniciativa de este tipo beneficia enormemente a toda la comunidad, no sólo
científica sino también de la educación.

Siguió otra presentación de la gente de la Universidad Politécnica de Sao
Paulo, En ella se habló del cálculo del potencial gravitatorio sobre las
estaciones propuestas para incorporar al IHRF. Se compararon distintas
metodologías, nuevamente se me escapan los detalles importantes, aunque cada
charla que pasa me crecen las ganas de agarrar ["Physical Geodesy" de
Hoffman-Wellenhof y Moritz](https://es.scribd.com/document/513340881/Hofmann-Wellenhof-B-Moritz-H-Physical-Geodesy-2005) y leerlo de punta a punta, por suerte no lo tenía a
mano y pude seguir atendiendo al resto del simposio.

Luego, llegó el turno de Juan Carlos Vidal Cejas, del IGM de Bolivia, que expuso
sobre una validación del modelo de Ondulación Geoidal de Bolivia con respecto
a puntos de la red nacional de nivelación. El modelo, de un minuto por un minuto,
fue interpolado para poder hacer las comparaciones en los puntos de validación.
Hubo en la presentación un pequeño desarrollo sobre los posibles métodos de
interpolación, y me siento tentado a extenderme, porque es otro de mis temas
favoritos, pero lo voy a dejar pasar para no aburrir.

Cerró la sesión con dos charlas de
[Walter Subiza](https://www.linkedin.com/in/walter-humberto-subiza-pina/),
del IGM de Uruguay.
Ambas charlas trataron sobre la actualización del sistema vertical de Uruguay,
la primera desde el punto de vista de modelado del geoide -- con muchas nuevas
referencias al experimento de colorado --, y la segunda desde el punto de vista
de la actualización de las mediciones y los acuerdos para compartir datos con
paises vecinos. Ambas charlas fueron muy interesantes y amenas, y me animo a
decir que Walter fue el orador con mejor manejo del auditorio en el día, sin
ofender al resto de los expositores o a mi mismo, que también formo parte de el
grupo de los no-mejores oradores del día.

No participé en las reuniones de los grupos de trabajo II y III, porque el
horario ya estaba suficientemente demorado. En lugar de eso salí a correr 8 km
por la costanera del río Mapocho, una decisión absolutamente recomendable.

Terminé el día suficientemente cansado como para no acordarme como terminó, y
dejamos acá el resumen.
