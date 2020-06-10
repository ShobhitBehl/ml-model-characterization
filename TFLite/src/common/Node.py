# Node module to store operator attributes
class Node:
    def __init__(self, label, value = None):

        self.label = label
        self.value = value

        self.operator_type = label

        # Following attributes are extracted from weights of CONV2D
        self.kernel_height = None
        self.kernel_width = None
        self.input_channels = None
        self.output_channels = None

        # For semantic meaning for the follwing attributes, refer to the options of operators in
        # https://www.tensorflow.org/lite/guide/ops_compatibility#unsupported_operations

        self.padding = None
        self.activation_function = None
        self.stride_h = None
        self.stride_w = None
        self.dilation_h_factor = None
        self.dilation_w_factor = None
        self.depth_multiplier = None
        self.num_channels = None
        self.lsh_projection_type = None

        # Filter size for Pool2D
        self.filter_width = None
        self.filter_height = None

        self.asymmetric_quantize_inputs = None
        self.weights_format = None
        self.keep_num_dims = None
        self.axis = None
        self.lstm_kernel_type = None
        self.ngram_size = None
        self.max_skip_size = None
        self.include_all_ngrams = None
        self.combiner = None
        self.num_splits = None

        # For Cast Operator, input and output tensor types
        self.in_data_type = None
        self.out_data_type = None

        self.merge_outputs = None
        self.mirror_pad_mode = None

    # Helper function to convert all attributes to a string except value
    def serialize(self):
        ret_str = ""
        attrs = vars(self)
        for item in attrs.items():
            if item[0] != 'value':
                ret_str += str(item[1]) + " "

        return ret_str