# SNMP MIB module (PDN-SPECTRUMMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-SPECTRUMMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:09 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifType")

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

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

pdnSpectrumMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19)
)
pdnSpectrumMgmt.setRevisions(
        ("2003-01-15 13:00",
         "2003-01-09 15:00",
         "1901-05-16 15:30",
         "1901-05-08 05:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnSpecMgmtObjects_ObjectIdentity = ObjectIdentity
pdnSpecMgmtObjects = _PdnSpecMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1)
)


class _SpectrumMgmtCountryCode_Type(Integer32):
    """Custom type spectrumMgmtCountryCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uk", 2),
          ("usa", 1))
    )


_SpectrumMgmtCountryCode_Type.__name__ = "Integer32"
_SpectrumMgmtCountryCode_Object = MibScalar
spectrumMgmtCountryCode = _SpectrumMgmtCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 2),
    _SpectrumMgmtCountryCode_Type()
)
spectrumMgmtCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spectrumMgmtCountryCode.setStatus("deprecated")
_SpectrumMgmtTable_Object = MibTable
spectrumMgmtTable = _SpectrumMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3)
)
if mibBuilder.loadTexts:
    spectrumMgmtTable.setStatus("deprecated")
_SpectrumMgmtEntry_Object = MibTableRow
spectrumMgmtEntry = _SpectrumMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1)
)
spectrumMgmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    spectrumMgmtEntry.setStatus("deprecated")
_SpectrumMgmtEWL_Type = Integer32
_SpectrumMgmtEWL_Object = MibTableColumn
spectrumMgmtEWL = _SpectrumMgmtEWL_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 1),
    _SpectrumMgmtEWL_Type()
)
spectrumMgmtEWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spectrumMgmtEWL.setStatus("deprecated")
_SpectrumMgmtAllowedSpeedsMin1_Type = Integer32
_SpectrumMgmtAllowedSpeedsMin1_Object = MibTableColumn
spectrumMgmtAllowedSpeedsMin1 = _SpectrumMgmtAllowedSpeedsMin1_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 2),
    _SpectrumMgmtAllowedSpeedsMin1_Type()
)
spectrumMgmtAllowedSpeedsMin1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spectrumMgmtAllowedSpeedsMin1.setStatus("deprecated")
_SpectrumMgmtAllowedSpeedsMax1_Type = Integer32
_SpectrumMgmtAllowedSpeedsMax1_Object = MibTableColumn
spectrumMgmtAllowedSpeedsMax1 = _SpectrumMgmtAllowedSpeedsMax1_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 3),
    _SpectrumMgmtAllowedSpeedsMax1_Type()
)
spectrumMgmtAllowedSpeedsMax1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spectrumMgmtAllowedSpeedsMax1.setStatus("deprecated")
_SpectrumMgmtAllowedSpeedsMin2_Type = Integer32
_SpectrumMgmtAllowedSpeedsMin2_Object = MibTableColumn
spectrumMgmtAllowedSpeedsMin2 = _SpectrumMgmtAllowedSpeedsMin2_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 4),
    _SpectrumMgmtAllowedSpeedsMin2_Type()
)
spectrumMgmtAllowedSpeedsMin2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spectrumMgmtAllowedSpeedsMin2.setStatus("deprecated")
_SpectrumMgmtAllowedSpeedsMax2_Type = Integer32
_SpectrumMgmtAllowedSpeedsMax2_Object = MibTableColumn
spectrumMgmtAllowedSpeedsMax2 = _SpectrumMgmtAllowedSpeedsMax2_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 5),
    _SpectrumMgmtAllowedSpeedsMax2_Type()
)
spectrumMgmtAllowedSpeedsMax2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spectrumMgmtAllowedSpeedsMax2.setStatus("deprecated")


class _SpectrumMgmtLineLength_Type(Integer32):
    """Custom type spectrumMgmtLineLength based on Integer32"""
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
        *(("long", 3),
          ("medium", 2),
          ("short", 1))
    )


_SpectrumMgmtLineLength_Type.__name__ = "Integer32"
_SpectrumMgmtLineLength_Object = MibTableColumn
spectrumMgmtLineLength = _SpectrumMgmtLineLength_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 1, 3, 1, 6),
    _SpectrumMgmtLineLength_Type()
)
spectrumMgmtLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spectrumMgmtLineLength.setStatus("deprecated")
_PdnNewSpecMgmtObjects_ObjectIdentity = ObjectIdentity
pdnNewSpecMgmtObjects = _PdnNewSpecMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2)
)
_NewSpectrumMgmtGeneralConfigTable_Object = MibTable
newSpectrumMgmtGeneralConfigTable = _NewSpectrumMgmtGeneralConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1)
)
if mibBuilder.loadTexts:
    newSpectrumMgmtGeneralConfigTable.setStatus("current")
_NewSpectrumMgmtGeneralConfigEntry_Object = MibTableRow
newSpectrumMgmtGeneralConfigEntry = _NewSpectrumMgmtGeneralConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1, 1)
)
newSpectrumMgmtGeneralConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "IF-MIB", "ifType"),
)
if mibBuilder.loadTexts:
    newSpectrumMgmtGeneralConfigEntry.setStatus("current")


class _NewSpectrumMgmtSelection_Type(Integer32):
    """Custom type newSpectrumMgmtSelection based on Integer32"""
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


_NewSpectrumMgmtSelection_Type.__name__ = "Integer32"
_NewSpectrumMgmtSelection_Object = MibTableColumn
newSpectrumMgmtSelection = _NewSpectrumMgmtSelection_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1, 1, 1),
    _NewSpectrumMgmtSelection_Type()
)
newSpectrumMgmtSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSpectrumMgmtSelection.setStatus("current")


class _NewSpectrumMgmtMode_Type(Integer32):
    """Custom type newSpectrumMgmtMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("disableOnly", 2),
          ("enableOnly", 1))
    )


_NewSpectrumMgmtMode_Type.__name__ = "Integer32"
_NewSpectrumMgmtMode_Object = MibTableColumn
newSpectrumMgmtMode = _NewSpectrumMgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1, 1, 2),
    _NewSpectrumMgmtMode_Type()
)
newSpectrumMgmtMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtMode.setStatus("current")


class _NewSpectrumMgmtLoopMeasurementMethod_Type(Integer32):
    """Custom type newSpectrumMgmtLoopMeasurementMethod based on Integer32"""
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
        *(("ewl", 3),
          ("loopLength", 2),
          ("none", 1),
          ("quadMode", 4))
    )


_NewSpectrumMgmtLoopMeasurementMethod_Type.__name__ = "Integer32"
_NewSpectrumMgmtLoopMeasurementMethod_Object = MibTableColumn
newSpectrumMgmtLoopMeasurementMethod = _NewSpectrumMgmtLoopMeasurementMethod_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1, 1, 3),
    _NewSpectrumMgmtLoopMeasurementMethod_Type()
)
newSpectrumMgmtLoopMeasurementMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtLoopMeasurementMethod.setStatus("current")


class _NewSpectrumMgmtEWLUnits_Type(Integer32):
    """Custom type newSpectrumMgmtEWLUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("feet", 2),
          ("meters", 3),
          ("none", 1))
    )


_NewSpectrumMgmtEWLUnits_Type.__name__ = "Integer32"
_NewSpectrumMgmtEWLUnits_Object = MibTableColumn
newSpectrumMgmtEWLUnits = _NewSpectrumMgmtEWLUnits_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 1, 1, 4),
    _NewSpectrumMgmtEWLUnits_Type()
)
newSpectrumMgmtEWLUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtEWLUnits.setStatus("current")
_NewSpectrumMgmtConfTable_Object = MibTable
newSpectrumMgmtConfTable = _NewSpectrumMgmtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 2)
)
if mibBuilder.loadTexts:
    newSpectrumMgmtConfTable.setStatus("current")
_NewSpectrumMgmtConfEntry_Object = MibTableRow
newSpectrumMgmtConfEntry = _NewSpectrumMgmtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 2, 1)
)
newSpectrumMgmtConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    newSpectrumMgmtConfEntry.setStatus("current")
_NewSpectrumMgmtConfEWL_Type = Unsigned32
_NewSpectrumMgmtConfEWL_Object = MibTableColumn
newSpectrumMgmtConfEWL = _NewSpectrumMgmtConfEWL_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 2, 1, 1),
    _NewSpectrumMgmtConfEWL_Type()
)
newSpectrumMgmtConfEWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSpectrumMgmtConfEWL.setStatus("current")


class _NewSpectrumMgmtConfLoopLength_Type(Integer32):
    """Custom type newSpectrumMgmtConfLoopLength based on Integer32"""
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


_NewSpectrumMgmtConfLoopLength_Type.__name__ = "Integer32"
_NewSpectrumMgmtConfLoopLength_Object = MibTableColumn
newSpectrumMgmtConfLoopLength = _NewSpectrumMgmtConfLoopLength_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 2, 1, 2),
    _NewSpectrumMgmtConfLoopLength_Type()
)
newSpectrumMgmtConfLoopLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSpectrumMgmtConfLoopLength.setStatus("current")


class _NewSpectrumMgmtConfQuadMode_Type(Integer32):
    """Custom type newSpectrumMgmtConfQuadMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sameQuad", 1),
          ("segregatedQuadAbove3km", 3),
          ("segregatedQuadUpto3km", 2))
    )


_NewSpectrumMgmtConfQuadMode_Type.__name__ = "Integer32"
_NewSpectrumMgmtConfQuadMode_Object = MibTableColumn
newSpectrumMgmtConfQuadMode = _NewSpectrumMgmtConfQuadMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 2, 1, 3),
    _NewSpectrumMgmtConfQuadMode_Type()
)
newSpectrumMgmtConfQuadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSpectrumMgmtConfQuadMode.setStatus("current")
_NewSpectrumMgmtLineInfoTable_Object = MibTable
newSpectrumMgmtLineInfoTable = _NewSpectrumMgmtLineInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3)
)
if mibBuilder.loadTexts:
    newSpectrumMgmtLineInfoTable.setStatus("current")
_NewSpectrumMgmtLineInfoEntry_Object = MibTableRow
newSpectrumMgmtLineInfoEntry = _NewSpectrumMgmtLineInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1)
)
newSpectrumMgmtLineInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    newSpectrumMgmtLineInfoEntry.setStatus("current")
_NewSpectrumMgmtXtucMax1TxRate_Type = Unsigned32
_NewSpectrumMgmtXtucMax1TxRate_Object = MibTableColumn
newSpectrumMgmtXtucMax1TxRate = _NewSpectrumMgmtXtucMax1TxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 1),
    _NewSpectrumMgmtXtucMax1TxRate_Type()
)
newSpectrumMgmtXtucMax1TxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtXtucMax1TxRate.setStatus("current")
if mibBuilder.loadTexts:
    newSpectrumMgmtXtucMax1TxRate.setUnits("bps")
_NewSpectrumMgmtXtucMin1TxRate_Type = Unsigned32
_NewSpectrumMgmtXtucMin1TxRate_Object = MibTableColumn
newSpectrumMgmtXtucMin1TxRate = _NewSpectrumMgmtXtucMin1TxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 2),
    _NewSpectrumMgmtXtucMin1TxRate_Type()
)
newSpectrumMgmtXtucMin1TxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtXtucMin1TxRate.setStatus("current")
if mibBuilder.loadTexts:
    newSpectrumMgmtXtucMin1TxRate.setUnits("bps")
_NewSpectrumMgmtXtucMax2TxRate_Type = Unsigned32
_NewSpectrumMgmtXtucMax2TxRate_Object = MibTableColumn
newSpectrumMgmtXtucMax2TxRate = _NewSpectrumMgmtXtucMax2TxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 3),
    _NewSpectrumMgmtXtucMax2TxRate_Type()
)
newSpectrumMgmtXtucMax2TxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtXtucMax2TxRate.setStatus("current")
if mibBuilder.loadTexts:
    newSpectrumMgmtXtucMax2TxRate.setUnits("bps")
_NewSpectrumMgmtXtucMin2TxRate_Type = Unsigned32
_NewSpectrumMgmtXtucMin2TxRate_Object = MibTableColumn
newSpectrumMgmtXtucMin2TxRate = _NewSpectrumMgmtXtucMin2TxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 4),
    _NewSpectrumMgmtXtucMin2TxRate_Type()
)
newSpectrumMgmtXtucMin2TxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtXtucMin2TxRate.setStatus("current")
if mibBuilder.loadTexts:
    newSpectrumMgmtXtucMin2TxRate.setUnits("bps")


class _NewSpectrumMgmtXtucMaxTxPower_Type(Integer32):
    """Custom type newSpectrumMgmtXtucMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 120),
    )


_NewSpectrumMgmtXtucMaxTxPower_Type.__name__ = "Integer32"
_NewSpectrumMgmtXtucMaxTxPower_Object = MibTableColumn
newSpectrumMgmtXtucMaxTxPower = _NewSpectrumMgmtXtucMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 5),
    _NewSpectrumMgmtXtucMaxTxPower_Type()
)
newSpectrumMgmtXtucMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtXtucMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    newSpectrumMgmtXtucMaxTxPower.setUnits("tenth dB")
_NewSpectrumMgmtXturMax1TxRate_Type = Unsigned32
_NewSpectrumMgmtXturMax1TxRate_Object = MibTableColumn
newSpectrumMgmtXturMax1TxRate = _NewSpectrumMgmtXturMax1TxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 6),
    _NewSpectrumMgmtXturMax1TxRate_Type()
)
newSpectrumMgmtXturMax1TxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtXturMax1TxRate.setStatus("current")
if mibBuilder.loadTexts:
    newSpectrumMgmtXturMax1TxRate.setUnits("bps")
_NewSpectrumMgmtXturMin1TxRate_Type = Unsigned32
_NewSpectrumMgmtXturMin1TxRate_Object = MibTableColumn
newSpectrumMgmtXturMin1TxRate = _NewSpectrumMgmtXturMin1TxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 7),
    _NewSpectrumMgmtXturMin1TxRate_Type()
)
newSpectrumMgmtXturMin1TxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtXturMin1TxRate.setStatus("current")
if mibBuilder.loadTexts:
    newSpectrumMgmtXturMin1TxRate.setUnits("bps")
_NewSpectrumMgmtXturMax2TxRate_Type = Unsigned32
_NewSpectrumMgmtXturMax2TxRate_Object = MibTableColumn
newSpectrumMgmtXturMax2TxRate = _NewSpectrumMgmtXturMax2TxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 8),
    _NewSpectrumMgmtXturMax2TxRate_Type()
)
newSpectrumMgmtXturMax2TxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtXturMax2TxRate.setStatus("current")
if mibBuilder.loadTexts:
    newSpectrumMgmtXturMax2TxRate.setUnits("bps")
_NewSpectrumMgmtXturMin2TxRate_Type = Unsigned32
_NewSpectrumMgmtXturMin2TxRate_Object = MibTableColumn
newSpectrumMgmtXturMin2TxRate = _NewSpectrumMgmtXturMin2TxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 9),
    _NewSpectrumMgmtXturMin2TxRate_Type()
)
newSpectrumMgmtXturMin2TxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtXturMin2TxRate.setStatus("current")
if mibBuilder.loadTexts:
    newSpectrumMgmtXturMin2TxRate.setUnits("bps")


class _NewSpectrumMgmtXturMaxTxPower_Type(Integer32):
    """Custom type newSpectrumMgmtXturMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 120),
    )


_NewSpectrumMgmtXturMaxTxPower_Type.__name__ = "Integer32"
_NewSpectrumMgmtXturMaxTxPower_Object = MibTableColumn
newSpectrumMgmtXturMaxTxPower = _NewSpectrumMgmtXturMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 10),
    _NewSpectrumMgmtXturMaxTxPower_Type()
)
newSpectrumMgmtXturMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtXturMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    newSpectrumMgmtXturMaxTxPower.setUnits("tenth dB")
_NewSpectrumMgmtMinEWL_Type = Unsigned32
_NewSpectrumMgmtMinEWL_Object = MibTableColumn
newSpectrumMgmtMinEWL = _NewSpectrumMgmtMinEWL_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 11),
    _NewSpectrumMgmtMinEWL_Type()
)
newSpectrumMgmtMinEWL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtMinEWL.setStatus("current")
_NewSpectrumMgmtMaxEWL_Type = Unsigned32
_NewSpectrumMgmtMaxEWL_Object = MibTableColumn
newSpectrumMgmtMaxEWL = _NewSpectrumMgmtMaxEWL_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 2, 3, 1, 12),
    _NewSpectrumMgmtMaxEWL_Type()
)
newSpectrumMgmtMaxEWL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newSpectrumMgmtMaxEWL.setStatus("current")
_PdnSpecMgmtConformance_ObjectIdentity = ObjectIdentity
pdnSpecMgmtConformance = _PdnSpecMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3)
)
_PdnSpecMgmtGroups_ObjectIdentity = ObjectIdentity
pdnSpecMgmtGroups = _PdnSpecMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1)
)
_PdnSpecMgmtCompliances_ObjectIdentity = ObjectIdentity
pdnSpecMgmtCompliances = _PdnSpecMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 2)
)

# Managed Objects groups

pdnGeneralConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 1)
)
pdnGeneralConfigGroup.setObjects(
      *(("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtSelection"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtMode"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtLoopMeasurementMethod"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtEWLUnits"))
)
if mibBuilder.loadTexts:
    pdnGeneralConfigGroup.setStatus("current")

pdnLineInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 2)
)
pdnLineInfoGroup.setObjects(
      *(("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXtucMax1TxRate"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXtucMin1TxRate"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXtucMax2TxRate"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXtucMin2TxRate"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXtucMaxTxPower"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXturMax1TxRate"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXturMin1TxRate"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXturMax2TxRate"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXturMin2TxRate"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtXturMaxTxPower"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtMinEWL"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtMaxEWL"))
)
if mibBuilder.loadTexts:
    pdnLineInfoGroup.setStatus("current")

pdnEWLModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 3)
)
pdnEWLModeGroup.setObjects(
      *(("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtConfEWL"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtMinEWL"),
        ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtMaxEWL"))
)
if mibBuilder.loadTexts:
    pdnEWLModeGroup.setStatus("current")

pdnLoopLengthModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 4)
)
pdnLoopLengthModeGroup.setObjects(
    ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtConfLoopLength")
)
if mibBuilder.loadTexts:
    pdnLoopLengthModeGroup.setStatus("current")

pdnQuadModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 5)
)
pdnQuadModeGroup.setObjects(
    ("PDN-SPECTRUMMGMT-MIB", "newSpectrumMgmtConfQuadMode")
)
if mibBuilder.loadTexts:
    pdnQuadModeGroup.setStatus("current")

pdnSpectrumMgmtDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 1, 7)
)
pdnSpectrumMgmtDeprecatedGroup.setObjects(
      *(("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtCountryCode"),
        ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtEWL"),
        ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtLineLength"),
        ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtAllowedSpeedsMin1"),
        ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtAllowedSpeedsMax1"),
        ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtAllowedSpeedsMin2"),
        ("PDN-SPECTRUMMGMT-MIB", "spectrumMgmtAllowedSpeedsMax2"))
)
if mibBuilder.loadTexts:
    pdnSpectrumMgmtDeprecatedGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnSpecMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 19, 3, 2, 1)
)
if mibBuilder.loadTexts:
    pdnSpecMgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-SPECTRUMMGMT-MIB",
    **{"pdnSpectrumMgmt": pdnSpectrumMgmt,
       "pdnSpecMgmtObjects": pdnSpecMgmtObjects,
       "spectrumMgmtCountryCode": spectrumMgmtCountryCode,
       "spectrumMgmtTable": spectrumMgmtTable,
       "spectrumMgmtEntry": spectrumMgmtEntry,
       "spectrumMgmtEWL": spectrumMgmtEWL,
       "spectrumMgmtAllowedSpeedsMin1": spectrumMgmtAllowedSpeedsMin1,
       "spectrumMgmtAllowedSpeedsMax1": spectrumMgmtAllowedSpeedsMax1,
       "spectrumMgmtAllowedSpeedsMin2": spectrumMgmtAllowedSpeedsMin2,
       "spectrumMgmtAllowedSpeedsMax2": spectrumMgmtAllowedSpeedsMax2,
       "spectrumMgmtLineLength": spectrumMgmtLineLength,
       "pdnNewSpecMgmtObjects": pdnNewSpecMgmtObjects,
       "newSpectrumMgmtGeneralConfigTable": newSpectrumMgmtGeneralConfigTable,
       "newSpectrumMgmtGeneralConfigEntry": newSpectrumMgmtGeneralConfigEntry,
       "newSpectrumMgmtSelection": newSpectrumMgmtSelection,
       "newSpectrumMgmtMode": newSpectrumMgmtMode,
       "newSpectrumMgmtLoopMeasurementMethod": newSpectrumMgmtLoopMeasurementMethod,
       "newSpectrumMgmtEWLUnits": newSpectrumMgmtEWLUnits,
       "newSpectrumMgmtConfTable": newSpectrumMgmtConfTable,
       "newSpectrumMgmtConfEntry": newSpectrumMgmtConfEntry,
       "newSpectrumMgmtConfEWL": newSpectrumMgmtConfEWL,
       "newSpectrumMgmtConfLoopLength": newSpectrumMgmtConfLoopLength,
       "newSpectrumMgmtConfQuadMode": newSpectrumMgmtConfQuadMode,
       "newSpectrumMgmtLineInfoTable": newSpectrumMgmtLineInfoTable,
       "newSpectrumMgmtLineInfoEntry": newSpectrumMgmtLineInfoEntry,
       "newSpectrumMgmtXtucMax1TxRate": newSpectrumMgmtXtucMax1TxRate,
       "newSpectrumMgmtXtucMin1TxRate": newSpectrumMgmtXtucMin1TxRate,
       "newSpectrumMgmtXtucMax2TxRate": newSpectrumMgmtXtucMax2TxRate,
       "newSpectrumMgmtXtucMin2TxRate": newSpectrumMgmtXtucMin2TxRate,
       "newSpectrumMgmtXtucMaxTxPower": newSpectrumMgmtXtucMaxTxPower,
       "newSpectrumMgmtXturMax1TxRate": newSpectrumMgmtXturMax1TxRate,
       "newSpectrumMgmtXturMin1TxRate": newSpectrumMgmtXturMin1TxRate,
       "newSpectrumMgmtXturMax2TxRate": newSpectrumMgmtXturMax2TxRate,
       "newSpectrumMgmtXturMin2TxRate": newSpectrumMgmtXturMin2TxRate,
       "newSpectrumMgmtXturMaxTxPower": newSpectrumMgmtXturMaxTxPower,
       "newSpectrumMgmtMinEWL": newSpectrumMgmtMinEWL,
       "newSpectrumMgmtMaxEWL": newSpectrumMgmtMaxEWL,
       "pdnSpecMgmtConformance": pdnSpecMgmtConformance,
       "pdnSpecMgmtGroups": pdnSpecMgmtGroups,
       "pdnGeneralConfigGroup": pdnGeneralConfigGroup,
       "pdnLineInfoGroup": pdnLineInfoGroup,
       "pdnEWLModeGroup": pdnEWLModeGroup,
       "pdnLoopLengthModeGroup": pdnLoopLengthModeGroup,
       "pdnQuadModeGroup": pdnQuadModeGroup,
       "pdnSpectrumMgmtDeprecatedGroup": pdnSpectrumMgmtDeprecatedGroup,
       "pdnSpecMgmtCompliances": pdnSpecMgmtCompliances,
       "pdnSpecMgmtCompliance": pdnSpecMgmtCompliance}
)
