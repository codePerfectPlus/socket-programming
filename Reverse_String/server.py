import socket


class Server:

    def __init__(self, host, port):
        """[summary]

        Args:
            host ([str]): [get the hostname]
            port ([int]): [reserve the port for connection]
        """
        self.host = host
        self.port = port

    def run_server(self):
        """
        This funtion will reverse the string provide by the client
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen(5)

            while True:
                conn, addr = s.accept()
                print(f"Got connection from {addr}")

                # It will only receive data less than 1kb.
                data = conn.recv(1024).decode("utf-8")
                data = data[::-1]

                conn.sendall(bytes(data, "utf-8"))


if __name__ == "__main__":
    host = socket.gethostname()
    port = 12345
    Server(host, port).run_server()
