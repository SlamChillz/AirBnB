# AirBnB clone - The console

  ---

  ## Summary
  This is the first step towards building your first full web application: the
  AirBnB clone. This first step is very important because you will use what you
  build during this project with all other following projects: HTML/CSS
  templating, database storage, API, front-end integration and more. For this
  project, the back-end console has been implemented.

  ## Class Models

  The following classes were created for this project:

  - BaseModel:

    - `id`, `created_at`, `updated_at`

  - User:
    - `emaiil`, `password`, `first_name`, `last_name`

  - State:
    - `name`

  - City:
    - `state_id`, `name`

  - Amenity:
    - `name`

  - Place:
    - `city_id`, `user_id`, `name`, `description`, `number_rooms`
    - `number_bathrooms`, `max_guest`, `price_by_night`, `latitudde`
    - `longitude`, `amenity_id`

  - Review:
    - `place_id`, `user_id`, `text`

  ## Database (File Storage)
 
  [FileStorage](./models/engine/file_storage.py) is the storage engine that
  persists database interaction.

  The storage object is an instantiation of `FileStorage` class.
  The `storage` object is loaded/re-loaded from any class instances
  stored in the JSON file `file.json`. As class instances are created,
  updated, or deleted, the `storage` object is used to register 
  corresponding changes in the `file.json`.

  ## Command Line Interpreter (Console)

  The console is a command line interpreter that permits management of the
  backend 
  of AirBnB. It can be used to handle and manipulate all classes utilized
  by 
  the application (achieved by calls on the `storage` object defined above).

  ### Familiarizing the Console

  The AirBnB console can be run both interactively and non-interactively. 
  To run the console in non-interactive mode, pipe any command(s) into an
  execution 
  of the file `console.py` at the command line.

  ```
  $ echo "help" | ./console.py
  (hbnb) 
  Documented commands (type help <topic>):
  ========================================
  EOF  all  count  create  destroy  help  quit  show  update

  (hbnb) 
  $
  ```

  Alternatively, to use the HolbertonBnB console in interactive mode, run the 
  file `console.py` by itself:

  ```
  $ ./console.py
  ```

  While running in interactive mode, the console displays a prompt for input:

  ```
  $ ./console.py
  (hbnb) 
  ```

  To quit the console, enter the command `quit`, or input an EOF signal 
  (`ctrl-D`).

  ```
  $ ./console.py
  (hbnb) quit
  $
  ```

  ```
  $ ./console.py
  (hbnb) EOF
  $
  ```

  ### Running Commands

  The AirBnB console supports the following commands:

  * **create**
    * Usage: `create <class>`

    Creates a new instance of a given class. The class' ID is printed and 
    the instance is saved to the file `file.json`.

    ```
    $ ./console.py
    (hbnb) create BaseModel
    791b4d1b-5873-4473-8f05-1d5042f3ea55
    (hbnb) quit
    $ cat file.json ; echo ""
    {"User.791b4d1b-5873-4473-8f05-1d5042f3ea55": {"id":
    "791b4d1b-5873-4473-8f05-1d5042f3ea55", "
    created_at": "2022-08-08T03:33:44.586704", "updated_at":
    "2022-08-08T03:33:44.586716", "__clas
    s__": "User"}}
    ```

  * **show**
    * Usage: `show <class> <id>` or `<class>.show(<id>)`

    Prints the string representation of a class instance based on a given id.

    ```
    $ ./console.py
    (hbnb) create BaseModel
    b9fffc7a-7460-4a92-9557-33069a224ad8
    (hbnb)
    (hbnb) show BaseModel b9fffc7a-7460-4a92-9557-33069a224ad8
    [BaseModel] (b9fffc7a-7460-4a92-9557-33069a224ad8) {'id':
    'b9fffc7a-7460-4a92-9557-33069a224ad
    8', 'created_at': datetime.datetime(2022, 8, 8, 3, 36, 16, 197918),
    'updated_at': datetime.dat
    etime(2022, 8, 8, 3, 36, 16, 197929)}
    (hbnb) 
    (hbnb) BaseModel.show("b9fffc7a-7460-4a92-9557-33069a224ad8")
    [BaseModel] (b9fffc7a-7460-4a92-9557-33069a224ad8) {'id':
    'b9fffc7a-7460-4a92-9557-33069a224ad
    8', 'created_at': datetime.datetime(2022, 8, 8, 3, 36, 16, 197918),
    'updated_at': datetime.dat
    etime(2022, 8, 8, 3, 36, 16, 197929)}
    (hbnb) 
    ```
  * **destroy**
    * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

    Deletes a class instance based on a given id. The storage file
    `file.json` 
    is updated accordingly.

    ```
    $ ./console.py
    (hbnb) create Review
    3a82eb9b-ebec-41b3-ad10-d671397152ed
    (hbnb)
    (hbnb) destroy BaseModel b9fffc7a-7460-4a92-9557-33069a224ad8
    (hbnb) Review.destroy("3a82eb9b-ebec-41b3-ad10-d671397152ed")
    (hbnb) quit
    $ cat file.json ; echo ""
    {}
    ```

  * **all**
    * Usage: `all` or `all <class>` or `<class>.all()`

    Prints the string representations of all instances of a given class.
    If no 
    class name is provided, the command prints all instances of every
    class.

    ```
    $ ./console.py
    (hbnb) create Place
    1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0
    (hbnb) create State
    5775db45-1e19-4d23-91ee-d6e77f39fd1e
    (hbnb)
    (hbnb) all
    ["[Place] (1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0) {'id':
    '1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0'
    , 'created_at': datetime.datetime(2022, 8, 8, 3, 45, 7, 308633),
    'updated_at': datetime.dateti
    me(2022, 8, 8, 3, 45, 7, 308644)}", "[State]
    (5775db45-1e19-4d23-91ee-d6e77f39fd1e) {'id': '57
    75db45-1e19-4d23-91ee-d6e77f39fd1e', 'created_at':
    datetime.datetime(2022, 8, 8, 3, 45, 41, 90
    1544), 'updated_at': datetime.datetime(2022, 8, 8, 3, 45, 41,
    901557)}"]
    (hbnb)
    (hbnb) State.all()
    ["[State] (5775db45-1e19-4d23-91ee-d6e77f39fd1e) {'id':
    '5775db45-1e19-4d23-91ee-d6e77f39fd1e'
    , 'created_at': datetime.datetime(2022, 8, 8, 3, 45, 41, 901544),
    'updated_at': datetime.datetime(2022, 8, 8, 3, 45, 41, 901557)}"]
    (hbnb) 
    (hbnb) all Place
    ["[Place] (1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0) {'id':
    '1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0'
    , 'created_at': datetime.datetime(2022, 8, 8, 3, 45, 7, 308633),
    'updated_at': datetime.datetime(2022, 8, 8, 3, 45, 7, 308644)}]
    (hbnb) 
    ```

  * **count**
    * Usage: `count <class>` or `<class>.count()`

    Retrieves the number of instances of a given class.

    ```
    $ ./console.py
    (hbnb) create City
    b39aed1b-44a0-49a5-b9ce-97061eda5afe
    (hbnb) create City
    98c01385-9152-4063-baa9-dcd4640ad83c
    (hbnb) 
    (hbnb) City.count()
    2
    (hbnb) 
    ```

  * **update**
    * Usage: `update <class> <id> <attribute name> "<attribute
    * value>"` or
    `<class>.update(<id>, <attribute name>, <attribute value>)` or
    `<class>.update(<id>, <attribute dictionary>)`.

    Updates a class instance based on a given id with a given
    key/value attribute 
    pair or dictionary of attribute pairs. If `update` is called with a single 
    key/value attribute pair, only "simple" attributes can be updated (ie. not 
    `id`, `created_at`, and `updated_at`). However, any attribute can
    be updated by 
    providing a dictionary.

    ```
    $ ./console.py
    (hbnb) create Place
    1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0
    (hbnb)
    (hbnb) update Place 1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0 location "south"
    (hbnb) show Place 1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0
    [Place] (1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0) {'id':
    '1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0',
    'created_at': datetime.datetime(2022, 8, 8, 3, 45, 7, 308633),
    'updated_at': datetime.datetime
    (2022, 8, 8, 3, 58, 35, 306147), 'location': 'south'}
    (hbnb)
    (hbnb) Place.update("1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0", "rooms", 5)
    (hbnb)
    (hbnb) Place.show("1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0")
    [Place] (1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0) {'id':
    '1fec9bbc-210c-4fa0-b4e1-0caad1a62bb0',
    'created_at': datetime.datetime(2022, 8, 8, 3, 45, 7, 308633),
    'updated_at': datetime.datetime
    (2022, 8, 8, 4, 0, 14, 570897), 'location': 'south', 'rooms': 5}
    (hbnb) 
    ```

    ## Testing

    Unittests for the HolbertonBnB project are defined in the
    [tests](./tests) 
    folder. To run the entire test suite simultaneously, execute the
    following command:

    ```
    $ python3 unittest -m discover tests
    ```

    Alternatively, you can specify a single test file to run at a time:

    ```
    $ python3 unittest -m tests/test_console.py
    ```

    ## Authors
  * **Mendie Uwemedimo**
    * <[Mendy](https://github.com/Slamchillz)>
  * **Oluwateniola Adegbulugbe**
    * <[Ludten](https://github.com/Ludten)>
