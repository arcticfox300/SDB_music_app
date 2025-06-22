from ui import UI
from service import Service

service = Service()
console_ui = UI(service)

console_ui.run()
