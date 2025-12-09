"use client";

import { motion, AnimatePresence } from "framer-motion";
import { ArrowRight, Sparkle } from "lucide-react";

const steps = [
  { id: "L0", label: "Gen" },
  { id: "L1", label: "Crit" },
  { id: "L2", label: "Verif" },
  { id: "L3", label: "Refine" },
];

interface LoopStatusProps {
  activeIndex?: number;
}

export function LoopStatus({ activeIndex = 0 }: LoopStatusProps) {
  return (
    <div className="relative overflow-hidden rounded-2xl border border-emerald-500/30 bg-white/5 p-6 backdrop-blur-lg shadow-lg shadow-emerald-500/10">
      <div className="absolute inset-0 bg-gradient-to-br from-emerald-500/10 via-transparent to-emerald-500/5 pointer-events-none" />
      <div className="relative flex flex-col gap-4">
        <div className="flex items-center gap-3 text-emerald-400">
          <Sparkle className="h-5 w-5" />
          <h3 className="text-lg font-semibold tracking-tight">Loop Visualizer</h3>
        </div>
        <div className="grid grid-cols-4 items-center gap-3">
          {steps.map((step, index) => {
            const isActive = index === activeIndex;
            const isComplete = index < activeIndex;

            return (
              <div key={step.id} className="flex items-center gap-2">
                <div className="relative flex-1">
                  <motion.div
                    initial={{ scale: 0.95, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    transition={{ delay: index * 0.1, type: "spring", stiffness: 120 }}
                    className={`flex items-center gap-2 rounded-xl border px-3 py-2 text-sm font-semibold tracking-tight ${
                      isActive
                        ? "border-emerald-400/80 bg-emerald-400/15 text-emerald-100 shadow-inner shadow-emerald-500/30"
                        : "border-white/10 bg-white/5 text-zinc-200"
                    }`}
                  >
                    <div className="relative h-8 w-8">
                      <motion.div
                        className="absolute inset-0 rounded-full border-2 border-emerald-400/50"
                        animate={isActive ? { scale: [1, 1.08, 1] } : { scale: 1 }}
                        transition={{ repeat: isActive ? Infinity : 0, duration: 2, ease: "easeInOut" }}
                      />
                      <div
                        className={`flex h-8 w-8 items-center justify-center rounded-full text-xs font-bold ${
                          isActive
                            ? "bg-emerald-500 text-emerald-950"
                            : isComplete
                            ? "bg-emerald-500/30 text-emerald-100"
                            : "bg-white/5 text-zinc-200"
                        }`}
                      >
                        {step.id}
                      </div>
                    </div>
                    <span className="uppercase tracking-wide">{step.label}</span>
                  </motion.div>
                  <AnimatePresence>
                    {isActive && (
                      <motion.div
                        layoutId="glow"
                        className="absolute -inset-1 rounded-2xl bg-emerald-400/10 blur-md"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                      />
                    )}
                  </AnimatePresence>
                </div>
                {index < steps.length - 1 && (
                  <ArrowRight className="h-4 w-4 text-emerald-300/70" />
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
