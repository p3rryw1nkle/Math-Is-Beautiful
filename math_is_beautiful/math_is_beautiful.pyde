def setup():
    '''
    This function is called once when the program starts to set up the screen
    '''

    global f, r, message
    
    message = "MATH IS BEAUTIFUL!"
    
    size(600, 600)

    # font for title text
    f = createFont("Georgia",50,True)
    textFont(f)
    textAlign(CENTER)
    smooth()
    
    #radius of title arc
    r = 250
    
    #position of tree window
    global treeX, treeY
    treeX = -210
    treeY = -100
    
    #position of mandelbrot window
    global mandelX, mandelY
    mandelX = 60
    mandelY = treeY
    
    #position of mondrian tiles window
    global mondriX, mondriY
    mondriX = treeX
    mondriY = 100
    
    #position of voronoi diagram window
    global voronoiX, voronoiY
    voronoiX = mandelX
    voronoiY = mondriY
    
    #size of preview windows
    global sizeX, sizeY
    sizeX = 150
    sizeY = 150
    
    #set background
    global baseColor, currentColor
    baseColor = color(255)
    currentColor = baseColor
    
    #variables that allow user to change screens
    global tree_s, mandelbrot_s, mondrian_s, voronoi_s, startscreen, set_points, pick_color, helpscreen
    startscreen = True
    tree_s = False
    mandelbrot_s = False
    mondrian_s = False
    voronoi_s = False
    set_points = False
    pick_color = False
    helpscreen = False
    
    #default variables that may be changed by the user
    global voronoi_color, l, seed, getSeed, subdivisions, min_diff, site_count, site_x_positions, site_y_positions, xmin, ymin, w, h, the_color
    
    seed = 1234
    getSeed = False
    
    #voronoi varaibles
    voronoi_color = True
    site_count = 25
    site_x_positions = [] #position coordinates of cell sites
    site_y_positions = []
    
    #tree varaibles
    l = 120 #length of initial branch
    the_color = [255, 255, 255]
    
    #mondrain variables
    subdivisions = 100 #max amount of lines that may be drawn
    min_diff = 50 #minimum space between squares
    
    #mandelbrot variables
    xmin = -3.0 #range on the complex plane
    ymin = -2.5
    w = 5.0
    h = 5.0

def draw():
    '''
    This function is called repeatedly to draw the screen
    '''
    update(mouseX, mouseY)
    
    global tree_s, mandelbrot_s, mondrian_s, voronoi_s, startscreen, helpscreen
    
    #startscreen draw function
    if startscreen:
        draw_start_screen()
    
    #recursive tree draw function
    if tree_s:
        generate_tree()
        
    # Mandelbrot set draw function
    if mandelbrot_s:
        generate_mandelbrot()

    # Mondrian tiles draw function
    if mondrian_s:
        generate_mondrian()
        
    if voronoi_s:
        generate_voronoi_diagram(width, height, 25, seed, voronoi_color)
    
    # screen where user is asked to set points for the voronoi
    if set_points:
        draw_set_points()
            
    # screen where user is asked to pick a color from the color wheel 
    if pick_color:
        draw_color_screen()
    
    if helpscreen:
        draw_help_screen()
        
'''''''''''''''''''''''''''
"      START SCREEN       "
'''''''''''''''''''''''''''
def draw_start_screen():
        clear()
        background(currentColor)
        drawHeader()
        
        global r,f 
        #creating curved text
        pushMatrix()
        translate(width / 2, height / 2)
        arclength = 0
        for i in xrange(len(message)):
            textFont(f)
            #check the width of each character.
            currentChar = message[i]
            text_width = textWidth(currentChar)
    
            #each box is centered so we move half the width
            arclength += text_width/2
            #angle in radians is the arclength divided by the radius
            #moving clockwise around the circle, adding (7*PI/6) as our offset
            theta = arclength / r + (7*PI/6)
    
            pushMatrix();
            #converting polar to cartestian coordinates
            translate(r*cos(theta), r*sin(theta))
            # rotate the box for each letter
            rotate(theta+PI/2)   #rotation is offset by 90 degrees
            # display the character
            fill(0)
            text(currentChar,0,0)
            popMatrix()
            #m ove halfway again
            arclength += text_width/2
        
        #load images
        drawTitles() 
        tree = loadImage("title_images/tree.png")
        image(tree, treeX, treeY, sizeX, sizeY)
        
        mandelbrot = loadImage("title_images/mandelbrot.png")
        image(mandelbrot, mandelX, mandelY, sizeX, sizeY)
        
        mondrian = loadImage("title_images/mondrian_tiles.png")
        image(mondrian, mondriX, mondriY, sizeX, sizeY)
        
        voronoi = loadImage("title_images/voronoi.jpg")
        image(voronoi, voronoiX, voronoiY, sizeX, sizeY)
        
        drawInstructions()
        popMatrix()

def drawHeader():
    textAlign(CENTER)
    h = createFont("Georgia", 16, True)
    fill(0)
    textFont(h)
    text("A project by Landon Brown", 300, 115)
    
def drawInstructions():
    textAlign(CENTER)
    g = createFont("Georgia", 10, True)
    fill(0)
    textFont(g)
    text("Press 'Q' to return to home screen", 0, -170)
    text("Press 'H' at any time for more controls", 0, -155)   
    text("Please give each algorithm up to 30 seconds to load", 0, -140)

#draws captions for each of the artworks    
def drawTitles():
    textAlign(CENTER)
    c = createFont("Georgia", 15, True)
    fill(0)
    textFont(c)
    text("Recursive Tree", treeX + 75, treeY + 175)
    text("Mandelbrot set", mandelX + 75, mandelY + 175)
    text("Piet Mondrian Tiles", mondriX + 75, mandelY + 375)
    text("Voronoi Diagram", voronoiX + 75, voronoiY + 175)
    
""""""""""""""""""""
"   OTHER SCREENS  "
""""""""""""""""""""

def draw_help_screen():
    background(255)
    c_1 = createFont("Georgia", 25, True)
    fill(0)
    textFont(c_1)
    textAlign(CENTER)
    text("Press 'H' to go back", width/2, 35)
    c_2 = createFont("Georgia", 20, True)
    textFont(c_2)
    textAlign(CENTER)
    text("Recursive Tree Functions:", width/2, 70)
    c_3 = createFont("Georgia", 15, True)
    textFont(c_3)
    text("Press the up arrow to increase the length of the trunk", width/2, 95)
    text("Press the down arrow to decrease the length of the trunk", width/2, 120)
    text("Press 'c' to change the color", width/2, 145)
    textFont(c_2)
    text("Mandelbrot Set Functions:", width/2, 195)
    textFont(c_3)
    text("Press the up arrow to zoom in on the fractal", width/2, 220)
    text("Press the down arrow to zoom out on the fractal", width/2, 245)
    text("Press 'c' to change the color", width/2, 270)
    textFont(c_2)
    text("Piet Mondrian Tiles Functions:", width/2, 320)
    textFont(c_3)
    text("Press 'r' to change the seed (see console)", width/2, 345)
    text("Press the up arrow to increase the complexity", width/2, 370)
    text("Press the down arrow to decrease the complexity", width/2, 395)
    textFont(c_2)
    text("Voronoi Diagram Functions:", width/2, 445)
    textFont(c_3)
    text("Press 'b' to change from color to black/white and vice versa", width/2, 470)
    text("Press 'p' to choose cell locations", width/2, 495)
    text("Press 'r' to change the seed/color randomness (see console)", width/2, 520)
    textFont(c_2)
    text("Press 's' at any time to save your work of art!", width/2, 570)    

def pick_color_screen():
    textAlign(CENTER)
    color_wheel = loadImage("color_wheel.jpg")
    background(255)
    image(color_wheel, 100, 100, 400, 400)
    text("Click asite_y_positionswhere to pick your color!", 300, 50)

def draw_set_points():
    global site_count, site_x_positions, site_y_positions
    background(255)
    frameRate(30)
    p = createFont("Georgia", 25, True)
    textFont(p)
    text(str(site_count), mouseX, mouseY)
    for i in site_x_positions:
        index = site_x_positions.index(i)
        noFill()
        stroke(255, 0, 0)
        circle(i, site_y_positions[index], 10)

""""""""""""""""""""
"ARTWORK FUNCTIONS"
""""""""""""""""""""
def generate_tree():
    clear()
    background(255)
    print("test")
    global the_color, l
    background(0)
    frameRate(30)
    
    def branch(l, theta):
        # global the_color
        # each branch will be 70% the size of the previous one
        l *= 0.7
        # tree will stop branching when the length is less than 2 pixels
        if l > 2:
            # save the current state of transformation (what position we're at now)
            stroke(the_color[0], the_color[1], the_color[2])
            pushMatrix()
            rotate(theta)  # rotate by theta
            line(0, 0, 0, -l)  # draw the branch
            translate(0, -l)  # move to the end of the branch
            branch(l, theta)  # function calls itself to draw to branches
            # whenever we get back here, we "pop" the matrix to restore the previous transformation state
            popMatrix()
            # repeat the same thing, only branch off to the left this time
            with pushMatrix():
                rotate(-theta)
                line(0, 0, 0, -l)
                translate(0, -l)
                branch(l, theta)
    
    stroke(the_color[0], the_color[1], the_color[2])
    strokeWeight(1)
    # gathers the mouse's position along the x-axis
    a = (mouseX / float(width)) * 90
    # convert angle into radians
    
    # start the tree from the bottom of the screen
    pushMatrix()
    translate(width / 2, height)
    line(0, 0, 0, - l) # start by drawing a line of l pixels
    translate(0, -l) # move to the end of that line
    branch(l, radians(a))
    popMatrix()

def generate_mandelbrot():
    # Declare global variables used for the Mandelbrot set
    global xmin, ymin, w, h, the_color
    
    # Set the background to white
    background(255)
    
    # Load the pixel array so we can manually modify pixel colors
    loadPixels()
    
    # Maximum number of iterations for checking Mandelbrot set membership
    max_iterations = 100
    
    # Calculate the maximum x and y coordinates in the complex plane
    xmax = xmin + w  # xmax is the right boundary
    ymax = ymin + h  # ymax is the upper boundary
    
    # Calculate the step size for incrementing x and y coordinates for each pixel
    dx = float(w) / width   # Width step per pixel
    dy = float(h) / height  # Height step per pixel
    
    # Start y at the ymin boundary
    y = ymin
    
    # Bailout value (if the magnitude of the complex number exceeds this, it diverges)
    bailout_value = 16.0
    
    # Extract the red, green, and blue components of the color
    red_value = the_color[0]
    if red_value == 0:
        red_value = 0.01  # Avoid division by zero
    
    green_value = the_color[1]
    if green_value == 0:
        green_value = 0.01  # Avoid division by zero
    
    blue_value = the_color[2]
    if blue_value == 0:
        blue_value = 0.01  # Avoid division by zero
    
    # Loop over each pixel on the screen (height-wise)
    for pixel_y in range(height):
        # Start x at the xmin boundary
        x = xmin
        # Loop over each pixel on the screen (width-wise)
        for pixel_x in range(width):
            # Initialize the real (a) and imaginary (b) parts of the complex number
            a = x
            b = y
            n = 0  # Iteration counter
            
            # Iterate z = z^2 + c and check for divergence
            while n < max_iterations:
                aa = a * a  # Real part squared
                bb = b * b  # Imaginary part squared
                twoab = 2.0 * a * b  # 2 * real * imaginary
                
                # Update the real and imaginary parts of the complex number
                a = aa - bb + x  # z_real = real^2 - imaginary^2 + initial x (real part of c)
                b = twoab + y    # z_imaginary = 2 * real * imaginary + initial y (imaginary part of c)
                
                # If the sum of the squares of the real and imaginary parts exceeds the bailout value, break
                if aa + bb > bailout_value:
                    break
                
                n += 1  # Increase the iteration count
            
            # Set the color based on the number of iterations taken to escape
            if n == max_iterations:
                # Point belongs to the Mandelbrot set, paint it black
                pixels[pixel_x + pixel_y * width] = color(0)
            else:
                # Point does not belong, color it based on how quickly it diverged
                pixels[pixel_x + pixel_y * width] = color(
                    ((red_value / bailout_value) * n), 
                    ((green_value / bailout_value) * n), 
                    ((blue_value / bailout_value) * n)
                )
            
            # Move to the next x value (increment in the complex plane)
            x += dx
        
        # Move to the next y value (increment in the complex plane)
        y += dy
    
    # Update the screen with the new pixel values
    updatePixels()

# Function to generate a Voronoi diagram
def generate_voronoi_diagram(canvas_width, canvas_height, num_sites, seed_value, use_voronoi_color):
    global site_x_positions, site_y_positions
    red_values, green_values, blue_values = [], [], []

    # Set the seed for consistent random site generation
    randomSeed(seed_value)

    # Generate random site positions and random color values for each site
    for i in range(num_sites):
        # If not enough x or y positions have been generated, append a random one
        if len(site_x_positions) == i:
            site_x_positions.append(int(random(canvas_width)))
        if len(site_y_positions) == i:
            site_y_positions.append(int(random(canvas_height)))
        
        # Generate random RGB color values
        red_values.append(int(random(256)))
        green_values.append(int(random(256)))
        blue_values.append(int(random(256)))

        # Visualize the site as a small circle on the canvas
        site = circle(site_x_positions[i], site_y_positions[i], 10)

    # Iterate over every pixel on the canvas to calculate Voronoi cells
    for y in range(canvas_height):
        for x in range(canvas_width):
            # Initialize the minimum distance as the diagonal length of the canvas
            min_distance = dist(0, 0, canvas_width - 1, canvas_height - 1)
            closest_site_index = 0
            
            # Find the closest site for each pixel
            for i in range(num_sites):
                distance_to_site = dist(0, 0, x - site_x_positions[i], y - site_y_positions[i])
                if distance_to_site < min_distance:
                    min_distance = distance_to_site
                    closest_site_index = i
            
            # Set pixel color based on the closest site
            if not use_voronoi_color:
                # Use only the red channel for grayscale
                set(x, y, color(red_values[closest_site_index]))
            else:
                # Use full RGB color
                set(x, y, color(red_values[closest_site_index], 
                                green_values[closest_site_index], 
                                blue_values[closest_site_index]))

def generate_mondrian():
    # Declare global variables for seed, subdivisions, and minimum difference
    global seed, subdivisions, min_diff
    
    # Separation between squares
    square_spacing = 1
    
    # Piet Mondrian color palette
    # Frequency of color in array corresponds to the likelihood of a square being colored
    colors = [
        (38, 71, 124),   # Blue
        (240, 217, 92),  # Yellow
        (162, 45, 40),   # Red
        (223, 224, 236), # Light gray
        (223, 224, 236), # Light gray
        (223, 224, 236), # Light gray
        (223, 224, 236), # Light gray
        (223, 224, 236)  # Light gray
    ]
    
    # Subdivision adjustment factors
    split_factors = [0.5, 1, 1.5]
    
    # Canvas border size
    canvas_edge = 10
    
    # Set the background to white
    background(255)
    
    # Initialize the list of quadrants (rectangles)
    quads = []
    
    # Add the initial rectangle that covers the entire canvas
    quads.append([
        (canvas_edge, canvas_edge), 
        (width - canvas_edge, canvas_edge), 
        (width - canvas_edge, height - canvas_edge), 
        (canvas_edge, height - canvas_edge)
    ])
    
    # Set the random seed to ensure reproducibility
    randomSeed(seed)
    
    # Start subdividing the rectangles for the specified number of subdivisions
    for i in range(subdivisions):
        # Select a random rectangle (quadrant) from the list
        quad_index = int(random(len(quads)))
        quad = quads[quad_index]
        
        # Extract the x and y coordinates of the current rectangle (quadrant)
        quad_left_x = quad[0][0]
        quad_right_x = quad[1][0]
        quad_top_y = quad[0][1]
        quad_bottom_y = quad[2][1]
        
        # Select a random split factor from the available options
        split_factor = split_factors[int(random(len(split_factors)))]
        
        # Determine if the split will be vertical or horizontal
        if random(1) < 0.5:
            # Vertical split
            if (quad_right_x - quad_left_x) > min_diff:
                # Calculate the x-coordinate where the split will occur
                x_split = (quad_right_x - quad_left_x) / 2 * split_factor + quad_left_x
                
                # Remove the original quadrant and replace it with two smaller ones
                quads.pop(quad_index)
                quads.append([
                    (quad_left_x, quad_top_y), 
                    (x_split - square_spacing, quad_top_y), 
                    (x_split - square_spacing, quad_bottom_y), 
                    (quad_left_x, quad_bottom_y)
                ])
                quads.append([
                    (x_split + square_spacing, quad_top_y), 
                    (quad_right_x, quad_top_y), 
                    (quad_right_x, quad_bottom_y), 
                    (x_split + square_spacing, quad_bottom_y)
                ])
        else:
            # Horizontal split
            if (quad_bottom_y - quad_top_y) > min_diff:
                # Calculate the y-coordinate where the split will occur
                y_split = (quad_bottom_y - quad_top_y) / 2 * split_factor + quad_top_y
                
                # Remove the original quadrant and replace it with two smaller ones
                quads.pop(quad_index)
                quads.append([
                    (quad_left_x, quad_top_y), 
                    (quad_right_x, quad_top_y), 
                    (quad_right_x, y_split - square_spacing), 
                    (quad_left_x, y_split - square_spacing)
                ])
                quads.append([
                    (quad_left_x, y_split + square_spacing), 
                    (quad_right_x, y_split + square_spacing), 
                    (quad_right_x, quad_bottom_y), 
                    (quad_left_x, quad_bottom_y)
                ])
    
    # Draw the quadrants with stroke and random colors from the palette
    stroke(0)          # Set the outline color to black
    strokeWeight(2)    # Set the outline thickness
    
    # Loop through each quadrant and draw it
    for quad in quads:
        # Fill each quadrant with a random color from the palette
        fill(*colors[int(random(len(colors)))])
        
        # Begin drawing the shape
        beginShape()
        for vertex_point in quad:
            vertex(vertex_point)
        endShape(CLOSE)  # Close the shape    

"""""""""""""""""""""""
"   INPUT HANDLING    "
"""""""""""""""""""""""

def update(x, y):
    '''
    Grabs mouse coordinates and updates variables accordingly
    '''
    global treeOver, mandelOver, mondriOver, voronoiOver
    treeOver = overTree(treeX + 300, treeY + 300, sizeX, sizeY)
    mandelOver = overMandel(mandelX + 300, mandelY + 300, sizeX, sizeY)
    mondriOver = overMondri(mondriX + 300, mondriY + 300, sizeX, sizeY)
    voronoiOver = overVoronoi(voronoiX + 300, voronoiY + 300, sizeX, sizeY)

def mousePressed():
    '''
    handles mouse-click events
    '''
    global currentColor, tree_s, mandelbrot_s, mondrian_s, voronoi_s, startscreen, set_points, site_x_positions, site_y_positions
    global site_count, seed, voronoi_color, xmin, ymin, w, h, pick_color, the_color
    
    # Handle setting points for the Voronoi diagram
    if set_points and site_count > 0:
        site_x_positions.append(mouseX)
        site_y_positions.append(mouseY)
        site_count -= 1
        if site_count == 0:
            set_points = False
            voronoi_s = True
            generate_voronoi_diagram(width, height, 25, seed, voronoi_color)
    
    # Handle picking a color
    if pick_color:
        c = get(mouseX, mouseY)
        the_color = [red(c), green(c), blue(c)]
        pick_color = False
    
    # Simplify switching between different screens based on the state of the start screen
    if startscreen:
        if treeOver:
            tree_s, voronoi_s, mandelbrot_s, mondrian_s, startscreen = True, False, False, False, False
            generate_tree()
        elif mandelOver:
            mandelbrot_s, voronoi_s, tree_s, mondrian_s, startscreen = True, False, False, False, False
        elif mondriOver:
            mondrian_s, voronoi_s, tree_s, mandelbrot_s, startscreen = True, False, False, False, False
            generate_mondrian()
        elif voronoiOver:
            voronoi_s, tree_s, mandelbrot_s, mondrian_s, startscreen = True, False, False, False, False
            generate_voronoi_diagram(width, height, 25, seed, voronoi_color)

def keyPressed():
    '''
    Handles key press events
    '''
    global tree_s, mandelbrot_s, mondrian_s, voronoi_s, startscreen, getSeed, set_points, seed, pick_color, helpscreen
    if key == 'q':
        # quit whatever screen your on and go back to home
        clear()
        startscreen = True
        tree_s = False
        mandelbrot_s = False
        mondrian_s = False
        voronoi_s = False
        set_points = False
        pick_color = False
        helpscreen = False
    if key == 's':
        # save depending on what screen is presented
        if tree_s:
            save("works_of_art/" + "recursive_tree" + str(int(random(1000))) + ".png")
        if mandelbrot_s:
            save("works_of_art/" + "mandelbrot" + str(int(random(1000))) + ".png")
        if mondrian_s:
            save("works_of_art/" + "mondrian" + str(int(random(1000))) + ".png")
        if voronoi_s:
            save("works_of_art/" + "voronoi" + str(int(random(1000))) + ".png")
    if keyCode == UP:
        # if on the tree screen, add length
        if tree_s:
            global l
            l += 10
        # if on the mondrian tiles screen, add more divisions
        if mondrian_s:
            global subdivisions
            subdivisions += 10
        # if on the mandelbrot screen, zoom in
        if mandelbrot_s:
            global xmin, ymin, w, h
            print(xmin, ymin, w, h)
            xmin = xmin/2
            ymin = ymin/2
            w = w/2
            h = h/2
            print(xmin, ymin, w, h)
    if keyCode == DOWN:
        # if on the tree screen, decrease length
        if tree_s:
            global l
            l -= 10
        # if on the mondrian tile screen, reduce subdivisions
        if mondrian_s:
            global subdivisions
            subdivisions -= 10
        # if on the mandelbrot screen, zoom out
        if mandelbrot_s:
            global xmin, ymin, w, h
            xmin = float(xmin*2)
            ymin = float(ymin*2)
            w = float(w*2)
            h = float(h*2)
            print(xmin, ymin, w, h)
    if keyCode == RIGHT:
        if mandelbrot_s:
            global xmin, ymin, w, h
            xmin += xmin/4
            ymin += ymin/4
    if keyCode == LEFT:
        if mandelbrot_s:
            global xmin, ymin, w, h
            xmin -= xmin/4
            ymin -= ymin/4
    if key == 'b':
        if voronoi_s:
            global voronoi_color
            vc = voronoi_color
            if vc == True:
                voronoi_color = False
            if vc == False:
                voronoi_color = True
            generate_voronoi_diagram(width, height, 25, seed, voronoi_color)
    if key == 'c':
        global pick_color
        startscreen = False
        if tree_s or mandelbrot_s:
            pick_color = True
    if key == 'r':
        global getSeed, seed, temp_seed
        print("Please enter a 4 digit code for your key")
        getSeed = True
        temp_seed = ''
    if getSeed == True and key in '0123456789':
        global seed, temp_seed
        temp_seed += key
        if len(temp_seed) == 4:
            seed = int(temp_seed)
            getSeed = False
            if voronoi_s:
                generate_voronoi_diagram(width, height, 25, seed, voronoi_color)
    if key == 'p':
        global site_x_positions, site_y_positions, site_count
        if voronoi_s:
            site_count = 25
            set_points = True
            voronoi_s = False
            site_x_positions = []
            site_y_positions = []
    if key == 'h':
        status = helpscreen
        if status == False:
            helpscreen = True
        if status == True:
            helpscreen = False

#tests to see if mouse is over asite_y_positions of the previews on title screen
def overTree(x, y, w, h):
    return x <= mouseX <= x + w and y <= mouseY <= y + h

def overMandel(x, y, w, h):
    return x <= mouseX <= x + w and y <= mouseY <= y + h

def overMondri(x, y, w, h):
    return x <= mouseX <= x + w and y <= mouseY <= y + h

def overVoronoi(x, y, w, h):
    return x <= mouseX <= x + w and y <= mouseY <= y + h




        
