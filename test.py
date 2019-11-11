from randimal import Randimal, DisplayOption

if __name__ == "__main__":
    randimal1 = Randimal(2)
    print("Default: " + randimal1.get())
    randimal1 = Randimal(2, displayOption=DisplayOption.LOWERCASE_HYPHENATED)
    print("LCH: " + randimal1.get())
    randimal1 = Randimal(2, displayOption=DisplayOption.CAMELCASE_HYPHENATED)
    print("CCH: " + randimal1.get())
    randimal1 = Randimal(2, displayOption=DisplayOption.CAMELCASE_SPACED)
    print("CCS: " + randimal1.get())
    randimal1 = Randimal(2, displayOption=DisplayOption.LOWERCASE_SPACED)
    print("LCS: " + randimal1.get())