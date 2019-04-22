import tensorflow as tf
from tensorflow.keras.callbacks import CSVLogger
import os


class BPNNKeras:
    def __init__(self, layer_sizes, train, test, log_info):
        # dimensions of layers
        self._input_size = layer_sizes[0]
        self._hidden_size = layer_sizes[1]
        self._output_size = layer_sizes[2]

        # data
        self._x_train = train[0]
        self._y_train = train[1]
        self._x_test = test[0]
        self._y_test = test[1]

        # model
        self._model = None

        # log
        self._log_loc = log_info[0]
        self._log_suffix = log_info[1]
        self._csv_logger = CSVLogger(os.path.join(self._log_loc, 'model-' + self._log_suffix + '.csv'), append=False,
                                     separator=";")
        self._scores = None

    def prepare_net(self):
        self._model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(self._hidden_size, activation=tf.nn.relu, input_shape=(self._input_size,)),
            tf.keras.layers.Dense(self._output_size, activation=tf.nn.sigmoid)
        ])
        self._model.compile(optimizer='adam',
                            loss='binary_crossentropy',
                            metrics=['accuracy'])

    def run(self):
        self._model.fit(self._x_train, self._y_train, epochs=10, callbacks=[self._csv_logger])
        self._scores = self._model.evaluate(self._x_test, self._y_test)
        self.log()

    def log(self):
        with open(os.path.join(self._log_loc, 'evaluations-' + self._log_suffix + '.txt'), 'w') as _file:
            _file.write("%s\n%s" % (str(self._model.metrics_names), str(self._scores)))

# TODO: evaluate AOC and ROC.
