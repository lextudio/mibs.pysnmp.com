# SNMP MIB module (CISCO-IF-LOOPBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IF-LOOPBACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:12 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoIfLoopbackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399)
)
ciscoIfLoopbackMIB.setRevisions(
        ("2001-11-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIfLoopbackMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIfLoopbackMIBObjects = _CiscoIfLoopbackMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1)
)
_CiscoIfLoopbackConfig_ObjectIdentity = ObjectIdentity
ciscoIfLoopbackConfig = _CiscoIfLoopbackConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1)
)
_CifLConfTable_Object = MibTable
cifLConfTable = _CifLConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cifLConfTable.setStatus("current")
_CifLConfEntry_Object = MibTableRow
cifLConfEntry = _CifLConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1)
)
cifLConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cifLConfEntry.setStatus("current")


class _CifLLoopback_Type(Integer32):
    """Custom type cifLLoopback based on Integer32"""
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
        *(("farEndLineLoopback", 1),
          ("farEndPayloadLoopback", 2),
          ("localLoopback", 5),
          ("remoteLineLoopback", 3),
          ("remotePayloadLoopback", 4))
    )


_CifLLoopback_Type.__name__ = "Integer32"
_CifLLoopback_Object = MibTableColumn
cifLLoopback = _CifLLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 1),
    _CifLLoopback_Type()
)
cifLLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifLLoopback.setStatus("current")


class _CifLLoopbackStatus_Type(Integer32):
    """Custom type cifLLoopbackStatus based on Integer32"""
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
        *(("clockOutOfSync", 3),
          ("completed", 1),
          ("failed", 4),
          ("inProgress", 2))
    )


_CifLLoopbackStatus_Type.__name__ = "Integer32"
_CifLLoopbackStatus_Object = MibTableColumn
cifLLoopbackStatus = _CifLLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 2),
    _CifLLoopbackStatus_Type()
)
cifLLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifLLoopbackStatus.setStatus("current")


class _CifLFELoopbackDeviceAndCode_Type(Integer32):
    """Custom type cifLFELoopbackDeviceAndCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("latchCSU", 8),
          ("latchDS0Drop", 5),
          ("latchDS0Line", 6),
          ("latchDSU", 9),
          ("latchHL96", 10),
          ("latchOCU", 7),
          ("lineInband", 12),
          ("lineLoopbackESF", 13),
          ("lineLoopbackFEAC", 16),
          ("noCode", 15),
          ("nonLatchCSU", 3),
          ("nonLatchDSU", 4),
          ("nonLatchOCUwith1", 1),
          ("nonLatchOCUwithout1", 2),
          ("payloadLoopbackESF", 14),
          ("smartJackInband", 17),
          ("v54PN127Polynomial", 11))
    )


_CifLFELoopbackDeviceAndCode_Type.__name__ = "Integer32"
_CifLFELoopbackDeviceAndCode_Object = MibTableColumn
cifLFELoopbackDeviceAndCode = _CifLFELoopbackDeviceAndCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 3),
    _CifLFELoopbackDeviceAndCode_Type()
)
cifLFELoopbackDeviceAndCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifLFELoopbackDeviceAndCode.setStatus("current")
_CifLRowStatus_Type = RowStatus
_CifLRowStatus_Object = MibTableColumn
cifLRowStatus = _CifLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 4),
    _CifLRowStatus_Type()
)
cifLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifLRowStatus.setStatus("current")
_CiscoIfLoopbackMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIfLoopbackMIBConformance = _CiscoIfLoopbackMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 8)
)
_CiscoIfLoopbackMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIfLoopbackMIBCompliances = _CiscoIfLoopbackMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 1)
)
_CiscoIfLoopbackMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIfLoopbackMIBGroups = _CiscoIfLoopbackMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 2)
)

# Managed Objects groups

ciscoIfLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 2, 1)
)
ciscoIfLoopbackGroup.setObjects(
      *(("CISCO-IF-LOOPBACK-MIB", "cifLLoopback"),
        ("CISCO-IF-LOOPBACK-MIB", "cifLLoopbackStatus"),
        ("CISCO-IF-LOOPBACK-MIB", "cifLFELoopbackDeviceAndCode"),
        ("CISCO-IF-LOOPBACK-MIB", "cifLRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIfLoopbackGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIfLoopbackMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIfLoopbackMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IF-LOOPBACK-MIB",
    **{"ciscoIfLoopbackMIB": ciscoIfLoopbackMIB,
       "ciscoIfLoopbackMIBObjects": ciscoIfLoopbackMIBObjects,
       "ciscoIfLoopbackConfig": ciscoIfLoopbackConfig,
       "cifLConfTable": cifLConfTable,
       "cifLConfEntry": cifLConfEntry,
       "cifLLoopback": cifLLoopback,
       "cifLLoopbackStatus": cifLLoopbackStatus,
       "cifLFELoopbackDeviceAndCode": cifLFELoopbackDeviceAndCode,
       "cifLRowStatus": cifLRowStatus,
       "ciscoIfLoopbackMIBConformance": ciscoIfLoopbackMIBConformance,
       "ciscoIfLoopbackMIBCompliances": ciscoIfLoopbackMIBCompliances,
       "ciscoIfLoopbackMIBCompliance": ciscoIfLoopbackMIBCompliance,
       "ciscoIfLoopbackMIBGroups": ciscoIfLoopbackMIBGroups,
       "ciscoIfLoopbackGroup": ciscoIfLoopbackGroup}
)
