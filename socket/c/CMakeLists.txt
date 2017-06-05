cmake_minimum_required (VERSION 2.8) 
project (socket_c)

add_executable (server server.c)
add_executable (server2 server2.c)
add_executable (client client.c)

add_executable (U_server U_server.c)
add_executable (U_client U_client.c)

add_executable (server_udp server_udp.c)
add_executable (client_udp client_udp.c)
