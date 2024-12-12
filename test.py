import json
from typing import List, Dict, Any
import os
finalData = []
master = [
    {
        "data": [
            {
                "timestamp": 0.07,
                "direction": "Straight"
            },
            {
                "timestamp": 0.1,
                "direction": "Straight"
            },
            {
                "timestamp": 0.13,
                "direction": "Straight"
            },
            {
                "timestamp": 0.17,
                "direction": "Straight"
            },
            {
                "timestamp": 0.2,
                "direction": "Straight"
            },
            {
                "timestamp": 0.23,
                "direction": "Straight"
            },
            {
                "timestamp": 0.27,
                "direction": "Straight"
            },
            {
                "timestamp": 0.3,
                "direction": "Straight"
            },
            {
                "timestamp": 0.33,
                "direction": "Straight"
            },
            {
                "timestamp": 0.37,
                "direction": "Straight"
            },
            {
                "timestamp": 0.4,
                "direction": "Straight"
            },
            {
                "timestamp": 0.43,
                "direction": "Straight"
            },
            {
                "timestamp": 0.47,
                "direction": "Slight Right"
            },
            {
                "timestamp": 0.5,
                "direction": "Slight Right"
            },
            {
                "timestamp": 0.53,
                "direction": "Slight Right"
            },
            {
                "timestamp": 0.57,
                "direction": "Slight Right"
            },
            {
                "timestamp": 0.6,
                "direction": "Slight Right"
            },
            {
                "timestamp": 0.63,
                "direction": "Slight Right"
            },
            {
                "timestamp": 0.67,
                "direction": "Slight Right"
            },
            {
                "timestamp": 0.7,
                "direction": "Slight Right"
            },
            {
                "timestamp": 0.73,
                "direction": "Straight"
            },
            {
                "timestamp": 0.77,
                "direction": "Straight"
            },
            {
                "timestamp": 0.8,
                "direction": "Straight"
            },
            {
                "timestamp": 0.83,
                "direction": "Straight"
            },
            {
                "timestamp": 0.87,
                "direction": "Straight"
            },
            {
                "timestamp": 0.9,
                "direction": "Straight"
            },
            {
                "timestamp": 0.93,
                "direction": "Straight"
            },
            {
                "timestamp": 0.97,
                "direction": "Straight"
            },
            {
                "timestamp": 1.0,
                "direction": "Slight Left"
            },
            {
                "timestamp": 1.03,
                "direction": "Slight Left"
            },
            {
                "timestamp": 1.07,
                "direction": "Straight"
            },
            {
                "timestamp": 1.1,
                "direction": "Straight"
            },
            {
                "timestamp": 1.13,
                "direction": "Slight Left"
            },
            {
                "timestamp": 1.17,
                "direction": "Slight Left"
            },
            {
                "timestamp": 1.2,
                "direction": "Slight Left"
            },
            {
                "timestamp": 1.23,
                "direction": "Slight Left"
            },
            {
                "timestamp": 1.27,
                "direction": "Slight Left"
            },
            {
                "timestamp": 1.3,
                "direction": "Slight Left"
            },
            {
                "timestamp": 1.33,
                "direction": "Slight Left"
            },
            {
                "timestamp": 1.37,
                "direction": "Slight Left"
            },
            {
                "timestamp": 1.4,
                "direction": "Slight Left"
            },
            {
                "timestamp": 1.43,
                "direction": "Straight"
            },
            {
                "timestamp": 1.47,
                "direction": "Straight"
            },
            {
                "timestamp": 1.5,
                "direction": "Straight"
            },
            {
                "timestamp": 1.53,
                "direction": "Straight"
            },
            {
                "timestamp": 1.57,
                "direction": "Straight"
            },
            {
                "timestamp": 1.6,
                "direction": "Straight"
            },
            {
                "timestamp": 1.63,
                "direction": "Straight"
            },
            {
                "timestamp": 1.67,
                "direction": "Straight"
            },
            {
                "timestamp": 1.7,
                "direction": "Straight"
            },
            {
                "timestamp": 1.73,
                "direction": "Straight"
            },
            {
                "timestamp": 1.77,
                "direction": "Straight"
            },
            {
                "timestamp": 1.8,
                "direction": "Straight"
            },
            {
                "timestamp": 1.83,
                "direction": "Straight"
            },
            {
                "timestamp": 1.87,
                "direction": "Straight"
            },
            {
                "timestamp": 1.9,
                "direction": "Straight"
            },
            {
                "timestamp": 1.93,
                "direction": "Straight"
            },
            {
                "timestamp": 1.97,
                "direction": "Straight"
            },
            {
                "timestamp": 2.0,
                "direction": "Straight"
            },
            {
                "timestamp": 2.03,
                "direction": "Straight"
            },
            {
                "timestamp": 2.07,
                "direction": "Straight"
            },
            {
                "timestamp": 2.1,
                "direction": "Straight"
            },
            {
                "timestamp": 2.13,
                "direction": "Straight"
            },
            {
                "timestamp": 2.17,
                "direction": "Straight"
            },
            {
                "timestamp": 2.2,
                "direction": "Straight"
            },
            {
                "timestamp": 2.24,
                "direction": "Straight"
            },
            {
                "timestamp": 2.27,
                "direction": "Straight"
            },
            {
                "timestamp": 2.3,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.34,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.37,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.4,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.44,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.47,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.5,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.54,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.57,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.6,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.64,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.67,
                "direction": "Slight Left"
            },
            {
                "timestamp": 2.7,
                "direction": "Straight"
            },
            {
                "timestamp": 2.74,
                "direction": "Straight"
            },
            {
                "timestamp": 2.77,
                "direction": "Straight"
            },
            {
                "timestamp": 2.8,
                "direction": "Straight"
            },
            {
                "timestamp": 2.84,
                "direction": "Straight"
            },
            {
                "timestamp": 2.87,
                "direction": "Straight"
            },
            {
                "timestamp": 2.9,
                "direction": "Straight"
            },
            {
                "timestamp": 2.94,
                "direction": "Straight"
            },
            {
                "timestamp": 2.97,
                "direction": "Straight"
            },
            {
                "timestamp": 3.0,
                "direction": "Straight"
            },
            {
                "timestamp": 3.04,
                "direction": "Straight"
            },
            {
                "timestamp": 3.07,
                "direction": "Straight"
            },
            {
                "timestamp": 3.1,
                "direction": "Straight"
            },
            {
                "timestamp": 3.14,
                "direction": "Straight"
            },
            {
                "timestamp": 3.17,
                "direction": "Straight"
            },
            {
                "timestamp": 3.2,
                "direction": "Straight"
            },
            {
                "timestamp": 3.24,
                "direction": "Straight"
            },
            {
                "timestamp": 3.27,
                "direction": "Straight"
            },
            {
                "timestamp": 3.3,
                "direction": "Straight"
            },
            {
                "timestamp": 3.34,
                "direction": "Straight"
            },
            {
                "timestamp": 3.37,
                "direction": "Straight"
            },
            {
                "timestamp": 3.4,
                "direction": "Straight"
            },
            {
                "timestamp": 3.44,
                "direction": "Straight"
            },
            {
                "timestamp": 3.47,
                "direction": "Straight"
            },
            {
                "timestamp": 3.5,
                "direction": "Straight"
            },
            {
                "timestamp": 3.54,
                "direction": "Straight"
            },
            {
                "timestamp": 3.57,
                "direction": "Straight"
            },
            {
                "timestamp": 3.6,
                "direction": "Straight"
            },
            {
                "timestamp": 3.64,
                "direction": "Straight"
            },
            {
                "timestamp": 3.67,
                "direction": "Straight"
            },
            {
                "timestamp": 3.7,
                "direction": "Straight"
            },
            {
                "timestamp": 3.74,
                "direction": "Straight"
            },
            {
                "timestamp": 3.77,
                "direction": "Straight"
            },
            {
                "timestamp": 3.8,
                "direction": "Straight"
            },
            {
                "timestamp": 3.84,
                "direction": "Straight"
            },
            {
                "timestamp": 3.87,
                "direction": "Straight"
            },
            {
                "timestamp": 3.9,
                "direction": "Straight"
            },
            {
                "timestamp": 3.94,
                "direction": "Straight"
            },
            {
                "timestamp": 3.97,
                "direction": "Straight"
            },
            {
                "timestamp": 4.0,
                "direction": "Straight"
            },
            {
                "timestamp": 4.04,
                "direction": "Straight"
            },
            {
                "timestamp": 4.07,
                "direction": "Straight"
            },
            {
                "timestamp": 4.1,
                "direction": "Straight"
            },
            {
                "timestamp": 4.14,
                "direction": "Straight"
            },
            {
                "timestamp": 4.17,
                "direction": "Straight"
            },
            {
                "timestamp": 4.2,
                "direction": "Straight"
            },
            {
                "timestamp": 4.24,
                "direction": "Straight"
            },
            {
                "timestamp": 4.27,
                "direction": "Straight"
            },
            {
                "timestamp": 4.3,
                "direction": "Straight"
            },
            {
                "timestamp": 4.34,
                "direction": "Straight"
            },
            {
                "timestamp": 4.37,
                "direction": "Straight"
            },
            {
                "timestamp": 4.4,
                "direction": "Straight"
            },
            {
                "timestamp": 4.44,
                "direction": "Straight"
            },
            {
                "timestamp": 4.47,
                "direction": "Straight"
            },
            {
                "timestamp": 4.5,
                "direction": "Straight"
            },
            {
                "timestamp": 4.54,
                "direction": "Straight"
            },
            {
                "timestamp": 4.57,
                "direction": "Straight"
            },
            {
                "timestamp": 4.6,
                "direction": "Straight"
            },
            {
                "timestamp": 4.64,
                "direction": "Straight"
            },
            {
                "timestamp": 4.67,
                "direction": "Straight"
            },
            {
                "timestamp": 4.7,
                "direction": "Straight"
            },
            {
                "timestamp": 4.74,
                "direction": "Straight"
            },
            {
                "timestamp": 4.77,
                "direction": "Straight"
            },
            {
                "timestamp": 4.8,
                "direction": "Straight"
            },
            {
                "timestamp": 4.84,
                "direction": "Straight"
            },
            {
                "timestamp": 4.87,
                "direction": "Straight"
            },
            {
                "timestamp": 4.9,
                "direction": "Straight"
            },
            {
                "timestamp": 4.94,
                "direction": "Straight"
            },
            {
                "timestamp": 4.97,
                "direction": "Straight"
            },
            {
                "timestamp": 5.0,
                "direction": "Straight"
            },
            {
                "timestamp": 5.04,
                "direction": "Straight"
            },
            {
                "timestamp": 5.07,
                "direction": "Slight Left"
            },
            {
                "timestamp": 5.1,
                "direction": "Straight"
            },
            {
                "timestamp": 5.14,
                "direction": "Straight"
            },
            {
                "timestamp": 5.17,
                "direction": "Straight"
            },
            {
                "timestamp": 5.2,
                "direction": "Straight"
            },
            {
                "timestamp": 5.24,
                "direction": "Straight"
            },
            {
                "timestamp": 5.27,
                "direction": "Straight"
            },
            {
                "timestamp": 5.3,
                "direction": "Straight"
            },
            {
                "timestamp": 5.34,
                "direction": "Straight"
            },
            {
                "timestamp": 5.37,
                "direction": "Straight"
            },
            {
                "timestamp": 5.4,
                "direction": "Straight"
            },
            {
                "timestamp": 5.44,
                "direction": "Straight"
            },
            {
                "timestamp": 5.47,
                "direction": "Straight"
            },
            {
                "timestamp": 5.5,
                "direction": "Straight"
            },
            {
                "timestamp": 5.54,
                "direction": "Straight"
            },
            {
                "timestamp": 5.57,
                "direction": "Straight"
            },
            {
                "timestamp": 5.6,
                "direction": "Straight"
            },
            {
                "timestamp": 5.64,
                "direction": "Straight"
            },
            {
                "timestamp": 5.67,
                "direction": "Straight"
            },
            {
                "timestamp": 5.7,
                "direction": "Straight"
            },
            {
                "timestamp": 5.74,
                "direction": "Straight"
            },
            {
                "timestamp": 5.77,
                "direction": "Straight"
            },
            {
                "timestamp": 5.8,
                "direction": "Straight"
            },
            {
                "timestamp": 5.84,
                "direction": "Straight"
            },
            {
                "timestamp": 5.87,
                "direction": "Straight"
            },
            {
                "timestamp": 5.9,
                "direction": "Straight"
            },
            {
                "timestamp": 5.94,
                "direction": "Straight"
            },
            {
                "timestamp": 5.97,
                "direction": "Straight"
            },
            {
                "timestamp": 6.0,
                "direction": "Straight"
            },
            {
                "timestamp": 6.04,
                "direction": "Straight"
            },
            {
                "timestamp": 6.07,
                "direction": "Straight"
            },
            {
                "timestamp": 6.1,
                "direction": "Straight"
            },
            {
                "timestamp": 6.14,
                "direction": "Straight"
            },
            {
                "timestamp": 6.17,
                "direction": "Straight"
            },
            {
                "timestamp": 6.2,
                "direction": "Straight"
            },
            {
                "timestamp": 6.24,
                "direction": "Straight"
            },
            {
                "timestamp": 6.27,
                "direction": "Straight"
            },
            {
                "timestamp": 6.3,
                "direction": "Straight"
            },
            {
                "timestamp": 6.34,
                "direction": "Straight"
            },
            {
                "timestamp": 6.37,
                "direction": "Straight"
            },
            {
                "timestamp": 6.4,
                "direction": "Straight"
            },
            {
                "timestamp": 6.44,
                "direction": "Straight"
            },
            {
                "timestamp": 6.47,
                "direction": "Straight"
            },
            {
                "timestamp": 6.5,
                "direction": "Straight"
            },
            {
                "timestamp": 6.54,
                "direction": "Straight"
            },
            {
                "timestamp": 6.57,
                "direction": "Straight"
            },
            {
                "timestamp": 6.6,
                "direction": "Straight"
            },
            {
                "timestamp": 6.64,
                "direction": "Straight"
            },
            {
                "timestamp": 6.67,
                "direction": "Straight"
            },
            {
                "timestamp": 6.71,
                "direction": "Straight"
            },
            {
                "timestamp": 6.74,
                "direction": "Straight"
            },
            {
                "timestamp": 6.77,
                "direction": "Straight"
            },
            {
                "timestamp": 6.81,
                "direction": "Straight"
            },
            {
                "timestamp": 6.84,
                "direction": "Straight"
            },
            {
                "timestamp": 6.87,
                "direction": "Straight"
            },
            {
                "timestamp": 6.91,
                "direction": "Straight"
            },
            {
                "timestamp": 6.94,
                "direction": "Straight"
            },
            {
                "timestamp": 6.97,
                "direction": "Straight"
            },
            {
                "timestamp": 7.01,
                "direction": "Straight"
            },
            {
                "timestamp": 7.04,
                "direction": "Straight"
            },
            {
                "timestamp": 7.07,
                "direction": "Straight"
            },
            {
                "timestamp": 7.11,
                "direction": "Straight"
            },
            {
                "timestamp": 7.14,
                "direction": "Straight"
            },
            {
                "timestamp": 7.17,
                "direction": "Straight"
            },
            {
                "timestamp": 7.21,
                "direction": "Straight"
            },
            {
                "timestamp": 7.24,
                "direction": "Straight"
            },
            {
                "timestamp": 7.27,
                "direction": "Straight"
            },
            {
                "timestamp": 7.31,
                "direction": "Straight"
            },
            {
                "timestamp": 7.34,
                "direction": "Straight"
            },
            {
                "timestamp": 7.37,
                "direction": "Straight"
            },
            {
                "timestamp": 7.41,
                "direction": "Straight"
            },
            {
                "timestamp": 7.44,
                "direction": "Straight"
            },
            {
                "timestamp": 7.47,
                "direction": "Straight"
            },
            {
                "timestamp": 7.51,
                "direction": "Straight"
            },
            {
                "timestamp": 7.54,
                "direction": "Straight"
            },
            {
                "timestamp": 7.57,
                "direction": "Straight"
            },
            {
                "timestamp": 7.61,
                "direction": "Straight"
            },
            {
                "timestamp": 7.64,
                "direction": "Straight"
            },
            {
                "timestamp": 7.67,
                "direction": "Straight"
            },
            {
                "timestamp": 7.71,
                "direction": "Straight"
            },
            {
                "timestamp": 7.74,
                "direction": "Straight"
            },
            {
                "timestamp": 7.77,
                "direction": "Straight"
            },
            {
                "timestamp": 7.81,
                "direction": "Straight"
            },
            {
                "timestamp": 7.84,
                "direction": "Straight"
            },
            {
                "timestamp": 7.87,
                "direction": "Straight"
            },
            {
                "timestamp": 7.91,
                "direction": "Straight"
            },
            {
                "timestamp": 7.94,
                "direction": "Slight Right"
            },
            {
                "timestamp": 7.97,
                "direction": "Straight"
            },
            {
                "timestamp": 8.01,
                "direction": "Slight Right"
            },
            {
                "timestamp": 8.04,
                "direction": "Slight Right"
            },
            {
                "timestamp": 8.07,
                "direction": "Slight Right"
            },
            {
                "timestamp": 8.11,
                "direction": "Slight Right"
            },
            {
                "timestamp": 8.14,
                "direction": "Slight Right"
            },
            {
                "timestamp": 8.17,
                "direction": "Slight Right"
            },
            {
                "timestamp": 8.21,
                "direction": "Straight"
            },
            {
                "timestamp": 8.24,
                "direction": "Straight"
            },
            {
                "timestamp": 8.27,
                "direction": "Straight"
            },
            {
                "timestamp": 8.31,
                "direction": "Straight"
            },
            {
                "timestamp": 8.34,
                "direction": "Straight"
            },
            {
                "timestamp": 8.37,
                "direction": "Straight"
            },
            {
                "timestamp": 8.41,
                "direction": "Straight"
            },
            {
                "timestamp": 8.44,
                "direction": "Straight"
            },
            {
                "timestamp": 8.47,
                "direction": "Straight"
            },
            {
                "timestamp": 8.51,
                "direction": "Straight"
            },
            {
                "timestamp": 8.54,
                "direction": "Straight"
            },
            {
                "timestamp": 8.57,
                "direction": "Straight"
            },
            {
                "timestamp": 8.61,
                "direction": "Straight"
            },
            {
                "timestamp": 8.64,
                "direction": "Straight"
            },
            {
                "timestamp": 8.67,
                "direction": "Straight"
            },
            {
                "timestamp": 8.71,
                "direction": "Straight"
            },
            {
                "timestamp": 8.74,
                "direction": "Straight"
            },
            {
                "timestamp": 8.77,
                "direction": "Straight"
            },
            {
                "timestamp": 8.81,
                "direction": "Straight"
            },
            {
                "timestamp": 8.84,
                "direction": "Straight"
            },
            {
                "timestamp": 8.87,
                "direction": "Straight"
            },
            {
                "timestamp": 8.91,
                "direction": "Straight"
            },
            {
                "timestamp": 8.94,
                "direction": "Straight"
            },
            {
                "timestamp": 8.97,
                "direction": "Straight"
            },
            {
                "timestamp": 9.01,
                "direction": "Straight"
            },
            {
                "timestamp": 9.04,
                "direction": "Straight"
            },
            {
                "timestamp": 9.07,
                "direction": "Straight"
            },
            {
                "timestamp": 9.11,
                "direction": "Straight"
            },
            {
                "timestamp": 9.14,
                "direction": "Straight"
            },
            {
                "timestamp": 9.17,
                "direction": "Straight"
            },
            {
                "timestamp": 9.21,
                "direction": "Straight"
            },
            {
                "timestamp": 9.24,
                "direction": "Straight"
            },
            {
                "timestamp": 9.27,
                "direction": "Straight"
            },
            {
                "timestamp": 9.31,
                "direction": "Straight"
            },
            {
                "timestamp": 9.34,
                "direction": "Straight"
            },
            {
                "timestamp": 9.37,
                "direction": "Straight"
            },
            {
                "timestamp": 9.41,
                "direction": "Straight"
            },
            {
                "timestamp": 9.44,
                "direction": "Straight"
            },
            {
                "timestamp": 9.47,
                "direction": "Straight"
            },
            {
                "timestamp": 9.51,
                "direction": "Straight"
            },
            {
                "timestamp": 9.54,
                "direction": "Straight"
            },
            {
                "timestamp": 9.57,
                "direction": "Straight"
            },
            {
                "timestamp": 9.61,
                "direction": "Straight"
            },
            {
                "timestamp": 9.64,
                "direction": "Straight"
            },
            {
                "timestamp": 9.67,
                "direction": "Straight"
            },
            {
                "timestamp": 9.71,
                "direction": "Straight"
            },
            {
                "timestamp": 9.74,
                "direction": "Straight"
            },
            {
                "timestamp": 9.77,
                "direction": "Straight"
            },
            {
                "timestamp": 9.81,
                "direction": "Straight"
            },
            {
                "timestamp": 9.84,
                "direction": "Straight"
            },
            {
                "timestamp": 9.87,
                "direction": "Straight"
            },
            {
                "timestamp": 9.91,
                "direction": "Slight Left"
            },
            {
                "timestamp": 9.94,
                "direction": "Slight Left"
            },
            {
                "timestamp": 9.97,
                "direction": "Slight Left"
            },
            {
                "timestamp": 10.01,
                "direction": "Straight"
            },
            {
                "timestamp": 10.04,
                "direction": "Straight"
            },
            {
                "timestamp": 10.07,
                "direction": "Straight"
            },
            {
                "timestamp": 10.11,
                "direction": "Straight"
            },
            {
                "timestamp": 10.14,
                "direction": "Straight"
            },
            {
                "timestamp": 10.17,
                "direction": "Straight"
            },
            {
                "timestamp": 10.21,
                "direction": "Straight"
            },
            {
                "timestamp": 10.24,
                "direction": "Straight"
            },
            {
                "timestamp": 10.27,
                "direction": "Straight"
            },
            {
                "timestamp": 10.31,
                "direction": "Straight"
            },
            {
                "timestamp": 10.34,
                "direction": "Straight"
            },
            {
                "timestamp": 10.37,
                "direction": "Straight"
            },
            {
                "timestamp": 10.41,
                "direction": "Straight"
            },
            {
                "timestamp": 10.44,
                "direction": "Straight"
            },
            {
                "timestamp": 10.47,
                "direction": "Straight"
            },
            {
                "timestamp": 10.51,
                "direction": "Straight"
            },
            {
                "timestamp": 10.54,
                "direction": "Straight"
            },
            {
                "timestamp": 10.57,
                "direction": "Straight"
            },
            {
                "timestamp": 10.61,
                "direction": "Slight Right"
            },
            {
                "timestamp": 10.64,
                "direction": "Straight"
            },
            {
                "timestamp": 10.67,
                "direction": "Straight"
            },
            {
                "timestamp": 10.71,
                "direction": "Straight"
            },
            {
                "timestamp": 10.74,
                "direction": "Straight"
            },
            {
                "timestamp": 10.77,
                "direction": "Straight"
            },
            {
                "timestamp": 10.81,
                "direction": "Straight"
            },
            {
                "timestamp": 10.84,
                "direction": "Straight"
            },
            {
                "timestamp": 10.87,
                "direction": "Straight"
            },
            {
                "timestamp": 10.91,
                "direction": "Straight"
            },
            {
                "timestamp": 10.94,
                "direction": "Straight"
            },
            {
                "timestamp": 10.97,
                "direction": "Straight"
            },
            {
                "timestamp": 11.01,
                "direction": "Straight"
            },
            {
                "timestamp": 11.04,
                "direction": "Straight"
            },
            {
                "timestamp": 11.07,
                "direction": "Straight"
            },
            {
                "timestamp": 11.11,
                "direction": "Straight"
            },
            {
                "timestamp": 11.14,
                "direction": "Straight"
            },
            {
                "timestamp": 11.18,
                "direction": "Straight"
            },
            {
                "timestamp": 11.21,
                "direction": "Straight"
            },
            {
                "timestamp": 11.24,
                "direction": "Straight"
            },
            {
                "timestamp": 11.28,
                "direction": "Straight"
            },
            {
                "timestamp": 11.31,
                "direction": "Straight"
            },
            {
                "timestamp": 11.34,
                "direction": "Straight"
            },
            {
                "timestamp": 11.38,
                "direction": "Straight"
            },
            {
                "timestamp": 11.41,
                "direction": "Straight"
            },
            {
                "timestamp": 11.44,
                "direction": "Straight"
            },
            {
                "timestamp": 11.48,
                "direction": "Straight"
            },
            {
                "timestamp": 11.51,
                "direction": "Straight"
            },
            {
                "timestamp": 11.54,
                "direction": "Straight"
            },
            {
                "timestamp": 11.58,
                "direction": "Straight"
            },
            {
                "timestamp": 11.61,
                "direction": "Straight"
            },
            {
                "timestamp": 11.64,
                "direction": "Straight"
            },
            {
                "timestamp": 11.68,
                "direction": "Straight"
            },
            {
                "timestamp": 11.71,
                "direction": "Straight"
            },
            {
                "timestamp": 11.74,
                "direction": "Straight"
            },
            {
                "timestamp": 11.78,
                "direction": "Straight"
            },
            {
                "timestamp": 11.81,
                "direction": "Straight"
            },
            {
                "timestamp": 11.84,
                "direction": "Straight"
            },
            {
                "timestamp": 11.88,
                "direction": "Straight"
            },
            {
                "timestamp": 11.91,
                "direction": "Straight"
            },
            {
                "timestamp": 11.94,
                "direction": "Straight"
            },
            {
                "timestamp": 11.98,
                "direction": "Straight"
            },
            {
                "timestamp": 12.01,
                "direction": "Straight"
            },
            {
                "timestamp": 12.04,
                "direction": "Straight"
            },
            {
                "timestamp": 12.08,
                "direction": "Straight"
            },
            {
                "timestamp": 12.11,
                "direction": "Straight"
            },
            {
                "timestamp": 12.14,
                "direction": "Straight"
            },
            {
                "timestamp": 12.18,
                "direction": "Straight"
            },
            {
                "timestamp": 12.21,
                "direction": "Straight"
            },
            {
                "timestamp": 12.24,
                "direction": "Straight"
            },
            {
                "timestamp": 12.28,
                "direction": "Straight"
            },
            {
                "timestamp": 12.31,
                "direction": "Straight"
            },
            {
                "timestamp": 12.34,
                "direction": "Straight"
            },
            {
                "timestamp": 12.38,
                "direction": "Straight"
            },
            {
                "timestamp": 12.41,
                "direction": "Straight"
            },
            {
                "timestamp": 12.44,
                "direction": "Straight"
            },
            {
                "timestamp": 12.48,
                "direction": "Straight"
            },
            {
                "timestamp": 12.51,
                "direction": "Straight"
            },
            {
                "timestamp": 12.54,
                "direction": "Straight"
            },
            {
                "timestamp": 12.58,
                "direction": "Straight"
            },
            {
                "timestamp": 12.61,
                "direction": "Straight"
            },
            {
                "timestamp": 12.64,
                "direction": "Straight"
            },
            {
                "timestamp": 12.68,
                "direction": "Straight"
            },
            {
                "timestamp": 12.71,
                "direction": "Straight"
            },
            {
                "timestamp": 12.74,
                "direction": "Straight"
            },
            {
                "timestamp": 12.78,
                "direction": "Straight"
            },
            {
                "timestamp": 12.81,
                "direction": "Straight"
            },
            {
                "timestamp": 12.84,
                "direction": "Straight"
            },
            {
                "timestamp": 12.88,
                "direction": "Straight"
            },
            {
                "timestamp": 12.91,
                "direction": "Straight"
            },
            {
                "timestamp": 12.94,
                "direction": "Slight Right"
            },
            {
                "timestamp": 12.98,
                "direction": "Slight Right"
            },
            {
                "timestamp": 13.01,
                "direction": "Slight Right"
            },
            {
                "timestamp": 13.04,
                "direction": "Straight"
            },
            {
                "timestamp": 13.08,
                "direction": "Straight"
            },
            {
                "timestamp": 13.11,
                "direction": "Straight"
            },
            {
                "timestamp": 13.14,
                "direction": "Straight"
            },
            {
                "timestamp": 13.18,
                "direction": "Straight"
            },
            {
                "timestamp": 13.21,
                "direction": "Straight"
            },
            {
                "timestamp": 13.24,
                "direction": "Straight"
            },
            {
                "timestamp": 13.28,
                "direction": "Straight"
            },
            {
                "timestamp": 13.31,
                "direction": "Straight"
            },
            {
                "timestamp": 13.34,
                "direction": "Straight"
            },
            {
                "timestamp": 13.38,
                "direction": "Straight"
            },
            {
                "timestamp": 13.41,
                "direction": "Straight"
            },
            {
                "timestamp": 13.44,
                "direction": "Straight"
            },
            {
                "timestamp": 13.48,
                "direction": "Straight"
            },
            {
                "timestamp": 13.51,
                "direction": "Straight"
            },
            {
                "timestamp": 13.54,
                "direction": "Straight"
            },
            {
                "timestamp": 13.58,
                "direction": "Straight"
            },
            {
                "timestamp": 13.61,
                "direction": "Straight"
            },
            {
                "timestamp": 13.64,
                "direction": "Straight"
            },
            {
                "timestamp": 13.68,
                "direction": "Straight"
            },
            {
                "timestamp": 13.71,
                "direction": "Straight"
            },
            {
                "timestamp": 13.74,
                "direction": "Straight"
            },
            {
                "timestamp": 13.78,
                "direction": "Straight"
            },
            {
                "timestamp": 13.81,
                "direction": "Straight"
            },
            {
                "timestamp": 13.84,
                "direction": "Straight"
            },
            {
                "timestamp": 13.88,
                "direction": "Straight"
            },
            {
                "timestamp": 13.91,
                "direction": "Straight"
            },
            {
                "timestamp": 13.94,
                "direction": "Straight"
            },
            {
                "timestamp": 13.98,
                "direction": "Straight"
            },
            {
                "timestamp": 14.01,
                "direction": "Straight"
            },
            {
                "timestamp": 14.04,
                "direction": "Straight"
            },
            {
                "timestamp": 14.08,
                "direction": "Slight Right"
            },
            {
                "timestamp": 14.11,
                "direction": "Slight Right"
            },
            {
                "timestamp": 14.14,
                "direction": "Slight Right"
            },
            {
                "timestamp": 14.18,
                "direction": "Slight Right"
            },
            {
                "timestamp": 14.21,
                "direction": "Slight Right"
            },
            {
                "timestamp": 14.24,
                "direction": "Slight Right"
            },
            {
                "timestamp": 14.28,
                "direction": "Straight"
            },
            {
                "timestamp": 14.31,
                "direction": "Straight"
            },
            {
                "timestamp": 14.34,
                "direction": "Straight"
            },
            {
                "timestamp": 14.38,
                "direction": "Straight"
            },
            {
                "timestamp": 14.41,
                "direction": "Straight"
            },
            {
                "timestamp": 14.44,
                "direction": "Straight"
            },
            {
                "timestamp": 14.48,
                "direction": "Straight"
            },
            {
                "timestamp": 14.51,
                "direction": "Straight"
            },
            {
                "timestamp": 14.54,
                "direction": "Straight"
            },
            {
                "timestamp": 14.58,
                "direction": "Straight"
            },
            {
                "timestamp": 14.61,
                "direction": "Straight"
            },
            {
                "timestamp": 14.64,
                "direction": "Straight"
            },
            {
                "timestamp": 14.68,
                "direction": "Straight"
            },
            {
                "timestamp": 14.71,
                "direction": "Straight"
            },
            {
                "timestamp": 14.74,
                "direction": "Straight"
            },
            {
                "timestamp": 14.78,
                "direction": "Straight"
            },
            {
                "timestamp": 14.81,
                "direction": "Straight"
            },
            {
                "timestamp": 14.84,
                "direction": "Straight"
            },
            {
                "timestamp": 14.88,
                "direction": "Straight"
            },
            {
                "timestamp": 14.91,
                "direction": "Straight"
            },
            {
                "timestamp": 14.94,
                "direction": "Straight"
            },
            {
                "timestamp": 14.98,
                "direction": "Straight"
            },
            {
                "timestamp": 15.01,
                "direction": "Straight"
            },
            {
                "timestamp": 15.04,
                "direction": "Straight"
            },
            {
                "timestamp": 15.08,
                "direction": "Straight"
            },
            {
                "timestamp": 15.11,
                "direction": "Straight"
            },
            {
                "timestamp": 15.14,
                "direction": "Straight"
            },
            {
                "timestamp": 15.18,
                "direction": "Straight"
            },
            {
                "timestamp": 15.21,
                "direction": "Straight"
            },
            {
                "timestamp": 15.24,
                "direction": "Straight"
            },
            {
                "timestamp": 15.28,
                "direction": "Straight"
            },
            {
                "timestamp": 15.31,
                "direction": "Straight"
            },
            {
                "timestamp": 15.34,
                "direction": "Slight Right"
            },
            {
                "timestamp": 15.38,
                "direction": "Slight Right"
            },
            {
                "timestamp": 15.41,
                "direction": "Straight"
            },
            {
                "timestamp": 15.44,
                "direction": "Straight"
            },
            {
                "timestamp": 15.48,
                "direction": "Straight"
            },
            {
                "timestamp": 15.51,
                "direction": "Straight"
            },
            {
                "timestamp": 15.55,
                "direction": "Straight"
            },
            {
                "timestamp": 15.58,
                "direction": "Straight"
            },
            {
                "timestamp": 15.61,
                "direction": "Straight"
            },
            {
                "timestamp": 15.65,
                "direction": "Straight"
            },
            {
                "timestamp": 15.68,
                "direction": "Straight"
            },
            {
                "timestamp": 15.71,
                "direction": "Straight"
            },
            {
                "timestamp": 15.75,
                "direction": "Straight"
            },
            {
                "timestamp": 15.78,
                "direction": "Straight"
            },
            {
                "timestamp": 15.81,
                "direction": "Straight"
            },
            {
                "timestamp": 15.85,
                "direction": "Straight"
            },
            {
                "timestamp": 15.88,
                "direction": "Straight"
            },
            {
                "timestamp": 15.91,
                "direction": "Straight"
            },
            {
                "timestamp": 15.95,
                "direction": "Slight Left"
            },
            {
                "timestamp": 15.98,
                "direction": "Straight"
            },
            {
                "timestamp": 16.01,
                "direction": "Straight"
            },
            {
                "timestamp": 16.05,
                "direction": "Straight"
            },
            {
                "timestamp": 16.08,
                "direction": "Straight"
            },
            {
                "timestamp": 16.11,
                "direction": "Straight"
            },
            {
                "timestamp": 16.15,
                "direction": "Straight"
            },
            {
                "timestamp": 16.18,
                "direction": "Straight"
            },
            {
                "timestamp": 16.21,
                "direction": "Straight"
            },
            {
                "timestamp": 16.25,
                "direction": "Straight"
            },
            {
                "timestamp": 16.28,
                "direction": "Straight"
            },
            {
                "timestamp": 16.31,
                "direction": "Straight"
            },
            {
                "timestamp": 16.35,
                "direction": "Straight"
            },
            {
                "timestamp": 16.38,
                "direction": "Straight"
            },
            {
                "timestamp": 16.41,
                "direction": "Straight"
            },
            {
                "timestamp": 16.45,
                "direction": "Straight"
            },
            {
                "timestamp": 16.48,
                "direction": "Straight"
            },
            {
                "timestamp": 16.51,
                "direction": "Straight"
            },
            {
                "timestamp": 16.55,
                "direction": "Slight Right"
            },
            {
                "timestamp": 16.58,
                "direction": "Slight Right"
            },
            {
                "timestamp": 16.61,
                "direction": "Straight"
            },
            {
                "timestamp": 16.65,
                "direction": "Straight"
            },
            {
                "timestamp": 16.68,
                "direction": "Straight"
            },
            {
                "timestamp": 16.71,
                "direction": "Straight"
            },
            {
                "timestamp": 16.75,
                "direction": "Straight"
            },
            {
                "timestamp": 16.78,
                "direction": "Straight"
            },
            {
                "timestamp": 16.81,
                "direction": "Straight"
            },
            {
                "timestamp": 16.85,
                "direction": "Straight"
            },
            {
                "timestamp": 16.88,
                "direction": "Straight"
            },
            {
                "timestamp": 16.91,
                "direction": "Straight"
            },
            {
                "timestamp": 16.95,
                "direction": "Straight"
            },
            {
                "timestamp": 16.98,
                "direction": "Straight"
            },
            {
                "timestamp": 17.01,
                "direction": "Straight"
            },
            {
                "timestamp": 17.05,
                "direction": "Straight"
            },
            {
                "timestamp": 17.08,
                "direction": "Straight"
            },
            {
                "timestamp": 17.11,
                "direction": "Straight"
            },
            {
                "timestamp": 17.15,
                "direction": "Straight"
            },
            {
                "timestamp": 17.18,
                "direction": "Straight"
            },
            {
                "timestamp": 17.21,
                "direction": "Straight"
            },
            {
                "timestamp": 17.25,
                "direction": "Straight"
            },
            {
                "timestamp": 17.28,
                "direction": "Straight"
            },
            {
                "timestamp": 17.31,
                "direction": "Straight"
            },
            {
                "timestamp": 17.35,
                "direction": "Straight"
            },
            {
                "timestamp": 17.38,
                "direction": "Straight"
            },
            {
                "timestamp": 17.41,
                "direction": "Straight"
            },
            {
                "timestamp": 17.45,
                "direction": "Straight"
            },
            {
                "timestamp": 17.48,
                "direction": "Straight"
            },
            {
                "timestamp": 17.51,
                "direction": "Straight"
            },
            {
                "timestamp": 17.55,
                "direction": "Straight"
            },
            {
                "timestamp": 17.58,
                "direction": "Straight"
            },
            {
                "timestamp": 17.61,
                "direction": "Straight"
            },
            {
                "timestamp": 17.65,
                "direction": "Straight"
            },
            {
                "timestamp": 17.68,
                "direction": "Straight"
            },
            {
                "timestamp": 17.71,
                "direction": "Straight"
            },
            {
                "timestamp": 17.75,
                "direction": "Straight"
            },
            {
                "timestamp": 17.78,
                "direction": "Straight"
            },
            {
                "timestamp": 17.81,
                "direction": "Straight"
            },
            {
                "timestamp": 17.85,
                "direction": "Straight"
            },
            {
                "timestamp": 17.88,
                "direction": "Straight"
            },
            {
                "timestamp": 17.91,
                "direction": "Straight"
            },
            {
                "timestamp": 17.95,
                "direction": "Straight"
            },
            {
                "timestamp": 17.98,
                "direction": "Straight"
            },
            {
                "timestamp": 18.01,
                "direction": "Straight"
            },
            {
                "timestamp": 18.05,
                "direction": "Straight"
            },
            {
                "timestamp": 18.08,
                "direction": "Straight"
            },
            {
                "timestamp": 18.11,
                "direction": "Slight Left"
            },
            {
                "timestamp": 18.15,
                "direction": "Straight"
            },
            {
                "timestamp": 18.18,
                "direction": "Straight"
            },
            {
                "timestamp": 18.21,
                "direction": "Straight"
            },
            {
                "timestamp": 18.25,
                "direction": "Straight"
            },
            {
                "timestamp": 18.28,
                "direction": "Slight Left"
            },
            {
                "timestamp": 18.31,
                "direction": "Slight Left"
            },
            {
                "timestamp": 18.35,
                "direction": "Slight Left"
            },
            {
                "timestamp": 18.38,
                "direction": "Slight Left"
            },
            {
                "timestamp": 18.41,
                "direction": "Straight"
            },
            {
                "timestamp": 18.45,
                "direction": "Straight"
            },
            {
                "timestamp": 18.48,
                "direction": "Straight"
            },
            {
                "timestamp": 18.51,
                "direction": "Straight"
            },
            {
                "timestamp": 18.55,
                "direction": "Straight"
            },
            {
                "timestamp": 18.58,
                "direction": "Straight"
            },
            {
                "timestamp": 18.61,
                "direction": "Straight"
            },
            {
                "timestamp": 18.65,
                "direction": "Straight"
            },
            {
                "timestamp": 18.68,
                "direction": "Straight"
            },
            {
                "timestamp": 18.71,
                "direction": "Straight"
            },
            {
                "timestamp": 18.75,
                "direction": "Straight"
            },
            {
                "timestamp": 18.78,
                "direction": "Straight"
            },
            {
                "timestamp": 18.81,
                "direction": "Straight"
            },
            {
                "timestamp": 18.85,
                "direction": "Straight"
            },
            {
                "timestamp": 18.88,
                "direction": "Straight"
            },
            {
                "timestamp": 18.91,
                "direction": "Straight"
            },
            {
                "timestamp": 18.95,
                "direction": "Straight"
            },
            {
                "timestamp": 18.98,
                "direction": "Straight"
            },
            {
                "timestamp": 19.01,
                "direction": "Straight"
            },
            {
                "timestamp": 19.05,
                "direction": "Straight"
            },
            {
                "timestamp": 19.08,
                "direction": "Straight"
            },
            {
                "timestamp": 19.11,
                "direction": "Straight"
            },
            {
                "timestamp": 19.15,
                "direction": "Straight"
            },
            {
                "timestamp": 19.18,
                "direction": "Straight"
            },
            {
                "timestamp": 19.21,
                "direction": "Straight"
            },
            {
                "timestamp": 19.25,
                "direction": "Straight"
            },
            {
                "timestamp": 19.28,
                "direction": "Straight"
            },
            {
                "timestamp": 19.31,
                "direction": "Straight"
            },
            {
                "timestamp": 19.35,
                "direction": "Straight"
            },
            {
                "timestamp": 19.38,
                "direction": "Straight"
            },
            {
                "timestamp": 19.41,
                "direction": "Straight"
            },
            {
                "timestamp": 19.45,
                "direction": "Straight"
            },
            {
                "timestamp": 19.48,
                "direction": "Straight"
            },
            {
                "timestamp": 19.51,
                "direction": "Straight"
            },
            {
                "timestamp": 19.55,
                "direction": "Straight"
            },
            {
                "timestamp": 19.58,
                "direction": "Straight"
            },
            {
                "timestamp": 19.61,
                "direction": "Straight"
            },
            {
                "timestamp": 19.65,
                "direction": "Straight"
            },
            {
                "timestamp": 19.68,
                "direction": "Straight"
            },
            {
                "timestamp": 19.71,
                "direction": "Straight"
            },
            {
                "timestamp": 19.75,
                "direction": "Straight"
            },
            {
                "timestamp": 19.78,
                "direction": "Straight"
            },
            {
                "timestamp": 19.81,
                "direction": "Straight"
            },
            {
                "timestamp": 19.85,
                "direction": "Straight"
            },
            {
                "timestamp": 19.88,
                "direction": "Straight"
            },
            {
                "timestamp": 19.91,
                "direction": "Straight"
            },
            {
                "timestamp": 19.95,
                "direction": "Straight"
            },
            {
                "timestamp": 19.98,
                "direction": "Straight"
            },
            {
                "timestamp": 20.02,
                "direction": "Straight"
            },
            {
                "timestamp": 20.05,
                "direction": "Straight"
            },
            {
                "timestamp": 20.08,
                "direction": "Straight"
            },
            {
                "timestamp": 20.12,
                "direction": "Straight"
            },
            {
                "timestamp": 20.15,
                "direction": "Straight"
            },
            {
                "timestamp": 20.18,
                "direction": "Slight Right"
            },
            {
                "timestamp": 20.22,
                "direction": "Slight Right"
            },
            {
                "timestamp": 20.25,
                "direction": "Slight Right"
            },
            {
                "timestamp": 20.28,
                "direction": "Straight"
            },
            {
                "timestamp": 20.32,
                "direction": "Straight"
            },
            {
                "timestamp": 20.35,
                "direction": "Straight"
            },
            {
                "timestamp": 20.38,
                "direction": "Straight"
            },
            {
                "timestamp": 20.42,
                "direction": "Straight"
            },
            {
                "timestamp": 20.45,
                "direction": "Straight"
            },
            {
                "timestamp": 20.48,
                "direction": "Straight"
            },
            {
                "timestamp": 20.52,
                "direction": "Straight"
            },
            {
                "timestamp": 20.55,
                "direction": "Straight"
            },
            {
                "timestamp": 20.58,
                "direction": "Straight"
            },
            {
                "timestamp": 20.62,
                "direction": "Straight"
            },
            {
                "timestamp": 20.65,
                "direction": "Straight"
            },
            {
                "timestamp": 20.68,
                "direction": "Straight"
            },
            {
                "timestamp": 20.72,
                "direction": "Straight"
            },
            {
                "timestamp": 20.75,
                "direction": "Straight"
            },
            {
                "timestamp": 20.78,
                "direction": "Straight"
            },
            {
                "timestamp": 20.82,
                "direction": "Straight"
            },
            {
                "timestamp": 20.85,
                "direction": "Straight"
            },
            {
                "timestamp": 20.88,
                "direction": "Straight"
            },
            {
                "timestamp": 20.92,
                "direction": "Straight"
            },
            {
                "timestamp": 20.95,
                "direction": "Straight"
            },
            {
                "timestamp": 20.98,
                "direction": "Straight"
            },
            {
                "timestamp": 21.02,
                "direction": "Straight"
            },
            {
                "timestamp": 21.05,
                "direction": "Straight"
            },
            {
                "timestamp": 21.08,
                "direction": "Straight"
            },
            {
                "timestamp": 21.12,
                "direction": "Straight"
            },
            {
                "timestamp": 21.15,
                "direction": "Straight"
            },
            {
                "timestamp": 21.18,
                "direction": "Straight"
            },
            {
                "timestamp": 21.22,
                "direction": "Straight"
            },
            {
                "timestamp": 21.25,
                "direction": "Straight"
            },
            {
                "timestamp": 21.28,
                "direction": "Slight Right"
            },
            {
                "timestamp": 21.32,
                "direction": "Slight Right"
            },
            {
                "timestamp": 21.35,
                "direction": "Slight Right"
            },
            {
                "timestamp": 21.38,
                "direction": "Slight Right"
            },
            {
                "timestamp": 21.42,
                "direction": "Slight Right"
            },
            {
                "timestamp": 21.45,
                "direction": "Slight Right"
            },
            {
                "timestamp": 21.48,
                "direction": "Straight"
            },
            {
                "timestamp": 21.52,
                "direction": "Straight"
            },
            {
                "timestamp": 21.55,
                "direction": "Straight"
            },
            {
                "timestamp": 21.58,
                "direction": "Straight"
            },
            {
                "timestamp": 21.62,
                "direction": "Straight"
            },
            {
                "timestamp": 21.65,
                "direction": "Straight"
            },
            {
                "timestamp": 21.68,
                "direction": "Straight"
            },
            {
                "timestamp": 21.72,
                "direction": "Straight"
            },
            {
                "timestamp": 21.75,
                "direction": "Straight"
            },
            {
                "timestamp": 21.78,
                "direction": "Straight"
            },
            {
                "timestamp": 21.82,
                "direction": "Straight"
            },
            {
                "timestamp": 21.85,
                "direction": "Straight"
            },
            {
                "timestamp": 21.88,
                "direction": "Straight"
            },
            {
                "timestamp": 21.92,
                "direction": "Straight"
            },
            {
                "timestamp": 21.95,
                "direction": "Straight"
            },
            {
                "timestamp": 21.98,
                "direction": "Straight"
            },
            {
                "timestamp": 22.02,
                "direction": "Straight"
            },
            {
                "timestamp": 22.05,
                "direction": "Straight"
            },
            {
                "timestamp": 22.08,
                "direction": "Straight"
            },
            {
                "timestamp": 22.12,
                "direction": "Straight"
            },
            {
                "timestamp": 22.15,
                "direction": "Straight"
            },
            {
                "timestamp": 22.18,
                "direction": "Straight"
            },
            {
                "timestamp": 22.22,
                "direction": "Straight"
            },
            {
                "timestamp": 22.25,
                "direction": "Straight"
            },
            {
                "timestamp": 22.28,
                "direction": "Straight"
            },
            {
                "timestamp": 22.32,
                "direction": "Straight"
            },
            {
                "timestamp": 22.35,
                "direction": "Straight"
            },
            {
                "timestamp": 22.38,
                "direction": "Straight"
            },
            {
                "timestamp": 22.42,
                "direction": "Straight"
            },
            {
                "timestamp": 22.45,
                "direction": "Straight"
            },
            {
                "timestamp": 22.48,
                "direction": "Straight"
            },
            {
                "timestamp": 22.52,
                "direction": "Straight"
            },
            {
                "timestamp": 22.55,
                "direction": "Straight"
            },
            {
                "timestamp": 22.58,
                "direction": "Straight"
            },
            {
                "timestamp": 22.62,
                "direction": "Straight"
            },
            {
                "timestamp": 22.65,
                "direction": "Straight"
            },
            {
                "timestamp": 22.68,
                "direction": "Straight"
            },
            {
                "timestamp": 22.72,
                "direction": "Straight"
            },
            {
                "timestamp": 22.75,
                "direction": "Straight"
            },
            {
                "timestamp": 22.78,
                "direction": "Straight"
            },
            {
                "timestamp": 22.82,
                "direction": "Straight"
            },
            {
                "timestamp": 22.85,
                "direction": "Straight"
            },
            {
                "timestamp": 22.88,
                "direction": "Straight"
            },
            {
                "timestamp": 22.92,
                "direction": "Straight"
            },
            {
                "timestamp": 22.95,
                "direction": "Straight"
            },
            {
                "timestamp": 22.98,
                "direction": "Straight"
            },
            {
                "timestamp": 23.02,
                "direction": "Straight"
            },
            {
                "timestamp": 23.05,
                "direction": "Straight"
            },
            {
                "timestamp": 23.08,
                "direction": "Straight"
            },
            {
                "timestamp": 23.12,
                "direction": "Straight"
            },
            {
                "timestamp": 23.15,
                "direction": "Straight"
            },
            {
                "timestamp": 23.18,
                "direction": "Straight"
            },
            {
                "timestamp": 23.22,
                "direction": "Straight"
            },
            {
                "timestamp": 23.25,
                "direction": "Straight"
            },
            {
                "timestamp": 23.28,
                "direction": "Straight"
            },
            {
                "timestamp": 23.32,
                "direction": "Straight"
            },
            {
                "timestamp": 23.35,
                "direction": "Straight"
            },
            {
                "timestamp": 23.38,
                "direction": "Straight"
            },
            {
                "timestamp": 23.42,
                "direction": "Straight"
            },
            {
                "timestamp": 23.45,
                "direction": "Straight"
            },
            {
                "timestamp": 23.48,
                "direction": "Straight"
            },
            {
                "timestamp": 23.52,
                "direction": "Straight"
            },
            {
                "timestamp": 23.55,
                "direction": "Straight"
            },
            {
                "timestamp": 23.58,
                "direction": "Straight"
            },
            {
                "timestamp": 23.62,
                "direction": "Straight"
            },
            {
                "timestamp": 23.65,
                "direction": "Straight"
            },
            {
                "timestamp": 23.68,
                "direction": "Straight"
            },
            {
                "timestamp": 23.72,
                "direction": "Slight Right"
            },
            {
                "timestamp": 23.75,
                "direction": "Slight Right"
            },
            {
                "timestamp": 23.78,
                "direction": "Slight Right"
            },
            {
                "timestamp": 23.82,
                "direction": "Slight Right"
            },
            {
                "timestamp": 23.85,
                "direction": "Slight Right"
            },
            {
                "timestamp": 23.88,
                "direction": "Slight Right"
            },
            {
                "timestamp": 23.92,
                "direction": "Straight"
            },
            {
                "timestamp": 23.95,
                "direction": "Straight"
            },
            {
                "timestamp": 23.98,
                "direction": "Straight"
            },
            {
                "timestamp": 24.02,
                "direction": "Straight"
            },
            {
                "timestamp": 24.05,
                "direction": "Straight"
            },
            {
                "timestamp": 24.08,
                "direction": "Straight"
            },
            {
                "timestamp": 24.12,
                "direction": "Straight"
            },
            {
                "timestamp": 24.15,
                "direction": "Straight"
            },
            {
                "timestamp": 24.18,
                "direction": "Straight"
            },
            {
                "timestamp": 24.22,
                "direction": "Straight"
            },
            {
                "timestamp": 24.25,
                "direction": "Straight"
            },
            {
                "timestamp": 24.28,
                "direction": "Straight"
            },
            {
                "timestamp": 24.32,
                "direction": "Straight"
            },
            {
                "timestamp": 24.35,
                "direction": "Straight"
            },
            {
                "timestamp": 24.39,
                "direction": "Straight"
            },
            {
                "timestamp": 24.42,
                "direction": "Straight"
            },
            {
                "timestamp": 24.45,
                "direction": "Straight"
            },
            {
                "timestamp": 24.49,
                "direction": "Straight"
            },
            {
                "timestamp": 24.52,
                "direction": "Straight"
            },
            {
                "timestamp": 24.55,
                "direction": "Straight"
            },
            {
                "timestamp": 24.59,
                "direction": "Straight"
            },
            {
                "timestamp": 24.62,
                "direction": "Straight"
            },
            {
                "timestamp": 24.65,
                "direction": "Straight"
            },
            {
                "timestamp": 24.69,
                "direction": "Straight"
            },
            {
                "timestamp": 24.72,
                "direction": "Straight"
            },
            {
                "timestamp": 24.75,
                "direction": "Straight"
            },
            {
                "timestamp": 24.79,
                "direction": "Straight"
            },
            {
                "timestamp": 24.82,
                "direction": "Straight"
            },
            {
                "timestamp": 24.85,
                "direction": "Straight"
            },
            {
                "timestamp": 24.89,
                "direction": "Straight"
            },
            {
                "timestamp": 24.92,
                "direction": "Slight Right"
            },
            {
                "timestamp": 24.95,
                "direction": "Slight Right"
            },
            {
                "timestamp": 24.99,
                "direction": "Slight Right"
            },
            {
                "timestamp": 25.02,
                "direction": "Slight Right"
            },
            {
                "timestamp": 25.05,
                "direction": "Slight Right"
            },
            {
                "timestamp": 25.09,
                "direction": "Straight"
            },
            {
                "timestamp": 25.12,
                "direction": "Straight"
            },
            {
                "timestamp": 25.15,
                "direction": "Straight"
            },
            {
                "timestamp": 25.19,
                "direction": "Straight"
            },
            {
                "timestamp": 25.22,
                "direction": "Straight"
            },
            {
                "timestamp": 25.25,
                "direction": "Straight"
            },
            {
                "timestamp": 25.29,
                "direction": "Straight"
            },
            {
                "timestamp": 25.32,
                "direction": "Straight"
            },
            {
                "timestamp": 25.35,
                "direction": "Straight"
            },
            {
                "timestamp": 25.39,
                "direction": "Straight"
            },
            {
                "timestamp": 25.42,
                "direction": "Straight"
            },
            {
                "timestamp": 25.45,
                "direction": "Straight"
            },
            {
                "timestamp": 25.49,
                "direction": "Straight"
            },
            {
                "timestamp": 25.52,
                "direction": "Straight"
            },
            {
                "timestamp": 25.55,
                "direction": "Straight"
            },
            {
                "timestamp": 25.59,
                "direction": "Straight"
            },
            {
                "timestamp": 25.62,
                "direction": "Straight"
            },
            {
                "timestamp": 25.65,
                "direction": "Straight"
            },
            {
                "timestamp": 25.69,
                "direction": "Straight"
            },
            {
                "timestamp": 25.72,
                "direction": "Straight"
            },
            {
                "timestamp": 25.75,
                "direction": "Straight"
            },
            {
                "timestamp": 25.79,
                "direction": "Straight"
            },
            {
                "timestamp": 25.82,
                "direction": "Straight"
            },
            {
                "timestamp": 25.85,
                "direction": "Straight"
            },
            {
                "timestamp": 25.89,
                "direction": "Straight"
            },
            {
                "timestamp": 25.92,
                "direction": "Straight"
            },
            {
                "timestamp": 25.95,
                "direction": "Straight"
            },
            {
                "timestamp": 25.99,
                "direction": "Straight"
            },
            {
                "timestamp": 26.02,
                "direction": "Straight"
            },
            {
                "timestamp": 26.05,
                "direction": "Straight"
            },
            {
                "timestamp": 26.09,
                "direction": "Slight Right"
            },
            {
                "timestamp": 26.12,
                "direction": "Slight Right"
            },
            {
                "timestamp": 26.15,
                "direction": "Slight Right"
            },
            {
                "timestamp": 26.19,
                "direction": "Slight Right"
            },
            {
                "timestamp": 26.22,
                "direction": "Slight Right"
            },
            {
                "timestamp": 26.25,
                "direction": "Slight Right"
            },
            {
                "timestamp": 26.29,
                "direction": "Straight"
            },
            {
                "timestamp": 26.32,
                "direction": "Straight"
            },
            {
                "timestamp": 26.35,
                "direction": "Straight"
            },
            {
                "timestamp": 26.39,
                "direction": "Straight"
            },
            {
                "timestamp": 26.42,
                "direction": "Straight"
            },
            {
                "timestamp": 26.45,
                "direction": "Straight"
            },
            {
                "timestamp": 26.49,
                "direction": "Straight"
            },
            {
                "timestamp": 26.52,
                "direction": "Straight"
            },
            {
                "timestamp": 26.55,
                "direction": "Straight"
            },
            {
                "timestamp": 26.59,
                "direction": "Straight"
            },
            {
                "timestamp": 26.62,
                "direction": "Straight"
            },
            {
                "timestamp": 26.65,
                "direction": "Straight"
            },
            {
                "timestamp": 26.69,
                "direction": "Straight"
            },
            {
                "timestamp": 26.72,
                "direction": "Straight"
            },
            {
                "timestamp": 26.75,
                "direction": "Straight"
            },
            {
                "timestamp": 26.79,
                "direction": "Straight"
            },
            {
                "timestamp": 26.82,
                "direction": "Straight"
            },
            {
                "timestamp": 26.85,
                "direction": "Straight"
            },
            {
                "timestamp": 26.89,
                "direction": "Straight"
            },
            {
                "timestamp": 26.92,
                "direction": "Straight"
            },
            {
                "timestamp": 26.95,
                "direction": "Straight"
            },
            {
                "timestamp": 26.99,
                "direction": "Straight"
            },
            {
                "timestamp": 27.02,
                "direction": "Straight"
            },
            {
                "timestamp": 27.05,
                "direction": "Straight"
            },
            {
                "timestamp": 27.09,
                "direction": "Straight"
            },
            {
                "timestamp": 27.12,
                "direction": "Straight"
            },
            {
                "timestamp": 27.15,
                "direction": "Straight"
            },
            {
                "timestamp": 27.19,
                "direction": "Straight"
            },
            {
                "timestamp": 27.22,
                "direction": "Straight"
            },
            {
                "timestamp": 27.25,
                "direction": "Straight"
            },
            {
                "timestamp": 27.29,
                "direction": "Slight Right"
            },
            {
                "timestamp": 27.32,
                "direction": "Slight Right"
            },
            {
                "timestamp": 27.35,
                "direction": "Slight Right"
            },
            {
                "timestamp": 27.39,
                "direction": "Slight Right"
            },
            {
                "timestamp": 27.42,
                "direction": "Straight"
            },
            {
                "timestamp": 27.45,
                "direction": "Straight"
            },
            {
                "timestamp": 27.49,
                "direction": "Straight"
            },
            {
                "timestamp": 27.52,
                "direction": "Straight"
            },
            {
                "timestamp": 27.55,
                "direction": "Straight"
            },
            {
                "timestamp": 27.59,
                "direction": "Straight"
            },
            {
                "timestamp": 27.62,
                "direction": "Straight"
            },
            {
                "timestamp": 27.65,
                "direction": "Straight"
            },
            {
                "timestamp": 27.69,
                "direction": "Straight"
            },
            {
                "timestamp": 27.72,
                "direction": "Straight"
            },
            {
                "timestamp": 27.75,
                "direction": "Straight"
            },
            {
                "timestamp": 27.79,
                "direction": "Straight"
            },
            {
                "timestamp": 27.82,
                "direction": "Straight"
            },
            {
                "timestamp": 27.85,
                "direction": "Straight"
            },
            {
                "timestamp": 27.89,
                "direction": "Straight"
            },
            {
                "timestamp": 27.92,
                "direction": "Straight"
            },
            {
                "timestamp": 27.95,
                "direction": "Straight"
            },
            {
                "timestamp": 27.99,
                "direction": "Straight"
            },
            {
                "timestamp": 28.02,
                "direction": "Straight"
            },
            {
                "timestamp": 28.05,
                "direction": "Straight"
            },
            {
                "timestamp": 28.09,
                "direction": "Straight"
            },
            {
                "timestamp": 28.12,
                "direction": "Straight"
            },
            {
                "timestamp": 28.15,
                "direction": "Straight"
            },
            {
                "timestamp": 28.19,
                "direction": "Straight"
            },
            {
                "timestamp": 28.22,
                "direction": "Straight"
            },
            {
                "timestamp": 28.25,
                "direction": "Straight"
            },
            {
                "timestamp": 28.29,
                "direction": "Straight"
            },
            {
                "timestamp": 28.32,
                "direction": "Straight"
            },
            {
                "timestamp": 28.35,
                "direction": "Straight"
            },
            {
                "timestamp": 28.39,
                "direction": "Straight"
            },
            {
                "timestamp": 28.42,
                "direction": "Straight"
            },
            {
                "timestamp": 28.45,
                "direction": "Straight"
            },
            {
                "timestamp": 28.49,
                "direction": "Straight"
            },
            {
                "timestamp": 28.52,
                "direction": "Slight Right"
            },
            {
                "timestamp": 28.55,
                "direction": "Straight"
            },
            {
                "timestamp": 28.59,
                "direction": "Straight"
            },
            {
                "timestamp": 28.62,
                "direction": "Straight"
            },
            {
                "timestamp": 28.65,
                "direction": "Straight"
            },
            {
                "timestamp": 28.69,
                "direction": "Straight"
            },
            {
                "timestamp": 28.72,
                "direction": "Straight"
            },
            {
                "timestamp": 28.75,
                "direction": "Straight"
            },
            {
                "timestamp": 28.79,
                "direction": "Straight"
            },
            {
                "timestamp": 28.82,
                "direction": "Straight"
            },
            {
                "timestamp": 28.86,
                "direction": "Straight"
            },
            {
                "timestamp": 28.89,
                "direction": "Straight"
            },
            {
                "timestamp": 28.92,
                "direction": "Straight"
            },
            {
                "timestamp": 28.96,
                "direction": "Straight"
            },
            {
                "timestamp": 28.99,
                "direction": "Straight"
            },
            {
                "timestamp": 29.02,
                "direction": "Straight"
            },
            {
                "timestamp": 29.06,
                "direction": "Straight"
            },
            {
                "timestamp": 29.09,
                "direction": "Straight"
            },
            {
                "timestamp": 29.12,
                "direction": "Straight"
            },
            {
                "timestamp": 29.16,
                "direction": "Straight"
            },
            {
                "timestamp": 29.19,
                "direction": "Straight"
            },
            {
                "timestamp": 29.22,
                "direction": "Straight"
            },
            {
                "timestamp": 29.26,
                "direction": "Straight"
            },
            {
                "timestamp": 29.29,
                "direction": "Straight"
            },
            {
                "timestamp": 29.32,
                "direction": "Straight"
            },
            {
                "timestamp": 29.36,
                "direction": "Straight"
            },
            {
                "timestamp": 29.39,
                "direction": "Straight"
            },
            {
                "timestamp": 29.42,
                "direction": "Straight"
            },
            {
                "timestamp": 29.46,
                "direction": "Straight"
            },
            {
                "timestamp": 29.49,
                "direction": "Straight"
            },
            {
                "timestamp": 29.52,
                "direction": "Straight"
            },
            {
                "timestamp": 29.56,
                "direction": "Straight"
            },
            {
                "timestamp": 29.59,
                "direction": "Straight"
            },
            {
                "timestamp": 29.62,
                "direction": "Straight"
            },
            {
                "timestamp": 29.66,
                "direction": "Straight"
            },
            {
                "timestamp": 29.69,
                "direction": "Straight"
            },
            {
                "timestamp": 29.72,
                "direction": "Straight"
            },
            {
                "timestamp": 29.76,
                "direction": "Straight"
            },
            {
                "timestamp": 29.79,
                "direction": "Straight"
            },
            {
                "timestamp": 29.82,
                "direction": "Straight"
            },
            {
                "timestamp": 29.86,
                "direction": "Straight"
            },
            {
                "timestamp": 29.89,
                "direction": "Straight"
            },
            {
                "timestamp": 29.92,
                "direction": "Straight"
            },
            {
                "timestamp": 29.96,
                "direction": "Straight"
            },
            {
                "timestamp": 29.99,
                "direction": "Straight"
            },
            {
                "timestamp": 30.02,
                "direction": "Straight"
            },
            {
                "timestamp": 30.06,
                "direction": "Straight"
            },
            {
                "timestamp": 30.09,
                "direction": "Straight"
            },
            {
                "timestamp": 30.12,
                "direction": "Straight"
            },
            {
                "timestamp": 30.16,
                "direction": "Straight"
            },
            {
                "timestamp": 30.19,
                "direction": "Straight"
            },
            {
                "timestamp": 30.22,
                "direction": "Straight"
            },
            {
                "timestamp": 30.26,
                "direction": "Straight"
            },
            {
                "timestamp": 30.29,
                "direction": "Straight"
            },
            {
                "timestamp": 30.32,
                "direction": "Straight"
            },
            {
                "timestamp": 30.36,
                "direction": "Straight"
            },
            {
                "timestamp": 30.39,
                "direction": "Straight"
            },
            {
                "timestamp": 30.42,
                "direction": "Straight"
            },
            {
                "timestamp": 30.46,
                "direction": "Straight"
            },
            {
                "timestamp": 30.49,
                "direction": "Straight"
            },
            {
                "timestamp": 30.52,
                "direction": "Straight"
            },
            {
                "timestamp": 30.56,
                "direction": "Straight"
            },
            {
                "timestamp": 30.59,
                "direction": "Straight"
            },
            {
                "timestamp": 30.62,
                "direction": "Straight"
            },
            {
                "timestamp": 30.66,
                "direction": "Straight"
            },
            {
                "timestamp": 30.69,
                "direction": "Straight"
            },
            {
                "timestamp": 30.72,
                "direction": "Straight"
            },
            {
                "timestamp": 30.76,
                "direction": "Straight"
            },
            {
                "timestamp": 30.79,
                "direction": "Straight"
            },
            {
                "timestamp": 30.82,
                "direction": "Slight Right"
            },
            {
                "timestamp": 30.86,
                "direction": "Slight Right"
            },
            {
                "timestamp": 30.89,
                "direction": "Slight Right"
            },
            {
                "timestamp": 30.92,
                "direction": "Slight Right"
            },
            {
                "timestamp": 30.96,
                "direction": "Straight"
            },
            {
                "timestamp": 30.99,
                "direction": "Straight"
            },
            {
                "timestamp": 31.02,
                "direction": "Straight"
            },
            {
                "timestamp": 31.06,
                "direction": "Straight"
            },
            {
                "timestamp": 31.09,
                "direction": "Straight"
            },
            {
                "timestamp": 31.12,
                "direction": "Straight"
            },
            {
                "timestamp": 31.16,
                "direction": "Straight"
            },
            {
                "timestamp": 31.19,
                "direction": "Straight"
            },
            {
                "timestamp": 31.22,
                "direction": "Straight"
            },
            {
                "timestamp": 31.26,
                "direction": "Straight"
            },
            {
                "timestamp": 31.29,
                "direction": "Straight"
            },
            {
                "timestamp": 31.32,
                "direction": "Straight"
            },
            {
                "timestamp": 31.36,
                "direction": "Straight"
            },
            {
                "timestamp": 31.39,
                "direction": "Straight"
            },
            {
                "timestamp": 31.42,
                "direction": "Slight Left"
            },
            {
                "timestamp": 31.46,
                "direction": "Slight Left"
            },
            {
                "timestamp": 31.49,
                "direction": "Slight Left"
            },
            {
                "timestamp": 31.52,
                "direction": "Slight Left"
            },
            {
                "timestamp": 31.56,
                "direction": "Straight"
            },
            {
                "timestamp": 31.59,
                "direction": "Straight"
            },
            {
                "timestamp": 31.62,
                "direction": "Straight"
            },
            {
                "timestamp": 31.66,
                "direction": "Straight"
            },
            {
                "timestamp": 31.69,
                "direction": "Straight"
            },
            {
                "timestamp": 31.72,
                "direction": "Straight"
            },
            {
                "timestamp": 31.76,
                "direction": "Straight"
            },
            {
                "timestamp": 31.79,
                "direction": "Straight"
            },
            {
                "timestamp": 31.82,
                "direction": "Straight"
            },
            {
                "timestamp": 31.86,
                "direction": "Straight"
            },
            {
                "timestamp": 31.89,
                "direction": "Straight"
            },
            {
                "timestamp": 31.92,
                "direction": "Straight"
            },
            {
                "timestamp": 31.96,
                "direction": "Straight"
            },
            {
                "timestamp": 31.99,
                "direction": "Straight"
            },
            {
                "timestamp": 32.02,
                "direction": "Straight"
            },
            {
                "timestamp": 32.06,
                "direction": "Straight"
            },
            {
                "timestamp": 32.09,
                "direction": "Straight"
            },
            {
                "timestamp": 32.12,
                "direction": "Straight"
            },
            {
                "timestamp": 32.16,
                "direction": "Straight"
            },
            {
                "timestamp": 32.19,
                "direction": "Straight"
            },
            {
                "timestamp": 32.22,
                "direction": "Straight"
            },
            {
                "timestamp": 32.26,
                "direction": "Straight"
            },
            {
                "timestamp": 32.29,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.32,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.36,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.39,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.42,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.46,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.49,
                "direction": "Left"
            },
            {
                "timestamp": 32.52,
                "direction": "Left"
            },
            {
                "timestamp": 32.56,
                "direction": "Left"
            },
            {
                "timestamp": 32.59,
                "direction": "Left"
            },
            {
                "timestamp": 32.62,
                "direction": "Left"
            },
            {
                "timestamp": 32.66,
                "direction": "Left"
            },
            {
                "timestamp": 32.69,
                "direction": "Left"
            },
            {
                "timestamp": 32.72,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.76,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.79,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.82,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.86,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.89,
                "direction": "Slight Left"
            },
            {
                "timestamp": 32.92,
                "direction": "Straight"
            },
            {
                "timestamp": 32.96,
                "direction": "Straight"
            },
            {
                "timestamp": 32.99,
                "direction": "Straight"
            },
            {
                "timestamp": 33.02,
                "direction": "Straight"
            },
            {
                "timestamp": 33.06,
                "direction": "Straight"
            },
            {
                "timestamp": 33.09,
                "direction": "Straight"
            },
            {
                "timestamp": 33.12,
                "direction": "Straight"
            },
            {
                "timestamp": 33.16,
                "direction": "Straight"
            },
            {
                "timestamp": 33.19,
                "direction": "Straight"
            },
            {
                "timestamp": 33.22,
                "direction": "Straight"
            },
            {
                "timestamp": 33.26,
                "direction": "Straight"
            },
            {
                "timestamp": 33.29,
                "direction": "Straight"
            },
            {
                "timestamp": 33.33,
                "direction": "Straight"
            },
            {
                "timestamp": 33.36,
                "direction": "Straight"
            },
            {
                "timestamp": 33.39,
                "direction": "Straight"
            },
            {
                "timestamp": 33.43,
                "direction": "Straight"
            },
            {
                "timestamp": 33.46,
                "direction": "Straight"
            },
            {
                "timestamp": 33.49,
                "direction": "Straight"
            },
            {
                "timestamp": 33.53,
                "direction": "Straight"
            },
            {
                "timestamp": 33.56,
                "direction": "Straight"
            },
            {
                "timestamp": 33.59,
                "direction": "Straight"
            },
            {
                "timestamp": 33.63,
                "direction": "Straight"
            },
            {
                "timestamp": 33.66,
                "direction": "Straight"
            },
            {
                "timestamp": 33.69,
                "direction": "Slight Left"
            },
            {
                "timestamp": 33.73,
                "direction": "Slight Left"
            },
            {
                "timestamp": 33.76,
                "direction": "Slight Left"
            },
            {
                "timestamp": 33.79,
                "direction": "Slight Left"
            },
            {
                "timestamp": 33.83,
                "direction": "Slight Left"
            },
            {
                "timestamp": 33.86,
                "direction": "Slight Left"
            },
            {
                "timestamp": 33.89,
                "direction": "Slight Left"
            },
            {
                "timestamp": 33.93,
                "direction": "Slight Left"
            },
            {
                "timestamp": 33.96,
                "direction": "Slight Left"
            },
            {
                "timestamp": 33.99,
                "direction": "Straight"
            },
            {
                "timestamp": 34.03,
                "direction": "Slight Left"
            },
            {
                "timestamp": 34.06,
                "direction": "Straight"
            },
            {
                "timestamp": 34.09,
                "direction": "Straight"
            },
            {
                "timestamp": 34.13,
                "direction": "Straight"
            },
            {
                "timestamp": 34.16,
                "direction": "Straight"
            },
            {
                "timestamp": 34.19,
                "direction": "Straight"
            },
            {
                "timestamp": 34.23,
                "direction": "Straight"
            },
            {
                "timestamp": 34.26,
                "direction": "Straight"
            },
            {
                "timestamp": 34.29,
                "direction": "Straight"
            },
            {
                "timestamp": 34.33,
                "direction": "Straight"
            },
            {
                "timestamp": 34.36,
                "direction": "Straight"
            },
            {
                "timestamp": 34.39,
                "direction": "Straight"
            },
            {
                "timestamp": 34.43,
                "direction": "Straight"
            },
            {
                "timestamp": 34.46,
                "direction": "Straight"
            },
            {
                "timestamp": 34.49,
                "direction": "Straight"
            },
            {
                "timestamp": 34.53,
                "direction": "Straight"
            },
            {
                "timestamp": 34.56,
                "direction": "Straight"
            },
            {
                "timestamp": 34.59,
                "direction": "Straight"
            },
            {
                "timestamp": 34.63,
                "direction": "Straight"
            },
            {
                "timestamp": 34.66,
                "direction": "Straight"
            },
            {
                "timestamp": 34.69,
                "direction": "Straight"
            },
            {
                "timestamp": 34.73,
                "direction": "Slight Left"
            },
            {
                "timestamp": 34.76,
                "direction": "Slight Left"
            },
            {
                "timestamp": 34.79,
                "direction": "Slight Left"
            },
            {
                "timestamp": 34.83,
                "direction": "Slight Left"
            },
            {
                "timestamp": 34.86,
                "direction": "Slight Left"
            },
            {
                "timestamp": 34.89,
                "direction": "Slight Left"
            },
            {
                "timestamp": 34.93,
                "direction": "Slight Left"
            },
            {
                "timestamp": 34.96,
                "direction": "Slight Left"
            },
            {
                "timestamp": 34.99,
                "direction": "Slight Left"
            },
            {
                "timestamp": 35.03,
                "direction": "Slight Left"
            },
            {
                "timestamp": 35.06,
                "direction": "Slight Left"
            },
            {
                "timestamp": 35.09,
                "direction": "Slight Left"
            },
            {
                "timestamp": 35.13,
                "direction": "Slight Left"
            },
            {
                "timestamp": 35.16,
                "direction": "Slight Left"
            },
            {
                "timestamp": 35.19,
                "direction": "Straight"
            },
            {
                "timestamp": 35.23,
                "direction": "Straight"
            },
            {
                "timestamp": 35.26,
                "direction": "Straight"
            },
            {
                "timestamp": 35.29,
                "direction": "Straight"
            },
            {
                "timestamp": 35.33,
                "direction": "Straight"
            },
            {
                "timestamp": 35.36,
                "direction": "Straight"
            },
            {
                "timestamp": 35.39,
                "direction": "Straight"
            },
            {
                "timestamp": 35.43,
                "direction": "Straight"
            },
            {
                "timestamp": 35.46,
                "direction": "Straight"
            },
            {
                "timestamp": 35.49,
                "direction": "Straight"
            },
            {
                "timestamp": 35.53,
                "direction": "Straight"
            },
            {
                "timestamp": 35.56,
                "direction": "Straight"
            },
            {
                "timestamp": 35.59,
                "direction": "Straight"
            },
            {
                "timestamp": 35.63,
                "direction": "Straight"
            },
            {
                "timestamp": 35.66,
                "direction": "Straight"
            },
            {
                "timestamp": 35.69,
                "direction": "Straight"
            },
            {
                "timestamp": 35.73,
                "direction": "Straight"
            },
            {
                "timestamp": 35.76,
                "direction": "Straight"
            },
            {
                "timestamp": 35.79,
                "direction": "Straight"
            },
            {
                "timestamp": 35.83,
                "direction": "Straight"
            },
            {
                "timestamp": 35.86,
                "direction": "Straight"
            },
            {
                "timestamp": 35.89,
                "direction": "Straight"
            },
            {
                "timestamp": 35.93,
                "direction": "Straight"
            },
            {
                "timestamp": 35.96,
                "direction": "Slight Left"
            },
            {
                "timestamp": 35.99,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.03,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.06,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.09,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.13,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.16,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.19,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.23,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.26,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.29,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.33,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.36,
                "direction": "Slight Left"
            },
            {
                "timestamp": 36.39,
                "direction": "Straight"
            },
            {
                "timestamp": 36.43,
                "direction": "Straight"
            },
            {
                "timestamp": 36.46,
                "direction": "Straight"
            },
            {
                "timestamp": 36.49,
                "direction": "Straight"
            },
            {
                "timestamp": 36.53,
                "direction": "Straight"
            },
            {
                "timestamp": 36.56,
                "direction": "Straight"
            },
            {
                "timestamp": 36.59,
                "direction": "Straight"
            },
            {
                "timestamp": 36.63,
                "direction": "Straight"
            },
            {
                "timestamp": 36.66,
                "direction": "Straight"
            },
            {
                "timestamp": 36.69,
                "direction": "Straight"
            },
            {
                "timestamp": 36.73,
                "direction": "Straight"
            },
            {
                "timestamp": 36.76,
                "direction": "Straight"
            },
            {
                "timestamp": 36.79,
                "direction": "Straight"
            },
            {
                "timestamp": 36.83,
                "direction": "Straight"
            },
            {
                "timestamp": 36.86,
                "direction": "Straight"
            },
            {
                "timestamp": 36.89,
                "direction": "Straight"
            },
            {
                "timestamp": 36.93,
                "direction": "Straight"
            },
            {
                "timestamp": 36.96,
                "direction": "Straight"
            },
            {
                "timestamp": 36.99,
                "direction": "Straight"
            },
            {
                "timestamp": 37.03,
                "direction": "Straight"
            },
            {
                "timestamp": 37.06,
                "direction": "Straight"
            },
            {
                "timestamp": 37.09,
                "direction": "Straight"
            },
            {
                "timestamp": 37.13,
                "direction": "Slight Left"
            },
            {
                "timestamp": 37.16,
                "direction": "Slight Left"
            },
            {
                "timestamp": 37.19,
                "direction": "Slight Left"
            },
            {
                "timestamp": 37.23,
                "direction": "Slight Left"
            },
            {
                "timestamp": 37.26,
                "direction": "Slight Left"
            },
            {
                "timestamp": 37.29,
                "direction": "Slight Left"
            },
            {
                "timestamp": 37.33,
                "direction": "Slight Left"
            },
            {
                "timestamp": 37.36,
                "direction": "Left"
            },
            {
                "timestamp": 37.39,
                "direction": "Left"
            },
            {
                "timestamp": 37.43,
                "direction": "Left"
            },
            {
                "timestamp": 37.46,
                "direction": "Left"
            },
            {
                "timestamp": 37.49,
                "direction": "Left"
            },
            {
                "timestamp": 37.53,
                "direction": "Left"
            },
            {
                "timestamp": 37.56,
                "direction": "Left"
            },
            {
                "timestamp": 37.59,
                "direction": "Slight Left"
            },
            {
                "timestamp": 37.63,
                "direction": "Slight Left"
            },
            {
                "timestamp": 37.66,
                "direction": "Slight Left"
            },
            {
                "timestamp": 37.7,
                "direction": "Straight"
            },
            {
                "timestamp": 37.73,
                "direction": "Straight"
            },
            {
                "timestamp": 37.76,
                "direction": "Straight"
            },
            {
                "timestamp": 37.8,
                "direction": "Straight"
            },
            {
                "timestamp": 37.83,
                "direction": "Straight"
            },
            {
                "timestamp": 37.86,
                "direction": "Straight"
            },
            {
                "timestamp": 37.9,
                "direction": "Straight"
            },
            {
                "timestamp": 37.93,
                "direction": "Straight"
            },
            {
                "timestamp": 37.96,
                "direction": "Straight"
            },
            {
                "timestamp": 38.0,
                "direction": "Straight"
            },
            {
                "timestamp": 38.03,
                "direction": "Straight"
            },
            {
                "timestamp": 38.06,
                "direction": "Slight Right"
            },
            {
                "timestamp": 38.1,
                "direction": "Slight Right"
            },
            {
                "timestamp": 38.13,
                "direction": "Slight Right"
            },
            {
                "timestamp": 38.16,
                "direction": "Straight"
            },
            {
                "timestamp": 38.2,
                "direction": "Straight"
            },
            {
                "timestamp": 38.23,
                "direction": "Straight"
            },
            {
                "timestamp": 38.26,
                "direction": "Straight"
            },
            {
                "timestamp": 38.3,
                "direction": "Straight"
            },
            {
                "timestamp": 38.33,
                "direction": "Straight"
            },
            {
                "timestamp": 38.36,
                "direction": "Straight"
            },
            {
                "timestamp": 38.4,
                "direction": "Straight"
            },
            {
                "timestamp": 38.43,
                "direction": "Straight"
            },
            {
                "timestamp": 38.46,
                "direction": "Straight"
            },
            {
                "timestamp": 38.5,
                "direction": "Straight"
            },
            {
                "timestamp": 38.53,
                "direction": "Straight"
            },
            {
                "timestamp": 38.56,
                "direction": "Straight"
            },
            {
                "timestamp": 38.6,
                "direction": "Straight"
            },
            {
                "timestamp": 38.63,
                "direction": "Straight"
            },
            {
                "timestamp": 38.66,
                "direction": "Straight"
            },
            {
                "timestamp": 38.7,
                "direction": "Straight"
            },
            {
                "timestamp": 38.73,
                "direction": "Straight"
            },
            {
                "timestamp": 38.76,
                "direction": "Straight"
            },
            {
                "timestamp": 38.8,
                "direction": "Straight"
            },
            {
                "timestamp": 38.83,
                "direction": "Straight"
            },
            {
                "timestamp": 38.86,
                "direction": "Straight"
            },
            {
                "timestamp": 38.9,
                "direction": "Straight"
            },
            {
                "timestamp": 38.93,
                "direction": "Straight"
            },
            {
                "timestamp": 38.96,
                "direction": "Straight"
            },
            {
                "timestamp": 39.0,
                "direction": "Straight"
            },
            {
                "timestamp": 39.03,
                "direction": "Straight"
            },
            {
                "timestamp": 39.06,
                "direction": "Straight"
            },
            {
                "timestamp": 39.1,
                "direction": "Straight"
            },
            {
                "timestamp": 39.13,
                "direction": "Slight Right"
            },
            {
                "timestamp": 39.16,
                "direction": "Slight Right"
            },
            {
                "timestamp": 39.2,
                "direction": "Slight Right"
            },
            {
                "timestamp": 39.23,
                "direction": "Slight Right"
            },
            {
                "timestamp": 39.26,
                "direction": "Right"
            },
            {
                "timestamp": 39.3,
                "direction": "Right"
            },
            {
                "timestamp": 39.33,
                "direction": "Right"
            },
            {
                "timestamp": 39.36,
                "direction": "Right"
            },
            {
                "timestamp": 39.4,
                "direction": "Slight Right"
            },
            {
                "timestamp": 39.43,
                "direction": "Slight Right"
            },
            {
                "timestamp": 39.46,
                "direction": "Slight Right"
            },
            {
                "timestamp": 39.5,
                "direction": "Straight"
            },
            {
                "timestamp": 39.53,
                "direction": "Straight"
            },
            {
                "timestamp": 39.56,
                "direction": "Straight"
            },
            {
                "timestamp": 39.6,
                "direction": "Straight"
            },
            {
                "timestamp": 39.63,
                "direction": "Straight"
            },
            {
                "timestamp": 39.66,
                "direction": "Straight"
            },
            {
                "timestamp": 39.7,
                "direction": "Straight"
            },
            {
                "timestamp": 39.73,
                "direction": "Straight"
            },
            {
                "timestamp": 39.76,
                "direction": "Straight"
            },
            {
                "timestamp": 39.8,
                "direction": "Straight"
            },
            {
                "timestamp": 39.83,
                "direction": "Straight"
            },
            {
                "timestamp": 39.86,
                "direction": "Straight"
            },
            {
                "timestamp": 39.9,
                "direction": "Straight"
            },
            {
                "timestamp": 39.93,
                "direction": "Straight"
            },
            {
                "timestamp": 39.96,
                "direction": "Straight"
            },
            {
                "timestamp": 40.0,
                "direction": "Straight"
            },
            {
                "timestamp": 40.03,
                "direction": "Straight"
            },
            {
                "timestamp": 40.06,
                "direction": "Straight"
            },
            {
                "timestamp": 40.1,
                "direction": "Straight"
            },
            {
                "timestamp": 40.13,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.16,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.2,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.23,
                "direction": "Straight"
            },
            {
                "timestamp": 40.26,
                "direction": "Straight"
            },
            {
                "timestamp": 40.3,
                "direction": "Straight"
            },
            {
                "timestamp": 40.33,
                "direction": "Straight"
            },
            {
                "timestamp": 40.36,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.4,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.43,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.46,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.5,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.53,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.56,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.6,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.63,
                "direction": "Slight Right"
            },
            {
                "timestamp": 40.66,
                "direction": "Straight"
            },
            {
                "timestamp": 40.7,
                "direction": "Straight"
            },
            {
                "timestamp": 40.73,
                "direction": "Straight"
            },
            {
                "timestamp": 40.76,
                "direction": "Straight"
            },
            {
                "timestamp": 40.8,
                "direction": "Straight"
            },
            {
                "timestamp": 40.83,
                "direction": "Straight"
            },
            {
                "timestamp": 40.86,
                "direction": "Straight"
            },
            {
                "timestamp": 40.9,
                "direction": "Straight"
            },
            {
                "timestamp": 40.93,
                "direction": "Straight"
            },
            {
                "timestamp": 40.96,
                "direction": "Straight"
            },
            {
                "timestamp": 41.0,
                "direction": "Slight Left"
            },
            {
                "timestamp": 41.03,
                "direction": "Slight Left"
            },
            {
                "timestamp": 41.06,
                "direction": "Slight Left"
            },
            {
                "timestamp": 41.1,
                "direction": "Slight Left"
            },
            {
                "timestamp": 41.13,
                "direction": "Slight Left"
            },
            {
                "timestamp": 41.16,
                "direction": "Slight Left"
            },
            {
                "timestamp": 41.2,
                "direction": "Slight Left"
            },
            {
                "timestamp": 41.23,
                "direction": "Straight"
            },
            {
                "timestamp": 41.26,
                "direction": "Straight"
            },
            {
                "timestamp": 41.3,
                "direction": "Straight"
            },
            {
                "timestamp": 41.33,
                "direction": "Straight"
            },
            {
                "timestamp": 41.36,
                "direction": "Straight"
            },
            {
                "timestamp": 41.4,
                "direction": "Straight"
            },
            {
                "timestamp": 41.43,
                "direction": "Straight"
            },
            {
                "timestamp": 41.46,
                "direction": "Straight"
            },
            {
                "timestamp": 41.5,
                "direction": "Straight"
            },
            {
                "timestamp": 41.53,
                "direction": "Straight"
            },
            {
                "timestamp": 41.56,
                "direction": "Straight"
            },
            {
                "timestamp": 41.6,
                "direction": "Straight"
            },
            {
                "timestamp": 41.63,
                "direction": "Straight"
            },
            {
                "timestamp": 41.66,
                "direction": "Straight"
            },
            {
                "timestamp": 41.7,
                "direction": "Straight"
            },
            {
                "timestamp": 41.73,
                "direction": "Straight"
            },
            {
                "timestamp": 41.76,
                "direction": "Straight"
            },
            {
                "timestamp": 41.8,
                "direction": "Straight"
            },
            {
                "timestamp": 41.83,
                "direction": "Straight"
            },
            {
                "timestamp": 41.86,
                "direction": "Straight"
            },
            {
                "timestamp": 41.9,
                "direction": "Straight"
            },
            {
                "timestamp": 41.93,
                "direction": "Straight"
            },
            {
                "timestamp": 41.96,
                "direction": "Straight"
            },
            {
                "timestamp": 42.0,
                "direction": "Straight"
            },
            {
                "timestamp": 42.03,
                "direction": "Straight"
            },
            {
                "timestamp": 42.06,
                "direction": "Straight"
            },
            {
                "timestamp": 42.1,
                "direction": "Straight"
            },
            {
                "timestamp": 42.13,
                "direction": "Straight"
            },
            {
                "timestamp": 42.17,
                "direction": "Straight"
            },
            {
                "timestamp": 42.2,
                "direction": "Straight"
            },
            {
                "timestamp": 42.23,
                "direction": "Straight"
            },
            {
                "timestamp": 42.27,
                "direction": "Straight"
            },
            {
                "timestamp": 42.3,
                "direction": "Straight"
            },
            {
                "timestamp": 42.33,
                "direction": "Straight"
            },
            {
                "timestamp": 42.37,
                "direction": "Straight"
            },
            {
                "timestamp": 42.4,
                "direction": "Straight"
            },
            {
                "timestamp": 42.43,
                "direction": "Straight"
            },
            {
                "timestamp": 42.47,
                "direction": "Straight"
            },
            {
                "timestamp": 42.5,
                "direction": "Straight"
            },
            {
                "timestamp": 42.53,
                "direction": "Straight"
            },
            {
                "timestamp": 42.57,
                "direction": "Straight"
            },
            {
                "timestamp": 42.6,
                "direction": "Straight"
            },
            {
                "timestamp": 42.63,
                "direction": "Straight"
            },
            {
                "timestamp": 42.67,
                "direction": "Straight"
            },
            {
                "timestamp": 42.7,
                "direction": "Straight"
            },
            {
                "timestamp": 42.73,
                "direction": "Straight"
            },
            {
                "timestamp": 42.77,
                "direction": "Straight"
            },
            {
                "timestamp": 42.8,
                "direction": "Straight"
            },
            {
                "timestamp": 42.83,
                "direction": "Straight"
            },
            {
                "timestamp": 42.87,
                "direction": "Straight"
            },
            {
                "timestamp": 42.9,
                "direction": "Straight"
            },
            {
                "timestamp": 42.93,
                "direction": "Straight"
            },
            {
                "timestamp": 42.97,
                "direction": "Straight"
            },
            {
                "timestamp": 43.0,
                "direction": "Straight"
            },
            {
                "timestamp": 43.03,
                "direction": "Straight"
            },
            {
                "timestamp": 43.07,
                "direction": "Straight"
            },
            {
                "timestamp": 43.1,
                "direction": "Straight"
            },
            {
                "timestamp": 43.13,
                "direction": "Straight"
            },
            {
                "timestamp": 43.17,
                "direction": "Straight"
            },
            {
                "timestamp": 43.2,
                "direction": "Straight"
            },
            {
                "timestamp": 43.23,
                "direction": "Straight"
            },
            {
                "timestamp": 43.27,
                "direction": "Straight"
            },
            {
                "timestamp": 43.3,
                "direction": "Straight"
            },
            {
                "timestamp": 43.33,
                "direction": "Straight"
            },
            {
                "timestamp": 43.37,
                "direction": "Straight"
            },
            {
                "timestamp": 43.4,
                "direction": "Straight"
            },
            {
                "timestamp": 43.43,
                "direction": "Straight"
            },
            {
                "timestamp": 43.47,
                "direction": "Straight"
            },
            {
                "timestamp": 43.5,
                "direction": "Straight"
            },
            {
                "timestamp": 43.53,
                "direction": "Straight"
            },
            {
                "timestamp": 43.57,
                "direction": "Straight"
            },
            {
                "timestamp": 43.6,
                "direction": "Straight"
            },
            {
                "timestamp": 43.63,
                "direction": "Straight"
            },
            {
                "timestamp": 43.67,
                "direction": "Straight"
            },
            {
                "timestamp": 43.7,
                "direction": "Straight"
            },
            {
                "timestamp": 43.73,
                "direction": "Straight"
            },
            {
                "timestamp": 43.77,
                "direction": "Straight"
            },
            {
                "timestamp": 43.8,
                "direction": "Straight"
            },
            {
                "timestamp": 43.83,
                "direction": "Straight"
            },
            {
                "timestamp": 43.87,
                "direction": "Straight"
            },
            {
                "timestamp": 43.9,
                "direction": "Straight"
            },
            {
                "timestamp": 43.93,
                "direction": "Straight"
            },
            {
                "timestamp": 43.97,
                "direction": "Straight"
            },
            {
                "timestamp": 44.0,
                "direction": "Straight"
            },
            {
                "timestamp": 44.03,
                "direction": "Straight"
            },
            {
                "timestamp": 44.07,
                "direction": "Straight"
            },
            {
                "timestamp": 44.1,
                "direction": "Straight"
            },
            {
                "timestamp": 44.13,
                "direction": "Slight Right"
            },
            {
                "timestamp": 44.17,
                "direction": "Slight Right"
            },
            {
                "timestamp": 44.2,
                "direction": "Slight Right"
            },
            {
                "timestamp": 44.23,
                "direction": "Slight Right"
            },
            {
                "timestamp": 44.27,
                "direction": "Slight Right"
            },
            {
                "timestamp": 44.3,
                "direction": "Slight Right"
            },
            {
                "timestamp": 44.33,
                "direction": "Straight"
            },
            {
                "timestamp": 44.37,
                "direction": "Straight"
            },
            {
                "timestamp": 44.4,
                "direction": "Straight"
            },
            {
                "timestamp": 44.43,
                "direction": "Straight"
            },
            {
                "timestamp": 44.47,
                "direction": "Straight"
            },
            {
                "timestamp": 44.5,
                "direction": "Straight"
            },
            {
                "timestamp": 44.53,
                "direction": "Straight"
            },
            {
                "timestamp": 44.57,
                "direction": "Straight"
            },
            {
                "timestamp": 44.6,
                "direction": "Straight"
            },
            {
                "timestamp": 44.63,
                "direction": "Slight Left"
            },
            {
                "timestamp": 44.67,
                "direction": "Slight Left"
            },
            {
                "timestamp": 44.7,
                "direction": "Slight Left"
            },
            {
                "timestamp": 44.73,
                "direction": "Slight Left"
            },
            {
                "timestamp": 44.77,
                "direction": "Slight Left"
            },
            {
                "timestamp": 44.8,
                "direction": "Slight Left"
            },
            {
                "timestamp": 44.83,
                "direction": "Slight Left"
            },
            {
                "timestamp": 44.87,
                "direction": "Slight Left"
            },
            {
                "timestamp": 44.9,
                "direction": "Slight Left"
            },
            {
                "timestamp": 44.93,
                "direction": "Slight Left"
            },
            {
                "timestamp": 44.97,
                "direction": "Slight Left"
            },
            {
                "timestamp": 45.0,
                "direction": "Straight"
            },
            {
                "timestamp": 45.03,
                "direction": "Straight"
            },
            {
                "timestamp": 45.07,
                "direction": "Straight"
            },
            {
                "timestamp": 45.1,
                "direction": "Straight"
            },
            {
                "timestamp": 45.13,
                "direction": "Straight"
            },
            {
                "timestamp": 45.17,
                "direction": "Straight"
            },
            {
                "timestamp": 45.2,
                "direction": "Straight"
            },
            {
                "timestamp": 45.23,
                "direction": "Straight"
            },
            {
                "timestamp": 45.27,
                "direction": "Straight"
            },
            {
                "timestamp": 45.3,
                "direction": "Straight"
            },
            {
                "timestamp": 45.33,
                "direction": "Straight"
            },
            {
                "timestamp": 45.37,
                "direction": "Straight"
            },
            {
                "timestamp": 45.4,
                "direction": "Straight"
            },
            {
                "timestamp": 45.43,
                "direction": "Straight"
            },
            {
                "timestamp": 45.47,
                "direction": "Straight"
            },
            {
                "timestamp": 45.5,
                "direction": "Straight"
            },
            {
                "timestamp": 45.53,
                "direction": "Straight"
            },
            {
                "timestamp": 45.57,
                "direction": "Straight"
            },
            {
                "timestamp": 45.6,
                "direction": "Straight"
            },
            {
                "timestamp": 45.63,
                "direction": "Straight"
            },
            {
                "timestamp": 45.67,
                "direction": "Straight"
            },
            {
                "timestamp": 45.7,
                "direction": "Straight"
            },
            {
                "timestamp": 45.73,
                "direction": "Straight"
            },
            {
                "timestamp": 45.77,
                "direction": "Slight Left"
            },
            {
                "timestamp": 45.8,
                "direction": "Slight Left"
            },
            {
                "timestamp": 45.83,
                "direction": "Slight Left"
            },
            {
                "timestamp": 45.87,
                "direction": "Slight Left"
            },
            {
                "timestamp": 45.9,
                "direction": "Slight Left"
            },
            {
                "timestamp": 45.93,
                "direction": "Slight Left"
            },
            {
                "timestamp": 45.97,
                "direction": "Left"
            },
            {
                "timestamp": 46.0,
                "direction": "Left"
            },
            {
                "timestamp": 46.03,
                "direction": "Slight Left"
            },
            {
                "timestamp": 46.07,
                "direction": "Slight Left"
            },
            {
                "timestamp": 46.1,
                "direction": "Slight Left"
            },
            {
                "timestamp": 46.13,
                "direction": "Slight Left"
            },
            {
                "timestamp": 46.17,
                "direction": "Slight Left"
            },
            {
                "timestamp": 46.2,
                "direction": "Straight"
            },
            {
                "timestamp": 46.23,
                "direction": "Straight"
            },
            {
                "timestamp": 46.27,
                "direction": "Straight"
            },
            {
                "timestamp": 46.3,
                "direction": "Straight"
            },
            {
                "timestamp": 46.33,
                "direction": "Straight"
            },
            {
                "timestamp": 46.37,
                "direction": "Straight"
            },
            {
                "timestamp": 46.4,
                "direction": "Straight"
            },
            {
                "timestamp": 46.43,
                "direction": "Straight"
            },
            {
                "timestamp": 46.47,
                "direction": "Straight"
            },
            {
                "timestamp": 46.5,
                "direction": "Straight"
            },
            {
                "timestamp": 46.54,
                "direction": "Straight"
            },
            {
                "timestamp": 46.57,
                "direction": "Straight"
            },
            {
                "timestamp": 46.6,
                "direction": "Straight"
            },
            {
                "timestamp": 46.64,
                "direction": "Straight"
            },
            {
                "timestamp": 46.67,
                "direction": "Straight"
            },
            {
                "timestamp": 46.7,
                "direction": "Straight"
            },
            {
                "timestamp": 46.74,
                "direction": "Straight"
            },
            {
                "timestamp": 46.77,
                "direction": "Straight"
            },
            {
                "timestamp": 46.8,
                "direction": "Straight"
            },
            {
                "timestamp": 46.84,
                "direction": "Straight"
            },
            {
                "timestamp": 46.87,
                "direction": "Straight"
            },
            {
                "timestamp": 46.9,
                "direction": "Straight"
            },
            {
                "timestamp": 46.94,
                "direction": "Straight"
            },
            {
                "timestamp": 46.97,
                "direction": "Straight"
            },
            {
                "timestamp": 47.0,
                "direction": "Straight"
            },
            {
                "timestamp": 47.04,
                "direction": "Straight"
            },
            {
                "timestamp": 47.07,
                "direction": "Straight"
            },
            {
                "timestamp": 47.1,
                "direction": "Straight"
            },
            {
                "timestamp": 47.14,
                "direction": "Straight"
            },
            {
                "timestamp": 47.17,
                "direction": "Straight"
            },
            {
                "timestamp": 47.2,
                "direction": "Straight"
            },
            {
                "timestamp": 47.24,
                "direction": "Straight"
            },
            {
                "timestamp": 47.27,
                "direction": "Straight"
            },
            {
                "timestamp": 47.3,
                "direction": "Straight"
            },
            {
                "timestamp": 47.34,
                "direction": "Straight"
            },
            {
                "timestamp": 47.37,
                "direction": "Straight"
            },
            {
                "timestamp": 47.4,
                "direction": "Straight"
            },
            {
                "timestamp": 47.44,
                "direction": "Straight"
            },
            {
                "timestamp": 47.47,
                "direction": "Straight"
            },
            {
                "timestamp": 47.5,
                "direction": "Straight"
            },
            {
                "timestamp": 47.54,
                "direction": "Straight"
            },
            {
                "timestamp": 47.57,
                "direction": "Straight"
            },
            {
                "timestamp": 47.6,
                "direction": "Straight"
            },
            {
                "timestamp": 47.64,
                "direction": "Straight"
            },
            {
                "timestamp": 47.67,
                "direction": "Straight"
            },
            {
                "timestamp": 47.7,
                "direction": "Straight"
            },
            {
                "timestamp": 47.74,
                "direction": "Straight"
            },
            {
                "timestamp": 47.77,
                "direction": "Straight"
            },
            {
                "timestamp": 47.8,
                "direction": "Straight"
            },
            {
                "timestamp": 47.84,
                "direction": "Straight"
            },
            {
                "timestamp": 47.87,
                "direction": "Straight"
            },
            {
                "timestamp": 47.9,
                "direction": "Straight"
            },
            {
                "timestamp": 47.94,
                "direction": "Straight"
            },
            {
                "timestamp": 47.97,
                "direction": "Straight"
            },
            {
                "timestamp": 48.0,
                "direction": "Straight"
            },
            {
                "timestamp": 48.04,
                "direction": "Straight"
            },
            {
                "timestamp": 48.07,
                "direction": "Straight"
            },
            {
                "timestamp": 48.1,
                "direction": "Straight"
            },
            {
                "timestamp": 48.14,
                "direction": "Straight"
            },
            {
                "timestamp": 48.17,
                "direction": "Straight"
            },
            {
                "timestamp": 48.2,
                "direction": "Straight"
            },
            {
                "timestamp": 48.24,
                "direction": "Straight"
            },
            {
                "timestamp": 48.27,
                "direction": "Straight"
            },
            {
                "timestamp": 48.3,
                "direction": "Straight"
            },
            {
                "timestamp": 48.34,
                "direction": "Straight"
            },
            {
                "timestamp": 48.37,
                "direction": "Straight"
            },
            {
                "timestamp": 48.4,
                "direction": "Straight"
            },
            {
                "timestamp": 48.44,
                "direction": "Straight"
            },
            {
                "timestamp": 48.47,
                "direction": "Straight"
            },
            {
                "timestamp": 48.5,
                "direction": "Straight"
            },
            {
                "timestamp": 48.54,
                "direction": "Straight"
            },
            {
                "timestamp": 48.57,
                "direction": "Straight"
            },
            {
                "timestamp": 48.6,
                "direction": "Straight"
            },
            {
                "timestamp": 48.64,
                "direction": "Straight"
            },
            {
                "timestamp": 48.67,
                "direction": "Straight"
            },
            {
                "timestamp": 48.7,
                "direction": "Straight"
            },
            {
                "timestamp": 48.74,
                "direction": "Straight"
            },
            {
                "timestamp": 48.77,
                "direction": "Straight"
            },
            {
                "timestamp": 48.8,
                "direction": "Straight"
            },
            {
                "timestamp": 48.84,
                "direction": "Straight"
            },
            {
                "timestamp": 48.87,
                "direction": "Straight"
            },
            {
                "timestamp": 48.9,
                "direction": "Straight"
            },
            {
                "timestamp": 48.94,
                "direction": "Straight"
            },
            {
                "timestamp": 48.97,
                "direction": "Straight"
            },
            {
                "timestamp": 49.0,
                "direction": "Straight"
            },
            {
                "timestamp": 49.04,
                "direction": "Straight"
            },
            {
                "timestamp": 49.07,
                "direction": "Straight"
            },
            {
                "timestamp": 49.1,
                "direction": "Straight"
            },
            {
                "timestamp": 49.14,
                "direction": "Straight"
            },
            {
                "timestamp": 49.17,
                "direction": "Straight"
            },
            {
                "timestamp": 49.2,
                "direction": "Straight"
            },
            {
                "timestamp": 49.24,
                "direction": "Straight"
            },
            {
                "timestamp": 49.27,
                "direction": "Straight"
            },
            {
                "timestamp": 49.3,
                "direction": "Straight"
            },
            {
                "timestamp": 49.34,
                "direction": "Straight"
            },
            {
                "timestamp": 49.37,
                "direction": "Straight"
            },
            {
                "timestamp": 49.4,
                "direction": "Straight"
            },
            {
                "timestamp": 49.44,
                "direction": "Straight"
            },
            {
                "timestamp": 49.47,
                "direction": "Straight"
            },
            {
                "timestamp": 49.5,
                "direction": "Straight"
            },
            {
                "timestamp": 49.54,
                "direction": "Straight"
            },
            {
                "timestamp": 49.57,
                "direction": "Straight"
            },
            {
                "timestamp": 49.6,
                "direction": "Straight"
            },
            {
                "timestamp": 49.64,
                "direction": "Straight"
            },
            {
                "timestamp": 49.67,
                "direction": "Straight"
            },
            {
                "timestamp": 49.7,
                "direction": "Straight"
            },
            {
                "timestamp": 49.74,
                "direction": "Straight"
            },
            {
                "timestamp": 49.77,
                "direction": "Straight"
            },
            {
                "timestamp": 49.8,
                "direction": "Straight"
            },
            {
                "timestamp": 49.84,
                "direction": "Straight"
            },
            {
                "timestamp": 49.87,
                "direction": "Straight"
            },
            {
                "timestamp": 49.9,
                "direction": "Straight"
            },
            {
                "timestamp": 49.94,
                "direction": "Straight"
            },
            {
                "timestamp": 49.97,
                "direction": "Straight"
            },
            {
                "timestamp": 50.0,
                "direction": "Straight"
            },
            {
                "timestamp": 50.04,
                "direction": "Straight"
            },
            {
                "timestamp": 50.07,
                "direction": "Straight"
            },
            {
                "timestamp": 50.1,
                "direction": "Straight"
            },
            {
                "timestamp": 50.14,
                "direction": "Straight"
            },
            {
                "timestamp": 50.17,
                "direction": "Slight Right"
            },
            {
                "timestamp": 50.2,
                "direction": "Slight Right"
            },
            {
                "timestamp": 50.24,
                "direction": "Slight Right"
            },
            {
                "timestamp": 50.27,
                "direction": "Slight Right"
            },
            {
                "timestamp": 50.3,
                "direction": "Straight"
            },
            {
                "timestamp": 50.34,
                "direction": "Straight"
            },
            {
                "timestamp": 50.37,
                "direction": "Straight"
            },
            {
                "timestamp": 50.4,
                "direction": "Straight"
            },
            {
                "timestamp": 50.44,
                "direction": "Straight"
            },
            {
                "timestamp": 50.47,
                "direction": "Straight"
            },
            {
                "timestamp": 50.5,
                "direction": "Straight"
            },
            {
                "timestamp": 50.54,
                "direction": "Straight"
            },
            {
                "timestamp": 50.57,
                "direction": "Straight"
            },
            {
                "timestamp": 50.6,
                "direction": "Straight"
            },
            {
                "timestamp": 50.64,
                "direction": "Straight"
            },
            {
                "timestamp": 50.67,
                "direction": "Straight"
            },
            {
                "timestamp": 50.7,
                "direction": "Straight"
            },
            {
                "timestamp": 50.74,
                "direction": "Straight"
            },
            {
                "timestamp": 50.77,
                "direction": "Straight"
            },
            {
                "timestamp": 50.8,
                "direction": "Straight"
            },
            {
                "timestamp": 50.84,
                "direction": "Straight"
            },
            {
                "timestamp": 50.87,
                "direction": "Straight"
            },
            {
                "timestamp": 50.9,
                "direction": "Straight"
            },
            {
                "timestamp": 50.94,
                "direction": "Straight"
            },
            {
                "timestamp": 50.97,
                "direction": "Straight"
            },
            {
                "timestamp": 51.01,
                "direction": "Straight"
            },
            {
                "timestamp": 51.04,
                "direction": "Straight"
            },
            {
                "timestamp": 51.07,
                "direction": "Straight"
            },
            {
                "timestamp": 51.11,
                "direction": "Straight"
            },
            {
                "timestamp": 51.14,
                "direction": "Straight"
            },
            {
                "timestamp": 51.17,
                "direction": "Straight"
            },
            {
                "timestamp": 51.21,
                "direction": "Straight"
            },
            {
                "timestamp": 51.24,
                "direction": "Straight"
            },
            {
                "timestamp": 51.27,
                "direction": "Straight"
            },
            {
                "timestamp": 51.31,
                "direction": "Straight"
            },
            {
                "timestamp": 51.34,
                "direction": "Straight"
            },
            {
                "timestamp": 51.37,
                "direction": "Straight"
            },
            {
                "timestamp": 51.41,
                "direction": "Straight"
            },
            {
                "timestamp": 51.44,
                "direction": "Straight"
            },
            {
                "timestamp": 51.47,
                "direction": "Straight"
            },
            {
                "timestamp": 51.51,
                "direction": "Straight"
            },
            {
                "timestamp": 51.54,
                "direction": "Straight"
            },
            {
                "timestamp": 51.57,
                "direction": "Straight"
            },
            {
                "timestamp": 51.61,
                "direction": "Straight"
            },
            {
                "timestamp": 51.64,
                "direction": "Straight"
            },
            {
                "timestamp": 51.67,
                "direction": "Straight"
            },
            {
                "timestamp": 51.71,
                "direction": "Straight"
            },
            {
                "timestamp": 51.74,
                "direction": "Straight"
            },
            {
                "timestamp": 51.77,
                "direction": "Straight"
            },
            {
                "timestamp": 51.81,
                "direction": "Straight"
            },
            {
                "timestamp": 51.84,
                "direction": "Straight"
            },
            {
                "timestamp": 51.87,
                "direction": "Straight"
            },
            {
                "timestamp": 51.91,
                "direction": "Straight"
            },
            {
                "timestamp": 51.94,
                "direction": "Straight"
            },
            {
                "timestamp": 51.97,
                "direction": "Straight"
            },
            {
                "timestamp": 52.01,
                "direction": "Straight"
            },
            {
                "timestamp": 52.04,
                "direction": "Straight"
            },
            {
                "timestamp": 52.07,
                "direction": "Straight"
            },
            {
                "timestamp": 52.11,
                "direction": "Straight"
            },
            {
                "timestamp": 52.14,
                "direction": "Straight"
            },
            {
                "timestamp": 52.17,
                "direction": "Straight"
            },
            {
                "timestamp": 52.21,
                "direction": "Straight"
            },
            {
                "timestamp": 52.24,
                "direction": "Straight"
            },
            {
                "timestamp": 52.27,
                "direction": "Straight"
            },
            {
                "timestamp": 52.31,
                "direction": "Straight"
            },
            {
                "timestamp": 52.34,
                "direction": "Straight"
            },
            {
                "timestamp": 52.37,
                "direction": "Straight"
            },
            {
                "timestamp": 52.41,
                "direction": "Straight"
            },
            {
                "timestamp": 52.44,
                "direction": "Straight"
            },
            {
                "timestamp": 52.47,
                "direction": "Straight"
            },
            {
                "timestamp": 52.51,
                "direction": "Straight"
            },
            {
                "timestamp": 52.54,
                "direction": "Straight"
            },
            {
                "timestamp": 52.57,
                "direction": "Straight"
            },
            {
                "timestamp": 52.61,
                "direction": "Straight"
            },
            {
                "timestamp": 52.64,
                "direction": "Straight"
            },
            {
                "timestamp": 52.67,
                "direction": "Straight"
            },
            {
                "timestamp": 52.71,
                "direction": "Straight"
            },
            {
                "timestamp": 52.74,
                "direction": "Straight"
            },
            {
                "timestamp": 52.77,
                "direction": "Straight"
            },
            {
                "timestamp": 52.81,
                "direction": "Straight"
            },
            {
                "timestamp": 52.84,
                "direction": "Straight"
            },
            {
                "timestamp": 52.87,
                "direction": "Straight"
            },
            {
                "timestamp": 52.91,
                "direction": "Straight"
            },
            {
                "timestamp": 52.94,
                "direction": "Straight"
            },
            {
                "timestamp": 52.97,
                "direction": "Straight"
            },
            {
                "timestamp": 53.01,
                "direction": "Straight"
            },
            {
                "timestamp": 53.04,
                "direction": "Straight"
            },
            {
                "timestamp": 53.07,
                "direction": "Straight"
            },
            {
                "timestamp": 53.11,
                "direction": "Slight Left"
            },
            {
                "timestamp": 53.14,
                "direction": "Slight Left"
            },
            {
                "timestamp": 53.17,
                "direction": "Slight Left"
            },
            {
                "timestamp": 53.21,
                "direction": "Slight Left"
            },
            {
                "timestamp": 53.24,
                "direction": "Slight Left"
            },
            {
                "timestamp": 53.27,
                "direction": "Straight"
            },
            {
                "timestamp": 53.31,
                "direction": "Straight"
            },
            {
                "timestamp": 53.34,
                "direction": "Straight"
            },
            {
                "timestamp": 53.37,
                "direction": "Straight"
            },
            {
                "timestamp": 53.41,
                "direction": "Straight"
            },
            {
                "timestamp": 53.44,
                "direction": "Straight"
            },
            {
                "timestamp": 53.47,
                "direction": "Straight"
            },
            {
                "timestamp": 53.51,
                "direction": "Straight"
            },
            {
                "timestamp": 53.54,
                "direction": "Straight"
            },
            {
                "timestamp": 53.57,
                "direction": "Straight"
            },
            {
                "timestamp": 53.61,
                "direction": "Straight"
            },
            {
                "timestamp": 53.64,
                "direction": "Straight"
            },
            {
                "timestamp": 53.67,
                "direction": "Straight"
            },
            {
                "timestamp": 53.71,
                "direction": "Straight"
            },
            {
                "timestamp": 53.74,
                "direction": "Straight"
            },
            {
                "timestamp": 53.77,
                "direction": "Straight"
            },
            {
                "timestamp": 53.81,
                "direction": "Straight"
            },
            {
                "timestamp": 53.84,
                "direction": "Straight"
            },
            {
                "timestamp": 53.87,
                "direction": "Straight"
            },
            {
                "timestamp": 53.91,
                "direction": "Straight"
            },
            {
                "timestamp": 53.94,
                "direction": "Straight"
            },
            {
                "timestamp": 53.97,
                "direction": "Straight"
            },
            {
                "timestamp": 54.01,
                "direction": "Straight"
            },
            {
                "timestamp": 54.04,
                "direction": "Straight"
            },
            {
                "timestamp": 54.07,
                "direction": "Straight"
            },
            {
                "timestamp": 54.11,
                "direction": "Straight"
            },
            {
                "timestamp": 54.14,
                "direction": "Straight"
            },
            {
                "timestamp": 54.17,
                "direction": "Straight"
            },
            {
                "timestamp": 54.21,
                "direction": "Straight"
            },
            {
                "timestamp": 54.24,
                "direction": "Straight"
            },
            {
                "timestamp": 54.27,
                "direction": "Straight"
            },
            {
                "timestamp": 54.31,
                "direction": "Straight"
            },
            {
                "timestamp": 54.34,
                "direction": "Straight"
            },
            {
                "timestamp": 54.37,
                "direction": "Straight"
            },
            {
                "timestamp": 54.41,
                "direction": "Straight"
            },
            {
                "timestamp": 54.44,
                "direction": "Straight"
            },
            {
                "timestamp": 54.47,
                "direction": "Straight"
            },
            {
                "timestamp": 54.51,
                "direction": "Straight"
            },
            {
                "timestamp": 54.54,
                "direction": "Straight"
            },
            {
                "timestamp": 54.57,
                "direction": "Straight"
            },
            {
                "timestamp": 54.61,
                "direction": "Straight"
            },
            {
                "timestamp": 54.64,
                "direction": "Straight"
            },
            {
                "timestamp": 54.67,
                "direction": "Straight"
            },
            {
                "timestamp": 54.71,
                "direction": "Straight"
            },
            {
                "timestamp": 54.74,
                "direction": "Straight"
            },
            {
                "timestamp": 54.77,
                "direction": "Straight"
            },
            {
                "timestamp": 54.81,
                "direction": "Straight"
            },
            {
                "timestamp": 54.84,
                "direction": "Straight"
            },
            {
                "timestamp": 54.87,
                "direction": "Straight"
            },
            {
                "timestamp": 54.91,
                "direction": "Straight"
            },
            {
                "timestamp": 54.94,
                "direction": "Slight Right"
            },
            {
                "timestamp": 54.97,
                "direction": "Slight Right"
            },
            {
                "timestamp": 55.01,
                "direction": "Slight Right"
            },
            {
                "timestamp": 55.04,
                "direction": "Slight Right"
            },
            {
                "timestamp": 55.07,
                "direction": "Slight Right"
            },
            {
                "timestamp": 55.11,
                "direction": "Straight"
            },
            {
                "timestamp": 55.14,
                "direction": "Straight"
            },
            {
                "timestamp": 55.17,
                "direction": "Straight"
            },
            {
                "timestamp": 55.21,
                "direction": "Straight"
            },
            {
                "timestamp": 55.24,
                "direction": "Straight"
            },
            {
                "timestamp": 55.27,
                "direction": "Straight"
            },
            {
                "timestamp": 55.31,
                "direction": "Straight"
            },
            {
                "timestamp": 55.34,
                "direction": "Straight"
            },
            {
                "timestamp": 55.37,
                "direction": "Straight"
            },
            {
                "timestamp": 55.41,
                "direction": "Straight"
            },
            {
                "timestamp": 55.44,
                "direction": "Straight"
            },
            {
                "timestamp": 55.48,
                "direction": "Straight"
            },
            {
                "timestamp": 55.51,
                "direction": "Straight"
            },
            {
                "timestamp": 55.54,
                "direction": "Straight"
            },
            {
                "timestamp": 55.58,
                "direction": "Straight"
            },
            {
                "timestamp": 55.61,
                "direction": "Straight"
            },
            {
                "timestamp": 55.64,
                "direction": "Straight"
            },
            {
                "timestamp": 55.68,
                "direction": "Straight"
            },
            {
                "timestamp": 55.71,
                "direction": "Straight"
            },
            {
                "timestamp": 55.74,
                "direction": "Straight"
            },
            {
                "timestamp": 55.78,
                "direction": "Straight"
            },
            {
                "timestamp": 55.81,
                "direction": "Straight"
            },
            {
                "timestamp": 55.84,
                "direction": "Straight"
            },
            {
                "timestamp": 55.88,
                "direction": "Straight"
            },
            {
                "timestamp": 55.91,
                "direction": "Straight"
            },
            {
                "timestamp": 55.94,
                "direction": "Straight"
            },
            {
                "timestamp": 55.98,
                "direction": "Straight"
            },
            {
                "timestamp": 56.01,
                "direction": "Straight"
            },
            {
                "timestamp": 56.04,
                "direction": "Straight"
            },
            {
                "timestamp": 56.08,
                "direction": "Straight"
            },
            {
                "timestamp": 56.11,
                "direction": "Straight"
            },
            {
                "timestamp": 56.14,
                "direction": "Straight"
            },
            {
                "timestamp": 56.18,
                "direction": "Straight"
            },
            {
                "timestamp": 56.21,
                "direction": "Straight"
            },
            {
                "timestamp": 56.24,
                "direction": "Straight"
            },
            {
                "timestamp": 56.28,
                "direction": "Straight"
            },
            {
                "timestamp": 56.31,
                "direction": "Straight"
            },
            {
                "timestamp": 56.34,
                "direction": "Straight"
            },
            {
                "timestamp": 56.38,
                "direction": "Straight"
            },
            {
                "timestamp": 56.41,
                "direction": "Straight"
            },
            {
                "timestamp": 56.44,
                "direction": "Straight"
            },
            {
                "timestamp": 56.48,
                "direction": "Straight"
            },
            {
                "timestamp": 56.51,
                "direction": "Straight"
            },
            {
                "timestamp": 56.54,
                "direction": "Straight"
            },
            {
                "timestamp": 56.58,
                "direction": "Straight"
            },
            {
                "timestamp": 56.61,
                "direction": "Straight"
            },
            {
                "timestamp": 56.64,
                "direction": "Straight"
            },
            {
                "timestamp": 56.68,
                "direction": "Straight"
            },
            {
                "timestamp": 56.71,
                "direction": "Straight"
            },
            {
                "timestamp": 56.74,
                "direction": "Slight Left"
            },
            {
                "timestamp": 56.78,
                "direction": "Slight Left"
            },
            {
                "timestamp": 56.81,
                "direction": "Slight Left"
            },
            {
                "timestamp": 56.84,
                "direction": "Slight Left"
            },
            {
                "timestamp": 56.88,
                "direction": "Slight Left"
            },
            {
                "timestamp": 56.91,
                "direction": "Slight Left"
            },
            {
                "timestamp": 56.94,
                "direction": "Straight"
            },
            {
                "timestamp": 56.98,
                "direction": "Straight"
            },
            {
                "timestamp": 57.01,
                "direction": "Straight"
            },
            {
                "timestamp": 57.04,
                "direction": "Straight"
            },
            {
                "timestamp": 57.08,
                "direction": "Straight"
            },
            {
                "timestamp": 57.11,
                "direction": "Straight"
            },
            {
                "timestamp": 57.14,
                "direction": "Straight"
            },
            {
                "timestamp": 57.18,
                "direction": "Straight"
            },
            {
                "timestamp": 57.21,
                "direction": "Straight"
            },
            {
                "timestamp": 57.24,
                "direction": "Straight"
            },
            {
                "timestamp": 57.28,
                "direction": "Straight"
            },
            {
                "timestamp": 57.31,
                "direction": "Straight"
            },
            {
                "timestamp": 57.34,
                "direction": "Straight"
            },
            {
                "timestamp": 57.38,
                "direction": "Straight"
            },
            {
                "timestamp": 57.41,
                "direction": "Straight"
            },
            {
                "timestamp": 57.44,
                "direction": "Straight"
            },
            {
                "timestamp": 57.48,
                "direction": "Straight"
            },
            {
                "timestamp": 57.51,
                "direction": "Straight"
            },
            {
                "timestamp": 57.54,
                "direction": "Straight"
            },
            {
                "timestamp": 57.58,
                "direction": "Straight"
            },
            {
                "timestamp": 57.61,
                "direction": "Straight"
            },
            {
                "timestamp": 57.64,
                "direction": "Straight"
            },
            {
                "timestamp": 57.68,
                "direction": "Straight"
            },
            {
                "timestamp": 57.71,
                "direction": "Straight"
            },
            {
                "timestamp": 57.74,
                "direction": "Straight"
            },
            {
                "timestamp": 57.78,
                "direction": "Straight"
            },
            {
                "timestamp": 57.81,
                "direction": "Straight"
            },
            {
                "timestamp": 57.84,
                "direction": "Straight"
            },
            {
                "timestamp": 57.88,
                "direction": "Straight"
            },
            {
                "timestamp": 57.91,
                "direction": "Straight"
            },
            {
                "timestamp": 57.94,
                "direction": "Straight"
            },
            {
                "timestamp": 57.98,
                "direction": "Straight"
            },
            {
                "timestamp": 58.01,
                "direction": "Straight"
            },
            {
                "timestamp": 58.04,
                "direction": "Slight Left"
            },
            {
                "timestamp": 58.08,
                "direction": "Straight"
            },
            {
                "timestamp": 58.11,
                "direction": "Straight"
            },
            {
                "timestamp": 58.14,
                "direction": "Straight"
            },
            {
                "timestamp": 58.18,
                "direction": "Straight"
            },
            {
                "timestamp": 58.21,
                "direction": "Straight"
            },
            {
                "timestamp": 58.24,
                "direction": "Straight"
            },
            {
                "timestamp": 58.28,
                "direction": "Straight"
            },
            {
                "timestamp": 58.31,
                "direction": "Straight"
            },
            {
                "timestamp": 58.34,
                "direction": "Straight"
            },
            {
                "timestamp": 58.38,
                "direction": "Straight"
            },
            {
                "timestamp": 58.41,
                "direction": "Straight"
            },
            {
                "timestamp": 58.44,
                "direction": "Straight"
            },
            {
                "timestamp": 58.48,
                "direction": "Straight"
            },
            {
                "timestamp": 58.51,
                "direction": "Straight"
            },
            {
                "timestamp": 58.54,
                "direction": "Straight"
            },
            {
                "timestamp": 58.58,
                "direction": "Straight"
            },
            {
                "timestamp": 58.61,
                "direction": "Straight"
            },
            {
                "timestamp": 58.64,
                "direction": "Straight"
            },
            {
                "timestamp": 58.68,
                "direction": "Straight"
            },
            {
                "timestamp": 58.71,
                "direction": "Straight"
            },
            {
                "timestamp": 58.74,
                "direction": "Straight"
            },
            {
                "timestamp": 58.78,
                "direction": "Straight"
            },
            {
                "timestamp": 58.81,
                "direction": "Straight"
            },
            {
                "timestamp": 58.84,
                "direction": "Straight"
            },
            {
                "timestamp": 58.88,
                "direction": "Straight"
            },
            {
                "timestamp": 58.91,
                "direction": "Straight"
            },
            {
                "timestamp": 58.94,
                "direction": "Straight"
            },
            {
                "timestamp": 58.98,
                "direction": "Straight"
            },
            {
                "timestamp": 59.01,
                "direction": "Straight"
            },
            {
                "timestamp": 59.04,
                "direction": "Straight"
            },
            {
                "timestamp": 59.08,
                "direction": "Straight"
            },
            {
                "timestamp": 59.11,
                "direction": "Straight"
            },
            {
                "timestamp": 59.14,
                "direction": "Slight Left"
            },
            {
                "timestamp": 59.18,
                "direction": "Slight Left"
            },
            {
                "timestamp": 59.21,
                "direction": "Slight Left"
            },
            {
                "timestamp": 59.24,
                "direction": "Slight Left"
            },
            {
                "timestamp": 59.28,
                "direction": "Slight Left"
            },
            {
                "timestamp": 59.31,
                "direction": "Straight"
            },
            {
                "timestamp": 59.34,
                "direction": "Straight"
            },
            {
                "timestamp": 59.38,
                "direction": "Straight"
            },
            {
                "timestamp": 59.41,
                "direction": "Straight"
            },
            {
                "timestamp": 59.44,
                "direction": "Straight"
            },
            {
                "timestamp": 59.48,
                "direction": "Straight"
            },
            {
                "timestamp": 59.51,
                "direction": "Straight"
            },
            {
                "timestamp": 59.54,
                "direction": "Straight"
            },
            {
                "timestamp": 59.58,
                "direction": "Straight"
            },
            {
                "timestamp": 59.61,
                "direction": "Straight"
            },
            {
                "timestamp": 59.64,
                "direction": "Straight"
            },
            {
                "timestamp": 59.68,
                "direction": "Straight"
            },
            {
                "timestamp": 59.71,
                "direction": "Straight"
            },
            {
                "timestamp": 59.74,
                "direction": "Straight"
            },
            {
                "timestamp": 59.78,
                "direction": "Straight"
            },
            {
                "timestamp": 59.81,
                "direction": "Straight"
            },
            {
                "timestamp": 59.85,
                "direction": "Straight"
            },
            {
                "timestamp": 59.88,
                "direction": "Straight"
            },
            {
                "timestamp": 59.91,
                "direction": "Straight"
            },
            {
                "timestamp": 59.95,
                "direction": "Straight"
            },
            {
                "timestamp": 59.98,
                "direction": "Straight"
            },
            {
                "timestamp": 60.01,
                "direction": "Straight"
            },
            {
                "timestamp": 60.05,
                "direction": "Straight"
            },
            {
                "timestamp": 60.08,
                "direction": "Straight"
            },
            {
                "timestamp": 60.11,
                "direction": "Straight"
            },
            {
                "timestamp": 60.15,
                "direction": "Straight"
            },
            {
                "timestamp": 60.18,
                "direction": "Straight"
            },
            {
                "timestamp": 60.21,
                "direction": "Straight"
            },
            {
                "timestamp": 60.25,
                "direction": "Straight"
            },
            {
                "timestamp": 60.28,
                "direction": "Straight"
            },
            {
                "timestamp": 60.31,
                "direction": "Straight"
            },
            {
                "timestamp": 60.35,
                "direction": "Straight"
            },
            {
                "timestamp": 60.38,
                "direction": "Straight"
            },
            {
                "timestamp": 60.41,
                "direction": "Straight"
            },
            {
                "timestamp": 60.45,
                "direction": "Straight"
            },
            {
                "timestamp": 60.48,
                "direction": "Straight"
            },
            {
                "timestamp": 60.51,
                "direction": "Straight"
            },
            {
                "timestamp": 60.55,
                "direction": "Straight"
            },
            {
                "timestamp": 60.58,
                "direction": "Straight"
            },
            {
                "timestamp": 60.61,
                "direction": "Straight"
            },
            {
                "timestamp": 60.65,
                "direction": "Straight"
            },
            {
                "timestamp": 60.68,
                "direction": "Straight"
            },
            {
                "timestamp": 60.71,
                "direction": "Straight"
            },
            {
                "timestamp": 60.75,
                "direction": "Straight"
            },
            {
                "timestamp": 60.78,
                "direction": "Straight"
            },
            {
                "timestamp": 60.81,
                "direction": "Straight"
            },
            {
                "timestamp": 60.85,
                "direction": "Straight"
            },
            {
                "timestamp": 60.88,
                "direction": "Straight"
            },
            {
                "timestamp": 60.91,
                "direction": "Straight"
            },
            {
                "timestamp": 60.95,
                "direction": "Straight"
            },
            {
                "timestamp": 60.98,
                "direction": "Straight"
            },
            {
                "timestamp": 61.01,
                "direction": "Straight"
            },
            {
                "timestamp": 61.05,
                "direction": "Straight"
            },
            {
                "timestamp": 61.08,
                "direction": "Straight"
            },
            {
                "timestamp": 61.11,
                "direction": "Straight"
            },
            {
                "timestamp": 61.15,
                "direction": "Straight"
            },
            {
                "timestamp": 61.18,
                "direction": "Straight"
            },
            {
                "timestamp": 61.21,
                "direction": "Straight"
            },
            {
                "timestamp": 61.25,
                "direction": "Straight"
            },
            {
                "timestamp": 61.28,
                "direction": "Straight"
            },
            {
                "timestamp": 61.31,
                "direction": "Straight"
            },
            {
                "timestamp": 61.35,
                "direction": "Straight"
            },
            {
                "timestamp": 61.38,
                "direction": "Straight"
            },
            {
                "timestamp": 61.41,
                "direction": "Straight"
            },
            {
                "timestamp": 61.45,
                "direction": "Straight"
            },
            {
                "timestamp": 61.48,
                "direction": "Straight"
            },
            {
                "timestamp": 61.51,
                "direction": "Straight"
            },
            {
                "timestamp": 61.55,
                "direction": "Straight"
            },
            {
                "timestamp": 61.58,
                "direction": "Straight"
            },
            {
                "timestamp": 61.61,
                "direction": "Straight"
            },
            {
                "timestamp": 61.65,
                "direction": "Straight"
            },
            {
                "timestamp": 61.68,
                "direction": "Straight"
            },
            {
                "timestamp": 61.71,
                "direction": "Straight"
            },
            {
                "timestamp": 61.75,
                "direction": "Straight"
            },
            {
                "timestamp": 61.78,
                "direction": "Straight"
            },
            {
                "timestamp": 61.81,
                "direction": "Straight"
            },
            {
                "timestamp": 61.85,
                "direction": "Straight"
            },
            {
                "timestamp": 61.88,
                "direction": "Straight"
            },
            {
                "timestamp": 61.91,
                "direction": "Straight"
            },
            {
                "timestamp": 61.95,
                "direction": "Straight"
            },
            {
                "timestamp": 61.98,
                "direction": "Straight"
            },
            {
                "timestamp": 62.01,
                "direction": "Straight"
            },
            {
                "timestamp": 62.05,
                "direction": "Straight"
            },
            {
                "timestamp": 62.08,
                "direction": "Straight"
            },
            {
                "timestamp": 62.11,
                "direction": "Straight"
            },
            {
                "timestamp": 62.15,
                "direction": "Straight"
            },
            {
                "timestamp": 62.18,
                "direction": "Straight"
            },
            {
                "timestamp": 62.21,
                "direction": "Straight"
            },
            {
                "timestamp": 62.25,
                "direction": "Straight"
            },
            {
                "timestamp": 62.28,
                "direction": "Slight Right"
            },
            {
                "timestamp": 62.31,
                "direction": "Straight"
            },
            {
                "timestamp": 62.35,
                "direction": "Straight"
            },
            {
                "timestamp": 62.38,
                "direction": "Straight"
            },
            {
                "timestamp": 62.41,
                "direction": "Straight"
            },
            {
                "timestamp": 62.45,
                "direction": "Straight"
            },
            {
                "timestamp": 62.48,
                "direction": "Straight"
            },
            {
                "timestamp": 62.51,
                "direction": "Straight"
            },
            {
                "timestamp": 62.55,
                "direction": "Straight"
            },
            {
                "timestamp": 62.58,
                "direction": "Straight"
            },
            {
                "timestamp": 62.61,
                "direction": "Straight"
            },
            {
                "timestamp": 62.65,
                "direction": "Straight"
            },
            {
                "timestamp": 62.68,
                "direction": "Straight"
            },
            {
                "timestamp": 62.71,
                "direction": "Straight"
            },
            {
                "timestamp": 62.75,
                "direction": "Slight Left"
            },
            {
                "timestamp": 62.78,
                "direction": "Slight Left"
            },
            {
                "timestamp": 62.81,
                "direction": "Slight Left"
            },
            {
                "timestamp": 62.85,
                "direction": "Slight Left"
            },
            {
                "timestamp": 62.88,
                "direction": "Slight Left"
            },
            {
                "timestamp": 62.91,
                "direction": "Slight Left"
            },
            {
                "timestamp": 62.95,
                "direction": "Straight"
            },
            {
                "timestamp": 62.98,
                "direction": "Straight"
            },
            {
                "timestamp": 63.01,
                "direction": "Straight"
            },
            {
                "timestamp": 63.05,
                "direction": "Straight"
            },
            {
                "timestamp": 63.08,
                "direction": "Straight"
            },
            {
                "timestamp": 63.11,
                "direction": "Straight"
            },
            {
                "timestamp": 63.15,
                "direction": "Straight"
            },
            {
                "timestamp": 63.18,
                "direction": "Straight"
            },
            {
                "timestamp": 63.21,
                "direction": "Straight"
            },
            {
                "timestamp": 63.25,
                "direction": "Straight"
            },
            {
                "timestamp": 63.28,
                "direction": "Straight"
            },
            {
                "timestamp": 63.31,
                "direction": "Straight"
            },
            {
                "timestamp": 63.35,
                "direction": "Straight"
            },
            {
                "timestamp": 63.38,
                "direction": "Straight"
            },
            {
                "timestamp": 63.41,
                "direction": "Straight"
            },
            {
                "timestamp": 63.45,
                "direction": "Straight"
            },
            {
                "timestamp": 63.48,
                "direction": "Straight"
            },
            {
                "timestamp": 63.51,
                "direction": "Straight"
            },
            {
                "timestamp": 63.55,
                "direction": "Straight"
            },
            {
                "timestamp": 63.58,
                "direction": "Straight"
            },
            {
                "timestamp": 63.61,
                "direction": "Straight"
            },
            {
                "timestamp": 63.65,
                "direction": "Straight"
            },
            {
                "timestamp": 63.68,
                "direction": "Straight"
            },
            {
                "timestamp": 63.71,
                "direction": "Straight"
            },
            {
                "timestamp": 63.75,
                "direction": "Straight"
            },
            {
                "timestamp": 63.78,
                "direction": "Straight"
            },
            {
                "timestamp": 63.81,
                "direction": "Straight"
            },
            {
                "timestamp": 63.85,
                "direction": "Straight"
            },
            {
                "timestamp": 63.88,
                "direction": "Straight"
            },
            {
                "timestamp": 63.91,
                "direction": "Straight"
            },
            {
                "timestamp": 63.95,
                "direction": "Straight"
            },
            {
                "timestamp": 63.98,
                "direction": "Straight"
            },
            {
                "timestamp": 64.01,
                "direction": "Straight"
            },
            {
                "timestamp": 64.05,
                "direction": "Straight"
            },
            {
                "timestamp": 64.08,
                "direction": "Straight"
            },
            {
                "timestamp": 64.11,
                "direction": "Straight"
            },
            {
                "timestamp": 64.15,
                "direction": "Straight"
            },
            {
                "timestamp": 64.18,
                "direction": "Straight"
            },
            {
                "timestamp": 64.21,
                "direction": "Straight"
            },
            {
                "timestamp": 64.25,
                "direction": "Straight"
            },
            {
                "timestamp": 64.28,
                "direction": "Straight"
            },
            {
                "timestamp": 64.32,
                "direction": "Straight"
            },
            {
                "timestamp": 64.35,
                "direction": "Straight"
            },
            {
                "timestamp": 64.38,
                "direction": "Straight"
            },
            {
                "timestamp": 64.42,
                "direction": "Straight"
            },
            {
                "timestamp": 64.45,
                "direction": "Straight"
            },
            {
                "timestamp": 64.48,
                "direction": "Straight"
            },
            {
                "timestamp": 64.52,
                "direction": "Straight"
            },
            {
                "timestamp": 64.55,
                "direction": "Straight"
            },
            {
                "timestamp": 64.58,
                "direction": "Straight"
            },
            {
                "timestamp": 64.62,
                "direction": "Slight Right"
            },
            {
                "timestamp": 64.65,
                "direction": "Slight Right"
            },
            {
                "timestamp": 64.68,
                "direction": "Slight Right"
            },
            {
                "timestamp": 64.72,
                "direction": "Straight"
            },
            {
                "timestamp": 64.75,
                "direction": "Straight"
            },
            {
                "timestamp": 64.78,
                "direction": "Straight"
            },
            {
                "timestamp": 64.82,
                "direction": "Straight"
            },
            {
                "timestamp": 64.85,
                "direction": "Straight"
            },
            {
                "timestamp": 64.88,
                "direction": "Straight"
            },
            {
                "timestamp": 64.92,
                "direction": "Straight"
            },
            {
                "timestamp": 64.95,
                "direction": "Straight"
            },
            {
                "timestamp": 64.98,
                "direction": "Straight"
            },
            {
                "timestamp": 65.02,
                "direction": "Straight"
            },
            {
                "timestamp": 65.05,
                "direction": "Straight"
            },
            {
                "timestamp": 65.08,
                "direction": "Straight"
            },
            {
                "timestamp": 65.12,
                "direction": "Straight"
            },
            {
                "timestamp": 65.15,
                "direction": "Straight"
            },
            {
                "timestamp": 65.18,
                "direction": "Straight"
            },
            {
                "timestamp": 65.22,
                "direction": "Straight"
            },
            {
                "timestamp": 65.25,
                "direction": "Straight"
            },
            {
                "timestamp": 65.28,
                "direction": "Straight"
            },
            {
                "timestamp": 65.32,
                "direction": "Straight"
            },
            {
                "timestamp": 65.35,
                "direction": "Straight"
            },
            {
                "timestamp": 65.38,
                "direction": "Straight"
            },
            {
                "timestamp": 65.42,
                "direction": "Straight"
            },
            {
                "timestamp": 65.45,
                "direction": "Straight"
            },
            {
                "timestamp": 65.48,
                "direction": "Straight"
            },
            {
                "timestamp": 65.52,
                "direction": "Straight"
            },
            {
                "timestamp": 65.55,
                "direction": "Straight"
            },
            {
                "timestamp": 65.58,
                "direction": "Straight"
            },
            {
                "timestamp": 65.62,
                "direction": "Straight"
            },
            {
                "timestamp": 65.65,
                "direction": "Straight"
            },
            {
                "timestamp": 65.68,
                "direction": "Straight"
            },
            {
                "timestamp": 65.72,
                "direction": "Straight"
            },
            {
                "timestamp": 65.75,
                "direction": "Straight"
            },
            {
                "timestamp": 65.78,
                "direction": "Straight"
            },
            {
                "timestamp": 65.82,
                "direction": "Straight"
            },
            {
                "timestamp": 65.85,
                "direction": "Straight"
            },
            {
                "timestamp": 65.88,
                "direction": "Straight"
            },
            {
                "timestamp": 65.92,
                "direction": "Straight"
            },
            {
                "timestamp": 65.95,
                "direction": "Straight"
            },
            {
                "timestamp": 65.98,
                "direction": "Straight"
            },
            {
                "timestamp": 66.02,
                "direction": "Straight"
            },
            {
                "timestamp": 66.05,
                "direction": "Straight"
            },
            {
                "timestamp": 66.08,
                "direction": "Straight"
            },
            {
                "timestamp": 66.12,
                "direction": "Straight"
            },
            {
                "timestamp": 66.15,
                "direction": "Straight"
            },
            {
                "timestamp": 66.18,
                "direction": "Straight"
            },
            {
                "timestamp": 66.22,
                "direction": "Straight"
            },
            {
                "timestamp": 66.25,
                "direction": "Straight"
            },
            {
                "timestamp": 66.28,
                "direction": "Straight"
            },
            {
                "timestamp": 66.32,
                "direction": "Straight"
            },
            {
                "timestamp": 66.35,
                "direction": "Straight"
            },
            {
                "timestamp": 66.38,
                "direction": "Straight"
            },
            {
                "timestamp": 66.42,
                "direction": "Straight"
            },
            {
                "timestamp": 66.45,
                "direction": "Straight"
            },
            {
                "timestamp": 66.48,
                "direction": "Straight"
            },
            {
                "timestamp": 66.52,
                "direction": "Straight"
            },
            {
                "timestamp": 66.55,
                "direction": "Straight"
            },
            {
                "timestamp": 66.58,
                "direction": "Straight"
            },
            {
                "timestamp": 66.62,
                "direction": "Straight"
            },
            {
                "timestamp": 66.65,
                "direction": "Straight"
            },
            {
                "timestamp": 66.68,
                "direction": "Straight"
            },
            {
                "timestamp": 66.72,
                "direction": "Straight"
            },
            {
                "timestamp": 66.75,
                "direction": "Straight"
            },
            {
                "timestamp": 66.78,
                "direction": "Straight"
            },
            {
                "timestamp": 66.82,
                "direction": "Straight"
            },
            {
                "timestamp": 66.85,
                "direction": "Straight"
            },
            {
                "timestamp": 66.88,
                "direction": "Straight"
            },
            {
                "timestamp": 66.92,
                "direction": "Straight"
            },
            {
                "timestamp": 66.95,
                "direction": "Straight"
            },
            {
                "timestamp": 66.98,
                "direction": "Straight"
            },
            {
                "timestamp": 67.02,
                "direction": "Straight"
            },
            {
                "timestamp": 67.05,
                "direction": "Straight"
            },
            {
                "timestamp": 67.08,
                "direction": "Straight"
            },
            {
                "timestamp": 67.12,
                "direction": "Straight"
            },
            {
                "timestamp": 67.15,
                "direction": "Straight"
            },
            {
                "timestamp": 67.18,
                "direction": "Straight"
            },
            {
                "timestamp": 67.22,
                "direction": "Straight"
            },
            {
                "timestamp": 67.25,
                "direction": "Straight"
            },
            {
                "timestamp": 67.28,
                "direction": "Straight"
            },
            {
                "timestamp": 67.32,
                "direction": "Straight"
            },
            {
                "timestamp": 67.35,
                "direction": "Straight"
            },
            {
                "timestamp": 67.38,
                "direction": "Straight"
            },
            {
                "timestamp": 67.42,
                "direction": "Straight"
            },
            {
                "timestamp": 67.45,
                "direction": "Straight"
            },
            {
                "timestamp": 67.48,
                "direction": "Straight"
            },
            {
                "timestamp": 67.52,
                "direction": "Straight"
            },
            {
                "timestamp": 67.55,
                "direction": "Straight"
            },
            {
                "timestamp": 67.58,
                "direction": "Slight Left"
            },
            {
                "timestamp": 67.62,
                "direction": "Straight"
            },
            {
                "timestamp": 67.65,
                "direction": "Slight Left"
            },
            {
                "timestamp": 67.68,
                "direction": "Slight Left"
            },
            {
                "timestamp": 67.72,
                "direction": "Slight Left"
            },
            {
                "timestamp": 67.75,
                "direction": "Straight"
            },
            {
                "timestamp": 67.78,
                "direction": "Straight"
            },
            {
                "timestamp": 67.82,
                "direction": "Straight"
            },
            {
                "timestamp": 67.85,
                "direction": "Straight"
            },
            {
                "timestamp": 67.88,
                "direction": "Straight"
            },
            {
                "timestamp": 67.92,
                "direction": "Straight"
            },
            {
                "timestamp": 67.95,
                "direction": "Straight"
            },
            {
                "timestamp": 67.98,
                "direction": "Straight"
            },
            {
                "timestamp": 68.02,
                "direction": "Straight"
            },
            {
                "timestamp": 68.05,
                "direction": "Straight"
            },
            {
                "timestamp": 68.08,
                "direction": "Straight"
            },
            {
                "timestamp": 68.12,
                "direction": "Straight"
            },
            {
                "timestamp": 68.15,
                "direction": "Straight"
            },
            {
                "timestamp": 68.18,
                "direction": "Straight"
            },
            {
                "timestamp": 68.22,
                "direction": "Straight"
            },
            {
                "timestamp": 68.25,
                "direction": "Straight"
            },
            {
                "timestamp": 68.28,
                "direction": "Slight Right"
            },
            {
                "timestamp": 68.32,
                "direction": "Slight Right"
            },
            {
                "timestamp": 68.35,
                "direction": "Straight"
            },
            {
                "timestamp": 68.38,
                "direction": "Straight"
            },
            {
                "timestamp": 68.42,
                "direction": "Straight"
            },
            {
                "timestamp": 68.45,
                "direction": "Straight"
            },
            {
                "timestamp": 68.48,
                "direction": "Straight"
            },
            {
                "timestamp": 68.52,
                "direction": "Straight"
            },
            {
                "timestamp": 68.55,
                "direction": "Straight"
            },
            {
                "timestamp": 68.58,
                "direction": "Straight"
            },
            {
                "timestamp": 68.62,
                "direction": "Straight"
            },
            {
                "timestamp": 68.65,
                "direction": "Straight"
            },
            {
                "timestamp": 68.69,
                "direction": "Straight"
            },
            {
                "timestamp": 68.72,
                "direction": "Straight"
            },
            {
                "timestamp": 68.75,
                "direction": "Straight"
            },
            {
                "timestamp": 68.79,
                "direction": "Straight"
            },
            {
                "timestamp": 68.82,
                "direction": "Straight"
            },
            {
                "timestamp": 68.85,
                "direction": "Straight"
            },
            {
                "timestamp": 68.89,
                "direction": "Straight"
            },
            {
                "timestamp": 68.92,
                "direction": "Straight"
            },
            {
                "timestamp": 68.95,
                "direction": "Straight"
            },
            {
                "timestamp": 68.99,
                "direction": "Straight"
            },
            {
                "timestamp": 69.02,
                "direction": "Straight"
            },
            {
                "timestamp": 69.05,
                "direction": "Straight"
            },
            {
                "timestamp": 69.09,
                "direction": "Straight"
            },
            {
                "timestamp": 69.12,
                "direction": "Straight"
            },
            {
                "timestamp": 69.15,
                "direction": "Straight"
            },
            {
                "timestamp": 69.19,
                "direction": "Straight"
            },
            {
                "timestamp": 69.22,
                "direction": "Straight"
            },
            {
                "timestamp": 69.25,
                "direction": "Straight"
            },
            {
                "timestamp": 69.29,
                "direction": "Straight"
            },
            {
                "timestamp": 69.32,
                "direction": "Straight"
            },
            {
                "timestamp": 69.35,
                "direction": "Straight"
            },
            {
                "timestamp": 69.39,
                "direction": "Straight"
            },
            {
                "timestamp": 69.42,
                "direction": "Slight Right"
            },
            {
                "timestamp": 69.45,
                "direction": "Slight Right"
            },
            {
                "timestamp": 69.49,
                "direction": "Slight Right"
            },
            {
                "timestamp": 69.52,
                "direction": "Straight"
            },
            {
                "timestamp": 69.55,
                "direction": "Straight"
            },
            {
                "timestamp": 69.59,
                "direction": "Straight"
            },
            {
                "timestamp": 69.62,
                "direction": "Straight"
            },
            {
                "timestamp": 69.65,
                "direction": "Straight"
            },
            {
                "timestamp": 69.69,
                "direction": "Straight"
            },
            {
                "timestamp": 69.72,
                "direction": "Straight"
            },
            {
                "timestamp": 69.75,
                "direction": "Straight"
            },
            {
                "timestamp": 69.79,
                "direction": "Straight"
            },
            {
                "timestamp": 69.82,
                "direction": "Straight"
            },
            {
                "timestamp": 69.85,
                "direction": "Straight"
            },
            {
                "timestamp": 69.89,
                "direction": "Straight"
            },
            {
                "timestamp": 69.92,
                "direction": "Straight"
            },
            {
                "timestamp": 69.95,
                "direction": "Straight"
            },
            {
                "timestamp": 69.99,
                "direction": "Straight"
            },
            {
                "timestamp": 70.02,
                "direction": "Slight Left"
            },
            {
                "timestamp": 70.05,
                "direction": "Slight Left"
            },
            {
                "timestamp": 70.09,
                "direction": "Slight Left"
            },
            {
                "timestamp": 70.12,
                "direction": "Straight"
            },
            {
                "timestamp": 70.15,
                "direction": "Straight"
            },
            {
                "timestamp": 70.19,
                "direction": "Straight"
            },
            {
                "timestamp": 70.22,
                "direction": "Straight"
            },
            {
                "timestamp": 70.25,
                "direction": "Straight"
            },
            {
                "timestamp": 70.29,
                "direction": "Straight"
            },
            {
                "timestamp": 70.32,
                "direction": "Straight"
            },
            {
                "timestamp": 70.35,
                "direction": "Straight"
            },
            {
                "timestamp": 70.39,
                "direction": "Straight"
            },
            {
                "timestamp": 70.42,
                "direction": "Straight"
            },
            {
                "timestamp": 70.45,
                "direction": "Straight"
            },
            {
                "timestamp": 70.49,
                "direction": "Straight"
            },
            {
                "timestamp": 70.52,
                "direction": "Straight"
            },
            {
                "timestamp": 70.55,
                "direction": "Straight"
            },
            {
                "timestamp": 70.59,
                "direction": "Straight"
            },
            {
                "timestamp": 70.62,
                "direction": "Straight"
            },
            {
                "timestamp": 70.65,
                "direction": "Slight Right"
            },
            {
                "timestamp": 70.69,
                "direction": "Straight"
            },
            {
                "timestamp": 70.72,
                "direction": "Straight"
            },
            {
                "timestamp": 70.75,
                "direction": "Straight"
            },
            {
                "timestamp": 70.79,
                "direction": "Straight"
            },
            {
                "timestamp": 70.82,
                "direction": "Straight"
            },
            {
                "timestamp": 70.85,
                "direction": "Straight"
            },
            {
                "timestamp": 70.89,
                "direction": "Straight"
            },
            {
                "timestamp": 70.92,
                "direction": "Straight"
            },
            {
                "timestamp": 70.95,
                "direction": "Straight"
            },
            {
                "timestamp": 70.99,
                "direction": "Straight"
            },
            {
                "timestamp": 71.02,
                "direction": "Straight"
            },
            {
                "timestamp": 71.05,
                "direction": "Straight"
            },
            {
                "timestamp": 71.09,
                "direction": "Straight"
            },
            {
                "timestamp": 71.12,
                "direction": "Straight"
            },
            {
                "timestamp": 71.15,
                "direction": "Straight"
            },
            {
                "timestamp": 71.19,
                "direction": "Straight"
            },
            {
                "timestamp": 71.22,
                "direction": "Straight"
            },
            {
                "timestamp": 71.25,
                "direction": "Straight"
            },
            {
                "timestamp": 71.29,
                "direction": "Straight"
            },
            {
                "timestamp": 71.32,
                "direction": "Straight"
            },
            {
                "timestamp": 71.35,
                "direction": "Straight"
            },
            {
                "timestamp": 71.39,
                "direction": "Straight"
            },
            {
                "timestamp": 71.42,
                "direction": "Straight"
            },
            {
                "timestamp": 71.45,
                "direction": "Straight"
            },
            {
                "timestamp": 71.49,
                "direction": "Straight"
            },
            {
                "timestamp": 71.52,
                "direction": "Straight"
            },
            {
                "timestamp": 71.55,
                "direction": "Straight"
            },
            {
                "timestamp": 71.59,
                "direction": "Straight"
            },
            {
                "timestamp": 71.62,
                "direction": "Straight"
            },
            {
                "timestamp": 71.65,
                "direction": "Straight"
            },
            {
                "timestamp": 71.69,
                "direction": "Straight"
            },
            {
                "timestamp": 71.72,
                "direction": "Straight"
            },
            {
                "timestamp": 71.75,
                "direction": "Straight"
            },
            {
                "timestamp": 71.79,
                "direction": "Straight"
            },
            {
                "timestamp": 71.82,
                "direction": "Straight"
            },
            {
                "timestamp": 71.85,
                "direction": "Straight"
            },
            {
                "timestamp": 71.89,
                "direction": "Straight"
            },
            {
                "timestamp": 71.92,
                "direction": "Straight"
            },
            {
                "timestamp": 71.95,
                "direction": "Straight"
            },
            {
                "timestamp": 71.99,
                "direction": "Straight"
            },
            {
                "timestamp": 72.02,
                "direction": "Straight"
            },
            {
                "timestamp": 72.05,
                "direction": "Straight"
            },
            {
                "timestamp": 72.09,
                "direction": "Straight"
            },
            {
                "timestamp": 72.12,
                "direction": "Straight"
            },
            {
                "timestamp": 72.15,
                "direction": "Straight"
            },
            {
                "timestamp": 72.19,
                "direction": "Straight"
            },
            {
                "timestamp": 72.22,
                "direction": "Straight"
            },
            {
                "timestamp": 72.25,
                "direction": "Straight"
            },
            {
                "timestamp": 72.29,
                "direction": "Straight"
            },
            {
                "timestamp": 72.32,
                "direction": "Straight"
            },
            {
                "timestamp": 72.35,
                "direction": "Straight"
            },
            {
                "timestamp": 72.39,
                "direction": "Straight"
            },
            {
                "timestamp": 72.42,
                "direction": "Straight"
            },
            {
                "timestamp": 72.45,
                "direction": "Straight"
            },
            {
                "timestamp": 72.49,
                "direction": "Straight"
            },
            {
                "timestamp": 72.52,
                "direction": "Straight"
            },
            {
                "timestamp": 72.55,
                "direction": "Straight"
            },
            {
                "timestamp": 72.59,
                "direction": "Straight"
            },
            {
                "timestamp": 72.62,
                "direction": "Straight"
            },
            {
                "timestamp": 72.65,
                "direction": "Straight"
            },
            {
                "timestamp": 72.69,
                "direction": "Straight"
            },
            {
                "timestamp": 72.72,
                "direction": "Straight"
            },
            {
                "timestamp": 72.75,
                "direction": "Straight"
            },
            {
                "timestamp": 72.79,
                "direction": "Straight"
            },
            {
                "timestamp": 72.82,
                "direction": "Straight"
            },
            {
                "timestamp": 72.85,
                "direction": "Straight"
            },
            {
                "timestamp": 72.89,
                "direction": "Straight"
            },
            {
                "timestamp": 72.92,
                "direction": "Straight"
            },
            {
                "timestamp": 72.95,
                "direction": "Straight"
            },
            {
                "timestamp": 72.99,
                "direction": "Straight"
            },
            {
                "timestamp": 73.02,
                "direction": "Slight Right"
            },
            {
                "timestamp": 73.05,
                "direction": "Slight Right"
            },
            {
                "timestamp": 73.09,
                "direction": "Slight Right"
            },
            {
                "timestamp": 73.12,
                "direction": "Slight Right"
            },
            {
                "timestamp": 73.16,
                "direction": "Slight Right"
            },
            {
                "timestamp": 73.19,
                "direction": "Slight Right"
            },
            {
                "timestamp": 73.22,
                "direction": "Straight"
            },
            {
                "timestamp": 73.26,
                "direction": "Straight"
            },
            {
                "timestamp": 73.29,
                "direction": "Straight"
            },
            {
                "timestamp": 73.32,
                "direction": "Straight"
            },
            {
                "timestamp": 73.36,
                "direction": "Straight"
            },
            {
                "timestamp": 73.39,
                "direction": "Straight"
            },
            {
                "timestamp": 73.42,
                "direction": "Straight"
            },
            {
                "timestamp": 73.46,
                "direction": "Straight"
            },
            {
                "timestamp": 73.49,
                "direction": "Straight"
            },
            {
                "timestamp": 73.52,
                "direction": "Straight"
            },
            {
                "timestamp": 73.56,
                "direction": "Straight"
            },
            {
                "timestamp": 73.59,
                "direction": "Straight"
            },
            {
                "timestamp": 73.62,
                "direction": "Straight"
            },
            {
                "timestamp": 73.66,
                "direction": "Straight"
            },
            {
                "timestamp": 73.69,
                "direction": "Straight"
            },
            {
                "timestamp": 73.72,
                "direction": "Straight"
            },
            {
                "timestamp": 73.76,
                "direction": "Straight"
            },
            {
                "timestamp": 73.79,
                "direction": "Straight"
            },
            {
                "timestamp": 73.82,
                "direction": "Straight"
            },
            {
                "timestamp": 73.86,
                "direction": "Straight"
            },
            {
                "timestamp": 73.89,
                "direction": "Straight"
            },
            {
                "timestamp": 73.92,
                "direction": "Straight"
            },
            {
                "timestamp": 73.96,
                "direction": "Straight"
            },
            {
                "timestamp": 73.99,
                "direction": "Straight"
            },
            {
                "timestamp": 74.02,
                "direction": "Straight"
            },
            {
                "timestamp": 74.06,
                "direction": "Straight"
            },
            {
                "timestamp": 74.09,
                "direction": "Straight"
            },
            {
                "timestamp": 74.12,
                "direction": "Straight"
            },
            {
                "timestamp": 74.16,
                "direction": "Straight"
            },
            {
                "timestamp": 74.19,
                "direction": "Straight"
            },
            {
                "timestamp": 74.22,
                "direction": "Slight Right"
            },
            {
                "timestamp": 74.26,
                "direction": "Slight Right"
            },
            {
                "timestamp": 74.29,
                "direction": "Slight Right"
            },
            {
                "timestamp": 74.32,
                "direction": "Straight"
            },
            {
                "timestamp": 74.36,
                "direction": "Straight"
            },
            {
                "timestamp": 74.39,
                "direction": "Straight"
            },
            {
                "timestamp": 74.42,
                "direction": "Straight"
            },
            {
                "timestamp": 74.46,
                "direction": "Straight"
            },
            {
                "timestamp": 74.49,
                "direction": "Straight"
            },
            {
                "timestamp": 74.52,
                "direction": "Straight"
            },
            {
                "timestamp": 74.56,
                "direction": "Straight"
            },
            {
                "timestamp": 74.59,
                "direction": "Straight"
            },
            {
                "timestamp": 74.62,
                "direction": "Straight"
            },
            {
                "timestamp": 74.66,
                "direction": "Straight"
            },
            {
                "timestamp": 74.69,
                "direction": "Straight"
            },
            {
                "timestamp": 74.72,
                "direction": "Slight Left"
            },
            {
                "timestamp": 74.76,
                "direction": "Slight Left"
            },
            {
                "timestamp": 74.79,
                "direction": "Slight Left"
            },
            {
                "timestamp": 74.82,
                "direction": "Slight Left"
            },
            {
                "timestamp": 74.86,
                "direction": "Slight Left"
            },
            {
                "timestamp": 74.89,
                "direction": "Slight Left"
            },
            {
                "timestamp": 74.92,
                "direction": "Slight Left"
            },
            {
                "timestamp": 74.96,
                "direction": "Slight Left"
            },
            {
                "timestamp": 74.99,
                "direction": "Straight"
            },
            {
                "timestamp": 75.02,
                "direction": "Straight"
            },
            {
                "timestamp": 75.06,
                "direction": "Straight"
            },
            {
                "timestamp": 75.09,
                "direction": "Straight"
            },
            {
                "timestamp": 75.12,
                "direction": "Straight"
            },
            {
                "timestamp": 75.16,
                "direction": "Straight"
            },
            {
                "timestamp": 75.19,
                "direction": "Straight"
            },
            {
                "timestamp": 75.22,
                "direction": "Straight"
            },
            {
                "timestamp": 75.26,
                "direction": "Straight"
            },
            {
                "timestamp": 75.29,
                "direction": "Straight"
            },
            {
                "timestamp": 75.32,
                "direction": "Straight"
            },
            {
                "timestamp": 75.36,
                "direction": "Straight"
            },
            {
                "timestamp": 75.39,
                "direction": "Straight"
            },
            {
                "timestamp": 75.42,
                "direction": "Straight"
            },
            {
                "timestamp": 75.46,
                "direction": "Straight"
            },
            {
                "timestamp": 75.49,
                "direction": "Straight"
            },
            {
                "timestamp": 75.52,
                "direction": "Straight"
            },
            {
                "timestamp": 75.56,
                "direction": "Straight"
            },
            {
                "timestamp": 75.59,
                "direction": "Straight"
            },
            {
                "timestamp": 75.62,
                "direction": "Straight"
            },
            {
                "timestamp": 75.66,
                "direction": "Straight"
            },
            {
                "timestamp": 75.69,
                "direction": "Straight"
            },
            {
                "timestamp": 75.72,
                "direction": "Straight"
            },
            {
                "timestamp": 75.76,
                "direction": "Straight"
            },
            {
                "timestamp": 75.79,
                "direction": "Straight"
            },
            {
                "timestamp": 75.82,
                "direction": "Straight"
            },
            {
                "timestamp": 75.86,
                "direction": "Slight Left"
            },
            {
                "timestamp": 75.89,
                "direction": "Slight Left"
            },
            {
                "timestamp": 75.92,
                "direction": "Slight Left"
            },
            {
                "timestamp": 75.96,
                "direction": "Slight Left"
            },
            {
                "timestamp": 75.99,
                "direction": "Slight Left"
            },
            {
                "timestamp": 76.02,
                "direction": "Straight"
            },
            {
                "timestamp": 76.06,
                "direction": "Straight"
            },
            {
                "timestamp": 76.09,
                "direction": "Straight"
            },
            {
                "timestamp": 76.12,
                "direction": "Straight"
            },
            {
                "timestamp": 76.16,
                "direction": "Straight"
            },
            {
                "timestamp": 76.19,
                "direction": "Straight"
            },
            {
                "timestamp": 76.22,
                "direction": "Straight"
            },
            {
                "timestamp": 76.26,
                "direction": "Straight"
            },
            {
                "timestamp": 76.29,
                "direction": "Straight"
            },
            {
                "timestamp": 76.32,
                "direction": "Straight"
            },
            {
                "timestamp": 76.36,
                "direction": "Straight"
            },
            {
                "timestamp": 76.39,
                "direction": "Straight"
            },
            {
                "timestamp": 76.42,
                "direction": "Straight"
            },
            {
                "timestamp": 76.46,
                "direction": "Straight"
            },
            {
                "timestamp": 76.49,
                "direction": "Straight"
            },
            {
                "timestamp": 76.52,
                "direction": "Straight"
            },
            {
                "timestamp": 76.56,
                "direction": "Straight"
            },
            {
                "timestamp": 76.59,
                "direction": "Straight"
            },
            {
                "timestamp": 76.62,
                "direction": "Straight"
            },
            {
                "timestamp": 76.66,
                "direction": "Straight"
            },
            {
                "timestamp": 76.69,
                "direction": "Straight"
            },
            {
                "timestamp": 76.72,
                "direction": "Straight"
            },
            {
                "timestamp": 76.76,
                "direction": "Straight"
            },
            {
                "timestamp": 76.79,
                "direction": "Straight"
            },
            {
                "timestamp": 76.82,
                "direction": "Straight"
            },
            {
                "timestamp": 76.86,
                "direction": "Slight Left"
            },
            {
                "timestamp": 76.89,
                "direction": "Slight Left"
            },
            {
                "timestamp": 76.92,
                "direction": "Slight Left"
            },
            {
                "timestamp": 76.96,
                "direction": "Slight Left"
            },
            {
                "timestamp": 76.99,
                "direction": "Slight Left"
            },
            {
                "timestamp": 77.02,
                "direction": "Slight Left"
            },
            {
                "timestamp": 77.06,
                "direction": "Slight Left"
            },
            {
                "timestamp": 77.09,
                "direction": "Slight Left"
            },
            {
                "timestamp": 77.12,
                "direction": "Slight Left"
            },
            {
                "timestamp": 77.16,
                "direction": "Left"
            },
            {
                "timestamp": 77.19,
                "direction": "Slight Left"
            },
            {
                "timestamp": 77.22,
                "direction": "Slight Left"
            },
            {
                "timestamp": 77.26,
                "direction": "Left"
            },
            {
                "timestamp": 77.29,
                "direction": "Slight Left"
            },
            {
                "timestamp": 77.32,
                "direction": "Slight Left"
            },
            {
                "timestamp": 77.36,
                "direction": "Slight Left"
            },
            {
                "timestamp": 77.39,
                "direction": "Slight Left"
            },
            {
                "timestamp": 77.42,
                "direction": "Straight"
            },
            {
                "timestamp": 77.46,
                "direction": "Straight"
            },
            {
                "timestamp": 77.49,
                "direction": "Straight"
            },
            {
                "timestamp": 77.52,
                "direction": "Straight"
            },
            {
                "timestamp": 77.56,
                "direction": "Straight"
            },
            {
                "timestamp": 77.59,
                "direction": "Straight"
            },
            {
                "timestamp": 77.63,
                "direction": "Straight"
            },
            {
                "timestamp": 77.66,
                "direction": "Straight"
            },
            {
                "timestamp": 77.69,
                "direction": "Straight"
            },
            {
                "timestamp": 77.73,
                "direction": "Straight"
            },
            {
                "timestamp": 77.76,
                "direction": "Straight"
            },
            {
                "timestamp": 77.79,
                "direction": "Straight"
            },
            {
                "timestamp": 77.83,
                "direction": "Straight"
            },
            {
                "timestamp": 77.86,
                "direction": "Straight"
            },
            {
                "timestamp": 77.89,
                "direction": "Straight"
            },
            {
                "timestamp": 77.93,
                "direction": "Straight"
            },
            {
                "timestamp": 77.96,
                "direction": "Straight"
            },
            {
                "timestamp": 77.99,
                "direction": "Straight"
            },
            {
                "timestamp": 78.03,
                "direction": "Straight"
            },
            {
                "timestamp": 78.06,
                "direction": "Straight"
            },
            {
                "timestamp": 78.09,
                "direction": "Straight"
            },
            {
                "timestamp": 78.13,
                "direction": "Straight"
            },
            {
                "timestamp": 78.16,
                "direction": "Straight"
            },
            {
                "timestamp": 78.19,
                "direction": "Straight"
            },
            {
                "timestamp": 78.23,
                "direction": "Straight"
            },
            {
                "timestamp": 78.26,
                "direction": "Straight"
            },
            {
                "timestamp": 78.29,
                "direction": "Straight"
            },
            {
                "timestamp": 78.33,
                "direction": "Straight"
            },
            {
                "timestamp": 78.36,
                "direction": "Straight"
            },
            {
                "timestamp": 78.39,
                "direction": "Straight"
            },
            {
                "timestamp": 78.43,
                "direction": "Straight"
            },
            {
                "timestamp": 78.46,
                "direction": "Straight"
            },
            {
                "timestamp": 78.49,
                "direction": "Straight"
            },
            {
                "timestamp": 78.53,
                "direction": "Straight"
            },
            {
                "timestamp": 78.56,
                "direction": "Straight"
            },
            {
                "timestamp": 78.59,
                "direction": "Straight"
            },
            {
                "timestamp": 78.63,
                "direction": "Straight"
            },
            {
                "timestamp": 78.66,
                "direction": "Straight"
            },
            {
                "timestamp": 78.69,
                "direction": "Straight"
            },
            {
                "timestamp": 78.73,
                "direction": "Straight"
            },
            {
                "timestamp": 78.76,
                "direction": "Straight"
            },
            {
                "timestamp": 78.79,
                "direction": "Straight"
            },
            {
                "timestamp": 78.83,
                "direction": "Straight"
            },
            {
                "timestamp": 78.86,
                "direction": "Straight"
            },
            {
                "timestamp": 78.89,
                "direction": "Straight"
            },
            {
                "timestamp": 78.93,
                "direction": "Slight Right"
            },
            {
                "timestamp": 78.96,
                "direction": "Slight Right"
            },
            {
                "timestamp": 78.99,
                "direction": "Slight Right"
            },
            {
                "timestamp": 79.03,
                "direction": "Slight Right"
            },
            {
                "timestamp": 79.06,
                "direction": "Slight Right"
            },
            {
                "timestamp": 79.09,
                "direction": "Slight Right"
            },
            {
                "timestamp": 79.13,
                "direction": "Slight Right"
            },
            {
                "timestamp": 79.16,
                "direction": "Slight Right"
            },
            {
                "timestamp": 79.19,
                "direction": "Straight"
            },
            {
                "timestamp": 79.23,
                "direction": "Straight"
            },
            {
                "timestamp": 79.26,
                "direction": "Straight"
            },
            {
                "timestamp": 79.29,
                "direction": "Straight"
            },
            {
                "timestamp": 79.33,
                "direction": "Straight"
            },
            {
                "timestamp": 79.36,
                "direction": "Straight"
            },
            {
                "timestamp": 79.39,
                "direction": "Straight"
            },
            {
                "timestamp": 79.43,
                "direction": "Straight"
            },
            {
                "timestamp": 79.46,
                "direction": "Straight"
            },
            {
                "timestamp": 79.49,
                "direction": "Straight"
            },
            {
                "timestamp": 79.53,
                "direction": "Straight"
            },
            {
                "timestamp": 79.56,
                "direction": "Straight"
            },
            {
                "timestamp": 79.59,
                "direction": "Straight"
            },
            {
                "timestamp": 79.63,
                "direction": "Straight"
            },
            {
                "timestamp": 79.66,
                "direction": "Straight"
            },
            {
                "timestamp": 79.69,
                "direction": "Straight"
            },
            {
                "timestamp": 79.73,
                "direction": "Straight"
            },
            {
                "timestamp": 79.76,
                "direction": "Straight"
            },
            {
                "timestamp": 79.79,
                "direction": "Straight"
            },
            {
                "timestamp": 79.83,
                "direction": "Straight"
            },
            {
                "timestamp": 79.86,
                "direction": "Straight"
            },
            {
                "timestamp": 79.89,
                "direction": "Slight Right"
            },
            {
                "timestamp": 79.93,
                "direction": "Slight Right"
            },
            {
                "timestamp": 79.96,
                "direction": "Slight Right"
            },
            {
                "timestamp": 79.99,
                "direction": "Straight"
            },
            {
                "timestamp": 80.03,
                "direction": "Slight Right"
            },
            {
                "timestamp": 80.06,
                "direction": "Slight Right"
            },
            {
                "timestamp": 80.09,
                "direction": "Slight Right"
            },
            {
                "timestamp": 80.13,
                "direction": "Slight Right"
            },
            {
                "timestamp": 80.16,
                "direction": "Slight Right"
            },
            {
                "timestamp": 80.19,
                "direction": "Slight Right"
            },
            {
                "timestamp": 80.23,
                "direction": "Slight Right"
            },
            {
                "timestamp": 80.26,
                "direction": "Slight Right"
            },
            {
                "timestamp": 80.29,
                "direction": "Slight Right"
            },
            {
                "timestamp": 80.33,
                "direction": "Slight Right"
            },
            {
                "timestamp": 80.36,
                "direction": "Slight Right"
            },
            {
                "timestamp": 80.39,
                "direction": "Straight"
            },
            {
                "timestamp": 80.43,
                "direction": "Straight"
            },
            {
                "timestamp": 80.46,
                "direction": "Straight"
            },
            {
                "timestamp": 80.49,
                "direction": "Straight"
            },
            {
                "timestamp": 80.53,
                "direction": "Straight"
            },
            {
                "timestamp": 80.56,
                "direction": "Straight"
            },
            {
                "timestamp": 80.59,
                "direction": "Straight"
            },
            {
                "timestamp": 80.63,
                "direction": "Straight"
            },
            {
                "timestamp": 80.66,
                "direction": "Straight"
            },
            {
                "timestamp": 80.69,
                "direction": "Straight"
            },
            {
                "timestamp": 80.73,
                "direction": "Straight"
            },
            {
                "timestamp": 80.76,
                "direction": "Straight"
            },
            {
                "timestamp": 80.79,
                "direction": "Straight"
            },
            {
                "timestamp": 80.83,
                "direction": "Straight"
            },
            {
                "timestamp": 80.86,
                "direction": "Straight"
            },
            {
                "timestamp": 80.89,
                "direction": "Straight"
            },
            {
                "timestamp": 80.93,
                "direction": "Straight"
            },
            {
                "timestamp": 80.96,
                "direction": "Straight"
            },
            {
                "timestamp": 80.99,
                "direction": "Straight"
            },
            {
                "timestamp": 81.03,
                "direction": "Straight"
            },
            {
                "timestamp": 81.06,
                "direction": "Straight"
            },
            {
                "timestamp": 81.09,
                "direction": "Straight"
            },
            {
                "timestamp": 81.13,
                "direction": "Straight"
            },
            {
                "timestamp": 81.16,
                "direction": "Straight"
            },
            {
                "timestamp": 81.19,
                "direction": "Straight"
            },
            {
                "timestamp": 81.23,
                "direction": "Straight"
            },
            {
                "timestamp": 81.26,
                "direction": "Straight"
            },
            {
                "timestamp": 81.29,
                "direction": "Straight"
            },
            {
                "timestamp": 81.33,
                "direction": "Straight"
            },
            {
                "timestamp": 81.36,
                "direction": "Straight"
            },
            {
                "timestamp": 81.39,
                "direction": "Straight"
            },
            {
                "timestamp": 81.43,
                "direction": "Straight"
            },
            {
                "timestamp": 81.46,
                "direction": "Straight"
            },
            {
                "timestamp": 81.49,
                "direction": "Straight"
            },
            {
                "timestamp": 81.53,
                "direction": "Straight"
            },
            {
                "timestamp": 81.56,
                "direction": "Straight"
            },
            {
                "timestamp": 81.59,
                "direction": "Straight"
            },
            {
                "timestamp": 81.63,
                "direction": "Straight"
            },
            {
                "timestamp": 81.66,
                "direction": "Straight"
            },
            {
                "timestamp": 81.69,
                "direction": "Straight"
            },
            {
                "timestamp": 81.73,
                "direction": "Straight"
            },
            {
                "timestamp": 81.76,
                "direction": "Straight"
            },
            {
                "timestamp": 81.79,
                "direction": "Straight"
            },
            {
                "timestamp": 81.83,
                "direction": "Straight"
            },
            {
                "timestamp": 81.86,
                "direction": "Straight"
            },
            {
                "timestamp": 81.89,
                "direction": "Straight"
            },
            {
                "timestamp": 81.93,
                "direction": "Straight"
            },
            {
                "timestamp": 81.96,
                "direction": "Straight"
            },
            {
                "timestamp": 82.0,
                "direction": "Straight"
            },
            {
                "timestamp": 82.03,
                "direction": "Straight"
            },
            {
                "timestamp": 82.06,
                "direction": "Straight"
            },
            {
                "timestamp": 82.1,
                "direction": "Straight"
            },
            {
                "timestamp": 82.13,
                "direction": "Straight"
            },
            {
                "timestamp": 82.16,
                "direction": "Straight"
            },
            {
                "timestamp": 82.2,
                "direction": "Straight"
            },
            {
                "timestamp": 82.23,
                "direction": "Straight"
            },
            {
                "timestamp": 82.26,
                "direction": "Straight"
            },
            {
                "timestamp": 82.3,
                "direction": "Straight"
            },
            {
                "timestamp": 82.33,
                "direction": "Straight"
            },
            {
                "timestamp": 82.36,
                "direction": "Straight"
            },
            {
                "timestamp": 82.4,
                "direction": "Straight"
            },
            {
                "timestamp": 82.43,
                "direction": "Straight"
            },
            {
                "timestamp": 82.46,
                "direction": "Straight"
            },
            {
                "timestamp": 82.5,
                "direction": "Straight"
            },
            {
                "timestamp": 82.53,
                "direction": "Slight Right"
            },
            {
                "timestamp": 82.56,
                "direction": "Slight Right"
            },
            {
                "timestamp": 82.6,
                "direction": "Slight Right"
            },
            {
                "timestamp": 82.63,
                "direction": "Slight Right"
            },
            {
                "timestamp": 82.66,
                "direction": "Slight Right"
            },
            {
                "timestamp": 82.7,
                "direction": "Slight Right"
            },
            {
                "timestamp": 82.73,
                "direction": "Slight Right"
            },
            {
                "timestamp": 82.76,
                "direction": "Slight Right"
            },
            {
                "timestamp": 82.8,
                "direction": "Slight Right"
            },
            {
                "timestamp": 82.83,
                "direction": "Straight"
            },
            {
                "timestamp": 82.86,
                "direction": "Straight"
            },
            {
                "timestamp": 82.9,
                "direction": "Straight"
            },
            {
                "timestamp": 82.93,
                "direction": "Straight"
            },
            {
                "timestamp": 82.96,
                "direction": "Straight"
            },
            {
                "timestamp": 83.0,
                "direction": "Straight"
            },
            {
                "timestamp": 83.03,
                "direction": "Straight"
            },
            {
                "timestamp": 83.06,
                "direction": "Straight"
            },
            {
                "timestamp": 83.1,
                "direction": "Straight"
            },
            {
                "timestamp": 83.13,
                "direction": "Straight"
            },
            {
                "timestamp": 83.16,
                "direction": "Straight"
            },
            {
                "timestamp": 83.2,
                "direction": "Straight"
            },
            {
                "timestamp": 83.23,
                "direction": "Straight"
            },
            {
                "timestamp": 83.26,
                "direction": "Straight"
            },
            {
                "timestamp": 83.3,
                "direction": "Straight"
            },
            {
                "timestamp": 83.33,
                "direction": "Straight"
            },
            {
                "timestamp": 83.36,
                "direction": "Straight"
            },
            {
                "timestamp": 83.4,
                "direction": "Straight"
            },
            {
                "timestamp": 83.43,
                "direction": "Straight"
            },
            {
                "timestamp": 83.46,
                "direction": "Straight"
            },
            {
                "timestamp": 83.5,
                "direction": "Straight"
            },
            {
                "timestamp": 83.53,
                "direction": "Straight"
            },
            {
                "timestamp": 83.56,
                "direction": "Slight Right"
            },
            {
                "timestamp": 83.6,
                "direction": "Straight"
            },
            {
                "timestamp": 83.63,
                "direction": "Slight Right"
            },
            {
                "timestamp": 83.66,
                "direction": "Slight Right"
            },
            {
                "timestamp": 83.7,
                "direction": "Slight Right"
            },
            {
                "timestamp": 83.73,
                "direction": "Slight Right"
            },
            {
                "timestamp": 83.76,
                "direction": "Slight Right"
            },
            {
                "timestamp": 83.8,
                "direction": "Slight Right"
            },
            {
                "timestamp": 83.83,
                "direction": "Slight Right"
            },
            {
                "timestamp": 83.86,
                "direction": "Slight Right"
            },
            {
                "timestamp": 83.9,
                "direction": "Slight Right"
            },
            {
                "timestamp": 83.93,
                "direction": "Slight Right"
            },
            {
                "timestamp": 83.96,
                "direction": "Slight Right"
            },
            {
                "timestamp": 84.0,
                "direction": "Slight Right"
            },
            {
                "timestamp": 84.03,
                "direction": "Slight Right"
            },
            {
                "timestamp": 84.06,
                "direction": "Straight"
            },
            {
                "timestamp": 84.1,
                "direction": "Straight"
            },
            {
                "timestamp": 84.13,
                "direction": "Straight"
            },
            {
                "timestamp": 84.16,
                "direction": "Straight"
            },
            {
                "timestamp": 84.2,
                "direction": "Straight"
            },
            {
                "timestamp": 84.23,
                "direction": "Straight"
            },
            {
                "timestamp": 84.26,
                "direction": "Straight"
            },
            {
                "timestamp": 84.3,
                "direction": "Straight"
            },
            {
                "timestamp": 84.33,
                "direction": "Straight"
            },
            {
                "timestamp": 84.36,
                "direction": "Straight"
            },
            {
                "timestamp": 84.4,
                "direction": "Straight"
            },
            {
                "timestamp": 84.43,
                "direction": "Straight"
            },
            {
                "timestamp": 84.46,
                "direction": "Straight"
            },
            {
                "timestamp": 84.5,
                "direction": "Straight"
            },
            {
                "timestamp": 84.53,
                "direction": "Straight"
            },
            {
                "timestamp": 84.56,
                "direction": "Straight"
            },
            {
                "timestamp": 84.6,
                "direction": "Straight"
            },
            {
                "timestamp": 84.63,
                "direction": "Straight"
            },
            {
                "timestamp": 84.66,
                "direction": "Straight"
            },
            {
                "timestamp": 84.7,
                "direction": "Straight"
            },
            {
                "timestamp": 84.73,
                "direction": "Straight"
            },
            {
                "timestamp": 84.76,
                "direction": "Straight"
            },
            {
                "timestamp": 84.8,
                "direction": "Straight"
            },
            {
                "timestamp": 84.83,
                "direction": "Straight"
            },
            {
                "timestamp": 84.86,
                "direction": "Straight"
            },
            {
                "timestamp": 84.9,
                "direction": "Straight"
            },
            {
                "timestamp": 84.93,
                "direction": "Straight"
            },
            {
                "timestamp": 84.96,
                "direction": "Straight"
            },
            {
                "timestamp": 85.0,
                "direction": "Straight"
            },
            {
                "timestamp": 85.03,
                "direction": "Straight"
            },
            {
                "timestamp": 85.06,
                "direction": "Straight"
            },
            {
                "timestamp": 85.1,
                "direction": "Straight"
            },
            {
                "timestamp": 85.13,
                "direction": "Straight"
            },
            {
                "timestamp": 85.16,
                "direction": "Straight"
            },
            {
                "timestamp": 85.2,
                "direction": "Straight"
            },
            {
                "timestamp": 85.23,
                "direction": "Straight"
            },
            {
                "timestamp": 85.26,
                "direction": "Straight"
            },
            {
                "timestamp": 85.3,
                "direction": "Straight"
            },
            {
                "timestamp": 85.33,
                "direction": "Straight"
            },
            {
                "timestamp": 85.36,
                "direction": "Straight"
            },
            {
                "timestamp": 85.4,
                "direction": "Straight"
            },
            {
                "timestamp": 85.43,
                "direction": "Straight"
            },
            {
                "timestamp": 85.46,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.5,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.53,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.56,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.6,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.63,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.66,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.7,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.73,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.76,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.8,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.83,
                "direction": "Slight Left"
            },
            {
                "timestamp": 85.86,
                "direction": "Straight"
            },
            {
                "timestamp": 85.9,
                "direction": "Straight"
            },
            {
                "timestamp": 85.93,
                "direction": "Straight"
            },
            {
                "timestamp": 85.96,
                "direction": "Straight"
            },
            {
                "timestamp": 86.0,
                "direction": "Straight"
            },
            {
                "timestamp": 86.03,
                "direction": "Straight"
            },
            {
                "timestamp": 86.06,
                "direction": "Straight"
            },
            {
                "timestamp": 86.1,
                "direction": "Straight"
            },
            {
                "timestamp": 86.13,
                "direction": "Straight"
            },
            {
                "timestamp": 86.16,
                "direction": "Straight"
            },
            {
                "timestamp": 86.2,
                "direction": "Straight"
            },
            {
                "timestamp": 86.23,
                "direction": "Straight"
            },
            {
                "timestamp": 86.26,
                "direction": "Straight"
            },
            {
                "timestamp": 86.3,
                "direction": "Straight"
            },
            {
                "timestamp": 86.33,
                "direction": "Straight"
            },
            {
                "timestamp": 86.36,
                "direction": "Straight"
            },
            {
                "timestamp": 86.4,
                "direction": "Straight"
            },
            {
                "timestamp": 86.43,
                "direction": "Straight"
            },
            {
                "timestamp": 86.47,
                "direction": "Straight"
            },
            {
                "timestamp": 86.5,
                "direction": "Straight"
            },
            {
                "timestamp": 86.53,
                "direction": "Straight"
            },
            {
                "timestamp": 86.57,
                "direction": "Straight"
            },
            {
                "timestamp": 86.6,
                "direction": "Straight"
            },
            {
                "timestamp": 86.63,
                "direction": "Straight"
            },
            {
                "timestamp": 86.67,
                "direction": "Straight"
            },
            {
                "timestamp": 86.7,
                "direction": "Straight"
            },
            {
                "timestamp": 86.73,
                "direction": "Straight"
            },
            {
                "timestamp": 86.77,
                "direction": "Straight"
            },
            {
                "timestamp": 86.8,
                "direction": "Straight"
            },
            {
                "timestamp": 86.83,
                "direction": "Straight"
            },
            {
                "timestamp": 86.87,
                "direction": "Straight"
            },
            {
                "timestamp": 86.9,
                "direction": "Straight"
            },
            {
                "timestamp": 86.93,
                "direction": "Straight"
            },
            {
                "timestamp": 86.97,
                "direction": "Straight"
            },
            {
                "timestamp": 87.0,
                "direction": "Straight"
            },
            {
                "timestamp": 87.03,
                "direction": "Straight"
            },
            {
                "timestamp": 87.07,
                "direction": "Straight"
            },
            {
                "timestamp": 87.1,
                "direction": "Straight"
            },
            {
                "timestamp": 87.13,
                "direction": "Straight"
            },
            {
                "timestamp": 87.17,
                "direction": "Straight"
            },
            {
                "timestamp": 87.2,
                "direction": "Straight"
            },
            {
                "timestamp": 87.23,
                "direction": "Straight"
            },
            {
                "timestamp": 87.27,
                "direction": "Straight"
            },
            {
                "timestamp": 87.3,
                "direction": "Straight"
            },
            {
                "timestamp": 87.33,
                "direction": "Straight"
            },
            {
                "timestamp": 87.37,
                "direction": "Straight"
            },
            {
                "timestamp": 87.4,
                "direction": "Straight"
            },
            {
                "timestamp": 87.43,
                "direction": "Straight"
            },
            {
                "timestamp": 87.47,
                "direction": "Straight"
            },
            {
                "timestamp": 87.5,
                "direction": "Straight"
            },
            {
                "timestamp": 87.53,
                "direction": "Straight"
            },
            {
                "timestamp": 87.57,
                "direction": "Straight"
            },
            {
                "timestamp": 87.6,
                "direction": "Straight"
            },
            {
                "timestamp": 87.63,
                "direction": "Straight"
            },
            {
                "timestamp": 87.67,
                "direction": "Straight"
            },
            {
                "timestamp": 87.7,
                "direction": "Straight"
            },
            {
                "timestamp": 87.73,
                "direction": "Straight"
            },
            {
                "timestamp": 87.77,
                "direction": "Straight"
            },
            {
                "timestamp": 87.8,
                "direction": "Straight"
            },
            {
                "timestamp": 87.83,
                "direction": "Straight"
            },
            {
                "timestamp": 87.87,
                "direction": "Straight"
            },
            {
                "timestamp": 87.9,
                "direction": "Straight"
            },
            {
                "timestamp": 87.93,
                "direction": "Straight"
            },
            {
                "timestamp": 87.97,
                "direction": "Straight"
            },
            {
                "timestamp": 88.0,
                "direction": "Straight"
            },
            {
                "timestamp": 88.03,
                "direction": "Straight"
            },
            {
                "timestamp": 88.07,
                "direction": "Straight"
            },
            {
                "timestamp": 88.1,
                "direction": "Straight"
            },
            {
                "timestamp": 88.13,
                "direction": "Straight"
            },
            {
                "timestamp": 88.17,
                "direction": "Straight"
            },
            {
                "timestamp": 88.2,
                "direction": "Straight"
            },
            {
                "timestamp": 88.23,
                "direction": "Straight"
            },
            {
                "timestamp": 88.27,
                "direction": "Straight"
            },
            {
                "timestamp": 88.3,
                "direction": "Straight"
            },
            {
                "timestamp": 88.33,
                "direction": "Straight"
            },
            {
                "timestamp": 88.37,
                "direction": "Straight"
            },
            {
                "timestamp": 88.4,
                "direction": "Straight"
            },
            {
                "timestamp": 88.43,
                "direction": "Straight"
            },
            {
                "timestamp": 88.47,
                "direction": "Straight"
            },
            {
                "timestamp": 88.5,
                "direction": "Straight"
            },
            {
                "timestamp": 88.53,
                "direction": "Straight"
            },
            {
                "timestamp": 88.57,
                "direction": "Straight"
            },
            {
                "timestamp": 88.6,
                "direction": "Straight"
            },
            {
                "timestamp": 88.63,
                "direction": "Straight"
            },
            {
                "timestamp": 88.67,
                "direction": "Straight"
            },
            {
                "timestamp": 88.7,
                "direction": "Straight"
            },
            {
                "timestamp": 88.73,
                "direction": "Straight"
            },
            {
                "timestamp": 88.77,
                "direction": "Straight"
            },
            {
                "timestamp": 88.8,
                "direction": "Straight"
            },
            {
                "timestamp": 88.83,
                "direction": "Straight"
            },
            {
                "timestamp": 88.87,
                "direction": "Straight"
            },
            {
                "timestamp": 88.9,
                "direction": "Straight"
            },
            {
                "timestamp": 88.93,
                "direction": "Straight"
            },
            {
                "timestamp": 88.97,
                "direction": "Straight"
            },
            {
                "timestamp": 89.0,
                "direction": "Straight"
            },
            {
                "timestamp": 89.03,
                "direction": "Straight"
            },
            {
                "timestamp": 89.07,
                "direction": "Straight"
            },
            {
                "timestamp": 89.1,
                "direction": "Straight"
            },
            {
                "timestamp": 89.13,
                "direction": "Straight"
            },
            {
                "timestamp": 89.17,
                "direction": "Straight"
            },
            {
                "timestamp": 89.2,
                "direction": "Straight"
            },
            {
                "timestamp": 89.23,
                "direction": "Straight"
            },
            {
                "timestamp": 89.27,
                "direction": "Straight"
            },
            {
                "timestamp": 89.3,
                "direction": "Straight"
            },
            {
                "timestamp": 89.33,
                "direction": "Straight"
            },
            {
                "timestamp": 89.37,
                "direction": "Straight"
            },
            {
                "timestamp": 89.4,
                "direction": "Straight"
            },
            {
                "timestamp": 89.43,
                "direction": "Straight"
            },
            {
                "timestamp": 89.47,
                "direction": "Straight"
            },
            {
                "timestamp": 89.5,
                "direction": "Straight"
            },
            {
                "timestamp": 89.53,
                "direction": "Straight"
            },
            {
                "timestamp": 89.57,
                "direction": "Straight"
            },
            {
                "timestamp": 89.6,
                "direction": "Straight"
            },
            {
                "timestamp": 89.63,
                "direction": "Straight"
            },
            {
                "timestamp": 89.67,
                "direction": "Straight"
            },
            {
                "timestamp": 89.7,
                "direction": "Straight"
            },
            {
                "timestamp": 89.73,
                "direction": "Straight"
            },
            {
                "timestamp": 89.77,
                "direction": "Straight"
            },
            {
                "timestamp": 89.8,
                "direction": "Straight"
            },
            {
                "timestamp": 89.83,
                "direction": "Straight"
            },
            {
                "timestamp": 89.87,
                "direction": "Straight"
            },
            {
                "timestamp": 89.9,
                "direction": "Straight"
            },
            {
                "timestamp": 89.93,
                "direction": "Straight"
            },
            {
                "timestamp": 89.97,
                "direction": "Straight"
            },
            {
                "timestamp": 90.0,
                "direction": "Straight"
            },
            {
                "timestamp": 90.03,
                "direction": "Straight"
            },
            {
                "timestamp": 90.07,
                "direction": "Straight"
            },
            {
                "timestamp": 90.1,
                "direction": "Straight"
            },
            {
                "timestamp": 90.13,
                "direction": "Straight"
            },
            {
                "timestamp": 90.17,
                "direction": "Straight"
            },
            {
                "timestamp": 90.2,
                "direction": "Straight"
            },
            {
                "timestamp": 90.23,
                "direction": "Straight"
            },
            {
                "timestamp": 90.27,
                "direction": "Straight"
            },
            {
                "timestamp": 90.3,
                "direction": "Straight"
            },
            {
                "timestamp": 90.33,
                "direction": "Straight"
            },
            {
                "timestamp": 90.37,
                "direction": "Straight"
            },
            {
                "timestamp": 90.4,
                "direction": "Straight"
            },
            {
                "timestamp": 90.43,
                "direction": "Straight"
            },
            {
                "timestamp": 90.47,
                "direction": "Straight"
            },
            {
                "timestamp": 90.5,
                "direction": "Straight"
            },
            {
                "timestamp": 90.53,
                "direction": "Straight"
            },
            {
                "timestamp": 90.57,
                "direction": "Straight"
            },
            {
                "timestamp": 90.6,
                "direction": "Straight"
            },
            {
                "timestamp": 90.63,
                "direction": "Straight"
            },
            {
                "timestamp": 90.67,
                "direction": "Straight"
            },
            {
                "timestamp": 90.7,
                "direction": "Straight"
            },
            {
                "timestamp": 90.73,
                "direction": "Straight"
            },
            {
                "timestamp": 90.77,
                "direction": "Straight"
            },
            {
                "timestamp": 90.8,
                "direction": "Straight"
            },
            {
                "timestamp": 90.84,
                "direction": "Straight"
            },
            {
                "timestamp": 90.87,
                "direction": "Straight"
            },
            {
                "timestamp": 90.9,
                "direction": "Straight"
            },
            {
                "timestamp": 90.94,
                "direction": "Straight"
            },
            {
                "timestamp": 90.97,
                "direction": "Slight Right"
            },
            {
                "timestamp": 91.0,
                "direction": "Slight Right"
            },
            {
                "timestamp": 91.04,
                "direction": "Slight Right"
            },
            {
                "timestamp": 91.07,
                "direction": "Slight Right"
            },
            {
                "timestamp": 91.1,
                "direction": "Straight"
            },
            {
                "timestamp": 91.14,
                "direction": "Straight"
            },
            {
                "timestamp": 91.17,
                "direction": "Straight"
            },
            {
                "timestamp": 91.2,
                "direction": "Straight"
            },
            {
                "timestamp": 91.24,
                "direction": "Straight"
            },
            {
                "timestamp": 91.27,
                "direction": "Straight"
            },
            {
                "timestamp": 91.3,
                "direction": "Straight"
            },
            {
                "timestamp": 91.34,
                "direction": "Straight"
            },
            {
                "timestamp": 91.37,
                "direction": "Straight"
            },
            {
                "timestamp": 91.4,
                "direction": "Straight"
            },
            {
                "timestamp": 91.44,
                "direction": "Straight"
            },
            {
                "timestamp": 91.47,
                "direction": "Straight"
            },
            {
                "timestamp": 91.5,
                "direction": "Straight"
            },
            {
                "timestamp": 91.54,
                "direction": "Straight"
            },
            {
                "timestamp": 91.57,
                "direction": "Straight"
            },
            {
                "timestamp": 91.6,
                "direction": "Straight"
            },
            {
                "timestamp": 91.64,
                "direction": "Straight"
            },
            {
                "timestamp": 91.67,
                "direction": "Straight"
            },
            {
                "timestamp": 91.7,
                "direction": "Straight"
            },
            {
                "timestamp": 91.74,
                "direction": "Straight"
            },
            {
                "timestamp": 91.77,
                "direction": "Straight"
            },
            {
                "timestamp": 91.8,
                "direction": "Straight"
            },
            {
                "timestamp": 91.84,
                "direction": "Straight"
            },
            {
                "timestamp": 91.87,
                "direction": "Straight"
            },
            {
                "timestamp": 91.9,
                "direction": "Straight"
            },
            {
                "timestamp": 91.94,
                "direction": "Straight"
            },
            {
                "timestamp": 91.97,
                "direction": "Straight"
            },
            {
                "timestamp": 92.0,
                "direction": "Straight"
            },
            {
                "timestamp": 92.04,
                "direction": "Straight"
            },
            {
                "timestamp": 92.07,
                "direction": "Straight"
            },
            {
                "timestamp": 92.1,
                "direction": "Straight"
            },
            {
                "timestamp": 92.14,
                "direction": "Straight"
            },
            {
                "timestamp": 92.17,
                "direction": "Straight"
            },
            {
                "timestamp": 92.2,
                "direction": "Straight"
            },
            {
                "timestamp": 92.24,
                "direction": "Straight"
            },
            {
                "timestamp": 92.27,
                "direction": "Straight"
            },
            {
                "timestamp": 92.3,
                "direction": "Straight"
            },
            {
                "timestamp": 92.34,
                "direction": "Straight"
            },
            {
                "timestamp": 92.37,
                "direction": "Straight"
            },
            {
                "timestamp": 92.4,
                "direction": "Straight"
            },
            {
                "timestamp": 92.44,
                "direction": "Straight"
            },
            {
                "timestamp": 92.47,
                "direction": "Straight"
            },
            {
                "timestamp": 92.5,
                "direction": "Straight"
            },
            {
                "timestamp": 92.54,
                "direction": "Straight"
            },
            {
                "timestamp": 92.57,
                "direction": "Straight"
            },
            {
                "timestamp": 92.6,
                "direction": "Straight"
            },
            {
                "timestamp": 92.64,
                "direction": "Straight"
            },
            {
                "timestamp": 92.67,
                "direction": "Straight"
            },
            {
                "timestamp": 92.7,
                "direction": "Straight"
            },
            {
                "timestamp": 92.74,
                "direction": "Straight"
            },
            {
                "timestamp": 92.77,
                "direction": "Straight"
            },
            {
                "timestamp": 92.8,
                "direction": "Straight"
            },
            {
                "timestamp": 92.84,
                "direction": "Straight"
            },
            {
                "timestamp": 92.87,
                "direction": "Straight"
            },
            {
                "timestamp": 92.9,
                "direction": "Straight"
            },
            {
                "timestamp": 92.94,
                "direction": "Straight"
            },
            {
                "timestamp": 92.97,
                "direction": "Straight"
            },
            {
                "timestamp": 93.0,
                "direction": "Straight"
            },
            {
                "timestamp": 93.04,
                "direction": "Straight"
            },
            {
                "timestamp": 93.07,
                "direction": "Straight"
            },
            {
                "timestamp": 93.1,
                "direction": "Straight"
            },
            {
                "timestamp": 93.14,
                "direction": "Straight"
            },
            {
                "timestamp": 93.17,
                "direction": "Straight"
            },
            {
                "timestamp": 93.2,
                "direction": "Straight"
            },
            {
                "timestamp": 93.24,
                "direction": "Straight"
            },
            {
                "timestamp": 93.27,
                "direction": "Straight"
            },
            {
                "timestamp": 93.3,
                "direction": "Straight"
            },
            {
                "timestamp": 93.34,
                "direction": "Straight"
            },
            {
                "timestamp": 93.37,
                "direction": "Straight"
            },
            {
                "timestamp": 93.4,
                "direction": "Straight"
            },
            {
                "timestamp": 93.44,
                "direction": "Straight"
            },
            {
                "timestamp": 93.47,
                "direction": "Straight"
            },
            {
                "timestamp": 93.5,
                "direction": "Straight"
            },
            {
                "timestamp": 93.54,
                "direction": "Straight"
            },
            {
                "timestamp": 93.57,
                "direction": "Straight"
            },
            {
                "timestamp": 93.6,
                "direction": "Straight"
            },
            {
                "timestamp": 93.64,
                "direction": "Straight"
            },
            {
                "timestamp": 93.67,
                "direction": "Straight"
            },
            {
                "timestamp": 93.7,
                "direction": "Straight"
            },
            {
                "timestamp": 93.74,
                "direction": "Straight"
            },
            {
                "timestamp": 93.77,
                "direction": "Straight"
            },
            {
                "timestamp": 93.8,
                "direction": "Straight"
            },
            {
                "timestamp": 93.84,
                "direction": "Straight"
            },
            {
                "timestamp": 93.87,
                "direction": "Slight Left"
            },
            {
                "timestamp": 93.9,
                "direction": "Slight Left"
            },
            {
                "timestamp": 93.94,
                "direction": "Slight Left"
            },
            {
                "timestamp": 93.97,
                "direction": "Slight Left"
            },
            {
                "timestamp": 94.0,
                "direction": "Slight Left"
            },
            {
                "timestamp": 94.04,
                "direction": "Slight Left"
            },
            {
                "timestamp": 94.07,
                "direction": "Slight Left"
            },
            {
                "timestamp": 94.1,
                "direction": "Straight"
            },
            {
                "timestamp": 94.14,
                "direction": "Straight"
            },
            {
                "timestamp": 94.17,
                "direction": "Straight"
            },
            {
                "timestamp": 94.2,
                "direction": "Straight"
            },
            {
                "timestamp": 94.24,
                "direction": "Straight"
            },
            {
                "timestamp": 94.27,
                "direction": "Straight"
            },
            {
                "timestamp": 94.3,
                "direction": "Straight"
            },
            {
                "timestamp": 94.34,
                "direction": "Straight"
            },
            {
                "timestamp": 94.37,
                "direction": "Straight"
            },
            {
                "timestamp": 94.4,
                "direction": "Straight"
            },
            {
                "timestamp": 94.44,
                "direction": "Straight"
            },
            {
                "timestamp": 94.47,
                "direction": "Straight"
            },
            {
                "timestamp": 94.5,
                "direction": "Straight"
            },
            {
                "timestamp": 94.54,
                "direction": "Straight"
            },
            {
                "timestamp": 94.57,
                "direction": "Straight"
            },
            {
                "timestamp": 94.6,
                "direction": "Straight"
            },
            {
                "timestamp": 94.64,
                "direction": "Straight"
            },
            {
                "timestamp": 94.67,
                "direction": "Straight"
            },
            {
                "timestamp": 94.7,
                "direction": "Straight"
            },
            {
                "timestamp": 94.74,
                "direction": "Straight"
            },
            {
                "timestamp": 94.77,
                "direction": "Straight"
            },
            {
                "timestamp": 94.8,
                "direction": "Straight"
            },
            {
                "timestamp": 94.84,
                "direction": "Straight"
            },
            {
                "timestamp": 94.87,
                "direction": "Straight"
            },
            {
                "timestamp": 94.9,
                "direction": "Straight"
            },
            {
                "timestamp": 94.94,
                "direction": "Straight"
            },
            {
                "timestamp": 94.97,
                "direction": "Straight"
            },
            {
                "timestamp": 95.0,
                "direction": "Straight"
            },
            {
                "timestamp": 95.04,
                "direction": "Straight"
            },
            {
                "timestamp": 95.07,
                "direction": "Straight"
            },
            {
                "timestamp": 95.1,
                "direction": "Straight"
            },
            {
                "timestamp": 95.14,
                "direction": "Straight"
            },
            {
                "timestamp": 95.17,
                "direction": "Straight"
            },
            {
                "timestamp": 95.2,
                "direction": "Straight"
            },
            {
                "timestamp": 95.24,
                "direction": "Straight"
            },
            {
                "timestamp": 95.27,
                "direction": "Straight"
            },
            {
                "timestamp": 95.31,
                "direction": "Straight"
            },
            {
                "timestamp": 95.34,
                "direction": "Straight"
            },
            {
                "timestamp": 95.37,
                "direction": "Straight"
            },
            {
                "timestamp": 95.41,
                "direction": "Straight"
            },
            {
                "timestamp": 95.44,
                "direction": "Straight"
            },
            {
                "timestamp": 95.47,
                "direction": "Straight"
            },
            {
                "timestamp": 95.51,
                "direction": "Straight"
            },
            {
                "timestamp": 95.54,
                "direction": "Straight"
            },
            {
                "timestamp": 95.57,
                "direction": "Straight"
            },
            {
                "timestamp": 95.61,
                "direction": "Straight"
            },
            {
                "timestamp": 95.64,
                "direction": "Straight"
            },
            {
                "timestamp": 95.67,
                "direction": "Straight"
            },
            {
                "timestamp": 95.71,
                "direction": "Straight"
            },
            {
                "timestamp": 95.74,
                "direction": "Slight Right"
            },
            {
                "timestamp": 95.77,
                "direction": "Slight Right"
            },
            {
                "timestamp": 95.81,
                "direction": "Slight Right"
            },
            {
                "timestamp": 95.84,
                "direction": "Slight Right"
            },
            {
                "timestamp": 95.87,
                "direction": "Slight Right"
            },
            {
                "timestamp": 95.91,
                "direction": "Slight Right"
            },
            {
                "timestamp": 95.94,
                "direction": "Straight"
            },
            {
                "timestamp": 95.97,
                "direction": "Straight"
            },
            {
                "timestamp": 96.01,
                "direction": "Straight"
            },
            {
                "timestamp": 96.04,
                "direction": "Straight"
            },
            {
                "timestamp": 96.07,
                "direction": "Straight"
            },
            {
                "timestamp": 96.11,
                "direction": "Straight"
            },
            {
                "timestamp": 96.14,
                "direction": "Straight"
            },
            {
                "timestamp": 96.17,
                "direction": "Straight"
            },
            {
                "timestamp": 96.21,
                "direction": "Straight"
            },
            {
                "timestamp": 96.24,
                "direction": "Straight"
            },
            {
                "timestamp": 96.27,
                "direction": "Straight"
            },
            {
                "timestamp": 96.31,
                "direction": "Straight"
            },
            {
                "timestamp": 96.34,
                "direction": "Straight"
            },
            {
                "timestamp": 96.37,
                "direction": "Straight"
            },
            {
                "timestamp": 96.41,
                "direction": "Straight"
            },
            {
                "timestamp": 96.44,
                "direction": "Straight"
            },
            {
                "timestamp": 96.47,
                "direction": "Straight"
            },
            {
                "timestamp": 96.51,
                "direction": "Straight"
            },
            {
                "timestamp": 96.54,
                "direction": "Straight"
            },
            {
                "timestamp": 96.57,
                "direction": "Straight"
            },
            {
                "timestamp": 96.61,
                "direction": "Straight"
            },
            {
                "timestamp": 96.64,
                "direction": "Straight"
            },
            {
                "timestamp": 96.67,
                "direction": "Straight"
            },
            {
                "timestamp": 96.71,
                "direction": "Straight"
            },
            {
                "timestamp": 96.74,
                "direction": "Straight"
            },
            {
                "timestamp": 96.77,
                "direction": "Straight"
            },
            {
                "timestamp": 96.81,
                "direction": "Straight"
            },
            {
                "timestamp": 96.84,
                "direction": "Straight"
            },
            {
                "timestamp": 96.87,
                "direction": "Straight"
            },
            {
                "timestamp": 96.91,
                "direction": "Straight"
            },
            {
                "timestamp": 96.94,
                "direction": "Straight"
            },
            {
                "timestamp": 96.97,
                "direction": "Straight"
            },
            {
                "timestamp": 97.01,
                "direction": "Straight"
            },
            {
                "timestamp": 97.04,
                "direction": "Straight"
            },
            {
                "timestamp": 97.07,
                "direction": "Straight"
            },
            {
                "timestamp": 97.11,
                "direction": "Straight"
            },
            {
                "timestamp": 97.14,
                "direction": "Straight"
            },
            {
                "timestamp": 97.17,
                "direction": "Straight"
            },
            {
                "timestamp": 97.21,
                "direction": "Straight"
            },
            {
                "timestamp": 97.24,
                "direction": "Straight"
            },
            {
                "timestamp": 97.27,
                "direction": "Straight"
            },
            {
                "timestamp": 97.31,
                "direction": "Straight"
            },
            {
                "timestamp": 97.34,
                "direction": "Straight"
            },
            {
                "timestamp": 97.37,
                "direction": "Straight"
            },
            {
                "timestamp": 97.41,
                "direction": "Straight"
            },
            {
                "timestamp": 97.44,
                "direction": "Straight"
            },
            {
                "timestamp": 97.47,
                "direction": "Straight"
            },
            {
                "timestamp": 97.51,
                "direction": "Straight"
            },
            {
                "timestamp": 97.54,
                "direction": "Slight Left"
            },
            {
                "timestamp": 97.57,
                "direction": "Slight Left"
            },
            {
                "timestamp": 97.61,
                "direction": "Slight Left"
            },
            {
                "timestamp": 97.64,
                "direction": "Slight Left"
            },
            {
                "timestamp": 97.67,
                "direction": "Straight"
            },
            {
                "timestamp": 97.71,
                "direction": "Straight"
            },
            {
                "timestamp": 97.74,
                "direction": "Straight"
            },
            {
                "timestamp": 97.77,
                "direction": "Straight"
            },
            {
                "timestamp": 97.81,
                "direction": "Straight"
            },
            {
                "timestamp": 97.84,
                "direction": "Straight"
            },
            {
                "timestamp": 97.87,
                "direction": "Straight"
            },
            {
                "timestamp": 97.91,
                "direction": "Straight"
            },
            {
                "timestamp": 97.94,
                "direction": "Straight"
            },
            {
                "timestamp": 97.97,
                "direction": "Straight"
            },
            {
                "timestamp": 98.01,
                "direction": "Straight"
            },
            {
                "timestamp": 98.04,
                "direction": "Straight"
            },
            {
                "timestamp": 98.07,
                "direction": "Straight"
            },
            {
                "timestamp": 98.11,
                "direction": "Straight"
            },
            {
                "timestamp": 98.14,
                "direction": "Straight"
            },
            {
                "timestamp": 98.17,
                "direction": "Straight"
            },
            {
                "timestamp": 98.21,
                "direction": "Straight"
            },
            {
                "timestamp": 98.24,
                "direction": "Straight"
            },
            {
                "timestamp": 98.27,
                "direction": "Straight"
            },
            {
                "timestamp": 98.31,
                "direction": "Straight"
            },
            {
                "timestamp": 98.34,
                "direction": "Straight"
            },
            {
                "timestamp": 98.37,
                "direction": "Straight"
            },
            {
                "timestamp": 98.41,
                "direction": "Straight"
            },
            {
                "timestamp": 98.44,
                "direction": "Straight"
            },
            {
                "timestamp": 98.47,
                "direction": "Straight"
            },
            {
                "timestamp": 98.51,
                "direction": "Straight"
            },
            {
                "timestamp": 98.54,
                "direction": "Straight"
            },
            {
                "timestamp": 98.57,
                "direction": "Straight"
            },
            {
                "timestamp": 98.61,
                "direction": "Straight"
            },
            {
                "timestamp": 98.64,
                "direction": "Slight Left"
            },
            {
                "timestamp": 98.67,
                "direction": "Slight Left"
            },
            {
                "timestamp": 98.71,
                "direction": "Slight Left"
            },
            {
                "timestamp": 98.74,
                "direction": "Slight Left"
            },
            {
                "timestamp": 98.77,
                "direction": "Slight Left"
            },
            {
                "timestamp": 98.81,
                "direction": "Straight"
            },
            {
                "timestamp": 98.84,
                "direction": "Straight"
            },
            {
                "timestamp": 98.87,
                "direction": "Straight"
            },
            {
                "timestamp": 98.91,
                "direction": "Straight"
            },
            {
                "timestamp": 98.94,
                "direction": "Straight"
            },
            {
                "timestamp": 98.97,
                "direction": "Straight"
            },
            {
                "timestamp": 99.01,
                "direction": "Straight"
            },
            {
                "timestamp": 99.04,
                "direction": "Straight"
            },
            {
                "timestamp": 99.07,
                "direction": "Straight"
            },
            {
                "timestamp": 99.11,
                "direction": "Straight"
            },
            {
                "timestamp": 99.14,
                "direction": "Straight"
            },
            {
                "timestamp": 99.17,
                "direction": "Straight"
            },
            {
                "timestamp": 99.21,
                "direction": "Straight"
            },
            {
                "timestamp": 99.24,
                "direction": "Straight"
            },
            {
                "timestamp": 99.27,
                "direction": "Straight"
            },
            {
                "timestamp": 99.31,
                "direction": "Straight"
            },
            {
                "timestamp": 99.34,
                "direction": "Slight Right"
            },
            {
                "timestamp": 99.37,
                "direction": "Slight Right"
            },
            {
                "timestamp": 99.41,
                "direction": "Slight Right"
            },
            {
                "timestamp": 99.44,
                "direction": "Straight"
            },
            {
                "timestamp": 99.47,
                "direction": "Straight"
            },
            {
                "timestamp": 99.51,
                "direction": "Straight"
            },
            {
                "timestamp": 99.54,
                "direction": "Straight"
            },
            {
                "timestamp": 99.57,
                "direction": "Straight"
            },
            {
                "timestamp": 99.61,
                "direction": "Straight"
            },
            {
                "timestamp": 99.64,
                "direction": "Straight"
            },
            {
                "timestamp": 99.67,
                "direction": "Straight"
            },
            {
                "timestamp": 99.71,
                "direction": "Straight"
            },
            {
                "timestamp": 99.74,
                "direction": "Straight"
            },
            {
                "timestamp": 99.78,
                "direction": "Straight"
            },
            {
                "timestamp": 99.81,
                "direction": "Straight"
            },
            {
                "timestamp": 99.84,
                "direction": "Straight"
            },
            {
                "timestamp": 99.88,
                "direction": "Straight"
            },
            {
                "timestamp": 99.91,
                "direction": "Straight"
            },
            {
                "timestamp": 99.94,
                "direction": "Straight"
            },
            {
                "timestamp": 99.98,
                "direction": "Straight"
            },
            {
                "timestamp": 100.01,
                "direction": "Straight"
            },
            {
                "timestamp": 100.04,
                "direction": "Straight"
            },
            {
                "timestamp": 100.08,
                "direction": "Straight"
            }
        ]
    },
    {
        "data": [
            {
                "timestamp": 100.14,
                "direction": "Straight"
            },
            {
                "timestamp": 100.18,
                "direction": "Straight"
            },
            {
                "timestamp": 100.21,
                "direction": "Straight"
            },
            {
                "timestamp": 100.24,
                "direction": "Straight"
            },
            {
                "timestamp": 100.28,
                "direction": "Straight"
            },
            {
                "timestamp": 100.31,
                "direction": "Straight"
            },
            {
                "timestamp": 100.34,
                "direction": "Straight"
            },
            {
                "timestamp": 100.38,
                "direction": "Straight"
            },
            {
                "timestamp": 100.41,
                "direction": "Straight"
            },
            {
                "timestamp": 100.44,
                "direction": "Straight"
            },
            {
                "timestamp": 100.48,
                "direction": "Straight"
            },
            {
                "timestamp": 100.51,
                "direction": "Straight"
            },
            {
                "timestamp": 100.54,
                "direction": "Slight Right"
            },
            {
                "timestamp": 100.58,
                "direction": "Slight Right"
            },
            {
                "timestamp": 100.61,
                "direction": "Slight Right"
            },
            {
                "timestamp": 100.64,
                "direction": "Straight"
            },
            {
                "timestamp": 100.68,
                "direction": "Straight"
            },
            {
                "timestamp": 100.71,
                "direction": "Straight"
            },
            {
                "timestamp": 100.74,
                "direction": "Straight"
            },
            {
                "timestamp": 100.78,
                "direction": "Straight"
            },
            {
                "timestamp": 100.81,
                "direction": "Straight"
            },
            {
                "timestamp": 100.84,
                "direction": "Straight"
            },
            {
                "timestamp": 100.88,
                "direction": "Straight"
            },
            {
                "timestamp": 100.91,
                "direction": "Straight"
            },
            {
                "timestamp": 100.94,
                "direction": "Straight"
            },
            {
                "timestamp": 100.98,
                "direction": "Straight"
            },
            {
                "timestamp": 101.01,
                "direction": "Straight"
            },
            {
                "timestamp": 101.04,
                "direction": "Straight"
            },
            {
                "timestamp": 101.08,
                "direction": "Straight"
            },
            {
                "timestamp": 101.11,
                "direction": "Straight"
            },
            {
                "timestamp": 101.14,
                "direction": "Straight"
            },
            {
                "timestamp": 101.18,
                "direction": "Straight"
            },
            {
                "timestamp": 101.21,
                "direction": "Straight"
            },
            {
                "timestamp": 101.24,
                "direction": "Straight"
            },
            {
                "timestamp": 101.28,
                "direction": "Straight"
            },
            {
                "timestamp": 101.31,
                "direction": "Straight"
            },
            {
                "timestamp": 101.34,
                "direction": "Straight"
            },
            {
                "timestamp": 101.38,
                "direction": "Straight"
            },
            {
                "timestamp": 101.41,
                "direction": "Straight"
            },
            {
                "timestamp": 101.44,
                "direction": "Straight"
            },
            {
                "timestamp": 101.48,
                "direction": "Straight"
            },
            {
                "timestamp": 101.51,
                "direction": "Straight"
            },
            {
                "timestamp": 101.54,
                "direction": "Straight"
            },
            {
                "timestamp": 101.58,
                "direction": "Straight"
            },
            {
                "timestamp": 101.61,
                "direction": "Straight"
            },
            {
                "timestamp": 101.64,
                "direction": "Straight"
            },
            {
                "timestamp": 101.68,
                "direction": "Straight"
            },
            {
                "timestamp": 101.71,
                "direction": "Straight"
            },
            {
                "timestamp": 101.74,
                "direction": "Slight Right"
            },
            {
                "timestamp": 101.78,
                "direction": "Slight Right"
            },
            {
                "timestamp": 101.81,
                "direction": "Straight"
            },
            {
                "timestamp": 101.84,
                "direction": "Straight"
            },
            {
                "timestamp": 101.88,
                "direction": "Straight"
            },
            {
                "timestamp": 101.91,
                "direction": "Straight"
            },
            {
                "timestamp": 101.94,
                "direction": "Straight"
            },
            {
                "timestamp": 101.98,
                "direction": "Straight"
            },
            {
                "timestamp": 102.01,
                "direction": "Straight"
            },
            {
                "timestamp": 102.04,
                "direction": "Straight"
            },
            {
                "timestamp": 102.08,
                "direction": "Straight"
            },
            {
                "timestamp": 102.11,
                "direction": "Straight"
            },
            {
                "timestamp": 102.14,
                "direction": "Straight"
            },
            {
                "timestamp": 102.18,
                "direction": "Straight"
            },
            {
                "timestamp": 102.21,
                "direction": "Straight"
            },
            {
                "timestamp": 102.24,
                "direction": "Straight"
            },
            {
                "timestamp": 102.28,
                "direction": "Straight"
            },
            {
                "timestamp": 102.31,
                "direction": "Straight"
            },
            {
                "timestamp": 102.34,
                "direction": "Straight"
            },
            {
                "timestamp": 102.38,
                "direction": "Straight"
            },
            {
                "timestamp": 102.41,
                "direction": "Straight"
            },
            {
                "timestamp": 102.44,
                "direction": "Straight"
            },
            {
                "timestamp": 102.48,
                "direction": "Straight"
            },
            {
                "timestamp": 102.51,
                "direction": "Straight"
            },
            {
                "timestamp": 102.54,
                "direction": "Straight"
            },
            {
                "timestamp": 102.58,
                "direction": "Straight"
            },
            {
                "timestamp": 102.61,
                "direction": "Straight"
            },
            {
                "timestamp": 102.64,
                "direction": "Straight"
            },
            {
                "timestamp": 102.68,
                "direction": "Straight"
            },
            {
                "timestamp": 102.71,
                "direction": "Straight"
            },
            {
                "timestamp": 102.74,
                "direction": "Straight"
            },
            {
                "timestamp": 102.78,
                "direction": "Straight"
            },
            {
                "timestamp": 102.81,
                "direction": "Straight"
            },
            {
                "timestamp": 102.84,
                "direction": "Straight"
            },
            {
                "timestamp": 102.88,
                "direction": "Straight"
            },
            {
                "timestamp": 102.91,
                "direction": "Straight"
            },
            {
                "timestamp": 102.94,
                "direction": "Straight"
            },
            {
                "timestamp": 102.98,
                "direction": "Straight"
            },
            {
                "timestamp": 103.01,
                "direction": "Straight"
            },
            {
                "timestamp": 103.04,
                "direction": "Straight"
            },
            {
                "timestamp": 103.08,
                "direction": "Straight"
            },
            {
                "timestamp": 103.11,
                "direction": "Straight"
            },
            {
                "timestamp": 103.14,
                "direction": "Straight"
            },
            {
                "timestamp": 103.18,
                "direction": "Straight"
            },
            {
                "timestamp": 103.21,
                "direction": "Straight"
            },
            {
                "timestamp": 103.24,
                "direction": "Straight"
            },
            {
                "timestamp": 103.28,
                "direction": "Straight"
            },
            {
                "timestamp": 103.31,
                "direction": "Straight"
            },
            {
                "timestamp": 103.34,
                "direction": "Straight"
            },
            {
                "timestamp": 103.38,
                "direction": "Straight"
            },
            {
                "timestamp": 103.41,
                "direction": "Straight"
            },
            {
                "timestamp": 103.44,
                "direction": "Slight Left"
            },
            {
                "timestamp": 103.48,
                "direction": "Slight Left"
            },
            {
                "timestamp": 103.51,
                "direction": "Slight Left"
            },
            {
                "timestamp": 103.54,
                "direction": "Slight Left"
            },
            {
                "timestamp": 103.58,
                "direction": "Slight Left"
            },
            {
                "timestamp": 103.61,
                "direction": "Slight Left"
            },
            {
                "timestamp": 103.64,
                "direction": "Straight"
            },
            {
                "timestamp": 103.68,
                "direction": "Straight"
            },
            {
                "timestamp": 103.71,
                "direction": "Straight"
            },
            {
                "timestamp": 103.74,
                "direction": "Straight"
            },
            {
                "timestamp": 103.78,
                "direction": "Straight"
            },
            {
                "timestamp": 103.81,
                "direction": "Straight"
            },
            {
                "timestamp": 103.84,
                "direction": "Straight"
            },
            {
                "timestamp": 103.88,
                "direction": "Straight"
            },
            {
                "timestamp": 103.91,
                "direction": "Straight"
            },
            {
                "timestamp": 103.94,
                "direction": "Straight"
            },
            {
                "timestamp": 103.98,
                "direction": "Straight"
            },
            {
                "timestamp": 104.01,
                "direction": "Straight"
            },
            {
                "timestamp": 104.04,
                "direction": "Straight"
            },
            {
                "timestamp": 104.08,
                "direction": "Straight"
            },
            {
                "timestamp": 104.11,
                "direction": "Straight"
            },
            {
                "timestamp": 104.15,
                "direction": "Straight"
            },
            {
                "timestamp": 104.18,
                "direction": "Straight"
            },
            {
                "timestamp": 104.21,
                "direction": "Straight"
            },
            {
                "timestamp": 104.25,
                "direction": "Straight"
            },
            {
                "timestamp": 104.28,
                "direction": "Straight"
            },
            {
                "timestamp": 104.31,
                "direction": "Straight"
            },
            {
                "timestamp": 104.35,
                "direction": "Straight"
            },
            {
                "timestamp": 104.38,
                "direction": "Straight"
            },
            {
                "timestamp": 104.41,
                "direction": "Straight"
            },
            {
                "timestamp": 104.45,
                "direction": "Straight"
            },
            {
                "timestamp": 104.48,
                "direction": "Straight"
            },
            {
                "timestamp": 104.51,
                "direction": "Straight"
            },
            {
                "timestamp": 104.55,
                "direction": "Straight"
            },
            {
                "timestamp": 104.58,
                "direction": "Straight"
            },
            {
                "timestamp": 104.61,
                "direction": "Straight"
            },
            {
                "timestamp": 104.65,
                "direction": "Straight"
            },
            {
                "timestamp": 104.68,
                "direction": "Straight"
            },
            {
                "timestamp": 104.71,
                "direction": "Straight"
            },
            {
                "timestamp": 104.75,
                "direction": "Straight"
            },
            {
                "timestamp": 104.78,
                "direction": "Straight"
            },
            {
                "timestamp": 104.81,
                "direction": "Straight"
            },
            {
                "timestamp": 104.85,
                "direction": "Straight"
            },
            {
                "timestamp": 104.88,
                "direction": "Straight"
            },
            {
                "timestamp": 104.91,
                "direction": "Straight"
            },
            {
                "timestamp": 104.95,
                "direction": "Straight"
            },
            {
                "timestamp": 104.98,
                "direction": "Straight"
            },
            {
                "timestamp": 105.01,
                "direction": "Straight"
            },
            {
                "timestamp": 105.05,
                "direction": "Straight"
            },
            {
                "timestamp": 105.08,
                "direction": "Straight"
            },
            {
                "timestamp": 105.11,
                "direction": "Straight"
            },
            {
                "timestamp": 105.15,
                "direction": "Straight"
            },
            {
                "timestamp": 105.18,
                "direction": "Straight"
            },
            {
                "timestamp": 105.21,
                "direction": "Straight"
            },
            {
                "timestamp": 105.25,
                "direction": "Straight"
            },
            {
                "timestamp": 105.28,
                "direction": "Straight"
            },
            {
                "timestamp": 105.31,
                "direction": "Straight"
            },
            {
                "timestamp": 105.35,
                "direction": "Straight"
            },
            {
                "timestamp": 105.38,
                "direction": "Straight"
            },
            {
                "timestamp": 105.41,
                "direction": "Straight"
            },
            {
                "timestamp": 105.45,
                "direction": "Straight"
            },
            {
                "timestamp": 105.48,
                "direction": "Straight"
            },
            {
                "timestamp": 105.51,
                "direction": "Straight"
            },
            {
                "timestamp": 105.55,
                "direction": "Straight"
            },
            {
                "timestamp": 105.58,
                "direction": "Straight"
            },
            {
                "timestamp": 105.61,
                "direction": "Straight"
            },
            {
                "timestamp": 105.65,
                "direction": "Straight"
            },
            {
                "timestamp": 105.68,
                "direction": "Straight"
            },
            {
                "timestamp": 105.71,
                "direction": "Straight"
            },
            {
                "timestamp": 105.75,
                "direction": "Straight"
            },
            {
                "timestamp": 105.78,
                "direction": "Straight"
            },
            {
                "timestamp": 105.81,
                "direction": "Straight"
            },
            {
                "timestamp": 105.85,
                "direction": "Slight Left"
            },
            {
                "timestamp": 105.88,
                "direction": "Straight"
            },
            {
                "timestamp": 105.91,
                "direction": "Slight Left"
            },
            {
                "timestamp": 105.95,
                "direction": "Straight"
            },
            {
                "timestamp": 105.98,
                "direction": "Straight"
            },
            {
                "timestamp": 106.01,
                "direction": "Straight"
            },
            {
                "timestamp": 106.05,
                "direction": "Straight"
            },
            {
                "timestamp": 106.08,
                "direction": "Straight"
            },
            {
                "timestamp": 106.11,
                "direction": "Straight"
            },
            {
                "timestamp": 106.15,
                "direction": "Straight"
            },
            {
                "timestamp": 106.18,
                "direction": "Straight"
            },
            {
                "timestamp": 106.21,
                "direction": "Straight"
            },
            {
                "timestamp": 106.25,
                "direction": "Straight"
            },
            {
                "timestamp": 106.28,
                "direction": "Straight"
            },
            {
                "timestamp": 106.31,
                "direction": "Straight"
            },
            {
                "timestamp": 106.35,
                "direction": "Straight"
            },
            {
                "timestamp": 106.38,
                "direction": "Straight"
            },
            {
                "timestamp": 106.41,
                "direction": "Straight"
            },
            {
                "timestamp": 106.45,
                "direction": "Straight"
            },
            {
                "timestamp": 106.48,
                "direction": "Straight"
            },
            {
                "timestamp": 106.51,
                "direction": "Slight Right"
            },
            {
                "timestamp": 106.55,
                "direction": "Slight Right"
            },
            {
                "timestamp": 106.58,
                "direction": "Straight"
            },
            {
                "timestamp": 106.61,
                "direction": "Straight"
            },
            {
                "timestamp": 106.65,
                "direction": "Straight"
            },
            {
                "timestamp": 106.68,
                "direction": "Straight"
            },
            {
                "timestamp": 106.71,
                "direction": "Straight"
            },
            {
                "timestamp": 106.75,
                "direction": "Straight"
            },
            {
                "timestamp": 106.78,
                "direction": "Straight"
            },
            {
                "timestamp": 106.81,
                "direction": "Straight"
            },
            {
                "timestamp": 106.85,
                "direction": "Straight"
            },
            {
                "timestamp": 106.88,
                "direction": "Straight"
            },
            {
                "timestamp": 106.91,
                "direction": "Straight"
            },
            {
                "timestamp": 106.95,
                "direction": "Straight"
            },
            {
                "timestamp": 106.98,
                "direction": "Straight"
            },
            {
                "timestamp": 107.01,
                "direction": "Straight"
            },
            {
                "timestamp": 107.05,
                "direction": "Straight"
            },
            {
                "timestamp": 107.08,
                "direction": "Straight"
            },
            {
                "timestamp": 107.11,
                "direction": "Straight"
            },
            {
                "timestamp": 107.15,
                "direction": "Straight"
            },
            {
                "timestamp": 107.18,
                "direction": "Straight"
            },
            {
                "timestamp": 107.21,
                "direction": "Straight"
            },
            {
                "timestamp": 107.25,
                "direction": "Straight"
            },
            {
                "timestamp": 107.28,
                "direction": "Straight"
            },
            {
                "timestamp": 107.31,
                "direction": "Straight"
            },
            {
                "timestamp": 107.35,
                "direction": "Straight"
            },
            {
                "timestamp": 107.38,
                "direction": "Straight"
            },
            {
                "timestamp": 107.41,
                "direction": "Straight"
            },
            {
                "timestamp": 107.45,
                "direction": "Straight"
            },
            {
                "timestamp": 107.48,
                "direction": "Straight"
            },
            {
                "timestamp": 107.51,
                "direction": "Straight"
            },
            {
                "timestamp": 107.55,
                "direction": "Straight"
            },
            {
                "timestamp": 107.58,
                "direction": "Straight"
            },
            {
                "timestamp": 107.61,
                "direction": "Straight"
            },
            {
                "timestamp": 107.65,
                "direction": "Slight Right"
            },
            {
                "timestamp": 107.68,
                "direction": "Slight Right"
            },
            {
                "timestamp": 107.71,
                "direction": "Slight Right"
            },
            {
                "timestamp": 107.75,
                "direction": "Slight Right"
            },
            {
                "timestamp": 107.78,
                "direction": "Straight"
            },
            {
                "timestamp": 107.81,
                "direction": "Straight"
            },
            {
                "timestamp": 107.85,
                "direction": "Straight"
            },
            {
                "timestamp": 107.88,
                "direction": "Straight"
            },
            {
                "timestamp": 107.91,
                "direction": "Straight"
            },
            {
                "timestamp": 107.95,
                "direction": "Straight"
            },
            {
                "timestamp": 107.98,
                "direction": "Straight"
            },
            {
                "timestamp": 108.01,
                "direction": "Straight"
            },
            {
                "timestamp": 108.05,
                "direction": "Straight"
            },
            {
                "timestamp": 108.08,
                "direction": "Straight"
            },
            {
                "timestamp": 108.11,
                "direction": "Straight"
            },
            {
                "timestamp": 108.15,
                "direction": "Straight"
            },
            {
                "timestamp": 108.18,
                "direction": "Straight"
            },
            {
                "timestamp": 108.21,
                "direction": "Straight"
            },
            {
                "timestamp": 108.25,
                "direction": "Straight"
            },
            {
                "timestamp": 108.28,
                "direction": "Straight"
            },
            {
                "timestamp": 108.31,
                "direction": "Straight"
            },
            {
                "timestamp": 108.35,
                "direction": "Straight"
            },
            {
                "timestamp": 108.38,
                "direction": "Straight"
            },
            {
                "timestamp": 108.41,
                "direction": "Straight"
            },
            {
                "timestamp": 108.45,
                "direction": "Straight"
            },
            {
                "timestamp": 108.48,
                "direction": "Straight"
            },
            {
                "timestamp": 108.51,
                "direction": "Straight"
            },
            {
                "timestamp": 108.55,
                "direction": "Straight"
            },
            {
                "timestamp": 108.58,
                "direction": "Straight"
            },
            {
                "timestamp": 108.62,
                "direction": "Straight"
            },
            {
                "timestamp": 108.65,
                "direction": "Straight"
            },
            {
                "timestamp": 108.68,
                "direction": "Straight"
            },
            {
                "timestamp": 108.72,
                "direction": "Straight"
            },
            {
                "timestamp": 108.75,
                "direction": "Straight"
            },
            {
                "timestamp": 108.78,
                "direction": "Straight"
            },
            {
                "timestamp": 108.82,
                "direction": "Straight"
            },
            {
                "timestamp": 108.85,
                "direction": "Straight"
            },
            {
                "timestamp": 108.88,
                "direction": "Slight Right"
            },
            {
                "timestamp": 108.92,
                "direction": "Slight Right"
            },
            {
                "timestamp": 108.95,
                "direction": "Straight"
            },
            {
                "timestamp": 108.98,
                "direction": "Straight"
            },
            {
                "timestamp": 109.02,
                "direction": "Straight"
            },
            {
                "timestamp": 109.05,
                "direction": "Straight"
            },
            {
                "timestamp": 109.08,
                "direction": "Straight"
            },
            {
                "timestamp": 109.12,
                "direction": "Straight"
            },
            {
                "timestamp": 109.15,
                "direction": "Straight"
            },
            {
                "timestamp": 109.18,
                "direction": "Straight"
            },
            {
                "timestamp": 109.22,
                "direction": "Straight"
            },
            {
                "timestamp": 109.25,
                "direction": "Straight"
            },
            {
                "timestamp": 109.28,
                "direction": "Straight"
            },
            {
                "timestamp": 109.32,
                "direction": "Straight"
            },
            {
                "timestamp": 109.35,
                "direction": "Straight"
            },
            {
                "timestamp": 109.38,
                "direction": "Straight"
            },
            {
                "timestamp": 109.42,
                "direction": "Straight"
            },
            {
                "timestamp": 109.45,
                "direction": "Straight"
            },
            {
                "timestamp": 109.48,
                "direction": "Straight"
            },
            {
                "timestamp": 109.52,
                "direction": "Straight"
            },
            {
                "timestamp": 109.55,
                "direction": "Straight"
            },
            {
                "timestamp": 109.58,
                "direction": "Straight"
            },
            {
                "timestamp": 109.62,
                "direction": "Straight"
            },
            {
                "timestamp": 109.65,
                "direction": "Straight"
            },
            {
                "timestamp": 109.68,
                "direction": "Straight"
            },
            {
                "timestamp": 109.72,
                "direction": "Straight"
            },
            {
                "timestamp": 109.75,
                "direction": "Straight"
            },
            {
                "timestamp": 109.78,
                "direction": "Straight"
            },
            {
                "timestamp": 109.82,
                "direction": "Straight"
            },
            {
                "timestamp": 109.85,
                "direction": "Straight"
            },
            {
                "timestamp": 109.88,
                "direction": "Straight"
            },
            {
                "timestamp": 109.92,
                "direction": "Straight"
            },
            {
                "timestamp": 109.95,
                "direction": "Straight"
            },
            {
                "timestamp": 109.98,
                "direction": "Straight"
            },
            {
                "timestamp": 110.02,
                "direction": "Slight Right"
            },
            {
                "timestamp": 110.05,
                "direction": "Slight Right"
            },
            {
                "timestamp": 110.08,
                "direction": "Slight Right"
            },
            {
                "timestamp": 110.12,
                "direction": "Slight Right"
            },
            {
                "timestamp": 110.15,
                "direction": "Slight Right"
            },
            {
                "timestamp": 110.18,
                "direction": "Slight Right"
            },
            {
                "timestamp": 110.22,
                "direction": "Straight"
            },
            {
                "timestamp": 110.25,
                "direction": "Straight"
            },
            {
                "timestamp": 110.28,
                "direction": "Straight"
            },
            {
                "timestamp": 110.32,
                "direction": "Straight"
            },
            {
                "timestamp": 110.35,
                "direction": "Straight"
            },
            {
                "timestamp": 110.38,
                "direction": "Straight"
            },
            {
                "timestamp": 110.42,
                "direction": "Straight"
            },
            {
                "timestamp": 110.45,
                "direction": "Straight"
            },
            {
                "timestamp": 110.48,
                "direction": "Straight"
            },
            {
                "timestamp": 110.52,
                "direction": "Straight"
            },
            {
                "timestamp": 110.55,
                "direction": "Straight"
            },
            {
                "timestamp": 110.58,
                "direction": "Straight"
            },
            {
                "timestamp": 110.62,
                "direction": "Straight"
            },
            {
                "timestamp": 110.65,
                "direction": "Straight"
            },
            {
                "timestamp": 110.68,
                "direction": "Straight"
            },
            {
                "timestamp": 110.72,
                "direction": "Straight"
            },
            {
                "timestamp": 110.75,
                "direction": "Straight"
            },
            {
                "timestamp": 110.78,
                "direction": "Straight"
            },
            {
                "timestamp": 110.82,
                "direction": "Straight"
            },
            {
                "timestamp": 110.85,
                "direction": "Straight"
            },
            {
                "timestamp": 110.88,
                "direction": "Straight"
            },
            {
                "timestamp": 110.92,
                "direction": "Straight"
            },
            {
                "timestamp": 110.95,
                "direction": "Straight"
            },
            {
                "timestamp": 110.98,
                "direction": "Straight"
            },
            {
                "timestamp": 111.02,
                "direction": "Straight"
            },
            {
                "timestamp": 111.05,
                "direction": "Straight"
            },
            {
                "timestamp": 111.08,
                "direction": "Straight"
            },
            {
                "timestamp": 111.12,
                "direction": "Straight"
            },
            {
                "timestamp": 111.15,
                "direction": "Straight"
            },
            {
                "timestamp": 111.18,
                "direction": "Straight"
            },
            {
                "timestamp": 111.22,
                "direction": "Straight"
            },
            {
                "timestamp": 111.25,
                "direction": "Straight"
            },
            {
                "timestamp": 111.28,
                "direction": "Straight"
            },
            {
                "timestamp": 111.32,
                "direction": "Straight"
            },
            {
                "timestamp": 111.35,
                "direction": "Straight"
            },
            {
                "timestamp": 111.38,
                "direction": "Straight"
            },
            {
                "timestamp": 111.42,
                "direction": "Straight"
            },
            {
                "timestamp": 111.45,
                "direction": "Straight"
            },
            {
                "timestamp": 111.48,
                "direction": "Straight"
            },
            {
                "timestamp": 111.52,
                "direction": "Straight"
            },
            {
                "timestamp": 111.55,
                "direction": "Straight"
            },
            {
                "timestamp": 111.58,
                "direction": "Straight"
            },
            {
                "timestamp": 111.62,
                "direction": "Straight"
            },
            {
                "timestamp": 111.65,
                "direction": "Straight"
            },
            {
                "timestamp": 111.68,
                "direction": "Straight"
            },
            {
                "timestamp": 111.72,
                "direction": "Straight"
            },
            {
                "timestamp": 111.75,
                "direction": "Straight"
            },
            {
                "timestamp": 111.78,
                "direction": "Slight Left"
            },
            {
                "timestamp": 111.82,
                "direction": "Slight Left"
            },
            {
                "timestamp": 111.85,
                "direction": "Slight Left"
            },
            {
                "timestamp": 111.88,
                "direction": "Straight"
            },
            {
                "timestamp": 111.92,
                "direction": "Straight"
            },
            {
                "timestamp": 111.95,
                "direction": "Slight Left"
            },
            {
                "timestamp": 111.98,
                "direction": "Straight"
            },
            {
                "timestamp": 112.02,
                "direction": "Straight"
            },
            {
                "timestamp": 112.05,
                "direction": "Straight"
            },
            {
                "timestamp": 112.08,
                "direction": "Straight"
            },
            {
                "timestamp": 112.12,
                "direction": "Straight"
            },
            {
                "timestamp": 112.15,
                "direction": "Straight"
            },
            {
                "timestamp": 112.18,
                "direction": "Straight"
            },
            {
                "timestamp": 112.22,
                "direction": "Straight"
            },
            {
                "timestamp": 112.25,
                "direction": "Straight"
            },
            {
                "timestamp": 112.28,
                "direction": "Straight"
            },
            {
                "timestamp": 112.32,
                "direction": "Straight"
            },
            {
                "timestamp": 112.35,
                "direction": "Straight"
            },
            {
                "timestamp": 112.38,
                "direction": "Straight"
            },
            {
                "timestamp": 112.42,
                "direction": "Straight"
            },
            {
                "timestamp": 112.45,
                "direction": "Straight"
            },
            {
                "timestamp": 112.48,
                "direction": "Straight"
            },
            {
                "timestamp": 112.52,
                "direction": "Straight"
            },
            {
                "timestamp": 112.55,
                "direction": "Straight"
            },
            {
                "timestamp": 112.58,
                "direction": "Straight"
            },
            {
                "timestamp": 112.62,
                "direction": "Straight"
            },
            {
                "timestamp": 112.65,
                "direction": "Straight"
            },
            {
                "timestamp": 112.68,
                "direction": "Straight"
            },
            {
                "timestamp": 112.72,
                "direction": "Straight"
            },
            {
                "timestamp": 112.75,
                "direction": "Straight"
            },
            {
                "timestamp": 112.78,
                "direction": "Straight"
            },
            {
                "timestamp": 112.82,
                "direction": "Straight"
            },
            {
                "timestamp": 112.85,
                "direction": "Slight Left"
            },
            {
                "timestamp": 112.88,
                "direction": "Slight Left"
            },
            {
                "timestamp": 112.92,
                "direction": "Slight Left"
            },
            {
                "timestamp": 112.95,
                "direction": "Slight Left"
            },
            {
                "timestamp": 112.99,
                "direction": "Slight Left"
            },
            {
                "timestamp": 113.02,
                "direction": "Slight Left"
            },
            {
                "timestamp": 113.05,
                "direction": "Slight Left"
            },
            {
                "timestamp": 113.09,
                "direction": "Slight Left"
            },
            {
                "timestamp": 113.12,
                "direction": "Slight Left"
            },
            {
                "timestamp": 113.15,
                "direction": "Slight Left"
            },
            {
                "timestamp": 113.19,
                "direction": "Slight Left"
            },
            {
                "timestamp": 113.22,
                "direction": "Slight Left"
            },
            {
                "timestamp": 113.25,
                "direction": "Straight"
            },
            {
                "timestamp": 113.29,
                "direction": "Straight"
            },
            {
                "timestamp": 113.32,
                "direction": "Straight"
            },
            {
                "timestamp": 113.35,
                "direction": "Straight"
            },
            {
                "timestamp": 113.39,
                "direction": "Straight"
            },
            {
                "timestamp": 113.42,
                "direction": "Straight"
            },
            {
                "timestamp": 113.45,
                "direction": "Straight"
            },
            {
                "timestamp": 113.49,
                "direction": "Straight"
            },
            {
                "timestamp": 113.52,
                "direction": "Straight"
            },
            {
                "timestamp": 113.55,
                "direction": "Straight"
            },
            {
                "timestamp": 113.59,
                "direction": "Straight"
            },
            {
                "timestamp": 113.62,
                "direction": "Straight"
            },
            {
                "timestamp": 113.65,
                "direction": "Straight"
            },
            {
                "timestamp": 113.69,
                "direction": "Straight"
            },
            {
                "timestamp": 113.72,
                "direction": "Straight"
            },
            {
                "timestamp": 113.75,
                "direction": "Straight"
            },
            {
                "timestamp": 113.79,
                "direction": "Straight"
            },
            {
                "timestamp": 113.82,
                "direction": "Straight"
            },
            {
                "timestamp": 113.85,
                "direction": "Straight"
            },
            {
                "timestamp": 113.89,
                "direction": "Straight"
            },
            {
                "timestamp": 113.92,
                "direction": "Straight"
            },
            {
                "timestamp": 113.95,
                "direction": "Slight Left"
            },
            {
                "timestamp": 113.99,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.02,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.05,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.09,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.12,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.15,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.19,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.22,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.25,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.29,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.32,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.35,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.39,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.42,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.45,
                "direction": "Slight Left"
            },
            {
                "timestamp": 114.49,
                "direction": "Straight"
            },
            {
                "timestamp": 114.52,
                "direction": "Straight"
            },
            {
                "timestamp": 114.55,
                "direction": "Straight"
            },
            {
                "timestamp": 114.59,
                "direction": "Straight"
            },
            {
                "timestamp": 114.62,
                "direction": "Straight"
            },
            {
                "timestamp": 114.65,
                "direction": "Straight"
            },
            {
                "timestamp": 114.69,
                "direction": "Straight"
            },
            {
                "timestamp": 114.72,
                "direction": "Straight"
            },
            {
                "timestamp": 114.75,
                "direction": "Straight"
            },
            {
                "timestamp": 114.79,
                "direction": "Straight"
            },
            {
                "timestamp": 114.82,
                "direction": "Straight"
            },
            {
                "timestamp": 114.85,
                "direction": "Straight"
            },
            {
                "timestamp": 114.89,
                "direction": "Straight"
            },
            {
                "timestamp": 114.92,
                "direction": "Straight"
            },
            {
                "timestamp": 114.95,
                "direction": "Straight"
            },
            {
                "timestamp": 114.99,
                "direction": "Straight"
            },
            {
                "timestamp": 115.02,
                "direction": "Straight"
            },
            {
                "timestamp": 115.05,
                "direction": "Straight"
            },
            {
                "timestamp": 115.09,
                "direction": "Straight"
            },
            {
                "timestamp": 115.12,
                "direction": "Straight"
            },
            {
                "timestamp": 115.15,
                "direction": "Straight"
            },
            {
                "timestamp": 115.19,
                "direction": "Straight"
            },
            {
                "timestamp": 115.22,
                "direction": "Straight"
            },
            {
                "timestamp": 115.25,
                "direction": "Straight"
            },
            {
                "timestamp": 115.29,
                "direction": "Straight"
            },
            {
                "timestamp": 115.32,
                "direction": "Slight Left"
            },
            {
                "timestamp": 115.35,
                "direction": "Slight Left"
            },
            {
                "timestamp": 115.39,
                "direction": "Slight Left"
            },
            {
                "timestamp": 115.42,
                "direction": "Slight Left"
            },
            {
                "timestamp": 115.45,
                "direction": "Slight Left"
            },
            {
                "timestamp": 115.49,
                "direction": "Slight Left"
            },
            {
                "timestamp": 115.52,
                "direction": "Slight Left"
            },
            {
                "timestamp": 115.55,
                "direction": "Slight Left"
            },
            {
                "timestamp": 115.59,
                "direction": "Slight Left"
            },
            {
                "timestamp": 115.62,
                "direction": "Slight Left"
            },
            {
                "timestamp": 115.65,
                "direction": "Straight"
            },
            {
                "timestamp": 115.69,
                "direction": "Straight"
            },
            {
                "timestamp": 115.72,
                "direction": "Straight"
            },
            {
                "timestamp": 115.75,
                "direction": "Straight"
            },
            {
                "timestamp": 115.79,
                "direction": "Straight"
            },
            {
                "timestamp": 115.82,
                "direction": "Straight"
            },
            {
                "timestamp": 115.85,
                "direction": "Straight"
            },
            {
                "timestamp": 115.89,
                "direction": "Straight"
            },
            {
                "timestamp": 115.92,
                "direction": "Straight"
            },
            {
                "timestamp": 115.95,
                "direction": "Straight"
            },
            {
                "timestamp": 115.99,
                "direction": "Straight"
            },
            {
                "timestamp": 116.02,
                "direction": "Straight"
            },
            {
                "timestamp": 116.05,
                "direction": "Straight"
            },
            {
                "timestamp": 116.09,
                "direction": "Straight"
            },
            {
                "timestamp": 116.12,
                "direction": "Straight"
            },
            {
                "timestamp": 116.15,
                "direction": "Straight"
            },
            {
                "timestamp": 116.19,
                "direction": "Straight"
            },
            {
                "timestamp": 116.22,
                "direction": "Straight"
            },
            {
                "timestamp": 116.25,
                "direction": "Straight"
            },
            {
                "timestamp": 116.29,
                "direction": "Straight"
            },
            {
                "timestamp": 116.32,
                "direction": "Straight"
            },
            {
                "timestamp": 116.35,
                "direction": "Straight"
            },
            {
                "timestamp": 116.39,
                "direction": "Straight"
            },
            {
                "timestamp": 116.42,
                "direction": "Straight"
            },
            {
                "timestamp": 116.45,
                "direction": "Slight Left"
            },
            {
                "timestamp": 116.49,
                "direction": "Slight Left"
            },
            {
                "timestamp": 116.52,
                "direction": "Straight"
            },
            {
                "timestamp": 116.55,
                "direction": "Straight"
            },
            {
                "timestamp": 116.59,
                "direction": "Slight Left"
            },
            {
                "timestamp": 116.62,
                "direction": "Straight"
            },
            {
                "timestamp": 116.65,
                "direction": "Straight"
            },
            {
                "timestamp": 116.69,
                "direction": "Straight"
            },
            {
                "timestamp": 116.72,
                "direction": "Straight"
            },
            {
                "timestamp": 116.75,
                "direction": "Straight"
            },
            {
                "timestamp": 116.79,
                "direction": "Straight"
            },
            {
                "timestamp": 116.82,
                "direction": "Straight"
            },
            {
                "timestamp": 116.85,
                "direction": "Straight"
            },
            {
                "timestamp": 116.89,
                "direction": "Straight"
            },
            {
                "timestamp": 116.92,
                "direction": "Straight"
            },
            {
                "timestamp": 116.95,
                "direction": "Straight"
            },
            {
                "timestamp": 116.99,
                "direction": "Straight"
            },
            {
                "timestamp": 117.02,
                "direction": "Straight"
            },
            {
                "timestamp": 117.05,
                "direction": "Straight"
            },
            {
                "timestamp": 117.09,
                "direction": "Straight"
            },
            {
                "timestamp": 117.12,
                "direction": "Straight"
            },
            {
                "timestamp": 117.15,
                "direction": "Straight"
            },
            {
                "timestamp": 117.19,
                "direction": "Straight"
            },
            {
                "timestamp": 117.22,
                "direction": "Straight"
            },
            {
                "timestamp": 117.25,
                "direction": "Slight Right"
            },
            {
                "timestamp": 117.29,
                "direction": "Straight"
            },
            {
                "timestamp": 117.32,
                "direction": "Straight"
            },
            {
                "timestamp": 117.35,
                "direction": "Straight"
            },
            {
                "timestamp": 117.39,
                "direction": "Straight"
            },
            {
                "timestamp": 117.42,
                "direction": "Straight"
            },
            {
                "timestamp": 117.46,
                "direction": "Straight"
            },
            {
                "timestamp": 117.49,
                "direction": "Straight"
            },
            {
                "timestamp": 117.52,
                "direction": "Straight"
            },
            {
                "timestamp": 117.56,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.59,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.62,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.66,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.69,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.72,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.76,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.79,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.82,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.86,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.89,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.92,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.96,
                "direction": "Slight Left"
            },
            {
                "timestamp": 117.99,
                "direction": "Straight"
            },
            {
                "timestamp": 118.02,
                "direction": "Straight"
            },
            {
                "timestamp": 118.06,
                "direction": "Straight"
            },
            {
                "timestamp": 118.09,
                "direction": "Straight"
            },
            {
                "timestamp": 118.12,
                "direction": "Straight"
            },
            {
                "timestamp": 118.16,
                "direction": "Straight"
            },
            {
                "timestamp": 118.19,
                "direction": "Straight"
            },
            {
                "timestamp": 118.22,
                "direction": "Straight"
            },
            {
                "timestamp": 118.26,
                "direction": "Straight"
            },
            {
                "timestamp": 118.29,
                "direction": "Straight"
            },
            {
                "timestamp": 118.32,
                "direction": "Straight"
            },
            {
                "timestamp": 118.36,
                "direction": "Straight"
            },
            {
                "timestamp": 118.39,
                "direction": "Straight"
            },
            {
                "timestamp": 118.42,
                "direction": "Straight"
            },
            {
                "timestamp": 118.46,
                "direction": "Straight"
            },
            {
                "timestamp": 118.49,
                "direction": "Straight"
            },
            {
                "timestamp": 118.52,
                "direction": "Straight"
            },
            {
                "timestamp": 118.56,
                "direction": "Straight"
            },
            {
                "timestamp": 118.59,
                "direction": "Straight"
            },
            {
                "timestamp": 118.62,
                "direction": "Straight"
            },
            {
                "timestamp": 118.66,
                "direction": "Straight"
            },
            {
                "timestamp": 118.69,
                "direction": "Straight"
            },
            {
                "timestamp": 118.72,
                "direction": "Straight"
            },
            {
                "timestamp": 118.76,
                "direction": "Straight"
            },
            {
                "timestamp": 118.79,
                "direction": "Straight"
            },
            {
                "timestamp": 118.82,
                "direction": "Straight"
            },
            {
                "timestamp": 118.86,
                "direction": "Straight"
            },
            {
                "timestamp": 118.89,
                "direction": "Straight"
            },
            {
                "timestamp": 118.92,
                "direction": "Straight"
            },
            {
                "timestamp": 118.96,
                "direction": "Straight"
            },
            {
                "timestamp": 118.99,
                "direction": "Straight"
            },
            {
                "timestamp": 119.02,
                "direction": "Straight"
            },
            {
                "timestamp": 119.06,
                "direction": "Straight"
            },
            {
                "timestamp": 119.09,
                "direction": "Straight"
            },
            {
                "timestamp": 119.12,
                "direction": "Straight"
            },
            {
                "timestamp": 119.16,
                "direction": "Straight"
            },
            {
                "timestamp": 119.19,
                "direction": "Straight"
            },
            {
                "timestamp": 119.22,
                "direction": "Straight"
            },
            {
                "timestamp": 119.26,
                "direction": "Straight"
            },
            {
                "timestamp": 119.29,
                "direction": "Straight"
            },
            {
                "timestamp": 119.32,
                "direction": "Straight"
            },
            {
                "timestamp": 119.36,
                "direction": "Straight"
            },
            {
                "timestamp": 119.39,
                "direction": "Straight"
            },
            {
                "timestamp": 119.42,
                "direction": "Straight"
            },
            {
                "timestamp": 119.46,
                "direction": "Straight"
            },
            {
                "timestamp": 119.49,
                "direction": "Straight"
            },
            {
                "timestamp": 119.52,
                "direction": "Straight"
            },
            {
                "timestamp": 119.56,
                "direction": "Straight"
            },
            {
                "timestamp": 119.59,
                "direction": "Slight Right"
            },
            {
                "timestamp": 119.62,
                "direction": "Slight Right"
            },
            {
                "timestamp": 119.66,
                "direction": "Slight Right"
            },
            {
                "timestamp": 119.69,
                "direction": "Slight Right"
            },
            {
                "timestamp": 119.72,
                "direction": "Slight Right"
            },
            {
                "timestamp": 119.76,
                "direction": "Straight"
            },
            {
                "timestamp": 119.79,
                "direction": "Straight"
            },
            {
                "timestamp": 119.82,
                "direction": "Straight"
            },
            {
                "timestamp": 119.86,
                "direction": "Straight"
            },
            {
                "timestamp": 119.89,
                "direction": "Straight"
            },
            {
                "timestamp": 119.92,
                "direction": "Straight"
            },
            {
                "timestamp": 119.96,
                "direction": "Straight"
            },
            {
                "timestamp": 119.99,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.02,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.06,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.09,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.12,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.16,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.19,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.22,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.26,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.29,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.32,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.36,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.39,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.42,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.46,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.49,
                "direction": "Slight Left"
            },
            {
                "timestamp": 120.52,
                "direction": "Straight"
            },
            {
                "timestamp": 120.56,
                "direction": "Straight"
            },
            {
                "timestamp": 120.59,
                "direction": "Straight"
            },
            {
                "timestamp": 120.62,
                "direction": "Straight"
            },
            {
                "timestamp": 120.66,
                "direction": "Straight"
            },
            {
                "timestamp": 120.69,
                "direction": "Straight"
            },
            {
                "timestamp": 120.72,
                "direction": "Straight"
            },
            {
                "timestamp": 120.76,
                "direction": "Straight"
            },
            {
                "timestamp": 120.79,
                "direction": "Straight"
            },
            {
                "timestamp": 120.82,
                "direction": "Straight"
            },
            {
                "timestamp": 120.86,
                "direction": "Straight"
            },
            {
                "timestamp": 120.89,
                "direction": "Straight"
            },
            {
                "timestamp": 120.92,
                "direction": "Straight"
            },
            {
                "timestamp": 120.96,
                "direction": "Straight"
            },
            {
                "timestamp": 120.99,
                "direction": "Straight"
            },
            {
                "timestamp": 121.02,
                "direction": "Slight Left"
            },
            {
                "timestamp": 121.06,
                "direction": "Slight Left"
            },
            {
                "timestamp": 121.09,
                "direction": "Slight Left"
            },
            {
                "timestamp": 121.12,
                "direction": "Slight Left"
            },
            {
                "timestamp": 121.16,
                "direction": "Slight Left"
            },
            {
                "timestamp": 121.19,
                "direction": "Left"
            },
            {
                "timestamp": 121.22,
                "direction": "Left"
            },
            {
                "timestamp": 121.26,
                "direction": "Left"
            },
            {
                "timestamp": 121.29,
                "direction": "Left"
            },
            {
                "timestamp": 121.32,
                "direction": "Left"
            },
            {
                "timestamp": 121.36,
                "direction": "Left"
            },
            {
                "timestamp": 121.39,
                "direction": "Left"
            },
            {
                "timestamp": 121.42,
                "direction": "Left"
            },
            {
                "timestamp": 121.46,
                "direction": "Left"
            },
            {
                "timestamp": 121.49,
                "direction": "Left"
            },
            {
                "timestamp": 121.52,
                "direction": "Slight Left"
            },
            {
                "timestamp": 121.56,
                "direction": "Slight Left"
            },
            {
                "timestamp": 121.59,
                "direction": "Slight Left"
            },
            {
                "timestamp": 121.62,
                "direction": "Slight Left"
            },
            {
                "timestamp": 121.66,
                "direction": "Slight Left"
            },
            {
                "timestamp": 121.69,
                "direction": "Slight Left"
            },
            {
                "timestamp": 121.72,
                "direction": "Straight"
            },
            {
                "timestamp": 121.76,
                "direction": "Straight"
            },
            {
                "timestamp": 121.79,
                "direction": "Straight"
            },
            {
                "timestamp": 121.82,
                "direction": "Straight"
            },
            {
                "timestamp": 121.86,
                "direction": "Straight"
            },
            {
                "timestamp": 121.89,
                "direction": "Straight"
            },
            {
                "timestamp": 121.93,
                "direction": "Straight"
            },
            {
                "timestamp": 121.96,
                "direction": "Straight"
            },
            {
                "timestamp": 121.99,
                "direction": "Straight"
            },
            {
                "timestamp": 122.03,
                "direction": "Straight"
            },
            {
                "timestamp": 122.06,
                "direction": "Straight"
            },
            {
                "timestamp": 122.09,
                "direction": "Straight"
            },
            {
                "timestamp": 122.13,
                "direction": "Straight"
            },
            {
                "timestamp": 122.16,
                "direction": "Straight"
            },
            {
                "timestamp": 122.19,
                "direction": "Straight"
            },
            {
                "timestamp": 122.23,
                "direction": "Straight"
            },
            {
                "timestamp": 122.26,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.29,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.33,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.36,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.39,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.43,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.46,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.49,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.53,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.56,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.59,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.63,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.66,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.69,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.73,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.76,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.79,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.83,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.86,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.89,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.93,
                "direction": "Slight Left"
            },
            {
                "timestamp": 122.96,
                "direction": "Straight"
            },
            {
                "timestamp": 122.99,
                "direction": "Straight"
            },
            {
                "timestamp": 123.03,
                "direction": "Straight"
            },
            {
                "timestamp": 123.06,
                "direction": "Straight"
            },
            {
                "timestamp": 123.09,
                "direction": "Straight"
            },
            {
                "timestamp": 123.13,
                "direction": "Straight"
            },
            {
                "timestamp": 123.16,
                "direction": "Straight"
            },
            {
                "timestamp": 123.19,
                "direction": "Straight"
            },
            {
                "timestamp": 123.23,
                "direction": "Straight"
            },
            {
                "timestamp": 123.26,
                "direction": "Straight"
            },
            {
                "timestamp": 123.29,
                "direction": "Straight"
            },
            {
                "timestamp": 123.33,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.36,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.39,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.43,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.46,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.49,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.53,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.56,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.59,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.63,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.66,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.69,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.73,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.76,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.79,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.83,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.86,
                "direction": "Slight Left"
            },
            {
                "timestamp": 123.89,
                "direction": "Straight"
            },
            {
                "timestamp": 123.93,
                "direction": "Straight"
            },
            {
                "timestamp": 123.96,
                "direction": "Straight"
            },
            {
                "timestamp": 123.99,
                "direction": "Straight"
            },
            {
                "timestamp": 124.03,
                "direction": "Straight"
            },
            {
                "timestamp": 124.06,
                "direction": "Straight"
            },
            {
                "timestamp": 124.09,
                "direction": "Straight"
            },
            {
                "timestamp": 124.13,
                "direction": "Straight"
            },
            {
                "timestamp": 124.16,
                "direction": "Straight"
            },
            {
                "timestamp": 124.19,
                "direction": "Straight"
            },
            {
                "timestamp": 124.23,
                "direction": "Straight"
            },
            {
                "timestamp": 124.26,
                "direction": "Straight"
            },
            {
                "timestamp": 124.29,
                "direction": "Straight"
            },
            {
                "timestamp": 124.33,
                "direction": "Straight"
            },
            {
                "timestamp": 124.36,
                "direction": "Straight"
            },
            {
                "timestamp": 124.39,
                "direction": "Straight"
            },
            {
                "timestamp": 124.43,
                "direction": "Straight"
            },
            {
                "timestamp": 124.46,
                "direction": "Straight"
            },
            {
                "timestamp": 124.49,
                "direction": "Straight"
            },
            {
                "timestamp": 124.53,
                "direction": "Straight"
            },
            {
                "timestamp": 124.56,
                "direction": "Straight"
            },
            {
                "timestamp": 124.59,
                "direction": "Straight"
            },
            {
                "timestamp": 124.63,
                "direction": "Straight"
            },
            {
                "timestamp": 124.66,
                "direction": "Straight"
            },
            {
                "timestamp": 124.69,
                "direction": "Straight"
            },
            {
                "timestamp": 124.73,
                "direction": "Straight"
            },
            {
                "timestamp": 124.76,
                "direction": "Straight"
            },
            {
                "timestamp": 124.79,
                "direction": "Straight"
            },
            {
                "timestamp": 124.83,
                "direction": "Straight"
            },
            {
                "timestamp": 124.86,
                "direction": "Straight"
            },
            {
                "timestamp": 124.89,
                "direction": "Straight"
            },
            {
                "timestamp": 124.93,
                "direction": "Straight"
            },
            {
                "timestamp": 124.96,
                "direction": "Straight"
            },
            {
                "timestamp": 124.99,
                "direction": "Straight"
            },
            {
                "timestamp": 125.03,
                "direction": "Straight"
            },
            {
                "timestamp": 125.06,
                "direction": "Straight"
            },
            {
                "timestamp": 125.09,
                "direction": "Straight"
            },
            {
                "timestamp": 125.13,
                "direction": "Straight"
            },
            {
                "timestamp": 125.16,
                "direction": "Straight"
            },
            {
                "timestamp": 125.19,
                "direction": "Straight"
            },
            {
                "timestamp": 125.23,
                "direction": "Straight"
            },
            {
                "timestamp": 125.26,
                "direction": "Straight"
            },
            {
                "timestamp": 125.29,
                "direction": "Straight"
            },
            {
                "timestamp": 125.33,
                "direction": "Straight"
            },
            {
                "timestamp": 125.36,
                "direction": "Slight Right"
            },
            {
                "timestamp": 125.39,
                "direction": "Slight Right"
            },
            {
                "timestamp": 125.43,
                "direction": "Slight Right"
            },
            {
                "timestamp": 125.46,
                "direction": "Slight Right"
            },
            {
                "timestamp": 125.49,
                "direction": "Slight Right"
            },
            {
                "timestamp": 125.53,
                "direction": "Straight"
            },
            {
                "timestamp": 125.56,
                "direction": "Straight"
            },
            {
                "timestamp": 125.59,
                "direction": "Straight"
            },
            {
                "timestamp": 125.63,
                "direction": "Straight"
            },
            {
                "timestamp": 125.66,
                "direction": "Straight"
            },
            {
                "timestamp": 125.69,
                "direction": "Straight"
            },
            {
                "timestamp": 125.73,
                "direction": "Straight"
            },
            {
                "timestamp": 125.76,
                "direction": "Straight"
            },
            {
                "timestamp": 125.79,
                "direction": "Straight"
            },
            {
                "timestamp": 125.83,
                "direction": "Straight"
            },
            {
                "timestamp": 125.86,
                "direction": "Straight"
            },
            {
                "timestamp": 125.89,
                "direction": "Straight"
            },
            {
                "timestamp": 125.93,
                "direction": "Straight"
            },
            {
                "timestamp": 125.96,
                "direction": "Straight"
            },
            {
                "timestamp": 125.99,
                "direction": "Straight"
            },
            {
                "timestamp": 126.03,
                "direction": "Straight"
            },
            {
                "timestamp": 126.06,
                "direction": "Slight Left"
            },
            {
                "timestamp": 126.09,
                "direction": "Straight"
            },
            {
                "timestamp": 126.13,
                "direction": "Straight"
            },
            {
                "timestamp": 126.16,
                "direction": "Straight"
            },
            {
                "timestamp": 126.19,
                "direction": "Straight"
            },
            {
                "timestamp": 126.23,
                "direction": "Straight"
            },
            {
                "timestamp": 126.26,
                "direction": "Straight"
            },
            {
                "timestamp": 126.3,
                "direction": "Straight"
            },
            {
                "timestamp": 126.33,
                "direction": "Straight"
            },
            {
                "timestamp": 126.36,
                "direction": "Straight"
            },
            {
                "timestamp": 126.4,
                "direction": "Straight"
            },
            {
                "timestamp": 126.43,
                "direction": "Straight"
            },
            {
                "timestamp": 126.46,
                "direction": "Straight"
            },
            {
                "timestamp": 126.5,
                "direction": "Straight"
            },
            {
                "timestamp": 126.53,
                "direction": "Straight"
            },
            {
                "timestamp": 126.56,
                "direction": "Straight"
            },
            {
                "timestamp": 126.6,
                "direction": "Straight"
            },
            {
                "timestamp": 126.63,
                "direction": "Straight"
            },
            {
                "timestamp": 126.66,
                "direction": "Straight"
            },
            {
                "timestamp": 126.7,
                "direction": "Straight"
            },
            {
                "timestamp": 126.73,
                "direction": "Straight"
            },
            {
                "timestamp": 126.76,
                "direction": "Straight"
            },
            {
                "timestamp": 126.8,
                "direction": "Straight"
            },
            {
                "timestamp": 126.83,
                "direction": "Straight"
            },
            {
                "timestamp": 126.86,
                "direction": "Straight"
            },
            {
                "timestamp": 126.9,
                "direction": "Straight"
            },
            {
                "timestamp": 126.93,
                "direction": "Straight"
            },
            {
                "timestamp": 126.96,
                "direction": "Straight"
            },
            {
                "timestamp": 127.0,
                "direction": "Straight"
            },
            {
                "timestamp": 127.03,
                "direction": "Straight"
            },
            {
                "timestamp": 127.06,
                "direction": "Straight"
            },
            {
                "timestamp": 127.1,
                "direction": "Straight"
            },
            {
                "timestamp": 127.13,
                "direction": "Straight"
            },
            {
                "timestamp": 127.16,
                "direction": "Straight"
            },
            {
                "timestamp": 127.2,
                "direction": "Straight"
            },
            {
                "timestamp": 127.23,
                "direction": "Straight"
            },
            {
                "timestamp": 127.26,
                "direction": "Straight"
            },
            {
                "timestamp": 127.3,
                "direction": "Straight"
            },
            {
                "timestamp": 127.33,
                "direction": "Straight"
            },
            {
                "timestamp": 127.36,
                "direction": "Straight"
            },
            {
                "timestamp": 127.4,
                "direction": "Straight"
            },
            {
                "timestamp": 127.43,
                "direction": "Straight"
            },
            {
                "timestamp": 127.46,
                "direction": "Straight"
            },
            {
                "timestamp": 127.5,
                "direction": "Straight"
            },
            {
                "timestamp": 127.53,
                "direction": "Straight"
            },
            {
                "timestamp": 127.56,
                "direction": "Straight"
            },
            {
                "timestamp": 127.6,
                "direction": "Straight"
            },
            {
                "timestamp": 127.63,
                "direction": "Straight"
            },
            {
                "timestamp": 127.66,
                "direction": "Straight"
            },
            {
                "timestamp": 127.7,
                "direction": "Straight"
            },
            {
                "timestamp": 127.73,
                "direction": "Straight"
            },
            {
                "timestamp": 127.76,
                "direction": "Straight"
            },
            {
                "timestamp": 127.8,
                "direction": "Straight"
            },
            {
                "timestamp": 127.83,
                "direction": "Straight"
            },
            {
                "timestamp": 127.86,
                "direction": "Straight"
            },
            {
                "timestamp": 127.9,
                "direction": "Straight"
            },
            {
                "timestamp": 127.93,
                "direction": "Straight"
            },
            {
                "timestamp": 127.96,
                "direction": "Straight"
            },
            {
                "timestamp": 128.0,
                "direction": "Straight"
            },
            {
                "timestamp": 128.03,
                "direction": "Straight"
            },
            {
                "timestamp": 128.06,
                "direction": "Straight"
            },
            {
                "timestamp": 128.1,
                "direction": "Straight"
            },
            {
                "timestamp": 128.13,
                "direction": "Straight"
            },
            {
                "timestamp": 128.16,
                "direction": "Straight"
            },
            {
                "timestamp": 128.2,
                "direction": "Straight"
            },
            {
                "timestamp": 128.23,
                "direction": "Straight"
            },
            {
                "timestamp": 128.26,
                "direction": "Straight"
            },
            {
                "timestamp": 128.3,
                "direction": "Straight"
            },
            {
                "timestamp": 128.33,
                "direction": "Straight"
            },
            {
                "timestamp": 128.36,
                "direction": "Straight"
            },
            {
                "timestamp": 128.4,
                "direction": "Straight"
            },
            {
                "timestamp": 128.43,
                "direction": "Straight"
            },
            {
                "timestamp": 128.46,
                "direction": "Straight"
            },
            {
                "timestamp": 128.5,
                "direction": "Straight"
            },
            {
                "timestamp": 128.53,
                "direction": "Straight"
            },
            {
                "timestamp": 128.56,
                "direction": "Straight"
            },
            {
                "timestamp": 128.6,
                "direction": "Straight"
            },
            {
                "timestamp": 128.63,
                "direction": "Straight"
            },
            {
                "timestamp": 128.66,
                "direction": "Straight"
            },
            {
                "timestamp": 128.7,
                "direction": "Straight"
            },
            {
                "timestamp": 128.73,
                "direction": "Straight"
            },
            {
                "timestamp": 128.76,
                "direction": "Straight"
            },
            {
                "timestamp": 128.8,
                "direction": "Straight"
            },
            {
                "timestamp": 128.83,
                "direction": "Straight"
            },
            {
                "timestamp": 128.86,
                "direction": "Straight"
            },
            {
                "timestamp": 128.9,
                "direction": "Straight"
            },
            {
                "timestamp": 128.93,
                "direction": "Straight"
            },
            {
                "timestamp": 128.96,
                "direction": "Straight"
            },
            {
                "timestamp": 129.0,
                "direction": "Straight"
            },
            {
                "timestamp": 129.03,
                "direction": "Straight"
            },
            {
                "timestamp": 129.06,
                "direction": "Straight"
            },
            {
                "timestamp": 129.1,
                "direction": "Straight"
            },
            {
                "timestamp": 129.13,
                "direction": "Straight"
            },
            {
                "timestamp": 129.16,
                "direction": "Straight"
            },
            {
                "timestamp": 129.2,
                "direction": "Straight"
            },
            {
                "timestamp": 129.23,
                "direction": "Straight"
            },
            {
                "timestamp": 129.26,
                "direction": "Straight"
            },
            {
                "timestamp": 129.3,
                "direction": "Straight"
            },
            {
                "timestamp": 129.33,
                "direction": "Straight"
            },
            {
                "timestamp": 129.36,
                "direction": "Straight"
            },
            {
                "timestamp": 129.4,
                "direction": "Straight"
            },
            {
                "timestamp": 129.43,
                "direction": "Straight"
            },
            {
                "timestamp": 129.46,
                "direction": "Straight"
            },
            {
                "timestamp": 129.5,
                "direction": "Straight"
            },
            {
                "timestamp": 129.53,
                "direction": "Straight"
            },
            {
                "timestamp": 129.56,
                "direction": "Straight"
            },
            {
                "timestamp": 129.6,
                "direction": "Straight"
            },
            {
                "timestamp": 129.63,
                "direction": "Straight"
            },
            {
                "timestamp": 129.66,
                "direction": "Straight"
            },
            {
                "timestamp": 129.7,
                "direction": "Straight"
            },
            {
                "timestamp": 129.73,
                "direction": "Straight"
            },
            {
                "timestamp": 129.76,
                "direction": "Straight"
            },
            {
                "timestamp": 129.8,
                "direction": "Straight"
            },
            {
                "timestamp": 129.83,
                "direction": "Slight Right"
            },
            {
                "timestamp": 129.86,
                "direction": "Slight Right"
            },
            {
                "timestamp": 129.9,
                "direction": "Slight Right"
            },
            {
                "timestamp": 129.93,
                "direction": "Slight Right"
            },
            {
                "timestamp": 129.96,
                "direction": "Slight Right"
            },
            {
                "timestamp": 130.0,
                "direction": "Slight Right"
            },
            {
                "timestamp": 130.03,
                "direction": "Slight Right"
            },
            {
                "timestamp": 130.06,
                "direction": "Slight Right"
            },
            {
                "timestamp": 130.1,
                "direction": "Slight Right"
            },
            {
                "timestamp": 130.13,
                "direction": "Slight Right"
            },
            {
                "timestamp": 130.16,
                "direction": "Slight Right"
            },
            {
                "timestamp": 130.2,
                "direction": "Straight"
            },
            {
                "timestamp": 130.23,
                "direction": "Straight"
            },
            {
                "timestamp": 130.26,
                "direction": "Straight"
            },
            {
                "timestamp": 130.3,
                "direction": "Straight"
            },
            {
                "timestamp": 130.33,
                "direction": "Straight"
            },
            {
                "timestamp": 130.36,
                "direction": "Straight"
            },
            {
                "timestamp": 130.4,
                "direction": "Straight"
            },
            {
                "timestamp": 130.43,
                "direction": "Straight"
            },
            {
                "timestamp": 130.46,
                "direction": "Straight"
            },
            {
                "timestamp": 130.5,
                "direction": "Straight"
            },
            {
                "timestamp": 130.53,
                "direction": "Straight"
            },
            {
                "timestamp": 130.56,
                "direction": "Straight"
            },
            {
                "timestamp": 130.6,
                "direction": "Straight"
            },
            {
                "timestamp": 130.63,
                "direction": "Straight"
            },
            {
                "timestamp": 130.66,
                "direction": "Straight"
            },
            {
                "timestamp": 130.7,
                "direction": "Straight"
            },
            {
                "timestamp": 130.73,
                "direction": "Straight"
            },
            {
                "timestamp": 130.77,
                "direction": "Straight"
            },
            {
                "timestamp": 130.8,
                "direction": "Straight"
            },
            {
                "timestamp": 130.83,
                "direction": "Straight"
            },
            {
                "timestamp": 130.87,
                "direction": "Straight"
            },
            {
                "timestamp": 130.9,
                "direction": "Slight Right"
            },
            {
                "timestamp": 130.93,
                "direction": "Slight Right"
            },
            {
                "timestamp": 130.97,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.0,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.03,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.07,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.1,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.13,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.17,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.2,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.23,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.27,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.3,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.33,
                "direction": "Slight Right"
            },
            {
                "timestamp": 131.37,
                "direction": "Straight"
            },
            {
                "timestamp": 131.4,
                "direction": "Straight"
            },
            {
                "timestamp": 131.43,
                "direction": "Straight"
            },
            {
                "timestamp": 131.47,
                "direction": "Straight"
            },
            {
                "timestamp": 131.5,
                "direction": "Straight"
            },
            {
                "timestamp": 131.53,
                "direction": "Straight"
            },
            {
                "timestamp": 131.57,
                "direction": "Straight"
            },
            {
                "timestamp": 131.6,
                "direction": "Straight"
            },
            {
                "timestamp": 131.63,
                "direction": "Straight"
            },
            {
                "timestamp": 131.67,
                "direction": "Straight"
            },
            {
                "timestamp": 131.7,
                "direction": "Straight"
            },
            {
                "timestamp": 131.73,
                "direction": "Straight"
            },
            {
                "timestamp": 131.77,
                "direction": "Straight"
            },
            {
                "timestamp": 131.8,
                "direction": "Straight"
            },
            {
                "timestamp": 131.83,
                "direction": "Straight"
            },
            {
                "timestamp": 131.87,
                "direction": "Straight"
            },
            {
                "timestamp": 131.9,
                "direction": "Straight"
            },
            {
                "timestamp": 131.93,
                "direction": "Straight"
            },
            {
                "timestamp": 131.97,
                "direction": "Straight"
            },
            {
                "timestamp": 132.0,
                "direction": "Straight"
            },
            {
                "timestamp": 132.03,
                "direction": "Straight"
            },
            {
                "timestamp": 132.07,
                "direction": "Straight"
            },
            {
                "timestamp": 132.1,
                "direction": "Straight"
            },
            {
                "timestamp": 132.13,
                "direction": "Straight"
            },
            {
                "timestamp": 132.17,
                "direction": "Straight"
            },
            {
                "timestamp": 132.2,
                "direction": "Straight"
            },
            {
                "timestamp": 132.23,
                "direction": "Straight"
            },
            {
                "timestamp": 132.27,
                "direction": "Straight"
            },
            {
                "timestamp": 132.3,
                "direction": "Slight Right"
            },
            {
                "timestamp": 132.33,
                "direction": "Slight Right"
            },
            {
                "timestamp": 132.37,
                "direction": "Slight Right"
            },
            {
                "timestamp": 132.4,
                "direction": "Slight Right"
            },
            {
                "timestamp": 132.43,
                "direction": "Slight Right"
            },
            {
                "timestamp": 132.47,
                "direction": "Straight"
            },
            {
                "timestamp": 132.5,
                "direction": "Straight"
            },
            {
                "timestamp": 132.53,
                "direction": "Straight"
            },
            {
                "timestamp": 132.57,
                "direction": "Straight"
            },
            {
                "timestamp": 132.6,
                "direction": "Straight"
            },
            {
                "timestamp": 132.63,
                "direction": "Straight"
            },
            {
                "timestamp": 132.67,
                "direction": "Straight"
            },
            {
                "timestamp": 132.7,
                "direction": "Straight"
            },
            {
                "timestamp": 132.73,
                "direction": "Straight"
            },
            {
                "timestamp": 132.77,
                "direction": "Straight"
            },
            {
                "timestamp": 132.8,
                "direction": "Straight"
            },
            {
                "timestamp": 132.83,
                "direction": "Straight"
            },
            {
                "timestamp": 132.87,
                "direction": "Straight"
            },
            {
                "timestamp": 132.9,
                "direction": "Straight"
            },
            {
                "timestamp": 132.93,
                "direction": "Straight"
            },
            {
                "timestamp": 132.97,
                "direction": "Straight"
            },
            {
                "timestamp": 133.0,
                "direction": "Straight"
            },
            {
                "timestamp": 133.03,
                "direction": "Straight"
            },
            {
                "timestamp": 133.07,
                "direction": "Straight"
            },
            {
                "timestamp": 133.1,
                "direction": "Straight"
            },
            {
                "timestamp": 133.13,
                "direction": "Straight"
            },
            {
                "timestamp": 133.17,
                "direction": "Straight"
            },
            {
                "timestamp": 133.2,
                "direction": "Straight"
            },
            {
                "timestamp": 133.23,
                "direction": "Straight"
            },
            {
                "timestamp": 133.27,
                "direction": "Straight"
            },
            {
                "timestamp": 133.3,
                "direction": "Straight"
            },
            {
                "timestamp": 133.33,
                "direction": "Straight"
            },
            {
                "timestamp": 133.37,
                "direction": "Straight"
            },
            {
                "timestamp": 133.4,
                "direction": "Straight"
            },
            {
                "timestamp": 133.43,
                "direction": "Straight"
            },
            {
                "timestamp": 133.47,
                "direction": "Straight"
            },
            {
                "timestamp": 133.5,
                "direction": "Straight"
            },
            {
                "timestamp": 133.53,
                "direction": "Straight"
            },
            {
                "timestamp": 133.57,
                "direction": "Straight"
            },
            {
                "timestamp": 133.6,
                "direction": "Straight"
            },
            {
                "timestamp": 133.63,
                "direction": "Straight"
            },
            {
                "timestamp": 133.67,
                "direction": "Straight"
            },
            {
                "timestamp": 133.7,
                "direction": "Straight"
            },
            {
                "timestamp": 133.73,
                "direction": "Straight"
            },
            {
                "timestamp": 133.77,
                "direction": "Straight"
            },
            {
                "timestamp": 133.8,
                "direction": "Straight"
            },
            {
                "timestamp": 133.83,
                "direction": "Straight"
            },
            {
                "timestamp": 133.87,
                "direction": "Straight"
            },
            {
                "timestamp": 133.9,
                "direction": "Straight"
            },
            {
                "timestamp": 133.93,
                "direction": "Straight"
            },
            {
                "timestamp": 133.97,
                "direction": "Straight"
            },
            {
                "timestamp": 134.0,
                "direction": "Straight"
            },
            {
                "timestamp": 134.03,
                "direction": "Straight"
            },
            {
                "timestamp": 134.07,
                "direction": "Straight"
            },
            {
                "timestamp": 134.1,
                "direction": "Straight"
            },
            {
                "timestamp": 134.13,
                "direction": "Slight Left"
            },
            {
                "timestamp": 134.17,
                "direction": "Slight Left"
            },
            {
                "timestamp": 134.2,
                "direction": "Straight"
            },
            {
                "timestamp": 134.23,
                "direction": "Straight"
            },
            {
                "timestamp": 134.27,
                "direction": "Straight"
            },
            {
                "timestamp": 134.3,
                "direction": "Straight"
            },
            {
                "timestamp": 134.33,
                "direction": "Straight"
            },
            {
                "timestamp": 134.37,
                "direction": "Straight"
            },
            {
                "timestamp": 134.4,
                "direction": "Straight"
            },
            {
                "timestamp": 134.43,
                "direction": "Straight"
            },
            {
                "timestamp": 134.47,
                "direction": "Straight"
            },
            {
                "timestamp": 134.5,
                "direction": "Straight"
            },
            {
                "timestamp": 134.53,
                "direction": "Straight"
            },
            {
                "timestamp": 134.57,
                "direction": "Straight"
            },
            {
                "timestamp": 134.6,
                "direction": "Straight"
            }
        ]
    },
    {
        "data": []
    }
]

threshold = 90
directionTypes = {
    'STRAIGHT': 'straight',
    'LEFT': 'left',
    'S_LEFT': 'slight left',
    'RIGHT': 'right',
    'S_RIGHT': 'slight right',
}

directionMessages = {
    'STRAIGHT': 'Go straight',
    'LEFT': 'Turn left',
    'S_LEFT': 'Turn slight left',
    'RIGHT': 'Turn right',
    'S_RIGHT': 'Turn slight right',
}


def get_verdict(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    direction_meta = {}
    for item in data:
        direction = item.get('direction', '').lower()
        direction_meta[direction] = direction_meta.get(direction, 0) + 1
    
    total = sum(direction_meta.values()) or 1
    direction_counts = sorted([
        {
            'direction': dir,
            'count': count,
            'percent': (count / total) * 100
        }
        for dir, count in direction_meta.items()
    ], key=lambda x: x['percent'], reverse=True)

    verdict = None
    if direction_counts:
        if len(direction_counts) > 2:
            if (
                (direction_counts[0]['direction'].lower() == directionTypes['LEFT'] and direction_counts[1]['direction'].lower() == directionTypes['S_LEFT']) or
                (direction_counts[1]['direction'].lower() == directionTypes['LEFT'] and direction_counts[0]['direction'].lower() == directionTypes['S_LEFT']) or
                (direction_counts[0]['direction'].lower() == directionTypes['RIGHT'] and direction_counts[1]['direction'].lower() == directionTypes['S_RIGHT']) or
                (direction_counts[1]['direction'].lower() == directionTypes['RIGHT'] and direction_counts[0]['direction'].lower() == directionTypes['S_RIGHT'])
            ):
                if (direction_counts[1]['percent'] + direction_counts[0]['percent']) >= threshold:
                    if directionTypes['LEFT'] in direction_counts[0]['direction'].lower():
                        verdict = directionTypes['S_LEFT']
                    elif directionTypes['RIGHT'] in direction_counts[0]['direction'].lower():
                        verdict = directionTypes['S_RIGHT']
            elif direction_counts[0]['percent'] >= threshold:
                verdict = direction_counts[0]['direction']
        else:
            if direction_counts[0]['percent'] >= threshold:
                verdict = direction_counts[0]['direction']

    time_gap = {
        'tStart': data[0]['timestamp'] if data else None,
        'tEnd': data[-1]['timestamp'] if data else None
    }

    return {'verdict': verdict, 'directionCounts': direction_counts, 'timeGap': time_gap}

def process_verdict(data: List[Dict[str, Any]], verdict_meta: Dict[str, Any]):
    if check_time_validity(data[0]['timestamp']):
        seconds = data[0]['timestamp']
        target_min = seconds // 60
        target_sec = seconds % 60
        return {
            'direction': verdict_meta.get('verdict'),
            'seconds': seconds,
            'format': f"{target_min} min {target_sec} sec",
        }
    else:
        return None

def format_seconds(seconds: int) -> str:
    target_min = seconds // 60
    target_sec = seconds % 60
    return f"{target_min} min {target_sec} sec"

def check_time_validity(time: int) -> bool:
    print(finalData)
    return not any(el['directionTime'] == time for el in finalData)


def get_chunks(xs: List[Any], size: int) -> List[List[Any]]:
    return [xs[i:i + size] for i in range(0, len(xs), size)]

def check_same_group(current_group_data: Dict[str, Any], data: Dict[str, Any]) -> bool:
    data_direction_is_left = directionTypes['LEFT'] in data['direction'].lower()
    same_direction = (
        directionTypes['LEFT'] in current_group_data['direction']
        if data_direction_is_left
        else directionTypes['RIGHT'] in current_group_data['direction']
    )
    if not same_direction:
        return False
    return data['seconds'] - current_group_data['seconds'] <= 2.5

def get_direction_mesage(direction):
    try:    
        message = ""
        if direction.lower() == directionTypes['STRAIGHT']:
            message = "Go straight"
        elif direction.lower() == directionTypes['LEFT']:
            message = "Turn left"
        elif direction.lower() == directionTypes['S_LEFT']:
            message = "Turn slight left"
        elif direction.lower() == directionTypes['RIGHT']:
            message = "Turn right"
        elif direction.lower() == directionTypes['S_RIGHT']:
            message = "Turn slight right"
        
        return message
    except Exception as e:
        print('Error in get_direction_mesage fn')

def process_sliding_window_output(data):
    try:
        current_group_lead = None
        group = []
        grouped_data = []
        final_data = []

        def clear():
            nonlocal current_group_lead, group
            current_group_lead = None
            group = []

        def make_new_group_lead(curr_data):
            nonlocal current_group_lead, group
            current_group_lead = {
                'direction': curr_data['direction'],
                'seconds': curr_data['seconds'],
            }
            group.append(current_group_lead)

        direction_data = [el for el in data if el['direction'] != directionTypes['STRAIGHT']]
        
        if len(direction_data) == 0 and len(data) > 0:
            # This will be the case when all the direction are straight
            final_data.append({
                'start': (data[0])['seconds'],
                'end': (data[-1])['seconds'],
                'direction': directionTypes['STRAIGHT'],
                'message': get_direction_mesage(directionTypes['STRAIGHT']),
                # 'startFormat': format_seconds(int(start)),
                # 'endFormat': format_seconds(int(end)),
            })
        else:
            if direction_data == None:
                direction_data = []

            for current in direction_data:
                if current_group_lead is None:
                    make_new_group_lead(current)
                    continue

                if check_same_group(current_group_lead, current):
                    group.append(current)
                else:
                    if group:
                        grouped_data.append(group)
                    clear()
                    make_new_group_lead(current)

            if group:
                grouped_data.append(group)
                clear()

            for group in grouped_data:
                start = group[0]['seconds']
                end = group[-1]['seconds'] + 1 if len(group) > 1 else start + 1
                final_data.append({
                    'start': int(start),
                    'end': int(end),
                    'direction': group[0]['direction'],
                    'message': get_direction_mesage(group[0]['direction']),
                    # 'startFormat': format_seconds(int(start)),
                    # 'endFormat': format_seconds(int(end)),
                })
            print('finall!!!!')
            print(final_data)
        return final_data
    except Exception as e:
        print('Error while processing sliding window output')
        print(e)
        return None



def fun(fps):
    try:
        data = []
        for item in master:
            if item != None and len(item) > 0:
                data.extend(item['data'])
        finalData = sliding_window(data, fps)
        outputData = process_sliding_window_output(finalData)
        print('done')
        return outputData
    except Exception as e:
        print('Error in slide mian')
        print(e)
        return None

def sliding_window(data, fps):
    try:
        chunks = get_chunks(data, int(fps * 1))
        final_data = []
        for chunk in chunks:
            verdict_meta = get_verdict(chunk)
            if verdict_meta.get('verdict'):
                pv = process_verdict(chunk, verdict_meta)
                # print('pv')
                # print(pv)
                if pv != None:
                    final_data.append(pv)
        return final_data
    except Exception as e:
        print('Error in sliding_window')
        print(e)
        
print(fun(30))