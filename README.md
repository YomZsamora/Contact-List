# Contact-List

Simple Python App that creates new contacts with properties. Touches on Test Driven Development using unittest (Python test framework).

## Technologies Used

- Python3.9
- unittest (Python test framework)
- PyperClip

##### Setup Instructions and Installation

- Clone this repository to a location in your file system. `git clone https://github.com/YomZsamora/Contact-List.git`
- Open terminal command line then navigate to the root folder of the application. `cd Contact-List`
- Run `./run.py` 


## Behaviour Driven Development

1. Displays Intro Message to user
    - OUTPUT: "Hello Welcome to your contact list. What is your name?"
   - INPUT: "Samora"
   - OUTPUT: "Hello Samora. what would you like to do?"
2. Enter Short Code
   - INPUT: "cc"
   - INPUT: "first_name", "last_name", "phone-number", "email"
   - OUTPUT: "New Contact Samora Yommie created" - Create new contact by providing required properties
3. Enter Short Code
   - INPUT: "dc" 
   - OUTPUT: "Enter the number you want to search for" - Prompts user to enter number to search for
   - OUTPUT: "Samora Yommie .....0712345678" - Displays existing contacts
4. Enter Short Code
   - INPUT: "fc"
   - INPUT: "0712345678" - Search by Phone Number
   - OUTPUT: "Phone number.......0712345678, Email address....... samora.y@adzumi.co.ke" - Returns contact if exists

## Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request


## Known Bugs

If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.

### License

*MIT*
Copyright (c) 2022 **Yommie Samora**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
