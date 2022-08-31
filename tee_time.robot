*** Settings ***
Documentation   Set a tee time.
...    Take care to leave at least 2 (or 4) spaces between key words.
...    E.g., "hoy o manana? _ _ manana" or  "hoy o manana? _ _ _ _ hoy"
Library    keywords

*** Tasks ***
Programar una Hora
    Navegar por  https://www.easycancha.com/login
    Ingresar  email: Hagemanjames@yahoo.com
    Ingresar  clave: Lucas2022!
    Apreton  Login
    Apreton  club brisas
    Apreton  Golf
    Escoja   hoy o manana?    hoy
    Escoja  la hora:    14:00     # Keep pattern of HH:MM, *note to include ":"


    [Teardown]    Close the browser