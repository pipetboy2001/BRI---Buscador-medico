# BRI - Buscador médico (Frontend con Vue.js)
Este es el frontend del buscador médico BRI, que utiliza Vue.js como framework de desarrollo.

Antes de comenzar con la configuración del frontend, asegúrate de seguir los siguientes pasos:

- Ejecuta el script de indexación y búsqueda de archivos PDF en el backend. Asegúrate de mantener Elasticsearch abierto para que el frontend pueda interactuar con él correctamente. Consulta el archivo README del [Procesamiento](https://github.com/pipetboy2001/BRI---Buscador-medico/tree/main/Procesamiento) para obtener instrucciones detalladas sobre cómo ejecutar el script y configurar Elasticsearch.
## Requisitos
Node.js (se recomienda la versión LTS)
## Instalación
- Clona o descarga este repositorio.

- Navega hasta el directorio del proyecto.

- Instala las dependencias del proyecto ejecutando el siguiente comando:

```shell
npm install
```

Una vez que hayas completado la instalación y configuración, puedes ejecutar el frontend con el siguiente comando:
```shell
npm run dev
```

## Uso
El frontend del buscador médico BRI ofrece una interfaz web para realizar búsquedas en los archivos PDF indexados en Elasticsearch. Para utilizar el buscador, sigue estos pasos:

- Asegúrate de haber ejecutado el script de indexación y búsqueda de archivos PDF en el backend y de que Elasticsearch esté funcionando correctamente.

- Abre la aplicación en tu navegador web visitando http://localhost:8080.

- Ingresa tu consulta de búsqueda en el campo de búsqueda y presiona Enter o haz clic en el botón de búsqueda.

- Verás los resultados de la búsqueda en la lista de documentos encontrados. Puedes hacer clic en un documento para ver su contenido completo.

¡Disfruta utilizando el buscador médico BRI!

Recuerda que si encuentras algún problema o tienes alguna pregunta, puedes consultar la documentación del proyecto o buscar ayuda en la comunidad en línea.
