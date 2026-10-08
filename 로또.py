import tkinter as tk
from tkinter import messagebox
import random


class LottoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎰 로또 번호 생성기")
        self.root.geometry("450x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#f8f9fa")

        self.current_set_count = 0
        self.max_sets = 5

        self.create_widgets()

    def get_ball_colors(self, num):
        """로또 번호별 실제 공 색상 및 글자색 반환"""
        if 1 <= num <= 10:
            return "#fbc02d", "#1e293b"  # 노란색 (글자 어둡게)
        elif 11 <= num <= 20:
            return "#1976d2", "#ffffff"  # 파란색
        elif 21 <= num <= 30:
            return "#e53935", "#ffffff"  # 빨간색
        elif 31 <= num <= 40:
            return "#616161", "#ffffff"  # 회색
        else:
            return "#43a047", "#ffffff"  # 초록색 (41~45)

    def create_widgets(self):
        # 타이틀 레이블
        title_label = tk.Label(
            self.root,
            text="🎰 로또 번호 생성기",
            font=("Pretendard", 18, "bold"),
            bg="#f8f9fa",
            fg="#333333",
            pady=15
        )
        title_label.pack()

        # 버튼 프레임
        btn_frame = tk.Frame(self.root, bg="#f8f9fa")
        btn_frame.pack(pady=5)

        self.btn_generate = tk.Button(
            btn_frame,
            text="로또번호 생성",
            font=("Pretendard", 12, "bold"),
            bg="#4f46e5",
            fg="white",
            activebackground="#4338ca",
            activeforeground="white",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.generate_lotto
        )
        self.btn_generate.grid(row=0, column=0, padx=5)

        self.btn_reset = tk.Button(
            btn_frame,
            text="초기화",
            font=("Pretendard", 12, "bold"),
            bg="#e5e7eb",
            fg="#374151",
            activebackground="#d1d5db",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.reset_lotto
        )
        self.btn_reset.grid(row=0, column=1, padx=5)

        # 번호 출력 영역 프레임
        self.sets_frame = tk.Frame(self.root, bg="#f8f9fa", pady=15)
        self.sets_frame.pack(fill="both", expand=True, padx=20)

    def generate_lotto(self):
        if self.current_set_count >= self.max_sets:
            messagebox.showwarning("최대 개수 도달", "로또 번호는 최대 5세트까지만 생성할 수 있습니다.")
            return

        # 1~45 중복 없는 6개 숫자 무작위 추출 및 오름차순 정렬
        numbers = sorted(random.sample(range(1, 46), 6))
        self.current_set_count += 1

        # 한 세트를 표시할 행 프레임
        row_frame = tk.Frame(self.sets_frame, bg="#ffffff", highlightbackground="#e5e7eb", highlightthickness=1, pady=8,
                             padx=12)
        row_frame.pack(fill="x", pady=6)

        # 세트 번호 표시 (#1, #2, ...)
        label_set = tk.Label(
            row_frame,
            text=f"#{self.current_set_count}",
            font=("Pretendard", 11, "bold"),
            fg="#6b7280",
            bg="#ffffff",
            width=4
        )
        label_set.pack(side="left")

        # 공 프레임
        balls_frame = tk.Frame(row_frame, bg="#ffffff")
        balls_frame.pack(side="right", expand=True)

        for num in numbers:
            bg_color, fg_color = self.get_ball_colors(num)

            # 원형 모양 느낌을 위해 Canvas 사용
            canvas = tk.Canvas(balls_frame, width=38, height=38, bg="#ffffff", highlightthickness=0)
            canvas.pack(side="left", padx=3)

            # 원 그리기
            canvas.create_oval(2, 2, 36, 36, fill=bg_color, outline=bg_color)
            # 숫자 텍스트
            canvas.create_text(19, 19, text=str(num), fill=fg_color, font=("Pretendard", 11, "bold"))

        # 5세트에 도달하면 생성 버튼 비활성화
        if self.current_set_count >= self.max_sets:
            self.btn_generate.config(state="disabled", bg="#d1d5db", cursor="arrow")

    def reset_lotto(self):
        """생성된 번호 세트 초기화"""
        self.current_set_count = 0
        for widget in self.sets_frame.winfo_children():
            widget.destroy()

        self.btn_generate.config(state="normal", bg="#4f46e5", cursor="hand2")


if __name__ == "__main__":
    root = tk.Tk()
    app = LottoApp(root)
    root.mainloop()