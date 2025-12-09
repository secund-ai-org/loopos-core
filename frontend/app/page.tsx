import { ActivitySquare, ArrowUpRight, TerminalSquare } from "lucide-react";
import { LoopStatus } from "../components/LoopStatus";
import { MetricsCard, TokenUsageCard } from "../components/MetricsCard";

export default function Page() {
  return (
    <main className="min-h-screen bg-zinc-950 text-white">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,_rgba(16,185,129,0.18),_transparent_45%)]" />
      <div className="relative mx-auto max-w-7xl px-6 py-10">
        <header className="mb-10 flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.35em] text-emerald-300/80">Secund Mission Control</p>
            <h1 className="text-4xl font-bold text-white">Deep Engineering Dashboard</h1>
            <p className="mt-2 max-w-2xl text-sm text-emerald-100/70">
              Monitoring the autonomous loop stack: generation, critique, verification, and refinement. Designed for operator trust
              with live telemetry and glassmorphic clarity.
            </p>
          </div>
          <div className="flex items-center gap-2 rounded-xl border border-emerald-500/30 bg-white/5 px-4 py-2 text-sm text-emerald-100 backdrop-blur-lg shadow-lg shadow-emerald-500/10">
            <ActivitySquare className="h-4 w-4 text-emerald-300" />
            <span className="font-mono">Subsystems: Green</span>
          </div>
        </header>

        <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
          <div className="lg:col-span-2 space-y-6">
            <section className="relative rounded-2xl border border-emerald-500/30 bg-white/5 p-6 backdrop-blur-lg shadow-xl shadow-emerald-500/10">
              <div className="absolute inset-0 bg-gradient-to-br from-emerald-500/10 via-transparent to-emerald-500/5" />
              <div className="relative flex flex-col gap-4">
                <div className="flex items-center gap-3 text-emerald-400">
                  <TerminalSquare className="h-5 w-5" />
                  <h3 className="text-lg font-semibold tracking-tight">Input Command Line</h3>
                </div>
                <div className="flex items-center gap-3 rounded-xl border border-white/10 bg-black/40 px-4 py-3 font-mono text-emerald-100 shadow-inner shadow-emerald-500/10">
                  <span className="text-emerald-400">$</span>
                  <input
                    type="text"
                    placeholder="issue.query('clarify mission & constraints').dispatch()"
                    className="flex-1 bg-transparent text-emerald-50 placeholder:text-emerald-200/40 focus:outline-none"
                  />
                  <button className="flex items-center gap-2 rounded-lg bg-emerald-500 px-3 py-1 text-sm font-semibold text-emerald-950 shadow-lg shadow-emerald-500/30">
                    Execute
                    <ArrowUpRight className="h-4 w-4" />
                  </button>
                </div>
                <div className="rounded-xl border border-emerald-500/20 bg-black/40 p-4 font-mono text-xs text-emerald-100/80 shadow-inner shadow-emerald-500/10">
                  <p className="text-emerald-300">// Live Log</p>
                  <ul className="mt-2 space-y-1">
                    <li>[12:01:24] Dispatching to Gen → Crit → Verif → Refine</li>
                    <li>[12:01:25] Signals stable, awaiting operator input...</li>
                  </ul>
                </div>
              </div>
            </section>

            <LoopStatus activeIndex={1} />

            <section className="relative rounded-2xl border border-emerald-500/30 bg-white/5 p-6 backdrop-blur-lg shadow-xl shadow-emerald-500/10">
              <div className="absolute inset-0 bg-gradient-to-br from-emerald-500/10 via-transparent to-emerald-500/5" />
              <div className="relative flex flex-col gap-3">
                <div className="flex items-center gap-3 text-emerald-400">
                  <ActivitySquare className="h-5 w-5" />
                  <h3 className="text-lg font-semibold tracking-tight">Output Window</h3>
                </div>
                <div className="min-h-[220px] rounded-xl border border-white/10 bg-black/40 p-4 font-mono text-sm text-emerald-50 shadow-inner shadow-emerald-500/10">
                  <p className="text-emerald-300">// Final Verified Response</p>
                  <p className="mt-2 leading-relaxed text-emerald-50/90">
                    SECUND confirms objective alignment. Deployment pathway validated. Critical anomalies: none detected. Ready for
                    live execution with autonomous safeguards engaged.
                  </p>
                </div>
              </div>
            </section>
          </div>

          <div className="space-y-4">
            <MetricsCard
              title="TOFU Index"
              value={82}
              max={100}
              subtitle="Trust over failed uncertainty"
            />
            <MetricsCard
              title="RBB Score"
              value={64}
              max={100}
              subtitle="Resilience before breakage"
              accent="text-emerald-300"
            />
            <TokenUsageCard tokens={15432} />
          </div>
        </div>
      </div>
    </main>
  );
}
