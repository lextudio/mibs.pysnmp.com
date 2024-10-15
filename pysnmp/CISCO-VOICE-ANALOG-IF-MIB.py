# SNMP MIB module (CISCO-VOICE-ANALOG-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-ANALOG-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:15 2024
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

ciscoVoiceAnalogIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 62)
)
ciscoVoiceAnalogIfMIB.setRevisions(
        ("2005-10-03 00:00",
         "2004-10-14 00:00",
         "2004-01-15 00:00",
         "2002-08-03 00:00",
         "2002-07-29 00:00",
         "2002-01-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceDialType(Integer32, TextualConvention):
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
        *(("dtmf", 1),
          ("mf", 3),
          ("pulse", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CvaIfObjects_ObjectIdentity = ObjectIdentity
cvaIfObjects = _CvaIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1)
)
_CvaIfGeneralObjects_ObjectIdentity = ObjectIdentity
cvaIfGeneralObjects = _CvaIfGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 1)
)
_CvaIfCfgTable_Object = MibTable
cvaIfCfgTable = _CvaIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvaIfCfgTable.setStatus("current")
_CvaIfCfgEntry_Object = MibTableRow
cvaIfCfgEntry = _CvaIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 1, 1, 1)
)
cvaIfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvaIfCfgEntry.setStatus("current")


class _CvaIfCfgImpedance_Type(Integer32):
    """Custom type cvaIfCfgImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ohms600Complex", 3),
          ("ohms600Real", 2),
          ("ohms900Complex", 4),
          ("ohmsComplex1", 5),
          ("ohmsComplex2", 6),
          ("other", 1))
    )


_CvaIfCfgImpedance_Type.__name__ = "Integer32"
_CvaIfCfgImpedance_Object = MibTableColumn
cvaIfCfgImpedance = _CvaIfCfgImpedance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 1, 1, 1, 1),
    _CvaIfCfgImpedance_Type()
)
cvaIfCfgImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfCfgImpedance.setStatus("current")
_CvaIfCfgIntegratedDSP_Type = TruthValue
_CvaIfCfgIntegratedDSP_Object = MibTableColumn
cvaIfCfgIntegratedDSP = _CvaIfCfgIntegratedDSP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 1, 1, 1, 2),
    _CvaIfCfgIntegratedDSP_Type()
)
cvaIfCfgIntegratedDSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfCfgIntegratedDSP.setStatus("current")
_CvaIfStatusTable_Object = MibTable
cvaIfStatusTable = _CvaIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvaIfStatusTable.setStatus("current")
_CvaIfStatusEntry_Object = MibTableRow
cvaIfStatusEntry = _CvaIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvaIfStatusEntry.setStatus("current")


class _CvaIfStatusInfoType_Type(Integer32):
    """Custom type cvaIfStatusInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g3Fax", 3),
          ("none", 1),
          ("voice", 2))
    )


_CvaIfStatusInfoType_Type.__name__ = "Integer32"
_CvaIfStatusInfoType_Object = MibTableColumn
cvaIfStatusInfoType = _CvaIfStatusInfoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 1, 2, 1, 1),
    _CvaIfStatusInfoType_Type()
)
cvaIfStatusInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfStatusInfoType.setStatus("current")


class _CvaIfMaintenanceMode_Type(Integer32):
    """Custom type cvaIfMaintenanceMode based on Integer32"""
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
        *(("hostCompressedLoopback", 2),
          ("hostUncompressedLoopback", 3),
          ("ifCompressedLoopback", 4),
          ("ifUncompressedLoopback", 5),
          ("none", 1))
    )


_CvaIfMaintenanceMode_Type.__name__ = "Integer32"
_CvaIfMaintenanceMode_Object = MibTableColumn
cvaIfMaintenanceMode = _CvaIfMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 1, 2, 1, 2),
    _CvaIfMaintenanceMode_Type()
)
cvaIfMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfMaintenanceMode.setStatus("current")
_CvaIfStatusSignalErrors_Type = Counter32
_CvaIfStatusSignalErrors_Object = MibTableColumn
cvaIfStatusSignalErrors = _CvaIfStatusSignalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 1, 2, 1, 3),
    _CvaIfStatusSignalErrors_Type()
)
cvaIfStatusSignalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfStatusSignalErrors.setStatus("current")
_CvaIfEMObjects_ObjectIdentity = ObjectIdentity
cvaIfEMObjects = _CvaIfEMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2)
)
_CvaIfEMCfgTable_Object = MibTable
cvaIfEMCfgTable = _CvaIfEMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvaIfEMCfgTable.setStatus("current")
_CvaIfEMCfgEntry_Object = MibTableRow
cvaIfEMCfgEntry = _CvaIfEMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 1, 1)
)
cvaIfEMCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvaIfEMCfgEntry.setStatus("current")


class _CvaIfEMCfgSignalType_Type(Integer32):
    """Custom type cvaIfEMCfgSignalType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("delayDial", 3),
          ("fgd", 5),
          ("fgd-eana", 6),
          ("immediateDial", 2),
          ("lmr", 4),
          ("winkStart", 1))
    )


_CvaIfEMCfgSignalType_Type.__name__ = "Integer32"
_CvaIfEMCfgSignalType_Object = MibTableColumn
cvaIfEMCfgSignalType = _CvaIfEMCfgSignalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 1, 1, 1),
    _CvaIfEMCfgSignalType_Type()
)
cvaIfEMCfgSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMCfgSignalType.setStatus("current")


class _CvaIfEMCfgOperation_Type(Integer32):
    """Custom type cvaIfEMCfgOperation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourWires", 2),
          ("twoWires", 1))
    )


_CvaIfEMCfgOperation_Type.__name__ = "Integer32"
_CvaIfEMCfgOperation_Object = MibTableColumn
cvaIfEMCfgOperation = _CvaIfEMCfgOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 1, 1, 2),
    _CvaIfEMCfgOperation_Type()
)
cvaIfEMCfgOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMCfgOperation.setStatus("current")


class _CvaIfEMCfgType_Type(Integer32):
    """Custom type cvaIfEMCfgType based on Integer32"""
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
        *(("typeI", 1),
          ("typeII", 2),
          ("typeIII", 3),
          ("typeIV", 4),
          ("typeV", 5))
    )


_CvaIfEMCfgType_Type.__name__ = "Integer32"
_CvaIfEMCfgType_Object = MibTableColumn
cvaIfEMCfgType = _CvaIfEMCfgType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 1, 1, 3),
    _CvaIfEMCfgType_Type()
)
cvaIfEMCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMCfgType.setStatus("current")


class _CvaIfEMCfgDialType_Type(InterfaceDialType):
    """Custom type cvaIfEMCfgDialType based on InterfaceDialType"""


_CvaIfEMCfgDialType_Object = MibTableColumn
cvaIfEMCfgDialType = _CvaIfEMCfgDialType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 1, 1, 4),
    _CvaIfEMCfgDialType_Type()
)
cvaIfEMCfgDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMCfgDialType.setStatus("current")


class _CvaIfEMCfgLmrMCap_Type(Integer32):
    """Custom type cvaIfEMCfgLmrMCap based on Integer32"""
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
        *(("audio", 2),
          ("dial", 3),
          ("inact", 1))
    )


_CvaIfEMCfgLmrMCap_Type.__name__ = "Integer32"
_CvaIfEMCfgLmrMCap_Object = MibTableColumn
cvaIfEMCfgLmrMCap = _CvaIfEMCfgLmrMCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 1, 1, 5),
    _CvaIfEMCfgLmrMCap_Type()
)
cvaIfEMCfgLmrMCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMCfgLmrMCap.setStatus("current")


class _CvaIfEMCfgLmrECap_Type(Integer32):
    """Custom type cvaIfEMCfgLmrECap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 6),
          ("seize", 4),
          ("voice", 5))
    )


_CvaIfEMCfgLmrECap_Type.__name__ = "Integer32"
_CvaIfEMCfgLmrECap_Object = MibTableColumn
cvaIfEMCfgLmrECap = _CvaIfEMCfgLmrECap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 1, 1, 6),
    _CvaIfEMCfgLmrECap_Type()
)
cvaIfEMCfgLmrECap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMCfgLmrECap.setStatus("current")


class _CvaIfEMCfgAutoGainControl_Type(TruthValue):
    """Custom type cvaIfEMCfgAutoGainControl based on TruthValue"""


_CvaIfEMCfgAutoGainControl_Object = MibTableColumn
cvaIfEMCfgAutoGainControl = _CvaIfEMCfgAutoGainControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 1, 1, 7),
    _CvaIfEMCfgAutoGainControl_Type()
)
cvaIfEMCfgAutoGainControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMCfgAutoGainControl.setStatus("current")
_CvaIfEMStatusTable_Object = MibTable
cvaIfEMStatusTable = _CvaIfEMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cvaIfEMStatusTable.setStatus("current")
_CvaIfEMStatusEntry_Object = MibTableRow
cvaIfEMStatusEntry = _CvaIfEMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cvaIfEMStatusEntry.setStatus("current")
_CvaIfEMInSeizureActive_Type = TruthValue
_CvaIfEMInSeizureActive_Object = MibTableColumn
cvaIfEMInSeizureActive = _CvaIfEMInSeizureActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 2, 1, 1),
    _CvaIfEMInSeizureActive_Type()
)
cvaIfEMInSeizureActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfEMInSeizureActive.setStatus("current")
_CvaIfEMOutSeizureActive_Type = TruthValue
_CvaIfEMOutSeizureActive_Object = MibTableColumn
cvaIfEMOutSeizureActive = _CvaIfEMOutSeizureActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 2, 1, 2),
    _CvaIfEMOutSeizureActive_Type()
)
cvaIfEMOutSeizureActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfEMOutSeizureActive.setStatus("current")
_CvaIfEMTimingTable_Object = MibTable
cvaIfEMTimingTable = _CvaIfEMTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cvaIfEMTimingTable.setStatus("current")
_CvaIfEMTimingEntry_Object = MibTableRow
cvaIfEMTimingEntry = _CvaIfEMTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cvaIfEMTimingEntry.setStatus("current")


class _CvaIfEMTimingDigitDuration_Type(Integer32):
    """Custom type cvaIfEMTimingDigitDuration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CvaIfEMTimingDigitDuration_Type.__name__ = "Integer32"
_CvaIfEMTimingDigitDuration_Object = MibTableColumn
cvaIfEMTimingDigitDuration = _CvaIfEMTimingDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 1),
    _CvaIfEMTimingDigitDuration_Type()
)
cvaIfEMTimingDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingDigitDuration.setUnits("milliseconds")


class _CvaIfEMTimingInterDigitDuration_Type(Integer32):
    """Custom type cvaIfEMTimingInterDigitDuration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CvaIfEMTimingInterDigitDuration_Type.__name__ = "Integer32"
_CvaIfEMTimingInterDigitDuration_Object = MibTableColumn
cvaIfEMTimingInterDigitDuration = _CvaIfEMTimingInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 2),
    _CvaIfEMTimingInterDigitDuration_Type()
)
cvaIfEMTimingInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingInterDigitDuration.setUnits("milliseconds")


class _CvaIfEMTimingPulseRate_Type(Integer32):
    """Custom type cvaIfEMTimingPulseRate based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20),
    )


_CvaIfEMTimingPulseRate_Type.__name__ = "Integer32"
_CvaIfEMTimingPulseRate_Object = MibTableColumn
cvaIfEMTimingPulseRate = _CvaIfEMTimingPulseRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 3),
    _CvaIfEMTimingPulseRate_Type()
)
cvaIfEMTimingPulseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingPulseRate.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingPulseRate.setUnits("pulses per second")


class _CvaIfEMTimingPulseInterDigitDuration_Type(Integer32):
    """Custom type cvaIfEMTimingPulseInterDigitDuration based on Integer32"""
    defaultValue = 750

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CvaIfEMTimingPulseInterDigitDuration_Type.__name__ = "Integer32"
_CvaIfEMTimingPulseInterDigitDuration_Object = MibTableColumn
cvaIfEMTimingPulseInterDigitDuration = _CvaIfEMTimingPulseInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 4),
    _CvaIfEMTimingPulseInterDigitDuration_Type()
)
cvaIfEMTimingPulseInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingPulseInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingPulseInterDigitDuration.setUnits("milliseconds")


class _CvaIfEMTimingClearWaitDuration_Type(Integer32):
    """Custom type cvaIfEMTimingClearWaitDuration based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 2000),
    )


_CvaIfEMTimingClearWaitDuration_Type.__name__ = "Integer32"
_CvaIfEMTimingClearWaitDuration_Object = MibTableColumn
cvaIfEMTimingClearWaitDuration = _CvaIfEMTimingClearWaitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 5),
    _CvaIfEMTimingClearWaitDuration_Type()
)
cvaIfEMTimingClearWaitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingClearWaitDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingClearWaitDuration.setUnits("milliseconds")


class _CvaIfEMTimingMaxWinkWaitDuration_Type(Integer32):
    """Custom type cvaIfEMTimingMaxWinkWaitDuration based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_CvaIfEMTimingMaxWinkWaitDuration_Type.__name__ = "Integer32"
_CvaIfEMTimingMaxWinkWaitDuration_Object = MibTableColumn
cvaIfEMTimingMaxWinkWaitDuration = _CvaIfEMTimingMaxWinkWaitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 6),
    _CvaIfEMTimingMaxWinkWaitDuration_Type()
)
cvaIfEMTimingMaxWinkWaitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingMaxWinkWaitDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingMaxWinkWaitDuration.setUnits("milliseconds")


class _CvaIfEMTimingMaxWinkDuration_Type(Integer32):
    """Custom type cvaIfEMTimingMaxWinkDuration based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3000),
    )


_CvaIfEMTimingMaxWinkDuration_Type.__name__ = "Integer32"
_CvaIfEMTimingMaxWinkDuration_Object = MibTableColumn
cvaIfEMTimingMaxWinkDuration = _CvaIfEMTimingMaxWinkDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 7),
    _CvaIfEMTimingMaxWinkDuration_Type()
)
cvaIfEMTimingMaxWinkDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingMaxWinkDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingMaxWinkDuration.setUnits("milliseconds")


class _CvaIfEMTimingDelayStart_Type(Integer32):
    """Custom type cvaIfEMTimingDelayStart based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_CvaIfEMTimingDelayStart_Type.__name__ = "Integer32"
_CvaIfEMTimingDelayStart_Object = MibTableColumn
cvaIfEMTimingDelayStart = _CvaIfEMTimingDelayStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 8),
    _CvaIfEMTimingDelayStart_Type()
)
cvaIfEMTimingDelayStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingDelayStart.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingDelayStart.setUnits("milliseconds")


class _CvaIfEMTimingMaxDelayDuration_Type(Integer32):
    """Custom type cvaIfEMTimingMaxDelayDuration based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_CvaIfEMTimingMaxDelayDuration_Type.__name__ = "Integer32"
_CvaIfEMTimingMaxDelayDuration_Object = MibTableColumn
cvaIfEMTimingMaxDelayDuration = _CvaIfEMTimingMaxDelayDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 9),
    _CvaIfEMTimingMaxDelayDuration_Type()
)
cvaIfEMTimingMaxDelayDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingMaxDelayDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingMaxDelayDuration.setUnits("milliseconds")


class _CvaIfEMTimingMinDelayPulseWidth_Type(Integer32):
    """Custom type cvaIfEMTimingMinDelayPulseWidth based on Integer32"""
    defaultValue = 140

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(140, 5000),
    )


_CvaIfEMTimingMinDelayPulseWidth_Type.__name__ = "Integer32"
_CvaIfEMTimingMinDelayPulseWidth_Object = MibTableColumn
cvaIfEMTimingMinDelayPulseWidth = _CvaIfEMTimingMinDelayPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 10),
    _CvaIfEMTimingMinDelayPulseWidth_Type()
)
cvaIfEMTimingMinDelayPulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingMinDelayPulseWidth.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingMinDelayPulseWidth.setUnits("milliseconds")


class _CvaIfEMTimingVoiceHangover_Type(Integer32):
    """Custom type cvaIfEMTimingVoiceHangover based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CvaIfEMTimingVoiceHangover_Type.__name__ = "Integer32"
_CvaIfEMTimingVoiceHangover_Object = MibTableColumn
cvaIfEMTimingVoiceHangover = _CvaIfEMTimingVoiceHangover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 11),
    _CvaIfEMTimingVoiceHangover_Type()
)
cvaIfEMTimingVoiceHangover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingVoiceHangover.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingVoiceHangover.setUnits("milliseconds")


class _CvaIfEMTimeoutLmrTeardown_Type(Integer32):
    """Custom type cvaIfEMTimeoutLmrTeardown based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(5, 60000),
    )


_CvaIfEMTimeoutLmrTeardown_Type.__name__ = "Integer32"
_CvaIfEMTimeoutLmrTeardown_Object = MibTableColumn
cvaIfEMTimeoutLmrTeardown = _CvaIfEMTimeoutLmrTeardown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 12),
    _CvaIfEMTimeoutLmrTeardown_Type()
)
cvaIfEMTimeoutLmrTeardown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimeoutLmrTeardown.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimeoutLmrTeardown.setUnits("seconds")


class _CvaIfEMTimeoutPttXmt_Type(Integer32):
    """Custom type cvaIfEMTimeoutPttXmt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CvaIfEMTimeoutPttXmt_Type.__name__ = "Integer32"
_CvaIfEMTimeoutPttXmt_Object = MibTableColumn
cvaIfEMTimeoutPttXmt = _CvaIfEMTimeoutPttXmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 13),
    _CvaIfEMTimeoutPttXmt_Type()
)
cvaIfEMTimeoutPttXmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimeoutPttXmt.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimeoutPttXmt.setUnits("minutes")


class _CvaIfEMTimeoutPttRcv_Type(Integer32):
    """Custom type cvaIfEMTimeoutPttRcv based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CvaIfEMTimeoutPttRcv_Type.__name__ = "Integer32"
_CvaIfEMTimeoutPttRcv_Object = MibTableColumn
cvaIfEMTimeoutPttRcv = _CvaIfEMTimeoutPttRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 14),
    _CvaIfEMTimeoutPttRcv_Type()
)
cvaIfEMTimeoutPttRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimeoutPttRcv.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimeoutPttRcv.setUnits("minutes")


class _CvaIfEMTimingDelayVoice_Type(Integer32):
    """Custom type cvaIfEMTimingDelayVoice based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_CvaIfEMTimingDelayVoice_Type.__name__ = "Integer32"
_CvaIfEMTimingDelayVoice_Object = MibTableColumn
cvaIfEMTimingDelayVoice = _CvaIfEMTimingDelayVoice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 2, 3, 1, 15),
    _CvaIfEMTimingDelayVoice_Type()
)
cvaIfEMTimingDelayVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfEMTimingDelayVoice.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfEMTimingDelayVoice.setUnits("milliseconds")
_CvaIfFXOObjects_ObjectIdentity = ObjectIdentity
cvaIfFXOObjects = _CvaIfFXOObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3)
)
_CvaIfFXOCfgTable_Object = MibTable
cvaIfFXOCfgTable = _CvaIfFXOCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cvaIfFXOCfgTable.setStatus("current")
_CvaIfFXOCfgEntry_Object = MibTableRow
cvaIfFXOCfgEntry = _CvaIfFXOCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 1, 1)
)
cvaIfFXOCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvaIfFXOCfgEntry.setStatus("current")


class _CvaIfFXOCfgSignalType_Type(Integer32):
    """Custom type cvaIfFXOCfgSignalType based on Integer32"""
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
        *(("fxoCama", 3),
          ("fxoGroundStart", 2),
          ("fxoLoopStart", 1))
    )


_CvaIfFXOCfgSignalType_Type.__name__ = "Integer32"
_CvaIfFXOCfgSignalType_Object = MibTableColumn
cvaIfFXOCfgSignalType = _CvaIfFXOCfgSignalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 1, 1, 1),
    _CvaIfFXOCfgSignalType_Type()
)
cvaIfFXOCfgSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXOCfgSignalType.setStatus("current")


class _CvaIfFXOCfgNumberRings_Type(Integer32):
    """Custom type cvaIfFXOCfgNumberRings based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CvaIfFXOCfgNumberRings_Type.__name__ = "Integer32"
_CvaIfFXOCfgNumberRings_Object = MibTableColumn
cvaIfFXOCfgNumberRings = _CvaIfFXOCfgNumberRings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 1, 1, 2),
    _CvaIfFXOCfgNumberRings_Type()
)
cvaIfFXOCfgNumberRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXOCfgNumberRings.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfFXOCfgNumberRings.setUnits("rings")


class _CvaIfFXOCfgSupDisconnect_Type(TruthValue):
    """Custom type cvaIfFXOCfgSupDisconnect based on TruthValue"""


_CvaIfFXOCfgSupDisconnect_Object = MibTableColumn
cvaIfFXOCfgSupDisconnect = _CvaIfFXOCfgSupDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 1, 1, 3),
    _CvaIfFXOCfgSupDisconnect_Type()
)
cvaIfFXOCfgSupDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXOCfgSupDisconnect.setStatus("deprecated")


class _CvaIfFXOCfgDialType_Type(InterfaceDialType):
    """Custom type cvaIfFXOCfgDialType based on InterfaceDialType"""


_CvaIfFXOCfgDialType_Object = MibTableColumn
cvaIfFXOCfgDialType = _CvaIfFXOCfgDialType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 1, 1, 4),
    _CvaIfFXOCfgDialType_Type()
)
cvaIfFXOCfgDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXOCfgDialType.setStatus("current")


class _CvaIfFXOCfgSupDisconnect2_Type(Integer32):
    """Custom type cvaIfFXOCfgSupDisconnect2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anytone", 1),
          ("dualtoneMidcall", 2),
          ("dualtonePreconnect", 3),
          ("signal", 0))
    )


_CvaIfFXOCfgSupDisconnect2_Type.__name__ = "Integer32"
_CvaIfFXOCfgSupDisconnect2_Object = MibTableColumn
cvaIfFXOCfgSupDisconnect2 = _CvaIfFXOCfgSupDisconnect2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 1, 1, 5),
    _CvaIfFXOCfgSupDisconnect2_Type()
)
cvaIfFXOCfgSupDisconnect2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXOCfgSupDisconnect2.setStatus("current")
_CvaIfFXOStatusTable_Object = MibTable
cvaIfFXOStatusTable = _CvaIfFXOStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cvaIfFXOStatusTable.setStatus("current")
_CvaIfFXOStatusEntry_Object = MibTableRow
cvaIfFXOStatusEntry = _CvaIfFXOStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cvaIfFXOStatusEntry.setStatus("current")


class _CvaIfFXOHookStatus_Type(Integer32):
    """Custom type cvaIfFXOHookStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offHook", 2),
          ("onHook", 1),
          ("trunked", 3))
    )


_CvaIfFXOHookStatus_Type.__name__ = "Integer32"
_CvaIfFXOHookStatus_Object = MibTableColumn
cvaIfFXOHookStatus = _CvaIfFXOHookStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 2, 1, 1),
    _CvaIfFXOHookStatus_Type()
)
cvaIfFXOHookStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfFXOHookStatus.setStatus("current")
_CvaIfFXORingDetect_Type = TruthValue
_CvaIfFXORingDetect_Object = MibTableColumn
cvaIfFXORingDetect = _CvaIfFXORingDetect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 2, 1, 2),
    _CvaIfFXORingDetect_Type()
)
cvaIfFXORingDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfFXORingDetect.setStatus("current")
_CvaIfFXORingGround_Type = TruthValue
_CvaIfFXORingGround_Object = MibTableColumn
cvaIfFXORingGround = _CvaIfFXORingGround_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 2, 1, 3),
    _CvaIfFXORingGround_Type()
)
cvaIfFXORingGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfFXORingGround.setStatus("current")
_CvaIfFXOTipGround_Type = TruthValue
_CvaIfFXOTipGround_Object = MibTableColumn
cvaIfFXOTipGround = _CvaIfFXOTipGround_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 2, 1, 4),
    _CvaIfFXOTipGround_Type()
)
cvaIfFXOTipGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfFXOTipGround.setStatus("current")
_CvaIfFXOTimingTable_Object = MibTable
cvaIfFXOTimingTable = _CvaIfFXOTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cvaIfFXOTimingTable.setStatus("current")
_CvaIfFXOTimingEntry_Object = MibTableRow
cvaIfFXOTimingEntry = _CvaIfFXOTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cvaIfFXOTimingEntry.setStatus("current")


class _CvaIfFXOTimingDigitDuration_Type(Integer32):
    """Custom type cvaIfFXOTimingDigitDuration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CvaIfFXOTimingDigitDuration_Type.__name__ = "Integer32"
_CvaIfFXOTimingDigitDuration_Object = MibTableColumn
cvaIfFXOTimingDigitDuration = _CvaIfFXOTimingDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 3, 1, 1),
    _CvaIfFXOTimingDigitDuration_Type()
)
cvaIfFXOTimingDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXOTimingDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfFXOTimingDigitDuration.setUnits("milliseconds")


class _CvaIfFXOTimingInterDigitDuration_Type(Integer32):
    """Custom type cvaIfFXOTimingInterDigitDuration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CvaIfFXOTimingInterDigitDuration_Type.__name__ = "Integer32"
_CvaIfFXOTimingInterDigitDuration_Object = MibTableColumn
cvaIfFXOTimingInterDigitDuration = _CvaIfFXOTimingInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 3, 1, 2),
    _CvaIfFXOTimingInterDigitDuration_Type()
)
cvaIfFXOTimingInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXOTimingInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfFXOTimingInterDigitDuration.setUnits("milliseconds")


class _CvaIfFXOTimingPulseRate_Type(Integer32):
    """Custom type cvaIfFXOTimingPulseRate based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20),
    )


_CvaIfFXOTimingPulseRate_Type.__name__ = "Integer32"
_CvaIfFXOTimingPulseRate_Object = MibTableColumn
cvaIfFXOTimingPulseRate = _CvaIfFXOTimingPulseRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 3, 1, 3),
    _CvaIfFXOTimingPulseRate_Type()
)
cvaIfFXOTimingPulseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXOTimingPulseRate.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfFXOTimingPulseRate.setUnits("pulses per second")


class _CvaIfFXOTimingPulseInterDigitDuration_Type(Integer32):
    """Custom type cvaIfFXOTimingPulseInterDigitDuration based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CvaIfFXOTimingPulseInterDigitDuration_Type.__name__ = "Integer32"
_CvaIfFXOTimingPulseInterDigitDuration_Object = MibTableColumn
cvaIfFXOTimingPulseInterDigitDuration = _CvaIfFXOTimingPulseInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 3, 3, 1, 4),
    _CvaIfFXOTimingPulseInterDigitDuration_Type()
)
cvaIfFXOTimingPulseInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXOTimingPulseInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfFXOTimingPulseInterDigitDuration.setUnits("milliseconds")
_CvaIfFXSObjects_ObjectIdentity = ObjectIdentity
cvaIfFXSObjects = _CvaIfFXSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4)
)
_CvaIfFXSCfgTable_Object = MibTable
cvaIfFXSCfgTable = _CvaIfFXSCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cvaIfFXSCfgTable.setStatus("current")
_CvaIfFXSCfgEntry_Object = MibTableRow
cvaIfFXSCfgEntry = _CvaIfFXSCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 1, 1)
)
cvaIfFXSCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvaIfFXSCfgEntry.setStatus("current")


class _CvaIfFXSCfgSignalType_Type(Integer32):
    """Custom type cvaIfFXSCfgSignalType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fxsGroundStart", 2),
          ("fxsLoopStart", 1))
    )


_CvaIfFXSCfgSignalType_Type.__name__ = "Integer32"
_CvaIfFXSCfgSignalType_Object = MibTableColumn
cvaIfFXSCfgSignalType = _CvaIfFXSCfgSignalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 1, 1, 1),
    _CvaIfFXSCfgSignalType_Type()
)
cvaIfFXSCfgSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXSCfgSignalType.setStatus("current")


class _CvaIfFXSRingFrequency_Type(Integer32):
    """Custom type cvaIfFXSRingFrequency based on Integer32"""
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
        *(("ringFrequency20", 3),
          ("ringFrequency25", 1),
          ("ringFrequency30", 4),
          ("ringFrequency50", 2))
    )


_CvaIfFXSRingFrequency_Type.__name__ = "Integer32"
_CvaIfFXSRingFrequency_Object = MibTableColumn
cvaIfFXSRingFrequency = _CvaIfFXSRingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 1, 1, 2),
    _CvaIfFXSRingFrequency_Type()
)
cvaIfFXSRingFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXSRingFrequency.setStatus("current")
_CvaIfFXSStatusTable_Object = MibTable
cvaIfFXSStatusTable = _CvaIfFXSStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cvaIfFXSStatusTable.setStatus("current")
_CvaIfFXSStatusEntry_Object = MibTableRow
cvaIfFXSStatusEntry = _CvaIfFXSStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cvaIfFXSStatusEntry.setStatus("current")


class _CvaIfFXSHookStatus_Type(Integer32):
    """Custom type cvaIfFXSHookStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offHook", 2),
          ("onHook", 1),
          ("trunked", 3))
    )


_CvaIfFXSHookStatus_Type.__name__ = "Integer32"
_CvaIfFXSHookStatus_Object = MibTableColumn
cvaIfFXSHookStatus = _CvaIfFXSHookStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 2, 1, 1),
    _CvaIfFXSHookStatus_Type()
)
cvaIfFXSHookStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfFXSHookStatus.setStatus("current")
_CvaIfFXSRingActive_Type = TruthValue
_CvaIfFXSRingActive_Object = MibTableColumn
cvaIfFXSRingActive = _CvaIfFXSRingActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 2, 1, 2),
    _CvaIfFXSRingActive_Type()
)
cvaIfFXSRingActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfFXSRingActive.setStatus("current")
_CvaIfFXSRingGround_Type = TruthValue
_CvaIfFXSRingGround_Object = MibTableColumn
cvaIfFXSRingGround = _CvaIfFXSRingGround_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 2, 1, 3),
    _CvaIfFXSRingGround_Type()
)
cvaIfFXSRingGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfFXSRingGround.setStatus("current")
_CvaIfFXSTipGround_Type = TruthValue
_CvaIfFXSTipGround_Object = MibTableColumn
cvaIfFXSTipGround = _CvaIfFXSTipGround_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 2, 1, 4),
    _CvaIfFXSTipGround_Type()
)
cvaIfFXSTipGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaIfFXSTipGround.setStatus("current")
_CvaIfFXSTimingTable_Object = MibTable
cvaIfFXSTimingTable = _CvaIfFXSTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cvaIfFXSTimingTable.setStatus("current")
_CvaIfFXSTimingEntry_Object = MibTableRow
cvaIfFXSTimingEntry = _CvaIfFXSTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cvaIfFXSTimingEntry.setStatus("current")


class _CvaIfFXSTimingDigitDuration_Type(Integer32):
    """Custom type cvaIfFXSTimingDigitDuration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CvaIfFXSTimingDigitDuration_Type.__name__ = "Integer32"
_CvaIfFXSTimingDigitDuration_Object = MibTableColumn
cvaIfFXSTimingDigitDuration = _CvaIfFXSTimingDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 3, 1, 1),
    _CvaIfFXSTimingDigitDuration_Type()
)
cvaIfFXSTimingDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXSTimingDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfFXSTimingDigitDuration.setUnits("milliseconds")


class _CvaIfFXSTimingInterDigitDuration_Type(Integer32):
    """Custom type cvaIfFXSTimingInterDigitDuration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CvaIfFXSTimingInterDigitDuration_Type.__name__ = "Integer32"
_CvaIfFXSTimingInterDigitDuration_Object = MibTableColumn
cvaIfFXSTimingInterDigitDuration = _CvaIfFXSTimingInterDigitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 1, 4, 3, 1, 2),
    _CvaIfFXSTimingInterDigitDuration_Type()
)
cvaIfFXSTimingInterDigitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaIfFXSTimingInterDigitDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvaIfFXSTimingInterDigitDuration.setUnits("milliseconds")
_CvaIfMIBConformance_ObjectIdentity = ObjectIdentity
cvaIfMIBConformance = _CvaIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3)
)
_CvaIfMIBCompliances_ObjectIdentity = ObjectIdentity
cvaIfMIBCompliances = _CvaIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 1)
)
_CvaIfMIBGroups_ObjectIdentity = ObjectIdentity
cvaIfMIBGroups = _CvaIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 2)
)
cvaIfCfgEntry.registerAugmentions(
    ("CISCO-VOICE-ANALOG-IF-MIB",
     "cvaIfStatusEntry")
)
cvaIfStatusEntry.setIndexNames(*cvaIfCfgEntry.getIndexNames())
cvaIfEMCfgEntry.registerAugmentions(
    ("CISCO-VOICE-ANALOG-IF-MIB",
     "cvaIfEMStatusEntry")
)
cvaIfEMStatusEntry.setIndexNames(*cvaIfEMCfgEntry.getIndexNames())
cvaIfEMCfgEntry.registerAugmentions(
    ("CISCO-VOICE-ANALOG-IF-MIB",
     "cvaIfEMTimingEntry")
)
cvaIfEMTimingEntry.setIndexNames(*cvaIfEMCfgEntry.getIndexNames())
cvaIfFXOCfgEntry.registerAugmentions(
    ("CISCO-VOICE-ANALOG-IF-MIB",
     "cvaIfFXOStatusEntry")
)
cvaIfFXOStatusEntry.setIndexNames(*cvaIfFXOCfgEntry.getIndexNames())
cvaIfFXOCfgEntry.registerAugmentions(
    ("CISCO-VOICE-ANALOG-IF-MIB",
     "cvaIfFXOTimingEntry")
)
cvaIfFXOTimingEntry.setIndexNames(*cvaIfFXOCfgEntry.getIndexNames())
cvaIfFXSCfgEntry.registerAugmentions(
    ("CISCO-VOICE-ANALOG-IF-MIB",
     "cvaIfFXSStatusEntry")
)
cvaIfFXSStatusEntry.setIndexNames(*cvaIfFXSCfgEntry.getIndexNames())
cvaIfFXSCfgEntry.registerAugmentions(
    ("CISCO-VOICE-ANALOG-IF-MIB",
     "cvaIfFXSTimingEntry")
)
cvaIfFXSTimingEntry.setIndexNames(*cvaIfFXSCfgEntry.getIndexNames())

# Managed Objects groups

cvaIfGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 2, 1)
)
cvaIfGeneralGroup.setObjects(
      *(("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfCfgIntegratedDSP"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfCfgImpedance"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfStatusInfoType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfMaintenanceMode"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfStatusSignalErrors"))
)
if mibBuilder.loadTexts:
    cvaIfGeneralGroup.setStatus("current")

cvaIfEMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 2, 2)
)
cvaIfEMGroup.setObjects(
      *(("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMInSeizureActive"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMOutSeizureActive"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgSignalType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgOperation"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgDialType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingInterDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingPulseRate"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingPulseInterDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingClearWaitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMaxWinkWaitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMaxWinkDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingDelayStart"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMaxDelayDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMinDelayPulseWidth"))
)
if mibBuilder.loadTexts:
    cvaIfEMGroup.setStatus("deprecated")

cvaIfFXOGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 2, 3)
)
cvaIfFXOGroup.setObjects(
      *(("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOHookStatus"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXORingDetect"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXORingGround"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOTipGround"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOCfgSignalType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOCfgNumberRings"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOCfgSupDisconnect"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOCfgDialType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOTimingDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOTimingInterDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOTimingPulseRate"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOTimingPulseInterDigitDuration"))
)
if mibBuilder.loadTexts:
    cvaIfFXOGroup.setStatus("deprecated")

cvaIfFXSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 2, 4)
)
cvaIfFXSGroup.setObjects(
      *(("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXSHookStatus"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXSRingActive"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXSRingGround"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXSTipGround"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXSCfgSignalType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXSRingFrequency"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXSTimingDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXSTimingInterDigitDuration"))
)
if mibBuilder.loadTexts:
    cvaIfFXSGroup.setStatus("current")

cvaIfFXOGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 2, 5)
)
cvaIfFXOGroup2.setObjects(
      *(("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOHookStatus"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXORingDetect"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXORingGround"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOTipGround"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOCfgSignalType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOCfgNumberRings"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOCfgSupDisconnect2"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOCfgDialType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOTimingDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOTimingInterDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOTimingPulseRate"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfFXOTimingPulseInterDigitDuration"))
)
if mibBuilder.loadTexts:
    cvaIfFXOGroup2.setStatus("current")

cvaIfEMGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 2, 6)
)
cvaIfEMGroupRev1.setObjects(
      *(("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMInSeizureActive"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMOutSeizureActive"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgSignalType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgOperation"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgDialType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingInterDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingPulseRate"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingPulseInterDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingClearWaitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMaxWinkWaitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMaxWinkDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingDelayStart"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMaxDelayDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMinDelayPulseWidth"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgLmrMCap"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgLmrECap"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingVoiceHangover"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimeoutLmrTeardown"))
)
if mibBuilder.loadTexts:
    cvaIfEMGroupRev1.setStatus("deprecated")

cvaIfEMGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 2, 7)
)
cvaIfEMGroupRev2.setObjects(
      *(("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMInSeizureActive"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMOutSeizureActive"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgSignalType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgOperation"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgDialType"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingInterDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingPulseRate"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingPulseInterDigitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingClearWaitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMaxWinkWaitDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMaxWinkDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingDelayStart"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMaxDelayDuration"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingMinDelayPulseWidth"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgLmrMCap"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgLmrECap"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingVoiceHangover"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimeoutLmrTeardown"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMCfgAutoGainControl"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimeoutPttXmt"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimeoutPttRcv"),
        ("CISCO-VOICE-ANALOG-IF-MIB", "cvaIfEMTimingDelayVoice"))
)
if mibBuilder.loadTexts:
    cvaIfEMGroupRev2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvaIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cvaIfMIBCompliance.setStatus(
        "deprecated"
    )

cvaIfMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cvaIfMIBCompliance2.setStatus(
        "deprecated"
    )

cvaIfMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 62, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cvaIfMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-ANALOG-IF-MIB",
    **{"InterfaceDialType": InterfaceDialType,
       "ciscoVoiceAnalogIfMIB": ciscoVoiceAnalogIfMIB,
       "cvaIfObjects": cvaIfObjects,
       "cvaIfGeneralObjects": cvaIfGeneralObjects,
       "cvaIfCfgTable": cvaIfCfgTable,
       "cvaIfCfgEntry": cvaIfCfgEntry,
       "cvaIfCfgImpedance": cvaIfCfgImpedance,
       "cvaIfCfgIntegratedDSP": cvaIfCfgIntegratedDSP,
       "cvaIfStatusTable": cvaIfStatusTable,
       "cvaIfStatusEntry": cvaIfStatusEntry,
       "cvaIfStatusInfoType": cvaIfStatusInfoType,
       "cvaIfMaintenanceMode": cvaIfMaintenanceMode,
       "cvaIfStatusSignalErrors": cvaIfStatusSignalErrors,
       "cvaIfEMObjects": cvaIfEMObjects,
       "cvaIfEMCfgTable": cvaIfEMCfgTable,
       "cvaIfEMCfgEntry": cvaIfEMCfgEntry,
       "cvaIfEMCfgSignalType": cvaIfEMCfgSignalType,
       "cvaIfEMCfgOperation": cvaIfEMCfgOperation,
       "cvaIfEMCfgType": cvaIfEMCfgType,
       "cvaIfEMCfgDialType": cvaIfEMCfgDialType,
       "cvaIfEMCfgLmrMCap": cvaIfEMCfgLmrMCap,
       "cvaIfEMCfgLmrECap": cvaIfEMCfgLmrECap,
       "cvaIfEMCfgAutoGainControl": cvaIfEMCfgAutoGainControl,
       "cvaIfEMStatusTable": cvaIfEMStatusTable,
       "cvaIfEMStatusEntry": cvaIfEMStatusEntry,
       "cvaIfEMInSeizureActive": cvaIfEMInSeizureActive,
       "cvaIfEMOutSeizureActive": cvaIfEMOutSeizureActive,
       "cvaIfEMTimingTable": cvaIfEMTimingTable,
       "cvaIfEMTimingEntry": cvaIfEMTimingEntry,
       "cvaIfEMTimingDigitDuration": cvaIfEMTimingDigitDuration,
       "cvaIfEMTimingInterDigitDuration": cvaIfEMTimingInterDigitDuration,
       "cvaIfEMTimingPulseRate": cvaIfEMTimingPulseRate,
       "cvaIfEMTimingPulseInterDigitDuration": cvaIfEMTimingPulseInterDigitDuration,
       "cvaIfEMTimingClearWaitDuration": cvaIfEMTimingClearWaitDuration,
       "cvaIfEMTimingMaxWinkWaitDuration": cvaIfEMTimingMaxWinkWaitDuration,
       "cvaIfEMTimingMaxWinkDuration": cvaIfEMTimingMaxWinkDuration,
       "cvaIfEMTimingDelayStart": cvaIfEMTimingDelayStart,
       "cvaIfEMTimingMaxDelayDuration": cvaIfEMTimingMaxDelayDuration,
       "cvaIfEMTimingMinDelayPulseWidth": cvaIfEMTimingMinDelayPulseWidth,
       "cvaIfEMTimingVoiceHangover": cvaIfEMTimingVoiceHangover,
       "cvaIfEMTimeoutLmrTeardown": cvaIfEMTimeoutLmrTeardown,
       "cvaIfEMTimeoutPttXmt": cvaIfEMTimeoutPttXmt,
       "cvaIfEMTimeoutPttRcv": cvaIfEMTimeoutPttRcv,
       "cvaIfEMTimingDelayVoice": cvaIfEMTimingDelayVoice,
       "cvaIfFXOObjects": cvaIfFXOObjects,
       "cvaIfFXOCfgTable": cvaIfFXOCfgTable,
       "cvaIfFXOCfgEntry": cvaIfFXOCfgEntry,
       "cvaIfFXOCfgSignalType": cvaIfFXOCfgSignalType,
       "cvaIfFXOCfgNumberRings": cvaIfFXOCfgNumberRings,
       "cvaIfFXOCfgSupDisconnect": cvaIfFXOCfgSupDisconnect,
       "cvaIfFXOCfgDialType": cvaIfFXOCfgDialType,
       "cvaIfFXOCfgSupDisconnect2": cvaIfFXOCfgSupDisconnect2,
       "cvaIfFXOStatusTable": cvaIfFXOStatusTable,
       "cvaIfFXOStatusEntry": cvaIfFXOStatusEntry,
       "cvaIfFXOHookStatus": cvaIfFXOHookStatus,
       "cvaIfFXORingDetect": cvaIfFXORingDetect,
       "cvaIfFXORingGround": cvaIfFXORingGround,
       "cvaIfFXOTipGround": cvaIfFXOTipGround,
       "cvaIfFXOTimingTable": cvaIfFXOTimingTable,
       "cvaIfFXOTimingEntry": cvaIfFXOTimingEntry,
       "cvaIfFXOTimingDigitDuration": cvaIfFXOTimingDigitDuration,
       "cvaIfFXOTimingInterDigitDuration": cvaIfFXOTimingInterDigitDuration,
       "cvaIfFXOTimingPulseRate": cvaIfFXOTimingPulseRate,
       "cvaIfFXOTimingPulseInterDigitDuration": cvaIfFXOTimingPulseInterDigitDuration,
       "cvaIfFXSObjects": cvaIfFXSObjects,
       "cvaIfFXSCfgTable": cvaIfFXSCfgTable,
       "cvaIfFXSCfgEntry": cvaIfFXSCfgEntry,
       "cvaIfFXSCfgSignalType": cvaIfFXSCfgSignalType,
       "cvaIfFXSRingFrequency": cvaIfFXSRingFrequency,
       "cvaIfFXSStatusTable": cvaIfFXSStatusTable,
       "cvaIfFXSStatusEntry": cvaIfFXSStatusEntry,
       "cvaIfFXSHookStatus": cvaIfFXSHookStatus,
       "cvaIfFXSRingActive": cvaIfFXSRingActive,
       "cvaIfFXSRingGround": cvaIfFXSRingGround,
       "cvaIfFXSTipGround": cvaIfFXSTipGround,
       "cvaIfFXSTimingTable": cvaIfFXSTimingTable,
       "cvaIfFXSTimingEntry": cvaIfFXSTimingEntry,
       "cvaIfFXSTimingDigitDuration": cvaIfFXSTimingDigitDuration,
       "cvaIfFXSTimingInterDigitDuration": cvaIfFXSTimingInterDigitDuration,
       "cvaIfMIBConformance": cvaIfMIBConformance,
       "cvaIfMIBCompliances": cvaIfMIBCompliances,
       "cvaIfMIBCompliance": cvaIfMIBCompliance,
       "cvaIfMIBCompliance2": cvaIfMIBCompliance2,
       "cvaIfMIBCompliance3": cvaIfMIBCompliance3,
       "cvaIfMIBGroups": cvaIfMIBGroups,
       "cvaIfGeneralGroup": cvaIfGeneralGroup,
       "cvaIfEMGroup": cvaIfEMGroup,
       "cvaIfFXOGroup": cvaIfFXOGroup,
       "cvaIfFXSGroup": cvaIfFXSGroup,
       "cvaIfFXOGroup2": cvaIfFXOGroup2,
       "cvaIfEMGroupRev1": cvaIfEMGroupRev1,
       "cvaIfEMGroupRev2": cvaIfEMGroupRev2}
)
