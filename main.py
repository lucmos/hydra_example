import hydra
from omegaconf import OmegaConf


@hydra.main(config_path="conf", config_name="default")
def main(cfg):
    print(OmegaConf.to_yaml(cfg, resolve=True))


if __name__ == "__main__":
    main()
