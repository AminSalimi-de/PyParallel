from mpi4py import MPI
from mpi4py_helper_functions import *

comm = MPI.COMM_WORLD

me = comm.Get_rank()

other = 1 - me

sent_msg = f"Dear {other}, Hi! Love {me}"

for n in range(1, 16):
    comm.send(sent_msg*2**n, dest=other)
    received_msg = comm.recv(source=other)

    print_sent_message(senderPID=me, receiverPID=other, message=sent_msg)
    print_received_message(receiverPID=me, senderPID=other, message=received_msg)