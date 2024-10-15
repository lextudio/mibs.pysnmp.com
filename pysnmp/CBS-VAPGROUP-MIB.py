# SNMP MIB module (CBS-VAPGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CBS-VAPGROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:47 2024
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

(ModuleState,
 cbsHwModuleID) = mibBuilder.importSymbols(
    "CBS-HARDWARE-MIB",
    "ModuleState",
    "cbsHwModuleID")

(cbsMIBs,
 cbsMgmt,
 cbsTraps) = mibBuilder.importSymbols(
    "CROSSBEAM-SYSTEMS-MIB",
    "cbsMIBs",
    "cbsMgmt",
    "cbsTraps")

(KBytes,
 ProductID) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "KBytes",
    "ProductID")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cbsVapGroupsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 3, 4)
)
cbsVapGroupsMIB.setRevisions(
        ("2008-09-02 00:00",
         "2009-12-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CbsVapGroups_ObjectIdentity = ObjectIdentity
cbsVapGroups = _CbsVapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4)
)
_CbsVapGroupTable_Object = MibTable
cbsVapGroupTable = _CbsVapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cbsVapGroupTable.setStatus("current")
_CbsVapGroupEntry_Object = MibTableRow
cbsVapGroupEntry = _CbsVapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1)
)
cbsVapGroupEntry.setIndexNames(
    (0, "CBS-VAPGROUP-MIB", "cbsVgVapGroupID"),
)
if mibBuilder.loadTexts:
    cbsVapGroupEntry.setStatus("current")


class _CbsVgVapGroupID_Type(Integer32):
    """Custom type cbsVgVapGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CbsVgVapGroupID_Type.__name__ = "Integer32"
_CbsVgVapGroupID_Object = MibTableColumn
cbsVgVapGroupID = _CbsVgVapGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 1),
    _CbsVgVapGroupID_Type()
)
cbsVgVapGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgVapGroupID.setStatus("current")
_CbsVgVapGroupName_Type = DisplayString
_CbsVgVapGroupName_Object = MibTableColumn
cbsVgVapGroupName = _CbsVgVapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 2),
    _CbsVgVapGroupName_Type()
)
cbsVgVapGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgVapGroupName.setStatus("current")
_CbsVgLoadPriority_Type = Integer32
_CbsVgLoadPriority_Object = MibTableColumn
cbsVgLoadPriority = _CbsVgLoadPriority_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 3),
    _CbsVgLoadPriority_Type()
)
cbsVgLoadPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgLoadPriority.setStatus("current")
_CbsVgPreempPriority_Type = Integer32
_CbsVgPreempPriority_Object = MibTableColumn
cbsVgPreempPriority = _CbsVgPreempPriority_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 4),
    _CbsVgPreempPriority_Type()
)
cbsVgPreempPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgPreempPriority.setStatus("current")
_CbsVgApmList_Type = DisplayString
_CbsVgApmList_Object = MibTableColumn
cbsVgApmList = _CbsVgApmList_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 5),
    _CbsVgApmList_Type()
)
cbsVgApmList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgApmList.setStatus("current")
_CbsVgVapCount_Type = Integer32
_CbsVgVapCount_Object = MibTableColumn
cbsVgVapCount = _CbsVgVapCount_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 6),
    _CbsVgVapCount_Type()
)
cbsVgVapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgVapCount.setStatus("current")
_CbsVgMaxLoadCount_Type = Integer32
_CbsVgMaxLoadCount_Object = MibTableColumn
cbsVgMaxLoadCount = _CbsVgMaxLoadCount_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 7),
    _CbsVgMaxLoadCount_Type()
)
cbsVgMaxLoadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgMaxLoadCount.setStatus("current")
_CbsVgLBList_Type = DisplayString
_CbsVgLBList_Object = MibTableColumn
cbsVgLBList = _CbsVgLBList_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 8),
    _CbsVgLBList_Type()
)
cbsVgLBList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgLBList.setStatus("current")


class _CbsVgBackUpMode_Type(Integer32):
    """Custom type cbsVgBackUpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 2),
          ("none", 0),
          ("pair", 1))
    )


_CbsVgBackUpMode_Type.__name__ = "Integer32"
_CbsVgBackUpMode_Object = MibTableColumn
cbsVgBackUpMode = _CbsVgBackUpMode_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 9),
    _CbsVgBackUpMode_Type()
)
cbsVgBackUpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgBackUpMode.setStatus("current")
_CbsVgIpForward_Type = TruthValue
_CbsVgIpForward_Object = MibTableColumn
cbsVgIpForward = _CbsVgIpForward_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 10),
    _CbsVgIpForward_Type()
)
cbsVgIpForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgIpForward.setStatus("current")
_CbsVgRpFilter_Type = TruthValue
_CbsVgRpFilter_Object = MibTableColumn
cbsVgRpFilter = _CbsVgRpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 11),
    _CbsVgRpFilter_Type()
)
cbsVgRpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgRpFilter.setStatus("current")
_CbsVgLogMartians_Type = TruthValue
_CbsVgLogMartians_Object = MibTableColumn
cbsVgLogMartians = _CbsVgLogMartians_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 12),
    _CbsVgLogMartians_Type()
)
cbsVgLogMartians.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgLogMartians.setStatus("current")
_CbsVgReloadTimer_Type = Integer32
_CbsVgReloadTimer_Object = MibTableColumn
cbsVgReloadTimer = _CbsVgReloadTimer_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 13),
    _CbsVgReloadTimer_Type()
)
cbsVgReloadTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgReloadTimer.setStatus("current")
_CbsVgRemoteBoxBackup_Type = TruthValue
_CbsVgRemoteBoxBackup_Object = MibTableColumn
cbsVgRemoteBoxBackup = _CbsVgRemoteBoxBackup_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 14),
    _CbsVgRemoteBoxBackup_Type()
)
cbsVgRemoteBoxBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgRemoteBoxBackup.setStatus("obsolete")
_CbsVgDelayFlow_Type = Integer32
_CbsVgDelayFlow_Object = MibTableColumn
cbsVgDelayFlow = _CbsVgDelayFlow_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 15),
    _CbsVgDelayFlow_Type()
)
cbsVgDelayFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgDelayFlow.setStatus("current")
_CbsVgIpv6Forward_Type = TruthValue
_CbsVgIpv6Forward_Object = MibTableColumn
cbsVgIpv6Forward = _CbsVgIpv6Forward_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 1, 1, 16),
    _CbsVgIpv6Forward_Type()
)
cbsVgIpv6Forward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVgIpv6Forward.setStatus("current")
_CbsVapMappingTable_Object = MibTable
cbsVapMappingTable = _CbsVapMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 2)
)
if mibBuilder.loadTexts:
    cbsVapMappingTable.setStatus("current")
_CbsVapMappingEntry_Object = MibTableRow
cbsVapMappingEntry = _CbsVapMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1)
)
cbsVapMappingEntry.setIndexNames(
    (0, "CBS-VAPGROUP-MIB", "cbsVmVapGroupID"),
    (0, "CBS-VAPGROUP-MIB", "cbsVmVapIndex"),
)
if mibBuilder.loadTexts:
    cbsVapMappingEntry.setStatus("current")


class _CbsVmVapGroupID_Type(Integer32):
    """Custom type cbsVmVapGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CbsVmVapGroupID_Type.__name__ = "Integer32"
_CbsVmVapGroupID_Object = MibTableColumn
cbsVmVapGroupID = _CbsVmVapGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 1),
    _CbsVmVapGroupID_Type()
)
cbsVmVapGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVmVapGroupID.setStatus("current")
_CbsVmVapGroupName_Type = DisplayString
_CbsVmVapGroupName_Object = MibTableColumn
cbsVmVapGroupName = _CbsVmVapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 2),
    _CbsVmVapGroupName_Type()
)
cbsVmVapGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVmVapGroupName.setStatus("current")
_CbsVmVapName_Type = DisplayString
_CbsVmVapName_Object = MibTableColumn
cbsVmVapName = _CbsVmVapName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 3),
    _CbsVmVapName_Type()
)
cbsVmVapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVmVapName.setStatus("current")


class _CbsVmVapIndex_Type(Integer32):
    """Custom type cbsVmVapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CbsVmVapIndex_Type.__name__ = "Integer32"
_CbsVmVapIndex_Object = MibTableColumn
cbsVmVapIndex = _CbsVmVapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 4),
    _CbsVmVapIndex_Type()
)
cbsVmVapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVmVapIndex.setStatus("current")
_CbsVmVapStatus_Type = ModuleState
_CbsVmVapStatus_Object = MibTableColumn
cbsVmVapStatus = _CbsVmVapStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 5),
    _CbsVmVapStatus_Type()
)
cbsVmVapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVmVapStatus.setStatus("current")
_CbsVmSlotNumber_Type = Integer32
_CbsVmSlotNumber_Object = MibTableColumn
cbsVmSlotNumber = _CbsVmSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 4, 2, 1, 6),
    _CbsVmSlotNumber_Type()
)
cbsVmSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVmSlotNumber.setStatus("current")
_CbsVapGroupsTraps_ObjectIdentity = ObjectIdentity
cbsVapGroupsTraps = _CbsVapGroupsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 4, 3)
)

# Managed Objects groups


# Notification objects

cbsVapStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 3, 1)
)
cbsVapStatusChanged.setObjects(
      *(("CBS-VAPGROUP-MIB", "cbsVmVapStatus"),
        ("CBS-VAPGROUP-MIB", "cbsVmVapName"))
)
if mibBuilder.loadTexts:
    cbsVapStatusChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CBS-VAPGROUP-MIB",
    **{"cbsVapGroups": cbsVapGroups,
       "cbsVapGroupTable": cbsVapGroupTable,
       "cbsVapGroupEntry": cbsVapGroupEntry,
       "cbsVgVapGroupID": cbsVgVapGroupID,
       "cbsVgVapGroupName": cbsVgVapGroupName,
       "cbsVgLoadPriority": cbsVgLoadPriority,
       "cbsVgPreempPriority": cbsVgPreempPriority,
       "cbsVgApmList": cbsVgApmList,
       "cbsVgVapCount": cbsVgVapCount,
       "cbsVgMaxLoadCount": cbsVgMaxLoadCount,
       "cbsVgLBList": cbsVgLBList,
       "cbsVgBackUpMode": cbsVgBackUpMode,
       "cbsVgIpForward": cbsVgIpForward,
       "cbsVgRpFilter": cbsVgRpFilter,
       "cbsVgLogMartians": cbsVgLogMartians,
       "cbsVgReloadTimer": cbsVgReloadTimer,
       "cbsVgRemoteBoxBackup": cbsVgRemoteBoxBackup,
       "cbsVgDelayFlow": cbsVgDelayFlow,
       "cbsVgIpv6Forward": cbsVgIpv6Forward,
       "cbsVapMappingTable": cbsVapMappingTable,
       "cbsVapMappingEntry": cbsVapMappingEntry,
       "cbsVmVapGroupID": cbsVmVapGroupID,
       "cbsVmVapGroupName": cbsVmVapGroupName,
       "cbsVmVapName": cbsVmVapName,
       "cbsVmVapIndex": cbsVmVapIndex,
       "cbsVmVapStatus": cbsVmVapStatus,
       "cbsVmSlotNumber": cbsVmSlotNumber,
       "cbsVapGroupsMIB": cbsVapGroupsMIB,
       "cbsVapGroupsTraps": cbsVapGroupsTraps,
       "cbsVapStatusChanged": cbsVapStatusChanged}
)
