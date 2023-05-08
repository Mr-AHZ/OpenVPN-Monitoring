#Created By Mr-AHZ
from rich.console import Console
from rich.table import Table
import time

while True:
        rows = []

        with open('/var/log/openvpn/status.log', 'r') as f:
            log = f.readlines()
            for i in range(3, len(log)):
                if log[i] == 'ROUTING TABLE\n':
                    break
                data = log[i].split(',')
                mbytesR = str(round(int(data[2]) / 1048576, 1)) + " Mb"
                mbytesS = str(round(int(data[3]) / 1048576, 1)) + " Mb"
                data[1].split(":")[0]
                rows.append([str(i - 2), data[0], data[1], mbytesR , mbytesS, data[4],])
            f.close()

            table = Table(title="VPN Log View", style='red', header_style='blue')
            columns = ["Num", "Name", "IP", "Received", "Send", "Connected Since"]
            for column in columns:
                table.add_column(column)
            for row in rows:
                table.add_row(*row, style='green', end_section=True)

            console = Console()
            console.print(table)

            watch_file = 'openvpn-status.log'
        time.sleep(10)  # Sleep for 1 minute before checking again
