# blogit-poc

Proof of Concept of a full-stack implementation of a custom blog platform.

Technologies used:

* React
* Bootstrap
* AWS
* Python

## Overview of the frontend

The frontend section of this stack uses React and Bootstrap to present the content. This POC uses a basic barebones website template hosted on Netlify as a demo.

[The frontend in more detail](./content/contentSection.md)

## Overview of the backend

The backend runs in AWS using an API Gateway connected to lambdas, which interfaces with a DynamoDB. The AWS stack can be generated from a Cloudformation template for an easier startup.

[The backend in more detail](./content/contentSection.md)

## Overview of the content management system

The context management system functions as a collection of Markdown texts and scripts. Blog text is written in Markdown, which is combined with any corresponding metadata and wrapped into a JSON payload to be posted to the blog's backend API.

[The content management in more detail](./content/contentSection.md)
