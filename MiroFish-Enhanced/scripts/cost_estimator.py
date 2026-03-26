#!/usr/bin/env python3
"""
MiroFish Cost Estimator
Estimate API costs before running a simulation.

Usage:
    python scripts/cost_estimator.py
    python scripts/cost_estimator.py --rounds 20 --agents 100 --provider qwen
"""

import argparse

# Cost per 1M tokens (input + output combined estimate) in USD
PROVIDER_COSTS = {
    "qwen": {
        "name": "Alibaba Qwen-Plus",
        "cost_per_1m": 0.40,
        "free_tier": "Limited free credits on signup",
        "signup": "https://bailian.console.aliyun.com/",
        "notes": "Cheapest option, best for MiroFish"
    },
    "deepseek": {
        "name": "DeepSeek Chat",
        "cost_per_1m": 0.27,
        "free_tier": "Free credits on signup",
        "signup": "https://platform.deepseek.com/",
        "notes": "Very cheap, high quality"
    },
    "groq": {
        "name": "Groq (Llama 3.3 70B)",
        "cost_per_1m": 0.05,
        "free_tier": "Generous free tier (daily limits)",
        "signup": "https://console.groq.com/",
        "notes": "Fastest inference, excellent free tier"
    },
    "gemini": {
        "name": "Google Gemini Flash",
        "cost_per_1m": 0.10,
        "free_tier": "Free tier available",
        "signup": "https://aistudio.google.com/",
        "notes": "Good free tier for experimentation"
    },
    "openai": {
        "name": "OpenAI GPT-4o-mini",
        "cost_per_1m": 0.60,
        "free_tier": "No free tier",
        "signup": "https://platform.openai.com/",
        "notes": "Most compatible but more expensive"
    }
}

def estimate_tokens(rounds: int, agents: int) -> dict:
    """Estimate token usage for a simulation."""
    # Per-round estimates (rough averages based on testing)
    tokens_per_agent_per_round = 800    # agent reasoning + actions
    tokens_for_graph_build = 15000       # knowledge graph construction
    tokens_for_agent_generation = agents * 400  # persona generation
    tokens_for_report = 8000             # final report generation

    simulation_tokens = rounds * agents * tokens_per_agent_per_round
    total_tokens = (
        tokens_for_graph_build +
        tokens_for_agent_generation +
        simulation_tokens +
        tokens_for_report
    )

    return {
        "graph_build": tokens_for_graph_build,
        "agent_generation": tokens_for_agent_generation,
        "simulation": simulation_tokens,
        "report": tokens_for_report,
        "total": total_tokens
    }

def calculate_cost(tokens: int, provider: str) -> float:
    """Calculate cost in USD."""
    cost_per_1m = PROVIDER_COSTS[provider]["cost_per_1m"]
    return (tokens / 1_000_000) * cost_per_1m

def print_estimate(rounds: int, agents: int, provider: str = None):
    """Print cost estimate."""
    tokens = estimate_tokens(rounds, agents)

    print("\n" + "=" * 55)
    print("  MiroFish Cost Estimator")
    print("=" * 55)
    print(f"\n  Simulation Parameters:")
    print(f"    Rounds  : {rounds}")
    print(f"    Agents  : ~{agents} per platform (x2 platforms)")
    print(f"\n  Estimated Token Usage:")
    print(f"    Graph build      : {tokens['graph_build']:,} tokens")
    print(f"    Agent generation : {tokens['agent_generation']:,} tokens")
    print(f"    Simulation       : {tokens['simulation']:,} tokens")
    print(f"    Report           : {tokens['report']:,} tokens")
    print(f"    TOTAL            : {tokens['total']:,} tokens")

    print(f"\n  Cost by Provider:")
    print(f"  {'Provider':<25} {'Est. Cost':>10}  {'Free Tier'}")
    print(f"  {'-'*55}")

    providers_to_show = [provider] if provider else list(PROVIDER_COSTS.keys())
    for p in providers_to_show:
        info = PROVIDER_COSTS[p]
        cost = calculate_cost(tokens['total'], p)
        cost_str = f"${cost:.3f}" if cost >= 0.001 else "< $0.001"
        free_str = info['free_tier']
        print(f"  {info['name']:<25} {cost_str:>10}  {free_str}")

    print(f"\n  Recommendations:")
    if rounds > 40:
        print(f"  ⚠  WARNING: {rounds} rounds is high — start with 10-20 rounds first!")
    else:
        print(f"  ✓  {rounds} rounds is a reasonable start")

    cheapest = min(PROVIDER_COSTS.keys(),
                   key=lambda p: calculate_cost(tokens['total'], p))
    cheapest_cost = calculate_cost(tokens['total'], cheapest)
    print(f"  ✓  Cheapest option: {PROVIDER_COSTS[cheapest]['name']} (~${cheapest_cost:.3f})")
    print(f"     Sign up: {PROVIDER_COSTS[cheapest]['signup']}")
    print()

def interactive_mode():
    """Interactive cost estimation."""
    print("\n MiroFish Cost Estimator — Interactive Mode")
    print(" Press Enter to use default values\n")

    try:
        rounds_input = input("  How many simulation rounds? [default: 10]: ").strip()
        rounds = int(rounds_input) if rounds_input else 10

        agents_input = input("  Approx. number of agents? [default: 50]: ").strip()
        agents = int(agents_input) if agents_input else 50

        print("\n  Available providers:")
        for i, (key, info) in enumerate(PROVIDER_COSTS.items(), 1):
            print(f"    {i}. {info['name']} — {info['notes']}")

        provider_input = input(
            "\n  Choose provider (1-5) or name [default: all]: "
        ).strip()

        if provider_input.isdigit():
            idx = int(provider_input) - 1
            provider = list(PROVIDER_COSTS.keys())[idx] if 0 <= idx < 5 else None
        elif provider_input.lower() in PROVIDER_COSTS:
            provider = provider_input.lower()
        else:
            provider = None

        print_estimate(rounds, agents, provider)

    except (ValueError, KeyboardInterrupt):
        print("\n  Invalid input, showing default estimate...\n")
        print_estimate(10, 50, None)

def main():
    parser = argparse.ArgumentParser(
        description="Estimate MiroFish simulation costs before running"
    )
    parser.add_argument(
        "--rounds", type=int, default=None,
        help="Number of simulation rounds"
    )
    parser.add_argument(
        "--agents", type=int, default=None,
        help="Approximate number of agents"
    )
    parser.add_argument(
        "--provider", type=str, default=None,
        choices=list(PROVIDER_COSTS.keys()),
        help="LLM provider to estimate for"
    )

    args = parser.parse_args()

    if args.rounds is None and args.agents is None:
        interactive_mode()
    else:
        rounds = args.rounds or 10
        agents = args.agents or 50
        print_estimate(rounds, agents, args.provider)

if __name__ == "__main__":
    main()
