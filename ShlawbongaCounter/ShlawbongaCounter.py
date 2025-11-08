import config

class ShlawbongaCounter:
    def __init__(self):
        self.total_subs = 0
        self.last_sub_total = 0
        self.total_bits = 0
    
    def update_subs(self, new_sub_total):
        if new_sub_total > self.last_sub_total:
            subs_delta = new_sub_total - self.last_sub_total
            self.total_subs += subs_delta
        
        self.last_sub_total = new_sub_total
    
    def update_bits(self, bits):
        self.total_bits += bits
    
    @property
    def shlawbonga_count(self):
        return self.total_subs + (self.total_bits // config.BITS_PER_HIT)

    def write_count(self, path):
        with open(path, "w") as f:
            f.write(f"SHLAWBONGA COUNT: {self.shlawbonga_count}")