"""boomerang.py

Usage:
  boomerang.py <archivo> --inicio=<inicio> --fin=<fin> [--resize=<resize>]

Options:
  -h --help     Show this screen.
"""

from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

def boomerang(archivo, inicio, fin, resize=None):
    v= VideoFileClip(archivo)    #carga el arcivo de video como un objeto de moviepy   
    v2= v.subclip(inicio, fin)   #recorta la porcion que intereza                                            
    v3= v2.fx(vfx.time_mirror)   #hace una version "reversa" de v2
    v4= concatenate_videoclips([v2,v3]) #concatena v1 y v2

    if resize:
        v4 = v4.resize(resize)
    
    gif = archivo[0:-4] + '.gif' #crea el nombre de archivo de salida
    print('guardando ' + gif)
    v4.write_gif(gif)  #guarda el archivo resultante como gif


if __name__ == '__main__':
    from docopt import docopt
    argumentos = docopt(__doc__)
    archivo = argumentos['<archivo>']
    inicio = float(argumentos['--inicio'])
    fin = float(argumentos['--fin'])
    resize = float(argumentos['--resize'])
    print (boomerang(archivo, inicio, fin, resize))
