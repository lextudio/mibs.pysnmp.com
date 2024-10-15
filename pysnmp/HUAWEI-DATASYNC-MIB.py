# SNMP MIB module (HUAWEI-DATASYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-DATASYNC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:26 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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

hwDataSync = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191)
)
hwDataSync.setRevisions(
        ("2015-07-16 13:49",
         "2014-09-04 17:10",
         "2009-03-17 10:27")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



# MIB Managed Objects in the order of their OIDs

_HwDataSyncScalarObjects_ObjectIdentity = ObjectIdentity
hwDataSyncScalarObjects = _HwDataSyncScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 1)
)
_HwCurrentCfgChgSeqID_Type = Integer32
_HwCurrentCfgChgSeqID_Object = MibScalar
hwCurrentCfgChgSeqID = _HwCurrentCfgChgSeqID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 1, 1),
    _HwCurrentCfgChgSeqID_Type()
)
hwCurrentCfgChgSeqID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCurrentCfgChgSeqID.setStatus("current")
_HwCfgChgSeqIDReveralCount_Type = Integer32
_HwCfgChgSeqIDReveralCount_Object = MibScalar
hwCfgChgSeqIDReveralCount = _HwCfgChgSeqIDReveralCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 1, 2),
    _HwCfgChgSeqIDReveralCount_Type()
)
hwCfgChgSeqIDReveralCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgChgSeqIDReveralCount.setStatus("current")
_HwCfgChgTableMaxItem_Type = Integer32
_HwCfgChgTableMaxItem_Object = MibScalar
hwCfgChgTableMaxItem = _HwCfgChgTableMaxItem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 1, 3),
    _HwCfgChgTableMaxItem_Type()
)
hwCfgChgTableMaxItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgChgTableMaxItem.setStatus("current")


class _HwCfgBaselineTime_Type(DisplayString):
    """Custom type hwCfgBaselineTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HwCfgBaselineTime_Type.__name__ = "DisplayString"
_HwCfgBaselineTime_Object = MibScalar
hwCfgBaselineTime = _HwCfgBaselineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 1, 4),
    _HwCfgBaselineTime_Type()
)
hwCfgBaselineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgBaselineTime.setStatus("current")
_HwDataSyncTableObjects_ObjectIdentity = ObjectIdentity
hwDataSyncTableObjects = _HwDataSyncTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2)
)
_HwCfgChgTable_Object = MibTable
hwCfgChgTable = _HwCfgChgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 1)
)
if mibBuilder.loadTexts:
    hwCfgChgTable.setStatus("current")
_HwCfgChgEntry_Object = MibTableRow
hwCfgChgEntry = _HwCfgChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 1, 1)
)
hwCfgChgEntry.setIndexNames(
    (0, "HUAWEI-DATASYNC-MIB", "hwCfgChgSeqID"),
)
if mibBuilder.loadTexts:
    hwCfgChgEntry.setStatus("current")


class _HwCfgChgSeqID_Type(Integer32):
    """Custom type hwCfgChgSeqID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwCfgChgSeqID_Type.__name__ = "Integer32"
_HwCfgChgSeqID_Object = MibTableColumn
hwCfgChgSeqID = _HwCfgChgSeqID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 1, 1, 1),
    _HwCfgChgSeqID_Type()
)
hwCfgChgSeqID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgChgSeqID.setStatus("current")
_HwCfgChgTime_Type = DateAndTime
_HwCfgChgTime_Object = MibTableColumn
hwCfgChgTime = _HwCfgChgTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 1, 1, 2),
    _HwCfgChgTime_Type()
)
hwCfgChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgChgTime.setStatus("current")


class _HwCfgChgTerminalType_Type(Integer32):
    """Custom type hwCfgChgTerminalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("netconf", 3),
          ("snmp", 1),
          ("telnet", 2))
    )


_HwCfgChgTerminalType_Type.__name__ = "Integer32"
_HwCfgChgTerminalType_Object = MibTableColumn
hwCfgChgTerminalType = _HwCfgChgTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 1, 1, 3),
    _HwCfgChgTerminalType_Type()
)
hwCfgChgTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgChgTerminalType.setStatus("current")


class _HwCfgChgTerminalID_Type(Integer32):
    """Custom type hwCfgChgTerminalID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwCfgChgTerminalID_Type.__name__ = "Integer32"
_HwCfgChgTerminalID_Object = MibTableColumn
hwCfgChgTerminalID = _HwCfgChgTerminalID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 1, 1, 4),
    _HwCfgChgTerminalID_Type()
)
hwCfgChgTerminalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgChgTerminalID.setStatus("current")


class _HwCfgChgType_Type(Integer32):
    """Custom type hwCfgChgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 3),
          ("modify", 2))
    )


_HwCfgChgType_Type.__name__ = "Integer32"
_HwCfgChgType_Object = MibTableColumn
hwCfgChgType = _HwCfgChgType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 1, 1, 5),
    _HwCfgChgType_Type()
)
hwCfgChgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgChgType.setStatus("current")
_HwCfgChgViewName_Type = OctetString
_HwCfgChgViewName_Object = MibTableColumn
hwCfgChgViewName = _HwCfgChgViewName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 1, 1, 6),
    _HwCfgChgViewName_Type()
)
hwCfgChgViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgChgViewName.setStatus("current")
_HwCfgChgCmdID_Type = Integer32
_HwCfgChgCmdID_Object = MibTableColumn
hwCfgChgCmdID = _HwCfgChgCmdID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 1, 1, 7),
    _HwCfgChgCmdID_Type()
)
hwCfgChgCmdID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgChgCmdID.setStatus("current")
_HwCfgChgDetailInfo_Type = OctetString
_HwCfgChgDetailInfo_Object = MibTableColumn
hwCfgChgDetailInfo = _HwCfgChgDetailInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 1, 1, 8),
    _HwCfgChgDetailInfo_Type()
)
hwCfgChgDetailInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgChgDetailInfo.setStatus("current")
_HwCollectTable_Object = MibTable
hwCollectTable = _HwCollectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 2)
)
if mibBuilder.loadTexts:
    hwCollectTable.setStatus("current")
_HwCollectEntry_Object = MibTableRow
hwCollectEntry = _HwCollectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 2, 1)
)
hwCollectEntry.setIndexNames(
    (0, "HUAWEI-DATASYNC-MIB", "hwCollectIndex"),
)
if mibBuilder.loadTexts:
    hwCollectEntry.setStatus("current")
_HwCollectIndex_Type = Integer32
_HwCollectIndex_Object = MibTableColumn
hwCollectIndex = _HwCollectIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 2, 1, 1),
    _HwCollectIndex_Type()
)
hwCollectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCollectIndex.setStatus("current")
_HwCollectNetManageId_Type = Integer32
_HwCollectNetManageId_Object = MibTableColumn
hwCollectNetManageId = _HwCollectNetManageId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 2, 1, 2),
    _HwCollectNetManageId_Type()
)
hwCollectNetManageId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCollectNetManageId.setStatus("current")


class _HwCollectOperation_Type(Integer32):
    """Custom type hwCollectOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("begin", 1),
          ("stop", 2))
    )


_HwCollectOperation_Type.__name__ = "Integer32"
_HwCollectOperation_Object = MibTableColumn
hwCollectOperation = _HwCollectOperation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 2, 1, 3),
    _HwCollectOperation_Type()
)
hwCollectOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCollectOperation.setStatus("current")


class _HwCollectInScriptFile_Type(OctetString):
    """Custom type hwCollectInScriptFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwCollectInScriptFile_Type.__name__ = "OctetString"
_HwCollectInScriptFile_Object = MibTableColumn
hwCollectInScriptFile = _HwCollectInScriptFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 2, 1, 4),
    _HwCollectInScriptFile_Type()
)
hwCollectInScriptFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCollectInScriptFile.setStatus("current")


class _HwCollectInResultFile_Type(OctetString):
    """Custom type hwCollectInResultFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwCollectInResultFile_Type.__name__ = "OctetString"
_HwCollectInResultFile_Object = MibTableColumn
hwCollectInResultFile = _HwCollectInResultFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 2, 1, 5),
    _HwCollectInResultFile_Type()
)
hwCollectInResultFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCollectInResultFile.setStatus("current")


class _HwCollectState_Type(Integer32):
    """Custom type hwCollectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("collecting", 2),
          ("idle", 1))
    )


_HwCollectState_Type.__name__ = "Integer32"
_HwCollectState_Object = MibTableColumn
hwCollectState = _HwCollectState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 2, 1, 6),
    _HwCollectState_Type()
)
hwCollectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCollectState.setStatus("current")
_HwCollectRowStatus_Type = RowStatus
_HwCollectRowStatus_Object = MibTableColumn
hwCollectRowStatus = _HwCollectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 2, 2, 1, 7),
    _HwCollectRowStatus_Type()
)
hwCollectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCollectRowStatus.setStatus("current")
_HwDataSyncNotifications_ObjectIdentity = ObjectIdentity
hwDataSyncNotifications = _HwDataSyncNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 3)
)
_HwDataSyncConformance_ObjectIdentity = ObjectIdentity
hwDataSyncConformance = _HwDataSyncConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 4)
)
_HwDataSyncGroups_ObjectIdentity = ObjectIdentity
hwDataSyncGroups = _HwDataSyncGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 4, 1)
)
_HwDataSyncCompliances_ObjectIdentity = ObjectIdentity
hwDataSyncCompliances = _HwDataSyncCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 4, 2)
)

# Managed Objects groups

hwDataSyncScalarObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 4, 1, 1)
)
hwDataSyncScalarObjectsGroup.setObjects(
      *(("HUAWEI-DATASYNC-MIB", "hwCurrentCfgChgSeqID"),
        ("HUAWEI-DATASYNC-MIB", "hwCfgChgSeqIDReveralCount"),
        ("HUAWEI-DATASYNC-MIB", "hwCfgChgTableMaxItem"),
        ("HUAWEI-DATASYNC-MIB", "hwCfgBaselineTime"))
)
if mibBuilder.loadTexts:
    hwDataSyncScalarObjectsGroup.setStatus("current")


# Notification objects

hwCfgChgNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 3, 1)
)
hwCfgChgNotify.setObjects(
      *(("HUAWEI-DATASYNC-MIB", "hwCurrentCfgChgSeqID"),
        ("HUAWEI-DATASYNC-MIB", "hwCfgChgSeqIDReveralCount"),
        ("HUAWEI-DATASYNC-MIB", "hwCfgChgTableMaxItem"),
        ("HUAWEI-DATASYNC-MIB", "hwCfgBaselineTime"))
)
if mibBuilder.loadTexts:
    hwCfgChgNotify.setStatus(
        "current"
    )

hwCfgLastSaveFailNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 3, 2)
)
if mibBuilder.loadTexts:
    hwCfgLastSaveFailNotify.setStatus(
        "current"
    )


# Notifications groups

hwCfgChgNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 4, 1, 2)
)
hwCfgChgNotifyGroup.setObjects(
    ("HUAWEI-DATASYNC-MIB", "hwCfgChgNotify")
)
if mibBuilder.loadTexts:
    hwCfgChgNotifyGroup.setStatus(
        "current"
    )

hwDataSyncNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 4, 1, 3)
)
hwDataSyncNotifyGroup.setObjects(
    ("HUAWEI-DATASYNC-MIB", "hwCfgLastSaveFailNotify")
)
if mibBuilder.loadTexts:
    hwDataSyncNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwDataSyncCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 191, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hwDataSyncCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DATASYNC-MIB",
    **{"DateAndTime": DateAndTime,
       "hwDataSync": hwDataSync,
       "hwDataSyncScalarObjects": hwDataSyncScalarObjects,
       "hwCurrentCfgChgSeqID": hwCurrentCfgChgSeqID,
       "hwCfgChgSeqIDReveralCount": hwCfgChgSeqIDReveralCount,
       "hwCfgChgTableMaxItem": hwCfgChgTableMaxItem,
       "hwCfgBaselineTime": hwCfgBaselineTime,
       "hwDataSyncTableObjects": hwDataSyncTableObjects,
       "hwCfgChgTable": hwCfgChgTable,
       "hwCfgChgEntry": hwCfgChgEntry,
       "hwCfgChgSeqID": hwCfgChgSeqID,
       "hwCfgChgTime": hwCfgChgTime,
       "hwCfgChgTerminalType": hwCfgChgTerminalType,
       "hwCfgChgTerminalID": hwCfgChgTerminalID,
       "hwCfgChgType": hwCfgChgType,
       "hwCfgChgViewName": hwCfgChgViewName,
       "hwCfgChgCmdID": hwCfgChgCmdID,
       "hwCfgChgDetailInfo": hwCfgChgDetailInfo,
       "hwCollectTable": hwCollectTable,
       "hwCollectEntry": hwCollectEntry,
       "hwCollectIndex": hwCollectIndex,
       "hwCollectNetManageId": hwCollectNetManageId,
       "hwCollectOperation": hwCollectOperation,
       "hwCollectInScriptFile": hwCollectInScriptFile,
       "hwCollectInResultFile": hwCollectInResultFile,
       "hwCollectState": hwCollectState,
       "hwCollectRowStatus": hwCollectRowStatus,
       "hwDataSyncNotifications": hwDataSyncNotifications,
       "hwCfgChgNotify": hwCfgChgNotify,
       "hwCfgLastSaveFailNotify": hwCfgLastSaveFailNotify,
       "hwDataSyncConformance": hwDataSyncConformance,
       "hwDataSyncGroups": hwDataSyncGroups,
       "hwDataSyncScalarObjectsGroup": hwDataSyncScalarObjectsGroup,
       "hwCfgChgNotifyGroup": hwCfgChgNotifyGroup,
       "hwDataSyncNotifyGroup": hwDataSyncNotifyGroup,
       "hwDataSyncCompliances": hwDataSyncCompliances,
       "hwDataSyncCompliance": hwDataSyncCompliance}
)
