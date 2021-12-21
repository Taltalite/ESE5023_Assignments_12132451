FC=gfortran
EXE_Matrix=Main.x 
EXE_Solar=Solar_elevation_angle.x
OBJ_Matrix=Main.o Matrix_multip_module.o 
OBJ_Solar=Solar_elevation_angle.o
LIB_Solar_OBJ=Solar_hour_angle.o Declination_angle.o
LIB_Solar=libsea.a
MOD_Matrix=matrix_multip_module.mod 
MOD_Solar=declination_angle_module.mod solar_hour_angle_module.mod
SRC_Matrix=Matrix_multip_module.f90 Main.f90
SRC_Solar=Declination_angle.f90 Solar_hour_angle.f90 Solar_elevation_angle.f90

CLEAN=$(EXE_Matrix) $(EXE_Solar) $(OBJ_Matrix) $(OBJ_Solar) $(LIB_Solar_OBJ) $(LIB_Solar) $(MOD_Matrix) $(MOD_Solar)

all:$(EXE_Matrix) $(EXE_Solar)

$(EXE_Matrix):$(OBJ_Matrix)
	$(FC) $^ -o $@

$(OBJ_Matrix):$(SRC_Matrix)
	$(FC) -c $^

$(EXE_Solar):$(OBJ_Solar) $(LIB_Solar)
	$(FC) $^ -o $@

$(LIB_Solar):$(LIB_Solar_OBJ)
	ar cr $@ $^

$(OBJ_Solar):$(SRC_Solar)
	$(FC) -c $^

clean:
	rm -rf $(CLEAN)
