class TextChunker:
    def __init__(self, size=400, overlap=50):
        self.size = size
        self.overlap = overlap

    def chunk(self, text):
        words = text.split()
        chunks = []
        i = 0
        while i < len(words):
            chunks.append(" ".join(words[i:i+self.size]))
            i += self.size - self.overlap
        return chunks
