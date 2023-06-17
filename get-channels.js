// En la página de suscripciones de YouTube, ejecuta el siguiente código en la consola del navegador:

// Obtener todos los enlaces de canales
const channelLinks = document.querySelectorAll('a.yt-uix-tile-link');

// Crear un array para almacenar los nombres y enlaces de los canales
const channels = [];

// Iterar sobre los enlaces y extraer los nombres y enlaces de los canales
channelLinks.forEach((link) => {
  const name = link.innerText.trim();
  const href = link.href;
  channels.push({ name, href });
});

// Generar el contenido del archivo de texto
let fileContent = '';
channels.forEach((channel) => {
  fileContent += `${channel.name}: ${channel.href}\n`;
});

// Crear un enlace de descarga para el archivo de texto
const fileBlob = new Blob([fileContent], { type: 'text/plain' });
const fileURL = URL.createObjectURL(fileBlob);
const link = document.createElement('a');
link.href = fileURL;
link.download = 'lista_canales.txt';
link.click();