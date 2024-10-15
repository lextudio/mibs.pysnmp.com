# SNMP MIB module (DELL-SNMP-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-SNMP-UPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:03 2024
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Upsdell_ObjectIdentity = ObjectIdentity
upsdell = _Upsdell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2)
)
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 100)
)
_ProductIDDisplayName_Type = DisplayString
_ProductIDDisplayName_Object = MibScalar
productIDDisplayName = _ProductIDDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 100, 1),
    _ProductIDDisplayName_Type()
)
productIDDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDDisplayName.setStatus("mandatory")


class _ProductIDDescription_Type(DisplayString):
    """Custom type productIDDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductIDDescription_Type.__name__ = "DisplayString"
_ProductIDDescription_Object = MibScalar
productIDDescription = _ProductIDDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 100, 2),
    _ProductIDDescription_Type()
)
productIDDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDDescription.setStatus("mandatory")


class _ProductIDVendor_Type(DisplayString):
    """Custom type productIDVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductIDVendor_Type.__name__ = "DisplayString"
_ProductIDVendor_Object = MibScalar
productIDVendor = _ProductIDVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 100, 3),
    _ProductIDVendor_Type()
)
productIDVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDVendor.setStatus("mandatory")


class _ProductIDVersion_Type(DisplayString):
    """Custom type productIDVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductIDVersion_Type.__name__ = "DisplayString"
_ProductIDVersion_Object = MibScalar
productIDVersion = _ProductIDVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 100, 4),
    _ProductIDVersion_Type()
)
productIDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDVersion.setStatus("mandatory")


class _ProductIDBuildNumber_Type(DisplayString):
    """Custom type productIDBuildNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductIDBuildNumber_Type.__name__ = "DisplayString"
_ProductIDBuildNumber_Object = MibScalar
productIDBuildNumber = _ProductIDBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 100, 5),
    _ProductIDBuildNumber_Type()
)
productIDBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDBuildNumber.setStatus("mandatory")


class _ProductIDURL_Type(DisplayString):
    """Custom type productIDURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductIDURL_Type.__name__ = "DisplayString"
_ProductIDURL_Object = MibScalar
productIDURL = _ProductIDURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 100, 6),
    _ProductIDURL_Type()
)
productIDURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDURL.setStatus("mandatory")


class _ProductIDDeviceNetworkName_Type(DisplayString):
    """Custom type productIDDeviceNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductIDDeviceNetworkName_Type.__name__ = "DisplayString"
_ProductIDDeviceNetworkName_Object = MibScalar
productIDDeviceNetworkName = _ProductIDDeviceNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 100, 7),
    _ProductIDDeviceNetworkName_Type()
)
productIDDeviceNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIDDeviceNetworkName.setStatus("mandatory")
_ProductStatus_ObjectIdentity = ObjectIdentity
productStatus = _ProductStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 110)
)


class _ProductStatusGlobalStatus_Type(Integer32):
    """Custom type productStatusGlobalStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-critical", 4),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ProductStatusGlobalStatus_Type.__name__ = "Integer32"
_ProductStatusGlobalStatus_Object = MibScalar
productStatusGlobalStatus = _ProductStatusGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 110, 1),
    _ProductStatusGlobalStatus_Type()
)
productStatusGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusGlobalStatus.setStatus("mandatory")
_ProductStatusLastGlobalStatus_Type = Integer32
_ProductStatusLastGlobalStatus_Object = MibScalar
productStatusLastGlobalStatus = _ProductStatusLastGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 110, 2),
    _ProductStatusLastGlobalStatus_Type()
)
productStatusLastGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusLastGlobalStatus.setStatus("mandatory")
_ProductStatusTimeStamp_Type = TimeStamp
_ProductStatusTimeStamp_Object = MibScalar
productStatusTimeStamp = _ProductStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 110, 3),
    _ProductStatusTimeStamp_Type()
)
productStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusTimeStamp.setStatus("mandatory")
_ProductStatusGetTimeOut_Type = Integer32
_ProductStatusGetTimeOut_Object = MibScalar
productStatusGetTimeOut = _ProductStatusGetTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 110, 4),
    _ProductStatusGetTimeOut_Type()
)
productStatusGetTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusGetTimeOut.setStatus("optional")
_ProductStatusRefreshRate_Type = Integer32
_ProductStatusRefreshRate_Object = MibScalar
productStatusRefreshRate = _ProductStatusRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 110, 5),
    _ProductStatusRefreshRate_Type()
)
productStatusRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusRefreshRate.setStatus("optional")


class _ProductStatusGeneratingTrapFlag_Type(Integer32):
    """Custom type productStatusGeneratingTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("false", 2),
          ("true", 1))
    )


_ProductStatusGeneratingTrapFlag_Type.__name__ = "Integer32"
_ProductStatusGeneratingTrapFlag_Object = MibScalar
productStatusGeneratingTrapFlag = _ProductStatusGeneratingTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 110, 6),
    _ProductStatusGeneratingTrapFlag_Type()
)
productStatusGeneratingTrapFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productStatusGeneratingTrapFlag.setStatus("optional")
_Physical_ObjectIdentity = ObjectIdentity
physical = _Physical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120)
)
_PhysicalIdent_ObjectIdentity = ObjectIdentity
physicalIdent = _PhysicalIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 1)
)


class _PhysicalIdentFamilyName_Type(DisplayString):
    """Custom type physicalIdentFamilyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PhysicalIdentFamilyName_Type.__name__ = "DisplayString"
_PhysicalIdentFamilyName_Object = MibScalar
physicalIdentFamilyName = _PhysicalIdentFamilyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 1, 1),
    _PhysicalIdentFamilyName_Type()
)
physicalIdentFamilyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalIdentFamilyName.setStatus("mandatory")


class _PhysicalIdentSerialNumber_Type(DisplayString):
    """Custom type physicalIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PhysicalIdentSerialNumber_Type.__name__ = "DisplayString"
_PhysicalIdentSerialNumber_Object = MibScalar
physicalIdentSerialNumber = _PhysicalIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 1, 2),
    _PhysicalIdentSerialNumber_Type()
)
physicalIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalIdentSerialNumber.setStatus("mandatory")


class _PhysicalIdentConverterType_Type(Integer32):
    """Custom type physicalIdentConverterType based on Integer32"""
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
        *(("lineInteractive", 1),
          ("onLine", 2),
          ("onLineHotStandbyRedundancy", 5),
          ("onLineParallelWithNS", 4),
          ("onLineUnitaryParallel", 3))
    )


_PhysicalIdentConverterType_Type.__name__ = "Integer32"
_PhysicalIdentConverterType_Object = MibScalar
physicalIdentConverterType = _PhysicalIdentConverterType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 1, 3),
    _PhysicalIdentConverterType_Type()
)
physicalIdentConverterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalIdentConverterType.setStatus("mandatory")


class _PhysicalIdentReferenceNumber_Type(DisplayString):
    """Custom type physicalIdentReferenceNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PhysicalIdentReferenceNumber_Type.__name__ = "DisplayString"
_PhysicalIdentReferenceNumber_Object = MibScalar
physicalIdentReferenceNumber = _PhysicalIdentReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 1, 4),
    _PhysicalIdentReferenceNumber_Type()
)
physicalIdentReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalIdentReferenceNumber.setStatus("mandatory")
_PhysicalOutput_ObjectIdentity = ObjectIdentity
physicalOutput = _PhysicalOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 2)
)
_PhysicalOutputInstantHeadroom_Type = Integer32
_PhysicalOutputInstantHeadroom_Object = MibScalar
physicalOutputInstantHeadroom = _PhysicalOutputInstantHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 2, 1),
    _PhysicalOutputInstantHeadroom_Type()
)
physicalOutputInstantHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalOutputInstantHeadroom.setStatus("mandatory")
_PhysicalOutputPeakHeadroom_Type = Integer32
_PhysicalOutputPeakHeadroom_Object = MibScalar
physicalOutputPeakHeadroom = _PhysicalOutputPeakHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 2, 2),
    _PhysicalOutputPeakHeadroom_Type()
)
physicalOutputPeakHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalOutputPeakHeadroom.setStatus("mandatory")
_PhysicalOutputPeakHeadroomTimestamp_Type = TimeStamp
_PhysicalOutputPeakHeadroomTimestamp_Object = MibScalar
physicalOutputPeakHeadroomTimestamp = _PhysicalOutputPeakHeadroomTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 2, 3),
    _PhysicalOutputPeakHeadroomTimestamp_Type()
)
physicalOutputPeakHeadroomTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalOutputPeakHeadroomTimestamp.setStatus("mandatory")
_PhysicalOutputPeakConsumption_Type = Integer32
_PhysicalOutputPeakConsumption_Object = MibScalar
physicalOutputPeakConsumption = _PhysicalOutputPeakConsumption_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 2, 4),
    _PhysicalOutputPeakConsumption_Type()
)
physicalOutputPeakConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalOutputPeakConsumption.setStatus("mandatory")
_PhysicalOutputPeakConsumptionTimestamp_Type = TimeStamp
_PhysicalOutputPeakConsumptionTimestamp_Object = MibScalar
physicalOutputPeakConsumptionTimestamp = _PhysicalOutputPeakConsumptionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 2, 5),
    _PhysicalOutputPeakConsumptionTimestamp_Type()
)
physicalOutputPeakConsumptionTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalOutputPeakConsumptionTimestamp.setStatus("mandatory")
_PhysicalOutputPresentConsumption_Type = Integer32
_PhysicalOutputPresentConsumption_Object = MibScalar
physicalOutputPresentConsumption = _PhysicalOutputPresentConsumption_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 2, 6),
    _PhysicalOutputPresentConsumption_Type()
)
physicalOutputPresentConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalOutputPresentConsumption.setStatus("mandatory")
_PhysicalOutputCumulativeConsumption_Type = Integer32
_PhysicalOutputCumulativeConsumption_Object = MibScalar
physicalOutputCumulativeConsumption = _PhysicalOutputCumulativeConsumption_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 2, 7),
    _PhysicalOutputCumulativeConsumption_Type()
)
physicalOutputCumulativeConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalOutputCumulativeConsumption.setStatus("mandatory")
_PhysicalOutputCumulativeConsumptionTimestamp_Type = TimeStamp
_PhysicalOutputCumulativeConsumptionTimestamp_Object = MibScalar
physicalOutputCumulativeConsumptionTimestamp = _PhysicalOutputCumulativeConsumptionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 2, 8),
    _PhysicalOutputCumulativeConsumptionTimestamp_Type()
)
physicalOutputCumulativeConsumptionTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalOutputCumulativeConsumptionTimestamp.setStatus("mandatory")
_PhysicalOutputVA_Type = Integer32
_PhysicalOutputVA_Object = MibScalar
physicalOutputVA = _PhysicalOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 2, 9),
    _PhysicalOutputVA_Type()
)
physicalOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalOutputVA.setStatus("mandatory")
_PhysicalRectifier_ObjectIdentity = ObjectIdentity
physicalRectifier = _PhysicalRectifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 3)
)
_PhysicalRectifierPosVoltage_Type = Integer32
_PhysicalRectifierPosVoltage_Object = MibScalar
physicalRectifierPosVoltage = _PhysicalRectifierPosVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 3, 1),
    _PhysicalRectifierPosVoltage_Type()
)
physicalRectifierPosVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalRectifierPosVoltage.setStatus("mandatory")
_PhysicalRectifierNegVoltage_Type = Integer32
_PhysicalRectifierNegVoltage_Object = MibScalar
physicalRectifierNegVoltage = _PhysicalRectifierNegVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 3, 2),
    _PhysicalRectifierNegVoltage_Type()
)
physicalRectifierNegVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalRectifierNegVoltage.setStatus("mandatory")
_PhysicalUPS_ObjectIdentity = ObjectIdentity
physicalUPS = _PhysicalUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 4)
)
_PhysicalUPSDateTime_Type = TimeStamp
_PhysicalUPSDateTime_Object = MibScalar
physicalUPSDateTime = _PhysicalUPSDateTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 4, 1),
    _PhysicalUPSDateTime_Type()
)
physicalUPSDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalUPSDateTime.setStatus("mandatory")
_PhysicalUPSAlarmsStatus_Type = DisplayString
_PhysicalUPSAlarmsStatus_Object = MibScalar
physicalUPSAlarmsStatus = _PhysicalUPSAlarmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 4, 2),
    _PhysicalUPSAlarmsStatus_Type()
)
physicalUPSAlarmsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalUPSAlarmsStatus.setStatus("mandatory")
_PhysicalUPSRuntimeToShutdown_Type = Integer32
_PhysicalUPSRuntimeToShutdown_Object = MibScalar
physicalUPSRuntimeToShutdown = _PhysicalUPSRuntimeToShutdown_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 4, 3),
    _PhysicalUPSRuntimeToShutdown_Type()
)
physicalUPSRuntimeToShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalUPSRuntimeToShutdown.setStatus("mandatory")


class _PhysicalUPSOutpoutSwitchable_Type(Integer32):
    """Custom type physicalUPSOutpoutSwitchable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSwitchable", 2),
          ("switchable", 1))
    )


_PhysicalUPSOutpoutSwitchable_Type.__name__ = "Integer32"
_PhysicalUPSOutpoutSwitchable_Object = MibScalar
physicalUPSOutpoutSwitchable = _PhysicalUPSOutpoutSwitchable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 4, 4),
    _PhysicalUPSOutpoutSwitchable_Type()
)
physicalUPSOutpoutSwitchable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalUPSOutpoutSwitchable.setStatus("mandatory")
_PhysicalBattery_ObjectIdentity = ObjectIdentity
physicalBattery = _PhysicalBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 5)
)


class _PhysicalBatteryABMStatus_Type(Integer32):
    """Custom type physicalBatteryABMStatus based on Integer32"""
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
        *(("abmCharging", 1),
          ("abmDischarging", 2),
          ("abmFloating", 3),
          ("abmOff", 5),
          ("abmResting", 4))
    )


_PhysicalBatteryABMStatus_Type.__name__ = "Integer32"
_PhysicalBatteryABMStatus_Object = MibScalar
physicalBatteryABMStatus = _PhysicalBatteryABMStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 5, 1),
    _PhysicalBatteryABMStatus_Type()
)
physicalBatteryABMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalBatteryABMStatus.setStatus("mandatory")


class _PhysicalBatteryTestStatus_Type(Integer32):
    """Custom type physicalBatteryTestStatus based on Integer32"""
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
        *(("aborted", 4),
          ("doneError", 3),
          ("donePassed", 1),
          ("doneWarning", 2),
          ("inProgress", 5),
          ("noTestIniated", 6),
          ("testScheduled", 7))
    )


_PhysicalBatteryTestStatus_Type.__name__ = "Integer32"
_PhysicalBatteryTestStatus_Object = MibScalar
physicalBatteryTestStatus = _PhysicalBatteryTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 5, 2),
    _PhysicalBatteryTestStatus_Type()
)
physicalBatteryTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalBatteryTestStatus.setStatus("mandatory")
_PhysicalBatterySecondsRemaining_Type = Integer32
_PhysicalBatterySecondsRemaining_Object = MibScalar
physicalBatterySecondsRemaining = _PhysicalBatterySecondsRemaining_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 5, 3),
    _PhysicalBatterySecondsRemaining_Type()
)
physicalBatterySecondsRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalBatterySecondsRemaining.setStatus("mandatory")
_PhysicalLoadSegment_ObjectIdentity = ObjectIdentity
physicalLoadSegment = _PhysicalLoadSegment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 6)
)
_PhysicalLoadSegment1ShutdownAfterDelay_Type = Integer32
_PhysicalLoadSegment1ShutdownAfterDelay_Object = MibScalar
physicalLoadSegment1ShutdownAfterDelay = _PhysicalLoadSegment1ShutdownAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 6, 1),
    _PhysicalLoadSegment1ShutdownAfterDelay_Type()
)
physicalLoadSegment1ShutdownAfterDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLoadSegment1ShutdownAfterDelay.setStatus("mandatory")
_PhysicalLoadSegment1StartupAfterDelay_Type = Integer32
_PhysicalLoadSegment1StartupAfterDelay_Object = MibScalar
physicalLoadSegment1StartupAfterDelay = _PhysicalLoadSegment1StartupAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 6, 2),
    _PhysicalLoadSegment1StartupAfterDelay_Type()
)
physicalLoadSegment1StartupAfterDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLoadSegment1StartupAfterDelay.setStatus("mandatory")
_PhysicalLoadSegment2ShutdownAfterDelay_Type = Integer32
_PhysicalLoadSegment2ShutdownAfterDelay_Object = MibScalar
physicalLoadSegment2ShutdownAfterDelay = _PhysicalLoadSegment2ShutdownAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 6, 3),
    _PhysicalLoadSegment2ShutdownAfterDelay_Type()
)
physicalLoadSegment2ShutdownAfterDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLoadSegment2ShutdownAfterDelay.setStatus("mandatory")
_PhysicalLoadSegment2StartupAfterDelay_Type = Integer32
_PhysicalLoadSegment2StartupAfterDelay_Object = MibScalar
physicalLoadSegment2StartupAfterDelay = _PhysicalLoadSegment2StartupAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 6, 4),
    _PhysicalLoadSegment2StartupAfterDelay_Type()
)
physicalLoadSegment2StartupAfterDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLoadSegment2StartupAfterDelay.setStatus("mandatory")
_PhysicalLoadSegment1RuntimeToShutdown_Type = Integer32
_PhysicalLoadSegment1RuntimeToShutdown_Object = MibScalar
physicalLoadSegment1RuntimeToShutdown = _PhysicalLoadSegment1RuntimeToShutdown_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 6, 5),
    _PhysicalLoadSegment1RuntimeToShutdown_Type()
)
physicalLoadSegment1RuntimeToShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLoadSegment1RuntimeToShutdown.setStatus("mandatory")
_PhysicalLoadSegment2RuntimeToShutdown_Type = Integer32
_PhysicalLoadSegment2RuntimeToShutdown_Object = MibScalar
physicalLoadSegment2RuntimeToShutdown = _PhysicalLoadSegment2RuntimeToShutdown_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 6, 6),
    _PhysicalLoadSegment2RuntimeToShutdown_Type()
)
physicalLoadSegment2RuntimeToShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalLoadSegment2RuntimeToShutdown.setStatus("mandatory")
_PhysicalEnvironment_ObjectIdentity = ObjectIdentity
physicalEnvironment = _PhysicalEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7)
)
_PhysicalEnvironmentSensorPresent_Type = Integer32
_PhysicalEnvironmentSensorPresent_Object = MibScalar
physicalEnvironmentSensorPresent = _PhysicalEnvironmentSensorPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 1),
    _PhysicalEnvironmentSensorPresent_Type()
)
physicalEnvironmentSensorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentSensorPresent.setStatus("mandatory")


class _PhysicalEnvironmentSensorName_Type(DisplayString):
    """Custom type physicalEnvironmentSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 59),
    )


_PhysicalEnvironmentSensorName_Type.__name__ = "DisplayString"
_PhysicalEnvironmentSensorName_Object = MibScalar
physicalEnvironmentSensorName = _PhysicalEnvironmentSensorName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 2),
    _PhysicalEnvironmentSensorName_Type()
)
physicalEnvironmentSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentSensorName.setStatus("mandatory")
_PhysicalEnvironmentValues_ObjectIdentity = ObjectIdentity
physicalEnvironmentValues = _PhysicalEnvironmentValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 3)
)


class _PhysicalEnvironmentValuesTemperatureUnit_Type(Integer32):
    """Custom type physicalEnvironmentValuesTemperatureUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_PhysicalEnvironmentValuesTemperatureUnit_Type.__name__ = "Integer32"
_PhysicalEnvironmentValuesTemperatureUnit_Object = MibScalar
physicalEnvironmentValuesTemperatureUnit = _PhysicalEnvironmentValuesTemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 3, 1),
    _PhysicalEnvironmentValuesTemperatureUnit_Type()
)
physicalEnvironmentValuesTemperatureUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentValuesTemperatureUnit.setStatus("mandatory")
_PhysicalEnvironmentValuesTemperature_Type = Integer32
_PhysicalEnvironmentValuesTemperature_Object = MibScalar
physicalEnvironmentValuesTemperature = _PhysicalEnvironmentValuesTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 3, 2),
    _PhysicalEnvironmentValuesTemperature_Type()
)
physicalEnvironmentValuesTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentValuesTemperature.setStatus("mandatory")
_PhysicalEnvironmentValuesHumidity_Type = Integer32
_PhysicalEnvironmentValuesHumidity_Object = MibScalar
physicalEnvironmentValuesHumidity = _PhysicalEnvironmentValuesHumidity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 3, 3),
    _PhysicalEnvironmentValuesHumidity_Type()
)
physicalEnvironmentValuesHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentValuesHumidity.setStatus("mandatory")
_PhysicalEnvironmentValuesTemperatureLow_Type = Integer32
_PhysicalEnvironmentValuesTemperatureLow_Object = MibScalar
physicalEnvironmentValuesTemperatureLow = _PhysicalEnvironmentValuesTemperatureLow_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 3, 4),
    _PhysicalEnvironmentValuesTemperatureLow_Type()
)
physicalEnvironmentValuesTemperatureLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentValuesTemperatureLow.setStatus("mandatory")
_PhysicalEnvironmentValuesTemperatureHigh_Type = Integer32
_PhysicalEnvironmentValuesTemperatureHigh_Object = MibScalar
physicalEnvironmentValuesTemperatureHigh = _PhysicalEnvironmentValuesTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 3, 5),
    _PhysicalEnvironmentValuesTemperatureHigh_Type()
)
physicalEnvironmentValuesTemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentValuesTemperatureHigh.setStatus("mandatory")
_PhysicalEnvironmentValuesTemperatureHysteresis_Type = Integer32
_PhysicalEnvironmentValuesTemperatureHysteresis_Object = MibScalar
physicalEnvironmentValuesTemperatureHysteresis = _PhysicalEnvironmentValuesTemperatureHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 3, 6),
    _PhysicalEnvironmentValuesTemperatureHysteresis_Type()
)
physicalEnvironmentValuesTemperatureHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentValuesTemperatureHysteresis.setStatus("mandatory")
_PhysicalEnvironmentValueshHumidityLow_Type = Integer32
_PhysicalEnvironmentValueshHumidityLow_Object = MibScalar
physicalEnvironmentValueshHumidityLow = _PhysicalEnvironmentValueshHumidityLow_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 3, 7),
    _PhysicalEnvironmentValueshHumidityLow_Type()
)
physicalEnvironmentValueshHumidityLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentValueshHumidityLow.setStatus("mandatory")
_PhysicalEnvironmentValuesHumidityHigh_Type = Integer32
_PhysicalEnvironmentValuesHumidityHigh_Object = MibScalar
physicalEnvironmentValuesHumidityHigh = _PhysicalEnvironmentValuesHumidityHigh_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 3, 8),
    _PhysicalEnvironmentValuesHumidityHigh_Type()
)
physicalEnvironmentValuesHumidityHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentValuesHumidityHigh.setStatus("mandatory")
_PhysicalEnvironmentValuesHumidityHysteresis_Type = Integer32
_PhysicalEnvironmentValuesHumidityHysteresis_Object = MibScalar
physicalEnvironmentValuesHumidityHysteresis = _PhysicalEnvironmentValuesHumidityHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 3, 9),
    _PhysicalEnvironmentValuesHumidityHysteresis_Type()
)
physicalEnvironmentValuesHumidityHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentValuesHumidityHysteresis.setStatus("mandatory")
_PhysicalEnvironmentInputTable_Object = MibTable
physicalEnvironmentInputTable = _PhysicalEnvironmentInputTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 4)
)
if mibBuilder.loadTexts:
    physicalEnvironmentInputTable.setStatus("mandatory")
_PhysicalEnvironmentInputEntry_Object = MibTableRow
physicalEnvironmentInputEntry = _PhysicalEnvironmentInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 4, 1)
)
physicalEnvironmentInputEntry.setIndexNames(
    (0, "DELL-SNMP-UPS-MIB", "physicalEnvironmentInputIndex"),
)
if mibBuilder.loadTexts:
    physicalEnvironmentInputEntry.setStatus("mandatory")


class _PhysicalEnvironmentInputIndex_Type(Integer32):
    """Custom type physicalEnvironmentInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PhysicalEnvironmentInputIndex_Type.__name__ = "Integer32"
_PhysicalEnvironmentInputIndex_Object = MibTableColumn
physicalEnvironmentInputIndex = _PhysicalEnvironmentInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 4, 1, 1),
    _PhysicalEnvironmentInputIndex_Type()
)
physicalEnvironmentInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentInputIndex.setStatus("mandatory")


class _PhysicalEnvironmentInputName_Type(DisplayString):
    """Custom type physicalEnvironmentInputName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_PhysicalEnvironmentInputName_Type.__name__ = "DisplayString"
_PhysicalEnvironmentInputName_Object = MibTableColumn
physicalEnvironmentInputName = _PhysicalEnvironmentInputName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 4, 1, 2),
    _PhysicalEnvironmentInputName_Type()
)
physicalEnvironmentInputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentInputName.setStatus("mandatory")


class _PhysicalEnvironmentInputState_Type(Integer32):
    """Custom type physicalEnvironmentInputState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("opened", 1))
    )


_PhysicalEnvironmentInputState_Type.__name__ = "Integer32"
_PhysicalEnvironmentInputState_Object = MibTableColumn
physicalEnvironmentInputState = _PhysicalEnvironmentInputState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 4, 1, 3),
    _PhysicalEnvironmentInputState_Type()
)
physicalEnvironmentInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentInputState.setStatus("mandatory")


class _PhysicalEnvironmentInputOpenedState_Type(DisplayString):
    """Custom type physicalEnvironmentInputOpenedState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_PhysicalEnvironmentInputOpenedState_Type.__name__ = "DisplayString"
_PhysicalEnvironmentInputOpenedState_Object = MibTableColumn
physicalEnvironmentInputOpenedState = _PhysicalEnvironmentInputOpenedState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 4, 1, 4),
    _PhysicalEnvironmentInputOpenedState_Type()
)
physicalEnvironmentInputOpenedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentInputOpenedState.setStatus("mandatory")


class _PhysicalEnvironmentInputClosedState_Type(DisplayString):
    """Custom type physicalEnvironmentInputClosedState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_PhysicalEnvironmentInputClosedState_Type.__name__ = "DisplayString"
_PhysicalEnvironmentInputClosedState_Object = MibTableColumn
physicalEnvironmentInputClosedState = _PhysicalEnvironmentInputClosedState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 120, 7, 4, 1, 5),
    _PhysicalEnvironmentInputClosedState_Type()
)
physicalEnvironmentInputClosedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalEnvironmentInputClosedState.setStatus("mandatory")
_Logical_ObjectIdentity = ObjectIdentity
logical = _Logical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 130)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140)
)

# Managed Objects groups


# Notification objects

trapInverterOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 1)
)
if mibBuilder.loadTexts:
    trapInverterOverVoltage.setStatus(
        ""
    )

trapInverterOverVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 2)
)
if mibBuilder.loadTexts:
    trapInverterOverVoltageOk.setStatus(
        ""
    )

trapInverterUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 3)
)
if mibBuilder.loadTexts:
    trapInverterUnderVoltage.setStatus(
        ""
    )

trapInverterUnderVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 4)
)
if mibBuilder.loadTexts:
    trapInverterUnderVoltageOk.setStatus(
        ""
    )

trapBypassFrequencyOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 5)
)
if mibBuilder.loadTexts:
    trapBypassFrequencyOutOfRange.setStatus(
        ""
    )

trapBypassFrequencyOutOfRangeOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 6)
)
if mibBuilder.loadTexts:
    trapBypassFrequencyOutOfRangeOk.setStatus(
        ""
    )

trapOnBuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 7)
)
if mibBuilder.loadTexts:
    trapOnBuck.setStatus(
        ""
    )

trapReturnFromBuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 8)
)
if mibBuilder.loadTexts:
    trapReturnFromBuck.setStatus(
        ""
    )

trapOnBoost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 9)
)
if mibBuilder.loadTexts:
    trapOnBoost.setStatus(
        ""
    )

trapReturnFromBoost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 10)
)
if mibBuilder.loadTexts:
    trapReturnFromBoost.setStatus(
        ""
    )

trapInputOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 11)
)
if mibBuilder.loadTexts:
    trapInputOverVoltage.setStatus(
        ""
    )

trapInputOverVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 12)
)
if mibBuilder.loadTexts:
    trapInputOverVoltageOk.setStatus(
        ""
    )

trapInputUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 13)
)
if mibBuilder.loadTexts:
    trapInputUnderVoltage.setStatus(
        ""
    )

trapInputUnderVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 14)
)
if mibBuilder.loadTexts:
    trapInputUnderVoltageOk.setStatus(
        ""
    )

trapInputFrequencyOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 15)
)
if mibBuilder.loadTexts:
    trapInputFrequencyOutOfRange.setStatus(
        ""
    )

trapInputFrequencyOutOfRangeOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 16)
)
if mibBuilder.loadTexts:
    trapInputFrequencyOutOfRangeOk.setStatus(
        ""
    )

trapRemoteEmergencyPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 17)
)
if mibBuilder.loadTexts:
    trapRemoteEmergencyPowerOff.setStatus(
        ""
    )

trapReturnFromEmergencyPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 18)
)
if mibBuilder.loadTexts:
    trapReturnFromEmergencyPowerOff.setStatus(
        ""
    )

trapLevel1Overload = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 19)
)
if mibBuilder.loadTexts:
    trapLevel1Overload.setStatus(
        ""
    )

trapLevel1OverloadOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 20)
)
if mibBuilder.loadTexts:
    trapLevel1OverloadOk.setStatus(
        ""
    )

trapLevel2Overload = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 21)
)
if mibBuilder.loadTexts:
    trapLevel2Overload.setStatus(
        ""
    )

trapLevel2OverloadOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 22)
)
if mibBuilder.loadTexts:
    trapLevel2OverloadOk.setStatus(
        ""
    )

trapLevel3Overload = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 23)
)
if mibBuilder.loadTexts:
    trapLevel3Overload.setStatus(
        ""
    )

trapLevel3OverloadOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 24)
)
if mibBuilder.loadTexts:
    trapLevel3OverloadOk.setStatus(
        ""
    )

trapPosDCLinkOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 25)
)
if mibBuilder.loadTexts:
    trapPosDCLinkOverVoltage.setStatus(
        ""
    )

trapPosDCLinkOverVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 26)
)
if mibBuilder.loadTexts:
    trapPosDCLinkOverVoltageOk.setStatus(
        ""
    )

trapPosDCLinkUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 27)
)
if mibBuilder.loadTexts:
    trapPosDCLinkUnderVoltage.setStatus(
        ""
    )

trapPosDCLinkUnderVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 28)
)
if mibBuilder.loadTexts:
    trapPosDCLinkUnderVoltageOk.setStatus(
        ""
    )

trapNegDCLinkOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 29)
)
if mibBuilder.loadTexts:
    trapNegDCLinkOverVoltage.setStatus(
        ""
    )

trapNegDCLinkOverVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 30)
)
if mibBuilder.loadTexts:
    trapNegDCLinkOverVoltageOk.setStatus(
        ""
    )

trapNegDCLinkUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 31)
)
if mibBuilder.loadTexts:
    trapNegDCLinkUnderVoltage.setStatus(
        ""
    )

trapNegDCLinkUnderVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 32)
)
if mibBuilder.loadTexts:
    trapNegDCLinkUnderVoltageOk.setStatus(
        ""
    )

trapRectifierFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 33)
)
if mibBuilder.loadTexts:
    trapRectifierFault.setStatus(
        ""
    )

trapRectifierOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 34)
)
if mibBuilder.loadTexts:
    trapRectifierOk.setStatus(
        ""
    )

trapInverterFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 35)
)
if mibBuilder.loadTexts:
    trapInverterFault.setStatus(
        ""
    )

trapInverterOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 36)
)
if mibBuilder.loadTexts:
    trapInverterOk.setStatus(
        ""
    )

trapChargerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 37)
)
if mibBuilder.loadTexts:
    trapChargerFailure.setStatus(
        ""
    )

trapChargerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 38)
)
if mibBuilder.loadTexts:
    trapChargerOk.setStatus(
        ""
    )

trapEepromFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 39)
)
if mibBuilder.loadTexts:
    trapEepromFailure.setStatus(
        ""
    )

trapEepromOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 40)
)
if mibBuilder.loadTexts:
    trapEepromOk.setStatus(
        ""
    )

trapShutdownImminent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 41)
)
if mibBuilder.loadTexts:
    trapShutdownImminent.setStatus(
        ""
    )

trapShutdownImminentOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 42)
)
if mibBuilder.loadTexts:
    trapShutdownImminentOver.setStatus(
        ""
    )

trapBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 43)
)
if mibBuilder.loadTexts:
    trapBatteryLow.setStatus(
        ""
    )

trapBatteryOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 44)
)
if mibBuilder.loadTexts:
    trapBatteryOk.setStatus(
        ""
    )

trapOutputShortCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 45)
)
if mibBuilder.loadTexts:
    trapOutputShortCircuit.setStatus(
        ""
    )

trapOutputReturnFromShortCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 46)
)
if mibBuilder.loadTexts:
    trapOutputReturnFromShortCircuit.setStatus(
        ""
    )

trapUtilityNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 47)
)
if mibBuilder.loadTexts:
    trapUtilityNotPresent.setStatus(
        ""
    )

trapUtilityPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 48)
)
if mibBuilder.loadTexts:
    trapUtilityPresent.setStatus(
        ""
    )

trapBatteryOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 49)
)
if mibBuilder.loadTexts:
    trapBatteryOverVoltage.setStatus(
        ""
    )

trapBatteryOverVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 50)
)
if mibBuilder.loadTexts:
    trapBatteryOverVoltageOk.setStatus(
        ""
    )

trapHeatsinkOvertemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 51)
)
if mibBuilder.loadTexts:
    trapHeatsinkOvertemperature.setStatus(
        ""
    )

trapHeatsinkOvertemperatureOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 52)
)
if mibBuilder.loadTexts:
    trapHeatsinkOvertemperatureOk.setStatus(
        ""
    )

trapBypassNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 53)
)
if mibBuilder.loadTexts:
    trapBypassNotAvailable.setStatus(
        ""
    )

trapBypassNotAvailableOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 54)
)
if mibBuilder.loadTexts:
    trapBypassNotAvailableOk.setStatus(
        ""
    )

trapOnManualBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 55)
)
if mibBuilder.loadTexts:
    trapOnManualBypass.setStatus(
        ""
    )

trapUPSOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 57)
)
if mibBuilder.loadTexts:
    trapUPSOnBattery.setStatus(
        ""
    )

trapUPSReturnFromBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 58)
)
if mibBuilder.loadTexts:
    trapUPSReturnFromBattery.setStatus(
        ""
    )

trapUPSOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 59)
)
if mibBuilder.loadTexts:
    trapUPSOnBypass.setStatus(
        ""
    )

trapUPSReturnFromBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 60)
)
if mibBuilder.loadTexts:
    trapUPSReturnFromBypass.setStatus(
        ""
    )

trapBatteryTestInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 61)
)
if mibBuilder.loadTexts:
    trapBatteryTestInProgress.setStatus(
        ""
    )

trapBatteryTestDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 62)
)
trapBatteryTestDone.setObjects(
    ("DELL-SNMP-UPS-MIB", "physicalBatteryTestStatus")
)
if mibBuilder.loadTexts:
    trapBatteryTestDone.setStatus(
        ""
    )

trapBatteryNeedReplacement = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 63)
)
if mibBuilder.loadTexts:
    trapBatteryNeedReplacement.setStatus(
        ""
    )

trapBatteryReplacementDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 64)
)
if mibBuilder.loadTexts:
    trapBatteryReplacementDone.setStatus(
        ""
    )

trapFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 65)
)
if mibBuilder.loadTexts:
    trapFanFailure.setStatus(
        ""
    )

trapFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 66)
)
if mibBuilder.loadTexts:
    trapFanOk.setStatus(
        ""
    )

trapSiteWiringFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 67)
)
if mibBuilder.loadTexts:
    trapSiteWiringFault.setStatus(
        ""
    )

trapSiteWiringOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 68)
)
if mibBuilder.loadTexts:
    trapSiteWiringOk.setStatus(
        ""
    )

trapBatteryDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 69)
)
if mibBuilder.loadTexts:
    trapBatteryDisconnected.setStatus(
        ""
    )

trapBatteryConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 70)
)
if mibBuilder.loadTexts:
    trapBatteryConnected.setStatus(
        ""
    )

trapUPSOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 71)
)
if mibBuilder.loadTexts:
    trapUPSOff.setStatus(
        ""
    )

trapUPSOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 72)
)
if mibBuilder.loadTexts:
    trapUPSOn.setStatus(
        ""
    )

trapDCLinkImbalance = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 73)
)
if mibBuilder.loadTexts:
    trapDCLinkImbalance.setStatus(
        ""
    )

trapDCLinkImbalanceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 74)
)
if mibBuilder.loadTexts:
    trapDCLinkImbalanceOk.setStatus(
        ""
    )

trapABMOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 79)
)
trapABMOn.setObjects(
    ("DELL-SNMP-UPS-MIB", "physicalBatteryABMStatus")
)
if mibBuilder.loadTexts:
    trapABMOn.setStatus(
        ""
    )

trapABMOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 80)
)
if mibBuilder.loadTexts:
    trapABMOff.setStatus(
        ""
    )

trapLoadSegment1Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 81)
)
if mibBuilder.loadTexts:
    trapLoadSegment1Off.setStatus(
        ""
    )

trapLoadSegment1On = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 82)
)
if mibBuilder.loadTexts:
    trapLoadSegment1On.setStatus(
        ""
    )

trapLoadSegment2Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 83)
)
if mibBuilder.loadTexts:
    trapLoadSegment2Off.setStatus(
        ""
    )

trapLoadSegment2On = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 84)
)
if mibBuilder.loadTexts:
    trapLoadSegment2On.setStatus(
        ""
    )

trapInHighEfficiencyMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 85)
)
if mibBuilder.loadTexts:
    trapInHighEfficiencyMode.setStatus(
        ""
    )

trapReturnFromHighEfficiencyMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 86)
)
if mibBuilder.loadTexts:
    trapReturnFromHighEfficiencyMode.setStatus(
        ""
    )

trapRectifierOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 87)
)
if mibBuilder.loadTexts:
    trapRectifierOverload.setStatus(
        ""
    )

trapRectifierOverloadOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 88)
)
if mibBuilder.loadTexts:
    trapRectifierOverloadOk.setStatus(
        ""
    )

trapInverterOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 89)
)
if mibBuilder.loadTexts:
    trapInverterOverload.setStatus(
        ""
    )

trapInverterOverloadOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 90)
)
if mibBuilder.loadTexts:
    trapInverterOverloadOk.setStatus(
        ""
    )

trapBypassVoltageOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 91)
)
if mibBuilder.loadTexts:
    trapBypassVoltageOutOfRange.setStatus(
        ""
    )

trapBypassVoltageOutOfRangeOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 92)
)
if mibBuilder.loadTexts:
    trapBypassVoltageOutOfRangeOk.setStatus(
        ""
    )

trapServiceBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 93)
)
if mibBuilder.loadTexts:
    trapServiceBattery.setStatus(
        ""
    )

trapToBypassCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 94)
)
if mibBuilder.loadTexts:
    trapToBypassCommand.setStatus(
        ""
    )

trapFromBypassCommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 95)
)
if mibBuilder.loadTexts:
    trapFromBypassCommand.setStatus(
        ""
    )

trapCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 96)
)
if mibBuilder.loadTexts:
    trapCommunicationLost.setStatus(
        ""
    )

trapCommunicationRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 97)
)
if mibBuilder.loadTexts:
    trapCommunicationRestored.setStatus(
        ""
    )

trapEnvironComFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 98)
)
if mibBuilder.loadTexts:
    trapEnvironComFailure.setStatus(
        ""
    )

trapEnvironComOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 99)
)
if mibBuilder.loadTexts:
    trapEnvironComOK.setStatus(
        ""
    )

trapEnvironTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 100)
)
if mibBuilder.loadTexts:
    trapEnvironTemperatureLow.setStatus(
        ""
    )

trapEnvironTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 102)
)
if mibBuilder.loadTexts:
    trapEnvironTemperatureHigh.setStatus(
        ""
    )

trapEnvironTemperatureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 103)
)
if mibBuilder.loadTexts:
    trapEnvironTemperatureOK.setStatus(
        ""
    )

trapEnvironHumidityLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 104)
)
if mibBuilder.loadTexts:
    trapEnvironHumidityLow.setStatus(
        ""
    )

trapEnvironHumidityHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 106)
)
if mibBuilder.loadTexts:
    trapEnvironHumidityHigh.setStatus(
        ""
    )

trapEnvironHumidityOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 107)
)
if mibBuilder.loadTexts:
    trapEnvironHumidityOK.setStatus(
        ""
    )

trapEnvironInput1Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 108)
)
if mibBuilder.loadTexts:
    trapEnvironInput1Closed.setStatus(
        ""
    )

trapEnvironInput1Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 109)
)
if mibBuilder.loadTexts:
    trapEnvironInput1Open.setStatus(
        ""
    )

trapEnvironInput2Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 110)
)
if mibBuilder.loadTexts:
    trapEnvironInput2Closed.setStatus(
        ""
    )

trapEnvironInput2Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10902, 2, 140, 0, 111)
)
if mibBuilder.loadTexts:
    trapEnvironInput2Open.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-SNMP-UPS-MIB",
    **{"dell": dell,
       "upsdell": upsdell,
       "hardware": hardware,
       "productID": productID,
       "productIDDisplayName": productIDDisplayName,
       "productIDDescription": productIDDescription,
       "productIDVendor": productIDVendor,
       "productIDVersion": productIDVersion,
       "productIDBuildNumber": productIDBuildNumber,
       "productIDURL": productIDURL,
       "productIDDeviceNetworkName": productIDDeviceNetworkName,
       "productStatus": productStatus,
       "productStatusGlobalStatus": productStatusGlobalStatus,
       "productStatusLastGlobalStatus": productStatusLastGlobalStatus,
       "productStatusTimeStamp": productStatusTimeStamp,
       "productStatusGetTimeOut": productStatusGetTimeOut,
       "productStatusRefreshRate": productStatusRefreshRate,
       "productStatusGeneratingTrapFlag": productStatusGeneratingTrapFlag,
       "physical": physical,
       "physicalIdent": physicalIdent,
       "physicalIdentFamilyName": physicalIdentFamilyName,
       "physicalIdentSerialNumber": physicalIdentSerialNumber,
       "physicalIdentConverterType": physicalIdentConverterType,
       "physicalIdentReferenceNumber": physicalIdentReferenceNumber,
       "physicalOutput": physicalOutput,
       "physicalOutputInstantHeadroom": physicalOutputInstantHeadroom,
       "physicalOutputPeakHeadroom": physicalOutputPeakHeadroom,
       "physicalOutputPeakHeadroomTimestamp": physicalOutputPeakHeadroomTimestamp,
       "physicalOutputPeakConsumption": physicalOutputPeakConsumption,
       "physicalOutputPeakConsumptionTimestamp": physicalOutputPeakConsumptionTimestamp,
       "physicalOutputPresentConsumption": physicalOutputPresentConsumption,
       "physicalOutputCumulativeConsumption": physicalOutputCumulativeConsumption,
       "physicalOutputCumulativeConsumptionTimestamp": physicalOutputCumulativeConsumptionTimestamp,
       "physicalOutputVA": physicalOutputVA,
       "physicalRectifier": physicalRectifier,
       "physicalRectifierPosVoltage": physicalRectifierPosVoltage,
       "physicalRectifierNegVoltage": physicalRectifierNegVoltage,
       "physicalUPS": physicalUPS,
       "physicalUPSDateTime": physicalUPSDateTime,
       "physicalUPSAlarmsStatus": physicalUPSAlarmsStatus,
       "physicalUPSRuntimeToShutdown": physicalUPSRuntimeToShutdown,
       "physicalUPSOutpoutSwitchable": physicalUPSOutpoutSwitchable,
       "physicalBattery": physicalBattery,
       "physicalBatteryABMStatus": physicalBatteryABMStatus,
       "physicalBatteryTestStatus": physicalBatteryTestStatus,
       "physicalBatterySecondsRemaining": physicalBatterySecondsRemaining,
       "physicalLoadSegment": physicalLoadSegment,
       "physicalLoadSegment1ShutdownAfterDelay": physicalLoadSegment1ShutdownAfterDelay,
       "physicalLoadSegment1StartupAfterDelay": physicalLoadSegment1StartupAfterDelay,
       "physicalLoadSegment2ShutdownAfterDelay": physicalLoadSegment2ShutdownAfterDelay,
       "physicalLoadSegment2StartupAfterDelay": physicalLoadSegment2StartupAfterDelay,
       "physicalLoadSegment1RuntimeToShutdown": physicalLoadSegment1RuntimeToShutdown,
       "physicalLoadSegment2RuntimeToShutdown": physicalLoadSegment2RuntimeToShutdown,
       "physicalEnvironment": physicalEnvironment,
       "physicalEnvironmentSensorPresent": physicalEnvironmentSensorPresent,
       "physicalEnvironmentSensorName": physicalEnvironmentSensorName,
       "physicalEnvironmentValues": physicalEnvironmentValues,
       "physicalEnvironmentValuesTemperatureUnit": physicalEnvironmentValuesTemperatureUnit,
       "physicalEnvironmentValuesTemperature": physicalEnvironmentValuesTemperature,
       "physicalEnvironmentValuesHumidity": physicalEnvironmentValuesHumidity,
       "physicalEnvironmentValuesTemperatureLow": physicalEnvironmentValuesTemperatureLow,
       "physicalEnvironmentValuesTemperatureHigh": physicalEnvironmentValuesTemperatureHigh,
       "physicalEnvironmentValuesTemperatureHysteresis": physicalEnvironmentValuesTemperatureHysteresis,
       "physicalEnvironmentValueshHumidityLow": physicalEnvironmentValueshHumidityLow,
       "physicalEnvironmentValuesHumidityHigh": physicalEnvironmentValuesHumidityHigh,
       "physicalEnvironmentValuesHumidityHysteresis": physicalEnvironmentValuesHumidityHysteresis,
       "physicalEnvironmentInputTable": physicalEnvironmentInputTable,
       "physicalEnvironmentInputEntry": physicalEnvironmentInputEntry,
       "physicalEnvironmentInputIndex": physicalEnvironmentInputIndex,
       "physicalEnvironmentInputName": physicalEnvironmentInputName,
       "physicalEnvironmentInputState": physicalEnvironmentInputState,
       "physicalEnvironmentInputOpenedState": physicalEnvironmentInputOpenedState,
       "physicalEnvironmentInputClosedState": physicalEnvironmentInputClosedState,
       "logical": logical,
       "traps": traps,
       "trapInverterOverVoltage": trapInverterOverVoltage,
       "trapInverterOverVoltageOk": trapInverterOverVoltageOk,
       "trapInverterUnderVoltage": trapInverterUnderVoltage,
       "trapInverterUnderVoltageOk": trapInverterUnderVoltageOk,
       "trapBypassFrequencyOutOfRange": trapBypassFrequencyOutOfRange,
       "trapBypassFrequencyOutOfRangeOk": trapBypassFrequencyOutOfRangeOk,
       "trapOnBuck": trapOnBuck,
       "trapReturnFromBuck": trapReturnFromBuck,
       "trapOnBoost": trapOnBoost,
       "trapReturnFromBoost": trapReturnFromBoost,
       "trapInputOverVoltage": trapInputOverVoltage,
       "trapInputOverVoltageOk": trapInputOverVoltageOk,
       "trapInputUnderVoltage": trapInputUnderVoltage,
       "trapInputUnderVoltageOk": trapInputUnderVoltageOk,
       "trapInputFrequencyOutOfRange": trapInputFrequencyOutOfRange,
       "trapInputFrequencyOutOfRangeOk": trapInputFrequencyOutOfRangeOk,
       "trapRemoteEmergencyPowerOff": trapRemoteEmergencyPowerOff,
       "trapReturnFromEmergencyPowerOff": trapReturnFromEmergencyPowerOff,
       "trapLevel1Overload": trapLevel1Overload,
       "trapLevel1OverloadOk": trapLevel1OverloadOk,
       "trapLevel2Overload": trapLevel2Overload,
       "trapLevel2OverloadOk": trapLevel2OverloadOk,
       "trapLevel3Overload": trapLevel3Overload,
       "trapLevel3OverloadOk": trapLevel3OverloadOk,
       "trapPosDCLinkOverVoltage": trapPosDCLinkOverVoltage,
       "trapPosDCLinkOverVoltageOk": trapPosDCLinkOverVoltageOk,
       "trapPosDCLinkUnderVoltage": trapPosDCLinkUnderVoltage,
       "trapPosDCLinkUnderVoltageOk": trapPosDCLinkUnderVoltageOk,
       "trapNegDCLinkOverVoltage": trapNegDCLinkOverVoltage,
       "trapNegDCLinkOverVoltageOk": trapNegDCLinkOverVoltageOk,
       "trapNegDCLinkUnderVoltage": trapNegDCLinkUnderVoltage,
       "trapNegDCLinkUnderVoltageOk": trapNegDCLinkUnderVoltageOk,
       "trapRectifierFault": trapRectifierFault,
       "trapRectifierOk": trapRectifierOk,
       "trapInverterFault": trapInverterFault,
       "trapInverterOk": trapInverterOk,
       "trapChargerFailure": trapChargerFailure,
       "trapChargerOk": trapChargerOk,
       "trapEepromFailure": trapEepromFailure,
       "trapEepromOk": trapEepromOk,
       "trapShutdownImminent": trapShutdownImminent,
       "trapShutdownImminentOver": trapShutdownImminentOver,
       "trapBatteryLow": trapBatteryLow,
       "trapBatteryOk": trapBatteryOk,
       "trapOutputShortCircuit": trapOutputShortCircuit,
       "trapOutputReturnFromShortCircuit": trapOutputReturnFromShortCircuit,
       "trapUtilityNotPresent": trapUtilityNotPresent,
       "trapUtilityPresent": trapUtilityPresent,
       "trapBatteryOverVoltage": trapBatteryOverVoltage,
       "trapBatteryOverVoltageOk": trapBatteryOverVoltageOk,
       "trapHeatsinkOvertemperature": trapHeatsinkOvertemperature,
       "trapHeatsinkOvertemperatureOk": trapHeatsinkOvertemperatureOk,
       "trapBypassNotAvailable": trapBypassNotAvailable,
       "trapBypassNotAvailableOk": trapBypassNotAvailableOk,
       "trapOnManualBypass": trapOnManualBypass,
       "trapUPSOnBattery": trapUPSOnBattery,
       "trapUPSReturnFromBattery": trapUPSReturnFromBattery,
       "trapUPSOnBypass": trapUPSOnBypass,
       "trapUPSReturnFromBypass": trapUPSReturnFromBypass,
       "trapBatteryTestInProgress": trapBatteryTestInProgress,
       "trapBatteryTestDone": trapBatteryTestDone,
       "trapBatteryNeedReplacement": trapBatteryNeedReplacement,
       "trapBatteryReplacementDone": trapBatteryReplacementDone,
       "trapFanFailure": trapFanFailure,
       "trapFanOk": trapFanOk,
       "trapSiteWiringFault": trapSiteWiringFault,
       "trapSiteWiringOk": trapSiteWiringOk,
       "trapBatteryDisconnected": trapBatteryDisconnected,
       "trapBatteryConnected": trapBatteryConnected,
       "trapUPSOff": trapUPSOff,
       "trapUPSOn": trapUPSOn,
       "trapDCLinkImbalance": trapDCLinkImbalance,
       "trapDCLinkImbalanceOk": trapDCLinkImbalanceOk,
       "trapABMOn": trapABMOn,
       "trapABMOff": trapABMOff,
       "trapLoadSegment1Off": trapLoadSegment1Off,
       "trapLoadSegment1On": trapLoadSegment1On,
       "trapLoadSegment2Off": trapLoadSegment2Off,
       "trapLoadSegment2On": trapLoadSegment2On,
       "trapInHighEfficiencyMode": trapInHighEfficiencyMode,
       "trapReturnFromHighEfficiencyMode": trapReturnFromHighEfficiencyMode,
       "trapRectifierOverload": trapRectifierOverload,
       "trapRectifierOverloadOk": trapRectifierOverloadOk,
       "trapInverterOverload": trapInverterOverload,
       "trapInverterOverloadOk": trapInverterOverloadOk,
       "trapBypassVoltageOutOfRange": trapBypassVoltageOutOfRange,
       "trapBypassVoltageOutOfRangeOk": trapBypassVoltageOutOfRangeOk,
       "trapServiceBattery": trapServiceBattery,
       "trapToBypassCommand": trapToBypassCommand,
       "trapFromBypassCommand": trapFromBypassCommand,
       "trapCommunicationLost": trapCommunicationLost,
       "trapCommunicationRestored": trapCommunicationRestored,
       "trapEnvironComFailure": trapEnvironComFailure,
       "trapEnvironComOK": trapEnvironComOK,
       "trapEnvironTemperatureLow": trapEnvironTemperatureLow,
       "trapEnvironTemperatureHigh": trapEnvironTemperatureHigh,
       "trapEnvironTemperatureOK": trapEnvironTemperatureOK,
       "trapEnvironHumidityLow": trapEnvironHumidityLow,
       "trapEnvironHumidityHigh": trapEnvironHumidityHigh,
       "trapEnvironHumidityOK": trapEnvironHumidityOK,
       "trapEnvironInput1Closed": trapEnvironInput1Closed,
       "trapEnvironInput1Open": trapEnvironInput1Open,
       "trapEnvironInput2Closed": trapEnvironInput2Closed,
       "trapEnvironInput2Open": trapEnvironInput2Open}
)
