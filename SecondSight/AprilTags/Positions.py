"""
________________________________________
|                                       |
|5                                     4|
|                                       |
|                origin                 |
|6                                     3|
|7   [|]b charge|        |r charge[|]  2|
|8                                     1|
|_______________________________________|

[|] denotes an autonomous entrance

y
|
|
|
|
z------x

      90
       |
       |
       |
180---yaw---0
       |
       |
       |
      270

up_down:z
distance:y
left_right:x

positions
*all units are CM and degrees
"""

# page 4:
# https://firstfrc.blob.core.windows.net/frc2023/FieldAssets/2023LayoutMarkingDiagram.pdf


# apriltagNumber:[x,y,z,roll]
apriltagPositions = {
    "2023": {
        '1': [610.77 * 25.4, 42.19 * 25.4, 18.22 * 25.4, 180],
        '2': [610.77 * 25.4, 108.19 * 25.4, 18.22 * 25.4, 180],
        '3': [610.77 * 25.4, 174.19 * 25.4, 18.22 * 25.4, 180],
        '4': [636.96 * 25.4, 265.74 * 25.4, 27.38 * 25.4, 180],
        '5': [14.25 * 25.4, 265.74 * 25.4, 27.38 * 25.4, 0],
        '6': [40.45 * 25.4, 174.19 * 25.4, 18.22 * 25.4, 0],
        '7': [40.45 * 25.4, 108.19 * 25.4, 18.22 * 25.4, 0],
        '8': [40.45 * 25.4, 42.19 * 25.4, 18.22 * 25.4, 0],
    }
}
