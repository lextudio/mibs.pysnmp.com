# SNMP MIB module (AGG-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AGG-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:56 2024
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
 file,
 host,
 mateHost,
 matePort,
 minutes,
 myHost,
 myPort,
 newFile,
 oldFile,
 pepName,
 port,
 reason,
 result,
 sbProducerHost,
 sbProducerPort,
 snName,
 unknownDeviceTrapContents) = mibBuilder.importSymbols(
    "AGGREGATED-EXT-MIB",
    "devName",
    "file",
    "host",
    "mateHost",
    "matePort",
    "minutes",
    "myHost",
    "myPort",
    "newFile",
    "oldFile",
    "pepName",
    "port",
    "reason",
    "result",
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
_MantraDevice_ObjectIdentity = ObjectIdentity
mantraDevice = _MantraDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198)
)

# Managed Objects groups


# Notification objects

unParsedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 5)
)
unParsedEvent.setObjects(
    ("AGGREGATED-EXT-MIB", "unknownDeviceTrapContents")
)
if mibBuilder.loadTexts:
    unParsedEvent.setStatus(
        "current"
    )

styxProducerConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 6)
)
styxProducerConnect.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "file"))
)
if mibBuilder.loadTexts:
    styxProducerConnect.setStatus(
        "current"
    )

styxProducerUnReadable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 7)
)
styxProducerUnReadable.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "file"))
)
if mibBuilder.loadTexts:
    styxProducerUnReadable.setStatus(
        "current"
    )

styxProducerDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 8)
)
styxProducerDisconnect.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "file"))
)
if mibBuilder.loadTexts:
    styxProducerDisconnect.setStatus(
        "current"
    )

styxProducerUnReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 9)
)
styxProducerUnReachable.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "host"),
        ("AGGREGATED-EXT-MIB", "port"),
        ("AGGREGATED-EXT-MIB", "file"),
        ("AGGREGATED-EXT-MIB", "minutes"))
)
if mibBuilder.loadTexts:
    styxProducerUnReachable.setStatus(
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

styxFTMateConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 11)
)
styxFTMateConnect.setObjects(
      *(("AGGREGATED-EXT-MIB", "snName"),
        ("AGGREGATED-EXT-MIB", "myHost"),
        ("AGGREGATED-EXT-MIB", "myPort"),
        ("AGGREGATED-EXT-MIB", "mateHost"),
        ("AGGREGATED-EXT-MIB", "matePort"))
)
if mibBuilder.loadTexts:
    styxFTMateConnect.setStatus(
        "current"
    )

styxFTMateDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 12)
)
styxFTMateDisconnect.setObjects(
      *(("AGGREGATED-EXT-MIB", "snName"),
        ("AGGREGATED-EXT-MIB", "myHost"),
        ("AGGREGATED-EXT-MIB", "myPort"),
        ("AGGREGATED-EXT-MIB", "mateHost"),
        ("AGGREGATED-EXT-MIB", "matePort"))
)
if mibBuilder.loadTexts:
    styxFTMateDisconnect.setStatus(
        "current"
    )

sBProducerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 13)
)
sBProducerUnreachable.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sBProducerUnreachable.setStatus(
        "current"
    )

sBProducerConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 14)
)
sBProducerConnected.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sBProducerConnected.setStatus(
        "current"
    )

sBProducerRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 15)
)
sBProducerRegistered.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sBProducerRegistered.setStatus(
        "current"
    )

sBProducerDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 16)
)
sBProducerDisconnected.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sBProducerDisconnected.setStatus(
        "current"
    )

sBProducerCannotRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 17)
)
sBProducerCannotRegister.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sBProducerCannotRegister.setStatus(
        "current"
    )

sBProducerCannotDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 18)
)
sBProducerCannotDisconnect.setObjects(
      *(("AGGREGATED-EXT-MIB", "pepName"),
        ("AGGREGATED-EXT-MIB", "devName"),
        ("AGGREGATED-EXT-MIB", "sbProducerHost"),
        ("AGGREGATED-EXT-MIB", "sbProducerPort"))
)
if mibBuilder.loadTexts:
    sBProducerCannotDisconnect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AGG-TRAP-MIB",
    **{"lucent": lucent,
       "products": products,
       "mantraDevice": mantraDevice,
       "mantraTraps": mantraTraps,
       "unParsedEvent": unParsedEvent,
       "styxProducerConnect": styxProducerConnect,
       "styxProducerUnReadable": styxProducerUnReadable,
       "styxProducerDisconnect": styxProducerDisconnect,
       "styxProducerUnReachable": styxProducerUnReachable,
       "logFileChanged": logFileChanged,
       "styxFTMateConnect": styxFTMateConnect,
       "styxFTMateDisconnect": styxFTMateDisconnect,
       "sBProducerUnreachable": sBProducerUnreachable,
       "sBProducerConnected": sBProducerConnected,
       "sBProducerRegistered": sBProducerRegistered,
       "sBProducerDisconnected": sBProducerDisconnected,
       "sBProducerCannotRegister": sBProducerCannotRegister,
       "sBProducerCannotDisconnect": sBProducerCannotDisconnect}
)
