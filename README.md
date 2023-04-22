
# Query Results Service 🔭
Microservice made with Django, that helps to received the requests for two purposes, 1) Get all the results for an especific investigator, 2) Return a .csv file with the history results of an investigator from the database **predictionsResultsDB**.


## Runnning
First, you need to pull the docker-compose repository, over there you can follow the steps to organize the project to run it successfully, here is the link to the repo.

[Docker-compose file repo](https://github.com/Proyecto-de-Grado-Brainy-Noise/docker-compose/tree/develop)

Just to let you know, the port to which you can send request is the port:

```sh
9005
```

Once the complete project is deployed the IP address will change and probably it won't be localhost, so, you just have to change the localhost in the endpoints with the IP you need. 🧐

### Endpoints
| Request Type | Endpoints |Description|Params|Body|
| ------ | ------ | ------ | ------ | ------ |
| GET | http://localhost:9005/queries/getAllPredictionsByEmail/ |This endpoint has the unique purpose to received the email of the investigator and returns a list of JSON objects with all the results of the predictions.|**email**(String)||
| GET | http://localhost:9005/queries/getAllResultsFileByEmail/ |This endpoint has the unique purpose to received the email of the investigator and returns a **.csv** file with the all the results.|**email**(String)||
| GET | http://localhost:9005/queries/getCurrentResultPrediction/ |This endpoint has the unique purpose to received the task_id and returns the json of the result.|**task_id**(String)||
| GET | http://localhost:9005/queries/getCurrentResultPredictionFile/ |This endpoint has the unique purpose to received the task_id  and returns a **.csv** file with the result.|**task_id**(String)||


👽 Feel free to make any changes in the code 👽


