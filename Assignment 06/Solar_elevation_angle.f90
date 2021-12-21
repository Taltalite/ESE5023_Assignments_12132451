Program Solar_elevation_angle

    USE Declination_angle_module
    USE Solar_hour_angle_module
    
    implicit none
    
    real(8), parameter :: pi = 3.1415926536
    real(8) :: lat, lon, TZ, LST, h, angle, SEA, toarc
    integer :: days,year,month,day
    integer,dimension(12) :: month_array,month_leap_array

    month_array=(/31,28,31,30,31,30,31,31,30,31,30,31/)
    month_leap_array=(/31,29,31,30,31,30,31,31,30,31,30,31/)

    toarc = pi / 180

    lat = 22.542883
    lon = 114.062996
    TZ = 8.0
    LST = 10.53333
    year = 2021
    month = 12
    day = 31

    ! check if year is a leap year
    if ((mod(year,400)==0) .or. (mod(year,4)==0 .and. mod(year,100)/=0)) then
        days = sum(month_leap_array(:month-1)) + day
    else
        days = sum(month_array(:month-1)) + day
    end if

    call Declination_angle(days, angle)

    call Solar_hour_angle(days,LST, lon, TZ, h)

    SEA = asin(sin(lat*toarc)*sin(angle*toarc)+cos(lat*toarc)*cos(angle*toarc)*cos(h*toarc))*1/toarc
    write(*,'(a6,f7.3)') 'SEA = ', SEA

End Program Solar_elevation_angle