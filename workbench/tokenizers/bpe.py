class BPETokenizer:
    def __init__(self, merges, vocab):
        self.merges = merges
        self.vocab = vocab
        self.merge_history = {}

    def train(self, text: str, vocab_size: int, verbose: bool = False):
        text_to_bytes = text.encode("utf-8")
        
        