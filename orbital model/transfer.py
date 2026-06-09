import data, func, math



def transfer_date(current_time, plannet_nr_1, plannet_nr_2,  eccentricity_1, Semimajor_axis_1, mean_motion_1, 
                  P_adjust_1, delay_1, eccentricity_2, Semimajor_axis_2, mean_motion_2, P_adjust_2, delay_2):
    if plannet_nr_1 < plannet_nr_2:
        transfer = 0
    else:
        transfer = 1
    launch_time = current_time
    #print(f"start time: {launch_time}")

    
    loop = True
    while loop:
        launch = func.solve_angle_and_range(launch_time, eccentricity_1, Semimajor_axis_1, mean_motion_1)
        launch_angle = launch[0]
        launch_range = launch[1]
        arival_angle = launch_angle - P_adjust_1 + P_adjust_2 + math.pi
        arival = func.data_from_angle(arival_angle, eccentricity_2, mean_motion_2, Semimajor_axis_2)
        arival_range = arival[0]
        if transfer == 0:
            transfer_elipse = func.elipse_calculator(launch_range, arival_range)
        elif transfer == 1:
            transfer_elipse = func.elipse_calculator(arival_range, launch_range)
        transfer_time = transfer_elipse[0]
        arival_time = launch_time + (transfer_time * 0.5)
        #print(f"launch_time = {launch_time},   arival_time = {arival_time}")
        location_2 = func.solve_angle_and_range(arival_time+delay_2, eccentricity_2, Semimajor_axis_2, mean_motion_2)
        angle_target = location_2[0]
        
        if angle_target > (2*math.pi):
            angle_target -= 2*math.pi

        if arival_angle > (2*math.pi):
            arival_angle -= 2*math.pi

        dif_angle = abs(arival_angle - angle_target)
        
        if dif_angle > math.pi:
            dif_angle -= math.pi

        #print(f"arival: {arival_angle},  target: {angle_target},  dif: {dif_angle}")

        delta_mean_motion = abs(mean_motion_1 - mean_motion_2)

        if dif_angle < 0.0175:
            if transfer == 0:
                periapsis = launch_range
                apoapsis = location_2
                angle = launch_angle + P_adjust_1
            else:
                periapsis = location_2
                apoapsis = launch_range
                angle = arival_range - P_adjust_2
            loop = False
            return launch_time, angle, periapsis, apoapsis
        elif dif_angle < delta_mean_motion:
            launch_time += 0.1
        else:
            launch_time += 1






launch_data = transfer_date(285, data.Earth_plannet_nr, data.Mars_plannet_nr, data.eccentricity_Earth, data.Semimajor_axis_Earth, data.mean_motion_Earth, data.Earth_periapsis_adjustment
              , data.delay_Earth, data.eccentricity_Mars, data.Semimajor_axis_Mars, data.mean_motion_Mars, data.Mars_periapsis_adjustment, data.delay_Mars)


print(f"date is {launch_data[0]} from now")
print(f"angle is {launch_data[1]} rads")
