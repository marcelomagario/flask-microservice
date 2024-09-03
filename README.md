# Flask Microservice

This is a Flask microservice that provides programming jokes with filtering by humor level and language selection.

## Running the Application

To run the application, you need to build and start the Docker container. Follow these steps:

### Setup

1. Clone the repository:

    ```bash
    git clone <REPOSITORY_URL>
    cd flask-microservice
    ```


2. Build the Docker image and start the container:

    ```bash
    docker-compose up --build
    ```

3. The application will be available at `http://localhost:5000`.




## API Endpoint

### `GET /joke`

Returns a programming joke based on the humor level and language.

#### Query Parameters

##### Level
1. low - For a joke with a low humor level.
2. medium - For a joke with a medium humor level.
3. high - For a joke with a high humor level.


##### Header: Accept-Language
1. en-us - For jokes in English (U.S.).
2. pt-br - For jokes in Portuguese (Brazil).


#### cURL to Test

```bash
curl --location 'http://localhost:5000/joke?level=low' \
--header 'Accept-Language: en-us'
```


![image](https://github.com/user-attachments/assets/3d95d22e-f20d-4978-9dfa-45f666f196a6)
