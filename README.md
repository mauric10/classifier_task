Simply run the following to run the classifier and produce an output with the predicted category. 
` python classifier.py "some financial question?"`

In order to run the tests you will need to install the package to your local environment. This should probably be done in a virtualenv as shown below:
`virtualenv classifier`

And from inside the new environment inside the classifier_task directory:
`pip install -e .`
`pip install -r requirments.txt`
`py.test`

