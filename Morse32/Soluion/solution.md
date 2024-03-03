# Solution
First of all, you can use any morse code decryption tool to get the output. The first result is `JJLE4RSPKIZEITCKJZDESVCTGJFUUS2FINLVGQ2LJJEEMU2OINKUSTSHKZCVMQJ5`. This is give non-sense to use. If you use some tools to identify encoding scheme you will know that this is base32 encoded text. After encoding with base32 you will get `JVNFOR2DLJNFITS2KJKECWSCKJHFSNCUINGVEVA=` which is also base32 decoded text. After several attempt you will finally get the flag.
# Answer
flag{3nc0d1n9123}
