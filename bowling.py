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
        for i, frame in enumerate(self.frames):
            if frame.is_spare():
                frame.set_bonus(self.frames[i+1].get_first_throw())
            if frame.is_strike():
                if self.frames[i+1].is_strike():
                    frame.set_bonus(self.frames[i+1].get_first_throw() + self.frames[i+1].get_second_throw() + self.frames[i+2].get_first_throw())
                else:
                    frame.set_bonus(self.frames[i+1].get_first_throw() + self.frames[i+1].get_second_throw())
            score += frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
