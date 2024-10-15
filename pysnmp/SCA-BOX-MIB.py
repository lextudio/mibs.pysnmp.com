# SNMP MIB module (SCA-BOX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCA-BOX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:50 2024
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

(scanet,) = mibBuilder.importSymbols(
    "SCANET-MIB",
    "scanet")

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

_Box_ObjectIdentity = ObjectIdentity
box = _Box_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 3)
)
_Enclosure_ObjectIdentity = ObjectIdentity
enclosure = _Enclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 3, 1)
)
_Led_Type = OctetString
_Led_Object = MibScalar
led = _Led_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 1),
    _Led_Type()
)
led.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    led.setStatus("mandatory")


class _Fan_Type(Integer32):
    """Custom type fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("fanFailure", 1)
    )


_Fan_Type.__name__ = "Integer32"
_Fan_Object = MibScalar
fan = _Fan_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 2),
    _Fan_Type()
)
fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fan.setStatus("mandatory")


class _Power_Type(Integer32):
    """Custom type power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("power1Failure", 1),
          ("power2Failure", 2),
          ("power3Failure", 4),
          ("power4Failure", 8),
          ("power5Failure", 16),
          ("power6Failure", 32))
    )


_Power_Type.__name__ = "Integer32"
_Power_Object = MibScalar
power = _Power_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 3),
    _Power_Type()
)
power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power.setStatus("mandatory")


class _Slots_Type(Integer32):
    """Custom type slots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              14,
              17)
        )
    )
    namedValues = NamedValues(
        *(("slot-14", 14),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-5", 5))
    )


_Slots_Type.__name__ = "Integer32"
_Slots_Object = MibScalar
slots = _Slots_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 4),
    _Slots_Type()
)
slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slots.setStatus("mandatory")
_Slotmap_Type = OctetString
_Slotmap_Object = MibScalar
slotmap = _Slotmap_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 5),
    _Slotmap_Type()
)
slotmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotmap.setStatus("mandatory")


class _Temperature_Type(Integer32):
    """Custom type temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("temperatureFailure", 1)
    )


_Temperature_Type.__name__ = "Integer32"
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 6),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("mandatory")
_FanNo_Type = Integer32
_FanNo_Object = MibScalar
fanNo = _FanNo_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 7),
    _FanNo_Type()
)
fanNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNo.setStatus("mandatory")
_PowerNo_Type = Integer32
_PowerNo_Object = MibScalar
powerNo = _PowerNo_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 8),
    _PowerNo_Type()
)
powerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerNo.setStatus("mandatory")


class _TemperatureNo_Type(Integer32):
    """Custom type temperatureNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_TemperatureNo_Type.__name__ = "Integer32"
_TemperatureNo_Object = MibScalar
temperatureNo = _TemperatureNo_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 9),
    _TemperatureNo_Type()
)
temperatureNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureNo.setStatus("mandatory")
_FanPresent_Type = Integer32
_FanPresent_Object = MibScalar
fanPresent = _FanPresent_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 10),
    _FanPresent_Type()
)
fanPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanPresent.setStatus("mandatory")
_PowerPresent_Type = Integer32
_PowerPresent_Object = MibScalar
powerPresent = _PowerPresent_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 11),
    _PowerPresent_Type()
)
powerPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPresent.setStatus("mandatory")


class _TemperaturePresent_Type(Integer32):
    """Custom type temperaturePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_TemperaturePresent_Type.__name__ = "Integer32"
_TemperaturePresent_Object = MibScalar
temperaturePresent = _TemperaturePresent_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 12),
    _TemperaturePresent_Type()
)
temperaturePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperaturePresent.setStatus("mandatory")


class _PsuFail_Type(Integer32):
    """Custom type psuFail based on Integer32"""
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
        *(("psu1Failure", 1),
          ("psu2Failure", 2),
          ("psu3Failure", 3),
          ("psu4Failure", 4),
          ("psu5Failure", 5),
          ("psu6Failure", 6))
    )


_PsuFail_Type.__name__ = "Integer32"
_PsuFail_Object = MibScalar
psuFail = _PsuFail_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 13),
    _PsuFail_Type()
)
psuFail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psuFail.setStatus("mandatory")
_SlotmapFail_Type = Integer32
_SlotmapFail_Object = MibScalar
slotmapFail = _SlotmapFail_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 1, 14),
    _SlotmapFail_Type()
)
slotmapFail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slotmapFail.setStatus("mandatory")
_Boards_ObjectIdentity = ObjectIdentity
boards = _Boards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 3, 2)
)
_BrdInfoTable_Object = MibTable
brdInfoTable = _BrdInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1)
)
if mibBuilder.loadTexts:
    brdInfoTable.setStatus("mandatory")
_BrdInfoEntry_Object = MibTableRow
brdInfoEntry = _BrdInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1)
)
brdInfoEntry.setIndexNames(
    (0, "SCA-BOX-MIB", "brdNumber1"),
)
if mibBuilder.loadTexts:
    brdInfoEntry.setStatus("mandatory")
_BrdNumber1_Type = Integer32
_BrdNumber1_Object = MibTableColumn
brdNumber1 = _BrdNumber1_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 1),
    _BrdNumber1_Type()
)
brdNumber1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdNumber1.setStatus("mandatory")
_CardType_Type = Integer32
_CardType_Object = MibTableColumn
cardType = _CardType_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 2),
    _CardType_Type()
)
cardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardType.setStatus("mandatory")
_PcbRevision_Type = Integer32
_PcbRevision_Object = MibTableColumn
pcbRevision = _PcbRevision_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 3),
    _PcbRevision_Type()
)
pcbRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcbRevision.setStatus("mandatory")
_MacAddress_Type = OctetString
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 4),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("mandatory")
_DriverSeq_Type = Integer32
_DriverSeq_Object = MibTableColumn
driverSeq = _DriverSeq_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 5),
    _DriverSeq_Type()
)
driverSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverSeq.setStatus("mandatory")


class _Product_Type(DisplayString):
    """Custom type product based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Product_Type.__name__ = "DisplayString"
_Product_Object = MibTableColumn
product = _Product_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 6),
    _Product_Type()
)
product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    product.setStatus("mandatory")


class _SerialNumber_Type(OctetString):
    """Custom type serialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialNumber_Type.__name__ = "OctetString"
_SerialNumber_Object = MibTableColumn
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 7),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")
_MasterSlave_Type = Integer32
_MasterSlave_Object = MibTableColumn
masterSlave = _MasterSlave_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 8),
    _MasterSlave_Type()
)
masterSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterSlave.setStatus("mandatory")
_Ram_Type = Integer32
_Ram_Object = MibTableColumn
ram = _Ram_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 9),
    _Ram_Type()
)
ram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ram.setStatus("mandatory")
_Shram_Type = Integer32
_Shram_Object = MibTableColumn
shram = _Shram_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 10),
    _Shram_Type()
)
shram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shram.setStatus("mandatory")
_Eprom_Type = Integer32
_Eprom_Object = MibTableColumn
eprom = _Eprom_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 11),
    _Eprom_Type()
)
eprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eprom.setStatus("mandatory")
_E2prom_Type = Integer32
_E2prom_Object = MibTableColumn
e2prom = _E2prom_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 12),
    _E2prom_Type()
)
e2prom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e2prom.setStatus("mandatory")
_Flashprom_Type = Integer32
_Flashprom_Object = MibTableColumn
flashprom = _Flashprom_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 13),
    _Flashprom_Type()
)
flashprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashprom.setStatus("mandatory")
_Spec0_Type = OctetString
_Spec0_Object = MibTableColumn
spec0 = _Spec0_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 14),
    _Spec0_Type()
)
spec0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spec0.setStatus("mandatory")
_Spec1_Type = OctetString
_Spec1_Object = MibTableColumn
spec1 = _Spec1_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 15),
    _Spec1_Type()
)
spec1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spec1.setStatus("mandatory")
_Spec2_Type = OctetString
_Spec2_Object = MibTableColumn
spec2 = _Spec2_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 16),
    _Spec2_Type()
)
spec2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spec2.setStatus("mandatory")
_Spec3_Type = OctetString
_Spec3_Object = MibTableColumn
spec3 = _Spec3_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 17),
    _Spec3_Type()
)
spec3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spec3.setStatus("mandatory")
_IpAddr_Type = IpAddress
_IpAddr_Object = MibTableColumn
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 18),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddr.setStatus("mandatory")
_Nsap_Type = OctetString
_Nsap_Object = MibTableColumn
nsap = _Nsap_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 19),
    _Nsap_Type()
)
nsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsap.setStatus("mandatory")
_BrdStatusTable_Object = MibTable
brdStatusTable = _BrdStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 2)
)
if mibBuilder.loadTexts:
    brdStatusTable.setStatus("mandatory")
_BrdStatusEntry_Object = MibTableRow
brdStatusEntry = _BrdStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 2, 1)
)
brdStatusEntry.setIndexNames(
    (0, "SCA-BOX-MIB", "brdNumber2"),
)
if mibBuilder.loadTexts:
    brdStatusEntry.setStatus("mandatory")
_BrdNumber2_Type = Integer32
_BrdNumber2_Object = MibTableColumn
brdNumber2 = _BrdNumber2_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 2, 1, 1),
    _BrdNumber2_Type()
)
brdNumber2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdNumber2.setStatus("mandatory")
_BrdStatus_Type = Integer32
_BrdStatus_Object = MibTableColumn
brdStatus = _BrdStatus_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 2, 1, 2),
    _BrdStatus_Type()
)
brdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdStatus.setStatus("mandatory")
_BrdLed_Type = OctetString
_BrdLed_Object = MibTableColumn
brdLed = _BrdLed_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 2, 1, 3),
    _BrdLed_Type()
)
brdLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdLed.setStatus("mandatory")
_BrdPlugTable_Object = MibTable
brdPlugTable = _BrdPlugTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 3)
)
if mibBuilder.loadTexts:
    brdPlugTable.setStatus("mandatory")
_BrdPlugEntry_Object = MibTableRow
brdPlugEntry = _BrdPlugEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1)
)
brdPlugEntry.setIndexNames(
    (0, "SCA-BOX-MIB", "brdNumber3"),
    (0, "SCA-BOX-MIB", "brdPlugNumber"),
)
if mibBuilder.loadTexts:
    brdPlugEntry.setStatus("mandatory")
_BrdNumber3_Type = Integer32
_BrdNumber3_Object = MibTableColumn
brdNumber3 = _BrdNumber3_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 1),
    _BrdNumber3_Type()
)
brdNumber3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdNumber3.setStatus("mandatory")
_BrdPlugNumber_Type = Integer32
_BrdPlugNumber_Object = MibTableColumn
brdPlugNumber = _BrdPlugNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 2),
    _BrdPlugNumber_Type()
)
brdPlugNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdPlugNumber.setStatus("mandatory")
_BrdPlugPosition_Type = OctetString
_BrdPlugPosition_Object = MibTableColumn
brdPlugPosition = _BrdPlugPosition_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 3),
    _BrdPlugPosition_Type()
)
brdPlugPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdPlugPosition.setStatus("mandatory")


class _BrdPlugStatus_Type(Integer32):
    """Custom type brdPlugStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("notAvailable", 1))
    )


_BrdPlugStatus_Type.__name__ = "Integer32"
_BrdPlugStatus_Object = MibTableColumn
brdPlugStatus = _BrdPlugStatus_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 4),
    _BrdPlugStatus_Type()
)
brdPlugStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdPlugStatus.setStatus("mandatory")
_BrdPlugType_Type = OctetString
_BrdPlugType_Object = MibTableColumn
brdPlugType = _BrdPlugType_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 5),
    _BrdPlugType_Type()
)
brdPlugType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdPlugType.setStatus("mandatory")


class _BrdPlugPimType_Type(OctetString):
    """Custom type brdPlugPimType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_BrdPlugPimType_Type.__name__ = "OctetString"
_BrdPlugPimType_Object = MibTableColumn
brdPlugPimType = _BrdPlugPimType_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 6),
    _BrdPlugPimType_Type()
)
brdPlugPimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdPlugPimType.setStatus("mandatory")
_BrdPlugPimLeds_Type = OctetString
_BrdPlugPimLeds_Object = MibTableColumn
brdPlugPimLeds = _BrdPlugPimLeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 7),
    _BrdPlugPimLeds_Type()
)
brdPlugPimLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdPlugPimLeds.setStatus("mandatory")
_BrdPlugPimOptions_Type = OctetString
_BrdPlugPimOptions_Object = MibTableColumn
brdPlugPimOptions = _BrdPlugPimOptions_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 8),
    _BrdPlugPimOptions_Type()
)
brdPlugPimOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdPlugPimOptions.setStatus("mandatory")
_BrdOptionTable_Object = MibTable
brdOptionTable = _BrdOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 4)
)
if mibBuilder.loadTexts:
    brdOptionTable.setStatus("mandatory")
_BrdOptionEntry_Object = MibTableRow
brdOptionEntry = _BrdOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 4, 1)
)
brdOptionEntry.setIndexNames(
    (0, "SCA-BOX-MIB", "brdNumber4"),
    (0, "SCA-BOX-MIB", "brdOptionNumber"),
)
if mibBuilder.loadTexts:
    brdOptionEntry.setStatus("mandatory")
_BrdNumber4_Type = Integer32
_BrdNumber4_Object = MibTableColumn
brdNumber4 = _BrdNumber4_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 4, 1, 1),
    _BrdNumber4_Type()
)
brdNumber4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdNumber4.setStatus("mandatory")
_BrdOptionNumber_Type = Integer32
_BrdOptionNumber_Object = MibTableColumn
brdOptionNumber = _BrdOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 4, 1, 2),
    _BrdOptionNumber_Type()
)
brdOptionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdOptionNumber.setStatus("mandatory")
_BrdOptionName_Type = OctetString
_BrdOptionName_Object = MibTableColumn
brdOptionName = _BrdOptionName_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 4, 1, 3),
    _BrdOptionName_Type()
)
brdOptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdOptionName.setStatus("mandatory")


class _BrdOptionState_Type(Integer32):
    """Custom type brdOptionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 2),
          ("notInstalled", 1))
    )


_BrdOptionState_Type.__name__ = "Integer32"
_BrdOptionState_Object = MibTableColumn
brdOptionState = _BrdOptionState_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 4, 1, 4),
    _BrdOptionState_Type()
)
brdOptionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdOptionState.setStatus("mandatory")
_BrdSwitchSettingTable_Object = MibTable
brdSwitchSettingTable = _BrdSwitchSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 5)
)
if mibBuilder.loadTexts:
    brdSwitchSettingTable.setStatus("mandatory")
_BrdSwitchSettingEntry_Object = MibTableRow
brdSwitchSettingEntry = _BrdSwitchSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 5, 1)
)
brdSwitchSettingEntry.setIndexNames(
    (0, "SCA-BOX-MIB", "brdNumber5"),
    (0, "SCA-BOX-MIB", "brdSwitchNumber"),
)
if mibBuilder.loadTexts:
    brdSwitchSettingEntry.setStatus("mandatory")
_BrdNumber5_Type = Integer32
_BrdNumber5_Object = MibTableColumn
brdNumber5 = _BrdNumber5_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 5, 1, 1),
    _BrdNumber5_Type()
)
brdNumber5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdNumber5.setStatus("mandatory")
_BrdSwitchNumber_Type = Integer32
_BrdSwitchNumber_Object = MibTableColumn
brdSwitchNumber = _BrdSwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 5, 1, 2),
    _BrdSwitchNumber_Type()
)
brdSwitchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdSwitchNumber.setStatus("mandatory")
_BrdSwitchName_Type = OctetString
_BrdSwitchName_Object = MibTableColumn
brdSwitchName = _BrdSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 5, 1, 3),
    _BrdSwitchName_Type()
)
brdSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdSwitchName.setStatus("mandatory")
_BrdSwitchSetting_Type = OctetString
_BrdSwitchSetting_Object = MibTableColumn
brdSwitchSetting = _BrdSwitchSetting_Object(
    (1, 3, 6, 1, 4, 1, 208, 3, 2, 5, 1, 4),
    _BrdSwitchSetting_Type()
)
brdSwitchSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brdSwitchSetting.setStatus("mandatory")

# Managed Objects groups


# Notification objects

boxPowerFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 3, 0, 1)
)
boxPowerFailureEvent.setObjects(
    ("SCA-BOX-MIB", "psuFail")
)
if mibBuilder.loadTexts:
    boxPowerFailureEvent.setStatus(
        ""
    )

boxFanFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 3, 0, 2)
)
if mibBuilder.loadTexts:
    boxFanFailureEvent.setStatus(
        ""
    )

boxTempFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 3, 0, 3)
)
if mibBuilder.loadTexts:
    boxTempFailureEvent.setStatus(
        ""
    )

boxModuleInsertedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 3, 0, 4)
)
boxModuleInsertedEvent.setObjects(
    ("SCA-BOX-MIB", "slotmapFail")
)
if mibBuilder.loadTexts:
    boxModuleInsertedEvent.setStatus(
        ""
    )

boxModuleRemovedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 3, 0, 5)
)
boxModuleRemovedEvent.setObjects(
    ("SCA-BOX-MIB", "slotmapFail")
)
if mibBuilder.loadTexts:
    boxModuleRemovedEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCA-BOX-MIB",
    **{"box": box,
       "boxPowerFailureEvent": boxPowerFailureEvent,
       "boxFanFailureEvent": boxFanFailureEvent,
       "boxTempFailureEvent": boxTempFailureEvent,
       "boxModuleInsertedEvent": boxModuleInsertedEvent,
       "boxModuleRemovedEvent": boxModuleRemovedEvent,
       "enclosure": enclosure,
       "led": led,
       "fan": fan,
       "power": power,
       "slots": slots,
       "slotmap": slotmap,
       "temperature": temperature,
       "fanNo": fanNo,
       "powerNo": powerNo,
       "temperatureNo": temperatureNo,
       "fanPresent": fanPresent,
       "powerPresent": powerPresent,
       "temperaturePresent": temperaturePresent,
       "psuFail": psuFail,
       "slotmapFail": slotmapFail,
       "boards": boards,
       "brdInfoTable": brdInfoTable,
       "brdInfoEntry": brdInfoEntry,
       "brdNumber1": brdNumber1,
       "cardType": cardType,
       "pcbRevision": pcbRevision,
       "macAddress": macAddress,
       "driverSeq": driverSeq,
       "product": product,
       "serialNumber": serialNumber,
       "masterSlave": masterSlave,
       "ram": ram,
       "shram": shram,
       "eprom": eprom,
       "e2prom": e2prom,
       "flashprom": flashprom,
       "spec0": spec0,
       "spec1": spec1,
       "spec2": spec2,
       "spec3": spec3,
       "ipAddr": ipAddr,
       "nsap": nsap,
       "brdStatusTable": brdStatusTable,
       "brdStatusEntry": brdStatusEntry,
       "brdNumber2": brdNumber2,
       "brdStatus": brdStatus,
       "brdLed": brdLed,
       "brdPlugTable": brdPlugTable,
       "brdPlugEntry": brdPlugEntry,
       "brdNumber3": brdNumber3,
       "brdPlugNumber": brdPlugNumber,
       "brdPlugPosition": brdPlugPosition,
       "brdPlugStatus": brdPlugStatus,
       "brdPlugType": brdPlugType,
       "brdPlugPimType": brdPlugPimType,
       "brdPlugPimLeds": brdPlugPimLeds,
       "brdPlugPimOptions": brdPlugPimOptions,
       "brdOptionTable": brdOptionTable,
       "brdOptionEntry": brdOptionEntry,
       "brdNumber4": brdNumber4,
       "brdOptionNumber": brdOptionNumber,
       "brdOptionName": brdOptionName,
       "brdOptionState": brdOptionState,
       "brdSwitchSettingTable": brdSwitchSettingTable,
       "brdSwitchSettingEntry": brdSwitchSettingEntry,
       "brdNumber5": brdNumber5,
       "brdSwitchNumber": brdSwitchNumber,
       "brdSwitchName": brdSwitchName,
       "brdSwitchSetting": brdSwitchSetting}
)
