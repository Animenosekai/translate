# server

This contains a slightly modified version of `translatepy server`.

## What is a *translation ID* ?

A translation ID is a hash created using the following information :

- the source language (resulting source language if it is an automatic detection)
- the destination language
- the source text
- the destination text

## Environment Variables

| Name                      | Description                                                            | Default     |
|---------------------------|------------------------------------------------------------------------|-------------|
| `HOST`                    | The host to listen to                                                  | `127.0.0.1` |
| `PORT`                    | The port to listen to                                                  | `5001`      |
| `TRANSLATEPY_DB_DISABLED` | To disable any DB interaction                                          | `False`     |
| `TRANSLATEPY_MONGO_URI`   | The MongoDB URI to connect to. If none, a `mongod` process will be ran | `None`      |
| `TRANSLATEPY_IP_SALT`     | The salt to create IP hashes                                           | ``          |
