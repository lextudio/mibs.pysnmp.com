# SNMP MIB module (OPCD-USSDB-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPCD-USSDB-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:16 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(opencode_systems,) = mibBuilder.importSymbols(
    "OPCD-SUPPORT-MIB-V2",
    "opencode-systems")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ocussdbrowser_ObjectIdentity = ObjectIdentity
ocussdbrowser = _Ocussdbrowser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 1)
)
_Ocussdbrowser_traps_ObjectIdentity = ObjectIdentity
ocussdbrowser_traps = _Ocussdbrowser_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1)
)
_Definitions_ObjectIdentity = ObjectIdentity
definitions = _Definitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0)
)
_Vars_ObjectIdentity = ObjectIdentity
vars = _Vars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 1)
)


class _Mcr_Host_Type(DisplayString):
    """Custom type mcr_Host based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Mcr_Host_Type.__name__ = "DisplayString"
_Mcr_Host_Object = MibScalar
mcr_Host = _Mcr_Host_Object(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 1, 1),
    _Mcr_Host_Type()
)
mcr_Host.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Host.setStatus("current")


class _Mcr_Severity_Type(Integer32):
    """Custom type mcr_Severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("normal", 4),
          ("warning", 5))
    )


_Mcr_Severity_Type.__name__ = "Integer32"
_Mcr_Severity_Object = MibScalar
mcr_Severity = _Mcr_Severity_Object(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 1, 2),
    _Mcr_Severity_Type()
)
mcr_Severity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Severity.setStatus("mandatory")


class _Mcr_Text_Type(DisplayString):
    """Custom type mcr_Text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Mcr_Text_Type.__name__ = "DisplayString"
_Mcr_Text_Object = MibScalar
mcr_Text = _Mcr_Text_Object(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 1, 3),
    _Mcr_Text_Type()
)
mcr_Text.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Text.setStatus("current")

# Managed Objects groups


# Notification objects

ocussdbrowser_Restart = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 2)
)
ocussdbrowser_Restart.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_Restart.setStatus(
        "current"
    )

ocussdbrowser_Restart_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 3)
)
ocussdbrowser_Restart_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_Restart_Canceled.setStatus(
        "current"
    )

ocussdbrowser_Crash = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 4)
)
ocussdbrowser_Crash.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_Crash.setStatus(
        "current"
    )

ocussdbrowser_Crash_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 5)
)
ocussdbrowser_Crash_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_Crash_Canceled.setStatus(
        "current"
    )

ocussdbrowser_Smsc_Conn = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 6)
)
ocussdbrowser_Smsc_Conn.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_Smsc_Conn.setStatus(
        "current"
    )

ocussdbrowser_Smsc_Conn_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 7)
)
ocussdbrowser_Smsc_Conn_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_Smsc_Conn_Canceled.setStatus(
        "current"
    )

ocussdbrowser_UssdgwConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 8)
)
ocussdbrowser_UssdgwConn.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_UssdgwConn.setStatus(
        "current"
    )

ocussdbrowser_UssdgwConn_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 9)
)
ocussdbrowser_UssdgwConn_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_UssdgwConn_Canceled.setStatus(
        "current"
    )

ocussdbrowser_SmppListener = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 10)
)
ocussdbrowser_SmppListener.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SmppListener.setStatus(
        "current"
    )

ocussdbrowser_SmppListener_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 11)
)
ocussdbrowser_SmppListener_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SmppListener_Canceled.setStatus(
        "current"
    )

ocussdbrowser_SmppClientConnectorDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 12)
)
ocussdbrowser_SmppClientConnectorDown.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SmppClientConnectorDown.setStatus(
        "current"
    )

ocussdbrowser_SmppClientConnectorDown_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 13)
)
ocussdbrowser_SmppClientConnectorDown_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SmppClientConnectorDown_Canceled.setStatus(
        "current"
    )

ocussdbrowser_SmppClients = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 14)
)
ocussdbrowser_SmppClients.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SmppClients.setStatus(
        "current"
    )

ocussdbrowser_SmppClients_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 15)
)
ocussdbrowser_SmppClients_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SmppClients_Canceled.setStatus(
        "current"
    )

ocussdbrowser_SmppClientsCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 16)
)
ocussdbrowser_SmppClientsCritical.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SmppClientsCritical.setStatus(
        "current"
    )

ocussdbrowser_SmppClientsCritical_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 17)
)
ocussdbrowser_SmppClientsCritical_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SmppClientsCritical_Canceled.setStatus(
        "current"
    )

ocussdbrowser_SmppClientsErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 18)
)
ocussdbrowser_SmppClientsErrors.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SmppClientsErrors.setStatus(
        "current"
    )

ocussdbrowser_SmppClientsErrors_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 19)
)
ocussdbrowser_SmppClientsErrors_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SmppClientsErrors_Canceled.setStatus(
        "current"
    )

ocussdbrowser_HttpConnector = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 20)
)
ocussdbrowser_HttpConnector.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_HttpConnector.setStatus(
        "current"
    )

ocussdbrowser_HttpConnector_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 21)
)
ocussdbrowser_HttpConnector_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_HttpConnector_Canceled.setStatus(
        "current"
    )

ocussdbrowser_HttpDedicatedUrl = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 22)
)
ocussdbrowser_HttpDedicatedUrl.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_HttpDedicatedUrl.setStatus(
        "current"
    )

ocussdbrowser_HttpDedicatedUrl_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 23)
)
ocussdbrowser_HttpDedicatedUrl_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_HttpDedicatedUrl_Canceled.setStatus(
        "current"
    )

ocussdbrowser_HttpListener = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 24)
)
ocussdbrowser_HttpListener.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_HttpListener.setStatus(
        "current"
    )

ocussdbrowser_HttpListener_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 25)
)
ocussdbrowser_HttpListener_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_HttpListener_Canceled.setStatus(
        "current"
    )

ocussdbrowser_IpcListener = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 26)
)
ocussdbrowser_IpcListener.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_IpcListener.setStatus(
        "current"
    )

ocussdbrowser_IpcListener_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 27)
)
ocussdbrowser_IpcListener_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_IpcListener_Canceled.setStatus(
        "current"
    )

ocussdbrowser_SoapListener = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 28)
)
ocussdbrowser_SoapListener.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SoapListener.setStatus(
        "current"
    )

ocussdbrowser_SoapListener_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 29)
)
ocussdbrowser_SoapListener_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_SoapListener_Canceled.setStatus(
        "current"
    )

ocussdbrowser_InvalidService = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 30)
)
ocussdbrowser_InvalidService.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_InvalidService.setStatus(
        "current"
    )

ocussdbrowser_InvalidService_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 31)
)
ocussdbrowser_InvalidService_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_InvalidService_Canceled.setStatus(
        "current"
    )

ocussdbrowser_MissingConnector = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 32)
)
ocussdbrowser_MissingConnector.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_MissingConnector.setStatus(
        "current"
    )

ocussdbrowser_MissingConnector_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 33)
)
ocussdbrowser_MissingConnector_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_MissingConnector_Canceled.setStatus(
        "current"
    )

ocussdbrowser_MissingService = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 34)
)
ocussdbrowser_MissingService.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_MissingService.setStatus(
        "current"
    )

ocussdbrowser_MissingService_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 1, 1, 0, 35)
)
ocussdbrowser_MissingService_Canceled.setObjects(
      *(("OPCD-USSDB-MIB-V2", "mcr_Host"),
        ("OPCD-USSDB-MIB-V2", "mcr_Severity"),
        ("OPCD-USSDB-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ocussdbrowser_MissingService_Canceled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPCD-USSDB-MIB-V2",
    **{"ocussdbrowser": ocussdbrowser,
       "ocussdbrowser-traps": ocussdbrowser_traps,
       "definitions": definitions,
       "ocussdbrowser-Restart": ocussdbrowser_Restart,
       "ocussdbrowser-Restart-Canceled": ocussdbrowser_Restart_Canceled,
       "ocussdbrowser-Crash": ocussdbrowser_Crash,
       "ocussdbrowser-Crash-Canceled": ocussdbrowser_Crash_Canceled,
       "ocussdbrowser-Smsc-Conn": ocussdbrowser_Smsc_Conn,
       "ocussdbrowser-Smsc-Conn-Canceled": ocussdbrowser_Smsc_Conn_Canceled,
       "ocussdbrowser-UssdgwConn": ocussdbrowser_UssdgwConn,
       "ocussdbrowser-UssdgwConn-Canceled": ocussdbrowser_UssdgwConn_Canceled,
       "ocussdbrowser-SmppListener": ocussdbrowser_SmppListener,
       "ocussdbrowser-SmppListener-Canceled": ocussdbrowser_SmppListener_Canceled,
       "ocussdbrowser-SmppClientConnectorDown": ocussdbrowser_SmppClientConnectorDown,
       "ocussdbrowser-SmppClientConnectorDown-Canceled": ocussdbrowser_SmppClientConnectorDown_Canceled,
       "ocussdbrowser-SmppClients": ocussdbrowser_SmppClients,
       "ocussdbrowser-SmppClients-Canceled": ocussdbrowser_SmppClients_Canceled,
       "ocussdbrowser-SmppClientsCritical": ocussdbrowser_SmppClientsCritical,
       "ocussdbrowser-SmppClientsCritical-Canceled": ocussdbrowser_SmppClientsCritical_Canceled,
       "ocussdbrowser-SmppClientsErrors": ocussdbrowser_SmppClientsErrors,
       "ocussdbrowser-SmppClientsErrors-Canceled": ocussdbrowser_SmppClientsErrors_Canceled,
       "ocussdbrowser-HttpConnector": ocussdbrowser_HttpConnector,
       "ocussdbrowser-HttpConnector-Canceled": ocussdbrowser_HttpConnector_Canceled,
       "ocussdbrowser-HttpDedicatedUrl": ocussdbrowser_HttpDedicatedUrl,
       "ocussdbrowser-HttpDedicatedUrl-Canceled": ocussdbrowser_HttpDedicatedUrl_Canceled,
       "ocussdbrowser-HttpListener": ocussdbrowser_HttpListener,
       "ocussdbrowser-HttpListener-Canceled": ocussdbrowser_HttpListener_Canceled,
       "ocussdbrowser-IpcListener": ocussdbrowser_IpcListener,
       "ocussdbrowser-IpcListener-Canceled": ocussdbrowser_IpcListener_Canceled,
       "ocussdbrowser-SoapListener": ocussdbrowser_SoapListener,
       "ocussdbrowser-SoapListener-Canceled": ocussdbrowser_SoapListener_Canceled,
       "ocussdbrowser-InvalidService": ocussdbrowser_InvalidService,
       "ocussdbrowser-InvalidService-Canceled": ocussdbrowser_InvalidService_Canceled,
       "ocussdbrowser-MissingConnector": ocussdbrowser_MissingConnector,
       "ocussdbrowser-MissingConnector-Canceled": ocussdbrowser_MissingConnector_Canceled,
       "ocussdbrowser-MissingService": ocussdbrowser_MissingService,
       "ocussdbrowser-MissingService-Canceled": ocussdbrowser_MissingService_Canceled,
       "vars": vars,
       "mcr-Host": mcr_Host,
       "mcr-Severity": mcr_Severity,
       "mcr-Text": mcr_Text}
)
