# SNMP MIB module (WILAN-120-58-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WILAN-120-58-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:57 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wilan_ObjectIdentity = ObjectIdentity
wilan = _Wilan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2686)
)
_Awe120_58_ObjectIdentity = ObjectIdentity
awe120_58 = _Awe120_58_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2686, 2)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1)
)


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _ProductionDate_Type(DisplayString):
    """Custom type productionDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ProductionDate_Type.__name__ = "DisplayString"
_ProductionDate_Object = MibScalar
productionDate = _ProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 2),
    _ProductionDate_Type()
)
productionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productionDate.setStatus("current")
_MacAddress_Type = PhysAddress
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 3),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")


class _SystemName_Type(DisplayString):
    """Custom type systemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SystemName_Type.__name__ = "DisplayString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 4),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("current")


class _UnitLocation_Type(DisplayString):
    """Custom type unitLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UnitLocation_Type.__name__ = "DisplayString"
_UnitLocation_Object = MibScalar
unitLocation = _UnitLocation_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 5),
    _UnitLocation_Type()
)
unitLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitLocation.setStatus("current")


class _ContactName_Type(DisplayString):
    """Custom type contactName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ContactName_Type.__name__ = "DisplayString"
_ContactName_Object = MibScalar
contactName = _ContactName_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 6),
    _ContactName_Type()
)
contactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactName.setStatus("current")
_Config7_Type = Integer32
_Config7_Object = MibScalar
config7 = _Config7_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 7),
    _Config7_Type()
)
config7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config7.setStatus("current")
_Config8_Type = Integer32
_Config8_Object = MibScalar
config8 = _Config8_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 8),
    _Config8_Type()
)
config8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config8.setStatus("current")
_Config9_Type = Integer32
_Config9_Object = MibScalar
config9 = _Config9_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 9),
    _Config9_Type()
)
config9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config9.setStatus("current")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 10),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_IpNewAddress_Type = IpAddress
_IpNewAddress_Object = MibScalar
ipNewAddress = _IpNewAddress_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 11),
    _IpNewAddress_Type()
)
ipNewAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNewAddress.setStatus("current")
_IpSubnetMask_Type = IpAddress
_IpSubnetMask_Object = MibScalar
ipSubnetMask = _IpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 12),
    _IpSubnetMask_Type()
)
ipSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSubnetMask.setStatus("current")
_IpGatewayAddr_Type = IpAddress
_IpGatewayAddr_Object = MibScalar
ipGatewayAddr = _IpGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 13),
    _IpGatewayAddr_Type()
)
ipGatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGatewayAddr.setStatus("current")
_IpNetmanAddr_Type = IpAddress
_IpNetmanAddr_Object = MibScalar
ipNetmanAddr = _IpNetmanAddr_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 14),
    _IpNetmanAddr_Type()
)
ipNetmanAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetmanAddr.setStatus("current")


class _IpPacketFiltering_Type(Integer32):
    """Custom type ipPacketFiltering based on Integer32"""
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


_IpPacketFiltering_Type.__name__ = "Integer32"
_IpPacketFiltering_Object = MibScalar
ipPacketFiltering = _IpPacketFiltering_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 15),
    _IpPacketFiltering_Type()
)
ipPacketFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPacketFiltering.setStatus("current")


class _IpAddressFiltering_Type(Integer32):
    """Custom type ipAddressFiltering based on Integer32"""
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


_IpAddressFiltering_Type.__name__ = "Integer32"
_IpAddressFiltering_Object = MibScalar
ipAddressFiltering = _IpAddressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 16),
    _IpAddressFiltering_Type()
)
ipAddressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressFiltering.setStatus("current")


class _IpFilter1Range_Type(Integer32):
    """Custom type ipFilter1Range based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpFilter1Range_Type.__name__ = "Integer32"
_IpFilter1Range_Object = MibScalar
ipFilter1Range = _IpFilter1Range_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 17),
    _IpFilter1Range_Type()
)
ipFilter1Range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilter1Range.setStatus("current")
_IpFilter1Base_Type = IpAddress
_IpFilter1Base_Object = MibScalar
ipFilter1Base = _IpFilter1Base_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 18),
    _IpFilter1Base_Type()
)
ipFilter1Base.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilter1Base.setStatus("current")


class _IpFilter2Range_Type(Integer32):
    """Custom type ipFilter2Range based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpFilter2Range_Type.__name__ = "Integer32"
_IpFilter2Range_Object = MibScalar
ipFilter2Range = _IpFilter2Range_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 19),
    _IpFilter2Range_Type()
)
ipFilter2Range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilter2Range.setStatus("current")
_IpFilter2Base_Type = IpAddress
_IpFilter2Base_Object = MibScalar
ipFilter2Base = _IpFilter2Base_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 20),
    _IpFilter2Base_Type()
)
ipFilter2Base.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilter2Base.setStatus("current")


class _IpFilter3Range_Type(Integer32):
    """Custom type ipFilter3Range based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpFilter3Range_Type.__name__ = "Integer32"
_IpFilter3Range_Object = MibScalar
ipFilter3Range = _IpFilter3Range_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 21),
    _IpFilter3Range_Type()
)
ipFilter3Range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilter3Range.setStatus("current")
_IpFilter3Base_Type = IpAddress
_IpFilter3Base_Object = MibScalar
ipFilter3Base = _IpFilter3Base_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 22),
    _IpFilter3Base_Type()
)
ipFilter3Base.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilter3Base.setStatus("current")


class _IpFilter4Range_Type(Integer32):
    """Custom type ipFilter4Range based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpFilter4Range_Type.__name__ = "Integer32"
_IpFilter4Range_Object = MibScalar
ipFilter4Range = _IpFilter4Range_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 23),
    _IpFilter4Range_Type()
)
ipFilter4Range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilter4Range.setStatus("current")
_IpFilter4Base_Type = IpAddress
_IpFilter4Base_Object = MibScalar
ipFilter4Base = _IpFilter4Base_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 24),
    _IpFilter4Base_Type()
)
ipFilter4Base.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilter4Base.setStatus("current")


class _IpFilter5Range_Type(Integer32):
    """Custom type ipFilter5Range based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpFilter5Range_Type.__name__ = "Integer32"
_IpFilter5Range_Object = MibScalar
ipFilter5Range = _IpFilter5Range_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 25),
    _IpFilter5Range_Type()
)
ipFilter5Range.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilter5Range.setStatus("current")
_IpFilter5Base_Type = IpAddress
_IpFilter5Base_Object = MibScalar
ipFilter5Base = _IpFilter5Base_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 26),
    _IpFilter5Base_Type()
)
ipFilter5Base.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilter5Base.setStatus("current")


class _MacFilterEntryAge_Type(Integer32):
    """Custom type macFilterEntryAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_MacFilterEntryAge_Type.__name__ = "Integer32"
_MacFilterEntryAge_Object = MibScalar
macFilterEntryAge = _MacFilterEntryAge_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 27),
    _MacFilterEntryAge_Type()
)
macFilterEntryAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterEntryAge.setStatus("current")
_Config28_Type = Integer32
_Config28_Object = MibScalar
config28 = _Config28_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 28),
    _Config28_Type()
)
config28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config28.setStatus("current")
_Config29_Type = Integer32
_Config29_Object = MibScalar
config29 = _Config29_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 29),
    _Config29_Type()
)
config29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config29.setStatus("current")


class _StationType_Type(Integer32):
    """Custom type stationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("base-stn", 1),
          ("remote", 0))
    )


_StationType_Type.__name__ = "Integer32"
_StationType_Object = MibScalar
stationType = _StationType_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 30),
    _StationType_Type()
)
stationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationType.setStatus("current")


class _StationRank_Type(Integer32):
    """Custom type stationRank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_StationRank_Type.__name__ = "Integer32"
_StationRank_Object = MibScalar
stationRank = _StationRank_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 31),
    _StationRank_Type()
)
stationRank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationRank.setStatus("current")


class _CenterFreq_Type(Integer32):
    """Custom type centerFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(57410, 58338),
    )


_CenterFreq_Type.__name__ = "Integer32"
_CenterFreq_Object = MibScalar
centerFreq = _CenterFreq_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 32),
    _CenterFreq_Type()
)
centerFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    centerFreq.setStatus("current")
_SecurityWord1_Type = Integer32
_SecurityWord1_Object = MibScalar
securityWord1 = _SecurityWord1_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 33),
    _SecurityWord1_Type()
)
securityWord1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityWord1.setStatus("current")
_SecurityWord2_Type = Integer32
_SecurityWord2_Object = MibScalar
securityWord2 = _SecurityWord2_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 34),
    _SecurityWord2_Type()
)
securityWord2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityWord2.setStatus("current")
_SecurityWord3_Type = Integer32
_SecurityWord3_Object = MibScalar
securityWord3 = _SecurityWord3_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 35),
    _SecurityWord3_Type()
)
securityWord3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityWord3.setStatus("current")
_SecurityWord4_Type = Integer32
_SecurityWord4_Object = MibScalar
securityWord4 = _SecurityWord4_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 36),
    _SecurityWord4_Type()
)
securityWord4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityWord4.setStatus("current")
_SecurityWord5_Type = Integer32
_SecurityWord5_Object = MibScalar
securityWord5 = _SecurityWord5_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 37),
    _SecurityWord5_Type()
)
securityWord5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityWord5.setStatus("current")
_ScramblingCode_Type = Integer32
_ScramblingCode_Object = MibScalar
scramblingCode = _ScramblingCode_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 38),
    _ScramblingCode_Type()
)
scramblingCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scramblingCode.setStatus("current")


class _AcquisitionCode_Type(Integer32):
    """Custom type acquisitionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcquisitionCode_Type.__name__ = "Integer32"
_AcquisitionCode_Object = MibScalar
acquisitionCode = _AcquisitionCode_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 39),
    _AcquisitionCode_Type()
)
acquisitionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acquisitionCode.setStatus("current")


class _ConfigMinutes_Type(Integer32):
    """Custom type configMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_ConfigMinutes_Type.__name__ = "Integer32"
_ConfigMinutes_Object = MibScalar
configMinutes = _ConfigMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 40),
    _ConfigMinutes_Type()
)
configMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configMinutes.setStatus("current")


class _RepeaterMode_Type(Integer32):
    """Custom type repeaterMode based on Integer32"""
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


_RepeaterMode_Type.__name__ = "Integer32"
_RepeaterMode_Object = MibScalar
repeaterMode = _RepeaterMode_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 41),
    _RepeaterMode_Type()
)
repeaterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterMode.setStatus("current")


class _SystemType_Type(Integer32):
    """Custom type systemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric", 0),
          ("symmetric", 1))
    )


_SystemType_Type.__name__ = "Integer32"
_SystemType_Object = MibScalar
systemType = _SystemType_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 42),
    _SystemType_Type()
)
systemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemType.setStatus("current")


class _RemoteGroup_Type(Integer32):
    """Custom type remoteGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RemoteGroup_Type.__name__ = "Integer32"
_RemoteGroup_Object = MibScalar
remoteGroup = _RemoteGroup_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 43),
    _RemoteGroup_Type()
)
remoteGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteGroup.setStatus("current")


class _NumOfPollRounds_Type(Integer32):
    """Custom type numOfPollRounds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_NumOfPollRounds_Type.__name__ = "Integer32"
_NumOfPollRounds_Object = MibScalar
numOfPollRounds = _NumOfPollRounds_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 44),
    _NumOfPollRounds_Type()
)
numOfPollRounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfPollRounds.setStatus("current")


class _TxPwrLevelAdj_Type(Integer32):
    """Custom type txPwrLevelAdj based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("dB-1", 30),
          ("dB-10", 21),
          ("dB-11", 20),
          ("dB-12", 19),
          ("dB-13", 18),
          ("dB-14", 17),
          ("dB-15", 16),
          ("dB-16", 15),
          ("dB-17", 14),
          ("dB-18", 13),
          ("dB-19", 12),
          ("dB-2", 29),
          ("dB-20", 11),
          ("dB-21", 10),
          ("dB-22", 9),
          ("dB-23", 8),
          ("dB-24", 7),
          ("dB-25", 6),
          ("dB-26", 5),
          ("dB-27", 4),
          ("dB-28", 3),
          ("dB-29", 2),
          ("dB-3", 28),
          ("dB-30", 1),
          ("dB-31", 0),
          ("dB-4", 27),
          ("dB-5", 26),
          ("dB-6", 25),
          ("dB-7", 24),
          ("dB-8", 23),
          ("dB-9", 22),
          ("dB0", 31))
    )


_TxPwrLevelAdj_Type.__name__ = "Integer32"
_TxPwrLevelAdj_Object = MibScalar
txPwrLevelAdj = _TxPwrLevelAdj_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 45),
    _TxPwrLevelAdj_Type()
)
txPwrLevelAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPwrLevelAdj.setStatus("current")


class _DefStationType_Type(Integer32):
    """Custom type defStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("base-stn", 1),
          ("remote", 0))
    )


_DefStationType_Type.__name__ = "Integer32"
_DefStationType_Object = MibScalar
defStationType = _DefStationType_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 46),
    _DefStationType_Type()
)
defStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defStationType.setStatus("current")


class _DefStationRank_Type(Integer32):
    """Custom type defStationRank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_DefStationRank_Type.__name__ = "Integer32"
_DefStationRank_Object = MibScalar
defStationRank = _DefStationRank_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 47),
    _DefStationRank_Type()
)
defStationRank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defStationRank.setStatus("current")


class _DefCenterFreq_Type(Integer32):
    """Custom type defCenterFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(57410, 58338),
    )


_DefCenterFreq_Type.__name__ = "Integer32"
_DefCenterFreq_Object = MibScalar
defCenterFreq = _DefCenterFreq_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 48),
    _DefCenterFreq_Type()
)
defCenterFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defCenterFreq.setStatus("current")
_DefSecurityWord1_Type = Integer32
_DefSecurityWord1_Object = MibScalar
defSecurityWord1 = _DefSecurityWord1_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 49),
    _DefSecurityWord1_Type()
)
defSecurityWord1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defSecurityWord1.setStatus("current")
_DefSecurityWord2_Type = Integer32
_DefSecurityWord2_Object = MibScalar
defSecurityWord2 = _DefSecurityWord2_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 50),
    _DefSecurityWord2_Type()
)
defSecurityWord2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defSecurityWord2.setStatus("current")
_DefSecurityWord3_Type = Integer32
_DefSecurityWord3_Object = MibScalar
defSecurityWord3 = _DefSecurityWord3_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 51),
    _DefSecurityWord3_Type()
)
defSecurityWord3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defSecurityWord3.setStatus("current")
_DefSecurityWord4_Type = Integer32
_DefSecurityWord4_Object = MibScalar
defSecurityWord4 = _DefSecurityWord4_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 52),
    _DefSecurityWord4_Type()
)
defSecurityWord4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defSecurityWord4.setStatus("current")
_DefSecurityWord5_Type = Integer32
_DefSecurityWord5_Object = MibScalar
defSecurityWord5 = _DefSecurityWord5_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 53),
    _DefSecurityWord5_Type()
)
defSecurityWord5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defSecurityWord5.setStatus("current")
_DefScramblingCode_Type = Integer32
_DefScramblingCode_Object = MibScalar
defScramblingCode = _DefScramblingCode_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 54),
    _DefScramblingCode_Type()
)
defScramblingCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defScramblingCode.setStatus("current")


class _DefAcquisitionCode_Type(Integer32):
    """Custom type defAcquisitionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DefAcquisitionCode_Type.__name__ = "Integer32"
_DefAcquisitionCode_Object = MibScalar
defAcquisitionCode = _DefAcquisitionCode_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 55),
    _DefAcquisitionCode_Type()
)
defAcquisitionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defAcquisitionCode.setStatus("current")


class _DefConfigMinutes_Type(Integer32):
    """Custom type defConfigMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_DefConfigMinutes_Type.__name__ = "Integer32"
_DefConfigMinutes_Object = MibScalar
defConfigMinutes = _DefConfigMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 56),
    _DefConfigMinutes_Type()
)
defConfigMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defConfigMinutes.setStatus("current")


class _DefRepeaterMode_Type(Integer32):
    """Custom type defRepeaterMode based on Integer32"""
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


_DefRepeaterMode_Type.__name__ = "Integer32"
_DefRepeaterMode_Object = MibScalar
defRepeaterMode = _DefRepeaterMode_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 57),
    _DefRepeaterMode_Type()
)
defRepeaterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defRepeaterMode.setStatus("current")


class _DefSystemType_Type(Integer32):
    """Custom type defSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric", 0),
          ("symmetric", 1))
    )


_DefSystemType_Type.__name__ = "Integer32"
_DefSystemType_Object = MibScalar
defSystemType = _DefSystemType_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 58),
    _DefSystemType_Type()
)
defSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defSystemType.setStatus("current")


class _DefRemoteGroup_Type(Integer32):
    """Custom type defRemoteGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DefRemoteGroup_Type.__name__ = "Integer32"
_DefRemoteGroup_Object = MibScalar
defRemoteGroup = _DefRemoteGroup_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 59),
    _DefRemoteGroup_Type()
)
defRemoteGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defRemoteGroup.setStatus("current")


class _DefNumOfPollRounds_Type(Integer32):
    """Custom type defNumOfPollRounds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_DefNumOfPollRounds_Type.__name__ = "Integer32"
_DefNumOfPollRounds_Object = MibScalar
defNumOfPollRounds = _DefNumOfPollRounds_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 60),
    _DefNumOfPollRounds_Type()
)
defNumOfPollRounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defNumOfPollRounds.setStatus("current")


class _DefTxPwrLevelAdj_Type(Integer32):
    """Custom type defTxPwrLevelAdj based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("dB-1", 30),
          ("dB-10", 21),
          ("dB-11", 20),
          ("dB-12", 19),
          ("dB-13", 18),
          ("dB-14", 17),
          ("dB-15", 16),
          ("dB-16", 15),
          ("dB-17", 14),
          ("dB-18", 13),
          ("dB-19", 12),
          ("dB-2", 29),
          ("dB-20", 11),
          ("dB-21", 10),
          ("dB-22", 9),
          ("dB-23", 8),
          ("dB-24", 7),
          ("dB-25", 6),
          ("dB-26", 5),
          ("dB-27", 4),
          ("dB-28", 3),
          ("dB-29", 2),
          ("dB-3", 28),
          ("dB-30", 1),
          ("dB-31", 0),
          ("dB-4", 27),
          ("dB-5", 26),
          ("dB-6", 25),
          ("dB-7", 24),
          ("dB-8", 23),
          ("dB-9", 22),
          ("dB0", 31))
    )


_DefTxPwrLevelAdj_Type.__name__ = "Integer32"
_DefTxPwrLevelAdj_Object = MibScalar
defTxPwrLevelAdj = _DefTxPwrLevelAdj_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 61),
    _DefTxPwrLevelAdj_Type()
)
defTxPwrLevelAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defTxPwrLevelAdj.setStatus("current")


class _NewStationType_Type(Integer32):
    """Custom type newStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("base-stn", 1),
          ("remote", 0))
    )


_NewStationType_Type.__name__ = "Integer32"
_NewStationType_Object = MibScalar
newStationType = _NewStationType_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 62),
    _NewStationType_Type()
)
newStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newStationType.setStatus("current")


class _NewStationRank_Type(Integer32):
    """Custom type newStationRank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NewStationRank_Type.__name__ = "Integer32"
_NewStationRank_Object = MibScalar
newStationRank = _NewStationRank_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 63),
    _NewStationRank_Type()
)
newStationRank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newStationRank.setStatus("current")


class _NewCenterFreq_Type(Integer32):
    """Custom type newCenterFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(57410, 58338),
    )


_NewCenterFreq_Type.__name__ = "Integer32"
_NewCenterFreq_Object = MibScalar
newCenterFreq = _NewCenterFreq_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 64),
    _NewCenterFreq_Type()
)
newCenterFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newCenterFreq.setStatus("current")
_NewSecurityWord1_Type = Integer32
_NewSecurityWord1_Object = MibScalar
newSecurityWord1 = _NewSecurityWord1_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 65),
    _NewSecurityWord1_Type()
)
newSecurityWord1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSecurityWord1.setStatus("current")
_NewSecurityWord2_Type = Integer32
_NewSecurityWord2_Object = MibScalar
newSecurityWord2 = _NewSecurityWord2_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 66),
    _NewSecurityWord2_Type()
)
newSecurityWord2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSecurityWord2.setStatus("current")
_NewSecurityWord3_Type = Integer32
_NewSecurityWord3_Object = MibScalar
newSecurityWord3 = _NewSecurityWord3_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 67),
    _NewSecurityWord3_Type()
)
newSecurityWord3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSecurityWord3.setStatus("current")
_NewSecurityWord4_Type = Integer32
_NewSecurityWord4_Object = MibScalar
newSecurityWord4 = _NewSecurityWord4_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 68),
    _NewSecurityWord4_Type()
)
newSecurityWord4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSecurityWord4.setStatus("current")
_NewSecurityWord5_Type = Integer32
_NewSecurityWord5_Object = MibScalar
newSecurityWord5 = _NewSecurityWord5_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 69),
    _NewSecurityWord5_Type()
)
newSecurityWord5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSecurityWord5.setStatus("current")
_NewScramblingCode_Type = Integer32
_NewScramblingCode_Object = MibScalar
newScramblingCode = _NewScramblingCode_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 70),
    _NewScramblingCode_Type()
)
newScramblingCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newScramblingCode.setStatus("current")


class _NewAcquisitionCode_Type(Integer32):
    """Custom type newAcquisitionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NewAcquisitionCode_Type.__name__ = "Integer32"
_NewAcquisitionCode_Object = MibScalar
newAcquisitionCode = _NewAcquisitionCode_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 71),
    _NewAcquisitionCode_Type()
)
newAcquisitionCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newAcquisitionCode.setStatus("current")


class _NewConfigMinutes_Type(Integer32):
    """Custom type newConfigMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_NewConfigMinutes_Type.__name__ = "Integer32"
_NewConfigMinutes_Object = MibScalar
newConfigMinutes = _NewConfigMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 72),
    _NewConfigMinutes_Type()
)
newConfigMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newConfigMinutes.setStatus("current")


class _NewRepeaterMode_Type(Integer32):
    """Custom type newRepeaterMode based on Integer32"""
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


_NewRepeaterMode_Type.__name__ = "Integer32"
_NewRepeaterMode_Object = MibScalar
newRepeaterMode = _NewRepeaterMode_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 73),
    _NewRepeaterMode_Type()
)
newRepeaterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newRepeaterMode.setStatus("current")


class _NewSystemType_Type(Integer32):
    """Custom type newSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric", 0),
          ("symmetric", 1))
    )


_NewSystemType_Type.__name__ = "Integer32"
_NewSystemType_Object = MibScalar
newSystemType = _NewSystemType_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 74),
    _NewSystemType_Type()
)
newSystemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newSystemType.setStatus("current")


class _NewRemoteGroup_Type(Integer32):
    """Custom type newRemoteGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NewRemoteGroup_Type.__name__ = "Integer32"
_NewRemoteGroup_Object = MibScalar
newRemoteGroup = _NewRemoteGroup_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 75),
    _NewRemoteGroup_Type()
)
newRemoteGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newRemoteGroup.setStatus("current")


class _NewNumOfPollRounds_Type(Integer32):
    """Custom type newNumOfPollRounds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_NewNumOfPollRounds_Type.__name__ = "Integer32"
_NewNumOfPollRounds_Object = MibScalar
newNumOfPollRounds = _NewNumOfPollRounds_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 76),
    _NewNumOfPollRounds_Type()
)
newNumOfPollRounds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newNumOfPollRounds.setStatus("current")


class _NewTxPwrLevelAdj_Type(Integer32):
    """Custom type newTxPwrLevelAdj based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("dB-1", 30),
          ("dB-10", 21),
          ("dB-11", 20),
          ("dB-12", 19),
          ("dB-13", 18),
          ("dB-14", 17),
          ("dB-15", 16),
          ("dB-16", 15),
          ("dB-17", 14),
          ("dB-18", 13),
          ("dB-19", 12),
          ("dB-2", 29),
          ("dB-20", 11),
          ("dB-21", 10),
          ("dB-22", 9),
          ("dB-23", 8),
          ("dB-24", 7),
          ("dB-25", 6),
          ("dB-26", 5),
          ("dB-27", 4),
          ("dB-28", 3),
          ("dB-29", 2),
          ("dB-3", 28),
          ("dB-30", 1),
          ("dB-31", 0),
          ("dB-4", 27),
          ("dB-5", 26),
          ("dB-6", 25),
          ("dB-7", 24),
          ("dB-8", 23),
          ("dB-9", 22),
          ("dB0", 31))
    )


_NewTxPwrLevelAdj_Type.__name__ = "Integer32"
_NewTxPwrLevelAdj_Object = MibScalar
newTxPwrLevelAdj = _NewTxPwrLevelAdj_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 77),
    _NewTxPwrLevelAdj_Type()
)
newTxPwrLevelAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newTxPwrLevelAdj.setStatus("current")


class _StationMode_Type(Integer32):
    """Custom type stationMode based on Integer32"""
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
        *(("normal", 0),
          ("rssi-test", 3),
          ("rx-test", 1),
          ("tx-test", 2))
    )


_StationMode_Type.__name__ = "Integer32"
_StationMode_Object = MibScalar
stationMode = _StationMode_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 78),
    _StationMode_Type()
)
stationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationMode.setStatus("current")


class _RfTransmitStatus_Type(Integer32):
    """Custom type rfTransmitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 0),
          ("unblocked", 1))
    )


_RfTransmitStatus_Type.__name__ = "Integer32"
_RfTransmitStatus_Object = MibScalar
rfTransmitStatus = _RfTransmitStatus_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 79),
    _RfTransmitStatus_Type()
)
rfTransmitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfTransmitStatus.setStatus("current")


class _LinkMonitorPeriod_Type(Integer32):
    """Custom type linkMonitorPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_LinkMonitorPeriod_Type.__name__ = "Integer32"
_LinkMonitorPeriod_Object = MibScalar
linkMonitorPeriod = _LinkMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 80),
    _LinkMonitorPeriod_Type()
)
linkMonitorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkMonitorPeriod.setStatus("current")


class _TestModeTimer_Type(Integer32):
    """Custom type testModeTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TestModeTimer_Type.__name__ = "Integer32"
_TestModeTimer_Object = MibScalar
testModeTimer = _TestModeTimer_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 81),
    _TestModeTimer_Type()
)
testModeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    testModeTimer.setStatus("current")


class _RemoteDistance_Type(Integer32):
    """Custom type remoteDistance based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("km05", 1),
          ("km10", 2),
          ("km15", 3),
          ("km20", 4),
          ("km25", 5),
          ("km30", 6),
          ("km35", 7),
          ("km40", 8),
          ("km45", 9),
          ("km50", 10),
          ("km55", 11),
          ("km60", 12))
    )


_RemoteDistance_Type.__name__ = "Integer32"
_RemoteDistance_Object = MibScalar
remoteDistance = _RemoteDistance_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 82),
    _RemoteDistance_Type()
)
remoteDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteDistance.setStatus("current")


class _LinkMonitorRank_Type(Integer32):
    """Custom type linkMonitorRank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_LinkMonitorRank_Type.__name__ = "Integer32"
_LinkMonitorRank_Object = MibScalar
linkMonitorRank = _LinkMonitorRank_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 83),
    _LinkMonitorRank_Type()
)
linkMonitorRank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkMonitorRank.setStatus("current")


class _ThrottleEnable_Type(Integer32):
    """Custom type throttleEnable based on Integer32"""
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


_ThrottleEnable_Type.__name__ = "Integer32"
_ThrottleEnable_Object = MibScalar
throttleEnable = _ThrottleEnable_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 84),
    _ThrottleEnable_Type()
)
throttleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    throttleEnable.setStatus("current")


class _ThrottleLevel_Type(Integer32):
    """Custom type throttleLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ThrottleLevel_Type.__name__ = "Integer32"
_ThrottleLevel_Object = MibScalar
throttleLevel = _ThrottleLevel_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 85),
    _ThrottleLevel_Type()
)
throttleLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    throttleLevel.setStatus("current")
_Config86_Type = Integer32
_Config86_Object = MibScalar
config86 = _Config86_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 86),
    _Config86_Type()
)
config86.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config86.setStatus("current")
_Config87_Type = Integer32
_Config87_Object = MibScalar
config87 = _Config87_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 87),
    _Config87_Type()
)
config87.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config87.setStatus("current")
_Config88_Type = Integer32
_Config88_Object = MibScalar
config88 = _Config88_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 88),
    _Config88_Type()
)
config88.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config88.setStatus("current")
_Config89_Type = Integer32
_Config89_Object = MibScalar
config89 = _Config89_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 89),
    _Config89_Type()
)
config89.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config89.setStatus("current")


class _CommunityName1_Type(DisplayString):
    """Custom type communityName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CommunityName1_Type.__name__ = "DisplayString"
_CommunityName1_Object = MibScalar
communityName1 = _CommunityName1_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 90),
    _CommunityName1_Type()
)
communityName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityName1.setStatus("current")


class _CommunityName2_Type(DisplayString):
    """Custom type communityName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CommunityName2_Type.__name__ = "DisplayString"
_CommunityName2_Object = MibScalar
communityName2 = _CommunityName2_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 91),
    _CommunityName2_Type()
)
communityName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityName2.setStatus("current")


class _EthernetAccess_Type(Integer32):
    """Custom type ethernetAccess based on Integer32"""
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


_EthernetAccess_Type.__name__ = "Integer32"
_EthernetAccess_Object = MibScalar
ethernetAccess = _EthernetAccess_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 92),
    _EthernetAccess_Type()
)
ethernetAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetAccess.setStatus("current")


class _WirelessAccess_Type(Integer32):
    """Custom type wirelessAccess based on Integer32"""
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


_WirelessAccess_Type.__name__ = "Integer32"
_WirelessAccess_Object = MibScalar
wirelessAccess = _WirelessAccess_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 93),
    _WirelessAccess_Type()
)
wirelessAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessAccess.setStatus("current")
_Config94_Type = Integer32
_Config94_Object = MibScalar
config94 = _Config94_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 94),
    _Config94_Type()
)
config94.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config94.setStatus("current")


class _CurrentImage_Type(DisplayString):
    """Custom type currentImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CurrentImage_Type.__name__ = "DisplayString"
_CurrentImage_Object = MibScalar
currentImage = _CurrentImage_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 95),
    _CurrentImage_Type()
)
currentImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentImage.setStatus("current")


class _DefaultImage_Type(DisplayString):
    """Custom type defaultImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DefaultImage_Type.__name__ = "DisplayString"
_DefaultImage_Object = MibScalar
defaultImage = _DefaultImage_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 96),
    _DefaultImage_Type()
)
defaultImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultImage.setStatus("current")


class _PrevDefaultImage_Type(DisplayString):
    """Custom type prevDefaultImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PrevDefaultImage_Type.__name__ = "DisplayString"
_PrevDefaultImage_Object = MibScalar
prevDefaultImage = _PrevDefaultImage_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 97),
    _PrevDefaultImage_Type()
)
prevDefaultImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prevDefaultImage.setStatus("current")
_Config98_Type = Integer32
_Config98_Object = MibScalar
config98 = _Config98_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 98),
    _Config98_Type()
)
config98.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config98.setStatus("current")
_Config99_Type = Integer32
_Config99_Object = MibScalar
config99 = _Config99_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 99),
    _Config99_Type()
)
config99.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config99.setStatus("current")
_SystemImageList_Object = MibTable
systemImageList = _SystemImageList_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 100)
)
if mibBuilder.loadTexts:
    systemImageList.setStatus("current")
_SystemImageEntry_Object = MibTableRow
systemImageEntry = _SystemImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 100, 1)
)
systemImageEntry.setIndexNames(
    (0, "WILAN-120-58-MIB", "systemImageNumber"),
)
if mibBuilder.loadTexts:
    systemImageEntry.setStatus("current")
_SystemImageNumber_Type = Integer32
_SystemImageNumber_Object = MibTableColumn
systemImageNumber = _SystemImageNumber_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 100, 1, 1),
    _SystemImageNumber_Type()
)
systemImageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemImageNumber.setStatus("current")


class _SystemImageName_Type(DisplayString):
    """Custom type systemImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SystemImageName_Type.__name__ = "DisplayString"
_SystemImageName_Object = MibTableColumn
systemImageName = _SystemImageName_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 100, 1, 2),
    _SystemImageName_Type()
)
systemImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemImageName.setStatus("current")


class _SystemImageRevn_Type(DisplayString):
    """Custom type systemImageRevn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SystemImageRevn_Type.__name__ = "DisplayString"
_SystemImageRevn_Object = MibTableColumn
systemImageRevn = _SystemImageRevn_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 100, 1, 3),
    _SystemImageRevn_Type()
)
systemImageRevn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemImageRevn.setStatus("current")


class _SystemImageDate_Type(DisplayString):
    """Custom type systemImageDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SystemImageDate_Type.__name__ = "DisplayString"
_SystemImageDate_Object = MibTableColumn
systemImageDate = _SystemImageDate_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 100, 1, 4),
    _SystemImageDate_Type()
)
systemImageDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemImageDate.setStatus("current")


class _SystemImageTime_Type(DisplayString):
    """Custom type systemImageTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SystemImageTime_Type.__name__ = "DisplayString"
_SystemImageTime_Object = MibTableColumn
systemImageTime = _SystemImageTime_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 100, 1, 5),
    _SystemImageTime_Type()
)
systemImageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemImageTime.setStatus("current")
_SystemImageSize_Type = Integer32
_SystemImageSize_Object = MibTableColumn
systemImageSize = _SystemImageSize_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 100, 1, 6),
    _SystemImageSize_Type()
)
systemImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemImageSize.setStatus("current")


class _SystemImageText_Type(DisplayString):
    """Custom type systemImageText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SystemImageText_Type.__name__ = "DisplayString"
_SystemImageText_Object = MibTableColumn
systemImageText = _SystemImageText_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 100, 1, 7),
    _SystemImageText_Type()
)
systemImageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemImageText.setStatus("current")
_Config101_Type = Integer32
_Config101_Object = MibScalar
config101 = _Config101_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 101),
    _Config101_Type()
)
config101.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config101.setStatus("current")
_Config102_Type = Integer32
_Config102_Object = MibScalar
config102 = _Config102_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 102),
    _Config102_Type()
)
config102.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config102.setStatus("current")
_Config103_Type = Integer32
_Config103_Object = MibScalar
config103 = _Config103_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 103),
    _Config103_Type()
)
config103.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config103.setStatus("current")
_Config104_Type = Integer32
_Config104_Object = MibScalar
config104 = _Config104_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 1, 104),
    _Config104_Type()
)
config104.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config104.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2686, 2, 2)
)
_TotalHours_Type = Counter32
_TotalHours_Object = MibScalar
totalHours = _TotalHours_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 2, 1),
    _TotalHours_Type()
)
totalHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalHours.setStatus("current")
_SystemHours_Type = Counter32
_SystemHours_Object = MibScalar
systemHours = _SystemHours_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 2, 2),
    _SystemHours_Type()
)
systemHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHours.setStatus("current")
_LoginOkays_Type = Counter32
_LoginOkays_Object = MibScalar
loginOkays = _LoginOkays_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 2, 3),
    _LoginOkays_Type()
)
loginOkays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginOkays.setStatus("current")
_LoginFails_Type = Counter32
_LoginFails_Object = MibScalar
loginFails = _LoginFails_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 2, 4),
    _LoginFails_Type()
)
loginFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginFails.setStatus("current")


class _LocalUser_Type(Integer32):
    """Custom type localUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("supervisor", 2),
          ("user", 1))
    )


_LocalUser_Type.__name__ = "Integer32"
_LocalUser_Object = MibScalar
localUser = _LocalUser_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 2, 5),
    _LocalUser_Type()
)
localUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localUser.setStatus("current")


class _TelnetUser_Type(Integer32):
    """Custom type telnetUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("supervisor", 2),
          ("user", 1))
    )


_TelnetUser_Type.__name__ = "Integer32"
_TelnetUser_Object = MibScalar
telnetUser = _TelnetUser_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 2, 6),
    _TelnetUser_Type()
)
telnetUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetUser.setStatus("current")


class _FtpUser_Type(Integer32):
    """Custom type ftpUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("supervisor", 2),
          ("user", 1))
    )


_FtpUser_Type.__name__ = "Integer32"
_FtpUser_Object = MibScalar
ftpUser = _FtpUser_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 2, 7),
    _FtpUser_Type()
)
ftpUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUser.setStatus("current")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3)
)
_EtherRxTotalPkts_Type = Counter32
_EtherRxTotalPkts_Object = MibScalar
etherRxTotalPkts = _EtherRxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 1),
    _EtherRxTotalPkts_Type()
)
etherRxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherRxTotalPkts.setStatus("current")
_EtherRxLocalPkts_Type = Counter32
_EtherRxLocalPkts_Object = MibScalar
etherRxLocalPkts = _EtherRxLocalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 2),
    _EtherRxLocalPkts_Type()
)
etherRxLocalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherRxLocalPkts.setStatus("current")
_EtherRxErrorPkts_Type = Counter32
_EtherRxErrorPkts_Object = MibScalar
etherRxErrorPkts = _EtherRxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 3),
    _EtherRxErrorPkts_Type()
)
etherRxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherRxErrorPkts.setStatus("current")
_EtherRxDroppedPkts_Type = Counter32
_EtherRxDroppedPkts_Object = MibScalar
etherRxDroppedPkts = _EtherRxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 4),
    _EtherRxDroppedPkts_Type()
)
etherRxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherRxDroppedPkts.setStatus("current")
_EtherRxDiscardPkts_Type = Counter32
_EtherRxDiscardPkts_Object = MibScalar
etherRxDiscardPkts = _EtherRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 5),
    _EtherRxDiscardPkts_Type()
)
etherRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherRxDiscardPkts.setStatus("current")
_EtherRxTotalKbytes_Type = Counter32
_EtherRxTotalKbytes_Object = MibScalar
etherRxTotalKbytes = _EtherRxTotalKbytes_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 6),
    _EtherRxTotalKbytes_Type()
)
etherRxTotalKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherRxTotalKbytes.setStatus("current")
_EtherRxBcastKbytes_Type = Counter32
_EtherRxBcastKbytes_Object = MibScalar
etherRxBcastKbytes = _EtherRxBcastKbytes_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 7),
    _EtherRxBcastKbytes_Type()
)
etherRxBcastKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherRxBcastKbytes.setStatus("current")
_EtherTxTotalPkts_Type = Counter32
_EtherTxTotalPkts_Object = MibScalar
etherTxTotalPkts = _EtherTxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 8),
    _EtherTxTotalPkts_Type()
)
etherTxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTxTotalPkts.setStatus("current")
_EtherTxDroppedPkts_Type = Counter32
_EtherTxDroppedPkts_Object = MibScalar
etherTxDroppedPkts = _EtherTxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 9),
    _EtherTxDroppedPkts_Type()
)
etherTxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTxDroppedPkts.setStatus("current")
_EtherTxTotalKbytes_Type = Counter32
_EtherTxTotalKbytes_Object = MibScalar
etherTxTotalKbytes = _EtherTxTotalKbytes_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 10),
    _EtherTxTotalKbytes_Type()
)
etherTxTotalKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTxTotalKbytes.setStatus("current")
_EtherTxBcastKbytes_Type = Counter32
_EtherTxBcastKbytes_Object = MibScalar
etherTxBcastKbytes = _EtherTxBcastKbytes_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 11),
    _EtherTxBcastKbytes_Type()
)
etherTxBcastKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTxBcastKbytes.setStatus("current")
_RfRxTotalPkts_Type = Counter32
_RfRxTotalPkts_Object = MibScalar
rfRxTotalPkts = _RfRxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 12),
    _RfRxTotalPkts_Type()
)
rfRxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxTotalPkts.setStatus("current")
_RfRxLocalPkts_Type = Counter32
_RfRxLocalPkts_Object = MibScalar
rfRxLocalPkts = _RfRxLocalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 13),
    _RfRxLocalPkts_Type()
)
rfRxLocalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxLocalPkts.setStatus("current")
_RfRxDroppedPkts_Type = Counter32
_RfRxDroppedPkts_Object = MibScalar
rfRxDroppedPkts = _RfRxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 14),
    _RfRxDroppedPkts_Type()
)
rfRxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxDroppedPkts.setStatus("current")
_RfRxDiscardedPkts_Type = Counter32
_RfRxDiscardedPkts_Object = MibScalar
rfRxDiscardedPkts = _RfRxDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 15),
    _RfRxDiscardedPkts_Type()
)
rfRxDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxDiscardedPkts.setStatus("current")
_RfTxTotalPkts_Type = Counter32
_RfTxTotalPkts_Object = MibScalar
rfTxTotalPkts = _RfTxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 16),
    _RfTxTotalPkts_Type()
)
rfTxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTxTotalPkts.setStatus("current")
_RfTxLocalPkts_Type = Counter32
_RfTxLocalPkts_Object = MibScalar
rfTxLocalPkts = _RfTxLocalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 17),
    _RfTxLocalPkts_Type()
)
rfTxLocalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTxLocalPkts.setStatus("current")
_RfTxDroppedPkts_Type = Counter32
_RfTxDroppedPkts_Object = MibScalar
rfTxDroppedPkts = _RfTxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 18),
    _RfTxDroppedPkts_Type()
)
rfTxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTxDroppedPkts.setStatus("current")
_RfRxSframeCount_Type = Counter32
_RfRxSframeCount_Object = MibScalar
rfRxSframeCount = _RfRxSframeCount_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 19),
    _RfRxSframeCount_Type()
)
rfRxSframeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxSframeCount.setStatus("current")
_RfRxOverrunErrors_Type = Counter32
_RfRxOverrunErrors_Object = MibScalar
rfRxOverrunErrors = _RfRxOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 20),
    _RfRxOverrunErrors_Type()
)
rfRxOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxOverrunErrors.setStatus("current")
_RfRxSFrameErrors_Type = Counter32
_RfRxSFrameErrors_Object = MibScalar
rfRxSFrameErrors = _RfRxSFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 21),
    _RfRxSFrameErrors_Type()
)
rfRxSFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxSFrameErrors.setStatus("current")
_RfRxChecksumErrors_Type = Counter32
_RfRxChecksumErrors_Object = MibScalar
rfRxChecksumErrors = _RfRxChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 22),
    _RfRxChecksumErrors_Type()
)
rfRxChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxChecksumErrors.setStatus("current")
_RfRxPacketErrors_Type = Counter32
_RfRxPacketErrors_Object = MibScalar
rfRxPacketErrors = _RfRxPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 23),
    _RfRxPacketErrors_Type()
)
rfRxPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxPacketErrors.setStatus("current")
_RfRxLengthErrors_Type = Counter32
_RfRxLengthErrors_Object = MibScalar
rfRxLengthErrors = _RfRxLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 24),
    _RfRxLengthErrors_Type()
)
rfRxLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxLengthErrors.setStatus("current")
_RfTxSuperFrameCnt_Type = Counter32
_RfTxSuperFrameCnt_Object = MibScalar
rfTxSuperFrameCnt = _RfTxSuperFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 25),
    _RfTxSuperFrameCnt_Type()
)
rfTxSuperFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTxSuperFrameCnt.setStatus("current")
_RfEtoIThroughput_Type = Counter32
_RfEtoIThroughput_Object = MibScalar
rfEtoIThroughput = _RfEtoIThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 26),
    _RfEtoIThroughput_Type()
)
rfEtoIThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfEtoIThroughput.setStatus("current")
_RfItoEThroughput_Type = Counter32
_RfItoEThroughput_Object = MibScalar
rfItoEThroughput = _RfItoEThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 27),
    _RfItoEThroughput_Type()
)
rfItoEThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfItoEThroughput.setStatus("current")
_Statistics24_Type = Counter32
_Statistics24_Object = MibScalar
statistics24 = _Statistics24_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 28),
    _Statistics24_Type()
)
statistics24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statistics24.setStatus("current")
_LinkMonitorRank1_Type = Integer32
_LinkMonitorRank1_Object = MibScalar
linkMonitorRank1 = _LinkMonitorRank1_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 29),
    _LinkMonitorRank1_Type()
)
linkMonitorRank1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkMonitorRank1.setStatus("current")


class _LinkMonRtoBber_Type(DisplayString):
    """Custom type linkMonRtoBber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LinkMonRtoBber_Type.__name__ = "DisplayString"
_LinkMonRtoBber_Object = MibScalar
linkMonRtoBber = _LinkMonRtoBber_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 30),
    _LinkMonRtoBber_Type()
)
linkMonRtoBber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkMonRtoBber.setStatus("current")


class _LinkMonBtoRber_Type(DisplayString):
    """Custom type linkMonBtoRber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LinkMonBtoRber_Type.__name__ = "DisplayString"
_LinkMonBtoRber_Object = MibScalar
linkMonBtoRber = _LinkMonBtoRber_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 31),
    _LinkMonBtoRber_Type()
)
linkMonBtoRber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkMonBtoRber.setStatus("current")
_LinkMonMissPktCnt_Type = Counter32
_LinkMonMissPktCnt_Object = MibScalar
linkMonMissPktCnt = _LinkMonMissPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 32),
    _LinkMonMissPktCnt_Type()
)
linkMonMissPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkMonMissPktCnt.setStatus("current")
_LinkMonEnvPBtoR_Type = Integer32
_LinkMonEnvPBtoR_Object = MibScalar
linkMonEnvPBtoR = _LinkMonEnvPBtoR_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 33),
    _LinkMonEnvPBtoR_Type()
)
linkMonEnvPBtoR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkMonEnvPBtoR.setStatus("current")
_LinkMonEnvPRtoB_Type = Integer32
_LinkMonEnvPRtoB_Object = MibScalar
linkMonEnvPRtoB = _LinkMonEnvPRtoB_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 34),
    _LinkMonEnvPRtoB_Type()
)
linkMonEnvPRtoB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkMonEnvPRtoB.setStatus("current")
_LinkMonCorrPBtoR_Type = Integer32
_LinkMonCorrPBtoR_Object = MibScalar
linkMonCorrPBtoR = _LinkMonCorrPBtoR_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 35),
    _LinkMonCorrPBtoR_Type()
)
linkMonCorrPBtoR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkMonCorrPBtoR.setStatus("current")
_LinkMonCorrPRtoB_Type = Integer32
_LinkMonCorrPRtoB_Object = MibScalar
linkMonCorrPRtoB = _LinkMonCorrPRtoB_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 3, 36),
    _LinkMonCorrPRtoB_Type()
)
linkMonCorrPRtoB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkMonCorrPRtoB.setStatus("current")
_Commands_ObjectIdentity = ObjectIdentity
commands = _Commands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2686, 2, 4)
)


class _RebootCurrent_Type(Integer32):
    """Custom type rebootCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_RebootCurrent_Type.__name__ = "Integer32"
_RebootCurrent_Object = MibScalar
rebootCurrent = _RebootCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 4, 1),
    _RebootCurrent_Type()
)
rebootCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootCurrent.setStatus("current")


class _RebootImage_Type(DisplayString):
    """Custom type rebootImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RebootImage_Type.__name__ = "DisplayString"
_RebootImage_Object = MibScalar
rebootImage = _RebootImage_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 4, 2),
    _RebootImage_Type()
)
rebootImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootImage.setStatus("current")


class _RebootNewRfConfig_Type(Integer32):
    """Custom type rebootNewRfConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_RebootNewRfConfig_Type.__name__ = "Integer32"
_RebootNewRfConfig_Object = MibScalar
rebootNewRfConfig = _RebootNewRfConfig_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 4, 3),
    _RebootNewRfConfig_Type()
)
rebootNewRfConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootNewRfConfig.setStatus("current")


class _RestFactConfReboot_Type(Integer32):
    """Custom type restFactConfReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restore", 1)
    )


_RestFactConfReboot_Type.__name__ = "Integer32"
_RestFactConfReboot_Object = MibScalar
restFactConfReboot = _RestFactConfReboot_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 4, 4),
    _RestFactConfReboot_Type()
)
restFactConfReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restFactConfReboot.setStatus("current")


class _SaveConfToFlash_Type(Integer32):
    """Custom type saveConfToFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_SaveConfToFlash_Type.__name__ = "Integer32"
_SaveConfToFlash_Object = MibScalar
saveConfToFlash = _SaveConfToFlash_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 4, 5),
    _SaveConfToFlash_Type()
)
saveConfToFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveConfToFlash.setStatus("current")


class _ResetRadioStats_Type(Integer32):
    """Custom type resetRadioStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ResetRadioStats_Type.__name__ = "Integer32"
_ResetRadioStats_Object = MibScalar
resetRadioStats = _ResetRadioStats_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 4, 6),
    _ResetRadioStats_Type()
)
resetRadioStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetRadioStats.setStatus("current")


class _ResetEthernetStats_Type(Integer32):
    """Custom type resetEthernetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ResetEthernetStats_Type.__name__ = "Integer32"
_ResetEthernetStats_Object = MibScalar
resetEthernetStats = _ResetEthernetStats_Object(
    (1, 3, 6, 1, 4, 1, 2686, 2, 4, 7),
    _ResetEthernetStats_Type()
)
resetEthernetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetEthernetStats.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WILAN-120-58-MIB",
    **{"wilan": wilan,
       "awe120-58": awe120_58,
       "config": config,
       "serialNumber": serialNumber,
       "productionDate": productionDate,
       "macAddress": macAddress,
       "systemName": systemName,
       "unitLocation": unitLocation,
       "contactName": contactName,
       "config7": config7,
       "config8": config8,
       "config9": config9,
       "ipAddress": ipAddress,
       "ipNewAddress": ipNewAddress,
       "ipSubnetMask": ipSubnetMask,
       "ipGatewayAddr": ipGatewayAddr,
       "ipNetmanAddr": ipNetmanAddr,
       "ipPacketFiltering": ipPacketFiltering,
       "ipAddressFiltering": ipAddressFiltering,
       "ipFilter1Range": ipFilter1Range,
       "ipFilter1Base": ipFilter1Base,
       "ipFilter2Range": ipFilter2Range,
       "ipFilter2Base": ipFilter2Base,
       "ipFilter3Range": ipFilter3Range,
       "ipFilter3Base": ipFilter3Base,
       "ipFilter4Range": ipFilter4Range,
       "ipFilter4Base": ipFilter4Base,
       "ipFilter5Range": ipFilter5Range,
       "ipFilter5Base": ipFilter5Base,
       "macFilterEntryAge": macFilterEntryAge,
       "config28": config28,
       "config29": config29,
       "stationType": stationType,
       "stationRank": stationRank,
       "centerFreq": centerFreq,
       "securityWord1": securityWord1,
       "securityWord2": securityWord2,
       "securityWord3": securityWord3,
       "securityWord4": securityWord4,
       "securityWord5": securityWord5,
       "scramblingCode": scramblingCode,
       "acquisitionCode": acquisitionCode,
       "configMinutes": configMinutes,
       "repeaterMode": repeaterMode,
       "systemType": systemType,
       "remoteGroup": remoteGroup,
       "numOfPollRounds": numOfPollRounds,
       "txPwrLevelAdj": txPwrLevelAdj,
       "defStationType": defStationType,
       "defStationRank": defStationRank,
       "defCenterFreq": defCenterFreq,
       "defSecurityWord1": defSecurityWord1,
       "defSecurityWord2": defSecurityWord2,
       "defSecurityWord3": defSecurityWord3,
       "defSecurityWord4": defSecurityWord4,
       "defSecurityWord5": defSecurityWord5,
       "defScramblingCode": defScramblingCode,
       "defAcquisitionCode": defAcquisitionCode,
       "defConfigMinutes": defConfigMinutes,
       "defRepeaterMode": defRepeaterMode,
       "defSystemType": defSystemType,
       "defRemoteGroup": defRemoteGroup,
       "defNumOfPollRounds": defNumOfPollRounds,
       "defTxPwrLevelAdj": defTxPwrLevelAdj,
       "newStationType": newStationType,
       "newStationRank": newStationRank,
       "newCenterFreq": newCenterFreq,
       "newSecurityWord1": newSecurityWord1,
       "newSecurityWord2": newSecurityWord2,
       "newSecurityWord3": newSecurityWord3,
       "newSecurityWord4": newSecurityWord4,
       "newSecurityWord5": newSecurityWord5,
       "newScramblingCode": newScramblingCode,
       "newAcquisitionCode": newAcquisitionCode,
       "newConfigMinutes": newConfigMinutes,
       "newRepeaterMode": newRepeaterMode,
       "newSystemType": newSystemType,
       "newRemoteGroup": newRemoteGroup,
       "newNumOfPollRounds": newNumOfPollRounds,
       "newTxPwrLevelAdj": newTxPwrLevelAdj,
       "stationMode": stationMode,
       "rfTransmitStatus": rfTransmitStatus,
       "linkMonitorPeriod": linkMonitorPeriod,
       "testModeTimer": testModeTimer,
       "remoteDistance": remoteDistance,
       "linkMonitorRank": linkMonitorRank,
       "throttleEnable": throttleEnable,
       "throttleLevel": throttleLevel,
       "config86": config86,
       "config87": config87,
       "config88": config88,
       "config89": config89,
       "communityName1": communityName1,
       "communityName2": communityName2,
       "ethernetAccess": ethernetAccess,
       "wirelessAccess": wirelessAccess,
       "config94": config94,
       "currentImage": currentImage,
       "defaultImage": defaultImage,
       "prevDefaultImage": prevDefaultImage,
       "config98": config98,
       "config99": config99,
       "systemImageList": systemImageList,
       "systemImageEntry": systemImageEntry,
       "systemImageNumber": systemImageNumber,
       "systemImageName": systemImageName,
       "systemImageRevn": systemImageRevn,
       "systemImageDate": systemImageDate,
       "systemImageTime": systemImageTime,
       "systemImageSize": systemImageSize,
       "systemImageText": systemImageText,
       "config101": config101,
       "config102": config102,
       "config103": config103,
       "config104": config104,
       "status": status,
       "totalHours": totalHours,
       "systemHours": systemHours,
       "loginOkays": loginOkays,
       "loginFails": loginFails,
       "localUser": localUser,
       "telnetUser": telnetUser,
       "ftpUser": ftpUser,
       "statistics": statistics,
       "etherRxTotalPkts": etherRxTotalPkts,
       "etherRxLocalPkts": etherRxLocalPkts,
       "etherRxErrorPkts": etherRxErrorPkts,
       "etherRxDroppedPkts": etherRxDroppedPkts,
       "etherRxDiscardPkts": etherRxDiscardPkts,
       "etherRxTotalKbytes": etherRxTotalKbytes,
       "etherRxBcastKbytes": etherRxBcastKbytes,
       "etherTxTotalPkts": etherTxTotalPkts,
       "etherTxDroppedPkts": etherTxDroppedPkts,
       "etherTxTotalKbytes": etherTxTotalKbytes,
       "etherTxBcastKbytes": etherTxBcastKbytes,
       "rfRxTotalPkts": rfRxTotalPkts,
       "rfRxLocalPkts": rfRxLocalPkts,
       "rfRxDroppedPkts": rfRxDroppedPkts,
       "rfRxDiscardedPkts": rfRxDiscardedPkts,
       "rfTxTotalPkts": rfTxTotalPkts,
       "rfTxLocalPkts": rfTxLocalPkts,
       "rfTxDroppedPkts": rfTxDroppedPkts,
       "rfRxSframeCount": rfRxSframeCount,
       "rfRxOverrunErrors": rfRxOverrunErrors,
       "rfRxSFrameErrors": rfRxSFrameErrors,
       "rfRxChecksumErrors": rfRxChecksumErrors,
       "rfRxPacketErrors": rfRxPacketErrors,
       "rfRxLengthErrors": rfRxLengthErrors,
       "rfTxSuperFrameCnt": rfTxSuperFrameCnt,
       "rfEtoIThroughput": rfEtoIThroughput,
       "rfItoEThroughput": rfItoEThroughput,
       "statistics24": statistics24,
       "linkMonitorRank1": linkMonitorRank1,
       "linkMonRtoBber": linkMonRtoBber,
       "linkMonBtoRber": linkMonBtoRber,
       "linkMonMissPktCnt": linkMonMissPktCnt,
       "linkMonEnvPBtoR": linkMonEnvPBtoR,
       "linkMonEnvPRtoB": linkMonEnvPRtoB,
       "linkMonCorrPBtoR": linkMonCorrPBtoR,
       "linkMonCorrPRtoB": linkMonCorrPRtoB,
       "commands": commands,
       "rebootCurrent": rebootCurrent,
       "rebootImage": rebootImage,
       "rebootNewRfConfig": rebootNewRfConfig,
       "restFactConfReboot": restFactConfReboot,
       "saveConfToFlash": saveConfToFlash,
       "resetRadioStats": resetRadioStats,
       "resetEthernetStats": resetEthernetStats}
)
