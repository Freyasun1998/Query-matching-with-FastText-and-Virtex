# Lab 06: Query matching with FastText and Virtex


## Launch a FastText service using the Virtex library in Python
The purpose of this lab is to expose you to a few things:

- The [FastText](https://fasttext.cc/docs/en/python-module.html) library in Python, which is a language modeling and text classification framework

- The idea that NLP systems typically take on the form of microservices, wherein specific functions, such as computing embeddings or computing similar words, are performed in isolation and accessed through HTTP requests (or other protocols such as gRPC).

- A web client such as [Postman](https://www.postman.com/downloads/) or [Advanced Rest Client](https://install.advancedrestclient.com/install), which allows you to make HTTP requests containing data (such as JSON) to the HTTP endpoint hosting your model.

- The [Virtex](https://pypi.org/project/virtex/) library, which provides a convenient way to expose your machine learning computation as a service over HTTP without having to write any networking code (see `query_matcher.py`, `query_matcher.sh`).


## Task I (20 pts)

1. Launch the FastText query matching service by running the following command from the terminal from within the `lab-06/` directory:
    
        $ ./query_matcher.sh

2. Open your REST client (e.g., ARC, Postman)

    - Enter `http://127.0.0.1:8092` into the Request URL bar
    
    - In the Body content type field choose `application/json`

    - Click the body tab and enter `{"data": ["dogs", "bakery", "python", "Python", "florida", "supreme"]}`

    - Explore FastText by changing the words and looking at the matches. Paste of a few of the responses below:

    ``` 
    # Query results go here
{
    "data": [
        [
            [
                "dog",
                0.7867995595824732
            ],
            [
                "cats",
                0.7165611165618743
            ],
            [
                "puppies",
                0.6921363999150841
            ],
            [
                "Dogs",
                0.6902032510944948
            ],
            [
                "pets",
                0.6587464319006179
            ],
            [
                "puppy",
                0.6317238632228434
            ],
            [
                "cat",
                0.5744769563535082
            ],
            [
                "animals",
                0.5688323939489226
            ],
            [
                "Dog",
                0.5603523654640973
            ],
            [
                "horses",
                0.5559973712560864
            ]
        ],
        [
            [
                "pastry",
                0.5819581440592939
            ],
            [
                "shop",
                0.5731792194770771
            ],
            [
                "cafe",
                0.570185424428111
            ],
            [
                "restaurant",
                0.5669266455894146
            ],
            [
                "grocery",
                0.5635846157197025
            ],
            [
                "supermarket",
                0.561918485321718
            ],
            [
                "café",
                0.5309661883651372
            ],
            [
                "shops",
                0.5293787097584538
            ],
            [
                "cakes",
                0.4914405795211418
            ],
            [
                "loaf",
                0.48259627856575155
            ]
        ],
        [
            [
                "tiger",
                0.28542779326847917
            ],
            [
                "turtle",
                0.2685207764328628
            ],
            [
                "turtles",
                0.25342329675413827
            ],
            [
                "shrimp",
                0.24927080782745467
            ],
            [
                "crab",
                0.24544058840416663
            ],
            [
                "dioxide",
                0.2407363370310442
            ],
            [
                "curry",
                0.23403165758016706
            ],
            [
                "rice",
                0.22783078414879454
            ],
            [
                "not",
                0.22409474172074184
            ],
            [
                "only",
                0.22377282601771795
            ]
        ],
        [
            [
                "PHP",
                0.5252903479827643
            ],
            [
                ".NET",
                0.5027453127530028
            ],
            [
                "Java",
                0.48971316163783307
            ],
            [
                "syntax",
                0.48009634662463696
            ],
            [
                "Programming",
                0.47753022364138964
            ],
            [
                "MySQL",
                0.460709743406548
            ],
            [
                "API",
                0.44191241747672627
            ],
            [
                "programming",
                0.43596008180787305
            ],
            [
                "GUI",
                0.4315750956018232
            ],
            [
                "scripts",
                0.42872353623161275
            ]
        ],
        [
            [
                "Lauderdale",
                0.352312199746364
            ],
            [
                "Florida",
                0.27162007515421743
            ],
            [
                "Miami",
                0.26587937421720886
            ],
            [
                "Paso",
                0.26465424582264657
            ],
            [
                "Melbourne",
                0.26404063159752517
            ],
            [
                "Jacksonville",
                0.25376261524812427
            ],
            [
                "Coral",
                0.24834282452447023
            ],
            [
                "Scotia",
                0.2476674552671307
            ],
            [
                "Palm",
                0.24353943074555384
            ],
            [
                "Santa",
                0.24330703357361358
            ]
        ],
        [
            [
                "ultimate",
                0.5284947594504621
            ],
            [
                "absolute",
                0.5193428218385738
            ],
            [
                "divine",
                0.47891367035950283
            ],
            [
                "Supreme",
                0.47699683046861485
            ],
            [
                "superior",
                0.4662356840014122
            ],
            [
                "greatest",
                0.4610117984126455
            ],
            [
                "utmost",
                0.44582795229665195
            ],
            [
                "highest",
                0.4432882690321498
            ],
            [
                "greatness",
                0.43724125240521317
            ],
            [
                "sovereign",
                0.43136246144662604
            ]
        ]
    ],
    "error": null
}
    ``` 

### Docker
Virtex will not run on certain machines / environments. If you encounter problems running this code on your machine, you can instead use [Docker](https://www.docker.com/products/docker-desktop/). Once you have docker installed, execute the following commands from within the `lab-06/` directory:

    $ docker build -t fasttext-query-matcher .
    $ docker run --rm --name query-matcher -p 8092:8092 fasttext-query-matcher:latest

And then head over to your rest client (step 2 above) to complete the task. 

### Programmatic interface
As a last resort, you can interact with FastText programmatically from within Python if you are unable to run the query mather on your local machine or in docker, for example:

   ```python
   import compress_fasttext as ft

   model_filepath = "en.model.bin"
   model = ft.models.CompressedFastTextKeyedVectors.load(model_filepath)
   match = model.most_similar("Python")
   print(match)
   ```
