# SNMP MIB module (SA-RG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SA-RG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:16 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

saRg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2)
)
saRg.setRevisions(
        ("2015-05-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SaRgTimeZone(Integer32, TextualConvention):
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
              62)
        )
    )
    namedValues = NamedValues(
        *(("gmtMinusEightPacificTimeCanadaTijuana", 5),
          ("gmtMinusElevenMidwayIslandSamoa", 2),
          ("gmtMinusFiveBogotaLimaQuito", 12),
          ("gmtMinusFiveEasternTimeCanada", 13),
          ("gmtMinusFiveIndianaEast", 14),
          ("gmtMinusFourAtlanticTimeCanada", 15),
          ("gmtMinusFourCaracasLaPaz", 16),
          ("gmtMinusFourSantiago", 17),
          ("gmtMinusNineAlaska", 4),
          ("gmtMinusOneAzores", 23),
          ("gmtMinusOneCapeVerdeIs", 24),
          ("gmtMinusSevenArizona", 6),
          ("gmtMinusSevenMountainTimeCanada", 7),
          ("gmtMinusSixCentralAmerica", 8),
          ("gmtMinusSixCentralTimeCanada", 9),
          ("gmtMinusSixMexicoCity", 10),
          ("gmtMinusSixSaskatchewan", 11),
          ("gmtMinusTenHawaii", 3),
          ("gmtMinusThreeBrasilia", 19),
          ("gmtMinusThreeBuenosAiresGeorgetown", 20),
          ("gmtMinusThreeGreenland", 21),
          ("gmtMinusThreeThirtyNewfoundland", 18),
          ("gmtMinusTwelveEniwetokKwajalein", 1),
          ("gmtMinusTwoMid-Atlantic", 22),
          ("gmtPlusEightBeijingChongqingHongKongUrumqi", 50),
          ("gmtPlusEightIrkustkUlaanBataar", 51),
          ("gmtPlusEightKualaLumpurSingapore", 52),
          ("gmtPlusEightTaipei", 53),
          ("gmtPlusElevenMagadanSolomonIsNewCaledonia", 59),
          ("gmtPlusFiveEkaterinburg", 42),
          ("gmtPlusFiveFourtyFiveKathmandu", 44),
          ("gmtPlusFiveThirtyCalcuttaChennaiMumbaiNewDelhi", 43),
          ("gmtPlusFourAbuDhabiMuscat", 40),
          ("gmtPlusFourThirtyKabul", 41),
          ("gmtPlusNineOsakaSapporoTokyo", 54),
          ("gmtPlusNineSeoul", 55),
          ("gmtPlusNineThirtyAdelaide", 56),
          ("gmtPlusOneAmsterdamBerlinRomeStockholmVienna", 27),
          ("gmtPlusOneBelgradeBratislavaBudapestLjubljanaPrague", 28),
          ("gmtPlusOneBrusselsCopenhagenMadridParis", 29),
          ("gmtPlusOneSarajevoSkopjeSofijaVilniusWarsawZagreb", 30),
          ("gmtPlusOneWestCentralAfrica", 31),
          ("gmtPlusSevenBangkokHanoiJakarta", 48),
          ("gmtPlusSevenKrasnoyarsk", 49),
          ("gmtPlusSixAlmatyNovosibirsk", 45),
          ("gmtPlusSixAstanaDhaka", 46),
          ("gmtPlusSixThirtyRangoon", 47),
          ("gmtPlusTenBrisbane", 57),
          ("gmtPlusTenVladivostok", 58),
          ("gmtPlusThirteenNukuAlofa", 62),
          ("gmtPlusThreeBaghdad", 36),
          ("gmtPlusThreeMoscowStPetersburgVolgograd", 37),
          ("gmtPlusThreeNairobi", 38),
          ("gmtPlusThreeThirtyTehran", 39),
          ("gmtPlusTwelveAucklandWellington", 60),
          ("gmtPlusTwelveFiji", 61),
          ("gmtPlusTwoAthensIstanbilMinsk", 32),
          ("gmtPlusTwoBucharest", 33),
          ("gmtPlusTwoHelsinkiRigaTallinn", 34),
          ("gmtPlusTwoJerusalem", 35),
          ("gmtZeroCasablancaMonrovia", 25),
          ("gmtZeroDublinEdinburghLisbonLondon", 26))
    )



# MIB Managed Objects in the order of their OIDs

_Sa_ObjectIdentity = ObjectIdentity
sa = _Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429)
)
_SaModules_ObjectIdentity = ObjectIdentity
saModules = _SaModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79)
)
_SaRgDevice_ObjectIdentity = ObjectIdentity
saRgDevice = _SaRgDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1)
)
_SaRgDeviceBase_ObjectIdentity = ObjectIdentity
saRgDeviceBase = _SaRgDeviceBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 1)
)


class _SaRgDeviceMode_Type(Integer32):
    """Custom type saRgDeviceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("dualstack", 5),
          ("ipv4", 3),
          ("ipv6", 4),
          ("multiSsid", 1))
    )


_SaRgDeviceMode_Type.__name__ = "Integer32"
_SaRgDeviceMode_Object = MibScalar
saRgDeviceMode = _SaRgDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 1, 1),
    _SaRgDeviceMode_Type()
)
saRgDeviceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDeviceMode.setStatus("current")


class _SaRgDeviceResetDefaultEnable_Type(TruthValue):
    """Custom type saRgDeviceResetDefaultEnable based on TruthValue"""


_SaRgDeviceResetDefaultEnable_Object = MibScalar
saRgDeviceResetDefaultEnable = _SaRgDeviceResetDefaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 1, 2),
    _SaRgDeviceResetDefaultEnable_Type()
)
saRgDeviceResetDefaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDeviceResetDefaultEnable.setStatus("current")


class _SaRgDeviceRemoteWebAccessPort_Type(InetPortNumber):
    """Custom type saRgDeviceRemoteWebAccessPort based on InetPortNumber"""
    defaultValue = 8080


_SaRgDeviceRemoteWebAccessPort_Object = MibScalar
saRgDeviceRemoteWebAccessPort = _SaRgDeviceRemoteWebAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 1, 4),
    _SaRgDeviceRemoteWebAccessPort_Type()
)
saRgDeviceRemoteWebAccessPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDeviceRemoteWebAccessPort.setStatus("current")


class _SaRgDeviceLanLanIsolation_Type(Integer32):
    """Custom type saRgDeviceLanLanIsolation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SaRgDeviceLanLanIsolation_Type.__name__ = "Integer32"
_SaRgDeviceLanLanIsolation_Object = MibScalar
saRgDeviceLanLanIsolation = _SaRgDeviceLanLanIsolation_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 1, 6),
    _SaRgDeviceLanLanIsolation_Type()
)
saRgDeviceLanLanIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDeviceLanLanIsolation.setStatus("current")


class _SaRgDeviceLanWlanIsolation_Type(Integer32):
    """Custom type saRgDeviceLanWlanIsolation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SaRgDeviceLanWlanIsolation_Type.__name__ = "Integer32"
_SaRgDeviceLanWlanIsolation_Object = MibScalar
saRgDeviceLanWlanIsolation = _SaRgDeviceLanWlanIsolation_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 1, 7),
    _SaRgDeviceLanWlanIsolation_Type()
)
saRgDeviceLanWlanIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDeviceLanWlanIsolation.setStatus("current")


class _SaRgDeviceIpv6Trans_Type(Integer32):
    """Custom type saRgDeviceIpv6Trans based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("dslite", 1))
    )


_SaRgDeviceIpv6Trans_Type.__name__ = "Integer32"
_SaRgDeviceIpv6Trans_Object = MibScalar
saRgDeviceIpv6Trans = _SaRgDeviceIpv6Trans_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 1, 8),
    _SaRgDeviceIpv6Trans_Type()
)
saRgDeviceIpv6Trans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIpv6Trans.setStatus("current")


class _SaRgDeviceIpv6Passthrough_Type(Integer32):
    """Custom type saRgDeviceIpv6Passthrough based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SaRgDeviceIpv6Passthrough_Type.__name__ = "Integer32"
_SaRgDeviceIpv6Passthrough_Object = MibScalar
saRgDeviceIpv6Passthrough = _SaRgDeviceIpv6Passthrough_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 1, 9),
    _SaRgDeviceIpv6Passthrough_Type()
)
saRgDeviceIpv6Passthrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDeviceIpv6Passthrough.setStatus("current")


class _SaRgDeviceFactoryReset_Type(Integer32):
    """Custom type saRgDeviceFactoryReset based on Integer32"""
    defaultValue = 0

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
        *(("false", 0),
          ("routerAndWifi", 1),
          ("routerOnly", 2),
          ("wifi", 3))
    )


_SaRgDeviceFactoryReset_Type.__name__ = "Integer32"
_SaRgDeviceFactoryReset_Object = MibScalar
saRgDeviceFactoryReset = _SaRgDeviceFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 1, 1002),
    _SaRgDeviceFactoryReset_Type()
)
saRgDeviceFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDeviceFactoryReset.setStatus("current")
_SaRgDeviceTimeSetup_ObjectIdentity = ObjectIdentity
saRgDeviceTimeSetup = _SaRgDeviceTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 5)
)
_SaRgDeviceTimeSetupNtpEnabled_Type = TruthValue
_SaRgDeviceTimeSetupNtpEnabled_Object = MibScalar
saRgDeviceTimeSetupNtpEnabled = _SaRgDeviceTimeSetupNtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 5, 1),
    _SaRgDeviceTimeSetupNtpEnabled_Type()
)
saRgDeviceTimeSetupNtpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDeviceTimeSetupNtpEnabled.setStatus("current")
_SaRgDeviceTimeSetupNtpServerTable_Object = MibTable
saRgDeviceTimeSetupNtpServerTable = _SaRgDeviceTimeSetupNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    saRgDeviceTimeSetupNtpServerTable.setStatus("current")
_SaRgDeviceTimeSetupNtpServerEntry_Object = MibTableRow
saRgDeviceTimeSetupNtpServerEntry = _SaRgDeviceTimeSetupNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 5, 2, 1)
)
saRgDeviceTimeSetupNtpServerEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgDeviceTimeSetupNtpServerIndex"),
)
if mibBuilder.loadTexts:
    saRgDeviceTimeSetupNtpServerEntry.setStatus("current")


class _SaRgDeviceTimeSetupNtpServerIndex_Type(Integer32):
    """Custom type saRgDeviceTimeSetupNtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SaRgDeviceTimeSetupNtpServerIndex_Type.__name__ = "Integer32"
_SaRgDeviceTimeSetupNtpServerIndex_Object = MibTableColumn
saRgDeviceTimeSetupNtpServerIndex = _SaRgDeviceTimeSetupNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 5, 2, 1, 1),
    _SaRgDeviceTimeSetupNtpServerIndex_Type()
)
saRgDeviceTimeSetupNtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgDeviceTimeSetupNtpServerIndex.setStatus("current")
_SaRgDeviceTimeSetupNtpServerAddress_Type = SnmpAdminString
_SaRgDeviceTimeSetupNtpServerAddress_Object = MibTableColumn
saRgDeviceTimeSetupNtpServerAddress = _SaRgDeviceTimeSetupNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 5, 2, 1, 2),
    _SaRgDeviceTimeSetupNtpServerAddress_Type()
)
saRgDeviceTimeSetupNtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDeviceTimeSetupNtpServerAddress.setStatus("current")
_SaRgDeviceTimeSetupZone_Type = SaRgTimeZone
_SaRgDeviceTimeSetupZone_Object = MibScalar
saRgDeviceTimeSetupZone = _SaRgDeviceTimeSetupZone_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 5, 3),
    _SaRgDeviceTimeSetupZone_Type()
)
saRgDeviceTimeSetupZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDeviceTimeSetupZone.setStatus("current")


class _SaRgDeviceTimeSetupDst_Type(Integer32):
    """Custom type saRgDeviceTimeSetupDst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_SaRgDeviceTimeSetupDst_Type.__name__ = "Integer32"
_SaRgDeviceTimeSetupDst_Object = MibScalar
saRgDeviceTimeSetupDst = _SaRgDeviceTimeSetupDst_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 5, 4),
    _SaRgDeviceTimeSetupDst_Type()
)
saRgDeviceTimeSetupDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDeviceTimeSetupDst.setStatus("current")
if mibBuilder.loadTexts:
    saRgDeviceTimeSetupDst.setUnits("Minutes")
_SaRgDeviceIanaContent_ObjectIdentity = ObjectIdentity
saRgDeviceIanaContent = _SaRgDeviceIanaContent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 7)
)
_SaRgDeviceIanaIAID_Type = Unsigned32
_SaRgDeviceIanaIAID_Object = MibScalar
saRgDeviceIanaIAID = _SaRgDeviceIanaIAID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 7, 1),
    _SaRgDeviceIanaIAID_Type()
)
saRgDeviceIanaIAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIanaIAID.setStatus("current")
_SaRgDeviceIanaT1_Type = Integer32
_SaRgDeviceIanaT1_Object = MibScalar
saRgDeviceIanaT1 = _SaRgDeviceIanaT1_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 7, 2),
    _SaRgDeviceIanaT1_Type()
)
saRgDeviceIanaT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIanaT1.setStatus("current")
_SaRgDeviceIanaT2_Type = Integer32
_SaRgDeviceIanaT2_Object = MibScalar
saRgDeviceIanaT2 = _SaRgDeviceIanaT2_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 7, 3),
    _SaRgDeviceIanaT2_Type()
)
saRgDeviceIanaT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIanaT2.setStatus("current")
_SaRgDeviceIanaTable_Object = MibTable
saRgDeviceIanaTable = _SaRgDeviceIanaTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    saRgDeviceIanaTable.setStatus("current")
_SaRgDeviceIanaEntry_Object = MibTableRow
saRgDeviceIanaEntry = _SaRgDeviceIanaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 7, 4, 1)
)
saRgDeviceIanaEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgDeviceIanaIndex"),
)
if mibBuilder.loadTexts:
    saRgDeviceIanaEntry.setStatus("current")


class _SaRgDeviceIanaIndex_Type(Integer32):
    """Custom type saRgDeviceIanaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SaRgDeviceIanaIndex_Type.__name__ = "Integer32"
_SaRgDeviceIanaIndex_Object = MibTableColumn
saRgDeviceIanaIndex = _SaRgDeviceIanaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 7, 4, 1, 1),
    _SaRgDeviceIanaIndex_Type()
)
saRgDeviceIanaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgDeviceIanaIndex.setStatus("current")
_SaRgDeviceIanaValue_Type = InetAddress
_SaRgDeviceIanaValue_Object = MibTableColumn
saRgDeviceIanaValue = _SaRgDeviceIanaValue_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 7, 4, 1, 2),
    _SaRgDeviceIanaValue_Type()
)
saRgDeviceIanaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIanaValue.setStatus("current")
_SaRgDeviceIanaPreferredLifetime_Type = Integer32
_SaRgDeviceIanaPreferredLifetime_Object = MibTableColumn
saRgDeviceIanaPreferredLifetime = _SaRgDeviceIanaPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 7, 4, 1, 3),
    _SaRgDeviceIanaPreferredLifetime_Type()
)
saRgDeviceIanaPreferredLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIanaPreferredLifetime.setStatus("current")
_SaRgDeviceIanaValidLifetime_Type = Integer32
_SaRgDeviceIanaValidLifetime_Object = MibTableColumn
saRgDeviceIanaValidLifetime = _SaRgDeviceIanaValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 7, 4, 1, 4),
    _SaRgDeviceIanaValidLifetime_Type()
)
saRgDeviceIanaValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIanaValidLifetime.setStatus("current")
_SaRgDeviceIapdContent_ObjectIdentity = ObjectIdentity
saRgDeviceIapdContent = _SaRgDeviceIapdContent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 8)
)
_SaRgDeviceIapdIAID_Type = Unsigned32
_SaRgDeviceIapdIAID_Object = MibScalar
saRgDeviceIapdIAID = _SaRgDeviceIapdIAID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 8, 1),
    _SaRgDeviceIapdIAID_Type()
)
saRgDeviceIapdIAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIapdIAID.setStatus("current")
_SaRgDeviceIapdT1_Type = Integer32
_SaRgDeviceIapdT1_Object = MibScalar
saRgDeviceIapdT1 = _SaRgDeviceIapdT1_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 8, 2),
    _SaRgDeviceIapdT1_Type()
)
saRgDeviceIapdT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIapdT1.setStatus("current")
_SaRgDeviceIapdT2_Type = Integer32
_SaRgDeviceIapdT2_Object = MibScalar
saRgDeviceIapdT2 = _SaRgDeviceIapdT2_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 8, 3),
    _SaRgDeviceIapdT2_Type()
)
saRgDeviceIapdT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIapdT2.setStatus("current")
_SaRgDeviceIapdTable_Object = MibTable
saRgDeviceIapdTable = _SaRgDeviceIapdTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    saRgDeviceIapdTable.setStatus("current")
_SaRgDeviceIapdEntry_Object = MibTableRow
saRgDeviceIapdEntry = _SaRgDeviceIapdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 8, 4, 1)
)
saRgDeviceIapdEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgDeviceIapdIndex"),
)
if mibBuilder.loadTexts:
    saRgDeviceIapdEntry.setStatus("current")


class _SaRgDeviceIapdIndex_Type(Integer32):
    """Custom type saRgDeviceIapdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SaRgDeviceIapdIndex_Type.__name__ = "Integer32"
_SaRgDeviceIapdIndex_Object = MibTableColumn
saRgDeviceIapdIndex = _SaRgDeviceIapdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 8, 4, 1, 1),
    _SaRgDeviceIapdIndex_Type()
)
saRgDeviceIapdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgDeviceIapdIndex.setStatus("current")
_SaRgDeviceIapdPreferredLifetime_Type = Integer32
_SaRgDeviceIapdPreferredLifetime_Object = MibTableColumn
saRgDeviceIapdPreferredLifetime = _SaRgDeviceIapdPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 8, 4, 1, 2),
    _SaRgDeviceIapdPreferredLifetime_Type()
)
saRgDeviceIapdPreferredLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIapdPreferredLifetime.setStatus("current")
_SaRgDeviceIapdValidLifetime_Type = Integer32
_SaRgDeviceIapdValidLifetime_Object = MibTableColumn
saRgDeviceIapdValidLifetime = _SaRgDeviceIapdValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 8, 4, 1, 3),
    _SaRgDeviceIapdValidLifetime_Type()
)
saRgDeviceIapdValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIapdValidLifetime.setStatus("current")
_SaRgDeviceIapdPrefixLength_Type = Integer32
_SaRgDeviceIapdPrefixLength_Object = MibTableColumn
saRgDeviceIapdPrefixLength = _SaRgDeviceIapdPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 8, 4, 1, 4),
    _SaRgDeviceIapdPrefixLength_Type()
)
saRgDeviceIapdPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIapdPrefixLength.setStatus("current")
_SaRgDeviceIapdPrefixValue_Type = InetAddress
_SaRgDeviceIapdPrefixValue_Object = MibTableColumn
saRgDeviceIapdPrefixValue = _SaRgDeviceIapdPrefixValue_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 1, 8, 4, 1, 5),
    _SaRgDeviceIapdPrefixValue_Type()
)
saRgDeviceIapdPrefixValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDeviceIapdPrefixValue.setStatus("current")
_SaRgDot11_ObjectIdentity = ObjectIdentity
saRgDot11 = _SaRgDot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2)
)
_SaRgDot11MgmtBase_ObjectIdentity = ObjectIdentity
saRgDot11MgmtBase = _SaRgDot11MgmtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 1)
)


class _SaRgDot11OnOffPushButtonTime_Type(Integer32):
    """Custom type saRgDot11OnOffPushButtonTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_SaRgDot11OnOffPushButtonTime_Type.__name__ = "Integer32"
_SaRgDot11OnOffPushButtonTime_Object = MibScalar
saRgDot11OnOffPushButtonTime = _SaRgDot11OnOffPushButtonTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 1, 20),
    _SaRgDot11OnOffPushButtonTime_Type()
)
saRgDot11OnOffPushButtonTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11OnOffPushButtonTime.setStatus("current")
if mibBuilder.loadTexts:
    saRgDot11OnOffPushButtonTime.setUnits("seconds")
_SaRgDot11Bss_ObjectIdentity = ObjectIdentity
saRgDot11Bss = _SaRgDot11Bss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2)
)
_SaRgDot11BssTable_Object = MibTable
saRgDot11BssTable = _SaRgDot11BssTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    saRgDot11BssTable.setStatus("current")
_SaRgDot11BssEntry_Object = MibTableRow
saRgDot11BssEntry = _SaRgDot11BssEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1)
)
saRgDot11BssEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    saRgDot11BssEntry.setStatus("current")
_SaRgDot11BssId_Type = PhysAddress
_SaRgDot11BssId_Object = MibTableColumn
saRgDot11BssId = _SaRgDot11BssId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1, 1),
    _SaRgDot11BssId_Type()
)
saRgDot11BssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDot11BssId.setStatus("current")


class _SaRgDot11BssEnable_Type(Integer32):
    """Custom type saRgDot11BssEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("enableOnline", 3))
    )


_SaRgDot11BssEnable_Type.__name__ = "Integer32"
_SaRgDot11BssEnable_Object = MibTableColumn
saRgDot11BssEnable = _SaRgDot11BssEnable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1, 2),
    _SaRgDot11BssEnable_Type()
)
saRgDot11BssEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11BssEnable.setStatus("current")


class _SaRgDot11BssSsid_Type(OctetString):
    """Custom type saRgDot11BssSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SaRgDot11BssSsid_Type.__name__ = "OctetString"
_SaRgDot11BssSsid_Object = MibTableColumn
saRgDot11BssSsid = _SaRgDot11BssSsid_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1, 3),
    _SaRgDot11BssSsid_Type()
)
saRgDot11BssSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11BssSsid.setStatus("current")


class _SaRgDot11BssSecurityMode_Type(Integer32):
    """Custom type saRgDot11BssSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("wep", 1),
          ("wpa2Enterprise", 5),
          ("wpa2Psk", 3),
          ("wpaEnterprise", 4),
          ("wpaPsk", 2),
          ("wpaWpa2Enterprise", 8),
          ("wpaWpa2Psk", 7))
    )


_SaRgDot11BssSecurityMode_Type.__name__ = "Integer32"
_SaRgDot11BssSecurityMode_Object = MibTableColumn
saRgDot11BssSecurityMode = _SaRgDot11BssSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1, 4),
    _SaRgDot11BssSecurityMode_Type()
)
saRgDot11BssSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11BssSecurityMode.setStatus("current")
_SaRgDot11BssClosedNetwork_Type = TruthValue
_SaRgDot11BssClosedNetwork_Object = MibTableColumn
saRgDot11BssClosedNetwork = _SaRgDot11BssClosedNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1, 5),
    _SaRgDot11BssClosedNetwork_Type()
)
saRgDot11BssClosedNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11BssClosedNetwork.setStatus("current")


class _SaRgDot11BssAccessMode_Type(Integer32):
    """Custom type saRgDot11BssAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowAny", 0),
          ("allowList", 1),
          ("denyList", 2))
    )


_SaRgDot11BssAccessMode_Type.__name__ = "Integer32"
_SaRgDot11BssAccessMode_Object = MibTableColumn
saRgDot11BssAccessMode = _SaRgDot11BssAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1, 6),
    _SaRgDot11BssAccessMode_Type()
)
saRgDot11BssAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11BssAccessMode.setStatus("current")


class _SaRgDot11BssMaxNumSta_Type(Integer32):
    """Custom type saRgDot11BssMaxNumSta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SaRgDot11BssMaxNumSta_Type.__name__ = "Integer32"
_SaRgDot11BssMaxNumSta_Object = MibTableColumn
saRgDot11BssMaxNumSta = _SaRgDot11BssMaxNumSta_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1, 11),
    _SaRgDot11BssMaxNumSta_Type()
)
saRgDot11BssMaxNumSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11BssMaxNumSta.setStatus("current")


class _SaRgDot11BssUserStatus_Type(Integer32):
    """Custom type saRgDot11BssUserStatus based on Integer32"""
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


_SaRgDot11BssUserStatus_Type.__name__ = "Integer32"
_SaRgDot11BssUserStatus_Object = MibTableColumn
saRgDot11BssUserStatus = _SaRgDot11BssUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1, 13),
    _SaRgDot11BssUserStatus_Type()
)
saRgDot11BssUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDot11BssUserStatus.setStatus("current")


class _SaRgDot11BssApIsolation_Type(Integer32):
    """Custom type saRgDot11BssApIsolation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SaRgDot11BssApIsolation_Type.__name__ = "Integer32"
_SaRgDot11BssApIsolation_Object = MibTableColumn
saRgDot11BssApIsolation = _SaRgDot11BssApIsolation_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1, 15),
    _SaRgDot11BssApIsolation_Type()
)
saRgDot11BssApIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11BssApIsolation.setStatus("current")


class _SaRgDot11BssSecSsidTrafficPriority_Type(Integer32):
    """Custom type saRgDot11BssSecSsidTrafficPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acBk", 1),
          ("disable", 0))
    )


_SaRgDot11BssSecSsidTrafficPriority_Type.__name__ = "Integer32"
_SaRgDot11BssSecSsidTrafficPriority_Object = MibTableColumn
saRgDot11BssSecSsidTrafficPriority = _SaRgDot11BssSecSsidTrafficPriority_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1, 16),
    _SaRgDot11BssSecSsidTrafficPriority_Type()
)
saRgDot11BssSecSsidTrafficPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDot11BssSecSsidTrafficPriority.setStatus("current")


class _SaRgDot11BssRejectPriSsidSta_Type(TruthValue):
    """Custom type saRgDot11BssRejectPriSsidSta based on TruthValue"""


_SaRgDot11BssRejectPriSsidSta_Object = MibTableColumn
saRgDot11BssRejectPriSsidSta = _SaRgDot11BssRejectPriSsidSta_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 1, 1, 17),
    _SaRgDot11BssRejectPriSsidSta_Type()
)
saRgDot11BssRejectPriSsidSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDot11BssRejectPriSsidSta.setStatus("current")
_SaRgDot11BssPrimary_ObjectIdentity = ObjectIdentity
saRgDot11BssPrimary = _SaRgDot11BssPrimary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 3)
)


class _SaRgDot11BssPrimarySsidType_Type(Integer32):
    """Custom type saRgDot11BssPrimarySsidType based on Integer32"""
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
        *(("mac4char-prefix", 3),
          ("mac6char", 1),
          ("mac6char-prefix", 2),
          ("prefix-force", 4))
    )


_SaRgDot11BssPrimarySsidType_Type.__name__ = "Integer32"
_SaRgDot11BssPrimarySsidType_Object = MibScalar
saRgDot11BssPrimarySsidType = _SaRgDot11BssPrimarySsidType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 3, 1),
    _SaRgDot11BssPrimarySsidType_Type()
)
saRgDot11BssPrimarySsidType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11BssPrimarySsidType.setStatus("current")


class _SaRgDot11BssPrimarySsidPrefix_Type(SnmpAdminString):
    """Custom type saRgDot11BssPrimarySsidPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SaRgDot11BssPrimarySsidPrefix_Type.__name__ = "SnmpAdminString"
_SaRgDot11BssPrimarySsidPrefix_Object = MibScalar
saRgDot11BssPrimarySsidPrefix = _SaRgDot11BssPrimarySsidPrefix_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 2, 3, 2),
    _SaRgDot11BssPrimarySsidPrefix_Type()
)
saRgDot11BssPrimarySsidPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11BssPrimarySsidPrefix.setStatus("current")
_SaRgDot11Privacy_ObjectIdentity = ObjectIdentity
saRgDot11Privacy = _SaRgDot11Privacy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3)
)
_SaRgDot11WpaTable_Object = MibTable
saRgDot11WpaTable = _SaRgDot11WpaTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    saRgDot11WpaTable.setStatus("current")
_SaRgDot11WpaEntry_Object = MibTableRow
saRgDot11WpaEntry = _SaRgDot11WpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 1, 1)
)
saRgDot11WpaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    saRgDot11WpaEntry.setStatus("current")


class _SaRgDot11WpaAlgorithm_Type(Integer32):
    """Custom type saRgDot11WpaAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 1),
          ("tkip", 0),
          ("tkipPlusAes", 2))
    )


_SaRgDot11WpaAlgorithm_Type.__name__ = "Integer32"
_SaRgDot11WpaAlgorithm_Object = MibTableColumn
saRgDot11WpaAlgorithm = _SaRgDot11WpaAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 1, 1, 1),
    _SaRgDot11WpaAlgorithm_Type()
)
saRgDot11WpaAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11WpaAlgorithm.setStatus("current")


class _SaRgDot11WpaPreSharedKey_Type(OctetString):
    """Custom type saRgDot11WpaPreSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_SaRgDot11WpaPreSharedKey_Type.__name__ = "OctetString"
_SaRgDot11WpaPreSharedKey_Object = MibTableColumn
saRgDot11WpaPreSharedKey = _SaRgDot11WpaPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 1, 1, 2),
    _SaRgDot11WpaPreSharedKey_Type()
)
saRgDot11WpaPreSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11WpaPreSharedKey.setStatus("current")
_SaRgDot11WpaGroupRekeyInterval_Type = Integer32
_SaRgDot11WpaGroupRekeyInterval_Object = MibTableColumn
saRgDot11WpaGroupRekeyInterval = _SaRgDot11WpaGroupRekeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 1, 1, 3),
    _SaRgDot11WpaGroupRekeyInterval_Type()
)
saRgDot11WpaGroupRekeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11WpaGroupRekeyInterval.setStatus("current")
if mibBuilder.loadTexts:
    saRgDot11WpaGroupRekeyInterval.setUnits("seconds")
_SaRgDot11RadiusTable_Object = MibTable
saRgDot11RadiusTable = _SaRgDot11RadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    saRgDot11RadiusTable.setStatus("current")
_SaRgDot11RadiusEntry_Object = MibTableRow
saRgDot11RadiusEntry = _SaRgDot11RadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 2, 1)
)
saRgDot11RadiusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    saRgDot11RadiusEntry.setStatus("current")


class _SaRgDot11RadiusAddressType_Type(InetAddressType):
    """Custom type saRgDot11RadiusAddressType based on InetAddressType"""


_SaRgDot11RadiusAddressType_Object = MibTableColumn
saRgDot11RadiusAddressType = _SaRgDot11RadiusAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 2, 1, 1),
    _SaRgDot11RadiusAddressType_Type()
)
saRgDot11RadiusAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11RadiusAddressType.setStatus("current")
_SaRgDot11RadiusAddress_Type = InetAddress
_SaRgDot11RadiusAddress_Object = MibTableColumn
saRgDot11RadiusAddress = _SaRgDot11RadiusAddress_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 2, 1, 2),
    _SaRgDot11RadiusAddress_Type()
)
saRgDot11RadiusAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11RadiusAddress.setStatus("current")
_SaRgDot11RadiusPort_Type = InetPortNumber
_SaRgDot11RadiusPort_Object = MibTableColumn
saRgDot11RadiusPort = _SaRgDot11RadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 2, 1, 3),
    _SaRgDot11RadiusPort_Type()
)
saRgDot11RadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11RadiusPort.setStatus("current")
_SaRgDot11RadiusKey_Type = DisplayString
_SaRgDot11RadiusKey_Object = MibTableColumn
saRgDot11RadiusKey = _SaRgDot11RadiusKey_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 2, 1, 4),
    _SaRgDot11RadiusKey_Type()
)
saRgDot11RadiusKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11RadiusKey.setStatus("current")
_SaRgDot11RadiusReAuthInterval_Type = Integer32
_SaRgDot11RadiusReAuthInterval_Object = MibTableColumn
saRgDot11RadiusReAuthInterval = _SaRgDot11RadiusReAuthInterval_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 2, 1, 5),
    _SaRgDot11RadiusReAuthInterval_Type()
)
saRgDot11RadiusReAuthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11RadiusReAuthInterval.setStatus("current")
if mibBuilder.loadTexts:
    saRgDot11RadiusReAuthInterval.setUnits("seconds")
_SaRgDot11WepTable_Object = MibTable
saRgDot11WepTable = _SaRgDot11WepTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    saRgDot11WepTable.setStatus("current")
_SaRgDot11WepEntry_Object = MibTableRow
saRgDot11WepEntry = _SaRgDot11WepEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 3, 1)
)
saRgDot11WepEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    saRgDot11WepEntry.setStatus("current")


class _SaRgDot11WepDefaultKey_Type(Integer32):
    """Custom type saRgDot11WepDefaultKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SaRgDot11WepDefaultKey_Type.__name__ = "Integer32"
_SaRgDot11WepDefaultKey_Object = MibTableColumn
saRgDot11WepDefaultKey = _SaRgDot11WepDefaultKey_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 3, 1, 1),
    _SaRgDot11WepDefaultKey_Type()
)
saRgDot11WepDefaultKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11WepDefaultKey.setStatus("current")


class _SaRgDot11WepEncryptionMode_Type(Integer32):
    """Custom type saRgDot11WepEncryptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wep128", 1),
          ("wep64", 0))
    )


_SaRgDot11WepEncryptionMode_Type.__name__ = "Integer32"
_SaRgDot11WepEncryptionMode_Object = MibTableColumn
saRgDot11WepEncryptionMode = _SaRgDot11WepEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 3, 1, 2),
    _SaRgDot11WepEncryptionMode_Type()
)
saRgDot11WepEncryptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11WepEncryptionMode.setStatus("current")


class _SaRgDot11WepPassPhrase_Type(DisplayString):
    """Custom type saRgDot11WepPassPhrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SaRgDot11WepPassPhrase_Type.__name__ = "DisplayString"
_SaRgDot11WepPassPhrase_Object = MibTableColumn
saRgDot11WepPassPhrase = _SaRgDot11WepPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 3, 1, 3),
    _SaRgDot11WepPassPhrase_Type()
)
saRgDot11WepPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11WepPassPhrase.setStatus("current")
_SaRgDot11Wep64BitKeyTable_Object = MibTable
saRgDot11Wep64BitKeyTable = _SaRgDot11Wep64BitKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    saRgDot11Wep64BitKeyTable.setStatus("current")
_SaRgDot11Wep64BitKeyEntry_Object = MibTableRow
saRgDot11Wep64BitKeyEntry = _SaRgDot11Wep64BitKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 4, 1)
)
saRgDot11Wep64BitKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SA-RG-MIB", "saRgDot11Wep64BitKeyIndex"),
)
if mibBuilder.loadTexts:
    saRgDot11Wep64BitKeyEntry.setStatus("current")


class _SaRgDot11Wep64BitKeyIndex_Type(Integer32):
    """Custom type saRgDot11Wep64BitKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SaRgDot11Wep64BitKeyIndex_Type.__name__ = "Integer32"
_SaRgDot11Wep64BitKeyIndex_Object = MibTableColumn
saRgDot11Wep64BitKeyIndex = _SaRgDot11Wep64BitKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 4, 1, 1),
    _SaRgDot11Wep64BitKeyIndex_Type()
)
saRgDot11Wep64BitKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgDot11Wep64BitKeyIndex.setStatus("current")


class _SaRgDot11Wep64BitKeyValue_Type(OctetString):
    """Custom type saRgDot11Wep64BitKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_SaRgDot11Wep64BitKeyValue_Type.__name__ = "OctetString"
_SaRgDot11Wep64BitKeyValue_Object = MibTableColumn
saRgDot11Wep64BitKeyValue = _SaRgDot11Wep64BitKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 4, 1, 2),
    _SaRgDot11Wep64BitKeyValue_Type()
)
saRgDot11Wep64BitKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11Wep64BitKeyValue.setStatus("current")
_SaRgDot11Wep128BitKeyTable_Object = MibTable
saRgDot11Wep128BitKeyTable = _SaRgDot11Wep128BitKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 5)
)
if mibBuilder.loadTexts:
    saRgDot11Wep128BitKeyTable.setStatus("current")
_SaRgDot11Wep128BitKeyEntry_Object = MibTableRow
saRgDot11Wep128BitKeyEntry = _SaRgDot11Wep128BitKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 5, 1)
)
saRgDot11Wep128BitKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SA-RG-MIB", "saRgDot11Wep128BitKeyIndex"),
)
if mibBuilder.loadTexts:
    saRgDot11Wep128BitKeyEntry.setStatus("current")


class _SaRgDot11Wep128BitKeyIndex_Type(Integer32):
    """Custom type saRgDot11Wep128BitKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SaRgDot11Wep128BitKeyIndex_Type.__name__ = "Integer32"
_SaRgDot11Wep128BitKeyIndex_Object = MibTableColumn
saRgDot11Wep128BitKeyIndex = _SaRgDot11Wep128BitKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 5, 1, 1),
    _SaRgDot11Wep128BitKeyIndex_Type()
)
saRgDot11Wep128BitKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgDot11Wep128BitKeyIndex.setStatus("current")


class _SaRgDot11Wep128BitKeyValue_Type(OctetString):
    """Custom type saRgDot11Wep128BitKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_SaRgDot11Wep128BitKeyValue_Type.__name__ = "OctetString"
_SaRgDot11Wep128BitKeyValue_Object = MibTableColumn
saRgDot11Wep128BitKeyValue = _SaRgDot11Wep128BitKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 5, 1, 2),
    _SaRgDot11Wep128BitKeyValue_Type()
)
saRgDot11Wep128BitKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11Wep128BitKeyValue.setStatus("current")
_SaRgDot11PrivacyWps_ObjectIdentity = ObjectIdentity
saRgDot11PrivacyWps = _SaRgDot11PrivacyWps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 6)
)


class _SaRgDot11PrivacyWpsPushButtonTime_Type(Integer32):
    """Custom type saRgDot11PrivacyWpsPushButtonTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SaRgDot11PrivacyWpsPushButtonTime_Type.__name__ = "Integer32"
_SaRgDot11PrivacyWpsPushButtonTime_Object = MibScalar
saRgDot11PrivacyWpsPushButtonTime = _SaRgDot11PrivacyWpsPushButtonTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 3, 6, 1),
    _SaRgDot11PrivacyWpsPushButtonTime_Type()
)
saRgDot11PrivacyWpsPushButtonTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11PrivacyWpsPushButtonTime.setStatus("current")
if mibBuilder.loadTexts:
    saRgDot11PrivacyWpsPushButtonTime.setUnits("seconds")
_SaRgDot11Client_ObjectIdentity = ObjectIdentity
saRgDot11Client = _SaRgDot11Client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 4)
)
_SaRgDot11ClientTable_Object = MibTable
saRgDot11ClientTable = _SaRgDot11ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    saRgDot11ClientTable.setStatus("current")
_SaRgDot11ClientEntry_Object = MibTableRow
saRgDot11ClientEntry = _SaRgDot11ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 4, 2, 1)
)
saRgDot11ClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SA-RG-MIB", "saRgDot11ClientIndex"),
)
if mibBuilder.loadTexts:
    saRgDot11ClientEntry.setStatus("current")


class _SaRgDot11ClientIndex_Type(Integer32):
    """Custom type saRgDot11ClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SaRgDot11ClientIndex_Type.__name__ = "Integer32"
_SaRgDot11ClientIndex_Object = MibTableColumn
saRgDot11ClientIndex = _SaRgDot11ClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 4, 2, 1, 1),
    _SaRgDot11ClientIndex_Type()
)
saRgDot11ClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgDot11ClientIndex.setStatus("current")
_SaRgDot11ClientStation_Type = MacAddress
_SaRgDot11ClientStation_Object = MibTableColumn
saRgDot11ClientStation = _SaRgDot11ClientStation_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 4, 2, 1, 2),
    _SaRgDot11ClientStation_Type()
)
saRgDot11ClientStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDot11ClientStation.setStatus("current")
_SaRgDot11ExtMgmt_ObjectIdentity = ObjectIdentity
saRgDot11ExtMgmt = _SaRgDot11ExtMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 6)
)
_SaRgDot11ExtMgmtTable_Object = MibTable
saRgDot11ExtMgmtTable = _SaRgDot11ExtMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    saRgDot11ExtMgmtTable.setStatus("current")
_SaRgDot11ExtMgmtEntry_Object = MibTableRow
saRgDot11ExtMgmtEntry = _SaRgDot11ExtMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 6, 1, 1)
)
saRgDot11ExtMgmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    saRgDot11ExtMgmtEntry.setStatus("current")


class _SaRgDot11ExtMbssUserControl_Type(Integer32):
    """Custom type saRgDot11ExtMbssUserControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
        ValueRangeConstraint(65536, 16711680),
    )


_SaRgDot11ExtMbssUserControl_Type.__name__ = "Integer32"
_SaRgDot11ExtMbssUserControl_Object = MibTableColumn
saRgDot11ExtMbssUserControl = _SaRgDot11ExtMbssUserControl_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 6, 1, 1, 15),
    _SaRgDot11ExtMbssUserControl_Type()
)
saRgDot11ExtMbssUserControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11ExtMbssUserControl.setStatus("current")
_SaRgDot11ExtMbssUseNonvol_Type = TruthValue
_SaRgDot11ExtMbssUseNonvol_Object = MibTableColumn
saRgDot11ExtMbssUseNonvol = _SaRgDot11ExtMbssUseNonvol_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 6, 1, 1, 16),
    _SaRgDot11ExtMbssUseNonvol_Type()
)
saRgDot11ExtMbssUseNonvol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11ExtMbssUseNonvol.setStatus("current")


class _SaRgDot11ExtMbssAdminControl_Type(Integer32):
    """Custom type saRgDot11ExtMbssAdminControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
        ValueRangeConstraint(65536, 16711680),
    )


_SaRgDot11ExtMbssAdminControl_Type.__name__ = "Integer32"
_SaRgDot11ExtMbssAdminControl_Object = MibTableColumn
saRgDot11ExtMbssAdminControl = _SaRgDot11ExtMbssAdminControl_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 6, 1, 1, 17),
    _SaRgDot11ExtMbssAdminControl_Type()
)
saRgDot11ExtMbssAdminControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11ExtMbssAdminControl.setStatus("current")
_SaRgDot11ExtActualChannel_Type = Integer32
_SaRgDot11ExtActualChannel_Object = MibTableColumn
saRgDot11ExtActualChannel = _SaRgDot11ExtActualChannel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 6, 1, 1, 18),
    _SaRgDot11ExtActualChannel_Type()
)
saRgDot11ExtActualChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgDot11ExtActualChannel.setStatus("current")
_SaRgDot11ApplySettings_Type = TruthValue
_SaRgDot11ApplySettings_Object = MibScalar
saRgDot11ApplySettings = _SaRgDot11ApplySettings_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 2, 1001),
    _SaRgDot11ApplySettings_Type()
)
saRgDot11ApplySettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDot11ApplySettings.setStatus("current")
_SaRgIpMgmt_ObjectIdentity = ObjectIdentity
saRgIpMgmt = _SaRgIpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3)
)
_SaRgIpMgmtLanTable_Object = MibTable
saRgIpMgmtLanTable = _SaRgIpMgmtLanTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2)
)
if mibBuilder.loadTexts:
    saRgIpMgmtLanTable.setStatus("current")
_SaRgIpMgmtLanEntry_Object = MibTableRow
saRgIpMgmtLanEntry = _SaRgIpMgmtLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1)
)
saRgIpMgmtLanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    saRgIpMgmtLanEntry.setStatus("current")


class _SaRgIpMgmtLanMode_Type(Integer32):
    """Custom type saRgIpMgmtLanMode based on Integer32"""
    defaultValue = 2

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
        *(("bridge", 1),
          ("l2tpv2-client", 3),
          ("mixed", 4),
          ("router", 2),
          ("vlan", 5))
    )


_SaRgIpMgmtLanMode_Type.__name__ = "Integer32"
_SaRgIpMgmtLanMode_Object = MibTableColumn
saRgIpMgmtLanMode = _SaRgIpMgmtLanMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1, 1),
    _SaRgIpMgmtLanMode_Type()
)
saRgIpMgmtLanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanMode.setStatus("current")
_SaRgIpMgmtLanNetwork_Type = IpAddress
_SaRgIpMgmtLanNetwork_Object = MibTableColumn
saRgIpMgmtLanNetwork = _SaRgIpMgmtLanNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1, 3),
    _SaRgIpMgmtLanNetwork_Type()
)
saRgIpMgmtLanNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanNetwork.setStatus("current")


class _SaRgIpMgmtLanNetworksAllow_Type(Integer32):
    """Custom type saRgIpMgmtLanNetworksAllow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anyClass", 2),
          ("anyPrivateClass", 1),
          ("default", 0))
    )


_SaRgIpMgmtLanNetworksAllow_Type.__name__ = "Integer32"
_SaRgIpMgmtLanNetworksAllow_Object = MibTableColumn
saRgIpMgmtLanNetworksAllow = _SaRgIpMgmtLanNetworksAllow_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1, 4),
    _SaRgIpMgmtLanNetworksAllow_Type()
)
saRgIpMgmtLanNetworksAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanNetworksAllow.setStatus("current")


class _SaRgIpMgmtLanSubnetMask_Type(IpAddress):
    """Custom type saRgIpMgmtLanSubnetMask based on IpAddress"""
    defaultHexValue = "ffffff00"


_SaRgIpMgmtLanSubnetMask_Object = MibTableColumn
saRgIpMgmtLanSubnetMask = _SaRgIpMgmtLanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1, 5),
    _SaRgIpMgmtLanSubnetMask_Type()
)
saRgIpMgmtLanSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanSubnetMask.setStatus("current")
_SaRgIpMgmtLanGateway_Type = IpAddress
_SaRgIpMgmtLanGateway_Object = MibTableColumn
saRgIpMgmtLanGateway = _SaRgIpMgmtLanGateway_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1, 7),
    _SaRgIpMgmtLanGateway_Type()
)
saRgIpMgmtLanGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanGateway.setStatus("current")


class _SaRgIpMgmtLanDhcpServer_Type(Integer32):
    """Custom type saRgIpMgmtLanDhcpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SaRgIpMgmtLanDhcpServer_Type.__name__ = "Integer32"
_SaRgIpMgmtLanDhcpServer_Object = MibTableColumn
saRgIpMgmtLanDhcpServer = _SaRgIpMgmtLanDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1, 8),
    _SaRgIpMgmtLanDhcpServer_Type()
)
saRgIpMgmtLanDhcpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanDhcpServer.setStatus("current")


class _SaRgIpMgmtLanNapt_Type(Integer32):
    """Custom type saRgIpMgmtLanNapt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SaRgIpMgmtLanNapt_Type.__name__ = "Integer32"
_SaRgIpMgmtLanNapt_Object = MibTableColumn
saRgIpMgmtLanNapt = _SaRgIpMgmtLanNapt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1, 9),
    _SaRgIpMgmtLanNapt_Type()
)
saRgIpMgmtLanNapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanNapt.setStatus("current")


class _SaRgIpMgmtLanTypeOfService_Type(Integer32):
    """Custom type saRgIpMgmtLanTypeOfService based on Integer32"""
    defaultValue = 0


_SaRgIpMgmtLanTypeOfService_Object = MibTableColumn
saRgIpMgmtLanTypeOfService = _SaRgIpMgmtLanTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1, 10),
    _SaRgIpMgmtLanTypeOfService_Type()
)
saRgIpMgmtLanTypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanTypeOfService.setStatus("current")


class _SaRgIpMgmtLanDhcp125Option_Type(Integer32):
    """Custom type saRgIpMgmtLanDhcp125Option based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("addSsidName", 1),
          ("disable", 0))
    )


_SaRgIpMgmtLanDhcp125Option_Type.__name__ = "Integer32"
_SaRgIpMgmtLanDhcp125Option_Object = MibTableColumn
saRgIpMgmtLanDhcp125Option = _SaRgIpMgmtLanDhcp125Option_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1, 11),
    _SaRgIpMgmtLanDhcp125Option_Type()
)
saRgIpMgmtLanDhcp125Option.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanDhcp125Option.setStatus("current")


class _SaRgIpMgmtLanUpnp_Type(Integer32):
    """Custom type saRgIpMgmtLanUpnp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SaRgIpMgmtLanUpnp_Type.__name__ = "Integer32"
_SaRgIpMgmtLanUpnp_Object = MibTableColumn
saRgIpMgmtLanUpnp = _SaRgIpMgmtLanUpnp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1, 13),
    _SaRgIpMgmtLanUpnp_Type()
)
saRgIpMgmtLanUpnp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanUpnp.setStatus("current")
_SaRgIpMgmtLanDhcpOption43_Type = SnmpAdminString
_SaRgIpMgmtLanDhcpOption43_Object = MibTableColumn
saRgIpMgmtLanDhcpOption43 = _SaRgIpMgmtLanDhcpOption43_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 2, 1, 14),
    _SaRgIpMgmtLanDhcpOption43_Type()
)
saRgIpMgmtLanDhcpOption43.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanDhcpOption43.setStatus("current")
_SaRgIpMgmtLanDhcpServerTable_Object = MibTable
saRgIpMgmtLanDhcpServerTable = _SaRgIpMgmtLanDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 3)
)
if mibBuilder.loadTexts:
    saRgIpMgmtLanDhcpServerTable.setStatus("current")
_SaRgIpMgmtLanDhcpServerEntry_Object = MibTableRow
saRgIpMgmtLanDhcpServerEntry = _SaRgIpMgmtLanDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 3, 1)
)
saRgIpMgmtLanDhcpServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    saRgIpMgmtLanDhcpServerEntry.setStatus("current")
_SaRgIpMgmtLanDhcpServerPoolStart_Type = IpAddress
_SaRgIpMgmtLanDhcpServerPoolStart_Object = MibTableColumn
saRgIpMgmtLanDhcpServerPoolStart = _SaRgIpMgmtLanDhcpServerPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 3, 1, 2),
    _SaRgIpMgmtLanDhcpServerPoolStart_Type()
)
saRgIpMgmtLanDhcpServerPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanDhcpServerPoolStart.setStatus("current")
_SaRgIpMgmtLanDhcpServerPoolEnd_Type = IpAddress
_SaRgIpMgmtLanDhcpServerPoolEnd_Object = MibTableColumn
saRgIpMgmtLanDhcpServerPoolEnd = _SaRgIpMgmtLanDhcpServerPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 3, 1, 4),
    _SaRgIpMgmtLanDhcpServerPoolEnd_Type()
)
saRgIpMgmtLanDhcpServerPoolEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanDhcpServerPoolEnd.setStatus("current")


class _SaRgIpMgmtLanDhcpServerLeaseTime_Type(Unsigned32):
    """Custom type saRgIpMgmtLanDhcpServerLeaseTime based on Unsigned32"""
    defaultValue = 3600


_SaRgIpMgmtLanDhcpServerLeaseTime_Object = MibTableColumn
saRgIpMgmtLanDhcpServerLeaseTime = _SaRgIpMgmtLanDhcpServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 3, 1, 5),
    _SaRgIpMgmtLanDhcpServerLeaseTime_Type()
)
saRgIpMgmtLanDhcpServerLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanDhcpServerLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    saRgIpMgmtLanDhcpServerLeaseTime.setUnits("seconds")
_SaRgIpMgmtLanAddrTable_Object = MibTable
saRgIpMgmtLanAddrTable = _SaRgIpMgmtLanAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 4)
)
if mibBuilder.loadTexts:
    saRgIpMgmtLanAddrTable.setStatus("current")
_SaRgIpMgmtLanAddrEntry_Object = MibTableRow
saRgIpMgmtLanAddrEntry = _SaRgIpMgmtLanAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 4, 1)
)
saRgIpMgmtLanAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SA-RG-MIB", "saRgIpMgmtLanAddrIndex"),
)
if mibBuilder.loadTexts:
    saRgIpMgmtLanAddrEntry.setStatus("current")


class _SaRgIpMgmtLanAddrIndex_Type(Integer32):
    """Custom type saRgIpMgmtLanAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SaRgIpMgmtLanAddrIndex_Type.__name__ = "Integer32"
_SaRgIpMgmtLanAddrIndex_Object = MibTableColumn
saRgIpMgmtLanAddrIndex = _SaRgIpMgmtLanAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 4, 1, 1),
    _SaRgIpMgmtLanAddrIndex_Type()
)
saRgIpMgmtLanAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgIpMgmtLanAddrIndex.setStatus("current")
_SaRgIpMgmtLanAddrIp_Type = IpAddress
_SaRgIpMgmtLanAddrIp_Object = MibTableColumn
saRgIpMgmtLanAddrIp = _SaRgIpMgmtLanAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 4, 1, 3),
    _SaRgIpMgmtLanAddrIp_Type()
)
saRgIpMgmtLanAddrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgIpMgmtLanAddrIp.setStatus("current")
_SaRgIpMgmtLanAddrPhysAddr_Type = PhysAddress
_SaRgIpMgmtLanAddrPhysAddr_Object = MibTableColumn
saRgIpMgmtLanAddrPhysAddr = _SaRgIpMgmtLanAddrPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 4, 1, 4),
    _SaRgIpMgmtLanAddrPhysAddr_Type()
)
saRgIpMgmtLanAddrPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgIpMgmtLanAddrPhysAddr.setStatus("current")
_SaRgIpMgmtLanAddrLeaseCreateTime_Type = DateAndTime
_SaRgIpMgmtLanAddrLeaseCreateTime_Object = MibTableColumn
saRgIpMgmtLanAddrLeaseCreateTime = _SaRgIpMgmtLanAddrLeaseCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 4, 1, 5),
    _SaRgIpMgmtLanAddrLeaseCreateTime_Type()
)
saRgIpMgmtLanAddrLeaseCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgIpMgmtLanAddrLeaseCreateTime.setStatus("current")
_SaRgIpMgmtLanAddrLeaseExpireTime_Type = DateAndTime
_SaRgIpMgmtLanAddrLeaseExpireTime_Object = MibTableColumn
saRgIpMgmtLanAddrLeaseExpireTime = _SaRgIpMgmtLanAddrLeaseExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 4, 1, 6),
    _SaRgIpMgmtLanAddrLeaseExpireTime_Type()
)
saRgIpMgmtLanAddrLeaseExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgIpMgmtLanAddrLeaseExpireTime.setStatus("current")
_SaRgIpMgmtLanAddrHostName_Type = SnmpAdminString
_SaRgIpMgmtLanAddrHostName_Object = MibTableColumn
saRgIpMgmtLanAddrHostName = _SaRgIpMgmtLanAddrHostName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 4, 1, 7),
    _SaRgIpMgmtLanAddrHostName_Type()
)
saRgIpMgmtLanAddrHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgIpMgmtLanAddrHostName.setStatus("current")
_SaRgIpMgmtLanAddrClientId_Type = SnmpAdminString
_SaRgIpMgmtLanAddrClientId_Object = MibTableColumn
saRgIpMgmtLanAddrClientId = _SaRgIpMgmtLanAddrClientId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 4, 1, 8),
    _SaRgIpMgmtLanAddrClientId_Type()
)
saRgIpMgmtLanAddrClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgIpMgmtLanAddrClientId.setStatus("current")
_SaRgIpMgmtLanAddrInterface_Type = SnmpAdminString
_SaRgIpMgmtLanAddrInterface_Object = MibTableColumn
saRgIpMgmtLanAddrInterface = _SaRgIpMgmtLanAddrInterface_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 4, 1, 9),
    _SaRgIpMgmtLanAddrInterface_Type()
)
saRgIpMgmtLanAddrInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgIpMgmtLanAddrInterface.setStatus("current")
_SaRgIpMgmtDnsServerTable_Object = MibTable
saRgIpMgmtDnsServerTable = _SaRgIpMgmtDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 5)
)
if mibBuilder.loadTexts:
    saRgIpMgmtDnsServerTable.setStatus("current")
_SaRgIpMgmtDnsServerEntry_Object = MibTableRow
saRgIpMgmtDnsServerEntry = _SaRgIpMgmtDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 5, 1)
)
saRgIpMgmtDnsServerEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgIpMgmtDnsServerOrder"),
)
if mibBuilder.loadTexts:
    saRgIpMgmtDnsServerEntry.setStatus("current")
_SaRgIpMgmtDnsServerIp_Type = IpAddress
_SaRgIpMgmtDnsServerIp_Object = MibTableColumn
saRgIpMgmtDnsServerIp = _SaRgIpMgmtDnsServerIp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 5, 1, 3),
    _SaRgIpMgmtDnsServerIp_Type()
)
saRgIpMgmtDnsServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtDnsServerIp.setStatus("current")
_SaRgIpMgmtDhcpFixedIpTable_Object = MibTable
saRgIpMgmtDhcpFixedIpTable = _SaRgIpMgmtDhcpFixedIpTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 6)
)
if mibBuilder.loadTexts:
    saRgIpMgmtDhcpFixedIpTable.setStatus("current")
_SaRgIpMgmtDhcpFixedIpEntry_Object = MibTableRow
saRgIpMgmtDhcpFixedIpEntry = _SaRgIpMgmtDhcpFixedIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 6, 1)
)
saRgIpMgmtDhcpFixedIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SA-RG-MIB", "saRgIpMgmtDhcpFixedIpIndex"),
)
if mibBuilder.loadTexts:
    saRgIpMgmtDhcpFixedIpEntry.setStatus("current")


class _SaRgIpMgmtDhcpFixedIpIndex_Type(Integer32):
    """Custom type saRgIpMgmtDhcpFixedIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SaRgIpMgmtDhcpFixedIpIndex_Type.__name__ = "Integer32"
_SaRgIpMgmtDhcpFixedIpIndex_Object = MibTableColumn
saRgIpMgmtDhcpFixedIpIndex = _SaRgIpMgmtDhcpFixedIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 6, 1, 1),
    _SaRgIpMgmtDhcpFixedIpIndex_Type()
)
saRgIpMgmtDhcpFixedIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgIpMgmtDhcpFixedIpIndex.setStatus("current")
_SaRgIpMgmtDhcpFixedIpRowStatus_Type = RowStatus
_SaRgIpMgmtDhcpFixedIpRowStatus_Object = MibTableColumn
saRgIpMgmtDhcpFixedIpRowStatus = _SaRgIpMgmtDhcpFixedIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 6, 1, 2),
    _SaRgIpMgmtDhcpFixedIpRowStatus_Type()
)
saRgIpMgmtDhcpFixedIpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtDhcpFixedIpRowStatus.setStatus("current")
_SaRgIpMgmtDhcpFixedIpAddress_Type = IpAddress
_SaRgIpMgmtDhcpFixedIpAddress_Object = MibTableColumn
saRgIpMgmtDhcpFixedIpAddress = _SaRgIpMgmtDhcpFixedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 6, 1, 4),
    _SaRgIpMgmtDhcpFixedIpAddress_Type()
)
saRgIpMgmtDhcpFixedIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtDhcpFixedIpAddress.setStatus("current")
_SaRgIpMgmtDhcpFixedIpPhysAddr_Type = PhysAddress
_SaRgIpMgmtDhcpFixedIpPhysAddr_Object = MibTableColumn
saRgIpMgmtDhcpFixedIpPhysAddr = _SaRgIpMgmtDhcpFixedIpPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 6, 1, 5),
    _SaRgIpMgmtDhcpFixedIpPhysAddr_Type()
)
saRgIpMgmtDhcpFixedIpPhysAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saRgIpMgmtDhcpFixedIpPhysAddr.setStatus("current")


class _SaRgIpMgmtDhcpFixedIpHostName_Type(SnmpAdminString):
    """Custom type saRgIpMgmtDhcpFixedIpHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SaRgIpMgmtDhcpFixedIpHostName_Type.__name__ = "SnmpAdminString"
_SaRgIpMgmtDhcpFixedIpHostName_Object = MibTableColumn
saRgIpMgmtDhcpFixedIpHostName = _SaRgIpMgmtDhcpFixedIpHostName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 6, 1, 6),
    _SaRgIpMgmtDhcpFixedIpHostName_Type()
)
saRgIpMgmtDhcpFixedIpHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtDhcpFixedIpHostName.setStatus("current")
_SaRgIpMgmtStaticRouteTable_Object = MibTable
saRgIpMgmtStaticRouteTable = _SaRgIpMgmtStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 8)
)
if mibBuilder.loadTexts:
    saRgIpMgmtStaticRouteTable.setStatus("current")
_SaRgIpMgmtStaticRouteEntry_Object = MibTableRow
saRgIpMgmtStaticRouteEntry = _SaRgIpMgmtStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 8, 1)
)
saRgIpMgmtStaticRouteEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgIpMgmtStaticRouteIndex"),
)
if mibBuilder.loadTexts:
    saRgIpMgmtStaticRouteEntry.setStatus("current")


class _SaRgIpMgmtStaticRouteIndex_Type(Integer32):
    """Custom type saRgIpMgmtStaticRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SaRgIpMgmtStaticRouteIndex_Type.__name__ = "Integer32"
_SaRgIpMgmtStaticRouteIndex_Object = MibTableColumn
saRgIpMgmtStaticRouteIndex = _SaRgIpMgmtStaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 8, 1, 1),
    _SaRgIpMgmtStaticRouteIndex_Type()
)
saRgIpMgmtStaticRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgIpMgmtStaticRouteIndex.setStatus("current")
_SaRgIpMgmtStaticRouteRowStatus_Type = RowStatus
_SaRgIpMgmtStaticRouteRowStatus_Object = MibTableColumn
saRgIpMgmtStaticRouteRowStatus = _SaRgIpMgmtStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 8, 1, 2),
    _SaRgIpMgmtStaticRouteRowStatus_Type()
)
saRgIpMgmtStaticRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtStaticRouteRowStatus.setStatus("current")
_SaRgIpMgmtStaticRouteNetwork_Type = IpAddress
_SaRgIpMgmtStaticRouteNetwork_Object = MibTableColumn
saRgIpMgmtStaticRouteNetwork = _SaRgIpMgmtStaticRouteNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 8, 1, 3),
    _SaRgIpMgmtStaticRouteNetwork_Type()
)
saRgIpMgmtStaticRouteNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtStaticRouteNetwork.setStatus("current")
_SaRgIpMgmtStaticRouteSubnetMask_Type = IpAddress
_SaRgIpMgmtStaticRouteSubnetMask_Object = MibTableColumn
saRgIpMgmtStaticRouteSubnetMask = _SaRgIpMgmtStaticRouteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 8, 1, 4),
    _SaRgIpMgmtStaticRouteSubnetMask_Type()
)
saRgIpMgmtStaticRouteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtStaticRouteSubnetMask.setStatus("current")
_SaRgIpMgmtStaticRouteGateway_Type = IpAddress
_SaRgIpMgmtStaticRouteGateway_Object = MibTableColumn
saRgIpMgmtStaticRouteGateway = _SaRgIpMgmtStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 8, 1, 5),
    _SaRgIpMgmtStaticRouteGateway_Type()
)
saRgIpMgmtStaticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtStaticRouteGateway.setStatus("current")


class _SaRgIpMgmtStaticRouteRipAdvertise_Type(TruthValue):
    """Custom type saRgIpMgmtStaticRouteRipAdvertise based on TruthValue"""


_SaRgIpMgmtStaticRouteRipAdvertise_Object = MibTableColumn
saRgIpMgmtStaticRouteRipAdvertise = _SaRgIpMgmtStaticRouteRipAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 8, 1, 6),
    _SaRgIpMgmtStaticRouteRipAdvertise_Type()
)
saRgIpMgmtStaticRouteRipAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtStaticRouteRipAdvertise.setStatus("current")
_SaRgIpMgmtWanAddr_ObjectIdentity = ObjectIdentity
saRgIpMgmtWanAddr = _SaRgIpMgmtWanAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9)
)
_SaRgIpMgmtWanAddrBase_ObjectIdentity = ObjectIdentity
saRgIpMgmtWanAddrBase = _SaRgIpMgmtWanAddrBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9, 1)
)


class _SaRgIpMgmtWanMode_Type(Integer32):
    """Custom type saRgIpMgmtWanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("dualIp", 3),
          ("static", 2))
    )


_SaRgIpMgmtWanMode_Type.__name__ = "Integer32"
_SaRgIpMgmtWanMode_Object = MibScalar
saRgIpMgmtWanMode = _SaRgIpMgmtWanMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9, 1, 1),
    _SaRgIpMgmtWanMode_Type()
)
saRgIpMgmtWanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtWanMode.setStatus("current")


class _SaRgIpMgmtWanMtu_Type(Integer32):
    """Custom type saRgIpMgmtWanMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_SaRgIpMgmtWanMtu_Type.__name__ = "Integer32"
_SaRgIpMgmtWanMtu_Object = MibScalar
saRgIpMgmtWanMtu = _SaRgIpMgmtWanMtu_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9, 1, 2),
    _SaRgIpMgmtWanMtu_Type()
)
saRgIpMgmtWanMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtWanMtu.setStatus("current")
if mibBuilder.loadTexts:
    saRgIpMgmtWanMtu.setUnits("bytes")


class _SaRgIpMgmtWanTtl_Type(Integer32):
    """Custom type saRgIpMgmtWanTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SaRgIpMgmtWanTtl_Type.__name__ = "Integer32"
_SaRgIpMgmtWanTtl_Object = MibScalar
saRgIpMgmtWanTtl = _SaRgIpMgmtWanTtl_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9, 1, 3),
    _SaRgIpMgmtWanTtl_Type()
)
saRgIpMgmtWanTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtWanTtl.setStatus("current")
if mibBuilder.loadTexts:
    saRgIpMgmtWanTtl.setUnits("hops")
_SaRgIpMgmtWanAddrStatic_ObjectIdentity = ObjectIdentity
saRgIpMgmtWanAddrStatic = _SaRgIpMgmtWanAddrStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9, 3)
)
_SaRgIpMgmtWanStaticNetwork_Type = IpAddress
_SaRgIpMgmtWanStaticNetwork_Object = MibScalar
saRgIpMgmtWanStaticNetwork = _SaRgIpMgmtWanStaticNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9, 3, 1),
    _SaRgIpMgmtWanStaticNetwork_Type()
)
saRgIpMgmtWanStaticNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtWanStaticNetwork.setStatus("current")
_SaRgIpMgmtWanStaticSubnetMask_Type = IpAddress
_SaRgIpMgmtWanStaticSubnetMask_Object = MibScalar
saRgIpMgmtWanStaticSubnetMask = _SaRgIpMgmtWanStaticSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9, 3, 2),
    _SaRgIpMgmtWanStaticSubnetMask_Type()
)
saRgIpMgmtWanStaticSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtWanStaticSubnetMask.setStatus("current")
_SaRgIpMgmtWanStaticGateway_Type = IpAddress
_SaRgIpMgmtWanStaticGateway_Object = MibScalar
saRgIpMgmtWanStaticGateway = _SaRgIpMgmtWanStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9, 3, 3),
    _SaRgIpMgmtWanStaticGateway_Type()
)
saRgIpMgmtWanStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtWanStaticGateway.setStatus("current")
_SaRgIpMgmtWanAddrDualIp_ObjectIdentity = ObjectIdentity
saRgIpMgmtWanAddrDualIp = _SaRgIpMgmtWanAddrDualIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9, 4)
)


class _SaRgIpMgmtWanDualIpAddr_Type(IpAddress):
    """Custom type saRgIpMgmtWanDualIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_SaRgIpMgmtWanDualIpAddr_Object = MibScalar
saRgIpMgmtWanDualIpAddr = _SaRgIpMgmtWanDualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9, 4, 1),
    _SaRgIpMgmtWanDualIpAddr_Type()
)
saRgIpMgmtWanDualIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgIpMgmtWanDualIpAddr.setStatus("current")


class _SaRgIpMgmtWanDualIpRipAdvertised_Type(TruthValue):
    """Custom type saRgIpMgmtWanDualIpRipAdvertised based on TruthValue"""


_SaRgIpMgmtWanDualIpRipAdvertised_Object = MibScalar
saRgIpMgmtWanDualIpRipAdvertised = _SaRgIpMgmtWanDualIpRipAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 9, 4, 2),
    _SaRgIpMgmtWanDualIpRipAdvertised_Type()
)
saRgIpMgmtWanDualIpRipAdvertised.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtWanDualIpRipAdvertised.setStatus("current")
_SaRgIpMgmtLanExtraSubnetTable_Object = MibTable
saRgIpMgmtLanExtraSubnetTable = _SaRgIpMgmtLanExtraSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 11)
)
if mibBuilder.loadTexts:
    saRgIpMgmtLanExtraSubnetTable.setStatus("current")
_SaRgIpMgmtLanExtraSubnetEntry_Object = MibTableRow
saRgIpMgmtLanExtraSubnetEntry = _SaRgIpMgmtLanExtraSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 11, 1)
)
saRgIpMgmtLanExtraSubnetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    saRgIpMgmtLanExtraSubnetEntry.setStatus("current")


class _SaRgIpMgmtLanExtraSubnetIndex_Type(Integer32):
    """Custom type saRgIpMgmtLanExtraSubnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fourthSubnet", 3),
          ("secondSubnet", 1),
          ("thirdSubnet", 2))
    )


_SaRgIpMgmtLanExtraSubnetIndex_Type.__name__ = "Integer32"
_SaRgIpMgmtLanExtraSubnetIndex_Object = MibTableColumn
saRgIpMgmtLanExtraSubnetIndex = _SaRgIpMgmtLanExtraSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 11, 1, 1),
    _SaRgIpMgmtLanExtraSubnetIndex_Type()
)
saRgIpMgmtLanExtraSubnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgIpMgmtLanExtraSubnetIndex.setStatus("current")
_SaRgIpMgmtLanExtraSubnetRowStatus_Type = RowStatus
_SaRgIpMgmtLanExtraSubnetRowStatus_Object = MibTableColumn
saRgIpMgmtLanExtraSubnetRowStatus = _SaRgIpMgmtLanExtraSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 11, 1, 2),
    _SaRgIpMgmtLanExtraSubnetRowStatus_Type()
)
saRgIpMgmtLanExtraSubnetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanExtraSubnetRowStatus.setStatus("current")
_SaRgIpMgmtLanExtraSubnetIpAddress_Type = IpAddress
_SaRgIpMgmtLanExtraSubnetIpAddress_Object = MibTableColumn
saRgIpMgmtLanExtraSubnetIpAddress = _SaRgIpMgmtLanExtraSubnetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 11, 1, 3),
    _SaRgIpMgmtLanExtraSubnetIpAddress_Type()
)
saRgIpMgmtLanExtraSubnetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanExtraSubnetIpAddress.setStatus("current")


class _SaRgIpMgmtLanExtraSubnetSubnetMask_Type(IpAddress):
    """Custom type saRgIpMgmtLanExtraSubnetSubnetMask based on IpAddress"""
    defaultHexValue = "ffffff00"


_SaRgIpMgmtLanExtraSubnetSubnetMask_Object = MibTableColumn
saRgIpMgmtLanExtraSubnetSubnetMask = _SaRgIpMgmtLanExtraSubnetSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 11, 1, 4),
    _SaRgIpMgmtLanExtraSubnetSubnetMask_Type()
)
saRgIpMgmtLanExtraSubnetSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanExtraSubnetSubnetMask.setStatus("current")
_SaRgIpMgmtLanExtraSubnetGateway_Type = IpAddress
_SaRgIpMgmtLanExtraSubnetGateway_Object = MibTableColumn
saRgIpMgmtLanExtraSubnetGateway = _SaRgIpMgmtLanExtraSubnetGateway_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 11, 1, 5),
    _SaRgIpMgmtLanExtraSubnetGateway_Type()
)
saRgIpMgmtLanExtraSubnetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanExtraSubnetGateway.setStatus("current")
_SaRgIpMgmtLanPortControl_ObjectIdentity = ObjectIdentity
saRgIpMgmtLanPortControl = _SaRgIpMgmtLanPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 13)
)
_SaRgIpMgmtLanPortControlTable_Object = MibTable
saRgIpMgmtLanPortControlTable = _SaRgIpMgmtLanPortControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 13, 1)
)
if mibBuilder.loadTexts:
    saRgIpMgmtLanPortControlTable.setStatus("current")
_SaRgIpMgmtLanPortControlEntry_Object = MibTableRow
saRgIpMgmtLanPortControlEntry = _SaRgIpMgmtLanPortControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 13, 1, 1)
)
saRgIpMgmtLanPortControlEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgIpMgmtLanPortControlIndex"),
)
if mibBuilder.loadTexts:
    saRgIpMgmtLanPortControlEntry.setStatus("current")


class _SaRgIpMgmtLanPortControlIndex_Type(Integer32):
    """Custom type saRgIpMgmtLanPortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SaRgIpMgmtLanPortControlIndex_Type.__name__ = "Integer32"
_SaRgIpMgmtLanPortControlIndex_Object = MibTableColumn
saRgIpMgmtLanPortControlIndex = _SaRgIpMgmtLanPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 13, 1, 1, 1),
    _SaRgIpMgmtLanPortControlIndex_Type()
)
saRgIpMgmtLanPortControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgIpMgmtLanPortControlIndex.setStatus("current")


class _SaRgIpMgmtLanPortMode_Type(Integer32):
    """Custom type saRgIpMgmtLanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("router", 2))
    )


_SaRgIpMgmtLanPortMode_Type.__name__ = "Integer32"
_SaRgIpMgmtLanPortMode_Object = MibTableColumn
saRgIpMgmtLanPortMode = _SaRgIpMgmtLanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 13, 1, 1, 2),
    _SaRgIpMgmtLanPortMode_Type()
)
saRgIpMgmtLanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtLanPortMode.setStatus("current")
_SaRgIpMgmtApplySettings_Type = TruthValue
_SaRgIpMgmtApplySettings_Object = MibScalar
saRgIpMgmtApplySettings = _SaRgIpMgmtApplySettings_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 3, 1001),
    _SaRgIpMgmtApplySettings_Type()
)
saRgIpMgmtApplySettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgIpMgmtApplySettings.setStatus("current")
_SaRgFirewall_ObjectIdentity = ObjectIdentity
saRgFirewall = _SaRgFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4)
)
_SaRgFirewallReport_ObjectIdentity = ObjectIdentity
saRgFirewallReport = _SaRgFirewallReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4)
)
_SaRgFirewallReportEventTable_Object = MibTable
saRgFirewallReportEventTable = _SaRgFirewallReportEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    saRgFirewallReportEventTable.setStatus("current")
_SaRgFirewallReportEventEntry_Object = MibTableRow
saRgFirewallReportEventEntry = _SaRgFirewallReportEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 1, 1)
)
saRgFirewallReportEventEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgFirewallReportEventIndex"),
)
if mibBuilder.loadTexts:
    saRgFirewallReportEventEntry.setStatus("current")


class _SaRgFirewallReportEventIndex_Type(Integer32):
    """Custom type saRgFirewallReportEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SaRgFirewallReportEventIndex_Type.__name__ = "Integer32"
_SaRgFirewallReportEventIndex_Object = MibTableColumn
saRgFirewallReportEventIndex = _SaRgFirewallReportEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 1, 1, 1),
    _SaRgFirewallReportEventIndex_Type()
)
saRgFirewallReportEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgFirewallReportEventIndex.setStatus("current")
_SaRgFirewallReportEventDescription_Type = SnmpAdminString
_SaRgFirewallReportEventDescription_Object = MibTableColumn
saRgFirewallReportEventDescription = _SaRgFirewallReportEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 1, 1, 2),
    _SaRgFirewallReportEventDescription_Type()
)
saRgFirewallReportEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgFirewallReportEventDescription.setStatus("current")
_SaRgFirewallReportEventCount_Type = Integer32
_SaRgFirewallReportEventCount_Object = MibTableColumn
saRgFirewallReportEventCount = _SaRgFirewallReportEventCount_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 1, 1, 3),
    _SaRgFirewallReportEventCount_Type()
)
saRgFirewallReportEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgFirewallReportEventCount.setStatus("current")
_SaRgFirewallReportEventLastOccurance_Type = SnmpAdminString
_SaRgFirewallReportEventLastOccurance_Object = MibTableColumn
saRgFirewallReportEventLastOccurance = _SaRgFirewallReportEventLastOccurance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 1, 1, 4),
    _SaRgFirewallReportEventLastOccurance_Type()
)
saRgFirewallReportEventLastOccurance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgFirewallReportEventLastOccurance.setStatus("current")
_SaRgFirewallReportEventTarget_Type = SnmpAdminString
_SaRgFirewallReportEventTarget_Object = MibTableColumn
saRgFirewallReportEventTarget = _SaRgFirewallReportEventTarget_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 1, 1, 5),
    _SaRgFirewallReportEventTarget_Type()
)
saRgFirewallReportEventTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgFirewallReportEventTarget.setStatus("current")
_SaRgFirewallReportEventSource_Type = SnmpAdminString
_SaRgFirewallReportEventSource_Object = MibTableColumn
saRgFirewallReportEventSource = _SaRgFirewallReportEventSource_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 1, 1, 6),
    _SaRgFirewallReportEventSource_Type()
)
saRgFirewallReportEventSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saRgFirewallReportEventSource.setStatus("current")
_SaRgFirewallReportMgmt_ObjectIdentity = ObjectIdentity
saRgFirewallReportMgmt = _SaRgFirewallReportMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 2)
)


class _SaRgFirewallReportMgmtClearLog_Type(TruthValue):
    """Custom type saRgFirewallReportMgmtClearLog based on TruthValue"""


_SaRgFirewallReportMgmtClearLog_Object = MibScalar
saRgFirewallReportMgmtClearLog = _SaRgFirewallReportMgmtClearLog_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 2, 1),
    _SaRgFirewallReportMgmtClearLog_Type()
)
saRgFirewallReportMgmtClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallReportMgmtClearLog.setStatus("current")


class _SaRgFirewallReportEmailLogNow_Type(TruthValue):
    """Custom type saRgFirewallReportEmailLogNow based on TruthValue"""


_SaRgFirewallReportEmailLogNow_Object = MibScalar
saRgFirewallReportEmailLogNow = _SaRgFirewallReportEmailLogNow_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 2, 2),
    _SaRgFirewallReportEmailLogNow_Type()
)
saRgFirewallReportEmailLogNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallReportEmailLogNow.setStatus("current")
_SaRgFirewallReportEmail_ObjectIdentity = ObjectIdentity
saRgFirewallReportEmail = _SaRgFirewallReportEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 3)
)
_SaRgFirewallReportEmailEnable_Type = TruthValue
_SaRgFirewallReportEmailEnable_Object = MibScalar
saRgFirewallReportEmailEnable = _SaRgFirewallReportEmailEnable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 3, 1),
    _SaRgFirewallReportEmailEnable_Type()
)
saRgFirewallReportEmailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallReportEmailEnable.setStatus("current")
_SaRgFirewallReportEmailAddress_Type = SnmpAdminString
_SaRgFirewallReportEmailAddress_Object = MibScalar
saRgFirewallReportEmailAddress = _SaRgFirewallReportEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 3, 2),
    _SaRgFirewallReportEmailAddress_Type()
)
saRgFirewallReportEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallReportEmailAddress.setStatus("current")
_SaRgFirewallReportEmailSmtpServer_Type = SnmpAdminString
_SaRgFirewallReportEmailSmtpServer_Object = MibScalar
saRgFirewallReportEmailSmtpServer = _SaRgFirewallReportEmailSmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 3, 3),
    _SaRgFirewallReportEmailSmtpServer_Type()
)
saRgFirewallReportEmailSmtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallReportEmailSmtpServer.setStatus("current")
_SaRgFirewallReportEmailUsername_Type = SnmpAdminString
_SaRgFirewallReportEmailUsername_Object = MibScalar
saRgFirewallReportEmailUsername = _SaRgFirewallReportEmailUsername_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 3, 4),
    _SaRgFirewallReportEmailUsername_Type()
)
saRgFirewallReportEmailUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallReportEmailUsername.setStatus("current")
_SaRgFirewallReportEmailPassword_Type = SnmpAdminString
_SaRgFirewallReportEmailPassword_Object = MibScalar
saRgFirewallReportEmailPassword = _SaRgFirewallReportEmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 4, 3, 5),
    _SaRgFirewallReportEmailPassword_Type()
)
saRgFirewallReportEmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallReportEmailPassword.setStatus("current")
_SaRgFirewallRules_ObjectIdentity = ObjectIdentity
saRgFirewallRules = _SaRgFirewallRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5)
)
_SaRgFirewallIpFilterTable_Object = MibTable
saRgFirewallIpFilterTable = _SaRgFirewallIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    saRgFirewallIpFilterTable.setStatus("current")
_SaRgFirewallIpFilterEntry_Object = MibTableRow
saRgFirewallIpFilterEntry = _SaRgFirewallIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 1, 1)
)
saRgFirewallIpFilterEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgFirewallIpFilterIndex"),
)
if mibBuilder.loadTexts:
    saRgFirewallIpFilterEntry.setStatus("current")


class _SaRgFirewallIpFilterIndex_Type(Integer32):
    """Custom type saRgFirewallIpFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SaRgFirewallIpFilterIndex_Type.__name__ = "Integer32"
_SaRgFirewallIpFilterIndex_Object = MibTableColumn
saRgFirewallIpFilterIndex = _SaRgFirewallIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 1, 1, 1),
    _SaRgFirewallIpFilterIndex_Type()
)
saRgFirewallIpFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgFirewallIpFilterIndex.setStatus("current")
_SaRgFirewallIpFilterRowStatus_Type = RowStatus
_SaRgFirewallIpFilterRowStatus_Object = MibTableColumn
saRgFirewallIpFilterRowStatus = _SaRgFirewallIpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 1, 1, 2),
    _SaRgFirewallIpFilterRowStatus_Type()
)
saRgFirewallIpFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallIpFilterRowStatus.setStatus("current")
_SaRgFirewallIpFilterAddressStart_Type = IpAddress
_SaRgFirewallIpFilterAddressStart_Object = MibTableColumn
saRgFirewallIpFilterAddressStart = _SaRgFirewallIpFilterAddressStart_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 1, 1, 3),
    _SaRgFirewallIpFilterAddressStart_Type()
)
saRgFirewallIpFilterAddressStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallIpFilterAddressStart.setStatus("current")
_SaRgFirewallIpFilterAddressEnd_Type = IpAddress
_SaRgFirewallIpFilterAddressEnd_Object = MibTableColumn
saRgFirewallIpFilterAddressEnd = _SaRgFirewallIpFilterAddressEnd_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 1, 1, 4),
    _SaRgFirewallIpFilterAddressEnd_Type()
)
saRgFirewallIpFilterAddressEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallIpFilterAddressEnd.setStatus("current")
_SaRgFirewallPortFilterTable_Object = MibTable
saRgFirewallPortFilterTable = _SaRgFirewallPortFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 2)
)
if mibBuilder.loadTexts:
    saRgFirewallPortFilterTable.setStatus("current")
_SaRgFirewallPortFilterEntry_Object = MibTableRow
saRgFirewallPortFilterEntry = _SaRgFirewallPortFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 2, 1)
)
saRgFirewallPortFilterEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgFirewallPortFilterIndex"),
)
if mibBuilder.loadTexts:
    saRgFirewallPortFilterEntry.setStatus("current")


class _SaRgFirewallPortFilterIndex_Type(Integer32):
    """Custom type saRgFirewallPortFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SaRgFirewallPortFilterIndex_Type.__name__ = "Integer32"
_SaRgFirewallPortFilterIndex_Object = MibTableColumn
saRgFirewallPortFilterIndex = _SaRgFirewallPortFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 2, 1, 1),
    _SaRgFirewallPortFilterIndex_Type()
)
saRgFirewallPortFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgFirewallPortFilterIndex.setStatus("current")
_SaRgFirewallPortFilterRowStatus_Type = RowStatus
_SaRgFirewallPortFilterRowStatus_Object = MibTableColumn
saRgFirewallPortFilterRowStatus = _SaRgFirewallPortFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 2, 1, 2),
    _SaRgFirewallPortFilterRowStatus_Type()
)
saRgFirewallPortFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortFilterRowStatus.setStatus("current")
_SaRgFirewallPortFilterPortStart_Type = InetPortNumber
_SaRgFirewallPortFilterPortStart_Object = MibTableColumn
saRgFirewallPortFilterPortStart = _SaRgFirewallPortFilterPortStart_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 2, 1, 5),
    _SaRgFirewallPortFilterPortStart_Type()
)
saRgFirewallPortFilterPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortFilterPortStart.setStatus("current")
_SaRgFirewallPortFilterPortEnd_Type = InetPortNumber
_SaRgFirewallPortFilterPortEnd_Object = MibTableColumn
saRgFirewallPortFilterPortEnd = _SaRgFirewallPortFilterPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 2, 1, 6),
    _SaRgFirewallPortFilterPortEnd_Type()
)
saRgFirewallPortFilterPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortFilterPortEnd.setStatus("current")


class _SaRgFirewallPortFilterProto_Type(Integer32):
    """Custom type saRgFirewallPortFilterProto based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1),
          ("udpTcp", 3))
    )


_SaRgFirewallPortFilterProto_Type.__name__ = "Integer32"
_SaRgFirewallPortFilterProto_Object = MibTableColumn
saRgFirewallPortFilterProto = _SaRgFirewallPortFilterProto_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 2, 1, 7),
    _SaRgFirewallPortFilterProto_Type()
)
saRgFirewallPortFilterProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortFilterProto.setStatus("current")
_SaRgFirewallMacFilterTable_Object = MibTable
saRgFirewallMacFilterTable = _SaRgFirewallMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 3)
)
if mibBuilder.loadTexts:
    saRgFirewallMacFilterTable.setStatus("current")
_SaRgFirewallMacFilterEntry_Object = MibTableRow
saRgFirewallMacFilterEntry = _SaRgFirewallMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 3, 1)
)
saRgFirewallMacFilterEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgFirewallMacFilterIndex"),
)
if mibBuilder.loadTexts:
    saRgFirewallMacFilterEntry.setStatus("current")


class _SaRgFirewallMacFilterIndex_Type(Integer32):
    """Custom type saRgFirewallMacFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SaRgFirewallMacFilterIndex_Type.__name__ = "Integer32"
_SaRgFirewallMacFilterIndex_Object = MibTableColumn
saRgFirewallMacFilterIndex = _SaRgFirewallMacFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 3, 1, 1),
    _SaRgFirewallMacFilterIndex_Type()
)
saRgFirewallMacFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgFirewallMacFilterIndex.setStatus("current")
_SaRgFirewallMacFilterRowStatus_Type = RowStatus
_SaRgFirewallMacFilterRowStatus_Object = MibTableColumn
saRgFirewallMacFilterRowStatus = _SaRgFirewallMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 3, 1, 2),
    _SaRgFirewallMacFilterRowStatus_Type()
)
saRgFirewallMacFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallMacFilterRowStatus.setStatus("current")
_SaRgFirewallMacFilterAddress_Type = MacAddress
_SaRgFirewallMacFilterAddress_Object = MibTableColumn
saRgFirewallMacFilterAddress = _SaRgFirewallMacFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 3, 1, 3),
    _SaRgFirewallMacFilterAddress_Type()
)
saRgFirewallMacFilterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallMacFilterAddress.setStatus("current")


class _SaRgFirewallMacFilterEnable_Type(TruthValue):
    """Custom type saRgFirewallMacFilterEnable based on TruthValue"""


_SaRgFirewallMacFilterEnable_Object = MibScalar
saRgFirewallMacFilterEnable = _SaRgFirewallMacFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 4),
    _SaRgFirewallMacFilterEnable_Type()
)
saRgFirewallMacFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallMacFilterEnable.setStatus("current")


class _SaRgFirewallMacFilterMode_Type(Integer32):
    """Custom type saRgFirewallMacFilterMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("permit", 1))
    )


_SaRgFirewallMacFilterMode_Type.__name__ = "Integer32"
_SaRgFirewallMacFilterMode_Object = MibScalar
saRgFirewallMacFilterMode = _SaRgFirewallMacFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 5, 5),
    _SaRgFirewallMacFilterMode_Type()
)
saRgFirewallMacFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallMacFilterMode.setStatus("current")
_SaRgFirewallPortFwdTable_Object = MibTable
saRgFirewallPortFwdTable = _SaRgFirewallPortFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 6)
)
if mibBuilder.loadTexts:
    saRgFirewallPortFwdTable.setStatus("current")
_SaRgFirewallPortFwdEntry_Object = MibTableRow
saRgFirewallPortFwdEntry = _SaRgFirewallPortFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 6, 1)
)
saRgFirewallPortFwdEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgFirewallPortFwdIndex"),
)
if mibBuilder.loadTexts:
    saRgFirewallPortFwdEntry.setStatus("current")


class _SaRgFirewallPortFwdIndex_Type(Integer32):
    """Custom type saRgFirewallPortFwdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SaRgFirewallPortFwdIndex_Type.__name__ = "Integer32"
_SaRgFirewallPortFwdIndex_Object = MibTableColumn
saRgFirewallPortFwdIndex = _SaRgFirewallPortFwdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 6, 1, 1),
    _SaRgFirewallPortFwdIndex_Type()
)
saRgFirewallPortFwdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgFirewallPortFwdIndex.setStatus("current")
_SaRgFirewallPortFwdRowStatus_Type = RowStatus
_SaRgFirewallPortFwdRowStatus_Object = MibTableColumn
saRgFirewallPortFwdRowStatus = _SaRgFirewallPortFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 6, 1, 2),
    _SaRgFirewallPortFwdRowStatus_Type()
)
saRgFirewallPortFwdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortFwdRowStatus.setStatus("current")
_SaRgFirewallPortFwdToAddress_Type = IpAddress
_SaRgFirewallPortFwdToAddress_Object = MibTableColumn
saRgFirewallPortFwdToAddress = _SaRgFirewallPortFwdToAddress_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 6, 1, 3),
    _SaRgFirewallPortFwdToAddress_Type()
)
saRgFirewallPortFwdToAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortFwdToAddress.setStatus("current")
_SaRgFirewallPortFwdPortStart_Type = InetPortNumber
_SaRgFirewallPortFwdPortStart_Object = MibTableColumn
saRgFirewallPortFwdPortStart = _SaRgFirewallPortFwdPortStart_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 6, 1, 4),
    _SaRgFirewallPortFwdPortStart_Type()
)
saRgFirewallPortFwdPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortFwdPortStart.setStatus("current")
_SaRgFirewallPortFwdPortEnd_Type = InetPortNumber
_SaRgFirewallPortFwdPortEnd_Object = MibTableColumn
saRgFirewallPortFwdPortEnd = _SaRgFirewallPortFwdPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 6, 1, 5),
    _SaRgFirewallPortFwdPortEnd_Type()
)
saRgFirewallPortFwdPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortFwdPortEnd.setStatus("current")


class _SaRgFirewallPortFwdProto_Type(Integer32):
    """Custom type saRgFirewallPortFwdProto based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1),
          ("udpTcp", 3))
    )


_SaRgFirewallPortFwdProto_Type.__name__ = "Integer32"
_SaRgFirewallPortFwdProto_Object = MibTableColumn
saRgFirewallPortFwdProto = _SaRgFirewallPortFwdProto_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 6, 1, 6),
    _SaRgFirewallPortFwdProto_Type()
)
saRgFirewallPortFwdProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortFwdProto.setStatus("current")
_SaRgFirewallPortFwdExternalPortStart_Type = InetPortNumber
_SaRgFirewallPortFwdExternalPortStart_Object = MibTableColumn
saRgFirewallPortFwdExternalPortStart = _SaRgFirewallPortFwdExternalPortStart_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 6, 1, 8),
    _SaRgFirewallPortFwdExternalPortStart_Type()
)
saRgFirewallPortFwdExternalPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortFwdExternalPortStart.setStatus("current")
_SaRgFirewallPortFwdExternalPortEnd_Type = InetPortNumber
_SaRgFirewallPortFwdExternalPortEnd_Object = MibTableColumn
saRgFirewallPortFwdExternalPortEnd = _SaRgFirewallPortFwdExternalPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 6, 1, 9),
    _SaRgFirewallPortFwdExternalPortEnd_Type()
)
saRgFirewallPortFwdExternalPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortFwdExternalPortEnd.setStatus("current")
_SaRgFirewallPortTrigTable_Object = MibTable
saRgFirewallPortTrigTable = _SaRgFirewallPortTrigTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 7)
)
if mibBuilder.loadTexts:
    saRgFirewallPortTrigTable.setStatus("current")
_SaRgFirewallPortTrigEntry_Object = MibTableRow
saRgFirewallPortTrigEntry = _SaRgFirewallPortTrigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 7, 1)
)
saRgFirewallPortTrigEntry.setIndexNames(
    (0, "SA-RG-MIB", "saRgFirewallPortTrigIndex"),
)
if mibBuilder.loadTexts:
    saRgFirewallPortTrigEntry.setStatus("current")


class _SaRgFirewallPortTrigIndex_Type(Integer32):
    """Custom type saRgFirewallPortTrigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SaRgFirewallPortTrigIndex_Type.__name__ = "Integer32"
_SaRgFirewallPortTrigIndex_Object = MibTableColumn
saRgFirewallPortTrigIndex = _SaRgFirewallPortTrigIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 7, 1, 1),
    _SaRgFirewallPortTrigIndex_Type()
)
saRgFirewallPortTrigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saRgFirewallPortTrigIndex.setStatus("current")
_SaRgFirewallPortTrigRowStatus_Type = RowStatus
_SaRgFirewallPortTrigRowStatus_Object = MibTableColumn
saRgFirewallPortTrigRowStatus = _SaRgFirewallPortTrigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 7, 1, 2),
    _SaRgFirewallPortTrigRowStatus_Type()
)
saRgFirewallPortTrigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortTrigRowStatus.setStatus("current")
_SaRgFirewallPortTrigTriggerPortStart_Type = InetPortNumber
_SaRgFirewallPortTrigTriggerPortStart_Object = MibTableColumn
saRgFirewallPortTrigTriggerPortStart = _SaRgFirewallPortTrigTriggerPortStart_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 7, 1, 3),
    _SaRgFirewallPortTrigTriggerPortStart_Type()
)
saRgFirewallPortTrigTriggerPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortTrigTriggerPortStart.setStatus("current")
_SaRgFirewallPortTrigTriggerPortEnd_Type = InetPortNumber
_SaRgFirewallPortTrigTriggerPortEnd_Object = MibTableColumn
saRgFirewallPortTrigTriggerPortEnd = _SaRgFirewallPortTrigTriggerPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 7, 1, 4),
    _SaRgFirewallPortTrigTriggerPortEnd_Type()
)
saRgFirewallPortTrigTriggerPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortTrigTriggerPortEnd.setStatus("current")
_SaRgFirewallPortTrigTargetPortStart_Type = InetPortNumber
_SaRgFirewallPortTrigTargetPortStart_Object = MibTableColumn
saRgFirewallPortTrigTargetPortStart = _SaRgFirewallPortTrigTargetPortStart_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 7, 1, 5),
    _SaRgFirewallPortTrigTargetPortStart_Type()
)
saRgFirewallPortTrigTargetPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortTrigTargetPortStart.setStatus("current")
_SaRgFirewallPortTrigTargetPortEnd_Type = InetPortNumber
_SaRgFirewallPortTrigTargetPortEnd_Object = MibTableColumn
saRgFirewallPortTrigTargetPortEnd = _SaRgFirewallPortTrigTargetPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 7, 1, 6),
    _SaRgFirewallPortTrigTargetPortEnd_Type()
)
saRgFirewallPortTrigTargetPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortTrigTargetPortEnd.setStatus("current")


class _SaRgFirewallPortTrigProto_Type(Integer32):
    """Custom type saRgFirewallPortTrigProto based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 1),
          ("udpTcp", 3))
    )


_SaRgFirewallPortTrigProto_Type.__name__ = "Integer32"
_SaRgFirewallPortTrigProto_Object = MibTableColumn
saRgFirewallPortTrigProto = _SaRgFirewallPortTrigProto_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 7, 1, 7),
    _SaRgFirewallPortTrigProto_Type()
)
saRgFirewallPortTrigProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallPortTrigProto.setStatus("current")
_SaRgFirewallApplySettings_Type = TruthValue
_SaRgFirewallApplySettings_Object = MibScalar
saRgFirewallApplySettings = _SaRgFirewallApplySettings_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 4, 1001),
    _SaRgFirewallApplySettings_Type()
)
saRgFirewallApplySettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgFirewallApplySettings.setStatus("current")
_SaRgDslite_ObjectIdentity = ObjectIdentity
saRgDslite = _SaRgDslite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 12)
)


class _SaRgDsliteOption_Type(Integer32):
    """Custom type saRgDsliteOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("option-64", 1))
    )


_SaRgDsliteOption_Type.__name__ = "Integer32"
_SaRgDsliteOption_Object = MibScalar
saRgDsliteOption = _SaRgDsliteOption_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 12, 1),
    _SaRgDsliteOption_Type()
)
saRgDsliteOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDsliteOption.setStatus("current")
_SaRgDsliteAftrName_Type = SnmpAdminString
_SaRgDsliteAftrName_Object = MibScalar
saRgDsliteAftrName = _SaRgDsliteAftrName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 12, 2),
    _SaRgDsliteAftrName_Type()
)
saRgDsliteAftrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDsliteAftrName.setStatus("current")
_SaRgDsliteAftrAddress_Type = InetAddressIPv6
_SaRgDsliteAftrAddress_Object = MibScalar
saRgDsliteAftrAddress = _SaRgDsliteAftrAddress_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 12, 3),
    _SaRgDsliteAftrAddress_Type()
)
saRgDsliteAftrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDsliteAftrAddress.setStatus("current")


class _SaRgDsliteTcpMssClamping_Type(Integer32):
    """Custom type saRgDsliteTcpMssClamping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1420),
    )


_SaRgDsliteTcpMssClamping_Type.__name__ = "Integer32"
_SaRgDsliteTcpMssClamping_Object = MibScalar
saRgDsliteTcpMssClamping = _SaRgDsliteTcpMssClamping_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 12, 4),
    _SaRgDsliteTcpMssClamping_Type()
)
saRgDsliteTcpMssClamping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDsliteTcpMssClamping.setStatus("current")
_SaRgDsliteApplySettings_Type = TruthValue
_SaRgDsliteApplySettings_Object = MibScalar
saRgDsliteApplySettings = _SaRgDsliteApplySettings_Object(
    (1, 3, 6, 1, 4, 1, 1429, 79, 2, 12, 1001),
    _SaRgDsliteApplySettings_Type()
)
saRgDsliteApplySettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saRgDsliteApplySettings.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SA-RG-MIB",
    **{"SaRgTimeZone": SaRgTimeZone,
       "sa": sa,
       "saModules": saModules,
       "saRg": saRg,
       "saRgDevice": saRgDevice,
       "saRgDeviceBase": saRgDeviceBase,
       "saRgDeviceMode": saRgDeviceMode,
       "saRgDeviceResetDefaultEnable": saRgDeviceResetDefaultEnable,
       "saRgDeviceRemoteWebAccessPort": saRgDeviceRemoteWebAccessPort,
       "saRgDeviceLanLanIsolation": saRgDeviceLanLanIsolation,
       "saRgDeviceLanWlanIsolation": saRgDeviceLanWlanIsolation,
       "saRgDeviceIpv6Trans": saRgDeviceIpv6Trans,
       "saRgDeviceIpv6Passthrough": saRgDeviceIpv6Passthrough,
       "saRgDeviceFactoryReset": saRgDeviceFactoryReset,
       "saRgDeviceTimeSetup": saRgDeviceTimeSetup,
       "saRgDeviceTimeSetupNtpEnabled": saRgDeviceTimeSetupNtpEnabled,
       "saRgDeviceTimeSetupNtpServerTable": saRgDeviceTimeSetupNtpServerTable,
       "saRgDeviceTimeSetupNtpServerEntry": saRgDeviceTimeSetupNtpServerEntry,
       "saRgDeviceTimeSetupNtpServerIndex": saRgDeviceTimeSetupNtpServerIndex,
       "saRgDeviceTimeSetupNtpServerAddress": saRgDeviceTimeSetupNtpServerAddress,
       "saRgDeviceTimeSetupZone": saRgDeviceTimeSetupZone,
       "saRgDeviceTimeSetupDst": saRgDeviceTimeSetupDst,
       "saRgDeviceIanaContent": saRgDeviceIanaContent,
       "saRgDeviceIanaIAID": saRgDeviceIanaIAID,
       "saRgDeviceIanaT1": saRgDeviceIanaT1,
       "saRgDeviceIanaT2": saRgDeviceIanaT2,
       "saRgDeviceIanaTable": saRgDeviceIanaTable,
       "saRgDeviceIanaEntry": saRgDeviceIanaEntry,
       "saRgDeviceIanaIndex": saRgDeviceIanaIndex,
       "saRgDeviceIanaValue": saRgDeviceIanaValue,
       "saRgDeviceIanaPreferredLifetime": saRgDeviceIanaPreferredLifetime,
       "saRgDeviceIanaValidLifetime": saRgDeviceIanaValidLifetime,
       "saRgDeviceIapdContent": saRgDeviceIapdContent,
       "saRgDeviceIapdIAID": saRgDeviceIapdIAID,
       "saRgDeviceIapdT1": saRgDeviceIapdT1,
       "saRgDeviceIapdT2": saRgDeviceIapdT2,
       "saRgDeviceIapdTable": saRgDeviceIapdTable,
       "saRgDeviceIapdEntry": saRgDeviceIapdEntry,
       "saRgDeviceIapdIndex": saRgDeviceIapdIndex,
       "saRgDeviceIapdPreferredLifetime": saRgDeviceIapdPreferredLifetime,
       "saRgDeviceIapdValidLifetime": saRgDeviceIapdValidLifetime,
       "saRgDeviceIapdPrefixLength": saRgDeviceIapdPrefixLength,
       "saRgDeviceIapdPrefixValue": saRgDeviceIapdPrefixValue,
       "saRgDot11": saRgDot11,
       "saRgDot11MgmtBase": saRgDot11MgmtBase,
       "saRgDot11OnOffPushButtonTime": saRgDot11OnOffPushButtonTime,
       "saRgDot11Bss": saRgDot11Bss,
       "saRgDot11BssTable": saRgDot11BssTable,
       "saRgDot11BssEntry": saRgDot11BssEntry,
       "saRgDot11BssId": saRgDot11BssId,
       "saRgDot11BssEnable": saRgDot11BssEnable,
       "saRgDot11BssSsid": saRgDot11BssSsid,
       "saRgDot11BssSecurityMode": saRgDot11BssSecurityMode,
       "saRgDot11BssClosedNetwork": saRgDot11BssClosedNetwork,
       "saRgDot11BssAccessMode": saRgDot11BssAccessMode,
       "saRgDot11BssMaxNumSta": saRgDot11BssMaxNumSta,
       "saRgDot11BssUserStatus": saRgDot11BssUserStatus,
       "saRgDot11BssApIsolation": saRgDot11BssApIsolation,
       "saRgDot11BssSecSsidTrafficPriority": saRgDot11BssSecSsidTrafficPriority,
       "saRgDot11BssRejectPriSsidSta": saRgDot11BssRejectPriSsidSta,
       "saRgDot11BssPrimary": saRgDot11BssPrimary,
       "saRgDot11BssPrimarySsidType": saRgDot11BssPrimarySsidType,
       "saRgDot11BssPrimarySsidPrefix": saRgDot11BssPrimarySsidPrefix,
       "saRgDot11Privacy": saRgDot11Privacy,
       "saRgDot11WpaTable": saRgDot11WpaTable,
       "saRgDot11WpaEntry": saRgDot11WpaEntry,
       "saRgDot11WpaAlgorithm": saRgDot11WpaAlgorithm,
       "saRgDot11WpaPreSharedKey": saRgDot11WpaPreSharedKey,
       "saRgDot11WpaGroupRekeyInterval": saRgDot11WpaGroupRekeyInterval,
       "saRgDot11RadiusTable": saRgDot11RadiusTable,
       "saRgDot11RadiusEntry": saRgDot11RadiusEntry,
       "saRgDot11RadiusAddressType": saRgDot11RadiusAddressType,
       "saRgDot11RadiusAddress": saRgDot11RadiusAddress,
       "saRgDot11RadiusPort": saRgDot11RadiusPort,
       "saRgDot11RadiusKey": saRgDot11RadiusKey,
       "saRgDot11RadiusReAuthInterval": saRgDot11RadiusReAuthInterval,
       "saRgDot11WepTable": saRgDot11WepTable,
       "saRgDot11WepEntry": saRgDot11WepEntry,
       "saRgDot11WepDefaultKey": saRgDot11WepDefaultKey,
       "saRgDot11WepEncryptionMode": saRgDot11WepEncryptionMode,
       "saRgDot11WepPassPhrase": saRgDot11WepPassPhrase,
       "saRgDot11Wep64BitKeyTable": saRgDot11Wep64BitKeyTable,
       "saRgDot11Wep64BitKeyEntry": saRgDot11Wep64BitKeyEntry,
       "saRgDot11Wep64BitKeyIndex": saRgDot11Wep64BitKeyIndex,
       "saRgDot11Wep64BitKeyValue": saRgDot11Wep64BitKeyValue,
       "saRgDot11Wep128BitKeyTable": saRgDot11Wep128BitKeyTable,
       "saRgDot11Wep128BitKeyEntry": saRgDot11Wep128BitKeyEntry,
       "saRgDot11Wep128BitKeyIndex": saRgDot11Wep128BitKeyIndex,
       "saRgDot11Wep128BitKeyValue": saRgDot11Wep128BitKeyValue,
       "saRgDot11PrivacyWps": saRgDot11PrivacyWps,
       "saRgDot11PrivacyWpsPushButtonTime": saRgDot11PrivacyWpsPushButtonTime,
       "saRgDot11Client": saRgDot11Client,
       "saRgDot11ClientTable": saRgDot11ClientTable,
       "saRgDot11ClientEntry": saRgDot11ClientEntry,
       "saRgDot11ClientIndex": saRgDot11ClientIndex,
       "saRgDot11ClientStation": saRgDot11ClientStation,
       "saRgDot11ExtMgmt": saRgDot11ExtMgmt,
       "saRgDot11ExtMgmtTable": saRgDot11ExtMgmtTable,
       "saRgDot11ExtMgmtEntry": saRgDot11ExtMgmtEntry,
       "saRgDot11ExtMbssUserControl": saRgDot11ExtMbssUserControl,
       "saRgDot11ExtMbssUseNonvol": saRgDot11ExtMbssUseNonvol,
       "saRgDot11ExtMbssAdminControl": saRgDot11ExtMbssAdminControl,
       "saRgDot11ExtActualChannel": saRgDot11ExtActualChannel,
       "saRgDot11ApplySettings": saRgDot11ApplySettings,
       "saRgIpMgmt": saRgIpMgmt,
       "saRgIpMgmtLanTable": saRgIpMgmtLanTable,
       "saRgIpMgmtLanEntry": saRgIpMgmtLanEntry,
       "saRgIpMgmtLanMode": saRgIpMgmtLanMode,
       "saRgIpMgmtLanNetwork": saRgIpMgmtLanNetwork,
       "saRgIpMgmtLanNetworksAllow": saRgIpMgmtLanNetworksAllow,
       "saRgIpMgmtLanSubnetMask": saRgIpMgmtLanSubnetMask,
       "saRgIpMgmtLanGateway": saRgIpMgmtLanGateway,
       "saRgIpMgmtLanDhcpServer": saRgIpMgmtLanDhcpServer,
       "saRgIpMgmtLanNapt": saRgIpMgmtLanNapt,
       "saRgIpMgmtLanTypeOfService": saRgIpMgmtLanTypeOfService,
       "saRgIpMgmtLanDhcp125Option": saRgIpMgmtLanDhcp125Option,
       "saRgIpMgmtLanUpnp": saRgIpMgmtLanUpnp,
       "saRgIpMgmtLanDhcpOption43": saRgIpMgmtLanDhcpOption43,
       "saRgIpMgmtLanDhcpServerTable": saRgIpMgmtLanDhcpServerTable,
       "saRgIpMgmtLanDhcpServerEntry": saRgIpMgmtLanDhcpServerEntry,
       "saRgIpMgmtLanDhcpServerPoolStart": saRgIpMgmtLanDhcpServerPoolStart,
       "saRgIpMgmtLanDhcpServerPoolEnd": saRgIpMgmtLanDhcpServerPoolEnd,
       "saRgIpMgmtLanDhcpServerLeaseTime": saRgIpMgmtLanDhcpServerLeaseTime,
       "saRgIpMgmtLanAddrTable": saRgIpMgmtLanAddrTable,
       "saRgIpMgmtLanAddrEntry": saRgIpMgmtLanAddrEntry,
       "saRgIpMgmtLanAddrIndex": saRgIpMgmtLanAddrIndex,
       "saRgIpMgmtLanAddrIp": saRgIpMgmtLanAddrIp,
       "saRgIpMgmtLanAddrPhysAddr": saRgIpMgmtLanAddrPhysAddr,
       "saRgIpMgmtLanAddrLeaseCreateTime": saRgIpMgmtLanAddrLeaseCreateTime,
       "saRgIpMgmtLanAddrLeaseExpireTime": saRgIpMgmtLanAddrLeaseExpireTime,
       "saRgIpMgmtLanAddrHostName": saRgIpMgmtLanAddrHostName,
       "saRgIpMgmtLanAddrClientId": saRgIpMgmtLanAddrClientId,
       "saRgIpMgmtLanAddrInterface": saRgIpMgmtLanAddrInterface,
       "saRgIpMgmtDnsServerTable": saRgIpMgmtDnsServerTable,
       "saRgIpMgmtDnsServerEntry": saRgIpMgmtDnsServerEntry,
       "saRgIpMgmtDnsServerIp": saRgIpMgmtDnsServerIp,
       "saRgIpMgmtDhcpFixedIpTable": saRgIpMgmtDhcpFixedIpTable,
       "saRgIpMgmtDhcpFixedIpEntry": saRgIpMgmtDhcpFixedIpEntry,
       "saRgIpMgmtDhcpFixedIpIndex": saRgIpMgmtDhcpFixedIpIndex,
       "saRgIpMgmtDhcpFixedIpRowStatus": saRgIpMgmtDhcpFixedIpRowStatus,
       "saRgIpMgmtDhcpFixedIpAddress": saRgIpMgmtDhcpFixedIpAddress,
       "saRgIpMgmtDhcpFixedIpPhysAddr": saRgIpMgmtDhcpFixedIpPhysAddr,
       "saRgIpMgmtDhcpFixedIpHostName": saRgIpMgmtDhcpFixedIpHostName,
       "saRgIpMgmtStaticRouteTable": saRgIpMgmtStaticRouteTable,
       "saRgIpMgmtStaticRouteEntry": saRgIpMgmtStaticRouteEntry,
       "saRgIpMgmtStaticRouteIndex": saRgIpMgmtStaticRouteIndex,
       "saRgIpMgmtStaticRouteRowStatus": saRgIpMgmtStaticRouteRowStatus,
       "saRgIpMgmtStaticRouteNetwork": saRgIpMgmtStaticRouteNetwork,
       "saRgIpMgmtStaticRouteSubnetMask": saRgIpMgmtStaticRouteSubnetMask,
       "saRgIpMgmtStaticRouteGateway": saRgIpMgmtStaticRouteGateway,
       "saRgIpMgmtStaticRouteRipAdvertise": saRgIpMgmtStaticRouteRipAdvertise,
       "saRgIpMgmtWanAddr": saRgIpMgmtWanAddr,
       "saRgIpMgmtWanAddrBase": saRgIpMgmtWanAddrBase,
       "saRgIpMgmtWanMode": saRgIpMgmtWanMode,
       "saRgIpMgmtWanMtu": saRgIpMgmtWanMtu,
       "saRgIpMgmtWanTtl": saRgIpMgmtWanTtl,
       "saRgIpMgmtWanAddrStatic": saRgIpMgmtWanAddrStatic,
       "saRgIpMgmtWanStaticNetwork": saRgIpMgmtWanStaticNetwork,
       "saRgIpMgmtWanStaticSubnetMask": saRgIpMgmtWanStaticSubnetMask,
       "saRgIpMgmtWanStaticGateway": saRgIpMgmtWanStaticGateway,
       "saRgIpMgmtWanAddrDualIp": saRgIpMgmtWanAddrDualIp,
       "saRgIpMgmtWanDualIpAddr": saRgIpMgmtWanDualIpAddr,
       "saRgIpMgmtWanDualIpRipAdvertised": saRgIpMgmtWanDualIpRipAdvertised,
       "saRgIpMgmtLanExtraSubnetTable": saRgIpMgmtLanExtraSubnetTable,
       "saRgIpMgmtLanExtraSubnetEntry": saRgIpMgmtLanExtraSubnetEntry,
       "saRgIpMgmtLanExtraSubnetIndex": saRgIpMgmtLanExtraSubnetIndex,
       "saRgIpMgmtLanExtraSubnetRowStatus": saRgIpMgmtLanExtraSubnetRowStatus,
       "saRgIpMgmtLanExtraSubnetIpAddress": saRgIpMgmtLanExtraSubnetIpAddress,
       "saRgIpMgmtLanExtraSubnetSubnetMask": saRgIpMgmtLanExtraSubnetSubnetMask,
       "saRgIpMgmtLanExtraSubnetGateway": saRgIpMgmtLanExtraSubnetGateway,
       "saRgIpMgmtLanPortControl": saRgIpMgmtLanPortControl,
       "saRgIpMgmtLanPortControlTable": saRgIpMgmtLanPortControlTable,
       "saRgIpMgmtLanPortControlEntry": saRgIpMgmtLanPortControlEntry,
       "saRgIpMgmtLanPortControlIndex": saRgIpMgmtLanPortControlIndex,
       "saRgIpMgmtLanPortMode": saRgIpMgmtLanPortMode,
       "saRgIpMgmtApplySettings": saRgIpMgmtApplySettings,
       "saRgFirewall": saRgFirewall,
       "saRgFirewallReport": saRgFirewallReport,
       "saRgFirewallReportEventTable": saRgFirewallReportEventTable,
       "saRgFirewallReportEventEntry": saRgFirewallReportEventEntry,
       "saRgFirewallReportEventIndex": saRgFirewallReportEventIndex,
       "saRgFirewallReportEventDescription": saRgFirewallReportEventDescription,
       "saRgFirewallReportEventCount": saRgFirewallReportEventCount,
       "saRgFirewallReportEventLastOccurance": saRgFirewallReportEventLastOccurance,
       "saRgFirewallReportEventTarget": saRgFirewallReportEventTarget,
       "saRgFirewallReportEventSource": saRgFirewallReportEventSource,
       "saRgFirewallReportMgmt": saRgFirewallReportMgmt,
       "saRgFirewallReportMgmtClearLog": saRgFirewallReportMgmtClearLog,
       "saRgFirewallReportEmailLogNow": saRgFirewallReportEmailLogNow,
       "saRgFirewallReportEmail": saRgFirewallReportEmail,
       "saRgFirewallReportEmailEnable": saRgFirewallReportEmailEnable,
       "saRgFirewallReportEmailAddress": saRgFirewallReportEmailAddress,
       "saRgFirewallReportEmailSmtpServer": saRgFirewallReportEmailSmtpServer,
       "saRgFirewallReportEmailUsername": saRgFirewallReportEmailUsername,
       "saRgFirewallReportEmailPassword": saRgFirewallReportEmailPassword,
       "saRgFirewallRules": saRgFirewallRules,
       "saRgFirewallIpFilterTable": saRgFirewallIpFilterTable,
       "saRgFirewallIpFilterEntry": saRgFirewallIpFilterEntry,
       "saRgFirewallIpFilterIndex": saRgFirewallIpFilterIndex,
       "saRgFirewallIpFilterRowStatus": saRgFirewallIpFilterRowStatus,
       "saRgFirewallIpFilterAddressStart": saRgFirewallIpFilterAddressStart,
       "saRgFirewallIpFilterAddressEnd": saRgFirewallIpFilterAddressEnd,
       "saRgFirewallPortFilterTable": saRgFirewallPortFilterTable,
       "saRgFirewallPortFilterEntry": saRgFirewallPortFilterEntry,
       "saRgFirewallPortFilterIndex": saRgFirewallPortFilterIndex,
       "saRgFirewallPortFilterRowStatus": saRgFirewallPortFilterRowStatus,
       "saRgFirewallPortFilterPortStart": saRgFirewallPortFilterPortStart,
       "saRgFirewallPortFilterPortEnd": saRgFirewallPortFilterPortEnd,
       "saRgFirewallPortFilterProto": saRgFirewallPortFilterProto,
       "saRgFirewallMacFilterTable": saRgFirewallMacFilterTable,
       "saRgFirewallMacFilterEntry": saRgFirewallMacFilterEntry,
       "saRgFirewallMacFilterIndex": saRgFirewallMacFilterIndex,
       "saRgFirewallMacFilterRowStatus": saRgFirewallMacFilterRowStatus,
       "saRgFirewallMacFilterAddress": saRgFirewallMacFilterAddress,
       "saRgFirewallMacFilterEnable": saRgFirewallMacFilterEnable,
       "saRgFirewallMacFilterMode": saRgFirewallMacFilterMode,
       "saRgFirewallPortFwdTable": saRgFirewallPortFwdTable,
       "saRgFirewallPortFwdEntry": saRgFirewallPortFwdEntry,
       "saRgFirewallPortFwdIndex": saRgFirewallPortFwdIndex,
       "saRgFirewallPortFwdRowStatus": saRgFirewallPortFwdRowStatus,
       "saRgFirewallPortFwdToAddress": saRgFirewallPortFwdToAddress,
       "saRgFirewallPortFwdPortStart": saRgFirewallPortFwdPortStart,
       "saRgFirewallPortFwdPortEnd": saRgFirewallPortFwdPortEnd,
       "saRgFirewallPortFwdProto": saRgFirewallPortFwdProto,
       "saRgFirewallPortFwdExternalPortStart": saRgFirewallPortFwdExternalPortStart,
       "saRgFirewallPortFwdExternalPortEnd": saRgFirewallPortFwdExternalPortEnd,
       "saRgFirewallPortTrigTable": saRgFirewallPortTrigTable,
       "saRgFirewallPortTrigEntry": saRgFirewallPortTrigEntry,
       "saRgFirewallPortTrigIndex": saRgFirewallPortTrigIndex,
       "saRgFirewallPortTrigRowStatus": saRgFirewallPortTrigRowStatus,
       "saRgFirewallPortTrigTriggerPortStart": saRgFirewallPortTrigTriggerPortStart,
       "saRgFirewallPortTrigTriggerPortEnd": saRgFirewallPortTrigTriggerPortEnd,
       "saRgFirewallPortTrigTargetPortStart": saRgFirewallPortTrigTargetPortStart,
       "saRgFirewallPortTrigTargetPortEnd": saRgFirewallPortTrigTargetPortEnd,
       "saRgFirewallPortTrigProto": saRgFirewallPortTrigProto,
       "saRgFirewallApplySettings": saRgFirewallApplySettings,
       "saRgDslite": saRgDslite,
       "saRgDsliteOption": saRgDsliteOption,
       "saRgDsliteAftrName": saRgDsliteAftrName,
       "saRgDsliteAftrAddress": saRgDsliteAftrAddress,
       "saRgDsliteTcpMssClamping": saRgDsliteTcpMssClamping,
       "saRgDsliteApplySettings": saRgDsliteApplySettings}
)
