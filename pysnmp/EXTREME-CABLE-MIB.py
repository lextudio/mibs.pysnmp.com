# SNMP MIB module (EXTREME-CABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(extremeAgent,
 extremeV2Traps,
 extremenetworks) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent",
    "extremeV2Traps",
    "extremenetworks")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeCable = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeDiagConfigGroup_ObjectIdentity = ObjectIdentity
extremeDiagConfigGroup = _ExtremeDiagConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 1)
)


class _ExtremeDiagConfigTime_Type(DisplayString):
    """Custom type extremeDiagConfigTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ExtremeDiagConfigTime_Type.__name__ = "DisplayString"
_ExtremeDiagConfigTime_Object = MibScalar
extremeDiagConfigTime = _ExtremeDiagConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 1, 1),
    _ExtremeDiagConfigTime_Type()
)
extremeDiagConfigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDiagConfigTime.setStatus("current")


class _ExtremeDiagConfigRoF_Type(Integer32):
    """Custom type extremeDiagConfigRoF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ExtremeDiagConfigRoF_Type.__name__ = "Integer32"
_ExtremeDiagConfigRoF_Object = MibScalar
extremeDiagConfigRoF = _ExtremeDiagConfigRoF_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 1, 2),
    _ExtremeDiagConfigRoF_Type()
)
extremeDiagConfigRoF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDiagConfigRoF.setStatus("current")
_ExtremeDiagPortConfigTable_Object = MibTable
extremeDiagPortConfigTable = _ExtremeDiagPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 2)
)
if mibBuilder.loadTexts:
    extremeDiagPortConfigTable.setStatus("current")
_ExtremeDiagPortConfigEntry_Object = MibTableRow
extremeDiagPortConfigEntry = _ExtremeDiagPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 2, 1)
)
extremeDiagPortConfigEntry.setIndexNames(
    (0, "EXTREME-CABLE-MIB", "extremeDiagPortCfgPortIfIndex"),
    (0, "EXTREME-CABLE-MIB", "extremeDiagPortCfgMode"),
)
if mibBuilder.loadTexts:
    extremeDiagPortConfigEntry.setStatus("current")
_ExtremeDiagPortCfgPortIfIndex_Type = Integer32
_ExtremeDiagPortCfgPortIfIndex_Object = MibTableColumn
extremeDiagPortCfgPortIfIndex = _ExtremeDiagPortCfgPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 2, 1, 1),
    _ExtremeDiagPortCfgPortIfIndex_Type()
)
extremeDiagPortCfgPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortCfgPortIfIndex.setStatus("current")


class _ExtremeDiagPortCfgMode_Type(Integer32):
    """Custom type extremeDiagPortCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_ExtremeDiagPortCfgMode_Type.__name__ = "Integer32"
_ExtremeDiagPortCfgMode_Object = MibTableColumn
extremeDiagPortCfgMode = _ExtremeDiagPortCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 2, 1, 2),
    _ExtremeDiagPortCfgMode_Type()
)
extremeDiagPortCfgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortCfgMode.setStatus("current")


class _ExtremeDiagPortCfgStatus_Type(Integer32):
    """Custom type extremeDiagPortCfgStatus based on Integer32"""
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
        *(("diagfail", 4),
          ("disable", 2),
          ("enable", 1),
          ("run", 3))
    )


_ExtremeDiagPortCfgStatus_Type.__name__ = "Integer32"
_ExtremeDiagPortCfgStatus_Object = MibTableColumn
extremeDiagPortCfgStatus = _ExtremeDiagPortCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 2, 1, 3),
    _ExtremeDiagPortCfgStatus_Type()
)
extremeDiagPortCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeDiagPortCfgStatus.setStatus("current")
_ExtremeDiagPortDiagTable_Object = MibTable
extremeDiagPortDiagTable = _ExtremeDiagPortDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3)
)
if mibBuilder.loadTexts:
    extremeDiagPortDiagTable.setStatus("current")
_ExtremeDiagPortDiagEntry_Object = MibTableRow
extremeDiagPortDiagEntry = _ExtremeDiagPortDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1)
)
extremeDiagPortDiagEntry.setIndexNames(
    (0, "EXTREME-CABLE-MIB", "extremeDiagPortDiagPortIfIndex"),
    (0, "EXTREME-CABLE-MIB", "extremeDiagPortDiagMode"),
)
if mibBuilder.loadTexts:
    extremeDiagPortDiagEntry.setStatus("current")
_ExtremeDiagPortDiagPortIfIndex_Type = Integer32
_ExtremeDiagPortDiagPortIfIndex_Object = MibTableColumn
extremeDiagPortDiagPortIfIndex = _ExtremeDiagPortDiagPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 1),
    _ExtremeDiagPortDiagPortIfIndex_Type()
)
extremeDiagPortDiagPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortDiagPortIfIndex.setStatus("current")


class _ExtremeDiagPortDiagMode_Type(Integer32):
    """Custom type extremeDiagPortDiagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_ExtremeDiagPortDiagMode_Type.__name__ = "Integer32"
_ExtremeDiagPortDiagMode_Object = MibTableColumn
extremeDiagPortDiagMode = _ExtremeDiagPortDiagMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 2),
    _ExtremeDiagPortDiagMode_Type()
)
extremeDiagPortDiagMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortDiagMode.setStatus("current")


class _ExtremeDiagPortSpeed_Type(Integer32):
    """Custom type extremeDiagPortSpeed based on Integer32"""
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
        *(("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3),
          ("unknown", 4))
    )


_ExtremeDiagPortSpeed_Type.__name__ = "Integer32"
_ExtremeDiagPortSpeed_Object = MibTableColumn
extremeDiagPortSpeed = _ExtremeDiagPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 3),
    _ExtremeDiagPortSpeed_Type()
)
extremeDiagPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortSpeed.setStatus("current")


class _ExtremeDiagPortSwapAB_Type(Integer32):
    """Custom type extremeDiagPortSwapAB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noswap", 2),
          ("swap", 1),
          ("unknown", 3))
    )


_ExtremeDiagPortSwapAB_Type.__name__ = "Integer32"
_ExtremeDiagPortSwapAB_Object = MibTableColumn
extremeDiagPortSwapAB = _ExtremeDiagPortSwapAB_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 4),
    _ExtremeDiagPortSwapAB_Type()
)
extremeDiagPortSwapAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortSwapAB.setStatus("current")


class _ExtremeDiagPortSwapCD_Type(Integer32):
    """Custom type extremeDiagPortSwapCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noswap", 2),
          ("swap", 1),
          ("unknown", 3))
    )


_ExtremeDiagPortSwapCD_Type.__name__ = "Integer32"
_ExtremeDiagPortSwapCD_Object = MibTableColumn
extremeDiagPortSwapCD = _ExtremeDiagPortSwapCD_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 5),
    _ExtremeDiagPortSwapCD_Type()
)
extremeDiagPortSwapCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortSwapCD.setStatus("current")


class _ExtremeDiagPortPairAPol_Type(Integer32):
    """Custom type extremeDiagPortPairAPol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1),
          ("unknown", 3))
    )


_ExtremeDiagPortPairAPol_Type.__name__ = "Integer32"
_ExtremeDiagPortPairAPol_Object = MibTableColumn
extremeDiagPortPairAPol = _ExtremeDiagPortPairAPol_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 6),
    _ExtremeDiagPortPairAPol_Type()
)
extremeDiagPortPairAPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairAPol.setStatus("current")
_ExtremeDiagPortPairAFlen_Type = Integer32
_ExtremeDiagPortPairAFlen_Object = MibTableColumn
extremeDiagPortPairAFlen = _ExtremeDiagPortPairAFlen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 7),
    _ExtremeDiagPortPairAFlen_Type()
)
extremeDiagPortPairAFlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairAFlen.setStatus("current")
_ExtremeDiagPortPairALen_Type = Integer32
_ExtremeDiagPortPairALen_Object = MibTableColumn
extremeDiagPortPairALen = _ExtremeDiagPortPairALen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 8),
    _ExtremeDiagPortPairALen_Type()
)
extremeDiagPortPairALen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairALen.setStatus("current")
_ExtremeDiagPortPairASkew_Type = Integer32
_ExtremeDiagPortPairASkew_Object = MibTableColumn
extremeDiagPortPairASkew = _ExtremeDiagPortPairASkew_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 9),
    _ExtremeDiagPortPairASkew_Type()
)
extremeDiagPortPairASkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairASkew.setStatus("current")


class _ExtremeDiagPortPairAStatus_Type(Integer32):
    """Custom type extremeDiagPortPairAStatus based on Integer32"""
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
        *(("imperror", 4),
          ("open", 1),
          ("short", 2),
          ("terminated", 3),
          ("unknown", 5))
    )


_ExtremeDiagPortPairAStatus_Type.__name__ = "Integer32"
_ExtremeDiagPortPairAStatus_Object = MibTableColumn
extremeDiagPortPairAStatus = _ExtremeDiagPortPairAStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 10),
    _ExtremeDiagPortPairAStatus_Type()
)
extremeDiagPortPairAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairAStatus.setStatus("current")


class _ExtremeDiagPortPairBPol_Type(Integer32):
    """Custom type extremeDiagPortPairBPol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1),
          ("unknown", 3))
    )


_ExtremeDiagPortPairBPol_Type.__name__ = "Integer32"
_ExtremeDiagPortPairBPol_Object = MibTableColumn
extremeDiagPortPairBPol = _ExtremeDiagPortPairBPol_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 11),
    _ExtremeDiagPortPairBPol_Type()
)
extremeDiagPortPairBPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairBPol.setStatus("current")
_ExtremeDiagPortPairBFlen_Type = Integer32
_ExtremeDiagPortPairBFlen_Object = MibTableColumn
extremeDiagPortPairBFlen = _ExtremeDiagPortPairBFlen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 12),
    _ExtremeDiagPortPairBFlen_Type()
)
extremeDiagPortPairBFlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairBFlen.setStatus("current")
_ExtremeDiagPortPairBLen_Type = Integer32
_ExtremeDiagPortPairBLen_Object = MibTableColumn
extremeDiagPortPairBLen = _ExtremeDiagPortPairBLen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 13),
    _ExtremeDiagPortPairBLen_Type()
)
extremeDiagPortPairBLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairBLen.setStatus("current")
_ExtremeDiagPortPairBSkew_Type = Integer32
_ExtremeDiagPortPairBSkew_Object = MibTableColumn
extremeDiagPortPairBSkew = _ExtremeDiagPortPairBSkew_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 14),
    _ExtremeDiagPortPairBSkew_Type()
)
extremeDiagPortPairBSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairBSkew.setStatus("current")


class _ExtremeDiagPortPairBStatus_Type(Integer32):
    """Custom type extremeDiagPortPairBStatus based on Integer32"""
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
        *(("imperror", 4),
          ("open", 1),
          ("short", 2),
          ("terminated", 3),
          ("unknown", 5))
    )


_ExtremeDiagPortPairBStatus_Type.__name__ = "Integer32"
_ExtremeDiagPortPairBStatus_Object = MibTableColumn
extremeDiagPortPairBStatus = _ExtremeDiagPortPairBStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 15),
    _ExtremeDiagPortPairBStatus_Type()
)
extremeDiagPortPairBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairBStatus.setStatus("current")


class _ExtremeDiagPortPairCPol_Type(Integer32):
    """Custom type extremeDiagPortPairCPol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1),
          ("unknown", 3))
    )


_ExtremeDiagPortPairCPol_Type.__name__ = "Integer32"
_ExtremeDiagPortPairCPol_Object = MibTableColumn
extremeDiagPortPairCPol = _ExtremeDiagPortPairCPol_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 16),
    _ExtremeDiagPortPairCPol_Type()
)
extremeDiagPortPairCPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairCPol.setStatus("current")
_ExtremeDiagPortPairCFlen_Type = Integer32
_ExtremeDiagPortPairCFlen_Object = MibTableColumn
extremeDiagPortPairCFlen = _ExtremeDiagPortPairCFlen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 17),
    _ExtremeDiagPortPairCFlen_Type()
)
extremeDiagPortPairCFlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairCFlen.setStatus("current")
_ExtremeDiagPortPairCLen_Type = Integer32
_ExtremeDiagPortPairCLen_Object = MibTableColumn
extremeDiagPortPairCLen = _ExtremeDiagPortPairCLen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 18),
    _ExtremeDiagPortPairCLen_Type()
)
extremeDiagPortPairCLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairCLen.setStatus("current")
_ExtremeDiagPortPairCSkew_Type = Integer32
_ExtremeDiagPortPairCSkew_Object = MibTableColumn
extremeDiagPortPairCSkew = _ExtremeDiagPortPairCSkew_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 19),
    _ExtremeDiagPortPairCSkew_Type()
)
extremeDiagPortPairCSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairCSkew.setStatus("current")


class _ExtremeDiagPortPairCStatus_Type(Integer32):
    """Custom type extremeDiagPortPairCStatus based on Integer32"""
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
        *(("imperror", 4),
          ("open", 1),
          ("short", 2),
          ("terminated", 3),
          ("unknown", 5))
    )


_ExtremeDiagPortPairCStatus_Type.__name__ = "Integer32"
_ExtremeDiagPortPairCStatus_Object = MibTableColumn
extremeDiagPortPairCStatus = _ExtremeDiagPortPairCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 20),
    _ExtremeDiagPortPairCStatus_Type()
)
extremeDiagPortPairCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairCStatus.setStatus("current")


class _ExtremeDiagPortPairDPol_Type(Integer32):
    """Custom type extremeDiagPortPairDPol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negative", 2),
          ("positive", 1),
          ("unknown", 3))
    )


_ExtremeDiagPortPairDPol_Type.__name__ = "Integer32"
_ExtremeDiagPortPairDPol_Object = MibTableColumn
extremeDiagPortPairDPol = _ExtremeDiagPortPairDPol_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 21),
    _ExtremeDiagPortPairDPol_Type()
)
extremeDiagPortPairDPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairDPol.setStatus("current")
_ExtremeDiagPortPairDFlen_Type = Integer32
_ExtremeDiagPortPairDFlen_Object = MibTableColumn
extremeDiagPortPairDFlen = _ExtremeDiagPortPairDFlen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 22),
    _ExtremeDiagPortPairDFlen_Type()
)
extremeDiagPortPairDFlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairDFlen.setStatus("current")
_ExtremeDiagPortPairDLen_Type = Integer32
_ExtremeDiagPortPairDLen_Object = MibTableColumn
extremeDiagPortPairDLen = _ExtremeDiagPortPairDLen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 23),
    _ExtremeDiagPortPairDLen_Type()
)
extremeDiagPortPairDLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairDLen.setStatus("current")
_ExtremeDiagPortPairDSkew_Type = Integer32
_ExtremeDiagPortPairDSkew_Object = MibTableColumn
extremeDiagPortPairDSkew = _ExtremeDiagPortPairDSkew_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 24),
    _ExtremeDiagPortPairDSkew_Type()
)
extremeDiagPortPairDSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairDSkew.setStatus("current")


class _ExtremeDiagPortPairDStatus_Type(Integer32):
    """Custom type extremeDiagPortPairDStatus based on Integer32"""
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
        *(("imperror", 4),
          ("open", 1),
          ("short", 2),
          ("terminated", 3),
          ("unknown", 5))
    )


_ExtremeDiagPortPairDStatus_Type.__name__ = "Integer32"
_ExtremeDiagPortPairDStatus_Object = MibTableColumn
extremeDiagPortPairDStatus = _ExtremeDiagPortPairDStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 25),
    _ExtremeDiagPortPairDStatus_Type()
)
extremeDiagPortPairDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortPairDStatus.setStatus("current")


class _ExtremeDiagPortDateTime_Type(DisplayString):
    """Custom type extremeDiagPortDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ExtremeDiagPortDateTime_Type.__name__ = "DisplayString"
_ExtremeDiagPortDateTime_Object = MibTableColumn
extremeDiagPortDateTime = _ExtremeDiagPortDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 26),
    _ExtremeDiagPortDateTime_Type()
)
extremeDiagPortDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortDateTime.setStatus("current")
_ExtremeDiagPortStatsTable_Object = MibTable
extremeDiagPortStatsTable = _ExtremeDiagPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 4)
)
if mibBuilder.loadTexts:
    extremeDiagPortStatsTable.setStatus("current")
_ExtremeDiagPortStatsEntry_Object = MibTableRow
extremeDiagPortStatsEntry = _ExtremeDiagPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1)
)
extremeDiagPortStatsEntry.setIndexNames(
    (0, "EXTREME-CABLE-MIB", "extremeDiagPortStatsPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeDiagPortStatsEntry.setStatus("current")
_ExtremeDiagPortStatsPortIfIndex_Type = Integer32
_ExtremeDiagPortStatsPortIfIndex_Object = MibTableColumn
extremeDiagPortStatsPortIfIndex = _ExtremeDiagPortStatsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 1),
    _ExtremeDiagPortStatsPortIfIndex_Type()
)
extremeDiagPortStatsPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortStatsPortIfIndex.setStatus("current")
_ExtremeDiagPortStatsNumDiag_Type = Integer32
_ExtremeDiagPortStatsNumDiag_Object = MibTableColumn
extremeDiagPortStatsNumDiag = _ExtremeDiagPortStatsNumDiag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 2),
    _ExtremeDiagPortStatsNumDiag_Type()
)
extremeDiagPortStatsNumDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortStatsNumDiag.setStatus("current")
_ExtremeDiagPortStatsNumSuccess_Type = Integer32
_ExtremeDiagPortStatsNumSuccess_Object = MibTableColumn
extremeDiagPortStatsNumSuccess = _ExtremeDiagPortStatsNumSuccess_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 3),
    _ExtremeDiagPortStatsNumSuccess_Type()
)
extremeDiagPortStatsNumSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortStatsNumSuccess.setStatus("current")
_ExtremeDiagPortStatsNumFail_Type = Integer32
_ExtremeDiagPortStatsNumFail_Object = MibTableColumn
extremeDiagPortStatsNumFail = _ExtremeDiagPortStatsNumFail_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 4),
    _ExtremeDiagPortStatsNumFail_Type()
)
extremeDiagPortStatsNumFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortStatsNumFail.setStatus("current")
_ExtremeDiagPortStatsNumChange_Type = Integer32
_ExtremeDiagPortStatsNumChange_Object = MibTableColumn
extremeDiagPortStatsNumChange = _ExtremeDiagPortStatsNumChange_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 5),
    _ExtremeDiagPortStatsNumChange_Type()
)
extremeDiagPortStatsNumChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortStatsNumChange.setStatus("current")
_ExtremeDiagPortStatsNumAbort_Type = Integer32
_ExtremeDiagPortStatsNumAbort_Object = MibTableColumn
extremeDiagPortStatsNumAbort = _ExtremeDiagPortStatsNumAbort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 6),
    _ExtremeDiagPortStatsNumAbort_Type()
)
extremeDiagPortStatsNumAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeDiagPortStatsNumAbort.setStatus("current")
_ExtremeCableTraps_ObjectIdentity = ObjectIdentity
extremeCableTraps = _ExtremeCableTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 13)
)
_ExtremeCableTrapsPrefix_ObjectIdentity = ObjectIdentity
extremeCableTrapsPrefix = _ExtremeCableTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4, 13, 0)
)

# Managed Objects groups


# Notification objects

extremeTrapDiagPortDiagnostics = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 4, 13, 0, 1)
)
extremeTrapDiagPortDiagnostics.setObjects(
      *(("EXTREME-CABLE-MIB", "extremeDiagPortCfgPortIfIndex"),
        ("EXTREME-CABLE-MIB", "extremeDiagPortCfgMode"),
        ("EXTREME-CABLE-MIB", "extremeDiagPortCfgStatus"))
)
if mibBuilder.loadTexts:
    extremeTrapDiagPortDiagnostics.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-CABLE-MIB",
    **{"extremeCable": extremeCable,
       "extremeDiagConfigGroup": extremeDiagConfigGroup,
       "extremeDiagConfigTime": extremeDiagConfigTime,
       "extremeDiagConfigRoF": extremeDiagConfigRoF,
       "extremeDiagPortConfigTable": extremeDiagPortConfigTable,
       "extremeDiagPortConfigEntry": extremeDiagPortConfigEntry,
       "extremeDiagPortCfgPortIfIndex": extremeDiagPortCfgPortIfIndex,
       "extremeDiagPortCfgMode": extremeDiagPortCfgMode,
       "extremeDiagPortCfgStatus": extremeDiagPortCfgStatus,
       "extremeDiagPortDiagTable": extremeDiagPortDiagTable,
       "extremeDiagPortDiagEntry": extremeDiagPortDiagEntry,
       "extremeDiagPortDiagPortIfIndex": extremeDiagPortDiagPortIfIndex,
       "extremeDiagPortDiagMode": extremeDiagPortDiagMode,
       "extremeDiagPortSpeed": extremeDiagPortSpeed,
       "extremeDiagPortSwapAB": extremeDiagPortSwapAB,
       "extremeDiagPortSwapCD": extremeDiagPortSwapCD,
       "extremeDiagPortPairAPol": extremeDiagPortPairAPol,
       "extremeDiagPortPairAFlen": extremeDiagPortPairAFlen,
       "extremeDiagPortPairALen": extremeDiagPortPairALen,
       "extremeDiagPortPairASkew": extremeDiagPortPairASkew,
       "extremeDiagPortPairAStatus": extremeDiagPortPairAStatus,
       "extremeDiagPortPairBPol": extremeDiagPortPairBPol,
       "extremeDiagPortPairBFlen": extremeDiagPortPairBFlen,
       "extremeDiagPortPairBLen": extremeDiagPortPairBLen,
       "extremeDiagPortPairBSkew": extremeDiagPortPairBSkew,
       "extremeDiagPortPairBStatus": extremeDiagPortPairBStatus,
       "extremeDiagPortPairCPol": extremeDiagPortPairCPol,
       "extremeDiagPortPairCFlen": extremeDiagPortPairCFlen,
       "extremeDiagPortPairCLen": extremeDiagPortPairCLen,
       "extremeDiagPortPairCSkew": extremeDiagPortPairCSkew,
       "extremeDiagPortPairCStatus": extremeDiagPortPairCStatus,
       "extremeDiagPortPairDPol": extremeDiagPortPairDPol,
       "extremeDiagPortPairDFlen": extremeDiagPortPairDFlen,
       "extremeDiagPortPairDLen": extremeDiagPortPairDLen,
       "extremeDiagPortPairDSkew": extremeDiagPortPairDSkew,
       "extremeDiagPortPairDStatus": extremeDiagPortPairDStatus,
       "extremeDiagPortDateTime": extremeDiagPortDateTime,
       "extremeDiagPortStatsTable": extremeDiagPortStatsTable,
       "extremeDiagPortStatsEntry": extremeDiagPortStatsEntry,
       "extremeDiagPortStatsPortIfIndex": extremeDiagPortStatsPortIfIndex,
       "extremeDiagPortStatsNumDiag": extremeDiagPortStatsNumDiag,
       "extremeDiagPortStatsNumSuccess": extremeDiagPortStatsNumSuccess,
       "extremeDiagPortStatsNumFail": extremeDiagPortStatsNumFail,
       "extremeDiagPortStatsNumChange": extremeDiagPortStatsNumChange,
       "extremeDiagPortStatsNumAbort": extremeDiagPortStatsNumAbort,
       "extremeCableTraps": extremeCableTraps,
       "extremeCableTrapsPrefix": extremeCableTrapsPrefix,
       "extremeTrapDiagPortDiagnostics": extremeTrapDiagPortDiagnostics}
)
