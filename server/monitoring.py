import os
import psutil
import logging
import subprocess
from datetime import datetime

class ServerMonitor:
    def __init__(self, log_file='/var/log/zmq-server-monitor.log'):
        self.log = self._setup_logger(log_file)

    def _setup_logger(self, log_file):
        logging.basicConfig(
            filename=log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        return logging.getLogger(__name__)

    def check_server_process(self, process_name='main.py'):
        for proc in psutil.process_iter(['name', 'cmdline']):
            if process_name in ' '.join(proc.info['cmdline'] or []):
                return True
        return False

    def restart_service(self):
        try:
            subprocess.run(['sudo', 'systemctl', 'restart', 'zmq-server'], check=True)
            self.log.info("Service restarted successfully")
            return True
        except subprocess.CalledProcessError as e:
            self.log.error(f"Failed to restart service: {e}")
            return False

    def system_resource_check(self):
        cpu_usage = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        if cpu_usage > 80:
            self.log.warning(f"High CPU Usage: {cpu_usage}%")
        
        if memory.percent > 85:
            self.log.warning(f"High Memory Usage: {memory.percent}%")
        
        if disk.percent > 90:
            self.log.warning(f"Low Disk Space: {disk.percent}% used")

        return {
            'cpu_usage': cpu_usage,
            'memory_usage': memory.percent,
            'disk_usage': disk.percent
        }

    def run_health_check(self):
        self.log.info("Starting health check routine")

        if not self.check_server_process():
            self.log.error("ZMQ Server process not running")
            self.restart_service()

        resources = self.system_resource_check()
        
        self.log.info(f"Health Check Complete: {resources}")

def main():
    monitor = ServerMonitor()
    monitor.run_health_check()

if __name__ == "__main__":
    main()

