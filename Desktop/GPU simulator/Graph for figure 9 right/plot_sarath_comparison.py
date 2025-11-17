def plot_sarathi_comparison(histories: dict):
    """只绘制Sarathi不同b_sarathi值的未处理token总数随时间变化图像"""
    import matplotlib.pyplot as plt
    colors = ['blue', 'red', 'green', 'orange', 'purple']  # 增加更多颜色
    configs = list(histories.keys())
    plt.figure(figsize=(8, 6))
    
    # 未处理token总数比较
    for i, config in enumerate(configs):
        history = histories[config]
        color = colors[i % len(colors)]  # 使用模运算避免索引超出范围
        plt.plot(history['time'], history['unprocessed_total'], 
                 label=config, linewidth=2, color=color)
    plt.title('Total Unprocessed Tokens Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Unprocessed Token Count')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('sarathi_b_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    import json
    import os
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'sarathi_histories_poisson.json')
    with open(json_path, 'r') as f:
        sarathi_histories = json.load(f)
    plot_sarathi_comparison(sarathi_histories)