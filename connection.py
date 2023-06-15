"""
Establish GUI Scripting connections to SAP GUI environments.

Allows connecting to existing sessions, or establishing entirely new sessions.
"""
import os
import time
import sys

try:
    import win32com.client  # pylint: disable=E0401
except ImportError:
    pass


def __get_connection(application, landscape):
    landscapes = {
        "PW4": "PW4 - PW4 - Dec. EWM S/4HANA Region 4",
        "PWP": "PWP - EWM Asia Production",
        "PRT": "PRT - RT Production",
        "RT2": "RT2 - RT Cycle 3 Testing System",
        "RT3": "RT3 - RT Cycle 3 Testing System",
        "WM3": "WM3 - WM Cycle 3 Testing System",
        "DAG": "DAG - North American Ag Dataload",
        "QRT": "QRT - RT Quality Assurance",
        "QWD": "QWD - ",
        "QWP": "QWP - EWM Asia Quality Assurance",
        "WD3": "WD3 - Decentralized EWM Cycle 3 Test System"
    }
    for app in range(0, application.Children.Count):
        conn = application.Children(app)
        for child in range(0, conn.Children.Count):
            sess = conn.Children(child)
            if sess.info.SystemName == landscape:
                return conn, True
    conn = application.OpenConnection(landscapes[landscape], True)
    return conn, False


def connect(landscape: str, new_session: bool = False):
    """
    Connect to an SAP Session.

    Parameters
    ----------
    landscape : str
        3 Byte code for SAP Landscape to connect to.
    newSession : bool, optional
        If existing session is open for given landscape, optionally force
        a new session to be created.

    Returns
    -------
    session : SAP Session.
        An SAP Session for scripting.

    """
    try:
        sap_auto = win32com.client.GetObject("SAPGUI")
    except BaseException:  # pylint: disable=broad-except
        print(sys.exc_info()[0])
        os.startfile("C:/Program Files (x86)/SAP/FrontEnd/SAPgui/SapLogon.exe")
        time.sleep(7.5)
        sap_auto = win32com.client.GetObject("SAPGUI")
    application = sap_auto.GetScriptingEngine
    connection, existing_conn = __get_connection(application, landscape)
    session = connection.Children(0)
    if new_session and existing_conn:
        session.createSession()
        connection, existing_conn = __get_connection(
            win32com.client.GetObject("SAPGUI").GetScriptingEngine, landscape
        )
        session = connection.Children(connection.Children.Count - 1)
    return session