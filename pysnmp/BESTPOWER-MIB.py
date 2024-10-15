# SNMP MIB module (BESTPOWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BESTPOWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:04 2024
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


# MODULE-IDENTITY


# Types definitions



class NonNegativeInteger(Integer32):
    """Custom type NonNegativeInteger based on Integer32"""




class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BestPower_ObjectIdentity = ObjectIdentity
bestPower = _BestPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947)
)
_BestLink_ObjectIdentity = ObjectIdentity
bestLink = _BestLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 1)
)


class _UpsIdentUpsName_Type(DisplayString):
    """Custom type upsIdentUpsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_UpsIdentUpsName_Type.__name__ = "DisplayString"
_UpsIdentUpsName_Object = MibScalar
upsIdentUpsName = _UpsIdentUpsName_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 1, 1),
    _UpsIdentUpsName_Type()
)
upsIdentUpsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUpsName.setStatus("mandatory")


class _UpsIdentModel_Type(DisplayString):
    """Custom type upsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_UpsIdentModel_Type.__name__ = "DisplayString"
_UpsIdentModel_Object = MibScalar
upsIdentModel = _UpsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 1, 2),
    _UpsIdentModel_Type()
)
upsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModel.setStatus("mandatory")
_UpsIdentVARating_Type = DisplayString
_UpsIdentVARating_Object = MibScalar
upsIdentVARating = _UpsIdentVARating_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 1, 3),
    _UpsIdentVARating_Type()
)
upsIdentVARating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentVARating.setStatus("mandatory")


class _UpsIdentUpsType_Type(Integer32):
    """Custom type upsIdentUpsType based on Integer32"""
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
        *(("hybrid", 5),
          ("lineInteractive", 4),
          ("offline", 3),
          ("online", 2),
          ("standby", 1))
    )


_UpsIdentUpsType_Type.__name__ = "Integer32"
_UpsIdentUpsType_Object = MibScalar
upsIdentUpsType = _UpsIdentUpsType_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 1, 4),
    _UpsIdentUpsType_Type()
)
upsIdentUpsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUpsType.setStatus("mandatory")
_UpsIdentUpsSerialNumber_Type = DisplayString
_UpsIdentUpsSerialNumber_Object = MibScalar
upsIdentUpsSerialNumber = _UpsIdentUpsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 1, 5),
    _UpsIdentUpsSerialNumber_Type()
)
upsIdentUpsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUpsSerialNumber.setStatus("mandatory")
_UpsIdentUpsIdentification_Type = DisplayString
_UpsIdentUpsIdentification_Object = MibScalar
upsIdentUpsIdentification = _UpsIdentUpsIdentification_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 1, 6),
    _UpsIdentUpsIdentification_Type()
)
upsIdentUpsIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentUpsIdentification.setStatus("mandatory")


class _UpsIdentFirmwareRevision_Type(DisplayString):
    """Custom type upsIdentFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_UpsIdentFirmwareRevision_Type.__name__ = "DisplayString"
_UpsIdentFirmwareRevision_Object = MibScalar
upsIdentFirmwareRevision = _UpsIdentFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 1, 7),
    _UpsIdentFirmwareRevision_Type()
)
upsIdentFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentFirmwareRevision.setStatus("mandatory")


class _UpsIdentDateOfManufacture_Type(DisplayString):
    """Custom type upsIdentDateOfManufacture based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 10),
    )


_UpsIdentDateOfManufacture_Type.__name__ = "DisplayString"
_UpsIdentDateOfManufacture_Object = MibScalar
upsIdentDateOfManufacture = _UpsIdentDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 1, 8),
    _UpsIdentDateOfManufacture_Type()
)
upsIdentDateOfManufacture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentDateOfManufacture.setStatus("mandatory")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 2)
)


class _UpsBatteryStatus_Type(Integer32):
    """Custom type upsBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverterOff", 1),
          ("inverterOn", 2))
    )


_UpsBatteryStatus_Type.__name__ = "Integer32"
_UpsBatteryStatus_Object = MibScalar
upsBatteryStatus = _UpsBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 2, 1),
    _UpsBatteryStatus_Type()
)
upsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatus.setStatus("mandatory")
_UpsBatteryTimeOnBattery_Type = Integer32
_UpsBatteryTimeOnBattery_Object = MibScalar
upsBatteryTimeOnBattery = _UpsBatteryTimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 2, 2),
    _UpsBatteryTimeOnBattery_Type()
)
upsBatteryTimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTimeOnBattery.setStatus("mandatory")
_UpsBatteryRuntimeRemaining_Type = Integer32
_UpsBatteryRuntimeRemaining_Object = MibScalar
upsBatteryRuntimeRemaining = _UpsBatteryRuntimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 2, 3),
    _UpsBatteryRuntimeRemaining_Type()
)
upsBatteryRuntimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRuntimeRemaining.setStatus("mandatory")
_UpsBatteryVoltage_Type = Integer32
_UpsBatteryVoltage_Object = MibScalar
upsBatteryVoltage = _UpsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 2, 4),
    _UpsBatteryVoltage_Type()
)
upsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setStatus("mandatory")
_UpsBatteryCurrent_Type = Integer32
_UpsBatteryCurrent_Object = MibScalar
upsBatteryCurrent = _UpsBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 2, 5),
    _UpsBatteryCurrent_Type()
)
upsBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrent.setStatus("mandatory")
_UpsBatteryTemperature_Type = Integer32
_UpsBatteryTemperature_Object = MibScalar
upsBatteryTemperature = _UpsBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 2, 6),
    _UpsBatteryTemperature_Type()
)
upsBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperature.setStatus("mandatory")


class _UpsBatteryLastReplaceDate_Type(DisplayString):
    """Custom type upsBatteryLastReplaceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 10),
    )


_UpsBatteryLastReplaceDate_Type.__name__ = "DisplayString"
_UpsBatteryLastReplaceDate_Object = MibScalar
upsBatteryLastReplaceDate = _UpsBatteryLastReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 2, 7),
    _UpsBatteryLastReplaceDate_Type()
)
upsBatteryLastReplaceDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryLastReplaceDate.setStatus("mandatory")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3)
)
_UpsInputPhase_Type = Integer32
_UpsInputPhase_Object = MibScalar
upsInputPhase = _UpsInputPhase_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 1),
    _UpsInputPhase_Type()
)
upsInputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputPhase.setStatus("mandatory")
_UpsInputFrequency_Type = Integer32
_UpsInputFrequency_Object = MibScalar
upsInputFrequency = _UpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 2),
    _UpsInputFrequency_Type()
)
upsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency.setStatus("mandatory")
_UpsInputVoltage_Type = Integer32
_UpsInputVoltage_Object = MibScalar
upsInputVoltage = _UpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 3),
    _UpsInputVoltage_Type()
)
upsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage.setStatus("mandatory")
_UpsInputCurrent_Type = Integer32
_UpsInputCurrent_Object = MibScalar
upsInputCurrent = _UpsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 4),
    _UpsInputCurrent_Type()
)
upsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrent.setStatus("mandatory")
_UpsInputPower_Type = Integer32
_UpsInputPower_Object = MibScalar
upsInputPower = _UpsInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 5),
    _UpsInputPower_Type()
)
upsInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputPower.setStatus("mandatory")
_UpsInputPhase2_ObjectIdentity = ObjectIdentity
upsInputPhase2 = _UpsInputPhase2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 6)
)
_UpsInputP2_Type = Integer32
_UpsInputP2_Object = MibScalar
upsInputP2 = _UpsInputP2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 6, 1),
    _UpsInputP2_Type()
)
upsInputP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputP2.setStatus("mandatory")
_UpsInputFrequency2_Type = Integer32
_UpsInputFrequency2_Object = MibScalar
upsInputFrequency2 = _UpsInputFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 6, 2),
    _UpsInputFrequency2_Type()
)
upsInputFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency2.setStatus("mandatory")
_UpsInputVoltage2_Type = Integer32
_UpsInputVoltage2_Object = MibScalar
upsInputVoltage2 = _UpsInputVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 6, 3),
    _UpsInputVoltage2_Type()
)
upsInputVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage2.setStatus("mandatory")
_UpsInputCurrent2_Type = Integer32
_UpsInputCurrent2_Object = MibScalar
upsInputCurrent2 = _UpsInputCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 6, 4),
    _UpsInputCurrent2_Type()
)
upsInputCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrent2.setStatus("mandatory")
_UpsInputPower2_Type = Integer32
_UpsInputPower2_Object = MibScalar
upsInputPower2 = _UpsInputPower2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 6, 5),
    _UpsInputPower2_Type()
)
upsInputPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputPower2.setStatus("mandatory")
_UpsInputPhase3_ObjectIdentity = ObjectIdentity
upsInputPhase3 = _UpsInputPhase3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 7)
)
_UpsInputP3_Type = Integer32
_UpsInputP3_Object = MibScalar
upsInputP3 = _UpsInputP3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 7, 1),
    _UpsInputP3_Type()
)
upsInputP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputP3.setStatus("mandatory")
_UpsInputFrequency3_Type = Integer32
_UpsInputFrequency3_Object = MibScalar
upsInputFrequency3 = _UpsInputFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 7, 2),
    _UpsInputFrequency3_Type()
)
upsInputFrequency3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency3.setStatus("mandatory")
_UpsInputVoltage3_Type = Integer32
_UpsInputVoltage3_Object = MibScalar
upsInputVoltage3 = _UpsInputVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 7, 3),
    _UpsInputVoltage3_Type()
)
upsInputVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage3.setStatus("mandatory")
_UpsInputCurrent3_Type = Integer32
_UpsInputCurrent3_Object = MibScalar
upsInputCurrent3 = _UpsInputCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 7, 4),
    _UpsInputCurrent3_Type()
)
upsInputCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrent3.setStatus("mandatory")
_UpsInputPower3_Type = Integer32
_UpsInputPower3_Object = MibScalar
upsInputPower3 = _UpsInputPower3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 3, 7, 5),
    _UpsInputPower3_Type()
)
upsInputPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputPower3.setStatus("mandatory")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4)
)


class _UpsOutputStatus_Type(Integer32):
    """Custom type upsOutputStatus based on Integer32"""
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
        *(("onBattery", 3),
          ("onBypass", 4),
          ("onLine", 2),
          ("unknown", 1))
    )


_UpsOutputStatus_Type.__name__ = "Integer32"
_UpsOutputStatus_Object = MibScalar
upsOutputStatus = _UpsOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 1),
    _UpsOutputStatus_Type()
)
upsOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputStatus.setStatus("mandatory")
_UpsOutputPhase_Type = Integer32
_UpsOutputPhase_Object = MibScalar
upsOutputPhase = _UpsOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 2),
    _UpsOutputPhase_Type()
)
upsOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPhase.setStatus("mandatory")
_UpsOutputFrequency_Type = Integer32
_UpsOutputFrequency_Object = MibScalar
upsOutputFrequency = _UpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 3),
    _UpsOutputFrequency_Type()
)
upsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency.setStatus("mandatory")
_UpsOutputVoltage_Type = Integer32
_UpsOutputVoltage_Object = MibScalar
upsOutputVoltage = _UpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 4),
    _UpsOutputVoltage_Type()
)
upsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage.setStatus("mandatory")
_UpsOutputCurrent_Type = NonNegativeInteger
_UpsOutputCurrent_Object = MibScalar
upsOutputCurrent = _UpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 5),
    _UpsOutputCurrent_Type()
)
upsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrent.setStatus("mandatory")
_UpsOutputTruePower_Type = NonNegativeInteger
_UpsOutputTruePower_Object = MibScalar
upsOutputTruePower = _UpsOutputTruePower_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 6),
    _UpsOutputTruePower_Type()
)
upsOutputTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputTruePower.setStatus("mandatory")
_UpsOutputApparentPower_Type = NonNegativeInteger
_UpsOutputApparentPower_Object = MibScalar
upsOutputApparentPower = _UpsOutputApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 7),
    _UpsOutputApparentPower_Type()
)
upsOutputApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputApparentPower.setStatus("mandatory")
_UpsOutputPowerFactor_Type = Integer32
_UpsOutputPowerFactor_Object = MibScalar
upsOutputPowerFactor = _UpsOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 8),
    _UpsOutputPowerFactor_Type()
)
upsOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactor.setStatus("mandatory")
_UpsOutputPercentLoad_Type = Integer32
_UpsOutputPercentLoad_Object = MibScalar
upsOutputPercentLoad = _UpsOutputPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 9),
    _UpsOutputPercentLoad_Type()
)
upsOutputPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoad.setStatus("mandatory")
_UpsOutputPhase2_ObjectIdentity = ObjectIdentity
upsOutputPhase2 = _UpsOutputPhase2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 10)
)
_UpsOutputP2_Type = Integer32
_UpsOutputP2_Object = MibScalar
upsOutputP2 = _UpsOutputP2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 10, 1),
    _UpsOutputP2_Type()
)
upsOutputP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputP2.setStatus("mandatory")
_UpsOutputFrequency2_Type = Integer32
_UpsOutputFrequency2_Object = MibScalar
upsOutputFrequency2 = _UpsOutputFrequency2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 10, 2),
    _UpsOutputFrequency2_Type()
)
upsOutputFrequency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency2.setStatus("mandatory")
_UpsOutputVoltage2_Type = Integer32
_UpsOutputVoltage2_Object = MibScalar
upsOutputVoltage2 = _UpsOutputVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 10, 3),
    _UpsOutputVoltage2_Type()
)
upsOutputVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage2.setStatus("mandatory")
_UpsOutputCurrent2_Type = NonNegativeInteger
_UpsOutputCurrent2_Object = MibScalar
upsOutputCurrent2 = _UpsOutputCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 10, 4),
    _UpsOutputCurrent2_Type()
)
upsOutputCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrent2.setStatus("mandatory")
_UpsOutputTruePower2_Type = NonNegativeInteger
_UpsOutputTruePower2_Object = MibScalar
upsOutputTruePower2 = _UpsOutputTruePower2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 10, 5),
    _UpsOutputTruePower2_Type()
)
upsOutputTruePower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputTruePower2.setStatus("mandatory")
_UpsOutputApparentPower2_Type = NonNegativeInteger
_UpsOutputApparentPower2_Object = MibScalar
upsOutputApparentPower2 = _UpsOutputApparentPower2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 10, 6),
    _UpsOutputApparentPower2_Type()
)
upsOutputApparentPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputApparentPower2.setStatus("mandatory")
_UpsOutputPowerFactor2_Type = Integer32
_UpsOutputPowerFactor2_Object = MibScalar
upsOutputPowerFactor2 = _UpsOutputPowerFactor2_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 10, 7),
    _UpsOutputPowerFactor2_Type()
)
upsOutputPowerFactor2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactor2.setStatus("mandatory")
_UpsOutputPhase3_ObjectIdentity = ObjectIdentity
upsOutputPhase3 = _UpsOutputPhase3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 11)
)
_UpsOutputP3_Type = Integer32
_UpsOutputP3_Object = MibScalar
upsOutputP3 = _UpsOutputP3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 11, 1),
    _UpsOutputP3_Type()
)
upsOutputP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputP3.setStatus("mandatory")
_UpsOutputFrequency3_Type = Integer32
_UpsOutputFrequency3_Object = MibScalar
upsOutputFrequency3 = _UpsOutputFrequency3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 11, 2),
    _UpsOutputFrequency3_Type()
)
upsOutputFrequency3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency3.setStatus("mandatory")
_UpsOutputVoltage3_Type = Integer32
_UpsOutputVoltage3_Object = MibScalar
upsOutputVoltage3 = _UpsOutputVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 11, 3),
    _UpsOutputVoltage3_Type()
)
upsOutputVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage3.setStatus("mandatory")
_UpsOutputCurrent3_Type = NonNegativeInteger
_UpsOutputCurrent3_Object = MibScalar
upsOutputCurrent3 = _UpsOutputCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 11, 4),
    _UpsOutputCurrent3_Type()
)
upsOutputCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrent3.setStatus("mandatory")
_UpsOutputTruePower3_Type = NonNegativeInteger
_UpsOutputTruePower3_Object = MibScalar
upsOutputTruePower3 = _UpsOutputTruePower3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 11, 5),
    _UpsOutputTruePower3_Type()
)
upsOutputTruePower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputTruePower3.setStatus("mandatory")
_UpsOutputApparentPower3_Type = NonNegativeInteger
_UpsOutputApparentPower3_Object = MibScalar
upsOutputApparentPower3 = _UpsOutputApparentPower3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 11, 6),
    _UpsOutputApparentPower3_Type()
)
upsOutputApparentPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputApparentPower3.setStatus("mandatory")
_UpsOutputPowerFactor3_Type = Integer32
_UpsOutputPowerFactor3_Object = MibScalar
upsOutputPowerFactor3 = _UpsOutputPowerFactor3_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 4, 11, 7),
    _UpsOutputPowerFactor3_Type()
)
upsOutputPowerFactor3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactor3.setStatus("mandatory")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5)
)
_UpsConfigLowRuntimeSetpoint_Type = Integer32
_UpsConfigLowRuntimeSetpoint_Object = MibScalar
upsConfigLowRuntimeSetpoint = _UpsConfigLowRuntimeSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 1),
    _UpsConfigLowRuntimeSetpoint_Type()
)
upsConfigLowRuntimeSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowRuntimeSetpoint.setStatus("mandatory")
_UpsConfigDelayBeforeRestart_Type = Integer32
_UpsConfigDelayBeforeRestart_Object = MibScalar
upsConfigDelayBeforeRestart = _UpsConfigDelayBeforeRestart_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 2),
    _UpsConfigDelayBeforeRestart_Type()
)
upsConfigDelayBeforeRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigDelayBeforeRestart.setStatus("mandatory")
_UpsConfigDelayBeforeShutdown_Type = Integer32
_UpsConfigDelayBeforeShutdown_Object = MibScalar
upsConfigDelayBeforeShutdown = _UpsConfigDelayBeforeShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 3),
    _UpsConfigDelayBeforeShutdown_Type()
)
upsConfigDelayBeforeShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigDelayBeforeShutdown.setStatus("mandatory")
_UpsConfigTest_ObjectIdentity = ObjectIdentity
upsConfigTest = _UpsConfigTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 4)
)


class _UpsConfigTestLevel_Type(Integer32):
    """Custom type upsConfigTestLevel based on Integer32"""
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
        *(("battery", 4),
          ("inverter", 3),
          ("logic", 2),
          ("none", 1))
    )


_UpsConfigTestLevel_Type.__name__ = "Integer32"
_UpsConfigTestLevel_Object = MibScalar
upsConfigTestLevel = _UpsConfigTestLevel_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 4, 1),
    _UpsConfigTestLevel_Type()
)
upsConfigTestLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigTestLevel.setStatus("mandatory")


class _UpsConfigDaysBetweenTests_Type(Integer32):
    """Custom type upsConfigDaysBetweenTests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 366),
    )


_UpsConfigDaysBetweenTests_Type.__name__ = "Integer32"
_UpsConfigDaysBetweenTests_Object = MibScalar
upsConfigDaysBetweenTests = _UpsConfigDaysBetweenTests_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 4, 3),
    _UpsConfigDaysBetweenTests_Type()
)
upsConfigDaysBetweenTests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigDaysBetweenTests.setStatus("mandatory")


class _UpsConfigBatteryTestDuration_Type(Integer32):
    """Custom type upsConfigBatteryTestDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_UpsConfigBatteryTestDuration_Type.__name__ = "Integer32"
_UpsConfigBatteryTestDuration_Object = MibScalar
upsConfigBatteryTestDuration = _UpsConfigBatteryTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 4, 4),
    _UpsConfigBatteryTestDuration_Type()
)
upsConfigBatteryTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryTestDuration.setStatus("mandatory")
_UpsConfigScheduleTable_Object = MibTable
upsConfigScheduleTable = _UpsConfigScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 5)
)
if mibBuilder.loadTexts:
    upsConfigScheduleTable.setStatus("mandatory")
_UpsConfigScheduleEntry_Object = MibTableRow
upsConfigScheduleEntry = _UpsConfigScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 5, 1)
)
upsConfigScheduleEntry.setIndexNames(
    (0, "BESTPOWER-MIB", "upsConfigScheduleIndex"),
)
if mibBuilder.loadTexts:
    upsConfigScheduleEntry.setStatus("mandatory")
_UpsConfigScheduleIndex_Type = Integer32
_UpsConfigScheduleIndex_Object = MibTableColumn
upsConfigScheduleIndex = _UpsConfigScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 5, 1, 1),
    _UpsConfigScheduleIndex_Type()
)
upsConfigScheduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigScheduleIndex.setStatus("mandatory")


class _UpsConfigScheduleShutdownDay_Type(Integer32):
    """Custom type upsConfigScheduleShutdownDay based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("none", 8),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UpsConfigScheduleShutdownDay_Type.__name__ = "Integer32"
_UpsConfigScheduleShutdownDay_Object = MibTableColumn
upsConfigScheduleShutdownDay = _UpsConfigScheduleShutdownDay_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 5, 1, 2),
    _UpsConfigScheduleShutdownDay_Type()
)
upsConfigScheduleShutdownDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigScheduleShutdownDay.setStatus("mandatory")
_UpsConfigScheduleShutdownTime_Type = DisplayString
_UpsConfigScheduleShutdownTime_Object = MibTableColumn
upsConfigScheduleShutdownTime = _UpsConfigScheduleShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 5, 1, 3),
    _UpsConfigScheduleShutdownTime_Type()
)
upsConfigScheduleShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigScheduleShutdownTime.setStatus("mandatory")


class _UpsConfigScheduleRestartDay_Type(Integer32):
    """Custom type upsConfigScheduleRestartDay based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("none", 8),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UpsConfigScheduleRestartDay_Type.__name__ = "Integer32"
_UpsConfigScheduleRestartDay_Object = MibTableColumn
upsConfigScheduleRestartDay = _UpsConfigScheduleRestartDay_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 5, 1, 4),
    _UpsConfigScheduleRestartDay_Type()
)
upsConfigScheduleRestartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigScheduleRestartDay.setStatus("mandatory")
_UpsConfigScheduleRestartTime_Type = DisplayString
_UpsConfigScheduleRestartTime_Object = MibTableColumn
upsConfigScheduleRestartTime = _UpsConfigScheduleRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 5, 1, 5),
    _UpsConfigScheduleRestartTime_Type()
)
upsConfigScheduleRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigScheduleRestartTime.setStatus("mandatory")
_UpsConfigbestLink_ObjectIdentity = ObjectIdentity
upsConfigbestLink = _UpsConfigbestLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8)
)
_BestLinkHistoryLogFrequency_Type = Integer32
_BestLinkHistoryLogFrequency_Object = MibScalar
bestLinkHistoryLogFrequency = _BestLinkHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 1),
    _BestLinkHistoryLogFrequency_Type()
)
bestLinkHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkHistoryLogFrequency.setStatus("mandatory")
_BestLinkRefreshFrequency_Type = Integer32
_BestLinkRefreshFrequency_Object = MibScalar
bestLinkRefreshFrequency = _BestLinkRefreshFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 2),
    _BestLinkRefreshFrequency_Type()
)
bestLinkRefreshFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkRefreshFrequency.setStatus("mandatory")
_BestLinkNetId_Type = IpAddress
_BestLinkNetId_Object = MibScalar
bestLinkNetId = _BestLinkNetId_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 3),
    _BestLinkNetId_Type()
)
bestLinkNetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkNetId.setStatus("mandatory")
_BestLinkGateway_Type = IpAddress
_BestLinkGateway_Object = MibScalar
bestLinkGateway = _BestLinkGateway_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 4),
    _BestLinkGateway_Type()
)
bestLinkGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkGateway.setStatus("mandatory")
_BestLinkNetMask_Type = IpAddress
_BestLinkNetMask_Object = MibScalar
bestLinkNetMask = _BestLinkNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 5),
    _BestLinkNetMask_Type()
)
bestLinkNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkNetMask.setStatus("mandatory")


class _BestLinkSysDate_Type(DisplayString):
    """Custom type bestLinkSysDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 10),
    )


_BestLinkSysDate_Type.__name__ = "DisplayString"
_BestLinkSysDate_Object = MibScalar
bestLinkSysDate = _BestLinkSysDate_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 6),
    _BestLinkSysDate_Type()
)
bestLinkSysDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkSysDate.setStatus("mandatory")


class _BestLinkSysTime_Type(DisplayString):
    """Custom type bestLinkSysTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 8),
    )


_BestLinkSysTime_Type.__name__ = "DisplayString"
_BestLinkSysTime_Object = MibScalar
bestLinkSysTime = _BestLinkSysTime_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 7),
    _BestLinkSysTime_Type()
)
bestLinkSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkSysTime.setStatus("mandatory")


class _BestLinkTftpFileName_Type(DisplayString):
    """Custom type bestLinkTftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 59),
    )


_BestLinkTftpFileName_Type.__name__ = "DisplayString"
_BestLinkTftpFileName_Object = MibScalar
bestLinkTftpFileName = _BestLinkTftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 8),
    _BestLinkTftpFileName_Type()
)
bestLinkTftpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkTftpFileName.setStatus("mandatory")
_BestLinkTftpHost_Type = IpAddress
_BestLinkTftpHost_Object = MibScalar
bestLinkTftpHost = _BestLinkTftpHost_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 9),
    _BestLinkTftpHost_Type()
)
bestLinkTftpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkTftpHost.setStatus("mandatory")


class _BestLinkFlashEEPROM_Type(Integer32):
    """Custom type bestLinkFlashEEPROM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BestLinkFlashEEPROM_Type.__name__ = "Integer32"
_BestLinkFlashEEPROM_Object = MibScalar
bestLinkFlashEEPROM = _BestLinkFlashEEPROM_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 10),
    _BestLinkFlashEEPROM_Type()
)
bestLinkFlashEEPROM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkFlashEEPROM.setStatus("mandatory")
_BestLinkPrimaryTimeServer_Type = IpAddress
_BestLinkPrimaryTimeServer_Object = MibScalar
bestLinkPrimaryTimeServer = _BestLinkPrimaryTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 11),
    _BestLinkPrimaryTimeServer_Type()
)
bestLinkPrimaryTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkPrimaryTimeServer.setStatus("mandatory")
_BestLinkSecondaryTimeServer_Type = IpAddress
_BestLinkSecondaryTimeServer_Object = MibScalar
bestLinkSecondaryTimeServer = _BestLinkSecondaryTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 12),
    _BestLinkSecondaryTimeServer_Type()
)
bestLinkSecondaryTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bestLinkSecondaryTimeServer.setStatus("mandatory")
_BestLinkSoftwareVersion_Type = DisplayString
_BestLinkSoftwareVersion_Object = MibScalar
bestLinkSoftwareVersion = _BestLinkSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 8, 13),
    _BestLinkSoftwareVersion_Type()
)
bestLinkSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bestLinkSoftwareVersion.setStatus("mandatory")
_UpsConfigTrapsReceivers_ObjectIdentity = ObjectIdentity
upsConfigTrapsReceivers = _UpsConfigTrapsReceivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 9)
)
_UpsConfigTrapsReceiversTable_Object = MibTable
upsConfigTrapsReceiversTable = _UpsConfigTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 9, 1)
)
if mibBuilder.loadTexts:
    upsConfigTrapsReceiversTable.setStatus("mandatory")
_UpsConfigTrapsReceiversEntry_Object = MibTableRow
upsConfigTrapsReceiversEntry = _UpsConfigTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 9, 1, 1)
)
upsConfigTrapsReceiversEntry.setIndexNames(
    (0, "BESTPOWER-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    upsConfigTrapsReceiversEntry.setStatus("mandatory")
_TrapsIndex_Type = Integer32
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 9, 1, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("mandatory")
_TrapsReceiverAddr_Type = IpAddress
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 9, 1, 1, 2),
    _TrapsReceiverAddr_Type()
)
trapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsReceiverAddr.setStatus("mandatory")


class _ReceiverCommunityString_Type(DisplayString):
    """Custom type receiverCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ReceiverCommunityString_Type.__name__ = "DisplayString"
_ReceiverCommunityString_Object = MibTableColumn
receiverCommunityString = _ReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 9, 1, 1, 3),
    _ReceiverCommunityString_Type()
)
receiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverCommunityString.setStatus("mandatory")


class _SeverityLevel_Type(Integer32):
    """Custom type severityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("information", 1),
          ("severe", 3),
          ("warning", 2))
    )


_SeverityLevel_Type.__name__ = "Integer32"
_SeverityLevel_Object = MibTableColumn
severityLevel = _SeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 9, 1, 1, 4),
    _SeverityLevel_Type()
)
severityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    severityLevel.setStatus("mandatory")


class _ReceiverAccept_Type(Integer32):
    """Custom type receiverAccept based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_ReceiverAccept_Type.__name__ = "Integer32"
_ReceiverAccept_Object = MibTableColumn
receiverAccept = _ReceiverAccept_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 9, 1, 1, 5),
    _ReceiverAccept_Type()
)
receiverAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverAccept.setStatus("mandatory")
_UpsConfigRegisteredShutdownClients_ObjectIdentity = ObjectIdentity
upsConfigRegisteredShutdownClients = _UpsConfigRegisteredShutdownClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 10)
)
_UpsRegisteredShutdownClientsTable_Object = MibTable
upsRegisteredShutdownClientsTable = _UpsRegisteredShutdownClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 10, 1)
)
if mibBuilder.loadTexts:
    upsRegisteredShutdownClientsTable.setStatus("mandatory")
_UpsRegisteredShutdownClientsEntry_Object = MibTableRow
upsRegisteredShutdownClientsEntry = _UpsRegisteredShutdownClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 10, 1, 1)
)
upsRegisteredShutdownClientsEntry.setIndexNames(
    (0, "BESTPOWER-MIB", "upsRegisteredShutdownClientsIndex"),
)
if mibBuilder.loadTexts:
    upsRegisteredShutdownClientsEntry.setStatus("mandatory")
_UpsRegisteredShutdownClientsIndex_Type = PositiveInteger
_UpsRegisteredShutdownClientsIndex_Object = MibTableColumn
upsRegisteredShutdownClientsIndex = _UpsRegisteredShutdownClientsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 10, 1, 1, 1),
    _UpsRegisteredShutdownClientsIndex_Type()
)
upsRegisteredShutdownClientsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRegisteredShutdownClientsIndex.setStatus("mandatory")
_UpsRegisteredShutdownClientsIPAddress_Type = IpAddress
_UpsRegisteredShutdownClientsIPAddress_Object = MibTableColumn
upsRegisteredShutdownClientsIPAddress = _UpsRegisteredShutdownClientsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 10, 1, 1, 2),
    _UpsRegisteredShutdownClientsIPAddress_Type()
)
upsRegisteredShutdownClientsIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRegisteredShutdownClientsIPAddress.setStatus("mandatory")
_UpsRegisteredShutdownClientsTotalNumberOf_Type = Integer32
_UpsRegisteredShutdownClientsTotalNumberOf_Object = MibScalar
upsRegisteredShutdownClientsTotalNumberOf = _UpsRegisteredShutdownClientsTotalNumberOf_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 5, 10, 2),
    _UpsRegisteredShutdownClientsTotalNumberOf_Type()
)
upsRegisteredShutdownClientsTotalNumberOf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRegisteredShutdownClientsTotalNumberOf.setStatus("mandatory")
_UpsControl_ObjectIdentity = ObjectIdentity
upsControl = _UpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 6)
)


class _UpsControlTurnOffUPS_Type(Integer32):
    """Custom type upsControlTurnOffUPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cancelUpsOff", 1),
          ("cancelrebootUps", 7),
          ("rebootUps", 3),
          ("upsOff", 2))
    )


_UpsControlTurnOffUPS_Type.__name__ = "Integer32"
_UpsControlTurnOffUPS_Object = MibScalar
upsControlTurnOffUPS = _UpsControlTurnOffUPS_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 6, 1),
    _UpsControlTurnOffUPS_Type()
)
upsControlTurnOffUPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlTurnOffUPS.setStatus("mandatory")


class _UpsControlActivateUpsScheduling_Type(Integer32):
    """Custom type upsControlActivateUpsScheduling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_UpsControlActivateUpsScheduling_Type.__name__ = "Integer32"
_UpsControlActivateUpsScheduling_Object = MibScalar
upsControlActivateUpsScheduling = _UpsControlActivateUpsScheduling_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 6, 4),
    _UpsControlActivateUpsScheduling_Type()
)
upsControlActivateUpsScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlActivateUpsScheduling.setStatus("mandatory")
_UpsTest_ObjectIdentity = ObjectIdentity
upsTest = _UpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 7)
)


class _UpsManualTests_Type(Integer32):
    """Custom type upsManualTests based on Integer32"""
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
        *(("abortManualBatteryTest", 9),
          ("abortManualBeeperTest", 6),
          ("abortManualInverterTest", 8),
          ("abortManualSystemTest", 7),
          ("initiateManualBatteryTest", 5),
          ("initiateManualBeeperTest", 2),
          ("initiateManualInverterTest", 4),
          ("initiateManualSystemTest", 3),
          ("noTestInitiated", 1))
    )


_UpsManualTests_Type.__name__ = "Integer32"
_UpsManualTests_Object = MibScalar
upsManualTests = _UpsManualTests_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 7, 1),
    _UpsManualTests_Type()
)
upsManualTests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsManualTests.setStatus("mandatory")
_UpsAlarm_ObjectIdentity = ObjectIdentity
upsAlarm = _UpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8)
)
_UpsAlarmsPresent_Type = Gauge32
_UpsAlarmsPresent_Object = MibScalar
upsAlarmsPresent = _UpsAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 1),
    _UpsAlarmsPresent_Type()
)
upsAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresent.setStatus("mandatory")


class _UpsLastKnownAlarm_Type(Integer32):
    """Custom type upsLastKnownAlarm based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("autoBypass", 15),
          ("batteriesDisconnected", 9),
          ("bypassOn", 14),
          ("callService", 29),
          ("checkBattery", 6),
          ("checkFan", 17),
          ("checkFuse", 26),
          ("checkInverter", 8),
          ("checkMOV", 27),
          ("checkPowerSupply", 23),
          ("circuitBreakerShdn", 13),
          ("circuitBreakerWarning", 12),
          ("communicationsLost", 36),
          ("diagnosticTestFailed", 33),
          ("ePO", 34),
          ("highAmbTemp", 18),
          ("highBattery", 5),
          ("highHSTemp", 19),
          ("highPFMTemp", 21),
          ("highXFMRTemp", 20),
          ("lowAcOut", 11),
          ("lowBattery", 4),
          ("lowRuntime", 2),
          ("memoryError", 28),
          ("nearLowBattery", 3),
          ("noAlarm", 37),
          ("onBattery", 1),
          ("outputOverload", 10),
          ("probeMissing", 22),
          ("relayFailure", 25),
          ("replaceBattery", 7),
          ("siteWiringFault", 16),
          ("tapRegulator", 24),
          ("testInProgress", 32),
          ("upsFailed", 30),
          ("upsOff", 35),
          ("userTest", 31))
    )


_UpsLastKnownAlarm_Type.__name__ = "Integer32"
_UpsLastKnownAlarm_Object = MibScalar
upsLastKnownAlarm = _UpsLastKnownAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 2),
    _UpsLastKnownAlarm_Type()
)
upsLastKnownAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsLastKnownAlarm.setStatus("mandatory")
_UpsAlarmTable_Object = MibTable
upsAlarmTable = _UpsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 3)
)
if mibBuilder.loadTexts:
    upsAlarmTable.setStatus("mandatory")
_UpsAlarmEntry_Object = MibTableRow
upsAlarmEntry = _UpsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 3, 1)
)
upsAlarmEntry.setIndexNames(
    (0, "BESTPOWER-MIB", "upsAlarmIndex"),
)
if mibBuilder.loadTexts:
    upsAlarmEntry.setStatus("mandatory")
_UpsAlarmIndex_Type = PositiveInteger
_UpsAlarmIndex_Object = MibTableColumn
upsAlarmIndex = _UpsAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 3, 1, 1),
    _UpsAlarmIndex_Type()
)
upsAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmIndex.setStatus("mandatory")


class _UpsAlarmName_Type(Integer32):
    """Custom type upsAlarmName based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("autoBypass", 15),
          ("batteriesDisconnected", 9),
          ("bypassOn", 14),
          ("callService", 29),
          ("checkBattery", 6),
          ("checkFan", 17),
          ("checkFuse", 26),
          ("checkInverter", 8),
          ("checkMOV", 27),
          ("checkPowerSupply", 23),
          ("circuitBreakerShdn", 13),
          ("circuitBreakerWarning", 12),
          ("communicationsLost", 36),
          ("diagnosticTestFailed", 33),
          ("ePO", 34),
          ("highAmbTemp", 18),
          ("highBattery", 5),
          ("highHSTemp", 19),
          ("highPFMTemp", 21),
          ("highXFMRTemp", 20),
          ("lowAcOut", 11),
          ("lowBattery", 4),
          ("lowRuntime", 2),
          ("memoryError", 28),
          ("nearLowBattery", 3),
          ("onBattery", 1),
          ("outputOverload", 10),
          ("probeMissing", 22),
          ("relayFailure", 25),
          ("replaceBattery", 7),
          ("siteWiringFault", 16),
          ("tapRegulator", 24),
          ("testInProgress", 32),
          ("upsFailed", 30),
          ("upsOff", 35),
          ("userTest", 31))
    )


_UpsAlarmName_Type.__name__ = "Integer32"
_UpsAlarmName_Object = MibTableColumn
upsAlarmName = _UpsAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 3, 1, 2),
    _UpsAlarmName_Type()
)
upsAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmName.setStatus("mandatory")
_UpsAlarmTime_Type = DisplayString
_UpsAlarmTime_Object = MibTableColumn
upsAlarmTime = _UpsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 3, 1, 3),
    _UpsAlarmTime_Type()
)
upsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTime.setStatus("mandatory")
_UpsWellKnownAlarms_ObjectIdentity = ObjectIdentity
upsWellKnownAlarms = _UpsWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4)
)
_UpsAlarmOnBattery_Type = Integer32
_UpsAlarmOnBattery_Object = MibScalar
upsAlarmOnBattery = _UpsAlarmOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 1),
    _UpsAlarmOnBattery_Type()
)
upsAlarmOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOnBattery.setStatus("mandatory")
_UpsAlarmLowRuntime_Type = Integer32
_UpsAlarmLowRuntime_Object = MibScalar
upsAlarmLowRuntime = _UpsAlarmLowRuntime_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 2),
    _UpsAlarmLowRuntime_Type()
)
upsAlarmLowRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmLowRuntime.setStatus("mandatory")
_UpsAlarmNearLowBattery_Type = Integer32
_UpsAlarmNearLowBattery_Object = MibScalar
upsAlarmNearLowBattery = _UpsAlarmNearLowBattery_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 3),
    _UpsAlarmNearLowBattery_Type()
)
upsAlarmNearLowBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmNearLowBattery.setStatus("mandatory")
_UpsAlarmLowBattery_Type = Integer32
_UpsAlarmLowBattery_Object = MibScalar
upsAlarmLowBattery = _UpsAlarmLowBattery_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 4),
    _UpsAlarmLowBattery_Type()
)
upsAlarmLowBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmLowBattery.setStatus("mandatory")
_UpsAlarmHighBattery_Type = Integer32
_UpsAlarmHighBattery_Object = MibScalar
upsAlarmHighBattery = _UpsAlarmHighBattery_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 5),
    _UpsAlarmHighBattery_Type()
)
upsAlarmHighBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmHighBattery.setStatus("mandatory")
_UpsAlarmCheckBattery_Type = Integer32
_UpsAlarmCheckBattery_Object = MibScalar
upsAlarmCheckBattery = _UpsAlarmCheckBattery_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 6),
    _UpsAlarmCheckBattery_Type()
)
upsAlarmCheckBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCheckBattery.setStatus("mandatory")
_UpsAlarmReplaceBattery_Type = Integer32
_UpsAlarmReplaceBattery_Object = MibScalar
upsAlarmReplaceBattery = _UpsAlarmReplaceBattery_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 7),
    _UpsAlarmReplaceBattery_Type()
)
upsAlarmReplaceBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmReplaceBattery.setStatus("mandatory")
_UpsAlarmCheckInverter_Type = Integer32
_UpsAlarmCheckInverter_Object = MibScalar
upsAlarmCheckInverter = _UpsAlarmCheckInverter_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 8),
    _UpsAlarmCheckInverter_Type()
)
upsAlarmCheckInverter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCheckInverter.setStatus("mandatory")
_UpsAlarmBatteriesDisconnected_Type = Integer32
_UpsAlarmBatteriesDisconnected_Object = MibScalar
upsAlarmBatteriesDisconnected = _UpsAlarmBatteriesDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 9),
    _UpsAlarmBatteriesDisconnected_Type()
)
upsAlarmBatteriesDisconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteriesDisconnected.setStatus("mandatory")
_UpsAlarmOutputOverload_Type = Integer32
_UpsAlarmOutputOverload_Object = MibScalar
upsAlarmOutputOverload = _UpsAlarmOutputOverload_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 10),
    _UpsAlarmOutputOverload_Type()
)
upsAlarmOutputOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputOverload.setStatus("mandatory")
_UpsAlarmLowAcOut_Type = Integer32
_UpsAlarmLowAcOut_Object = MibScalar
upsAlarmLowAcOut = _UpsAlarmLowAcOut_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 11),
    _UpsAlarmLowAcOut_Type()
)
upsAlarmLowAcOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmLowAcOut.setStatus("mandatory")
_UpsAlarmCircuitBreakerWarning_Type = Integer32
_UpsAlarmCircuitBreakerWarning_Object = MibScalar
upsAlarmCircuitBreakerWarning = _UpsAlarmCircuitBreakerWarning_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 12),
    _UpsAlarmCircuitBreakerWarning_Type()
)
upsAlarmCircuitBreakerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCircuitBreakerWarning.setStatus("mandatory")
_UpsAlarmCircuitBreakerShdn_Type = Integer32
_UpsAlarmCircuitBreakerShdn_Object = MibScalar
upsAlarmCircuitBreakerShdn = _UpsAlarmCircuitBreakerShdn_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 13),
    _UpsAlarmCircuitBreakerShdn_Type()
)
upsAlarmCircuitBreakerShdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCircuitBreakerShdn.setStatus("mandatory")
_UpsAlarmBypassOn_Type = Integer32
_UpsAlarmBypassOn_Object = MibScalar
upsAlarmBypassOn = _UpsAlarmBypassOn_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 14),
    _UpsAlarmBypassOn_Type()
)
upsAlarmBypassOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBypassOn.setStatus("mandatory")
_UpsAlarmAutoBypass_Type = Integer32
_UpsAlarmAutoBypass_Object = MibScalar
upsAlarmAutoBypass = _UpsAlarmAutoBypass_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 15),
    _UpsAlarmAutoBypass_Type()
)
upsAlarmAutoBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmAutoBypass.setStatus("mandatory")
_UpsAlarmSiteWiringFault_Type = Integer32
_UpsAlarmSiteWiringFault_Object = MibScalar
upsAlarmSiteWiringFault = _UpsAlarmSiteWiringFault_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 16),
    _UpsAlarmSiteWiringFault_Type()
)
upsAlarmSiteWiringFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmSiteWiringFault.setStatus("mandatory")
_UpsAlarmCheckFan_Type = Integer32
_UpsAlarmCheckFan_Object = MibScalar
upsAlarmCheckFan = _UpsAlarmCheckFan_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 17),
    _UpsAlarmCheckFan_Type()
)
upsAlarmCheckFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCheckFan.setStatus("mandatory")
_UpsAlarmHighAmbTemp_Type = Integer32
_UpsAlarmHighAmbTemp_Object = MibScalar
upsAlarmHighAmbTemp = _UpsAlarmHighAmbTemp_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 18),
    _UpsAlarmHighAmbTemp_Type()
)
upsAlarmHighAmbTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmHighAmbTemp.setStatus("mandatory")
_UpsAlarmHighHSTemp_Type = Integer32
_UpsAlarmHighHSTemp_Object = MibScalar
upsAlarmHighHSTemp = _UpsAlarmHighHSTemp_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 19),
    _UpsAlarmHighHSTemp_Type()
)
upsAlarmHighHSTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmHighHSTemp.setStatus("mandatory")
_UpsAlarmHighXFMRTemp_Type = Integer32
_UpsAlarmHighXFMRTemp_Object = MibScalar
upsAlarmHighXFMRTemp = _UpsAlarmHighXFMRTemp_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 20),
    _UpsAlarmHighXFMRTemp_Type()
)
upsAlarmHighXFMRTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmHighXFMRTemp.setStatus("mandatory")
_UpsAlarmHighPFMTemp_Type = Integer32
_UpsAlarmHighPFMTemp_Object = MibScalar
upsAlarmHighPFMTemp = _UpsAlarmHighPFMTemp_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 21),
    _UpsAlarmHighPFMTemp_Type()
)
upsAlarmHighPFMTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmHighPFMTemp.setStatus("mandatory")
_UpsAlarmProbeMissing_Type = Integer32
_UpsAlarmProbeMissing_Object = MibScalar
upsAlarmProbeMissing = _UpsAlarmProbeMissing_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 22),
    _UpsAlarmProbeMissing_Type()
)
upsAlarmProbeMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmProbeMissing.setStatus("mandatory")
_UpsAlarmCheckPowerSupply_Type = Integer32
_UpsAlarmCheckPowerSupply_Object = MibScalar
upsAlarmCheckPowerSupply = _UpsAlarmCheckPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 23),
    _UpsAlarmCheckPowerSupply_Type()
)
upsAlarmCheckPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCheckPowerSupply.setStatus("mandatory")
_UpsAlarmTapRegulator_Type = Integer32
_UpsAlarmTapRegulator_Object = MibScalar
upsAlarmTapRegulator = _UpsAlarmTapRegulator_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 24),
    _UpsAlarmTapRegulator_Type()
)
upsAlarmTapRegulator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTapRegulator.setStatus("mandatory")
_UpsAlarmRelayFailure_Type = Integer32
_UpsAlarmRelayFailure_Object = MibScalar
upsAlarmRelayFailure = _UpsAlarmRelayFailure_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 25),
    _UpsAlarmRelayFailure_Type()
)
upsAlarmRelayFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmRelayFailure.setStatus("mandatory")
_UpsAlarmCheckFuse_Type = Integer32
_UpsAlarmCheckFuse_Object = MibScalar
upsAlarmCheckFuse = _UpsAlarmCheckFuse_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 26),
    _UpsAlarmCheckFuse_Type()
)
upsAlarmCheckFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCheckFuse.setStatus("mandatory")
_UpsAlarmCheckMOV_Type = Integer32
_UpsAlarmCheckMOV_Object = MibScalar
upsAlarmCheckMOV = _UpsAlarmCheckMOV_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 27),
    _UpsAlarmCheckMOV_Type()
)
upsAlarmCheckMOV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCheckMOV.setStatus("mandatory")
_UpsAlarmMemoryError_Type = Integer32
_UpsAlarmMemoryError_Object = MibScalar
upsAlarmMemoryError = _UpsAlarmMemoryError_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 28),
    _UpsAlarmMemoryError_Type()
)
upsAlarmMemoryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMemoryError.setStatus("mandatory")
_UpsAlarmCallService_Type = Integer32
_UpsAlarmCallService_Object = MibScalar
upsAlarmCallService = _UpsAlarmCallService_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 29),
    _UpsAlarmCallService_Type()
)
upsAlarmCallService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCallService.setStatus("mandatory")
_UpsAlarmupsFailed_Type = Integer32
_UpsAlarmupsFailed_Object = MibScalar
upsAlarmupsFailed = _UpsAlarmupsFailed_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 30),
    _UpsAlarmupsFailed_Type()
)
upsAlarmupsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmupsFailed.setStatus("mandatory")
_UpsAlarmUserTest_Type = Integer32
_UpsAlarmUserTest_Object = MibScalar
upsAlarmUserTest = _UpsAlarmUserTest_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 31),
    _UpsAlarmUserTest_Type()
)
upsAlarmUserTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUserTest.setStatus("mandatory")
_UpsAlarmTestInProgress_Type = Integer32
_UpsAlarmTestInProgress_Object = MibScalar
upsAlarmTestInProgress = _UpsAlarmTestInProgress_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 32),
    _UpsAlarmTestInProgress_Type()
)
upsAlarmTestInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTestInProgress.setStatus("mandatory")
_UpsAlarmDiagnosticTestFailed_Type = Integer32
_UpsAlarmDiagnosticTestFailed_Object = MibScalar
upsAlarmDiagnosticTestFailed = _UpsAlarmDiagnosticTestFailed_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 33),
    _UpsAlarmDiagnosticTestFailed_Type()
)
upsAlarmDiagnosticTestFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailed.setStatus("mandatory")
_UpsAlarmEPO_Type = Integer32
_UpsAlarmEPO_Object = MibScalar
upsAlarmEPO = _UpsAlarmEPO_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 34),
    _UpsAlarmEPO_Type()
)
upsAlarmEPO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmEPO.setStatus("mandatory")
_UpsAlarmUpsOff_Type = Integer32
_UpsAlarmUpsOff_Object = MibScalar
upsAlarmUpsOff = _UpsAlarmUpsOff_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 35),
    _UpsAlarmUpsOff_Type()
)
upsAlarmUpsOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUpsOff.setStatus("mandatory")
_UpsAlarmCommunicationsLost_Type = Integer32
_UpsAlarmCommunicationsLost_Object = MibScalar
upsAlarmCommunicationsLost = _UpsAlarmCommunicationsLost_Object(
    (1, 3, 6, 1, 4, 1, 2947, 1, 8, 4, 36),
    _UpsAlarmCommunicationsLost_Type()
)
upsAlarmCommunicationsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLost.setStatus("mandatory")

# Managed Objects groups


# Notification objects

upsTrapPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 1)
)
if mibBuilder.loadTexts:
    upsTrapPowerFail.setStatus(
        ""
    )

upsTrapPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 2)
)
if mibBuilder.loadTexts:
    upsTrapPowerRestored.setStatus(
        ""
    )

upsTrapUPSOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 3)
)
upsTrapUPSOnBattery.setObjects(
      *(("BESTPOWER-MIB", "upsBatteryTimeOnBattery"),
        ("BESTPOWER-MIB", "upsBatteryRuntimeRemaining"),
        ("BESTPOWER-MIB", "upsConfigLowRuntimeSetpoint"),
        ("BESTPOWER-MIB", "upsBatteryVoltage"))
)
if mibBuilder.loadTexts:
    upsTrapUPSOnBattery.setStatus(
        ""
    )

upsTrapUPSNotOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 4)
)
if mibBuilder.loadTexts:
    upsTrapUPSNotOnBattery.setStatus(
        ""
    )

upsTrapLowRuntime = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 5)
)
if mibBuilder.loadTexts:
    upsTrapLowRuntime.setStatus(
        ""
    )

upsTrapUPSCanRunOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 6)
)
if mibBuilder.loadTexts:
    upsTrapUPSCanRunOnBattery.setStatus(
        ""
    )

upsTrapNearLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 7)
)
upsTrapNearLowBattery.setObjects(
    ("BESTPOWER-MIB", "upsBatteryVoltage")
)
if mibBuilder.loadTexts:
    upsTrapNearLowBattery.setStatus(
        ""
    )

upsTrapHighBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 8)
)
upsTrapHighBattery.setObjects(
    ("BESTPOWER-MIB", "upsBatteryVoltage")
)
if mibBuilder.loadTexts:
    upsTrapHighBattery.setStatus(
        ""
    )

upsTrapBatteryOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 9)
)
if mibBuilder.loadTexts:
    upsTrapBatteryOK.setStatus(
        ""
    )

upsTrapLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 10)
)
upsTrapLowBattery.setObjects(
    ("BESTPOWER-MIB", "upsBatteryVoltage")
)
if mibBuilder.loadTexts:
    upsTrapLowBattery.setStatus(
        ""
    )

upsTrapCheckBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 11)
)
if mibBuilder.loadTexts:
    upsTrapCheckBattery.setStatus(
        ""
    )

upsTrapReplaceBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 12)
)
if mibBuilder.loadTexts:
    upsTrapReplaceBattery.setStatus(
        ""
    )

upsTrapCheckInverter = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 13)
)
if mibBuilder.loadTexts:
    upsTrapCheckInverter.setStatus(
        ""
    )

upsTrapBatteriesDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 14)
)
if mibBuilder.loadTexts:
    upsTrapBatteriesDisconnected.setStatus(
        ""
    )

upsTrapOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 15)
)
if mibBuilder.loadTexts:
    upsTrapOutputOverload.setStatus(
        ""
    )

upsTrapUPSNoLongerOverloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 16)
)
if mibBuilder.loadTexts:
    upsTrapUPSNoLongerOverloaded.setStatus(
        ""
    )

upsTrapLowAcOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 17)
)
if mibBuilder.loadTexts:
    upsTrapLowAcOut.setStatus(
        ""
    )

upsTrapCircuitBreakerWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 18)
)
if mibBuilder.loadTexts:
    upsTrapCircuitBreakerWarning.setStatus(
        ""
    )

upsTrapCircuitBreakerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 19)
)
if mibBuilder.loadTexts:
    upsTrapCircuitBreakerOK.setStatus(
        ""
    )

upsTrapCircuitBreakerShdn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 20)
)
if mibBuilder.loadTexts:
    upsTrapCircuitBreakerShdn.setStatus(
        ""
    )

upsTrapBypassOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 21)
)
if mibBuilder.loadTexts:
    upsTrapBypassOn.setStatus(
        ""
    )

upsTrapUPSOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 22)
)
if mibBuilder.loadTexts:
    upsTrapUPSOnline.setStatus(
        ""
    )

upsTrapSiteWiringFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 23)
)
if mibBuilder.loadTexts:
    upsTrapSiteWiringFault.setStatus(
        ""
    )

upsTrapCheckFan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 24)
)
if mibBuilder.loadTexts:
    upsTrapCheckFan.setStatus(
        ""
    )

upsTrapHighUPSTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 25)
)
if mibBuilder.loadTexts:
    upsTrapHighUPSTemp.setStatus(
        ""
    )

upsTrapTempOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 26)
)
if mibBuilder.loadTexts:
    upsTrapTempOK.setStatus(
        ""
    )

upsTrapHighHSTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 27)
)
if mibBuilder.loadTexts:
    upsTrapHighHSTemp.setStatus(
        ""
    )

upsTrapHSTempOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 28)
)
if mibBuilder.loadTexts:
    upsTrapHSTempOK.setStatus(
        ""
    )

upsTrapHighXFMRTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 29)
)
if mibBuilder.loadTexts:
    upsTrapHighXFMRTemp.setStatus(
        ""
    )

upsTrapHighPFMTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 30)
)
if mibBuilder.loadTexts:
    upsTrapHighPFMTemp.setStatus(
        ""
    )

upsTrapProbeMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 31)
)
if mibBuilder.loadTexts:
    upsTrapProbeMissing.setStatus(
        ""
    )

upsTrapProbeReconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 32)
)
if mibBuilder.loadTexts:
    upsTrapProbeReconnected.setStatus(
        ""
    )

upsTrapCheckPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 33)
)
if mibBuilder.loadTexts:
    upsTrapCheckPowerSupply.setStatus(
        ""
    )

upsTrapTapRegulatorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 34)
)
if mibBuilder.loadTexts:
    upsTrapTapRegulatorFault.setStatus(
        ""
    )

upsTrapRelayFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 35)
)
if mibBuilder.loadTexts:
    upsTrapRelayFailure.setStatus(
        ""
    )

upsTrapCheckFuse = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 36)
)
if mibBuilder.loadTexts:
    upsTrapCheckFuse.setStatus(
        ""
    )

upsTrapCheckMOV = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 37)
)
if mibBuilder.loadTexts:
    upsTrapCheckMOV.setStatus(
        ""
    )

upsTrapMemoryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 38)
)
if mibBuilder.loadTexts:
    upsTrapMemoryError.setStatus(
        ""
    )

upsTrapCallService = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 39)
)
if mibBuilder.loadTexts:
    upsTrapCallService.setStatus(
        ""
    )

upsTrapManualAlarmBeeperTestInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 40)
)
if mibBuilder.loadTexts:
    upsTrapManualAlarmBeeperTestInitiated.setStatus(
        ""
    )

upsTrapManualAlarmBeeperTestAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 41)
)
if mibBuilder.loadTexts:
    upsTrapManualAlarmBeeperTestAborted.setStatus(
        ""
    )

upsTrapScheduledTestInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 42)
)
if mibBuilder.loadTexts:
    upsTrapScheduledTestInProgress.setStatus(
        ""
    )

upsTrapScheduledTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 43)
)
if mibBuilder.loadTexts:
    upsTrapScheduledTestFailed.setStatus(
        ""
    )

upsTrapCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 44)
)
if mibBuilder.loadTexts:
    upsTrapCommunicationLost.setStatus(
        ""
    )

upsTrapCommunicationRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 45)
)
if mibBuilder.loadTexts:
    upsTrapCommunicationRestored.setStatus(
        ""
    )

upsTrapUPSGoingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 46)
)
if mibBuilder.loadTexts:
    upsTrapUPSGoingDown.setStatus(
        ""
    )

upsTrapUPSTurnedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 47)
)
if mibBuilder.loadTexts:
    upsTrapUPSTurnedOff.setStatus(
        ""
    )

upsTrapUPSSleeping = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 48)
)
if mibBuilder.loadTexts:
    upsTrapUPSSleeping.setStatus(
        ""
    )

upsTrapUPSWokeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 49)
)
if mibBuilder.loadTexts:
    upsTrapUPSWokeUp.setStatus(
        ""
    )

upsTrapUPSRebooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 50)
)
if mibBuilder.loadTexts:
    upsTrapUPSRebooted.setStatus(
        ""
    )

upsTrapEmergencyPowerOFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 51)
)
if mibBuilder.loadTexts:
    upsTrapEmergencyPowerOFF.setStatus(
        ""
    )

upsTrapHistLogWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 52)
)
if mibBuilder.loadTexts:
    upsTrapHistLogWarn.setStatus(
        ""
    )

upsTrapEventLogWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 53)
)
if mibBuilder.loadTexts:
    upsTrapEventLogWarn.setStatus(
        ""
    )

upsTrapUPSFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2947, 1, 0, 54)
)
if mibBuilder.loadTexts:
    upsTrapUPSFail.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BESTPOWER-MIB",
    **{"NonNegativeInteger": NonNegativeInteger,
       "PositiveInteger": PositiveInteger,
       "bestPower": bestPower,
       "bestLink": bestLink,
       "upsTrapPowerFail": upsTrapPowerFail,
       "upsTrapPowerRestored": upsTrapPowerRestored,
       "upsTrapUPSOnBattery": upsTrapUPSOnBattery,
       "upsTrapUPSNotOnBattery": upsTrapUPSNotOnBattery,
       "upsTrapLowRuntime": upsTrapLowRuntime,
       "upsTrapUPSCanRunOnBattery": upsTrapUPSCanRunOnBattery,
       "upsTrapNearLowBattery": upsTrapNearLowBattery,
       "upsTrapHighBattery": upsTrapHighBattery,
       "upsTrapBatteryOK": upsTrapBatteryOK,
       "upsTrapLowBattery": upsTrapLowBattery,
       "upsTrapCheckBattery": upsTrapCheckBattery,
       "upsTrapReplaceBattery": upsTrapReplaceBattery,
       "upsTrapCheckInverter": upsTrapCheckInverter,
       "upsTrapBatteriesDisconnected": upsTrapBatteriesDisconnected,
       "upsTrapOutputOverload": upsTrapOutputOverload,
       "upsTrapUPSNoLongerOverloaded": upsTrapUPSNoLongerOverloaded,
       "upsTrapLowAcOut": upsTrapLowAcOut,
       "upsTrapCircuitBreakerWarning": upsTrapCircuitBreakerWarning,
       "upsTrapCircuitBreakerOK": upsTrapCircuitBreakerOK,
       "upsTrapCircuitBreakerShdn": upsTrapCircuitBreakerShdn,
       "upsTrapBypassOn": upsTrapBypassOn,
       "upsTrapUPSOnline": upsTrapUPSOnline,
       "upsTrapSiteWiringFault": upsTrapSiteWiringFault,
       "upsTrapCheckFan": upsTrapCheckFan,
       "upsTrapHighUPSTemp": upsTrapHighUPSTemp,
       "upsTrapTempOK": upsTrapTempOK,
       "upsTrapHighHSTemp": upsTrapHighHSTemp,
       "upsTrapHSTempOK": upsTrapHSTempOK,
       "upsTrapHighXFMRTemp": upsTrapHighXFMRTemp,
       "upsTrapHighPFMTemp": upsTrapHighPFMTemp,
       "upsTrapProbeMissing": upsTrapProbeMissing,
       "upsTrapProbeReconnected": upsTrapProbeReconnected,
       "upsTrapCheckPowerSupply": upsTrapCheckPowerSupply,
       "upsTrapTapRegulatorFault": upsTrapTapRegulatorFault,
       "upsTrapRelayFailure": upsTrapRelayFailure,
       "upsTrapCheckFuse": upsTrapCheckFuse,
       "upsTrapCheckMOV": upsTrapCheckMOV,
       "upsTrapMemoryError": upsTrapMemoryError,
       "upsTrapCallService": upsTrapCallService,
       "upsTrapManualAlarmBeeperTestInitiated": upsTrapManualAlarmBeeperTestInitiated,
       "upsTrapManualAlarmBeeperTestAborted": upsTrapManualAlarmBeeperTestAborted,
       "upsTrapScheduledTestInProgress": upsTrapScheduledTestInProgress,
       "upsTrapScheduledTestFailed": upsTrapScheduledTestFailed,
       "upsTrapCommunicationLost": upsTrapCommunicationLost,
       "upsTrapCommunicationRestored": upsTrapCommunicationRestored,
       "upsTrapUPSGoingDown": upsTrapUPSGoingDown,
       "upsTrapUPSTurnedOff": upsTrapUPSTurnedOff,
       "upsTrapUPSSleeping": upsTrapUPSSleeping,
       "upsTrapUPSWokeUp": upsTrapUPSWokeUp,
       "upsTrapUPSRebooted": upsTrapUPSRebooted,
       "upsTrapEmergencyPowerOFF": upsTrapEmergencyPowerOFF,
       "upsTrapHistLogWarn": upsTrapHistLogWarn,
       "upsTrapEventLogWarn": upsTrapEventLogWarn,
       "upsTrapUPSFail": upsTrapUPSFail,
       "upsIdent": upsIdent,
       "upsIdentUpsName": upsIdentUpsName,
       "upsIdentModel": upsIdentModel,
       "upsIdentVARating": upsIdentVARating,
       "upsIdentUpsType": upsIdentUpsType,
       "upsIdentUpsSerialNumber": upsIdentUpsSerialNumber,
       "upsIdentUpsIdentification": upsIdentUpsIdentification,
       "upsIdentFirmwareRevision": upsIdentFirmwareRevision,
       "upsIdentDateOfManufacture": upsIdentDateOfManufacture,
       "upsBattery": upsBattery,
       "upsBatteryStatus": upsBatteryStatus,
       "upsBatteryTimeOnBattery": upsBatteryTimeOnBattery,
       "upsBatteryRuntimeRemaining": upsBatteryRuntimeRemaining,
       "upsBatteryVoltage": upsBatteryVoltage,
       "upsBatteryCurrent": upsBatteryCurrent,
       "upsBatteryTemperature": upsBatteryTemperature,
       "upsBatteryLastReplaceDate": upsBatteryLastReplaceDate,
       "upsInput": upsInput,
       "upsInputPhase": upsInputPhase,
       "upsInputFrequency": upsInputFrequency,
       "upsInputVoltage": upsInputVoltage,
       "upsInputCurrent": upsInputCurrent,
       "upsInputPower": upsInputPower,
       "upsInputPhase2": upsInputPhase2,
       "upsInputP2": upsInputP2,
       "upsInputFrequency2": upsInputFrequency2,
       "upsInputVoltage2": upsInputVoltage2,
       "upsInputCurrent2": upsInputCurrent2,
       "upsInputPower2": upsInputPower2,
       "upsInputPhase3": upsInputPhase3,
       "upsInputP3": upsInputP3,
       "upsInputFrequency3": upsInputFrequency3,
       "upsInputVoltage3": upsInputVoltage3,
       "upsInputCurrent3": upsInputCurrent3,
       "upsInputPower3": upsInputPower3,
       "upsOutput": upsOutput,
       "upsOutputStatus": upsOutputStatus,
       "upsOutputPhase": upsOutputPhase,
       "upsOutputFrequency": upsOutputFrequency,
       "upsOutputVoltage": upsOutputVoltage,
       "upsOutputCurrent": upsOutputCurrent,
       "upsOutputTruePower": upsOutputTruePower,
       "upsOutputApparentPower": upsOutputApparentPower,
       "upsOutputPowerFactor": upsOutputPowerFactor,
       "upsOutputPercentLoad": upsOutputPercentLoad,
       "upsOutputPhase2": upsOutputPhase2,
       "upsOutputP2": upsOutputP2,
       "upsOutputFrequency2": upsOutputFrequency2,
       "upsOutputVoltage2": upsOutputVoltage2,
       "upsOutputCurrent2": upsOutputCurrent2,
       "upsOutputTruePower2": upsOutputTruePower2,
       "upsOutputApparentPower2": upsOutputApparentPower2,
       "upsOutputPowerFactor2": upsOutputPowerFactor2,
       "upsOutputPhase3": upsOutputPhase3,
       "upsOutputP3": upsOutputP3,
       "upsOutputFrequency3": upsOutputFrequency3,
       "upsOutputVoltage3": upsOutputVoltage3,
       "upsOutputCurrent3": upsOutputCurrent3,
       "upsOutputTruePower3": upsOutputTruePower3,
       "upsOutputApparentPower3": upsOutputApparentPower3,
       "upsOutputPowerFactor3": upsOutputPowerFactor3,
       "upsConfig": upsConfig,
       "upsConfigLowRuntimeSetpoint": upsConfigLowRuntimeSetpoint,
       "upsConfigDelayBeforeRestart": upsConfigDelayBeforeRestart,
       "upsConfigDelayBeforeShutdown": upsConfigDelayBeforeShutdown,
       "upsConfigTest": upsConfigTest,
       "upsConfigTestLevel": upsConfigTestLevel,
       "upsConfigDaysBetweenTests": upsConfigDaysBetweenTests,
       "upsConfigBatteryTestDuration": upsConfigBatteryTestDuration,
       "upsConfigScheduleTable": upsConfigScheduleTable,
       "upsConfigScheduleEntry": upsConfigScheduleEntry,
       "upsConfigScheduleIndex": upsConfigScheduleIndex,
       "upsConfigScheduleShutdownDay": upsConfigScheduleShutdownDay,
       "upsConfigScheduleShutdownTime": upsConfigScheduleShutdownTime,
       "upsConfigScheduleRestartDay": upsConfigScheduleRestartDay,
       "upsConfigScheduleRestartTime": upsConfigScheduleRestartTime,
       "upsConfigbestLink": upsConfigbestLink,
       "bestLinkHistoryLogFrequency": bestLinkHistoryLogFrequency,
       "bestLinkRefreshFrequency": bestLinkRefreshFrequency,
       "bestLinkNetId": bestLinkNetId,
       "bestLinkGateway": bestLinkGateway,
       "bestLinkNetMask": bestLinkNetMask,
       "bestLinkSysDate": bestLinkSysDate,
       "bestLinkSysTime": bestLinkSysTime,
       "bestLinkTftpFileName": bestLinkTftpFileName,
       "bestLinkTftpHost": bestLinkTftpHost,
       "bestLinkFlashEEPROM": bestLinkFlashEEPROM,
       "bestLinkPrimaryTimeServer": bestLinkPrimaryTimeServer,
       "bestLinkSecondaryTimeServer": bestLinkSecondaryTimeServer,
       "bestLinkSoftwareVersion": bestLinkSoftwareVersion,
       "upsConfigTrapsReceivers": upsConfigTrapsReceivers,
       "upsConfigTrapsReceiversTable": upsConfigTrapsReceiversTable,
       "upsConfigTrapsReceiversEntry": upsConfigTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverCommunityString": receiverCommunityString,
       "severityLevel": severityLevel,
       "receiverAccept": receiverAccept,
       "upsConfigRegisteredShutdownClients": upsConfigRegisteredShutdownClients,
       "upsRegisteredShutdownClientsTable": upsRegisteredShutdownClientsTable,
       "upsRegisteredShutdownClientsEntry": upsRegisteredShutdownClientsEntry,
       "upsRegisteredShutdownClientsIndex": upsRegisteredShutdownClientsIndex,
       "upsRegisteredShutdownClientsIPAddress": upsRegisteredShutdownClientsIPAddress,
       "upsRegisteredShutdownClientsTotalNumberOf": upsRegisteredShutdownClientsTotalNumberOf,
       "upsControl": upsControl,
       "upsControlTurnOffUPS": upsControlTurnOffUPS,
       "upsControlActivateUpsScheduling": upsControlActivateUpsScheduling,
       "upsTest": upsTest,
       "upsManualTests": upsManualTests,
       "upsAlarm": upsAlarm,
       "upsAlarmsPresent": upsAlarmsPresent,
       "upsLastKnownAlarm": upsLastKnownAlarm,
       "upsAlarmTable": upsAlarmTable,
       "upsAlarmEntry": upsAlarmEntry,
       "upsAlarmIndex": upsAlarmIndex,
       "upsAlarmName": upsAlarmName,
       "upsAlarmTime": upsAlarmTime,
       "upsWellKnownAlarms": upsWellKnownAlarms,
       "upsAlarmOnBattery": upsAlarmOnBattery,
       "upsAlarmLowRuntime": upsAlarmLowRuntime,
       "upsAlarmNearLowBattery": upsAlarmNearLowBattery,
       "upsAlarmLowBattery": upsAlarmLowBattery,
       "upsAlarmHighBattery": upsAlarmHighBattery,
       "upsAlarmCheckBattery": upsAlarmCheckBattery,
       "upsAlarmReplaceBattery": upsAlarmReplaceBattery,
       "upsAlarmCheckInverter": upsAlarmCheckInverter,
       "upsAlarmBatteriesDisconnected": upsAlarmBatteriesDisconnected,
       "upsAlarmOutputOverload": upsAlarmOutputOverload,
       "upsAlarmLowAcOut": upsAlarmLowAcOut,
       "upsAlarmCircuitBreakerWarning": upsAlarmCircuitBreakerWarning,
       "upsAlarmCircuitBreakerShdn": upsAlarmCircuitBreakerShdn,
       "upsAlarmBypassOn": upsAlarmBypassOn,
       "upsAlarmAutoBypass": upsAlarmAutoBypass,
       "upsAlarmSiteWiringFault": upsAlarmSiteWiringFault,
       "upsAlarmCheckFan": upsAlarmCheckFan,
       "upsAlarmHighAmbTemp": upsAlarmHighAmbTemp,
       "upsAlarmHighHSTemp": upsAlarmHighHSTemp,
       "upsAlarmHighXFMRTemp": upsAlarmHighXFMRTemp,
       "upsAlarmHighPFMTemp": upsAlarmHighPFMTemp,
       "upsAlarmProbeMissing": upsAlarmProbeMissing,
       "upsAlarmCheckPowerSupply": upsAlarmCheckPowerSupply,
       "upsAlarmTapRegulator": upsAlarmTapRegulator,
       "upsAlarmRelayFailure": upsAlarmRelayFailure,
       "upsAlarmCheckFuse": upsAlarmCheckFuse,
       "upsAlarmCheckMOV": upsAlarmCheckMOV,
       "upsAlarmMemoryError": upsAlarmMemoryError,
       "upsAlarmCallService": upsAlarmCallService,
       "upsAlarmupsFailed": upsAlarmupsFailed,
       "upsAlarmUserTest": upsAlarmUserTest,
       "upsAlarmTestInProgress": upsAlarmTestInProgress,
       "upsAlarmDiagnosticTestFailed": upsAlarmDiagnosticTestFailed,
       "upsAlarmEPO": upsAlarmEPO,
       "upsAlarmUpsOff": upsAlarmUpsOff,
       "upsAlarmCommunicationsLost": upsAlarmCommunicationsLost}
)
