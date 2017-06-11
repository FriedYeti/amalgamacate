# Amalgamacate

Easily create one amalgamated source file by adding hotwords into comments where you want the other files pasted.

Useful for when you want to work in multiple files, but a single source file is required, (typically for online editors or single file submittal).

---

## Dependencies

* python3

---

## Command Line Interface Help

Running `python amalgamacate.py -h` will pull up a brief description of the command line inputs, like so:

```
usage: amalgamacate.py [-h] [-hw HOTWORD] main output

Amalgamate source files into one large file

positional arguments:  
	main                 			the file that contains the main process  
	output            			the destination file
optional arguments:  
	-h, --help            			show this help message and exit  
	-hw HOTWORD, --hotword HOTWORD          the hot word to look for, default="AMALGAMACATE:"
```

---

## How to use it:

The first step to using Amalgamacate is to add comments with a "hotword:FILE" format to your main file (i.e. **main.cpp**).
The default hotword is AMALGAMACATE, but the script accepts any string via the `-hw` or `--hotword` option argument.

I find the easiest way to use it is to add a comment on the same line as your include (or import, or whatever it is in your language choice), so that it looks like this:

`#include "utilities.hpp" // -> AMALGAMACATE:utilities.hpp`

*(this will take care of removing the `#include` statement for you, as when the hotword is found it replaces the entire line the hotword is on)*

Once your main source file has the **hotword:file** stuff in place, simply run from the command line:

`python amalgamacate.py main.cpp amalgamated.cpp`

and the script will find the hotwords in main.cpp, replace them with the full contents of their files, and then be copied into a new file **amalgamated.cpp**.

### Custom Hotword

If you decide you don't want to use AMALGAMACATE for your hotword, you can simply append `-hw` or `--hotword` followed by your preferred hotword.
Given the same situation above, you can have the script look for the hotword **MoNkEyBuTt** by running it like this:

`python amalgamacate.py main.cpp amalgamacate.cpp -hw MoNkEyBuTt`

---

## Example Usage

Given two files, **main.cpp** and **utilities.hpp**:

```
main.cpp:

#include <iostream>

#include "utilities.hpp" // -> AMALGAMACATE:utilities.hpp

int main() {
	std::cout << WhatDoISay();
}

```

```
utilities.hpp:

#include <string>

std::string WhatDoISay() {
	return "Hello World!";
}

```

and running:

`python amalgamacate.py main.cpp amalgamated.cpp`

will create:
```
amalgamated.cpp:

#include <iostream>

#include <string>

std::string WhatDoISay() {
	return "Hello World!";
}

int main() {
	std::cout << WhatDoISay();
}
```

---

## Why is it called Amalgamacate?

I decided I wanted something that was easy to identify what it did (i.e. amalgamating files into one), but I didn't want the chance that some peoples files would have false positives on the hotword, so I made up my own word. Now, unless people are using made up words, the only file that will have false positives is the actual script itself.
