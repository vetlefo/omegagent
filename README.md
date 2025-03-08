# Agentic Reasoning: Reasoning LLM with Agentic Tools
An open-source framework for deep research and beyond. The core idea is to integrate agentic tools into LLM reasoning.

Warning: Still in development. Theoretically runnable, but undergoing rapid updates.

## Install
install from environment.yml, e.g.
```
conda env create -f environment.yml
```

## Run
export your remote LLM API key in environment if you are using remote LLM, e.g.
```
export OPENAI_API_KEY="your openai api key"
```

export your you.com api key in environment if you are using deep research
```
export YDC_API_KEY="your you.com api key"
```

prepare JINA and BING API key if needed

run command:
```
python scripts/run_agentic_reason.py \
--use_jina True \
--jina_api_key "your jina api key" \
--bing_subscription_key "your bing api key"\ 
--remote_model "your remote model name, e.g. gpt-4o" \
--mind_map True \ (optional)
--deep_research True \ (optional, if you want to use deep research)
```

## TODO LIST
- [ ] auto research
- [ ] clean agentic reasoning


## Thanks
Code copied a lot from ...

## Ref
~~~
@misc{wu2025agenticreasoningreasoningllms,
      title={Agentic Reasoning: Reasoning LLMs with Tools for the Deep Research}, 
      author={Junde Wu and Jiayuan Zhu and Yuyuan Liu},
      year={2025},
      eprint={2502.04644},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2502.04644}, 
}
~~~


```
Agentic-Reasoning
├─ .trunk
│  ├─ actions
│  │  ├─ trunk-cache-prune
│  │  │  ├─ 2025-03-04-08-56-22.764.yaml
│  │  │  ├─ 2025-03-04-09-56-22.762.yaml
│  │  │  ├─ 2025-03-05-09-01-58.519.yaml
│  │  │  ├─ 2025-03-06-10-28-21.239.yaml
│  │  │  └─ 2025-03-07-09-22-29.761.yaml
│  │  ├─ trunk-share-with-everyone
│  │  │  ├─ 2025-03-04-08-56-22.758.yaml
│  │  │  ├─ 2025-03-04-09-56-22.768.yaml
│  │  │  ├─ 2025-03-05-09-01-58.520.yaml
│  │  │  ├─ 2025-03-06-10-28-21.207.yaml
│  │  │  └─ 2025-03-07-09-22-29.762.yaml
│  │  ├─ trunk-single-player-auto-on-upgrade
│  │  │  ├─ 2025-03-04-09-01-56.370.yaml
│  │  │  ├─ 2025-03-04-09-56-56.287.yaml
│  │  │  ├─ 2025-03-05-09-22-21.409.yaml
│  │  │  ├─ 2025-03-06-10-29-00.767.yaml
│  │  │  └─ 2025-03-07-09-23-04.174.yaml
│  │  ├─ trunk-single-player-auto-upgrade
│  │  │  ├─ 2025-03-04-10-02-05.439.yaml
│  │  │  ├─ 2025-03-05-11-04-30.778.yaml
│  │  │  ├─ 2025-03-06-10-28-26.107.yaml
│  │  │  └─ 2025-03-07-10-04-41.905.yaml
│  │  ├─ trunk-upgrade-available
│  │  │  ├─ 2025-03-04-09-02-11.920.yaml
│  │  │  ├─ 2025-03-04-09-56-34.765.yaml
│  │  │  ├─ 2025-03-04-09-56-48.514.yaml
│  │  │  ├─ 2025-03-04-09-56-59.831.yaml
│  │  │  ├─ 2025-03-04-09-57-12.245.yaml
│  │  │  ├─ 2025-03-04-10-02-10.152.yaml
│  │  │  ├─ 2025-03-04-10-02-17.256.yaml
│  │  │  ├─ 2025-03-04-11-02-10.357.yaml
│  │  │  ├─ 2025-03-04-12-02-12.512.yaml
│  │  │  ├─ 2025-03-04-13-02-10.417.yaml
│  │  │  ├─ 2025-03-04-14-02-14.681.yaml
│  │  │  ├─ 2025-03-04-15-44-41.469.yaml
│  │  │  ├─ 2025-03-04-16-02-12.763.yaml
│  │  │  ├─ 2025-03-04-17-02-10.556.yaml
│  │  │  ├─ 2025-03-04-18-02-12.513.yaml
│  │  │  ├─ 2025-03-04-19-02-11.58.yaml
│  │  │  ├─ 2025-03-04-20-02-12.710.yaml
│  │  │  ├─ 2025-03-05-05-03-28.889.yaml
│  │  │  ├─ 2025-03-05-05-03-28.890.yaml
│  │  │  ├─ 2025-03-05-07-02-44.707.yaml
│  │  │  ├─ 2025-03-05-07-03-28.522.yaml
│  │  │  ├─ 2025-03-05-08-18-33.95.yaml
│  │  │  ├─ 2025-03-05-09-03-26.555.yaml
│  │  │  ├─ 2025-03-05-09-22-19.915.yaml
│  │  │  ├─ 2025-03-05-09-22-20.431.yaml
│  │  │  ├─ 2025-03-05-09-22-34.903.yaml
│  │  │  ├─ 2025-03-05-11-04-36.675.yaml
│  │  │  ├─ 2025-03-05-11-04-38.267.yaml
│  │  │  ├─ 2025-03-05-11-04-43.466.yaml
│  │  │  ├─ 2025-03-05-12-22-00.77.yaml
│  │  │  ├─ 2025-03-05-13-04-37.766.yaml
│  │  │  ├─ 2025-03-05-14-29-48.261.yaml
│  │  │  ├─ 2025-03-05-15-19-11.652.yaml
│  │  │  ├─ 2025-03-05-19-07-53.947.yaml
│  │  │  ├─ 2025-03-05-19-07-54.260.yaml
│  │  │  ├─ 2025-03-05-20-22-36.198.yaml
│  │  │  ├─ 2025-03-05-21-07-54.191.yaml
│  │  │  ├─ 2025-03-05-22-24-11.352.yaml
│  │  │  ├─ 2025-03-05-23-07-52.56.yaml
│  │  │  ├─ 2025-03-06-01-56-14.888.yaml
│  │  │  ├─ 2025-03-06-01-56-14.916.yaml
│  │  │  ├─ 2025-03-06-02-56-11.652.yaml
│  │  │  ├─ 2025-03-06-07-56-48.1.yaml
│  │  │  ├─ 2025-03-06-07-56-48.224.yaml
│  │  │  ├─ 2025-03-06-10-28-39.512.yaml
│  │  │  ├─ 2025-03-06-10-28-39.759.yaml
│  │  │  ├─ 2025-03-06-10-28-40.825.yaml
│  │  │  ├─ 2025-03-06-10-28-49.741.yaml
│  │  │  ├─ 2025-03-06-10-28-58.897.yaml
│  │  │  ├─ 2025-03-06-10-29-15.511.yaml
│  │  │  ├─ 2025-03-06-11-42-41.249.yaml
│  │  │  ├─ 2025-03-06-12-28-34.868.yaml
│  │  │  ├─ 2025-03-06-13-28-34.57.yaml
│  │  │  ├─ 2025-03-06-14-28-34.772.yaml
│  │  │  ├─ 2025-03-06-15-29-44.473.yaml
│  │  │  ├─ 2025-03-06-16-51-54.260.yaml
│  │  │  ├─ 2025-03-06-17-28-33.56.yaml
│  │  │  ├─ 2025-03-06-18-28-34.951.yaml
│  │  │  ├─ 2025-03-06-20-38-33.574.yaml
│  │  │  ├─ 2025-03-06-20-38-35.513.yaml
│  │  │  ├─ 2025-03-06-21-38-34.55.yaml
│  │  │  ├─ 2025-03-06-22-56-19.266.yaml
│  │  │  ├─ 2025-03-06-23-38-32.387.yaml
│  │  │  ├─ 2025-03-07-03-06-02.517.yaml
│  │  │  ├─ 2025-03-07-03-06-02.709.yaml
│  │  │  ├─ 2025-03-07-05-02-24.263.yaml
│  │  │  ├─ 2025-03-07-05-06-02.263.yaml
│  │  │  ├─ 2025-03-07-08-24-56.498.yaml
│  │  │  ├─ 2025-03-07-08-24-58.516.yaml
│  │  │  ├─ 2025-03-07-09-22-55.782.yaml
│  │  │  ├─ 2025-03-07-09-23-07.510.yaml
│  │  │  ├─ 2025-03-07-09-23-20.517.yaml
│  │  │  ├─ 2025-03-07-09-24-55.675.yaml
│  │  │  ├─ 2025-03-07-10-04-54.685.yaml
│  │  │  ├─ 2025-03-07-10-24-55.640.yaml
│  │  │  ├─ 2025-03-07-11-43-24.715.yaml
│  │  │  ├─ 2025-03-07-13-03-30.815.yaml
│  │  │  ├─ 2025-03-07-13-24-56.141.yaml
│  │  │  ├─ 2025-03-07-14-24-58.677.yaml
│  │  │  ├─ 2025-03-07-15-24-58.158.yaml
│  │  │  ├─ 2025-03-07-19-19-14.728.yaml
│  │  │  ├─ 2025-03-07-19-19-14.774.yaml
│  │  │  ├─ 2025-03-07-20-28-05.400.yaml
│  │  │  ├─ 2025-03-07-21-27-06.730.yaml
│  │  │  └─ 2025-03-07-22-19-14.256.yaml
│  │  └─ trunk-whoami
│  │     ├─ 2025-03-04-10-02-09.532.yaml
│  │     ├─ 2025-03-05-11-04-34.776.yaml
│  │     ├─ 2025-03-06-10-28-34.734.yaml
│  │     └─ 2025-03-07-10-04-47.928.yaml
│  ├─ configs
│  │  ├─ .isort.cfg
│  │  ├─ .markdownlint.yaml
│  │  ├─ .yamllint.yaml
│  │  ├─ ruff.toml
│  │  └─ svgo.config.mjs
│  ├─ notifications
│  │  ├─ trunk-share-with-everyone.yaml
│  │  ├─ trunk-share-with-everyone.yaml.lock
│  │  ├─ trunk-upgrade.yaml
│  │  └─ trunk-upgrade.yaml.lock
│  ├─ out
│  │  ├─ 05K2X.yaml
│  │  ├─ 0E923.yaml
│  │  ├─ 0ZM0J.yaml
│  │  ├─ 1D7C4.yaml
│  │  ├─ 1EEBF.yaml
│  │  ├─ 1GJ15.yaml
│  │  ├─ 1H2FX.yaml
│  │  ├─ 1JR5T.yaml
│  │  ├─ 1U8EQ.yaml
│  │  ├─ 1W6VV.yaml
│  │  ├─ 1YJS3.yaml
│  │  ├─ 23TBQ.yaml
│  │  ├─ 2402Z.yaml
│  │  ├─ 2E91J.yaml
│  │  ├─ 2EKFD.yaml
│  │  ├─ 2KDC8.yaml
│  │  ├─ 2MW9C.yaml
│  │  ├─ 2PHAX.yaml
│  │  ├─ 3HB0E.yaml
│  │  ├─ 3J8HC.yaml
│  │  ├─ 3MN18.yaml
│  │  ├─ 3SGZH.yaml
│  │  ├─ 3YQK3.yaml
│  │  ├─ 413J3.yaml
│  │  ├─ 4190S.yaml
│  │  ├─ 41QRG.yaml
│  │  ├─ 434TF.yaml
│  │  ├─ 4389U.yaml
│  │  ├─ 4DM3F.yaml
│  │  ├─ 4GMCP.yaml
│  │  ├─ 4HXS1.yaml
│  │  ├─ 4Y9K2.yaml
│  │  ├─ 5BYXR.yaml
│  │  ├─ 5W7BC.yaml
│  │  ├─ 5ZB46.yaml
│  │  ├─ 61T1R.yaml
│  │  ├─ 659EN.yaml
│  │  ├─ 674C2.yaml
│  │  ├─ 67D0H.yaml
│  │  ├─ 68VBD.yaml
│  │  ├─ 6BLSM.yaml
│  │  ├─ 6F08U.yaml
│  │  ├─ 7325Q.yaml
│  │  ├─ 7AER1.yaml
│  │  ├─ 7CVMM.yaml
│  │  ├─ 7L912.yaml
│  │  ├─ 7QQJK.yaml
│  │  ├─ 7RZJC.yaml
│  │  ├─ 7SPAY.yaml
│  │  ├─ 7TMG2.yaml
│  │  ├─ 7X51Q.yaml
│  │  ├─ 83N0K.yaml
│  │  ├─ 83RXM.yaml
│  │  ├─ 88STR.yaml
│  │  ├─ 8A8B4.yaml
│  │  ├─ 8FNXJ.yaml
│  │  ├─ 8YXD3.yaml
│  │  ├─ 9342L.yaml
│  │  ├─ 95RB6.yaml
│  │  ├─ 9GMEG.yaml
│  │  ├─ 9NT76.yaml
│  │  ├─ 9QPNJ.yaml
│  │  ├─ A6EDG.yaml
│  │  ├─ AFZ30.yaml
│  │  ├─ AN5RE.yaml
│  │  ├─ AWNJS.yaml
│  │  ├─ B70D4.yaml
│  │  ├─ BEK9R.yaml
│  │  ├─ BETRV.yaml
│  │  ├─ BGUAU.yaml
│  │  ├─ BH58H.yaml
│  │  ├─ C04PL.yaml
│  │  ├─ C95M1.yaml
│  │  ├─ C95PX.yaml
│  │  ├─ CG860.yaml
│  │  ├─ CJ66A.yaml
│  │  ├─ CTRQL.yaml
│  │  ├─ CWKV0.yaml
│  │  ├─ CXgGj.yaml
│  │  ├─ D3V8V.yaml
│  │  ├─ D5RRC.yaml
│  │  ├─ D6HB2.yaml
│  │  ├─ DBBWN.yaml
│  │  ├─ DNNAJ.yaml
│  │  ├─ DU4L4.yaml
│  │  ├─ E2x6E.yaml
│  │  ├─ EDYLP.yaml
│  │  ├─ EX3BF.yaml
│  │  ├─ F3GTW.yaml
│  │  ├─ F6VEM.yaml
│  │  ├─ FJ0W7.yaml
│  │  ├─ FOb6K.yaml
│  │  ├─ FT8FS.yaml
│  │  ├─ G6A1N.yaml
│  │  ├─ G6Rem.yaml
│  │  ├─ GDXLD.yaml
│  │  ├─ GFQH6.yaml
│  │  ├─ GNLX2.yaml
│  │  ├─ GZJTL.yaml
│  │  ├─ H76F9.yaml
│  │  ├─ HAVNV.yaml
│  │  ├─ HLMDL.yaml
│  │  ├─ HPTFY.yaml
│  │  ├─ J1WYR.yaml
│  │  ├─ J2RWK.yaml
│  │  ├─ JATNK.yaml
│  │  ├─ JQ90J.yaml
│  │  ├─ JR8VN.yaml
│  │  ├─ JRTXN.yaml
│  │  ├─ KDCYZ.yaml
│  │  ├─ KLBQ2.yaml
│  │  ├─ KR44N.yaml
│  │  ├─ L1U55.yaml
│  │  ├─ L7PWD.yaml
│  │  ├─ MMPLH.yaml
│  │  ├─ NZCDT.yaml
│  │  ├─ PB0GA.yaml
│  │  ├─ PEXCU.yaml
│  │  ├─ PGWJQ.yaml
│  │  ├─ PKS01.yaml
│  │  ├─ PLP33.yaml
│  │  ├─ PNLJ5.yaml
│  │  ├─ PTTEQ.yaml
│  │  ├─ PWA0M.yaml
│  │  ├─ PY6GY.yaml
│  │  ├─ Q05KJ.yaml
│  │  ├─ Q08TB.yaml
│  │  ├─ Q20C3.yaml
│  │  ├─ R0JSL.yaml
│  │  ├─ R7FX3.yaml
│  │  ├─ RB1J6.yaml
│  │  ├─ RQK6U.yaml
│  │  ├─ RRAKW.yaml
│  │  ├─ RRULP.yaml
│  │  ├─ RVSBG.yaml
│  │  ├─ SBQ1R.yaml
│  │  ├─ SXN22.yaml
│  │  ├─ TA212.yaml
│  │  ├─ TAC5C.yaml
│  │  ├─ TBTX0.yaml
│  │  ├─ TD98D.yaml
│  │  ├─ TGwWX.yaml
│  │  ├─ TJQG0.yaml
│  │  ├─ TK6XM.yaml
│  │  ├─ TKD0A.yaml
│  │  ├─ TRLEZ.yaml
│  │  ├─ TXBMP.yaml
│  │  ├─ UAYHR.yaml
│  │  ├─ UPW5Y.yaml
│  │  ├─ V0X1G.yaml
│  │  ├─ V2SQM.yaml
│  │  ├─ V36R8.yaml
│  │  ├─ V6JCX.yaml
│  │  ├─ VVUNE.yaml
│  │  ├─ VY2NH.yaml
│  │  ├─ WC7KE.yaml
│  │  ├─ WL1TT.yaml
│  │  ├─ WTBX8.yaml
│  │  ├─ WTPGC.yaml
│  │  ├─ XUGA3.yaml
│  │  ├─ Y46CY.yaml
│  │  ├─ YKXR0.yaml
│  │  ├─ YMnsS.yaml
│  │  ├─ YWURY.yaml
│  │  ├─ YX5D5.yaml
│  │  ├─ ZNZHQ.yaml
│  │  ├─ ZXGZX.yaml
│  │  ├─ bPxxr.yaml
│  │  ├─ bolcb.yaml
│  │  └─ s6jem.yaml
│  ├─ plugins
│  │  └─ trunk
│  │     ├─ .devcontainer.json
│  │     ├─ .editorconfig
│  │     ├─ .trunk
│  │     │  ├─ setup-ci
│  │     │  │  └─ action.yaml
│  │     │  └─ trunk.yaml
│  │     ├─ CONTRIBUTING.md
│  │     ├─ LICENSE
│  │     ├─ README.md
│  │     ├─ actions
│  │     │  ├─ buf
│  │     │  │  ├─ README.md
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ commitizen
│  │     │  │  ├─ README.md
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ commitlint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ commitlint.test.ts
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ git
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ git-blame-ignore-revs
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ update_config.sh
│  │     │  ├─ go-mod-tidy
│  │     │  │  ├─ README.md
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ go-mod-tidy-vendor
│  │     │  │  ├─ README.md
│  │     │  │  ├─ go-mod-tidy-vendor.sh
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ hello-world
│  │     │  │  └─ python
│  │     │  │     ├─ README.md
│  │     │  │     ├─ hello
│  │     │  │     ├─ hello_world.test.ts
│  │     │  │     ├─ plugin.yaml
│  │     │  │     └─ requirements.txt
│  │     │  ├─ npm-check
│  │     │  │  ├─ README.md
│  │     │  │  ├─ npm.png
│  │     │  │  ├─ npm_check.js
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ npm-check-pre-push
│  │     │  │  ├─ npm_check.js
│  │     │  │  ├─ package.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ poetry
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ poetry.test.ts
│  │     │  │  └─ requirements.txt
│  │     │  ├─ submodules
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ terraform-docs
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform-docs.py
│  │     │  ├─ trunk
│  │     │  │  └─ plugin.yaml
│  │     │  └─ yarn-check
│  │     │     ├─ README.md
│  │     │     ├─ package.json
│  │     │     ├─ plugin.yaml
│  │     │     ├─ yarn.png
│  │     │     └─ yarn_check.js
│  │     ├─ eslint.config.cjs
│  │     ├─ jest.config.json
│  │     ├─ linters
│  │     │  ├─ actionlint
│  │     │  │  ├─ actionlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ansible-lint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ ansible_lint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ autopep8
│  │     │  │  ├─ autopep8.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ bandit
│  │     │  │  ├─ bandit.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ biome
│  │     │  │  ├─ biome.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ black
│  │     │  │  ├─ black.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ brakeman
│  │     │  │  ├─ brakeman.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ buf
│  │     │  │  ├─ buf.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ buildifier
│  │     │  │  ├─ buildifier.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cfnlint
│  │     │  │  ├─ cfnlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ checkov
│  │     │  │  ├─ checkov.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ circleci
│  │     │  │  ├─ circleci.test.ts
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ run.sh
│  │     │  ├─ clang-format
│  │     │  │  ├─ clang_format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clang-tidy
│  │     │  │  ├─ .clang-tidy
│  │     │  │  ├─ clang_tidy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clippy
│  │     │  │  ├─ clippy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cmake-format
│  │     │  │  ├─ cmake-format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ codespell
│  │     │  │  ├─ codespell.test.ts
│  │     │  │  ├─ codespell_to_sarif.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cspell
│  │     │  │  ├─ cspell.test.ts
│  │     │  │  ├─ cspell.yaml
│  │     │  │  ├─ expected_basic_issues.json
│  │     │  │  ├─ expected_dictionary_issues.json
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ cue-fmt
│  │     │  │  ├─ cue_fmt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dart
│  │     │  │  ├─ dart.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ deno
│  │     │  │  ├─ deno.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ detekt
│  │     │  │  ├─ detekt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ djlint
│  │     │  │  ├─ .djlintrc
│  │     │  │  ├─ README.md
│  │     │  │  ├─ djlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dotenv-linter
│  │     │  │  ├─ dotenv_linter.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dotnet-format
│  │     │  │  ├─ dotnet_format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dustilock
│  │     │  │  ├─ dustilock.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ eslint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ eslint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ flake8
│  │     │  │  ├─ .flake8
│  │     │  │  ├─ flake8.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ git-diff-check
│  │     │  │  ├─ git_diff_check.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gitleaks
│  │     │  │  ├─ gitleaks.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gofmt
│  │     │  │  ├─ gofmt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gofumpt
│  │     │  │  ├─ gofumpt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ goimports
│  │     │  │  ├─ goimports.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gokart
│  │     │  │  ├─ analyzers.yml
│  │     │  │  ├─ gokart.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ golangci-lint
│  │     │  │  ├─ golangci_lint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ golines
│  │     │  │  ├─ golines.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ google-java-format
│  │     │  │  ├─ google-java-format.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ graphql-schema-linter
│  │     │  │  ├─ graphql_schema_linter.test.ts
│  │     │  │  ├─ parse.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ hadolint
│  │     │  │  ├─ .hadolint.yaml
│  │     │  │  ├─ hadolint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ haml-lint
│  │     │  │  ├─ haml_lint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ isort
│  │     │  │  ├─ .isort.cfg
│  │     │  │  ├─ isort.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ iwyu
│  │     │  │  ├─ iwyu.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ktlint
│  │     │  │  ├─ ktlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ kube-linter
│  │     │  │  ├─ kube_linter.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdown-link-check
│  │     │  │  ├─ markdown-link-check.test.ts
│  │     │  │  ├─ parse.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdown-table-prettify
│  │     │  │  ├─ markdown_table_prettify.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdownlint
│  │     │  │  ├─ .markdownlint.yaml
│  │     │  │  ├─ markdownlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ markdownlint-cli2
│  │     │  │  ├─ markdownlint.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ mypy
│  │     │  │  ├─ mypy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ nancy
│  │     │  │  ├─ expected_issues.json
│  │     │  │  ├─ nancy.test.ts
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ run.sh
│  │     │  ├─ nixpkgs-fmt
│  │     │  │  ├─ nixpkgs_fmt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ opa
│  │     │  │  ├─ opa.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ osv-scanner
│  │     │  │  ├─ expected_issues.json
│  │     │  │  ├─ osv_scanner.test.ts
│  │     │  │  ├─ osv_to_sarif.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ oxipng
│  │     │  │  ├─ oxipng.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ perlcritic
│  │     │  │  ├─ .perlcriticrc
│  │     │  │  ├─ perlcritic.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ perltidy
│  │     │  │  ├─ .perltidyrc
│  │     │  │  ├─ perltidy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ php-cs-fixer
│  │     │  │  ├─ php-cs-fixer.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ phpstan
│  │     │  │  ├─ phpstan.test.ts
│  │     │  │  ├─ phpstan_parser.py
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ plugin.yaml
│  │     │  ├─ pmd
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pmd.test.ts
│  │     │  ├─ pragma-once
│  │     │  │  ├─ README.md
│  │     │  │  ├─ fix.sh
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pragma_once.test.ts
│  │     │  ├─ pre-commit-hooks
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pre_commit_hooks.test.ts
│  │     │  ├─ prettier
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ prettier.test.ts
│  │     │  │  └─ prettier_to_sarif.py
│  │     │  ├─ prisma
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ prisma.test.ts
│  │     │  ├─ psscriptanalyzer
│  │     │  │  ├─ README.md
│  │     │  │  ├─ format.ps1
│  │     │  │  ├─ lint.ps1
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ psscriptanalyzer.test.ts
│  │     │  ├─ pylint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pylint.test.ts
│  │     │  ├─ pyright
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ pyright.test.ts
│  │     │  │  └─ pyright_to_sarif.py
│  │     │  ├─ regal
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ regal.test.ts
│  │     │  ├─ remark-lint
│  │     │  │  ├─ .remarkrc.yaml
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ remark_lint.test.ts
│  │     │  ├─ renovate
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ renovate.test.ts
│  │     │  ├─ rome
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ rome.test.ts
│  │     │  ├─ rubocop
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ rubocop.test.ts
│  │     │  │  └─ rubocop_to_sarif.py
│  │     │  ├─ ruff
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ ruff.test.ts
│  │     │  │  ├─ ruff.toml
│  │     │  │  └─ ruff_to_sarif.py
│  │     │  ├─ rufo
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ rufo.test.ts
│  │     │  ├─ rustfmt
│  │     │  │  ├─ .rustfmt.toml
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ rustfmt.test.ts
│  │     │  ├─ scalafmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ scalafmt.test.ts
│  │     │  ├─ semgrep
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ semgrep.test.ts
│  │     │  ├─ shellcheck
│  │     │  │  ├─ .shellcheckrc
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ shellcheck.test.ts
│  │     │  ├─ shfmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ shfmt.test.ts
│  │     │  ├─ snyk
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ snyk.test.ts
│  │     │  ├─ sort-package-json
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sort_package_json.test.ts
│  │     │  ├─ sourcery
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sourcery.test.ts
│  │     │  ├─ sql-formatter
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sql_formatter.test.ts
│  │     │  ├─ sqlfluff
│  │     │  │  ├─ .sqlfluff
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ sqlfluff.test.ts
│  │     │  │  └─ sqlfluff_to_sarif.py
│  │     │  ├─ sqlfmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sqlfmt.test.ts
│  │     │  ├─ squawk
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ squawk.test.ts
│  │     │  ├─ standardrb
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ standardrb.test.ts
│  │     │  ├─ stringslint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ stringslint.test.ts
│  │     │  ├─ stylelint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ stylelint.test.ts
│  │     │  ├─ stylua
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ stylua.test.ts
│  │     │  │  └─ stylua.toml
│  │     │  ├─ svgo
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ svgo.config.mjs
│  │     │  │  └─ svgo.test.ts
│  │     │  ├─ swiftformat
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ swiftformat.test.ts
│  │     │  ├─ swiftlint
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ swiftlint.test.ts
│  │     │  ├─ taplo
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ taplo.test.ts
│  │     │  ├─ terraform
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform.test.ts
│  │     │  ├─ terragrunt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terragrunt.test.ts
│  │     │  ├─ terrascan
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ sarif_to_sarif.py
│  │     │  │  └─ terrascan.test.ts
│  │     │  ├─ tflint
│  │     │  │  ├─ README.md
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tflint.test.ts
│  │     │  ├─ tfsec
│  │     │  │  ├─ parse.py
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfsec.test.ts
│  │     │  ├─ tofu
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tofu.test.ts
│  │     │  ├─ trivy
│  │     │  │  ├─ README.md
│  │     │  │  ├─ config_expected_issues.json
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ trivy.test.ts
│  │     │  │  ├─ trivy_config_to_sarif.py
│  │     │  │  ├─ trivy_fs_secret_to_sarif.py
│  │     │  │  ├─ trivy_fs_vuln_to_sarif.py
│  │     │  │  └─ vuln_expected_issues.json
│  │     │  ├─ trufflehog
│  │     │  │  ├─ plugin.yaml
│  │     │  │  ├─ trufflehog.test.ts
│  │     │  │  └─ trufflehog_to_sarif.py
│  │     │  ├─ trunk-toolbox
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ trunk_toolbox.test.ts
│  │     │  ├─ txtpbfmt
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ txtpbfmt.test.ts
│  │     │  ├─ vale
│  │     │  │  ├─ .vale.ini
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ vale.test.ts
│  │     │  ├─ yamllint
│  │     │  │  ├─ .yamllint.yaml
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ yamllint.test.ts
│  │     │  └─ yapf
│  │     │     ├─ plugin.yaml
│  │     │     └─ yapf.test.ts
│  │     ├─ package-lock.json
│  │     ├─ package.json
│  │     ├─ plugin.yaml
│  │     ├─ repo-tools
│  │     │  ├─ definition-checker
│  │     │  │  └─ check.ts
│  │     │  ├─ linter-test-helper
│  │     │  │  ├─ generate
│  │     │  │  ├─ linter_sample.test.ts
│  │     │  │  ├─ linter_sample_plugin.yaml
│  │     │  │  └─ requirements.txt
│  │     │  └─ tool-test-helper
│  │     │     ├─ generate
│  │     │     ├─ requirements.txt
│  │     │     ├─ tool_sample.test.ts
│  │     │     └─ tool_sample_plugin.yaml
│  │     ├─ runtimes
│  │     │  ├─ README.md
│  │     │  ├─ go
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ java
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ node
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ php
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ python
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ruby
│  │     │  │  └─ plugin.yaml
│  │     │  └─ rust
│  │     │     └─ plugin.yaml
│  │     ├─ security.md
│  │     ├─ tests
│  │     │  ├─ README.md
│  │     │  ├─ driver
│  │     │  │  ├─ action_driver.ts
│  │     │  │  ├─ driver.ts
│  │     │  │  ├─ index.ts
│  │     │  │  ├─ lint_driver.ts
│  │     │  │  └─ tool_driver.ts
│  │     │  ├─ index.ts
│  │     │  ├─ jest_setup.ts
│  │     │  ├─ parse
│  │     │  │  └─ index.ts
│  │     │  ├─ repo_tests
│  │     │  │  ├─ config_check.test.ts
│  │     │  │  ├─ readme_inclusion.test.ts
│  │     │  │  └─ valid_package_download.test.ts
│  │     │  ├─ reporter
│  │     │  │  ├─ index.js
│  │     │  │  └─ reporter.ts
│  │     │  ├─ types
│  │     │  │  └─ index.ts
│  │     │  └─ utils
│  │     │     ├─ index.ts
│  │     │     ├─ landing_state.ts
│  │     │     └─ trunk_config.ts
│  │     ├─ tools
│  │     │  ├─ 1password-cli
│  │     │  │  ├─ 1password_cli.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ act
│  │     │  │  ├─ act.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ action-validator
│  │     │  │  ├─ action_validator.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ adr
│  │     │  │  ├─ adr.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ age
│  │     │  │  ├─ age.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ agebox
│  │     │  │  ├─ agebox.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ air
│  │     │  │  ├─ air.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ alp
│  │     │  │  ├─ alp.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ amazon-ecr-credential-helper
│  │     │  │  ├─ amazon_ecr_credential_helper.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ asciinema
│  │     │  │  ├─ asciinema.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ assh
│  │     │  │  ├─ assh.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ aws-amplify
│  │     │  │  ├─ aws_amplify.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ awscli
│  │     │  │  ├─ awscli.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ bazel
│  │     │  │  ├─ bazel.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ bazel-differ
│  │     │  │  ├─ bazel.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ circleci
│  │     │  │  ├─ circleci.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clangd
│  │     │  │  ├─ clangd.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ clangd-indexing-tools
│  │     │  │  ├─ clangd_indexing_tools.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dbt-cli
│  │     │  │  ├─ dbt_cli.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ deno
│  │     │  │  ├─ deno.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ diff-so-fancy
│  │     │  │  ├─ diff_so_fancy.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ difft
│  │     │  │  ├─ difft.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ docker-credential-ecr-login
│  │     │  │  ├─ docker-credential-ecr-login.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ dotnet
│  │     │  │  ├─ dotnet.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ eksctl
│  │     │  │  ├─ eksctl.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gh
│  │     │  │  ├─ gh.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gk
│  │     │  │  ├─ gk.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ goreleaser
│  │     │  │  ├─ goreleaser.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ grpcui
│  │     │  │  ├─ grpcui.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gt
│  │     │  │  ├─ gt.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ gulp
│  │     │  │  ├─ gulp.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ helm
│  │     │  │  ├─ helm.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ ibazel
│  │     │  │  ├─ ibazel.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ istioctl
│  │     │  │  ├─ istioctl.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ jq
│  │     │  │  ├─ jq.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ kubectl
│  │     │  │  ├─ kubectl.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ minikube
│  │     │  │  ├─ minikube.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ paratest
│  │     │  │  ├─ paratest.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ phpunit
│  │     │  │  ├─ phpunit.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ platformio
│  │     │  │  ├─ platformio.test.ts
│  │     │  │  └─ plugin.yaml
│  │     │  ├─ pnpm
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pnpm.test.ts
│  │     │  ├─ prisma
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ prisma.test.ts
│  │     │  ├─ pwsh
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ pwsh.test.ts
│  │     │  ├─ renovate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ renovate.test.ts
│  │     │  ├─ ripgrep
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ ripgrep.test.ts
│  │     │  ├─ sentry-cli
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sentry_cli.test.ts
│  │     │  ├─ sfdx
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sfdx.test.ts
│  │     │  ├─ sourcery
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ sourcery.test.ts
│  │     │  ├─ tailwindcss
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tailwindcss.test.ts
│  │     │  ├─ target-determinator
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ target_determinator.test.ts
│  │     │  ├─ terraform
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform.test.ts
│  │     │  ├─ terraform-docs
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform_docs.test.ts
│  │     │  ├─ terraform-switcher
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraform_switcher.test.ts
│  │     │  ├─ terraformer
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terraformer.test.ts
│  │     │  ├─ terramate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ terramate.test.ts
│  │     │  ├─ tfmigrate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfmigrate.test.ts
│  │     │  ├─ tfnotify
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfnotify.test.ts
│  │     │  ├─ tfupdate
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tfupdate.test.ts
│  │     │  ├─ tofu
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tofu.test.ts
│  │     │  ├─ tree-sitter
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tree_sitter.test.ts
│  │     │  ├─ ts-node
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ ts_node.test.ts
│  │     │  ├─ tsc
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ tsc.test.ts
│  │     │  ├─ webpack
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ webpack.test.ts
│  │     │  ├─ yarn
│  │     │  │  ├─ plugin.yaml
│  │     │  │  └─ yarn.test.ts
│  │     │  └─ yq
│  │     │     ├─ plugin.yaml
│  │     │     └─ yq.test.ts
│  │     ├─ trunk.ps1
│  │     └─ tsconfig.json
│  ├─ tools
│  │  ├─ bandit
│  │  ├─ black
│  │  ├─ checkov
│  │  ├─ isort
│  │  ├─ markdownlint
│  │  ├─ osv-scanner
│  │  ├─ prettier
│  │  ├─ ruff
│  │  ├─ svgo
│  │  ├─ trufflehog
│  │  ├─ trunk
│  │  └─ yamllint
│  └─ trunk.yaml
├─ AGENTIC_REASONING_INTEGRATION.md
├─ CLAUDE.md
├─ CODEBASE_IMPROVEMENT_ROADMAP.md
├─ CODEBASE_IMPROVEMENT_SUMMARY.md
├─ CONTINUOUS_ORCHESTRATION.md
├─ GEMINI_FEEDBACK_ASSESSMENT.md
├─ GEMINI_INTEGRATION.md
├─ IMPLEMENTATION_PREREQUISITES.md
├─ INTEGRATION_GUIDE.md
├─ LICENSE
├─ Miniconda3-latest-MacOSX-x86_64.sh
├─ ORCHESTRATION_FIXES.md
├─ PROJECT_BREAKDOWN.md
├─ PROJECT_STATUS.md
├─ PROMPT_LIBRARY_DESIGN.md
├─ README 2.md
├─ README.md
├─ TESTING_GUIDE.md
├─ agentic_research
│  ├─ __init__.py
│  ├─ collaborative_storm
│  │  ├─ __init__.py
│  │  ├─ engine.py
│  │  └─ modules
│  │     ├─ __init__.py
│  │     ├─ article_generation.py
│  │     ├─ callback.py
│  │     ├─ co_storm_agents.py
│  │     ├─ collaborative_storm_utils.py
│  │     ├─ costorm_expert_utterance_generator.py
│  │     ├─ expert_generation.py
│  │     ├─ grounded_question_answering.py
│  │     ├─ grounded_question_generation.py
│  │     ├─ information_insertion_module.py
│  │     ├─ knowledge_base_summary.py
│  │     ├─ simulate_user.py
│  │     └─ warmstart_hierarchical_chat.py
│  ├─ dataclass.py
│  ├─ encoder.py
│  ├─ interface.py
│  ├─ lm.py
│  ├─ logging_wrapper.py
│  ├─ rm.py
│  ├─ storm_analysis
│  │  ├─ __init__.py
│  │  ├─ engine.py
│  │  └─ modules
│  │     ├─ __init__.py
│  │     ├─ article_generation.py
│  │     ├─ article_polish.py
│  │     ├─ callback.py
│  │     ├─ knowledge_curation.py
│  │     ├─ outline_generation.py
│  │     ├─ persona_generator.py
│  │     ├─ retriever.py
│  │     └─ storm_dataclass.py
│  ├─ test_engine.py
│  └─ utils.py
├─ backend
│  ├─ __init__.py
│  ├─ agents
│  │  ├─ __init__.py
│  │  ├─ coder_agent.py
│  │  ├─ merge_agent.py
│  │  ├─ models.py
│  │  ├─ orchestrator_agent.py
│  │  ├─ planner_agent.py
│  │  ├─ review_agent.py
│  │  ├─ storm_orchestrator_agent.py
│  │  ├─ test_coder_agent.py
│  │  └─ utils.py
│  ├─ communication.py
│  ├─ main.py
│  ├─ models
│  │  └─ shared.py
│  ├─ repo_map.py
│  ├─ server.py
│  └─ utils.py
├─ environment.yml
├─ frontend
│  ├─ README.md
│  ├─ assets
│  │  ├─ index-BOKcLGz6.css
│  │  └─ index-CL5YnCuQ.js
│  ├─ index.html
│  ├─ jsconfig.json
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  └─ vite.svg
│  ├─ src
│  │  ├─ App.svelte
│  │  ├─ app.css
│  │  ├─ main.js
│  │  └─ vite-env.d.ts
│  ├─ svelte.config.js
│  ├─ vite.config.js
│  └─ vite.svg
├─ gemini_feedback.md
├─ integration_guardrails.md
├─ lol
├─ pytest.ini
├─ requirements.txt
├─ scripts
│  ├─ __init__.py
│  ├─ agentic_ds.py
│  ├─ agentic_reason
│  │  ├─ __init__.py
│  │  ├─ cache.py
│  │  ├─ config.py
│  │  ├─ data_loader.py
│  │  ├─ generation.py
│  │  ├─ models.py
│  │  ├─ prompt_manager.py
│  │  ├─ search.py
│  │  └─ utils.py
│  ├─ evaluate.py
│  ├─ github_upload.py
│  ├─ lcb_runner
│  │  ├─ benchmarks
│  │  │  ├─ __init__.py
│  │  │  ├─ code_execution.py
│  │  │  └─ code_generation.py
│  │  ├─ evaluation
│  │  │  ├─ __init__.py
│  │  │  ├─ compute_code_execution_metrics.py
│  │  │  ├─ compute_code_generation_metrics.py
│  │  │  ├─ compute_scores.py
│  │  │  ├─ compute_test_output_prediction_metrics.py
│  │  │  ├─ old_results_check.py
│  │  │  ├─ pass_k_utils.py
│  │  │  ├─ testing_util.py
│  │  │  └─ utils_execute.py
│  │  ├─ lm_styles.py
│  │  ├─ prompts
│  │  │  ├─ __init__.py
│  │  │  ├─ code_execution.py
│  │  │  ├─ code_generation.py
│  │  │  ├─ few_shot_examples
│  │  │  │  └─ generation
│  │  │  │     ├─ func.json
│  │  │  │     └─ stdin.json
│  │  │  └─ self_repair.py
│  │  ├─ pyext
│  │  │  ├─ pyext-0.7
│  │  │  │  ├─ PKG-INFO
│  │  │  │  ├─ README.rst
│  │  │  │  ├─ pyext.py
│  │  │  │  ├─ setup.cfg
│  │  │  │  └─ setup.py
│  │  │  └─ pyext-0.7.tar.gz
│  │  ├─ runner
│  │  │  ├─ base_runner.py
│  │  │  ├─ claude3_runner.py
│  │  │  ├─ claude_runner.py
│  │  │  ├─ cohere_runner.py
│  │  │  ├─ custom_evaluator.py
│  │  │  ├─ deepseek_runner.py
│  │  │  ├─ gemini_runner.py
│  │  │  ├─ main.py
│  │  │  ├─ mistral_runner.py
│  │  │  ├─ oai_runner.py
│  │  │  ├─ parser.py
│  │  │  ├─ runner_utils.py
│  │  │  ├─ scenario_router.py
│  │  │  └─ vllm_runner.py
│  │  └─ utils
│  │     ├─ extraction_utils.py
│  │     ├─ multiprocess.py
│  │     ├─ path_utils.py
│  │     └─ scenarios.py
│  ├─ prompts.py
│  ├─ run_agentic_reason.py
│  ├─ tools
│  │  ├─ __init__.py
│  │  ├─ bing_search.py
│  │  ├─ creat_graph.py
│  │  ├─ duck_search.py
│  │  ├─ mcp_tool.py
│  │  ├─ ollama_client.py
│  │  ├─ run_code.py
│  │  ├─ run_search.py
│  │  └─ temp.py
│  ├─ utils
│  │  ├─ math_equivalence.py
│  │  └─ remote_llm.py
│  └─ yolo.md
├─ setup.py
├─ temp.py
├─ test_import.py
├─ test_imports.py
├─ test_pydantic_ai.py
├─ test_scripts_import.py
└─ test_sentence_transformers.py

```