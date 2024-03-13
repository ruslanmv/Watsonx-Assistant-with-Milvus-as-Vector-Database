
![](assets/2024-03-13-10-30-20.png)

## Creating a Watson Assistant with a Custom Extension (MedicX)



This tutorial guides you through creating a Watson assistant that utilizes a custom extension (MedicX) to interact with an external API. We'll achieve this without dialog skills or webhooks, focusing on modern actions and extension calls.

### Prerequisites:

* An IBM Cloud account with access to Watson Assistant service
* Basic understanding of Watson Assistant and creating actions

### Steps:

1. **Create a New Watson Assistant:**
    * Log in to your IBM Cloud account and access the Watson Assistant service.
    * Click on "Create assistant" and provide a name and description for your assistant.
     ![](assets/2024-03-11-18-54-49.png)
     
    * Click "Create" to initiate the assistant creation.
     ![](assets/2024-03-11-18-56-03.png)
2. **Build the Custom Extension:**
    * Navigate to the "Integrations" tab within your newly created assistant.
    * Click on "Build custom extension."
     ![](assets/2024-03-11-19-00-33.png)
    * In the "Basic information" section, provide a name and description for your custom extension (e.g., MedicX Extension).
     ![](assets/2024-03-11-19-01-23.png)
    * Click "Next" to proceed to the "Import OpenAPI" step.
    * In this step, you'll import the OpenAPI document (openapi.json) that describes the MedicX API. You can typically find this file on the MedicX developer portal or documentation. Click "Browse" and select the `code-engine/openapi.json` file (replace with the actual location of your file)
    ![](assets/2024-03-11-19-04-10.png)
    * Click "Next" to review the imported operations. This allows you to verify that the extension can interact with the MedicX API endpoints as defined in the OpenAPI document.
    * If everything looks good, click "Finish" to create the custom extension.
    ![](assets/2024-03-11-19-05-24.png)

3. **Add the Custom Extension to Your Assistant:**
    * On the "Extensions" dashboard, locate your newly created MedicX extension.
    ![](assets/2024-03-11-19-07-16.png)
    * Click the extension tile and then click "Add" to integrate it with your assistant.
     ![](assets/2024-03-11-19-07-46.png)
    * Follow the on-screen prompts to complete the integration process.
      ![](assets/2024-03-11-19-10-23.png)   
4. **Create an Action:**
    * Navigate to the "Actions" tab within your assistant.
    * Click on "Create action" and provide a name and description for your action (e.g., Process Medical Query).
    
    ![](assets/2024-03-11-19-12-25.png)
    * This action will handle user queries and interact with the MedicX API through the custom extension.
    ![](assets/2024-03-12-10-21-43.png)


    5. **Define Action Variables:**
    * In the action editor, create a new assistant variable to store the user's input message. 

    We create the first step, we can say

    ```
    Please enter in your question
    ```
    ![](assets/2024-03-12-17-23-04.png)


    and then we define a custemer response like Free text
    ![](assets/2024-03-12-17-23-58.png)


6. **Call the MedicX API:**


    We create an extra step, the step we name

    `Call custom extension`


  
    * Within continue to next step, you'll use the `Use extension` node to invoke the desired MedicX API endpoint.
    * In the "Extension" dropdown, choose your custom extension (MedicX Extension).
    ![](assets/2024-03-12-17-26-24.png)

    * Select the specific operation you want to call from the MedicX API (e.g., send a message and receive a response).

    * Update the optional parameters as needed.  
    * **Message:** This parameter should be set to the user's input retrieved
    * **History:** (Optional) This parameter might be used by the MedicX API to maintain conversation context. You can leave it blank or populate it based on your specific use case.

    For input message you will choose Action Step Variables and then you choose the first step 1.`Please enter in your question`
    ![](assets/2024-03-12-17-28-25.png)
    This ensures the MedicX API receives the user's query.    
   * Click "Apply" to save the extension call configuration,
    and we will obtain in Step 2 this
    ![](assets/2024-03-13-08-56-44.png)


7. **Process the Response:**
    * After calling the MedicX API,  we create a new step, with conditions, we choose My Medical Api (step2) then Ran successfully 
    

    ![](assets/2024-03-12-17-31-51.png)

    in order to express code we set variable values, and we create a `New session variable`
    ![](assets/2024-03-12-17-33-44.png)

    we name result and will be free text and then apply.

    ```
    ${result} =${body.message}+"\\nOutput: \\n"+${body.response}
   
    ```
    ![](assets/2024-03-12-17-49-55.png)
    
    If you want clean answer try this
    ```
    ${result_clean} =${body.response}

    ```
    ![](assets/2024-03-13-12-12-27.png)
  
    then in the assitant says you add a function result

    ![](assets/2024-03-12-17-50-43.png)

    This might involve parsing the response data, extracting relevant information, and crafting a response for the user.

8. **Ending**
If you want to end you can create a new step
    ```
    Do you you need anything else?
    ```
    ![](assets/2024-03-13-12-38-17.png)
    Create new step for yes
    ![](assets/2024-03-13-12-39-05.png)
    and another for no
    ![](assets/2024-03-13-12-39-23.png)



9. **Test and Train:**
    * Once you've defined the action flow, including the MedicX extension call and response processing, save your action.
    Click on Preview and then type

    ```
    Medical Query
    ```

    then you ask for example

    ```
    I have drunk too much alcohol I have headache what should do
    ```

    you got


    ![](assets/2024-03-12-17-53-09.png)

   * Test your assistant  Watson Assistant to simulate user interactions and observe how your assistant interacts with the MedicX API.
You can try the following question and check it out  in preview

![](assets/2024-03-13-12-04-57.png)
with the question
```
  I have drunk too much alcohol I have headache what should do
```
![](assets/2024-03-13-12-42-14.png)

then yes
```
What precautions should I take to avoid the spread of contagious illnesses, like the flu or common cold, within my household?
```
![](assets/2024-03-13-12-42-46.png)

```
How to maintain good indoor air quality?
```
![](assets/2024-03-13-12-43-13.png)


**By following these steps, you've successfully created a Watson assistant that leverages a custom extension to interact with an external API (MedicX). This empowers your assistant to access valuable data and functionalities from external sources, enhancing its capabilities and user experience.**

