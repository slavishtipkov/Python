
#bytes
    # very similar to strings
    # immutable sequences of bytes
    # ASCII
    # Bytes Literals
        # b'data'
        # b"data"
    # Converting Between Strings and Bytes
        # encode
        # decode
    # Used a lot when working with Files, Network resources, Http responses, etc. (streams)



d = b'some bytes'
print(d.split()) # [b'some', b'bytes']


test_encoding = 'asdgs swfdsf  дргсдфг яв фддгх асфгдфхгф весдгф дфгх дг'

data = test_encoding.encode("utf-8")
print(data) # 4\xd1\x80\xd0\xb3\xd1\x81\x ...

bulgarian = data.decode("utf-8")
print(bulgarian) # ддгх асфгдфхгф ве ...

print(bulgarian == test_encoding) # True