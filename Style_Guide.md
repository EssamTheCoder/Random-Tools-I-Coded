# Style Guide
This is a comprehensive guide on how to style your code (purely optional btw), it contains some languages
***NOTE: I DO NOT CODE IN ALL LANGUAGES AND FRAMEWORKS, THIS IS VERY MUCH INCOMPLETE AND SUBJECT TO ERRORS AND MISTAKES PLEASE CONTRIBUTE***
First, see multilanguage stuff and then see the stuff that's specific to a single language.

# Multilanguage Stuff

## Curly Braces

### One-liners
When dealing with an if, while, for or any other such statement and the code inside is just one line, do this:

```JavaScript
if(x == y){return "Use only one line, optionally, no semicolon"}
```
For longer one-liners, do it the normal way.

### Statement Spacing
When you write an if, while, for, try or any other statment that has the following syntax:
```Javascript
name(args){}
```
DO NOT space out the (regular brackets) at all.
As for the {Curly Braces}, you may space them, that's up to you


# Python
It is _heavily reccomended_ to use a main function and the `if __name__ == "__main__":` idiom. Do with this information as you please.

# Sass or Scss
## Ending a style block
If there are no child blocks withing the current block of code, you may optionally remove the last semicolon

```SCSS
.stuff{
    width: 90px;
    height: 100px;
    border: 1px solid beige;
    border-radius: 20px;
    background: linear-gradient(#f00,#0f0,#00f)
}
```