# SNMP MIB module (CISCO-WIRELESS-DOCS-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WIRELESS-DOCS-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:34 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CwrdBm,) = mibBuilder.importSymbols(
    "CISCO-WIRELESS-TC-MIB",
    "CwrdBm")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoWirelessDocsIfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 167)
)
ciscoWirelessDocsIfMib.setRevisions(
        ("2005-12-27 10:03",
         "2000-06-07 10:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CwdIfMibObjects_ObjectIdentity = ObjectIdentity
cwdIfMibObjects = _CwdIfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1)
)
_CwdIfBaseObjects_ObjectIdentity = ObjectIdentity
cwdIfBaseObjects = _CwdIfBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1)
)
_CwdIfChannelTable_Object = MibTable
cwdIfChannelTable = _CwdIfChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwdIfChannelTable.setStatus("current")
_CwdIfChannelEntry_Object = MibTableRow
cwdIfChannelEntry = _CwdIfChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 1, 1)
)
cwdIfChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwdIfChannelEntry.setStatus("current")


class _CwdIfChannelUpFrequency_Type(Integer32):
    """Custom type cwdIfChannelUpFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_CwdIfChannelUpFrequency_Type.__name__ = "Integer32"
_CwdIfChannelUpFrequency_Object = MibTableColumn
cwdIfChannelUpFrequency = _CwdIfChannelUpFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 1, 1, 1),
    _CwdIfChannelUpFrequency_Type()
)
cwdIfChannelUpFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfChannelUpFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfChannelUpFrequency.setUnits("kHz")


class _CwdIfChannelUpWidth_Type(Integer32):
    """Custom type cwdIfChannelUpWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_CwdIfChannelUpWidth_Type.__name__ = "Integer32"
_CwdIfChannelUpWidth_Object = MibTableColumn
cwdIfChannelUpWidth = _CwdIfChannelUpWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 1, 1, 2),
    _CwdIfChannelUpWidth_Type()
)
cwdIfChannelUpWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfChannelUpWidth.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfChannelUpWidth.setUnits("kHz")


class _CwdIfChannelDownFrequency_Type(Integer32):
    """Custom type cwdIfChannelDownFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_CwdIfChannelDownFrequency_Type.__name__ = "Integer32"
_CwdIfChannelDownFrequency_Object = MibTableColumn
cwdIfChannelDownFrequency = _CwdIfChannelDownFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 1, 1, 3),
    _CwdIfChannelDownFrequency_Type()
)
cwdIfChannelDownFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfChannelDownFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfChannelDownFrequency.setUnits("kHz")


class _CwdIfChannelDownWidth_Type(Integer32):
    """Custom type cwdIfChannelDownWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_CwdIfChannelDownWidth_Type.__name__ = "Integer32"
_CwdIfChannelDownWidth_Object = MibTableColumn
cwdIfChannelDownWidth = _CwdIfChannelDownWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 1, 1, 4),
    _CwdIfChannelDownWidth_Type()
)
cwdIfChannelDownWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfChannelDownWidth.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfChannelDownWidth.setUnits("kHz")


class _CwdIfChannelMiniSlotTimeBaseTick_Type(Integer32):
    """Custom type cwdIfChannelMiniSlotTimeBaseTick based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 102400000),
    )


_CwdIfChannelMiniSlotTimeBaseTick_Type.__name__ = "Integer32"
_CwdIfChannelMiniSlotTimeBaseTick_Object = MibTableColumn
cwdIfChannelMiniSlotTimeBaseTick = _CwdIfChannelMiniSlotTimeBaseTick_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 1, 1, 5),
    _CwdIfChannelMiniSlotTimeBaseTick_Type()
)
cwdIfChannelMiniSlotTimeBaseTick.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfChannelMiniSlotTimeBaseTick.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfChannelMiniSlotTimeBaseTick.setUnits("Microseconds")
_CwdIfChannelSubChannelPlanVer_Type = Unsigned32
_CwdIfChannelSubChannelPlanVer_Object = MibTableColumn
cwdIfChannelSubChannelPlanVer = _CwdIfChannelSubChannelPlanVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 1, 1, 6),
    _CwdIfChannelSubChannelPlanVer_Type()
)
cwdIfChannelSubChannelPlanVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfChannelSubChannelPlanVer.setStatus("current")
_CwdIfDownstreamChannelTable_Object = MibTable
cwdIfDownstreamChannelTable = _CwdIfDownstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cwdIfDownstreamChannelTable.setStatus("current")
_CwdIfDownstreamChannelEntry_Object = MibTableRow
cwdIfDownstreamChannelEntry = _CwdIfDownstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 2, 1)
)
cwdIfDownstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwdIfDownstreamChannelEntry.setStatus("current")


class _CwdIfDownChannelSubChannelNumber_Type(Integer32):
    """Custom type cwdIfDownChannelSubChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CwdIfDownChannelSubChannelNumber_Type.__name__ = "Integer32"
_CwdIfDownChannelSubChannelNumber_Object = MibTableColumn
cwdIfDownChannelSubChannelNumber = _CwdIfDownChannelSubChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 2, 1, 1),
    _CwdIfDownChannelSubChannelNumber_Type()
)
cwdIfDownChannelSubChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfDownChannelSubChannelNumber.setStatus("current")


class _CwdIfDownChannelId_Type(Integer32):
    """Custom type cwdIfDownChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CwdIfDownChannelId_Type.__name__ = "Integer32"
_CwdIfDownChannelId_Object = MibTableColumn
cwdIfDownChannelId = _CwdIfDownChannelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 2, 1, 2),
    _CwdIfDownChannelId_Type()
)
cwdIfDownChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfDownChannelId.setStatus("current")


class _CwdIfDownChannelFrequency_Type(Integer32):
    """Custom type cwdIfDownChannelFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_CwdIfDownChannelFrequency_Type.__name__ = "Integer32"
_CwdIfDownChannelFrequency_Object = MibTableColumn
cwdIfDownChannelFrequency = _CwdIfDownChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 2, 1, 3),
    _CwdIfDownChannelFrequency_Type()
)
cwdIfDownChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfDownChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfDownChannelFrequency.setUnits("kHz")


class _CwdIfDownChannelWidth_Type(Integer32):
    """Custom type cwdIfDownChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_CwdIfDownChannelWidth_Type.__name__ = "Integer32"
_CwdIfDownChannelWidth_Object = MibTableColumn
cwdIfDownChannelWidth = _CwdIfDownChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 2, 1, 4),
    _CwdIfDownChannelWidth_Type()
)
cwdIfDownChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfDownChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfDownChannelWidth.setUnits("kHz")


class _CwdIfDownChannelPower_Type(Integer32):
    """Custom type cwdIfDownChannelPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 50),
    )


_CwdIfDownChannelPower_Type.__name__ = "Integer32"
_CwdIfDownChannelPower_Object = MibTableColumn
cwdIfDownChannelPower = _CwdIfDownChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 2, 1, 5),
    _CwdIfDownChannelPower_Type()
)
cwdIfDownChannelPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfDownChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfDownChannelPower.setUnits("dBm - decibel milliwatts")
_CwdIfDownChannelModProfileIndex_Type = Unsigned32
_CwdIfDownChannelModProfileIndex_Object = MibTableColumn
cwdIfDownChannelModProfileIndex = _CwdIfDownChannelModProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 2, 1, 6),
    _CwdIfDownChannelModProfileIndex_Type()
)
cwdIfDownChannelModProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfDownChannelModProfileIndex.setStatus("current")
_CwdIfUpstreamChannelTable_Object = MibTable
cwdIfUpstreamChannelTable = _CwdIfUpstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cwdIfUpstreamChannelTable.setStatus("current")
_CwdIfUpstreamChannelEntry_Object = MibTableRow
cwdIfUpstreamChannelEntry = _CwdIfUpstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1)
)
cwdIfUpstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwdIfUpstreamChannelEntry.setStatus("current")


class _CwdIfUpChannelSubChannelNumber_Type(Integer32):
    """Custom type cwdIfUpChannelSubChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CwdIfUpChannelSubChannelNumber_Type.__name__ = "Integer32"
_CwdIfUpChannelSubChannelNumber_Object = MibTableColumn
cwdIfUpChannelSubChannelNumber = _CwdIfUpChannelSubChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 1),
    _CwdIfUpChannelSubChannelNumber_Type()
)
cwdIfUpChannelSubChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfUpChannelSubChannelNumber.setStatus("current")


class _CwdIfUpChannelId_Type(Integer32):
    """Custom type cwdIfUpChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CwdIfUpChannelId_Type.__name__ = "Integer32"
_CwdIfUpChannelId_Object = MibTableColumn
cwdIfUpChannelId = _CwdIfUpChannelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 2),
    _CwdIfUpChannelId_Type()
)
cwdIfUpChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfUpChannelId.setStatus("current")


class _CwdIfUpChannelFrequency_Type(Integer32):
    """Custom type cwdIfUpChannelFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_CwdIfUpChannelFrequency_Type.__name__ = "Integer32"
_CwdIfUpChannelFrequency_Object = MibTableColumn
cwdIfUpChannelFrequency = _CwdIfUpChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 3),
    _CwdIfUpChannelFrequency_Type()
)
cwdIfUpChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfUpChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfUpChannelFrequency.setUnits("kHz")


class _CwdIfUpChannelWidth_Type(Integer32):
    """Custom type cwdIfUpChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_CwdIfUpChannelWidth_Type.__name__ = "Integer32"
_CwdIfUpChannelWidth_Object = MibTableColumn
cwdIfUpChannelWidth = _CwdIfUpChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 4),
    _CwdIfUpChannelWidth_Type()
)
cwdIfUpChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfUpChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfUpChannelWidth.setUnits("kHz")


class _CwdIfUpChannelTargetPower_Type(Integer32):
    """Custom type cwdIfUpChannelTargetPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 50),
    )


_CwdIfUpChannelTargetPower_Type.__name__ = "Integer32"
_CwdIfUpChannelTargetPower_Object = MibTableColumn
cwdIfUpChannelTargetPower = _CwdIfUpChannelTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 5),
    _CwdIfUpChannelTargetPower_Type()
)
cwdIfUpChannelTargetPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfUpChannelTargetPower.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfUpChannelTargetPower.setUnits("dBm - decibel milliwatts")
_CwdIfUpChannelModProfileIndex_Type = Unsigned32
_CwdIfUpChannelModProfileIndex_Object = MibTableColumn
cwdIfUpChannelModProfileIndex = _CwdIfUpChannelModProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 6),
    _CwdIfUpChannelModProfileIndex_Type()
)
cwdIfUpChannelModProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfUpChannelModProfileIndex.setStatus("current")
_CwdIfUpChannelSlotSize_Type = Unsigned32
_CwdIfUpChannelSlotSize_Object = MibTableColumn
cwdIfUpChannelSlotSize = _CwdIfUpChannelSlotSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 7),
    _CwdIfUpChannelSlotSize_Type()
)
cwdIfUpChannelSlotSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfUpChannelSlotSize.setStatus("current")
_CwdIfUpChannelTxTimingOffset_Type = Unsigned32
_CwdIfUpChannelTxTimingOffset_Object = MibTableColumn
cwdIfUpChannelTxTimingOffset = _CwdIfUpChannelTxTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 8),
    _CwdIfUpChannelTxTimingOffset_Type()
)
cwdIfUpChannelTxTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfUpChannelTxTimingOffset.setStatus("current")


class _CwdIfUpChannelRangBackoffStart_Type(Integer32):
    """Custom type cwdIfUpChannelRangBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CwdIfUpChannelRangBackoffStart_Type.__name__ = "Integer32"
_CwdIfUpChannelRangBackoffStart_Object = MibTableColumn
cwdIfUpChannelRangBackoffStart = _CwdIfUpChannelRangBackoffStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 9),
    _CwdIfUpChannelRangBackoffStart_Type()
)
cwdIfUpChannelRangBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfUpChannelRangBackoffStart.setStatus("current")


class _CwdIfUpChannelRangBackoffEnd_Type(Integer32):
    """Custom type cwdIfUpChannelRangBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CwdIfUpChannelRangBackoffEnd_Type.__name__ = "Integer32"
_CwdIfUpChannelRangBackoffEnd_Object = MibTableColumn
cwdIfUpChannelRangBackoffEnd = _CwdIfUpChannelRangBackoffEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 10),
    _CwdIfUpChannelRangBackoffEnd_Type()
)
cwdIfUpChannelRangBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfUpChannelRangBackoffEnd.setStatus("current")


class _CwdIfUpChannelTxBackoffStart_Type(Integer32):
    """Custom type cwdIfUpChannelTxBackoffStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CwdIfUpChannelTxBackoffStart_Type.__name__ = "Integer32"
_CwdIfUpChannelTxBackoffStart_Object = MibTableColumn
cwdIfUpChannelTxBackoffStart = _CwdIfUpChannelTxBackoffStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 11),
    _CwdIfUpChannelTxBackoffStart_Type()
)
cwdIfUpChannelTxBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfUpChannelTxBackoffStart.setStatus("current")


class _CwdIfUpChannelTxBackoffEnd_Type(Integer32):
    """Custom type cwdIfUpChannelTxBackoffEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CwdIfUpChannelTxBackoffEnd_Type.__name__ = "Integer32"
_CwdIfUpChannelTxBackoffEnd_Object = MibTableColumn
cwdIfUpChannelTxBackoffEnd = _CwdIfUpChannelTxBackoffEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 4, 1, 12),
    _CwdIfUpChannelTxBackoffEnd_Type()
)
cwdIfUpChannelTxBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfUpChannelTxBackoffEnd.setStatus("current")
_CwdIfQosProfileTable_Object = MibTable
cwdIfQosProfileTable = _CwdIfQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cwdIfQosProfileTable.setStatus("current")
_CwdIfQosProfileEntry_Object = MibTableRow
cwdIfQosProfileEntry = _CwdIfQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 5, 1)
)
cwdIfQosProfileEntry.setIndexNames(
    (0, "CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfQosProfIndex"),
)
if mibBuilder.loadTexts:
    cwdIfQosProfileEntry.setStatus("current")


class _CwdIfQosProfIndex_Type(Integer32):
    """Custom type cwdIfQosProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CwdIfQosProfIndex_Type.__name__ = "Integer32"
_CwdIfQosProfIndex_Object = MibTableColumn
cwdIfQosProfIndex = _CwdIfQosProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 5, 1, 1),
    _CwdIfQosProfIndex_Type()
)
cwdIfQosProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdIfQosProfIndex.setStatus("current")


class _CwdIfQosProfPriority_Type(Integer32):
    """Custom type cwdIfQosProfPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CwdIfQosProfPriority_Type.__name__ = "Integer32"
_CwdIfQosProfPriority_Object = MibTableColumn
cwdIfQosProfPriority = _CwdIfQosProfPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 5, 1, 2),
    _CwdIfQosProfPriority_Type()
)
cwdIfQosProfPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfQosProfPriority.setStatus("current")


class _CwdIfQosProfMaxUpBandwidth_Type(Integer32):
    """Custom type cwdIfQosProfMaxUpBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CwdIfQosProfMaxUpBandwidth_Type.__name__ = "Integer32"
_CwdIfQosProfMaxUpBandwidth_Object = MibTableColumn
cwdIfQosProfMaxUpBandwidth = _CwdIfQosProfMaxUpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 5, 1, 3),
    _CwdIfQosProfMaxUpBandwidth_Type()
)
cwdIfQosProfMaxUpBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfQosProfMaxUpBandwidth.setStatus("current")


class _CwdIfQosProfGuarUpBandwidth_Type(Integer32):
    """Custom type cwdIfQosProfGuarUpBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CwdIfQosProfGuarUpBandwidth_Type.__name__ = "Integer32"
_CwdIfQosProfGuarUpBandwidth_Object = MibTableColumn
cwdIfQosProfGuarUpBandwidth = _CwdIfQosProfGuarUpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 5, 1, 4),
    _CwdIfQosProfGuarUpBandwidth_Type()
)
cwdIfQosProfGuarUpBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfQosProfGuarUpBandwidth.setStatus("current")


class _CwdIfQosProfMaxDownBandwidth_Type(Integer32):
    """Custom type cwdIfQosProfMaxDownBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CwdIfQosProfMaxDownBandwidth_Type.__name__ = "Integer32"
_CwdIfQosProfMaxDownBandwidth_Object = MibTableColumn
cwdIfQosProfMaxDownBandwidth = _CwdIfQosProfMaxDownBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 5, 1, 5),
    _CwdIfQosProfMaxDownBandwidth_Type()
)
cwdIfQosProfMaxDownBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfQosProfMaxDownBandwidth.setStatus("current")


class _CwdIfQosProfMaxTxBurst_Type(Integer32):
    """Custom type cwdIfQosProfMaxTxBurst based on Integer32"""
    defaultValue = 0


_CwdIfQosProfMaxTxBurst_Object = MibTableColumn
cwdIfQosProfMaxTxBurst = _CwdIfQosProfMaxTxBurst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 5, 1, 6),
    _CwdIfQosProfMaxTxBurst_Type()
)
cwdIfQosProfMaxTxBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfQosProfMaxTxBurst.setStatus("current")


class _CwdIfQosProfBaselinePrivacy_Type(TruthValue):
    """Custom type cwdIfQosProfBaselinePrivacy based on TruthValue"""


_CwdIfQosProfBaselinePrivacy_Object = MibTableColumn
cwdIfQosProfBaselinePrivacy = _CwdIfQosProfBaselinePrivacy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 5, 1, 7),
    _CwdIfQosProfBaselinePrivacy_Type()
)
cwdIfQosProfBaselinePrivacy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfQosProfBaselinePrivacy.setStatus("current")
_CwdIfQosProfStatus_Type = RowStatus
_CwdIfQosProfStatus_Object = MibTableColumn
cwdIfQosProfStatus = _CwdIfQosProfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 5, 1, 8),
    _CwdIfQosProfStatus_Type()
)
cwdIfQosProfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfQosProfStatus.setStatus("current")
_CwdIfSignalQualityTable_Object = MibTable
cwdIfSignalQualityTable = _CwdIfSignalQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cwdIfSignalQualityTable.setStatus("current")
_CwdIfSignalQualityEntry_Object = MibTableRow
cwdIfSignalQualityEntry = _CwdIfSignalQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 6, 1)
)
cwdIfSignalQualityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwdIfSignalQualityEntry.setStatus("current")
_CwdIfSigQIncludesContention_Type = TruthValue
_CwdIfSigQIncludesContention_Object = MibTableColumn
cwdIfSigQIncludesContention = _CwdIfSigQIncludesContention_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 6, 1, 1),
    _CwdIfSigQIncludesContention_Type()
)
cwdIfSigQIncludesContention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSigQIncludesContention.setStatus("current")
_CwdIfSigQUnerroreds_Type = Counter32
_CwdIfSigQUnerroreds_Object = MibTableColumn
cwdIfSigQUnerroreds = _CwdIfSigQUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 6, 1, 2),
    _CwdIfSigQUnerroreds_Type()
)
cwdIfSigQUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSigQUnerroreds.setStatus("current")
_CwdIfSigQCorrecteds_Type = Counter32
_CwdIfSigQCorrecteds_Object = MibTableColumn
cwdIfSigQCorrecteds = _CwdIfSigQCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 6, 1, 3),
    _CwdIfSigQCorrecteds_Type()
)
cwdIfSigQCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSigQCorrecteds.setStatus("current")
_CwdIfSigQUncorrectables_Type = Counter32
_CwdIfSigQUncorrectables_Object = MibTableColumn
cwdIfSigQUncorrectables = _CwdIfSigQUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 6, 1, 4),
    _CwdIfSigQUncorrectables_Type()
)
cwdIfSigQUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSigQUncorrectables.setStatus("current")
_CwdIfSigQSignalNoise_Type = CwrdBm
_CwdIfSigQSignalNoise_Object = MibTableColumn
cwdIfSigQSignalNoise = _CwdIfSigQSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 6, 1, 5),
    _CwdIfSigQSignalNoise_Type()
)
cwdIfSigQSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSigQSignalNoise.setStatus("current")
_CwdIfModulationTable_Object = MibTable
cwdIfModulationTable = _CwdIfModulationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cwdIfModulationTable.setStatus("current")
_CwdIfModulationEntry_Object = MibTableRow
cwdIfModulationEntry = _CwdIfModulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 7, 1)
)
cwdIfModulationEntry.setIndexNames(
    (0, "CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfModIndex"),
)
if mibBuilder.loadTexts:
    cwdIfModulationEntry.setStatus("current")


class _CwdIfModIndex_Type(Integer32):
    """Custom type cwdIfModIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwdIfModIndex_Type.__name__ = "Integer32"
_CwdIfModIndex_Object = MibTableColumn
cwdIfModIndex = _CwdIfModIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 7, 1, 1),
    _CwdIfModIndex_Type()
)
cwdIfModIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdIfModIndex.setStatus("current")
_CwdIfModRowStatus_Type = RowStatus
_CwdIfModRowStatus_Object = MibTableColumn
cwdIfModRowStatus = _CwdIfModRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 7, 1, 2),
    _CwdIfModRowStatus_Type()
)
cwdIfModRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfModRowStatus.setStatus("current")


class _CwdIfModBandwidth_Type(Integer32):
    """Custom type cwdIfModBandwidth based on Integer32"""
    defaultValue = 6000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_CwdIfModBandwidth_Type.__name__ = "Integer32"
_CwdIfModBandwidth_Object = MibTableColumn
cwdIfModBandwidth = _CwdIfModBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 7, 1, 3),
    _CwdIfModBandwidth_Type()
)
cwdIfModBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfModBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfModBandwidth.setUnits("kHz")


class _CwdIfModThroughput_Type(Integer32):
    """Custom type cwdIfModThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_CwdIfModThroughput_Type.__name__ = "Integer32"
_CwdIfModThroughput_Object = MibTableColumn
cwdIfModThroughput = _CwdIfModThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 7, 1, 4),
    _CwdIfModThroughput_Type()
)
cwdIfModThroughput.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfModThroughput.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfModThroughput.setUnits("bps")


class _CwdIfModBurstLength_Type(Integer32):
    """Custom type cwdIfModBurstLength based on Integer32"""
    defaultValue = 3

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
        *(("long", 4),
          ("medium", 3),
          ("short", 2),
          ("veryShort", 1))
    )


_CwdIfModBurstLength_Type.__name__ = "Integer32"
_CwdIfModBurstLength_Object = MibTableColumn
cwdIfModBurstLength = _CwdIfModBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 7, 1, 5),
    _CwdIfModBurstLength_Type()
)
cwdIfModBurstLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfModBurstLength.setStatus("current")


class _CwdIfModMultipathRobustness_Type(Integer32):
    """Custom type cwdIfModMultipathRobustness based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("standard", 1))
    )


_CwdIfModMultipathRobustness_Type.__name__ = "Integer32"
_CwdIfModMultipathRobustness_Object = MibTableColumn
cwdIfModMultipathRobustness = _CwdIfModMultipathRobustness_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 1, 7, 1, 6),
    _CwdIfModMultipathRobustness_Type()
)
cwdIfModMultipathRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwdIfModMultipathRobustness.setStatus("current")
_CwdIfSuObjects_ObjectIdentity = ObjectIdentity
cwdIfSuObjects = _CwdIfSuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2)
)
_CwdIfSuMacTable_Object = MibTable
cwdIfSuMacTable = _CwdIfSuMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwdIfSuMacTable.setStatus("current")
_CwdIfSuMacEntry_Object = MibTableRow
cwdIfSuMacEntry = _CwdIfSuMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 1, 1)
)
cwdIfSuMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwdIfSuMacEntry.setStatus("current")
_CwdIfSuHeAddress_Type = MacAddress
_CwdIfSuHeAddress_Object = MibTableColumn
cwdIfSuHeAddress = _CwdIfSuHeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 1, 1, 1),
    _CwdIfSuHeAddress_Type()
)
cwdIfSuHeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuHeAddress.setStatus("current")


class _CwdIfSuCapabilities_Type(Bits):
    """Custom type cwdIfSuCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("atmCells", 0),
          ("concatenation", 1))
    )

_CwdIfSuCapabilities_Type.__name__ = "Bits"
_CwdIfSuCapabilities_Object = MibTableColumn
cwdIfSuCapabilities = _CwdIfSuCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 1, 1, 2),
    _CwdIfSuCapabilities_Type()
)
cwdIfSuCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuCapabilities.setStatus("current")


class _CwdIfSuRangingRespTimeout_Type(TimeInterval):
    """Custom type cwdIfSuRangingRespTimeout based on TimeInterval"""
    defaultValue = 20


_CwdIfSuRangingRespTimeout_Object = MibTableColumn
cwdIfSuRangingRespTimeout = _CwdIfSuRangingRespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 1, 1, 3),
    _CwdIfSuRangingRespTimeout_Type()
)
cwdIfSuRangingRespTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfSuRangingRespTimeout.setStatus("current")
_CwdIfSuStatusTable_Object = MibTable
cwdIfSuStatusTable = _CwdIfSuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cwdIfSuStatusTable.setStatus("current")
_CwdIfSuStatusEntry_Object = MibTableRow
cwdIfSuStatusEntry = _CwdIfSuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1)
)
cwdIfSuStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwdIfSuStatusEntry.setStatus("current")


class _CwdIfSuStatusValue_Type(Integer32):
    """Custom type cwdIfSuStatusValue based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 13),
          ("ipComplete", 7),
          ("notReady", 2),
          ("notSynchronized", 3),
          ("operational", 12),
          ("other", 1),
          ("paramTransferComplete", 10),
          ("phySynchronized", 4),
          ("rangingComplete", 6),
          ("registrationComplete", 11),
          ("securityEstablished", 9),
          ("todEstablished", 8),
          ("usParametersAcquired", 5))
    )


_CwdIfSuStatusValue_Type.__name__ = "Integer32"
_CwdIfSuStatusValue_Object = MibTableColumn
cwdIfSuStatusValue = _CwdIfSuStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 1),
    _CwdIfSuStatusValue_Type()
)
cwdIfSuStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusValue.setStatus("current")
_CwdIfSuStatusCode_Type = OctetString
_CwdIfSuStatusCode_Object = MibTableColumn
cwdIfSuStatusCode = _CwdIfSuStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 2),
    _CwdIfSuStatusCode_Type()
)
cwdIfSuStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusCode.setStatus("current")


class _CwdIfSuStatusTxPower_Type(Integer32):
    """Custom type cwdIfSuStatusTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 50),
    )


_CwdIfSuStatusTxPower_Type.__name__ = "Integer32"
_CwdIfSuStatusTxPower_Object = MibTableColumn
cwdIfSuStatusTxPower = _CwdIfSuStatusTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 3),
    _CwdIfSuStatusTxPower_Type()
)
cwdIfSuStatusTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfSuStatusTxPower.setUnits("dBm - decibel milliwatts")
_CwdIfSuStatusResets_Type = Counter32
_CwdIfSuStatusResets_Object = MibTableColumn
cwdIfSuStatusResets = _CwdIfSuStatusResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 4),
    _CwdIfSuStatusResets_Type()
)
cwdIfSuStatusResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusResets.setStatus("current")
_CwdIfSuStatusLostSyncs_Type = Counter32
_CwdIfSuStatusLostSyncs_Object = MibTableColumn
cwdIfSuStatusLostSyncs = _CwdIfSuStatusLostSyncs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 5),
    _CwdIfSuStatusLostSyncs_Type()
)
cwdIfSuStatusLostSyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusLostSyncs.setStatus("current")
_CwdIfSuStatusInvalidMaps_Type = Counter32
_CwdIfSuStatusInvalidMaps_Object = MibTableColumn
cwdIfSuStatusInvalidMaps = _CwdIfSuStatusInvalidMaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 6),
    _CwdIfSuStatusInvalidMaps_Type()
)
cwdIfSuStatusInvalidMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusInvalidMaps.setStatus("current")
_CwdIfSuStatusInvalidUcds_Type = Counter32
_CwdIfSuStatusInvalidUcds_Object = MibTableColumn
cwdIfSuStatusInvalidUcds = _CwdIfSuStatusInvalidUcds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 7),
    _CwdIfSuStatusInvalidUcds_Type()
)
cwdIfSuStatusInvalidUcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusInvalidUcds.setStatus("current")
_CwdIfSuStatusInvalidRangingResp_Type = Counter32
_CwdIfSuStatusInvalidRangingResp_Object = MibTableColumn
cwdIfSuStatusInvalidRangingResp = _CwdIfSuStatusInvalidRangingResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 8),
    _CwdIfSuStatusInvalidRangingResp_Type()
)
cwdIfSuStatusInvalidRangingResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusInvalidRangingResp.setStatus("current")
_CwdIfSuStatusInvalidRegResp_Type = Counter32
_CwdIfSuStatusInvalidRegResp_Object = MibTableColumn
cwdIfSuStatusInvalidRegResp = _CwdIfSuStatusInvalidRegResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 9),
    _CwdIfSuStatusInvalidRegResp_Type()
)
cwdIfSuStatusInvalidRegResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusInvalidRegResp.setStatus("current")
_CwdIfSuStatusT1Timeouts_Type = Counter32
_CwdIfSuStatusT1Timeouts_Object = MibTableColumn
cwdIfSuStatusT1Timeouts = _CwdIfSuStatusT1Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 10),
    _CwdIfSuStatusT1Timeouts_Type()
)
cwdIfSuStatusT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusT1Timeouts.setStatus("current")
_CwdIfSuStatusT2Timeouts_Type = Counter32
_CwdIfSuStatusT2Timeouts_Object = MibTableColumn
cwdIfSuStatusT2Timeouts = _CwdIfSuStatusT2Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 11),
    _CwdIfSuStatusT2Timeouts_Type()
)
cwdIfSuStatusT2Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusT2Timeouts.setStatus("current")
_CwdIfSuStatusT3Timeouts_Type = Counter32
_CwdIfSuStatusT3Timeouts_Object = MibTableColumn
cwdIfSuStatusT3Timeouts = _CwdIfSuStatusT3Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 12),
    _CwdIfSuStatusT3Timeouts_Type()
)
cwdIfSuStatusT3Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusT3Timeouts.setStatus("current")
_CwdIfSuStatusT4Timeouts_Type = Counter32
_CwdIfSuStatusT4Timeouts_Object = MibTableColumn
cwdIfSuStatusT4Timeouts = _CwdIfSuStatusT4Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 13),
    _CwdIfSuStatusT4Timeouts_Type()
)
cwdIfSuStatusT4Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusT4Timeouts.setStatus("current")
_CwdIfSuStatusRangingAborteds_Type = Counter32
_CwdIfSuStatusRangingAborteds_Object = MibTableColumn
cwdIfSuStatusRangingAborteds = _CwdIfSuStatusRangingAborteds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 2, 1, 14),
    _CwdIfSuStatusRangingAborteds_Type()
)
cwdIfSuStatusRangingAborteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuStatusRangingAborteds.setStatus("current")
_CwdIfSuServiceTable_Object = MibTable
cwdIfSuServiceTable = _CwdIfSuServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cwdIfSuServiceTable.setStatus("current")
_CwdIfSuServiceEntry_Object = MibTableRow
cwdIfSuServiceEntry = _CwdIfSuServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 3, 1)
)
cwdIfSuServiceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuServiceId"),
)
if mibBuilder.loadTexts:
    cwdIfSuServiceEntry.setStatus("current")


class _CwdIfSuServiceId_Type(Integer32):
    """Custom type cwdIfSuServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CwdIfSuServiceId_Type.__name__ = "Integer32"
_CwdIfSuServiceId_Object = MibTableColumn
cwdIfSuServiceId = _CwdIfSuServiceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 3, 1, 1),
    _CwdIfSuServiceId_Type()
)
cwdIfSuServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdIfSuServiceId.setStatus("current")


class _CwdIfSuServiceQosProfile_Type(Integer32):
    """Custom type cwdIfSuServiceQosProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CwdIfSuServiceQosProfile_Type.__name__ = "Integer32"
_CwdIfSuServiceQosProfile_Object = MibTableColumn
cwdIfSuServiceQosProfile = _CwdIfSuServiceQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 3, 1, 2),
    _CwdIfSuServiceQosProfile_Type()
)
cwdIfSuServiceQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuServiceQosProfile.setStatus("current")
_CwdIfSuServiceTxSlotsImmed_Type = Counter32
_CwdIfSuServiceTxSlotsImmed_Object = MibTableColumn
cwdIfSuServiceTxSlotsImmed = _CwdIfSuServiceTxSlotsImmed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 3, 1, 3),
    _CwdIfSuServiceTxSlotsImmed_Type()
)
cwdIfSuServiceTxSlotsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuServiceTxSlotsImmed.setStatus("current")
_CwdIfSuServiceTxSlotsDed_Type = Counter32
_CwdIfSuServiceTxSlotsDed_Object = MibTableColumn
cwdIfSuServiceTxSlotsDed = _CwdIfSuServiceTxSlotsDed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 3, 1, 4),
    _CwdIfSuServiceTxSlotsDed_Type()
)
cwdIfSuServiceTxSlotsDed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuServiceTxSlotsDed.setStatus("current")
_CwdIfSuServiceTxRetries_Type = Counter32
_CwdIfSuServiceTxRetries_Object = MibTableColumn
cwdIfSuServiceTxRetries = _CwdIfSuServiceTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 3, 1, 5),
    _CwdIfSuServiceTxRetries_Type()
)
cwdIfSuServiceTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuServiceTxRetries.setStatus("current")
_CwdIfSuServiceTxExceeded_Type = Counter32
_CwdIfSuServiceTxExceeded_Object = MibTableColumn
cwdIfSuServiceTxExceeded = _CwdIfSuServiceTxExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 3, 1, 6),
    _CwdIfSuServiceTxExceeded_Type()
)
cwdIfSuServiceTxExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuServiceTxExceeded.setStatus("current")
_CwdIfSuServiceRqRetries_Type = Counter32
_CwdIfSuServiceRqRetries_Object = MibTableColumn
cwdIfSuServiceRqRetries = _CwdIfSuServiceRqRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 3, 1, 7),
    _CwdIfSuServiceRqRetries_Type()
)
cwdIfSuServiceRqRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuServiceRqRetries.setStatus("current")
_CwdIfSuServiceRqExceeded_Type = Counter32
_CwdIfSuServiceRqExceeded_Object = MibTableColumn
cwdIfSuServiceRqExceeded = _CwdIfSuServiceRqExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 2, 3, 1, 8),
    _CwdIfSuServiceRqExceeded_Type()
)
cwdIfSuServiceRqExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfSuServiceRqExceeded.setStatus("current")
_CwdIfHeObjects_ObjectIdentity = ObjectIdentity
cwdIfHeObjects = _CwdIfHeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3)
)
_CwdIfHeMacTable_Object = MibTable
cwdIfHeMacTable = _CwdIfHeMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwdIfHeMacTable.setStatus("current")
_CwdIfHeMacEntry_Object = MibTableRow
cwdIfHeMacEntry = _CwdIfHeMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 1, 1)
)
cwdIfHeMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwdIfHeMacEntry.setStatus("current")


class _CwdIfHeCapabilities_Type(Bits):
    """Custom type cwdIfHeCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("atmCells", 0),
          ("concatenation", 1))
    )

_CwdIfHeCapabilities_Type.__name__ = "Bits"
_CwdIfHeCapabilities_Object = MibTableColumn
cwdIfHeCapabilities = _CwdIfHeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 1, 1, 1),
    _CwdIfHeCapabilities_Type()
)
cwdIfHeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeCapabilities.setStatus("current")


class _CwdIfHeSyncInterval_Type(Integer32):
    """Custom type cwdIfHeSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CwdIfHeSyncInterval_Type.__name__ = "Integer32"
_CwdIfHeSyncInterval_Object = MibTableColumn
cwdIfHeSyncInterval = _CwdIfHeSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 1, 1, 2),
    _CwdIfHeSyncInterval_Type()
)
cwdIfHeSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfHeSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfHeSyncInterval.setUnits("Milliseconds")


class _CwdIfHeUcdInterval_Type(Integer32):
    """Custom type cwdIfHeUcdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_CwdIfHeUcdInterval_Type.__name__ = "Integer32"
_CwdIfHeUcdInterval_Object = MibTableColumn
cwdIfHeUcdInterval = _CwdIfHeUcdInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 1, 1, 3),
    _CwdIfHeUcdInterval_Type()
)
cwdIfHeUcdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfHeUcdInterval.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfHeUcdInterval.setUnits("Milliseconds")


class _CwdIfHeMaxServiceIds_Type(Integer32):
    """Custom type cwdIfHeMaxServiceIds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CwdIfHeMaxServiceIds_Type.__name__ = "Integer32"
_CwdIfHeMaxServiceIds_Object = MibTableColumn
cwdIfHeMaxServiceIds = _CwdIfHeMaxServiceIds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 1, 1, 4),
    _CwdIfHeMaxServiceIds_Type()
)
cwdIfHeMaxServiceIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeMaxServiceIds.setStatus("current")
_CwdIfHeInsertionInterval_Type = TimeInterval
_CwdIfHeInsertionInterval_Object = MibTableColumn
cwdIfHeInsertionInterval = _CwdIfHeInsertionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 1, 1, 5),
    _CwdIfHeInsertionInterval_Type()
)
cwdIfHeInsertionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfHeInsertionInterval.setStatus("current")


class _CwdIfHeInvitedRangingAttempts_Type(Integer32):
    """Custom type cwdIfHeInvitedRangingAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CwdIfHeInvitedRangingAttempts_Type.__name__ = "Integer32"
_CwdIfHeInvitedRangingAttempts_Object = MibTableColumn
cwdIfHeInvitedRangingAttempts = _CwdIfHeInvitedRangingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 1, 1, 6),
    _CwdIfHeInvitedRangingAttempts_Type()
)
cwdIfHeInvitedRangingAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfHeInvitedRangingAttempts.setStatus("current")
_CwdIfHeStatusTable_Object = MibTable
cwdIfHeStatusTable = _CwdIfHeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cwdIfHeStatusTable.setStatus("current")
_CwdIfHeStatusEntry_Object = MibTableRow
cwdIfHeStatusEntry = _CwdIfHeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 2, 1)
)
cwdIfHeStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwdIfHeStatusEntry.setStatus("current")
_CwdIfHeStatusInvalidRangeReqs_Type = Counter32
_CwdIfHeStatusInvalidRangeReqs_Object = MibTableColumn
cwdIfHeStatusInvalidRangeReqs = _CwdIfHeStatusInvalidRangeReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 2, 1, 1),
    _CwdIfHeStatusInvalidRangeReqs_Type()
)
cwdIfHeStatusInvalidRangeReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeStatusInvalidRangeReqs.setStatus("current")
_CwdIfHeStatusRangingAborteds_Type = Counter32
_CwdIfHeStatusRangingAborteds_Object = MibTableColumn
cwdIfHeStatusRangingAborteds = _CwdIfHeStatusRangingAborteds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 2, 1, 2),
    _CwdIfHeStatusRangingAborteds_Type()
)
cwdIfHeStatusRangingAborteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeStatusRangingAborteds.setStatus("current")
_CwdIfHeStatusInvalidRegReqs_Type = Counter32
_CwdIfHeStatusInvalidRegReqs_Object = MibTableColumn
cwdIfHeStatusInvalidRegReqs = _CwdIfHeStatusInvalidRegReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 2, 1, 3),
    _CwdIfHeStatusInvalidRegReqs_Type()
)
cwdIfHeStatusInvalidRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeStatusInvalidRegReqs.setStatus("current")
_CwdIfHeStatusFailedRegReqs_Type = Counter32
_CwdIfHeStatusFailedRegReqs_Object = MibTableColumn
cwdIfHeStatusFailedRegReqs = _CwdIfHeStatusFailedRegReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 2, 1, 4),
    _CwdIfHeStatusFailedRegReqs_Type()
)
cwdIfHeStatusFailedRegReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeStatusFailedRegReqs.setStatus("current")
_CwdIfHeStatusInvalidDataReqs_Type = Counter32
_CwdIfHeStatusInvalidDataReqs_Object = MibTableColumn
cwdIfHeStatusInvalidDataReqs = _CwdIfHeStatusInvalidDataReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 2, 1, 5),
    _CwdIfHeStatusInvalidDataReqs_Type()
)
cwdIfHeStatusInvalidDataReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeStatusInvalidDataReqs.setStatus("current")
_CwdIfHeStatusT5Timeouts_Type = Counter32
_CwdIfHeStatusT5Timeouts_Object = MibTableColumn
cwdIfHeStatusT5Timeouts = _CwdIfHeStatusT5Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 2, 1, 6),
    _CwdIfHeStatusT5Timeouts_Type()
)
cwdIfHeStatusT5Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeStatusT5Timeouts.setStatus("current")
_CwdIfHeSuStatusTable_Object = MibTable
cwdIfHeSuStatusTable = _CwdIfHeSuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cwdIfHeSuStatusTable.setStatus("current")
_CwdIfHeSuStatusEntry_Object = MibTableRow
cwdIfHeSuStatusEntry = _CwdIfHeSuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3, 1)
)
cwdIfHeSuStatusEntry.setIndexNames(
    (0, "CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusIndex"),
)
if mibBuilder.loadTexts:
    cwdIfHeSuStatusEntry.setStatus("current")


class _CwdIfHeSuStatusIndex_Type(Integer32):
    """Custom type cwdIfHeSuStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwdIfHeSuStatusIndex_Type.__name__ = "Integer32"
_CwdIfHeSuStatusIndex_Object = MibTableColumn
cwdIfHeSuStatusIndex = _CwdIfHeSuStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3, 1, 1),
    _CwdIfHeSuStatusIndex_Type()
)
cwdIfHeSuStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdIfHeSuStatusIndex.setStatus("current")
_CwdIfHeSuStatusMacAddress_Type = MacAddress
_CwdIfHeSuStatusMacAddress_Object = MibTableColumn
cwdIfHeSuStatusMacAddress = _CwdIfHeSuStatusMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3, 1, 2),
    _CwdIfHeSuStatusMacAddress_Type()
)
cwdIfHeSuStatusMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeSuStatusMacAddress.setStatus("current")
_CwdIfHeSuStatusIpAddress_Type = IpAddress
_CwdIfHeSuStatusIpAddress_Object = MibTableColumn
cwdIfHeSuStatusIpAddress = _CwdIfHeSuStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3, 1, 3),
    _CwdIfHeSuStatusIpAddress_Type()
)
cwdIfHeSuStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeSuStatusIpAddress.setStatus("current")
_CwdIfHeSuStatusDownChanIfIndex_Type = InterfaceIndexOrZero
_CwdIfHeSuStatusDownChanIfIndex_Object = MibTableColumn
cwdIfHeSuStatusDownChanIfIndex = _CwdIfHeSuStatusDownChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3, 1, 4),
    _CwdIfHeSuStatusDownChanIfIndex_Type()
)
cwdIfHeSuStatusDownChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeSuStatusDownChanIfIndex.setStatus("current")
_CwdIfHeSuStatusUpChanIfIndex_Type = InterfaceIndexOrZero
_CwdIfHeSuStatusUpChanIfIndex_Object = MibTableColumn
cwdIfHeSuStatusUpChanIfIndex = _CwdIfHeSuStatusUpChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3, 1, 5),
    _CwdIfHeSuStatusUpChanIfIndex_Type()
)
cwdIfHeSuStatusUpChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeSuStatusUpChanIfIndex.setStatus("current")


class _CwdIfHeSuStatusRxPower_Type(Integer32):
    """Custom type cwdIfHeSuStatusRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 33),
    )


_CwdIfHeSuStatusRxPower_Type.__name__ = "Integer32"
_CwdIfHeSuStatusRxPower_Object = MibTableColumn
cwdIfHeSuStatusRxPower = _CwdIfHeSuStatusRxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3, 1, 6),
    _CwdIfHeSuStatusRxPower_Type()
)
cwdIfHeSuStatusRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeSuStatusRxPower.setStatus("current")
if mibBuilder.loadTexts:
    cwdIfHeSuStatusRxPower.setUnits("dBm Decibel milliwatts")
_CwdIfHeSuStatusTimingOffset_Type = Unsigned32
_CwdIfHeSuStatusTimingOffset_Object = MibTableColumn
cwdIfHeSuStatusTimingOffset = _CwdIfHeSuStatusTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3, 1, 7),
    _CwdIfHeSuStatusTimingOffset_Type()
)
cwdIfHeSuStatusTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeSuStatusTimingOffset.setStatus("current")


class _CwdIfHeSuStatusValue_Type(Integer32):
    """Custom type cwdIfHeSuStatusValue based on Integer32"""
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
        *(("accessDenied", 7),
          ("ipComplete", 5),
          ("other", 1),
          ("ranging", 2),
          ("rangingAborted", 3),
          ("rangingComplete", 4),
          ("registrationComplete", 6))
    )


_CwdIfHeSuStatusValue_Type.__name__ = "Integer32"
_CwdIfHeSuStatusValue_Object = MibTableColumn
cwdIfHeSuStatusValue = _CwdIfHeSuStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3, 1, 8),
    _CwdIfHeSuStatusValue_Type()
)
cwdIfHeSuStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeSuStatusValue.setStatus("current")
_CwdIfHeSuStatusIfIndex_Type = InterfaceIndex
_CwdIfHeSuStatusIfIndex_Object = MibTableColumn
cwdIfHeSuStatusIfIndex = _CwdIfHeSuStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3, 1, 9),
    _CwdIfHeSuStatusIfIndex_Type()
)
cwdIfHeSuStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeSuStatusIfIndex.setStatus("current")


class _CwdIfHeSuStatusServiceId_Type(Integer32):
    """Custom type cwdIfHeSuStatusServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CwdIfHeSuStatusServiceId_Type.__name__ = "Integer32"
_CwdIfHeSuStatusServiceId_Object = MibTableColumn
cwdIfHeSuStatusServiceId = _CwdIfHeSuStatusServiceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 3, 1, 10),
    _CwdIfHeSuStatusServiceId_Type()
)
cwdIfHeSuStatusServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeSuStatusServiceId.setStatus("current")
_CwdIfHeServiceTable_Object = MibTable
cwdIfHeServiceTable = _CwdIfHeServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cwdIfHeServiceTable.setStatus("current")
_CwdIfHeServiceEntry_Object = MibTableRow
cwdIfHeServiceEntry = _CwdIfHeServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 4, 1)
)
cwdIfHeServiceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeServiceId"),
)
if mibBuilder.loadTexts:
    cwdIfHeServiceEntry.setStatus("current")


class _CwdIfHeServiceId_Type(Integer32):
    """Custom type cwdIfHeServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CwdIfHeServiceId_Type.__name__ = "Integer32"
_CwdIfHeServiceId_Object = MibTableColumn
cwdIfHeServiceId = _CwdIfHeServiceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 4, 1, 1),
    _CwdIfHeServiceId_Type()
)
cwdIfHeServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwdIfHeServiceId.setStatus("current")


class _CwdIfHeServiceSuStatusIndex_Type(Integer32):
    """Custom type cwdIfHeServiceSuStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwdIfHeServiceSuStatusIndex_Type.__name__ = "Integer32"
_CwdIfHeServiceSuStatusIndex_Object = MibTableColumn
cwdIfHeServiceSuStatusIndex = _CwdIfHeServiceSuStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 4, 1, 2),
    _CwdIfHeServiceSuStatusIndex_Type()
)
cwdIfHeServiceSuStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeServiceSuStatusIndex.setStatus("current")


class _CwdIfHeServiceAdminStatus_Type(Integer32):
    """Custom type cwdIfHeServiceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destroyed", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_CwdIfHeServiceAdminStatus_Type.__name__ = "Integer32"
_CwdIfHeServiceAdminStatus_Object = MibTableColumn
cwdIfHeServiceAdminStatus = _CwdIfHeServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 4, 1, 3),
    _CwdIfHeServiceAdminStatus_Type()
)
cwdIfHeServiceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfHeServiceAdminStatus.setStatus("current")


class _CwdIfHeServiceQosProfile_Type(Integer32):
    """Custom type cwdIfHeServiceQosProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CwdIfHeServiceQosProfile_Type.__name__ = "Integer32"
_CwdIfHeServiceQosProfile_Object = MibTableColumn
cwdIfHeServiceQosProfile = _CwdIfHeServiceQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 4, 1, 4),
    _CwdIfHeServiceQosProfile_Type()
)
cwdIfHeServiceQosProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeServiceQosProfile.setStatus("current")
_CwdIfHeServiceCreateTime_Type = TimeStamp
_CwdIfHeServiceCreateTime_Object = MibTableColumn
cwdIfHeServiceCreateTime = _CwdIfHeServiceCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 4, 1, 5),
    _CwdIfHeServiceCreateTime_Type()
)
cwdIfHeServiceCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeServiceCreateTime.setStatus("current")
_CwdIfHeServiceInOctets_Type = Counter32
_CwdIfHeServiceInOctets_Object = MibTableColumn
cwdIfHeServiceInOctets = _CwdIfHeServiceInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 4, 1, 6),
    _CwdIfHeServiceInOctets_Type()
)
cwdIfHeServiceInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeServiceInOctets.setStatus("current")
_CwdIfHeServiceInPackets_Type = Counter32
_CwdIfHeServiceInPackets_Object = MibTableColumn
cwdIfHeServiceInPackets = _CwdIfHeServiceInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 4, 1, 7),
    _CwdIfHeServiceInPackets_Type()
)
cwdIfHeServiceInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdIfHeServiceInPackets.setStatus("current")


class _CwdIfHeQosProfilePermissions_Type(Bits):
    """Custom type cwdIfHeQosProfilePermissions based on Bits"""
    namedValues = NamedValues(
        *(("createByManagement", 0),
          ("createBySubscriberUnits", 2),
          ("updateByManagement", 1))
    )

_CwdIfHeQosProfilePermissions_Type.__name__ = "Bits"
_CwdIfHeQosProfilePermissions_Object = MibScalar
cwdIfHeQosProfilePermissions = _CwdIfHeQosProfilePermissions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 1, 3, 6),
    _CwdIfHeQosProfilePermissions_Type()
)
cwdIfHeQosProfilePermissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdIfHeQosProfilePermissions.setStatus("current")
_CwdIfNotification_ObjectIdentity = ObjectIdentity
cwdIfNotification = _CwdIfNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 2)
)
_CwdIfConformance_ObjectIdentity = ObjectIdentity
cwdIfConformance = _CwdIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 3)
)
_CwdIfCompliances_ObjectIdentity = ObjectIdentity
cwdIfCompliances = _CwdIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 3, 1)
)
_CwdIfGroups_ObjectIdentity = ObjectIdentity
cwdIfGroups = _CwdIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 3, 2)
)

# Managed Objects groups

cwdIfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 3, 2, 1)
)
cwdIfBasicGroup.setObjects(
      *(("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfChannelUpFrequency"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfChannelUpWidth"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfChannelDownFrequency"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfChannelDownWidth"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfChannelMiniSlotTimeBaseTick"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfChannelSubChannelPlanVer"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfDownChannelSubChannelNumber"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfDownChannelId"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfDownChannelFrequency"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfDownChannelWidth"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfDownChannelPower"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfDownChannelModProfileIndex"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelSubChannelNumber"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelId"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelFrequency"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelWidth"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelTargetPower"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelModProfileIndex"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelSlotSize"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelTxTimingOffset"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelRangBackoffStart"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelRangBackoffEnd"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelTxBackoffStart"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfUpChannelTxBackoffEnd"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSigQIncludesContention"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSigQUnerroreds"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSigQCorrecteds"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSigQUncorrectables"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSigQSignalNoise"))
)
if mibBuilder.loadTexts:
    cwdIfBasicGroup.setStatus("current")

cwdIfSuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 3, 2, 2)
)
cwdIfSuGroup.setObjects(
      *(("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuHeAddress"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuCapabilities"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuRangingRespTimeout"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusValue"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusCode"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusTxPower"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusResets"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusLostSyncs"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusInvalidMaps"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusInvalidUcds"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusInvalidRangingResp"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusInvalidRegResp"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusT1Timeouts"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusT2Timeouts"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusT3Timeouts"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusT4Timeouts"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuStatusRangingAborteds"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuServiceQosProfile"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuServiceTxSlotsImmed"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuServiceTxSlotsDed"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuServiceTxRetries"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuServiceTxExceeded"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuServiceRqRetries"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfSuServiceRqExceeded"))
)
if mibBuilder.loadTexts:
    cwdIfSuGroup.setStatus("current")

cwdIfQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 3, 2, 3)
)
cwdIfQosGroup.setObjects(
      *(("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfQosProfPriority"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfQosProfMaxUpBandwidth"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfQosProfGuarUpBandwidth"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfQosProfMaxDownBandwidth"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfQosProfMaxTxBurst"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfQosProfBaselinePrivacy"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfQosProfStatus"))
)
if mibBuilder.loadTexts:
    cwdIfQosGroup.setStatus("current")

cwdIfQosHeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 3, 2, 4)
)
cwdIfQosHeGroup.setObjects(
    ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeQosProfilePermissions")
)
if mibBuilder.loadTexts:
    cwdIfQosHeGroup.setStatus("current")

cwdIfModGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 3, 2, 5)
)
cwdIfModGroup.setObjects(
      *(("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfModRowStatus"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfModBandwidth"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfModThroughput"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfModBurstLength"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfModMultipathRobustness"))
)
if mibBuilder.loadTexts:
    cwdIfModGroup.setStatus("current")

cwdIfHeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 3, 2, 7)
)
cwdIfHeGroup.setObjects(
      *(("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeCapabilities"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSyncInterval"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeUcdInterval"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeMaxServiceIds"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeInsertionInterval"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeInvitedRangingAttempts"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeStatusInvalidRangeReqs"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeStatusRangingAborteds"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeStatusInvalidRegReqs"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeStatusFailedRegReqs"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeStatusInvalidDataReqs"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeStatusT5Timeouts"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusMacAddress"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusIpAddress"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusDownChanIfIndex"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusUpChanIfIndex"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusRxPower"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusTimingOffset"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusValue"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusIfIndex"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeSuStatusServiceId"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeServiceSuStatusIndex"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeServiceAdminStatus"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeServiceQosProfile"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeServiceCreateTime"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeServiceInOctets"),
        ("CISCO-WIRELESS-DOCS-IF-MIB", "cwdIfHeServiceInPackets"))
)
if mibBuilder.loadTexts:
    cwdIfHeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwdIfBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 167, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cwdIfBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-DOCS-IF-MIB",
    **{"ciscoWirelessDocsIfMib": ciscoWirelessDocsIfMib,
       "cwdIfMibObjects": cwdIfMibObjects,
       "cwdIfBaseObjects": cwdIfBaseObjects,
       "cwdIfChannelTable": cwdIfChannelTable,
       "cwdIfChannelEntry": cwdIfChannelEntry,
       "cwdIfChannelUpFrequency": cwdIfChannelUpFrequency,
       "cwdIfChannelUpWidth": cwdIfChannelUpWidth,
       "cwdIfChannelDownFrequency": cwdIfChannelDownFrequency,
       "cwdIfChannelDownWidth": cwdIfChannelDownWidth,
       "cwdIfChannelMiniSlotTimeBaseTick": cwdIfChannelMiniSlotTimeBaseTick,
       "cwdIfChannelSubChannelPlanVer": cwdIfChannelSubChannelPlanVer,
       "cwdIfDownstreamChannelTable": cwdIfDownstreamChannelTable,
       "cwdIfDownstreamChannelEntry": cwdIfDownstreamChannelEntry,
       "cwdIfDownChannelSubChannelNumber": cwdIfDownChannelSubChannelNumber,
       "cwdIfDownChannelId": cwdIfDownChannelId,
       "cwdIfDownChannelFrequency": cwdIfDownChannelFrequency,
       "cwdIfDownChannelWidth": cwdIfDownChannelWidth,
       "cwdIfDownChannelPower": cwdIfDownChannelPower,
       "cwdIfDownChannelModProfileIndex": cwdIfDownChannelModProfileIndex,
       "cwdIfUpstreamChannelTable": cwdIfUpstreamChannelTable,
       "cwdIfUpstreamChannelEntry": cwdIfUpstreamChannelEntry,
       "cwdIfUpChannelSubChannelNumber": cwdIfUpChannelSubChannelNumber,
       "cwdIfUpChannelId": cwdIfUpChannelId,
       "cwdIfUpChannelFrequency": cwdIfUpChannelFrequency,
       "cwdIfUpChannelWidth": cwdIfUpChannelWidth,
       "cwdIfUpChannelTargetPower": cwdIfUpChannelTargetPower,
       "cwdIfUpChannelModProfileIndex": cwdIfUpChannelModProfileIndex,
       "cwdIfUpChannelSlotSize": cwdIfUpChannelSlotSize,
       "cwdIfUpChannelTxTimingOffset": cwdIfUpChannelTxTimingOffset,
       "cwdIfUpChannelRangBackoffStart": cwdIfUpChannelRangBackoffStart,
       "cwdIfUpChannelRangBackoffEnd": cwdIfUpChannelRangBackoffEnd,
       "cwdIfUpChannelTxBackoffStart": cwdIfUpChannelTxBackoffStart,
       "cwdIfUpChannelTxBackoffEnd": cwdIfUpChannelTxBackoffEnd,
       "cwdIfQosProfileTable": cwdIfQosProfileTable,
       "cwdIfQosProfileEntry": cwdIfQosProfileEntry,
       "cwdIfQosProfIndex": cwdIfQosProfIndex,
       "cwdIfQosProfPriority": cwdIfQosProfPriority,
       "cwdIfQosProfMaxUpBandwidth": cwdIfQosProfMaxUpBandwidth,
       "cwdIfQosProfGuarUpBandwidth": cwdIfQosProfGuarUpBandwidth,
       "cwdIfQosProfMaxDownBandwidth": cwdIfQosProfMaxDownBandwidth,
       "cwdIfQosProfMaxTxBurst": cwdIfQosProfMaxTxBurst,
       "cwdIfQosProfBaselinePrivacy": cwdIfQosProfBaselinePrivacy,
       "cwdIfQosProfStatus": cwdIfQosProfStatus,
       "cwdIfSignalQualityTable": cwdIfSignalQualityTable,
       "cwdIfSignalQualityEntry": cwdIfSignalQualityEntry,
       "cwdIfSigQIncludesContention": cwdIfSigQIncludesContention,
       "cwdIfSigQUnerroreds": cwdIfSigQUnerroreds,
       "cwdIfSigQCorrecteds": cwdIfSigQCorrecteds,
       "cwdIfSigQUncorrectables": cwdIfSigQUncorrectables,
       "cwdIfSigQSignalNoise": cwdIfSigQSignalNoise,
       "cwdIfModulationTable": cwdIfModulationTable,
       "cwdIfModulationEntry": cwdIfModulationEntry,
       "cwdIfModIndex": cwdIfModIndex,
       "cwdIfModRowStatus": cwdIfModRowStatus,
       "cwdIfModBandwidth": cwdIfModBandwidth,
       "cwdIfModThroughput": cwdIfModThroughput,
       "cwdIfModBurstLength": cwdIfModBurstLength,
       "cwdIfModMultipathRobustness": cwdIfModMultipathRobustness,
       "cwdIfSuObjects": cwdIfSuObjects,
       "cwdIfSuMacTable": cwdIfSuMacTable,
       "cwdIfSuMacEntry": cwdIfSuMacEntry,
       "cwdIfSuHeAddress": cwdIfSuHeAddress,
       "cwdIfSuCapabilities": cwdIfSuCapabilities,
       "cwdIfSuRangingRespTimeout": cwdIfSuRangingRespTimeout,
       "cwdIfSuStatusTable": cwdIfSuStatusTable,
       "cwdIfSuStatusEntry": cwdIfSuStatusEntry,
       "cwdIfSuStatusValue": cwdIfSuStatusValue,
       "cwdIfSuStatusCode": cwdIfSuStatusCode,
       "cwdIfSuStatusTxPower": cwdIfSuStatusTxPower,
       "cwdIfSuStatusResets": cwdIfSuStatusResets,
       "cwdIfSuStatusLostSyncs": cwdIfSuStatusLostSyncs,
       "cwdIfSuStatusInvalidMaps": cwdIfSuStatusInvalidMaps,
       "cwdIfSuStatusInvalidUcds": cwdIfSuStatusInvalidUcds,
       "cwdIfSuStatusInvalidRangingResp": cwdIfSuStatusInvalidRangingResp,
       "cwdIfSuStatusInvalidRegResp": cwdIfSuStatusInvalidRegResp,
       "cwdIfSuStatusT1Timeouts": cwdIfSuStatusT1Timeouts,
       "cwdIfSuStatusT2Timeouts": cwdIfSuStatusT2Timeouts,
       "cwdIfSuStatusT3Timeouts": cwdIfSuStatusT3Timeouts,
       "cwdIfSuStatusT4Timeouts": cwdIfSuStatusT4Timeouts,
       "cwdIfSuStatusRangingAborteds": cwdIfSuStatusRangingAborteds,
       "cwdIfSuServiceTable": cwdIfSuServiceTable,
       "cwdIfSuServiceEntry": cwdIfSuServiceEntry,
       "cwdIfSuServiceId": cwdIfSuServiceId,
       "cwdIfSuServiceQosProfile": cwdIfSuServiceQosProfile,
       "cwdIfSuServiceTxSlotsImmed": cwdIfSuServiceTxSlotsImmed,
       "cwdIfSuServiceTxSlotsDed": cwdIfSuServiceTxSlotsDed,
       "cwdIfSuServiceTxRetries": cwdIfSuServiceTxRetries,
       "cwdIfSuServiceTxExceeded": cwdIfSuServiceTxExceeded,
       "cwdIfSuServiceRqRetries": cwdIfSuServiceRqRetries,
       "cwdIfSuServiceRqExceeded": cwdIfSuServiceRqExceeded,
       "cwdIfHeObjects": cwdIfHeObjects,
       "cwdIfHeMacTable": cwdIfHeMacTable,
       "cwdIfHeMacEntry": cwdIfHeMacEntry,
       "cwdIfHeCapabilities": cwdIfHeCapabilities,
       "cwdIfHeSyncInterval": cwdIfHeSyncInterval,
       "cwdIfHeUcdInterval": cwdIfHeUcdInterval,
       "cwdIfHeMaxServiceIds": cwdIfHeMaxServiceIds,
       "cwdIfHeInsertionInterval": cwdIfHeInsertionInterval,
       "cwdIfHeInvitedRangingAttempts": cwdIfHeInvitedRangingAttempts,
       "cwdIfHeStatusTable": cwdIfHeStatusTable,
       "cwdIfHeStatusEntry": cwdIfHeStatusEntry,
       "cwdIfHeStatusInvalidRangeReqs": cwdIfHeStatusInvalidRangeReqs,
       "cwdIfHeStatusRangingAborteds": cwdIfHeStatusRangingAborteds,
       "cwdIfHeStatusInvalidRegReqs": cwdIfHeStatusInvalidRegReqs,
       "cwdIfHeStatusFailedRegReqs": cwdIfHeStatusFailedRegReqs,
       "cwdIfHeStatusInvalidDataReqs": cwdIfHeStatusInvalidDataReqs,
       "cwdIfHeStatusT5Timeouts": cwdIfHeStatusT5Timeouts,
       "cwdIfHeSuStatusTable": cwdIfHeSuStatusTable,
       "cwdIfHeSuStatusEntry": cwdIfHeSuStatusEntry,
       "cwdIfHeSuStatusIndex": cwdIfHeSuStatusIndex,
       "cwdIfHeSuStatusMacAddress": cwdIfHeSuStatusMacAddress,
       "cwdIfHeSuStatusIpAddress": cwdIfHeSuStatusIpAddress,
       "cwdIfHeSuStatusDownChanIfIndex": cwdIfHeSuStatusDownChanIfIndex,
       "cwdIfHeSuStatusUpChanIfIndex": cwdIfHeSuStatusUpChanIfIndex,
       "cwdIfHeSuStatusRxPower": cwdIfHeSuStatusRxPower,
       "cwdIfHeSuStatusTimingOffset": cwdIfHeSuStatusTimingOffset,
       "cwdIfHeSuStatusValue": cwdIfHeSuStatusValue,
       "cwdIfHeSuStatusIfIndex": cwdIfHeSuStatusIfIndex,
       "cwdIfHeSuStatusServiceId": cwdIfHeSuStatusServiceId,
       "cwdIfHeServiceTable": cwdIfHeServiceTable,
       "cwdIfHeServiceEntry": cwdIfHeServiceEntry,
       "cwdIfHeServiceId": cwdIfHeServiceId,
       "cwdIfHeServiceSuStatusIndex": cwdIfHeServiceSuStatusIndex,
       "cwdIfHeServiceAdminStatus": cwdIfHeServiceAdminStatus,
       "cwdIfHeServiceQosProfile": cwdIfHeServiceQosProfile,
       "cwdIfHeServiceCreateTime": cwdIfHeServiceCreateTime,
       "cwdIfHeServiceInOctets": cwdIfHeServiceInOctets,
       "cwdIfHeServiceInPackets": cwdIfHeServiceInPackets,
       "cwdIfHeQosProfilePermissions": cwdIfHeQosProfilePermissions,
       "cwdIfNotification": cwdIfNotification,
       "cwdIfConformance": cwdIfConformance,
       "cwdIfCompliances": cwdIfCompliances,
       "cwdIfBasicCompliance": cwdIfBasicCompliance,
       "cwdIfGroups": cwdIfGroups,
       "cwdIfBasicGroup": cwdIfBasicGroup,
       "cwdIfSuGroup": cwdIfSuGroup,
       "cwdIfQosGroup": cwdIfQosGroup,
       "cwdIfQosHeGroup": cwdIfQosHeGroup,
       "cwdIfModGroup": cwdIfModGroup,
       "cwdIfHeGroup": cwdIfHeGroup}
)
