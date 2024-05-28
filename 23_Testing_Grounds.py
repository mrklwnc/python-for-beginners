import hmac
import hashlib


def ksort(obj):
    """Sort objects in an alphabetical order"""

    mykeys = list(obj.keys())
    mykeys.sort()

    return {i: obj[i] for i in mykeys}


def hash_string(obj):
    """Returns a hashable string"""

    hashing_string = ""

    for key in obj.keys():
        if key != "hash":
            hashing_string += f"{obj[key]}"

    return hashing_string


# Sample body from the request
request_body = {
    "merchant_id": 10412,
    "amount": "500.00",
    "invoice": "JAREFERENCE00003",
    "reference_id": "JAREFERENCE00003",
    "callback_url_be": "https://vinu.jaarce.com/webhook",
    "skip_receipt": 0,
    "hash": "CQiDMvu4sIW6",
}

# Sort Alphabetically
sorted_body = ksort(request_body)

# Convert to a byte string
hashing_string = hash_string(sorted_body).encode()

# Encrypt to HmacSHA256
hash = hmac.new(b"CQiDMvu4sIW6", hashing_string, hashlib.sha256).hexdigest()

# Update the hash from the request body
request_body["hash"] = hash
