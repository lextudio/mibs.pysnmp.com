# SNMP MIB module (Wellfleet-ACCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-ACCT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:43 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfAcctGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfAcctGroup")


# MODULE-IDENTITY


# Types definitions



class RtrTimeStamp(Integer32):
    """Custom type RtrTimeStamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfAcct_ObjectIdentity = ObjectIdentity
wfAcct = _WfAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1)
)


class _WfAcctCreate_Type(Integer32):
    """Custom type wfAcctCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAcctCreate_Type.__name__ = "Integer32"
_WfAcctCreate_Object = MibScalar
wfAcctCreate = _WfAcctCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 1),
    _WfAcctCreate_Type()
)
wfAcctCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctCreate.setStatus("mandatory")


class _WfAcctEnable_Type(Integer32):
    """Custom type wfAcctEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfAcctEnable_Type.__name__ = "Integer32"
_WfAcctEnable_Object = MibScalar
wfAcctEnable = _WfAcctEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 2),
    _WfAcctEnable_Type()
)
wfAcctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctEnable.setStatus("mandatory")


class _WfAcctOperState_Type(Integer32):
    """Custom type wfAcctOperState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfAcctOperState_Type.__name__ = "Integer32"
_WfAcctOperState_Object = MibScalar
wfAcctOperState = _WfAcctOperState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 3),
    _WfAcctOperState_Type()
)
wfAcctOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctOperState.setStatus("mandatory")


class _WfAcctLogLevel_Type(Integer32):
    """Custom type wfAcctLogLevel based on Integer32"""
    defaultValue = 917504

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65536,
              131072,
              262144,
              524288,
              917504,
              1048576,
              2031616)
        )
    )
    namedValues = NamedValues(
        *(("all", 2031616),
          ("debug", 65536),
          ("fault", 524288),
          ("info", 131072),
          ("infofaultwarning", 917504),
          ("trace", 1048576),
          ("warning", 262144))
    )


_WfAcctLogLevel_Type.__name__ = "Integer32"
_WfAcctLogLevel_Object = MibScalar
wfAcctLogLevel = _WfAcctLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 4),
    _WfAcctLogLevel_Type()
)
wfAcctLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctLogLevel.setStatus("mandatory")


class _WfAcctCircularSnapshotFlag_Type(Integer32):
    """Custom type wfAcctCircularSnapshotFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfAcctCircularSnapshotFlag_Type.__name__ = "Integer32"
_WfAcctCircularSnapshotFlag_Object = MibScalar
wfAcctCircularSnapshotFlag = _WfAcctCircularSnapshotFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 5),
    _WfAcctCircularSnapshotFlag_Type()
)
wfAcctCircularSnapshotFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctCircularSnapshotFlag.setStatus("mandatory")


class _WfAcctCollectDuration_Type(Integer32):
    """Custom type wfAcctCollectDuration based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_WfAcctCollectDuration_Type.__name__ = "Integer32"
_WfAcctCollectDuration_Object = MibScalar
wfAcctCollectDuration = _WfAcctCollectDuration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 6),
    _WfAcctCollectDuration_Type()
)
wfAcctCollectDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctCollectDuration.setStatus("mandatory")


class _WfAcctUpdateInterval_Type(Integer32):
    """Custom type wfAcctUpdateInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 360),
    )


_WfAcctUpdateInterval_Type.__name__ = "Integer32"
_WfAcctUpdateInterval_Object = MibScalar
wfAcctUpdateInterval = _WfAcctUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 7),
    _WfAcctUpdateInterval_Type()
)
wfAcctUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctUpdateInterval.setStatus("mandatory")


class _WfAcctFlushOnRetrieval_Type(Integer32):
    """Custom type wfAcctFlushOnRetrieval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfAcctFlushOnRetrieval_Type.__name__ = "Integer32"
_WfAcctFlushOnRetrieval_Object = MibScalar
wfAcctFlushOnRetrieval = _WfAcctFlushOnRetrieval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 8),
    _WfAcctFlushOnRetrieval_Type()
)
wfAcctFlushOnRetrieval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctFlushOnRetrieval.setStatus("mandatory")


class _WfAcctFlushData_Type(Integer32):
    """Custom type wfAcctFlushData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_WfAcctFlushData_Type.__name__ = "Integer32"
_WfAcctFlushData_Object = MibScalar
wfAcctFlushData = _WfAcctFlushData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 9),
    _WfAcctFlushData_Type()
)
wfAcctFlushData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctFlushData.setStatus("mandatory")
_WfAcctLastUpdateTimeStampHigh_Type = RtrTimeStamp
_WfAcctLastUpdateTimeStampHigh_Object = MibScalar
wfAcctLastUpdateTimeStampHigh = _WfAcctLastUpdateTimeStampHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 10),
    _WfAcctLastUpdateTimeStampHigh_Type()
)
wfAcctLastUpdateTimeStampHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctLastUpdateTimeStampHigh.setStatus("mandatory")
_WfAcctLastUpdateTimeStampLow_Type = RtrTimeStamp
_WfAcctLastUpdateTimeStampLow_Object = MibScalar
wfAcctLastUpdateTimeStampLow = _WfAcctLastUpdateTimeStampLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 11),
    _WfAcctLastUpdateTimeStampLow_Type()
)
wfAcctLastUpdateTimeStampLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctLastUpdateTimeStampLow.setStatus("mandatory")
_WfAcctLastFlushTimeStampHigh_Type = RtrTimeStamp
_WfAcctLastFlushTimeStampHigh_Object = MibScalar
wfAcctLastFlushTimeStampHigh = _WfAcctLastFlushTimeStampHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 12),
    _WfAcctLastFlushTimeStampHigh_Type()
)
wfAcctLastFlushTimeStampHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctLastFlushTimeStampHigh.setStatus("mandatory")
_WfAcctLastFlushTimeStampLow_Type = RtrTimeStamp
_WfAcctLastFlushTimeStampLow_Object = MibScalar
wfAcctLastFlushTimeStampLow = _WfAcctLastFlushTimeStampLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 13),
    _WfAcctLastFlushTimeStampLow_Type()
)
wfAcctLastFlushTimeStampLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctLastFlushTimeStampLow.setStatus("mandatory")


class _WfAcctRuleNumEntries_Type(Integer32):
    """Custom type wfAcctRuleNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfAcctRuleNumEntries_Type.__name__ = "Integer32"
_WfAcctRuleNumEntries_Object = MibScalar
wfAcctRuleNumEntries = _WfAcctRuleNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 14),
    _WfAcctRuleNumEntries_Type()
)
wfAcctRuleNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctRuleNumEntries.setStatus("mandatory")


class _WfAcctCtrlNumEntries_Type(Integer32):
    """Custom type wfAcctCtrlNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfAcctCtrlNumEntries_Type.__name__ = "Integer32"
_WfAcctCtrlNumEntries_Object = MibScalar
wfAcctCtrlNumEntries = _WfAcctCtrlNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 15),
    _WfAcctCtrlNumEntries_Type()
)
wfAcctCtrlNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctCtrlNumEntries.setStatus("mandatory")


class _WfAcctDataNumEntries_Type(Integer32):
    """Custom type wfAcctDataNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfAcctDataNumEntries_Type.__name__ = "Integer32"
_WfAcctDataNumEntries_Object = MibScalar
wfAcctDataNumEntries = _WfAcctDataNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 16),
    _WfAcctDataNumEntries_Type()
)
wfAcctDataNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctDataNumEntries.setStatus("mandatory")
_WfAcctRuleTable_Object = MibTable
wfAcctRuleTable = _WfAcctRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2)
)
if mibBuilder.loadTexts:
    wfAcctRuleTable.setStatus("mandatory")
_WfAcctRuleEntry_Object = MibTableRow
wfAcctRuleEntry = _WfAcctRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1)
)
wfAcctRuleEntry.setIndexNames(
    (0, "Wellfleet-ACCT-MIB", "wfAcctRuleNumber"),
)
if mibBuilder.loadTexts:
    wfAcctRuleEntry.setStatus("mandatory")


class _WfAcctRuleCreate_Type(Integer32):
    """Custom type wfAcctRuleCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAcctRuleCreate_Type.__name__ = "Integer32"
_WfAcctRuleCreate_Object = MibTableColumn
wfAcctRuleCreate = _WfAcctRuleCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1, 1),
    _WfAcctRuleCreate_Type()
)
wfAcctRuleCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctRuleCreate.setStatus("mandatory")


class _WfAcctRuleNumber_Type(Integer32):
    """Custom type wfAcctRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfAcctRuleNumber_Type.__name__ = "Integer32"
_WfAcctRuleNumber_Object = MibTableColumn
wfAcctRuleNumber = _WfAcctRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1, 2),
    _WfAcctRuleNumber_Type()
)
wfAcctRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctRuleNumber.setStatus("mandatory")
_WfAcctRuleName_Type = DisplayString
_WfAcctRuleName_Object = MibTableColumn
wfAcctRuleName = _WfAcctRuleName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1, 3),
    _WfAcctRuleName_Type()
)
wfAcctRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctRuleName.setStatus("mandatory")


class _WfAcctRuleStatDirection_Type(Integer32):
    """Custom type wfAcctRuleStatDirection based on Integer32"""
    defaultValue = 1

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
        *(("both", 4),
          ("in", 2),
          ("none", 1),
          ("out", 3))
    )


_WfAcctRuleStatDirection_Type.__name__ = "Integer32"
_WfAcctRuleStatDirection_Object = MibTableColumn
wfAcctRuleStatDirection = _WfAcctRuleStatDirection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1, 4),
    _WfAcctRuleStatDirection_Type()
)
wfAcctRuleStatDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctRuleStatDirection.setStatus("mandatory")


class _WfAcctRuleStatCollect_Type(Integer32):
    """Custom type wfAcctRuleStatCollect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("octets", 1),
          ("packets", 2))
    )


_WfAcctRuleStatCollect_Type.__name__ = "Integer32"
_WfAcctRuleStatCollect_Object = MibTableColumn
wfAcctRuleStatCollect = _WfAcctRuleStatCollect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1, 5),
    _WfAcctRuleStatCollect_Type()
)
wfAcctRuleStatCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAcctRuleStatCollect.setStatus("mandatory")
_WfAcctCtrlTable_Object = MibTable
wfAcctCtrlTable = _WfAcctCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3)
)
if mibBuilder.loadTexts:
    wfAcctCtrlTable.setStatus("mandatory")
_WfAcctCtrlEntry_Object = MibTableRow
wfAcctCtrlEntry = _WfAcctCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3, 1)
)
wfAcctCtrlEntry.setIndexNames(
    (0, "Wellfleet-ACCT-MIB", "wfAcctCtrlCctNum"),
    (0, "Wellfleet-ACCT-MIB", "wfAcctCtrlServicePkg"),
    (0, "Wellfleet-ACCT-MIB", "wfAcctCtrlQueueIndex"),
)
if mibBuilder.loadTexts:
    wfAcctCtrlEntry.setStatus("mandatory")
_WfAcctCtrlCctNum_Type = Integer32
_WfAcctCtrlCctNum_Object = MibTableColumn
wfAcctCtrlCctNum = _WfAcctCtrlCctNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3, 1, 1),
    _WfAcctCtrlCctNum_Type()
)
wfAcctCtrlCctNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctCtrlCctNum.setStatus("mandatory")
_WfAcctCtrlServicePkg_Type = Integer32
_WfAcctCtrlServicePkg_Object = MibTableColumn
wfAcctCtrlServicePkg = _WfAcctCtrlServicePkg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3, 1, 2),
    _WfAcctCtrlServicePkg_Type()
)
wfAcctCtrlServicePkg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctCtrlServicePkg.setStatus("mandatory")
_WfAcctCtrlQueueIndex_Type = Integer32
_WfAcctCtrlQueueIndex_Object = MibTableColumn
wfAcctCtrlQueueIndex = _WfAcctCtrlQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3, 1, 3),
    _WfAcctCtrlQueueIndex_Type()
)
wfAcctCtrlQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctCtrlQueueIndex.setStatus("mandatory")


class _WfAcctCtrlRuleNumber_Type(Integer32):
    """Custom type wfAcctCtrlRuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfAcctCtrlRuleNumber_Type.__name__ = "Integer32"
_WfAcctCtrlRuleNumber_Object = MibTableColumn
wfAcctCtrlRuleNumber = _WfAcctCtrlRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3, 1, 4),
    _WfAcctCtrlRuleNumber_Type()
)
wfAcctCtrlRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctCtrlRuleNumber.setStatus("mandatory")
_WfAcctDataTable_Object = MibTable
wfAcctDataTable = _WfAcctDataTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4)
)
if mibBuilder.loadTexts:
    wfAcctDataTable.setStatus("mandatory")
_WfAcctDataEntry_Object = MibTableRow
wfAcctDataEntry = _WfAcctDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1)
)
wfAcctDataEntry.setIndexNames(
    (0, "Wellfleet-ACCT-MIB", "wfAcctDataCctNum"),
    (0, "Wellfleet-ACCT-MIB", "wfAcctDataServicePkg"),
    (0, "Wellfleet-ACCT-MIB", "wfAcctDataQueueIndex"),
    (0, "Wellfleet-ACCT-MIB", "wfAcctDataTimeStampHigh"),
    (0, "Wellfleet-ACCT-MIB", "wfAcctDataTimeStampLow"),
)
if mibBuilder.loadTexts:
    wfAcctDataEntry.setStatus("mandatory")
_WfAcctDataCctNum_Type = Integer32
_WfAcctDataCctNum_Object = MibTableColumn
wfAcctDataCctNum = _WfAcctDataCctNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 1),
    _WfAcctDataCctNum_Type()
)
wfAcctDataCctNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctDataCctNum.setStatus("mandatory")
_WfAcctDataServicePkg_Type = Integer32
_WfAcctDataServicePkg_Object = MibTableColumn
wfAcctDataServicePkg = _WfAcctDataServicePkg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 2),
    _WfAcctDataServicePkg_Type()
)
wfAcctDataServicePkg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctDataServicePkg.setStatus("mandatory")
_WfAcctDataQueueIndex_Type = Integer32
_WfAcctDataQueueIndex_Object = MibTableColumn
wfAcctDataQueueIndex = _WfAcctDataQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 3),
    _WfAcctDataQueueIndex_Type()
)
wfAcctDataQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctDataQueueIndex.setStatus("mandatory")
_WfAcctDataTimeStampHigh_Type = RtrTimeStamp
_WfAcctDataTimeStampHigh_Object = MibTableColumn
wfAcctDataTimeStampHigh = _WfAcctDataTimeStampHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 4),
    _WfAcctDataTimeStampHigh_Type()
)
wfAcctDataTimeStampHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctDataTimeStampHigh.setStatus("mandatory")
_WfAcctDataTimeStampLow_Type = RtrTimeStamp
_WfAcctDataTimeStampLow_Object = MibTableColumn
wfAcctDataTimeStampLow = _WfAcctDataTimeStampLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 5),
    _WfAcctDataTimeStampLow_Type()
)
wfAcctDataTimeStampLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctDataTimeStampLow.setStatus("mandatory")
_WfAcctDataBitmask_Type = Gauge32
_WfAcctDataBitmask_Object = MibTableColumn
wfAcctDataBitmask = _WfAcctDataBitmask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 6),
    _WfAcctDataBitmask_Type()
)
wfAcctDataBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctDataBitmask.setStatus("mandatory")
_WfAcctInBelowCirOctets_Type = Counter32
_WfAcctInBelowCirOctets_Object = MibTableColumn
wfAcctInBelowCirOctets = _WfAcctInBelowCirOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 7),
    _WfAcctInBelowCirOctets_Type()
)
wfAcctInBelowCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctInBelowCirOctets.setStatus("mandatory")
_WfAcctInAboveCirOctets_Type = Counter32
_WfAcctInAboveCirOctets_Object = MibTableColumn
wfAcctInAboveCirOctets = _WfAcctInAboveCirOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 8),
    _WfAcctInAboveCirOctets_Type()
)
wfAcctInAboveCirOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctInAboveCirOctets.setStatus("mandatory")
_WfAcctInAboveBrOctets_Type = Counter32
_WfAcctInAboveBrOctets_Object = MibTableColumn
wfAcctInAboveBrOctets = _WfAcctInAboveBrOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 9),
    _WfAcctInAboveBrOctets_Type()
)
wfAcctInAboveBrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctInAboveBrOctets.setStatus("mandatory")
_WfAcctInBelowCirPkts_Type = Counter32
_WfAcctInBelowCirPkts_Object = MibTableColumn
wfAcctInBelowCirPkts = _WfAcctInBelowCirPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 10),
    _WfAcctInBelowCirPkts_Type()
)
wfAcctInBelowCirPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctInBelowCirPkts.setStatus("mandatory")
_WfAcctInAboveCirPkts_Type = Counter32
_WfAcctInAboveCirPkts_Object = MibTableColumn
wfAcctInAboveCirPkts = _WfAcctInAboveCirPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 11),
    _WfAcctInAboveCirPkts_Type()
)
wfAcctInAboveCirPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctInAboveCirPkts.setStatus("mandatory")
_WfAcctInAboveBrPkts_Type = Counter32
_WfAcctInAboveBrPkts_Object = MibTableColumn
wfAcctInAboveBrPkts = _WfAcctInAboveBrPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 12),
    _WfAcctInAboveBrPkts_Type()
)
wfAcctInAboveBrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctInAboveBrPkts.setStatus("mandatory")
_WfAcctOutOctets_Type = Counter32
_WfAcctOutOctets_Object = MibTableColumn
wfAcctOutOctets = _WfAcctOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 13),
    _WfAcctOutOctets_Type()
)
wfAcctOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctOutOctets.setStatus("mandatory")
_WfAcctOutPkts_Type = Counter32
_WfAcctOutPkts_Object = MibTableColumn
wfAcctOutPkts = _WfAcctOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 14),
    _WfAcctOutPkts_Type()
)
wfAcctOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAcctOutPkts.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wfAcctBufferFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 0, 1)
)
if mibBuilder.loadTexts:
    wfAcctBufferFull.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-ACCT-MIB",
    **{"RtrTimeStamp": RtrTimeStamp,
       "wfAcctBufferFull": wfAcctBufferFull,
       "wfAcct": wfAcct,
       "wfAcctCreate": wfAcctCreate,
       "wfAcctEnable": wfAcctEnable,
       "wfAcctOperState": wfAcctOperState,
       "wfAcctLogLevel": wfAcctLogLevel,
       "wfAcctCircularSnapshotFlag": wfAcctCircularSnapshotFlag,
       "wfAcctCollectDuration": wfAcctCollectDuration,
       "wfAcctUpdateInterval": wfAcctUpdateInterval,
       "wfAcctFlushOnRetrieval": wfAcctFlushOnRetrieval,
       "wfAcctFlushData": wfAcctFlushData,
       "wfAcctLastUpdateTimeStampHigh": wfAcctLastUpdateTimeStampHigh,
       "wfAcctLastUpdateTimeStampLow": wfAcctLastUpdateTimeStampLow,
       "wfAcctLastFlushTimeStampHigh": wfAcctLastFlushTimeStampHigh,
       "wfAcctLastFlushTimeStampLow": wfAcctLastFlushTimeStampLow,
       "wfAcctRuleNumEntries": wfAcctRuleNumEntries,
       "wfAcctCtrlNumEntries": wfAcctCtrlNumEntries,
       "wfAcctDataNumEntries": wfAcctDataNumEntries,
       "wfAcctRuleTable": wfAcctRuleTable,
       "wfAcctRuleEntry": wfAcctRuleEntry,
       "wfAcctRuleCreate": wfAcctRuleCreate,
       "wfAcctRuleNumber": wfAcctRuleNumber,
       "wfAcctRuleName": wfAcctRuleName,
       "wfAcctRuleStatDirection": wfAcctRuleStatDirection,
       "wfAcctRuleStatCollect": wfAcctRuleStatCollect,
       "wfAcctCtrlTable": wfAcctCtrlTable,
       "wfAcctCtrlEntry": wfAcctCtrlEntry,
       "wfAcctCtrlCctNum": wfAcctCtrlCctNum,
       "wfAcctCtrlServicePkg": wfAcctCtrlServicePkg,
       "wfAcctCtrlQueueIndex": wfAcctCtrlQueueIndex,
       "wfAcctCtrlRuleNumber": wfAcctCtrlRuleNumber,
       "wfAcctDataTable": wfAcctDataTable,
       "wfAcctDataEntry": wfAcctDataEntry,
       "wfAcctDataCctNum": wfAcctDataCctNum,
       "wfAcctDataServicePkg": wfAcctDataServicePkg,
       "wfAcctDataQueueIndex": wfAcctDataQueueIndex,
       "wfAcctDataTimeStampHigh": wfAcctDataTimeStampHigh,
       "wfAcctDataTimeStampLow": wfAcctDataTimeStampLow,
       "wfAcctDataBitmask": wfAcctDataBitmask,
       "wfAcctInBelowCirOctets": wfAcctInBelowCirOctets,
       "wfAcctInAboveCirOctets": wfAcctInAboveCirOctets,
       "wfAcctInAboveBrOctets": wfAcctInAboveBrOctets,
       "wfAcctInBelowCirPkts": wfAcctInBelowCirPkts,
       "wfAcctInAboveCirPkts": wfAcctInAboveCirPkts,
       "wfAcctInAboveBrPkts": wfAcctInAboveBrPkts,
       "wfAcctOutOctets": wfAcctOutOctets,
       "wfAcctOutPkts": wfAcctOutPkts}
)
