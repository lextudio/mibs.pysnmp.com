# SNMP MIB module (HUAWEI-CONFIG-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-CONFIG-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:23 2024
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

(huaweiUtility,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiUtility")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10)
)
hwConfig.setRevisions(
        ("2015-04-27 14:02",
         "2015-04-13 11:19",
         "2015-02-02 23:00",
         "2014-09-18 22:00",
         "2014-09-16 10:20",
         "2014-08-21 16:02",
         "2014-05-29 22:30",
         "2014-05-26 22:30",
         "2013-09-03 22:30",
         "2013-08-30 22:30",
         "2006-08-22 22:30",
         "2006-08-22 22:30",
         "2006-08-22 22:30",
         "2006-08-22 22:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigOperationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("net2Running", 4),
          ("net2Startup", 5),
          ("running2Net", 3),
          ("running2Startup", 1),
          ("startup2Net", 6),
          ("startup2Running", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwConfigManObjects_ObjectIdentity = ObjectIdentity
hwConfigManObjects = _HwConfigManObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1)
)
_HwCfgLog_ObjectIdentity = ObjectIdentity
hwCfgLog = _HwCfgLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1)
)
_HwCfgRunModifiedLast_Type = TimeTicks
_HwCfgRunModifiedLast_Object = MibScalar
hwCfgRunModifiedLast = _HwCfgRunModifiedLast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 1),
    _HwCfgRunModifiedLast_Type()
)
hwCfgRunModifiedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgRunModifiedLast.setStatus("current")
_HwCfgRunSavedLast_Type = TimeTicks
_HwCfgRunSavedLast_Object = MibScalar
hwCfgRunSavedLast = _HwCfgRunSavedLast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 2),
    _HwCfgRunSavedLast_Type()
)
hwCfgRunSavedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgRunSavedLast.setStatus("current")
_HwCfgStartModifiedLast_Type = TimeTicks
_HwCfgStartModifiedLast_Object = MibScalar
hwCfgStartModifiedLast = _HwCfgStartModifiedLast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 3),
    _HwCfgStartModifiedLast_Type()
)
hwCfgStartModifiedLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgStartModifiedLast.setStatus("current")


class _HwCfgLogLimitedEntries_Type(Integer32):
    """Custom type hwCfgLogLimitedEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwCfgLogLimitedEntries_Type.__name__ = "Integer32"
_HwCfgLogLimitedEntries_Object = MibScalar
hwCfgLogLimitedEntries = _HwCfgLogLimitedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 4),
    _HwCfgLogLimitedEntries_Type()
)
hwCfgLogLimitedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogLimitedEntries.setStatus("current")
_HwCfgLogDeletedEntries_Type = Counter32
_HwCfgLogDeletedEntries_Object = MibScalar
hwCfgLogDeletedEntries = _HwCfgLogDeletedEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 5),
    _HwCfgLogDeletedEntries_Type()
)
hwCfgLogDeletedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogDeletedEntries.setStatus("current")
_HwCfgLogWantBackup_Type = TruthValue
_HwCfgLogWantBackup_Object = MibScalar
hwCfgLogWantBackup = _HwCfgLogWantBackup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 6),
    _HwCfgLogWantBackup_Type()
)
hwCfgLogWantBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCfgLogWantBackup.setStatus("current")
_HwCfgLogTable_Object = MibTable
hwCfgLogTable = _HwCfgLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwCfgLogTable.setStatus("current")
_HwCfgLogEntry_Object = MibTableRow
hwCfgLogEntry = _HwCfgLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1)
)
hwCfgLogEntry.setIndexNames(
    (0, "HUAWEI-CONFIG-MAN-MIB", "hwCfgLogIndex"),
)
if mibBuilder.loadTexts:
    hwCfgLogEntry.setStatus("current")


class _HwCfgLogIndex_Type(Integer32):
    """Custom type hwCfgLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwCfgLogIndex_Type.__name__ = "Integer32"
_HwCfgLogIndex_Object = MibTableColumn
hwCfgLogIndex = _HwCfgLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 1),
    _HwCfgLogIndex_Type()
)
hwCfgLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgLogIndex.setStatus("current")
_HwCfgLogTime_Type = TimeTicks
_HwCfgLogTime_Object = MibTableColumn
hwCfgLogTime = _HwCfgLogTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 2),
    _HwCfgLogTime_Type()
)
hwCfgLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogTime.setStatus("current")


class _HwCfgLogSrcCmd_Type(Integer32):
    """Custom type hwCfgLogSrcCmd based on Integer32"""
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
        *(("cmdLine", 1),
          ("netconf", 3),
          ("other", 4),
          ("snmp", 2))
    )


_HwCfgLogSrcCmd_Type.__name__ = "Integer32"
_HwCfgLogSrcCmd_Object = MibTableColumn
hwCfgLogSrcCmd = _HwCfgLogSrcCmd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 3),
    _HwCfgLogSrcCmd_Type()
)
hwCfgLogSrcCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogSrcCmd.setStatus("current")


class _HwCfgLogSrcData_Type(Integer32):
    """Custom type hwCfgLogSrcData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("commandSource", 3),
          ("erase", 1),
          ("hotPlugging", 7),
          ("local", 5),
          ("netFtp", 6),
          ("runningData", 2),
          ("startupData", 4))
    )


_HwCfgLogSrcData_Type.__name__ = "Integer32"
_HwCfgLogSrcData_Object = MibTableColumn
hwCfgLogSrcData = _HwCfgLogSrcData_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 4),
    _HwCfgLogSrcData_Type()
)
hwCfgLogSrcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogSrcData.setStatus("current")


class _HwCfgLogDesData_Type(Integer32):
    """Custom type hwCfgLogDesData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("commandSource", 3),
          ("hotPlugging", 7),
          ("local", 5),
          ("netkFtp", 6),
          ("runningData", 2),
          ("startupData", 4),
          ("unknown", 1))
    )


_HwCfgLogDesData_Type.__name__ = "Integer32"
_HwCfgLogDesData_Object = MibTableColumn
hwCfgLogDesData = _HwCfgLogDesData_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 5),
    _HwCfgLogDesData_Type()
)
hwCfgLogDesData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogDesData.setStatus("current")


class _HwCfgLogTerminalType_Type(Integer32):
    """Custom type hwCfgLogTerminalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auxiliary", 6),
          ("console", 3),
          ("notApplicable", 1),
          ("terminal", 4),
          ("unknown", 2),
          ("virtual", 5))
    )


_HwCfgLogTerminalType_Type.__name__ = "Integer32"
_HwCfgLogTerminalType_Object = MibTableColumn
hwCfgLogTerminalType = _HwCfgLogTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 6),
    _HwCfgLogTerminalType_Type()
)
hwCfgLogTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogTerminalType.setStatus("current")


class _HwCfgLogTerminalUser_Type(DisplayString):
    """Custom type hwCfgLogTerminalUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwCfgLogTerminalUser_Type.__name__ = "DisplayString"
_HwCfgLogTerminalUser_Object = MibTableColumn
hwCfgLogTerminalUser = _HwCfgLogTerminalUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 7),
    _HwCfgLogTerminalUser_Type()
)
hwCfgLogTerminalUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogTerminalUser.setStatus("current")
_HwCfgLogTerminalNum_Type = Integer32
_HwCfgLogTerminalNum_Object = MibTableColumn
hwCfgLogTerminalNum = _HwCfgLogTerminalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 8),
    _HwCfgLogTerminalNum_Type()
)
hwCfgLogTerminalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogTerminalNum.setStatus("current")


class _HwCfgLogTerminalLocation_Type(DisplayString):
    """Custom type hwCfgLogTerminalLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwCfgLogTerminalLocation_Type.__name__ = "DisplayString"
_HwCfgLogTerminalLocation_Object = MibTableColumn
hwCfgLogTerminalLocation = _HwCfgLogTerminalLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 9),
    _HwCfgLogTerminalLocation_Type()
)
hwCfgLogTerminalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogTerminalLocation.setStatus("current")
_HwCfgLogCmdSrcAddress_Type = IpAddress
_HwCfgLogCmdSrcAddress_Object = MibTableColumn
hwCfgLogCmdSrcAddress = _HwCfgLogCmdSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 10),
    _HwCfgLogCmdSrcAddress_Type()
)
hwCfgLogCmdSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogCmdSrcAddress.setStatus("current")


class _HwCfgLogVirHost_Type(DisplayString):
    """Custom type hwCfgLogVirHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwCfgLogVirHost_Type.__name__ = "DisplayString"
_HwCfgLogVirHost_Object = MibTableColumn
hwCfgLogVirHost = _HwCfgLogVirHost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 11),
    _HwCfgLogVirHost_Type()
)
hwCfgLogVirHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogVirHost.setStatus("current")


class _HwCfgLogUserName_Type(DisplayString):
    """Custom type hwCfgLogUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwCfgLogUserName_Type.__name__ = "DisplayString"
_HwCfgLogUserName_Object = MibTableColumn
hwCfgLogUserName = _HwCfgLogUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 12),
    _HwCfgLogUserName_Type()
)
hwCfgLogUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogUserName.setStatus("current")
_HwCfgLogServerAddress_Type = IpAddress
_HwCfgLogServerAddress_Object = MibTableColumn
hwCfgLogServerAddress = _HwCfgLogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 13),
    _HwCfgLogServerAddress_Type()
)
hwCfgLogServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogServerAddress.setStatus("current")


class _HwCfgLogFile_Type(DisplayString):
    """Custom type hwCfgLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwCfgLogFile_Type.__name__ = "DisplayString"
_HwCfgLogFile_Object = MibTableColumn
hwCfgLogFile = _HwCfgLogFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 14),
    _HwCfgLogFile_Type()
)
hwCfgLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogFile.setStatus("current")


class _HwCfgLogConfigChangeId_Type(Unsigned32):
    """Custom type hwCfgLogConfigChangeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_HwCfgLogConfigChangeId_Type.__name__ = "Unsigned32"
_HwCfgLogConfigChangeId_Object = MibTableColumn
hwCfgLogConfigChangeId = _HwCfgLogConfigChangeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 15),
    _HwCfgLogConfigChangeId_Type()
)
hwCfgLogConfigChangeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogConfigChangeId.setStatus("obsolete")


class _HwCfgLogCfgBaselineTime_Type(DisplayString):
    """Custom type hwCfgLogCfgBaselineTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HwCfgLogCfgBaselineTime_Type.__name__ = "DisplayString"
_HwCfgLogCfgBaselineTime_Object = MibTableColumn
hwCfgLogCfgBaselineTime = _HwCfgLogCfgBaselineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 1, 7, 1, 16),
    _HwCfgLogCfgBaselineTime_Type()
)
hwCfgLogCfgBaselineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgLogCfgBaselineTime.setStatus("obsolete")
_HwCfgOperate_ObjectIdentity = ObjectIdentity
hwCfgOperate = _HwCfgOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2)
)


class _HwCfgOperateGlobalEntryLimit_Type(Integer32):
    """Custom type hwCfgOperateGlobalEntryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwCfgOperateGlobalEntryLimit_Type.__name__ = "Integer32"
_HwCfgOperateGlobalEntryLimit_Object = MibScalar
hwCfgOperateGlobalEntryLimit = _HwCfgOperateGlobalEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 1),
    _HwCfgOperateGlobalEntryLimit_Type()
)
hwCfgOperateGlobalEntryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateGlobalEntryLimit.setStatus("current")


class _HwCfgOperateEntryAgeOutTime_Type(Integer32):
    """Custom type hwCfgOperateEntryAgeOutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HwCfgOperateEntryAgeOutTime_Type.__name__ = "Integer32"
_HwCfgOperateEntryAgeOutTime_Object = MibScalar
hwCfgOperateEntryAgeOutTime = _HwCfgOperateEntryAgeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 2),
    _HwCfgOperateEntryAgeOutTime_Type()
)
hwCfgOperateEntryAgeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCfgOperateEntryAgeOutTime.setStatus("current")
if mibBuilder.loadTexts:
    hwCfgOperateEntryAgeOutTime.setUnits("minute")


class _HwCfgOperateResultGlobalEntryLimit_Type(Integer32):
    """Custom type hwCfgOperateResultGlobalEntryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_HwCfgOperateResultGlobalEntryLimit_Type.__name__ = "Integer32"
_HwCfgOperateResultGlobalEntryLimit_Object = MibScalar
hwCfgOperateResultGlobalEntryLimit = _HwCfgOperateResultGlobalEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 3),
    _HwCfgOperateResultGlobalEntryLimit_Type()
)
hwCfgOperateResultGlobalEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCfgOperateResultGlobalEntryLimit.setStatus("current")
_HwCfgOperateTable_Object = MibTable
hwCfgOperateTable = _HwCfgOperateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hwCfgOperateTable.setStatus("current")
_HwCfgOperateEntry_Object = MibTableRow
hwCfgOperateEntry = _HwCfgOperateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1)
)
hwCfgOperateEntry.setIndexNames(
    (0, "HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateIndex"),
)
if mibBuilder.loadTexts:
    hwCfgOperateEntry.setStatus("current")


class _HwCfgOperateIndex_Type(Integer32):
    """Custom type hwCfgOperateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwCfgOperateIndex_Type.__name__ = "Integer32"
_HwCfgOperateIndex_Object = MibTableColumn
hwCfgOperateIndex = _HwCfgOperateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 1),
    _HwCfgOperateIndex_Type()
)
hwCfgOperateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgOperateIndex.setStatus("current")
_HwCfgOperateType_Type = ConfigOperationType
_HwCfgOperateType_Object = MibTableColumn
hwCfgOperateType = _HwCfgOperateType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 2),
    _HwCfgOperateType_Type()
)
hwCfgOperateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateType.setStatus("current")


class _HwCfgOperateProtocol_Type(Integer32):
    """Custom type hwCfgOperateProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 3),
          ("tftp", 2))
    )


_HwCfgOperateProtocol_Type.__name__ = "Integer32"
_HwCfgOperateProtocol_Object = MibTableColumn
hwCfgOperateProtocol = _HwCfgOperateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 3),
    _HwCfgOperateProtocol_Type()
)
hwCfgOperateProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateProtocol.setStatus("current")


class _HwCfgOperateFileName_Type(DisplayString):
    """Custom type hwCfgOperateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwCfgOperateFileName_Type.__name__ = "DisplayString"
_HwCfgOperateFileName_Object = MibTableColumn
hwCfgOperateFileName = _HwCfgOperateFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 4),
    _HwCfgOperateFileName_Type()
)
hwCfgOperateFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateFileName.setStatus("current")
_HwCfgOperateServerAddress_Type = IpAddress
_HwCfgOperateServerAddress_Object = MibTableColumn
hwCfgOperateServerAddress = _HwCfgOperateServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 5),
    _HwCfgOperateServerAddress_Type()
)
hwCfgOperateServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateServerAddress.setStatus("current")


class _HwCfgOperateUserName_Type(DisplayString):
    """Custom type hwCfgOperateUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_HwCfgOperateUserName_Type.__name__ = "DisplayString"
_HwCfgOperateUserName_Object = MibTableColumn
hwCfgOperateUserName = _HwCfgOperateUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 6),
    _HwCfgOperateUserName_Type()
)
hwCfgOperateUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateUserName.setStatus("current")


class _HwCfgOperateUserPassword_Type(DisplayString):
    """Custom type hwCfgOperateUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HwCfgOperateUserPassword_Type.__name__ = "DisplayString"
_HwCfgOperateUserPassword_Object = MibTableColumn
hwCfgOperateUserPassword = _HwCfgOperateUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 7),
    _HwCfgOperateUserPassword_Type()
)
hwCfgOperateUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateUserPassword.setStatus("current")


class _HwCfgOperateEndNotificationSwitch_Type(TruthValue):
    """Custom type hwCfgOperateEndNotificationSwitch based on TruthValue"""


_HwCfgOperateEndNotificationSwitch_Object = MibTableColumn
hwCfgOperateEndNotificationSwitch = _HwCfgOperateEndNotificationSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 8),
    _HwCfgOperateEndNotificationSwitch_Type()
)
hwCfgOperateEndNotificationSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateEndNotificationSwitch.setStatus("current")
_HwCfgOperateRowStatus_Type = RowStatus
_HwCfgOperateRowStatus_Object = MibTableColumn
hwCfgOperateRowStatus = _HwCfgOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 9),
    _HwCfgOperateRowStatus_Type()
)
hwCfgOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateRowStatus.setStatus("current")


class _HwCfgOperateServerPort_Type(Integer32):
    """Custom type hwCfgOperateServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwCfgOperateServerPort_Type.__name__ = "Integer32"
_HwCfgOperateServerPort_Object = MibTableColumn
hwCfgOperateServerPort = _HwCfgOperateServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 10),
    _HwCfgOperateServerPort_Type()
)
hwCfgOperateServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateServerPort.setStatus("current")


class _HwCfgOperateSourceAddress_Type(IpAddress):
    """Custom type hwCfgOperateSourceAddress based on IpAddress"""
    defaultValue = 0


_HwCfgOperateSourceAddress_Object = MibTableColumn
hwCfgOperateSourceAddress = _HwCfgOperateSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 11),
    _HwCfgOperateSourceAddress_Type()
)
hwCfgOperateSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateSourceAddress.setStatus("current")


class _HwCfgOperateSourceInterface_Type(OctetString):
    """Custom type hwCfgOperateSourceInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwCfgOperateSourceInterface_Type.__name__ = "OctetString"
_HwCfgOperateSourceInterface_Object = MibTableColumn
hwCfgOperateSourceInterface = _HwCfgOperateSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 12),
    _HwCfgOperateSourceInterface_Type()
)
hwCfgOperateSourceInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateSourceInterface.setStatus("current")


class _HwCfgOperateOnError_Type(Integer32):
    """Custom type hwCfgOperateOnError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continueOnError", 1),
          ("rollbackOnError", 3),
          ("stopOnError", 2))
    )


_HwCfgOperateOnError_Type.__name__ = "Integer32"
_HwCfgOperateOnError_Object = MibTableColumn
hwCfgOperateOnError = _HwCfgOperateOnError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 13),
    _HwCfgOperateOnError_Type()
)
hwCfgOperateOnError.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateOnError.setStatus("current")
_HwCfgOperateServerAddressType_Type = InetAddressType
_HwCfgOperateServerAddressType_Object = MibTableColumn
hwCfgOperateServerAddressType = _HwCfgOperateServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 17),
    _HwCfgOperateServerAddressType_Type()
)
hwCfgOperateServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateServerAddressType.setStatus("current")
_HwCfgOperateServerAddressNet_Type = InetAddress
_HwCfgOperateServerAddressNet_Object = MibTableColumn
hwCfgOperateServerAddressNet = _HwCfgOperateServerAddressNet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 18),
    _HwCfgOperateServerAddressNet_Type()
)
hwCfgOperateServerAddressNet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateServerAddressNet.setStatus("current")


class _HwCfgOperateVpnInstance_Type(DisplayString):
    """Custom type hwCfgOperateVpnInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwCfgOperateVpnInstance_Type.__name__ = "DisplayString"
_HwCfgOperateVpnInstance_Object = MibTableColumn
hwCfgOperateVpnInstance = _HwCfgOperateVpnInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 4, 1, 19),
    _HwCfgOperateVpnInstance_Type()
)
hwCfgOperateVpnInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgOperateVpnInstance.setStatus("current")
_HwCfgOperateResultTable_Object = MibTable
hwCfgOperateResultTable = _HwCfgOperateResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hwCfgOperateResultTable.setStatus("current")
_HwCfgOperateResultEntry_Object = MibTableRow
hwCfgOperateResultEntry = _HwCfgOperateResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 5, 1)
)
hwCfgOperateResultEntry.setIndexNames(
    (0, "HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateResultIndex"),
)
if mibBuilder.loadTexts:
    hwCfgOperateResultEntry.setStatus("current")


class _HwCfgOperateResultIndex_Type(Integer32):
    """Custom type hwCfgOperateResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwCfgOperateResultIndex_Type.__name__ = "Integer32"
_HwCfgOperateResultIndex_Object = MibTableColumn
hwCfgOperateResultIndex = _HwCfgOperateResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 5, 1, 1),
    _HwCfgOperateResultIndex_Type()
)
hwCfgOperateResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgOperateResultIndex.setStatus("current")


class _HwCfgOperateResultOptIndex_Type(Integer32):
    """Custom type hwCfgOperateResultOptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwCfgOperateResultOptIndex_Type.__name__ = "Integer32"
_HwCfgOperateResultOptIndex_Object = MibTableColumn
hwCfgOperateResultOptIndex = _HwCfgOperateResultOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 5, 1, 2),
    _HwCfgOperateResultOptIndex_Type()
)
hwCfgOperateResultOptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateResultOptIndex.setStatus("current")
_HwCfgOperateResultOpType_Type = ConfigOperationType
_HwCfgOperateResultOpType_Object = MibTableColumn
hwCfgOperateResultOpType = _HwCfgOperateResultOpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 5, 1, 3),
    _HwCfgOperateResultOpType_Type()
)
hwCfgOperateResultOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateResultOpType.setStatus("current")


class _HwCfgOperateState_Type(Integer32):
    """Custom type hwCfgOperateState based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("opAbort", 20),
          ("opAuthFail", 17),
          ("opCmdExecuteFail", 23),
          ("opDeviceBusy", 8),
          ("opDeviceError", 10),
          ("opDeviceFull", 12),
          ("opDeviceNotProgrammable", 11),
          ("opDeviceOpenError", 9),
          ("opFileChecksumError", 15),
          ("opFileOpenError", 13),
          ("opFileTransferError", 14),
          ("opInProgress", 1),
          ("opInvalidDestName", 6),
          ("opInvalidOperation", 3),
          ("opInvalidProtocol", 4),
          ("opInvalidServerAddress", 7),
          ("opInvalidSourceAddress", 21),
          ("opInvalidSourceInterface", 22),
          ("opInvalidSourceName", 5),
          ("opNoMemory", 16),
          ("opSuccess", 2),
          ("opTimeOut", 18),
          ("opUnknownFailure", 19))
    )


_HwCfgOperateState_Type.__name__ = "Integer32"
_HwCfgOperateState_Object = MibTableColumn
hwCfgOperateState = _HwCfgOperateState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 5, 1, 4),
    _HwCfgOperateState_Type()
)
hwCfgOperateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateState.setStatus("current")
_HwCfgOperateTime_Type = TimeTicks
_HwCfgOperateTime_Object = MibTableColumn
hwCfgOperateTime = _HwCfgOperateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 5, 1, 5),
    _HwCfgOperateTime_Type()
)
hwCfgOperateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateTime.setStatus("current")
_HwCfgOperateEndTime_Type = TimeTicks
_HwCfgOperateEndTime_Object = MibTableColumn
hwCfgOperateEndTime = _HwCfgOperateEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 5, 1, 6),
    _HwCfgOperateEndTime_Type()
)
hwCfgOperateEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateEndTime.setStatus("current")


class _HwCfgOperateTransferProgress_Type(Integer32):
    """Custom type hwCfgOperateTransferProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
        ValueRangeConstraint(65535, 65535),
    )


_HwCfgOperateTransferProgress_Type.__name__ = "Integer32"
_HwCfgOperateTransferProgress_Object = MibTableColumn
hwCfgOperateTransferProgress = _HwCfgOperateTransferProgress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 5, 1, 7),
    _HwCfgOperateTransferProgress_Type()
)
hwCfgOperateTransferProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateTransferProgress.setStatus("current")


class _HwCfgOperateErrorReason_Type(DisplayString):
    """Custom type hwCfgOperateErrorReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwCfgOperateErrorReason_Type.__name__ = "DisplayString"
_HwCfgOperateErrorReason_Object = MibTableColumn
hwCfgOperateErrorReason = _HwCfgOperateErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 5, 1, 8),
    _HwCfgOperateErrorReason_Type()
)
hwCfgOperateErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateErrorReason.setStatus("current")
_HwCfgModuleChangeTimeTable_Object = MibTable
hwCfgModuleChangeTimeTable = _HwCfgModuleChangeTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hwCfgModuleChangeTimeTable.setStatus("current")
_HwCfgModuleChangeTimeEntry_Object = MibTableRow
hwCfgModuleChangeTimeEntry = _HwCfgModuleChangeTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 6, 1)
)
hwCfgModuleChangeTimeEntry.setIndexNames(
    (0, "HUAWEI-CONFIG-MAN-MIB", "hwCfgModuleId"),
)
if mibBuilder.loadTexts:
    hwCfgModuleChangeTimeEntry.setStatus("current")


class _HwCfgModuleId_Type(Integer32):
    """Custom type hwCfgModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwCfgModuleId_Type.__name__ = "Integer32"
_HwCfgModuleId_Object = MibTableColumn
hwCfgModuleId = _HwCfgModuleId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 6, 1, 1),
    _HwCfgModuleId_Type()
)
hwCfgModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgModuleId.setStatus("current")
_HwCfgModuleChangeTime_Type = TimeTicks
_HwCfgModuleChangeTime_Object = MibTableColumn
hwCfgModuleChangeTime = _HwCfgModuleChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 6, 1, 11),
    _HwCfgModuleChangeTime_Type()
)
hwCfgModuleChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgModuleChangeTime.setStatus("current")


class _HwCfgOperateCompareConfig_Type(Integer32):
    """Custom type hwCfgOperateCompareConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("different", 2),
          ("initial", 0),
          ("same", 1))
    )


_HwCfgOperateCompareConfig_Type.__name__ = "Integer32"
_HwCfgOperateCompareConfig_Object = MibScalar
hwCfgOperateCompareConfig = _HwCfgOperateCompareConfig_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 7),
    _HwCfgOperateCompareConfig_Type()
)
hwCfgOperateCompareConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCfgOperateCompareConfig.setStatus("current")


class _HwCfgRestoreErrCode_Type(Integer32):
    """Custom type hwCfgRestoreErrCode based on Integer32"""
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
        *(("fileNotExist", 3),
          ("fileOpenFail", 2),
          ("fileVerifyFail", 4),
          ("other", 5),
          ("warnning", 1))
    )


_HwCfgRestoreErrCode_Type.__name__ = "Integer32"
_HwCfgRestoreErrCode_Object = MibScalar
hwCfgRestoreErrCode = _HwCfgRestoreErrCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 2, 8),
    _HwCfgRestoreErrCode_Type()
)
hwCfgRestoreErrCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfgRestoreErrCode.setStatus("current")
_HwCfgSave_ObjectIdentity = ObjectIdentity
hwCfgSave = _HwCfgSave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3)
)


class _HwCfgSaveAutoInterval_Type(Integer32):
    """Custom type hwCfgSaveAutoInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 43200),
    )


_HwCfgSaveAutoInterval_Type.__name__ = "Integer32"
_HwCfgSaveAutoInterval_Object = MibScalar
hwCfgSaveAutoInterval = _HwCfgSaveAutoInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 1),
    _HwCfgSaveAutoInterval_Type()
)
hwCfgSaveAutoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCfgSaveAutoInterval.setStatus("current")
_HwCfgSaveAutoTime_Type = DateAndTime
_HwCfgSaveAutoTime_Object = MibScalar
hwCfgSaveAutoTime = _HwCfgSaveAutoTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 2),
    _HwCfgSaveAutoTime_Type()
)
hwCfgSaveAutoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgSaveAutoTime.setStatus("current")
_HwCfgSaveManualTime_Type = DateAndTime
_HwCfgSaveManualTime_Object = MibScalar
hwCfgSaveManualTime = _HwCfgSaveManualTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 3),
    _HwCfgSaveManualTime_Type()
)
hwCfgSaveManualTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgSaveManualTime.setStatus("current")


class _HwCfgSaveAutoCpuLimit_Type(Integer32):
    """Custom type hwCfgSaveAutoCpuLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HwCfgSaveAutoCpuLimit_Type.__name__ = "Integer32"
_HwCfgSaveAutoCpuLimit_Object = MibScalar
hwCfgSaveAutoCpuLimit = _HwCfgSaveAutoCpuLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 4),
    _HwCfgSaveAutoCpuLimit_Type()
)
hwCfgSaveAutoCpuLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCfgSaveAutoCpuLimit.setStatus("current")


class _HwCfgSaveAutoNoCfgInterval_Type(Integer32):
    """Custom type hwCfgSaveAutoNoCfgInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 43200),
    )


_HwCfgSaveAutoNoCfgInterval_Type.__name__ = "Integer32"
_HwCfgSaveAutoNoCfgInterval_Object = MibScalar
hwCfgSaveAutoNoCfgInterval = _HwCfgSaveAutoNoCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 5),
    _HwCfgSaveAutoNoCfgInterval_Type()
)
hwCfgSaveAutoNoCfgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCfgSaveAutoNoCfgInterval.setStatus("obsolete")


class _HwCfgSaveAutoDelay_Type(Integer32):
    """Custom type hwCfgSaveAutoDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HwCfgSaveAutoDelay_Type.__name__ = "Integer32"
_HwCfgSaveAutoDelay_Object = MibScalar
hwCfgSaveAutoDelay = _HwCfgSaveAutoDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 6),
    _HwCfgSaveAutoDelay_Type()
)
hwCfgSaveAutoDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCfgSaveAutoDelay.setStatus("current")
_HwCfgBackup2ServerTable_Object = MibTable
hwCfgBackup2ServerTable = _HwCfgBackup2ServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 7)
)
if mibBuilder.loadTexts:
    hwCfgBackup2ServerTable.setStatus("current")
_HwCfgBackup2ServerEntry_Object = MibTableRow
hwCfgBackup2ServerEntry = _HwCfgBackup2ServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 7, 1)
)
hwCfgBackup2ServerEntry.setIndexNames(
    (0, "HUAWEI-CONFIG-MAN-MIB", "hwCfgBackupIndex"),
)
if mibBuilder.loadTexts:
    hwCfgBackup2ServerEntry.setStatus("current")


class _HwCfgBackupIndex_Type(Integer32):
    """Custom type hwCfgBackupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HwCfgBackupIndex_Type.__name__ = "Integer32"
_HwCfgBackupIndex_Object = MibTableColumn
hwCfgBackupIndex = _HwCfgBackupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 7, 1, 1),
    _HwCfgBackupIndex_Type()
)
hwCfgBackupIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfgBackupIndex.setStatus("current")
_HwCfgBackupServerIp_Type = IpAddress
_HwCfgBackupServerIp_Object = MibTableColumn
hwCfgBackupServerIp = _HwCfgBackupServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 7, 1, 2),
    _HwCfgBackupServerIp_Type()
)
hwCfgBackupServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgBackupServerIp.setStatus("current")


class _HwCfgBackupProtocol_Type(Integer32):
    """Custom type hwCfgBackupProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 3),
          ("tftp", 2))
    )


_HwCfgBackupProtocol_Type.__name__ = "Integer32"
_HwCfgBackupProtocol_Object = MibTableColumn
hwCfgBackupProtocol = _HwCfgBackupProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 7, 1, 3),
    _HwCfgBackupProtocol_Type()
)
hwCfgBackupProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgBackupProtocol.setStatus("current")


class _HwCfgBackupUser_Type(DisplayString):
    """Custom type hwCfgBackupUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCfgBackupUser_Type.__name__ = "DisplayString"
_HwCfgBackupUser_Object = MibTableColumn
hwCfgBackupUser = _HwCfgBackupUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 7, 1, 4),
    _HwCfgBackupUser_Type()
)
hwCfgBackupUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgBackupUser.setStatus("current")


class _HwCfgBackupPassword_Type(OctetString):
    """Custom type hwCfgBackupPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwCfgBackupPassword_Type.__name__ = "OctetString"
_HwCfgBackupPassword_Object = MibTableColumn
hwCfgBackupPassword = _HwCfgBackupPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 7, 1, 5),
    _HwCfgBackupPassword_Type()
)
hwCfgBackupPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgBackupPassword.setStatus("current")


class _HwCfgBackupServerPath_Type(DisplayString):
    """Custom type hwCfgBackupServerPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCfgBackupServerPath_Type.__name__ = "DisplayString"
_HwCfgBackupServerPath_Object = MibTableColumn
hwCfgBackupServerPath = _HwCfgBackupServerPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 7, 1, 6),
    _HwCfgBackupServerPath_Type()
)
hwCfgBackupServerPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgBackupServerPath.setStatus("current")
_HwCfgBackupRowStatus_Type = RowStatus
_HwCfgBackupRowStatus_Object = MibTableColumn
hwCfgBackupRowStatus = _HwCfgBackupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 7, 1, 7),
    _HwCfgBackupRowStatus_Type()
)
hwCfgBackupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgBackupRowStatus.setStatus("current")


class _HwCfgBackupResult_Type(DisplayString):
    """Custom type hwCfgBackupResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCfgBackupResult_Type.__name__ = "DisplayString"
_HwCfgBackupResult_Object = MibTableColumn
hwCfgBackupResult = _HwCfgBackupResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 7, 1, 8),
    _HwCfgBackupResult_Type()
)
hwCfgBackupResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgBackupResult.setStatus("current")


class _HwCfgBackupVpnInstance_Type(DisplayString):
    """Custom type hwCfgBackupVpnInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwCfgBackupVpnInstance_Type.__name__ = "DisplayString"
_HwCfgBackupVpnInstance_Object = MibTableColumn
hwCfgBackupVpnInstance = _HwCfgBackupVpnInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 3, 7, 1, 9),
    _HwCfgBackupVpnInstance_Type()
)
hwCfgBackupVpnInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgBackupVpnInstance.setStatus("current")
_HwCfgLock_ObjectIdentity = ObjectIdentity
hwCfgLock = _HwCfgLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 4)
)


class _HwCfgOperateLockConfigDataStore_Type(Integer32):
    """Custom type hwCfgOperateLockConfigDataStore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_HwCfgOperateLockConfigDataStore_Type.__name__ = "Integer32"
_HwCfgOperateLockConfigDataStore_Object = MibScalar
hwCfgOperateLockConfigDataStore = _HwCfgOperateLockConfigDataStore_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 4, 1),
    _HwCfgOperateLockConfigDataStore_Type()
)
hwCfgOperateLockConfigDataStore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCfgOperateLockConfigDataStore.setStatus("current")
_HwCfgOperateLevelUsersTable_Object = MibTable
hwCfgOperateLevelUsersTable = _HwCfgOperateLevelUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hwCfgOperateLevelUsersTable.setStatus("current")
_HwCfgOperateLevelUsersEntry_Object = MibTableRow
hwCfgOperateLevelUsersEntry = _HwCfgOperateLevelUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 4, 2, 1)
)
hwCfgOperateLevelUsersEntry.setIndexNames(
    (0, "HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateLevelUsersSessionID"),
)
if mibBuilder.loadTexts:
    hwCfgOperateLevelUsersEntry.setStatus("current")


class _HwCfgOperateLevelUsersSessionID_Type(Integer32):
    """Custom type hwCfgOperateLevelUsersSessionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_HwCfgOperateLevelUsersSessionID_Type.__name__ = "Integer32"
_HwCfgOperateLevelUsersSessionID_Object = MibTableColumn
hwCfgOperateLevelUsersSessionID = _HwCfgOperateLevelUsersSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 4, 2, 1, 1),
    _HwCfgOperateLevelUsersSessionID_Type()
)
hwCfgOperateLevelUsersSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateLevelUsersSessionID.setStatus("current")
_HwCfgOperateLevelUsersSessionDesc_Type = DisplayString
_HwCfgOperateLevelUsersSessionDesc_Object = MibTableColumn
hwCfgOperateLevelUsersSessionDesc = _HwCfgOperateLevelUsersSessionDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 4, 2, 1, 2),
    _HwCfgOperateLevelUsersSessionDesc_Type()
)
hwCfgOperateLevelUsersSessionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateLevelUsersSessionDesc.setStatus("current")
_HwCfgOperateLevelUsersName_Type = DisplayString
_HwCfgOperateLevelUsersName_Object = MibTableColumn
hwCfgOperateLevelUsersName = _HwCfgOperateLevelUsersName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 4, 2, 1, 3),
    _HwCfgOperateLevelUsersName_Type()
)
hwCfgOperateLevelUsersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateLevelUsersName.setStatus("current")
_HwCfgOperateLevelUsersLockedTime_Type = DisplayString
_HwCfgOperateLevelUsersLockedTime_Object = MibTableColumn
hwCfgOperateLevelUsersLockedTime = _HwCfgOperateLevelUsersLockedTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 4, 2, 1, 4),
    _HwCfgOperateLevelUsersLockedTime_Type()
)
hwCfgOperateLevelUsersLockedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateLevelUsersLockedTime.setStatus("current")
_HwCfgOperateLevelUsersIPAddr_Type = DisplayString
_HwCfgOperateLevelUsersIPAddr_Object = MibTableColumn
hwCfgOperateLevelUsersIPAddr = _HwCfgOperateLevelUsersIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 4, 2, 1, 5),
    _HwCfgOperateLevelUsersIPAddr_Type()
)
hwCfgOperateLevelUsersIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateLevelUsersIPAddr.setStatus("current")
_HwCfgOperateLevelUsersLastCfgTime_Type = DisplayString
_HwCfgOperateLevelUsersLastCfgTime_Object = MibTableColumn
hwCfgOperateLevelUsersLastCfgTime = _HwCfgOperateLevelUsersLastCfgTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 4, 2, 1, 6),
    _HwCfgOperateLevelUsersLastCfgTime_Type()
)
hwCfgOperateLevelUsersLastCfgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateLevelUsersLastCfgTime.setStatus("current")


class _HwCfgOperateLevelUsersTimeout_Type(Integer32):
    """Custom type hwCfgOperateLevelUsersTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_HwCfgOperateLevelUsersTimeout_Type.__name__ = "Integer32"
_HwCfgOperateLevelUsersTimeout_Object = MibTableColumn
hwCfgOperateLevelUsersTimeout = _HwCfgOperateLevelUsersTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 1, 4, 2, 1, 7),
    _HwCfgOperateLevelUsersTimeout_Type()
)
hwCfgOperateLevelUsersTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgOperateLevelUsersTimeout.setStatus("current")
_HwConfigManNotifications_ObjectIdentity = ObjectIdentity
hwConfigManNotifications = _HwConfigManNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 2)
)
_HwConfigManConformance_ObjectIdentity = ObjectIdentity
hwConfigManConformance = _HwConfigManConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 3)
)
_HwConfigManCompliances_ObjectIdentity = ObjectIdentity
hwConfigManCompliances = _HwConfigManCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 3, 1)
)
_HwConfigManGroups_ObjectIdentity = ObjectIdentity
hwConfigManGroups = _HwConfigManGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 3, 2)
)

# Managed Objects groups

hwCfgManLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 3, 2, 1)
)
hwCfgManLogGroup.setObjects(
      *(("HUAWEI-CONFIG-MAN-MIB", "hwCfgRunModifiedLast"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgRunSavedLast"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgStartModifiedLast"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogLimitedEntries"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogDeletedEntries"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogTime"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogSrcCmd"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogTerminalType"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogTerminalNum"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogTerminalUser"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogTerminalLocation"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogCmdSrcAddress"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogVirHost"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogServerAddress"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogFile"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogUserName"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogWantBackup"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogSrcData"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogDesData"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogConfigChangeId"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogCfgBaselineTime"))
)
if mibBuilder.loadTexts:
    hwCfgManLogGroup.setStatus("current")

hwCfgOperateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 3, 2, 2)
)
hwCfgOperateGroup.setObjects(
      *(("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateGlobalEntryLimit"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateEntryAgeOutTime"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateType"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateProtocol"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateFileName"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateServerAddress"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateUserName"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateUserPassword"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateTime"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateEndNotificationSwitch"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateResultGlobalEntryLimit"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateState"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateRowStatus"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateServerPort"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateSourceAddress"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateSourceInterface"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateOnError"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateServerAddressType"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateServerAddressNet"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateVpnInstance"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateResultOptIndex"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateResultOpType"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateEndTime"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateTransferProgress"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateErrorReason"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgModuleChangeTime"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateLockConfigDataStore"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateLevelUsersSessionID"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateLevelUsersSessionDesc"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateLevelUsersName"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateLevelUsersLockedTime"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateLevelUsersIPAddr"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateLevelUsersLastCfgTime"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateLevelUsersTimeout"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateCompareConfig"))
)
if mibBuilder.loadTexts:
    hwCfgOperateGroup.setStatus("current")

hwCfgSaveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 3, 2, 4)
)
hwCfgSaveGroup.setObjects(
      *(("HUAWEI-CONFIG-MAN-MIB", "hwCfgSaveAutoInterval"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgSaveAutoTime"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgSaveManualTime"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgSaveAutoCpuLimit"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgSaveAutoNoCfgInterval"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgSaveAutoDelay"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgRestoreErrCode"))
)
if mibBuilder.loadTexts:
    hwCfgSaveGroup.setStatus("current")


# Notification objects

hwCfgManEventlog = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 2, 1)
)
hwCfgManEventlog.setObjects(
      *(("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogSrcCmd"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogSrcData"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogDesData"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogTerminalUser"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogCmdSrcAddress"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogConfigChangeId"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogTime"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgLogCfgBaselineTime"))
)
if mibBuilder.loadTexts:
    hwCfgManEventlog.setStatus(
        "current"
    )

hwCfgOperateCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 2, 2)
)
hwCfgOperateCompletion.setObjects(
      *(("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateType"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateTime"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateState"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateEndTime"))
)
if mibBuilder.loadTexts:
    hwCfgOperateCompletion.setStatus(
        "current"
    )

hwCfgInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 2, 3)
)
if mibBuilder.loadTexts:
    hwCfgInconsistent.setStatus(
        "obsolete"
    )

hwCfgInconsistentResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 2, 4)
)
if mibBuilder.loadTexts:
    hwCfgInconsistentResume.setStatus(
        "obsolete"
    )

hwCfgB2STransferFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 2, 5)
)
hwCfgB2STransferFail.setObjects(
      *(("HUAWEI-CONFIG-MAN-MIB", "hwCfgBackupIndex"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgBackupServerIp"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgBackupProtocol"))
)
if mibBuilder.loadTexts:
    hwCfgB2STransferFail.setStatus(
        "current"
    )

hwCfgB2SOperate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 2, 6)
)
if mibBuilder.loadTexts:
    hwCfgB2SOperate.setStatus(
        "current"
    )

hwCfgRestoreFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 2, 7)
)
hwCfgRestoreFail.setObjects(
    ("HUAWEI-CONFIG-MAN-MIB", "hwCfgRestoreErrCode")
)
if mibBuilder.loadTexts:
    hwCfgRestoreFail.setStatus(
        "current"
    )

hwConfigInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 2, 8)
)
if mibBuilder.loadTexts:
    hwConfigInconsistent.setStatus(
        "current"
    )

hwConfigConsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 2, 9)
)
if mibBuilder.loadTexts:
    hwConfigConsistent.setStatus(
        "current"
    )


# Notifications groups

hwCfgManNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 3, 2, 3)
)
hwCfgManNotificationGroup.setObjects(
      *(("HUAWEI-CONFIG-MAN-MIB", "hwCfgManEventlog"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgOperateCompletion"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgInconsistent"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgInconsistentResume"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgB2STransferFail"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgB2SOperate"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwCfgRestoreFail"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwConfigInconsistent"),
        ("HUAWEI-CONFIG-MAN-MIB", "hwConfigConsistent"))
)
if mibBuilder.loadTexts:
    hwCfgManNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwConfigManCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwConfigManCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-CONFIG-MAN-MIB",
    **{"ConfigOperationType": ConfigOperationType,
       "hwConfig": hwConfig,
       "hwConfigManObjects": hwConfigManObjects,
       "hwCfgLog": hwCfgLog,
       "hwCfgRunModifiedLast": hwCfgRunModifiedLast,
       "hwCfgRunSavedLast": hwCfgRunSavedLast,
       "hwCfgStartModifiedLast": hwCfgStartModifiedLast,
       "hwCfgLogLimitedEntries": hwCfgLogLimitedEntries,
       "hwCfgLogDeletedEntries": hwCfgLogDeletedEntries,
       "hwCfgLogWantBackup": hwCfgLogWantBackup,
       "hwCfgLogTable": hwCfgLogTable,
       "hwCfgLogEntry": hwCfgLogEntry,
       "hwCfgLogIndex": hwCfgLogIndex,
       "hwCfgLogTime": hwCfgLogTime,
       "hwCfgLogSrcCmd": hwCfgLogSrcCmd,
       "hwCfgLogSrcData": hwCfgLogSrcData,
       "hwCfgLogDesData": hwCfgLogDesData,
       "hwCfgLogTerminalType": hwCfgLogTerminalType,
       "hwCfgLogTerminalUser": hwCfgLogTerminalUser,
       "hwCfgLogTerminalNum": hwCfgLogTerminalNum,
       "hwCfgLogTerminalLocation": hwCfgLogTerminalLocation,
       "hwCfgLogCmdSrcAddress": hwCfgLogCmdSrcAddress,
       "hwCfgLogVirHost": hwCfgLogVirHost,
       "hwCfgLogUserName": hwCfgLogUserName,
       "hwCfgLogServerAddress": hwCfgLogServerAddress,
       "hwCfgLogFile": hwCfgLogFile,
       "hwCfgLogConfigChangeId": hwCfgLogConfigChangeId,
       "hwCfgLogCfgBaselineTime": hwCfgLogCfgBaselineTime,
       "hwCfgOperate": hwCfgOperate,
       "hwCfgOperateGlobalEntryLimit": hwCfgOperateGlobalEntryLimit,
       "hwCfgOperateEntryAgeOutTime": hwCfgOperateEntryAgeOutTime,
       "hwCfgOperateResultGlobalEntryLimit": hwCfgOperateResultGlobalEntryLimit,
       "hwCfgOperateTable": hwCfgOperateTable,
       "hwCfgOperateEntry": hwCfgOperateEntry,
       "hwCfgOperateIndex": hwCfgOperateIndex,
       "hwCfgOperateType": hwCfgOperateType,
       "hwCfgOperateProtocol": hwCfgOperateProtocol,
       "hwCfgOperateFileName": hwCfgOperateFileName,
       "hwCfgOperateServerAddress": hwCfgOperateServerAddress,
       "hwCfgOperateUserName": hwCfgOperateUserName,
       "hwCfgOperateUserPassword": hwCfgOperateUserPassword,
       "hwCfgOperateEndNotificationSwitch": hwCfgOperateEndNotificationSwitch,
       "hwCfgOperateRowStatus": hwCfgOperateRowStatus,
       "hwCfgOperateServerPort": hwCfgOperateServerPort,
       "hwCfgOperateSourceAddress": hwCfgOperateSourceAddress,
       "hwCfgOperateSourceInterface": hwCfgOperateSourceInterface,
       "hwCfgOperateOnError": hwCfgOperateOnError,
       "hwCfgOperateServerAddressType": hwCfgOperateServerAddressType,
       "hwCfgOperateServerAddressNet": hwCfgOperateServerAddressNet,
       "hwCfgOperateVpnInstance": hwCfgOperateVpnInstance,
       "hwCfgOperateResultTable": hwCfgOperateResultTable,
       "hwCfgOperateResultEntry": hwCfgOperateResultEntry,
       "hwCfgOperateResultIndex": hwCfgOperateResultIndex,
       "hwCfgOperateResultOptIndex": hwCfgOperateResultOptIndex,
       "hwCfgOperateResultOpType": hwCfgOperateResultOpType,
       "hwCfgOperateState": hwCfgOperateState,
       "hwCfgOperateTime": hwCfgOperateTime,
       "hwCfgOperateEndTime": hwCfgOperateEndTime,
       "hwCfgOperateTransferProgress": hwCfgOperateTransferProgress,
       "hwCfgOperateErrorReason": hwCfgOperateErrorReason,
       "hwCfgModuleChangeTimeTable": hwCfgModuleChangeTimeTable,
       "hwCfgModuleChangeTimeEntry": hwCfgModuleChangeTimeEntry,
       "hwCfgModuleId": hwCfgModuleId,
       "hwCfgModuleChangeTime": hwCfgModuleChangeTime,
       "hwCfgOperateCompareConfig": hwCfgOperateCompareConfig,
       "hwCfgRestoreErrCode": hwCfgRestoreErrCode,
       "hwCfgSave": hwCfgSave,
       "hwCfgSaveAutoInterval": hwCfgSaveAutoInterval,
       "hwCfgSaveAutoTime": hwCfgSaveAutoTime,
       "hwCfgSaveManualTime": hwCfgSaveManualTime,
       "hwCfgSaveAutoCpuLimit": hwCfgSaveAutoCpuLimit,
       "hwCfgSaveAutoNoCfgInterval": hwCfgSaveAutoNoCfgInterval,
       "hwCfgSaveAutoDelay": hwCfgSaveAutoDelay,
       "hwCfgBackup2ServerTable": hwCfgBackup2ServerTable,
       "hwCfgBackup2ServerEntry": hwCfgBackup2ServerEntry,
       "hwCfgBackupIndex": hwCfgBackupIndex,
       "hwCfgBackupServerIp": hwCfgBackupServerIp,
       "hwCfgBackupProtocol": hwCfgBackupProtocol,
       "hwCfgBackupUser": hwCfgBackupUser,
       "hwCfgBackupPassword": hwCfgBackupPassword,
       "hwCfgBackupServerPath": hwCfgBackupServerPath,
       "hwCfgBackupRowStatus": hwCfgBackupRowStatus,
       "hwCfgBackupResult": hwCfgBackupResult,
       "hwCfgBackupVpnInstance": hwCfgBackupVpnInstance,
       "hwCfgLock": hwCfgLock,
       "hwCfgOperateLockConfigDataStore": hwCfgOperateLockConfigDataStore,
       "hwCfgOperateLevelUsersTable": hwCfgOperateLevelUsersTable,
       "hwCfgOperateLevelUsersEntry": hwCfgOperateLevelUsersEntry,
       "hwCfgOperateLevelUsersSessionID": hwCfgOperateLevelUsersSessionID,
       "hwCfgOperateLevelUsersSessionDesc": hwCfgOperateLevelUsersSessionDesc,
       "hwCfgOperateLevelUsersName": hwCfgOperateLevelUsersName,
       "hwCfgOperateLevelUsersLockedTime": hwCfgOperateLevelUsersLockedTime,
       "hwCfgOperateLevelUsersIPAddr": hwCfgOperateLevelUsersIPAddr,
       "hwCfgOperateLevelUsersLastCfgTime": hwCfgOperateLevelUsersLastCfgTime,
       "hwCfgOperateLevelUsersTimeout": hwCfgOperateLevelUsersTimeout,
       "hwConfigManNotifications": hwConfigManNotifications,
       "hwCfgManEventlog": hwCfgManEventlog,
       "hwCfgOperateCompletion": hwCfgOperateCompletion,
       "hwCfgInconsistent": hwCfgInconsistent,
       "hwCfgInconsistentResume": hwCfgInconsistentResume,
       "hwCfgB2STransferFail": hwCfgB2STransferFail,
       "hwCfgB2SOperate": hwCfgB2SOperate,
       "hwCfgRestoreFail": hwCfgRestoreFail,
       "hwConfigInconsistent": hwConfigInconsistent,
       "hwConfigConsistent": hwConfigConsistent,
       "hwConfigManConformance": hwConfigManConformance,
       "hwConfigManCompliances": hwConfigManCompliances,
       "hwConfigManCompliance": hwConfigManCompliance,
       "hwConfigManGroups": hwConfigManGroups,
       "hwCfgManLogGroup": hwCfgManLogGroup,
       "hwCfgOperateGroup": hwCfgOperateGroup,
       "hwCfgManNotificationGroup": hwCfgManNotificationGroup,
       "hwCfgSaveGroup": hwCfgSaveGroup}
)
