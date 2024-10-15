# SNMP MIB module (EATON-ATS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EATON-ATS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:18 2024
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

(sts,) = mibBuilder.importSymbols(
    "EATON-OIDS",
    "sts")

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

ats2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2)
)
ats2.setRevisions(
        ("2014-07-31 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UnixTimeStamp(Counter32, TextualConvention):
    status = "current"
    displayHint = "dddddddddd"


# MIB Managed Objects in the order of their OIDs

_Ats2Ident_ObjectIdentity = ObjectIdentity
ats2Ident = _Ats2Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 1)
)


class _Ats2IdentManufacturer_Type(DisplayString):
    """Custom type ats2IdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ats2IdentManufacturer_Type.__name__ = "DisplayString"
_Ats2IdentManufacturer_Object = MibScalar
ats2IdentManufacturer = _Ats2IdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 1),
    _Ats2IdentManufacturer_Type()
)
ats2IdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2IdentManufacturer.setStatus("current")


class _Ats2IdentModel_Type(DisplayString):
    """Custom type ats2IdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ats2IdentModel_Type.__name__ = "DisplayString"
_Ats2IdentModel_Object = MibScalar
ats2IdentModel = _Ats2IdentModel_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 2),
    _Ats2IdentModel_Type()
)
ats2IdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2IdentModel.setStatus("current")


class _Ats2IdentFWVersion_Type(DisplayString):
    """Custom type ats2IdentFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ats2IdentFWVersion_Type.__name__ = "DisplayString"
_Ats2IdentFWVersion_Object = MibScalar
ats2IdentFWVersion = _Ats2IdentFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 3),
    _Ats2IdentFWVersion_Type()
)
ats2IdentFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2IdentFWVersion.setStatus("current")


class _Ats2IdentRelease_Type(DisplayString):
    """Custom type ats2IdentRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ats2IdentRelease_Type.__name__ = "DisplayString"
_Ats2IdentRelease_Object = MibScalar
ats2IdentRelease = _Ats2IdentRelease_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 4),
    _Ats2IdentRelease_Type()
)
ats2IdentRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2IdentRelease.setStatus("current")


class _Ats2IdentSerialNumber_Type(DisplayString):
    """Custom type ats2IdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ats2IdentSerialNumber_Type.__name__ = "DisplayString"
_Ats2IdentSerialNumber_Object = MibScalar
ats2IdentSerialNumber = _Ats2IdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 5),
    _Ats2IdentSerialNumber_Type()
)
ats2IdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2IdentSerialNumber.setStatus("current")


class _Ats2IdentPartNumber_Type(DisplayString):
    """Custom type ats2IdentPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ats2IdentPartNumber_Type.__name__ = "DisplayString"
_Ats2IdentPartNumber_Object = MibScalar
ats2IdentPartNumber = _Ats2IdentPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 6),
    _Ats2IdentPartNumber_Type()
)
ats2IdentPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2IdentPartNumber.setStatus("current")


class _Ats2IdentAgentVersion_Type(DisplayString):
    """Custom type ats2IdentAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ats2IdentAgentVersion_Type.__name__ = "DisplayString"
_Ats2IdentAgentVersion_Object = MibScalar
ats2IdentAgentVersion = _Ats2IdentAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 1, 7),
    _Ats2IdentAgentVersion_Type()
)
ats2IdentAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2IdentAgentVersion.setStatus("current")
_Ats2Measure_ObjectIdentity = ObjectIdentity
ats2Measure = _Ats2Measure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2)
)
_Ats2Input_ObjectIdentity = ObjectIdentity
ats2Input = _Ats2Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 1)
)
_Ats2InputDephasing_Type = Integer32
_Ats2InputDephasing_Object = MibScalar
ats2InputDephasing = _Ats2InputDephasing_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 1, 1),
    _Ats2InputDephasing_Type()
)
ats2InputDephasing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2InputDephasing.setStatus("current")
if mibBuilder.loadTexts:
    ats2InputDephasing.setUnits("degrees")
_Ats2InputTable_Object = MibTable
ats2InputTable = _Ats2InputTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ats2InputTable.setStatus("current")
_Ats2InputEntry_Object = MibTableRow
ats2InputEntry = _Ats2InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 2, 1)
)
ats2InputEntry.setIndexNames(
    (0, "EATON-ATS2-MIB", "ats2InputIndex"),
)
if mibBuilder.loadTexts:
    ats2InputEntry.setStatus("current")


class _Ats2InputIndex_Type(Integer32):
    """Custom type ats2InputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source1", 1),
          ("source2", 2))
    )


_Ats2InputIndex_Type.__name__ = "Integer32"
_Ats2InputIndex_Object = MibTableColumn
ats2InputIndex = _Ats2InputIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 2, 1, 1),
    _Ats2InputIndex_Type()
)
ats2InputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2InputIndex.setStatus("current")
_Ats2InputVoltage_Type = Integer32
_Ats2InputVoltage_Object = MibTableColumn
ats2InputVoltage = _Ats2InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 2, 1, 2),
    _Ats2InputVoltage_Type()
)
ats2InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ats2InputVoltage.setUnits("0.1 V")
_Ats2InputFrequency_Type = Integer32
_Ats2InputFrequency_Object = MibTableColumn
ats2InputFrequency = _Ats2InputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 2, 1, 3),
    _Ats2InputFrequency_Type()
)
ats2InputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2InputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ats2InputFrequency.setUnits("0.1 Hz")
_Ats2Output_ObjectIdentity = ObjectIdentity
ats2Output = _Ats2Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 3)
)
_Ats2OutputVoltage_Type = Integer32
_Ats2OutputVoltage_Object = MibScalar
ats2OutputVoltage = _Ats2OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 3, 1),
    _Ats2OutputVoltage_Type()
)
ats2OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ats2OutputVoltage.setUnits("0.1 V")
_Ats2OutputCurrent_Type = Integer32
_Ats2OutputCurrent_Object = MibScalar
ats2OutputCurrent = _Ats2OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 3, 2),
    _Ats2OutputCurrent_Type()
)
ats2OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ats2OutputCurrent.setUnits("0.1 A")


class _Ats2OperationMode_Type(Integer32):
    """Custom type ats2OperationMode based on Integer32"""
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
        *(("diagnosis", 2),
          ("fault", 7),
          ("initialization", 1),
          ("off", 3),
          ("safe", 6),
          ("source1", 4),
          ("source2", 5))
    )


_Ats2OperationMode_Type.__name__ = "Integer32"
_Ats2OperationMode_Object = MibScalar
ats2OperationMode = _Ats2OperationMode_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 2, 4),
    _Ats2OperationMode_Type()
)
ats2OperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2OperationMode.setStatus("current")
_Ats2Status_ObjectIdentity = ObjectIdentity
ats2Status = _Ats2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3)
)
_Ats2InputStatus_ObjectIdentity = ObjectIdentity
ats2InputStatus = _Ats2InputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 1)
)


class _Ats2InputStatusDephasing_Type(Integer32):
    """Custom type ats2InputStatusDephasing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("outOfRange", 2))
    )


_Ats2InputStatusDephasing_Type.__name__ = "Integer32"
_Ats2InputStatusDephasing_Object = MibScalar
ats2InputStatusDephasing = _Ats2InputStatusDephasing_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 1, 1),
    _Ats2InputStatusDephasing_Type()
)
ats2InputStatusDephasing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2InputStatusDephasing.setStatus("current")
_Ats2InputStatusTable_Object = MibTable
ats2InputStatusTable = _Ats2InputStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ats2InputStatusTable.setStatus("current")
_Ats2InputStatusEntry_Object = MibTableRow
ats2InputStatusEntry = _Ats2InputStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1)
)
ats2InputStatusEntry.setIndexNames(
    (0, "EATON-ATS2-MIB", "ats2InputStatusIndex"),
)
if mibBuilder.loadTexts:
    ats2InputStatusEntry.setStatus("current")


class _Ats2InputStatusIndex_Type(Integer32):
    """Custom type ats2InputStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source1", 1),
          ("source2", 2))
    )


_Ats2InputStatusIndex_Type.__name__ = "Integer32"
_Ats2InputStatusIndex_Object = MibTableColumn
ats2InputStatusIndex = _Ats2InputStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 1),
    _Ats2InputStatusIndex_Type()
)
ats2InputStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2InputStatusIndex.setStatus("current")


class _Ats2InputStatusFrequency_Type(Integer32):
    """Custom type ats2InputStatusFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("outOfRange", 2))
    )


_Ats2InputStatusFrequency_Type.__name__ = "Integer32"
_Ats2InputStatusFrequency_Object = MibTableColumn
ats2InputStatusFrequency = _Ats2InputStatusFrequency_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 2),
    _Ats2InputStatusFrequency_Type()
)
ats2InputStatusFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2InputStatusFrequency.setStatus("current")


class _Ats2InputStatusGood_Type(Integer32):
    """Custom type ats2InputStatusGood based on Integer32"""
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
        *(("voltageAndFreqNormalRange", 2),
          ("voltageAndFreqNormalRangeWaveformNok", 4),
          ("voltageDeratedRangeAndFreqNormalRange", 3),
          ("voltageOrFreqOutofRange", 1))
    )


_Ats2InputStatusGood_Type.__name__ = "Integer32"
_Ats2InputStatusGood_Object = MibTableColumn
ats2InputStatusGood = _Ats2InputStatusGood_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 3),
    _Ats2InputStatusGood_Type()
)
ats2InputStatusGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2InputStatusGood.setStatus("current")


class _Ats2InputStatusInternalFailure_Type(Integer32):
    """Custom type ats2InputStatusInternalFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("internalFailure", 2))
    )


_Ats2InputStatusInternalFailure_Type.__name__ = "Integer32"
_Ats2InputStatusInternalFailure_Object = MibTableColumn
ats2InputStatusInternalFailure = _Ats2InputStatusInternalFailure_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 4),
    _Ats2InputStatusInternalFailure_Type()
)
ats2InputStatusInternalFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2InputStatusInternalFailure.setStatus("current")


class _Ats2InputStatusVoltage_Type(Integer32):
    """Custom type ats2InputStatusVoltage based on Integer32"""
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
        *(("deratedRange", 2),
          ("missing", 4),
          ("normalRange", 1),
          ("outofRange", 3))
    )


_Ats2InputStatusVoltage_Type.__name__ = "Integer32"
_Ats2InputStatusVoltage_Object = MibTableColumn
ats2InputStatusVoltage = _Ats2InputStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 5),
    _Ats2InputStatusVoltage_Type()
)
ats2InputStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2InputStatusVoltage.setStatus("current")


class _Ats2InputStatusUsed_Type(Integer32):
    """Custom type ats2InputStatusUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPoweringLoad", 1),
          ("poweringLoad", 2))
    )


_Ats2InputStatusUsed_Type.__name__ = "Integer32"
_Ats2InputStatusUsed_Object = MibTableColumn
ats2InputStatusUsed = _Ats2InputStatusUsed_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 2, 1, 6),
    _Ats2InputStatusUsed_Type()
)
ats2InputStatusUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2InputStatusUsed.setStatus("current")
_Ats2OutputStatus_ObjectIdentity = ObjectIdentity
ats2OutputStatus = _Ats2OutputStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3)
)


class _Ats2StatusInternalFailure_Type(Integer32):
    """Custom type ats2StatusInternalFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("internalFailure", 2))
    )


_Ats2StatusInternalFailure_Type.__name__ = "Integer32"
_Ats2StatusInternalFailure_Object = MibScalar
ats2StatusInternalFailure = _Ats2StatusInternalFailure_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 1),
    _Ats2StatusInternalFailure_Type()
)
ats2StatusInternalFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2StatusInternalFailure.setStatus("current")


class _Ats2StatusOutput_Type(Integer32):
    """Custom type ats2StatusOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outputNotPowered", 1),
          ("outputPowered", 2))
    )


_Ats2StatusOutput_Type.__name__ = "Integer32"
_Ats2StatusOutput_Object = MibScalar
ats2StatusOutput = _Ats2StatusOutput_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 2),
    _Ats2StatusOutput_Type()
)
ats2StatusOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2StatusOutput.setStatus("current")


class _Ats2StatusOverload_Type(Integer32):
    """Custom type ats2StatusOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("criticalOverload", 3),
          ("noOverload", 1),
          ("warningOverload", 2))
    )


_Ats2StatusOverload_Type.__name__ = "Integer32"
_Ats2StatusOverload_Object = MibScalar
ats2StatusOverload = _Ats2StatusOverload_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 3),
    _Ats2StatusOverload_Type()
)
ats2StatusOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2StatusOverload.setStatus("current")


class _Ats2StatusOverTemperature_Type(Integer32):
    """Custom type ats2StatusOverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOverTemperature", 1),
          ("overTemperature", 2))
    )


_Ats2StatusOverTemperature_Type.__name__ = "Integer32"
_Ats2StatusOverTemperature_Object = MibScalar
ats2StatusOverTemperature = _Ats2StatusOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 4),
    _Ats2StatusOverTemperature_Type()
)
ats2StatusOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2StatusOverTemperature.setStatus("current")


class _Ats2StatusShortCircuit_Type(Integer32):
    """Custom type ats2StatusShortCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noShortCircuit", 1),
          ("shortCircuit", 2))
    )


_Ats2StatusShortCircuit_Type.__name__ = "Integer32"
_Ats2StatusShortCircuit_Object = MibScalar
ats2StatusShortCircuit = _Ats2StatusShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 5),
    _Ats2StatusShortCircuit_Type()
)
ats2StatusShortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2StatusShortCircuit.setStatus("current")


class _Ats2StatusCommunicationLost_Type(Integer32):
    """Custom type ats2StatusCommunicationLost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("communicationLost", 2),
          ("good", 1))
    )


_Ats2StatusCommunicationLost_Type.__name__ = "Integer32"
_Ats2StatusCommunicationLost_Object = MibScalar
ats2StatusCommunicationLost = _Ats2StatusCommunicationLost_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 6),
    _Ats2StatusCommunicationLost_Type()
)
ats2StatusCommunicationLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2StatusCommunicationLost.setStatus("current")


class _Ats2StatusConfigurationFailure_Type(Integer32):
    """Custom type ats2StatusConfigurationFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configurationFailure", 2),
          ("good", 1))
    )


_Ats2StatusConfigurationFailure_Type.__name__ = "Integer32"
_Ats2StatusConfigurationFailure_Object = MibScalar
ats2StatusConfigurationFailure = _Ats2StatusConfigurationFailure_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 3, 3, 7),
    _Ats2StatusConfigurationFailure_Type()
)
ats2StatusConfigurationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2StatusConfigurationFailure.setStatus("current")
_Ats2Config_ObjectIdentity = ObjectIdentity
ats2Config = _Ats2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4)
)
_Ats2ConfigTime_ObjectIdentity = ObjectIdentity
ats2ConfigTime = _Ats2ConfigTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 1)
)
_Ats2ConfigTimeRTC_Type = UnixTimeStamp
_Ats2ConfigTimeRTC_Object = MibScalar
ats2ConfigTimeRTC = _Ats2ConfigTimeRTC_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 1, 1),
    _Ats2ConfigTimeRTC_Type()
)
ats2ConfigTimeRTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats2ConfigTimeRTC.setStatus("current")


class _Ats2ConfigTimeTextDate_Type(DisplayString):
    """Custom type ats2ConfigTimeTextDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Ats2ConfigTimeTextDate_Type.__name__ = "DisplayString"
_Ats2ConfigTimeTextDate_Object = MibScalar
ats2ConfigTimeTextDate = _Ats2ConfigTimeTextDate_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 1, 2),
    _Ats2ConfigTimeTextDate_Type()
)
ats2ConfigTimeTextDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2ConfigTimeTextDate.setStatus("current")


class _Ats2ConfigTimeTextTime_Type(DisplayString):
    """Custom type ats2ConfigTimeTextTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ats2ConfigTimeTextTime_Type.__name__ = "DisplayString"
_Ats2ConfigTimeTextTime_Object = MibScalar
ats2ConfigTimeTextTime = _Ats2ConfigTimeTextTime_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 1, 3),
    _Ats2ConfigTimeTextTime_Type()
)
ats2ConfigTimeTextTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2ConfigTimeTextTime.setStatus("current")
_Ats2ConfigInputVoltageRating_Type = Integer32
_Ats2ConfigInputVoltageRating_Object = MibScalar
ats2ConfigInputVoltageRating = _Ats2ConfigInputVoltageRating_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 2),
    _Ats2ConfigInputVoltageRating_Type()
)
ats2ConfigInputVoltageRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2ConfigInputVoltageRating.setStatus("current")
if mibBuilder.loadTexts:
    ats2ConfigInputVoltageRating.setUnits("1 V")
_Ats2ConfigInputFrequencyRating_Type = Integer32
_Ats2ConfigInputFrequencyRating_Object = MibScalar
ats2ConfigInputFrequencyRating = _Ats2ConfigInputFrequencyRating_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 3),
    _Ats2ConfigInputFrequencyRating_Type()
)
ats2ConfigInputFrequencyRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2ConfigInputFrequencyRating.setStatus("current")
if mibBuilder.loadTexts:
    ats2ConfigInputFrequencyRating.setUnits("Hz")
_Ats2ConfigOutputVoltage_Type = Integer32
_Ats2ConfigOutputVoltage_Object = MibScalar
ats2ConfigOutputVoltage = _Ats2ConfigOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 4),
    _Ats2ConfigOutputVoltage_Type()
)
ats2ConfigOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats2ConfigOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ats2ConfigOutputVoltage.setUnits("1 V")


class _Ats2ConfigPreferred_Type(Integer32):
    """Custom type ats2ConfigPreferred based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source1", 1),
          ("source2", 2))
    )


_Ats2ConfigPreferred_Type.__name__ = "Integer32"
_Ats2ConfigPreferred_Object = MibScalar
ats2ConfigPreferred = _Ats2ConfigPreferred_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 5),
    _Ats2ConfigPreferred_Type()
)
ats2ConfigPreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats2ConfigPreferred.setStatus("current")


class _Ats2ConfigSensitivity_Type(Integer32):
    """Custom type ats2ConfigSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highSensitivity", 2),
          ("lowSensitivity", 3),
          ("normal", 1))
    )


_Ats2ConfigSensitivity_Type.__name__ = "Integer32"
_Ats2ConfigSensitivity_Object = MibScalar
ats2ConfigSensitivity = _Ats2ConfigSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 6),
    _Ats2ConfigSensitivity_Type()
)
ats2ConfigSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats2ConfigSensitivity.setStatus("current")


class _Ats2ConfigTransferMode_Type(Integer32):
    """Custom type ats2ConfigTransferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gap", 2),
          ("standard", 1))
    )


_Ats2ConfigTransferMode_Type.__name__ = "Integer32"
_Ats2ConfigTransferMode_Object = MibScalar
ats2ConfigTransferMode = _Ats2ConfigTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 7),
    _Ats2ConfigTransferMode_Type()
)
ats2ConfigTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats2ConfigTransferMode.setStatus("current")


class _Ats2ConfigTransferTest_Type(Integer32):
    """Custom type ats2ConfigTransferTest based on Integer32"""
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
        *(("aborted", 4),
          ("doneAndError", 3),
          ("doneAndPassed", 1),
          ("doneAndWarning", 2),
          ("inProgress", 5),
          ("noTestInitiated", 6))
    )


_Ats2ConfigTransferTest_Type.__name__ = "Integer32"
_Ats2ConfigTransferTest_Object = MibScalar
ats2ConfigTransferTest = _Ats2ConfigTransferTest_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 8),
    _Ats2ConfigTransferTest_Type()
)
ats2ConfigTransferTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2ConfigTransferTest.setStatus("current")
_Ats2ConfigBrownoutLow_Type = Integer32
_Ats2ConfigBrownoutLow_Object = MibScalar
ats2ConfigBrownoutLow = _Ats2ConfigBrownoutLow_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 9),
    _Ats2ConfigBrownoutLow_Type()
)
ats2ConfigBrownoutLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2ConfigBrownoutLow.setStatus("current")
if mibBuilder.loadTexts:
    ats2ConfigBrownoutLow.setUnits("1 V")
_Ats2ConfigBrownoutLowDerated_Type = Integer32
_Ats2ConfigBrownoutLowDerated_Object = MibScalar
ats2ConfigBrownoutLowDerated = _Ats2ConfigBrownoutLowDerated_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 10),
    _Ats2ConfigBrownoutLowDerated_Type()
)
ats2ConfigBrownoutLowDerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2ConfigBrownoutLowDerated.setStatus("current")
if mibBuilder.loadTexts:
    ats2ConfigBrownoutLowDerated.setUnits("1 V")
_Ats2ConfigBrownoutHigh_Type = Integer32
_Ats2ConfigBrownoutHigh_Object = MibScalar
ats2ConfigBrownoutHigh = _Ats2ConfigBrownoutHigh_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 11),
    _Ats2ConfigBrownoutHigh_Type()
)
ats2ConfigBrownoutHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2ConfigBrownoutHigh.setStatus("current")
if mibBuilder.loadTexts:
    ats2ConfigBrownoutHigh.setUnits("1 V")
_Ats2ConfigHysteresisVoltage_Type = Integer32
_Ats2ConfigHysteresisVoltage_Object = MibScalar
ats2ConfigHysteresisVoltage = _Ats2ConfigHysteresisVoltage_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 4, 12),
    _Ats2ConfigHysteresisVoltage_Type()
)
ats2ConfigHysteresisVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2ConfigHysteresisVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ats2ConfigHysteresisVoltage.setUnits("1 V")
_Ats2Environment_ObjectIdentity = ObjectIdentity
ats2Environment = _Ats2Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5)
)


class _Ats2EnvRemoteTemp_Type(Integer32):
    """Custom type ats2EnvRemoteTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_Ats2EnvRemoteTemp_Type.__name__ = "Integer32"
_Ats2EnvRemoteTemp_Object = MibScalar
ats2EnvRemoteTemp = _Ats2EnvRemoteTemp_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 1),
    _Ats2EnvRemoteTemp_Type()
)
ats2EnvRemoteTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2EnvRemoteTemp.setStatus("current")
if mibBuilder.loadTexts:
    ats2EnvRemoteTemp.setUnits("degrees Centigrade")


class _Ats2EnvRemoteHumidity_Type(Integer32):
    """Custom type ats2EnvRemoteHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ats2EnvRemoteHumidity_Type.__name__ = "Integer32"
_Ats2EnvRemoteHumidity_Object = MibScalar
ats2EnvRemoteHumidity = _Ats2EnvRemoteHumidity_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 2),
    _Ats2EnvRemoteHumidity_Type()
)
ats2EnvRemoteHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2EnvRemoteHumidity.setStatus("current")
if mibBuilder.loadTexts:
    ats2EnvRemoteHumidity.setUnits("percent")


class _Ats2EnvNumContacts_Type(Integer32):
    """Custom type ats2EnvNumContacts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Ats2EnvNumContacts_Type.__name__ = "Integer32"
_Ats2EnvNumContacts_Object = MibScalar
ats2EnvNumContacts = _Ats2EnvNumContacts_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 3),
    _Ats2EnvNumContacts_Type()
)
ats2EnvNumContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2EnvNumContacts.setStatus("current")
_Ats2ContactSenseTable_Object = MibTable
ats2ContactSenseTable = _Ats2ContactSenseTable_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4)
)
if mibBuilder.loadTexts:
    ats2ContactSenseTable.setStatus("current")
_Ats2ContactsTableEntry_Object = MibTableRow
ats2ContactsTableEntry = _Ats2ContactsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4, 1)
)
ats2ContactsTableEntry.setIndexNames(
    (0, "EATON-ATS2-MIB", "ats2ContactIndex"),
)
if mibBuilder.loadTexts:
    ats2ContactsTableEntry.setStatus("current")


class _Ats2ContactIndex_Type(Integer32):
    """Custom type ats2ContactIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Ats2ContactIndex_Type.__name__ = "Integer32"
_Ats2ContactIndex_Object = MibTableColumn
ats2ContactIndex = _Ats2ContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4, 1, 1),
    _Ats2ContactIndex_Type()
)
ats2ContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2ContactIndex.setStatus("current")


class _Ats2ContactType_Type(Integer32):
    """Custom type ats2ContactType based on Integer32"""
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
        *(("anyChange", 3),
          ("normallyClosed", 2),
          ("normallyOpen", 1),
          ("notUsed", 4))
    )


_Ats2ContactType_Type.__name__ = "Integer32"
_Ats2ContactType_Object = MibTableColumn
ats2ContactType = _Ats2ContactType_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4, 1, 2),
    _Ats2ContactType_Type()
)
ats2ContactType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats2ContactType.setStatus("current")


class _Ats2ContactState_Type(Integer32):
    """Custom type ats2ContactState based on Integer32"""
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
        *(("closed", 2),
          ("closedWithNotice", 4),
          ("open", 1),
          ("openWithNotice", 3))
    )


_Ats2ContactState_Type.__name__ = "Integer32"
_Ats2ContactState_Object = MibTableColumn
ats2ContactState = _Ats2ContactState_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4, 1, 3),
    _Ats2ContactState_Type()
)
ats2ContactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats2ContactState.setStatus("current")


class _Ats2ContactDescr_Type(DisplayString):
    """Custom type ats2ContactDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Ats2ContactDescr_Type.__name__ = "DisplayString"
_Ats2ContactDescr_Object = MibTableColumn
ats2ContactDescr = _Ats2ContactDescr_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 4, 1, 4),
    _Ats2ContactDescr_Type()
)
ats2ContactDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats2ContactDescr.setStatus("current")


class _Ats2EnvRemoteTempLowerLimit_Type(Integer32):
    """Custom type ats2EnvRemoteTempLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_Ats2EnvRemoteTempLowerLimit_Type.__name__ = "Integer32"
_Ats2EnvRemoteTempLowerLimit_Object = MibScalar
ats2EnvRemoteTempLowerLimit = _Ats2EnvRemoteTempLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 5),
    _Ats2EnvRemoteTempLowerLimit_Type()
)
ats2EnvRemoteTempLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats2EnvRemoteTempLowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    ats2EnvRemoteTempLowerLimit.setUnits("degrees Centigrade")


class _Ats2EnvRemoteTempUpperLimit_Type(Integer32):
    """Custom type ats2EnvRemoteTempUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_Ats2EnvRemoteTempUpperLimit_Type.__name__ = "Integer32"
_Ats2EnvRemoteTempUpperLimit_Object = MibScalar
ats2EnvRemoteTempUpperLimit = _Ats2EnvRemoteTempUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 6),
    _Ats2EnvRemoteTempUpperLimit_Type()
)
ats2EnvRemoteTempUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats2EnvRemoteTempUpperLimit.setStatus("current")
if mibBuilder.loadTexts:
    ats2EnvRemoteTempUpperLimit.setUnits("degrees Centigrade")


class _Ats2EnvRemoteHumidityLowerLimit_Type(Integer32):
    """Custom type ats2EnvRemoteHumidityLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ats2EnvRemoteHumidityLowerLimit_Type.__name__ = "Integer32"
_Ats2EnvRemoteHumidityLowerLimit_Object = MibScalar
ats2EnvRemoteHumidityLowerLimit = _Ats2EnvRemoteHumidityLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 7),
    _Ats2EnvRemoteHumidityLowerLimit_Type()
)
ats2EnvRemoteHumidityLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats2EnvRemoteHumidityLowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    ats2EnvRemoteHumidityLowerLimit.setUnits("percent")


class _Ats2EnvRemoteHumidityUpperLimit_Type(Integer32):
    """Custom type ats2EnvRemoteHumidityUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ats2EnvRemoteHumidityUpperLimit_Type.__name__ = "Integer32"
_Ats2EnvRemoteHumidityUpperLimit_Object = MibScalar
ats2EnvRemoteHumidityUpperLimit = _Ats2EnvRemoteHumidityUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 5, 8),
    _Ats2EnvRemoteHumidityUpperLimit_Type()
)
ats2EnvRemoteHumidityUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats2EnvRemoteHumidityUpperLimit.setStatus("current")
if mibBuilder.loadTexts:
    ats2EnvRemoteHumidityUpperLimit.setUnits("percent")
_Ats2Traps_ObjectIdentity = ObjectIdentity
ats2Traps = _Ats2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10)
)

# Managed Objects groups


# Notification objects

ats2TrapCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 1)
)
if mibBuilder.loadTexts:
    ats2TrapCommunicationLost.setStatus(
        "current"
    )

ats2TrapCommunicationRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 2)
)
if mibBuilder.loadTexts:
    ats2TrapCommunicationRecovered.setStatus(
        "current"
    )

ats2TrapOutputPowered = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 3)
)
if mibBuilder.loadTexts:
    ats2TrapOutputPowered.setStatus(
        "current"
    )

ats2TrapOutputNotPowered = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 4)
)
if mibBuilder.loadTexts:
    ats2TrapOutputNotPowered.setStatus(
        "current"
    )

ats2TrapOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 5)
)
if mibBuilder.loadTexts:
    ats2TrapOverload.setStatus(
        "current"
    )

ats2TrapNoOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 6)
)
if mibBuilder.loadTexts:
    ats2TrapNoOverLoad.setStatus(
        "current"
    )

ats2TrapInternalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 7)
)
if mibBuilder.loadTexts:
    ats2TrapInternalFailure.setStatus(
        "current"
    )

ats2TrapNoInternalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 8)
)
if mibBuilder.loadTexts:
    ats2TrapNoInternalFailure.setStatus(
        "current"
    )

ats2TrapSource1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 9)
)
if mibBuilder.loadTexts:
    ats2TrapSource1Normal.setStatus(
        "current"
    )

ats2TrapSource1OutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 10)
)
if mibBuilder.loadTexts:
    ats2TrapSource1OutOfRange.setStatus(
        "current"
    )

ats2TrapSource2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 11)
)
if mibBuilder.loadTexts:
    ats2TrapSource2Normal.setStatus(
        "current"
    )

ats2TrapSource2OutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 12)
)
if mibBuilder.loadTexts:
    ats2TrapSource2OutOfRange.setStatus(
        "current"
    )

ats2TrapSourceDesynchronized = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 13)
)
if mibBuilder.loadTexts:
    ats2TrapSourceDesynchronized.setStatus(
        "current"
    )

ats2TrapSourceSynchronized = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 14)
)
if mibBuilder.loadTexts:
    ats2TrapSourceSynchronized.setStatus(
        "current"
    )

ats2TrapOutputPoweredBySource1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 15)
)
if mibBuilder.loadTexts:
    ats2TrapOutputPoweredBySource1.setStatus(
        "current"
    )

ats2TrapOutputPoweredBySource2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 16)
)
if mibBuilder.loadTexts:
    ats2TrapOutputPoweredBySource2.setStatus(
        "current"
    )

ats2TrapRemoteTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 20)
)
if mibBuilder.loadTexts:
    ats2TrapRemoteTempLow.setStatus(
        "current"
    )

ats2TrapRemoteTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 21)
)
if mibBuilder.loadTexts:
    ats2TrapRemoteTempHigh.setStatus(
        "current"
    )

ats2TrapRemoteTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 22)
)
if mibBuilder.loadTexts:
    ats2TrapRemoteTempNormal.setStatus(
        "current"
    )

ats2TrapRemoteHumidityLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 23)
)
if mibBuilder.loadTexts:
    ats2TrapRemoteHumidityLow.setStatus(
        "current"
    )

ats2TrapRemoteHumidityHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 24)
)
if mibBuilder.loadTexts:
    ats2TrapRemoteHumidityHigh.setStatus(
        "current"
    )

ats2TrapRemoteHumidityNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 25)
)
if mibBuilder.loadTexts:
    ats2TrapRemoteHumidityNormal.setStatus(
        "current"
    )

ats2Contact1ActiveNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 26)
)
if mibBuilder.loadTexts:
    ats2Contact1ActiveNotice.setStatus(
        "current"
    )

ats2Contact1InactiveNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 27)
)
if mibBuilder.loadTexts:
    ats2Contact1InactiveNotice.setStatus(
        "current"
    )

ats2Contact2ActiveNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 28)
)
if mibBuilder.loadTexts:
    ats2Contact2ActiveNotice.setStatus(
        "current"
    )

ats2Contact2InactiveNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 29)
)
if mibBuilder.loadTexts:
    ats2Contact2InactiveNotice.setStatus(
        "current"
    )

ats2TestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 534, 10, 2, 10, 40)
)
if mibBuilder.loadTexts:
    ats2TestTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EATON-ATS2-MIB",
    **{"UnixTimeStamp": UnixTimeStamp,
       "ats2": ats2,
       "ats2Ident": ats2Ident,
       "ats2IdentManufacturer": ats2IdentManufacturer,
       "ats2IdentModel": ats2IdentModel,
       "ats2IdentFWVersion": ats2IdentFWVersion,
       "ats2IdentRelease": ats2IdentRelease,
       "ats2IdentSerialNumber": ats2IdentSerialNumber,
       "ats2IdentPartNumber": ats2IdentPartNumber,
       "ats2IdentAgentVersion": ats2IdentAgentVersion,
       "ats2Measure": ats2Measure,
       "ats2Input": ats2Input,
       "ats2InputDephasing": ats2InputDephasing,
       "ats2InputTable": ats2InputTable,
       "ats2InputEntry": ats2InputEntry,
       "ats2InputIndex": ats2InputIndex,
       "ats2InputVoltage": ats2InputVoltage,
       "ats2InputFrequency": ats2InputFrequency,
       "ats2Output": ats2Output,
       "ats2OutputVoltage": ats2OutputVoltage,
       "ats2OutputCurrent": ats2OutputCurrent,
       "ats2OperationMode": ats2OperationMode,
       "ats2Status": ats2Status,
       "ats2InputStatus": ats2InputStatus,
       "ats2InputStatusDephasing": ats2InputStatusDephasing,
       "ats2InputStatusTable": ats2InputStatusTable,
       "ats2InputStatusEntry": ats2InputStatusEntry,
       "ats2InputStatusIndex": ats2InputStatusIndex,
       "ats2InputStatusFrequency": ats2InputStatusFrequency,
       "ats2InputStatusGood": ats2InputStatusGood,
       "ats2InputStatusInternalFailure": ats2InputStatusInternalFailure,
       "ats2InputStatusVoltage": ats2InputStatusVoltage,
       "ats2InputStatusUsed": ats2InputStatusUsed,
       "ats2OutputStatus": ats2OutputStatus,
       "ats2StatusInternalFailure": ats2StatusInternalFailure,
       "ats2StatusOutput": ats2StatusOutput,
       "ats2StatusOverload": ats2StatusOverload,
       "ats2StatusOverTemperature": ats2StatusOverTemperature,
       "ats2StatusShortCircuit": ats2StatusShortCircuit,
       "ats2StatusCommunicationLost": ats2StatusCommunicationLost,
       "ats2StatusConfigurationFailure": ats2StatusConfigurationFailure,
       "ats2Config": ats2Config,
       "ats2ConfigTime": ats2ConfigTime,
       "ats2ConfigTimeRTC": ats2ConfigTimeRTC,
       "ats2ConfigTimeTextDate": ats2ConfigTimeTextDate,
       "ats2ConfigTimeTextTime": ats2ConfigTimeTextTime,
       "ats2ConfigInputVoltageRating": ats2ConfigInputVoltageRating,
       "ats2ConfigInputFrequencyRating": ats2ConfigInputFrequencyRating,
       "ats2ConfigOutputVoltage": ats2ConfigOutputVoltage,
       "ats2ConfigPreferred": ats2ConfigPreferred,
       "ats2ConfigSensitivity": ats2ConfigSensitivity,
       "ats2ConfigTransferMode": ats2ConfigTransferMode,
       "ats2ConfigTransferTest": ats2ConfigTransferTest,
       "ats2ConfigBrownoutLow": ats2ConfigBrownoutLow,
       "ats2ConfigBrownoutLowDerated": ats2ConfigBrownoutLowDerated,
       "ats2ConfigBrownoutHigh": ats2ConfigBrownoutHigh,
       "ats2ConfigHysteresisVoltage": ats2ConfigHysteresisVoltage,
       "ats2Environment": ats2Environment,
       "ats2EnvRemoteTemp": ats2EnvRemoteTemp,
       "ats2EnvRemoteHumidity": ats2EnvRemoteHumidity,
       "ats2EnvNumContacts": ats2EnvNumContacts,
       "ats2ContactSenseTable": ats2ContactSenseTable,
       "ats2ContactsTableEntry": ats2ContactsTableEntry,
       "ats2ContactIndex": ats2ContactIndex,
       "ats2ContactType": ats2ContactType,
       "ats2ContactState": ats2ContactState,
       "ats2ContactDescr": ats2ContactDescr,
       "ats2EnvRemoteTempLowerLimit": ats2EnvRemoteTempLowerLimit,
       "ats2EnvRemoteTempUpperLimit": ats2EnvRemoteTempUpperLimit,
       "ats2EnvRemoteHumidityLowerLimit": ats2EnvRemoteHumidityLowerLimit,
       "ats2EnvRemoteHumidityUpperLimit": ats2EnvRemoteHumidityUpperLimit,
       "ats2Traps": ats2Traps,
       "ats2TrapCommunicationLost": ats2TrapCommunicationLost,
       "ats2TrapCommunicationRecovered": ats2TrapCommunicationRecovered,
       "ats2TrapOutputPowered": ats2TrapOutputPowered,
       "ats2TrapOutputNotPowered": ats2TrapOutputNotPowered,
       "ats2TrapOverload": ats2TrapOverload,
       "ats2TrapNoOverLoad": ats2TrapNoOverLoad,
       "ats2TrapInternalFailure": ats2TrapInternalFailure,
       "ats2TrapNoInternalFailure": ats2TrapNoInternalFailure,
       "ats2TrapSource1Normal": ats2TrapSource1Normal,
       "ats2TrapSource1OutOfRange": ats2TrapSource1OutOfRange,
       "ats2TrapSource2Normal": ats2TrapSource2Normal,
       "ats2TrapSource2OutOfRange": ats2TrapSource2OutOfRange,
       "ats2TrapSourceDesynchronized": ats2TrapSourceDesynchronized,
       "ats2TrapSourceSynchronized": ats2TrapSourceSynchronized,
       "ats2TrapOutputPoweredBySource1": ats2TrapOutputPoweredBySource1,
       "ats2TrapOutputPoweredBySource2": ats2TrapOutputPoweredBySource2,
       "ats2TrapRemoteTempLow": ats2TrapRemoteTempLow,
       "ats2TrapRemoteTempHigh": ats2TrapRemoteTempHigh,
       "ats2TrapRemoteTempNormal": ats2TrapRemoteTempNormal,
       "ats2TrapRemoteHumidityLow": ats2TrapRemoteHumidityLow,
       "ats2TrapRemoteHumidityHigh": ats2TrapRemoteHumidityHigh,
       "ats2TrapRemoteHumidityNormal": ats2TrapRemoteHumidityNormal,
       "ats2Contact1ActiveNotice": ats2Contact1ActiveNotice,
       "ats2Contact1InactiveNotice": ats2Contact1InactiveNotice,
       "ats2Contact2ActiveNotice": ats2Contact2ActiveNotice,
       "ats2Contact2InactiveNotice": ats2Contact2InactiveNotice,
       "ats2TestTrap": ats2TestTrap}
)
