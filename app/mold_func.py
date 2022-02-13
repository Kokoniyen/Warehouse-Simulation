import os
import uuid
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def get_temp_varies(
    Density=1.205,
    Specific_heat=400,
    Heat_conductivity_of_walls=6.001,
    Initial_Temperature=35,
    Length=10,
    Breadth=10,
    Height=10,
):
    """

    rho(float): density kg/m3
    cp(int): specific heat kg/(J*K)
    KK1(float): heat conductivity of walls W/(m*k)
    Temp_1(int): initial ambient temp (C)
    Nt(int): 5 hours converted to secconds
    c(int): speed
    C_num(int): Courant number Ninad: changed from C to C_num just in case Python does not recognize small/big case for var names
    dt(int): timestep between iterations
    """

    T_initial = Initial_Temperature * (9 / 5) + 32  # initial ambient temp (F)
    T_outside = Initial_Temperature * (9 / 5) + 32  # external temperature (F)

    # number of iterations
    Nt = 5 * 3600  # 5 hours converted to secconds
    Nx = (Length * 2) + 1
    Ny = (Breadth * 2) + 1
    Nz = (Height * 2) + 1

    dx = Length / (Nx - 1)
    dy = Length / (Nx - 1)
    dz = Length / (Nx - 1)

    # thermal conductivity of facility
    #   Ninad: I believe this sets the conductivity along the boundaries to a different number

    K = 0.02 * np.ones((Nx, Ny, Nz)) + 0.0257 * 100
    K[0, :, :] = Heat_conductivity_of_walls
    # thermal conductivity for x-dimension
    K[-1, :, :] = Heat_conductivity_of_walls
    # Ninad: '-1' indexes to the last element
    K[:, 0, :] = Heat_conductivity_of_walls
    # thermal conductivity for y-dimension
    K[:, -1, :] = Heat_conductivity_of_walls
    K[:, :, 0] = Heat_conductivity_of_walls
    # thermal conductivity for z-dimension
    K[:, :, -1] = Heat_conductivity_of_walls

    Th_Conduc_wood = 0.12
    K[2:3, 1:4, :] = Th_Conduc_wood
    # Stack 1 coordinates in x,y,z
    K[3:4, 1:5, 0:8] = Th_Conduc_wood
    # Stack 2 coordinates in x,y,z
    K[5:6, 1:5, 0:8] = Th_Conduc_wood
    # Stack 3 coordinates in x,y,z
    K[3:4, 4:5, 0:8] = Th_Conduc_wood
    # Stack 4 coordinates in x,y,z
    K[0:1, 5:6, 0:8] = Th_Conduc_wood
    # Stack 5 coordinates in x,y,z
    K[7:9, 7:8, 0:8] = Th_Conduc_wood
    # Stack 6 coordinates in x,y,z
    K[2:4, 5:6, 0:8] = Th_Conduc_wood
    # Stack 7 coordinates in x,y,z
    K[7:9, 7:9, 0:8] = Th_Conduc_wood
    # Stack 8 coordinates in x,y,z

    # Fabiano: satisfy CFL condition for simulation stability
    c = 2  # speed
    C_num = 0.5  # Courant number Ninad: changed from C to C_num just in case Python does not recognize small/big case for var names
    dt = 1  # timestep between iterations

    # field variables
    Tn = np.zeros((Nx, Ny, Nz))
    x = np.linspace(
        0, Length, Nx
    )  # generates Nx evenly spaced pts between values 0 and Lx
    y = np.linspace(0, Breadth, Ny)
    z = np.linspace(0, Height, Nz)
    [Xm, Ym, Zm] = np.meshgrid(
        x, y, z
    )  # Ninad: m represents "mesh", changed var name again to avoid capitalization issues

    t = 0
    for n in range(
        Nt
    ):  # Ninad: python "range" excludes the final number, i.e. range Nt counts to 0...Nt-1
        t = t + dt  # time increment

        # print('n:', n, 'of ', Nt-1)
        Tc = Tn  # save the temperature for later use
        Tc_i_minus = np.roll(Tc, -1, 1)  # i-1,j,k
        Tc_i_plus = np.roll(Tc, 1, 1)  # i+1,j,k
        Tc_j_minus = np.roll(Tc, -1, 2)  # i,j-1,k
        Tc_j_plus = np.roll(Tc, 1, 2)  # i,j+1,k
        Tc_k_minus = np.roll(Tc, -1, 0)  # i,j,k-1
        Tc_k_plus = np.roll(Tc, 1, 0)  # i,j,k+1

        # perform the calculation (actual calculation is only for 1...Nx-2 or Ny or Nz)
        Tn = Tc + dt * (K / Density / Specific_heat) * (
            (Tc_i_plus - 2 * Tc + Tc_i_minus) / (dx * dx)
            + (Tc_j_plus - 2 * Tc + Tc_j_minus) / (dy * dy)
            + (Tc_k_plus - 2 * Tc + Tc_k_minus) / (dz * dz)
        )

        # Tbar = np.mean(Tn) # Ninad: commented this out since it wasn't being used later
        Tn[:, :, -1] = T_initial + dt * 1000 / (Density * Specific_heat)

        # boundary conditions
        Tn[0, :, :] = Tn[1, :, :]  # Constraint for boundary along x-axis
        Tn[-1, :, :] = Tn[-2, :, :]
        Tn[:, 0, :] = Tn[:, 1, :]  # Constraint for boundary along y-axis
        Tn[:, -1, :] = Tn[:, -2, :]
        Tn[:, :, 0] = T_initial
        # Constraint Temperature of the floor

    print("Temperature varies between: ", np.min(Tn), " and ", np.max(Tn))
    print("Model computations completed for time t:", t)

    # visualize the output

    riskmap = np.mean(Tn, 1)  # average down y axis

    min_temp = np.min(riskmap)
    max_temp = np.max(riskmap)

    print("Average temp varies between ", min_temp, " to ", max_temp)

    plt.figure(figsize=(7, 6))
    plt.pcolormesh(riskmap)

    image_path = os.path.join("app", "static", str(uuid.uuid4()) + ".png")
    plt.savefig(image_path)

    print("Riskmap generation completed")

    print("/".join(image_path.split("/")[1:]))

    return "/".join(image_path.split("/")[1:])


if __name__ == "__main__":
    get_temp_varies()
