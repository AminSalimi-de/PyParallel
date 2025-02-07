from mpi4py import MPI
from mpi4py_helper_functions import *

comm = MPI.COMM_WORLD # the comminucation channel

rank = comm.Get_rank() # PID
    
if rank == 0:
   msg = "Dear 1, Hi! Love 0"
   comm.send(msg, dest=1)
   print_sent_message(rank, 1, msg)
   
elif rank == 1:
    msg = comm.recv(source=0)
    print_received_message(rank, 0, msg)

