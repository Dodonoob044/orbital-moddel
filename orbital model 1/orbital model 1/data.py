rotation = 0



#constants
μ = 1.32712440018e20
AU = 149597870691

#angle periapsis of planets and Earth

Mars_periapsis_adjustment = 2.453985730083436 + rotation
Venus_periapsis_adjustment = -0.4917868504634558 + rotation
Mercury_periapsis_adjustment = 0.5197628231051556 + rotation
Jupiter_periapsis_adjustment = 1.5506772717783741 + rotation
Saturn_periapsis_adjustment = 0.1960914748187934 + rotation
Uranus_periapsis_adjustment = -1.1954542835139543 + rotation
Neptune_periapsis_adjustment = 1.005683087011651 + rotation
#these are temporary periapsis adjustments due to some difficulty with calculating the actual
#values from the outer plannets.

#Mars data

Periapsis_Mars = 206744257295
Apoapsis_Mars = 249230052571
Semimajor_axis_Mars = 227987154933
eccentricity_Mars = 0.09317585301787192
orbital_period_Mars = 687.1884910540242
mean_motion_Mars = 0.00914332150345287
Periapsis_date_Mars = [2026, 3, 26, 6.75]
size_Mars = 5
size_Mars_min = 3
delay_Mars = -81.5625
color_Mars = (148, 10, 10)

#Earth data

Periapsis_Earth = 147098450000
Apoapsis_Earth = 152097597000
Semimajor_axis_Earth = 149598023500
eccentricity_Earth = 0.01670859976301759
orbital_period_Earth = 365.2574579722
mean_motion_Earth = 0.01720207259301959
Periapsis_date_Earth = [2026, 1, 3, 17.25]
size_Earth = 7
size_Earth_min = 4
delay_Earth = 0
color_Earth = (16,154,235)

#Venus data

Periapsis_Venus = 107477000000
Apoapsis_Venus = 108939000000
Semimajor_axis_Venus = 108208000000
eccentricity_Venus = 0.0067555079
orbital_period_Venus = 224.69808128656544
mean_motion_Venus = 0.027962790208103366
Periapsis_date_Venus = [2026, 5, 15, 4]
size_Venus = 4
size_Venus_min = 3
delay_Venus = -131.44791666662786
color_Venus = (233,205,93)

#Mercury data

Periapsis_Mercury = 46001200000
Apoapsis_Mercury = 69816900000
Semimajor_axis_Mercury = 57909050000
eccentricity_Mercury = 0.2056302080590167
orbital_period_Mercury = 87.96906366518645
mean_motion_Mercury = 0.07142494242173163
Periapsis_date_Mercury = [2026, 5, 18, 11.5]
size_Mercury = 2
size_Mercury_min = 2
delay_Mercury = -46.7913530014414
color_Mercury = (212,210,202)

#Jupiter data

Periapsis_Jupiter = 740743000000
Apoapsis_Jupiter = 816081000000
Semimajor_axis_Jupiter = 778412000000
eccentricity_Jupiter = 0.04839211111853363
orbital_period_Jupiter = 4335.354271446193
mean_motion_Jupiter = 0.0014492899342880307
Periapsis_date_Jupiter = [2023, 1, 20, 1]
size_Jupiter = 20
size_Jupiter_min = 5
delay_Jupiter = 1079.4494572499534
color_Jupiter = (233,206,117)

#Saturn data

Periapsis_Saturn = 1349823615000
Apoapsis_Saturn = 1514500000000
Semimajor_axis_Saturn = 1432161807500
eccentricity_Saturn = 0.05749224149730023
orbital_period_Saturn = 10819.282001126652
mean_motion_Saturn = 0.0005807395820282062
Periapsis_date_Saturn = [2003, 7, 21, 2]
size_Saturn = 20
size_Saturn_min = 5
delay_Saturn = 7836.299492054968
color_Saturn = (233,206,117)

#Uranus data

Periapsis_Uranus = 18.33*AU
Apoapsis_Uranus = 20.11*AU
Semimajor_axis_Uranus = 19.189*AU
eccentricity_Uranus = 0.04630593132154007
orbital_period_Uranus = 30777.157135390007
mean_motion_Uranus = 0.00020415093179462906
Periapsis_date_Uranus = [1966, 11, 9, 10.666]
size_Uranus = 20
size_Uranus_min = 5
delay_Uranus = 21605.72181166534
color_Uranus = (145,176,222)

#Neptune data

Periapsis_Neptune = 29.81*AU
Apoapsis_Neptune = 30.33*AU
Semimajor_axis_Neptune = 30.07*AU
eccentricity_Neptune = 0.008646491519787091
orbital_period_Neptune = 60228.017652727
mean_motion_Neptune = 0.00010432329590205425
Periapsis_date_Neptune = [1881, 2, 2, 1]
size_Neptune = 20
size_Neptune_min = 5
delay_Neptune = 52933.00848930236
color_Neptune = (101,203,246)


