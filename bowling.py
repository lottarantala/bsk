from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []
    
    def add_frame(self, frame: Frame) -> None:
        if len(self.frames) >= 10:
            raise BowlingError
        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i >= len(self.frames):
            raise BowlingError
        return self.frames[i]

    def calculate_score(self) -> int:
        score = 0
        isSpare = False
        isStrike = False
        for frame in self.frames:
            if isStrike:
                score = score + frame.get_first_throw() + frame.get_second_throw()
                isStrike = False
            if isSpare:
                score = score + frame.get_first_throw()
                isSpare = False
            if frame.is_spare():
                isSpare = True
            if frame.is_strike():
                isStrike = True
            score += frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
