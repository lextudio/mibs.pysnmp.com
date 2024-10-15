# SNMP MIB module (SENAO-ENTERPRISE-INDOOR-AP-CB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SENAO-ENTERPRISE-INDOOR-AP-CB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:19 2024
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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

senao = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14125)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IndoorWirelessDevice_ObjectIdentity = ObjectIdentity
indoorWirelessDevice = _IndoorWirelessDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100)
)
_EntSystem_ObjectIdentity = ObjectIdentity
entSystem = _EntSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1)
)


class _EntPassword_Type(DisplayString):
    """Custom type entPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EntPassword_Type.__name__ = "DisplayString"
_EntPassword_Object = MibScalar
entPassword = _EntPassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1, 2),
    _EntPassword_Type()
)
entPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    entPassword.setStatus("mandatory")
_EntSysModel_Type = DisplayString
_EntSysModel_Object = MibScalar
entSysModel = _EntSysModel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1, 3),
    _EntSysModel_Type()
)
entSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSysModel.setStatus("mandatory")


class _EntSysMode_Type(Integer32):
    """Custom type entSysMode based on Integer32"""
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
        *(("ap-bridge", 2),
          ("ap-router", 0),
          ("client-bridge", 3),
          ("client-router", 4),
          ("repeater", 1),
          ("wds-bridge", 5))
    )


_EntSysMode_Type.__name__ = "Integer32"
_EntSysMode_Object = MibScalar
entSysMode = _EntSysMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1, 4),
    _EntSysMode_Type()
)
entSysMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSysMode.setStatus("mandatory")
_EntSysUpTime_Type = TimeTicks
_EntSysUpTime_Object = MibScalar
entSysUpTime = _EntSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1, 5),
    _EntSysUpTime_Type()
)
entSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSysUpTime.setStatus("mandatory")
_EntHwVersion_Type = DisplayString
_EntHwVersion_Object = MibScalar
entHwVersion = _EntHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1, 6),
    _EntHwVersion_Type()
)
entHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entHwVersion.setStatus("mandatory")
_EntSN_Type = DisplayString
_EntSN_Object = MibScalar
entSN = _EntSN_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1, 7),
    _EntSN_Type()
)
entSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSN.setStatus("mandatory")
_EntKenelVersion_Type = DisplayString
_EntKenelVersion_Object = MibScalar
entKenelVersion = _EntKenelVersion_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1, 8),
    _EntKenelVersion_Type()
)
entKenelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entKenelVersion.setStatus("mandatory")
_EntAppVersion_Type = DisplayString
_EntAppVersion_Object = MibScalar
entAppVersion = _EntAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1, 9),
    _EntAppVersion_Type()
)
entAppVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entAppVersion.setStatus("mandatory")
_EntReset_Type = TruthValue
_EntReset_Object = MibScalar
entReset = _EntReset_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1, 10),
    _EntReset_Type()
)
entReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    entReset.setStatus("mandatory")
_EntResetToDefault_Type = TruthValue
_EntResetToDefault_Object = MibScalar
entResetToDefault = _EntResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1, 11),
    _EntResetToDefault_Type()
)
entResetToDefault.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    entResetToDefault.setStatus("mandatory")
_EntApplyModules_Type = TruthValue
_EntApplyModules_Object = MibScalar
entApplyModules = _EntApplyModules_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 1, 12),
    _EntApplyModules_Type()
)
entApplyModules.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    entApplyModules.setStatus("mandatory")
_EntLAN_ObjectIdentity = ObjectIdentity
entLAN = _EntLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100, 2)
)
_EntLANIP_Type = IpAddress
_EntLANIP_Object = MibScalar
entLANIP = _EntLANIP_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 2, 1),
    _EntLANIP_Type()
)
entLANIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entLANIP.setStatus("mandatory")
_EntLANSubnetMask_Type = IpAddress
_EntLANSubnetMask_Object = MibScalar
entLANSubnetMask = _EntLANSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 2, 2),
    _EntLANSubnetMask_Type()
)
entLANSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entLANSubnetMask.setStatus("mandatory")
_EntSTPEnable_Type = TruthValue
_EntSTPEnable_Object = MibScalar
entSTPEnable = _EntSTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 2, 3),
    _EntSTPEnable_Type()
)
entSTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entSTPEnable.setStatus("mandatory")
_EntDHCPEnable_Type = TruthValue
_EntDHCPEnable_Object = MibScalar
entDHCPEnable = _EntDHCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 2, 4),
    _EntDHCPEnable_Type()
)
entDHCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entDHCPEnable.setStatus("mandatory")
_EntIPPoolStart_Type = IpAddress
_EntIPPoolStart_Object = MibScalar
entIPPoolStart = _EntIPPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 2, 5),
    _EntIPPoolStart_Type()
)
entIPPoolStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entIPPoolStart.setStatus("mandatory")
_EntIPPoolEnd_Type = IpAddress
_EntIPPoolEnd_Object = MibScalar
entIPPoolEnd = _EntIPPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 2, 6),
    _EntIPPoolEnd_Type()
)
entIPPoolEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entIPPoolEnd.setStatus("mandatory")


class _EntIPLeaseTime_Type(Integer32):
    """Custom type entIPLeaseTime based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("forever", 8),
          ("half-day", 3),
          ("half-hour", 0),
          ("one-day", 4),
          ("one-hour", 1),
          ("one-week", 6),
          ("two-days", 5),
          ("two-hours", 2),
          ("two-weeks", 7))
    )


_EntIPLeaseTime_Type.__name__ = "Integer32"
_EntIPLeaseTime_Object = MibScalar
entIPLeaseTime = _EntIPLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 2, 7),
    _EntIPLeaseTime_Type()
)
entIPLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entIPLeaseTime.setStatus("mandatory")
_EntWAN_ObjectIdentity = ObjectIdentity
entWAN = _EntWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100, 3)
)
_EntRouterEnable_Type = TruthValue
_EntRouterEnable_Object = MibScalar
entRouterEnable = _EntRouterEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 3, 1),
    _EntRouterEnable_Type()
)
entRouterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entRouterEnable.setStatus("mandatory")
_EntMacFilter_ObjectIdentity = ObjectIdentity
entMacFilter = _EntMacFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100, 4)
)
_EntLanMacFilteringEnable_Type = TruthValue
_EntLanMacFilteringEnable_Object = MibScalar
entLanMacFilteringEnable = _EntLanMacFilteringEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 4, 1),
    _EntLanMacFilteringEnable_Type()
)
entLanMacFilteringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entLanMacFilteringEnable.setStatus("mandatory")


class _EntLanMacFilteringMode_Type(Integer32):
    """Custom type entLanMacFilteringMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("black-list", 1),
          ("white-list", 0))
    )


_EntLanMacFilteringMode_Type.__name__ = "Integer32"
_EntLanMacFilteringMode_Object = MibScalar
entLanMacFilteringMode = _EntLanMacFilteringMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 4, 2),
    _EntLanMacFilteringMode_Type()
)
entLanMacFilteringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entLanMacFilteringMode.setStatus("mandatory")
_EntLanMacFilterTable_Object = MibTable
entLanMacFilterTable = _EntLanMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 4, 3)
)
if mibBuilder.loadTexts:
    entLanMacFilterTable.setStatus("current")
_EntLanMacFilterEntry_Object = MibTableRow
entLanMacFilterEntry = _EntLanMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 4, 3, 1)
)
entLanMacFilterEntry.setIndexNames(
    (0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entMacAddressIndex"),
)
if mibBuilder.loadTexts:
    entLanMacFilterEntry.setStatus("current")
_EntMacAddressIndex_Type = Integer32
_EntMacAddressIndex_Object = MibTableColumn
entMacAddressIndex = _EntMacAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 4, 3, 1, 1),
    _EntMacAddressIndex_Type()
)
entMacAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entMacAddressIndex.setStatus("current")
_EntMacAddress_Type = DisplayString
_EntMacAddress_Object = MibTableColumn
entMacAddress = _EntMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 4, 3, 1, 2),
    _EntMacAddress_Type()
)
entMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entMacAddress.setStatus("current")
_EntMacFilteringValid_Type = TruthValue
_EntMacFilteringValid_Object = MibTableColumn
entMacFilteringValid = _EntMacFilteringValid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 4, 3, 1, 3),
    _EntMacFilteringValid_Type()
)
entMacFilteringValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entMacFilteringValid.setStatus("current")
_EntWlan_ObjectIdentity = ObjectIdentity
entWlan = _EntWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5)
)
_EntWlanCommonInfo_ObjectIdentity = ObjectIdentity
entWlanCommonInfo = _EntWlanCommonInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1)
)


class _EntOpMode_Type(Integer32):
    """Custom type entOpMode based on Integer32"""
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
        *(("ap", 0),
          ("client-bridge", 1),
          ("repeater", 3),
          ("wds-bridge", 2))
    )


_EntOpMode_Type.__name__ = "Integer32"
_EntOpMode_Object = MibScalar
entOpMode = _EntOpMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 1),
    _EntOpMode_Type()
)
entOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entOpMode.setStatus("mandatory")
_EntRadio_Type = TruthValue
_EntRadio_Object = MibScalar
entRadio = _EntRadio_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 2),
    _EntRadio_Type()
)
entRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entRadio.setStatus("mandatory")


class _EntAPMode_Type(Integer32):
    """Custom type entAPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ap", 0),
          ("wds", 1))
    )


_EntAPMode_Type.__name__ = "Integer32"
_EntAPMode_Object = MibScalar
entAPMode = _EntAPMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 3),
    _EntAPMode_Type()
)
entAPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entAPMode.setStatus("mandatory")


class _EntBand_Type(Integer32):
    """Custom type entBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11-a", 2),
          ("ieee802dot11-a-n", 8),
          ("ieee802dot11-b", 1),
          ("ieee802dot11-b-g", 0),
          ("ieee802dot11-b-g-n", 9),
          ("ieee802dot11-g", 4),
          ("ieee802dot11-g-n", 7),
          ("ieee802dot11-n", 6))
    )


_EntBand_Type.__name__ = "Integer32"
_EntBand_Object = MibScalar
entBand = _EntBand_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 4),
    _EntBand_Type()
)
entBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entBand.setStatus("mandatory")


class _EntESSIDNum_Type(Integer32):
    """Custom type entESSIDNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EntESSIDNum_Type.__name__ = "Integer32"
_EntESSIDNum_Object = MibScalar
entESSIDNum = _EntESSIDNum_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 5),
    _EntESSIDNum_Type()
)
entESSIDNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entESSIDNum.setStatus("mandatory")


class _EntChannel_Type(Integer32):
    """Custom type entChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_EntChannel_Type.__name__ = "Integer32"
_EntChannel_Object = MibScalar
entChannel = _EntChannel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 6),
    _EntChannel_Type()
)
entChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entChannel.setStatus("mandatory")


class _EntDataRate_Type(Integer32):
    """Custom type entDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              6,
              9,
              11,
              12,
              18,
              24,
              36,
              48,
              54)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("eighteenMbps", 18),
          ("elevenMbps", 11),
          ("fiftyfourMbps", 54),
          ("fiveNhalfMbps", 5),
          ("fortyeightMbps", 48),
          ("nineMbps", 9),
          ("oneMbps", 1),
          ("sixMbps", 6),
          ("thirtysixMbps", 36),
          ("twelveMbps", 12),
          ("twentytwoMbps", 24),
          ("twoMbps", 2))
    )


_EntDataRate_Type.__name__ = "Integer32"
_EntDataRate_Object = MibScalar
entDataRate = _EntDataRate_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 7),
    _EntDataRate_Type()
)
entDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entDataRate.setStatus("mandatory")
_EntNDataRate_Type = Integer32
_EntNDataRate_Object = MibScalar
entNDataRate = _EntNDataRate_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 8),
    _EntNDataRate_Type()
)
entNDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entNDataRate.setStatus("mandatory")
_EntTxPower_Type = Integer32
_EntTxPower_Object = MibScalar
entTxPower = _EntTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 9),
    _EntTxPower_Type()
)
entTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entTxPower.setStatus("mandatory")


class _EntBeaconInterval_Type(Integer32):
    """Custom type entBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1024),
    )


_EntBeaconInterval_Type.__name__ = "Integer32"
_EntBeaconInterval_Object = MibScalar
entBeaconInterval = _EntBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 10),
    _EntBeaconInterval_Type()
)
entBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entBeaconInterval.setStatus("mandatory")


class _EntDTIMPeriod_Type(Integer32):
    """Custom type entDTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EntDTIMPeriod_Type.__name__ = "Integer32"
_EntDTIMPeriod_Object = MibScalar
entDTIMPeriod = _EntDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 11),
    _EntDTIMPeriod_Type()
)
entDTIMPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entDTIMPeriod.setStatus("mandatory")


class _EntFragmentationThreshold_Type(Integer32):
    """Custom type entFragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_EntFragmentationThreshold_Type.__name__ = "Integer32"
_EntFragmentationThreshold_Object = MibScalar
entFragmentationThreshold = _EntFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 12),
    _EntFragmentationThreshold_Type()
)
entFragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entFragmentationThreshold.setStatus("mandatory")


class _EntRTSThreshold_Type(Integer32):
    """Custom type entRTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_EntRTSThreshold_Type.__name__ = "Integer32"
_EntRTSThreshold_Object = MibScalar
entRTSThreshold = _EntRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 13),
    _EntRTSThreshold_Type()
)
entRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entRTSThreshold.setStatus("mandatory")


class _EntChannelBandwidth_Type(Integer32):
    """Custom type entChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EntChannelBandwidth_Type.__name__ = "Integer32"
_EntChannelBandwidth_Object = MibScalar
entChannelBandwidth = _EntChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 14),
    _EntChannelBandwidth_Type()
)
entChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entChannelBandwidth.setStatus("mandatory")


class _EntPreambleType_Type(Integer32):
    """Custom type entPreambleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_EntPreambleType_Type.__name__ = "Integer32"
_EntPreambleType_Object = MibScalar
entPreambleType = _EntPreambleType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 15),
    _EntPreambleType_Type()
)
entPreambleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entPreambleType.setStatus("mandatory")


class _EntCTSProtection_Type(Integer32):
    """Custom type entCTSProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("auto", 0),
          ("none", 2))
    )


_EntCTSProtection_Type.__name__ = "Integer32"
_EntCTSProtection_Object = MibScalar
entCTSProtection = _EntCTSProtection_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 1, 16),
    _EntCTSProtection_Type()
)
entCTSProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entCTSProtection.setStatus("mandatory")
_EntWlanESSIDInfoTable_Object = MibTable
entWlanESSIDInfoTable = _EntWlanESSIDInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 2)
)
if mibBuilder.loadTexts:
    entWlanESSIDInfoTable.setStatus("current")
_EntWlanESSIDInfoEntry_Object = MibTableRow
entWlanESSIDInfoEntry = _EntWlanESSIDInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1)
)
entWlanESSIDInfoEntry.setIndexNames(
    (0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entWlanESSIDInfoIndex"),
)
if mibBuilder.loadTexts:
    entWlanESSIDInfoEntry.setStatus("current")
_EntWlanESSIDInfoIndex_Type = Integer32
_EntWlanESSIDInfoIndex_Object = MibTableColumn
entWlanESSIDInfoIndex = _EntWlanESSIDInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 1),
    _EntWlanESSIDInfoIndex_Type()
)
entWlanESSIDInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entWlanESSIDInfoIndex.setStatus("current")


class _EntESSID_Type(OctetString):
    """Custom type entESSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EntESSID_Type.__name__ = "OctetString"
_EntESSID_Object = MibTableColumn
entESSID = _EntESSID_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 2),
    _EntESSID_Type()
)
entESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entESSID.setStatus("current")
_EntBroadcastESSID_Type = TruthValue
_EntBroadcastESSID_Object = MibTableColumn
entBroadcastESSID = _EntBroadcastESSID_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 3),
    _EntBroadcastESSID_Type()
)
entBroadcastESSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entBroadcastESSID.setStatus("mandatory")
_EntWMM_Type = TruthValue
_EntWMM_Object = MibTableColumn
entWMM = _EntWMM_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 4),
    _EntWMM_Type()
)
entWMM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entWMM.setStatus("mandatory")


class _EntEncryption_Type(Integer32):
    """Custom type entEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_EntEncryption_Type.__name__ = "Integer32"
_EntEncryption_Object = MibTableColumn
entEncryption = _EntEncryption_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 5),
    _EntEncryption_Type()
)
entEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entEncryption.setStatus("current")


class _EntWlanAuthenticationType_Type(Integer32):
    """Custom type entWlanAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_EntWlanAuthenticationType_Type.__name__ = "Integer32"
_EntWlanAuthenticationType_Object = MibTableColumn
entWlanAuthenticationType = _EntWlanAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 2, 1, 6),
    _EntWlanAuthenticationType_Type()
)
entWlanAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entWlanAuthenticationType.setStatus("current")
_EntWlanWepInfoTable_Object = MibTable
entWlanWepInfoTable = _EntWlanWepInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 3)
)
if mibBuilder.loadTexts:
    entWlanWepInfoTable.setStatus("current")
_EntWlanWepInfoEntry_Object = MibTableRow
entWlanWepInfoEntry = _EntWlanWepInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1)
)
entWlanWepInfoEntry.setIndexNames(
    (0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entWlanESSIDIndex"),
)
if mibBuilder.loadTexts:
    entWlanWepInfoEntry.setStatus("current")
_EntWlanESSIDIndex_Type = Integer32
_EntWlanESSIDIndex_Object = MibTableColumn
entWlanESSIDIndex = _EntWlanESSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 1),
    _EntWlanESSIDIndex_Type()
)
entWlanESSIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entWlanESSIDIndex.setStatus("current")


class _EntWlanWepKeyID_Type(Integer32):
    """Custom type entWlanWepKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EntWlanWepKeyID_Type.__name__ = "Integer32"
_EntWlanWepKeyID_Object = MibTableColumn
entWlanWepKeyID = _EntWlanWepKeyID_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 2),
    _EntWlanWepKeyID_Type()
)
entWlanWepKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entWlanWepKeyID.setStatus("current")
_EntWlanWepKey1Value_Type = OctetString
_EntWlanWepKey1Value_Object = MibTableColumn
entWlanWepKey1Value = _EntWlanWepKey1Value_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 3),
    _EntWlanWepKey1Value_Type()
)
entWlanWepKey1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entWlanWepKey1Value.setStatus("current")
_EntWlanWepKey2Value_Type = OctetString
_EntWlanWepKey2Value_Object = MibTableColumn
entWlanWepKey2Value = _EntWlanWepKey2Value_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 4),
    _EntWlanWepKey2Value_Type()
)
entWlanWepKey2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entWlanWepKey2Value.setStatus("current")
_EntWlanWepKey3Value_Type = OctetString
_EntWlanWepKey3Value_Object = MibTableColumn
entWlanWepKey3Value = _EntWlanWepKey3Value_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 5),
    _EntWlanWepKey3Value_Type()
)
entWlanWepKey3Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entWlanWepKey3Value.setStatus("current")
_EntWlanWepKey4Value_Type = OctetString
_EntWlanWepKey4Value_Object = MibTableColumn
entWlanWepKey4Value = _EntWlanWepKey4Value_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 3, 1, 6),
    _EntWlanWepKey4Value_Type()
)
entWlanWepKey4Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entWlanWepKey4Value.setStatus("current")
_EntWlanWPAInfoTable_Object = MibTable
entWlanWPAInfoTable = _EntWlanWPAInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 4)
)
if mibBuilder.loadTexts:
    entWlanWPAInfoTable.setStatus("current")
_EntWlanWPAInfoEntry_Object = MibTableRow
entWlanWPAInfoEntry = _EntWlanWPAInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 4, 1)
)
entWlanWPAInfoEntry.setIndexNames(
    (0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entWlanWPAESSIDIndex"),
)
if mibBuilder.loadTexts:
    entWlanWPAInfoEntry.setStatus("current")
_EntWlanWPAESSIDIndex_Type = Integer32
_EntWlanWPAESSIDIndex_Object = MibTableColumn
entWlanWPAESSIDIndex = _EntWlanWPAESSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 4, 1, 1),
    _EntWlanWPAESSIDIndex_Type()
)
entWlanWPAESSIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entWlanWPAESSIDIndex.setStatus("current")
_EntPresharedKey_Type = DisplayString
_EntPresharedKey_Object = MibTableColumn
entPresharedKey = _EntPresharedKey_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 4, 1, 2),
    _EntPresharedKey_Type()
)
entPresharedKey.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    entPresharedKey.setStatus("current")
_Ent802dot1xInfoTable_Object = MibTable
ent802dot1xInfoTable = _Ent802dot1xInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 5)
)
if mibBuilder.loadTexts:
    ent802dot1xInfoTable.setStatus("current")
_Ent802dot1xInfoEntry_Object = MibTableRow
ent802dot1xInfoEntry = _Ent802dot1xInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1)
)
ent802dot1xInfoEntry.setIndexNames(
    (0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entWlan802dot1xESSIDIndex"),
)
if mibBuilder.loadTexts:
    ent802dot1xInfoEntry.setStatus("current")
_EntWlan802dot1xESSIDIndex_Type = Integer32
_EntWlan802dot1xESSIDIndex_Object = MibTableColumn
entWlan802dot1xESSIDIndex = _EntWlan802dot1xESSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1, 1),
    _EntWlan802dot1xESSIDIndex_Type()
)
entWlan802dot1xESSIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entWlan802dot1xESSIDIndex.setStatus("current")
_EntRADIUSServerIPAddress_Type = IpAddress
_EntRADIUSServerIPAddress_Object = MibTableColumn
entRADIUSServerIPAddress = _EntRADIUSServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1, 2),
    _EntRADIUSServerIPAddress_Type()
)
entRADIUSServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entRADIUSServerIPAddress.setStatus("current")


class _EntRADIUSServerPort_Type(Integer32):
    """Custom type entRADIUSServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EntRADIUSServerPort_Type.__name__ = "Integer32"
_EntRADIUSServerPort_Object = MibTableColumn
entRADIUSServerPort = _EntRADIUSServerPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1, 3),
    _EntRADIUSServerPort_Type()
)
entRADIUSServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entRADIUSServerPort.setStatus("current")
_EntRADIUSServerPassword_Type = DisplayString
_EntRADIUSServerPassword_Object = MibTableColumn
entRADIUSServerPassword = _EntRADIUSServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1, 4),
    _EntRADIUSServerPassword_Type()
)
entRADIUSServerPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    entRADIUSServerPassword.setStatus("current")
_EntWlan802dot1xEnable_Type = TruthValue
_EntWlan802dot1xEnable_Object = MibTableColumn
entWlan802dot1xEnable = _EntWlan802dot1xEnable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 5, 1, 5),
    _EntWlan802dot1xEnable_Type()
)
entWlan802dot1xEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entWlan802dot1xEnable.setStatus("current")
_EntWlanClientListInfoTable_Object = MibTable
entWlanClientListInfoTable = _EntWlanClientListInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 6)
)
if mibBuilder.loadTexts:
    entWlanClientListInfoTable.setStatus("current")
_EntWlanClientListInfoEntry_Object = MibTableRow
entWlanClientListInfoEntry = _EntWlanClientListInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1)
)
entWlanClientListInfoEntry.setIndexNames(
    (0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entCLInfoIndex"),
)
if mibBuilder.loadTexts:
    entWlanClientListInfoEntry.setStatus("current")
_EntCLInfoIndex_Type = Integer32
_EntCLInfoIndex_Object = MibTableColumn
entCLInfoIndex = _EntCLInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 1),
    _EntCLInfoIndex_Type()
)
entCLInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entCLInfoIndex.setStatus("current")
_EntCLInterface_Type = OctetString
_EntCLInterface_Object = MibTableColumn
entCLInterface = _EntCLInterface_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 2),
    _EntCLInterface_Type()
)
entCLInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entCLInterface.setStatus("current")
_EntCLMAC_Type = OctetString
_EntCLMAC_Object = MibTableColumn
entCLMAC = _EntCLMAC_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 3),
    _EntCLMAC_Type()
)
entCLMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entCLMAC.setStatus("current")
_EntCLRx_Type = OctetString
_EntCLRx_Object = MibTableColumn
entCLRx = _EntCLRx_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 4),
    _EntCLRx_Type()
)
entCLRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entCLRx.setStatus("current")
_EntCLTx_Type = OctetString
_EntCLTx_Object = MibTableColumn
entCLTx = _EntCLTx_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 5),
    _EntCLTx_Type()
)
entCLTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entCLTx.setStatus("current")
_EntCLSignal_Type = Integer32
_EntCLSignal_Object = MibTableColumn
entCLSignal = _EntCLSignal_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 6),
    _EntCLSignal_Type()
)
entCLSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entCLSignal.setStatus("current")
_EntCLConnectedTime_Type = OctetString
_EntCLConnectedTime_Object = MibTableColumn
entCLConnectedTime = _EntCLConnectedTime_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 7),
    _EntCLConnectedTime_Type()
)
entCLConnectedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entCLConnectedTime.setStatus("current")
_EntCLIdleTime_Type = OctetString
_EntCLIdleTime_Object = MibTableColumn
entCLIdleTime = _EntCLIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 5, 6, 1, 8),
    _EntCLIdleTime_Type()
)
entCLIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entCLIdleTime.setStatus("current")
_EntSNMP_ObjectIdentity = ObjectIdentity
entSNMP = _EntSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6)
)
_EntSNMPStatus_Type = TruthValue
_EntSNMPStatus_Object = MibScalar
entSNMPStatus = _EntSNMPStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 1),
    _EntSNMPStatus_Type()
)
entSNMPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entSNMPStatus.setStatus("mandatory")


class _EntSNMPVerType_Type(Integer32):
    """Custom type entSNMPVerType based on Integer32"""
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
        *(("all", 0),
          ("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_EntSNMPVerType_Type.__name__ = "Integer32"
_EntSNMPVerType_Object = MibScalar
entSNMPVerType = _EntSNMPVerType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 2),
    _EntSNMPVerType_Type()
)
entSNMPVerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entSNMPVerType.setStatus("mandatory")
_EntSNMPCommunityTable_Object = MibTable
entSNMPCommunityTable = _EntSNMPCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 3)
)
if mibBuilder.loadTexts:
    entSNMPCommunityTable.setStatus("current")
_EntSNMPCommunityEntry_Object = MibTableRow
entSNMPCommunityEntry = _EntSNMPCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 3, 1)
)
entSNMPCommunityEntry.setIndexNames(
    (0, "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "entSNMPCommunityIndex"),
)
if mibBuilder.loadTexts:
    entSNMPCommunityEntry.setStatus("current")


class _EntSNMPCommunityIndex_Type(Integer32):
    """Custom type entSNMPCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EntSNMPCommunityIndex_Type.__name__ = "Integer32"
_EntSNMPCommunityIndex_Object = MibTableColumn
entSNMPCommunityIndex = _EntSNMPCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 3, 1, 1),
    _EntSNMPCommunityIndex_Type()
)
entSNMPCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSNMPCommunityIndex.setStatus("current")


class _EntSNMPCommunityName_Type(DisplayString):
    """Custom type entSNMPCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EntSNMPCommunityName_Type.__name__ = "DisplayString"
_EntSNMPCommunityName_Object = MibTableColumn
entSNMPCommunityName = _EntSNMPCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 3, 1, 2),
    _EntSNMPCommunityName_Type()
)
entSNMPCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entSNMPCommunityName.setStatus("current")


class _EntSNMPCommunityType_Type(Integer32):
    """Custom type entSNMPCommunityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("write", 2))
    )


_EntSNMPCommunityType_Type.__name__ = "Integer32"
_EntSNMPCommunityType_Object = MibTableColumn
entSNMPCommunityType = _EntSNMPCommunityType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 3, 1, 3),
    _EntSNMPCommunityType_Type()
)
entSNMPCommunityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSNMPCommunityType.setStatus("current")
_EntSNMPCommunityValid_Type = TruthValue
_EntSNMPCommunityValid_Object = MibTableColumn
entSNMPCommunityValid = _EntSNMPCommunityValid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 3, 1, 4),
    _EntSNMPCommunityValid_Type()
)
entSNMPCommunityValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSNMPCommunityValid.setStatus("current")
_EntSNMPTrap_ObjectIdentity = ObjectIdentity
entSNMPTrap = _EntSNMPTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 4)
)
_EntTrapStatus_Type = TruthValue
_EntTrapStatus_Object = MibScalar
entTrapStatus = _EntTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 4, 1),
    _EntTrapStatus_Type()
)
entTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entTrapStatus.setStatus("mandatory")


class _EntTrapVer_Type(Integer32):
    """Custom type entTrapVer based on Integer32"""
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
        *(("all", 0),
          ("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_EntTrapVer_Type.__name__ = "Integer32"
_EntTrapVer_Object = MibScalar
entTrapVer = _EntTrapVer_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 4, 2),
    _EntTrapVer_Type()
)
entTrapVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entTrapVer.setStatus("mandatory")
_EntTrapReceiverIPAddress_Type = IpAddress
_EntTrapReceiverIPAddress_Object = MibScalar
entTrapReceiverIPAddress = _EntTrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 4, 3),
    _EntTrapReceiverIPAddress_Type()
)
entTrapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entTrapReceiverIPAddress.setStatus("mandatory")
_EntTrapReceiverCommunityName_Type = DisplayString
_EntTrapReceiverCommunityName_Object = MibScalar
entTrapReceiverCommunityName = _EntTrapReceiverCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 100, 6, 4, 4),
    _EntTrapReceiverCommunityName_Type()
)
entTrapReceiverCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entTrapReceiverCommunityName.setStatus("mandatory")
_EntTraps_ObjectIdentity = ObjectIdentity
entTraps = _EntTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100, 20)
)
_EntSystemTraps_ObjectIdentity = ObjectIdentity
entSystemTraps = _EntSystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100, 20, 1)
)
_EntWanTraps_ObjectIdentity = ObjectIdentity
entWanTraps = _EntWanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 100, 20, 2)
)

# Managed Objects groups


# Notification objects

entSystemTrapsReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 100, 20, 1, 1)
)
if mibBuilder.loadTexts:
    entSystemTrapsReboot.setStatus(
        "current"
    )

entSystemTrapsRestoreToDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 100, 20, 1, 2)
)
if mibBuilder.loadTexts:
    entSystemTrapsRestoreToDefault.setStatus(
        "current"
    )

entSystemTrapsReloadModules = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 100, 20, 1, 3)
)
if mibBuilder.loadTexts:
    entSystemTrapsReloadModules.setStatus(
        "current"
    )

entWanTrapsLinkDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 100, 20, 2, 1)
)
entWanTrapsLinkDisconnect.setObjects(
    ("SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    entWanTrapsLinkDisconnect.setStatus(
        "current"
    )

entWanTrapsLinkRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 100, 20, 2, 2)
)
entWanTrapsLinkRecover.setObjects(
    ("SENAO-ENTERPRISE-INDOOR-AP-CB-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    entWanTrapsLinkRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SENAO-ENTERPRISE-INDOOR-AP-CB-MIB",
    **{"senao": senao,
       "indoorWirelessDevice": indoorWirelessDevice,
       "entSystem": entSystem,
       "entPassword": entPassword,
       "entSysModel": entSysModel,
       "entSysMode": entSysMode,
       "entSysUpTime": entSysUpTime,
       "entHwVersion": entHwVersion,
       "entSN": entSN,
       "entKenelVersion": entKenelVersion,
       "entAppVersion": entAppVersion,
       "entReset": entReset,
       "entResetToDefault": entResetToDefault,
       "entApplyModules": entApplyModules,
       "entLAN": entLAN,
       "entLANIP": entLANIP,
       "entLANSubnetMask": entLANSubnetMask,
       "entSTPEnable": entSTPEnable,
       "entDHCPEnable": entDHCPEnable,
       "entIPPoolStart": entIPPoolStart,
       "entIPPoolEnd": entIPPoolEnd,
       "entIPLeaseTime": entIPLeaseTime,
       "entWAN": entWAN,
       "entRouterEnable": entRouterEnable,
       "entMacFilter": entMacFilter,
       "entLanMacFilteringEnable": entLanMacFilteringEnable,
       "entLanMacFilteringMode": entLanMacFilteringMode,
       "entLanMacFilterTable": entLanMacFilterTable,
       "entLanMacFilterEntry": entLanMacFilterEntry,
       "entMacAddressIndex": entMacAddressIndex,
       "entMacAddress": entMacAddress,
       "entMacFilteringValid": entMacFilteringValid,
       "entWlan": entWlan,
       "entWlanCommonInfo": entWlanCommonInfo,
       "entOpMode": entOpMode,
       "entRadio": entRadio,
       "entAPMode": entAPMode,
       "entBand": entBand,
       "entESSIDNum": entESSIDNum,
       "entChannel": entChannel,
       "entDataRate": entDataRate,
       "entNDataRate": entNDataRate,
       "entTxPower": entTxPower,
       "entBeaconInterval": entBeaconInterval,
       "entDTIMPeriod": entDTIMPeriod,
       "entFragmentationThreshold": entFragmentationThreshold,
       "entRTSThreshold": entRTSThreshold,
       "entChannelBandwidth": entChannelBandwidth,
       "entPreambleType": entPreambleType,
       "entCTSProtection": entCTSProtection,
       "entWlanESSIDInfoTable": entWlanESSIDInfoTable,
       "entWlanESSIDInfoEntry": entWlanESSIDInfoEntry,
       "entWlanESSIDInfoIndex": entWlanESSIDInfoIndex,
       "entESSID": entESSID,
       "entBroadcastESSID": entBroadcastESSID,
       "entWMM": entWMM,
       "entEncryption": entEncryption,
       "entWlanAuthenticationType": entWlanAuthenticationType,
       "entWlanWepInfoTable": entWlanWepInfoTable,
       "entWlanWepInfoEntry": entWlanWepInfoEntry,
       "entWlanESSIDIndex": entWlanESSIDIndex,
       "entWlanWepKeyID": entWlanWepKeyID,
       "entWlanWepKey1Value": entWlanWepKey1Value,
       "entWlanWepKey2Value": entWlanWepKey2Value,
       "entWlanWepKey3Value": entWlanWepKey3Value,
       "entWlanWepKey4Value": entWlanWepKey4Value,
       "entWlanWPAInfoTable": entWlanWPAInfoTable,
       "entWlanWPAInfoEntry": entWlanWPAInfoEntry,
       "entWlanWPAESSIDIndex": entWlanWPAESSIDIndex,
       "entPresharedKey": entPresharedKey,
       "ent802dot1xInfoTable": ent802dot1xInfoTable,
       "ent802dot1xInfoEntry": ent802dot1xInfoEntry,
       "entWlan802dot1xESSIDIndex": entWlan802dot1xESSIDIndex,
       "entRADIUSServerIPAddress": entRADIUSServerIPAddress,
       "entRADIUSServerPort": entRADIUSServerPort,
       "entRADIUSServerPassword": entRADIUSServerPassword,
       "entWlan802dot1xEnable": entWlan802dot1xEnable,
       "entWlanClientListInfoTable": entWlanClientListInfoTable,
       "entWlanClientListInfoEntry": entWlanClientListInfoEntry,
       "entCLInfoIndex": entCLInfoIndex,
       "entCLInterface": entCLInterface,
       "entCLMAC": entCLMAC,
       "entCLRx": entCLRx,
       "entCLTx": entCLTx,
       "entCLSignal": entCLSignal,
       "entCLConnectedTime": entCLConnectedTime,
       "entCLIdleTime": entCLIdleTime,
       "entSNMP": entSNMP,
       "entSNMPStatus": entSNMPStatus,
       "entSNMPVerType": entSNMPVerType,
       "entSNMPCommunityTable": entSNMPCommunityTable,
       "entSNMPCommunityEntry": entSNMPCommunityEntry,
       "entSNMPCommunityIndex": entSNMPCommunityIndex,
       "entSNMPCommunityName": entSNMPCommunityName,
       "entSNMPCommunityType": entSNMPCommunityType,
       "entSNMPCommunityValid": entSNMPCommunityValid,
       "entSNMPTrap": entSNMPTrap,
       "entTrapStatus": entTrapStatus,
       "entTrapVer": entTrapVer,
       "entTrapReceiverIPAddress": entTrapReceiverIPAddress,
       "entTrapReceiverCommunityName": entTrapReceiverCommunityName,
       "entTraps": entTraps,
       "entSystemTraps": entSystemTraps,
       "entSystemTrapsReboot": entSystemTrapsReboot,
       "entSystemTrapsRestoreToDefault": entSystemTrapsRestoreToDefault,
       "entSystemTrapsReloadModules": entSystemTrapsReloadModules,
       "entWanTraps": entWanTraps,
       "entWanTrapsLinkDisconnect": entWanTrapsLinkDisconnect,
       "entWanTrapsLinkRecover": entWanTrapsLinkRecover}
)
