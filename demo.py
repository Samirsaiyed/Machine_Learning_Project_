from housing import pipeline
from housing.pipeline.pipleline import Pipeline
from housing.logger import logging

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipleline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__=="__main__":
    main()
