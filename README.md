# FastAPI OTEL Instrumentation

API escrita em Python utilizando FastAPI, com o objetivo de gerar métricas e profiling para testar o Grafana Pyroscope.

## Requisitos
- **Sistema operacional** 
  - Linux 
  - MacOS
- **Python** >= 3.12

## Instalação

Para instalar todas as dependências, basta executar o seguinte comando:

```bash
pip install -r requirements.txt
```

## Inicializar Aplicação

Para inicializar a aplicação, basta executar o comando abaixo:

``` bash
opentelemetry-instrument --traces_exporter console,otlp --metrics_exporter console,otlp --logs_exporter console,otlp --service_name pyotl-demo --exporter_otlp_endpoint http://localhost:4317 opentelemetry-instrument uvicorn src.main:app --host 0.0.0.0 --port 5000
```