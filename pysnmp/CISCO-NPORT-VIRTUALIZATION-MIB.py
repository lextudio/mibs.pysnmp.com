# SNMP MIB module (CISCO-NPORT-VIRTUALIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NPORT-VIRTUALIZATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:17 2024
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

(InterfaceIndexList,) = mibBuilder.importSymbols(
    "CISCO-IF-EXTENSION-MIB",
    "InterfaceIndexList")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoNportVirtualizationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 660)
)
ciscoNportVirtualizationMIB.setRevisions(
        ("2008-06-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoNportVirtualizationMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoNportVirtualizationMIBNotifs = _CiscoNportVirtualizationMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 0)
)
_CiscoNportVirtualizationMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNportVirtualizationMIBObjects = _CiscoNportVirtualizationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1)
)
_CnpvConfiguration_ObjectIdentity = ObjectIdentity
cnpvConfiguration = _CnpvConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1, 1)
)
_CnpvGlobal_ObjectIdentity = ObjectIdentity
cnpvGlobal = _CnpvGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1, 1, 1)
)
_CnpvTrafficAutoLoadbalance_Type = TruthValue
_CnpvTrafficAutoLoadbalance_Object = MibScalar
cnpvTrafficAutoLoadbalance = _CnpvTrafficAutoLoadbalance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1, 1, 1, 1),
    _CnpvTrafficAutoLoadbalance_Type()
)
cnpvTrafficAutoLoadbalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnpvTrafficAutoLoadbalance.setStatus("current")
_CnpvTrafficMap_ObjectIdentity = ObjectIdentity
cnpvTrafficMap = _CnpvTrafficMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1, 1, 2)
)
_CnpvTrafficMapTable_Object = MibTable
cnpvTrafficMapTable = _CnpvTrafficMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cnpvTrafficMapTable.setStatus("current")
_CnpvTrafficMapEntry_Object = MibTableRow
cnpvTrafficMapEntry = _CnpvTrafficMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1, 1, 2, 1, 1)
)
cnpvTrafficMapEntry.setIndexNames(
    (0, "CISCO-NPORT-VIRTUALIZATION-MIB", "cnpvTrafficMapFromIfIndex"),
)
if mibBuilder.loadTexts:
    cnpvTrafficMapEntry.setStatus("current")
_CnpvTrafficMapFromIfIndex_Type = InterfaceIndex
_CnpvTrafficMapFromIfIndex_Object = MibTableColumn
cnpvTrafficMapFromIfIndex = _CnpvTrafficMapFromIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1, 1, 2, 1, 1, 1),
    _CnpvTrafficMapFromIfIndex_Type()
)
cnpvTrafficMapFromIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnpvTrafficMapFromIfIndex.setStatus("current")


class _CnpvTrafficMapToIfIndexList_Type(InterfaceIndexList):
    """Custom type cnpvTrafficMapToIfIndexList based on InterfaceIndexList"""
    subtypeSpec = InterfaceIndexList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 256),
    )


_CnpvTrafficMapToIfIndexList_Type.__name__ = "InterfaceIndexList"
_CnpvTrafficMapToIfIndexList_Object = MibTableColumn
cnpvTrafficMapToIfIndexList = _CnpvTrafficMapToIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1, 1, 2, 1, 1, 2),
    _CnpvTrafficMapToIfIndexList_Type()
)
cnpvTrafficMapToIfIndexList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpvTrafficMapToIfIndexList.setStatus("current")
_CnpvTrafficMapLastChange_Type = TimeStamp
_CnpvTrafficMapLastChange_Object = MibTableColumn
cnpvTrafficMapLastChange = _CnpvTrafficMapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1, 1, 2, 1, 1, 3),
    _CnpvTrafficMapLastChange_Type()
)
cnpvTrafficMapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnpvTrafficMapLastChange.setStatus("current")


class _CnpvTrafficMapStorageType_Type(StorageType):
    """Custom type cnpvTrafficMapStorageType based on StorageType"""


_CnpvTrafficMapStorageType_Object = MibTableColumn
cnpvTrafficMapStorageType = _CnpvTrafficMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1, 1, 2, 1, 1, 4),
    _CnpvTrafficMapStorageType_Type()
)
cnpvTrafficMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpvTrafficMapStorageType.setStatus("current")
_CnpvTrafficMapRowStatus_Type = RowStatus
_CnpvTrafficMapRowStatus_Object = MibTableColumn
cnpvTrafficMapRowStatus = _CnpvTrafficMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 1, 1, 2, 1, 1, 5),
    _CnpvTrafficMapRowStatus_Type()
)
cnpvTrafficMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnpvTrafficMapRowStatus.setStatus("current")
_CiscoNportVirtualizationMIBConform_ObjectIdentity = ObjectIdentity
ciscoNportVirtualizationMIBConform = _CiscoNportVirtualizationMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 2)
)
_CiscoNportVirtualizationMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoNportVirtualizationMIBCompliances = _CiscoNportVirtualizationMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 2, 1)
)
_CiscoNportVirtualizationMIBGroups_ObjectIdentity = ObjectIdentity
ciscoNportVirtualizationMIBGroups = _CiscoNportVirtualizationMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 2, 2)
)

# Managed Objects groups

cnpvTrafficMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 2, 2, 1)
)
cnpvTrafficMapGroup.setObjects(
      *(("CISCO-NPORT-VIRTUALIZATION-MIB", "cnpvTrafficAutoLoadbalance"),
        ("CISCO-NPORT-VIRTUALIZATION-MIB", "cnpvTrafficMapToIfIndexList"),
        ("CISCO-NPORT-VIRTUALIZATION-MIB", "cnpvTrafficMapStorageType"),
        ("CISCO-NPORT-VIRTUALIZATION-MIB", "cnpvTrafficMapRowStatus"),
        ("CISCO-NPORT-VIRTUALIZATION-MIB", "cnpvTrafficMapLastChange"))
)
if mibBuilder.loadTexts:
    cnpvTrafficMapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoNportVirtualizationMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 660, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoNportVirtualizationMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NPORT-VIRTUALIZATION-MIB",
    **{"ciscoNportVirtualizationMIB": ciscoNportVirtualizationMIB,
       "ciscoNportVirtualizationMIBNotifs": ciscoNportVirtualizationMIBNotifs,
       "ciscoNportVirtualizationMIBObjects": ciscoNportVirtualizationMIBObjects,
       "cnpvConfiguration": cnpvConfiguration,
       "cnpvGlobal": cnpvGlobal,
       "cnpvTrafficAutoLoadbalance": cnpvTrafficAutoLoadbalance,
       "cnpvTrafficMap": cnpvTrafficMap,
       "cnpvTrafficMapTable": cnpvTrafficMapTable,
       "cnpvTrafficMapEntry": cnpvTrafficMapEntry,
       "cnpvTrafficMapFromIfIndex": cnpvTrafficMapFromIfIndex,
       "cnpvTrafficMapToIfIndexList": cnpvTrafficMapToIfIndexList,
       "cnpvTrafficMapLastChange": cnpvTrafficMapLastChange,
       "cnpvTrafficMapStorageType": cnpvTrafficMapStorageType,
       "cnpvTrafficMapRowStatus": cnpvTrafficMapRowStatus,
       "ciscoNportVirtualizationMIBConform": ciscoNportVirtualizationMIBConform,
       "ciscoNportVirtualizationMIBCompliances": ciscoNportVirtualizationMIBCompliances,
       "ciscoNportVirtualizationMIBCompliance": ciscoNportVirtualizationMIBCompliance,
       "ciscoNportVirtualizationMIBGroups": ciscoNportVirtualizationMIBGroups,
       "cnpvTrafficMapGroup": cnpvTrafficMapGroup}
)
