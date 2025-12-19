# Inflación Alimentos y Energía en Perú (2020-2025)

Análisis exploratorio de la variación mensual del IPC Alimentos y Energía en Lima Metropolitana, utilizando datos oficiales del Banco Central de Reserva del Perú (BCRP).

## Objetivo
Explorar las tendencias de inflación en uno de los rubros más volátiles de la economía peruana, identificar picos mensuales y visualizar la evolución desde 2020 hasta noviembre 2025.

## Dataset
- **Fuente**: BCRP – Serie PN09816PM (Índice de Precios al Consumidor – Alimentos y Energía)
- **Período**: Enero 2000 – Noviembre 2025 (filtrado 2020-2025 para análisis actual)
- **Formato**: CSV oficial descargado desde estadisticas.bcrp.gob.pe

## Tecnologías utilizadas
- Python
- Pandas (limpieza y manipulación de datos)
- Matplotlib & Seaborn (visualizaciones)
- Jupyter Notebook / VS Code

## Insights principales (2020-2025)
- Inflación promedio mensual: ~0.3%
- Mes con mayor inflación: [ej: Agosto 2022 – +1.5%]
- Tendencia general: picos marcados en 2022 por factores externos (guerra Ucrania, precios de combustibles)
- Noviembre 2025: variación mensual de 0.11% (datos preliminares)

## Estructura del repositorio
- `inflation_analysis.csv` → dataset original
- `inflation_analysis.py` → código completo de limpieza y análisis
- `inflacion_mensual_2020_2025.png` → gráfico principal de evolución mensual

## Próximos pasos
- Dashboard interactivo en Power BI
- Comparación con IPC general y otros rubros
