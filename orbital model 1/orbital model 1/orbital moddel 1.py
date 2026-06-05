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
import data


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
    t += 0.5
    #t = 152

    #inner plannets
    if scale <= 4.5e9:
        #object scaling
        size_Mars_adjusted = object_size(data.size_Mars, data.size_Mars_min)
        size_Earth_adjusted = object_size(data.size_Earth, data.size_Earth_min)
        size_Venus_adjusted = object_size(data.size_Venus, data.size_Venus_min)
        size_Mercury_adjusted = object_size(data.size_Mercury, data.size_Mercury_min)

        #object tracing
        trace_time_Mars = calculate_tracers(data.Semimajor_axis_Mars, data.orbital_period_Mars)
        trace_time_Earth = calculate_tracers(data.Semimajor_axis_Earth, data.orbital_period_Earth)
        trace_time_Venus = calculate_tracers(data.Semimajor_axis_Venus, data.orbital_period_Venus)
        trace_time_Mercury = calculate_tracers(data.Semimajor_axis_Mercury, data.orbital_period_Mercury)
        
        
        #Mars
        for i in range (0, int(data.orbital_period_Mars), int(trace_time_Mars)):
            draw_object_in_orbit(i, data.eccentricity_Mars, data.Semimajor_axis_Mars, data.mean_motion_Mars, 0, color_trace, 1, False, data.Mars_periapsis_adjustment)
        draw_object_in_orbit(t, data.eccentricity_Mars, data.Semimajor_axis_Mars, data.mean_motion_Mars, data.delay_Mars, data.color_Mars, size_Mars_adjusted, True, data.Mars_periapsis_adjustment)

        #Earth
        for i in range(0, int(data.orbital_period_Earth), int(trace_time_Earth)):
            draw_object_in_orbit(i, data.eccentricity_Earth, data.Semimajor_axis_Earth, data.mean_motion_Earth, 0, color_trace, 1, False, rotation)
        draw_object_in_orbit(t, data.eccentricity_Earth, data.Semimajor_axis_Earth, data.mean_motion_Earth, data.delay_Earth, data.color_Earth, size_Earth_adjusted, True, rotation)

        #Venus
        for i in range(0,int(data.orbital_period_Venus), int(trace_time_Venus)):
            draw_object_in_orbit(i, data.eccentricity_Venus, data.Semimajor_axis_Venus, data.mean_motion_Venus, 0, color_trace, 1, False, data.Venus_periapsis_adjustment)
        draw_object_in_orbit(t, data.eccentricity_Venus, data.Semimajor_axis_Venus, data.mean_motion_Venus, data.delay_Venus, data.color_Venus, size_Venus_adjusted, True, data.Venus_periapsis_adjustment)

        #Mercury
        for i in range(0,int(data.orbital_period_Mercury), int(trace_time_Mercury)):
            draw_object_in_orbit(i, data.eccentricity_Mercury, data.Semimajor_axis_Mercury, data.mean_motion_Mercury, 0, color_trace, 1, False, data.Mercury_periapsis_adjustment)
        draw_object_in_orbit(t, data.eccentricity_Mercury, data.Semimajor_axis_Mercury, data.mean_motion_Mercury, data.delay_Mercury, data.color_Mercury, size_Mercury_adjusted, True, data.Mercury_periapsis_adjustment)
    #inner blur
    else:
        size_inner = data.Apoapsis_Mars/scale*2
        line_with_inner = size_inner*0.386
        inner_plannets = pygame.Rect((X_adjust-0.5*size_inner), (Y_adjust-0.5*size_inner), size_inner, size_inner)
        pygame.draw.ellipse(SCREEN, (color_inner_blur), inner_plannets, int(line_with_inner))
    
    #outer plannets

    #object tracing
    trace_time_Jupiter = calculate_tracers(data.Semimajor_axis_Jupiter, data.orbital_period_Jupiter)
    trace_time_Saturn = calculate_tracers(data.Semimajor_axis_Saturn, data.orbital_period_Saturn)
    trace_time_Uranus = calculate_tracers(data.Semimajor_axis_Uranus, data.orbital_period_Uranus)
    trace_time_Neptune = calculate_tracers(data.Semimajor_axis_Neptune, data.orbital_period_Neptune)


    #object scaling
    size_Jupiter_adjusted = object_size(data.size_Jupiter, data.size_Jupiter_min)
    size_Saturn_adjusted = object_size(data.size_Saturn, data.size_Saturn_min)
    size_Uranus_adjusted = object_size(data.size_Uranus, data.size_Uranus_min)
    size_Neptune_adjusted = object_size(data.size_Neptune, data.size_Neptune_min)


    for i in range(0, int(data.orbital_period_Jupiter), int(trace_time_Jupiter)):
        draw_object_in_orbit(i, data.eccentricity_Jupiter, data.Semimajor_axis_Jupiter, data.mean_motion_Jupiter, data.delay_Jupiter, color_trace, 1, False, data.Jupiter_periapsis_adjustment)
    draw_object_in_orbit(t, data.eccentricity_Jupiter, data.Semimajor_axis_Jupiter, data.mean_motion_Jupiter, data.delay_Jupiter, data.color_Jupiter, size_Jupiter_adjusted, True, data.Jupiter_periapsis_adjustment)
    for i in range(0, int(data.orbital_period_Saturn), int(trace_time_Saturn)):
        draw_object_in_orbit(i, data.eccentricity_Saturn, data.Semimajor_axis_Saturn, data.mean_motion_Saturn, 0, color_trace, 1, False, data.Saturn_periapsis_adjustment)
    draw_object_in_orbit(t, data.eccentricity_Saturn, data.Semimajor_axis_Saturn, data.mean_motion_Saturn, data.delay_Saturn, data.color_Saturn, size_Saturn_adjusted, True, data.Saturn_periapsis_adjustment)
    for i in range(0, int(data.orbital_period_Uranus), int(trace_time_Uranus)):
        draw_object_in_orbit(i, data.eccentricity_Uranus, data.Semimajor_axis_Uranus, data.mean_motion_Uranus, 0, color_trace, 1, False, data.Uranus_periapsis_adjustment)
    draw_object_in_orbit(t, data.eccentricity_Uranus, data.Semimajor_axis_Uranus, data.mean_motion_Uranus, data.delay_Uranus, data.color_Uranus, size_Uranus_adjusted, True, data.Uranus_periapsis_adjustment)
    for i in range(0, int(data.orbital_period_Neptune), int(trace_time_Neptune)):
        draw_object_in_orbit(i, data.eccentricity_Neptune, data.Semimajor_axis_Neptune, data.mean_motion_Neptune, 0, color_trace, 1, False, data.Neptune_periapsis_adjustment)
    draw_object_in_orbit(t, data.eccentricity_Neptune, data.Semimajor_axis_Neptune, data.mean_motion_Neptune, data.delay_Neptune, data.color_Neptune, size_Neptune_adjusted, True, data.Neptune_periapsis_adjustment)



    
    
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