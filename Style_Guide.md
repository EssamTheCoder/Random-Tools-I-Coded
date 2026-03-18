# Style Guide
This is a (in)comprehensive guide on how to style your code (purely optional btw).
***NOTE: I DO NOT CODE IN ALL LANGUAGES AND FRAMEWORKS, THIS IS VERY MUCH INCOMPLETE AND SUBJECT TO ERRORS AND MISTAKES PLEASE CONTRIBUTE***
As a reference, see multilanguage stuff and then see the stuff that's specific to a single language.

# Multilanguage Stuff

## Curly Braces

### One-liners
When dealing with an if, while, for or any other such statement and the code inside is just one line, do this:

```JavaScript
if(x == y){return "Use only one line, optionally, no semicolon"}
```

For longer one-liners:

```Javascript
if(x == y){
    return "X EQUALS Y OMG IT'S THE END OF THE WORLD AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
}
```

#### Comments
They either go after the closing curly brace or not at all. (short)
For long one-liners, pu them after the actual code meant to be executed inside the block

### Statement Spacing
When you write an if, while, for, try or any other statment that has the following syntax:
```Javascript
name(args){}
```
DO NOT space out the (regular brackets) at all.
As for the {Curly Braces}, you may space them, that's up to you


# Python
It is _heavily_ reccomended to use a main function and the `if __name__ == "__main__":` idiom. Do with this information as you please.

# Sass or Scss

## Ending a style block
If there are no child blocks withing the current block of code, you may optionally remove the last semicolon:

```SCSS
.stuff{
    width: 90px;
    height: 100px;
    border: 1px solid beige;
    border-radius: 20px;
    background: linear-gradient(#f00,#0f0,#00f)
}
```

## Spacing Stuff Out
When writing indented code, just remember to space out the style blocks for the child elements, this includes pseudoclasses of the main element

```SCSS
a{
    color: var(--anchor);
    text-decoration: none;

    &:hover{
        color: var(--anchor-hover);
        font-weight: 600;
    }
}
```

## One-Liners
When using one-liners, follow the code above, but also, use them like normal style definitions, no spacing required. 
Do remember to add a semicolon the end of the main style definition if you're not including it because without it the compiler may return an error

```SCSS
.stuff{
    width: 90px;
    height: 100px;
    border: 1px solid beige;
    border-radius: 20px;
    background: linear-gradient(#f00,#0f0,#00f);
    & .otherstuff{background: #fff}
}
```