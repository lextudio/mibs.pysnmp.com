# SNMP MIB module (CISCO-FABRICPATH-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FABRICPATH-TOPOLOGY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:10 2024
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

(Cisco2KVlanList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Cisco2KVlanList")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoFabricPathTopologyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 801)
)
ciscoFabricPathTopologyMIB.setRevisions(
        ("2013-03-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFabricPathTopologyMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFabricPathTopologyMIBNotifs = _CiscoFabricPathTopologyMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 0)
)
_CiscoFabricPathTopologyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFabricPathTopologyMIBObjects = _CiscoFabricPathTopologyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1)
)
_CfptTopologyTable_Object = MibTable
cfptTopologyTable = _CfptTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1)
)
if mibBuilder.loadTexts:
    cfptTopologyTable.setStatus("current")
_CfptTopologyEntry_Object = MibTableRow
cfptTopologyEntry = _CfptTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1)
)
cfptTopologyEntry.setIndexNames(
    (0, "CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIndex"),
)
if mibBuilder.loadTexts:
    cfptTopologyEntry.setStatus("current")
_CfptTopologyIndex_Type = Unsigned32
_CfptTopologyIndex_Object = MibTableColumn
cfptTopologyIndex = _CfptTopologyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 1),
    _CfptTopologyIndex_Type()
)
cfptTopologyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfptTopologyIndex.setStatus("current")
_CfptTopologyDescr_Type = SnmpAdminString
_CfptTopologyDescr_Object = MibTableColumn
cfptTopologyDescr = _CfptTopologyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 2),
    _CfptTopologyDescr_Type()
)
cfptTopologyDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfptTopologyDescr.setStatus("current")


class _CfptTopologyState_Type(Integer32):
    """Custom type cfptTopologyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_CfptTopologyState_Type.__name__ = "Integer32"
_CfptTopologyState_Object = MibTableColumn
cfptTopologyState = _CfptTopologyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 3),
    _CfptTopologyState_Type()
)
cfptTopologyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyState.setStatus("current")
_CfptTopologyStateChangeReason_Type = SnmpAdminString
_CfptTopologyStateChangeReason_Object = MibTableColumn
cfptTopologyStateChangeReason = _CfptTopologyStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 4),
    _CfptTopologyStateChangeReason_Type()
)
cfptTopologyStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyStateChangeReason.setStatus("current")
_CfptTopologyVlansFirst2K_Type = Cisco2KVlanList
_CfptTopologyVlansFirst2K_Object = MibTableColumn
cfptTopologyVlansFirst2K = _CfptTopologyVlansFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 5),
    _CfptTopologyVlansFirst2K_Type()
)
cfptTopologyVlansFirst2K.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfptTopologyVlansFirst2K.setStatus("current")
_CfptTopologyVlansSecond2K_Type = Cisco2KVlanList
_CfptTopologyVlansSecond2K_Object = MibTableColumn
cfptTopologyVlansSecond2K = _CfptTopologyVlansSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 6),
    _CfptTopologyVlansSecond2K_Type()
)
cfptTopologyVlansSecond2K.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfptTopologyVlansSecond2K.setStatus("current")
_CfptTopologyActiveVlansFirst2K_Type = Cisco2KVlanList
_CfptTopologyActiveVlansFirst2K_Object = MibTableColumn
cfptTopologyActiveVlansFirst2K = _CfptTopologyActiveVlansFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 7),
    _CfptTopologyActiveVlansFirst2K_Type()
)
cfptTopologyActiveVlansFirst2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyActiveVlansFirst2K.setStatus("current")
_CfptTopologyActiveVlansSecond2K_Type = Cisco2KVlanList
_CfptTopologyActiveVlansSecond2K_Object = MibTableColumn
cfptTopologyActiveVlansSecond2K = _CfptTopologyActiveVlansSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 8),
    _CfptTopologyActiveVlansSecond2K_Type()
)
cfptTopologyActiveVlansSecond2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyActiveVlansSecond2K.setStatus("current")


class _CfptTopologyStorageType_Type(StorageType):
    """Custom type cfptTopologyStorageType based on StorageType"""


_CfptTopologyStorageType_Object = MibTableColumn
cfptTopologyStorageType = _CfptTopologyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 9),
    _CfptTopologyStorageType_Type()
)
cfptTopologyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfptTopologyStorageType.setStatus("current")
_CfptTopologyRowStatus_Type = RowStatus
_CfptTopologyRowStatus_Object = MibTableColumn
cfptTopologyRowStatus = _CfptTopologyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 1, 1, 10),
    _CfptTopologyRowStatus_Type()
)
cfptTopologyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfptTopologyRowStatus.setStatus("current")
_CfptTopologyIfTable_Object = MibTable
cfptTopologyIfTable = _CfptTopologyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2)
)
if mibBuilder.loadTexts:
    cfptTopologyIfTable.setStatus("current")
_CfptTopologyIfEntry_Object = MibTableRow
cfptTopologyIfEntry = _CfptTopologyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2, 1)
)
cfptTopologyIfEntry.setIndexNames(
    (0, "CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfTopoIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfptTopologyIfEntry.setStatus("current")
_CfptTopologyIfTopoIndex_Type = Unsigned32
_CfptTopologyIfTopoIndex_Object = MibTableColumn
cfptTopologyIfTopoIndex = _CfptTopologyIfTopoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2, 1, 1),
    _CfptTopologyIfTopoIndex_Type()
)
cfptTopologyIfTopoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfptTopologyIfTopoIndex.setStatus("current")


class _CfptTopologyIfState_Type(Integer32):
    """Custom type cfptTopologyIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_CfptTopologyIfState_Type.__name__ = "Integer32"
_CfptTopologyIfState_Object = MibTableColumn
cfptTopologyIfState = _CfptTopologyIfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2, 1, 2),
    _CfptTopologyIfState_Type()
)
cfptTopologyIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyIfState.setStatus("current")


class _CfptTopologyIfStorageType_Type(StorageType):
    """Custom type cfptTopologyIfStorageType based on StorageType"""


_CfptTopologyIfStorageType_Object = MibTableColumn
cfptTopologyIfStorageType = _CfptTopologyIfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2, 1, 3),
    _CfptTopologyIfStorageType_Type()
)
cfptTopologyIfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfptTopologyIfStorageType.setStatus("current")
_CfptTopologyIfRowStatus_Type = RowStatus
_CfptTopologyIfRowStatus_Object = MibTableColumn
cfptTopologyIfRowStatus = _CfptTopologyIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 2, 1, 4),
    _CfptTopologyIfRowStatus_Type()
)
cfptTopologyIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfptTopologyIfRowStatus.setStatus("current")
_CfptTopologyIfVlanTable_Object = MibTable
cfptTopologyIfVlanTable = _CfptTopologyIfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3)
)
if mibBuilder.loadTexts:
    cfptTopologyIfVlanTable.setStatus("current")
_CfptTopologyIfVlanEntry_Object = MibTableRow
cfptTopologyIfVlanEntry = _CfptTopologyIfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3, 1)
)
cfptTopologyIfVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfptTopologyIfVlanEntry.setStatus("current")
_CfptTopologyIfVlansFirst2K_Type = Cisco2KVlanList
_CfptTopologyIfVlansFirst2K_Object = MibTableColumn
cfptTopologyIfVlansFirst2K = _CfptTopologyIfVlansFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3, 1, 1),
    _CfptTopologyIfVlansFirst2K_Type()
)
cfptTopologyIfVlansFirst2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyIfVlansFirst2K.setStatus("current")
_CfptTopologyIfVlansSecond2K_Type = Cisco2KVlanList
_CfptTopologyIfVlansSecond2K_Object = MibTableColumn
cfptTopologyIfVlansSecond2K = _CfptTopologyIfVlansSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3, 1, 2),
    _CfptTopologyIfVlansSecond2K_Type()
)
cfptTopologyIfVlansSecond2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyIfVlansSecond2K.setStatus("current")
_CfptTopologyIfActiveVlansFirst2K_Type = Cisco2KVlanList
_CfptTopologyIfActiveVlansFirst2K_Object = MibTableColumn
cfptTopologyIfActiveVlansFirst2K = _CfptTopologyIfActiveVlansFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3, 1, 3),
    _CfptTopologyIfActiveVlansFirst2K_Type()
)
cfptTopologyIfActiveVlansFirst2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyIfActiveVlansFirst2K.setStatus("current")
_CfptTopologyIfActiveVlansSecond2K_Type = Cisco2KVlanList
_CfptTopologyIfActiveVlansSecond2K_Object = MibTableColumn
cfptTopologyIfActiveVlansSecond2K = _CfptTopologyIfActiveVlansSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 3, 1, 4),
    _CfptTopologyIfActiveVlansSecond2K_Type()
)
cfptTopologyIfActiveVlansSecond2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyIfActiveVlansSecond2K.setStatus("current")
_CfptTopologyTreeTable_Object = MibTable
cfptTopologyTreeTable = _CfptTopologyTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4)
)
if mibBuilder.loadTexts:
    cfptTopologyTreeTable.setStatus("current")
_CfptTopologyTreeEntry_Object = MibTableRow
cfptTopologyTreeEntry = _CfptTopologyTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4, 1)
)
cfptTopologyTreeEntry.setIndexNames(
    (0, "CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIndex"),
    (0, "CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyTreeId"),
)
if mibBuilder.loadTexts:
    cfptTopologyTreeEntry.setStatus("current")
_CfptTopologyTreeId_Type = Unsigned32
_CfptTopologyTreeId_Object = MibTableColumn
cfptTopologyTreeId = _CfptTopologyTreeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4, 1, 1),
    _CfptTopologyTreeId_Type()
)
cfptTopologyTreeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfptTopologyTreeId.setStatus("current")
_CfptTopologyTreeFtag_Type = Unsigned32
_CfptTopologyTreeFtag_Object = MibTableColumn
cfptTopologyTreeFtag = _CfptTopologyTreeFtag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4, 1, 2),
    _CfptTopologyTreeFtag_Type()
)
cfptTopologyTreeFtag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyTreeFtag.setStatus("current")


class _CfptTopologyTreeState_Type(Integer32):
    """Custom type cfptTopologyTreeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("other", 1))
    )


_CfptTopologyTreeState_Type.__name__ = "Integer32"
_CfptTopologyTreeState_Object = MibTableColumn
cfptTopologyTreeState = _CfptTopologyTreeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4, 1, 3),
    _CfptTopologyTreeState_Type()
)
cfptTopologyTreeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyTreeState.setStatus("current")


class _CfptTopologyTreeType_Type(Integer32):
    """Custom type cfptTopologyTreeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 2),
          ("multicast", 3),
          ("other", 1))
    )


_CfptTopologyTreeType_Type.__name__ = "Integer32"
_CfptTopologyTreeType_Object = MibTableColumn
cfptTopologyTreeType = _CfptTopologyTreeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 1, 4, 1, 4),
    _CfptTopologyTreeType_Type()
)
cfptTopologyTreeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfptTopologyTreeType.setStatus("current")
_CiscoFabricPathTopologyMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFabricPathTopologyMIBConformance = _CiscoFabricPathTopologyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 2)
)
_CfptFabricPathTopologyMIBCompliances_ObjectIdentity = ObjectIdentity
cfptFabricPathTopologyMIBCompliances = _CfptFabricPathTopologyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 1)
)
_CfptFabricPathTopologyMIBGroups_ObjectIdentity = ObjectIdentity
cfptFabricPathTopologyMIBGroups = _CfptFabricPathTopologyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 2)
)

# Managed Objects groups

cfptTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 2, 1)
)
cfptTopologyGroup.setObjects(
      *(("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyDescr"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyState"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyStateChangeReason"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyVlansFirst2K"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyVlansSecond2K"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyActiveVlansFirst2K"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyActiveVlansSecond2K"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyStorageType"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyRowStatus"))
)
if mibBuilder.loadTexts:
    cfptTopologyGroup.setStatus("current")

cfptTopologyIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 2, 2)
)
cfptTopologyIfGroup.setObjects(
      *(("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfState"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfStorageType"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfRowStatus"))
)
if mibBuilder.loadTexts:
    cfptTopologyIfGroup.setStatus("current")

cfptTopologyIfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 2, 3)
)
cfptTopologyIfVlanGroup.setObjects(
      *(("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfVlansFirst2K"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfVlansSecond2K"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfActiveVlansFirst2K"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyIfActiveVlansSecond2K"))
)
if mibBuilder.loadTexts:
    cfptTopologyIfVlanGroup.setStatus("current")

cfptTopologyTreeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 2, 4)
)
cfptTopologyTreeGroup.setObjects(
      *(("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyTreeFtag"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyTreeState"),
        ("CISCO-FABRICPATH-TOPOLOGY-MIB", "cfptTopologyTreeType"))
)
if mibBuilder.loadTexts:
    cfptTopologyTreeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cfptFabricPathTopologyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 801, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cfptFabricPathTopologyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FABRICPATH-TOPOLOGY-MIB",
    **{"ciscoFabricPathTopologyMIB": ciscoFabricPathTopologyMIB,
       "ciscoFabricPathTopologyMIBNotifs": ciscoFabricPathTopologyMIBNotifs,
       "ciscoFabricPathTopologyMIBObjects": ciscoFabricPathTopologyMIBObjects,
       "cfptTopologyTable": cfptTopologyTable,
       "cfptTopologyEntry": cfptTopologyEntry,
       "cfptTopologyIndex": cfptTopologyIndex,
       "cfptTopologyDescr": cfptTopologyDescr,
       "cfptTopologyState": cfptTopologyState,
       "cfptTopologyStateChangeReason": cfptTopologyStateChangeReason,
       "cfptTopologyVlansFirst2K": cfptTopologyVlansFirst2K,
       "cfptTopologyVlansSecond2K": cfptTopologyVlansSecond2K,
       "cfptTopologyActiveVlansFirst2K": cfptTopologyActiveVlansFirst2K,
       "cfptTopologyActiveVlansSecond2K": cfptTopologyActiveVlansSecond2K,
       "cfptTopologyStorageType": cfptTopologyStorageType,
       "cfptTopologyRowStatus": cfptTopologyRowStatus,
       "cfptTopologyIfTable": cfptTopologyIfTable,
       "cfptTopologyIfEntry": cfptTopologyIfEntry,
       "cfptTopologyIfTopoIndex": cfptTopologyIfTopoIndex,
       "cfptTopologyIfState": cfptTopologyIfState,
       "cfptTopologyIfStorageType": cfptTopologyIfStorageType,
       "cfptTopologyIfRowStatus": cfptTopologyIfRowStatus,
       "cfptTopologyIfVlanTable": cfptTopologyIfVlanTable,
       "cfptTopologyIfVlanEntry": cfptTopologyIfVlanEntry,
       "cfptTopologyIfVlansFirst2K": cfptTopologyIfVlansFirst2K,
       "cfptTopologyIfVlansSecond2K": cfptTopologyIfVlansSecond2K,
       "cfptTopologyIfActiveVlansFirst2K": cfptTopologyIfActiveVlansFirst2K,
       "cfptTopologyIfActiveVlansSecond2K": cfptTopologyIfActiveVlansSecond2K,
       "cfptTopologyTreeTable": cfptTopologyTreeTable,
       "cfptTopologyTreeEntry": cfptTopologyTreeEntry,
       "cfptTopologyTreeId": cfptTopologyTreeId,
       "cfptTopologyTreeFtag": cfptTopologyTreeFtag,
       "cfptTopologyTreeState": cfptTopologyTreeState,
       "cfptTopologyTreeType": cfptTopologyTreeType,
       "ciscoFabricPathTopologyMIBConformance": ciscoFabricPathTopologyMIBConformance,
       "cfptFabricPathTopologyMIBCompliances": cfptFabricPathTopologyMIBCompliances,
       "cfptFabricPathTopologyMIBCompliance": cfptFabricPathTopologyMIBCompliance,
       "cfptFabricPathTopologyMIBGroups": cfptFabricPathTopologyMIBGroups,
       "cfptTopologyGroup": cfptTopologyGroup,
       "cfptTopologyIfGroup": cfptTopologyIfGroup,
       "cfptTopologyIfVlanGroup": cfptTopologyIfVlanGroup,
       "cfptTopologyTreeGroup": cfptTopologyTreeGroup}
)
