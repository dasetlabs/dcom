import pandas as pd
from ast import literal_eval
from models import DCoMModel
from config import USE_AUX, MODEL_TYPE, PADDING_LEN, VOCAB_SIZE, TRAIN_CSV_PATH, VALID_CSV_PATH, BATCH_SIZE, \
    OPTIMIZER, MODEL_SAVE_DIR, INITIAL_METADATA_PATH, INITIAL_MODEL_WEIGHT_PATH

def train():
    model = DCoMModel(USE_AUX, MODEL_TYPE, PADDING_LEN, VOCAB_SIZE)
    train = pd.read_csv(TRAIN_CSV_PATH)
    train["values"] = train["values"].apply(lambda x: literal_eval(x))
    valid = pd.read_csv(VALID_CSV_PATH)
    valid["values"] = valid["values"].apply(lambda x: literal_eval(x))
    initial_metadata_path = INITIAL_METADATA_PATH if pathlib.Path(INITIAL_METADATA_PATH).exists() else None
    initial_model_weight_path = INITIAL_MODEL_WEIGHT_PATH if pathlib.Path(INITIAL_MODEL_WEIGHT_PATH).exists() else None
    model.fit(train, valid, BATCH_SIZE, OPTIMIZER, MODEL_SAVE_DIR, initial_model_weight_path, initial_metadata_path)



if __name__=="__main__":
    train()