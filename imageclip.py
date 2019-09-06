"""imageclip.py

Usage:
   imageclip.py  --nombre_extension=<nombre_extension> --duracion=<duracion> 

Options:
  -h --help     Show this screen

"""

from pathlib import Path  #trabajamos con archivos y directorios                                             
from moviepy.editor import *                                            


def slides(duracion, nombre_extension):
    directorio = Path('.')  #nos paramos en la carpeta donde creamos la carpeta .mp4
    clips = [] #creamos la lista vacia
                                                         
   
    for archivo in directorio.iterdir(): 
        if archivo.is_file() and archivo.name.endswith(('.jpg','.png','.jpeg')): #verificamos que sean archivos de imagenes
           archivo = str(archivo) #la ruta para hacer string
           clip = ImageClip(archivo, duration=duracion) #le damos la duracion y las imagenes para el video que vamos a crear
           clips.append(clip) #adjunta las imagenes
    img=concatenate_videoclips(clips) #concatena el clips
    clip=nombre_extension #definimos lo que va ser (nombre_extension)
    img.write_videofile(clip, fps=15) #guardamos la imagenes como video life

if __name__ == '__main__':
    from docopt import docopt
    argumentos = docopt(__doc__)    
    nombre_extension = argumentos['--nombre_extension']
    duracion = float(argumentos['--duracion'])
    slides(duracion, nombre_extension)
                            
