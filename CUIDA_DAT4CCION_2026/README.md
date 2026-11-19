# CUIDA — DAT4CCIÓN 2026

Dashboard nacional de México: tiempo, demanda, recepción de cuidados, uso de servicios, calidad deseada y bienestar. Datos seleccionados de INEGI ENUT 2024, ENASIC 2022 y CSTNRHM 2024.

## Ejecutar
Abra `dist/index.html` en un navegador moderno. No requiere instalación, conexión, API, claves ni servidor. Los enlaces de fuentes requieren conexión. Alternativa: `python -m http.server 8000 --directory dist`.

## Contenido
- `dist/index.html`: aplicación autónoma, con CSS, JavaScript y datos integrados.
- `dist/datos.csv` y `dist/datos.json`: 40 observaciones y metadatos.
- `build_dashboard.py`: generador, Python 3 sin dependencias externas.
- `validate.py`: comprobaciones de integridad y cálculos.

Para reconstruir: `python build_dashboard.py`. El generador escribe `dist` junto al script. Ejecutar `python validate.py` para verificar integridad y cálculos.

## Métodos
Brecha = mujeres menos hombres. Razón = horas de mujeres / hombres. Nunca sumar promedios con distintos participantes. Tasas de asistencia no equivalen a capacidad ni a cobertura de demanda efectiva. Preferencias de calidad no son inspecciones. Los datos no permiten priorización municipal ni inferencia causal.

Escenario: N × horas × utilización × sustitución = tiempo potencial liberado. Costo = N × horas × costo supuesto. Parámetros ilustrativos, no estimaciones oficiales. El resultado no garantiza impacto.

## Replicar
1. Identificar encuesta nacional y universo equivalente.
2. Agregar filas con fuente, año, sexo, unidad, universo y localizador.
3. No mezclar fechas ni denominadores para calcular brechas.
4. Adaptar marco normativo y validar servicios con actores locales.
5. Ejecutar comprobaciones, revisar filtros y exportaciones.
6. Documentar fecha, cambios, faltantes e incertidumbre antes de distribuir.

## Herramientas y atribución
HTML, CSS, JavaScript y Python. Asistencia de ChatGPT en programación y redacción. Cifras de INEGI; contexto normativo de TEPJF. CUIDA no es un producto oficial de ONU Mujeres ni de INEGI. Se conservan las fuentes y atribución; no se añaden restricciones a los datos oficiales.

## Pruebas realizadas
Navegación, cambio de actividad, orden por brecha, filtro textual y descarga CSV en navegador. Escenario de 100 personas = 336 horas/semana; al cambiar a 200 = 672. Revisión de gráficos y texto. Sin auditoría formal WCAG ni prueba con usuarios reales.
