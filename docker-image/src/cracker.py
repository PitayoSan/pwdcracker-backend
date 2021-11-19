from __future__ import division
from mpi4py import MPI
import string
import itertools
import requests
import os
import sys


CHARS = [''] + list(string.ascii_lowercase + string.digits)
CLIENT_PASSWORD = 'CLIENT_PASSWORD'


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

#pw = os.getnev(CLIENT_PASSWORD)
pw = sys.argv[1]
print(pw)
length = len(pw)

n_chars_first = len(CHARS) // size
start_index = int(len(CHARS) * (rank / size))
if rank == size - 1:
	list_for_first = CHARS[start_index :]
else:
	list_for_first = CHARS[start_index : start_index + n_chars_first]

guessed = False
index = 0
for i in list_for_first:
	if rank == size - 1:
		print index / len(list_for_first)

	for guess in itertools.product(CHARS, repeat=length-1):
		guess = i + ''.join(guess)
		if guess == pw:
			guessed = True
			print 'Rank {} named {} did guess the password, which was "{}".'.format(rank, name, pw)
			comm.Abort()
			break

	if guessed: break
	index += 1

