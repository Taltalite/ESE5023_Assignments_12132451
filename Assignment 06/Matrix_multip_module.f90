!-----------------------------------
! This is a subroutine, Matrix_multip
!-----------------------------------
MODULE Matrix_multip_module
    CONTAINS
    subroutine Matrix_multip(m,n,res)

        implicit none
        
        real(8),dimension(:,:),allocatable,intent(INOUT) :: m,n,res
        integer :: m_row,m_col,n_row,n_col,res_row,res_col,i,j,k
        real(8) :: temp
        if ( allocated(m) ) then
            write(*,*) "subroutine allocated!"

            m_col = size(m,dim=1)
            m_row = size(m,dim=2)
            n_col = size(n,dim=1)
            n_row = size(n,dim=2)
            res_row = m_row
            res_col = n_col

            do i=1,m_row
                do j=1,n_col
                    temp = 0.0
                    do k=1,m_col
                        temp = temp + m(k,i)*n(j,k)
                    enddo
                    res(j,i) = temp
                enddo
            enddo
        else
            write(*,*) "subroutine not allocated!"
        end if
    end subroutine Matrix_multip
end MODULE Matrix_multip_module