from functions import displayData, getData, getGameMode, gameModeStatsDict

if __name__ == "__main__":
    allPlayerData = getData.getData()
    selectedGame = getGameMode.getGameMode()

    displayData.displayData(allPlayerData, selectedGame, gameModeStatsDict.gamemodeStats)

