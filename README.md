En el repositorio actual, se debía crear el modelo de base de datos para instagram. Previamente, debíamos hacer un pequeño diagrama de lo que queremos representar, para posteriormente proceder a realizarlo en el boilerplate actual.

Se recrearon 4 tablas (usuario, post, comentarios y followers), dentro de cada una, las distintas columnas con las propiedades que las componen, así como las relaciones que hay entre las tablas, entre Primary Key y las Foreign Keys.


<img src="./DataBaseModelling.jpg">




# Create the database model for Instagram

**Important**: To do this activity you need to `fork` this repo into your **Github** account and then open the forked repo on Gitpod.

Inside he `src/models.py` file you will find a couple of classes describing an example database.

Here is a 4min video explaining what UML is: [https://www.youtube.com/watch?v=UI6lqHOVHic](https://www.youtube.com/watch?v=UI6lqHOVHic)

We are going to be creating the Entity Relationship Diagram for Instagram Database, a very similar diagram to this one:

![Instagram Diagram](https://github.com/breatheco-de/exercise-instagram-data-modeling/blob/master/assets/example.png?raw=true)
[Click to open diagram](https://app.quickdatabasediagrams.com/#/d/LxNXQZ)

> 🔥 You can use this FREE tool to practice your diagram for the first time: https://app.quickdatabasediagrams.com/#/d/


## 💻 Installation

1. Get inside the environment `$ pipenv shell`

2. Install all dependencies `$ pipenv install`

3. Generate de diagram as many times as you need `$ python src/models.py`

4. Open the file `diagram.png` to check out your UML diagram!


## 📝Instructions

Your Job is to update the `src/models.py` file with the code needed to replicate the instagram data model.

The project is using the SQLAlchemy Python library to generate the database.

- What tables do you think instagram might have on its database: E.g: Post, User, etc.?
- What properties should go inside the user? or inside the Post table?
- Please add at least 4 models with all of its properties.
- Degenerate the diagram.png file at the end by running `$ python3 models.py` on the console.


