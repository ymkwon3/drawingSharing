import socket, pickle, json, time, base64
from PIL import Image

HOST = '203.255.3.229'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))



# 키보드로 입력한 문자열을 서버로 전송하고

# 서버에서 에코되어 돌아오는 메시지를 받으면 화면에 출력합니다.

# quit를 입력할 때 까지 반복합니다.
while True:

    # message = input('Enter Message : ')
    # if message == 'quit':
    # 	break

    # client_socket.send(message.encode())
    # data = client_socket.recv(1024)
    # datadic = pickle.loads(data)
    # print('Received from the server :', repr(datadic))
    data = b""
    packet = client_socket.recv(4096)
    # if not packet:
    #     try:
    #         print(data)
    #         data_arr = pickle.loads(data)
    #         encoded = base64.b64encode(data_arr).decode()
    #         encoded.save("app.png")
    #         print(data_arr)
    #
    #     except Exception as e:
    #         print('Connect Error : ', e)
    #     break
    # data += packet
    print(packet)
    # while True:
    #     # if not packet: break
    #     # data += packet
    #     print(packet)
    # data = client_socket.recv(8182)
    # dumpfile = pickle.loads(data)
    # typetest = dumpfile["file"]
    
    # print('Received from the server :', type(typetest))

client_socket.close()

