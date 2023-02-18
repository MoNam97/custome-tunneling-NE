import socket, threading
from Xclient import M_FORMAT

ip = '127.0.0.12'
port = 12000

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((ip, port))


def send_request_udp(request):
    return request


def handle_tcp_recv(Xclient, addr):
    print(f'new udp connection from {addr}')
    try:
        request = Xclient.recv(1024).decode(M_FORMAT)
        print(f'request:\t{request}\n')

        response = send_request_udp(request)

        Xclient.send(('I received the following response for request:\n' + response).encode(M_FORMAT))
        Xclient.close()
    except:
        print('TCP connection failed...')
    #
    # try:
    #     while True:
    #
    #         request, address = udp_socket.recvfrom(1024)
    #         if address not in udp_conn_list:
    #             print(f'new udp connection from {address}')
    #             tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #             # tcp_socket.connect(tcp_server_addr)
    #             # tcp_socket.sendall(rmt_udp_addr)
    #             udp_conn_list[address] = tcp_socket
    #             # threading.Thread(target=handle_tcp_conn_recv, args=(tcp_socket, udp_socket, address)).start()
    #             # threading.Thread(target=handle_tcp_conn_send, args=(tcp_socket, rmt_udp_addr, outgoing_udp_queue)).start()
    #         request = request.decode(M_FORMAT)
    #         print(f'received UDP request from client {address}')
    #         print(f'request:\t{request}\n')
    #         # handle_udp_conn_recv(request)
    #         incoming_udp_queue.put((request, address))
    #         incoming_udp_list.append((request, address))
    #
    #         print(f"{os.getpid()}\nudp_conn_list: {udp_conn_list}\n")
    #         for item in incoming_udp_list:
    #             print(item)
    #         print("_____________\n")
    #
    #         udp_socket.sendto("message received\n".encode(M_FORMAT), address)
    # except KeyboardInterrupt:
    #     print("Closing the UDP connection...")


if __name__ == "__main__":
    tcp_socket.listen()
    print('Xserver listening...')
    while True:
        Xclient, addr = tcp_socket.accept()
        threading.Thread(target=handle_tcp_recv, args=(Xclient, addr))