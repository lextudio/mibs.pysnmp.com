# SNMP MIB module (HUAWEI-PERFMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PERFMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:27 2024
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hwPerfMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190)
)
hwPerfMgmt.setRevisions(
        ("2015-10-16 14:34",
         "2015-09-21 14:34",
         "2015-02-07 14:34",
         "2015-02-06 14:34",
         "2014-05-05 16:31",
         "2014-03-13 21:19",
         "2013-10-14 16:55",
         "2013-09-26 10:00",
         "2013-05-20 15:12",
         "2013-05-20 15:12",
         "2013-05-20 15:12",
         "2011-03-16 00:00",
         "2009-02-27 11:41")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwPMStatisticsMIBInstances_ObjectIdentity = ObjectIdentity
hwPMStatisticsMIBInstances = _HwPMStatisticsMIBInstances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1)
)


class _HwPMStatisticsEnable_Type(Integer32):
    """Custom type hwPMStatisticsEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwPMStatisticsEnable_Type.__name__ = "Integer32"
_HwPMStatisticsEnable_Object = MibScalar
hwPMStatisticsEnable = _HwPMStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 1),
    _HwPMStatisticsEnable_Type()
)
hwPMStatisticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPMStatisticsEnable.setStatus("current")
_HwPMStatisticsMaxFilesPerTask_Type = Unsigned32
_HwPMStatisticsMaxFilesPerTask_Object = MibScalar
hwPMStatisticsMaxFilesPerTask = _HwPMStatisticsMaxFilesPerTask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 2),
    _HwPMStatisticsMaxFilesPerTask_Type()
)
hwPMStatisticsMaxFilesPerTask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMStatisticsMaxFilesPerTask.setStatus("current")
_HwPMStatisticsMaxTasks_Type = Unsigned32
_HwPMStatisticsMaxTasks_Object = MibScalar
hwPMStatisticsMaxTasks = _HwPMStatisticsMaxTasks_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 3),
    _HwPMStatisticsMaxTasks_Type()
)
hwPMStatisticsMaxTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMStatisticsMaxTasks.setStatus("current")
_HwPMStatisticsCurrentTasks_Type = Unsigned32
_HwPMStatisticsCurrentTasks_Object = MibScalar
hwPMStatisticsCurrentTasks = _HwPMStatisticsCurrentTasks_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 4),
    _HwPMStatisticsCurrentTasks_Type()
)
hwPMStatisticsCurrentTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMStatisticsCurrentTasks.setStatus("current")
_HwPMStatisticsTaskTable_Object = MibTable
hwPMStatisticsTaskTable = _HwPMStatisticsTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5)
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskTable.setStatus("current")
_HwPMStatisticsTaskEntry_Object = MibTableRow
hwPMStatisticsTaskEntry = _HwPMStatisticsTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1)
)
hwPMStatisticsTaskEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskName"),
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskEntry.setStatus("current")


class _HwPMStatisticsTaskName_Type(OctetString):
    """Custom type hwPMStatisticsTaskName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwPMStatisticsTaskName_Type.__name__ = "OctetString"
_HwPMStatisticsTaskName_Object = MibTableColumn
hwPMStatisticsTaskName = _HwPMStatisticsTaskName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 1),
    _HwPMStatisticsTaskName_Type()
)
hwPMStatisticsTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskName.setStatus("current")


class _HwPMStatisticsTaskFileFormat_Type(Integer32):
    """Custom type hwPMStatisticsTaskFileFormat based on Integer32"""
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
        *(("hwPM3Gppxmlv1", 3),
          ("hwPMbinv1", 2),
          ("hwPMtxtv1", 1))
    )


_HwPMStatisticsTaskFileFormat_Type.__name__ = "Integer32"
_HwPMStatisticsTaskFileFormat_Object = MibTableColumn
hwPMStatisticsTaskFileFormat = _HwPMStatisticsTaskFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 2),
    _HwPMStatisticsTaskFileFormat_Type()
)
hwPMStatisticsTaskFileFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskFileFormat.setStatus("current")


class _HwPMStatisticsRecordFileEnable_Type(Integer32):
    """Custom type hwPMStatisticsRecordFileEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwPMStatisticsRecordFileEnable_Type.__name__ = "Integer32"
_HwPMStatisticsRecordFileEnable_Object = MibTableColumn
hwPMStatisticsRecordFileEnable = _HwPMStatisticsRecordFileEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 3),
    _HwPMStatisticsRecordFileEnable_Type()
)
hwPMStatisticsRecordFileEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsRecordFileEnable.setStatus("current")


class _HwPMStatisticsThresholdEnable_Type(Integer32):
    """Custom type hwPMStatisticsThresholdEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwPMStatisticsThresholdEnable_Type.__name__ = "Integer32"
_HwPMStatisticsThresholdEnable_Object = MibTableColumn
hwPMStatisticsThresholdEnable = _HwPMStatisticsThresholdEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 4),
    _HwPMStatisticsThresholdEnable_Type()
)
hwPMStatisticsThresholdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsThresholdEnable.setStatus("current")


class _HwPMStatisticsTaskPeriod_Type(Integer32):
    """Custom type hwPMStatisticsTaskPeriod based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              10,
              15,
              30,
              60,
              1440)
        )
    )
    namedValues = NamedValues(
        *(("fifteen", 15),
          ("five", 5),
          ("invalid", 0),
          ("sixty", 60),
          ("ten", 10),
          ("thirty", 30),
          ("twentyfourhours", 1440))
    )


_HwPMStatisticsTaskPeriod_Type.__name__ = "Integer32"
_HwPMStatisticsTaskPeriod_Object = MibTableColumn
hwPMStatisticsTaskPeriod = _HwPMStatisticsTaskPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 5),
    _HwPMStatisticsTaskPeriod_Type()
)
hwPMStatisticsTaskPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskPeriod.setStatus("current")


class _HwPMStatisticsTaskTransferPeriod_Type(Integer32):
    """Custom type hwPMStatisticsTaskTransferPeriod based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HwPMStatisticsTaskTransferPeriod_Type.__name__ = "Integer32"
_HwPMStatisticsTaskTransferPeriod_Object = MibTableColumn
hwPMStatisticsTaskTransferPeriod = _HwPMStatisticsTaskTransferPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 6),
    _HwPMStatisticsTaskTransferPeriod_Type()
)
hwPMStatisticsTaskTransferPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskTransferPeriod.setStatus("current")


class _HwPMStatisticsTaskCurrentFileIndex_Type(Unsigned32):
    """Custom type hwPMStatisticsTaskCurrentFileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HwPMStatisticsTaskCurrentFileIndex_Type.__name__ = "Unsigned32"
_HwPMStatisticsTaskCurrentFileIndex_Object = MibTableColumn
hwPMStatisticsTaskCurrentFileIndex = _HwPMStatisticsTaskCurrentFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 7),
    _HwPMStatisticsTaskCurrentFileIndex_Type()
)
hwPMStatisticsTaskCurrentFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskCurrentFileIndex.setStatus("current")
_HwPMStatisticsTaskRowStatus_Type = RowStatus
_HwPMStatisticsTaskRowStatus_Object = MibTableColumn
hwPMStatisticsTaskRowStatus = _HwPMStatisticsTaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 16),
    _HwPMStatisticsTaskRowStatus_Type()
)
hwPMStatisticsTaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskRowStatus.setStatus("current")


class _HwPMStatisticsTaskSampleInterval_Type(Integer32):
    """Custom type hwPMStatisticsTaskSampleInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              10,
              15,
              30,
              60)
        )
    )
    namedValues = NamedValues(
        *(("fifteen", 15),
          ("five", 5),
          ("one", 1),
          ("sixty", 60),
          ("ten", 10),
          ("thirty", 30),
          ("three", 3),
          ("two", 2))
    )


_HwPMStatisticsTaskSampleInterval_Type.__name__ = "Integer32"
_HwPMStatisticsTaskSampleInterval_Object = MibTableColumn
hwPMStatisticsTaskSampleInterval = _HwPMStatisticsTaskSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 17),
    _HwPMStatisticsTaskSampleInterval_Type()
)
hwPMStatisticsTaskSampleInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskSampleInterval.setStatus("current")


class _HwPMStatisticsUploadAutoName_Type(OctetString):
    """Custom type hwPMStatisticsUploadAutoName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPMStatisticsUploadAutoName_Type.__name__ = "OctetString"
_HwPMStatisticsUploadAutoName_Object = MibTableColumn
hwPMStatisticsUploadAutoName = _HwPMStatisticsUploadAutoName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 18),
    _HwPMStatisticsUploadAutoName_Type()
)
hwPMStatisticsUploadAutoName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsUploadAutoName.setStatus("current")


class _HwPMStatisticsTaskType_Type(Integer32):
    """Custom type hwPMStatisticsTaskType based on Integer32"""

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("monHistory", 7),
          ("monStatistics", 8),
          ("pmSdh", 6),
          ("pmStatistics", 3),
          ("sdhShort", 10))
    )


_HwPMStatisticsTaskType_Type.__name__ = "Integer32"
_HwPMStatisticsTaskType_Object = MibTableColumn
hwPMStatisticsTaskType = _HwPMStatisticsTaskType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 19),
    _HwPMStatisticsTaskType_Type()
)
hwPMStatisticsTaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskType.setStatus("current")


class _HwPMStatisticsHighPrecisionPeriod_Type(Unsigned32):
    """Custom type hwPMStatisticsHighPrecisionPeriod based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_HwPMStatisticsHighPrecisionPeriod_Type.__name__ = "Unsigned32"
_HwPMStatisticsHighPrecisionPeriod_Object = MibTableColumn
hwPMStatisticsHighPrecisionPeriod = _HwPMStatisticsHighPrecisionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 5, 1, 20),
    _HwPMStatisticsHighPrecisionPeriod_Type()
)
hwPMStatisticsHighPrecisionPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsHighPrecisionPeriod.setStatus("current")
_HwPMStatisticsTaskInstanceTable_Object = MibTable
hwPMStatisticsTaskInstanceTable = _HwPMStatisticsTaskInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 6)
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskInstanceTable.setStatus("current")
_HwPMStatisticsTaskInstanceEntry_Object = MibTableRow
hwPMStatisticsTaskInstanceEntry = _HwPMStatisticsTaskInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 6, 1)
)
hwPMStatisticsTaskInstanceEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskName"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskInstanceType"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskInstanceName"),
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskInstanceEntry.setStatus("current")
_HwPMStatisticsTaskInstanceType_Type = Unsigned32
_HwPMStatisticsTaskInstanceType_Object = MibTableColumn
hwPMStatisticsTaskInstanceType = _HwPMStatisticsTaskInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 6, 1, 1),
    _HwPMStatisticsTaskInstanceType_Type()
)
hwPMStatisticsTaskInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskInstanceType.setStatus("current")


class _HwPMStatisticsTaskInstanceName_Type(OctetString):
    """Custom type hwPMStatisticsTaskInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwPMStatisticsTaskInstanceName_Type.__name__ = "OctetString"
_HwPMStatisticsTaskInstanceName_Object = MibTableColumn
hwPMStatisticsTaskInstanceName = _HwPMStatisticsTaskInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 6, 1, 2),
    _HwPMStatisticsTaskInstanceName_Type()
)
hwPMStatisticsTaskInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskInstanceName.setStatus("current")
_HwPMStatisticsTaskInstanceRowStatus_Type = RowStatus
_HwPMStatisticsTaskInstanceRowStatus_Object = MibTableColumn
hwPMStatisticsTaskInstanceRowStatus = _HwPMStatisticsTaskInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 6, 1, 3),
    _HwPMStatisticsTaskInstanceRowStatus_Type()
)
hwPMStatisticsTaskInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskInstanceRowStatus.setStatus("current")
_HwPMStatisticsTaskIndicatorTable_Object = MibTable
hwPMStatisticsTaskIndicatorTable = _HwPMStatisticsTaskIndicatorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 7)
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskIndicatorTable.setStatus("current")
_HwPMStatisticsTaskIndicatorEntry_Object = MibTableRow
hwPMStatisticsTaskIndicatorEntry = _HwPMStatisticsTaskIndicatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 7, 1)
)
hwPMStatisticsTaskIndicatorEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskName"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskInstanceType"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicator"),
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskIndicatorEntry.setStatus("current")
_HwPMStatisticsTaskIndicator_Type = Unsigned32
_HwPMStatisticsTaskIndicator_Object = MibTableColumn
hwPMStatisticsTaskIndicator = _HwPMStatisticsTaskIndicator_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 7, 1, 1),
    _HwPMStatisticsTaskIndicator_Type()
)
hwPMStatisticsTaskIndicator.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskIndicator.setStatus("current")
_HwPMStatisticsTaskIndicatorRowStatus_Type = RowStatus
_HwPMStatisticsTaskIndicatorRowStatus_Object = MibTableColumn
hwPMStatisticsTaskIndicatorRowStatus = _HwPMStatisticsTaskIndicatorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 7, 1, 2),
    _HwPMStatisticsTaskIndicatorRowStatus_Type()
)
hwPMStatisticsTaskIndicatorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskIndicatorRowStatus.setStatus("current")
_HwPMStatisticsTaskThresholdRuleTable_Object = MibTable
hwPMStatisticsTaskThresholdRuleTable = _HwPMStatisticsTaskThresholdRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 8)
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskThresholdRuleTable.setStatus("current")
_HwPMStatisticsTaskThresholdRuleEntry_Object = MibTableRow
hwPMStatisticsTaskThresholdRuleEntry = _HwPMStatisticsTaskThresholdRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 8, 1)
)
hwPMStatisticsTaskThresholdRuleEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskName"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskInstanceType"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicator"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdType"),
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskThresholdRuleEntry.setStatus("current")


class _HwPMStatisticsTaskThresholdType_Type(Integer32):
    """Custom type hwPMStatisticsTaskThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hightrigger", 1),
          ("lowtrigger", 2))
    )


_HwPMStatisticsTaskThresholdType_Type.__name__ = "Integer32"
_HwPMStatisticsTaskThresholdType_Object = MibTableColumn
hwPMStatisticsTaskThresholdType = _HwPMStatisticsTaskThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 8, 1, 1),
    _HwPMStatisticsTaskThresholdType_Type()
)
hwPMStatisticsTaskThresholdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskThresholdType.setStatus("current")
_HwPMStatisticsTaskThresholdHighTriggerValue_Type = Unsigned32
_HwPMStatisticsTaskThresholdHighTriggerValue_Object = MibTableColumn
hwPMStatisticsTaskThresholdHighTriggerValue = _HwPMStatisticsTaskThresholdHighTriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 8, 1, 2),
    _HwPMStatisticsTaskThresholdHighTriggerValue_Type()
)
hwPMStatisticsTaskThresholdHighTriggerValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskThresholdHighTriggerValue.setStatus("current")
_HwPMStatisticsTaskThresholdLowTriggerValue_Type = Unsigned32
_HwPMStatisticsTaskThresholdLowTriggerValue_Object = MibTableColumn
hwPMStatisticsTaskThresholdLowTriggerValue = _HwPMStatisticsTaskThresholdLowTriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 8, 1, 3),
    _HwPMStatisticsTaskThresholdLowTriggerValue_Type()
)
hwPMStatisticsTaskThresholdLowTriggerValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskThresholdLowTriggerValue.setStatus("current")
_HwPMStatisticsTaskThresholdHighClearedValue_Type = Unsigned32
_HwPMStatisticsTaskThresholdHighClearedValue_Object = MibTableColumn
hwPMStatisticsTaskThresholdHighClearedValue = _HwPMStatisticsTaskThresholdHighClearedValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 8, 1, 4),
    _HwPMStatisticsTaskThresholdHighClearedValue_Type()
)
hwPMStatisticsTaskThresholdHighClearedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskThresholdHighClearedValue.setStatus("current")
_HwPMStatisticsTaskThresholdLowClearedValue_Type = Unsigned32
_HwPMStatisticsTaskThresholdLowClearedValue_Object = MibTableColumn
hwPMStatisticsTaskThresholdLowClearedValue = _HwPMStatisticsTaskThresholdLowClearedValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 8, 1, 5),
    _HwPMStatisticsTaskThresholdLowClearedValue_Type()
)
hwPMStatisticsTaskThresholdLowClearedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskThresholdLowClearedValue.setStatus("current")
_HwPMStatisticsTaskThresholdRuleRowStatus_Type = RowStatus
_HwPMStatisticsTaskThresholdRuleRowStatus_Object = MibTableColumn
hwPMStatisticsTaskThresholdRuleRowStatus = _HwPMStatisticsTaskThresholdRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 8, 1, 50),
    _HwPMStatisticsTaskThresholdRuleRowStatus_Type()
)
hwPMStatisticsTaskThresholdRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskThresholdRuleRowStatus.setStatus("current")
_HwPMStatisticsTaskThresholdEvent_ObjectIdentity = ObjectIdentity
hwPMStatisticsTaskThresholdEvent = _HwPMStatisticsTaskThresholdEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 9)
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskThresholdEvent.setStatus("current")
_HwPMStatisticsTaskIndicateLowValue_Type = Unsigned32
_HwPMStatisticsTaskIndicateLowValue_Object = MibScalar
hwPMStatisticsTaskIndicateLowValue = _HwPMStatisticsTaskIndicateLowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 10),
    _HwPMStatisticsTaskIndicateLowValue_Type()
)
hwPMStatisticsTaskIndicateLowValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskIndicateLowValue.setStatus("current")
_HwPMStatisticsTaskIndicateHighValue_Type = Unsigned32
_HwPMStatisticsTaskIndicateHighValue_Object = MibScalar
hwPMStatisticsTaskIndicateHighValue = _HwPMStatisticsTaskIndicateHighValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 11),
    _HwPMStatisticsTaskIndicateHighValue_Type()
)
hwPMStatisticsTaskIndicateHighValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskIndicateHighValue.setStatus("current")
_HwPMStatisticsTaskFileTable_Object = MibTable
hwPMStatisticsTaskFileTable = _HwPMStatisticsTaskFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 12)
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskFileTable.setStatus("current")
_HwPMStatisticsTaskFileEntry_Object = MibTableRow
hwPMStatisticsTaskFileEntry = _HwPMStatisticsTaskFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 12, 1)
)
hwPMStatisticsTaskFileEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskName"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskFileIndex"),
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskFileEntry.setStatus("current")
_HwPMStatisticsTaskFileIndex_Type = Unsigned32
_HwPMStatisticsTaskFileIndex_Object = MibTableColumn
hwPMStatisticsTaskFileIndex = _HwPMStatisticsTaskFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 12, 1, 1),
    _HwPMStatisticsTaskFileIndex_Type()
)
hwPMStatisticsTaskFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskFileIndex.setStatus("current")
_HwPMStatisticsTaskFileName_Type = OctetString
_HwPMStatisticsTaskFileName_Object = MibTableColumn
hwPMStatisticsTaskFileName = _HwPMStatisticsTaskFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 12, 1, 2),
    _HwPMStatisticsTaskFileName_Type()
)
hwPMStatisticsTaskFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMStatisticsTaskFileName.setStatus("current")
_HwPMStatisticsTraps_ObjectIdentity = ObjectIdentity
hwPMStatisticsTraps = _HwPMStatisticsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 13)
)
if mibBuilder.loadTexts:
    hwPMStatisticsTraps.setStatus("current")
_HwPMFileUploadMgmtInstances_ObjectIdentity = ObjectIdentity
hwPMFileUploadMgmtInstances = _HwPMFileUploadMgmtInstances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2)
)
_HwPMServerTable_Object = MibTable
hwPMServerTable = _HwPMServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1)
)
if mibBuilder.loadTexts:
    hwPMServerTable.setStatus("current")
_HwPMServerEntry_Object = MibTableRow
hwPMServerEntry = _HwPMServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1)
)
hwPMServerEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMServerName"),
)
if mibBuilder.loadTexts:
    hwPMServerEntry.setStatus("current")


class _HwPMServerName_Type(OctetString):
    """Custom type hwPMServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwPMServerName_Type.__name__ = "OctetString"
_HwPMServerName_Object = MibTableColumn
hwPMServerName = _HwPMServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 1),
    _HwPMServerName_Type()
)
hwPMServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMServerName.setStatus("current")


class _HwPMServerSrcAddrType_Type(InetAddressType):
    """Custom type hwPMServerSrcAddrType based on InetAddressType"""


_HwPMServerSrcAddrType_Object = MibTableColumn
hwPMServerSrcAddrType = _HwPMServerSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 2),
    _HwPMServerSrcAddrType_Type()
)
hwPMServerSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMServerSrcAddrType.setStatus("current")
_HwPMServerSrcAddr_Type = InetAddress
_HwPMServerSrcAddr_Object = MibTableColumn
hwPMServerSrcAddr = _HwPMServerSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 3),
    _HwPMServerSrcAddr_Type()
)
hwPMServerSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMServerSrcAddr.setStatus("current")


class _HwPMServerVpnName_Type(OctetString):
    """Custom type hwPMServerVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPMServerVpnName_Type.__name__ = "OctetString"
_HwPMServerVpnName_Object = MibTableColumn
hwPMServerVpnName = _HwPMServerVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 4),
    _HwPMServerVpnName_Type()
)
hwPMServerVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMServerVpnName.setStatus("current")


class _HwPMServerHostAddrType_Type(InetAddressType):
    """Custom type hwPMServerHostAddrType based on InetAddressType"""


_HwPMServerHostAddrType_Object = MibTableColumn
hwPMServerHostAddrType = _HwPMServerHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 5),
    _HwPMServerHostAddrType_Type()
)
hwPMServerHostAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMServerHostAddrType.setStatus("current")
_HwPMServerHostAddr_Type = InetAddress
_HwPMServerHostAddr_Object = MibTableColumn
hwPMServerHostAddr = _HwPMServerHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 6),
    _HwPMServerHostAddr_Type()
)
hwPMServerHostAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMServerHostAddr.setStatus("current")


class _HwPMServerPort_Type(Integer32):
    """Custom type hwPMServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwPMServerPort_Type.__name__ = "Integer32"
_HwPMServerPort_Object = MibTableColumn
hwPMServerPort = _HwPMServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 7),
    _HwPMServerPort_Type()
)
hwPMServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMServerPort.setStatus("current")


class _HwPMServerUserName_Type(OctetString):
    """Custom type hwPMServerUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwPMServerUserName_Type.__name__ = "OctetString"
_HwPMServerUserName_Object = MibTableColumn
hwPMServerUserName = _HwPMServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 8),
    _HwPMServerUserName_Type()
)
hwPMServerUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMServerUserName.setStatus("current")


class _HwPMServerPassword_Type(OctetString):
    """Custom type hwPMServerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwPMServerPassword_Type.__name__ = "OctetString"
_HwPMServerPassword_Object = MibTableColumn
hwPMServerPassword = _HwPMServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 9),
    _HwPMServerPassword_Type()
)
hwPMServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMServerPassword.setStatus("current")


class _HwPMServerSrcIfName_Type(OctetString):
    """Custom type hwPMServerSrcIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwPMServerSrcIfName_Type.__name__ = "OctetString"
_HwPMServerSrcIfName_Object = MibTableColumn
hwPMServerSrcIfName = _HwPMServerSrcIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 10),
    _HwPMServerSrcIfName_Type()
)
hwPMServerSrcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMServerSrcIfName.setStatus("current")


class _HwPMServerRetryTimes_Type(Unsigned32):
    """Custom type hwPMServerRetryTimes based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HwPMServerRetryTimes_Type.__name__ = "Unsigned32"
_HwPMServerRetryTimes_Object = MibTableColumn
hwPMServerRetryTimes = _HwPMServerRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 11),
    _HwPMServerRetryTimes_Type()
)
hwPMServerRetryTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMServerRetryTimes.setStatus("current")


class _HwPMServerDestPath_Type(OctetString):
    """Custom type hwPMServerDestPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwPMServerDestPath_Type.__name__ = "OctetString"
_HwPMServerDestPath_Object = MibTableColumn
hwPMServerDestPath = _HwPMServerDestPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 12),
    _HwPMServerDestPath_Type()
)
hwPMServerDestPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMServerDestPath.setStatus("current")


class _HwPMServerTransferProtocol_Type(Integer32):
    """Custom type hwPMServerTransferProtocol based on Integer32"""
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


_HwPMServerTransferProtocol_Type.__name__ = "Integer32"
_HwPMServerTransferProtocol_Object = MibTableColumn
hwPMServerTransferProtocol = _HwPMServerTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 13),
    _HwPMServerTransferProtocol_Type()
)
hwPMServerTransferProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMServerTransferProtocol.setStatus("current")
_HwPMServerRowStatus_Type = RowStatus
_HwPMServerRowStatus_Object = MibTableColumn
hwPMServerRowStatus = _HwPMServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 14),
    _HwPMServerRowStatus_Type()
)
hwPMServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMServerRowStatus.setStatus("current")


class _HwPMServerVpnType_Type(Integer32):
    """Custom type hwPMServerVpnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("managevpn", 1),
          ("none", 0),
          ("vpninstance", 2))
    )


_HwPMServerVpnType_Type.__name__ = "Integer32"
_HwPMServerVpnType_Object = MibTableColumn
hwPMServerVpnType = _HwPMServerVpnType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 1, 1, 15),
    _HwPMServerVpnType_Type()
)
hwPMServerVpnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMServerVpnType.setStatus("current")
_HwPMFileUploadCfgTable_Object = MibTable
hwPMFileUploadCfgTable = _HwPMFileUploadCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 2)
)
if mibBuilder.loadTexts:
    hwPMFileUploadCfgTable.setStatus("current")
_HwPMFileUploadCfgEntry_Object = MibTableRow
hwPMFileUploadCfgEntry = _HwPMFileUploadCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 2, 1)
)
hwPMFileUploadCfgEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMFileUploadRequestName"),
)
if mibBuilder.loadTexts:
    hwPMFileUploadCfgEntry.setStatus("current")


class _HwPMFileUploadRequestName_Type(OctetString):
    """Custom type hwPMFileUploadRequestName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwPMFileUploadRequestName_Type.__name__ = "OctetString"
_HwPMFileUploadRequestName_Object = MibTableColumn
hwPMFileUploadRequestName = _HwPMFileUploadRequestName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 2, 1, 1),
    _HwPMFileUploadRequestName_Type()
)
hwPMFileUploadRequestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMFileUploadRequestName.setStatus("current")


class _HwPMFileUploadServerName_Type(OctetString):
    """Custom type hwPMFileUploadServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwPMFileUploadServerName_Type.__name__ = "OctetString"
_HwPMFileUploadServerName_Object = MibTableColumn
hwPMFileUploadServerName = _HwPMFileUploadServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 2, 1, 2),
    _HwPMFileUploadServerName_Type()
)
hwPMFileUploadServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMFileUploadServerName.setStatus("current")
_HwPMFileUploadCfgRowStatus_Type = RowStatus
_HwPMFileUploadCfgRowStatus_Object = MibTableColumn
hwPMFileUploadCfgRowStatus = _HwPMFileUploadCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 2, 1, 3),
    _HwPMFileUploadCfgRowStatus_Type()
)
hwPMFileUploadCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMFileUploadCfgRowStatus.setStatus("current")
_HwPMFileUploadMgmtTable_Object = MibTable
hwPMFileUploadMgmtTable = _HwPMFileUploadMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 3)
)
if mibBuilder.loadTexts:
    hwPMFileUploadMgmtTable.setStatus("current")
_HwPMFileUploadMgmtEntry_Object = MibTableRow
hwPMFileUploadMgmtEntry = _HwPMFileUploadMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 3, 1)
)
hwPMFileUploadMgmtEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMFileUploadRequestName"),
)
if mibBuilder.loadTexts:
    hwPMFileUploadMgmtEntry.setStatus("current")


class _HwPMFileUploadFileList_Type(OctetString):
    """Custom type hwPMFileUploadFileList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 543),
    )


_HwPMFileUploadFileList_Type.__name__ = "OctetString"
_HwPMFileUploadFileList_Object = MibTableColumn
hwPMFileUploadFileList = _HwPMFileUploadFileList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 3, 1, 3),
    _HwPMFileUploadFileList_Type()
)
hwPMFileUploadFileList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPMFileUploadFileList.setStatus("current")


class _HwPMFileUploadStatus_Type(Integer32):
    """Custom type hwPMFileUploadStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("authenticateFailed", 7),
          ("failed", 10),
          ("fileOpenFail", 4),
          ("fileReadFailed", 8),
          ("fileWriteFailed", 9),
          ("init", 1),
          ("linkFailed", 6),
          ("running", 2),
          ("success", 3),
          ("unreachableServerIp", 5))
    )


_HwPMFileUploadStatus_Type.__name__ = "Integer32"
_HwPMFileUploadStatus_Object = MibTableColumn
hwPMFileUploadStatus = _HwPMFileUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 2, 3, 1, 4),
    _HwPMFileUploadStatus_Type()
)
hwPMFileUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMFileUploadStatus.setStatus("current")
_HwPMDataInstances_ObjectIdentity = ObjectIdentity
hwPMDataInstances = _HwPMDataInstances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4)
)
_HwPMHistoryDataTable_Object = MibTable
hwPMHistoryDataTable = _HwPMHistoryDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 1)
)
if mibBuilder.loadTexts:
    hwPMHistoryDataTable.setStatus("current")
_HwPMHistoryDataEntry_Object = MibTableRow
hwPMHistoryDataEntry = _HwPMHistoryDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 1, 1)
)
hwPMHistoryDataEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskName"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMHistoryDataInstanceType"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMHistoryDataInstanceName"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMHistoryDataIndicatorID"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMHistoryDataIntervalIndex"),
)
if mibBuilder.loadTexts:
    hwPMHistoryDataEntry.setStatus("current")
_HwPMHistoryDataInstanceType_Type = Unsigned32
_HwPMHistoryDataInstanceType_Object = MibTableColumn
hwPMHistoryDataInstanceType = _HwPMHistoryDataInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 1, 1, 1),
    _HwPMHistoryDataInstanceType_Type()
)
hwPMHistoryDataInstanceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPMHistoryDataInstanceType.setStatus("current")
_HwPMHistoryDataInstanceName_Type = OctetString
_HwPMHistoryDataInstanceName_Object = MibTableColumn
hwPMHistoryDataInstanceName = _HwPMHistoryDataInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 1, 1, 2),
    _HwPMHistoryDataInstanceName_Type()
)
hwPMHistoryDataInstanceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPMHistoryDataInstanceName.setStatus("current")
_HwPMHistoryDataIndicatorID_Type = Unsigned32
_HwPMHistoryDataIndicatorID_Object = MibTableColumn
hwPMHistoryDataIndicatorID = _HwPMHistoryDataIndicatorID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 1, 1, 3),
    _HwPMHistoryDataIndicatorID_Type()
)
hwPMHistoryDataIndicatorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPMHistoryDataIndicatorID.setStatus("current")


class _HwPMHistoryDataIntervalIndex_Type(Integer32):
    """Custom type hwPMHistoryDataIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwPMHistoryDataIntervalIndex_Type.__name__ = "Integer32"
_HwPMHistoryDataIntervalIndex_Object = MibTableColumn
hwPMHistoryDataIntervalIndex = _HwPMHistoryDataIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 1, 1, 4),
    _HwPMHistoryDataIntervalIndex_Type()
)
hwPMHistoryDataIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPMHistoryDataIntervalIndex.setStatus("current")
_HwPMHistoryDataHighValue_Type = Unsigned32
_HwPMHistoryDataHighValue_Object = MibTableColumn
hwPMHistoryDataHighValue = _HwPMHistoryDataHighValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 1, 1, 5),
    _HwPMHistoryDataHighValue_Type()
)
hwPMHistoryDataHighValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMHistoryDataHighValue.setStatus("current")
_HwPMHistoryDataLowValue_Type = Unsigned32
_HwPMHistoryDataLowValue_Object = MibTableColumn
hwPMHistoryDataLowValue = _HwPMHistoryDataLowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 1, 1, 6),
    _HwPMHistoryDataLowValue_Type()
)
hwPMHistoryDataLowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMHistoryDataLowValue.setStatus("current")


class _HwPMHistoryDataValidFlag_Type(Integer32):
    """Custom type hwPMHistoryDataValidFlag based on Integer32"""
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
        *(("incredible", 3),
          ("init", 1),
          ("measureNotConfigured", 4),
          ("valid", 2))
    )


_HwPMHistoryDataValidFlag_Type.__name__ = "Integer32"
_HwPMHistoryDataValidFlag_Object = MibTableColumn
hwPMHistoryDataValidFlag = _HwPMHistoryDataValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 1, 1, 7),
    _HwPMHistoryDataValidFlag_Type()
)
hwPMHistoryDataValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMHistoryDataValidFlag.setStatus("current")
_HwPMHistoryDateAndTime_Type = DateAndTime
_HwPMHistoryDateAndTime_Object = MibTableColumn
hwPMHistoryDateAndTime = _HwPMHistoryDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 1, 1, 8),
    _HwPMHistoryDateAndTime_Type()
)
hwPMHistoryDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMHistoryDateAndTime.setStatus("current")
_HwPMCurrentDataTable_Object = MibTable
hwPMCurrentDataTable = _HwPMCurrentDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 2)
)
if mibBuilder.loadTexts:
    hwPMCurrentDataTable.setStatus("current")
_HwPMCurrentDataEntry_Object = MibTableRow
hwPMCurrentDataEntry = _HwPMCurrentDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 2, 1)
)
hwPMCurrentDataEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskName"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMCurrentDataInstanceType"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMCurrentDataInstanceName"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMCurrentDataIndicatorID"),
)
if mibBuilder.loadTexts:
    hwPMCurrentDataEntry.setStatus("current")
_HwPMCurrentDataInstanceType_Type = Unsigned32
_HwPMCurrentDataInstanceType_Object = MibTableColumn
hwPMCurrentDataInstanceType = _HwPMCurrentDataInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 2, 1, 1),
    _HwPMCurrentDataInstanceType_Type()
)
hwPMCurrentDataInstanceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPMCurrentDataInstanceType.setStatus("current")
_HwPMCurrentDataInstanceName_Type = OctetString
_HwPMCurrentDataInstanceName_Object = MibTableColumn
hwPMCurrentDataInstanceName = _HwPMCurrentDataInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 2, 1, 2),
    _HwPMCurrentDataInstanceName_Type()
)
hwPMCurrentDataInstanceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPMCurrentDataInstanceName.setStatus("current")
_HwPMCurrentDataIndicatorID_Type = Unsigned32
_HwPMCurrentDataIndicatorID_Object = MibTableColumn
hwPMCurrentDataIndicatorID = _HwPMCurrentDataIndicatorID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 2, 1, 3),
    _HwPMCurrentDataIndicatorID_Type()
)
hwPMCurrentDataIndicatorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPMCurrentDataIndicatorID.setStatus("current")
_HwPMCurrentDataHighValue_Type = Unsigned32
_HwPMCurrentDataHighValue_Object = MibTableColumn
hwPMCurrentDataHighValue = _HwPMCurrentDataHighValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 2, 1, 5),
    _HwPMCurrentDataHighValue_Type()
)
hwPMCurrentDataHighValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMCurrentDataHighValue.setStatus("current")
_HwPMCurrentDataLowValue_Type = Unsigned32
_HwPMCurrentDataLowValue_Object = MibTableColumn
hwPMCurrentDataLowValue = _HwPMCurrentDataLowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 2, 1, 6),
    _HwPMCurrentDataLowValue_Type()
)
hwPMCurrentDataLowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMCurrentDataLowValue.setStatus("current")


class _HwPMCurrentDataValidFlag_Type(Integer32):
    """Custom type hwPMCurrentDataValidFlag based on Integer32"""
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
        *(("incredible", 3),
          ("init", 1),
          ("measureNotConfigured", 4),
          ("valid", 2))
    )


_HwPMCurrentDataValidFlag_Type.__name__ = "Integer32"
_HwPMCurrentDataValidFlag_Object = MibTableColumn
hwPMCurrentDataValidFlag = _HwPMCurrentDataValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 2, 1, 7),
    _HwPMCurrentDataValidFlag_Type()
)
hwPMCurrentDataValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMCurrentDataValidFlag.setStatus("current")
_HwPMCurrentDateAndTime_Type = DateAndTime
_HwPMCurrentDateAndTime_Object = MibTableColumn
hwPMCurrentDateAndTime = _HwPMCurrentDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 2, 1, 8),
    _HwPMCurrentDateAndTime_Type()
)
hwPMCurrentDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMCurrentDateAndTime.setStatus("current")
_HwPMResetCurrentDataTable_Object = MibTable
hwPMResetCurrentDataTable = _HwPMResetCurrentDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 3)
)
if mibBuilder.loadTexts:
    hwPMResetCurrentDataTable.setStatus("current")
_HwPMResetCurrentDataEntry_Object = MibTableRow
hwPMResetCurrentDataEntry = _HwPMResetCurrentDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 3, 1)
)
hwPMResetCurrentDataEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskName"),
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMResetCurrentDataInstanceType"),
)
if mibBuilder.loadTexts:
    hwPMResetCurrentDataEntry.setStatus("current")
_HwPMResetCurrentDataInstanceType_Type = Unsigned32
_HwPMResetCurrentDataInstanceType_Object = MibTableColumn
hwPMResetCurrentDataInstanceType = _HwPMResetCurrentDataInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 3, 1, 1),
    _HwPMResetCurrentDataInstanceType_Type()
)
hwPMResetCurrentDataInstanceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPMResetCurrentDataInstanceType.setStatus("current")
_HwPMResetCurrentDataInstanceName_Type = OctetString
_HwPMResetCurrentDataInstanceName_Object = MibTableColumn
hwPMResetCurrentDataInstanceName = _HwPMResetCurrentDataInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 3, 1, 2),
    _HwPMResetCurrentDataInstanceName_Type()
)
hwPMResetCurrentDataInstanceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPMResetCurrentDataInstanceName.setStatus("current")
_HwPMResetCurrentDataIndicatorID_Type = Unsigned32
_HwPMResetCurrentDataIndicatorID_Object = MibTableColumn
hwPMResetCurrentDataIndicatorID = _HwPMResetCurrentDataIndicatorID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 4, 3, 1, 3),
    _HwPMResetCurrentDataIndicatorID_Type()
)
hwPMResetCurrentDataIndicatorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPMResetCurrentDataIndicatorID.setStatus("current")
_HwPMGlobalInstances_ObjectIdentity = ObjectIdentity
hwPMGlobalInstances = _HwPMGlobalInstances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5)
)
_HwPMIntervalTypeTable_Object = MibTable
hwPMIntervalTypeTable = _HwPMIntervalTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 1)
)
if mibBuilder.loadTexts:
    hwPMIntervalTypeTable.setStatus("current")
_HwPMIntervalTypeEntry_Object = MibTableRow
hwPMIntervalTypeEntry = _HwPMIntervalTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 1, 1)
)
hwPMIntervalTypeEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMIntervalType"),
)
if mibBuilder.loadTexts:
    hwPMIntervalTypeEntry.setStatus("current")
_HwPMIntervalType_Type = Unsigned32
_HwPMIntervalType_Object = MibTableColumn
hwPMIntervalType = _HwPMIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 1, 1, 1),
    _HwPMIntervalType_Type()
)
hwPMIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPMIntervalType.setStatus("current")
_HwPMIntervalTypeName_Type = OctetString
_HwPMIntervalTypeName_Object = MibTableColumn
hwPMIntervalTypeName = _HwPMIntervalTypeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 1, 1, 2),
    _HwPMIntervalTypeName_Type()
)
hwPMIntervalTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMIntervalTypeName.setStatus("current")


class _HwPMIntervalTypeInterval_Type(Integer32):
    """Custom type hwPMIntervalTypeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              30,
              60,
              1440)
        )
    )
    namedValues = NamedValues(
        *(("fifteen", 15),
          ("five", 5),
          ("sixty", 60),
          ("ten", 10),
          ("thirty", 30),
          ("twentyfourhours", 1440))
    )


_HwPMIntervalTypeInterval_Type.__name__ = "Integer32"
_HwPMIntervalTypeInterval_Object = MibTableColumn
hwPMIntervalTypeInterval = _HwPMIntervalTypeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 1, 1, 3),
    _HwPMIntervalTypeInterval_Type()
)
hwPMIntervalTypeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMIntervalTypeInterval.setStatus("current")


class _HwPMIntervalTypeHistorynum_Type(Unsigned32):
    """Custom type hwPMIntervalTypeHistorynum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwPMIntervalTypeHistorynum_Type.__name__ = "Unsigned32"
_HwPMIntervalTypeHistorynum_Object = MibTableColumn
hwPMIntervalTypeHistorynum = _HwPMIntervalTypeHistorynum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 1, 1, 4),
    _HwPMIntervalTypeHistorynum_Type()
)
hwPMIntervalTypeHistorynum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMIntervalTypeHistorynum.setStatus("current")
_HwPMIntervalTypeDelayRange_Type = Unsigned32
_HwPMIntervalTypeDelayRange_Object = MibTableColumn
hwPMIntervalTypeDelayRange = _HwPMIntervalTypeDelayRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 1, 1, 5),
    _HwPMIntervalTypeDelayRange_Type()
)
hwPMIntervalTypeDelayRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMIntervalTypeDelayRange.setStatus("current")
if mibBuilder.loadTexts:
    hwPMIntervalTypeDelayRange.setUnits("second")
_HwPMIntervalTypeSampleInterval_Type = Unsigned32
_HwPMIntervalTypeSampleInterval_Object = MibTableColumn
hwPMIntervalTypeSampleInterval = _HwPMIntervalTypeSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 1, 1, 6),
    _HwPMIntervalTypeSampleInterval_Type()
)
hwPMIntervalTypeSampleInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMIntervalTypeSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwPMIntervalTypeSampleInterval.setUnits("second")
_HwPMInstanceTypeTable_Object = MibTable
hwPMInstanceTypeTable = _HwPMInstanceTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 2)
)
if mibBuilder.loadTexts:
    hwPMInstanceTypeTable.setStatus("current")
_HwPMInstanceTypeEntry_Object = MibTableRow
hwPMInstanceTypeEntry = _HwPMInstanceTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 2, 1)
)
hwPMInstanceTypeEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMInstanceTypeID"),
)
if mibBuilder.loadTexts:
    hwPMInstanceTypeEntry.setStatus("current")
_HwPMInstanceTypeID_Type = Unsigned32
_HwPMInstanceTypeID_Object = MibTableColumn
hwPMInstanceTypeID = _HwPMInstanceTypeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 2, 1, 1),
    _HwPMInstanceTypeID_Type()
)
hwPMInstanceTypeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPMInstanceTypeID.setStatus("current")
_HwPMInstanceTypeName_Type = OctetString
_HwPMInstanceTypeName_Object = MibTableColumn
hwPMInstanceTypeName = _HwPMInstanceTypeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 2, 1, 2),
    _HwPMInstanceTypeName_Type()
)
hwPMInstanceTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMInstanceTypeName.setStatus("current")
_HwPMIndicatorTable_Object = MibTable
hwPMIndicatorTable = _HwPMIndicatorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 3)
)
if mibBuilder.loadTexts:
    hwPMIndicatorTable.setStatus("current")
_HwPMIndicatorEntry_Object = MibTableRow
hwPMIndicatorEntry = _HwPMIndicatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 3, 1)
)
hwPMIndicatorEntry.setIndexNames(
    (0, "HUAWEI-PERFMGMT-MIB", "hwPMIndicatorID"),
)
if mibBuilder.loadTexts:
    hwPMIndicatorEntry.setStatus("current")
_HwPMIndicatorID_Type = Unsigned32
_HwPMIndicatorID_Object = MibTableColumn
hwPMIndicatorID = _HwPMIndicatorID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 3, 1, 1),
    _HwPMIndicatorID_Type()
)
hwPMIndicatorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPMIndicatorID.setStatus("current")
_HwPMIndicatorName_Type = OctetString
_HwPMIndicatorName_Object = MibTableColumn
hwPMIndicatorName = _HwPMIndicatorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 3, 1, 2),
    _HwPMIndicatorName_Type()
)
hwPMIndicatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMIndicatorName.setStatus("current")


class _HwPMIndicatorType_Type(Integer32):
    """Custom type hwPMIndicatorType based on Integer32"""
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
        *(("avg", 5),
          ("delta", 7),
          ("es", 6),
          ("increase", 1),
          ("max", 3),
          ("measure", 2),
          ("min", 4))
    )


_HwPMIndicatorType_Type.__name__ = "Integer32"
_HwPMIndicatorType_Object = MibTableColumn
hwPMIndicatorType = _HwPMIndicatorType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 3, 1, 3),
    _HwPMIndicatorType_Type()
)
hwPMIndicatorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMIndicatorType.setStatus("current")


class _HwPMIndicatorCounterType_Type(Integer32):
    """Custom type hwPMIndicatorCounterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("counter32", 1),
          ("counter64", 2))
    )


_HwPMIndicatorCounterType_Type.__name__ = "Integer32"
_HwPMIndicatorCounterType_Object = MibTableColumn
hwPMIndicatorCounterType = _HwPMIndicatorCounterType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 5, 3, 1, 4),
    _HwPMIndicatorCounterType_Type()
)
hwPMIndicatorCounterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPMIndicatorCounterType.setStatus("current")
_HwPMConformance_ObjectIdentity = ObjectIdentity
hwPMConformance = _HwPMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6)
)
_HwPMCompliances_ObjectIdentity = ObjectIdentity
hwPMCompliances = _HwPMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 1)
)
_HwPMGroup_ObjectIdentity = ObjectIdentity
hwPMGroup = _HwPMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2)
)

# Managed Objects groups

hwPMMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2, 1)
)
hwPMMIBGroup.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsEnable"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsMaxFilesPerTask"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsMaxTasks"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsCurrentTasks"))
)
if mibBuilder.loadTexts:
    hwPMMIBGroup.setStatus("current")

hwPMTaskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2, 2)
)
hwPMTaskGroup.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskFileFormat"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsRecordFileEnable"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsThresholdEnable"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskPeriod"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskTransferPeriod"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskRowStatus"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskSampleInterval"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicator"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicatorRowStatus"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskCurrentFileIndex"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsUploadAutoName"))
)
if mibBuilder.loadTexts:
    hwPMTaskGroup.setStatus("current")

hwPMTaskInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2, 3)
)
hwPMTaskInstanceGroup.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskInstanceType"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskInstanceName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskInstanceRowStatus"))
)
if mibBuilder.loadTexts:
    hwPMTaskInstanceGroup.setStatus("current")

hwPMTaskThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2, 4)
)
hwPMTaskThresholdGroup.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdType"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdHighTriggerValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdLowTriggerValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdHighClearedValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdLowClearedValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdRuleRowStatus"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicateLowValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicateHighValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdRuleRowStatus"))
)
if mibBuilder.loadTexts:
    hwPMTaskThresholdGroup.setStatus("current")

hwPMTaskFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2, 5)
)
hwPMTaskFileGroup.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskFileIndex"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskFileName"))
)
if mibBuilder.loadTexts:
    hwPMTaskFileGroup.setStatus("current")

hwPMFileUploadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2, 6)
)
hwPMFileUploadGroup.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMFileUploadRequestName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMFileUploadServerName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMFileUploadFileList"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMFileUploadStatus"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMFileUploadCfgRowStatus"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerSrcAddrType"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerSrcAddr"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerVpnName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerHostAddr"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerHostAddrType"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerPort"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerUserName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerPassword"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerSrcIfName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerRetryTimes"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerTransferProtocol"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerDestPath"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerRowStatus"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMServerVpnType"))
)
if mibBuilder.loadTexts:
    hwPMFileUploadGroup.setStatus("current")

hwPMDataInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2, 7)
)
hwPMDataInstanceGroup.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMHistoryDataHighValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMHistoryDataLowValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMHistoryDataValidFlag"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMHistoryDateAndTime"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMCurrentDataHighValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMCurrentDataLowValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMCurrentDataValidFlag"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMCurrentDateAndTime"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMResetCurrentDataIndicatorID"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMResetCurrentDataInstanceName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMResetCurrentDataInstanceType"))
)
if mibBuilder.loadTexts:
    hwPMDataInstanceGroup.setStatus("current")

hwPMIntervalTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2, 8)
)
hwPMIntervalTypeGroup.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMIntervalTypeName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMIntervalTypeInterval"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMIntervalTypeHistorynum"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMIntervalTypeDelayRange"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMIntervalTypeSampleInterval"))
)
if mibBuilder.loadTexts:
    hwPMIntervalTypeGroup.setStatus("current")

hwPMInstanceTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2, 9)
)
hwPMInstanceTypeGroup.setObjects(
    ("HUAWEI-PERFMGMT-MIB", "hwPMInstanceTypeName")
)
if mibBuilder.loadTexts:
    hwPMInstanceTypeGroup.setStatus("current")

hwPMIndicatorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2, 10)
)
hwPMIndicatorGroup.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMIndicatorName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMIndicatorType"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMIndicatorCounterType"))
)
if mibBuilder.loadTexts:
    hwPMIndicatorGroup.setStatus("current")


# Notification objects

hwPMStatisticsTaskThresholdTriggerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 9, 1)
)
hwPMStatisticsTaskThresholdTriggerAlarm.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskPeriod"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskInstanceName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicator"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdType"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdHighTriggerValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdLowTriggerValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicateHighValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicateLowValue"))
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskThresholdTriggerAlarm.setStatus(
        "current"
    )

hwPMStatisticsTaskThresholdClearAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 9, 2)
)
hwPMStatisticsTaskThresholdClearAlarm.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskPeriod"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskInstanceName"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicator"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdType"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdHighClearedValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdLowClearedValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicateHighValue"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskIndicateLowValue"))
)
if mibBuilder.loadTexts:
    hwPMStatisticsTaskThresholdClearAlarm.setStatus(
        "current"
    )

hwPMMeasureExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 1, 13, 1)
)
if mibBuilder.loadTexts:
    hwPMMeasureExceed.setStatus(
        "current"
    )


# Notifications groups

hwPMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 2, 11)
)
hwPMNotificationGroup.setObjects(
      *(("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdTriggerAlarm"),
        ("HUAWEI-PERFMGMT-MIB", "hwPMStatisticsTaskThresholdClearAlarm"))
)
if mibBuilder.loadTexts:
    hwPMNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwPMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 190, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwPMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PERFMGMT-MIB",
    **{"hwPerfMgmt": hwPerfMgmt,
       "hwPMStatisticsMIBInstances": hwPMStatisticsMIBInstances,
       "hwPMStatisticsEnable": hwPMStatisticsEnable,
       "hwPMStatisticsMaxFilesPerTask": hwPMStatisticsMaxFilesPerTask,
       "hwPMStatisticsMaxTasks": hwPMStatisticsMaxTasks,
       "hwPMStatisticsCurrentTasks": hwPMStatisticsCurrentTasks,
       "hwPMStatisticsTaskTable": hwPMStatisticsTaskTable,
       "hwPMStatisticsTaskEntry": hwPMStatisticsTaskEntry,
       "hwPMStatisticsTaskName": hwPMStatisticsTaskName,
       "hwPMStatisticsTaskFileFormat": hwPMStatisticsTaskFileFormat,
       "hwPMStatisticsRecordFileEnable": hwPMStatisticsRecordFileEnable,
       "hwPMStatisticsThresholdEnable": hwPMStatisticsThresholdEnable,
       "hwPMStatisticsTaskPeriod": hwPMStatisticsTaskPeriod,
       "hwPMStatisticsTaskTransferPeriod": hwPMStatisticsTaskTransferPeriod,
       "hwPMStatisticsTaskCurrentFileIndex": hwPMStatisticsTaskCurrentFileIndex,
       "hwPMStatisticsTaskRowStatus": hwPMStatisticsTaskRowStatus,
       "hwPMStatisticsTaskSampleInterval": hwPMStatisticsTaskSampleInterval,
       "hwPMStatisticsUploadAutoName": hwPMStatisticsUploadAutoName,
       "hwPMStatisticsTaskType": hwPMStatisticsTaskType,
       "hwPMStatisticsHighPrecisionPeriod": hwPMStatisticsHighPrecisionPeriod,
       "hwPMStatisticsTaskInstanceTable": hwPMStatisticsTaskInstanceTable,
       "hwPMStatisticsTaskInstanceEntry": hwPMStatisticsTaskInstanceEntry,
       "hwPMStatisticsTaskInstanceType": hwPMStatisticsTaskInstanceType,
       "hwPMStatisticsTaskInstanceName": hwPMStatisticsTaskInstanceName,
       "hwPMStatisticsTaskInstanceRowStatus": hwPMStatisticsTaskInstanceRowStatus,
       "hwPMStatisticsTaskIndicatorTable": hwPMStatisticsTaskIndicatorTable,
       "hwPMStatisticsTaskIndicatorEntry": hwPMStatisticsTaskIndicatorEntry,
       "hwPMStatisticsTaskIndicator": hwPMStatisticsTaskIndicator,
       "hwPMStatisticsTaskIndicatorRowStatus": hwPMStatisticsTaskIndicatorRowStatus,
       "hwPMStatisticsTaskThresholdRuleTable": hwPMStatisticsTaskThresholdRuleTable,
       "hwPMStatisticsTaskThresholdRuleEntry": hwPMStatisticsTaskThresholdRuleEntry,
       "hwPMStatisticsTaskThresholdType": hwPMStatisticsTaskThresholdType,
       "hwPMStatisticsTaskThresholdHighTriggerValue": hwPMStatisticsTaskThresholdHighTriggerValue,
       "hwPMStatisticsTaskThresholdLowTriggerValue": hwPMStatisticsTaskThresholdLowTriggerValue,
       "hwPMStatisticsTaskThresholdHighClearedValue": hwPMStatisticsTaskThresholdHighClearedValue,
       "hwPMStatisticsTaskThresholdLowClearedValue": hwPMStatisticsTaskThresholdLowClearedValue,
       "hwPMStatisticsTaskThresholdRuleRowStatus": hwPMStatisticsTaskThresholdRuleRowStatus,
       "hwPMStatisticsTaskThresholdEvent": hwPMStatisticsTaskThresholdEvent,
       "hwPMStatisticsTaskThresholdTriggerAlarm": hwPMStatisticsTaskThresholdTriggerAlarm,
       "hwPMStatisticsTaskThresholdClearAlarm": hwPMStatisticsTaskThresholdClearAlarm,
       "hwPMStatisticsTaskIndicateLowValue": hwPMStatisticsTaskIndicateLowValue,
       "hwPMStatisticsTaskIndicateHighValue": hwPMStatisticsTaskIndicateHighValue,
       "hwPMStatisticsTaskFileTable": hwPMStatisticsTaskFileTable,
       "hwPMStatisticsTaskFileEntry": hwPMStatisticsTaskFileEntry,
       "hwPMStatisticsTaskFileIndex": hwPMStatisticsTaskFileIndex,
       "hwPMStatisticsTaskFileName": hwPMStatisticsTaskFileName,
       "hwPMStatisticsTraps": hwPMStatisticsTraps,
       "hwPMMeasureExceed": hwPMMeasureExceed,
       "hwPMFileUploadMgmtInstances": hwPMFileUploadMgmtInstances,
       "hwPMServerTable": hwPMServerTable,
       "hwPMServerEntry": hwPMServerEntry,
       "hwPMServerName": hwPMServerName,
       "hwPMServerSrcAddrType": hwPMServerSrcAddrType,
       "hwPMServerSrcAddr": hwPMServerSrcAddr,
       "hwPMServerVpnName": hwPMServerVpnName,
       "hwPMServerHostAddrType": hwPMServerHostAddrType,
       "hwPMServerHostAddr": hwPMServerHostAddr,
       "hwPMServerPort": hwPMServerPort,
       "hwPMServerUserName": hwPMServerUserName,
       "hwPMServerPassword": hwPMServerPassword,
       "hwPMServerSrcIfName": hwPMServerSrcIfName,
       "hwPMServerRetryTimes": hwPMServerRetryTimes,
       "hwPMServerDestPath": hwPMServerDestPath,
       "hwPMServerTransferProtocol": hwPMServerTransferProtocol,
       "hwPMServerRowStatus": hwPMServerRowStatus,
       "hwPMServerVpnType": hwPMServerVpnType,
       "hwPMFileUploadCfgTable": hwPMFileUploadCfgTable,
       "hwPMFileUploadCfgEntry": hwPMFileUploadCfgEntry,
       "hwPMFileUploadRequestName": hwPMFileUploadRequestName,
       "hwPMFileUploadServerName": hwPMFileUploadServerName,
       "hwPMFileUploadCfgRowStatus": hwPMFileUploadCfgRowStatus,
       "hwPMFileUploadMgmtTable": hwPMFileUploadMgmtTable,
       "hwPMFileUploadMgmtEntry": hwPMFileUploadMgmtEntry,
       "hwPMFileUploadFileList": hwPMFileUploadFileList,
       "hwPMFileUploadStatus": hwPMFileUploadStatus,
       "hwPMDataInstances": hwPMDataInstances,
       "hwPMHistoryDataTable": hwPMHistoryDataTable,
       "hwPMHistoryDataEntry": hwPMHistoryDataEntry,
       "hwPMHistoryDataInstanceType": hwPMHistoryDataInstanceType,
       "hwPMHistoryDataInstanceName": hwPMHistoryDataInstanceName,
       "hwPMHistoryDataIndicatorID": hwPMHistoryDataIndicatorID,
       "hwPMHistoryDataIntervalIndex": hwPMHistoryDataIntervalIndex,
       "hwPMHistoryDataHighValue": hwPMHistoryDataHighValue,
       "hwPMHistoryDataLowValue": hwPMHistoryDataLowValue,
       "hwPMHistoryDataValidFlag": hwPMHistoryDataValidFlag,
       "hwPMHistoryDateAndTime": hwPMHistoryDateAndTime,
       "hwPMCurrentDataTable": hwPMCurrentDataTable,
       "hwPMCurrentDataEntry": hwPMCurrentDataEntry,
       "hwPMCurrentDataInstanceType": hwPMCurrentDataInstanceType,
       "hwPMCurrentDataInstanceName": hwPMCurrentDataInstanceName,
       "hwPMCurrentDataIndicatorID": hwPMCurrentDataIndicatorID,
       "hwPMCurrentDataHighValue": hwPMCurrentDataHighValue,
       "hwPMCurrentDataLowValue": hwPMCurrentDataLowValue,
       "hwPMCurrentDataValidFlag": hwPMCurrentDataValidFlag,
       "hwPMCurrentDateAndTime": hwPMCurrentDateAndTime,
       "hwPMResetCurrentDataTable": hwPMResetCurrentDataTable,
       "hwPMResetCurrentDataEntry": hwPMResetCurrentDataEntry,
       "hwPMResetCurrentDataInstanceType": hwPMResetCurrentDataInstanceType,
       "hwPMResetCurrentDataInstanceName": hwPMResetCurrentDataInstanceName,
       "hwPMResetCurrentDataIndicatorID": hwPMResetCurrentDataIndicatorID,
       "hwPMGlobalInstances": hwPMGlobalInstances,
       "hwPMIntervalTypeTable": hwPMIntervalTypeTable,
       "hwPMIntervalTypeEntry": hwPMIntervalTypeEntry,
       "hwPMIntervalType": hwPMIntervalType,
       "hwPMIntervalTypeName": hwPMIntervalTypeName,
       "hwPMIntervalTypeInterval": hwPMIntervalTypeInterval,
       "hwPMIntervalTypeHistorynum": hwPMIntervalTypeHistorynum,
       "hwPMIntervalTypeDelayRange": hwPMIntervalTypeDelayRange,
       "hwPMIntervalTypeSampleInterval": hwPMIntervalTypeSampleInterval,
       "hwPMInstanceTypeTable": hwPMInstanceTypeTable,
       "hwPMInstanceTypeEntry": hwPMInstanceTypeEntry,
       "hwPMInstanceTypeID": hwPMInstanceTypeID,
       "hwPMInstanceTypeName": hwPMInstanceTypeName,
       "hwPMIndicatorTable": hwPMIndicatorTable,
       "hwPMIndicatorEntry": hwPMIndicatorEntry,
       "hwPMIndicatorID": hwPMIndicatorID,
       "hwPMIndicatorName": hwPMIndicatorName,
       "hwPMIndicatorType": hwPMIndicatorType,
       "hwPMIndicatorCounterType": hwPMIndicatorCounterType,
       "hwPMConformance": hwPMConformance,
       "hwPMCompliances": hwPMCompliances,
       "hwPMCompliance": hwPMCompliance,
       "hwPMGroup": hwPMGroup,
       "hwPMMIBGroup": hwPMMIBGroup,
       "hwPMTaskGroup": hwPMTaskGroup,
       "hwPMTaskInstanceGroup": hwPMTaskInstanceGroup,
       "hwPMTaskThresholdGroup": hwPMTaskThresholdGroup,
       "hwPMTaskFileGroup": hwPMTaskFileGroup,
       "hwPMFileUploadGroup": hwPMFileUploadGroup,
       "hwPMDataInstanceGroup": hwPMDataInstanceGroup,
       "hwPMIntervalTypeGroup": hwPMIntervalTypeGroup,
       "hwPMInstanceTypeGroup": hwPMInstanceTypeGroup,
       "hwPMIndicatorGroup": hwPMIndicatorGroup,
       "hwPMNotificationGroup": hwPMNotificationGroup}
)
