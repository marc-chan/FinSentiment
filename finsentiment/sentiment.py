import os
import numpy as np
import pandas as pd
from finsentiment.utils import ensure_upper

STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')

class SentimentDictModel(object):
    def __init__(self, token_polarities):
        self._dictionary = {
            token: polarity \
            for token, polarity \
            in token_polarities}

    @ensure_upper
    def _tokenizer(self, text):
        tokens = text.split(' ')
        return tokens

    @ensure_upper
    def _token_polarity(self, token):
        polarity = self._dictionary.get(token)
        return polarity

    def _get_polarities(self, tokens):
        polarities = [self._token_polarity(token) for token in tokens]
        polarities = [p for p in polarities if p is not None]
        return polarities

    def _get_direction(self, tokens):
        polarities = self._get_polarities(tokens)
        direction = [(p > 0) * 2.0 - 1.0 for p in polarities]
        return direction

    def sentiment(self, text, strategy='direction'):
        tokens = self._tokenizer(text)
        if strategy == 'direction':
            vals = self._get_direction(tokens)
        elif strategy == 'polarity':
            vals = self._get_polarities(tokens)
        else:
            raise InvalidArgumentError(f"{strategy} is not a valid strategy.")

        if len(vals) == 0:
            return 0.0
        else:
            return np.mean(vals)

class LoughranMcDonaldModel(SentimentDictModel):
    def __init__(self, dictionary_path=None):
        if not dictionary_path:
            default_fn = 'LoughranMcDonald_MasterDictionary_2018.csv'
            dictionary_path = os.path.join(STATIC_PATH, default_fn)
        lm_df = pd.read_csv(dictionary_path)
        lm_dict = {}
        for _, score in lm_df.iterrows():
            if score['Positive']:
                lm_dict[score['Word']] = +1.0
            elif score['Negative']:
                lm_dict[score['Word']] = -1.0
            else:
                continue
        super().__init__(tuple(lm_dict.items()))

class HarvardGeneralInquirerModel(SentimentDictModel):
    def __init__(self, dictionary_path=None):
        if not dictionary_path:
            default_fn = 'inquirerbasic.csv'
            dictionary_path = os.path.join(STATIC_PATH, default_fn)
        hv_df = pd.read_csv(dictionary_path, low_memory=False)
        hv_dict = {}
        for _, score in hv_df.iterrows():
            if not pd.isna(score['Pstv']):
                hv_dict[score['Entry']] = +1.0
            elif not pd.isna(score['Ngtv']):
                hv_dict[score['Entry']] = -1.0
            else:
                continue
        super().__init__(tuple(hv_dict.items()))
