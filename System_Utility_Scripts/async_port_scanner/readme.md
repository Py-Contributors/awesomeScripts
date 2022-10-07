# Python Port Scanner Using Asyncio Module

## Key points:
- It doesn't use multiprocessing or multithreading; it uses asynchronous processes.
- The scripts send the requests one after another and processes the replies when they arrive.
- Adding timeout is important because some connection attempts may hang. asyncio.wait_for is used for that purpose.