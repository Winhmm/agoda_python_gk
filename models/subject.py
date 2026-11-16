from utils.validation import Validator


class Subject:
    # Môn học gồm 2 điểm thành phần: 40% và 60%.

    def __init__(self, name, score_40, score_60):
        # Tạo môn học, kiểm tra điểm hợp lệ ngay khi tạo.
        self.name = name
        self.score_40 = Validator.validate_score(score_40)
        self.score_60 = Validator.validate_score(score_60)

    @property
    def final_score(self):
        # Điểm môn = 40% x 0.4 + 60% x 0.6, lấy 1 chữ số thập phân.
        score = self.score_40 * 0.4 + self.score_60 * 0.6
        return Validator.round_half_up(score, 1)

    def to_dict(self):
        # Chuyển Subject thành dictionary để lưu JSON.
        return {
            "name": self.name,
            "score_40": self.score_40,
            "score_60": self.score_60,
            "final_score": self.final_score,
        }

    @classmethod
    def from_dict(cls, data):
        # Tạo Subject từ dictionary đọc từ JSON.
        return cls(data["name"], data["score_40"], data["score_60"])
