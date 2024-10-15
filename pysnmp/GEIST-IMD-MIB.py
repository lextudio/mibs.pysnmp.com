# SNMP MIB module (GEIST-IMD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GEIST-IMD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:25 2024
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

geist = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21239)
)
geist.setRevisions(
        ("2012-09-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Blackbird_ObjectIdentity = ObjectIdentity
blackbird = _Blackbird_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5)
)
_Imd_ObjectIdentity = ObjectIdentity
imd = _Imd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1)
)
_ProductTitle_Type = DisplayString
_ProductTitle_Object = MibScalar
productTitle = _ProductTitle_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 1),
    _ProductTitle_Type()
)
productTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productTitle.setStatus("current")
_ProductVersion_Type = DisplayString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_ProductFriendlyName_Type = DisplayString
_ProductFriendlyName_Object = MibScalar
productFriendlyName = _ProductFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 3),
    _ProductFriendlyName_Type()
)
productFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFriendlyName.setStatus("current")
_ProductMacAddress_Type = OctetString
_ProductMacAddress_Object = MibScalar
productMacAddress = _ProductMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 4),
    _ProductMacAddress_Type()
)
productMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMacAddress.setStatus("current")
_ProductUrl_Type = IpAddress
_ProductUrl_Object = MibScalar
productUrl = _ProductUrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 5),
    _ProductUrl_Type()
)
productUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productUrl.setStatus("current")


class _DeviceCount_Type(Integer32):
    """Custom type deviceCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DeviceCount_Type.__name__ = "Integer32"
_DeviceCount_Object = MibScalar
deviceCount = _DeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 6),
    _DeviceCount_Type()
)
deviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCount.setStatus("current")


class _TemperatureUnits_Type(Integer32):
    """Custom type temperatureUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TemperatureUnits_Type.__name__ = "Integer32"
_TemperatureUnits_Object = MibScalar
temperatureUnits = _TemperatureUnits_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 1, 7),
    _TemperatureUnits_Type()
)
temperatureUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureUnits.setStatus("current")
_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3)
)
_PduMainTable_Object = MibTable
pduMainTable = _PduMainTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pduMainTable.setStatus("current")
_PduMainEntry_Object = MibTableRow
pduMainEntry = _PduMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1)
)
pduMainEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "pduMainIndex"),
)
if mibBuilder.loadTexts:
    pduMainEntry.setStatus("current")


class _PduMainIndex_Type(Integer32):
    """Custom type pduMainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PduMainIndex_Type.__name__ = "Integer32"
_PduMainIndex_Object = MibTableColumn
pduMainIndex = _PduMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 1),
    _PduMainIndex_Type()
)
pduMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMainIndex.setStatus("current")
_PduMainSerial_Type = DisplayString
_PduMainSerial_Object = MibTableColumn
pduMainSerial = _PduMainSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 2),
    _PduMainSerial_Type()
)
pduMainSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMainSerial.setStatus("current")
_PduMainName_Type = DisplayString
_PduMainName_Object = MibTableColumn
pduMainName = _PduMainName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 3),
    _PduMainName_Type()
)
pduMainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMainName.setStatus("current")
_PduMainLabel_Type = DisplayString
_PduMainLabel_Object = MibTableColumn
pduMainLabel = _PduMainLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 4),
    _PduMainLabel_Type()
)
pduMainLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMainLabel.setStatus("current")
_PduMainAvail_Type = Gauge32
_PduMainAvail_Object = MibTableColumn
pduMainAvail = _PduMainAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 5),
    _PduMainAvail_Type()
)
pduMainAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMainAvail.setStatus("current")


class _PduMeterType_Type(Integer32):
    """Custom type pduMeterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PduMeterType_Type.__name__ = "Integer32"
_PduMeterType_Object = MibTableColumn
pduMeterType = _PduMeterType_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 6),
    _PduMeterType_Type()
)
pduMeterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduMeterType.setStatus("current")
_PduTotalName_Type = DisplayString
_PduTotalName_Object = MibTableColumn
pduTotalName = _PduTotalName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 7),
    _PduTotalName_Type()
)
pduTotalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalName.setStatus("current")
_PduTotalLabel_Type = DisplayString
_PduTotalLabel_Object = MibTableColumn
pduTotalLabel = _PduTotalLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 8),
    _PduTotalLabel_Type()
)
pduTotalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalLabel.setStatus("current")
_PduTotalRealPower_Type = Gauge32
_PduTotalRealPower_Object = MibTableColumn
pduTotalRealPower = _PduTotalRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 9),
    _PduTotalRealPower_Type()
)
pduTotalRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalRealPower.setStatus("current")
if mibBuilder.loadTexts:
    pduTotalRealPower.setUnits("watts")
_PduTotalApparentPower_Type = Gauge32
_PduTotalApparentPower_Object = MibTableColumn
pduTotalApparentPower = _PduTotalApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 10),
    _PduTotalApparentPower_Type()
)
pduTotalApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    pduTotalApparentPower.setUnits("volt-amps")
_PduTotalPowerFactor_Type = Gauge32
_PduTotalPowerFactor_Object = MibTableColumn
pduTotalPowerFactor = _PduTotalPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 11),
    _PduTotalPowerFactor_Type()
)
pduTotalPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pduTotalPowerFactor.setUnits("%")
_PduTotalEnergy_Type = Gauge32
_PduTotalEnergy_Object = MibTableColumn
pduTotalEnergy = _PduTotalEnergy_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 1, 1, 12),
    _PduTotalEnergy_Type()
)
pduTotalEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduTotalEnergy.setStatus("current")
if mibBuilder.loadTexts:
    pduTotalEnergy.setUnits("watt-hours")
_PduPhaseTable_Object = MibTable
pduPhaseTable = _PduPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2)
)
if mibBuilder.loadTexts:
    pduPhaseTable.setStatus("current")
_PduPhaseEntry_Object = MibTableRow
pduPhaseEntry = _PduPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1)
)
pduPhaseEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "pduPhaseIndex"),
)
if mibBuilder.loadTexts:
    pduPhaseEntry.setStatus("current")


class _PduPhaseIndex_Type(Integer32):
    """Custom type pduPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PduPhaseIndex_Type.__name__ = "Integer32"
_PduPhaseIndex_Object = MibTableColumn
pduPhaseIndex = _PduPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 1),
    _PduPhaseIndex_Type()
)
pduPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseIndex.setStatus("current")
_PduPhaseName_Type = DisplayString
_PduPhaseName_Object = MibTableColumn
pduPhaseName = _PduPhaseName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 2),
    _PduPhaseName_Type()
)
pduPhaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseName.setStatus("current")
_PduPhaseLabel_Type = DisplayString
_PduPhaseLabel_Object = MibTableColumn
pduPhaseLabel = _PduPhaseLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 3),
    _PduPhaseLabel_Type()
)
pduPhaseLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseLabel.setStatus("current")
_PduPhaseVoltage_Type = Gauge32
_PduPhaseVoltage_Object = MibTableColumn
pduPhaseVoltage = _PduPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 4),
    _PduPhaseVoltage_Type()
)
pduPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseVoltage.setUnits("decivolts (rms)")
_PduPhaseVoltageMax_Type = Gauge32
_PduPhaseVoltageMax_Object = MibTableColumn
pduPhaseVoltageMax = _PduPhaseVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 5),
    _PduPhaseVoltageMax_Type()
)
pduPhaseVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseVoltageMax.setUnits("decivolts (rms)")
_PduPhaseVoltageMin_Type = Gauge32
_PduPhaseVoltageMin_Object = MibTableColumn
pduPhaseVoltageMin = _PduPhaseVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 6),
    _PduPhaseVoltageMin_Type()
)
pduPhaseVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseVoltageMin.setUnits("decivolts (rms)")
_PduPhaseVoltagePeak_Type = Gauge32
_PduPhaseVoltagePeak_Object = MibTableColumn
pduPhaseVoltagePeak = _PduPhaseVoltagePeak_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 7),
    _PduPhaseVoltagePeak_Type()
)
pduPhaseVoltagePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseVoltagePeak.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseVoltagePeak.setUnits("decivolts")
_PduPhaseCurrent_Type = Gauge32
_PduPhaseCurrent_Object = MibTableColumn
pduPhaseCurrent = _PduPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 8),
    _PduPhaseCurrent_Type()
)
pduPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseCurrent.setUnits("centiamps (rms)")
_PduPhaseCurrentMax_Type = Gauge32
_PduPhaseCurrentMax_Object = MibTableColumn
pduPhaseCurrentMax = _PduPhaseCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 9),
    _PduPhaseCurrentMax_Type()
)
pduPhaseCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseCurrentMax.setUnits("centiamps (rms)")
_PduPhaseCurrentMin_Type = Gauge32
_PduPhaseCurrentMin_Object = MibTableColumn
pduPhaseCurrentMin = _PduPhaseCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 10),
    _PduPhaseCurrentMin_Type()
)
pduPhaseCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseCurrentMin.setUnits("centiamps (rms)")
_PduPhaseCurrentPeak_Type = Gauge32
_PduPhaseCurrentPeak_Object = MibTableColumn
pduPhaseCurrentPeak = _PduPhaseCurrentPeak_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 11),
    _PduPhaseCurrentPeak_Type()
)
pduPhaseCurrentPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseCurrentPeak.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseCurrentPeak.setUnits("centiamps (rms)")
_PduPhaseRealPower_Type = Gauge32
_PduPhaseRealPower_Object = MibTableColumn
pduPhaseRealPower = _PduPhaseRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 12),
    _PduPhaseRealPower_Type()
)
pduPhaseRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseRealPower.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseRealPower.setUnits("watts")
_PduPhaseApparentPower_Type = Gauge32
_PduPhaseApparentPower_Object = MibTableColumn
pduPhaseApparentPower = _PduPhaseApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 13),
    _PduPhaseApparentPower_Type()
)
pduPhaseApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseApparentPower.setUnits("volt-amps")
_PduPhasePowerFactor_Type = Gauge32
_PduPhasePowerFactor_Object = MibTableColumn
pduPhasePowerFactor = _PduPhasePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 14),
    _PduPhasePowerFactor_Type()
)
pduPhasePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhasePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pduPhasePowerFactor.setUnits("%")
_PduPhaseEnergy_Type = Gauge32
_PduPhaseEnergy_Object = MibTableColumn
pduPhaseEnergy = _PduPhaseEnergy_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 2, 1, 15),
    _PduPhaseEnergy_Type()
)
pduPhaseEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPhaseEnergy.setStatus("current")
if mibBuilder.loadTexts:
    pduPhaseEnergy.setUnits("watt-hours")
_PduBreakerTable_Object = MibTable
pduBreakerTable = _PduBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3)
)
if mibBuilder.loadTexts:
    pduBreakerTable.setStatus("current")
_PduBreakerEntry_Object = MibTableRow
pduBreakerEntry = _PduBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1)
)
pduBreakerEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "pduBreakerIndex"),
)
if mibBuilder.loadTexts:
    pduBreakerEntry.setStatus("current")


class _PduBreakerIndex_Type(Integer32):
    """Custom type pduBreakerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PduBreakerIndex_Type.__name__ = "Integer32"
_PduBreakerIndex_Object = MibTableColumn
pduBreakerIndex = _PduBreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 1),
    _PduBreakerIndex_Type()
)
pduBreakerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerIndex.setStatus("current")
_PduBreakerName_Type = DisplayString
_PduBreakerName_Object = MibTableColumn
pduBreakerName = _PduBreakerName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 2),
    _PduBreakerName_Type()
)
pduBreakerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerName.setStatus("current")
_PduBreakerLabel_Type = DisplayString
_PduBreakerLabel_Object = MibTableColumn
pduBreakerLabel = _PduBreakerLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 3),
    _PduBreakerLabel_Type()
)
pduBreakerLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerLabel.setStatus("current")
_PduBreakerCurrent_Type = Gauge32
_PduBreakerCurrent_Object = MibTableColumn
pduBreakerCurrent = _PduBreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 4),
    _PduBreakerCurrent_Type()
)
pduBreakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduBreakerCurrent.setUnits("centiamps (rms)")
_PduBreakerCurrentMax_Type = Gauge32
_PduBreakerCurrentMax_Object = MibTableColumn
pduBreakerCurrentMax = _PduBreakerCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 5),
    _PduBreakerCurrentMax_Type()
)
pduBreakerCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    pduBreakerCurrentMax.setUnits("centiamps (rms)")
_PduBreakerCurrentMin_Type = Gauge32
_PduBreakerCurrentMin_Object = MibTableColumn
pduBreakerCurrentMin = _PduBreakerCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 6),
    _PduBreakerCurrentMin_Type()
)
pduBreakerCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    pduBreakerCurrentMin.setUnits("centiamps (rms)")
_PduBreakerCurrentPeak_Type = Gauge32
_PduBreakerCurrentPeak_Object = MibTableColumn
pduBreakerCurrentPeak = _PduBreakerCurrentPeak_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 3, 1, 7),
    _PduBreakerCurrentPeak_Type()
)
pduBreakerCurrentPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBreakerCurrentPeak.setStatus("current")
if mibBuilder.loadTexts:
    pduBreakerCurrentPeak.setUnits("centiamps (rms)")
_PduLineTable_Object = MibTable
pduLineTable = _PduLineTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4)
)
if mibBuilder.loadTexts:
    pduLineTable.setStatus("current")
_PduLineEntry_Object = MibTableRow
pduLineEntry = _PduLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1)
)
pduLineEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "pduLineIndex"),
)
if mibBuilder.loadTexts:
    pduLineEntry.setStatus("current")


class _PduLineIndex_Type(Integer32):
    """Custom type pduLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PduLineIndex_Type.__name__ = "Integer32"
_PduLineIndex_Object = MibTableColumn
pduLineIndex = _PduLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1, 1),
    _PduLineIndex_Type()
)
pduLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduLineIndex.setStatus("current")
_PduLineName_Type = DisplayString
_PduLineName_Object = MibTableColumn
pduLineName = _PduLineName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1, 2),
    _PduLineName_Type()
)
pduLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduLineName.setStatus("current")
_PduLineLabel_Type = DisplayString
_PduLineLabel_Object = MibTableColumn
pduLineLabel = _PduLineLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1, 3),
    _PduLineLabel_Type()
)
pduLineLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduLineLabel.setStatus("current")
_PduLineCurrent_Type = Gauge32
_PduLineCurrent_Object = MibTableColumn
pduLineCurrent = _PduLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1, 4),
    _PduLineCurrent_Type()
)
pduLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduLineCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pduLineCurrent.setUnits("centiamps (rms)")
_PduLineCurrentMax_Type = Gauge32
_PduLineCurrentMax_Object = MibTableColumn
pduLineCurrentMax = _PduLineCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1, 5),
    _PduLineCurrentMax_Type()
)
pduLineCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduLineCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    pduLineCurrentMax.setUnits("centiamps (rms)")
_PduLineCurrentMin_Type = Gauge32
_PduLineCurrentMin_Object = MibTableColumn
pduLineCurrentMin = _PduLineCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1, 6),
    _PduLineCurrentMin_Type()
)
pduLineCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduLineCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    pduLineCurrentMin.setUnits("centiamps (rms)")
_PduLineCurrentPeak_Type = Gauge32
_PduLineCurrentPeak_Object = MibTableColumn
pduLineCurrentPeak = _PduLineCurrentPeak_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 3, 4, 1, 7),
    _PduLineCurrentPeak_Type()
)
pduLineCurrentPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduLineCurrentPeak.setStatus("current")
if mibBuilder.loadTexts:
    pduLineCurrentPeak.setUnits("centiamps (rms)")
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1)
)
tempSensorEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "tempSensorIndex"),
)
if mibBuilder.loadTexts:
    tempSensorEntry.setStatus("current")


class _TempSensorIndex_Type(Integer32):
    """Custom type tempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TempSensorIndex_Type.__name__ = "Integer32"
_TempSensorIndex_Object = MibTableColumn
tempSensorIndex = _TempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1, 1),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("current")
_TempSensorSerial_Type = DisplayString
_TempSensorSerial_Object = MibTableColumn
tempSensorSerial = _TempSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1, 2),
    _TempSensorSerial_Type()
)
tempSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorSerial.setStatus("current")
_TempSensorName_Type = DisplayString
_TempSensorName_Object = MibTableColumn
tempSensorName = _TempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1, 3),
    _TempSensorName_Type()
)
tempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorName.setStatus("current")
_TempSensorAvail_Type = Gauge32
_TempSensorAvail_Object = MibTableColumn
tempSensorAvail = _TempSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1, 4),
    _TempSensorAvail_Type()
)
tempSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorAvail.setStatus("current")


class _TempSensorTemp_Type(Integer32):
    """Custom type tempSensorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_TempSensorTemp_Type.__name__ = "Integer32"
_TempSensorTemp_Object = MibTableColumn
tempSensorTemp = _TempSensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 4, 1, 5),
    _TempSensorTemp_Type()
)
tempSensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorTemp.setStatus("current")
if mibBuilder.loadTexts:
    tempSensorTemp.setUnits("0.1 Degrees")
_AirFlowSensorTable_Object = MibTable
airFlowSensorTable = _AirFlowSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5)
)
if mibBuilder.loadTexts:
    airFlowSensorTable.setStatus("current")
_AirFlowSensorEntry_Object = MibTableRow
airFlowSensorEntry = _AirFlowSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1)
)
airFlowSensorEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "airFlowSensorIndex"),
)
if mibBuilder.loadTexts:
    airFlowSensorEntry.setStatus("current")


class _AirFlowSensorIndex_Type(Integer32):
    """Custom type airFlowSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AirFlowSensorIndex_Type.__name__ = "Integer32"
_AirFlowSensorIndex_Object = MibTableColumn
airFlowSensorIndex = _AirFlowSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 1),
    _AirFlowSensorIndex_Type()
)
airFlowSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorIndex.setStatus("current")
_AirFlowSensorSerial_Type = DisplayString
_AirFlowSensorSerial_Object = MibTableColumn
airFlowSensorSerial = _AirFlowSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 2),
    _AirFlowSensorSerial_Type()
)
airFlowSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorSerial.setStatus("current")
_AirFlowSensorName_Type = DisplayString
_AirFlowSensorName_Object = MibTableColumn
airFlowSensorName = _AirFlowSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 3),
    _AirFlowSensorName_Type()
)
airFlowSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorName.setStatus("current")
_AirFlowSensorAvail_Type = Gauge32
_AirFlowSensorAvail_Object = MibTableColumn
airFlowSensorAvail = _AirFlowSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 4),
    _AirFlowSensorAvail_Type()
)
airFlowSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorAvail.setStatus("current")


class _AirFlowSensorTemp_Type(Integer32):
    """Custom type airFlowSensorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_AirFlowSensorTemp_Type.__name__ = "Integer32"
_AirFlowSensorTemp_Object = MibTableColumn
airFlowSensorTemp = _AirFlowSensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 5),
    _AirFlowSensorTemp_Type()
)
airFlowSensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorTemp.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorTemp.setUnits("0.1 Degrees")


class _AirFlowSensorFlow_Type(Integer32):
    """Custom type airFlowSensorFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AirFlowSensorFlow_Type.__name__ = "Integer32"
_AirFlowSensorFlow_Object = MibTableColumn
airFlowSensorFlow = _AirFlowSensorFlow_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 6),
    _AirFlowSensorFlow_Type()
)
airFlowSensorFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorFlow.setStatus("current")


class _AirFlowSensorHumidity_Type(Integer32):
    """Custom type airFlowSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AirFlowSensorHumidity_Type.__name__ = "Integer32"
_AirFlowSensorHumidity_Object = MibTableColumn
airFlowSensorHumidity = _AirFlowSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 7),
    _AirFlowSensorHumidity_Type()
)
airFlowSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorHumidity.setUnits("%")


class _AirFlowSensorDewPoint_Type(Integer32):
    """Custom type airFlowSensorDewPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_AirFlowSensorDewPoint_Type.__name__ = "Integer32"
_AirFlowSensorDewPoint_Object = MibTableColumn
airFlowSensorDewPoint = _AirFlowSensorDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 5, 1, 8),
    _AirFlowSensorDewPoint_Type()
)
airFlowSensorDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorDewPoint.setUnits("0.1 Degrees")
_DewPointSensorTable_Object = MibTable
dewPointSensorTable = _DewPointSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 6)
)
if mibBuilder.loadTexts:
    dewPointSensorTable.setStatus("current")
_DewPointSensorEntry_Object = MibTableRow
dewPointSensorEntry = _DewPointSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 6, 1)
)
dewPointSensorEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "dewPointSensorIndex"),
)
if mibBuilder.loadTexts:
    dewPointSensorEntry.setStatus("current")


class _DewPointSensorIndex_Type(Integer32):
    """Custom type dewPointSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DewPointSensorIndex_Type.__name__ = "Integer32"
_DewPointSensorIndex_Object = MibTableColumn
dewPointSensorIndex = _DewPointSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 6, 1, 1),
    _DewPointSensorIndex_Type()
)
dewPointSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorIndex.setStatus("current")
_DewPointSensorSerial_Type = DisplayString
_DewPointSensorSerial_Object = MibTableColumn
dewPointSensorSerial = _DewPointSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 6, 1, 2),
    _DewPointSensorSerial_Type()
)
dewPointSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorSerial.setStatus("current")
_DewPointSensorName_Type = DisplayString
_DewPointSensorName_Object = MibTableColumn
dewPointSensorName = _DewPointSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 6, 1, 3),
    _DewPointSensorName_Type()
)
dewPointSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorName.setStatus("current")
_DewPointSensorAvail_Type = Gauge32
_DewPointSensorAvail_Object = MibTableColumn
dewPointSensorAvail = _DewPointSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 6, 1, 4),
    _DewPointSensorAvail_Type()
)
dewPointSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorAvail.setStatus("current")


class _DewPointSensorTemp_Type(Integer32):
    """Custom type dewPointSensorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_DewPointSensorTemp_Type.__name__ = "Integer32"
_DewPointSensorTemp_Object = MibTableColumn
dewPointSensorTemp = _DewPointSensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 6, 1, 5),
    _DewPointSensorTemp_Type()
)
dewPointSensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorTemp.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorTemp.setUnits("0.1 Degrees")


class _DewPointSensorHumidity_Type(Integer32):
    """Custom type dewPointSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DewPointSensorHumidity_Type.__name__ = "Integer32"
_DewPointSensorHumidity_Object = MibTableColumn
dewPointSensorHumidity = _DewPointSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 6, 1, 6),
    _DewPointSensorHumidity_Type()
)
dewPointSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorHumidity.setUnits("%")


class _DewPointSensorDewPoint_Type(Integer32):
    """Custom type dewPointSensorDewPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_DewPointSensorDewPoint_Type.__name__ = "Integer32"
_DewPointSensorDewPoint_Object = MibTableColumn
dewPointSensorDewPoint = _DewPointSensorDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 6, 1, 7),
    _DewPointSensorDewPoint_Type()
)
dewPointSensorDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorDewPoint.setUnits("0.1 Degrees")
_CcatSensorTable_Object = MibTable
ccatSensorTable = _CcatSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 7)
)
if mibBuilder.loadTexts:
    ccatSensorTable.setStatus("current")
_CcatSensorEntry_Object = MibTableRow
ccatSensorEntry = _CcatSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 7, 1)
)
ccatSensorEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "ccatSensorIndex"),
)
if mibBuilder.loadTexts:
    ccatSensorEntry.setStatus("current")


class _CcatSensorIndex_Type(Integer32):
    """Custom type ccatSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcatSensorIndex_Type.__name__ = "Integer32"
_CcatSensorIndex_Object = MibTableColumn
ccatSensorIndex = _CcatSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 7, 1, 1),
    _CcatSensorIndex_Type()
)
ccatSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorIndex.setStatus("current")
_CcatSensorSerial_Type = DisplayString
_CcatSensorSerial_Object = MibTableColumn
ccatSensorSerial = _CcatSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 7, 1, 2),
    _CcatSensorSerial_Type()
)
ccatSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorSerial.setStatus("current")
_CcatSensorName_Type = DisplayString
_CcatSensorName_Object = MibTableColumn
ccatSensorName = _CcatSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 7, 1, 3),
    _CcatSensorName_Type()
)
ccatSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorName.setStatus("current")
_CcatSensorAvail_Type = Gauge32
_CcatSensorAvail_Object = MibTableColumn
ccatSensorAvail = _CcatSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 7, 1, 4),
    _CcatSensorAvail_Type()
)
ccatSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorAvail.setStatus("current")


class _CcatSensorValue_Type(Integer32):
    """Custom type ccatSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 5000),
    )


_CcatSensorValue_Type.__name__ = "Integer32"
_CcatSensorValue_Object = MibTableColumn
ccatSensorValue = _CcatSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 7, 1, 5),
    _CcatSensorValue_Type()
)
ccatSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorValue.setStatus("current")
_CcatSensorType_Type = DisplayString
_CcatSensorType_Object = MibTableColumn
ccatSensorType = _CcatSensorType_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 7, 1, 6),
    _CcatSensorType_Type()
)
ccatSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorType.setStatus("current")
_CcatSensorDescription_Type = DisplayString
_CcatSensorDescription_Object = MibTableColumn
ccatSensorDescription = _CcatSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 7, 1, 7),
    _CcatSensorDescription_Type()
)
ccatSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccatSensorDescription.setStatus("current")
_T3hdSensorTable_Object = MibTable
t3hdSensorTable = _T3hdSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8)
)
if mibBuilder.loadTexts:
    t3hdSensorTable.setStatus("current")
_T3hdSensorEntry_Object = MibTableRow
t3hdSensorEntry = _T3hdSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1)
)
t3hdSensorEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "t3hdSensorIndex"),
)
if mibBuilder.loadTexts:
    t3hdSensorEntry.setStatus("current")


class _T3hdSensorIndex_Type(Integer32):
    """Custom type t3hdSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_T3hdSensorIndex_Type.__name__ = "Integer32"
_T3hdSensorIndex_Object = MibTableColumn
t3hdSensorIndex = _T3hdSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 1),
    _T3hdSensorIndex_Type()
)
t3hdSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIndex.setStatus("current")
_T3hdSensorSerial_Type = DisplayString
_T3hdSensorSerial_Object = MibTableColumn
t3hdSensorSerial = _T3hdSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 2),
    _T3hdSensorSerial_Type()
)
t3hdSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorSerial.setStatus("current")
_T3hdSensorName_Type = DisplayString
_T3hdSensorName_Object = MibTableColumn
t3hdSensorName = _T3hdSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 3),
    _T3hdSensorName_Type()
)
t3hdSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorName.setStatus("current")
_T3hdSensorAvail_Type = Gauge32
_T3hdSensorAvail_Object = MibTableColumn
t3hdSensorAvail = _T3hdSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 4),
    _T3hdSensorAvail_Type()
)
t3hdSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorAvail.setStatus("current")
_T3hdSensorIntName_Type = DisplayString
_T3hdSensorIntName_Object = MibTableColumn
t3hdSensorIntName = _T3hdSensorIntName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 5),
    _T3hdSensorIntName_Type()
)
t3hdSensorIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntName.setStatus("current")


class _T3hdSensorIntTemp_Type(Integer32):
    """Custom type t3hdSensorIntTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_T3hdSensorIntTemp_Type.__name__ = "Integer32"
_T3hdSensorIntTemp_Object = MibTableColumn
t3hdSensorIntTemp = _T3hdSensorIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 6),
    _T3hdSensorIntTemp_Type()
)
t3hdSensorIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntTemp.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntTemp.setUnits("0.1 Degrees")


class _T3hdSensorIntHumidity_Type(Integer32):
    """Custom type t3hdSensorIntHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_T3hdSensorIntHumidity_Type.__name__ = "Integer32"
_T3hdSensorIntHumidity_Object = MibTableColumn
t3hdSensorIntHumidity = _T3hdSensorIntHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 7),
    _T3hdSensorIntHumidity_Type()
)
t3hdSensorIntHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntHumidity.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntHumidity.setUnits("%")


class _T3hdSensorIntDewPoint_Type(Integer32):
    """Custom type t3hdSensorIntDewPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_T3hdSensorIntDewPoint_Type.__name__ = "Integer32"
_T3hdSensorIntDewPoint_Object = MibTableColumn
t3hdSensorIntDewPoint = _T3hdSensorIntDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 8),
    _T3hdSensorIntDewPoint_Type()
)
t3hdSensorIntDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntDewPoint.setUnits("0.1 Degrees")
_T3hdSensorExtAAvail_Type = Gauge32
_T3hdSensorExtAAvail_Object = MibTableColumn
t3hdSensorExtAAvail = _T3hdSensorExtAAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 9),
    _T3hdSensorExtAAvail_Type()
)
t3hdSensorExtAAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtAAvail.setStatus("current")
_T3hdSensorExtAName_Type = DisplayString
_T3hdSensorExtAName_Object = MibTableColumn
t3hdSensorExtAName = _T3hdSensorExtAName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 10),
    _T3hdSensorExtAName_Type()
)
t3hdSensorExtAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtAName.setStatus("current")


class _T3hdSensorExtATemp_Type(Integer32):
    """Custom type t3hdSensorExtATemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_T3hdSensorExtATemp_Type.__name__ = "Integer32"
_T3hdSensorExtATemp_Object = MibTableColumn
t3hdSensorExtATemp = _T3hdSensorExtATemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 11),
    _T3hdSensorExtATemp_Type()
)
t3hdSensorExtATemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtATemp.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorExtATemp.setUnits("0.1 Degrees")
_T3hdSensorExtBAvail_Type = Gauge32
_T3hdSensorExtBAvail_Object = MibTableColumn
t3hdSensorExtBAvail = _T3hdSensorExtBAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 12),
    _T3hdSensorExtBAvail_Type()
)
t3hdSensorExtBAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtBAvail.setStatus("current")
_T3hdSensorExtBName_Type = DisplayString
_T3hdSensorExtBName_Object = MibTableColumn
t3hdSensorExtBName = _T3hdSensorExtBName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 13),
    _T3hdSensorExtBName_Type()
)
t3hdSensorExtBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtBName.setStatus("current")


class _T3hdSensorExtBTemp_Type(Integer32):
    """Custom type t3hdSensorExtBTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_T3hdSensorExtBTemp_Type.__name__ = "Integer32"
_T3hdSensorExtBTemp_Object = MibTableColumn
t3hdSensorExtBTemp = _T3hdSensorExtBTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 8, 1, 14),
    _T3hdSensorExtBTemp_Type()
)
t3hdSensorExtBTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExtBTemp.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorExtBTemp.setUnits("0.1 Degrees")
_ThdSensorTable_Object = MibTable
thdSensorTable = _ThdSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9)
)
if mibBuilder.loadTexts:
    thdSensorTable.setStatus("current")
_ThdSensorEntry_Object = MibTableRow
thdSensorEntry = _ThdSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1)
)
thdSensorEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "thdSensorIndex"),
)
if mibBuilder.loadTexts:
    thdSensorEntry.setStatus("current")


class _ThdSensorIndex_Type(Integer32):
    """Custom type thdSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ThdSensorIndex_Type.__name__ = "Integer32"
_ThdSensorIndex_Object = MibTableColumn
thdSensorIndex = _ThdSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 1),
    _ThdSensorIndex_Type()
)
thdSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorIndex.setStatus("current")
_ThdSensorSerial_Type = DisplayString
_ThdSensorSerial_Object = MibTableColumn
thdSensorSerial = _ThdSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 2),
    _ThdSensorSerial_Type()
)
thdSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorSerial.setStatus("current")
_ThdSensorName_Type = DisplayString
_ThdSensorName_Object = MibTableColumn
thdSensorName = _ThdSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 3),
    _ThdSensorName_Type()
)
thdSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorName.setStatus("current")
_ThdSensorAvail_Type = Gauge32
_ThdSensorAvail_Object = MibTableColumn
thdSensorAvail = _ThdSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 4),
    _ThdSensorAvail_Type()
)
thdSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorAvail.setStatus("current")


class _ThdSensorTemp_Type(Integer32):
    """Custom type thdSensorTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_ThdSensorTemp_Type.__name__ = "Integer32"
_ThdSensorTemp_Object = MibTableColumn
thdSensorTemp = _ThdSensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 5),
    _ThdSensorTemp_Type()
)
thdSensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorTemp.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorTemp.setUnits("0.1 Degrees")


class _ThdSensorHumidity_Type(Integer32):
    """Custom type thdSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ThdSensorHumidity_Type.__name__ = "Integer32"
_ThdSensorHumidity_Object = MibTableColumn
thdSensorHumidity = _ThdSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 6),
    _ThdSensorHumidity_Type()
)
thdSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorHumidity.setUnits("%")


class _ThdSensorDewPoint_Type(Integer32):
    """Custom type thdSensorDewPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 200),
    )


_ThdSensorDewPoint_Type.__name__ = "Integer32"
_ThdSensorDewPoint_Object = MibTableColumn
thdSensorDewPoint = _ThdSensorDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 9, 1, 7),
    _ThdSensorDewPoint_Type()
)
thdSensorDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorDewPoint.setUnits("0.1 Degrees")
_RpmSensorTable_Object = MibTable
rpmSensorTable = _RpmSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10)
)
if mibBuilder.loadTexts:
    rpmSensorTable.setStatus("current")
_RpmSensorEntry_Object = MibTableRow
rpmSensorEntry = _RpmSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1)
)
rpmSensorEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "rpmSensorIndex"),
)
if mibBuilder.loadTexts:
    rpmSensorEntry.setStatus("current")


class _RpmSensorIndex_Type(Integer32):
    """Custom type rpmSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RpmSensorIndex_Type.__name__ = "Integer32"
_RpmSensorIndex_Object = MibTableColumn
rpmSensorIndex = _RpmSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 1),
    _RpmSensorIndex_Type()
)
rpmSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorIndex.setStatus("current")
_RpmSensorSerial_Type = DisplayString
_RpmSensorSerial_Object = MibTableColumn
rpmSensorSerial = _RpmSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 2),
    _RpmSensorSerial_Type()
)
rpmSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorSerial.setStatus("current")
_RpmSensorName_Type = DisplayString
_RpmSensorName_Object = MibTableColumn
rpmSensorName = _RpmSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 3),
    _RpmSensorName_Type()
)
rpmSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorName.setStatus("current")
_RpmSensorAvail_Type = Gauge32
_RpmSensorAvail_Object = MibTableColumn
rpmSensorAvail = _RpmSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 4),
    _RpmSensorAvail_Type()
)
rpmSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorAvail.setStatus("current")
_RpmSensorEnergy_Type = Gauge32
_RpmSensorEnergy_Object = MibTableColumn
rpmSensorEnergy = _RpmSensorEnergy_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 5),
    _RpmSensorEnergy_Type()
)
rpmSensorEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorEnergy.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorEnergy.setUnits("kWh")
_RpmSensorVoltage_Type = Gauge32
_RpmSensorVoltage_Object = MibTableColumn
rpmSensorVoltage = _RpmSensorVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 6),
    _RpmSensorVoltage_Type()
)
rpmSensorVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorVoltage.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorVoltage.setUnits("Volts (rms)")
_RpmSensorVoltageMax_Type = Gauge32
_RpmSensorVoltageMax_Object = MibTableColumn
rpmSensorVoltageMax = _RpmSensorVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 7),
    _RpmSensorVoltageMax_Type()
)
rpmSensorVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorVoltageMax.setUnits("Volts (rms)")
_RpmSensorVoltageMin_Type = Gauge32
_RpmSensorVoltageMin_Object = MibTableColumn
rpmSensorVoltageMin = _RpmSensorVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 8),
    _RpmSensorVoltageMin_Type()
)
rpmSensorVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorVoltageMin.setUnits("Volts (rms)")
_RpmSensorVoltagePeak_Type = Gauge32
_RpmSensorVoltagePeak_Object = MibTableColumn
rpmSensorVoltagePeak = _RpmSensorVoltagePeak_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 9),
    _RpmSensorVoltagePeak_Type()
)
rpmSensorVoltagePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorVoltagePeak.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorVoltagePeak.setUnits("Volts")
_RpmSensorCurrent_Type = Gauge32
_RpmSensorCurrent_Object = MibTableColumn
rpmSensorCurrent = _RpmSensorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 10),
    _RpmSensorCurrent_Type()
)
rpmSensorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorCurrent.setUnits("0.1 Amps (rms)")
_RpmSensorRealPower_Type = Gauge32
_RpmSensorRealPower_Object = MibTableColumn
rpmSensorRealPower = _RpmSensorRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 11),
    _RpmSensorRealPower_Type()
)
rpmSensorRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorRealPower.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorRealPower.setUnits("Watts")
_RpmSensorApparentPower_Type = Gauge32
_RpmSensorApparentPower_Object = MibTableColumn
rpmSensorApparentPower = _RpmSensorApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 12),
    _RpmSensorApparentPower_Type()
)
rpmSensorApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorApparentPower.setUnits("Volt-Amps")
_RpmSensorPowerFactor_Type = Gauge32
_RpmSensorPowerFactor_Object = MibTableColumn
rpmSensorPowerFactor = _RpmSensorPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 13),
    _RpmSensorPowerFactor_Type()
)
rpmSensorPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    rpmSensorPowerFactor.setUnits("%")
_RpmSensorOutlet1_Type = Gauge32
_RpmSensorOutlet1_Object = MibTableColumn
rpmSensorOutlet1 = _RpmSensorOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 14),
    _RpmSensorOutlet1_Type()
)
rpmSensorOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorOutlet1.setStatus("current")
_RpmSensorOutlet2_Type = Gauge32
_RpmSensorOutlet2_Object = MibTableColumn
rpmSensorOutlet2 = _RpmSensorOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 10, 1, 15),
    _RpmSensorOutlet2_Type()
)
rpmSensorOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmSensorOutlet2.setStatus("current")
_A2dSensorTable_Object = MibTable
a2dSensorTable = _A2dSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11)
)
if mibBuilder.loadTexts:
    a2dSensorTable.setStatus("current")
_A2DSensorEntry_Object = MibTableRow
a2DSensorEntry = _A2DSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1)
)
a2DSensorEntry.setIndexNames(
    (0, "GEIST-IMD-MIB", "a2dSensorIndex"),
)
if mibBuilder.loadTexts:
    a2DSensorEntry.setStatus("current")


class _A2dSensorIndex_Type(Integer32):
    """Custom type a2dSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_A2dSensorIndex_Type.__name__ = "Integer32"
_A2dSensorIndex_Object = MibTableColumn
a2dSensorIndex = _A2dSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 1),
    _A2dSensorIndex_Type()
)
a2dSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorIndex.setStatus("current")
_A2dSensorSerial_Type = DisplayString
_A2dSensorSerial_Object = MibTableColumn
a2dSensorSerial = _A2dSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 2),
    _A2dSensorSerial_Type()
)
a2dSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorSerial.setStatus("current")
_A2dSensorName_Type = DisplayString
_A2dSensorName_Object = MibTableColumn
a2dSensorName = _A2dSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 3),
    _A2dSensorName_Type()
)
a2dSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorName.setStatus("current")
_A2dSensorAvail_Type = Gauge32
_A2dSensorAvail_Object = MibTableColumn
a2dSensorAvail = _A2dSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 4),
    _A2dSensorAvail_Type()
)
a2dSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorAvail.setStatus("current")


class _A2dSensorValue_Type(Integer32):
    """Custom type a2dSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )


_A2dSensorValue_Type.__name__ = "Integer32"
_A2dSensorValue_Object = MibTableColumn
a2dSensorValue = _A2dSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 11, 1, 5),
    _A2dSensorValue_Type()
)
a2dSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2dSensorValue.setStatus("current")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767)
)
_TrapPrefix_ObjectIdentity = ObjectIdentity
trapPrefix = _TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0)
)

# Managed Objects groups


# Notification objects

internalTestNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10101)
)
if mibBuilder.loadTexts:
    internalTestNOTIFY.setStatus(
        "current"
    )

pduMainAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10305)
)
pduMainAvailNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduMainAvail")
)
if mibBuilder.loadTexts:
    pduMainAvailNOTIFY.setStatus(
        "current"
    )

pduTotalRealPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10309)
)
pduTotalRealPowerNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduTotalRealPower")
)
if mibBuilder.loadTexts:
    pduTotalRealPowerNOTIFY.setStatus(
        "current"
    )

pduTotalApparentPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10310)
)
pduTotalApparentPowerNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduTotalApparentPower")
)
if mibBuilder.loadTexts:
    pduTotalApparentPowerNOTIFY.setStatus(
        "current"
    )

pduTotalPowerFactorNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10311)
)
pduTotalPowerFactorNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduTotalPowerFactor")
)
if mibBuilder.loadTexts:
    pduTotalPowerFactorNOTIFY.setStatus(
        "current"
    )

pduTotalEnergyNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10312)
)
pduTotalEnergyNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduTotalEnergy")
)
if mibBuilder.loadTexts:
    pduTotalEnergyNOTIFY.setStatus(
        "current"
    )

pduPhaseVoltageNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10324)
)
pduPhaseVoltageNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseVoltage")
)
if mibBuilder.loadTexts:
    pduPhaseVoltageNOTIFY.setStatus(
        "current"
    )

pduPhaseVoltageMaxNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10325)
)
pduPhaseVoltageMaxNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseVoltageMax")
)
if mibBuilder.loadTexts:
    pduPhaseVoltageMaxNOTIFY.setStatus(
        "current"
    )

pduPhaseVoltageMinNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10326)
)
pduPhaseVoltageMinNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseVoltageMin")
)
if mibBuilder.loadTexts:
    pduPhaseVoltageMinNOTIFY.setStatus(
        "current"
    )

pduPhaseVoltagePeakNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10327)
)
pduPhaseVoltagePeakNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseVoltagePeak")
)
if mibBuilder.loadTexts:
    pduPhaseVoltagePeakNOTIFY.setStatus(
        "current"
    )

pduPhaseCurrentNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10328)
)
pduPhaseCurrentNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseCurrent")
)
if mibBuilder.loadTexts:
    pduPhaseCurrentNOTIFY.setStatus(
        "current"
    )

pduPhaseCurrentMaxNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10329)
)
pduPhaseCurrentMaxNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseCurrentMax")
)
if mibBuilder.loadTexts:
    pduPhaseCurrentMaxNOTIFY.setStatus(
        "current"
    )

pduPhaseCurrentMinNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10330)
)
pduPhaseCurrentMinNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseCurrentMin")
)
if mibBuilder.loadTexts:
    pduPhaseCurrentMinNOTIFY.setStatus(
        "current"
    )

pduPhaseCurrentPeakNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10331)
)
pduPhaseCurrentPeakNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseCurrentPeak")
)
if mibBuilder.loadTexts:
    pduPhaseCurrentPeakNOTIFY.setStatus(
        "current"
    )

pduPhaseRealPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10332)
)
pduPhaseRealPowerNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseRealPower")
)
if mibBuilder.loadTexts:
    pduPhaseRealPowerNOTIFY.setStatus(
        "current"
    )

pduPhaseApparentPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10333)
)
pduPhaseApparentPowerNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseApparentPower")
)
if mibBuilder.loadTexts:
    pduPhaseApparentPowerNOTIFY.setStatus(
        "current"
    )

pduPhasePowerFactorNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10334)
)
pduPhasePowerFactorNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhasePowerFactor")
)
if mibBuilder.loadTexts:
    pduPhasePowerFactorNOTIFY.setStatus(
        "current"
    )

pduPhaseEnergyNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10335)
)
pduPhaseEnergyNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseEnergy")
)
if mibBuilder.loadTexts:
    pduPhaseEnergyNOTIFY.setStatus(
        "current"
    )

pduBreakerCurrentNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10354)
)
pduBreakerCurrentNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduBreakerCurrent")
)
if mibBuilder.loadTexts:
    pduBreakerCurrentNOTIFY.setStatus(
        "current"
    )

pduBreakerCurrentMaxNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10355)
)
pduBreakerCurrentMaxNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduBreakerCurrentMax")
)
if mibBuilder.loadTexts:
    pduBreakerCurrentMaxNOTIFY.setStatus(
        "current"
    )

pduBreakerCurrentMinNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10356)
)
pduBreakerCurrentMinNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduBreakerCurrentMin")
)
if mibBuilder.loadTexts:
    pduBreakerCurrentMinNOTIFY.setStatus(
        "current"
    )

pduBreakerCurrentPeakNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10357)
)
pduBreakerCurrentPeakNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduBreakerCurrentPeak")
)
if mibBuilder.loadTexts:
    pduBreakerCurrentPeakNOTIFY.setStatus(
        "current"
    )

pduLineCurrentNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10374)
)
pduLineCurrentNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduLineCurrent")
)
if mibBuilder.loadTexts:
    pduLineCurrentNOTIFY.setStatus(
        "current"
    )

pduLineCurrentMaxNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10375)
)
pduLineCurrentMaxNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduLineCurrentMax")
)
if mibBuilder.loadTexts:
    pduLineCurrentMaxNOTIFY.setStatus(
        "current"
    )

pduLineCurrentMinNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10376)
)
pduLineCurrentMinNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduLineCurrentMin")
)
if mibBuilder.loadTexts:
    pduLineCurrentMinNOTIFY.setStatus(
        "current"
    )

pduLineCurrentPeakNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10377)
)
pduLineCurrentPeakNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "pduLineCurrentPeak")
)
if mibBuilder.loadTexts:
    pduLineCurrentPeakNOTIFY.setStatus(
        "current"
    )

tempSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10404)
)
tempSensorAvailNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "tempSensorAvail")
)
if mibBuilder.loadTexts:
    tempSensorAvailNOTIFY.setStatus(
        "current"
    )

tempSensorTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10405)
)
tempSensorTempNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "tempSensorTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    tempSensorTempNOTIFY.setStatus(
        "current"
    )

airFlowSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10504)
)
airFlowSensorAvailNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "airFlowSensorAvail")
)
if mibBuilder.loadTexts:
    airFlowSensorAvailNOTIFY.setStatus(
        "current"
    )

airFlowSensorTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10505)
)
airFlowSensorTempNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "airFlowSensorTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    airFlowSensorTempNOTIFY.setStatus(
        "current"
    )

airFlowSensorFlowNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10506)
)
airFlowSensorFlowNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "airFlowSensorFlow")
)
if mibBuilder.loadTexts:
    airFlowSensorFlowNOTIFY.setStatus(
        "current"
    )

airFlowSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10507)
)
airFlowSensorHumidityNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "airFlowSensorHumidity")
)
if mibBuilder.loadTexts:
    airFlowSensorHumidityNOTIFY.setStatus(
        "current"
    )

airFlowSensorDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10508)
)
airFlowSensorDewPointNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "airFlowSensorDewPoint"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    airFlowSensorDewPointNOTIFY.setStatus(
        "current"
    )

dewPointSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10604)
)
dewPointSensorAvailNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "dewPointSensorAvail")
)
if mibBuilder.loadTexts:
    dewPointSensorAvailNOTIFY.setStatus(
        "current"
    )

dewPointSensorTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10605)
)
dewPointSensorTempNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "dewPointSensorTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    dewPointSensorTempNOTIFY.setStatus(
        "current"
    )

dewPointSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10606)
)
dewPointSensorHumidityNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "dewPointSensorHumidity")
)
if mibBuilder.loadTexts:
    dewPointSensorHumidityNOTIFY.setStatus(
        "current"
    )

dewPointSensorDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10607)
)
dewPointSensorDewPointNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "dewPointSensorDewPoint"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    dewPointSensorDewPointNOTIFY.setStatus(
        "current"
    )

ccatSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10704)
)
ccatSensorAvailNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "ccatSensorAvail")
)
if mibBuilder.loadTexts:
    ccatSensorAvailNOTIFY.setStatus(
        "current"
    )

ccatSensorValueNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10705)
)
ccatSensorValueNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "ccatSensorValue"),
        ("GEIST-IMD-MIB", "ccatSensorType"))
)
if mibBuilder.loadTexts:
    ccatSensorValueNOTIFY.setStatus(
        "current"
    )

t3hdSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10804)
)
t3hdSensorAvailNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "t3hdSensorAvail")
)
if mibBuilder.loadTexts:
    t3hdSensorAvailNOTIFY.setStatus(
        "current"
    )

t3hdSensorIntTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10806)
)
t3hdSensorIntTempNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "t3hdSensorIntTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntTempNOTIFY.setStatus(
        "current"
    )

t3hdSensorIntHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10807)
)
t3hdSensorIntHumidityNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "t3hdSensorIntHumidity")
)
if mibBuilder.loadTexts:
    t3hdSensorIntHumidityNOTIFY.setStatus(
        "current"
    )

t3hdSensorIntDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10808)
)
t3hdSensorIntDewPointNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "t3hdSensorIntDewPoint"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntDewPointNOTIFY.setStatus(
        "current"
    )

t3hdSensorExtATempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10811)
)
t3hdSensorExtATempNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "t3hdSensorExtATemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtATempNOTIFY.setStatus(
        "current"
    )

t3hdSensorExtBTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10814)
)
t3hdSensorExtBTempNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "t3hdSensorExtBTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtBTempNOTIFY.setStatus(
        "current"
    )

thdSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10904)
)
thdSensorAvailNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "thdSensorAvail")
)
if mibBuilder.loadTexts:
    thdSensorAvailNOTIFY.setStatus(
        "current"
    )

thdSensorTempNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10905)
)
thdSensorTempNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "thdSensorTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    thdSensorTempNOTIFY.setStatus(
        "current"
    )

thdSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10906)
)
thdSensorHumidityNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "thdSensorHumidity")
)
if mibBuilder.loadTexts:
    thdSensorHumidityNOTIFY.setStatus(
        "current"
    )

thdSensorDewPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 10907)
)
thdSensorDewPointNOTIFY.setObjects(
      *(("GEIST-IMD-MIB", "thdSensorDewPoint"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    thdSensorDewPointNOTIFY.setStatus(
        "current"
    )

rpmSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11004)
)
rpmSensorAvailNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorAvail")
)
if mibBuilder.loadTexts:
    rpmSensorAvailNOTIFY.setStatus(
        "current"
    )

rpmSensorEnergyNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11005)
)
rpmSensorEnergyNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorEnergy")
)
if mibBuilder.loadTexts:
    rpmSensorEnergyNOTIFY.setStatus(
        "current"
    )

rpmSensorVoltageNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11006)
)
rpmSensorVoltageNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorVoltage")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageNOTIFY.setStatus(
        "current"
    )

rpmSensorVoltageMaxNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11007)
)
rpmSensorVoltageMaxNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorVoltageMax")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageMaxNOTIFY.setStatus(
        "current"
    )

rpmSensorVoltageMinNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11008)
)
rpmSensorVoltageMinNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorVoltageMin")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageMinNOTIFY.setStatus(
        "current"
    )

rpmSensorVoltagePeakNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11009)
)
rpmSensorVoltagePeakNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorVoltagePeak")
)
if mibBuilder.loadTexts:
    rpmSensorVoltagePeakNOTIFY.setStatus(
        "current"
    )

rpmSensorCurrentNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11010)
)
rpmSensorCurrentNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorCurrent")
)
if mibBuilder.loadTexts:
    rpmSensorCurrentNOTIFY.setStatus(
        "current"
    )

rpmSensorRealPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11011)
)
rpmSensorRealPowerNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorRealPower")
)
if mibBuilder.loadTexts:
    rpmSensorRealPowerNOTIFY.setStatus(
        "current"
    )

rpmSensorApparentPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11012)
)
rpmSensorApparentPowerNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorApparentPower")
)
if mibBuilder.loadTexts:
    rpmSensorApparentPowerNOTIFY.setStatus(
        "current"
    )

rpmSensorPowerFactorNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11013)
)
rpmSensorPowerFactorNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorPowerFactor")
)
if mibBuilder.loadTexts:
    rpmSensorPowerFactorNOTIFY.setStatus(
        "current"
    )

a2dSensorAvailNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11104)
)
a2dSensorAvailNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "a2dSensorAvail")
)
if mibBuilder.loadTexts:
    a2dSensorAvailNOTIFY.setStatus(
        "current"
    )

a2dSensorValueNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 11105)
)
a2dSensorValueNOTIFY.setObjects(
    ("GEIST-IMD-MIB", "a2dSensorValue")
)
if mibBuilder.loadTexts:
    a2dSensorValueNOTIFY.setStatus(
        "current"
    )

pduMainAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20305)
)
pduMainAvailCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduMainAvail")
)
if mibBuilder.loadTexts:
    pduMainAvailCLEAR.setStatus(
        "current"
    )

pduTotalRealPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20309)
)
pduTotalRealPowerCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduTotalRealPower")
)
if mibBuilder.loadTexts:
    pduTotalRealPowerCLEAR.setStatus(
        "current"
    )

pduTotalApparentPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20310)
)
pduTotalApparentPowerCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduTotalApparentPower")
)
if mibBuilder.loadTexts:
    pduTotalApparentPowerCLEAR.setStatus(
        "current"
    )

pduTotalPowerFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20311)
)
pduTotalPowerFactorCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduTotalPowerFactor")
)
if mibBuilder.loadTexts:
    pduTotalPowerFactorCLEAR.setStatus(
        "current"
    )

pduTotalEnergyCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20312)
)
pduTotalEnergyCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduTotalEnergy")
)
if mibBuilder.loadTexts:
    pduTotalEnergyCLEAR.setStatus(
        "current"
    )

pduPhaseVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20324)
)
pduPhaseVoltageCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseVoltage")
)
if mibBuilder.loadTexts:
    pduPhaseVoltageCLEAR.setStatus(
        "current"
    )

pduPhaseVoltageMaxCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20325)
)
pduPhaseVoltageMaxCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseVoltageMax")
)
if mibBuilder.loadTexts:
    pduPhaseVoltageMaxCLEAR.setStatus(
        "current"
    )

pduPhaseVoltageMinCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20326)
)
pduPhaseVoltageMinCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseVoltageMin")
)
if mibBuilder.loadTexts:
    pduPhaseVoltageMinCLEAR.setStatus(
        "current"
    )

pduPhaseVoltagePeakCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20327)
)
pduPhaseVoltagePeakCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseVoltagePeak")
)
if mibBuilder.loadTexts:
    pduPhaseVoltagePeakCLEAR.setStatus(
        "current"
    )

pduPhaseCurrentCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20328)
)
pduPhaseCurrentCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseCurrent")
)
if mibBuilder.loadTexts:
    pduPhaseCurrentCLEAR.setStatus(
        "current"
    )

pduPhaseCurrentMaxCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20329)
)
pduPhaseCurrentMaxCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseCurrentMax")
)
if mibBuilder.loadTexts:
    pduPhaseCurrentMaxCLEAR.setStatus(
        "current"
    )

pduPhaseCurrentMinCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20330)
)
pduPhaseCurrentMinCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseCurrentMin")
)
if mibBuilder.loadTexts:
    pduPhaseCurrentMinCLEAR.setStatus(
        "current"
    )

pduPhaseCurrentPeakCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20331)
)
pduPhaseCurrentPeakCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseCurrentPeak")
)
if mibBuilder.loadTexts:
    pduPhaseCurrentPeakCLEAR.setStatus(
        "current"
    )

pduPhaseRealPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20332)
)
pduPhaseRealPowerCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseRealPower")
)
if mibBuilder.loadTexts:
    pduPhaseRealPowerCLEAR.setStatus(
        "current"
    )

pduPhaseApparentPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20333)
)
pduPhaseApparentPowerCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseApparentPower")
)
if mibBuilder.loadTexts:
    pduPhaseApparentPowerCLEAR.setStatus(
        "current"
    )

pduPhasePowerFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20334)
)
pduPhasePowerFactorCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhasePowerFactor")
)
if mibBuilder.loadTexts:
    pduPhasePowerFactorCLEAR.setStatus(
        "current"
    )

pduPhaseEnergyCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20335)
)
pduPhaseEnergyCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduPhaseEnergy")
)
if mibBuilder.loadTexts:
    pduPhaseEnergyCLEAR.setStatus(
        "current"
    )

pduBreakerCurrentCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20354)
)
pduBreakerCurrentCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduBreakerCurrent")
)
if mibBuilder.loadTexts:
    pduBreakerCurrentCLEAR.setStatus(
        "current"
    )

pduBreakerCurrentMaxCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20355)
)
pduBreakerCurrentMaxCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduBreakerCurrentMax")
)
if mibBuilder.loadTexts:
    pduBreakerCurrentMaxCLEAR.setStatus(
        "current"
    )

pduBreakerCurrentMinCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20356)
)
pduBreakerCurrentMinCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduBreakerCurrentMin")
)
if mibBuilder.loadTexts:
    pduBreakerCurrentMinCLEAR.setStatus(
        "current"
    )

pduBreakerCurrentPeakCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20357)
)
pduBreakerCurrentPeakCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduBreakerCurrentPeak")
)
if mibBuilder.loadTexts:
    pduBreakerCurrentPeakCLEAR.setStatus(
        "current"
    )

pduLineCurrentCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20374)
)
pduLineCurrentCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduLineCurrent")
)
if mibBuilder.loadTexts:
    pduLineCurrentCLEAR.setStatus(
        "current"
    )

pduLineCurrentMaxCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20375)
)
pduLineCurrentMaxCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduLineCurrentMax")
)
if mibBuilder.loadTexts:
    pduLineCurrentMaxCLEAR.setStatus(
        "current"
    )

pduLineCurrentMinCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20376)
)
pduLineCurrentMinCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduLineCurrentMin")
)
if mibBuilder.loadTexts:
    pduLineCurrentMinCLEAR.setStatus(
        "current"
    )

pduLineCurrentPeakCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20377)
)
pduLineCurrentPeakCLEAR.setObjects(
    ("GEIST-IMD-MIB", "pduLineCurrentPeak")
)
if mibBuilder.loadTexts:
    pduLineCurrentPeakCLEAR.setStatus(
        "current"
    )

tempSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20404)
)
tempSensorAvailCLEAR.setObjects(
    ("GEIST-IMD-MIB", "tempSensorAvail")
)
if mibBuilder.loadTexts:
    tempSensorAvailCLEAR.setStatus(
        "current"
    )

tempSensorTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20405)
)
tempSensorTempCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "tempSensorTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    tempSensorTempCLEAR.setStatus(
        "current"
    )

airFlowSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20504)
)
airFlowSensorAvailCLEAR.setObjects(
    ("GEIST-IMD-MIB", "airFlowSensorAvail")
)
if mibBuilder.loadTexts:
    airFlowSensorAvailCLEAR.setStatus(
        "current"
    )

airFlowSensorTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20505)
)
airFlowSensorTempCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "airFlowSensorTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    airFlowSensorTempCLEAR.setStatus(
        "current"
    )

airFlowSensorFlowCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20506)
)
airFlowSensorFlowCLEAR.setObjects(
    ("GEIST-IMD-MIB", "airFlowSensorFlow")
)
if mibBuilder.loadTexts:
    airFlowSensorFlowCLEAR.setStatus(
        "current"
    )

airFlowSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20507)
)
airFlowSensorHumidityCLEAR.setObjects(
    ("GEIST-IMD-MIB", "airFlowSensorHumidity")
)
if mibBuilder.loadTexts:
    airFlowSensorHumidityCLEAR.setStatus(
        "current"
    )

airFlowSensorDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20508)
)
airFlowSensorDewPointCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "airFlowSensorDewPoint"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    airFlowSensorDewPointCLEAR.setStatus(
        "current"
    )

dewPointSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20604)
)
dewPointSensorAvailCLEAR.setObjects(
    ("GEIST-IMD-MIB", "dewPointSensorAvail")
)
if mibBuilder.loadTexts:
    dewPointSensorAvailCLEAR.setStatus(
        "current"
    )

dewPointSensorTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20605)
)
dewPointSensorTempCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "dewPointSensorTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    dewPointSensorTempCLEAR.setStatus(
        "current"
    )

dewPointSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20606)
)
dewPointSensorHumidityCLEAR.setObjects(
    ("GEIST-IMD-MIB", "dewPointSensorHumidity")
)
if mibBuilder.loadTexts:
    dewPointSensorHumidityCLEAR.setStatus(
        "current"
    )

dewPointSensorDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20607)
)
dewPointSensorDewPointCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "dewPointSensorDewPoint"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    dewPointSensorDewPointCLEAR.setStatus(
        "current"
    )

ccatSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20704)
)
ccatSensorAvailCLEAR.setObjects(
    ("GEIST-IMD-MIB", "ccatSensorAvail")
)
if mibBuilder.loadTexts:
    ccatSensorAvailCLEAR.setStatus(
        "current"
    )

ccatSensorValueCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20705)
)
ccatSensorValueCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "ccatSensorValue"),
        ("GEIST-IMD-MIB", "ccatSensorType"))
)
if mibBuilder.loadTexts:
    ccatSensorValueCLEAR.setStatus(
        "current"
    )

t3hdSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20804)
)
t3hdSensorAvailCLEAR.setObjects(
    ("GEIST-IMD-MIB", "t3hdSensorAvail")
)
if mibBuilder.loadTexts:
    t3hdSensorAvailCLEAR.setStatus(
        "current"
    )

t3hdSensorIntTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20806)
)
t3hdSensorIntTempCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "t3hdSensorIntTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntTempCLEAR.setStatus(
        "current"
    )

t3hdSensorIntHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20807)
)
t3hdSensorIntHumidityCLEAR.setObjects(
    ("GEIST-IMD-MIB", "t3hdSensorIntHumidity")
)
if mibBuilder.loadTexts:
    t3hdSensorIntHumidityCLEAR.setStatus(
        "current"
    )

t3hdSensorIntDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20808)
)
t3hdSensorIntDewPointCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "t3hdSensorIntDewPoint"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorIntDewPointCLEAR.setStatus(
        "current"
    )

t3hdSensorExtATempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20811)
)
t3hdSensorExtATempCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "t3hdSensorExtATemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtATempCLEAR.setStatus(
        "current"
    )

t3hdSensorExtBTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20814)
)
t3hdSensorExtBTempCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "t3hdSensorExtBTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    t3hdSensorExtBTempCLEAR.setStatus(
        "current"
    )

thdSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20904)
)
thdSensorAvailCLEAR.setObjects(
    ("GEIST-IMD-MIB", "thdSensorAvail")
)
if mibBuilder.loadTexts:
    thdSensorAvailCLEAR.setStatus(
        "current"
    )

thdSensorTempCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20905)
)
thdSensorTempCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "thdSensorTemp"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    thdSensorTempCLEAR.setStatus(
        "current"
    )

thdSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20906)
)
thdSensorHumidityCLEAR.setObjects(
    ("GEIST-IMD-MIB", "thdSensorHumidity")
)
if mibBuilder.loadTexts:
    thdSensorHumidityCLEAR.setStatus(
        "current"
    )

thdSensorDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 20907)
)
thdSensorDewPointCLEAR.setObjects(
      *(("GEIST-IMD-MIB", "thdSensorDewPoint"),
        ("GEIST-IMD-MIB", "temperatureUnits"))
)
if mibBuilder.loadTexts:
    thdSensorDewPointCLEAR.setStatus(
        "current"
    )

rpmSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21004)
)
rpmSensorAvailCLEAR.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorAvail")
)
if mibBuilder.loadTexts:
    rpmSensorAvailCLEAR.setStatus(
        "current"
    )

rpmSensorEnergyCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21005)
)
rpmSensorEnergyCLEAR.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorEnergy")
)
if mibBuilder.loadTexts:
    rpmSensorEnergyCLEAR.setStatus(
        "current"
    )

rpmSensorVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21006)
)
rpmSensorVoltageCLEAR.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorVoltage")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageCLEAR.setStatus(
        "current"
    )

rpmSensorVoltageMaxCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21007)
)
rpmSensorVoltageMaxCLEAR.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorVoltageMax")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageMaxCLEAR.setStatus(
        "current"
    )

rpmSensorVoltageMinCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21008)
)
rpmSensorVoltageMinCLEAR.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorVoltageMin")
)
if mibBuilder.loadTexts:
    rpmSensorVoltageMinCLEAR.setStatus(
        "current"
    )

rpmSensorVoltagePeakCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21009)
)
rpmSensorVoltagePeakCLEAR.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorVoltagePeak")
)
if mibBuilder.loadTexts:
    rpmSensorVoltagePeakCLEAR.setStatus(
        "current"
    )

rpmSensorCurrentCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21010)
)
rpmSensorCurrentCLEAR.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorCurrent")
)
if mibBuilder.loadTexts:
    rpmSensorCurrentCLEAR.setStatus(
        "current"
    )

rpmSensorRealPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21011)
)
rpmSensorRealPowerCLEAR.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorRealPower")
)
if mibBuilder.loadTexts:
    rpmSensorRealPowerCLEAR.setStatus(
        "current"
    )

rpmSensorApparentPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21012)
)
rpmSensorApparentPowerCLEAR.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorApparentPower")
)
if mibBuilder.loadTexts:
    rpmSensorApparentPowerCLEAR.setStatus(
        "current"
    )

rpmSensorPowerFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21013)
)
rpmSensorPowerFactorCLEAR.setObjects(
    ("GEIST-IMD-MIB", "rpmSensorPowerFactor")
)
if mibBuilder.loadTexts:
    rpmSensorPowerFactorCLEAR.setStatus(
        "current"
    )

a2dSensorAvailCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21104)
)
a2dSensorAvailCLEAR.setObjects(
    ("GEIST-IMD-MIB", "a2dSensorAvail")
)
if mibBuilder.loadTexts:
    a2dSensorAvailCLEAR.setStatus(
        "current"
    )

a2dSensorValueCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 5, 2, 32767, 0, 21105)
)
a2dSensorValueCLEAR.setObjects(
    ("GEIST-IMD-MIB", "a2dSensorValue")
)
if mibBuilder.loadTexts:
    a2dSensorValueCLEAR.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GEIST-IMD-MIB",
    **{"geist": geist,
       "blackbird": blackbird,
       "imd": imd,
       "deviceInfo": deviceInfo,
       "productTitle": productTitle,
       "productVersion": productVersion,
       "productFriendlyName": productFriendlyName,
       "productMacAddress": productMacAddress,
       "productUrl": productUrl,
       "deviceCount": deviceCount,
       "temperatureUnits": temperatureUnits,
       "pdu": pdu,
       "pduMainTable": pduMainTable,
       "pduMainEntry": pduMainEntry,
       "pduMainIndex": pduMainIndex,
       "pduMainSerial": pduMainSerial,
       "pduMainName": pduMainName,
       "pduMainLabel": pduMainLabel,
       "pduMainAvail": pduMainAvail,
       "pduMeterType": pduMeterType,
       "pduTotalName": pduTotalName,
       "pduTotalLabel": pduTotalLabel,
       "pduTotalRealPower": pduTotalRealPower,
       "pduTotalApparentPower": pduTotalApparentPower,
       "pduTotalPowerFactor": pduTotalPowerFactor,
       "pduTotalEnergy": pduTotalEnergy,
       "pduPhaseTable": pduPhaseTable,
       "pduPhaseEntry": pduPhaseEntry,
       "pduPhaseIndex": pduPhaseIndex,
       "pduPhaseName": pduPhaseName,
       "pduPhaseLabel": pduPhaseLabel,
       "pduPhaseVoltage": pduPhaseVoltage,
       "pduPhaseVoltageMax": pduPhaseVoltageMax,
       "pduPhaseVoltageMin": pduPhaseVoltageMin,
       "pduPhaseVoltagePeak": pduPhaseVoltagePeak,
       "pduPhaseCurrent": pduPhaseCurrent,
       "pduPhaseCurrentMax": pduPhaseCurrentMax,
       "pduPhaseCurrentMin": pduPhaseCurrentMin,
       "pduPhaseCurrentPeak": pduPhaseCurrentPeak,
       "pduPhaseRealPower": pduPhaseRealPower,
       "pduPhaseApparentPower": pduPhaseApparentPower,
       "pduPhasePowerFactor": pduPhasePowerFactor,
       "pduPhaseEnergy": pduPhaseEnergy,
       "pduBreakerTable": pduBreakerTable,
       "pduBreakerEntry": pduBreakerEntry,
       "pduBreakerIndex": pduBreakerIndex,
       "pduBreakerName": pduBreakerName,
       "pduBreakerLabel": pduBreakerLabel,
       "pduBreakerCurrent": pduBreakerCurrent,
       "pduBreakerCurrentMax": pduBreakerCurrentMax,
       "pduBreakerCurrentMin": pduBreakerCurrentMin,
       "pduBreakerCurrentPeak": pduBreakerCurrentPeak,
       "pduLineTable": pduLineTable,
       "pduLineEntry": pduLineEntry,
       "pduLineIndex": pduLineIndex,
       "pduLineName": pduLineName,
       "pduLineLabel": pduLineLabel,
       "pduLineCurrent": pduLineCurrent,
       "pduLineCurrentMax": pduLineCurrentMax,
       "pduLineCurrentMin": pduLineCurrentMin,
       "pduLineCurrentPeak": pduLineCurrentPeak,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorIndex": tempSensorIndex,
       "tempSensorSerial": tempSensorSerial,
       "tempSensorName": tempSensorName,
       "tempSensorAvail": tempSensorAvail,
       "tempSensorTemp": tempSensorTemp,
       "airFlowSensorTable": airFlowSensorTable,
       "airFlowSensorEntry": airFlowSensorEntry,
       "airFlowSensorIndex": airFlowSensorIndex,
       "airFlowSensorSerial": airFlowSensorSerial,
       "airFlowSensorName": airFlowSensorName,
       "airFlowSensorAvail": airFlowSensorAvail,
       "airFlowSensorTemp": airFlowSensorTemp,
       "airFlowSensorFlow": airFlowSensorFlow,
       "airFlowSensorHumidity": airFlowSensorHumidity,
       "airFlowSensorDewPoint": airFlowSensorDewPoint,
       "dewPointSensorTable": dewPointSensorTable,
       "dewPointSensorEntry": dewPointSensorEntry,
       "dewPointSensorIndex": dewPointSensorIndex,
       "dewPointSensorSerial": dewPointSensorSerial,
       "dewPointSensorName": dewPointSensorName,
       "dewPointSensorAvail": dewPointSensorAvail,
       "dewPointSensorTemp": dewPointSensorTemp,
       "dewPointSensorHumidity": dewPointSensorHumidity,
       "dewPointSensorDewPoint": dewPointSensorDewPoint,
       "ccatSensorTable": ccatSensorTable,
       "ccatSensorEntry": ccatSensorEntry,
       "ccatSensorIndex": ccatSensorIndex,
       "ccatSensorSerial": ccatSensorSerial,
       "ccatSensorName": ccatSensorName,
       "ccatSensorAvail": ccatSensorAvail,
       "ccatSensorValue": ccatSensorValue,
       "ccatSensorType": ccatSensorType,
       "ccatSensorDescription": ccatSensorDescription,
       "t3hdSensorTable": t3hdSensorTable,
       "t3hdSensorEntry": t3hdSensorEntry,
       "t3hdSensorIndex": t3hdSensorIndex,
       "t3hdSensorSerial": t3hdSensorSerial,
       "t3hdSensorName": t3hdSensorName,
       "t3hdSensorAvail": t3hdSensorAvail,
       "t3hdSensorIntName": t3hdSensorIntName,
       "t3hdSensorIntTemp": t3hdSensorIntTemp,
       "t3hdSensorIntHumidity": t3hdSensorIntHumidity,
       "t3hdSensorIntDewPoint": t3hdSensorIntDewPoint,
       "t3hdSensorExtAAvail": t3hdSensorExtAAvail,
       "t3hdSensorExtAName": t3hdSensorExtAName,
       "t3hdSensorExtATemp": t3hdSensorExtATemp,
       "t3hdSensorExtBAvail": t3hdSensorExtBAvail,
       "t3hdSensorExtBName": t3hdSensorExtBName,
       "t3hdSensorExtBTemp": t3hdSensorExtBTemp,
       "thdSensorTable": thdSensorTable,
       "thdSensorEntry": thdSensorEntry,
       "thdSensorIndex": thdSensorIndex,
       "thdSensorSerial": thdSensorSerial,
       "thdSensorName": thdSensorName,
       "thdSensorAvail": thdSensorAvail,
       "thdSensorTemp": thdSensorTemp,
       "thdSensorHumidity": thdSensorHumidity,
       "thdSensorDewPoint": thdSensorDewPoint,
       "rpmSensorTable": rpmSensorTable,
       "rpmSensorEntry": rpmSensorEntry,
       "rpmSensorIndex": rpmSensorIndex,
       "rpmSensorSerial": rpmSensorSerial,
       "rpmSensorName": rpmSensorName,
       "rpmSensorAvail": rpmSensorAvail,
       "rpmSensorEnergy": rpmSensorEnergy,
       "rpmSensorVoltage": rpmSensorVoltage,
       "rpmSensorVoltageMax": rpmSensorVoltageMax,
       "rpmSensorVoltageMin": rpmSensorVoltageMin,
       "rpmSensorVoltagePeak": rpmSensorVoltagePeak,
       "rpmSensorCurrent": rpmSensorCurrent,
       "rpmSensorRealPower": rpmSensorRealPower,
       "rpmSensorApparentPower": rpmSensorApparentPower,
       "rpmSensorPowerFactor": rpmSensorPowerFactor,
       "rpmSensorOutlet1": rpmSensorOutlet1,
       "rpmSensorOutlet2": rpmSensorOutlet2,
       "a2dSensorTable": a2dSensorTable,
       "a2DSensorEntry": a2DSensorEntry,
       "a2dSensorIndex": a2dSensorIndex,
       "a2dSensorSerial": a2dSensorSerial,
       "a2dSensorName": a2dSensorName,
       "a2dSensorAvail": a2dSensorAvail,
       "a2dSensorValue": a2dSensorValue,
       "trap": trap,
       "trapPrefix": trapPrefix,
       "internalTestNOTIFY": internalTestNOTIFY,
       "pduMainAvailNOTIFY": pduMainAvailNOTIFY,
       "pduTotalRealPowerNOTIFY": pduTotalRealPowerNOTIFY,
       "pduTotalApparentPowerNOTIFY": pduTotalApparentPowerNOTIFY,
       "pduTotalPowerFactorNOTIFY": pduTotalPowerFactorNOTIFY,
       "pduTotalEnergyNOTIFY": pduTotalEnergyNOTIFY,
       "pduPhaseVoltageNOTIFY": pduPhaseVoltageNOTIFY,
       "pduPhaseVoltageMaxNOTIFY": pduPhaseVoltageMaxNOTIFY,
       "pduPhaseVoltageMinNOTIFY": pduPhaseVoltageMinNOTIFY,
       "pduPhaseVoltagePeakNOTIFY": pduPhaseVoltagePeakNOTIFY,
       "pduPhaseCurrentNOTIFY": pduPhaseCurrentNOTIFY,
       "pduPhaseCurrentMaxNOTIFY": pduPhaseCurrentMaxNOTIFY,
       "pduPhaseCurrentMinNOTIFY": pduPhaseCurrentMinNOTIFY,
       "pduPhaseCurrentPeakNOTIFY": pduPhaseCurrentPeakNOTIFY,
       "pduPhaseRealPowerNOTIFY": pduPhaseRealPowerNOTIFY,
       "pduPhaseApparentPowerNOTIFY": pduPhaseApparentPowerNOTIFY,
       "pduPhasePowerFactorNOTIFY": pduPhasePowerFactorNOTIFY,
       "pduPhaseEnergyNOTIFY": pduPhaseEnergyNOTIFY,
       "pduBreakerCurrentNOTIFY": pduBreakerCurrentNOTIFY,
       "pduBreakerCurrentMaxNOTIFY": pduBreakerCurrentMaxNOTIFY,
       "pduBreakerCurrentMinNOTIFY": pduBreakerCurrentMinNOTIFY,
       "pduBreakerCurrentPeakNOTIFY": pduBreakerCurrentPeakNOTIFY,
       "pduLineCurrentNOTIFY": pduLineCurrentNOTIFY,
       "pduLineCurrentMaxNOTIFY": pduLineCurrentMaxNOTIFY,
       "pduLineCurrentMinNOTIFY": pduLineCurrentMinNOTIFY,
       "pduLineCurrentPeakNOTIFY": pduLineCurrentPeakNOTIFY,
       "tempSensorAvailNOTIFY": tempSensorAvailNOTIFY,
       "tempSensorTempNOTIFY": tempSensorTempNOTIFY,
       "airFlowSensorAvailNOTIFY": airFlowSensorAvailNOTIFY,
       "airFlowSensorTempNOTIFY": airFlowSensorTempNOTIFY,
       "airFlowSensorFlowNOTIFY": airFlowSensorFlowNOTIFY,
       "airFlowSensorHumidityNOTIFY": airFlowSensorHumidityNOTIFY,
       "airFlowSensorDewPointNOTIFY": airFlowSensorDewPointNOTIFY,
       "dewPointSensorAvailNOTIFY": dewPointSensorAvailNOTIFY,
       "dewPointSensorTempNOTIFY": dewPointSensorTempNOTIFY,
       "dewPointSensorHumidityNOTIFY": dewPointSensorHumidityNOTIFY,
       "dewPointSensorDewPointNOTIFY": dewPointSensorDewPointNOTIFY,
       "ccatSensorAvailNOTIFY": ccatSensorAvailNOTIFY,
       "ccatSensorValueNOTIFY": ccatSensorValueNOTIFY,
       "t3hdSensorAvailNOTIFY": t3hdSensorAvailNOTIFY,
       "t3hdSensorIntTempNOTIFY": t3hdSensorIntTempNOTIFY,
       "t3hdSensorIntHumidityNOTIFY": t3hdSensorIntHumidityNOTIFY,
       "t3hdSensorIntDewPointNOTIFY": t3hdSensorIntDewPointNOTIFY,
       "t3hdSensorExtATempNOTIFY": t3hdSensorExtATempNOTIFY,
       "t3hdSensorExtBTempNOTIFY": t3hdSensorExtBTempNOTIFY,
       "thdSensorAvailNOTIFY": thdSensorAvailNOTIFY,
       "thdSensorTempNOTIFY": thdSensorTempNOTIFY,
       "thdSensorHumidityNOTIFY": thdSensorHumidityNOTIFY,
       "thdSensorDewPointNOTIFY": thdSensorDewPointNOTIFY,
       "rpmSensorAvailNOTIFY": rpmSensorAvailNOTIFY,
       "rpmSensorEnergyNOTIFY": rpmSensorEnergyNOTIFY,
       "rpmSensorVoltageNOTIFY": rpmSensorVoltageNOTIFY,
       "rpmSensorVoltageMaxNOTIFY": rpmSensorVoltageMaxNOTIFY,
       "rpmSensorVoltageMinNOTIFY": rpmSensorVoltageMinNOTIFY,
       "rpmSensorVoltagePeakNOTIFY": rpmSensorVoltagePeakNOTIFY,
       "rpmSensorCurrentNOTIFY": rpmSensorCurrentNOTIFY,
       "rpmSensorRealPowerNOTIFY": rpmSensorRealPowerNOTIFY,
       "rpmSensorApparentPowerNOTIFY": rpmSensorApparentPowerNOTIFY,
       "rpmSensorPowerFactorNOTIFY": rpmSensorPowerFactorNOTIFY,
       "a2dSensorAvailNOTIFY": a2dSensorAvailNOTIFY,
       "a2dSensorValueNOTIFY": a2dSensorValueNOTIFY,
       "pduMainAvailCLEAR": pduMainAvailCLEAR,
       "pduTotalRealPowerCLEAR": pduTotalRealPowerCLEAR,
       "pduTotalApparentPowerCLEAR": pduTotalApparentPowerCLEAR,
       "pduTotalPowerFactorCLEAR": pduTotalPowerFactorCLEAR,
       "pduTotalEnergyCLEAR": pduTotalEnergyCLEAR,
       "pduPhaseVoltageCLEAR": pduPhaseVoltageCLEAR,
       "pduPhaseVoltageMaxCLEAR": pduPhaseVoltageMaxCLEAR,
       "pduPhaseVoltageMinCLEAR": pduPhaseVoltageMinCLEAR,
       "pduPhaseVoltagePeakCLEAR": pduPhaseVoltagePeakCLEAR,
       "pduPhaseCurrentCLEAR": pduPhaseCurrentCLEAR,
       "pduPhaseCurrentMaxCLEAR": pduPhaseCurrentMaxCLEAR,
       "pduPhaseCurrentMinCLEAR": pduPhaseCurrentMinCLEAR,
       "pduPhaseCurrentPeakCLEAR": pduPhaseCurrentPeakCLEAR,
       "pduPhaseRealPowerCLEAR": pduPhaseRealPowerCLEAR,
       "pduPhaseApparentPowerCLEAR": pduPhaseApparentPowerCLEAR,
       "pduPhasePowerFactorCLEAR": pduPhasePowerFactorCLEAR,
       "pduPhaseEnergyCLEAR": pduPhaseEnergyCLEAR,
       "pduBreakerCurrentCLEAR": pduBreakerCurrentCLEAR,
       "pduBreakerCurrentMaxCLEAR": pduBreakerCurrentMaxCLEAR,
       "pduBreakerCurrentMinCLEAR": pduBreakerCurrentMinCLEAR,
       "pduBreakerCurrentPeakCLEAR": pduBreakerCurrentPeakCLEAR,
       "pduLineCurrentCLEAR": pduLineCurrentCLEAR,
       "pduLineCurrentMaxCLEAR": pduLineCurrentMaxCLEAR,
       "pduLineCurrentMinCLEAR": pduLineCurrentMinCLEAR,
       "pduLineCurrentPeakCLEAR": pduLineCurrentPeakCLEAR,
       "tempSensorAvailCLEAR": tempSensorAvailCLEAR,
       "tempSensorTempCLEAR": tempSensorTempCLEAR,
       "airFlowSensorAvailCLEAR": airFlowSensorAvailCLEAR,
       "airFlowSensorTempCLEAR": airFlowSensorTempCLEAR,
       "airFlowSensorFlowCLEAR": airFlowSensorFlowCLEAR,
       "airFlowSensorHumidityCLEAR": airFlowSensorHumidityCLEAR,
       "airFlowSensorDewPointCLEAR": airFlowSensorDewPointCLEAR,
       "dewPointSensorAvailCLEAR": dewPointSensorAvailCLEAR,
       "dewPointSensorTempCLEAR": dewPointSensorTempCLEAR,
       "dewPointSensorHumidityCLEAR": dewPointSensorHumidityCLEAR,
       "dewPointSensorDewPointCLEAR": dewPointSensorDewPointCLEAR,
       "ccatSensorAvailCLEAR": ccatSensorAvailCLEAR,
       "ccatSensorValueCLEAR": ccatSensorValueCLEAR,
       "t3hdSensorAvailCLEAR": t3hdSensorAvailCLEAR,
       "t3hdSensorIntTempCLEAR": t3hdSensorIntTempCLEAR,
       "t3hdSensorIntHumidityCLEAR": t3hdSensorIntHumidityCLEAR,
       "t3hdSensorIntDewPointCLEAR": t3hdSensorIntDewPointCLEAR,
       "t3hdSensorExtATempCLEAR": t3hdSensorExtATempCLEAR,
       "t3hdSensorExtBTempCLEAR": t3hdSensorExtBTempCLEAR,
       "thdSensorAvailCLEAR": thdSensorAvailCLEAR,
       "thdSensorTempCLEAR": thdSensorTempCLEAR,
       "thdSensorHumidityCLEAR": thdSensorHumidityCLEAR,
       "thdSensorDewPointCLEAR": thdSensorDewPointCLEAR,
       "rpmSensorAvailCLEAR": rpmSensorAvailCLEAR,
       "rpmSensorEnergyCLEAR": rpmSensorEnergyCLEAR,
       "rpmSensorVoltageCLEAR": rpmSensorVoltageCLEAR,
       "rpmSensorVoltageMaxCLEAR": rpmSensorVoltageMaxCLEAR,
       "rpmSensorVoltageMinCLEAR": rpmSensorVoltageMinCLEAR,
       "rpmSensorVoltagePeakCLEAR": rpmSensorVoltagePeakCLEAR,
       "rpmSensorCurrentCLEAR": rpmSensorCurrentCLEAR,
       "rpmSensorRealPowerCLEAR": rpmSensorRealPowerCLEAR,
       "rpmSensorApparentPowerCLEAR": rpmSensorApparentPowerCLEAR,
       "rpmSensorPowerFactorCLEAR": rpmSensorPowerFactorCLEAR,
       "a2dSensorAvailCLEAR": a2dSensorAvailCLEAR,
       "a2dSensorValueCLEAR": a2dSensorValueCLEAR}
)
