from worker.strategy import MessageStrategy
from worker.message import Message

message = Message(youtube_url="https://www.youtube.com/watch?v=8VyxjhtF-dM")

strategy = MessageStrategy.get_strategy(message)
strategy.execute(message)
