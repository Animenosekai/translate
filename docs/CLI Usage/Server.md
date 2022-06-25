# Server

Finally, translatepy also has a built-in HTTP server, which lets you use it from other programming languages without reloading Python every time you want to use translatepy.

## Installation

You will need to install translatepy using the `[server]` option to be able to use the server.

## Running the server

```swift
🧃❯ translatepy server -h                           
usage: translatepy server [-h] [--port PORT] [--host HOST]

optional arguments:
  -h, --help            show this help message and exit
  --port PORT, -p PORT  port to run the server on
  --host HOST           host to run the server on
```

### Arguments

- `--port (-p)` is the port to run the server on. 5000 by default.
- `--host` is the host to run the server on. 127.0.0.1 by default.

## Documentation

Look at the [Getting Started](./Server%20Documentation/Getting%20Started.md) file to get started using the server.
