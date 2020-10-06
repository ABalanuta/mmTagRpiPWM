sudo apt-get install \
    pigpio \
    python-pigpio \
    python3-pigpio \
    python3-click

sudo ln -s /home/pi/gpioService.service /etc/systemd/system/gpioService.service
sudo systemctl enable gpioService.service
