# Group 4 Project

- The purpose of this is to pull player information from the Hypixel API, which stores Minecraft (an online game) Player Data.
- The User will filter the data using input from the terminal filtering on name data and game mode type.
- This application will return kills, deaths, wins and kill/death ratio for the selected player and game mode.
- Kill/Death ratio will be calculated by a function which utilises the data from API called 'kills' and 'deaths'.

## How the program works

- Run the program [functions/main](functions/main.py)
- Enter the username/player you are looking for
- Program will get, filter and display the required stats

## Useful information

- [Project Trello board](https://trello.com/b/N6nXzian/tsi-team-4)
- [Hypixel API link](https://api.hypixel.net/player?key=c1e412b1-5131-49f9-b7a2-bdfda4371684&name=Jif)
- [Team Retrospective (via Teams)](https://teams.microsoft.com/l/file/49ABE7D5-C95D-465B-B8ED-63E200225C80?tenantId=6e725c29-763a-4f50-81f2-2e254f0133c8&fileType=xlsx&objectUrl=https%3A%2F%2Fgla.sharepoint.com%2Fsites%2Fmsteams_19d476-GroupFour%2FShared%20Documents%2FGroup%20Four%2FGroup4_Retrospective.xlsx&baseUrl=https%3A%2F%2Fgla.sharepoint.com%2Fsites%2Fmsteams_19d476-GroupFour&serviceName=teams&threadId=19:6645007512514573bea2e0363765e6e2@thread.tacv2&groupId=a4a306c3-e31e-48f6-9eb9-f1ee4d95eb4b)

## Architecture

In Progress...

## Well refactored code

- [getData](functions/getData.py)
- [getGameMode](functions/getGameMode.py)
- [getRatio](functions/getRatio.py)

## Tests

- [testGetData](tests/test_get_data.py)
- [testGetGameMode](tests/test_get_game_mode.py)
- [testRatio](test/test_ratio.py)
