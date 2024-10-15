# SNMP MIB module (CISCO-IETF-PW-ENET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-PW-ENET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:55 2024
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

(cpwVcIndex,) = mibBuilder.importSymbols(
    "CISCO-IETF-PW-MIB",
    "cpwVcIndex")

(CpwVcVlanCfg,) = mibBuilder.importSymbols(
    "CISCO-IETF-PW-TC-MIB",
    "CpwVcVlanCfg")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 experimental,
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
    "experimental",
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

cpwVcEnetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 108)
)
cpwVcEnetMIB.setRevisions(
        ("2002-09-22 12:00",
         "2002-08-20 12:00",
         "2002-02-03 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpwVcEnetNotifications_ObjectIdentity = ObjectIdentity
cpwVcEnetNotifications = _CpwVcEnetNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 0)
)
_CpwVcEnetObjects_ObjectIdentity = ObjectIdentity
cpwVcEnetObjects = _CpwVcEnetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1)
)
_CpwVcEnetTable_Object = MibTable
cpwVcEnetTable = _CpwVcEnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 1)
)
if mibBuilder.loadTexts:
    cpwVcEnetTable.setStatus("current")
_CpwVcEnetEntry_Object = MibTableRow
cpwVcEnetEntry = _CpwVcEnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 1, 1)
)
cpwVcEnetEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
    (0, "CISCO-IETF-PW-ENET-MIB", "cpwVcEnetPwVlan"),
)
if mibBuilder.loadTexts:
    cpwVcEnetEntry.setStatus("current")
_CpwVcEnetPwVlan_Type = CpwVcVlanCfg
_CpwVcEnetPwVlan_Object = MibTableColumn
cpwVcEnetPwVlan = _CpwVcEnetPwVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 1, 1, 1),
    _CpwVcEnetPwVlan_Type()
)
cpwVcEnetPwVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcEnetPwVlan.setStatus("current")


class _CpwVcEnetVlanMode_Type(Integer32):
    """Custom type cpwVcEnetVlanMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("addVlan", 4),
          ("changeVlan", 3),
          ("noChange", 2),
          ("other", 0),
          ("portBased", 1),
          ("removeVlan", 5))
    )


_CpwVcEnetVlanMode_Type.__name__ = "Integer32"
_CpwVcEnetVlanMode_Object = MibTableColumn
cpwVcEnetVlanMode = _CpwVcEnetVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 1, 1, 2),
    _CpwVcEnetVlanMode_Type()
)
cpwVcEnetVlanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcEnetVlanMode.setStatus("current")


class _CpwVcEnetPortVlan_Type(CpwVcVlanCfg):
    """Custom type cpwVcEnetPortVlan based on CpwVcVlanCfg"""
    defaultValue = 4097


_CpwVcEnetPortVlan_Object = MibTableColumn
cpwVcEnetPortVlan = _CpwVcEnetPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 1, 1, 3),
    _CpwVcEnetPortVlan_Type()
)
cpwVcEnetPortVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcEnetPortVlan.setStatus("current")
_CpwVcEnetVcIfIndex_Type = InterfaceIndexOrZero
_CpwVcEnetVcIfIndex_Object = MibTableColumn
cpwVcEnetVcIfIndex = _CpwVcEnetVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 1, 1, 4),
    _CpwVcEnetVcIfIndex_Type()
)
cpwVcEnetVcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcEnetVcIfIndex.setStatus("current")
_CpwVcEnetPortIfIndex_Type = InterfaceIndexOrZero
_CpwVcEnetPortIfIndex_Object = MibTableColumn
cpwVcEnetPortIfIndex = _CpwVcEnetPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 1, 1, 5),
    _CpwVcEnetPortIfIndex_Type()
)
cpwVcEnetPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcEnetPortIfIndex.setStatus("current")
_CpwVcEnetRowStatus_Type = RowStatus
_CpwVcEnetRowStatus_Object = MibTableColumn
cpwVcEnetRowStatus = _CpwVcEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 1, 1, 6),
    _CpwVcEnetRowStatus_Type()
)
cpwVcEnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcEnetRowStatus.setStatus("current")
_CpwVcEnetStorageType_Type = StorageType
_CpwVcEnetStorageType_Object = MibTableColumn
cpwVcEnetStorageType = _CpwVcEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 1, 1, 7),
    _CpwVcEnetStorageType_Type()
)
cpwVcEnetStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcEnetStorageType.setStatus("current")
_CpwVcEnetMplsPriMappingTable_Object = MibTable
cpwVcEnetMplsPriMappingTable = _CpwVcEnetMplsPriMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 2)
)
if mibBuilder.loadTexts:
    cpwVcEnetMplsPriMappingTable.setStatus("current")
_CpwVcEnetMplsPriMappingTableEntry_Object = MibTableRow
cpwVcEnetMplsPriMappingTableEntry = _CpwVcEnetMplsPriMappingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 2, 1)
)
cpwVcEnetMplsPriMappingTableEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcEnetMplsPriMappingTableEntry.setStatus("current")


class _CpwVcEnetMplsPriMapping_Type(Bits):
    """Custom type cpwVcEnetMplsPriMapping based on Bits"""
    namedValues = NamedValues(
        *(("pri000", 0),
          ("pri001", 1),
          ("pri010", 2),
          ("pri011", 3),
          ("pri100", 4),
          ("pri101", 5),
          ("pri110", 6),
          ("pri111", 7),
          ("untagged", 8))
    )

_CpwVcEnetMplsPriMapping_Type.__name__ = "Bits"
_CpwVcEnetMplsPriMapping_Object = MibTableColumn
cpwVcEnetMplsPriMapping = _CpwVcEnetMplsPriMapping_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 2, 1, 1),
    _CpwVcEnetMplsPriMapping_Type()
)
cpwVcEnetMplsPriMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcEnetMplsPriMapping.setStatus("current")
_CpwVcEnetMplsPriMappingRowStatus_Type = RowStatus
_CpwVcEnetMplsPriMappingRowStatus_Object = MibTableColumn
cpwVcEnetMplsPriMappingRowStatus = _CpwVcEnetMplsPriMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 2, 1, 2),
    _CpwVcEnetMplsPriMappingRowStatus_Type()
)
cpwVcEnetMplsPriMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcEnetMplsPriMappingRowStatus.setStatus("current")
_CpwVcEnetMplsPriMappingStorageType_Type = StorageType
_CpwVcEnetMplsPriMappingStorageType_Object = MibTableColumn
cpwVcEnetMplsPriMappingStorageType = _CpwVcEnetMplsPriMappingStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 2, 1, 3),
    _CpwVcEnetMplsPriMappingStorageType_Type()
)
cpwVcEnetMplsPriMappingStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcEnetMplsPriMappingStorageType.setStatus("current")
_CpwVcEnetStatsTable_Object = MibTable
cpwVcEnetStatsTable = _CpwVcEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 3)
)
if mibBuilder.loadTexts:
    cpwVcEnetStatsTable.setStatus("current")
_CpwVcEnetStatsEntry_Object = MibTableRow
cpwVcEnetStatsEntry = _CpwVcEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 3, 1)
)
cpwVcEnetStatsEntry.setIndexNames(
    (0, "CISCO-IETF-PW-MIB", "cpwVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcEnetStatsEntry.setStatus("current")
_CpwVcEnetStatsIllegalVlan_Type = Counter64
_CpwVcEnetStatsIllegalVlan_Object = MibTableColumn
cpwVcEnetStatsIllegalVlan = _CpwVcEnetStatsIllegalVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 3, 1, 1),
    _CpwVcEnetStatsIllegalVlan_Type()
)
cpwVcEnetStatsIllegalVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcEnetStatsIllegalVlan.setStatus("current")
_CpwVcEnetStatsIllegalLength_Type = Counter64
_CpwVcEnetStatsIllegalLength_Object = MibTableColumn
cpwVcEnetStatsIllegalLength = _CpwVcEnetStatsIllegalLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 1, 3, 1, 2),
    _CpwVcEnetStatsIllegalLength_Type()
)
cpwVcEnetStatsIllegalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcEnetStatsIllegalLength.setStatus("current")
_CpwVcEnetConformance_ObjectIdentity = ObjectIdentity
cpwVcEnetConformance = _CpwVcEnetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 2)
)
_CpwVcEnetGroups_ObjectIdentity = ObjectIdentity
cpwVcEnetGroups = _CpwVcEnetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 2, 1)
)
_CpwVcEnetCompliances_ObjectIdentity = ObjectIdentity
cpwVcEnetCompliances = _CpwVcEnetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 2, 2)
)

# Managed Objects groups

cpwVcEnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 2, 1, 1)
)
cpwVcEnetGroup.setObjects(
      *(("CISCO-IETF-PW-ENET-MIB", "cpwVcEnetVlanMode"),
        ("CISCO-IETF-PW-ENET-MIB", "cpwVcEnetPortVlan"),
        ("CISCO-IETF-PW-ENET-MIB", "cpwVcEnetPortIfIndex"),
        ("CISCO-IETF-PW-ENET-MIB", "cpwVcEnetVcIfIndex"),
        ("CISCO-IETF-PW-ENET-MIB", "cpwVcEnetRowStatus"),
        ("CISCO-IETF-PW-ENET-MIB", "cpwVcEnetStorageType"))
)
if mibBuilder.loadTexts:
    cpwVcEnetGroup.setStatus("current")

cpwVcStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 2, 1, 2)
)
cpwVcStatsGroup.setObjects(
      *(("CISCO-IETF-PW-ENET-MIB", "cpwVcEnetStatsIllegalVlan"),
        ("CISCO-IETF-PW-ENET-MIB", "cpwVcEnetStatsIllegalLength"))
)
if mibBuilder.loadTexts:
    cpwVcStatsGroup.setStatus("current")

cpwVcEnetMplsPriGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 2, 1, 3)
)
cpwVcEnetMplsPriGroup.setObjects(
      *(("CISCO-IETF-PW-ENET-MIB", "cpwVcEnetMplsPriMapping"),
        ("CISCO-IETF-PW-ENET-MIB", "cpwVcEnetMplsPriMappingRowStatus"),
        ("CISCO-IETF-PW-ENET-MIB", "cpwVcEnetMplsPriMappingStorageType"))
)
if mibBuilder.loadTexts:
    cpwVcEnetMplsPriGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cpwVcEnetModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 108, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpwVcEnetModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-PW-ENET-MIB",
    **{"cpwVcEnetMIB": cpwVcEnetMIB,
       "cpwVcEnetNotifications": cpwVcEnetNotifications,
       "cpwVcEnetObjects": cpwVcEnetObjects,
       "cpwVcEnetTable": cpwVcEnetTable,
       "cpwVcEnetEntry": cpwVcEnetEntry,
       "cpwVcEnetPwVlan": cpwVcEnetPwVlan,
       "cpwVcEnetVlanMode": cpwVcEnetVlanMode,
       "cpwVcEnetPortVlan": cpwVcEnetPortVlan,
       "cpwVcEnetVcIfIndex": cpwVcEnetVcIfIndex,
       "cpwVcEnetPortIfIndex": cpwVcEnetPortIfIndex,
       "cpwVcEnetRowStatus": cpwVcEnetRowStatus,
       "cpwVcEnetStorageType": cpwVcEnetStorageType,
       "cpwVcEnetMplsPriMappingTable": cpwVcEnetMplsPriMappingTable,
       "cpwVcEnetMplsPriMappingTableEntry": cpwVcEnetMplsPriMappingTableEntry,
       "cpwVcEnetMplsPriMapping": cpwVcEnetMplsPriMapping,
       "cpwVcEnetMplsPriMappingRowStatus": cpwVcEnetMplsPriMappingRowStatus,
       "cpwVcEnetMplsPriMappingStorageType": cpwVcEnetMplsPriMappingStorageType,
       "cpwVcEnetStatsTable": cpwVcEnetStatsTable,
       "cpwVcEnetStatsEntry": cpwVcEnetStatsEntry,
       "cpwVcEnetStatsIllegalVlan": cpwVcEnetStatsIllegalVlan,
       "cpwVcEnetStatsIllegalLength": cpwVcEnetStatsIllegalLength,
       "cpwVcEnetConformance": cpwVcEnetConformance,
       "cpwVcEnetGroups": cpwVcEnetGroups,
       "cpwVcEnetGroup": cpwVcEnetGroup,
       "cpwVcStatsGroup": cpwVcStatsGroup,
       "cpwVcEnetMplsPriGroup": cpwVcEnetMplsPriGroup,
       "cpwVcEnetCompliances": cpwVcEnetCompliances,
       "cpwVcEnetModuleCompliance": cpwVcEnetModuleCompliance}
)
