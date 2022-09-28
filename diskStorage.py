"""
This file implements the simulated disk storage/memory pool in the form of disk + index.
This pool should be able to assign new blocks if needed.
"""

# RECORDSIZE - the size of a record in unit B (byte)
# For the following attributes of a record, these are the respective sizes
# tconst -> 10
# avgRating -> 3
# numVotes -> 7
# total = 20



class Storage():
    """
    
    """
    def __init__(self, max_size, block_size) -> None:
        self.max_size = max_size
        self.block_size = block_size

        self.size_used = 0
        self.actual_size_used = 0
        self.blocks_count = 0

        self.block_size_used = 0
        self.blocks_accessed = 0

        self.cur_block = None  # block address

        # all_blocks is a dict of dicts (many blocks, each with many records)
        # key:value is blockID:record
        self.all_blocks = {}    
    
    def allocate_block(self, size_needed):
        # If incoming record is larger than block size, error!
        if size_needed > self.block_size:
            print("ERROR: Incoming record size is larger than block size!")
            return False

        # Make and allocate new block if no current block OR record can't fit in current block
        if (self.blocks_count == 0 or (self.block_size_used + size_needed > self.block_size)):

            # Allocate a new block only if max_size is not exceeded yet
            if (self.size_used + self.block_size <= self.max_size):
                # Allocate new block, increment size_used by block_size
                new_block = {}
                new_block_address = hex(id(new_block))

                self.size_used += self.block_size
                self.cur_block = new_block_address     
                self.all_blocks[new_block_address] = new_block

                # New block has not been used
                self.block_size_used = 0    

                # Increment number of blocks
                self.blocks_count += 1

                # offset = self.block_size_used

                self.block_size_used += size_needed
                self.actual_size_used += size_needed

                return True

            else:
                print("ERROR: Not enough memory left in storage for new block!")
                print("Currently using " + self.size_used + " out of " + self.max_size)
                return False



    #def deallocate_block(self):

    #def get_record(self, item_address):




    



        





# The disk stores blocks, which are simulated by arrays
# disk = []

# def insert(record):




