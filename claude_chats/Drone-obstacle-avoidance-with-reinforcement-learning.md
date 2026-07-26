# Drone obstacle avoidance with reinforcement learning

- Source: https://claude.ai/share/804de4a9-c600-47b0-aef0-4890046f3a0e
- Author: MikeChang
- Created: 2025-12-06
- Messages: 6

---

## Human

teach a dron obstacle avoidance using RL

---

## Assistant

# Drone Obstacle Avoidance with Reinforcement Learning

Teaching a drone to avoid obstacles via RL involves framing the problem as a Markov Decision Process (MDP). Here's a structured approach:

## 1. Problem Formulation

**State Space (S):** What the drone "perceives"
- Position (x, y, z)
- Velocity (vx, vy, vz)
- Orientation (roll, pitch, yaw)
- Sensor readings: LiDAR distances, depth camera, or ultrasonic distances to obstacles in multiple directions

**Action Space (A):** What the drone can do
- Continuous: thrust adjustments (Δvx, Δvy, Δvz)
- Discrete: {forward, backward, left, right, up, down, hover}

**Reward Function (R):** Guides learning
```
R = r_goal + r_collision + r_progress + r_energy

where:
  r_goal     = +100 if reached target
  r_collision = -100 if hit obstacle
  r_progress = +α × (distance_reduction_to_goal)
  r_energy   = -β × (thrust_magnitude)  # penalize excessive movement
```

## 2. Common RL Algorithms

| Algorithm | Type | Best For |
|-----------|------|----------|
| **PPO** (Proximal Policy Optimization) | On-policy | Stable training, continuous actions |
| **SAC** (Soft Actor-Critic) | Off-policy | Sample efficiency, exploration |
| **TD3** (Twin Delayed DDPG) | Off-policy | Continuous control, reduced overestimation |
| **DQN** | Off-policy | Discrete action spaces |

**PPO** is often the go-to choice for drone control due to its stability.

## 3. Training Pipeline

```
┌─────────────────┐
│   Simulator     │  (Gazebo, AirSim, PyBullet)
│   Environment   │
└────────┬────────┘
         │ state, reward
         ▼
┌─────────────────┐
│   RL Agent      │  (PyTorch / TensorFlow)
│   (Policy π)    │
└────────┬────────┘
         │ action
         ▼
┌─────────────────┐
│   Drone Model   │  (dynamics, sensors)
└─────────────────┘
```

## 4. Neural Network Architecture

A typical policy network for obstacle avoidance:

```
Input Layer:  [position(3) + velocity(3) + sensor_readings(N)]
     │
Hidden Layer 1: 256 units, ReLU
     │
Hidden Layer 2: 256 units, ReLU
     │
Output Layer:  [action_mean(3), action_std(3)]  # for continuous
```

For sensor-rich inputs (depth images), add CNN layers before the MLP.

## 5. Key Implementation Tips

**Sim-to-Real Transfer:**
- Add domain randomization (vary mass, drag, sensor noise)
- Use dynamics randomization during training
- Train with latency injection to mimic real-world delays

**Reward Shaping:**
- Start with dense rewards (progress-based), then anneal to sparse
- Add a small time penalty to encourage efficiency
- Consider curriculum learning: start with few obstacles, gradually increase

**Safety During Deployment:**
- Use a safety filter (e.g., Control Barrier Functions) on top of RL policy
- Implement geofencing as a hard constraint

## 6. Popular Simulation Environments

| Simulator | Pros |
|-----------|------|
| **AirSim** (Microsoft) | Realistic rendering, Unreal Engine |
| **Gazebo + PX4** | ROS integration, physics fidelity |
| **PyBullet** | Lightweight, fast iteration |
| **Isaac Gym** (NVIDIA) | GPU-accelerated, massive parallelism |

---

Would you like me to create a working simulation with visualization (using PyBullet or a simplified 2D/3D environment)? I can build an interactive demo showing the drone learning to navigate through obstacles.

---

## Human

animate the learning process in three.js

---

## Assistant

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

[View your Drone RL Learning Visualization](computer:///mnt/user-data/outputs/drone_rl_learning.html)

This interactive Three.js visualization demonstrates the complete RL learning process for drone obstacle avoidance:

**Key Features:**

1. **Live Training Monitor** - Episode count, step counter, current/total rewards, epsilon decay, success rate, and collision tracking

2. **Learning Phases Visualized:**
   - 🔴 **Exploration** (ε > 0.5): Random actions, many collisions
   - 🟡 **Learning** (0.1 < ε < 0.5): Balancing exploration/exploitation
   - 🟢 **Exploitation** (ε < 0.1): Optimal learned behavior

3. **Visual Elements:**
   - Blue drone with spinning rotors and glow effect
   - Red obstacles with edge highlighting
   - Green goal target with pulsing animation
   - Yellow sensor rays showing obstacle detection
   - Color-coded path trail (red→green as episode progresses)

4. **Q-Value Display** - Real-time action values showing which direction the policy favors

5. **Reward Graph** - Historical episode rewards showing learning progress

**Controls:**
- ▶ Start / ⏸ Pause training
- ↺ Reset to untrained agent
- ⏭ Skip 10 episodes (fast-forward training)
- Speed slider for simulation pace

Watch the drone evolve from chaotic random movements to smooth goal-seeking behavior while avoiding obstacles!

---

## Human

do it a html format let me can share with anyone

---

## Assistant

The file I created is already a standalone HTML file that anyone can open in their browser! It's completely self-contained with all Three.js loaded from CDN.

[View/Download your Drone RL Learning Visualization](computer:///mnt/user-data/outputs/drone_rl_learning.html)

**How to share it:**

1. **Download** the HTML file from the link above
2. **Share directly** - Send the `.html` file via email, Slack, Google Drive, Dropbox, etc.
3. **Recipients just double-click** the file to open it in any browser - no installation needed!

The file includes:
- All Three.js 3D rendering (loaded from CDN)
- Complete DQN reinforcement learning agent
- Interactive controls and real-time statistics
- Works offline after first load

Anyone with a modern browser (Chrome, Firefox, Safari, Edge) can run it instantly. 🚁
