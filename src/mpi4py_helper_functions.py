def print_sent_message(senderPID, receiverPID, message):
    print(f"Processor {senderPID} sent message to processor {receiverPID}: {message}")
    
def print_received_message(receiverPID, senderPID, message):
    print(f"Processor {receiverPID} received message from processor {senderPID}: {message}")