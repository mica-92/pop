 

> notas mica hoy por la mañana: cambiar líderes a coordinadores, quiero sacar fechas y dejar solo meses de implementación. cambiar establecimiento a locales comerciales. unificar peta pedidosya. cambiar básica y pro a basic y extended

## 1. Resumen Ejecutivo

**POP (Plataforma Operativa de PLVs)** es una plataforma web diseñada a medida para Picnic con el objetivo de **modernizar y automatizar el control y seguimiento de la colocación de PLVs (Publicidad en Lugares de Venta)**. Actualmente, este proceso se realiza sobre la aplicación PeYa Trade (PYT), una herramienta que presenta limitaciones operativas significativas, dificultando la obtención y entrega de resultados precisos a PedidosYa.

**POP** responde a dos significados que confluyen en un mismo objetivo. Por un lado, *Plataforma Operativa de PLVs*, el sistema que organiza y da seguimiento a cada material publicitario en terreno. Por el otro, *Point of Purchase* en referencia al punto de venta (PDV), el lugar físico donde la marca y el consumidor se encuentran. **POP es la herramienta que hace que ese encuentro sea posible, medible y escalable.**

### Diagnóstico Operativo Actual

Las limitaciones de PYT se evidencian en el uso cotidiano de la aplicación. Estas radican principalmente en un deficiente manejo de la información, y pueden resumirse en 4 puntos centrales:

- **Usabilidad y análisis limitado:** Interfaz rígida que no permite filtrar ni segmentar datos dinámicamente; obliga a exportar la información y la producción manual de cada reporte, generando demoras y restando confiabilidad a la toma de decisiones. Además, está construido sobre bibliotecas programáticas antiguas, lo que vuelve el programa lento e inestable en el uso diario;

- **Falta de trazabilidad temporal y geográfica:** Sin historial ni métricas evolutivas; imposibilita comparar la evolución de los PDVs entre períodos, ni segmentar por localidad o rango de tiempo para planificar prioridades;

- **Fragmentación de la información:** La información se encuentra aislada por período, producto y tipo de material, sin una vista consolidada por PDV; obliga a cruces manuales entre diferentes hojas y archivos, incrementando errores y esfuerzo operativo en auditorías integrales;

- **Debilidades en el control operativo:** Carece de trazabilidad de visitas, integración de coordinadores regionales en el flujo de trabajo, y controles de acceso sólidos; comprometiendo la seguridad, integridad y auditabilidad del proceso, y limitando la capacidad de supervisión efectiva del equipo en campo.

Generando en consecuencia:

- **Inconvenientes en la detección de cuellos de botella operativos**, como zonas o productos con bajo desempeño, que no pueden identificarse a tiempo;
- **Inhabilitando un seguimiento eficiente de la campaña**, al no contar con información confiable ni actualizada para la toma de decisiones;
- **Limitaciones en la capacidad de Picnic para anticiparse a las necesidades de su cliente**, ofreciendo soluciones proactivas basadas en datos en lugar de reaccionar ante consultas o problemas sobre la marcha.

### Propuesta Operativa POP

Con el objetivo de resolver los inconvenientes identificados, **POP centraliza la operación con una interfaz rápida y moderna**, construida sobre una nueva arquitectura de base de datos que integra de forma eficiente todas las diferentes dimensiones del proyecto — PDVs, PLVs, períodos, coordinadores y cliente — dentro de un ecosistema unificado, y ofrece:

- **La agilización y automatización de las tareas repetitivas y cotidianas**, muchas de las cuales se realizan de forma manual actualmente, como la carga de los PDVs y la distribución de los mismos a los coordinadores;

- **Facilita la visualización del estado actual de cada campaña**, con KPIs (*Key Performance Indicators*) en tiempo real desde el dashboard, integrando el análisis de datos en el flujo operativo diario para revisar, evaluar y ajustar estrategias con información actualizada;

- **Permite el análisis histórico y comparativo entre períodos**, con dashboards personalizados para la consulta de períodos pasados y una correcta evaluación de la evolución temporal de los indicadores clave;

- **Promueve un entrecruzamiento natural de la información** desde distintos ángulos (PDVs, productos, zonas geográficas y períodos), brindando una comprensión holística de la logística de la campaña que hoy requiere consultar múltiples archivos y hacer cruces manuales;

- **Garantiza trazabilidad operativa en dos niveles de control**: a nivel de coordinadores regionales (asignación de zonas, distribución de tareas y monitoreo de desempeño por coordinador) y a nivel de visita (quién, cuándo, dónde, con registro fotográfico y log de auditoría), permitiendo a Picnic identificar problemas logísticos y medir la eficiencia de su operación en tiempo real;

- **Ofrece dashboards diferenciados por perfil de usuario** — gestión para Picnic, operativo para coordinadores regionales y transparencia para PeYa — con un panel de cliente que brinda acceso autónomo a KPIs, fotos y reportes, reduciendo pedidos de información ad-hoc y fortaleciendo la relación comercial;

- **Su arquitectura modular y su nueva estructura de datos** permiten que el software crezca junto con las necesidades de Picnic, incorporando nuevas funcionalidades sin replantear el sistema completo, protegiendo la inversión a largo plazo.

POP organiza el ciclo de vida de una campaña de PLVs en torno a cuatro dimensiones operativas interconectadas, articuladas sobre un único modelo de datos compartido:

- **Gestión central (Picnic):** administración de campañas, carga y configuración de PDVs, definición de productos y períodos, y supervisión general del avance desde un dashboard con KPIs en tiempo real. Es el núcleo desde el cual se estructura y controla toda la actividad de la plataforma.

- **Coordinación territorial (coordinadores regionales):** acceso a zona asignada, visualización de listados operativos, distribución de tareas y monitoreo de desempeño en campo. Introduce una capa de supervisión intermedia que hoy no existe, permitiendo detectar desvíos y actuar sin escalar cada consulta al equipo central.

- **Ejecución en punto de venta (colocadores):** registro de visitas desde app móvil optimizada para campo, con documentación fotográfica, registro de incidencias y confirmación de colocación en tiempo real, eliminando la demora entre la visita y la actualización de la base de datos.

- **Rendición de cuentas al cliente (PeYa):** panel autónomo para consultar estado de campañas, KPIs, registros fotográficos y descarga de reportes, reduciendo la carga operativa del equipo de Picnic y fortaleciendo la transparencia en la relación comercial.

Las cuatro dimensiones comparten un único modelo de datos, eliminando la fragmentación actual y garantizando que la información fluya sin fricciones desde el PDV hasta el reporte final, sin cruces manuales ni archivos intermedios.

### Valor Agregado

Más allá de resolver las limitaciones operativas actuales, POP construye activos estratégicos para Picnic.

El primero es una **base de datos de PDVs operativa y verificada en campo**. El sistema consolida y mantiene actualizada la información de cada punto de venta — dirección, contacto, estado del PLV e historial de visitas —, construyendo un activo de información que no solo potencia la operación actual, sino que representa un recurso valioso para futuras campañas y análisis.

El segundo es una **plataforma replicable para otros clientes**. La arquitectura modular de POP permite adaptar la solución a las necesidades de otros clientes de Picnic con modificaciones menores. La inversión en desarrollo no queda atada a un único cliente: el sistema puede extenderse y reutilizarse, multiplicando el retorno sobre la inversión inicial y posicionando a Picnic con una capacidad diferencial en su mercado.

### Versiones de Implementación

POP se presenta en dos versiones que comparten la misma arquitectura técnica y entregan valor operativo desde el primer mes de uso. La elección entre ambas no implica un cambio de plataforma sino de alcance: la Versión Extended es una expansión natural de la Básica, y cualquier funcionalidad desarrollada en la primera etapa es parte integral de la segunda.

La **Versión Basic** cubre el flujo central de la operación. Incluye la carga y gestión de PDVs y productos, el registro de visitas con evidencia fotográfica, el dashboard de seguimiento con KPIs por período, producto y zona geográfica, y el sistema de reportes exportables. Está orientada a reemplazar el flujo manual de archivos Excel con una herramienta moderna, centralizada y confiable, y que buscan resultados operativos concretos desde el primer período de uso.

La **Versión Extended** incorpora las capas de control operativo avanzado que habilitan una gestión más sofisticada de la campaña. Sobre la base funcional de la Versión Básica, agrega la gestión de coordinadores regionales con asignación de zonas y monitoreo de desempeño por coordinador, la trazabilidad nominal de visitas — registro de quién realizó cada acción y cuándo —, dashboards diferenciados por perfil de usuario con accesos segmentados para Picnic, coordinadores y PeYa, y herramientas de análisis histórico y comparativo entre períodos. Está diseñada para equipos que buscan no solo modernizar la operación, sino optimizar toda la cadena de gestión y construir inteligencia operativa acumulada sobre sus campañas.

### Fases de Implementación

El desarrollo de POP se estructura en fases secuenciales, cada una con entregables concretos y una instancia de validación con el equipo de Picnic. Este esquema permite incorporar aprendizajes del uso real en etapas tempranas y ajustar prioridades sin comprometer la coherencia del sistema.

**Fase 1 — Arquitectura y base de datos**
Se define y construye el modelo de datos central: PDVs, productos, períodos y estructura de visitas. Se configura el entorno de desarrollo y se establece el pipeline de importación de datos desde los archivos actuales. Esta fase sienta las bases técnicas sobre las que opera todo el sistema y no produce interfaz visible, pero es el cimiento que garantiza la integridad y escalabilidad de la plataforma.

**Fase 2 — Dashboard de gestión y reportes**
Se desarrolla el dashboard principal para el equipo de Picnic, con visualización de KPIs por período, producto, zona geográfica y PDV. Se incorpora el sistema de filtros dinámicos, la vista de detalle por PDV con historial fotográfico, y el módulo de reportes exportables. Al cierre de esta fase, el equipo de Picnic cuenta con una herramienta funcional para el seguimiento y análisis de campañas en curso.

**Fase 3 — Aplicación móvil para colocadores**
Se desarrolla la aplicación de campo optimizada para dispositivos móviles, que permite a los colocadores registrar visitas, cargar fotografías y reportar incidencias directamente desde el PDV. La información ingresada se refleja en tiempo real en el dashboard de gestión, cerrando el ciclo entre la ejecución en terreno y la supervisión central.

**Fase 4 — Coordinadores y panel de cliente**
En la Versión Básica, esta fase consolida el sistema con ajustes de usabilidad, pruebas de carga y documentación operativa. En la Versión Extended, se desarrollan adicionalmente el módulo de coordinadores regionales — con gestión de zonas, distribución de tareas y monitoreo de desempeño por coordinador —, el panel autónomo para PeYa con dashboards diferenciados y acceso segmentado, y las herramientas de análisis histórico y comparativo entre períodos.

### En Síntesis

POP se diseña en coordinación constante con Picnic, incorporando directamente el aprendizaje acumulado sobre las dificultades y obstáculos que el equipo enfrenta hoy. Cada decisión técnica responde a un problema operativo real, y la plataforma se construye para habilitar una visualización holística de cada campaña, el desarrollo de estrategias fundamentadas en información concreta, y la capacidad de crecer sin replantear el sistema completo.

POP no es solo un reemplazo: es la oportunidad de transformar la gestión de PLVs en una ventaja competitiva, devolviéndole a Picnic el control, la velocidad y la inteligencia operativa que necesita para responder a su cliente, diversificar su oferta y proyectarse a futuro.

## 2. Alcance del Proyecto

POP se estructura en torno a **cuatro experiencias diferenciadas**, una por cada actor del proceso de colocación de PLVs. Cada experiencia está diseñada para que la persona responsable acceda exclusivamente a la información que necesita para su gestión, con Picnic como coordinador central y veedor de toda la cadena. Sobre estas cuatro experiencias operan un conjunto de **módulos transversales** —carga de datos, configuración, reportería y auditoría— que dan soporte al funcionamiento integral de la plataforma.

Todas las experiencias y módulos comparten un **único modelo de datos**, lo que elimina la fragmentación actual y garantiza que la información fluya sin fricciones desde el punto de venta hasta el reporte final. La diferencia entre las versiones **Basic** y **Extended** no implica un cambio de plataforma sino de alcance: Extended es una expansión natural de Basic, y toda funcionalidad desarrollada en la primera es parte integral de la segunda.

A lo largo de esta sección se utiliza el término **PDV** (Punto de Venta) para referirse a cada establecimiento físico donde se coloca material publicitario, y **coordinador regional** para el responsable de gestionar una zona operativa y su equipo de colocadores en campo.

---

## 3. Las Cuatro Experiencias

### 3.1 Panel de Gestión Central (Picnic)

El Panel de Gestión Central es el centro de control del equipo de Picnic sobre la operación completa. Desde una única interfaz, el admin monitorea el estado de cada campaña, accede al detalle de cualquier PDV, supervisa el trabajo del equipo de campo y exporta la información que necesita para responder a PeYa en cualquier momento.

Al ingresar, el admin visualiza el panel del período actual con los **KPIs core** en la parte superior —total de PDVs, visitados, efectivos, pendientes, abiertos y cerrados, con desglose de motivos de no efectividad—, dos visualizaciones de breakdown que muestran el avance por PLV y la cobertura por geografía, y la tabla completa de PDVs del período con todas sus columnas de información: identificador, nombre, tipo, contacto, ubicación, producto, estado y fecha de visita. El admin puede ordenar por cualquier columna, buscar por Grid o nombre, filtrar según las dimensiones disponibles en su versión, y exportar a Excel la vista actual conservando todos los filtros aplicados.

Los **KPIs se recalculan dinámicamente** según los filtros: al acotar por una provincia o producto específico, los números superiores se actualizan al instante, integrando el análisis de datos en el flujo operativo diario. El selector de período permite navegar a cualquier mes histórico cargado en POP, mostrando una vista consistente de la operación pasada como snapshot al cierre.

**Basic vs Extended.** En ambas versiones el admin filtra por provincia y PLV combinándolos entre sí, lo cual resuelve la operatoria cotidiana. La versión **Extended** amplía radicalmente la capacidad analítica: incorpora filtros avanzados sobre todas las dimensiones disponibles (ciudad, barrio, zona, estado, motivo específico de no efectividad y cadena comercial), combinables libremente entre sí, y suma un selector de rango de fechas para análisis multi-período. Extended agrega además tres pestañas de análisis dedicado: una pestaña **Por PLV** que agrupa los PDVs por producto mostrando el desempeño independiente de cada uno; una pestaña **Por Geografía** con drill-down que permite navegar la jerarquía territorial (provincia → ciudad → barrio → zona) con KPIs agregados en cada nivel; y una pestaña de **Histórico de KPIs** que muestra los indicadores clave de cada período cerrado en una tabla comparativa mes a mes. Las columnas de zona, ciudad y barrio son visibles y ordenables en ambas versiones; la diferencia está en la capacidad de filtrar por esos niveles, no de verlos.

| Funcionalidad | Basic | Extended |
|---|:-:|:-:|
| Login con email y contraseña | ✅ | ✅ |
| Home con KPIs del período actual (total, visitados, efectivos, pendientes, abierto/cerrado, motivos) | ✅ | ✅ |
| Selector de período individual (cualquier mes histórico) | ✅ | ✅ |
| KPIs reactivos a los filtros aplicados | ✅ | ✅ |
| Breakdown por PLV y por geografía | ✅ | ✅ |
| Tabla de PDVs con todas las columnas + sort + búsqueda | ✅ | ✅ |
| Filtros simples: provincia + PLV (combinables) | ✅ | ✅ |
| Exportación a Excel con filtros aplicados | ✅ | ✅ |
| Vista de períodos pasados como snapshot al cierre | ✅ | ✅ |
| Selector de rango de fechas | ❌ | ✅ |
| Filtros avanzados combinables (ciudad, barrio, zona, estado, motivo, cadena) | ❌ | ✅ |
| Pestaña separada "Por PLV" | ❌ | ✅ |
| Pestaña separada "Por Geografía" con drill-down | ❌ | ✅ |
| Pestaña "Histórico de KPIs por mes" | ❌ | ✅ |

---

#### 3.1.1 Detalle de PDV

El detalle de PDV se abre desde cualquier vista del Panel de Gestión Central que liste puntos de venta, y permite al admin profundizar en un registro puntual sin perder el contexto del panel general. Responde a una necesidad operativa concreta: poder responderle a PeYa cuando pregunta por un PDV específico, auditar la actividad cuando algo no cuadra, y corregir información en el momento sin procesar datos por fuera del sistema.

Muestra la **información general** del PDV —Grid, nombre del partner, business name, teléfono, dirección completa, estado abierto/cerrado— y permite editar los campos habilitados directamente, con cada modificación quedando registrada en el log de cambios con fecha, hora y descripción. El admin puede además **cerrar o reabrir manualmente** el PDV: cerrarlo lo retira de las listas operativas y no aparecerá para visitas en ningún período hasta que se reabra. Incluye un **historial cronológico completo** de todas las visitas que el PDV recibió a lo largo del tiempo, en cualquier período cargado, con fecha, PLV asociado, estado y motivo cuando corresponde, lo que permite responder preguntas como "¿cuántas veces fue visitado este PDV?", "¿qué productos ya tuvo?" o "¿siempre hay problemas para colocar acá?".

**Basic vs Extended.** La versión **Extended** agrega el atributo **Cadena** como campo editable, lo que permite agrupar PDVs por marca comercial (Carrefour, McDonald's, Café Martínez, etc.) y filtrar o reportar sobre esa dimensión. La versión **Basic** no soporta el concepto de cadena: cada PDV es independiente. El resto del módulo es idéntico entre ambas versiones.

| Funcionalidad | Basic | Extended |
|---|:-:|:-:|
| Información general del PDV | ✅ | ✅ |
| Edición de campos (nombre, teléfono, dirección, abierto/cerrado, zona) | ✅ | ✅ |
| Historial completo de visitas en todos los períodos | ✅ | ✅ |
| Log de cambios del PDV | ✅ | ✅ |
| Acción: cerrar / reabrir manualmente | ✅ | ✅ |
| Edición del atributo Cadena | ❌ | ✅ |

---

#### 3.1.2 Detalle de Visita

El detalle de visita se abre desde el historial del PDV o desde cualquier tabla que liste visitas, y muestra el registro completo de una colocación puntual. Incluye el **estado** (efectiva o no efectiva), el motivo cuando aplica, los comentarios que dejó el colocador en campo, las **fotos del antes y del después** tomadas durante la visita, y la fecha y hora exacta en que se guardó. Las fotos se muestran como miniaturas inline dentro del modal, de tamaño suficiente para identificar el contenido sin necesidad de abrirlas a pantalla completa.

El admin puede **cerrar o reabrir manualmente** la visita: una visita cerrada deja de aparecer en las listas operativas del colocador, mientras que una reabierta vuelve a estar disponible para reintentar. Estas acciones quedan registradas en el log general de auditoría.

**Basic vs Extended.** La versión **Extended** agrega trazabilidad nominal completa sobre cada visita: registra el **ID del colocador** que la realizó y captura el **GPS del dispositivo** al momento de guardarla. Esto habilita auditoría individual ("¿quién hizo esta visita?") y verificación de presencia en el PDV, contrastando el GPS capturado con las coordenadas del establecimiento. La versión **Basic** no captura ID ni GPS desde la app de campo, por lo que las visitas quedan operativamente anónimas: sirven para registrar el estado de las campañas pero no para auditar el trabajo individual de los colocadores. El resto de la información de la visita es idéntica entre ambas versiones.

| Funcionalidad | Basic | Extended |
|---|:-:|:-:|
| Estado de la visita (efectiva / no efectiva) | ✅ | ✅ |
| Motivo de no efectividad | ✅ | ✅ |
| Fotos antes y después | ✅ | ✅ |
| Fecha y hora de la visita | ✅ | ✅ |
| Comentarios del colocador | ✅ | ✅ |
| Acción: cerrar / reabrir visita manualmente | ✅ | ✅ |
| ID del colocador | ❌ | ✅ |
| GPS del dispositivo al guardar la visita | ❌ | ✅ |

---

### 3.2 App de Campo (colocadores)

La App de Campo es la herramienta que usan los colocadores en terreno para cargar el resultado de cada visita en tiempo real. Es una aplicación web optimizada para celular (**PWA**), accesible desde cualquier dispositivo con navegador moderno y opcionalmente instalable en la home screen como una app nativa, abriéndose en pantalla completa. Reemplaza el flujo actual de cargar planillas, sacar fotos sueltas y consolidar todo después por otros canales.

Está pensada para una realidad operativa específica: el colocador trabaja en la calle, con un celular en la mano, posiblemente con mala conectividad. Cada interacción tiene que ser **rápida, robusta y a prueba de errores**. Después de ingresar, el colocador ve la lista de PDVs pendientes de su zona y producto, con búsqueda por nombre o Grid. Al tocar cualquier PDV, se abre el modal de visita con la información del establecimiento —nombre del partner, business name, teléfono con tap-to-call, dirección con tap-to-open en Google Maps—.

El registro de la visita consta de un **toggle Efectiva Sí/No**; si es efectiva, toggles de PLV con lógica especial para Kit Básico (sticker y saliente como toggles independientes para registrar qué pieza se colocó); si es no efectiva, un dropdown de motivo precargado desde Settings; comentarios opcionales; **foto antes obligatoria**; y **foto después obligatoria solo si la visita fue efectiva**. Las fotos se toman con la cámara nativa del dispositivo o se seleccionan desde la galería, a elección del colocador, y se **comprimen automáticamente en el dispositivo** antes de subir: cada foto pasa de aproximadamente 5MB a 250KB, lo que ahorra datos móviles del colocador, acelera la carga sobre conexiones lentas y reduce el costo de almacenamiento. Si la conexión falla al subir, la app retiene la foto y reintenta automáticamente. Al guardar, los datos quedan inmediatamente disponibles en el Panel de Gestión Central, el Portal de Coordinadores correspondiente y el Panel de Cliente de PeYa.

**Basic vs Extended.** La diferencia entre ambas versiones de la App de Campo es la más significativa del sistema porque define el modelo de control sobre el trabajo en terreno. En la versión **Basic** las visitas son operativamente anónimas: no hay autenticación (cualquiera con la URL accede ingresando solo zona y PLV), no se identifica al colocador, no se captura ubicación al guardar, y los datos del PDV son de solo lectura. POP Basic funciona perfectamente para registrar el estado de las campañas, pero no para auditar el trabajo individual ni verificar presencia en el PDV.

La versión **Extended** convierte la app en una herramienta completa de gestión de equipo de campo. El acceso queda protegido con **PIN de zona** (el colocador ingresa zona, PLV y PIN en un solo paso, y POP valida que el PIN corresponda a la zona seleccionada); cada visita queda asociada al colocador específico mediante **ID obligatorio** (validación de 7-8 dígitos, sin prellenado entre visitas para forzar la identificación consciente); se captura el **GPS del dispositivo** al guardar, con manejo defensivo si el permiso está denegado (la visita se guarda igual con flag "sin GPS"); el colocador puede **editar los datos del PDV** si encuentra discrepancias con la realidad, confirmando obligatoriamente antes de guardar; y si falla tres veces consecutivas el PIN, aparece un botón **"Avisar a mi coordinador"** que envía un email automático al coordinador regional con el ID del colocador y un mensaje opcional, resolviendo en el momento problemas de coordinación que hoy implican llamadas o esperas. La sincronización offline no está incluida en la v1 de ninguna de las dos versiones; está disponible como extensión futura cotizable aparte.

| Funcionalidad | Basic | Extended |
|---|:-:|:-:|
| URL pública accesible desde celular | ✅ | ✅ |
| PWA instalable en home screen | ✅ | ✅ |
| Lista de PDVs pendientes con búsqueda | ✅ | ✅ |
| Toggle Efectiva Sí/No | ✅ | ✅ |
| Lógica Kit Básico (toggles independientes sticker + saliente) | ✅ | ✅ |
| Foto antes obligatoria | ✅ | ✅ |
| Foto después obligatoria si efectiva | ✅ | ✅ |
| Compresión automática de fotos en el dispositivo | ✅ | ✅ |
| Cámara nativa + selección desde galería | ✅ | ✅ |
| Motivos precargados desde Settings | ✅ | ✅ |
| Comentarios opcionales | ✅ | ✅ |
| Datos del PDV en solo lectura | ✅ | ❌ |
| Datos del PDV editables | ❌ | ✅ |
| Acceso sin autenticación (zona + PLV únicamente) | ✅ | ❌ |
| Acceso protegido con PIN de zona | ❌ | ✅ |
| ID obligatorio del colocador en cada visita | ❌ | ✅ |
| Captura de GPS al guardar la visita | ❌ | ✅ |
| Botón "Avisar a mi coordinador" tras 3er error de PIN | ❌ | ✅ |
| Email automático al coordinador con ID + mensaje opcional | ❌ | ✅ |
| Edición de datos del PDV + confirmación obligatoria | ❌ | ✅ |

---

### 3.3 Portal de Coordinadores (Extended)

El Portal de Coordinadores es un acceso individual, exclusivo de la versión **Extended**, que permite a cada coordinador regional gestionar su territorio de forma autónoma sin depender del equipo central. Cada coordinador ingresa mediante un **link único y un PIN de 4 dígitos**, sin necesidad de usuario y contraseña, a un dashboard inmediato y simple diseñado para operar el período actual.

Al ingresar, el coordinador ve los **KPIs operativos de su zona** en el período actual —total de PDVs, visitados, pendientes, efectivos, distribución por PLV— junto con la tabla completa de PDVs asignados, con sort, búsqueda y filtros por PLV, estado y motivo. Puede **descargar el listado en Excel**, consolidado o multi-hoja por PLV, para distribuir a sus colocadores, y ve el **PIN de su zona** en un widget destacado para compartir con su equipo, quienes lo usan para acceder a la App de Campo.

El coordinador accede únicamente a lo que necesita para operar: no ve ID de colocadores, fotos de visitas, GPS, información de otras zonas ni períodos pasados. Esta acotación deliberada mantiene el foco operativo y protege la información sensible del resto de la operación.

**Basic vs Extended.** En la versión **Basic** este portal no existe. La coordinación se resuelve manteniendo el flujo que Picnic tiene hoy: el admin descarga desde el Panel de Gestión Central los Excels filtrados por provincia y los envía manualmente a sus coordinadores regionales. La versión **Extended** habilita el acceso autónomo de cada coordinador, eliminando ese paso manual y descentralizando la distribución de tareas sin perder el control central.

| Funcionalidad | Basic | Extended |
|---|:-:|:-:|
| Portal con link único + PIN | ❌ | ✅ |
| Vista de KPIs y tabla de la zona asignada | ❌ | ✅ |
| Filtros por PLV, estado y motivo | ❌ | ✅ |
| Descarga Excel consolidado o multi-hoja por PLV | ❌ | ✅ |
| Widget con el PIN de zona para compartir con colocadores | ❌ | ✅ |
| Distribución manual vía Excel filtrado por provincia | ✅ | — |

---

### 3.4 Panel de Cliente (PeYa)

El Panel de Cliente es la ventana de transparencia que Picnic le ofrece a PeYa sobre el avance de sus campañas. Es de **solo lectura**: el cliente ingresa con su login propio, gestionado desde Settings por el admin de Picnic, y accede a una vista similar a la del Panel de Gestión Central pero con los campos operativos internos restringidos.

PeYa visualiza los **KPIs del período actual** con desglose de motivos de no efectividad, los breakdowns por PLV y por geografía, y la tabla completa de PDVs con todas las columnas relevantes para su seguimiento: identificador, nombre, dirección, producto, estado, fecha de visita y motivo cuando corresponde. Puede ordenar por cualquier columna, buscar por Grid o nombre, filtrar por provincia y PLV, y exportar a Excel con los filtros aplicados. Tiene acceso al **detalle de cada visita** con sus fotos antes y después, motivo, comentarios y fecha, y puede consultar cualquier período histórico cargado en POP para hacer comparaciones o responder preguntas internas.

Lo que el cliente **no ve en ninguna versión**: zonas operativas internas de Picnic, identidad de los colocadores, coordenadas GPS de las visitas, ni información sobre coordinadores regionales o estructura del equipo de campo. Esta separación protege la operación interna de Picnic mientras entrega a PeYa total visibilidad sobre los resultados.

**Basic vs Extended.** La versión **Basic** le entrega a PeYa una herramienta de consulta y descarga moderna con todo lo necesario para el seguimiento: KPIs, breakdowns, tabla filtrable, detalle con fotos y exportación. La versión **Extended** amplía la autonomía analítica del cliente con el selector de rango de fechas, los filtros avanzados combinables, las tres pestañas de análisis (Por PLV, Por Geografía con drill-down e Histórico mensual) y un **Constructor de Reportes propio** con campos restringidos que nunca expone ID, GPS ni zona operativa. En la práctica, con Extended PeYa tiene autonomía analítica completa sin necesidad de pedirle reportes específicos a Picnic; con Basic depende de Picnic para análisis no contemplados en las vistas estándar.

| Funcionalidad | Basic | Extended |
|---|:-:|:-:|
| Login email + contraseña gestionado por admin | ✅ | ✅ |
| Vista solo lectura | ✅ | ✅ |
| Selector de período individual (cualquier mes histórico) | ✅ | ✅ |
| KPIs core reactivos a los filtros | ✅ | ✅ |
| Breakdowns por PLV y por geografía | ✅ | ✅ |
| Tabla de PDVs con sort y búsqueda | ✅ | ✅ |
| Filtros simples (provincia + PLV combinables) | ✅ | ✅ |
| Detalle de visita (sin ID, sin GPS, sin zona interna) | ✅ | ✅ |
| Fotos de cada visita visibles | ✅ | ✅ |
| Botón Excel con filtros aplicados | ✅ | ✅ |
| Selector de rango de fechas | ❌ | ✅ |
| Filtros avanzados combinables | ❌ | ✅ |
| Pestañas separadas (Por PLV, Por Geografía, Histórico mensual) | ❌ | ✅ |
| Constructor de Reportes propio (campos restringidos) | ❌ | ✅ |

---

## 4. Módulos Transversales

Sobre las cuatro experiencias operan un conjunto de módulos que dan soporte al funcionamiento integral de la plataforma: la ingesta de datos, la configuración territorial, la reportería avanzada y la administración del sistema.

### 4.1 Carga de PDVs

POP centraliza la ingesta de la información que PeYa envía mensualmente. El módulo está diseñado para **absorber la realidad operativa actual de Picnic sin imponer pasos manuales de preparación**: el sistema procesa los archivos tal como vienen, en los formatos que PeYa envía habitualmente, y deja al admin el control sobre cómo se interpreta cada hoja antes de impactar la base de datos.

Cuando el admin sube un archivo, POP **detecta automáticamente todas las hojas** y presenta una pantalla de configuración donde se define, para cada una, el tipo de formato (Establecimientos estándar o Partners) y el PLV asociado, sin requerir mapeo manual de columnas. Las hojas que no aportan al flujo operativo —por ejemplo, reportes de instalaciones realizadas por agencias externas— pueden marcarse como "Ignorar" y quedan excluidas del procesamiento. Antes de impactar la base de datos, POP presenta un **resumen consolidado** indicando cuántos PDVs se cargarán, distribuidos por hoja y por producto; recién cuando el admin confirma, los datos se persisten y quedan inmediatamente disponibles para todos los actores del sistema. Cada carga queda registrada en el log de auditoría con detalle del archivo procesado, período asignado, hojas incluidas e ignoradas, y volumen total importado.

**Basic vs Extended.** La versión **Extended** agrega dos capas de inteligencia sobre la carga. Por un lado, **detecta automáticamente duplicados** cuando el mismo PDV aparece con el mismo PLV en el mismo período, y ofrece tres formas de resolverlo según el caso operativo (descartar todos, reagregar como nuevas visitas, o seleccionar manualmente cuáles incorporar), cubriendo escenarios reales como cargas repetidas o errores en los envíos de PeYa. Por otro lado, **resuelve discrepancias** entre los datos que envía PeYa y las correcciones que los colocadores hacen en campo: si un colocador actualizó una dirección desactualizada durante una visita y en la siguiente carga PeYa vuelve a enviar la dirección vieja, POP detecta la discrepancia y le pregunta al admin si mantiene la versión corregida o la reemplaza, garantizando que el conocimiento operativo del equipo de campo no se pierda. Extended incorpora además la asignación del atributo **Cadena**, que en Basic no existe.

| Funcionalidad | Basic | Extended |
|---|:-:|:-:|
| Parser de archivo Excel (.xlsx) | ✅ | ✅ |
| Detección de hojas con clasificación (Establecimientos / Partners / Ignorar) + asignación de PLV | ✅ | ✅ |
| Definición manual de período (AAMM) al cargar | ✅ | ✅ |
| Reconocimiento nativo de los dos formatos que PeYa envía | ✅ | ✅ |
| Resumen pre-confirmación con detalle de la carga | ✅ | ✅ |
| Detección y resolución de duplicados | ❌ | ✅ |
| Resolución de discrepancias con datos editados en campo | ❌ | ✅ |
| Asignación de Cadena al PDV (atributo + filtro en reportes) | ❌ | ✅ |

---

### 4.2 Configuración de Zonas (Extended)

La configuración de zonas, exclusiva de la versión **Extended**, convierte la gestión territorial en una herramienta flexible que se adapta a la realidad cambiante del equipo de campo. Desde **Settings → Zonas**, el admin de Picnic crea, configura y administra las zonas que componen su estructura territorial: cuando un coordinador se incorpora, se va o se reorganiza una zona, el admin lo refleja directamente desde la interfaz.

El modal de edición presenta un **árbol jerárquico de la geografía** con checkboxes a cada nivel (provincia → ciudad → barrio), donde marcar un nivel incluye automáticamente todos sus hijos, y desmarcar hijos individuales permite construir composiciones complejas como "Buenos Aires excepto Mar del Plata" o "CABA excepto Centro". Antes de guardar, el sistema **valida superposiciones** con otras zonas existentes y muestra un aviso si hay solapamiento, permitiendo confirmar o ajustar la selección. Un **attention box** en el panel del admin alerta cuando hay PDVs del período actual en geografías no asignadas a ninguna zona, y abre un modal de asignación masiva para resolverlas.

Los cambios en zonas se aplican **solo a futuro**: las visitas históricas cerradas mantienen su snapshot original de zona, coordinador y PIN al momento de la visita, garantizando trazabilidad y permitiendo generar reportes pasados con la información correcta de quién era responsable en cada momento. Cada zona tiene asociado un coordinador regional con nombre, email y PIN de 4 dígitos, y genera automáticamente la URL única del Portal de Coordinadores.

**Basic vs Extended.** En la versión **Basic** las zonas se definen al inicio del proyecto y quedan fijas en el sistema: no son modificables desde la interfaz y aparecen únicamente como columna en la tabla del Panel de Gestión Central, para ordenar y consultar. La versión **Extended** habilita la gestión visual completa, la validación de superposiciones y el snapshot histórico de zona-coordinador-PIN en cada visita.

| Funcionalidad | Basic | Extended |
|---|:-:|:-:|
| Zonas fijas definidas al inicio del proyecto | ✅ | — |
| Sección Settings → Zonas con gestión visual | ❌ | ✅ |
| Crear, editar y eliminar zonas desde la interfaz | ❌ | ✅ |
| Árbol jerárquico de geografía con checkboxes | ❌ | ✅ |
| Composición de zona con suma y resta de regiones | ❌ | ✅ |
| Attention box de zonas no asignadas | ❌ | ✅ |
| Validación de superposiciones entre zonas | ❌ | ✅ |
| Asignación de coordinador por zona (nombre, email, PIN) | ❌ | ✅ |
| Snapshot histórico de zona-coordinador-PIN en cada visita | ❌ | ✅ |

---

### 4.3 Constructor de Reportes (Extended)

El Constructor de Reportes es la herramienta de análisis dedicada de POP, disponible exclusivamente en la versión **Extended**. Permite al admin de Picnic generar reportes a medida combinando libremente filtros, columnas y formato de salida, sin depender de la vista del Panel de Gestión Central ni de su estructura predefinida. Responde a una necesidad recurrente que PeYa Trade no resuelve: **armar un reporte específico para una pregunta puntual sin tener que exportar todo y procesar manualmente en Excel**.

El admin ingresa a la sección Reportes y define tres cosas: el **período** (individual o rango de fechas), los **filtros** a aplicar (geografía completa, PLV, estado, motivo, cadena, PDVs específicos, todos combinables entre sí) y el **tipo de output**. Hay dos formatos de salida que pueden generarse individualmente o en conjunto: un **listado** con elección libre de columnas (Grid, nombre, business name, dirección, zona, PLV, estado, fecha, ID del colocador, motivo, comentarios, GPS, etc.) y un **reporte estadístico** con KPIs agregados sobre el subset filtrado, con agregaciones configurables por dimensión (por PLV, por zona, por cadena, por motivo, o combinaciones como PLV × zona). El resultado se descarga como Excel; si el admin pidió listado más estadísticas, el archivo trae múltiples hojas. Para consultas muy grandes (más de 10.000 registros), POP procesa en background y notifica cuando el reporte está listo. Cada reporte generado queda registrado en el log con su configuración completa, lo que permite repetir o auditar consultas anteriores.

**Basic vs Extended.** El Constructor de Reportes no existe en la versión **Basic**. Basic resuelve la exportación mediante el botón **Excel** del Panel de Gestión Central, que descarga la vista actual con los filtros aplicados conservando todas las columnas. Ese botón sigue existiendo y funcionando igual en ambas versiones, y cubre la mayoría de los casos cotidianos. El Constructor está pensado para los casos donde el admin necesita combinar dimensiones que no están todas a la vista, generar reportes estadísticos complejos o producir archivos multi-hoja. Es exclusivo del admin de Picnic; PeYa tiene su propio constructor con campos restringidos, descripto en el Panel de Cliente.

| Funcionalidad | Basic | Extended |
|---|:-:|:-:|
| Sección dedicada a generación de reportes a medida | ❌ | ✅ |
| Selección libre de columnas a incluir | ❌ | ✅ |
| Filtros avanzados combinables | ❌ | ✅ |
| Output: listado de PDVs | ❌ | ✅ |
| Output: estadísticas agregadas (KPIs) | ❌ | ✅ |
| Excel multi-hoja (listado + estadísticas combinadas) | ❌ | ✅ |
| Agregaciones configurables (por PLV, geo, cadena, motivo) | ❌ | ✅ |
| Botón Excel del panel con filtros aplicados | ✅ | ✅ |

---

### 4.4 Settings, Reglas Automatizadas y Auditoría

Este módulo agrupa tres áreas administrativas que comparten un mismo principio: **el admin de Picnic mantiene el control operativo de POP desde un solo lugar mientras el sistema ejecuta automatizaciones que reducen el trabajo manual**.

La sección de **Settings** centraliza toda la configuración parametrizable, accesible solo para el admin. Permite gestionar productos (PLVs, con su flag de "producto compuesto" que habilita en la App de Campo los toggles independientes de sticker y saliente para casos como Kit Básico), motivos de no efectividad (con flag "cierra Sí/No" que define si al seleccionar ese motivo el PDV se cierra directamente o vuelve a la lista para reintento), usuarios de PeYa (alta, edición, reset de contraseña, activación/desactivación) y la cuenta del admin.

Las **reglas de negocio automatizadas** funcionan en segundo plano sin intervención del admin. El cierre directo por motivo se activa cuando el colocador marca una visita no efectiva con un motivo que tiene la flag "cierra Sí" (ej. "No existe", "No quiere PLV"), retirando el PDV de la lista inmediatamente. El cierre automático tras N intentos no efectivos consecutivos evita reintentos indefinidos sobre un PDV que repite un mismo obstáculo (ej. "Local cerrado"). El cierre o apertura manual del admin sobrescribe cualquier estado automático cuando es necesario.

El **Log de Auditoría** es el registro cronológico de toda la actividad relevante en POP, accesible exclusivamente desde el panel del admin y no expuesto a coordinadores ni a PeYa. Captura cada carga de PDVs con detalle completo, cada edición manual del admin (campo, valor anterior, valor nuevo), cada cierre o apertura manual, cada cambio de configuración y cada visita registrada por un colocador. La búsqueda por palabra clave permite encontrar rápidamente eventos relacionados con un Grid, un nombre o un archivo cargado; los filtros por rango de fechas acotan al período relevante; y la exportación a Excel habilita análisis externos.

**Basic vs Extended.** En Settings, la versión **Extended** suma tres sub-secciones que Basic no tiene: gestión de **Cadenas comerciales** con detección automática por nombre (el sistema sugiere clasificaciones al detectar patrones como "McDonald's Recoleta" y "McDonald's Pacífico", y el admin confirma o edita antes de aplicar); **gestión visual de mappings** recordados de hojas Partners (el sistema recuerda el mapeo de columnas de la primera carga y lo aplica automáticamente en las siguientes); y **configuración flexible de las reglas de cierre automático**, donde el admin define el número N de intentos desde la interfaz en lugar de tenerlo fijo. Extended incluye además la Configuración de Zonas descripta arriba. En las reglas, Basic tiene N=3 fijo mientras que Extended lo hace configurable. En el Log, Extended registra información significativamente más rica en cada visita (ID del colocador, zona, PIN, GPS), captura las ediciones que los colocadores hacen en campo, registra los reportes generados desde el Constructor y suma filtros avanzados combinables (por tipo de evento, usuario, ID, zona). En síntesis, Basic resuelve trazabilidad operativa (qué pasó y cuándo) mientras que Extended resuelve **trazabilidad nominal completa** (qué pasó, cuándo, quién y dónde).

| Funcionalidad | Basic | Extended |
|---|:-:|:-:|
| Settings → PLVs (crear, editar, marcar compuesto) | ✅ | ✅ |
| Settings → Motivos (crear, editar, flag "cierra Sí/No") | ✅ | ✅ |
| Settings → Usuarios PeYa (alta, edición, reset) | ✅ | ✅ |
| Settings → Cuenta del admin | ✅ | ✅ |
| Cierre directo de visita por motivo | ✅ | ✅ |
| Cierre / apertura manual desde modal | ✅ | ✅ |
| Cierre automático tras 3 intentos no efectivos (fijo) | ✅ | ❌ |
| Cierre automático tras N intentos configurable | ❌ | ✅ |
| Log de cargas | ✅ | ✅ |
| Log de ediciones manuales del admin | ✅ | ✅ |
| Log de visitas registradas (anónimas) | ✅ | ❌ |
| Log de visitas registradas (con ID, zona, PIN, GPS) | ❌ | ✅ |
| Búsqueda por palabra clave en el log | ✅ | ✅ |
| Filtro por rango de fechas en el log | ✅ | ✅ |
| Exportación del log a Excel | ✅ | ✅ |
| Settings → Cadenas con detección automática por nombre | ❌ | ✅ |
| Settings → Gestión visual de mappings de hojas Partners | ❌ | ✅ |
| Filtros avanzados en el log (tipo, usuario, ID, zona) | ❌ | ✅ |

## 5. Plan de Trabajo

El desarrollo se organiza en fases mensuales con entregables progresivos. Cada fase culmina con una demo de avance y la conformidad escrita de Picnic antes de pasar a la siguiente.

<div class="info-callout"> <strong>Nota sobre tiempos:</strong> los cronogramas presentados consideran un ritmo de trabajo sostenible y realista. Pueden surgir demoras operativas por imprevistos propios del desarrollo (bugs complejos, decisiones a discutir, dependencias externas, etc.). Cuando ocurra, se comunica con anticipación y se ajusta el cronograma en conjunto. </div>

#### Plan para Versión Básica (Agosto 2026 — Diciembre 2026)

**Duración total:** 5 meses (~20 semanas).  
**Volumen total:** 265 horas (~13 horas semanales promedio).

|Fase|Mes|Horas|Entregable principal|
|---|---|---|---|
|1. Foundation|Agosto|55|Setup técnico, modelo de datos, autenticación del admin, configuración inicial de PLVs y motivos.|
|2. Carga + Panel de Gestión|Septiembre|60|Carga de Locales funcionando + Panel de Gestión Central con KPIs, tabla, filtros simples y exportación.|
|3. Detalle + Panel de Cliente|Octubre|60|Detalle de Establecimiento y Detalle de Visita con historial + Panel de Cliente para Peya con vista de campañas y descarga.|
|4. App de Campo + Log|Noviembre|55|App de Campo completa con flujo de visita + Log de Auditoría.|
|5. Calibración + Producción|Diciembre|35|Testing exhaustivo, ajustes finales, deploy a producción, capacitación y soporte intensivo.|

#### Plan para Versión Pro (Agosto 2026 — Enero 2027)

**Duración total:** 6 meses (~24 semanas).  
**Volumen total:** 579 horas (~24 horas semanales promedio).

|Fase|Mes|Horas|Entregable principal|
|---|---|---|---|
|1. Foundation + Zonas|Agosto|110|Setup técnico, modelo de datos, autenticación, Gestión de Zonas y Líderes desde Settings (módulo más complejo del proyecto).|
|2. Carga Pro + Panel de Gestión Pro|Septiembre|110|Carga de Locales con detección de duplicados y discrepancias + Panel de Gestión Central con filtros avanzados y pestañas separadas.|
|3. Detalle + Constructor de Reportes|Octubre|110|Detalle de Establecimiento y Detalle de Visita con trazabilidad nominal + Constructor de Reportes funcionando.|
|4. App de Campo Pro + Portal de Líderes|Noviembre|110|App de Campo con PIN, ID, GPS, email a líder + Portal de Líderes funcionando.|
|5. Panel de Cliente Pro + Log avanzado|Diciembre|85|Panel de Cliente con todas las pestañas y Constructor de Reportes propio + Log con filtros avanzados.|
|6. Calibración + Producción|Enero|54|Testing exhaustivo, ajustes finales, deploy a producción, capacitación y soporte intensivo.|

#### Reuniones y Comunicación

- **Reuniones de revisión:** cada dos semanas con el equipo de Picnic.
- **Demo al cierre de cada fase:** en vivo, con conformidad por escrito antes de pasar a la siguiente.
- **Canal directo:** WhatsApp y email para consultas puntuales en horario laboral.

---

## 6. Inversión

#### Versión Básica

|Concepto|Horas|Inversión USD|Referencia ARS|
|---|---|---|---|
|Total desarrollo|265|**USD 9.275**|ARS ~14M|
|Distribución mensual (promedio)|53|USD 1.855|ARS ~2.8M|

#### Versión Pro

|Concepto|Horas|Inversión USD|Referencia ARS|
|---|---|---|---|
|Total desarrollo|579|**USD 20.265**|ARS ~31M|
|Distribución mensual (promedio)|96.5|USD 3.378|ARS ~5.1M|

_Referencias en ARS calculadas al tipo de cambio aproximado al momento de la propuesta. El valor final en pesos puede variar según la cotización al momento de cada facturación._

#### Tarifa Horaria

USD 35 por hora.

#### Forma de Pago

**Pago mensual contra entregable de fase**, al cierre de cada mes:

- Conformidad de fase + factura emitida = pago en 7 días corridos.
- La conformidad se otorga después de la demo de cierre de fase, con un plazo sugerido de 5 días hábiles de revisión por parte de Picnic.
- Si una fase entrega menos horas de las estimadas, se factura solo lo trabajado efectivamente.

---

## 7. Infraestructura y Costos Operativos

POP requiere de servicios de terceros para funcionar en producción. Estos servicios se contratan a nombre de Picnic, lo que garantiza la propiedad de las cuentas, los datos y el acceso bajo su control en todo momento.

**Estimación mensual: USD 80 aproximados.**

Este valor cubre los servicios necesarios para que POP funcione en producción: hosting de la aplicación, base de datos, almacenamiento de fotos, envío de emails, monitoreo y dominio personalizado. La variabilidad principal viene del volumen de fotografías acumuladas con el tiempo, pero se mantiene en ese orden de magnitud durante el uso normal del sistema.

Estos costos son **independientes del modelo elegido (Básica o Pro)**: son los mismos en ambos casos. El upgrade a Pro no incrementa la infraestructura.

#### Lo que está incluido en el desarrollo sin costo adicional

- Configuración inicial completa de todos los servicios.
- Vinculación del dominio personalizado (ej. `pop-picnic.com.ar`).
- Certificados de seguridad SSL/HTTPS.
- Configuración de backups automáticos.
- Acceso a paneles de monitoreo de salud del sistema.

#### Disponibilidad y Seguridad

- **Uptime objetivo:** 99.9% mensual.
- **Backups:** automáticos diarios, retenidos durante 30 días.
- **Encriptación:** todas las comunicaciones HTTPS, base de datos encriptada en reposo.
- **Acceso protegido** con autenticación diferenciada según rol.
- **Aislamiento de datos:** la información del cliente solo es visible para usuarios autorizados.

---

## 8. Plan de Mantenimiento Post-entrega

Una vez POP esté en producción, se ofrece un **plan flexible de mantenimiento mensual** para garantizar la continuidad operativa y atender ajustes según necesidades emergentes.

#### Plan Flex

**Volumen base:** hasta 10 horas/mes facturadas a USD 35/hora.  
**Inversión esperada mensual:** USD 0 a USD 350 según uso real.

<div class="info-callout"> <strong>Modalidad:</strong> solo se factura el tiempo efectivamente utilizado. Si en un mes no surge ninguna necesidad de soporte, no hay facturación de mantenimiento ese mes. </div>

**Cubierto sin facturación adicional bajo este esquema:**

- Atención a incidencias y resolución de bugs originados en el desarrollo.
- Soporte técnico al equipo de Picnic por email/WhatsApp en horario laboral.
- Ajustes menores que surjan del uso del sistema y mejoras pequeñas de UX.
- Verificación mensual de backups y salud del sistema.
- Monitoreo proactivo de errores reportados por el sistema.
- Asistencia para resolver inconvenientes que surjan dentro del proyecto principal en curso.

**Excedente sobre 10 horas mensuales:**

Si en un mes específico surge una necesidad que exceda las 10 horas, se conversa antes de avanzar y se acuerda cómo proceder (postergar, priorizar, o autorizar horas adicionales a la misma tarifa estándar de USD 35/hora).

**Desarrollos nuevos o cambios mayores** (no incluidos en el plan flex):

Funcionalidades nuevas, cambios mayores de diseño, integraciones con sistemas externos, migración de datos históricos, módulos adicionales — se cotizan aparte como proyecto puntual.

**Condiciones generales:**

- Sin permanencia mínima.
- Cancelable con 30 días de aviso.
- Horas no utilizadas en el mes no se acumulan al siguiente.

---

## 9. Capacitación

La transición desde PEYA Trade hacia POP incluye capacitación sin costo para los equipos de Picnic y Peya:

- **Manual de usuario en formato escrito** entregado al cierre del proyecto, con instrucciones paso a paso de las principales operaciones.
- **Material de apoyo** para distribuir a colocadores y líderes regionales (instrucciones de uso de la App de Campo y del Portal de Líderes).
- **Consultas y dudas durante el período de adopción** atendidas vía mensajería y email sin costo adicional.

Si Picnic identifica necesidad de sesiones presenciales o videollamadas dedicadas de capacitación más allá del material escrito, se conversan y coordinan sin problema dentro del plan flex de mantenimiento.

---

## 10. Modalidad de Contratación

Las dos versiones presentadas (Básica y Pro) son **alternativas excluyentes al inicio del proyecto**. Picnic elige cuál implementar antes del kick-off.

<div class="info-callout"> <strong>Flexibilidad para incorporar funcionalidades Pro sobre Básica:</strong> si Picnic elige Básica y posteriormente desea incorporar funcionalidades presentes en Pro, no es necesario contratar el paquete Pro completo. Cada funcionalidad adicional se conversa, se evalúa su impacto técnico (algunas requieren cambios de base de datos no triviales) y se cotiza individualmente según el alcance acordado, generando una propuesta complementaria. El trabajo ya realizado en Básica no se descarta: las funcionalidades nuevas se incorporan sobre lo existente, permitiendo a Picnic crecer en el sistema según las necesidades reales que vayan surgiendo del uso. </div>

---

## 11. Términos Generales

**Propiedad del código.** El código fuente y todos los activos desarrollados son propiedad de Picnic una vez finalizado el desarrollo y abonado el total del proyecto. Se entrega el repositorio completo con su historial.

**Confidencialidad.** Toda información compartida durante el desarrollo (datos del cliente, base de partners, criterios operativos, etc.) se trata como confidencial.

**Uso del proyecto como portfolio profesional.** Una vez finalizado el desarrollo, el proyecto puede ser referenciado en el portfolio profesional de la desarrolladora a fines de demostración de trabajo realizado. La referencia incluye nombre del cliente (Picnic), descripción general del sistema (gestión de PLVs), capturas de pantalla genéricas que no expongan información sensible y stack técnico utilizado. No se publica ningún dato operativo, comercial o de partners en cumplimiento con la cláusula de confidencialidad. Si Picnic tiene preferencia sobre cómo presentar este material, se acuerda antes de su publicación.

**Cambios de alcance.** Cambios menores (ajustes de UI, textos, comportamientos pequeños) están contemplados en el buffer de cada fase. Cambios mayores que impliquen nuevo desarrollo se documentan y cotizan por escrito antes de ejecutarse.

**Comunicación.** Reuniones de revisión quincenales con Picnic. Canal directo de WhatsApp/email para consultas puntuales durante días hábiles. Demo en vivo al cierre de cada fase.

**Garantía post-lanzamiento.** Durante los primeros 30 días posteriores a la salida a producción, cualquier bug originado en el desarrollo se corrige sin cargo adicional, incluso fuera del plan flex de mantenimiento.

**Aceptación de fase.** Cada fase se considera entregada una vez Picnic revisa el entregable y comunica conformidad. Plazo de revisión sugerido: 5 días hábiles.

**Demoras operativas.** El cronograma presentado es realista pero sujeto a imprevistos propios del desarrollo de software. Si surgen demoras, se comunican con anticipación y se reajusta el plan en conjunto con Picnic.

---

## 12. Módulos Adicionales

Más allá del alcance principal de las versiones Básica y Pro, POP está diseñado para crecer en el tiempo según las necesidades reales que vayan surgiendo del uso. Esta sección presenta una serie de módulos y extensiones que pueden incorporarse posteriormente como proyectos puntuales, cada uno cotizable de forma independiente.

Algunos módulos requieren funcionalidades específicas de la versión Pro como pre-requisito técnico (por ejemplo, los módulos analíticos individuales necesitan que se capture ID y GPS por visita, algo que la versión Básica no contempla). Otros son agnósticos a la versión inicial elegida y pueden incorporarse sobre cualquier implementación.

| Módulo adicional                             | Descripción breve                                                                                                                                                               | Viabilidad                                                                                                          |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Migración de base histórica**              | Procesamiento, normalización e ingesta de los Excels históricos de Picnic (desde 2019) como períodos pasados consultables dentro de POP.                                        | Disponible sobre Básica o Pro. Cotizable como proyecto independiente según volumen y calidad de los datos a migrar. |
| **Mapa interactivo y geo-analítica**         | Vista de mapa con pins de estado por local, filtros geográficos, heatmaps de efectividad por zona.                                                                              | Disponible sobre Básica o Pro. Requiere integración con API de mapas con costo recurrente adicional.                |
| **Comparativas y tendencias entre períodos** | Gráficos de evolución temporal de KPIs, comparativa lado a lado de dos períodos cualesquiera, detección de outliers y análisis por dimensión.                                   | Disponible sobre Básica o Pro.                                                                                      |
| **Alertas y notificaciones automáticas**     | Emails automáticos al admin ante condiciones configurables (locales con N intentos sin éxito, zonas con baja efectividad, inactividad del equipo de campo, etc.).               | Disponible sobre Básica o Pro.                                                                                      |
| **Módulo de Seguimiento de Colocadores**     | Análisis individual del desempeño de cada colocador a partir del ID capturado en cada visita: efectividad, distribución por PLV, motivos top, tendencia temporal, GPS matching. | Requiere Pro implementado (depende de ID y GPS por visita).                                                         |
| **Módulo de Seguimiento de Líderes**         | Análisis individual del desempeño de cada líder regional a partir del snapshot histórico de zona-líder-PIN en cada visita.                                                      | Requiere Pro implementado (depende del snapshot de zonas).                                                          |

Cada módulo adicional incluye su propia propuesta detallada con alcance, horas estimadas, inversión y plazo cuando Picnic decida avanzar con él. La cotización se realiza al momento de la solicitud para reflejar las condiciones vigentes y el contexto del sistema en ese momento.

---

## 13. Próximos Pasos

Si Picnic acuerda con la presente propuesta:

1. **Firma de acuerdo** (esta propuesta + adenda de propiedad intelectual y confidencialidad).
2. **Elección de modalidad** (Básica o Pro).
3. **Definición de stack tecnológico** (1 semana). Se documenta y comparte con Picnic.
4. **Apertura de cuentas** de servicios de terceros a nombre de Picnic (~1 semana).
5. **Kick-off del proyecto:** inicio de Fase 1 en la primera semana de agosto.
6. **Primera reunión de revisión:** segunda quincena de agosto.

---

*Documento sujeto a aceptación. Válido por hasta 31 de Julio 2026.*

<strong>Nota:</strong> Esta propuesta es confidencial y de uso exclusivo de Picnic. Queda prohibida su reproducción total o parcial sin autorización expresa de la autora.
### Comparativa rápida

```pricing
{
  "basica": {
    "title": "Versión Básica",
    "price": "USD 9.275",
    "detail": "265 horas · Agosto a Diciembre 2026",
    "features": [
      "Reemplazo completo de PEYA Trade",
      "Dashboard con KPIs y filtros simples",
      "App de campo sin autenticación",
      "Portal de Peya con descarga de Excel",
      "Log de auditoría básico"
    ]
  },
  "pro": {
    "title": "Versión Pro",
    "price": "USD 20.265",
    "detail": "579 horas · Agosto 2026 a Enero 2027",
    "features": [
      "Todo lo de Básica",
      "Trazabilidad nominal completa (DNI + GPS)",
      "Dashboard de Líderes Regionales",
      "Constructor de Reportes dedicado",
      "Gestión flexible de zonas",
      "Filtros avanzados y vistas múltiples"
    ]
  }
}
```
