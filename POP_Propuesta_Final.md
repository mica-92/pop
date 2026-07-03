
# Propuesta De Desarrollo: POP — Plataforma Operativa De PLVs

**Cliente:** Picnic
**Presentada por:** María Micaela Ninni
**Fecha:** Julio 2026
**Versión:** 1.0

> notas mica hoy por la mañana: cambiar líderes a coordinadores, quiero sacar fechas y dejar solo meses de implementación. cambiar establecimiento a locales comerciales. unificar peta pedidosya. cambiar básica y pro a basic y extended

## 1. Resumen Ejecutivo

**POP (Plataforma Operativa de PLVs)** es una plataforma web diseñada a medida para Picnic con el objetivo de **modernizar y automatizar el control y seguimiento de la colocación de PLVs (Publicidad en Lugares de Venta)**. Actualmente, este proceso se realiza sobre la aplicación PeYa Trade (PYT), una herramienta que presenta limitaciones operativas significativas, dificultando la obtención y entrega de resultados oportunos y confiables a PedidosYa.

Las limitaciones del sistema actual se evidencian en el uso cotidiano de la aplicación. Estas radican principalmente en un deficiente manejo de la información, y pueden resumirse en 4 puntos centrales:

- **Usabilidad y análisis limitado:** Interfaz rígida que no permite filtrar ni segmentar datos dinámicamente; obliga a exportar manualmente a Excel para cada reporte, generando demoras y restando confiabilidad a la toma de decisiones.
- **Falta de trazabilidad temporal y geográfica:** Sin historial ni métricas evolutivas; imposibilita comparar la evolución de establecimientos entre períodos, ni segmentar por localidad o rango de tiempo para planificar prioridades.
- **Fragmentación de materiales PLV:** Información aislada por tipo de material (bicicletero, cartel, sticker) sin una vista consolidada por establecimiento; obliga a cruces manuales, incrementando errores y esfuerzo operativo en auditorías integrales.
- **Debilidades en el control operativo:** Carece de trazabilidad de visitas (quién, cuándo, condiciones), controles de acceso débiles y mala integración del registro fotográfico, lo que compromete la seguridad, integridad y auditabilidad del proceso.

Esto obstaculiza la detección de cuellos de botella operativos —zonas o productos con bajo desempeño—, inhabilita un seguimiento eficienciente de la campaña y fundamentalmente **limita la capacidad de Picnic para anticiparse a las necesidades de su cliente para ofrecer soluciones proactivas.**

**POP centraliza la operación con una interfaz rápida y moderna, construida sobre una nueva arquitectura de base de datos que integra de forma eficiente las todas las diferentes dimensiones del proyecto - locales comerciales, PLVs, períodos, coordinadores y cliente - dentro de un ecosistema unificado.** -> switch to callout 

Esta nueva herramienta no solo agiliza y automatiza procesos que hoy se realizan a manualmente, sino que facilita la visualización del estado actual de cada campaña, permite la extracción de información y 



consulta de períodos pasados queda resuelta de forma nativa, garantizando a Picnic la capacidad de responder a Peya con la velocidad que la operación requiere.

**POP reúne:**

- Un **Panel de Gestión Central** para el equipo de Picnic.
- Una **App de Campo** para colocadores en terreno.
- Un **Portal de Líderes** para acceso simplificado de los líderes regionales.
- Un **Panel de Cliente** para que Peya posea visibilidad directa sobre el avance de sus campañas.

Esta propuesta presenta dos modalidades de implementación: **Versión Básica** y **Versión Pro**. Ambas reemplazan el flujo de carga de datos manual actual, comparten la misma arquitectura técnica y entregan valor operativo desde el primer mes.

La ejecución se realiza en fases mensuales: entre **agosto y diciembre de 2026** para la Versión Básica (5 fases) y entre **agosto de 2026 y enero de 2027** para la Versión Pro (6 fases). Cada fase culmina con un entregable concreto y una demo de avance.

POP se diseña en coordinación constante con Picnic, incorporando directamente el aprendizaje acumulado sobre las dificultades y obstáculos que el equipo enfrenta hoy. **Cada decisión técnica responde a un problema operativo real y a una utilización eficiente y moderna de los datos disponibles, habilitando una visualización holística de cada campaña y el desarrollo de estrategias de marketing fundamentadas en información concreta.**

**POP no es solo un reemplazo: es la oportunidad de transformar la gestión de PLVs en una ventaja competitiva, devolviéndole a Picnic el control, la velocidad y la inteligencia operativa que necesita para responder a su cliente y proyectarse a futuro.**


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

---
---

## 2. Alcance Del Proyecto

POP se compone de cuatro experiencias diferenciadas, una por cada actor del proceso. Cada una está pensada para que la persona responsable acceda exclusivamente a la información necesaria para su gestión, con Picnic como coordinador central y veedor de toda la cadena de colocación.

### Picnic: Panel de Gestión Central

El equipo de Picnic accede a un panel central desde donde gestiona y visualiza toda la operación:

- **Carga de locales para el período actual** que envía el cliente. POP detecta automáticamente las hojas, identifica el tipo de formato y permite confirmar antes de importar.
- **Visualización del estado de cada campaña** en una vista unificada con KPIs reactivos (total, visitados, efectivos, pendientes, abiertos, cerrados), gráficos de avance por producto y por geografía, y tabla completa de locales con sort, búsqueda y filtros.
- **Acceso al detalle de cada establecimiento** incluyendo su historial completo de visitas en todos los períodos cargados.
- **Generación de reportes a medida** eligiendo columnas y filtros, exportables a Excel.
- **Configuración desde Settings**: productos (PLVs), motivos de no efectividad, usuarios de Peya, reglas de cierre automático, y (en _Pro_) zonas operativas, líderes regionales y cadenas comerciales.
- **Auditoría de cambios** desde un log de modificaciones que registra cada acción del sistema.

### Peya: Panel de Cliente

Acceso de solo lectura para el equipo de Peya, con login propio gestionado por Picnic.

- Visualiza el estado de sus campañas en cualquier período cargado.
- Accede al **status e información de cada visita**.
- Genera **reportes a medida** eligiendo columnas y filtros (_Pro_), o descarga el listado del período actual con filtros aplicados (_Básica_).

El cliente **no accede a información operativa interna de Picnic**: no ve zonas operativas, líderes, identidad de colocadores ni coordenadas GPS de las visitas.

### Colocadores: App de Campo

Aplicación web optimizada para uso en celular (PWA), accesible desde cualquier navegador y opcionalmente instalable en la home screen del dispositivo.

- **Listado de locales pendientes** filtrado por zona y producto.
- **Carga de visita** con:
    - Toggle efectiva sí/no.
    - Carga de fotos.
    - Motivo de no efectividad (si aplica), elegible desde lista precargada.
    - Comentarios opcionales.
- **Compresión automática de fotos** en el dispositivo: cada foto se reduce de ~5MB a ~250KB antes de subir, ahorrando datos móviles del colocador y acelerando la operación.
- **Cámara nativa o galería**: el colocador elige cómo subir cada foto.

La **Versión Pro** además ofrece:

- Acceso protegido con PIN de zona.
- ID obligatorio en cada visita para trazabilidad nominal.
- Captura de GPS al guardar para verificación de presencia.
- Edición de los datos del establecimiento desde campo + confirmación obligatoria.
- Botón de aviso al líder con email automático ante 3 intentos fallidos de PIN.

### Líderes Regionales: Portal de Líderes _(Pro)_

Cada líder regional accede a su dashboard mediante un link único y un PIN de 4 dígitos. Sin necesidad de usuario y contraseña.

- Visualiza los locales de su zona pendientes de visitar en el período actual.
- Descarga el listado en Excel (consolidado o multi-hoja por producto) para distribuir a su equipo de colocadores.
- Visualiza el PIN de zona que comparte con sus colocadores para acceder a la app de campo.

En la **Versión Básica** este acceso no existe: el admin descarga los Excels filtrados por provincia y los envía manualmente a sus líderes regionales, manteniendo el flujo de coordinación que Picnic tiene hoy.

---

## 3. Diferencias entre Versiones

Ambas versiones reemplazan completamente el flujo actual y resuelven los problemas operativos identificados. La diferencia principal está en el **nivel de control, automatización y trazabilidad**.

### Versión Básica — Operación Esencial

Diseñada para reemplazar PEYA Trade con una herramienta moderna sin sumar complejidad operativa. Incluye:

- Carga de locales con detección de hojas y resumen pre-confirmación.
- Panel de Gestión Central con KPIs, breakdowns y tabla unificada con filtros simples (provincia + PLV).
- Detalle de establecimientos con historial completo de visitas.
- Detalle de visitas con fotos y motivos.
- Panel de Cliente para Peya con vista de campañas y descarga de Excel.
- App de Campo sin autenticación (acceso libre por URL).
- Settings para productos, motivos y usuarios.
- Log de auditoría con búsqueda por palabra clave y filtros básicos.

**Lo que NO incluye:**

- Acceso individual para líderes regionales.
- Constructor de reportes con elección de columnas.
- Filtros avanzados combinables.
- Pestañas separadas Por PLV / Por Geografía / Histórico mensual.
- ID o identificador del colocador en visitas.
- GPS de la visita.
- Atributo "Cadena" del establecimiento.
- Detección y resolución de duplicados durante la carga.
- Resolución de discrepancias con datos editados en campo.
- Gestión flexible de zonas desde la interfaz (las zonas se definen al inicio del proyecto y son fijas).
- Reglas configurables de cierre automático (la regla es fija: cierre tras 3 intentos no efectivos consecutivos).

### Versión Pro — Operación Completa con Trazabilidad

Incluye todo lo de la Básica más:

- **Acceso individual para Líderes Regionales** con link único y PIN.
- **Gestión flexible de Zonas** desde Settings con árbol jerárquico de geografía (composición por suma/resta de regiones a cualquier nivel: provincia, ciudad, barrio).
- **Constructor de Reportes** dedicado, con elección de columnas, filtros combinables y output como listado, estadísticas o ambos en multi-hoja.
- **Filtros avanzados combinables** en el panel (todas las dimensiones disponibles).
- **Selector de rango de fechas** para análisis multi-período.
- **Pestañas separadas** Por PLV, Por Geografía (con drill-down) y Histórico de KPIs por mes pasado.
- **App de Campo con autenticación**: PIN de zona obligatorio, ID por visita, GPS al guardar.
- **Email automático al líder** ante 3 intentos fallidos de PIN del colocador.
- **Edición de datos del establecimiento** desde la app de campo con confirmación obligatoria.
- **Atributo "Cadena"** del establecimiento, con detección automática por nombre (sistema sugiere, admin confirma).
- **Detección y resolución de duplicados** durante la carga (descartar / reagregar / selección manual).
- **Resolución de discrepancias** entre datos de Peya y datos editados en campo.
- **Reglas configurables de cierre automático** (N intentos configurable).
- **Filtros avanzados en el log** (por tipo de evento, usuario, ID, zona).
- **Snapshot histórico** de zona, líder y PIN en cada visita para análisis posterior.

---

## 4. Inventario Completo de Funcionalidades

### Módulo 1 — Carga de Locales

|Funcionalidad|Básica|Pro|
|---|:-:|:-:|
|Parser de archivo Excel (.xlsx)|✅|✅|
|Detección de hojas con clasificación (Establecimientos / Partners / Ignorar) + asignación de PLV|✅|✅|
|Definición manual de período (AAMM) al cargar|✅|✅|
|Reconocimiento nativo de los dos formatos que Peya envía|✅|✅|
|Resumen pre-confirmación con detalle de la carga|✅|✅|
|Detección y resolución de duplicados|❌|✅|
|Resolución de discrepancias con datos editados en campo|❌|✅|
|Asignación de Cadena al establecimiento (atributo + filtro en reportes)|❌|✅|

**Descripción del Módulo:** POP centraliza la ingesta de la información que Peya envía mensualmente. El módulo está diseñado para absorber la realidad operativa actual de Picnic sin imponer pasos manuales de preparación: el sistema procesa los archivos tal como vienen, en los formatos que Peya envía habitualmente, y deja al admin de Picnic el control sobre cómo se interpreta cada hoja antes de impactar la base de datos. Cuando el admin sube un archivo, POP detecta automáticamente todas las hojas y presenta una pantalla de configuración donde se define para cada una el tipo de formato (Establecimientos estándar o Partners) y el PLV asociado, sin requerir mapeo manual de columnas. Las hojas que no aportan al flujo operativo —por ejemplo, reportes de instalaciones realizadas por agencias externas— pueden marcarse como "Ignorar" y quedan excluidas del procesamiento. Antes de impactar la base de datos, POP presenta un resumen consolidado indicando cuántos establecimientos se cargarán, distribuidos por hoja y por producto; recién cuando el admin confirma, los datos se persisten y quedan inmediatamente disponibles para todos los demás actores del sistema. Cada carga queda registrada en el log de auditoría con detalle del archivo procesado, período asignado, hojas incluidas e ignoradas, y volumen total importado.

**Diferencia entre versiones:** La Versión Pro agrega dos capas adicionales de inteligencia sobre la carga. Por un lado, detecta automáticamente duplicados cuando el mismo establecimiento aparece con el mismo PLV en el mismo período y ofrece al admin tres formas de resolverlo según el caso operativo (descartar todos, reagregar como nuevas visitas, o seleccionar manualmente cuáles incorporar), cubriendo escenarios reales como cargas accidentalmente repetidas o errores administrativos en los envíos de Peya. Por otro lado, resuelve discrepancias entre los datos que envía Peya y las correcciones que los colocadores hacen en campo: si un colocador actualizó una dirección desactualizada durante una visita y en la siguiente carga Peya vuelve a enviar la dirección vieja, POP detecta la discrepancia y le pregunta al admin si pisa la versión corregida o la mantiene, garantizando que el conocimiento operativo del equipo de campo no se pierda. La Pro también incorpora la asignación del atributo "Cadena" a cada establecimiento, que en la Básica no existe.

---

### Módulo 2 — Panel de Gestión Central

|Funcionalidad|Básica|Pro|
|---|:-:|:-:|
|Login con email y contraseña|✅|✅|
|Home con KPIs del período actual (Total, Visitados, Efectivos, Pendientes, Abierto/Cerrado, motivos)|✅|✅|
|Selector de período individual (cualquier mes histórico)|✅|✅|
|KPIs reactivos a filtros aplicados|✅|✅|
|Breakdown por PLV y por geografía (barras)|✅|✅|
|Tabla de locales con todas las columnas + sort + búsqueda|✅|✅|
|Filtros simples: provincia + PLV (combinables)|✅|✅|
|Exportación a Excel con filtros aplicados|✅|✅|
|Vista de períodos pasados como snapshot al cierre|✅|✅|
|Selector de rango de fechas|❌|✅|
|Filtros avanzados combinables (ciudad, barrio, zona, estado, motivo, cadena)|❌|✅|
|Pestaña separada "Por PLV"|❌|✅|
|Pestaña separada "Por Geografía" con drill-down|❌|✅|
|Pestaña "Histórico de KPIs por mes pasado"|❌|✅|

**Descripción del Módulo:** El Panel de Gestión Central es el centro de control del equipo de Picnic sobre la operación completa. Desde una única interfaz, el admin monitorea el estado de cada campaña, accede al detalle de cualquier establecimiento, supervisa el trabajo del equipo de campo, y exporta la información que necesita para responder a Peya en cualquier momento. Al ingresar, ve el panel del período actual con los KPIs core en la parte superior, dos visualizaciones de breakdown (por PLV y por geografía) que muestran avance por producto y cobertura territorial, y la tabla completa de locales del período con todas sus columnas de información (identificador, nombre, tipo, contacto, ubicación, producto, estado, fecha de visita). El admin puede ordenar por cualquier columna, buscar por Grid o nombre, filtrar según las dimensiones disponibles en su versión, y exportar a Excel la vista actual conservando todos los filtros. Los KPIs se recalculan dinámicamente según los filtros aplicados, de modo que filtrar por una provincia o producto específico actualiza instantáneamente los números arriba. El selector de período permite navegar a cualquier mes histórico cargado en POP, mostrando una vista consistente de la operación pasada.

**Diferencia entre versiones:** En ambas versiones el admin puede filtrar por provincia y PLV combinándolos entre sí, lo cual resuelve la operatoria cotidiana. La Versión Pro amplía radicalmente la capacidad analítica con filtros avanzados sobre todas las dimensiones disponibles (ciudad, barrio, zona Picnic, estado, motivo específico de no efectividad, cadena comercial), combinables libremente entre sí, y agrega el selector de rango de fechas para análisis multi-período. Pro también incorpora tres pestañas adicionales que reorganizan la información para análisis específicos: una pestaña Por PLV que agrupa los locales por producto mostrando el desempeño de cada uno de forma independiente; una pestaña Por Geografía que permite navegar la jerarquía territorial con drill-down (provincia → ciudad → barrio → zona) mostrando KPIs agregados en cada nivel; y una pestaña de Histórico de KPIs por mes pasado, que muestra los indicadores clave de cada período cerrado en una tabla simple para comparar el desempeño mes a mes de un vistazo. Las columnas de zona, ciudad y barrio están visibles y se pueden ordenar en ambas versiones; la diferencia es la capacidad de filtrar por esos niveles, no la de verlos.

---

### Módulo 3 — Detalle de Establecimiento

|Funcionalidad|Básica|Pro|
|---|:-:|:-:|
|Información general del establecimiento|✅|✅|
|Edición de campos (nombre, teléfono, dirección, abierto/cerrado, zona)|✅|✅|
|Historial completo de visitas en todos los períodos|✅|✅|
|Log de cambios del establecimiento|✅|✅|
|Acción: cerrar / reabrir manualmente|✅|✅|
|Edición del atributo Cadena|❌|✅|

**Descripción del Módulo:** El detalle de establecimiento se abre desde cualquier vista del Panel de Gestión Central que liste locales, y permite al admin profundizar en cualquier registro puntual sin perder el contexto del panel general. Es la respuesta a una necesidad operativa concreta: poder responderle a Peya cuando pregunta por un local específico, auditar la actividad cuando algo no cuadra, y corregir información en el momento sin procesar datos por fuera del sistema. Muestra la información general del establecimiento (Grid, nombre del partner, business name, teléfono, dirección completa, estado abierto/cerrado) y permite editar los campos permitidos directamente, con cada modificación quedando registrada en el log de cambios con fecha, hora y descripción. El admin puede también cerrar o reabrir manualmente el establecimiento: cerrarlo lo retira de las listas operativas y no aparecerá para visitas en ningún período hasta que se reabra. Incluye un historial cronológico completo de todas las visitas que el local recibió a lo largo del tiempo, en cualquier período cargado, con fecha, PLV asociado, estado y motivo cuando corresponde, lo que permite responder preguntas como "¿este local cuántas veces fue visitado?", "¿qué productos ya tuvo?" o "¿siempre hay problemas para colocar acá?".

**Diferencia entre versiones:** La Versión Pro agrega el atributo "Cadena" como campo editable desde el detalle del establecimiento, lo que permite agrupar locales por marca comercial (Carrefour, McDonald's, Café Martínez, etc.) y filtrar/reportar sobre esa dimensión. La Versión Básica no soporta el concepto de cadena: cada local es independiente. El resto del módulo es idéntico entre ambas versiones.

---

### Módulo 4 — Detalle de Visita

|Funcionalidad|Básica|Pro|
|---|:-:|:-:|
|Estado de la visita (efectiva / no efectiva)|✅|✅|
|Motivo de no efectividad|✅|✅|
|Fotos antes y después|✅|✅|
|Fecha y hora de la visita|✅|✅|
|Comentarios del colocador|✅|✅|
|Acción: cerrar / reabrir visita manualmente|✅|✅|
|ID del colocador|❌|✅|
|GPS del dispositivo al guardar la visita|❌|✅|

**Descripción del Módulo:** El detalle de visita se abre desde el historial del establecimiento o desde cualquier tabla que liste visitas, y muestra el registro completo de una colocación puntual. Incluye el estado (efectiva o no efectiva), el motivo cuando aplica, los comentarios que dejó el colocador en campo, las fotos del antes y del después tomadas durante la visita, y la fecha y hora exacta en que se guardó. Las fotos se muestran como miniaturas inline dentro del modal, de tamaño suficiente para identificar el contenido sin necesidad de abrirlas a pantalla completa. El admin puede cerrar o reabrir manualmente la visita: una visita cerrada deja de aparecer en las listas operativas del colocador, mientras que una reabierta vuelve a estar disponible para reintentar. Estas acciones manuales del admin quedan registradas en el log general de auditoría del sistema.

**Diferencia entre versiones:** La Versión Pro agrega trazabilidad nominal completa sobre cada visita: registra el ID del colocador que la realizó y captura el GPS del dispositivo al momento de guardarla. Esto permite auditoría individual ("¿quién hizo esta visita?") y verificación de presencia en el local (contrastando el GPS capturado con la lat/lon del establecimiento). La Versión Básica no captura ni ID ni GPS desde la app de campo, por lo que las visitas quedan operativamente anónimas: sirven para registrar el estado de las campañas pero no para auditar el trabajo individual de los colocadores. El resto de la información de la visita (estado, motivo, fotos, comentarios, acciones de cierre/apertura manual) es idéntica entre ambas versiones.

---

### Módulo 5 — Constructor de Reportes _(solo Pro)_

|Funcionalidad|Básica|Pro|
|---|:-:|:-:|
|Sección dedicada a generación de reportes a medida|❌|✅|
|Selección libre de columnas a incluir|❌|✅|
|Filtros avanzados combinables|❌|✅|
|Output: listado de locales|❌|✅|
|Output: estadísticas agregadas (KPIs)|❌|✅|
|Excel multi-hoja (listado + estadísticas combinadas)|❌|✅|
|Agregaciones configurables (por PLV, geo, cadena, motivo)|❌|✅|

**Descripción del Módulo:** El Constructor de Reportes es la herramienta de análisis dedicada de POP, disponible exclusivamente en la Versión Pro. Permite al admin de Picnic generar reportes a medida combinando libremente filtros, columnas y formato de salida, sin depender de la vista del Panel de Gestión Central ni de su estructura predefinida. Es la respuesta a una necesidad recurrente que PEYA Trade no resuelve: poder armar un reporte específico para responder a una pregunta puntual de Peya o del equipo interno sin tener que exportar todo y procesar manualmente en Excel. El admin entra a la sección Reportes desde el menú principal y define tres cosas: el período (individual o rango de fechas), los filtros que quiere aplicar (geografía completa, PLV, estado, motivo, cadena, establecimientos específicos, todos combinables libremente entre sí) y el tipo de output. Hay dos formatos de salida que pueden generarse individualmente o en conjunto: un listado con elección libre de columnas a incluir (Grid, Nombre, Business Name, dirección completa, zona, PLV, estado, fecha, ID del colocador, motivo, comentarios, GPS, etc.) y un reporte estadístico con KPIs agregados sobre el subset filtrado, con agregaciones configurables por dimensión (por PLV, por zona, por cadena, por motivo, o combinaciones como PLV × zona). El resultado se descarga como Excel; si el admin pidió listado más estadísticas, el archivo trae múltiples hojas. Para consultas muy grandes (más de 10.000 registros), POP procesa en background y notifica al admin cuando el reporte está listo. Cada reporte generado queda registrado en el log con su configuración completa, lo que permite repetir o auditar consultas anteriores.

**Diferencia entre versiones:** El Constructor de Reportes no existe en la Versión Básica. La Básica resuelve la exportación de datos mediante el botón "Excel" del Panel de Gestión Central, que descarga la vista actual con los filtros aplicados conservando todas las columnas. Ese botón sigue existiendo y funcionando igual en ambas versiones, y cubre la mayoría de los casos cotidianos (exportar lo que se está viendo). El Constructor de Reportes está pensado para los casos donde el admin necesita combinar dimensiones que no están todas a la vista, generar reportes estadísticos más complejos, o producir archivos multi-hoja con listado y agregaciones combinadas. Es exclusivo del admin de Picnic: no se expone a líderes ni a Peya en su versión completa (aunque Peya tiene su propio constructor con campos restringidos, descripto en el Módulo 7).

---

### Módulo 6 — Gestión de Zonas y Portal de Líderes _(solo Pro)_

|Funcionalidad|Básica|Pro|
|---|:-:|:-:|
|Zonas hardcoded definidas al inicio del proyecto|✅|❌|
|Sección Settings → Zonas con gestión visual|❌|✅|
|Crear, editar, eliminar zonas desde la interfaz|❌|✅|
|Árbol jerárquico de geografía con checkboxes|❌|✅|
|Composición de zona con suma y resta de regiones|❌|✅|
|Attention box: zonas no asignadas|❌|✅|
|Validación de superposiciones entre zonas|❌|✅|
|Asignación de líder por zona (nombre, email, PIN)|❌|✅|
|Portal de Líderes con link único + PIN|❌|✅|
|Vista del líder con KPIs y tabla de su zona|❌|✅|
|Descarga Excel consolidado o multi-hoja por PLV|❌|✅|

**Descripción del Módulo:** Este módulo, exclusivo de la Versión Pro, convierte la gestión de zonas operativas en una herramienta flexible que se adapta a la realidad cambiante del equipo de campo, y habilita un acceso individual para que cada líder regional gestione su territorio de forma autónoma. Desde Settings → Zonas el admin de Picnic crea, configura y administra las zonas que componen su estructura territorial: cuando un líder se incorpora, se va, o se reorganiza una zona, el admin lo refleja directamente desde la interfaz. El modal de edición de zona presenta un árbol jerárquico de la geografía con checkboxes a cada nivel (provincia → ciudad → barrio), donde marcar un nivel incluye automáticamente todos sus hijos, y desmarcar hijos individuales después de marcar el padre permite construir composiciones complejas como "Buenos Aires excepto Mar del Plata" o "CABA excepto Centro". Antes de guardar, el sistema valida superposiciones con otras zonas existentes y muestra un warning si hay solapamiento, permitiendo confirmar la superposición o ajustar la selección. Un attention box visible en el panel del admin alerta cuando hay locales del período actual en geografías no asignadas a ninguna zona configurada, y abre un modal de asignación masiva para resolverlas. Los cambios en zonas se aplican solo a futuro: las visitas históricas cerradas mantienen su snapshot original (zona, líder y PIN al momento de la visita), garantizando trazabilidad y permitiendo generar reportes pasados con la información correcta de quién era responsable en ese momento. Cada zona configurada tiene asociada un líder regional con nombre, email y PIN de 4 dígitos, y genera automáticamente una URL única (ej. `pop-picnic.com.ar/zonas/costa_atlantica`) que el líder usa para acceder a su Portal. El Portal de Líderes es un dashboard inmediato y simple, sin necesidad de usuario y contraseña: el líder entra desde su URL, ingresa el PIN, y ve los KPIs operativos de su zona en el período actual (total de locales, visitados, pendientes, efectivos, distribución por PLV) junto con la tabla completa de locales asignados, con sort, búsqueda y filtros por PLV, estado y motivo. Puede descargar el listado en Excel consolidado o multi-hoja por PLV para distribuir a sus colocadores, y ve el PIN de su zona en un widget destacado para compartir con su equipo. El líder no ve ID de colocadores, fotos de visitas, GPS, información de otras zonas, ni períodos pasados: solo lo que necesita para operar el período actual.

**Diferencia entre versiones:** En la Versión Básica las zonas operativas se definen al inicio del proyecto y quedan hardcoded en el sistema, no son modificables desde la interfaz, y aparecen únicamente como columna en la tabla del Panel de Gestión Central para ordenar y consultar. El admin no tiene Portal de Líderes ni puede crear accesos individuales: cuando necesita distribuir el trabajo, descarga el Excel filtrado por provincia y lo envía manualmente a sus líderes regionales por afuera del sistema, manteniendo el flujo de coordinación que Picnic tiene hoy con PEYA Trade. La Versión Pro habilita la gestión visual completa de zonas, los líderes regionales con su propio Portal de acceso, y el snapshot histórico de zona-líder-PIN en cada visita para análisis posterior.

---

### Módulo 7 — Panel de Cliente

|Funcionalidad|Básica|Pro|
|---|:-:|:-:|
|Login email + contraseña gestionado por admin|✅|✅|
|Vista solo lectura|✅|✅|
|Selector de período individual (cualquier mes histórico)|✅|✅|
|KPIs core reactivos a filtros aplicados|✅|✅|
|Breakdowns por PLV y por geografía|✅|✅|
|Tabla de locales con sort y búsqueda|✅|✅|
|Filtros simples (provincia + PLV combinables)|✅|✅|
|Detalle de visita (sin ID, sin GPS, sin zona interna)|✅|✅|
|Fotos de cada visita visibles|✅|✅|
|Botón Excel con filtros aplicados|✅|✅|
|Selector de rango de fechas|❌|✅|
|Filtros avanzados combinables|❌|✅|
|Pestañas separadas (Por PLV, Por Geografía, Histórico mensual)|❌|✅|
|Constructor de Reportes propio (campos restringidos)|❌|✅|

**Descripción del Módulo:** El Panel de Cliente es la ventana de transparencia que Picnic le ofrece a Peya sobre el avance de sus campañas. Es de solo lectura: el cliente entra con su login propio (gestionado desde Settings por el admin de Picnic) y accede a una vista similar a la del Panel de Gestión Central pero con los campos operativos internos restringidos. Ve los KPIs del período actual con desglose de motivos de no efectividad, los breakdowns por PLV y por geografía, y la tabla completa de locales con todas las columnas relevantes para su seguimiento: identificador, nombre, dirección, producto, estado, fecha de visita, motivo cuando corresponde. Puede ordenar por cualquier columna, buscar por Grid o nombre, filtrar por provincia y PLV, y exportar a Excel con los filtros aplicados. Tiene acceso al detalle de cada visita con sus fotos antes y después, motivo, comentarios y fecha; las miniaturas se muestran directamente en el modal sin necesidad de abrirlas a pantalla completa. Peya puede consultar cualquier período histórico cargado en POP, navegando libremente entre meses pasados para hacer comparaciones o responder preguntas internas. Lo que el cliente NO ve en ninguna versión: zonas operativas internas de Picnic, identidad de los colocadores (ID), coordenadas GPS de las visitas, ni información sobre líderes regionales o estructura del equipo de campo.

**Diferencia entre versiones:** La Versión Básica le entrega a Peya una herramienta de consulta y descarga moderna con todo lo necesario para hacer seguimiento del estado de cada campaña: KPIs, breakdowns, tabla filtrable, detalle con fotos, y exportación. La Versión Pro amplía sustancialmente la capacidad analítica del cliente sumando el selector de rango de fechas para análisis multi-período, los filtros avanzados combinables sobre todas las dimensiones disponibles (ciudad, barrio, estado, motivo), las tres pestañas adicionales de análisis (Por PLV, Por Geografía con drill-down, Histórico de KPIs por mes pasado), y un Constructor de Reportes propio que le permite a Peya generar sus propios reportes a medida con elección de columnas y agregaciones configurables. El Constructor de Reportes del cliente tiene campos restringidos comparado con el del admin: nunca expone ID, GPS ni zona operativa, incluso si Peya quisiera incluirlos en su reporte. En la práctica, esto significa que con la Versión Pro Peya tiene autonomía analítica completa sobre su campaña sin necesidad de pedirle reportes específicos a Picnic, mientras que con la Básica depende de Picnic para análisis no contemplados en las vistas estándar.

---

### Módulo 8 — App de Campo

|Funcionalidad|Básica|Pro|
|---|:-:|:-:|
|URL pública `/colocador` accesible desde celular|✅|✅|
|PWA instalable en home screen|✅|✅|
|Lista de locales pendientes con búsqueda|✅|✅|
|Toggle Efectiva Sí/No|✅|✅|
|Lógica KB (toggles independientes sticker + saliente)|✅|✅|
|Foto antes obligatoria|✅|✅|
|Foto después obligatoria si efectiva|✅|✅|
|Compresión automática de fotos en el dispositivo|✅|✅|
|Cámara nativa + selección desde galería|✅|✅|
|Motivos precargados desde Settings|✅|✅|
|Comentarios opcionales|✅|✅|
|Datos del establecimiento solo lectura|✅|❌|
|Datos del establecimiento editables|❌|✅|
|Acceso sin autenticación (zona + PLV únicamente)|✅|❌|
|Acceso protegido con PIN de zona|❌|✅|
|ID obligatorio del colocador en cada visita|❌|✅|
|Captura de GPS al guardar la visita|❌|✅|
|Botón "Avisar a mi líder" tras 3er error de PIN|❌|✅|
|Email automático al líder con ID + mensaje opcional|❌|✅|
|Edición de 4 campos del establecimiento + "Confirmar información"|❌|✅|

**Descripción del Módulo:** La App de Campo es la herramienta que usan los colocadores en terreno para cargar el resultado de cada visita en tiempo real. Es una aplicación web optimizada para celular (PWA), accesible desde cualquier dispositivo con navegador moderno y opcionalmente instalable en la home screen como una app nativa (abre en pantalla completa, sin barra de navegador). Reemplaza el flujo actual de cargar planillas, sacar fotos sueltas y consolidar todo después por otros canales. Está pensada para una realidad operativa específica: el colocador trabaja en la calle, con un celular en la mano, posiblemente con mala conectividad, posiblemente bajo el sol. Cada interacción tiene que ser rápida, robusta y a prueba de errores. Después de ingresar, el colocador ve la lista de locales pendientes en su zona y producto, con búsqueda por nombre o Grid. Al tocar cualquier local, se abre el modal de visita con la información del establecimiento (nombre del partner, business name, teléfono con tap-to-call, dirección con tap-to-open en Google Maps). El registro de la visita consta de un toggle Efectiva Sí/No; si es efectiva, toggles de PLV (con lógica especial para Kit Básico: sticker y saliente como toggles independientes para registrar qué pieza se colocó); si es no efectiva, un dropdown de motivo precargado desde Settings; comentarios opcionales; foto antes obligatoria; y foto después obligatoria solo si la visita fue efectiva. Las fotos se toman con la cámara nativa del dispositivo o se seleccionan desde la galería (el colocador elige), y se comprimen automáticamente en el cliente antes de subir: cada foto pasa de aproximadamente 5MB a 250KB, lo que ahorra datos móviles del colocador, acelera la carga sobre conexiones lentas, y reduce el costo de almacenamiento. Si la conexión falla al subir, la app retiene la foto y reintenta automáticamente. Al guardar la visita, los datos quedan inmediatamente disponibles en el Panel de Gestión Central de Picnic, el Portal de Líderes correspondiente y el Panel de Cliente de Peya.

**Diferencia entre versiones:** La diferencia entre ambas versiones de la App de Campo es la más significativa del sistema porque define el modelo operativo de control sobre el trabajo en terreno. En la Versión Básica las visitas son operativamente anónimas: no hay autenticación (cualquiera con la URL accede ingresando solo zona y PLV), no se identifica al colocador (sin ID), no se captura ubicación al guardar (sin GPS), y los datos del establecimiento son solo lectura (si están desactualizados, el colocador no puede corregirlos desde la app y debe avisar al admin por afuera). Esto significa que POP Básica funciona perfectamente para registrar el estado de las campañas pero no para auditar el trabajo individual de los colocadores ni verificar presencia en el local. La Versión Pro convierte la app en una herramienta completa de gestión de equipo de campo: el acceso queda protegido con PIN de zona (el colocador ingresa zona, PLV y PIN en un solo paso, y POP valida que el PIN matchee con la zona seleccionada); cada visita queda asociada al colocador específico que la registró mediante ID obligatorio (validación de 7-8 dígitos, no se prellena entre visitas para forzar identificación consciente); se captura el GPS del dispositivo al guardar para verificación de presencia (con manejo defensivo si el permiso GPS está denegado: la visita se guarda igual con flag "sin GPS" registrado); el colocador puede editar los 4 campos principales del establecimiento (nombre, business name, dirección, teléfono) si encuentra discrepancias con la realidad, presionando obligatoriamente "Confirmar información" antes de guardar para indicar que los datos son correctos con o sin modificaciones; y si el colocador falla 3 veces consecutivas el PIN, aparece un botón "Avisar a mi líder" que envía un email automático al líder regional con el ID del colocador y un mensaje opcional, resolviendo en el momento problemas de coordinación que hoy implican llamadas o esperas. Una vez ingresado correctamente, la sesión queda activa hasta cerrar el navegador. La sincronización offline no está incluida en ninguna de las dos versiones de v1: si el colocador pierde conexión, debe completar la visita en un lugar con señal. Está disponible como extensión futura cotizable aparte.

---

### Módulo 9 — Settings, Reglas Automatizadas y Auditoría

|Funcionalidad|Básica|Pro|
|---|:-:|:-:|
|Settings → PLVs (crear, editar, marcar compuesto)|✅|✅|
|Settings → Motivos (crear, editar, flag "cierra Sí/No")|✅|✅|
|Settings → Usuarios Peya (alta, edición, reset)|✅|✅|
|Settings → Cuenta del admin|✅|✅|
|Cierre directo de visita por motivo|✅|✅|
|Cierre/apertura manual desde modal|✅|✅|
|Cierre automático tras 3 intentos no efectivos (fijo en código)|✅|❌|
|Cierre automático tras N intentos configurable desde Settings|❌|✅|
|Log de cargas|✅|✅|
|Log de ediciones manuales del admin|✅|✅|
|Log de visitas registradas (anónimas)|✅|❌|
|Log de visitas registradas (con ID, zona, PIN, GPS)|❌|✅|
|Búsqueda por palabra clave en el log|✅|✅|
|Filtro por rango de fechas en el log|✅|✅|
|Exportación del log a Excel|✅|✅|
|Settings → Cadenas con detección automática por nombre|❌|✅|
|Settings → Gestión visual de mappings de hojas Partners|❌|✅|
|Filtros avanzados en el log (tipo, usuario, ID, zona)|❌|✅|

**Descripción del Módulo:** Este módulo agrupa tres áreas administrativas del sistema que comparten un mismo principio: el admin de Picnic mantiene el control operativo de POP desde un solo lugar mientras el sistema ejecuta automatizaciones que reducen el trabajo manual. La sección de Settings centraliza toda la configuración parametrizable del sistema, accesible solo para el admin, con sub-secciones para gestionar productos (PLVs con su flag de "producto compuesto" que habilita en la App de Campo los toggles independientes de sticker y saliente para casos como Kit Básico), motivos de no efectividad (con flag "cierra Sí/No" que define el comportamiento automático tras seleccionar ese motivo: cierre directo del local o vuelta a la lista para reintento), usuarios de Peya (alta, edición, reset de contraseña, activación/desactivación), cuenta del admin (cambio de contraseña y gestión de admins adicionales si los hubiera), y reglas de cierre automático. Las reglas de negocio automatizadas funcionan en segundo plano sin requerir intervención del admin: el cierre directo por motivo se activa cuando el colocador marca una visita no efectiva con un motivo que tiene la flag "cierra Sí" (ej. "No existe", "No quiere PLV"), retirando el local de la lista del colocador inmediatamente; el cierre automático tras N intentos no efectivos se activa cuando un local recibe N visitas consecutivas con motivos que "dejan abierto" (ej. "Local cerrado" repetido), evitando reintentos indefinidos; y el cierre o apertura manual del admin desde el modal correspondiente sobrescribe cualquier estado automático cuando es necesario. El Log de Auditoría es el registro cronológico de toda la actividad relevante en POP, accesible exclusivamente desde el panel del admin y no expuesto a líderes ni a Peya. Captura cada carga de locales con detalle (archivo procesado, período asignado, hojas detectadas/ignoradas/procesadas, cantidad de establecimientos importados, usuario admin que realizó la carga, fecha y hora), cada edición manual del admin (qué campo se cambió, valor anterior, valor nuevo), cada cierre o apertura manual, cada cambio en la configuración (PLVs, motivos, reglas, etc.), y cada visita registrada por un colocador. La búsqueda por palabra clave permite encontrar rápidamente eventos relacionados con un Grid, un nombre de local o un archivo cargado; los filtros por rango de fechas permiten acotar al período relevante; y la exportación a Excel permite hacer análisis externos cuando se necesita.

**Diferencia entre versiones:** En Settings, la Versión Pro suma tres sub-secciones que la Básica no tiene: gestión de Cadenas comerciales con detección automática por nombre (el sistema sugiere clasificaciones al detectar patrones como "McDonald's Recoleta", "McDonald's Pacífico" y el admin confirma, edita o agrega antes de aplicarlas, manteniendo control total); gestión visual de mappings recordados de hojas en formato Partners (cuando el admin mapea las columnas de una hoja Partners por primera vez, el sistema lo recuerda y aplica automáticamente la próxima carga, y desde acá puede ver, editar o eliminar mappings); y configuración flexible de las reglas de cierre automático, donde el admin define el número N de intentos desde la interfaz en lugar de tenerlo hardcoded. Adicionalmente, en Pro Settings incluye la sección completa de Zonas descripta en el Módulo 6. En las reglas automatizadas, la diferencia es que la Básica tiene N=3 fijo en código (tras 3 visitas no efectivas consecutivas con motivos que dejan abierto, el local se cierra) mientras que la Pro permite ajustar ese N desde Settings según necesidad operativa. En el Log, la Pro registra información significativamente más rica en cada visita (ID del colocador, zona usada, PIN usado para acceder, GPS de la visita) lo que habilita auditoría nominal completa, captura las ediciones que los colocadores hacen en campo sobre los datos del establecimiento (en Básica el colocador no edita), registra los reportes generados desde el Constructor con su configuración completa para poder repetir o auditar consultas anteriores, y suma filtros avanzados combinables sobre el log (tipo de evento, usuario admin, ID del colocador, zona) con vista detallada de cada entrada y contexto completo. La Versión Básica resuelve trazabilidad operativa básica (qué pasó, cuándo) mientras que la Pro resuelve trazabilidad nominal completa (qué pasó, cuándo, quién, dónde).

---

Con esto cierra la Sección 4 completa. Avisame si querés que aplique todos estos cambios al MD y siga con el resto del documento (secciones 6 a 14: Plan de Trabajo, Inversión, Infraestructura, Mantenimiento, Capacitación, etc.) que también tienen vocabulario para unificar.

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
