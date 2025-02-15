# Custom processing block example (C/CPP)

Note, if you pip install cppyy locally, it will define an environment variable called "HOST" which will conflict with the HOST environment variable you may have used in other custom DSP blocks.  B/c of this, this example just sets the host to 0.0.0.0...see dsp-server.py if you need to change that.

This is an example of a custom processing block, which you can load in the Edge Impulse studio. See the docs: [Building custom processing blocks](https://docs.edgeimpulse.com/docs/custom-blocks).

## Troubleshooting

### ERROR in cling
If you get the following error:
```
(Re-)building pre-compiled headers (options: -O2); this may take a minute ...
ERROR in cling::CIFactory::createCI(): cannot extract standard library include paths!
Invoking:
  LC_ALL=C clang-14  -O2 -DNDEBUG -xc++ -E -v /dev/null 2>&1 | sed -n -e '/^.*include/,${' -e '/^ \/.*++/p' -e '}'
```

Create a symlink for clang-14
```
cd $(dirname $(which clang))
ln -s clang clang-14
```

### error: the clang compiler does not support '-march=native'
This may occur if you host the Dockerfile on Apple silicon. (note, shouldn't happen if you push to Studio)
If you see this, add this environment variable to your Dockerfile or call to dsp-server.py
```
EXTRA_CLING_ARGS=''
```

You can also try this for better performance
```
EXTRA_CLING_ARGS='-O2'
```
