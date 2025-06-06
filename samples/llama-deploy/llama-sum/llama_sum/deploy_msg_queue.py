# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0

from llama_deploy import (
    deploy_core,
    ControlPlaneConfig,
    SimpleMessageQueueConfig,
)

async def main():
    await deploy_core(
        control_plane_config=ControlPlaneConfig(),
        message_queue_config=SimpleMessageQueueConfig(),
        disable_control_plane=True,
    )

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())