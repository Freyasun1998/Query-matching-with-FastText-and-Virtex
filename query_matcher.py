from typing import List

import compress_fasttext as ft
from virtex import RequestHandler
from virtex import http_server


model_filepath = "en.model.bin"


class MatchingService(RequestHandler):

    def __init__(self):
        self.model = ft.models.CompressedFastTextKeyedVectors.load(model_filepath)

    def process_request(self, data):
        return [sent.strip() for sent in data]

    def run_inference(self, model_input):
        matches = [self.model.most_similar(q) for q in model_input]
        return matches

    def process_response(self, model_output_item):
        return model_output_item


app = http_server(
    name='fasttext_word_matcher',
    handler=MatchingService(),
    max_batch_size=128,
    max_time_on_queue=0.005
)
