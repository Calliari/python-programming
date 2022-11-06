### One way of working with python environments
#### Use/install an modern virtual env with pip
`pip3.7 install --user pipenv`

#### Create a project dir 
`mkdir database-proj; cd database-proj`

#### Create the pipenv env
`pipenv --python python3.7`
A 'Pipfile' will be created with details about the project

#### Activate the env 
`pipenv shell`

#### Install modules (the modules will be save in the Pipfile - good to recreate the env later if need)
`pipenv install psycopg2`

#### Deactivate the pipenv type - 'exit' or the old way 'deactivate'

#### Install the packages based on the Pipfile
`pipenv install`

<hr>
### Another  way of working with python environments
#### Create a project dir 
`mkdir database-proj; cd database-proj`

#### Use/install an modern virtual env with pip
`pip3 install -U virtualenv`

#### Create the pipenv env
`virtualenv database-proj`

#### Activate the env 
`source database-proj/bin/activate`

#### Install modules (the modules will be save in the Pipfile - good to recreate the env later if need)
`virtualenv install psycopg2`

#### Deactivate the pipenv type - 'exit' or the old way 'deactivate'

#### Install the packages based on the Pipfile
`virtualenv install`





