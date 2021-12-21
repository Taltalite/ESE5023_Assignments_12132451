Program Main
USE Matrix_multip_module
Implicit none

integer :: f1,f2,f3,i,j,m_row,m_col,n_row,n_col
real(8),dimension(:,:),allocatable :: M_matrix,N_matrix,res_matrix
CHARACTER(LEN=*), PARAMETER  :: FMT_M = "(*(F6.2))"
CHARACTER(LEN=*), PARAMETER  :: FMT_N = "(*(F6.2))"
CHARACTER(LEN=*), PARAMETER  :: FMT_RES = "(*(F9.2))"

f1 = 50
f2 = 54
f3 = 58

m_row = 5
m_col = 3
n_row = 3
n_col = 5

open(unit=f1, file='./fortran_demo1/M.dat', status='old')
open(unit=f2, file='./fortran_demo1/N.dat',status='old')
open(unit=f3, file='./MN.dat',status='replace')

allocate(M_matrix(m_col,m_row), N_matrix(n_col,n_row)) 

do i = 1 ,m_row
    read(f1,*) M_matrix(:,i)
enddo

do i=1,n_row
    read(f2,*) N_matrix(:,i)
enddo

close(f2)
close(f1)

write(*,*) "matrix M:"

do i=1,m_row
    write(*,FMT_M) M_matrix(:,i)
enddo

write(*,*) "matrix N:"

do i=1,n_row
    write(*,FMT_N) N_matrix(:,i)
enddo


allocate(res_matrix(m_row,n_col)) 
call Matrix_multip(M_matrix,N_matrix,res_matrix)
write(*,*) "result of M*N:"
do i=1,m_row
    write(f3,FMT_RES) res_matrix(:,i)
    write(*,FMT_RES) res_matrix(:,i)
enddo


deallocate(M_matrix)
deallocate(N_matrix)
deallocate(res_matrix)

End Program Main





