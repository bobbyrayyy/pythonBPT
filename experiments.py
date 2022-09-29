# Import libraries
import sys

# Import project files
from bPlusTree import *
from diskStorage import *

# Constants (in bytes)
RECORD_SIZE = 20
OFFSET_SIZE = 5

DISK_SIZE = 200000000    # 200MB
INDEX_SIZE = 300000000   # 300MB


def experiment_one(BLOCK_SIZE):
    """
    Experiment 1: store the data (which is about IMDb movives and described in Part 4) 
    on the disk (as specified in Part 1) and report the following statistics:
    - the number of blocks;
    - the size of database (in terms of MB);
    """
    print("\n---------------------------------------------------")
    print("Starting experiment 1")

    max_records_per_block = BLOCK_SIZE//(RECORD_SIZE)
    print("The max number of records per block is:", max_records_per_block)

    # Initialise a b+ tree 
    bplustree = BPlusTree(max_records_per_block)

    # Open data file 
    records = []
    with open("data/data.tsv") as file:
        for line in file:
            record=line.split('\t')
            records.append(record)

    # Insert each record into the b+ tree and simulate storing in disk
    for record in records:
        # key is numVotes, which is index 2 of the record
        key = int(record[2][:-1])
        bplustree.insert(key, record)


        # print('Insert ')
        # print(record)
        # bplustree.show()

        # Simulate storing in disk
        record_size = sys.getsizeof(record)
        record_adddress = hex(id(record))
        # print(record_size)
        # print(record_adddress)

    bplustree.showTop(5)
    #print(bplustree.find(1308)[1308])

    # Print num of blocks
    print("Number of blocks:", bplustree.get_count_blocks())

    # Print num of records
    print("Number of records:", bplustree.get_count_records())

    # Print size of database in MB


   


    
# def experiment_two():

# def experiment_three():

# def experiment_four():

# def experiment_five():




if __name__ == '__main__':
    BLOCK_SIZES = [200, 500]
    for BLOCK_SIZE in BLOCK_SIZES:
        print("\n\nPerforming experiments with block size =", BLOCK_SIZE)
        experiment_one(BLOCK_SIZE)

    
