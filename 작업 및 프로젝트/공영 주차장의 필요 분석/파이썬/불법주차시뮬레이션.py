# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class ParkingSpace:
    def __init__(self, id):
        self.id = id
        self.is_occupied = False
        self.parking_time = 0

class RoadSegment:
    def __init__(self, id):
        self.id = id
        self.is_illegally_occupied = False

class MarketParking:
    def __init__(self, width, height, inflow_rate, outflow_rate):
        self.width = width
        self.height = height
        self.inflow_rate = inflow_rate
        self.outflow_rate = outflow_rate
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.illegal_queue = []
        self.total_illegal_parked_time = 0
        self.time = 0
        self.total_illegal_cars = 0
        
        # Initialize parking spaces and roads
        for y in range(height):
            for x in range(width):
                if y < height - 1:  # Parking spaces
                    self.grid[y][x] = ParkingSpace(id=(y, x))
                else:  # Road segments
                    self.grid[y][x] = RoadSegment(id=(y, x))
        
    def update(self):
        # Add new cars
        new_cars = random.randint(0, self.inflow_rate)
        for _ in range(new_cars):
            empty_spaces = [(y, x) for y in range(self.height - 1) for x in range(self.width) if not self.grid[y][x].is_occupied]
            if empty_spaces:
                y, x = random.choice(empty_spaces)
                self.grid[y][x].is_occupied = True
            else:
                # Add to illegal queue if no space
                self.illegal_queue.append(self.time)
                self.total_illegal_cars += 1
        
        # Remove leaving cars
        leaving_cars = random.randint(0, self.outflow_rate)
        # Remove from legal parking
        for _ in range(leaving_cars):
            occupied_spaces = [(y, x) for y in range(self.height - 1) for x in range(self.width) if self.grid[y][x].is_occupied]
            if occupied_spaces:
                y, x = random.choice(occupied_spaces)
                self.grid[y][x].is_occupied = False
                self.grid[y][x].parking_time = 0

        # Remove from illegal parking
        for _ in range(leaving_cars):
            if self.illegal_queue:
                parked_time = self.illegal_queue.pop(0)
                self.total_illegal_parked_time += self.time - parked_time
        
        # Update parking time
        for y in range(self.height - 1):
            for x in range(self.width):
                if self.grid[y][x].is_occupied:
                    self.grid[y][x].parking_time += 1
        
        self.time += 1
        
        return self.grid

def update_plot(frame, market, ax1, ax2, parking_plot, illegal_plot, time_text):
    grid = market.update()
    
    # Update parking data for visualization
    parking_data = np.zeros((market.height - 1, market.width))
    for y in range(market.height - 1):
        for x in range(market.width):
            if grid[y][x].is_occupied:
                parking_data[y][x] = 1
    
    # Update illegal parking data for visualization
    illegal_data = np.zeros((1, market.width))
    illegal_parked = len(market.illegal_queue)
    if illegal_parked > 0:
        illegal_data[0, :illegal_parked] = 1
    
    parking_plot.set_array(parking_data)
    illegal_plot.set_array(illegal_data)
    
    time_text.set_text(f'Time: {market.time} min')
    
    return parking_plot, illegal_plot, time_text

# Simulation parameters
roads = 5  # Number of road segments
parking_spaces = 50  # Number of legal parking spaces
inflow_rate = 240  # Maximum number of cars arriving per time unit
outflow_rate = 15  # Maximum number of cars leaving per time unit
duration = 24 * 60  # Duration of the simulation (in minutes)

# Create simulation object
market = MarketParking(parking_spaces // roads, roads + 1, inflow_rate, outflow_rate)

# Graph settings
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
parking_data = np.zeros((roads, parking_spaces // roads))
illegal_data = np.zeros((1, parking_spaces // roads))

parking_plot = ax1.imshow(parking_data, cmap='coolwarm', aspect='auto', vmin=0, vmax=1)
illegal_plot = ax2.imshow(illegal_data, cmap='coolwarm', aspect='auto', vmin=0, vmax=1)

ax1.set_title('합법 주차 공간')
ax2.set_title('불법 주차 (도로)')

for ax in [ax1, ax2]:
    ax.set_yticks([])
    ax.set_xticks([])

fig.suptitle('수원시 골목시장 주차 시뮬레이션')
time_text = ax1.text(0.02, 1.1, '', transform=ax1.transAxes)

# Add legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#3B4CC0', edgecolor='black', label='빈 주차 공간'),
                   Patch(facecolor='#B40426', edgecolor='black', label='주차된 차량'),
                   Patch(facecolor='#FFA500', edgecolor='black', label='불법 주차')]
ax1.legend(handles=legend_elements, loc='upper right')

# Create animation
ani = animation.FuncAnimation(fig, update_plot, frames=duration, 
                              fargs=(market, ax1, ax2, parking_plot, illegal_plot, time_text),
                              interval=50, blit=True)

plt.tight_layout()
plt.savefig('1.png', dpi=300)
plt.show()

# Print final results
print(f"최대 불법주차 차량수: {market.total_illegal_cars}")
print(f"평균 불법주차 시간: {market.total_illegal_parked_time / max(market.total_illegal_cars, 1):.2f} 분")


# 1. 각 도로별로 불법 주차가 발생하지 않습니다. 대신 전체 도로 수만큼의 불법 주차 칸이 수동적으로 생성되어 불법 주차 칸이 필요한 부분에 배치되지 않습니다.
# 2. 불법 주차 시 차량이 움직이지 않습니다. 실제 골목시장에서는 불법 주차 차량이 차례대로 움직이며, 주차 공간이 나오는 순간 빠르게 주차되는 것으로 확인됩니다.
# 3. 불법 주차 차량의 평균 계산은 불법 주차 시간대별 총합만 고려하여 평균이 잘못된 것으로 보입니다.
# 4. 각 주차 공간별로 주차 시간을 기록하지 않아 각 주차 공간의 주차 시간이나 주차 빈도를 계산할 수 없습니다.
# 5. 도로 또는 주차 공간에 대한 별도의 ID 또는 인덱스를 부여하지 않아 각 주차 공간이나 도로의 상태를 따로 추적할 수 없습니다.

# 위의 개선할 사항을 수정할 수 있는 방법
# 1. 주차 공간과 도로를 1차원 배열로 나타내선 안되고, 2차원 배열로 나타내어 주차 공간의 위치와 도로 위치를 명확히 구분합니다.
# 2. 불법 주차가 발생할 때마다 해당 위치에 불법 주차 차량이 있는 상태로 변경하고, 주차 공간이 나올 때마다 불법 주차 차량을 이동시킵니다.
# 3. 불법 주차 시간대별 총합과 전체 시간대를 고려하여 불법 주차 차량의 평균을 계산합니다.
# 4. 각 주차 공간별로 주차 시간과 주차 빈도를 기록하여 각 주차 공간의 사용량을 평가할 수 있도록 합니다.
# 5. 주차 공간과 도로에 대한 고유한 ID를 부여하여 각 주차 공간이나 도로의 상태를 따로 추적할 수 있도록 합니다.

# # 명령문을 계속해서 수정해 나가야 함