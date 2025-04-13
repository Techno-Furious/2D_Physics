import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
dt = 1
colors = ["red", "green", "blue", "purple", "orange", "yellow", "cyan", "magenta", "white", "gray"]

#PHYSICS
GRAVITY = 980
toggle_gravity = False


class BALL:
    def __init__(self,x,y,radius,BOUNCE_FACTOR=0.8,mass=1.0,color="white"):

        self.mass = mass
        self.pos_x = x
        self.pos_y = y
        self.radius = radius
        self.vel=[10,0]
        self.acc=[0,0]
        self.BOUNCE_FACTOR = BOUNCE_FACTOR
        self.color = color



#OBJECT CONFIGURATION
FPS=60
circle_radius = 20
ball_select=1


def create_balls(n):
    balls = []
    start_x = 300
    spacing = 50  
    colors = ["red", "green", "blue", "purple", "orange", "yellow", "cyan", "magenta", "white", "gray"]

    for i in range(n):
        x = start_x + i * spacing
        color = colors[i % len(colors)]  
        ball = BALL(
            x=x,
            y=100,
            radius=10,
            BOUNCE_FACTOR=0.8,
            mass=1.0,
            color=color
        )
        balls.append(ball)

    return balls



# ball1 = BALL(x=640, y=100, radius=50,BOUNCE_FACTOR=0.9,mass=10.0)
# ball2 = BALL(x=540, y=100, radius=50,BOUNCE_FACTOR=1.0,mass=1.0,color="red")
# ball3 = BALL(x=740, y=100, radius=50,BOUNCE_FACTOR=1.0,mass=1.0,color="green")
# ball4 = BALL(x=840, y=100, radius=50,BOUNCE_FACTOR=1.0,mass=1.0,color="blue")

balls=create_balls(30)

ball1 = balls[0]


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
            
    for ball in balls:
        
        ball.vel[1] += ball.acc[1] * dt
        ball.pos_y += ball.vel[1] * dt

        ball.vel[0] += ball.acc[0] * dt
        ball.pos_x += ball.vel[0] * dt

        if ball.pos_y + ball.radius >= screen.get_height():
            ball.pos_y = screen.get_height() - ball.radius
            ball.vel[1] = -ball.vel[1] * ball.BOUNCE_FACTOR  # Apply bounce factor
        if ball.pos_y - ball.radius <= 0:
            ball.pos_y = ball.radius
            ball.vel[1] = -ball.vel[1] * ball.BOUNCE_FACTOR
        if ball.pos_x + ball.radius >= screen.get_width():
            ball.pos_x = screen.get_width() - ball.radius
            ball.vel[0] = -ball.vel[0] * ball.BOUNCE_FACTOR
        if ball.pos_x - ball.radius <= 0:
            ball.pos_x = ball.radius
            ball.vel[0] = -ball.vel[0] * ball.BOUNCE_FACTOR
        
        other_balls = [b for b in balls if b != ball]
        for other_ball in other_balls:
            distance = ((ball.pos_x - other_ball.pos_x) ** 2 + (ball.pos_y - other_ball.pos_y) ** 2) ** 0.5
            if distance < ball.radius + other_ball.radius:
                # font=pygame.font.Font(None, 25)
                # text=font.render("COLLISION",True,"red")
                # screen.blit(text,(screen.get_width()/2,screen.get_height()/2))
                overlap = ball.radius + other_ball.radius - distance
                nx = (ball.pos_x - other_ball.pos_x) / distance
                ny = (ball.pos_y - other_ball.pos_y) / distance

                # Push them apart equally 
                ball.pos_x += nx * overlap / 2
                ball.pos_y += ny * overlap / 2
                other_ball.pos_x -= nx * overlap / 2
                other_ball.pos_y -= ny * overlap / 2
                # Relative velocity
                rvx = ball.vel[0] - other_ball.vel[0]
                rvy = ball.vel[1] - other_ball.vel[1]

                # Velocity along the normal
                vel_along_normal = rvx * nx + rvy * ny

                # Skip if they are moving apart
                if vel_along_normal > 0:
                    continue

                # Restitution (bounciness)
                restitution = min(ball.BOUNCE_FACTOR, other_ball.BOUNCE_FACTOR)

                # Impulse scalar
                impulse = -(1 + restitution) * vel_along_normal
                impulse /= (1 / ball.mass + 1 / other_ball.mass)

                # Apply impulse
                impulse_x = impulse * nx
                impulse_y = impulse * ny

                ball.vel[0] += impulse_x / ball.mass
                ball.vel[1] += impulse_y / ball.mass

                other_ball.vel[0] -= impulse_x / other_ball.mass
                other_ball.vel[1] -= impulse_y / other_ball.mass


    

        pygame.draw.circle(screen, ball.color, (int(ball.pos_x), int(ball.pos_y)), ball.radius)


    keys = pygame.key.get_pressed()

    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  
            mouse_x, mouse_y = pygame.mouse.get_pos()
            ball_new = BALL(
                x=mouse_x,
                y=mouse_y,
                radius=10,
                BOUNCE_FACTOR=0.9,
                mass=1.0,
                color=random.choice(colors)
            )
            balls.append(ball_new)
        if event.button == 3:  
            mouse_x, mouse_y = pygame.mouse.get_pos()
            ball_new = BALL(
                x=mouse_x,
                y=mouse_y,
                radius=20,
                BOUNCE_FACTOR=0.9,
                mass=10.0,
                color=random.choice(colors)
            )
            balls.append(ball_new)

    if keys[pygame.K_r]:
        balls=[]
        balls=create_balls(2)

    if keys[pygame.K_w]:
        for ball in balls:
            ball.acc[1] -= 30
    if keys[pygame.K_s]:
        for ball in balls:
            ball.acc[1] += 30
    if keys[pygame.K_a]:
        for ball in balls:
            ball.acc[0] -= 30
    if keys[pygame.K_d]:
        for ball in balls:
            ball.acc[0] += 30
    if keys[pygame.K_SPACE]:
        for ball in balls:
            ball.acc=[0,0]
            toggle_gravity = False
            text=font.render(f"Gravity: OFF",True,"white")
            screen.blit(text,(screen.get_width()/2,screen.get_height()/2))
    if keys[pygame.K_g]:
        for ball in balls:
            ball.acc=[0,GRAVITY ]
            toggle_gravity = True
            text=font.render(f"Gravity: ON",True,"white")
            screen.blit(text,(screen.get_width()/2,screen.get_height()/2))
        

    font=pygame.font.Font(None, 25)
    text=font.render("FPS: "+str(int(clock.get_fps())),True,"white")
    screen.blit(text,(10,10))
    text=font.render(f"ACC_X: {ball1.acc[0]:.2f} ACC_Y:{ball1.acc[1]:.2f}",True,"white")
    screen.blit(text,(10,40))
    text=font.render(f"Number of balls: {len(balls)}",True,"white")
    screen.blit(text,(10,70))
    text=font.render(f"Gravity: {toggle_gravity}",True,"white")
    screen.blit(text,(10,100))


    # flip() the display to put your work on screen
    pygame.display.flip()
    

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS) / 1000

pygame.quit()
