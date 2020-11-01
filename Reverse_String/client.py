import socket


class Client:

    def __init__(self, host, port):
        """[summary]

        Args:
            host ([str]): [get the hostname]
            port ([int]): [reserve the port for connection]
        """
        self.host = host
        self.port = port

    def run_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))

            input_string = input("Enter string : -> ")
            s.sendall(bytes(input_string, "utf-8"))
            print(s.recv(1024).decode("utf-8"))


if __name__ == "__main__":
    host = socket.gethostname()
    port = 12345
    Client(host, port).run_client()
