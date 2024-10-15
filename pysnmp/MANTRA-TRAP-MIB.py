# SNMP MIB module (MANTRA-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MANTRA-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:01 2024
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

(devName,
 deviceType,
 domain,
 file,
 group,
 host,
 mateHost,
 matePort,
 minutes,
 myHost,
 myPort,
 name,
 newFile,
 oldFile,
 pepName,
 port,
 reason,
 result,
 runStatus,
 sbProducerHost,
 sbProducerPort,
 snName,
 unknownDeviceTrapContents) = mibBuilder.importSymbols(
    "AGGREGATED-EXT-MIB",
    "devName",
    "deviceType",
    "domain",
    "file",
    "group",
    "host",
    "mateHost",
    "matePort",
    "minutes",
    "myHost",
    "myPort",
    "name",
    "newFile",
    "oldFile",
    "pepName",
    "port",
    "reason",
    "result",
    "runStatus",
    "sbProducerHost",
    "sbProducerPort",
    "snName",
    "unknownDeviceTrapContents")

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
 ObjectName,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "ObjectName",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mantraTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_SoftSwitch_ObjectIdentity = ObjectIdentity
softSwitch = _SoftSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198)
)

# Managed Objects groups


# Notification objects

lssProcessUnstartable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 0)
)
lssProcessUnstartable.setObjects(
      *(("AGGREGATED-EXT-MIB", "deviceType"),
        ("AGGREGATED-EXT-MIB", "domain"),
        ("AGGREGATED-EXT-MIB", "group"),
        ("AGGREGATED-EXT-MIB", "name"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "runStatus"))
)
if mibBuilder.loadTexts:
    lssProcessUnstartable.setStatus(
        "current"
    )

lssProcessCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 1)
)
lssProcessCreated.setObjects(
      *(("AGGREGATED-EXT-MIB", "deviceType"),
        ("AGGREGATED-EXT-MIB", "domain"),
        ("AGGREGATED-EXT-MIB", "group"),
        ("AGGREGATED-EXT-MIB", "name"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "runStatus"))
)
if mibBuilder.loadTexts:
    lssProcessCreated.setStatus(
        "current"
    )

lssProcessDied = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 2)
)
lssProcessDied.setObjects(
      *(("AGGREGATED-EXT-MIB", "deviceType"),
        ("AGGREGATED-EXT-MIB", "domain"),
        ("AGGREGATED-EXT-MIB", "group"),
        ("AGGREGATED-EXT-MIB", "name"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "runStatus"))
)
if mibBuilder.loadTexts:
    lssProcessDied.setStatus(
        "current"
    )

lssProcessKilled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 3)
)
lssProcessKilled.setObjects(
      *(("AGGREGATED-EXT-MIB", "deviceType"),
        ("AGGREGATED-EXT-MIB", "domain"),
        ("AGGREGATED-EXT-MIB", "group"),
        ("AGGREGATED-EXT-MIB", "name"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "runStatus"))
)
if mibBuilder.loadTexts:
    lssProcessKilled.setStatus(
        "current"
    )

lssProcessStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 4)
)
lssProcessStateChange.setObjects(
      *(("AGGREGATED-EXT-MIB", "deviceType"),
        ("AGGREGATED-EXT-MIB", "domain"),
        ("AGGREGATED-EXT-MIB", "group"),
        ("AGGREGATED-EXT-MIB", "name"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "runStatus"))
)
if mibBuilder.loadTexts:
    lssProcessStateChange.setStatus(
        "current"
    )

lssInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 5)
)
lssInternalError.setObjects(
    ("AGGREGATED-EXT-MIB", "unknownDeviceTrapContents")
)
if mibBuilder.loadTexts:
    lssInternalError.setStatus(
        "current"
    )

lssElementSuccessfulConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 6)
)
lssElementSuccessfulConnection.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "file"))
)
if mibBuilder.loadTexts:
    lssElementSuccessfulConnection.setStatus(
        "current"
    )

lssElementFileUnReadable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 7)
)
lssElementFileUnReadable.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "file"))
)
if mibBuilder.loadTexts:
    lssElementFileUnReadable.setStatus(
        "current"
    )

lssElementDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 8)
)
lssElementDisconnect.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "file"))
)
if mibBuilder.loadTexts:
    lssElementDisconnect.setStatus(
        "current"
    )

lssElementUnReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 9)
)
lssElementUnReachable.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "file"),
        ("AGGREGATED-EXT-MIB", "minutes"))
)
if mibBuilder.loadTexts:
    lssElementUnReachable.setStatus(
        "current"
    )

logFileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 10)
)
logFileChanged.setObjects(
      *(("AGGREGATED-EXT-MIB", "oldFile"),
        ("AGGREGATED-EXT-MIB", "newFile"),
        ("AGGREGATED-EXT-MIB", "result"),
        ("AGGREGATED-EXT-MIB", "reason"))
)
if mibBuilder.loadTexts:
    logFileChanged.setStatus(
        "current"
    )

lssFTMateConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 11)
)
lssFTMateConnect.setObjects(
      *(("AGGREGATED-EXT-MIB", "snName"),
        ("AGGREGATED-EXT-MIB", "myHost"),
        ("AGGREGATED-EXT-MIB", "myPort"),
        ("AGGREGATED-EXT-MIB", "mateHost"),
        ("AGGREGATED-EXT-MIB", "matePort"))
)
if mibBuilder.loadTexts:
    lssFTMateConnect.setStatus(
        "current"
    )

lssFTMateDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 12)
)
lssFTMateDisconnect.setObjects(
      *(("AGGREGATED-EXT-MIB", "snName"),
        ("AGGREGATED-EXT-MIB", "myHost"),
        ("AGGREGATED-EXT-MIB", "myPort"),
        ("AGGREGATED-EXT-MIB", "mateHost"),
        ("AGGREGATED-EXT-MIB", "matePort"))
)
if mibBuilder.loadTexts:
    lssFTMateDisconnect.setStatus(
        "current"
    )

sbProducerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 13)
)
sbProducerUnreachable.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sbProducerUnreachable.setStatus(
        "current"
    )

sbProducerConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 14)
)
sbProducerConnected.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sbProducerConnected.setStatus(
        "current"
    )

sbProducerRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 15)
)
sbProducerRegistered.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sbProducerRegistered.setStatus(
        "current"
    )

sbProducerDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 16)
)
sbProducerDisconnected.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sbProducerDisconnected.setStatus(
        "current"
    )

sbProducerCannotRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 17)
)
sbProducerCannotRegister.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sbProducerCannotRegister.setStatus(
        "current"
    )

sbProducerCannotDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 18)
)
sbProducerCannotDisconnect.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sbProducerCannotDisconnect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MANTRA-TRAP-MIB",
    **{"lucent": lucent,
       "products": products,
       "softSwitch": softSwitch,
       "mantraTraps": mantraTraps,
       "lssProcessUnstartable": lssProcessUnstartable,
       "lssProcessCreated": lssProcessCreated,
       "lssProcessDied": lssProcessDied,
       "lssProcessKilled": lssProcessKilled,
       "lssProcessStateChange": lssProcessStateChange,
       "lssInternalError": lssInternalError,
       "lssElementSuccessfulConnection": lssElementSuccessfulConnection,
       "lssElementFileUnReadable": lssElementFileUnReadable,
       "lssElementDisconnect": lssElementDisconnect,
       "lssElementUnReachable": lssElementUnReachable,
       "logFileChanged": logFileChanged,
       "lssFTMateConnect": lssFTMateConnect,
       "lssFTMateDisconnect": lssFTMateDisconnect,
       "sbProducerUnreachable": sbProducerUnreachable,
       "sbProducerConnected": sbProducerConnected,
       "sbProducerRegistered": sbProducerRegistered,
       "sbProducerDisconnected": sbProducerDisconnected,
       "sbProducerCannotRegister": sbProducerCannotRegister,
       "sbProducerCannotDisconnect": sbProducerCannotDisconnect}
)
