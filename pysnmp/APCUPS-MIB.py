# SNMP MIB module (APCUPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APCUPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:12 2024
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


# Types definitions



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiGauge(Gauge32):
    """Custom type DmiGauge based on Gauge32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDateX(OctetString):
    """Custom type DmiDateX based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Apc_ObjectIdentity = ObjectIdentity
apc = _Apc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 2)
)
_PowerChuteDMIAgent_ObjectIdentity = ObjectIdentity
powerChuteDMIAgent = _PowerChuteDMIAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "APCUPS-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDateX
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 1, 1, 5),
    _A1Installation_Type()
)
a1Installation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Installation.setStatus("mandatory")


class _A1Verify_Type(Integer32):
    """Custom type a1Verify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("vAnErrorOccuredCheckStatusCode", 0),
          ("vReserved", 3),
          ("vThisComponentDoesNotExist", 1),
          ("vThisComponentExistsAndIsFunctioningCorr", 7),
          ("vThisComponentExistsAndIsNotFunctioningC", 6),
          ("vThisComponentExistsButTheFunctionality1", 5),
          ("vThisComponentExistsButTheFunctionalityI", 4),
          ("vVerificationIsNotSupported", 2))
    )


_A1Verify_Type.__name__ = "Integer32"
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TUpsBattery_Object = MibTable
tUpsBattery = _TUpsBattery_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tUpsBattery.setStatus("mandatory")
_EUpsBattery_Object = MibTableRow
eUpsBattery = _EUpsBattery_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 2, 1)
)
eUpsBattery.setIndexNames(
    (0, "APCUPS-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eUpsBattery.setStatus("mandatory")


class _A2BatteryStatus_Type(Integer32):
    """Custom type a2BatteryStatus based on Integer32"""
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
        *(("vBatteryDepleted", 4),
          ("vBatteryLow", 3),
          ("vBatteryNormal", 2),
          ("vUnknown", 1))
    )


_A2BatteryStatus_Type.__name__ = "Integer32"
_A2BatteryStatus_Object = MibTableColumn
a2BatteryStatus = _A2BatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 2, 1, 1),
    _A2BatteryStatus_Type()
)
a2BatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2BatteryStatus.setStatus("mandatory")
_A2SecondsOnBattery_Type = DmiCounter
_A2SecondsOnBattery_Object = MibTableColumn
a2SecondsOnBattery = _A2SecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 2, 1, 2),
    _A2SecondsOnBattery_Type()
)
a2SecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2SecondsOnBattery.setStatus("mandatory")
_A2EstimatedMinutesRemaining_Type = DmiInteger
_A2EstimatedMinutesRemaining_Object = MibTableColumn
a2EstimatedMinutesRemaining = _A2EstimatedMinutesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 2, 1, 3),
    _A2EstimatedMinutesRemaining_Type()
)
a2EstimatedMinutesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2EstimatedMinutesRemaining.setStatus("mandatory")
_A2EstimatedChargeRemaining_Type = DmiGauge
_A2EstimatedChargeRemaining_Object = MibTableColumn
a2EstimatedChargeRemaining = _A2EstimatedChargeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 2, 1, 4),
    _A2EstimatedChargeRemaining_Type()
)
a2EstimatedChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2EstimatedChargeRemaining.setStatus("mandatory")
_A2BatteryVoltage_Type = DmiGauge
_A2BatteryVoltage_Object = MibTableColumn
a2BatteryVoltage = _A2BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 2, 1, 5),
    _A2BatteryVoltage_Type()
)
a2BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2BatteryVoltage.setStatus("mandatory")
_A2BatteryCurrent_Type = DmiGauge
_A2BatteryCurrent_Object = MibTableColumn
a2BatteryCurrent = _A2BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 2, 1, 6),
    _A2BatteryCurrent_Type()
)
a2BatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2BatteryCurrent.setStatus("mandatory")
_A2TemperatureProbeIndex_Type = DmiInteger
_A2TemperatureProbeIndex_Object = MibTableColumn
a2TemperatureProbeIndex = _A2TemperatureProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 2, 1, 7),
    _A2TemperatureProbeIndex_Type()
)
a2TemperatureProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2TemperatureProbeIndex.setStatus("mandatory")
_A2FruGroupIndex_Type = DmiInteger
_A2FruGroupIndex_Object = MibTableColumn
a2FruGroupIndex = _A2FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 2, 1, 8),
    _A2FruGroupIndex_Type()
)
a2FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2FruGroupIndex.setStatus("mandatory")
_A2OperationalGroupIndex_Type = DmiInteger
_A2OperationalGroupIndex_Object = MibTableColumn
a2OperationalGroupIndex = _A2OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 2, 1, 9),
    _A2OperationalGroupIndex_Type()
)
a2OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2OperationalGroupIndex.setStatus("mandatory")
_TTemperatureProbe_Object = MibTable
tTemperatureProbe = _TTemperatureProbe_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tTemperatureProbe.setStatus("mandatory")
_ETemperatureProbe_Object = MibTableRow
eTemperatureProbe = _ETemperatureProbe_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1)
)
eTemperatureProbe.setIndexNames(
    (0, "APCUPS-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eTemperatureProbe.setStatus("mandatory")
_A3TemperatureProbeTableIndex_Type = DmiInteger
_A3TemperatureProbeTableIndex_Object = MibTableColumn
a3TemperatureProbeTableIndex = _A3TemperatureProbeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 1),
    _A3TemperatureProbeTableIndex_Type()
)
a3TemperatureProbeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3TemperatureProbeTableIndex.setStatus("mandatory")


class _A3TemperatureProbeLocation_Type(Integer32):
    """Custom type a3TemperatureProbeLocation based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("vAdd-inCard", 11),
          ("vDisk", 4),
          ("vMemoryModule", 8),
          ("vMotherboard", 7),
          ("vOther", 1),
          ("vPeripheralBay", 5),
          ("vPowerUnit", 10),
          ("vProcessor", 3),
          ("vProcessorModule", 9),
          ("vSmbMaster", 6),
          ("vUnknown", 2))
    )


_A3TemperatureProbeLocation_Type.__name__ = "Integer32"
_A3TemperatureProbeLocation_Object = MibTableColumn
a3TemperatureProbeLocation = _A3TemperatureProbeLocation_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 2),
    _A3TemperatureProbeLocation_Type()
)
a3TemperatureProbeLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3TemperatureProbeLocation.setStatus("mandatory")
_A3TemperatureProbeDescription_Type = DmiDisplaystring
_A3TemperatureProbeDescription_Object = MibTableColumn
a3TemperatureProbeDescription = _A3TemperatureProbeDescription_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 3),
    _A3TemperatureProbeDescription_Type()
)
a3TemperatureProbeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3TemperatureProbeDescription.setStatus("mandatory")


class _A3TemperatureStatus_Type(Integer32):
    """Custom type a3TemperatureStatus based on Integer32"""
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
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A3TemperatureStatus_Type.__name__ = "Integer32"
_A3TemperatureStatus_Object = MibTableColumn
a3TemperatureStatus = _A3TemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 4),
    _A3TemperatureStatus_Type()
)
a3TemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3TemperatureStatus.setStatus("mandatory")
_A3TemperatureProbeTemperatureReading_Type = DmiInteger
_A3TemperatureProbeTemperatureReading_Object = MibTableColumn
a3TemperatureProbeTemperatureReading = _A3TemperatureProbeTemperatureReading_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 5),
    _A3TemperatureProbeTemperatureReading_Type()
)
a3TemperatureProbeTemperatureReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3TemperatureProbeTemperatureReading.setStatus("mandatory")
_A3MonitoredTemperatureNominalReading_Type = DmiInteger
_A3MonitoredTemperatureNominalReading_Object = MibTableColumn
a3MonitoredTemperatureNominalReading = _A3MonitoredTemperatureNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 6),
    _A3MonitoredTemperatureNominalReading_Type()
)
a3MonitoredTemperatureNominalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3MonitoredTemperatureNominalReading.setStatus("mandatory")
_A3MonitoredTemperatureNormalMaximum_Type = DmiInteger
_A3MonitoredTemperatureNormalMaximum_Object = MibTableColumn
a3MonitoredTemperatureNormalMaximum = _A3MonitoredTemperatureNormalMaximum_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 7),
    _A3MonitoredTemperatureNormalMaximum_Type()
)
a3MonitoredTemperatureNormalMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3MonitoredTemperatureNormalMaximum.setStatus("mandatory")
_A3MonitoredTemperatureNormalMinimum_Type = DmiInteger
_A3MonitoredTemperatureNormalMinimum_Object = MibTableColumn
a3MonitoredTemperatureNormalMinimum = _A3MonitoredTemperatureNormalMinimum_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 8),
    _A3MonitoredTemperatureNormalMinimum_Type()
)
a3MonitoredTemperatureNormalMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3MonitoredTemperatureNormalMinimum.setStatus("mandatory")
_A3TemperatureProbeMaximum_Type = DmiInteger
_A3TemperatureProbeMaximum_Object = MibTableColumn
a3TemperatureProbeMaximum = _A3TemperatureProbeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 9),
    _A3TemperatureProbeMaximum_Type()
)
a3TemperatureProbeMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3TemperatureProbeMaximum.setStatus("mandatory")
_A3TemperatureProbeMinimum_Type = DmiInteger
_A3TemperatureProbeMinimum_Object = MibTableColumn
a3TemperatureProbeMinimum = _A3TemperatureProbeMinimum_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 10),
    _A3TemperatureProbeMinimum_Type()
)
a3TemperatureProbeMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3TemperatureProbeMinimum.setStatus("mandatory")
_A3TemperatureReadingLowerThreshold_Non_c_Type = DmiInteger
_A3TemperatureReadingLowerThreshold_Non_c_Object = MibScalar
a3TemperatureReadingLowerThreshold_Non_c = _A3TemperatureReadingLowerThreshold_Non_c_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 11),
    _A3TemperatureReadingLowerThreshold_Non_c_Type()
)
a3TemperatureReadingLowerThreshold_Non_c.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3TemperatureReadingLowerThreshold_Non_c.setStatus("mandatory")
_A3TemperatureReadingUpperThreshold_Non_c_Type = DmiInteger
_A3TemperatureReadingUpperThreshold_Non_c_Object = MibScalar
a3TemperatureReadingUpperThreshold_Non_c = _A3TemperatureReadingUpperThreshold_Non_c_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 12),
    _A3TemperatureReadingUpperThreshold_Non_c_Type()
)
a3TemperatureReadingUpperThreshold_Non_c.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3TemperatureReadingUpperThreshold_Non_c.setStatus("mandatory")
_A3TemperatureReadingLowerThreshold_Criti_Type = DmiInteger
_A3TemperatureReadingLowerThreshold_Criti_Object = MibScalar
a3TemperatureReadingLowerThreshold_Criti = _A3TemperatureReadingLowerThreshold_Criti_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 13),
    _A3TemperatureReadingLowerThreshold_Criti_Type()
)
a3TemperatureReadingLowerThreshold_Criti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3TemperatureReadingLowerThreshold_Criti.setStatus("mandatory")
_A3TemperatureReadingUpperThreshold_Criti_Type = DmiInteger
_A3TemperatureReadingUpperThreshold_Criti_Object = MibScalar
a3TemperatureReadingUpperThreshold_Criti = _A3TemperatureReadingUpperThreshold_Criti_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 14),
    _A3TemperatureReadingUpperThreshold_Criti_Type()
)
a3TemperatureReadingUpperThreshold_Criti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3TemperatureReadingUpperThreshold_Criti.setStatus("mandatory")
_A3TemperatureReadingLowerThreshold_Non_r_Type = DmiInteger
_A3TemperatureReadingLowerThreshold_Non_r_Object = MibScalar
a3TemperatureReadingLowerThreshold_Non_r = _A3TemperatureReadingLowerThreshold_Non_r_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 15),
    _A3TemperatureReadingLowerThreshold_Non_r_Type()
)
a3TemperatureReadingLowerThreshold_Non_r.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3TemperatureReadingLowerThreshold_Non_r.setStatus("mandatory")
_A3TemperatureReadingUpperThreshold_Non_r_Type = DmiInteger
_A3TemperatureReadingUpperThreshold_Non_r_Object = MibScalar
a3TemperatureReadingUpperThreshold_Non_r = _A3TemperatureReadingUpperThreshold_Non_r_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 16),
    _A3TemperatureReadingUpperThreshold_Non_r_Type()
)
a3TemperatureReadingUpperThreshold_Non_r.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3TemperatureReadingUpperThreshold_Non_r.setStatus("mandatory")
_A3TemperatureProbeResolution_Type = DmiInteger
_A3TemperatureProbeResolution_Object = MibTableColumn
a3TemperatureProbeResolution = _A3TemperatureProbeResolution_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 17),
    _A3TemperatureProbeResolution_Type()
)
a3TemperatureProbeResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3TemperatureProbeResolution.setStatus("mandatory")
_A3TemperatureProbeTolerance_Type = DmiInteger
_A3TemperatureProbeTolerance_Object = MibTableColumn
a3TemperatureProbeTolerance = _A3TemperatureProbeTolerance_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 18),
    _A3TemperatureProbeTolerance_Type()
)
a3TemperatureProbeTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3TemperatureProbeTolerance.setStatus("mandatory")
_A3TemperatureProbeAccuracy_Type = DmiInteger
_A3TemperatureProbeAccuracy_Object = MibTableColumn
a3TemperatureProbeAccuracy = _A3TemperatureProbeAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 19),
    _A3TemperatureProbeAccuracy_Type()
)
a3TemperatureProbeAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3TemperatureProbeAccuracy.setStatus("mandatory")
_A3FruGroupIndex_Type = DmiInteger
_A3FruGroupIndex_Object = MibScalar
a3FruGroupIndex = _A3FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 20),
    _A3FruGroupIndex_Type()
)
a3FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3FruGroupIndex.setStatus("mandatory")
_A3OperationalGroupIndex_Type = DmiInteger
_A3OperationalGroupIndex_Object = MibScalar
a3OperationalGroupIndex = _A3OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 3, 1, 21),
    _A3OperationalGroupIndex_Type()
)
a3OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3OperationalGroupIndex.setStatus("mandatory")
_TOperationalStateTable_Object = MibTable
tOperationalStateTable = _TOperationalStateTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tOperationalStateTable.setStatus("mandatory")
_EOperationalStateTable_Object = MibTableRow
eOperationalStateTable = _EOperationalStateTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4, 1)
)
eOperationalStateTable.setIndexNames(
    (0, "APCUPS-MIB", "DmiComponentIndex"),
    (0, "APCUPS-MIB", "a4OperationalStateInstanceIndex"),
)
if mibBuilder.loadTexts:
    eOperationalStateTable.setStatus("mandatory")
_A4OperationalStateInstanceIndex_Type = DmiInteger
_A4OperationalStateInstanceIndex_Object = MibTableColumn
a4OperationalStateInstanceIndex = _A4OperationalStateInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4, 1, 1),
    _A4OperationalStateInstanceIndex_Type()
)
a4OperationalStateInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4OperationalStateInstanceIndex.setStatus("mandatory")
_A4DeviceGroupIndex_Type = DmiInteger
_A4DeviceGroupIndex_Object = MibTableColumn
a4DeviceGroupIndex = _A4DeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4, 1, 2),
    _A4DeviceGroupIndex_Type()
)
a4DeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4DeviceGroupIndex.setStatus("mandatory")


class _A4OperationalStatus_Type(Integer32):
    """Custom type a4OperationalStatus based on Integer32"""
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
        *(("vDisabled", 4),
          ("vEnabled", 3),
          ("vNotApplicable", 5),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A4OperationalStatus_Type.__name__ = "Integer32"
_A4OperationalStatus_Object = MibTableColumn
a4OperationalStatus = _A4OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4, 1, 3),
    _A4OperationalStatus_Type()
)
a4OperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4OperationalStatus.setStatus("mandatory")


class _A4UsageState_Type(Integer32):
    """Custom type a4UsageState based on Integer32"""
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
        *(("vActive", 4),
          ("vBusy", 5),
          ("vIdle", 3),
          ("vNotApplicable", 6),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A4UsageState_Type.__name__ = "Integer32"
_A4UsageState_Object = MibTableColumn
a4UsageState = _A4UsageState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4, 1, 4),
    _A4UsageState_Type()
)
a4UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4UsageState.setStatus("mandatory")


class _A4AvailabilityStatus_Type(Integer32):
    """Custom type a4AvailabilityStatus based on Integer32"""
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
        *(("vDegraded", 10),
          ("vInTest", 5),
          ("vInstallError", 12),
          ("vNotApplicable", 6),
          ("vNotInstalled", 11),
          ("vOffDuty", 9),
          ("vOffLine", 8),
          ("vOther", 1),
          ("vPowerOff", 7),
          ("vPowerSave", 13),
          ("vRunning", 3),
          ("vUnknown", 2),
          ("vWarning", 4))
    )


_A4AvailabilityStatus_Type.__name__ = "Integer32"
_A4AvailabilityStatus_Object = MibTableColumn
a4AvailabilityStatus = _A4AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4, 1, 5),
    _A4AvailabilityStatus_Type()
)
a4AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4AvailabilityStatus.setStatus("mandatory")


class _A4AdministrativeState_Type(Integer32):
    """Custom type a4AdministrativeState based on Integer32"""
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
        *(("vLocked", 3),
          ("vNotApplicable", 5),
          ("vOther", 1),
          ("vShuttingDown", 6),
          ("vUnknown", 2),
          ("vUnlocked", 4))
    )


_A4AdministrativeState_Type.__name__ = "Integer32"
_A4AdministrativeState_Object = MibTableColumn
a4AdministrativeState = _A4AdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4, 1, 6),
    _A4AdministrativeState_Type()
)
a4AdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4AdministrativeState.setStatus("mandatory")
_A4FatalErrorCount_Type = DmiCounter
_A4FatalErrorCount_Object = MibTableColumn
a4FatalErrorCount = _A4FatalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4, 1, 7),
    _A4FatalErrorCount_Type()
)
a4FatalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4FatalErrorCount.setStatus("mandatory")
_A4MajorErrorCount_Type = DmiCounter
_A4MajorErrorCount_Object = MibTableColumn
a4MajorErrorCount = _A4MajorErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4, 1, 8),
    _A4MajorErrorCount_Type()
)
a4MajorErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4MajorErrorCount.setStatus("mandatory")
_A4WarningErrorCount_Type = DmiCounter
_A4WarningErrorCount_Object = MibTableColumn
a4WarningErrorCount = _A4WarningErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4, 1, 9),
    _A4WarningErrorCount_Type()
)
a4WarningErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4WarningErrorCount.setStatus("mandatory")


class _A4CurrentErrorStatus_Type(Integer32):
    """Custom type a4CurrentErrorStatus based on Integer32"""
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
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A4CurrentErrorStatus_Type.__name__ = "Integer32"
_A4CurrentErrorStatus_Object = MibTableColumn
a4CurrentErrorStatus = _A4CurrentErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 4, 1, 10),
    _A4CurrentErrorStatus_Type()
)
a4CurrentErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4CurrentErrorStatus.setStatus("mandatory")
_TDiagnostics_Object = MibTable
tDiagnostics = _TDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tDiagnostics.setStatus("mandatory")
_EDiagnostics_Object = MibTableRow
eDiagnostics = _EDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 5, 1)
)
eDiagnostics.setIndexNames(
    (0, "APCUPS-MIB", "DmiComponentIndex"),
    (0, "APCUPS-MIB", "a5DiagnosticFunctionTableIndex"),
)
if mibBuilder.loadTexts:
    eDiagnostics.setStatus("mandatory")
_A5DiagnosticFunctionTableIndex_Type = DmiInteger
_A5DiagnosticFunctionTableIndex_Object = MibTableColumn
a5DiagnosticFunctionTableIndex = _A5DiagnosticFunctionTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 5, 1, 1),
    _A5DiagnosticFunctionTableIndex_Type()
)
a5DiagnosticFunctionTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5DiagnosticFunctionTableIndex.setStatus("mandatory")
_A5DiagnosticFunctionName_Type = DmiDisplaystring
_A5DiagnosticFunctionName_Object = MibTableColumn
a5DiagnosticFunctionName = _A5DiagnosticFunctionName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 5, 1, 2),
    _A5DiagnosticFunctionName_Type()
)
a5DiagnosticFunctionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5DiagnosticFunctionName.setStatus("mandatory")
_A5DiagnosticFunctionDescription_Type = DmiDisplaystring
_A5DiagnosticFunctionDescription_Object = MibTableColumn
a5DiagnosticFunctionDescription = _A5DiagnosticFunctionDescription_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 5, 1, 3),
    _A5DiagnosticFunctionDescription_Type()
)
a5DiagnosticFunctionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5DiagnosticFunctionDescription.setStatus("mandatory")


class _A5ExclusiveAccessRequired_Type(Integer32):
    """Custom type a5ExclusiveAccessRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A5ExclusiveAccessRequired_Type.__name__ = "Integer32"
_A5ExclusiveAccessRequired_Object = MibTableColumn
a5ExclusiveAccessRequired = _A5ExclusiveAccessRequired_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 5, 1, 4),
    _A5ExclusiveAccessRequired_Type()
)
a5ExclusiveAccessRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5ExclusiveAccessRequired.setStatus("mandatory")


class _A5PrerequisiteConditions_Type(Integer32):
    """Custom type a5PrerequisiteConditions based on Integer32"""
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
        *(("vNoMediaInstalled", 5),
          ("vNoPrerequisites", 3),
          ("vOther", 1),
          ("vScratchMediaInstalled", 6),
          ("vSystemReferenceDisketteInstalled", 8),
          ("vTestMediaInstalled", 7),
          ("vUnknown", 2),
          ("vWrapPlugInstalled", 4))
    )


_A5PrerequisiteConditions_Type.__name__ = "Integer32"
_A5PrerequisiteConditions_Object = MibTableColumn
a5PrerequisiteConditions = _A5PrerequisiteConditions_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 5, 1, 5),
    _A5PrerequisiteConditions_Type()
)
a5PrerequisiteConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5PrerequisiteConditions.setStatus("mandatory")
_A5PrerequisiteDiagnosticFunction_Type = DmiInteger
_A5PrerequisiteDiagnosticFunction_Object = MibTableColumn
a5PrerequisiteDiagnosticFunction = _A5PrerequisiteDiagnosticFunction_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 5, 1, 6),
    _A5PrerequisiteDiagnosticFunction_Type()
)
a5PrerequisiteDiagnosticFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5PrerequisiteDiagnosticFunction.setStatus("mandatory")
_TDiagnosticRequestGroup_Object = MibTable
tDiagnosticRequestGroup = _TDiagnosticRequestGroup_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tDiagnosticRequestGroup.setStatus("mandatory")
_EDiagnosticRequestGroup_Object = MibTableRow
eDiagnosticRequestGroup = _EDiagnosticRequestGroup_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 6, 1)
)
eDiagnosticRequestGroup.setIndexNames(
    (0, "APCUPS-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eDiagnosticRequestGroup.setStatus("mandatory")
_A6DiagnosticFunctionReserveKey_Type = DmiInteger
_A6DiagnosticFunctionReserveKey_Object = MibTableColumn
a6DiagnosticFunctionReserveKey = _A6DiagnosticFunctionReserveKey_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 6, 1, 1),
    _A6DiagnosticFunctionReserveKey_Type()
)
a6DiagnosticFunctionReserveKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a6DiagnosticFunctionReserveKey.setStatus("mandatory")
_A6DiagnosticFunctionRequest_Type = DmiInteger
_A6DiagnosticFunctionRequest_Object = MibTableColumn
a6DiagnosticFunctionRequest = _A6DiagnosticFunctionRequest_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 6, 1, 2),
    _A6DiagnosticFunctionRequest_Type()
)
a6DiagnosticFunctionRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a6DiagnosticFunctionRequest.setStatus("mandatory")
_A6DiagnosticFunctionResult_Type = DmiInteger
_A6DiagnosticFunctionResult_Object = MibTableColumn
a6DiagnosticFunctionResult = _A6DiagnosticFunctionResult_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 6, 1, 3),
    _A6DiagnosticFunctionResult_Type()
)
a6DiagnosticFunctionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6DiagnosticFunctionResult.setStatus("mandatory")
_TDiagnosticResults_Object = MibTable
tDiagnosticResults = _TDiagnosticResults_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tDiagnosticResults.setStatus("mandatory")
_EDiagnosticResults_Object = MibTableRow
eDiagnosticResults = _EDiagnosticResults_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 7, 1)
)
eDiagnosticResults.setIndexNames(
    (0, "APCUPS-MIB", "DmiComponentIndex"),
    (0, "APCUPS-MIB", "a7DiagnosticFunctionId"),
    (0, "APCUPS-MIB", "a7DiagnosticFunctionResult"),
)
if mibBuilder.loadTexts:
    eDiagnosticResults.setStatus("mandatory")
_A7DiagnosticFunctionId_Type = DmiInteger
_A7DiagnosticFunctionId_Object = MibTableColumn
a7DiagnosticFunctionId = _A7DiagnosticFunctionId_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 7, 1, 1),
    _A7DiagnosticFunctionId_Type()
)
a7DiagnosticFunctionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7DiagnosticFunctionId.setStatus("mandatory")
_A7DiagnosticFunctionResult_Type = DmiInteger
_A7DiagnosticFunctionResult_Object = MibTableColumn
a7DiagnosticFunctionResult = _A7DiagnosticFunctionResult_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 7, 1, 2),
    _A7DiagnosticFunctionResult_Type()
)
a7DiagnosticFunctionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7DiagnosticFunctionResult.setStatus("mandatory")
_A7DiagnosticFunctionResultDescription_Type = DmiDisplaystring
_A7DiagnosticFunctionResultDescription_Object = MibTableColumn
a7DiagnosticFunctionResultDescription = _A7DiagnosticFunctionResultDescription_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 7, 1, 3),
    _A7DiagnosticFunctionResultDescription_Type()
)
a7DiagnosticFunctionResultDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7DiagnosticFunctionResultDescription.setStatus("mandatory")


class _A7FaultIsolatedToThisComponent_Type(Integer32):
    """Custom type a7FaultIsolatedToThisComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A7FaultIsolatedToThisComponent_Type.__name__ = "Integer32"
_A7FaultIsolatedToThisComponent_Object = MibTableColumn
a7FaultIsolatedToThisComponent = _A7FaultIsolatedToThisComponent_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 7, 1, 4),
    _A7FaultIsolatedToThisComponent_Type()
)
a7FaultIsolatedToThisComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7FaultIsolatedToThisComponent.setStatus("mandatory")
_TErrorControlGroup_Object = MibTable
tErrorControlGroup = _TErrorControlGroup_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tErrorControlGroup.setStatus("mandatory")
_EErrorControlGroup_Object = MibTableRow
eErrorControlGroup = _EErrorControlGroup_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 8, 1)
)
eErrorControlGroup.setIndexNames(
    (0, "APCUPS-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eErrorControlGroup.setStatus("mandatory")
_A8Selfid_Type = DmiInteger
_A8Selfid_Object = MibTableColumn
a8Selfid = _A8Selfid_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 8, 1, 1),
    _A8Selfid_Type()
)
a8Selfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Selfid.setStatus("mandatory")
_A8NumberOfFatalErrors_Type = DmiCounter
_A8NumberOfFatalErrors_Object = MibTableColumn
a8NumberOfFatalErrors = _A8NumberOfFatalErrors_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 8, 1, 2),
    _A8NumberOfFatalErrors_Type()
)
a8NumberOfFatalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfFatalErrors.setStatus("mandatory")
_A8NumberOfMajorErrors_Type = DmiCounter
_A8NumberOfMajorErrors_Object = MibTableColumn
a8NumberOfMajorErrors = _A8NumberOfMajorErrors_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 8, 1, 3),
    _A8NumberOfMajorErrors_Type()
)
a8NumberOfMajorErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfMajorErrors.setStatus("mandatory")
_A8NumberOfWarnings_Type = DmiCounter
_A8NumberOfWarnings_Object = MibTableColumn
a8NumberOfWarnings = _A8NumberOfWarnings_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 8, 1, 4),
    _A8NumberOfWarnings_Type()
)
a8NumberOfWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8NumberOfWarnings.setStatus("mandatory")


class _A8ErrorStatus_Type(Integer32):
    """Custom type a8ErrorStatus based on Integer32"""
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
        *(("vFatal", 3),
          ("vMajor", 2),
          ("vOk", 0),
          ("vWarning", 1))
    )


_A8ErrorStatus_Type.__name__ = "Integer32"
_A8ErrorStatus_Object = MibTableColumn
a8ErrorStatus = _A8ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 8, 1, 5),
    _A8ErrorStatus_Type()
)
a8ErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8ErrorStatus.setStatus("mandatory")


class _A8ErrorStatusType_Type(Integer32):
    """Custom type a8ErrorStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vDiagnosticTest", 2),
          ("vPost", 0),
          ("vRuntime", 1))
    )


_A8ErrorStatusType_Type.__name__ = "Integer32"
_A8ErrorStatusType_Object = MibTableColumn
a8ErrorStatusType = _A8ErrorStatusType_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 8, 1, 6),
    _A8ErrorStatusType_Type()
)
a8ErrorStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8ErrorStatusType.setStatus("mandatory")


class _A8AlarmGeneration_Type(Integer32):
    """Custom type a8AlarmGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A8AlarmGeneration_Type.__name__ = "Integer32"
_A8AlarmGeneration_Object = MibTableColumn
a8AlarmGeneration = _A8AlarmGeneration_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 8, 1, 7),
    _A8AlarmGeneration_Type()
)
a8AlarmGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a8AlarmGeneration.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "APCUPS-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99MibName_Type = DmiDisplaystring
_A99MibName_Object = MibTableColumn
a99MibName = _A99MibName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 99, 1, 1),
    _A99MibName_Type()
)
a99MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibName.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTrap_Type = DmiInteger
_A99DisableTrap_Object = MibTableColumn
a99DisableTrap = _A99DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 99, 1, 3),
    _A99DisableTrap_Type()
)
a99DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a99DisableTrap.setStatus("mandatory")
_TTrapGroup_Object = MibTable
tTrapGroup = _TTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999)
)
if mibBuilder.loadTexts:
    tTrapGroup.setStatus("mandatory")
_ETrapGroup_Object = MibTableRow
eTrapGroup = _ETrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1)
)
eTrapGroup.setIndexNames(
    (0, "APCUPS-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eTrapGroup.setStatus("mandatory")
_A9999ErrorTime_Type = DisplayString
_A9999ErrorTime_Object = MibTableColumn
a9999ErrorTime = _A9999ErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 1),
    _A9999ErrorTime_Type()
)
a9999ErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorTime.setStatus("mandatory")
_A9999ErrorStatus_Type = DmiInteger
_A9999ErrorStatus_Object = MibTableColumn
a9999ErrorStatus = _A9999ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 2),
    _A9999ErrorStatus_Type()
)
a9999ErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorStatus.setStatus("mandatory")
_A9999ErrorGroupId_Type = DmiInteger
_A9999ErrorGroupId_Object = MibTableColumn
a9999ErrorGroupId = _A9999ErrorGroupId_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 3),
    _A9999ErrorGroupId_Type()
)
a9999ErrorGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorGroupId.setStatus("mandatory")
_A9999ErrorInstanceId_Type = DmiInteger
_A9999ErrorInstanceId_Object = MibTableColumn
a9999ErrorInstanceId = _A9999ErrorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 4),
    _A9999ErrorInstanceId_Type()
)
a9999ErrorInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorInstanceId.setStatus("mandatory")
_A9999ComponentId_Type = DmiInteger
_A9999ComponentId_Object = MibTableColumn
a9999ComponentId = _A9999ComponentId_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 5),
    _A9999ComponentId_Type()
)
a9999ComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ComponentId.setStatus("mandatory")
_A9999GroupId_Type = DmiInteger
_A9999GroupId_Object = MibTableColumn
a9999GroupId = _A9999GroupId_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 6),
    _A9999GroupId_Type()
)
a9999GroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999GroupId.setStatus("mandatory")
_A9999InstanceId_Type = DmiInteger
_A9999InstanceId_Object = MibTableColumn
a9999InstanceId = _A9999InstanceId_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 7),
    _A9999InstanceId_Type()
)
a9999InstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999InstanceId.setStatus("mandatory")
_A9999VendorCode1_Type = DmiInteger
_A9999VendorCode1_Object = MibTableColumn
a9999VendorCode1 = _A9999VendorCode1_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 8),
    _A9999VendorCode1_Type()
)
a9999VendorCode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorCode1.setStatus("mandatory")
_A9999VendorCode2_Type = DmiInteger
_A9999VendorCode2_Object = MibTableColumn
a9999VendorCode2 = _A9999VendorCode2_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 9),
    _A9999VendorCode2_Type()
)
a9999VendorCode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorCode2.setStatus("mandatory")
_A9999VendorText_Type = OctetString
_A9999VendorText_Object = MibTableColumn
a9999VendorText = _A9999VendorText_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 10),
    _A9999VendorText_Type()
)
a9999VendorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorText.setStatus("mandatory")
_A9999ParentGroupId_Type = DmiInteger
_A9999ParentGroupId_Object = MibTableColumn
a9999ParentGroupId = _A9999ParentGroupId_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 11),
    _A9999ParentGroupId_Type()
)
a9999ParentGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ParentGroupId.setStatus("mandatory")
_A9999ParentInstanceId_Type = DmiInteger
_A9999ParentInstanceId_Object = MibTableColumn
a9999ParentInstanceId = _A9999ParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 12),
    _A9999ParentInstanceId_Type()
)
a9999ParentInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ParentInstanceId.setStatus("mandatory")

# Managed Objects groups


# Notification objects

pwrchuteEventError = NotificationType(
    (1, 3, 6, 1, 4, 1, 318, 1, 2, 2, 1, 9999, 1, 0, 1)
)
pwrchuteEventError.setObjects(
      *(("APCUPS-MIB", "a9999ErrorTime"),
        ("APCUPS-MIB", "a9999ErrorStatus"),
        ("APCUPS-MIB", "a9999ErrorGroupId"),
        ("APCUPS-MIB", "a9999ErrorInstanceId"),
        ("APCUPS-MIB", "a9999ComponentId"),
        ("APCUPS-MIB", "a9999GroupId"),
        ("APCUPS-MIB", "a9999InstanceId"),
        ("APCUPS-MIB", "a9999VendorCode1"),
        ("APCUPS-MIB", "a9999VendorCode2"),
        ("APCUPS-MIB", "a9999VendorText"),
        ("APCUPS-MIB", "a9999ParentGroupId"),
        ("APCUPS-MIB", "a9999ParentInstanceId"))
)
if mibBuilder.loadTexts:
    pwrchuteEventError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APCUPS-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiGauge": DmiGauge,
       "DmiInteger": DmiInteger,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDateX": DmiDateX,
       "DmiComponentIndex": DmiComponentIndex,
       "apc": apc,
       "products": products,
       "software": software,
       "powerChuteDMIAgent": powerChuteDMIAgent,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tUpsBattery": tUpsBattery,
       "eUpsBattery": eUpsBattery,
       "a2BatteryStatus": a2BatteryStatus,
       "a2SecondsOnBattery": a2SecondsOnBattery,
       "a2EstimatedMinutesRemaining": a2EstimatedMinutesRemaining,
       "a2EstimatedChargeRemaining": a2EstimatedChargeRemaining,
       "a2BatteryVoltage": a2BatteryVoltage,
       "a2BatteryCurrent": a2BatteryCurrent,
       "a2TemperatureProbeIndex": a2TemperatureProbeIndex,
       "a2FruGroupIndex": a2FruGroupIndex,
       "a2OperationalGroupIndex": a2OperationalGroupIndex,
       "tTemperatureProbe": tTemperatureProbe,
       "eTemperatureProbe": eTemperatureProbe,
       "a3TemperatureProbeTableIndex": a3TemperatureProbeTableIndex,
       "a3TemperatureProbeLocation": a3TemperatureProbeLocation,
       "a3TemperatureProbeDescription": a3TemperatureProbeDescription,
       "a3TemperatureStatus": a3TemperatureStatus,
       "a3TemperatureProbeTemperatureReading": a3TemperatureProbeTemperatureReading,
       "a3MonitoredTemperatureNominalReading": a3MonitoredTemperatureNominalReading,
       "a3MonitoredTemperatureNormalMaximum": a3MonitoredTemperatureNormalMaximum,
       "a3MonitoredTemperatureNormalMinimum": a3MonitoredTemperatureNormalMinimum,
       "a3TemperatureProbeMaximum": a3TemperatureProbeMaximum,
       "a3TemperatureProbeMinimum": a3TemperatureProbeMinimum,
       "a3TemperatureReadingLowerThreshold-Non-c": a3TemperatureReadingLowerThreshold_Non_c,
       "a3TemperatureReadingUpperThreshold-Non-c": a3TemperatureReadingUpperThreshold_Non_c,
       "a3TemperatureReadingLowerThreshold-Criti": a3TemperatureReadingLowerThreshold_Criti,
       "a3TemperatureReadingUpperThreshold-Criti": a3TemperatureReadingUpperThreshold_Criti,
       "a3TemperatureReadingLowerThreshold-Non-r": a3TemperatureReadingLowerThreshold_Non_r,
       "a3TemperatureReadingUpperThreshold-Non-r": a3TemperatureReadingUpperThreshold_Non_r,
       "a3TemperatureProbeResolution": a3TemperatureProbeResolution,
       "a3TemperatureProbeTolerance": a3TemperatureProbeTolerance,
       "a3TemperatureProbeAccuracy": a3TemperatureProbeAccuracy,
       "a3FruGroupIndex": a3FruGroupIndex,
       "a3OperationalGroupIndex": a3OperationalGroupIndex,
       "tOperationalStateTable": tOperationalStateTable,
       "eOperationalStateTable": eOperationalStateTable,
       "a4OperationalStateInstanceIndex": a4OperationalStateInstanceIndex,
       "a4DeviceGroupIndex": a4DeviceGroupIndex,
       "a4OperationalStatus": a4OperationalStatus,
       "a4UsageState": a4UsageState,
       "a4AvailabilityStatus": a4AvailabilityStatus,
       "a4AdministrativeState": a4AdministrativeState,
       "a4FatalErrorCount": a4FatalErrorCount,
       "a4MajorErrorCount": a4MajorErrorCount,
       "a4WarningErrorCount": a4WarningErrorCount,
       "a4CurrentErrorStatus": a4CurrentErrorStatus,
       "tDiagnostics": tDiagnostics,
       "eDiagnostics": eDiagnostics,
       "a5DiagnosticFunctionTableIndex": a5DiagnosticFunctionTableIndex,
       "a5DiagnosticFunctionName": a5DiagnosticFunctionName,
       "a5DiagnosticFunctionDescription": a5DiagnosticFunctionDescription,
       "a5ExclusiveAccessRequired": a5ExclusiveAccessRequired,
       "a5PrerequisiteConditions": a5PrerequisiteConditions,
       "a5PrerequisiteDiagnosticFunction": a5PrerequisiteDiagnosticFunction,
       "tDiagnosticRequestGroup": tDiagnosticRequestGroup,
       "eDiagnosticRequestGroup": eDiagnosticRequestGroup,
       "a6DiagnosticFunctionReserveKey": a6DiagnosticFunctionReserveKey,
       "a6DiagnosticFunctionRequest": a6DiagnosticFunctionRequest,
       "a6DiagnosticFunctionResult": a6DiagnosticFunctionResult,
       "tDiagnosticResults": tDiagnosticResults,
       "eDiagnosticResults": eDiagnosticResults,
       "a7DiagnosticFunctionId": a7DiagnosticFunctionId,
       "a7DiagnosticFunctionResult": a7DiagnosticFunctionResult,
       "a7DiagnosticFunctionResultDescription": a7DiagnosticFunctionResultDescription,
       "a7FaultIsolatedToThisComponent": a7FaultIsolatedToThisComponent,
       "tErrorControlGroup": tErrorControlGroup,
       "eErrorControlGroup": eErrorControlGroup,
       "a8Selfid": a8Selfid,
       "a8NumberOfFatalErrors": a8NumberOfFatalErrors,
       "a8NumberOfMajorErrors": a8NumberOfMajorErrors,
       "a8NumberOfWarnings": a8NumberOfWarnings,
       "a8ErrorStatus": a8ErrorStatus,
       "a8ErrorStatusType": a8ErrorStatusType,
       "a8AlarmGeneration": a8AlarmGeneration,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99MibName": a99MibName,
       "a99MibOid": a99MibOid,
       "a99DisableTrap": a99DisableTrap,
       "tTrapGroup": tTrapGroup,
       "eTrapGroup": eTrapGroup,
       "pwrchuteEventError": pwrchuteEventError,
       "a9999ErrorTime": a9999ErrorTime,
       "a9999ErrorStatus": a9999ErrorStatus,
       "a9999ErrorGroupId": a9999ErrorGroupId,
       "a9999ErrorInstanceId": a9999ErrorInstanceId,
       "a9999ComponentId": a9999ComponentId,
       "a9999GroupId": a9999GroupId,
       "a9999InstanceId": a9999InstanceId,
       "a9999VendorCode1": a9999VendorCode1,
       "a9999VendorCode2": a9999VendorCode2,
       "a9999VendorText": a9999VendorText,
       "a9999ParentGroupId": a9999ParentGroupId,
       "a9999ParentInstanceId": a9999ParentInstanceId}
)
