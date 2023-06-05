@echo off

echo Ejecutando PDF to txt in folder.py
python "PDF to txt in folder.py"
if %errorlevel% neq 0 (
    echo Error al ejecutar PDF to txt in folder.py
    exit /b
)

echo Ejecutando Preprocesamiento.py
python "Preprocesamiento.py"
if %errorlevel% neq 0 (
    echo Error al ejecutar Preprocesamiento.py
    exit /b
)

echo Ejecutando procesado con pdf to Elastisearch.py
python "TXT to ElasticSearch.py"
if %errorlevel% neq 0 (
    echo Error al ejecutar procesado con pdf to Elastisearch.py
    exit /b
)

echo Todos los scripts se han ejecutado correctamente.
pause