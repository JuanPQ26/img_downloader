import os
import csv
import shutil
import requests
from rich.console import Console
from rich.progress import track

if __name__ == '__main__':
    console = Console()
    
    try:

        console.print("¡Bienvenido al descargador de imágenes!\n", style="bold ")
        console.print("Para comenzar, por favor ingrese la ruta del archivo CSV que contiene las URLs de las imágenes a descargar. Por ejemplo: C:\\imagenes\\urls.csv\n")

        file_path = input("Ruta del archivo CSV: ")

        console.print("\nAhora ingrese la ruta de la carpeta donde desea guardar las imágenes descargadas.")
        console.print("Por ejemplo: C:\\imagenes\\descargas ")
        console.print("(La carpeta sera creada si no existe).\n")

        destination_path = input("Ruta de la carpeta de destino: ")

        console.print("\nPerfecto, vamos a comenzar con la descarga de las imágenes especificadas en el archivo CSV.")
        console.print("Esto puede tomar algunos minutos dependiendo de la cantidad de imágenes.")
        console.print("Por favor espere, se mostrará el progreso a medida que se descargan. \n")

        data = []
        with open(file_path) as f:
            f_reader = csv.DictReader(f)
            for line in f_reader:
                data.append(line)

        data_len = len(data)

        not_downloaded = 0

        for i in track(range(data_len), description="Descargando"):
            print(data[i])
            image_name = os.path.basename(data[i]['image_url'])
            destination_file = os.path.join(destination_path, image_name)

            response = requests.get(data[i]['image_url'], stream=True)

            with open(destination_file, 'wb') as image_file:
                shutil.copyfileobj(response.raw, image_file)

        console.print("\n¡Descarga completada!\n", style="bold green")
        console.print(f"Se han descargado y guardado todas las imágenes exitosamente en la carpeta '{destination_path}'.\n")
        console.print("Resumen:")
        console.print("- Total de imágenes: ", style="bold", end="")
        console.print(f"{data_len}")
        console.print("- Imágenes descargadas: ", style="bold green", end="")
        console.print(f"{data_len - not_downloaded}")
        console.print("- Imágenes fallidas: ", style="bold red", end="")
        console.print(f"{not_downloaded}\n")
        console.print("Muchas gracias por utilizar nuestro programa de descarga de imágenes.")
        console.print("Que tenga un excelente día.\n")

        input("Presione Enter para salir.") 
    except Exception:
        console.print_exception(show_locals=True)