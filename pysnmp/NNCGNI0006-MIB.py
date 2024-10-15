# SNMP MIB module (NNCGNI0006-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCGNI0006-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:19 2024
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

(nncExtCodeSpace,
 nncExtDiag,
 nncExtEnvironmental,
 nncExtNVM,
 nncExtProbe,
 nncExtRestart,
 nncExtSystem,
 nncLegacyModules) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtCodeSpace",
    "nncExtDiag",
    "nncExtEnvironmental",
    "nncExtNVM",
    "nncExtProbe",
    "nncExtRestart",
    "nncExtSystem",
    "nncLegacyModules")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nncExtBasics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RestartCause(Integer32, TextualConvention):
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
              15,
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
              72)
        )
    )
    namedValues = NamedValues(
        *(("trblAddressError", 3),
          ("trblBadFlashConfig", 55),
          ("trblBusError", 2),
          ("trblCPUReset", 71),
          ("trblChkFailure", 6),
          ("trblCopyRamToFlash", 53),
          ("trblDCMPDeath", 62),
          ("trblDnldAborted", 54),
          ("trblDspDead", 61),
          ("trblDspDiedOnTx", 60),
          ("trblDspDnldFailed", 58),
          ("trblDspPollFailed", 59),
          ("trblDspReset", 57),
          ("trblIllegalInst", 4),
          ("trblIntLevel1", 25),
          ("trblIntLevel2", 26),
          ("trblIntLevel3", 27),
          ("trblIntLevel4", 28),
          ("trblIntLevel5", 29),
          ("trblIntLevel6", 30),
          ("trblIntLevel7", 31),
          ("trblLine1010", 10),
          ("trblLine1111", 11),
          ("trblNCIReload", 69),
          ("trblNCIReset", 49),
          ("trblNCIRunMinusOne", 50),
          ("trblNVMReset", 56),
          ("trblPanic", 51),
          ("trblPrivilege", 8),
          ("trblPushButton", 70),
          ("trblRDSReset", 72),
          ("trblRunBootProm", 52),
          ("trblRunningLowComms", 63),
          ("trblRunningLowFrame", 64),
          ("trblRunningLowMgmt", 67),
          ("trblRunningLowPoolUnknown", 68),
          ("trblRunningLowSonic", 66),
          ("trblRunningLowSys", 65),
          ("trblSpurious", 24),
          ("trblTraceTrap", 9),
          ("trblTrap00", 32),
          ("trblTrap01", 33),
          ("trblTrap02", 34),
          ("trblTrap03", 35),
          ("trblTrap04", 36),
          ("trblTrap05", 37),
          ("trblTrap06", 38),
          ("trblTrap07", 39),
          ("trblTrap08", 40),
          ("trblTrap09", 41),
          ("trblTrap10", 42),
          ("trblTrap11", 43),
          ("trblTrap12", 44),
          ("trblTrap13", 45),
          ("trblTrap14", 46),
          ("trblTrap15", 47),
          ("trblTrapVInst", 7),
          ("trblUninitialized", 15),
          ("trblUnknown", 1),
          ("trblWatchDog", 48),
          ("trblZeroDivide", 5),
          ("trblnoProblem", 0))
    )



class Nci2DeviceIDType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
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
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              93,
              97,
              101,
              102,
              112)
        )
    )
    namedValues = NamedValues(
        *(("bert2601", 53),
          ("bert2602", 54),
          ("bert2603", 55),
          ("bertMgr", 61),
          ("bri3600St", 80),
          ("dclcRs232", 7),
          ("dclcRs422", 62),
          ("dclcV35", 9),
          ("dclcX21", 8),
          ("dcp3600", 2),
          ("detE1", 25),
          ("detT1", 24),
          ("dpm3600", 23),
          ("dsp3600", 22),
          ("dtu2601", 4),
          ("dtu2601Anm", 18),
          ("dtu2602", 5),
          ("dtu2602Anm", 19),
          ("dtu2603", 6),
          ("dtu2603Anm", 20),
          ("dtu2606", 33),
          ("dtu2608", 21),
          ("dtu2610Pad", 32),
          ("dtu2701", 50),
          ("dtu2701Anm", 56),
          ("dtu2702", 51),
          ("dtu2702Anm", 57),
          ("dtu2703", 52),
          ("dtu2703Anm", 58),
          ("dtu2704", 73),
          ("eapApi", 63),
          ("elb8230", 42),
          ("er8231", 65),
          ("esn3700", 70),
          ("esnEsc", 71),
          ("esnOne", 72),
          ("ldm1121", 11),
          ("ldm1124", 10),
          ("ldm1135", 12),
          ("nc1615C", 46),
          ("nc3600", 1),
          ("nc3606Data", 48),
          ("nc3606Voice", 47),
          ("nc3612", 16),
          ("nc36150", 69),
          ("nc36170", 79),
          ("nc3620", 77),
          ("nc3624", 15),
          ("nc3630", 17),
          ("nc3645PE", 31),
          ("nc3645SE", 30),
          ("nc3664", 68),
          ("ncATMNIC", 84),
          ("ncBlueRidge", 97),
          ("ncCampusSwitch", 112),
          ("ncDS3", 35),
          ("ncELSU", 93),
          ("ncFRATM", 81),
          ("ncOrangeRidge", 101),
          ("ncRedRidge", 102),
          ("ncRouteServer", 82),
          ("ncSystemManager", 83),
          ("ncWgs", 78),
          ("ncYellowRidge", 85),
          ("ncdE3", 64),
          ("nmu4601", 13),
          ("nmu4601A", 26),
          ("nmu4602", 14),
          ("nmu4602Cn", 75),
          ("nmu4602Dn", 74),
          ("nmu4602Rn", 76),
          ("nmu4605", 27),
          ("nmu5602", 28),
          ("nmu5610", 29),
          ("nmu5610ci", 34),
          ("nmu8001", 60),
          ("nvp1000", 49),
          ("nvpEdsp", 45),
          ("nvpSysMgr", 43),
          ("nvpVoiceSrvr", 44),
          ("pte", 67),
          ("ta1601S", 36),
          ("ta1601U", 37),
          ("ta1602S", 38),
          ("ta1602U", 39),
          ("ta1603S", 40),
          ("ta1603U", 41),
          ("tap", 59),
          ("tr8251", 66),
          ("unknown", 0))
    )



class CurrentGenericType(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class ProductPartNumberType(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class CardIDType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              51,
              57,
              58,
              59,
              60,
              61,
              62)
        )
    )
    namedValues = NamedValues(
        *(("coElsu10BaseTBackplane", 62),
          ("coElsuAtmCard", 58),
          ("coElsuMainCard", 59),
          ("cpElsuMainCard", 57),
          ("elsuAuiBackplane", 61),
          ("elsuDisplayModule", 60),
          ("unknown", 0),
          ("yellowRidgeBufferModule", 7),
          ("yellowRidgeLEDBoard", 5),
          ("yellowRidgeMainCard", 4),
          ("yellowRidgeOc3MmfPdmModule", 6),
          ("yellowRidgeOc3SmfPdmModule", 51))
    )



class CardSerialNumberType(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-2d,1d,8d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )



class NncSwStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("empty", 4),
          ("error", 3),
          ("notApplicable", 1),
          ("ok", 2))
    )



class NncSwBank(Integer32, TextualConvention):
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
              257)
        )
    )
    namedValues = NamedValues(
        *(("bank1", 2),
          ("bank10", 11),
          ("bank11", 12),
          ("bank12", 13),
          ("bank13", 14),
          ("bank14", 15),
          ("bank15", 16),
          ("bank16", 17),
          ("bank17", 18),
          ("bank18", 19),
          ("bank19", 20),
          ("bank2", 3),
          ("bank20", 21),
          ("bank21", 22),
          ("bank22", 23),
          ("bank23", 24),
          ("bank24", 25),
          ("bank25", 26),
          ("bank26", 27),
          ("bank27", 28),
          ("bank28", 29),
          ("bank29", 30),
          ("bank3", 4),
          ("bank30", 31),
          ("bank31", 32),
          ("bank32", 33),
          ("bank4", 5),
          ("bank5", 6),
          ("bank6", 7),
          ("bank7", 8),
          ("bank8", 9),
          ("bank9", 10),
          ("bootbank", 1),
          ("notapplicable", 0),
          ("unknown", 257))
    )



class FanStatusType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("ok", 0))
    )



class PwrSupplyStatusType(Integer32, TextualConvention):
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
        *(("noAc", 1),
          ("noDc", 2),
          ("notPresent", 3),
          ("ok", 0))
    )



class CodeSpaceIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )



class NVMPoolIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )



class SvcEpdOptionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class SvcPpdOptionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



# MIB Managed Objects in the order of their OIDs



class _NncExtSysProductName_Type(DisplayString):
    """Custom type nncExtSysProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_NncExtSysProductName_Type.__name__ = "DisplayString"
_NncExtSysProductName_Object = MibScalar
nncExtSysProductName = _NncExtSysProductName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 1),
    _NncExtSysProductName_Type()
)
nncExtSysProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSysProductName.setStatus("current")
_NncExtSysCurrentGeneric_Type = CurrentGenericType
_NncExtSysCurrentGeneric_Object = MibScalar
nncExtSysCurrentGeneric = _NncExtSysCurrentGeneric_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 2),
    _NncExtSysCurrentGeneric_Type()
)
nncExtSysCurrentGeneric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSysCurrentGeneric.setStatus("current")
_NncExtSysProductPartNumber_Type = ProductPartNumberType
_NncExtSysProductPartNumber_Object = MibScalar
nncExtSysProductPartNumber = _NncExtSysProductPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 3),
    _NncExtSysProductPartNumber_Type()
)
nncExtSysProductPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSysProductPartNumber.setStatus("current")
_NncExtSysNci2DeviceID_Type = Nci2DeviceIDType
_NncExtSysNci2DeviceID_Object = MibScalar
nncExtSysNci2DeviceID = _NncExtSysNci2DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 4),
    _NncExtSysNci2DeviceID_Type()
)
nncExtSysNci2DeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSysNci2DeviceID.setStatus("current")
_NncExtSysCurrentDateAndTime_Type = DateAndTime
_NncExtSysCurrentDateAndTime_Object = MibScalar
nncExtSysCurrentDateAndTime = _NncExtSysCurrentDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 5),
    _NncExtSysCurrentDateAndTime_Type()
)
nncExtSysCurrentDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtSysCurrentDateAndTime.setStatus("current")
_NncExtSysCardTable_Object = MibTable
nncExtSysCardTable = _NncExtSysCardTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 6)
)
if mibBuilder.loadTexts:
    nncExtSysCardTable.setStatus("current")
_NncExtSysCardEntry_Object = MibTableRow
nncExtSysCardEntry = _NncExtSysCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1)
)
nncExtSysCardEntry.setIndexNames(
    (0, "NNCGNI0006-MIB", "nncExtSysCardIndex"),
)
if mibBuilder.loadTexts:
    nncExtSysCardEntry.setStatus("current")
_NncExtSysCardIndex_Type = Integer32
_NncExtSysCardIndex_Object = MibTableColumn
nncExtSysCardIndex = _NncExtSysCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 1),
    _NncExtSysCardIndex_Type()
)
nncExtSysCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSysCardIndex.setStatus("current")
_NncExtSysCardIDType_Type = CardIDType
_NncExtSysCardIDType_Object = MibTableColumn
nncExtSysCardIDType = _NncExtSysCardIDType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 2),
    _NncExtSysCardIDType_Type()
)
nncExtSysCardIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSysCardIDType.setStatus("current")


class _NncExtSysCardName_Type(OctetString):
    """Custom type nncExtSysCardName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NncExtSysCardName_Type.__name__ = "OctetString"
_NncExtSysCardName_Object = MibTableColumn
nncExtSysCardName = _NncExtSysCardName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 3),
    _NncExtSysCardName_Type()
)
nncExtSysCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSysCardName.setStatus("current")
_NncExtSysCardSerialNumber_Type = CardSerialNumberType
_NncExtSysCardSerialNumber_Object = MibTableColumn
nncExtSysCardSerialNumber = _NncExtSysCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 6, 1, 4),
    _NncExtSysCardSerialNumber_Type()
)
nncExtSysCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSysCardSerialNumber.setStatus("current")


class _NncExtEnvFanStatus_Type(Integer32):
    """Custom type nncExtEnvFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fanFailed", 2),
          ("fanOk", 1))
    )


_NncExtEnvFanStatus_Type.__name__ = "Integer32"
_NncExtEnvFanStatus_Object = MibScalar
nncExtEnvFanStatus = _NncExtEnvFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 1),
    _NncExtEnvFanStatus_Type()
)
nncExtEnvFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvFanStatus.setStatus("current")


class _NncExtEnvTemperatureSensor_Type(Integer32):
    """Custom type nncExtEnvTemperatureSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("tooHot", 2))
    )


_NncExtEnvTemperatureSensor_Type.__name__ = "Integer32"
_NncExtEnvTemperatureSensor_Object = MibScalar
nncExtEnvTemperatureSensor = _NncExtEnvTemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 2),
    _NncExtEnvTemperatureSensor_Type()
)
nncExtEnvTemperatureSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvTemperatureSensor.setStatus("current")


class _NncExtEnvPlus12Status_Type(Integer32):
    """Custom type nncExtEnvPlus12Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("outOfSpec", 2))
    )


_NncExtEnvPlus12Status_Type.__name__ = "Integer32"
_NncExtEnvPlus12Status_Object = MibScalar
nncExtEnvPlus12Status = _NncExtEnvPlus12Status_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 3),
    _NncExtEnvPlus12Status_Type()
)
nncExtEnvPlus12Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvPlus12Status.setStatus("current")


class _NncExtEnvMinus12Status_Type(Integer32):
    """Custom type nncExtEnvMinus12Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("outOfSpec", 2))
    )


_NncExtEnvMinus12Status_Type.__name__ = "Integer32"
_NncExtEnvMinus12Status_Object = MibScalar
nncExtEnvMinus12Status = _NncExtEnvMinus12Status_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 4),
    _NncExtEnvMinus12Status_Type()
)
nncExtEnvMinus12Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvMinus12Status.setStatus("current")
_NncExtEnvFanTable_Object = MibTable
nncExtEnvFanTable = _NncExtEnvFanTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 5)
)
if mibBuilder.loadTexts:
    nncExtEnvFanTable.setStatus("current")
_NncExtEnvFanTableEntry_Object = MibTableRow
nncExtEnvFanTableEntry = _NncExtEnvFanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 5, 1)
)
nncExtEnvFanTableEntry.setIndexNames(
    (0, "NNCGNI0006-MIB", "nncExtEnvFanIndex"),
)
if mibBuilder.loadTexts:
    nncExtEnvFanTableEntry.setStatus("current")


class _NncExtEnvFanIndex_Type(Integer32):
    """Custom type nncExtEnvFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NncExtEnvFanIndex_Type.__name__ = "Integer32"
_NncExtEnvFanIndex_Object = MibTableColumn
nncExtEnvFanIndex = _NncExtEnvFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 5, 1, 1),
    _NncExtEnvFanIndex_Type()
)
nncExtEnvFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvFanIndex.setStatus("current")
_NncExtEnvFanStatusByFanIndex_Type = FanStatusType
_NncExtEnvFanStatusByFanIndex_Object = MibTableColumn
nncExtEnvFanStatusByFanIndex = _NncExtEnvFanStatusByFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 5, 1, 2),
    _NncExtEnvFanStatusByFanIndex_Type()
)
nncExtEnvFanStatusByFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvFanStatusByFanIndex.setStatus("current")
_NncExtEnvPwrSupplyTable_Object = MibTable
nncExtEnvPwrSupplyTable = _NncExtEnvPwrSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 6)
)
if mibBuilder.loadTexts:
    nncExtEnvPwrSupplyTable.setStatus("current")
_NncExtEnvPwrSupplyTableEntry_Object = MibTableRow
nncExtEnvPwrSupplyTableEntry = _NncExtEnvPwrSupplyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 6, 1)
)
nncExtEnvPwrSupplyTableEntry.setIndexNames(
    (0, "NNCGNI0006-MIB", "nncExtEnvPwrSupplySlotIndex"),
)
if mibBuilder.loadTexts:
    nncExtEnvPwrSupplyTableEntry.setStatus("current")


class _NncExtEnvPwrSupplySlotIndex_Type(Integer32):
    """Custom type nncExtEnvPwrSupplySlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NncExtEnvPwrSupplySlotIndex_Type.__name__ = "Integer32"
_NncExtEnvPwrSupplySlotIndex_Object = MibTableColumn
nncExtEnvPwrSupplySlotIndex = _NncExtEnvPwrSupplySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 6, 1, 1),
    _NncExtEnvPwrSupplySlotIndex_Type()
)
nncExtEnvPwrSupplySlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvPwrSupplySlotIndex.setStatus("current")
_NncExtEnvPwrSupplyStatus_Type = PwrSupplyStatusType
_NncExtEnvPwrSupplyStatus_Object = MibTableColumn
nncExtEnvPwrSupplyStatus = _NncExtEnvPwrSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 6, 1, 2),
    _NncExtEnvPwrSupplyStatus_Type()
)
nncExtEnvPwrSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvPwrSupplyStatus.setStatus("current")
_NncExtRestarts_Type = Counter32
_NncExtRestarts_Object = MibScalar
nncExtRestarts = _NncExtRestarts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 1),
    _NncExtRestarts_Type()
)
nncExtRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestarts.setStatus("current")
_NncExtFaultInducedRestarts_Type = Counter32
_NncExtFaultInducedRestarts_Object = MibScalar
nncExtFaultInducedRestarts = _NncExtFaultInducedRestarts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 2),
    _NncExtFaultInducedRestarts_Type()
)
nncExtFaultInducedRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtFaultInducedRestarts.setStatus("current")
_NncExtLastFault_Type = RestartCause
_NncExtLastFault_Object = MibScalar
nncExtLastFault = _NncExtLastFault_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 3),
    _NncExtLastFault_Type()
)
nncExtLastFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtLastFault.setStatus("current")


class _NncExtFaultRepetitions_Type(Integer32):
    """Custom type nncExtFaultRepetitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NncExtFaultRepetitions_Type.__name__ = "Integer32"
_NncExtFaultRepetitions_Object = MibScalar
nncExtFaultRepetitions = _NncExtFaultRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 4),
    _NncExtFaultRepetitions_Type()
)
nncExtFaultRepetitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtFaultRepetitions.setStatus("current")
_NncExtRestartTracebackTable_Object = MibTable
nncExtRestartTracebackTable = _NncExtRestartTracebackTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 5)
)
if mibBuilder.loadTexts:
    nncExtRestartTracebackTable.setStatus("current")
_NncExtRestartTracebackEntry_Object = MibTableRow
nncExtRestartTracebackEntry = _NncExtRestartTracebackEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1)
)
nncExtRestartTracebackEntry.setIndexNames(
    (0, "NNCGNI0006-MIB", "nncExtRestartTracebackIndex"),
)
if mibBuilder.loadTexts:
    nncExtRestartTracebackEntry.setStatus("current")


class _NncExtRestartTracebackIndex_Type(Integer32):
    """Custom type nncExtRestartTracebackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NncExtRestartTracebackIndex_Type.__name__ = "Integer32"
_NncExtRestartTracebackIndex_Object = MibTableColumn
nncExtRestartTracebackIndex = _NncExtRestartTracebackIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1, 1),
    _NncExtRestartTracebackIndex_Type()
)
nncExtRestartTracebackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestartTracebackIndex.setStatus("current")


class _NncExtRestartTracebackPCValue_Type(Integer32):
    """Custom type nncExtRestartTracebackPCValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtRestartTracebackPCValue_Type.__name__ = "Integer32"
_NncExtRestartTracebackPCValue_Object = MibTableColumn
nncExtRestartTracebackPCValue = _NncExtRestartTracebackPCValue_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1, 2),
    _NncExtRestartTracebackPCValue_Type()
)
nncExtRestartTracebackPCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestartTracebackPCValue.setStatus("current")
_NncExtRestartRegisterTable_Object = MibTable
nncExtRestartRegisterTable = _NncExtRestartRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 6)
)
if mibBuilder.loadTexts:
    nncExtRestartRegisterTable.setStatus("current")
_NncExtRestartRegisterEntry_Object = MibTableRow
nncExtRestartRegisterEntry = _NncExtRestartRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1)
)
nncExtRestartRegisterEntry.setIndexNames(
    (0, "NNCGNI0006-MIB", "nncExtRestartRegisterIndex"),
)
if mibBuilder.loadTexts:
    nncExtRestartRegisterEntry.setStatus("current")


class _NncExtRestartRegisterIndex_Type(Integer32):
    """Custom type nncExtRestartRegisterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NncExtRestartRegisterIndex_Type.__name__ = "Integer32"
_NncExtRestartRegisterIndex_Object = MibTableColumn
nncExtRestartRegisterIndex = _NncExtRestartRegisterIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1, 1),
    _NncExtRestartRegisterIndex_Type()
)
nncExtRestartRegisterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestartRegisterIndex.setStatus("current")


class _NncExtRestartRegisterValue_Type(Integer32):
    """Custom type nncExtRestartRegisterValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtRestartRegisterValue_Type.__name__ = "Integer32"
_NncExtRestartRegisterValue_Object = MibTableColumn
nncExtRestartRegisterValue = _NncExtRestartRegisterValue_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1, 2),
    _NncExtRestartRegisterValue_Type()
)
nncExtRestartRegisterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestartRegisterValue.setStatus("current")


class _NncExtRestartForceToBoot_Type(Integer32):
    """Custom type nncExtRestartForceToBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36000),
    )


_NncExtRestartForceToBoot_Type.__name__ = "Integer32"
_NncExtRestartForceToBoot_Object = MibScalar
nncExtRestartForceToBoot = _NncExtRestartForceToBoot_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 7),
    _NncExtRestartForceToBoot_Type()
)
nncExtRestartForceToBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtRestartForceToBoot.setStatus("current")
if mibBuilder.loadTexts:
    nncExtRestartForceToBoot.setUnits("seconds")
_NncExtRestartCause_Type = RestartCause
_NncExtRestartCause_Object = MibScalar
nncExtRestartCause = _NncExtRestartCause_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 8),
    _NncExtRestartCause_Type()
)
nncExtRestartCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestartCause.setStatus("current")


class _NncExtRestartSystem_Type(Integer32):
    """Custom type nncExtRestartSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36000),
    )


_NncExtRestartSystem_Type.__name__ = "Integer32"
_NncExtRestartSystem_Object = MibScalar
nncExtRestartSystem = _NncExtRestartSystem_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 9),
    _NncExtRestartSystem_Type()
)
nncExtRestartSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtRestartSystem.setStatus("current")
if mibBuilder.loadTexts:
    nncExtRestartSystem.setUnits("Seconds")
_NncExtCodeSpaceCurrentlyActive_Type = CodeSpaceIndex
_NncExtCodeSpaceCurrentlyActive_Object = MibScalar
nncExtCodeSpaceCurrentlyActive = _NncExtCodeSpaceCurrentlyActive_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 1),
    _NncExtCodeSpaceCurrentlyActive_Type()
)
nncExtCodeSpaceCurrentlyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceCurrentlyActive.setStatus("current")
_NncExtCodeSpaceNextActive_Type = CodeSpaceIndex
_NncExtCodeSpaceNextActive_Object = MibScalar
nncExtCodeSpaceNextActive = _NncExtCodeSpaceNextActive_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 2),
    _NncExtCodeSpaceNextActive_Type()
)
nncExtCodeSpaceNextActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtCodeSpaceNextActive.setStatus("current")
_NncExtCodeSpaceNumber_Type = CodeSpaceIndex
_NncExtCodeSpaceNumber_Object = MibScalar
nncExtCodeSpaceNumber = _NncExtCodeSpaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 3),
    _NncExtCodeSpaceNumber_Type()
)
nncExtCodeSpaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceNumber.setStatus("current")
_NncExtCodeSpaceTable_Object = MibTable
nncExtCodeSpaceTable = _NncExtCodeSpaceTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4)
)
if mibBuilder.loadTexts:
    nncExtCodeSpaceTable.setStatus("current")
_NncExtCodeSpaceEntry_Object = MibTableRow
nncExtCodeSpaceEntry = _NncExtCodeSpaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1)
)
nncExtCodeSpaceEntry.setIndexNames(
    (0, "NNCGNI0006-MIB", "nncExtCodeSpaceIndex"),
)
if mibBuilder.loadTexts:
    nncExtCodeSpaceEntry.setStatus("current")
_NncExtCodeSpaceIndex_Type = CodeSpaceIndex
_NncExtCodeSpaceIndex_Object = MibTableColumn
nncExtCodeSpaceIndex = _NncExtCodeSpaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 1),
    _NncExtCodeSpaceIndex_Type()
)
nncExtCodeSpaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceIndex.setStatus("current")


class _NncExtCodeSpaceSize_Type(Integer32):
    """Custom type nncExtCodeSpaceSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtCodeSpaceSize_Type.__name__ = "Integer32"
_NncExtCodeSpaceSize_Object = MibTableColumn
nncExtCodeSpaceSize = _NncExtCodeSpaceSize_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 2),
    _NncExtCodeSpaceSize_Type()
)
nncExtCodeSpaceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceSize.setStatus("current")
if mibBuilder.loadTexts:
    nncExtCodeSpaceSize.setUnits("bytes")


class _NncExtCodeSpaceStatus_Type(Integer32):
    """Custom type nncExtCodeSpaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NncExtCodeSpaceStatus_Type.__name__ = "Integer32"
_NncExtCodeSpaceStatus_Object = MibTableColumn
nncExtCodeSpaceStatus = _NncExtCodeSpaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 3),
    _NncExtCodeSpaceStatus_Type()
)
nncExtCodeSpaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceStatus.setStatus("current")
_NncExtCodeSpaceGeneric_Type = CurrentGenericType
_NncExtCodeSpaceGeneric_Object = MibTableColumn
nncExtCodeSpaceGeneric = _NncExtCodeSpaceGeneric_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 4),
    _NncExtCodeSpaceGeneric_Type()
)
nncExtCodeSpaceGeneric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceGeneric.setStatus("current")


class _NncExtCodeSpaceDownloadDate_Type(DisplayString):
    """Custom type nncExtCodeSpaceDownloadDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_NncExtCodeSpaceDownloadDate_Type.__name__ = "DisplayString"
_NncExtCodeSpaceDownloadDate_Object = MibTableColumn
nncExtCodeSpaceDownloadDate = _NncExtCodeSpaceDownloadDate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 5),
    _NncExtCodeSpaceDownloadDate_Type()
)
nncExtCodeSpaceDownloadDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceDownloadDate.setStatus("current")


class _NncExtCodeSpaceDownloadTime_Type(DisplayString):
    """Custom type nncExtCodeSpaceDownloadTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_NncExtCodeSpaceDownloadTime_Type.__name__ = "DisplayString"
_NncExtCodeSpaceDownloadTime_Object = MibTableColumn
nncExtCodeSpaceDownloadTime = _NncExtCodeSpaceDownloadTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 6),
    _NncExtCodeSpaceDownloadTime_Type()
)
nncExtCodeSpaceDownloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceDownloadTime.setStatus("current")
_NncExtCodeSpaceDownloadServer_Type = DisplayString
_NncExtCodeSpaceDownloadServer_Object = MibTableColumn
nncExtCodeSpaceDownloadServer = _NncExtCodeSpaceDownloadServer_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 7),
    _NncExtCodeSpaceDownloadServer_Type()
)
nncExtCodeSpaceDownloadServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceDownloadServer.setStatus("current")
_NncExtCodeSpaceDownloadRequestor_Type = DisplayString
_NncExtCodeSpaceDownloadRequestor_Object = MibTableColumn
nncExtCodeSpaceDownloadRequestor = _NncExtCodeSpaceDownloadRequestor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 8),
    _NncExtCodeSpaceDownloadRequestor_Type()
)
nncExtCodeSpaceDownloadRequestor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceDownloadRequestor.setStatus("current")


class _NncExtCodeSpaceCompressionType_Type(Integer32):
    """Custom type nncExtCodeSpaceCompressionType based on Integer32"""
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
        *(("c1", 2),
          ("c2", 3),
          ("c3", 4),
          ("none", 1))
    )


_NncExtCodeSpaceCompressionType_Type.__name__ = "Integer32"
_NncExtCodeSpaceCompressionType_Object = MibTableColumn
nncExtCodeSpaceCompressionType = _NncExtCodeSpaceCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 9),
    _NncExtCodeSpaceCompressionType_Type()
)
nncExtCodeSpaceCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceCompressionType.setStatus("current")


class _NncExtCodeSpaceLoadSize_Type(Integer32):
    """Custom type nncExtCodeSpaceLoadSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtCodeSpaceLoadSize_Type.__name__ = "Integer32"
_NncExtCodeSpaceLoadSize_Object = MibTableColumn
nncExtCodeSpaceLoadSize = _NncExtCodeSpaceLoadSize_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 10),
    _NncExtCodeSpaceLoadSize_Type()
)
nncExtCodeSpaceLoadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceLoadSize.setStatus("current")
if mibBuilder.loadTexts:
    nncExtCodeSpaceLoadSize.setUnits("bytes")


class _NncExtCodeSpaceCompressLoadSize_Type(Integer32):
    """Custom type nncExtCodeSpaceCompressLoadSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtCodeSpaceCompressLoadSize_Type.__name__ = "Integer32"
_NncExtCodeSpaceCompressLoadSize_Object = MibTableColumn
nncExtCodeSpaceCompressLoadSize = _NncExtCodeSpaceCompressLoadSize_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 11),
    _NncExtCodeSpaceCompressLoadSize_Type()
)
nncExtCodeSpaceCompressLoadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceCompressLoadSize.setStatus("current")
if mibBuilder.loadTexts:
    nncExtCodeSpaceCompressLoadSize.setUnits("bytes")
_NncExtNVMUsageTable_Object = MibTable
nncExtNVMUsageTable = _NncExtNVMUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 1)
)
if mibBuilder.loadTexts:
    nncExtNVMUsageTable.setStatus("current")
_NncExtNVMUsageEntry_Object = MibTableRow
nncExtNVMUsageEntry = _NncExtNVMUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1)
)
nncExtNVMUsageEntry.setIndexNames(
    (0, "NNCGNI0006-MIB", "nncExtNVMPoolIndex"),
)
if mibBuilder.loadTexts:
    nncExtNVMUsageEntry.setStatus("current")
_NncExtNVMPoolIndex_Type = NVMPoolIndex
_NncExtNVMPoolIndex_Object = MibTableColumn
nncExtNVMPoolIndex = _NncExtNVMPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 1),
    _NncExtNVMPoolIndex_Type()
)
nncExtNVMPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNVMPoolIndex.setStatus("current")


class _NncExtNVMPoolSize_Type(Integer32):
    """Custom type nncExtNVMPoolSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtNVMPoolSize_Type.__name__ = "Integer32"
_NncExtNVMPoolSize_Object = MibTableColumn
nncExtNVMPoolSize = _NncExtNVMPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 2),
    _NncExtNVMPoolSize_Type()
)
nncExtNVMPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNVMPoolSize.setStatus("current")
if mibBuilder.loadTexts:
    nncExtNVMPoolSize.setUnits("bytes")


class _NncExtNVMPoolBytesUsed_Type(Integer32):
    """Custom type nncExtNVMPoolBytesUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtNVMPoolBytesUsed_Type.__name__ = "Integer32"
_NncExtNVMPoolBytesUsed_Object = MibTableColumn
nncExtNVMPoolBytesUsed = _NncExtNVMPoolBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 3),
    _NncExtNVMPoolBytesUsed_Type()
)
nncExtNVMPoolBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNVMPoolBytesUsed.setStatus("current")
if mibBuilder.loadTexts:
    nncExtNVMPoolBytesUsed.setUnits("bytes")


class _NncExtNVMLastRepair_Type(OctetString):
    """Custom type nncExtNVMLastRepair based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 31),
    )


_NncExtNVMLastRepair_Type.__name__ = "OctetString"
_NncExtNVMLastRepair_Object = MibScalar
nncExtNVMLastRepair = _NncExtNVMLastRepair_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 2),
    _NncExtNVMLastRepair_Type()
)
nncExtNVMLastRepair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNVMLastRepair.setStatus("current")
_NncExtProbeMPLTable_Object = MibTable
nncExtProbeMPLTable = _NncExtProbeMPLTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 12, 1)
)
if mibBuilder.loadTexts:
    nncExtProbeMPLTable.setStatus("current")
_NncExtProbeMPLEntry_Object = MibTableRow
nncExtProbeMPLEntry = _NncExtProbeMPLEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 12, 1, 1)
)
nncExtProbeMPLEntry.setIndexNames(
    (0, "NNCGNI0006-MIB", "nncExtProbeMPL"),
)
if mibBuilder.loadTexts:
    nncExtProbeMPLEntry.setStatus("current")


class _NncExtProbeMPL_Type(OctetString):
    """Custom type nncExtProbeMPL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NncExtProbeMPL_Type.__name__ = "OctetString"
_NncExtProbeMPL_Object = MibTableColumn
nncExtProbeMPL = _NncExtProbeMPL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 12, 1, 1, 1),
    _NncExtProbeMPL_Type()
)
nncExtProbeMPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtProbeMPL.setStatus("current")


class _NncDiagUndoAll_Type(Integer32):
    """Custom type nncDiagUndoAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("undo", 1)
    )


_NncDiagUndoAll_Type.__name__ = "Integer32"
_NncDiagUndoAll_Object = MibScalar
nncDiagUndoAll = _NncDiagUndoAll_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 13, 1),
    _NncDiagUndoAll_Type()
)
nncDiagUndoAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncDiagUndoAll.setStatus("current")


class _NncExtStartupDiagnosticResults_Type(Integer32):
    """Custom type nncExtStartupDiagnosticResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passed", 1),
          ("unspecifiedFailure", 2))
    )


_NncExtStartupDiagnosticResults_Type.__name__ = "Integer32"
_NncExtStartupDiagnosticResults_Object = MibScalar
nncExtStartupDiagnosticResults = _NncExtStartupDiagnosticResults_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 13, 2),
    _NncExtStartupDiagnosticResults_Type()
)
nncExtStartupDiagnosticResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtStartupDiagnosticResults.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCGNI0006-MIB",
    **{"RestartCause": RestartCause,
       "Nci2DeviceIDType": Nci2DeviceIDType,
       "CurrentGenericType": CurrentGenericType,
       "ProductPartNumberType": ProductPartNumberType,
       "CardIDType": CardIDType,
       "CardSerialNumberType": CardSerialNumberType,
       "NncSwStatus": NncSwStatus,
       "NncSwBank": NncSwBank,
       "FanStatusType": FanStatusType,
       "PwrSupplyStatusType": PwrSupplyStatusType,
       "CodeSpaceIndex": CodeSpaceIndex,
       "NVMPoolIndex": NVMPoolIndex,
       "SvcEpdOptionType": SvcEpdOptionType,
       "SvcPpdOptionType": SvcPpdOptionType,
       "nncExtSysProductName": nncExtSysProductName,
       "nncExtSysCurrentGeneric": nncExtSysCurrentGeneric,
       "nncExtSysProductPartNumber": nncExtSysProductPartNumber,
       "nncExtSysNci2DeviceID": nncExtSysNci2DeviceID,
       "nncExtSysCurrentDateAndTime": nncExtSysCurrentDateAndTime,
       "nncExtSysCardTable": nncExtSysCardTable,
       "nncExtSysCardEntry": nncExtSysCardEntry,
       "nncExtSysCardIndex": nncExtSysCardIndex,
       "nncExtSysCardIDType": nncExtSysCardIDType,
       "nncExtSysCardName": nncExtSysCardName,
       "nncExtSysCardSerialNumber": nncExtSysCardSerialNumber,
       "nncExtEnvFanStatus": nncExtEnvFanStatus,
       "nncExtEnvTemperatureSensor": nncExtEnvTemperatureSensor,
       "nncExtEnvPlus12Status": nncExtEnvPlus12Status,
       "nncExtEnvMinus12Status": nncExtEnvMinus12Status,
       "nncExtEnvFanTable": nncExtEnvFanTable,
       "nncExtEnvFanTableEntry": nncExtEnvFanTableEntry,
       "nncExtEnvFanIndex": nncExtEnvFanIndex,
       "nncExtEnvFanStatusByFanIndex": nncExtEnvFanStatusByFanIndex,
       "nncExtEnvPwrSupplyTable": nncExtEnvPwrSupplyTable,
       "nncExtEnvPwrSupplyTableEntry": nncExtEnvPwrSupplyTableEntry,
       "nncExtEnvPwrSupplySlotIndex": nncExtEnvPwrSupplySlotIndex,
       "nncExtEnvPwrSupplyStatus": nncExtEnvPwrSupplyStatus,
       "nncExtRestarts": nncExtRestarts,
       "nncExtFaultInducedRestarts": nncExtFaultInducedRestarts,
       "nncExtLastFault": nncExtLastFault,
       "nncExtFaultRepetitions": nncExtFaultRepetitions,
       "nncExtRestartTracebackTable": nncExtRestartTracebackTable,
       "nncExtRestartTracebackEntry": nncExtRestartTracebackEntry,
       "nncExtRestartTracebackIndex": nncExtRestartTracebackIndex,
       "nncExtRestartTracebackPCValue": nncExtRestartTracebackPCValue,
       "nncExtRestartRegisterTable": nncExtRestartRegisterTable,
       "nncExtRestartRegisterEntry": nncExtRestartRegisterEntry,
       "nncExtRestartRegisterIndex": nncExtRestartRegisterIndex,
       "nncExtRestartRegisterValue": nncExtRestartRegisterValue,
       "nncExtRestartForceToBoot": nncExtRestartForceToBoot,
       "nncExtRestartCause": nncExtRestartCause,
       "nncExtRestartSystem": nncExtRestartSystem,
       "nncExtCodeSpaceCurrentlyActive": nncExtCodeSpaceCurrentlyActive,
       "nncExtCodeSpaceNextActive": nncExtCodeSpaceNextActive,
       "nncExtCodeSpaceNumber": nncExtCodeSpaceNumber,
       "nncExtCodeSpaceTable": nncExtCodeSpaceTable,
       "nncExtCodeSpaceEntry": nncExtCodeSpaceEntry,
       "nncExtCodeSpaceIndex": nncExtCodeSpaceIndex,
       "nncExtCodeSpaceSize": nncExtCodeSpaceSize,
       "nncExtCodeSpaceStatus": nncExtCodeSpaceStatus,
       "nncExtCodeSpaceGeneric": nncExtCodeSpaceGeneric,
       "nncExtCodeSpaceDownloadDate": nncExtCodeSpaceDownloadDate,
       "nncExtCodeSpaceDownloadTime": nncExtCodeSpaceDownloadTime,
       "nncExtCodeSpaceDownloadServer": nncExtCodeSpaceDownloadServer,
       "nncExtCodeSpaceDownloadRequestor": nncExtCodeSpaceDownloadRequestor,
       "nncExtCodeSpaceCompressionType": nncExtCodeSpaceCompressionType,
       "nncExtCodeSpaceLoadSize": nncExtCodeSpaceLoadSize,
       "nncExtCodeSpaceCompressLoadSize": nncExtCodeSpaceCompressLoadSize,
       "nncExtNVMUsageTable": nncExtNVMUsageTable,
       "nncExtNVMUsageEntry": nncExtNVMUsageEntry,
       "nncExtNVMPoolIndex": nncExtNVMPoolIndex,
       "nncExtNVMPoolSize": nncExtNVMPoolSize,
       "nncExtNVMPoolBytesUsed": nncExtNVMPoolBytesUsed,
       "nncExtNVMLastRepair": nncExtNVMLastRepair,
       "nncExtProbeMPLTable": nncExtProbeMPLTable,
       "nncExtProbeMPLEntry": nncExtProbeMPLEntry,
       "nncExtProbeMPL": nncExtProbeMPL,
       "nncDiagUndoAll": nncDiagUndoAll,
       "nncExtStartupDiagnosticResults": nncExtStartupDiagnosticResults,
       "nncExtBasics": nncExtBasics}
)
