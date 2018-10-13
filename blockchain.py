# Import libraries
import hashlib # to hash passwords
from datetime import datetime as date # to get the current date

class Block:
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()

	# returns a new hash for the new block
	def hash_block(self):
		# initiate a hasher object
		sha = hashlib.sha256()
		# generate a hashed text using the index, timestamp, data and previous hash
		sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
		# a hashed string
		return sha.hexdigest()

class Blockchain:
	def __init__(self):
		self.blocks = []
		self.prev_block = None
		self.create_genesis_block()

	def create_genesis_block(self):
		block = Block(0, date.now(), "Genesis block", "0")
		self.blocks.append(block)
		self.prev_block = block

	def generate_next_block(self, data):
		this_index = self.prev_block.index + 1
		this_timestamp = date.now()
		this_data = data
		this_previous_hash = self.prev_block.hash
		block = Block(this_index, this_timestamp, this_data, this_previous_hash)
		self.blocks.append(block)
		self.prev_block = block


if __name__ == '__main__':
	blockchain = Blockchain()
	for i in range(5):
		blockchain.generate_next_block()

	for block in blockchain.blocks:
		if block.index == 0:
			print("Genesis block: {}".format(block.hash))
		else:
			print("Block #{}: {}".format(block.index, block.hash))