# 3/2/23
Thought about how to implement the three different processes and inter-process communication. Decided to have the three processes as three seperate python processes and have them communicate through sockets. At this point it seems like feeding the port to listen on as an argument is the most straight-forward solution. While there is probably a more elegant solution to getting the ports automaticaly, it doesn't seem worth the effort. 

Wrote some code to run a tick() function X times a second where X is the randomly chosen clock speed, instead of using a sleep() statement we use a while True loop that sees if a certain amount of time has passed so we don't run into an issue where tick() takes too long (unlikely but sendall may take a non-negligible amount of time, possibly).

Process spins up two threads to listen for messages from the other two processes and write them to a global message queue, which the tick() message checks when it runs for new messages. Need to use a lock for adding to that queue.