Deployment ML Model
===============
In this project we deploy an API of a machine learning model that predicts the worldwide gross expected from a movie. 
- The API was created using **FastAPI**.
- **DVC** is also implemented for data tracking and firebase is used as storage.
- Implemented **workflows** for testing, continuous integration and continuous deployment using **github actions**.
- The api is implemented in heroku.
- Design - Model as Service

[![arquitectura-1.png](https://i.postimg.cc/mgjqnm3R/arquitectura-1.png)](https://postimg.cc/cvKXgM55)

> The deployment can be implemented on other platforms such as google cloud run or azure, but for this test project heroku was used for the deployment because it  provides a free server.