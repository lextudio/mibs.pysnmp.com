# SNMP MIB module (EPPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EPPC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:54 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(NonNegativeInteger,
 PositiveInteger) = mibBuilder.importSymbols(
    "UPS-MIB",
    "NonNegativeInteger",
    "PositiveInteger")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ppc_ObjectIdentity = ObjectIdentity
ppc = _Ppc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10)
)
_UpsAgent_ObjectIdentity = ObjectIdentity
upsAgent = _UpsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1)
)
_UpsE_ObjectIdentity = ObjectIdentity
upsE = _UpsE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1)
)
_UpsEIdentity_ObjectIdentity = ObjectIdentity
upsEIdentity = _UpsEIdentity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 1)
)


class _UpsEIdentityManufacturer_Type(DisplayString):
    """Custom type upsEIdentityManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsEIdentityManufacturer_Type.__name__ = "DisplayString"
_UpsEIdentityManufacturer_Object = MibScalar
upsEIdentityManufacturer = _UpsEIdentityManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 1, 1),
    _UpsEIdentityManufacturer_Type()
)
upsEIdentityManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEIdentityManufacturer.setStatus("mandatory")


class _UpsEIdentityModel_Type(DisplayString):
    """Custom type upsEIdentityModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsEIdentityModel_Type.__name__ = "DisplayString"
_UpsEIdentityModel_Object = MibScalar
upsEIdentityModel = _UpsEIdentityModel_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 1, 2),
    _UpsEIdentityModel_Type()
)
upsEIdentityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEIdentityModel.setStatus("mandatory")


class _UpsEIdentityUPSFirmwareVerison_Type(DisplayString):
    """Custom type upsEIdentityUPSFirmwareVerison based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsEIdentityUPSFirmwareVerison_Type.__name__ = "DisplayString"
_UpsEIdentityUPSFirmwareVerison_Object = MibScalar
upsEIdentityUPSFirmwareVerison = _UpsEIdentityUPSFirmwareVerison_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 1, 3),
    _UpsEIdentityUPSFirmwareVerison_Type()
)
upsEIdentityUPSFirmwareVerison.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEIdentityUPSFirmwareVerison.setStatus("mandatory")


class _UpsEIndentityUPSSerialNumber_Type(DisplayString):
    """Custom type upsEIndentityUPSSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsEIndentityUPSSerialNumber_Type.__name__ = "DisplayString"
_UpsEIndentityUPSSerialNumber_Object = MibScalar
upsEIndentityUPSSerialNumber = _UpsEIndentityUPSSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 1, 4),
    _UpsEIndentityUPSSerialNumber_Type()
)
upsEIndentityUPSSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEIndentityUPSSerialNumber.setStatus("mandatory")


class _UpsEIdentityDescription_Type(DisplayString):
    """Custom type upsEIdentityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsEIdentityDescription_Type.__name__ = "DisplayString"
_UpsEIdentityDescription_Object = MibScalar
upsEIdentityDescription = _UpsEIdentityDescription_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 1, 5),
    _UpsEIdentityDescription_Type()
)
upsEIdentityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEIdentityDescription.setStatus("mandatory")


class _UpsEIdentityAgentSoftwareVerison_Type(DisplayString):
    """Custom type upsEIdentityAgentSoftwareVerison based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsEIdentityAgentSoftwareVerison_Type.__name__ = "DisplayString"
_UpsEIdentityAgentSoftwareVerison_Object = MibScalar
upsEIdentityAgentSoftwareVerison = _UpsEIdentityAgentSoftwareVerison_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 1, 6),
    _UpsEIdentityAgentSoftwareVerison_Type()
)
upsEIdentityAgentSoftwareVerison.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEIdentityAgentSoftwareVerison.setStatus("mandatory")


class _UpsEIdentityAttachedDevices_Type(DisplayString):
    """Custom type upsEIdentityAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsEIdentityAttachedDevices_Type.__name__ = "DisplayString"
_UpsEIdentityAttachedDevices_Object = MibScalar
upsEIdentityAttachedDevices = _UpsEIdentityAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 1, 7),
    _UpsEIdentityAttachedDevices_Type()
)
upsEIdentityAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEIdentityAttachedDevices.setStatus("mandatory")
_UpsESystemSummary_ObjectIdentity = ObjectIdentity
upsESystemSummary = _UpsESystemSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2)
)


class _UpsESystemStatus_Type(Integer32):
    """Custom type upsESystemStatus based on Integer32"""
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
        *(("battery", 5),
          ("battery-test", 6),
          ("by-pass", 3),
          ("converter", 8),
          ("eco", 9),
          ("fault", 7),
          ("line", 4),
          ("on-booster", 11),
          ("on-reducer", 12),
          ("other", 13),
          ("power-on", 1),
          ("shutdown", 10),
          ("stand-by", 2))
    )


_UpsESystemStatus_Type.__name__ = "Integer32"
_UpsESystemStatus_Object = MibScalar
upsESystemStatus = _UpsESystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 1),
    _UpsESystemStatus_Type()
)
upsESystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemStatus.setStatus("mandatory")
_UpsESystemTemperature_Type = Integer32
_UpsESystemTemperature_Object = MibScalar
upsESystemTemperature = _UpsESystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 2),
    _UpsESystemTemperature_Type()
)
upsESystemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemTemperature.setStatus("mandatory")


class _UpsESystemWarningCode_Type(DisplayString):
    """Custom type upsESystemWarningCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UpsESystemWarningCode_Type.__name__ = "DisplayString"
_UpsESystemWarningCode_Object = MibScalar
upsESystemWarningCode = _UpsESystemWarningCode_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 3),
    _UpsESystemWarningCode_Type()
)
upsESystemWarningCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemWarningCode.setStatus("mandatory")


class _UpsESystemFaultCode_Type(DisplayString):
    """Custom type upsESystemFaultCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UpsESystemFaultCode_Type.__name__ = "DisplayString"
_UpsESystemFaultCode_Object = MibScalar
upsESystemFaultCode = _UpsESystemFaultCode_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 4),
    _UpsESystemFaultCode_Type()
)
upsESystemFaultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemFaultCode.setStatus("mandatory")
_UpsESystemConfigInputVoltage_Type = NonNegativeInteger
_UpsESystemConfigInputVoltage_Object = MibScalar
upsESystemConfigInputVoltage = _UpsESystemConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 5),
    _UpsESystemConfigInputVoltage_Type()
)
upsESystemConfigInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemConfigInputVoltage.setStatus("mandatory")
_UpsESystemConfigInputFrequence_Type = NonNegativeInteger
_UpsESystemConfigInputFrequence_Object = MibScalar
upsESystemConfigInputFrequence = _UpsESystemConfigInputFrequence_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 6),
    _UpsESystemConfigInputFrequence_Type()
)
upsESystemConfigInputFrequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemConfigInputFrequence.setStatus("mandatory")
_UpsESystemConfigOutputVoltage_Type = NonNegativeInteger
_UpsESystemConfigOutputVoltage_Object = MibScalar
upsESystemConfigOutputVoltage = _UpsESystemConfigOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 7),
    _UpsESystemConfigOutputVoltage_Type()
)
upsESystemConfigOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemConfigOutputVoltage.setStatus("mandatory")
_UpsESystemConfigOutputFrequency_Type = NonNegativeInteger
_UpsESystemConfigOutputFrequency_Object = MibScalar
upsESystemConfigOutputFrequency = _UpsESystemConfigOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 8),
    _UpsESystemConfigOutputFrequency_Type()
)
upsESystemConfigOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemConfigOutputFrequency.setStatus("mandatory")
_UpsESystemConfigOutputVA_Type = NonNegativeInteger
_UpsESystemConfigOutputVA_Object = MibScalar
upsESystemConfigOutputVA = _UpsESystemConfigOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 9),
    _UpsESystemConfigOutputVA_Type()
)
upsESystemConfigOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemConfigOutputVA.setStatus("mandatory")
_UpsESystemConfigOutputPower_Type = NonNegativeInteger
_UpsESystemConfigOutputPower_Object = MibScalar
upsESystemConfigOutputPower = _UpsESystemConfigOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 10),
    _UpsESystemConfigOutputPower_Type()
)
upsESystemConfigOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemConfigOutputPower.setStatus("mandatory")
_UpsESystemConfigOutputLoadHighSetPoint_Type = NonNegativeInteger
_UpsESystemConfigOutputLoadHighSetPoint_Object = MibScalar
upsESystemConfigOutputLoadHighSetPoint = _UpsESystemConfigOutputLoadHighSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 11),
    _UpsESystemConfigOutputLoadHighSetPoint_Type()
)
upsESystemConfigOutputLoadHighSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsESystemConfigOutputLoadHighSetPoint.setStatus("mandatory")
_UpsESystemConfigOverTemperatureSetPoint_Type = NonNegativeInteger
_UpsESystemConfigOverTemperatureSetPoint_Object = MibScalar
upsESystemConfigOverTemperatureSetPoint = _UpsESystemConfigOverTemperatureSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 12),
    _UpsESystemConfigOverTemperatureSetPoint_Type()
)
upsESystemConfigOverTemperatureSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsESystemConfigOverTemperatureSetPoint.setStatus("mandatory")
_UpsESystemInputSourceNum_Type = Integer32
_UpsESystemInputSourceNum_Object = MibScalar
upsESystemInputSourceNum = _UpsESystemInputSourceNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 13),
    _UpsESystemInputSourceNum_Type()
)
upsESystemInputSourceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemInputSourceNum.setStatus("mandatory")
_UpsESystemInputLineBads_Type = Counter32
_UpsESystemInputLineBads_Object = MibScalar
upsESystemInputLineBads = _UpsESystemInputLineBads_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 14),
    _UpsESystemInputLineBads_Type()
)
upsESystemInputLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemInputLineBads.setStatus("mandatory")


class _UpsESystemInputNumPhases_Type(PositiveInteger):
    """Custom type upsESystemInputNumPhases based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_UpsESystemInputNumPhases_Type.__name__ = "PositiveInteger"
_UpsESystemInputNumPhases_Object = MibScalar
upsESystemInputNumPhases = _UpsESystemInputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 15),
    _UpsESystemInputNumPhases_Type()
)
upsESystemInputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemInputNumPhases.setStatus("mandatory")
_UpsESystemInputTable_Object = MibTable
upsESystemInputTable = _UpsESystemInputTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 16)
)
if mibBuilder.loadTexts:
    upsESystemInputTable.setStatus("mandatory")
_UpsESystemInputEntry_Object = MibTableRow
upsESystemInputEntry = _UpsESystemInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 16, 1)
)
upsESystemInputEntry.setIndexNames(
    (0, "EPPC-MIB", "upsESystemInputPhase"),
)
if mibBuilder.loadTexts:
    upsESystemInputEntry.setStatus("mandatory")


class _UpsESystemInputPhase_Type(PositiveInteger):
    """Custom type upsESystemInputPhase based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_UpsESystemInputPhase_Type.__name__ = "PositiveInteger"
_UpsESystemInputPhase_Object = MibTableColumn
upsESystemInputPhase = _UpsESystemInputPhase_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 16, 1, 1),
    _UpsESystemInputPhase_Type()
)
upsESystemInputPhase.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsESystemInputPhase.setStatus("mandatory")
_UpsESystemInputFrequency_Type = NonNegativeInteger
_UpsESystemInputFrequency_Object = MibTableColumn
upsESystemInputFrequency = _UpsESystemInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 16, 1, 2),
    _UpsESystemInputFrequency_Type()
)
upsESystemInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemInputFrequency.setStatus("mandatory")
_UpsESystemInputVoltage_Type = NonNegativeInteger
_UpsESystemInputVoltage_Object = MibTableColumn
upsESystemInputVoltage = _UpsESystemInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 16, 1, 3),
    _UpsESystemInputVoltage_Type()
)
upsESystemInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemInputVoltage.setStatus("mandatory")
_UpsESystemInputCurrent_Type = NonNegativeInteger
_UpsESystemInputCurrent_Object = MibTableColumn
upsESystemInputCurrent = _UpsESystemInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 16, 1, 4),
    _UpsESystemInputCurrent_Type()
)
upsESystemInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemInputCurrent.setStatus("mandatory")
_UpsESystemInputWatts_Type = NonNegativeInteger
_UpsESystemInputWatts_Object = MibTableColumn
upsESystemInputWatts = _UpsESystemInputWatts_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 16, 1, 5),
    _UpsESystemInputWatts_Type()
)
upsESystemInputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemInputWatts.setStatus("mandatory")


class _UpsESystemOutputNumPhase_Type(PositiveInteger):
    """Custom type upsESystemOutputNumPhase based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_UpsESystemOutputNumPhase_Type.__name__ = "PositiveInteger"
_UpsESystemOutputNumPhase_Object = MibScalar
upsESystemOutputNumPhase = _UpsESystemOutputNumPhase_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 17),
    _UpsESystemOutputNumPhase_Type()
)
upsESystemOutputNumPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemOutputNumPhase.setStatus("mandatory")
_UpsESystemOutputTable_Object = MibTable
upsESystemOutputTable = _UpsESystemOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 18)
)
if mibBuilder.loadTexts:
    upsESystemOutputTable.setStatus("mandatory")
_UpsESystemOutputEntry_Object = MibTableRow
upsESystemOutputEntry = _UpsESystemOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 18, 1)
)
upsESystemOutputEntry.setIndexNames(
    (0, "EPPC-MIB", "upsESystemOutputPhase"),
)
if mibBuilder.loadTexts:
    upsESystemOutputEntry.setStatus("mandatory")


class _UpsESystemOutputPhase_Type(PositiveInteger):
    """Custom type upsESystemOutputPhase based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_UpsESystemOutputPhase_Type.__name__ = "PositiveInteger"
_UpsESystemOutputPhase_Object = MibTableColumn
upsESystemOutputPhase = _UpsESystemOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 18, 1, 1),
    _UpsESystemOutputPhase_Type()
)
upsESystemOutputPhase.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsESystemOutputPhase.setStatus("mandatory")
_UpsESystemOutputFrequency_Type = NonNegativeInteger
_UpsESystemOutputFrequency_Object = MibTableColumn
upsESystemOutputFrequency = _UpsESystemOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 18, 1, 2),
    _UpsESystemOutputFrequency_Type()
)
upsESystemOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemOutputFrequency.setStatus("mandatory")
_UpsESystemOutputVoltage_Type = NonNegativeInteger
_UpsESystemOutputVoltage_Object = MibTableColumn
upsESystemOutputVoltage = _UpsESystemOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 18, 1, 3),
    _UpsESystemOutputVoltage_Type()
)
upsESystemOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemOutputVoltage.setStatus("mandatory")
_UpsESystemOutputCurrent_Type = NonNegativeInteger
_UpsESystemOutputCurrent_Object = MibTableColumn
upsESystemOutputCurrent = _UpsESystemOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 18, 1, 4),
    _UpsESystemOutputCurrent_Type()
)
upsESystemOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemOutputCurrent.setStatus("mandatory")
_UpsESystemOutputWatts_Type = NonNegativeInteger
_UpsESystemOutputWatts_Object = MibTableColumn
upsESystemOutputWatts = _UpsESystemOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 18, 1, 5),
    _UpsESystemOutputWatts_Type()
)
upsESystemOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemOutputWatts.setStatus("mandatory")
_UpsESystemOutputVA_Type = NonNegativeInteger
_UpsESystemOutputVA_Object = MibTableColumn
upsESystemOutputVA = _UpsESystemOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 18, 1, 6),
    _UpsESystemOutputVA_Type()
)
upsESystemOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemOutputVA.setStatus("mandatory")
_UpsESystemOutputLoad_Type = NonNegativeInteger
_UpsESystemOutputLoad_Object = MibTableColumn
upsESystemOutputLoad = _UpsESystemOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 18, 1, 7),
    _UpsESystemOutputLoad_Type()
)
upsESystemOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemOutputLoad.setStatus("mandatory")


class _UpsESystemBypassNumPhase_Type(PositiveInteger):
    """Custom type upsESystemBypassNumPhase based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_UpsESystemBypassNumPhase_Type.__name__ = "PositiveInteger"
_UpsESystemBypassNumPhase_Object = MibScalar
upsESystemBypassNumPhase = _UpsESystemBypassNumPhase_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 19),
    _UpsESystemBypassNumPhase_Type()
)
upsESystemBypassNumPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemBypassNumPhase.setStatus("mandatory")
_UpsESystemBypassTable_Object = MibTable
upsESystemBypassTable = _UpsESystemBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 20)
)
if mibBuilder.loadTexts:
    upsESystemBypassTable.setStatus("mandatory")
_UpsESystemBypassEntry_Object = MibTableRow
upsESystemBypassEntry = _UpsESystemBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 20, 1)
)
upsESystemBypassEntry.setIndexNames(
    (0, "EPPC-MIB", "upsESystemBypassPhase"),
)
if mibBuilder.loadTexts:
    upsESystemBypassEntry.setStatus("mandatory")


class _UpsESystemBypassPhase_Type(PositiveInteger):
    """Custom type upsESystemBypassPhase based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_UpsESystemBypassPhase_Type.__name__ = "PositiveInteger"
_UpsESystemBypassPhase_Object = MibTableColumn
upsESystemBypassPhase = _UpsESystemBypassPhase_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 20, 1, 1),
    _UpsESystemBypassPhase_Type()
)
upsESystemBypassPhase.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsESystemBypassPhase.setStatus("mandatory")
_UpsESystemBypassFrequency_Type = NonNegativeInteger
_UpsESystemBypassFrequency_Object = MibTableColumn
upsESystemBypassFrequency = _UpsESystemBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 20, 1, 2),
    _UpsESystemBypassFrequency_Type()
)
upsESystemBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemBypassFrequency.setStatus("mandatory")
_UpsESystemBypassVoltage_Type = NonNegativeInteger
_UpsESystemBypassVoltage_Object = MibTableColumn
upsESystemBypassVoltage = _UpsESystemBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 20, 1, 3),
    _UpsESystemBypassVoltage_Type()
)
upsESystemBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemBypassVoltage.setStatus("mandatory")
_UpsESystemBypassCurrent_Type = NonNegativeInteger
_UpsESystemBypassCurrent_Object = MibTableColumn
upsESystemBypassCurrent = _UpsESystemBypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 20, 1, 4),
    _UpsESystemBypassCurrent_Type()
)
upsESystemBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemBypassCurrent.setStatus("mandatory")
_UpsESystemBypassWatts_Type = NonNegativeInteger
_UpsESystemBypassWatts_Object = MibTableColumn
upsESystemBypassWatts = _UpsESystemBypassWatts_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 20, 1, 5),
    _UpsESystemBypassWatts_Type()
)
upsESystemBypassWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemBypassWatts.setStatus("mandatory")
_UpsESystemConfigBelowCapacityLimit_Type = NonNegativeInteger
_UpsESystemConfigBelowCapacityLimit_Object = MibScalar
upsESystemConfigBelowCapacityLimit = _UpsESystemConfigBelowCapacityLimit_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 21),
    _UpsESystemConfigBelowCapacityLimit_Type()
)
upsESystemConfigBelowCapacityLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsESystemConfigBelowCapacityLimit.setStatus("mandatory")
_UpsESystemConfigBelowRemainTimeLimit_Type = NonNegativeInteger
_UpsESystemConfigBelowRemainTimeLimit_Object = MibScalar
upsESystemConfigBelowRemainTimeLimit = _UpsESystemConfigBelowRemainTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 2, 22),
    _UpsESystemConfigBelowRemainTimeLimit_Type()
)
upsESystemConfigBelowRemainTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsESystemConfigBelowRemainTimeLimit.setStatus("mandatory")
_UpsEBatterySystem_ObjectIdentity = ObjectIdentity
upsEBatterySystem = _UpsEBatterySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3)
)


class _UpsEBatteryStatus_Type(Integer32):
    """Custom type upsEBatteryStatus based on Integer32"""
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
        *(("batteryDepleted", 4),
          ("batteryDischarging", 5),
          ("batteryFailure", 6),
          ("batteryLow", 3),
          ("batteryNormal", 2),
          ("unknown", 1))
    )


_UpsEBatteryStatus_Type.__name__ = "Integer32"
_UpsEBatteryStatus_Object = MibScalar
upsEBatteryStatus = _UpsEBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 1),
    _UpsEBatteryStatus_Type()
)
upsEBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEBatteryStatus.setStatus("mandatory")
_UpsESecondsOnBattery_Type = NonNegativeInteger
_UpsESecondsOnBattery_Object = MibScalar
upsESecondsOnBattery = _UpsESecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 2),
    _UpsESecondsOnBattery_Type()
)
upsESecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESecondsOnBattery.setStatus("mandatory")
_UpsEBatteryEstimatedMinutesRemaining_Type = PositiveInteger
_UpsEBatteryEstimatedMinutesRemaining_Object = MibScalar
upsEBatteryEstimatedMinutesRemaining = _UpsEBatteryEstimatedMinutesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 3),
    _UpsEBatteryEstimatedMinutesRemaining_Type()
)
upsEBatteryEstimatedMinutesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEBatteryEstimatedMinutesRemaining.setStatus("mandatory")


class _UpsEBatteryEstimatedChargeRemaining_Type(Integer32):
    """Custom type upsEBatteryEstimatedChargeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEBatteryEstimatedChargeRemaining_Type.__name__ = "Integer32"
_UpsEBatteryEstimatedChargeRemaining_Object = MibScalar
upsEBatteryEstimatedChargeRemaining = _UpsEBatteryEstimatedChargeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 4),
    _UpsEBatteryEstimatedChargeRemaining_Type()
)
upsEBatteryEstimatedChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEBatteryEstimatedChargeRemaining.setStatus("mandatory")
_UpsEPositiveBatteryVoltage_Type = NonNegativeInteger
_UpsEPositiveBatteryVoltage_Object = MibScalar
upsEPositiveBatteryVoltage = _UpsEPositiveBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 5),
    _UpsEPositiveBatteryVoltage_Type()
)
upsEPositiveBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEPositiveBatteryVoltage.setStatus("mandatory")
_UpsENegativeBatteryVoltage_Type = NonNegativeInteger
_UpsENegativeBatteryVoltage_Object = MibScalar
upsENegativeBatteryVoltage = _UpsENegativeBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 6),
    _UpsENegativeBatteryVoltage_Type()
)
upsENegativeBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsENegativeBatteryVoltage.setStatus("mandatory")
_UpsEBatteryCellNumber_Type = NonNegativeInteger
_UpsEBatteryCellNumber_Object = MibScalar
upsEBatteryCellNumber = _UpsEBatteryCellNumber_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 7),
    _UpsEBatteryCellNumber_Type()
)
upsEBatteryCellNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEBatteryCellNumber.setStatus("mandatory")
_UpsEBatteryTemperature_Type = Integer32
_UpsEBatteryTemperature_Object = MibScalar
upsEBatteryTemperature = _UpsEBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 8),
    _UpsEBatteryTemperature_Type()
)
upsEBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEBatteryTemperature.setStatus("mandatory")


class _UpsEBatteryLastReplacedDate_Type(DisplayString):
    """Custom type upsEBatteryLastReplacedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpsEBatteryLastReplacedDate_Type.__name__ = "DisplayString"
_UpsEBatteryLastReplacedDate_Object = MibScalar
upsEBatteryLastReplacedDate = _UpsEBatteryLastReplacedDate_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 9),
    _UpsEBatteryLastReplacedDate_Type()
)
upsEBatteryLastReplacedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEBatteryLastReplacedDate.setStatus("mandatory")


class _UpsEBatteryABMStatus_Type(Integer32):
    """Custom type upsEBatteryABMStatus based on Integer32"""
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
        *(("charge", 1),
          ("disable", 5),
          ("discharge", 4),
          ("float", 2),
          ("rest", 3))
    )


_UpsEBatteryABMStatus_Type.__name__ = "Integer32"
_UpsEBatteryABMStatus_Object = MibScalar
upsEBatteryABMStatus = _UpsEBatteryABMStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 10),
    _UpsEBatteryABMStatus_Type()
)
upsEBatteryABMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEBatteryABMStatus.setStatus("mandatory")


class _UpsEChargerModulesNum_Type(NonNegativeInteger):
    """Custom type upsEChargerModulesNum based on NonNegativeInteger"""
    subtypeSpec = NonNegativeInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UpsEChargerModulesNum_Type.__name__ = "NonNegativeInteger"
_UpsEChargerModulesNum_Object = MibScalar
upsEChargerModulesNum = _UpsEChargerModulesNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 11),
    _UpsEChargerModulesNum_Type()
)
upsEChargerModulesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEChargerModulesNum.setStatus("mandatory")
_UpsEChargerModulesTable_Object = MibTable
upsEChargerModulesTable = _UpsEChargerModulesTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 12)
)
if mibBuilder.loadTexts:
    upsEChargerModulesTable.setStatus("mandatory")
_UpsEChargerModulesEntry_Object = MibTableRow
upsEChargerModulesEntry = _UpsEChargerModulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 12, 1)
)
upsEChargerModulesEntry.setIndexNames(
    (0, "EPPC-MIB", "chargerModulesNum"),
)
if mibBuilder.loadTexts:
    upsEChargerModulesEntry.setStatus("mandatory")


class _ChargerModulesNum_Type(PositiveInteger):
    """Custom type chargerModulesNum based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ChargerModulesNum_Type.__name__ = "PositiveInteger"
_ChargerModulesNum_Object = MibTableColumn
chargerModulesNum = _ChargerModulesNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 12, 1, 1),
    _ChargerModulesNum_Type()
)
chargerModulesNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chargerModulesNum.setStatus("mandatory")
_ChargerModulesAddress_Type = NonNegativeInteger
_ChargerModulesAddress_Object = MibTableColumn
chargerModulesAddress = _ChargerModulesAddress_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 12, 1, 2),
    _ChargerModulesAddress_Type()
)
chargerModulesAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargerModulesAddress.setStatus("mandatory")
_PositiveChargeVotlage_Type = NonNegativeInteger
_PositiveChargeVotlage_Object = MibTableColumn
positiveChargeVotlage = _PositiveChargeVotlage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 12, 1, 3),
    _PositiveChargeVotlage_Type()
)
positiveChargeVotlage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    positiveChargeVotlage.setStatus("mandatory")
_NegativeChargeVoltage_Type = NonNegativeInteger
_NegativeChargeVoltage_Object = MibTableColumn
negativeChargeVoltage = _NegativeChargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 12, 1, 4),
    _NegativeChargeVoltage_Type()
)
negativeChargeVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    negativeChargeVoltage.setStatus("mandatory")
_PositiveChargeCurrent_Type = NonNegativeInteger
_PositiveChargeCurrent_Object = MibTableColumn
positiveChargeCurrent = _PositiveChargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 12, 1, 5),
    _PositiveChargeCurrent_Type()
)
positiveChargeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    positiveChargeCurrent.setStatus("mandatory")
_NegativeChargeCurrent_Type = NonNegativeInteger
_NegativeChargeCurrent_Object = MibTableColumn
negativeChargeCurrent = _NegativeChargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 12, 1, 6),
    _NegativeChargeCurrent_Type()
)
negativeChargeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    negativeChargeCurrent.setStatus("mandatory")
_ChargerModulesTemperature_Type = Integer32
_ChargerModulesTemperature_Object = MibTableColumn
chargerModulesTemperature = _ChargerModulesTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 12, 1, 7),
    _ChargerModulesTemperature_Type()
)
chargerModulesTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargerModulesTemperature.setStatus("mandatory")


class _ChargerModulesMode_Type(Integer32):
    """Custom type chargerModulesMode based on Integer32"""
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
        *(("fault", 3),
          ("powerOn", 1),
          ("running", 5),
          ("shutdown", 4),
          ("standyby", 2),
          ("suicide", 6),
          ("unknown", 7))
    )


_ChargerModulesMode_Type.__name__ = "Integer32"
_ChargerModulesMode_Object = MibTableColumn
chargerModulesMode = _ChargerModulesMode_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 3, 12, 1, 8),
    _ChargerModulesMode_Type()
)
chargerModulesMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargerModulesMode.setStatus("mandatory")
_UpsEPowerConverterSystem_ObjectIdentity = ObjectIdentity
upsEPowerConverterSystem = _UpsEPowerConverterSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4)
)


class _UpsEUPSModulesNum_Type(NonNegativeInteger):
    """Custom type upsEUPSModulesNum based on NonNegativeInteger"""
    subtypeSpec = NonNegativeInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UpsEUPSModulesNum_Type.__name__ = "NonNegativeInteger"
_UpsEUPSModulesNum_Object = MibScalar
upsEUPSModulesNum = _UpsEUPSModulesNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 1),
    _UpsEUPSModulesNum_Type()
)
upsEUPSModulesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEUPSModulesNum.setStatus("mandatory")
_UpsEModulesTable_Object = MibTable
upsEModulesTable = _UpsEModulesTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    upsEModulesTable.setStatus("mandatory")
_UpsEModulesEntry_Object = MibTableRow
upsEModulesEntry = _UpsEModulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1)
)
upsEModulesEntry.setIndexNames(
    (0, "EPPC-MIB", "upsEModulesNum"),
)
if mibBuilder.loadTexts:
    upsEModulesEntry.setStatus("mandatory")


class _UpsEModulesNum_Type(PositiveInteger):
    """Custom type upsEModulesNum based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_UpsEModulesNum_Type.__name__ = "PositiveInteger"
_UpsEModulesNum_Object = MibTableColumn
upsEModulesNum = _UpsEModulesNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 1),
    _UpsEModulesNum_Type()
)
upsEModulesNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEModulesNum.setStatus("mandatory")
_UpsEModuleAddress_Type = Integer32
_UpsEModuleAddress_Object = MibTableColumn
upsEModuleAddress = _UpsEModuleAddress_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 2),
    _UpsEModuleAddress_Type()
)
upsEModuleAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleAddress.setStatus("mandatory")
_UpsEModulePositiveBusVolt_Type = NonNegativeInteger
_UpsEModulePositiveBusVolt_Object = MibTableColumn
upsEModulePositiveBusVolt = _UpsEModulePositiveBusVolt_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 3),
    _UpsEModulePositiveBusVolt_Type()
)
upsEModulePositiveBusVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModulePositiveBusVolt.setStatus("mandatory")
_UpsEModuleNegativeBusVolt_Type = NonNegativeInteger
_UpsEModuleNegativeBusVolt_Object = MibTableColumn
upsEModuleNegativeBusVolt = _UpsEModuleNegativeBusVolt_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 4),
    _UpsEModuleNegativeBusVolt_Type()
)
upsEModuleNegativeBusVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleNegativeBusVolt.setStatus("mandatory")
_UpsEModuleTemperature_Type = Integer32
_UpsEModuleTemperature_Object = MibTableColumn
upsEModuleTemperature = _UpsEModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 5),
    _UpsEModuleTemperature_Type()
)
upsEModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleTemperature.setStatus("mandatory")


class _UpsEModuleWorkingMode_Type(Integer32):
    """Custom type upsEModuleWorkingMode based on Integer32"""
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
        *(("battery", 5),
          ("battery-test", 6),
          ("by-pass", 3),
          ("converter", 8),
          ("eco", 9),
          ("fault", 7),
          ("line", 4),
          ("on-booster", 11),
          ("on-reducer", 12),
          ("other", 13),
          ("power-on", 1),
          ("shutdown", 10),
          ("stand-by", 2))
    )


_UpsEModuleWorkingMode_Type.__name__ = "Integer32"
_UpsEModuleWorkingMode_Object = MibTableColumn
upsEModuleWorkingMode = _UpsEModuleWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 6),
    _UpsEModuleWorkingMode_Type()
)
upsEModuleWorkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleWorkingMode.setStatus("mandatory")
_UpsEModuleOutputCurrentR_Type = NonNegativeInteger
_UpsEModuleOutputCurrentR_Object = MibTableColumn
upsEModuleOutputCurrentR = _UpsEModuleOutputCurrentR_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 7),
    _UpsEModuleOutputCurrentR_Type()
)
upsEModuleOutputCurrentR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputCurrentR.setStatus("mandatory")
_UpsEModuleOutputWattR_Type = NonNegativeInteger
_UpsEModuleOutputWattR_Object = MibTableColumn
upsEModuleOutputWattR = _UpsEModuleOutputWattR_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 8),
    _UpsEModuleOutputWattR_Type()
)
upsEModuleOutputWattR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputWattR.setStatus("mandatory")
_UpsEModuleOutputLoadR_Type = Integer32
_UpsEModuleOutputLoadR_Object = MibTableColumn
upsEModuleOutputLoadR = _UpsEModuleOutputLoadR_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 9),
    _UpsEModuleOutputLoadR_Type()
)
upsEModuleOutputLoadR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputLoadR.setStatus("mandatory")


class _UpsEModuleWarningCode_Type(DisplayString):
    """Custom type upsEModuleWarningCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UpsEModuleWarningCode_Type.__name__ = "DisplayString"
_UpsEModuleWarningCode_Object = MibTableColumn
upsEModuleWarningCode = _UpsEModuleWarningCode_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 10),
    _UpsEModuleWarningCode_Type()
)
upsEModuleWarningCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleWarningCode.setStatus("mandatory")


class _UpsEModuleFaultCode_Type(DisplayString):
    """Custom type upsEModuleFaultCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UpsEModuleFaultCode_Type.__name__ = "DisplayString"
_UpsEModuleFaultCode_Object = MibTableColumn
upsEModuleFaultCode = _UpsEModuleFaultCode_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 11),
    _UpsEModuleFaultCode_Type()
)
upsEModuleFaultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleFaultCode.setStatus("mandatory")


class _UpsEModuleTrapState_Type(DisplayString):
    """Custom type upsEModuleTrapState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UpsEModuleTrapState_Type.__name__ = "DisplayString"
_UpsEModuleTrapState_Object = MibTableColumn
upsEModuleTrapState = _UpsEModuleTrapState_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 12),
    _UpsEModuleTrapState_Type()
)
upsEModuleTrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleTrapState.setStatus("mandatory")
_UpsEModuleConfigOutputVA_Type = NonNegativeInteger
_UpsEModuleConfigOutputVA_Object = MibTableColumn
upsEModuleConfigOutputVA = _UpsEModuleConfigOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 13),
    _UpsEModuleConfigOutputVA_Type()
)
upsEModuleConfigOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleConfigOutputVA.setStatus("mandatory")
_UpsEModuleOutputCurrentS_Type = NonNegativeInteger
_UpsEModuleOutputCurrentS_Object = MibTableColumn
upsEModuleOutputCurrentS = _UpsEModuleOutputCurrentS_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 14),
    _UpsEModuleOutputCurrentS_Type()
)
upsEModuleOutputCurrentS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputCurrentS.setStatus("mandatory")
_UpsEModuleOutputCurrentT_Type = NonNegativeInteger
_UpsEModuleOutputCurrentT_Object = MibTableColumn
upsEModuleOutputCurrentT = _UpsEModuleOutputCurrentT_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 15),
    _UpsEModuleOutputCurrentT_Type()
)
upsEModuleOutputCurrentT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputCurrentT.setStatus("mandatory")
_UpsEModuleOutputWattS_Type = NonNegativeInteger
_UpsEModuleOutputWattS_Object = MibTableColumn
upsEModuleOutputWattS = _UpsEModuleOutputWattS_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 16),
    _UpsEModuleOutputWattS_Type()
)
upsEModuleOutputWattS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputWattS.setStatus("mandatory")
_UpsEModuleOutputWattT_Type = NonNegativeInteger
_UpsEModuleOutputWattT_Object = MibTableColumn
upsEModuleOutputWattT = _UpsEModuleOutputWattT_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 17),
    _UpsEModuleOutputWattT_Type()
)
upsEModuleOutputWattT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputWattT.setStatus("mandatory")
_UpsEModuleOutputLoadS_Type = Integer32
_UpsEModuleOutputLoadS_Object = MibTableColumn
upsEModuleOutputLoadS = _UpsEModuleOutputLoadS_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 18),
    _UpsEModuleOutputLoadS_Type()
)
upsEModuleOutputLoadS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputLoadS.setStatus("mandatory")
_UpsEModuleOutputLoadT_Type = Integer32
_UpsEModuleOutputLoadT_Object = MibTableColumn
upsEModuleOutputLoadT = _UpsEModuleOutputLoadT_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 19),
    _UpsEModuleOutputLoadT_Type()
)
upsEModuleOutputLoadT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputLoadT.setStatus("mandatory")
_UpsEModuleOutputVAR_Type = NonNegativeInteger
_UpsEModuleOutputVAR_Object = MibTableColumn
upsEModuleOutputVAR = _UpsEModuleOutputVAR_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 20),
    _UpsEModuleOutputVAR_Type()
)
upsEModuleOutputVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputVAR.setStatus("mandatory")
_UpsEModuleOutputVAS_Type = NonNegativeInteger
_UpsEModuleOutputVAS_Object = MibTableColumn
upsEModuleOutputVAS = _UpsEModuleOutputVAS_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 21),
    _UpsEModuleOutputVAS_Type()
)
upsEModuleOutputVAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputVAS.setStatus("mandatory")
_UpsEModuleOutputVAT_Type = NonNegativeInteger
_UpsEModuleOutputVAT_Object = MibTableColumn
upsEModuleOutputVAT = _UpsEModuleOutputVAT_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 4, 2, 1, 22),
    _UpsEModuleOutputVAT_Type()
)
upsEModuleOutputVAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEModuleOutputVAT.setStatus("mandatory")
_UpsELoadSegment_ObjectIdentity = ObjectIdentity
upsELoadSegment = _UpsELoadSegment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 5)
)
_UpsELoadSegment1OffDelay_Type = Integer32
_UpsELoadSegment1OffDelay_Object = MibScalar
upsELoadSegment1OffDelay = _UpsELoadSegment1OffDelay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 5, 1),
    _UpsELoadSegment1OffDelay_Type()
)
upsELoadSegment1OffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsELoadSegment1OffDelay.setStatus("mandatory")
_UpsELoadSegment1OnDelay_Type = Integer32
_UpsELoadSegment1OnDelay_Object = MibScalar
upsELoadSegment1OnDelay = _UpsELoadSegment1OnDelay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 5, 2),
    _UpsELoadSegment1OnDelay_Type()
)
upsELoadSegment1OnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsELoadSegment1OnDelay.setStatus("mandatory")
_UpsELoadSegment1AutoOffTimer_Type = Integer32
_UpsELoadSegment1AutoOffTimer_Object = MibScalar
upsELoadSegment1AutoOffTimer = _UpsELoadSegment1AutoOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 5, 3),
    _UpsELoadSegment1AutoOffTimer_Type()
)
upsELoadSegment1AutoOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsELoadSegment1AutoOffTimer.setStatus("mandatory")
_UpsELoadSegment1AutoOnTimer_Type = Integer32
_UpsELoadSegment1AutoOnTimer_Object = MibScalar
upsELoadSegment1AutoOnTimer = _UpsELoadSegment1AutoOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 5, 4),
    _UpsELoadSegment1AutoOnTimer_Type()
)
upsELoadSegment1AutoOnTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsELoadSegment1AutoOnTimer.setStatus("mandatory")


class _UpsELoadSegment1State_Type(Integer32):
    """Custom type upsELoadSegment1State based on Integer32"""
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
        *(("not-support", 5),
          ("off", 1),
          ("off-pending", 3),
          ("on", 2),
          ("on-pending", 4))
    )


_UpsELoadSegment1State_Type.__name__ = "Integer32"
_UpsELoadSegment1State_Object = MibScalar
upsELoadSegment1State = _UpsELoadSegment1State_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 5, 5),
    _UpsELoadSegment1State_Type()
)
upsELoadSegment1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsELoadSegment1State.setStatus("mandatory")
_UpsELoadSegment2OffDelay_Type = Integer32
_UpsELoadSegment2OffDelay_Object = MibScalar
upsELoadSegment2OffDelay = _UpsELoadSegment2OffDelay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 5, 6),
    _UpsELoadSegment2OffDelay_Type()
)
upsELoadSegment2OffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsELoadSegment2OffDelay.setStatus("mandatory")
_UpsELoadSegment2OnDelay_Type = Integer32
_UpsELoadSegment2OnDelay_Object = MibScalar
upsELoadSegment2OnDelay = _UpsELoadSegment2OnDelay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 5, 7),
    _UpsELoadSegment2OnDelay_Type()
)
upsELoadSegment2OnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsELoadSegment2OnDelay.setStatus("mandatory")
_UpsELoadSegment2AutoOffTimer_Type = Integer32
_UpsELoadSegment2AutoOffTimer_Object = MibScalar
upsELoadSegment2AutoOffTimer = _UpsELoadSegment2AutoOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 5, 8),
    _UpsELoadSegment2AutoOffTimer_Type()
)
upsELoadSegment2AutoOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsELoadSegment2AutoOffTimer.setStatus("mandatory")
_UpsELoadSegment2AutoOnTimer_Type = Integer32
_UpsELoadSegment2AutoOnTimer_Object = MibScalar
upsELoadSegment2AutoOnTimer = _UpsELoadSegment2AutoOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 5, 9),
    _UpsELoadSegment2AutoOnTimer_Type()
)
upsELoadSegment2AutoOnTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsELoadSegment2AutoOnTimer.setStatus("mandatory")


class _UpsELoadSegment2State_Type(Integer32):
    """Custom type upsELoadSegment2State based on Integer32"""
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
        *(("not-support", 5),
          ("off", 1),
          ("off-pending", 3),
          ("on", 2),
          ("on-pending", 4))
    )


_UpsELoadSegment2State_Type.__name__ = "Integer32"
_UpsELoadSegment2State_Object = MibScalar
upsELoadSegment2State = _UpsELoadSegment2State_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 5, 10),
    _UpsELoadSegment2State_Type()
)
upsELoadSegment2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsELoadSegment2State.setStatus("mandatory")
_UpsEEnvironment_ObjectIdentity = ObjectIdentity
upsEEnvironment = _UpsEEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6)
)
_UpsEEnvironmentTemperature_ObjectIdentity = ObjectIdentity
upsEEnvironmentTemperature = _UpsEEnvironmentTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 1)
)
_UpsEEnvironmentCurrentTemperature_Type = Integer32
_UpsEEnvironmentCurrentTemperature_Object = MibScalar
upsEEnvironmentCurrentTemperature = _UpsEEnvironmentCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 1, 1),
    _UpsEEnvironmentCurrentTemperature_Type()
)
upsEEnvironmentCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEEnvironmentCurrentTemperature.setStatus("mandatory")
_UpsEEnvironmentTemperatureHighSetPoint_Type = Integer32
_UpsEEnvironmentTemperatureHighSetPoint_Object = MibScalar
upsEEnvironmentTemperatureHighSetPoint = _UpsEEnvironmentTemperatureHighSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 1, 2),
    _UpsEEnvironmentTemperatureHighSetPoint_Type()
)
upsEEnvironmentTemperatureHighSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentTemperatureHighSetPoint.setStatus("mandatory")


class _UpsEEnvironmentTemperatureHighStatus_Type(Integer32):
    """Custom type upsEEnvironmentTemperatureHighStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsEEnvironmentTemperatureHighStatus_Type.__name__ = "Integer32"
_UpsEEnvironmentTemperatureHighStatus_Object = MibScalar
upsEEnvironmentTemperatureHighStatus = _UpsEEnvironmentTemperatureHighStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 1, 3),
    _UpsEEnvironmentTemperatureHighStatus_Type()
)
upsEEnvironmentTemperatureHighStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentTemperatureHighStatus.setStatus("mandatory")
_UpsEEnvironmentTemperatureLowSetPoint_Type = Integer32
_UpsEEnvironmentTemperatureLowSetPoint_Object = MibScalar
upsEEnvironmentTemperatureLowSetPoint = _UpsEEnvironmentTemperatureLowSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 1, 4),
    _UpsEEnvironmentTemperatureLowSetPoint_Type()
)
upsEEnvironmentTemperatureLowSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentTemperatureLowSetPoint.setStatus("mandatory")


class _UpsEEnvironmentTemperatureLowStatus_Type(Integer32):
    """Custom type upsEEnvironmentTemperatureLowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsEEnvironmentTemperatureLowStatus_Type.__name__ = "Integer32"
_UpsEEnvironmentTemperatureLowStatus_Object = MibScalar
upsEEnvironmentTemperatureLowStatus = _UpsEEnvironmentTemperatureLowStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 1, 5),
    _UpsEEnvironmentTemperatureLowStatus_Type()
)
upsEEnvironmentTemperatureLowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentTemperatureLowStatus.setStatus("mandatory")
_UpsEEnvironmentTemperatureOffset_Type = Integer32
_UpsEEnvironmentTemperatureOffset_Object = MibScalar
upsEEnvironmentTemperatureOffset = _UpsEEnvironmentTemperatureOffset_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 1, 6),
    _UpsEEnvironmentTemperatureOffset_Type()
)
upsEEnvironmentTemperatureOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentTemperatureOffset.setStatus("mandatory")
_UpsEEnvironmentHumidity_ObjectIdentity = ObjectIdentity
upsEEnvironmentHumidity = _UpsEEnvironmentHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 2)
)
_UpsEEnvironmentCurrentHumidity_Type = Integer32
_UpsEEnvironmentCurrentHumidity_Object = MibScalar
upsEEnvironmentCurrentHumidity = _UpsEEnvironmentCurrentHumidity_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 2, 1),
    _UpsEEnvironmentCurrentHumidity_Type()
)
upsEEnvironmentCurrentHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEEnvironmentCurrentHumidity.setStatus("mandatory")
_UpsEEnvironmentHumidityHighSetPoint_Type = Integer32
_UpsEEnvironmentHumidityHighSetPoint_Object = MibScalar
upsEEnvironmentHumidityHighSetPoint = _UpsEEnvironmentHumidityHighSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 2, 2),
    _UpsEEnvironmentHumidityHighSetPoint_Type()
)
upsEEnvironmentHumidityHighSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentHumidityHighSetPoint.setStatus("mandatory")


class _UpsEEnvironmentHumidityHighStatus_Type(Integer32):
    """Custom type upsEEnvironmentHumidityHighStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsEEnvironmentHumidityHighStatus_Type.__name__ = "Integer32"
_UpsEEnvironmentHumidityHighStatus_Object = MibScalar
upsEEnvironmentHumidityHighStatus = _UpsEEnvironmentHumidityHighStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 2, 3),
    _UpsEEnvironmentHumidityHighStatus_Type()
)
upsEEnvironmentHumidityHighStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentHumidityHighStatus.setStatus("mandatory")
_UpsEEnvironmentHumidityLowSetPoint_Type = Integer32
_UpsEEnvironmentHumidityLowSetPoint_Object = MibScalar
upsEEnvironmentHumidityLowSetPoint = _UpsEEnvironmentHumidityLowSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 2, 4),
    _UpsEEnvironmentHumidityLowSetPoint_Type()
)
upsEEnvironmentHumidityLowSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentHumidityLowSetPoint.setStatus("mandatory")


class _UpsEEnvironmentHumidityLowStatus_Type(Integer32):
    """Custom type upsEEnvironmentHumidityLowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UpsEEnvironmentHumidityLowStatus_Type.__name__ = "Integer32"
_UpsEEnvironmentHumidityLowStatus_Object = MibScalar
upsEEnvironmentHumidityLowStatus = _UpsEEnvironmentHumidityLowStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 2, 5),
    _UpsEEnvironmentHumidityLowStatus_Type()
)
upsEEnvironmentHumidityLowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentHumidityLowStatus.setStatus("mandatory")
_UpsEEnvironmentHumidityOffset_Type = Integer32
_UpsEEnvironmentHumidityOffset_Object = MibScalar
upsEEnvironmentHumidityOffset = _UpsEEnvironmentHumidityOffset_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 2, 6),
    _UpsEEnvironmentHumidityOffset_Type()
)
upsEEnvironmentHumidityOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentHumidityOffset.setStatus("mandatory")
_UpsEEnvironmentContactsNum_Type = NonNegativeInteger
_UpsEEnvironmentContactsNum_Object = MibScalar
upsEEnvironmentContactsNum = _UpsEEnvironmentContactsNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 3),
    _UpsEEnvironmentContactsNum_Type()
)
upsEEnvironmentContactsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEEnvironmentContactsNum.setStatus("mandatory")
_UpsEEnvironmentContactTable_Object = MibTable
upsEEnvironmentContactTable = _UpsEEnvironmentContactTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    upsEEnvironmentContactTable.setStatus("mandatory")
_UpsEEnvironmentContactEntry_Object = MibTableRow
upsEEnvironmentContactEntry = _UpsEEnvironmentContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 4, 1)
)
upsEEnvironmentContactEntry.setIndexNames(
    (0, "EPPC-MIB", "upsEEnvironmentContactIndex"),
)
if mibBuilder.loadTexts:
    upsEEnvironmentContactEntry.setStatus("mandatory")
_UpsEEnvironmentContactIndex_Type = PositiveInteger
_UpsEEnvironmentContactIndex_Object = MibTableColumn
upsEEnvironmentContactIndex = _UpsEEnvironmentContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 4, 1, 1),
    _UpsEEnvironmentContactIndex_Type()
)
upsEEnvironmentContactIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEEnvironmentContactIndex.setStatus("mandatory")


class _UpsEEnvironmentContactType_Type(Integer32):
    """Custom type upsEEnvironmentContactType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normallyClosed", 2),
          ("normallyOpen", 1),
          ("notUsed", 3))
    )


_UpsEEnvironmentContactType_Type.__name__ = "Integer32"
_UpsEEnvironmentContactType_Object = MibTableColumn
upsEEnvironmentContactType = _UpsEEnvironmentContactType_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 4, 1, 2),
    _UpsEEnvironmentContactType_Type()
)
upsEEnvironmentContactType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentContactType.setStatus("mandatory")


class _UpsEEnvironmentContactState_Type(Integer32):
    """Custom type upsEEnvironmentContactState based on Integer32"""
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


_UpsEEnvironmentContactState_Type.__name__ = "Integer32"
_UpsEEnvironmentContactState_Object = MibTableColumn
upsEEnvironmentContactState = _UpsEEnvironmentContactState_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 4, 1, 3),
    _UpsEEnvironmentContactState_Type()
)
upsEEnvironmentContactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEEnvironmentContactState.setStatus("mandatory")


class _UpsEEnvironmentContactDescription_Type(DisplayString):
    """Custom type upsEEnvironmentContactDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsEEnvironmentContactDescription_Type.__name__ = "DisplayString"
_UpsEEnvironmentContactDescription_Object = MibTableColumn
upsEEnvironmentContactDescription = _UpsEEnvironmentContactDescription_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 6, 4, 1, 4),
    _UpsEEnvironmentContactDescription_Type()
)
upsEEnvironmentContactDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEEnvironmentContactDescription.setStatus("mandatory")
_UpsEBatteryTest_ObjectIdentity = ObjectIdentity
upsEBatteryTest = _UpsEBatteryTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7)
)


class _UpsEBatteryTestStart_Type(Integer32):
    """Custom type upsEBatteryTestStart based on Integer32"""
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
        *(("batteryTest10Sec", 2),
          ("batteryTestUntilLow", 3),
          ("batteryTestWithTime", 4),
          ("cancelBatteryTest", 5),
          ("clearBatteryInfo", 6),
          ("none", 1))
    )


_UpsEBatteryTestStart_Type.__name__ = "Integer32"
_UpsEBatteryTestStart_Object = MibScalar
upsEBatteryTestStart = _UpsEBatteryTestStart_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 1),
    _UpsEBatteryTestStart_Type()
)
upsEBatteryTestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEBatteryTestStart.setStatus("mandatory")
_UpsEBatteryTestSettingTime_Type = NonNegativeInteger
_UpsEBatteryTestSettingTime_Object = MibScalar
upsEBatteryTestSettingTime = _UpsEBatteryTestSettingTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 2),
    _UpsEBatteryTestSettingTime_Type()
)
upsEBatteryTestSettingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEBatteryTestSettingTime.setStatus("mandatory")


class _UpsEBatteryTestResult_Type(Integer32):
    """Custom type upsEBatteryTestResult based on Integer32"""
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
        *(("failureOrWarning", 4),
          ("idle", 1),
          ("noFailure", 3),
          ("notPossible", 5),
          ("processing", 2),
          ("testCancel", 6))
    )


_UpsEBatteryTestResult_Type.__name__ = "Integer32"
_UpsEBatteryTestResult_Object = MibScalar
upsEBatteryTestResult = _UpsEBatteryTestResult_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 3),
    _UpsEBatteryTestResult_Type()
)
upsEBatteryTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEBatteryTestResult.setStatus("mandatory")


class _UpsEBatteryTestStartTime_Type(DisplayString):
    """Custom type upsEBatteryTestStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_UpsEBatteryTestStartTime_Type.__name__ = "DisplayString"
_UpsEBatteryTestStartTime_Object = MibScalar
upsEBatteryTestStartTime = _UpsEBatteryTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 4),
    _UpsEBatteryTestStartTime_Type()
)
upsEBatteryTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEBatteryTestStartTime.setStatus("mandatory")


class _UpsEBatteryTestElapsedTime_Type(DisplayString):
    """Custom type upsEBatteryTestElapsedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_UpsEBatteryTestElapsedTime_Type.__name__ = "DisplayString"
_UpsEBatteryTestElapsedTime_Object = MibScalar
upsEBatteryTestElapsedTime = _UpsEBatteryTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 5),
    _UpsEBatteryTestElapsedTime_Type()
)
upsEBatteryTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEBatteryTestElapsedTime.setStatus("mandatory")
_UpsEBatteryTestScheduleTable_Object = MibTable
upsEBatteryTestScheduleTable = _UpsEBatteryTestScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 6)
)
if mibBuilder.loadTexts:
    upsEBatteryTestScheduleTable.setStatus("mandatory")
_UpsEBatteryTestScheduleEntry_Object = MibTableRow
upsEBatteryTestScheduleEntry = _UpsEBatteryTestScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 6, 1)
)
upsEBatteryTestScheduleEntry.setIndexNames(
    (0, "EPPC-MIB", "upsEBatteryTestScheduleIndex"),
)
if mibBuilder.loadTexts:
    upsEBatteryTestScheduleEntry.setStatus("mandatory")
_UpsEBatteryTestScheduleIndex_Type = PositiveInteger
_UpsEBatteryTestScheduleIndex_Object = MibTableColumn
upsEBatteryTestScheduleIndex = _UpsEBatteryTestScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 6, 1, 1),
    _UpsEBatteryTestScheduleIndex_Type()
)
upsEBatteryTestScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEBatteryTestScheduleIndex.setStatus("mandatory")


class _UpsEBatteryTestScheduleDay_Type(Integer32):
    """Custom type upsEBatteryTestScheduleDay based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("none", 9),
          ("saturday", 6),
          ("specialday", 8),
          ("sunday", 7),
          ("thusday", 4),
          ("tuesday", 2),
          ("wednsday", 3))
    )


_UpsEBatteryTestScheduleDay_Type.__name__ = "Integer32"
_UpsEBatteryTestScheduleDay_Object = MibTableColumn
upsEBatteryTestScheduleDay = _UpsEBatteryTestScheduleDay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 6, 1, 2),
    _UpsEBatteryTestScheduleDay_Type()
)
upsEBatteryTestScheduleDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEBatteryTestScheduleDay.setStatus("mandatory")


class _UpsEBatteryTestScheduleTime_Type(DisplayString):
    """Custom type upsEBatteryTestScheduleTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsEBatteryTestScheduleTime_Type.__name__ = "DisplayString"
_UpsEBatteryTestScheduleTime_Object = MibTableColumn
upsEBatteryTestScheduleTime = _UpsEBatteryTestScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 6, 1, 3),
    _UpsEBatteryTestScheduleTime_Type()
)
upsEBatteryTestScheduleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEBatteryTestScheduleTime.setStatus("mandatory")


class _UpsEBatteryTestScheduleType_Type(Integer32):
    """Custom type upsEBatteryTestScheduleType based on Integer32"""
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
        *(("batteryTest10sec", 2),
          ("batteryTestUntilLow", 3),
          ("batteryTestWithTime", 4),
          ("none", 1))
    )


_UpsEBatteryTestScheduleType_Type.__name__ = "Integer32"
_UpsEBatteryTestScheduleType_Object = MibTableColumn
upsEBatteryTestScheduleType = _UpsEBatteryTestScheduleType_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 6, 1, 5),
    _UpsEBatteryTestScheduleType_Type()
)
upsEBatteryTestScheduleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEBatteryTestScheduleType.setStatus("mandatory")
_UpsEBatteryTestScheduleTestWithTime_Type = NonNegativeInteger
_UpsEBatteryTestScheduleTestWithTime_Object = MibTableColumn
upsEBatteryTestScheduleTestWithTime = _UpsEBatteryTestScheduleTestWithTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 6, 1, 6),
    _UpsEBatteryTestScheduleTestWithTime_Type()
)
upsEBatteryTestScheduleTestWithTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEBatteryTestScheduleTestWithTime.setStatus("mandatory")


class _UpsEBatteryTestScheduleSpecialDay_Type(DisplayString):
    """Custom type upsEBatteryTestScheduleSpecialDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpsEBatteryTestScheduleSpecialDay_Type.__name__ = "DisplayString"
_UpsEBatteryTestScheduleSpecialDay_Object = MibTableColumn
upsEBatteryTestScheduleSpecialDay = _UpsEBatteryTestScheduleSpecialDay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 7, 6, 1, 7),
    _UpsEBatteryTestScheduleSpecialDay_Type()
)
upsEBatteryTestScheduleSpecialDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEBatteryTestScheduleSpecialDay.setStatus("mandatory")
_UpsEControl_ObjectIdentity = ObjectIdentity
upsEControl = _UpsEControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8)
)
_UpsEControlOutputOffDelay_Type = NonNegativeInteger
_UpsEControlOutputOffDelay_Object = MibScalar
upsEControlOutputOffDelay = _UpsEControlOutputOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 1),
    _UpsEControlOutputOffDelay_Type()
)
upsEControlOutputOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEControlOutputOffDelay.setStatus("mandatory")
_UpsEControlOutputOnDelay_Type = NonNegativeInteger
_UpsEControlOutputOnDelay_Object = MibScalar
upsEControlOutputOnDelay = _UpsEControlOutputOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 2),
    _UpsEControlOutputOnDelay_Type()
)
upsEControlOutputOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEControlOutputOnDelay.setStatus("mandatory")


class _UpsEControlOutputOnOffControl_Type(Integer32):
    """Custom type upsEControlOutputOnOffControl based on Integer32"""
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
        *(("none", 4),
          ("upsEOutputOff", 1),
          ("upsEOutputOffCancel", 2),
          ("upsESleep", 3))
    )


_UpsEControlOutputOnOffControl_Type.__name__ = "Integer32"
_UpsEControlOutputOnOffControl_Object = MibScalar
upsEControlOutputOnOffControl = _UpsEControlOutputOnOffControl_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 3),
    _UpsEControlOutputOnOffControl_Type()
)
upsEControlOutputOnOffControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEControlOutputOnOffControl.setStatus("mandatory")
_UpsEShutdownEventsTable_Object = MibTable
upsEShutdownEventsTable = _UpsEShutdownEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 4)
)
if mibBuilder.loadTexts:
    upsEShutdownEventsTable.setStatus("mandatory")
_UpsEShutdownEventsEntry_Object = MibTableRow
upsEShutdownEventsEntry = _UpsEShutdownEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 4, 1)
)
upsEShutdownEventsEntry.setIndexNames(
    (0, "EPPC-MIB", "upsEShutdownEvent"),
)
if mibBuilder.loadTexts:
    upsEShutdownEventsEntry.setStatus("mandatory")


class _UpsEShutdownEvent_Type(Integer32):
    """Custom type upsEShutdownEvent based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("acFail", 1),
          ("batteryLow", 2),
          ("belowCapacityLimit", 11),
          ("belowRemainTimeLimit", 12),
          ("environmentContact1Alarm", 9),
          ("environmentContact2Alarm", 10),
          ("environmentHumidityOverThreshold", 8),
          ("environmentTemperatureOverThreshold", 7),
          ("upsEOverLoad", 3),
          ("upsEOverTemperature", 4),
          ("upsESpecialSchedule", 6),
          ("upsEWeeklySchedule", 5))
    )


_UpsEShutdownEvent_Type.__name__ = "Integer32"
_UpsEShutdownEvent_Object = MibTableColumn
upsEShutdownEvent = _UpsEShutdownEvent_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 4, 1, 1),
    _UpsEShutdownEvent_Type()
)
upsEShutdownEvent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEShutdownEvent.setStatus("mandatory")


class _UpsEShutdownEventAction_Type(Integer32):
    """Custom type upsEShutdownEventAction based on Integer32"""
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
        *(("disable", 1),
          ("shutdownClient", 3),
          ("shutdownUPS", 4),
          ("warning", 2))
    )


_UpsEShutdownEventAction_Type.__name__ = "Integer32"
_UpsEShutdownEventAction_Object = MibTableColumn
upsEShutdownEventAction = _UpsEShutdownEventAction_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 4, 1, 2),
    _UpsEShutdownEventAction_Type()
)
upsEShutdownEventAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEShutdownEventAction.setStatus("mandatory")
_UpsEShutdownwarningPeriodTime_Type = NonNegativeInteger
_UpsEShutdownwarningPeriodTime_Object = MibTableColumn
upsEShutdownwarningPeriodTime = _UpsEShutdownwarningPeriodTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 4, 1, 3),
    _UpsEShutdownwarningPeriodTime_Type()
)
upsEShutdownwarningPeriodTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEShutdownwarningPeriodTime.setStatus("mandatory")
_UpsEShutdownWarningPeriodInterval_Type = NonNegativeInteger
_UpsEShutdownWarningPeriodInterval_Object = MibTableColumn
upsEShutdownWarningPeriodInterval = _UpsEShutdownWarningPeriodInterval_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 4, 1, 4),
    _UpsEShutdownWarningPeriodInterval_Type()
)
upsEShutdownWarningPeriodInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEShutdownWarningPeriodInterval.setStatus("mandatory")
_UpsEControlWeeklyScheduleTable_Object = MibTable
upsEControlWeeklyScheduleTable = _UpsEControlWeeklyScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    upsEControlWeeklyScheduleTable.setStatus("mandatory")
_UpsEControlWeeklyScheduleEntry_Object = MibTableRow
upsEControlWeeklyScheduleEntry = _UpsEControlWeeklyScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 5, 1)
)
upsEControlWeeklyScheduleEntry.setIndexNames(
    (0, "EPPC-MIB", "upsEControlWeeklyScheduleIndex"),
)
if mibBuilder.loadTexts:
    upsEControlWeeklyScheduleEntry.setStatus("mandatory")
_UpsEControlWeeklyScheduleIndex_Type = PositiveInteger
_UpsEControlWeeklyScheduleIndex_Object = MibTableColumn
upsEControlWeeklyScheduleIndex = _UpsEControlWeeklyScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 5, 1, 1),
    _UpsEControlWeeklyScheduleIndex_Type()
)
upsEControlWeeklyScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEControlWeeklyScheduleIndex.setStatus("mandatory")


class _UpsEWeeklyScheduleShutdownDay_Type(Integer32):
    """Custom type upsEWeeklyScheduleShutdownDay based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("none", 8),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_UpsEWeeklyScheduleShutdownDay_Type.__name__ = "Integer32"
_UpsEWeeklyScheduleShutdownDay_Object = MibTableColumn
upsEWeeklyScheduleShutdownDay = _UpsEWeeklyScheduleShutdownDay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 5, 1, 2),
    _UpsEWeeklyScheduleShutdownDay_Type()
)
upsEWeeklyScheduleShutdownDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEWeeklyScheduleShutdownDay.setStatus("mandatory")


class _UpsEWeeklyScheduleShutdownTime_Type(DisplayString):
    """Custom type upsEWeeklyScheduleShutdownTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsEWeeklyScheduleShutdownTime_Type.__name__ = "DisplayString"
_UpsEWeeklyScheduleShutdownTime_Object = MibTableColumn
upsEWeeklyScheduleShutdownTime = _UpsEWeeklyScheduleShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 5, 1, 3),
    _UpsEWeeklyScheduleShutdownTime_Type()
)
upsEWeeklyScheduleShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEWeeklyScheduleShutdownTime.setStatus("mandatory")


class _UpsEWeeklyScheduleRestartDay_Type(Integer32):
    """Custom type upsEWeeklyScheduleRestartDay based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("none", 8),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_UpsEWeeklyScheduleRestartDay_Type.__name__ = "Integer32"
_UpsEWeeklyScheduleRestartDay_Object = MibTableColumn
upsEWeeklyScheduleRestartDay = _UpsEWeeklyScheduleRestartDay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 5, 1, 4),
    _UpsEWeeklyScheduleRestartDay_Type()
)
upsEWeeklyScheduleRestartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEWeeklyScheduleRestartDay.setStatus("mandatory")


class _UpsEWeeklyScheduleRestartTime_Type(DisplayString):
    """Custom type upsEWeeklyScheduleRestartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsEWeeklyScheduleRestartTime_Type.__name__ = "DisplayString"
_UpsEWeeklyScheduleRestartTime_Object = MibTableColumn
upsEWeeklyScheduleRestartTime = _UpsEWeeklyScheduleRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 5, 1, 5),
    _UpsEWeeklyScheduleRestartTime_Type()
)
upsEWeeklyScheduleRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEWeeklyScheduleRestartTime.setStatus("mandatory")
_UpsEControlSpecialDayScheduleTable_Object = MibTable
upsEControlSpecialDayScheduleTable = _UpsEControlSpecialDayScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 6)
)
if mibBuilder.loadTexts:
    upsEControlSpecialDayScheduleTable.setStatus("mandatory")
_UpsEControlSpecialDayScheduleEntry_Object = MibTableRow
upsEControlSpecialDayScheduleEntry = _UpsEControlSpecialDayScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 6, 1)
)
upsEControlSpecialDayScheduleEntry.setIndexNames(
    (0, "EPPC-MIB", "upsEControlSpecialDayScheduleIndex"),
)
if mibBuilder.loadTexts:
    upsEControlSpecialDayScheduleEntry.setStatus("mandatory")
_UpsEControlSpecialDayScheduleIndex_Type = PositiveInteger
_UpsEControlSpecialDayScheduleIndex_Object = MibTableColumn
upsEControlSpecialDayScheduleIndex = _UpsEControlSpecialDayScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 6, 1, 1),
    _UpsEControlSpecialDayScheduleIndex_Type()
)
upsEControlSpecialDayScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEControlSpecialDayScheduleIndex.setStatus("mandatory")


class _UpsESpecialDayScheduleShutdownDay_Type(DisplayString):
    """Custom type upsESpecialDayScheduleShutdownDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpsESpecialDayScheduleShutdownDay_Type.__name__ = "DisplayString"
_UpsESpecialDayScheduleShutdownDay_Object = MibTableColumn
upsESpecialDayScheduleShutdownDay = _UpsESpecialDayScheduleShutdownDay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 6, 1, 2),
    _UpsESpecialDayScheduleShutdownDay_Type()
)
upsESpecialDayScheduleShutdownDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsESpecialDayScheduleShutdownDay.setStatus("mandatory")


class _UpsESpecialDayScheduleShutdownTime_Type(DisplayString):
    """Custom type upsESpecialDayScheduleShutdownTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsESpecialDayScheduleShutdownTime_Type.__name__ = "DisplayString"
_UpsESpecialDayScheduleShutdownTime_Object = MibTableColumn
upsESpecialDayScheduleShutdownTime = _UpsESpecialDayScheduleShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 6, 1, 3),
    _UpsESpecialDayScheduleShutdownTime_Type()
)
upsESpecialDayScheduleShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsESpecialDayScheduleShutdownTime.setStatus("mandatory")


class _UpsESpecialDayScheduleRestartDay_Type(DisplayString):
    """Custom type upsESpecialDayScheduleRestartDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpsESpecialDayScheduleRestartDay_Type.__name__ = "DisplayString"
_UpsESpecialDayScheduleRestartDay_Object = MibTableColumn
upsESpecialDayScheduleRestartDay = _UpsESpecialDayScheduleRestartDay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 6, 1, 4),
    _UpsESpecialDayScheduleRestartDay_Type()
)
upsESpecialDayScheduleRestartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsESpecialDayScheduleRestartDay.setStatus("mandatory")


class _UpsESpecialDayScheduleRestartTime_Type(DisplayString):
    """Custom type upsESpecialDayScheduleRestartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsESpecialDayScheduleRestartTime_Type.__name__ = "DisplayString"
_UpsESpecialDayScheduleRestartTime_Object = MibTableColumn
upsESpecialDayScheduleRestartTime = _UpsESpecialDayScheduleRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 6, 1, 5),
    _UpsESpecialDayScheduleRestartTime_Type()
)
upsESpecialDayScheduleRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsESpecialDayScheduleRestartTime.setStatus("mandatory")
_UpsESystemMasterOffDelay_Type = Integer32
_UpsESystemMasterOffDelay_Object = MibScalar
upsESystemMasterOffDelay = _UpsESystemMasterOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 7),
    _UpsESystemMasterOffDelay_Type()
)
upsESystemMasterOffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemMasterOffDelay.setStatus("mandatory")
_UpsESystemMasterOnDelay_Type = Integer32
_UpsESystemMasterOnDelay_Object = MibScalar
upsESystemMasterOnDelay = _UpsESystemMasterOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 8, 8),
    _UpsESystemMasterOnDelay_Type()
)
upsESystemMasterOnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsESystemMasterOnDelay.setStatus("mandatory")
_UpsETrapControl_ObjectIdentity = ObjectIdentity
upsETrapControl = _UpsETrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 9)
)
_UpsETrapsReceiversTable_Object = MibTable
upsETrapsReceiversTable = _UpsETrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    upsETrapsReceiversTable.setStatus("mandatory")
_UpsETrapsReceiversEntry_Object = MibTableRow
upsETrapsReceiversEntry = _UpsETrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 9, 1, 1)
)
upsETrapsReceiversEntry.setIndexNames(
    (0, "EPPC-MIB", "upsETrapsReceiversIndex"),
)
if mibBuilder.loadTexts:
    upsETrapsReceiversEntry.setStatus("mandatory")
_UpsETrapsReceiversIndex_Type = PositiveInteger
_UpsETrapsReceiversIndex_Object = MibTableColumn
upsETrapsReceiversIndex = _UpsETrapsReceiversIndex_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 9, 1, 1, 1),
    _UpsETrapsReceiversIndex_Type()
)
upsETrapsReceiversIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsETrapsReceiversIndex.setStatus("mandatory")


class _UpsETrapsReceiverAddress_Type(DisplayString):
    """Custom type upsETrapsReceiverAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_UpsETrapsReceiverAddress_Type.__name__ = "DisplayString"
_UpsETrapsReceiverAddress_Object = MibTableColumn
upsETrapsReceiverAddress = _UpsETrapsReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 9, 1, 1, 2),
    _UpsETrapsReceiverAddress_Type()
)
upsETrapsReceiverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsETrapsReceiverAddress.setStatus("mandatory")


class _UpsETrapReceiverCommunityString_Type(DisplayString):
    """Custom type upsETrapReceiverCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpsETrapReceiverCommunityString_Type.__name__ = "DisplayString"
_UpsETrapReceiverCommunityString_Object = MibTableColumn
upsETrapReceiverCommunityString = _UpsETrapReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 9, 1, 1, 3),
    _UpsETrapReceiverCommunityString_Type()
)
upsETrapReceiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsETrapReceiverCommunityString.setStatus("mandatory")


class _UpsETrapType_Type(Integer32):
    """Custom type upsETrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eppcTrap", 3),
          ("none", 1),
          ("rfc1628Trap", 2))
    )


_UpsETrapType_Type.__name__ = "Integer32"
_UpsETrapType_Object = MibTableColumn
upsETrapType = _UpsETrapType_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 9, 1, 1, 4),
    _UpsETrapType_Type()
)
upsETrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsETrapType.setStatus("mandatory")


class _UpsETrapsSeverityLevel_Type(Integer32):
    """Custom type upsETrapsSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informational", 1),
          ("severe", 3),
          ("warning", 2))
    )


_UpsETrapsSeverityLevel_Type.__name__ = "Integer32"
_UpsETrapsSeverityLevel_Object = MibTableColumn
upsETrapsSeverityLevel = _UpsETrapsSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 9, 1, 1, 5),
    _UpsETrapsSeverityLevel_Type()
)
upsETrapsSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsETrapsSeverityLevel.setStatus("mandatory")


class _UpsETrapReceiverDescription_Type(DisplayString):
    """Custom type upsETrapReceiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsETrapReceiverDescription_Type.__name__ = "DisplayString"
_UpsETrapReceiverDescription_Object = MibTableColumn
upsETrapReceiverDescription = _UpsETrapReceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 9, 1, 1, 6),
    _UpsETrapReceiverDescription_Type()
)
upsETrapReceiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsETrapReceiverDescription.setStatus("mandatory")


class _UpsETrapState_Type(DisplayString):
    """Custom type upsETrapState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UpsETrapState_Type.__name__ = "DisplayString"
_UpsETrapState_Object = MibScalar
upsETrapState = _UpsETrapState_Object(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 1, 9, 2),
    _UpsETrapState_Type()
)
upsETrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsETrapState.setStatus("mandatory")
_UpsETraps_ObjectIdentity = ObjectIdentity
upsETraps = _UpsETraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2)
)

# Managed Objects groups


# Notification objects

upsEPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    upsEPowerFail.setStatus(
        ""
    )

upsEPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    upsEPowerRestored.setStatus(
        ""
    )

upsELowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 3)
)
if mibBuilder.loadTexts:
    upsELowBattery.setStatus(
        ""
    )

upsEReturnFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    upsEReturnFromLowBattery.setStatus(
        ""
    )

upsEFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    upsEFailed.setStatus(
        ""
    )

upsEOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    upsEOk.setStatus(
        ""
    )

upsEOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 7)
)
upsEOnBattery.setObjects(
      *(("EPPC-MIB", "upsEBatteryEstimatedMinutesRemaining"),
        ("EPPC-MIB", "upsESecondsOnBattery"))
)
if mibBuilder.loadTexts:
    upsEOnBattery.setStatus(
        ""
    )

upsENotOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 8)
)
if mibBuilder.loadTexts:
    upsENotOnBattery.setStatus(
        ""
    )

upsETestInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 9)
)
if mibBuilder.loadTexts:
    upsETestInProgress.setStatus(
        ""
    )

upsETestOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 10)
)
upsETestOver.setObjects(
      *(("EPPC-MIB", "upsEBatteryTestStart"),
        ("EPPC-MIB", "upsEBatteryTestSettingTime"),
        ("EPPC-MIB", "upsEBatteryTestResult"),
        ("EPPC-MIB", "upsEBatteryTestStartTime"))
)
if mibBuilder.loadTexts:
    upsETestOver.setStatus(
        ""
    )

upsEBypassOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 11)
)
if mibBuilder.loadTexts:
    upsEBypassOn.setStatus(
        ""
    )

upsEOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 12)
)
if mibBuilder.loadTexts:
    upsEOnline.setStatus(
        ""
    )

upsECommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 13)
)
if mibBuilder.loadTexts:
    upsECommunicationLost.setStatus(
        ""
    )

upsECommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 14)
)
if mibBuilder.loadTexts:
    upsECommunicationEstablished.setStatus(
        ""
    )

upsEGoingShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 15)
)
if mibBuilder.loadTexts:
    upsEGoingShutdown.setStatus(
        ""
    )

upsEShutdownCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 16)
)
if mibBuilder.loadTexts:
    upsEShutdownCancelled.setStatus(
        ""
    )

upsEOutlet1GoingShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 17)
)
if mibBuilder.loadTexts:
    upsEOutlet1GoingShutdown.setStatus(
        ""
    )

upsEOutlet1ShutdownCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 18)
)
if mibBuilder.loadTexts:
    upsEOutlet1ShutdownCancelled.setStatus(
        ""
    )

upsEOutlet2GoingShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 19)
)
if mibBuilder.loadTexts:
    upsEOutlet2GoingShutdown.setStatus(
        ""
    )

upsEOutlet2ShutdownCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 20)
)
if mibBuilder.loadTexts:
    upsEOutlet2ShutdownCancelled.setStatus(
        ""
    )

upsESleeping = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 21)
)
upsESleeping.setObjects(
    ("EPPC-MIB", "upsEControlOutputOnDelay")
)
if mibBuilder.loadTexts:
    upsESleeping.setStatus(
        ""
    )

upsEWokeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 22)
)
if mibBuilder.loadTexts:
    upsEWokeUp.setStatus(
        ""
    )

upsEOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 23)
)
upsEOverTemperature.setObjects(
      *(("EPPC-MIB", "upsESystemTemperature"),
        ("EPPC-MIB", "upsESystemConfigOverTemperatureSetPoint"))
)
if mibBuilder.loadTexts:
    upsEOverTemperature.setStatus(
        ""
    )

upsENotOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 24)
)
upsENotOverTemperature.setObjects(
      *(("EPPC-MIB", "upsESystemTemperature"),
        ("EPPC-MIB", "upsESystemConfigOverTemperatureSetPoint"))
)
if mibBuilder.loadTexts:
    upsENotOverTemperature.setStatus(
        ""
    )

upsEOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 25)
)
upsEOverLoad.setObjects(
      *(("EPPC-MIB", "upsESystemOutputLoad"),
        ("EPPC-MIB", "upsESystemConfigOutputLoadHighSetPoint"))
)
if mibBuilder.loadTexts:
    upsEOverLoad.setStatus(
        ""
    )

upsENotOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 26)
)
upsENotOverLoad.setObjects(
      *(("EPPC-MIB", "upsESystemOutputLoad"),
        ("EPPC-MIB", "upsESystemConfigOutputLoadHighSetPoint"))
)
if mibBuilder.loadTexts:
    upsENotOverLoad.setStatus(
        ""
    )

upsEModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 27)
)
if mibBuilder.loadTexts:
    upsEModuleInserted.setStatus(
        ""
    )

upsEModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 28)
)
if mibBuilder.loadTexts:
    upsEModuleRemoved.setStatus(
        ""
    )

sensorTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 29)
)
sensorTemperatureTooHigh.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentTemperatureHighSetPoint"),
        ("EPPC-MIB", "upsEEnvironmentCurrentTemperature"))
)
if mibBuilder.loadTexts:
    sensorTemperatureTooHigh.setStatus(
        ""
    )

sensorTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 30)
)
sensorTemperatureNotHigh.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentTemperatureHighSetPoint"),
        ("EPPC-MIB", "upsEEnvironmentCurrentTemperature"))
)
if mibBuilder.loadTexts:
    sensorTemperatureNotHigh.setStatus(
        ""
    )

sensorTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 31)
)
sensorTemperatureTooLow.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentTemperatureLowSetPoint"),
        ("EPPC-MIB", "upsEEnvironmentCurrentTemperature"))
)
if mibBuilder.loadTexts:
    sensorTemperatureTooLow.setStatus(
        ""
    )

sensorTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 32)
)
sensorTemperatureNotLow.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentTemperatureLowSetPoint"),
        ("EPPC-MIB", "upsEEnvironmentCurrentTemperature"))
)
if mibBuilder.loadTexts:
    sensorTemperatureNotLow.setStatus(
        ""
    )

sensorHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 33)
)
sensorHumidityTooHigh.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentHumidityHighSetPoint"),
        ("EPPC-MIB", "upsEEnvironmentCurrentHumidity"))
)
if mibBuilder.loadTexts:
    sensorHumidityTooHigh.setStatus(
        ""
    )

sensorHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 34)
)
sensorHumidityNotHigh.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentHumidityHighSetPoint"),
        ("EPPC-MIB", "upsEEnvironmentCurrentHumidity"))
)
if mibBuilder.loadTexts:
    sensorHumidityNotHigh.setStatus(
        ""
    )

sensorHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 35)
)
sensorHumidityTooLow.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentHumidityLowSetPoint"),
        ("EPPC-MIB", "upsEEnvironmentCurrentHumidity"))
)
if mibBuilder.loadTexts:
    sensorHumidityTooLow.setStatus(
        ""
    )

sensorHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 36)
)
sensorHumidityNotLow.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentHumidityLowSetPoint"),
        ("EPPC-MIB", "upsEEnvironmentCurrentHumidity"))
)
if mibBuilder.loadTexts:
    sensorHumidityNotLow.setStatus(
        ""
    )

contactAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 37)
)
contactAlarm1Active.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentContactType"),
        ("EPPC-MIB", "upsEEnvironmentContactDescription"))
)
if mibBuilder.loadTexts:
    contactAlarm1Active.setStatus(
        ""
    )

concactAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 38)
)
concactAlarm1Normal.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentContactType"),
        ("EPPC-MIB", "upsEEnvironmentContactDescription"))
)
if mibBuilder.loadTexts:
    concactAlarm1Normal.setStatus(
        ""
    )

contactAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 39)
)
contactAlarm2Active.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentContactType"),
        ("EPPC-MIB", "upsEEnvironmentContactDescription"))
)
if mibBuilder.loadTexts:
    contactAlarm2Active.setStatus(
        ""
    )

contactAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 40)
)
contactAlarm2Normal.setObjects(
      *(("EPPC-MIB", "upsEEnvironmentContactType"),
        ("EPPC-MIB", "upsEEnvironmentContactDescription"))
)
if mibBuilder.loadTexts:
    contactAlarm2Normal.setStatus(
        ""
    )

upsEInternalwarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 41)
)
if mibBuilder.loadTexts:
    upsEInternalwarning.setStatus(
        ""
    )

upsEReturnFromInternalwarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 42)
)
if mibBuilder.loadTexts:
    upsEReturnFromInternalwarning.setStatus(
        ""
    )

upsEEPOActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 43)
)
if mibBuilder.loadTexts:
    upsEEPOActive.setStatus(
        ""
    )

upsEReturnFromEPOActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 44)
)
if mibBuilder.loadTexts:
    upsEReturnFromEPOActive.setStatus(
        ""
    )

upsEModuleUnlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 45)
)
if mibBuilder.loadTexts:
    upsEModuleUnlock.setStatus(
        ""
    )

upsEReturnFromModuleUnlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 46)
)
if mibBuilder.loadTexts:
    upsEReturnFromModuleUnlock.setStatus(
        ""
    )

upsEMain1Neutralloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 47)
)
if mibBuilder.loadTexts:
    upsEMain1Neutralloss.setStatus(
        ""
    )

upsEReturnFromMain1Neutralloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 48)
)
if mibBuilder.loadTexts:
    upsEReturnFromMain1Neutralloss.setStatus(
        ""
    )

upsEMain1phaseerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 49)
)
if mibBuilder.loadTexts:
    upsEMain1phaseerror.setStatus(
        ""
    )

upsEReturnFromMain1phaseerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 50)
)
if mibBuilder.loadTexts:
    upsEReturnFromMain1phaseerror.setStatus(
        ""
    )

upsESitefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 51)
)
if mibBuilder.loadTexts:
    upsESitefault.setStatus(
        ""
    )

upsEReturnFromSitefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 52)
)
if mibBuilder.loadTexts:
    upsEReturnFromSitefault.setStatus(
        ""
    )

upsEBypassAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 53)
)
if mibBuilder.loadTexts:
    upsEBypassAbnormal.setStatus(
        ""
    )

upsEReturnFromBypassAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 54)
)
if mibBuilder.loadTexts:
    upsEReturnFromBypassAbnormal.setStatus(
        ""
    )

upsEBypassPhaseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 55)
)
if mibBuilder.loadTexts:
    upsEBypassPhaseError.setStatus(
        ""
    )

upsEReturnFromBypassPhaseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 56)
)
if mibBuilder.loadTexts:
    upsEReturnFromBypassPhaseError.setStatus(
        ""
    )

upsEBatteryOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 57)
)
if mibBuilder.loadTexts:
    upsEBatteryOpen.setStatus(
        ""
    )

upsEReturnFromBatteryOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 58)
)
if mibBuilder.loadTexts:
    upsEReturnFromBatteryOpen.setStatus(
        ""
    )

upsEBatteryOverCharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 59)
)
if mibBuilder.loadTexts:
    upsEBatteryOverCharge.setStatus(
        ""
    )

upsEReturnFromBatteryOverCharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 60)
)
if mibBuilder.loadTexts:
    upsEReturnFromBatteryOverCharge.setStatus(
        ""
    )

upsEBatteryReverse = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 61)
)
if mibBuilder.loadTexts:
    upsEBatteryReverse.setStatus(
        ""
    )

upsEReturnFromBatteryReverse = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 62)
)
if mibBuilder.loadTexts:
    upsEReturnFromBatteryReverse.setStatus(
        ""
    )

upsEOverloadforewarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 63)
)
if mibBuilder.loadTexts:
    upsEOverloadforewarning.setStatus(
        ""
    )

upsEReturnFromOverloadforewarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 64)
)
if mibBuilder.loadTexts:
    upsEReturnFromOverloadforewarning.setStatus(
        ""
    )

upsEOverloadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 65)
)
if mibBuilder.loadTexts:
    upsEOverloadWarning.setStatus(
        ""
    )

upsEReturnFromOverloadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 66)
)
if mibBuilder.loadTexts:
    upsEReturnFromOverloadWarning.setStatus(
        ""
    )

upsEFanLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 67)
)
if mibBuilder.loadTexts:
    upsEFanLock.setStatus(
        ""
    )

upsEReturnFromFanLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 68)
)
if mibBuilder.loadTexts:
    upsEReturnFromFanLock.setStatus(
        ""
    )

upsEMaintaincoverisopen = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 69)
)
if mibBuilder.loadTexts:
    upsEMaintaincoverisopen.setStatus(
        ""
    )

upsEReturnFromMaintaincoverisopen = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 70)
)
if mibBuilder.loadTexts:
    upsEReturnFromMaintaincoverisopen.setStatus(
        ""
    )

upsEChargerfault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 71)
)
if mibBuilder.loadTexts:
    upsEChargerfault.setStatus(
        ""
    )

upsEReturnFromChargerfault = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 72)
)
if mibBuilder.loadTexts:
    upsEReturnFromChargerfault.setStatus(
        ""
    )

upsEModulelocationerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 73)
)
if mibBuilder.loadTexts:
    upsEModulelocationerror.setStatus(
        ""
    )

upsEReturnFromModulelocationerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 74)
)
if mibBuilder.loadTexts:
    upsEReturnFromModulelocationerror.setStatus(
        ""
    )

upsETurnonabnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 75)
)
if mibBuilder.loadTexts:
    upsETurnonabnormal.setStatus(
        ""
    )

upsEReturnFromTurnonabnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 76)
)
if mibBuilder.loadTexts:
    upsEReturnFromTurnonabnormal.setStatus(
        ""
    )

upsERedundancyloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 77)
)
if mibBuilder.loadTexts:
    upsERedundancyloss.setStatus(
        ""
    )

upsEReturnFromRedundancyloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 78)
)
if mibBuilder.loadTexts:
    upsEReturnFromRedundancyloss.setStatus(
        ""
    )

upsEHotSwapActived = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 79)
)
if mibBuilder.loadTexts:
    upsEHotSwapActived.setStatus(
        ""
    )

upsEReturnFromHotSwapActived = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 80)
)
if mibBuilder.loadTexts:
    upsEReturnFromHotSwapActived.setStatus(
        ""
    )

upsEBatteryInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 81)
)
if mibBuilder.loadTexts:
    upsEBatteryInform.setStatus(
        ""
    )

upsEReturnFromBatteryInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 82)
)
if mibBuilder.loadTexts:
    upsEReturnFromBatteryInform.setStatus(
        ""
    )

upsEInspectionInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 83)
)
if mibBuilder.loadTexts:
    upsEInspectionInform.setStatus(
        ""
    )

upsEReturnFromInspectionInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 84)
)
if mibBuilder.loadTexts:
    upsEReturnFromInspectionInform.setStatus(
        ""
    )

upsEGuaranteeInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 85)
)
if mibBuilder.loadTexts:
    upsEGuaranteeInform.setStatus(
        ""
    )

upsEReturnFromGuaranteeInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 86)
)
if mibBuilder.loadTexts:
    upsEReturnFromGuaranteeInform.setStatus(
        ""
    )

upsETemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 87)
)
if mibBuilder.loadTexts:
    upsETemperatureLow.setStatus(
        ""
    )

upsEReturnFromTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 88)
)
if mibBuilder.loadTexts:
    upsEReturnFromTemperatureLow.setStatus(
        ""
    )

upsETemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 89)
)
if mibBuilder.loadTexts:
    upsETemperatureHigh.setStatus(
        ""
    )

upsEReturnFromTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 90)
)
if mibBuilder.loadTexts:
    upsEReturnFromTemperatureHigh.setStatus(
        ""
    )

upsEBatteryOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 91)
)
if mibBuilder.loadTexts:
    upsEBatteryOverTemperature.setStatus(
        ""
    )

upsEReturnFromBatteryOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 92)
)
if mibBuilder.loadTexts:
    upsEReturnFromBatteryOverTemperature.setStatus(
        ""
    )

upsEFanMaintainInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 93)
)
if mibBuilder.loadTexts:
    upsEFanMaintainInform.setStatus(
        ""
    )

upsEReturnFromFanMaintainInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 94)
)
if mibBuilder.loadTexts:
    upsEReturnFromFanMaintainInform.setStatus(
        ""
    )

upsEBusCapacitanceMaintainInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 95)
)
if mibBuilder.loadTexts:
    upsEBusCapacitanceMaintainInform.setStatus(
        ""
    )

upsEReturnFromBusCapacitanceMaintainInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 96)
)
if mibBuilder.loadTexts:
    upsEReturnFromBusCapacitanceMaintainInform.setStatus(
        ""
    )

upsESystemOverCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 97)
)
if mibBuilder.loadTexts:
    upsESystemOverCapacity.setStatus(
        ""
    )

upsEReturnFromSystemOverCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 98)
)
if mibBuilder.loadTexts:
    upsEReturnFromSystemOverCapacity.setStatus(
        ""
    )

upsEBelowCapacityLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 123)
)
upsEBelowCapacityLimit.setObjects(
      *(("EPPC-MIB", "upsEBatteryEstimatedChargeRemaining"),
        ("EPPC-MIB", "upsESystemConfigBelowCapacityLimit"))
)
if mibBuilder.loadTexts:
    upsEBelowCapacityLimit.setStatus(
        ""
    )

upsENotBelowCapacityLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 124)
)
if mibBuilder.loadTexts:
    upsENotBelowCapacityLimit.setStatus(
        ""
    )

upsEBelowRemainTimeLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 125)
)
upsEBelowRemainTimeLimit.setObjects(
      *(("EPPC-MIB", "upsEBatteryEstimatedMinutesRemaining"),
        ("EPPC-MIB", "upsESystemConfigBelowRemainTimeLimit"))
)
if mibBuilder.loadTexts:
    upsEBelowRemainTimeLimit.setStatus(
        ""
    )

upsENotBelowRemainTimeLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 126)
)
if mibBuilder.loadTexts:
    upsENotBelowRemainTimeLimit.setStatus(
        ""
    )

upsELoadSegment1Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 127)
)
if mibBuilder.loadTexts:
    upsELoadSegment1Off.setStatus(
        ""
    )

upsELoadSegment1On = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 128)
)
if mibBuilder.loadTexts:
    upsELoadSegment1On.setStatus(
        ""
    )

upsELoadSegment2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 129)
)
if mibBuilder.loadTexts:
    upsELoadSegment2Off.setStatus(
        ""
    )

upsELoadSegment2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 10, 1, 2, 0, 130)
)
if mibBuilder.loadTexts:
    upsELoadSegment2On.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EPPC-MIB",
    **{"ppc": ppc,
       "device": device,
       "upsAgent": upsAgent,
       "upsE": upsE,
       "upsEIdentity": upsEIdentity,
       "upsEIdentityManufacturer": upsEIdentityManufacturer,
       "upsEIdentityModel": upsEIdentityModel,
       "upsEIdentityUPSFirmwareVerison": upsEIdentityUPSFirmwareVerison,
       "upsEIndentityUPSSerialNumber": upsEIndentityUPSSerialNumber,
       "upsEIdentityDescription": upsEIdentityDescription,
       "upsEIdentityAgentSoftwareVerison": upsEIdentityAgentSoftwareVerison,
       "upsEIdentityAttachedDevices": upsEIdentityAttachedDevices,
       "upsESystemSummary": upsESystemSummary,
       "upsESystemStatus": upsESystemStatus,
       "upsESystemTemperature": upsESystemTemperature,
       "upsESystemWarningCode": upsESystemWarningCode,
       "upsESystemFaultCode": upsESystemFaultCode,
       "upsESystemConfigInputVoltage": upsESystemConfigInputVoltage,
       "upsESystemConfigInputFrequence": upsESystemConfigInputFrequence,
       "upsESystemConfigOutputVoltage": upsESystemConfigOutputVoltage,
       "upsESystemConfigOutputFrequency": upsESystemConfigOutputFrequency,
       "upsESystemConfigOutputVA": upsESystemConfigOutputVA,
       "upsESystemConfigOutputPower": upsESystemConfigOutputPower,
       "upsESystemConfigOutputLoadHighSetPoint": upsESystemConfigOutputLoadHighSetPoint,
       "upsESystemConfigOverTemperatureSetPoint": upsESystemConfigOverTemperatureSetPoint,
       "upsESystemInputSourceNum": upsESystemInputSourceNum,
       "upsESystemInputLineBads": upsESystemInputLineBads,
       "upsESystemInputNumPhases": upsESystemInputNumPhases,
       "upsESystemInputTable": upsESystemInputTable,
       "upsESystemInputEntry": upsESystemInputEntry,
       "upsESystemInputPhase": upsESystemInputPhase,
       "upsESystemInputFrequency": upsESystemInputFrequency,
       "upsESystemInputVoltage": upsESystemInputVoltage,
       "upsESystemInputCurrent": upsESystemInputCurrent,
       "upsESystemInputWatts": upsESystemInputWatts,
       "upsESystemOutputNumPhase": upsESystemOutputNumPhase,
       "upsESystemOutputTable": upsESystemOutputTable,
       "upsESystemOutputEntry": upsESystemOutputEntry,
       "upsESystemOutputPhase": upsESystemOutputPhase,
       "upsESystemOutputFrequency": upsESystemOutputFrequency,
       "upsESystemOutputVoltage": upsESystemOutputVoltage,
       "upsESystemOutputCurrent": upsESystemOutputCurrent,
       "upsESystemOutputWatts": upsESystemOutputWatts,
       "upsESystemOutputVA": upsESystemOutputVA,
       "upsESystemOutputLoad": upsESystemOutputLoad,
       "upsESystemBypassNumPhase": upsESystemBypassNumPhase,
       "upsESystemBypassTable": upsESystemBypassTable,
       "upsESystemBypassEntry": upsESystemBypassEntry,
       "upsESystemBypassPhase": upsESystemBypassPhase,
       "upsESystemBypassFrequency": upsESystemBypassFrequency,
       "upsESystemBypassVoltage": upsESystemBypassVoltage,
       "upsESystemBypassCurrent": upsESystemBypassCurrent,
       "upsESystemBypassWatts": upsESystemBypassWatts,
       "upsESystemConfigBelowCapacityLimit": upsESystemConfigBelowCapacityLimit,
       "upsESystemConfigBelowRemainTimeLimit": upsESystemConfigBelowRemainTimeLimit,
       "upsEBatterySystem": upsEBatterySystem,
       "upsEBatteryStatus": upsEBatteryStatus,
       "upsESecondsOnBattery": upsESecondsOnBattery,
       "upsEBatteryEstimatedMinutesRemaining": upsEBatteryEstimatedMinutesRemaining,
       "upsEBatteryEstimatedChargeRemaining": upsEBatteryEstimatedChargeRemaining,
       "upsEPositiveBatteryVoltage": upsEPositiveBatteryVoltage,
       "upsENegativeBatteryVoltage": upsENegativeBatteryVoltage,
       "upsEBatteryCellNumber": upsEBatteryCellNumber,
       "upsEBatteryTemperature": upsEBatteryTemperature,
       "upsEBatteryLastReplacedDate": upsEBatteryLastReplacedDate,
       "upsEBatteryABMStatus": upsEBatteryABMStatus,
       "upsEChargerModulesNum": upsEChargerModulesNum,
       "upsEChargerModulesTable": upsEChargerModulesTable,
       "upsEChargerModulesEntry": upsEChargerModulesEntry,
       "chargerModulesNum": chargerModulesNum,
       "chargerModulesAddress": chargerModulesAddress,
       "positiveChargeVotlage": positiveChargeVotlage,
       "negativeChargeVoltage": negativeChargeVoltage,
       "positiveChargeCurrent": positiveChargeCurrent,
       "negativeChargeCurrent": negativeChargeCurrent,
       "chargerModulesTemperature": chargerModulesTemperature,
       "chargerModulesMode": chargerModulesMode,
       "upsEPowerConverterSystem": upsEPowerConverterSystem,
       "upsEUPSModulesNum": upsEUPSModulesNum,
       "upsEModulesTable": upsEModulesTable,
       "upsEModulesEntry": upsEModulesEntry,
       "upsEModulesNum": upsEModulesNum,
       "upsEModuleAddress": upsEModuleAddress,
       "upsEModulePositiveBusVolt": upsEModulePositiveBusVolt,
       "upsEModuleNegativeBusVolt": upsEModuleNegativeBusVolt,
       "upsEModuleTemperature": upsEModuleTemperature,
       "upsEModuleWorkingMode": upsEModuleWorkingMode,
       "upsEModuleOutputCurrentR": upsEModuleOutputCurrentR,
       "upsEModuleOutputWattR": upsEModuleOutputWattR,
       "upsEModuleOutputLoadR": upsEModuleOutputLoadR,
       "upsEModuleWarningCode": upsEModuleWarningCode,
       "upsEModuleFaultCode": upsEModuleFaultCode,
       "upsEModuleTrapState": upsEModuleTrapState,
       "upsEModuleConfigOutputVA": upsEModuleConfigOutputVA,
       "upsEModuleOutputCurrentS": upsEModuleOutputCurrentS,
       "upsEModuleOutputCurrentT": upsEModuleOutputCurrentT,
       "upsEModuleOutputWattS": upsEModuleOutputWattS,
       "upsEModuleOutputWattT": upsEModuleOutputWattT,
       "upsEModuleOutputLoadS": upsEModuleOutputLoadS,
       "upsEModuleOutputLoadT": upsEModuleOutputLoadT,
       "upsEModuleOutputVAR": upsEModuleOutputVAR,
       "upsEModuleOutputVAS": upsEModuleOutputVAS,
       "upsEModuleOutputVAT": upsEModuleOutputVAT,
       "upsELoadSegment": upsELoadSegment,
       "upsELoadSegment1OffDelay": upsELoadSegment1OffDelay,
       "upsELoadSegment1OnDelay": upsELoadSegment1OnDelay,
       "upsELoadSegment1AutoOffTimer": upsELoadSegment1AutoOffTimer,
       "upsELoadSegment1AutoOnTimer": upsELoadSegment1AutoOnTimer,
       "upsELoadSegment1State": upsELoadSegment1State,
       "upsELoadSegment2OffDelay": upsELoadSegment2OffDelay,
       "upsELoadSegment2OnDelay": upsELoadSegment2OnDelay,
       "upsELoadSegment2AutoOffTimer": upsELoadSegment2AutoOffTimer,
       "upsELoadSegment2AutoOnTimer": upsELoadSegment2AutoOnTimer,
       "upsELoadSegment2State": upsELoadSegment2State,
       "upsEEnvironment": upsEEnvironment,
       "upsEEnvironmentTemperature": upsEEnvironmentTemperature,
       "upsEEnvironmentCurrentTemperature": upsEEnvironmentCurrentTemperature,
       "upsEEnvironmentTemperatureHighSetPoint": upsEEnvironmentTemperatureHighSetPoint,
       "upsEEnvironmentTemperatureHighStatus": upsEEnvironmentTemperatureHighStatus,
       "upsEEnvironmentTemperatureLowSetPoint": upsEEnvironmentTemperatureLowSetPoint,
       "upsEEnvironmentTemperatureLowStatus": upsEEnvironmentTemperatureLowStatus,
       "upsEEnvironmentTemperatureOffset": upsEEnvironmentTemperatureOffset,
       "upsEEnvironmentHumidity": upsEEnvironmentHumidity,
       "upsEEnvironmentCurrentHumidity": upsEEnvironmentCurrentHumidity,
       "upsEEnvironmentHumidityHighSetPoint": upsEEnvironmentHumidityHighSetPoint,
       "upsEEnvironmentHumidityHighStatus": upsEEnvironmentHumidityHighStatus,
       "upsEEnvironmentHumidityLowSetPoint": upsEEnvironmentHumidityLowSetPoint,
       "upsEEnvironmentHumidityLowStatus": upsEEnvironmentHumidityLowStatus,
       "upsEEnvironmentHumidityOffset": upsEEnvironmentHumidityOffset,
       "upsEEnvironmentContactsNum": upsEEnvironmentContactsNum,
       "upsEEnvironmentContactTable": upsEEnvironmentContactTable,
       "upsEEnvironmentContactEntry": upsEEnvironmentContactEntry,
       "upsEEnvironmentContactIndex": upsEEnvironmentContactIndex,
       "upsEEnvironmentContactType": upsEEnvironmentContactType,
       "upsEEnvironmentContactState": upsEEnvironmentContactState,
       "upsEEnvironmentContactDescription": upsEEnvironmentContactDescription,
       "upsEBatteryTest": upsEBatteryTest,
       "upsEBatteryTestStart": upsEBatteryTestStart,
       "upsEBatteryTestSettingTime": upsEBatteryTestSettingTime,
       "upsEBatteryTestResult": upsEBatteryTestResult,
       "upsEBatteryTestStartTime": upsEBatteryTestStartTime,
       "upsEBatteryTestElapsedTime": upsEBatteryTestElapsedTime,
       "upsEBatteryTestScheduleTable": upsEBatteryTestScheduleTable,
       "upsEBatteryTestScheduleEntry": upsEBatteryTestScheduleEntry,
       "upsEBatteryTestScheduleIndex": upsEBatteryTestScheduleIndex,
       "upsEBatteryTestScheduleDay": upsEBatteryTestScheduleDay,
       "upsEBatteryTestScheduleTime": upsEBatteryTestScheduleTime,
       "upsEBatteryTestScheduleType": upsEBatteryTestScheduleType,
       "upsEBatteryTestScheduleTestWithTime": upsEBatteryTestScheduleTestWithTime,
       "upsEBatteryTestScheduleSpecialDay": upsEBatteryTestScheduleSpecialDay,
       "upsEControl": upsEControl,
       "upsEControlOutputOffDelay": upsEControlOutputOffDelay,
       "upsEControlOutputOnDelay": upsEControlOutputOnDelay,
       "upsEControlOutputOnOffControl": upsEControlOutputOnOffControl,
       "upsEShutdownEventsTable": upsEShutdownEventsTable,
       "upsEShutdownEventsEntry": upsEShutdownEventsEntry,
       "upsEShutdownEvent": upsEShutdownEvent,
       "upsEShutdownEventAction": upsEShutdownEventAction,
       "upsEShutdownwarningPeriodTime": upsEShutdownwarningPeriodTime,
       "upsEShutdownWarningPeriodInterval": upsEShutdownWarningPeriodInterval,
       "upsEControlWeeklyScheduleTable": upsEControlWeeklyScheduleTable,
       "upsEControlWeeklyScheduleEntry": upsEControlWeeklyScheduleEntry,
       "upsEControlWeeklyScheduleIndex": upsEControlWeeklyScheduleIndex,
       "upsEWeeklyScheduleShutdownDay": upsEWeeklyScheduleShutdownDay,
       "upsEWeeklyScheduleShutdownTime": upsEWeeklyScheduleShutdownTime,
       "upsEWeeklyScheduleRestartDay": upsEWeeklyScheduleRestartDay,
       "upsEWeeklyScheduleRestartTime": upsEWeeklyScheduleRestartTime,
       "upsEControlSpecialDayScheduleTable": upsEControlSpecialDayScheduleTable,
       "upsEControlSpecialDayScheduleEntry": upsEControlSpecialDayScheduleEntry,
       "upsEControlSpecialDayScheduleIndex": upsEControlSpecialDayScheduleIndex,
       "upsESpecialDayScheduleShutdownDay": upsESpecialDayScheduleShutdownDay,
       "upsESpecialDayScheduleShutdownTime": upsESpecialDayScheduleShutdownTime,
       "upsESpecialDayScheduleRestartDay": upsESpecialDayScheduleRestartDay,
       "upsESpecialDayScheduleRestartTime": upsESpecialDayScheduleRestartTime,
       "upsESystemMasterOffDelay": upsESystemMasterOffDelay,
       "upsESystemMasterOnDelay": upsESystemMasterOnDelay,
       "upsETrapControl": upsETrapControl,
       "upsETrapsReceiversTable": upsETrapsReceiversTable,
       "upsETrapsReceiversEntry": upsETrapsReceiversEntry,
       "upsETrapsReceiversIndex": upsETrapsReceiversIndex,
       "upsETrapsReceiverAddress": upsETrapsReceiverAddress,
       "upsETrapReceiverCommunityString": upsETrapReceiverCommunityString,
       "upsETrapType": upsETrapType,
       "upsETrapsSeverityLevel": upsETrapsSeverityLevel,
       "upsETrapReceiverDescription": upsETrapReceiverDescription,
       "upsETrapState": upsETrapState,
       "upsETraps": upsETraps,
       "upsEPowerFail": upsEPowerFail,
       "upsEPowerRestored": upsEPowerRestored,
       "upsELowBattery": upsELowBattery,
       "upsEReturnFromLowBattery": upsEReturnFromLowBattery,
       "upsEFailed": upsEFailed,
       "upsEOk": upsEOk,
       "upsEOnBattery": upsEOnBattery,
       "upsENotOnBattery": upsENotOnBattery,
       "upsETestInProgress": upsETestInProgress,
       "upsETestOver": upsETestOver,
       "upsEBypassOn": upsEBypassOn,
       "upsEOnline": upsEOnline,
       "upsECommunicationLost": upsECommunicationLost,
       "upsECommunicationEstablished": upsECommunicationEstablished,
       "upsEGoingShutdown": upsEGoingShutdown,
       "upsEShutdownCancelled": upsEShutdownCancelled,
       "upsEOutlet1GoingShutdown": upsEOutlet1GoingShutdown,
       "upsEOutlet1ShutdownCancelled": upsEOutlet1ShutdownCancelled,
       "upsEOutlet2GoingShutdown": upsEOutlet2GoingShutdown,
       "upsEOutlet2ShutdownCancelled": upsEOutlet2ShutdownCancelled,
       "upsESleeping": upsESleeping,
       "upsEWokeUp": upsEWokeUp,
       "upsEOverTemperature": upsEOverTemperature,
       "upsENotOverTemperature": upsENotOverTemperature,
       "upsEOverLoad": upsEOverLoad,
       "upsENotOverLoad": upsENotOverLoad,
       "upsEModuleInserted": upsEModuleInserted,
       "upsEModuleRemoved": upsEModuleRemoved,
       "sensorTemperatureTooHigh": sensorTemperatureTooHigh,
       "sensorTemperatureNotHigh": sensorTemperatureNotHigh,
       "sensorTemperatureTooLow": sensorTemperatureTooLow,
       "sensorTemperatureNotLow": sensorTemperatureNotLow,
       "sensorHumidityTooHigh": sensorHumidityTooHigh,
       "sensorHumidityNotHigh": sensorHumidityNotHigh,
       "sensorHumidityTooLow": sensorHumidityTooLow,
       "sensorHumidityNotLow": sensorHumidityNotLow,
       "contactAlarm1Active": contactAlarm1Active,
       "concactAlarm1Normal": concactAlarm1Normal,
       "contactAlarm2Active": contactAlarm2Active,
       "contactAlarm2Normal": contactAlarm2Normal,
       "upsEInternalwarning": upsEInternalwarning,
       "upsEReturnFromInternalwarning": upsEReturnFromInternalwarning,
       "upsEEPOActive": upsEEPOActive,
       "upsEReturnFromEPOActive": upsEReturnFromEPOActive,
       "upsEModuleUnlock": upsEModuleUnlock,
       "upsEReturnFromModuleUnlock": upsEReturnFromModuleUnlock,
       "upsEMain1Neutralloss": upsEMain1Neutralloss,
       "upsEReturnFromMain1Neutralloss": upsEReturnFromMain1Neutralloss,
       "upsEMain1phaseerror": upsEMain1phaseerror,
       "upsEReturnFromMain1phaseerror": upsEReturnFromMain1phaseerror,
       "upsESitefault": upsESitefault,
       "upsEReturnFromSitefault": upsEReturnFromSitefault,
       "upsEBypassAbnormal": upsEBypassAbnormal,
       "upsEReturnFromBypassAbnormal": upsEReturnFromBypassAbnormal,
       "upsEBypassPhaseError": upsEBypassPhaseError,
       "upsEReturnFromBypassPhaseError": upsEReturnFromBypassPhaseError,
       "upsEBatteryOpen": upsEBatteryOpen,
       "upsEReturnFromBatteryOpen": upsEReturnFromBatteryOpen,
       "upsEBatteryOverCharge": upsEBatteryOverCharge,
       "upsEReturnFromBatteryOverCharge": upsEReturnFromBatteryOverCharge,
       "upsEBatteryReverse": upsEBatteryReverse,
       "upsEReturnFromBatteryReverse": upsEReturnFromBatteryReverse,
       "upsEOverloadforewarning": upsEOverloadforewarning,
       "upsEReturnFromOverloadforewarning": upsEReturnFromOverloadforewarning,
       "upsEOverloadWarning": upsEOverloadWarning,
       "upsEReturnFromOverloadWarning": upsEReturnFromOverloadWarning,
       "upsEFanLock": upsEFanLock,
       "upsEReturnFromFanLock": upsEReturnFromFanLock,
       "upsEMaintaincoverisopen": upsEMaintaincoverisopen,
       "upsEReturnFromMaintaincoverisopen": upsEReturnFromMaintaincoverisopen,
       "upsEChargerfault": upsEChargerfault,
       "upsEReturnFromChargerfault": upsEReturnFromChargerfault,
       "upsEModulelocationerror": upsEModulelocationerror,
       "upsEReturnFromModulelocationerror": upsEReturnFromModulelocationerror,
       "upsETurnonabnormal": upsETurnonabnormal,
       "upsEReturnFromTurnonabnormal": upsEReturnFromTurnonabnormal,
       "upsERedundancyloss": upsERedundancyloss,
       "upsEReturnFromRedundancyloss": upsEReturnFromRedundancyloss,
       "upsEHotSwapActived": upsEHotSwapActived,
       "upsEReturnFromHotSwapActived": upsEReturnFromHotSwapActived,
       "upsEBatteryInform": upsEBatteryInform,
       "upsEReturnFromBatteryInform": upsEReturnFromBatteryInform,
       "upsEInspectionInform": upsEInspectionInform,
       "upsEReturnFromInspectionInform": upsEReturnFromInspectionInform,
       "upsEGuaranteeInform": upsEGuaranteeInform,
       "upsEReturnFromGuaranteeInform": upsEReturnFromGuaranteeInform,
       "upsETemperatureLow": upsETemperatureLow,
       "upsEReturnFromTemperatureLow": upsEReturnFromTemperatureLow,
       "upsETemperatureHigh": upsETemperatureHigh,
       "upsEReturnFromTemperatureHigh": upsEReturnFromTemperatureHigh,
       "upsEBatteryOverTemperature": upsEBatteryOverTemperature,
       "upsEReturnFromBatteryOverTemperature": upsEReturnFromBatteryOverTemperature,
       "upsEFanMaintainInform": upsEFanMaintainInform,
       "upsEReturnFromFanMaintainInform": upsEReturnFromFanMaintainInform,
       "upsEBusCapacitanceMaintainInform": upsEBusCapacitanceMaintainInform,
       "upsEReturnFromBusCapacitanceMaintainInform": upsEReturnFromBusCapacitanceMaintainInform,
       "upsESystemOverCapacity": upsESystemOverCapacity,
       "upsEReturnFromSystemOverCapacity": upsEReturnFromSystemOverCapacity,
       "upsEBelowCapacityLimit": upsEBelowCapacityLimit,
       "upsENotBelowCapacityLimit": upsENotBelowCapacityLimit,
       "upsEBelowRemainTimeLimit": upsEBelowRemainTimeLimit,
       "upsENotBelowRemainTimeLimit": upsENotBelowRemainTimeLimit,
       "upsELoadSegment1Off": upsELoadSegment1Off,
       "upsELoadSegment1On": upsELoadSegment1On,
       "upsELoadSegment2Off": upsELoadSegment2Off,
       "upsELoadSegment2On": upsELoadSegment2On}
)
