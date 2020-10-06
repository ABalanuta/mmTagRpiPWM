#!/usr/bin/env python3

import click
import pigpio
from os import system
from time import sleep

__author__ = "Artur Balanuta"
__copyright__ = "Copyright 2020, The Millimitro Project"
__license__ = "Apache"
__version__ = "1.0.1"
__maintainer__ = "Artur Balanuta"
__email__ = "arturb@cmu.edu"
__status__ = "Production"

@click.command('cli')
@click.option('--rf', '-t', required=True, type=click.Choice(['reflective', 'non-reflective', 'disable-all'], case_sensitive=False))
@click.option('--mode', '-m', type=click.Choice(['ON', 'OFF', 'PWM'], case_sensitive=False))
#@click.option('--speed', '-s', type=click.IntRange(100, 10000), default=1000, show_default=True)
def cli(rf, mode):
    """Millimetro Configuration Tool"""
    
    # restarting pigpiod with proper Flag
    system("sudo killall pigpiod")
    sleep(.05)
    system("sudo pigpiod -s 4")
    sleep(.05)

    gpio = pigpio.pi()

    if rf == 'reflective':
        gpio.write(27, 1) # Inverter Enable
        gpio.write(22, 1) # Switch A Enable
        if mode.upper() == 'ON':
            gpio.write(12, 1) # Set High
        elif mode.upper() == 'OFF':
            gpio.write(12, 0) # Set Low
        elif mode.upper() == 'PWM':
            gpio.set_PWM_dutycycle(12, 128) # Set PWM of Switch A (out of 255)
        else:
            click.echo('Please specify --mode, -m ')

    elif rf == 'non-reflective':
        gpio.write(17, 1) # Switch B Enable
        if mode.upper() == 'ON':
            gpio.write(13, 1) # Set High
        elif mode.upper() == 'OFF':
            gpio.write(13, 0) # Set Low
        elif mode.upper() == 'PWM':
            gpio.set_PWM_dutycycle(13, 128) # Set PWM of Switch B (out of 255)
        else:
            click.echo('Please specify --mode, -m ')

    elif rf == 'disable-all':
        gpio.write(22, 0) # Switch A Disable
        gpio.write(17, 0) # Switch B Disable
        gpio.write(27, 0) # Inverter Disable
        
if __name__ == '__main__':
    cli()
