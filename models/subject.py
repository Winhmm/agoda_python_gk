# models/subject.py

from utils.validation import validate


class Subject:
    def __init__(self, name, score_40, score_60):
        self.name = name
        # Validate điểm ngay khi khởi tạo
        self.score_40 = validate.validateScore(score_40)
        self.score_60 = validate.validateScore(score_60)

    @property
    def final_score(self):
        score = (self.score_40 * 0.4) + (self.score_60 * 0.6)
        return round(score, 1)

    def to_dict(self):
        # Chuyển object thành Dictionary để sau này lưu vào JSON
        return {
            "name": self.name,
            "score_40": self.score_40,
            "score_60": self.score_60,
            "final_score": self.final_score,
        }

    @classmethod
    def from_dict(cls, data):
        # Tạo object Subject từ Dictionary (khi đọc từ JSON)
        return cls(data["name"], data["score_40"], data["score_60"])

    def __str__(self):
        return f"{self.name}: 40%({self.score_40}) | 60%({self.score_60}) -> Tổng: {self.final_score}"
