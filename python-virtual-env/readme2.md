### Use an modern virtual env with pip
`pip3.7 install --user pipenv`

### Create a project dir 
`mkdir database-proj`; `cd database-proj`

### Create the pipenv env
`pipenv --python python3.7`
A 'Pipfile' will be created with details about the project

### Activate the env 
`pipenv shell`

### Install modules (the modiles will be save in the Pipfile - good to recreate the env )
`pipenv install psycopg2`

### Deactivate the pipenv type - 'exit' or the old way 'deactivate'

### Install the packages based on the Pipfile
`pipenv install`


