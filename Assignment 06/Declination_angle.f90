!-----------------------------------
! This is a module, Declination_angle
!-----------------------------------
MODULE Declination_angle_module
    CONTAINS
    
    subroutine Declination_angle(days,angle)
        implicit none   
        integer, intent(in)  :: days
        real(8), intent(out)    :: angle
        real(8)                 :: pi,toarc,delta
    
        pi = 3.1415926
        toarc = pi / 180.0
    
        delta = asin(sin(-23.44*toarc)*cos(toarc*(360.0/365.24*(days+10)+(360.0/pi)*0.0167*sin(360.0*(days-2)/365.24)))) * 1/toarc

        angle = delta

    end subroutine Declination_angle 
    
end MODULE Declination_angle_module