# Watsonx Assistant with Milvus as Vector Database

Hello everyone, today We are going to build a WatsonX Assistant with Milvus as Vector Database. 

# Introduction 

![alt text](imagenx.png)


In this blog, we will explore the development of a  WatsonX Assistant that can engage in voice interactions and deliver responses using synthetic speech from Watsonx.ai within a Vector Database. This innovative solution harnesses the power of the latest artificial intelligence models, for retrieving questions. Specifically, we will delve into the integration of a Milvus Vector Database within a healthcare use case, creating a virtual assistant doctor for an enhanced patient experience.

Milvus is a database designed to store, index, and manage massive embedding vectors generated by deep neural networks and other machine learning models. It is capable of indexing vectors on a trillion scale and is built to handle embedding vectors converted from unstructured data, which has become increasingly common with the growth of the internet. 

By calculating similarity distances between vectors, WatsonX.ai's Foundation Model analyzes the questions using the Augmented Knowledge Base created by Milvus. This process allows for the examination of correlations between original data sources. In our specific case, we have numerous questions and answers, and our goal is to identify the best answer for each given question.

# Setup 

## Step 1 - Creation of the Virtual Server

First we need to install our Vector Database. The sytem where we want to deploy our database is Ubuntu 22.04.
1. Log in to your IBM Cloud account [here](https://cloud.ibm.com/).
2. From the IBM Cloud dashboard, click on the "Catalog" tab.
3. In the search bar, type "Virtual Servers" and select the "Virtual Servers" option from the results.
4. On the Virtual Servers page, you will find various options for virtual servers. 
Got to Image and Profile and click Change image and find for ubuntu and we choose 
`22.04 LTS Jammy Jellyfish Minimal Install` and click save
![](assets/2024-02-14-16-42-14.png)
5. Click on the chosen virtual server option to start configuring it.
6. On the configuration page, you will be prompted to provide various details like the location, CPU, memory, storage, and operating system. We choose the simplest `bx2-2x8`
![](assets/2024-02-14-16-49-31.png)
7. We create a ssh key with the name pem_ibmcloud and we download.
8.  Complete the remaining configuration options as default,  network settings, and storage options.
9. Once you have configured the instance, review the settings and click on the "Create" button to create the instance.
10. IBM Cloud will initiate the provisioning process, and your Ubuntu instance will be created.
Copy the public ip of you virtual instance.

## Step 2 - Connection to the server
Once the server is running we can connect to the server via ssh, for example

```
ssh -i pem_ibmcloud.pem itzuser@158.175.181.145
```










