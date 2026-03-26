# 🕵️‍♂️ Financial Fraud Detection Engine (Unsupervised ML)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Isolation%20Forest-red.svg)
![Data Viz](https://img.shields.io/badge/Data%20Viz-Seaborn%2FMatplotlib-green.svg)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458.svg)

## 📌 Visión General
Este proyecto es un motor de detección de anomalías diseñado para el sector financiero y bancario. Utiliza **Machine Learning No Supervisado** para auditar masivamente historiales de transacciones e identificar comportamientos fraudulentos sin depender de reglas estáticas o datos previamente etiquetados.

El objetivo de negocio es la mitigación proactiva de riesgos (Risk Management), aislando transacciones atípicas en milisegundos para su bloqueo preventivo antes de que impacten los estados financieros.

## 🚀 Arquitectura del Motor Analítico

* **1. Ingesta y Simulación de Datos:** Generación programática de un *dataset* financiero con ruido estadístico (ruido Gaussiano) para simular 5,000 transacciones legítimas y la inyección oculta de anomalías (1% de contaminación).
* **2. Modelado de Machine Learning (`scikit-learn`):** * Implementación del algoritmo **Isolation Forest**.
  * Análisis multidimensional (Monto de la transacción, Hora de ejecución, Frecuencia de la ubicación) para calcular la distancia de aislamiento de cada punto de datos.
* **3. Clasificación Autónoma:** El modelo asigna predicciones binarias (`1` para comportamiento normal, `-1` para anomalía matemática) sin intervención humana.
* **4. Visualización de Alto Impacto (`seaborn`):** Renderizado de un gráfico de dispersión bidimensional que mapea visualmente la frontera de decisión del algoritmo, permitiendo a los *stakeholders* no técnicos comprender la agrupación de datos legítimos vs. atípicos.

## 🛠️ Stack Tecnológico

* **Lenguaje Core:** Python
* **Machine Learning:** Scikit-Learn
* **Análisis de Datos:** Pandas, NumPy
* **Visualización:** Seaborn, Matplotlib

## 💡 Impacto y Retorno de Inversión (ROI)
Demuestra la capacidad técnica para implementar sistemas de seguridad basados en IA. Esta arquitectura supera a los sistemas basados en reglas tradicionales (ej. "bloquear toda compra mayor a $500"), reduciendo los "falsos positivos" que frustran a los clientes legítimos y detectando fraudes sofisticados basados en el cambio de hábitos transaccionales.
