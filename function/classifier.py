__FUNCTION_KEYDICT__ = {
    "'\\x01'": '+A ', "'\\x02'": '+B ',
    "'\\x03'": '+C ', "'\\x04'": '+D ',
    "'\\x05'": '+E ', "'\\x06'": '+F ',
    "'\\x07'": '+G ', "'\\x08'": '+H ',
    "'\\x09'": '+I ', "'\\x0a'": '+J ',
    "'\\x0b'": '+K ', "'\\x0c'": '+L ',
    "'\\x0d'": '+M ', "'\\x0e'": '+N ',
    "'\\x0f'": '+O ', "'\\x10'": '+P ',
    "'\\x11'": '+Q ', "'\\x12'": '+R ',
    "'\\x13'": '+S ', "'\\x14'": '+T ',
    "'\\x15'": '+U ', "'\\x16'": '+V ',
    "'\\x17'": '+W ', "'\\x18'": '+X ',
    "'\\x19'": '+Y ', "'\\x1a'": '+Z '
}

__LOWER_KEYDICT__ = {}

def returns(keys):
    keys = str(keys)
    if __FUNCTION_KEYDICT__.get(keys):
        return __FUNCTION_KEYDICT__[keys]
    else:
        return keys