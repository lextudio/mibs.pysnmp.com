# SNMP MIB module (ACD-SA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-SA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:23 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

acdSa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12)
)
acdSa.setRevisions(
        ("2011-12-21 01:00",
         "2011-03-15 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcdSaMetricType(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("metricCfmOwDelay", 7),
          ("metricCfmOwDv", 8),
          ("metricCfmPlr", 6),
          ("metricCfmSlmFarEndPlr", 12),
          ("metricCfmSlmNearEndPlr", 11),
          ("metricCfmTwDelay", 9),
          ("metricCfmTwDv", 10),
          ("metricPaaOwDelay", 2),
          ("metricPaaOwDv", 3),
          ("metricPaaPlr", 1),
          ("metricPaaTwDelay", 4),
          ("metricPaaTwDv", 5))
    )



class AcdSaValidFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adjusted", 2),
          ("pending", 3),
          ("valid", 1))
    )



class AcdSaAdminStateFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2))
    )



class AcdSaOperStateFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2),
          ("oosAu", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AcdSaNotifications_ObjectIdentity = ObjectIdentity
acdSaNotifications = _AcdSaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 0)
)
_AcdSaMIBObjects_ObjectIdentity = ObjectIdentity
acdSaMIBObjects = _AcdSaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1)
)
_AcdSaConfig_ObjectIdentity = ObjectIdentity
acdSaConfig = _AcdSaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1)
)
_AcdSaServiceConfigTable_Object = MibTable
acdSaServiceConfigTable = _AcdSaServiceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acdSaServiceConfigTable.setStatus("current")
_AcdSaServiceConfigEntry_Object = MibTableRow
acdSaServiceConfigEntry = _AcdSaServiceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1)
)
acdSaServiceConfigEntry.setIndexNames(
    (0, "ACD-SA-MIB", "acdSaServiceIndex"),
)
if mibBuilder.loadTexts:
    acdSaServiceConfigEntry.setStatus("current")
_AcdSaServiceIndex_Type = Unsigned32
_AcdSaServiceIndex_Object = MibTableColumn
acdSaServiceIndex = _AcdSaServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 1),
    _AcdSaServiceIndex_Type()
)
acdSaServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSaServiceIndex.setStatus("current")
_AcdSaServiceConfigRowStatus_Type = RowStatus
_AcdSaServiceConfigRowStatus_Object = MibTableColumn
acdSaServiceConfigRowStatus = _AcdSaServiceConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 2),
    _AcdSaServiceConfigRowStatus_Type()
)
acdSaServiceConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSaServiceConfigRowStatus.setStatus("current")


class _AcdSaServiceConfigName_Type(DisplayString):
    """Custom type acdSaServiceConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdSaServiceConfigName_Type.__name__ = "DisplayString"
_AcdSaServiceConfigName_Object = MibTableColumn
acdSaServiceConfigName = _AcdSaServiceConfigName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 3),
    _AcdSaServiceConfigName_Type()
)
acdSaServiceConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSaServiceConfigName.setStatus("current")


class _AcdSaServiceConfigAdminState_Type(AcdSaAdminStateFlag):
    """Custom type acdSaServiceConfigAdminState based on AcdSaAdminStateFlag"""
    defaultValue = 2


_AcdSaServiceConfigAdminState_Object = MibTableColumn
acdSaServiceConfigAdminState = _AcdSaServiceConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 4),
    _AcdSaServiceConfigAdminState_Type()
)
acdSaServiceConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSaServiceConfigAdminState.setStatus("current")


class _AcdSaServiceConfigReportingPeriod_Type(Unsigned32):
    """Custom type acdSaServiceConfigReportingPeriod based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_AcdSaServiceConfigReportingPeriod_Type.__name__ = "Unsigned32"
_AcdSaServiceConfigReportingPeriod_Object = MibTableColumn
acdSaServiceConfigReportingPeriod = _AcdSaServiceConfigReportingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 5),
    _AcdSaServiceConfigReportingPeriod_Type()
)
acdSaServiceConfigReportingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSaServiceConfigReportingPeriod.setStatus("current")


class _AcdSaServiceConfigUaWindowSize_Type(Unsigned32):
    """Custom type acdSaServiceConfigUaWindowSize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AcdSaServiceConfigUaWindowSize_Type.__name__ = "Unsigned32"
_AcdSaServiceConfigUaWindowSize_Object = MibTableColumn
acdSaServiceConfigUaWindowSize = _AcdSaServiceConfigUaWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 6),
    _AcdSaServiceConfigUaWindowSize_Type()
)
acdSaServiceConfigUaWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSaServiceConfigUaWindowSize.setStatus("current")


class _AcdSaServiceConfigHliWindowSize_Type(Unsigned32):
    """Custom type acdSaServiceConfigHliWindowSize based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_AcdSaServiceConfigHliWindowSize_Type.__name__ = "Unsigned32"
_AcdSaServiceConfigHliWindowSize_Object = MibTableColumn
acdSaServiceConfigHliWindowSize = _AcdSaServiceConfigHliWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 7),
    _AcdSaServiceConfigHliWindowSize_Type()
)
acdSaServiceConfigHliWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSaServiceConfigHliWindowSize.setStatus("current")


class _AcdSaServiceConfigTimeInterval_Type(Unsigned32):
    """Custom type acdSaServiceConfigTimeInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AcdSaServiceConfigTimeInterval_Type.__name__ = "Unsigned32"
_AcdSaServiceConfigTimeInterval_Object = MibTableColumn
acdSaServiceConfigTimeInterval = _AcdSaServiceConfigTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 1, 1, 8),
    _AcdSaServiceConfigTimeInterval_Type()
)
acdSaServiceConfigTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSaServiceConfigTimeInterval.setStatus("current")
_AcdSaMetricConfigTable_Object = MibTable
acdSaMetricConfigTable = _AcdSaMetricConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    acdSaMetricConfigTable.setStatus("current")
_AcdSaMetricConfigEntry_Object = MibTableRow
acdSaMetricConfigEntry = _AcdSaMetricConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1)
)
acdSaMetricConfigEntry.setIndexNames(
    (0, "ACD-SA-MIB", "acdSaServiceIndex"),
    (0, "ACD-SA-MIB", "acdSaMetricIndex"),
)
if mibBuilder.loadTexts:
    acdSaMetricConfigEntry.setStatus("current")
_AcdSaMetricIndex_Type = Unsigned32
_AcdSaMetricIndex_Object = MibTableColumn
acdSaMetricIndex = _AcdSaMetricIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 1),
    _AcdSaMetricIndex_Type()
)
acdSaMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSaMetricIndex.setStatus("current")
_AcdSaMetricConfigRowStatus_Type = RowStatus
_AcdSaMetricConfigRowStatus_Object = MibTableColumn
acdSaMetricConfigRowStatus = _AcdSaMetricConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 2),
    _AcdSaMetricConfigRowStatus_Type()
)
acdSaMetricConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSaMetricConfigRowStatus.setStatus("current")


class _AcdSaMetricConfigName_Type(DisplayString):
    """Custom type acdSaMetricConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdSaMetricConfigName_Type.__name__ = "DisplayString"
_AcdSaMetricConfigName_Object = MibTableColumn
acdSaMetricConfigName = _AcdSaMetricConfigName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 3),
    _AcdSaMetricConfigName_Type()
)
acdSaMetricConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSaMetricConfigName.setStatus("current")


class _AcdSaMetricConfigSrcName_Type(DisplayString):
    """Custom type acdSaMetricConfigSrcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdSaMetricConfigSrcName_Type.__name__ = "DisplayString"
_AcdSaMetricConfigSrcName_Object = MibTableColumn
acdSaMetricConfigSrcName = _AcdSaMetricConfigSrcName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 4),
    _AcdSaMetricConfigSrcName_Type()
)
acdSaMetricConfigSrcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSaMetricConfigSrcName.setStatus("current")


class _AcdSaMetricConfigType_Type(AcdSaMetricType):
    """Custom type acdSaMetricConfigType based on AcdSaMetricType"""


_AcdSaMetricConfigType_Object = MibTableColumn
acdSaMetricConfigType = _AcdSaMetricConfigType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 5),
    _AcdSaMetricConfigType_Type()
)
acdSaMetricConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSaMetricConfigType.setStatus("current")


class _AcdSaMetricConfigThreshold_Type(Unsigned32):
    """Custom type acdSaMetricConfigThreshold based on Unsigned32"""
    defaultValue = 0


_AcdSaMetricConfigThreshold_Object = MibTableColumn
acdSaMetricConfigThreshold = _AcdSaMetricConfigThreshold_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 1, 2, 1, 6),
    _AcdSaMetricConfigThreshold_Type()
)
acdSaMetricConfigThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSaMetricConfigThreshold.setStatus("current")
_AcdSaCounter_ObjectIdentity = ObjectIdentity
acdSaCounter = _AcdSaCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2)
)
_AcdSaServiceCounterTable_Object = MibTable
acdSaServiceCounterTable = _AcdSaServiceCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acdSaServiceCounterTable.setStatus("current")
_AcdSaServiceCounterEntry_Object = MibTableRow
acdSaServiceCounterEntry = _AcdSaServiceCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1)
)
acdSaServiceCounterEntry.setIndexNames(
    (0, "ACD-SA-MIB", "acdSaServiceIndex"),
)
if mibBuilder.loadTexts:
    acdSaServiceCounterEntry.setStatus("current")
_AcdSaServiceCounterPeriodIndex_Type = Unsigned32
_AcdSaServiceCounterPeriodIndex_Object = MibTableColumn
acdSaServiceCounterPeriodIndex = _AcdSaServiceCounterPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 1),
    _AcdSaServiceCounterPeriodIndex_Type()
)
acdSaServiceCounterPeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceCounterPeriodIndex.setStatus("current")
_AcdSaServiceCounterValidFlag_Type = AcdSaValidFlag
_AcdSaServiceCounterValidFlag_Object = MibTableColumn
acdSaServiceCounterValidFlag = _AcdSaServiceCounterValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 2),
    _AcdSaServiceCounterValidFlag_Type()
)
acdSaServiceCounterValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceCounterValidFlag.setStatus("current")
_AcdSaServiceCounterUpTime_Type = Unsigned32
_AcdSaServiceCounterUpTime_Object = MibTableColumn
acdSaServiceCounterUpTime = _AcdSaServiceCounterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 3),
    _AcdSaServiceCounterUpTime_Type()
)
acdSaServiceCounterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceCounterUpTime.setStatus("current")
_AcdSaServiceCounterUaTime_Type = Unsigned32
_AcdSaServiceCounterUaTime_Object = MibTableColumn
acdSaServiceCounterUaTime = _AcdSaServiceCounterUaTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 4),
    _AcdSaServiceCounterUaTime_Type()
)
acdSaServiceCounterUaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceCounterUaTime.setStatus("current")
_AcdSaServiceCounterMaintTime_Type = Unsigned32
_AcdSaServiceCounterMaintTime_Object = MibTableColumn
acdSaServiceCounterMaintTime = _AcdSaServiceCounterMaintTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 5),
    _AcdSaServiceCounterMaintTime_Type()
)
acdSaServiceCounterMaintTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceCounterMaintTime.setStatus("current")


class _AcdSaServiceCounterAvailRatio_Type(Unsigned32):
    """Custom type acdSaServiceCounterAvailRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdSaServiceCounterAvailRatio_Type.__name__ = "Unsigned32"
_AcdSaServiceCounterAvailRatio_Object = MibTableColumn
acdSaServiceCounterAvailRatio = _AcdSaServiceCounterAvailRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 6),
    _AcdSaServiceCounterAvailRatio_Type()
)
acdSaServiceCounterAvailRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceCounterAvailRatio.setStatus("current")
_AcdSaServiceCounterGaps_Type = Unsigned32
_AcdSaServiceCounterGaps_Object = MibTableColumn
acdSaServiceCounterGaps = _AcdSaServiceCounterGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 7),
    _AcdSaServiceCounterGaps_Type()
)
acdSaServiceCounterGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceCounterGaps.setStatus("current")
_AcdSaServiceCounterLargestGap_Type = Unsigned32
_AcdSaServiceCounterLargestGap_Object = MibTableColumn
acdSaServiceCounterLargestGap = _AcdSaServiceCounterLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 8),
    _AcdSaServiceCounterLargestGap_Type()
)
acdSaServiceCounterLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceCounterLargestGap.setStatus("current")
_AcdSaServiceCounterChliTime_Type = Unsigned32
_AcdSaServiceCounterChliTime_Object = MibTableColumn
acdSaServiceCounterChliTime = _AcdSaServiceCounterChliTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 9),
    _AcdSaServiceCounterChliTime_Type()
)
acdSaServiceCounterChliTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceCounterChliTime.setStatus("current")


class _AcdSaServiceCounterChliRatio_Type(Unsigned32):
    """Custom type acdSaServiceCounterChliRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdSaServiceCounterChliRatio_Type.__name__ = "Unsigned32"
_AcdSaServiceCounterChliRatio_Object = MibTableColumn
acdSaServiceCounterChliRatio = _AcdSaServiceCounterChliRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 1, 1, 10),
    _AcdSaServiceCounterChliRatio_Type()
)
acdSaServiceCounterChliRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceCounterChliRatio.setStatus("current")
_AcdSaServiceHistCounterTable_Object = MibTable
acdSaServiceHistCounterTable = _AcdSaServiceHistCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    acdSaServiceHistCounterTable.setStatus("current")
_AcdSaServiceHistCounterEntry_Object = MibTableRow
acdSaServiceHistCounterEntry = _AcdSaServiceHistCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1)
)
acdSaServiceHistCounterEntry.setIndexNames(
    (0, "ACD-SA-MIB", "acdSaServiceIndex"),
    (0, "ACD-SA-MIB", "acdSaServiceHistCounterPeriodIndex"),
)
if mibBuilder.loadTexts:
    acdSaServiceHistCounterEntry.setStatus("current")
_AcdSaServiceHistCounterPeriodIndex_Type = Unsigned32
_AcdSaServiceHistCounterPeriodIndex_Object = MibTableColumn
acdSaServiceHistCounterPeriodIndex = _AcdSaServiceHistCounterPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 1),
    _AcdSaServiceHistCounterPeriodIndex_Type()
)
acdSaServiceHistCounterPeriodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSaServiceHistCounterPeriodIndex.setStatus("current")
_AcdSaServiceHistCounterIntervalEnd_Type = DateAndTime
_AcdSaServiceHistCounterIntervalEnd_Object = MibTableColumn
acdSaServiceHistCounterIntervalEnd = _AcdSaServiceHistCounterIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 2),
    _AcdSaServiceHistCounterIntervalEnd_Type()
)
acdSaServiceHistCounterIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceHistCounterIntervalEnd.setStatus("current")
_AcdSaServiceHistCounterValidFlag_Type = AcdSaValidFlag
_AcdSaServiceHistCounterValidFlag_Object = MibTableColumn
acdSaServiceHistCounterValidFlag = _AcdSaServiceHistCounterValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 3),
    _AcdSaServiceHistCounterValidFlag_Type()
)
acdSaServiceHistCounterValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceHistCounterValidFlag.setStatus("current")
_AcdSaServiceHistCounterUpTime_Type = Unsigned32
_AcdSaServiceHistCounterUpTime_Object = MibTableColumn
acdSaServiceHistCounterUpTime = _AcdSaServiceHistCounterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 4),
    _AcdSaServiceHistCounterUpTime_Type()
)
acdSaServiceHistCounterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceHistCounterUpTime.setStatus("current")
_AcdSaServiceHistCounterUaTime_Type = Unsigned32
_AcdSaServiceHistCounterUaTime_Object = MibTableColumn
acdSaServiceHistCounterUaTime = _AcdSaServiceHistCounterUaTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 5),
    _AcdSaServiceHistCounterUaTime_Type()
)
acdSaServiceHistCounterUaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceHistCounterUaTime.setStatus("current")
_AcdSaServiceHistCounterMaintTime_Type = Unsigned32
_AcdSaServiceHistCounterMaintTime_Object = MibTableColumn
acdSaServiceHistCounterMaintTime = _AcdSaServiceHistCounterMaintTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 6),
    _AcdSaServiceHistCounterMaintTime_Type()
)
acdSaServiceHistCounterMaintTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceHistCounterMaintTime.setStatus("current")


class _AcdSaServiceHistCounterAvailRatio_Type(Unsigned32):
    """Custom type acdSaServiceHistCounterAvailRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdSaServiceHistCounterAvailRatio_Type.__name__ = "Unsigned32"
_AcdSaServiceHistCounterAvailRatio_Object = MibTableColumn
acdSaServiceHistCounterAvailRatio = _AcdSaServiceHistCounterAvailRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 7),
    _AcdSaServiceHistCounterAvailRatio_Type()
)
acdSaServiceHistCounterAvailRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceHistCounterAvailRatio.setStatus("current")
_AcdSaServiceHistCounterGaps_Type = Unsigned32
_AcdSaServiceHistCounterGaps_Object = MibTableColumn
acdSaServiceHistCounterGaps = _AcdSaServiceHistCounterGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 8),
    _AcdSaServiceHistCounterGaps_Type()
)
acdSaServiceHistCounterGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceHistCounterGaps.setStatus("current")
_AcdSaServiceHistCounterLargestGap_Type = Unsigned32
_AcdSaServiceHistCounterLargestGap_Object = MibTableColumn
acdSaServiceHistCounterLargestGap = _AcdSaServiceHistCounterLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 9),
    _AcdSaServiceHistCounterLargestGap_Type()
)
acdSaServiceHistCounterLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceHistCounterLargestGap.setStatus("current")
_AcdSaServiceHistCounterChliTime_Type = Unsigned32
_AcdSaServiceHistCounterChliTime_Object = MibTableColumn
acdSaServiceHistCounterChliTime = _AcdSaServiceHistCounterChliTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 10),
    _AcdSaServiceHistCounterChliTime_Type()
)
acdSaServiceHistCounterChliTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceHistCounterChliTime.setStatus("current")


class _AcdSaServiceHistCounterChliRatio_Type(Unsigned32):
    """Custom type acdSaServiceHistCounterChliRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdSaServiceHistCounterChliRatio_Type.__name__ = "Unsigned32"
_AcdSaServiceHistCounterChliRatio_Object = MibTableColumn
acdSaServiceHistCounterChliRatio = _AcdSaServiceHistCounterChliRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 2, 1, 11),
    _AcdSaServiceHistCounterChliRatio_Type()
)
acdSaServiceHistCounterChliRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceHistCounterChliRatio.setStatus("current")
_AcdSaServiceMonoCounterTable_Object = MibTable
acdSaServiceMonoCounterTable = _AcdSaServiceMonoCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3)
)
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterTable.setStatus("current")
_AcdSaServiceMonoCounterEntry_Object = MibTableRow
acdSaServiceMonoCounterEntry = _AcdSaServiceMonoCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1)
)
acdSaServiceMonoCounterEntry.setIndexNames(
    (0, "ACD-SA-MIB", "acdSaServiceIndex"),
)
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterEntry.setStatus("current")
_AcdSaServiceMonoCounterValidFlag_Type = AcdSaValidFlag
_AcdSaServiceMonoCounterValidFlag_Object = MibTableColumn
acdSaServiceMonoCounterValidFlag = _AcdSaServiceMonoCounterValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 1),
    _AcdSaServiceMonoCounterValidFlag_Type()
)
acdSaServiceMonoCounterValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterValidFlag.setStatus("current")
_AcdSaServiceMonoCounterUpTime_Type = Unsigned32
_AcdSaServiceMonoCounterUpTime_Object = MibTableColumn
acdSaServiceMonoCounterUpTime = _AcdSaServiceMonoCounterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 2),
    _AcdSaServiceMonoCounterUpTime_Type()
)
acdSaServiceMonoCounterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterUpTime.setStatus("current")
_AcdSaServiceMonoCounterUaTime_Type = Unsigned32
_AcdSaServiceMonoCounterUaTime_Object = MibTableColumn
acdSaServiceMonoCounterUaTime = _AcdSaServiceMonoCounterUaTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 3),
    _AcdSaServiceMonoCounterUaTime_Type()
)
acdSaServiceMonoCounterUaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterUaTime.setStatus("current")
_AcdSaServiceMonoCounterMaintTime_Type = Unsigned32
_AcdSaServiceMonoCounterMaintTime_Object = MibTableColumn
acdSaServiceMonoCounterMaintTime = _AcdSaServiceMonoCounterMaintTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 4),
    _AcdSaServiceMonoCounterMaintTime_Type()
)
acdSaServiceMonoCounterMaintTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterMaintTime.setStatus("current")


class _AcdSaServiceMonoCounterAvailRatio_Type(Unsigned32):
    """Custom type acdSaServiceMonoCounterAvailRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdSaServiceMonoCounterAvailRatio_Type.__name__ = "Unsigned32"
_AcdSaServiceMonoCounterAvailRatio_Object = MibTableColumn
acdSaServiceMonoCounterAvailRatio = _AcdSaServiceMonoCounterAvailRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 5),
    _AcdSaServiceMonoCounterAvailRatio_Type()
)
acdSaServiceMonoCounterAvailRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterAvailRatio.setStatus("current")
_AcdSaServiceMonoCounterGaps_Type = Unsigned32
_AcdSaServiceMonoCounterGaps_Object = MibTableColumn
acdSaServiceMonoCounterGaps = _AcdSaServiceMonoCounterGaps_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 6),
    _AcdSaServiceMonoCounterGaps_Type()
)
acdSaServiceMonoCounterGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterGaps.setStatus("current")
_AcdSaServiceMonoCounterLargestGap_Type = Unsigned32
_AcdSaServiceMonoCounterLargestGap_Object = MibTableColumn
acdSaServiceMonoCounterLargestGap = _AcdSaServiceMonoCounterLargestGap_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 7),
    _AcdSaServiceMonoCounterLargestGap_Type()
)
acdSaServiceMonoCounterLargestGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterLargestGap.setStatus("current")
_AcdSaServiceMonoCounterChliTime_Type = Unsigned32
_AcdSaServiceMonoCounterChliTime_Object = MibTableColumn
acdSaServiceMonoCounterChliTime = _AcdSaServiceMonoCounterChliTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 8),
    _AcdSaServiceMonoCounterChliTime_Type()
)
acdSaServiceMonoCounterChliTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterChliTime.setStatus("current")


class _AcdSaServiceMonoCounterChliRatio_Type(Unsigned32):
    """Custom type acdSaServiceMonoCounterChliRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_AcdSaServiceMonoCounterChliRatio_Type.__name__ = "Unsigned32"
_AcdSaServiceMonoCounterChliRatio_Object = MibTableColumn
acdSaServiceMonoCounterChliRatio = _AcdSaServiceMonoCounterChliRatio_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 3, 1, 9),
    _AcdSaServiceMonoCounterChliRatio_Type()
)
acdSaServiceMonoCounterChliRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterChliRatio.setStatus("current")
_AcdSaMetricCounterTable_Object = MibTable
acdSaMetricCounterTable = _AcdSaMetricCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 4)
)
if mibBuilder.loadTexts:
    acdSaMetricCounterTable.setStatus("current")
_AcdSaMetricCounterEntry_Object = MibTableRow
acdSaMetricCounterEntry = _AcdSaMetricCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 4, 1)
)
acdSaMetricCounterEntry.setIndexNames(
    (0, "ACD-SA-MIB", "acdSaServiceIndex"),
    (0, "ACD-SA-MIB", "acdSaMetricIndex"),
)
if mibBuilder.loadTexts:
    acdSaMetricCounterEntry.setStatus("current")
_AcdSaMetricCounterValidFlag_Type = AcdSaValidFlag
_AcdSaMetricCounterValidFlag_Object = MibTableColumn
acdSaMetricCounterValidFlag = _AcdSaMetricCounterValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 4, 1, 1),
    _AcdSaMetricCounterValidFlag_Type()
)
acdSaMetricCounterValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaMetricCounterValidFlag.setStatus("current")
_AcdSaMetricCounterUaTime_Type = Unsigned32
_AcdSaMetricCounterUaTime_Object = MibTableColumn
acdSaMetricCounterUaTime = _AcdSaMetricCounterUaTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 4, 1, 2),
    _AcdSaMetricCounterUaTime_Type()
)
acdSaMetricCounterUaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaMetricCounterUaTime.setStatus("current")
_AcdSaMetricCounterChliTime_Type = Unsigned32
_AcdSaMetricCounterChliTime_Object = MibTableColumn
acdSaMetricCounterChliTime = _AcdSaMetricCounterChliTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 4, 1, 3),
    _AcdSaMetricCounterChliTime_Type()
)
acdSaMetricCounterChliTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaMetricCounterChliTime.setStatus("current")
_AcdSaMetricHistCounterTable_Object = MibTable
acdSaMetricHistCounterTable = _AcdSaMetricHistCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5)
)
if mibBuilder.loadTexts:
    acdSaMetricHistCounterTable.setStatus("current")
_AcdSaMetricHistCounterEntry_Object = MibTableRow
acdSaMetricHistCounterEntry = _AcdSaMetricHistCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1)
)
acdSaMetricHistCounterEntry.setIndexNames(
    (0, "ACD-SA-MIB", "acdSaMetricHistCounterID"),
    (0, "ACD-SA-MIB", "acdSaMetricHistCounterPeriodIndex"),
)
if mibBuilder.loadTexts:
    acdSaMetricHistCounterEntry.setStatus("current")
_AcdSaMetricHistCounterID_Type = Unsigned32
_AcdSaMetricHistCounterID_Object = MibTableColumn
acdSaMetricHistCounterID = _AcdSaMetricHistCounterID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 1),
    _AcdSaMetricHistCounterID_Type()
)
acdSaMetricHistCounterID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSaMetricHistCounterID.setStatus("current")
_AcdSaMetricHistCounterPeriodIndex_Type = Unsigned32
_AcdSaMetricHistCounterPeriodIndex_Object = MibTableColumn
acdSaMetricHistCounterPeriodIndex = _AcdSaMetricHistCounterPeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 2),
    _AcdSaMetricHistCounterPeriodIndex_Type()
)
acdSaMetricHistCounterPeriodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSaMetricHistCounterPeriodIndex.setStatus("current")
_AcdSaMetricHistCounterIntervalEnd_Type = DateAndTime
_AcdSaMetricHistCounterIntervalEnd_Object = MibTableColumn
acdSaMetricHistCounterIntervalEnd = _AcdSaMetricHistCounterIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 3),
    _AcdSaMetricHistCounterIntervalEnd_Type()
)
acdSaMetricHistCounterIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaMetricHistCounterIntervalEnd.setStatus("current")
_AcdSaMetricHistCounterValidFlag_Type = AcdSaValidFlag
_AcdSaMetricHistCounterValidFlag_Object = MibTableColumn
acdSaMetricHistCounterValidFlag = _AcdSaMetricHistCounterValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 4),
    _AcdSaMetricHistCounterValidFlag_Type()
)
acdSaMetricHistCounterValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaMetricHistCounterValidFlag.setStatus("current")
_AcdSaMetricHistCounterUaTime_Type = Unsigned32
_AcdSaMetricHistCounterUaTime_Object = MibTableColumn
acdSaMetricHistCounterUaTime = _AcdSaMetricHistCounterUaTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 5),
    _AcdSaMetricHistCounterUaTime_Type()
)
acdSaMetricHistCounterUaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaMetricHistCounterUaTime.setStatus("current")
_AcdSaMetricHistCounterChliTime_Type = Unsigned32
_AcdSaMetricHistCounterChliTime_Object = MibTableColumn
acdSaMetricHistCounterChliTime = _AcdSaMetricHistCounterChliTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 5, 1, 6),
    _AcdSaMetricHistCounterChliTime_Type()
)
acdSaMetricHistCounterChliTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaMetricHistCounterChliTime.setStatus("current")
_AcdSaMetricMonoCounterTable_Object = MibTable
acdSaMetricMonoCounterTable = _AcdSaMetricMonoCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 6)
)
if mibBuilder.loadTexts:
    acdSaMetricMonoCounterTable.setStatus("current")
_AcdSaMetricMonoCounterEntry_Object = MibTableRow
acdSaMetricMonoCounterEntry = _AcdSaMetricMonoCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 6, 1)
)
acdSaMetricMonoCounterEntry.setIndexNames(
    (0, "ACD-SA-MIB", "acdSaServiceIndex"),
    (0, "ACD-SA-MIB", "acdSaMetricIndex"),
)
if mibBuilder.loadTexts:
    acdSaMetricMonoCounterEntry.setStatus("current")
_AcdSaMetricMonoCounterValidFlag_Type = AcdSaValidFlag
_AcdSaMetricMonoCounterValidFlag_Object = MibTableColumn
acdSaMetricMonoCounterValidFlag = _AcdSaMetricMonoCounterValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 6, 1, 1),
    _AcdSaMetricMonoCounterValidFlag_Type()
)
acdSaMetricMonoCounterValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaMetricMonoCounterValidFlag.setStatus("current")
_AcdSaMetricMonoCounterUaTime_Type = Unsigned32
_AcdSaMetricMonoCounterUaTime_Object = MibTableColumn
acdSaMetricMonoCounterUaTime = _AcdSaMetricMonoCounterUaTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 6, 1, 2),
    _AcdSaMetricMonoCounterUaTime_Type()
)
acdSaMetricMonoCounterUaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaMetricMonoCounterUaTime.setStatus("current")
_AcdSaMetricMonoCounterChliTime_Type = Unsigned32
_AcdSaMetricMonoCounterChliTime_Object = MibTableColumn
acdSaMetricMonoCounterChliTime = _AcdSaMetricMonoCounterChliTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 2, 6, 1, 3),
    _AcdSaMetricMonoCounterChliTime_Type()
)
acdSaMetricMonoCounterChliTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaMetricMonoCounterChliTime.setStatus("current")
_AcdSaStatus_ObjectIdentity = ObjectIdentity
acdSaStatus = _AcdSaStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3)
)
_AcdSaServiceStatusTable_Object = MibTable
acdSaServiceStatusTable = _AcdSaServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    acdSaServiceStatusTable.setStatus("current")
_AcdSaServiceStatusEntry_Object = MibTableRow
acdSaServiceStatusEntry = _AcdSaServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1)
)
acdSaServiceStatusEntry.setIndexNames(
    (0, "ACD-SA-MIB", "acdSaServiceStatusID"),
)
if mibBuilder.loadTexts:
    acdSaServiceStatusEntry.setStatus("current")
_AcdSaServiceStatusID_Type = Unsigned32
_AcdSaServiceStatusID_Object = MibTableColumn
acdSaServiceStatusID = _AcdSaServiceStatusID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1, 1),
    _AcdSaServiceStatusID_Type()
)
acdSaServiceStatusID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSaServiceStatusID.setStatus("current")


class _AcdSaServiceStatusName_Type(DisplayString):
    """Custom type acdSaServiceStatusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdSaServiceStatusName_Type.__name__ = "DisplayString"
_AcdSaServiceStatusName_Object = MibTableColumn
acdSaServiceStatusName = _AcdSaServiceStatusName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1, 2),
    _AcdSaServiceStatusName_Type()
)
acdSaServiceStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceStatusName.setStatus("current")


class _AcdSaServiceStatusAdminState_Type(AcdSaAdminStateFlag):
    """Custom type acdSaServiceStatusAdminState based on AcdSaAdminStateFlag"""
    defaultValue = 2


_AcdSaServiceStatusAdminState_Object = MibTableColumn
acdSaServiceStatusAdminState = _AcdSaServiceStatusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1, 3),
    _AcdSaServiceStatusAdminState_Type()
)
acdSaServiceStatusAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceStatusAdminState.setStatus("current")


class _AcdSaServiceStatusOperState_Type(AcdSaOperStateFlag):
    """Custom type acdSaServiceStatusOperState based on AcdSaOperStateFlag"""
    defaultValue = 2


_AcdSaServiceStatusOperState_Object = MibTableColumn
acdSaServiceStatusOperState = _AcdSaServiceStatusOperState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1, 4),
    _AcdSaServiceStatusOperState_Type()
)
acdSaServiceStatusOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceStatusOperState.setStatus("current")


class _AcdSaServiceStatusNbrMetrics_Type(Gauge32):
    """Custom type acdSaServiceStatusNbrMetrics based on Gauge32"""
    defaultValue = 0


_AcdSaServiceStatusNbrMetrics_Object = MibTableColumn
acdSaServiceStatusNbrMetrics = _AcdSaServiceStatusNbrMetrics_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 1, 3, 1, 1, 5),
    _AcdSaServiceStatusNbrMetrics_Type()
)
acdSaServiceStatusNbrMetrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSaServiceStatusNbrMetrics.setStatus("current")
_AcdSaConformance_ObjectIdentity = ObjectIdentity
acdSaConformance = _AcdSaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2)
)
_AcdSaCompliances_ObjectIdentity = ObjectIdentity
acdSaCompliances = _AcdSaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 1)
)
_AcdSaGroups_ObjectIdentity = ObjectIdentity
acdSaGroups = _AcdSaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2)
)

# Managed Objects groups

acdSaServiceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 1)
)
acdSaServiceConfigGroup.setObjects(
      *(("ACD-SA-MIB", "acdSaServiceConfigRowStatus"),
        ("ACD-SA-MIB", "acdSaServiceConfigName"),
        ("ACD-SA-MIB", "acdSaServiceConfigAdminState"),
        ("ACD-SA-MIB", "acdSaServiceConfigReportingPeriod"),
        ("ACD-SA-MIB", "acdSaServiceConfigUaWindowSize"),
        ("ACD-SA-MIB", "acdSaServiceConfigHliWindowSize"),
        ("ACD-SA-MIB", "acdSaServiceConfigTimeInterval"))
)
if mibBuilder.loadTexts:
    acdSaServiceConfigGroup.setStatus("current")

acdSaMetricConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 2)
)
acdSaMetricConfigGroup.setObjects(
      *(("ACD-SA-MIB", "acdSaMetricConfigRowStatus"),
        ("ACD-SA-MIB", "acdSaMetricConfigName"),
        ("ACD-SA-MIB", "acdSaMetricConfigSrcName"),
        ("ACD-SA-MIB", "acdSaMetricConfigType"),
        ("ACD-SA-MIB", "acdSaMetricConfigThreshold"))
)
if mibBuilder.loadTexts:
    acdSaMetricConfigGroup.setStatus("current")

acdSaServiceCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 3)
)
acdSaServiceCounterGroup.setObjects(
      *(("ACD-SA-MIB", "acdSaServiceCounterPeriodIndex"),
        ("ACD-SA-MIB", "acdSaServiceCounterValidFlag"),
        ("ACD-SA-MIB", "acdSaServiceCounterUpTime"),
        ("ACD-SA-MIB", "acdSaServiceCounterUaTime"),
        ("ACD-SA-MIB", "acdSaServiceCounterMaintTime"),
        ("ACD-SA-MIB", "acdSaServiceCounterAvailRatio"),
        ("ACD-SA-MIB", "acdSaServiceCounterGaps"),
        ("ACD-SA-MIB", "acdSaServiceCounterLargestGap"),
        ("ACD-SA-MIB", "acdSaServiceCounterChliTime"),
        ("ACD-SA-MIB", "acdSaServiceCounterChliRatio"))
)
if mibBuilder.loadTexts:
    acdSaServiceCounterGroup.setStatus("current")

acdSaServiceHistCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 4)
)
acdSaServiceHistCounterGroup.setObjects(
      *(("ACD-SA-MIB", "acdSaServiceHistCounterIntervalEnd"),
        ("ACD-SA-MIB", "acdSaServiceHistCounterValidFlag"),
        ("ACD-SA-MIB", "acdSaServiceHistCounterUpTime"),
        ("ACD-SA-MIB", "acdSaServiceHistCounterUaTime"),
        ("ACD-SA-MIB", "acdSaServiceHistCounterMaintTime"),
        ("ACD-SA-MIB", "acdSaServiceHistCounterAvailRatio"),
        ("ACD-SA-MIB", "acdSaServiceHistCounterGaps"),
        ("ACD-SA-MIB", "acdSaServiceHistCounterLargestGap"),
        ("ACD-SA-MIB", "acdSaServiceHistCounterChliTime"),
        ("ACD-SA-MIB", "acdSaServiceHistCounterChliRatio"))
)
if mibBuilder.loadTexts:
    acdSaServiceHistCounterGroup.setStatus("current")

acdSaServiceMonoCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 5)
)
acdSaServiceMonoCounterGroup.setObjects(
      *(("ACD-SA-MIB", "acdSaServiceMonoCounterValidFlag"),
        ("ACD-SA-MIB", "acdSaServiceMonoCounterUpTime"),
        ("ACD-SA-MIB", "acdSaServiceMonoCounterUaTime"),
        ("ACD-SA-MIB", "acdSaServiceMonoCounterMaintTime"),
        ("ACD-SA-MIB", "acdSaServiceMonoCounterAvailRatio"),
        ("ACD-SA-MIB", "acdSaServiceMonoCounterGaps"),
        ("ACD-SA-MIB", "acdSaServiceMonoCounterLargestGap"),
        ("ACD-SA-MIB", "acdSaServiceMonoCounterChliTime"),
        ("ACD-SA-MIB", "acdSaServiceMonoCounterChliRatio"))
)
if mibBuilder.loadTexts:
    acdSaServiceMonoCounterGroup.setStatus("current")

acdSaMetricCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 6)
)
acdSaMetricCounterGroup.setObjects(
      *(("ACD-SA-MIB", "acdSaMetricCounterValidFlag"),
        ("ACD-SA-MIB", "acdSaMetricCounterUaTime"),
        ("ACD-SA-MIB", "acdSaMetricCounterChliTime"))
)
if mibBuilder.loadTexts:
    acdSaMetricCounterGroup.setStatus("current")

acdSaMetricHistCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 7)
)
acdSaMetricHistCounterGroup.setObjects(
      *(("ACD-SA-MIB", "acdSaMetricHistCounterIntervalEnd"),
        ("ACD-SA-MIB", "acdSaMetricHistCounterValidFlag"),
        ("ACD-SA-MIB", "acdSaMetricHistCounterUaTime"),
        ("ACD-SA-MIB", "acdSaMetricHistCounterChliTime"))
)
if mibBuilder.loadTexts:
    acdSaMetricHistCounterGroup.setStatus("current")

acdSaMetricMonoCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 8)
)
acdSaMetricMonoCounterGroup.setObjects(
      *(("ACD-SA-MIB", "acdSaMetricMonoCounterValidFlag"),
        ("ACD-SA-MIB", "acdSaMetricMonoCounterUaTime"),
        ("ACD-SA-MIB", "acdSaMetricMonoCounterChliTime"))
)
if mibBuilder.loadTexts:
    acdSaMetricMonoCounterGroup.setStatus("current")

acdSaServiceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 2, 9)
)
acdSaServiceStatusGroup.setObjects(
      *(("ACD-SA-MIB", "acdSaServiceStatusName"),
        ("ACD-SA-MIB", "acdSaServiceStatusAdminState"),
        ("ACD-SA-MIB", "acdSaServiceStatusOperState"),
        ("ACD-SA-MIB", "acdSaServiceStatusNbrMetrics"))
)
if mibBuilder.loadTexts:
    acdSaServiceStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdSaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 12, 2, 1, 1)
)
if mibBuilder.loadTexts:
    acdSaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-SA-MIB",
    **{"AcdSaMetricType": AcdSaMetricType,
       "AcdSaValidFlag": AcdSaValidFlag,
       "AcdSaAdminStateFlag": AcdSaAdminStateFlag,
       "AcdSaOperStateFlag": AcdSaOperStateFlag,
       "acdSa": acdSa,
       "acdSaNotifications": acdSaNotifications,
       "acdSaMIBObjects": acdSaMIBObjects,
       "acdSaConfig": acdSaConfig,
       "acdSaServiceConfigTable": acdSaServiceConfigTable,
       "acdSaServiceConfigEntry": acdSaServiceConfigEntry,
       "acdSaServiceIndex": acdSaServiceIndex,
       "acdSaServiceConfigRowStatus": acdSaServiceConfigRowStatus,
       "acdSaServiceConfigName": acdSaServiceConfigName,
       "acdSaServiceConfigAdminState": acdSaServiceConfigAdminState,
       "acdSaServiceConfigReportingPeriod": acdSaServiceConfigReportingPeriod,
       "acdSaServiceConfigUaWindowSize": acdSaServiceConfigUaWindowSize,
       "acdSaServiceConfigHliWindowSize": acdSaServiceConfigHliWindowSize,
       "acdSaServiceConfigTimeInterval": acdSaServiceConfigTimeInterval,
       "acdSaMetricConfigTable": acdSaMetricConfigTable,
       "acdSaMetricConfigEntry": acdSaMetricConfigEntry,
       "acdSaMetricIndex": acdSaMetricIndex,
       "acdSaMetricConfigRowStatus": acdSaMetricConfigRowStatus,
       "acdSaMetricConfigName": acdSaMetricConfigName,
       "acdSaMetricConfigSrcName": acdSaMetricConfigSrcName,
       "acdSaMetricConfigType": acdSaMetricConfigType,
       "acdSaMetricConfigThreshold": acdSaMetricConfigThreshold,
       "acdSaCounter": acdSaCounter,
       "acdSaServiceCounterTable": acdSaServiceCounterTable,
       "acdSaServiceCounterEntry": acdSaServiceCounterEntry,
       "acdSaServiceCounterPeriodIndex": acdSaServiceCounterPeriodIndex,
       "acdSaServiceCounterValidFlag": acdSaServiceCounterValidFlag,
       "acdSaServiceCounterUpTime": acdSaServiceCounterUpTime,
       "acdSaServiceCounterUaTime": acdSaServiceCounterUaTime,
       "acdSaServiceCounterMaintTime": acdSaServiceCounterMaintTime,
       "acdSaServiceCounterAvailRatio": acdSaServiceCounterAvailRatio,
       "acdSaServiceCounterGaps": acdSaServiceCounterGaps,
       "acdSaServiceCounterLargestGap": acdSaServiceCounterLargestGap,
       "acdSaServiceCounterChliTime": acdSaServiceCounterChliTime,
       "acdSaServiceCounterChliRatio": acdSaServiceCounterChliRatio,
       "acdSaServiceHistCounterTable": acdSaServiceHistCounterTable,
       "acdSaServiceHistCounterEntry": acdSaServiceHistCounterEntry,
       "acdSaServiceHistCounterPeriodIndex": acdSaServiceHistCounterPeriodIndex,
       "acdSaServiceHistCounterIntervalEnd": acdSaServiceHistCounterIntervalEnd,
       "acdSaServiceHistCounterValidFlag": acdSaServiceHistCounterValidFlag,
       "acdSaServiceHistCounterUpTime": acdSaServiceHistCounterUpTime,
       "acdSaServiceHistCounterUaTime": acdSaServiceHistCounterUaTime,
       "acdSaServiceHistCounterMaintTime": acdSaServiceHistCounterMaintTime,
       "acdSaServiceHistCounterAvailRatio": acdSaServiceHistCounterAvailRatio,
       "acdSaServiceHistCounterGaps": acdSaServiceHistCounterGaps,
       "acdSaServiceHistCounterLargestGap": acdSaServiceHistCounterLargestGap,
       "acdSaServiceHistCounterChliTime": acdSaServiceHistCounterChliTime,
       "acdSaServiceHistCounterChliRatio": acdSaServiceHistCounterChliRatio,
       "acdSaServiceMonoCounterTable": acdSaServiceMonoCounterTable,
       "acdSaServiceMonoCounterEntry": acdSaServiceMonoCounterEntry,
       "acdSaServiceMonoCounterValidFlag": acdSaServiceMonoCounterValidFlag,
       "acdSaServiceMonoCounterUpTime": acdSaServiceMonoCounterUpTime,
       "acdSaServiceMonoCounterUaTime": acdSaServiceMonoCounterUaTime,
       "acdSaServiceMonoCounterMaintTime": acdSaServiceMonoCounterMaintTime,
       "acdSaServiceMonoCounterAvailRatio": acdSaServiceMonoCounterAvailRatio,
       "acdSaServiceMonoCounterGaps": acdSaServiceMonoCounterGaps,
       "acdSaServiceMonoCounterLargestGap": acdSaServiceMonoCounterLargestGap,
       "acdSaServiceMonoCounterChliTime": acdSaServiceMonoCounterChliTime,
       "acdSaServiceMonoCounterChliRatio": acdSaServiceMonoCounterChliRatio,
       "acdSaMetricCounterTable": acdSaMetricCounterTable,
       "acdSaMetricCounterEntry": acdSaMetricCounterEntry,
       "acdSaMetricCounterValidFlag": acdSaMetricCounterValidFlag,
       "acdSaMetricCounterUaTime": acdSaMetricCounterUaTime,
       "acdSaMetricCounterChliTime": acdSaMetricCounterChliTime,
       "acdSaMetricHistCounterTable": acdSaMetricHistCounterTable,
       "acdSaMetricHistCounterEntry": acdSaMetricHistCounterEntry,
       "acdSaMetricHistCounterID": acdSaMetricHistCounterID,
       "acdSaMetricHistCounterPeriodIndex": acdSaMetricHistCounterPeriodIndex,
       "acdSaMetricHistCounterIntervalEnd": acdSaMetricHistCounterIntervalEnd,
       "acdSaMetricHistCounterValidFlag": acdSaMetricHistCounterValidFlag,
       "acdSaMetricHistCounterUaTime": acdSaMetricHistCounterUaTime,
       "acdSaMetricHistCounterChliTime": acdSaMetricHistCounterChliTime,
       "acdSaMetricMonoCounterTable": acdSaMetricMonoCounterTable,
       "acdSaMetricMonoCounterEntry": acdSaMetricMonoCounterEntry,
       "acdSaMetricMonoCounterValidFlag": acdSaMetricMonoCounterValidFlag,
       "acdSaMetricMonoCounterUaTime": acdSaMetricMonoCounterUaTime,
       "acdSaMetricMonoCounterChliTime": acdSaMetricMonoCounterChliTime,
       "acdSaStatus": acdSaStatus,
       "acdSaServiceStatusTable": acdSaServiceStatusTable,
       "acdSaServiceStatusEntry": acdSaServiceStatusEntry,
       "acdSaServiceStatusID": acdSaServiceStatusID,
       "acdSaServiceStatusName": acdSaServiceStatusName,
       "acdSaServiceStatusAdminState": acdSaServiceStatusAdminState,
       "acdSaServiceStatusOperState": acdSaServiceStatusOperState,
       "acdSaServiceStatusNbrMetrics": acdSaServiceStatusNbrMetrics,
       "acdSaConformance": acdSaConformance,
       "acdSaCompliances": acdSaCompliances,
       "acdSaCompliance": acdSaCompliance,
       "acdSaGroups": acdSaGroups,
       "acdSaServiceConfigGroup": acdSaServiceConfigGroup,
       "acdSaMetricConfigGroup": acdSaMetricConfigGroup,
       "acdSaServiceCounterGroup": acdSaServiceCounterGroup,
       "acdSaServiceHistCounterGroup": acdSaServiceHistCounterGroup,
       "acdSaServiceMonoCounterGroup": acdSaServiceMonoCounterGroup,
       "acdSaMetricCounterGroup": acdSaMetricCounterGroup,
       "acdSaMetricHistCounterGroup": acdSaMetricHistCounterGroup,
       "acdSaMetricMonoCounterGroup": acdSaMetricMonoCounterGroup,
       "acdSaServiceStatusGroup": acdSaServiceStatusGroup}
)
