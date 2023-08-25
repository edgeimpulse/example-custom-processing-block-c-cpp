# Custom processing block example (C/CPP)

Note, if you pip install cppyy locally, it will define an environment variable called "HOST" which will conflict with the HOST environment variable you may have used in other custom DSP blocks.  B/c of this, this example just sets the host to 0.0.0.0...see dsp-server.py if you need to change that.

This is an example of a custom processing block, which you can load in the Edge Impulse studio. See the docs: [Building custom processing blocks](https://docs.edgeimpulse.com/docs/custom-blocks).

# Known Issues

There are known issues with cppyy running on some Apple M2 processors (including in a Linux container).  If you see errors when trying to run the example python file here, consider another Python to CPP binding tool like pybind11.
