# SNMP MIB module (G9981-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/G9981-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:35 2024
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

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfInvalidIntervals,
 HCPerfTimeElapsed,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfInvalidIntervals",
    "HCPerfTimeElapsed",
    "HCPerfValidIntervals")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

g9981MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 208)
)
g9981MIB.setRevisions(
        ("2013-02-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MilliSeconds(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_G9981Objects_ObjectIdentity = ObjectIdentity
g9981Objects = _G9981Objects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 208, 1)
)
_G9981Port_ObjectIdentity = ObjectIdentity
g9981Port = _G9981Port_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 208, 1, 1)
)
_G9981PortNotifications_ObjectIdentity = ObjectIdentity
g9981PortNotifications = _G9981PortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 0)
)
_G9981PortConfTable_Object = MibTable
g9981PortConfTable = _G9981PortConfTable_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 1)
)
if mibBuilder.loadTexts:
    g9981PortConfTable.setStatus("current")
_G9981PortConfEntry_Object = MibTableRow
g9981PortConfEntry = _G9981PortConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 1, 1)
)
g9981PortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9981PortConfEntry.setStatus("current")


class _G9981PortConfUpDiffDelayTolerance_Type(MilliSeconds):
    """Custom type g9981PortConfUpDiffDelayTolerance based on MilliSeconds"""
    subtypeSpec = MilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_G9981PortConfUpDiffDelayTolerance_Type.__name__ = "MilliSeconds"
_G9981PortConfUpDiffDelayTolerance_Object = MibTableColumn
g9981PortConfUpDiffDelayTolerance = _G9981PortConfUpDiffDelayTolerance_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 1, 1, 1),
    _G9981PortConfUpDiffDelayTolerance_Type()
)
g9981PortConfUpDiffDelayTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9981PortConfUpDiffDelayTolerance.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortConfUpDiffDelayTolerance.setUnits("milliseconds")


class _G9981PortConfDnDiffDelayTolerance_Type(MilliSeconds):
    """Custom type g9981PortConfDnDiffDelayTolerance based on MilliSeconds"""
    subtypeSpec = MilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_G9981PortConfDnDiffDelayTolerance_Type.__name__ = "MilliSeconds"
_G9981PortConfDnDiffDelayTolerance_Object = MibTableColumn
g9981PortConfDnDiffDelayTolerance = _G9981PortConfDnDiffDelayTolerance_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 1, 1, 2),
    _G9981PortConfDnDiffDelayTolerance_Type()
)
g9981PortConfDnDiffDelayTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9981PortConfDnDiffDelayTolerance.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortConfDnDiffDelayTolerance.setUnits("milliseconds")
_G9981PortConfDiffDelayToleranceExceededEnable_Type = TruthValue
_G9981PortConfDiffDelayToleranceExceededEnable_Object = MibTableColumn
g9981PortConfDiffDelayToleranceExceededEnable = _G9981PortConfDiffDelayToleranceExceededEnable_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 1, 1, 3),
    _G9981PortConfDiffDelayToleranceExceededEnable_Type()
)
g9981PortConfDiffDelayToleranceExceededEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9981PortConfDiffDelayToleranceExceededEnable.setStatus("current")
_G9981PortStatTable_Object = MibTable
g9981PortStatTable = _G9981PortStatTable_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 2)
)
if mibBuilder.loadTexts:
    g9981PortStatTable.setStatus("current")
_G9981PortStatEntry_Object = MibTableRow
g9981PortStatEntry = _G9981PortStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 2, 1)
)
g9981PortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9981PortStatEntry.setStatus("current")
_G9981PortStatRxLostCells_Type = Counter32
_G9981PortStatRxLostCells_Object = MibTableColumn
g9981PortStatRxLostCells = _G9981PortStatRxLostCells_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 2, 1, 1),
    _G9981PortStatRxLostCells_Type()
)
g9981PortStatRxLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortStatRxLostCells.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortStatRxLostCells.setUnits("cells")
_G9981PortStatTxLostCells_Type = Counter32
_G9981PortStatTxLostCells_Object = MibTableColumn
g9981PortStatTxLostCells = _G9981PortStatTxLostCells_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 2, 1, 2),
    _G9981PortStatTxLostCells_Type()
)
g9981PortStatTxLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortStatTxLostCells.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortStatTxLostCells.setUnits("cells")
_G9981PortStatMaxUpDiffDelay_Type = Unsigned32
_G9981PortStatMaxUpDiffDelay_Object = MibTableColumn
g9981PortStatMaxUpDiffDelay = _G9981PortStatMaxUpDiffDelay_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 2, 1, 3),
    _G9981PortStatMaxUpDiffDelay_Type()
)
g9981PortStatMaxUpDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortStatMaxUpDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortStatMaxUpDiffDelay.setUnits("0.1 ms")
_G9981PortStatMaxDnDiffDelay_Type = Unsigned32
_G9981PortStatMaxDnDiffDelay_Object = MibTableColumn
g9981PortStatMaxDnDiffDelay = _G9981PortStatMaxDnDiffDelay_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 2, 1, 4),
    _G9981PortStatMaxDnDiffDelay_Type()
)
g9981PortStatMaxDnDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortStatMaxDnDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortStatMaxDnDiffDelay.setUnits("0.1 ms")
_G9981PM_ObjectIdentity = ObjectIdentity
g9981PM = _G9981PM_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3)
)
_G9981PortPmCurTable_Object = MibTable
g9981PortPmCurTable = _G9981PortPmCurTable_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    g9981PortPmCurTable.setStatus("current")
_G9981PortPmCurEntry_Object = MibTableRow
g9981PortPmCurEntry = _G9981PortPmCurEntry_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1)
)
g9981PortPmCurEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9981PortPmCurEntry.setStatus("current")
_G9981PortPmCur15MinValidIntervals_Type = HCPerfValidIntervals
_G9981PortPmCur15MinValidIntervals_Object = MibTableColumn
g9981PortPmCur15MinValidIntervals = _G9981PortPmCur15MinValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 1),
    _G9981PortPmCur15MinValidIntervals_Type()
)
g9981PortPmCur15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinValidIntervals.setStatus("current")
_G9981PortPmCur15MinInvalidIntervals_Type = HCPerfInvalidIntervals
_G9981PortPmCur15MinInvalidIntervals_Object = MibTableColumn
g9981PortPmCur15MinInvalidIntervals = _G9981PortPmCur15MinInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 2),
    _G9981PortPmCur15MinInvalidIntervals_Type()
)
g9981PortPmCur15MinInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinInvalidIntervals.setStatus("current")
_G9981PortPmCur15MinTimeElapsed_Type = HCPerfTimeElapsed
_G9981PortPmCur15MinTimeElapsed_Object = MibTableColumn
g9981PortPmCur15MinTimeElapsed = _G9981PortPmCur15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 3),
    _G9981PortPmCur15MinTimeElapsed_Type()
)
g9981PortPmCur15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinTimeElapsed.setUnits("seconds")
_G9981PortPmCur15MinRxLostCells_Type = HCPerfCurrentCount
_G9981PortPmCur15MinRxLostCells_Object = MibTableColumn
g9981PortPmCur15MinRxLostCells = _G9981PortPmCur15MinRxLostCells_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 4),
    _G9981PortPmCur15MinRxLostCells_Type()
)
g9981PortPmCur15MinRxLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinRxLostCells.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinRxLostCells.setUnits("cells")
_G9981PortPmCur15MinTxLostCells_Type = HCPerfCurrentCount
_G9981PortPmCur15MinTxLostCells_Object = MibTableColumn
g9981PortPmCur15MinTxLostCells = _G9981PortPmCur15MinTxLostCells_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 5),
    _G9981PortPmCur15MinTxLostCells_Type()
)
g9981PortPmCur15MinTxLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinTxLostCells.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinTxLostCells.setUnits("cells")
_G9981PortPmCur15MinUpDiffDelay_Type = HCPerfCurrentCount
_G9981PortPmCur15MinUpDiffDelay_Object = MibTableColumn
g9981PortPmCur15MinUpDiffDelay = _G9981PortPmCur15MinUpDiffDelay_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 6),
    _G9981PortPmCur15MinUpDiffDelay_Type()
)
g9981PortPmCur15MinUpDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinUpDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinUpDiffDelay.setUnits("0.1 ms")
_G9981PortPmCur15MinDnDiffDelay_Type = HCPerfCurrentCount
_G9981PortPmCur15MinDnDiffDelay_Object = MibTableColumn
g9981PortPmCur15MinDnDiffDelay = _G9981PortPmCur15MinDnDiffDelay_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 7),
    _G9981PortPmCur15MinDnDiffDelay_Type()
)
g9981PortPmCur15MinDnDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinDnDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur15MinDnDiffDelay.setUnits("0.1 ms")


class _G9981PortPmCur1DayValidIntervals_Type(Unsigned32):
    """Custom type g9981PortPmCur1DayValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_G9981PortPmCur1DayValidIntervals_Type.__name__ = "Unsigned32"
_G9981PortPmCur1DayValidIntervals_Object = MibTableColumn
g9981PortPmCur1DayValidIntervals = _G9981PortPmCur1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 8),
    _G9981PortPmCur1DayValidIntervals_Type()
)
g9981PortPmCur1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayValidIntervals.setUnits("days")


class _G9981PortPmCur1DayInvalidIntervals_Type(Unsigned32):
    """Custom type g9981PortPmCur1DayInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_G9981PortPmCur1DayInvalidIntervals_Type.__name__ = "Unsigned32"
_G9981PortPmCur1DayInvalidIntervals_Object = MibTableColumn
g9981PortPmCur1DayInvalidIntervals = _G9981PortPmCur1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 9),
    _G9981PortPmCur1DayInvalidIntervals_Type()
)
g9981PortPmCur1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayInvalidIntervals.setUnits("days")
_G9981PortPmCur1DayTimeElapsed_Type = HCPerfTimeElapsed
_G9981PortPmCur1DayTimeElapsed_Object = MibTableColumn
g9981PortPmCur1DayTimeElapsed = _G9981PortPmCur1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 10),
    _G9981PortPmCur1DayTimeElapsed_Type()
)
g9981PortPmCur1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayTimeElapsed.setUnits("seconds")
_G9981PortPmCur1DayRxLostCells_Type = HCPerfCurrentCount
_G9981PortPmCur1DayRxLostCells_Object = MibTableColumn
g9981PortPmCur1DayRxLostCells = _G9981PortPmCur1DayRxLostCells_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 11),
    _G9981PortPmCur1DayRxLostCells_Type()
)
g9981PortPmCur1DayRxLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayRxLostCells.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayRxLostCells.setUnits("cells")
_G9981PortPmCur1DayTxLostCells_Type = HCPerfCurrentCount
_G9981PortPmCur1DayTxLostCells_Object = MibTableColumn
g9981PortPmCur1DayTxLostCells = _G9981PortPmCur1DayTxLostCells_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 12),
    _G9981PortPmCur1DayTxLostCells_Type()
)
g9981PortPmCur1DayTxLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayTxLostCells.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayTxLostCells.setUnits("cells")
_G9981PortPmCur1DayUpDiffDelay_Type = HCPerfCurrentCount
_G9981PortPmCur1DayUpDiffDelay_Object = MibTableColumn
g9981PortPmCur1DayUpDiffDelay = _G9981PortPmCur1DayUpDiffDelay_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 13),
    _G9981PortPmCur1DayUpDiffDelay_Type()
)
g9981PortPmCur1DayUpDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayUpDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayUpDiffDelay.setUnits("0.1 ms")
_G9981PortPmCur1DayDnDiffDelay_Type = HCPerfCurrentCount
_G9981PortPmCur1DayDnDiffDelay_Object = MibTableColumn
g9981PortPmCur1DayDnDiffDelay = _G9981PortPmCur1DayDnDiffDelay_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 1, 1, 14),
    _G9981PortPmCur1DayDnDiffDelay_Type()
)
g9981PortPmCur1DayDnDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayDnDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPmCur1DayDnDiffDelay.setUnits("0.1 ms")
_G9981PortPm15MinTable_Object = MibTable
g9981PortPm15MinTable = _G9981PortPm15MinTable_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    g9981PortPm15MinTable.setStatus("current")
_G9981PortPm15MinEntry_Object = MibTableRow
g9981PortPm15MinEntry = _G9981PortPm15MinEntry_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 2, 1)
)
g9981PortPm15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "G9981-MIB", "g9981PortPm15MinIntervalIndex"),
)
if mibBuilder.loadTexts:
    g9981PortPm15MinEntry.setStatus("current")


class _G9981PortPm15MinIntervalIndex_Type(Unsigned32):
    """Custom type g9981PortPm15MinIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_G9981PortPm15MinIntervalIndex_Type.__name__ = "Unsigned32"
_G9981PortPm15MinIntervalIndex_Object = MibTableColumn
g9981PortPm15MinIntervalIndex = _G9981PortPm15MinIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 2, 1, 1),
    _G9981PortPm15MinIntervalIndex_Type()
)
g9981PortPm15MinIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalIndex.setStatus("current")
_G9981PortPm15MinIntervalMoniTime_Type = HCPerfTimeElapsed
_G9981PortPm15MinIntervalMoniTime_Object = MibTableColumn
g9981PortPm15MinIntervalMoniTime = _G9981PortPm15MinIntervalMoniTime_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 2, 1, 2),
    _G9981PortPm15MinIntervalMoniTime_Type()
)
g9981PortPm15MinIntervalMoniTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalMoniTime.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalMoniTime.setUnits("seconds")
_G9981PortPm15MinIntervalRxLostCells_Type = HCPerfIntervalCount
_G9981PortPm15MinIntervalRxLostCells_Object = MibTableColumn
g9981PortPm15MinIntervalRxLostCells = _G9981PortPm15MinIntervalRxLostCells_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 2, 1, 3),
    _G9981PortPm15MinIntervalRxLostCells_Type()
)
g9981PortPm15MinIntervalRxLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalRxLostCells.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalRxLostCells.setUnits("cells")
_G9981PortPm15MinIntervalTxLostCells_Type = HCPerfIntervalCount
_G9981PortPm15MinIntervalTxLostCells_Object = MibTableColumn
g9981PortPm15MinIntervalTxLostCells = _G9981PortPm15MinIntervalTxLostCells_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 2, 1, 4),
    _G9981PortPm15MinIntervalTxLostCells_Type()
)
g9981PortPm15MinIntervalTxLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalTxLostCells.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalTxLostCells.setUnits("cells")
_G9981PortPm15MinIntervalUpDiffDelay_Type = HCPerfIntervalCount
_G9981PortPm15MinIntervalUpDiffDelay_Object = MibTableColumn
g9981PortPm15MinIntervalUpDiffDelay = _G9981PortPm15MinIntervalUpDiffDelay_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 2, 1, 5),
    _G9981PortPm15MinIntervalUpDiffDelay_Type()
)
g9981PortPm15MinIntervalUpDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalUpDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalUpDiffDelay.setUnits("0.1 ms")
_G9981PortPm15MinIntervalDnDiffDelay_Type = HCPerfIntervalCount
_G9981PortPm15MinIntervalDnDiffDelay_Object = MibTableColumn
g9981PortPm15MinIntervalDnDiffDelay = _G9981PortPm15MinIntervalDnDiffDelay_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 2, 1, 6),
    _G9981PortPm15MinIntervalDnDiffDelay_Type()
)
g9981PortPm15MinIntervalDnDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalDnDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalDnDiffDelay.setUnits("0.1 ms")
_G9981PortPm15MinIntervalValid_Type = TruthValue
_G9981PortPm15MinIntervalValid_Object = MibTableColumn
g9981PortPm15MinIntervalValid = _G9981PortPm15MinIntervalValid_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 2, 1, 7),
    _G9981PortPm15MinIntervalValid_Type()
)
g9981PortPm15MinIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm15MinIntervalValid.setStatus("current")
_G9981PortPm1DayTable_Object = MibTable
g9981PortPm1DayTable = _G9981PortPm1DayTable_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    g9981PortPm1DayTable.setStatus("current")
_G9981PortPm1DayEntry_Object = MibTableRow
g9981PortPm1DayEntry = _G9981PortPm1DayEntry_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 3, 1)
)
g9981PortPm1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "G9981-MIB", "g9981PortPm1DayIntervalIndex"),
)
if mibBuilder.loadTexts:
    g9981PortPm1DayEntry.setStatus("current")


class _G9981PortPm1DayIntervalIndex_Type(Unsigned32):
    """Custom type g9981PortPm1DayIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_G9981PortPm1DayIntervalIndex_Type.__name__ = "Unsigned32"
_G9981PortPm1DayIntervalIndex_Object = MibTableColumn
g9981PortPm1DayIntervalIndex = _G9981PortPm1DayIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 3, 1, 1),
    _G9981PortPm1DayIntervalIndex_Type()
)
g9981PortPm1DayIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalIndex.setStatus("current")
_G9981PortPm1DayIntervalMoniTime_Type = HCPerfTimeElapsed
_G9981PortPm1DayIntervalMoniTime_Object = MibTableColumn
g9981PortPm1DayIntervalMoniTime = _G9981PortPm1DayIntervalMoniTime_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 3, 1, 2),
    _G9981PortPm1DayIntervalMoniTime_Type()
)
g9981PortPm1DayIntervalMoniTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalMoniTime.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalMoniTime.setUnits("seconds")
_G9981PortPm1DayIntervalRxLostCells_Type = HCPerfIntervalCount
_G9981PortPm1DayIntervalRxLostCells_Object = MibTableColumn
g9981PortPm1DayIntervalRxLostCells = _G9981PortPm1DayIntervalRxLostCells_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 3, 1, 3),
    _G9981PortPm1DayIntervalRxLostCells_Type()
)
g9981PortPm1DayIntervalRxLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalRxLostCells.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalRxLostCells.setUnits("cells")
_G9981PortPm1DayIntervalTxLostCells_Type = HCPerfIntervalCount
_G9981PortPm1DayIntervalTxLostCells_Object = MibTableColumn
g9981PortPm1DayIntervalTxLostCells = _G9981PortPm1DayIntervalTxLostCells_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 3, 1, 4),
    _G9981PortPm1DayIntervalTxLostCells_Type()
)
g9981PortPm1DayIntervalTxLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalTxLostCells.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalTxLostCells.setUnits("cells")
_G9981PortPm1DayIntervalUpDiffDelay_Type = HCPerfIntervalCount
_G9981PortPm1DayIntervalUpDiffDelay_Object = MibTableColumn
g9981PortPm1DayIntervalUpDiffDelay = _G9981PortPm1DayIntervalUpDiffDelay_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 3, 1, 5),
    _G9981PortPm1DayIntervalUpDiffDelay_Type()
)
g9981PortPm1DayIntervalUpDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalUpDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalUpDiffDelay.setUnits("0.1 ms")
_G9981PortPm1DayIntervalDnDiffDelay_Type = HCPerfIntervalCount
_G9981PortPm1DayIntervalDnDiffDelay_Object = MibTableColumn
g9981PortPm1DayIntervalDnDiffDelay = _G9981PortPm1DayIntervalDnDiffDelay_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 3, 1, 6),
    _G9981PortPm1DayIntervalDnDiffDelay_Type()
)
g9981PortPm1DayIntervalDnDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalDnDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalDnDiffDelay.setUnits("0.1 ms")
_G9981PortPm1DayIntervalValid_Type = TruthValue
_G9981PortPm1DayIntervalValid_Object = MibTableColumn
g9981PortPm1DayIntervalValid = _G9981PortPm1DayIntervalValid_Object(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 3, 3, 1, 7),
    _G9981PortPm1DayIntervalValid_Type()
)
g9981PortPm1DayIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9981PortPm1DayIntervalValid.setStatus("current")
_G9981Conformance_ObjectIdentity = ObjectIdentity
g9981Conformance = _G9981Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 208, 2)
)
_G9981Groups_ObjectIdentity = ObjectIdentity
g9981Groups = _G9981Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 208, 2, 1)
)
_G9981Compliances_ObjectIdentity = ObjectIdentity
g9981Compliances = _G9981Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 208, 2, 2)
)

# Managed Objects groups

g9981BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 208, 2, 1, 1)
)
g9981BasicGroup.setObjects(
      *(("G9981-MIB", "g9981PortStatRxLostCells"),
        ("G9981-MIB", "g9981PortStatTxLostCells"),
        ("G9981-MIB", "g9981PortStatMaxUpDiffDelay"),
        ("G9981-MIB", "g9981PortStatMaxDnDiffDelay"))
)
if mibBuilder.loadTexts:
    g9981BasicGroup.setStatus("current")

g9981AlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 208, 2, 1, 2)
)
g9981AlarmConfGroup.setObjects(
      *(("G9981-MIB", "g9981PortConfUpDiffDelayTolerance"),
        ("G9981-MIB", "g9981PortConfDnDiffDelayTolerance"),
        ("G9981-MIB", "g9981PortConfDiffDelayToleranceExceededEnable"))
)
if mibBuilder.loadTexts:
    g9981AlarmConfGroup.setStatus("current")

g9981PerfCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 208, 2, 1, 4)
)
g9981PerfCurrGroup.setObjects(
      *(("G9981-MIB", "g9981PortPmCur15MinValidIntervals"),
        ("G9981-MIB", "g9981PortPmCur15MinInvalidIntervals"),
        ("G9981-MIB", "g9981PortPmCur15MinTimeElapsed"),
        ("G9981-MIB", "g9981PortPmCur15MinRxLostCells"),
        ("G9981-MIB", "g9981PortPmCur15MinTxLostCells"),
        ("G9981-MIB", "g9981PortPmCur15MinUpDiffDelay"),
        ("G9981-MIB", "g9981PortPmCur15MinDnDiffDelay"),
        ("G9981-MIB", "g9981PortPmCur1DayValidIntervals"),
        ("G9981-MIB", "g9981PortPmCur1DayInvalidIntervals"),
        ("G9981-MIB", "g9981PortPmCur1DayTimeElapsed"),
        ("G9981-MIB", "g9981PortPmCur1DayRxLostCells"),
        ("G9981-MIB", "g9981PortPmCur1DayTxLostCells"),
        ("G9981-MIB", "g9981PortPmCur1DayUpDiffDelay"),
        ("G9981-MIB", "g9981PortPmCur1DayDnDiffDelay"))
)
if mibBuilder.loadTexts:
    g9981PerfCurrGroup.setStatus("current")

g9981Perf15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 208, 2, 1, 5)
)
g9981Perf15MinGroup.setObjects(
      *(("G9981-MIB", "g9981PortPm15MinIntervalMoniTime"),
        ("G9981-MIB", "g9981PortPm15MinIntervalRxLostCells"),
        ("G9981-MIB", "g9981PortPm15MinIntervalTxLostCells"),
        ("G9981-MIB", "g9981PortPm15MinIntervalUpDiffDelay"),
        ("G9981-MIB", "g9981PortPm15MinIntervalDnDiffDelay"),
        ("G9981-MIB", "g9981PortPm15MinIntervalValid"))
)
if mibBuilder.loadTexts:
    g9981Perf15MinGroup.setStatus("current")

g9981Perf1DayGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 208, 2, 1, 6)
)
g9981Perf1DayGroup.setObjects(
      *(("G9981-MIB", "g9981PortPm1DayIntervalMoniTime"),
        ("G9981-MIB", "g9981PortPm1DayIntervalRxLostCells"),
        ("G9981-MIB", "g9981PortPm1DayIntervalTxLostCells"),
        ("G9981-MIB", "g9981PortPm1DayIntervalUpDiffDelay"),
        ("G9981-MIB", "g9981PortPm1DayIntervalDnDiffDelay"),
        ("G9981-MIB", "g9981PortPm1DayIntervalValid"))
)
if mibBuilder.loadTexts:
    g9981Perf1DayGroup.setStatus("current")


# Notification objects

g9981UpDiffDelayToleranceExceeded = NotificationType(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 0, 1)
)
g9981UpDiffDelayToleranceExceeded.setObjects(
      *(("G9981-MIB", "g9981PortConfUpDiffDelayTolerance"),
        ("G9981-MIB", "g9981PortStatMaxUpDiffDelay"))
)
if mibBuilder.loadTexts:
    g9981UpDiffDelayToleranceExceeded.setStatus(
        "current"
    )

g9981DnDiffDelayToleranceExceeded = NotificationType(
    (1, 3, 6, 1, 2, 1, 208, 1, 1, 0, 2)
)
g9981DnDiffDelayToleranceExceeded.setObjects(
      *(("G9981-MIB", "g9981PortConfDnDiffDelayTolerance"),
        ("G9981-MIB", "g9981PortStatMaxDnDiffDelay"))
)
if mibBuilder.loadTexts:
    g9981DnDiffDelayToleranceExceeded.setStatus(
        "current"
    )


# Notifications groups

g9981NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 208, 2, 1, 3)
)
g9981NotificationGroup.setObjects(
      *(("G9981-MIB", "g9981UpDiffDelayToleranceExceeded"),
        ("G9981-MIB", "g9981DnDiffDelayToleranceExceeded"))
)
if mibBuilder.loadTexts:
    g9981NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

g9981Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 208, 2, 2, 1)
)
if mibBuilder.loadTexts:
    g9981Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G9981-MIB",
    **{"MilliSeconds": MilliSeconds,
       "g9981MIB": g9981MIB,
       "g9981Objects": g9981Objects,
       "g9981Port": g9981Port,
       "g9981PortNotifications": g9981PortNotifications,
       "g9981UpDiffDelayToleranceExceeded": g9981UpDiffDelayToleranceExceeded,
       "g9981DnDiffDelayToleranceExceeded": g9981DnDiffDelayToleranceExceeded,
       "g9981PortConfTable": g9981PortConfTable,
       "g9981PortConfEntry": g9981PortConfEntry,
       "g9981PortConfUpDiffDelayTolerance": g9981PortConfUpDiffDelayTolerance,
       "g9981PortConfDnDiffDelayTolerance": g9981PortConfDnDiffDelayTolerance,
       "g9981PortConfDiffDelayToleranceExceededEnable": g9981PortConfDiffDelayToleranceExceededEnable,
       "g9981PortStatTable": g9981PortStatTable,
       "g9981PortStatEntry": g9981PortStatEntry,
       "g9981PortStatRxLostCells": g9981PortStatRxLostCells,
       "g9981PortStatTxLostCells": g9981PortStatTxLostCells,
       "g9981PortStatMaxUpDiffDelay": g9981PortStatMaxUpDiffDelay,
       "g9981PortStatMaxDnDiffDelay": g9981PortStatMaxDnDiffDelay,
       "g9981PM": g9981PM,
       "g9981PortPmCurTable": g9981PortPmCurTable,
       "g9981PortPmCurEntry": g9981PortPmCurEntry,
       "g9981PortPmCur15MinValidIntervals": g9981PortPmCur15MinValidIntervals,
       "g9981PortPmCur15MinInvalidIntervals": g9981PortPmCur15MinInvalidIntervals,
       "g9981PortPmCur15MinTimeElapsed": g9981PortPmCur15MinTimeElapsed,
       "g9981PortPmCur15MinRxLostCells": g9981PortPmCur15MinRxLostCells,
       "g9981PortPmCur15MinTxLostCells": g9981PortPmCur15MinTxLostCells,
       "g9981PortPmCur15MinUpDiffDelay": g9981PortPmCur15MinUpDiffDelay,
       "g9981PortPmCur15MinDnDiffDelay": g9981PortPmCur15MinDnDiffDelay,
       "g9981PortPmCur1DayValidIntervals": g9981PortPmCur1DayValidIntervals,
       "g9981PortPmCur1DayInvalidIntervals": g9981PortPmCur1DayInvalidIntervals,
       "g9981PortPmCur1DayTimeElapsed": g9981PortPmCur1DayTimeElapsed,
       "g9981PortPmCur1DayRxLostCells": g9981PortPmCur1DayRxLostCells,
       "g9981PortPmCur1DayTxLostCells": g9981PortPmCur1DayTxLostCells,
       "g9981PortPmCur1DayUpDiffDelay": g9981PortPmCur1DayUpDiffDelay,
       "g9981PortPmCur1DayDnDiffDelay": g9981PortPmCur1DayDnDiffDelay,
       "g9981PortPm15MinTable": g9981PortPm15MinTable,
       "g9981PortPm15MinEntry": g9981PortPm15MinEntry,
       "g9981PortPm15MinIntervalIndex": g9981PortPm15MinIntervalIndex,
       "g9981PortPm15MinIntervalMoniTime": g9981PortPm15MinIntervalMoniTime,
       "g9981PortPm15MinIntervalRxLostCells": g9981PortPm15MinIntervalRxLostCells,
       "g9981PortPm15MinIntervalTxLostCells": g9981PortPm15MinIntervalTxLostCells,
       "g9981PortPm15MinIntervalUpDiffDelay": g9981PortPm15MinIntervalUpDiffDelay,
       "g9981PortPm15MinIntervalDnDiffDelay": g9981PortPm15MinIntervalDnDiffDelay,
       "g9981PortPm15MinIntervalValid": g9981PortPm15MinIntervalValid,
       "g9981PortPm1DayTable": g9981PortPm1DayTable,
       "g9981PortPm1DayEntry": g9981PortPm1DayEntry,
       "g9981PortPm1DayIntervalIndex": g9981PortPm1DayIntervalIndex,
       "g9981PortPm1DayIntervalMoniTime": g9981PortPm1DayIntervalMoniTime,
       "g9981PortPm1DayIntervalRxLostCells": g9981PortPm1DayIntervalRxLostCells,
       "g9981PortPm1DayIntervalTxLostCells": g9981PortPm1DayIntervalTxLostCells,
       "g9981PortPm1DayIntervalUpDiffDelay": g9981PortPm1DayIntervalUpDiffDelay,
       "g9981PortPm1DayIntervalDnDiffDelay": g9981PortPm1DayIntervalDnDiffDelay,
       "g9981PortPm1DayIntervalValid": g9981PortPm1DayIntervalValid,
       "g9981Conformance": g9981Conformance,
       "g9981Groups": g9981Groups,
       "g9981BasicGroup": g9981BasicGroup,
       "g9981AlarmConfGroup": g9981AlarmConfGroup,
       "g9981NotificationGroup": g9981NotificationGroup,
       "g9981PerfCurrGroup": g9981PerfCurrGroup,
       "g9981Perf15MinGroup": g9981Perf15MinGroup,
       "g9981Perf1DayGroup": g9981Perf1DayGroup,
       "g9981Compliances": g9981Compliances,
       "g9981Compliance": g9981Compliance}
)
