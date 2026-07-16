#!/usr/bin/env python3
"""Reproduce Fig. 9: robustness and baseline comparison.

This script reads:
- results/fig9_poisoning_defense.csv
- results/fig9_telemetry_degradation.csv
- results/table13_baseline_comparison.csv

and writes:
- figures/fig9_robustness_comparison.png
- figures/fig9_robustness_comparison.pdf

No caption is embedded in the image.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"


def make_fig9() -> None:
    FIGURES.mkdir(exist_ok=True, parents=True)

    poison = pd.read_csv(RESULTS / "fig9_poisoning_defense.csv")
    telem = pd.read_csv(RESULTS / "fig9_telemetry_degradation.csv")
    baseline = pd.read_csv(RESULTS / "table13_baseline_comparison.csv")

    colors = {
        "blue": "#5D7FA6",
        "green": "#6FA878",
        "orange": "#D98A52",
        "purple": "#8E62A6",
        "grid": "#D0D0D0",
    }

    fig = plt.figure(figsize=(9.4, 6.1), dpi=300)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.45], hspace=0.50, wspace=0.36)

    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[0, 1])
    ax_c = fig.add_subplot(gs[1, :])

    # Panel A
    groups = ["20% poison", "40% poison"]
    methods = ["No defense", "Influence-ceiling + trust-decay"]
    x = np.arange(len(groups))
    width = 0.36
    method_colors = [colors["blue"], colors["green"]]

    for i, method in enumerate(methods):
        vals, errs = [], []
        for g in groups:
            row = poison[(poison["poison_rate"] == g) & (poison["method"] == method)].iloc[0]
            vals.append(float(row["risk_score"]))
            errs.append(float(row["error"]))
        bars = ax_a.bar(x + (i - 0.5) * width, vals, width,
                        yerr=errs, capsize=3, label=method,
                        color=method_colors[i], edgecolor="black", linewidth=0.3)
        for bar in bars:
            value = bar.get_height()
            ax_a.text(bar.get_x() + bar.get_width()/2, value + 0.018,
                      f"{value:.2f}", va="bottom", ha="center", fontsize=8)

    ax_a.set_title("(A) Poisoning Defense", loc="left", fontsize=11, fontweight="bold")
    ax_a.set_ylabel("Decoy-module risk score")
    ax_a.set_xticks(x)
    ax_a.set_xticklabels(groups)
    ax_a.set_ylim(0, 1.15)
    ax_a.set_yticks([0.0, 0.25, 0.50, 0.75, 1.00])
    ax_a.grid(axis="y", color=colors["grid"], linewidth=0.6, alpha=0.8)
    ax_a.set_axisbelow(True)
    ax_a.legend(frameon=True, fontsize=8, loc="upper right", bbox_to_anchor=(1.0, 1.12))
    ax_a.spines["top"].set_visible(False)
    ax_a.spines["right"].set_visible(False)

    # Panel B
    conditions = ["Clean", "30% loss", "30% duplication", "30% delay"]
    labels = ["Clean", "30%\nloss", "30%\ndup.", "30%\ndelay"]
    vals = [float(telem[telem["condition"] == c]["normalized_evidence_yield"].iloc[0])
            for c in conditions]
    xb = np.arange(len(conditions))
    bars = ax_b.bar(xb, vals, color=colors["blue"], edgecolor="black", linewidth=0.3)
    for bar in bars:
        value = bar.get_height()
        ax_b.text(bar.get_x() + bar.get_width()/2, value + 0.02,
                  f"{value:.2f}", va="bottom", ha="center", fontsize=8)
    ax_b.axhline(1.0, color="#8C8C8C", linewidth=0.8, linestyle="--")
    ax_b.text(-0.42, 1.08, "clean baseline = 1.0", fontsize=8, ha="left", va="bottom")
    ax_b.set_title("(B) Telemetry Degradation", loc="left", fontsize=11, fontweight="bold")
    ax_b.set_ylabel("Normalized evidence yield")
    ax_b.set_xticks(xb)
    ax_b.set_xticklabels(labels)
    ax_b.set_ylim(0, 1.5)
    ax_b.set_yticks([0.0, 0.5, 1.0, 1.5])
    ax_b.grid(axis="y", color=colors["grid"], linewidth=0.6, alpha=0.8)
    ax_b.set_axisbelow(True)
    ax_b.spines["top"].set_visible(False)
    ax_b.spines["right"].set_visible(False)

    # Panel C
    metrics = ["precision", "recall", "specificity", "f1"]
    metric_labels = ["Precision", "Recall", "Specificity", "F1"]
    metric_colors = [colors["blue"], colors["orange"], colors["green"], colors["purple"]]

    methods_order = [
        "RMS-Loop CRM/PTS",
        "Manual review",
        "Static-analysis only",
        "Fuzzing only",
        "Test-passing harness",
        "Sanitizer (detection only)",
    ]
    baseline = baseline.set_index("method").loc[methods_order].reset_index()

    y = np.arange(len(methods_order))
    h = 0.16
    offsets = [-1.5*h, -0.5*h, 0.5*h, 1.5*h]

    for metric, label, color, offset in zip(metrics, metric_labels, metric_colors, offsets):
        vals = baseline[metric].astype(float).values
        bars = ax_c.barh(y + offset, vals, height=h, color=color,
                         edgecolor="black", linewidth=0.25, label=label)
        for j, bar in enumerate(bars):
            value = bar.get_width()
            dy = 0.0
            if j == 0:
                dy = {"precision": -0.012, "recall": 0.004,
                      "specificity": 0.012, "f1": -0.004}[metric]
            ax_c.text(value + 0.006, bar.get_y() + bar.get_height()/2 + dy,
                      f"{value:.3f}", va="center", ha="left", fontsize=7)

    ax_c.set_title("(C) Baseline Comparison", loc="left", fontsize=11, fontweight="bold")
    ax_c.set_xlabel("Metric score")
    ax_c.set_yticks(y)
    ax_c.set_yticklabels(methods_order)
    ax_c.invert_yaxis()
    ax_c.set_xlim(0, 1.05)
    ax_c.set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax_c.grid(axis="x", color=colors["grid"], linewidth=0.6, alpha=0.8)
    ax_c.set_axisbelow(True)
    ax_c.legend(ncol=4, frameon=False, loc="lower center",
                bbox_to_anchor=(0.5, 1.03), fontsize=8)
    ax_c.spines["top"].set_visible(False)
    ax_c.spines["right"].set_visible(False)

    fig.subplots_adjust(left=0.11, right=0.985, top=0.94, bottom=0.10)
    fig.savefig(FIGURES / "fig9_robustness_comparison.png", dpi=600)
    fig.savefig(FIGURES / "fig9_robustness_comparison.pdf")
    plt.close(fig)


if __name__ == "__main__":
    make_fig9()
    print("Wrote figures/fig9_robustness_comparison.png and .pdf")
