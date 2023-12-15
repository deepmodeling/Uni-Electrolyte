# Changelog

## [1.20.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.19.0...v1.20.0) (2023-12-11)


### Features

* add support for postgresql ([070da91](https://github.com/Franklalalala/uni_electrolyte_beta/commit/070da9180335cc886a1c16659b8c9c3621f43e46))

## [1.19.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.18.0...v1.19.0) (2023-12-02)


### Features

* support thu-3-props train & infer, edm npz 2 db ([0bbf40f](https://github.com/Franklalalala/uni_electrolyte_beta/commit/0bbf40f7bd782aaf1169541bc31424df98c42da5))

## [1.18.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.17.0...v1.18.0) (2023-11-29)


### Features

* better cG-LEFTNet inference, cas support, interval 2D rectangle ([ff6afae](https://github.com/Franklalalala/uni_electrolyte_beta/commit/ff6afae8a3892012e950494a95d25d62610cf3ac))

## [1.17.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.16.0...v1.17.0) (2023-11-25)


### Features

* add cg-leftnet support ([1286a63](https://github.com/Franklalalala/uni_electrolyte_beta/commit/1286a63448490196519fd19b381a64df73c02c79))
* add cg-leftnet support and optimized pipeline ([1286a63](https://github.com/Franklalalala/uni_electrolyte_beta/commit/1286a63448490196519fd19b381a64df73c02c79))
* new schnetpack callbacks and utils for easier load and dump cg-leftnet models ([1286a63](https://github.com/Franklalalala/uni_electrolyte_beta/commit/1286a63448490196519fd19b381a64df73c02c79))


### Bug Fixes

* edm atom encoder & decoder bug ([1286a63](https://github.com/Franklalalala/uni_electrolyte_beta/commit/1286a63448490196519fd19b381a64df73c02c79))

## [1.16.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.15.0...v1.16.0) (2023-11-23)


### Features

* optimized gen pipeline and data transform ([780e032](https://github.com/Franklalalala/uni_electrolyte_beta/commit/780e032abb7e72de07531bb090f3ee5f707fd6de))

## [1.15.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.14.0...v1.15.0) (2023-11-22)


### Features

* move rdkit warning logic to chk_topo func ([0d4547b](https://github.com/Franklalalala/uni_electrolyte_beta/commit/0d4547be44bf3ca540e2771765aa7eb4dee77ac4))

## [1.14.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.13.0...v1.14.0) (2023-11-21)


### Features

* optimized gen pipeline ([d8d9f1c](https://github.com/Franklalalala/uni_electrolyte_beta/commit/d8d9f1c541b28751d247edf7a2fdb76687512ac9))

## [1.13.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.12.1...v1.13.0) (2023-11-21)


### Features

* mask seen to prevent src db leak ([035e124](https://github.com/Franklalalala/uni_electrolyte_beta/commit/035e124b684e97976c62bc8b251539a83565bfca))
* r2 score ( coefficient of determination ) ([035e124](https://github.com/Franklalalala/uni_electrolyte_beta/commit/035e124b684e97976c62bc8b251539a83565bfca))
* r2_score support and mask seen ([035e124](https://github.com/Franklalalala/uni_electrolyte_beta/commit/035e124b684e97976c62bc8b251539a83565bfca))

## [1.12.1](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.12.0...v1.12.1) (2023-11-21)


### Bug Fixes

* inference shuffle bugs && feat: faster db2npz transformation ([e77031b](https://github.com/Franklalalala/uni_electrolyte_beta/commit/e77031b4a3efe79852fb4dd1f362cee650e260ea))

## [1.12.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.11.0...v1.12.0) (2023-11-18)


### Features

* generation with fixed atoms and dummy exponential lr scheme ([6db10d7](https://github.com/Franklalalala/uni_electrolyte_beta/commit/6db10d7876da52ca0a761fec331f2c4554201307))

## [1.11.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.10.0...v1.11.0) (2023-11-17)


### Features

* add support for edm generation ([1832b6b](https://github.com/Franklalalala/uni_electrolyte_beta/commit/1832b6b4431ddfe08e92aabe88fbc9450b172585))

## [1.10.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.9.0...v1.10.0) (2023-11-15)


### Features

* add interval-style conditional generation ([f6a77d4](https://github.com/Franklalalala/uni_electrolyte_beta/commit/f6a77d4b3c6710449b54d38336c200be2ce5fc08))


### Bug Fixes

* fix condition data ([54800ff](https://github.com/Franklalalala/uni_electrolyte_beta/commit/54800ffdbf5f59d1f8fed2fb2ac05ab8734f966e))

## [1.9.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.8.1...v1.9.0) (2023-11-09)


### Features

* a modified painn for better adaptation of cg-schnet ([0a6ecda](https://github.com/Franklalalala/uni_electrolyte_beta/commit/0a6ecdabfc862dca585dd4600feee3abf60d63ab))
* add ase.db split function ([9d02f46](https://github.com/Franklalalala/uni_electrolyte_beta/commit/9d02f467a0d65acc7a1299512442e256b2dedbb1))

## [1.8.1](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.8.0...v1.8.1) (2023-11-03)


### Bug Fixes

* clean db pipeline ([2a6b7dd](https://github.com/Franklalalala/uni_electrolyte_beta/commit/2a6b7dd9825ca0d5ee5ad6b04065221ff23e1874))

## [1.8.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.7.0...v1.8.0) (2023-10-31)


### Features

* add cg-schnet generation pipeline ([fd4708c](https://github.com/Franklalalala/uni_electrolyte_beta/commit/fd4708cc4d7b61adf1db0947639d86c0d9ce2a45))

## [1.7.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.6.0...v1.7.0) (2023-10-25)


### Features

* add cgschnet support ([d216f5c](https://github.com/Franklalalala/uni_electrolyte_beta/commit/d216f5cfd0b05f28c2a61949ca2e2fd4e3801bec))

## [1.6.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.5.0...v1.6.0) (2023-10-12)


### Features

* add pbc data pipeline ([f35edaa](https://github.com/Franklalalala/uni_electrolyte_beta/commit/f35edaa53b9a3242454bf6661c2bfa1bd6ed626c))

## [1.5.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.4.1...v1.5.0) (2023-10-10)


### Features

* pbc support ([ac97c54](https://github.com/Franklalalala/uni_electrolyte_beta/commit/ac97c5490859c7760c2caacde993190226e1836f))

## [1.4.1](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.4.0...v1.4.1) (2023-09-25)


### Bug Fixes

* change entry name ([bcff69f](https://github.com/Franklalalala/uni_electrolyte_beta/commit/bcff69ff9fc8d7ded69ea90961ad4c34a50b9cd4))

## [1.4.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.3.0...v1.4.0) (2023-09-25)


### Features

* add model entry ([a62ff61](https://github.com/Franklalalala/uni_electrolyte_beta/commit/a62ff61c65135aae71174c2b64240a42b964039b))

## [1.3.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.2.0...v1.3.0) (2023-09-24)


### Features

* clean property dependency ([cb80d93](https://github.com/Franklalalala/uni_electrolyte_beta/commit/cb80d9347096fded26ade71d5bd4f8181e15ba52))

## [1.2.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.1.1...v1.2.0) (2023-09-22)


### Features

* change predict step ([e7f4f4b](https://github.com/Franklalalala/uni_electrolyte_beta/commit/e7f4f4bd6c932100679f80d05fcd96d56b04f300))

## [1.1.1](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.1.0...v1.1.1) (2023-09-21)


### Bug Fixes

* a better setup.py ([450f443](https://github.com/Franklalalala/uni_electrolyte_beta/commit/450f443a36b3638e5a34603749f6a6684bb5c7e9))

## [1.1.0](https://github.com/Franklalalala/uni_electrolyte_beta/compare/v1.0.0...v1.1.0) (2023-09-21)


### Features

* add g2gt support ([104bc78](https://github.com/Franklalalala/uni_electrolyte_beta/commit/104bc781b2172aeda5567d1cee6d4ad48fa6343f))

## 1.0.0 (2023-09-17)


### Bug Fixes

* update spherenet features ([4b6f2c9](https://github.com/Franklalalala/uni_electrolyte_beta/commit/4b6f2c95a6a5176cc73116187445c15920d5af88))
