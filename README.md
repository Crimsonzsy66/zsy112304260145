# 机器学习实验：基于 TF-IDF/Word2Vec 的情感预测

> 🎯 实验课程：机器学习
> 👤 学生姓名：周思言
> 📚 学号：112304260145
> 🏫 班级：数据1231
> 📅 实验日期：2026-05-17

---

## 一、项目简介

本项目是机器学习课程的情感分析实验，使用 **TF-IDF** 和 **Word2Vec** 两种特征提取方法，结合多种分类模型，完成 Kaggle 竞赛 "Bag of Words Meets Bags of Popcorn" 的情感预测任务。

**GitHub 仓库**: https://github.com/Crimsonzsy66/zsy112304260145

---

## 二、项目结构

```
baomihua/
├─ code/                     # 📝 实验代码
│  └─ experiment_word2vec_auc.py
│
├─ report/                   # 📊 实验报告
│  └─ experiment_report.md
│
├─ results/                  # 📈 实验结果
│  ├─ 实验结果报告.md
│  └─ 实验进度记录.md
│
├─ data/                     # 📂 数据集
│  ├─ labeledTrainData.tsv/  # 训练数据 (25,000条)
│  ├─ unlabeledTrainData.tsv/ # 无标签数据 (50,000条)
│  └─ testData.tsv/          # 测试数据 (25,000条)
│
├─ submission/              # 📤 提交文件
│  └─ submission_*.csv
│
├─ logs/                    # 📝 实验日志
│  └─ attempt_log.csv
│
├─ images/                  # 🖼️ 结果截图
│  └─ kaggle.png
│
├─ README.md                # 📖 项目说明
├─ requirements.txt         # Python依赖
└─ run_optimized.py         # 🚀 运行脚本
```

---

## 三、快速开始

### 环境配置

```bash
# 安装依赖
pip install -r requirements.txt
```

### 运行实验

```bash
# 运行优化后的脚本
python run_optimized.py

# 或手动指定参数
cd code
python experiment_word2vec_auc.py \
    --feature tfidf \
    --classifier linear_svc \
    --lr-c 0.5 \
    --ngram-min 1 \
    --ngram-max 4 \
    --max-features 100000
```

---

## 四、实验结果

### 最佳模型配置

| 项目 | 配置 |
|------|------|
| **特征提取** | TF-IDF (1-4 gram, 100k features) |
| **分类模型** | LinearSVC (C=0.5) |
| **交叉验证** | 5折 StratifiedKFold |
| **CV AUC** | **0.968351** |
| **标准差** | 0.001872 |

### 各折得分

| Fold | ROC-AUC |
|------|---------|
| 1 | 0.966052 |
| 2 | 0.966530 |
| 3 | 0.970862 |
| 4 | 0.968342 |
| 5 | 0.969970 |
| **平均** | **0.968351** |

### Kaggle 提交

- **Public Score**: 0.96753
- **提交日期**: 2026-05-17
- **提交文件**: `submission/submission_2026-05-17T21-25-00.176412_linear_svc_c0.5_tfidf_ngram1_4_max100000.csv`

---

## 五、实验方法

### 5.1 文本预处理

```python
# 保留否定词（关键优化点）
NEGATION_WORDS = {"no", "not", "nor", "never", "none", "n't"}
STOP_WORDS = set(ENGLISH_STOP_WORDS) - NEGATION_WORDS
```

### 5.2 特征提取

#### TF-IDF 特征
```python
TfidfVectorizer(
    ngram_range=(1, 4),      # 1-4元语法
    max_features=100000,      # 最大特征数
    min_df=2,                 # 最小文档频率
    max_df=0.95,              # 最大文档频率
    sublinear_tf=True,        # TF对数归一化
)
```

#### Word2Vec 特征（备用）
```python
Word2Vec(
    vector_size=300,
    window=10,
    min_count=40,
    sg=1,
    hs=1,
)
```

### 5.3 分类模型

测试了以下模型：
- **Logistic Regression** - CV AUC: 0.963
- **LinearSVC** - CV AUC: 0.968 ✓ 最佳
- **Random Forest**

---

## 六、关键发现

### 6.1 保留否定词的重要性

```python
# 否定词对情感分析至关重要
"not good"  → 情感为负
"good"      → 情感为正
```

### 6.2 N-gram 的作用

| N-gram | 示例 | 作用 |
|--------|------|------|
| 1-gram | good, bad | 基础词汇 |
| 2-gram | not good, very bad | 否定和程度 |
| 3-gram | not very good | 复杂修饰 |
| 4-gram | not very good at | 更细粒度 |

### 6.3 TF-IDF vs Word2Vec

- **TF-IDF AUC**: 0.96835 ✓
- **Word2Vec AUC**: ~0.95

原因：TF-IDF的N-gram能更好地捕获短语模式

---

## 七、GitHub 使用指南

### 7.1 提交规范

```bash
# 查看状态
git status

# 添加文件
git add -A

# 提交（信息要清晰）
git commit -m "feat: 完成TF-IDF特征提取

- 添加TF-IDF实现
- 保留否定词优化
- CV AUC达到0.968"

# 推送到GitHub
git push origin main
```

### 7.2 版本管理

```bash
# 查看历史
git log --oneline

# 恢复之前版本
git checkout <commit-hash>
```

### 7.3 注意事项

✅ **应该做的**:
- 每次实验后及时提交
- 提交信息要清晰
- 保留实验过程和结果

⛔ **不应该做的**:
- 不上传敏感信息（密码、Token）
- 不上传过大文件
- 不覆盖之前的好结果

---

## 八、实验记录

### 实验时间线

| 日期 | 实验内容 | 结果 |
|------|---------|------|
| 2026-04-15 | LogisticRegression + TF-IDF | AUC: 0.963 |
| 2026-04-15 | LinearSVC + TF-IDF | AUC: 0.968 ✓ |
| 2026-05-17 | 代码优化 | AUC: 0.968 ✓ |

### 优化过程

1. **特征优化**: N-gram (1,3) → (1,4), 特征数 50k → 100k
2. **模型优化**: LogisticRegression → LinearSVC
3. **参数优化**: C=1.0 → C=0.5
4. **预处理优化**: 保留否定词

---

## 九、实验心得

### 技术收获

1. ✅ 掌握了文本预处理技术
2. ✅ 学会了 TF-IDF 和 Word2Vec 特征提取
3. ✅ 理解了分类模型的原理和应用
4. ✅ 学会了交叉验证和模型评估
5. ✅ 掌握了 GitHub 版本管理

### 后续改进

1. 尝试更多 N-gram 范围 (1-5)
2. 集成学习：结合 TF-IDF 和 Word2Vec
3. 尝试其他模型：XGBoost、LightGBM

---

## 十、参考资料

- [Kaggle 竞赛页面](https://www.kaggle.com/competitions/word2vec-nlp-tutorial)
- [scikit-learn 文档](https://scikit-learn.org/)
- [Gensim Word2Vec](https://radimrehurek.com/gensim/models/word2vec.html)

---

## 十一、联系信息

- **GitHub**: https://github.com/Crimsonzsy66/zsy112304260145
- **学生**: 周思言
- **学号**: 112304260145

---

*实验完成日期: 2026-05-17*
*最后更新: 2026-05-17*
