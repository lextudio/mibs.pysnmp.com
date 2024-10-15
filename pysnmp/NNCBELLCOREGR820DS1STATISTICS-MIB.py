# SNMP MIB module (NNCBELLCOREGR820DS1STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCBELLCOREGR820DS1STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:16 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtensions")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nncBellcoreGR820Ds1Statistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 70)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncBellcoreGR820Ds1StatisticsObjects_ObjectIdentity = ObjectIdentity
nncBellcoreGR820Ds1StatisticsObjects = _NncBellcoreGR820Ds1StatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1)
)
_NncBellcoreGR820Ds1CurrStatsTable_Object = MibTable
nncBellcoreGR820Ds1CurrStatsTable = _NncBellcoreGR820Ds1CurrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1)
)
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrStatsTable.setStatus("current")
_NncBellcoreGR820Ds1CurrStatsEntry_Object = MibTableRow
nncBellcoreGR820Ds1CurrStatsEntry = _NncBellcoreGR820Ds1CurrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1)
)
nncBellcoreGR820Ds1CurrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrStatsEntry.setStatus("current")
_NncBellcoreGR820Ds1CurrLineCV_Type = Counter32
_NncBellcoreGR820Ds1CurrLineCV_Object = MibTableColumn
nncBellcoreGR820Ds1CurrLineCV = _NncBellcoreGR820Ds1CurrLineCV_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 1),
    _NncBellcoreGR820Ds1CurrLineCV_Type()
)
nncBellcoreGR820Ds1CurrLineCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrLineCV.setStatus("current")
_NncBellcoreGR820Ds1CurrLineES_Type = Counter32
_NncBellcoreGR820Ds1CurrLineES_Object = MibTableColumn
nncBellcoreGR820Ds1CurrLineES = _NncBellcoreGR820Ds1CurrLineES_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 2),
    _NncBellcoreGR820Ds1CurrLineES_Type()
)
nncBellcoreGR820Ds1CurrLineES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrLineES.setStatus("current")
_NncBellcoreGR820Ds1CurrLineLOSS_Type = Counter32
_NncBellcoreGR820Ds1CurrLineLOSS_Object = MibTableColumn
nncBellcoreGR820Ds1CurrLineLOSS = _NncBellcoreGR820Ds1CurrLineLOSS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 3),
    _NncBellcoreGR820Ds1CurrLineLOSS_Type()
)
nncBellcoreGR820Ds1CurrLineLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrLineLOSS.setStatus("current")
_NncBellcoreGR820Ds1CurrPathCV_Type = Counter32
_NncBellcoreGR820Ds1CurrPathCV_Object = MibTableColumn
nncBellcoreGR820Ds1CurrPathCV = _NncBellcoreGR820Ds1CurrPathCV_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 4),
    _NncBellcoreGR820Ds1CurrPathCV_Type()
)
nncBellcoreGR820Ds1CurrPathCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrPathCV.setStatus("current")
_NncBellcoreGR820Ds1CurrPathES_Type = Counter32
_NncBellcoreGR820Ds1CurrPathES_Object = MibTableColumn
nncBellcoreGR820Ds1CurrPathES = _NncBellcoreGR820Ds1CurrPathES_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 5),
    _NncBellcoreGR820Ds1CurrPathES_Type()
)
nncBellcoreGR820Ds1CurrPathES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrPathES.setStatus("current")
_NncBellcoreGR820Ds1CurrPathSES_Type = Counter32
_NncBellcoreGR820Ds1CurrPathSES_Object = MibTableColumn
nncBellcoreGR820Ds1CurrPathSES = _NncBellcoreGR820Ds1CurrPathSES_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 6),
    _NncBellcoreGR820Ds1CurrPathSES_Type()
)
nncBellcoreGR820Ds1CurrPathSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrPathSES.setStatus("current")
_NncBellcoreGR820Ds1CurrPathAISS_Type = Counter32
_NncBellcoreGR820Ds1CurrPathAISS_Object = MibTableColumn
nncBellcoreGR820Ds1CurrPathAISS = _NncBellcoreGR820Ds1CurrPathAISS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 7),
    _NncBellcoreGR820Ds1CurrPathAISS_Type()
)
nncBellcoreGR820Ds1CurrPathAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrPathAISS.setStatus("current")
_NncBellcoreGR820Ds1CurrPathCSS_Type = Counter32
_NncBellcoreGR820Ds1CurrPathCSS_Object = MibTableColumn
nncBellcoreGR820Ds1CurrPathCSS = _NncBellcoreGR820Ds1CurrPathCSS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 8),
    _NncBellcoreGR820Ds1CurrPathCSS_Type()
)
nncBellcoreGR820Ds1CurrPathCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrPathCSS.setStatus("current")
_NncBellcoreGR820Ds1CurrPathUAS_Type = Counter32
_NncBellcoreGR820Ds1CurrPathUAS_Object = MibTableColumn
nncBellcoreGR820Ds1CurrPathUAS = _NncBellcoreGR820Ds1CurrPathUAS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 9),
    _NncBellcoreGR820Ds1CurrPathUAS_Type()
)
nncBellcoreGR820Ds1CurrPathUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrPathUAS.setStatus("current")
_NncBellcoreGR820Ds1CurrPathSAS_Type = Counter32
_NncBellcoreGR820Ds1CurrPathSAS_Object = MibTableColumn
nncBellcoreGR820Ds1CurrPathSAS = _NncBellcoreGR820Ds1CurrPathSAS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 10),
    _NncBellcoreGR820Ds1CurrPathSAS_Type()
)
nncBellcoreGR820Ds1CurrPathSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrPathSAS.setStatus("current")
_NncBellcoreGR820Ds1CurrPathFC_Type = Counter32
_NncBellcoreGR820Ds1CurrPathFC_Object = MibTableColumn
nncBellcoreGR820Ds1CurrPathFC = _NncBellcoreGR820Ds1CurrPathFC_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 11),
    _NncBellcoreGR820Ds1CurrPathFC_Type()
)
nncBellcoreGR820Ds1CurrPathFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrPathFC.setStatus("current")
_NncBellcoreGR820Ds1IntervalStatsTable_Object = MibTable
nncBellcoreGR820Ds1IntervalStatsTable = _NncBellcoreGR820Ds1IntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2)
)
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalStatsTable.setStatus("current")
_NncBellcoreGR820Ds1IntervalStatsEntry_Object = MibTableRow
nncBellcoreGR820Ds1IntervalStatsEntry = _NncBellcoreGR820Ds1IntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1)
)
nncBellcoreGR820Ds1IntervalStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalIndex"),
)
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalStatsEntry.setStatus("current")


class _NncBellcoreGR820Ds1IntervalIndex_Type(Integer32):
    """Custom type nncBellcoreGR820Ds1IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncBellcoreGR820Ds1IntervalIndex_Type.__name__ = "Integer32"
_NncBellcoreGR820Ds1IntervalIndex_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalIndex = _NncBellcoreGR820Ds1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 1),
    _NncBellcoreGR820Ds1IntervalIndex_Type()
)
nncBellcoreGR820Ds1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalIndex.setStatus("current")
_NncBellcoreGR820Ds1IntervalLineCV_Type = Counter32
_NncBellcoreGR820Ds1IntervalLineCV_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalLineCV = _NncBellcoreGR820Ds1IntervalLineCV_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 2),
    _NncBellcoreGR820Ds1IntervalLineCV_Type()
)
nncBellcoreGR820Ds1IntervalLineCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalLineCV.setStatus("current")
_NncBellcoreGR820Ds1IntervalLineES_Type = Counter32
_NncBellcoreGR820Ds1IntervalLineES_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalLineES = _NncBellcoreGR820Ds1IntervalLineES_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 3),
    _NncBellcoreGR820Ds1IntervalLineES_Type()
)
nncBellcoreGR820Ds1IntervalLineES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalLineES.setStatus("current")
_NncBellcoreGR820Ds1IntervalLineLOSS_Type = Counter32
_NncBellcoreGR820Ds1IntervalLineLOSS_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalLineLOSS = _NncBellcoreGR820Ds1IntervalLineLOSS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 4),
    _NncBellcoreGR820Ds1IntervalLineLOSS_Type()
)
nncBellcoreGR820Ds1IntervalLineLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalLineLOSS.setStatus("current")
_NncBellcoreGR820Ds1IntervalPathCV_Type = Counter32
_NncBellcoreGR820Ds1IntervalPathCV_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalPathCV = _NncBellcoreGR820Ds1IntervalPathCV_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 5),
    _NncBellcoreGR820Ds1IntervalPathCV_Type()
)
nncBellcoreGR820Ds1IntervalPathCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalPathCV.setStatus("current")
_NncBellcoreGR820Ds1IntervalPathES_Type = Counter32
_NncBellcoreGR820Ds1IntervalPathES_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalPathES = _NncBellcoreGR820Ds1IntervalPathES_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 6),
    _NncBellcoreGR820Ds1IntervalPathES_Type()
)
nncBellcoreGR820Ds1IntervalPathES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalPathES.setStatus("current")
_NncBellcoreGR820Ds1IntervalPathSES_Type = Counter32
_NncBellcoreGR820Ds1IntervalPathSES_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalPathSES = _NncBellcoreGR820Ds1IntervalPathSES_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 7),
    _NncBellcoreGR820Ds1IntervalPathSES_Type()
)
nncBellcoreGR820Ds1IntervalPathSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalPathSES.setStatus("current")
_NncBellcoreGR820Ds1IntervalPathAISS_Type = Counter32
_NncBellcoreGR820Ds1IntervalPathAISS_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalPathAISS = _NncBellcoreGR820Ds1IntervalPathAISS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 8),
    _NncBellcoreGR820Ds1IntervalPathAISS_Type()
)
nncBellcoreGR820Ds1IntervalPathAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalPathAISS.setStatus("current")
_NncBellcoreGR820Ds1IntervalPathCSS_Type = Counter32
_NncBellcoreGR820Ds1IntervalPathCSS_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalPathCSS = _NncBellcoreGR820Ds1IntervalPathCSS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 9),
    _NncBellcoreGR820Ds1IntervalPathCSS_Type()
)
nncBellcoreGR820Ds1IntervalPathCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalPathCSS.setStatus("current")
_NncBellcoreGR820Ds1IntervalPathUAS_Type = Counter32
_NncBellcoreGR820Ds1IntervalPathUAS_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalPathUAS = _NncBellcoreGR820Ds1IntervalPathUAS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 10),
    _NncBellcoreGR820Ds1IntervalPathUAS_Type()
)
nncBellcoreGR820Ds1IntervalPathUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalPathUAS.setStatus("current")
_NncBellcoreGR820Ds1IntervalPathSAS_Type = Counter32
_NncBellcoreGR820Ds1IntervalPathSAS_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalPathSAS = _NncBellcoreGR820Ds1IntervalPathSAS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 11),
    _NncBellcoreGR820Ds1IntervalPathSAS_Type()
)
nncBellcoreGR820Ds1IntervalPathSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalPathSAS.setStatus("current")
_NncBellcoreGR820Ds1IntervalPathFC_Type = Counter32
_NncBellcoreGR820Ds1IntervalPathFC_Object = MibTableColumn
nncBellcoreGR820Ds1IntervalPathFC = _NncBellcoreGR820Ds1IntervalPathFC_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 12),
    _NncBellcoreGR820Ds1IntervalPathFC_Type()
)
nncBellcoreGR820Ds1IntervalPathFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalPathFC.setStatus("current")
_NncBellcoreGR820Ds1TotalStatsTable_Object = MibTable
nncBellcoreGR820Ds1TotalStatsTable = _NncBellcoreGR820Ds1TotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3)
)
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalStatsTable.setStatus("current")
_NncBellcoreGR820Ds1TotalStatsEntry_Object = MibTableRow
nncBellcoreGR820Ds1TotalStatsEntry = _NncBellcoreGR820Ds1TotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1)
)
nncBellcoreGR820Ds1TotalStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalStatsEntry.setStatus("current")
_NncBellcoreGR820Ds1TotalLineCV_Type = Counter32
_NncBellcoreGR820Ds1TotalLineCV_Object = MibTableColumn
nncBellcoreGR820Ds1TotalLineCV = _NncBellcoreGR820Ds1TotalLineCV_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 1),
    _NncBellcoreGR820Ds1TotalLineCV_Type()
)
nncBellcoreGR820Ds1TotalLineCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalLineCV.setStatus("current")
_NncBellcoreGR820Ds1TotalLineES_Type = Counter32
_NncBellcoreGR820Ds1TotalLineES_Object = MibTableColumn
nncBellcoreGR820Ds1TotalLineES = _NncBellcoreGR820Ds1TotalLineES_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 2),
    _NncBellcoreGR820Ds1TotalLineES_Type()
)
nncBellcoreGR820Ds1TotalLineES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalLineES.setStatus("current")
_NncBellcoreGR820Ds1TotalLineLOSS_Type = Counter32
_NncBellcoreGR820Ds1TotalLineLOSS_Object = MibTableColumn
nncBellcoreGR820Ds1TotalLineLOSS = _NncBellcoreGR820Ds1TotalLineLOSS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 3),
    _NncBellcoreGR820Ds1TotalLineLOSS_Type()
)
nncBellcoreGR820Ds1TotalLineLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalLineLOSS.setStatus("current")
_NncBellcoreGR820Ds1TotalPathCV_Type = Counter32
_NncBellcoreGR820Ds1TotalPathCV_Object = MibTableColumn
nncBellcoreGR820Ds1TotalPathCV = _NncBellcoreGR820Ds1TotalPathCV_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 4),
    _NncBellcoreGR820Ds1TotalPathCV_Type()
)
nncBellcoreGR820Ds1TotalPathCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalPathCV.setStatus("current")
_NncBellcoreGR820Ds1TotalPathES_Type = Counter32
_NncBellcoreGR820Ds1TotalPathES_Object = MibTableColumn
nncBellcoreGR820Ds1TotalPathES = _NncBellcoreGR820Ds1TotalPathES_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 5),
    _NncBellcoreGR820Ds1TotalPathES_Type()
)
nncBellcoreGR820Ds1TotalPathES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalPathES.setStatus("current")
_NncBellcoreGR820Ds1TotalPathSES_Type = Counter32
_NncBellcoreGR820Ds1TotalPathSES_Object = MibTableColumn
nncBellcoreGR820Ds1TotalPathSES = _NncBellcoreGR820Ds1TotalPathSES_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 6),
    _NncBellcoreGR820Ds1TotalPathSES_Type()
)
nncBellcoreGR820Ds1TotalPathSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalPathSES.setStatus("current")
_NncBellcoreGR820Ds1TotalPathAISS_Type = Counter32
_NncBellcoreGR820Ds1TotalPathAISS_Object = MibTableColumn
nncBellcoreGR820Ds1TotalPathAISS = _NncBellcoreGR820Ds1TotalPathAISS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 7),
    _NncBellcoreGR820Ds1TotalPathAISS_Type()
)
nncBellcoreGR820Ds1TotalPathAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalPathAISS.setStatus("current")
_NncBellcoreGR820Ds1TotalPathCSS_Type = Counter32
_NncBellcoreGR820Ds1TotalPathCSS_Object = MibTableColumn
nncBellcoreGR820Ds1TotalPathCSS = _NncBellcoreGR820Ds1TotalPathCSS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 8),
    _NncBellcoreGR820Ds1TotalPathCSS_Type()
)
nncBellcoreGR820Ds1TotalPathCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalPathCSS.setStatus("current")
_NncBellcoreGR820Ds1TotalPathUAS_Type = Counter32
_NncBellcoreGR820Ds1TotalPathUAS_Object = MibTableColumn
nncBellcoreGR820Ds1TotalPathUAS = _NncBellcoreGR820Ds1TotalPathUAS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 9),
    _NncBellcoreGR820Ds1TotalPathUAS_Type()
)
nncBellcoreGR820Ds1TotalPathUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalPathUAS.setStatus("current")
_NncBellcoreGR820Ds1TotalPathSAS_Type = Counter32
_NncBellcoreGR820Ds1TotalPathSAS_Object = MibTableColumn
nncBellcoreGR820Ds1TotalPathSAS = _NncBellcoreGR820Ds1TotalPathSAS_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 10),
    _NncBellcoreGR820Ds1TotalPathSAS_Type()
)
nncBellcoreGR820Ds1TotalPathSAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalPathSAS.setStatus("current")
_NncBellcoreGR820Ds1TotalPathFC_Type = Counter32
_NncBellcoreGR820Ds1TotalPathFC_Object = MibTableColumn
nncBellcoreGR820Ds1TotalPathFC = _NncBellcoreGR820Ds1TotalPathFC_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 11),
    _NncBellcoreGR820Ds1TotalPathFC_Type()
)
nncBellcoreGR820Ds1TotalPathFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalPathFC.setStatus("current")
_NncBellcoreGR820Ds1StatisticsGroups_ObjectIdentity = ObjectIdentity
nncBellcoreGR820Ds1StatisticsGroups = _NncBellcoreGR820Ds1StatisticsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 2)
)
_NncBellcoreGR820Ds1StatisticsCompliances_ObjectIdentity = ObjectIdentity
nncBellcoreGR820Ds1StatisticsCompliances = _NncBellcoreGR820Ds1StatisticsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 3)
)

# Managed Objects groups

nncBellcoreGR820Ds1CurrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 2, 1)
)
nncBellcoreGR820Ds1CurrStatsGroup.setObjects(
      *(("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrLineCV"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrLineES"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrLineLOSS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathCV"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathES"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathSES"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathAISS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathCSS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathUAS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathSAS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathFC"))
)
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1CurrStatsGroup.setStatus("current")

nncBellcoreGR820Ds1IntervalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 2, 2)
)
nncBellcoreGR820Ds1IntervalStatsGroup.setObjects(
      *(("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalIndex"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalLineCV"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalLineES"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalLineLOSS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathCV"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathES"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathSES"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathAISS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathCSS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathUAS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathSAS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathFC"))
)
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1IntervalStatsGroup.setStatus("current")

nncBellcoreGR820Ds1TotalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 2, 3)
)
nncBellcoreGR820Ds1TotalStatsGroup.setObjects(
      *(("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalLineCV"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalLineES"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalLineLOSS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathCV"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathES"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathSES"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathAISS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathCSS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathUAS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathSAS"),
        ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathFC"))
)
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1TotalStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncBellcoreGR820Ds1StatisticsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 70, 3, 1)
)
if mibBuilder.loadTexts:
    nncBellcoreGR820Ds1StatisticsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCBELLCOREGR820DS1STATISTICS-MIB",
    **{"nncBellcoreGR820Ds1Statistics": nncBellcoreGR820Ds1Statistics,
       "nncBellcoreGR820Ds1StatisticsObjects": nncBellcoreGR820Ds1StatisticsObjects,
       "nncBellcoreGR820Ds1CurrStatsTable": nncBellcoreGR820Ds1CurrStatsTable,
       "nncBellcoreGR820Ds1CurrStatsEntry": nncBellcoreGR820Ds1CurrStatsEntry,
       "nncBellcoreGR820Ds1CurrLineCV": nncBellcoreGR820Ds1CurrLineCV,
       "nncBellcoreGR820Ds1CurrLineES": nncBellcoreGR820Ds1CurrLineES,
       "nncBellcoreGR820Ds1CurrLineLOSS": nncBellcoreGR820Ds1CurrLineLOSS,
       "nncBellcoreGR820Ds1CurrPathCV": nncBellcoreGR820Ds1CurrPathCV,
       "nncBellcoreGR820Ds1CurrPathES": nncBellcoreGR820Ds1CurrPathES,
       "nncBellcoreGR820Ds1CurrPathSES": nncBellcoreGR820Ds1CurrPathSES,
       "nncBellcoreGR820Ds1CurrPathAISS": nncBellcoreGR820Ds1CurrPathAISS,
       "nncBellcoreGR820Ds1CurrPathCSS": nncBellcoreGR820Ds1CurrPathCSS,
       "nncBellcoreGR820Ds1CurrPathUAS": nncBellcoreGR820Ds1CurrPathUAS,
       "nncBellcoreGR820Ds1CurrPathSAS": nncBellcoreGR820Ds1CurrPathSAS,
       "nncBellcoreGR820Ds1CurrPathFC": nncBellcoreGR820Ds1CurrPathFC,
       "nncBellcoreGR820Ds1IntervalStatsTable": nncBellcoreGR820Ds1IntervalStatsTable,
       "nncBellcoreGR820Ds1IntervalStatsEntry": nncBellcoreGR820Ds1IntervalStatsEntry,
       "nncBellcoreGR820Ds1IntervalIndex": nncBellcoreGR820Ds1IntervalIndex,
       "nncBellcoreGR820Ds1IntervalLineCV": nncBellcoreGR820Ds1IntervalLineCV,
       "nncBellcoreGR820Ds1IntervalLineES": nncBellcoreGR820Ds1IntervalLineES,
       "nncBellcoreGR820Ds1IntervalLineLOSS": nncBellcoreGR820Ds1IntervalLineLOSS,
       "nncBellcoreGR820Ds1IntervalPathCV": nncBellcoreGR820Ds1IntervalPathCV,
       "nncBellcoreGR820Ds1IntervalPathES": nncBellcoreGR820Ds1IntervalPathES,
       "nncBellcoreGR820Ds1IntervalPathSES": nncBellcoreGR820Ds1IntervalPathSES,
       "nncBellcoreGR820Ds1IntervalPathAISS": nncBellcoreGR820Ds1IntervalPathAISS,
       "nncBellcoreGR820Ds1IntervalPathCSS": nncBellcoreGR820Ds1IntervalPathCSS,
       "nncBellcoreGR820Ds1IntervalPathUAS": nncBellcoreGR820Ds1IntervalPathUAS,
       "nncBellcoreGR820Ds1IntervalPathSAS": nncBellcoreGR820Ds1IntervalPathSAS,
       "nncBellcoreGR820Ds1IntervalPathFC": nncBellcoreGR820Ds1IntervalPathFC,
       "nncBellcoreGR820Ds1TotalStatsTable": nncBellcoreGR820Ds1TotalStatsTable,
       "nncBellcoreGR820Ds1TotalStatsEntry": nncBellcoreGR820Ds1TotalStatsEntry,
       "nncBellcoreGR820Ds1TotalLineCV": nncBellcoreGR820Ds1TotalLineCV,
       "nncBellcoreGR820Ds1TotalLineES": nncBellcoreGR820Ds1TotalLineES,
       "nncBellcoreGR820Ds1TotalLineLOSS": nncBellcoreGR820Ds1TotalLineLOSS,
       "nncBellcoreGR820Ds1TotalPathCV": nncBellcoreGR820Ds1TotalPathCV,
       "nncBellcoreGR820Ds1TotalPathES": nncBellcoreGR820Ds1TotalPathES,
       "nncBellcoreGR820Ds1TotalPathSES": nncBellcoreGR820Ds1TotalPathSES,
       "nncBellcoreGR820Ds1TotalPathAISS": nncBellcoreGR820Ds1TotalPathAISS,
       "nncBellcoreGR820Ds1TotalPathCSS": nncBellcoreGR820Ds1TotalPathCSS,
       "nncBellcoreGR820Ds1TotalPathUAS": nncBellcoreGR820Ds1TotalPathUAS,
       "nncBellcoreGR820Ds1TotalPathSAS": nncBellcoreGR820Ds1TotalPathSAS,
       "nncBellcoreGR820Ds1TotalPathFC": nncBellcoreGR820Ds1TotalPathFC,
       "nncBellcoreGR820Ds1StatisticsGroups": nncBellcoreGR820Ds1StatisticsGroups,
       "nncBellcoreGR820Ds1CurrStatsGroup": nncBellcoreGR820Ds1CurrStatsGroup,
       "nncBellcoreGR820Ds1IntervalStatsGroup": nncBellcoreGR820Ds1IntervalStatsGroup,
       "nncBellcoreGR820Ds1TotalStatsGroup": nncBellcoreGR820Ds1TotalStatsGroup,
       "nncBellcoreGR820Ds1StatisticsCompliances": nncBellcoreGR820Ds1StatisticsCompliances,
       "nncBellcoreGR820Ds1StatisticsCompliance": nncBellcoreGR820Ds1StatisticsCompliance}
)
