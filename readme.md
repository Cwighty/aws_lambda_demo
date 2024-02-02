# Steps to deploy lambda function

## 1. Create a new lambda function in AWS console

- you can pick from many languages

## 2. Create a new API Gateway

- You can pick from many triggers (one is API Gateway)
- you can see the body or the query parameters and parse them
- Tip: return the event object as the response to see what it provides

## 3. Call the api endpoint

# Pros and Cons of using AWS Lambda

## Pros

- No need to manage servers
- Pay per use
- Easy to scale
- Many triggers available

## Cons

- Limited languages
- Limited libraries
- Not good for long running processes
- Don't try and make an entire application with lambda functions

### Scenarios

- You have a simple cross cutting concern that you want to extract to a lambda function without having to create/manage/maintain a new server/project
