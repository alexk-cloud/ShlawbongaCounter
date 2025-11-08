import config

class ShlawbongaCounter:
    def __init__(self):
        self.total_subs = 0
        self.last_sub_total = 0
        self.subs_gained = 0
        self.total_bits = 0
        self.last_bits_total = 0
        self.bits_gained = 0
    
    def update_subs(self, new_sub_total):
        if new_sub_total > self.last_sub_total:
            self.subs_gained = new_sub_total - self.last_sub_total
            self.total_subs += self.subs_gained
        
        self.last_sub_total = new_sub_total
    
    def update_bits(self, bits):
        if bits > self.last_bits_total:
            self.bits_gained = bits - self.last_bits_total
            self.total_bits += bits
        
        self.last_bits_total = bits
        
    @property
    def shlawbonga_count(self):
        return self.subs_gained + (self.bits_gained // config.BITS_PER_HIT)

    def write_count(self, path):
        with open(path, "w") as f:
            f.write(f"SHLAWBONGA COUNT: {self.shlawbonga_count}")