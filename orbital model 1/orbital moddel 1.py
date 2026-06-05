#agenda
#calculate the correct periapsis adjustments
#in seperate file make a better code for intercepts
# make the moon
# make moons, i dont know how many i expect. not a priority
# make the camera move 

#bugs


#imports
import pygame
import time
import math
pygame.init()


#window details
SCREEN_WITH = 1000
SCREEN_HEIGHT = 650
SCREEN = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT))
X_adjust = SCREEN_WITH*0.5
Y_adjust = SCREEN_HEIGHT*0.5
t = 0
scale = 1e9
rotation = -2
scale_variable = 1e9/scale

#functions
def solve_E_for_M(M, e):
    E = M
    while True:
        correction = (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        E = E - correction
        if abs(correction) < 1e-6:
            break
    return E
#E = solve_E_for_M(2.497705102854544, eccentricity_Earth)
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
#solve_angle_and_range(145.156249999961, eccentricity_Earth, Semimajor_axis_Earth, mean_motion_Earth)
def draw_object_in_orbit(t, e, a, n, delay, color, size, important, p_adjust):
    object_data = solve_angle_and_range((t+delay), e, a, n)
    X_object = (math.cos(2*math.pi-object_data[0]+p_adjust) * object_data[1])/ scale
    Y_object = (math.sin(2*math.pi-object_data[0]+p_adjust) * object_data[1])/ scale
    
    #if important:
    #    pygame.draw.circle(SCREEN, (0, 0, 0), ((X_object + X_adjust), (Y_object + Y_adjust)), size+3)
    pygame.draw.circle(SCREEN, (color), ((X_object + X_adjust), (Y_object + Y_adjust)), size)
#draws an object in orbit around the Sol
def calculate_tracers(a, T):
    tracers = (2*math.pi*a)/(10216870687/scale_variable)
    trace_time = T/tracers
    if trace_time<1:
        trace_time = 1
    return(trace_time)
#calculates the delay between every tracer to prevent overcrowding/overspacing
def object_size(max, min):
    size = max*scale_variable
    if size<min:
        size = min
    return(size)






#data
μ = 1.32712440018e20
AU = 149597870691


#Sol
size_Sol = 20
size_Sol_min = 7

#angle periapsis of planets and Earth
def data_periapsis():
    global Uranus_periapsis_adjustment, Mars_periapsis_adjustment, Venus_periapsis_adjustment, Mercury_periapsis_adjustment ,Jupiter_periapsis_adjustment, Saturn_periapsis_adjustment, Neptune_periapsis_adjustment
    Mars_periapsis_adjustment = 2.453985730083436 + rotation
    Venus_periapsis_adjustment = -0.4917868504634558 + rotation
    Mercury_periapsis_adjustment = 0.5197628231051556 + rotation
    #Jupiter_periapsis_adjustment = -1.5506772717783741 + rotation
    Jupiter_periapsis_adjustment = 3.14 + rotation
    #Saturn_periapsis_adjustment = -0.1960914748187934 + rotation
    Saturn_periapsis_adjustment = 4.8 + rotation
    Uranus_periapsis_adjustment = 3.7 + rotation
    Neptune_periapsis_adjustment = 0.5 + rotation
    #these are temporary periapsis adjustments due to some difficulty with calculating the actual
    #values from the outer plannets.

data_periapsis()
#Mars data
def data_Mars():
    global size_Mars_min, orbital_period_Mars, Periapsis_date_Mars, Apoapsis_Mars, Semimajor_axis_Mars, eccentricity_Mars, mean_motion_Mars, Periapsis_date_Mars, size_Mars, delay_Mars, color_Mars, tracers_Mars, trace_time_Mars
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
data_Mars()
#Earth data
def data_Earth():
    global size_Earth_min, orbital_period_Earth, Periapsis_date_Earth, Apoapsis_Earth, Semimajor_axis_Earth, eccentricity_Earth, mean_motion_Earth, Periapsis_date_Earth, size_Earth, delay_Earth, color_Earth, tracers_Earth, trace_time_Earth
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
data_Earth()
#Venus data
def data_Venus():
    global size_Venus_min, orbital_period_Venus, Periapsis_date_Venus, Apoapsis_Venus, Semimajor_axis_Venus, eccentricity_Venus, mean_motion_Venus, Periapsis_date_Venus, size_Venus, delay_Venus, color_Venus, tracers_Venus, trace_time_Venus
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
data_Venus()
#Mercury data
def data_Mercury():
    global size_Mercury_min, orbital_period_Mercury, Periapsis_date_Mercury, Apoapsis_Mercury, Semimajor_axis_Mercury, eccentricity_Mercury, mean_motion_Mercury, Periapsis_date_Mercury, size_Mercury, delay_Mercury, color_Mercury, tracers_Mercury, trace_time_Mercury
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
data_Mercury()
#Jupiter data
def data_Jupiter():
    global size_Jupiter_min, orbital_period_Jupiter, Periapsis_date_Jupiter, Apoapsis_Jupiter, Semimajor_axis_Jupiter, eccentricity_Jupiter, mean_motion_Jupiter, Periapsis_date_Jupiter, size_Jupiter, delay_Jupiter, color_Jupiter, tracers_Jupiter, trace_time_Jupiter
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
data_Jupiter()
#Saturn data
def data_Saturn():
    global size_Saturn_min, orbital_period_Saturn, Periapsis_date_Saturn, Apoapsis_Saturn, Semimajor_axis_Saturn, eccentricity_Saturn, mean_motion_Saturn, Periapsis_date_Saturn, size_Saturn, delay_Saturn, color_Saturn, tracers_Saturn, trace_time_Saturn
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
data_Saturn()
#Uranus data
def data_Uranus():
    global size_Uranus_min, orbital_period_Uranus, Periapsis_date_Uranus, Apoapsis_Uranus, Semimajor_axis_Uranus, eccentricity_Uranus, mean_motion_Uranus, Periapsis_date_Uranus, size_Uranus, delay_Uranus, color_Uranus, tracers_Uranus, trace_time_Uranus
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
data_Uranus()
#Neptune data
def data_Neptune():
    global size_Neptune_min, orbital_period_Neptune, Periapsis_date_Neptune, Apoapsis_Neptune, Semimajor_axis_Neptune, eccentricity_Neptune, mean_motion_Neptune, Periapsis_date_Neptune, size_Neptune, delay_Neptune, color_Neptune, tracers_Neptune, trace_time_Neptune
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
data_Neptune()

#color data
color_inner_blur = (31, 31, 31)
color_trace = (135, 144, 149)



run =  True
while run == True:
    scale_variable = 1 * 1e9/scale
    events = pygame.event.get()
    SCREEN.fill((0, 0, 0))
    time.sleep(0.01)
    #if t<152:
    #    t += 0.5
    t = 152

    #inner plannets
    if scale <= 4.5e9:
        #object scaling
        size_Mars_adjusted = object_size(size_Mars, size_Mars_min)
        size_Earth_adjusted = object_size(size_Earth, size_Earth_min)
        size_Venus_adjusted = object_size(size_Venus, size_Venus_min)
        size_Mercury_adjusted = object_size(size_Mercury, size_Mercury_min)

        #object tracing
        trace_time_Mars = calculate_tracers(Semimajor_axis_Mars, orbital_period_Mars)
        trace_time_Earth = calculate_tracers(Semimajor_axis_Earth, orbital_period_Earth)
        trace_time_Venus = calculate_tracers(Semimajor_axis_Venus, orbital_period_Venus)
        trace_time_Mercury = calculate_tracers(Semimajor_axis_Mercury, orbital_period_Mercury)
        
        
        #Mars
        for i in range (0, int(orbital_period_Mars), int(trace_time_Mars)):
            draw_object_in_orbit(i, eccentricity_Mars, Semimajor_axis_Mars, mean_motion_Mars, 0, color_trace, 1, False, Mars_periapsis_adjustment)
        draw_object_in_orbit(t, eccentricity_Mars, Semimajor_axis_Mars, mean_motion_Mars, delay_Mars, color_Mars, size_Mars_adjusted, True, Mars_periapsis_adjustment)

        #Earth
        for i in range(0, int(orbital_period_Earth), int(trace_time_Earth)):
            draw_object_in_orbit(i, eccentricity_Earth, Semimajor_axis_Earth, mean_motion_Earth, 0, color_trace, 1, False, rotation)
        draw_object_in_orbit(t, eccentricity_Earth, Semimajor_axis_Earth, mean_motion_Earth, delay_Earth, color_Earth, size_Earth_adjusted, True, rotation)

        #Venus
        for i in range(0,int(orbital_period_Venus), int(trace_time_Venus)):
            draw_object_in_orbit(i, eccentricity_Venus, Semimajor_axis_Venus, mean_motion_Venus, 0, color_trace, 1, False, Venus_periapsis_adjustment)
        draw_object_in_orbit(t, eccentricity_Venus, Semimajor_axis_Venus, mean_motion_Venus, delay_Venus, color_Venus, size_Venus_adjusted, True, Venus_periapsis_adjustment)

        #Mercury
        for i in range(0,int(orbital_period_Mercury), int(trace_time_Mercury)):
            draw_object_in_orbit(i, eccentricity_Mercury, Semimajor_axis_Mercury, mean_motion_Mercury, 0, color_trace, 1, False, Mercury_periapsis_adjustment)
        draw_object_in_orbit(t, eccentricity_Mercury, Semimajor_axis_Mercury, mean_motion_Mercury, delay_Mercury, color_Mercury, size_Mercury_adjusted, True, Mercury_periapsis_adjustment)
    #inner blur
    else:
        size_inner = Apoapsis_Mars/scale*2
        line_with_inner = size_inner*0.386
        inner_plannets = pygame.Rect((X_adjust-0.5*size_inner), (Y_adjust-0.5*size_inner), size_inner, size_inner)
        pygame.draw.ellipse(SCREEN, (color_inner_blur), inner_plannets, int(line_with_inner))
    
    #outer plannets

    #object tracing
    trace_time_Jupiter = calculate_tracers(Semimajor_axis_Jupiter, orbital_period_Jupiter)
    trace_time_Saturn = calculate_tracers(Semimajor_axis_Saturn, orbital_period_Saturn)
    trace_time_Uranus = calculate_tracers(Semimajor_axis_Uranus, orbital_period_Uranus)
    trace_time_Neptune = calculate_tracers(Semimajor_axis_Neptune, orbital_period_Neptune)


    #object scaling
    size_Jupiter_adjusted = object_size(size_Jupiter, size_Jupiter_min)
    size_Saturn_adjusted = object_size(size_Saturn, size_Saturn_min)
    size_Uranus_adjusted = object_size(size_Uranus, size_Uranus_min)
    size_Neptune_adjusted = object_size(size_Neptune, size_Neptune_min)


    for i in range(0, int(orbital_period_Jupiter), int(trace_time_Jupiter)):
        draw_object_in_orbit(i, eccentricity_Jupiter, Semimajor_axis_Jupiter, mean_motion_Jupiter, delay_Jupiter, color_trace, 1, False, Jupiter_periapsis_adjustment)
    draw_object_in_orbit(t+delay_Jupiter, eccentricity_Jupiter, Semimajor_axis_Jupiter, mean_motion_Jupiter, delay_Jupiter, color_Jupiter, size_Jupiter_adjusted, True, Jupiter_periapsis_adjustment)
    for i in range(0, int(orbital_period_Saturn), int(trace_time_Saturn)):
        draw_object_in_orbit(i, eccentricity_Saturn, Semimajor_axis_Saturn, mean_motion_Saturn, 0, color_trace, 1, False, Saturn_periapsis_adjustment)
    draw_object_in_orbit(t+delay_Saturn, eccentricity_Saturn, Semimajor_axis_Saturn, mean_motion_Saturn, delay_Saturn, color_Saturn, size_Saturn_adjusted, True, Saturn_periapsis_adjustment)
    for i in range(0, int(orbital_period_Uranus), int(trace_time_Uranus)):
        draw_object_in_orbit(i, eccentricity_Uranus, Semimajor_axis_Uranus, mean_motion_Uranus, 0, color_trace, 1, False, Uranus_periapsis_adjustment)
    draw_object_in_orbit(t+delay_Uranus, eccentricity_Uranus, Semimajor_axis_Uranus, mean_motion_Uranus, delay_Uranus, color_Uranus, size_Uranus_adjusted, True, Uranus_periapsis_adjustment)
    for i in range(0, int(orbital_period_Neptune), int(trace_time_Neptune)):
        draw_object_in_orbit(i, eccentricity_Neptune, Semimajor_axis_Neptune, mean_motion_Neptune, 0, color_trace, 1, False, Neptune_periapsis_adjustment)
    draw_object_in_orbit(t+delay_Neptune, eccentricity_Neptune, Semimajor_axis_Neptune, mean_motion_Neptune, delay_Neptune, color_Neptune, size_Neptune_adjusted, True, Neptune_periapsis_adjustment)



    
    
    #Sol
    if scale > 0:
        size_Sol_adjusted = object_size(size_Sol, size_Sol_min)
        if size_Sol_adjusted<5:
            size_Sol_adjusted = 5
        pygame.draw.circle(SCREEN, (255, 214, 74), (X_adjust, Y_adjust), size_Sol_adjusted)



    #quit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if scale/(1e8) >= 4:
            if event.type == pygame.MOUSEWHEEL:
                if scale/(1e9) <=4.5:
                    scale -= 100000000*event.y
                if scale/(1e9) > 4.5:
                    scale -= 500000000*event.y
                
        if scale/(1e8) <= 4:
            scale = 4e8
        if scale/(1e8) > 450:
            scale = 450e8
        print(scale/1e8)
            
    pygame.display.update()

pygame.quit()