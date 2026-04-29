"""
实验8示例代码 - 包含多种代码坏味道
"""

# 坏味道1: 重复代码（两个几乎相同的函数）
# 坏味道2: 过长函数
# 坏味道3: 未使用的变量

def calculate_student_score_v1(scores):
    """计算学生成绩 - 版本1"""
    # 未使用的变量
    unused_var = 100
    
    # 重复的验证逻辑
    if not scores:
        return 0
    if not isinstance(scores, list):
        return 0
    
    total = 0
    count = 0
    
    # 重复的过滤和计算逻辑
    for score in scores:
        if isinstance(score, (int, float)):
            if score >= 0 and score <= 100:
                total += score
                count += 1
    
    if count == 0:
        return 0
    
    average = total / count
    
    # 打印调试信息（过长函数的体现）
    print("=== 开始计算平均分 ===")
    print("原始分数:", scores)
    print("有效分数个数:", count)
    print("总分:", total)
    print("平均分:", average)
    print("=== 计算结束 ===")
    
    return average


def calculate_student_score_v2(scores, weight):
    """计算学生成绩 - 版本2（与v1大量重复）"""
    # 与v1完全相同的验证逻辑（重复代码）
    if not scores:
        return 0
    if not isinstance(scores, list):
        return 0
    
    total = 0
    count = 0
    
    # 与v1完全相同的过滤和累加逻辑（重复代码）
    for score in scores:
        if isinstance(score, (int, float)):
            if score >= 0 and score <= 100:
                total += score
                count += 1
    
    if count == 0:
        return 0
    
    average = total / count
    
    # 额外添加加权计算
    weighted_score = average * weight
    
    # 重复的打印逻辑（重复代码）
    print("=== 开始计算加权平均分 ===")
    print("原始分数:", scores)
    print("有效分数个数:", count)
    print("总分:", total)
    print("平均分:", average)
    print("权重:", weight)
    print("加权得分:", weighted_score)
    print("=== 计算结束 ===")
    
    return weighted_score


def process_scores():
    """处理多个班级的成绩（包含更多坏味道）"""
    class_a = [85, 92, 78, 90, 88]
    class_b = [75, 82, 95, 68, 79, 100]
    class_c = [88, 91]
    
    # 重复调用，本可统一处理
    avg_a = calculate_student_score_v1(class_a)
    avg_b = calculate_student_score_v1(class_b)
    avg_c = calculate_student_score_v1(class_c)
    
    # 重复的打印格式
    print("班级A平均分: " + str(avg_a))
    print("班级B平均分: " + str(avg_b))
    print("班级C平均分: " + str(avg_c))
    
    # 未使用的变量
    unused_result = avg_a + avg_b + avg_c
    
    return {
        'class_a': avg_a,
        'class_b': avg_b,
        'class_c': avg_c
    }


if __name__ == "__main__":
    process_scores()
