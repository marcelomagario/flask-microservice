# Flask Microservice

This is a Flask microservice that provides programming jokes with filtering by humor level and language selection.

## Requirements

- Docker
- Docker Compose

## Setup

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

## Endpoints

### `GET /joke`

Returns a programming joke based on the humor level and language.

#### Query Parameters

- `level`: Humor level of the joke (`low`, `medium`, `high`). Default is `medium`.

#### Headers

- `Accept-Language`: Language of the joke (`en` for English, `pt-br` for Brazilian Portuguese). Default is `en`.

#### Example

```bash
curl -H "Accept-Language: pt-br" "http://localhost:5000/joke?level=high"
