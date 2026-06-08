#agenda
#calculate the correct periapsis adjustments
#in seperate file make a better code for intercepts
# make the moon
# make moons, i dont know how many i expect. not a priority
# make the camera move 

#bugs


#imports
import pygame, math, time

#related files
import data, func, UI

pygame.init()

#window details
SCREEN_WITH = data.SCREEN_with
SCREEN_HEIGHT = data.SCREEN_height
SCREEN = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT))

t = 0
scale = 10e8
X_move = 0
Y_move = 0
scale_variable_min = 10e8/scale
tracking = True
gear = 0
freeze = False
help_status = False












run =  True
while run == True:
    X_move_adjusted = X_move/scale
    Y_move_adjusted = Y_move/scale
    scale_variable_min = 1 * 1e9/scale

    events = pygame.event.get()
    SCREEN.fill((0, 0, 0))

    if freeze:
        speed = 0
    else:
        speed = func.speed(gear)
    t += speed
    #t = 152

    #inner plannets
    if scale <= 4.5e9:
        #object scaling
        
        
        
        #Mars
        func.plannet(SCREEN, scale, t, X_move_adjusted, Y_move_adjusted, data.size_Mars, data.size_Mars_min, data.Semimajor_axis_Mars, 
        data.orbital_period_Mars, data.eccentricity_Mars, data.mean_motion_Mars, data.Mars_periapsis_adjustment, data.color_Mars, data.delay_Mars)
        
        #Earth
        func.plannet(SCREEN, scale, t, X_move_adjusted, Y_move_adjusted, data.size_Earth, data.size_Earth_min, data.Semimajor_axis_Earth, 
        data.orbital_period_Earth, data.eccentricity_Earth, data.mean_motion_Earth, data.Earth_periapsis_adjustment, data.color_Earth, data.delay_Earth)

        #Venus
        func.plannet(SCREEN, scale, t, X_move_adjusted, Y_move_adjusted, data.size_Venus, data.size_Venus_min, data.Semimajor_axis_Venus, 
        data.orbital_period_Venus, data.eccentricity_Venus, data.mean_motion_Venus, data.Venus_periapsis_adjustment, data.color_Venus, data.delay_Venus)

        #Mercury
        func.plannet(SCREEN, scale, t, X_move_adjusted, Y_move_adjusted, data.size_Mercury, data.size_Mercury_min, data.Semimajor_axis_Mercury, 
        data.orbital_period_Mercury, data.eccentricity_Mercury, data.mean_motion_Mercury, data.Mercury_periapsis_adjustment, data.color_Mercury, data.delay_Mercury)



    #inner blur
    else:
        size_inner = data.Apoapsis_Mars/scale*2
        line_with_inner = size_inner*0.386
        inner_plannets = pygame.Rect((data.X_adjust-0.5*size_inner+X_move_adjusted), (data.Y_adjust-0.5*size_inner+Y_move_adjusted), size_inner, size_inner)
        pygame.draw.ellipse(SCREEN, (data.color_inner_blur), inner_plannets, int(line_with_inner))
    
    #outer plannets

    #Jupiter
    func.plannet(SCREEN, scale, t, X_move_adjusted, Y_move_adjusted, data.size_Jupiter, data.size_Jupiter_min, data.Semimajor_axis_Jupiter, 
    data.orbital_period_Jupiter, data.eccentricity_Jupiter, data.mean_motion_Jupiter, data.Jupiter_periapsis_adjustment, data.color_Jupiter, data.delay_Jupiter)
    #Saturn
    func.plannet(SCREEN, scale, t, X_move_adjusted, Y_move_adjusted, data.size_Saturn, data.size_Saturn_min, data.Semimajor_axis_Saturn, 
    data.orbital_period_Saturn, data.eccentricity_Saturn, data.mean_motion_Saturn, data.Saturn_periapsis_adjustment, data.color_Saturn, data.delay_Saturn)
    #Uranus
    func.plannet(SCREEN, scale, t, X_move_adjusted, Y_move_adjusted, data.size_Uranus, data.size_Uranus_min, data.Semimajor_axis_Uranus, 
    data.orbital_period_Uranus, data.eccentricity_Uranus, data.mean_motion_Uranus, data.Uranus_periapsis_adjustment, data.color_Uranus, data.delay_Uranus)
    #Neptune
    func.plannet(SCREEN, scale, t, X_move_adjusted, Y_move_adjusted, data.size_Neptune, data.size_Neptune_min, data.Semimajor_axis_Neptune, 
    data.orbital_period_Neptune, data.eccentricity_Neptune, data.mean_motion_Neptune, data.Neptune_periapsis_adjustment, data.color_Neptune, data.delay_Neptune)

    #Sol
    
    size_Sol_adjusted = func.object_size(data.size_Sol, data.size_Sol_min, scale)
    if size_Sol_adjusted<5:
        size_Sol_adjusted = 5
    pygame.draw.circle(SCREEN, (255, 214, 74), (data.X_adjust+X_move_adjusted, data.Y_adjust+Y_move_adjusted), size_Sol_adjusted)

    #Tracking
    if X_move == 0 and Y_move == 0:
        Tracking = True
    else:
        Tracking = False
    
    if not Tracking:
        zoom = pygame.Rect((data.X_adjust, data.Y_adjust, 4, 4))
        pygame.draw.rect(SCREEN, (255, 1, 1), zoom)




    #quit function
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        
        #zooming function
        if scale/(1e8) >= 4:
            if event.type == pygame.MOUSEWHEEL:
                if scale/(1e9) <=4.5:
                    scale -= 100000000*event.y
                if scale/(1e9) > 4.5:
                    scale -= 500000000*event.y            
        if scale/(1e8) <= 4:
            scale = 4e8
        if scale/(1e8) > 350:
            scale = 350e8
        #print(scale/1e8)


        

    #moving function
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        if key[pygame.K_d] == True:
            X_move -= data.move_speed * scale
        if key[pygame.K_a] == True:
            X_move += data.move_speed * scale
        Y_move += data.move_speed * scale
    elif key[pygame.K_s] == True:
        if key[pygame.K_d] == True:
            X_move -= data.move_speed * scale
        if key[pygame.K_a] == True:
            X_move += data.move_speed * scale
        Y_move -= data.move_speed * scale
    elif key[pygame.K_d] == True:
        X_move -= data.move_speed * scale
    elif key[pygame.K_a] == True:
        X_move += data.move_speed * scale

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                gear = func.gear_up(gear)
            if event.key == pygame.K_q:
                gear = func.gear_down(gear)
            if event.key == pygame.K_SPACE:
                if freeze:
                    freeze = False
                else:
                    freeze = True
            if event.key == pygame.K_h:
                if help_status:
                    help_status = False
                else:
                    help_status = True



    #UI display
    UI.speed(SCREEN, speed, freeze)
    UI.help(SCREEN, help_status)
    UI.date(SCREEN, t)






    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(data.framerate)
pygame.quit()