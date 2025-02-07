from mpi4py import MPI
from mpi4py_helper_functions import *

comm = MPI.COMM_WORLD
BUFFER_SIZE = 1 << 20 # 1MB

me = comm.Get_rank()

other = 1 - me

sent_msg = f"Dear {other}, Hi! Love {me}"

buffer = bytearray(BUFFER_SIZE)

for n in range(1, 16):
    sreq = comm.isend(sent_msg*2**n, dest=other)
    rreq = comm.irecv(buf=buffer, source=other)

    received_msg = rreq.wait()
    
    print_sent_message(senderPID=me, receiverPID=other, message=sent_msg)
    print_received_message(receiverPID=me, senderPID=other, message=received_msg)
    
    sreq.wait()