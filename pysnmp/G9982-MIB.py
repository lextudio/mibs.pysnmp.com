# SNMP MIB module (G9982-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/G9982-MIB
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
 HCPerfInvalidIntervals,
 HCPerfTimeElapsed,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

g9982MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 264)
)
g9982MIB.setRevisions(
        ("2013-02-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class G9982PtmTcType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tc6465", 1),
          ("tcHDLC", 2))
    )



class G9982CpType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpBACP", 2),
          ("cpHS", 1),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_G9982Objects_ObjectIdentity = ObjectIdentity
g9982Objects = _G9982Objects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 264, 1)
)
_G9982Port_ObjectIdentity = ObjectIdentity
g9982Port = _G9982Port_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 264, 1, 1)
)
_G9982PortConfTable_Object = MibTable
g9982PortConfTable = _G9982PortConfTable_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 1)
)
if mibBuilder.loadTexts:
    g9982PortConfTable.setStatus("current")
_G9982PortConfEntry_Object = MibTableRow
g9982PortConfEntry = _G9982PortConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 1, 1)
)
g9982PortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9982PortConfEntry.setStatus("current")
_G9982PortConfTcAdminType_Type = G9982PtmTcType
_G9982PortConfTcAdminType_Object = MibTableColumn
g9982PortConfTcAdminType = _G9982PortConfTcAdminType_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 1, 1, 1),
    _G9982PortConfTcAdminType_Type()
)
g9982PortConfTcAdminType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9982PortConfTcAdminType.setStatus("current")


class _G9982PortConfAdminCp_Type(G9982CpType):
    """Custom type g9982PortConfAdminCp based on G9982CpType"""


_G9982PortConfAdminCp_Object = MibTableColumn
g9982PortConfAdminCp = _G9982PortConfAdminCp_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 1, 1, 2),
    _G9982PortConfAdminCp_Type()
)
g9982PortConfAdminCp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9982PortConfAdminCp.setStatus("current")
_G9982PortCapTable_Object = MibTable
g9982PortCapTable = _G9982PortCapTable_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 2)
)
if mibBuilder.loadTexts:
    g9982PortCapTable.setStatus("current")
_G9982PortCapEntry_Object = MibTableRow
g9982PortCapEntry = _G9982PortCapEntry_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 2, 1)
)
g9982PortCapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9982PortCapEntry.setStatus("current")


class _G9982PortCapTcTypesSupported_Type(Bits):
    """Custom type g9982PortCapTcTypesSupported based on Bits"""
    namedValues = NamedValues(
        *(("tc6465", 0),
          ("tcHDLC", 1))
    )

_G9982PortCapTcTypesSupported_Type.__name__ = "Bits"
_G9982PortCapTcTypesSupported_Object = MibTableColumn
g9982PortCapTcTypesSupported = _G9982PortCapTcTypesSupported_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 2, 1, 1),
    _G9982PortCapTcTypesSupported_Type()
)
g9982PortCapTcTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortCapTcTypesSupported.setStatus("current")
_G9982PortCapBacpSupported_Type = TruthValue
_G9982PortCapBacpSupported_Object = MibTableColumn
g9982PortCapBacpSupported = _G9982PortCapBacpSupported_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 2, 1, 2),
    _G9982PortCapBacpSupported_Type()
)
g9982PortCapBacpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortCapBacpSupported.setStatus("current")
_G9982PortStatTable_Object = MibTable
g9982PortStatTable = _G9982PortStatTable_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3)
)
if mibBuilder.loadTexts:
    g9982PortStatTable.setStatus("current")
_G9982PortStatEntry_Object = MibTableRow
g9982PortStatEntry = _G9982PortStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3, 1)
)
g9982PortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9982PortStatEntry.setStatus("current")
_G9982PortStatTcOperType_Type = G9982PtmTcType
_G9982PortStatTcOperType_Object = MibTableColumn
g9982PortStatTcOperType = _G9982PortStatTcOperType_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3, 1, 1),
    _G9982PortStatTcOperType_Type()
)
g9982PortStatTcOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortStatTcOperType.setStatus("current")
_G9982PortStatOperCp_Type = G9982CpType
_G9982PortStatOperCp_Object = MibTableColumn
g9982PortStatOperCp = _G9982PortStatOperCp_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3, 1, 2),
    _G9982PortStatOperCp_Type()
)
g9982PortStatOperCp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortStatOperCp.setStatus("current")
_G9982PortStatRxErrors_Type = Counter32
_G9982PortStatRxErrors_Object = MibTableColumn
g9982PortStatRxErrors = _G9982PortStatRxErrors_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3, 1, 3),
    _G9982PortStatRxErrors_Type()
)
g9982PortStatRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortStatRxErrors.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortStatRxErrors.setUnits("fragments")
_G9982PortStatRxSmallFragments_Type = Counter32
_G9982PortStatRxSmallFragments_Object = MibTableColumn
g9982PortStatRxSmallFragments = _G9982PortStatRxSmallFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3, 1, 4),
    _G9982PortStatRxSmallFragments_Type()
)
g9982PortStatRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortStatRxSmallFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortStatRxSmallFragments.setUnits("fragments")
_G9982PortStatRxLargeFragments_Type = Counter32
_G9982PortStatRxLargeFragments_Object = MibTableColumn
g9982PortStatRxLargeFragments = _G9982PortStatRxLargeFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3, 1, 5),
    _G9982PortStatRxLargeFragments_Type()
)
g9982PortStatRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortStatRxLargeFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortStatRxLargeFragments.setUnits("fragments")
_G9982PortStatRxBadFragments_Type = Counter32
_G9982PortStatRxBadFragments_Object = MibTableColumn
g9982PortStatRxBadFragments = _G9982PortStatRxBadFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3, 1, 6),
    _G9982PortStatRxBadFragments_Type()
)
g9982PortStatRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortStatRxBadFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortStatRxBadFragments.setUnits("fragments")
_G9982PortStatRxLostFragments_Type = Counter32
_G9982PortStatRxLostFragments_Object = MibTableColumn
g9982PortStatRxLostFragments = _G9982PortStatRxLostFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3, 1, 7),
    _G9982PortStatRxLostFragments_Type()
)
g9982PortStatRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortStatRxLostFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortStatRxLostFragments.setUnits("fragments")
_G9982PortStatRxLostStarts_Type = Counter32
_G9982PortStatRxLostStarts_Object = MibTableColumn
g9982PortStatRxLostStarts = _G9982PortStatRxLostStarts_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3, 1, 8),
    _G9982PortStatRxLostStarts_Type()
)
g9982PortStatRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortStatRxLostStarts.setStatus("current")
_G9982PortStatRxLostEnds_Type = Counter32
_G9982PortStatRxLostEnds_Object = MibTableColumn
g9982PortStatRxLostEnds = _G9982PortStatRxLostEnds_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3, 1, 9),
    _G9982PortStatRxLostEnds_Type()
)
g9982PortStatRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortStatRxLostEnds.setStatus("current")
_G9982PortStatRxOverflows_Type = Counter32
_G9982PortStatRxOverflows_Object = MibTableColumn
g9982PortStatRxOverflows = _G9982PortStatRxOverflows_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 3, 1, 10),
    _G9982PortStatRxOverflows_Type()
)
g9982PortStatRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortStatRxOverflows.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortStatRxOverflows.setUnits("fragments")
_G9982PM_ObjectIdentity = ObjectIdentity
g9982PM = _G9982PM_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4)
)
_G9982PortPmCurTable_Object = MibTable
g9982PortPmCurTable = _G9982PortPmCurTable_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    g9982PortPmCurTable.setStatus("current")
_G9982PortPmCurEntry_Object = MibTableRow
g9982PortPmCurEntry = _G9982PortPmCurEntry_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1)
)
g9982PortPmCurEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9982PortPmCurEntry.setStatus("current")
_G9982PortPm15MinValidIntervals_Type = HCPerfValidIntervals
_G9982PortPm15MinValidIntervals_Object = MibTableColumn
g9982PortPm15MinValidIntervals = _G9982PortPm15MinValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 1),
    _G9982PortPm15MinValidIntervals_Type()
)
g9982PortPm15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinValidIntervals.setStatus("current")
_G9982PortPm15MinInvalidIntervals_Type = HCPerfInvalidIntervals
_G9982PortPm15MinInvalidIntervals_Object = MibTableColumn
g9982PortPm15MinInvalidIntervals = _G9982PortPm15MinInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 2),
    _G9982PortPm15MinInvalidIntervals_Type()
)
g9982PortPm15MinInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinInvalidIntervals.setStatus("current")
_G9982PortPmCur15MinTimeElapsed_Type = HCPerfTimeElapsed
_G9982PortPmCur15MinTimeElapsed_Object = MibTableColumn
g9982PortPmCur15MinTimeElapsed = _G9982PortPmCur15MinTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 3),
    _G9982PortPmCur15MinTimeElapsed_Type()
)
g9982PortPmCur15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinTimeElapsed.setUnits("seconds")
_G9982PortPmCur15MinRxErrors_Type = HCPerfCurrentCount
_G9982PortPmCur15MinRxErrors_Object = MibTableColumn
g9982PortPmCur15MinRxErrors = _G9982PortPmCur15MinRxErrors_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 4),
    _G9982PortPmCur15MinRxErrors_Type()
)
g9982PortPmCur15MinRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxErrors.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxErrors.setUnits("fragments")
_G9982PortPmCur15MinRxSmallFragments_Type = HCPerfCurrentCount
_G9982PortPmCur15MinRxSmallFragments_Object = MibTableColumn
g9982PortPmCur15MinRxSmallFragments = _G9982PortPmCur15MinRxSmallFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 5),
    _G9982PortPmCur15MinRxSmallFragments_Type()
)
g9982PortPmCur15MinRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxSmallFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxSmallFragments.setUnits("fragments")
_G9982PortPmCur15MinRxLargeFragments_Type = HCPerfCurrentCount
_G9982PortPmCur15MinRxLargeFragments_Object = MibTableColumn
g9982PortPmCur15MinRxLargeFragments = _G9982PortPmCur15MinRxLargeFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 6),
    _G9982PortPmCur15MinRxLargeFragments_Type()
)
g9982PortPmCur15MinRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxLargeFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxLargeFragments.setUnits("fragments")
_G9982PortPmCur15MinRxBadFragments_Type = HCPerfCurrentCount
_G9982PortPmCur15MinRxBadFragments_Object = MibTableColumn
g9982PortPmCur15MinRxBadFragments = _G9982PortPmCur15MinRxBadFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 7),
    _G9982PortPmCur15MinRxBadFragments_Type()
)
g9982PortPmCur15MinRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxBadFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxBadFragments.setUnits("fragments")
_G9982PortPmCur15MinRxLostFragments_Type = HCPerfCurrentCount
_G9982PortPmCur15MinRxLostFragments_Object = MibTableColumn
g9982PortPmCur15MinRxLostFragments = _G9982PortPmCur15MinRxLostFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 8),
    _G9982PortPmCur15MinRxLostFragments_Type()
)
g9982PortPmCur15MinRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxLostFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxLostFragments.setUnits("fragments")
_G9982PortPmCur15MinRxLostStarts_Type = HCPerfCurrentCount
_G9982PortPmCur15MinRxLostStarts_Object = MibTableColumn
g9982PortPmCur15MinRxLostStarts = _G9982PortPmCur15MinRxLostStarts_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 9),
    _G9982PortPmCur15MinRxLostStarts_Type()
)
g9982PortPmCur15MinRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxLostStarts.setStatus("current")
_G9982PortPmCur15MinRxLostEnds_Type = HCPerfCurrentCount
_G9982PortPmCur15MinRxLostEnds_Object = MibTableColumn
g9982PortPmCur15MinRxLostEnds = _G9982PortPmCur15MinRxLostEnds_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 10),
    _G9982PortPmCur15MinRxLostEnds_Type()
)
g9982PortPmCur15MinRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxLostEnds.setStatus("current")
_G9982PortPmCur15MinRxOverflows_Type = HCPerfCurrentCount
_G9982PortPmCur15MinRxOverflows_Object = MibTableColumn
g9982PortPmCur15MinRxOverflows = _G9982PortPmCur15MinRxOverflows_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 11),
    _G9982PortPmCur15MinRxOverflows_Type()
)
g9982PortPmCur15MinRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxOverflows.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur15MinRxOverflows.setUnits("fragments")


class _G9982PortPm1DayValidIntervals_Type(Unsigned32):
    """Custom type g9982PortPm1DayValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_G9982PortPm1DayValidIntervals_Type.__name__ = "Unsigned32"
_G9982PortPm1DayValidIntervals_Object = MibTableColumn
g9982PortPm1DayValidIntervals = _G9982PortPm1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 12),
    _G9982PortPm1DayValidIntervals_Type()
)
g9982PortPm1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayValidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm1DayValidIntervals.setUnits("days")


class _G9982PortPm1DayInvalidIntervals_Type(Unsigned32):
    """Custom type g9982PortPm1DayInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_G9982PortPm1DayInvalidIntervals_Type.__name__ = "Unsigned32"
_G9982PortPm1DayInvalidIntervals_Object = MibTableColumn
g9982PortPm1DayInvalidIntervals = _G9982PortPm1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 13),
    _G9982PortPm1DayInvalidIntervals_Type()
)
g9982PortPm1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm1DayInvalidIntervals.setUnits("days")
_G9982PortPmCur1DayTimeElapsed_Type = HCPerfTimeElapsed
_G9982PortPmCur1DayTimeElapsed_Object = MibTableColumn
g9982PortPmCur1DayTimeElapsed = _G9982PortPmCur1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 14),
    _G9982PortPmCur1DayTimeElapsed_Type()
)
g9982PortPmCur1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayTimeElapsed.setUnits("seconds")
_G9982PortPmCur1DayRxErrors_Type = HCPerfCurrentCount
_G9982PortPmCur1DayRxErrors_Object = MibTableColumn
g9982PortPmCur1DayRxErrors = _G9982PortPmCur1DayRxErrors_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 15),
    _G9982PortPmCur1DayRxErrors_Type()
)
g9982PortPmCur1DayRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxErrors.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxErrors.setUnits("fragments")
_G9982PortPmCur1DayRxSmallFragments_Type = HCPerfCurrentCount
_G9982PortPmCur1DayRxSmallFragments_Object = MibTableColumn
g9982PortPmCur1DayRxSmallFragments = _G9982PortPmCur1DayRxSmallFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 16),
    _G9982PortPmCur1DayRxSmallFragments_Type()
)
g9982PortPmCur1DayRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxSmallFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxSmallFragments.setUnits("fragments")
_G9982PortPmCur1DayRxLargeFragments_Type = HCPerfCurrentCount
_G9982PortPmCur1DayRxLargeFragments_Object = MibTableColumn
g9982PortPmCur1DayRxLargeFragments = _G9982PortPmCur1DayRxLargeFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 17),
    _G9982PortPmCur1DayRxLargeFragments_Type()
)
g9982PortPmCur1DayRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxLargeFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxLargeFragments.setUnits("fragments")
_G9982PortPmCur1DayRxBadFragments_Type = HCPerfCurrentCount
_G9982PortPmCur1DayRxBadFragments_Object = MibTableColumn
g9982PortPmCur1DayRxBadFragments = _G9982PortPmCur1DayRxBadFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 18),
    _G9982PortPmCur1DayRxBadFragments_Type()
)
g9982PortPmCur1DayRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxBadFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxBadFragments.setUnits("fragments")
_G9982PortPmCur1DayRxLostFragments_Type = HCPerfCurrentCount
_G9982PortPmCur1DayRxLostFragments_Object = MibTableColumn
g9982PortPmCur1DayRxLostFragments = _G9982PortPmCur1DayRxLostFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 19),
    _G9982PortPmCur1DayRxLostFragments_Type()
)
g9982PortPmCur1DayRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxLostFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxLostFragments.setUnits("fragments")
_G9982PortPmCur1DayRxLostStarts_Type = HCPerfCurrentCount
_G9982PortPmCur1DayRxLostStarts_Object = MibTableColumn
g9982PortPmCur1DayRxLostStarts = _G9982PortPmCur1DayRxLostStarts_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 20),
    _G9982PortPmCur1DayRxLostStarts_Type()
)
g9982PortPmCur1DayRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxLostStarts.setStatus("current")
_G9982PortPmCur1DayRxLostEnds_Type = HCPerfCurrentCount
_G9982PortPmCur1DayRxLostEnds_Object = MibTableColumn
g9982PortPmCur1DayRxLostEnds = _G9982PortPmCur1DayRxLostEnds_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 21),
    _G9982PortPmCur1DayRxLostEnds_Type()
)
g9982PortPmCur1DayRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxLostEnds.setStatus("current")
_G9982PortPmCur1DayRxOverflows_Type = HCPerfCurrentCount
_G9982PortPmCur1DayRxOverflows_Object = MibTableColumn
g9982PortPmCur1DayRxOverflows = _G9982PortPmCur1DayRxOverflows_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 1, 1, 22),
    _G9982PortPmCur1DayRxOverflows_Type()
)
g9982PortPmCur1DayRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxOverflows.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPmCur1DayRxOverflows.setUnits("fragments")
_G9982PortPm15MinTable_Object = MibTable
g9982PortPm15MinTable = _G9982PortPm15MinTable_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    g9982PortPm15MinTable.setStatus("current")
_G9982PortPm15MinEntry_Object = MibTableRow
g9982PortPm15MinEntry = _G9982PortPm15MinEntry_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1)
)
g9982PortPm15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "G9982-MIB", "g9982PortPm15MinIntervalIndex"),
)
if mibBuilder.loadTexts:
    g9982PortPm15MinEntry.setStatus("current")


class _G9982PortPm15MinIntervalIndex_Type(Unsigned32):
    """Custom type g9982PortPm15MinIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_G9982PortPm15MinIntervalIndex_Type.__name__ = "Unsigned32"
_G9982PortPm15MinIntervalIndex_Object = MibTableColumn
g9982PortPm15MinIntervalIndex = _G9982PortPm15MinIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1, 1),
    _G9982PortPm15MinIntervalIndex_Type()
)
g9982PortPm15MinIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalIndex.setStatus("current")
_G9982PortPm15MinIntervalMoniTime_Type = HCPerfTimeElapsed
_G9982PortPm15MinIntervalMoniTime_Object = MibTableColumn
g9982PortPm15MinIntervalMoniTime = _G9982PortPm15MinIntervalMoniTime_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1, 2),
    _G9982PortPm15MinIntervalMoniTime_Type()
)
g9982PortPm15MinIntervalMoniTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalMoniTime.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalMoniTime.setUnits("seconds")
_G9982PortPm15MinIntervalRxErrors_Type = HCPerfCurrentCount
_G9982PortPm15MinIntervalRxErrors_Object = MibTableColumn
g9982PortPm15MinIntervalRxErrors = _G9982PortPm15MinIntervalRxErrors_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1, 3),
    _G9982PortPm15MinIntervalRxErrors_Type()
)
g9982PortPm15MinIntervalRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxErrors.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxErrors.setUnits("fragments")
_G9982PortPm15MinIntervalRxSmallFragments_Type = HCPerfCurrentCount
_G9982PortPm15MinIntervalRxSmallFragments_Object = MibTableColumn
g9982PortPm15MinIntervalRxSmallFragments = _G9982PortPm15MinIntervalRxSmallFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1, 4),
    _G9982PortPm15MinIntervalRxSmallFragments_Type()
)
g9982PortPm15MinIntervalRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxSmallFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxSmallFragments.setUnits("fragments")
_G9982PortPm15MinIntervalRxLargeFragments_Type = HCPerfCurrentCount
_G9982PortPm15MinIntervalRxLargeFragments_Object = MibTableColumn
g9982PortPm15MinIntervalRxLargeFragments = _G9982PortPm15MinIntervalRxLargeFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1, 5),
    _G9982PortPm15MinIntervalRxLargeFragments_Type()
)
g9982PortPm15MinIntervalRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxLargeFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxLargeFragments.setUnits("fragments")
_G9982PortPm15MinIntervalRxBadFragments_Type = HCPerfCurrentCount
_G9982PortPm15MinIntervalRxBadFragments_Object = MibTableColumn
g9982PortPm15MinIntervalRxBadFragments = _G9982PortPm15MinIntervalRxBadFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1, 6),
    _G9982PortPm15MinIntervalRxBadFragments_Type()
)
g9982PortPm15MinIntervalRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxBadFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxBadFragments.setUnits("fragments")
_G9982PortPm15MinIntervalRxLostFragments_Type = HCPerfCurrentCount
_G9982PortPm15MinIntervalRxLostFragments_Object = MibTableColumn
g9982PortPm15MinIntervalRxLostFragments = _G9982PortPm15MinIntervalRxLostFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1, 7),
    _G9982PortPm15MinIntervalRxLostFragments_Type()
)
g9982PortPm15MinIntervalRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxLostFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxLostFragments.setUnits("fragments")
_G9982PortPm15MinIntervalRxLostStarts_Type = HCPerfCurrentCount
_G9982PortPm15MinIntervalRxLostStarts_Object = MibTableColumn
g9982PortPm15MinIntervalRxLostStarts = _G9982PortPm15MinIntervalRxLostStarts_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1, 8),
    _G9982PortPm15MinIntervalRxLostStarts_Type()
)
g9982PortPm15MinIntervalRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxLostStarts.setStatus("current")
_G9982PortPm15MinIntervalRxLostEnds_Type = HCPerfCurrentCount
_G9982PortPm15MinIntervalRxLostEnds_Object = MibTableColumn
g9982PortPm15MinIntervalRxLostEnds = _G9982PortPm15MinIntervalRxLostEnds_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1, 9),
    _G9982PortPm15MinIntervalRxLostEnds_Type()
)
g9982PortPm15MinIntervalRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxLostEnds.setStatus("current")
_G9982PortPm15MinIntervalRxOverflows_Type = HCPerfCurrentCount
_G9982PortPm15MinIntervalRxOverflows_Object = MibTableColumn
g9982PortPm15MinIntervalRxOverflows = _G9982PortPm15MinIntervalRxOverflows_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1, 10),
    _G9982PortPm15MinIntervalRxOverflows_Type()
)
g9982PortPm15MinIntervalRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxOverflows.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalRxOverflows.setUnits("fragments")
_G9982PortPm15MinIntervalValid_Type = TruthValue
_G9982PortPm15MinIntervalValid_Object = MibTableColumn
g9982PortPm15MinIntervalValid = _G9982PortPm15MinIntervalValid_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 2, 1, 11),
    _G9982PortPm15MinIntervalValid_Type()
)
g9982PortPm15MinIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm15MinIntervalValid.setStatus("current")
_G9982PortPm1DayTable_Object = MibTable
g9982PortPm1DayTable = _G9982PortPm1DayTable_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    g9982PortPm1DayTable.setStatus("current")
_G9982PortPm1DayEntry_Object = MibTableRow
g9982PortPm1DayEntry = _G9982PortPm1DayEntry_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1)
)
g9982PortPm1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "G9982-MIB", "g9982PortPm1DayIntervalIndex"),
)
if mibBuilder.loadTexts:
    g9982PortPm1DayEntry.setStatus("current")


class _G9982PortPm1DayIntervalIndex_Type(Unsigned32):
    """Custom type g9982PortPm1DayIntervalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_G9982PortPm1DayIntervalIndex_Type.__name__ = "Unsigned32"
_G9982PortPm1DayIntervalIndex_Object = MibTableColumn
g9982PortPm1DayIntervalIndex = _G9982PortPm1DayIntervalIndex_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1, 1),
    _G9982PortPm1DayIntervalIndex_Type()
)
g9982PortPm1DayIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalIndex.setStatus("current")
_G9982PortPm1DayIntervalMoniTime_Type = HCPerfTimeElapsed
_G9982PortPm1DayIntervalMoniTime_Object = MibTableColumn
g9982PortPm1DayIntervalMoniTime = _G9982PortPm1DayIntervalMoniTime_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1, 2),
    _G9982PortPm1DayIntervalMoniTime_Type()
)
g9982PortPm1DayIntervalMoniTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalMoniTime.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalMoniTime.setUnits("seconds")
_G9982PortPm1DayIntervalRxErrors_Type = HCPerfCurrentCount
_G9982PortPm1DayIntervalRxErrors_Object = MibTableColumn
g9982PortPm1DayIntervalRxErrors = _G9982PortPm1DayIntervalRxErrors_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1, 3),
    _G9982PortPm1DayIntervalRxErrors_Type()
)
g9982PortPm1DayIntervalRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxErrors.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxErrors.setUnits("fragments")
_G9982PortPm1DayIntervalRxSmallFragments_Type = HCPerfCurrentCount
_G9982PortPm1DayIntervalRxSmallFragments_Object = MibTableColumn
g9982PortPm1DayIntervalRxSmallFragments = _G9982PortPm1DayIntervalRxSmallFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1, 4),
    _G9982PortPm1DayIntervalRxSmallFragments_Type()
)
g9982PortPm1DayIntervalRxSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxSmallFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxSmallFragments.setUnits("fragments")
_G9982PortPm1DayIntervalRxLargeFragments_Type = HCPerfCurrentCount
_G9982PortPm1DayIntervalRxLargeFragments_Object = MibTableColumn
g9982PortPm1DayIntervalRxLargeFragments = _G9982PortPm1DayIntervalRxLargeFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1, 5),
    _G9982PortPm1DayIntervalRxLargeFragments_Type()
)
g9982PortPm1DayIntervalRxLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxLargeFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxLargeFragments.setUnits("fragments")
_G9982PortPm1DayIntervalRxBadFragments_Type = HCPerfCurrentCount
_G9982PortPm1DayIntervalRxBadFragments_Object = MibTableColumn
g9982PortPm1DayIntervalRxBadFragments = _G9982PortPm1DayIntervalRxBadFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1, 6),
    _G9982PortPm1DayIntervalRxBadFragments_Type()
)
g9982PortPm1DayIntervalRxBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxBadFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxBadFragments.setUnits("fragments")
_G9982PortPm1DayIntervalRxLostFragments_Type = HCPerfCurrentCount
_G9982PortPm1DayIntervalRxLostFragments_Object = MibTableColumn
g9982PortPm1DayIntervalRxLostFragments = _G9982PortPm1DayIntervalRxLostFragments_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1, 7),
    _G9982PortPm1DayIntervalRxLostFragments_Type()
)
g9982PortPm1DayIntervalRxLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxLostFragments.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxLostFragments.setUnits("fragments")
_G9982PortPm1DayIntervalRxLostStarts_Type = HCPerfCurrentCount
_G9982PortPm1DayIntervalRxLostStarts_Object = MibTableColumn
g9982PortPm1DayIntervalRxLostStarts = _G9982PortPm1DayIntervalRxLostStarts_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1, 8),
    _G9982PortPm1DayIntervalRxLostStarts_Type()
)
g9982PortPm1DayIntervalRxLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxLostStarts.setStatus("current")
_G9982PortPm1DayIntervalRxLostEnds_Type = HCPerfCurrentCount
_G9982PortPm1DayIntervalRxLostEnds_Object = MibTableColumn
g9982PortPm1DayIntervalRxLostEnds = _G9982PortPm1DayIntervalRxLostEnds_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1, 9),
    _G9982PortPm1DayIntervalRxLostEnds_Type()
)
g9982PortPm1DayIntervalRxLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxLostEnds.setStatus("current")
_G9982PortPm1DayIntervalRxOverflows_Type = HCPerfCurrentCount
_G9982PortPm1DayIntervalRxOverflows_Object = MibTableColumn
g9982PortPm1DayIntervalRxOverflows = _G9982PortPm1DayIntervalRxOverflows_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1, 10),
    _G9982PortPm1DayIntervalRxOverflows_Type()
)
g9982PortPm1DayIntervalRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxOverflows.setStatus("current")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalRxOverflows.setUnits("fragments")
_G9982PortPm1DayIntervalValid_Type = TruthValue
_G9982PortPm1DayIntervalValid_Object = MibTableColumn
g9982PortPm1DayIntervalValid = _G9982PortPm1DayIntervalValid_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 1, 4, 3, 1, 11),
    _G9982PortPm1DayIntervalValid_Type()
)
g9982PortPm1DayIntervalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982PortPm1DayIntervalValid.setStatus("current")
_G9982Bce_ObjectIdentity = ObjectIdentity
g9982Bce = _G9982Bce_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 264, 1, 2)
)
_G9982BceConfTable_Object = MibTable
g9982BceConfTable = _G9982BceConfTable_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 2, 1)
)
if mibBuilder.loadTexts:
    g9982BceConfTable.setStatus("current")
_G9982BceConfEntry_Object = MibTableRow
g9982BceConfEntry = _G9982BceConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 2, 1, 1)
)
g9982BceConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9982BceConfEntry.setStatus("current")


class _G9982BceConfEligibleGroupID_Type(PhysAddress):
    """Custom type g9982BceConfEligibleGroupID based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_G9982BceConfEligibleGroupID_Type.__name__ = "PhysAddress"
_G9982BceConfEligibleGroupID_Object = MibTableColumn
g9982BceConfEligibleGroupID = _G9982BceConfEligibleGroupID_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 2, 1, 1, 1),
    _G9982BceConfEligibleGroupID_Type()
)
g9982BceConfEligibleGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g9982BceConfEligibleGroupID.setStatus("current")


class _G9982BceConfPeerEligibleGroupID_Type(PhysAddress):
    """Custom type g9982BceConfPeerEligibleGroupID based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_G9982BceConfPeerEligibleGroupID_Type.__name__ = "PhysAddress"
_G9982BceConfPeerEligibleGroupID_Object = MibTableColumn
g9982BceConfPeerEligibleGroupID = _G9982BceConfPeerEligibleGroupID_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 2, 1, 1, 2),
    _G9982BceConfPeerEligibleGroupID_Type()
)
g9982BceConfPeerEligibleGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982BceConfPeerEligibleGroupID.setStatus("current")
_G9982BceStatTable_Object = MibTable
g9982BceStatTable = _G9982BceStatTable_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 2, 2)
)
if mibBuilder.loadTexts:
    g9982BceStatTable.setStatus("current")
_G9982BceStatEntry_Object = MibTableRow
g9982BceStatEntry = _G9982BceStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 2, 2, 1)
)
g9982BceStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    g9982BceStatEntry.setStatus("current")
_G9982BceStatTcInCodingErrors_Type = Counter32
_G9982BceStatTcInCodingErrors_Object = MibTableColumn
g9982BceStatTcInCodingErrors = _G9982BceStatTcInCodingErrors_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 2, 2, 1, 1),
    _G9982BceStatTcInCodingErrors_Type()
)
g9982BceStatTcInCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982BceStatTcInCodingErrors.setStatus("current")
_G9982BceStatTcInCrcErrors_Type = Counter32
_G9982BceStatTcInCrcErrors_Object = MibTableColumn
g9982BceStatTcInCrcErrors = _G9982BceStatTcInCrcErrors_Object(
    (1, 3, 6, 1, 2, 1, 264, 1, 2, 2, 1, 2),
    _G9982BceStatTcInCrcErrors_Type()
)
g9982BceStatTcInCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g9982BceStatTcInCrcErrors.setStatus("current")
_G9982Conformance_ObjectIdentity = ObjectIdentity
g9982Conformance = _G9982Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 264, 2)
)
_G9982Groups_ObjectIdentity = ObjectIdentity
g9982Groups = _G9982Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 264, 2, 1)
)
_G9982Compliances_ObjectIdentity = ObjectIdentity
g9982Compliances = _G9982Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 264, 2, 2)
)

# Managed Objects groups

g9982BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 264, 2, 1, 1)
)
g9982BasicGroup.setObjects(
      *(("G9982-MIB", "g9982PortCapTcTypesSupported"),
        ("G9982-MIB", "g9982PortCapBacpSupported"),
        ("G9982-MIB", "g9982PortConfTcAdminType"),
        ("G9982-MIB", "g9982PortStatTcOperType"),
        ("G9982-MIB", "g9982PortStatRxErrors"),
        ("G9982-MIB", "g9982PortStatRxSmallFragments"),
        ("G9982-MIB", "g9982PortStatRxLargeFragments"),
        ("G9982-MIB", "g9982PortStatRxBadFragments"),
        ("G9982-MIB", "g9982PortStatRxLostFragments"),
        ("G9982-MIB", "g9982PortStatRxLostStarts"),
        ("G9982-MIB", "g9982PortStatRxLostEnds"),
        ("G9982-MIB", "g9982PortStatRxOverflows"),
        ("G9982-MIB", "g9982BceStatTcInCodingErrors"),
        ("G9982-MIB", "g9982BceStatTcInCrcErrors"))
)
if mibBuilder.loadTexts:
    g9982BasicGroup.setStatus("current")

g9982BacpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 264, 2, 1, 2)
)
g9982BacpGroup.setObjects(
      *(("G9982-MIB", "g9982PortConfAdminCp"),
        ("G9982-MIB", "g9982PortStatOperCp"),
        ("G9982-MIB", "g9982BceConfEligibleGroupID"),
        ("G9982-MIB", "g9982BceConfPeerEligibleGroupID"))
)
if mibBuilder.loadTexts:
    g9982BacpGroup.setStatus("current")

g9982BceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 264, 2, 1, 3)
)
g9982BceGroup.setObjects(
      *(("G9982-MIB", "g9982BceStatTcInCodingErrors"),
        ("G9982-MIB", "g9982BceStatTcInCrcErrors"))
)
if mibBuilder.loadTexts:
    g9982BceGroup.setStatus("current")

g9982PerfCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 264, 2, 1, 4)
)
g9982PerfCurrGroup.setObjects(
      *(("G9982-MIB", "g9982PortPm15MinValidIntervals"),
        ("G9982-MIB", "g9982PortPm15MinInvalidIntervals"),
        ("G9982-MIB", "g9982PortPmCur15MinTimeElapsed"),
        ("G9982-MIB", "g9982PortPmCur15MinRxErrors"),
        ("G9982-MIB", "g9982PortPmCur15MinRxSmallFragments"),
        ("G9982-MIB", "g9982PortPmCur15MinRxLargeFragments"),
        ("G9982-MIB", "g9982PortPmCur15MinRxBadFragments"),
        ("G9982-MIB", "g9982PortPmCur15MinRxLostFragments"),
        ("G9982-MIB", "g9982PortPmCur15MinRxLostStarts"),
        ("G9982-MIB", "g9982PortPmCur15MinRxLostEnds"),
        ("G9982-MIB", "g9982PortPmCur15MinRxOverflows"),
        ("G9982-MIB", "g9982PortPm1DayValidIntervals"),
        ("G9982-MIB", "g9982PortPm1DayInvalidIntervals"),
        ("G9982-MIB", "g9982PortPmCur1DayTimeElapsed"),
        ("G9982-MIB", "g9982PortPmCur1DayRxErrors"),
        ("G9982-MIB", "g9982PortPmCur1DayRxSmallFragments"),
        ("G9982-MIB", "g9982PortPmCur1DayRxLargeFragments"),
        ("G9982-MIB", "g9982PortPmCur1DayRxBadFragments"),
        ("G9982-MIB", "g9982PortPmCur1DayRxLostFragments"),
        ("G9982-MIB", "g9982PortPmCur1DayRxLostStarts"),
        ("G9982-MIB", "g9982PortPmCur1DayRxLostEnds"),
        ("G9982-MIB", "g9982PortPmCur1DayRxOverflows"))
)
if mibBuilder.loadTexts:
    g9982PerfCurrGroup.setStatus("current")

g9982Perf15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 264, 2, 1, 5)
)
g9982Perf15MinGroup.setObjects(
      *(("G9982-MIB", "g9982PortPm15MinIntervalMoniTime"),
        ("G9982-MIB", "g9982PortPm15MinIntervalRxErrors"),
        ("G9982-MIB", "g9982PortPm15MinIntervalRxSmallFragments"),
        ("G9982-MIB", "g9982PortPm15MinIntervalRxLargeFragments"),
        ("G9982-MIB", "g9982PortPm15MinIntervalRxBadFragments"),
        ("G9982-MIB", "g9982PortPm15MinIntervalRxLostFragments"),
        ("G9982-MIB", "g9982PortPm15MinIntervalRxLostStarts"),
        ("G9982-MIB", "g9982PortPm15MinIntervalRxLostEnds"),
        ("G9982-MIB", "g9982PortPm15MinIntervalRxOverflows"),
        ("G9982-MIB", "g9982PortPm15MinIntervalValid"))
)
if mibBuilder.loadTexts:
    g9982Perf15MinGroup.setStatus("current")

g9982Perf1DayGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 264, 2, 1, 6)
)
g9982Perf1DayGroup.setObjects(
      *(("G9982-MIB", "g9982PortPm1DayIntervalMoniTime"),
        ("G9982-MIB", "g9982PortPm1DayIntervalRxErrors"),
        ("G9982-MIB", "g9982PortPm1DayIntervalRxSmallFragments"),
        ("G9982-MIB", "g9982PortPm1DayIntervalRxLargeFragments"),
        ("G9982-MIB", "g9982PortPm1DayIntervalRxBadFragments"),
        ("G9982-MIB", "g9982PortPm1DayIntervalRxLostFragments"),
        ("G9982-MIB", "g9982PortPm1DayIntervalRxLostStarts"),
        ("G9982-MIB", "g9982PortPm1DayIntervalRxLostEnds"),
        ("G9982-MIB", "g9982PortPm1DayIntervalRxOverflows"),
        ("G9982-MIB", "g9982PortPm1DayIntervalValid"))
)
if mibBuilder.loadTexts:
    g9982Perf1DayGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

g9982Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 264, 2, 2, 1)
)
if mibBuilder.loadTexts:
    g9982Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G9982-MIB",
    **{"G9982PtmTcType": G9982PtmTcType,
       "G9982CpType": G9982CpType,
       "g9982MIB": g9982MIB,
       "g9982Objects": g9982Objects,
       "g9982Port": g9982Port,
       "g9982PortConfTable": g9982PortConfTable,
       "g9982PortConfEntry": g9982PortConfEntry,
       "g9982PortConfTcAdminType": g9982PortConfTcAdminType,
       "g9982PortConfAdminCp": g9982PortConfAdminCp,
       "g9982PortCapTable": g9982PortCapTable,
       "g9982PortCapEntry": g9982PortCapEntry,
       "g9982PortCapTcTypesSupported": g9982PortCapTcTypesSupported,
       "g9982PortCapBacpSupported": g9982PortCapBacpSupported,
       "g9982PortStatTable": g9982PortStatTable,
       "g9982PortStatEntry": g9982PortStatEntry,
       "g9982PortStatTcOperType": g9982PortStatTcOperType,
       "g9982PortStatOperCp": g9982PortStatOperCp,
       "g9982PortStatRxErrors": g9982PortStatRxErrors,
       "g9982PortStatRxSmallFragments": g9982PortStatRxSmallFragments,
       "g9982PortStatRxLargeFragments": g9982PortStatRxLargeFragments,
       "g9982PortStatRxBadFragments": g9982PortStatRxBadFragments,
       "g9982PortStatRxLostFragments": g9982PortStatRxLostFragments,
       "g9982PortStatRxLostStarts": g9982PortStatRxLostStarts,
       "g9982PortStatRxLostEnds": g9982PortStatRxLostEnds,
       "g9982PortStatRxOverflows": g9982PortStatRxOverflows,
       "g9982PM": g9982PM,
       "g9982PortPmCurTable": g9982PortPmCurTable,
       "g9982PortPmCurEntry": g9982PortPmCurEntry,
       "g9982PortPm15MinValidIntervals": g9982PortPm15MinValidIntervals,
       "g9982PortPm15MinInvalidIntervals": g9982PortPm15MinInvalidIntervals,
       "g9982PortPmCur15MinTimeElapsed": g9982PortPmCur15MinTimeElapsed,
       "g9982PortPmCur15MinRxErrors": g9982PortPmCur15MinRxErrors,
       "g9982PortPmCur15MinRxSmallFragments": g9982PortPmCur15MinRxSmallFragments,
       "g9982PortPmCur15MinRxLargeFragments": g9982PortPmCur15MinRxLargeFragments,
       "g9982PortPmCur15MinRxBadFragments": g9982PortPmCur15MinRxBadFragments,
       "g9982PortPmCur15MinRxLostFragments": g9982PortPmCur15MinRxLostFragments,
       "g9982PortPmCur15MinRxLostStarts": g9982PortPmCur15MinRxLostStarts,
       "g9982PortPmCur15MinRxLostEnds": g9982PortPmCur15MinRxLostEnds,
       "g9982PortPmCur15MinRxOverflows": g9982PortPmCur15MinRxOverflows,
       "g9982PortPm1DayValidIntervals": g9982PortPm1DayValidIntervals,
       "g9982PortPm1DayInvalidIntervals": g9982PortPm1DayInvalidIntervals,
       "g9982PortPmCur1DayTimeElapsed": g9982PortPmCur1DayTimeElapsed,
       "g9982PortPmCur1DayRxErrors": g9982PortPmCur1DayRxErrors,
       "g9982PortPmCur1DayRxSmallFragments": g9982PortPmCur1DayRxSmallFragments,
       "g9982PortPmCur1DayRxLargeFragments": g9982PortPmCur1DayRxLargeFragments,
       "g9982PortPmCur1DayRxBadFragments": g9982PortPmCur1DayRxBadFragments,
       "g9982PortPmCur1DayRxLostFragments": g9982PortPmCur1DayRxLostFragments,
       "g9982PortPmCur1DayRxLostStarts": g9982PortPmCur1DayRxLostStarts,
       "g9982PortPmCur1DayRxLostEnds": g9982PortPmCur1DayRxLostEnds,
       "g9982PortPmCur1DayRxOverflows": g9982PortPmCur1DayRxOverflows,
       "g9982PortPm15MinTable": g9982PortPm15MinTable,
       "g9982PortPm15MinEntry": g9982PortPm15MinEntry,
       "g9982PortPm15MinIntervalIndex": g9982PortPm15MinIntervalIndex,
       "g9982PortPm15MinIntervalMoniTime": g9982PortPm15MinIntervalMoniTime,
       "g9982PortPm15MinIntervalRxErrors": g9982PortPm15MinIntervalRxErrors,
       "g9982PortPm15MinIntervalRxSmallFragments": g9982PortPm15MinIntervalRxSmallFragments,
       "g9982PortPm15MinIntervalRxLargeFragments": g9982PortPm15MinIntervalRxLargeFragments,
       "g9982PortPm15MinIntervalRxBadFragments": g9982PortPm15MinIntervalRxBadFragments,
       "g9982PortPm15MinIntervalRxLostFragments": g9982PortPm15MinIntervalRxLostFragments,
       "g9982PortPm15MinIntervalRxLostStarts": g9982PortPm15MinIntervalRxLostStarts,
       "g9982PortPm15MinIntervalRxLostEnds": g9982PortPm15MinIntervalRxLostEnds,
       "g9982PortPm15MinIntervalRxOverflows": g9982PortPm15MinIntervalRxOverflows,
       "g9982PortPm15MinIntervalValid": g9982PortPm15MinIntervalValid,
       "g9982PortPm1DayTable": g9982PortPm1DayTable,
       "g9982PortPm1DayEntry": g9982PortPm1DayEntry,
       "g9982PortPm1DayIntervalIndex": g9982PortPm1DayIntervalIndex,
       "g9982PortPm1DayIntervalMoniTime": g9982PortPm1DayIntervalMoniTime,
       "g9982PortPm1DayIntervalRxErrors": g9982PortPm1DayIntervalRxErrors,
       "g9982PortPm1DayIntervalRxSmallFragments": g9982PortPm1DayIntervalRxSmallFragments,
       "g9982PortPm1DayIntervalRxLargeFragments": g9982PortPm1DayIntervalRxLargeFragments,
       "g9982PortPm1DayIntervalRxBadFragments": g9982PortPm1DayIntervalRxBadFragments,
       "g9982PortPm1DayIntervalRxLostFragments": g9982PortPm1DayIntervalRxLostFragments,
       "g9982PortPm1DayIntervalRxLostStarts": g9982PortPm1DayIntervalRxLostStarts,
       "g9982PortPm1DayIntervalRxLostEnds": g9982PortPm1DayIntervalRxLostEnds,
       "g9982PortPm1DayIntervalRxOverflows": g9982PortPm1DayIntervalRxOverflows,
       "g9982PortPm1DayIntervalValid": g9982PortPm1DayIntervalValid,
       "g9982Bce": g9982Bce,
       "g9982BceConfTable": g9982BceConfTable,
       "g9982BceConfEntry": g9982BceConfEntry,
       "g9982BceConfEligibleGroupID": g9982BceConfEligibleGroupID,
       "g9982BceConfPeerEligibleGroupID": g9982BceConfPeerEligibleGroupID,
       "g9982BceStatTable": g9982BceStatTable,
       "g9982BceStatEntry": g9982BceStatEntry,
       "g9982BceStatTcInCodingErrors": g9982BceStatTcInCodingErrors,
       "g9982BceStatTcInCrcErrors": g9982BceStatTcInCrcErrors,
       "g9982Conformance": g9982Conformance,
       "g9982Groups": g9982Groups,
       "g9982BasicGroup": g9982BasicGroup,
       "g9982BacpGroup": g9982BacpGroup,
       "g9982BceGroup": g9982BceGroup,
       "g9982PerfCurrGroup": g9982PerfCurrGroup,
       "g9982Perf15MinGroup": g9982Perf15MinGroup,
       "g9982Perf1DayGroup": g9982Perf1DayGroup,
       "g9982Compliances": g9982Compliances,
       "g9982Compliance": g9982Compliance}
)
