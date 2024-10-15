# SNMP MIB module (ETHER-WIS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ETHER-WIS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:56 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(sonetFarEndLineStuff2,
 sonetFarEndPathStuff2,
 sonetLineStuff2,
 sonetMediumCircuitIdentifier,
 sonetMediumLineCoding,
 sonetMediumLineType,
 sonetMediumLoopbackConfig,
 sonetMediumStuff2,
 sonetMediumType,
 sonetPathCurrentWidth,
 sonetPathStuff2,
 sonetSESthresholdSet,
 sonetSectionStuff2) = mibBuilder.importSymbols(
    "SONET-MIB",
    "sonetFarEndLineStuff2",
    "sonetFarEndPathStuff2",
    "sonetLineStuff2",
    "sonetMediumCircuitIdentifier",
    "sonetMediumLineCoding",
    "sonetMediumLineType",
    "sonetMediumLoopbackConfig",
    "sonetMediumStuff2",
    "sonetMediumType",
    "sonetPathCurrentWidth",
    "sonetPathStuff2",
    "sonetSESthresholdSet",
    "sonetSectionStuff2")


# MODULE-IDENTITY

etherWisMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 134)
)
etherWisMIB.setRevisions(
        ("2003-09-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtherWisObjects_ObjectIdentity = ObjectIdentity
etherWisObjects = _EtherWisObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 134, 1)
)
_EtherWisDevice_ObjectIdentity = ObjectIdentity
etherWisDevice = _EtherWisDevice_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 134, 1, 1)
)
_EtherWisDeviceTable_Object = MibTable
etherWisDeviceTable = _EtherWisDeviceTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etherWisDeviceTable.setStatus("current")
_EtherWisDeviceEntry_Object = MibTableRow
etherWisDeviceEntry = _EtherWisDeviceEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 1, 1, 1, 1)
)
etherWisDeviceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etherWisDeviceEntry.setStatus("current")


class _EtherWisDeviceTxTestPatternMode_Type(Integer32):
    """Custom type etherWisDeviceTxTestPatternMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mixedFrequency", 4),
          ("none", 1),
          ("prbs31", 3),
          ("squareWave", 2))
    )


_EtherWisDeviceTxTestPatternMode_Type.__name__ = "Integer32"
_EtherWisDeviceTxTestPatternMode_Object = MibTableColumn
etherWisDeviceTxTestPatternMode = _EtherWisDeviceTxTestPatternMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 1, 1, 1, 1, 1),
    _EtherWisDeviceTxTestPatternMode_Type()
)
etherWisDeviceTxTestPatternMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherWisDeviceTxTestPatternMode.setStatus("current")


class _EtherWisDeviceRxTestPatternMode_Type(Integer32):
    """Custom type etherWisDeviceRxTestPatternMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mixedFrequency", 4),
          ("none", 1),
          ("prbs31", 3))
    )


_EtherWisDeviceRxTestPatternMode_Type.__name__ = "Integer32"
_EtherWisDeviceRxTestPatternMode_Object = MibTableColumn
etherWisDeviceRxTestPatternMode = _EtherWisDeviceRxTestPatternMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 1, 1, 1, 1, 2),
    _EtherWisDeviceRxTestPatternMode_Type()
)
etherWisDeviceRxTestPatternMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherWisDeviceRxTestPatternMode.setStatus("current")


class _EtherWisDeviceRxTestPatternErrors_Type(Gauge32):
    """Custom type etherWisDeviceRxTestPatternErrors based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtherWisDeviceRxTestPatternErrors_Type.__name__ = "Gauge32"
_EtherWisDeviceRxTestPatternErrors_Object = MibTableColumn
etherWisDeviceRxTestPatternErrors = _EtherWisDeviceRxTestPatternErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 1, 1, 1, 1, 3),
    _EtherWisDeviceRxTestPatternErrors_Type()
)
etherWisDeviceRxTestPatternErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherWisDeviceRxTestPatternErrors.setStatus("current")
_EtherWisSection_ObjectIdentity = ObjectIdentity
etherWisSection = _EtherWisSection_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 134, 1, 2)
)
_EtherWisSectionCurrentTable_Object = MibTable
etherWisSectionCurrentTable = _EtherWisSectionCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etherWisSectionCurrentTable.setStatus("current")
_EtherWisSectionCurrentEntry_Object = MibTableRow
etherWisSectionCurrentEntry = _EtherWisSectionCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 1, 2, 1, 1)
)
etherWisSectionCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etherWisSectionCurrentEntry.setStatus("current")


class _EtherWisSectionCurrentJ0Transmitted_Type(OctetString):
    """Custom type etherWisSectionCurrentJ0Transmitted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EtherWisSectionCurrentJ0Transmitted_Type.__name__ = "OctetString"
_EtherWisSectionCurrentJ0Transmitted_Object = MibTableColumn
etherWisSectionCurrentJ0Transmitted = _EtherWisSectionCurrentJ0Transmitted_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 1, 2, 1, 1, 1),
    _EtherWisSectionCurrentJ0Transmitted_Type()
)
etherWisSectionCurrentJ0Transmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherWisSectionCurrentJ0Transmitted.setStatus("current")


class _EtherWisSectionCurrentJ0Received_Type(OctetString):
    """Custom type etherWisSectionCurrentJ0Received based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EtherWisSectionCurrentJ0Received_Type.__name__ = "OctetString"
_EtherWisSectionCurrentJ0Received_Object = MibTableColumn
etherWisSectionCurrentJ0Received = _EtherWisSectionCurrentJ0Received_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 1, 2, 1, 1, 2),
    _EtherWisSectionCurrentJ0Received_Type()
)
etherWisSectionCurrentJ0Received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherWisSectionCurrentJ0Received.setStatus("current")
_EtherWisObjectsPath_ObjectIdentity = ObjectIdentity
etherWisObjectsPath = _EtherWisObjectsPath_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 134, 2)
)
_EtherWisPath_ObjectIdentity = ObjectIdentity
etherWisPath = _EtherWisPath_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 134, 2, 1)
)
_EtherWisPathCurrentTable_Object = MibTable
etherWisPathCurrentTable = _EtherWisPathCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etherWisPathCurrentTable.setStatus("current")
_EtherWisPathCurrentEntry_Object = MibTableRow
etherWisPathCurrentEntry = _EtherWisPathCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 2, 1, 1, 1)
)
etherWisPathCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etherWisPathCurrentEntry.setStatus("current")


class _EtherWisPathCurrentStatus_Type(Bits):
    """Custom type etherWisPathCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("etherWisPathAIS", 1),
          ("etherWisPathLCD", 3),
          ("etherWisPathLOP", 0),
          ("etherWisPathPLM", 2))
    )

_EtherWisPathCurrentStatus_Type.__name__ = "Bits"
_EtherWisPathCurrentStatus_Object = MibTableColumn
etherWisPathCurrentStatus = _EtherWisPathCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 2, 1, 1, 1, 1),
    _EtherWisPathCurrentStatus_Type()
)
etherWisPathCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherWisPathCurrentStatus.setStatus("current")


class _EtherWisPathCurrentJ1Transmitted_Type(OctetString):
    """Custom type etherWisPathCurrentJ1Transmitted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EtherWisPathCurrentJ1Transmitted_Type.__name__ = "OctetString"
_EtherWisPathCurrentJ1Transmitted_Object = MibTableColumn
etherWisPathCurrentJ1Transmitted = _EtherWisPathCurrentJ1Transmitted_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 2, 1, 1, 1, 2),
    _EtherWisPathCurrentJ1Transmitted_Type()
)
etherWisPathCurrentJ1Transmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherWisPathCurrentJ1Transmitted.setStatus("current")


class _EtherWisPathCurrentJ1Received_Type(OctetString):
    """Custom type etherWisPathCurrentJ1Received based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EtherWisPathCurrentJ1Received_Type.__name__ = "OctetString"
_EtherWisPathCurrentJ1Received_Object = MibTableColumn
etherWisPathCurrentJ1Received = _EtherWisPathCurrentJ1Received_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 2, 1, 1, 1, 3),
    _EtherWisPathCurrentJ1Received_Type()
)
etherWisPathCurrentJ1Received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherWisPathCurrentJ1Received.setStatus("current")
_EtherWisFarEndPath_ObjectIdentity = ObjectIdentity
etherWisFarEndPath = _EtherWisFarEndPath_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 134, 2, 2)
)
_EtherWisFarEndPathCurrentTable_Object = MibTable
etherWisFarEndPathCurrentTable = _EtherWisFarEndPathCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etherWisFarEndPathCurrentTable.setStatus("current")
_EtherWisFarEndPathCurrentEntry_Object = MibTableRow
etherWisFarEndPathCurrentEntry = _EtherWisFarEndPathCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 2, 2, 1, 1)
)
etherWisFarEndPathCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etherWisFarEndPathCurrentEntry.setStatus("current")


class _EtherWisFarEndPathCurrentStatus_Type(Bits):
    """Custom type etherWisFarEndPathCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("etherWisFarEndPayloadDefect", 0),
          ("etherWisFarEndServerDefect", 1))
    )

_EtherWisFarEndPathCurrentStatus_Type.__name__ = "Bits"
_EtherWisFarEndPathCurrentStatus_Object = MibTableColumn
etherWisFarEndPathCurrentStatus = _EtherWisFarEndPathCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 134, 2, 2, 1, 1, 1),
    _EtherWisFarEndPathCurrentStatus_Type()
)
etherWisFarEndPathCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherWisFarEndPathCurrentStatus.setStatus("current")
_EtherWisConformance_ObjectIdentity = ObjectIdentity
etherWisConformance = _EtherWisConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 134, 3)
)
_EtherWisGroups_ObjectIdentity = ObjectIdentity
etherWisGroups = _EtherWisGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 134, 3, 1)
)
_EtherWisCompliances_ObjectIdentity = ObjectIdentity
etherWisCompliances = _EtherWisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 134, 3, 2)
)

# Managed Objects groups

etherWisDeviceGroupBasic = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 134, 3, 1, 1)
)
etherWisDeviceGroupBasic.setObjects(
      *(("ETHER-WIS", "etherWisDeviceTxTestPatternMode"),
        ("ETHER-WIS", "etherWisDeviceRxTestPatternMode"))
)
if mibBuilder.loadTexts:
    etherWisDeviceGroupBasic.setStatus("current")

etherWisDeviceGroupExtra = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 134, 3, 1, 2)
)
etherWisDeviceGroupExtra.setObjects(
    ("ETHER-WIS", "etherWisDeviceRxTestPatternErrors")
)
if mibBuilder.loadTexts:
    etherWisDeviceGroupExtra.setStatus("current")

etherWisSectionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 134, 3, 1, 3)
)
etherWisSectionGroup.setObjects(
      *(("ETHER-WIS", "etherWisSectionCurrentJ0Transmitted"),
        ("ETHER-WIS", "etherWisSectionCurrentJ0Received"))
)
if mibBuilder.loadTexts:
    etherWisSectionGroup.setStatus("current")

etherWisPathGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 134, 3, 1, 4)
)
etherWisPathGroup.setObjects(
      *(("ETHER-WIS", "etherWisPathCurrentStatus"),
        ("ETHER-WIS", "etherWisPathCurrentJ1Transmitted"),
        ("ETHER-WIS", "etherWisPathCurrentJ1Received"))
)
if mibBuilder.loadTexts:
    etherWisPathGroup.setStatus("current")

etherWisFarEndPathGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 134, 3, 1, 5)
)
etherWisFarEndPathGroup.setObjects(
    ("ETHER-WIS", "etherWisFarEndPathCurrentStatus")
)
if mibBuilder.loadTexts:
    etherWisFarEndPathGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etherWisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 134, 3, 2, 1)
)
if mibBuilder.loadTexts:
    etherWisCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ETHER-WIS",
    **{"etherWisMIB": etherWisMIB,
       "etherWisObjects": etherWisObjects,
       "etherWisDevice": etherWisDevice,
       "etherWisDeviceTable": etherWisDeviceTable,
       "etherWisDeviceEntry": etherWisDeviceEntry,
       "etherWisDeviceTxTestPatternMode": etherWisDeviceTxTestPatternMode,
       "etherWisDeviceRxTestPatternMode": etherWisDeviceRxTestPatternMode,
       "etherWisDeviceRxTestPatternErrors": etherWisDeviceRxTestPatternErrors,
       "etherWisSection": etherWisSection,
       "etherWisSectionCurrentTable": etherWisSectionCurrentTable,
       "etherWisSectionCurrentEntry": etherWisSectionCurrentEntry,
       "etherWisSectionCurrentJ0Transmitted": etherWisSectionCurrentJ0Transmitted,
       "etherWisSectionCurrentJ0Received": etherWisSectionCurrentJ0Received,
       "etherWisObjectsPath": etherWisObjectsPath,
       "etherWisPath": etherWisPath,
       "etherWisPathCurrentTable": etherWisPathCurrentTable,
       "etherWisPathCurrentEntry": etherWisPathCurrentEntry,
       "etherWisPathCurrentStatus": etherWisPathCurrentStatus,
       "etherWisPathCurrentJ1Transmitted": etherWisPathCurrentJ1Transmitted,
       "etherWisPathCurrentJ1Received": etherWisPathCurrentJ1Received,
       "etherWisFarEndPath": etherWisFarEndPath,
       "etherWisFarEndPathCurrentTable": etherWisFarEndPathCurrentTable,
       "etherWisFarEndPathCurrentEntry": etherWisFarEndPathCurrentEntry,
       "etherWisFarEndPathCurrentStatus": etherWisFarEndPathCurrentStatus,
       "etherWisConformance": etherWisConformance,
       "etherWisGroups": etherWisGroups,
       "etherWisDeviceGroupBasic": etherWisDeviceGroupBasic,
       "etherWisDeviceGroupExtra": etherWisDeviceGroupExtra,
       "etherWisSectionGroup": etherWisSectionGroup,
       "etherWisPathGroup": etherWisPathGroup,
       "etherWisFarEndPathGroup": etherWisFarEndPathGroup,
       "etherWisCompliances": etherWisCompliances,
       "etherWisCompliance": etherWisCompliance}
)
