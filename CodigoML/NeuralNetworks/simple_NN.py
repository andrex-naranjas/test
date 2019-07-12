#Programa para usar rapidamente Neural Networks
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from display_data import display_data


input_layer_size = 400  # 20x20 Imagenes de entrada
hidden_layer_size = 25  # 25 unidades escondidas
num_labels = 10         # 10 etiquetas del 1 al 10

mat_data = sio.loadmat('data/numeros_escritos.mat')
X = mat_data['X']
y = mat_data['y'].ravel()
m, n = X.shape


rand_indices = np.random.permutation(m)
sel = X[rand_indices[0:100], :]
plt.figure()
display_data(sel, padding=1)
plt.savefig('numeros_random.png')

#Cargar los parametros entrenados de neural network
mat_param = sio.loadmat('data/trained_NN.mat')
Theta_1 = mat_param['Theta1']
Theta_2 = mat_param['Theta2']


#La funcion predict() predice la etiqueta de un unput dada una neural network entrenada
def predict(Theta_1, Theta_2, X):
    """
    Predict the label of an input given a trained neural network.

    Parameters
    ----------
    Theta_1 : ndarray
        Trained weights of layer 1 of the neural network.
    Theta_2 : ndarray
        Trained weights of layer 2 of the neural network.
    X : ndarray, shape (n_samples, n_features)
        Samples, where n_samples is the number of samples and n_features is the number of features.

    Returns
    -------
    p : ndarray, shape (n_samples,)
         The prediction for x.
    """

    m, n = X.shape
    X = np.hstack((np.ones((m, 1)), X))
    A_1 = sigmoid(X.dot(Theta_1.T))
    A_1 = np.hstack((np.ones((m, 1)), A_1))
    A_2 = sigmoid(A_1.dot(Theta_2.T))

    p = np.argmax(A_2, axis=1)
    p += 1  # The theta_1 and theta_2 are loaded from Matlab data, in which the matrix index starts from 1.

    return p



def sigmoid(z):
    g = 1 / (1 + np.exp(-z))
    return g

#Calcular la precision
pred = predict(Theta_1, Theta_2, X)
print('Precision de los datos training :', np.mean(pred == y) * 100)



rp = np.random.permutation(m)
for i in range(5):
    display_data(X[rp[i],].reshape(1, n))    
    pred = predict(Theta_1, Theta_2, X[rp[i],].reshape(1, n))
    print ('Prediccion del Neural Network: {0} (digit {1})'.format(pred, pred % 10))
    plt.savefig('numero_'+str(pred)+'.png')
