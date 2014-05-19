
class Parser:

    @classmethod
    def Parse(cls, value):
        try: return int(value)
        except ValueError: pass

        try: return float(value)
        except ValueError: return value
