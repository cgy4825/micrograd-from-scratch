# micrograd-from-scratch

跟着 Andrej Karpathy 的课程，从零手写一个自动微分引擎。
不复制粘贴，全部自己敲。

## 进度

- [ ] 里程碑 1：Value 类 + 反向传播（能算出 `c = a*b; c.backward()` 后 `a.grad == 3.0`）
- [ ] 里程碑 2：补齐算子（+ - * / tanh exp relu pow）
- [ ] 里程碑 3：Neuron / Layer / MLP
- [ ] 里程碑 4：损失函数 + 梯度下降，loss 收敛
- [ ] 里程碑 5：二维分类可视化

## 为什么要手写

自动微分是 PyTorch 的心脏。手写过一遍，之后读 PyTorch 和 vLLM 的源码就不会怕。
