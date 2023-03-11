import socket
import threading
import json
from logger import *


class Server:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.address = (host, port)

        self.connecton_pool = []
        self.controls = []
        self.managers = []

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.address)

    def listen(self) -> None:
        self.socket.listen()

    def accept_requests(self) -> None:
        while True:
            client, addr = self.socket.accept()
            self.connecton_pool.append(client)
            thread = threading.Thread(
                target=self.handle_tcp_request, args=(client, addr))
            thread.start()

    def handle_tcp_request(self, conn: socket.socket, addr: socket._RetAddress) -> None:
        handshake_packet: str = conn.recv(4096).decode()

        try:
            handshake_json: dict = json.loads(handshake_packet)
        except json.JSONDecodeError:
            info(f"Invalid requests from {addr}")
            return

        if "client" not in handshake_json.keys():
            info(f"Invalid requests from {addr}")
            return

        if handshake_json["client"] == "control":
            self.handle_control(conn, addr)
        if handshake_json["client"] == "manager":
            self.handle_manager(conn, addr)

    def handle_control(self, conn: socket.socket, addr: socket._RetAddress) -> None:
        pass

    def handle_manager(self, conn: socket.socket, addr: socket._RetAddress) -> None:
        pass


if __name__ == "__main__":
    server = Server("0.0.0.0", 10721)
    server.listen
    server.accept_requests()
