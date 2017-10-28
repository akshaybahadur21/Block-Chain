import hashlib as hasher
import datetime as date

class CreateBlock:
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.create_hash()
		
	def create_hash(self):
		sha=hasher.sha256()
		sha.update(str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash))
		return sha.hexdigest()
	
def create_first_block():
		return CreateBlock(0, date.datetime.now(), "First Block", "0")

def next_block(last_block):
		this_index = last_block.index + 1
		this_timestamp = date.datetime.now()
		this_data = "Block " + str(this_index)
		this_hash = last_block.create_hash
		return CreateBlock(this_index, this_timestamp, this_data, this_hash)


blockchain=[create_first_block()]
previous_block=blockchain[0]
for i in range(0,10):
	block_to_add=next_block(previous_block)
	blockchain.append(block_to_add)
	previous_block=block_to_add
	print "Block #{} has been added".format(block_to_add.index)
	print "Hash: {}\n".format(block_to_add.hash) 
	
