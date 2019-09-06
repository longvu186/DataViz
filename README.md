# DataViz App - A product of Metric Analytics - Pre-alpha 
This is a very, very very pre-alpha version of the DataViz App. You can only create an animation of Bar Chart Race (for now)
Please fork and sync this repo for further updates

**WARNING: THE APP IS REALLY FRAGILE (like my heart) SINCE IT'S NOT COMPLETE YET. EDIT FILES AT YOUR OWN RISK**

Brief guide on how to use the app: Run DataViz.exe (shortcut) and edit BarChartRace.xlsx (shortcut) only

How to config the BarChartRace animation: (Default configurations are applied. You may leave the configs alone at will)
1. Title: This is the title, but it does nothing at the moment
2. Color of time indicator: Color of the, well, time indicator. Please use hex color code
3. Value format: Please do not delete the '{}'. The values appear at the end of the bars. The '{}' represents the values. You may add anything to the values. For instance, input '${}' if you want to add a dollor sign
4. Transparent background: Tick this if you want a transparent background. This output file will be in .mov format (this format can only be open by some applications). You can then add your own background with video editors such as Premiere Pro
5. Floating point: 0 means no digits after the comma. To add digits after the comma, add 0s and a 1 at the end. For instance: 0,001
6. Data interpolation: Add values inbetween the originals. This smooths out the animation. Please leave the setting 20 or more. (the algorithm is in early stages, be careful when using it)
7. FPS: It's frame per second!
8. Font size: It's font size!

**PREVIEW**: Press it to see a preview (the first frame) of the animation

**EXPORT**: At the moment the file will be saved into the "dist" folder. You'll see the percentage running in the console.

>Made with Matplotlib and Kivy (and tears, due to the bugs)
