# SNMP MIB module (EATON-PDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EATON-PDU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:23 2024
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

(pduAgent,) = mibBuilder.importSymbols(
    "EATON-OIDS",
    "pduAgent")

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

eatonPduMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4)
)
eatonPduMIB.setRevisions(
        ("2007-01-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PositiveInteger(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NonNegativeInteger(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_EatonPduMIBObjects_ObjectIdentity = ObjectIdentity
eatonPduMIBObjects = _EatonPduMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1)
)
_MainPdu_ObjectIdentity = ObjectIdentity
mainPdu = _MainPdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1)
)
_PduNameplate_ObjectIdentity = ObjectIdentity
pduNameplate = _PduNameplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1)
)
_PduRatingVA_Type = PositiveInteger
_PduRatingVA_Object = MibScalar
pduRatingVA = _PduRatingVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 1),
    _PduRatingVA_Type()
)
pduRatingVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRatingVA.setStatus("current")
if mibBuilder.loadTexts:
    pduRatingVA.setUnits("volt-amps")
_PduNominalOutputVoltage_Type = PositiveInteger
_PduNominalOutputVoltage_Object = MibScalar
pduNominalOutputVoltage = _PduNominalOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 2),
    _PduNominalOutputVoltage_Type()
)
pduNominalOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNominalOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pduNominalOutputVoltage.setUnits("Volts RMS")
_PduNumPhases_Type = PositiveInteger
_PduNumPhases_Object = MibScalar
pduNumPhases = _PduNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 3),
    _PduNumPhases_Type()
)
pduNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNumPhases.setStatus("current")
_PduNumPanels_Type = PositiveInteger
_PduNumPanels_Object = MibScalar
pduNumPanels = _PduNumPanels_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 1, 4),
    _PduNumPanels_Type()
)
pduNumPanels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNumPanels.setStatus("current")
_PduInput_ObjectIdentity = ObjectIdentity
pduInput = _PduInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2)
)
_PduFrequency_Type = NonNegativeInteger
_PduFrequency_Object = MibScalar
pduFrequency = _PduFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 1),
    _PduFrequency_Type()
)
pduFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pduFrequency.setUnits("0.1 Hertz")
_PduInputVA_Type = NonNegativeInteger
_PduInputVA_Object = MibScalar
pduInputVA = _PduInputVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 2),
    _PduInputVA_Type()
)
pduInputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputVA.setStatus("current")
if mibBuilder.loadTexts:
    pduInputVA.setUnits("VA")
_PduInputPower_Type = NonNegativeInteger
_PduInputPower_Object = MibScalar
pduInputPower = _PduInputPower_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 3),
    _PduInputPower_Type()
)
pduInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPower.setStatus("current")
if mibBuilder.loadTexts:
    pduInputPower.setUnits("Watts")


class _PduInputPowerFactor_Type(Integer32):
    """Custom type pduInputPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_PduInputPowerFactor_Type.__name__ = "Integer32"
_PduInputPowerFactor_Object = MibScalar
pduInputPowerFactor = _PduInputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 4),
    _PduInputPowerFactor_Type()
)
pduInputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pduInputPowerFactor.setUnits("pf * 100")
_PduGroundCurrent_Type = NonNegativeInteger
_PduGroundCurrent_Object = MibScalar
pduGroundCurrent = _PduGroundCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 5),
    _PduGroundCurrent_Type()
)
pduGroundCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGroundCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduGroundCurrent.setUnits("0.1 Amps RMS")


class _PduInputVoltageUnits_Type(DisplayString):
    """Custom type pduInputVoltageUnits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduInputVoltageUnits_Type.__name__ = "DisplayString"
_PduInputVoltageUnits_Object = MibScalar
pduInputVoltageUnits = _PduInputVoltageUnits_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 6),
    _PduInputVoltageUnits_Type()
)
pduInputVoltageUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputVoltageUnits.setStatus("current")
_PduInputNumPhases_Type = PositiveInteger
_PduInputNumPhases_Object = MibScalar
pduInputNumPhases = _PduInputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 7),
    _PduInputNumPhases_Type()
)
pduInputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputNumPhases.setStatus("current")
_PduInputTable_Object = MibTable
pduInputTable = _PduInputTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    pduInputTable.setStatus("current")
_PduInputEntry_Object = MibTableRow
pduInputEntry = _PduInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1)
)
pduInputEntry.setIndexNames(
    (0, "EATON-PDU-MIB", "pduInputPhaseIndex"),
)
if mibBuilder.loadTexts:
    pduInputEntry.setStatus("current")
_PduInputPhaseIndex_Type = PositiveInteger
_PduInputPhaseIndex_Object = MibTableColumn
pduInputPhaseIndex = _PduInputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 1),
    _PduInputPhaseIndex_Type()
)
pduInputPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduInputPhaseIndex.setStatus("current")
_PduInputPhaseVoltage_Type = NonNegativeInteger
_PduInputPhaseVoltage_Object = MibTableColumn
pduInputPhaseVoltage = _PduInputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 2),
    _PduInputPhaseVoltage_Type()
)
pduInputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pduInputPhaseVoltage.setUnits("Volts RMS")
_PduInputPhaseCurrent_Type = NonNegativeInteger
_PduInputPhaseCurrent_Object = MibTableColumn
pduInputPhaseCurrent = _PduInputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 3),
    _PduInputPhaseCurrent_Type()
)
pduInputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduInputPhaseCurrent.setUnits("0.1 Amps RMS")


class _PduInputPhasePercentLoad_Type(Integer32):
    """Custom type pduInputPhasePercentLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PduInputPhasePercentLoad_Type.__name__ = "Integer32"
_PduInputPhasePercentLoad_Object = MibTableColumn
pduInputPhasePercentLoad = _PduInputPhasePercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 2, 8, 1, 4),
    _PduInputPhasePercentLoad_Type()
)
pduInputPhasePercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhasePercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    pduInputPhasePercentLoad.setUnits("percent")
_PduOutput_ObjectIdentity = ObjectIdentity
pduOutput = _PduOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3)
)
_PduOutputKilowattHours_Type = NonNegativeInteger
_PduOutputKilowattHours_Object = MibScalar
pduOutputKilowattHours = _PduOutputKilowattHours_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 1),
    _PduOutputKilowattHours_Type()
)
pduOutputKilowattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputKilowattHours.setStatus("current")
if mibBuilder.loadTexts:
    pduOutputKilowattHours.setUnits("KWH")
_PduOutputVA_Type = NonNegativeInteger
_PduOutputVA_Object = MibScalar
pduOutputVA = _PduOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 2),
    _PduOutputVA_Type()
)
pduOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputVA.setStatus("current")
if mibBuilder.loadTexts:
    pduOutputVA.setUnits("VA")
_PduOutputPower_Type = NonNegativeInteger
_PduOutputPower_Object = MibScalar
pduOutputPower = _PduOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 3),
    _PduOutputPower_Type()
)
pduOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    pduOutputPower.setUnits("Watts")


class _PduOutputPowerFactor_Type(Integer32):
    """Custom type pduOutputPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_PduOutputPowerFactor_Type.__name__ = "Integer32"
_PduOutputPowerFactor_Object = MibScalar
pduOutputPowerFactor = _PduOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 4),
    _PduOutputPowerFactor_Type()
)
pduOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pduOutputPowerFactor.setUnits("pf * 100")
_PduNeutralCurrent_Type = NonNegativeInteger
_PduNeutralCurrent_Object = MibScalar
pduNeutralCurrent = _PduNeutralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 5),
    _PduNeutralCurrent_Type()
)
pduNeutralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNeutralCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduNeutralCurrent.setUnits("0.1 Amps RMS")
_PduRatedOutputCurrent_Type = PositiveInteger
_PduRatedOutputCurrent_Object = MibScalar
pduRatedOutputCurrent = _PduRatedOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 6),
    _PduRatedOutputCurrent_Type()
)
pduRatedOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRatedOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduRatedOutputCurrent.setUnits("0.1 Amps RMS")


class _PduOutputVoltageUnits_Type(DisplayString):
    """Custom type pduOutputVoltageUnits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PduOutputVoltageUnits_Type.__name__ = "DisplayString"
_PduOutputVoltageUnits_Object = MibScalar
pduOutputVoltageUnits = _PduOutputVoltageUnits_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 7),
    _PduOutputVoltageUnits_Type()
)
pduOutputVoltageUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputVoltageUnits.setStatus("current")
_PduOutputNumPhases_Type = PositiveInteger
_PduOutputNumPhases_Object = MibScalar
pduOutputNumPhases = _PduOutputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 8),
    _PduOutputNumPhases_Type()
)
pduOutputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputNumPhases.setStatus("current")
_PduOutputTable_Object = MibTable
pduOutputTable = _PduOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    pduOutputTable.setStatus("current")
_PduOutputEntry_Object = MibTableRow
pduOutputEntry = _PduOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1)
)
pduOutputEntry.setIndexNames(
    (0, "EATON-PDU-MIB", "pduOutputPhaseIndex"),
)
if mibBuilder.loadTexts:
    pduOutputEntry.setStatus("current")
_PduOutputPhaseIndex_Type = PositiveInteger
_PduOutputPhaseIndex_Object = MibTableColumn
pduOutputPhaseIndex = _PduOutputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 1),
    _PduOutputPhaseIndex_Type()
)
pduOutputPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutputPhaseIndex.setStatus("current")
_PduOutputPhaseVoltage_Type = NonNegativeInteger
_PduOutputPhaseVoltage_Object = MibTableColumn
pduOutputPhaseVoltage = _PduOutputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 2),
    _PduOutputPhaseVoltage_Type()
)
pduOutputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pduOutputPhaseVoltage.setUnits("Volts RMS")
_PduOutputPhaseCurrent_Type = NonNegativeInteger
_PduOutputPhaseCurrent_Object = MibTableColumn
pduOutputPhaseCurrent = _PduOutputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 3),
    _PduOutputPhaseCurrent_Type()
)
pduOutputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduOutputPhaseCurrent.setUnits("0.1 Amps RMS")


class _PduOutputPhasePercentLoad_Type(Integer32):
    """Custom type pduOutputPhasePercentLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PduOutputPhasePercentLoad_Type.__name__ = "Integer32"
_PduOutputPhasePercentLoad_Object = MibTableColumn
pduOutputPhasePercentLoad = _PduOutputPhasePercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 1, 3, 9, 1, 4),
    _PduOutputPhasePercentLoad_Type()
)
pduOutputPhasePercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputPhasePercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    pduOutputPhasePercentLoad.setUnits("percent")
_PduPanel_ObjectIdentity = ObjectIdentity
pduPanel = _PduPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2)
)
_PanelRatingsTable_Object = MibTable
panelRatingsTable = _PanelRatingsTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    panelRatingsTable.setStatus("current")
_PanelRatingsEntry_Object = MibTableRow
panelRatingsEntry = _PanelRatingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1)
)
panelRatingsEntry.setIndexNames(
    (0, "EATON-PDU-MIB", "panelNumber"),
)
if mibBuilder.loadTexts:
    panelRatingsEntry.setStatus("current")
_PanelNumber_Type = PositiveInteger
_PanelNumber_Object = MibTableColumn
panelNumber = _PanelNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 1),
    _PanelNumber_Type()
)
panelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    panelNumber.setStatus("current")
_PanelRatedVoltage_Type = PositiveInteger
_PanelRatedVoltage_Object = MibTableColumn
panelRatedVoltage = _PanelRatedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 2),
    _PanelRatedVoltage_Type()
)
panelRatedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelRatedVoltage.setStatus("current")
if mibBuilder.loadTexts:
    panelRatedVoltage.setUnits("Volts RMS")
_PanelRatedBreakerCurrent_Type = PositiveInteger
_PanelRatedBreakerCurrent_Object = MibTableColumn
panelRatedBreakerCurrent = _PanelRatedBreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 3),
    _PanelRatedBreakerCurrent_Type()
)
panelRatedBreakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelRatedBreakerCurrent.setStatus("current")
if mibBuilder.loadTexts:
    panelRatedBreakerCurrent.setUnits("0.1 Amps RMS")
_PanelNumPhases_Type = PositiveInteger
_PanelNumPhases_Object = MibTableColumn
panelNumPhases = _PanelNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 4),
    _PanelNumPhases_Type()
)
panelNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelNumPhases.setStatus("current")
_PanelNumBreakers_Type = PositiveInteger
_PanelNumBreakers_Object = MibTableColumn
panelNumBreakers = _PanelNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 5),
    _PanelNumBreakers_Type()
)
panelNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelNumBreakers.setStatus("current")


class _PanelVoltageUnits_Type(DisplayString):
    """Custom type panelVoltageUnits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PanelVoltageUnits_Type.__name__ = "DisplayString"
_PanelVoltageUnits_Object = MibTableColumn
panelVoltageUnits = _PanelVoltageUnits_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 1, 1, 6),
    _PanelVoltageUnits_Type()
)
panelVoltageUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelVoltageUnits.setStatus("current")
_PanelMetersTable_Object = MibTable
panelMetersTable = _PanelMetersTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    panelMetersTable.setStatus("current")
_PanelMetersEntry_Object = MibTableRow
panelMetersEntry = _PanelMetersEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1)
)
panelMetersEntry.setIndexNames(
    (0, "EATON-PDU-MIB", "panelNumber"),
)
if mibBuilder.loadTexts:
    panelMetersEntry.setStatus("current")
_PanelTotalKilowattHours_Type = NonNegativeInteger
_PanelTotalKilowattHours_Object = MibTableColumn
panelTotalKilowattHours = _PanelTotalKilowattHours_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 1),
    _PanelTotalKilowattHours_Type()
)
panelTotalKilowattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelTotalKilowattHours.setStatus("current")
if mibBuilder.loadTexts:
    panelTotalKilowattHours.setUnits("KWH")
_PanelMonthlyKilowattHours_Type = NonNegativeInteger
_PanelMonthlyKilowattHours_Object = MibTableColumn
panelMonthlyKilowattHours = _PanelMonthlyKilowattHours_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 2),
    _PanelMonthlyKilowattHours_Type()
)
panelMonthlyKilowattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelMonthlyKilowattHours.setStatus("current")
if mibBuilder.loadTexts:
    panelMonthlyKilowattHours.setUnits("KWH")
_PanelYtdKilowattHours_Type = NonNegativeInteger
_PanelYtdKilowattHours_Object = MibTableColumn
panelYtdKilowattHours = _PanelYtdKilowattHours_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 3),
    _PanelYtdKilowattHours_Type()
)
panelYtdKilowattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelYtdKilowattHours.setStatus("current")
if mibBuilder.loadTexts:
    panelYtdKilowattHours.setUnits("KWH")
_PanelVA_Type = NonNegativeInteger
_PanelVA_Object = MibTableColumn
panelVA = _PanelVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 4),
    _PanelVA_Type()
)
panelVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelVA.setStatus("current")
if mibBuilder.loadTexts:
    panelVA.setUnits("VA")
_PanelPower_Type = NonNegativeInteger
_PanelPower_Object = MibTableColumn
panelPower = _PanelPower_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 5),
    _PanelPower_Type()
)
panelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelPower.setStatus("current")
if mibBuilder.loadTexts:
    panelPower.setUnits("Watts")


class _PanelPowerFactor_Type(Integer32):
    """Custom type panelPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_PanelPowerFactor_Type.__name__ = "Integer32"
_PanelPowerFactor_Object = MibTableColumn
panelPowerFactor = _PanelPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 6),
    _PanelPowerFactor_Type()
)
panelPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    panelPowerFactor.setUnits("pf * 100")
_PanelNeutralCurrent_Type = NonNegativeInteger
_PanelNeutralCurrent_Object = MibTableColumn
panelNeutralCurrent = _PanelNeutralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 2, 1, 7),
    _PanelNeutralCurrent_Type()
)
panelNeutralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelNeutralCurrent.setStatus("current")
if mibBuilder.loadTexts:
    panelNeutralCurrent.setUnits("0.1 Amps RMS")
_PanelPhaseMetersTable_Object = MibTable
panelPhaseMetersTable = _PanelPhaseMetersTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    panelPhaseMetersTable.setStatus("current")
_PanelPhaseMetersEntry_Object = MibTableRow
panelPhaseMetersEntry = _PanelPhaseMetersEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1)
)
panelPhaseMetersEntry.setIndexNames(
    (0, "EATON-PDU-MIB", "panelNumber"),
    (0, "EATON-PDU-MIB", "panelPhaseIndex"),
)
if mibBuilder.loadTexts:
    panelPhaseMetersEntry.setStatus("current")
_PanelPhaseIndex_Type = PositiveInteger
_PanelPhaseIndex_Object = MibTableColumn
panelPhaseIndex = _PanelPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 1),
    _PanelPhaseIndex_Type()
)
panelPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    panelPhaseIndex.setStatus("current")
_PanelPhaseVoltage_Type = NonNegativeInteger
_PanelPhaseVoltage_Object = MibTableColumn
panelPhaseVoltage = _PanelPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 2),
    _PanelPhaseVoltage_Type()
)
panelPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    panelPhaseVoltage.setUnits("Volts RMS")
_PanelPhaseCurrent_Type = NonNegativeInteger
_PanelPhaseCurrent_Object = MibTableColumn
panelPhaseCurrent = _PanelPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 3),
    _PanelPhaseCurrent_Type()
)
panelPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    panelPhaseCurrent.setUnits("0.1 Amps RMS")


class _PanelPhasePercentLoad_Type(Integer32):
    """Custom type panelPhasePercentLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PanelPhasePercentLoad_Type.__name__ = "Integer32"
_PanelPhasePercentLoad_Object = MibTableColumn
panelPhasePercentLoad = _PanelPhasePercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 2, 3, 1, 4),
    _PanelPhasePercentLoad_Type()
)
panelPhasePercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panelPhasePercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    panelPhasePercentLoad.setUnits("percent")
_PduBreaker_ObjectIdentity = ObjectIdentity
pduBreaker = _PduBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3)
)
_BreakerRatingsTable_Object = MibTable
breakerRatingsTable = _BreakerRatingsTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    breakerRatingsTable.setStatus("current")
_BreakerRatingsEntry_Object = MibTableRow
breakerRatingsEntry = _BreakerRatingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1)
)
breakerRatingsEntry.setIndexNames(
    (0, "EATON-PDU-MIB", "panelNumber"),
    (0, "EATON-PDU-MIB", "breakerNumber"),
)
if mibBuilder.loadTexts:
    breakerRatingsEntry.setStatus("current")
_BreakerNumber_Type = PositiveInteger
_BreakerNumber_Object = MibTableColumn
breakerNumber = _BreakerNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 1),
    _BreakerNumber_Type()
)
breakerNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    breakerNumber.setStatus("current")


class _BreakerName_Type(DisplayString):
    """Custom type breakerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BreakerName_Type.__name__ = "DisplayString"
_BreakerName_Object = MibTableColumn
breakerName = _BreakerName_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 2),
    _BreakerName_Type()
)
breakerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerName.setStatus("current")
_BreakerRatedCurrent_Type = PositiveInteger
_BreakerRatedCurrent_Object = MibTableColumn
breakerRatedCurrent = _BreakerRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 3),
    _BreakerRatedCurrent_Type()
)
breakerRatedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerRatedCurrent.setStatus("current")
if mibBuilder.loadTexts:
    breakerRatedCurrent.setUnits("0.1 Amps RMS")
_BreakerNumPhases_Type = PositiveInteger
_BreakerNumPhases_Object = MibTableColumn
breakerNumPhases = _BreakerNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 1, 1, 4),
    _BreakerNumPhases_Type()
)
breakerNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerNumPhases.setStatus("current")
_BreakerMetersTable_Object = MibTable
breakerMetersTable = _BreakerMetersTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    breakerMetersTable.setStatus("current")
_BreakerMetersEntry_Object = MibTableRow
breakerMetersEntry = _BreakerMetersEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1)
)
breakerMetersEntry.setIndexNames(
    (0, "EATON-PDU-MIB", "panelNumber"),
    (0, "EATON-PDU-MIB", "breakerNumber"),
)
if mibBuilder.loadTexts:
    breakerMetersEntry.setStatus("current")
_BreakerTotalKilowattHours_Type = NonNegativeInteger
_BreakerTotalKilowattHours_Object = MibTableColumn
breakerTotalKilowattHours = _BreakerTotalKilowattHours_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1, 1),
    _BreakerTotalKilowattHours_Type()
)
breakerTotalKilowattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerTotalKilowattHours.setStatus("current")
if mibBuilder.loadTexts:
    breakerTotalKilowattHours.setUnits("KWH")
_BreakerMonthlyKilowattHours_Type = NonNegativeInteger
_BreakerMonthlyKilowattHours_Object = MibTableColumn
breakerMonthlyKilowattHours = _BreakerMonthlyKilowattHours_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1, 2),
    _BreakerMonthlyKilowattHours_Type()
)
breakerMonthlyKilowattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerMonthlyKilowattHours.setStatus("current")
if mibBuilder.loadTexts:
    breakerMonthlyKilowattHours.setUnits("KWH")
_BreakerYtdKilowattHours_Type = NonNegativeInteger
_BreakerYtdKilowattHours_Object = MibTableColumn
breakerYtdKilowattHours = _BreakerYtdKilowattHours_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 2, 1, 3),
    _BreakerYtdKilowattHours_Type()
)
breakerYtdKilowattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerYtdKilowattHours.setStatus("current")
if mibBuilder.loadTexts:
    breakerYtdKilowattHours.setUnits("KWH")
_BreakerPhaseMetersTable_Object = MibTable
breakerPhaseMetersTable = _BreakerPhaseMetersTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    breakerPhaseMetersTable.setStatus("current")
_BreakerPhaseMetersEntry_Object = MibTableRow
breakerPhaseMetersEntry = _BreakerPhaseMetersEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1)
)
breakerPhaseMetersEntry.setIndexNames(
    (0, "EATON-PDU-MIB", "panelNumber"),
    (0, "EATON-PDU-MIB", "breakerNumber"),
    (0, "EATON-PDU-MIB", "breakerPhaseIndex"),
)
if mibBuilder.loadTexts:
    breakerPhaseMetersEntry.setStatus("current")
_BreakerPhaseIndex_Type = PositiveInteger
_BreakerPhaseIndex_Object = MibTableColumn
breakerPhaseIndex = _BreakerPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 1),
    _BreakerPhaseIndex_Type()
)
breakerPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    breakerPhaseIndex.setStatus("current")
_BreakerPhaseVA_Type = NonNegativeInteger
_BreakerPhaseVA_Object = MibTableColumn
breakerPhaseVA = _BreakerPhaseVA_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 2),
    _BreakerPhaseVA_Type()
)
breakerPhaseVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerPhaseVA.setStatus("current")
if mibBuilder.loadTexts:
    breakerPhaseVA.setUnits("VA")
_BreakerPhasePower_Type = NonNegativeInteger
_BreakerPhasePower_Object = MibTableColumn
breakerPhasePower = _BreakerPhasePower_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 3),
    _BreakerPhasePower_Type()
)
breakerPhasePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerPhasePower.setStatus("current")
if mibBuilder.loadTexts:
    breakerPhasePower.setUnits("Watts")


class _BreakerPhasePowerFactor_Type(Integer32):
    """Custom type breakerPhasePowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_BreakerPhasePowerFactor_Type.__name__ = "Integer32"
_BreakerPhasePowerFactor_Object = MibTableColumn
breakerPhasePowerFactor = _BreakerPhasePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 4),
    _BreakerPhasePowerFactor_Type()
)
breakerPhasePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerPhasePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    breakerPhasePowerFactor.setUnits("pf * 100")
_BreakerPhaseCurrent_Type = NonNegativeInteger
_BreakerPhaseCurrent_Object = MibTableColumn
breakerPhaseCurrent = _BreakerPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 5),
    _BreakerPhaseCurrent_Type()
)
breakerPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    breakerPhaseCurrent.setUnits("0.1 Amps RMS")


class _BreakerPhasePercentLoad_Type(Integer32):
    """Custom type breakerPhasePercentLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_BreakerPhasePercentLoad_Type.__name__ = "Integer32"
_BreakerPhasePercentLoad_Object = MibTableColumn
breakerPhasePercentLoad = _BreakerPhasePercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 1, 3, 3, 1, 6),
    _BreakerPhasePercentLoad_Type()
)
breakerPhasePercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerPhasePercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    breakerPhasePercentLoad.setUnits("percent")
_EatonPduConformance_ObjectIdentity = ObjectIdentity
eatonPduConformance = _EatonPduConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2)
)

# Managed Objects groups

pduNameplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 1)
)
pduNameplateGroup.setObjects(
      *(("EATON-PDU-MIB", "pduNumPhases"),
        ("EATON-PDU-MIB", "pduNominalOutputVoltage"),
        ("EATON-PDU-MIB", "pduRatingVA"),
        ("EATON-PDU-MIB", "pduNumPanels"))
)
if mibBuilder.loadTexts:
    pduNameplateGroup.setStatus("current")

pduInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 2)
)
pduInputGroup.setObjects(
      *(("EATON-PDU-MIB", "pduFrequency"),
        ("EATON-PDU-MIB", "pduInputVA"),
        ("EATON-PDU-MIB", "pduInputPower"),
        ("EATON-PDU-MIB", "pduInputPowerFactor"),
        ("EATON-PDU-MIB", "pduGroundCurrent"),
        ("EATON-PDU-MIB", "pduInputVoltageUnits"),
        ("EATON-PDU-MIB", "pduInputNumPhases"),
        ("EATON-PDU-MIB", "pduInputPhaseVoltage"),
        ("EATON-PDU-MIB", "pduInputPhaseCurrent"),
        ("EATON-PDU-MIB", "pduInputPhasePercentLoad"))
)
if mibBuilder.loadTexts:
    pduInputGroup.setStatus("current")

pduOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 3)
)
pduOutputGroup.setObjects(
      *(("EATON-PDU-MIB", "pduOutputKilowattHours"),
        ("EATON-PDU-MIB", "pduOutputVA"),
        ("EATON-PDU-MIB", "pduOutputPower"),
        ("EATON-PDU-MIB", "pduOutputPowerFactor"),
        ("EATON-PDU-MIB", "pduNeutralCurrent"),
        ("EATON-PDU-MIB", "pduRatedOutputCurrent"),
        ("EATON-PDU-MIB", "pduOutputVoltageUnits"),
        ("EATON-PDU-MIB", "pduOutputNumPhases"),
        ("EATON-PDU-MIB", "pduOutputPhaseVoltage"),
        ("EATON-PDU-MIB", "pduOutputPhaseCurrent"),
        ("EATON-PDU-MIB", "pduOutputPhasePercentLoad"))
)
if mibBuilder.loadTexts:
    pduOutputGroup.setStatus("current")

panelRatingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 4)
)
panelRatingsGroup.setObjects(
      *(("EATON-PDU-MIB", "panelRatedVoltage"),
        ("EATON-PDU-MIB", "panelRatedBreakerCurrent"),
        ("EATON-PDU-MIB", "panelNumPhases"),
        ("EATON-PDU-MIB", "panelNumBreakers"),
        ("EATON-PDU-MIB", "panelVoltageUnits"))
)
if mibBuilder.loadTexts:
    panelRatingsGroup.setStatus("current")

panelMetersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 5)
)
panelMetersGroup.setObjects(
      *(("EATON-PDU-MIB", "panelTotalKilowattHours"),
        ("EATON-PDU-MIB", "panelMonthlyKilowattHours"),
        ("EATON-PDU-MIB", "panelYtdKilowattHours"),
        ("EATON-PDU-MIB", "panelVA"),
        ("EATON-PDU-MIB", "panelPower"),
        ("EATON-PDU-MIB", "panelPowerFactor"),
        ("EATON-PDU-MIB", "panelNeutralCurrent"))
)
if mibBuilder.loadTexts:
    panelMetersGroup.setStatus("current")

panelPhaseMetersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 6)
)
panelPhaseMetersGroup.setObjects(
      *(("EATON-PDU-MIB", "panelPhaseVoltage"),
        ("EATON-PDU-MIB", "panelPhaseCurrent"),
        ("EATON-PDU-MIB", "panelPhasePercentLoad"))
)
if mibBuilder.loadTexts:
    panelPhaseMetersGroup.setStatus("current")

breakerRatingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 7)
)
breakerRatingsGroup.setObjects(
      *(("EATON-PDU-MIB", "breakerName"),
        ("EATON-PDU-MIB", "breakerRatedCurrent"),
        ("EATON-PDU-MIB", "breakerNumPhases"))
)
if mibBuilder.loadTexts:
    breakerRatingsGroup.setStatus("current")

breakerMetersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 8)
)
breakerMetersGroup.setObjects(
      *(("EATON-PDU-MIB", "breakerTotalKilowattHours"),
        ("EATON-PDU-MIB", "breakerMonthlyKilowattHours"),
        ("EATON-PDU-MIB", "breakerYtdKilowattHours"))
)
if mibBuilder.loadTexts:
    breakerMetersGroup.setStatus("current")

breakerPhaseMetersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 9)
)
breakerPhaseMetersGroup.setObjects(
      *(("EATON-PDU-MIB", "breakerPhaseVA"),
        ("EATON-PDU-MIB", "breakerPhasePower"),
        ("EATON-PDU-MIB", "breakerPhasePowerFactor"),
        ("EATON-PDU-MIB", "breakerPhaseCurrent"),
        ("EATON-PDU-MIB", "breakerPhasePercentLoad"))
)
if mibBuilder.loadTexts:
    breakerPhaseMetersGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdu3phaseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 534, 6, 6, 4, 2, 10)
)
if mibBuilder.loadTexts:
    pdu3phaseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EATON-PDU-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "eatonPduMIB": eatonPduMIB,
       "eatonPduMIBObjects": eatonPduMIBObjects,
       "mainPdu": mainPdu,
       "pduNameplate": pduNameplate,
       "pduRatingVA": pduRatingVA,
       "pduNominalOutputVoltage": pduNominalOutputVoltage,
       "pduNumPhases": pduNumPhases,
       "pduNumPanels": pduNumPanels,
       "pduInput": pduInput,
       "pduFrequency": pduFrequency,
       "pduInputVA": pduInputVA,
       "pduInputPower": pduInputPower,
       "pduInputPowerFactor": pduInputPowerFactor,
       "pduGroundCurrent": pduGroundCurrent,
       "pduInputVoltageUnits": pduInputVoltageUnits,
       "pduInputNumPhases": pduInputNumPhases,
       "pduInputTable": pduInputTable,
       "pduInputEntry": pduInputEntry,
       "pduInputPhaseIndex": pduInputPhaseIndex,
       "pduInputPhaseVoltage": pduInputPhaseVoltage,
       "pduInputPhaseCurrent": pduInputPhaseCurrent,
       "pduInputPhasePercentLoad": pduInputPhasePercentLoad,
       "pduOutput": pduOutput,
       "pduOutputKilowattHours": pduOutputKilowattHours,
       "pduOutputVA": pduOutputVA,
       "pduOutputPower": pduOutputPower,
       "pduOutputPowerFactor": pduOutputPowerFactor,
       "pduNeutralCurrent": pduNeutralCurrent,
       "pduRatedOutputCurrent": pduRatedOutputCurrent,
       "pduOutputVoltageUnits": pduOutputVoltageUnits,
       "pduOutputNumPhases": pduOutputNumPhases,
       "pduOutputTable": pduOutputTable,
       "pduOutputEntry": pduOutputEntry,
       "pduOutputPhaseIndex": pduOutputPhaseIndex,
       "pduOutputPhaseVoltage": pduOutputPhaseVoltage,
       "pduOutputPhaseCurrent": pduOutputPhaseCurrent,
       "pduOutputPhasePercentLoad": pduOutputPhasePercentLoad,
       "pduPanel": pduPanel,
       "panelRatingsTable": panelRatingsTable,
       "panelRatingsEntry": panelRatingsEntry,
       "panelNumber": panelNumber,
       "panelRatedVoltage": panelRatedVoltage,
       "panelRatedBreakerCurrent": panelRatedBreakerCurrent,
       "panelNumPhases": panelNumPhases,
       "panelNumBreakers": panelNumBreakers,
       "panelVoltageUnits": panelVoltageUnits,
       "panelMetersTable": panelMetersTable,
       "panelMetersEntry": panelMetersEntry,
       "panelTotalKilowattHours": panelTotalKilowattHours,
       "panelMonthlyKilowattHours": panelMonthlyKilowattHours,
       "panelYtdKilowattHours": panelYtdKilowattHours,
       "panelVA": panelVA,
       "panelPower": panelPower,
       "panelPowerFactor": panelPowerFactor,
       "panelNeutralCurrent": panelNeutralCurrent,
       "panelPhaseMetersTable": panelPhaseMetersTable,
       "panelPhaseMetersEntry": panelPhaseMetersEntry,
       "panelPhaseIndex": panelPhaseIndex,
       "panelPhaseVoltage": panelPhaseVoltage,
       "panelPhaseCurrent": panelPhaseCurrent,
       "panelPhasePercentLoad": panelPhasePercentLoad,
       "pduBreaker": pduBreaker,
       "breakerRatingsTable": breakerRatingsTable,
       "breakerRatingsEntry": breakerRatingsEntry,
       "breakerNumber": breakerNumber,
       "breakerName": breakerName,
       "breakerRatedCurrent": breakerRatedCurrent,
       "breakerNumPhases": breakerNumPhases,
       "breakerMetersTable": breakerMetersTable,
       "breakerMetersEntry": breakerMetersEntry,
       "breakerTotalKilowattHours": breakerTotalKilowattHours,
       "breakerMonthlyKilowattHours": breakerMonthlyKilowattHours,
       "breakerYtdKilowattHours": breakerYtdKilowattHours,
       "breakerPhaseMetersTable": breakerPhaseMetersTable,
       "breakerPhaseMetersEntry": breakerPhaseMetersEntry,
       "breakerPhaseIndex": breakerPhaseIndex,
       "breakerPhaseVA": breakerPhaseVA,
       "breakerPhasePower": breakerPhasePower,
       "breakerPhasePowerFactor": breakerPhasePowerFactor,
       "breakerPhaseCurrent": breakerPhaseCurrent,
       "breakerPhasePercentLoad": breakerPhasePercentLoad,
       "eatonPduConformance": eatonPduConformance,
       "pduNameplateGroup": pduNameplateGroup,
       "pduInputGroup": pduInputGroup,
       "pduOutputGroup": pduOutputGroup,
       "panelRatingsGroup": panelRatingsGroup,
       "panelMetersGroup": panelMetersGroup,
       "panelPhaseMetersGroup": panelPhaseMetersGroup,
       "breakerRatingsGroup": breakerRatingsGroup,
       "breakerMetersGroup": breakerMetersGroup,
       "breakerPhaseMetersGroup": breakerPhaseMetersGroup,
       "pdu3phaseCompliance": pdu3phaseCompliance}
)
