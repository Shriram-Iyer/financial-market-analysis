import yfinance as yf
import json
from kafka import KafkaProducer
import schedule
import time
from datetime import datetime
import logging
import os
from dotenv import load_dotenv

# Main producer code here...

if __name__ == "__main__":
    main()