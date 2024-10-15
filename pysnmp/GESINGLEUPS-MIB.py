# SNMP MIB module (GESINGLEUPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GESINGLEUPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:35 2024
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

(AutonomousType,
 DisplayString,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

imv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 818)
)
imv.setRevisions(
        ("2010-07-05 00:00",
         "2008-01-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PositiveInteger32(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NonNegativeInteger32(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_GeHardware_ObjectIdentity = ObjectIdentity
geHardware = _GeHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1)
)
_GeUPS_ObjectIdentity = ObjectIdentity
geUPS = _GeUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1)
)
_GeDiscoveredUPSsMask_Type = Integer32
_GeDiscoveredUPSsMask_Object = MibScalar
geDiscoveredUPSsMask = _GeDiscoveredUPSsMask_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 1),
    _GeDiscoveredUPSsMask_Type()
)
geDiscoveredUPSsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geDiscoveredUPSsMask.setStatus("current")
_GeRequestPacket_Type = DisplayString
_GeRequestPacket_Object = MibScalar
geRequestPacket = _GeRequestPacket_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 2),
    _GeRequestPacket_Type()
)
geRequestPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geRequestPacket.setStatus("current")
_GeReplyPacket_Type = DisplayString
_GeReplyPacket_Object = MibScalar
geReplyPacket = _GeReplyPacket_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 3),
    _GeReplyPacket_Type()
)
geReplyPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geReplyPacket.setStatus("current")
_GeGenericUPS_ObjectIdentity = ObjectIdentity
geGenericUPS = _GeGenericUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10)
)
_UpsIdentgen_ObjectIdentity = ObjectIdentity
upsIdentgen = _UpsIdentgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1)
)
_UpsIdentManufacturergen_Type = DisplayString
_UpsIdentManufacturergen_Object = MibScalar
upsIdentManufacturergen = _UpsIdentManufacturergen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 1),
    _UpsIdentManufacturergen_Type()
)
upsIdentManufacturergen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturergen.setStatus("current")
_UpsIdentModelgen_Type = DisplayString
_UpsIdentModelgen_Object = MibScalar
upsIdentModelgen = _UpsIdentModelgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 2),
    _UpsIdentModelgen_Type()
)
upsIdentModelgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModelgen.setStatus("current")
_UpsIdentUPSSoftwareVersiongen_Type = DisplayString
_UpsIdentUPSSoftwareVersiongen_Object = MibScalar
upsIdentUPSSoftwareVersiongen = _UpsIdentUPSSoftwareVersiongen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 3),
    _UpsIdentUPSSoftwareVersiongen_Type()
)
upsIdentUPSSoftwareVersiongen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSoftwareVersiongen.setStatus("current")
_UpsIdentAgentSoftwareVersiongen_Type = DisplayString
_UpsIdentAgentSoftwareVersiongen_Object = MibScalar
upsIdentAgentSoftwareVersiongen = _UpsIdentAgentSoftwareVersiongen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 4),
    _UpsIdentAgentSoftwareVersiongen_Type()
)
upsIdentAgentSoftwareVersiongen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentAgentSoftwareVersiongen.setStatus("current")
_UpsIdentNamegen_Type = DisplayString
_UpsIdentNamegen_Object = MibScalar
upsIdentNamegen = _UpsIdentNamegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 5),
    _UpsIdentNamegen_Type()
)
upsIdentNamegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentNamegen.setStatus("current")
_UpsIdentAttachedDevicesgen_Type = DisplayString
_UpsIdentAttachedDevicesgen_Object = MibScalar
upsIdentAttachedDevicesgen = _UpsIdentAttachedDevicesgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 6),
    _UpsIdentAttachedDevicesgen_Type()
)
upsIdentAttachedDevicesgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevicesgen.setStatus("current")
_UpsIdentUPSSerialNumbergen_Type = DisplayString
_UpsIdentUPSSerialNumbergen_Object = MibScalar
upsIdentUPSSerialNumbergen = _UpsIdentUPSSerialNumbergen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 7),
    _UpsIdentUPSSerialNumbergen_Type()
)
upsIdentUPSSerialNumbergen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSSerialNumbergen.setStatus("current")
_UpsIdentComProtVersiongen_Type = DisplayString
_UpsIdentComProtVersiongen_Object = MibScalar
upsIdentComProtVersiongen = _UpsIdentComProtVersiongen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 8),
    _UpsIdentComProtVersiongen_Type()
)
upsIdentComProtVersiongen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentComProtVersiongen.setStatus("current")
_UpsIdentOperatingTimegen_Type = NonNegativeInteger32
_UpsIdentOperatingTimegen_Object = MibScalar
upsIdentOperatingTimegen = _UpsIdentOperatingTimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 1, 9),
    _UpsIdentOperatingTimegen_Type()
)
upsIdentOperatingTimegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOperatingTimegen.setStatus("current")
if mibBuilder.loadTexts:
    upsIdentOperatingTimegen.setUnits("seconds")
_UpsBatterygen_ObjectIdentity = ObjectIdentity
upsBatterygen = _UpsBatterygen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2)
)


class _UpsBatteryStatusgen_Type(Integer32):
    """Custom type upsBatteryStatusgen based on Integer32"""
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
        *(("batteryDepleted", 4),
          ("batteryLow", 3),
          ("batteryNormal", 2),
          ("unknown", 1))
    )


_UpsBatteryStatusgen_Type.__name__ = "Integer32"
_UpsBatteryStatusgen_Object = MibScalar
upsBatteryStatusgen = _UpsBatteryStatusgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 1),
    _UpsBatteryStatusgen_Type()
)
upsBatteryStatusgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatusgen.setStatus("current")
_UpsSecondsOnBatterygen_Type = Integer32
_UpsSecondsOnBatterygen_Object = MibScalar
upsSecondsOnBatterygen = _UpsSecondsOnBatterygen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 2),
    _UpsSecondsOnBatterygen_Type()
)
upsSecondsOnBatterygen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsSecondsOnBatterygen.setStatus("current")
if mibBuilder.loadTexts:
    upsSecondsOnBatterygen.setUnits("seconds")
_UpsEstimatedMinutesRemaininggen_Type = PositiveInteger32
_UpsEstimatedMinutesRemaininggen_Object = MibScalar
upsEstimatedMinutesRemaininggen = _UpsEstimatedMinutesRemaininggen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 3),
    _UpsEstimatedMinutesRemaininggen_Type()
)
upsEstimatedMinutesRemaininggen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemaininggen.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedMinutesRemaininggen.setUnits("minutes")


class _UpsEstimatedChargeRemaininggen_Type(Integer32):
    """Custom type upsEstimatedChargeRemaininggen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEstimatedChargeRemaininggen_Type.__name__ = "Integer32"
_UpsEstimatedChargeRemaininggen_Object = MibScalar
upsEstimatedChargeRemaininggen = _UpsEstimatedChargeRemaininggen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 4),
    _UpsEstimatedChargeRemaininggen_Type()
)
upsEstimatedChargeRemaininggen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemaininggen.setStatus("current")
if mibBuilder.loadTexts:
    upsEstimatedChargeRemaininggen.setUnits("percent")
_UpsBatteryVoltagegen_Type = NonNegativeInteger32
_UpsBatteryVoltagegen_Object = MibScalar
upsBatteryVoltagegen = _UpsBatteryVoltagegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 5),
    _UpsBatteryVoltagegen_Type()
)
upsBatteryVoltagegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltagegen.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryVoltagegen.setUnits("0.1 Volt DC")
_UpsBatteryCurrentgen_Type = Integer32
_UpsBatteryCurrentgen_Object = MibScalar
upsBatteryCurrentgen = _UpsBatteryCurrentgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 6),
    _UpsBatteryCurrentgen_Type()
)
upsBatteryCurrentgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCurrentgen.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryCurrentgen.setUnits("0.1 Amp DC")
_UpsBatteryTemperaturegen_Type = Integer32
_UpsBatteryTemperaturegen_Object = MibScalar
upsBatteryTemperaturegen = _UpsBatteryTemperaturegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 7),
    _UpsBatteryTemperaturegen_Type()
)
upsBatteryTemperaturegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTemperaturegen.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryTemperaturegen.setUnits("degrees Centigrade")
_UpsBatteryRipplegen_Type = Integer32
_UpsBatteryRipplegen_Object = MibScalar
upsBatteryRipplegen = _UpsBatteryRipplegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 2, 8),
    _UpsBatteryRipplegen_Type()
)
upsBatteryRipplegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryRipplegen.setStatus("current")
if mibBuilder.loadTexts:
    upsBatteryRipplegen.setUnits("0.1 Volt RMS")
_UpsInputgen_ObjectIdentity = ObjectIdentity
upsInputgen = _UpsInputgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3)
)
_UpsInputLineBadsgen_Type = Counter32
_UpsInputLineBadsgen_Object = MibScalar
upsInputLineBadsgen = _UpsInputLineBadsgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 1),
    _UpsInputLineBadsgen_Type()
)
upsInputLineBadsgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBadsgen.setStatus("current")
_UpsInputNumLinesgen_Type = NonNegativeInteger32
_UpsInputNumLinesgen_Object = MibScalar
upsInputNumLinesgen = _UpsInputNumLinesgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 2),
    _UpsInputNumLinesgen_Type()
)
upsInputNumLinesgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumLinesgen.setStatus("current")
_UpsInputGenTable_Object = MibTable
upsInputGenTable = _UpsInputGenTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputGenTable.setStatus("current")
_UpsInputGenEntry_Object = MibTableRow
upsInputGenEntry = _UpsInputGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1)
)
upsInputGenEntry.setIndexNames(
    (0, "GESINGLEUPS-MIB", "upsInputLineIndexgen"),
)
if mibBuilder.loadTexts:
    upsInputGenEntry.setStatus("current")
_UpsInputLineIndexgen_Type = PositiveInteger32
_UpsInputLineIndexgen_Object = MibTableColumn
upsInputLineIndexgen = _UpsInputLineIndexgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 1),
    _UpsInputLineIndexgen_Type()
)
upsInputLineIndexgen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsInputLineIndexgen.setStatus("current")
_UpsInputFrequencygen_Type = NonNegativeInteger32
_UpsInputFrequencygen_Object = MibTableColumn
upsInputFrequencygen = _UpsInputFrequencygen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 2),
    _UpsInputFrequencygen_Type()
)
upsInputFrequencygen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequencygen.setStatus("current")
if mibBuilder.loadTexts:
    upsInputFrequencygen.setUnits("0.1 Hertz")
_UpsInputVoltagegen_Type = NonNegativeInteger32
_UpsInputVoltagegen_Object = MibTableColumn
upsInputVoltagegen = _UpsInputVoltagegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 3),
    _UpsInputVoltagegen_Type()
)
upsInputVoltagegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltagegen.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltagegen.setUnits("RMS Volts")
_UpsInputCurrentgen_Type = NonNegativeInteger32
_UpsInputCurrentgen_Object = MibTableColumn
upsInputCurrentgen = _UpsInputCurrentgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 4),
    _UpsInputCurrentgen_Type()
)
upsInputCurrentgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentgen.setStatus("current")
if mibBuilder.loadTexts:
    upsInputCurrentgen.setUnits("0.1 RMS Amp")
_UpsInputTruePowergen_Type = NonNegativeInteger32
_UpsInputTruePowergen_Object = MibTableColumn
upsInputTruePowergen = _UpsInputTruePowergen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 5),
    _UpsInputTruePowergen_Type()
)
upsInputTruePowergen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTruePowergen.setStatus("current")
if mibBuilder.loadTexts:
    upsInputTruePowergen.setUnits("Watts")
_UpsInputVoltageMingen_Type = NonNegativeInteger32
_UpsInputVoltageMingen_Object = MibTableColumn
upsInputVoltageMingen = _UpsInputVoltageMingen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 6),
    _UpsInputVoltageMingen_Type()
)
upsInputVoltageMingen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMingen.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMingen.setUnits("RMS Volts")
_UpsInputVoltageMaxgen_Type = NonNegativeInteger32
_UpsInputVoltageMaxgen_Object = MibTableColumn
upsInputVoltageMaxgen = _UpsInputVoltageMaxgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 3, 3, 1, 7),
    _UpsInputVoltageMaxgen_Type()
)
upsInputVoltageMaxgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltageMaxgen.setStatus("current")
if mibBuilder.loadTexts:
    upsInputVoltageMaxgen.setUnits("RMS Volts")
_UpsOutputgen_ObjectIdentity = ObjectIdentity
upsOutputgen = _UpsOutputgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4)
)


class _UpsOutputSourcegen_Type(Integer32):
    """Custom type upsOutputSourcegen based on Integer32"""
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
        *(("battery", 5),
          ("booster", 6),
          ("bypass", 4),
          ("none", 2),
          ("normal", 3),
          ("other", 1),
          ("reducer", 7))
    )


_UpsOutputSourcegen_Type.__name__ = "Integer32"
_UpsOutputSourcegen_Object = MibScalar
upsOutputSourcegen = _UpsOutputSourcegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 1),
    _UpsOutputSourcegen_Type()
)
upsOutputSourcegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSourcegen.setStatus("current")
_UpsOutputFrequencygen_Type = NonNegativeInteger32
_UpsOutputFrequencygen_Object = MibScalar
upsOutputFrequencygen = _UpsOutputFrequencygen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 2),
    _UpsOutputFrequencygen_Type()
)
upsOutputFrequencygen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequencygen.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputFrequencygen.setUnits("0.1 Hertz")
_UpsOutputNumLinesgen_Type = NonNegativeInteger32
_UpsOutputNumLinesgen_Object = MibScalar
upsOutputNumLinesgen = _UpsOutputNumLinesgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 3),
    _UpsOutputNumLinesgen_Type()
)
upsOutputNumLinesgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumLinesgen.setStatus("current")
_UpsOutputGenTable_Object = MibTable
upsOutputGenTable = _UpsOutputGenTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputGenTable.setStatus("current")
_UpsOutputGenEntry_Object = MibTableRow
upsOutputGenEntry = _UpsOutputGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1)
)
upsOutputGenEntry.setIndexNames(
    (0, "GESINGLEUPS-MIB", "upsOutputLineIndexgen"),
)
if mibBuilder.loadTexts:
    upsOutputGenEntry.setStatus("current")
_UpsOutputLineIndexgen_Type = PositiveInteger32
_UpsOutputLineIndexgen_Object = MibTableColumn
upsOutputLineIndexgen = _UpsOutputLineIndexgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 1),
    _UpsOutputLineIndexgen_Type()
)
upsOutputLineIndexgen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsOutputLineIndexgen.setStatus("current")
_UpsOutputVoltagegen_Type = NonNegativeInteger32
_UpsOutputVoltagegen_Object = MibTableColumn
upsOutputVoltagegen = _UpsOutputVoltagegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 2),
    _UpsOutputVoltagegen_Type()
)
upsOutputVoltagegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltagegen.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputVoltagegen.setUnits("RMS Volts")
_UpsOutputCurrentgen_Type = NonNegativeInteger32
_UpsOutputCurrentgen_Object = MibTableColumn
upsOutputCurrentgen = _UpsOutputCurrentgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 3),
    _UpsOutputCurrentgen_Type()
)
upsOutputCurrentgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentgen.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputCurrentgen.setUnits("0.1 RMS Amp")
_UpsOutputPowergen_Type = NonNegativeInteger32
_UpsOutputPowergen_Object = MibTableColumn
upsOutputPowergen = _UpsOutputPowergen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 4),
    _UpsOutputPowergen_Type()
)
upsOutputPowergen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowergen.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowergen.setUnits("Watts")


class _UpsOutputPercentLoadgen_Type(Integer32):
    """Custom type upsOutputPercentLoadgen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputPercentLoadgen_Type.__name__ = "Integer32"
_UpsOutputPercentLoadgen_Object = MibTableColumn
upsOutputPercentLoadgen = _UpsOutputPercentLoadgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 5),
    _UpsOutputPercentLoadgen_Type()
)
upsOutputPercentLoadgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPercentLoadgen.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPercentLoadgen.setUnits("percent")


class _UpsOutputPowerFactorgen_Type(Integer32):
    """Custom type upsOutputPowerFactorgen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 100),
    )


_UpsOutputPowerFactorgen_Type.__name__ = "Integer32"
_UpsOutputPowerFactorgen_Object = MibTableColumn
upsOutputPowerFactorgen = _UpsOutputPowerFactorgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 6),
    _UpsOutputPowerFactorgen_Type()
)
upsOutputPowerFactorgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactorgen.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPowerFactorgen.setUnits("0.01 cos phi")
_UpsOutputPeakCurrentgen_Type = Integer32
_UpsOutputPeakCurrentgen_Object = MibTableColumn
upsOutputPeakCurrentgen = _UpsOutputPeakCurrentgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 7),
    _UpsOutputPeakCurrentgen_Type()
)
upsOutputPeakCurrentgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentgen.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputPeakCurrentgen.setUnits("Amps")
_UpsOutputShareCurrentgen_Type = Integer32
_UpsOutputShareCurrentgen_Object = MibTableColumn
upsOutputShareCurrentgen = _UpsOutputShareCurrentgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 4, 4, 1, 8),
    _UpsOutputShareCurrentgen_Type()
)
upsOutputShareCurrentgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputShareCurrentgen.setStatus("current")
if mibBuilder.loadTexts:
    upsOutputShareCurrentgen.setUnits("Amps")
_UpsBypassgen_ObjectIdentity = ObjectIdentity
upsBypassgen = _UpsBypassgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5)
)
_UpsBypassFrequencygen_Type = NonNegativeInteger32
_UpsBypassFrequencygen_Object = MibScalar
upsBypassFrequencygen = _UpsBypassFrequencygen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 1),
    _UpsBypassFrequencygen_Type()
)
upsBypassFrequencygen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequencygen.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassFrequencygen.setUnits("0.1 Hertz")
_UpsBypassNumLinesgen_Type = NonNegativeInteger32
_UpsBypassNumLinesgen_Object = MibScalar
upsBypassNumLinesgen = _UpsBypassNumLinesgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 2),
    _UpsBypassNumLinesgen_Type()
)
upsBypassNumLinesgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumLinesgen.setStatus("current")
_UpsBypassGenTable_Object = MibTable
upsBypassGenTable = _UpsBypassGenTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassGenTable.setStatus("current")
_UpsBypassGenEntry_Object = MibTableRow
upsBypassGenEntry = _UpsBypassGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3, 1)
)
upsBypassGenEntry.setIndexNames(
    (0, "GESINGLEUPS-MIB", "upsBypassLineIndexgen"),
)
if mibBuilder.loadTexts:
    upsBypassGenEntry.setStatus("current")
_UpsBypassLineIndexgen_Type = PositiveInteger32
_UpsBypassLineIndexgen_Object = MibTableColumn
upsBypassLineIndexgen = _UpsBypassLineIndexgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3, 1, 1),
    _UpsBypassLineIndexgen_Type()
)
upsBypassLineIndexgen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsBypassLineIndexgen.setStatus("current")
_UpsBypassVoltagegen_Type = NonNegativeInteger32
_UpsBypassVoltagegen_Object = MibTableColumn
upsBypassVoltagegen = _UpsBypassVoltagegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3, 1, 2),
    _UpsBypassVoltagegen_Type()
)
upsBypassVoltagegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltagegen.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassVoltagegen.setUnits("RMS Volts")
_UpsBypassCurrentgen_Type = NonNegativeInteger32
_UpsBypassCurrentgen_Object = MibTableColumn
upsBypassCurrentgen = _UpsBypassCurrentgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3, 1, 3),
    _UpsBypassCurrentgen_Type()
)
upsBypassCurrentgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassCurrentgen.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassCurrentgen.setUnits("0.1 RMS Amp")
_UpsBypassPowergen_Type = NonNegativeInteger32
_UpsBypassPowergen_Object = MibTableColumn
upsBypassPowergen = _UpsBypassPowergen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 5, 3, 1, 4),
    _UpsBypassPowergen_Type()
)
upsBypassPowergen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPowergen.setStatus("current")
if mibBuilder.loadTexts:
    upsBypassPowergen.setUnits("Watts")
_UpsAlarmgen_ObjectIdentity = ObjectIdentity
upsAlarmgen = _UpsAlarmgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6)
)
_UpsAlarmsPresentgen_Type = Gauge32
_UpsAlarmsPresentgen_Object = MibScalar
upsAlarmsPresentgen = _UpsAlarmsPresentgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 1),
    _UpsAlarmsPresentgen_Type()
)
upsAlarmsPresentgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresentgen.setStatus("current")
_UpsAlarmGenTable_Object = MibTable
upsAlarmGenTable = _UpsAlarmGenTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmGenTable.setStatus("current")
_UpsAlarmGenEntry_Object = MibTableRow
upsAlarmGenEntry = _UpsAlarmGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 2, 1)
)
upsAlarmGenEntry.setIndexNames(
    (0, "GESINGLEUPS-MIB", "upsAlarmIdgen"),
)
if mibBuilder.loadTexts:
    upsAlarmGenEntry.setStatus("current")
_UpsAlarmIdgen_Type = PositiveInteger32
_UpsAlarmIdgen_Object = MibTableColumn
upsAlarmIdgen = _UpsAlarmIdgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 2, 1, 1),
    _UpsAlarmIdgen_Type()
)
upsAlarmIdgen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmIdgen.setStatus("current")
_UpsAlarmDescrgen_Type = AutonomousType
_UpsAlarmDescrgen_Object = MibTableColumn
upsAlarmDescrgen = _UpsAlarmDescrgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 2, 1, 2),
    _UpsAlarmDescrgen_Type()
)
upsAlarmDescrgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescrgen.setStatus("current")
_UpsAlarmTimegen_Type = TimeStamp
_UpsAlarmTimegen_Object = MibTableColumn
upsAlarmTimegen = _UpsAlarmTimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 2, 1, 3),
    _UpsAlarmTimegen_Type()
)
upsAlarmTimegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTimegen.setStatus("current")
_UpsWellKnownAlarmsgen_ObjectIdentity = ObjectIdentity
upsWellKnownAlarmsgen = _UpsWellKnownAlarmsgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3)
)
_UpsAlarmBatteryBadgen_ObjectIdentity = ObjectIdentity
upsAlarmBatteryBadgen = _UpsAlarmBatteryBadgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 1)
)
if mibBuilder.loadTexts:
    upsAlarmBatteryBadgen.setStatus("current")
_UpsAlarmOnBatterygen_ObjectIdentity = ObjectIdentity
upsAlarmOnBatterygen = _UpsAlarmOnBatterygen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 2)
)
if mibBuilder.loadTexts:
    upsAlarmOnBatterygen.setStatus("current")
_UpsAlarmLowBatterygen_ObjectIdentity = ObjectIdentity
upsAlarmLowBatterygen = _UpsAlarmLowBatterygen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 3)
)
if mibBuilder.loadTexts:
    upsAlarmLowBatterygen.setStatus("current")
_UpsAlarmDepletedBatterygen_ObjectIdentity = ObjectIdentity
upsAlarmDepletedBatterygen = _UpsAlarmDepletedBatterygen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 4)
)
if mibBuilder.loadTexts:
    upsAlarmDepletedBatterygen.setStatus("current")
_UpsAlarmTempBadgen_ObjectIdentity = ObjectIdentity
upsAlarmTempBadgen = _UpsAlarmTempBadgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 5)
)
if mibBuilder.loadTexts:
    upsAlarmTempBadgen.setStatus("current")
_UpsAlarmInputBadgen_ObjectIdentity = ObjectIdentity
upsAlarmInputBadgen = _UpsAlarmInputBadgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 6)
)
if mibBuilder.loadTexts:
    upsAlarmInputBadgen.setStatus("current")
_UpsAlarmOutputBadgen_ObjectIdentity = ObjectIdentity
upsAlarmOutputBadgen = _UpsAlarmOutputBadgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 7)
)
if mibBuilder.loadTexts:
    upsAlarmOutputBadgen.setStatus("current")
_UpsAlarmOutputOverloadgen_ObjectIdentity = ObjectIdentity
upsAlarmOutputOverloadgen = _UpsAlarmOutputOverloadgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 8)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOverloadgen.setStatus("current")
_UpsAlarmOnBypassgen_ObjectIdentity = ObjectIdentity
upsAlarmOnBypassgen = _UpsAlarmOnBypassgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 9)
)
if mibBuilder.loadTexts:
    upsAlarmOnBypassgen.setStatus("current")
_UpsAlarmBypassBadgen_ObjectIdentity = ObjectIdentity
upsAlarmBypassBadgen = _UpsAlarmBypassBadgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 10)
)
if mibBuilder.loadTexts:
    upsAlarmBypassBadgen.setStatus("current")
_UpsAlarmOutputOffAsRequestedgen_ObjectIdentity = ObjectIdentity
upsAlarmOutputOffAsRequestedgen = _UpsAlarmOutputOffAsRequestedgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 11)
)
if mibBuilder.loadTexts:
    upsAlarmOutputOffAsRequestedgen.setStatus("current")
_UpsAlarmUpsOffAsRequestedgen_ObjectIdentity = ObjectIdentity
upsAlarmUpsOffAsRequestedgen = _UpsAlarmUpsOffAsRequestedgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 12)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOffAsRequestedgen.setStatus("current")
_UpsAlarmChargerFailedgen_ObjectIdentity = ObjectIdentity
upsAlarmChargerFailedgen = _UpsAlarmChargerFailedgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 13)
)
if mibBuilder.loadTexts:
    upsAlarmChargerFailedgen.setStatus("current")
_UpsAlarmUpsOutputOffgen_ObjectIdentity = ObjectIdentity
upsAlarmUpsOutputOffgen = _UpsAlarmUpsOutputOffgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 14)
)
if mibBuilder.loadTexts:
    upsAlarmUpsOutputOffgen.setStatus("current")
_UpsAlarmUpsSystemOffgen_ObjectIdentity = ObjectIdentity
upsAlarmUpsSystemOffgen = _UpsAlarmUpsSystemOffgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 15)
)
if mibBuilder.loadTexts:
    upsAlarmUpsSystemOffgen.setStatus("current")
_UpsAlarmFanFailuregen_ObjectIdentity = ObjectIdentity
upsAlarmFanFailuregen = _UpsAlarmFanFailuregen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 16)
)
if mibBuilder.loadTexts:
    upsAlarmFanFailuregen.setStatus("current")
_UpsAlarmFuseFailuregen_ObjectIdentity = ObjectIdentity
upsAlarmFuseFailuregen = _UpsAlarmFuseFailuregen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 17)
)
if mibBuilder.loadTexts:
    upsAlarmFuseFailuregen.setStatus("current")
_UpsAlarmGeneralFaultgen_ObjectIdentity = ObjectIdentity
upsAlarmGeneralFaultgen = _UpsAlarmGeneralFaultgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 18)
)
if mibBuilder.loadTexts:
    upsAlarmGeneralFaultgen.setStatus("current")
_UpsAlarmDiagnosticTestFailedgen_ObjectIdentity = ObjectIdentity
upsAlarmDiagnosticTestFailedgen = _UpsAlarmDiagnosticTestFailedgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 19)
)
if mibBuilder.loadTexts:
    upsAlarmDiagnosticTestFailedgen.setStatus("current")
_UpsAlarmCommunicationsLostgen_ObjectIdentity = ObjectIdentity
upsAlarmCommunicationsLostgen = _UpsAlarmCommunicationsLostgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 20)
)
if mibBuilder.loadTexts:
    upsAlarmCommunicationsLostgen.setStatus("current")
_UpsAlarmAwaitingPowergen_ObjectIdentity = ObjectIdentity
upsAlarmAwaitingPowergen = _UpsAlarmAwaitingPowergen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 21)
)
if mibBuilder.loadTexts:
    upsAlarmAwaitingPowergen.setStatus("current")
_UpsAlarmShutdownPendinggen_ObjectIdentity = ObjectIdentity
upsAlarmShutdownPendinggen = _UpsAlarmShutdownPendinggen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 22)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownPendinggen.setStatus("current")
_UpsAlarmShutdownImminentgen_ObjectIdentity = ObjectIdentity
upsAlarmShutdownImminentgen = _UpsAlarmShutdownImminentgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 23)
)
if mibBuilder.loadTexts:
    upsAlarmShutdownImminentgen.setStatus("current")
_UpsAlarmTestInProgressgen_ObjectIdentity = ObjectIdentity
upsAlarmTestInProgressgen = _UpsAlarmTestInProgressgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 24)
)
if mibBuilder.loadTexts:
    upsAlarmTestInProgressgen.setStatus("current")
_UpsAlarmReceptacleOffgen_ObjectIdentity = ObjectIdentity
upsAlarmReceptacleOffgen = _UpsAlarmReceptacleOffgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 25)
)
if mibBuilder.loadTexts:
    upsAlarmReceptacleOffgen.setStatus("current")
_UpsAlarmHighSpeedBusFailuregen_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusFailuregen = _UpsAlarmHighSpeedBusFailuregen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 26)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusFailuregen.setStatus("current")
_UpsAlarmHighSpeedBusJACRCFailuregen_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJACRCFailuregen = _UpsAlarmHighSpeedBusJACRCFailuregen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 27)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJACRCFailuregen.setStatus("current")
_UpsAlarmConnectivityBusFailuregen_ObjectIdentity = ObjectIdentity
upsAlarmConnectivityBusFailuregen = _UpsAlarmConnectivityBusFailuregen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 28)
)
if mibBuilder.loadTexts:
    upsAlarmConnectivityBusFailuregen.setStatus("current")
_UpsAlarmHighSpeedBusJBCRCFailuregen_ObjectIdentity = ObjectIdentity
upsAlarmHighSpeedBusJBCRCFailuregen = _UpsAlarmHighSpeedBusJBCRCFailuregen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 29)
)
if mibBuilder.loadTexts:
    upsAlarmHighSpeedBusJBCRCFailuregen.setStatus("current")
_UpsAlarmCurrentSharinggen_ObjectIdentity = ObjectIdentity
upsAlarmCurrentSharinggen = _UpsAlarmCurrentSharinggen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 30)
)
if mibBuilder.loadTexts:
    upsAlarmCurrentSharinggen.setStatus("current")
_UpsAlarmDCRipplegen_ObjectIdentity = ObjectIdentity
upsAlarmDCRipplegen = _UpsAlarmDCRipplegen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 3, 31)
)
if mibBuilder.loadTexts:
    upsAlarmDCRipplegen.setStatus("current")
_UpsAlarmMaskAgen_Type = Unsigned32
_UpsAlarmMaskAgen_Object = MibScalar
upsAlarmMaskAgen = _UpsAlarmMaskAgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 6, 4),
    _UpsAlarmMaskAgen_Type()
)
upsAlarmMaskAgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmMaskAgen.setStatus("current")
_UpsTestgen_ObjectIdentity = ObjectIdentity
upsTestgen = _UpsTestgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7)
)
_UpsTestIdgen_Type = ObjectIdentifier
_UpsTestIdgen_Object = MibScalar
upsTestIdgen = _UpsTestIdgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 1),
    _UpsTestIdgen_Type()
)
upsTestIdgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestIdgen.setStatus("current")
_UpsTestSpinLockgen_Type = TestAndIncr
_UpsTestSpinLockgen_Object = MibScalar
upsTestSpinLockgen = _UpsTestSpinLockgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 2),
    _UpsTestSpinLockgen_Type()
)
upsTestSpinLockgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestSpinLockgen.setStatus("current")


class _UpsTestResultsSummarygen_Type(Integer32):
    """Custom type upsTestResultsSummarygen based on Integer32"""
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
          ("doneError", 3),
          ("donePass", 1),
          ("doneWarning", 2),
          ("inProgress", 5),
          ("noTestsInitiated", 6))
    )


_UpsTestResultsSummarygen_Type.__name__ = "Integer32"
_UpsTestResultsSummarygen_Object = MibScalar
upsTestResultsSummarygen = _UpsTestResultsSummarygen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 3),
    _UpsTestResultsSummarygen_Type()
)
upsTestResultsSummarygen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsSummarygen.setStatus("current")
_UpsTestResultsDetailgen_Type = DisplayString
_UpsTestResultsDetailgen_Object = MibScalar
upsTestResultsDetailgen = _UpsTestResultsDetailgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 4),
    _UpsTestResultsDetailgen_Type()
)
upsTestResultsDetailgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestResultsDetailgen.setStatus("current")
_UpsTestStartTimegen_Type = TimeStamp
_UpsTestStartTimegen_Object = MibScalar
upsTestStartTimegen = _UpsTestStartTimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 5),
    _UpsTestStartTimegen_Type()
)
upsTestStartTimegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestStartTimegen.setStatus("current")
_UpsTestElapsedTimegen_Type = TimeInterval
_UpsTestElapsedTimegen_Object = MibScalar
upsTestElapsedTimegen = _UpsTestElapsedTimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 6),
    _UpsTestElapsedTimegen_Type()
)
upsTestElapsedTimegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestElapsedTimegen.setStatus("current")
_UpsWellKnownTestsgen_ObjectIdentity = ObjectIdentity
upsWellKnownTestsgen = _UpsWellKnownTestsgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7)
)
_UpsTestNoTestsInitiatedgen_ObjectIdentity = ObjectIdentity
upsTestNoTestsInitiatedgen = _UpsTestNoTestsInitiatedgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7, 1)
)
if mibBuilder.loadTexts:
    upsTestNoTestsInitiatedgen.setStatus("current")
_UpsTestAbortTestInProgressgen_ObjectIdentity = ObjectIdentity
upsTestAbortTestInProgressgen = _UpsTestAbortTestInProgressgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7, 2)
)
if mibBuilder.loadTexts:
    upsTestAbortTestInProgressgen.setStatus("current")
_UpsTestGeneralSystemsTestgen_ObjectIdentity = ObjectIdentity
upsTestGeneralSystemsTestgen = _UpsTestGeneralSystemsTestgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7, 3)
)
if mibBuilder.loadTexts:
    upsTestGeneralSystemsTestgen.setStatus("current")
_UpsTestQuickBatteryTestgen_ObjectIdentity = ObjectIdentity
upsTestQuickBatteryTestgen = _UpsTestQuickBatteryTestgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7, 4)
)
if mibBuilder.loadTexts:
    upsTestQuickBatteryTestgen.setStatus("current")
_UpsTestDeepBatteryCalibrationgen_ObjectIdentity = ObjectIdentity
upsTestDeepBatteryCalibrationgen = _UpsTestDeepBatteryCalibrationgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 7, 7, 5)
)
if mibBuilder.loadTexts:
    upsTestDeepBatteryCalibrationgen.setStatus("current")
_UpsControlgen_ObjectIdentity = ObjectIdentity
upsControlgen = _UpsControlgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8)
)


class _UpsShutdownTypegen_Type(Integer32):
    """Custom type upsShutdownTypegen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("output", 1),
          ("system", 2))
    )


_UpsShutdownTypegen_Type.__name__ = "Integer32"
_UpsShutdownTypegen_Object = MibScalar
upsShutdownTypegen = _UpsShutdownTypegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 1),
    _UpsShutdownTypegen_Type()
)
upsShutdownTypegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownTypegen.setStatus("current")


class _UpsShutdownAfterDelaygen_Type(Integer32):
    """Custom type upsShutdownAfterDelaygen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsShutdownAfterDelaygen_Type.__name__ = "Integer32"
_UpsShutdownAfterDelaygen_Object = MibScalar
upsShutdownAfterDelaygen = _UpsShutdownAfterDelaygen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 2),
    _UpsShutdownAfterDelaygen_Type()
)
upsShutdownAfterDelaygen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsShutdownAfterDelaygen.setStatus("current")
if mibBuilder.loadTexts:
    upsShutdownAfterDelaygen.setUnits("seconds")


class _UpsStartupAfterDelaygen_Type(Integer32):
    """Custom type upsStartupAfterDelaygen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsStartupAfterDelaygen_Type.__name__ = "Integer32"
_UpsStartupAfterDelaygen_Object = MibScalar
upsStartupAfterDelaygen = _UpsStartupAfterDelaygen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 3),
    _UpsStartupAfterDelaygen_Type()
)
upsStartupAfterDelaygen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsStartupAfterDelaygen.setStatus("current")
if mibBuilder.loadTexts:
    upsStartupAfterDelaygen.setUnits("seconds")


class _UpsRebootWithDurationgen_Type(Integer32):
    """Custom type upsRebootWithDurationgen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_UpsRebootWithDurationgen_Type.__name__ = "Integer32"
_UpsRebootWithDurationgen_Object = MibScalar
upsRebootWithDurationgen = _UpsRebootWithDurationgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 4),
    _UpsRebootWithDurationgen_Type()
)
upsRebootWithDurationgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRebootWithDurationgen.setStatus("current")
if mibBuilder.loadTexts:
    upsRebootWithDurationgen.setUnits("seconds")


class _UpsAutoRestartgen_Type(Integer32):
    """Custom type upsAutoRestartgen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UpsAutoRestartgen_Type.__name__ = "Integer32"
_UpsAutoRestartgen_Object = MibScalar
upsAutoRestartgen = _UpsAutoRestartgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 5),
    _UpsAutoRestartgen_Type()
)
upsAutoRestartgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsAutoRestartgen.setStatus("current")
_UpsReceptaclesNumgen_Type = NonNegativeInteger32
_UpsReceptaclesNumgen_Object = MibScalar
upsReceptaclesNumgen = _UpsReceptaclesNumgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 6),
    _UpsReceptaclesNumgen_Type()
)
upsReceptaclesNumgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsReceptaclesNumgen.setStatus("current")
_UpsReceptacleGenTable_Object = MibTable
upsReceptacleGenTable = _UpsReceptacleGenTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 7)
)
if mibBuilder.loadTexts:
    upsReceptacleGenTable.setStatus("current")
_UpsReceptacleGenEntry_Object = MibTableRow
upsReceptacleGenEntry = _UpsReceptacleGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 7, 1)
)
upsReceptacleGenEntry.setIndexNames(
    (0, "GESINGLEUPS-MIB", "upsReceptacleLineIndexgen"),
)
if mibBuilder.loadTexts:
    upsReceptacleGenEntry.setStatus("current")
_UpsReceptacleLineIndexgen_Type = PositiveInteger32
_UpsReceptacleLineIndexgen_Object = MibTableColumn
upsReceptacleLineIndexgen = _UpsReceptacleLineIndexgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 7, 1, 1),
    _UpsReceptacleLineIndexgen_Type()
)
upsReceptacleLineIndexgen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsReceptacleLineIndexgen.setStatus("current")


class _UpsReceptacleOnOffgen_Type(Integer32):
    """Custom type upsReceptacleOnOffgen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UpsReceptacleOnOffgen_Type.__name__ = "Integer32"
_UpsReceptacleOnOffgen_Object = MibTableColumn
upsReceptacleOnOffgen = _UpsReceptacleOnOffgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 7, 1, 2),
    _UpsReceptacleOnOffgen_Type()
)
upsReceptacleOnOffgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsReceptacleOnOffgen.setStatus("current")


class _UpsUPSModegen_Type(Integer32):
    """Custom type upsUPSModegen based on Integer32"""
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
        *(("ecomode", 3),
          ("iem", 4),
          ("offLine", 1),
          ("onLine", 2))
    )


_UpsUPSModegen_Type.__name__ = "Integer32"
_UpsUPSModegen_Object = MibScalar
upsUPSModegen = _UpsUPSModegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 8),
    _UpsUPSModegen_Type()
)
upsUPSModegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsUPSModegen.setStatus("current")


class _UpsRectifierOnOffgen_Type(Integer32):
    """Custom type upsRectifierOnOffgen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UpsRectifierOnOffgen_Type.__name__ = "Integer32"
_UpsRectifierOnOffgen_Object = MibScalar
upsRectifierOnOffgen = _UpsRectifierOnOffgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 9),
    _UpsRectifierOnOffgen_Type()
)
upsRectifierOnOffgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRectifierOnOffgen.setStatus("current")


class _UpsBatteryChargeMethodgen_Type(Integer32):
    """Custom type upsBatteryChargeMethodgen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boostcharge", 2),
          ("normalcharge", 1))
    )


_UpsBatteryChargeMethodgen_Type.__name__ = "Integer32"
_UpsBatteryChargeMethodgen_Object = MibScalar
upsBatteryChargeMethodgen = _UpsBatteryChargeMethodgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 10),
    _UpsBatteryChargeMethodgen_Type()
)
upsBatteryChargeMethodgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryChargeMethodgen.setStatus("current")


class _UpsInverterOnOffgen_Type(Integer32):
    """Custom type upsInverterOnOffgen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UpsInverterOnOffgen_Type.__name__ = "Integer32"
_UpsInverterOnOffgen_Object = MibScalar
upsInverterOnOffgen = _UpsInverterOnOffgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 11),
    _UpsInverterOnOffgen_Type()
)
upsInverterOnOffgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsInverterOnOffgen.setStatus("current")


class _UpsBypassOnOffgen_Type(Integer32):
    """Custom type upsBypassOnOffgen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UpsBypassOnOffgen_Type.__name__ = "Integer32"
_UpsBypassOnOffgen_Object = MibScalar
upsBypassOnOffgen = _UpsBypassOnOffgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 12),
    _UpsBypassOnOffgen_Type()
)
upsBypassOnOffgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBypassOnOffgen.setStatus("current")


class _UpsLoadSourcegen_Type(Integer32):
    """Custom type upsLoadSourcegen based on Integer32"""
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
        *(("loadOff", 4),
          ("onDetour", 3),
          ("onInverter", 2),
          ("onbypass", 1),
          ("other", 5))
    )


_UpsLoadSourcegen_Type.__name__ = "Integer32"
_UpsLoadSourcegen_Object = MibScalar
upsLoadSourcegen = _UpsLoadSourcegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 8, 13),
    _UpsLoadSourcegen_Type()
)
upsLoadSourcegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadSourcegen.setStatus("current")
_UpsConfiggen_ObjectIdentity = ObjectIdentity
upsConfiggen = _UpsConfiggen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9)
)
_UpsConfigInputVoltagegen_Type = NonNegativeInteger32
_UpsConfigInputVoltagegen_Object = MibScalar
upsConfigInputVoltagegen = _UpsConfigInputVoltagegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 1),
    _UpsConfigInputVoltagegen_Type()
)
upsConfigInputVoltagegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputVoltagegen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputVoltagegen.setUnits("RMS Volts")
_UpsConfigInputFreqgen_Type = NonNegativeInteger32
_UpsConfigInputFreqgen_Object = MibScalar
upsConfigInputFreqgen = _UpsConfigInputFreqgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 2),
    _UpsConfigInputFreqgen_Type()
)
upsConfigInputFreqgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigInputFreqgen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigInputFreqgen.setUnits("0.1 Hertz")
_UpsConfigOutputVoltagegen_Type = NonNegativeInteger32
_UpsConfigOutputVoltagegen_Object = MibScalar
upsConfigOutputVoltagegen = _UpsConfigOutputVoltagegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 3),
    _UpsConfigOutputVoltagegen_Type()
)
upsConfigOutputVoltagegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagegen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVoltagegen.setUnits("RMS Volts")
_UpsConfigOutputFreqgen_Type = NonNegativeInteger32
_UpsConfigOutputFreqgen_Object = MibScalar
upsConfigOutputFreqgen = _UpsConfigOutputFreqgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 4),
    _UpsConfigOutputFreqgen_Type()
)
upsConfigOutputFreqgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigOutputFreqgen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputFreqgen.setUnits("0.1 Hertz")
_UpsConfigOutputVAgen_Type = NonNegativeInteger32
_UpsConfigOutputVAgen_Object = MibScalar
upsConfigOutputVAgen = _UpsConfigOutputVAgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 5),
    _UpsConfigOutputVAgen_Type()
)
upsConfigOutputVAgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVAgen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputVAgen.setUnits("Volt-Amps")
_UpsConfigOutputPowergen_Type = NonNegativeInteger32
_UpsConfigOutputPowergen_Object = MibScalar
upsConfigOutputPowergen = _UpsConfigOutputPowergen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 6),
    _UpsConfigOutputPowergen_Type()
)
upsConfigOutputPowergen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputPowergen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigOutputPowergen.setUnits("Watts")
_UpsConfigLowBattTimegen_Type = NonNegativeInteger32
_UpsConfigLowBattTimegen_Object = MibScalar
upsConfigLowBattTimegen = _UpsConfigLowBattTimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 7),
    _UpsConfigLowBattTimegen_Type()
)
upsConfigLowBattTimegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowBattTimegen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowBattTimegen.setUnits("minutes")


class _UpsConfigAudibleStatusgen_Type(Integer32):
    """Custom type upsConfigAudibleStatusgen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("muted", 3))
    )


_UpsConfigAudibleStatusgen_Type.__name__ = "Integer32"
_UpsConfigAudibleStatusgen_Object = MibScalar
upsConfigAudibleStatusgen = _UpsConfigAudibleStatusgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 8),
    _UpsConfigAudibleStatusgen_Type()
)
upsConfigAudibleStatusgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAudibleStatusgen.setStatus("current")
_UpsConfigLowVoltageTransferPointgen_Type = NonNegativeInteger32
_UpsConfigLowVoltageTransferPointgen_Object = MibScalar
upsConfigLowVoltageTransferPointgen = _UpsConfigLowVoltageTransferPointgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 9),
    _UpsConfigLowVoltageTransferPointgen_Type()
)
upsConfigLowVoltageTransferPointgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointgen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPointgen.setUnits("RMS Volts")
_UpsConfigHighVoltageTransferPointgen_Type = NonNegativeInteger32
_UpsConfigHighVoltageTransferPointgen_Object = MibScalar
upsConfigHighVoltageTransferPointgen = _UpsConfigHighVoltageTransferPointgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 10),
    _UpsConfigHighVoltageTransferPointgen_Type()
)
upsConfigHighVoltageTransferPointgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointgen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPointgen.setUnits("RMS Volts")
_UpsConfigBatteryCapacitygen_Type = NonNegativeInteger32
_UpsConfigBatteryCapacitygen_Object = MibScalar
upsConfigBatteryCapacitygen = _UpsConfigBatteryCapacitygen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 11),
    _UpsConfigBatteryCapacitygen_Type()
)
upsConfigBatteryCapacitygen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacitygen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryCapacitygen.setUnits("Amps Hours")
_UpsConfigBatteryChargeCurrentgen_Type = NonNegativeInteger32
_UpsConfigBatteryChargeCurrentgen_Object = MibScalar
upsConfigBatteryChargeCurrentgen = _UpsConfigBatteryChargeCurrentgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 12),
    _UpsConfigBatteryChargeCurrentgen_Type()
)
upsConfigBatteryChargeCurrentgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentgen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigBatteryChargeCurrentgen.setUnits("0.1 Amp DC")


class _UpsConfigNoLoadShutdowngen_Type(Integer32):
    """Custom type upsConfigNoLoadShutdowngen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_UpsConfigNoLoadShutdowngen_Type.__name__ = "Integer32"
_UpsConfigNoLoadShutdowngen_Object = MibScalar
upsConfigNoLoadShutdowngen = _UpsConfigNoLoadShutdowngen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 13),
    _UpsConfigNoLoadShutdowngen_Type()
)
upsConfigNoLoadShutdowngen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigNoLoadShutdowngen.setStatus("current")
_UpsConfigStartDelaygen_Type = PositiveInteger32
_UpsConfigStartDelaygen_Object = MibScalar
upsConfigStartDelaygen = _UpsConfigStartDelaygen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 9, 14),
    _UpsConfigStartDelaygen_Type()
)
upsConfigStartDelaygen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigStartDelaygen.setStatus("current")
if mibBuilder.loadTexts:
    upsConfigStartDelaygen.setUnits("minutes")
_UpsGetSetgen_ObjectIdentity = ObjectIdentity
upsGetSetgen = _UpsGetSetgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10)
)
_UpsEventGetNextgen_Type = PositiveInteger32
_UpsEventGetNextgen_Object = MibScalar
upsEventGetNextgen = _UpsEventGetNextgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 1),
    _UpsEventGetNextgen_Type()
)
upsEventGetNextgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetNextgen.setStatus("current")
_UpsEventGetPreviousgen_Type = PositiveInteger32
_UpsEventGetPreviousgen_Object = MibScalar
upsEventGetPreviousgen = _UpsEventGetPreviousgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 2),
    _UpsEventGetPreviousgen_Type()
)
upsEventGetPreviousgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetPreviousgen.setStatus("current")
_UpsEventSetStartingTimeStampgen_Type = NonNegativeInteger32
_UpsEventSetStartingTimeStampgen_Object = MibScalar
upsEventSetStartingTimeStampgen = _UpsEventSetStartingTimeStampgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 3),
    _UpsEventSetStartingTimeStampgen_Type()
)
upsEventSetStartingTimeStampgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSetStartingTimeStampgen.setStatus("current")
_UpsEventRetreiveCurrentTimeStampgen_Type = NonNegativeInteger32
_UpsEventRetreiveCurrentTimeStampgen_Object = MibScalar
upsEventRetreiveCurrentTimeStampgen = _UpsEventRetreiveCurrentTimeStampgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 4),
    _UpsEventRetreiveCurrentTimeStampgen_Type()
)
upsEventRetreiveCurrentTimeStampgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventRetreiveCurrentTimeStampgen.setStatus("current")
_UpsEventTableSizegen_Type = NonNegativeInteger32
_UpsEventTableSizegen_Object = MibScalar
upsEventTableSizegen = _UpsEventTableSizegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 5),
    _UpsEventTableSizegen_Type()
)
upsEventTableSizegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTableSizegen.setStatus("current")
_UpsEventGenTable_Object = MibTable
upsEventGenTable = _UpsEventGenTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6)
)
if mibBuilder.loadTexts:
    upsEventGenTable.setStatus("current")
_UpsEventGenEntry_Object = MibTableRow
upsEventGenEntry = _UpsEventGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6, 1)
)
upsEventGenEntry.setIndexNames(
    (0, "GESINGLEUPS-MIB", "upsEventLineIndexgen"),
)
if mibBuilder.loadTexts:
    upsEventGenEntry.setStatus("current")
_UpsEventLineIndexgen_Type = PositiveInteger32
_UpsEventLineIndexgen_Object = MibTableColumn
upsEventLineIndexgen = _UpsEventLineIndexgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6, 1, 1),
    _UpsEventLineIndexgen_Type()
)
upsEventLineIndexgen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsEventLineIndexgen.setStatus("current")
_UpsEventCodegen_Type = Integer32
_UpsEventCodegen_Object = MibTableColumn
upsEventCodegen = _UpsEventCodegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6, 1, 2),
    _UpsEventCodegen_Type()
)
upsEventCodegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventCodegen.setStatus("current")
_UpsEventStatusgen_Type = NonNegativeInteger32
_UpsEventStatusgen_Object = MibTableColumn
upsEventStatusgen = _UpsEventStatusgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6, 1, 3),
    _UpsEventStatusgen_Type()
)
upsEventStatusgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventStatusgen.setStatus("current")
_UpsEventTimegen_Type = NonNegativeInteger32
_UpsEventTimegen_Object = MibTableColumn
upsEventTimegen = _UpsEventTimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 6, 1, 4),
    _UpsEventTimegen_Type()
)
upsEventTimegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEventTimegen.setStatus("current")
_UpsParametersReadgen_Type = PositiveInteger32
_UpsParametersReadgen_Object = MibScalar
upsParametersReadgen = _UpsParametersReadgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 7),
    _UpsParametersReadgen_Type()
)
upsParametersReadgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersReadgen.setStatus("current")
_UpsParametersWritegen_Type = PositiveInteger32
_UpsParametersWritegen_Object = MibScalar
upsParametersWritegen = _UpsParametersWritegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 8),
    _UpsParametersWritegen_Type()
)
upsParametersWritegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersWritegen.setStatus("current")
_UpsParametersStartAddressgen_Type = NonNegativeInteger32
_UpsParametersStartAddressgen_Object = MibScalar
upsParametersStartAddressgen = _UpsParametersStartAddressgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 9),
    _UpsParametersStartAddressgen_Type()
)
upsParametersStartAddressgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParametersStartAddressgen.setStatus("current")
_UpsParameterTableSizegen_Type = NonNegativeInteger32
_UpsParameterTableSizegen_Object = MibScalar
upsParameterTableSizegen = _UpsParameterTableSizegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 10),
    _UpsParameterTableSizegen_Type()
)
upsParameterTableSizegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsParameterTableSizegen.setStatus("current")
_UpsParameterGenTable_Object = MibTable
upsParameterGenTable = _UpsParameterGenTable_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 11)
)
if mibBuilder.loadTexts:
    upsParameterGenTable.setStatus("current")
_UpsParameterGenEntry_Object = MibTableRow
upsParameterGenEntry = _UpsParameterGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 11, 1)
)
upsParameterGenEntry.setIndexNames(
    (0, "GESINGLEUPS-MIB", "upsParameterLineIndexgen"),
)
if mibBuilder.loadTexts:
    upsParameterGenEntry.setStatus("current")
_UpsParameterLineIndexgen_Type = PositiveInteger32
_UpsParameterLineIndexgen_Object = MibTableColumn
upsParameterLineIndexgen = _UpsParameterLineIndexgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 11, 1, 1),
    _UpsParameterLineIndexgen_Type()
)
upsParameterLineIndexgen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsParameterLineIndexgen.setStatus("current")
_UpsParameterValuegen_Type = Integer32
_UpsParameterValuegen_Object = MibTableColumn
upsParameterValuegen = _UpsParameterValuegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 11, 1, 2),
    _UpsParameterValuegen_Type()
)
upsParameterValuegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterValuegen.setStatus("current")
_UpsStatusgen_Type = NonNegativeInteger32
_UpsStatusgen_Object = MibScalar
upsStatusgen = _UpsStatusgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 12),
    _UpsStatusgen_Type()
)
upsStatusgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatusgen.setStatus("current")
_UpsMainsStatisticsMBfailgen_Type = NonNegativeInteger32
_UpsMainsStatisticsMBfailgen_Object = MibScalar
upsMainsStatisticsMBfailgen = _UpsMainsStatisticsMBfailgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 13),
    _UpsMainsStatisticsMBfailgen_Type()
)
upsMainsStatisticsMBfailgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMBfailgen.setStatus("current")
_UpsMainsStatisticsMRfailgen_Type = NonNegativeInteger32
_UpsMainsStatisticsMRfailgen_Object = MibScalar
upsMainsStatisticsMRfailgen = _UpsMainsStatisticsMRfailgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 14),
    _UpsMainsStatisticsMRfailgen_Type()
)
upsMainsStatisticsMRfailgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsMRfailgen.setStatus("current")
_UpsMainsStatisticsB2gen_Type = NonNegativeInteger32
_UpsMainsStatisticsB2gen_Object = MibScalar
upsMainsStatisticsB2gen = _UpsMainsStatisticsB2gen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 15),
    _UpsMainsStatisticsB2gen_Type()
)
upsMainsStatisticsB2gen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB2gen.setStatus("current")
_UpsMainsStatisticsB5gen_Type = NonNegativeInteger32
_UpsMainsStatisticsB5gen_Object = MibScalar
upsMainsStatisticsB5gen = _UpsMainsStatisticsB5gen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 16),
    _UpsMainsStatisticsB5gen_Type()
)
upsMainsStatisticsB5gen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB5gen.setStatus("current")
_UpsMainsStatisticsB10gen_Type = NonNegativeInteger32
_UpsMainsStatisticsB10gen_Object = MibScalar
upsMainsStatisticsB10gen = _UpsMainsStatisticsB10gen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 17),
    _UpsMainsStatisticsB10gen_Type()
)
upsMainsStatisticsB10gen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB10gen.setStatus("current")
_UpsMainsStatisticsB200gen_Type = NonNegativeInteger32
_UpsMainsStatisticsB200gen_Object = MibScalar
upsMainsStatisticsB200gen = _UpsMainsStatisticsB200gen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 18),
    _UpsMainsStatisticsB200gen_Type()
)
upsMainsStatisticsB200gen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsB200gen.setStatus("current")
_UpsMainsStatisticsBypRelgen_Type = NonNegativeInteger32
_UpsMainsStatisticsBypRelgen_Object = MibScalar
upsMainsStatisticsBypRelgen = _UpsMainsStatisticsBypRelgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 19),
    _UpsMainsStatisticsBypRelgen_Type()
)
upsMainsStatisticsBypRelgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsMainsStatisticsBypRelgen.setStatus("current")
_UpsTimegen_Type = NonNegativeInteger32
_UpsTimegen_Object = MibScalar
upsTimegen = _UpsTimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 20),
    _UpsTimegen_Type()
)
upsTimegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimegen.setStatus("current")
_UpsRequestPermissiongen_Type = DisplayString
_UpsRequestPermissiongen_Object = MibScalar
upsRequestPermissiongen = _UpsRequestPermissiongen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 21),
    _UpsRequestPermissiongen_Type()
)
upsRequestPermissiongen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRequestPermissiongen.setStatus("current")
_UpsEventGetCodegen_Type = Integer32
_UpsEventGetCodegen_Object = MibScalar
upsEventGetCodegen = _UpsEventGetCodegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 22),
    _UpsEventGetCodegen_Type()
)
upsEventGetCodegen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventGetCodegen.setStatus("current")
_UpsEventSpinLockgen_Type = TestAndIncr
_UpsEventSpinLockgen_Object = MibScalar
upsEventSpinLockgen = _UpsEventSpinLockgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 23),
    _UpsEventSpinLockgen_Type()
)
upsEventSpinLockgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEventSpinLockgen.setStatus("current")
_UpsParameterSpinLockgen_Type = TestAndIncr
_UpsParameterSpinLockgen_Object = MibScalar
upsParameterSpinLockgen = _UpsParameterSpinLockgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 10, 24),
    _UpsParameterSpinLockgen_Type()
)
upsParameterSpinLockgen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsParameterSpinLockgen.setStatus("current")
_GeUPSTrapsgen_ObjectIdentity = ObjectIdentity
geUPSTrapsgen = _GeUPSTrapsgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11)
)
_UpsDiagnosticgen_ObjectIdentity = ObjectIdentity
upsDiagnosticgen = _UpsDiagnosticgen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12)
)
_UpsDiagnosticBusJACommunicationStatusgen_Type = Integer32
_UpsDiagnosticBusJACommunicationStatusgen_Object = MibScalar
upsDiagnosticBusJACommunicationStatusgen = _UpsDiagnosticBusJACommunicationStatusgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 1),
    _UpsDiagnosticBusJACommunicationStatusgen_Type()
)
upsDiagnosticBusJACommunicationStatusgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJACommunicationStatusgen.setStatus("current")
_UpsDiagnosticBusJBCommunicationStatusgen_Type = Integer32
_UpsDiagnosticBusJBCommunicationStatusgen_Object = MibScalar
upsDiagnosticBusJBCommunicationStatusgen = _UpsDiagnosticBusJBCommunicationStatusgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 2),
    _UpsDiagnosticBusJBCommunicationStatusgen_Type()
)
upsDiagnosticBusJBCommunicationStatusgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBusJBCommunicationStatusgen.setStatus("current")
_UpsDiagnosticBatteryLifetimegen_Type = Integer32
_UpsDiagnosticBatteryLifetimegen_Object = MibScalar
upsDiagnosticBatteryLifetimegen = _UpsDiagnosticBatteryLifetimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 3),
    _UpsDiagnosticBatteryLifetimegen_Type()
)
upsDiagnosticBatteryLifetimegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticBatteryLifetimegen.setStatus("current")
_UpsDiagnosticFansLifetimegen_Type = Integer32
_UpsDiagnosticFansLifetimegen_Object = MibScalar
upsDiagnosticFansLifetimegen = _UpsDiagnosticFansLifetimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 4),
    _UpsDiagnosticFansLifetimegen_Type()
)
upsDiagnosticFansLifetimegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticFansLifetimegen.setStatus("current")
_UpsDiagnosticDCcapacitorsLifetimegen_Type = Integer32
_UpsDiagnosticDCcapacitorsLifetimegen_Object = MibScalar
upsDiagnosticDCcapacitorsLifetimegen = _UpsDiagnosticDCcapacitorsLifetimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 5),
    _UpsDiagnosticDCcapacitorsLifetimegen_Type()
)
upsDiagnosticDCcapacitorsLifetimegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticDCcapacitorsLifetimegen.setStatus("current")
_UpsDiagnosticACcapacitorsLifetimegen_Type = Integer32
_UpsDiagnosticACcapacitorsLifetimegen_Object = MibScalar
upsDiagnosticACcapacitorsLifetimegen = _UpsDiagnosticACcapacitorsLifetimegen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 6),
    _UpsDiagnosticACcapacitorsLifetimegen_Type()
)
upsDiagnosticACcapacitorsLifetimegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticACcapacitorsLifetimegen.setStatus("current")
_UpsDiagnosticGlobalServiceCheckgen_Type = Integer32
_UpsDiagnosticGlobalServiceCheckgen_Object = MibScalar
upsDiagnosticGlobalServiceCheckgen = _UpsDiagnosticGlobalServiceCheckgen_Object(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 12, 7),
    _UpsDiagnosticGlobalServiceCheckgen_Type()
)
upsDiagnosticGlobalServiceCheckgen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsDiagnosticGlobalServiceCheckgen.setStatus("current")
_GeDevices_ObjectIdentity = ObjectIdentity
geDevices = _GeDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 100)
)
_GeDevicesDescriptions_ObjectIdentity = ObjectIdentity
geDevicesDescriptions = _GeDevicesDescriptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 100, 1)
)
_AdvSNMPWebIntCard_ObjectIdentity = ObjectIdentity
advSNMPWebIntCard = _AdvSNMPWebIntCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 100, 1, 1)
)
_SnmpWebIntCard_ObjectIdentity = ObjectIdentity
snmpWebIntCard = _SnmpWebIntCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 100, 1, 2)
)
_SnmpWebIntBox_ObjectIdentity = ObjectIdentity
snmpWebIntBox = _SnmpWebIntBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 818, 1, 100, 1, 3)
)

# Managed Objects groups


# Notification objects

upsTrapAlarmBatteryBadgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 1)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadgen.setStatus(
        "current"
    )

upsTrapAlarmOnBatterygen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 2)
)
upsTrapAlarmOnBatterygen.setObjects(
    ("GESINGLEUPS-MIB", "upsSecondsOnBatterygen")
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatterygen.setStatus(
        "current"
    )

upsTrapAlarmLowBatterygen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 3)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatterygen.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatterygen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 4)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatterygen.setStatus(
        "current"
    )

upsTrapAlarmTempBadgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 5)
)
upsTrapAlarmTempBadgen.setObjects(
    ("GESINGLEUPS-MIB", "upsBatteryTemperaturegen")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadgen.setStatus(
        "current"
    )

upsTrapAlarmInputBadgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 6)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadgen.setStatus(
        "current"
    )

upsTrapAlarmOutputBadgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 7)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadgen.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 8)
)
upsTrapAlarmOutputOverloadgen.setObjects(
      *(("GESINGLEUPS-MIB", "upsOutputNumLinesgen"),
        ("GESINGLEUPS-MIB", "upsOutputPercentLoadgen"))
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadgen.setStatus(
        "current"
    )

upsTrapAlarmOnBypassgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 9)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassgen.setStatus(
        "current"
    )

upsTrapAlarmBypassBadgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 10)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadgen.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 11)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedgen.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 12)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedgen.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 13)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedgen.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOffgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 14)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOffgen.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOffgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 15)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOffgen.setStatus(
        "current"
    )

upsTrapAlarmFanFailuregen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 16)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailuregen.setStatus(
        "current"
    )

upsTrapAlarmFuseFailuregen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 17)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailuregen.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 18)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultgen.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 19)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedgen.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 20)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostgen.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowergen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 21)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowergen.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendinggen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 22)
)
upsTrapAlarmShutdownPendinggen.setObjects(
    ("GESINGLEUPS-MIB", "upsShutdownAfterDelaygen")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendinggen.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 23)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentgen.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 24)
)
upsTrapAlarmTestInProgressgen.setObjects(
    ("GESINGLEUPS-MIB", "upsTestIdgen")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressgen.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOffgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 25)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOffgen.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusFailuregen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 26)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusFailuregen.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCFailuregen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 27)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCFailuregen.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusFailuregen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 28)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusFailuregen.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCFailuregen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 29)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCFailuregen.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingFailuregen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 30)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingFailuregen.setStatus(
        "current"
    )

upsTrapAlarmDCRippleFailuregen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 31)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleFailuregen.setStatus(
        "current"
    )

upsTrapAlarmBatteryBadRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 33)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBatteryBadRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmOnBatteryRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 34)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBatteryRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmLowBatteryRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 35)
)
if mibBuilder.loadTexts:
    upsTrapAlarmLowBatteryRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmDepletedBatteryRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 36)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDepletedBatteryRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmTempBadRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 37)
)
if mibBuilder.loadTexts:
    upsTrapAlarmTempBadRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmInputBadRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 38)
)
if mibBuilder.loadTexts:
    upsTrapAlarmInputBadRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmOutputBadRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 39)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputBadRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmOutputOverloadRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 40)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOverloadRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmOnBypassRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 41)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOnBypassRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmBypassBadRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 42)
)
if mibBuilder.loadTexts:
    upsTrapAlarmBypassBadRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmOutputOffAsRequestedRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 43)
)
if mibBuilder.loadTexts:
    upsTrapAlarmOutputOffAsRequestedRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmUpsOffAsRequestedRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 44)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOffAsRequestedRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmChargerFailedRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 45)
)
if mibBuilder.loadTexts:
    upsTrapAlarmChargerFailedRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmUpsOutputOngen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 46)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsOutputOngen.setStatus(
        "current"
    )

upsTrapAlarmUpsSystemOngen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 47)
)
if mibBuilder.loadTexts:
    upsTrapAlarmUpsSystemOngen.setStatus(
        "current"
    )

upsTrapAlarmFanFailureRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 48)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFanFailureRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmFuseFailureRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 49)
)
if mibBuilder.loadTexts:
    upsTrapAlarmFuseFailureRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmGeneralFaultRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 50)
)
if mibBuilder.loadTexts:
    upsTrapAlarmGeneralFaultRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmDiagnosticTestFailedRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 51)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDiagnosticTestFailedRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmCommunicationsLostRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 52)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCommunicationsLostRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmAwaitingPowerRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 53)
)
if mibBuilder.loadTexts:
    upsTrapAlarmAwaitingPowerRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmShutdownPendingRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 54)
)
upsTrapAlarmShutdownPendingRestoredgen.setObjects(
    ("GESINGLEUPS-MIB", "upsShutdownAfterDelaygen")
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownPendingRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmShutdownImminentRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 55)
)
if mibBuilder.loadTexts:
    upsTrapAlarmShutdownImminentRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmTestInProgressRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 56)
)
upsTrapAlarmTestInProgressRestoredgen.setObjects(
    ("GESINGLEUPS-MIB", "upsTestIdgen")
)
if mibBuilder.loadTexts:
    upsTrapAlarmTestInProgressRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmReceptacleOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 57)
)
if mibBuilder.loadTexts:
    upsTrapAlarmReceptacleOn.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 58)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJACRCRestoredAgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 59)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJACRCRestoredAgen.setStatus(
        "current"
    )

upsTrapAlarmConnectivityBusRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 60)
)
if mibBuilder.loadTexts:
    upsTrapAlarmConnectivityBusRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmHighspeedBusJBCRCRestoredBgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 61)
)
if mibBuilder.loadTexts:
    upsTrapAlarmHighspeedBusJBCRCRestoredBgen.setStatus(
        "current"
    )

upsTrapAlarmCurrentSharingRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 62)
)
if mibBuilder.loadTexts:
    upsTrapAlarmCurrentSharingRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmDCRippleRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 63)
)
if mibBuilder.loadTexts:
    upsTrapAlarmDCRippleRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmValueLowgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 129)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowgen.setStatus(
        "current"
    )

upsTrapAlarmValueHighgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 130)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighgen.setStatus(
        "current"
    )

upsTrapAlarmValueLowRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 133)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueLowRestoredgen.setStatus(
        "current"
    )

upsTrapAlarmValueHighRestoredgen = NotificationType(
    (1, 3, 6, 1, 4, 1, 818, 1, 1, 10, 11, 134)
)
if mibBuilder.loadTexts:
    upsTrapAlarmValueHighRestoredgen.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GESINGLEUPS-MIB",
    **{"PositiveInteger32": PositiveInteger32,
       "NonNegativeInteger32": NonNegativeInteger32,
       "imv": imv,
       "geHardware": geHardware,
       "geUPS": geUPS,
       "geDiscoveredUPSsMask": geDiscoveredUPSsMask,
       "geRequestPacket": geRequestPacket,
       "geReplyPacket": geReplyPacket,
       "geGenericUPS": geGenericUPS,
       "upsIdentgen": upsIdentgen,
       "upsIdentManufacturergen": upsIdentManufacturergen,
       "upsIdentModelgen": upsIdentModelgen,
       "upsIdentUPSSoftwareVersiongen": upsIdentUPSSoftwareVersiongen,
       "upsIdentAgentSoftwareVersiongen": upsIdentAgentSoftwareVersiongen,
       "upsIdentNamegen": upsIdentNamegen,
       "upsIdentAttachedDevicesgen": upsIdentAttachedDevicesgen,
       "upsIdentUPSSerialNumbergen": upsIdentUPSSerialNumbergen,
       "upsIdentComProtVersiongen": upsIdentComProtVersiongen,
       "upsIdentOperatingTimegen": upsIdentOperatingTimegen,
       "upsBatterygen": upsBatterygen,
       "upsBatteryStatusgen": upsBatteryStatusgen,
       "upsSecondsOnBatterygen": upsSecondsOnBatterygen,
       "upsEstimatedMinutesRemaininggen": upsEstimatedMinutesRemaininggen,
       "upsEstimatedChargeRemaininggen": upsEstimatedChargeRemaininggen,
       "upsBatteryVoltagegen": upsBatteryVoltagegen,
       "upsBatteryCurrentgen": upsBatteryCurrentgen,
       "upsBatteryTemperaturegen": upsBatteryTemperaturegen,
       "upsBatteryRipplegen": upsBatteryRipplegen,
       "upsInputgen": upsInputgen,
       "upsInputLineBadsgen": upsInputLineBadsgen,
       "upsInputNumLinesgen": upsInputNumLinesgen,
       "upsInputGenTable": upsInputGenTable,
       "upsInputGenEntry": upsInputGenEntry,
       "upsInputLineIndexgen": upsInputLineIndexgen,
       "upsInputFrequencygen": upsInputFrequencygen,
       "upsInputVoltagegen": upsInputVoltagegen,
       "upsInputCurrentgen": upsInputCurrentgen,
       "upsInputTruePowergen": upsInputTruePowergen,
       "upsInputVoltageMingen": upsInputVoltageMingen,
       "upsInputVoltageMaxgen": upsInputVoltageMaxgen,
       "upsOutputgen": upsOutputgen,
       "upsOutputSourcegen": upsOutputSourcegen,
       "upsOutputFrequencygen": upsOutputFrequencygen,
       "upsOutputNumLinesgen": upsOutputNumLinesgen,
       "upsOutputGenTable": upsOutputGenTable,
       "upsOutputGenEntry": upsOutputGenEntry,
       "upsOutputLineIndexgen": upsOutputLineIndexgen,
       "upsOutputVoltagegen": upsOutputVoltagegen,
       "upsOutputCurrentgen": upsOutputCurrentgen,
       "upsOutputPowergen": upsOutputPowergen,
       "upsOutputPercentLoadgen": upsOutputPercentLoadgen,
       "upsOutputPowerFactorgen": upsOutputPowerFactorgen,
       "upsOutputPeakCurrentgen": upsOutputPeakCurrentgen,
       "upsOutputShareCurrentgen": upsOutputShareCurrentgen,
       "upsBypassgen": upsBypassgen,
       "upsBypassFrequencygen": upsBypassFrequencygen,
       "upsBypassNumLinesgen": upsBypassNumLinesgen,
       "upsBypassGenTable": upsBypassGenTable,
       "upsBypassGenEntry": upsBypassGenEntry,
       "upsBypassLineIndexgen": upsBypassLineIndexgen,
       "upsBypassVoltagegen": upsBypassVoltagegen,
       "upsBypassCurrentgen": upsBypassCurrentgen,
       "upsBypassPowergen": upsBypassPowergen,
       "upsAlarmgen": upsAlarmgen,
       "upsAlarmsPresentgen": upsAlarmsPresentgen,
       "upsAlarmGenTable": upsAlarmGenTable,
       "upsAlarmGenEntry": upsAlarmGenEntry,
       "upsAlarmIdgen": upsAlarmIdgen,
       "upsAlarmDescrgen": upsAlarmDescrgen,
       "upsAlarmTimegen": upsAlarmTimegen,
       "upsWellKnownAlarmsgen": upsWellKnownAlarmsgen,
       "upsAlarmBatteryBadgen": upsAlarmBatteryBadgen,
       "upsAlarmOnBatterygen": upsAlarmOnBatterygen,
       "upsAlarmLowBatterygen": upsAlarmLowBatterygen,
       "upsAlarmDepletedBatterygen": upsAlarmDepletedBatterygen,
       "upsAlarmTempBadgen": upsAlarmTempBadgen,
       "upsAlarmInputBadgen": upsAlarmInputBadgen,
       "upsAlarmOutputBadgen": upsAlarmOutputBadgen,
       "upsAlarmOutputOverloadgen": upsAlarmOutputOverloadgen,
       "upsAlarmOnBypassgen": upsAlarmOnBypassgen,
       "upsAlarmBypassBadgen": upsAlarmBypassBadgen,
       "upsAlarmOutputOffAsRequestedgen": upsAlarmOutputOffAsRequestedgen,
       "upsAlarmUpsOffAsRequestedgen": upsAlarmUpsOffAsRequestedgen,
       "upsAlarmChargerFailedgen": upsAlarmChargerFailedgen,
       "upsAlarmUpsOutputOffgen": upsAlarmUpsOutputOffgen,
       "upsAlarmUpsSystemOffgen": upsAlarmUpsSystemOffgen,
       "upsAlarmFanFailuregen": upsAlarmFanFailuregen,
       "upsAlarmFuseFailuregen": upsAlarmFuseFailuregen,
       "upsAlarmGeneralFaultgen": upsAlarmGeneralFaultgen,
       "upsAlarmDiagnosticTestFailedgen": upsAlarmDiagnosticTestFailedgen,
       "upsAlarmCommunicationsLostgen": upsAlarmCommunicationsLostgen,
       "upsAlarmAwaitingPowergen": upsAlarmAwaitingPowergen,
       "upsAlarmShutdownPendinggen": upsAlarmShutdownPendinggen,
       "upsAlarmShutdownImminentgen": upsAlarmShutdownImminentgen,
       "upsAlarmTestInProgressgen": upsAlarmTestInProgressgen,
       "upsAlarmReceptacleOffgen": upsAlarmReceptacleOffgen,
       "upsAlarmHighSpeedBusFailuregen": upsAlarmHighSpeedBusFailuregen,
       "upsAlarmHighSpeedBusJACRCFailuregen": upsAlarmHighSpeedBusJACRCFailuregen,
       "upsAlarmConnectivityBusFailuregen": upsAlarmConnectivityBusFailuregen,
       "upsAlarmHighSpeedBusJBCRCFailuregen": upsAlarmHighSpeedBusJBCRCFailuregen,
       "upsAlarmCurrentSharinggen": upsAlarmCurrentSharinggen,
       "upsAlarmDCRipplegen": upsAlarmDCRipplegen,
       "upsAlarmMaskAgen": upsAlarmMaskAgen,
       "upsTestgen": upsTestgen,
       "upsTestIdgen": upsTestIdgen,
       "upsTestSpinLockgen": upsTestSpinLockgen,
       "upsTestResultsSummarygen": upsTestResultsSummarygen,
       "upsTestResultsDetailgen": upsTestResultsDetailgen,
       "upsTestStartTimegen": upsTestStartTimegen,
       "upsTestElapsedTimegen": upsTestElapsedTimegen,
       "upsWellKnownTestsgen": upsWellKnownTestsgen,
       "upsTestNoTestsInitiatedgen": upsTestNoTestsInitiatedgen,
       "upsTestAbortTestInProgressgen": upsTestAbortTestInProgressgen,
       "upsTestGeneralSystemsTestgen": upsTestGeneralSystemsTestgen,
       "upsTestQuickBatteryTestgen": upsTestQuickBatteryTestgen,
       "upsTestDeepBatteryCalibrationgen": upsTestDeepBatteryCalibrationgen,
       "upsControlgen": upsControlgen,
       "upsShutdownTypegen": upsShutdownTypegen,
       "upsShutdownAfterDelaygen": upsShutdownAfterDelaygen,
       "upsStartupAfterDelaygen": upsStartupAfterDelaygen,
       "upsRebootWithDurationgen": upsRebootWithDurationgen,
       "upsAutoRestartgen": upsAutoRestartgen,
       "upsReceptaclesNumgen": upsReceptaclesNumgen,
       "upsReceptacleGenTable": upsReceptacleGenTable,
       "upsReceptacleGenEntry": upsReceptacleGenEntry,
       "upsReceptacleLineIndexgen": upsReceptacleLineIndexgen,
       "upsReceptacleOnOffgen": upsReceptacleOnOffgen,
       "upsUPSModegen": upsUPSModegen,
       "upsRectifierOnOffgen": upsRectifierOnOffgen,
       "upsBatteryChargeMethodgen": upsBatteryChargeMethodgen,
       "upsInverterOnOffgen": upsInverterOnOffgen,
       "upsBypassOnOffgen": upsBypassOnOffgen,
       "upsLoadSourcegen": upsLoadSourcegen,
       "upsConfiggen": upsConfiggen,
       "upsConfigInputVoltagegen": upsConfigInputVoltagegen,
       "upsConfigInputFreqgen": upsConfigInputFreqgen,
       "upsConfigOutputVoltagegen": upsConfigOutputVoltagegen,
       "upsConfigOutputFreqgen": upsConfigOutputFreqgen,
       "upsConfigOutputVAgen": upsConfigOutputVAgen,
       "upsConfigOutputPowergen": upsConfigOutputPowergen,
       "upsConfigLowBattTimegen": upsConfigLowBattTimegen,
       "upsConfigAudibleStatusgen": upsConfigAudibleStatusgen,
       "upsConfigLowVoltageTransferPointgen": upsConfigLowVoltageTransferPointgen,
       "upsConfigHighVoltageTransferPointgen": upsConfigHighVoltageTransferPointgen,
       "upsConfigBatteryCapacitygen": upsConfigBatteryCapacitygen,
       "upsConfigBatteryChargeCurrentgen": upsConfigBatteryChargeCurrentgen,
       "upsConfigNoLoadShutdowngen": upsConfigNoLoadShutdowngen,
       "upsConfigStartDelaygen": upsConfigStartDelaygen,
       "upsGetSetgen": upsGetSetgen,
       "upsEventGetNextgen": upsEventGetNextgen,
       "upsEventGetPreviousgen": upsEventGetPreviousgen,
       "upsEventSetStartingTimeStampgen": upsEventSetStartingTimeStampgen,
       "upsEventRetreiveCurrentTimeStampgen": upsEventRetreiveCurrentTimeStampgen,
       "upsEventTableSizegen": upsEventTableSizegen,
       "upsEventGenTable": upsEventGenTable,
       "upsEventGenEntry": upsEventGenEntry,
       "upsEventLineIndexgen": upsEventLineIndexgen,
       "upsEventCodegen": upsEventCodegen,
       "upsEventStatusgen": upsEventStatusgen,
       "upsEventTimegen": upsEventTimegen,
       "upsParametersReadgen": upsParametersReadgen,
       "upsParametersWritegen": upsParametersWritegen,
       "upsParametersStartAddressgen": upsParametersStartAddressgen,
       "upsParameterTableSizegen": upsParameterTableSizegen,
       "upsParameterGenTable": upsParameterGenTable,
       "upsParameterGenEntry": upsParameterGenEntry,
       "upsParameterLineIndexgen": upsParameterLineIndexgen,
       "upsParameterValuegen": upsParameterValuegen,
       "upsStatusgen": upsStatusgen,
       "upsMainsStatisticsMBfailgen": upsMainsStatisticsMBfailgen,
       "upsMainsStatisticsMRfailgen": upsMainsStatisticsMRfailgen,
       "upsMainsStatisticsB2gen": upsMainsStatisticsB2gen,
       "upsMainsStatisticsB5gen": upsMainsStatisticsB5gen,
       "upsMainsStatisticsB10gen": upsMainsStatisticsB10gen,
       "upsMainsStatisticsB200gen": upsMainsStatisticsB200gen,
       "upsMainsStatisticsBypRelgen": upsMainsStatisticsBypRelgen,
       "upsTimegen": upsTimegen,
       "upsRequestPermissiongen": upsRequestPermissiongen,
       "upsEventGetCodegen": upsEventGetCodegen,
       "upsEventSpinLockgen": upsEventSpinLockgen,
       "upsParameterSpinLockgen": upsParameterSpinLockgen,
       "geUPSTrapsgen": geUPSTrapsgen,
       "upsTrapAlarmBatteryBadgen": upsTrapAlarmBatteryBadgen,
       "upsTrapAlarmOnBatterygen": upsTrapAlarmOnBatterygen,
       "upsTrapAlarmLowBatterygen": upsTrapAlarmLowBatterygen,
       "upsTrapAlarmDepletedBatterygen": upsTrapAlarmDepletedBatterygen,
       "upsTrapAlarmTempBadgen": upsTrapAlarmTempBadgen,
       "upsTrapAlarmInputBadgen": upsTrapAlarmInputBadgen,
       "upsTrapAlarmOutputBadgen": upsTrapAlarmOutputBadgen,
       "upsTrapAlarmOutputOverloadgen": upsTrapAlarmOutputOverloadgen,
       "upsTrapAlarmOnBypassgen": upsTrapAlarmOnBypassgen,
       "upsTrapAlarmBypassBadgen": upsTrapAlarmBypassBadgen,
       "upsTrapAlarmOutputOffAsRequestedgen": upsTrapAlarmOutputOffAsRequestedgen,
       "upsTrapAlarmUpsOffAsRequestedgen": upsTrapAlarmUpsOffAsRequestedgen,
       "upsTrapAlarmChargerFailedgen": upsTrapAlarmChargerFailedgen,
       "upsTrapAlarmUpsOutputOffgen": upsTrapAlarmUpsOutputOffgen,
       "upsTrapAlarmUpsSystemOffgen": upsTrapAlarmUpsSystemOffgen,
       "upsTrapAlarmFanFailuregen": upsTrapAlarmFanFailuregen,
       "upsTrapAlarmFuseFailuregen": upsTrapAlarmFuseFailuregen,
       "upsTrapAlarmGeneralFaultgen": upsTrapAlarmGeneralFaultgen,
       "upsTrapAlarmDiagnosticTestFailedgen": upsTrapAlarmDiagnosticTestFailedgen,
       "upsTrapAlarmCommunicationsLostgen": upsTrapAlarmCommunicationsLostgen,
       "upsTrapAlarmAwaitingPowergen": upsTrapAlarmAwaitingPowergen,
       "upsTrapAlarmShutdownPendinggen": upsTrapAlarmShutdownPendinggen,
       "upsTrapAlarmShutdownImminentgen": upsTrapAlarmShutdownImminentgen,
       "upsTrapAlarmTestInProgressgen": upsTrapAlarmTestInProgressgen,
       "upsTrapAlarmReceptacleOffgen": upsTrapAlarmReceptacleOffgen,
       "upsTrapAlarmHighspeedBusFailuregen": upsTrapAlarmHighspeedBusFailuregen,
       "upsTrapAlarmHighspeedBusJACRCFailuregen": upsTrapAlarmHighspeedBusJACRCFailuregen,
       "upsTrapAlarmConnectivityBusFailuregen": upsTrapAlarmConnectivityBusFailuregen,
       "upsTrapAlarmHighspeedBusJBCRCFailuregen": upsTrapAlarmHighspeedBusJBCRCFailuregen,
       "upsTrapAlarmCurrentSharingFailuregen": upsTrapAlarmCurrentSharingFailuregen,
       "upsTrapAlarmDCRippleFailuregen": upsTrapAlarmDCRippleFailuregen,
       "upsTrapAlarmBatteryBadRestoredgen": upsTrapAlarmBatteryBadRestoredgen,
       "upsTrapAlarmOnBatteryRestoredgen": upsTrapAlarmOnBatteryRestoredgen,
       "upsTrapAlarmLowBatteryRestoredgen": upsTrapAlarmLowBatteryRestoredgen,
       "upsTrapAlarmDepletedBatteryRestoredgen": upsTrapAlarmDepletedBatteryRestoredgen,
       "upsTrapAlarmTempBadRestoredgen": upsTrapAlarmTempBadRestoredgen,
       "upsTrapAlarmInputBadRestoredgen": upsTrapAlarmInputBadRestoredgen,
       "upsTrapAlarmOutputBadRestoredgen": upsTrapAlarmOutputBadRestoredgen,
       "upsTrapAlarmOutputOverloadRestoredgen": upsTrapAlarmOutputOverloadRestoredgen,
       "upsTrapAlarmOnBypassRestoredgen": upsTrapAlarmOnBypassRestoredgen,
       "upsTrapAlarmBypassBadRestoredgen": upsTrapAlarmBypassBadRestoredgen,
       "upsTrapAlarmOutputOffAsRequestedRestoredgen": upsTrapAlarmOutputOffAsRequestedRestoredgen,
       "upsTrapAlarmUpsOffAsRequestedRestoredgen": upsTrapAlarmUpsOffAsRequestedRestoredgen,
       "upsTrapAlarmChargerFailedRestoredgen": upsTrapAlarmChargerFailedRestoredgen,
       "upsTrapAlarmUpsOutputOngen": upsTrapAlarmUpsOutputOngen,
       "upsTrapAlarmUpsSystemOngen": upsTrapAlarmUpsSystemOngen,
       "upsTrapAlarmFanFailureRestoredgen": upsTrapAlarmFanFailureRestoredgen,
       "upsTrapAlarmFuseFailureRestoredgen": upsTrapAlarmFuseFailureRestoredgen,
       "upsTrapAlarmGeneralFaultRestoredgen": upsTrapAlarmGeneralFaultRestoredgen,
       "upsTrapAlarmDiagnosticTestFailedRestoredgen": upsTrapAlarmDiagnosticTestFailedRestoredgen,
       "upsTrapAlarmCommunicationsLostRestoredgen": upsTrapAlarmCommunicationsLostRestoredgen,
       "upsTrapAlarmAwaitingPowerRestoredgen": upsTrapAlarmAwaitingPowerRestoredgen,
       "upsTrapAlarmShutdownPendingRestoredgen": upsTrapAlarmShutdownPendingRestoredgen,
       "upsTrapAlarmShutdownImminentRestoredgen": upsTrapAlarmShutdownImminentRestoredgen,
       "upsTrapAlarmTestInProgressRestoredgen": upsTrapAlarmTestInProgressRestoredgen,
       "upsTrapAlarmReceptacleOn": upsTrapAlarmReceptacleOn,
       "upsTrapAlarmHighspeedBusRestoredgen": upsTrapAlarmHighspeedBusRestoredgen,
       "upsTrapAlarmHighspeedBusJACRCRestoredAgen": upsTrapAlarmHighspeedBusJACRCRestoredAgen,
       "upsTrapAlarmConnectivityBusRestoredgen": upsTrapAlarmConnectivityBusRestoredgen,
       "upsTrapAlarmHighspeedBusJBCRCRestoredBgen": upsTrapAlarmHighspeedBusJBCRCRestoredBgen,
       "upsTrapAlarmCurrentSharingRestoredgen": upsTrapAlarmCurrentSharingRestoredgen,
       "upsTrapAlarmDCRippleRestoredgen": upsTrapAlarmDCRippleRestoredgen,
       "upsTrapAlarmValueLowgen": upsTrapAlarmValueLowgen,
       "upsTrapAlarmValueHighgen": upsTrapAlarmValueHighgen,
       "upsTrapAlarmValueLowRestoredgen": upsTrapAlarmValueLowRestoredgen,
       "upsTrapAlarmValueHighRestoredgen": upsTrapAlarmValueHighRestoredgen,
       "upsDiagnosticgen": upsDiagnosticgen,
       "upsDiagnosticBusJACommunicationStatusgen": upsDiagnosticBusJACommunicationStatusgen,
       "upsDiagnosticBusJBCommunicationStatusgen": upsDiagnosticBusJBCommunicationStatusgen,
       "upsDiagnosticBatteryLifetimegen": upsDiagnosticBatteryLifetimegen,
       "upsDiagnosticFansLifetimegen": upsDiagnosticFansLifetimegen,
       "upsDiagnosticDCcapacitorsLifetimegen": upsDiagnosticDCcapacitorsLifetimegen,
       "upsDiagnosticACcapacitorsLifetimegen": upsDiagnosticACcapacitorsLifetimegen,
       "upsDiagnosticGlobalServiceCheckgen": upsDiagnosticGlobalServiceCheckgen,
       "geDevices": geDevices,
       "geDevicesDescriptions": geDevicesDescriptions,
       "advSNMPWebIntCard": advSNMPWebIntCard,
       "snmpWebIntCard": snmpWebIntCard,
       "snmpWebIntBox": snmpWebIntBox}
)
