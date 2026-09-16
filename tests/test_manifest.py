# -*- coding: utf-8 -*-
"""SKILL.md 必须能被 agent 的技能加载器认出来——它只看 frontmatter，不看目录。
name 不合法 / description 缺失 / 值里有裸的 ASCII 冒号+空格（YAML 解析直接失败），
后果都是"装上了但 agent 看不见"。跑法：python -m unittest discover -s tests。"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
KEY = re.compile(r'^([A-Za-z0-9_-]+):[ \t]*(.*)$')


class TestManifest(unittest.TestCase):
    def _fm_lines(self):
        lines = (REPO / "SKILL.md").read_text(encoding="utf-8").splitlines()
        self.assertEqual(lines[0].strip(), "---", "SKILL.md 第一行必须是 frontmatter 起始 ---")
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        self.assertIsNotNone(end, "frontmatter 没有闭合的 ---")
        return lines[1:end]

    def _values(self):
        out = {}
        for line in self._fm_lines():
            m = KEY.match(line)
            if m:
                out[m.group(1)] = m.group(2)
        return out

    def test_name_is_canonical(self):
        name = self._values().get("name", "").strip().strip('"').strip("'")
        self.assertEqual(name, "humanizer-zh-plus")
        self.assertRegex(name, r"^[a-z0-9]+(-[a-z0-9]+)*$", "name 必须是小写 kebab-case")

    def test_description_present(self):
        self.assertTrue(self._values().get("description", "").strip(), "缺 description，严格加载器会跳过该技能")

    def test_no_bare_colon_in_values(self):
        for k, v in self._values().items():
            if not v or v[0] in "\"'|>[&*":
                continue
            self.assertNotIn(": ", v, "frontmatter 值 '%s' 里有裸冒号+空格，YAML 整块解析会失败" % k)

    def test_base_layer_pointer(self):
        """plus 是增量层：正文必须点名基座，否则单独加载等于只有一半规则。"""
        body = (REPO / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("humanizer-zh", body[:4000])


if __name__ == "__main__":
    unittest.main()
