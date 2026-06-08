import data
import math
import pygame




def object_size(max, min, scale):
    scale_variable_min = 10e8/scale
    size = max*scale_variable_min
    if size<min:
        size = min
    return(size)

def calculate_tracers(a, T, scale_variable_min):
    tracers = (2*math.pi*a)/(10216870687/scale_variable_min)
    trace_time = T/tracers
    if trace_time<1:
        trace_time = 1
    return(trace_time)

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

def draw_object_in_orbit(SCREEN, t, e, a, n, delay, color, size, important, p_adjust, scale, X_move_adjusted, Y_move_adjusted):
    object_data = solve_angle_and_range((t+delay), e, a, n)
    X_object = (math.cos(2*math.pi-object_data[0]+p_adjust) * object_data[1])/ scale
    Y_object = (math.sin(2*math.pi-object_data[0]+p_adjust) * object_data[1])/ scale
    
    #adding potential movement
    X = data.X_adjust + X_move_adjusted
    Y = data.Y_adjust + Y_move_adjusted
    #if important:
    #    pygame.draw.circle(SCREEN, (0, 0, 0), ((X_object + X_adjust), (Y_object + Y_adjust)), size+3)
    pygame.draw.circle(SCREEN, (color), ((X_object + X), (Y_object + Y)), size)

def gear_up(gear):
    gear += 1
    if gear > data.max_gear:
        gear = data.max_gear
    return gear

def gear_down(gear):
    gear -= 1
    if gear < data.min_gear:
        gear = data.min_gear
    return gear

def speed(gear):
    if gear == 0:
        speed = 0
    elif gear > 0:
        speed = data.gears[gear-1]
    elif gear < 0:
        gear = gear * -1
        speed = (data.gears[gear-1]) * -1
    return(speed)
    
def plannet(SCREEN, scale, t, X_move_adjusted, Y_move_adjusted, size_max, size_min, a, T, e, n, P_adjust, color, delay):
    scale_variable_min = 10e8/scale

    size = object_size(size_max, size_min, scale)
    trace_time = calculate_tracers(a, T, scale_variable_min)
    
    for i in range (0, int(T), int(trace_time)):        
        
        l_data = solve_angle_and_range((i), e, a, n)

        X_object = (math.cos(2*math.pi-l_data[0]+P_adjust) * l_data[1])/ scale
        Y_object = (math.sin(2*math.pi-l_data[0]+P_adjust) * l_data[1])/ scale
        X = data.X_adjust + X_move_adjusted
        Y = data.Y_adjust + Y_move_adjusted

        pygame.draw.circle(SCREEN, (data.color_trace), ((X_object + X), (Y_object + Y)), 1)
    
    l_data = solve_angle_and_range((t+delay), e, a, n)
    
    X_object = (math.cos(2*math.pi-l_data[0]+P_adjust) * l_data[1])/ scale
    Y_object = (math.sin(2*math.pi-l_data[0]+P_adjust) * l_data[1])/ scale
    
    X = data.X_adjust + X_move_adjusted
    Y = data.Y_adjust + Y_move_adjusted

    pygame.draw.circle(SCREEN, (color), ((X_object + X), (Y_object + Y)), size)

def track(nr ,t, scale):
    if nr == 1:
        delay = data.delay_Mercury
        p_adjust = data.Mercury_periapsis_adjustment
        e = data.eccentricity_Mercury
        a = data.Semimajor_axis_Mercury
        n = data.mean_motion_Mercury
    elif nr == 2:
        delay = data.delay_Venus
        p_adjust = data.Venus_periapsis_adjustment
        e = data.eccentricity_Venus
        a = data.Semimajor_axis_Venus
        n = data.mean_motion_Venus
    elif nr == 3:
        delay = data.delay_Earth
        p_adjust = data.Earth_periapsis_adjustment
        e = data.eccentricity_Earth
        a = data.Semimajor_axis_Earth
        n = data.mean_motion_Earth      
    elif nr == 4:
        delay = data.delay_Mars
        p_adjust = data.Mars_periapsis_adjustment
        e = data.eccentricity_Mars
        a = data.Semimajor_axis_Mars
        n = data.mean_motion_Mars
    elif nr == 5:
        delay = data.delay_Jupiter
        p_adjust = data.Jupiter_periapsis_adjustment
        e = data.eccentricity_Jupiter
        a = data.Semimajor_axis_Jupiter
        n = data.mean_motion_Jupiter
    elif nr == 6:
        delay = data.delay_Saturn
        p_adjust = data.Saturn_periapsis_adjustment
        e = data.eccentricity_Saturn
        a = data.Semimajor_axis_Saturn
        n = data.mean_motion_Saturn
    elif nr == 7:
        delay = data.delay_Uranus
        p_adjust = data.Uranus_periapsis_adjustment
        e = data.eccentricity_Uranus
        a = data.Semimajor_axis_Uranus
        n = data.mean_motion_Uranus
    elif nr == 8:
        delay = data.delay_Neptune
        p_adjust = data.Neptune_periapsis_adjustment
        e = data.eccentricity_Neptune
        a = data.Semimajor_axis_Neptune
        n = data.mean_motion_Neptune

    object_data = solve_angle_and_range((t+delay), e, a, n)
    X_object = (math.cos(2*math.pi-object_data[0]+p_adjust) * object_data[1])/ scale
    Y_object = (math.sin(2*math.pi-object_data[0]+p_adjust) * object_data[1])/ scale
    
    return(X_object, Y_object)