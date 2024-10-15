# SNMP MIB module (FOUNDRY-SN-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:20 2024
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

(snAgentSys,
 snChassis,
 snStack) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "snAgentSys",
    "snChassis",
    "snStack")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

snAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 4)
)
snAgent.setRevisions(
        ("2014-03-10 00:00",
         "2013-02-28 00:00",
         "2012-09-21 00:00",
         "2012-04-18 00:00",
         "2012-01-24 00:00",
         "2011-12-22 00:00",
         "2010-06-02 00:00",
         "2009-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MacAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class DisplayString(OctetString, TextualConvention):
    status = "current"


class BrcdImageType(Integer32, TextualConvention):
    status = "current"
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("fpgaBundled", 13),
          ("fpgaHBridge", 12),
          ("fpgaMBridge", 9),
          ("fpgaMBridge32", 10),
          ("fpgaPbif4x40", 28),
          ("fpgaPbif8x10", 23),
          ("fpgaPbifMetro", 26),
          ("fpgaPbifMrj", 17),
          ("fpgaPbifOc", 14),
          ("fpgaPbifSp2", 20),
          ("fpgaSBridge", 11),
          ("fpgaStatsMrj", 18),
          ("fpgaStatsOc", 15),
          ("fpgaXgmacSp2", 21),
          ("fpgaXpp2x100", 25),
          ("fpgaXpp4x40", 27),
          ("fpgaXpp8x10", 24),
          ("fpgaXppMrj", 19),
          ("fpgaXppOc", 16),
          ("fpgaXppSp2", 22),
          ("interfaceModuleApplication", 7),
          ("interfaceModuleBoot", 5),
          ("interfaceModuleMonitor", 6),
          ("managementModuleApplication", 4),
          ("managementModuleBoot", 2),
          ("managementModuleMonitor", 3),
          ("mgmtAndIntfModuleCombinedApp", 8),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_SnChasGen_ObjectIdentity = ObjectIdentity
snChasGen = _SnChasGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1)
)


class _SnChasType_Type(DisplayString):
    """Custom type snChasType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasType_Type.__name__ = "DisplayString"
_SnChasType_Object = MibScalar
snChasType = _SnChasType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 1),
    _SnChasType_Type()
)
snChasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasType.setStatus("current")


class _SnChasSerNum_Type(DisplayString):
    """Custom type snChasSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasSerNum_Type.__name__ = "DisplayString"
_SnChasSerNum_Object = MibScalar
snChasSerNum = _SnChasSerNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 2),
    _SnChasSerNum_Type()
)
snChasSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasSerNum.setStatus("current")
_SnChasPwrSupplyStatus_Type = Integer32
_SnChasPwrSupplyStatus_Object = MibScalar
snChasPwrSupplyStatus = _SnChasPwrSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 3),
    _SnChasPwrSupplyStatus_Type()
)
snChasPwrSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupplyStatus.setStatus("deprecated")
_SnChasFanStatus_Type = Integer32
_SnChasFanStatus_Object = MibScalar
snChasFanStatus = _SnChasFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 4),
    _SnChasFanStatus_Type()
)
snChasFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFanStatus.setStatus("deprecated")


class _SnChasMainBrdDescription_Type(DisplayString):
    """Custom type snChasMainBrdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasMainBrdDescription_Type.__name__ = "DisplayString"
_SnChasMainBrdDescription_Object = MibScalar
snChasMainBrdDescription = _SnChasMainBrdDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 5),
    _SnChasMainBrdDescription_Type()
)
snChasMainBrdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasMainBrdDescription.setStatus("current")


class _SnChasMainPortTotal_Type(Integer32):
    """Custom type snChasMainPortTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SnChasMainPortTotal_Type.__name__ = "Integer32"
_SnChasMainPortTotal_Object = MibScalar
snChasMainPortTotal = _SnChasMainPortTotal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 6),
    _SnChasMainPortTotal_Type()
)
snChasMainPortTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasMainPortTotal.setStatus("current")


class _SnChasExpBrdDescription_Type(DisplayString):
    """Custom type snChasExpBrdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasExpBrdDescription_Type.__name__ = "DisplayString"
_SnChasExpBrdDescription_Object = MibScalar
snChasExpBrdDescription = _SnChasExpBrdDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 7),
    _SnChasExpBrdDescription_Type()
)
snChasExpBrdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasExpBrdDescription.setStatus("current")


class _SnChasExpPortTotal_Type(Integer32):
    """Custom type snChasExpPortTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SnChasExpPortTotal_Type.__name__ = "Integer32"
_SnChasExpPortTotal_Object = MibScalar
snChasExpPortTotal = _SnChasExpPortTotal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 8),
    _SnChasExpPortTotal_Type()
)
snChasExpPortTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasExpPortTotal.setStatus("current")
_SnChasStatusLeds_Type = Integer32
_SnChasStatusLeds_Object = MibScalar
snChasStatusLeds = _SnChasStatusLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 9),
    _SnChasStatusLeds_Type()
)
snChasStatusLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasStatusLeds.setStatus("current")
_SnChasTrafficLeds_Type = Integer32
_SnChasTrafficLeds_Object = MibScalar
snChasTrafficLeds = _SnChasTrafficLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 10),
    _SnChasTrafficLeds_Type()
)
snChasTrafficLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasTrafficLeds.setStatus("current")
_SnChasMediaLeds_Type = Integer32
_SnChasMediaLeds_Object = MibScalar
snChasMediaLeds = _SnChasMediaLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 11),
    _SnChasMediaLeds_Type()
)
snChasMediaLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasMediaLeds.setStatus("current")


class _SnChasEnablePwrSupplyTrap_Type(Integer32):
    """Custom type snChasEnablePwrSupplyTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnChasEnablePwrSupplyTrap_Type.__name__ = "Integer32"
_SnChasEnablePwrSupplyTrap_Object = MibScalar
snChasEnablePwrSupplyTrap = _SnChasEnablePwrSupplyTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 12),
    _SnChasEnablePwrSupplyTrap_Type()
)
snChasEnablePwrSupplyTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasEnablePwrSupplyTrap.setStatus("current")
_SnChasMainBrdId_Type = OctetString
_SnChasMainBrdId_Object = MibScalar
snChasMainBrdId = _SnChasMainBrdId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 13),
    _SnChasMainBrdId_Type()
)
snChasMainBrdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasMainBrdId.setStatus("current")
_SnChasExpBrdId_Type = OctetString
_SnChasExpBrdId_Object = MibScalar
snChasExpBrdId = _SnChasExpBrdId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 14),
    _SnChasExpBrdId_Type()
)
snChasExpBrdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasExpBrdId.setStatus("current")
_SnChasSpeedLeds_Type = Integer32
_SnChasSpeedLeds_Object = MibScalar
snChasSpeedLeds = _SnChasSpeedLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 15),
    _SnChasSpeedLeds_Type()
)
snChasSpeedLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasSpeedLeds.setStatus("current")


class _SnChasEnableFanTrap_Type(Integer32):
    """Custom type snChasEnableFanTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnChasEnableFanTrap_Type.__name__ = "Integer32"
_SnChasEnableFanTrap_Object = MibScalar
snChasEnableFanTrap = _SnChasEnableFanTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 16),
    _SnChasEnableFanTrap_Type()
)
snChasEnableFanTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasEnableFanTrap.setStatus("current")


class _SnChasIdNumber_Type(DisplayString):
    """Custom type snChasIdNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnChasIdNumber_Type.__name__ = "DisplayString"
_SnChasIdNumber_Object = MibScalar
snChasIdNumber = _SnChasIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 17),
    _SnChasIdNumber_Type()
)
snChasIdNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasIdNumber.setStatus("current")


class _SnChasActualTemperature_Type(Integer32):
    """Custom type snChasActualTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 250),
    )


_SnChasActualTemperature_Type.__name__ = "Integer32"
_SnChasActualTemperature_Object = MibScalar
snChasActualTemperature = _SnChasActualTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 18),
    _SnChasActualTemperature_Type()
)
snChasActualTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasActualTemperature.setStatus("current")


class _SnChasWarningTemperature_Type(Integer32):
    """Custom type snChasWarningTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SnChasWarningTemperature_Type.__name__ = "Integer32"
_SnChasWarningTemperature_Object = MibScalar
snChasWarningTemperature = _SnChasWarningTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 19),
    _SnChasWarningTemperature_Type()
)
snChasWarningTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasWarningTemperature.setStatus("current")


class _SnChasShutdownTemperature_Type(Integer32):
    """Custom type snChasShutdownTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SnChasShutdownTemperature_Type.__name__ = "Integer32"
_SnChasShutdownTemperature_Object = MibScalar
snChasShutdownTemperature = _SnChasShutdownTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 20),
    _SnChasShutdownTemperature_Type()
)
snChasShutdownTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasShutdownTemperature.setStatus("current")


class _SnChasEnableTempWarnTrap_Type(Integer32):
    """Custom type snChasEnableTempWarnTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnChasEnableTempWarnTrap_Type.__name__ = "Integer32"
_SnChasEnableTempWarnTrap_Object = MibScalar
snChasEnableTempWarnTrap = _SnChasEnableTempWarnTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 21),
    _SnChasEnableTempWarnTrap_Type()
)
snChasEnableTempWarnTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasEnableTempWarnTrap.setStatus("current")
_SnChasFlashCard_Type = Integer32
_SnChasFlashCard_Object = MibScalar
snChasFlashCard = _SnChasFlashCard_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 22),
    _SnChasFlashCard_Type()
)
snChasFlashCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFlashCard.setStatus("current")
_SnChasFlashCardLeds_Type = Integer32
_SnChasFlashCardLeds_Object = MibScalar
snChasFlashCardLeds = _SnChasFlashCardLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 23),
    _SnChasFlashCardLeds_Type()
)
snChasFlashCardLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFlashCardLeds.setStatus("current")
_SnChasNumSlots_Type = Integer32
_SnChasNumSlots_Object = MibScalar
snChasNumSlots = _SnChasNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 24),
    _SnChasNumSlots_Type()
)
snChasNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasNumSlots.setStatus("current")


class _SnChasArchitectureType_Type(Integer32):
    """Custom type snChasArchitectureType based on Integer32"""
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
        *(("bigIron", 2),
          ("fifthGen", 4),
          ("stackable", 1),
          ("terathon", 3))
    )


_SnChasArchitectureType_Type.__name__ = "Integer32"
_SnChasArchitectureType_Object = MibScalar
snChasArchitectureType = _SnChasArchitectureType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 25),
    _SnChasArchitectureType_Type()
)
snChasArchitectureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasArchitectureType.setStatus("current")


class _SnChasProductType_Type(Integer32):
    """Custom type snChasProductType based on Integer32"""
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
              50,
              66,
              77,
              78,
              83,
              87)
        )
    )
    namedValues = NamedValues(
        *(("biBB", 66),
          ("biM4", 77),
          ("biNI", 78),
          ("biNI2", 50),
          ("biRx200", 8),
          ("biRx32", 15),
          ("biRx400", 6),
          ("biRx800", 4),
          ("biSLB", 83),
          ("biWG", 87),
          ("brMlxE16", 20),
          ("brMlxE32", 21),
          ("brMlxE4", 18),
          ("brMlxE8", 19),
          ("imr", 3),
          ("invalid", 0),
          ("mg8", 1),
          ("ni40G", 2),
          ("niCER2000Series", 17),
          ("niCES2000Series", 16),
          ("niMlx16", 10),
          ("niMlx32", 13),
          ("niMlx4", 12),
          ("niMlx8", 11),
          ("niXmr16000", 5),
          ("niXmr32000", 14),
          ("niXmr4000", 9),
          ("niXmr8000", 7))
    )


_SnChasProductType_Type.__name__ = "Integer32"
_SnChasProductType_Object = MibScalar
snChasProductType = _SnChasProductType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 26),
    _SnChasProductType_Type()
)
snChasProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasProductType.setStatus("current")


class _SnChasSystemMode_Type(Integer32):
    """Custom type snChasSystemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mlx", 2),
          ("xmr", 1))
    )


_SnChasSystemMode_Type.__name__ = "Integer32"
_SnChasSystemMode_Object = MibScalar
snChasSystemMode = _SnChasSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 27),
    _SnChasSystemMode_Type()
)
snChasSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasSystemMode.setStatus("current")


class _SnChasFactoryPartNumber_Type(DisplayString):
    """Custom type snChasFactoryPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnChasFactoryPartNumber_Type.__name__ = "DisplayString"
_SnChasFactoryPartNumber_Object = MibScalar
snChasFactoryPartNumber = _SnChasFactoryPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 28),
    _SnChasFactoryPartNumber_Type()
)
snChasFactoryPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFactoryPartNumber.setStatus("current")


class _SnChasFactorySerialNumber_Type(DisplayString):
    """Custom type snChasFactorySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasFactorySerialNumber_Type.__name__ = "DisplayString"
_SnChasFactorySerialNumber_Object = MibScalar
snChasFactorySerialNumber = _SnChasFactorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 1, 29),
    _SnChasFactorySerialNumber_Type()
)
snChasFactorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFactorySerialNumber.setStatus("current")
_SnChasPwr_ObjectIdentity = ObjectIdentity
snChasPwr = _SnChasPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2)
)
_SnChasPwrSupplyTable_Object = MibTable
snChasPwrSupplyTable = _SnChasPwrSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    snChasPwrSupplyTable.setStatus("current")
_SnChasPwrSupplyEntry_Object = MibTableRow
snChasPwrSupplyEntry = _SnChasPwrSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2, 1, 1)
)
snChasPwrSupplyEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
)
if mibBuilder.loadTexts:
    snChasPwrSupplyEntry.setStatus("current")
_SnChasPwrSupplyIndex_Type = Integer32
_SnChasPwrSupplyIndex_Object = MibTableColumn
snChasPwrSupplyIndex = _SnChasPwrSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2, 1, 1, 1),
    _SnChasPwrSupplyIndex_Type()
)
snChasPwrSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupplyIndex.setStatus("current")


class _SnChasPwrSupplyDescription_Type(DisplayString):
    """Custom type snChasPwrSupplyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasPwrSupplyDescription_Type.__name__ = "DisplayString"
_SnChasPwrSupplyDescription_Object = MibTableColumn
snChasPwrSupplyDescription = _SnChasPwrSupplyDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2, 1, 1, 2),
    _SnChasPwrSupplyDescription_Type()
)
snChasPwrSupplyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupplyDescription.setStatus("current")


class _SnChasPwrSupplyOperStatus_Type(Integer32):
    """Custom type snChasPwrSupplyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("normal", 2),
          ("other", 1))
    )


_SnChasPwrSupplyOperStatus_Type.__name__ = "Integer32"
_SnChasPwrSupplyOperStatus_Object = MibTableColumn
snChasPwrSupplyOperStatus = _SnChasPwrSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2, 1, 1, 3),
    _SnChasPwrSupplyOperStatus_Type()
)
snChasPwrSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupplyOperStatus.setStatus("current")
_SnChasPwrSupply2Table_Object = MibTable
snChasPwrSupply2Table = _SnChasPwrSupply2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    snChasPwrSupply2Table.setStatus("current")
_SnChasPwrSupply2Entry_Object = MibTableRow
snChasPwrSupply2Entry = _SnChasPwrSupply2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2, 2, 1)
)
snChasPwrSupply2Entry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snChasPwrSupply2Unit"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snChasPwrSupply2Index"),
)
if mibBuilder.loadTexts:
    snChasPwrSupply2Entry.setStatus("current")
_SnChasPwrSupply2Unit_Type = Integer32
_SnChasPwrSupply2Unit_Object = MibTableColumn
snChasPwrSupply2Unit = _SnChasPwrSupply2Unit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2, 2, 1, 1),
    _SnChasPwrSupply2Unit_Type()
)
snChasPwrSupply2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupply2Unit.setStatus("current")
_SnChasPwrSupply2Index_Type = Integer32
_SnChasPwrSupply2Index_Object = MibTableColumn
snChasPwrSupply2Index = _SnChasPwrSupply2Index_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2, 2, 1, 2),
    _SnChasPwrSupply2Index_Type()
)
snChasPwrSupply2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupply2Index.setStatus("current")


class _SnChasPwrSupply2Description_Type(DisplayString):
    """Custom type snChasPwrSupply2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasPwrSupply2Description_Type.__name__ = "DisplayString"
_SnChasPwrSupply2Description_Object = MibTableColumn
snChasPwrSupply2Description = _SnChasPwrSupply2Description_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2, 2, 1, 3),
    _SnChasPwrSupply2Description_Type()
)
snChasPwrSupply2Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupply2Description.setStatus("current")


class _SnChasPwrSupply2OperStatus_Type(Integer32):
    """Custom type snChasPwrSupply2OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("normal", 2),
          ("other", 1))
    )


_SnChasPwrSupply2OperStatus_Type.__name__ = "Integer32"
_SnChasPwrSupply2OperStatus_Object = MibTableColumn
snChasPwrSupply2OperStatus = _SnChasPwrSupply2OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 2, 2, 1, 4),
    _SnChasPwrSupply2OperStatus_Type()
)
snChasPwrSupply2OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupply2OperStatus.setStatus("current")
_SnChasFan_ObjectIdentity = ObjectIdentity
snChasFan = _SnChasFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3)
)
_SnChasFanTable_Object = MibTable
snChasFanTable = _SnChasFanTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    snChasFanTable.setStatus("current")
_SnChasFanEntry_Object = MibTableRow
snChasFanEntry = _SnChasFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3, 1, 1)
)
snChasFanEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snChasFanIndex"),
)
if mibBuilder.loadTexts:
    snChasFanEntry.setStatus("current")
_SnChasFanIndex_Type = Integer32
_SnChasFanIndex_Object = MibTableColumn
snChasFanIndex = _SnChasFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3, 1, 1, 1),
    _SnChasFanIndex_Type()
)
snChasFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFanIndex.setStatus("current")


class _SnChasFanDescription_Type(DisplayString):
    """Custom type snChasFanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasFanDescription_Type.__name__ = "DisplayString"
_SnChasFanDescription_Object = MibTableColumn
snChasFanDescription = _SnChasFanDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3, 1, 1, 2),
    _SnChasFanDescription_Type()
)
snChasFanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFanDescription.setStatus("current")


class _SnChasFanOperStatus_Type(Integer32):
    """Custom type snChasFanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("normal", 2),
          ("other", 1))
    )


_SnChasFanOperStatus_Type.__name__ = "Integer32"
_SnChasFanOperStatus_Object = MibTableColumn
snChasFanOperStatus = _SnChasFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3, 1, 1, 3),
    _SnChasFanOperStatus_Type()
)
snChasFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFanOperStatus.setStatus("current")
_SnChasFan2Table_Object = MibTable
snChasFan2Table = _SnChasFan2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    snChasFan2Table.setStatus("current")
_SnChasFan2Entry_Object = MibTableRow
snChasFan2Entry = _SnChasFan2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3, 2, 1)
)
snChasFan2Entry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snChasFan2Unit"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snChasFan2Index"),
)
if mibBuilder.loadTexts:
    snChasFan2Entry.setStatus("current")
_SnChasFan2Unit_Type = Integer32
_SnChasFan2Unit_Object = MibTableColumn
snChasFan2Unit = _SnChasFan2Unit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3, 2, 1, 1),
    _SnChasFan2Unit_Type()
)
snChasFan2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFan2Unit.setStatus("current")
_SnChasFan2Index_Type = Integer32
_SnChasFan2Index_Object = MibTableColumn
snChasFan2Index = _SnChasFan2Index_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3, 2, 1, 2),
    _SnChasFan2Index_Type()
)
snChasFan2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFan2Index.setStatus("current")


class _SnChasFan2Description_Type(DisplayString):
    """Custom type snChasFan2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasFan2Description_Type.__name__ = "DisplayString"
_SnChasFan2Description_Object = MibTableColumn
snChasFan2Description = _SnChasFan2Description_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3, 2, 1, 3),
    _SnChasFan2Description_Type()
)
snChasFan2Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFan2Description.setStatus("current")


class _SnChasFan2OperStatus_Type(Integer32):
    """Custom type snChasFan2OperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("normal", 2),
          ("other", 1))
    )


_SnChasFan2OperStatus_Type.__name__ = "Integer32"
_SnChasFan2OperStatus_Object = MibTableColumn
snChasFan2OperStatus = _SnChasFan2OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 3, 2, 1, 4),
    _SnChasFan2OperStatus_Type()
)
snChasFan2OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFan2OperStatus.setStatus("current")
_SnChasUnit_ObjectIdentity = ObjectIdentity
snChasUnit = _SnChasUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 4)
)
_SnChasUnitTable_Object = MibTable
snChasUnitTable = _SnChasUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    snChasUnitTable.setStatus("current")
_SnChasUnitEntry_Object = MibTableRow
snChasUnitEntry = _SnChasUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 4, 1, 1)
)
snChasUnitEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snChasUnitIndex"),
)
if mibBuilder.loadTexts:
    snChasUnitEntry.setStatus("current")
_SnChasUnitIndex_Type = Integer32
_SnChasUnitIndex_Object = MibTableColumn
snChasUnitIndex = _SnChasUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 4, 1, 1, 1),
    _SnChasUnitIndex_Type()
)
snChasUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasUnitIndex.setStatus("current")


class _SnChasUnitSerNum_Type(DisplayString):
    """Custom type snChasUnitSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasUnitSerNum_Type.__name__ = "DisplayString"
_SnChasUnitSerNum_Object = MibTableColumn
snChasUnitSerNum = _SnChasUnitSerNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 4, 1, 1, 2),
    _SnChasUnitSerNum_Type()
)
snChasUnitSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasUnitSerNum.setStatus("current")
_SnChasUnitNumSlots_Type = Integer32
_SnChasUnitNumSlots_Object = MibTableColumn
snChasUnitNumSlots = _SnChasUnitNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 4, 1, 1, 3),
    _SnChasUnitNumSlots_Type()
)
snChasUnitNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasUnitNumSlots.setStatus("current")


class _SnChasUnitActualTemperature_Type(Integer32):
    """Custom type snChasUnitActualTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 250),
    )


_SnChasUnitActualTemperature_Type.__name__ = "Integer32"
_SnChasUnitActualTemperature_Object = MibTableColumn
snChasUnitActualTemperature = _SnChasUnitActualTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 4, 1, 1, 4),
    _SnChasUnitActualTemperature_Type()
)
snChasUnitActualTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasUnitActualTemperature.setStatus("current")


class _SnChasUnitWarningTemperature_Type(Integer32):
    """Custom type snChasUnitWarningTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SnChasUnitWarningTemperature_Type.__name__ = "Integer32"
_SnChasUnitWarningTemperature_Object = MibTableColumn
snChasUnitWarningTemperature = _SnChasUnitWarningTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 4, 1, 1, 5),
    _SnChasUnitWarningTemperature_Type()
)
snChasUnitWarningTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasUnitWarningTemperature.setStatus("current")


class _SnChasUnitShutdownTemperature_Type(Integer32):
    """Custom type snChasUnitShutdownTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SnChasUnitShutdownTemperature_Type.__name__ = "Integer32"
_SnChasUnitShutdownTemperature_Object = MibTableColumn
snChasUnitShutdownTemperature = _SnChasUnitShutdownTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 4, 1, 1, 6),
    _SnChasUnitShutdownTemperature_Type()
)
snChasUnitShutdownTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasUnitShutdownTemperature.setStatus("current")
_SnChasUnitPartNum_Type = DisplayString
_SnChasUnitPartNum_Object = MibTableColumn
snChasUnitPartNum = _SnChasUnitPartNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 1, 4, 1, 1, 7),
    _SnChasUnitPartNum_Type()
)
snChasUnitPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasUnitPartNum.setStatus("current")
_SnAgentGbl_ObjectIdentity = ObjectIdentity
snAgentGbl = _SnAgentGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1)
)


class _SnAgReload_Type(Integer32):
    """Custom type snAgReload based on Integer32"""
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
        *(("busy", 4),
          ("other", 1),
          ("reset", 3),
          ("running", 2))
    )


_SnAgReload_Type.__name__ = "Integer32"
_SnAgReload_Object = MibScalar
snAgReload = _SnAgReload_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 1),
    _SnAgReload_Type()
)
snAgReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgReload.setStatus("current")


class _SnAgEraseNVRAM_Type(Integer32):
    """Custom type snAgEraseNVRAM based on Integer32"""
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
        *(("busy", 5),
          ("erase", 3),
          ("erasing", 4),
          ("error", 2),
          ("normal", 1))
    )


_SnAgEraseNVRAM_Type.__name__ = "Integer32"
_SnAgEraseNVRAM_Object = MibScalar
snAgEraseNVRAM = _SnAgEraseNVRAM_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 2),
    _SnAgEraseNVRAM_Type()
)
snAgEraseNVRAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgEraseNVRAM.setStatus("current")


class _SnAgWriteNVRAM_Type(Integer32):
    """Custom type snAgWriteNVRAM based on Integer32"""
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
        *(("busy", 5),
          ("error", 2),
          ("normal", 1),
          ("write", 3),
          ("writing", 4))
    )


_SnAgWriteNVRAM_Type.__name__ = "Integer32"
_SnAgWriteNVRAM_Object = MibScalar
snAgWriteNVRAM = _SnAgWriteNVRAM_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 3),
    _SnAgWriteNVRAM_Type()
)
snAgWriteNVRAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgWriteNVRAM.setStatus("current")


class _SnAgConfigFromNVRAM_Type(Integer32):
    """Custom type snAgConfigFromNVRAM based on Integer32"""
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
        *(("busy", 5),
          ("config", 3),
          ("configing", 4),
          ("error", 2),
          ("normal", 1))
    )


_SnAgConfigFromNVRAM_Type.__name__ = "Integer32"
_SnAgConfigFromNVRAM_Object = MibScalar
snAgConfigFromNVRAM = _SnAgConfigFromNVRAM_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 4),
    _SnAgConfigFromNVRAM_Type()
)
snAgConfigFromNVRAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgConfigFromNVRAM.setStatus("current")
_SnAgTftpServerIp_Type = IpAddress
_SnAgTftpServerIp_Object = MibScalar
snAgTftpServerIp = _SnAgTftpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 5),
    _SnAgTftpServerIp_Type()
)
snAgTftpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTftpServerIp.setStatus("deprecated")


class _SnAgImgFname_Type(DisplayString):
    """Custom type snAgImgFname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgImgFname_Type.__name__ = "DisplayString"
_SnAgImgFname_Object = MibScalar
snAgImgFname = _SnAgImgFname_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 6),
    _SnAgImgFname_Type()
)
snAgImgFname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgImgFname.setStatus("current")


class _SnAgImgLoad_Type(Integer32):
    """Custom type snAgImgLoad based on Integer32"""
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
              33)
        )
    )
    namedValues = NamedValues(
        *(("downloadMPBootROM", 27),
          ("downloadMPBootTFTP", 29),
          ("downloadMPMonitor", 31),
          ("downloadMPPrimary", 20),
          ("downloadMPSecondary", 22),
          ("downloadSPBootROM", 32),
          ("downloadSPMonitor", 33),
          ("downloadSPPrimary", 24),
          ("downloadSPSecondary", 25),
          ("flashPrepareReadFailure", 2),
          ("flashPrepareWriteFailure", 4),
          ("flashReadError", 3),
          ("flashWriteError", 5),
          ("loading", 18),
          ("normal", 1),
          ("operationError", 17),
          ("tftpBusy", 8),
          ("tftpOutOfBufferSpace", 7),
          ("tftpRemoteBadAccess", 11),
          ("tftpRemoteBadId", 14),
          ("tftpRemoteBadOperation", 13),
          ("tftpRemoteDiskFull", 12),
          ("tftpRemoteFileExists", 15),
          ("tftpRemoteNoFile", 10),
          ("tftpRemoteNoUser", 16),
          ("tftpRemoteOtherErrors", 9),
          ("tftpTimeoutError", 6),
          ("tftpWrongFileType", 23),
          ("uploadMPBootROM", 26),
          ("uploadMPBootTFTP", 28),
          ("uploadMPMonitor", 30),
          ("uploadMPPrimary", 19),
          ("uploadMPSecondary", 21))
    )


_SnAgImgLoad_Type.__name__ = "Integer32"
_SnAgImgLoad_Object = MibScalar
snAgImgLoad = _SnAgImgLoad_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 7),
    _SnAgImgLoad_Type()
)
snAgImgLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgImgLoad.setStatus("current")


class _SnAgCfgFname_Type(DisplayString):
    """Custom type snAgCfgFname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgCfgFname_Type.__name__ = "DisplayString"
_SnAgCfgFname_Object = MibScalar
snAgCfgFname = _SnAgCfgFname_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 8),
    _SnAgCfgFname_Type()
)
snAgCfgFname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgCfgFname.setStatus("current")


class _SnAgCfgLoad_Type(Integer32):
    """Custom type snAgCfgLoad based on Integer32"""
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("downloadToDramFromNMS", 27),
          ("downloadToDramFromServer", 23),
          ("downloadToDramFromServerOverwrite", 30),
          ("downloadToFlashFromNMS", 25),
          ("downloadToFlashFromServer", 21),
          ("flashPrepareReadFailure", 2),
          ("flashPrepareWriteFailure", 4),
          ("flashReadError", 3),
          ("flashWriteError", 5),
          ("loading", 18),
          ("normal", 1),
          ("operationDoneWithNMS", 28),
          ("operationError", 17),
          ("tftpBusy", 8),
          ("tftpOutOfBufferSpace", 7),
          ("tftpRemoteBadAccess", 11),
          ("tftpRemoteBadId", 14),
          ("tftpRemoteBadOperation", 13),
          ("tftpRemoteDiskFull", 12),
          ("tftpRemoteFileExists", 15),
          ("tftpRemoteNoFile", 10),
          ("tftpRemoteNoUser", 16),
          ("tftpRemoteOtherErrors", 9),
          ("tftpTimeoutError", 6),
          ("tftpWrongFileType", 29),
          ("uploadFromDramToNMS", 26),
          ("uploadFromDramToServer", 22),
          ("uploadFromFlashToNMS", 24),
          ("uploadFromFlashToServer", 20))
    )


_SnAgCfgLoad_Type.__name__ = "Integer32"
_SnAgCfgLoad_Object = MibScalar
snAgCfgLoad = _SnAgCfgLoad_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 9),
    _SnAgCfgLoad_Type()
)
snAgCfgLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgCfgLoad.setStatus("current")
_SnAgDefGwayIp_Type = IpAddress
_SnAgDefGwayIp_Object = MibScalar
snAgDefGwayIp = _SnAgDefGwayIp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 10),
    _SnAgDefGwayIp_Type()
)
snAgDefGwayIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgDefGwayIp.setStatus("current")


class _SnAgImgVer_Type(DisplayString):
    """Custom type snAgImgVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgImgVer_Type.__name__ = "DisplayString"
_SnAgImgVer_Object = MibScalar
snAgImgVer = _SnAgImgVer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 11),
    _SnAgImgVer_Type()
)
snAgImgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgImgVer.setStatus("current")


class _SnAgFlashImgVer_Type(DisplayString):
    """Custom type snAgFlashImgVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgFlashImgVer_Type.__name__ = "DisplayString"
_SnAgFlashImgVer_Object = MibScalar
snAgFlashImgVer = _SnAgFlashImgVer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 12),
    _SnAgFlashImgVer_Type()
)
snAgFlashImgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgFlashImgVer.setStatus("current")
_SnAgGblIfIpAddr_Type = IpAddress
_SnAgGblIfIpAddr_Object = MibScalar
snAgGblIfIpAddr = _SnAgGblIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 13),
    _SnAgGblIfIpAddr_Type()
)
snAgGblIfIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblIfIpAddr.setStatus("current")
_SnAgGblIfIpMask_Type = IpAddress
_SnAgGblIfIpMask_Object = MibScalar
snAgGblIfIpMask = _SnAgGblIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 14),
    _SnAgGblIfIpMask_Type()
)
snAgGblIfIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblIfIpMask.setStatus("current")


class _SnAgGblPassword_Type(DisplayString):
    """Custom type snAgGblPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 97),
    )


_SnAgGblPassword_Type.__name__ = "DisplayString"
_SnAgGblPassword_Object = MibScalar
snAgGblPassword = _SnAgGblPassword_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 15),
    _SnAgGblPassword_Type()
)
snAgGblPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblPassword.setStatus("current")


class _SnAgTrpRcvrCurEntry_Type(Integer32):
    """Custom type snAgTrpRcvrCurEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnAgTrpRcvrCurEntry_Type.__name__ = "Integer32"
_SnAgTrpRcvrCurEntry_Object = MibScalar
snAgTrpRcvrCurEntry = _SnAgTrpRcvrCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 16),
    _SnAgTrpRcvrCurEntry_Type()
)
snAgTrpRcvrCurEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgTrpRcvrCurEntry.setStatus("current")


class _SnAgGblDataRetrieveMode_Type(Integer32):
    """Custom type snAgGblDataRetrieveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nextbootCfg", 0),
          ("operationalData", 1))
    )


_SnAgGblDataRetrieveMode_Type.__name__ = "Integer32"
_SnAgGblDataRetrieveMode_Object = MibScalar
snAgGblDataRetrieveMode = _SnAgGblDataRetrieveMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 19),
    _SnAgGblDataRetrieveMode_Type()
)
snAgGblDataRetrieveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblDataRetrieveMode.setStatus("current")


class _SnAgSystemLog_Type(OctetString):
    """Custom type snAgSystemLog based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_SnAgSystemLog_Type.__name__ = "OctetString"
_SnAgSystemLog_Object = MibScalar
snAgSystemLog = _SnAgSystemLog_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 20),
    _SnAgSystemLog_Type()
)
snAgSystemLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSystemLog.setStatus("current")


class _SnAgGblEnableColdStartTrap_Type(Integer32):
    """Custom type snAgGblEnableColdStartTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableColdStartTrap_Type.__name__ = "Integer32"
_SnAgGblEnableColdStartTrap_Object = MibScalar
snAgGblEnableColdStartTrap = _SnAgGblEnableColdStartTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 21),
    _SnAgGblEnableColdStartTrap_Type()
)
snAgGblEnableColdStartTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableColdStartTrap.setStatus("current")


class _SnAgGblEnableLinkUpTrap_Type(Integer32):
    """Custom type snAgGblEnableLinkUpTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableLinkUpTrap_Type.__name__ = "Integer32"
_SnAgGblEnableLinkUpTrap_Object = MibScalar
snAgGblEnableLinkUpTrap = _SnAgGblEnableLinkUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 22),
    _SnAgGblEnableLinkUpTrap_Type()
)
snAgGblEnableLinkUpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableLinkUpTrap.setStatus("current")


class _SnAgGblEnableLinkDownTrap_Type(Integer32):
    """Custom type snAgGblEnableLinkDownTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableLinkDownTrap_Type.__name__ = "Integer32"
_SnAgGblEnableLinkDownTrap_Object = MibScalar
snAgGblEnableLinkDownTrap = _SnAgGblEnableLinkDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 23),
    _SnAgGblEnableLinkDownTrap_Type()
)
snAgGblEnableLinkDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableLinkDownTrap.setStatus("current")


class _SnAgGblPasswordChangeMode_Type(Integer32):
    """Custom type snAgGblPasswordChangeMode based on Integer32"""
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
        *(("anyMgmtEntity", 1),
          ("consoleAndTelnet", 2),
          ("consoleOnly", 3),
          ("telnetOnly", 4))
    )


_SnAgGblPasswordChangeMode_Type.__name__ = "Integer32"
_SnAgGblPasswordChangeMode_Object = MibScalar
snAgGblPasswordChangeMode = _SnAgGblPasswordChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 24),
    _SnAgGblPasswordChangeMode_Type()
)
snAgGblPasswordChangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblPasswordChangeMode.setStatus("current")


class _SnAgGblReadOnlyCommunity_Type(DisplayString):
    """Custom type snAgGblReadOnlyCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgGblReadOnlyCommunity_Type.__name__ = "DisplayString"
_SnAgGblReadOnlyCommunity_Object = MibScalar
snAgGblReadOnlyCommunity = _SnAgGblReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 25),
    _SnAgGblReadOnlyCommunity_Type()
)
snAgGblReadOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblReadOnlyCommunity.setStatus("current")


class _SnAgGblReadWriteCommunity_Type(DisplayString):
    """Custom type snAgGblReadWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgGblReadWriteCommunity_Type.__name__ = "DisplayString"
_SnAgGblReadWriteCommunity_Object = MibScalar
snAgGblReadWriteCommunity = _SnAgGblReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 26),
    _SnAgGblReadWriteCommunity_Type()
)
snAgGblReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblReadWriteCommunity.setStatus("current")


class _SnAgGblCurrentSecurityLevel_Type(Integer32):
    """Custom type snAgGblCurrentSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SnAgGblCurrentSecurityLevel_Type.__name__ = "Integer32"
_SnAgGblCurrentSecurityLevel_Object = MibScalar
snAgGblCurrentSecurityLevel = _SnAgGblCurrentSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 27),
    _SnAgGblCurrentSecurityLevel_Type()
)
snAgGblCurrentSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblCurrentSecurityLevel.setStatus("current")


class _SnAgGblSecurityLevelSet_Type(Integer32):
    """Custom type snAgGblSecurityLevelSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SnAgGblSecurityLevelSet_Type.__name__ = "Integer32"
_SnAgGblSecurityLevelSet_Object = MibScalar
snAgGblSecurityLevelSet = _SnAgGblSecurityLevelSet_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 28),
    _SnAgGblSecurityLevelSet_Type()
)
snAgGblSecurityLevelSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblSecurityLevelSet.setStatus("current")
_SnAgGblLevelPasswordsMask_Type = Integer32
_SnAgGblLevelPasswordsMask_Object = MibScalar
snAgGblLevelPasswordsMask = _SnAgGblLevelPasswordsMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 29),
    _SnAgGblLevelPasswordsMask_Type()
)
snAgGblLevelPasswordsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblLevelPasswordsMask.setStatus("current")


class _SnAgGblQueueOverflow_Type(Integer32):
    """Custom type snAgGblQueueOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnAgGblQueueOverflow_Type.__name__ = "Integer32"
_SnAgGblQueueOverflow_Object = MibScalar
snAgGblQueueOverflow = _SnAgGblQueueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 30),
    _SnAgGblQueueOverflow_Type()
)
snAgGblQueueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblQueueOverflow.setStatus("current")


class _SnAgGblBufferShortage_Type(Integer32):
    """Custom type snAgGblBufferShortage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnAgGblBufferShortage_Type.__name__ = "Integer32"
_SnAgGblBufferShortage_Object = MibScalar
snAgGblBufferShortage = _SnAgGblBufferShortage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 31),
    _SnAgGblBufferShortage_Type()
)
snAgGblBufferShortage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblBufferShortage.setStatus("current")


class _SnAgGblDmaFailure_Type(Integer32):
    """Custom type snAgGblDmaFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnAgGblDmaFailure_Type.__name__ = "Integer32"
_SnAgGblDmaFailure_Object = MibScalar
snAgGblDmaFailure = _SnAgGblDmaFailure_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 32),
    _SnAgGblDmaFailure_Type()
)
snAgGblDmaFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblDmaFailure.setStatus("current")


class _SnAgGblResourceLowWarning_Type(Integer32):
    """Custom type snAgGblResourceLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnAgGblResourceLowWarning_Type.__name__ = "Integer32"
_SnAgGblResourceLowWarning_Object = MibScalar
snAgGblResourceLowWarning = _SnAgGblResourceLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 33),
    _SnAgGblResourceLowWarning_Type()
)
snAgGblResourceLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblResourceLowWarning.setStatus("current")


class _SnAgGblExcessiveErrorWarning_Type(Integer32):
    """Custom type snAgGblExcessiveErrorWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnAgGblExcessiveErrorWarning_Type.__name__ = "Integer32"
_SnAgGblExcessiveErrorWarning_Object = MibScalar
snAgGblExcessiveErrorWarning = _SnAgGblExcessiveErrorWarning_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 34),
    _SnAgGblExcessiveErrorWarning_Type()
)
snAgGblExcessiveErrorWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblExcessiveErrorWarning.setStatus("current")
_SnAgGblCpuUtilData_Type = Gauge32
_SnAgGblCpuUtilData_Object = MibScalar
snAgGblCpuUtilData = _SnAgGblCpuUtilData_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 35),
    _SnAgGblCpuUtilData_Type()
)
snAgGblCpuUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblCpuUtilData.setStatus("current")


class _SnAgGblCpuUtilCollect_Type(Integer32):
    """Custom type snAgGblCpuUtilCollect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblCpuUtilCollect_Type.__name__ = "Integer32"
_SnAgGblCpuUtilCollect_Object = MibScalar
snAgGblCpuUtilCollect = _SnAgGblCpuUtilCollect_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 36),
    _SnAgGblCpuUtilCollect_Type()
)
snAgGblCpuUtilCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblCpuUtilCollect.setStatus("deprecated")
_SnAgGblTelnetTimeout_Type = Integer32
_SnAgGblTelnetTimeout_Object = MibScalar
snAgGblTelnetTimeout = _SnAgGblTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 37),
    _SnAgGblTelnetTimeout_Type()
)
snAgGblTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblTelnetTimeout.setStatus("current")


class _SnAgGblEnableWebMgmt_Type(Integer32):
    """Custom type snAgGblEnableWebMgmt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableWebMgmt_Type.__name__ = "Integer32"
_SnAgGblEnableWebMgmt_Object = MibScalar
snAgGblEnableWebMgmt = _SnAgGblEnableWebMgmt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 38),
    _SnAgGblEnableWebMgmt_Type()
)
snAgGblEnableWebMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableWebMgmt.setStatus("current")
_SnAgGblSecurityLevelBinding_Type = Integer32
_SnAgGblSecurityLevelBinding_Object = MibScalar
snAgGblSecurityLevelBinding = _SnAgGblSecurityLevelBinding_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 39),
    _SnAgGblSecurityLevelBinding_Type()
)
snAgGblSecurityLevelBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblSecurityLevelBinding.setStatus("current")


class _SnAgGblEnableSLB_Type(Integer32):
    """Custom type snAgGblEnableSLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableSLB_Type.__name__ = "Integer32"
_SnAgGblEnableSLB_Object = MibScalar
snAgGblEnableSLB = _SnAgGblEnableSLB_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 40),
    _SnAgGblEnableSLB_Type()
)
snAgGblEnableSLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblEnableSLB.setStatus("current")
_SnAgSoftwareFeature_Type = OctetString
_SnAgSoftwareFeature_Object = MibScalar
snAgSoftwareFeature = _SnAgSoftwareFeature_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 41),
    _SnAgSoftwareFeature_Type()
)
snAgSoftwareFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSoftwareFeature.setStatus("current")


class _SnAgGblEnableModuleInsertedTrap_Type(Integer32):
    """Custom type snAgGblEnableModuleInsertedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableModuleInsertedTrap_Type.__name__ = "Integer32"
_SnAgGblEnableModuleInsertedTrap_Object = MibScalar
snAgGblEnableModuleInsertedTrap = _SnAgGblEnableModuleInsertedTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 42),
    _SnAgGblEnableModuleInsertedTrap_Type()
)
snAgGblEnableModuleInsertedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableModuleInsertedTrap.setStatus("current")


class _SnAgGblEnableModuleRemovedTrap_Type(Integer32):
    """Custom type snAgGblEnableModuleRemovedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableModuleRemovedTrap_Type.__name__ = "Integer32"
_SnAgGblEnableModuleRemovedTrap_Object = MibScalar
snAgGblEnableModuleRemovedTrap = _SnAgGblEnableModuleRemovedTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 43),
    _SnAgGblEnableModuleRemovedTrap_Type()
)
snAgGblEnableModuleRemovedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableModuleRemovedTrap.setStatus("current")
_SnAgGblTrapMessage_Type = DisplayString
_SnAgGblTrapMessage_Object = MibScalar
snAgGblTrapMessage = _SnAgGblTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 44),
    _SnAgGblTrapMessage_Type()
)
snAgGblTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblTrapMessage.setStatus("current")


class _SnAgGblEnableTelnetServer_Type(Integer32):
    """Custom type snAgGblEnableTelnetServer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableTelnetServer_Type.__name__ = "Integer32"
_SnAgGblEnableTelnetServer_Object = MibScalar
snAgGblEnableTelnetServer = _SnAgGblEnableTelnetServer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 45),
    _SnAgGblEnableTelnetServer_Type()
)
snAgGblEnableTelnetServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableTelnetServer.setStatus("current")


class _SnAgGblTelnetPassword_Type(DisplayString):
    """Custom type snAgGblTelnetPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnAgGblTelnetPassword_Type.__name__ = "DisplayString"
_SnAgGblTelnetPassword_Object = MibScalar
snAgGblTelnetPassword = _SnAgGblTelnetPassword_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 46),
    _SnAgGblTelnetPassword_Type()
)
snAgGblTelnetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblTelnetPassword.setStatus("current")


class _SnAgBuildDate_Type(DisplayString):
    """Custom type snAgBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgBuildDate_Type.__name__ = "DisplayString"
_SnAgBuildDate_Object = MibScalar
snAgBuildDate = _SnAgBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 47),
    _SnAgBuildDate_Type()
)
snAgBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgBuildDate.setStatus("current")


class _SnAgBuildtime_Type(DisplayString):
    """Custom type snAgBuildtime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgBuildtime_Type.__name__ = "DisplayString"
_SnAgBuildtime_Object = MibScalar
snAgBuildtime = _SnAgBuildtime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 48),
    _SnAgBuildtime_Type()
)
snAgBuildtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgBuildtime.setStatus("current")


class _SnAgBuildVer_Type(DisplayString):
    """Custom type snAgBuildVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgBuildVer_Type.__name__ = "DisplayString"
_SnAgBuildVer_Object = MibScalar
snAgBuildVer = _SnAgBuildVer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 49),
    _SnAgBuildVer_Type()
)
snAgBuildVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgBuildVer.setStatus("current")
_SnAgGblCpuUtil1SecAvg_Type = Gauge32
_SnAgGblCpuUtil1SecAvg_Object = MibScalar
snAgGblCpuUtil1SecAvg = _SnAgGblCpuUtil1SecAvg_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 50),
    _SnAgGblCpuUtil1SecAvg_Type()
)
snAgGblCpuUtil1SecAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblCpuUtil1SecAvg.setStatus("current")
_SnAgGblCpuUtil5SecAvg_Type = Gauge32
_SnAgGblCpuUtil5SecAvg_Object = MibScalar
snAgGblCpuUtil5SecAvg = _SnAgGblCpuUtil5SecAvg_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 51),
    _SnAgGblCpuUtil5SecAvg_Type()
)
snAgGblCpuUtil5SecAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblCpuUtil5SecAvg.setStatus("current")
_SnAgGblCpuUtil1MinAvg_Type = Gauge32
_SnAgGblCpuUtil1MinAvg_Object = MibScalar
snAgGblCpuUtil1MinAvg = _SnAgGblCpuUtil1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 52),
    _SnAgGblCpuUtil1MinAvg_Type()
)
snAgGblCpuUtil1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblCpuUtil1MinAvg.setStatus("current")
_SnAgGblDynMemUtil_Type = Gauge32
_SnAgGblDynMemUtil_Object = MibScalar
snAgGblDynMemUtil = _SnAgGblDynMemUtil_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 53),
    _SnAgGblDynMemUtil_Type()
)
snAgGblDynMemUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblDynMemUtil.setStatus("deprecated")
_SnAgGblDynMemTotal_Type = Integer32
_SnAgGblDynMemTotal_Object = MibScalar
snAgGblDynMemTotal = _SnAgGblDynMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 54),
    _SnAgGblDynMemTotal_Type()
)
snAgGblDynMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblDynMemTotal.setStatus("deprecated")
_SnAgGblDynMemFree_Type = Gauge32
_SnAgGblDynMemFree_Object = MibScalar
snAgGblDynMemFree = _SnAgGblDynMemFree_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 55),
    _SnAgGblDynMemFree_Type()
)
snAgGblDynMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblDynMemFree.setStatus("deprecated")


class _SnAgImgLoadSPModuleType_Type(Integer32):
    """Custom type snAgImgLoadSPModuleType based on Integer32"""
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
        *(("atm", 5),
          ("gignpa", 6),
          ("lp", 7),
          ("other", 1),
          ("pos12", 3),
          ("pos48", 4),
          ("vm1", 2))
    )


_SnAgImgLoadSPModuleType_Type.__name__ = "Integer32"
_SnAgImgLoadSPModuleType_Object = MibScalar
snAgImgLoadSPModuleType = _SnAgImgLoadSPModuleType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 56),
    _SnAgImgLoadSPModuleType_Type()
)
snAgImgLoadSPModuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgImgLoadSPModuleType.setStatus("current")
_SnAgImgLoadSPModuleNumber_Type = Integer32
_SnAgImgLoadSPModuleNumber_Object = MibScalar
snAgImgLoadSPModuleNumber = _SnAgImgLoadSPModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 57),
    _SnAgImgLoadSPModuleNumber_Type()
)
snAgImgLoadSPModuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgImgLoadSPModuleNumber.setStatus("current")


class _SnAgTrapHoldTime_Type(Integer32):
    """Custom type snAgTrapHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SnAgTrapHoldTime_Type.__name__ = "Integer32"
_SnAgTrapHoldTime_Object = MibScalar
snAgTrapHoldTime = _SnAgTrapHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 58),
    _SnAgTrapHoldTime_Type()
)
snAgTrapHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTrapHoldTime.setStatus("current")
_SnAgSFlowSourceInterface_Type = InterfaceIndex
_SnAgSFlowSourceInterface_Object = MibScalar
snAgSFlowSourceInterface = _SnAgSFlowSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 59),
    _SnAgSFlowSourceInterface_Type()
)
snAgSFlowSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSFlowSourceInterface.setStatus("current")
_SnAgGblTelnetLoginTimeout_Type = Integer32
_SnAgGblTelnetLoginTimeout_Object = MibScalar
snAgGblTelnetLoginTimeout = _SnAgGblTelnetLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 60),
    _SnAgGblTelnetLoginTimeout_Type()
)
snAgGblTelnetLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblTelnetLoginTimeout.setStatus("current")
_SnAgGblBannerExec_Type = DisplayString
_SnAgGblBannerExec_Object = MibScalar
snAgGblBannerExec = _SnAgGblBannerExec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 61),
    _SnAgGblBannerExec_Type()
)
snAgGblBannerExec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblBannerExec.setStatus("current")
_SnAgGblBannerIncoming_Type = DisplayString
_SnAgGblBannerIncoming_Object = MibScalar
snAgGblBannerIncoming = _SnAgGblBannerIncoming_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 62),
    _SnAgGblBannerIncoming_Type()
)
snAgGblBannerIncoming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblBannerIncoming.setStatus("current")
_SnAgGblBannerMotd_Type = DisplayString
_SnAgGblBannerMotd_Object = MibScalar
snAgGblBannerMotd = _SnAgGblBannerMotd_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 63),
    _SnAgGblBannerMotd_Type()
)
snAgGblBannerMotd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblBannerMotd.setStatus("current")


class _SnAgWebMgmtServerTcpPort_Type(Integer32):
    """Custom type snAgWebMgmtServerTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnAgWebMgmtServerTcpPort_Type.__name__ = "Integer32"
_SnAgWebMgmtServerTcpPort_Object = MibScalar
snAgWebMgmtServerTcpPort = _SnAgWebMgmtServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 64),
    _SnAgWebMgmtServerTcpPort_Type()
)
snAgWebMgmtServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgWebMgmtServerTcpPort.setStatus("current")


class _SnAgTftpServerAddrType_Type(InetAddressType):
    """Custom type snAgTftpServerAddrType based on InetAddressType"""


_SnAgTftpServerAddrType_Object = MibScalar
snAgTftpServerAddrType = _SnAgTftpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 65),
    _SnAgTftpServerAddrType_Type()
)
snAgTftpServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTftpServerAddrType.setStatus("current")
_SnAgTftpServerAddr_Type = InetAddress
_SnAgTftpServerAddr_Object = MibScalar
snAgTftpServerAddr = _SnAgTftpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 66),
    _SnAgTftpServerAddr_Type()
)
snAgTftpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTftpServerAddr.setStatus("current")
_SnAgGblDeleteFirstBeforeDownload_Type = TruthValue
_SnAgGblDeleteFirstBeforeDownload_Object = MibScalar
snAgGblDeleteFirstBeforeDownload = _SnAgGblDeleteFirstBeforeDownload_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 67),
    _SnAgGblDeleteFirstBeforeDownload_Type()
)
snAgGblDeleteFirstBeforeDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblDeleteFirstBeforeDownload.setStatus("current")


class _SnAgGblPasswordCheckMode_Type(EnabledStatus):
    """Custom type snAgGblPasswordCheckMode based on EnabledStatus"""


_SnAgGblPasswordCheckMode_Object = MibScalar
snAgGblPasswordCheckMode = _SnAgGblPasswordCheckMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 1, 68),
    _SnAgGblPasswordCheckMode_Type()
)
snAgGblPasswordCheckMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblPasswordCheckMode.setStatus("current")
_SnAgentBrd_ObjectIdentity = ObjectIdentity
snAgentBrd = _SnAgentBrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2)
)
_SnAgentBrdTable_Object = MibTable
snAgentBrdTable = _SnAgentBrdTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    snAgentBrdTable.setStatus("current")
_SnAgentBrdEntry_Object = MibTableRow
snAgentBrdEntry = _SnAgentBrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1)
)
snAgentBrdEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentBrdIndex"),
)
if mibBuilder.loadTexts:
    snAgentBrdEntry.setStatus("current")
_SnAgentBrdIndex_Type = Integer32
_SnAgentBrdIndex_Object = MibTableColumn
snAgentBrdIndex = _SnAgentBrdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 1),
    _SnAgentBrdIndex_Type()
)
snAgentBrdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdIndex.setStatus("current")


class _SnAgentBrdMainBrdDescription_Type(DisplayString):
    """Custom type snAgentBrdMainBrdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnAgentBrdMainBrdDescription_Type.__name__ = "DisplayString"
_SnAgentBrdMainBrdDescription_Object = MibTableColumn
snAgentBrdMainBrdDescription = _SnAgentBrdMainBrdDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 2),
    _SnAgentBrdMainBrdDescription_Type()
)
snAgentBrdMainBrdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMainBrdDescription.setStatus("current")
_SnAgentBrdMainBrdId_Type = OctetString
_SnAgentBrdMainBrdId_Object = MibTableColumn
snAgentBrdMainBrdId = _SnAgentBrdMainBrdId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 3),
    _SnAgentBrdMainBrdId_Type()
)
snAgentBrdMainBrdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMainBrdId.setStatus("current")
_SnAgentBrdMainPortTotal_Type = Integer32
_SnAgentBrdMainPortTotal_Object = MibTableColumn
snAgentBrdMainPortTotal = _SnAgentBrdMainPortTotal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 4),
    _SnAgentBrdMainPortTotal_Type()
)
snAgentBrdMainPortTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMainPortTotal.setStatus("current")


class _SnAgentBrdExpBrdDescription_Type(DisplayString):
    """Custom type snAgentBrdExpBrdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnAgentBrdExpBrdDescription_Type.__name__ = "DisplayString"
_SnAgentBrdExpBrdDescription_Object = MibTableColumn
snAgentBrdExpBrdDescription = _SnAgentBrdExpBrdDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 5),
    _SnAgentBrdExpBrdDescription_Type()
)
snAgentBrdExpBrdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdExpBrdDescription.setStatus("current")
_SnAgentBrdExpBrdId_Type = OctetString
_SnAgentBrdExpBrdId_Object = MibTableColumn
snAgentBrdExpBrdId = _SnAgentBrdExpBrdId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 6),
    _SnAgentBrdExpBrdId_Type()
)
snAgentBrdExpBrdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdExpBrdId.setStatus("current")


class _SnAgentBrdExpPortTotal_Type(Integer32):
    """Custom type snAgentBrdExpPortTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_SnAgentBrdExpPortTotal_Type.__name__ = "Integer32"
_SnAgentBrdExpPortTotal_Object = MibTableColumn
snAgentBrdExpPortTotal = _SnAgentBrdExpPortTotal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 7),
    _SnAgentBrdExpPortTotal_Type()
)
snAgentBrdExpPortTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdExpPortTotal.setStatus("current")
_SnAgentBrdStatusLeds_Type = Integer32
_SnAgentBrdStatusLeds_Object = MibTableColumn
snAgentBrdStatusLeds = _SnAgentBrdStatusLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 8),
    _SnAgentBrdStatusLeds_Type()
)
snAgentBrdStatusLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdStatusLeds.setStatus("deprecated")
_SnAgentBrdTrafficLeds_Type = Integer32
_SnAgentBrdTrafficLeds_Object = MibTableColumn
snAgentBrdTrafficLeds = _SnAgentBrdTrafficLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 9),
    _SnAgentBrdTrafficLeds_Type()
)
snAgentBrdTrafficLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdTrafficLeds.setStatus("deprecated")
_SnAgentBrdMediaLeds_Type = Integer32
_SnAgentBrdMediaLeds_Object = MibTableColumn
snAgentBrdMediaLeds = _SnAgentBrdMediaLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 10),
    _SnAgentBrdMediaLeds_Type()
)
snAgentBrdMediaLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMediaLeds.setStatus("deprecated")
_SnAgentBrdSpeedLeds_Type = Integer32
_SnAgentBrdSpeedLeds_Object = MibTableColumn
snAgentBrdSpeedLeds = _SnAgentBrdSpeedLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 11),
    _SnAgentBrdSpeedLeds_Type()
)
snAgentBrdSpeedLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdSpeedLeds.setStatus("deprecated")


class _SnAgentBrdModuleStatus_Type(Integer32):
    """Custom type snAgentBrdModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("moduleBad", 4),
          ("moduleBlocked", 11),
          ("moduleComingUp", 9),
          ("moduleConfigured", 8),
          ("moduleEmpty", 0),
          ("moduleGoingDown", 2),
          ("moduleRejected", 3),
          ("moduleRunning", 10))
    )


_SnAgentBrdModuleStatus_Type.__name__ = "Integer32"
_SnAgentBrdModuleStatus_Object = MibTableColumn
snAgentBrdModuleStatus = _SnAgentBrdModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 12),
    _SnAgentBrdModuleStatus_Type()
)
snAgentBrdModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdModuleStatus.setStatus("current")


class _SnAgentBrdRedundantStatus_Type(Integer32):
    """Custom type snAgentBrdRedundantStatus based on Integer32"""
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
        *(("active", 2),
          ("comingUp", 5),
          ("crashed", 4),
          ("other", 1),
          ("standby", 3))
    )


_SnAgentBrdRedundantStatus_Type.__name__ = "Integer32"
_SnAgentBrdRedundantStatus_Object = MibTableColumn
snAgentBrdRedundantStatus = _SnAgentBrdRedundantStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 13),
    _SnAgentBrdRedundantStatus_Type()
)
snAgentBrdRedundantStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdRedundantStatus.setStatus("current")
_SnAgentBrdAlarmLeds_Type = Integer32
_SnAgentBrdAlarmLeds_Object = MibTableColumn
snAgentBrdAlarmLeds = _SnAgentBrdAlarmLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 14),
    _SnAgentBrdAlarmLeds_Type()
)
snAgentBrdAlarmLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdAlarmLeds.setStatus("deprecated")
_SnAgentBrdTxTrafficLeds_Type = Integer32
_SnAgentBrdTxTrafficLeds_Object = MibTableColumn
snAgentBrdTxTrafficLeds = _SnAgentBrdTxTrafficLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 15),
    _SnAgentBrdTxTrafficLeds_Type()
)
snAgentBrdTxTrafficLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdTxTrafficLeds.setStatus("deprecated")
_SnAgentBrdRxTrafficLeds_Type = Integer32
_SnAgentBrdRxTrafficLeds_Object = MibTableColumn
snAgentBrdRxTrafficLeds = _SnAgentBrdRxTrafficLeds_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 16),
    _SnAgentBrdRxTrafficLeds_Type()
)
snAgentBrdRxTrafficLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdRxTrafficLeds.setStatus("deprecated")
_SnAgentBrdStatusLedString_Type = OctetString
_SnAgentBrdStatusLedString_Object = MibTableColumn
snAgentBrdStatusLedString = _SnAgentBrdStatusLedString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 17),
    _SnAgentBrdStatusLedString_Type()
)
snAgentBrdStatusLedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdStatusLedString.setStatus("current")
_SnAgentBrdTrafficLedString_Type = OctetString
_SnAgentBrdTrafficLedString_Object = MibTableColumn
snAgentBrdTrafficLedString = _SnAgentBrdTrafficLedString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 18),
    _SnAgentBrdTrafficLedString_Type()
)
snAgentBrdTrafficLedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdTrafficLedString.setStatus("current")
_SnAgentBrdMediaLedString_Type = OctetString
_SnAgentBrdMediaLedString_Object = MibTableColumn
snAgentBrdMediaLedString = _SnAgentBrdMediaLedString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 19),
    _SnAgentBrdMediaLedString_Type()
)
snAgentBrdMediaLedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMediaLedString.setStatus("current")
_SnAgentBrdSpeedLedString_Type = OctetString
_SnAgentBrdSpeedLedString_Object = MibTableColumn
snAgentBrdSpeedLedString = _SnAgentBrdSpeedLedString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 20),
    _SnAgentBrdSpeedLedString_Type()
)
snAgentBrdSpeedLedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdSpeedLedString.setStatus("current")
_SnAgentBrdAlarmLedString_Type = OctetString
_SnAgentBrdAlarmLedString_Object = MibTableColumn
snAgentBrdAlarmLedString = _SnAgentBrdAlarmLedString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 21),
    _SnAgentBrdAlarmLedString_Type()
)
snAgentBrdAlarmLedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdAlarmLedString.setStatus("current")
_SnAgentBrdTxTrafficLedString_Type = OctetString
_SnAgentBrdTxTrafficLedString_Object = MibTableColumn
snAgentBrdTxTrafficLedString = _SnAgentBrdTxTrafficLedString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 22),
    _SnAgentBrdTxTrafficLedString_Type()
)
snAgentBrdTxTrafficLedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdTxTrafficLedString.setStatus("current")
_SnAgentBrdRxTrafficLedString_Type = OctetString
_SnAgentBrdRxTrafficLedString_Object = MibTableColumn
snAgentBrdRxTrafficLedString = _SnAgentBrdRxTrafficLedString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 23),
    _SnAgentBrdRxTrafficLedString_Type()
)
snAgentBrdRxTrafficLedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdRxTrafficLedString.setStatus("current")
_SnAgentBrdMemoryTotal_Type = CounterBasedGauge64
_SnAgentBrdMemoryTotal_Object = MibTableColumn
snAgentBrdMemoryTotal = _SnAgentBrdMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 24),
    _SnAgentBrdMemoryTotal_Type()
)
snAgentBrdMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMemoryTotal.setStatus("current")
_SnAgentBrdMemoryAvailable_Type = CounterBasedGauge64
_SnAgentBrdMemoryAvailable_Object = MibTableColumn
snAgentBrdMemoryAvailable = _SnAgentBrdMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 25),
    _SnAgentBrdMemoryAvailable_Type()
)
snAgentBrdMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMemoryAvailable.setStatus("current")
_SnAgentBrdSerialNumber_Type = DisplayString
_SnAgentBrdSerialNumber_Object = MibTableColumn
snAgentBrdSerialNumber = _SnAgentBrdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 26),
    _SnAgentBrdSerialNumber_Type()
)
snAgentBrdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdSerialNumber.setStatus("current")
_SnAgentBrdPartNumber_Type = DisplayString
_SnAgentBrdPartNumber_Object = MibTableColumn
snAgentBrdPartNumber = _SnAgentBrdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 27),
    _SnAgentBrdPartNumber_Type()
)
snAgentBrdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdPartNumber.setStatus("current")


class _SnAgentBrdMemoryUtil100thPercent_Type(Unsigned32):
    """Custom type snAgentBrdMemoryUtil100thPercent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SnAgentBrdMemoryUtil100thPercent_Type.__name__ = "Unsigned32"
_SnAgentBrdMemoryUtil100thPercent_Object = MibTableColumn
snAgentBrdMemoryUtil100thPercent = _SnAgentBrdMemoryUtil100thPercent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 28),
    _SnAgentBrdMemoryUtil100thPercent_Type()
)
snAgentBrdMemoryUtil100thPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMemoryUtil100thPercent.setStatus("current")
_SnAgentBrdUpTime_Type = TimeTicks
_SnAgentBrdUpTime_Object = MibTableColumn
snAgentBrdUpTime = _SnAgentBrdUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 1, 1, 29),
    _SnAgentBrdUpTime_Type()
)
snAgentBrdUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdUpTime.setStatus("current")
_SnAgentBrd2Table_Object = MibTable
snAgentBrd2Table = _SnAgentBrd2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    snAgentBrd2Table.setStatus("current")
_SnAgentBrd2Entry_Object = MibTableRow
snAgentBrd2Entry = _SnAgentBrd2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 2, 1)
)
snAgentBrd2Entry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentBrd2Unit"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentBrd2Slot"),
)
if mibBuilder.loadTexts:
    snAgentBrd2Entry.setStatus("current")
_SnAgentBrd2Unit_Type = Integer32
_SnAgentBrd2Unit_Object = MibTableColumn
snAgentBrd2Unit = _SnAgentBrd2Unit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 2, 1, 1),
    _SnAgentBrd2Unit_Type()
)
snAgentBrd2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrd2Unit.setStatus("current")
_SnAgentBrd2Slot_Type = Integer32
_SnAgentBrd2Slot_Object = MibTableColumn
snAgentBrd2Slot = _SnAgentBrd2Slot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 2, 1, 2),
    _SnAgentBrd2Slot_Type()
)
snAgentBrd2Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrd2Slot.setStatus("current")


class _SnAgentBrd2MainBrdDescription_Type(DisplayString):
    """Custom type snAgentBrd2MainBrdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnAgentBrd2MainBrdDescription_Type.__name__ = "DisplayString"
_SnAgentBrd2MainBrdDescription_Object = MibTableColumn
snAgentBrd2MainBrdDescription = _SnAgentBrd2MainBrdDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 2, 1, 3),
    _SnAgentBrd2MainBrdDescription_Type()
)
snAgentBrd2MainBrdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrd2MainBrdDescription.setStatus("current")
_SnAgentBrd2MainBrdId_Type = OctetString
_SnAgentBrd2MainBrdId_Object = MibTableColumn
snAgentBrd2MainBrdId = _SnAgentBrd2MainBrdId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 2, 1, 4),
    _SnAgentBrd2MainBrdId_Type()
)
snAgentBrd2MainBrdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrd2MainBrdId.setStatus("current")
_SnAgentBrd2MainPortTotal_Type = Integer32
_SnAgentBrd2MainPortTotal_Object = MibTableColumn
snAgentBrd2MainPortTotal = _SnAgentBrd2MainPortTotal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 2, 1, 5),
    _SnAgentBrd2MainPortTotal_Type()
)
snAgentBrd2MainPortTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrd2MainPortTotal.setStatus("current")


class _SnAgentBrd2ModuleStatus_Type(Integer32):
    """Custom type snAgentBrd2ModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("moduleBad", 4),
          ("moduleBlocked", 11),
          ("moduleComingUp", 9),
          ("moduleConfigured", 8),
          ("moduleEmpty", 0),
          ("moduleGoingDown", 2),
          ("moduleRejected", 3),
          ("moduleRunning", 10))
    )


_SnAgentBrd2ModuleStatus_Type.__name__ = "Integer32"
_SnAgentBrd2ModuleStatus_Object = MibTableColumn
snAgentBrd2ModuleStatus = _SnAgentBrd2ModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 2, 1, 6),
    _SnAgentBrd2ModuleStatus_Type()
)
snAgentBrd2ModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrd2ModuleStatus.setStatus("current")


class _SnAgentBrd2RedundantStatus_Type(Integer32):
    """Custom type snAgentBrd2RedundantStatus based on Integer32"""
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
        *(("active", 2),
          ("comingUp", 5),
          ("crashed", 4),
          ("other", 1),
          ("standby", 3))
    )


_SnAgentBrd2RedundantStatus_Type.__name__ = "Integer32"
_SnAgentBrd2RedundantStatus_Object = MibTableColumn
snAgentBrd2RedundantStatus = _SnAgentBrd2RedundantStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 2, 2, 1, 7),
    _SnAgentBrd2RedundantStatus_Type()
)
snAgentBrd2RedundantStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrd2RedundantStatus.setStatus("current")
_SnAgentTrp_ObjectIdentity = ObjectIdentity
snAgentTrp = _SnAgentTrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 3)
)
_SnAgTrpRcvrTable_Object = MibTable
snAgTrpRcvrTable = _SnAgTrpRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    snAgTrpRcvrTable.setStatus("deprecated")
_SnAgTrpRcvrEntry_Object = MibTableRow
snAgTrpRcvrEntry = _SnAgTrpRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 3, 1, 1)
)
snAgTrpRcvrEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgTrpRcvrIndex"),
)
if mibBuilder.loadTexts:
    snAgTrpRcvrEntry.setStatus("deprecated")
_SnAgTrpRcvrIndex_Type = Integer32
_SnAgTrpRcvrIndex_Object = MibTableColumn
snAgTrpRcvrIndex = _SnAgTrpRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 3, 1, 1, 1),
    _SnAgTrpRcvrIndex_Type()
)
snAgTrpRcvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgTrpRcvrIndex.setStatus("deprecated")
_SnAgTrpRcvrIpAddr_Type = IpAddress
_SnAgTrpRcvrIpAddr_Object = MibTableColumn
snAgTrpRcvrIpAddr = _SnAgTrpRcvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 3, 1, 1, 2),
    _SnAgTrpRcvrIpAddr_Type()
)
snAgTrpRcvrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTrpRcvrIpAddr.setStatus("deprecated")


class _SnAgTrpRcvrCommunityOrSecurityName_Type(OctetString):
    """Custom type snAgTrpRcvrCommunityOrSecurityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgTrpRcvrCommunityOrSecurityName_Type.__name__ = "OctetString"
_SnAgTrpRcvrCommunityOrSecurityName_Object = MibTableColumn
snAgTrpRcvrCommunityOrSecurityName = _SnAgTrpRcvrCommunityOrSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 3, 1, 1, 3),
    _SnAgTrpRcvrCommunityOrSecurityName_Type()
)
snAgTrpRcvrCommunityOrSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTrpRcvrCommunityOrSecurityName.setStatus("deprecated")


class _SnAgTrpRcvrStatus_Type(Integer32):
    """Custom type snAgTrpRcvrStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("ignore", 5),
          ("other", 1),
          ("valid", 2))
    )


_SnAgTrpRcvrStatus_Type.__name__ = "Integer32"
_SnAgTrpRcvrStatus_Object = MibTableColumn
snAgTrpRcvrStatus = _SnAgTrpRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 3, 1, 1, 4),
    _SnAgTrpRcvrStatus_Type()
)
snAgTrpRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTrpRcvrStatus.setStatus("deprecated")


class _SnAgTrpRcvrUDPPort_Type(Integer32):
    """Custom type snAgTrpRcvrUDPPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnAgTrpRcvrUDPPort_Type.__name__ = "Integer32"
_SnAgTrpRcvrUDPPort_Object = MibTableColumn
snAgTrpRcvrUDPPort = _SnAgTrpRcvrUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 3, 1, 1, 5),
    _SnAgTrpRcvrUDPPort_Type()
)
snAgTrpRcvrUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTrpRcvrUDPPort.setStatus("deprecated")


class _SnAgTrpRcvrSecurityModel_Type(Integer32):
    """Custom type snAgTrpRcvrSecurityModel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("usm", 3),
          ("v1", 1),
          ("v2c", 2))
    )


_SnAgTrpRcvrSecurityModel_Type.__name__ = "Integer32"
_SnAgTrpRcvrSecurityModel_Object = MibTableColumn
snAgTrpRcvrSecurityModel = _SnAgTrpRcvrSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 3, 1, 1, 6),
    _SnAgTrpRcvrSecurityModel_Type()
)
snAgTrpRcvrSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTrpRcvrSecurityModel.setStatus("deprecated")


class _SnAgTrpRcvrSecurityLevel_Type(Integer32):
    """Custom type snAgTrpRcvrSecurityLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auth", 2),
          ("authPriv", 3),
          ("noAuth", 1))
    )


_SnAgTrpRcvrSecurityLevel_Type.__name__ = "Integer32"
_SnAgTrpRcvrSecurityLevel_Object = MibTableColumn
snAgTrpRcvrSecurityLevel = _SnAgTrpRcvrSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 3, 1, 1, 7),
    _SnAgTrpRcvrSecurityLevel_Type()
)
snAgTrpRcvrSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTrpRcvrSecurityLevel.setStatus("deprecated")
_SnAgentBoot_ObjectIdentity = ObjectIdentity
snAgentBoot = _SnAgentBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4)
)
_SnAgBootSeqTable_Object = MibTable
snAgBootSeqTable = _SnAgBootSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    snAgBootSeqTable.setStatus("current")
_SnAgBootSeqEntry_Object = MibTableRow
snAgBootSeqEntry = _SnAgBootSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 1, 1)
)
snAgBootSeqEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgBootSeqIndex"),
)
if mibBuilder.loadTexts:
    snAgBootSeqEntry.setStatus("current")


class _SnAgBootSeqIndex_Type(Integer32):
    """Custom type snAgBootSeqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SnAgBootSeqIndex_Type.__name__ = "Integer32"
_SnAgBootSeqIndex_Object = MibTableColumn
snAgBootSeqIndex = _SnAgBootSeqIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 1, 1, 1),
    _SnAgBootSeqIndex_Type()
)
snAgBootSeqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgBootSeqIndex.setStatus("current")


class _SnAgBootSeqInstruction_Type(Integer32):
    """Custom type snAgBootSeqInstruction based on Integer32"""
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
        *(("fromBootpServer", 4),
          ("fromPcmciaCard1", 5),
          ("fromPcmciaCard2", 6),
          ("fromPrimaryFlash", 1),
          ("fromSecondaryFlash", 2),
          ("fromTftpServer", 3))
    )


_SnAgBootSeqInstruction_Type.__name__ = "Integer32"
_SnAgBootSeqInstruction_Object = MibTableColumn
snAgBootSeqInstruction = _SnAgBootSeqInstruction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 1, 1, 2),
    _SnAgBootSeqInstruction_Type()
)
snAgBootSeqInstruction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgBootSeqInstruction.setStatus("current")
_SnAgBootSeqIpAddr_Type = IpAddress
_SnAgBootSeqIpAddr_Object = MibTableColumn
snAgBootSeqIpAddr = _SnAgBootSeqIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 1, 1, 3),
    _SnAgBootSeqIpAddr_Type()
)
snAgBootSeqIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgBootSeqIpAddr.setStatus("current")


class _SnAgBootSeqFilename_Type(DisplayString):
    """Custom type snAgBootSeqFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgBootSeqFilename_Type.__name__ = "DisplayString"
_SnAgBootSeqFilename_Object = MibTableColumn
snAgBootSeqFilename = _SnAgBootSeqFilename_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 1, 1, 4),
    _SnAgBootSeqFilename_Type()
)
snAgBootSeqFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgBootSeqFilename.setStatus("current")


class _SnAgBootSeqRowStatus_Type(Integer32):
    """Custom type snAgBootSeqRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnAgBootSeqRowStatus_Type.__name__ = "Integer32"
_SnAgBootSeqRowStatus_Object = MibTableColumn
snAgBootSeqRowStatus = _SnAgBootSeqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 1, 1, 5),
    _SnAgBootSeqRowStatus_Type()
)
snAgBootSeqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgBootSeqRowStatus.setStatus("current")
_SnAgSpBootSeqTable_Object = MibTable
snAgSpBootSeqTable = _SnAgSpBootSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    snAgSpBootSeqTable.setStatus("current")
_SnAgSpBootSeqEntry_Object = MibTableRow
snAgSpBootSeqEntry = _SnAgSpBootSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 2, 1)
)
snAgSpBootSeqEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgSpBootSeqSpNumber"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgSpBootSeqIndex"),
)
if mibBuilder.loadTexts:
    snAgSpBootSeqEntry.setStatus("current")


class _SnAgSpBootSeqSpNumber_Type(Integer32):
    """Custom type snAgSpBootSeqSpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SnAgSpBootSeqSpNumber_Type.__name__ = "Integer32"
_SnAgSpBootSeqSpNumber_Object = MibTableColumn
snAgSpBootSeqSpNumber = _SnAgSpBootSeqSpNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 2, 1, 1),
    _SnAgSpBootSeqSpNumber_Type()
)
snAgSpBootSeqSpNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snAgSpBootSeqSpNumber.setStatus("current")
_SnAgSpBootSeqIndex_Type = Integer32
_SnAgSpBootSeqIndex_Object = MibTableColumn
snAgSpBootSeqIndex = _SnAgSpBootSeqIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 2, 1, 2),
    _SnAgSpBootSeqIndex_Type()
)
snAgSpBootSeqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snAgSpBootSeqIndex.setStatus("current")


class _SnAgSpBootSeqInstruction_Type(Integer32):
    """Custom type snAgSpBootSeqInstruction based on Integer32"""
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
        *(("fromMpPrimaryFlash", 3),
          ("fromMpSecondaryFlash", 4),
          ("fromPcmciaCard1", 5),
          ("fromPcmciaCard2", 6),
          ("fromSpPrimaryFlash", 1),
          ("fromSpSecondaryFlash", 2),
          ("fromTftpServer", 7),
          ("interactively", 8))
    )


_SnAgSpBootSeqInstruction_Type.__name__ = "Integer32"
_SnAgSpBootSeqInstruction_Object = MibTableColumn
snAgSpBootSeqInstruction = _SnAgSpBootSeqInstruction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 2, 1, 3),
    _SnAgSpBootSeqInstruction_Type()
)
snAgSpBootSeqInstruction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSpBootSeqInstruction.setStatus("current")
_SnAgSpBootSeqIpAddr_Type = IpAddress
_SnAgSpBootSeqIpAddr_Object = MibTableColumn
snAgSpBootSeqIpAddr = _SnAgSpBootSeqIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 2, 1, 4),
    _SnAgSpBootSeqIpAddr_Type()
)
snAgSpBootSeqIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSpBootSeqIpAddr.setStatus("current")


class _SnAgSpBootSeqFilename_Type(DisplayString):
    """Custom type snAgSpBootSeqFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgSpBootSeqFilename_Type.__name__ = "DisplayString"
_SnAgSpBootSeqFilename_Object = MibTableColumn
snAgSpBootSeqFilename = _SnAgSpBootSeqFilename_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 2, 1, 5),
    _SnAgSpBootSeqFilename_Type()
)
snAgSpBootSeqFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSpBootSeqFilename.setStatus("current")


class _SnAgSpBootSeqRowStatus_Type(Integer32):
    """Custom type snAgSpBootSeqRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 3),
          ("delete", 2),
          ("valid", 1))
    )


_SnAgSpBootSeqRowStatus_Type.__name__ = "Integer32"
_SnAgSpBootSeqRowStatus_Object = MibTableColumn
snAgSpBootSeqRowStatus = _SnAgSpBootSeqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 4, 2, 1, 6),
    _SnAgSpBootSeqRowStatus_Type()
)
snAgSpBootSeqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSpBootSeqRowStatus.setStatus("current")
_SnAgCfgEos_ObjectIdentity = ObjectIdentity
snAgCfgEos = _SnAgCfgEos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 5)
)
_SnAgCfgEosTable_Object = MibTable
snAgCfgEosTable = _SnAgCfgEosTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    snAgCfgEosTable.setStatus("current")
_SnAgCfgEosEntry_Object = MibTableRow
snAgCfgEosEntry = _SnAgCfgEosEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 5, 1, 1)
)
snAgCfgEosEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgCfgEosIndex"),
)
if mibBuilder.loadTexts:
    snAgCfgEosEntry.setStatus("current")
_SnAgCfgEosIndex_Type = Integer32
_SnAgCfgEosIndex_Object = MibTableColumn
snAgCfgEosIndex = _SnAgCfgEosIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 5, 1, 1, 1),
    _SnAgCfgEosIndex_Type()
)
snAgCfgEosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgCfgEosIndex.setStatus("current")


class _SnAgCfgEosPacket_Type(OctetString):
    """Custom type snAgCfgEosPacket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_SnAgCfgEosPacket_Type.__name__ = "OctetString"
_SnAgCfgEosPacket_Object = MibTableColumn
snAgCfgEosPacket = _SnAgCfgEosPacket_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 5, 1, 1, 2),
    _SnAgCfgEosPacket_Type()
)
snAgCfgEosPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgCfgEosPacket.setStatus("current")
_SnAgCfgEosChkSum_Type = Integer32
_SnAgCfgEosChkSum_Object = MibTableColumn
snAgCfgEosChkSum = _SnAgCfgEosChkSum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 5, 1, 1, 3),
    _SnAgCfgEosChkSum_Type()
)
snAgCfgEosChkSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgCfgEosChkSum.setStatus("current")
_SnAgentLog_ObjectIdentity = ObjectIdentity
snAgentLog = _SnAgentLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6)
)
_SnAgSysLogGbl_ObjectIdentity = ObjectIdentity
snAgSysLogGbl = _SnAgSysLogGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1)
)


class _SnAgSysLogGblEnable_Type(Integer32):
    """Custom type snAgSysLogGblEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgSysLogGblEnable_Type.__name__ = "Integer32"
_SnAgSysLogGblEnable_Object = MibScalar
snAgSysLogGblEnable = _SnAgSysLogGblEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1, 1),
    _SnAgSysLogGblEnable_Type()
)
snAgSysLogGblEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblEnable.setStatus("current")


class _SnAgSysLogGblBufferSize_Type(Integer32):
    """Custom type snAgSysLogGblBufferSize based on Integer32"""
    defaultValue = 50


_SnAgSysLogGblBufferSize_Object = MibScalar
snAgSysLogGblBufferSize = _SnAgSysLogGblBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1, 2),
    _SnAgSysLogGblBufferSize_Type()
)
snAgSysLogGblBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblBufferSize.setStatus("current")


class _SnAgSysLogGblClear_Type(Integer32):
    """Custom type snAgSysLogGblClear based on Integer32"""
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
        *(("clearAll", 1),
          ("clearDynamic", 2),
          ("clearStatic", 3),
          ("normal", 0))
    )


_SnAgSysLogGblClear_Type.__name__ = "Integer32"
_SnAgSysLogGblClear_Object = MibScalar
snAgSysLogGblClear = _SnAgSysLogGblClear_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1, 3),
    _SnAgSysLogGblClear_Type()
)
snAgSysLogGblClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblClear.setStatus("current")


class _SnAgSysLogGblCriticalLevel_Type(Integer32):
    """Custom type snAgSysLogGblCriticalLevel based on Integer32"""
    defaultValue = 255


_SnAgSysLogGblCriticalLevel_Object = MibScalar
snAgSysLogGblCriticalLevel = _SnAgSysLogGblCriticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1, 4),
    _SnAgSysLogGblCriticalLevel_Type()
)
snAgSysLogGblCriticalLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblCriticalLevel.setStatus("current")
_SnAgSysLogGblLoggedCount_Type = Counter32
_SnAgSysLogGblLoggedCount_Object = MibScalar
snAgSysLogGblLoggedCount = _SnAgSysLogGblLoggedCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1, 5),
    _SnAgSysLogGblLoggedCount_Type()
)
snAgSysLogGblLoggedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogGblLoggedCount.setStatus("current")
_SnAgSysLogGblDroppedCount_Type = Counter32
_SnAgSysLogGblDroppedCount_Object = MibScalar
snAgSysLogGblDroppedCount = _SnAgSysLogGblDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1, 6),
    _SnAgSysLogGblDroppedCount_Type()
)
snAgSysLogGblDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogGblDroppedCount.setStatus("current")
_SnAgSysLogGblFlushedCount_Type = Counter32
_SnAgSysLogGblFlushedCount_Object = MibScalar
snAgSysLogGblFlushedCount = _SnAgSysLogGblFlushedCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1, 7),
    _SnAgSysLogGblFlushedCount_Type()
)
snAgSysLogGblFlushedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogGblFlushedCount.setStatus("current")
_SnAgSysLogGblOverrunCount_Type = Counter32
_SnAgSysLogGblOverrunCount_Object = MibScalar
snAgSysLogGblOverrunCount = _SnAgSysLogGblOverrunCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1, 8),
    _SnAgSysLogGblOverrunCount_Type()
)
snAgSysLogGblOverrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogGblOverrunCount.setStatus("current")
_SnAgSysLogGblServer_Type = IpAddress
_SnAgSysLogGblServer_Object = MibScalar
snAgSysLogGblServer = _SnAgSysLogGblServer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1, 9),
    _SnAgSysLogGblServer_Type()
)
snAgSysLogGblServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblServer.setStatus("deprecated")


class _SnAgSysLogGblFacility_Type(Integer32):
    """Custom type snAgSysLogGblFacility based on Integer32"""
    defaultValue = 2

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
              24)
        )
    )
    namedValues = NamedValues(
        *(("auth", 5),
          ("cron", 16),
          ("daemon", 4),
          ("kern", 1),
          ("local0", 17),
          ("local1", 18),
          ("local2", 19),
          ("local3", 20),
          ("local4", 21),
          ("local5", 22),
          ("local6", 23),
          ("local7", 24),
          ("lpr", 7),
          ("mail", 3),
          ("news", 8),
          ("sys10", 11),
          ("sys11", 12),
          ("sys12", 13),
          ("sys13", 14),
          ("sys14", 15),
          ("sys9", 10),
          ("syslog", 6),
          ("user", 2),
          ("uucp", 9))
    )


_SnAgSysLogGblFacility_Type.__name__ = "Integer32"
_SnAgSysLogGblFacility_Object = MibScalar
snAgSysLogGblFacility = _SnAgSysLogGblFacility_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1, 10),
    _SnAgSysLogGblFacility_Type()
)
snAgSysLogGblFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblFacility.setStatus("current")


class _SnAgSysLogGblPersistenceEnable_Type(Integer32):
    """Custom type snAgSysLogGblPersistenceEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgSysLogGblPersistenceEnable_Type.__name__ = "Integer32"
_SnAgSysLogGblPersistenceEnable_Object = MibScalar
snAgSysLogGblPersistenceEnable = _SnAgSysLogGblPersistenceEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 1, 11),
    _SnAgSysLogGblPersistenceEnable_Type()
)
snAgSysLogGblPersistenceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblPersistenceEnable.setStatus("current")
_SnAgSysLogBufferTable_Object = MibTable
snAgSysLogBufferTable = _SnAgSysLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    snAgSysLogBufferTable.setStatus("current")
_SnAgSysLogBufferEntry_Object = MibTableRow
snAgSysLogBufferEntry = _SnAgSysLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 2, 1)
)
snAgSysLogBufferEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgSysLogBufferIndex"),
)
if mibBuilder.loadTexts:
    snAgSysLogBufferEntry.setStatus("current")
_SnAgSysLogBufferIndex_Type = Integer32
_SnAgSysLogBufferIndex_Object = MibTableColumn
snAgSysLogBufferIndex = _SnAgSysLogBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 2, 1, 1),
    _SnAgSysLogBufferIndex_Type()
)
snAgSysLogBufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogBufferIndex.setStatus("current")
_SnAgSysLogBufferTimeStamp_Type = TimeTicks
_SnAgSysLogBufferTimeStamp_Object = MibTableColumn
snAgSysLogBufferTimeStamp = _SnAgSysLogBufferTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 2, 1, 2),
    _SnAgSysLogBufferTimeStamp_Type()
)
snAgSysLogBufferTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogBufferTimeStamp.setStatus("current")


class _SnAgSysLogBufferCriticalLevel_Type(Integer32):
    """Custom type snAgSysLogBufferCriticalLevel based on Integer32"""
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
        *(("alert", 2),
          ("critical", 3),
          ("debugging", 4),
          ("emergency", 5),
          ("error", 6),
          ("informational", 7),
          ("notification", 8),
          ("other", 1),
          ("warning", 9))
    )


_SnAgSysLogBufferCriticalLevel_Type.__name__ = "Integer32"
_SnAgSysLogBufferCriticalLevel_Object = MibTableColumn
snAgSysLogBufferCriticalLevel = _SnAgSysLogBufferCriticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 2, 1, 3),
    _SnAgSysLogBufferCriticalLevel_Type()
)
snAgSysLogBufferCriticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogBufferCriticalLevel.setStatus("current")
_SnAgSysLogBufferMessage_Type = DisplayString
_SnAgSysLogBufferMessage_Object = MibTableColumn
snAgSysLogBufferMessage = _SnAgSysLogBufferMessage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 2, 1, 4),
    _SnAgSysLogBufferMessage_Type()
)
snAgSysLogBufferMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogBufferMessage.setStatus("current")
_SnAgSysLogBufferCalTimeStamp_Type = DisplayString
_SnAgSysLogBufferCalTimeStamp_Object = MibTableColumn
snAgSysLogBufferCalTimeStamp = _SnAgSysLogBufferCalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 2, 1, 5),
    _SnAgSysLogBufferCalTimeStamp_Type()
)
snAgSysLogBufferCalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogBufferCalTimeStamp.setStatus("current")
_SnAgStaticSysLogBufferTable_Object = MibTable
snAgStaticSysLogBufferTable = _SnAgStaticSysLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferTable.setStatus("current")
_SnAgStaticSysLogBufferEntry_Object = MibTableRow
snAgStaticSysLogBufferEntry = _SnAgStaticSysLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 3, 1)
)
snAgStaticSysLogBufferEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgStaticSysLogBufferIndex"),
)
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferEntry.setStatus("current")


class _SnAgStaticSysLogBufferIndex_Type(Integer32):
    """Custom type snAgStaticSysLogBufferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SnAgStaticSysLogBufferIndex_Type.__name__ = "Integer32"
_SnAgStaticSysLogBufferIndex_Object = MibTableColumn
snAgStaticSysLogBufferIndex = _SnAgStaticSysLogBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 3, 1, 1),
    _SnAgStaticSysLogBufferIndex_Type()
)
snAgStaticSysLogBufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferIndex.setStatus("current")
_SnAgStaticSysLogBufferTimeStamp_Type = TimeTicks
_SnAgStaticSysLogBufferTimeStamp_Object = MibTableColumn
snAgStaticSysLogBufferTimeStamp = _SnAgStaticSysLogBufferTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 3, 1, 2),
    _SnAgStaticSysLogBufferTimeStamp_Type()
)
snAgStaticSysLogBufferTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferTimeStamp.setStatus("current")


class _SnAgStaticSysLogBufferCriticalLevel_Type(Integer32):
    """Custom type snAgStaticSysLogBufferCriticalLevel based on Integer32"""
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
        *(("alert", 2),
          ("critical", 3),
          ("debugging", 4),
          ("emergency", 5),
          ("error", 6),
          ("informational", 7),
          ("notification", 8),
          ("other", 1),
          ("warning", 9))
    )


_SnAgStaticSysLogBufferCriticalLevel_Type.__name__ = "Integer32"
_SnAgStaticSysLogBufferCriticalLevel_Object = MibTableColumn
snAgStaticSysLogBufferCriticalLevel = _SnAgStaticSysLogBufferCriticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 3, 1, 3),
    _SnAgStaticSysLogBufferCriticalLevel_Type()
)
snAgStaticSysLogBufferCriticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferCriticalLevel.setStatus("current")
_SnAgStaticSysLogBufferMessage_Type = DisplayString
_SnAgStaticSysLogBufferMessage_Object = MibTableColumn
snAgStaticSysLogBufferMessage = _SnAgStaticSysLogBufferMessage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 3, 1, 4),
    _SnAgStaticSysLogBufferMessage_Type()
)
snAgStaticSysLogBufferMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferMessage.setStatus("current")
_SnAgStaticSysLogBufferCalTimeStamp_Type = DisplayString
_SnAgStaticSysLogBufferCalTimeStamp_Object = MibTableColumn
snAgStaticSysLogBufferCalTimeStamp = _SnAgStaticSysLogBufferCalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 3, 1, 5),
    _SnAgStaticSysLogBufferCalTimeStamp_Type()
)
snAgStaticSysLogBufferCalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferCalTimeStamp.setStatus("current")
_SnAgSysLogServerTable_Object = MibTable
snAgSysLogServerTable = _SnAgSysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    snAgSysLogServerTable.setStatus("current")
_SnAgSysLogServerEntry_Object = MibTableRow
snAgSysLogServerEntry = _SnAgSysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 4, 1)
)
snAgSysLogServerEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgSysLogServerIP"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgSysLogServerUDPPort"),
)
if mibBuilder.loadTexts:
    snAgSysLogServerEntry.setStatus("current")
_SnAgSysLogServerIP_Type = IpAddress
_SnAgSysLogServerIP_Object = MibTableColumn
snAgSysLogServerIP = _SnAgSysLogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 4, 1, 1),
    _SnAgSysLogServerIP_Type()
)
snAgSysLogServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogServerIP.setStatus("current")


class _SnAgSysLogServerUDPPort_Type(Integer32):
    """Custom type snAgSysLogServerUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnAgSysLogServerUDPPort_Type.__name__ = "Integer32"
_SnAgSysLogServerUDPPort_Object = MibTableColumn
snAgSysLogServerUDPPort = _SnAgSysLogServerUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 4, 1, 2),
    _SnAgSysLogServerUDPPort_Type()
)
snAgSysLogServerUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogServerUDPPort.setStatus("current")


class _SnAgSysLogServerRowStatus_Type(Integer32):
    """Custom type snAgSysLogServerRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnAgSysLogServerRowStatus_Type.__name__ = "Integer32"
_SnAgSysLogServerRowStatus_Object = MibTableColumn
snAgSysLogServerRowStatus = _SnAgSysLogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 6, 4, 1, 3),
    _SnAgSysLogServerRowStatus_Type()
)
snAgSysLogServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogServerRowStatus.setStatus("current")
_SnAgentSysParaConfig_ObjectIdentity = ObjectIdentity
snAgentSysParaConfig = _SnAgentSysParaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 7)
)
_SnAgentSysParaConfigTable_Object = MibTable
snAgentSysParaConfigTable = _SnAgentSysParaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    snAgentSysParaConfigTable.setStatus("current")
_SnAgentSysParaConfigEntry_Object = MibTableRow
snAgentSysParaConfigEntry = _SnAgentSysParaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 7, 1, 1)
)
snAgentSysParaConfigEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentSysParaConfigIndex"),
)
if mibBuilder.loadTexts:
    snAgentSysParaConfigEntry.setStatus("current")
_SnAgentSysParaConfigIndex_Type = Integer32
_SnAgentSysParaConfigIndex_Object = MibTableColumn
snAgentSysParaConfigIndex = _SnAgentSysParaConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 7, 1, 1, 1),
    _SnAgentSysParaConfigIndex_Type()
)
snAgentSysParaConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentSysParaConfigIndex.setStatus("current")


class _SnAgentSysParaConfigDescription_Type(DisplayString):
    """Custom type snAgentSysParaConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgentSysParaConfigDescription_Type.__name__ = "DisplayString"
_SnAgentSysParaConfigDescription_Object = MibTableColumn
snAgentSysParaConfigDescription = _SnAgentSysParaConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 7, 1, 1, 2),
    _SnAgentSysParaConfigDescription_Type()
)
snAgentSysParaConfigDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentSysParaConfigDescription.setStatus("current")
_SnAgentSysParaConfigMin_Type = Integer32
_SnAgentSysParaConfigMin_Object = MibTableColumn
snAgentSysParaConfigMin = _SnAgentSysParaConfigMin_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 7, 1, 1, 3),
    _SnAgentSysParaConfigMin_Type()
)
snAgentSysParaConfigMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentSysParaConfigMin.setStatus("current")
_SnAgentSysParaConfigMax_Type = Integer32
_SnAgentSysParaConfigMax_Object = MibTableColumn
snAgentSysParaConfigMax = _SnAgentSysParaConfigMax_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 7, 1, 1, 4),
    _SnAgentSysParaConfigMax_Type()
)
snAgentSysParaConfigMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentSysParaConfigMax.setStatus("current")
_SnAgentSysParaConfigDefault_Type = Integer32
_SnAgentSysParaConfigDefault_Object = MibTableColumn
snAgentSysParaConfigDefault = _SnAgentSysParaConfigDefault_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 7, 1, 1, 5),
    _SnAgentSysParaConfigDefault_Type()
)
snAgentSysParaConfigDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentSysParaConfigDefault.setStatus("current")
_SnAgentSysParaConfigCurrent_Type = Integer32
_SnAgentSysParaConfigCurrent_Object = MibTableColumn
snAgentSysParaConfigCurrent = _SnAgentSysParaConfigCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 7, 1, 1, 6),
    _SnAgentSysParaConfigCurrent_Type()
)
snAgentSysParaConfigCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentSysParaConfigCurrent.setStatus("current")
_SnAgentConfigModule_ObjectIdentity = ObjectIdentity
snAgentConfigModule = _SnAgentConfigModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8)
)
_SnAgentConfigModuleTable_Object = MibTable
snAgentConfigModuleTable = _SnAgentConfigModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    snAgentConfigModuleTable.setStatus("current")
_SnAgentConfigModuleEntry_Object = MibTableRow
snAgentConfigModuleEntry = _SnAgentConfigModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 1, 1)
)
snAgentConfigModuleEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentConfigModuleIndex"),
)
if mibBuilder.loadTexts:
    snAgentConfigModuleEntry.setStatus("current")
_SnAgentConfigModuleIndex_Type = Integer32
_SnAgentConfigModuleIndex_Object = MibTableColumn
snAgentConfigModuleIndex = _SnAgentConfigModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 1, 1, 1),
    _SnAgentConfigModuleIndex_Type()
)
snAgentConfigModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModuleIndex.setStatus("current")


class _SnAgentConfigModuleType_Type(Integer32):
    """Custom type snAgentConfigModuleType based on Integer32"""
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
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              103,
              112,
              113,
              114,
              144,
              145,
              152,
              153,
              154,
              155,
              160,
              161,
              168,
              169,
              176,
              177,
              180,
              181,
              184,
              185,
              192,
              195,
              196,
              197,
              198,
              200,
              201,
              202,
              206,
              207,
              208,
              209,
              212,
              214,
              1048,
              1049,
              1050,
              1051,
              1052,
              1053,
              1054,
              1055,
              1056,
              1057,
              1058,
              1059,
              1060,
              1061,
              1062,
              1063,
              1064,
              1065,
              1066,
              1067,
              1075,
              1076,
              1077,
              1078,
              1079,
              1080,
              1081,
              1082,
              1083,
              1084,
              1085,
              1086,
              1087,
              1088,
              1089,
              1090,
              1091,
              1093,
              1094,
              1095,
              1096,
              1097,
              1098,
              1099,
              1100,
              1101,
              1102,
              1103,
              1104,
              1105,
              1106,
              1107,
              1108,
              1109,
              1110,
              1111,
              1112,
              1113,
              1114,
              1115,
              1116,
              1117,
              1118,
              1119,
              1120,
              1121,
              1122,
              1123,
              1124,
              1125,
              2016,
              2017,
              2020,
              2021,
              2024,
              2032,
              2033,
              2036,
              2037,
              2040,
              2055,
              2056,
              2057,
              2064,
              2065,
              2066,
              2067,
              2068,
              2069,
              2074,
              2080,
              2081,
              2083,
              2096,
              2098,
              2100,
              2101,
              2102,
              2103,
              2104,
              2105,
              2106,
              2112,
              2113,
              2132,
              2133,
              2134,
              2135,
              2136,
              2137,
              2138,
              2139,
              2140,
              2141,
              2142,
              2208,
              2209,
              2220,
              2224,
              2225,
              2227,
              2228,
              2229,
              2233,
              2234,
              2235,
              2236,
              2240,
              2241,
              2244,
              2245,
              2246,
              2248,
              2249)
        )
    )
    namedValues = NamedValues(
        *(("bi0PortGigM4ManagementModule", 38),
          ("bi0PortManagementModule", 20),
          ("bi0PortWSMManagementModule", 39),
          ("bi0PortWSMModule", 41),
          ("bi10PortGigHVModule", 61),
          ("bi12PortGigCopper2PortGigFiber", 15),
          ("bi12PortGigCopper2PortGigFiberManagement", 9),
          ("bi16Port100FXModule", 12),
          ("bi16PortCopperManagementModule", 2),
          ("bi1Port10GigModule", 47),
          ("bi20PortGigHVModule", 62),
          ("bi24Port100FXModule", 19),
          ("bi24PortCopperModule", 10),
          ("bi24PortGigCopperModule", 64),
          ("bi24PortGigFiberModule", 66),
          ("bi24PortGigModule", 63),
          ("bi2Port10GigModule", 207),
          ("bi2PortGigCopperManagementModule", 34),
          ("bi2PortGigCopperModule", 24),
          ("bi2PortGigM4ManagementModule", 37),
          ("bi2PortGigManagementModule", 18),
          ("bi2PortGigModule", 23),
          ("bi40PortGigCopperHVModule", 58),
          ("bi48PortGigCopperModule", 65),
          ("bi4PortGigCopperManagementModule", 33),
          ("bi4PortGigM4ManagementModule", 36),
          ("bi4PortGigManagementModule", 1),
          ("bi4PortGigModule", 3),
          ("bi4PortGigNPAModule", 44),
          ("bi60PortGigCopperHVModule", 59),
          ("bi8Port100FXModule", 13),
          ("bi8Port10GigModule", 60),
          ("bi8PortGigCopperManagementModule", 6),
          ("bi8PortGigCopperModule", 14),
          ("bi8PortGigM4ManagementModule", 35),
          ("bi8PortGigManagementModule", 0),
          ("bi8PortGigModule", 8),
          ("biAtm2Port155MbsModule", 45),
          ("biAtm4Port155MbsModule", 46),
          ("biFiJc16PortGigIgcModule", 200),
          ("biFiJc24Port100fxIpcModule", 206),
          ("biFiJc48ePort100fxIpcModule", 195),
          ("biFiJc48tPort100fxIpcModule", 196),
          ("biFiJc8PortGigIgcModule", 198),
          ("biFiJc8PortGigM4ManagementModule", 197),
          ("biJc16PortGigCopperIgcModule", 202),
          ("biJc24PortCopperIpc4GigIgcModule", 201),
          ("biJc24PortIpcRJ45PoeModule", 212),
          ("biJc2PortGigIgcM4ManagementModule", 214),
          ("biJc48ePortRJ45OmpModule", 209),
          ("biJc48tPortRJ21OmpModule", 208),
          ("biPos2Port2488MbsModule", 40),
          ("brMlx20Port10GigModule", 1124),
          ("brMlx24PortGigCopperXModule", 1094),
          ("brMlx24PortGigSfpXModule", 1095),
          ("brMlx2Port100GigCFP2Module", 1123),
          ("brMlx2Port100GigXModule", 1113),
          ("brMlx4Port10GigXIPSecModule", 1125),
          ("brMlx4Port10GigXModule", 1093),
          ("brMlx4Port40GigMModule", 1121),
          ("brMlx8Port10GigXModule", 1112),
          ("brcdMlx24Port10GigDMModule", 1120),
          ("brcdMlx32Mr2ManagementModule", 1116),
          ("brcdMlxMr2ManagementModule", 1114),
          ("brcdNiCes4Port10GigModule", 1122),
          ("brcdNiMlx32MrManagementModule", 1119),
          ("brcdNiXmr32MrManagementModule", 1118),
          ("brcdXmr32Mr2ManagementModule", 1117),
          ("brcdXmrMr2ManagementModule", 1115),
          ("fcx624SBaseModule", 176),
          ("fcx624SFBaseModule", 192),
          ("fcx624SPoeBaseModule", 180),
          ("fcx648SBaseModule", 177),
          ("fcx648SPoeBaseModule", 181),
          ("fcxCx42Port16gModule", 185),
          ("fcxXfp2Port10gModule", 184),
          ("fdryBi10PortGigHVModule", 1061),
          ("fdryBi16Port10GigModule", 1067),
          ("fdryBi1Port100FXManagementModule", 1050),
          ("fdryBi20PortGigHVModule", 1062),
          ("fdryBi24PortGigCopperModule", 1064),
          ("fdryBi24PortGigFiberModule", 1066),
          ("fdryBi24PortGigModule", 1063),
          ("fdryBi2Port10GigHVModule", 1055),
          ("fdryBi2Port10GigModule", 1051),
          ("fdryBi40PortGigCopperHVModule", 1058),
          ("fdryBi40PortGigCopperModule", 1052),
          ("fdryBi40PortGigHVModule", 1057),
          ("fdryBi40PortGigModule", 1049),
          ("fdryBi48PortGigCopperModule", 1065),
          ("fdryBi4Port10GigHVModule", 1054),
          ("fdryBi4Port10GigModule", 1048),
          ("fdryBi60PortGigCopperHVModule", 1059),
          ("fdryBi60PortGigCopperModule", 1053),
          ("fdryBi8Port10GigHVModule", 1056),
          ("fdryBi8Port10GigModule", 1060),
          ("fdryFcx624BaseModule", 2208),
          ("fdryFcx648BaseModule", 2209),
          ("fdryFcxSfpPlus4Port10gModule", 2220),
          ("fdryFiSx0PortManagementModule", 2081),
          ("fdryFiV4Sx12ComboPortManagement2Module", 2074),
          ("fdryFiV4Sx12ComboPortManagementModule", 2064),
          ("fdryFiV4Sx210gPortManagementModule", 2080),
          ("fdryFiV4Sx24Port100m1gFiberModule", 2069),
          ("fdryFiV4Sx24PortGigCopperModule", 2066),
          ("fdryFiV4Sx24PortGigFiberModule", 2067),
          ("fdryFiV4Sx2Port10gLanWanModule", 2068),
          ("fdryFiV4Sx2Port10gModule", 2065),
          ("fdryFiV4Sx4g4fPortManagementModule", 2083),
          ("fdryFiV6Sx12ComboPortManagement2Module", 2105),
          ("fdryFiV6Sx12ComboPortManagementModule", 2096),
          ("fdryFiV6Sx210gPortManagementModule", 2102),
          ("fdryFiV6Sx24Port100m1gFiberModule", 2101),
          ("fdryFiV6Sx24PortGigCopperModule", 2098),
          ("fdryFiV6Sx2Port10gModule", 2100),
          ("fdryFiV6Sx48PortGigCopperModule", 2106),
          ("fdryFiV6Sx48PortGigCopperPoeModule", 2103),
          ("fdryFiV6Sx4g4fPortManagementModule", 2104),
          ("fdryFiV6SxXl0PortManagementModule", 2112),
          ("fdryFiV6SxXl210gPortManagementModule", 2113),
          ("fdryIcx6430612CBaseModule", 2137),
          ("fdryIcx6430624BaseModule", 2016),
          ("fdryIcx6430624PoeBaseModule", 2020),
          ("fdryIcx6430648BaseModule", 2017),
          ("fdryIcx6430648PoeBaseModule", 2021),
          ("fdryIcx6430Copper2Port2gModule", 2138),
          ("fdryIcx6430sfp2Port2gModule", 2139),
          ("fdryIcx6430sfp4Port4gModule", 2024),
          ("fdryIcx6450612CPDBaseModule", 2140),
          ("fdryIcx6450624BaseModule", 2032),
          ("fdryIcx6450624PoeBaseModule", 2036),
          ("fdryIcx6450648BaseModule", 2033),
          ("fdryIcx6450648PoeBaseModule", 2037),
          ("fdryIcx6450Copper2Port2gModule", 2141),
          ("fdryIcx6450sfp2Port2gModule", 2142),
          ("fdryIcx6450sfp4Port40gModule", 2040),
          ("fdryIcx6610624BaseModule", 2240),
          ("fdryIcx6610624FBaseModule", 2246),
          ("fdryIcx6610624PoeBaseModule", 2244),
          ("fdryIcx6610648BaseModule", 2241),
          ("fdryIcx6610648PoeBaseModule", 2245),
          ("fdryIcx6610DualMode8PortModule", 2248),
          ("fdryIcx6610Qsfp10Port160gModule", 2249),
          ("fdryIcx665056BaseModule", 2055),
          ("fdryIcx6650sfp4Port40gModule", 2056),
          ("fdryIcx6650sfp8Port10gModule", 2057),
          ("fdryIcx7400copper4Port40gModule", 2234),
          ("fdryIcx7400qsfpplus1Port40gModule", 2236),
          ("fdryIcx7400sfp4Port4gModule", 2235),
          ("fdryIcx7400sfpplus4Port40gModule", 2233),
          ("fdryIcx7450624BaseModule", 2224),
          ("fdryIcx7450624PoeBaseModule", 2228),
          ("fdryIcx7450648BaseModule", 2225),
          ("fdryIcx7450648FBaseModule", 2227),
          ("fdryIcx7450648PoeBaseModule", 2229),
          ("fdryIcx775026QBaseModule", 2134),
          ("fdryIcx775048CBaseModule", 2136),
          ("fdryIcx775048FBaseModule", 2135),
          ("fdryIcx77506Q6port40gModule", 2133),
          ("fdryIcx7750QSFP6port40gModule", 2132),
          ("fdryMlx20PortGigCopperSPModule", 1090),
          ("fdryMlx20PortGigFXSPModule", 1091),
          ("fdryMlx2Port10GigSPModule", 1089),
          ("fdryMlx48PortGigMrj21SPModule", 1103),
          ("fdryMlx4Port10GigSPModule", 1088),
          ("fdryNi10PortGigSPModule", 1079),
          ("fdryNi20PortGigSPModule", 1080),
          ("fdryNi2Port10GigSPModule", 1078),
          ("fdryNi40PortGigCopperSPModule", 1077),
          ("fdryNi40PortGigSPModule", 1076),
          ("fdryNi4Port10GigSPModule", 1075),
          ("fdryNiImrMrManagementModule", 1086),
          ("fdryNiMlxMrManagementModule", 1109),
          ("fdryNiXmrMrManagementModule", 1087),
          ("fdryXmr1PortOC192SPModule", 1105),
          ("fdryXmr20PortGigCopperSPModule", 1084),
          ("fdryXmr20PortGigFXSPModule", 1085),
          ("fdryXmr20PortGigSPModule", 1082),
          ("fdryXmr2Port10GigSPModule", 1083),
          ("fdryXmr2PortOC192SPModule", 1104),
          ("fdryXmr2PortOC48SPModule", 1108),
          ("fdryXmr4Port10GigSPModule", 1081),
          ("fdryXmr4PortOC48SPModule", 1107),
          ("fdryXmr8PortOC48SPModule", 1106),
          ("fes12GigCopperAndGigFiberModule", 51),
          ("fes2402Module", 49),
          ("fes4802Module", 48),
          ("fes9604Module", 50),
          ("fesx24Gig1TenGigModule", 54),
          ("fesx24Gig2TenGigModule", 53),
          ("fesx24GigFiber1TenGigModule", 114),
          ("fesx24GigFiber2TenGigModule", 113),
          ("fesx24GigFiberGigCopperModule", 112),
          ("fesx24GigModule", 52),
          ("fesx48Gig1TenGigModule", 57),
          ("fesx48Gig2TenGigModule", 56),
          ("fesx48GigModule", 55),
          ("fgs24PortManagementModule", 144),
          ("fgs48PortManagementModule", 145),
          ("fgsCx42Port10gModule", 153),
          ("fgsXfp1Cx41Port10gModule", 154),
          ("fgsXfp2Port10gModule", 152),
          ("fgsXpf1Port10gModule", 155),
          ("fi24PortCopperModule", 11),
          ("fi2PortGigCopperManagementModule", 32),
          ("fi2PortGigManagementModule", 4),
          ("fi2PortGigModule", 25),
          ("fi4PortGigCopperManagementModule", 31),
          ("fi4PortGigManagementModule", 5),
          ("fi4PortGigModule", 26),
          ("fi8PortGigCopperManagementModule", 29),
          ("fi8PortGigCopperModule", 28),
          ("fi8PortGigManagementModule", 7),
          ("fi8PortGigModule", 27),
          ("fls24PortCopperBaseModule", 160),
          ("fls48PortCopperBaseModule", 161),
          ("flsCx41Port10gModule", 169),
          ("flsXfp1Port10gModule", 168),
          ("mlx20PortGigCopperSPModule", 94),
          ("mlx20PortGigFXSPModule", 95),
          ("mlx2Port10GigSPModule", 93),
          ("mlx48PortGigMrj21SPModule", 103),
          ("mlx4Port10GigSPModule", 92),
          ("ni10PortGigSPModule", 79),
          ("ni20PortGigSPModule", 80),
          ("ni2Port10GigSPModule", 78),
          ("ni40PortGigCopperSPModule", 77),
          ("ni40PortGigSPModule", 76),
          ("ni4802", 43),
          ("ni4Port10GigSPModule", 75),
          ("niCes24PortCopperModule", 1097),
          ("niCes24PortFiberModule", 1096),
          ("niCes2Port10GigModule", 1098),
          ("niCes48PortCopperModule", 1100),
          ("niCes48PortCopperWith2Port10GModule", 1102),
          ("niCes48PortFiberModule", 1099),
          ("niCes48PortFiberWith2Port10GModule", 1101),
          ("niImrMrManagementModule", 86),
          ("niMlx8Port10GigDModule", 1111),
          ("niMlx8Port10GigMModule", 1110),
          ("niPos2Port2488MbsModule", 42),
          ("niXmrMrManagementModule", 87),
          ("pos155Mbs2PModule", 30),
          ("pos155MbsModule", 22),
          ("pos622MbsModule", 21),
          ("xer20PortGigCopperSPModule", 90),
          ("xer20PortGigFXSPModule", 91),
          ("xer2Port10GigSPModule", 89),
          ("xer4Port10GigSPModule", 88),
          ("xmr20PortGigCopperSPModule", 84),
          ("xmr20PortGigFXSPModule", 85),
          ("xmr20PortGigSPModule", 82),
          ("xmr2Port10GigSPModule", 83),
          ("xmr4Port10GigSPModule", 81))
    )


_SnAgentConfigModuleType_Type.__name__ = "Integer32"
_SnAgentConfigModuleType_Object = MibTableColumn
snAgentConfigModuleType = _SnAgentConfigModuleType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 1, 1, 2),
    _SnAgentConfigModuleType_Type()
)
snAgentConfigModuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentConfigModuleType.setStatus("current")


class _SnAgentConfigModuleRowStatus_Type(Integer32):
    """Custom type snAgentConfigModuleRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnAgentConfigModuleRowStatus_Type.__name__ = "Integer32"
_SnAgentConfigModuleRowStatus_Object = MibTableColumn
snAgentConfigModuleRowStatus = _SnAgentConfigModuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 1, 1, 3),
    _SnAgentConfigModuleRowStatus_Type()
)
snAgentConfigModuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentConfigModuleRowStatus.setStatus("current")
_SnAgentConfigModuleDescription_Type = DisplayString
_SnAgentConfigModuleDescription_Object = MibTableColumn
snAgentConfigModuleDescription = _SnAgentConfigModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 1, 1, 4),
    _SnAgentConfigModuleDescription_Type()
)
snAgentConfigModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModuleDescription.setStatus("current")
_SnAgentConfigModuleOperStatus_Type = DisplayString
_SnAgentConfigModuleOperStatus_Object = MibTableColumn
snAgentConfigModuleOperStatus = _SnAgentConfigModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 1, 1, 5),
    _SnAgentConfigModuleOperStatus_Type()
)
snAgentConfigModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModuleOperStatus.setStatus("current")
_SnAgentConfigModuleSerialNumber_Type = DisplayString
_SnAgentConfigModuleSerialNumber_Object = MibTableColumn
snAgentConfigModuleSerialNumber = _SnAgentConfigModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 1, 1, 6),
    _SnAgentConfigModuleSerialNumber_Type()
)
snAgentConfigModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModuleSerialNumber.setStatus("current")
_SnAgentConfigModuleNumberOfPorts_Type = Integer32
_SnAgentConfigModuleNumberOfPorts_Object = MibTableColumn
snAgentConfigModuleNumberOfPorts = _SnAgentConfigModuleNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 1, 1, 7),
    _SnAgentConfigModuleNumberOfPorts_Type()
)
snAgentConfigModuleNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModuleNumberOfPorts.setStatus("current")


class _SnAgentConfigModuleMgmtModuleType_Type(Integer32):
    """Custom type snAgentConfigModuleMgmtModuleType based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("fastIronSXRManagementModule", 16),
          ("fastIronSuperXManagementModule", 15),
          ("fastIronV6SXRManagementModule", 18),
          ("fastIronV6SuperXManagementModule", 17),
          ("fesXStackManagementModule", 12),
          ("fgsStackManagementModule", 13),
          ("jetcoreStackManagementModule", 9),
          ("m1ManagementModule", 4),
          ("m2ManagementModule", 5),
          ("m3ManagementModule", 6),
          ("m4ManagementModule", 7),
          ("m5ManagementModule", 8),
          ("muchoManagementModule", 10),
          ("niCesManagementModule", 14),
          ("nonManagementModule", 2),
          ("other", 1),
          ("rottWeilerManagementModule", 11),
          ("unknownManagementModule", 3))
    )


_SnAgentConfigModuleMgmtModuleType_Type.__name__ = "Integer32"
_SnAgentConfigModuleMgmtModuleType_Object = MibTableColumn
snAgentConfigModuleMgmtModuleType = _SnAgentConfigModuleMgmtModuleType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 1, 1, 8),
    _SnAgentConfigModuleMgmtModuleType_Type()
)
snAgentConfigModuleMgmtModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModuleMgmtModuleType.setStatus("current")
_SnAgentConfigModuleNumberOfCpus_Type = Integer32
_SnAgentConfigModuleNumberOfCpus_Object = MibTableColumn
snAgentConfigModuleNumberOfCpus = _SnAgentConfigModuleNumberOfCpus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 1, 1, 9),
    _SnAgentConfigModuleNumberOfCpus_Type()
)
snAgentConfigModuleNumberOfCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModuleNumberOfCpus.setStatus("current")
_SnAgentConfigModule2Table_Object = MibTable
snAgentConfigModule2Table = _SnAgentConfigModule2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    snAgentConfigModule2Table.setStatus("current")
_SnAgentConfigModule2Entry_Object = MibTableRow
snAgentConfigModule2Entry = _SnAgentConfigModule2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2, 1)
)
snAgentConfigModule2Entry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentConfigModule2Unit"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentConfigModule2Slot"),
)
if mibBuilder.loadTexts:
    snAgentConfigModule2Entry.setStatus("current")
_SnAgentConfigModule2Unit_Type = Integer32
_SnAgentConfigModule2Unit_Object = MibTableColumn
snAgentConfigModule2Unit = _SnAgentConfigModule2Unit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2, 1, 1),
    _SnAgentConfigModule2Unit_Type()
)
snAgentConfigModule2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModule2Unit.setStatus("current")
_SnAgentConfigModule2Slot_Type = Integer32
_SnAgentConfigModule2Slot_Object = MibTableColumn
snAgentConfigModule2Slot = _SnAgentConfigModule2Slot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2, 1, 2),
    _SnAgentConfigModule2Slot_Type()
)
snAgentConfigModule2Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModule2Slot.setStatus("current")


class _SnAgentConfigModule2Type_Type(Integer32):
    """Custom type snAgentConfigModule2Type based on Integer32"""
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
              64,
              65,
              66,
              67,
              68,
              69,
              74,
              80,
              81,
              112,
              113,
              114,
              144,
              145,
              152,
              153,
              154,
              155,
              160,
              161,
              168,
              169,
              176,
              177,
              180,
              181,
              184,
              185,
              192,
              195,
              196,
              197,
              198,
              200,
              201,
              202,
              206,
              207,
              208,
              209,
              212,
              214,
              2016,
              2017,
              2020,
              2021,
              2024,
              2032,
              2033,
              2036,
              2037,
              2040,
              2055,
              2056,
              2057,
              2132,
              2133,
              2134,
              2135,
              2136,
              2137,
              2138,
              2139,
              2140,
              2141,
              2142,
              2208,
              2209,
              2220,
              2224,
              2225,
              2227,
              2228,
              2229,
              2233,
              2234,
              2235,
              2236,
              2240,
              2241,
              2244,
              2245,
              2246,
              2248,
              2249)
        )
    )
    namedValues = NamedValues(
        *(("bi0PortGigM4ManagementModule", 38),
          ("bi0PortManagementModule", 20),
          ("bi0PortWSMManagementModule", 39),
          ("bi0PortWSMModule", 41),
          ("bi12PortGigCopper2PortGigFiber", 15),
          ("bi12PortGigCopper2PortGigFiberManagement", 9),
          ("bi16Port100FXModule", 12),
          ("bi16PortCopperManagementModule", 2),
          ("bi1Port10GigModule", 47),
          ("bi24Port100FXModule", 19),
          ("bi24PortCopperModule", 10),
          ("bi2Port10GigModule", 207),
          ("bi2PortGigCopperManagementModule", 34),
          ("bi2PortGigCopperModule", 24),
          ("bi2PortGigM4ManagementModule", 37),
          ("bi2PortGigManagementModule", 18),
          ("bi2PortGigModule", 23),
          ("bi4PortGigCopperManagementModule", 33),
          ("bi4PortGigM4ManagementModule", 36),
          ("bi4PortGigManagementModule", 1),
          ("bi4PortGigModule", 3),
          ("bi4PortGigNPAModule", 44),
          ("bi8Port100FXModule", 13),
          ("bi8PortGigCopperManagementModule", 6),
          ("bi8PortGigCopperModule", 14),
          ("bi8PortGigM4ManagementModule", 35),
          ("bi8PortGigManagementModule", 0),
          ("bi8PortGigModule", 8),
          ("biAtm2Port155MbsModule", 45),
          ("biAtm4Port155MbsModule", 46),
          ("biFiJc16PortGigIgcModule", 200),
          ("biFiJc24Port100fxIpcModule", 206),
          ("biFiJc48ePort100fxIpcModule", 195),
          ("biFiJc48tPort100fxIpcModule", 196),
          ("biFiJc8PortGigIgcModule", 198),
          ("biFiJc8PortGigM4ManagementModule", 197),
          ("biJc16PortGigCopperIgcModule", 202),
          ("biJc24PortCopperIpc4GigIgcModule", 201),
          ("biJc24PortIpcRJ45PoeModule", 212),
          ("biJc2PortGigIgcM4ManagementModule", 214),
          ("biJc48ePortRJ45OmpModule", 209),
          ("biJc48tPortRJ21OmpModule", 208),
          ("biPos2Port2488MbsModule", 40),
          ("fcx624SBaseModule", 176),
          ("fcx624SFBaseModule", 192),
          ("fcx624SPoeBaseModule", 180),
          ("fcx648SBaseModule", 177),
          ("fcx648SPoeBaseModule", 181),
          ("fcxCx42Port16gModule", 185),
          ("fcxXfp2Port10gModule", 184),
          ("fdryFcx624BaseModule", 2208),
          ("fdryFcx648BaseModule", 2209),
          ("fdryFcxSfpPlus4Port10gModule", 2220),
          ("fdryIcx6430612CBaseModule", 2137),
          ("fdryIcx6430624BaseModule", 2016),
          ("fdryIcx6430624PoeBaseModule", 2020),
          ("fdryIcx6430648BaseModule", 2017),
          ("fdryIcx6430648PoeBaseModule", 2021),
          ("fdryIcx6430Copper2Port2gModule", 2138),
          ("fdryIcx6430sfp2Port2gModule", 2139),
          ("fdryIcx6430sfp4Port4gModule", 2024),
          ("fdryIcx6450612CPDBaseModule", 2140),
          ("fdryIcx6450624BaseModule", 2032),
          ("fdryIcx6450624PoeBaseModule", 2036),
          ("fdryIcx6450648BaseModule", 2033),
          ("fdryIcx6450648PoeBaseModule", 2037),
          ("fdryIcx6450Copper2Port2gModule", 2141),
          ("fdryIcx6450sfp2Port2gModule", 2142),
          ("fdryIcx6450sfp4Port40gModule", 2040),
          ("fdryIcx6610624BaseModule", 2240),
          ("fdryIcx6610624FBaseModule", 2246),
          ("fdryIcx6610624PoeBaseModule", 2244),
          ("fdryIcx6610648BaseModule", 2241),
          ("fdryIcx6610648PoeBaseModule", 2245),
          ("fdryIcx6610DualMode8PortModule", 2248),
          ("fdryIcx6610Qsfp10Port160gModule", 2249),
          ("fdryIcx665056BaseModule", 2055),
          ("fdryIcx6650sfp4Port40gModule", 2056),
          ("fdryIcx6650sfp8Port10gModule", 2057),
          ("fdryIcx7400copper4Port40gModule", 2234),
          ("fdryIcx7400qsfpplus1Port40gModule", 2236),
          ("fdryIcx7400sfp4Port4gModule", 2235),
          ("fdryIcx7400sfpplus4Port40gModule", 2233),
          ("fdryIcx7450624BaseModule", 2224),
          ("fdryIcx7450624PoeBaseModule", 2228),
          ("fdryIcx7450648BaseModule", 2225),
          ("fdryIcx7450648FBaseModule", 2227),
          ("fdryIcx7450648PoeBaseModule", 2229),
          ("fdryIcx775026QBaseModule", 2134),
          ("fdryIcx775048CBaseModule", 2136),
          ("fdryIcx775048FBaseModule", 2135),
          ("fdryIcx77506Q6port40gModule", 2133),
          ("fdryIcx7750QSFP6port40gModule", 2132),
          ("fes12GigCopperAndGigFiberModule", 51),
          ("fes2402Module", 49),
          ("fes4802Module", 48),
          ("fes9604Module", 50),
          ("fesx24Gig1TenGigModule", 54),
          ("fesx24Gig2TenGigModule", 53),
          ("fesx24GigFiber1TenGigModule", 114),
          ("fesx24GigFiber2TenGigModule", 113),
          ("fesx24GigFiberGigCopperModule", 112),
          ("fesx24GigModule", 52),
          ("fesx48Gig1TenGigModule", 57),
          ("fesx48Gig2TenGigModule", 56),
          ("fesx48GigModule", 55),
          ("fgs24PortManagementModule", 144),
          ("fgs48PortManagementModule", 145),
          ("fgsCx42Port10gModule", 153),
          ("fgsXfp1Cx41Port10gModule", 154),
          ("fgsXfp2Port10gModule", 152),
          ("fgsXpf1Port10gModule", 155),
          ("fi24PortCopperModule", 11),
          ("fi2PortGigCopperManagementModule", 32),
          ("fi2PortGigManagementModule", 4),
          ("fi2PortGigModule", 25),
          ("fi4PortGigCopperManagementModule", 31),
          ("fi4PortGigManagementModule", 5),
          ("fi4PortGigModule", 26),
          ("fi8PortGigCopperManagementModule", 29),
          ("fi8PortGigCopperModule", 28),
          ("fi8PortGigManagementModule", 7),
          ("fi8PortGigModule", 27),
          ("fls24PortCopperBaseModule", 160),
          ("fls48PortCopperBaseModule", 161),
          ("flsCx41Port10gModule", 169),
          ("flsXfp1Port10gModule", 168),
          ("ni4802", 43),
          ("niPos2Port2488MbsModule", 42),
          ("pos155Mbs2PModule", 30),
          ("pos155MbsModule", 22),
          ("pos622MbsModule", 21),
          ("superx12ComboPortManagement2Module", 74),
          ("superx12ComboPortManagementModule", 64),
          ("superx24Port100tx1PortGigFiberModule", 69),
          ("superx24PortGigCopperModule", 66),
          ("superx24PortGigFiberModule", 67),
          ("superx2PortTenGigLanWanModule", 68),
          ("superx2PortTenGigModule", 65),
          ("superxR2PortTenGigManagementModule", 80),
          ("superxRManagementModule", 81))
    )


_SnAgentConfigModule2Type_Type.__name__ = "Integer32"
_SnAgentConfigModule2Type_Object = MibTableColumn
snAgentConfigModule2Type = _SnAgentConfigModule2Type_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2, 1, 3),
    _SnAgentConfigModule2Type_Type()
)
snAgentConfigModule2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentConfigModule2Type.setStatus("current")


class _SnAgentConfigModule2RowStatus_Type(Integer32):
    """Custom type snAgentConfigModule2RowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnAgentConfigModule2RowStatus_Type.__name__ = "Integer32"
_SnAgentConfigModule2RowStatus_Object = MibTableColumn
snAgentConfigModule2RowStatus = _SnAgentConfigModule2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2, 1, 4),
    _SnAgentConfigModule2RowStatus_Type()
)
snAgentConfigModule2RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentConfigModule2RowStatus.setStatus("current")
_SnAgentConfigModule2Description_Type = DisplayString
_SnAgentConfigModule2Description_Object = MibTableColumn
snAgentConfigModule2Description = _SnAgentConfigModule2Description_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2, 1, 5),
    _SnAgentConfigModule2Description_Type()
)
snAgentConfigModule2Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModule2Description.setStatus("current")
_SnAgentConfigModule2OperStatus_Type = DisplayString
_SnAgentConfigModule2OperStatus_Object = MibTableColumn
snAgentConfigModule2OperStatus = _SnAgentConfigModule2OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2, 1, 6),
    _SnAgentConfigModule2OperStatus_Type()
)
snAgentConfigModule2OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModule2OperStatus.setStatus("current")
_SnAgentConfigModule2SerialNumber_Type = DisplayString
_SnAgentConfigModule2SerialNumber_Object = MibTableColumn
snAgentConfigModule2SerialNumber = _SnAgentConfigModule2SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2, 1, 7),
    _SnAgentConfigModule2SerialNumber_Type()
)
snAgentConfigModule2SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModule2SerialNumber.setStatus("current")
_SnAgentConfigModule2NumberOfPorts_Type = Integer32
_SnAgentConfigModule2NumberOfPorts_Object = MibTableColumn
snAgentConfigModule2NumberOfPorts = _SnAgentConfigModule2NumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2, 1, 8),
    _SnAgentConfigModule2NumberOfPorts_Type()
)
snAgentConfigModule2NumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModule2NumberOfPorts.setStatus("current")


class _SnAgentConfigModule2MgmtModuleType_Type(Integer32):
    """Custom type snAgentConfigModule2MgmtModuleType based on Integer32"""
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
        *(("fesXStackManagementModule", 12),
          ("fgsStackManagementModule", 13),
          ("jetcoreStackManagementModule", 9),
          ("m1ManagementModule", 4),
          ("m2ManagementModule", 5),
          ("m3ManagementModule", 6),
          ("m4ManagementModule", 7),
          ("m5ManagementModule", 8),
          ("muchoManagementModule", 10),
          ("nonManagementModule", 2),
          ("other", 1),
          ("rottWeilerManagementModule", 11),
          ("unknownManagementModule", 3))
    )


_SnAgentConfigModule2MgmtModuleType_Type.__name__ = "Integer32"
_SnAgentConfigModule2MgmtModuleType_Object = MibTableColumn
snAgentConfigModule2MgmtModuleType = _SnAgentConfigModule2MgmtModuleType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2, 1, 9),
    _SnAgentConfigModule2MgmtModuleType_Type()
)
snAgentConfigModule2MgmtModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModule2MgmtModuleType.setStatus("current")
_SnAgentConfigModule2NumberOfCpus_Type = Integer32
_SnAgentConfigModule2NumberOfCpus_Object = MibTableColumn
snAgentConfigModule2NumberOfCpus = _SnAgentConfigModule2NumberOfCpus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 8, 2, 1, 10),
    _SnAgentConfigModule2NumberOfCpus_Type()
)
snAgentConfigModule2NumberOfCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModule2NumberOfCpus.setStatus("current")
_SnAgentUser_ObjectIdentity = ObjectIdentity
snAgentUser = _SnAgentUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 9)
)
_SnAgentUserGbl_ObjectIdentity = ObjectIdentity
snAgentUserGbl = _SnAgentUserGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 9, 1)
)
_SnAgentUserMaxAccnt_Type = Integer32
_SnAgentUserMaxAccnt_Object = MibScalar
snAgentUserMaxAccnt = _SnAgentUserMaxAccnt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 9, 1, 1),
    _SnAgentUserMaxAccnt_Type()
)
snAgentUserMaxAccnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentUserMaxAccnt.setStatus("current")
_SnAgentUserAccntTable_Object = MibTable
snAgentUserAccntTable = _SnAgentUserAccntTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    snAgentUserAccntTable.setStatus("current")
_SnAgentUserAccntEntry_Object = MibTableRow
snAgentUserAccntEntry = _SnAgentUserAccntEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 9, 2, 1)
)
snAgentUserAccntEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentUserAccntName"),
)
if mibBuilder.loadTexts:
    snAgentUserAccntEntry.setStatus("current")


class _SnAgentUserAccntName_Type(DisplayString):
    """Custom type snAgentUserAccntName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SnAgentUserAccntName_Type.__name__ = "DisplayString"
_SnAgentUserAccntName_Object = MibTableColumn
snAgentUserAccntName = _SnAgentUserAccntName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 9, 2, 1, 1),
    _SnAgentUserAccntName_Type()
)
snAgentUserAccntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentUserAccntName.setStatus("current")


class _SnAgentUserAccntPassword_Type(DisplayString):
    """Custom type snAgentUserAccntPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnAgentUserAccntPassword_Type.__name__ = "DisplayString"
_SnAgentUserAccntPassword_Object = MibTableColumn
snAgentUserAccntPassword = _SnAgentUserAccntPassword_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 9, 2, 1, 2),
    _SnAgentUserAccntPassword_Type()
)
snAgentUserAccntPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentUserAccntPassword.setStatus("current")
_SnAgentUserAccntEncryptCode_Type = Integer32
_SnAgentUserAccntEncryptCode_Object = MibTableColumn
snAgentUserAccntEncryptCode = _SnAgentUserAccntEncryptCode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 9, 2, 1, 3),
    _SnAgentUserAccntEncryptCode_Type()
)
snAgentUserAccntEncryptCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentUserAccntEncryptCode.setStatus("current")
_SnAgentUserAccntPrivilege_Type = Integer32
_SnAgentUserAccntPrivilege_Object = MibTableColumn
snAgentUserAccntPrivilege = _SnAgentUserAccntPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 9, 2, 1, 4),
    _SnAgentUserAccntPrivilege_Type()
)
snAgentUserAccntPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentUserAccntPrivilege.setStatus("current")


class _SnAgentUserAccntRowStatus_Type(Integer32):
    """Custom type snAgentUserAccntRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("modify", 5),
          ("other", 1),
          ("valid", 2))
    )


_SnAgentUserAccntRowStatus_Type.__name__ = "Integer32"
_SnAgentUserAccntRowStatus_Object = MibTableColumn
snAgentUserAccntRowStatus = _SnAgentUserAccntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 9, 2, 1, 5),
    _SnAgentUserAccntRowStatus_Type()
)
snAgentUserAccntRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentUserAccntRowStatus.setStatus("current")
_SnAgentRedundant_ObjectIdentity = ObjectIdentity
snAgentRedundant = _SnAgentRedundant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 10)
)
_SnAgentRedunGbl_ObjectIdentity = ObjectIdentity
snAgentRedunGbl = _SnAgentRedunGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 10, 1)
)


class _SnAgentRedunActiveMgmtMod_Type(Integer32):
    """Custom type snAgentRedunActiveMgmtMod based on Integer32"""
    defaultValue = 0


_SnAgentRedunActiveMgmtMod_Object = MibScalar
snAgentRedunActiveMgmtMod = _SnAgentRedunActiveMgmtMod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 10, 1, 1),
    _SnAgentRedunActiveMgmtMod_Type()
)
snAgentRedunActiveMgmtMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentRedunActiveMgmtMod.setStatus("current")
_SnAgentRedunSyncConfig_Type = Integer32
_SnAgentRedunSyncConfig_Object = MibScalar
snAgentRedunSyncConfig = _SnAgentRedunSyncConfig_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 10, 1, 2),
    _SnAgentRedunSyncConfig_Type()
)
snAgentRedunSyncConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentRedunSyncConfig.setStatus("current")


class _SnAgentRedunBkupCopyBootCode_Type(Integer32):
    """Custom type snAgentRedunBkupCopyBootCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgentRedunBkupCopyBootCode_Type.__name__ = "Integer32"
_SnAgentRedunBkupCopyBootCode_Object = MibScalar
snAgentRedunBkupCopyBootCode = _SnAgentRedunBkupCopyBootCode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 10, 1, 3),
    _SnAgentRedunBkupCopyBootCode_Type()
)
snAgentRedunBkupCopyBootCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentRedunBkupCopyBootCode.setStatus("current")


class _SnAgentEnableMgmtModRedunStateChangeTrap_Type(Integer32):
    """Custom type snAgentEnableMgmtModRedunStateChangeTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgentEnableMgmtModRedunStateChangeTrap_Type.__name__ = "Integer32"
_SnAgentEnableMgmtModRedunStateChangeTrap_Object = MibScalar
snAgentEnableMgmtModRedunStateChangeTrap = _SnAgentEnableMgmtModRedunStateChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 10, 1, 4),
    _SnAgentEnableMgmtModRedunStateChangeTrap_Type()
)
snAgentEnableMgmtModRedunStateChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentEnableMgmtModRedunStateChangeTrap.setStatus("current")


class _SnAgentRedunBkupBootLoad_Type(Integer32):
    """Custom type snAgentRedunBkupBootLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              17,
              20)
        )
    )
    namedValues = NamedValues(
        *(("downloadBackup", 20),
          ("normal", 1),
          ("operationError", 17))
    )


_SnAgentRedunBkupBootLoad_Type.__name__ = "Integer32"
_SnAgentRedunBkupBootLoad_Object = MibScalar
snAgentRedunBkupBootLoad = _SnAgentRedunBkupBootLoad_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 10, 1, 5),
    _SnAgentRedunBkupBootLoad_Type()
)
snAgentRedunBkupBootLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentRedunBkupBootLoad.setStatus("current")


class _SnAgentRedunSwitchOver_Type(Integer32):
    """Custom type snAgentRedunSwitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_SnAgentRedunSwitchOver_Type.__name__ = "Integer32"
_SnAgentRedunSwitchOver_Object = MibScalar
snAgentRedunSwitchOver = _SnAgentRedunSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 10, 1, 6),
    _SnAgentRedunSwitchOver_Type()
)
snAgentRedunSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentRedunSwitchOver.setStatus("current")
_SnAgentCpu_ObjectIdentity = ObjectIdentity
snAgentCpu = _SnAgentCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11)
)
_SnAgentCpuUtilTable_Object = MibTable
snAgentCpuUtilTable = _SnAgentCpuUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    snAgentCpuUtilTable.setStatus("current")
_SnAgentCpuUtilEntry_Object = MibTableRow
snAgentCpuUtilEntry = _SnAgentCpuUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 1, 1)
)
snAgentCpuUtilEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentCpuUtilSlotNum"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentCpuUtilCpuId"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentCpuUtilInterval"),
)
if mibBuilder.loadTexts:
    snAgentCpuUtilEntry.setStatus("current")
_SnAgentCpuUtilSlotNum_Type = Integer32
_SnAgentCpuUtilSlotNum_Object = MibTableColumn
snAgentCpuUtilSlotNum = _SnAgentCpuUtilSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 1, 1, 1),
    _SnAgentCpuUtilSlotNum_Type()
)
snAgentCpuUtilSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentCpuUtilSlotNum.setStatus("current")
_SnAgentCpuUtilCpuId_Type = Integer32
_SnAgentCpuUtilCpuId_Object = MibTableColumn
snAgentCpuUtilCpuId = _SnAgentCpuUtilCpuId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 1, 1, 2),
    _SnAgentCpuUtilCpuId_Type()
)
snAgentCpuUtilCpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentCpuUtilCpuId.setStatus("current")
_SnAgentCpuUtilInterval_Type = Integer32
_SnAgentCpuUtilInterval_Object = MibTableColumn
snAgentCpuUtilInterval = _SnAgentCpuUtilInterval_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 1, 1, 3),
    _SnAgentCpuUtilInterval_Type()
)
snAgentCpuUtilInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentCpuUtilInterval.setStatus("current")
_SnAgentCpuUtilValue_Type = Gauge32
_SnAgentCpuUtilValue_Object = MibTableColumn
snAgentCpuUtilValue = _SnAgentCpuUtilValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 1, 1, 4),
    _SnAgentCpuUtilValue_Type()
)
snAgentCpuUtilValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentCpuUtilValue.setStatus("deprecated")
_SnAgentCpuUtilPercent_Type = Gauge32
_SnAgentCpuUtilPercent_Object = MibTableColumn
snAgentCpuUtilPercent = _SnAgentCpuUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 1, 1, 5),
    _SnAgentCpuUtilPercent_Type()
)
snAgentCpuUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentCpuUtilPercent.setStatus("current")
_SnAgentCpuUtil100thPercent_Type = Gauge32
_SnAgentCpuUtil100thPercent_Object = MibTableColumn
snAgentCpuUtil100thPercent = _SnAgentCpuUtil100thPercent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 1, 1, 6),
    _SnAgentCpuUtil100thPercent_Type()
)
snAgentCpuUtil100thPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentCpuUtil100thPercent.setStatus("current")
_SnCpuProcessTable_Object = MibTable
snCpuProcessTable = _SnCpuProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    snCpuProcessTable.setStatus("current")
_SnCpuProcessEntry_Object = MibTableRow
snCpuProcessEntry = _SnCpuProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 2, 1)
)
snCpuProcessEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snCpuProcessName"),
)
if mibBuilder.loadTexts:
    snCpuProcessEntry.setStatus("current")


class _SnCpuProcessName_Type(DisplayString):
    """Custom type snCpuProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SnCpuProcessName_Type.__name__ = "DisplayString"
_SnCpuProcessName_Object = MibTableColumn
snCpuProcessName = _SnCpuProcessName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 2, 1, 1),
    _SnCpuProcessName_Type()
)
snCpuProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCpuProcessName.setStatus("current")
_SnCpuProcess5SecUtil_Type = Gauge32
_SnCpuProcess5SecUtil_Object = MibTableColumn
snCpuProcess5SecUtil = _SnCpuProcess5SecUtil_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 2, 1, 2),
    _SnCpuProcess5SecUtil_Type()
)
snCpuProcess5SecUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCpuProcess5SecUtil.setStatus("current")
_SnCpuProcess1MinUtil_Type = Gauge32
_SnCpuProcess1MinUtil_Object = MibTableColumn
snCpuProcess1MinUtil = _SnCpuProcess1MinUtil_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 2, 1, 3),
    _SnCpuProcess1MinUtil_Type()
)
snCpuProcess1MinUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCpuProcess1MinUtil.setStatus("current")
_SnCpuProcess5MinUtil_Type = Gauge32
_SnCpuProcess5MinUtil_Object = MibTableColumn
snCpuProcess5MinUtil = _SnCpuProcess5MinUtil_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 2, 1, 4),
    _SnCpuProcess5MinUtil_Type()
)
snCpuProcess5MinUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCpuProcess5MinUtil.setStatus("current")
_SnCpuProcess15MinUtil_Type = Gauge32
_SnCpuProcess15MinUtil_Object = MibTableColumn
snCpuProcess15MinUtil = _SnCpuProcess15MinUtil_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 2, 1, 5),
    _SnCpuProcess15MinUtil_Type()
)
snCpuProcess15MinUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCpuProcess15MinUtil.setStatus("current")
_SnCpuProcessRuntime_Type = Counter32
_SnCpuProcessRuntime_Object = MibTableColumn
snCpuProcessRuntime = _SnCpuProcessRuntime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 2, 1, 6),
    _SnCpuProcessRuntime_Type()
)
snCpuProcessRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCpuProcessRuntime.setStatus("current")
_SnAgentCpuProcessEnable_Type = EnabledStatus
_SnAgentCpuProcessEnable_Object = MibScalar
snAgentCpuProcessEnable = _SnAgentCpuProcessEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 11, 3),
    _SnAgentCpuProcessEnable_Type()
)
snAgentCpuProcessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentCpuProcessEnable.setStatus("current")
_SnAgentHw_ObjectIdentity = ObjectIdentity
snAgentHw = _SnAgentHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12)
)
_SnAgentHwICBMCounterTable_Object = MibTable
snAgentHwICBMCounterTable = _SnAgentHwICBMCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    snAgentHwICBMCounterTable.setStatus("current")
_SnAgentHwICBMCounterEntry_Object = MibTableRow
snAgentHwICBMCounterEntry = _SnAgentHwICBMCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 1, 1)
)
snAgentHwICBMCounterEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentHwICBMCounterSlot"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentHwICBMCounterDMA"),
)
if mibBuilder.loadTexts:
    snAgentHwICBMCounterEntry.setStatus("current")
_SnAgentHwICBMCounterSlot_Type = Unsigned32
_SnAgentHwICBMCounterSlot_Object = MibTableColumn
snAgentHwICBMCounterSlot = _SnAgentHwICBMCounterSlot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 1, 1, 1),
    _SnAgentHwICBMCounterSlot_Type()
)
snAgentHwICBMCounterSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentHwICBMCounterSlot.setStatus("current")
_SnAgentHwICBMCounterDMA_Type = Unsigned32
_SnAgentHwICBMCounterDMA_Object = MibTableColumn
snAgentHwICBMCounterDMA = _SnAgentHwICBMCounterDMA_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 1, 1, 2),
    _SnAgentHwICBMCounterDMA_Type()
)
snAgentHwICBMCounterDMA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentHwICBMCounterDMA.setStatus("current")
_SnAgentHwICBMCounterFreeDepth_Type = Gauge32
_SnAgentHwICBMCounterFreeDepth_Object = MibTableColumn
snAgentHwICBMCounterFreeDepth = _SnAgentHwICBMCounterFreeDepth_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 1, 1, 3),
    _SnAgentHwICBMCounterFreeDepth_Type()
)
snAgentHwICBMCounterFreeDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentHwICBMCounterFreeDepth.setStatus("current")
_SnAgentHwICBMCounterWriteDrop_Type = Counter32
_SnAgentHwICBMCounterWriteDrop_Object = MibTableColumn
snAgentHwICBMCounterWriteDrop = _SnAgentHwICBMCounterWriteDrop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 1, 1, 4),
    _SnAgentHwICBMCounterWriteDrop_Type()
)
snAgentHwICBMCounterWriteDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentHwICBMCounterWriteDrop.setStatus("current")
_SnAgentHwICBMCounterWriteInput_Type = Counter32
_SnAgentHwICBMCounterWriteInput_Object = MibTableColumn
snAgentHwICBMCounterWriteInput = _SnAgentHwICBMCounterWriteInput_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 1, 1, 5),
    _SnAgentHwICBMCounterWriteInput_Type()
)
snAgentHwICBMCounterWriteInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentHwICBMCounterWriteInput.setStatus("current")
_SnAgentHwICBMCounterWriteOutput_Type = Counter32
_SnAgentHwICBMCounterWriteOutput_Object = MibTableColumn
snAgentHwICBMCounterWriteOutput = _SnAgentHwICBMCounterWriteOutput_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 1, 1, 6),
    _SnAgentHwICBMCounterWriteOutput_Type()
)
snAgentHwICBMCounterWriteOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentHwICBMCounterWriteOutput.setStatus("current")
_SnAgentHwICBMCounterReadInput_Type = Counter32
_SnAgentHwICBMCounterReadInput_Object = MibTableColumn
snAgentHwICBMCounterReadInput = _SnAgentHwICBMCounterReadInput_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 1, 1, 7),
    _SnAgentHwICBMCounterReadInput_Type()
)
snAgentHwICBMCounterReadInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentHwICBMCounterReadInput.setStatus("current")
_SnAgentHwICBMCounterReadOutput_Type = Counter32
_SnAgentHwICBMCounterReadOutput_Object = MibTableColumn
snAgentHwICBMCounterReadOutput = _SnAgentHwICBMCounterReadOutput_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 1, 1, 8),
    _SnAgentHwICBMCounterReadOutput_Type()
)
snAgentHwICBMCounterReadOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentHwICBMCounterReadOutput.setStatus("current")
_SnCAMIpStatTable_Object = MibTable
snCAMIpStatTable = _SnCAMIpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    snCAMIpStatTable.setStatus("current")
_SnCAMIpStatEntry_Object = MibTableRow
snCAMIpStatEntry = _SnCAMIpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 2, 1)
)
snCAMIpStatEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snCAMIpStatIfIndex"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snCAMIpStatLevel"),
)
if mibBuilder.loadTexts:
    snCAMIpStatEntry.setStatus("current")
_SnCAMIpStatIfIndex_Type = Unsigned32
_SnCAMIpStatIfIndex_Object = MibTableColumn
snCAMIpStatIfIndex = _SnCAMIpStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 2, 1, 1),
    _SnCAMIpStatIfIndex_Type()
)
snCAMIpStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCAMIpStatIfIndex.setStatus("current")
_SnCAMIpStatLevel_Type = Unsigned32
_SnCAMIpStatLevel_Object = MibTableColumn
snCAMIpStatLevel = _SnCAMIpStatLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 2, 1, 2),
    _SnCAMIpStatLevel_Type()
)
snCAMIpStatLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCAMIpStatLevel.setStatus("current")
_SnCAMIpStatFreeEntries_Type = Unsigned32
_SnCAMIpStatFreeEntries_Object = MibTableColumn
snCAMIpStatFreeEntries = _SnCAMIpStatFreeEntries_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 2, 1, 3),
    _SnCAMIpStatFreeEntries_Type()
)
snCAMIpStatFreeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCAMIpStatFreeEntries.setStatus("current")
_SnCAMIpStatTotalEntries_Type = Unsigned32
_SnCAMIpStatTotalEntries_Object = MibTableColumn
snCAMIpStatTotalEntries = _SnCAMIpStatTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 2, 1, 4),
    _SnCAMIpStatTotalEntries_Type()
)
snCAMIpStatTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCAMIpStatTotalEntries.setStatus("current")
_SnCAMStatTable_Object = MibTable
snCAMStatTable = _SnCAMStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3)
)
if mibBuilder.loadTexts:
    snCAMStatTable.setStatus("current")
_SnCAMStatEntry_Object = MibTableRow
snCAMStatEntry = _SnCAMStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1)
)
snCAMStatEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snCamStatDMAIdNumber"),
)
if mibBuilder.loadTexts:
    snCAMStatEntry.setStatus("current")
_SnCamStatDMAIdNumber_Type = Unsigned32
_SnCamStatDMAIdNumber_Object = MibTableColumn
snCamStatDMAIdNumber = _SnCamStatDMAIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 1),
    _SnCamStatDMAIdNumber_Type()
)
snCamStatDMAIdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatDMAIdNumber.setStatus("current")
_SnCamStatDMAMasterNumber_Type = Unsigned32
_SnCamStatDMAMasterNumber_Object = MibTableColumn
snCamStatDMAMasterNumber = _SnCamStatDMAMasterNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 2),
    _SnCamStatDMAMasterNumber_Type()
)
snCamStatDMAMasterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatDMAMasterNumber.setStatus("current")
_SnCamStatFreePool0Entries_Type = Unsigned32
_SnCamStatFreePool0Entries_Object = MibTableColumn
snCamStatFreePool0Entries = _SnCamStatFreePool0Entries_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 3),
    _SnCamStatFreePool0Entries_Type()
)
snCamStatFreePool0Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatFreePool0Entries.setStatus("current")
_SnCamStatFreePool1Entries_Type = Unsigned32
_SnCamStatFreePool1Entries_Object = MibTableColumn
snCamStatFreePool1Entries = _SnCamStatFreePool1Entries_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 4),
    _SnCamStatFreePool1Entries_Type()
)
snCamStatFreePool1Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatFreePool1Entries.setStatus("current")
_SnCamStatFreePool2Entries_Type = Unsigned32
_SnCamStatFreePool2Entries_Object = MibTableColumn
snCamStatFreePool2Entries = _SnCamStatFreePool2Entries_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 5),
    _SnCamStatFreePool2Entries_Type()
)
snCamStatFreePool2Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatFreePool2Entries.setStatus("current")
_SnCamStatFreePool3Entries_Type = Unsigned32
_SnCamStatFreePool3Entries_Object = MibTableColumn
snCamStatFreePool3Entries = _SnCamStatFreePool3Entries_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 6),
    _SnCamStatFreePool3Entries_Type()
)
snCamStatFreePool3Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatFreePool3Entries.setStatus("current")
_SnCamStatFreeL2Entries_Type = Unsigned32
_SnCamStatFreeL2Entries_Object = MibTableColumn
snCamStatFreeL2Entries = _SnCamStatFreeL2Entries_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 7),
    _SnCamStatFreeL2Entries_Type()
)
snCamStatFreeL2Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatFreeL2Entries.setStatus("current")
_SnCamStatFreeL2LowestSection_Type = Unsigned32
_SnCamStatFreeL2LowestSection_Object = MibTableColumn
snCamStatFreeL2LowestSection = _SnCamStatFreeL2LowestSection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 8),
    _SnCamStatFreeL2LowestSection_Type()
)
snCamStatFreeL2LowestSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatFreeL2LowestSection.setStatus("current")
_SnCamStatHostLookupCount_Type = Counter32
_SnCamStatHostLookupCount_Object = MibTableColumn
snCamStatHostLookupCount = _SnCamStatHostLookupCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 9),
    _SnCamStatHostLookupCount_Type()
)
snCamStatHostLookupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatHostLookupCount.setStatus("current")
_SnCamStatRouteLookupCount_Type = Counter32
_SnCamStatRouteLookupCount_Object = MibTableColumn
snCamStatRouteLookupCount = _SnCamStatRouteLookupCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 10),
    _SnCamStatRouteLookupCount_Type()
)
snCamStatRouteLookupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatRouteLookupCount.setStatus("current")
_SnCamStatLevel1_Type = Unsigned32
_SnCamStatLevel1_Object = MibTableColumn
snCamStatLevel1 = _SnCamStatLevel1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 11),
    _SnCamStatLevel1_Type()
)
snCamStatLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatLevel1.setStatus("current")
_SnCamStatLevel2_Type = Unsigned32
_SnCamStatLevel2_Object = MibTableColumn
snCamStatLevel2 = _SnCamStatLevel2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 12),
    _SnCamStatLevel2_Type()
)
snCamStatLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatLevel2.setStatus("current")
_SnCamStatLevel3_Type = Unsigned32
_SnCamStatLevel3_Object = MibTableColumn
snCamStatLevel3 = _SnCamStatLevel3_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 13),
    _SnCamStatLevel3_Type()
)
snCamStatLevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatLevel3.setStatus("current")
_SnCamStatMacFailCount_Type = Counter32
_SnCamStatMacFailCount_Object = MibTableColumn
snCamStatMacFailCount = _SnCamStatMacFailCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 14),
    _SnCamStatMacFailCount_Type()
)
snCamStatMacFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatMacFailCount.setStatus("current")
_SnCamStatIPRouteFailCount_Type = Counter32
_SnCamStatIPRouteFailCount_Object = MibTableColumn
snCamStatIPRouteFailCount = _SnCamStatIPRouteFailCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 15),
    _SnCamStatIPRouteFailCount_Type()
)
snCamStatIPRouteFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatIPRouteFailCount.setStatus("current")
_SnCamStatIPSessionFailCount_Type = Counter32
_SnCamStatIPSessionFailCount_Object = MibTableColumn
snCamStatIPSessionFailCount = _SnCamStatIPSessionFailCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 16),
    _SnCamStatIPSessionFailCount_Type()
)
snCamStatIPSessionFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatIPSessionFailCount.setStatus("current")
_SnCamStatIPMCastFailCount_Type = Counter32
_SnCamStatIPMCastFailCount_Object = MibTableColumn
snCamStatIPMCastFailCount = _SnCamStatIPMCastFailCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 17),
    _SnCamStatIPMCastFailCount_Type()
)
snCamStatIPMCastFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatIPMCastFailCount.setStatus("current")
_SnCamStatL2SessionFailCount_Type = Counter32
_SnCamStatL2SessionFailCount_Object = MibTableColumn
snCamStatL2SessionFailCount = _SnCamStatL2SessionFailCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 18),
    _SnCamStatL2SessionFailCount_Type()
)
snCamStatL2SessionFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatL2SessionFailCount.setStatus("current")
_SnCamStatAddMACCount_Type = Counter32
_SnCamStatAddMACCount_Object = MibTableColumn
snCamStatAddMACCount = _SnCamStatAddMACCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 19),
    _SnCamStatAddMACCount_Type()
)
snCamStatAddMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatAddMACCount.setStatus("current")
_SnCamStatAddVLANCount_Type = Counter32
_SnCamStatAddVLANCount_Object = MibTableColumn
snCamStatAddVLANCount = _SnCamStatAddVLANCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 20),
    _SnCamStatAddVLANCount_Type()
)
snCamStatAddVLANCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatAddVLANCount.setStatus("current")
_SnCamStatAddIPHostCount_Type = Counter32
_SnCamStatAddIPHostCount_Object = MibTableColumn
snCamStatAddIPHostCount = _SnCamStatAddIPHostCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 21),
    _SnCamStatAddIPHostCount_Type()
)
snCamStatAddIPHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatAddIPHostCount.setStatus("current")
_SnCamStatAddIPRouteCount_Type = Counter32
_SnCamStatAddIPRouteCount_Object = MibTableColumn
snCamStatAddIPRouteCount = _SnCamStatAddIPRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 22),
    _SnCamStatAddIPRouteCount_Type()
)
snCamStatAddIPRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatAddIPRouteCount.setStatus("current")
_SnCamStatAddIPSessionCount_Type = Counter32
_SnCamStatAddIPSessionCount_Object = MibTableColumn
snCamStatAddIPSessionCount = _SnCamStatAddIPSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 23),
    _SnCamStatAddIPSessionCount_Type()
)
snCamStatAddIPSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatAddIPSessionCount.setStatus("current")
_SnCamStatAddIPMCastCount_Type = Counter32
_SnCamStatAddIPMCastCount_Object = MibTableColumn
snCamStatAddIPMCastCount = _SnCamStatAddIPMCastCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 24),
    _SnCamStatAddIPMCastCount_Type()
)
snCamStatAddIPMCastCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatAddIPMCastCount.setStatus("current")
_SnCamStatAddL2SessionCount_Type = Counter32
_SnCamStatAddL2SessionCount_Object = MibTableColumn
snCamStatAddL2SessionCount = _SnCamStatAddL2SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 25),
    _SnCamStatAddL2SessionCount_Type()
)
snCamStatAddL2SessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatAddL2SessionCount.setStatus("current")
_SnCamStatAddIPXCount_Type = Counter32
_SnCamStatAddIPXCount_Object = MibTableColumn
snCamStatAddIPXCount = _SnCamStatAddIPXCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 26),
    _SnCamStatAddIPXCount_Type()
)
snCamStatAddIPXCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatAddIPXCount.setStatus("current")
_SnCamStatDeleteDMACamCount_Type = Counter32
_SnCamStatDeleteDMACamCount_Object = MibTableColumn
snCamStatDeleteDMACamCount = _SnCamStatDeleteDMACamCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 3, 1, 27),
    _SnCamStatDeleteDMACamCount_Type()
)
snCamStatDeleteDMACamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCamStatDeleteDMACamCount.setStatus("current")
_SnAgSystemDRAM_ObjectIdentity = ObjectIdentity
snAgSystemDRAM = _SnAgSystemDRAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 4)
)
_SnAgSystemDRAMUtil_Type = Gauge32
_SnAgSystemDRAMUtil_Object = MibScalar
snAgSystemDRAMUtil = _SnAgSystemDRAMUtil_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 4, 1),
    _SnAgSystemDRAMUtil_Type()
)
snAgSystemDRAMUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDRAMUtil.setStatus("current")
_SnAgSystemDRAMTotal_Type = Integer32
_SnAgSystemDRAMTotal_Object = MibScalar
snAgSystemDRAMTotal = _SnAgSystemDRAMTotal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 4, 2),
    _SnAgSystemDRAMTotal_Type()
)
snAgSystemDRAMTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDRAMTotal.setStatus("current")
_SnAgSystemDRAMFree_Type = Integer32
_SnAgSystemDRAMFree_Object = MibScalar
snAgSystemDRAMFree = _SnAgSystemDRAMFree_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 4, 3),
    _SnAgSystemDRAMFree_Type()
)
snAgSystemDRAMFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDRAMFree.setStatus("current")
_SnAgSystemDRAMForBGP_Type = Integer32
_SnAgSystemDRAMForBGP_Object = MibScalar
snAgSystemDRAMForBGP = _SnAgSystemDRAMForBGP_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 4, 4),
    _SnAgSystemDRAMForBGP_Type()
)
snAgSystemDRAMForBGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDRAMForBGP.setStatus("current")
_SnAgSystemDRAMForOSPF_Type = Integer32
_SnAgSystemDRAMForOSPF_Object = MibScalar
snAgSystemDRAMForOSPF = _SnAgSystemDRAMForOSPF_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 4, 5),
    _SnAgSystemDRAMForOSPF_Type()
)
snAgSystemDRAMForOSPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDRAMForOSPF.setStatus("current")
_SnAgSystemDebug_ObjectIdentity = ObjectIdentity
snAgSystemDebug = _SnAgSystemDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 5)
)
_SnAgSystemDebugTotalIn_Type = Integer32
_SnAgSystemDebugTotalIn_Object = MibScalar
snAgSystemDebugTotalIn = _SnAgSystemDebugTotalIn_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 5, 1),
    _SnAgSystemDebugTotalIn_Type()
)
snAgSystemDebugTotalIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDebugTotalIn.setStatus("current")
_SnAgSystemDebugTotalOut_Type = Integer32
_SnAgSystemDebugTotalOut_Object = MibScalar
snAgSystemDebugTotalOut = _SnAgSystemDebugTotalOut_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 5, 2),
    _SnAgSystemDebugTotalOut_Type()
)
snAgSystemDebugTotalOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDebugTotalOut.setStatus("current")
_SnAgSystemDebugCpuQueueRead_Type = Integer32
_SnAgSystemDebugCpuQueueRead_Object = MibScalar
snAgSystemDebugCpuQueueRead = _SnAgSystemDebugCpuQueueRead_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 5, 3),
    _SnAgSystemDebugCpuQueueRead_Type()
)
snAgSystemDebugCpuQueueRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDebugCpuQueueRead.setStatus("current")
_SnAgSystemDebugDRAMBuffer_Type = Integer32
_SnAgSystemDebugDRAMBuffer_Object = MibScalar
snAgSystemDebugDRAMBuffer = _SnAgSystemDebugDRAMBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 5, 4),
    _SnAgSystemDebugDRAMBuffer_Type()
)
snAgSystemDebugDRAMBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDebugDRAMBuffer.setStatus("current")
_SnAgSystemDebugBMBuffer_Type = Integer32
_SnAgSystemDebugBMBuffer_Object = MibScalar
snAgSystemDebugBMBuffer = _SnAgSystemDebugBMBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 5, 5),
    _SnAgSystemDebugBMBuffer_Type()
)
snAgSystemDebugBMBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDebugBMBuffer.setStatus("current")
_SnAgSystemDebugBMFreeBuffer_Type = Integer32
_SnAgSystemDebugBMFreeBuffer_Object = MibScalar
snAgSystemDebugBMFreeBuffer = _SnAgSystemDebugBMFreeBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 5, 6),
    _SnAgSystemDebugBMFreeBuffer_Type()
)
snAgSystemDebugBMFreeBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDebugBMFreeBuffer.setStatus("current")
_SnAgSystemDebugBMFreeBufferMgmt_Type = Integer32
_SnAgSystemDebugBMFreeBufferMgmt_Object = MibScalar
snAgSystemDebugBMFreeBufferMgmt = _SnAgSystemDebugBMFreeBufferMgmt_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 5, 7),
    _SnAgSystemDebugBMFreeBufferMgmt_Type()
)
snAgSystemDebugBMFreeBufferMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDebugBMFreeBufferMgmt.setStatus("current")
_SnAgSystemDebugIpcGigLock_Type = Integer32
_SnAgSystemDebugIpcGigLock_Object = MibScalar
snAgSystemDebugIpcGigLock = _SnAgSystemDebugIpcGigLock_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 5, 8),
    _SnAgSystemDebugIpcGigLock_Type()
)
snAgSystemDebugIpcGigLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDebugIpcGigLock.setStatus("current")
_SnAgSystemDebugDRAMGetError_Type = Integer32
_SnAgSystemDebugDRAMGetError_Object = MibScalar
snAgSystemDebugDRAMGetError = _SnAgSystemDebugDRAMGetError_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 5, 9),
    _SnAgSystemDebugDRAMGetError_Type()
)
snAgSystemDebugDRAMGetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDebugDRAMGetError.setStatus("current")
_SnAgSystemDebugDRAMToBMCopyFail_Type = Integer32
_SnAgSystemDebugDRAMToBMCopyFail_Object = MibScalar
snAgSystemDebugDRAMToBMCopyFail = _SnAgSystemDebugDRAMToBMCopyFail_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 12, 5, 10),
    _SnAgSystemDebugDRAMToBMCopyFail_Type()
)
snAgSystemDebugDRAMToBMCopyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSystemDebugDRAMToBMCopyFail.setStatus("current")
_SnAgentTemp_ObjectIdentity = ObjectIdentity
snAgentTemp = _SnAgentTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13)
)
_SnAgentTempTable_Object = MibTable
snAgentTempTable = _SnAgentTempTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    snAgentTempTable.setStatus("current")
_SnAgentTempEntry_Object = MibTableRow
snAgentTempEntry = _SnAgentTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 1, 1)
)
snAgentTempEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTempSlotNum"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTempSensorId"),
)
if mibBuilder.loadTexts:
    snAgentTempEntry.setStatus("current")
_SnAgentTempSlotNum_Type = Integer32
_SnAgentTempSlotNum_Object = MibTableColumn
snAgentTempSlotNum = _SnAgentTempSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 1, 1, 1),
    _SnAgentTempSlotNum_Type()
)
snAgentTempSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snAgentTempSlotNum.setStatus("current")
_SnAgentTempSensorId_Type = Integer32
_SnAgentTempSensorId_Object = MibTableColumn
snAgentTempSensorId = _SnAgentTempSensorId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 1, 1, 2),
    _SnAgentTempSensorId_Type()
)
snAgentTempSensorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snAgentTempSensorId.setStatus("current")


class _SnAgentTempSensorDescr_Type(DisplayString):
    """Custom type snAgentTempSensorDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnAgentTempSensorDescr_Type.__name__ = "DisplayString"
_SnAgentTempSensorDescr_Object = MibTableColumn
snAgentTempSensorDescr = _SnAgentTempSensorDescr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 1, 1, 3),
    _SnAgentTempSensorDescr_Type()
)
snAgentTempSensorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTempSensorDescr.setStatus("current")


class _SnAgentTempValue_Type(Integer32):
    """Custom type snAgentTempValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 250),
    )


_SnAgentTempValue_Type.__name__ = "Integer32"
_SnAgentTempValue_Object = MibTableColumn
snAgentTempValue = _SnAgentTempValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 1, 1, 4),
    _SnAgentTempValue_Type()
)
snAgentTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTempValue.setStatus("current")
_SnAgentTempThresholdTable_Object = MibTable
snAgentTempThresholdTable = _SnAgentTempThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    snAgentTempThresholdTable.setStatus("current")
_SnAgentTempThresholdEntry_Object = MibTableRow
snAgentTempThresholdEntry = _SnAgentTempThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 2, 1)
)
snAgentTempThresholdEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTempThresholdModule"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTempThresholdLevel"),
)
if mibBuilder.loadTexts:
    snAgentTempThresholdEntry.setStatus("current")


class _SnAgentTempThresholdModule_Type(Integer32):
    """Custom type snAgentTempThresholdModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mgmtModule", 1),
          ("slaveModule", 2),
          ("switchFabricModule", 3))
    )


_SnAgentTempThresholdModule_Type.__name__ = "Integer32"
_SnAgentTempThresholdModule_Object = MibTableColumn
snAgentTempThresholdModule = _SnAgentTempThresholdModule_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 2, 1, 1),
    _SnAgentTempThresholdModule_Type()
)
snAgentTempThresholdModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snAgentTempThresholdModule.setStatus("current")


class _SnAgentTempThresholdLevel_Type(Integer32):
    """Custom type snAgentTempThresholdLevel based on Integer32"""
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
        *(("high", 4),
          ("low", 1),
          ("medium", 2),
          ("mediumHhigh", 3))
    )


_SnAgentTempThresholdLevel_Type.__name__ = "Integer32"
_SnAgentTempThresholdLevel_Object = MibTableColumn
snAgentTempThresholdLevel = _SnAgentTempThresholdLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 2, 1, 2),
    _SnAgentTempThresholdLevel_Type()
)
snAgentTempThresholdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snAgentTempThresholdLevel.setStatus("current")


class _SnAgentTempThresholdHighValue_Type(Integer32):
    """Custom type snAgentTempThresholdHighValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 250),
    )


_SnAgentTempThresholdHighValue_Type.__name__ = "Integer32"
_SnAgentTempThresholdHighValue_Object = MibTableColumn
snAgentTempThresholdHighValue = _SnAgentTempThresholdHighValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 2, 1, 3),
    _SnAgentTempThresholdHighValue_Type()
)
snAgentTempThresholdHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentTempThresholdHighValue.setStatus("current")


class _SnAgentTempThresholdLowValue_Type(Integer32):
    """Custom type snAgentTempThresholdLowValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 250),
    )


_SnAgentTempThresholdLowValue_Type.__name__ = "Integer32"
_SnAgentTempThresholdLowValue_Object = MibTableColumn
snAgentTempThresholdLowValue = _SnAgentTempThresholdLowValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 2, 1, 4),
    _SnAgentTempThresholdLowValue_Type()
)
snAgentTempThresholdLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentTempThresholdLowValue.setStatus("current")
_SnAgentTemp2Table_Object = MibTable
snAgentTemp2Table = _SnAgentTemp2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 3)
)
if mibBuilder.loadTexts:
    snAgentTemp2Table.setStatus("current")
_SnAgentTemp2Entry_Object = MibTableRow
snAgentTemp2Entry = _SnAgentTemp2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 3, 1)
)
snAgentTemp2Entry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTemp2UnitNum"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTemp2SlotNum"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTemp2SensorId"),
)
if mibBuilder.loadTexts:
    snAgentTemp2Entry.setStatus("current")
_SnAgentTemp2UnitNum_Type = Integer32
_SnAgentTemp2UnitNum_Object = MibTableColumn
snAgentTemp2UnitNum = _SnAgentTemp2UnitNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 3, 1, 1),
    _SnAgentTemp2UnitNum_Type()
)
snAgentTemp2UnitNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snAgentTemp2UnitNum.setStatus("current")
_SnAgentTemp2SlotNum_Type = Integer32
_SnAgentTemp2SlotNum_Object = MibTableColumn
snAgentTemp2SlotNum = _SnAgentTemp2SlotNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 3, 1, 2),
    _SnAgentTemp2SlotNum_Type()
)
snAgentTemp2SlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snAgentTemp2SlotNum.setStatus("current")
_SnAgentTemp2SensorId_Type = Integer32
_SnAgentTemp2SensorId_Object = MibTableColumn
snAgentTemp2SensorId = _SnAgentTemp2SensorId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 3, 1, 3),
    _SnAgentTemp2SensorId_Type()
)
snAgentTemp2SensorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snAgentTemp2SensorId.setStatus("current")


class _SnAgentTemp2SensorDescr_Type(DisplayString):
    """Custom type snAgentTemp2SensorDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnAgentTemp2SensorDescr_Type.__name__ = "DisplayString"
_SnAgentTemp2SensorDescr_Object = MibTableColumn
snAgentTemp2SensorDescr = _SnAgentTemp2SensorDescr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 3, 1, 4),
    _SnAgentTemp2SensorDescr_Type()
)
snAgentTemp2SensorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTemp2SensorDescr.setStatus("current")


class _SnAgentTemp2Value_Type(Integer32):
    """Custom type snAgentTemp2Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 250),
    )


_SnAgentTemp2Value_Type.__name__ = "Integer32"
_SnAgentTemp2Value_Object = MibTableColumn
snAgentTemp2Value = _SnAgentTemp2Value_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 13, 3, 1, 5),
    _SnAgentTemp2Value_Type()
)
snAgentTemp2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTemp2Value.setStatus("current")
_SnAgentPoe_ObjectIdentity = ObjectIdentity
snAgentPoe = _SnAgentPoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 14)
)
_SnAgentLicense_ObjectIdentity = ObjectIdentity
snAgentLicense = _SnAgentLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15)
)
_FdryLicenseTable_Object = MibTable
fdryLicenseTable = _FdryLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    fdryLicenseTable.setStatus("current")
_FdryLicenseEntry_Object = MibTableRow
fdryLicenseEntry = _FdryLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1)
)
fdryLicenseEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "fdryLicensePackageName"),
    (0, "FOUNDRY-SN-AGENT-MIB", "fdryLicenseLid"),
    (1, "FOUNDRY-SN-AGENT-MIB", "fdryLicenseHash"),
)
if mibBuilder.loadTexts:
    fdryLicenseEntry.setStatus("current")


class _FdryLicensePackageName_Type(DisplayString):
    """Custom type fdryLicensePackageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_FdryLicensePackageName_Type.__name__ = "DisplayString"
_FdryLicensePackageName_Object = MibTableColumn
fdryLicensePackageName = _FdryLicensePackageName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 1),
    _FdryLicensePackageName_Type()
)
fdryLicensePackageName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryLicensePackageName.setStatus("current")


class _FdryLicenseLid_Type(DisplayString):
    """Custom type fdryLicenseLid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_FdryLicenseLid_Type.__name__ = "DisplayString"
_FdryLicenseLid_Object = MibTableColumn
fdryLicenseLid = _FdryLicenseLid_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 2),
    _FdryLicenseLid_Type()
)
fdryLicenseLid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryLicenseLid.setStatus("current")


class _FdryLicenseHash_Type(DisplayString):
    """Custom type fdryLicenseHash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_FdryLicenseHash_Type.__name__ = "DisplayString"
_FdryLicenseHash_Object = MibTableColumn
fdryLicenseHash = _FdryLicenseHash_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 3),
    _FdryLicenseHash_Type()
)
fdryLicenseHash.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryLicenseHash.setStatus("current")


class _FdryLicenseType_Type(Integer32):
    """Custom type fdryLicenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("trial", 2))
    )


_FdryLicenseType_Type.__name__ = "Integer32"
_FdryLicenseType_Object = MibTableColumn
fdryLicenseType = _FdryLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 4),
    _FdryLicenseType_Type()
)
fdryLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicenseType.setStatus("current")


class _FdryLicensePrecedence_Type(Unsigned32):
    """Custom type fdryLicensePrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryLicensePrecedence_Type.__name__ = "Unsigned32"
_FdryLicensePrecedence_Object = MibTableColumn
fdryLicensePrecedence = _FdryLicensePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 5),
    _FdryLicensePrecedence_Type()
)
fdryLicensePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicensePrecedence.setStatus("current")


class _FdryLicenseTrialDays_Type(Unsigned32):
    """Custom type fdryLicenseTrialDays based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryLicenseTrialDays_Type.__name__ = "Unsigned32"
_FdryLicenseTrialDays_Object = MibTableColumn
fdryLicenseTrialDays = _FdryLicenseTrialDays_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 6),
    _FdryLicenseTrialDays_Type()
)
fdryLicenseTrialDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicenseTrialDays.setStatus("current")


class _FdryLicenseTrialTimeElapsed_Type(Unsigned32):
    """Custom type fdryLicenseTrialTimeElapsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryLicenseTrialTimeElapsed_Type.__name__ = "Unsigned32"
_FdryLicenseTrialTimeElapsed_Object = MibTableColumn
fdryLicenseTrialTimeElapsed = _FdryLicenseTrialTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 7),
    _FdryLicenseTrialTimeElapsed_Type()
)
fdryLicenseTrialTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicenseTrialTimeElapsed.setStatus("current")


class _FdryLicenseTrialTimeLeft_Type(Unsigned32):
    """Custom type fdryLicenseTrialTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryLicenseTrialTimeLeft_Type.__name__ = "Unsigned32"
_FdryLicenseTrialTimeLeft_Object = MibTableColumn
fdryLicenseTrialTimeLeft = _FdryLicenseTrialTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 8),
    _FdryLicenseTrialTimeLeft_Type()
)
fdryLicenseTrialTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicenseTrialTimeLeft.setStatus("current")


class _FdryLicenseTrialState_Type(Integer32):
    """Custom type fdryLicenseTrialState based on Integer32"""
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
        *(("active", 3),
          ("duplicated", 5),
          ("expired", 4),
          ("invalid", 1),
          ("unused", 2))
    )


_FdryLicenseTrialState_Type.__name__ = "Integer32"
_FdryLicenseTrialState_Object = MibTableColumn
fdryLicenseTrialState = _FdryLicenseTrialState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 9),
    _FdryLicenseTrialState_Type()
)
fdryLicenseTrialState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicenseTrialState.setStatus("current")
_FdryLicenseVendorInfo_Type = DisplayString
_FdryLicenseVendorInfo_Object = MibTableColumn
fdryLicenseVendorInfo = _FdryLicenseVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 10),
    _FdryLicenseVendorInfo_Type()
)
fdryLicenseVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicenseVendorInfo.setStatus("current")
_FdryLicenseSlot_Type = Integer32
_FdryLicenseSlot_Object = MibTableColumn
fdryLicenseSlot = _FdryLicenseSlot_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 11),
    _FdryLicenseSlot_Type()
)
fdryLicenseSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicenseSlot.setStatus("current")


class _FdryLicenseMode_Type(Integer32):
    """Custom type fdryLicenseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodeLocked", 1),
          ("nonNodeLocked", 2))
    )


_FdryLicenseMode_Type.__name__ = "Integer32"
_FdryLicenseMode_Object = MibTableColumn
fdryLicenseMode = _FdryLicenseMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 12),
    _FdryLicenseMode_Type()
)
fdryLicenseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicenseMode.setStatus("current")
_FdryLicenseSerialNumber_Type = DisplayString
_FdryLicenseSerialNumber_Object = MibTableColumn
fdryLicenseSerialNumber = _FdryLicenseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 13),
    _FdryLicenseSerialNumber_Type()
)
fdryLicenseSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicenseSerialNumber.setStatus("current")
_FdryLicenseCapacity_Type = Integer32
_FdryLicenseCapacity_Object = MibTableColumn
fdryLicenseCapacity = _FdryLicenseCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 1, 1, 14),
    _FdryLicenseCapacity_Type()
)
fdryLicenseCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicenseCapacity.setStatus("current")


class _FdryLicensedFeatureInfo_Type(Bits):
    """Custom type fdryLicensedFeatureInfo based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 2),
          ("isis", 1),
          ("mpls", 3),
          ("ospf", 0))
    )

_FdryLicensedFeatureInfo_Type.__name__ = "Bits"
_FdryLicensedFeatureInfo_Object = MibScalar
fdryLicensedFeatureInfo = _FdryLicensedFeatureInfo_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 2),
    _FdryLicensedFeatureInfo_Type()
)
fdryLicensedFeatureInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLicensedFeatureInfo.setStatus("current")
_BrcdPortLicenseTable_Object = MibTable
brcdPortLicenseTable = _BrcdPortLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 3)
)
if mibBuilder.loadTexts:
    brcdPortLicenseTable.setStatus("current")
_BrcdPortLicenseEntry_Object = MibTableRow
brcdPortLicenseEntry = _BrcdPortLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 3, 1)
)
brcdPortLicenseEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "brcdPortLicenseIndex"),
)
if mibBuilder.loadTexts:
    brcdPortLicenseEntry.setStatus("current")
_BrcdPortLicenseIndex_Type = InterfaceIndex
_BrcdPortLicenseIndex_Object = MibTableColumn
brcdPortLicenseIndex = _BrcdPortLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 3, 1, 1),
    _BrcdPortLicenseIndex_Type()
)
brcdPortLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdPortLicenseIndex.setStatus("current")


class _BrcdPortLicenseStatus_Type(Integer32):
    """Custom type brcdPortLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noLic", 2),
          ("validLic", 1))
    )


_BrcdPortLicenseStatus_Type.__name__ = "Integer32"
_BrcdPortLicenseStatus_Object = MibTableColumn
brcdPortLicenseStatus = _BrcdPortLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 15, 3, 1, 2),
    _BrcdPortLicenseStatus_Type()
)
brcdPortLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdPortLicenseStatus.setStatus("current")
_BrcdSw_ObjectIdentity = ObjectIdentity
brcdSw = _BrcdSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16)
)
_BrcdSwPackageGroup_ObjectIdentity = ObjectIdentity
brcdSwPackageGroup = _BrcdSwPackageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1)
)
_BrcdSwPackageUpgrade_ObjectIdentity = ObjectIdentity
brcdSwPackageUpgrade = _BrcdSwPackageUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1)
)


class _BrcdSwPackageFname_Type(DisplayString):
    """Custom type brcdSwPackageFname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BrcdSwPackageFname_Type.__name__ = "DisplayString"
_BrcdSwPackageFname_Object = MibScalar
brcdSwPackageFname = _BrcdSwPackageFname_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 1),
    _BrcdSwPackageFname_Type()
)
brcdSwPackageFname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSwPackageFname.setStatus("current")


class _BrcdSwPackageLoad_Type(Integer32):
    """Custom type brcdSwPackageLoad based on Integer32"""
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
        *(("none", 1),
          ("tftpToMgmtModulePrimaryIntfModuleSecondary", 4),
          ("tftpToMgmtModuleSecondaryIntfModulePrimary", 5),
          ("tftpToPrimary", 2),
          ("tftpToSecondary", 3))
    )


_BrcdSwPackageLoad_Type.__name__ = "Integer32"
_BrcdSwPackageLoad_Object = MibScalar
brcdSwPackageLoad = _BrcdSwPackageLoad_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 2),
    _BrcdSwPackageLoad_Type()
)
brcdSwPackageLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSwPackageLoad.setStatus("current")


class _BrcdSwPackageLoadStatus_Type(Integer32):
    """Custom type brcdSwPackageLoadStatus based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("downloadingFpgaHBridge", 15),
          ("downloadingFpgaMBridge", 13),
          ("downloadingFpgaSBridge", 14),
          ("downloadingInterfaceModuleApplication", 11),
          ("downloadingInterfaceModuleBoot", 9),
          ("downloadingInterfaceModuleFpga", 12),
          ("downloadingInterfaceModuleMonitor", 10),
          ("downloadingManagementModuleApplication", 8),
          ("downloadingManagementModuleBoot", 6),
          ("downloadingManagementModuleMonitor", 7),
          ("internalError", 3),
          ("manifestFileDownloadError", 4),
          ("manifestFileValidationError", 5),
          ("normal", 1),
          ("started", 2),
          ("upgradingFpgaHBridge", 25),
          ("upgradingFpgaMBridge", 23),
          ("upgradingFpgaSBridge", 24),
          ("upgradingInterfaceModuleApplication", 21),
          ("upgradingInterfaceModuleBoot", 19),
          ("upgradingInterfaceModuleFpga", 22),
          ("upgradingInterfaceModuleMonitor", 20),
          ("upgradingManagementModuleApplication", 18),
          ("upgradingManagementModuleBoot", 16),
          ("upgradingManagementModuleMonitor", 17))
    )


_BrcdSwPackageLoadStatus_Type.__name__ = "Integer32"
_BrcdSwPackageLoadStatus_Object = MibScalar
brcdSwPackageLoadStatus = _BrcdSwPackageLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 3),
    _BrcdSwPackageLoadStatus_Type()
)
brcdSwPackageLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSwPackageLoadStatus.setStatus("current")


class _BrcdSwPackageUpgradeAllImages_Type(TruthValue):
    """Custom type brcdSwPackageUpgradeAllImages based on TruthValue"""


_BrcdSwPackageUpgradeAllImages_Object = MibScalar
brcdSwPackageUpgradeAllImages = _BrcdSwPackageUpgradeAllImages_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 4),
    _BrcdSwPackageUpgradeAllImages_Type()
)
brcdSwPackageUpgradeAllImages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSwPackageUpgradeAllImages.setStatus("current")
_BrcdSwPackageUpgradeResultTable_Object = MibTable
brcdSwPackageUpgradeResultTable = _BrcdSwPackageUpgradeResultTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 5)
)
if mibBuilder.loadTexts:
    brcdSwPackageUpgradeResultTable.setStatus("current")
_BrcdSwPackageUpgradeResultEntry_Object = MibTableRow
brcdSwPackageUpgradeResultEntry = _BrcdSwPackageUpgradeResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 5, 1)
)
brcdSwPackageUpgradeResultEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "brcdSwPackageUpgradeResultIndex"),
)
if mibBuilder.loadTexts:
    brcdSwPackageUpgradeResultEntry.setStatus("current")
_BrcdSwPackageUpgradeResultIndex_Type = Unsigned32
_BrcdSwPackageUpgradeResultIndex_Object = MibTableColumn
brcdSwPackageUpgradeResultIndex = _BrcdSwPackageUpgradeResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 5, 1, 1),
    _BrcdSwPackageUpgradeResultIndex_Type()
)
brcdSwPackageUpgradeResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdSwPackageUpgradeResultIndex.setStatus("current")
_BrcdSwPackageUpgradeResultImageType_Type = BrcdImageType
_BrcdSwPackageUpgradeResultImageType_Object = MibTableColumn
brcdSwPackageUpgradeResultImageType = _BrcdSwPackageUpgradeResultImageType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 5, 1, 2),
    _BrcdSwPackageUpgradeResultImageType_Type()
)
brcdSwPackageUpgradeResultImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSwPackageUpgradeResultImageType.setStatus("current")


class _BrcdSwPackageUpgradeResultStatus_Type(Integer32):
    """Custom type brcdSwPackageUpgradeResultStatus based on Integer32"""
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
        *(("downloadFailed", 2),
          ("installFailed", 3),
          ("ok", 1),
          ("skipped", 4),
          ("unknown", 5))
    )


_BrcdSwPackageUpgradeResultStatus_Type.__name__ = "Integer32"
_BrcdSwPackageUpgradeResultStatus_Object = MibTableColumn
brcdSwPackageUpgradeResultStatus = _BrcdSwPackageUpgradeResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 5, 1, 3),
    _BrcdSwPackageUpgradeResultStatus_Type()
)
brcdSwPackageUpgradeResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSwPackageUpgradeResultStatus.setStatus("current")
_BrcdSwPackageUpgradeResultTimeStamp_Type = TimeStamp
_BrcdSwPackageUpgradeResultTimeStamp_Object = MibTableColumn
brcdSwPackageUpgradeResultTimeStamp = _BrcdSwPackageUpgradeResultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 5, 1, 4),
    _BrcdSwPackageUpgradeResultTimeStamp_Type()
)
brcdSwPackageUpgradeResultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSwPackageUpgradeResultTimeStamp.setStatus("current")


class _BrcdSwPackageUpgradeResultDescription_Type(DisplayString):
    """Custom type brcdSwPackageUpgradeResultDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BrcdSwPackageUpgradeResultDescription_Type.__name__ = "DisplayString"
_BrcdSwPackageUpgradeResultDescription_Object = MibTableColumn
brcdSwPackageUpgradeResultDescription = _BrcdSwPackageUpgradeResultDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 5, 1, 5),
    _BrcdSwPackageUpgradeResultDescription_Type()
)
brcdSwPackageUpgradeResultDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSwPackageUpgradeResultDescription.setStatus("current")


class _BrcdSwPackageUpgradeSkipVersionCheck_Type(TruthValue):
    """Custom type brcdSwPackageUpgradeSkipVersionCheck based on TruthValue"""


_BrcdSwPackageUpgradeSkipVersionCheck_Object = MibScalar
brcdSwPackageUpgradeSkipVersionCheck = _BrcdSwPackageUpgradeSkipVersionCheck_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 1, 6),
    _BrcdSwPackageUpgradeSkipVersionCheck_Type()
)
brcdSwPackageUpgradeSkipVersionCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSwPackageUpgradeSkipVersionCheck.setStatus("current")
_BrcdSwIntfModAutoUpgrade_ObjectIdentity = ObjectIdentity
brcdSwIntfModAutoUpgrade = _BrcdSwIntfModAutoUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 2)
)


class _BrcdSwIntfModAutoUpgradeMode_Type(Integer32):
    """Custom type brcdSwIntfModAutoUpgradeMode based on Integer32"""
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
        *(("disabled", 2),
          ("slot1", 4),
          ("slot2", 5),
          ("tftp", 3),
          ("unknown", 1))
    )


_BrcdSwIntfModAutoUpgradeMode_Type.__name__ = "Integer32"
_BrcdSwIntfModAutoUpgradeMode_Object = MibScalar
brcdSwIntfModAutoUpgradeMode = _BrcdSwIntfModAutoUpgradeMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 2, 1),
    _BrcdSwIntfModAutoUpgradeMode_Type()
)
brcdSwIntfModAutoUpgradeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSwIntfModAutoUpgradeMode.setStatus("current")
_BrcdSwIntfModAutoUpgradeTftpAddrType_Type = InetAddressType
_BrcdSwIntfModAutoUpgradeTftpAddrType_Object = MibScalar
brcdSwIntfModAutoUpgradeTftpAddrType = _BrcdSwIntfModAutoUpgradeTftpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 2, 2),
    _BrcdSwIntfModAutoUpgradeTftpAddrType_Type()
)
brcdSwIntfModAutoUpgradeTftpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSwIntfModAutoUpgradeTftpAddrType.setStatus("current")
_BrcdSwIntfModAutoUpgradeTftpAddr_Type = InetAddress
_BrcdSwIntfModAutoUpgradeTftpAddr_Object = MibScalar
brcdSwIntfModAutoUpgradeTftpAddr = _BrcdSwIntfModAutoUpgradeTftpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 2, 3),
    _BrcdSwIntfModAutoUpgradeTftpAddr_Type()
)
brcdSwIntfModAutoUpgradeTftpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSwIntfModAutoUpgradeTftpAddr.setStatus("current")


class _BrcdSwIntfModAutoUpgradeSrcPath_Type(DisplayString):
    """Custom type brcdSwIntfModAutoUpgradeSrcPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BrcdSwIntfModAutoUpgradeSrcPath_Type.__name__ = "DisplayString"
_BrcdSwIntfModAutoUpgradeSrcPath_Object = MibScalar
brcdSwIntfModAutoUpgradeSrcPath = _BrcdSwIntfModAutoUpgradeSrcPath_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 2, 4),
    _BrcdSwIntfModAutoUpgradeSrcPath_Type()
)
brcdSwIntfModAutoUpgradeSrcPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSwIntfModAutoUpgradeSrcPath.setStatus("current")


class _BrcdSwIntfModAutoUpgradeAllImages_Type(TruthValue):
    """Custom type brcdSwIntfModAutoUpgradeAllImages based on TruthValue"""


_BrcdSwIntfModAutoUpgradeAllImages_Object = MibScalar
brcdSwIntfModAutoUpgradeAllImages = _BrcdSwIntfModAutoUpgradeAllImages_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 16, 1, 2, 5),
    _BrcdSwIntfModAutoUpgradeAllImages_Type()
)
brcdSwIntfModAutoUpgradeAllImages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdSwIntfModAutoUpgradeAllImages.setStatus("deprecated")
_SnAgentTask_ObjectIdentity = ObjectIdentity
snAgentTask = _SnAgentTask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17)
)
_SnAgentTaskCpuTable_Object = MibTable
snAgentTaskCpuTable = _SnAgentTaskCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    snAgentTaskCpuTable.setStatus("current")
_SnAgentTaskCpuEntry_Object = MibTableRow
snAgentTaskCpuEntry = _SnAgentTaskCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 1, 1)
)
snAgentTaskCpuEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTaskCpuTaskID"),
)
if mibBuilder.loadTexts:
    snAgentTaskCpuEntry.setStatus("current")
_SnAgentTaskCpuTaskID_Type = Integer32
_SnAgentTaskCpuTaskID_Object = MibTableColumn
snAgentTaskCpuTaskID = _SnAgentTaskCpuTaskID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 1, 1, 1),
    _SnAgentTaskCpuTaskID_Type()
)
snAgentTaskCpuTaskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskCpuTaskID.setStatus("current")


class _SnAgentTaskCpuTaskName_Type(DisplayString):
    """Custom type snAgentTaskCpuTaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgentTaskCpuTaskName_Type.__name__ = "DisplayString"
_SnAgentTaskCpuTaskName_Object = MibTableColumn
snAgentTaskCpuTaskName = _SnAgentTaskCpuTaskName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 1, 1, 2),
    _SnAgentTaskCpuTaskName_Type()
)
snAgentTaskCpuTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskCpuTaskName.setStatus("current")


class _SnAgentTaskCpuState_Type(DisplayString):
    """Custom type snAgentTaskCpuState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnAgentTaskCpuState_Type.__name__ = "DisplayString"
_SnAgentTaskCpuState_Object = MibTableColumn
snAgentTaskCpuState = _SnAgentTaskCpuState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 1, 1, 3),
    _SnAgentTaskCpuState_Type()
)
snAgentTaskCpuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskCpuState.setStatus("current")
_SnAgentTaskCpuWaitTime_Type = Gauge32
_SnAgentTaskCpuWaitTime_Object = MibTableColumn
snAgentTaskCpuWaitTime = _SnAgentTaskCpuWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 1, 1, 4),
    _SnAgentTaskCpuWaitTime_Type()
)
snAgentTaskCpuWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskCpuWaitTime.setStatus("current")
_SnAgentTaskCpuHoldTime_Type = Gauge32
_SnAgentTaskCpuHoldTime_Object = MibTableColumn
snAgentTaskCpuHoldTime = _SnAgentTaskCpuHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 1, 1, 5),
    _SnAgentTaskCpuHoldTime_Type()
)
snAgentTaskCpuHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskCpuHoldTime.setStatus("current")


class _SnAgentTaskCpuTaskActivity_Type(DisplayString):
    """Custom type snAgentTaskCpuTaskActivity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SnAgentTaskCpuTaskActivity_Type.__name__ = "DisplayString"
_SnAgentTaskCpuTaskActivity_Object = MibTableColumn
snAgentTaskCpuTaskActivity = _SnAgentTaskCpuTaskActivity_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 1, 1, 6),
    _SnAgentTaskCpuTaskActivity_Type()
)
snAgentTaskCpuTaskActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskCpuTaskActivity.setStatus("current")
_SnAgentTaskMQTable_Object = MibTable
snAgentTaskMQTable = _SnAgentTaskMQTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2)
)
if mibBuilder.loadTexts:
    snAgentTaskMQTable.setStatus("current")
_SnAgentTaskMQEntry_Object = MibTableRow
snAgentTaskMQEntry = _SnAgentTaskMQEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1)
)
snAgentTaskMQEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTaskMQTaskID"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTaskMQPriority"),
)
if mibBuilder.loadTexts:
    snAgentTaskMQEntry.setStatus("current")
_SnAgentTaskMQTaskID_Type = Integer32
_SnAgentTaskMQTaskID_Object = MibTableColumn
snAgentTaskMQTaskID = _SnAgentTaskMQTaskID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 1),
    _SnAgentTaskMQTaskID_Type()
)
snAgentTaskMQTaskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQTaskID.setStatus("current")
_SnAgentTaskMQPriority_Type = Integer32
_SnAgentTaskMQPriority_Object = MibTableColumn
snAgentTaskMQPriority = _SnAgentTaskMQPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 2),
    _SnAgentTaskMQPriority_Type()
)
snAgentTaskMQPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQPriority.setStatus("current")


class _SnAgentTaskMQTaskName_Type(DisplayString):
    """Custom type snAgentTaskMQTaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgentTaskMQTaskName_Type.__name__ = "DisplayString"
_SnAgentTaskMQTaskName_Object = MibTableColumn
snAgentTaskMQTaskName = _SnAgentTaskMQTaskName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 3),
    _SnAgentTaskMQTaskName_Type()
)
snAgentTaskMQTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQTaskName.setStatus("current")
_SnAgentTaskMQLength_Type = Integer32
_SnAgentTaskMQLength_Object = MibTableColumn
snAgentTaskMQLength = _SnAgentTaskMQLength_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 4),
    _SnAgentTaskMQLength_Type()
)
snAgentTaskMQLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQLength.setStatus("current")
_SnAgentTaskMQDepth_Type = Gauge32
_SnAgentTaskMQDepth_Object = MibTableColumn
snAgentTaskMQDepth = _SnAgentTaskMQDepth_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 5),
    _SnAgentTaskMQDepth_Type()
)
snAgentTaskMQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQDepth.setStatus("current")
_SnAgentTaskMQMaxDepth_Type = Counter32
_SnAgentTaskMQMaxDepth_Object = MibTableColumn
snAgentTaskMQMaxDepth = _SnAgentTaskMQMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 6),
    _SnAgentTaskMQMaxDepth_Type()
)
snAgentTaskMQMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQMaxDepth.setStatus("current")
_SnAgentTaskMQStickyMaxDepth_Type = Counter32
_SnAgentTaskMQStickyMaxDepth_Object = MibTableColumn
snAgentTaskMQStickyMaxDepth = _SnAgentTaskMQStickyMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 7),
    _SnAgentTaskMQStickyMaxDepth_Type()
)
snAgentTaskMQStickyMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQStickyMaxDepth.setStatus("current")
_SnAgentTaskMQMsgs_Type = Gauge32
_SnAgentTaskMQMsgs_Object = MibTableColumn
snAgentTaskMQMsgs = _SnAgentTaskMQMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 8),
    _SnAgentTaskMQMsgs_Type()
)
snAgentTaskMQMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQMsgs.setStatus("current")
_SnAgentTaskMQMaxMsgs_Type = Counter32
_SnAgentTaskMQMaxMsgs_Object = MibTableColumn
snAgentTaskMQMaxMsgs = _SnAgentTaskMQMaxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 9),
    _SnAgentTaskMQMaxMsgs_Type()
)
snAgentTaskMQMaxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQMaxMsgs.setStatus("current")
_SnAgentTaskMQStickyMaxMsgs_Type = Counter32
_SnAgentTaskMQStickyMaxMsgs_Object = MibTableColumn
snAgentTaskMQStickyMaxMsgs = _SnAgentTaskMQStickyMaxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 10),
    _SnAgentTaskMQStickyMaxMsgs_Type()
)
snAgentTaskMQStickyMaxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQStickyMaxMsgs.setStatus("current")
_SnAgentTaskMQFailedCount_Type = Gauge32
_SnAgentTaskMQFailedCount_Object = MibTableColumn
snAgentTaskMQFailedCount = _SnAgentTaskMQFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 11),
    _SnAgentTaskMQFailedCount_Type()
)
snAgentTaskMQFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQFailedCount.setStatus("current")
_SnAgentTaskMQStickyFailedCount_Type = Counter32
_SnAgentTaskMQStickyFailedCount_Object = MibTableColumn
snAgentTaskMQStickyFailedCount = _SnAgentTaskMQStickyFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 2, 1, 12),
    _SnAgentTaskMQStickyFailedCount_Type()
)
snAgentTaskMQStickyFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskMQStickyFailedCount.setStatus("current")
_SnAgentTaskBufferTable_Object = MibTable
snAgentTaskBufferTable = _SnAgentTaskBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 3)
)
if mibBuilder.loadTexts:
    snAgentTaskBufferTable.setStatus("current")
_SnAgentTaskBufferEntry_Object = MibTableRow
snAgentTaskBufferEntry = _SnAgentTaskBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 3, 1)
)
snAgentTaskBufferEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTaskBufferTaskID"),
    (0, "FOUNDRY-SN-AGENT-MIB", "snAgentTaskBufferPoolID"),
)
if mibBuilder.loadTexts:
    snAgentTaskBufferEntry.setStatus("current")
_SnAgentTaskBufferTaskID_Type = Integer32
_SnAgentTaskBufferTaskID_Object = MibTableColumn
snAgentTaskBufferTaskID = _SnAgentTaskBufferTaskID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 3, 1, 1),
    _SnAgentTaskBufferTaskID_Type()
)
snAgentTaskBufferTaskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskBufferTaskID.setStatus("current")
_SnAgentTaskBufferPoolID_Type = Integer32
_SnAgentTaskBufferPoolID_Object = MibTableColumn
snAgentTaskBufferPoolID = _SnAgentTaskBufferPoolID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 3, 1, 2),
    _SnAgentTaskBufferPoolID_Type()
)
snAgentTaskBufferPoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskBufferPoolID.setStatus("current")


class _SnAgentTaskBufferTaskName_Type(DisplayString):
    """Custom type snAgentTaskBufferTaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgentTaskBufferTaskName_Type.__name__ = "DisplayString"
_SnAgentTaskBufferTaskName_Object = MibTableColumn
snAgentTaskBufferTaskName = _SnAgentTaskBufferTaskName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 3, 1, 3),
    _SnAgentTaskBufferTaskName_Type()
)
snAgentTaskBufferTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskBufferTaskName.setStatus("current")
_SnAgentTaskBufferCount_Type = Gauge32
_SnAgentTaskBufferCount_Object = MibTableColumn
snAgentTaskBufferCount = _SnAgentTaskBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 2, 17, 3, 1, 4),
    _SnAgentTaskBufferCount_Type()
)
snAgentTaskBufferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentTaskBufferCount.setStatus("current")
_SnStackGen_ObjectIdentity = ObjectIdentity
snStackGen = _SnStackGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 1)
)


class _SnStackPriSwitchMode_Type(Integer32):
    """Custom type snStackPriSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnStackPriSwitchMode_Type.__name__ = "Integer32"
_SnStackPriSwitchMode_Object = MibScalar
snStackPriSwitchMode = _SnStackPriSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 1, 1),
    _SnStackPriSwitchMode_Type()
)
snStackPriSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackPriSwitchMode.setStatus("current")
_SnStackMaxSecSwitch_Type = Integer32
_SnStackMaxSecSwitch_Object = MibScalar
snStackMaxSecSwitch = _SnStackMaxSecSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 1, 2),
    _SnStackMaxSecSwitch_Type()
)
snStackMaxSecSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackMaxSecSwitch.setStatus("current")
_SnStackTotalSecSwitch_Type = Integer32
_SnStackTotalSecSwitch_Object = MibScalar
snStackTotalSecSwitch = _SnStackTotalSecSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 1, 3),
    _SnStackTotalSecSwitch_Type()
)
snStackTotalSecSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackTotalSecSwitch.setStatus("current")


class _SnStackSyncAllSecSwitch_Type(Integer32):
    """Custom type snStackSyncAllSecSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("device", 2),
          ("global", 3),
          ("invalid", 1),
          ("local", 4),
          ("normal", 0))
    )


_SnStackSyncAllSecSwitch_Type.__name__ = "Integer32"
_SnStackSyncAllSecSwitch_Object = MibScalar
snStackSyncAllSecSwitch = _SnStackSyncAllSecSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 1, 4),
    _SnStackSyncAllSecSwitch_Type()
)
snStackSyncAllSecSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSyncAllSecSwitch.setStatus("current")


class _SnStackSmSlotIndex_Type(Integer32):
    """Custom type snStackSmSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SnStackSmSlotIndex_Type.__name__ = "Integer32"
_SnStackSmSlotIndex_Object = MibScalar
snStackSmSlotIndex = _SnStackSmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 1, 5),
    _SnStackSmSlotIndex_Type()
)
snStackSmSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSmSlotIndex.setStatus("current")


class _SnStackFmpSetProcess_Type(Integer32):
    """Custom type snStackFmpSetProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("normal", 0),
          ("pending", 1))
    )


_SnStackFmpSetProcess_Type.__name__ = "Integer32"
_SnStackFmpSetProcess_Object = MibScalar
snStackFmpSetProcess = _SnStackFmpSetProcess_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 1, 6),
    _SnStackFmpSetProcess_Type()
)
snStackFmpSetProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackFmpSetProcess.setStatus("current")
_SnStackSecSwitchInfo_ObjectIdentity = ObjectIdentity
snStackSecSwitchInfo = _SnStackSecSwitchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2)
)
_SnStackSecSwitchTable_Object = MibTable
snStackSecSwitchTable = _SnStackSecSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    snStackSecSwitchTable.setStatus("current")
_SnStackSecSwitchEntry_Object = MibTableRow
snStackSecSwitchEntry = _SnStackSecSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1, 1)
)
snStackSecSwitchEntry.setIndexNames(
    (0, "FOUNDRY-SN-AGENT-MIB", "snStackSecSwitchIndex"),
)
if mibBuilder.loadTexts:
    snStackSecSwitchEntry.setStatus("current")


class _SnStackSecSwitchIndex_Type(Integer32):
    """Custom type snStackSecSwitchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_SnStackSecSwitchIndex_Type.__name__ = "Integer32"
_SnStackSecSwitchIndex_Object = MibTableColumn
snStackSecSwitchIndex = _SnStackSecSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1, 1, 1),
    _SnStackSecSwitchIndex_Type()
)
snStackSecSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackSecSwitchIndex.setStatus("current")


class _SnStackSecSwitchSlotId_Type(Integer32):
    """Custom type snStackSecSwitchSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_SnStackSecSwitchSlotId_Type.__name__ = "Integer32"
_SnStackSecSwitchSlotId_Object = MibTableColumn
snStackSecSwitchSlotId = _SnStackSecSwitchSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1, 1, 2),
    _SnStackSecSwitchSlotId_Type()
)
snStackSecSwitchSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchSlotId.setStatus("current")


class _SnStackSecSwitchPortCnts_Type(Integer32):
    """Custom type snStackSecSwitchPortCnts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_SnStackSecSwitchPortCnts_Type.__name__ = "Integer32"
_SnStackSecSwitchPortCnts_Object = MibTableColumn
snStackSecSwitchPortCnts = _SnStackSecSwitchPortCnts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1, 1, 3),
    _SnStackSecSwitchPortCnts_Type()
)
snStackSecSwitchPortCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackSecSwitchPortCnts.setStatus("current")


class _SnStackSecSwitchEnabled_Type(Integer32):
    """Custom type snStackSecSwitchEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnStackSecSwitchEnabled_Type.__name__ = "Integer32"
_SnStackSecSwitchEnabled_Object = MibTableColumn
snStackSecSwitchEnabled = _SnStackSecSwitchEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1, 1, 4),
    _SnStackSecSwitchEnabled_Type()
)
snStackSecSwitchEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchEnabled.setStatus("current")


class _SnStackSecSwitchAck_Type(Integer32):
    """Custom type snStackSecSwitchAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnStackSecSwitchAck_Type.__name__ = "Integer32"
_SnStackSecSwitchAck_Object = MibTableColumn
snStackSecSwitchAck = _SnStackSecSwitchAck_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1, 1, 5),
    _SnStackSecSwitchAck_Type()
)
snStackSecSwitchAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackSecSwitchAck.setStatus("current")
_SnStackSecSwitchMacAddr_Type = MacAddress
_SnStackSecSwitchMacAddr_Object = MibTableColumn
snStackSecSwitchMacAddr = _SnStackSecSwitchMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1, 1, 6),
    _SnStackSecSwitchMacAddr_Type()
)
snStackSecSwitchMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackSecSwitchMacAddr.setStatus("current")


class _SnStackSecSwitchSyncCmd_Type(Integer32):
    """Custom type snStackSecSwitchSyncCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("device", 2),
          ("global", 3),
          ("invalid", 1),
          ("local", 4),
          ("normal", 0))
    )


_SnStackSecSwitchSyncCmd_Type.__name__ = "Integer32"
_SnStackSecSwitchSyncCmd_Object = MibTableColumn
snStackSecSwitchSyncCmd = _SnStackSecSwitchSyncCmd_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1, 1, 7),
    _SnStackSecSwitchSyncCmd_Type()
)
snStackSecSwitchSyncCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchSyncCmd.setStatus("current")
_SnStackSecSwitchIpAddr_Type = IpAddress
_SnStackSecSwitchIpAddr_Object = MibTableColumn
snStackSecSwitchIpAddr = _SnStackSecSwitchIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1, 1, 8),
    _SnStackSecSwitchIpAddr_Type()
)
snStackSecSwitchIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchIpAddr.setStatus("current")
_SnStackSecSwitchSubnetMask_Type = IpAddress
_SnStackSecSwitchSubnetMask_Object = MibTableColumn
snStackSecSwitchSubnetMask = _SnStackSecSwitchSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1, 1, 9),
    _SnStackSecSwitchSubnetMask_Type()
)
snStackSecSwitchSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchSubnetMask.setStatus("current")


class _SnStackSecSwitchCfgCmd_Type(Integer32):
    """Custom type snStackSecSwitchCfgCmd based on Integer32"""
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
        *(("auto", 2),
          ("invalid", 1),
          ("manual", 3),
          ("normal", 0))
    )


_SnStackSecSwitchCfgCmd_Type.__name__ = "Integer32"
_SnStackSecSwitchCfgCmd_Object = MibTableColumn
snStackSecSwitchCfgCmd = _SnStackSecSwitchCfgCmd_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 5, 2, 1, 1, 10),
    _SnStackSecSwitchCfgCmd_Type()
)
snStackSecSwitchCfgCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchCfgCmd.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    **{"MacAddress": MacAddress,
       "DisplayString": DisplayString,
       "BrcdImageType": BrcdImageType,
       "snChasGen": snChasGen,
       "snChasType": snChasType,
       "snChasSerNum": snChasSerNum,
       "snChasPwrSupplyStatus": snChasPwrSupplyStatus,
       "snChasFanStatus": snChasFanStatus,
       "snChasMainBrdDescription": snChasMainBrdDescription,
       "snChasMainPortTotal": snChasMainPortTotal,
       "snChasExpBrdDescription": snChasExpBrdDescription,
       "snChasExpPortTotal": snChasExpPortTotal,
       "snChasStatusLeds": snChasStatusLeds,
       "snChasTrafficLeds": snChasTrafficLeds,
       "snChasMediaLeds": snChasMediaLeds,
       "snChasEnablePwrSupplyTrap": snChasEnablePwrSupplyTrap,
       "snChasMainBrdId": snChasMainBrdId,
       "snChasExpBrdId": snChasExpBrdId,
       "snChasSpeedLeds": snChasSpeedLeds,
       "snChasEnableFanTrap": snChasEnableFanTrap,
       "snChasIdNumber": snChasIdNumber,
       "snChasActualTemperature": snChasActualTemperature,
       "snChasWarningTemperature": snChasWarningTemperature,
       "snChasShutdownTemperature": snChasShutdownTemperature,
       "snChasEnableTempWarnTrap": snChasEnableTempWarnTrap,
       "snChasFlashCard": snChasFlashCard,
       "snChasFlashCardLeds": snChasFlashCardLeds,
       "snChasNumSlots": snChasNumSlots,
       "snChasArchitectureType": snChasArchitectureType,
       "snChasProductType": snChasProductType,
       "snChasSystemMode": snChasSystemMode,
       "snChasFactoryPartNumber": snChasFactoryPartNumber,
       "snChasFactorySerialNumber": snChasFactorySerialNumber,
       "snChasPwr": snChasPwr,
       "snChasPwrSupplyTable": snChasPwrSupplyTable,
       "snChasPwrSupplyEntry": snChasPwrSupplyEntry,
       "snChasPwrSupplyIndex": snChasPwrSupplyIndex,
       "snChasPwrSupplyDescription": snChasPwrSupplyDescription,
       "snChasPwrSupplyOperStatus": snChasPwrSupplyOperStatus,
       "snChasPwrSupply2Table": snChasPwrSupply2Table,
       "snChasPwrSupply2Entry": snChasPwrSupply2Entry,
       "snChasPwrSupply2Unit": snChasPwrSupply2Unit,
       "snChasPwrSupply2Index": snChasPwrSupply2Index,
       "snChasPwrSupply2Description": snChasPwrSupply2Description,
       "snChasPwrSupply2OperStatus": snChasPwrSupply2OperStatus,
       "snChasFan": snChasFan,
       "snChasFanTable": snChasFanTable,
       "snChasFanEntry": snChasFanEntry,
       "snChasFanIndex": snChasFanIndex,
       "snChasFanDescription": snChasFanDescription,
       "snChasFanOperStatus": snChasFanOperStatus,
       "snChasFan2Table": snChasFan2Table,
       "snChasFan2Entry": snChasFan2Entry,
       "snChasFan2Unit": snChasFan2Unit,
       "snChasFan2Index": snChasFan2Index,
       "snChasFan2Description": snChasFan2Description,
       "snChasFan2OperStatus": snChasFan2OperStatus,
       "snChasUnit": snChasUnit,
       "snChasUnitTable": snChasUnitTable,
       "snChasUnitEntry": snChasUnitEntry,
       "snChasUnitIndex": snChasUnitIndex,
       "snChasUnitSerNum": snChasUnitSerNum,
       "snChasUnitNumSlots": snChasUnitNumSlots,
       "snChasUnitActualTemperature": snChasUnitActualTemperature,
       "snChasUnitWarningTemperature": snChasUnitWarningTemperature,
       "snChasUnitShutdownTemperature": snChasUnitShutdownTemperature,
       "snChasUnitPartNum": snChasUnitPartNum,
       "snAgentGbl": snAgentGbl,
       "snAgReload": snAgReload,
       "snAgEraseNVRAM": snAgEraseNVRAM,
       "snAgWriteNVRAM": snAgWriteNVRAM,
       "snAgConfigFromNVRAM": snAgConfigFromNVRAM,
       "snAgTftpServerIp": snAgTftpServerIp,
       "snAgImgFname": snAgImgFname,
       "snAgImgLoad": snAgImgLoad,
       "snAgCfgFname": snAgCfgFname,
       "snAgCfgLoad": snAgCfgLoad,
       "snAgDefGwayIp": snAgDefGwayIp,
       "snAgImgVer": snAgImgVer,
       "snAgFlashImgVer": snAgFlashImgVer,
       "snAgGblIfIpAddr": snAgGblIfIpAddr,
       "snAgGblIfIpMask": snAgGblIfIpMask,
       "snAgGblPassword": snAgGblPassword,
       "snAgTrpRcvrCurEntry": snAgTrpRcvrCurEntry,
       "snAgGblDataRetrieveMode": snAgGblDataRetrieveMode,
       "snAgSystemLog": snAgSystemLog,
       "snAgGblEnableColdStartTrap": snAgGblEnableColdStartTrap,
       "snAgGblEnableLinkUpTrap": snAgGblEnableLinkUpTrap,
       "snAgGblEnableLinkDownTrap": snAgGblEnableLinkDownTrap,
       "snAgGblPasswordChangeMode": snAgGblPasswordChangeMode,
       "snAgGblReadOnlyCommunity": snAgGblReadOnlyCommunity,
       "snAgGblReadWriteCommunity": snAgGblReadWriteCommunity,
       "snAgGblCurrentSecurityLevel": snAgGblCurrentSecurityLevel,
       "snAgGblSecurityLevelSet": snAgGblSecurityLevelSet,
       "snAgGblLevelPasswordsMask": snAgGblLevelPasswordsMask,
       "snAgGblQueueOverflow": snAgGblQueueOverflow,
       "snAgGblBufferShortage": snAgGblBufferShortage,
       "snAgGblDmaFailure": snAgGblDmaFailure,
       "snAgGblResourceLowWarning": snAgGblResourceLowWarning,
       "snAgGblExcessiveErrorWarning": snAgGblExcessiveErrorWarning,
       "snAgGblCpuUtilData": snAgGblCpuUtilData,
       "snAgGblCpuUtilCollect": snAgGblCpuUtilCollect,
       "snAgGblTelnetTimeout": snAgGblTelnetTimeout,
       "snAgGblEnableWebMgmt": snAgGblEnableWebMgmt,
       "snAgGblSecurityLevelBinding": snAgGblSecurityLevelBinding,
       "snAgGblEnableSLB": snAgGblEnableSLB,
       "snAgSoftwareFeature": snAgSoftwareFeature,
       "snAgGblEnableModuleInsertedTrap": snAgGblEnableModuleInsertedTrap,
       "snAgGblEnableModuleRemovedTrap": snAgGblEnableModuleRemovedTrap,
       "snAgGblTrapMessage": snAgGblTrapMessage,
       "snAgGblEnableTelnetServer": snAgGblEnableTelnetServer,
       "snAgGblTelnetPassword": snAgGblTelnetPassword,
       "snAgBuildDate": snAgBuildDate,
       "snAgBuildtime": snAgBuildtime,
       "snAgBuildVer": snAgBuildVer,
       "snAgGblCpuUtil1SecAvg": snAgGblCpuUtil1SecAvg,
       "snAgGblCpuUtil5SecAvg": snAgGblCpuUtil5SecAvg,
       "snAgGblCpuUtil1MinAvg": snAgGblCpuUtil1MinAvg,
       "snAgGblDynMemUtil": snAgGblDynMemUtil,
       "snAgGblDynMemTotal": snAgGblDynMemTotal,
       "snAgGblDynMemFree": snAgGblDynMemFree,
       "snAgImgLoadSPModuleType": snAgImgLoadSPModuleType,
       "snAgImgLoadSPModuleNumber": snAgImgLoadSPModuleNumber,
       "snAgTrapHoldTime": snAgTrapHoldTime,
       "snAgSFlowSourceInterface": snAgSFlowSourceInterface,
       "snAgGblTelnetLoginTimeout": snAgGblTelnetLoginTimeout,
       "snAgGblBannerExec": snAgGblBannerExec,
       "snAgGblBannerIncoming": snAgGblBannerIncoming,
       "snAgGblBannerMotd": snAgGblBannerMotd,
       "snAgWebMgmtServerTcpPort": snAgWebMgmtServerTcpPort,
       "snAgTftpServerAddrType": snAgTftpServerAddrType,
       "snAgTftpServerAddr": snAgTftpServerAddr,
       "snAgGblDeleteFirstBeforeDownload": snAgGblDeleteFirstBeforeDownload,
       "snAgGblPasswordCheckMode": snAgGblPasswordCheckMode,
       "snAgentBrd": snAgentBrd,
       "snAgentBrdTable": snAgentBrdTable,
       "snAgentBrdEntry": snAgentBrdEntry,
       "snAgentBrdIndex": snAgentBrdIndex,
       "snAgentBrdMainBrdDescription": snAgentBrdMainBrdDescription,
       "snAgentBrdMainBrdId": snAgentBrdMainBrdId,
       "snAgentBrdMainPortTotal": snAgentBrdMainPortTotal,
       "snAgentBrdExpBrdDescription": snAgentBrdExpBrdDescription,
       "snAgentBrdExpBrdId": snAgentBrdExpBrdId,
       "snAgentBrdExpPortTotal": snAgentBrdExpPortTotal,
       "snAgentBrdStatusLeds": snAgentBrdStatusLeds,
       "snAgentBrdTrafficLeds": snAgentBrdTrafficLeds,
       "snAgentBrdMediaLeds": snAgentBrdMediaLeds,
       "snAgentBrdSpeedLeds": snAgentBrdSpeedLeds,
       "snAgentBrdModuleStatus": snAgentBrdModuleStatus,
       "snAgentBrdRedundantStatus": snAgentBrdRedundantStatus,
       "snAgentBrdAlarmLeds": snAgentBrdAlarmLeds,
       "snAgentBrdTxTrafficLeds": snAgentBrdTxTrafficLeds,
       "snAgentBrdRxTrafficLeds": snAgentBrdRxTrafficLeds,
       "snAgentBrdStatusLedString": snAgentBrdStatusLedString,
       "snAgentBrdTrafficLedString": snAgentBrdTrafficLedString,
       "snAgentBrdMediaLedString": snAgentBrdMediaLedString,
       "snAgentBrdSpeedLedString": snAgentBrdSpeedLedString,
       "snAgentBrdAlarmLedString": snAgentBrdAlarmLedString,
       "snAgentBrdTxTrafficLedString": snAgentBrdTxTrafficLedString,
       "snAgentBrdRxTrafficLedString": snAgentBrdRxTrafficLedString,
       "snAgentBrdMemoryTotal": snAgentBrdMemoryTotal,
       "snAgentBrdMemoryAvailable": snAgentBrdMemoryAvailable,
       "snAgentBrdSerialNumber": snAgentBrdSerialNumber,
       "snAgentBrdPartNumber": snAgentBrdPartNumber,
       "snAgentBrdMemoryUtil100thPercent": snAgentBrdMemoryUtil100thPercent,
       "snAgentBrdUpTime": snAgentBrdUpTime,
       "snAgentBrd2Table": snAgentBrd2Table,
       "snAgentBrd2Entry": snAgentBrd2Entry,
       "snAgentBrd2Unit": snAgentBrd2Unit,
       "snAgentBrd2Slot": snAgentBrd2Slot,
       "snAgentBrd2MainBrdDescription": snAgentBrd2MainBrdDescription,
       "snAgentBrd2MainBrdId": snAgentBrd2MainBrdId,
       "snAgentBrd2MainPortTotal": snAgentBrd2MainPortTotal,
       "snAgentBrd2ModuleStatus": snAgentBrd2ModuleStatus,
       "snAgentBrd2RedundantStatus": snAgentBrd2RedundantStatus,
       "snAgentTrp": snAgentTrp,
       "snAgTrpRcvrTable": snAgTrpRcvrTable,
       "snAgTrpRcvrEntry": snAgTrpRcvrEntry,
       "snAgTrpRcvrIndex": snAgTrpRcvrIndex,
       "snAgTrpRcvrIpAddr": snAgTrpRcvrIpAddr,
       "snAgTrpRcvrCommunityOrSecurityName": snAgTrpRcvrCommunityOrSecurityName,
       "snAgTrpRcvrStatus": snAgTrpRcvrStatus,
       "snAgTrpRcvrUDPPort": snAgTrpRcvrUDPPort,
       "snAgTrpRcvrSecurityModel": snAgTrpRcvrSecurityModel,
       "snAgTrpRcvrSecurityLevel": snAgTrpRcvrSecurityLevel,
       "snAgentBoot": snAgentBoot,
       "snAgBootSeqTable": snAgBootSeqTable,
       "snAgBootSeqEntry": snAgBootSeqEntry,
       "snAgBootSeqIndex": snAgBootSeqIndex,
       "snAgBootSeqInstruction": snAgBootSeqInstruction,
       "snAgBootSeqIpAddr": snAgBootSeqIpAddr,
       "snAgBootSeqFilename": snAgBootSeqFilename,
       "snAgBootSeqRowStatus": snAgBootSeqRowStatus,
       "snAgSpBootSeqTable": snAgSpBootSeqTable,
       "snAgSpBootSeqEntry": snAgSpBootSeqEntry,
       "snAgSpBootSeqSpNumber": snAgSpBootSeqSpNumber,
       "snAgSpBootSeqIndex": snAgSpBootSeqIndex,
       "snAgSpBootSeqInstruction": snAgSpBootSeqInstruction,
       "snAgSpBootSeqIpAddr": snAgSpBootSeqIpAddr,
       "snAgSpBootSeqFilename": snAgSpBootSeqFilename,
       "snAgSpBootSeqRowStatus": snAgSpBootSeqRowStatus,
       "snAgCfgEos": snAgCfgEos,
       "snAgCfgEosTable": snAgCfgEosTable,
       "snAgCfgEosEntry": snAgCfgEosEntry,
       "snAgCfgEosIndex": snAgCfgEosIndex,
       "snAgCfgEosPacket": snAgCfgEosPacket,
       "snAgCfgEosChkSum": snAgCfgEosChkSum,
       "snAgentLog": snAgentLog,
       "snAgSysLogGbl": snAgSysLogGbl,
       "snAgSysLogGblEnable": snAgSysLogGblEnable,
       "snAgSysLogGblBufferSize": snAgSysLogGblBufferSize,
       "snAgSysLogGblClear": snAgSysLogGblClear,
       "snAgSysLogGblCriticalLevel": snAgSysLogGblCriticalLevel,
       "snAgSysLogGblLoggedCount": snAgSysLogGblLoggedCount,
       "snAgSysLogGblDroppedCount": snAgSysLogGblDroppedCount,
       "snAgSysLogGblFlushedCount": snAgSysLogGblFlushedCount,
       "snAgSysLogGblOverrunCount": snAgSysLogGblOverrunCount,
       "snAgSysLogGblServer": snAgSysLogGblServer,
       "snAgSysLogGblFacility": snAgSysLogGblFacility,
       "snAgSysLogGblPersistenceEnable": snAgSysLogGblPersistenceEnable,
       "snAgSysLogBufferTable": snAgSysLogBufferTable,
       "snAgSysLogBufferEntry": snAgSysLogBufferEntry,
       "snAgSysLogBufferIndex": snAgSysLogBufferIndex,
       "snAgSysLogBufferTimeStamp": snAgSysLogBufferTimeStamp,
       "snAgSysLogBufferCriticalLevel": snAgSysLogBufferCriticalLevel,
       "snAgSysLogBufferMessage": snAgSysLogBufferMessage,
       "snAgSysLogBufferCalTimeStamp": snAgSysLogBufferCalTimeStamp,
       "snAgStaticSysLogBufferTable": snAgStaticSysLogBufferTable,
       "snAgStaticSysLogBufferEntry": snAgStaticSysLogBufferEntry,
       "snAgStaticSysLogBufferIndex": snAgStaticSysLogBufferIndex,
       "snAgStaticSysLogBufferTimeStamp": snAgStaticSysLogBufferTimeStamp,
       "snAgStaticSysLogBufferCriticalLevel": snAgStaticSysLogBufferCriticalLevel,
       "snAgStaticSysLogBufferMessage": snAgStaticSysLogBufferMessage,
       "snAgStaticSysLogBufferCalTimeStamp": snAgStaticSysLogBufferCalTimeStamp,
       "snAgSysLogServerTable": snAgSysLogServerTable,
       "snAgSysLogServerEntry": snAgSysLogServerEntry,
       "snAgSysLogServerIP": snAgSysLogServerIP,
       "snAgSysLogServerUDPPort": snAgSysLogServerUDPPort,
       "snAgSysLogServerRowStatus": snAgSysLogServerRowStatus,
       "snAgentSysParaConfig": snAgentSysParaConfig,
       "snAgentSysParaConfigTable": snAgentSysParaConfigTable,
       "snAgentSysParaConfigEntry": snAgentSysParaConfigEntry,
       "snAgentSysParaConfigIndex": snAgentSysParaConfigIndex,
       "snAgentSysParaConfigDescription": snAgentSysParaConfigDescription,
       "snAgentSysParaConfigMin": snAgentSysParaConfigMin,
       "snAgentSysParaConfigMax": snAgentSysParaConfigMax,
       "snAgentSysParaConfigDefault": snAgentSysParaConfigDefault,
       "snAgentSysParaConfigCurrent": snAgentSysParaConfigCurrent,
       "snAgentConfigModule": snAgentConfigModule,
       "snAgentConfigModuleTable": snAgentConfigModuleTable,
       "snAgentConfigModuleEntry": snAgentConfigModuleEntry,
       "snAgentConfigModuleIndex": snAgentConfigModuleIndex,
       "snAgentConfigModuleType": snAgentConfigModuleType,
       "snAgentConfigModuleRowStatus": snAgentConfigModuleRowStatus,
       "snAgentConfigModuleDescription": snAgentConfigModuleDescription,
       "snAgentConfigModuleOperStatus": snAgentConfigModuleOperStatus,
       "snAgentConfigModuleSerialNumber": snAgentConfigModuleSerialNumber,
       "snAgentConfigModuleNumberOfPorts": snAgentConfigModuleNumberOfPorts,
       "snAgentConfigModuleMgmtModuleType": snAgentConfigModuleMgmtModuleType,
       "snAgentConfigModuleNumberOfCpus": snAgentConfigModuleNumberOfCpus,
       "snAgentConfigModule2Table": snAgentConfigModule2Table,
       "snAgentConfigModule2Entry": snAgentConfigModule2Entry,
       "snAgentConfigModule2Unit": snAgentConfigModule2Unit,
       "snAgentConfigModule2Slot": snAgentConfigModule2Slot,
       "snAgentConfigModule2Type": snAgentConfigModule2Type,
       "snAgentConfigModule2RowStatus": snAgentConfigModule2RowStatus,
       "snAgentConfigModule2Description": snAgentConfigModule2Description,
       "snAgentConfigModule2OperStatus": snAgentConfigModule2OperStatus,
       "snAgentConfigModule2SerialNumber": snAgentConfigModule2SerialNumber,
       "snAgentConfigModule2NumberOfPorts": snAgentConfigModule2NumberOfPorts,
       "snAgentConfigModule2MgmtModuleType": snAgentConfigModule2MgmtModuleType,
       "snAgentConfigModule2NumberOfCpus": snAgentConfigModule2NumberOfCpus,
       "snAgentUser": snAgentUser,
       "snAgentUserGbl": snAgentUserGbl,
       "snAgentUserMaxAccnt": snAgentUserMaxAccnt,
       "snAgentUserAccntTable": snAgentUserAccntTable,
       "snAgentUserAccntEntry": snAgentUserAccntEntry,
       "snAgentUserAccntName": snAgentUserAccntName,
       "snAgentUserAccntPassword": snAgentUserAccntPassword,
       "snAgentUserAccntEncryptCode": snAgentUserAccntEncryptCode,
       "snAgentUserAccntPrivilege": snAgentUserAccntPrivilege,
       "snAgentUserAccntRowStatus": snAgentUserAccntRowStatus,
       "snAgentRedundant": snAgentRedundant,
       "snAgentRedunGbl": snAgentRedunGbl,
       "snAgentRedunActiveMgmtMod": snAgentRedunActiveMgmtMod,
       "snAgentRedunSyncConfig": snAgentRedunSyncConfig,
       "snAgentRedunBkupCopyBootCode": snAgentRedunBkupCopyBootCode,
       "snAgentEnableMgmtModRedunStateChangeTrap": snAgentEnableMgmtModRedunStateChangeTrap,
       "snAgentRedunBkupBootLoad": snAgentRedunBkupBootLoad,
       "snAgentRedunSwitchOver": snAgentRedunSwitchOver,
       "snAgentCpu": snAgentCpu,
       "snAgentCpuUtilTable": snAgentCpuUtilTable,
       "snAgentCpuUtilEntry": snAgentCpuUtilEntry,
       "snAgentCpuUtilSlotNum": snAgentCpuUtilSlotNum,
       "snAgentCpuUtilCpuId": snAgentCpuUtilCpuId,
       "snAgentCpuUtilInterval": snAgentCpuUtilInterval,
       "snAgentCpuUtilValue": snAgentCpuUtilValue,
       "snAgentCpuUtilPercent": snAgentCpuUtilPercent,
       "snAgentCpuUtil100thPercent": snAgentCpuUtil100thPercent,
       "snCpuProcessTable": snCpuProcessTable,
       "snCpuProcessEntry": snCpuProcessEntry,
       "snCpuProcessName": snCpuProcessName,
       "snCpuProcess5SecUtil": snCpuProcess5SecUtil,
       "snCpuProcess1MinUtil": snCpuProcess1MinUtil,
       "snCpuProcess5MinUtil": snCpuProcess5MinUtil,
       "snCpuProcess15MinUtil": snCpuProcess15MinUtil,
       "snCpuProcessRuntime": snCpuProcessRuntime,
       "snAgentCpuProcessEnable": snAgentCpuProcessEnable,
       "snAgentHw": snAgentHw,
       "snAgentHwICBMCounterTable": snAgentHwICBMCounterTable,
       "snAgentHwICBMCounterEntry": snAgentHwICBMCounterEntry,
       "snAgentHwICBMCounterSlot": snAgentHwICBMCounterSlot,
       "snAgentHwICBMCounterDMA": snAgentHwICBMCounterDMA,
       "snAgentHwICBMCounterFreeDepth": snAgentHwICBMCounterFreeDepth,
       "snAgentHwICBMCounterWriteDrop": snAgentHwICBMCounterWriteDrop,
       "snAgentHwICBMCounterWriteInput": snAgentHwICBMCounterWriteInput,
       "snAgentHwICBMCounterWriteOutput": snAgentHwICBMCounterWriteOutput,
       "snAgentHwICBMCounterReadInput": snAgentHwICBMCounterReadInput,
       "snAgentHwICBMCounterReadOutput": snAgentHwICBMCounterReadOutput,
       "snCAMIpStatTable": snCAMIpStatTable,
       "snCAMIpStatEntry": snCAMIpStatEntry,
       "snCAMIpStatIfIndex": snCAMIpStatIfIndex,
       "snCAMIpStatLevel": snCAMIpStatLevel,
       "snCAMIpStatFreeEntries": snCAMIpStatFreeEntries,
       "snCAMIpStatTotalEntries": snCAMIpStatTotalEntries,
       "snCAMStatTable": snCAMStatTable,
       "snCAMStatEntry": snCAMStatEntry,
       "snCamStatDMAIdNumber": snCamStatDMAIdNumber,
       "snCamStatDMAMasterNumber": snCamStatDMAMasterNumber,
       "snCamStatFreePool0Entries": snCamStatFreePool0Entries,
       "snCamStatFreePool1Entries": snCamStatFreePool1Entries,
       "snCamStatFreePool2Entries": snCamStatFreePool2Entries,
       "snCamStatFreePool3Entries": snCamStatFreePool3Entries,
       "snCamStatFreeL2Entries": snCamStatFreeL2Entries,
       "snCamStatFreeL2LowestSection": snCamStatFreeL2LowestSection,
       "snCamStatHostLookupCount": snCamStatHostLookupCount,
       "snCamStatRouteLookupCount": snCamStatRouteLookupCount,
       "snCamStatLevel1": snCamStatLevel1,
       "snCamStatLevel2": snCamStatLevel2,
       "snCamStatLevel3": snCamStatLevel3,
       "snCamStatMacFailCount": snCamStatMacFailCount,
       "snCamStatIPRouteFailCount": snCamStatIPRouteFailCount,
       "snCamStatIPSessionFailCount": snCamStatIPSessionFailCount,
       "snCamStatIPMCastFailCount": snCamStatIPMCastFailCount,
       "snCamStatL2SessionFailCount": snCamStatL2SessionFailCount,
       "snCamStatAddMACCount": snCamStatAddMACCount,
       "snCamStatAddVLANCount": snCamStatAddVLANCount,
       "snCamStatAddIPHostCount": snCamStatAddIPHostCount,
       "snCamStatAddIPRouteCount": snCamStatAddIPRouteCount,
       "snCamStatAddIPSessionCount": snCamStatAddIPSessionCount,
       "snCamStatAddIPMCastCount": snCamStatAddIPMCastCount,
       "snCamStatAddL2SessionCount": snCamStatAddL2SessionCount,
       "snCamStatAddIPXCount": snCamStatAddIPXCount,
       "snCamStatDeleteDMACamCount": snCamStatDeleteDMACamCount,
       "snAgSystemDRAM": snAgSystemDRAM,
       "snAgSystemDRAMUtil": snAgSystemDRAMUtil,
       "snAgSystemDRAMTotal": snAgSystemDRAMTotal,
       "snAgSystemDRAMFree": snAgSystemDRAMFree,
       "snAgSystemDRAMForBGP": snAgSystemDRAMForBGP,
       "snAgSystemDRAMForOSPF": snAgSystemDRAMForOSPF,
       "snAgSystemDebug": snAgSystemDebug,
       "snAgSystemDebugTotalIn": snAgSystemDebugTotalIn,
       "snAgSystemDebugTotalOut": snAgSystemDebugTotalOut,
       "snAgSystemDebugCpuQueueRead": snAgSystemDebugCpuQueueRead,
       "snAgSystemDebugDRAMBuffer": snAgSystemDebugDRAMBuffer,
       "snAgSystemDebugBMBuffer": snAgSystemDebugBMBuffer,
       "snAgSystemDebugBMFreeBuffer": snAgSystemDebugBMFreeBuffer,
       "snAgSystemDebugBMFreeBufferMgmt": snAgSystemDebugBMFreeBufferMgmt,
       "snAgSystemDebugIpcGigLock": snAgSystemDebugIpcGigLock,
       "snAgSystemDebugDRAMGetError": snAgSystemDebugDRAMGetError,
       "snAgSystemDebugDRAMToBMCopyFail": snAgSystemDebugDRAMToBMCopyFail,
       "snAgentTemp": snAgentTemp,
       "snAgentTempTable": snAgentTempTable,
       "snAgentTempEntry": snAgentTempEntry,
       "snAgentTempSlotNum": snAgentTempSlotNum,
       "snAgentTempSensorId": snAgentTempSensorId,
       "snAgentTempSensorDescr": snAgentTempSensorDescr,
       "snAgentTempValue": snAgentTempValue,
       "snAgentTempThresholdTable": snAgentTempThresholdTable,
       "snAgentTempThresholdEntry": snAgentTempThresholdEntry,
       "snAgentTempThresholdModule": snAgentTempThresholdModule,
       "snAgentTempThresholdLevel": snAgentTempThresholdLevel,
       "snAgentTempThresholdHighValue": snAgentTempThresholdHighValue,
       "snAgentTempThresholdLowValue": snAgentTempThresholdLowValue,
       "snAgentTemp2Table": snAgentTemp2Table,
       "snAgentTemp2Entry": snAgentTemp2Entry,
       "snAgentTemp2UnitNum": snAgentTemp2UnitNum,
       "snAgentTemp2SlotNum": snAgentTemp2SlotNum,
       "snAgentTemp2SensorId": snAgentTemp2SensorId,
       "snAgentTemp2SensorDescr": snAgentTemp2SensorDescr,
       "snAgentTemp2Value": snAgentTemp2Value,
       "snAgentPoe": snAgentPoe,
       "snAgentLicense": snAgentLicense,
       "fdryLicenseTable": fdryLicenseTable,
       "fdryLicenseEntry": fdryLicenseEntry,
       "fdryLicensePackageName": fdryLicensePackageName,
       "fdryLicenseLid": fdryLicenseLid,
       "fdryLicenseHash": fdryLicenseHash,
       "fdryLicenseType": fdryLicenseType,
       "fdryLicensePrecedence": fdryLicensePrecedence,
       "fdryLicenseTrialDays": fdryLicenseTrialDays,
       "fdryLicenseTrialTimeElapsed": fdryLicenseTrialTimeElapsed,
       "fdryLicenseTrialTimeLeft": fdryLicenseTrialTimeLeft,
       "fdryLicenseTrialState": fdryLicenseTrialState,
       "fdryLicenseVendorInfo": fdryLicenseVendorInfo,
       "fdryLicenseSlot": fdryLicenseSlot,
       "fdryLicenseMode": fdryLicenseMode,
       "fdryLicenseSerialNumber": fdryLicenseSerialNumber,
       "fdryLicenseCapacity": fdryLicenseCapacity,
       "fdryLicensedFeatureInfo": fdryLicensedFeatureInfo,
       "brcdPortLicenseTable": brcdPortLicenseTable,
       "brcdPortLicenseEntry": brcdPortLicenseEntry,
       "brcdPortLicenseIndex": brcdPortLicenseIndex,
       "brcdPortLicenseStatus": brcdPortLicenseStatus,
       "brcdSw": brcdSw,
       "brcdSwPackageGroup": brcdSwPackageGroup,
       "brcdSwPackageUpgrade": brcdSwPackageUpgrade,
       "brcdSwPackageFname": brcdSwPackageFname,
       "brcdSwPackageLoad": brcdSwPackageLoad,
       "brcdSwPackageLoadStatus": brcdSwPackageLoadStatus,
       "brcdSwPackageUpgradeAllImages": brcdSwPackageUpgradeAllImages,
       "brcdSwPackageUpgradeResultTable": brcdSwPackageUpgradeResultTable,
       "brcdSwPackageUpgradeResultEntry": brcdSwPackageUpgradeResultEntry,
       "brcdSwPackageUpgradeResultIndex": brcdSwPackageUpgradeResultIndex,
       "brcdSwPackageUpgradeResultImageType": brcdSwPackageUpgradeResultImageType,
       "brcdSwPackageUpgradeResultStatus": brcdSwPackageUpgradeResultStatus,
       "brcdSwPackageUpgradeResultTimeStamp": brcdSwPackageUpgradeResultTimeStamp,
       "brcdSwPackageUpgradeResultDescription": brcdSwPackageUpgradeResultDescription,
       "brcdSwPackageUpgradeSkipVersionCheck": brcdSwPackageUpgradeSkipVersionCheck,
       "brcdSwIntfModAutoUpgrade": brcdSwIntfModAutoUpgrade,
       "brcdSwIntfModAutoUpgradeMode": brcdSwIntfModAutoUpgradeMode,
       "brcdSwIntfModAutoUpgradeTftpAddrType": brcdSwIntfModAutoUpgradeTftpAddrType,
       "brcdSwIntfModAutoUpgradeTftpAddr": brcdSwIntfModAutoUpgradeTftpAddr,
       "brcdSwIntfModAutoUpgradeSrcPath": brcdSwIntfModAutoUpgradeSrcPath,
       "brcdSwIntfModAutoUpgradeAllImages": brcdSwIntfModAutoUpgradeAllImages,
       "snAgentTask": snAgentTask,
       "snAgentTaskCpuTable": snAgentTaskCpuTable,
       "snAgentTaskCpuEntry": snAgentTaskCpuEntry,
       "snAgentTaskCpuTaskID": snAgentTaskCpuTaskID,
       "snAgentTaskCpuTaskName": snAgentTaskCpuTaskName,
       "snAgentTaskCpuState": snAgentTaskCpuState,
       "snAgentTaskCpuWaitTime": snAgentTaskCpuWaitTime,
       "snAgentTaskCpuHoldTime": snAgentTaskCpuHoldTime,
       "snAgentTaskCpuTaskActivity": snAgentTaskCpuTaskActivity,
       "snAgentTaskMQTable": snAgentTaskMQTable,
       "snAgentTaskMQEntry": snAgentTaskMQEntry,
       "snAgentTaskMQTaskID": snAgentTaskMQTaskID,
       "snAgentTaskMQPriority": snAgentTaskMQPriority,
       "snAgentTaskMQTaskName": snAgentTaskMQTaskName,
       "snAgentTaskMQLength": snAgentTaskMQLength,
       "snAgentTaskMQDepth": snAgentTaskMQDepth,
       "snAgentTaskMQMaxDepth": snAgentTaskMQMaxDepth,
       "snAgentTaskMQStickyMaxDepth": snAgentTaskMQStickyMaxDepth,
       "snAgentTaskMQMsgs": snAgentTaskMQMsgs,
       "snAgentTaskMQMaxMsgs": snAgentTaskMQMaxMsgs,
       "snAgentTaskMQStickyMaxMsgs": snAgentTaskMQStickyMaxMsgs,
       "snAgentTaskMQFailedCount": snAgentTaskMQFailedCount,
       "snAgentTaskMQStickyFailedCount": snAgentTaskMQStickyFailedCount,
       "snAgentTaskBufferTable": snAgentTaskBufferTable,
       "snAgentTaskBufferEntry": snAgentTaskBufferEntry,
       "snAgentTaskBufferTaskID": snAgentTaskBufferTaskID,
       "snAgentTaskBufferPoolID": snAgentTaskBufferPoolID,
       "snAgentTaskBufferTaskName": snAgentTaskBufferTaskName,
       "snAgentTaskBufferCount": snAgentTaskBufferCount,
       "snStackGen": snStackGen,
       "snStackPriSwitchMode": snStackPriSwitchMode,
       "snStackMaxSecSwitch": snStackMaxSecSwitch,
       "snStackTotalSecSwitch": snStackTotalSecSwitch,
       "snStackSyncAllSecSwitch": snStackSyncAllSecSwitch,
       "snStackSmSlotIndex": snStackSmSlotIndex,
       "snStackFmpSetProcess": snStackFmpSetProcess,
       "snStackSecSwitchInfo": snStackSecSwitchInfo,
       "snStackSecSwitchTable": snStackSecSwitchTable,
       "snStackSecSwitchEntry": snStackSecSwitchEntry,
       "snStackSecSwitchIndex": snStackSecSwitchIndex,
       "snStackSecSwitchSlotId": snStackSecSwitchSlotId,
       "snStackSecSwitchPortCnts": snStackSecSwitchPortCnts,
       "snStackSecSwitchEnabled": snStackSecSwitchEnabled,
       "snStackSecSwitchAck": snStackSecSwitchAck,
       "snStackSecSwitchMacAddr": snStackSecSwitchMacAddr,
       "snStackSecSwitchSyncCmd": snStackSecSwitchSyncCmd,
       "snStackSecSwitchIpAddr": snStackSecSwitchIpAddr,
       "snStackSecSwitchSubnetMask": snStackSecSwitchSubnetMask,
       "snStackSecSwitchCfgCmd": snStackSecSwitchCfgCmd,
       "snAgent": snAgent}
)
