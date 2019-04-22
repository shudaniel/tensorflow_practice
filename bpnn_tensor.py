import tensorflow as tf


class BPNNTensor:
    def __init__(self, layer_sizes, train, test):
        # dimensions of layers
        self._input_size = layer_sizes[0]
        self._hidden_size = layer_sizes[1]
        self._output_size = layer_sizes[2]

        # data
        self._x_train = train[0]
        self._y_train = train[1]
        self._x_test = test[0]
        self._y_test = test[1]

        # Optimisation variables
        self._learning_rate = 0.5
        self._epochs = 10
        self._batch_size = 100

        self._init_op = None
        self._cross_entropy = None
        self._optimiser = None
        self._accuracy = None
        self._x = None
        self._y = None

    def prepare_net(self):
        # declare the training data placeholders
        self._x = tf.placeholder(tf.float32, [None, self._input_size])
        # the output data placeholder
        self._y = tf.placeholder(tf.float32, [None, self._output_size])

        # declare the weights connecting the input to the hidden layer
        W1 = tf.Variable(tf.random_normal([self._input_size, self._hidden_size], stddev=0.03), name='W1')
        b1 = tf.Variable(tf.random_normal([self._hidden_size]), name='b1')
        # the weights connecting the hidden layer to the output layer
        W2 = tf.Variable(tf.random_normal([self._hidden_size, self._output_size], stddev=0.03), name='W2')
        b2 = tf.Variable(tf.random_normal([self._output_size]), name='b2')

        # calculate the output of the hidden layer
        hidden_out = tf.add(tf.matmul(self._x, W1), b1)
        hidden_out = tf.nn.relu(hidden_out)

        # calculate the hidden layer output
        # output layer
        y_ = tf.nn.sigmoid(tf.add(tf.matmul(hidden_out, W2), b2))

        # This is to make sure that we never get a case were we have a log(0) operation occurring during training
        y_clipped = tf.clip_by_value(y_, 1e-10, 0.9999999)

        # Loss/Cost function
        self._cross_entropy = -tf.reduce_mean(
            tf.reduce_sum(self._y * tf.log(y_clipped) + (1 - self._y) * tf.log(1 - y_clipped), axis=1))

        # add an optimiser
        self._optimiser = tf.train.GradientDescentOptimizer(
            learning_rate=self._learning_rate).minimize(self._cross_entropy)

        # setup the initialisation operator
        self._init_op = tf.global_variables_initializer()

        # define an accuracy assessment operation
        correct_prediction = tf.equal(tf.argmax(self._y, 1), tf.argmax(y_, 1))
        self._accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    def run(self):
        # start the session
        with tf.Session() as sess:
            # initialise the variables
            sess.run(self._init_op)
            for epoch in range(self._epochs):
                _, c = sess.run([self._optimiser, self._cross_entropy],
                                feed_dict={self._x: self._x_train, self._y: self._y_train})
                print("Epoch:", (epoch + 1), "cost =", "{:.3f}".format(c))
            print(sess.run(self._accuracy, feed_dict={self._x: self._x_test, self._y: self._y_test}))
