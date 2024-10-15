# SNMP MIB module (ZHNSYSTEM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHNSYSTEM
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:04 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhnSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2)
)
zhnSystem.setRevisions(
        ("2012-07-13 12:00",
         "2012-07-06 12:00",
         "2012-05-18 12:00",
         "2012-05-16 12:00",
         "2012-04-12 00:00",
         "2012-02-03 12:00",
         "2012-01-19 14:20",
         "2011-09-09 01:00",
         "2011-01-05 01:00",
         "2009-05-20 01:00",
         "2008-08-25 01:00",
         "2007-11-26 01:00",
         "2007-03-15 01:00",
         "2006-10-17 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WFNT(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("baseStation", 1),
          ("mesh", 2),
          ("notApplicable", 0))
    )



class ELTYPE(Integer32, TextualConvention):
    status = "current"
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
        *(("docsis", 4),
          ("efm", 2),
          ("ethernet", 1),
          ("shdsl", 3),
          ("wimax", 5))
    )



class ELSUBTYPE(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )



class LPT(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("none", 0),
          ("out", 2))
    )



class UPT(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )



class TCSI(Integer32, TextualConvention):
    status = "current"
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
        *(("local", 2),
          ("loop", 1),
          ("notApplicable", 0),
          ("pwe", 3))
    )



class LTRI(Integer32, TextualConvention):
    status = "current"
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
        *(("ethernet", 1),
          ("internal", 2),
          ("notApplicable", 0),
          ("shdsl", 3))
    )



class CSMI(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 1),
          ("differential", 2),
          ("dslAdaptive", 4),
          ("loop", 5),
          ("notApplicable", 0),
          ("synchronous", 3))
    )



class SEI(Integer32, TextualConvention):
    status = "current"
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



class CMI(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("differential", 2),
          ("normal", 1),
          ("notApplicable", 0))
    )



class CDA(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("resetToDefaults", 2),
          ("save", 1))
    )



class RBT(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reboot", 1))
    )



class SCS(Integer32, TextualConvention):
    status = "current"
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
        *(("ds1", 2),
          ("ieee1588", 3),
          ("notApplicable", 0),
          ("uplink", 1))
    )



class ETCS(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("notApplicable", 0),
          ("systemClock", 2))
    )



class SysFirmwareAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("restoreAltFirmware", 1))
    )



class SysAdminStatus(Integer32, TextualConvention):
    status = "current"
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



class SysLogLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("informational", 6),
          ("notice", 5),
          ("warning", 4))
    )



class SysLogMode(Integer32, TextualConvention):
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
        *(("both", 3),
          ("local", 1),
          ("remote", 2))
    )



class SysSntpTimeZones(Integer32, TextualConvention):
    status = "current"
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
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("abu", 1),
          ("adelaide", 2),
          ("alaska", 3),
          ("almaty", 4),
          ("amsterdam", 5),
          ("arizona", 6),
          ("astana", 7),
          ("athens", 8),
          ("atlantic", 9),
          ("auckland", 10),
          ("azores", 11),
          ("baghdad", 12),
          ("baku", 13),
          ("bangkok", 14),
          ("beijing", 15),
          ("belgrade", 16),
          ("bogota", 17),
          ("brasilia", 18),
          ("brisbane", 19),
          ("brussels", 20),
          ("bucharest", 21),
          ("buenos", 22),
          ("cairo", 23),
          ("canberra", 24),
          ("cape", 25),
          ("caracas", 26),
          ("casablanca", 27),
          ("central", 28),
          ("centraltime", 29),
          ("chennai", 30),
          ("chihuahua", 31),
          ("darwin", 32),
          ("eastern", 33),
          ("ekaterinburg", 34),
          ("fiji", 35),
          ("greenland", 36),
          ("greenwich", 37),
          ("guadalajara", 38),
          ("guam", 39),
          ("harare", 40),
          ("hawaii", 41),
          ("helsinki", 42),
          ("hobart", 43),
          ("indiana", 44),
          ("international", 45),
          ("irkutsk", 46),
          ("islamabad", 47),
          ("jerusalem", 48),
          ("kabul", 49),
          ("kathmandu", 50),
          ("krasnoyarsk", 51),
          ("kuala", 52),
          ("kuwait", 53),
          ("magadan", 54),
          ("midatlantic", 55),
          ("midway", 56),
          ("moscow", 57),
          ("mountain", 58),
          ("nairobi", 59),
          ("newfoundland", 60),
          ("osaka", 61),
          ("pacific", 62),
          ("perth", 63),
          ("rangoon", 64),
          ("santiago", 65),
          ("sarajevo", 66),
          ("saskatchewan", 67),
          ("seoul", 68),
          ("solomon", 69),
          ("sri", 70),
          ("taipei", 71),
          ("tehran", 72),
          ("unknown", 0),
          ("vladivostok", 73),
          ("west", 74),
          ("yakutsk", 75))
    )



class IPInterfaceAddressingTypeValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class BasicAddressingTypeValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_ZhnSystemObjects_ObjectIdentity = ObjectIdentity
zhnSystemObjects = _ZhnSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1)
)
_ZhnSystemGeneralObjects_ObjectIdentity = ObjectIdentity
zhnSystemGeneralObjects = _ZhnSystemGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1)
)
_ModelNumber_Type = DisplayString
_ModelNumber_Object = MibScalar
modelNumber = _ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 1),
    _ModelNumber_Type()
)
modelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelNumber.setStatus("current")
_MacBaseAddress_Type = MacAddress
_MacBaseAddress_Object = MibScalar
macBaseAddress = _MacBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 2),
    _MacBaseAddress_Type()
)
macBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macBaseAddress.setStatus("current")


class _NumberOfMacAddresses_Type(Unsigned32):
    """Custom type numberOfMacAddresses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_NumberOfMacAddresses_Type.__name__ = "Unsigned32"
_NumberOfMacAddresses_Object = MibScalar
numberOfMacAddresses = _NumberOfMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 3),
    _NumberOfMacAddresses_Type()
)
numberOfMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfMacAddresses.setStatus("current")
_WifiNetworkType_Type = WFNT
_WifiNetworkType_Object = MibScalar
wifiNetworkType = _WifiNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 4),
    _WifiNetworkType_Type()
)
wifiNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wifiNetworkType.setStatus("current")
_PowerSupplyType_Type = UPT
_PowerSupplyType_Object = MibScalar
powerSupplyType = _PowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 5),
    _PowerSupplyType_Type()
)
powerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyType.setStatus("current")
_LocationLatitude_Type = DisplayString
_LocationLatitude_Object = MibScalar
locationLatitude = _LocationLatitude_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 6),
    _LocationLatitude_Type()
)
locationLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationLatitude.setStatus("current")
_LocationLongitude_Type = DisplayString
_LocationLongitude_Object = MibScalar
locationLongitude = _LocationLongitude_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 7),
    _LocationLongitude_Type()
)
locationLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locationLongitude.setStatus("current")
_ZhnSystemAction_Type = RowStatus
_ZhnSystemAction_Object = MibScalar
zhnSystemAction = _ZhnSystemAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 8),
    _ZhnSystemAction_Type()
)
zhnSystemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnSystemAction.setStatus("current")
_ZhnSysLocation_Type = DisplayString
_ZhnSysLocation_Object = MibScalar
zhnSysLocation = _ZhnSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 9),
    _ZhnSysLocation_Type()
)
zhnSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnSysLocation.setStatus("current")
_ZhnSysContact_Type = DisplayString
_ZhnSysContact_Object = MibScalar
zhnSysContact = _ZhnSysContact_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 10),
    _ZhnSysContact_Type()
)
zhnSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnSysContact.setStatus("current")
_SysTransmitClockSource_Type = TCSI
_SysTransmitClockSource_Object = MibScalar
sysTransmitClockSource = _SysTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 11),
    _SysTransmitClockSource_Type()
)
sysTransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTransmitClockSource.setStatus("current")
_SysLocalTimingReference_Type = LTRI
_SysLocalTimingReference_Object = MibScalar
sysLocalTimingReference = _SysLocalTimingReference_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 12),
    _SysLocalTimingReference_Type()
)
sysLocalTimingReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocalTimingReference.setStatus("current")
_SysSynchronizationMode_Type = CSMI
_SysSynchronizationMode_Object = MibScalar
sysSynchronizationMode = _SysSynchronizationMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 13),
    _SysSynchronizationMode_Type()
)
sysSynchronizationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSynchronizationMode.setStatus("current")
_SysSynchronousEthernet_Type = SEI
_SysSynchronousEthernet_Object = MibScalar
sysSynchronousEthernet = _SysSynchronousEthernet_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 14),
    _SysSynchronousEthernet_Type()
)
sysSynchronousEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSynchronousEthernet.setStatus("current")
_SysClockMode_Type = CMI
_SysClockMode_Object = MibScalar
sysClockMode = _SysClockMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 15),
    _SysClockMode_Type()
)
sysClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysClockMode.setStatus("current")
_SysCfgDBAction_Type = CDA
_SysCfgDBAction_Object = MibScalar
sysCfgDBAction = _SysCfgDBAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 16),
    _SysCfgDBAction_Type()
)
sysCfgDBAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCfgDBAction.setStatus("current")
_SysSoftwareReboot_Type = RBT
_SysSoftwareReboot_Object = MibScalar
sysSoftwareReboot = _SysSoftwareReboot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 17),
    _SysSoftwareReboot_Type()
)
sysSoftwareReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSoftwareReboot.setStatus("current")
_SysSystemClockSource_Type = SCS
_SysSystemClockSource_Object = MibScalar
sysSystemClockSource = _SysSystemClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 18),
    _SysSystemClockSource_Type()
)
sysSystemClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSystemClockSource.setStatus("current")
_SysEthernetTransmitClockSource_Type = ETCS
_SysEthernetTransmitClockSource_Object = MibScalar
sysEthernetTransmitClockSource = _SysEthernetTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 19),
    _SysEthernetTransmitClockSource_Type()
)
sysEthernetTransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEthernetTransmitClockSource.setStatus("current")
_SysDs1ClockSourcePort_Type = DisplayString
_SysDs1ClockSourcePort_Object = MibScalar
sysDs1ClockSourcePort = _SysDs1ClockSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 20),
    _SysDs1ClockSourcePort_Type()
)
sysDs1ClockSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDs1ClockSourcePort.setStatus("current")


class _SysBootloaderVersion_Type(OctetString):
    """Custom type sysBootloaderVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SysBootloaderVersion_Type.__name__ = "OctetString"
_SysBootloaderVersion_Object = MibScalar
sysBootloaderVersion = _SysBootloaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 21),
    _SysBootloaderVersion_Type()
)
sysBootloaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootloaderVersion.setStatus("current")


class _SysFirmwareVersion_Type(OctetString):
    """Custom type sysFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SysFirmwareVersion_Type.__name__ = "OctetString"
_SysFirmwareVersion_Object = MibScalar
sysFirmwareVersion = _SysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 22),
    _SysFirmwareVersion_Type()
)
sysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirmwareVersion.setStatus("current")


class _SysAltFirmwareVersion_Type(OctetString):
    """Custom type sysAltFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SysAltFirmwareVersion_Type.__name__ = "OctetString"
_SysAltFirmwareVersion_Object = MibScalar
sysAltFirmwareVersion = _SysAltFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 23),
    _SysAltFirmwareVersion_Type()
)
sysAltFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAltFirmwareVersion.setStatus("current")
_SysRestoreAltFirmwareVersion_Type = SysFirmwareAction
_SysRestoreAltFirmwareVersion_Object = MibScalar
sysRestoreAltFirmwareVersion = _SysRestoreAltFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 24),
    _SysRestoreAltFirmwareVersion_Type()
)
sysRestoreAltFirmwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRestoreAltFirmwareVersion.setStatus("current")
_SysSnmpProvisioningLock_Type = TruthValue
_SysSnmpProvisioningLock_Object = MibScalar
sysSnmpProvisioningLock = _SysSnmpProvisioningLock_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 25),
    _SysSnmpProvisioningLock_Type()
)
sysSnmpProvisioningLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpProvisioningLock.setStatus("current")
_SysSnmpProvisioningChange_Type = Unsigned32
_SysSnmpProvisioningChange_Object = MibScalar
sysSnmpProvisioningChange = _SysSnmpProvisioningChange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 1, 26),
    _SysSnmpProvisioningChange_Type()
)
sysSnmpProvisioningChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpProvisioningChange.setStatus("current")
_ZhnSystemBoardObjects_ObjectIdentity = ObjectIdentity
zhnSystemBoardObjects = _ZhnSystemBoardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 2)
)


class _NumberOfBoards_Type(Unsigned32):
    """Custom type numberOfBoards based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_NumberOfBoards_Type.__name__ = "Unsigned32"
_NumberOfBoards_Object = MibScalar
numberOfBoards = _NumberOfBoards_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 2, 1),
    _NumberOfBoards_Type()
)
numberOfBoards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfBoards.setStatus("current")
_BoardDescriptorTable_Object = MibTable
boardDescriptorTable = _BoardDescriptorTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    boardDescriptorTable.setStatus("current")
_BoardDescriptorEntry_Object = MibTableRow
boardDescriptorEntry = _BoardDescriptorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 2, 2, 1)
)
boardDescriptorEntry.setIndexNames(
    (0, "ZHNSYSTEM", "boardIndex"),
)
if mibBuilder.loadTexts:
    boardDescriptorEntry.setStatus("current")


class _BoardIndex_Type(Unsigned32):
    """Custom type boardIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_BoardIndex_Type.__name__ = "Unsigned32"
_BoardIndex_Object = MibTableColumn
boardIndex = _BoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 2, 2, 1, 1),
    _BoardIndex_Type()
)
boardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardIndex.setStatus("current")
_BoardName_Type = DisplayString
_BoardName_Object = MibTableColumn
boardName = _BoardName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 2, 2, 1, 2),
    _BoardName_Type()
)
boardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardName.setStatus("current")
_BoardPartNumber_Type = DisplayString
_BoardPartNumber_Object = MibTableColumn
boardPartNumber = _BoardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 2, 2, 1, 3),
    _BoardPartNumber_Type()
)
boardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPartNumber.setStatus("current")
_BoardSerialNumber_Type = DisplayString
_BoardSerialNumber_Object = MibTableColumn
boardSerialNumber = _BoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 2, 2, 1, 4),
    _BoardSerialNumber_Type()
)
boardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSerialNumber.setStatus("current")
_BoardRevision_Type = DisplayString
_BoardRevision_Object = MibTableColumn
boardRevision = _BoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 2, 2, 1, 5),
    _BoardRevision_Type()
)
boardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardRevision.setStatus("current")
_ZhnSystemPldObjects_ObjectIdentity = ObjectIdentity
zhnSystemPldObjects = _ZhnSystemPldObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 3)
)


class _NumberOfPlds_Type(Unsigned32):
    """Custom type numberOfPlds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_NumberOfPlds_Type.__name__ = "Unsigned32"
_NumberOfPlds_Object = MibScalar
numberOfPlds = _NumberOfPlds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 3, 1),
    _NumberOfPlds_Type()
)
numberOfPlds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfPlds.setStatus("current")
_PldDescriptorTable_Object = MibTable
pldDescriptorTable = _PldDescriptorTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pldDescriptorTable.setStatus("current")
_PldDescriptorEntry_Object = MibTableRow
pldDescriptorEntry = _PldDescriptorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 3, 2, 1)
)
pldDescriptorEntry.setIndexNames(
    (0, "ZHNSYSTEM", "pldIndex"),
)
if mibBuilder.loadTexts:
    pldDescriptorEntry.setStatus("current")


class _PldIndex_Type(Unsigned32):
    """Custom type pldIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_PldIndex_Type.__name__ = "Unsigned32"
_PldIndex_Object = MibTableColumn
pldIndex = _PldIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 3, 2, 1, 1),
    _PldIndex_Type()
)
pldIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pldIndex.setStatus("current")
_PldName_Type = DisplayString
_PldName_Object = MibTableColumn
pldName = _PldName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 3, 2, 1, 2),
    _PldName_Type()
)
pldName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldName.setStatus("current")
_PldVersion_Type = DisplayString
_PldVersion_Object = MibTableColumn
pldVersion = _PldVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 3, 2, 1, 3),
    _PldVersion_Type()
)
pldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldVersion.setStatus("current")
_ZhnSystemRadioObjects_ObjectIdentity = ObjectIdentity
zhnSystemRadioObjects = _ZhnSystemRadioObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 4)
)


class _NumberOfRadios_Type(Unsigned32):
    """Custom type numberOfRadios based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_NumberOfRadios_Type.__name__ = "Unsigned32"
_NumberOfRadios_Object = MibScalar
numberOfRadios = _NumberOfRadios_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 4, 1),
    _NumberOfRadios_Type()
)
numberOfRadios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfRadios.setStatus("current")
_ZhnSystemEthernetLikeObjects_ObjectIdentity = ObjectIdentity
zhnSystemEthernetLikeObjects = _ZhnSystemEthernetLikeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 5)
)


class _NumberOfEthernetLikeInterfaces_Type(Unsigned32):
    """Custom type numberOfEthernetLikeInterfaces based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_NumberOfEthernetLikeInterfaces_Type.__name__ = "Unsigned32"
_NumberOfEthernetLikeInterfaces_Object = MibScalar
numberOfEthernetLikeInterfaces = _NumberOfEthernetLikeInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 5, 1),
    _NumberOfEthernetLikeInterfaces_Type()
)
numberOfEthernetLikeInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfEthernetLikeInterfaces.setStatus("current")
_EthernetlikeInterfaceTable_Object = MibTable
ethernetlikeInterfaceTable = _EthernetlikeInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ethernetlikeInterfaceTable.setStatus("current")
_EthernetlikeInterfaceEntry_Object = MibTableRow
ethernetlikeInterfaceEntry = _EthernetlikeInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 5, 2, 1)
)
ethernetlikeInterfaceEntry.setIndexNames(
    (0, "ZHNSYSTEM", "etherIndex"),
)
if mibBuilder.loadTexts:
    ethernetlikeInterfaceEntry.setStatus("current")


class _EtherIndex_Type(Unsigned32):
    """Custom type etherIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_EtherIndex_Type.__name__ = "Unsigned32"
_EtherIndex_Object = MibTableColumn
etherIndex = _EtherIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 5, 2, 1, 1),
    _EtherIndex_Type()
)
etherIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etherIndex.setStatus("current")
_EtherName_Type = DisplayString
_EtherName_Object = MibTableColumn
etherName = _EtherName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 5, 2, 1, 2),
    _EtherName_Type()
)
etherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherName.setStatus("current")
_EtherType_Type = ELTYPE
_EtherType_Object = MibTableColumn
etherType = _EtherType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 5, 2, 1, 3),
    _EtherType_Type()
)
etherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherType.setStatus("current")
_EtherSubtype_Type = ELSUBTYPE
_EtherSubtype_Object = MibTableColumn
etherSubtype = _EtherSubtype_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 5, 2, 1, 4),
    _EtherSubtype_Type()
)
etherSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherSubtype.setStatus("current")


class _EtherNumberOfPorts_Type(Unsigned32):
    """Custom type etherNumberOfPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_EtherNumberOfPorts_Type.__name__ = "Unsigned32"
_EtherNumberOfPorts_Object = MibTableColumn
etherNumberOfPorts = _EtherNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 5, 2, 1, 5),
    _EtherNumberOfPorts_Type()
)
etherNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherNumberOfPorts.setStatus("current")
_EtherLinePower_Type = LPT
_EtherLinePower_Object = MibTableColumn
etherLinePower = _EtherLinePower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 5, 2, 1, 6),
    _EtherLinePower_Type()
)
etherLinePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherLinePower.setStatus("current")
_EtherPowerPairs_Type = Integer32
_EtherPowerPairs_Object = MibTableColumn
etherPowerPairs = _EtherPowerPairs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 5, 2, 1, 7),
    _EtherPowerPairs_Type()
)
etherPowerPairs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherPowerPairs.setStatus("current")
_ZhnSystemTempSensorObjects_ObjectIdentity = ObjectIdentity
zhnSystemTempSensorObjects = _ZhnSystemTempSensorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 6)
)


class _NumberOfTemperatureSensors_Type(Unsigned32):
    """Custom type numberOfTemperatureSensors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_NumberOfTemperatureSensors_Type.__name__ = "Unsigned32"
_NumberOfTemperatureSensors_Object = MibScalar
numberOfTemperatureSensors = _NumberOfTemperatureSensors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 6, 1),
    _NumberOfTemperatureSensors_Type()
)
numberOfTemperatureSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfTemperatureSensors.setStatus("current")
_TemperatureSensorTable_Object = MibTable
temperatureSensorTable = _TemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    temperatureSensorTable.setStatus("current")
_TemperatureSensorEntry_Object = MibTableRow
temperatureSensorEntry = _TemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 6, 2, 1)
)
temperatureSensorEntry.setIndexNames(
    (0, "ZHNSYSTEM", "temperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    temperatureSensorEntry.setStatus("current")


class _TemperatureSensorIndex_Type(Unsigned32):
    """Custom type temperatureSensorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_TemperatureSensorIndex_Type.__name__ = "Unsigned32"
_TemperatureSensorIndex_Object = MibTableColumn
temperatureSensorIndex = _TemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 6, 2, 1, 1),
    _TemperatureSensorIndex_Type()
)
temperatureSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temperatureSensorIndex.setStatus("current")
_TemperatureSensorName_Type = DisplayString
_TemperatureSensorName_Object = MibTableColumn
temperatureSensorName = _TemperatureSensorName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 6, 2, 1, 2),
    _TemperatureSensorName_Type()
)
temperatureSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorName.setStatus("current")
_TemperatureSensorMaximum_Type = DisplayString
_TemperatureSensorMaximum_Object = MibTableColumn
temperatureSensorMaximum = _TemperatureSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 6, 2, 1, 3),
    _TemperatureSensorMaximum_Type()
)
temperatureSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorMaximum.setStatus("current")
_TemperatureSensorMinimum_Type = DisplayString
_TemperatureSensorMinimum_Object = MibTableColumn
temperatureSensorMinimum = _TemperatureSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 6, 2, 1, 4),
    _TemperatureSensorMinimum_Type()
)
temperatureSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorMinimum.setStatus("current")
_ZhnSystemSNMPObjects_ObjectIdentity = ObjectIdentity
zhnSystemSNMPObjects = _ZhnSystemSNMPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7)
)


class _NumberOfCommunities_Type(Unsigned32):
    """Custom type numberOfCommunities based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_NumberOfCommunities_Type.__name__ = "Unsigned32"
_NumberOfCommunities_Object = MibScalar
numberOfCommunities = _NumberOfCommunities_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7, 1),
    _NumberOfCommunities_Type()
)
numberOfCommunities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfCommunities.setStatus("current")
_ZhnCommunityTable_Object = MibTable
zhnCommunityTable = _ZhnCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    zhnCommunityTable.setStatus("current")
_ZhnCommunityTableEntry_Object = MibTableRow
zhnCommunityTableEntry = _ZhnCommunityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7, 2, 1)
)
zhnCommunityTableEntry.setIndexNames(
    (0, "ZHNSYSTEM", "communityName"),
)
if mibBuilder.loadTexts:
    zhnCommunityTableEntry.setStatus("current")
_CommunityName_Type = DisplayString
_CommunityName_Object = MibTableColumn
communityName = _CommunityName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7, 2, 1, 1),
    _CommunityName_Type()
)
communityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    communityName.setStatus("current")


class _CommunityType_Type(Integer32):
    """Custom type communityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_CommunityType_Type.__name__ = "Integer32"
_CommunityType_Object = MibTableColumn
communityType = _CommunityType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7, 2, 1, 2),
    _CommunityType_Type()
)
communityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityType.setStatus("current")
_CommunityRowStatus_Type = RowStatus
_CommunityRowStatus_Object = MibTableColumn
communityRowStatus = _CommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7, 2, 1, 3),
    _CommunityRowStatus_Type()
)
communityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    communityRowStatus.setStatus("current")
_ZhnFixedCommunityTable_Object = MibTable
zhnFixedCommunityTable = _ZhnFixedCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    zhnFixedCommunityTable.setStatus("current")
_ZhnFixedCommunityTableEntry_Object = MibTableRow
zhnFixedCommunityTableEntry = _ZhnFixedCommunityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7, 3, 1)
)
zhnFixedCommunityTableEntry.setIndexNames(
    (0, "ZHNSYSTEM", "communityType"),
)
if mibBuilder.loadTexts:
    zhnFixedCommunityTableEntry.setStatus("current")
_FixedCommunityName_Type = DisplayString
_FixedCommunityName_Object = MibTableColumn
fixedCommunityName = _FixedCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7, 3, 1, 1),
    _FixedCommunityName_Type()
)
fixedCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fixedCommunityName.setStatus("current")


class _FixedCommunityType_Type(Integer32):
    """Custom type fixedCommunityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_FixedCommunityType_Type.__name__ = "Integer32"
_FixedCommunityType_Object = MibTableColumn
fixedCommunityType = _FixedCommunityType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7, 3, 1, 2),
    _FixedCommunityType_Type()
)
fixedCommunityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fixedCommunityType.setStatus("current")
_FixedCommunityRowStatus_Type = RowStatus
_FixedCommunityRowStatus_Object = MibTableColumn
fixedCommunityRowStatus = _FixedCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 7, 3, 1, 3),
    _FixedCommunityRowStatus_Type()
)
fixedCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fixedCommunityRowStatus.setStatus("current")
_ZhnSystemTrapObjects_ObjectIdentity = ObjectIdentity
zhnSystemTrapObjects = _ZhnSystemTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8)
)


class _NumberOfTrapManagers_Type(Unsigned32):
    """Custom type numberOfTrapManagers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_NumberOfTrapManagers_Type.__name__ = "Unsigned32"
_NumberOfTrapManagers_Object = MibScalar
numberOfTrapManagers = _NumberOfTrapManagers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 1),
    _NumberOfTrapManagers_Type()
)
numberOfTrapManagers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfTrapManagers.setStatus("current")
_ZhnDefaultTrapCommunity_Type = DisplayString
_ZhnDefaultTrapCommunity_Object = MibScalar
zhnDefaultTrapCommunity = _ZhnDefaultTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 2),
    _ZhnDefaultTrapCommunity_Type()
)
zhnDefaultTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnDefaultTrapCommunity.setStatus("current")


class _ZhnTrapTypeLinkUpDown_Type(Integer32):
    """Custom type zhnTrapTypeLinkUpDown based on Integer32"""
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


_ZhnTrapTypeLinkUpDown_Type.__name__ = "Integer32"
_ZhnTrapTypeLinkUpDown_Object = MibScalar
zhnTrapTypeLinkUpDown = _ZhnTrapTypeLinkUpDown_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 3),
    _ZhnTrapTypeLinkUpDown_Type()
)
zhnTrapTypeLinkUpDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnTrapTypeLinkUpDown.setStatus("current")


class _ZhnTrapTypeAuthFailure_Type(Integer32):
    """Custom type zhnTrapTypeAuthFailure based on Integer32"""
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


_ZhnTrapTypeAuthFailure_Type.__name__ = "Integer32"
_ZhnTrapTypeAuthFailure_Object = MibScalar
zhnTrapTypeAuthFailure = _ZhnTrapTypeAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 4),
    _ZhnTrapTypeAuthFailure_Type()
)
zhnTrapTypeAuthFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnTrapTypeAuthFailure.setStatus("current")


class _ZhnTrapTypeConfigChange_Type(Integer32):
    """Custom type zhnTrapTypeConfigChange based on Integer32"""
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


_ZhnTrapTypeConfigChange_Type.__name__ = "Integer32"
_ZhnTrapTypeConfigChange_Object = MibScalar
zhnTrapTypeConfigChange = _ZhnTrapTypeConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 5),
    _ZhnTrapTypeConfigChange_Type()
)
zhnTrapTypeConfigChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnTrapTypeConfigChange.setStatus("current")
_ZhnTrapManagerInfoTable_Object = MibTable
zhnTrapManagerInfoTable = _ZhnTrapManagerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 6)
)
if mibBuilder.loadTexts:
    zhnTrapManagerInfoTable.setStatus("current")
_ZhnTrapManagerInfoTableEntry_Object = MibTableRow
zhnTrapManagerInfoTableEntry = _ZhnTrapManagerInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 6, 1)
)
zhnTrapManagerInfoTableEntry.setIndexNames(
    (0, "ZHNSYSTEM", "trapDestination"),
)
if mibBuilder.loadTexts:
    zhnTrapManagerInfoTableEntry.setStatus("current")
_TrapDestination_Type = IpAddress
_TrapDestination_Object = MibTableColumn
trapDestination = _TrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 6, 1, 1),
    _TrapDestination_Type()
)
trapDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDestination.setStatus("current")
_TrapCommunityName_Type = DisplayString
_TrapCommunityName_Object = MibTableColumn
trapCommunityName = _TrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 6, 1, 2),
    _TrapCommunityName_Type()
)
trapCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunityName.setStatus("current")


class _TrapVersion_Type(Integer32):
    """Custom type trapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2))
    )


_TrapVersion_Type.__name__ = "Integer32"
_TrapVersion_Object = MibTableColumn
trapVersion = _TrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 6, 1, 3),
    _TrapVersion_Type()
)
trapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapVersion.setStatus("current")


class _TrapPort_Type(Integer32):
    """Custom type trapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_TrapPort_Type.__name__ = "Integer32"
_TrapPort_Object = MibTableColumn
trapPort = _TrapPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 6, 1, 4),
    _TrapPort_Type()
)
trapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapPort.setStatus("current")
_TrapRowStatus_Type = RowStatus
_TrapRowStatus_Object = MibTableColumn
trapRowStatus = _TrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 6, 1, 5),
    _TrapRowStatus_Type()
)
trapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapRowStatus.setStatus("current")


class _ZhnTrapTypeColdStart_Type(Integer32):
    """Custom type zhnTrapTypeColdStart based on Integer32"""
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


_ZhnTrapTypeColdStart_Type.__name__ = "Integer32"
_ZhnTrapTypeColdStart_Object = MibScalar
zhnTrapTypeColdStart = _ZhnTrapTypeColdStart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 7),
    _ZhnTrapTypeColdStart_Type()
)
zhnTrapTypeColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnTrapTypeColdStart.setStatus("current")


class _ZhnTrapTypeWarmStart_Type(Integer32):
    """Custom type zhnTrapTypeWarmStart based on Integer32"""
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


_ZhnTrapTypeWarmStart_Type.__name__ = "Integer32"
_ZhnTrapTypeWarmStart_Object = MibScalar
zhnTrapTypeWarmStart = _ZhnTrapTypeWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 8),
    _ZhnTrapTypeWarmStart_Type()
)
zhnTrapTypeWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnTrapTypeWarmStart.setStatus("current")


class _ZhnTrapTypeEnterprise_Type(Integer32):
    """Custom type zhnTrapTypeEnterprise based on Integer32"""
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


_ZhnTrapTypeEnterprise_Type.__name__ = "Integer32"
_ZhnTrapTypeEnterprise_Object = MibScalar
zhnTrapTypeEnterprise = _ZhnTrapTypeEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 8, 9),
    _ZhnTrapTypeEnterprise_Type()
)
zhnTrapTypeEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnTrapTypeEnterprise.setStatus("current")
_ZhnSystemSyslogObjects_ObjectIdentity = ObjectIdentity
zhnSystemSyslogObjects = _ZhnSystemSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 9)
)
_SysLogAdminStatus_Type = SysAdminStatus
_SysLogAdminStatus_Object = MibScalar
sysLogAdminStatus = _SysLogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 9, 1),
    _SysLogAdminStatus_Type()
)
sysLogAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogAdminStatus.setStatus("current")
_SysLogLocalLogLevel_Type = SysLogLevel
_SysLogLocalLogLevel_Object = MibScalar
sysLogLocalLogLevel = _SysLogLocalLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 9, 2),
    _SysLogLocalLogLevel_Type()
)
sysLogLocalLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogLocalLogLevel.setStatus("current")
_SysLogRemoteLogLevel_Type = SysLogLevel
_SysLogRemoteLogLevel_Object = MibScalar
sysLogRemoteLogLevel = _SysLogRemoteLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 9, 3),
    _SysLogRemoteLogLevel_Type()
)
sysLogRemoteLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogRemoteLogLevel.setStatus("current")
_SysLogDisplayLogLevel_Type = SysLogLevel
_SysLogDisplayLogLevel_Object = MibScalar
sysLogDisplayLogLevel = _SysLogDisplayLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 9, 4),
    _SysLogDisplayLogLevel_Type()
)
sysLogDisplayLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogDisplayLogLevel.setStatus("current")
_SysLogMode_Type = SysLogMode
_SysLogMode_Object = MibScalar
sysLogMode = _SysLogMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 9, 5),
    _SysLogMode_Type()
)
sysLogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogMode.setStatus("current")
_SysLogRemoteServerAddress_Type = IpAddress
_SysLogRemoteServerAddress_Object = MibScalar
sysLogRemoteServerAddress = _SysLogRemoteServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 9, 6),
    _SysLogRemoteServerAddress_Type()
)
sysLogRemoteServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogRemoteServerAddress.setStatus("current")


class _SysLogRemoteServerPort_Type(Unsigned32):
    """Custom type sysLogRemoteServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysLogRemoteServerPort_Type.__name__ = "Unsigned32"
_SysLogRemoteServerPort_Object = MibScalar
sysLogRemoteServerPort = _SysLogRemoteServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 9, 7),
    _SysLogRemoteServerPort_Type()
)
sysLogRemoteServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogRemoteServerPort.setStatus("current")
_ZhnSystemSNTPObjects_ObjectIdentity = ObjectIdentity
zhnSystemSNTPObjects = _ZhnSystemSNTPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 10)
)
_SntpAdminStatus_Type = SysAdminStatus
_SntpAdminStatus_Object = MibScalar
sntpAdminStatus = _SntpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 10, 1),
    _SntpAdminStatus_Type()
)
sntpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpAdminStatus.setStatus("current")
_SntpOperStatus_Type = SysAdminStatus
_SntpOperStatus_Object = MibScalar
sntpOperStatus = _SntpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 10, 2),
    _SntpOperStatus_Type()
)
sntpOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpOperStatus.setStatus("current")


class _SntpServer1_Type(OctetString):
    """Custom type sntpServer1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SntpServer1_Type.__name__ = "OctetString"
_SntpServer1_Object = MibScalar
sntpServer1 = _SntpServer1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 10, 3),
    _SntpServer1_Type()
)
sntpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServer1.setStatus("current")


class _SntpServer2_Type(OctetString):
    """Custom type sntpServer2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SntpServer2_Type.__name__ = "OctetString"
_SntpServer2_Object = MibScalar
sntpServer2 = _SntpServer2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 10, 4),
    _SntpServer2_Type()
)
sntpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServer2.setStatus("current")


class _SntpServer3_Type(OctetString):
    """Custom type sntpServer3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SntpServer3_Type.__name__ = "OctetString"
_SntpServer3_Object = MibScalar
sntpServer3 = _SntpServer3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 10, 5),
    _SntpServer3_Type()
)
sntpServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServer3.setStatus("current")


class _SntpServer4_Type(OctetString):
    """Custom type sntpServer4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SntpServer4_Type.__name__ = "OctetString"
_SntpServer4_Object = MibScalar
sntpServer4 = _SntpServer4_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 10, 6),
    _SntpServer4_Type()
)
sntpServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServer4.setStatus("current")


class _SntpServer5_Type(OctetString):
    """Custom type sntpServer5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SntpServer5_Type.__name__ = "OctetString"
_SntpServer5_Object = MibScalar
sntpServer5 = _SntpServer5_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 10, 7),
    _SntpServer5_Type()
)
sntpServer5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServer5.setStatus("current")
_SntpLocalTimeZone_Type = SysSntpTimeZones
_SntpLocalTimeZone_Object = MibScalar
sntpLocalTimeZone = _SntpLocalTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 10, 8),
    _SntpLocalTimeZone_Type()
)
sntpLocalTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpLocalTimeZone.setStatus("current")
_SntpCurrentDateAndTime_Type = DisplayString
_SntpCurrentDateAndTime_Object = MibScalar
sntpCurrentDateAndTime = _SntpCurrentDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 10, 9),
    _SntpCurrentDateAndTime_Type()
)
sntpCurrentDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpCurrentDateAndTime.setStatus("current")
_ZhnSystemUserLoginObjects_ObjectIdentity = ObjectIdentity
zhnSystemUserLoginObjects = _ZhnSystemUserLoginObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 11)
)


class _AdminUserName_Type(OctetString):
    """Custom type adminUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdminUserName_Type.__name__ = "OctetString"
_AdminUserName_Object = MibScalar
adminUserName = _AdminUserName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 11, 1),
    _AdminUserName_Type()
)
adminUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminUserName.setStatus("current")


class _AdminPassword_Type(OctetString):
    """Custom type adminPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdminPassword_Type.__name__ = "OctetString"
_AdminPassword_Object = MibScalar
adminPassword = _AdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 11, 2),
    _AdminPassword_Type()
)
adminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminPassword.setStatus("current")


class _SupportUserName_Type(OctetString):
    """Custom type supportUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SupportUserName_Type.__name__ = "OctetString"
_SupportUserName_Object = MibScalar
supportUserName = _SupportUserName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 11, 3),
    _SupportUserName_Type()
)
supportUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportUserName.setStatus("current")


class _SupportPassword_Type(OctetString):
    """Custom type supportPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SupportPassword_Type.__name__ = "OctetString"
_SupportPassword_Object = MibScalar
supportPassword = _SupportPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 11, 4),
    _SupportPassword_Type()
)
supportPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supportPassword.setStatus("current")


class _UserUserName_Type(OctetString):
    """Custom type userUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UserUserName_Type.__name__ = "OctetString"
_UserUserName_Object = MibScalar
userUserName = _UserUserName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 11, 5),
    _UserUserName_Type()
)
userUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userUserName.setStatus("current")


class _UserPassword_Type(OctetString):
    """Custom type userPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UserPassword_Type.__name__ = "OctetString"
_UserPassword_Object = MibScalar
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 11, 6),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")
_ZhnSystemPowerSheddingObjects_ObjectIdentity = ObjectIdentity
zhnSystemPowerSheddingObjects = _ZhnSystemPowerSheddingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 12)
)
_PowerSheddingAdminStatus_Type = SysAdminStatus
_PowerSheddingAdminStatus_Object = MibScalar
powerSheddingAdminStatus = _PowerSheddingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 12, 1),
    _PowerSheddingAdminStatus_Type()
)
powerSheddingAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSheddingAdminStatus.setStatus("current")


class _PowerSheddingShutdownDelay_Type(Unsigned32):
    """Custom type powerSheddingShutdownDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PowerSheddingShutdownDelay_Type.__name__ = "Unsigned32"
_PowerSheddingShutdownDelay_Object = MibScalar
powerSheddingShutdownDelay = _PowerSheddingShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 12, 2),
    _PowerSheddingShutdownDelay_Type()
)
powerSheddingShutdownDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSheddingShutdownDelay.setStatus("current")


class _PowerSheddingRestoreDelay_Type(Unsigned32):
    """Custom type powerSheddingRestoreDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PowerSheddingRestoreDelay_Type.__name__ = "Unsigned32"
_PowerSheddingRestoreDelay_Object = MibScalar
powerSheddingRestoreDelay = _PowerSheddingRestoreDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 12, 3),
    _PowerSheddingRestoreDelay_Type()
)
powerSheddingRestoreDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSheddingRestoreDelay.setStatus("current")
_ZhnSystemFirewallObjects_ObjectIdentity = ObjectIdentity
zhnSystemFirewallObjects = _ZhnSystemFirewallObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 13)
)
_SysFirewallEnable_Type = TruthValue
_SysFirewallEnable_Object = MibScalar
sysFirewallEnable = _SysFirewallEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 13, 1),
    _SysFirewallEnable_Type()
)
sysFirewallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFirewallEnable.setStatus("current")
_SysFirewallTcpSynCookies_Type = TruthValue
_SysFirewallTcpSynCookies_Object = MibScalar
sysFirewallTcpSynCookies = _SysFirewallTcpSynCookies_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 13, 2),
    _SysFirewallTcpSynCookies_Type()
)
sysFirewallTcpSynCookies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirewallTcpSynCookies.setStatus("current")
_ZhnSystemDNSClientObjects_ObjectIdentity = ObjectIdentity
zhnSystemDNSClientObjects = _ZhnSystemDNSClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 14)
)
_SysDNSAddressingType_Type = IPInterfaceAddressingTypeValues
_SysDNSAddressingType_Object = MibScalar
sysDNSAddressingType = _SysDNSAddressingType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 14, 1),
    _SysDNSAddressingType_Type()
)
sysDNSAddressingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDNSAddressingType.setStatus("current")


class _SysDNSDHCPSource_Type(OctetString):
    """Custom type sysDNSDHCPSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SysDNSDHCPSource_Type.__name__ = "OctetString"
_SysDNSDHCPSource_Object = MibScalar
sysDNSDHCPSource = _SysDNSDHCPSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 14, 2),
    _SysDNSDHCPSource_Type()
)
sysDNSDHCPSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDNSDHCPSource.setStatus("current")
_SysDNSPrimaryIPAddress_Type = IpAddress
_SysDNSPrimaryIPAddress_Object = MibScalar
sysDNSPrimaryIPAddress = _SysDNSPrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 14, 3),
    _SysDNSPrimaryIPAddress_Type()
)
sysDNSPrimaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDNSPrimaryIPAddress.setStatus("current")
_SysDNSSecondaryIPAddress_Type = IpAddress
_SysDNSSecondaryIPAddress_Object = MibScalar
sysDNSSecondaryIPAddress = _SysDNSSecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 14, 4),
    _SysDNSSecondaryIPAddress_Type()
)
sysDNSSecondaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDNSSecondaryIPAddress.setStatus("current")
_ZhnSystemDNSProxyObjects_ObjectIdentity = ObjectIdentity
zhnSystemDNSProxyObjects = _ZhnSystemDNSProxyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 15)
)


class _ZhnDnsProxyHostMaxHostEntries_Type(Unsigned32):
    """Custom type zhnDnsProxyHostMaxHostEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_ZhnDnsProxyHostMaxHostEntries_Type.__name__ = "Unsigned32"
_ZhnDnsProxyHostMaxHostEntries_Object = MibScalar
zhnDnsProxyHostMaxHostEntries = _ZhnDnsProxyHostMaxHostEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 15, 1),
    _ZhnDnsProxyHostMaxHostEntries_Type()
)
zhnDnsProxyHostMaxHostEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnDnsProxyHostMaxHostEntries.setStatus("current")
_ZhnDnsProxyHostTable_Object = MibTable
zhnDnsProxyHostTable = _ZhnDnsProxyHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 15, 2)
)
if mibBuilder.loadTexts:
    zhnDnsProxyHostTable.setStatus("current")
_ZhnDnsProxyHostEntry_Object = MibTableRow
zhnDnsProxyHostEntry = _ZhnDnsProxyHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 15, 2, 1)
)
zhnDnsProxyHostEntry.setIndexNames(
    (0, "ZHNSYSTEM", "dnsProxyHostIndex"),
)
if mibBuilder.loadTexts:
    zhnDnsProxyHostEntry.setStatus("current")


class _DnsProxyHostIndex_Type(Unsigned32):
    """Custom type dnsProxyHostIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_DnsProxyHostIndex_Type.__name__ = "Unsigned32"
_DnsProxyHostIndex_Object = MibTableColumn
dnsProxyHostIndex = _DnsProxyHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 15, 2, 1, 1),
    _DnsProxyHostIndex_Type()
)
dnsProxyHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsProxyHostIndex.setStatus("current")
_DnsProxyHostIPAddress_Type = IpAddress
_DnsProxyHostIPAddress_Object = MibTableColumn
dnsProxyHostIPAddress = _DnsProxyHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 15, 2, 1, 2),
    _DnsProxyHostIPAddress_Type()
)
dnsProxyHostIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsProxyHostIPAddress.setStatus("current")
_DnsProxyHostName_Type = OctetString
_DnsProxyHostName_Object = MibTableColumn
dnsProxyHostName = _DnsProxyHostName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 15, 2, 1, 3),
    _DnsProxyHostName_Type()
)
dnsProxyHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsProxyHostName.setStatus("current")
_DnsProxyRowStatus_Type = ZhoneRowStatus
_DnsProxyRowStatus_Object = MibTableColumn
dnsProxyRowStatus = _DnsProxyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 15, 2, 1, 4),
    _DnsProxyRowStatus_Type()
)
dnsProxyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsProxyRowStatus.setStatus("current")
_ZhnSystemWanBackupObjects_ObjectIdentity = ObjectIdentity
zhnSystemWanBackupObjects = _ZhnSystemWanBackupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16)
)
_FailoverTimer_Type = Unsigned32
_FailoverTimer_Object = MibScalar
failoverTimer = _FailoverTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 1),
    _FailoverTimer_Type()
)
failoverTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    failoverTimer.setStatus("current")
_RestoralTimer_Type = Unsigned32
_RestoralTimer_Object = MibScalar
restoralTimer = _RestoralTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 2),
    _RestoralTimer_Type()
)
restoralTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restoralTimer.setStatus("current")


class _BackupDataVlan_Type(Unsigned32):
    """Custom type backupDataVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_BackupDataVlan_Type.__name__ = "Unsigned32"
_BackupDataVlan_Object = MibScalar
backupDataVlan = _BackupDataVlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 3),
    _BackupDataVlan_Type()
)
backupDataVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupDataVlan.setStatus("current")


class _CellularPinNumber_Type(OctetString):
    """Custom type cellularPinNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CellularPinNumber_Type.__name__ = "OctetString"
_CellularPinNumber_Object = MibScalar
cellularPinNumber = _CellularPinNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 4),
    _CellularPinNumber_Type()
)
cellularPinNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cellularPinNumber.setStatus("current")


class _CellularDataNumber_Type(OctetString):
    """Custom type cellularDataNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CellularDataNumber_Type.__name__ = "OctetString"
_CellularDataNumber_Object = MibScalar
cellularDataNumber = _CellularDataNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 5),
    _CellularDataNumber_Type()
)
cellularDataNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cellularDataNumber.setStatus("current")


class _AtInitCommands_Type(OctetString):
    """Custom type atInitCommands based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AtInitCommands_Type.__name__ = "OctetString"
_AtInitCommands_Object = MibScalar
atInitCommands = _AtInitCommands_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 6),
    _AtInitCommands_Type()
)
atInitCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atInitCommands.setStatus("current")


class _AccessPointName_Type(OctetString):
    """Custom type accessPointName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AccessPointName_Type.__name__ = "OctetString"
_AccessPointName_Object = MibScalar
accessPointName = _AccessPointName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 7),
    _AccessPointName_Type()
)
accessPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessPointName.setStatus("current")


class _ChapPapUsername_Type(OctetString):
    """Custom type chapPapUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChapPapUsername_Type.__name__ = "OctetString"
_ChapPapUsername_Object = MibScalar
chapPapUsername = _ChapPapUsername_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 8),
    _ChapPapUsername_Type()
)
chapPapUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chapPapUsername.setStatus("current")


class _ChapPapPassword_Type(OctetString):
    """Custom type chapPapPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChapPapPassword_Type.__name__ = "OctetString"
_ChapPapPassword_Object = MibScalar
chapPapPassword = _ChapPapPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 9),
    _ChapPapPassword_Type()
)
chapPapPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chapPapPassword.setStatus("current")
_ConnectionTimeout_Type = Unsigned32
_ConnectionTimeout_Object = MibScalar
connectionTimeout = _ConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 10),
    _ConnectionTimeout_Type()
)
connectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionTimeout.setStatus("current")
_BackupIpAddressMode_Type = BasicAddressingTypeValues
_BackupIpAddressMode_Object = MibScalar
backupIpAddressMode = _BackupIpAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 11),
    _BackupIpAddressMode_Type()
)
backupIpAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupIpAddressMode.setStatus("current")
_BackupIpAddress_Type = IpAddress
_BackupIpAddress_Object = MibScalar
backupIpAddress = _BackupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 12),
    _BackupIpAddress_Type()
)
backupIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupIpAddress.setStatus("current")
_BackupDefaultGateway_Type = IpAddress
_BackupDefaultGateway_Object = MibScalar
backupDefaultGateway = _BackupDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 13),
    _BackupDefaultGateway_Type()
)
backupDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupDefaultGateway.setStatus("current")
_BackupSubnetMask_Type = IpAddress
_BackupSubnetMask_Object = MibScalar
backupSubnetMask = _BackupSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 14),
    _BackupSubnetMask_Type()
)
backupSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupSubnetMask.setStatus("current")
_BackupPrimaryDns_Type = IpAddress
_BackupPrimaryDns_Object = MibScalar
backupPrimaryDns = _BackupPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 15),
    _BackupPrimaryDns_Type()
)
backupPrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupPrimaryDns.setStatus("current")
_BackupSecondaryDns_Type = IpAddress
_BackupSecondaryDns_Object = MibScalar
backupSecondaryDns = _BackupSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 16, 16),
    _BackupSecondaryDns_Type()
)
backupSecondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupSecondaryDns.setStatus("current")
_ZhnSystemTr69cObjects_ObjectIdentity = ObjectIdentity
zhnSystemTr69cObjects = _ZhnSystemTr69cObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17)
)
_SysTr69cConfigObjects_ObjectIdentity = ObjectIdentity
sysTr69cConfigObjects = _SysTr69cConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 1)
)
_SysTr69cConfigLoggingSOAP_Type = TruthValue
_SysTr69cConfigLoggingSOAP_Object = MibScalar
sysTr69cConfigLoggingSOAP = _SysTr69cConfigLoggingSOAP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 1, 1),
    _SysTr69cConfigLoggingSOAP_Type()
)
sysTr69cConfigLoggingSOAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTr69cConfigLoggingSOAP.setStatus("current")
_SysTr69cConfigConnectionRequestAuthentication_Type = TruthValue
_SysTr69cConfigConnectionRequestAuthentication_Object = MibScalar
sysTr69cConfigConnectionRequestAuthentication = _SysTr69cConfigConnectionRequestAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 1, 2),
    _SysTr69cConfigConnectionRequestAuthentication_Type()
)
sysTr69cConfigConnectionRequestAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTr69cConfigConnectionRequestAuthentication.setStatus("current")
_SysTr69cServerObjects_ObjectIdentity = ObjectIdentity
sysTr69cServerObjects = _SysTr69cServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2)
)


class _SysTr69cServerURL_Type(OctetString):
    """Custom type sysTr69cServerURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SysTr69cServerURL_Type.__name__ = "OctetString"
_SysTr69cServerURL_Object = MibScalar
sysTr69cServerURL = _SysTr69cServerURL_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 1),
    _SysTr69cServerURL_Type()
)
sysTr69cServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTr69cServerURL.setStatus("current")


class _SysTr69cServerLastConnectedURL_Type(OctetString):
    """Custom type sysTr69cServerLastConnectedURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SysTr69cServerLastConnectedURL_Type.__name__ = "OctetString"
_SysTr69cServerLastConnectedURL_Object = MibScalar
sysTr69cServerLastConnectedURL = _SysTr69cServerLastConnectedURL_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 2),
    _SysTr69cServerLastConnectedURL_Type()
)
sysTr69cServerLastConnectedURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTr69cServerLastConnectedURL.setStatus("current")


class _SysTr69cServerUsername_Type(OctetString):
    """Custom type sysTr69cServerUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SysTr69cServerUsername_Type.__name__ = "OctetString"
_SysTr69cServerUsername_Object = MibScalar
sysTr69cServerUsername = _SysTr69cServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 3),
    _SysTr69cServerUsername_Type()
)
sysTr69cServerUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTr69cServerUsername.setStatus("current")


class _SysTr69cServerPassword_Type(OctetString):
    """Custom type sysTr69cServerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SysTr69cServerPassword_Type.__name__ = "OctetString"
_SysTr69cServerPassword_Object = MibScalar
sysTr69cServerPassword = _SysTr69cServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 4),
    _SysTr69cServerPassword_Type()
)
sysTr69cServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTr69cServerPassword.setStatus("current")
_SysTr69cServerPeriodicInformEnable_Type = TruthValue
_SysTr69cServerPeriodicInformEnable_Object = MibScalar
sysTr69cServerPeriodicInformEnable = _SysTr69cServerPeriodicInformEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 5),
    _SysTr69cServerPeriodicInformEnable_Type()
)
sysTr69cServerPeriodicInformEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTr69cServerPeriodicInformEnable.setStatus("current")
_SysTr69cServerPeriodicInformInterval_Type = Unsigned32
_SysTr69cServerPeriodicInformInterval_Object = MibScalar
sysTr69cServerPeriodicInformInterval = _SysTr69cServerPeriodicInformInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 6),
    _SysTr69cServerPeriodicInformInterval_Type()
)
sysTr69cServerPeriodicInformInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTr69cServerPeriodicInformInterval.setStatus("current")


class _SysTr69cServerParameterKey_Type(OctetString):
    """Custom type sysTr69cServerParameterKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysTr69cServerParameterKey_Type.__name__ = "OctetString"
_SysTr69cServerParameterKey_Object = MibScalar
sysTr69cServerParameterKey = _SysTr69cServerParameterKey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 7),
    _SysTr69cServerParameterKey_Type()
)
sysTr69cServerParameterKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTr69cServerParameterKey.setStatus("current")


class _SysTr69cServerBoundIfName_Type(OctetString):
    """Custom type sysTr69cServerBoundIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysTr69cServerBoundIfName_Type.__name__ = "OctetString"
_SysTr69cServerBoundIfName_Object = MibScalar
sysTr69cServerBoundIfName = _SysTr69cServerBoundIfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 8),
    _SysTr69cServerBoundIfName_Type()
)
sysTr69cServerBoundIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTr69cServerBoundIfName.setStatus("current")


class _SysTr69cServerConnectionRequestURL_Type(OctetString):
    """Custom type sysTr69cServerConnectionRequestURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SysTr69cServerConnectionRequestURL_Type.__name__ = "OctetString"
_SysTr69cServerConnectionRequestURL_Object = MibScalar
sysTr69cServerConnectionRequestURL = _SysTr69cServerConnectionRequestURL_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 9),
    _SysTr69cServerConnectionRequestURL_Type()
)
sysTr69cServerConnectionRequestURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTr69cServerConnectionRequestURL.setStatus("current")


class _SysTr69cServerConnectionRequestUsername_Type(OctetString):
    """Custom type sysTr69cServerConnectionRequestUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SysTr69cServerConnectionRequestUsername_Type.__name__ = "OctetString"
_SysTr69cServerConnectionRequestUsername_Object = MibScalar
sysTr69cServerConnectionRequestUsername = _SysTr69cServerConnectionRequestUsername_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 10),
    _SysTr69cServerConnectionRequestUsername_Type()
)
sysTr69cServerConnectionRequestUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTr69cServerConnectionRequestUsername.setStatus("current")


class _SysTr69cServerConnectionRequestPassword_Type(OctetString):
    """Custom type sysTr69cServerConnectionRequestPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SysTr69cServerConnectionRequestPassword_Type.__name__ = "OctetString"
_SysTr69cServerConnectionRequestPassword_Object = MibScalar
sysTr69cServerConnectionRequestPassword = _SysTr69cServerConnectionRequestPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 11),
    _SysTr69cServerConnectionRequestPassword_Type()
)
sysTr69cServerConnectionRequestPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTr69cServerConnectionRequestPassword.setStatus("current")
_SysTr69cServerUpgradesManaged_Type = TruthValue
_SysTr69cServerUpgradesManaged_Object = MibScalar
sysTr69cServerUpgradesManaged = _SysTr69cServerUpgradesManaged_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 1, 17, 2, 12),
    _SysTr69cServerUpgradesManaged_Type()
)
sysTr69cServerUpgradesManaged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTr69cServerUpgradesManaged.setStatus("current")
_ZhnSystemConformance_ObjectIdentity = ObjectIdentity
zhnSystemConformance = _ZhnSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2)
)
_ZhnSystemGroups_ObjectIdentity = ObjectIdentity
zhnSystemGroups = _ZhnSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1)
)
_ZhnSystemCompliances_ObjectIdentity = ObjectIdentity
zhnSystemCompliances = _ZhnSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 2)
)

# Managed Objects groups

zhnSystemActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 1)
)
zhnSystemActiveGroup.setObjects(
      *(("ZHNSYSTEM", "modelNumber"),
        ("ZHNSYSTEM", "macBaseAddress"),
        ("ZHNSYSTEM", "numberOfMacAddresses"),
        ("ZHNSYSTEM", "numberOfBoards"),
        ("ZHNSYSTEM", "numberOfPlds"),
        ("ZHNSYSTEM", "numberOfRadios"),
        ("ZHNSYSTEM", "wifiNetworkType"),
        ("ZHNSYSTEM", "numberOfEthernetLikeInterfaces"),
        ("ZHNSYSTEM", "numberOfTemperatureSensors"),
        ("ZHNSYSTEM", "powerSupplyType"),
        ("ZHNSYSTEM", "sysBootloaderVersion"),
        ("ZHNSYSTEM", "sysFirmwareVersion"),
        ("ZHNSYSTEM", "sysAltFirmwareVersion"))
)
if mibBuilder.loadTexts:
    zhnSystemActiveGroup.setStatus("current")

zhnSystemTablesItems = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 2)
)
zhnSystemTablesItems.setObjects(
      *(("ZHNSYSTEM", "boardName"),
        ("ZHNSYSTEM", "boardPartNumber"),
        ("ZHNSYSTEM", "boardSerialNumber"),
        ("ZHNSYSTEM", "boardRevision"),
        ("ZHNSYSTEM", "pldName"),
        ("ZHNSYSTEM", "pldVersion"),
        ("ZHNSYSTEM", "etherName"),
        ("ZHNSYSTEM", "etherType"),
        ("ZHNSYSTEM", "etherSubtype"),
        ("ZHNSYSTEM", "etherNumberOfPorts"),
        ("ZHNSYSTEM", "etherLinePower"),
        ("ZHNSYSTEM", "etherPowerPairs"),
        ("ZHNSYSTEM", "temperatureSensorName"),
        ("ZHNSYSTEM", "temperatureSensorMaximum"),
        ("ZHNSYSTEM", "temperatureSensorMinimum"))
)
if mibBuilder.loadTexts:
    zhnSystemTablesItems.setStatus("current")

zhnSystemConfigItems = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 3)
)
zhnSystemConfigItems.setObjects(
      *(("ZHNSYSTEM", "locationLatitude"),
        ("ZHNSYSTEM", "locationLongitude"),
        ("ZHNSYSTEM", "zhnSystemAction"),
        ("ZHNSYSTEM", "zhnSysLocation"),
        ("ZHNSYSTEM", "zhnSysContact"),
        ("ZHNSYSTEM", "sysTransmitClockSource"),
        ("ZHNSYSTEM", "sysLocalTimingReference"),
        ("ZHNSYSTEM", "sysSynchronizationMode"),
        ("ZHNSYSTEM", "sysSynchronousEthernet"),
        ("ZHNSYSTEM", "sysClockMode"),
        ("ZHNSYSTEM", "sysCfgDBAction"),
        ("ZHNSYSTEM", "sysSoftwareReboot"),
        ("ZHNSYSTEM", "sysRestoreAltFirmwareVersion"),
        ("ZHNSYSTEM", "sysSnmpProvisioningLock"),
        ("ZHNSYSTEM", "sysSnmpProvisioningChange"))
)
if mibBuilder.loadTexts:
    zhnSystemConfigItems.setStatus("current")

zhnSystemTrapItems = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 4)
)
zhnSystemTrapItems.setObjects(
      *(("ZHNSYSTEM", "numberOfTrapManagers"),
        ("ZHNSYSTEM", "zhnDefaultTrapCommunity"),
        ("ZHNSYSTEM", "zhnTrapTypeLinkUpDown"),
        ("ZHNSYSTEM", "zhnTrapTypeAuthFailure"),
        ("ZHNSYSTEM", "zhnTrapTypeConfigChange"),
        ("ZHNSYSTEM", "trapCommunityName"),
        ("ZHNSYSTEM", "trapVersion"),
        ("ZHNSYSTEM", "trapPort"),
        ("ZHNSYSTEM", "trapRowStatus"),
        ("ZHNSYSTEM", "zhnTrapTypeColdStart"),
        ("ZHNSYSTEM", "zhnTrapTypeWarmStart"),
        ("ZHNSYSTEM", "zhnTrapTypeEnterprise"))
)
if mibBuilder.loadTexts:
    zhnSystemTrapItems.setStatus("current")

zhnSystemCommunityItems = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 5)
)
zhnSystemCommunityItems.setObjects(
      *(("ZHNSYSTEM", "numberOfCommunities"),
        ("ZHNSYSTEM", "communityType"),
        ("ZHNSYSTEM", "communityRowStatus"))
)
if mibBuilder.loadTexts:
    zhnSystemCommunityItems.setStatus("current")

zhnSystemFixedCommunityItems = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 6)
)
zhnSystemFixedCommunityItems.setObjects(
      *(("ZHNSYSTEM", "fixedCommunityName"),
        ("ZHNSYSTEM", "fixedCommunityType"),
        ("ZHNSYSTEM", "fixedCommunityRowStatus"))
)
if mibBuilder.loadTexts:
    zhnSystemFixedCommunityItems.setStatus("current")

zhnSystemClockingItems = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 7)
)
zhnSystemClockingItems.setObjects(
      *(("ZHNSYSTEM", "sysSystemClockSource"),
        ("ZHNSYSTEM", "sysEthernetTransmitClockSource"),
        ("ZHNSYSTEM", "sysDs1ClockSourcePort"))
)
if mibBuilder.loadTexts:
    zhnSystemClockingItems.setStatus("current")

zhnSyslogConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 8)
)
zhnSyslogConfigGroup.setObjects(
      *(("ZHNSYSTEM", "sysLogAdminStatus"),
        ("ZHNSYSTEM", "sysLogLocalLogLevel"),
        ("ZHNSYSTEM", "sysLogRemoteLogLevel"),
        ("ZHNSYSTEM", "sysLogDisplayLogLevel"),
        ("ZHNSYSTEM", "sysLogMode"),
        ("ZHNSYSTEM", "sysLogRemoteServerAddress"),
        ("ZHNSYSTEM", "sysLogRemoteServerPort"))
)
if mibBuilder.loadTexts:
    zhnSyslogConfigGroup.setStatus("current")

zhnSntpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 9)
)
zhnSntpConfigGroup.setObjects(
      *(("ZHNSYSTEM", "sntpAdminStatus"),
        ("ZHNSYSTEM", "sntpOperStatus"),
        ("ZHNSYSTEM", "sntpServer1"),
        ("ZHNSYSTEM", "sntpServer2"),
        ("ZHNSYSTEM", "sntpServer3"),
        ("ZHNSYSTEM", "sntpServer4"),
        ("ZHNSYSTEM", "sntpServer5"),
        ("ZHNSYSTEM", "sntpLocalTimeZone"),
        ("ZHNSYSTEM", "sntpCurrentDateAndTime"))
)
if mibBuilder.loadTexts:
    zhnSntpConfigGroup.setStatus("current")

zhnUserLoginGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 10)
)
zhnUserLoginGroup.setObjects(
      *(("ZHNSYSTEM", "adminUserName"),
        ("ZHNSYSTEM", "adminPassword"),
        ("ZHNSYSTEM", "supportUserName"),
        ("ZHNSYSTEM", "supportPassword"),
        ("ZHNSYSTEM", "userUserName"),
        ("ZHNSYSTEM", "userPassword"))
)
if mibBuilder.loadTexts:
    zhnUserLoginGroup.setStatus("current")

zhnPowerSheddingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 11)
)
zhnPowerSheddingGroup.setObjects(
      *(("ZHNSYSTEM", "powerSheddingAdminStatus"),
        ("ZHNSYSTEM", "powerSheddingShutdownDelay"),
        ("ZHNSYSTEM", "powerSheddingRestoreDelay"))
)
if mibBuilder.loadTexts:
    zhnPowerSheddingGroup.setStatus("current")

zhnSystemFirewallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 12)
)
zhnSystemFirewallGroup.setObjects(
      *(("ZHNSYSTEM", "sysFirewallEnable"),
        ("ZHNSYSTEM", "sysFirewallTcpSynCookies"))
)
if mibBuilder.loadTexts:
    zhnSystemFirewallGroup.setStatus("current")

zhnSystemDNSClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 13)
)
zhnSystemDNSClientGroup.setObjects(
      *(("ZHNSYSTEM", "sysDNSAddressingType"),
        ("ZHNSYSTEM", "sysDNSDHCPSource"),
        ("ZHNSYSTEM", "sysDNSPrimaryIPAddress"),
        ("ZHNSYSTEM", "sysDNSSecondaryIPAddress"))
)
if mibBuilder.loadTexts:
    zhnSystemDNSClientGroup.setStatus("current")

zhnSystemDNSProxyHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 14)
)
zhnSystemDNSProxyHostGroup.setObjects(
      *(("ZHNSYSTEM", "zhnDnsProxyHostMaxHostEntries"),
        ("ZHNSYSTEM", "dnsProxyHostIPAddress"),
        ("ZHNSYSTEM", "dnsProxyHostName"),
        ("ZHNSYSTEM", "dnsProxyRowStatus"))
)
if mibBuilder.loadTexts:
    zhnSystemDNSProxyHostGroup.setStatus("current")

zhnSystemWanBackupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 15)
)
zhnSystemWanBackupGroup.setObjects(
      *(("ZHNSYSTEM", "failoverTimer"),
        ("ZHNSYSTEM", "restoralTimer"),
        ("ZHNSYSTEM", "backupDataVlan"),
        ("ZHNSYSTEM", "cellularPinNumber"),
        ("ZHNSYSTEM", "cellularDataNumber"),
        ("ZHNSYSTEM", "atInitCommands"),
        ("ZHNSYSTEM", "accessPointName"),
        ("ZHNSYSTEM", "chapPapUsername"),
        ("ZHNSYSTEM", "chapPapPassword"),
        ("ZHNSYSTEM", "connectionTimeout"),
        ("ZHNSYSTEM", "backupIpAddressMode"),
        ("ZHNSYSTEM", "backupIpAddress"),
        ("ZHNSYSTEM", "backupDefaultGateway"),
        ("ZHNSYSTEM", "backupSubnetMask"),
        ("ZHNSYSTEM", "backupPrimaryDns"),
        ("ZHNSYSTEM", "backupSecondaryDns"))
)
if mibBuilder.loadTexts:
    zhnSystemWanBackupGroup.setStatus("current")

zhnSystemTr69cGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 1, 16)
)
zhnSystemTr69cGroup.setObjects(
      *(("ZHNSYSTEM", "sysTr69cConfigLoggingSOAP"),
        ("ZHNSYSTEM", "sysTr69cConfigConnectionRequestAuthentication"),
        ("ZHNSYSTEM", "sysTr69cServerURL"),
        ("ZHNSYSTEM", "sysTr69cServerLastConnectedURL"),
        ("ZHNSYSTEM", "sysTr69cServerUsername"),
        ("ZHNSYSTEM", "sysTr69cServerPassword"),
        ("ZHNSYSTEM", "sysTr69cServerPeriodicInformEnable"),
        ("ZHNSYSTEM", "sysTr69cServerPeriodicInformInterval"),
        ("ZHNSYSTEM", "sysTr69cServerParameterKey"),
        ("ZHNSYSTEM", "sysTr69cServerBoundIfName"),
        ("ZHNSYSTEM", "sysTr69cServerConnectionRequestURL"),
        ("ZHNSYSTEM", "sysTr69cServerConnectionRequestUsername"),
        ("ZHNSYSTEM", "sysTr69cServerConnectionRequestPassword"),
        ("ZHNSYSTEM", "sysTr69cServerUpgradesManaged"))
)
if mibBuilder.loadTexts:
    zhnSystemTr69cGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zhnSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    zhnSystemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNSYSTEM",
    **{"WFNT": WFNT,
       "ELTYPE": ELTYPE,
       "ELSUBTYPE": ELSUBTYPE,
       "LPT": LPT,
       "UPT": UPT,
       "TCSI": TCSI,
       "LTRI": LTRI,
       "CSMI": CSMI,
       "SEI": SEI,
       "CMI": CMI,
       "CDA": CDA,
       "RBT": RBT,
       "SCS": SCS,
       "ETCS": ETCS,
       "SysFirmwareAction": SysFirmwareAction,
       "SysAdminStatus": SysAdminStatus,
       "SysLogLevel": SysLogLevel,
       "SysLogMode": SysLogMode,
       "SysSntpTimeZones": SysSntpTimeZones,
       "IPInterfaceAddressingTypeValues": IPInterfaceAddressingTypeValues,
       "BasicAddressingTypeValues": BasicAddressingTypeValues,
       "zhnSystem": zhnSystem,
       "zhnSystemObjects": zhnSystemObjects,
       "zhnSystemGeneralObjects": zhnSystemGeneralObjects,
       "modelNumber": modelNumber,
       "macBaseAddress": macBaseAddress,
       "numberOfMacAddresses": numberOfMacAddresses,
       "wifiNetworkType": wifiNetworkType,
       "powerSupplyType": powerSupplyType,
       "locationLatitude": locationLatitude,
       "locationLongitude": locationLongitude,
       "zhnSystemAction": zhnSystemAction,
       "zhnSysLocation": zhnSysLocation,
       "zhnSysContact": zhnSysContact,
       "sysTransmitClockSource": sysTransmitClockSource,
       "sysLocalTimingReference": sysLocalTimingReference,
       "sysSynchronizationMode": sysSynchronizationMode,
       "sysSynchronousEthernet": sysSynchronousEthernet,
       "sysClockMode": sysClockMode,
       "sysCfgDBAction": sysCfgDBAction,
       "sysSoftwareReboot": sysSoftwareReboot,
       "sysSystemClockSource": sysSystemClockSource,
       "sysEthernetTransmitClockSource": sysEthernetTransmitClockSource,
       "sysDs1ClockSourcePort": sysDs1ClockSourcePort,
       "sysBootloaderVersion": sysBootloaderVersion,
       "sysFirmwareVersion": sysFirmwareVersion,
       "sysAltFirmwareVersion": sysAltFirmwareVersion,
       "sysRestoreAltFirmwareVersion": sysRestoreAltFirmwareVersion,
       "sysSnmpProvisioningLock": sysSnmpProvisioningLock,
       "sysSnmpProvisioningChange": sysSnmpProvisioningChange,
       "zhnSystemBoardObjects": zhnSystemBoardObjects,
       "numberOfBoards": numberOfBoards,
       "boardDescriptorTable": boardDescriptorTable,
       "boardDescriptorEntry": boardDescriptorEntry,
       "boardIndex": boardIndex,
       "boardName": boardName,
       "boardPartNumber": boardPartNumber,
       "boardSerialNumber": boardSerialNumber,
       "boardRevision": boardRevision,
       "zhnSystemPldObjects": zhnSystemPldObjects,
       "numberOfPlds": numberOfPlds,
       "pldDescriptorTable": pldDescriptorTable,
       "pldDescriptorEntry": pldDescriptorEntry,
       "pldIndex": pldIndex,
       "pldName": pldName,
       "pldVersion": pldVersion,
       "zhnSystemRadioObjects": zhnSystemRadioObjects,
       "numberOfRadios": numberOfRadios,
       "zhnSystemEthernetLikeObjects": zhnSystemEthernetLikeObjects,
       "numberOfEthernetLikeInterfaces": numberOfEthernetLikeInterfaces,
       "ethernetlikeInterfaceTable": ethernetlikeInterfaceTable,
       "ethernetlikeInterfaceEntry": ethernetlikeInterfaceEntry,
       "etherIndex": etherIndex,
       "etherName": etherName,
       "etherType": etherType,
       "etherSubtype": etherSubtype,
       "etherNumberOfPorts": etherNumberOfPorts,
       "etherLinePower": etherLinePower,
       "etherPowerPairs": etherPowerPairs,
       "zhnSystemTempSensorObjects": zhnSystemTempSensorObjects,
       "numberOfTemperatureSensors": numberOfTemperatureSensors,
       "temperatureSensorTable": temperatureSensorTable,
       "temperatureSensorEntry": temperatureSensorEntry,
       "temperatureSensorIndex": temperatureSensorIndex,
       "temperatureSensorName": temperatureSensorName,
       "temperatureSensorMaximum": temperatureSensorMaximum,
       "temperatureSensorMinimum": temperatureSensorMinimum,
       "zhnSystemSNMPObjects": zhnSystemSNMPObjects,
       "numberOfCommunities": numberOfCommunities,
       "zhnCommunityTable": zhnCommunityTable,
       "zhnCommunityTableEntry": zhnCommunityTableEntry,
       "communityName": communityName,
       "communityType": communityType,
       "communityRowStatus": communityRowStatus,
       "zhnFixedCommunityTable": zhnFixedCommunityTable,
       "zhnFixedCommunityTableEntry": zhnFixedCommunityTableEntry,
       "fixedCommunityName": fixedCommunityName,
       "fixedCommunityType": fixedCommunityType,
       "fixedCommunityRowStatus": fixedCommunityRowStatus,
       "zhnSystemTrapObjects": zhnSystemTrapObjects,
       "numberOfTrapManagers": numberOfTrapManagers,
       "zhnDefaultTrapCommunity": zhnDefaultTrapCommunity,
       "zhnTrapTypeLinkUpDown": zhnTrapTypeLinkUpDown,
       "zhnTrapTypeAuthFailure": zhnTrapTypeAuthFailure,
       "zhnTrapTypeConfigChange": zhnTrapTypeConfigChange,
       "zhnTrapManagerInfoTable": zhnTrapManagerInfoTable,
       "zhnTrapManagerInfoTableEntry": zhnTrapManagerInfoTableEntry,
       "trapDestination": trapDestination,
       "trapCommunityName": trapCommunityName,
       "trapVersion": trapVersion,
       "trapPort": trapPort,
       "trapRowStatus": trapRowStatus,
       "zhnTrapTypeColdStart": zhnTrapTypeColdStart,
       "zhnTrapTypeWarmStart": zhnTrapTypeWarmStart,
       "zhnTrapTypeEnterprise": zhnTrapTypeEnterprise,
       "zhnSystemSyslogObjects": zhnSystemSyslogObjects,
       "sysLogAdminStatus": sysLogAdminStatus,
       "sysLogLocalLogLevel": sysLogLocalLogLevel,
       "sysLogRemoteLogLevel": sysLogRemoteLogLevel,
       "sysLogDisplayLogLevel": sysLogDisplayLogLevel,
       "sysLogMode": sysLogMode,
       "sysLogRemoteServerAddress": sysLogRemoteServerAddress,
       "sysLogRemoteServerPort": sysLogRemoteServerPort,
       "zhnSystemSNTPObjects": zhnSystemSNTPObjects,
       "sntpAdminStatus": sntpAdminStatus,
       "sntpOperStatus": sntpOperStatus,
       "sntpServer1": sntpServer1,
       "sntpServer2": sntpServer2,
       "sntpServer3": sntpServer3,
       "sntpServer4": sntpServer4,
       "sntpServer5": sntpServer5,
       "sntpLocalTimeZone": sntpLocalTimeZone,
       "sntpCurrentDateAndTime": sntpCurrentDateAndTime,
       "zhnSystemUserLoginObjects": zhnSystemUserLoginObjects,
       "adminUserName": adminUserName,
       "adminPassword": adminPassword,
       "supportUserName": supportUserName,
       "supportPassword": supportPassword,
       "userUserName": userUserName,
       "userPassword": userPassword,
       "zhnSystemPowerSheddingObjects": zhnSystemPowerSheddingObjects,
       "powerSheddingAdminStatus": powerSheddingAdminStatus,
       "powerSheddingShutdownDelay": powerSheddingShutdownDelay,
       "powerSheddingRestoreDelay": powerSheddingRestoreDelay,
       "zhnSystemFirewallObjects": zhnSystemFirewallObjects,
       "sysFirewallEnable": sysFirewallEnable,
       "sysFirewallTcpSynCookies": sysFirewallTcpSynCookies,
       "zhnSystemDNSClientObjects": zhnSystemDNSClientObjects,
       "sysDNSAddressingType": sysDNSAddressingType,
       "sysDNSDHCPSource": sysDNSDHCPSource,
       "sysDNSPrimaryIPAddress": sysDNSPrimaryIPAddress,
       "sysDNSSecondaryIPAddress": sysDNSSecondaryIPAddress,
       "zhnSystemDNSProxyObjects": zhnSystemDNSProxyObjects,
       "zhnDnsProxyHostMaxHostEntries": zhnDnsProxyHostMaxHostEntries,
       "zhnDnsProxyHostTable": zhnDnsProxyHostTable,
       "zhnDnsProxyHostEntry": zhnDnsProxyHostEntry,
       "dnsProxyHostIndex": dnsProxyHostIndex,
       "dnsProxyHostIPAddress": dnsProxyHostIPAddress,
       "dnsProxyHostName": dnsProxyHostName,
       "dnsProxyRowStatus": dnsProxyRowStatus,
       "zhnSystemWanBackupObjects": zhnSystemWanBackupObjects,
       "failoverTimer": failoverTimer,
       "restoralTimer": restoralTimer,
       "backupDataVlan": backupDataVlan,
       "cellularPinNumber": cellularPinNumber,
       "cellularDataNumber": cellularDataNumber,
       "atInitCommands": atInitCommands,
       "accessPointName": accessPointName,
       "chapPapUsername": chapPapUsername,
       "chapPapPassword": chapPapPassword,
       "connectionTimeout": connectionTimeout,
       "backupIpAddressMode": backupIpAddressMode,
       "backupIpAddress": backupIpAddress,
       "backupDefaultGateway": backupDefaultGateway,
       "backupSubnetMask": backupSubnetMask,
       "backupPrimaryDns": backupPrimaryDns,
       "backupSecondaryDns": backupSecondaryDns,
       "zhnSystemTr69cObjects": zhnSystemTr69cObjects,
       "sysTr69cConfigObjects": sysTr69cConfigObjects,
       "sysTr69cConfigLoggingSOAP": sysTr69cConfigLoggingSOAP,
       "sysTr69cConfigConnectionRequestAuthentication": sysTr69cConfigConnectionRequestAuthentication,
       "sysTr69cServerObjects": sysTr69cServerObjects,
       "sysTr69cServerURL": sysTr69cServerURL,
       "sysTr69cServerLastConnectedURL": sysTr69cServerLastConnectedURL,
       "sysTr69cServerUsername": sysTr69cServerUsername,
       "sysTr69cServerPassword": sysTr69cServerPassword,
       "sysTr69cServerPeriodicInformEnable": sysTr69cServerPeriodicInformEnable,
       "sysTr69cServerPeriodicInformInterval": sysTr69cServerPeriodicInformInterval,
       "sysTr69cServerParameterKey": sysTr69cServerParameterKey,
       "sysTr69cServerBoundIfName": sysTr69cServerBoundIfName,
       "sysTr69cServerConnectionRequestURL": sysTr69cServerConnectionRequestURL,
       "sysTr69cServerConnectionRequestUsername": sysTr69cServerConnectionRequestUsername,
       "sysTr69cServerConnectionRequestPassword": sysTr69cServerConnectionRequestPassword,
       "sysTr69cServerUpgradesManaged": sysTr69cServerUpgradesManaged,
       "zhnSystemConformance": zhnSystemConformance,
       "zhnSystemGroups": zhnSystemGroups,
       "zhnSystemActiveGroup": zhnSystemActiveGroup,
       "zhnSystemTablesItems": zhnSystemTablesItems,
       "zhnSystemConfigItems": zhnSystemConfigItems,
       "zhnSystemTrapItems": zhnSystemTrapItems,
       "zhnSystemCommunityItems": zhnSystemCommunityItems,
       "zhnSystemFixedCommunityItems": zhnSystemFixedCommunityItems,
       "zhnSystemClockingItems": zhnSystemClockingItems,
       "zhnSyslogConfigGroup": zhnSyslogConfigGroup,
       "zhnSntpConfigGroup": zhnSntpConfigGroup,
       "zhnUserLoginGroup": zhnUserLoginGroup,
       "zhnPowerSheddingGroup": zhnPowerSheddingGroup,
       "zhnSystemFirewallGroup": zhnSystemFirewallGroup,
       "zhnSystemDNSClientGroup": zhnSystemDNSClientGroup,
       "zhnSystemDNSProxyHostGroup": zhnSystemDNSProxyHostGroup,
       "zhnSystemWanBackupGroup": zhnSystemWanBackupGroup,
       "zhnSystemTr69cGroup": zhnSystemTr69cGroup,
       "zhnSystemCompliances": zhnSystemCompliances,
       "zhnSystemCompliance": zhnSystemCompliance}
)
