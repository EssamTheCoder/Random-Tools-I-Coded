# Style Guide
This is a comprehensive guide on how to style your code (purely optional btw), it contains some languages
***NOTE: I DO NOT CODE IN ALL LANGUAGES AND FRAMEWORKS, THIS IS VERY MUCH INCOMPLETE AND SUBJECT TO ERRORS AND MISTAKES PLEASE CONTRIBUTE***
First, see multilanguage stuff and then see the stuff that's specific to a single language.

# Multilanguage Stuff
## Curly Braces
When dealing with an if, while, for... statement and the code inside is just one line, do the following

`example.js`
```JavaScript
if(x == y){return "Use only one line, and optionally, no semicolons"}
```

For longer one-liners, do it the normal way.


# Python
It is _heavily reccomended_ to use a main function and the `if __name__ == "__main__":` idiom. Do with this information as you please.1

# Sass or Scss
# Ending a style block
If there are no child blocks withing the current block of code, you may optionally remove the last semicolon

`example.scss`
```SCSS
.stuff{
    width: 90px;
    height: 100px;
    border: 1px solid beige;
    border-radius: 20px;
    background: linear-gradient(#f00,#0f0,#00f)
}
```