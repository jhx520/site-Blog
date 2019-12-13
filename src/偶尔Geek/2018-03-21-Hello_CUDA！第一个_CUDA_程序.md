---
layout: post
cid: 99
title: Hello CUDA！第一个 CUDA 程序
slug: 99
date: 2018/03/21 22:27:00
updated: 2018/08/27 11:17:42
status: publish
author: 熊猫小A
categories: 
  - 偶尔Geek
tags: 
excerpt: 
---


最近要和 CUDA 打交道，作为笔记，就来一个 Hello World for CUDA 吧！

Compute Unified Device Architecture（CUDA）是英伟达为旗下图形硬件开发的一套并行计算平台，目前已经到 CUDA 9 了。这个平台提供了简洁易用的 API，可以让使用者以类 C 的语法来进行存储管理、进行计算任务。作为 CUDA 的 Hello World，这里就来讲解一个简单的 CUDA 程序：一维向量加，以及一个基本的 CUDA 程序需要包括哪些部分。

> 这里略过 CUDA 的配置过程。本文使用的环境是 CUDA 9.1 + VS2015

### 代码

首先先把代码扔上来：

```cpp
#include <iostream>
#include <device_launch_parameters.h>
#include <cuda_runtime.h>

using namespace std;

__global__ //这里是要在显卡上运行的代码，用 __global__ 来指明
void VecAdd(float *d_A, float *d_B, float *d_C) {
    int i = threadIdx.x;
    if (i<512) d_C[i] = d_A[i] + d_B[i];
}

__host__ //这里是在 CPU 上运行的代码，用 __host__ 来指明
int main() {
    float h_A[512], h_B[512], h_C[512];

    for (int i = 0; i < 512; i++) {
        h_A[i] = i;
        h_B[i] = 3;
    }

    float *d_A, *d_B, *d_C;

    //在显卡上分配内存
    cudaMalloc((void**)&d_A, sizeof(float) * 512); 
    cudaMalloc((void**)&d_B, sizeof(float) * 512);
    cudaMalloc((void**)&d_C, sizeof(float) * 512);

    //将内存中的数据拷贝到显卡上
    cudaMemcpy(d_A, h_A, sizeof(h_A), cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, sizeof(h_B), cudaMemcpyHostToDevice);

    //这俩参数用来决定线程的组织方式，看下文
    dim3 DimGrid(1, 1, 1);
    dim3 DimBlock(512, 1, 1);

    //在显卡上执行代码
    VecAdd <<<DimGrid, DimBlock >>>(d_A, d_B, d_C);

    //将运算结果从显卡拷贝回来
    cudaMemcpy(h_C, d_C, sizeof(h_C), cudaMemcpyDeviceToHost);

    for (int i = 0; i < 512; i++) {
        cout << h_C[i] << ' ';
    }

    //释放显存
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    return 0;
}
```

### 简单解析

像上面一个最简单的 CUDA 程序总结起来可以有以下几个部分

**宿主机代码**

所谓宿主机代码（host code），可理解为执行在 CPU 上的代码。这部分代码分为几块的话大概是下面这样：

* 在 CPU 上分配内存，确定需要处理的数据
* 在显卡上分配内存
* 将内存中的数据拷贝到显卡上
* 决定线程组织方式
* 执行 kernel 代码（Device 代码）
* 将结果拷贝回 CPU
* 释放显存


大部分都没什么可说的，重点在「决定线程组织方式」上。可以这么说：显卡之所以适用于并行计算，正是因为它允许同一时刻有极大量的线程在执行。the trick is，记住让每个线程*进行同样的任务，只是处理不同的数据*。对一个一维向量加，有 C[i]=A[i]+B[i]，也就是说，每个线程都做加法，但是由 i 来决定要操作的两个数（A[i]与B[i]）以及结果的存放位置（C[i]）。这样一来，一个 512 维的向量加，让 512 个线程来执行就好啦。

所谓的 i 来决定处理不同的数据，在 CUDA 中也就是告诉显卡每个线程要操作什么数据。这与 CUDA 中线程的组织方式很有关系。线程是多线程处理的最小单位，将线程以一维或者二维或者三维组织起来就称为一个「block」，再将 block 以一维或者二维组织起来则成为一个「grid」，一个 grid 也就是一个「kernel」。宿主机代码调用的即是 kernel。看上面代码中的这几行：

```cpp
//这俩参数用来决定线程的组织方式，看下文
dim3 DimGrid(1, 1, 1);
dim3 DimBlock(512, 1, 1);
```

可见用 dim3 的类型声明了两个变量 `DimGrid` 、`DimBlock` ，其中以 `1,1,1` 的方式组织 grid，也就是说，这个 gird 中包含一个 block（x、y、z 方向上都是 1）。以`512,1,1` 的方式组织 block 中的 thread，也就是说这个 block 中包含 512 个 thread 排成一行（x 方向上是 512，y、z 方向上都是 1）。

决定线程组织方式时要注意能够覆盖所有的待处理数据，在这里向量长 512 ，因此总的线程数不能低于 512。注意，由于 grid 只能以一维或者二维组织，因此 DimGrid 第三个参数总是 1。决定了线程的组织方式后就需要调用 kernel 代码执行真正的操作。

**Device 代码**

```cpp
//在显卡上执行代码
VecAdd <<<DimGrid, DimBlock >>>(d_A, d_B, d_C);
```

这行代码调用了执行在显卡上的函数 `VecAdd`，带上了三个指针以及 `DimGrid` 和 `DimBlock` 。于是显卡便根据此分配线程。于是在每个线程上将执行以下代码：

```cpp
int i = threadIdx.x;
if (i<512) d_C[i] = d_A[i] + d_B[i];
```

首先通过`threadIdx.x` 决定 i，这里的 i 将介于 0 至 511 之间。也就是说，i 号线程执行的操作是：`d_C[i] = d_A[i] + d_B[i];` 。这个简单的程序就是这样。在这个例子里只用到了 `threadIdx` ，因为线程组织方式是一维的。对更复杂的线程组织方式，可能需要更多的参数，例如 `blockIdx`。

记住，the trick is：**记住让每个线程进行同样的任务，只是处理不同的数据** 。如何实现这一点？每个线程有不同的线程 id，通过不同的线程 id 即可达成不同的线程执行一样的代码，但是处理不同的数据。

### 其他

以上是我的个人理解，而且我也刚开始学，可能有很多不准确的地方。关于 GPU 中的存储管理的部分我略过了，因为我其实并不那么明白……