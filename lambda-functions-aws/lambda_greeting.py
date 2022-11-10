
### Open the AWS lambda console, create a function from "scratch" paste the code into the "lambda_function.py" file on the "Code source" where the folder "greeting".
# Function Name: greeting
# Execution role: Create a new role with basic Lambda permissions
# Press the "Create: button
    
def lambda_handler(event, context):
      greeting = 'I am a DevOps Pro and my name is {} {}'.format(event['firstname'], event['lastname'])
      print(greeting)
      print(event)
      print(context)
      return {
        'message return': greeting
    }


### To test this simple lambda function, press "Test" button and "Configure test event" with: 
## Event JSON
# {
#   "firstname": "Bob",
#   "lastname": "Smith"
# }
