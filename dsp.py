# This example uses cppyy to bind to c/cpp, https://cppyy.readthedocs.io/en/latest/
import cppyy
import os

# Import cpp or c below.  It will be compiled when this python module is loaded.

# Add include paths.  No need to add paths to system or STL headers.
cppyy.add_include_path(os.path.abspath('cpp/include'))

# Add all source (c/cpp) files here.
sources = [
    'cpp/generate_features.cpp',
]
for filename in sources:
    with open(filename, 'r') as file:
        source = file.read()
    cppyy.cppdef(source)

# Now, import the symbols from c/cpp that you'll need for training.  Most likely, just the generate_features function.
from cppyy.gbl import generate_features_cpp

# End c/cpp import


def generate_features(implementation_version, draw_graphs, raw_data, axes, sampling_freq, scale_axes):
    # features is a 1D array, reshape so we have a matrix
    raw_data = raw_data.reshape(int(len(raw_data) / len(axes)), len(axes))

    features = []
    graphs = []

    # split out the data from all axes
    for ax in range(0, len(axes)):

        # Input prototype is inferred the cpp source
        # If you use STL types, as in this example, cppyy will automatically convert from many python types
        # But all c/cpp types are supported, including pointers, arrays, and structs
        # Those types may need to be converted manually
        # See https://cppyy.readthedocs.io/en/latest/basic_types.html for examples of other input types
        rms = generate_features_cpp(raw_data[:, ax].tolist())
        features.append(rms)

    return {
        'features': features,
        'graphs': graphs,
        # if you use FFTs then set the used FFT sizes here (this helps with memory optimization on MCUs)
        'fft_used': [],
        'output_config': {
            # type can be 'flat', 'image' or 'spectrogram'
            'type': 'flat',
            'shape': {
                # shape should be { width, height, channels } for image, { width, height } for spectrogram
                'width': len(features)
            }
        }
    }
