"""Runpod configuration bootstrapping."""

from sky.provision import common


def bootstrap_instances(
        _region: str, cluster_name: str,
        config: common.ProvisionConfig) -> common.ProvisionConfig:
    """Bootstraps instances for the given cluster."""
    del cluster_name  # unused
    return config
