# Entorno de emulacion retro-gym
import retro
# Para tranformación y reescalado de imagen
import cv2
# Transformaciones sobre frames como matrices
import numpy as np
# Utilizado para dumpear variables
import pickle
# Libreria de red neuronal
import neat
# Animacion con botones presionados
import mando

# Entorno de emulación
env = retro.make(game='CircusCharlie-Nes',state='CircusCharlie.level2.1live',record=True)

# Obtiene el ancho y alto que tendra cada frame
width,height,_ = env.observation_space.shape
# Reduce el ancho y alto obtenidos en una octava parte
width = int(width/8)
height = int(height/8)

def frame_to_array(ob):
    # Redimensiona el frame a una octava parte del mismo
    ob = cv2.resize(ob,(width,height))
    # Transforma el frame a escala de grises
    # El color no es importante solo significa más ruido para analizar
    ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
    # Transforma el frame cv2 a matriz numpy
    ob = np.reshape(ob,(width,height))
    # Transforma frame de una matriz bidimensional a un arreglo unidimensional
    return ob.flatten()

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        # Primer frame
        ob = env.reset()
        # Inicializa la red neuronal
        net = neat.nn.RecurrentNetwork.create(genome,config)
        # Mayor puntaje obtenido para la generación actual
        current_max_score = 0
        # Puntaje obtenido por el genome actual
        current_score = 0
        # Contador de la cantidad de movimientos
        # realizados por el gnome con mayor puntaje
        counter = 0
        # Valor de estado actual, indica si la partida acaba
        done = False
        # Mientras la partida no acabe
        while not done:
            #env.render()
            # Transforma el frame anterior a un arreglo unidimensional
            oned_image = frame_to_array(ob)
            # Recibe el output desde la red neuronal a partir del frame entregado
            neuralnet_output = net.activate(oned_image)
            # Movimiento de salida redondeado a su valor entero mas proximo 0 o 1.
            neuralnet_output = [round(button,0) for button in neuralnet_output]
            # Ejecuta acción obtenida anteriormente
            # Obteniendo un nuevo frame ob
            # un nuevo reward dependiendo del movimiento realizado
            # y un nuevo indicador de done para saber el estado de Charlie
            ob, rew, done, _info = env.step(neuralnet_output)

            # Añade el reward obtenido al punaje del genome actual
            current_score += rew
            # Si el puntaje obtenido por el genome actual
            # es mayor que el maximo de toda la generación
            if current_score>current_max_score:
                # El puntaje obtenido pasa a ser el nuevo maximo
                current_max_score = current_score
                # Reinicia el contador de pasos para llegar a este
                counter = 0
            # De no cumplirse
            else:
                # Suma al contador de pasos hasta llegar a este
                counter+=1

            # Si la partida acaba (mono colisiona con Charlie)
            if done:
                # Marca la partida como terminada
                done = True 
                # Despliega el numero del genome con su puntaje obtenido
                print(genome_id,current_score)

            # Actualiza el puntaje del genoma por cada iteración de este
            genome.fitness = current_score

if __name__ == "__main__":

    # Inicializa la configuración de la red neuronal y las caracteristicas de los genomas
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,'config-feedforward')

    p = neat.Population(config)
    
    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.StatisticsReporter())
    # Guardar cada 10 frames
    p.add_reporter(neat.Checkpointer(10))

    winner = p.run(eval_genomes)

    with open('winner.pkl', 'wb') as output:
        pickle.dump(winner, output, 1)