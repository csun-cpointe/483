###
# #%L
# Test argocd::Pipelines::Pyspark Pipeline
# %%
# Copyright (C) 2021 Booz Allen
# %%
# All Rights Reserved. You may not copy, reproduce, distribute, publish, display,
# execute, modify, create derivative works of, transmit, sell or offer for resale,
# or in any way exploit any part of this solution without Booz Allen Hamilton's
# express written permission.
# #L%
###
from pyspark_pipeline.step.ingest import Ingest
from krausening.logging import LogManager
from pyspark_pipeline.generated.pipeline.pipeline_base import PipelineBase

"""
Driver to run the PysparkPipeline.

GENERATED STUB CODE - PLEASE ***DO*** MODIFY

Originally generated from: templates/data-delivery-pyspark/pipeline.driver.py.vm 
"""

logger = LogManager.get_instance().get_logger("PysparkPipeline")


if __name__ == "__main__":
    logger.info("STARTED: PysparkPipeline driver")
    PipelineBase().record_pipeline_lineage_start_event()

    # TODO: Execute steps in desired order and handle any inbound and outbound types
    Ingest().execute_step()
    PipelineBase().record_pipeline_lineage_complete_event()
