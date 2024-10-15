# SNMP MIB module (XPPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XPPC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:46 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ppc_ObjectIdentity = ObjectIdentity
ppc = _Ppc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1)
)
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1)
)
_UpsIdentp_ObjectIdentity = ObjectIdentity
upsIdentp = _UpsIdentp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 1)
)
_UpsBaseIdent_ObjectIdentity = ObjectIdentity
upsBaseIdent = _UpsBaseIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 1, 1)
)
_UpsBaseIdentModel_Type = DisplayString
_UpsBaseIdentModel_Object = MibScalar
upsBaseIdentModel = _UpsBaseIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 1, 1, 1),
    _UpsBaseIdentModel_Type()
)
upsBaseIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseIdentModel.setStatus("mandatory")
_UpsBaseIdentUpsName_Type = DisplayString
_UpsBaseIdentUpsName_Object = MibScalar
upsBaseIdentUpsName = _UpsBaseIdentUpsName_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 1, 1, 2),
    _UpsBaseIdentUpsName_Type()
)
upsBaseIdentUpsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBaseIdentUpsName.setStatus("mandatory")
_UpsSmartIdent_ObjectIdentity = ObjectIdentity
upsSmartIdent = _UpsSmartIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 1, 2)
)
_UpsSmartIdentFirmwareRevision_Type = DisplayString
_UpsSmartIdentFirmwareRevision_Object = MibScalar
upsSmartIdentFirmwareRevision = _UpsSmartIdentFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 1, 2, 1),
    _UpsSmartIdentFirmwareRevision_Type()
)
upsSmartIdentFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartIdentFirmwareRevision.setStatus("mandatory")
_UpsSmartIdentDateOfManufacture_Type = DisplayString
_UpsSmartIdentDateOfManufacture_Object = MibScalar
upsSmartIdentDateOfManufacture = _UpsSmartIdentDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 1, 2, 2),
    _UpsSmartIdentDateOfManufacture_Type()
)
upsSmartIdentDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartIdentDateOfManufacture.setStatus("mandatory")
_UpsSmartIdentUpsSerialNumber_Type = DisplayString
_UpsSmartIdentUpsSerialNumber_Object = MibScalar
upsSmartIdentUpsSerialNumber = _UpsSmartIdentUpsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 1, 2, 3),
    _UpsSmartIdentUpsSerialNumber_Type()
)
upsSmartIdentUpsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartIdentUpsSerialNumber.setStatus("mandatory")
_UpsSmartIdentAgentFirmwareRevision_Type = DisplayString
_UpsSmartIdentAgentFirmwareRevision_Object = MibScalar
upsSmartIdentAgentFirmwareRevision = _UpsSmartIdentAgentFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 1, 2, 4),
    _UpsSmartIdentAgentFirmwareRevision_Type()
)
upsSmartIdentAgentFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartIdentAgentFirmwareRevision.setStatus("mandatory")
_UpsBatteryp_ObjectIdentity = ObjectIdentity
upsBatteryp = _UpsBatteryp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2)
)
_UpsBaseBattery_ObjectIdentity = ObjectIdentity
upsBaseBattery = _UpsBaseBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 1)
)


class _UpsBaseBatteryStatus_Type(Integer32):
    """Custom type upsBaseBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("batteryLow", 3),
          ("batteryNormal", 2),
          ("unknown", 1))
    )


_UpsBaseBatteryStatus_Type.__name__ = "Integer32"
_UpsBaseBatteryStatus_Object = MibScalar
upsBaseBatteryStatus = _UpsBaseBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 1, 1),
    _UpsBaseBatteryStatus_Type()
)
upsBaseBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseBatteryStatus.setStatus("mandatory")
_UpsBaseBatteryTimeOnBattery_Type = Integer32
_UpsBaseBatteryTimeOnBattery_Object = MibScalar
upsBaseBatteryTimeOnBattery = _UpsBaseBatteryTimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 1, 2),
    _UpsBaseBatteryTimeOnBattery_Type()
)
upsBaseBatteryTimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseBatteryTimeOnBattery.setStatus("mandatory")
_UpsBaseBatteryLastReplaceDate_Type = DisplayString
_UpsBaseBatteryLastReplaceDate_Object = MibScalar
upsBaseBatteryLastReplaceDate = _UpsBaseBatteryLastReplaceDate_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 1, 3),
    _UpsBaseBatteryLastReplaceDate_Type()
)
upsBaseBatteryLastReplaceDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBaseBatteryLastReplaceDate.setStatus("mandatory")
_UpsSmartBattery_ObjectIdentity = ObjectIdentity
upsSmartBattery = _UpsSmartBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 2)
)
_UpsSmartBatteryCapacity_Type = Integer32
_UpsSmartBatteryCapacity_Object = MibScalar
upsSmartBatteryCapacity = _UpsSmartBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 2, 1),
    _UpsSmartBatteryCapacity_Type()
)
upsSmartBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartBatteryCapacity.setStatus("mandatory")
_UpsSmartBatteryVoltage_Type = Integer32
_UpsSmartBatteryVoltage_Object = MibScalar
upsSmartBatteryVoltage = _UpsSmartBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 2, 2),
    _UpsSmartBatteryVoltage_Type()
)
upsSmartBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartBatteryVoltage.setStatus("mandatory")
_UpsSmartBatteryTemperature_Type = Integer32
_UpsSmartBatteryTemperature_Object = MibScalar
upsSmartBatteryTemperature = _UpsSmartBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 2, 3),
    _UpsSmartBatteryTemperature_Type()
)
upsSmartBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartBatteryTemperature.setStatus("mandatory")
_UpsSmartBatteryRunTimeRemaining_Type = Integer32
_UpsSmartBatteryRunTimeRemaining_Object = MibScalar
upsSmartBatteryRunTimeRemaining = _UpsSmartBatteryRunTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 2, 4),
    _UpsSmartBatteryRunTimeRemaining_Type()
)
upsSmartBatteryRunTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartBatteryRunTimeRemaining.setStatus("mandatory")


class _UpsSmartBatteryReplaceIndicator_Type(Integer32):
    """Custom type upsSmartBatteryReplaceIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batteryNeedsReplacing", 2),
          ("noBatteryNeedsReplacing", 1))
    )


_UpsSmartBatteryReplaceIndicator_Type.__name__ = "Integer32"
_UpsSmartBatteryReplaceIndicator_Object = MibScalar
upsSmartBatteryReplaceIndicator = _UpsSmartBatteryReplaceIndicator_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 2, 5),
    _UpsSmartBatteryReplaceIndicator_Type()
)
upsSmartBatteryReplaceIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartBatteryReplaceIndicator.setStatus("mandatory")
_UpsSmartBatteryFullChargeVoltage_Type = Integer32
_UpsSmartBatteryFullChargeVoltage_Object = MibScalar
upsSmartBatteryFullChargeVoltage = _UpsSmartBatteryFullChargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 2, 6),
    _UpsSmartBatteryFullChargeVoltage_Type()
)
upsSmartBatteryFullChargeVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartBatteryFullChargeVoltage.setStatus("mandatory")
_UpsSmartBatteryCurrent_Type = Integer32
_UpsSmartBatteryCurrent_Object = MibScalar
upsSmartBatteryCurrent = _UpsSmartBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 2, 2, 7),
    _UpsSmartBatteryCurrent_Type()
)
upsSmartBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartBatteryCurrent.setStatus("mandatory")
_UpsInputp_ObjectIdentity = ObjectIdentity
upsInputp = _UpsInputp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 3)
)
_UpsBaseInput_ObjectIdentity = ObjectIdentity
upsBaseInput = _UpsBaseInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 3, 1)
)
_UpsBaseInputPhase_Type = Integer32
_UpsBaseInputPhase_Object = MibScalar
upsBaseInputPhase = _UpsBaseInputPhase_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 3, 1, 1),
    _UpsBaseInputPhase_Type()
)
upsBaseInputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseInputPhase.setStatus("mandatory")
_UpsSmartInput_ObjectIdentity = ObjectIdentity
upsSmartInput = _UpsSmartInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 3, 2)
)
_UpsSmartInputLineVoltage_Type = Integer32
_UpsSmartInputLineVoltage_Object = MibScalar
upsSmartInputLineVoltage = _UpsSmartInputLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 3, 2, 1),
    _UpsSmartInputLineVoltage_Type()
)
upsSmartInputLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartInputLineVoltage.setStatus("mandatory")
_UpsSmartInputMaxLineVoltage_Type = Integer32
_UpsSmartInputMaxLineVoltage_Object = MibScalar
upsSmartInputMaxLineVoltage = _UpsSmartInputMaxLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 3, 2, 2),
    _UpsSmartInputMaxLineVoltage_Type()
)
upsSmartInputMaxLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartInputMaxLineVoltage.setStatus("mandatory")
_UpsSmartInputMinLineVoltage_Type = Integer32
_UpsSmartInputMinLineVoltage_Object = MibScalar
upsSmartInputMinLineVoltage = _UpsSmartInputMinLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 3, 2, 3),
    _UpsSmartInputMinLineVoltage_Type()
)
upsSmartInputMinLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartInputMinLineVoltage.setStatus("mandatory")
_UpsSmartInputFrequency_Type = Integer32
_UpsSmartInputFrequency_Object = MibScalar
upsSmartInputFrequency = _UpsSmartInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 3, 2, 4),
    _UpsSmartInputFrequency_Type()
)
upsSmartInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartInputFrequency.setStatus("mandatory")


class _UpsSmartInputLineFailCause_Type(Integer32):
    """Custom type upsSmartInputLineFailCause based on Integer32"""
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
        *(("blackout", 4),
          ("brownout", 3),
          ("deepMomentarySag", 6),
          ("highLineVoltage", 2),
          ("largeMomentarySpike", 8),
          ("noTransfer", 1),
          ("smallMomentarySag", 5),
          ("smallMomentarySpike", 7))
    )


_UpsSmartInputLineFailCause_Type.__name__ = "Integer32"
_UpsSmartInputLineFailCause_Object = MibScalar
upsSmartInputLineFailCause = _UpsSmartInputLineFailCause_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 3, 2, 5),
    _UpsSmartInputLineFailCause_Type()
)
upsSmartInputLineFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartInputLineFailCause.setStatus("mandatory")
_UpsOutputp_ObjectIdentity = ObjectIdentity
upsOutputp = _UpsOutputp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 4)
)
_UpsBaseOutput_ObjectIdentity = ObjectIdentity
upsBaseOutput = _UpsBaseOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 4, 1)
)


class _UpsBaseOutputStatus_Type(Integer32):
    """Custom type upsBaseOutputStatus based on Integer32"""
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
        *(("onBattery", 3),
          ("onBoost", 4),
          ("onBuck", 9),
          ("onBypass", 6),
          ("onLine", 2),
          ("rebooting", 7),
          ("sleeping", 5),
          ("standBy", 8),
          ("unknown", 1))
    )


_UpsBaseOutputStatus_Type.__name__ = "Integer32"
_UpsBaseOutputStatus_Object = MibScalar
upsBaseOutputStatus = _UpsBaseOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 4, 1, 1),
    _UpsBaseOutputStatus_Type()
)
upsBaseOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseOutputStatus.setStatus("mandatory")
_UpsBaseOutputPhase_Type = Integer32
_UpsBaseOutputPhase_Object = MibScalar
upsBaseOutputPhase = _UpsBaseOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 4, 1, 2),
    _UpsBaseOutputPhase_Type()
)
upsBaseOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseOutputPhase.setStatus("mandatory")
_UpsSmartOutput_ObjectIdentity = ObjectIdentity
upsSmartOutput = _UpsSmartOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 4, 2)
)
_UpsSmartOutputVoltage_Type = Integer32
_UpsSmartOutputVoltage_Object = MibScalar
upsSmartOutputVoltage = _UpsSmartOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 4, 2, 1),
    _UpsSmartOutputVoltage_Type()
)
upsSmartOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartOutputVoltage.setStatus("mandatory")
_UpsSmartOutputFrequency_Type = Integer32
_UpsSmartOutputFrequency_Object = MibScalar
upsSmartOutputFrequency = _UpsSmartOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 4, 2, 2),
    _UpsSmartOutputFrequency_Type()
)
upsSmartOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartOutputFrequency.setStatus("mandatory")
_UpsSmartOutputLoad_Type = Integer32
_UpsSmartOutputLoad_Object = MibScalar
upsSmartOutputLoad = _UpsSmartOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 4, 2, 3),
    _UpsSmartOutputLoad_Type()
)
upsSmartOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartOutputLoad.setStatus("mandatory")
_UpsConfigp_ObjectIdentity = ObjectIdentity
upsConfigp = _UpsConfigp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5)
)
_UpsBaseConfig_ObjectIdentity = ObjectIdentity
upsBaseConfig = _UpsBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 1)
)
_UpsBaseConfigNumDevices_Type = Integer32
_UpsBaseConfigNumDevices_Object = MibScalar
upsBaseConfigNumDevices = _UpsBaseConfigNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 1, 1),
    _UpsBaseConfigNumDevices_Type()
)
upsBaseConfigNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBaseConfigNumDevices.setStatus("mandatory")
_UpsBaseConfigDeviceTable_Object = MibTable
upsBaseConfigDeviceTable = _UpsBaseConfigDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    upsBaseConfigDeviceTable.setStatus("mandatory")
_UpsBaseConfigDeviceEntry_Object = MibTableRow
upsBaseConfigDeviceEntry = _UpsBaseConfigDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 1, 2, 1)
)
upsBaseConfigDeviceEntry.setIndexNames(
    (0, "XPPC-MIB", "indexOfDevice"),
)
if mibBuilder.loadTexts:
    upsBaseConfigDeviceEntry.setStatus("mandatory")
_IndexOfDevice_Type = Integer32
_IndexOfDevice_Object = MibTableColumn
indexOfDevice = _IndexOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 1, 2, 1, 1),
    _IndexOfDevice_Type()
)
indexOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indexOfDevice.setStatus("mandatory")
_NameOfDevice_Type = DisplayString
_NameOfDevice_Object = MibTableColumn
nameOfDevice = _NameOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 1, 2, 1, 2),
    _NameOfDevice_Type()
)
nameOfDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameOfDevice.setStatus("mandatory")
_VaRatingOfDevice_Type = Integer32
_VaRatingOfDevice_Object = MibTableColumn
vaRatingOfDevice = _VaRatingOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 1, 2, 1, 3),
    _VaRatingOfDevice_Type()
)
vaRatingOfDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vaRatingOfDevice.setStatus("mandatory")


class _DeviceAccept_Type(Integer32):
    """Custom type deviceAccept based on Integer32"""
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


_DeviceAccept_Type.__name__ = "Integer32"
_DeviceAccept_Object = MibTableColumn
deviceAccept = _DeviceAccept_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 1, 2, 1, 4),
    _DeviceAccept_Type()
)
deviceAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceAccept.setStatus("mandatory")
_UpsSmartConfig_ObjectIdentity = ObjectIdentity
upsSmartConfig = _UpsSmartConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2)
)
_UpsSmartConfigRatedOutputVoltage_Type = Integer32
_UpsSmartConfigRatedOutputVoltage_Object = MibScalar
upsSmartConfigRatedOutputVoltage = _UpsSmartConfigRatedOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 1),
    _UpsSmartConfigRatedOutputVoltage_Type()
)
upsSmartConfigRatedOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigRatedOutputVoltage.setStatus("mandatory")
_UpsSmartConfigHighTransferVolt_Type = Integer32
_UpsSmartConfigHighTransferVolt_Object = MibScalar
upsSmartConfigHighTransferVolt = _UpsSmartConfigHighTransferVolt_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 2),
    _UpsSmartConfigHighTransferVolt_Type()
)
upsSmartConfigHighTransferVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigHighTransferVolt.setStatus("mandatory")
_UpsSmartConfigLowTransferVolt_Type = Integer32
_UpsSmartConfigLowTransferVolt_Object = MibScalar
upsSmartConfigLowTransferVolt = _UpsSmartConfigLowTransferVolt_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 3),
    _UpsSmartConfigLowTransferVolt_Type()
)
upsSmartConfigLowTransferVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigLowTransferVolt.setStatus("mandatory")


class _UpsSmartConfigAlarm_Type(Integer32):
    """Custom type upsSmartConfigAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atLowBattery", 2),
          ("never", 3),
          ("timed", 1))
    )


_UpsSmartConfigAlarm_Type.__name__ = "Integer32"
_UpsSmartConfigAlarm_Object = MibScalar
upsSmartConfigAlarm = _UpsSmartConfigAlarm_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 4),
    _UpsSmartConfigAlarm_Type()
)
upsSmartConfigAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigAlarm.setStatus("mandatory")
_UpsSmartConfigAlarmTimer_Type = Integer32
_UpsSmartConfigAlarmTimer_Object = MibScalar
upsSmartConfigAlarmTimer = _UpsSmartConfigAlarmTimer_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 5),
    _UpsSmartConfigAlarmTimer_Type()
)
upsSmartConfigAlarmTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigAlarmTimer.setStatus("mandatory")
_UpsSmartConfigMinReturnCapacity_Type = Integer32
_UpsSmartConfigMinReturnCapacity_Object = MibScalar
upsSmartConfigMinReturnCapacity = _UpsSmartConfigMinReturnCapacity_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 6),
    _UpsSmartConfigMinReturnCapacity_Type()
)
upsSmartConfigMinReturnCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigMinReturnCapacity.setStatus("mandatory")


class _UpsSmartConfigSensitivity_Type(Integer32):
    """Custom type upsSmartConfigSensitivity based on Integer32"""
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
        *(("auto", 1),
          ("high", 4),
          ("low", 2),
          ("medium", 3))
    )


_UpsSmartConfigSensitivity_Type.__name__ = "Integer32"
_UpsSmartConfigSensitivity_Object = MibScalar
upsSmartConfigSensitivity = _UpsSmartConfigSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 7),
    _UpsSmartConfigSensitivity_Type()
)
upsSmartConfigSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigSensitivity.setStatus("mandatory")
_UpsSmartConfigLowBatteryRunTime_Type = Integer32
_UpsSmartConfigLowBatteryRunTime_Object = MibScalar
upsSmartConfigLowBatteryRunTime = _UpsSmartConfigLowBatteryRunTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 8),
    _UpsSmartConfigLowBatteryRunTime_Type()
)
upsSmartConfigLowBatteryRunTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigLowBatteryRunTime.setStatus("mandatory")
_UpsSmartConfigReturnDelay_Type = Integer32
_UpsSmartConfigReturnDelay_Object = MibScalar
upsSmartConfigReturnDelay = _UpsSmartConfigReturnDelay_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 9),
    _UpsSmartConfigReturnDelay_Type()
)
upsSmartConfigReturnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigReturnDelay.setStatus("mandatory")
_UpsSmartConfigShutoffDelay_Type = Integer32
_UpsSmartConfigShutoffDelay_Object = MibScalar
upsSmartConfigShutoffDelay = _UpsSmartConfigShutoffDelay_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 10),
    _UpsSmartConfigShutoffDelay_Type()
)
upsSmartConfigShutoffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigShutoffDelay.setStatus("mandatory")
_UpsSmartConfigUpsSleepTime_Type = Integer32
_UpsSmartConfigUpsSleepTime_Object = MibScalar
upsSmartConfigUpsSleepTime = _UpsSmartConfigUpsSleepTime_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 11),
    _UpsSmartConfigUpsSleepTime_Type()
)
upsSmartConfigUpsSleepTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigUpsSleepTime.setStatus("mandatory")


class _UpsSmartConfigSetEEPROMDefaults_Type(Integer32):
    """Custom type upsSmartConfigSetEEPROMDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSetEEPROMDefaults", 1),
          ("setEEPROMDefaults", 2))
    )


_UpsSmartConfigSetEEPROMDefaults_Type.__name__ = "Integer32"
_UpsSmartConfigSetEEPROMDefaults_Object = MibScalar
upsSmartConfigSetEEPROMDefaults = _UpsSmartConfigSetEEPROMDefaults_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 5, 2, 12),
    _UpsSmartConfigSetEEPROMDefaults_Type()
)
upsSmartConfigSetEEPROMDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartConfigSetEEPROMDefaults.setStatus("mandatory")
_UpsControlp_ObjectIdentity = ObjectIdentity
upsControlp = _UpsControlp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 6)
)
_UpsBaseControl_ObjectIdentity = ObjectIdentity
upsBaseControl = _UpsBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 6, 1)
)


class _UpsBaseControlConserveBattery_Type(Integer32):
    """Custom type upsBaseControlConserveBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTurnOffUps", 1),
          ("turnUpsOffToConserveBattery", 2),
          ("turnUpsOffToConserveBatteryDelay", 3))
    )


_UpsBaseControlConserveBattery_Type.__name__ = "Integer32"
_UpsBaseControlConserveBattery_Object = MibScalar
upsBaseControlConserveBattery = _UpsBaseControlConserveBattery_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 6, 1, 1),
    _UpsBaseControlConserveBattery_Type()
)
upsBaseControlConserveBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBaseControlConserveBattery.setStatus("mandatory")
_UpsSmartControl_ObjectIdentity = ObjectIdentity
upsSmartControl = _UpsSmartControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 6, 2)
)


class _UpsSmartControlUpsOff_Type(Integer32):
    """Custom type upsSmartControlUpsOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTurnUpsOff", 1),
          ("turnUpsOff", 2))
    )


_UpsSmartControlUpsOff_Type.__name__ = "Integer32"
_UpsSmartControlUpsOff_Object = MibScalar
upsSmartControlUpsOff = _UpsSmartControlUpsOff_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 6, 2, 1),
    _UpsSmartControlUpsOff_Type()
)
upsSmartControlUpsOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartControlUpsOff.setStatus("mandatory")


class _UpsSmartControlRebootUps_Type(Integer32):
    """Custom type upsSmartControlRebootUps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRebootUps", 1),
          ("rebootUps", 2))
    )


_UpsSmartControlRebootUps_Type.__name__ = "Integer32"
_UpsSmartControlRebootUps_Object = MibScalar
upsSmartControlRebootUps = _UpsSmartControlRebootUps_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 6, 2, 2),
    _UpsSmartControlRebootUps_Type()
)
upsSmartControlRebootUps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartControlRebootUps.setStatus("mandatory")


class _UpsSmartControlUpsSleep_Type(Integer32):
    """Custom type upsSmartControlUpsSleep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPutUpsToSleep", 1),
          ("putUpsToSleep", 2))
    )


_UpsSmartControlUpsSleep_Type.__name__ = "Integer32"
_UpsSmartControlUpsSleep_Object = MibScalar
upsSmartControlUpsSleep = _UpsSmartControlUpsSleep_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 6, 2, 3),
    _UpsSmartControlUpsSleep_Type()
)
upsSmartControlUpsSleep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartControlUpsSleep.setStatus("mandatory")


class _UpsSmartControlSimulatePowerFail_Type(Integer32):
    """Custom type upsSmartControlSimulatePowerFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSimulatePowerFailure", 1),
          ("simulatePowerFailure", 2))
    )


_UpsSmartControlSimulatePowerFail_Type.__name__ = "Integer32"
_UpsSmartControlSimulatePowerFail_Object = MibScalar
upsSmartControlSimulatePowerFail = _UpsSmartControlSimulatePowerFail_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 6, 2, 4),
    _UpsSmartControlSimulatePowerFail_Type()
)
upsSmartControlSimulatePowerFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartControlSimulatePowerFail.setStatus("mandatory")


class _UpsSmartControlFlashAndBeep_Type(Integer32):
    """Custom type upsSmartControlFlashAndBeep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flashAndBeep", 2),
          ("noFlashAndBeep", 1))
    )


_UpsSmartControlFlashAndBeep_Type.__name__ = "Integer32"
_UpsSmartControlFlashAndBeep_Object = MibScalar
upsSmartControlFlashAndBeep = _UpsSmartControlFlashAndBeep_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 6, 2, 5),
    _UpsSmartControlFlashAndBeep_Type()
)
upsSmartControlFlashAndBeep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartControlFlashAndBeep.setStatus("mandatory")


class _UpsSmartControlTurnOnUpsLoad_Type(Integer32):
    """Custom type upsSmartControlTurnOnUpsLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noUpsSmartControlTurnOnUpsLoad", 1),
          ("upsSmartControlTurnOnUpsLoad", 2))
    )


_UpsSmartControlTurnOnUpsLoad_Type.__name__ = "Integer32"
_UpsSmartControlTurnOnUpsLoad_Object = MibScalar
upsSmartControlTurnOnUpsLoad = _UpsSmartControlTurnOnUpsLoad_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 6, 2, 6),
    _UpsSmartControlTurnOnUpsLoad_Type()
)
upsSmartControlTurnOnUpsLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartControlTurnOnUpsLoad.setStatus("mandatory")
_UpsTestp_ObjectIdentity = ObjectIdentity
upsTestp = _UpsTestp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 7)
)
_UpsBaseTest_ObjectIdentity = ObjectIdentity
upsBaseTest = _UpsBaseTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 7, 1)
)
_UpsSmartTest_ObjectIdentity = ObjectIdentity
upsSmartTest = _UpsSmartTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 7, 2)
)


class _UpsSmartTestDiagnosticSchedule_Type(Integer32):
    """Custom type upsSmartTestDiagnosticSchedule based on Integer32"""
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
        *(("biweekly", 2),
          ("never", 4),
          ("unknown", 1),
          ("weekly", 3))
    )


_UpsSmartTestDiagnosticSchedule_Type.__name__ = "Integer32"
_UpsSmartTestDiagnosticSchedule_Object = MibScalar
upsSmartTestDiagnosticSchedule = _UpsSmartTestDiagnosticSchedule_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 7, 2, 1),
    _UpsSmartTestDiagnosticSchedule_Type()
)
upsSmartTestDiagnosticSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartTestDiagnosticSchedule.setStatus("mandatory")


class _UpsSmartTestDiagnostics_Type(Integer32):
    """Custom type upsSmartTestDiagnostics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTestDiagnostics", 1),
          ("testDiagnostics", 2))
    )


_UpsSmartTestDiagnostics_Type.__name__ = "Integer32"
_UpsSmartTestDiagnostics_Object = MibScalar
upsSmartTestDiagnostics = _UpsSmartTestDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 7, 2, 2),
    _UpsSmartTestDiagnostics_Type()
)
upsSmartTestDiagnostics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartTestDiagnostics.setStatus("mandatory")


class _UpsSmartTestDiagnosticsResults_Type(Integer32):
    """Custom type upsSmartTestDiagnosticsResults based on Integer32"""
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
        *(("failed", 2),
          ("invalidTest", 3),
          ("ok", 1),
          ("testInProgress", 4))
    )


_UpsSmartTestDiagnosticsResults_Type.__name__ = "Integer32"
_UpsSmartTestDiagnosticsResults_Object = MibScalar
upsSmartTestDiagnosticsResults = _UpsSmartTestDiagnosticsResults_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 7, 2, 3),
    _UpsSmartTestDiagnosticsResults_Type()
)
upsSmartTestDiagnosticsResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartTestDiagnosticsResults.setStatus("mandatory")
_UpsSmartTestLastDiagnosticsDate_Type = DisplayString
_UpsSmartTestLastDiagnosticsDate_Object = MibScalar
upsSmartTestLastDiagnosticsDate = _UpsSmartTestLastDiagnosticsDate_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 7, 2, 4),
    _UpsSmartTestLastDiagnosticsDate_Type()
)
upsSmartTestLastDiagnosticsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartTestLastDiagnosticsDate.setStatus("mandatory")


class _UpsSmartTestIndicators_Type(Integer32):
    """Custom type upsSmartTestIndicators based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTestIndicators", 1),
          ("testIndicators", 2))
    )


_UpsSmartTestIndicators_Type.__name__ = "Integer32"
_UpsSmartTestIndicators_Object = MibScalar
upsSmartTestIndicators = _UpsSmartTestIndicators_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 7, 2, 5),
    _UpsSmartTestIndicators_Type()
)
upsSmartTestIndicators.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartTestIndicators.setStatus("mandatory")


class _UpsSmartTestRuntimeCalibration_Type(Integer32):
    """Custom type upsSmartTestRuntimeCalibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cancelCurrentCalibration", 3),
          ("noPerformCalibration", 1),
          ("performCalibration", 2))
    )


_UpsSmartTestRuntimeCalibration_Type.__name__ = "Integer32"
_UpsSmartTestRuntimeCalibration_Object = MibScalar
upsSmartTestRuntimeCalibration = _UpsSmartTestRuntimeCalibration_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 7, 2, 6),
    _UpsSmartTestRuntimeCalibration_Type()
)
upsSmartTestRuntimeCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsSmartTestRuntimeCalibration.setStatus("mandatory")


class _UpsSmartTestCalibrationResults_Type(Integer32):
    """Custom type upsSmartTestCalibrationResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("calibrationInProgress", 3),
          ("invalidTest", 2),
          ("ok", 1))
    )


_UpsSmartTestCalibrationResults_Type.__name__ = "Integer32"
_UpsSmartTestCalibrationResults_Object = MibScalar
upsSmartTestCalibrationResults = _UpsSmartTestCalibrationResults_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 7, 2, 7),
    _UpsSmartTestCalibrationResults_Type()
)
upsSmartTestCalibrationResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartTestCalibrationResults.setStatus("mandatory")
_UpsSmartTestCalibrationDate_Type = DisplayString
_UpsSmartTestCalibrationDate_Object = MibScalar
upsSmartTestCalibrationDate = _UpsSmartTestCalibrationDate_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 7, 2, 8),
    _UpsSmartTestCalibrationDate_Type()
)
upsSmartTestCalibrationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSmartTestCalibrationDate.setStatus("mandatory")
_UpsThreePhase_ObjectIdentity = ObjectIdentity
upsThreePhase = _UpsThreePhase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8)
)
_UpsThreePhaseBatteryGrp_ObjectIdentity = ObjectIdentity
upsThreePhaseBatteryGrp = _UpsThreePhaseBatteryGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 1)
)
_UpsThreePhaseBatteryVoltage_Type = Integer32
_UpsThreePhaseBatteryVoltage_Object = MibScalar
upsThreePhaseBatteryVoltage = _UpsThreePhaseBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 1, 1),
    _UpsThreePhaseBatteryVoltage_Type()
)
upsThreePhaseBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseBatteryVoltage.setStatus("mandatory")
_UpsThreePhaseBatteryCapacityPercentage_Type = Integer32
_UpsThreePhaseBatteryCapacityPercentage_Object = MibScalar
upsThreePhaseBatteryCapacityPercentage = _UpsThreePhaseBatteryCapacityPercentage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 1, 2),
    _UpsThreePhaseBatteryCapacityPercentage_Type()
)
upsThreePhaseBatteryCapacityPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseBatteryCapacityPercentage.setStatus("mandatory")
_UpsThreePhaseBatteryTimeRemain_Type = Integer32
_UpsThreePhaseBatteryTimeRemain_Object = MibScalar
upsThreePhaseBatteryTimeRemain = _UpsThreePhaseBatteryTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 1, 3),
    _UpsThreePhaseBatteryTimeRemain_Type()
)
upsThreePhaseBatteryTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseBatteryTimeRemain.setStatus("mandatory")
_UpsThreePhaseBatteryCurrent_Type = Integer32
_UpsThreePhaseBatteryCurrent_Object = MibScalar
upsThreePhaseBatteryCurrent = _UpsThreePhaseBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 1, 4),
    _UpsThreePhaseBatteryCurrent_Type()
)
upsThreePhaseBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseBatteryCurrent.setStatus("mandatory")
_UpsThreePhaseBatteryTemperature_Type = Integer32
_UpsThreePhaseBatteryTemperature_Object = MibScalar
upsThreePhaseBatteryTemperature = _UpsThreePhaseBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 1, 5),
    _UpsThreePhaseBatteryTemperature_Type()
)
upsThreePhaseBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseBatteryTemperature.setStatus("mandatory")
_UpsThreePhaseInputGrp_ObjectIdentity = ObjectIdentity
upsThreePhaseInputGrp = _UpsThreePhaseInputGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 2)
)
_UpsThreePhaseInputFrequency_Type = Integer32
_UpsThreePhaseInputFrequency_Object = MibScalar
upsThreePhaseInputFrequency = _UpsThreePhaseInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 2, 1),
    _UpsThreePhaseInputFrequency_Type()
)
upsThreePhaseInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseInputFrequency.setStatus("mandatory")
_UpsThreePhaseInputVoltageR_Type = Integer32
_UpsThreePhaseInputVoltageR_Object = MibScalar
upsThreePhaseInputVoltageR = _UpsThreePhaseInputVoltageR_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 2, 2),
    _UpsThreePhaseInputVoltageR_Type()
)
upsThreePhaseInputVoltageR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseInputVoltageR.setStatus("mandatory")
_UpsThreePhaseInputVoltageS_Type = Integer32
_UpsThreePhaseInputVoltageS_Object = MibScalar
upsThreePhaseInputVoltageS = _UpsThreePhaseInputVoltageS_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 2, 3),
    _UpsThreePhaseInputVoltageS_Type()
)
upsThreePhaseInputVoltageS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseInputVoltageS.setStatus("mandatory")
_UpsThreePhaseInputVoltageT_Type = Integer32
_UpsThreePhaseInputVoltageT_Object = MibScalar
upsThreePhaseInputVoltageT = _UpsThreePhaseInputVoltageT_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 2, 4),
    _UpsThreePhaseInputVoltageT_Type()
)
upsThreePhaseInputVoltageT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseInputVoltageT.setStatus("mandatory")
_UpsThreePhaseOutputGrp_ObjectIdentity = ObjectIdentity
upsThreePhaseOutputGrp = _UpsThreePhaseOutputGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 3)
)
_UpsThreePhaseOutputFrequency_Type = Integer32
_UpsThreePhaseOutputFrequency_Object = MibScalar
upsThreePhaseOutputFrequency = _UpsThreePhaseOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 3, 1),
    _UpsThreePhaseOutputFrequency_Type()
)
upsThreePhaseOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseOutputFrequency.setStatus("mandatory")
_UpsThreePhaseOutputVoltageR_Type = Integer32
_UpsThreePhaseOutputVoltageR_Object = MibScalar
upsThreePhaseOutputVoltageR = _UpsThreePhaseOutputVoltageR_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 3, 2),
    _UpsThreePhaseOutputVoltageR_Type()
)
upsThreePhaseOutputVoltageR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseOutputVoltageR.setStatus("mandatory")
_UpsThreePhaseOutputVoltageS_Type = Integer32
_UpsThreePhaseOutputVoltageS_Object = MibScalar
upsThreePhaseOutputVoltageS = _UpsThreePhaseOutputVoltageS_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 3, 3),
    _UpsThreePhaseOutputVoltageS_Type()
)
upsThreePhaseOutputVoltageS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseOutputVoltageS.setStatus("mandatory")
_UpsThreePhaseOutputVoltageT_Type = Integer32
_UpsThreePhaseOutputVoltageT_Object = MibScalar
upsThreePhaseOutputVoltageT = _UpsThreePhaseOutputVoltageT_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 3, 4),
    _UpsThreePhaseOutputVoltageT_Type()
)
upsThreePhaseOutputVoltageT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseOutputVoltageT.setStatus("mandatory")
_UpsThreePhaseOutputLoadPercentageR_Type = Integer32
_UpsThreePhaseOutputLoadPercentageR_Object = MibScalar
upsThreePhaseOutputLoadPercentageR = _UpsThreePhaseOutputLoadPercentageR_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 3, 5),
    _UpsThreePhaseOutputLoadPercentageR_Type()
)
upsThreePhaseOutputLoadPercentageR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseOutputLoadPercentageR.setStatus("mandatory")
_UpsThreePhaseOutputLoadPercentageS_Type = Integer32
_UpsThreePhaseOutputLoadPercentageS_Object = MibScalar
upsThreePhaseOutputLoadPercentageS = _UpsThreePhaseOutputLoadPercentageS_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 3, 6),
    _UpsThreePhaseOutputLoadPercentageS_Type()
)
upsThreePhaseOutputLoadPercentageS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseOutputLoadPercentageS.setStatus("mandatory")
_UpsThreePhaseOutputLoadPercentageT_Type = Integer32
_UpsThreePhaseOutputLoadPercentageT_Object = MibScalar
upsThreePhaseOutputLoadPercentageT = _UpsThreePhaseOutputLoadPercentageT_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 3, 7),
    _UpsThreePhaseOutputLoadPercentageT_Type()
)
upsThreePhaseOutputLoadPercentageT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseOutputLoadPercentageT.setStatus("mandatory")
_UpsThreePhaseBypassGrp_ObjectIdentity = ObjectIdentity
upsThreePhaseBypassGrp = _UpsThreePhaseBypassGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 4)
)
_UpsThreePhaseBypassSourceFrequency_Type = Integer32
_UpsThreePhaseBypassSourceFrequency_Object = MibScalar
upsThreePhaseBypassSourceFrequency = _UpsThreePhaseBypassSourceFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 4, 1),
    _UpsThreePhaseBypassSourceFrequency_Type()
)
upsThreePhaseBypassSourceFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseBypassSourceFrequency.setStatus("mandatory")
_UpsThreePhaseBypssSourceVoltageR_Type = Integer32
_UpsThreePhaseBypssSourceVoltageR_Object = MibScalar
upsThreePhaseBypssSourceVoltageR = _UpsThreePhaseBypssSourceVoltageR_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 4, 2),
    _UpsThreePhaseBypssSourceVoltageR_Type()
)
upsThreePhaseBypssSourceVoltageR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseBypssSourceVoltageR.setStatus("mandatory")
_UpsThreePhaseBypssSourceVoltageS_Type = Integer32
_UpsThreePhaseBypssSourceVoltageS_Object = MibScalar
upsThreePhaseBypssSourceVoltageS = _UpsThreePhaseBypssSourceVoltageS_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 4, 3),
    _UpsThreePhaseBypssSourceVoltageS_Type()
)
upsThreePhaseBypssSourceVoltageS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseBypssSourceVoltageS.setStatus("mandatory")
_UpsThreePhaseBypssSourceVoltageT_Type = Integer32
_UpsThreePhaseBypssSourceVoltageT_Object = MibScalar
upsThreePhaseBypssSourceVoltageT = _UpsThreePhaseBypssSourceVoltageT_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 4, 4),
    _UpsThreePhaseBypssSourceVoltageT_Type()
)
upsThreePhaseBypssSourceVoltageT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseBypssSourceVoltageT.setStatus("mandatory")
_UpsThreePhaseDCandRectifierStatusGrp_ObjectIdentity = ObjectIdentity
upsThreePhaseDCandRectifierStatusGrp = _UpsThreePhaseDCandRectifierStatusGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 5)
)


class _UpsThreePhaseDCandRectifierStatusRecRotError_Type(Integer32):
    """Custom type upsThreePhaseDCandRectifierStatusRecRotError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseDCandRectifierStatusRecRotError_Type.__name__ = "Integer32"
_UpsThreePhaseDCandRectifierStatusRecRotError_Object = MibScalar
upsThreePhaseDCandRectifierStatusRecRotError = _UpsThreePhaseDCandRectifierStatusRecRotError_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 5, 1),
    _UpsThreePhaseDCandRectifierStatusRecRotError_Type()
)
upsThreePhaseDCandRectifierStatusRecRotError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseDCandRectifierStatusRecRotError.setStatus("mandatory")


class _UpsThreePhaseDCandRectifierStatusLowBatteryShutdown_Type(Integer32):
    """Custom type upsThreePhaseDCandRectifierStatusLowBatteryShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseDCandRectifierStatusLowBatteryShutdown_Type.__name__ = "Integer32"
_UpsThreePhaseDCandRectifierStatusLowBatteryShutdown_Object = MibScalar
upsThreePhaseDCandRectifierStatusLowBatteryShutdown = _UpsThreePhaseDCandRectifierStatusLowBatteryShutdown_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 5, 2),
    _UpsThreePhaseDCandRectifierStatusLowBatteryShutdown_Type()
)
upsThreePhaseDCandRectifierStatusLowBatteryShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseDCandRectifierStatusLowBatteryShutdown.setStatus("mandatory")


class _UpsThreePhaseDCandRectifierStatusLowBattery_Type(Integer32):
    """Custom type upsThreePhaseDCandRectifierStatusLowBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseDCandRectifierStatusLowBattery_Type.__name__ = "Integer32"
_UpsThreePhaseDCandRectifierStatusLowBattery_Object = MibScalar
upsThreePhaseDCandRectifierStatusLowBattery = _UpsThreePhaseDCandRectifierStatusLowBattery_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 5, 3),
    _UpsThreePhaseDCandRectifierStatusLowBattery_Type()
)
upsThreePhaseDCandRectifierStatusLowBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseDCandRectifierStatusLowBattery.setStatus("mandatory")


class _UpsThreePhaseDCandRectifierStatusInAndOut_Type(Integer32):
    """Custom type upsThreePhaseDCandRectifierStatusInAndOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("threeInOneOut", 2),
          ("threeInThreeOut", 3))
    )


_UpsThreePhaseDCandRectifierStatusInAndOut_Type.__name__ = "Integer32"
_UpsThreePhaseDCandRectifierStatusInAndOut_Object = MibScalar
upsThreePhaseDCandRectifierStatusInAndOut = _UpsThreePhaseDCandRectifierStatusInAndOut_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 5, 4),
    _UpsThreePhaseDCandRectifierStatusInAndOut_Type()
)
upsThreePhaseDCandRectifierStatusInAndOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseDCandRectifierStatusInAndOut.setStatus("mandatory")


class _UpsThreePhaseDCandRectifierStatusBatteryStatus_Type(Integer32):
    """Custom type upsThreePhaseDCandRectifierStatusBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acnormal", 5),
          ("backup", 4))
    )


_UpsThreePhaseDCandRectifierStatusBatteryStatus_Type.__name__ = "Integer32"
_UpsThreePhaseDCandRectifierStatusBatteryStatus_Object = MibScalar
upsThreePhaseDCandRectifierStatusBatteryStatus = _UpsThreePhaseDCandRectifierStatusBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 5, 5),
    _UpsThreePhaseDCandRectifierStatusBatteryStatus_Type()
)
upsThreePhaseDCandRectifierStatusBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseDCandRectifierStatusBatteryStatus.setStatus("mandatory")


class _UpsThreePhaseDCandRectifierStatusChargeStatus_Type(Integer32):
    """Custom type upsThreePhaseDCandRectifierStatusChargeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              16)
        )
    )
    namedValues = NamedValues(
        *(("boost", 6),
          ("float", 7),
          ("no", 16))
    )


_UpsThreePhaseDCandRectifierStatusChargeStatus_Type.__name__ = "Integer32"
_UpsThreePhaseDCandRectifierStatusChargeStatus_Object = MibScalar
upsThreePhaseDCandRectifierStatusChargeStatus = _UpsThreePhaseDCandRectifierStatusChargeStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 5, 6),
    _UpsThreePhaseDCandRectifierStatusChargeStatus_Type()
)
upsThreePhaseDCandRectifierStatusChargeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseDCandRectifierStatusChargeStatus.setStatus("mandatory")


class _UpsThreePhaseDCandRectifierStatusRecOperating_Type(Integer32):
    """Custom type upsThreePhaseDCandRectifierStatusRecOperating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseDCandRectifierStatusRecOperating_Type.__name__ = "Integer32"
_UpsThreePhaseDCandRectifierStatusRecOperating_Object = MibScalar
upsThreePhaseDCandRectifierStatusRecOperating = _UpsThreePhaseDCandRectifierStatusRecOperating_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 5, 7),
    _UpsThreePhaseDCandRectifierStatusRecOperating_Type()
)
upsThreePhaseDCandRectifierStatusRecOperating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseDCandRectifierStatusRecOperating.setStatus("mandatory")
_UpsThreePhaseUPSStatusGrp_ObjectIdentity = ObjectIdentity
upsThreePhaseUPSStatusGrp = _UpsThreePhaseUPSStatusGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 6)
)


class _UpsThreePhaseUPSStatusBypassFreqFail_Type(Integer32):
    """Custom type upsThreePhaseUPSStatusBypassFreqFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseUPSStatusBypassFreqFail_Type.__name__ = "Integer32"
_UpsThreePhaseUPSStatusBypassFreqFail_Object = MibScalar
upsThreePhaseUPSStatusBypassFreqFail = _UpsThreePhaseUPSStatusBypassFreqFail_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 6, 1),
    _UpsThreePhaseUPSStatusBypassFreqFail_Type()
)
upsThreePhaseUPSStatusBypassFreqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseUPSStatusBypassFreqFail.setStatus("mandatory")


class _UpsThreePhaseUPSStatusManualBypassBreaker_Type(Integer32):
    """Custom type upsThreePhaseUPSStatusManualBypassBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("close", 8),
          ("open", 9))
    )


_UpsThreePhaseUPSStatusManualBypassBreaker_Type.__name__ = "Integer32"
_UpsThreePhaseUPSStatusManualBypassBreaker_Object = MibScalar
upsThreePhaseUPSStatusManualBypassBreaker = _UpsThreePhaseUPSStatusManualBypassBreaker_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 6, 2),
    _UpsThreePhaseUPSStatusManualBypassBreaker_Type()
)
upsThreePhaseUPSStatusManualBypassBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseUPSStatusManualBypassBreaker.setStatus("mandatory")


class _UpsThreePhaseUPSStatusACStatus_Type(Integer32):
    """Custom type upsThreePhaseUPSStatusACStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 11),
          ("normal", 10))
    )


_UpsThreePhaseUPSStatusACStatus_Type.__name__ = "Integer32"
_UpsThreePhaseUPSStatusACStatus_Object = MibScalar
upsThreePhaseUPSStatusACStatus = _UpsThreePhaseUPSStatusACStatus_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 6, 3),
    _UpsThreePhaseUPSStatusACStatus_Type()
)
upsThreePhaseUPSStatusACStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseUPSStatusACStatus.setStatus("mandatory")


class _UpsThreePhaseUPSStaticSwitchMode_Type(Integer32):
    """Custom type upsThreePhaseUPSStaticSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("bypassmode", 13),
          ("invermode", 12))
    )


_UpsThreePhaseUPSStaticSwitchMode_Type.__name__ = "Integer32"
_UpsThreePhaseUPSStaticSwitchMode_Object = MibScalar
upsThreePhaseUPSStaticSwitchMode = _UpsThreePhaseUPSStaticSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 6, 4),
    _UpsThreePhaseUPSStaticSwitchMode_Type()
)
upsThreePhaseUPSStaticSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseUPSStaticSwitchMode.setStatus("mandatory")


class _UpsThreePhaseUPSStatusInverterOperating_Type(Integer32):
    """Custom type upsThreePhaseUPSStatusInverterOperating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseUPSStatusInverterOperating_Type.__name__ = "Integer32"
_UpsThreePhaseUPSStatusInverterOperating_Object = MibScalar
upsThreePhaseUPSStatusInverterOperating = _UpsThreePhaseUPSStatusInverterOperating_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 6, 5),
    _UpsThreePhaseUPSStatusInverterOperating_Type()
)
upsThreePhaseUPSStatusInverterOperating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseUPSStatusInverterOperating.setStatus("mandatory")
_UpsThreePhaseFaultStatusGrp_ObjectIdentity = ObjectIdentity
upsThreePhaseFaultStatusGrp = _UpsThreePhaseFaultStatusGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 7)
)


class _UpsThreePhaseFaultStatusEmergencyStop_Type(Integer32):
    """Custom type upsThreePhaseFaultStatusEmergencyStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseFaultStatusEmergencyStop_Type.__name__ = "Integer32"
_UpsThreePhaseFaultStatusEmergencyStop_Object = MibScalar
upsThreePhaseFaultStatusEmergencyStop = _UpsThreePhaseFaultStatusEmergencyStop_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 7, 1),
    _UpsThreePhaseFaultStatusEmergencyStop_Type()
)
upsThreePhaseFaultStatusEmergencyStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseFaultStatusEmergencyStop.setStatus("mandatory")


class _UpsThreePhaseFaultStatusHighDCShutdown_Type(Integer32):
    """Custom type upsThreePhaseFaultStatusHighDCShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseFaultStatusHighDCShutdown_Type.__name__ = "Integer32"
_UpsThreePhaseFaultStatusHighDCShutdown_Object = MibScalar
upsThreePhaseFaultStatusHighDCShutdown = _UpsThreePhaseFaultStatusHighDCShutdown_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 7, 2),
    _UpsThreePhaseFaultStatusHighDCShutdown_Type()
)
upsThreePhaseFaultStatusHighDCShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseFaultStatusHighDCShutdown.setStatus("mandatory")


class _UpsThreePhaseFaultStatusBypassBreaker_Type(Integer32):
    """Custom type upsThreePhaseFaultStatusBypassBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseFaultStatusBypassBreaker_Type.__name__ = "Integer32"
_UpsThreePhaseFaultStatusBypassBreaker_Object = MibScalar
upsThreePhaseFaultStatusBypassBreaker = _UpsThreePhaseFaultStatusBypassBreaker_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 7, 3),
    _UpsThreePhaseFaultStatusBypassBreaker_Type()
)
upsThreePhaseFaultStatusBypassBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseFaultStatusBypassBreaker.setStatus("mandatory")


class _UpsThreePhaseFaultStatusOverLoad_Type(Integer32):
    """Custom type upsThreePhaseFaultStatusOverLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseFaultStatusOverLoad_Type.__name__ = "Integer32"
_UpsThreePhaseFaultStatusOverLoad_Object = MibScalar
upsThreePhaseFaultStatusOverLoad = _UpsThreePhaseFaultStatusOverLoad_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 7, 4),
    _UpsThreePhaseFaultStatusOverLoad_Type()
)
upsThreePhaseFaultStatusOverLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseFaultStatusOverLoad.setStatus("mandatory")


class _UpsThreePhaseFaultStatusInverterOutputFail_Type(Integer32):
    """Custom type upsThreePhaseFaultStatusInverterOutputFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseFaultStatusInverterOutputFail_Type.__name__ = "Integer32"
_UpsThreePhaseFaultStatusInverterOutputFail_Object = MibScalar
upsThreePhaseFaultStatusInverterOutputFail = _UpsThreePhaseFaultStatusInverterOutputFail_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 7, 5),
    _UpsThreePhaseFaultStatusInverterOutputFail_Type()
)
upsThreePhaseFaultStatusInverterOutputFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseFaultStatusInverterOutputFail.setStatus("mandatory")


class _UpsThreePhaseFaultStatusOverTemperature_Type(Integer32):
    """Custom type upsThreePhaseFaultStatusOverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseFaultStatusOverTemperature_Type.__name__ = "Integer32"
_UpsThreePhaseFaultStatusOverTemperature_Object = MibScalar
upsThreePhaseFaultStatusOverTemperature = _UpsThreePhaseFaultStatusOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 7, 6),
    _UpsThreePhaseFaultStatusOverTemperature_Type()
)
upsThreePhaseFaultStatusOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseFaultStatusOverTemperature.setStatus("mandatory")


class _UpsThreePhaseFaultStatusShortCircuit_Type(Integer32):
    """Custom type upsThreePhaseFaultStatusShortCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("no", 16),
          ("yes", 14))
    )


_UpsThreePhaseFaultStatusShortCircuit_Type.__name__ = "Integer32"
_UpsThreePhaseFaultStatusShortCircuit_Object = MibScalar
upsThreePhaseFaultStatusShortCircuit = _UpsThreePhaseFaultStatusShortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 7, 7),
    _UpsThreePhaseFaultStatusShortCircuit_Type()
)
upsThreePhaseFaultStatusShortCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseFaultStatusShortCircuit.setStatus("mandatory")
_UpsThreePhaseRatingGrp_ObjectIdentity = ObjectIdentity
upsThreePhaseRatingGrp = _UpsThreePhaseRatingGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 8)
)
_UpsThreePhaseRatingRectifierVoltage_Type = DisplayString
_UpsThreePhaseRatingRectifierVoltage_Object = MibScalar
upsThreePhaseRatingRectifierVoltage = _UpsThreePhaseRatingRectifierVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 8, 1),
    _UpsThreePhaseRatingRectifierVoltage_Type()
)
upsThreePhaseRatingRectifierVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseRatingRectifierVoltage.setStatus("mandatory")
_UpsThreePhaseRatingRectifierFrequency_Type = Integer32
_UpsThreePhaseRatingRectifierFrequency_Object = MibScalar
upsThreePhaseRatingRectifierFrequency = _UpsThreePhaseRatingRectifierFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 8, 2),
    _UpsThreePhaseRatingRectifierFrequency_Type()
)
upsThreePhaseRatingRectifierFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseRatingRectifierFrequency.setStatus("mandatory")
_UpsThreePhaseRatingBypassVoltage_Type = DisplayString
_UpsThreePhaseRatingBypassVoltage_Object = MibScalar
upsThreePhaseRatingBypassVoltage = _UpsThreePhaseRatingBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 8, 3),
    _UpsThreePhaseRatingBypassVoltage_Type()
)
upsThreePhaseRatingBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseRatingBypassVoltage.setStatus("mandatory")
_UpsThreePhaseRatingBypassFrequency_Type = Integer32
_UpsThreePhaseRatingBypassFrequency_Object = MibScalar
upsThreePhaseRatingBypassFrequency = _UpsThreePhaseRatingBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 8, 4),
    _UpsThreePhaseRatingBypassFrequency_Type()
)
upsThreePhaseRatingBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseRatingBypassFrequency.setStatus("mandatory")
_UpsThreePhaseRatingOutputVoltage_Type = DisplayString
_UpsThreePhaseRatingOutputVoltage_Object = MibScalar
upsThreePhaseRatingOutputVoltage = _UpsThreePhaseRatingOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 8, 5),
    _UpsThreePhaseRatingOutputVoltage_Type()
)
upsThreePhaseRatingOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseRatingOutputVoltage.setStatus("mandatory")
_UpsThreePhaseRatingOutputFrequency_Type = Integer32
_UpsThreePhaseRatingOutputFrequency_Object = MibScalar
upsThreePhaseRatingOutputFrequency = _UpsThreePhaseRatingOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 8, 6),
    _UpsThreePhaseRatingOutputFrequency_Type()
)
upsThreePhaseRatingOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseRatingOutputFrequency.setStatus("mandatory")
_UpsThreePhaseRatingBatteryVoltage_Type = Integer32
_UpsThreePhaseRatingBatteryVoltage_Object = MibScalar
upsThreePhaseRatingBatteryVoltage = _UpsThreePhaseRatingBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 8, 7),
    _UpsThreePhaseRatingBatteryVoltage_Type()
)
upsThreePhaseRatingBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseRatingBatteryVoltage.setStatus("mandatory")
_UpsThreePhaseRatingPower_Type = DisplayString
_UpsThreePhaseRatingPower_Object = MibScalar
upsThreePhaseRatingPower = _UpsThreePhaseRatingPower_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 8, 8, 8),
    _UpsThreePhaseRatingPower_Type()
)
upsThreePhaseRatingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsThreePhaseRatingPower.setStatus("mandatory")
_UpsEnvironment_ObjectIdentity = ObjectIdentity
upsEnvironment = _UpsEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9)
)
_UpsEnvStatus_ObjectIdentity = ObjectIdentity
upsEnvStatus = _UpsEnvStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1)
)
_UpsEnvTemperature_Type = Integer32
_UpsEnvTemperature_Object = MibScalar
upsEnvTemperature = _UpsEnvTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1, 1),
    _UpsEnvTemperature_Type()
)
upsEnvTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvTemperature.setStatus("mandatory")
_UpsEnvHumidity_Type = Integer32
_UpsEnvHumidity_Object = MibScalar
upsEnvHumidity = _UpsEnvHumidity_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1, 2),
    _UpsEnvHumidity_Type()
)
upsEnvHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvHumidity.setStatus("mandatory")


class _UpsEnvWater_Type(Integer32):
    """Custom type upsEnvWater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_UpsEnvWater_Type.__name__ = "Integer32"
_UpsEnvWater_Object = MibScalar
upsEnvWater = _UpsEnvWater_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1, 3),
    _UpsEnvWater_Type()
)
upsEnvWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvWater.setStatus("mandatory")


class _UpsEnvSmoke_Type(Integer32):
    """Custom type upsEnvSmoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_UpsEnvSmoke_Type.__name__ = "Integer32"
_UpsEnvSmoke_Object = MibScalar
upsEnvSmoke = _UpsEnvSmoke_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1, 4),
    _UpsEnvSmoke_Type()
)
upsEnvSmoke.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvSmoke.setStatus("mandatory")


class _UpsEnvSecurity1_Type(Integer32):
    """Custom type upsEnvSecurity1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_UpsEnvSecurity1_Type.__name__ = "Integer32"
_UpsEnvSecurity1_Object = MibScalar
upsEnvSecurity1 = _UpsEnvSecurity1_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1, 5),
    _UpsEnvSecurity1_Type()
)
upsEnvSecurity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvSecurity1.setStatus("mandatory")


class _UpsEnvSecurity2_Type(Integer32):
    """Custom type upsEnvSecurity2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_UpsEnvSecurity2_Type.__name__ = "Integer32"
_UpsEnvSecurity2_Object = MibScalar
upsEnvSecurity2 = _UpsEnvSecurity2_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1, 6),
    _UpsEnvSecurity2_Type()
)
upsEnvSecurity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvSecurity2.setStatus("mandatory")


class _UpsEnvSecurity3_Type(Integer32):
    """Custom type upsEnvSecurity3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_UpsEnvSecurity3_Type.__name__ = "Integer32"
_UpsEnvSecurity3_Object = MibScalar
upsEnvSecurity3 = _UpsEnvSecurity3_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1, 7),
    _UpsEnvSecurity3_Type()
)
upsEnvSecurity3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvSecurity3.setStatus("mandatory")


class _UpsEnvSecurity4_Type(Integer32):
    """Custom type upsEnvSecurity4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_UpsEnvSecurity4_Type.__name__ = "Integer32"
_UpsEnvSecurity4_Object = MibScalar
upsEnvSecurity4 = _UpsEnvSecurity4_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1, 8),
    _UpsEnvSecurity4_Type()
)
upsEnvSecurity4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvSecurity4.setStatus("mandatory")


class _UpsEnvSecurity5_Type(Integer32):
    """Custom type upsEnvSecurity5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_UpsEnvSecurity5_Type.__name__ = "Integer32"
_UpsEnvSecurity5_Object = MibScalar
upsEnvSecurity5 = _UpsEnvSecurity5_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1, 9),
    _UpsEnvSecurity5_Type()
)
upsEnvSecurity5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvSecurity5.setStatus("mandatory")


class _UpsEnvSecurity6_Type(Integer32):
    """Custom type upsEnvSecurity6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_UpsEnvSecurity6_Type.__name__ = "Integer32"
_UpsEnvSecurity6_Object = MibScalar
upsEnvSecurity6 = _UpsEnvSecurity6_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1, 10),
    _UpsEnvSecurity6_Type()
)
upsEnvSecurity6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvSecurity6.setStatus("mandatory")


class _UpsEnvSecurity7_Type(Integer32):
    """Custom type upsEnvSecurity7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 2),
          ("normal", 1))
    )


_UpsEnvSecurity7_Type.__name__ = "Integer32"
_UpsEnvSecurity7_Object = MibScalar
upsEnvSecurity7 = _UpsEnvSecurity7_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 1, 11),
    _UpsEnvSecurity7_Type()
)
upsEnvSecurity7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvSecurity7.setStatus("mandatory")
_UpsEnvSetting_ObjectIdentity = ObjectIdentity
upsEnvSetting = _UpsEnvSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 2)
)
_UpsEnvOverTemperature_Type = Integer32
_UpsEnvOverTemperature_Object = MibScalar
upsEnvOverTemperature = _UpsEnvOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 2, 1),
    _UpsEnvOverTemperature_Type()
)
upsEnvOverTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvOverTemperature.setStatus("mandatory")
_UpsEnvUnderTemperature_Type = Integer32
_UpsEnvUnderTemperature_Object = MibScalar
upsEnvUnderTemperature = _UpsEnvUnderTemperature_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 2, 2),
    _UpsEnvUnderTemperature_Type()
)
upsEnvUnderTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvUnderTemperature.setStatus("mandatory")
_UpsEnvOverHumidity_Type = Integer32
_UpsEnvOverHumidity_Object = MibScalar
upsEnvOverHumidity = _UpsEnvOverHumidity_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 2, 3),
    _UpsEnvOverHumidity_Type()
)
upsEnvOverHumidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvOverHumidity.setStatus("mandatory")
_UpsEnvUnderHumidity_Type = Integer32
_UpsEnvUnderHumidity_Object = MibScalar
upsEnvUnderHumidity = _UpsEnvUnderHumidity_Object(
    (1, 3, 6, 1, 4, 1, 935, 1, 1, 1, 9, 2, 4),
    _UpsEnvUnderHumidity_Type()
)
upsEnvUnderHumidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvUnderHumidity.setStatus("mandatory")
_Ppcmgmt_ObjectIdentity = ObjectIdentity
ppcmgmt = _Ppcmgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 2)
)
_Mconfig_ObjectIdentity = ObjectIdentity
mconfig = _Mconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 935, 2, 1)
)
_MconfigTrapsReceiversNum_Type = Integer32
_MconfigTrapsReceiversNum_Object = MibScalar
mconfigTrapsReceiversNum = _MconfigTrapsReceiversNum_Object(
    (1, 3, 6, 1, 4, 1, 935, 2, 1, 1),
    _MconfigTrapsReceiversNum_Type()
)
mconfigTrapsReceiversNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mconfigTrapsReceiversNum.setStatus("mandatory")
_MconfigTrapsReceiversTable_Object = MibTable
mconfigTrapsReceiversTable = _MconfigTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 935, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mconfigTrapsReceiversTable.setStatus("mandatory")
_MconfigTrapsReceiversEntry_Object = MibTableRow
mconfigTrapsReceiversEntry = _MconfigTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 935, 2, 1, 2, 1)
)
mconfigTrapsReceiversEntry.setIndexNames(
    (0, "XPPC-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    mconfigTrapsReceiversEntry.setStatus("mandatory")
_TrapsIndex_Type = Integer32
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 935, 2, 1, 2, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("mandatory")
_TrapsReceiverAddr_Type = IpAddress
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 935, 2, 1, 2, 1, 2),
    _TrapsReceiverAddr_Type()
)
trapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsReceiverAddr.setStatus("mandatory")
_ReceiverCommunityString_Type = DisplayString
_ReceiverCommunityString_Object = MibTableColumn
receiverCommunityString = _ReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 935, 2, 1, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 935, 2, 1, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 935, 2, 1, 2, 1, 5),
    _ReceiverAccept_Type()
)
receiverAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverAccept.setStatus("mandatory")

# Managed Objects groups


# Notification objects

communicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 1)
)
if mibBuilder.loadTexts:
    communicationLost.setStatus(
        ""
    )

upsOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 2)
)
if mibBuilder.loadTexts:
    upsOverLoad.setStatus(
        ""
    )

upsDiagnosticsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 3)
)
if mibBuilder.loadTexts:
    upsDiagnosticsFailed.setStatus(
        ""
    )

upsDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 4)
)
if mibBuilder.loadTexts:
    upsDischarged.setStatus(
        ""
    )

upsOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 5)
)
if mibBuilder.loadTexts:
    upsOnBattery.setStatus(
        ""
    )

boostOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 6)
)
if mibBuilder.loadTexts:
    boostOn.setStatus(
        ""
    )

lowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 7)
)
if mibBuilder.loadTexts:
    lowBattery.setStatus(
        ""
    )

communicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 8)
)
if mibBuilder.loadTexts:
    communicationEstablished.setStatus(
        ""
    )

powerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 9)
)
if mibBuilder.loadTexts:
    powerRestored.setStatus(
        ""
    )

upsDiagnosticsPassed = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 10)
)
if mibBuilder.loadTexts:
    upsDiagnosticsPassed.setStatus(
        ""
    )

returnFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 11)
)
if mibBuilder.loadTexts:
    returnFromLowBattery.setStatus(
        ""
    )

upsTurnedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 12)
)
if mibBuilder.loadTexts:
    upsTurnedOff.setStatus(
        ""
    )

upsSleeping = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 13)
)
if mibBuilder.loadTexts:
    upsSleeping.setStatus(
        ""
    )

upsWokeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 14)
)
if mibBuilder.loadTexts:
    upsWokeUp.setStatus(
        ""
    )

upsRebootStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 15)
)
if mibBuilder.loadTexts:
    upsRebootStarted.setStatus(
        ""
    )

envOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 16)
)
if mibBuilder.loadTexts:
    envOverTemperature.setStatus(
        ""
    )

envTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 17)
)
if mibBuilder.loadTexts:
    envTemperatureNormal.setStatus(
        ""
    )

envOverHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 18)
)
if mibBuilder.loadTexts:
    envOverHumidity.setStatus(
        ""
    )

envHumidityNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 19)
)
if mibBuilder.loadTexts:
    envHumidityNormal.setStatus(
        ""
    )

envSmokeAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 20)
)
if mibBuilder.loadTexts:
    envSmokeAbnormal.setStatus(
        ""
    )

envWaterAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 21)
)
if mibBuilder.loadTexts:
    envWaterAbnormal.setStatus(
        ""
    )

envSecurityAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 22)
)
if mibBuilder.loadTexts:
    envSecurityAbnormal.setStatus(
        ""
    )

envWaterNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 24)
)
if mibBuilder.loadTexts:
    envWaterNormal.setStatus(
        ""
    )

envGasAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 26)
)
if mibBuilder.loadTexts:
    envGasAbnormal.setStatus(
        ""
    )

upsTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 27)
)
if mibBuilder.loadTexts:
    upsTemp.setStatus(
        ""
    )

upsLoadNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 28)
)
if mibBuilder.loadTexts:
    upsLoadNormal.setStatus(
        ""
    )

upsTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 29)
)
if mibBuilder.loadTexts:
    upsTempNormal.setStatus(
        ""
    )

envUnderTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 30)
)
if mibBuilder.loadTexts:
    envUnderTemperature.setStatus(
        ""
    )

envUnderHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 31)
)
if mibBuilder.loadTexts:
    envUnderHumidity.setStatus(
        ""
    )

upsBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 32)
)
if mibBuilder.loadTexts:
    upsBypass.setStatus(
        ""
    )

envSecurity1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 33)
)
if mibBuilder.loadTexts:
    envSecurity1.setStatus(
        ""
    )

envSecurity2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 34)
)
if mibBuilder.loadTexts:
    envSecurity2.setStatus(
        ""
    )

envSecurity3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 35)
)
if mibBuilder.loadTexts:
    envSecurity3.setStatus(
        ""
    )

envSecurity4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 36)
)
if mibBuilder.loadTexts:
    envSecurity4.setStatus(
        ""
    )

envSecurity5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 37)
)
if mibBuilder.loadTexts:
    envSecurity5.setStatus(
        ""
    )

envSecurity6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 38)
)
if mibBuilder.loadTexts:
    envSecurity6.setStatus(
        ""
    )

envSecurity7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 39)
)
if mibBuilder.loadTexts:
    envSecurity7.setStatus(
        ""
    )

upsRecroterror = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 47)
)
if mibBuilder.loadTexts:
    upsRecroterror.setStatus(
        ""
    )

upsBypassFreFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 48)
)
if mibBuilder.loadTexts:
    upsBypassFreFail.setStatus(
        ""
    )

upsBypassacnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 49)
)
if mibBuilder.loadTexts:
    upsBypassacnormal.setStatus(
        ""
    )

upsBypassacabnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 50)
)
if mibBuilder.loadTexts:
    upsBypassacabnormal.setStatus(
        ""
    )

upsTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 51)
)
if mibBuilder.loadTexts:
    upsTest.setStatus(
        ""
    )

upsScheduleShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 52)
)
if mibBuilder.loadTexts:
    upsScheduleShutdown.setStatus(
        ""
    )

upsBypassReturn = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 53)
)
if mibBuilder.loadTexts:
    upsBypassReturn.setStatus(
        ""
    )

upsShortCircuitShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 54)
)
if mibBuilder.loadTexts:
    upsShortCircuitShutdown.setStatus(
        ""
    )

upsInverterOutputFailShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 55)
)
if mibBuilder.loadTexts:
    upsInverterOutputFailShutdown.setStatus(
        ""
    )

upsBypassBreadkerOnShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 56)
)
if mibBuilder.loadTexts:
    upsBypassBreadkerOnShutdown.setStatus(
        ""
    )

upsHighDCShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 57)
)
if mibBuilder.loadTexts:
    upsHighDCShutdown.setStatus(
        ""
    )

upsEmergencyStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 58)
)
if mibBuilder.loadTexts:
    upsEmergencyStop.setStatus(
        ""
    )

upsInverterMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 59)
)
if mibBuilder.loadTexts:
    upsInverterMode.setStatus(
        ""
    )

upsBypassMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 60)
)
if mibBuilder.loadTexts:
    upsBypassMode.setStatus(
        ""
    )

upsOverTemperatureShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 61)
)
if mibBuilder.loadTexts:
    upsOverTemperatureShutdown.setStatus(
        ""
    )

upsOverLoadShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 62)
)
if mibBuilder.loadTexts:
    upsOverLoadShutdown.setStatus(
        ""
    )

upsCapacityUnderrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 63)
)
if mibBuilder.loadTexts:
    upsCapacityUnderrun.setStatus(
        ""
    )

upsCapacityNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 64)
)
if mibBuilder.loadTexts:
    upsCapacityNormal.setStatus(
        ""
    )

upsLowBatteryShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 67)
)
if mibBuilder.loadTexts:
    upsLowBatteryShutdown.setStatus(
        ""
    )

buckOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 68)
)
if mibBuilder.loadTexts:
    buckOn.setStatus(
        ""
    )

returnFromBuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 69)
)
if mibBuilder.loadTexts:
    returnFromBuck.setStatus(
        ""
    )

returnFromBoost = NotificationType(
    (1, 3, 6, 1, 4, 1, 935, 0, 70)
)
if mibBuilder.loadTexts:
    returnFromBoost.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XPPC-MIB",
    **{"ppc": ppc,
       "communicationLost": communicationLost,
       "upsOverLoad": upsOverLoad,
       "upsDiagnosticsFailed": upsDiagnosticsFailed,
       "upsDischarged": upsDischarged,
       "upsOnBattery": upsOnBattery,
       "boostOn": boostOn,
       "lowBattery": lowBattery,
       "communicationEstablished": communicationEstablished,
       "powerRestored": powerRestored,
       "upsDiagnosticsPassed": upsDiagnosticsPassed,
       "returnFromLowBattery": returnFromLowBattery,
       "upsTurnedOff": upsTurnedOff,
       "upsSleeping": upsSleeping,
       "upsWokeUp": upsWokeUp,
       "upsRebootStarted": upsRebootStarted,
       "envOverTemperature": envOverTemperature,
       "envTemperatureNormal": envTemperatureNormal,
       "envOverHumidity": envOverHumidity,
       "envHumidityNormal": envHumidityNormal,
       "envSmokeAbnormal": envSmokeAbnormal,
       "envWaterAbnormal": envWaterAbnormal,
       "envSecurityAbnormal": envSecurityAbnormal,
       "envWaterNormal": envWaterNormal,
       "envGasAbnormal": envGasAbnormal,
       "upsTemp": upsTemp,
       "upsLoadNormal": upsLoadNormal,
       "upsTempNormal": upsTempNormal,
       "envUnderTemperature": envUnderTemperature,
       "envUnderHumidity": envUnderHumidity,
       "upsBypass": upsBypass,
       "envSecurity1": envSecurity1,
       "envSecurity2": envSecurity2,
       "envSecurity3": envSecurity3,
       "envSecurity4": envSecurity4,
       "envSecurity5": envSecurity5,
       "envSecurity6": envSecurity6,
       "envSecurity7": envSecurity7,
       "upsRecroterror": upsRecroterror,
       "upsBypassFreFail": upsBypassFreFail,
       "upsBypassacnormal": upsBypassacnormal,
       "upsBypassacabnormal": upsBypassacabnormal,
       "upsTest": upsTest,
       "upsScheduleShutdown": upsScheduleShutdown,
       "upsBypassReturn": upsBypassReturn,
       "upsShortCircuitShutdown": upsShortCircuitShutdown,
       "upsInverterOutputFailShutdown": upsInverterOutputFailShutdown,
       "upsBypassBreadkerOnShutdown": upsBypassBreadkerOnShutdown,
       "upsHighDCShutdown": upsHighDCShutdown,
       "upsEmergencyStop": upsEmergencyStop,
       "upsInverterMode": upsInverterMode,
       "upsBypassMode": upsBypassMode,
       "upsOverTemperatureShutdown": upsOverTemperatureShutdown,
       "upsOverLoadShutdown": upsOverLoadShutdown,
       "upsCapacityUnderrun": upsCapacityUnderrun,
       "upsCapacityNormal": upsCapacityNormal,
       "upsLowBatteryShutdown": upsLowBatteryShutdown,
       "buckOn": buckOn,
       "returnFromBuck": returnFromBuck,
       "returnFromBoost": returnFromBoost,
       "products": products,
       "hardware": hardware,
       "ups": ups,
       "upsIdentp": upsIdentp,
       "upsBaseIdent": upsBaseIdent,
       "upsBaseIdentModel": upsBaseIdentModel,
       "upsBaseIdentUpsName": upsBaseIdentUpsName,
       "upsSmartIdent": upsSmartIdent,
       "upsSmartIdentFirmwareRevision": upsSmartIdentFirmwareRevision,
       "upsSmartIdentDateOfManufacture": upsSmartIdentDateOfManufacture,
       "upsSmartIdentUpsSerialNumber": upsSmartIdentUpsSerialNumber,
       "upsSmartIdentAgentFirmwareRevision": upsSmartIdentAgentFirmwareRevision,
       "upsBatteryp": upsBatteryp,
       "upsBaseBattery": upsBaseBattery,
       "upsBaseBatteryStatus": upsBaseBatteryStatus,
       "upsBaseBatteryTimeOnBattery": upsBaseBatteryTimeOnBattery,
       "upsBaseBatteryLastReplaceDate": upsBaseBatteryLastReplaceDate,
       "upsSmartBattery": upsSmartBattery,
       "upsSmartBatteryCapacity": upsSmartBatteryCapacity,
       "upsSmartBatteryVoltage": upsSmartBatteryVoltage,
       "upsSmartBatteryTemperature": upsSmartBatteryTemperature,
       "upsSmartBatteryRunTimeRemaining": upsSmartBatteryRunTimeRemaining,
       "upsSmartBatteryReplaceIndicator": upsSmartBatteryReplaceIndicator,
       "upsSmartBatteryFullChargeVoltage": upsSmartBatteryFullChargeVoltage,
       "upsSmartBatteryCurrent": upsSmartBatteryCurrent,
       "upsInputp": upsInputp,
       "upsBaseInput": upsBaseInput,
       "upsBaseInputPhase": upsBaseInputPhase,
       "upsSmartInput": upsSmartInput,
       "upsSmartInputLineVoltage": upsSmartInputLineVoltage,
       "upsSmartInputMaxLineVoltage": upsSmartInputMaxLineVoltage,
       "upsSmartInputMinLineVoltage": upsSmartInputMinLineVoltage,
       "upsSmartInputFrequency": upsSmartInputFrequency,
       "upsSmartInputLineFailCause": upsSmartInputLineFailCause,
       "upsOutputp": upsOutputp,
       "upsBaseOutput": upsBaseOutput,
       "upsBaseOutputStatus": upsBaseOutputStatus,
       "upsBaseOutputPhase": upsBaseOutputPhase,
       "upsSmartOutput": upsSmartOutput,
       "upsSmartOutputVoltage": upsSmartOutputVoltage,
       "upsSmartOutputFrequency": upsSmartOutputFrequency,
       "upsSmartOutputLoad": upsSmartOutputLoad,
       "upsConfigp": upsConfigp,
       "upsBaseConfig": upsBaseConfig,
       "upsBaseConfigNumDevices": upsBaseConfigNumDevices,
       "upsBaseConfigDeviceTable": upsBaseConfigDeviceTable,
       "upsBaseConfigDeviceEntry": upsBaseConfigDeviceEntry,
       "indexOfDevice": indexOfDevice,
       "nameOfDevice": nameOfDevice,
       "vaRatingOfDevice": vaRatingOfDevice,
       "deviceAccept": deviceAccept,
       "upsSmartConfig": upsSmartConfig,
       "upsSmartConfigRatedOutputVoltage": upsSmartConfigRatedOutputVoltage,
       "upsSmartConfigHighTransferVolt": upsSmartConfigHighTransferVolt,
       "upsSmartConfigLowTransferVolt": upsSmartConfigLowTransferVolt,
       "upsSmartConfigAlarm": upsSmartConfigAlarm,
       "upsSmartConfigAlarmTimer": upsSmartConfigAlarmTimer,
       "upsSmartConfigMinReturnCapacity": upsSmartConfigMinReturnCapacity,
       "upsSmartConfigSensitivity": upsSmartConfigSensitivity,
       "upsSmartConfigLowBatteryRunTime": upsSmartConfigLowBatteryRunTime,
       "upsSmartConfigReturnDelay": upsSmartConfigReturnDelay,
       "upsSmartConfigShutoffDelay": upsSmartConfigShutoffDelay,
       "upsSmartConfigUpsSleepTime": upsSmartConfigUpsSleepTime,
       "upsSmartConfigSetEEPROMDefaults": upsSmartConfigSetEEPROMDefaults,
       "upsControlp": upsControlp,
       "upsBaseControl": upsBaseControl,
       "upsBaseControlConserveBattery": upsBaseControlConserveBattery,
       "upsSmartControl": upsSmartControl,
       "upsSmartControlUpsOff": upsSmartControlUpsOff,
       "upsSmartControlRebootUps": upsSmartControlRebootUps,
       "upsSmartControlUpsSleep": upsSmartControlUpsSleep,
       "upsSmartControlSimulatePowerFail": upsSmartControlSimulatePowerFail,
       "upsSmartControlFlashAndBeep": upsSmartControlFlashAndBeep,
       "upsSmartControlTurnOnUpsLoad": upsSmartControlTurnOnUpsLoad,
       "upsTestp": upsTestp,
       "upsBaseTest": upsBaseTest,
       "upsSmartTest": upsSmartTest,
       "upsSmartTestDiagnosticSchedule": upsSmartTestDiagnosticSchedule,
       "upsSmartTestDiagnostics": upsSmartTestDiagnostics,
       "upsSmartTestDiagnosticsResults": upsSmartTestDiagnosticsResults,
       "upsSmartTestLastDiagnosticsDate": upsSmartTestLastDiagnosticsDate,
       "upsSmartTestIndicators": upsSmartTestIndicators,
       "upsSmartTestRuntimeCalibration": upsSmartTestRuntimeCalibration,
       "upsSmartTestCalibrationResults": upsSmartTestCalibrationResults,
       "upsSmartTestCalibrationDate": upsSmartTestCalibrationDate,
       "upsThreePhase": upsThreePhase,
       "upsThreePhaseBatteryGrp": upsThreePhaseBatteryGrp,
       "upsThreePhaseBatteryVoltage": upsThreePhaseBatteryVoltage,
       "upsThreePhaseBatteryCapacityPercentage": upsThreePhaseBatteryCapacityPercentage,
       "upsThreePhaseBatteryTimeRemain": upsThreePhaseBatteryTimeRemain,
       "upsThreePhaseBatteryCurrent": upsThreePhaseBatteryCurrent,
       "upsThreePhaseBatteryTemperature": upsThreePhaseBatteryTemperature,
       "upsThreePhaseInputGrp": upsThreePhaseInputGrp,
       "upsThreePhaseInputFrequency": upsThreePhaseInputFrequency,
       "upsThreePhaseInputVoltageR": upsThreePhaseInputVoltageR,
       "upsThreePhaseInputVoltageS": upsThreePhaseInputVoltageS,
       "upsThreePhaseInputVoltageT": upsThreePhaseInputVoltageT,
       "upsThreePhaseOutputGrp": upsThreePhaseOutputGrp,
       "upsThreePhaseOutputFrequency": upsThreePhaseOutputFrequency,
       "upsThreePhaseOutputVoltageR": upsThreePhaseOutputVoltageR,
       "upsThreePhaseOutputVoltageS": upsThreePhaseOutputVoltageS,
       "upsThreePhaseOutputVoltageT": upsThreePhaseOutputVoltageT,
       "upsThreePhaseOutputLoadPercentageR": upsThreePhaseOutputLoadPercentageR,
       "upsThreePhaseOutputLoadPercentageS": upsThreePhaseOutputLoadPercentageS,
       "upsThreePhaseOutputLoadPercentageT": upsThreePhaseOutputLoadPercentageT,
       "upsThreePhaseBypassGrp": upsThreePhaseBypassGrp,
       "upsThreePhaseBypassSourceFrequency": upsThreePhaseBypassSourceFrequency,
       "upsThreePhaseBypssSourceVoltageR": upsThreePhaseBypssSourceVoltageR,
       "upsThreePhaseBypssSourceVoltageS": upsThreePhaseBypssSourceVoltageS,
       "upsThreePhaseBypssSourceVoltageT": upsThreePhaseBypssSourceVoltageT,
       "upsThreePhaseDCandRectifierStatusGrp": upsThreePhaseDCandRectifierStatusGrp,
       "upsThreePhaseDCandRectifierStatusRecRotError": upsThreePhaseDCandRectifierStatusRecRotError,
       "upsThreePhaseDCandRectifierStatusLowBatteryShutdown": upsThreePhaseDCandRectifierStatusLowBatteryShutdown,
       "upsThreePhaseDCandRectifierStatusLowBattery": upsThreePhaseDCandRectifierStatusLowBattery,
       "upsThreePhaseDCandRectifierStatusInAndOut": upsThreePhaseDCandRectifierStatusInAndOut,
       "upsThreePhaseDCandRectifierStatusBatteryStatus": upsThreePhaseDCandRectifierStatusBatteryStatus,
       "upsThreePhaseDCandRectifierStatusChargeStatus": upsThreePhaseDCandRectifierStatusChargeStatus,
       "upsThreePhaseDCandRectifierStatusRecOperating": upsThreePhaseDCandRectifierStatusRecOperating,
       "upsThreePhaseUPSStatusGrp": upsThreePhaseUPSStatusGrp,
       "upsThreePhaseUPSStatusBypassFreqFail": upsThreePhaseUPSStatusBypassFreqFail,
       "upsThreePhaseUPSStatusManualBypassBreaker": upsThreePhaseUPSStatusManualBypassBreaker,
       "upsThreePhaseUPSStatusACStatus": upsThreePhaseUPSStatusACStatus,
       "upsThreePhaseUPSStaticSwitchMode": upsThreePhaseUPSStaticSwitchMode,
       "upsThreePhaseUPSStatusInverterOperating": upsThreePhaseUPSStatusInverterOperating,
       "upsThreePhaseFaultStatusGrp": upsThreePhaseFaultStatusGrp,
       "upsThreePhaseFaultStatusEmergencyStop": upsThreePhaseFaultStatusEmergencyStop,
       "upsThreePhaseFaultStatusHighDCShutdown": upsThreePhaseFaultStatusHighDCShutdown,
       "upsThreePhaseFaultStatusBypassBreaker": upsThreePhaseFaultStatusBypassBreaker,
       "upsThreePhaseFaultStatusOverLoad": upsThreePhaseFaultStatusOverLoad,
       "upsThreePhaseFaultStatusInverterOutputFail": upsThreePhaseFaultStatusInverterOutputFail,
       "upsThreePhaseFaultStatusOverTemperature": upsThreePhaseFaultStatusOverTemperature,
       "upsThreePhaseFaultStatusShortCircuit": upsThreePhaseFaultStatusShortCircuit,
       "upsThreePhaseRatingGrp": upsThreePhaseRatingGrp,
       "upsThreePhaseRatingRectifierVoltage": upsThreePhaseRatingRectifierVoltage,
       "upsThreePhaseRatingRectifierFrequency": upsThreePhaseRatingRectifierFrequency,
       "upsThreePhaseRatingBypassVoltage": upsThreePhaseRatingBypassVoltage,
       "upsThreePhaseRatingBypassFrequency": upsThreePhaseRatingBypassFrequency,
       "upsThreePhaseRatingOutputVoltage": upsThreePhaseRatingOutputVoltage,
       "upsThreePhaseRatingOutputFrequency": upsThreePhaseRatingOutputFrequency,
       "upsThreePhaseRatingBatteryVoltage": upsThreePhaseRatingBatteryVoltage,
       "upsThreePhaseRatingPower": upsThreePhaseRatingPower,
       "upsEnvironment": upsEnvironment,
       "upsEnvStatus": upsEnvStatus,
       "upsEnvTemperature": upsEnvTemperature,
       "upsEnvHumidity": upsEnvHumidity,
       "upsEnvWater": upsEnvWater,
       "upsEnvSmoke": upsEnvSmoke,
       "upsEnvSecurity1": upsEnvSecurity1,
       "upsEnvSecurity2": upsEnvSecurity2,
       "upsEnvSecurity3": upsEnvSecurity3,
       "upsEnvSecurity4": upsEnvSecurity4,
       "upsEnvSecurity5": upsEnvSecurity5,
       "upsEnvSecurity6": upsEnvSecurity6,
       "upsEnvSecurity7": upsEnvSecurity7,
       "upsEnvSetting": upsEnvSetting,
       "upsEnvOverTemperature": upsEnvOverTemperature,
       "upsEnvUnderTemperature": upsEnvUnderTemperature,
       "upsEnvOverHumidity": upsEnvOverHumidity,
       "upsEnvUnderHumidity": upsEnvUnderHumidity,
       "ppcmgmt": ppcmgmt,
       "mconfig": mconfig,
       "mconfigTrapsReceiversNum": mconfigTrapsReceiversNum,
       "mconfigTrapsReceiversTable": mconfigTrapsReceiversTable,
       "mconfigTrapsReceiversEntry": mconfigTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverCommunityString": receiverCommunityString,
       "severityLevel": severityLevel,
       "receiverAccept": receiverAccept}
)
