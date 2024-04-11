# Caesar-Cipher--Text-encoder-decoder
![V](https://github.com/Himel-Sarder/Caesar-Cipher--Text-encoder-decoder/assets/143216886/0e8a60da-a645-4c0c-a390-1bce633d3c5c)

## What is Caesar Cipher?   
Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

For example, with a shift of 3:   
A becomes D   
B becomes E   
C becomes F   
...   
X becomes A   
Y becomes B   
Z becomes C   

More : https://en.wikipedia.org/wiki/Caesar_cipher

## Features
- Encrypt text using a specified shift value
- Decrypt text using the same shift value
- Support for both uppercase and lowercase letters
- Command-line interface for easy usage

## Installation
To install the Caesar Cipher program, follow these steps:
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd caesar cipher`
3. Install dependencies: `pip install -r requirements.txt`

## Usage
To use the Caesar Cipher program, run the following command:
```
python caesar cipher.py
```
Follow the prompts to enter the text to encrypt or decrypt, the shift value, and the desired operation (encode or decode).

## Examples
Suppose we have the plaintext message "HELLO" and we want to encrypt it using a Caesar Cipher with a shift value of 3:   
Determine the shift value: In this case, it's 3.   
Map each letter of the plaintext to its corresponding letter after shifting by 3:   
'H' becomes 'K'   
'E' becomes 'H'   
'L' becomes 'O'   
'L' becomes 'O'   
'O' becomes 'R'   
Combine the shifted letters to form the encrypted message: "KHOOH".   
So, the encrypted message for "HELLO" using a Caesar Cipher with a shift value of 3 is "KHOOH".   

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
- Himel Sarder
- Dept. of CSE, BSFMSTU, Bangladesh

## Required knowledge   
- Loops
- If/else conditons
- Python function
- Module
- ASCII art


## FAQ
**Q: What is the maximum shift value supported by the Caesar Cipher program?**   
A: The maximum shift value is 25, which corresponds to shifting the entire alphabet by one position.   

**Q: Can I use negative shift values to encrypt text in reverse?**   
A: Yes, negative shift values can be used to encrypt text in reverse order, but decryption will require a positive shift value.   

## Roadmap
- Add support for special characters and punctuation
- Implement additional encryption algorithms for comparison
- Improve error handling and input validation


## Online caesar cipher for better experience   
https://www.boxentriq.com/code-breaking/caesar-cipher

## Conclusion
Thank you for using the Caesar Cipher program! We hope you find it useful for encrypting and decrypting your messages securely.

# Thank You   
