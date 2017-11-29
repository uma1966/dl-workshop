#!/bin/bash

#
# This file will launch Jupyter notebook server with openssl certificates
# which might have been created through helper script init.sh. It is meant
# to be called in /etc/rc.local for automatic launch of Jupyter server on
# system startup.
#
# Your Jupyter notebook server will be accessible at:
#  https://YourEC2IP:8888
#

export PATH="$PATH:/usr/local/cuda/bin:/home/ubuntu/anaconda2/bin"
jupyter notebook --certfile=~/certs/mycert.pem --keyfile=~/certs/mycert.key --notebook-dir=/home/ubuntu/work/dl-workshop > /tmp/ipynb.out 2>&1 &
