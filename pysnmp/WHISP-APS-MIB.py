# SNMP MIB module (WHISP-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WHISP-APS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:51 2024
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(whispBoxEsn,
 whispBoxRFPhysicalRadioEntry) = mibBuilder.importSymbols(
    "WHISP-BOX-MIBV2-MIB",
    "whispBoxEsn",
    "whispBoxRFPhysicalRadioEntry")

(whispAps,
 whispBox,
 whispModules) = mibBuilder.importSymbols(
    "WHISP-GLOBAL-REG-MIB",
    "whispAps",
    "whispBox",
    "whispModules")

(EventString,
 WhispLUID,
 WhispMACAddress) = mibBuilder.importSymbols(
    "WHISP-TCV2-MIB",
    "EventString",
    "WhispLUID",
    "WhispMACAddress")


# MODULE-IDENTITY

whispApsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WhispApsConfig_ObjectIdentity = ObjectIdentity
whispApsConfig = _WhispApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1)
)


class _GpsInput_Type(Integer32):
    """Custom type gpsInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generateSyncSignal", 0),
          ("syncToReceivedSignalPowerPort", 2),
          ("syncToReceivedSignalTimingPort", 1))
    )


_GpsInput_Type.__name__ = "Integer32"
_GpsInput_Object = MibScalar
gpsInput = _GpsInput_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 1),
    _GpsInput_Type()
)
gpsInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpsInput.setStatus("obsolete")


class _RfFreqCarrier_Type(Integer32):
    """Custom type rfFreqCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("wired", 0)
    )


_RfFreqCarrier_Type.__name__ = "Integer32"
_RfFreqCarrier_Object = MibScalar
rfFreqCarrier = _RfFreqCarrier_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 2),
    _RfFreqCarrier_Type()
)
rfFreqCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfFreqCarrier.setStatus("deprecated")
_ApLinkSpeed_Type = DisplayString
_ApLinkSpeed_Object = MibScalar
apLinkSpeed = _ApLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 3),
    _ApLinkSpeed_Type()
)
apLinkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLinkSpeed.setStatus("obsolete")


class _DwnLnkData_Type(Integer32):
    """Custom type dwnLnkData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_DwnLnkData_Type.__name__ = "Integer32"
_DwnLnkData_Object = MibScalar
dwnLnkData = _DwnLnkData_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 4),
    _DwnLnkData_Type()
)
dwnLnkData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwnLnkData.setStatus("deprecated")
if mibBuilder.loadTexts:
    dwnLnkData.setUnits("%")


class _HighPriorityUpLnkPct_Type(Integer32):
    """Custom type highPriorityUpLnkPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_HighPriorityUpLnkPct_Type.__name__ = "Integer32"
_HighPriorityUpLnkPct_Object = MibScalar
highPriorityUpLnkPct = _HighPriorityUpLnkPct_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 5),
    _HighPriorityUpLnkPct_Type()
)
highPriorityUpLnkPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highPriorityUpLnkPct.setStatus("obsolete")
if mibBuilder.loadTexts:
    highPriorityUpLnkPct.setUnits("%")
_NumUAckSlots_Type = Integer32
_NumUAckSlots_Object = MibScalar
numUAckSlots = _NumUAckSlots_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 6),
    _NumUAckSlots_Type()
)
numUAckSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numUAckSlots.setStatus("obsolete")
_UAcksReservHigh_Type = Integer32
_UAcksReservHigh_Object = MibScalar
uAcksReservHigh = _UAcksReservHigh_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 7),
    _UAcksReservHigh_Type()
)
uAcksReservHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uAcksReservHigh.setStatus("obsolete")
_NumDAckSlots_Type = Integer32
_NumDAckSlots_Object = MibScalar
numDAckSlots = _NumDAckSlots_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 8),
    _NumDAckSlots_Type()
)
numDAckSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numDAckSlots.setStatus("obsolete")
_DAcksReservHigh_Type = Integer32
_DAcksReservHigh_Object = MibScalar
dAcksReservHigh = _DAcksReservHigh_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 9),
    _DAcksReservHigh_Type()
)
dAcksReservHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dAcksReservHigh.setStatus("obsolete")
_NumCtlSlots_Type = Integer32
_NumCtlSlots_Object = MibScalar
numCtlSlots = _NumCtlSlots_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 10),
    _NumCtlSlots_Type()
)
numCtlSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numCtlSlots.setStatus("obsolete")
_NumCtlSlotsReserveHigh_Type = Integer32
_NumCtlSlotsReserveHigh_Object = MibScalar
numCtlSlotsReserveHigh = _NumCtlSlotsReserveHigh_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 11),
    _NumCtlSlotsReserveHigh_Type()
)
numCtlSlotsReserveHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numCtlSlotsReserveHigh.setStatus("obsolete")
_UpLnkDataRate_Type = Integer32
_UpLnkDataRate_Object = MibScalar
upLnkDataRate = _UpLnkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 12),
    _UpLnkDataRate_Type()
)
upLnkDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upLnkDataRate.setStatus("current")
if mibBuilder.loadTexts:
    upLnkDataRate.setUnits("Kilobits/sec")
_UpLnkLimit_Type = Integer32
_UpLnkLimit_Object = MibScalar
upLnkLimit = _UpLnkLimit_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 13),
    _UpLnkLimit_Type()
)
upLnkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upLnkLimit.setStatus("current")
if mibBuilder.loadTexts:
    upLnkLimit.setUnits("Kilobits/sec")
_DwnLnkDataRate_Type = Integer32
_DwnLnkDataRate_Object = MibScalar
dwnLnkDataRate = _DwnLnkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 14),
    _DwnLnkDataRate_Type()
)
dwnLnkDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwnLnkDataRate.setStatus("current")
if mibBuilder.loadTexts:
    dwnLnkDataRate.setUnits("Kilobits/sec")
_DwnLnkLimit_Type = Integer32
_DwnLnkLimit_Object = MibScalar
dwnLnkLimit = _DwnLnkLimit_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 15),
    _DwnLnkLimit_Type()
)
dwnLnkLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwnLnkLimit.setStatus("current")
if mibBuilder.loadTexts:
    dwnLnkLimit.setUnits("Kilobits/sec")


class _SectorID_Type(Integer32):
    """Custom type sectorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SectorID_Type.__name__ = "Integer32"
_SectorID_Object = MibScalar
sectorID = _SectorID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 16),
    _SectorID_Type()
)
sectorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sectorID.setStatus("current")
_MaxRange_Type = Integer32
_MaxRange_Object = MibScalar
maxRange = _MaxRange_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 17),
    _MaxRange_Type()
)
maxRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxRange.setStatus("deprecated")
if mibBuilder.loadTexts:
    maxRange.setUnits("miles")


class _AirLinkSecurity_Type(Integer32):
    """Custom type airLinkSecurity based on Integer32"""
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
        *(("authenticationIfAvailable", 3),
          ("desEnhanced", 1),
          ("desEnhancedAndAuthentication", 2),
          ("standard", 0))
    )


_AirLinkSecurity_Type.__name__ = "Integer32"
_AirLinkSecurity_Object = MibScalar
airLinkSecurity = _AirLinkSecurity_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 18),
    _AirLinkSecurity_Type()
)
airLinkSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    airLinkSecurity.setStatus("obsolete")


class _BerMode_Type(Integer32):
    """Custom type berMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("berStream", 0),
          ("noBerStream", 1))
    )


_BerMode_Type.__name__ = "Integer32"
_BerMode_Object = MibScalar
berMode = _BerMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 19),
    _BerMode_Type()
)
berMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berMode.setStatus("obsolete")
_AsIP1_Type = IpAddress
_AsIP1_Object = MibScalar
asIP1 = _AsIP1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 20),
    _AsIP1_Type()
)
asIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asIP1.setStatus("obsolete")
_AsIP2_Type = IpAddress
_AsIP2_Object = MibScalar
asIP2 = _AsIP2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 21),
    _AsIP2_Type()
)
asIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asIP2.setStatus("obsolete")
_AsIP3_Type = IpAddress
_AsIP3_Object = MibScalar
asIP3 = _AsIP3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 22),
    _AsIP3_Type()
)
asIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asIP3.setStatus("obsolete")
_LanIpAp_Type = IpAddress
_LanIpAp_Object = MibScalar
lanIpAp = _LanIpAp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 23),
    _LanIpAp_Type()
)
lanIpAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanIpAp.setStatus("current")
_LanMaskAp_Type = IpAddress
_LanMaskAp_Object = MibScalar
lanMaskAp = _LanMaskAp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 24),
    _LanMaskAp_Type()
)
lanMaskAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanMaskAp.setStatus("current")
_DefaultGwAp_Type = IpAddress
_DefaultGwAp_Object = MibScalar
defaultGwAp = _DefaultGwAp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 25),
    _DefaultGwAp_Type()
)
defaultGwAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGwAp.setStatus("current")
_PrivateIp_Type = IpAddress
_PrivateIp_Object = MibScalar
privateIp = _PrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 26),
    _PrivateIp_Type()
)
privateIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateIp.setStatus("current")


class _GpsTrap_Type(Integer32):
    """Custom type gpsTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gpsTrapDisabled", 0),
          ("gpsTrapEnabled", 1))
    )


_GpsTrap_Type.__name__ = "Integer32"
_GpsTrap_Object = MibScalar
gpsTrap = _GpsTrap_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 27),
    _GpsTrap_Type()
)
gpsTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpsTrap.setStatus("current")


class _RegTrap_Type(Integer32):
    """Custom type regTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("regTrapDisabled", 0),
          ("regTrapEnabled", 1))
    )


_RegTrap_Type.__name__ = "Integer32"
_RegTrap_Object = MibScalar
regTrap = _RegTrap_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 28),
    _RegTrap_Type()
)
regTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regTrap.setStatus("current")


class _TxSpreading_Type(Integer32):
    """Custom type txSpreading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("txSpreadingDisabled", 0),
          ("txSpreadingEnabled", 1))
    )


_TxSpreading_Type.__name__ = "Integer32"
_TxSpreading_Object = MibScalar
txSpreading = _TxSpreading_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 29),
    _TxSpreading_Type()
)
txSpreading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txSpreading.setStatus("current")


class _ApBeaconInfo_Type(Integer32):
    """Custom type apBeaconInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableApBeaconInfo", 1),
          ("enableApBeaconInfo", 0))
    )


_ApBeaconInfo_Type.__name__ = "Integer32"
_ApBeaconInfo_Object = MibScalar
apBeaconInfo = _ApBeaconInfo_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 30),
    _ApBeaconInfo_Type()
)
apBeaconInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBeaconInfo.setStatus("current")


class _AuthMode_Type(Integer32):
    """Custom type authMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("authenticationDisabled", 0),
          ("authenticationRequiredAAA", 4),
          ("authenticationRequiredAP", 3),
          ("authenticationRequiredBam", 1))
    )


_AuthMode_Type.__name__ = "Integer32"
_AuthMode_Object = MibScalar
authMode = _AuthMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 31),
    _AuthMode_Type()
)
authMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMode.setStatus("current")
_AuthKeyAp_Type = DisplayString
_AuthKeyAp_Object = MibScalar
authKeyAp = _AuthKeyAp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 32),
    _AuthKeyAp_Type()
)
authKeyAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authKeyAp.setStatus("current")


class _EncryptionMode_Type(Integer32):
    """Custom type encryptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("encryptionDisabled", 0),
          ("encryptionEnabled", 1))
    )


_EncryptionMode_Type.__name__ = "Integer32"
_EncryptionMode_Object = MibScalar
encryptionMode = _EncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 33),
    _EncryptionMode_Type()
)
encryptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryptionMode.setStatus("current")
_NtpServerIp_Type = IpAddress
_NtpServerIp_Object = MibScalar
ntpServerIp = _NtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 34),
    _NtpServerIp_Type()
)
ntpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerIp.setStatus("obsolete")
_BroadcastRetryCount_Type = Integer32
_BroadcastRetryCount_Object = MibScalar
broadcastRetryCount = _BroadcastRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 35),
    _BroadcastRetryCount_Type()
)
broadcastRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastRetryCount.setStatus("current")


class _EncryptDwBroadcast_Type(Integer32):
    """Custom type encryptDwBroadcast based on Integer32"""
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


_EncryptDwBroadcast_Type.__name__ = "Integer32"
_EncryptDwBroadcast_Object = MibScalar
encryptDwBroadcast = _EncryptDwBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 36),
    _EncryptDwBroadcast_Type()
)
encryptDwBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryptDwBroadcast.setStatus("current")
_UpdateAppAddress_Type = IpAddress
_UpdateAppAddress_Object = MibScalar
updateAppAddress = _UpdateAppAddress_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 37),
    _UpdateAppAddress_Type()
)
updateAppAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    updateAppAddress.setStatus("current")


class _DfsConfig_Type(Integer32):
    """Custom type dfsConfig based on Integer32"""
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


_DfsConfig_Type.__name__ = "Integer32"
_DfsConfig_Object = MibScalar
dfsConfig = _DfsConfig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 38),
    _DfsConfig_Type()
)
dfsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dfsConfig.setStatus("obsolete")


class _VlanEnable_Type(Integer32):
    """Custom type vlanEnable based on Integer32"""
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


_VlanEnable_Type.__name__ = "Integer32"
_VlanEnable_Object = MibScalar
vlanEnable = _VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 39),
    _VlanEnable_Type()
)
vlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanEnable.setStatus("current")


class _ConfigSource_Type(Integer32):
    """Custom type configSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bam", 0),
          ("bamsm", 2),
          ("sm", 1))
    )


_ConfigSource_Type.__name__ = "Integer32"
_ConfigSource_Object = MibScalar
configSource = _ConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 40),
    _ConfigSource_Type()
)
configSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSource.setStatus("current")


class _ApRateAdapt_Type(Integer32):
    """Custom type apRateAdapt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onex", 0),
          ("onextwox", 1),
          ("onextwoxthreex", 2))
    )


_ApRateAdapt_Type.__name__ = "Integer32"
_ApRateAdapt_Object = MibScalar
apRateAdapt = _ApRateAdapt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 41),
    _ApRateAdapt_Type()
)
apRateAdapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRateAdapt.setStatus("obsolete")
_NumCtlSlotsHW_Type = Integer32
_NumCtlSlotsHW_Object = MibScalar
numCtlSlotsHW = _NumCtlSlotsHW_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 42),
    _NumCtlSlotsHW_Type()
)
numCtlSlotsHW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numCtlSlotsHW.setStatus("deprecated")


class _DisplayAPEval_Type(Integer32):
    """Custom type displayAPEval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_DisplayAPEval_Type.__name__ = "Integer32"
_DisplayAPEval_Object = MibScalar
displayAPEval = _DisplayAPEval_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 43),
    _DisplayAPEval_Type()
)
displayAPEval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    displayAPEval.setStatus("current")


class _SmIsolation_Type(Integer32):
    """Custom type smIsolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("smIsolationDisable", 0),
          ("smIsolationDrop", 1),
          ("smIsolationFwd", 2))
    )


_SmIsolation_Type.__name__ = "Integer32"
_SmIsolation_Object = MibScalar
smIsolation = _SmIsolation_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 44),
    _SmIsolation_Type()
)
smIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smIsolation.setStatus("current")


class _IpAccessFilterEnable_Type(Integer32):
    """Custom type ipAccessFilterEnable based on Integer32"""
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


_IpAccessFilterEnable_Type.__name__ = "Integer32"
_IpAccessFilterEnable_Object = MibScalar
ipAccessFilterEnable = _IpAccessFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 45),
    _IpAccessFilterEnable_Type()
)
ipAccessFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessFilterEnable.setStatus("current")
_AllowedIPAccess1_Type = IpAddress
_AllowedIPAccess1_Object = MibScalar
allowedIPAccess1 = _AllowedIPAccess1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 46),
    _AllowedIPAccess1_Type()
)
allowedIPAccess1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccess1.setStatus("current")
_AllowedIPAccess2_Type = IpAddress
_AllowedIPAccess2_Object = MibScalar
allowedIPAccess2 = _AllowedIPAccess2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 47),
    _AllowedIPAccess2_Type()
)
allowedIPAccess2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccess2.setStatus("current")
_AllowedIPAccess3_Type = IpAddress
_AllowedIPAccess3_Object = MibScalar
allowedIPAccess3 = _AllowedIPAccess3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 48),
    _AllowedIPAccess3_Type()
)
allowedIPAccess3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccess3.setStatus("current")


class _TslBridging_Type(Integer32):
    """Custom type tslBridging based on Integer32"""
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


_TslBridging_Type.__name__ = "Integer32"
_TslBridging_Object = MibScalar
tslBridging = _TslBridging_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 49),
    _TslBridging_Type()
)
tslBridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tslBridging.setStatus("current")


class _UntranslatedArp_Type(Integer32):
    """Custom type untranslatedArp based on Integer32"""
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


_UntranslatedArp_Type.__name__ = "Integer32"
_UntranslatedArp_Object = MibScalar
untranslatedArp = _UntranslatedArp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 50),
    _UntranslatedArp_Type()
)
untranslatedArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    untranslatedArp.setStatus("current")


class _LimitFreqBand900_Type(Integer32):
    """Custom type limitFreqBand900 based on Integer32"""
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


_LimitFreqBand900_Type.__name__ = "Integer32"
_LimitFreqBand900_Object = MibScalar
limitFreqBand900 = _LimitFreqBand900_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 51),
    _LimitFreqBand900_Type()
)
limitFreqBand900.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    limitFreqBand900.setStatus("current")
_TxPwrLevel_Type = Integer32
_TxPwrLevel_Object = MibScalar
txPwrLevel = _TxPwrLevel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 52),
    _TxPwrLevel_Type()
)
txPwrLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txPwrLevel.setStatus("obsolete")


class _RfFreqCaralt1_Type(Integer32):
    """Custom type rfFreqCaralt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_RfFreqCaralt1_Type.__name__ = "Integer32"
_RfFreqCaralt1_Object = MibScalar
rfFreqCaralt1 = _RfFreqCaralt1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 53),
    _RfFreqCaralt1_Type()
)
rfFreqCaralt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfFreqCaralt1.setStatus("current")


class _RfFreqCaralt2_Type(Integer32):
    """Custom type rfFreqCaralt2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_RfFreqCaralt2_Type.__name__ = "Integer32"
_RfFreqCaralt2_Object = MibScalar
rfFreqCaralt2 = _RfFreqCaralt2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 54),
    _RfFreqCaralt2_Type()
)
rfFreqCaralt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfFreqCaralt2.setStatus("current")


class _ScheduleWhitening_Type(Integer32):
    """Custom type scheduleWhitening based on Integer32"""
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


_ScheduleWhitening_Type.__name__ = "Integer32"
_ScheduleWhitening_Object = MibScalar
scheduleWhitening = _ScheduleWhitening_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 55),
    _ScheduleWhitening_Type()
)
scheduleWhitening.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleWhitening.setStatus("current")


class _RemoteSpectrumAnalysisDuration_Type(Integer32):
    """Custom type remoteSpectrumAnalysisDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_RemoteSpectrumAnalysisDuration_Type.__name__ = "Integer32"
_RemoteSpectrumAnalysisDuration_Object = MibScalar
remoteSpectrumAnalysisDuration = _RemoteSpectrumAnalysisDuration_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 56),
    _RemoteSpectrumAnalysisDuration_Type()
)
remoteSpectrumAnalysisDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSpectrumAnalysisDuration.setStatus("current")


class _RemoteSpectrumAnalyzerLUID_Type(Integer32):
    """Custom type remoteSpectrumAnalyzerLUID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RemoteSpectrumAnalyzerLUID_Type.__name__ = "Integer32"
_RemoteSpectrumAnalyzerLUID_Object = MibScalar
remoteSpectrumAnalyzerLUID = _RemoteSpectrumAnalyzerLUID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 57),
    _RemoteSpectrumAnalyzerLUID_Type()
)
remoteSpectrumAnalyzerLUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSpectrumAnalyzerLUID.setStatus("current")


class _BhReReg_Type(Integer32):
    """Custom type bhReReg based on Integer32"""
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


_BhReReg_Type.__name__ = "Integer32"
_BhReReg_Object = MibScalar
bhReReg = _BhReReg_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 58),
    _BhReReg_Type()
)
bhReReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bhReReg.setStatus("current")
_DlnkBcastCIR_Type = Integer32
_DlnkBcastCIR_Object = MibScalar
dlnkBcastCIR = _DlnkBcastCIR_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 59),
    _DlnkBcastCIR_Type()
)
dlnkBcastCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlnkBcastCIR.setStatus("current")


class _VerifyGPSChecksum_Type(Integer32):
    """Custom type verifyGPSChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNotVerifyGPSMessageChecksum", 0),
          ("verifyGPSMessageChecksum", 1))
    )


_VerifyGPSChecksum_Type.__name__ = "Integer32"
_VerifyGPSChecksum_Object = MibScalar
verifyGPSChecksum = _VerifyGPSChecksum_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 60),
    _VerifyGPSChecksum_Type()
)
verifyGPSChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    verifyGPSChecksum.setStatus("current")


class _ApVlanOverride_Type(Integer32):
    """Custom type apVlanOverride based on Integer32"""
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


_ApVlanOverride_Type.__name__ = "Integer32"
_ApVlanOverride_Object = MibScalar
apVlanOverride = _ApVlanOverride_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 61),
    _ApVlanOverride_Type()
)
apVlanOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVlanOverride.setStatus("current")


class _DhcpRelayAgentEnable_Type(Integer32):
    """Custom type dhcpRelayAgentEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("fullRelay", 1),
          ("option82Only", 2))
    )


_DhcpRelayAgentEnable_Type.__name__ = "Integer32"
_DhcpRelayAgentEnable_Object = MibScalar
dhcpRelayAgentEnable = _DhcpRelayAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 62),
    _DhcpRelayAgentEnable_Type()
)
dhcpRelayAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayAgentEnable.setStatus("current")
_DhcpRelayAgentSrvrIP_Type = IpAddress
_DhcpRelayAgentSrvrIP_Object = MibScalar
dhcpRelayAgentSrvrIP = _DhcpRelayAgentSrvrIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 63),
    _DhcpRelayAgentSrvrIP_Type()
)
dhcpRelayAgentSrvrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayAgentSrvrIP.setStatus("obsolete")


class _ColorCodeRescanTimer_Type(Integer32):
    """Custom type colorCodeRescanTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_ColorCodeRescanTimer_Type.__name__ = "Integer32"
_ColorCodeRescanTimer_Object = MibScalar
colorCodeRescanTimer = _ColorCodeRescanTimer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 64),
    _ColorCodeRescanTimer_Type()
)
colorCodeRescanTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCodeRescanTimer.setStatus("current")


class _ColorCodeRescanIdleTimer_Type(Integer32):
    """Custom type colorCodeRescanIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ColorCodeRescanIdleTimer_Type.__name__ = "Integer32"
_ColorCodeRescanIdleTimer_Object = MibScalar
colorCodeRescanIdleTimer = _ColorCodeRescanIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 65),
    _ColorCodeRescanIdleTimer_Type()
)
colorCodeRescanIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colorCodeRescanIdleTimer.setStatus("current")


class _AuthKeyOptionAP_Type(Integer32):
    """Custom type authKeyOptionAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useDefault", 0),
          ("useKeySet", 1))
    )


_AuthKeyOptionAP_Type.__name__ = "Integer32"
_AuthKeyOptionAP_Object = MibScalar
authKeyOptionAP = _AuthKeyOptionAP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 66),
    _AuthKeyOptionAP_Type()
)
authKeyOptionAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authKeyOptionAP.setStatus("current")
_AsIP4_Type = IpAddress
_AsIP4_Object = MibScalar
asIP4 = _AsIP4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 67),
    _AsIP4_Type()
)
asIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asIP4.setStatus("obsolete")
_AsIP5_Type = IpAddress
_AsIP5_Object = MibScalar
asIP5 = _AsIP5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 68),
    _AsIP5_Type()
)
asIP5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asIP5.setStatus("obsolete")


class _OnlyAllowVer95OrAbove_Type(Integer32):
    """Custom type onlyAllowVer95OrAbove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("onlyAllowVer95OrAboveDisabled", 0),
          ("onlyAllowVer95OrAboveEnabled", 1))
    )


_OnlyAllowVer95OrAbove_Type.__name__ = "Integer32"
_OnlyAllowVer95OrAbove_Object = MibScalar
onlyAllowVer95OrAbove = _OnlyAllowVer95OrAbove_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 69),
    _OnlyAllowVer95OrAbove_Type()
)
onlyAllowVer95OrAbove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onlyAllowVer95OrAbove.setStatus("current")
_ApRxDelay_Type = Integer32
_ApRxDelay_Object = MibScalar
apRxDelay = _ApRxDelay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 70),
    _ApRxDelay_Type()
)
apRxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRxDelay.setStatus("current")


class _QinqEthType_Type(Integer32):
    """Custom type qinqEthType based on Integer32"""
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
        *(("x8100", 1),
          ("x88a8", 0),
          ("x9100", 2),
          ("x9200", 3),
          ("x9300", 4))
    )


_QinqEthType_Type.__name__ = "Integer32"
_QinqEthType_Object = MibScalar
qinqEthType = _QinqEthType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 71),
    _QinqEthType_Type()
)
qinqEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qinqEthType.setStatus("current")


class _FskSMTxPwrCntl_Type(Integer32):
    """Custom type fskSMTxPwrCntl based on Integer32"""
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


_FskSMTxPwrCntl_Type.__name__ = "Integer32"
_FskSMTxPwrCntl_Object = MibScalar
fskSMTxPwrCntl = _FskSMTxPwrCntl_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 72),
    _FskSMTxPwrCntl_Type()
)
fskSMTxPwrCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fskSMTxPwrCntl.setStatus("current")


class _FskSMRcvTargetLvl_Type(Integer32):
    """Custom type fskSMRcvTargetLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, -40),
    )


_FskSMRcvTargetLvl_Type.__name__ = "Integer32"
_FskSMRcvTargetLvl_Object = MibScalar
fskSMRcvTargetLvl = _FskSMRcvTargetLvl_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 73),
    _FskSMRcvTargetLvl_Type()
)
fskSMRcvTargetLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fskSMRcvTargetLvl.setStatus("current")
if mibBuilder.loadTexts:
    fskSMRcvTargetLvl.setUnits("dBm")
_AuthSharedSecret1_Type = DisplayString
_AuthSharedSecret1_Object = MibScalar
authSharedSecret1 = _AuthSharedSecret1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 74),
    _AuthSharedSecret1_Type()
)
authSharedSecret1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSharedSecret1.setStatus("current")
_AuthSharedSecret2_Type = DisplayString
_AuthSharedSecret2_Object = MibScalar
authSharedSecret2 = _AuthSharedSecret2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 75),
    _AuthSharedSecret2_Type()
)
authSharedSecret2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSharedSecret2.setStatus("current")
_AuthSharedSecret3_Type = DisplayString
_AuthSharedSecret3_Object = MibScalar
authSharedSecret3 = _AuthSharedSecret3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 76),
    _AuthSharedSecret3_Type()
)
authSharedSecret3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authSharedSecret3.setStatus("current")
_WhispUsrAuthSharedSecret1_Type = DisplayString
_WhispUsrAuthSharedSecret1_Object = MibScalar
whispUsrAuthSharedSecret1 = _WhispUsrAuthSharedSecret1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 79),
    _WhispUsrAuthSharedSecret1_Type()
)
whispUsrAuthSharedSecret1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    whispUsrAuthSharedSecret1.setStatus("obsolete")
_WhispUsrAuthSharedSecret2_Type = DisplayString
_WhispUsrAuthSharedSecret2_Object = MibScalar
whispUsrAuthSharedSecret2 = _WhispUsrAuthSharedSecret2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 80),
    _WhispUsrAuthSharedSecret2_Type()
)
whispUsrAuthSharedSecret2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    whispUsrAuthSharedSecret2.setStatus("obsolete")
_WhispUsrAuthSharedSecret3_Type = DisplayString
_WhispUsrAuthSharedSecret3_Object = MibScalar
whispUsrAuthSharedSecret3 = _WhispUsrAuthSharedSecret3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 81),
    _WhispUsrAuthSharedSecret3_Type()
)
whispUsrAuthSharedSecret3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    whispUsrAuthSharedSecret3.setStatus("obsolete")
_WhispUsrAcctSvr1_Type = DisplayString
_WhispUsrAcctSvr1_Object = MibScalar
whispUsrAcctSvr1 = _WhispUsrAcctSvr1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 82),
    _WhispUsrAcctSvr1_Type()
)
whispUsrAcctSvr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    whispUsrAcctSvr1.setStatus("obsolete")
_WhispUsrAcctSvr2_Type = DisplayString
_WhispUsrAcctSvr2_Object = MibScalar
whispUsrAcctSvr2 = _WhispUsrAcctSvr2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 83),
    _WhispUsrAcctSvr2_Type()
)
whispUsrAcctSvr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    whispUsrAcctSvr2.setStatus("obsolete")
_WhispUsrAcctSvr3_Type = DisplayString
_WhispUsrAcctSvr3_Object = MibScalar
whispUsrAcctSvr3 = _WhispUsrAcctSvr3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 84),
    _WhispUsrAcctSvr3_Type()
)
whispUsrAcctSvr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    whispUsrAcctSvr3.setStatus("obsolete")


class _WhispUsrAuthPhase1_Type(Integer32):
    """Custom type whispUsrAuthPhase1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("md5", 0)
    )


_WhispUsrAuthPhase1_Type.__name__ = "Integer32"
_WhispUsrAuthPhase1_Object = MibScalar
whispUsrAuthPhase1 = _WhispUsrAuthPhase1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 85),
    _WhispUsrAuthPhase1_Type()
)
whispUsrAuthPhase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    whispUsrAuthPhase1.setStatus("current")


class _WhispWebUseAuthServer_Type(Integer32):
    """Custom type whispWebUseAuthServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useRADIUSAccountingSvr", 0),
          ("useRADIUSAuthenticationSvr", 1))
    )


_WhispWebUseAuthServer_Type.__name__ = "Integer32"
_WhispWebUseAuthServer_Object = MibScalar
whispWebUseAuthServer = _WhispWebUseAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 86),
    _WhispWebUseAuthServer_Type()
)
whispWebUseAuthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    whispWebUseAuthServer.setStatus("obsolete")
_DropSession_Type = MacAddress
_DropSession_Object = MibScalar
dropSession = _DropSession_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 87),
    _DropSession_Type()
)
dropSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dropSession.setStatus("current")


class _UGPSPower_Type(Integer32):
    """Custom type uGPSPower based on Integer32"""
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


_UGPSPower_Type.__name__ = "Integer32"
_UGPSPower_Object = MibScalar
uGPSPower = _UGPSPower_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 88),
    _UGPSPower_Type()
)
uGPSPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uGPSPower.setStatus("current")


class _TimeZone_Type(Integer32):
    """Custom type timeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 124),
    )


_TimeZone_Type.__name__ = "Integer32"
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 89),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")


class _OfdmSMRcvTargetLvl_Type(Integer32):
    """Custom type ofdmSMRcvTargetLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, -40),
    )


_OfdmSMRcvTargetLvl_Type.__name__ = "Integer32"
_OfdmSMRcvTargetLvl_Object = MibScalar
ofdmSMRcvTargetLvl = _OfdmSMRcvTargetLvl_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 90),
    _OfdmSMRcvTargetLvl_Type()
)
ofdmSMRcvTargetLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofdmSMRcvTargetLvl.setStatus("current")
if mibBuilder.loadTexts:
    ofdmSMRcvTargetLvl.setUnits("dBm")
_RadiusPort_Type = Integer32
_RadiusPort_Object = MibScalar
radiusPort = _RadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 91),
    _RadiusPort_Type()
)
radiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPort.setStatus("current")
_RadiusAcctPort_Type = Integer32
_RadiusAcctPort_Object = MibScalar
radiusAcctPort = _RadiusAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 92),
    _RadiusAcctPort_Type()
)
radiusAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctPort.setStatus("current")
_LastSesStatsReset_Type = DisplayString
_LastSesStatsReset_Object = MibScalar
lastSesStatsReset = _LastSesStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 93),
    _LastSesStatsReset_Type()
)
lastSesStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSesStatsReset.setStatus("current")


class _ResetSesStats_Type(Integer32):
    """Custom type resetSesStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 0),
          ("reset", 1))
    )


_ResetSesStats_Type.__name__ = "Integer32"
_ResetSesStats_Object = MibScalar
resetSesStats = _ResetSesStats_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 94),
    _ResetSesStats_Type()
)
resetSesStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetSesStats.setStatus("current")


class _RfOLTrap_Type(Integer32):
    """Custom type rfOLTrap based on Integer32"""
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


_RfOLTrap_Type.__name__ = "Integer32"
_RfOLTrap_Object = MibScalar
rfOLTrap = _RfOLTrap_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 95),
    _RfOLTrap_Type()
)
rfOLTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfOLTrap.setStatus("current")


class _RfOLThreshold_Type(Integer32):
    """Custom type rfOLThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RfOLThreshold_Type.__name__ = "Integer32"
_RfOLThreshold_Object = MibScalar
rfOLThreshold = _RfOLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 96),
    _RfOLThreshold_Type()
)
rfOLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfOLThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rfOLThreshold.setUnits("%")


class _RfOLEnable_Type(Integer32):
    """Custom type rfOLEnable based on Integer32"""
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


_RfOLEnable_Type.__name__ = "Integer32"
_RfOLEnable_Object = MibScalar
rfOLEnable = _RfOLEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 97),
    _RfOLEnable_Type()
)
rfOLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfOLEnable.setStatus("current")
_ActionListFilename_Type = DisplayString
_ActionListFilename_Object = MibScalar
actionListFilename = _ActionListFilename_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 98),
    _ActionListFilename_Type()
)
actionListFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionListFilename.setStatus("current")


class _EnableAutoupdate_Type(Integer32):
    """Custom type enableAutoupdate based on Integer32"""
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


_EnableAutoupdate_Type.__name__ = "Integer32"
_EnableAutoupdate_Object = MibScalar
enableAutoupdate = _EnableAutoupdate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 99),
    _EnableAutoupdate_Type()
)
enableAutoupdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAutoupdate.setStatus("current")
_AccountingSmReAuthInterval_Type = Integer32
_AccountingSmReAuthInterval_Object = MibScalar
accountingSmReAuthInterval = _AccountingSmReAuthInterval_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 100),
    _AccountingSmReAuthInterval_Type()
)
accountingSmReAuthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingSmReAuthInterval.setStatus("current")


class _SyslogDomainNameAppend_Type(Integer32):
    """Custom type syslogDomainNameAppend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("appendDomain", 1),
          ("disableDomain", 0))
    )


_SyslogDomainNameAppend_Type.__name__ = "Integer32"
_SyslogDomainNameAppend_Object = MibScalar
syslogDomainNameAppend = _SyslogDomainNameAppend_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 101),
    _SyslogDomainNameAppend_Type()
)
syslogDomainNameAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogDomainNameAppend.setStatus("deprecated")
_SyslogServerAddr_Type = DisplayString
_SyslogServerAddr_Object = MibScalar
syslogServerAddr = _SyslogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 102),
    _SyslogServerAddr_Type()
)
syslogServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerAddr.setStatus("deprecated")
_SyslogServerPort_Type = Integer32
_SyslogServerPort_Object = MibScalar
syslogServerPort = _SyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 103),
    _SyslogServerPort_Type()
)
syslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerPort.setStatus("current")


class _SyslogXmitAP_Type(Integer32):
    """Custom type syslogXmitAP based on Integer32"""
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


_SyslogXmitAP_Type.__name__ = "Integer32"
_SyslogXmitAP_Object = MibScalar
syslogXmitAP = _SyslogXmitAP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 104),
    _SyslogXmitAP_Type()
)
syslogXmitAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogXmitAP.setStatus("current")


class _SyslogXmitSMs_Type(Integer32):
    """Custom type syslogXmitSMs based on Integer32"""
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


_SyslogXmitSMs_Type.__name__ = "Integer32"
_SyslogXmitSMs_Object = MibScalar
syslogXmitSMs = _SyslogXmitSMs_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 105),
    _SyslogXmitSMs_Type()
)
syslogXmitSMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogXmitSMs.setStatus("current")
_AccountingInterimUpdateInterval_Type = Integer32
_AccountingInterimUpdateInterval_Object = MibScalar
accountingInterimUpdateInterval = _AccountingInterimUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 106),
    _AccountingInterimUpdateInterval_Type()
)
accountingInterimUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingInterimUpdateInterval.setStatus("current")


class _GpsOutputEn_Type(Integer32):
    """Custom type gpsOutputEn based on Integer32"""
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


_GpsOutputEn_Type.__name__ = "Integer32"
_GpsOutputEn_Object = MibScalar
gpsOutputEn = _GpsOutputEn_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 107),
    _GpsOutputEn_Type()
)
gpsOutputEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpsOutputEn.setStatus("current")


class _RadioMode_Type(Integer32):
    """Custom type radioMode based on Integer32"""
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
        *(("combo", 0),
          ("comboDualChan", 1),
          ("fskOnly", 3),
          ("mimoOnly", 2))
    )


_RadioMode_Type.__name__ = "Integer32"
_RadioMode_Object = MibScalar
radioMode = _RadioMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 206),
    _RadioMode_Type()
)
radioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioMode.setStatus("obsolete")


class _RfTelnetAccess_Type(Integer32):
    """Custom type rfTelnetAccess based on Integer32"""
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


_RfTelnetAccess_Type.__name__ = "Integer32"
_RfTelnetAccess_Object = MibScalar
rfTelnetAccess = _RfTelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 207),
    _RfTelnetAccess_Type()
)
rfTelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfTelnetAccess.setStatus("current")
_UpLnkMaxBurstDataRate_Type = Integer32
_UpLnkMaxBurstDataRate_Object = MibScalar
upLnkMaxBurstDataRate = _UpLnkMaxBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 208),
    _UpLnkMaxBurstDataRate_Type()
)
upLnkMaxBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upLnkMaxBurstDataRate.setStatus("current")
if mibBuilder.loadTexts:
    upLnkMaxBurstDataRate.setUnits("Kilobits/sec")
_DwnLnkMaxBurstDataRate_Type = Integer32
_DwnLnkMaxBurstDataRate_Object = MibScalar
dwnLnkMaxBurstDataRate = _DwnLnkMaxBurstDataRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 209),
    _DwnLnkMaxBurstDataRate_Type()
)
dwnLnkMaxBurstDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwnLnkMaxBurstDataRate.setStatus("current")
if mibBuilder.loadTexts:
    dwnLnkMaxBurstDataRate.setUnits("Kilobits/sec")


class _RfPPPoEPADIForwarding_Type(Integer32):
    """Custom type rfPPPoEPADIForwarding based on Integer32"""
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


_RfPPPoEPADIForwarding_Type.__name__ = "Integer32"
_RfPPPoEPADIForwarding_Object = MibScalar
rfPPPoEPADIForwarding = _RfPPPoEPADIForwarding_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 210),
    _RfPPPoEPADIForwarding_Type()
)
rfPPPoEPADIForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfPPPoEPADIForwarding.setStatus("current")


class _AllowedIPAccessNMLength1_Type(Integer32):
    """Custom type allowedIPAccessNMLength1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AllowedIPAccessNMLength1_Type.__name__ = "Integer32"
_AllowedIPAccessNMLength1_Object = MibScalar
allowedIPAccessNMLength1 = _AllowedIPAccessNMLength1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 211),
    _AllowedIPAccessNMLength1_Type()
)
allowedIPAccessNMLength1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccessNMLength1.setStatus("current")


class _AllowedIPAccessNMLength2_Type(Integer32):
    """Custom type allowedIPAccessNMLength2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AllowedIPAccessNMLength2_Type.__name__ = "Integer32"
_AllowedIPAccessNMLength2_Object = MibScalar
allowedIPAccessNMLength2 = _AllowedIPAccessNMLength2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 212),
    _AllowedIPAccessNMLength2_Type()
)
allowedIPAccessNMLength2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccessNMLength2.setStatus("current")


class _AllowedIPAccessNMLength3_Type(Integer32):
    """Custom type allowedIPAccessNMLength3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AllowedIPAccessNMLength3_Type.__name__ = "Integer32"
_AllowedIPAccessNMLength3_Object = MibScalar
allowedIPAccessNMLength3 = _AllowedIPAccessNMLength3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 213),
    _AllowedIPAccessNMLength3_Type()
)
allowedIPAccessNMLength3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccessNMLength3.setStatus("current")


class _BridgeFloodUnknownsEnable_Type(Integer32):
    """Custom type bridgeFloodUnknownsEnable based on Integer32"""
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


_BridgeFloodUnknownsEnable_Type.__name__ = "Integer32"
_BridgeFloodUnknownsEnable_Object = MibScalar
bridgeFloodUnknownsEnable = _BridgeFloodUnknownsEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 214),
    _BridgeFloodUnknownsEnable_Type()
)
bridgeFloodUnknownsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeFloodUnknownsEnable.setStatus("current")


class _BerModSelect_Type(Integer32):
    """Custom type berModSelect based on Integer32"""
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
        *(("qam-16", 1),
          ("qam-256", 3),
          ("qam-64", 2),
          ("qpsk", 0))
    )


_BerModSelect_Type.__name__ = "Integer32"
_BerModSelect_Object = MibScalar
berModSelect = _BerModSelect_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 215),
    _BerModSelect_Type()
)
berModSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    berModSelect.setStatus("current")


class _RemoteSpectrumAnalyzerScanBandwidth_Type(Integer32):
    """Custom type remoteSpectrumAnalyzerScanBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth10MHz", 1),
          ("bandwidth20MHz", 2),
          ("bandwidth5MHz", 0))
    )


_RemoteSpectrumAnalyzerScanBandwidth_Type.__name__ = "Integer32"
_RemoteSpectrumAnalyzerScanBandwidth_Object = MibScalar
remoteSpectrumAnalyzerScanBandwidth = _RemoteSpectrumAnalyzerScanBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 216),
    _RemoteSpectrumAnalyzerScanBandwidth_Type()
)
remoteSpectrumAnalyzerScanBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSpectrumAnalyzerScanBandwidth.setStatus("current")


class _MulticastVCDataRate_Type(Integer32):
    """Custom type multicastVCDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate1X", 4),
          ("rate2X", 5),
          ("rate4X", 7),
          ("rate6X", 8),
          ("rate8X", 9))
    )


_MulticastVCDataRate_Type.__name__ = "Integer32"
_MulticastVCDataRate_Object = MibScalar
multicastVCDataRate = _MulticastVCDataRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 217),
    _MulticastVCDataRate_Type()
)
multicastVCDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastVCDataRate.setStatus("current")
_DlnkMcastCIR_Type = Integer32
_DlnkMcastCIR_Object = MibScalar
dlnkMcastCIR = _DlnkMcastCIR_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 218),
    _DlnkMcastCIR_Type()
)
dlnkMcastCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlnkMcastCIR.setStatus("current")
_MulticastRetryCount_Type = Integer32
_MulticastRetryCount_Object = MibScalar
multicastRetryCount = _MulticastRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 219),
    _MulticastRetryCount_Type()
)
multicastRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastRetryCount.setStatus("current")


class _ApConfigAdjacentChanSupport_Type(Integer32):
    """Custom type apConfigAdjacentChanSupport based on Integer32"""
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


_ApConfigAdjacentChanSupport_Type.__name__ = "Integer32"
_ApConfigAdjacentChanSupport_Object = MibScalar
apConfigAdjacentChanSupport = _ApConfigAdjacentChanSupport_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 1, 220),
    _ApConfigAdjacentChanSupport_Type()
)
apConfigAdjacentChanSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apConfigAdjacentChanSupport.setStatus("current")
_WhispApsLink_ObjectIdentity = ObjectIdentity
whispApsLink = _WhispApsLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2)
)
_WhispApsLinkTestConfig_ObjectIdentity = ObjectIdentity
whispApsLinkTestConfig = _WhispApsLinkTestConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 1)
)
_LinkTestLUID_Type = Integer32
_LinkTestLUID_Object = MibScalar
linkTestLUID = _LinkTestLUID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 1, 1),
    _LinkTestLUID_Type()
)
linkTestLUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestLUID.setStatus("current")
_LinkTestDuration_Type = Integer32
_LinkTestDuration_Object = MibScalar
linkTestDuration = _LinkTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 1, 2),
    _LinkTestDuration_Type()
)
linkTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestDuration.setStatus("current")


class _LinkTestAction_Type(Integer32):
    """Custom type linkTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stopped", 0))
    )


_LinkTestAction_Type.__name__ = "Integer32"
_LinkTestAction_Object = MibScalar
linkTestAction = _LinkTestAction_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 1, 3),
    _LinkTestAction_Type()
)
linkTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestAction.setStatus("current")
_LinkTestPktLength_Type = Integer32
_LinkTestPktLength_Object = MibScalar
linkTestPktLength = _LinkTestPktLength_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 1, 4),
    _LinkTestPktLength_Type()
)
linkTestPktLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestPktLength.setStatus("current")


class _LinkTestMode_Type(Integer32):
    """Custom type linkTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linktestwithbridging", 1),
          ("linktestwithbridgingandmir", 2),
          ("rflinktest", 0))
    )


_LinkTestMode_Type.__name__ = "Integer32"
_LinkTestMode_Object = MibScalar
linkTestMode = _LinkTestMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 1, 5),
    _LinkTestMode_Type()
)
linkTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestMode.setStatus("current")


class _LinkTestSNRCalculation_Type(Integer32):
    """Custom type linkTestSNRCalculation based on Integer32"""
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


_LinkTestSNRCalculation_Type.__name__ = "Integer32"
_LinkTestSNRCalculation_Object = MibScalar
linkTestSNRCalculation = _LinkTestSNRCalculation_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 1, 6),
    _LinkTestSNRCalculation_Type()
)
linkTestSNRCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestSNRCalculation.setStatus("current")


class _LinkTestWithDualPath_Type(Integer32):
    """Custom type linkTestWithDualPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("highandlowpriorityvcs", 1),
          ("lowpriorityvconly", 0))
    )


_LinkTestWithDualPath_Type.__name__ = "Integer32"
_LinkTestWithDualPath_Object = MibScalar
linkTestWithDualPath = _LinkTestWithDualPath_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 1, 7),
    _LinkTestWithDualPath_Type()
)
linkTestWithDualPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestWithDualPath.setStatus("current")
_LinkTestNumPkt_Type = Integer32
_LinkTestNumPkt_Object = MibScalar
linkTestNumPkt = _LinkTestNumPkt_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 1, 8),
    _LinkTestNumPkt_Type()
)
linkTestNumPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestNumPkt.setStatus("current")
_WhispApsLinkTestResult_ObjectIdentity = ObjectIdentity
whispApsLinkTestResult = _WhispApsLinkTestResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2)
)
_TestLUID_Type = Integer32
_TestLUID_Object = MibScalar
testLUID = _TestLUID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 1),
    _TestLUID_Type()
)
testLUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testLUID.setStatus("current")
_LinkTestStatus_Type = DisplayString
_LinkTestStatus_Object = MibScalar
linkTestStatus = _LinkTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 2),
    _LinkTestStatus_Type()
)
linkTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTestStatus.setStatus("current")
_LinkTestError_Type = DisplayString
_LinkTestError_Object = MibScalar
linkTestError = _LinkTestError_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 3),
    _LinkTestError_Type()
)
linkTestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTestError.setStatus("current")
_TestDuration_Type = Integer32
_TestDuration_Object = MibScalar
testDuration = _TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 4),
    _TestDuration_Type()
)
testDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testDuration.setStatus("current")
_DownLinkRate_Type = Integer32
_DownLinkRate_Object = MibScalar
downLinkRate = _DownLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 5),
    _DownLinkRate_Type()
)
downLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downLinkRate.setStatus("current")
if mibBuilder.loadTexts:
    downLinkRate.setUnits("bps")
_UpLinkRate_Type = Integer32
_UpLinkRate_Object = MibScalar
upLinkRate = _UpLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 6),
    _UpLinkRate_Type()
)
upLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upLinkRate.setStatus("current")
if mibBuilder.loadTexts:
    upLinkRate.setUnits("bps")
_DownLinkEff_Type = Integer32
_DownLinkEff_Object = MibScalar
downLinkEff = _DownLinkEff_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 7),
    _DownLinkEff_Type()
)
downLinkEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downLinkEff.setStatus("current")
if mibBuilder.loadTexts:
    downLinkEff.setUnits("%")
_MaxDwnLinkIndex_Type = Integer32
_MaxDwnLinkIndex_Object = MibScalar
maxDwnLinkIndex = _MaxDwnLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 8),
    _MaxDwnLinkIndex_Type()
)
maxDwnLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxDwnLinkIndex.setStatus("current")
_ActDwnLinkIndex_Type = Integer32
_ActDwnLinkIndex_Object = MibScalar
actDwnLinkIndex = _ActDwnLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 9),
    _ActDwnLinkIndex_Type()
)
actDwnLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actDwnLinkIndex.setStatus("current")
_ExpDwnFragCount_Type = Gauge32
_ExpDwnFragCount_Object = MibScalar
expDwnFragCount = _ExpDwnFragCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 10),
    _ExpDwnFragCount_Type()
)
expDwnFragCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expDwnFragCount.setStatus("current")
_ActDwnFragCount_Type = Gauge32
_ActDwnFragCount_Object = MibScalar
actDwnFragCount = _ActDwnFragCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 11),
    _ActDwnFragCount_Type()
)
actDwnFragCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actDwnFragCount.setStatus("current")
_UpLinkEff_Type = Integer32
_UpLinkEff_Object = MibScalar
upLinkEff = _UpLinkEff_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 12),
    _UpLinkEff_Type()
)
upLinkEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upLinkEff.setStatus("current")
if mibBuilder.loadTexts:
    upLinkEff.setUnits("%")
_ExpUpFragCount_Type = Gauge32
_ExpUpFragCount_Object = MibScalar
expUpFragCount = _ExpUpFragCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 13),
    _ExpUpFragCount_Type()
)
expUpFragCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expUpFragCount.setStatus("current")
_ActUpFragCount_Type = Gauge32
_ActUpFragCount_Object = MibScalar
actUpFragCount = _ActUpFragCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 14),
    _ActUpFragCount_Type()
)
actUpFragCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actUpFragCount.setStatus("current")
_MaxUpLinkIndex_Type = Integer32
_MaxUpLinkIndex_Object = MibScalar
maxUpLinkIndex = _MaxUpLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 15),
    _MaxUpLinkIndex_Type()
)
maxUpLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxUpLinkIndex.setStatus("current")
_ActUpLinkIndex_Type = Integer32
_ActUpLinkIndex_Object = MibScalar
actUpLinkIndex = _ActUpLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 16),
    _ActUpLinkIndex_Type()
)
actUpLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actUpLinkIndex.setStatus("current")
_Fragments1xDwnLinkVertical_Type = Integer32
_Fragments1xDwnLinkVertical_Object = MibScalar
fragments1xDwnLinkVertical = _Fragments1xDwnLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 17),
    _Fragments1xDwnLinkVertical_Type()
)
fragments1xDwnLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments1xDwnLinkVertical.setStatus("current")
_Fragments2xDwnLinkVertical_Type = Integer32
_Fragments2xDwnLinkVertical_Object = MibScalar
fragments2xDwnLinkVertical = _Fragments2xDwnLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 18),
    _Fragments2xDwnLinkVertical_Type()
)
fragments2xDwnLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments2xDwnLinkVertical.setStatus("current")
_Fragments3xDwnLinkVertical_Type = Integer32
_Fragments3xDwnLinkVertical_Object = MibScalar
fragments3xDwnLinkVertical = _Fragments3xDwnLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 19),
    _Fragments3xDwnLinkVertical_Type()
)
fragments3xDwnLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments3xDwnLinkVertical.setStatus("current")
_Fragments4xDwnLinkVertical_Type = Integer32
_Fragments4xDwnLinkVertical_Object = MibScalar
fragments4xDwnLinkVertical = _Fragments4xDwnLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 20),
    _Fragments4xDwnLinkVertical_Type()
)
fragments4xDwnLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments4xDwnLinkVertical.setStatus("current")
_Fragments1xUpLinkVertical_Type = Integer32
_Fragments1xUpLinkVertical_Object = MibScalar
fragments1xUpLinkVertical = _Fragments1xUpLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 21),
    _Fragments1xUpLinkVertical_Type()
)
fragments1xUpLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments1xUpLinkVertical.setStatus("current")
_Fragments2xUpLinkVertical_Type = Integer32
_Fragments2xUpLinkVertical_Object = MibScalar
fragments2xUpLinkVertical = _Fragments2xUpLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 22),
    _Fragments2xUpLinkVertical_Type()
)
fragments2xUpLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments2xUpLinkVertical.setStatus("current")
_Fragments3xUpLinkVertical_Type = Integer32
_Fragments3xUpLinkVertical_Object = MibScalar
fragments3xUpLinkVertical = _Fragments3xUpLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 23),
    _Fragments3xUpLinkVertical_Type()
)
fragments3xUpLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments3xUpLinkVertical.setStatus("current")
_Fragments4xUpLinkVertical_Type = Integer32
_Fragments4xUpLinkVertical_Object = MibScalar
fragments4xUpLinkVertical = _Fragments4xUpLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 24),
    _Fragments4xUpLinkVertical_Type()
)
fragments4xUpLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments4xUpLinkVertical.setStatus("current")
_BitErrorsCorrected1xDwnLinkVertical_Type = DisplayString
_BitErrorsCorrected1xDwnLinkVertical_Object = MibScalar
bitErrorsCorrected1xDwnLinkVertical = _BitErrorsCorrected1xDwnLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 25),
    _BitErrorsCorrected1xDwnLinkVertical_Type()
)
bitErrorsCorrected1xDwnLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected1xDwnLinkVertical.setStatus("current")
_BitErrorsCorrected2xDwnLinkVertical_Type = DisplayString
_BitErrorsCorrected2xDwnLinkVertical_Object = MibScalar
bitErrorsCorrected2xDwnLinkVertical = _BitErrorsCorrected2xDwnLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 26),
    _BitErrorsCorrected2xDwnLinkVertical_Type()
)
bitErrorsCorrected2xDwnLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected2xDwnLinkVertical.setStatus("current")
_BitErrorsCorrected3xDwnLinkVertical_Type = DisplayString
_BitErrorsCorrected3xDwnLinkVertical_Object = MibScalar
bitErrorsCorrected3xDwnLinkVertical = _BitErrorsCorrected3xDwnLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 27),
    _BitErrorsCorrected3xDwnLinkVertical_Type()
)
bitErrorsCorrected3xDwnLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected3xDwnLinkVertical.setStatus("current")
_BitErrorsCorrected4xDwnLinkVertical_Type = DisplayString
_BitErrorsCorrected4xDwnLinkVertical_Object = MibScalar
bitErrorsCorrected4xDwnLinkVertical = _BitErrorsCorrected4xDwnLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 28),
    _BitErrorsCorrected4xDwnLinkVertical_Type()
)
bitErrorsCorrected4xDwnLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected4xDwnLinkVertical.setStatus("current")
_BitErrorsCorrected1xUpLinkVertical_Type = DisplayString
_BitErrorsCorrected1xUpLinkVertical_Object = MibScalar
bitErrorsCorrected1xUpLinkVertical = _BitErrorsCorrected1xUpLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 29),
    _BitErrorsCorrected1xUpLinkVertical_Type()
)
bitErrorsCorrected1xUpLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected1xUpLinkVertical.setStatus("current")
_BitErrorsCorrected2xUpLinkVertical_Type = DisplayString
_BitErrorsCorrected2xUpLinkVertical_Object = MibScalar
bitErrorsCorrected2xUpLinkVertical = _BitErrorsCorrected2xUpLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 30),
    _BitErrorsCorrected2xUpLinkVertical_Type()
)
bitErrorsCorrected2xUpLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected2xUpLinkVertical.setStatus("current")
_BitErrorsCorrected3xUpLinkVertical_Type = DisplayString
_BitErrorsCorrected3xUpLinkVertical_Object = MibScalar
bitErrorsCorrected3xUpLinkVertical = _BitErrorsCorrected3xUpLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 31),
    _BitErrorsCorrected3xUpLinkVertical_Type()
)
bitErrorsCorrected3xUpLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected3xUpLinkVertical.setStatus("current")
_BitErrorsCorrected4xUpLinkVertical_Type = DisplayString
_BitErrorsCorrected4xUpLinkVertical_Object = MibScalar
bitErrorsCorrected4xUpLinkVertical = _BitErrorsCorrected4xUpLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 32),
    _BitErrorsCorrected4xUpLinkVertical_Type()
)
bitErrorsCorrected4xUpLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected4xUpLinkVertical.setStatus("current")
_SignalToNoiseRatioDownLinkVertical_Type = Integer32
_SignalToNoiseRatioDownLinkVertical_Object = MibScalar
signalToNoiseRatioDownLinkVertical = _SignalToNoiseRatioDownLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 33),
    _SignalToNoiseRatioDownLinkVertical_Type()
)
signalToNoiseRatioDownLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalToNoiseRatioDownLinkVertical.setStatus("current")
_SignalToNoiseRatioUpLinkVertical_Type = Integer32
_SignalToNoiseRatioUpLinkVertical_Object = MibScalar
signalToNoiseRatioUpLinkVertical = _SignalToNoiseRatioUpLinkVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 34),
    _SignalToNoiseRatioUpLinkVertical_Type()
)
signalToNoiseRatioUpLinkVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalToNoiseRatioUpLinkVertical.setStatus("current")
_Fragments1xDwnLinkHorizontal_Type = Integer32
_Fragments1xDwnLinkHorizontal_Object = MibScalar
fragments1xDwnLinkHorizontal = _Fragments1xDwnLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 35),
    _Fragments1xDwnLinkHorizontal_Type()
)
fragments1xDwnLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments1xDwnLinkHorizontal.setStatus("current")
_Fragments2xDwnLinkHorizontal_Type = Integer32
_Fragments2xDwnLinkHorizontal_Object = MibScalar
fragments2xDwnLinkHorizontal = _Fragments2xDwnLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 36),
    _Fragments2xDwnLinkHorizontal_Type()
)
fragments2xDwnLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments2xDwnLinkHorizontal.setStatus("current")
_Fragments3xDwnLinkHorizontal_Type = Integer32
_Fragments3xDwnLinkHorizontal_Object = MibScalar
fragments3xDwnLinkHorizontal = _Fragments3xDwnLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 37),
    _Fragments3xDwnLinkHorizontal_Type()
)
fragments3xDwnLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments3xDwnLinkHorizontal.setStatus("current")
_Fragments4xDwnLinkHorizontal_Type = Integer32
_Fragments4xDwnLinkHorizontal_Object = MibScalar
fragments4xDwnLinkHorizontal = _Fragments4xDwnLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 38),
    _Fragments4xDwnLinkHorizontal_Type()
)
fragments4xDwnLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments4xDwnLinkHorizontal.setStatus("current")
_Fragments1xUpLinkHorizontal_Type = Integer32
_Fragments1xUpLinkHorizontal_Object = MibScalar
fragments1xUpLinkHorizontal = _Fragments1xUpLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 39),
    _Fragments1xUpLinkHorizontal_Type()
)
fragments1xUpLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments1xUpLinkHorizontal.setStatus("current")
_Fragments2xUpLinkHorizontal_Type = Integer32
_Fragments2xUpLinkHorizontal_Object = MibScalar
fragments2xUpLinkHorizontal = _Fragments2xUpLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 40),
    _Fragments2xUpLinkHorizontal_Type()
)
fragments2xUpLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments2xUpLinkHorizontal.setStatus("current")
_Fragments3xUpLinkHorizontal_Type = Integer32
_Fragments3xUpLinkHorizontal_Object = MibScalar
fragments3xUpLinkHorizontal = _Fragments3xUpLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 41),
    _Fragments3xUpLinkHorizontal_Type()
)
fragments3xUpLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments3xUpLinkHorizontal.setStatus("current")
_Fragments4xUpLinkHorizontal_Type = Integer32
_Fragments4xUpLinkHorizontal_Object = MibScalar
fragments4xUpLinkHorizontal = _Fragments4xUpLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 42),
    _Fragments4xUpLinkHorizontal_Type()
)
fragments4xUpLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragments4xUpLinkHorizontal.setStatus("current")
_BitErrorsCorrected1xDwnLinkHorizontal_Type = DisplayString
_BitErrorsCorrected1xDwnLinkHorizontal_Object = MibScalar
bitErrorsCorrected1xDwnLinkHorizontal = _BitErrorsCorrected1xDwnLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 43),
    _BitErrorsCorrected1xDwnLinkHorizontal_Type()
)
bitErrorsCorrected1xDwnLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected1xDwnLinkHorizontal.setStatus("current")
_BitErrorsCorrected2xDwnLinkHorizontal_Type = DisplayString
_BitErrorsCorrected2xDwnLinkHorizontal_Object = MibScalar
bitErrorsCorrected2xDwnLinkHorizontal = _BitErrorsCorrected2xDwnLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 44),
    _BitErrorsCorrected2xDwnLinkHorizontal_Type()
)
bitErrorsCorrected2xDwnLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected2xDwnLinkHorizontal.setStatus("current")
_BitErrorsCorrected3xDwnLinkHorizontal_Type = DisplayString
_BitErrorsCorrected3xDwnLinkHorizontal_Object = MibScalar
bitErrorsCorrected3xDwnLinkHorizontal = _BitErrorsCorrected3xDwnLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 45),
    _BitErrorsCorrected3xDwnLinkHorizontal_Type()
)
bitErrorsCorrected3xDwnLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected3xDwnLinkHorizontal.setStatus("current")
_BitErrorsCorrected4xDwnLinkHorizontal_Type = DisplayString
_BitErrorsCorrected4xDwnLinkHorizontal_Object = MibScalar
bitErrorsCorrected4xDwnLinkHorizontal = _BitErrorsCorrected4xDwnLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 46),
    _BitErrorsCorrected4xDwnLinkHorizontal_Type()
)
bitErrorsCorrected4xDwnLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected4xDwnLinkHorizontal.setStatus("current")
_BitErrorsCorrected1xUpLinkHorizontal_Type = DisplayString
_BitErrorsCorrected1xUpLinkHorizontal_Object = MibScalar
bitErrorsCorrected1xUpLinkHorizontal = _BitErrorsCorrected1xUpLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 47),
    _BitErrorsCorrected1xUpLinkHorizontal_Type()
)
bitErrorsCorrected1xUpLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected1xUpLinkHorizontal.setStatus("current")
_BitErrorsCorrected2xUpLinkHorizontal_Type = DisplayString
_BitErrorsCorrected2xUpLinkHorizontal_Object = MibScalar
bitErrorsCorrected2xUpLinkHorizontal = _BitErrorsCorrected2xUpLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 48),
    _BitErrorsCorrected2xUpLinkHorizontal_Type()
)
bitErrorsCorrected2xUpLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected2xUpLinkHorizontal.setStatus("current")
_BitErrorsCorrected3xUpLinkHorizontal_Type = DisplayString
_BitErrorsCorrected3xUpLinkHorizontal_Object = MibScalar
bitErrorsCorrected3xUpLinkHorizontal = _BitErrorsCorrected3xUpLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 49),
    _BitErrorsCorrected3xUpLinkHorizontal_Type()
)
bitErrorsCorrected3xUpLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected3xUpLinkHorizontal.setStatus("current")
_BitErrorsCorrected4xUpLinkHorizontal_Type = DisplayString
_BitErrorsCorrected4xUpLinkHorizontal_Object = MibScalar
bitErrorsCorrected4xUpLinkHorizontal = _BitErrorsCorrected4xUpLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 50),
    _BitErrorsCorrected4xUpLinkHorizontal_Type()
)
bitErrorsCorrected4xUpLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitErrorsCorrected4xUpLinkHorizontal.setStatus("current")
_SignalToNoiseRatioDownLinkHorizontal_Type = Integer32
_SignalToNoiseRatioDownLinkHorizontal_Object = MibScalar
signalToNoiseRatioDownLinkHorizontal = _SignalToNoiseRatioDownLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 51),
    _SignalToNoiseRatioDownLinkHorizontal_Type()
)
signalToNoiseRatioDownLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalToNoiseRatioDownLinkHorizontal.setStatus("current")
_SignalToNoiseRatioUpLinkHorizontal_Type = Integer32
_SignalToNoiseRatioUpLinkHorizontal_Object = MibScalar
signalToNoiseRatioUpLinkHorizontal = _SignalToNoiseRatioUpLinkHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 2, 52),
    _SignalToNoiseRatioUpLinkHorizontal_Type()
)
signalToNoiseRatioUpLinkHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalToNoiseRatioUpLinkHorizontal.setStatus("current")
_WhispRegStatus_Type = DisplayString
_WhispRegStatus_Object = MibScalar
whispRegStatus = _WhispRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 2, 4),
    _WhispRegStatus_Type()
)
whispRegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispRegStatus.setStatus("obsolete")
_WhispApsGPS_ObjectIdentity = ObjectIdentity
whispApsGPS = _WhispApsGPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3)
)


class _WhispGPSStats_Type(Integer32):
    """Custom type whispGPSStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("generatingSync", 3),
          ("gpsLostSync", 2),
          ("gpsSynchronized", 1))
    )


_WhispGPSStats_Type.__name__ = "Integer32"
_WhispGPSStats_Object = MibScalar
whispGPSStats = _WhispGPSStats_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 1),
    _WhispGPSStats_Type()
)
whispGPSStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whispGPSStats.setStatus("current")
_GpsSyncSource_Type = DisplayString
_GpsSyncSource_Object = MibScalar
gpsSyncSource = _GpsSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 2),
    _GpsSyncSource_Type()
)
gpsSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSyncSource.setStatus("current")
_GpsSyncStatus_Type = DisplayString
_GpsSyncStatus_Object = MibScalar
gpsSyncStatus = _GpsSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 3),
    _GpsSyncStatus_Type()
)
gpsSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSyncStatus.setStatus("current")
_GpsTrackingMode_Type = DisplayString
_GpsTrackingMode_Object = MibScalar
gpsTrackingMode = _GpsTrackingMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 4),
    _GpsTrackingMode_Type()
)
gpsTrackingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTrackingMode.setStatus("current")
_GpsTime_Type = DisplayString
_GpsTime_Object = MibScalar
gpsTime = _GpsTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 5),
    _GpsTime_Type()
)
gpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTime.setStatus("current")
_GpsDate_Type = DisplayString
_GpsDate_Object = MibScalar
gpsDate = _GpsDate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 6),
    _GpsDate_Type()
)
gpsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsDate.setStatus("current")
_GpsSatellitesTracked_Type = DisplayString
_GpsSatellitesTracked_Object = MibScalar
gpsSatellitesTracked = _GpsSatellitesTracked_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 7),
    _GpsSatellitesTracked_Type()
)
gpsSatellitesTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatellitesTracked.setStatus("current")
_GpsSatellitesVisible_Type = DisplayString
_GpsSatellitesVisible_Object = MibScalar
gpsSatellitesVisible = _GpsSatellitesVisible_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 8),
    _GpsSatellitesVisible_Type()
)
gpsSatellitesVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatellitesVisible.setStatus("current")
_GpsHeight_Type = DisplayString
_GpsHeight_Object = MibScalar
gpsHeight = _GpsHeight_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 9),
    _GpsHeight_Type()
)
gpsHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHeight.setStatus("current")
_GpsAntennaConnection_Type = DisplayString
_GpsAntennaConnection_Object = MibScalar
gpsAntennaConnection = _GpsAntennaConnection_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 10),
    _GpsAntennaConnection_Type()
)
gpsAntennaConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAntennaConnection.setStatus("current")
_GpsLatitude_Type = DisplayString
_GpsLatitude_Object = MibScalar
gpsLatitude = _GpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 11),
    _GpsLatitude_Type()
)
gpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLatitude.setStatus("current")
_GpsLongitude_Type = DisplayString
_GpsLongitude_Object = MibScalar
gpsLongitude = _GpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 12),
    _GpsLongitude_Type()
)
gpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLongitude.setStatus("current")
_GpsInvalidMsg_Type = DisplayString
_GpsInvalidMsg_Object = MibScalar
gpsInvalidMsg = _GpsInvalidMsg_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 13),
    _GpsInvalidMsg_Type()
)
gpsInvalidMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsInvalidMsg.setStatus("current")
_GpsRestartCount_Type = Integer32
_GpsRestartCount_Object = MibScalar
gpsRestartCount = _GpsRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 14),
    _GpsRestartCount_Type()
)
gpsRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsRestartCount.setStatus("current")
_GpsReInitCount_Type = Integer32
_GpsReInitCount_Object = MibScalar
gpsReInitCount = _GpsReInitCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 15),
    _GpsReInitCount_Type()
)
gpsReInitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReInitCount.setStatus("current")
_GpsReceiverInfo_Type = DisplayString
_GpsReceiverInfo_Object = MibScalar
gpsReceiverInfo = _GpsReceiverInfo_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 16),
    _GpsReceiverInfo_Type()
)
gpsReceiverInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReceiverInfo.setStatus("current")


class _GpsFreeRun_Type(Integer32):
    """Custom type gpsFreeRun based on Integer32"""
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


_GpsFreeRun_Type.__name__ = "Integer32"
_GpsFreeRun_Object = MibScalar
gpsFreeRun = _GpsFreeRun_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 17),
    _GpsFreeRun_Type()
)
gpsFreeRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpsFreeRun.setStatus("current")


class _AutoSyncStatus_Type(Integer32):
    """Custom type autoSyncStatus based on Integer32"""
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
        *(("noSync", 0),
          ("onBoardGPSAndPowrPortSync", 5),
          ("onBoardGPSAndTimingPortUGPSAndPowrPortSync", 7),
          ("onBoardGPSAndTimingPortUGPSSync", 3),
          ("onBoardGPSSync", 1),
          ("powrPortSync", 4),
          ("timingPortUGPSAndPowrPortSync", 6),
          ("timingPortUGPSSync", 2))
    )


_AutoSyncStatus_Type.__name__ = "Integer32"
_AutoSyncStatus_Object = MibScalar
autoSyncStatus = _AutoSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 3, 18),
    _AutoSyncStatus_Type()
)
autoSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoSyncStatus.setStatus("current")
_WhispLinkTable_Object = MibTable
whispLinkTable = _WhispLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4)
)
if mibBuilder.loadTexts:
    whispLinkTable.setStatus("current")
_WhispLinkEntry_Object = MibTableRow
whispLinkEntry = _WhispLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1)
)
whispLinkEntry.setIndexNames(
    (0, "WHISP-APS-MIB", "linkLUID"),
)
if mibBuilder.loadTexts:
    whispLinkEntry.setStatus("current")


class _LinkLUID_Type(Integer32):
    """Custom type linkLUID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LinkLUID_Type.__name__ = "Integer32"
_LinkLUID_Object = MibTableColumn
linkLUID = _LinkLUID_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 1),
    _LinkLUID_Type()
)
linkLUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLUID.setStatus("current")
_LinkDescr_Type = DisplayString
_LinkDescr_Object = MibTableColumn
linkDescr = _LinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 2),
    _LinkDescr_Type()
)
linkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDescr.setStatus("current")
_LinkPhysAddress_Type = PhysAddress
_LinkPhysAddress_Object = MibTableColumn
linkPhysAddress = _LinkPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 3),
    _LinkPhysAddress_Type()
)
linkPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPhysAddress.setStatus("current")
_LinkMtu_Type = Integer32
_LinkMtu_Object = MibTableColumn
linkMtu = _LinkMtu_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 4),
    _LinkMtu_Type()
)
linkMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkMtu.setStatus("current")
_LinkSpeed_Type = Gauge32
_LinkSpeed_Object = MibTableColumn
linkSpeed = _LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 5),
    _LinkSpeed_Type()
)
linkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSpeed.setStatus("current")


class _LinkOperStatus_Type(Integer32):
    """Custom type linkOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LinkOperStatus_Type.__name__ = "Integer32"
_LinkOperStatus_Object = MibTableColumn
linkOperStatus = _LinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 6),
    _LinkOperStatus_Type()
)
linkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOperStatus.setStatus("obsolete")
_LinkInOctets_Type = Counter32
_LinkInOctets_Object = MibTableColumn
linkInOctets = _LinkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 7),
    _LinkInOctets_Type()
)
linkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInOctets.setStatus("current")
_LinkInUcastPkts_Type = Counter32
_LinkInUcastPkts_Object = MibTableColumn
linkInUcastPkts = _LinkInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 8),
    _LinkInUcastPkts_Type()
)
linkInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInUcastPkts.setStatus("current")
_LinkInNUcastPkts_Type = Counter32
_LinkInNUcastPkts_Object = MibTableColumn
linkInNUcastPkts = _LinkInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 9),
    _LinkInNUcastPkts_Type()
)
linkInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInNUcastPkts.setStatus("current")
_LinkInDiscards_Type = Counter32
_LinkInDiscards_Object = MibTableColumn
linkInDiscards = _LinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 10),
    _LinkInDiscards_Type()
)
linkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInDiscards.setStatus("current")
_LinkInError_Type = Counter32
_LinkInError_Object = MibTableColumn
linkInError = _LinkInError_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 11),
    _LinkInError_Type()
)
linkInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInError.setStatus("current")
_LinkInUnknownProtos_Type = Counter32
_LinkInUnknownProtos_Object = MibTableColumn
linkInUnknownProtos = _LinkInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 12),
    _LinkInUnknownProtos_Type()
)
linkInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInUnknownProtos.setStatus("current")
_LinkOutOctets_Type = Counter32
_LinkOutOctets_Object = MibTableColumn
linkOutOctets = _LinkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 13),
    _LinkOutOctets_Type()
)
linkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutOctets.setStatus("current")
_LinkOutUcastPkts_Type = Counter32
_LinkOutUcastPkts_Object = MibTableColumn
linkOutUcastPkts = _LinkOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 14),
    _LinkOutUcastPkts_Type()
)
linkOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutUcastPkts.setStatus("current")
_LinkOutNUcastPkts_Type = Counter32
_LinkOutNUcastPkts_Object = MibTableColumn
linkOutNUcastPkts = _LinkOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 15),
    _LinkOutNUcastPkts_Type()
)
linkOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutNUcastPkts.setStatus("current")
_LinkOutDiscards_Type = Counter32
_LinkOutDiscards_Object = MibTableColumn
linkOutDiscards = _LinkOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 16),
    _LinkOutDiscards_Type()
)
linkOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutDiscards.setStatus("current")
_LinkOutError_Type = Counter32
_LinkOutError_Object = MibTableColumn
linkOutError = _LinkOutError_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 17),
    _LinkOutError_Type()
)
linkOutError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutError.setStatus("current")
_LinkOutQLen_Type = Gauge32
_LinkOutQLen_Object = MibTableColumn
linkOutQLen = _LinkOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 18),
    _LinkOutQLen_Type()
)
linkOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutQLen.setStatus("current")


class _LinkSessState_Type(Integer32):
    """Custom type linkSessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("authChal", 4),
          ("clearing", 2),
          ("idle", 0),
          ("inSession", 1),
          ("notInUse", 6),
          ("reRegDnRst", 3),
          ("registering", 5))
    )


_LinkSessState_Type.__name__ = "Integer32"
_LinkSessState_Object = MibTableColumn
linkSessState = _LinkSessState_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 19),
    _LinkSessState_Type()
)
linkSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSessState.setStatus("current")
_LinkESN_Type = PhysAddress
_LinkESN_Object = MibTableColumn
linkESN = _LinkESN_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 20),
    _LinkESN_Type()
)
linkESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkESN.setStatus("current")
_LinkRSSI_Type = Integer32
_LinkRSSI_Object = MibTableColumn
linkRSSI = _LinkRSSI_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 21),
    _LinkRSSI_Type()
)
linkRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRSSI.setStatus("current")


class _LinkAveJitter_Type(Gauge32):
    """Custom type linkAveJitter based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LinkAveJitter_Type.__name__ = "Gauge32"
_LinkAveJitter_Object = MibTableColumn
linkAveJitter = _LinkAveJitter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 22),
    _LinkAveJitter_Type()
)
linkAveJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAveJitter.setStatus("current")


class _LinkLastJitter_Type(Gauge32):
    """Custom type linkLastJitter based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LinkLastJitter_Type.__name__ = "Gauge32"
_LinkLastJitter_Object = MibTableColumn
linkLastJitter = _LinkLastJitter_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 23),
    _LinkLastJitter_Type()
)
linkLastJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLastJitter.setStatus("current")
_LinkAirDelay_Type = Integer32
_LinkAirDelay_Object = MibTableColumn
linkAirDelay = _LinkAirDelay_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 24),
    _LinkAirDelay_Type()
)
linkAirDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAirDelay.setStatus("current")
_LinkRegCount_Type = Integer32
_LinkRegCount_Object = MibTableColumn
linkRegCount = _LinkRegCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 25),
    _LinkRegCount_Type()
)
linkRegCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRegCount.setStatus("current")
_LinkReRegCount_Type = Integer32
_LinkReRegCount_Object = MibTableColumn
linkReRegCount = _LinkReRegCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 26),
    _LinkReRegCount_Type()
)
linkReRegCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkReRegCount.setStatus("current")
_LinkTimeOut_Type = Integer32
_LinkTimeOut_Object = MibTableColumn
linkTimeOut = _LinkTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 27),
    _LinkTimeOut_Type()
)
linkTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTimeOut.setStatus("current")
_LinkLastRSSI_Type = Integer32
_LinkLastRSSI_Object = MibTableColumn
linkLastRSSI = _LinkLastRSSI_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 28),
    _LinkLastRSSI_Type()
)
linkLastRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLastRSSI.setStatus("current")
_SessionCount_Type = Integer32
_SessionCount_Object = MibTableColumn
sessionCount = _SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 29),
    _SessionCount_Type()
)
sessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionCount.setStatus("current")
_SoftwareVersion_Type = DisplayString
_SoftwareVersion_Object = MibTableColumn
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 30),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_SoftwareBootVersion_Type = DisplayString
_SoftwareBootVersion_Object = MibTableColumn
softwareBootVersion = _SoftwareBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 31),
    _SoftwareBootVersion_Type()
)
softwareBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareBootVersion.setStatus("current")
_FpgaVersion_Type = DisplayString
_FpgaVersion_Object = MibTableColumn
fpgaVersion = _FpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 32),
    _FpgaVersion_Type()
)
fpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaVersion.setStatus("current")
_LinkSiteName_Type = DisplayString
_LinkSiteName_Object = MibTableColumn
linkSiteName = _LinkSiteName_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 33),
    _LinkSiteName_Type()
)
linkSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSiteName.setStatus("current")
_AvgPowerLevel_Type = DisplayString
_AvgPowerLevel_Object = MibTableColumn
avgPowerLevel = _AvgPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 34),
    _AvgPowerLevel_Type()
)
avgPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgPowerLevel.setStatus("current")
_LastPowerLevel_Type = DisplayString
_LastPowerLevel_Object = MibTableColumn
lastPowerLevel = _LastPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 35),
    _LastPowerLevel_Type()
)
lastPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPowerLevel.setStatus("current")
_SesDownLinkRate_Type = Integer32
_SesDownLinkRate_Object = MibTableColumn
sesDownLinkRate = _SesDownLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 36),
    _SesDownLinkRate_Type()
)
sesDownLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesDownLinkRate.setStatus("current")
_SesDownLinkLimit_Type = Integer32
_SesDownLinkLimit_Object = MibTableColumn
sesDownLinkLimit = _SesDownLinkLimit_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 37),
    _SesDownLinkLimit_Type()
)
sesDownLinkLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesDownLinkLimit.setStatus("current")
_SesUpLinkRate_Type = Integer32
_SesUpLinkRate_Object = MibTableColumn
sesUpLinkRate = _SesUpLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 38),
    _SesUpLinkRate_Type()
)
sesUpLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesUpLinkRate.setStatus("current")
_SesUpLinkLimit_Type = Integer32
_SesUpLinkLimit_Object = MibTableColumn
sesUpLinkLimit = _SesUpLinkLimit_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 39),
    _SesUpLinkLimit_Type()
)
sesUpLinkLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesUpLinkLimit.setStatus("current")
_AdaptRate_Type = DisplayString
_AdaptRate_Object = MibTableColumn
adaptRate = _AdaptRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 40),
    _AdaptRate_Type()
)
adaptRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptRate.setStatus("current")
_SesLoUpCIR_Type = Integer32
_SesLoUpCIR_Object = MibTableColumn
sesLoUpCIR = _SesLoUpCIR_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 41),
    _SesLoUpCIR_Type()
)
sesLoUpCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLoUpCIR.setStatus("current")
_SesLoDownCIR_Type = Integer32
_SesLoDownCIR_Object = MibTableColumn
sesLoDownCIR = _SesLoDownCIR_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 42),
    _SesLoDownCIR_Type()
)
sesLoDownCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLoDownCIR.setStatus("current")
_SesHiUpCIR_Type = Integer32
_SesHiUpCIR_Object = MibTableColumn
sesHiUpCIR = _SesHiUpCIR_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 43),
    _SesHiUpCIR_Type()
)
sesHiUpCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesHiUpCIR.setStatus("current")
_SesHiDownCIR_Type = Integer32
_SesHiDownCIR_Object = MibTableColumn
sesHiDownCIR = _SesHiDownCIR_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 44),
    _SesHiDownCIR_Type()
)
sesHiDownCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesHiDownCIR.setStatus("current")
_PlatformVer_Type = Integer32
_PlatformVer_Object = MibTableColumn
platformVer = _PlatformVer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 45),
    _PlatformVer_Type()
)
platformVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    platformVer.setStatus("current")
_SmSessionTmr_Type = TimeTicks
_SmSessionTmr_Object = MibTableColumn
smSessionTmr = _SmSessionTmr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 46),
    _SmSessionTmr_Type()
)
smSessionTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSessionTmr.setStatus("current")
_SmSessionSeqNumMismatch_Type = Counter32
_SmSessionSeqNumMismatch_Object = MibTableColumn
smSessionSeqNumMismatch = _SmSessionSeqNumMismatch_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 47),
    _SmSessionSeqNumMismatch_Type()
)
smSessionSeqNumMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSessionSeqNumMismatch.setStatus("current")
_DataVCNum_Type = Integer32
_DataVCNum_Object = MibTableColumn
dataVCNum = _DataVCNum_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 48),
    _DataVCNum_Type()
)
dataVCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataVCNum.setStatus("current")


class _HiPriQEn_Type(Integer32):
    """Custom type hiPriQEn based on Integer32"""
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


_HiPriQEn_Type.__name__ = "Integer32"
_HiPriQEn_Object = MibTableColumn
hiPriQEn = _HiPriQEn_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 49),
    _HiPriQEn_Type()
)
hiPriQEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hiPriQEn.setStatus("current")
_DataVCNumHiQ_Type = Integer32
_DataVCNumHiQ_Object = MibTableColumn
dataVCNumHiQ = _DataVCNumHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 50),
    _DataVCNumHiQ_Type()
)
dataVCNumHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataVCNumHiQ.setStatus("current")
_LinkInOctetsHiQ_Type = Counter32
_LinkInOctetsHiQ_Object = MibTableColumn
linkInOctetsHiQ = _LinkInOctetsHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 51),
    _LinkInOctetsHiQ_Type()
)
linkInOctetsHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInOctetsHiQ.setStatus("current")
_LinkInUcastPktsHiQ_Type = Counter32
_LinkInUcastPktsHiQ_Object = MibTableColumn
linkInUcastPktsHiQ = _LinkInUcastPktsHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 52),
    _LinkInUcastPktsHiQ_Type()
)
linkInUcastPktsHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInUcastPktsHiQ.setStatus("current")
_LinkInNUcastPktsHiQ_Type = Counter32
_LinkInNUcastPktsHiQ_Object = MibTableColumn
linkInNUcastPktsHiQ = _LinkInNUcastPktsHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 53),
    _LinkInNUcastPktsHiQ_Type()
)
linkInNUcastPktsHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInNUcastPktsHiQ.setStatus("current")
_LinkInDiscardsHiQ_Type = Counter32
_LinkInDiscardsHiQ_Object = MibTableColumn
linkInDiscardsHiQ = _LinkInDiscardsHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 54),
    _LinkInDiscardsHiQ_Type()
)
linkInDiscardsHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInDiscardsHiQ.setStatus("current")
_LinkInErrorHiQ_Type = Counter32
_LinkInErrorHiQ_Object = MibTableColumn
linkInErrorHiQ = _LinkInErrorHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 55),
    _LinkInErrorHiQ_Type()
)
linkInErrorHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInErrorHiQ.setStatus("current")
_LinkInUnknownProtosHiQ_Type = Counter32
_LinkInUnknownProtosHiQ_Object = MibTableColumn
linkInUnknownProtosHiQ = _LinkInUnknownProtosHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 56),
    _LinkInUnknownProtosHiQ_Type()
)
linkInUnknownProtosHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInUnknownProtosHiQ.setStatus("current")
_LinkOutOctetsHiQ_Type = Counter32
_LinkOutOctetsHiQ_Object = MibTableColumn
linkOutOctetsHiQ = _LinkOutOctetsHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 57),
    _LinkOutOctetsHiQ_Type()
)
linkOutOctetsHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutOctetsHiQ.setStatus("current")
_LinkOutUcastPktsHiQ_Type = Counter32
_LinkOutUcastPktsHiQ_Object = MibTableColumn
linkOutUcastPktsHiQ = _LinkOutUcastPktsHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 58),
    _LinkOutUcastPktsHiQ_Type()
)
linkOutUcastPktsHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutUcastPktsHiQ.setStatus("current")
_LinkOutNUcastPktsHiQ_Type = Counter32
_LinkOutNUcastPktsHiQ_Object = MibTableColumn
linkOutNUcastPktsHiQ = _LinkOutNUcastPktsHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 59),
    _LinkOutNUcastPktsHiQ_Type()
)
linkOutNUcastPktsHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutNUcastPktsHiQ.setStatus("current")
_LinkOutDiscardsHiQ_Type = Counter32
_LinkOutDiscardsHiQ_Object = MibTableColumn
linkOutDiscardsHiQ = _LinkOutDiscardsHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 60),
    _LinkOutDiscardsHiQ_Type()
)
linkOutDiscardsHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutDiscardsHiQ.setStatus("current")
_LinkOutErrorHiQ_Type = Counter32
_LinkOutErrorHiQ_Object = MibTableColumn
linkOutErrorHiQ = _LinkOutErrorHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 61),
    _LinkOutErrorHiQ_Type()
)
linkOutErrorHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutErrorHiQ.setStatus("current")
_VcQOverflow_Type = Counter32
_VcQOverflow_Object = MibTableColumn
vcQOverflow = _VcQOverflow_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 62),
    _VcQOverflow_Type()
)
vcQOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQOverflow.setStatus("current")
_VcQOverflowHiQ_Type = Counter32
_VcQOverflowHiQ_Object = MibTableColumn
vcQOverflowHiQ = _VcQOverflowHiQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 63),
    _VcQOverflowHiQ_Type()
)
vcQOverflowHiQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQOverflowHiQ.setStatus("current")


class _P7p8HiPriQEn_Type(Integer32):
    """Custom type p7p8HiPriQEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled-or-NA", 0),
          ("enabled", 1))
    )


_P7p8HiPriQEn_Type.__name__ = "Integer32"
_P7p8HiPriQEn_Object = MibTableColumn
p7p8HiPriQEn = _P7p8HiPriQEn_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 64),
    _P7p8HiPriQEn_Type()
)
p7p8HiPriQEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p7p8HiPriQEn.setStatus("current")
_P7p8HiPriQ_Type = Counter32
_P7p8HiPriQ_Object = MibTableColumn
p7p8HiPriQ = _P7p8HiPriQ_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 65),
    _P7p8HiPriQ_Type()
)
p7p8HiPriQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p7p8HiPriQ.setStatus("current")
_LinkAirDelayns_Type = Integer32
_LinkAirDelayns_Object = MibTableColumn
linkAirDelayns = _LinkAirDelayns_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 66),
    _LinkAirDelayns_Type()
)
linkAirDelayns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAirDelayns.setStatus("current")
_LinkQualityAPData_Type = DisplayString
_LinkQualityAPData_Object = MibTableColumn
linkQualityAPData = _LinkQualityAPData_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 67),
    _LinkQualityAPData_Type()
)
linkQualityAPData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkQualityAPData.setStatus("current")
_LinkManagementIP_Type = IpAddress
_LinkManagementIP_Object = MibTableColumn
linkManagementIP = _LinkManagementIP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 69),
    _LinkManagementIP_Type()
)
linkManagementIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkManagementIP.setStatus("current")
_LinkFragmentsReceived1XVertical_Type = Counter32
_LinkFragmentsReceived1XVertical_Object = MibTableColumn
linkFragmentsReceived1XVertical = _LinkFragmentsReceived1XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 70),
    _LinkFragmentsReceived1XVertical_Type()
)
linkFragmentsReceived1XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFragmentsReceived1XVertical.setStatus("current")
_LinkFragmentsReceived2XVertical_Type = Counter32
_LinkFragmentsReceived2XVertical_Object = MibTableColumn
linkFragmentsReceived2XVertical = _LinkFragmentsReceived2XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 71),
    _LinkFragmentsReceived2XVertical_Type()
)
linkFragmentsReceived2XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFragmentsReceived2XVertical.setStatus("current")
_LinkFragmentsReceived3XVertical_Type = Counter32
_LinkFragmentsReceived3XVertical_Object = MibTableColumn
linkFragmentsReceived3XVertical = _LinkFragmentsReceived3XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 72),
    _LinkFragmentsReceived3XVertical_Type()
)
linkFragmentsReceived3XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFragmentsReceived3XVertical.setStatus("current")
_LinkFragmentsReceived4XVertical_Type = Counter32
_LinkFragmentsReceived4XVertical_Object = MibTableColumn
linkFragmentsReceived4XVertical = _LinkFragmentsReceived4XVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 73),
    _LinkFragmentsReceived4XVertical_Type()
)
linkFragmentsReceived4XVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFragmentsReceived4XVertical.setStatus("current")
_SignalToNoiseRatioVertical_Type = Integer32
_SignalToNoiseRatioVertical_Object = MibTableColumn
signalToNoiseRatioVertical = _SignalToNoiseRatioVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 74),
    _SignalToNoiseRatioVertical_Type()
)
signalToNoiseRatioVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalToNoiseRatioVertical.setStatus("current")
_RadiusReplyMsg_Type = DisplayString
_RadiusReplyMsg_Object = MibTableColumn
radiusReplyMsg = _RadiusReplyMsg_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 75),
    _RadiusReplyMsg_Type()
)
radiusReplyMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusReplyMsg.setStatus("current")
_AutoUpdateStatus_Type = Integer32
_AutoUpdateStatus_Object = MibTableColumn
autoUpdateStatus = _AutoUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 76),
    _AutoUpdateStatus_Type()
)
autoUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoUpdateStatus.setStatus("current")
_RadiusFramedIPAddress_Type = IpAddress
_RadiusFramedIPAddress_Object = MibTableColumn
radiusFramedIPAddress = _RadiusFramedIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 77),
    _RadiusFramedIPAddress_Type()
)
radiusFramedIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusFramedIPAddress.setStatus("current")
_RadiusFramedIPNetmask_Type = IpAddress
_RadiusFramedIPNetmask_Object = MibTableColumn
radiusFramedIPNetmask = _RadiusFramedIPNetmask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 78),
    _RadiusFramedIPNetmask_Type()
)
radiusFramedIPNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusFramedIPNetmask.setStatus("current")
_RadiusDefaultGateway_Type = IpAddress
_RadiusDefaultGateway_Object = MibTableColumn
radiusDefaultGateway = _RadiusDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 79),
    _RadiusDefaultGateway_Type()
)
radiusDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDefaultGateway.setStatus("current")
_LinkFragmentsReceived1XHorizontal_Type = Counter32
_LinkFragmentsReceived1XHorizontal_Object = MibTableColumn
linkFragmentsReceived1XHorizontal = _LinkFragmentsReceived1XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 80),
    _LinkFragmentsReceived1XHorizontal_Type()
)
linkFragmentsReceived1XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFragmentsReceived1XHorizontal.setStatus("current")
_LinkFragmentsReceived2XHorizontal_Type = Counter32
_LinkFragmentsReceived2XHorizontal_Object = MibTableColumn
linkFragmentsReceived2XHorizontal = _LinkFragmentsReceived2XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 81),
    _LinkFragmentsReceived2XHorizontal_Type()
)
linkFragmentsReceived2XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFragmentsReceived2XHorizontal.setStatus("current")
_LinkFragmentsReceived3XHorizontal_Type = Counter32
_LinkFragmentsReceived3XHorizontal_Object = MibTableColumn
linkFragmentsReceived3XHorizontal = _LinkFragmentsReceived3XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 82),
    _LinkFragmentsReceived3XHorizontal_Type()
)
linkFragmentsReceived3XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFragmentsReceived3XHorizontal.setStatus("current")
_LinkFragmentsReceived4XHorizontal_Type = Counter32
_LinkFragmentsReceived4XHorizontal_Object = MibTableColumn
linkFragmentsReceived4XHorizontal = _LinkFragmentsReceived4XHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 83),
    _LinkFragmentsReceived4XHorizontal_Type()
)
linkFragmentsReceived4XHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFragmentsReceived4XHorizontal.setStatus("current")
_SignalToNoiseRatioHorizontal_Type = Integer32
_SignalToNoiseRatioHorizontal_Object = MibTableColumn
signalToNoiseRatioHorizontal = _SignalToNoiseRatioHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 84),
    _SignalToNoiseRatioHorizontal_Type()
)
signalToNoiseRatioHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalToNoiseRatioHorizontal.setStatus("current")
_LinkSignalStrengthRatio_Type = DisplayString
_LinkSignalStrengthRatio_Object = MibTableColumn
linkSignalStrengthRatio = _LinkSignalStrengthRatio_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 86),
    _LinkSignalStrengthRatio_Type()
)
linkSignalStrengthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSignalStrengthRatio.setStatus("current")
_LinkRadioDbmHorizontal_Type = DisplayString
_LinkRadioDbmHorizontal_Object = MibTableColumn
linkRadioDbmHorizontal = _LinkRadioDbmHorizontal_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 87),
    _LinkRadioDbmHorizontal_Type()
)
linkRadioDbmHorizontal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRadioDbmHorizontal.setStatus("current")
_LinkRadioDbmVertical_Type = DisplayString
_LinkRadioDbmVertical_Object = MibTableColumn
linkRadioDbmVertical = _LinkRadioDbmVertical_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 88),
    _LinkRadioDbmVertical_Type()
)
linkRadioDbmVertical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRadioDbmVertical.setStatus("current")
_MaxSMTxPwr_Type = Integer32
_MaxSMTxPwr_Object = MibTableColumn
maxSMTxPwr = _MaxSMTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 89),
    _MaxSMTxPwr_Type()
)
maxSMTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSMTxPwr.setStatus("current")


class _ProductType_Type(Integer32):
    """Custom type productType based on Integer32"""
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
        *(("pmp430SISOOFDM", 2),
          ("pmp450MIMOOFDM", 1),
          ("pmp450SISOOFDM", 3),
          ("unknown", 0))
    )


_ProductType_Type.__name__ = "Integer32"
_ProductType_Object = MibTableColumn
productType = _ProductType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 90),
    _ProductType_Type()
)
productType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productType.setStatus("current")


class _LinkAdaptRateLowPri_Type(Integer32):
    """Custom type linkAdaptRateLowPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noSession", 0),
          ("rate1X", 1),
          ("rate2X", 2),
          ("rate4X", 4),
          ("rate6X", 6),
          ("rate8X", 8),
          ("rete3X", 3))
    )


_LinkAdaptRateLowPri_Type.__name__ = "Integer32"
_LinkAdaptRateLowPri_Object = MibTableColumn
linkAdaptRateLowPri = _LinkAdaptRateLowPri_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 91),
    _LinkAdaptRateLowPri_Type()
)
linkAdaptRateLowPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAdaptRateLowPri.setStatus("current")


class _LinkAdaptRateHighPri_Type(Integer32):
    """Custom type linkAdaptRateHighPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noHighPriorityChannel", -1),
          ("noSession", 0),
          ("rate1X", 1),
          ("rate2X", 2),
          ("rate4X", 4),
          ("rate6X", 6),
          ("rate8X", 8),
          ("rete3X", 3))
    )


_LinkAdaptRateHighPri_Type.__name__ = "Integer32"
_LinkAdaptRateHighPri_Object = MibTableColumn
linkAdaptRateHighPri = _LinkAdaptRateHighPri_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 4, 1, 92),
    _LinkAdaptRateHighPri_Type()
)
linkAdaptRateHighPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAdaptRateHighPri.setStatus("current")
_WhispApsEvent_ObjectIdentity = ObjectIdentity
whispApsEvent = _WhispApsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5)
)
_WhispApsRegEvent_ObjectIdentity = ObjectIdentity
whispApsRegEvent = _WhispApsRegEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 1)
)
_WhispGPSEvent_ObjectIdentity = ObjectIdentity
whispGPSEvent = _WhispGPSEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 2)
)
_WhispApsDfsEvent_ObjectIdentity = ObjectIdentity
whispApsDfsEvent = _WhispApsDfsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 3)
)
_WhispApRegulatoryEvent_ObjectIdentity = ObjectIdentity
whispApRegulatoryEvent = _WhispApRegulatoryEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 4)
)
_WhispApRFOverloadEvent_ObjectIdentity = ObjectIdentity
whispApRFOverloadEvent = _WhispApRFOverloadEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 5)
)
_WhispApsGroups_ObjectIdentity = ObjectIdentity
whispApsGroups = _WhispApsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 6)
)
_WhispApsStatus_ObjectIdentity = ObjectIdentity
whispApsStatus = _WhispApsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7)
)
_RegCount_Type = Unsigned32
_RegCount_Object = MibScalar
regCount = _RegCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 1),
    _RegCount_Type()
)
regCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regCount.setStatus("current")
_GpsStatus_Type = DisplayString
_GpsStatus_Object = MibScalar
gpsStatus = _GpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 2),
    _GpsStatus_Type()
)
gpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsStatus.setStatus("current")
_RadioSlicingAp_Type = Integer32
_RadioSlicingAp_Object = MibScalar
radioSlicingAp = _RadioSlicingAp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 3),
    _RadioSlicingAp_Type()
)
radioSlicingAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioSlicingAp.setStatus("obsolete")
_RadioTxGainAp_Type = Integer32
_RadioTxGainAp_Object = MibScalar
radioTxGainAp = _RadioTxGainAp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 4),
    _RadioTxGainAp_Type()
)
radioTxGainAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioTxGainAp.setStatus("current")
_DataSlotDwn_Type = Integer32
_DataSlotDwn_Object = MibScalar
dataSlotDwn = _DataSlotDwn_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 5),
    _DataSlotDwn_Type()
)
dataSlotDwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSlotDwn.setStatus("current")
_DataSlotUp_Type = Integer32
_DataSlotUp_Object = MibScalar
dataSlotUp = _DataSlotUp_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 6),
    _DataSlotUp_Type()
)
dataSlotUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSlotUp.setStatus("current")
_DataSlotUpHi_Type = Unsigned32
_DataSlotUpHi_Object = MibScalar
dataSlotUpHi = _DataSlotUpHi_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 7),
    _DataSlotUpHi_Type()
)
dataSlotUpHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSlotUpHi.setStatus("current")
_UpLnkAckSlot_Type = Unsigned32
_UpLnkAckSlot_Object = MibScalar
upLnkAckSlot = _UpLnkAckSlot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 8),
    _UpLnkAckSlot_Type()
)
upLnkAckSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upLnkAckSlot.setStatus("current")
_UpLnkAckSlotHi_Type = Unsigned32
_UpLnkAckSlotHi_Object = MibScalar
upLnkAckSlotHi = _UpLnkAckSlotHi_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 9),
    _UpLnkAckSlotHi_Type()
)
upLnkAckSlotHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upLnkAckSlotHi.setStatus("current")
_DwnLnkAckSlot_Type = Unsigned32
_DwnLnkAckSlot_Object = MibScalar
dwnLnkAckSlot = _DwnLnkAckSlot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 10),
    _DwnLnkAckSlot_Type()
)
dwnLnkAckSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwnLnkAckSlot.setStatus("current")
_DwnLnkAckSlotHi_Type = Unsigned32
_DwnLnkAckSlotHi_Object = MibScalar
dwnLnkAckSlotHi = _DwnLnkAckSlotHi_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 11),
    _DwnLnkAckSlotHi_Type()
)
dwnLnkAckSlotHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwnLnkAckSlotHi.setStatus("current")
_NumCtrSlot_Type = Unsigned32
_NumCtrSlot_Object = MibScalar
numCtrSlot = _NumCtrSlot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 12),
    _NumCtrSlot_Type()
)
numCtrSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numCtrSlot.setStatus("current")
_NumCtrSlotHi_Type = Unsigned32
_NumCtrSlotHi_Object = MibScalar
numCtrSlotHi = _NumCtrSlotHi_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 13),
    _NumCtrSlotHi_Type()
)
numCtrSlotHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numCtrSlotHi.setStatus("current")
_DfsStatus_Type = DisplayString
_DfsStatus_Object = MibScalar
dfsStatus = _DfsStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 14),
    _DfsStatus_Type()
)
dfsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsStatus.setStatus("current")
_DfsStatusPrimary_Type = DisplayString
_DfsStatusPrimary_Object = MibScalar
dfsStatusPrimary = _DfsStatusPrimary_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 15),
    _DfsStatusPrimary_Type()
)
dfsStatusPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsStatusPrimary.setStatus("current")
_DfsStatusAlt1_Type = DisplayString
_DfsStatusAlt1_Object = MibScalar
dfsStatusAlt1 = _DfsStatusAlt1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 16),
    _DfsStatusAlt1_Type()
)
dfsStatusAlt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsStatusAlt1.setStatus("current")
_DfsStatusAlt2_Type = DisplayString
_DfsStatusAlt2_Object = MibScalar
dfsStatusAlt2 = _DfsStatusAlt2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 17),
    _DfsStatusAlt2_Type()
)
dfsStatusAlt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsStatusAlt2.setStatus("current")
_MaxRegSMCount_Type = Integer32
_MaxRegSMCount_Object = MibScalar
maxRegSMCount = _MaxRegSMCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 18),
    _MaxRegSMCount_Type()
)
maxRegSMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxRegSMCount.setStatus("current")
_SystemTime_Type = DisplayString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 19),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_LastNTPTime_Type = DisplayString
_LastNTPTime_Object = MibScalar
lastNTPTime = _LastNTPTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 20),
    _LastNTPTime_Type()
)
lastNTPTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastNTPTime.setStatus("current")
_RegulatoryStatus_Type = DisplayString
_RegulatoryStatus_Object = MibScalar
regulatoryStatus = _RegulatoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 21),
    _RegulatoryStatus_Type()
)
regulatoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regulatoryStatus.setStatus("current")
_DhcpRlyAgntStat_reqRecvd_Type = Counter32
_DhcpRlyAgntStat_reqRecvd_Object = MibScalar
dhcpRlyAgntStat_reqRecvd = _DhcpRlyAgntStat_reqRecvd_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 22),
    _DhcpRlyAgntStat_reqRecvd_Type()
)
dhcpRlyAgntStat_reqRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRlyAgntStat_reqRecvd.setStatus("current")
_DhcpRlyAgntStat_reqRelayed_Type = Counter32
_DhcpRlyAgntStat_reqRelayed_Object = MibScalar
dhcpRlyAgntStat_reqRelayed = _DhcpRlyAgntStat_reqRelayed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 23),
    _DhcpRlyAgntStat_reqRelayed_Type()
)
dhcpRlyAgntStat_reqRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRlyAgntStat_reqRelayed.setStatus("current")
_DhcpRlyAgntStat_reqDiscards_Type = Counter32
_DhcpRlyAgntStat_reqDiscards_Object = MibScalar
dhcpRlyAgntStat_reqDiscards = _DhcpRlyAgntStat_reqDiscards_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 24),
    _DhcpRlyAgntStat_reqDiscards_Type()
)
dhcpRlyAgntStat_reqDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRlyAgntStat_reqDiscards.setStatus("current")
_DhcpRlyAgntStat_respRecvd_Type = Counter32
_DhcpRlyAgntStat_respRecvd_Object = MibScalar
dhcpRlyAgntStat_respRecvd = _DhcpRlyAgntStat_respRecvd_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 25),
    _DhcpRlyAgntStat_respRecvd_Type()
)
dhcpRlyAgntStat_respRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRlyAgntStat_respRecvd.setStatus("current")
_DhcpRlyAgntStat_respRelayed_Type = Counter32
_DhcpRlyAgntStat_respRelayed_Object = MibScalar
dhcpRlyAgntStat_respRelayed = _DhcpRlyAgntStat_respRelayed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 26),
    _DhcpRlyAgntStat_respRelayed_Type()
)
dhcpRlyAgntStat_respRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRlyAgntStat_respRelayed.setStatus("current")
_DhcpRlyAgntStat_respDiscards_Type = Counter32
_DhcpRlyAgntStat_respDiscards_Object = MibScalar
dhcpRlyAgntStat_respDiscards = _DhcpRlyAgntStat_respDiscards_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 27),
    _DhcpRlyAgntStat_respDiscards_Type()
)
dhcpRlyAgntStat_respDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRlyAgntStat_respDiscards.setStatus("current")
_DhcpRlyAgntStat_untrustedDiscards_Type = Counter32
_DhcpRlyAgntStat_untrustedDiscards_Object = MibScalar
dhcpRlyAgntStat_untrustedDiscards = _DhcpRlyAgntStat_untrustedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 28),
    _DhcpRlyAgntStat_untrustedDiscards_Type()
)
dhcpRlyAgntStat_untrustedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRlyAgntStat_untrustedDiscards.setStatus("current")
_DhcpRlyAgntStat_maxHopDiscards_Type = Counter32
_DhcpRlyAgntStat_maxHopDiscards_Object = MibScalar
dhcpRlyAgntStat_maxHopDiscards = _DhcpRlyAgntStat_maxHopDiscards_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 29),
    _DhcpRlyAgntStat_maxHopDiscards_Type()
)
dhcpRlyAgntStat_maxHopDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRlyAgntStat_maxHopDiscards.setStatus("current")
_DhcpRlyAgntStat_pktTooBig_Type = Counter32
_DhcpRlyAgntStat_pktTooBig_Object = MibScalar
dhcpRlyAgntStat_pktTooBig = _DhcpRlyAgntStat_pktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 30),
    _DhcpRlyAgntStat_pktTooBig_Type()
)
dhcpRlyAgntStat_pktTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRlyAgntStat_pktTooBig.setStatus("current")
_DhcpRlyAgntStat_invalidGiaddrDiscards_Type = Counter32
_DhcpRlyAgntStat_invalidGiaddrDiscards_Object = MibScalar
dhcpRlyAgntStat_invalidGiaddrDiscards = _DhcpRlyAgntStat_invalidGiaddrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 31),
    _DhcpRlyAgntStat_invalidGiaddrDiscards_Type()
)
dhcpRlyAgntStat_invalidGiaddrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRlyAgntStat_invalidGiaddrDiscards.setStatus("current")
_RegFailureCount_Type = Counter32
_RegFailureCount_Object = MibScalar
regFailureCount = _RegFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 32),
    _RegFailureCount_Type()
)
regFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regFailureCount.setStatus("current")
_NtpLogSNMP_Type = EventString
_NtpLogSNMP_Object = MibScalar
ntpLogSNMP = _NtpLogSNMP_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 33),
    _NtpLogSNMP_Type()
)
ntpLogSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpLogSNMP.setStatus("current")
_UGPSPowerStatus_Type = DisplayString
_UGPSPowerStatus_Object = MibScalar
uGPSPowerStatus = _UGPSPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 34),
    _UGPSPowerStatus_Type()
)
uGPSPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uGPSPowerStatus.setStatus("current")


class _RfOutDiscardRate_Type(Integer32):
    """Custom type rfOutDiscardRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RfOutDiscardRate_Type.__name__ = "Integer32"
_RfOutDiscardRate_Object = MibScalar
rfOutDiscardRate = _RfOutDiscardRate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 35),
    _RfOutDiscardRate_Type()
)
rfOutDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOutDiscardRate.setStatus("current")
_AutoUpdateGlobalStatus_Type = Integer32
_AutoUpdateGlobalStatus_Object = MibScalar
autoUpdateGlobalStatus = _AutoUpdateGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 36),
    _AutoUpdateGlobalStatus_Type()
)
autoUpdateGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoUpdateGlobalStatus.setStatus("current")
_CurrentRadioFreqCarrier_Type = Integer32
_CurrentRadioFreqCarrier_Object = MibScalar
currentRadioFreqCarrier = _CurrentRadioFreqCarrier_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 7, 37),
    _CurrentRadioFreqCarrier_Type()
)
currentRadioFreqCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentRadioFreqCarrier.setStatus("current")
_WhispFailedRegTable_Object = MibTable
whispFailedRegTable = _WhispFailedRegTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 8)
)
if mibBuilder.loadTexts:
    whispFailedRegTable.setStatus("current")
_WhispFailedRegEntry_Object = MibTableRow
whispFailedRegEntry = _WhispFailedRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 8, 1)
)
whispFailedRegEntry.setIndexNames(
    (0, "WHISP-APS-MIB", "regFailSeqNum"),
)
if mibBuilder.loadTexts:
    whispFailedRegEntry.setStatus("current")


class _RegGrantReason_Type(Integer32):
    """Custom type regGrantReason based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("reggnt-authfail", 4),
          ("reggnt-encryptfail", 5),
          ("reggnt-fail95orabove", 12),
          ("reggnt-failhivcdata", 10),
          ("reggnt-failsmlimit", 11),
          ("reggnt-failvcactive", 9),
          ("reggnt-failvcreserve", 8),
          ("reggnt-nolUIDS", 2),
          ("reggnt-novcs", 7),
          ("reggnt-outofrange", 1),
          ("reggnt-poweradjust", 6),
          ("reggnt-rerange", 3),
          ("reggnt-valid", 0))
    )


_RegGrantReason_Type.__name__ = "Integer32"
_RegGrantReason_Object = MibTableColumn
regGrantReason = _RegGrantReason_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 8, 1, 1),
    _RegGrantReason_Type()
)
regGrantReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regGrantReason.setStatus("current")
_RegFailESN_Type = PhysAddress
_RegFailESN_Object = MibTableColumn
regFailESN = _RegFailESN_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 8, 1, 2),
    _RegFailESN_Type()
)
regFailESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regFailESN.setStatus("current")
_RegFailTime_Type = TimeTicks
_RegFailTime_Object = MibTableColumn
regFailTime = _RegFailTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 8, 1, 3),
    _RegFailTime_Type()
)
regFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regFailTime.setStatus("current")
_RegFailSeqNum_Type = Counter32
_RegFailSeqNum_Object = MibTableColumn
regFailSeqNum = _RegFailSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 8, 1, 4),
    _RegFailSeqNum_Type()
)
regFailSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regFailSeqNum.setStatus("current")
_RegFailReasonText_Type = DisplayString
_RegFailReasonText_Object = MibTableColumn
regFailReasonText = _RegFailReasonText_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 8, 1, 5),
    _RegFailReasonText_Type()
)
regFailReasonText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regFailReasonText.setStatus("current")
_WhispApsDNS_ObjectIdentity = ObjectIdentity
whispApsDNS = _WhispApsDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9)
)


class _NtpDomainNameAppend_Type(Integer32):
    """Custom type ntpDomainNameAppend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("appendDomain", 1),
          ("disableDomain", 0))
    )


_NtpDomainNameAppend_Type.__name__ = "Integer32"
_NtpDomainNameAppend_Object = MibScalar
ntpDomainNameAppend = _NtpDomainNameAppend_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 1),
    _NtpDomainNameAppend_Type()
)
ntpDomainNameAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpDomainNameAppend.setStatus("current")
_NtpServer1_Type = DisplayString
_NtpServer1_Object = MibScalar
ntpServer1 = _NtpServer1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 2),
    _NtpServer1_Type()
)
ntpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServer1.setStatus("current")
_NtpServer2_Type = DisplayString
_NtpServer2_Object = MibScalar
ntpServer2 = _NtpServer2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 3),
    _NtpServer2_Type()
)
ntpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServer2.setStatus("current")
_NtpServer3_Type = DisplayString
_NtpServer3_Object = MibScalar
ntpServer3 = _NtpServer3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 4),
    _NtpServer3_Type()
)
ntpServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServer3.setStatus("current")


class _DhcprDomainNameAppend_Type(Integer32):
    """Custom type dhcprDomainNameAppend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("appendDomain", 1),
          ("disableDomain", 0))
    )


_DhcprDomainNameAppend_Type.__name__ = "Integer32"
_DhcprDomainNameAppend_Object = MibScalar
dhcprDomainNameAppend = _DhcprDomainNameAppend_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 5),
    _DhcprDomainNameAppend_Type()
)
dhcprDomainNameAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcprDomainNameAppend.setStatus("current")
_DhcprServer_Type = DisplayString
_DhcprServer_Object = MibScalar
dhcprServer = _DhcprServer_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 6),
    _DhcprServer_Type()
)
dhcprServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcprServer.setStatus("current")


class _AuthDomainNameAppend_Type(Integer32):
    """Custom type authDomainNameAppend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableDNSDomain", 0),
          ("enableDNSDomain", 1))
    )


_AuthDomainNameAppend_Type.__name__ = "Integer32"
_AuthDomainNameAppend_Object = MibScalar
authDomainNameAppend = _AuthDomainNameAppend_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 7),
    _AuthDomainNameAppend_Type()
)
authDomainNameAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authDomainNameAppend.setStatus("current")
_AuthServer1_Type = DisplayString
_AuthServer1_Object = MibScalar
authServer1 = _AuthServer1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 8),
    _AuthServer1_Type()
)
authServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authServer1.setStatus("current")
_AuthServer2_Type = DisplayString
_AuthServer2_Object = MibScalar
authServer2 = _AuthServer2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 9),
    _AuthServer2_Type()
)
authServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authServer2.setStatus("current")
_AuthServer3_Type = DisplayString
_AuthServer3_Object = MibScalar
authServer3 = _AuthServer3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 10),
    _AuthServer3_Type()
)
authServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authServer3.setStatus("current")
_AuthServer4_Type = DisplayString
_AuthServer4_Object = MibScalar
authServer4 = _AuthServer4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 11),
    _AuthServer4_Type()
)
authServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authServer4.setStatus("current")
_AuthServer5_Type = DisplayString
_AuthServer5_Object = MibScalar
authServer5 = _AuthServer5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 12),
    _AuthServer5_Type()
)
authServer5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authServer5.setStatus("current")


class _AcctDomainNameAppend_Type(Integer32):
    """Custom type acctDomainNameAppend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("appendDomain", 1),
          ("disableDomain", 0))
    )


_AcctDomainNameAppend_Type.__name__ = "Integer32"
_AcctDomainNameAppend_Object = MibScalar
acctDomainNameAppend = _AcctDomainNameAppend_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 9, 13),
    _AcctDomainNameAppend_Type()
)
acctDomainNameAppend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acctDomainNameAppend.setStatus("obsolete")
_WhispApsRFConfig_ObjectIdentity = ObjectIdentity
whispApsRFConfig = _WhispApsRFConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 10)
)
_WhispApsRFConfigRadios_Object = MibTable
whispApsRFConfigRadios = _WhispApsRFConfigRadios_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 10, 1)
)
if mibBuilder.loadTexts:
    whispApsRFConfigRadios.setStatus("current")
_WhispApsRFConfigRadioEntry_Object = MibTableRow
whispApsRFConfigRadioEntry = _WhispApsRFConfigRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    whispApsRFConfigRadioEntry.setStatus("current")


class _RadioFreqCarrier_Type(Integer32):
    """Custom type radioFreqCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("wired", 0)
    )


_RadioFreqCarrier_Type.__name__ = "Integer32"
_RadioFreqCarrier_Object = MibTableColumn
radioFreqCarrier = _RadioFreqCarrier_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 10, 1, 1, 1),
    _RadioFreqCarrier_Type()
)
radioFreqCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioFreqCarrier.setStatus("current")
if mibBuilder.loadTexts:
    radioFreqCarrier.setUnits("kHz")


class _RadioDownlinkPercent_Type(Integer32):
    """Custom type radioDownlinkPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_RadioDownlinkPercent_Type.__name__ = "Integer32"
_RadioDownlinkPercent_Object = MibTableColumn
radioDownlinkPercent = _RadioDownlinkPercent_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 10, 1, 1, 2),
    _RadioDownlinkPercent_Type()
)
radioDownlinkPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioDownlinkPercent.setStatus("current")
if mibBuilder.loadTexts:
    radioDownlinkPercent.setUnits("%")
_RadioMaxRange_Type = Integer32
_RadioMaxRange_Object = MibTableColumn
radioMaxRange = _RadioMaxRange_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 10, 1, 1, 3),
    _RadioMaxRange_Type()
)
radioMaxRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioMaxRange.setStatus("current")
if mibBuilder.loadTexts:
    radioMaxRange.setUnits("miles")
_RadioControlSlots_Type = Integer32
_RadioControlSlots_Object = MibTableColumn
radioControlSlots = _RadioControlSlots_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 10, 1, 1, 4),
    _RadioControlSlots_Type()
)
radioControlSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioControlSlots.setStatus("current")
_RadioTransmitOutputPower_Type = Integer32
_RadioTransmitOutputPower_Object = MibTableColumn
radioTransmitOutputPower = _RadioTransmitOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 10, 1, 1, 5),
    _RadioTransmitOutputPower_Type()
)
radioTransmitOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTransmitOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    radioTransmitOutputPower.setUnits("dBm")


class _RadioColorCode_Type(Integer32):
    """Custom type radioColorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_RadioColorCode_Type.__name__ = "Integer32"
_RadioColorCode_Object = MibTableColumn
radioColorCode = _RadioColorCode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 10, 1, 1, 6),
    _RadioColorCode_Type()
)
radioColorCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioColorCode.setStatus("current")
_WhispApsControls_ObjectIdentity = ObjectIdentity
whispApsControls = _WhispApsControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 11)
)
_ClearLinkTableStats_Type = Integer32
_ClearLinkTableStats_Object = MibScalar
clearLinkTableStats = _ClearLinkTableStats_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 11, 1),
    _ClearLinkTableStats_Type()
)
clearLinkTableStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearLinkTableStats.setStatus("current")
whispBoxRFPhysicalRadioEntry.registerAugmentions(
    ("WHISP-APS-MIB",
     "whispApsRFConfigRadioEntry")
)
whispApsRFConfigRadioEntry.setIndexNames(*whispBoxRFPhysicalRadioEntry.getIndexNames())

# Managed Objects groups

whispLinkTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 6, 1)
)
whispLinkTestGroup.setObjects(
      *(("WHISP-APS-MIB", "linkTestLUID"),
        ("WHISP-APS-MIB", "linkTestDuration"),
        ("WHISP-APS-MIB", "linkTestAction"),
        ("WHISP-APS-MIB", "linkTestPktLength"),
        ("WHISP-APS-MIB", "testLUID"),
        ("WHISP-APS-MIB", "linkTestStatus"),
        ("WHISP-APS-MIB", "linkTestError"),
        ("WHISP-APS-MIB", "testDuration"),
        ("WHISP-APS-MIB", "downLinkRate"),
        ("WHISP-APS-MIB", "upLinkRate"),
        ("WHISP-APS-MIB", "downLinkEff"),
        ("WHISP-APS-MIB", "maxDwnLinkIndex"),
        ("WHISP-APS-MIB", "actDwnLinkIndex"),
        ("WHISP-APS-MIB", "expDwnFragCount"),
        ("WHISP-APS-MIB", "actDwnFragCount"),
        ("WHISP-APS-MIB", "upLinkEff"),
        ("WHISP-APS-MIB", "expUpFragCount"),
        ("WHISP-APS-MIB", "actUpFragCount"),
        ("WHISP-APS-MIB", "maxUpLinkIndex"),
        ("WHISP-APS-MIB", "actUpLinkIndex"),
        ("WHISP-APS-MIB", "fragments1xDwnLinkVertical"),
        ("WHISP-APS-MIB", "fragments2xDwnLinkVertical"),
        ("WHISP-APS-MIB", "fragments3xDwnLinkVertical"),
        ("WHISP-APS-MIB", "fragments4xDwnLinkVertical"),
        ("WHISP-APS-MIB", "fragments1xUpLinkVertical"),
        ("WHISP-APS-MIB", "fragments2xUpLinkVertical"),
        ("WHISP-APS-MIB", "fragments3xUpLinkVertical"),
        ("WHISP-APS-MIB", "fragments4xUpLinkVertical"),
        ("WHISP-APS-MIB", "fragments1xDwnLinkHorizontal"),
        ("WHISP-APS-MIB", "fragments2xDwnLinkHorizontal"),
        ("WHISP-APS-MIB", "fragments3xDwnLinkHorizontal"),
        ("WHISP-APS-MIB", "fragments4xDwnLinkHorizontal"),
        ("WHISP-APS-MIB", "fragments1xUpLinkHorizontal"),
        ("WHISP-APS-MIB", "fragments2xUpLinkHorizontal"),
        ("WHISP-APS-MIB", "fragments3xUpLinkHorizontal"),
        ("WHISP-APS-MIB", "fragments4xUpLinkHorizontal"),
        ("WHISP-APS-MIB", "bitErrorsCorrected1xDwnLinkVertical"),
        ("WHISP-APS-MIB", "bitErrorsCorrected2xDwnLinkVertical"),
        ("WHISP-APS-MIB", "bitErrorsCorrected3xDwnLinkVertical"),
        ("WHISP-APS-MIB", "bitErrorsCorrected4xDwnLinkVertical"),
        ("WHISP-APS-MIB", "bitErrorsCorrected1xUpLinkVertical"),
        ("WHISP-APS-MIB", "bitErrorsCorrected2xUpLinkVertical"),
        ("WHISP-APS-MIB", "bitErrorsCorrected3xUpLinkVertical"),
        ("WHISP-APS-MIB", "bitErrorsCorrected4xUpLinkVertical"),
        ("WHISP-APS-MIB", "signalToNoiseRatioDownLinkVertical"),
        ("WHISP-APS-MIB", "signalToNoiseRatioUpLinkVertical"),
        ("WHISP-APS-MIB", "bitErrorsCorrected1xDwnLinkHorizontal"),
        ("WHISP-APS-MIB", "bitErrorsCorrected2xDwnLinkHorizontal"),
        ("WHISP-APS-MIB", "bitErrorsCorrected3xDwnLinkHorizontal"),
        ("WHISP-APS-MIB", "bitErrorsCorrected4xDwnLinkHorizontal"),
        ("WHISP-APS-MIB", "bitErrorsCorrected1xUpLinkHorizontal"),
        ("WHISP-APS-MIB", "bitErrorsCorrected2xUpLinkHorizontal"),
        ("WHISP-APS-MIB", "bitErrorsCorrected3xUpLinkHorizontal"),
        ("WHISP-APS-MIB", "bitErrorsCorrected4xUpLinkHorizontal"),
        ("WHISP-APS-MIB", "signalToNoiseRatioDownLinkHorizontal"),
        ("WHISP-APS-MIB", "signalToNoiseRatioUpLinkHorizontal"),
        ("WHISP-APS-MIB", "linkTestSNRCalculation"),
        ("WHISP-APS-MIB", "linkTestWithDualPath"),
        ("WHISP-APS-MIB", "linkTestMode"),
        ("WHISP-APS-MIB", "linkTestNumPkt"))
)
if mibBuilder.loadTexts:
    whispLinkTestGroup.setStatus("current")

whispApsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 6, 2)
)
whispApsConfigGroup.setObjects(
      *(("WHISP-APS-MIB", "gpsInput"),
        ("WHISP-APS-MIB", "rfFreqCarrier"),
        ("WHISP-APS-MIB", "dwnLnkData"),
        ("WHISP-APS-MIB", "highPriorityUpLnkPct"),
        ("WHISP-APS-MIB", "numUAckSlots"),
        ("WHISP-APS-MIB", "uAcksReservHigh"),
        ("WHISP-APS-MIB", "numDAckSlots"),
        ("WHISP-APS-MIB", "dAcksReservHigh"),
        ("WHISP-APS-MIB", "numCtlSlots"),
        ("WHISP-APS-MIB", "numCtlSlotsReserveHigh"),
        ("WHISP-APS-MIB", "upLnkMaxBurstDataRate"),
        ("WHISP-APS-MIB", "upLnkDataRate"),
        ("WHISP-APS-MIB", "upLnkLimit"),
        ("WHISP-APS-MIB", "dwnLnkMaxBurstDataRate"),
        ("WHISP-APS-MIB", "dwnLnkDataRate"),
        ("WHISP-APS-MIB", "dwnLnkLimit"),
        ("WHISP-APS-MIB", "sectorID"),
        ("WHISP-APS-MIB", "maxRange"),
        ("WHISP-APS-MIB", "asIP1"),
        ("WHISP-APS-MIB", "asIP2"),
        ("WHISP-APS-MIB", "asIP3"),
        ("WHISP-APS-MIB", "asIP4"),
        ("WHISP-APS-MIB", "asIP5"),
        ("WHISP-APS-MIB", "lanIpAp"),
        ("WHISP-APS-MIB", "lanMaskAp"),
        ("WHISP-APS-MIB", "defaultGwAp"),
        ("WHISP-APS-MIB", "privateIp"),
        ("WHISP-APS-MIB", "gpsTrap"),
        ("WHISP-APS-MIB", "regTrap"),
        ("WHISP-APS-MIB", "txSpreading"),
        ("WHISP-APS-MIB", "apBeaconInfo"),
        ("WHISP-APS-MIB", "authMode"),
        ("WHISP-APS-MIB", "authKeyAp"),
        ("WHISP-APS-MIB", "authKeyOptionAP"),
        ("WHISP-APS-MIB", "encryptionMode"),
        ("WHISP-APS-MIB", "ntpServerIp"),
        ("WHISP-APS-MIB", "multicastRetryCount"),
        ("WHISP-APS-MIB", "encryptDwBroadcast"),
        ("WHISP-APS-MIB", "updateAppAddress"),
        ("WHISP-APS-MIB", "dfsConfig"),
        ("WHISP-APS-MIB", "vlanEnable"),
        ("WHISP-APS-MIB", "configSource"),
        ("WHISP-APS-MIB", "apRateAdapt"),
        ("WHISP-APS-MIB", "numCtlSlotsHW"),
        ("WHISP-APS-MIB", "displayAPEval"),
        ("WHISP-APS-MIB", "smIsolation"),
        ("WHISP-APS-MIB", "bridgeFloodUnknownsEnable"),
        ("WHISP-APS-MIB", "ipAccessFilterEnable"),
        ("WHISP-APS-MIB", "allowedIPAccess1"),
        ("WHISP-APS-MIB", "allowedIPAccess2"),
        ("WHISP-APS-MIB", "allowedIPAccess3"),
        ("WHISP-APS-MIB", "allowedIPAccessNMLength1"),
        ("WHISP-APS-MIB", "allowedIPAccessNMLength2"),
        ("WHISP-APS-MIB", "allowedIPAccessNMLength3"),
        ("WHISP-APS-MIB", "rfTelnetAccess"),
        ("WHISP-APS-MIB", "rfPPPoEPADIForwarding"),
        ("WHISP-APS-MIB", "tslBridging"),
        ("WHISP-APS-MIB", "untranslatedArp"),
        ("WHISP-APS-MIB", "limitFreqBand900"),
        ("WHISP-APS-MIB", "txPwrLevel"),
        ("WHISP-APS-MIB", "rfFreqCaralt1"),
        ("WHISP-APS-MIB", "rfFreqCaralt2"),
        ("WHISP-APS-MIB", "scheduleWhitening"),
        ("WHISP-APS-MIB", "remoteSpectrumAnalysisDuration"),
        ("WHISP-APS-MIB", "remoteSpectrumAnalyzerLUID"),
        ("WHISP-APS-MIB", "bhReReg"),
        ("WHISP-APS-MIB", "dlnkBcastCIR"),
        ("WHISP-APS-MIB", "dlnkMcastCIR"),
        ("WHISP-APS-MIB", "verifyGPSChecksum"),
        ("WHISP-APS-MIB", "qinqEthType"),
        ("WHISP-APS-MIB", "multicastVCDataRate"),
        ("WHISP-APS-MIB", "colorCodeRescanTimer"),
        ("WHISP-APS-MIB", "colorCodeRescanIdleTimer"),
        ("WHISP-APS-MIB", "fskSMTxPwrCntl"),
        ("WHISP-APS-MIB", "fskSMRcvTargetLvl"),
        ("WHISP-APS-MIB", "berModSelect"),
        ("WHISP-APS-MIB", "lastSesStatsReset"),
        ("WHISP-APS-MIB", "resetSesStats"),
        ("WHISP-APS-MIB", "syslogDomainNameAppend"),
        ("WHISP-APS-MIB", "syslogServerAddr"),
        ("WHISP-APS-MIB", "syslogServerPort"),
        ("WHISP-APS-MIB", "syslogXmitAP"),
        ("WHISP-APS-MIB", "syslogXmitSMs"),
        ("WHISP-APS-MIB", "uGPSPower"),
        ("WHISP-APS-MIB", "gpsOutputEn"),
        ("WHISP-APS-MIB", "radioMode"),
        ("WHISP-APS-MIB", "authSharedSecret1"),
        ("WHISP-APS-MIB", "authSharedSecret2"),
        ("WHISP-APS-MIB", "authSharedSecret3"),
        ("WHISP-APS-MIB", "radiusPort"),
        ("WHISP-APS-MIB", "radiusAcctPort"),
        ("WHISP-APS-MIB", "rfOLEnable"),
        ("WHISP-APS-MIB", "rfOLTrap"),
        ("WHISP-APS-MIB", "rfOLThreshold"),
        ("WHISP-APS-MIB", "remoteSpectrumAnalyzerScanBandwidth"),
        ("WHISP-APS-MIB", "apConfigAdjacentChanSupport"),
        ("WHISP-APS-MIB", "ofdmSMRcvTargetLvl"),
        ("WHISP-APS-MIB", "apRxDelay"),
        ("WHISP-APS-MIB", "apVlanOverride"),
        ("WHISP-APS-MIB", "dhcpRelayAgentEnable"),
        ("WHISP-APS-MIB", "dhcpRelayAgentSrvrIP"),
        ("WHISP-APS-MIB", "onlyAllowVer95OrAbove"),
        ("WHISP-APS-MIB", "whispWebUseAuthServer"),
        ("WHISP-APS-MIB", "whispUsrAuthSharedSecret1"),
        ("WHISP-APS-MIB", "whispUsrAuthSharedSecret2"),
        ("WHISP-APS-MIB", "whispUsrAuthSharedSecret3"),
        ("WHISP-APS-MIB", "whispUsrAcctSvr1"),
        ("WHISP-APS-MIB", "whispUsrAcctSvr2"),
        ("WHISP-APS-MIB", "whispUsrAcctSvr3"),
        ("WHISP-APS-MIB", "whispUsrAuthPhase1"),
        ("WHISP-APS-MIB", "accountingInterimUpdateInterval"),
        ("WHISP-APS-MIB", "accountingSmReAuthInterval"),
        ("WHISP-APS-MIB", "dropSession"),
        ("WHISP-APS-MIB", "timeZone"),
        ("WHISP-APS-MIB", "actionListFilename"),
        ("WHISP-APS-MIB", "enableAutoupdate"))
)
if mibBuilder.loadTexts:
    whispApsConfigGroup.setStatus("current")

whispApsLinkTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 6, 3)
)
whispApsLinkTableGroup.setObjects(
      *(("WHISP-APS-MIB", "linkLUID"),
        ("WHISP-APS-MIB", "linkDescr"),
        ("WHISP-APS-MIB", "linkPhysAddress"),
        ("WHISP-APS-MIB", "linkManagementIP"),
        ("WHISP-APS-MIB", "linkFragmentsReceived1XVertical"),
        ("WHISP-APS-MIB", "linkFragmentsReceived2XVertical"),
        ("WHISP-APS-MIB", "linkFragmentsReceived3XVertical"),
        ("WHISP-APS-MIB", "linkFragmentsReceived4XVertical"),
        ("WHISP-APS-MIB", "signalToNoiseRatioVertical"),
        ("WHISP-APS-MIB", "linkFragmentsReceived1XHorizontal"),
        ("WHISP-APS-MIB", "linkFragmentsReceived2XHorizontal"),
        ("WHISP-APS-MIB", "linkFragmentsReceived3XHorizontal"),
        ("WHISP-APS-MIB", "linkFragmentsReceived4XHorizontal"),
        ("WHISP-APS-MIB", "signalToNoiseRatioHorizontal"),
        ("WHISP-APS-MIB", "linkSignalStrengthRatio"),
        ("WHISP-APS-MIB", "linkRadioDbmHorizontal"),
        ("WHISP-APS-MIB", "linkRadioDbmVertical"),
        ("WHISP-APS-MIB", "maxSMTxPwr"),
        ("WHISP-APS-MIB", "productType"),
        ("WHISP-APS-MIB", "linkAdaptRateLowPri"),
        ("WHISP-APS-MIB", "linkAdaptRateHighPri"),
        ("WHISP-APS-MIB", "autoUpdateStatus"),
        ("WHISP-APS-MIB", "linkMtu"),
        ("WHISP-APS-MIB", "linkSpeed"),
        ("WHISP-APS-MIB", "linkOperStatus"),
        ("WHISP-APS-MIB", "linkInOctets"),
        ("WHISP-APS-MIB", "linkInUcastPkts"),
        ("WHISP-APS-MIB", "linkInNUcastPkts"),
        ("WHISP-APS-MIB", "linkInDiscards"),
        ("WHISP-APS-MIB", "linkInError"),
        ("WHISP-APS-MIB", "linkInUnknownProtos"),
        ("WHISP-APS-MIB", "linkOutOctets"),
        ("WHISP-APS-MIB", "linkOutUcastPkts"),
        ("WHISP-APS-MIB", "linkOutNUcastPkts"),
        ("WHISP-APS-MIB", "linkOutDiscards"),
        ("WHISP-APS-MIB", "linkOutError"),
        ("WHISP-APS-MIB", "linkOutQLen"),
        ("WHISP-APS-MIB", "linkSessState"),
        ("WHISP-APS-MIB", "linkESN"),
        ("WHISP-APS-MIB", "linkRSSI"),
        ("WHISP-APS-MIB", "linkAveJitter"),
        ("WHISP-APS-MIB", "linkLastJitter"),
        ("WHISP-APS-MIB", "linkAirDelay"),
        ("WHISP-APS-MIB", "linkRegCount"),
        ("WHISP-APS-MIB", "linkReRegCount"),
        ("WHISP-APS-MIB", "linkTimeOut"),
        ("WHISP-APS-MIB", "linkLastRSSI"),
        ("WHISP-APS-MIB", "sessionCount"),
        ("WHISP-APS-MIB", "softwareVersion"),
        ("WHISP-APS-MIB", "softwareBootVersion"),
        ("WHISP-APS-MIB", "fpgaVersion"),
        ("WHISP-APS-MIB", "linkSiteName"),
        ("WHISP-APS-MIB", "avgPowerLevel"),
        ("WHISP-APS-MIB", "lastPowerLevel"),
        ("WHISP-APS-MIB", "sesDownLinkRate"),
        ("WHISP-APS-MIB", "sesDownLinkLimit"),
        ("WHISP-APS-MIB", "sesUpLinkRate"),
        ("WHISP-APS-MIB", "sesUpLinkLimit"),
        ("WHISP-APS-MIB", "adaptRate"),
        ("WHISP-APS-MIB", "sesLoUpCIR"),
        ("WHISP-APS-MIB", "sesLoDownCIR"),
        ("WHISP-APS-MIB", "sesHiUpCIR"),
        ("WHISP-APS-MIB", "sesHiDownCIR"),
        ("WHISP-APS-MIB", "platformVer"),
        ("WHISP-APS-MIB", "smSessionTmr"),
        ("WHISP-APS-MIB", "smSessionSeqNumMismatch"),
        ("WHISP-APS-MIB", "dataVCNum"),
        ("WHISP-APS-MIB", "hiPriQEn"),
        ("WHISP-APS-MIB", "dataVCNumHiQ"),
        ("WHISP-APS-MIB", "linkInOctetsHiQ"),
        ("WHISP-APS-MIB", "linkInUcastPktsHiQ"),
        ("WHISP-APS-MIB", "linkInNUcastPktsHiQ"),
        ("WHISP-APS-MIB", "linkInDiscardsHiQ"),
        ("WHISP-APS-MIB", "linkInErrorHiQ"),
        ("WHISP-APS-MIB", "linkInUnknownProtosHiQ"),
        ("WHISP-APS-MIB", "linkOutOctetsHiQ"),
        ("WHISP-APS-MIB", "linkOutUcastPktsHiQ"),
        ("WHISP-APS-MIB", "linkOutNUcastPktsHiQ"),
        ("WHISP-APS-MIB", "linkOutDiscardsHiQ"),
        ("WHISP-APS-MIB", "linkOutErrorHiQ"),
        ("WHISP-APS-MIB", "vcQOverflow"),
        ("WHISP-APS-MIB", "vcQOverflowHiQ"),
        ("WHISP-APS-MIB", "p7p8HiPriQEn"),
        ("WHISP-APS-MIB", "p7p8HiPriQ"),
        ("WHISP-APS-MIB", "linkAirDelayns"),
        ("WHISP-APS-MIB", "linkQualityAPData"),
        ("WHISP-APS-MIB", "radiusReplyMsg"),
        ("WHISP-APS-MIB", "radiusFramedIPAddress"),
        ("WHISP-APS-MIB", "radiusFramedIPNetmask"),
        ("WHISP-APS-MIB", "radiusDefaultGateway"))
)
if mibBuilder.loadTexts:
    whispApsLinkTableGroup.setStatus("current")

whispApsFailedRegTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 6, 5)
)
whispApsFailedRegTableGroup.setObjects(
      *(("WHISP-APS-MIB", "regGrantReason"),
        ("WHISP-APS-MIB", "regFailESN"),
        ("WHISP-APS-MIB", "regFailTime"),
        ("WHISP-APS-MIB", "regFailSeqNum"),
        ("WHISP-APS-MIB", "regFailReasonText"))
)
if mibBuilder.loadTexts:
    whispApsFailedRegTableGroup.setStatus("current")


# Notification objects

whispRegComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 1, 1)
)
whispRegComplete.setObjects(
      *(("WHISP-APS-MIB", "linkLUID"),
        ("WHISP-APS-MIB", "linkPhysAddress"))
)
if mibBuilder.loadTexts:
    whispRegComplete.setStatus(
        "current"
    )

whispRegLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 1, 2)
)
whispRegLost.setObjects(
      *(("WHISP-APS-MIB", "linkLUID"),
        ("WHISP-APS-MIB", "linkPhysAddress"))
)
if mibBuilder.loadTexts:
    whispRegLost.setStatus(
        "current"
    )

whispRegFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 1, 3)
)
whispRegFailure.setObjects(
      *(("WHISP-APS-MIB", "regFailESN"),
        ("WHISP-APS-MIB", "regGrantReason"))
)
if mibBuilder.loadTexts:
    whispRegFailure.setStatus(
        "current"
    )

whispDefKeyUsed = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 1, 4)
)
whispDefKeyUsed.setObjects(
      *(("WHISP-APS-MIB", "linkLUID"),
        ("WHISP-APS-MIB", "linkPhysAddress"))
)
if mibBuilder.loadTexts:
    whispDefKeyUsed.setStatus(
        "current"
    )

whispGPSInSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 2, 1)
)
whispGPSInSync.setObjects(
      *(("WHISP-APS-MIB", "whispGPSStats"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    whispGPSInSync.setStatus(
        "current"
    )

whispGPSOutSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 2, 2)
)
whispGPSOutSync.setObjects(
      *(("WHISP-APS-MIB", "gpsStatus"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    whispGPSOutSync.setStatus(
        "current"
    )

whispRadarDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 3, 1)
)
whispRadarDetected.setObjects(
      *(("WHISP-APS-MIB", "dfsStatus"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    whispRadarDetected.setStatus(
        "current"
    )

whispRadarEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 3, 2)
)
whispRadarEnd.setObjects(
      *(("WHISP-APS-MIB", "dfsStatus"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    whispRadarEnd.setStatus(
        "current"
    )

regulatoryApCheckInvalidChanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 4, 1)
)
regulatoryApCheckInvalidChanFailed.setObjects(
      *(("WHISP-APS-MIB", "regulatoryStatus"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    regulatoryApCheckInvalidChanFailed.setStatus(
        "current"
    )

regulatoryCheckFailedNoRegionAp = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 4, 2)
)
regulatoryCheckFailedNoRegionAp.setObjects(
    ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn")
)
if mibBuilder.loadTexts:
    regulatoryCheckFailedNoRegionAp.setStatus(
        "current"
    )

regulatoryApCheckInvalidChBwFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 4, 3)
)
regulatoryApCheckInvalidChBwFailed.setObjects(
      *(("WHISP-APS-MIB", "regulatoryStatus"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    regulatoryApCheckInvalidChBwFailed.setStatus(
        "current"
    )

rfLinkOverloadCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 5, 5, 1)
)
rfLinkOverloadCondition.setObjects(
      *(("WHISP-APS-MIB", "rfOutDiscardRate"),
        ("WHISP-BOX-MIBV2-MIB", "whispBoxEsn"))
)
if mibBuilder.loadTexts:
    rfLinkOverloadCondition.setStatus(
        "current"
    )


# Notifications groups

whispApsNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 1, 6, 4)
)
whispApsNotifGroup.setObjects(
      *(("WHISP-APS-MIB", "whispRegComplete"),
        ("WHISP-APS-MIB", "whispRegLost"),
        ("WHISP-APS-MIB", "whispRegFailure"),
        ("WHISP-APS-MIB", "whispDefKeyUsed"),
        ("WHISP-APS-MIB", "whispGPSInSync"),
        ("WHISP-APS-MIB", "whispGPSOutSync"),
        ("WHISP-APS-MIB", "whispRadarDetected"),
        ("WHISP-APS-MIB", "whispRadarEnd"),
        ("WHISP-APS-MIB", "regulatoryApCheckInvalidChanFailed"),
        ("WHISP-APS-MIB", "regulatoryCheckFailedNoRegionAp"),
        ("WHISP-APS-MIB", "regulatoryApCheckInvalidChBwFailed"),
        ("WHISP-APS-MIB", "rfLinkOverloadCondition"))
)
if mibBuilder.loadTexts:
    whispApsNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WHISP-APS-MIB",
    **{"whispApsMibModule": whispApsMibModule,
       "whispApsConfig": whispApsConfig,
       "gpsInput": gpsInput,
       "rfFreqCarrier": rfFreqCarrier,
       "apLinkSpeed": apLinkSpeed,
       "dwnLnkData": dwnLnkData,
       "highPriorityUpLnkPct": highPriorityUpLnkPct,
       "numUAckSlots": numUAckSlots,
       "uAcksReservHigh": uAcksReservHigh,
       "numDAckSlots": numDAckSlots,
       "dAcksReservHigh": dAcksReservHigh,
       "numCtlSlots": numCtlSlots,
       "numCtlSlotsReserveHigh": numCtlSlotsReserveHigh,
       "upLnkDataRate": upLnkDataRate,
       "upLnkLimit": upLnkLimit,
       "dwnLnkDataRate": dwnLnkDataRate,
       "dwnLnkLimit": dwnLnkLimit,
       "sectorID": sectorID,
       "maxRange": maxRange,
       "airLinkSecurity": airLinkSecurity,
       "berMode": berMode,
       "asIP1": asIP1,
       "asIP2": asIP2,
       "asIP3": asIP3,
       "lanIpAp": lanIpAp,
       "lanMaskAp": lanMaskAp,
       "defaultGwAp": defaultGwAp,
       "privateIp": privateIp,
       "gpsTrap": gpsTrap,
       "regTrap": regTrap,
       "txSpreading": txSpreading,
       "apBeaconInfo": apBeaconInfo,
       "authMode": authMode,
       "authKeyAp": authKeyAp,
       "encryptionMode": encryptionMode,
       "ntpServerIp": ntpServerIp,
       "broadcastRetryCount": broadcastRetryCount,
       "encryptDwBroadcast": encryptDwBroadcast,
       "updateAppAddress": updateAppAddress,
       "dfsConfig": dfsConfig,
       "vlanEnable": vlanEnable,
       "configSource": configSource,
       "apRateAdapt": apRateAdapt,
       "numCtlSlotsHW": numCtlSlotsHW,
       "displayAPEval": displayAPEval,
       "smIsolation": smIsolation,
       "ipAccessFilterEnable": ipAccessFilterEnable,
       "allowedIPAccess1": allowedIPAccess1,
       "allowedIPAccess2": allowedIPAccess2,
       "allowedIPAccess3": allowedIPAccess3,
       "tslBridging": tslBridging,
       "untranslatedArp": untranslatedArp,
       "limitFreqBand900": limitFreqBand900,
       "txPwrLevel": txPwrLevel,
       "rfFreqCaralt1": rfFreqCaralt1,
       "rfFreqCaralt2": rfFreqCaralt2,
       "scheduleWhitening": scheduleWhitening,
       "remoteSpectrumAnalysisDuration": remoteSpectrumAnalysisDuration,
       "remoteSpectrumAnalyzerLUID": remoteSpectrumAnalyzerLUID,
       "bhReReg": bhReReg,
       "dlnkBcastCIR": dlnkBcastCIR,
       "verifyGPSChecksum": verifyGPSChecksum,
       "apVlanOverride": apVlanOverride,
       "dhcpRelayAgentEnable": dhcpRelayAgentEnable,
       "dhcpRelayAgentSrvrIP": dhcpRelayAgentSrvrIP,
       "colorCodeRescanTimer": colorCodeRescanTimer,
       "colorCodeRescanIdleTimer": colorCodeRescanIdleTimer,
       "authKeyOptionAP": authKeyOptionAP,
       "asIP4": asIP4,
       "asIP5": asIP5,
       "onlyAllowVer95OrAbove": onlyAllowVer95OrAbove,
       "apRxDelay": apRxDelay,
       "qinqEthType": qinqEthType,
       "fskSMTxPwrCntl": fskSMTxPwrCntl,
       "fskSMRcvTargetLvl": fskSMRcvTargetLvl,
       "authSharedSecret1": authSharedSecret1,
       "authSharedSecret2": authSharedSecret2,
       "authSharedSecret3": authSharedSecret3,
       "whispUsrAuthSharedSecret1": whispUsrAuthSharedSecret1,
       "whispUsrAuthSharedSecret2": whispUsrAuthSharedSecret2,
       "whispUsrAuthSharedSecret3": whispUsrAuthSharedSecret3,
       "whispUsrAcctSvr1": whispUsrAcctSvr1,
       "whispUsrAcctSvr2": whispUsrAcctSvr2,
       "whispUsrAcctSvr3": whispUsrAcctSvr3,
       "whispUsrAuthPhase1": whispUsrAuthPhase1,
       "whispWebUseAuthServer": whispWebUseAuthServer,
       "dropSession": dropSession,
       "uGPSPower": uGPSPower,
       "timeZone": timeZone,
       "ofdmSMRcvTargetLvl": ofdmSMRcvTargetLvl,
       "radiusPort": radiusPort,
       "radiusAcctPort": radiusAcctPort,
       "lastSesStatsReset": lastSesStatsReset,
       "resetSesStats": resetSesStats,
       "rfOLTrap": rfOLTrap,
       "rfOLThreshold": rfOLThreshold,
       "rfOLEnable": rfOLEnable,
       "actionListFilename": actionListFilename,
       "enableAutoupdate": enableAutoupdate,
       "accountingSmReAuthInterval": accountingSmReAuthInterval,
       "syslogDomainNameAppend": syslogDomainNameAppend,
       "syslogServerAddr": syslogServerAddr,
       "syslogServerPort": syslogServerPort,
       "syslogXmitAP": syslogXmitAP,
       "syslogXmitSMs": syslogXmitSMs,
       "accountingInterimUpdateInterval": accountingInterimUpdateInterval,
       "gpsOutputEn": gpsOutputEn,
       "radioMode": radioMode,
       "rfTelnetAccess": rfTelnetAccess,
       "upLnkMaxBurstDataRate": upLnkMaxBurstDataRate,
       "dwnLnkMaxBurstDataRate": dwnLnkMaxBurstDataRate,
       "rfPPPoEPADIForwarding": rfPPPoEPADIForwarding,
       "allowedIPAccessNMLength1": allowedIPAccessNMLength1,
       "allowedIPAccessNMLength2": allowedIPAccessNMLength2,
       "allowedIPAccessNMLength3": allowedIPAccessNMLength3,
       "bridgeFloodUnknownsEnable": bridgeFloodUnknownsEnable,
       "berModSelect": berModSelect,
       "remoteSpectrumAnalyzerScanBandwidth": remoteSpectrumAnalyzerScanBandwidth,
       "multicastVCDataRate": multicastVCDataRate,
       "dlnkMcastCIR": dlnkMcastCIR,
       "multicastRetryCount": multicastRetryCount,
       "apConfigAdjacentChanSupport": apConfigAdjacentChanSupport,
       "whispApsLink": whispApsLink,
       "whispApsLinkTestConfig": whispApsLinkTestConfig,
       "linkTestLUID": linkTestLUID,
       "linkTestDuration": linkTestDuration,
       "linkTestAction": linkTestAction,
       "linkTestPktLength": linkTestPktLength,
       "linkTestMode": linkTestMode,
       "linkTestSNRCalculation": linkTestSNRCalculation,
       "linkTestWithDualPath": linkTestWithDualPath,
       "linkTestNumPkt": linkTestNumPkt,
       "whispApsLinkTestResult": whispApsLinkTestResult,
       "testLUID": testLUID,
       "linkTestStatus": linkTestStatus,
       "linkTestError": linkTestError,
       "testDuration": testDuration,
       "downLinkRate": downLinkRate,
       "upLinkRate": upLinkRate,
       "downLinkEff": downLinkEff,
       "maxDwnLinkIndex": maxDwnLinkIndex,
       "actDwnLinkIndex": actDwnLinkIndex,
       "expDwnFragCount": expDwnFragCount,
       "actDwnFragCount": actDwnFragCount,
       "upLinkEff": upLinkEff,
       "expUpFragCount": expUpFragCount,
       "actUpFragCount": actUpFragCount,
       "maxUpLinkIndex": maxUpLinkIndex,
       "actUpLinkIndex": actUpLinkIndex,
       "fragments1xDwnLinkVertical": fragments1xDwnLinkVertical,
       "fragments2xDwnLinkVertical": fragments2xDwnLinkVertical,
       "fragments3xDwnLinkVertical": fragments3xDwnLinkVertical,
       "fragments4xDwnLinkVertical": fragments4xDwnLinkVertical,
       "fragments1xUpLinkVertical": fragments1xUpLinkVertical,
       "fragments2xUpLinkVertical": fragments2xUpLinkVertical,
       "fragments3xUpLinkVertical": fragments3xUpLinkVertical,
       "fragments4xUpLinkVertical": fragments4xUpLinkVertical,
       "bitErrorsCorrected1xDwnLinkVertical": bitErrorsCorrected1xDwnLinkVertical,
       "bitErrorsCorrected2xDwnLinkVertical": bitErrorsCorrected2xDwnLinkVertical,
       "bitErrorsCorrected3xDwnLinkVertical": bitErrorsCorrected3xDwnLinkVertical,
       "bitErrorsCorrected4xDwnLinkVertical": bitErrorsCorrected4xDwnLinkVertical,
       "bitErrorsCorrected1xUpLinkVertical": bitErrorsCorrected1xUpLinkVertical,
       "bitErrorsCorrected2xUpLinkVertical": bitErrorsCorrected2xUpLinkVertical,
       "bitErrorsCorrected3xUpLinkVertical": bitErrorsCorrected3xUpLinkVertical,
       "bitErrorsCorrected4xUpLinkVertical": bitErrorsCorrected4xUpLinkVertical,
       "signalToNoiseRatioDownLinkVertical": signalToNoiseRatioDownLinkVertical,
       "signalToNoiseRatioUpLinkVertical": signalToNoiseRatioUpLinkVertical,
       "fragments1xDwnLinkHorizontal": fragments1xDwnLinkHorizontal,
       "fragments2xDwnLinkHorizontal": fragments2xDwnLinkHorizontal,
       "fragments3xDwnLinkHorizontal": fragments3xDwnLinkHorizontal,
       "fragments4xDwnLinkHorizontal": fragments4xDwnLinkHorizontal,
       "fragments1xUpLinkHorizontal": fragments1xUpLinkHorizontal,
       "fragments2xUpLinkHorizontal": fragments2xUpLinkHorizontal,
       "fragments3xUpLinkHorizontal": fragments3xUpLinkHorizontal,
       "fragments4xUpLinkHorizontal": fragments4xUpLinkHorizontal,
       "bitErrorsCorrected1xDwnLinkHorizontal": bitErrorsCorrected1xDwnLinkHorizontal,
       "bitErrorsCorrected2xDwnLinkHorizontal": bitErrorsCorrected2xDwnLinkHorizontal,
       "bitErrorsCorrected3xDwnLinkHorizontal": bitErrorsCorrected3xDwnLinkHorizontal,
       "bitErrorsCorrected4xDwnLinkHorizontal": bitErrorsCorrected4xDwnLinkHorizontal,
       "bitErrorsCorrected1xUpLinkHorizontal": bitErrorsCorrected1xUpLinkHorizontal,
       "bitErrorsCorrected2xUpLinkHorizontal": bitErrorsCorrected2xUpLinkHorizontal,
       "bitErrorsCorrected3xUpLinkHorizontal": bitErrorsCorrected3xUpLinkHorizontal,
       "bitErrorsCorrected4xUpLinkHorizontal": bitErrorsCorrected4xUpLinkHorizontal,
       "signalToNoiseRatioDownLinkHorizontal": signalToNoiseRatioDownLinkHorizontal,
       "signalToNoiseRatioUpLinkHorizontal": signalToNoiseRatioUpLinkHorizontal,
       "whispRegStatus": whispRegStatus,
       "whispApsGPS": whispApsGPS,
       "whispGPSStats": whispGPSStats,
       "gpsSyncSource": gpsSyncSource,
       "gpsSyncStatus": gpsSyncStatus,
       "gpsTrackingMode": gpsTrackingMode,
       "gpsTime": gpsTime,
       "gpsDate": gpsDate,
       "gpsSatellitesTracked": gpsSatellitesTracked,
       "gpsSatellitesVisible": gpsSatellitesVisible,
       "gpsHeight": gpsHeight,
       "gpsAntennaConnection": gpsAntennaConnection,
       "gpsLatitude": gpsLatitude,
       "gpsLongitude": gpsLongitude,
       "gpsInvalidMsg": gpsInvalidMsg,
       "gpsRestartCount": gpsRestartCount,
       "gpsReInitCount": gpsReInitCount,
       "gpsReceiverInfo": gpsReceiverInfo,
       "gpsFreeRun": gpsFreeRun,
       "autoSyncStatus": autoSyncStatus,
       "whispLinkTable": whispLinkTable,
       "whispLinkEntry": whispLinkEntry,
       "linkLUID": linkLUID,
       "linkDescr": linkDescr,
       "linkPhysAddress": linkPhysAddress,
       "linkMtu": linkMtu,
       "linkSpeed": linkSpeed,
       "linkOperStatus": linkOperStatus,
       "linkInOctets": linkInOctets,
       "linkInUcastPkts": linkInUcastPkts,
       "linkInNUcastPkts": linkInNUcastPkts,
       "linkInDiscards": linkInDiscards,
       "linkInError": linkInError,
       "linkInUnknownProtos": linkInUnknownProtos,
       "linkOutOctets": linkOutOctets,
       "linkOutUcastPkts": linkOutUcastPkts,
       "linkOutNUcastPkts": linkOutNUcastPkts,
       "linkOutDiscards": linkOutDiscards,
       "linkOutError": linkOutError,
       "linkOutQLen": linkOutQLen,
       "linkSessState": linkSessState,
       "linkESN": linkESN,
       "linkRSSI": linkRSSI,
       "linkAveJitter": linkAveJitter,
       "linkLastJitter": linkLastJitter,
       "linkAirDelay": linkAirDelay,
       "linkRegCount": linkRegCount,
       "linkReRegCount": linkReRegCount,
       "linkTimeOut": linkTimeOut,
       "linkLastRSSI": linkLastRSSI,
       "sessionCount": sessionCount,
       "softwareVersion": softwareVersion,
       "softwareBootVersion": softwareBootVersion,
       "fpgaVersion": fpgaVersion,
       "linkSiteName": linkSiteName,
       "avgPowerLevel": avgPowerLevel,
       "lastPowerLevel": lastPowerLevel,
       "sesDownLinkRate": sesDownLinkRate,
       "sesDownLinkLimit": sesDownLinkLimit,
       "sesUpLinkRate": sesUpLinkRate,
       "sesUpLinkLimit": sesUpLinkLimit,
       "adaptRate": adaptRate,
       "sesLoUpCIR": sesLoUpCIR,
       "sesLoDownCIR": sesLoDownCIR,
       "sesHiUpCIR": sesHiUpCIR,
       "sesHiDownCIR": sesHiDownCIR,
       "platformVer": platformVer,
       "smSessionTmr": smSessionTmr,
       "smSessionSeqNumMismatch": smSessionSeqNumMismatch,
       "dataVCNum": dataVCNum,
       "hiPriQEn": hiPriQEn,
       "dataVCNumHiQ": dataVCNumHiQ,
       "linkInOctetsHiQ": linkInOctetsHiQ,
       "linkInUcastPktsHiQ": linkInUcastPktsHiQ,
       "linkInNUcastPktsHiQ": linkInNUcastPktsHiQ,
       "linkInDiscardsHiQ": linkInDiscardsHiQ,
       "linkInErrorHiQ": linkInErrorHiQ,
       "linkInUnknownProtosHiQ": linkInUnknownProtosHiQ,
       "linkOutOctetsHiQ": linkOutOctetsHiQ,
       "linkOutUcastPktsHiQ": linkOutUcastPktsHiQ,
       "linkOutNUcastPktsHiQ": linkOutNUcastPktsHiQ,
       "linkOutDiscardsHiQ": linkOutDiscardsHiQ,
       "linkOutErrorHiQ": linkOutErrorHiQ,
       "vcQOverflow": vcQOverflow,
       "vcQOverflowHiQ": vcQOverflowHiQ,
       "p7p8HiPriQEn": p7p8HiPriQEn,
       "p7p8HiPriQ": p7p8HiPriQ,
       "linkAirDelayns": linkAirDelayns,
       "linkQualityAPData": linkQualityAPData,
       "linkManagementIP": linkManagementIP,
       "linkFragmentsReceived1XVertical": linkFragmentsReceived1XVertical,
       "linkFragmentsReceived2XVertical": linkFragmentsReceived2XVertical,
       "linkFragmentsReceived3XVertical": linkFragmentsReceived3XVertical,
       "linkFragmentsReceived4XVertical": linkFragmentsReceived4XVertical,
       "signalToNoiseRatioVertical": signalToNoiseRatioVertical,
       "radiusReplyMsg": radiusReplyMsg,
       "autoUpdateStatus": autoUpdateStatus,
       "radiusFramedIPAddress": radiusFramedIPAddress,
       "radiusFramedIPNetmask": radiusFramedIPNetmask,
       "radiusDefaultGateway": radiusDefaultGateway,
       "linkFragmentsReceived1XHorizontal": linkFragmentsReceived1XHorizontal,
       "linkFragmentsReceived2XHorizontal": linkFragmentsReceived2XHorizontal,
       "linkFragmentsReceived3XHorizontal": linkFragmentsReceived3XHorizontal,
       "linkFragmentsReceived4XHorizontal": linkFragmentsReceived4XHorizontal,
       "signalToNoiseRatioHorizontal": signalToNoiseRatioHorizontal,
       "linkSignalStrengthRatio": linkSignalStrengthRatio,
       "linkRadioDbmHorizontal": linkRadioDbmHorizontal,
       "linkRadioDbmVertical": linkRadioDbmVertical,
       "maxSMTxPwr": maxSMTxPwr,
       "productType": productType,
       "linkAdaptRateLowPri": linkAdaptRateLowPri,
       "linkAdaptRateHighPri": linkAdaptRateHighPri,
       "whispApsEvent": whispApsEvent,
       "whispApsRegEvent": whispApsRegEvent,
       "whispRegComplete": whispRegComplete,
       "whispRegLost": whispRegLost,
       "whispRegFailure": whispRegFailure,
       "whispDefKeyUsed": whispDefKeyUsed,
       "whispGPSEvent": whispGPSEvent,
       "whispGPSInSync": whispGPSInSync,
       "whispGPSOutSync": whispGPSOutSync,
       "whispApsDfsEvent": whispApsDfsEvent,
       "whispRadarDetected": whispRadarDetected,
       "whispRadarEnd": whispRadarEnd,
       "whispApRegulatoryEvent": whispApRegulatoryEvent,
       "regulatoryApCheckInvalidChanFailed": regulatoryApCheckInvalidChanFailed,
       "regulatoryCheckFailedNoRegionAp": regulatoryCheckFailedNoRegionAp,
       "regulatoryApCheckInvalidChBwFailed": regulatoryApCheckInvalidChBwFailed,
       "whispApRFOverloadEvent": whispApRFOverloadEvent,
       "rfLinkOverloadCondition": rfLinkOverloadCondition,
       "whispApsGroups": whispApsGroups,
       "whispLinkTestGroup": whispLinkTestGroup,
       "whispApsConfigGroup": whispApsConfigGroup,
       "whispApsLinkTableGroup": whispApsLinkTableGroup,
       "whispApsNotifGroup": whispApsNotifGroup,
       "whispApsFailedRegTableGroup": whispApsFailedRegTableGroup,
       "whispApsStatus": whispApsStatus,
       "regCount": regCount,
       "gpsStatus": gpsStatus,
       "radioSlicingAp": radioSlicingAp,
       "radioTxGainAp": radioTxGainAp,
       "dataSlotDwn": dataSlotDwn,
       "dataSlotUp": dataSlotUp,
       "dataSlotUpHi": dataSlotUpHi,
       "upLnkAckSlot": upLnkAckSlot,
       "upLnkAckSlotHi": upLnkAckSlotHi,
       "dwnLnkAckSlot": dwnLnkAckSlot,
       "dwnLnkAckSlotHi": dwnLnkAckSlotHi,
       "numCtrSlot": numCtrSlot,
       "numCtrSlotHi": numCtrSlotHi,
       "dfsStatus": dfsStatus,
       "dfsStatusPrimary": dfsStatusPrimary,
       "dfsStatusAlt1": dfsStatusAlt1,
       "dfsStatusAlt2": dfsStatusAlt2,
       "maxRegSMCount": maxRegSMCount,
       "systemTime": systemTime,
       "lastNTPTime": lastNTPTime,
       "regulatoryStatus": regulatoryStatus,
       "dhcpRlyAgntStat-reqRecvd": dhcpRlyAgntStat_reqRecvd,
       "dhcpRlyAgntStat-reqRelayed": dhcpRlyAgntStat_reqRelayed,
       "dhcpRlyAgntStat-reqDiscards": dhcpRlyAgntStat_reqDiscards,
       "dhcpRlyAgntStat-respRecvd": dhcpRlyAgntStat_respRecvd,
       "dhcpRlyAgntStat-respRelayed": dhcpRlyAgntStat_respRelayed,
       "dhcpRlyAgntStat-respDiscards": dhcpRlyAgntStat_respDiscards,
       "dhcpRlyAgntStat-untrustedDiscards": dhcpRlyAgntStat_untrustedDiscards,
       "dhcpRlyAgntStat-maxHopDiscards": dhcpRlyAgntStat_maxHopDiscards,
       "dhcpRlyAgntStat-pktTooBig": dhcpRlyAgntStat_pktTooBig,
       "dhcpRlyAgntStat-invalidGiaddrDiscards": dhcpRlyAgntStat_invalidGiaddrDiscards,
       "regFailureCount": regFailureCount,
       "ntpLogSNMP": ntpLogSNMP,
       "uGPSPowerStatus": uGPSPowerStatus,
       "rfOutDiscardRate": rfOutDiscardRate,
       "autoUpdateGlobalStatus": autoUpdateGlobalStatus,
       "currentRadioFreqCarrier": currentRadioFreqCarrier,
       "whispFailedRegTable": whispFailedRegTable,
       "whispFailedRegEntry": whispFailedRegEntry,
       "regGrantReason": regGrantReason,
       "regFailESN": regFailESN,
       "regFailTime": regFailTime,
       "regFailSeqNum": regFailSeqNum,
       "regFailReasonText": regFailReasonText,
       "whispApsDNS": whispApsDNS,
       "ntpDomainNameAppend": ntpDomainNameAppend,
       "ntpServer1": ntpServer1,
       "ntpServer2": ntpServer2,
       "ntpServer3": ntpServer3,
       "dhcprDomainNameAppend": dhcprDomainNameAppend,
       "dhcprServer": dhcprServer,
       "authDomainNameAppend": authDomainNameAppend,
       "authServer1": authServer1,
       "authServer2": authServer2,
       "authServer3": authServer3,
       "authServer4": authServer4,
       "authServer5": authServer5,
       "acctDomainNameAppend": acctDomainNameAppend,
       "whispApsRFConfig": whispApsRFConfig,
       "whispApsRFConfigRadios": whispApsRFConfigRadios,
       "whispApsRFConfigRadioEntry": whispApsRFConfigRadioEntry,
       "radioFreqCarrier": radioFreqCarrier,
       "radioDownlinkPercent": radioDownlinkPercent,
       "radioMaxRange": radioMaxRange,
       "radioControlSlots": radioControlSlots,
       "radioTransmitOutputPower": radioTransmitOutputPower,
       "radioColorCode": radioColorCode,
       "whispApsControls": whispApsControls,
       "clearLinkTableStats": clearLinkTableStats}
)
