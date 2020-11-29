# WebServer

Python web server developed for cs3840.  This is a rudamentary web server with multithreading capabilities.  Currently it is able to run **.html** files within the same directory as the server file.

*Developers: Mikhail Husyev, Viktoria Kondratneko, and Andriy Usyk*

## Dependencies
- python
- python socket
- python threading

## Running the server

To run the server run the following command within the root directory:

```shell
> python webserver.py
```
Any html file that should returned by the server must be within the directory of the web server.

## Using the server/Loading Files

The default implimentation will use the server's ip address as the base address. To access your html files you can use this url format: **server_ip_address/your_file.html**




