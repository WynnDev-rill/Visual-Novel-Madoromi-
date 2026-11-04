#!/usr/bin/env python3
"""Check portable Graphify artifacts without installing development dependencies."""
import runpy
from pathlib import Path

namespace = runpy.run_path(str(Path(__file__).resolve().parents[1] / "tools/knowledge_graph.py"))
namespace["check"]()
