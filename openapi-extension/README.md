# OpenAPI  Extension

OpenAPI (formerly known as Swagger) is an open standard for describing and documenting REST APIs. An OpenAPI document defines the resources and operations that are supported by an API, including request parameters and response data, along with details such as server URLs and authentication methods.

An OpenAPI document describes a REST API in terms of paths and operations. A path identifies a particular resource that can be accessed by using the API (for example, a hotel reservation or a customer record). An operation defines a particular action that can be performed on that resource (such as creating, retrieving, updating, or deleting it).

The OpenAPI document specifies all of the details for each operation, including the HTTP method that is used, request parameters, the data included in the request body, and the structure of the response body.

## API definition

To create a custom extension, you need access to an OpenAPI document that describes the REST API you want to integrate with. Many third-party services publish OpenAPI documents that describe their APIs, which you can download and import. For an API that your company maintains, you can use standard tools to create an OpenAPI document that describes it.

The SwaggerHub website offers an OpenAPI 3.0 Tutorial, and tools to help you develop and validate your OpenAPI document. You can use the online Swagger editor to convert your OpenAPI document to the correct format and OpenAPI version.

The OpenAPI document must satisfy the following requirements and restrictions:

- The document must conform to the OpenAPI 3.0 specification. If you have an OpenAPI (or Swagger) document that uses an     earlier version of the specification, you can use the online Swagger editor to convert it to OpenAPI 3.0.
[https://editor.swagger.io/](https://editor.swagger.io/)

- The document must be in JSON format (YAML is not supported). If you have a YAML document, you can use the online Swagger editor to convert it to JSON.

- The size of the document must not be more than 4 MB if you have a Plus or higher plan of watsonx Assistant. However, if you have an Enteprise plan with data isolation, the size of the document must not be more than 8 MB.

- The content-type must be application/json.
- Each operation must have a clear and concise summary. The summary text is used in the UI to describe the operations that are available from an action, so it should be short and meaningful to someone who is building an assistant.
- Relative URLs are currently not supported.
- Only Basic, Bearer, OAuth 2.0, and API key authentication are supported.
    For OAuth 2.0 authentication, Authorization Code, Client Credentials, Password, and custom grant types that starts with x- are supported. Note that x- is used by the IBM IAM authentication mechanism and by watsonx.
- Schemas that are defined by using anyOf, oneOf, and allOf are currently not supported.

- In addition, any call to the external API must complete within 30 seconds.


# Testing OpenAPI extensions

We developed a simple notebook to verify the openapi.json extensions.

## Examples 1

```
cd example1

```
