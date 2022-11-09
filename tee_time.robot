*** Settings ***
Documentation   Set a tee time.
...    Take care to leave at least 2 (or 4) spaces 
...    between variables and their values.
...      E.g., "email_ _ myEmail@example.com"
...       or   "dia_ _ _ _ manana"
Library    keywords

*** Variables ***
${email}    Hagemanjames@yahoo.com
${pw}    test
${dia}    hoy   ## hoy o manana
${hora}    15:20   ### Pattern of HH:MM (I.e., 08:30 or 14:00 etc.)
${zona}    montana  ## montana o valle

*** Tasks ***
Programar una Hora
    Navegar por  https://www.easycancha.com/login
    Ingresar  email: ${email}
    Ingresar  clave: ${pw}
    Apreton  Login
    Apreton  club brisas
    Apreton  Golf
    Escoja   hoy o manana?    ${dia}
    Escoja  la hora:    ${hora}
    Apreton   Siguiente
    Escoja  montana o valle?    ${zona}       
    Apreton  Agregar/Quitar jugadores
    Escoja  2 jugadores
    Apreton  Seleccionar
    Apreton  Reservar y pagar mas tarde

    [Teardown]    Close the browser