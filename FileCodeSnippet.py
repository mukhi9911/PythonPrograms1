def setOutputs(key, value):
    import sys
    sys.stdout = open(key,'wt')
    print ("Hello stackoverflow!")
    print ("I have a question.")
    print('ABCD partial execute')
    setOutputs("C:\Files\Output.txt", "")
