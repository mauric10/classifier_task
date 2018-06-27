This code was tested with python 2.7.9 on Ubuntu and works if the packages listed in requirements.txt are installed: 

If you have the required packages already installed on the host machine, simply run the following to run the classifier and produce an output with the predicted category. 

`python classifier.py "some financial question?"`

If that does not work, use virtualenv to create a virtual environment with python 2.7.9 installed:

`virtualenv --python=/usr/local/bin/python classifier`

Of course, use the location to the location of python 2.7.9 on your host machine.

You will need to install BLAS and the Fortran compiler to get scipy to install for this version of python. 

`sudo apt-get install libblas3 liblapack3 liblapack-dev libblas-dev`

`sudo apt-get install gfortran`

`pip install -r requirments.txt`

In order to run the tests you will need to install the package to your local environment. This too should probably be done in a virtualenv as shown above and here again:

`virtualenv --python=/usr/local/bin/python classifier`

From inside the virtual environment and inside the classifier_task directory, run:

`pip install -e .`

And finally to run the tests:

`py.test`

If all else fails, a docker container is inlcuded with known working code for python 2.7.13.

`docker-compose up -d`

When it finished  building and the container is running:

`docker exec $(docker ps -qf name='classifier') python classifier.py "i need to pay my bills..."`
