import turtle
from typing import Dict, Any, Tuple
# initializes turtle graphics coordinates
new_x_position = 720 / -2
new_y_position = 675 / -2
print('Window height:' + str(new_x_position))
print('Window width:' + str(new_y_position))
turtle.tracer(0, 0)

# draws a text on the screen
def draw_text(the_text: str, x: int, y: int) -> None:
    turtle.penup()
    turtle.goto(new_x_position + x, new_y_position + y)
    turtle.pendown()
    turtle.write(the_text, True, align="left", font=("Arial", 20, "normal"))

# draws a bar on the screen
def draw_bar(x: int, y: int, height: int, width: int, color: str) -> None:
    turtle.pencolor(color)
    turtle.pensize(0)
    turtle.penup()
    turtle.setposition(new_x_position + x, new_y_position + y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()



def draw_bars(x: int, y: int, color: str, width: int = 10, gap: int = 5, total_bars: int = 1) -> None:
    i = 0
    while i < total_bars:
        draw_bar(x + (i * (width + gap)), y, 400, width, color)
        i += 1

def render() -> None:
    turtle.update()  # Render image
    turtle.exitonclick()  # Wait for user's mouse click

# You have to implement the following 4 functions
def get_value_from_tuple(x: Tuple[Any, int]) -> int:
    return x[1]

def plot_top_k_service_types(data: Dict[str, Dict[Any, int]], metadata: str, k: int) -> None:
    x_start = -300
    list_to_graph = sorted(list(data[metadata].items()), key=get_value_from_tuple, reverse=True)[:k]
    max_value = max([value for key, value in list_to_graph]) if list_to_graph else 1
    scale_factor = 80 / max_value if max_value > 80 else 1
    
    for key, value in list_to_graph:
            scaled_height = int(value * scale_factor)
            draw_bar(x_start, 120, scaled_height, 35, 'green')
            draw_text(str(key), x_start + 5, 100)
            draw_text(str(value), x_start + 10, 120 + scaled_height + 5)
            x_start += 70
    draw_text('Top service types by day of week', -300, 220)

def plot_bottom_k_service_types(data: Dict[str, Dict[Any, int]], metadata: str, k: int) -> None:
    x_start = 100
    list_to_graph = sorted(list(data[metadata].items()), key=get_value_from_tuple, reverse=True)[-k:]
    max_value = max([value for key, value in list_to_graph]) if list_to_graph else 1
    scale_factor = 80 / max_value if max_value > 80 else 1

    for key, value in list_to_graph:
            scaled_height = int(value * scale_factor)
            draw_bar(x_start, 120, scaled_height, 35, 'blue')
            draw_text(str(key), x_start + 5, 100)
            draw_text(str(value), x_start + 10, 120 + scaled_height + 5)
            x_start += 70
    draw_text('Bottom service types by day of week', 100, 220)

def plot_service_by_day(data: Dict[str, Dict[Any, int]], day: int) -> None:
    if day in data['day_of_week']:
        count = data['day_of_week'][day]
        scaled_height = min(count * 4, 100)  # Scale to reasonable height
        draw_bar(-300, -80, scaled_height, 50, 'red')
        draw_text(f'Day {day}', -320, -110)
        draw_text(f'Count: {count}', -320, -80 + scaled_height + 10)
        draw_text('Service calls by day', -300, 20)
    else:
        draw_text(f'No data for day {day}', -320, -80)
        draw_text('Service calls by day', -300, 20)

def plot_service_by_hour(data: Dict[str, Dict[Any, int]], hour: int) -> None:
    if hour in data['hour_of_day']:
        count = data['hour_of_day'][hour]
        scaled_height = min(count * 3, 100)  # Scale to reasonable height
        draw_bar(100, -80, scaled_height, 50, 'purple')
        draw_text(f'Hour {hour}', 80, -110)
        draw_text(f'Count: {count}', 80, -80 + scaled_height + 10)
        draw_text('Service calls by hour', 100, 20)
    else:
        draw_text(f'No data for hour {hour}', 80, -80)
        draw_text('Service calls by hour', 100, 20)

