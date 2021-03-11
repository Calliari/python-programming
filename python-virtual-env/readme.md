# Create a local python environment
`python3.7 -m venv ~/database-pg`

# Acvate the env
`source database-pg/bin/activate`

# Deacvate the env
`deactivate`
or
`database-pg/bin/deactivate` 

# Install what is needed/wanted on this env
`pip install psycopg2`

# Getting what is running on the env 
`pip freeze > requirements.txt`

# Uninstall a pip module
`pip uninstall psycopg2 -y`

# Install a module from another env use the requirement.txt file
`pip install -r requirements.txt`

# Unnstall modules using requirement.txt file
`pip uninstall -r requirements.txt -y`

