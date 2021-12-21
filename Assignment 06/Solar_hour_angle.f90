!-----------------------------------
! This is a module, Solar_hour_angle
!-----------------------------------
MODULE Solar_hour_angle_module
    CONTAINS

    subroutine Solar_hour_angle(days,LST,lon,TZ,h)

    implicit none

    real(8), intent(in) :: lon, TZ, LST     
    integer, intent(in) :: days      
    real(8), intent(out) :: h
    real(8) :: pi,gamma, EoT, Offset, LST_corrected

    pi = 3.1415926

    gamma = 2*pi/365*(days-1+(LST-12)/24)

    EoT = 229.18*(0.000075+0.001868*cos(gamma)-0.032077*sin(gamma)-0.014615*cos(2*gamma)-0.040849*sin(2*gamma))

    Offset = EoT + 4*(lon - 15*TZ)

    LST_corrected = LST + Offset/60

    h = 15*(LST_corrected - 12)
    
    end subroutine Solar_hour_angle

end MODULE Solar_hour_angle_module