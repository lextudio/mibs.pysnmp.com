# SNMP MIB module (DOCS-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-DIAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:34 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(docsDevEvId,
 docsDevEvLevel) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevEvId",
    "docsDevEvLevel")

(CmtsCmRegState,
 docsIf3CmtsCmRegStatusId) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "CmtsCmRegState",
    "docsIf3CmtsCmRegStatusId")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsDiagMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9)
)
docsDiagMib.setRevisions(
        ("2007-12-06 00:00",
         "2007-05-18 00:00",
         "2006-12-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TriggerFlag(Bits, TextualConvention):
    status = "current"


class RegistrationDetailFlag(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_DocsDiagLogNotifications_ObjectIdentity = ObjectIdentity
docsDiagLogNotifications = _DocsDiagLogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 0)
)
_DocsDiagLogMibObjects_ObjectIdentity = ObjectIdentity
docsDiagLogMibObjects = _DocsDiagLogMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1)
)
_DocsDiagLogGlobal_ObjectIdentity = ObjectIdentity
docsDiagLogGlobal = _DocsDiagLogGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 1)
)


class _DocsDiagLogMaxSize_Type(Unsigned32):
    """Custom type docsDiagLogMaxSize based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsDiagLogMaxSize_Type.__name__ = "Unsigned32"
_DocsDiagLogMaxSize_Object = MibScalar
docsDiagLogMaxSize = _DocsDiagLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 1, 1),
    _DocsDiagLogMaxSize_Type()
)
docsDiagLogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    docsDiagLogMaxSize.setUnits("entries")


class _DocsDiagLogCurrentSize_Type(Gauge32):
    """Custom type docsDiagLogCurrentSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsDiagLogCurrentSize_Type.__name__ = "Gauge32"
_DocsDiagLogCurrentSize_Object = MibScalar
docsDiagLogCurrentSize = _DocsDiagLogCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 1, 2),
    _DocsDiagLogCurrentSize_Type()
)
docsDiagLogCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogCurrentSize.setStatus("current")
if mibBuilder.loadTexts:
    docsDiagLogCurrentSize.setUnits("entries")


class _DocsDiagLogNotifyLogSizeHighThrshld_Type(Unsigned32):
    """Custom type docsDiagLogNotifyLogSizeHighThrshld based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsDiagLogNotifyLogSizeHighThrshld_Type.__name__ = "Unsigned32"
_DocsDiagLogNotifyLogSizeHighThrshld_Object = MibScalar
docsDiagLogNotifyLogSizeHighThrshld = _DocsDiagLogNotifyLogSizeHighThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 1, 3),
    _DocsDiagLogNotifyLogSizeHighThrshld_Type()
)
docsDiagLogNotifyLogSizeHighThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogNotifyLogSizeHighThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsDiagLogNotifyLogSizeHighThrshld.setUnits("entries")


class _DocsDiagLogNotifyLogSizeLowThrshld_Type(Unsigned32):
    """Custom type docsDiagLogNotifyLogSizeLowThrshld based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsDiagLogNotifyLogSizeLowThrshld_Type.__name__ = "Unsigned32"
_DocsDiagLogNotifyLogSizeLowThrshld_Object = MibScalar
docsDiagLogNotifyLogSizeLowThrshld = _DocsDiagLogNotifyLogSizeLowThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 1, 4),
    _DocsDiagLogNotifyLogSizeLowThrshld_Type()
)
docsDiagLogNotifyLogSizeLowThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogNotifyLogSizeLowThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsDiagLogNotifyLogSizeLowThrshld.setUnits("entries")


class _DocsDiagLogAging_Type(Unsigned32):
    """Custom type docsDiagLogAging based on Unsigned32"""
    defaultValue = 10080

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_DocsDiagLogAging_Type.__name__ = "Unsigned32"
_DocsDiagLogAging_Object = MibScalar
docsDiagLogAging = _DocsDiagLogAging_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 1, 5),
    _DocsDiagLogAging_Type()
)
docsDiagLogAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogAging.setStatus("current")
if mibBuilder.loadTexts:
    docsDiagLogAging.setUnits("minutes")
_DocsDiagLogResetAll_Type = TruthValue
_DocsDiagLogResetAll_Object = MibScalar
docsDiagLogResetAll = _DocsDiagLogResetAll_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 1, 6),
    _DocsDiagLogResetAll_Type()
)
docsDiagLogResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogResetAll.setStatus("current")
_DocsDiagLogLastResetTime_Type = DateAndTime
_DocsDiagLogLastResetTime_Object = MibScalar
docsDiagLogLastResetTime = _DocsDiagLogLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 1, 7),
    _DocsDiagLogLastResetTime_Type()
)
docsDiagLogLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogLastResetTime.setStatus("current")
_DocsDiagLogClearAll_Type = TruthValue
_DocsDiagLogClearAll_Object = MibScalar
docsDiagLogClearAll = _DocsDiagLogClearAll_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 1, 8),
    _DocsDiagLogClearAll_Type()
)
docsDiagLogClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogClearAll.setStatus("current")
_DocsDiagLogLastClearTime_Type = DateAndTime
_DocsDiagLogLastClearTime_Object = MibScalar
docsDiagLogLastClearTime = _DocsDiagLogLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 1, 9),
    _DocsDiagLogLastClearTime_Type()
)
docsDiagLogLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogLastClearTime.setStatus("current")


class _DocsDiagLogNotifCtrl_Type(Bits):
    """Custom type docsDiagLogNotifCtrl based on Bits"""
    defaultHexValue = ""

    namedValues = NamedValues(
        *(("full", 2),
          ("highThresholdReached", 0),
          ("lowThresholdReached", 1))
    )

_DocsDiagLogNotifCtrl_Type.__name__ = "Bits"
_DocsDiagLogNotifCtrl_Object = MibScalar
docsDiagLogNotifCtrl = _DocsDiagLogNotifCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 1, 10),
    _DocsDiagLogNotifCtrl_Type()
)
docsDiagLogNotifCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogNotifCtrl.setStatus("current")
_DocsDiagLogTriggersCfg_ObjectIdentity = ObjectIdentity
docsDiagLogTriggersCfg = _DocsDiagLogTriggersCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 2)
)


class _DocsDiagLogIncludeTriggers_Type(TriggerFlag):
    """Custom type docsDiagLogIncludeTriggers based on TriggerFlag"""
    defaultHexValue = "C0"


_DocsDiagLogIncludeTriggers_Object = MibScalar
docsDiagLogIncludeTriggers = _DocsDiagLogIncludeTriggers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 2, 1),
    _DocsDiagLogIncludeTriggers_Type()
)
docsDiagLogIncludeTriggers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogIncludeTriggers.setStatus("current")


class _DocsDiagLogEnableAgingTriggers_Type(TriggerFlag):
    """Custom type docsDiagLogEnableAgingTriggers based on TriggerFlag"""
    defaultHexValue = ""


_DocsDiagLogEnableAgingTriggers_Object = MibScalar
docsDiagLogEnableAgingTriggers = _DocsDiagLogEnableAgingTriggers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 2, 2),
    _DocsDiagLogEnableAgingTriggers_Type()
)
docsDiagLogEnableAgingTriggers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogEnableAgingTriggers.setStatus("current")


class _DocsDiagLogRegTimeInterval_Type(Unsigned32):
    """Custom type docsDiagLogRegTimeInterval based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_DocsDiagLogRegTimeInterval_Type.__name__ = "Unsigned32"
_DocsDiagLogRegTimeInterval_Object = MibScalar
docsDiagLogRegTimeInterval = _DocsDiagLogRegTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 2, 3),
    _DocsDiagLogRegTimeInterval_Type()
)
docsDiagLogRegTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogRegTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsDiagLogRegTimeInterval.setUnits("seconds")


class _DocsDiagLogRegDetail_Type(RegistrationDetailFlag):
    """Custom type docsDiagLogRegDetail based on RegistrationDetailFlag"""
    defaultHexValue = ""


_DocsDiagLogRegDetail_Object = MibScalar
docsDiagLogRegDetail = _DocsDiagLogRegDetail_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 2, 4),
    _DocsDiagLogRegDetail_Type()
)
docsDiagLogRegDetail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogRegDetail.setStatus("current")


class _DocsDiagLogRangingRetryType_Type(Integer32):
    """Custom type docsDiagLogRangingRetryType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("consecutiveMiss", 1),
          ("missRatio", 2))
    )


_DocsDiagLogRangingRetryType_Type.__name__ = "Integer32"
_DocsDiagLogRangingRetryType_Object = MibScalar
docsDiagLogRangingRetryType = _DocsDiagLogRangingRetryType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 2, 5),
    _DocsDiagLogRangingRetryType_Type()
)
docsDiagLogRangingRetryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogRangingRetryType.setStatus("current")


class _DocsDiagLogRangingRetryThrhld_Type(Unsigned32):
    """Custom type docsDiagLogRangingRetryThrhld based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 12),
    )


_DocsDiagLogRangingRetryThrhld_Type.__name__ = "Unsigned32"
_DocsDiagLogRangingRetryThrhld_Object = MibScalar
docsDiagLogRangingRetryThrhld = _DocsDiagLogRangingRetryThrhld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 2, 6),
    _DocsDiagLogRangingRetryThrhld_Type()
)
docsDiagLogRangingRetryThrhld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogRangingRetryThrhld.setStatus("current")


class _DocsDiagLogRangingRetryStationMaintNum_Type(Unsigned32):
    """Custom type docsDiagLogRangingRetryStationMaintNum based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_DocsDiagLogRangingRetryStationMaintNum_Type.__name__ = "Unsigned32"
_DocsDiagLogRangingRetryStationMaintNum_Object = MibScalar
docsDiagLogRangingRetryStationMaintNum = _DocsDiagLogRangingRetryStationMaintNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 2, 7),
    _DocsDiagLogRangingRetryStationMaintNum_Type()
)
docsDiagLogRangingRetryStationMaintNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDiagLogRangingRetryStationMaintNum.setStatus("current")
_DocsDiagLogTable_Object = MibTable
docsDiagLogTable = _DocsDiagLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    docsDiagLogTable.setStatus("current")
_DocsDiagLogEntry_Object = MibTableRow
docsDiagLogEntry = _DocsDiagLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 3, 1)
)
docsDiagLogEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
)
if mibBuilder.loadTexts:
    docsDiagLogEntry.setStatus("current")
_DocsDiagLogCmMacAddr_Type = MacAddress
_DocsDiagLogCmMacAddr_Object = MibTableColumn
docsDiagLogCmMacAddr = _DocsDiagLogCmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 3, 1, 1),
    _DocsDiagLogCmMacAddr_Type()
)
docsDiagLogCmMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogCmMacAddr.setStatus("current")
_DocsDiagLogLastUpdateTime_Type = DateAndTime
_DocsDiagLogLastUpdateTime_Object = MibTableColumn
docsDiagLogLastUpdateTime = _DocsDiagLogLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 3, 1, 2),
    _DocsDiagLogLastUpdateTime_Type()
)
docsDiagLogLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogLastUpdateTime.setStatus("current")
_DocsDiagLogCreateTime_Type = DateAndTime
_DocsDiagLogCreateTime_Object = MibTableColumn
docsDiagLogCreateTime = _DocsDiagLogCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 3, 1, 3),
    _DocsDiagLogCreateTime_Type()
)
docsDiagLogCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogCreateTime.setStatus("current")
_DocsDiagLogLastRegTime_Type = DateAndTime
_DocsDiagLogLastRegTime_Object = MibTableColumn
docsDiagLogLastRegTime = _DocsDiagLogLastRegTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 3, 1, 4),
    _DocsDiagLogLastRegTime_Type()
)
docsDiagLogLastRegTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogLastRegTime.setStatus("current")
_DocsDiagLogRegCount_Type = Counter32
_DocsDiagLogRegCount_Object = MibTableColumn
docsDiagLogRegCount = _DocsDiagLogRegCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 3, 1, 5),
    _DocsDiagLogRegCount_Type()
)
docsDiagLogRegCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogRegCount.setStatus("current")
_DocsDiagLogRangingRetryCount_Type = Counter32
_DocsDiagLogRangingRetryCount_Object = MibTableColumn
docsDiagLogRangingRetryCount = _DocsDiagLogRangingRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 3, 1, 6),
    _DocsDiagLogRangingRetryCount_Type()
)
docsDiagLogRangingRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogRangingRetryCount.setStatus("current")
_DocsDiagLogDetailTable_Object = MibTable
docsDiagLogDetailTable = _DocsDiagLogDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 4)
)
if mibBuilder.loadTexts:
    docsDiagLogDetailTable.setStatus("current")
_DocsDiagLogDetailEntry_Object = MibTableRow
docsDiagLogDetailEntry = _DocsDiagLogDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 4, 1)
)
docsDiagLogDetailEntry.setIndexNames(
    (0, "DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusId"),
    (0, "DOCS-DIAG-MIB", "docsDiagLogDetailTypeValue"),
)
if mibBuilder.loadTexts:
    docsDiagLogDetailEntry.setStatus("current")
_DocsDiagLogDetailTypeValue_Type = CmtsCmRegState
_DocsDiagLogDetailTypeValue_Object = MibTableColumn
docsDiagLogDetailTypeValue = _DocsDiagLogDetailTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 4, 1, 1),
    _DocsDiagLogDetailTypeValue_Type()
)
docsDiagLogDetailTypeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDiagLogDetailTypeValue.setStatus("current")
_DocsDiagLogDetailCount_Type = Counter32
_DocsDiagLogDetailCount_Object = MibTableColumn
docsDiagLogDetailCount = _DocsDiagLogDetailCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 4, 1, 2),
    _DocsDiagLogDetailCount_Type()
)
docsDiagLogDetailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogDetailCount.setStatus("current")
_DocsDiagLogDetailLastUpdate_Type = DateAndTime
_DocsDiagLogDetailLastUpdate_Object = MibTableColumn
docsDiagLogDetailLastUpdate = _DocsDiagLogDetailLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 4, 1, 3),
    _DocsDiagLogDetailLastUpdate_Type()
)
docsDiagLogDetailLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogDetailLastUpdate.setStatus("current")
_DocsDiagLogDetailLastErrorText_Type = SnmpAdminString
_DocsDiagLogDetailLastErrorText_Object = MibTableColumn
docsDiagLogDetailLastErrorText = _DocsDiagLogDetailLastErrorText_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 1, 4, 1, 4),
    _DocsDiagLogDetailLastErrorText_Type()
)
docsDiagLogDetailLastErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDiagLogDetailLastErrorText.setStatus("current")
_DocsDiagLogConformance_ObjectIdentity = ObjectIdentity
docsDiagLogConformance = _DocsDiagLogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 2)
)
_DocsDiagLogCompliances_ObjectIdentity = ObjectIdentity
docsDiagLogCompliances = _DocsDiagLogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 2, 1)
)
_DocsDiagLogGroups_ObjectIdentity = ObjectIdentity
docsDiagLogGroups = _DocsDiagLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 2, 2)
)

# Managed Objects groups

docsDiagLogBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 2, 2, 1)
)
docsDiagLogBaseGroup.setObjects(
      *(("DOCS-DIAG-MIB", "docsDiagLogMaxSize"),
        ("DOCS-DIAG-MIB", "docsDiagLogCurrentSize"),
        ("DOCS-DIAG-MIB", "docsDiagLogNotifyLogSizeHighThrshld"),
        ("DOCS-DIAG-MIB", "docsDiagLogNotifyLogSizeLowThrshld"),
        ("DOCS-DIAG-MIB", "docsDiagLogAging"),
        ("DOCS-DIAG-MIB", "docsDiagLogResetAll"),
        ("DOCS-DIAG-MIB", "docsDiagLogLastResetTime"),
        ("DOCS-DIAG-MIB", "docsDiagLogClearAll"),
        ("DOCS-DIAG-MIB", "docsDiagLogLastClearTime"),
        ("DOCS-DIAG-MIB", "docsDiagLogNotifCtrl"),
        ("DOCS-DIAG-MIB", "docsDiagLogIncludeTriggers"),
        ("DOCS-DIAG-MIB", "docsDiagLogEnableAgingTriggers"),
        ("DOCS-DIAG-MIB", "docsDiagLogRegTimeInterval"),
        ("DOCS-DIAG-MIB", "docsDiagLogRegDetail"),
        ("DOCS-DIAG-MIB", "docsDiagLogRangingRetryType"),
        ("DOCS-DIAG-MIB", "docsDiagLogRangingRetryThrhld"),
        ("DOCS-DIAG-MIB", "docsDiagLogRangingRetryStationMaintNum"),
        ("DOCS-DIAG-MIB", "docsDiagLogCmMacAddr"),
        ("DOCS-DIAG-MIB", "docsDiagLogLastUpdateTime"),
        ("DOCS-DIAG-MIB", "docsDiagLogCreateTime"),
        ("DOCS-DIAG-MIB", "docsDiagLogLastRegTime"),
        ("DOCS-DIAG-MIB", "docsDiagLogRegCount"),
        ("DOCS-DIAG-MIB", "docsDiagLogRangingRetryCount"),
        ("DOCS-DIAG-MIB", "docsDiagLogDetailCount"),
        ("DOCS-DIAG-MIB", "docsDiagLogDetailLastUpdate"),
        ("DOCS-DIAG-MIB", "docsDiagLogDetailLastErrorText"))
)
if mibBuilder.loadTexts:
    docsDiagLogBaseGroup.setStatus("current")


# Notification objects

docsDiagLogSizeHighThrshldReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 0, 1)
)
docsDiagLogSizeHighThrshldReached.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-DIAG-MIB", "docsDiagLogIncludeTriggers"),
        ("DOCS-DIAG-MIB", "docsDiagLogMaxSize"))
)
if mibBuilder.loadTexts:
    docsDiagLogSizeHighThrshldReached.setStatus(
        "current"
    )

docsDiagLogSizeLowThrshldReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 0, 2)
)
docsDiagLogSizeLowThrshldReached.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-DIAG-MIB", "docsDiagLogIncludeTriggers"),
        ("DOCS-DIAG-MIB", "docsDiagLogMaxSize"))
)
if mibBuilder.loadTexts:
    docsDiagLogSizeLowThrshldReached.setStatus(
        "current"
    )

docsDiagLogSizeFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 0, 3)
)
docsDiagLogSizeFull.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-DIAG-MIB", "docsDiagLogIncludeTriggers"),
        ("DOCS-DIAG-MIB", "docsDiagLogMaxSize"))
)
if mibBuilder.loadTexts:
    docsDiagLogSizeFull.setStatus(
        "current"
    )


# Notifications groups

docsDiagLogNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 2, 2, 2)
)
docsDiagLogNotificationGroup.setObjects(
      *(("DOCS-DIAG-MIB", "docsDiagLogSizeHighThrshldReached"),
        ("DOCS-DIAG-MIB", "docsDiagLogSizeLowThrshldReached"),
        ("DOCS-DIAG-MIB", "docsDiagLogSizeFull"))
)
if mibBuilder.loadTexts:
    docsDiagLogNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

docsDiagLogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsDiagLogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-DIAG-MIB",
    **{"TriggerFlag": TriggerFlag,
       "RegistrationDetailFlag": RegistrationDetailFlag,
       "docsDiagMib": docsDiagMib,
       "docsDiagLogNotifications": docsDiagLogNotifications,
       "docsDiagLogSizeHighThrshldReached": docsDiagLogSizeHighThrshldReached,
       "docsDiagLogSizeLowThrshldReached": docsDiagLogSizeLowThrshldReached,
       "docsDiagLogSizeFull": docsDiagLogSizeFull,
       "docsDiagLogMibObjects": docsDiagLogMibObjects,
       "docsDiagLogGlobal": docsDiagLogGlobal,
       "docsDiagLogMaxSize": docsDiagLogMaxSize,
       "docsDiagLogCurrentSize": docsDiagLogCurrentSize,
       "docsDiagLogNotifyLogSizeHighThrshld": docsDiagLogNotifyLogSizeHighThrshld,
       "docsDiagLogNotifyLogSizeLowThrshld": docsDiagLogNotifyLogSizeLowThrshld,
       "docsDiagLogAging": docsDiagLogAging,
       "docsDiagLogResetAll": docsDiagLogResetAll,
       "docsDiagLogLastResetTime": docsDiagLogLastResetTime,
       "docsDiagLogClearAll": docsDiagLogClearAll,
       "docsDiagLogLastClearTime": docsDiagLogLastClearTime,
       "docsDiagLogNotifCtrl": docsDiagLogNotifCtrl,
       "docsDiagLogTriggersCfg": docsDiagLogTriggersCfg,
       "docsDiagLogIncludeTriggers": docsDiagLogIncludeTriggers,
       "docsDiagLogEnableAgingTriggers": docsDiagLogEnableAgingTriggers,
       "docsDiagLogRegTimeInterval": docsDiagLogRegTimeInterval,
       "docsDiagLogRegDetail": docsDiagLogRegDetail,
       "docsDiagLogRangingRetryType": docsDiagLogRangingRetryType,
       "docsDiagLogRangingRetryThrhld": docsDiagLogRangingRetryThrhld,
       "docsDiagLogRangingRetryStationMaintNum": docsDiagLogRangingRetryStationMaintNum,
       "docsDiagLogTable": docsDiagLogTable,
       "docsDiagLogEntry": docsDiagLogEntry,
       "docsDiagLogCmMacAddr": docsDiagLogCmMacAddr,
       "docsDiagLogLastUpdateTime": docsDiagLogLastUpdateTime,
       "docsDiagLogCreateTime": docsDiagLogCreateTime,
       "docsDiagLogLastRegTime": docsDiagLogLastRegTime,
       "docsDiagLogRegCount": docsDiagLogRegCount,
       "docsDiagLogRangingRetryCount": docsDiagLogRangingRetryCount,
       "docsDiagLogDetailTable": docsDiagLogDetailTable,
       "docsDiagLogDetailEntry": docsDiagLogDetailEntry,
       "docsDiagLogDetailTypeValue": docsDiagLogDetailTypeValue,
       "docsDiagLogDetailCount": docsDiagLogDetailCount,
       "docsDiagLogDetailLastUpdate": docsDiagLogDetailLastUpdate,
       "docsDiagLogDetailLastErrorText": docsDiagLogDetailLastErrorText,
       "docsDiagLogConformance": docsDiagLogConformance,
       "docsDiagLogCompliances": docsDiagLogCompliances,
       "docsDiagLogCompliance": docsDiagLogCompliance,
       "docsDiagLogGroups": docsDiagLogGroups,
       "docsDiagLogBaseGroup": docsDiagLogBaseGroup,
       "docsDiagLogNotificationGroup": docsDiagLogNotificationGroup}
)
