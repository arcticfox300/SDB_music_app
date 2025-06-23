from Repository.Repository import Repository
from Service.ListenerService import ListenerService
from Service.StatisticsService import StatisticsService
from UI.ui import UI
from Service.SongService import SongService

song_repository = Repository([])
listener_repository = Repository([])
song_service = SongService(song_repository)
listener_service = ListenerService(listener_repository)
statistics_service = StatisticsService(song_repository, listener_repository)
console_ui = UI(song_service, listener_service, statistics_service)

console_ui.run()
