import socket


def start_server():

    try:

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("127.0.0.1", 8000))
        server.listen(4)

        while True:

            cl_soc, adress = server.accept()

            data = cl_soc.recv(1024).decode("utf-8")

            print(data)

            hdrs = 'HTTP/1.1 200 OK\r\nContent-type: text/html; charset = utf-8\r\n\r\n'

            content = get_resp(data)
            cl_soc.send(content)
            cl_soc.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        print(" все пошло по .... ")
        server.close()
    print("thats all")


def get_resp(request_data):
    hdrs = 'HTTP/1.1 200 OK\r\nContent-type: text/html; charset = utf-8\r\n\r\n'
    hdrs404 = 'HTTP/1.1 404 OK\r\nContent-type: text/html; charset = utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    response = ''
    try:
        with open('views'+path, 'rb') as file:
            response = file.read()
        return hdrs.encode('utf-8') + response
    except FileNotFoundError:
        with open('views/'+'not_found.html', 'rb') as file:
            response = file.read()
        return (hdrs404).encode('utf-8') + response


if __name__ == "__main__":
    start_server()
