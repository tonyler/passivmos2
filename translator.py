from bech32 import bech32_decode, bech32_encode, convertbits

def convert_address(address, prefixes):
    address_list = []
    # Decode the Bech32 address
    decoded = bech32_decode(address)
    if decoded is None:
        print(f"Invalid Bech32 address: {address}")
        return None

    # Extract the data part
    hrp, data = decoded

    # Convert the data to bytes
    data_bytes = convertbits(data, 5, 8, False)
    if data_bytes is None:
        print(f"Failed to convert data for address: {address}")
        return None
    for new_prefix in prefixes:
        # Encode the data with the new prefix
        new_address = bech32_encode(new_prefix, convertbits(data_bytes, 8, 5, True))
        address_list.append(new_address)
    return address_list
        

