import socket
from _thread import *
import threading
import concurrent.futures
import pickle
from player import Player
import pygame

server = "127.0.0.1"
port = 8080

def threaded_client(conn, player):
    pick = pickle.dumps(players[player])
    conn.send(pick)
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))            
            if not data: 
                print("Disconnected!")
                break
            else:
                players[player] = data
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
            conn.sendall(pickle.dumps(reply))
        except:
            break
    print("Lost connection! Closing thread for player " + str(player))
    conn.close()

players = [Player(0,0,50,50,(255,0,0),1), Player(100,100,50,50,(0,0,255),2)]

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((server, port))
    except socket.error as e:
        print(str(e))

    s.listen(2)
    print("Server active, waiting for connection")
    currentPlayer = 0
    joinTasksDone = False
    threads = []
    while True:
        if currentPlayer < 2:        
            conn, addr = s.accept()
            print("Connected to: ", addr)
            t = threading.Thread(target=threaded_client, args=(conn, currentPlayer), daemon=True)
            t.start()            
            threads.append(t)
            # start_new_thread(threaded_client, (conn, currentPlayer))
            currentPlayer += 1
        else:
            if joinTasksDone == False:
                print("No more players, please!")                
                for t in threads:
                    t.join()
                joinTasksDone = True

start_server()