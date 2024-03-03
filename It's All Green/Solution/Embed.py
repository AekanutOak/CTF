import struct

def append_text_to_png(input_png, output_png, text_key, text_value):
    with open(input_png, 'rb') as f_in:
        png_data = f_in.read()

    # Define the new "tEXt" chunk
    new_chunk = struct.pack('>I', len(text_key)) + text_key.encode('utf-8') + b'\x00' + text_value.encode('utf-8')

    # Find the position to insert the new chunk
    iend_pos = png_data.rfind(b'IEND')
    insert_pos = iend_pos - 12  # Place the new chunk just before the IEND chunk

    # Insert the new "tEXt" chunk
    modified_data = png_data[:insert_pos] + new_chunk + png_data[insert_pos:]

    with open(output_png, 'wb') as f_out:
        f_out.write(modified_data)

# Example usage
input_file = './problem2.png'
output_file = './output.png'
text_key = 'flag'
text_value = 'flag{St39an0gr4phy}'

append_text_to_png(input_file, output_file, text_key, text_value)
