# SNMP MIB module (PDN-REACHDSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-REACHDSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:04 2024
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

pdnReachDSL = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20)
)
pdnReachDSL.setRevisions(
        ("2003-01-15 12:00",
         "2003-01-12 12:00",
         "2002-10-15 17:00",
         "2002-07-12 03:15")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnReachDSLObjects_ObjectIdentity = ObjectIdentity
pdnReachDSLObjects = _PdnReachDSLObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1)
)


class _ReachDSLSpectrumMgmtSelection_Type(Integer32):
    """Custom type reachDSLSpectrumMgmtSelection based on Integer32"""
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


_ReachDSLSpectrumMgmtSelection_Type.__name__ = "Integer32"
_ReachDSLSpectrumMgmtSelection_Object = MibScalar
reachDSLSpectrumMgmtSelection = _ReachDSLSpectrumMgmtSelection_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 1),
    _ReachDSLSpectrumMgmtSelection_Type()
)
reachDSLSpectrumMgmtSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtSelection.setStatus("current")


class _ReachDSLSpectrumMgmtZone_Type(Integer32):
    """Custom type reachDSLSpectrumMgmtZone based on Integer32"""
    defaultValue = 1

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
        *(("canada1", 3),
          ("emea1", 5),
          ("japan1", 4),
          ("uk1", 2),
          ("usa1", 1))
    )


_ReachDSLSpectrumMgmtZone_Type.__name__ = "Integer32"
_ReachDSLSpectrumMgmtZone_Object = MibScalar
reachDSLSpectrumMgmtZone = _ReachDSLSpectrumMgmtZone_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 2),
    _ReachDSLSpectrumMgmtZone_Type()
)
reachDSLSpectrumMgmtZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtZone.setStatus("deprecated")
_ReachDSLSpectrumMgmtConfTable_Object = MibTable
reachDSLSpectrumMgmtConfTable = _ReachDSLSpectrumMgmtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3)
)
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtConfTable.setStatus("current")
_ReachDSLSpectrumMgmtConfEntry_Object = MibTableRow
reachDSLSpectrumMgmtConfEntry = _ReachDSLSpectrumMgmtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1)
)
reachDSLSpectrumMgmtConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtConfEntry.setStatus("current")
_ReachDSLSpectrumMgmtConfEWL_Type = Unsigned32
_ReachDSLSpectrumMgmtConfEWL_Object = MibTableColumn
reachDSLSpectrumMgmtConfEWL = _ReachDSLSpectrumMgmtConfEWL_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1, 1),
    _ReachDSLSpectrumMgmtConfEWL_Type()
)
reachDSLSpectrumMgmtConfEWL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtConfEWL.setStatus("current")


class _ReachDSLSpectrumMgmtConfLoopLength_Type(Integer32):
    """Custom type reachDSLSpectrumMgmtConfLoopLength based on Integer32"""
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


_ReachDSLSpectrumMgmtConfLoopLength_Type.__name__ = "Integer32"
_ReachDSLSpectrumMgmtConfLoopLength_Object = MibTableColumn
reachDSLSpectrumMgmtConfLoopLength = _ReachDSLSpectrumMgmtConfLoopLength_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1, 2),
    _ReachDSLSpectrumMgmtConfLoopLength_Type()
)
reachDSLSpectrumMgmtConfLoopLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtConfLoopLength.setStatus("current")


class _ReachDSLSpectrumMgmtConfAtucMaxTxPower_Type(Integer32):
    """Custom type reachDSLSpectrumMgmtConfAtucMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 120),
    )


_ReachDSLSpectrumMgmtConfAtucMaxTxPower_Type.__name__ = "Integer32"
_ReachDSLSpectrumMgmtConfAtucMaxTxPower_Object = MibTableColumn
reachDSLSpectrumMgmtConfAtucMaxTxPower = _ReachDSLSpectrumMgmtConfAtucMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1, 3),
    _ReachDSLSpectrumMgmtConfAtucMaxTxPower_Type()
)
reachDSLSpectrumMgmtConfAtucMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtConfAtucMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtConfAtucMaxTxPower.setUnits("tenth dB")


class _ReachDSLSpectrumMgmtConfAturMaxTxPower_Type(Integer32):
    """Custom type reachDSLSpectrumMgmtConfAturMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 120),
    )


_ReachDSLSpectrumMgmtConfAturMaxTxPower_Type.__name__ = "Integer32"
_ReachDSLSpectrumMgmtConfAturMaxTxPower_Object = MibTableColumn
reachDSLSpectrumMgmtConfAturMaxTxPower = _ReachDSLSpectrumMgmtConfAturMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1, 4),
    _ReachDSLSpectrumMgmtConfAturMaxTxPower_Type()
)
reachDSLSpectrumMgmtConfAturMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtConfAturMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtConfAturMaxTxPower.setUnits("tenth dB")


class _ReachDSLSpectrumMgmtConfQuadMode_Type(Integer32):
    """Custom type reachDSLSpectrumMgmtConfQuadMode based on Integer32"""
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


_ReachDSLSpectrumMgmtConfQuadMode_Type.__name__ = "Integer32"
_ReachDSLSpectrumMgmtConfQuadMode_Object = MibTableColumn
reachDSLSpectrumMgmtConfQuadMode = _ReachDSLSpectrumMgmtConfQuadMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 3, 1, 5),
    _ReachDSLSpectrumMgmtConfQuadMode_Type()
)
reachDSLSpectrumMgmtConfQuadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtConfQuadMode.setStatus("current")
_ReachDSLSpectrumMgmtLineInfoTable_Object = MibTable
reachDSLSpectrumMgmtLineInfoTable = _ReachDSLSpectrumMgmtLineInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4)
)
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtLineInfoTable.setStatus("current")
_ReachDSLSpectrumMgmtLineInfoEntry_Object = MibTableRow
reachDSLSpectrumMgmtLineInfoEntry = _ReachDSLSpectrumMgmtLineInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1)
)
reachDSLSpectrumMgmtLineInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtLineInfoEntry.setStatus("current")
_ReachDSLSpectrumMgmtAtucMaxTxRate_Type = Unsigned32
_ReachDSLSpectrumMgmtAtucMaxTxRate_Object = MibTableColumn
reachDSLSpectrumMgmtAtucMaxTxRate = _ReachDSLSpectrumMgmtAtucMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 1),
    _ReachDSLSpectrumMgmtAtucMaxTxRate_Type()
)
reachDSLSpectrumMgmtAtucMaxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAtucMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAtucMaxTxRate.setUnits("bps")
_ReachDSLSpectrumMgmtAtucMinTxRate_Type = Unsigned32
_ReachDSLSpectrumMgmtAtucMinTxRate_Object = MibTableColumn
reachDSLSpectrumMgmtAtucMinTxRate = _ReachDSLSpectrumMgmtAtucMinTxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 2),
    _ReachDSLSpectrumMgmtAtucMinTxRate_Type()
)
reachDSLSpectrumMgmtAtucMinTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAtucMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAtucMinTxRate.setUnits("bps")


class _ReachDSLSpectrumMgmtAtucMaxTxPower_Type(Integer32):
    """Custom type reachDSLSpectrumMgmtAtucMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 120),
    )


_ReachDSLSpectrumMgmtAtucMaxTxPower_Type.__name__ = "Integer32"
_ReachDSLSpectrumMgmtAtucMaxTxPower_Object = MibTableColumn
reachDSLSpectrumMgmtAtucMaxTxPower = _ReachDSLSpectrumMgmtAtucMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 3),
    _ReachDSLSpectrumMgmtAtucMaxTxPower_Type()
)
reachDSLSpectrumMgmtAtucMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAtucMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAtucMaxTxPower.setUnits("tenth dB")
_ReachDSLSpectrumMgmtAturMaxTxRate_Type = Unsigned32
_ReachDSLSpectrumMgmtAturMaxTxRate_Object = MibTableColumn
reachDSLSpectrumMgmtAturMaxTxRate = _ReachDSLSpectrumMgmtAturMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 4),
    _ReachDSLSpectrumMgmtAturMaxTxRate_Type()
)
reachDSLSpectrumMgmtAturMaxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAturMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAturMaxTxRate.setUnits("bps")
_ReachDSLSpectrumMgmtAturMinTxRate_Type = Unsigned32
_ReachDSLSpectrumMgmtAturMinTxRate_Object = MibTableColumn
reachDSLSpectrumMgmtAturMinTxRate = _ReachDSLSpectrumMgmtAturMinTxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 5),
    _ReachDSLSpectrumMgmtAturMinTxRate_Type()
)
reachDSLSpectrumMgmtAturMinTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAturMinTxRate.setStatus("current")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAturMinTxRate.setUnits("bps")


class _ReachDSLSpectrumMgmtAturMaxTxPower_Type(Integer32):
    """Custom type reachDSLSpectrumMgmtAturMaxTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 120),
    )


_ReachDSLSpectrumMgmtAturMaxTxPower_Type.__name__ = "Integer32"
_ReachDSLSpectrumMgmtAturMaxTxPower_Object = MibTableColumn
reachDSLSpectrumMgmtAturMaxTxPower = _ReachDSLSpectrumMgmtAturMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 6),
    _ReachDSLSpectrumMgmtAturMaxTxPower_Type()
)
reachDSLSpectrumMgmtAturMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAturMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtAturMaxTxPower.setUnits("tenth dB")
_ReachDSLSpectrumMgmtMinEWL_Type = Unsigned32
_ReachDSLSpectrumMgmtMinEWL_Object = MibTableColumn
reachDSLSpectrumMgmtMinEWL = _ReachDSLSpectrumMgmtMinEWL_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 7),
    _ReachDSLSpectrumMgmtMinEWL_Type()
)
reachDSLSpectrumMgmtMinEWL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtMinEWL.setStatus("current")
_ReachDSLSpectrumMgmtMaxEWL_Type = Unsigned32
_ReachDSLSpectrumMgmtMaxEWL_Object = MibTableColumn
reachDSLSpectrumMgmtMaxEWL = _ReachDSLSpectrumMgmtMaxEWL_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 4, 1, 8),
    _ReachDSLSpectrumMgmtMaxEWL_Type()
)
reachDSLSpectrumMgmtMaxEWL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtMaxEWL.setStatus("current")
_ReachDSLLineTable_Object = MibTable
reachDSLLineTable = _ReachDSLLineTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 5)
)
if mibBuilder.loadTexts:
    reachDSLLineTable.setStatus("current")
_ReachDSLLineEntry_Object = MibTableRow
reachDSLLineEntry = _ReachDSLLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 5, 1)
)
reachDSLLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    reachDSLLineEntry.setStatus("current")


class _ReachDSLPotsDetectionVoltage_Type(Integer32):
    """Custom type reachDSLPotsDetectionVoltage based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 74),
    )


_ReachDSLPotsDetectionVoltage_Type.__name__ = "Integer32"
_ReachDSLPotsDetectionVoltage_Object = MibTableColumn
reachDSLPotsDetectionVoltage = _ReachDSLPotsDetectionVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 5, 1, 1),
    _ReachDSLPotsDetectionVoltage_Type()
)
reachDSLPotsDetectionVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reachDSLPotsDetectionVoltage.setStatus("current")
if mibBuilder.loadTexts:
    reachDSLPotsDetectionVoltage.setUnits("volts")


class _ReachDSLCircuitIdentifier_Type(DisplayString):
    """Custom type reachDSLCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ReachDSLCircuitIdentifier_Type.__name__ = "DisplayString"
_ReachDSLCircuitIdentifier_Object = MibTableColumn
reachDSLCircuitIdentifier = _ReachDSLCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 5, 1, 2),
    _ReachDSLCircuitIdentifier_Type()
)
reachDSLCircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reachDSLCircuitIdentifier.setStatus("deprecated")


class _ReachDSLSpectrumMgmtLoopMeasurementMethod_Type(Integer32):
    """Custom type reachDSLSpectrumMgmtLoopMeasurementMethod based on Integer32"""
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


_ReachDSLSpectrumMgmtLoopMeasurementMethod_Type.__name__ = "Integer32"
_ReachDSLSpectrumMgmtLoopMeasurementMethod_Object = MibScalar
reachDSLSpectrumMgmtLoopMeasurementMethod = _ReachDSLSpectrumMgmtLoopMeasurementMethod_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 6),
    _ReachDSLSpectrumMgmtLoopMeasurementMethod_Type()
)
reachDSLSpectrumMgmtLoopMeasurementMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtLoopMeasurementMethod.setStatus("current")


class _ReachDSLSpectrumMgmtEWLUnits_Type(Integer32):
    """Custom type reachDSLSpectrumMgmtEWLUnits based on Integer32"""
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


_ReachDSLSpectrumMgmtEWLUnits_Type.__name__ = "Integer32"
_ReachDSLSpectrumMgmtEWLUnits_Object = MibScalar
reachDSLSpectrumMgmtEWLUnits = _ReachDSLSpectrumMgmtEWLUnits_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 7),
    _ReachDSLSpectrumMgmtEWLUnits_Type()
)
reachDSLSpectrumMgmtEWLUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtEWLUnits.setStatus("current")


class _ReachDSLSpectrumMgmtMode_Type(Integer32):
    """Custom type reachDSLSpectrumMgmtMode based on Integer32"""
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


_ReachDSLSpectrumMgmtMode_Type.__name__ = "Integer32"
_ReachDSLSpectrumMgmtMode_Object = MibScalar
reachDSLSpectrumMgmtMode = _ReachDSLSpectrumMgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 1, 8),
    _ReachDSLSpectrumMgmtMode_Type()
)
reachDSLSpectrumMgmtMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reachDSLSpectrumMgmtMode.setStatus("current")
_PdnReachDSLConformance_ObjectIdentity = ObjectIdentity
pdnReachDSLConformance = _PdnReachDSLConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2)
)
_PdnReachDSLGroups_ObjectIdentity = ObjectIdentity
pdnReachDSLGroups = _PdnReachDSLGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1)
)
_PdnReachDSLCompliances_ObjectIdentity = ObjectIdentity
pdnReachDSLCompliances = _PdnReachDSLCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 2)
)

# Managed Objects groups

pdnReachDSLConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 1)
)
pdnReachDSLConfigurationGroup.setObjects(
      *(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtSelection"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfEWL"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfLoopLength"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfAtucMaxTxPower"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfAturMaxTxPower"),
        ("PDN-REACHDSL-MIB", "reachDSLPotsDetectionVoltage"),
        ("PDN-REACHDSL-MIB", "reachDSLCircuitIdentifier"))
)
if mibBuilder.loadTexts:
    pdnReachDSLConfigurationGroup.setStatus("deprecated")

pdnReachDSLInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 2)
)
pdnReachDSLInformationGroup.setObjects(
      *(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMaxTxRate"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMinTxRate"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMaxTxPower"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMaxTxRate"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMinTxRate"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMaxTxPower"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMinEWL"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMaxEWL"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtLoopMeasurementMethod"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtEWLUnits"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMode"))
)
if mibBuilder.loadTexts:
    pdnReachDSLInformationGroup.setStatus("deprecated")

pdnReachDSLDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 3)
)
pdnReachDSLDeprecatedGroup.setObjects(
      *(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtZone"),
        ("PDN-REACHDSL-MIB", "reachDSLCircuitIdentifier"))
)
if mibBuilder.loadTexts:
    pdnReachDSLDeprecatedGroup.setStatus("deprecated")

pdnReachDSLGeneralConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 4)
)
pdnReachDSLGeneralConfigGroup.setObjects(
      *(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtSelection"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfAtucMaxTxPower"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfAturMaxTxPower"),
        ("PDN-REACHDSL-MIB", "reachDSLPotsDetectionVoltage"))
)
if mibBuilder.loadTexts:
    pdnReachDSLGeneralConfigGroup.setStatus("current")

pdnReachDSLGeneralInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 5)
)
pdnReachDSLGeneralInformationGroup.setObjects(
      *(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMaxTxRate"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMinTxRate"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAtucMaxTxPower"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMaxTxRate"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMinTxRate"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtAturMaxTxPower"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtLoopMeasurementMethod"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtEWLUnits"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMode"))
)
if mibBuilder.loadTexts:
    pdnReachDSLGeneralInformationGroup.setStatus("current")

pdnReachDSLEWLModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 6)
)
pdnReachDSLEWLModeGroup.setObjects(
      *(("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfEWL"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMinEWL"),
        ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtMaxEWL"))
)
if mibBuilder.loadTexts:
    pdnReachDSLEWLModeGroup.setStatus("current")

pdnReachDSLLoopLengthModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 7)
)
pdnReachDSLLoopLengthModeGroup.setObjects(
    ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfLoopLength")
)
if mibBuilder.loadTexts:
    pdnReachDSLLoopLengthModeGroup.setStatus("current")

pdnReachDSLQuadModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 1, 8)
)
pdnReachDSLQuadModeGroup.setObjects(
    ("PDN-REACHDSL-MIB", "reachDSLSpectrumMgmtConfQuadMode")
)
if mibBuilder.loadTexts:
    pdnReachDSLQuadModeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnReachDSLCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pdnReachDSLCompliance.setStatus(
        "deprecated"
    )

pdnReachDSLCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 20, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pdnReachDSLCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-REACHDSL-MIB",
    **{"pdnReachDSL": pdnReachDSL,
       "pdnReachDSLObjects": pdnReachDSLObjects,
       "reachDSLSpectrumMgmtSelection": reachDSLSpectrumMgmtSelection,
       "reachDSLSpectrumMgmtZone": reachDSLSpectrumMgmtZone,
       "reachDSLSpectrumMgmtConfTable": reachDSLSpectrumMgmtConfTable,
       "reachDSLSpectrumMgmtConfEntry": reachDSLSpectrumMgmtConfEntry,
       "reachDSLSpectrumMgmtConfEWL": reachDSLSpectrumMgmtConfEWL,
       "reachDSLSpectrumMgmtConfLoopLength": reachDSLSpectrumMgmtConfLoopLength,
       "reachDSLSpectrumMgmtConfAtucMaxTxPower": reachDSLSpectrumMgmtConfAtucMaxTxPower,
       "reachDSLSpectrumMgmtConfAturMaxTxPower": reachDSLSpectrumMgmtConfAturMaxTxPower,
       "reachDSLSpectrumMgmtConfQuadMode": reachDSLSpectrumMgmtConfQuadMode,
       "reachDSLSpectrumMgmtLineInfoTable": reachDSLSpectrumMgmtLineInfoTable,
       "reachDSLSpectrumMgmtLineInfoEntry": reachDSLSpectrumMgmtLineInfoEntry,
       "reachDSLSpectrumMgmtAtucMaxTxRate": reachDSLSpectrumMgmtAtucMaxTxRate,
       "reachDSLSpectrumMgmtAtucMinTxRate": reachDSLSpectrumMgmtAtucMinTxRate,
       "reachDSLSpectrumMgmtAtucMaxTxPower": reachDSLSpectrumMgmtAtucMaxTxPower,
       "reachDSLSpectrumMgmtAturMaxTxRate": reachDSLSpectrumMgmtAturMaxTxRate,
       "reachDSLSpectrumMgmtAturMinTxRate": reachDSLSpectrumMgmtAturMinTxRate,
       "reachDSLSpectrumMgmtAturMaxTxPower": reachDSLSpectrumMgmtAturMaxTxPower,
       "reachDSLSpectrumMgmtMinEWL": reachDSLSpectrumMgmtMinEWL,
       "reachDSLSpectrumMgmtMaxEWL": reachDSLSpectrumMgmtMaxEWL,
       "reachDSLLineTable": reachDSLLineTable,
       "reachDSLLineEntry": reachDSLLineEntry,
       "reachDSLPotsDetectionVoltage": reachDSLPotsDetectionVoltage,
       "reachDSLCircuitIdentifier": reachDSLCircuitIdentifier,
       "reachDSLSpectrumMgmtLoopMeasurementMethod": reachDSLSpectrumMgmtLoopMeasurementMethod,
       "reachDSLSpectrumMgmtEWLUnits": reachDSLSpectrumMgmtEWLUnits,
       "reachDSLSpectrumMgmtMode": reachDSLSpectrumMgmtMode,
       "pdnReachDSLConformance": pdnReachDSLConformance,
       "pdnReachDSLGroups": pdnReachDSLGroups,
       "pdnReachDSLConfigurationGroup": pdnReachDSLConfigurationGroup,
       "pdnReachDSLInformationGroup": pdnReachDSLInformationGroup,
       "pdnReachDSLDeprecatedGroup": pdnReachDSLDeprecatedGroup,
       "pdnReachDSLGeneralConfigGroup": pdnReachDSLGeneralConfigGroup,
       "pdnReachDSLGeneralInformationGroup": pdnReachDSLGeneralInformationGroup,
       "pdnReachDSLEWLModeGroup": pdnReachDSLEWLModeGroup,
       "pdnReachDSLLoopLengthModeGroup": pdnReachDSLLoopLengthModeGroup,
       "pdnReachDSLQuadModeGroup": pdnReachDSLQuadModeGroup,
       "pdnReachDSLCompliances": pdnReachDSLCompliances,
       "pdnReachDSLCompliance": pdnReachDSLCompliance,
       "pdnReachDSLCompliance1": pdnReachDSLCompliance1}
)
