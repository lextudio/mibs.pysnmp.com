# SNMP MIB module (HUAWEI-CLOCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-CLOCK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:22 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

hwClockMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186)
)
hwClockMIB.setRevisions(
        ("2014-11-29 00:00",
         "2014-11-03 00:00",
         "2014-08-13 00:00",
         "2014-04-21 00:00",
         "2014-01-07 00:00",
         "2013-11-12 00:00",
         "2013-10-31 00:00",
         "2013-05-23 00:00",
         "2013-05-14 00:00",
         "2013-03-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwClockManageObjects_ObjectIdentity = ObjectIdentity
hwClockManageObjects = _HwClockManageObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1)
)
_HwClockGlobalObjects_ObjectIdentity = ObjectIdentity
hwClockGlobalObjects = _HwClockGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1)
)
_HwClockSourceEthClkEnable_Type = EnabledStatus
_HwClockSourceEthClkEnable_Object = MibScalar
hwClockSourceEthClkEnable = _HwClockSourceEthClkEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 1),
    _HwClockSourceEthClkEnable_Type()
)
hwClockSourceEthClkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSourceEthClkEnable.setStatus("current")


class _HwClockSourceSsmUnknown_Type(Integer32):
    """Custom type hwClockSourceSsmUnknown based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 15),
          ("prc", 2),
          ("sec", 11),
          ("ssua", 4),
          ("ssub", 8))
    )


_HwClockSourceSsmUnknown_Type.__name__ = "Integer32"
_HwClockSourceSsmUnknown_Object = MibScalar
hwClockSourceSsmUnknown = _HwClockSourceSsmUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 2),
    _HwClockSourceSsmUnknown_Type()
)
hwClockSourceSsmUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSourceSsmUnknown.setStatus("current")


class _HwClockSourceSysClkWorkMode_Type(Integer32):
    """Custom type hwClockSourceSysClkWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freeoscillate", 3),
          ("hold", 2),
          ("trace", 1))
    )


_HwClockSourceSysClkWorkMode_Type.__name__ = "Integer32"
_HwClockSourceSysClkWorkMode_Object = MibScalar
hwClockSourceSysClkWorkMode = _HwClockSourceSysClkWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 3),
    _HwClockSourceSysClkWorkMode_Type()
)
hwClockSourceSysClkWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSourceSysClkWorkMode.setStatus("current")
_HwClockSourceForceCloseEnableStatus_Type = EnabledStatus
_HwClockSourceForceCloseEnableStatus_Object = MibScalar
hwClockSourceForceCloseEnableStatus = _HwClockSourceForceCloseEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 4),
    _HwClockSourceForceCloseEnableStatus_Type()
)
hwClockSourceForceCloseEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSourceForceCloseEnableStatus.setStatus("current")


class _HwClockSourceSsmControl_Type(Integer32):
    """Custom type hwClockSourceSsmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("extend", 3),
          ("off", 2),
          ("on", 1))
    )


_HwClockSourceSsmControl_Type.__name__ = "Integer32"
_HwClockSourceSsmControl_Object = MibScalar
hwClockSourceSsmControl = _HwClockSourceSsmControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 5),
    _HwClockSourceSsmControl_Type()
)
hwClockSourceSsmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSourceSsmControl.setStatus("current")


class _HwClockSourceHoldMode_Type(Integer32):
    """Custom type hwClockSourceHoldMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hold24Hours", 1),
          ("holdForever", 2))
    )


_HwClockSourceHoldMode_Type.__name__ = "Integer32"
_HwClockSourceHoldMode_Object = MibScalar
hwClockSourceHoldMode = _HwClockSourceHoldMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 6),
    _HwClockSourceHoldMode_Type()
)
hwClockSourceHoldMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSourceHoldMode.setStatus("current")
_HwClockSourceFreqCheckEnable_Type = EnabledStatus
_HwClockSourceFreqCheckEnable_Object = MibScalar
hwClockSourceFreqCheckEnable = _HwClockSourceFreqCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 7),
    _HwClockSourceFreqCheckEnable_Type()
)
hwClockSourceFreqCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSourceFreqCheckEnable.setStatus("current")


class _HwClockSourceFreqCheckLeftRange_Type(Integer32):
    """Custom type hwClockSourceFreqCheckLeftRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000),
    )


_HwClockSourceFreqCheckLeftRange_Type.__name__ = "Integer32"
_HwClockSourceFreqCheckLeftRange_Object = MibScalar
hwClockSourceFreqCheckLeftRange = _HwClockSourceFreqCheckLeftRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 8),
    _HwClockSourceFreqCheckLeftRange_Type()
)
hwClockSourceFreqCheckLeftRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSourceFreqCheckLeftRange.setStatus("current")


class _HwClockSourceFreqCheckRightRange_Type(Integer32):
    """Custom type hwClockSourceFreqCheckRightRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000),
    )


_HwClockSourceFreqCheckRightRange_Type.__name__ = "Integer32"
_HwClockSourceFreqCheckRightRange_Object = MibScalar
hwClockSourceFreqCheckRightRange = _HwClockSourceFreqCheckRightRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 9),
    _HwClockSourceFreqCheckRightRange_Type()
)
hwClockSourceFreqCheckRightRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSourceFreqCheckRightRange.setStatus("current")


class _HwClockSourceRetrieveMode_Type(Integer32):
    """Custom type hwClockSourceRetrieveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRetrieve", 2),
          ("retrieve", 1))
    )


_HwClockSourceRetrieveMode_Type.__name__ = "Integer32"
_HwClockSourceRetrieveMode_Object = MibScalar
hwClockSourceRetrieveMode = _HwClockSourceRetrieveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 10),
    _HwClockSourceRetrieveMode_Type()
)
hwClockSourceRetrieveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSourceRetrieveMode.setStatus("current")


class _HwClockTimeUsedSource_Type(Integer32):
    """Custom type hwClockTimeUsedSource based on Integer32"""
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
        *(("src1ppsTodBit0", 3),
          ("src1ppsTodBit1", 4),
          ("srcDclsTimeBit0", 1),
          ("srcDclsTimeBit1", 2),
          ("srcFreeRun", 6),
          ("srcPtp", 5))
    )


_HwClockTimeUsedSource_Type.__name__ = "Integer32"
_HwClockTimeUsedSource_Object = MibScalar
hwClockTimeUsedSource = _HwClockTimeUsedSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 11),
    _HwClockTimeUsedSource_Type()
)
hwClockTimeUsedSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockTimeUsedSource.setStatus("current")


class _HwClockExtTimeInputType_Type(Integer32):
    """Custom type hwClockExtTimeInputType based on Integer32"""
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
        *(("type1ppsTodGps", 3),
          ("type1ppsTodRs232", 2),
          ("typeDclsTime", 1),
          ("typeNone", 4))
    )


_HwClockExtTimeInputType_Type.__name__ = "Integer32"
_HwClockExtTimeInputType_Object = MibScalar
hwClockExtTimeInputType = _HwClockExtTimeInputType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 12),
    _HwClockExtTimeInputType_Type()
)
hwClockExtTimeInputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockExtTimeInputType.setStatus("current")


class _HwClockExtTimeOutputType_Type(Integer32):
    """Custom type hwClockExtTimeOutputType based on Integer32"""
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
        *(("type1ppsTodGps", 3),
          ("type1ppsTodRs232", 2),
          ("typeDclsTime", 1),
          ("typeNone", 4))
    )


_HwClockExtTimeOutputType_Type.__name__ = "Integer32"
_HwClockExtTimeOutputType_Object = MibScalar
hwClockExtTimeOutputType = _HwClockExtTimeOutputType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 13),
    _HwClockExtTimeOutputType_Type()
)
hwClockExtTimeOutputType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockExtTimeOutputType.setStatus("current")


class _HwClockAlarmThresholdFrequencyOffset_Type(Integer32):
    """Custom type hwClockAlarmThresholdFrequencyOffset based on Integer32"""
    defaultValue = 92

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 92),
    )


_HwClockAlarmThresholdFrequencyOffset_Type.__name__ = "Integer32"
_HwClockAlarmThresholdFrequencyOffset_Object = MibScalar
hwClockAlarmThresholdFrequencyOffset = _HwClockAlarmThresholdFrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 14),
    _HwClockAlarmThresholdFrequencyOffset_Type()
)
hwClockAlarmThresholdFrequencyOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAlarmThresholdFrequencyOffset.setStatus("current")
if mibBuilder.loadTexts:
    hwClockAlarmThresholdFrequencyOffset.setUnits("100ppb")
_HwClockFrequencyOffsetMax_Type = Integer32
_HwClockFrequencyOffsetMax_Object = MibScalar
hwClockFrequencyOffsetMax = _HwClockFrequencyOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 15),
    _HwClockFrequencyOffsetMax_Type()
)
hwClockFrequencyOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockFrequencyOffsetMax.setStatus("current")
if mibBuilder.loadTexts:
    hwClockFrequencyOffsetMax.setUnits("ppb")
_HwClockFrequencyOffsetMin_Type = Integer32
_HwClockFrequencyOffsetMin_Object = MibScalar
hwClockFrequencyOffsetMin = _HwClockFrequencyOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 16),
    _HwClockFrequencyOffsetMin_Type()
)
hwClockFrequencyOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockFrequencyOffsetMin.setStatus("current")
if mibBuilder.loadTexts:
    hwClockFrequencyOffsetMin.setUnits("ppb")
_HwClockFrequencyOffsetMean_Type = Integer32
_HwClockFrequencyOffsetMean_Object = MibScalar
hwClockFrequencyOffsetMean = _HwClockFrequencyOffsetMean_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 17),
    _HwClockFrequencyOffsetMean_Type()
)
hwClockFrequencyOffsetMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockFrequencyOffsetMean.setStatus("current")
if mibBuilder.loadTexts:
    hwClockFrequencyOffsetMean.setUnits("ppb")
_HwClockFrequencyOffset_Type = Integer32
_HwClockFrequencyOffset_Object = MibScalar
hwClockFrequencyOffset = _HwClockFrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 1, 18),
    _HwClockFrequencyOffset_Type()
)
hwClockFrequencyOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockFrequencyOffset.setStatus("current")
if mibBuilder.loadTexts:
    hwClockFrequencyOffset.setUnits("ppb")
_HwClockSourceSelTable_Object = MibTable
hwClockSourceSelTable = _HwClockSourceSelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 2)
)
if mibBuilder.loadTexts:
    hwClockSourceSelTable.setStatus("current")
_HwClockSourceSelEntry_Object = MibTableRow
hwClockSourceSelEntry = _HwClockSourceSelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 2, 1)
)
hwClockSourceSelEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockSourceSelChassisIndex"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockSourceSelType"),
)
if mibBuilder.loadTexts:
    hwClockSourceSelEntry.setStatus("current")
_HwClockSourceSelChassisIndex_Type = PhysicalIndex
_HwClockSourceSelChassisIndex_Object = MibTableColumn
hwClockSourceSelChassisIndex = _HwClockSourceSelChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 2, 1, 1),
    _HwClockSourceSelChassisIndex_Type()
)
hwClockSourceSelChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockSourceSelChassisIndex.setStatus("current")


class _HwClockSourceSelType_Type(Integer32):
    """Custom type hwClockSourceSelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwClockSourceSelType_Type.__name__ = "Integer32"
_HwClockSourceSelType_Object = MibTableColumn
hwClockSourceSelType = _HwClockSourceSelType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 2, 1, 2),
    _HwClockSourceSelType_Type()
)
hwClockSourceSelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockSourceSelType.setStatus("current")


class _HwClockSourceSelMode_Type(Integer32):
    """Custom type hwClockSourceSelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("force", 3),
          ("manual", 2))
    )


_HwClockSourceSelMode_Type.__name__ = "Integer32"
_HwClockSourceSelMode_Object = MibTableColumn
hwClockSourceSelMode = _HwClockSourceSelMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 2, 1, 3),
    _HwClockSourceSelMode_Type()
)
hwClockSourceSelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockSourceSelMode.setStatus("current")
_HwClockSourceSelSourceId_Type = Integer32
_HwClockSourceSelSourceId_Object = MibTableColumn
hwClockSourceSelSourceId = _HwClockSourceSelSourceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 2, 1, 4),
    _HwClockSourceSelSourceId_Type()
)
hwClockSourceSelSourceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockSourceSelSourceId.setStatus("current")
_HwClockSourceCfgTable_Object = MibTable
hwClockSourceCfgTable = _HwClockSourceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3)
)
if mibBuilder.loadTexts:
    hwClockSourceCfgTable.setStatus("current")
_HwClockSourceCfgEntry_Object = MibTableRow
hwClockSourceCfgEntry = _HwClockSourceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1)
)
hwClockSourceCfgEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockCfgChassisIndex"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockCfgSourceIndex"),
)
if mibBuilder.loadTexts:
    hwClockSourceCfgEntry.setStatus("current")
_HwClockCfgChassisIndex_Type = PhysicalIndex
_HwClockCfgChassisIndex_Object = MibTableColumn
hwClockCfgChassisIndex = _HwClockCfgChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 1),
    _HwClockCfgChassisIndex_Type()
)
hwClockCfgChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockCfgChassisIndex.setStatus("current")


class _HwClockCfgSourceIndex_Type(Integer32):
    """Custom type hwClockCfgSourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HwClockCfgSourceIndex_Type.__name__ = "Integer32"
_HwClockCfgSourceIndex_Object = MibTableColumn
hwClockCfgSourceIndex = _HwClockCfgSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 2),
    _HwClockCfgSourceIndex_Type()
)
hwClockCfgSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockCfgSourceIndex.setStatus("current")
_HwClockCfgSourceId_Type = Integer32
_HwClockCfgSourceId_Object = MibTableColumn
hwClockCfgSourceId = _HwClockCfgSourceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 3),
    _HwClockCfgSourceId_Type()
)
hwClockCfgSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockCfgSourceId.setStatus("current")
_HwClockCfgSourceDescr_Type = OctetString
_HwClockCfgSourceDescr_Object = MibTableColumn
hwClockCfgSourceDescr = _HwClockCfgSourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 4),
    _HwClockCfgSourceDescr_Type()
)
hwClockCfgSourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockCfgSourceDescr.setStatus("current")


class _HwClockCfgWtrTime_Type(Integer32):
    """Custom type hwClockCfgWtrTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_HwClockCfgWtrTime_Type.__name__ = "Integer32"
_HwClockCfgWtrTime_Object = MibTableColumn
hwClockCfgWtrTime = _HwClockCfgWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 5),
    _HwClockCfgWtrTime_Type()
)
hwClockCfgWtrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgWtrTime.setStatus("current")
_HwClockCfgBadDetect_Type = EnabledStatus
_HwClockCfgBadDetect_Object = MibTableColumn
hwClockCfgBadDetect = _HwClockCfgBadDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 6),
    _HwClockCfgBadDetect_Type()
)
hwClockCfgBadDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgBadDetect.setStatus("current")


class _HwClockCfgSystemPriority_Type(Integer32):
    """Custom type hwClockCfgSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_HwClockCfgSystemPriority_Type.__name__ = "Integer32"
_HwClockCfgSystemPriority_Object = MibTableColumn
hwClockCfgSystemPriority = _HwClockCfgSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 7),
    _HwClockCfgSystemPriority_Type()
)
hwClockCfgSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgSystemPriority.setStatus("current")


class _HwClockCfgBits0Priority_Type(Integer32):
    """Custom type hwClockCfgBits0Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_HwClockCfgBits0Priority_Type.__name__ = "Integer32"
_HwClockCfgBits0Priority_Object = MibTableColumn
hwClockCfgBits0Priority = _HwClockCfgBits0Priority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 8),
    _HwClockCfgBits0Priority_Type()
)
hwClockCfgBits0Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgBits0Priority.setStatus("current")


class _HwClockCfgBits1Priority_Type(Integer32):
    """Custom type hwClockCfgBits1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_HwClockCfgBits1Priority_Type.__name__ = "Integer32"
_HwClockCfgBits1Priority_Object = MibTableColumn
hwClockCfgBits1Priority = _HwClockCfgBits1Priority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 9),
    _HwClockCfgBits1Priority_Type()
)
hwClockCfgBits1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgBits1Priority.setStatus("current")
_HwClockCfgSystemLockOut_Type = Integer32
_HwClockCfgSystemLockOut_Object = MibTableColumn
hwClockCfgSystemLockOut = _HwClockCfgSystemLockOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 10),
    _HwClockCfgSystemLockOut_Type()
)
hwClockCfgSystemLockOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgSystemLockOut.setStatus("current")
_HwClockCfgBits0LockOut_Type = Integer32
_HwClockCfgBits0LockOut_Object = MibTableColumn
hwClockCfgBits0LockOut = _HwClockCfgBits0LockOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 11),
    _HwClockCfgBits0LockOut_Type()
)
hwClockCfgBits0LockOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgBits0LockOut.setStatus("current")
_HwClockCfgBits1LockOut_Type = Integer32
_HwClockCfgBits1LockOut_Object = MibTableColumn
hwClockCfgBits1LockOut = _HwClockCfgBits1LockOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 12),
    _HwClockCfgBits1LockOut_Type()
)
hwClockCfgBits1LockOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgBits1LockOut.setStatus("current")


class _HwClockCfgSourceSsm_Type(Integer32):
    """Custom type hwClockCfgSourceSsm based on Integer32"""
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
        *(("ssmDnu", 5),
          ("ssmPrc", 1),
          ("ssmSec", 4),
          ("ssmSsul", 3),
          ("ssmSsut", 2),
          ("ssmUnknown", 6))
    )


_HwClockCfgSourceSsm_Type.__name__ = "Integer32"
_HwClockCfgSourceSsm_Object = MibTableColumn
hwClockCfgSourceSsm = _HwClockCfgSourceSsm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 13),
    _HwClockCfgSourceSsm_Type()
)
hwClockCfgSourceSsm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgSourceSsm.setStatus("current")


class _HwClockCfgSourceSsmSetMode_Type(Integer32):
    """Custom type hwClockCfgSourceSsmSetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 1))
    )


_HwClockCfgSourceSsmSetMode_Type.__name__ = "Integer32"
_HwClockCfgSourceSsmSetMode_Object = MibTableColumn
hwClockCfgSourceSsmSetMode = _HwClockCfgSourceSsmSetMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 14),
    _HwClockCfgSourceSsmSetMode_Type()
)
hwClockCfgSourceSsmSetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgSourceSsmSetMode.setStatus("current")
_HwClockCfgExportEnableStatus_Type = EnabledStatus
_HwClockCfgExportEnableStatus_Object = MibTableColumn
hwClockCfgExportEnableStatus = _HwClockCfgExportEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 15),
    _HwClockCfgExportEnableStatus_Type()
)
hwClockCfgExportEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgExportEnableStatus.setStatus("current")
_HwClockCfgSwiEnableStatus_Type = EnabledStatus
_HwClockCfgSwiEnableStatus_Object = MibTableColumn
hwClockCfgSwiEnableStatus = _HwClockCfgSwiEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 16),
    _HwClockCfgSwiEnableStatus_Type()
)
hwClockCfgSwiEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgSwiEnableStatus.setStatus("current")


class _HwClockCfgSourceState_Type(Integer32):
    """Custom type hwClockCfgSourceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_HwClockCfgSourceState_Type.__name__ = "Integer32"
_HwClockCfgSourceState_Object = MibTableColumn
hwClockCfgSourceState = _HwClockCfgSourceState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 17),
    _HwClockCfgSourceState_Type()
)
hwClockCfgSourceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgSourceState.setStatus("current")


class _HwClockCfgSsmThreshold_Type(Integer32):
    """Custom type hwClockCfgSsmThreshold based on Integer32"""
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
        *(("qlDnu", 1),
          ("qlPrc", 5),
          ("qlSec", 2),
          ("qlSsua", 4),
          ("qlSsub", 3))
    )


_HwClockCfgSsmThreshold_Type.__name__ = "Integer32"
_HwClockCfgSsmThreshold_Object = MibTableColumn
hwClockCfgSsmThreshold = _HwClockCfgSsmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 18),
    _HwClockCfgSsmThreshold_Type()
)
hwClockCfgSsmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgSsmThreshold.setStatus("current")


class _HwClockCfgSourceS1Id_Type(Integer32):
    """Custom type hwClockCfgSourceS1Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwClockCfgSourceS1Id_Type.__name__ = "Integer32"
_HwClockCfgSourceS1Id_Object = MibTableColumn
hwClockCfgSourceS1Id = _HwClockCfgSourceS1Id_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 19),
    _HwClockCfgSourceS1Id_Type()
)
hwClockCfgSourceS1Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockCfgSourceS1Id.setStatus("current")
_HwClockCfgFreqCheckResult_Type = Integer32
_HwClockCfgFreqCheckResult_Object = MibTableColumn
hwClockCfgFreqCheckResult = _HwClockCfgFreqCheckResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 20),
    _HwClockCfgFreqCheckResult_Type()
)
hwClockCfgFreqCheckResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgFreqCheckResult.setStatus("current")


class _HwClockCfgHoldOffTime_Type(Integer32):
    """Custom type hwClockCfgHoldOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 18),
    )


_HwClockCfgHoldOffTime_Type.__name__ = "Integer32"
_HwClockCfgHoldOffTime_Object = MibTableColumn
hwClockCfgHoldOffTime = _HwClockCfgHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 21),
    _HwClockCfgHoldOffTime_Type()
)
hwClockCfgHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgHoldOffTime.setStatus("current")
_HwClockCfgPriRvtEnableStatus_Type = EnabledStatus
_HwClockCfgPriRvtEnableStatus_Object = MibTableColumn
hwClockCfgPriRvtEnableStatus = _HwClockCfgPriRvtEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 22),
    _HwClockCfgPriRvtEnableStatus_Type()
)
hwClockCfgPriRvtEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgPriRvtEnableStatus.setStatus("current")


class _HwClockCfgSwitchCondition_Type(Integer32):
    """Custom type hwClockCfgSwitchCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSwitch", 1),
          ("switch", 2))
    )


_HwClockCfgSwitchCondition_Type.__name__ = "Integer32"
_HwClockCfgSwitchCondition_Object = MibTableColumn
hwClockCfgSwitchCondition = _HwClockCfgSwitchCondition_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 23),
    _HwClockCfgSwitchCondition_Type()
)
hwClockCfgSwitchCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockCfgSwitchCondition.setStatus("current")


class _HwClockCfgClkSourceType_Type(Integer32):
    """Custom type hwClockCfgClkSourceType based on Integer32"""
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
        *(("bits", 1),
          ("inner", 3),
          ("line", 2),
          ("system", 4))
    )


_HwClockCfgClkSourceType_Type.__name__ = "Integer32"
_HwClockCfgClkSourceType_Object = MibTableColumn
hwClockCfgClkSourceType = _HwClockCfgClkSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 3, 1, 24),
    _HwClockCfgClkSourceType_Type()
)
hwClockCfgClkSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockCfgClkSourceType.setStatus("current")
_HwClockBitsCfgTable_Object = MibTable
hwClockBitsCfgTable = _HwClockBitsCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4)
)
if mibBuilder.loadTexts:
    hwClockBitsCfgTable.setStatus("current")
_HwClockBitsCfgEntry_Object = MibTableRow
hwClockBitsCfgEntry = _HwClockBitsCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1)
)
hwClockBitsCfgEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockBitsCfgChassisIndex"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockBitsCfgBitsIndex"),
)
if mibBuilder.loadTexts:
    hwClockBitsCfgEntry.setStatus("current")
_HwClockBitsCfgChassisIndex_Type = PhysicalIndex
_HwClockBitsCfgChassisIndex_Object = MibTableColumn
hwClockBitsCfgChassisIndex = _HwClockBitsCfgChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 1),
    _HwClockBitsCfgChassisIndex_Type()
)
hwClockBitsCfgChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockBitsCfgChassisIndex.setStatus("current")


class _HwClockBitsCfgBitsIndex_Type(Integer32):
    """Custom type hwClockBitsCfgBitsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwClockBitsCfgBitsIndex_Type.__name__ = "Integer32"
_HwClockBitsCfgBitsIndex_Object = MibTableColumn
hwClockBitsCfgBitsIndex = _HwClockBitsCfgBitsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 2),
    _HwClockBitsCfgBitsIndex_Type()
)
hwClockBitsCfgBitsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockBitsCfgBitsIndex.setStatus("current")
_HwClockBitsCfgName_Type = OctetString
_HwClockBitsCfgName_Object = MibTableColumn
hwClockBitsCfgName = _HwClockBitsCfgName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 3),
    _HwClockBitsCfgName_Type()
)
hwClockBitsCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockBitsCfgName.setStatus("current")


class _HwClockBitsCfgBitsPortType_Type(Integer32):
    """Custom type hwClockBitsCfgBitsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portRj45", 1),
          ("portSMB", 2))
    )


_HwClockBitsCfgBitsPortType_Type.__name__ = "Integer32"
_HwClockBitsCfgBitsPortType_Object = MibTableColumn
hwClockBitsCfgBitsPortType = _HwClockBitsCfgBitsPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 4),
    _HwClockBitsCfgBitsPortType_Type()
)
hwClockBitsCfgBitsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockBitsCfgBitsPortType.setStatus("current")


class _HwClockBitsCfgBitsType_Type(Integer32):
    """Custom type hwClockBitsCfgBitsType based on Integer32"""
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
        *(("none", 4),
          ("type1544Mbps", 5),
          ("type1ppsTod", 3),
          ("type2Mbps", 0),
          ("type2Mhz", 1),
          ("typeDclsTime", 2))
    )


_HwClockBitsCfgBitsType_Type.__name__ = "Integer32"
_HwClockBitsCfgBitsType_Object = MibTableColumn
hwClockBitsCfgBitsType = _HwClockBitsCfgBitsType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 5),
    _HwClockBitsCfgBitsType_Type()
)
hwClockBitsCfgBitsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockBitsCfgBitsType.setStatus("current")


class _HwClockBitsCfgDirection_Type(Integer32):
    """Custom type hwClockBitsCfgDirection based on Integer32"""
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
        *(("in", 1),
          ("inAndOut", 3),
          ("none", 4),
          ("out", 2))
    )


_HwClockBitsCfgDirection_Type.__name__ = "Integer32"
_HwClockBitsCfgDirection_Object = MibTableColumn
hwClockBitsCfgDirection = _HwClockBitsCfgDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 6),
    _HwClockBitsCfgDirection_Type()
)
hwClockBitsCfgDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockBitsCfgDirection.setStatus("current")


class _HwClockBitsCfgRecvSaBit_Type(Integer32):
    """Custom type hwClockBitsCfgRecvSaBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("sa4", 4),
          ("sa5", 5),
          ("sa6", 6),
          ("sa7", 7),
          ("sa8", 8))
    )


_HwClockBitsCfgRecvSaBit_Type.__name__ = "Integer32"
_HwClockBitsCfgRecvSaBit_Object = MibTableColumn
hwClockBitsCfgRecvSaBit = _HwClockBitsCfgRecvSaBit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 7),
    _HwClockBitsCfgRecvSaBit_Type()
)
hwClockBitsCfgRecvSaBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockBitsCfgRecvSaBit.setStatus("current")


class _HwClockBitsCfgSendSaBit_Type(Integer32):
    """Custom type hwClockBitsCfgSendSaBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("sa4", 4),
          ("sa5", 5),
          ("sa6", 6),
          ("sa7", 7),
          ("sa8", 8))
    )


_HwClockBitsCfgSendSaBit_Type.__name__ = "Integer32"
_HwClockBitsCfgSendSaBit_Object = MibTableColumn
hwClockBitsCfgSendSaBit = _HwClockBitsCfgSendSaBit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 8),
    _HwClockBitsCfgSendSaBit_Type()
)
hwClockBitsCfgSendSaBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockBitsCfgSendSaBit.setStatus("current")


class _HwClockBitsCfgForceOutS1_Type(Integer32):
    """Custom type hwClockBitsCfgForceOutS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 15),
          ("prc", 2),
          ("sec", 11),
          ("ssua", 4),
          ("ssub", 8),
          ("unk", 0))
    )


_HwClockBitsCfgForceOutS1_Type.__name__ = "Integer32"
_HwClockBitsCfgForceOutS1_Object = MibTableColumn
hwClockBitsCfgForceOutS1 = _HwClockBitsCfgForceOutS1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 9),
    _HwClockBitsCfgForceOutS1_Type()
)
hwClockBitsCfgForceOutS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockBitsCfgForceOutS1.setStatus("current")


class _HwClockBitsCfgSaBit_Type(Integer32):
    """Custom type hwClockBitsCfgSaBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("sa4", 4),
          ("sa5", 5),
          ("sa6", 6),
          ("sa7", 7),
          ("sa8", 8))
    )


_HwClockBitsCfgSaBit_Type.__name__ = "Integer32"
_HwClockBitsCfgSaBit_Object = MibTableColumn
hwClockBitsCfgSaBit = _HwClockBitsCfgSaBit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 10),
    _HwClockBitsCfgSaBit_Type()
)
hwClockBitsCfgSaBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockBitsCfgSaBit.setStatus("current")


class _HwClockBitsCfgInputMode_Type(Integer32):
    """Custom type hwClockBitsCfgInputMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clk2MBits", 0),
          ("clk2MHz", 1),
          ("dclsTime", 2))
    )


_HwClockBitsCfgInputMode_Type.__name__ = "Integer32"
_HwClockBitsCfgInputMode_Object = MibTableColumn
hwClockBitsCfgInputMode = _HwClockBitsCfgInputMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 11),
    _HwClockBitsCfgInputMode_Type()
)
hwClockBitsCfgInputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockBitsCfgInputMode.setStatus("current")


class _HwClockBitsCfgOutputMode_Type(Integer32):
    """Custom type hwClockBitsCfgOutputMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clk2MBits", 0),
          ("clk2MHz", 1),
          ("dclsTime", 2))
    )


_HwClockBitsCfgOutputMode_Type.__name__ = "Integer32"
_HwClockBitsCfgOutputMode_Object = MibTableColumn
hwClockBitsCfgOutputMode = _HwClockBitsCfgOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 12),
    _HwClockBitsCfgOutputMode_Type()
)
hwClockBitsCfgOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockBitsCfgOutputMode.setStatus("current")


class _HwClockBitsCfgInvalidCond_Type(Integer32):
    """Custom type hwClockBitsCfgInvalidCond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ais", 2),
          ("lof", 3),
          ("no", 1))
    )


_HwClockBitsCfgInvalidCond_Type.__name__ = "Integer32"
_HwClockBitsCfgInvalidCond_Object = MibTableColumn
hwClockBitsCfgInvalidCond = _HwClockBitsCfgInvalidCond_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 13),
    _HwClockBitsCfgInvalidCond_Type()
)
hwClockBitsCfgInvalidCond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockBitsCfgInvalidCond.setStatus("current")
_HwClockBitsCfgSourceId_Type = Integer32
_HwClockBitsCfgSourceId_Object = MibTableColumn
hwClockBitsCfgSourceId = _HwClockBitsCfgSourceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 14),
    _HwClockBitsCfgSourceId_Type()
)
hwClockBitsCfgSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockBitsCfgSourceId.setStatus("current")


class _HwClockBitsCfgTodSignal_Type(Integer32):
    """Custom type hwClockBitsCfgTodSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nmea", 1),
          ("none", 3),
          ("ubx", 2))
    )


_HwClockBitsCfgTodSignal_Type.__name__ = "Integer32"
_HwClockBitsCfgTodSignal_Object = MibTableColumn
hwClockBitsCfgTodSignal = _HwClockBitsCfgTodSignal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 15),
    _HwClockBitsCfgTodSignal_Type()
)
hwClockBitsCfgTodSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockBitsCfgTodSignal.setStatus("current")


class _HwClockBitsCfgFrameFormat_Type(Integer32):
    """Custom type hwClockBitsCfgFrameFormat based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pcm30crc", 2),
          ("pcm30nocrc", 1),
          ("pcm31crc", 4),
          ("pcm31nocrc", 3))
    )


_HwClockBitsCfgFrameFormat_Type.__name__ = "Integer32"
_HwClockBitsCfgFrameFormat_Object = MibTableColumn
hwClockBitsCfgFrameFormat = _HwClockBitsCfgFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 4, 1, 16),
    _HwClockBitsCfgFrameFormat_Type()
)
hwClockBitsCfgFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockBitsCfgFrameFormat.setStatus("current")
_HwClockPortCfgTable_Object = MibTable
hwClockPortCfgTable = _HwClockPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 5)
)
if mibBuilder.loadTexts:
    hwClockPortCfgTable.setStatus("current")
_HwClockPortCfgEntry_Object = MibTableRow
hwClockPortCfgEntry = _HwClockPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 5, 1)
)
hwClockPortCfgEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockPortCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwClockPortCfgEntry.setStatus("current")
_HwClockPortCfgIfIndex_Type = InterfaceIndex
_HwClockPortCfgIfIndex_Object = MibTableColumn
hwClockPortCfgIfIndex = _HwClockPortCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 5, 1, 1),
    _HwClockPortCfgIfIndex_Type()
)
hwClockPortCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockPortCfgIfIndex.setStatus("current")


class _HwClockPortCfgLeftFramePri_Type(Integer32):
    """Custom type hwClockPortCfgLeftFramePri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwClockPortCfgLeftFramePri_Type.__name__ = "Integer32"
_HwClockPortCfgLeftFramePri_Object = MibTableColumn
hwClockPortCfgLeftFramePri = _HwClockPortCfgLeftFramePri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 5, 1, 2),
    _HwClockPortCfgLeftFramePri_Type()
)
hwClockPortCfgLeftFramePri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockPortCfgLeftFramePri.setStatus("current")


class _HwClockPortCfgRightFramePri_Type(Integer32):
    """Custom type hwClockPortCfgRightFramePri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwClockPortCfgRightFramePri_Type.__name__ = "Integer32"
_HwClockPortCfgRightFramePri_Object = MibTableColumn
hwClockPortCfgRightFramePri = _HwClockPortCfgRightFramePri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 5, 1, 3),
    _HwClockPortCfgRightFramePri_Type()
)
hwClockPortCfgRightFramePri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockPortCfgRightFramePri.setStatus("current")


class _HwClockPortCfgForceOutS1_Type(Integer32):
    """Custom type hwClockPortCfgForceOutS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_HwClockPortCfgForceOutS1_Type.__name__ = "Integer32"
_HwClockPortCfgForceOutS1_Object = MibTableColumn
hwClockPortCfgForceOutS1 = _HwClockPortCfgForceOutS1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 5, 1, 4),
    _HwClockPortCfgForceOutS1_Type()
)
hwClockPortCfgForceOutS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockPortCfgForceOutS1.setStatus("current")
_HwClockLineClkCfgTable_Object = MibTable
hwClockLineClkCfgTable = _HwClockLineClkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 6)
)
if mibBuilder.loadTexts:
    hwClockLineClkCfgTable.setStatus("current")
_HwClockLineClkCfgEntry_Object = MibTableRow
hwClockLineClkCfgEntry = _HwClockLineClkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 6, 1)
)
hwClockLineClkCfgEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockLineClkCfgChassisIndex"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockLineClkCfgSlotIndex"),
)
if mibBuilder.loadTexts:
    hwClockLineClkCfgEntry.setStatus("current")
_HwClockLineClkCfgChassisIndex_Type = PhysicalIndex
_HwClockLineClkCfgChassisIndex_Object = MibTableColumn
hwClockLineClkCfgChassisIndex = _HwClockLineClkCfgChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 6, 1, 1),
    _HwClockLineClkCfgChassisIndex_Type()
)
hwClockLineClkCfgChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockLineClkCfgChassisIndex.setStatus("current")


class _HwClockLineClkCfgSlotIndex_Type(Integer32):
    """Custom type hwClockLineClkCfgSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_HwClockLineClkCfgSlotIndex_Type.__name__ = "Integer32"
_HwClockLineClkCfgSlotIndex_Object = MibTableColumn
hwClockLineClkCfgSlotIndex = _HwClockLineClkCfgSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 6, 1, 2),
    _HwClockLineClkCfgSlotIndex_Type()
)
hwClockLineClkCfgSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockLineClkCfgSlotIndex.setStatus("current")
_HwClockLineClkCfgCardId_Type = Integer32
_HwClockLineClkCfgCardId_Object = MibTableColumn
hwClockLineClkCfgCardId = _HwClockLineClkCfgCardId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 6, 1, 3),
    _HwClockLineClkCfgCardId_Type()
)
hwClockLineClkCfgCardId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockLineClkCfgCardId.setStatus("current")
_HwClockLineClkCfgPortId_Type = Integer32
_HwClockLineClkCfgPortId_Object = MibTableColumn
hwClockLineClkCfgPortId = _HwClockLineClkCfgPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 6, 1, 4),
    _HwClockLineClkCfgPortId_Type()
)
hwClockLineClkCfgPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockLineClkCfgPortId.setStatus("current")
_HwClockLineClkCfgRecvS1_Type = Integer32
_HwClockLineClkCfgRecvS1_Object = MibTableColumn
hwClockLineClkCfgRecvS1 = _HwClockLineClkCfgRecvS1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 6, 1, 5),
    _HwClockLineClkCfgRecvS1_Type()
)
hwClockLineClkCfgRecvS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockLineClkCfgRecvS1.setStatus("current")
_HwClockLineClkCfgSendS1_Type = Integer32
_HwClockLineClkCfgSendS1_Object = MibTableColumn
hwClockLineClkCfgSendS1 = _HwClockLineClkCfgSendS1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 6, 1, 6),
    _HwClockLineClkCfgSendS1_Type()
)
hwClockLineClkCfgSendS1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockLineClkCfgSendS1.setStatus("current")
_HwClockLineCfgSoureId_Type = Integer32
_HwClockLineCfgSoureId_Object = MibTableColumn
hwClockLineCfgSoureId = _HwClockLineCfgSoureId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 6, 1, 7),
    _HwClockLineCfgSoureId_Type()
)
hwClockLineCfgSoureId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockLineCfgSoureId.setStatus("current")
_HwClockTrapOid_ObjectIdentity = ObjectIdentity
hwClockTrapOid = _HwClockTrapOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7)
)
_HwClockLastSourceName_Type = OctetString
_HwClockLastSourceName_Object = MibScalar
hwClockLastSourceName = _HwClockLastSourceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 1),
    _HwClockLastSourceName_Type()
)
hwClockLastSourceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockLastSourceName.setStatus("current")
_HwClockCurSourceName_Type = OctetString
_HwClockCurSourceName_Object = MibScalar
hwClockCurSourceName = _HwClockCurSourceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 2),
    _HwClockCurSourceName_Type()
)
hwClockCurSourceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCurSourceName.setStatus("current")


class _HwClockSourceOldLockMode_Type(Integer32):
    """Custom type hwClockSourceOldLockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              16,
              19)
        )
    )
    namedValues = NamedValues(
        *(("fastLock", 1),
          ("freeRun", 0),
          ("freeRunJudge", 16),
          ("hold", 3),
          ("holdJudge", 19),
          ("lock", 2))
    )


_HwClockSourceOldLockMode_Type.__name__ = "Integer32"
_HwClockSourceOldLockMode_Object = MibScalar
hwClockSourceOldLockMode = _HwClockSourceOldLockMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 3),
    _HwClockSourceOldLockMode_Type()
)
hwClockSourceOldLockMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockSourceOldLockMode.setStatus("current")
_HwClockChassisId_Type = Integer32
_HwClockChassisId_Object = MibScalar
hwClockChassisId = _HwClockChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 4),
    _HwClockChassisId_Type()
)
hwClockChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockChassisId.setStatus("current")


class _HwClockOldSourceState_Type(Integer32):
    """Custom type hwClockOldSourceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("holdoff", 4),
          ("initial", 0),
          ("normal", 1),
          ("wtr", 3))
    )


_HwClockOldSourceState_Type.__name__ = "Integer32"
_HwClockOldSourceState_Object = MibScalar
hwClockOldSourceState = _HwClockOldSourceState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 5),
    _HwClockOldSourceState_Type()
)
hwClockOldSourceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockOldSourceState.setStatus("current")


class _HwClockPllId_Type(Integer32):
    """Custom type hwClockPllId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sync2M1", 2),
          ("sync2M2", 3),
          ("system", 1))
    )


_HwClockPllId_Type.__name__ = "Integer32"
_HwClockPllId_Object = MibScalar
hwClockPllId = _HwClockPllId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 6),
    _HwClockPllId_Type()
)
hwClockPllId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockPllId.setStatus("current")


class _HwClockAttributeOutValue_Type(Integer32):
    """Custom type hwClockAttributeOutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 15),
          ("prc", 2),
          ("sec", 11),
          ("ssua", 4),
          ("ssub", 8),
          ("unk", 0))
    )


_HwClockAttributeOutValue_Type.__name__ = "Integer32"
_HwClockAttributeOutValue_Object = MibScalar
hwClockAttributeOutValue = _HwClockAttributeOutValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 7),
    _HwClockAttributeOutValue_Type()
)
hwClockAttributeOutValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockAttributeOutValue.setStatus("current")
_HwClockCesAcrSlot_Type = Integer32
_HwClockCesAcrSlot_Object = MibScalar
hwClockCesAcrSlot = _HwClockCesAcrSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 8),
    _HwClockCesAcrSlot_Type()
)
hwClockCesAcrSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesAcrSlot.setStatus("current")
_HwClockCesAcrCard_Type = Integer32
_HwClockCesAcrCard_Object = MibScalar
hwClockCesAcrCard = _HwClockCesAcrCard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 9),
    _HwClockCesAcrCard_Type()
)
hwClockCesAcrCard.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesAcrCard.setStatus("current")
_HwClockCesAcrDomain_Type = Integer32
_HwClockCesAcrDomain_Object = MibScalar
hwClockCesAcrDomain = _HwClockCesAcrDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 10),
    _HwClockCesAcrDomain_Type()
)
hwClockCesAcrDomain.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesAcrDomain.setStatus("current")
_HwClockCesAcrOldMasterPwName_Type = OctetString
_HwClockCesAcrOldMasterPwName_Object = MibScalar
hwClockCesAcrOldMasterPwName = _HwClockCesAcrOldMasterPwName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 11),
    _HwClockCesAcrOldMasterPwName_Type()
)
hwClockCesAcrOldMasterPwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesAcrOldMasterPwName.setStatus("current")
_HwClockCesAcrNewMasterPwName_Type = OctetString
_HwClockCesAcrNewMasterPwName_Object = MibScalar
hwClockCesAcrNewMasterPwName = _HwClockCesAcrNewMasterPwName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 12),
    _HwClockCesAcrNewMasterPwName_Type()
)
hwClockCesAcrNewMasterPwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesAcrNewMasterPwName.setStatus("current")
_HwClockCesAcrLockState_Type = Integer32
_HwClockCesAcrLockState_Object = MibScalar
hwClockCesAcrLockState = _HwClockCesAcrLockState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 13),
    _HwClockCesAcrLockState_Type()
)
hwClockCesAcrLockState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesAcrLockState.setStatus("current")
_HwClockCesDcrSlot_Type = Integer32
_HwClockCesDcrSlot_Object = MibScalar
hwClockCesDcrSlot = _HwClockCesDcrSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 14),
    _HwClockCesDcrSlot_Type()
)
hwClockCesDcrSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesDcrSlot.setStatus("current")
_HwClockCesDcrCard_Type = Integer32
_HwClockCesDcrCard_Object = MibScalar
hwClockCesDcrCard = _HwClockCesDcrCard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 15),
    _HwClockCesDcrCard_Type()
)
hwClockCesDcrCard.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesDcrCard.setStatus("current")
_HwClockCesDcrDomain_Type = Integer32
_HwClockCesDcrDomain_Object = MibScalar
hwClockCesDcrDomain = _HwClockCesDcrDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 16),
    _HwClockCesDcrDomain_Type()
)
hwClockCesDcrDomain.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesDcrDomain.setStatus("current")
_HwClockCesDcrOldMasterPwName_Type = OctetString
_HwClockCesDcrOldMasterPwName_Object = MibScalar
hwClockCesDcrOldMasterPwName = _HwClockCesDcrOldMasterPwName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 17),
    _HwClockCesDcrOldMasterPwName_Type()
)
hwClockCesDcrOldMasterPwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesDcrOldMasterPwName.setStatus("current")
_HwClockCesDcrNewMasterPwName_Type = OctetString
_HwClockCesDcrNewMasterPwName_Object = MibScalar
hwClockCesDcrNewMasterPwName = _HwClockCesDcrNewMasterPwName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 18),
    _HwClockCesDcrNewMasterPwName_Type()
)
hwClockCesDcrNewMasterPwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesDcrNewMasterPwName.setStatus("current")
_HwClockCesDcrLockState_Type = Integer32
_HwClockCesDcrLockState_Object = MibScalar
hwClockCesDcrLockState = _HwClockCesDcrLockState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 7, 19),
    _HwClockCesDcrLockState_Type()
)
hwClockCesDcrLockState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockCesDcrLockState.setStatus("current")
_HwClockNotifications_ObjectIdentity = ObjectIdentity
hwClockNotifications = _HwClockNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8)
)
_HwClockAttributeTable_Object = MibTable
hwClockAttributeTable = _HwClockAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9)
)
if mibBuilder.loadTexts:
    hwClockAttributeTable.setStatus("current")
_HwClockAttributeEntry_Object = MibTableRow
hwClockAttributeEntry = _HwClockAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1)
)
hwClockAttributeEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockAttributeChassisIndex"),
)
if mibBuilder.loadTexts:
    hwClockAttributeEntry.setStatus("current")
_HwClockAttributeChassisIndex_Type = PhysicalIndex
_HwClockAttributeChassisIndex_Object = MibTableColumn
hwClockAttributeChassisIndex = _HwClockAttributeChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 1),
    _HwClockAttributeChassisIndex_Type()
)
hwClockAttributeChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockAttributeChassisIndex.setStatus("current")


class _HwClockAttributeSysClkRunMode_Type(Integer32):
    """Custom type hwClockAttributeSysClkRunMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freeRun", 1),
          ("hold", 2),
          ("normal", 0))
    )


_HwClockAttributeSysClkRunMode_Type.__name__ = "Integer32"
_HwClockAttributeSysClkRunMode_Object = MibTableColumn
hwClockAttributeSysClkRunMode = _HwClockAttributeSysClkRunMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 2),
    _HwClockAttributeSysClkRunMode_Type()
)
hwClockAttributeSysClkRunMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeSysClkRunMode.setStatus("current")


class _HwClockAttributeSsmControl_Type(Integer32):
    """Custom type hwClockAttributeSsmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_HwClockAttributeSsmControl_Type.__name__ = "Integer32"
_HwClockAttributeSsmControl_Object = MibTableColumn
hwClockAttributeSsmControl = _HwClockAttributeSsmControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 3),
    _HwClockAttributeSsmControl_Type()
)
hwClockAttributeSsmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeSsmControl.setStatus("current")
_HwClockAttributeFreqCheckEnable_Type = EnabledStatus
_HwClockAttributeFreqCheckEnable_Object = MibTableColumn
hwClockAttributeFreqCheckEnable = _HwClockAttributeFreqCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 4),
    _HwClockAttributeFreqCheckEnable_Type()
)
hwClockAttributeFreqCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeFreqCheckEnable.setStatus("current")


class _HwClockAttributeRetrieveMode_Type(Integer32):
    """Custom type hwClockAttributeRetrieveMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noRetrieve", 1),
          ("retrieve", 0))
    )


_HwClockAttributeRetrieveMode_Type.__name__ = "Integer32"
_HwClockAttributeRetrieveMode_Object = MibTableColumn
hwClockAttributeRetrieveMode = _HwClockAttributeRetrieveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 5),
    _HwClockAttributeRetrieveMode_Type()
)
hwClockAttributeRetrieveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeRetrieveMode.setStatus("current")


class _HwClockAttributeWtrTime_Type(Integer32):
    """Custom type hwClockAttributeWtrTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_HwClockAttributeWtrTime_Type.__name__ = "Integer32"
_HwClockAttributeWtrTime_Object = MibTableColumn
hwClockAttributeWtrTime = _HwClockAttributeWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 6),
    _HwClockAttributeWtrTime_Type()
)
hwClockAttributeWtrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeWtrTime.setStatus("current")


class _HwClockAttributeHoldOffTime_Type(Integer32):
    """Custom type hwClockAttributeHoldOffTime based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1800),
    )


_HwClockAttributeHoldOffTime_Type.__name__ = "Integer32"
_HwClockAttributeHoldOffTime_Object = MibTableColumn
hwClockAttributeHoldOffTime = _HwClockAttributeHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 7),
    _HwClockAttributeHoldOffTime_Type()
)
hwClockAttributeHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeHoldOffTime.setStatus("current")


class _HwClockAttributeOutThreshold_Type(Integer32):
    """Custom type hwClockAttributeOutThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 15),
          ("prc", 2),
          ("sec", 11),
          ("ssua", 4),
          ("ssub", 8))
    )


_HwClockAttributeOutThreshold_Type.__name__ = "Integer32"
_HwClockAttributeOutThreshold_Object = MibTableColumn
hwClockAttributeOutThreshold = _HwClockAttributeOutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 8),
    _HwClockAttributeOutThreshold_Type()
)
hwClockAttributeOutThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeOutThreshold.setStatus("current")


class _HwClockAttributeSysMaxOutSsm_Type(Integer32):
    """Custom type hwClockAttributeSysMaxOutSsm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11)
        )
    )
    namedValues = NamedValues(
        *(("prc", 2),
          ("sec", 11),
          ("ssua", 4),
          ("ssub", 8),
          ("unk", 0))
    )


_HwClockAttributeSysMaxOutSsm_Type.__name__ = "Integer32"
_HwClockAttributeSysMaxOutSsm_Object = MibTableColumn
hwClockAttributeSysMaxOutSsm = _HwClockAttributeSysMaxOutSsm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 9),
    _HwClockAttributeSysMaxOutSsm_Type()
)
hwClockAttributeSysMaxOutSsm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeSysMaxOutSsm.setStatus("current")


class _HwClockAttribute2M1MaxOutSsm_Type(Integer32):
    """Custom type hwClockAttribute2M1MaxOutSsm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11)
        )
    )
    namedValues = NamedValues(
        *(("prc", 2),
          ("sec", 11),
          ("ssua", 4),
          ("ssub", 8),
          ("unk", 0))
    )


_HwClockAttribute2M1MaxOutSsm_Type.__name__ = "Integer32"
_HwClockAttribute2M1MaxOutSsm_Object = MibTableColumn
hwClockAttribute2M1MaxOutSsm = _HwClockAttribute2M1MaxOutSsm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 10),
    _HwClockAttribute2M1MaxOutSsm_Type()
)
hwClockAttribute2M1MaxOutSsm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttribute2M1MaxOutSsm.setStatus("current")


class _HwClockAttribute2M2MaxOutSsm_Type(Integer32):
    """Custom type hwClockAttribute2M2MaxOutSsm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11)
        )
    )
    namedValues = NamedValues(
        *(("prc", 2),
          ("sec", 11),
          ("ssua", 4),
          ("ssub", 8),
          ("unk", 0))
    )


_HwClockAttribute2M2MaxOutSsm_Type.__name__ = "Integer32"
_HwClockAttribute2M2MaxOutSsm_Object = MibTableColumn
hwClockAttribute2M2MaxOutSsm = _HwClockAttribute2M2MaxOutSsm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 11),
    _HwClockAttribute2M2MaxOutSsm_Type()
)
hwClockAttribute2M2MaxOutSsm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttribute2M2MaxOutSsm.setStatus("current")


class _HwClockAttributeSysClkLockMode_Type(Integer32):
    """Custom type hwClockAttributeSysClkLockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              16,
              19)
        )
    )
    namedValues = NamedValues(
        *(("fastLock", 1),
          ("freeRun", 0),
          ("freeRunJudge", 16),
          ("hold", 3),
          ("holdJudge", 19),
          ("lock", 2))
    )


_HwClockAttributeSysClkLockMode_Type.__name__ = "Integer32"
_HwClockAttributeSysClkLockMode_Object = MibTableColumn
hwClockAttributeSysClkLockMode = _HwClockAttributeSysClkLockMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 12),
    _HwClockAttributeSysClkLockMode_Type()
)
hwClockAttributeSysClkLockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockAttributeSysClkLockMode.setStatus("current")


class _HwClockAttributeExtendSsmControl_Type(Integer32):
    """Custom type hwClockAttributeExtendSsmControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_HwClockAttributeExtendSsmControl_Type.__name__ = "Integer32"
_HwClockAttributeExtendSsmControl_Object = MibTableColumn
hwClockAttributeExtendSsmControl = _HwClockAttributeExtendSsmControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 13),
    _HwClockAttributeExtendSsmControl_Type()
)
hwClockAttributeExtendSsmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeExtendSsmControl.setStatus("current")


class _HwClockAttributeInternalClockId_Type(Integer32):
    """Custom type hwClockAttributeInternalClockId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwClockAttributeInternalClockId_Type.__name__ = "Integer32"
_HwClockAttributeInternalClockId_Object = MibTableColumn
hwClockAttributeInternalClockId = _HwClockAttributeInternalClockId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 14),
    _HwClockAttributeInternalClockId_Type()
)
hwClockAttributeInternalClockId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeInternalClockId.setStatus("current")


class _HwClockAttributeTodProtocol_Type(Integer32):
    """Custom type hwClockAttributeTodProtocol based on Integer32"""
    defaultValue = 2

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
        *(("ccsa", 4),
          ("nmea", 1),
          ("none", 3),
          ("ubx", 2))
    )


_HwClockAttributeTodProtocol_Type.__name__ = "Integer32"
_HwClockAttributeTodProtocol_Object = MibTableColumn
hwClockAttributeTodProtocol = _HwClockAttributeTodProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 15),
    _HwClockAttributeTodProtocol_Type()
)
hwClockAttributeTodProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeTodProtocol.setStatus("current")


class _HwClockAttributeLtiSquelch_Type(EnabledStatus):
    """Custom type hwClockAttributeLtiSquelch based on EnabledStatus"""
    defaultValue = 2


_HwClockAttributeLtiSquelch_Object = MibTableColumn
hwClockAttributeLtiSquelch = _HwClockAttributeLtiSquelch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 16),
    _HwClockAttributeLtiSquelch_Type()
)
hwClockAttributeLtiSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeLtiSquelch.setStatus("current")


class _HwClockAttributeInputThreshold_Type(Integer32):
    """Custom type hwClockAttributeInputThreshold based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8,
              11,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 15),
          ("prc", 2),
          ("sec", 11),
          ("ssua", 4),
          ("ssub", 8))
    )


_HwClockAttributeInputThreshold_Type.__name__ = "Integer32"
_HwClockAttributeInputThreshold_Object = MibTableColumn
hwClockAttributeInputThreshold = _HwClockAttributeInputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 9, 1, 17),
    _HwClockAttributeInputThreshold_Type()
)
hwClockAttributeInputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockAttributeInputThreshold.setStatus("current")
_HwClockSrcSelTable_Object = MibTable
hwClockSrcSelTable = _HwClockSrcSelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 10)
)
if mibBuilder.loadTexts:
    hwClockSrcSelTable.setStatus("current")
_HwClockSrcSelEntry_Object = MibTableRow
hwClockSrcSelEntry = _HwClockSrcSelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 10, 1)
)
hwClockSrcSelEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockSrcSelChassisIndex"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockSrcSelType"),
)
if mibBuilder.loadTexts:
    hwClockSrcSelEntry.setStatus("current")
_HwClockSrcSelChassisIndex_Type = PhysicalIndex
_HwClockSrcSelChassisIndex_Object = MibTableColumn
hwClockSrcSelChassisIndex = _HwClockSrcSelChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 10, 1, 1),
    _HwClockSrcSelChassisIndex_Type()
)
hwClockSrcSelChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockSrcSelChassisIndex.setStatus("current")


class _HwClockSrcSelType_Type(Integer32):
    """Custom type hwClockSrcSelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sync2M1", 2),
          ("sync2M2", 3),
          ("system", 1))
    )


_HwClockSrcSelType_Type.__name__ = "Integer32"
_HwClockSrcSelType_Object = MibTableColumn
hwClockSrcSelType = _HwClockSrcSelType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 10, 1, 2),
    _HwClockSrcSelType_Type()
)
hwClockSrcSelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockSrcSelType.setStatus("current")


class _HwClockSrcSelMode_Type(Integer32):
    """Custom type hwClockSrcSelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("force", 2),
          ("manual", 1))
    )


_HwClockSrcSelMode_Type.__name__ = "Integer32"
_HwClockSrcSelMode_Object = MibTableColumn
hwClockSrcSelMode = _HwClockSrcSelMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 10, 1, 3),
    _HwClockSrcSelMode_Type()
)
hwClockSrcSelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSrcSelMode.setStatus("current")
_HwClockSrcSelSrcName_Type = OctetString
_HwClockSrcSelSrcName_Object = MibTableColumn
hwClockSrcSelSrcName = _HwClockSrcSelSrcName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 10, 1, 4),
    _HwClockSrcSelSrcName_Type()
)
hwClockSrcSelSrcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSrcSelSrcName.setStatus("current")
_HwClockSrcTraceSrcName_Type = OctetString
_HwClockSrcTraceSrcName_Object = MibTableColumn
hwClockSrcTraceSrcName = _HwClockSrcTraceSrcName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 10, 1, 5),
    _HwClockSrcTraceSrcName_Type()
)
hwClockSrcTraceSrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSrcTraceSrcName.setStatus("current")
_HwClockSrcCfgTable_Object = MibTable
hwClockSrcCfgTable = _HwClockSrcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11)
)
if mibBuilder.loadTexts:
    hwClockSrcCfgTable.setStatus("current")
_HwClockSrcCfgEntry_Object = MibTableRow
hwClockSrcCfgEntry = _HwClockSrcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1)
)
hwClockSrcCfgEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockSrcCfgChassisIndex"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockSrcCfgSourceTypeIndex"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockSrcCfgSourceIndex"),
)
if mibBuilder.loadTexts:
    hwClockSrcCfgEntry.setStatus("current")
_HwClockSrcCfgChassisIndex_Type = PhysicalIndex
_HwClockSrcCfgChassisIndex_Object = MibTableColumn
hwClockSrcCfgChassisIndex = _HwClockSrcCfgChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 1),
    _HwClockSrcCfgChassisIndex_Type()
)
hwClockSrcCfgChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockSrcCfgChassisIndex.setStatus("current")


class _HwClockSrcCfgSourceTypeIndex_Type(Integer32):
    """Custom type hwClockSrcCfgSourceTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bits", 1),
          ("interface", 3),
          ("ptp", 2))
    )


_HwClockSrcCfgSourceTypeIndex_Type.__name__ = "Integer32"
_HwClockSrcCfgSourceTypeIndex_Object = MibTableColumn
hwClockSrcCfgSourceTypeIndex = _HwClockSrcCfgSourceTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 2),
    _HwClockSrcCfgSourceTypeIndex_Type()
)
hwClockSrcCfgSourceTypeIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwClockSrcCfgSourceTypeIndex.setStatus("current")
_HwClockSrcCfgSourceIndex_Type = Integer32
_HwClockSrcCfgSourceIndex_Object = MibTableColumn
hwClockSrcCfgSourceIndex = _HwClockSrcCfgSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 3),
    _HwClockSrcCfgSourceIndex_Type()
)
hwClockSrcCfgSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockSrcCfgSourceIndex.setStatus("current")
_HwClockSrcCfgSourceDescr_Type = OctetString
_HwClockSrcCfgSourceDescr_Object = MibTableColumn
hwClockSrcCfgSourceDescr = _HwClockSrcCfgSourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 4),
    _HwClockSrcCfgSourceDescr_Type()
)
hwClockSrcCfgSourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSrcCfgSourceDescr.setStatus("current")
_HwClockSrcCfgClkEnable_Type = EnabledStatus
_HwClockSrcCfgClkEnable_Object = MibTableColumn
hwClockSrcCfgClkEnable = _HwClockSrcCfgClkEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 5),
    _HwClockSrcCfgClkEnable_Type()
)
hwClockSrcCfgClkEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockSrcCfgClkEnable.setStatus("current")


class _HwClockSrcCfgSystemPriority_Type(Integer32):
    """Custom type hwClockSrcCfgSystemPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwClockSrcCfgSystemPriority_Type.__name__ = "Integer32"
_HwClockSrcCfgSystemPriority_Object = MibTableColumn
hwClockSrcCfgSystemPriority = _HwClockSrcCfgSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 6),
    _HwClockSrcCfgSystemPriority_Type()
)
hwClockSrcCfgSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockSrcCfgSystemPriority.setStatus("current")


class _HwClockSrcCfg2M1Priority_Type(Integer32):
    """Custom type hwClockSrcCfg2M1Priority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwClockSrcCfg2M1Priority_Type.__name__ = "Integer32"
_HwClockSrcCfg2M1Priority_Object = MibTableColumn
hwClockSrcCfg2M1Priority = _HwClockSrcCfg2M1Priority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 7),
    _HwClockSrcCfg2M1Priority_Type()
)
hwClockSrcCfg2M1Priority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockSrcCfg2M1Priority.setStatus("current")


class _HwClockSrcCfg2M2Priority_Type(Integer32):
    """Custom type hwClockSrcCfg2M2Priority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwClockSrcCfg2M2Priority_Type.__name__ = "Integer32"
_HwClockSrcCfg2M2Priority_Object = MibTableColumn
hwClockSrcCfg2M2Priority = _HwClockSrcCfg2M2Priority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 8),
    _HwClockSrcCfg2M2Priority_Type()
)
hwClockSrcCfg2M2Priority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockSrcCfg2M2Priority.setStatus("current")


class _HwClockSrcCfgSourceSsm_Type(Integer32):
    """Custom type hwClockSrcCfgSourceSsm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 15),
          ("prc", 2),
          ("sec", 11),
          ("ssua", 4),
          ("ssub", 8),
          ("unk", 0),
          ("unknown", 16))
    )


_HwClockSrcCfgSourceSsm_Type.__name__ = "Integer32"
_HwClockSrcCfgSourceSsm_Object = MibTableColumn
hwClockSrcCfgSourceSsm = _HwClockSrcCfgSourceSsm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 9),
    _HwClockSrcCfgSourceSsm_Type()
)
hwClockSrcCfgSourceSsm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockSrcCfgSourceSsm.setStatus("current")


class _HwClockSrcCfgSsmSetMode_Type(Integer32):
    """Custom type hwClockSrcCfgSsmSetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 1))
    )


_HwClockSrcCfgSsmSetMode_Type.__name__ = "Integer32"
_HwClockSrcCfgSsmSetMode_Object = MibTableColumn
hwClockSrcCfgSsmSetMode = _HwClockSrcCfgSsmSetMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 10),
    _HwClockSrcCfgSsmSetMode_Type()
)
hwClockSrcCfgSsmSetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSrcCfgSsmSetMode.setStatus("current")


class _HwClockSrcCfgSourceState_Type(Integer32):
    """Custom type hwClockSrcCfgSourceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("holdoff", 4),
          ("initial", 0),
          ("normal", 1),
          ("waitwtr", 3))
    )


_HwClockSrcCfgSourceState_Type.__name__ = "Integer32"
_HwClockSrcCfgSourceState_Object = MibTableColumn
hwClockSrcCfgSourceState = _HwClockSrcCfgSourceState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 11),
    _HwClockSrcCfgSourceState_Type()
)
hwClockSrcCfgSourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSrcCfgSourceState.setStatus("current")


class _HwClockSrcCfgFreqCheckResult_Type(Integer32):
    """Custom type hwClockSrcCfgFreqCheckResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 0),
          ("normal", 1))
    )


_HwClockSrcCfgFreqCheckResult_Type.__name__ = "Integer32"
_HwClockSrcCfgFreqCheckResult_Object = MibTableColumn
hwClockSrcCfgFreqCheckResult = _HwClockSrcCfgFreqCheckResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 12),
    _HwClockSrcCfgFreqCheckResult_Type()
)
hwClockSrcCfgFreqCheckResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSrcCfgFreqCheckResult.setStatus("current")


class _HwClockSrcCfgSsmInterval_Type(Integer32):
    """Custom type hwClockSrcCfgSsmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 8000),
    )


_HwClockSrcCfgSsmInterval_Type.__name__ = "Integer32"
_HwClockSrcCfgSsmInterval_Object = MibTableColumn
hwClockSrcCfgSsmInterval = _HwClockSrcCfgSsmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 13),
    _HwClockSrcCfgSsmInterval_Type()
)
hwClockSrcCfgSsmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockSrcCfgSsmInterval.setStatus("current")


class _HwClockSrcCfgSsmTimeout_Type(Integer32):
    """Custom type hwClockSrcCfgSsmTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 32000),
    )


_HwClockSrcCfgSsmTimeout_Type.__name__ = "Integer32"
_HwClockSrcCfgSsmTimeout_Object = MibTableColumn
hwClockSrcCfgSsmTimeout = _HwClockSrcCfgSsmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 14),
    _HwClockSrcCfgSsmTimeout_Type()
)
hwClockSrcCfgSsmTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockSrcCfgSsmTimeout.setStatus("current")


class _HwClockSrcCfgSabit_Type(Integer32):
    """Custom type hwClockSrcCfgSabit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              99)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 99),
          ("sa4", 4),
          ("sa5", 5),
          ("sa6", 6),
          ("sa7", 7),
          ("sa8", 8))
    )


_HwClockSrcCfgSabit_Type.__name__ = "Integer32"
_HwClockSrcCfgSabit_Object = MibTableColumn
hwClockSrcCfgSabit = _HwClockSrcCfgSabit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 15),
    _HwClockSrcCfgSabit_Type()
)
hwClockSrcCfgSabit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSrcCfgSabit.setStatus("current")


class _HwClockSrcCfgClockId_Type(Integer32):
    """Custom type hwClockSrcCfgClockId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwClockSrcCfgClockId_Type.__name__ = "Integer32"
_HwClockSrcCfgClockId_Object = MibTableColumn
hwClockSrcCfgClockId = _HwClockSrcCfgClockId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 16),
    _HwClockSrcCfgClockId_Type()
)
hwClockSrcCfgClockId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwClockSrcCfgClockId.setStatus("current")


class _HwClockSrcCfgClockIdSetMode_Type(Integer32):
    """Custom type hwClockSrcCfgClockIdSetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 1))
    )


_HwClockSrcCfgClockIdSetMode_Type.__name__ = "Integer32"
_HwClockSrcCfgClockIdSetMode_Object = MibTableColumn
hwClockSrcCfgClockIdSetMode = _HwClockSrcCfgClockIdSetMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 17),
    _HwClockSrcCfgClockIdSetMode_Type()
)
hwClockSrcCfgClockIdSetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSrcCfgClockIdSetMode.setStatus("current")


class _HwClockSrcCfgOutSsm_Type(Integer32):
    """Custom type hwClockSrcCfgOutSsm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15,
              16,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 15),
          ("invalid", 99),
          ("prc", 2),
          ("sec", 11),
          ("ssua", 4),
          ("ssub", 8),
          ("unk", 0),
          ("unknown", 16))
    )


_HwClockSrcCfgOutSsm_Type.__name__ = "Integer32"
_HwClockSrcCfgOutSsm_Object = MibTableColumn
hwClockSrcCfgOutSsm = _HwClockSrcCfgOutSsm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 18),
    _HwClockSrcCfgOutSsm_Type()
)
hwClockSrcCfgOutSsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSrcCfgOutSsm.setStatus("current")


class _HwClockSrcCfgOutClockId_Type(Integer32):
    """Custom type hwClockSrcCfgOutClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("clockid0", 0),
          ("clockid1", 1),
          ("clockid10", 10),
          ("clockid11", 11),
          ("clockid12", 12),
          ("clockid13", 13),
          ("clockid14", 14),
          ("clockid15", 15),
          ("clockid2", 2),
          ("clockid3", 3),
          ("clockid4", 4),
          ("clockid5", 5),
          ("clockid6", 6),
          ("clockid7", 7),
          ("clockid8", 8),
          ("clockid9", 9),
          ("notsupport", 99))
    )


_HwClockSrcCfgOutClockId_Type.__name__ = "Integer32"
_HwClockSrcCfgOutClockId_Object = MibTableColumn
hwClockSrcCfgOutClockId = _HwClockSrcCfgOutClockId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 19),
    _HwClockSrcCfgOutClockId_Type()
)
hwClockSrcCfgOutClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSrcCfgOutClockId.setStatus("current")
_HwClockSrcCfgRowStatus_Type = RowStatus
_HwClockSrcCfgRowStatus_Object = MibTableColumn
hwClockSrcCfgRowStatus = _HwClockSrcCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 20),
    _HwClockSrcCfgRowStatus_Type()
)
hwClockSrcCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockSrcCfgRowStatus.setStatus("current")
_HwClockSrcCfgFreqDeviation_Type = OctetString
_HwClockSrcCfgFreqDeviation_Object = MibTableColumn
hwClockSrcCfgFreqDeviation = _HwClockSrcCfgFreqDeviation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 21),
    _HwClockSrcCfgFreqDeviation_Type()
)
hwClockSrcCfgFreqDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSrcCfgFreqDeviation.setStatus("current")


class _HwClockSrcCfgPhyState_Type(Integer32):
    """Custom type hwClockSrcCfgPhyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cardTypeNotSupport", 0),
          ("master", 2),
          ("portDown", 4),
          ("slave", 1),
          ("speedNotSupport", 3))
    )


_HwClockSrcCfgPhyState_Type.__name__ = "Integer32"
_HwClockSrcCfgPhyState_Object = MibTableColumn
hwClockSrcCfgPhyState = _HwClockSrcCfgPhyState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 22),
    _HwClockSrcCfgPhyState_Type()
)
hwClockSrcCfgPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockSrcCfgPhyState.setStatus("current")


class _HwClockSrcCfgNegotiationSlave_Type(Integer32):
    """Custom type hwClockSrcCfgNegotiationSlave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notSupport", 0))
    )


_HwClockSrcCfgNegotiationSlave_Type.__name__ = "Integer32"
_HwClockSrcCfgNegotiationSlave_Object = MibTableColumn
hwClockSrcCfgNegotiationSlave = _HwClockSrcCfgNegotiationSlave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 11, 1, 23),
    _HwClockSrcCfgNegotiationSlave_Type()
)
hwClockSrcCfgNegotiationSlave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockSrcCfgNegotiationSlave.setStatus("current")
_HwClockCesAcrPortCfgTable_Object = MibTable
hwClockCesAcrPortCfgTable = _HwClockCesAcrPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12)
)
if mibBuilder.loadTexts:
    hwClockCesAcrPortCfgTable.setStatus("current")
_HwClockCesAcrPortCfgEntry_Object = MibTableRow
hwClockCesAcrPortCfgEntry = _HwClockCesAcrPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1)
)
hwClockCesAcrPortCfgEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockCesAcrParentIfIndex"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockCesAcrChannelId"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockCesAcrIfIndex"),
)
if mibBuilder.loadTexts:
    hwClockCesAcrPortCfgEntry.setStatus("current")
_HwClockCesAcrParentIfIndex_Type = InterfaceIndex
_HwClockCesAcrParentIfIndex_Object = MibTableColumn
hwClockCesAcrParentIfIndex = _HwClockCesAcrParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1, 1),
    _HwClockCesAcrParentIfIndex_Type()
)
hwClockCesAcrParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockCesAcrParentIfIndex.setStatus("current")
_HwClockCesAcrChannelId_Type = Integer32
_HwClockCesAcrChannelId_Object = MibTableColumn
hwClockCesAcrChannelId = _HwClockCesAcrChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1, 2),
    _HwClockCesAcrChannelId_Type()
)
hwClockCesAcrChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockCesAcrChannelId.setStatus("current")
_HwClockCesAcrIfIndex_Type = InterfaceIndex
_HwClockCesAcrIfIndex_Object = MibTableColumn
hwClockCesAcrIfIndex = _HwClockCesAcrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1, 3),
    _HwClockCesAcrIfIndex_Type()
)
hwClockCesAcrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockCesAcrIfIndex.setStatus("current")
_HwClockCesAcrPortName_Type = OctetString
_HwClockCesAcrPortName_Object = MibTableColumn
hwClockCesAcrPortName = _HwClockCesAcrPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1, 4),
    _HwClockCesAcrPortName_Type()
)
hwClockCesAcrPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockCesAcrPortName.setStatus("current")


class _HwClockCesAcrChannelType_Type(Integer32):
    """Custom type hwClockCesAcrChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_HwClockCesAcrChannelType_Type.__name__ = "Integer32"
_HwClockCesAcrChannelType_Object = MibTableColumn
hwClockCesAcrChannelType = _HwClockCesAcrChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1, 5),
    _HwClockCesAcrChannelType_Type()
)
hwClockCesAcrChannelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesAcrChannelType.setStatus("current")


class _HwClockCesAcrSourceMode_Type(Integer32):
    """Custom type hwClockCesAcrSourceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("recoveryDomain", 3),
          ("slave", 2))
    )


_HwClockCesAcrSourceMode_Type.__name__ = "Integer32"
_HwClockCesAcrSourceMode_Object = MibTableColumn
hwClockCesAcrSourceMode = _HwClockCesAcrSourceMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1, 6),
    _HwClockCesAcrSourceMode_Type()
)
hwClockCesAcrSourceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesAcrSourceMode.setStatus("current")


class _HwClockCesAcrRecoveryDomain_Type(Integer32):
    """Custom type hwClockCesAcrRecoveryDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwClockCesAcrRecoveryDomain_Type.__name__ = "Integer32"
_HwClockCesAcrRecoveryDomain_Object = MibTableColumn
hwClockCesAcrRecoveryDomain = _HwClockCesAcrRecoveryDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1, 7),
    _HwClockCesAcrRecoveryDomain_Type()
)
hwClockCesAcrRecoveryDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesAcrRecoveryDomain.setStatus("current")


class _HwClockCesAcrPwDomain_Type(Integer32):
    """Custom type hwClockCesAcrPwDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwClockCesAcrPwDomain_Type.__name__ = "Integer32"
_HwClockCesAcrPwDomain_Object = MibTableColumn
hwClockCesAcrPwDomain = _HwClockCesAcrPwDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1, 8),
    _HwClockCesAcrPwDomain_Type()
)
hwClockCesAcrPwDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesAcrPwDomain.setStatus("current")
_HwClockCesAcrPortCfgRowStatus_Type = RowStatus
_HwClockCesAcrPortCfgRowStatus_Object = MibTableColumn
hwClockCesAcrPortCfgRowStatus = _HwClockCesAcrPortCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1, 9),
    _HwClockCesAcrPortCfgRowStatus_Type()
)
hwClockCesAcrPortCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesAcrPortCfgRowStatus.setStatus("current")


class _HwClockCesAcrMasterDomain_Type(Integer32):
    """Custom type hwClockCesAcrMasterDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwClockCesAcrMasterDomain_Type.__name__ = "Integer32"
_HwClockCesAcrMasterDomain_Object = MibTableColumn
hwClockCesAcrMasterDomain = _HwClockCesAcrMasterDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1, 10),
    _HwClockCesAcrMasterDomain_Type()
)
hwClockCesAcrMasterDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesAcrMasterDomain.setStatus("current")


class _HwClockCesMode_Type(Integer32):
    """Custom type hwClockCesMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acr", 1),
          ("dcr", 2))
    )


_HwClockCesMode_Type.__name__ = "Integer32"
_HwClockCesMode_Object = MibTableColumn
hwClockCesMode = _HwClockCesMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 12, 1, 11),
    _HwClockCesMode_Type()
)
hwClockCesMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesMode.setStatus("current")
_HwClockCesAcrCfgTable_Object = MibTable
hwClockCesAcrCfgTable = _HwClockCesAcrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13)
)
if mibBuilder.loadTexts:
    hwClockCesAcrCfgTable.setStatus("current")
_HwClockCesAcrCfgEntry_Object = MibTableRow
hwClockCesAcrCfgEntry = _HwClockCesAcrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1)
)
hwClockCesAcrCfgEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockCesAcrCfgSlot"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockCesAcrCfgCard"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockCesAcrCfgDomain"),
)
if mibBuilder.loadTexts:
    hwClockCesAcrCfgEntry.setStatus("current")
_HwClockCesAcrCfgSlot_Type = Integer32
_HwClockCesAcrCfgSlot_Object = MibTableColumn
hwClockCesAcrCfgSlot = _HwClockCesAcrCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1, 1),
    _HwClockCesAcrCfgSlot_Type()
)
hwClockCesAcrCfgSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockCesAcrCfgSlot.setStatus("current")
_HwClockCesAcrCfgCard_Type = Integer32
_HwClockCesAcrCfgCard_Object = MibTableColumn
hwClockCesAcrCfgCard = _HwClockCesAcrCfgCard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1, 2),
    _HwClockCesAcrCfgCard_Type()
)
hwClockCesAcrCfgCard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockCesAcrCfgCard.setStatus("current")


class _HwClockCesAcrCfgDomain_Type(Integer32):
    """Custom type hwClockCesAcrCfgDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwClockCesAcrCfgDomain_Type.__name__ = "Integer32"
_HwClockCesAcrCfgDomain_Object = MibTableColumn
hwClockCesAcrCfgDomain = _HwClockCesAcrCfgDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1, 3),
    _HwClockCesAcrCfgDomain_Type()
)
hwClockCesAcrCfgDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockCesAcrCfgDomain.setStatus("current")
_HwClockCesAcrCfgDescr_Type = OctetString
_HwClockCesAcrCfgDescr_Object = MibTableColumn
hwClockCesAcrCfgDescr = _HwClockCesAcrCfgDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1, 4),
    _HwClockCesAcrCfgDescr_Type()
)
hwClockCesAcrCfgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockCesAcrCfgDescr.setStatus("current")
_HwClockCesAcrCfgSyncEnable_Type = EnabledStatus
_HwClockCesAcrCfgSyncEnable_Object = MibTableColumn
hwClockCesAcrCfgSyncEnable = _HwClockCesAcrCfgSyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1, 5),
    _HwClockCesAcrCfgSyncEnable_Type()
)
hwClockCesAcrCfgSyncEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesAcrCfgSyncEnable.setStatus("current")


class _HwClockCesAcrCfgSystemPriority_Type(Integer32):
    """Custom type hwClockCesAcrCfgSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwClockCesAcrCfgSystemPriority_Type.__name__ = "Integer32"
_HwClockCesAcrCfgSystemPriority_Object = MibTableColumn
hwClockCesAcrCfgSystemPriority = _HwClockCesAcrCfgSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1, 6),
    _HwClockCesAcrCfgSystemPriority_Type()
)
hwClockCesAcrCfgSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesAcrCfgSystemPriority.setStatus("current")


class _HwClockCesAcrCfgSsm_Type(Integer32):
    """Custom type hwClockCesAcrCfgSsm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              8,
              11,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 15),
          ("prc", 2),
          ("sec", 11),
          ("ssua", 4),
          ("ssub", 8),
          ("unk", 0),
          ("unknown", 16))
    )


_HwClockCesAcrCfgSsm_Type.__name__ = "Integer32"
_HwClockCesAcrCfgSsm_Object = MibTableColumn
hwClockCesAcrCfgSsm = _HwClockCesAcrCfgSsm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1, 7),
    _HwClockCesAcrCfgSsm_Type()
)
hwClockCesAcrCfgSsm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesAcrCfgSsm.setStatus("current")


class _HwClockCesAcrCfgClockId_Type(Integer32):
    """Custom type hwClockCesAcrCfgClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwClockCesAcrCfgClockId_Type.__name__ = "Integer32"
_HwClockCesAcrCfgClockId_Object = MibTableColumn
hwClockCesAcrCfgClockId = _HwClockCesAcrCfgClockId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1, 8),
    _HwClockCesAcrCfgClockId_Type()
)
hwClockCesAcrCfgClockId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesAcrCfgClockId.setStatus("current")


class _HwClockCesAcrCfgSourceState_Type(Integer32):
    """Custom type hwClockCesAcrCfgSourceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("holdoff", 4),
          ("initial", 0),
          ("normal", 1),
          ("waitwtr", 3))
    )


_HwClockCesAcrCfgSourceState_Type.__name__ = "Integer32"
_HwClockCesAcrCfgSourceState_Object = MibTableColumn
hwClockCesAcrCfgSourceState = _HwClockCesAcrCfgSourceState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1, 9),
    _HwClockCesAcrCfgSourceState_Type()
)
hwClockCesAcrCfgSourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockCesAcrCfgSourceState.setStatus("current")


class _HwClockCesAcrCfgFreqCheckResult_Type(Integer32):
    """Custom type hwClockCesAcrCfgFreqCheckResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 0),
          ("normal", 1))
    )


_HwClockCesAcrCfgFreqCheckResult_Type.__name__ = "Integer32"
_HwClockCesAcrCfgFreqCheckResult_Object = MibTableColumn
hwClockCesAcrCfgFreqCheckResult = _HwClockCesAcrCfgFreqCheckResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1, 10),
    _HwClockCesAcrCfgFreqCheckResult_Type()
)
hwClockCesAcrCfgFreqCheckResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockCesAcrCfgFreqCheckResult.setStatus("current")
_HwClockCesAcrCfgRowStatus_Type = RowStatus
_HwClockCesAcrCfgRowStatus_Object = MibTableColumn
hwClockCesAcrCfgRowStatus = _HwClockCesAcrCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 13, 1, 11),
    _HwClockCesAcrCfgRowStatus_Type()
)
hwClockCesAcrCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwClockCesAcrCfgRowStatus.setStatus("current")
_HwClockCesAcrDomainInfoTable_Object = MibTable
hwClockCesAcrDomainInfoTable = _HwClockCesAcrDomainInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 14)
)
if mibBuilder.loadTexts:
    hwClockCesAcrDomainInfoTable.setStatus("current")
_HwClockCesAcrDomainInfoEntry_Object = MibTableRow
hwClockCesAcrDomainInfoEntry = _HwClockCesAcrDomainInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 14, 1)
)
hwClockCesAcrDomainInfoEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockCesAcrDomianInfoSlot"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockCesAcrDomianInfoCard"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockCesAcrDomianInfoDomain"),
)
if mibBuilder.loadTexts:
    hwClockCesAcrDomainInfoEntry.setStatus("current")
_HwClockCesAcrDomianInfoSlot_Type = Integer32
_HwClockCesAcrDomianInfoSlot_Object = MibTableColumn
hwClockCesAcrDomianInfoSlot = _HwClockCesAcrDomianInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 14, 1, 1),
    _HwClockCesAcrDomianInfoSlot_Type()
)
hwClockCesAcrDomianInfoSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockCesAcrDomianInfoSlot.setStatus("current")
_HwClockCesAcrDomianInfoCard_Type = Integer32
_HwClockCesAcrDomianInfoCard_Object = MibTableColumn
hwClockCesAcrDomianInfoCard = _HwClockCesAcrDomianInfoCard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 14, 1, 2),
    _HwClockCesAcrDomianInfoCard_Type()
)
hwClockCesAcrDomianInfoCard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockCesAcrDomianInfoCard.setStatus("current")


class _HwClockCesAcrDomianInfoDomain_Type(Integer32):
    """Custom type hwClockCesAcrDomianInfoDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwClockCesAcrDomianInfoDomain_Type.__name__ = "Integer32"
_HwClockCesAcrDomianInfoDomain_Object = MibTableColumn
hwClockCesAcrDomianInfoDomain = _HwClockCesAcrDomianInfoDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 14, 1, 3),
    _HwClockCesAcrDomianInfoDomain_Type()
)
hwClockCesAcrDomianInfoDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClockCesAcrDomianInfoDomain.setStatus("current")
_HwClockCesAcrDomianInfoMasterPwName_Type = OctetString
_HwClockCesAcrDomianInfoMasterPwName_Object = MibTableColumn
hwClockCesAcrDomianInfoMasterPwName = _HwClockCesAcrDomianInfoMasterPwName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 14, 1, 4),
    _HwClockCesAcrDomianInfoMasterPwName_Type()
)
hwClockCesAcrDomianInfoMasterPwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockCesAcrDomianInfoMasterPwName.setStatus("current")
_HwClockCesAcrDomianInfoChannelId_Type = Integer32
_HwClockCesAcrDomianInfoChannelId_Object = MibTableColumn
hwClockCesAcrDomianInfoChannelId = _HwClockCesAcrDomianInfoChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 14, 1, 5),
    _HwClockCesAcrDomianInfoChannelId_Type()
)
hwClockCesAcrDomianInfoChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockCesAcrDomianInfoChannelId.setStatus("current")


class _HwClockCesAcrDomianInfoState_Type(Integer32):
    """Custom type hwClockCesAcrDomianInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lock", 3),
          ("none", 1),
          ("wait", 2))
    )


_HwClockCesAcrDomianInfoState_Type.__name__ = "Integer32"
_HwClockCesAcrDomianInfoState_Object = MibTableColumn
hwClockCesAcrDomianInfoState = _HwClockCesAcrDomianInfoState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 14, 1, 6),
    _HwClockCesAcrDomianInfoState_Type()
)
hwClockCesAcrDomianInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockCesAcrDomianInfoState.setStatus("current")
_HwClockClusterTopoTable_Object = MibTable
hwClockClusterTopoTable = _HwClockClusterTopoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 15)
)
if mibBuilder.loadTexts:
    hwClockClusterTopoTable.setStatus("current")
_HwClockClusterTopoEntry_Object = MibTableRow
hwClockClusterTopoEntry = _HwClockClusterTopoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 15, 1)
)
hwClockClusterTopoEntry.setIndexNames(
    (0, "HUAWEI-CLOCK-MIB", "hwClockClusterSyncType"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockClusterTopoType"),
    (0, "HUAWEI-CLOCK-MIB", "hwClockClusterTopoLinkType"),
)
if mibBuilder.loadTexts:
    hwClockClusterTopoEntry.setStatus("current")


class _HwClockClusterSyncType_Type(Integer32):
    """Custom type hwClockClusterSyncType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frequency", 1),
          ("time", 2))
    )


_HwClockClusterSyncType_Type.__name__ = "Integer32"
_HwClockClusterSyncType_Object = MibTableColumn
hwClockClusterSyncType = _HwClockClusterSyncType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 15, 1, 1),
    _HwClockClusterSyncType_Type()
)
hwClockClusterSyncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockClusterSyncType.setStatus("current")


class _HwClockClusterTopoType_Type(Integer32):
    """Custom type hwClockClusterTopoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("interlink", 1)
    )


_HwClockClusterTopoType_Type.__name__ = "Integer32"
_HwClockClusterTopoType_Object = MibTableColumn
hwClockClusterTopoType = _HwClockClusterTopoType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 15, 1, 2),
    _HwClockClusterTopoType_Type()
)
hwClockClusterTopoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockClusterTopoType.setStatus("current")


class _HwClockClusterTopoLinkType_Type(Integer32):
    """Custom type hwClockClusterTopoLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bits", 1)
    )


_HwClockClusterTopoLinkType_Type.__name__ = "Integer32"
_HwClockClusterTopoLinkType_Object = MibTableColumn
hwClockClusterTopoLinkType = _HwClockClusterTopoLinkType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 15, 1, 3),
    _HwClockClusterTopoLinkType_Type()
)
hwClockClusterTopoLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockClusterTopoLinkType.setStatus("current")


class _HwClockClusterTopoStatus_Type(Integer32):
    """Custom type hwClockClusterTopoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("success", 2))
    )


_HwClockClusterTopoStatus_Type.__name__ = "Integer32"
_HwClockClusterTopoStatus_Object = MibTableColumn
hwClockClusterTopoStatus = _HwClockClusterTopoStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 15, 1, 4),
    _HwClockClusterTopoStatus_Type()
)
hwClockClusterTopoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClockClusterTopoStatus.setStatus("current")
_HwClockConformance_ObjectIdentity = ObjectIdentity
hwClockConformance = _HwClockConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10)
)
_HwClockSourceCompliances_ObjectIdentity = ObjectIdentity
hwClockSourceCompliances = _HwClockSourceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10, 1)
)
_HwClockSourceGroups_ObjectIdentity = ObjectIdentity
hwClockSourceGroups = _HwClockSourceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10, 2)
)

# Managed Objects groups

hwClockManageSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10, 2, 8)
)
hwClockManageSysGroup.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockSourceSysClkWorkMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceFreqCheckEnable"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceHoldMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceSsmControl"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceFreqCheckRightRange"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceFreqCheckLeftRange"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceRetrieveMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceForceCloseEnableStatus"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceSsmUnknown"),
        ("HUAWEI-CLOCK-MIB", "hwClockExtTimeOutputType"),
        ("HUAWEI-CLOCK-MIB", "hwClockExtTimeInputType"),
        ("HUAWEI-CLOCK-MIB", "hwClockTimeUsedSource"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceEthClkEnable"),
        ("HUAWEI-CLOCK-MIB", "hwClockAlarmThresholdFrequencyOffset"),
        ("HUAWEI-CLOCK-MIB", "hwClockFrequencyOffsetMax"),
        ("HUAWEI-CLOCK-MIB", "hwClockFrequencyOffsetMin"),
        ("HUAWEI-CLOCK-MIB", "hwClockFrequencyOffsetMean"),
        ("HUAWEI-CLOCK-MIB", "hwClockFrequencyOffset"))
)
if mibBuilder.loadTexts:
    hwClockManageSysGroup.setStatus("current")

hwClockSysSelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10, 2, 9)
)
hwClockSysSelGroup.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockSourceSelMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceSelSourceId"),
        ("HUAWEI-CLOCK-MIB", "hwClockCurSourceName"),
        ("HUAWEI-CLOCK-MIB", "hwClockLastSourceName"),
        ("HUAWEI-CLOCK-MIB", "hwClockPllId"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceOldLockMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrOldMasterPwName"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrNewMasterPwName"),
        ("HUAWEI-CLOCK-MIB", "hwClockAttributeOutValue"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrSlot"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrLockState"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrDomain"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrCard"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrSlot"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrCard"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrDomain"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrOldMasterPwName"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrNewMasterPwName"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrLockState"))
)
if mibBuilder.loadTexts:
    hwClockSysSelGroup.setStatus("current")

hwClockSourceCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10, 2, 10)
)
hwClockSourceCfgGroup.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockCfgSourceId"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgPriRvtEnableStatus"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgSwitchCondition"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgWtrTime"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgBadDetect"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgSourceSsm"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgExportEnableStatus"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgSwiEnableStatus"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgSourceState"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgSourceDescr"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgFreqCheckResult"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgHoldOffTime"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgBits0Priority"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgBits1Priority"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgSystemPriority"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgSourceSsmSetMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgSourceS1Id"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgClkSourceType"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgSsmThreshold"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgSystemLockOut"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgBits0LockOut"),
        ("HUAWEI-CLOCK-MIB", "hwClockCfgBits1LockOut"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgTodSignal"))
)
if mibBuilder.loadTexts:
    hwClockSourceCfgGroup.setStatus("current")

hwClockPortCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10, 2, 13)
)
hwClockPortCfgGroup.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockPortCfgLeftFramePri"),
        ("HUAWEI-CLOCK-MIB", "hwClockPortCfgRightFramePri"),
        ("HUAWEI-CLOCK-MIB", "hwClockPortCfgForceOutS1"))
)
if mibBuilder.loadTexts:
    hwClockPortCfgGroup.setStatus("current")

hwClockBitsCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10, 2, 14)
)
hwClockBitsCfgGroup.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockBitsCfgRecvSaBit"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgSendSaBit"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgForceOutS1"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgName"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgBitsType"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgDirection"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgSaBit"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgInputMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgOutputMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgSourceId"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgInvalidCond"),
        ("HUAWEI-CLOCK-MIB", "hwClockBitsCfgBitsPortType"))
)
if mibBuilder.loadTexts:
    hwClockBitsCfgGroup.setStatus("current")

hwClockTrapOidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10, 2, 15)
)
hwClockTrapOidGroup.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockLastSourceName"),
        ("HUAWEI-CLOCK-MIB", "hwClockCurSourceName"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceOldLockMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockOldSourceState"))
)
if mibBuilder.loadTexts:
    hwClockTrapOidGroup.setStatus("current")

hwClockLineCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10, 2, 17)
)
hwClockLineCfgGroup.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockLineClkCfgRecvS1"),
        ("HUAWEI-CLOCK-MIB", "hwClockLineClkCfgSendS1"),
        ("HUAWEI-CLOCK-MIB", "hwClockLineClkCfgCardId"),
        ("HUAWEI-CLOCK-MIB", "hwClockLineClkCfgPortId"))
)
if mibBuilder.loadTexts:
    hwClockLineCfgGroup.setStatus("current")


# Notification objects

hwClockSourceSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 1)
)
hwClockSourceSwitch.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockPllId"),
        ("HUAWEI-CLOCK-MIB", "hwClockLastSourceName"),
        ("HUAWEI-CLOCK-MIB", "hwClockCurSourceName"),
        ("HUAWEI-CLOCK-MIB", "hwClockSrcSelMode"))
)
if mibBuilder.loadTexts:
    hwClockSourceSwitch.setStatus(
        "current"
    )

hwClockSourceSysClkLockModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 2)
)
hwClockSourceSysClkLockModeChange.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceOldLockMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockAttributeSysClkLockMode"))
)
if mibBuilder.loadTexts:
    hwClockSourceSysClkLockModeChange.setStatus(
        "current"
    )

hwClockSourceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 3)
)
hwClockSourceStateChange.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockCurSourceName"),
        ("HUAWEI-CLOCK-MIB", "hwClockOldSourceState"),
        ("HUAWEI-CLOCK-MIB", "hwClockSrcCfgSourceState"))
)
if mibBuilder.loadTexts:
    hwClockSourceStateChange.setStatus(
        "current"
    )

hwClockSourceStateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 4)
)
hwClockSourceStateResume.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockCurSourceName"),
        ("HUAWEI-CLOCK-MIB", "hwClockOldSourceState"),
        ("HUAWEI-CLOCK-MIB", "hwClockSrcCfgSourceState"))
)
if mibBuilder.loadTexts:
    hwClockSourceStateResume.setStatus(
        "current"
    )

hwClockSourceFreqCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 5)
)
hwClockSourceFreqCheck.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockSrcCfgSourceDescr"),
        ("HUAWEI-CLOCK-MIB", "hwClockSrcCfgFreqCheckResult"))
)
if mibBuilder.loadTexts:
    hwClockSourceFreqCheck.setStatus(
        "current"
    )

hwClockSourceOutputBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 6)
)
hwClockSourceOutputBelowThreshold.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockPllId"),
        ("HUAWEI-CLOCK-MIB", "hwClockCurSourceName"),
        ("HUAWEI-CLOCK-MIB", "hwClockAttributeOutThreshold"),
        ("HUAWEI-CLOCK-MIB", "hwClockAttributeOutValue"))
)
if mibBuilder.loadTexts:
    hwClockSourceOutputBelowThreshold.setStatus(
        "current"
    )

hwClockNotInLockedMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 7)
)
hwClockNotInLockedMode.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockAttributeSysClkLockMode"))
)
if mibBuilder.loadTexts:
    hwClockNotInLockedMode.setStatus(
        "current"
    )

hwClockInLockedMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 8)
)
hwClockInLockedMode.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockAttributeSysClkLockMode"))
)
if mibBuilder.loadTexts:
    hwClockInLockedMode.setStatus(
        "current"
    )

hwClockSourceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 11)
)
hwClockSourceFailed.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockCurSourceName"),
        ("HUAWEI-CLOCK-MIB", "hwClockSrcCfgSourceState"))
)
if mibBuilder.loadTexts:
    hwClockSourceFailed.setStatus(
        "current"
    )

hwClockSourceValid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 12)
)
hwClockSourceValid.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockCurSourceName"),
        ("HUAWEI-CLOCK-MIB", "hwClockSrcCfgSourceState"))
)
if mibBuilder.loadTexts:
    hwClockSourceValid.setStatus(
        "current"
    )

hwClockSourceFreqCheckResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 13)
)
hwClockSourceFreqCheckResume.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockSrcCfgSourceDescr"),
        ("HUAWEI-CLOCK-MIB", "hwClockSrcCfgFreqCheckResult"))
)
if mibBuilder.loadTexts:
    hwClockSourceFreqCheckResume.setStatus(
        "current"
    )

hwClockSourceOutputBelowThresholdResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 14)
)
hwClockSourceOutputBelowThresholdResume.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockPllId"),
        ("HUAWEI-CLOCK-MIB", "hwClockAttributeOutThreshold"),
        ("HUAWEI-CLOCK-MIB", "hwClockAttributeOutValue"),
        ("HUAWEI-CLOCK-MIB", "hwClockCurSourceName"))
)
if mibBuilder.loadTexts:
    hwClockSourceOutputBelowThresholdResume.setStatus(
        "current"
    )

hwClockCesAcrMasterPwChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 15)
)
hwClockCesAcrMasterPwChange.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockCesAcrSlot"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrCard"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrDomain"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrOldMasterPwName"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrNewMasterPwName"))
)
if mibBuilder.loadTexts:
    hwClockCesAcrMasterPwChange.setStatus(
        "current"
    )

hwClockCesAcrLockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 16)
)
hwClockCesAcrLockFail.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockCesAcrSlot"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrCard"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrDomain"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrLockState"))
)
if mibBuilder.loadTexts:
    hwClockCesAcrLockFail.setStatus(
        "current"
    )

hwClockCesAcrLockFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 17)
)
hwClockCesAcrLockFailResume.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockCesAcrSlot"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrCard"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrDomain"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrLockState"))
)
if mibBuilder.loadTexts:
    hwClockCesAcrLockFailResume.setStatus(
        "current"
    )

hwClockClusterTopoFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 22)
)
hwClockClusterTopoFail.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockClusterSyncType"),
        ("HUAWEI-CLOCK-MIB", "hwClockClusterTopoType"),
        ("HUAWEI-CLOCK-MIB", "hwClockClusterTopoLinkType"),
        ("HUAWEI-CLOCK-MIB", "hwClockClusterTopoStatus"))
)
if mibBuilder.loadTexts:
    hwClockClusterTopoFail.setStatus(
        "current"
    )

hwClockClusterTopoFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 23)
)
hwClockClusterTopoFailResume.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockClusterSyncType"),
        ("HUAWEI-CLOCK-MIB", "hwClockClusterTopoType"),
        ("HUAWEI-CLOCK-MIB", "hwClockClusterTopoLinkType"),
        ("HUAWEI-CLOCK-MIB", "hwClockClusterTopoStatus"))
)
if mibBuilder.loadTexts:
    hwClockClusterTopoFailResume.setStatus(
        "current"
    )

hwClockSourceInputBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 24)
)
hwClockSourceInputBelowThreshold.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockPllId"),
        ("HUAWEI-CLOCK-MIB", "hwClockAttributeInputThreshold"),
        ("HUAWEI-CLOCK-MIB", "hwClockSrcCfgSourceSsm"))
)
if mibBuilder.loadTexts:
    hwClockSourceInputBelowThreshold.setStatus(
        "current"
    )

hwClockSourceInputBelowThresholdResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 25)
)
hwClockSourceInputBelowThresholdResume.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockChassisId"),
        ("HUAWEI-CLOCK-MIB", "hwClockPllId"),
        ("HUAWEI-CLOCK-MIB", "hwClockAttributeInputThreshold"),
        ("HUAWEI-CLOCK-MIB", "hwClockSrcCfgSourceSsm"))
)
if mibBuilder.loadTexts:
    hwClockSourceInputBelowThresholdResume.setStatus(
        "current"
    )

hwClockSsmPktLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 26)
)
hwClockSsmPktLos.setObjects(
    ("HUAWEI-CLOCK-MIB", "hwClockCurSourceName")
)
if mibBuilder.loadTexts:
    hwClockSsmPktLos.setStatus(
        "current"
    )

hwClockSsmPktLosResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 27)
)
hwClockSsmPktLosResume.setObjects(
    ("HUAWEI-CLOCK-MIB", "hwClockCurSourceName")
)
if mibBuilder.loadTexts:
    hwClockSsmPktLosResume.setStatus(
        "current"
    )

hwClockCesDcrMasterPwChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 28)
)
hwClockCesDcrMasterPwChange.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockCesDcrSlot"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrCard"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrDomain"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrOldMasterPwName"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrNewMasterPwName"))
)
if mibBuilder.loadTexts:
    hwClockCesDcrMasterPwChange.setStatus(
        "current"
    )

hwClockCesDcrLockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 29)
)
hwClockCesDcrLockFail.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockCesDcrSlot"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrCard"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrDomain"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrLockState"))
)
if mibBuilder.loadTexts:
    hwClockCesDcrLockFail.setStatus(
        "current"
    )

hwClockCesDcrLockFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 1, 8, 30)
)
hwClockCesDcrLockFailResume.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockCesDcrSlot"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrCard"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrDomain"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrLockState"))
)
if mibBuilder.loadTexts:
    hwClockCesDcrLockFailResume.setStatus(
        "current"
    )


# Notifications groups

hwClockNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10, 2, 16)
)
hwClockNotificationsGroup.setObjects(
      *(("HUAWEI-CLOCK-MIB", "hwClockSourceSwitch"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceStateChange"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceStateResume"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceFreqCheck"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceFreqCheckResume"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceOutputBelowThreshold"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceOutputBelowThresholdResume"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrLockFail"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrLockFailResume"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesAcrMasterPwChange"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceValid"),
        ("HUAWEI-CLOCK-MIB", "hwClockInLockedMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockClusterTopoFailResume"),
        ("HUAWEI-CLOCK-MIB", "hwClockClusterTopoFail"),
        ("HUAWEI-CLOCK-MIB", "hwClockNotInLockedMode"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceSysClkLockModeChange"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceFailed"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceInputBelowThreshold"),
        ("HUAWEI-CLOCK-MIB", "hwClockSourceInputBelowThresholdResume"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrMasterPwChange"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrLockFail"),
        ("HUAWEI-CLOCK-MIB", "hwClockCesDcrLockFailResume"),
        ("HUAWEI-CLOCK-MIB", "hwClockSsmPktLos"),
        ("HUAWEI-CLOCK-MIB", "hwClockSsmPktLosResume"))
)
if mibBuilder.loadTexts:
    hwClockNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwClockSourceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 186, 10, 1, 1)
)
if mibBuilder.loadTexts:
    hwClockSourceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-CLOCK-MIB",
    **{"hwClockMIB": hwClockMIB,
       "hwClockManageObjects": hwClockManageObjects,
       "hwClockGlobalObjects": hwClockGlobalObjects,
       "hwClockSourceEthClkEnable": hwClockSourceEthClkEnable,
       "hwClockSourceSsmUnknown": hwClockSourceSsmUnknown,
       "hwClockSourceSysClkWorkMode": hwClockSourceSysClkWorkMode,
       "hwClockSourceForceCloseEnableStatus": hwClockSourceForceCloseEnableStatus,
       "hwClockSourceSsmControl": hwClockSourceSsmControl,
       "hwClockSourceHoldMode": hwClockSourceHoldMode,
       "hwClockSourceFreqCheckEnable": hwClockSourceFreqCheckEnable,
       "hwClockSourceFreqCheckLeftRange": hwClockSourceFreqCheckLeftRange,
       "hwClockSourceFreqCheckRightRange": hwClockSourceFreqCheckRightRange,
       "hwClockSourceRetrieveMode": hwClockSourceRetrieveMode,
       "hwClockTimeUsedSource": hwClockTimeUsedSource,
       "hwClockExtTimeInputType": hwClockExtTimeInputType,
       "hwClockExtTimeOutputType": hwClockExtTimeOutputType,
       "hwClockAlarmThresholdFrequencyOffset": hwClockAlarmThresholdFrequencyOffset,
       "hwClockFrequencyOffsetMax": hwClockFrequencyOffsetMax,
       "hwClockFrequencyOffsetMin": hwClockFrequencyOffsetMin,
       "hwClockFrequencyOffsetMean": hwClockFrequencyOffsetMean,
       "hwClockFrequencyOffset": hwClockFrequencyOffset,
       "hwClockSourceSelTable": hwClockSourceSelTable,
       "hwClockSourceSelEntry": hwClockSourceSelEntry,
       "hwClockSourceSelChassisIndex": hwClockSourceSelChassisIndex,
       "hwClockSourceSelType": hwClockSourceSelType,
       "hwClockSourceSelMode": hwClockSourceSelMode,
       "hwClockSourceSelSourceId": hwClockSourceSelSourceId,
       "hwClockSourceCfgTable": hwClockSourceCfgTable,
       "hwClockSourceCfgEntry": hwClockSourceCfgEntry,
       "hwClockCfgChassisIndex": hwClockCfgChassisIndex,
       "hwClockCfgSourceIndex": hwClockCfgSourceIndex,
       "hwClockCfgSourceId": hwClockCfgSourceId,
       "hwClockCfgSourceDescr": hwClockCfgSourceDescr,
       "hwClockCfgWtrTime": hwClockCfgWtrTime,
       "hwClockCfgBadDetect": hwClockCfgBadDetect,
       "hwClockCfgSystemPriority": hwClockCfgSystemPriority,
       "hwClockCfgBits0Priority": hwClockCfgBits0Priority,
       "hwClockCfgBits1Priority": hwClockCfgBits1Priority,
       "hwClockCfgSystemLockOut": hwClockCfgSystemLockOut,
       "hwClockCfgBits0LockOut": hwClockCfgBits0LockOut,
       "hwClockCfgBits1LockOut": hwClockCfgBits1LockOut,
       "hwClockCfgSourceSsm": hwClockCfgSourceSsm,
       "hwClockCfgSourceSsmSetMode": hwClockCfgSourceSsmSetMode,
       "hwClockCfgExportEnableStatus": hwClockCfgExportEnableStatus,
       "hwClockCfgSwiEnableStatus": hwClockCfgSwiEnableStatus,
       "hwClockCfgSourceState": hwClockCfgSourceState,
       "hwClockCfgSsmThreshold": hwClockCfgSsmThreshold,
       "hwClockCfgSourceS1Id": hwClockCfgSourceS1Id,
       "hwClockCfgFreqCheckResult": hwClockCfgFreqCheckResult,
       "hwClockCfgHoldOffTime": hwClockCfgHoldOffTime,
       "hwClockCfgPriRvtEnableStatus": hwClockCfgPriRvtEnableStatus,
       "hwClockCfgSwitchCondition": hwClockCfgSwitchCondition,
       "hwClockCfgClkSourceType": hwClockCfgClkSourceType,
       "hwClockBitsCfgTable": hwClockBitsCfgTable,
       "hwClockBitsCfgEntry": hwClockBitsCfgEntry,
       "hwClockBitsCfgChassisIndex": hwClockBitsCfgChassisIndex,
       "hwClockBitsCfgBitsIndex": hwClockBitsCfgBitsIndex,
       "hwClockBitsCfgName": hwClockBitsCfgName,
       "hwClockBitsCfgBitsPortType": hwClockBitsCfgBitsPortType,
       "hwClockBitsCfgBitsType": hwClockBitsCfgBitsType,
       "hwClockBitsCfgDirection": hwClockBitsCfgDirection,
       "hwClockBitsCfgRecvSaBit": hwClockBitsCfgRecvSaBit,
       "hwClockBitsCfgSendSaBit": hwClockBitsCfgSendSaBit,
       "hwClockBitsCfgForceOutS1": hwClockBitsCfgForceOutS1,
       "hwClockBitsCfgSaBit": hwClockBitsCfgSaBit,
       "hwClockBitsCfgInputMode": hwClockBitsCfgInputMode,
       "hwClockBitsCfgOutputMode": hwClockBitsCfgOutputMode,
       "hwClockBitsCfgInvalidCond": hwClockBitsCfgInvalidCond,
       "hwClockBitsCfgSourceId": hwClockBitsCfgSourceId,
       "hwClockBitsCfgTodSignal": hwClockBitsCfgTodSignal,
       "hwClockBitsCfgFrameFormat": hwClockBitsCfgFrameFormat,
       "hwClockPortCfgTable": hwClockPortCfgTable,
       "hwClockPortCfgEntry": hwClockPortCfgEntry,
       "hwClockPortCfgIfIndex": hwClockPortCfgIfIndex,
       "hwClockPortCfgLeftFramePri": hwClockPortCfgLeftFramePri,
       "hwClockPortCfgRightFramePri": hwClockPortCfgRightFramePri,
       "hwClockPortCfgForceOutS1": hwClockPortCfgForceOutS1,
       "hwClockLineClkCfgTable": hwClockLineClkCfgTable,
       "hwClockLineClkCfgEntry": hwClockLineClkCfgEntry,
       "hwClockLineClkCfgChassisIndex": hwClockLineClkCfgChassisIndex,
       "hwClockLineClkCfgSlotIndex": hwClockLineClkCfgSlotIndex,
       "hwClockLineClkCfgCardId": hwClockLineClkCfgCardId,
       "hwClockLineClkCfgPortId": hwClockLineClkCfgPortId,
       "hwClockLineClkCfgRecvS1": hwClockLineClkCfgRecvS1,
       "hwClockLineClkCfgSendS1": hwClockLineClkCfgSendS1,
       "hwClockLineCfgSoureId": hwClockLineCfgSoureId,
       "hwClockTrapOid": hwClockTrapOid,
       "hwClockLastSourceName": hwClockLastSourceName,
       "hwClockCurSourceName": hwClockCurSourceName,
       "hwClockSourceOldLockMode": hwClockSourceOldLockMode,
       "hwClockChassisId": hwClockChassisId,
       "hwClockOldSourceState": hwClockOldSourceState,
       "hwClockPllId": hwClockPllId,
       "hwClockAttributeOutValue": hwClockAttributeOutValue,
       "hwClockCesAcrSlot": hwClockCesAcrSlot,
       "hwClockCesAcrCard": hwClockCesAcrCard,
       "hwClockCesAcrDomain": hwClockCesAcrDomain,
       "hwClockCesAcrOldMasterPwName": hwClockCesAcrOldMasterPwName,
       "hwClockCesAcrNewMasterPwName": hwClockCesAcrNewMasterPwName,
       "hwClockCesAcrLockState": hwClockCesAcrLockState,
       "hwClockCesDcrSlot": hwClockCesDcrSlot,
       "hwClockCesDcrCard": hwClockCesDcrCard,
       "hwClockCesDcrDomain": hwClockCesDcrDomain,
       "hwClockCesDcrOldMasterPwName": hwClockCesDcrOldMasterPwName,
       "hwClockCesDcrNewMasterPwName": hwClockCesDcrNewMasterPwName,
       "hwClockCesDcrLockState": hwClockCesDcrLockState,
       "hwClockNotifications": hwClockNotifications,
       "hwClockSourceSwitch": hwClockSourceSwitch,
       "hwClockSourceSysClkLockModeChange": hwClockSourceSysClkLockModeChange,
       "hwClockSourceStateChange": hwClockSourceStateChange,
       "hwClockSourceStateResume": hwClockSourceStateResume,
       "hwClockSourceFreqCheck": hwClockSourceFreqCheck,
       "hwClockSourceOutputBelowThreshold": hwClockSourceOutputBelowThreshold,
       "hwClockNotInLockedMode": hwClockNotInLockedMode,
       "hwClockInLockedMode": hwClockInLockedMode,
       "hwClockSourceFailed": hwClockSourceFailed,
       "hwClockSourceValid": hwClockSourceValid,
       "hwClockSourceFreqCheckResume": hwClockSourceFreqCheckResume,
       "hwClockSourceOutputBelowThresholdResume": hwClockSourceOutputBelowThresholdResume,
       "hwClockCesAcrMasterPwChange": hwClockCesAcrMasterPwChange,
       "hwClockCesAcrLockFail": hwClockCesAcrLockFail,
       "hwClockCesAcrLockFailResume": hwClockCesAcrLockFailResume,
       "hwClockClusterTopoFail": hwClockClusterTopoFail,
       "hwClockClusterTopoFailResume": hwClockClusterTopoFailResume,
       "hwClockSourceInputBelowThreshold": hwClockSourceInputBelowThreshold,
       "hwClockSourceInputBelowThresholdResume": hwClockSourceInputBelowThresholdResume,
       "hwClockSsmPktLos": hwClockSsmPktLos,
       "hwClockSsmPktLosResume": hwClockSsmPktLosResume,
       "hwClockCesDcrMasterPwChange": hwClockCesDcrMasterPwChange,
       "hwClockCesDcrLockFail": hwClockCesDcrLockFail,
       "hwClockCesDcrLockFailResume": hwClockCesDcrLockFailResume,
       "hwClockAttributeTable": hwClockAttributeTable,
       "hwClockAttributeEntry": hwClockAttributeEntry,
       "hwClockAttributeChassisIndex": hwClockAttributeChassisIndex,
       "hwClockAttributeSysClkRunMode": hwClockAttributeSysClkRunMode,
       "hwClockAttributeSsmControl": hwClockAttributeSsmControl,
       "hwClockAttributeFreqCheckEnable": hwClockAttributeFreqCheckEnable,
       "hwClockAttributeRetrieveMode": hwClockAttributeRetrieveMode,
       "hwClockAttributeWtrTime": hwClockAttributeWtrTime,
       "hwClockAttributeHoldOffTime": hwClockAttributeHoldOffTime,
       "hwClockAttributeOutThreshold": hwClockAttributeOutThreshold,
       "hwClockAttributeSysMaxOutSsm": hwClockAttributeSysMaxOutSsm,
       "hwClockAttribute2M1MaxOutSsm": hwClockAttribute2M1MaxOutSsm,
       "hwClockAttribute2M2MaxOutSsm": hwClockAttribute2M2MaxOutSsm,
       "hwClockAttributeSysClkLockMode": hwClockAttributeSysClkLockMode,
       "hwClockAttributeExtendSsmControl": hwClockAttributeExtendSsmControl,
       "hwClockAttributeInternalClockId": hwClockAttributeInternalClockId,
       "hwClockAttributeTodProtocol": hwClockAttributeTodProtocol,
       "hwClockAttributeLtiSquelch": hwClockAttributeLtiSquelch,
       "hwClockAttributeInputThreshold": hwClockAttributeInputThreshold,
       "hwClockSrcSelTable": hwClockSrcSelTable,
       "hwClockSrcSelEntry": hwClockSrcSelEntry,
       "hwClockSrcSelChassisIndex": hwClockSrcSelChassisIndex,
       "hwClockSrcSelType": hwClockSrcSelType,
       "hwClockSrcSelMode": hwClockSrcSelMode,
       "hwClockSrcSelSrcName": hwClockSrcSelSrcName,
       "hwClockSrcTraceSrcName": hwClockSrcTraceSrcName,
       "hwClockSrcCfgTable": hwClockSrcCfgTable,
       "hwClockSrcCfgEntry": hwClockSrcCfgEntry,
       "hwClockSrcCfgChassisIndex": hwClockSrcCfgChassisIndex,
       "hwClockSrcCfgSourceTypeIndex": hwClockSrcCfgSourceTypeIndex,
       "hwClockSrcCfgSourceIndex": hwClockSrcCfgSourceIndex,
       "hwClockSrcCfgSourceDescr": hwClockSrcCfgSourceDescr,
       "hwClockSrcCfgClkEnable": hwClockSrcCfgClkEnable,
       "hwClockSrcCfgSystemPriority": hwClockSrcCfgSystemPriority,
       "hwClockSrcCfg2M1Priority": hwClockSrcCfg2M1Priority,
       "hwClockSrcCfg2M2Priority": hwClockSrcCfg2M2Priority,
       "hwClockSrcCfgSourceSsm": hwClockSrcCfgSourceSsm,
       "hwClockSrcCfgSsmSetMode": hwClockSrcCfgSsmSetMode,
       "hwClockSrcCfgSourceState": hwClockSrcCfgSourceState,
       "hwClockSrcCfgFreqCheckResult": hwClockSrcCfgFreqCheckResult,
       "hwClockSrcCfgSsmInterval": hwClockSrcCfgSsmInterval,
       "hwClockSrcCfgSsmTimeout": hwClockSrcCfgSsmTimeout,
       "hwClockSrcCfgSabit": hwClockSrcCfgSabit,
       "hwClockSrcCfgClockId": hwClockSrcCfgClockId,
       "hwClockSrcCfgClockIdSetMode": hwClockSrcCfgClockIdSetMode,
       "hwClockSrcCfgOutSsm": hwClockSrcCfgOutSsm,
       "hwClockSrcCfgOutClockId": hwClockSrcCfgOutClockId,
       "hwClockSrcCfgRowStatus": hwClockSrcCfgRowStatus,
       "hwClockSrcCfgFreqDeviation": hwClockSrcCfgFreqDeviation,
       "hwClockSrcCfgPhyState": hwClockSrcCfgPhyState,
       "hwClockSrcCfgNegotiationSlave": hwClockSrcCfgNegotiationSlave,
       "hwClockCesAcrPortCfgTable": hwClockCesAcrPortCfgTable,
       "hwClockCesAcrPortCfgEntry": hwClockCesAcrPortCfgEntry,
       "hwClockCesAcrParentIfIndex": hwClockCesAcrParentIfIndex,
       "hwClockCesAcrChannelId": hwClockCesAcrChannelId,
       "hwClockCesAcrIfIndex": hwClockCesAcrIfIndex,
       "hwClockCesAcrPortName": hwClockCesAcrPortName,
       "hwClockCesAcrChannelType": hwClockCesAcrChannelType,
       "hwClockCesAcrSourceMode": hwClockCesAcrSourceMode,
       "hwClockCesAcrRecoveryDomain": hwClockCesAcrRecoveryDomain,
       "hwClockCesAcrPwDomain": hwClockCesAcrPwDomain,
       "hwClockCesAcrPortCfgRowStatus": hwClockCesAcrPortCfgRowStatus,
       "hwClockCesAcrMasterDomain": hwClockCesAcrMasterDomain,
       "hwClockCesMode": hwClockCesMode,
       "hwClockCesAcrCfgTable": hwClockCesAcrCfgTable,
       "hwClockCesAcrCfgEntry": hwClockCesAcrCfgEntry,
       "hwClockCesAcrCfgSlot": hwClockCesAcrCfgSlot,
       "hwClockCesAcrCfgCard": hwClockCesAcrCfgCard,
       "hwClockCesAcrCfgDomain": hwClockCesAcrCfgDomain,
       "hwClockCesAcrCfgDescr": hwClockCesAcrCfgDescr,
       "hwClockCesAcrCfgSyncEnable": hwClockCesAcrCfgSyncEnable,
       "hwClockCesAcrCfgSystemPriority": hwClockCesAcrCfgSystemPriority,
       "hwClockCesAcrCfgSsm": hwClockCesAcrCfgSsm,
       "hwClockCesAcrCfgClockId": hwClockCesAcrCfgClockId,
       "hwClockCesAcrCfgSourceState": hwClockCesAcrCfgSourceState,
       "hwClockCesAcrCfgFreqCheckResult": hwClockCesAcrCfgFreqCheckResult,
       "hwClockCesAcrCfgRowStatus": hwClockCesAcrCfgRowStatus,
       "hwClockCesAcrDomainInfoTable": hwClockCesAcrDomainInfoTable,
       "hwClockCesAcrDomainInfoEntry": hwClockCesAcrDomainInfoEntry,
       "hwClockCesAcrDomianInfoSlot": hwClockCesAcrDomianInfoSlot,
       "hwClockCesAcrDomianInfoCard": hwClockCesAcrDomianInfoCard,
       "hwClockCesAcrDomianInfoDomain": hwClockCesAcrDomianInfoDomain,
       "hwClockCesAcrDomianInfoMasterPwName": hwClockCesAcrDomianInfoMasterPwName,
       "hwClockCesAcrDomianInfoChannelId": hwClockCesAcrDomianInfoChannelId,
       "hwClockCesAcrDomianInfoState": hwClockCesAcrDomianInfoState,
       "hwClockClusterTopoTable": hwClockClusterTopoTable,
       "hwClockClusterTopoEntry": hwClockClusterTopoEntry,
       "hwClockClusterSyncType": hwClockClusterSyncType,
       "hwClockClusterTopoType": hwClockClusterTopoType,
       "hwClockClusterTopoLinkType": hwClockClusterTopoLinkType,
       "hwClockClusterTopoStatus": hwClockClusterTopoStatus,
       "hwClockConformance": hwClockConformance,
       "hwClockSourceCompliances": hwClockSourceCompliances,
       "hwClockSourceCompliance": hwClockSourceCompliance,
       "hwClockSourceGroups": hwClockSourceGroups,
       "hwClockManageSysGroup": hwClockManageSysGroup,
       "hwClockSysSelGroup": hwClockSysSelGroup,
       "hwClockSourceCfgGroup": hwClockSourceCfgGroup,
       "hwClockPortCfgGroup": hwClockPortCfgGroup,
       "hwClockBitsCfgGroup": hwClockBitsCfgGroup,
       "hwClockTrapOidGroup": hwClockTrapOidGroup,
       "hwClockNotificationsGroup": hwClockNotificationsGroup,
       "hwClockLineCfgGroup": hwClockLineCfgGroup}
)
