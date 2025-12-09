"use client";

import { motion } from "framer-motion";
import { Gauge, Cpu } from "lucide-react";

interface MetricsCardProps {
  title: string;
  value: number;
  max?: number;
  subtitle?: string;
  accent?: string;
  icon?: React.ReactNode;
}

export function MetricsCard({
  title,
  value,
  max = 100,
  subtitle,
  accent = "text-emerald-400",
  icon,
}: MetricsCardProps) {
  const percentage = Math.min(100, Math.max(0, (value / max) * 100));
  const circumference = 2 * Math.PI * 32;
  const offset = circumference - (percentage / 100) * circumference;

  return (
    <div className="relative overflow-hidden rounded-2xl border border-emerald-500/30 bg-white/5 p-5 backdrop-blur-lg shadow-lg shadow-emerald-500/10">
      <div className="absolute inset-0 bg-gradient-to-br from-emerald-500/10 via-transparent to-emerald-500/5 pointer-events-none" />
      <div className="relative flex items-center gap-4">
        <div className="relative flex h-20 w-20 items-center justify-center">
          <svg className="h-20 w-20 -rotate-90" viewBox="0 0 80 80">
            <circle
              cx="40"
              cy="40"
              r="32"
              className="stroke-white/10"
              strokeWidth="8"
              fill="none"
            />
            <motion.circle
              cx="40"
              cy="40"
              r="32"
              stroke="url(#emeraldGradient)"
              strokeWidth="8"
              strokeLinecap="round"
              fill="none"
              strokeDasharray={circumference}
              strokeDashoffset={offset}
              initial={{ strokeDashoffset: circumference }}
              animate={{ strokeDashoffset: offset }}
              transition={{ duration: 1, ease: "easeOut" }}
            />
            <defs>
              <linearGradient id="emeraldGradient" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0%" stopColor="#34d399" />
                <stop offset="100%" stopColor="#10b981" />
              </linearGradient>
            </defs>
          </svg>
          <div className="absolute inset-0 flex items-center justify-center">
            <span className={`text-lg font-semibold ${accent}`}>{percentage.toFixed(0)}%</span>
          </div>
        </div>
        <div className="flex flex-1 flex-col gap-1 text-sm text-zinc-100">
          <div className="flex items-center gap-2">
            <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-emerald-500/20 text-emerald-300">
              {icon ?? <Gauge className="h-5 w-5" />}
            </div>
            <div>
              <p className="text-xs uppercase tracking-[0.25em] text-emerald-300/80">{title}</p>
              <p className="text-2xl font-semibold text-white">{value.toLocaleString()} <span className="text-xs text-emerald-200/70">/ {max}</span></p>
            </div>
          </div>
          {subtitle && <p className="font-mono text-xs text-emerald-100/70">{subtitle}</p>}
        </div>
      </div>
    </div>
  );
}

export function TokenUsageCard({ tokens }: { tokens: number }) {
  return (
    <div className="relative overflow-hidden rounded-2xl border border-emerald-500/30 bg-white/5 p-5 backdrop-blur-lg shadow-lg shadow-emerald-500/10">
      <div className="absolute inset-0 bg-gradient-to-br from-emerald-500/10 via-transparent to-emerald-500/5 pointer-events-none" />
      <div className="relative flex items-center gap-4">
        <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-emerald-500/20 text-emerald-300">
          <Cpu className="h-5 w-5" />
        </div>
        <div className="flex flex-1 flex-col">
          <p className="text-xs uppercase tracking-[0.25em] text-emerald-300/80">Token Usage</p>
          <p className="text-3xl font-semibold text-white">{tokens.toLocaleString()} tokens</p>
          <p className="font-mono text-xs text-emerald-100/70">Real-time accumulation</p>
        </div>
      </div>
    </div>
  );
}
