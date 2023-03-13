

import numpy as np          # emulate training data
import tensorflow as tf     # to retreive optimizer

from tensorflow.keras.models import Model           # model class that can be trained
from tensorflow.keras.layers import Input, Dense    # model layer classes


 


 













































'''
Create an Neural Network made of Dense layers. With
an auto-encoder architecture.
    - inputs_shape: defines the number of inputs
'''
def create_model(input_shape):
    # define input layer
    input_layer = Input(shape=input_shape, name='input_layer')

    # hidden layers - encoder
    nn = Dense(64, activation='relu')(input_layer)
    nn = Dense(32, activation='relu')(nn)

    # hidden layers - latent space
    nn = Dense(16, activation='relu')(nn)

    # hidden layers - decoder
    nn = Dense(32, activation='relu')(nn)
    nn = Dense(64, activation='relu')(nn)

    # define output layer
    output_layer = Dense(64, activation='linear')(nn)

    # define model
    model = Model(inputs=[input_layer], outputs=[output_layer])

    return model

















if __name__ == '__main__':

    # create the model
    model = create_model([64])

    # build the model and its learning strategy
    model.compile(
        optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
        loss='mse',
        metrics=['accuracy']
    )

    # create some example inputs and expected outputs
    x_train = np.asarray([tf.ones((64,)) for _ in range(80)])
    y_train = np.asarray([tf.ones((64,)) for _ in range(80)])

    # show model in output
    model.summary()

    # start training and specify training parameters
    model.fit(x_train, y_train, batch_size=8, epochs=100, shuffle=True)

    print('done...')





