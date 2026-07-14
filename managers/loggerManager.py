"""
loggerManager.py

Purpose:
    Configures and provides the application's logger.

Primary Functions:
    - getLogger()
"""

import logging

def getLogger():
    """
    Creates and returns the application's logger.

    Parameters:
        None

    Returns:
        logging.Logger: Configured application logger.

    Workflow:
        1. Configure the logging system.
        2. Return a named logger.
    """

    # logging.basicConfig() is from the Pyton standard library and sets up the logging configuration for the application. 
    # It specifies the logging level and format for log messages.
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s"
    )

    # logging.getLogger("BibleStudyAgent") retrieves a logger instance with the name "BibleStudyAgent" to be shared throughout the application.
    return logging.getLogger("BibleStudyAgent")