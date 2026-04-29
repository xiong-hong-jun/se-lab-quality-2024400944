"""
实验8重构后代码 - 消除坏味道
重构手法：提取方法、消除重复、移除未使用变量、缩短函数
"""

def _validate_and_filter_scores(scores):
    """
    验证并过滤有效分数（提取出的公共方法）
    返回：有效分数列表
    """
    if not scores or not isinstance(scores, list):
        return []
    
    valid_scores = []
    for score in scores:
        if isinstance(score, (int, float)) and 0 <= score <= 100:
            valid_scores.append(score)
    
    return valid_scores


def _calculate_average(valid_scores):
    """
    计算平均值（提取出的公共方法）
    返回：平均值，若无有效分数则返回0
    """
    if not valid_scores:
        return 0
    return sum(valid_scores) / len(valid_scores)


def _print_calculation_details(scores, valid_scores, average, title="计算结果"):
    """
    打印计算详情（提取出的打印方法）
    """
    print(f"=== {title} ===")
    print(f"原始分数: {scores}")
    print(f"有效分数个数: {len(valid_scores)}")
    print(f"总分: {sum(valid_scores)}")
    print(f"平均分: {average:.2f}")
    

def calculate_average_score(scores):
    """
    计算平均分（重构后的简洁版本）
    """
    valid_scores = _validate_and_filter_scores(scores)
    average = _calculate_average(valid_scores)
    
    _print_calculation_details(scores, valid_scores, average, "平均分计算")
    
    return average


def calculate_weighted_score(scores, weight):
    """
    计算加权得分（重构后的简洁版本）
    """
    valid_scores = _validate_and_filter_scores(scores)
    average = _calculate_average(valid_scores)
    weighted_score = average * weight
    
    _print_calculation_details(scores, valid_scores, average, "加权平均分计算")
    print(f"权重: {weight}")
    print(f"加权得分: {weighted_score:.2f}")
    print("=== 计算结束 ===\n")
    
    return weighted_score


def process_scores():
    """
    处理多个班级的成绩
    """
    classes_data = {
        'A': [85, 92, 78, 90, 88],
        'B': [75, 82, 95, 68, 79, 100],
        'C': [88, 91]
    }
    
    results = {}
    for class_name, scores in classes_data.items():
        avg = calculate_average_score(scores)
        results[f'class_{class_name.lower()}'] = avg
        print(f"班级{class_name}平均分: {avg:.2f}\n")
    
    return results


if __name__ == "__main__":
    process_scores()
