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

1. Query Parameter: level
low - For a joke with a low humor level.
medium - For a joke with a medium humor level.
high - For a joke with a high humor level.

2. Header: Accept-Language
en-us - For jokes in English (U.S.).
pt-br - For jokes in Portuguese (Brazil).


#### Example

```bash
curl -H "Accept-Language: pt-br" "http://localhost:5000/joke?level=high"
