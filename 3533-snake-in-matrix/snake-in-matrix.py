class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        
        current_pos = 0

        for command in commands:
            if command == "UP":
                current_pos -= n
            elif command == "RIGHT":
                current_pos += 1
            elif command == "LEFT":
                current_pos -= 1
            elif command == "DOWN":
                current_pos += n

        return current_pos