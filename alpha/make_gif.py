
from PIL import Image
def make_gif(imgs_list):
    
    frames = [Image.open(image) for image in imgs_list]
    frame_one = frames[0]
    frame_one.save("plots/energies.gif", format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)
    
if __name__ == "__main__":
    imgs = ["good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=7.141399.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=7.047561.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=6.589746.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=6.452817.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=6.076519.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=5.951505.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=5.574583.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=5.450465.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=5.325791.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=5.201036.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=5.051783.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=4.948586.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=4.801757.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=4.697881.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=4.551224.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=4.448358.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=4.300582.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=4.198157.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=4.049926.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=3.947691.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=3.799531.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=3.697325.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=3.548766.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=3.446908.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=3.058835.png", "good_plots/10-12-00-49-33/10-12-00-49-33-energy-distr-vac=2.94621.png"]
    
    make_gif(imgs)