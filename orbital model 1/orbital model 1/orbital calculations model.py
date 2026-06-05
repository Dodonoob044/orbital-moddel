#orbital calculator
import math
print("hello world")

μ = 1.32712440018e20
AU = 149597870691

for i in range(1):
    month_01 = 31
    month_02 = 28
    month_03 = 31
    month_04 = 30
    month_05 = 31
    month_06 = 30
    month_07 = 31
    month_08 = 31
    month_09 = 30 
    month_10 = 31
    month_11 = 30
    month_12 = 31

    month_set = [month_01, month_02, month_03 , month_04 , month_05, month_06, month_07, month_08 , month_09 , month_10, month_11, month_12]

    #periapsis shifts
    Mars_P_shift = 1.9684851172830897
    Venus_P_shift = 1.5649935688888306
    Mercury_P_shift = 1.5377068543850678
    

    #Mars data
    Periapsis_Mars = 206744257295
    Apoapsis_Mars = 249230052571
    Semimajor_axis_Mars = 227987154933
    eccentricity_Mars = 0.09317585301787192
    orbital_period_Mars = 687.1884910540242
    mean_motion_Mars = 0.00914332150345287
    Periapsis_date_Mars = [2026, 3, 26, 6.75]

    #Earth data
    Periapsis_Earth = 147098450000
    Apoapsis_Earth = 152097597000
    Semimajor_axis_Earth = 149598023500
    eccentricity_Earth = 0.01670859976301759
    orbital_period_Earth = 365.2574579722
    mean_motion_Earth = 0.01720207259301959
    Periapsis_date_Earth = [2026, 1, 3, 17.25]

    #Venus data
    Periapsis_Venus = 107477000000
    Apoapsis_Venus = 108939000000
    Semimajor_axis_Venus = 108208000000
    eccentricity_Venus = 0.0067555079
    orbital_period_Venus = 224.69808128656544
    mean_motion_Venus = 0.027962790208103366
    Periapsis_date_Venus = [2026, 5, 15, 4]

    #Mercury data
    Periapsis_Mercury = 46001200000
    Apoapsis_Mercury = 69816900000
    Semimajor_axis_Mercury = 57909050000
    eccentricity_Mercury = 0.2056302080590167
    orbital_period_Mercury = 87.96906366518645
    mean_motion_Mercury = 0.07142494242173163
    Periapsis_date_Mercury = [2026, 5, 18, 11.5]


def elipse_calculator(Rperiapsis, Rapoapsis):
    a = (Rperiapsis + Rapoapsis)/2
    T = 2* math.pi * math.sqrt((a**3)/μ)
    T = T/24/3600
    e = (Rapoapsis-Rperiapsis)/(Rperiapsis+Rapoapsis)
    n = 2*math.pi/T
    return(T, a, e, n)
    
def solve_E_for_M(M, e):
    E = M
    while True:
        correction = (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        E = E - correction
        if abs(correction) < 1e-6:
            break
    return E

def solve_angle_and_range(t, e, a, n):
    M = n*t
    E = solve_E_for_M(M, e)
    x = math.sqrt((1+e)/(1-e))*math.tan(E/2)
    θ = 2*math.atan(x)
    if θ< 0:
        θ += (math.pi*2)
    # now i have the angle i just need the distance
    r = a*(1-e*math.cos(E))
    return(θ, r)

def days_since_O(year, month, day, hour):
    days = year * 365.2574579722
    #month part
    for i in range(1,12, 1):
        if i == month:
            break
        else:
            days += month_set[i-1]
    
    for i in range(0, year+1, 4):
        if i == year:
            if month > 2:
                days += 1
                for j in range(0,year+1,100):
                    if j == year:
                        days-=1
                        for k in range(0, year+1, 400):
                            if k == year:
                                days+=1
    #day part
    if month_set[month-1] < day:
        days += month_set[month-1]
    else:
        days += day - 1
    
    days += hour/24
    
    return(days)

def cos_rule(a,b,c):
    x = ((b**2)+(c**2)-(a**2))/(2*b*c)
    A = math.acos(x)
    return(A)

def figguring_out_periapsis_adjustment():
    current = [int(input("year: ")), int(input("month: ")), int(input("day: ")), float(input("hour: "))]

    distance_Earth_Mercury = 154898369000

    time_Mercury = days_since_O(current[0], current[1], current[2], current[3]) - days_since_O(2023, 1, 20, 1)
    print(time_Mercury)
    Mercury = solve_angle_and_range(time_Mercury, eccentricity_Mercury, Semimajor_axis_Mercury, mean_motion_Mercury)
    print(f"angle Mercury: {Mercury[0]/math.pi*180},  distance Mercury-Sun: {Mercury[1]}")

    time_Earth = days_since_O(current[0], current[1], current[2], current[3]) - days_since_O(Periapsis_date_Earth[0], Periapsis_date_Earth[1], Periapsis_date_Earth[2], Periapsis_date_Earth[3])
    print(time_Earth)
    Earth = solve_angle_and_range(time_Earth, eccentricity_Earth, Semimajor_axis_Earth, mean_motion_Earth)
    print(f"angle Earth: {Earth[0]/math.pi*180},  distance Earth-Sun: {Earth[1]}")

    angle_Mercury_Earth = cos_rule(distance_Earth_Mercury, Earth[1], Mercury[1])
    print(f"angle Mercury-Earth: {angle_Mercury_Earth/math.pi*180}")

    x = Earth[0] - angle_Mercury_Earth
    x -= Mercury[0]
    print(x)



distance_Neptune_Earth = 4518072616000

days_Neptune = days_since_O(2026, 6, 5, 10.75)-days_since_O(1881, 2, 2, 1)
Neptune = solve_angle_and_range(days_Neptune, 0.008646491519787091, 30.07*AU, 0.00010432329590205425)
print(f"angle Neptune: {Neptune[0]/math.pi*180}, range Neptune: {Neptune[1]}")


days_Earth = days_since_O(2026, 6, 5, 10.75)-days_since_O(2026, 1, 3, 17.25)
Earth = solve_angle_and_range(days_Earth, eccentricity_Earth, Semimajor_axis_Earth, mean_motion_Earth)
print(f"angle Earth: {Earth[0]/math.pi*180}, range Earth: {Earth[1]}")


angle_Earth_Neptune = cos_rule(distance_Neptune_Earth, Neptune[1], Earth[1])
print(f"angel between Neptune & Earth: {angle_Earth_Neptune/math.pi*180}")

x = Neptune[0]-Earth[0]-angle_Earth_Neptune
print(x)
