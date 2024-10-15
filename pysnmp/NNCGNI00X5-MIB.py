# SNMP MIB module (NNCGNI00X5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCGNI00X5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:27 2024
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

(nncExtDs1,) = mibBuilder.importSymbols(
    "NNCGNI00X1-SMI",
    "nncExtDs1")

(CircuitIndex,
 PortIndex) = mibBuilder.importSymbols(
    "NNCGNI00X7-MIB",
    "CircuitIndex",
    "PortIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Ds1LineIndex(Integer32):
    """Custom type Ds1LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class Ds1IntervalIndex(Integer32):
    """Custom type Ds1IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )





class DebounceInterval(Integer32):
    """Custom type DebounceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncExtDs1ConfigTable_Object = MibTable
nncExtDs1ConfigTable = _NncExtDs1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1)
)
if mibBuilder.loadTexts:
    nncExtDs1ConfigTable.setStatus("mandatory")
_NncExtDs1ConfigEntry_Object = MibTableRow
nncExtDs1ConfigEntry = _NncExtDs1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1)
)
nncExtDs1ConfigEntry.setIndexNames(
    (0, "NNCGNI00X5-MIB", "nncExtDs1ConfigIndex"),
)
if mibBuilder.loadTexts:
    nncExtDs1ConfigEntry.setStatus("mandatory")
_NncExtDs1ConfigIndex_Type = Ds1LineIndex
_NncExtDs1ConfigIndex_Object = MibTableColumn
nncExtDs1ConfigIndex = _NncExtDs1ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 1),
    _NncExtDs1ConfigIndex_Type()
)
nncExtDs1ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1ConfigIndex.setStatus("mandatory")


class _NncExtDs1LineLength_Type(Integer32):
    """Custom type nncExtDs1LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("long", 3),
          ("medium", 2),
          ("short", 1))
    )


_NncExtDs1LineLength_Type.__name__ = "Integer32"
_NncExtDs1LineLength_Object = MibTableColumn
nncExtDs1LineLength = _NncExtDs1LineLength_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 2),
    _NncExtDs1LineLength_Type()
)
nncExtDs1LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1LineLength.setStatus("mandatory")


class _NncExtDs1LineStatus_Type(Integer32):
    """Custom type nncExtDs1LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_NncExtDs1LineStatus_Type.__name__ = "Integer32"
_NncExtDs1LineStatus_Object = MibTableColumn
nncExtDs1LineStatus = _NncExtDs1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 3),
    _NncExtDs1LineStatus_Type()
)
nncExtDs1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1LineStatus.setStatus("mandatory")


class _NncExtDs1TrunkCondEnable_Type(Integer32):
    """Custom type nncExtDs1TrunkCondEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NncExtDs1TrunkCondEnable_Type.__name__ = "Integer32"
_NncExtDs1TrunkCondEnable_Object = MibTableColumn
nncExtDs1TrunkCondEnable = _NncExtDs1TrunkCondEnable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 4),
    _NncExtDs1TrunkCondEnable_Type()
)
nncExtDs1TrunkCondEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1TrunkCondEnable.setStatus("mandatory")


class _NncExtDs1LossOfFrameConditioning_Type(Integer32):
    """Custom type nncExtDs1LossOfFrameConditioning based on Integer32"""
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


_NncExtDs1LossOfFrameConditioning_Type.__name__ = "Integer32"
_NncExtDs1LossOfFrameConditioning_Object = MibTableColumn
nncExtDs1LossOfFrameConditioning = _NncExtDs1LossOfFrameConditioning_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 5),
    _NncExtDs1LossOfFrameConditioning_Type()
)
nncExtDs1LossOfFrameConditioning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1LossOfFrameConditioning.setStatus("mandatory")


class _NncExtDs1DistantLossOfFrameConditioning_Type(Integer32):
    """Custom type nncExtDs1DistantLossOfFrameConditioning based on Integer32"""
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


_NncExtDs1DistantLossOfFrameConditioning_Type.__name__ = "Integer32"
_NncExtDs1DistantLossOfFrameConditioning_Object = MibTableColumn
nncExtDs1DistantLossOfFrameConditioning = _NncExtDs1DistantLossOfFrameConditioning_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 6),
    _NncExtDs1DistantLossOfFrameConditioning_Type()
)
nncExtDs1DistantLossOfFrameConditioning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1DistantLossOfFrameConditioning.setStatus("mandatory")


class _NncExtDs1FailedStateConditioning_Type(Integer32):
    """Custom type nncExtDs1FailedStateConditioning based on Integer32"""
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


_NncExtDs1FailedStateConditioning_Type.__name__ = "Integer32"
_NncExtDs1FailedStateConditioning_Object = MibTableColumn
nncExtDs1FailedStateConditioning = _NncExtDs1FailedStateConditioning_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 7),
    _NncExtDs1FailedStateConditioning_Type()
)
nncExtDs1FailedStateConditioning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1FailedStateConditioning.setStatus("mandatory")


class _NncExtDs1ErrorRateConditioning_Type(Integer32):
    """Custom type nncExtDs1ErrorRateConditioning based on Integer32"""
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


_NncExtDs1ErrorRateConditioning_Type.__name__ = "Integer32"
_NncExtDs1ErrorRateConditioning_Object = MibTableColumn
nncExtDs1ErrorRateConditioning = _NncExtDs1ErrorRateConditioning_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 8),
    _NncExtDs1ErrorRateConditioning_Type()
)
nncExtDs1ErrorRateConditioning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1ErrorRateConditioning.setStatus("mandatory")


class _NncExtDs1CSULoopbackConditioning_Type(Integer32):
    """Custom type nncExtDs1CSULoopbackConditioning based on Integer32"""
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


_NncExtDs1CSULoopbackConditioning_Type.__name__ = "Integer32"
_NncExtDs1CSULoopbackConditioning_Object = MibTableColumn
nncExtDs1CSULoopbackConditioning = _NncExtDs1CSULoopbackConditioning_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 9),
    _NncExtDs1CSULoopbackConditioning_Type()
)
nncExtDs1CSULoopbackConditioning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1CSULoopbackConditioning.setStatus("mandatory")
_NncExtDs1AlarmDeclareTime_Type = DebounceInterval
_NncExtDs1AlarmDeclareTime_Object = MibTableColumn
nncExtDs1AlarmDeclareTime = _NncExtDs1AlarmDeclareTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 10),
    _NncExtDs1AlarmDeclareTime_Type()
)
nncExtDs1AlarmDeclareTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1AlarmDeclareTime.setStatus("mandatory")
_NncExtDs1AlarmClearTime_Type = DebounceInterval
_NncExtDs1AlarmClearTime_Object = MibTableColumn
nncExtDs1AlarmClearTime = _NncExtDs1AlarmClearTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 11),
    _NncExtDs1AlarmClearTime_Type()
)
nncExtDs1AlarmClearTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1AlarmClearTime.setStatus("mandatory")


class _NncExtDs1UseCRCOnReframe_Type(Integer32):
    """Custom type nncExtDs1UseCRCOnReframe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_NncExtDs1UseCRCOnReframe_Type.__name__ = "Integer32"
_NncExtDs1UseCRCOnReframe_Object = MibTableColumn
nncExtDs1UseCRCOnReframe = _NncExtDs1UseCRCOnReframe_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 12),
    _NncExtDs1UseCRCOnReframe_Type()
)
nncExtDs1UseCRCOnReframe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1UseCRCOnReframe.setStatus("mandatory")


class _NncExtDs1WorstInterval_Type(Integer32):
    """Custom type nncExtDs1WorstInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncExtDs1WorstInterval_Type.__name__ = "Integer32"
_NncExtDs1WorstInterval_Object = MibTableColumn
nncExtDs1WorstInterval = _NncExtDs1WorstInterval_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 13),
    _NncExtDs1WorstInterval_Type()
)
nncExtDs1WorstInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstInterval.setStatus("mandatory")


class _NncExtDs1ErrorEvents_Type(Integer32):
    """Custom type nncExtDs1ErrorEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NncExtDs1ErrorEvents_Type.__name__ = "Integer32"
_NncExtDs1ErrorEvents_Object = MibTableColumn
nncExtDs1ErrorEvents = _NncExtDs1ErrorEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 14),
    _NncExtDs1ErrorEvents_Type()
)
nncExtDs1ErrorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1ErrorEvents.setStatus("mandatory")


class _NncExtDs181XXCompatibility_Type(Integer32):
    """Custom type nncExtDs181XXCompatibility based on Integer32"""
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


_NncExtDs181XXCompatibility_Type.__name__ = "Integer32"
_NncExtDs181XXCompatibility_Object = MibTableColumn
nncExtDs181XXCompatibility = _NncExtDs181XXCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 15),
    _NncExtDs181XXCompatibility_Type()
)
nncExtDs181XXCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs181XXCompatibility.setStatus("mandatory")


class _NncExtDs1LoopbackConfig_Type(Integer32):
    """Custom type nncExtDs1LoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("equipment", 2),
          ("line", 5),
          ("none", 1))
    )


_NncExtDs1LoopbackConfig_Type.__name__ = "Integer32"
_NncExtDs1LoopbackConfig_Object = MibTableColumn
nncExtDs1LoopbackConfig = _NncExtDs1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 16),
    _NncExtDs1LoopbackConfig_Type()
)
nncExtDs1LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1LoopbackConfig.setStatus("mandatory")


class _NncExtDs1E1TrunkCondEnable_Type(Integer32):
    """Custom type nncExtDs1E1TrunkCondEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NncExtDs1E1TrunkCondEnable_Type.__name__ = "Integer32"
_NncExtDs1E1TrunkCondEnable_Object = MibTableColumn
nncExtDs1E1TrunkCondEnable = _NncExtDs1E1TrunkCondEnable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 17),
    _NncExtDs1E1TrunkCondEnable_Type()
)
nncExtDs1E1TrunkCondEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1E1TrunkCondEnable.setStatus("deprecated")
_NncExtDs1E1ConfigTable_Object = MibTable
nncExtDs1E1ConfigTable = _NncExtDs1E1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 2)
)
if mibBuilder.loadTexts:
    nncExtDs1E1ConfigTable.setStatus("mandatory")
_NncExtDs1E1ConfigEntry_Object = MibTableRow
nncExtDs1E1ConfigEntry = _NncExtDs1E1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 2, 1)
)
nncExtDs1E1ConfigEntry.setIndexNames(
    (0, "NNCGNI00X5-MIB", "nncExtDs1E1Index"),
)
if mibBuilder.loadTexts:
    nncExtDs1E1ConfigEntry.setStatus("mandatory")
_NncExtDs1E1Index_Type = Ds1LineIndex
_NncExtDs1E1Index_Object = MibTableColumn
nncExtDs1E1Index = _NncExtDs1E1Index_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 2, 1, 1),
    _NncExtDs1E1Index_Type()
)
nncExtDs1E1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1E1Index.setStatus("mandatory")


class _NncExtDs1E1TransmitShieldStatus_Type(Integer32):
    """Custom type nncExtDs1E1TransmitShieldStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("earthed", 1),
          ("floating", 2),
          ("notApplicable", 3))
    )


_NncExtDs1E1TransmitShieldStatus_Type.__name__ = "Integer32"
_NncExtDs1E1TransmitShieldStatus_Object = MibTableColumn
nncExtDs1E1TransmitShieldStatus = _NncExtDs1E1TransmitShieldStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 2, 1, 2),
    _NncExtDs1E1TransmitShieldStatus_Type()
)
nncExtDs1E1TransmitShieldStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1E1TransmitShieldStatus.setStatus("mandatory")


class _NncExtDs1E1ReceivedShieldStatus_Type(Integer32):
    """Custom type nncExtDs1E1ReceivedShieldStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("earthed", 1),
          ("floating", 2),
          ("notApplicable", 3))
    )


_NncExtDs1E1ReceivedShieldStatus_Type.__name__ = "Integer32"
_NncExtDs1E1ReceivedShieldStatus_Object = MibTableColumn
nncExtDs1E1ReceivedShieldStatus = _NncExtDs1E1ReceivedShieldStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 2, 1, 3),
    _NncExtDs1E1ReceivedShieldStatus_Type()
)
nncExtDs1E1ReceivedShieldStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1E1ReceivedShieldStatus.setStatus("mandatory")


class _NncExtDs1E1StatisticsType_Type(Integer32):
    """Custom type nncExtDs1E1StatisticsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc4", 2),
          ("hdb3", 1))
    )


_NncExtDs1E1StatisticsType_Type.__name__ = "Integer32"
_NncExtDs1E1StatisticsType_Object = MibTableColumn
nncExtDs1E1StatisticsType = _NncExtDs1E1StatisticsType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 2, 1, 4),
    _NncExtDs1E1StatisticsType_Type()
)
nncExtDs1E1StatisticsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1E1StatisticsType.setStatus("mandatory")
_NncExtDs1G821StatisticsTable_Object = MibTable
nncExtDs1G821StatisticsTable = _NncExtDs1G821StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 3)
)
if mibBuilder.loadTexts:
    nncExtDs1G821StatisticsTable.setStatus("mandatory")
_NncExtDs1G821StatisticsEntry_Object = MibTableRow
nncExtDs1G821StatisticsEntry = _NncExtDs1G821StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1)
)
nncExtDs1G821StatisticsEntry.setIndexNames(
    (0, "NNCGNI00X5-MIB", "nncG821Index"),
)
if mibBuilder.loadTexts:
    nncExtDs1G821StatisticsEntry.setStatus("mandatory")
_NncG821Index_Type = Ds1LineIndex
_NncG821Index_Object = MibTableColumn
nncG821Index = _NncG821Index_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 1),
    _NncG821Index_Type()
)
nncG821Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncG821Index.setStatus("mandatory")
_NncG821DegradedMinutes_Type = Counter32
_NncG821DegradedMinutes_Object = MibTableColumn
nncG821DegradedMinutes = _NncG821DegradedMinutes_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 2),
    _NncG821DegradedMinutes_Type()
)
nncG821DegradedMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncG821DegradedMinutes.setStatus("mandatory")
_NncG821ErroredSeconds_Type = Counter32
_NncG821ErroredSeconds_Object = MibTableColumn
nncG821ErroredSeconds = _NncG821ErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 3),
    _NncG821ErroredSeconds_Type()
)
nncG821ErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncG821ErroredSeconds.setStatus("mandatory")
_NncG821SeverelyErroredSeconds_Type = Counter32
_NncG821SeverelyErroredSeconds_Object = MibTableColumn
nncG821SeverelyErroredSeconds = _NncG821SeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 4),
    _NncG821SeverelyErroredSeconds_Type()
)
nncG821SeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncG821SeverelyErroredSeconds.setStatus("mandatory")
_NncG821UnavailableSeconds_Type = Counter32
_NncG821UnavailableSeconds_Object = MibTableColumn
nncG821UnavailableSeconds = _NncG821UnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 5),
    _NncG821UnavailableSeconds_Type()
)
nncG821UnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncG821UnavailableSeconds.setStatus("mandatory")
_NncG821TotalSeconds_Type = Counter32
_NncG821TotalSeconds_Object = MibTableColumn
nncG821TotalSeconds = _NncG821TotalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 6),
    _NncG821TotalSeconds_Type()
)
nncG821TotalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncG821TotalSeconds.setStatus("mandatory")
_NncExtDs1IntervalTable_Object = MibTable
nncExtDs1IntervalTable = _NncExtDs1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 4)
)
if mibBuilder.loadTexts:
    nncExtDs1IntervalTable.setStatus("mandatory")
_NncExtDs1IntervalEntry_Object = MibTableRow
nncExtDs1IntervalEntry = _NncExtDs1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 4, 1)
)
nncExtDs1IntervalEntry.setIndexNames(
    (0, "NNCGNI00X5-MIB", "nncExtDs1IntervalIndex"),
    (0, "NNCGNI00X5-MIB", "nncExtDs1IntervalNumber"),
)
if mibBuilder.loadTexts:
    nncExtDs1IntervalEntry.setStatus("mandatory")
_NncExtDs1IntervalIndex_Type = Ds1LineIndex
_NncExtDs1IntervalIndex_Object = MibTableColumn
nncExtDs1IntervalIndex = _NncExtDs1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 4, 1, 1),
    _NncExtDs1IntervalIndex_Type()
)
nncExtDs1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1IntervalIndex.setStatus("mandatory")


class _NncExtDs1IntervalNumber_Type(Integer32):
    """Custom type nncExtDs1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncExtDs1IntervalNumber_Type.__name__ = "Integer32"
_NncExtDs1IntervalNumber_Object = MibTableColumn
nncExtDs1IntervalNumber = _NncExtDs1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 4, 1, 2),
    _NncExtDs1IntervalNumber_Type()
)
nncExtDs1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1IntervalNumber.setStatus("mandatory")
_NncExtDs1IntervalLOFC_Type = Gauge32
_NncExtDs1IntervalLOFC_Object = MibTableColumn
nncExtDs1IntervalLOFC = _NncExtDs1IntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 4, 1, 3),
    _NncExtDs1IntervalLOFC_Type()
)
nncExtDs1IntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1IntervalLOFC.setStatus("mandatory")
_NncExtDs1TotalTable_Object = MibTable
nncExtDs1TotalTable = _NncExtDs1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 5)
)
if mibBuilder.loadTexts:
    nncExtDs1TotalTable.setStatus("mandatory")
_NncExtDs1TotalEntry_Object = MibTableRow
nncExtDs1TotalEntry = _NncExtDs1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 5, 1)
)
nncExtDs1TotalEntry.setIndexNames(
    (0, "NNCGNI00X5-MIB", "nncExtDs1TotalIndex"),
)
if mibBuilder.loadTexts:
    nncExtDs1TotalEntry.setStatus("mandatory")
_NncExtDs1TotalIndex_Type = Ds1LineIndex
_NncExtDs1TotalIndex_Object = MibTableColumn
nncExtDs1TotalIndex = _NncExtDs1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 5, 1, 1),
    _NncExtDs1TotalIndex_Type()
)
nncExtDs1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1TotalIndex.setStatus("mandatory")
_NncExtDs1TotalLOFC_Type = Gauge32
_NncExtDs1TotalLOFC_Object = MibTableColumn
nncExtDs1TotalLOFC = _NncExtDs1TotalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 5, 1, 2),
    _NncExtDs1TotalLOFC_Type()
)
nncExtDs1TotalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1TotalLOFC.setStatus("mandatory")
_NncExtDs1WorstIntervalTable_Object = MibTable
nncExtDs1WorstIntervalTable = _NncExtDs1WorstIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6)
)
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalTable.setStatus("mandatory")
_NncExtDs1WorstIntervalEntry_Object = MibTableRow
nncExtDs1WorstIntervalEntry = _NncExtDs1WorstIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1)
)
nncExtDs1WorstIntervalEntry.setIndexNames(
    (0, "NNCGNI00X5-MIB", "nncExtDs1WorstIntervalIndex"),
)
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalEntry.setStatus("mandatory")
_NncExtDs1WorstIntervalIndex_Type = Ds1LineIndex
_NncExtDs1WorstIntervalIndex_Object = MibTableColumn
nncExtDs1WorstIntervalIndex = _NncExtDs1WorstIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 1),
    _NncExtDs1WorstIntervalIndex_Type()
)
nncExtDs1WorstIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalIndex.setStatus("mandatory")
_NncExtDs1WorstIntervalBESs_Type = Gauge32
_NncExtDs1WorstIntervalBESs_Object = MibTableColumn
nncExtDs1WorstIntervalBESs = _NncExtDs1WorstIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 2),
    _NncExtDs1WorstIntervalBESs_Type()
)
nncExtDs1WorstIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalBESs.setStatus("mandatory")
_NncExtDs1WorstIntervalLOFC_Type = Gauge32
_NncExtDs1WorstIntervalLOFC_Object = MibTableColumn
nncExtDs1WorstIntervalLOFC = _NncExtDs1WorstIntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 3),
    _NncExtDs1WorstIntervalLOFC_Type()
)
nncExtDs1WorstIntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalLOFC.setStatus("mandatory")
_NncExtDs1WorstIntervalESs_Type = Gauge32
_NncExtDs1WorstIntervalESs_Object = MibTableColumn
nncExtDs1WorstIntervalESs = _NncExtDs1WorstIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 4),
    _NncExtDs1WorstIntervalESs_Type()
)
nncExtDs1WorstIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalESs.setStatus("mandatory")
_NncExtDs1WorstIntervalSESs_Type = Gauge32
_NncExtDs1WorstIntervalSESs_Object = MibTableColumn
nncExtDs1WorstIntervalSESs = _NncExtDs1WorstIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 5),
    _NncExtDs1WorstIntervalSESs_Type()
)
nncExtDs1WorstIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalSESs.setStatus("mandatory")
_NncExtDs1WorstIntervalSEFSs_Type = Gauge32
_NncExtDs1WorstIntervalSEFSs_Object = MibTableColumn
nncExtDs1WorstIntervalSEFSs = _NncExtDs1WorstIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 6),
    _NncExtDs1WorstIntervalSEFSs_Type()
)
nncExtDs1WorstIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalSEFSs.setStatus("mandatory")
_NncExtDs1WorstIntervalUASs_Type = Gauge32
_NncExtDs1WorstIntervalUASs_Object = MibTableColumn
nncExtDs1WorstIntervalUASs = _NncExtDs1WorstIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 7),
    _NncExtDs1WorstIntervalUASs_Type()
)
nncExtDs1WorstIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalUASs.setStatus("mandatory")
_NncExtDs1WorstIntervalCSSs_Type = Gauge32
_NncExtDs1WorstIntervalCSSs_Object = MibTableColumn
nncExtDs1WorstIntervalCSSs = _NncExtDs1WorstIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 8),
    _NncExtDs1WorstIntervalCSSs_Type()
)
nncExtDs1WorstIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalCSSs.setStatus("mandatory")
_NncExtDs1WorstIntervalBPVs_Type = Gauge32
_NncExtDs1WorstIntervalBPVs_Object = MibTableColumn
nncExtDs1WorstIntervalBPVs = _NncExtDs1WorstIntervalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 9),
    _NncExtDs1WorstIntervalBPVs_Type()
)
nncExtDs1WorstIntervalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalBPVs.setStatus("mandatory")
_NncExtDs1WorstIntervalCVs_Type = Gauge32
_NncExtDs1WorstIntervalCVs_Object = MibTableColumn
nncExtDs1WorstIntervalCVs = _NncExtDs1WorstIntervalCVs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 10),
    _NncExtDs1WorstIntervalCVs_Type()
)
nncExtDs1WorstIntervalCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalCVs.setStatus("mandatory")
_NncExtDs1WorstIntervalLESs_Type = Gauge32
_NncExtDs1WorstIntervalLESs_Object = MibTableColumn
nncExtDs1WorstIntervalLESs = _NncExtDs1WorstIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 11),
    _NncExtDs1WorstIntervalLESs_Type()
)
nncExtDs1WorstIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1WorstIntervalLESs.setStatus("mandatory")
_NncExtDs1CircuitTable_Object = MibTable
nncExtDs1CircuitTable = _NncExtDs1CircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7)
)
if mibBuilder.loadTexts:
    nncExtDs1CircuitTable.setStatus("mandatory")
_NncExtDs1CircuitEntry_Object = MibTableRow
nncExtDs1CircuitEntry = _NncExtDs1CircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1)
)
nncExtDs1CircuitEntry.setIndexNames(
    (0, "NNCGNI00X5-MIB", "nncExtDs1CctIndex"),
    (0, "NNCGNI00X5-MIB", "nncExtDs1CctPortNumber"),
    (0, "NNCGNI00X5-MIB", "nncExtDs1CctNumber"),
)
if mibBuilder.loadTexts:
    nncExtDs1CircuitEntry.setStatus("mandatory")
_NncExtDs1CctIndex_Type = Ds1LineIndex
_NncExtDs1CctIndex_Object = MibTableColumn
nncExtDs1CctIndex = _NncExtDs1CctIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 1),
    _NncExtDs1CctIndex_Type()
)
nncExtDs1CctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1CctIndex.setStatus("mandatory")


class _NncExtDs1CctPortNumber_Type(Integer32):
    """Custom type nncExtDs1CctPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NncExtDs1CctPortNumber_Type.__name__ = "Integer32"
_NncExtDs1CctPortNumber_Object = MibTableColumn
nncExtDs1CctPortNumber = _NncExtDs1CctPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 2),
    _NncExtDs1CctPortNumber_Type()
)
nncExtDs1CctPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1CctPortNumber.setStatus("mandatory")


class _NncExtDs1CctNumber_Type(Integer32):
    """Custom type nncExtDs1CctNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_NncExtDs1CctNumber_Type.__name__ = "Integer32"
_NncExtDs1CctNumber_Object = MibTableColumn
nncExtDs1CctNumber = _NncExtDs1CctNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 3),
    _NncExtDs1CctNumber_Type()
)
nncExtDs1CctNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1CctNumber.setStatus("mandatory")


class _NncExtDs1CctUseRBS_Type(Integer32):
    """Custom type nncExtDs1CctUseRBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rbsOff", 2),
          ("rbsOn", 1))
    )


_NncExtDs1CctUseRBS_Type.__name__ = "Integer32"
_NncExtDs1CctUseRBS_Object = MibTableColumn
nncExtDs1CctUseRBS = _NncExtDs1CctUseRBS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 4),
    _NncExtDs1CctUseRBS_Type()
)
nncExtDs1CctUseRBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1CctUseRBS.setStatus("mandatory")


class _NncExtDs1CctDataInversion_Type(Integer32):
    """Custom type nncExtDs1CctDataInversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invertOff", 2),
          ("invertOn", 1))
    )


_NncExtDs1CctDataInversion_Type.__name__ = "Integer32"
_NncExtDs1CctDataInversion_Object = MibTableColumn
nncExtDs1CctDataInversion = _NncExtDs1CctDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 5),
    _NncExtDs1CctDataInversion_Type()
)
nncExtDs1CctDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1CctDataInversion.setStatus("mandatory")


class _NncExtDs1CctDefaultData_Type(Integer32):
    """Custom type nncExtDs1CctDefaultData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NncExtDs1CctDefaultData_Type.__name__ = "Integer32"
_NncExtDs1CctDefaultData_Object = MibTableColumn
nncExtDs1CctDefaultData = _NncExtDs1CctDefaultData_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 6),
    _NncExtDs1CctDefaultData_Type()
)
nncExtDs1CctDefaultData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1CctDefaultData.setStatus("mandatory")


class _NncExtDs1CctFirstCode_Type(Integer32):
    """Custom type nncExtDs1CctFirstCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NncExtDs1CctFirstCode_Type.__name__ = "Integer32"
_NncExtDs1CctFirstCode_Object = MibTableColumn
nncExtDs1CctFirstCode = _NncExtDs1CctFirstCode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 7),
    _NncExtDs1CctFirstCode_Type()
)
nncExtDs1CctFirstCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1CctFirstCode.setStatus("mandatory")


class _NncExtDs1CctSecondCode_Type(Integer32):
    """Custom type nncExtDs1CctSecondCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NncExtDs1CctSecondCode_Type.__name__ = "Integer32"
_NncExtDs1CctSecondCode_Object = MibTableColumn
nncExtDs1CctSecondCode = _NncExtDs1CctSecondCode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 8),
    _NncExtDs1CctSecondCode_Type()
)
nncExtDs1CctSecondCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1CctSecondCode.setStatus("mandatory")


class _NncExtDs1CctBitsToUse_Type(Integer32):
    """Custom type nncExtDs1CctBitsToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NncExtDs1CctBitsToUse_Type.__name__ = "Integer32"
_NncExtDs1CctBitsToUse_Object = MibTableColumn
nncExtDs1CctBitsToUse = _NncExtDs1CctBitsToUse_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 9),
    _NncExtDs1CctBitsToUse_Type()
)
nncExtDs1CctBitsToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1CctBitsToUse.setStatus("mandatory")


class _NncExtDs1CctSuperRateMap_Type(Integer32):
    """Custom type nncExtDs1CctSuperRateMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NncExtDs1CctSuperRateMap_Type.__name__ = "Integer32"
_NncExtDs1CctSuperRateMap_Object = MibTableColumn
nncExtDs1CctSuperRateMap = _NncExtDs1CctSuperRateMap_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 10),
    _NncExtDs1CctSuperRateMap_Type()
)
nncExtDs1CctSuperRateMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1CctSuperRateMap.setStatus("mandatory")


class _NncExtDs1CctFaultSignalling_Type(Integer32):
    """Custom type nncExtDs1CctFaultSignalling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("none", 3),
          ("seized", 2))
    )


_NncExtDs1CctFaultSignalling_Type.__name__ = "Integer32"
_NncExtDs1CctFaultSignalling_Object = MibTableColumn
nncExtDs1CctFaultSignalling = _NncExtDs1CctFaultSignalling_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 11),
    _NncExtDs1CctFaultSignalling_Type()
)
nncExtDs1CctFaultSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtDs1CctFaultSignalling.setStatus("mandatory")
_NncExtDs1CurrentTable_Object = MibTable
nncExtDs1CurrentTable = _NncExtDs1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 8)
)
if mibBuilder.loadTexts:
    nncExtDs1CurrentTable.setStatus("mandatory")
_NncExtDs1CurrentEntry_Object = MibTableRow
nncExtDs1CurrentEntry = _NncExtDs1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 8, 1)
)
nncExtDs1CurrentEntry.setIndexNames(
    (0, "NNCGNI00X5-MIB", "nncExtDs1CurrentIndex"),
)
if mibBuilder.loadTexts:
    nncExtDs1CurrentEntry.setStatus("mandatory")
_NncExtDs1CurrentIndex_Type = Ds1LineIndex
_NncExtDs1CurrentIndex_Object = MibTableColumn
nncExtDs1CurrentIndex = _NncExtDs1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 8, 1, 1),
    _NncExtDs1CurrentIndex_Type()
)
nncExtDs1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1CurrentIndex.setStatus("mandatory")
_NncExtDs1CurrentLOFC_Type = Gauge32
_NncExtDs1CurrentLOFC_Object = MibTableColumn
nncExtDs1CurrentLOFC = _NncExtDs1CurrentLOFC_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 10, 8, 1, 2),
    _NncExtDs1CurrentLOFC_Type()
)
nncExtDs1CurrentLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtDs1CurrentLOFC.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCGNI00X5-MIB",
    **{"Ds1LineIndex": Ds1LineIndex,
       "Ds1IntervalIndex": Ds1IntervalIndex,
       "DebounceInterval": DebounceInterval,
       "nncExtDs1ConfigTable": nncExtDs1ConfigTable,
       "nncExtDs1ConfigEntry": nncExtDs1ConfigEntry,
       "nncExtDs1ConfigIndex": nncExtDs1ConfigIndex,
       "nncExtDs1LineLength": nncExtDs1LineLength,
       "nncExtDs1LineStatus": nncExtDs1LineStatus,
       "nncExtDs1TrunkCondEnable": nncExtDs1TrunkCondEnable,
       "nncExtDs1LossOfFrameConditioning": nncExtDs1LossOfFrameConditioning,
       "nncExtDs1DistantLossOfFrameConditioning": nncExtDs1DistantLossOfFrameConditioning,
       "nncExtDs1FailedStateConditioning": nncExtDs1FailedStateConditioning,
       "nncExtDs1ErrorRateConditioning": nncExtDs1ErrorRateConditioning,
       "nncExtDs1CSULoopbackConditioning": nncExtDs1CSULoopbackConditioning,
       "nncExtDs1AlarmDeclareTime": nncExtDs1AlarmDeclareTime,
       "nncExtDs1AlarmClearTime": nncExtDs1AlarmClearTime,
       "nncExtDs1UseCRCOnReframe": nncExtDs1UseCRCOnReframe,
       "nncExtDs1WorstInterval": nncExtDs1WorstInterval,
       "nncExtDs1ErrorEvents": nncExtDs1ErrorEvents,
       "nncExtDs181XXCompatibility": nncExtDs181XXCompatibility,
       "nncExtDs1LoopbackConfig": nncExtDs1LoopbackConfig,
       "nncExtDs1E1TrunkCondEnable": nncExtDs1E1TrunkCondEnable,
       "nncExtDs1E1ConfigTable": nncExtDs1E1ConfigTable,
       "nncExtDs1E1ConfigEntry": nncExtDs1E1ConfigEntry,
       "nncExtDs1E1Index": nncExtDs1E1Index,
       "nncExtDs1E1TransmitShieldStatus": nncExtDs1E1TransmitShieldStatus,
       "nncExtDs1E1ReceivedShieldStatus": nncExtDs1E1ReceivedShieldStatus,
       "nncExtDs1E1StatisticsType": nncExtDs1E1StatisticsType,
       "nncExtDs1G821StatisticsTable": nncExtDs1G821StatisticsTable,
       "nncExtDs1G821StatisticsEntry": nncExtDs1G821StatisticsEntry,
       "nncG821Index": nncG821Index,
       "nncG821DegradedMinutes": nncG821DegradedMinutes,
       "nncG821ErroredSeconds": nncG821ErroredSeconds,
       "nncG821SeverelyErroredSeconds": nncG821SeverelyErroredSeconds,
       "nncG821UnavailableSeconds": nncG821UnavailableSeconds,
       "nncG821TotalSeconds": nncG821TotalSeconds,
       "nncExtDs1IntervalTable": nncExtDs1IntervalTable,
       "nncExtDs1IntervalEntry": nncExtDs1IntervalEntry,
       "nncExtDs1IntervalIndex": nncExtDs1IntervalIndex,
       "nncExtDs1IntervalNumber": nncExtDs1IntervalNumber,
       "nncExtDs1IntervalLOFC": nncExtDs1IntervalLOFC,
       "nncExtDs1TotalTable": nncExtDs1TotalTable,
       "nncExtDs1TotalEntry": nncExtDs1TotalEntry,
       "nncExtDs1TotalIndex": nncExtDs1TotalIndex,
       "nncExtDs1TotalLOFC": nncExtDs1TotalLOFC,
       "nncExtDs1WorstIntervalTable": nncExtDs1WorstIntervalTable,
       "nncExtDs1WorstIntervalEntry": nncExtDs1WorstIntervalEntry,
       "nncExtDs1WorstIntervalIndex": nncExtDs1WorstIntervalIndex,
       "nncExtDs1WorstIntervalBESs": nncExtDs1WorstIntervalBESs,
       "nncExtDs1WorstIntervalLOFC": nncExtDs1WorstIntervalLOFC,
       "nncExtDs1WorstIntervalESs": nncExtDs1WorstIntervalESs,
       "nncExtDs1WorstIntervalSESs": nncExtDs1WorstIntervalSESs,
       "nncExtDs1WorstIntervalSEFSs": nncExtDs1WorstIntervalSEFSs,
       "nncExtDs1WorstIntervalUASs": nncExtDs1WorstIntervalUASs,
       "nncExtDs1WorstIntervalCSSs": nncExtDs1WorstIntervalCSSs,
       "nncExtDs1WorstIntervalBPVs": nncExtDs1WorstIntervalBPVs,
       "nncExtDs1WorstIntervalCVs": nncExtDs1WorstIntervalCVs,
       "nncExtDs1WorstIntervalLESs": nncExtDs1WorstIntervalLESs,
       "nncExtDs1CircuitTable": nncExtDs1CircuitTable,
       "nncExtDs1CircuitEntry": nncExtDs1CircuitEntry,
       "nncExtDs1CctIndex": nncExtDs1CctIndex,
       "nncExtDs1CctPortNumber": nncExtDs1CctPortNumber,
       "nncExtDs1CctNumber": nncExtDs1CctNumber,
       "nncExtDs1CctUseRBS": nncExtDs1CctUseRBS,
       "nncExtDs1CctDataInversion": nncExtDs1CctDataInversion,
       "nncExtDs1CctDefaultData": nncExtDs1CctDefaultData,
       "nncExtDs1CctFirstCode": nncExtDs1CctFirstCode,
       "nncExtDs1CctSecondCode": nncExtDs1CctSecondCode,
       "nncExtDs1CctBitsToUse": nncExtDs1CctBitsToUse,
       "nncExtDs1CctSuperRateMap": nncExtDs1CctSuperRateMap,
       "nncExtDs1CctFaultSignalling": nncExtDs1CctFaultSignalling,
       "nncExtDs1CurrentTable": nncExtDs1CurrentTable,
       "nncExtDs1CurrentEntry": nncExtDs1CurrentEntry,
       "nncExtDs1CurrentIndex": nncExtDs1CurrentIndex,
       "nncExtDs1CurrentLOFC": nncExtDs1CurrentLOFC}
)
