# *module* **gtoken**

> [Source: ../../../../../utils/gtoken.py @ line 0](../../../../../utils/gtoken.py#L0)

ORIGINAL FILENAME:  
    gtoken.py  
SOURCE PROJECT:  
    ssut/py-googletrans (https://github.com/ssut/py-googletrans)  
AUTHOR:  
    SuHun Han (@ssut on GitHub)  
EXPLANATION:  
    Generates a ticket to access Google Translate's API  
    Reverse engineered by ssut on the obfuscated and minified code used by Google to generate such token, and implemented on the top of Python.  
    However, this could be blocked at any time.  
COPYRIGHT:  
    Copyright (c) 2015 SuHun Han  
LICENSE:  
    The MIT License (MIT)  
    Copyright (c) 2015 SuHun Han  
    Permission is hereby granted, free of charge, to any person obtaining a copy  
    of this software and associated documentation files (the "Software"), to deal  
    in the Software without restriction, including without limitation the rights  
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
    copies of the Software, and to permit persons to whom the Software is  
    furnished to do so, subject to the following conditions:  
    The above copyright notice and this permission notice shall be included in all  
    copies or substantial portions of the Software.  
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
    SOFTWARE.

## *const* **HEADERS**

> [Source: ../../../../../utils/gtoken.py @ line 45](../../../../../utils/gtoken.py#L45)

## *class* **TokenAcquirer**

> [Source: ../../../../../utils/gtoken.py @ line 56-244](../../../../../utils/gtoken.py#L56-L244)

Google Translate API token generator  
translate.google.com uses a token to authorize the requests. If you are  
not Google, you do have this token and will have to pay for use.  
This class is the result of reverse engineering on the obfuscated and  
minified code used by Google to generate such token.  
The token is based on a seed which is updated once per hour and on the  
text that will be translated.  
Both are combined - by some strange math - in order to generate a final  
token (e.g. 744915.856682) which is used by the API to validate the  
request.  
This operation will cause an additional request to get an initial  
token from translate.google.com.  
Example usage:  
    >>> from googletrans.gtoken import TokenAcquirer  
    >>> acquirer = TokenAcquirer()  
    >>> text = 'test'  
    >>> tk = acquirer.do(text)  
    >>> tk  
    950629.577246

### Raises

- `Exception`

### *attr* TokenAcquirer.**RE_TKK**

> [Source: ../../../../../utils/gtoken.py @ line 82](../../../../../utils/gtoken.py#L82)

### *attr* TokenAcquirer.**RE_RAWTKK**

> [Source: ../../../../../utils/gtoken.py @ line 83](../../../../../utils/gtoken.py#L83)

### *func* TokenAcquirer.**acquire**

> [Source: ../../../../../utils/gtoken.py @ line 185-239](../../../../../utils/gtoken.py#L185-L239)

#### Parameters

- **text**


### *func* TokenAcquirer.**do**

> [Source: ../../../../../utils/gtoken.py @ line 241-244](../../../../../utils/gtoken.py#L241-L244)

#### Parameters

- **text**

