
from collections import namedtuple  #datatype for state
import csv      #for csv processing
import io       #for input from file

State = namedtuple("State", "name, nextStates, outputs")


def readCSV(filename):
    """reads the CSV file into a State object

    filename: a string representing a filename, reletive to this file
    returns: a State object filled with the data from filename"""
    stateTable = []     #this will be a list of State objects

    with open("statetable.csv") as file:
        reader = csv.reader(file)       # returns an "iterator" type.  that means you
                                        # can use it like: for (row) in reader.

        #-------------  ALGORITHM  ---------------
        # First, we need to figure out how many inputs & outputs there are in the csv.
        # Via the format specifications, we assume the first column is the "name" of
        # the state.  The next columns are next states, until the header cell starts
        # with a z, then they are outputs.


        header = next(reader) #start with the first line in the header

        #to find out which column the output starts, we start at the left and find the z
        zcol = 1
        for entry in header:
            if zcol >= 2 and entry[0].lower() == "z":
                break
            zcol += 1


        #now to transfer data from the file into the State type
        for line in reader:     #line is a list of strings
            name = line[0]      #the name is always the first column

            nextStates = []     #collect the next states into a list
            for col in range (2, zcol):     #note: col # is index + 1
                nextStates.append(line[col-1])

            outputs = []        #collect the outputs into a list
            for col in range(zcol, len(line)+1):
                outputs.append(line[col-1])

            toAdd = State(name, nextStates, outputs)
            stateTable.append(toAdd)

    return stateTable