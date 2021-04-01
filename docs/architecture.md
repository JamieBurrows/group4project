# Architecture

While our program doesn't actually utilise Classes, we have created a diagram to outline the different files and respective modules which are called. We use a format similar to UML to show this, but instead the heading for each 'box' is the Python file and then underneath are the functions that are present and can be called.

Classes aren't used as we decided to not go down the Object-Oriented route. We implemented our solution to the problem outlined in our [Introduction](../README.md) on a procedural basis.

Our program starts by running **main.py**, which will import the other required function files and then call our **getData** function and assign the result to the variable **allPlayerData**. Inside this call is a user input requirement to retrieve the Player's username. This is just handled as a **String**. There is also the option to load directly from an existing **JSON** file (previously searched Player data). For either selection, the full player data returned to the variable is made up of **JSON**.

Next, we call **getGameMode** and assign the result to variable **selectedGame**. This takes a user input as returns it as a **String**.

Finally, using the above two variables which have now been assigned their relevant data, the program makes a call to **displayData**. This function will retrieve numerous bits of Player data the user is specifically looking for. This will then be printed and displayed to the console as a **String**.

### Diagram

As our program is procedural, these functions run left to right - starting with getData.py.

![Architecture Diagram](../resources/architecture-diagram.png)