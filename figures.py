import matplotlib.pyplot as plt

def create_time_domain_figures(T, t, damped_data, undamped_data, fig_width, fig_height, line_width, label_fontsize, subplot_vspace):
    
    # Create figure
    fig = plt.figure(figsize=(fig_width, fig_height))

    # Create figure title
    plt.suptitle('Time-domain responses to stochastic vertical gust input', \
                 x=0.5, y=.94, fontsize = 15)

    # Set vertical space between subplots
    plt.subplots_adjust(hspace = subplot_vspace)

    # Start plotting all subplots
    ax = plt.subplot(511)
    plt.plot(t, undamped_data[0], linewidth = line_width, label = "Undamped")
    plt.plot(t, damped_data[0], linewidth = line_width, label = "Damped")

    # Create legend above the first subplot and increase line thickness 
    # for legend only
    leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2)
    for legobj in leg.legendHandles:
        legobj.set_linewidth(2.0)

    plt.xticks([]) # Hide the time labels for the upper subplots
    plt.xlim([0,T]) # Remove white space in graph
    plt.ylabel(r"$V$ [m/s]", fontsize = label_fontsize)

    # Do the same for the rest of the graphs, except the legend part 
    # (only 1 legend required)
    plt.subplot(512)
    plt.plot(t, undamped_data[1], linewidth = line_width)
    plt.plot(t, damped_data[1], linewidth = line_width)
    plt.xticks([])
    plt.xlim([0,T])
    plt.ylabel(r"$\alpha$ [rad]", fontsize = label_fontsize)
                         
    plt.subplot(513)
    plt.plot(t, undamped_data[2], linewidth = line_width)
    plt.plot(t, damped_data[2], linewidth = line_width)
    plt.xticks([])
    plt.xlim([0,T])
    plt.ylabel(r"$\theta$ [rad]", fontsize = label_fontsize)

    plt.subplot(514)
    plt.plot(t, undamped_data[3], linewidth = line_width)
    plt.plot(t, damped_data[3], linewidth = line_width)
    plt.xticks([])
    plt.xlim([0,T])
    plt.ylabel(r"$q$ [rad/s]",fontsize = label_fontsize)

    plt.subplot(515)
    plt.plot(t, undamped_data[4], linewidth = line_width)
    plt.plot(t, damped_data[4], linewidth = line_width)
    plt.xlim([0,T])
    plt.ylabel(r"$n_z$ [g-units]", fontsize = label_fontsize)
    plt.xlabel('Time [s]', fontsize = label_fontsize)

    return

def create_aPSD_figures(w, damped_data, undamped_data, fig_width, fig_height, line_width, label_fontsize, subplot_vspace):
    # Create figure
    fig = plt.figure(figsize=(fig_width, fig_height))

    # Create figure title
    plt.suptitle('Analytical Power Spectrum Density functions', \
                 x=0.5, y=.94, fontsize = 15)

    # Set vertical space between subplots
    plt.subplots_adjust(hspace = subplot_vspace)

    # Start plotting all subplots
    ax = plt.subplot(511)
    plt.loglog(w, undamped_data[0], linewidth = line_width, label = "Undamped")
    plt.loglog(w, damped_data[0], linewidth = line_width, label = "Damped")

    # Create legend above the first subplot and increase line thickness 
    # for legend only
    leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.28), ncol=2)
    for legobj in leg.legendHandles:
        legobj.set_linewidth(2.0)

    plt.xticks([]) # Hide the time labels for the upper subplots
    plt.xlim([w[0],w[-1]])
    plt.title(r"$V$", x=0.95, y=.7)
    plt.ylabel(r"$S_{NN}$", fontsize = label_fontsize)

    # Do the same for the rest of the graphs, except the legend part 
    # (only 1 legend required)
    plt.subplot(512)
    plt.loglog(w, undamped_data[1], linewidth = line_width)
    plt.loglog(w, damped_data[1], linewidth = line_width)
    plt.xticks([])
    plt.xlim([w[0],w[-1]])
    plt.title(r"$\alpha$", x=0.95, y=.7)
    plt.ylabel(r"$S_{NN}$", fontsize = label_fontsize)
                         
    plt.subplot(513)
    plt.loglog(w, undamped_data[2], linewidth = line_width)
    plt.loglog(w, damped_data[2], linewidth = line_width)
    plt.xticks([])
    plt.xlim([w[0],w[-1]])
    plt.title(r"$\theta$", x=0.95, y=.7)
    plt.ylabel(r"$S_{NN}$", fontsize = label_fontsize)

    plt.subplot(514)
    plt.loglog(w, undamped_data[3], linewidth = line_width)
    plt.loglog(w, damped_data[3], linewidth = line_width)
    plt.xticks([])
    plt.xlim([w[0],w[-1]])
    plt.title(r"$q$", x=0.95, y=.7)
    plt.ylabel(r"$S_{NN}$",fontsize = label_fontsize)

    plt.subplot(515)
    plt.loglog(w, undamped_data[4], linewidth = line_width)
    plt.loglog(w, damped_data[4], linewidth = line_width)
    plt.xlim([w[0],w[-1]])
    plt.title(r"$n_z$", x=0.95, y=.7)
    plt.ylabel(r"$S_{NN}$", fontsize = label_fontsize)
    plt.xlabel(r"$\omega$ [rad/s]", fontsize = label_fontsize)

def create_ePSD_figures(w_aPSD, w_ePSD, w_pPSD, damped_aPSD_data, undamped_aPSD_data, damped_ePSD_data,
                        undamped_ePSD_data, damped_pPSD_data, undamped_pPSD_data, fig_width, fig_height,
                        line_width, label_fontsize, subplot_vspace):
    # Create figure
    fig = plt.figure(figsize=(fig_width, fig_height))

    # Create figure title
    plt.suptitle('Analytical and Experimental Power Spectrum Density functions', \
                 x=0.5, y=0.98, fontsize = 15)

    # Set vertical space between subplots
    plt.subplots_adjust(hspace = subplot_vspace)

    # Start plotting all subplots
    ax1 = plt.subplot(5,2,1)
    ax1.text(0.5, 1.5, 'Undamped', fontsize=13)
    
    plt.loglog(w_ePSD, undamped_ePSD_data[0], linewidth = line_width, label = "Experimental PSD (fft)")
    plt.loglog(w_pPSD, undamped_pPSD_data[0], linewidth = line_width, label = "Experimental PSD (pwelch)")
    plt.loglog(w_aPSD, undamped_aPSD_data[0], linewidth = line_width, label = "Analytical PSD", color='red')

    # Create legend above the first subplot and increase line thickness 
    # for legend only
    leg = ax1.legend(loc='upper center', bbox_to_anchor=(1, 1.57), ncol=3)
    for legobj in leg.legendHandles:
        legobj.set_linewidth(2.0)

    plt.xticks([]) # Hide the time labels for the upper subplots
    plt.xlim([w_aPSD[0],w_ePSD[-1]])
    plt.title(r"$V$", x=0.95, y=.7)
    plt.ylabel(r"$S_{VV}$", fontsize = label_fontsize)

    ax2 = plt.subplot(5,2,2)
    ax2.text(0.5, 0.04, 'Damped', fontsize=13)
    plt.loglog(w_ePSD, damped_ePSD_data[0], linewidth = line_width)
    plt.loglog(w_pPSD, damped_pPSD_data[0], linewidth = line_width)
    plt.loglog(w_aPSD, damped_aPSD_data[0], linewidth = line_width, color='red')
    plt.xticks([]) # Hide the time labels for the upper subplots
    plt.xlim([w_aPSD[0],w_ePSD[-1]])
    plt.title(r"$V$", x=0.95, y=.7)
    plt.ylabel(r"$S_{VV}$", fontsize = label_fontsize)

    # Do the same for the rest of the graphs, except the legend part 
    # (only 1 legend required)
    plt.subplot(5,2,3)
    plt.loglog(w_ePSD, undamped_ePSD_data[1], linewidth = line_width)
    plt.loglog(w_pPSD, undamped_pPSD_data[1], linewidth = line_width)
    plt.loglog(w_aPSD, undamped_aPSD_data[1], linewidth = line_width, color='red')
    plt.xticks([])
    plt.xlim([w_aPSD[0],w_ePSD[-1]])
    plt.title(r"$\alpha$", x=0.95, y=.7)
    plt.ylabel(r"$S_{\alpha\alpha}$", fontsize = label_fontsize)

    plt.subplot(5,2,4)
    plt.loglog(w_ePSD, damped_ePSD_data[1], linewidth = line_width)
    plt.loglog(w_pPSD, damped_pPSD_data[1], linewidth = line_width)
    plt.loglog(w_aPSD, damped_aPSD_data[1], linewidth = line_width, color='red')
    plt.xticks([])
    plt.xlim([w_aPSD[0],w_ePSD[-1]])
    plt.title(r"$\alpha$", x=0.95, y=.7)
    plt.ylabel(r"$S_{\alpha\alpha}$", fontsize = label_fontsize)
                         
    plt.subplot(5,2,5)
    plt.loglog(w_ePSD, undamped_ePSD_data[2], linewidth = line_width)
    plt.loglog(w_pPSD, undamped_pPSD_data[2], linewidth = line_width)
    plt.loglog(w_aPSD, undamped_aPSD_data[2], linewidth = line_width, color='red')
    plt.xticks([])
    plt.xlim([w_aPSD[0],w_ePSD[-1]])
    plt.title(r"$\theta$", x=0.95, y=.7)
    plt.ylabel(r"$S_{\theta\theta}$", fontsize = label_fontsize)

    plt.subplot(5,2,6)
    plt.loglog(w_ePSD, damped_ePSD_data[2], linewidth = line_width)
    plt.loglog(w_pPSD, damped_pPSD_data[2], linewidth = line_width)
    plt.loglog(w_aPSD, damped_aPSD_data[2], linewidth = line_width, color='red')
    plt.xticks([])
    plt.xlim([w_aPSD[0],w_ePSD[-1]])
    plt.title(r"$\theta$", x=0.95, y=.7)
    plt.ylabel(r"$S_{\theta\theta}$", fontsize = label_fontsize)

    plt.subplot(5,2,7)
    plt.loglog(w_ePSD, undamped_ePSD_data[3], linewidth = line_width)
    plt.loglog(w_pPSD, undamped_pPSD_data[3], linewidth = line_width)
    plt.loglog(w_aPSD, undamped_aPSD_data[3], linewidth = line_width, color='red')
    plt.xticks([])
    plt.xlim([w_aPSD[0],w_ePSD[-1]])
    plt.title(r"$q$", x=0.95, y=.7)
    plt.ylabel(r"$S_{qq}$",fontsize = label_fontsize)

    plt.subplot(5,2,8)
    plt.loglog(w_ePSD, damped_ePSD_data[3], linewidth = line_width)
    plt.loglog(w_pPSD, damped_pPSD_data[3], linewidth = line_width)
    plt.loglog(w_aPSD, damped_aPSD_data[3], linewidth = line_width, color='red')
    plt.xticks([])
    plt.xlim([w_aPSD[0],w_ePSD[-1]])
    plt.title(r"$q$", x=0.95, y=.7)
    plt.ylabel(r"$S_{qq}$",fontsize = label_fontsize)

    plt.subplot(5,2,9)
    plt.loglog(w_ePSD, undamped_ePSD_data[4], linewidth = line_width)
    plt.loglog(w_pPSD, undamped_pPSD_data[4], linewidth = line_width)
    plt.loglog(w_aPSD, undamped_aPSD_data[4], linewidth = line_width, color='red')
    plt.xlim([w_aPSD[0],w_ePSD[-1]])
    plt.title(r"$n_z$", x=0.95, y=.7)
    plt.ylabel(r"$S_{NN}$", fontsize = label_fontsize)
    plt.xlabel(r"$\omega$ [rad/s]", fontsize = label_fontsize)

    plt.subplot(5,2,10)
    plt.loglog(w_ePSD, damped_ePSD_data[4], linewidth = line_width)
    plt.loglog(w_pPSD, damped_pPSD_data[4], linewidth = line_width)
    plt.loglog(w_aPSD, damped_aPSD_data[4], linewidth = line_width, color='red')
    plt.xlim([w_aPSD[0],w_ePSD[-1]])
    plt.title(r"$n_z$", x=0.95, y=.7)
    plt.ylabel(r"$S_{NN}$", fontsize = label_fontsize)
    plt.xlabel(r"$\omega$ [rad/s]", fontsize = label_fontsize)

