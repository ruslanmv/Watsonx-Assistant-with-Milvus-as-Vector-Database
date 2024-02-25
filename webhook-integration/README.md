## Building a Watson Assistant with a Simple Webhook: Step-by-Step Guide


This blog post guides you through creating a basic Watson Assistant and integrating a simple pre-message webhook to enhance its functionality. We'll use the provided example of language detection as a reference. 

Prerequisites:

- An IBM Cloud account
- Access to the Watson Assistant platform

## Steps:

1. Create your Watson Assistant:

Go to the Watson Assistant interface on IBM Cloud.
Click "Create assistant" and choose a name for your assistant.
Select "English" as the language model.
Click "Create".
2. Define your dialog:

In the "Dialog" tab, add a new "Node".
Choose "Welcome" as the node type and define a welcome message.
Add another "Node" and choose "Action". Name it "Check language".
In the "Action" node settings, select "Webhook" as the action type.


1. Create a Watson Assistant Skill
Navigate to the Watson Assistant service on IBM Cloud.
Click on "Create skill" and choose a name for your skill.
Select "Dialog" as the skill type.

2. Define a Simple Action
In the skill builder, click on "Actions" and then "Create action."
and give your action a name, like "check_language."


3. Integrate the Webhook
This part depends on your chosen webhook implementation. Let's assume you're using IBM Cloud Functions with the provided Node.js code example:

Create a new Cloud Function on IBM Cloud.
Choose Node.js as the runtime and paste the example code into the editor.
Update the placeholders with your actual API key and service URL for the Language Translator service.
Deploy the function and note the function URL, which will be the webhook endpoint.

3. Configure the webhook:

Click "Configure webhook".
Enter the following details:
URL: Replace with the actual URL of your webhook endpoint 
(e.g., https://us-south.functions.appdomain.cloud/api/v1/web/e97d2516-5ce4-4fd9-9d05-acc3dd8ennn/default/check_language).

Secret: Set a secret key if required by your webhook .
Header name: Leave as "Content-Type".
Header value: Set to "application/json".
Click "Save".


4. Call the Webhook from your Dialog
In your assistant's dialog, create a node where you want to call the webhook.
 This could be a specific intent or a general node.
Click on the node and choose "Call action."
Select the "check_language" action you created earlier.
5. Test and Analyze
Train your assistant and test it out by sending text input.
Go to the "Analyze" section and examine the conversation logs. You should see the webhook's response and the appended language information.
Bonus Tip: For more control over the webhook response, you can modify the response object in the Node.js code. You can access the user input, context, and other data from the params object and build a customized response.

Conclusion
This guide provides a basic example of creating a Watson Assistant with a webhook. Remember to adapt the steps and code to your specific needs and chosen webhook implementation. For more complex scenarios, refer to the extensive Watson Assistant documentation for advanced features and best practices.