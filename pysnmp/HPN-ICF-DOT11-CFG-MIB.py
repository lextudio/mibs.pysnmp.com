# SNMP MIB module (HPN-ICF-DOT11-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-CFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:50 2024
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

(HpnicfDot11AuthenType,
 HpnicfDot11ChannelScopeType,
 HpnicfDot11CirMode,
 HpnicfDot11ObjectIDType,
 HpnicfDot11PreambleType,
 HpnicfDot11RadioElementIndex,
 HpnicfDot11RadioScopeType,
 HpnicfDot11RadioType,
 HpnicfDot11RadioType2,
 HpnicfDot11SSIDEncryptModeType,
 HpnicfDot11SSIDStringType,
 HpnicfDot11SecIEStatusType,
 HpnicfDot11ServicePolicyIDType,
 HpnicfDot11TruthValueCM,
 HpnicfDot11TunnelSecSchemType,
 HpnicfDot11TxPwrLevelScopeType,
 HpnicfDot11WorkMode,
 hpnicfDot11,
 hpnicfDot11APElementIndex) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "HpnicfDot11AuthenType",
    "HpnicfDot11ChannelScopeType",
    "HpnicfDot11CirMode",
    "HpnicfDot11ObjectIDType",
    "HpnicfDot11PreambleType",
    "HpnicfDot11RadioElementIndex",
    "HpnicfDot11RadioScopeType",
    "HpnicfDot11RadioType",
    "HpnicfDot11RadioType2",
    "HpnicfDot11SSIDEncryptModeType",
    "HpnicfDot11SSIDStringType",
    "HpnicfDot11SecIEStatusType",
    "HpnicfDot11ServicePolicyIDType",
    "HpnicfDot11TruthValueCM",
    "HpnicfDot11TunnelSecSchemType",
    "HpnicfDot11TxPwrLevelScopeType",
    "HpnicfDot11WorkMode",
    "hpnicfDot11",
    "hpnicfDot11APElementIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfDot11CFG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4)
)
hpnicfDot11CFG.setRevisions(
        ("2010-09-25 18:00",
         "2010-09-02 18:00",
         "2009-07-29 18:00",
         "2009-05-07 20:00",
         "2009-03-20 15:30",
         "2008-11-07 15:30",
         "2008-07-09 18:00",
         "2008-02-25 18:00",
         "2007-12-21 18:00",
         "2007-10-09 16:55",
         "2007-06-19 18:00",
         "2007-04-27 20:00",
         "2007-02-01 20:00",
         "2006-05-10 19:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDot11GlobeConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11GlobeConfigGroup = _HpnicfDot11GlobeConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1)
)


class _HpnicfDot11GlobalCountryCode_Type(OctetString):
    """Custom type hpnicfDot11GlobalCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpnicfDot11GlobalCountryCode_Type.__name__ = "OctetString"
_HpnicfDot11GlobalCountryCode_Object = MibScalar
hpnicfDot11GlobalCountryCode = _HpnicfDot11GlobalCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 1),
    _HpnicfDot11GlobalCountryCode_Type()
)
hpnicfDot11GlobalCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11GlobalCountryCode.setStatus("current")


class _HpnicfDot11StaKeepALiveTimerIntvl_Type(Unsigned32):
    """Custom type hpnicfDot11StaKeepALiveTimerIntvl based on Unsigned32"""
    defaultValue = 0


_HpnicfDot11StaKeepALiveTimerIntvl_Object = MibScalar
hpnicfDot11StaKeepALiveTimerIntvl = _HpnicfDot11StaKeepALiveTimerIntvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 2),
    _HpnicfDot11StaKeepALiveTimerIntvl_Type()
)
hpnicfDot11StaKeepALiveTimerIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11StaKeepALiveTimerIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StaKeepALiveTimerIntvl.setUnits("second")
_HpnicfDot11StaIdleTimerIntvl_Type = Integer32
_HpnicfDot11StaIdleTimerIntvl_Object = MibScalar
hpnicfDot11StaIdleTimerIntvl = _HpnicfDot11StaIdleTimerIntvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 3),
    _HpnicfDot11StaIdleTimerIntvl_Type()
)
hpnicfDot11StaIdleTimerIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11StaIdleTimerIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StaIdleTimerIntvl.setUnits("second")


class _HpnicfDot11BroadcastProbeReply_Type(TruthValue):
    """Custom type hpnicfDot11BroadcastProbeReply based on TruthValue"""


_HpnicfDot11BroadcastProbeReply_Object = MibScalar
hpnicfDot11BroadcastProbeReply = _HpnicfDot11BroadcastProbeReply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 4),
    _HpnicfDot11BroadcastProbeReply_Type()
)
hpnicfDot11BroadcastProbeReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11BroadcastProbeReply.setStatus("current")


class _HpnicfDot11APScanMode_Type(Integer32):
    """Custom type hpnicfDot11APScanMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_HpnicfDot11APScanMode_Type.__name__ = "Integer32"
_HpnicfDot11APScanMode_Object = MibScalar
hpnicfDot11APScanMode = _HpnicfDot11APScanMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 5),
    _HpnicfDot11APScanMode_Type()
)
hpnicfDot11APScanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APScanMode.setStatus("current")
_HpnicfDot11ACCtrlTunnelSecSupport_Type = HpnicfDot11TunnelSecSchemType
_HpnicfDot11ACCtrlTunnelSecSupport_Object = MibScalar
hpnicfDot11ACCtrlTunnelSecSupport = _HpnicfDot11ACCtrlTunnelSecSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 6),
    _HpnicfDot11ACCtrlTunnelSecSupport_Type()
)
hpnicfDot11ACCtrlTunnelSecSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ACCtrlTunnelSecSupport.setStatus("current")


class _HpnicfDot11ACDataTunnelSecSupport_Type(HpnicfDot11TunnelSecSchemType):
    """Custom type hpnicfDot11ACDataTunnelSecSupport based on HpnicfDot11TunnelSecSchemType"""


_HpnicfDot11ACDataTunnelSecSupport_Object = MibScalar
hpnicfDot11ACDataTunnelSecSupport = _HpnicfDot11ACDataTunnelSecSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 7),
    _HpnicfDot11ACDataTunnelSecSupport_Type()
)
hpnicfDot11ACDataTunnelSecSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ACDataTunnelSecSupport.setStatus("current")


class _HpnicfDot11ACAutoAPSupport_Type(TruthValue):
    """Custom type hpnicfDot11ACAutoAPSupport based on TruthValue"""


_HpnicfDot11ACAutoAPSupport_Object = MibScalar
hpnicfDot11ACAutoAPSupport = _HpnicfDot11ACAutoAPSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 8),
    _HpnicfDot11ACAutoAPSupport_Type()
)
hpnicfDot11ACAutoAPSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ACAutoAPSupport.setStatus("current")


class _HpnicfDot11AutoAPName_Type(OctetString):
    """Custom type hpnicfDot11AutoAPName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11AutoAPName_Type.__name__ = "OctetString"
_HpnicfDot11AutoAPName_Object = MibScalar
hpnicfDot11AutoAPName = _HpnicfDot11AutoAPName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 9),
    _HpnicfDot11AutoAPName_Type()
)
hpnicfDot11AutoAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11AutoAPName.setStatus("current")


class _HpnicfDot11PersistentName_Type(OctetString):
    """Custom type hpnicfDot11PersistentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11PersistentName_Type.__name__ = "OctetString"
_HpnicfDot11PersistentName_Object = MibScalar
hpnicfDot11PersistentName = _HpnicfDot11PersistentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 10),
    _HpnicfDot11PersistentName_Type()
)
hpnicfDot11PersistentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11PersistentName.setStatus("current")
_HpnicfDot11IntfTrapThreshold_Type = Integer32
_HpnicfDot11IntfTrapThreshold_Object = MibScalar
hpnicfDot11IntfTrapThreshold = _HpnicfDot11IntfTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 11),
    _HpnicfDot11IntfTrapThreshold_Type()
)
hpnicfDot11IntfTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11IntfTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11IntfTrapThreshold.setUnits("dbm")


class _HpnicfDot11MonitorInterval_Type(Unsigned32):
    """Custom type hpnicfDot11MonitorInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 15),
    )


_HpnicfDot11MonitorInterval_Type.__name__ = "Unsigned32"
_HpnicfDot11MonitorInterval_Object = MibScalar
hpnicfDot11MonitorInterval = _HpnicfDot11MonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 12),
    _HpnicfDot11MonitorInterval_Type()
)
hpnicfDot11MonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11MonitorInterval.setUnits("minute")


class _HpnicfDot11SampleInterval_Type(Unsigned32):
    """Custom type hpnicfDot11SampleInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 300),
    )


_HpnicfDot11SampleInterval_Type.__name__ = "Unsigned32"
_HpnicfDot11SampleInterval_Object = MibScalar
hpnicfDot11SampleInterval = _HpnicfDot11SampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 13),
    _HpnicfDot11SampleInterval_Type()
)
hpnicfDot11SampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11SampleInterval.setUnits("second")


class _HpnicfDot11ChnlSwitChkInterval_Type(Unsigned32):
    """Custom type hpnicfDot11ChnlSwitChkInterval based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 180),
    )


_HpnicfDot11ChnlSwitChkInterval_Type.__name__ = "Unsigned32"
_HpnicfDot11ChnlSwitChkInterval_Object = MibScalar
hpnicfDot11ChnlSwitChkInterval = _HpnicfDot11ChnlSwitChkInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 14),
    _HpnicfDot11ChnlSwitChkInterval_Type()
)
hpnicfDot11ChnlSwitChkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ChnlSwitChkInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11ChnlSwitChkInterval.setUnits("minute")


class _HpnicfDot11APUserUplimit_Type(Unsigned32):
    """Custom type hpnicfDot11APUserUplimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfDot11APUserUplimit_Type.__name__ = "Unsigned32"
_HpnicfDot11APUserUplimit_Object = MibScalar
hpnicfDot11APUserUplimit = _HpnicfDot11APUserUplimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 15),
    _HpnicfDot11APUserUplimit_Type()
)
hpnicfDot11APUserUplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APUserUplimit.setStatus("current")


class _HpnicfDot11APL2IsolateEnable_Type(TruthValue):
    """Custom type hpnicfDot11APL2IsolateEnable based on TruthValue"""


_HpnicfDot11APL2IsolateEnable_Object = MibScalar
hpnicfDot11APL2IsolateEnable = _HpnicfDot11APL2IsolateEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 16),
    _HpnicfDot11APL2IsolateEnable_Type()
)
hpnicfDot11APL2IsolateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APL2IsolateEnable.setStatus("current")
_HpnicfDot11APBSSIDSupportNum_Type = Integer32
_HpnicfDot11APBSSIDSupportNum_Object = MibScalar
hpnicfDot11APBSSIDSupportNum = _HpnicfDot11APBSSIDSupportNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 17),
    _HpnicfDot11APBSSIDSupportNum_Type()
)
hpnicfDot11APBSSIDSupportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APBSSIDSupportNum.setStatus("current")
_HpnicfDot11APLastUpdateStatTime_Type = DateAndTime
_HpnicfDot11APLastUpdateStatTime_Object = MibScalar
hpnicfDot11APLastUpdateStatTime = _HpnicfDot11APLastUpdateStatTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 18),
    _HpnicfDot11APLastUpdateStatTime_Type()
)
hpnicfDot11APLastUpdateStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APLastUpdateStatTime.setStatus("current")


class _HpnicfDot11APDoSProtectEnable_Type(TruthValue):
    """Custom type hpnicfDot11APDoSProtectEnable based on TruthValue"""


_HpnicfDot11APDoSProtectEnable_Object = MibScalar
hpnicfDot11APDoSProtectEnable = _HpnicfDot11APDoSProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 19),
    _HpnicfDot11APDoSProtectEnable_Type()
)
hpnicfDot11APDoSProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APDoSProtectEnable.setStatus("current")


class _HpnicfDot11MaxAPPerIf_Type(Unsigned32):
    """Custom type hpnicfDot11MaxAPPerIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfDot11MaxAPPerIf_Type.__name__ = "Unsigned32"
_HpnicfDot11MaxAPPerIf_Object = MibScalar
hpnicfDot11MaxAPPerIf = _HpnicfDot11MaxAPPerIf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 20),
    _HpnicfDot11MaxAPPerIf_Type()
)
hpnicfDot11MaxAPPerIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11MaxAPPerIf.setStatus("current")
_HpnicfDot11SampleTimeStamp_Type = DateAndTime
_HpnicfDot11SampleTimeStamp_Object = MibScalar
hpnicfDot11SampleTimeStamp = _HpnicfDot11SampleTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 21),
    _HpnicfDot11SampleTimeStamp_Type()
)
hpnicfDot11SampleTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SampleTimeStamp.setStatus("current")


class _HpnicfDot11UplinkTrackId_Type(Unsigned32):
    """Custom type hpnicfDot11UplinkTrackId based on Unsigned32"""
    defaultValue = 0


_HpnicfDot11UplinkTrackId_Object = MibScalar
hpnicfDot11UplinkTrackId = _HpnicfDot11UplinkTrackId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 22),
    _HpnicfDot11UplinkTrackId_Type()
)
hpnicfDot11UplinkTrackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11UplinkTrackId.setStatus("current")


class _HpnicfDot11RtCollectSwitch_Type(TruthValue):
    """Custom type hpnicfDot11RtCollectSwitch based on TruthValue"""


_HpnicfDot11RtCollectSwitch_Object = MibScalar
hpnicfDot11RtCollectSwitch = _HpnicfDot11RtCollectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 23),
    _HpnicfDot11RtCollectSwitch_Type()
)
hpnicfDot11RtCollectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RtCollectSwitch.setStatus("current")
_HpnicfDot11RglCollectIntvl_Type = Integer32
_HpnicfDot11RglCollectIntvl_Object = MibScalar
hpnicfDot11RglCollectIntvl = _HpnicfDot11RglCollectIntvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 24),
    _HpnicfDot11RglCollectIntvl_Type()
)
hpnicfDot11RglCollectIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RglCollectIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RglCollectIntvl.setUnits("second")
_HpnicfDot11RtCollectIntvl_Type = Integer32
_HpnicfDot11RtCollectIntvl_Object = MibScalar
hpnicfDot11RtCollectIntvl = _HpnicfDot11RtCollectIntvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 25),
    _HpnicfDot11RtCollectIntvl_Type()
)
hpnicfDot11RtCollectIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RtCollectIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RtCollectIntvl.setUnits("second")


class _HpnicfDot11AllAPCpuUsageThreshold_Type(Integer32):
    """Custom type hpnicfDot11AllAPCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11AllAPCpuUsageThreshold_Type.__name__ = "Integer32"
_HpnicfDot11AllAPCpuUsageThreshold_Object = MibScalar
hpnicfDot11AllAPCpuUsageThreshold = _HpnicfDot11AllAPCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 26),
    _HpnicfDot11AllAPCpuUsageThreshold_Type()
)
hpnicfDot11AllAPCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11AllAPCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11AllAPCpuUsageThreshold.setUnits("onepercent")


class _HpnicfDot11AllAPMemUsageThreshold_Type(Integer32):
    """Custom type hpnicfDot11AllAPMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11AllAPMemUsageThreshold_Type.__name__ = "Integer32"
_HpnicfDot11AllAPMemUsageThreshold_Object = MibScalar
hpnicfDot11AllAPMemUsageThreshold = _HpnicfDot11AllAPMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 27),
    _HpnicfDot11AllAPMemUsageThreshold_Type()
)
hpnicfDot11AllAPMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11AllAPMemUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11AllAPMemUsageThreshold.setUnits("onepercent")
_HpnicfDot11AdjIntfTrapThreshold_Type = Integer32
_HpnicfDot11AdjIntfTrapThreshold_Object = MibScalar
hpnicfDot11AdjIntfTrapThreshold = _HpnicfDot11AdjIntfTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 28),
    _HpnicfDot11AdjIntfTrapThreshold_Type()
)
hpnicfDot11AdjIntfTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11AdjIntfTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11AdjIntfTrapThreshold.setUnits("dbm")


class _HpnicfDot11AllAPMonitorMode_Type(Integer32):
    """Custom type hpnicfDot11AllAPMonitorMode based on Integer32"""
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
        *(("hybrid", 3),
          ("monitor", 2),
          ("normal", 1))
    )


_HpnicfDot11AllAPMonitorMode_Type.__name__ = "Integer32"
_HpnicfDot11AllAPMonitorMode_Object = MibScalar
hpnicfDot11AllAPMonitorMode = _HpnicfDot11AllAPMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 29),
    _HpnicfDot11AllAPMonitorMode_Type()
)
hpnicfDot11AllAPMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11AllAPMonitorMode.setStatus("current")


class _HpnicfDot11GlobalApFmwUpdState_Type(Integer32):
    """Custom type hpnicfDot11GlobalApFmwUpdState based on Integer32"""
    defaultValue = 1

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


_HpnicfDot11GlobalApFmwUpdState_Type.__name__ = "Integer32"
_HpnicfDot11GlobalApFmwUpdState_Object = MibScalar
hpnicfDot11GlobalApFmwUpdState = _HpnicfDot11GlobalApFmwUpdState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 30),
    _HpnicfDot11GlobalApFmwUpdState_Type()
)
hpnicfDot11GlobalApFmwUpdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11GlobalApFmwUpdState.setStatus("current")
_HpnicfDot11ACNasIDCM_Type = OctetString
_HpnicfDot11ACNasIDCM_Object = MibScalar
hpnicfDot11ACNasIDCM = _HpnicfDot11ACNasIDCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 1, 31),
    _HpnicfDot11ACNasIDCM_Type()
)
hpnicfDot11ACNasIDCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ACNasIDCM.setStatus("current")
_HpnicfDot11PolicyConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11PolicyConfigGroup = _HpnicfDot11PolicyConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2)
)
_HpnicfDot11RadioPolicyTable_Object = MibTable
hpnicfDot11RadioPolicyTable = _HpnicfDot11RadioPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioPolicyTable.setStatus("current")
_HpnicfDot11RadioPolicyEntry_Object = MibTableRow
hpnicfDot11RadioPolicyEntry = _HpnicfDot11RadioPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1)
)
hpnicfDot11RadioPolicyEntry.setIndexNames(
    (1, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RadioPolicyName"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioPolicyEntry.setStatus("current")


class _HpnicfDot11RadioPolicyName_Type(OctetString):
    """Custom type hpnicfDot11RadioPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11RadioPolicyName_Type.__name__ = "OctetString"
_HpnicfDot11RadioPolicyName_Object = MibTableColumn
hpnicfDot11RadioPolicyName = _HpnicfDot11RadioPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1, 1),
    _HpnicfDot11RadioPolicyName_Type()
)
hpnicfDot11RadioPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RadioPolicyName.setStatus("current")


class _HpnicfDot11BeaconInterval_Type(Integer32):
    """Custom type hpnicfDot11BeaconInterval based on Integer32"""
    defaultValue = 100


_HpnicfDot11BeaconInterval_Object = MibTableColumn
hpnicfDot11BeaconInterval = _HpnicfDot11BeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1, 2),
    _HpnicfDot11BeaconInterval_Type()
)
hpnicfDot11BeaconInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11BeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11BeaconInterval.setUnits("TU")


class _HpnicfDot11DtimInterval_Type(Integer32):
    """Custom type hpnicfDot11DtimInterval based on Integer32"""
    defaultValue = 1


_HpnicfDot11DtimInterval_Object = MibTableColumn
hpnicfDot11DtimInterval = _HpnicfDot11DtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1, 3),
    _HpnicfDot11DtimInterval_Type()
)
hpnicfDot11DtimInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11DtimInterval.setStatus("current")


class _HpnicfDot11RtsThreshold_Type(Integer32):
    """Custom type hpnicfDot11RtsThreshold based on Integer32"""
    defaultValue = 2346


_HpnicfDot11RtsThreshold_Object = MibTableColumn
hpnicfDot11RtsThreshold = _HpnicfDot11RtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1, 4),
    _HpnicfDot11RtsThreshold_Type()
)
hpnicfDot11RtsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11RtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RtsThreshold.setUnits("byte")


class _HpnicfDot11FragThreshold_Type(Integer32):
    """Custom type hpnicfDot11FragThreshold based on Integer32"""
    defaultValue = 2346


_HpnicfDot11FragThreshold_Object = MibTableColumn
hpnicfDot11FragThreshold = _HpnicfDot11FragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1, 5),
    _HpnicfDot11FragThreshold_Type()
)
hpnicfDot11FragThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11FragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11FragThreshold.setUnits("byte")


class _HpnicfDot11ShortRetryThreshold_Type(Integer32):
    """Custom type hpnicfDot11ShortRetryThreshold based on Integer32"""
    defaultValue = 7


_HpnicfDot11ShortRetryThreshold_Object = MibTableColumn
hpnicfDot11ShortRetryThreshold = _HpnicfDot11ShortRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1, 6),
    _HpnicfDot11ShortRetryThreshold_Type()
)
hpnicfDot11ShortRetryThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11ShortRetryThreshold.setStatus("current")


class _HpnicfDot11LongRetryThreshold_Type(Integer32):
    """Custom type hpnicfDot11LongRetryThreshold based on Integer32"""
    defaultValue = 4


_HpnicfDot11LongRetryThreshold_Object = MibTableColumn
hpnicfDot11LongRetryThreshold = _HpnicfDot11LongRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1, 7),
    _HpnicfDot11LongRetryThreshold_Type()
)
hpnicfDot11LongRetryThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11LongRetryThreshold.setStatus("current")


class _HpnicfDot11MaxRxLifetime_Type(Unsigned32):
    """Custom type hpnicfDot11MaxRxLifetime based on Unsigned32"""
    defaultValue = 2000


_HpnicfDot11MaxRxLifetime_Object = MibTableColumn
hpnicfDot11MaxRxLifetime = _HpnicfDot11MaxRxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1, 8),
    _HpnicfDot11MaxRxLifetime_Type()
)
hpnicfDot11MaxRxLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11MaxRxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11MaxRxLifetime.setUnits("millisecond")
_HpnicfDot11RdoPolicyRowStatus_Type = RowStatus
_HpnicfDot11RdoPolicyRowStatus_Object = MibTableColumn
hpnicfDot11RdoPolicyRowStatus = _HpnicfDot11RdoPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1, 9),
    _HpnicfDot11RdoPolicyRowStatus_Type()
)
hpnicfDot11RdoPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11RdoPolicyRowStatus.setStatus("current")


class _HpnicfDot11RdoClientMaxCount_Type(Integer32):
    """Custom type hpnicfDot11RdoClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfDot11RdoClientMaxCount_Type.__name__ = "Integer32"
_HpnicfDot11RdoClientMaxCount_Object = MibTableColumn
hpnicfDot11RdoClientMaxCount = _HpnicfDot11RdoClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1, 10),
    _HpnicfDot11RdoClientMaxCount_Type()
)
hpnicfDot11RdoClientMaxCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11RdoClientMaxCount.setStatus("current")
_HpnicfDot11BeaconIntervalMs_Type = Integer32
_HpnicfDot11BeaconIntervalMs_Object = MibTableColumn
hpnicfDot11BeaconIntervalMs = _HpnicfDot11BeaconIntervalMs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 1, 1, 11),
    _HpnicfDot11BeaconIntervalMs_Type()
)
hpnicfDot11BeaconIntervalMs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11BeaconIntervalMs.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11BeaconIntervalMs.setUnits("ms")
_HpnicfDot11ServicePolicyTable_Object = MibTable
hpnicfDot11ServicePolicyTable = _HpnicfDot11ServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11ServicePolicyTable.setStatus("current")
_HpnicfDot11ServicePolicyEntry_Object = MibTableRow
hpnicfDot11ServicePolicyEntry = _HpnicfDot11ServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1)
)
hpnicfDot11ServicePolicyEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11ServicePolicyID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11ServicePolicyEntry.setStatus("current")
_HpnicfDot11ServicePolicyID_Type = HpnicfDot11ServicePolicyIDType
_HpnicfDot11ServicePolicyID_Object = MibTableColumn
hpnicfDot11ServicePolicyID = _HpnicfDot11ServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 1),
    _HpnicfDot11ServicePolicyID_Type()
)
hpnicfDot11ServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11ServicePolicyID.setStatus("current")
_HpnicfDot11SSIDName_Type = HpnicfDot11SSIDStringType
_HpnicfDot11SSIDName_Object = MibTableColumn
hpnicfDot11SSIDName = _HpnicfDot11SSIDName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 2),
    _HpnicfDot11SSIDName_Type()
)
hpnicfDot11SSIDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SSIDName.setStatus("current")


class _HpnicfDot11SSIDHidden_Type(TruthValue):
    """Custom type hpnicfDot11SSIDHidden based on TruthValue"""


_HpnicfDot11SSIDHidden_Object = MibTableColumn
hpnicfDot11SSIDHidden = _HpnicfDot11SSIDHidden_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 3),
    _HpnicfDot11SSIDHidden_Type()
)
hpnicfDot11SSIDHidden.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SSIDHidden.setStatus("current")
_HpnicfDot11AuthenMode_Type = HpnicfDot11AuthenType
_HpnicfDot11AuthenMode_Object = MibTableColumn
hpnicfDot11AuthenMode = _HpnicfDot11AuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 4),
    _HpnicfDot11AuthenMode_Type()
)
hpnicfDot11AuthenMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11AuthenMode.setStatus("current")
_HpnicfDot11SSIDEncryptionMode_Type = HpnicfDot11SSIDEncryptModeType
_HpnicfDot11SSIDEncryptionMode_Object = MibTableColumn
hpnicfDot11SSIDEncryptionMode = _HpnicfDot11SSIDEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 5),
    _HpnicfDot11SSIDEncryptionMode_Type()
)
hpnicfDot11SSIDEncryptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SSIDEncryptionMode.setStatus("current")


class _HpnicfDot11WlanInfBindingType_Type(OctetString):
    """Custom type hpnicfDot11WlanInfBindingType based on OctetString"""
    defaultValue = OctetString("WLAN-ESS")


_HpnicfDot11WlanInfBindingType_Object = MibTableColumn
hpnicfDot11WlanInfBindingType = _HpnicfDot11WlanInfBindingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 6),
    _HpnicfDot11WlanInfBindingType_Type()
)
hpnicfDot11WlanInfBindingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11WlanInfBindingType.setStatus("current")
_HpnicfDot11WlanInfBindingID_Type = Integer32
_HpnicfDot11WlanInfBindingID_Object = MibTableColumn
hpnicfDot11WlanInfBindingID = _HpnicfDot11WlanInfBindingID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 7),
    _HpnicfDot11WlanInfBindingID_Type()
)
hpnicfDot11WlanInfBindingID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11WlanInfBindingID.setStatus("current")
_HpnicfDot11SrvPolicyRowStatus_Type = RowStatus
_HpnicfDot11SrvPolicyRowStatus_Object = MibTableColumn
hpnicfDot11SrvPolicyRowStatus = _HpnicfDot11SrvPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 8),
    _HpnicfDot11SrvPolicyRowStatus_Type()
)
hpnicfDot11SrvPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SrvPolicyRowStatus.setStatus("current")


class _HpnicfDot11ClientMaxCount_Type(Integer32):
    """Custom type hpnicfDot11ClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfDot11ClientMaxCount_Type.__name__ = "Integer32"
_HpnicfDot11ClientMaxCount_Object = MibTableColumn
hpnicfDot11ClientMaxCount = _HpnicfDot11ClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 9),
    _HpnicfDot11ClientMaxCount_Type()
)
hpnicfDot11ClientMaxCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11ClientMaxCount.setStatus("current")


class _HpnicfDot11SPInCirMode_Type(HpnicfDot11CirMode):
    """Custom type hpnicfDot11SPInCirMode based on HpnicfDot11CirMode"""


_HpnicfDot11SPInCirMode_Object = MibTableColumn
hpnicfDot11SPInCirMode = _HpnicfDot11SPInCirMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 10),
    _HpnicfDot11SPInCirMode_Type()
)
hpnicfDot11SPInCirMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SPInCirMode.setStatus("current")


class _HpnicfDot11SPInCirValue_Type(Integer32):
    """Custom type hpnicfDot11SPInCirValue based on Integer32"""
    defaultValue = 0


_HpnicfDot11SPInCirValue_Object = MibTableColumn
hpnicfDot11SPInCirValue = _HpnicfDot11SPInCirValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 11),
    _HpnicfDot11SPInCirValue_Type()
)
hpnicfDot11SPInCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SPInCirValue.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11SPInCirValue.setUnits("Kbps")


class _HpnicfDot11SPOutCirMode_Type(HpnicfDot11CirMode):
    """Custom type hpnicfDot11SPOutCirMode based on HpnicfDot11CirMode"""


_HpnicfDot11SPOutCirMode_Object = MibTableColumn
hpnicfDot11SPOutCirMode = _HpnicfDot11SPOutCirMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 12),
    _HpnicfDot11SPOutCirMode_Type()
)
hpnicfDot11SPOutCirMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SPOutCirMode.setStatus("current")


class _HpnicfDot11SPOutCirValue_Type(Integer32):
    """Custom type hpnicfDot11SPOutCirValue based on Integer32"""
    defaultValue = 0


_HpnicfDot11SPOutCirValue_Object = MibTableColumn
hpnicfDot11SPOutCirValue = _HpnicfDot11SPOutCirValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 13),
    _HpnicfDot11SPOutCirValue_Type()
)
hpnicfDot11SPOutCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SPOutCirValue.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11SPOutCirValue.setUnits("Kbps")


class _HpnicfDot11WlanInfPVID_Type(Integer32):
    """Custom type hpnicfDot11WlanInfPVID based on Integer32"""
    defaultValue = 1


_HpnicfDot11WlanInfPVID_Object = MibTableColumn
hpnicfDot11WlanInfPVID = _HpnicfDot11WlanInfPVID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 14),
    _HpnicfDot11WlanInfPVID_Type()
)
hpnicfDot11WlanInfPVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11WlanInfPVID.setStatus("current")


class _HpnicfDot11SPInCirStaticValue_Type(Integer32):
    """Custom type hpnicfDot11SPInCirStaticValue based on Integer32"""
    defaultValue = 0


_HpnicfDot11SPInCirStaticValue_Object = MibTableColumn
hpnicfDot11SPInCirStaticValue = _HpnicfDot11SPInCirStaticValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 15),
    _HpnicfDot11SPInCirStaticValue_Type()
)
hpnicfDot11SPInCirStaticValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SPInCirStaticValue.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11SPInCirStaticValue.setUnits("Kbps")


class _HpnicfDot11SPOutCirStaticValue_Type(Integer32):
    """Custom type hpnicfDot11SPOutCirStaticValue based on Integer32"""
    defaultValue = 0


_HpnicfDot11SPOutCirStaticValue_Object = MibTableColumn
hpnicfDot11SPOutCirStaticValue = _HpnicfDot11SPOutCirStaticValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 16),
    _HpnicfDot11SPOutCirStaticValue_Type()
)
hpnicfDot11SPOutCirStaticValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SPOutCirStaticValue.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11SPOutCirStaticValue.setUnits("Kbps")


class _HpnicfDot11SPIsolate_Type(TruthValue):
    """Custom type hpnicfDot11SPIsolate based on TruthValue"""


_HpnicfDot11SPIsolate_Object = MibTableColumn
hpnicfDot11SPIsolate = _HpnicfDot11SPIsolate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 17),
    _HpnicfDot11SPIsolate_Type()
)
hpnicfDot11SPIsolate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SPIsolate.setStatus("current")
_HpnicfDot11WlanexAuthServerIP_Type = IpAddress
_HpnicfDot11WlanexAuthServerIP_Object = MibTableColumn
hpnicfDot11WlanexAuthServerIP = _HpnicfDot11WlanexAuthServerIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 18),
    _HpnicfDot11WlanexAuthServerIP_Type()
)
hpnicfDot11WlanexAuthServerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11WlanexAuthServerIP.setStatus("current")


class _HpnicfDot11SPBeaconMeasEnable_Type(TruthValue):
    """Custom type hpnicfDot11SPBeaconMeasEnable based on TruthValue"""


_HpnicfDot11SPBeaconMeasEnable_Object = MibTableColumn
hpnicfDot11SPBeaconMeasEnable = _HpnicfDot11SPBeaconMeasEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 19),
    _HpnicfDot11SPBeaconMeasEnable_Type()
)
hpnicfDot11SPBeaconMeasEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SPBeaconMeasEnable.setStatus("current")


class _HpnicfDot11SPBeaconMeasType_Type(Integer32):
    """Custom type hpnicfDot11SPBeaconMeasType based on Integer32"""
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
        *(("active", 2),
          ("beaconTable", 3),
          ("passive", 1))
    )


_HpnicfDot11SPBeaconMeasType_Type.__name__ = "Integer32"
_HpnicfDot11SPBeaconMeasType_Object = MibTableColumn
hpnicfDot11SPBeaconMeasType = _HpnicfDot11SPBeaconMeasType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 20),
    _HpnicfDot11SPBeaconMeasType_Type()
)
hpnicfDot11SPBeaconMeasType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SPBeaconMeasType.setStatus("current")


class _HpnicfDot11SPBeaconMeasInterval_Type(Integer32):
    """Custom type hpnicfDot11SPBeaconMeasInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_HpnicfDot11SPBeaconMeasInterval_Type.__name__ = "Integer32"
_HpnicfDot11SPBeaconMeasInterval_Object = MibTableColumn
hpnicfDot11SPBeaconMeasInterval = _HpnicfDot11SPBeaconMeasInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 21),
    _HpnicfDot11SPBeaconMeasInterval_Type()
)
hpnicfDot11SPBeaconMeasInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SPBeaconMeasInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11SPBeaconMeasInterval.setUnits("second")


class _HpnicfDot11AuthenModeCM_Type(Integer32):
    """Custom type hpnicfDot11AuthenModeCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 0),
          ("sharedkey", 1))
    )


_HpnicfDot11AuthenModeCM_Type.__name__ = "Integer32"
_HpnicfDot11AuthenModeCM_Object = MibTableColumn
hpnicfDot11AuthenModeCM = _HpnicfDot11AuthenModeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 22),
    _HpnicfDot11AuthenModeCM_Type()
)
hpnicfDot11AuthenModeCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11AuthenModeCM.setStatus("current")


class _HpnicfDot11SecIEStatusCM_Type(Integer32):
    """Custom type hpnicfDot11SecIEStatusCM based on Integer32"""
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
        *(("none", 0),
          ("wlanex", 3),
          ("wpa", 1),
          ("wpa2", 2))
    )


_HpnicfDot11SecIEStatusCM_Type.__name__ = "Integer32"
_HpnicfDot11SecIEStatusCM_Object = MibTableColumn
hpnicfDot11SecIEStatusCM = _HpnicfDot11SecIEStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 23),
    _HpnicfDot11SecIEStatusCM_Type()
)
hpnicfDot11SecIEStatusCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SecIEStatusCM.setStatus("current")


class _HpnicfDot11SecurityCiphersCM_Type(Integer32):
    """Custom type hpnicfDot11SecurityCiphersCM based on Integer32"""
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
        *(("aesccmp", 4),
          ("none", 0),
          ("tkip", 3),
          ("wep104", 2),
          ("wep40", 1),
          ("wpisms4", 5))
    )


_HpnicfDot11SecurityCiphersCM_Type.__name__ = "Integer32"
_HpnicfDot11SecurityCiphersCM_Object = MibTableColumn
hpnicfDot11SecurityCiphersCM = _HpnicfDot11SecurityCiphersCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 24),
    _HpnicfDot11SecurityCiphersCM_Type()
)
hpnicfDot11SecurityCiphersCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SecurityCiphersCM.setStatus("current")


class _HpnicfDot11SrvPolicyStatusCM_Type(Integer32):
    """Custom type hpnicfDot11SrvPolicyStatusCM based on Integer32"""
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


_HpnicfDot11SrvPolicyStatusCM_Type.__name__ = "Integer32"
_HpnicfDot11SrvPolicyStatusCM_Object = MibTableColumn
hpnicfDot11SrvPolicyStatusCM = _HpnicfDot11SrvPolicyStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 25),
    _HpnicfDot11SrvPolicyStatusCM_Type()
)
hpnicfDot11SrvPolicyStatusCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SrvPolicyStatusCM.setStatus("current")


class _HpnicfDot11SSIDHiddenCM_Type(HpnicfDot11TruthValueCM):
    """Custom type hpnicfDot11SSIDHiddenCM based on HpnicfDot11TruthValueCM"""


_HpnicfDot11SSIDHiddenCM_Object = MibTableColumn
hpnicfDot11SSIDHiddenCM = _HpnicfDot11SSIDHiddenCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 26),
    _HpnicfDot11SSIDHiddenCM_Type()
)
hpnicfDot11SSIDHiddenCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SSIDHiddenCM.setStatus("current")


class _HpnicfDot11SPIsolateCM_Type(HpnicfDot11TruthValueCM):
    """Custom type hpnicfDot11SPIsolateCM based on HpnicfDot11TruthValueCM"""


_HpnicfDot11SPIsolateCM_Object = MibTableColumn
hpnicfDot11SPIsolateCM = _HpnicfDot11SPIsolateCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 2, 1, 27),
    _HpnicfDot11SPIsolateCM_Type()
)
hpnicfDot11SPIsolateCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SPIsolateCM.setStatus("current")
_HpnicfDot11ServicePolicyExtTable_Object = MibTable
hpnicfDot11ServicePolicyExtTable = _HpnicfDot11ServicePolicyExtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11ServicePolicyExtTable.setStatus("current")
_HpnicfDot11ServicePolicyExtEntry_Object = MibTableRow
hpnicfDot11ServicePolicyExtEntry = _HpnicfDot11ServicePolicyExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 3, 1)
)
hpnicfDot11ServicePolicyExtEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11ServicePolicyExtID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11ServicePolicyExtEntry.setStatus("current")
_HpnicfDot11ServicePolicyExtID_Type = HpnicfDot11ServicePolicyIDType
_HpnicfDot11ServicePolicyExtID_Object = MibTableColumn
hpnicfDot11ServicePolicyExtID = _HpnicfDot11ServicePolicyExtID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 3, 1, 1),
    _HpnicfDot11ServicePolicyExtID_Type()
)
hpnicfDot11ServicePolicyExtID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11ServicePolicyExtID.setStatus("current")
_HpnicfDot11SecIEStatus_Type = HpnicfDot11SecIEStatusType
_HpnicfDot11SecIEStatus_Object = MibTableColumn
hpnicfDot11SecIEStatus = _HpnicfDot11SecIEStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 3, 1, 2),
    _HpnicfDot11SecIEStatus_Type()
)
hpnicfDot11SecIEStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SecIEStatus.setStatus("current")
_HpnicfDot11SecurityCiphers_Type = Integer32
_HpnicfDot11SecurityCiphers_Object = MibTableColumn
hpnicfDot11SecurityCiphers = _HpnicfDot11SecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 3, 1, 3),
    _HpnicfDot11SecurityCiphers_Type()
)
hpnicfDot11SecurityCiphers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SecurityCiphers.setStatus("current")


class _HpnicfDot11CipherKeyIndex_Type(Integer32):
    """Custom type hpnicfDot11CipherKeyIndex based on Integer32"""
    defaultValue = 1


_HpnicfDot11CipherKeyIndex_Object = MibTableColumn
hpnicfDot11CipherKeyIndex = _HpnicfDot11CipherKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 3, 1, 4),
    _HpnicfDot11CipherKeyIndex_Type()
)
hpnicfDot11CipherKeyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11CipherKeyIndex.setStatus("current")
_HpnicfDot11CipherKey_Type = OctetString
_HpnicfDot11CipherKey_Object = MibTableColumn
hpnicfDot11CipherKey = _HpnicfDot11CipherKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 3, 1, 5),
    _HpnicfDot11CipherKey_Type()
)
hpnicfDot11CipherKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11CipherKey.setStatus("current")
_HpnicfDot11SrvPolicyExtRowStatus_Type = RowStatus
_HpnicfDot11SrvPolicyExtRowStatus_Object = MibTableColumn
hpnicfDot11SrvPolicyExtRowStatus = _HpnicfDot11SrvPolicyExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 3, 1, 6),
    _HpnicfDot11SrvPolicyExtRowStatus_Type()
)
hpnicfDot11SrvPolicyExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SrvPolicyExtRowStatus.setStatus("current")


class _HpnicfDot11CipherKeyType_Type(Integer32):
    """Custom type hpnicfDot11CipherKeyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("char", 1),
          ("hex", 2))
    )


_HpnicfDot11CipherKeyType_Type.__name__ = "Integer32"
_HpnicfDot11CipherKeyType_Object = MibTableColumn
hpnicfDot11CipherKeyType = _HpnicfDot11CipherKeyType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 3, 1, 7),
    _HpnicfDot11CipherKeyType_Type()
)
hpnicfDot11CipherKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11CipherKeyType.setStatus("current")
_HpnicfDot11RadioPolicyExtTable_Object = MibTable
hpnicfDot11RadioPolicyExtTable = _HpnicfDot11RadioPolicyExtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioPolicyExtTable.setStatus("current")
_HpnicfDot11RadioPolicyExtEntry_Object = MibTableRow
hpnicfDot11RadioPolicyExtEntry = _HpnicfDot11RadioPolicyExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4, 1)
)
hpnicfDot11RadioPolicyExtEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RPAPSerialID"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RPRadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioPolicyExtEntry.setStatus("current")


class _HpnicfDot11RPAPSerialID_Type(OctetString):
    """Custom type hpnicfDot11RPAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11RPAPSerialID_Type.__name__ = "OctetString"
_HpnicfDot11RPAPSerialID_Object = MibTableColumn
hpnicfDot11RPAPSerialID = _HpnicfDot11RPAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4, 1, 1),
    _HpnicfDot11RPAPSerialID_Type()
)
hpnicfDot11RPAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RPAPSerialID.setStatus("current")
_HpnicfDot11RPRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11RPRadioID_Object = MibTableColumn
hpnicfDot11RPRadioID = _HpnicfDot11RPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4, 1, 2),
    _HpnicfDot11RPRadioID_Type()
)
hpnicfDot11RPRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RPRadioID.setStatus("current")


class _HpnicfDot11RPBeaconInterval_Type(Integer32):
    """Custom type hpnicfDot11RPBeaconInterval based on Integer32"""
    defaultValue = 100


_HpnicfDot11RPBeaconInterval_Object = MibTableColumn
hpnicfDot11RPBeaconInterval = _HpnicfDot11RPBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4, 1, 3),
    _HpnicfDot11RPBeaconInterval_Type()
)
hpnicfDot11RPBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RPBeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RPBeaconInterval.setUnits("milliseconds")


class _HpnicfDot11RPDtimInterval_Type(Integer32):
    """Custom type hpnicfDot11RPDtimInterval based on Integer32"""
    defaultValue = 1


_HpnicfDot11RPDtimInterval_Object = MibTableColumn
hpnicfDot11RPDtimInterval = _HpnicfDot11RPDtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4, 1, 4),
    _HpnicfDot11RPDtimInterval_Type()
)
hpnicfDot11RPDtimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RPDtimInterval.setStatus("current")


class _HpnicfDot11RPRtsThreshold_Type(Integer32):
    """Custom type hpnicfDot11RPRtsThreshold based on Integer32"""
    defaultValue = 2346


_HpnicfDot11RPRtsThreshold_Object = MibTableColumn
hpnicfDot11RPRtsThreshold = _HpnicfDot11RPRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4, 1, 5),
    _HpnicfDot11RPRtsThreshold_Type()
)
hpnicfDot11RPRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RPRtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RPRtsThreshold.setUnits("byte")


class _HpnicfDot11RPFragThreshold_Type(Integer32):
    """Custom type hpnicfDot11RPFragThreshold based on Integer32"""
    defaultValue = 2346


_HpnicfDot11RPFragThreshold_Object = MibTableColumn
hpnicfDot11RPFragThreshold = _HpnicfDot11RPFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4, 1, 6),
    _HpnicfDot11RPFragThreshold_Type()
)
hpnicfDot11RPFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RPFragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RPFragThreshold.setUnits("byte")


class _HpnicfDot11RPShortRetryThreshold_Type(Integer32):
    """Custom type hpnicfDot11RPShortRetryThreshold based on Integer32"""
    defaultValue = 7


_HpnicfDot11RPShortRetryThreshold_Object = MibTableColumn
hpnicfDot11RPShortRetryThreshold = _HpnicfDot11RPShortRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4, 1, 7),
    _HpnicfDot11RPShortRetryThreshold_Type()
)
hpnicfDot11RPShortRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RPShortRetryThreshold.setStatus("current")


class _HpnicfDot11RPLongRetryThreshold_Type(Integer32):
    """Custom type hpnicfDot11RPLongRetryThreshold based on Integer32"""
    defaultValue = 4


_HpnicfDot11RPLongRetryThreshold_Object = MibTableColumn
hpnicfDot11RPLongRetryThreshold = _HpnicfDot11RPLongRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4, 1, 8),
    _HpnicfDot11RPLongRetryThreshold_Type()
)
hpnicfDot11RPLongRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RPLongRetryThreshold.setStatus("current")


class _HpnicfDot11RPClientMaxCount_Type(Integer32):
    """Custom type hpnicfDot11RPClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfDot11RPClientMaxCount_Type.__name__ = "Integer32"
_HpnicfDot11RPClientMaxCount_Object = MibTableColumn
hpnicfDot11RPClientMaxCount = _HpnicfDot11RPClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4, 1, 9),
    _HpnicfDot11RPClientMaxCount_Type()
)
hpnicfDot11RPClientMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RPClientMaxCount.setStatus("current")


class _HpnicfDot11RPBeaconIntervalCM_Type(Integer32):
    """Custom type hpnicfDot11RPBeaconIntervalCM based on Integer32"""
    defaultValue = 100


_HpnicfDot11RPBeaconIntervalCM_Object = MibTableColumn
hpnicfDot11RPBeaconIntervalCM = _HpnicfDot11RPBeaconIntervalCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 4, 1, 10),
    _HpnicfDot11RPBeaconIntervalCM_Type()
)
hpnicfDot11RPBeaconIntervalCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RPBeaconIntervalCM.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RPBeaconIntervalCM.setUnits("timeunit")
_HpnicfDot11SrvPortSecurityTable_Object = MibTable
hpnicfDot11SrvPortSecurityTable = _HpnicfDot11SrvPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfDot11SrvPortSecurityTable.setStatus("current")
_HpnicfDot11SrvPortSecurityEntry_Object = MibTableRow
hpnicfDot11SrvPortSecurityEntry = _HpnicfDot11SrvPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 5, 1)
)
hpnicfDot11SrvPortSecurityEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11SecurityServicePolicyID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11SrvPortSecurityEntry.setStatus("current")
_HpnicfDot11SecurityServicePolicyID_Type = HpnicfDot11ServicePolicyIDType
_HpnicfDot11SecurityServicePolicyID_Object = MibTableColumn
hpnicfDot11SecurityServicePolicyID = _HpnicfDot11SecurityServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 5, 1, 1),
    _HpnicfDot11SecurityServicePolicyID_Type()
)
hpnicfDot11SecurityServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11SecurityServicePolicyID.setStatus("current")


class _HpnicfDot11SrvPortSecurityMode_Type(Integer32):
    """Custom type hpnicfDot11SrvPortSecurityMode based on Integer32"""
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
        *(("ext", 6),
          ("macAddressAndPsk", 4),
          ("noRestrictions", 1),
          ("psk", 3),
          ("userLoginSecureExt", 2),
          ("userLoginSecureExtOrPsk", 5))
    )


_HpnicfDot11SrvPortSecurityMode_Type.__name__ = "Integer32"
_HpnicfDot11SrvPortSecurityMode_Object = MibTableColumn
hpnicfDot11SrvPortSecurityMode = _HpnicfDot11SrvPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 5, 1, 2),
    _HpnicfDot11SrvPortSecurityMode_Type()
)
hpnicfDot11SrvPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SrvPortSecurityMode.setStatus("current")


class _HpnicfDot11SrvSecurityKeyType_Type(Integer32):
    """Custom type hpnicfDot11SrvSecurityKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userLoginTxKeyTypeDot11Key", 2),
          ("userLoginTxKeyTypeNone", 1),
          ("userLoginTxKeyTypeRsaRC4Key", 3))
    )


_HpnicfDot11SrvSecurityKeyType_Type.__name__ = "Integer32"
_HpnicfDot11SrvSecurityKeyType_Object = MibTableColumn
hpnicfDot11SrvSecurityKeyType = _HpnicfDot11SrvSecurityKeyType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 5, 1, 3),
    _HpnicfDot11SrvSecurityKeyType_Type()
)
hpnicfDot11SrvSecurityKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SrvSecurityKeyType.setStatus("current")


class _HpnicfDot11SrvSecurityPskKeyMode_Type(Integer32):
    """Custom type hpnicfDot11SrvSecurityPskKeyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pskKeyModeNone", 1),
          ("pskKeyModePassPhrase", 2),
          ("pskKeyModeRawKey", 3))
    )


_HpnicfDot11SrvSecurityPskKeyMode_Type.__name__ = "Integer32"
_HpnicfDot11SrvSecurityPskKeyMode_Object = MibTableColumn
hpnicfDot11SrvSecurityPskKeyMode = _HpnicfDot11SrvSecurityPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 5, 1, 4),
    _HpnicfDot11SrvSecurityPskKeyMode_Type()
)
hpnicfDot11SrvSecurityPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SrvSecurityPskKeyMode.setStatus("current")


class _HpnicfDot11SrvSecurityPskKeyString_Type(DisplayString):
    """Custom type hpnicfDot11SrvSecurityPskKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfDot11SrvSecurityPskKeyString_Type.__name__ = "DisplayString"
_HpnicfDot11SrvSecurityPskKeyString_Object = MibTableColumn
hpnicfDot11SrvSecurityPskKeyString = _HpnicfDot11SrvSecurityPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 5, 1, 5),
    _HpnicfDot11SrvSecurityPskKeyString_Type()
)
hpnicfDot11SrvSecurityPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SrvSecurityPskKeyString.setStatus("current")


class _HpnicfDot11SrvPortSecurityModeCM_Type(Integer32):
    """Custom type hpnicfDot11SrvPortSecurityModeCM based on Integer32"""
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
        *(("none", 0),
          ("psk", 1),
          ("radius", 2),
          ("wlanex", 3))
    )


_HpnicfDot11SrvPortSecurityModeCM_Type.__name__ = "Integer32"
_HpnicfDot11SrvPortSecurityModeCM_Object = MibTableColumn
hpnicfDot11SrvPortSecurityModeCM = _HpnicfDot11SrvPortSecurityModeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 5, 1, 6),
    _HpnicfDot11SrvPortSecurityModeCM_Type()
)
hpnicfDot11SrvPortSecurityModeCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SrvPortSecurityModeCM.setStatus("current")
_HpnicfDot11SrvPolicyExtendTable_Object = MibTable
hpnicfDot11SrvPolicyExtendTable = _HpnicfDot11SrvPolicyExtendTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfDot11SrvPolicyExtendTable.setStatus("current")
_HpnicfDot11SrvPolicyExtendEntry_Object = MibTableRow
hpnicfDot11SrvPolicyExtendEntry = _HpnicfDot11SrvPolicyExtendEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 6, 1)
)
hpnicfDot11SrvPolicyExtendEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11ServicePolicyID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11SrvPolicyExtendEntry.setStatus("current")


class _HpnicfDot11SPEnable_Type(Integer32):
    """Custom type hpnicfDot11SPEnable based on Integer32"""
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


_HpnicfDot11SPEnable_Type.__name__ = "Integer32"
_HpnicfDot11SPEnable_Object = MibTableColumn
hpnicfDot11SPEnable = _HpnicfDot11SPEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 2, 6, 1, 1),
    _HpnicfDot11SPEnable_Type()
)
hpnicfDot11SPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SPEnable.setStatus("current")
_HpnicfDot11APConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11APConfigGroup = _HpnicfDot11APConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3)
)
_HpnicfDot11APTemplateTable_Object = MibTable
hpnicfDot11APTemplateTable = _HpnicfDot11APTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11APTemplateTable.setStatus("current")
_HpnicfDot11APTemplateEntry_Object = MibTableRow
hpnicfDot11APTemplateEntry = _HpnicfDot11APTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1)
)
hpnicfDot11APTemplateEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11APTemplateName"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APTemplateEntry.setStatus("current")


class _HpnicfDot11APTemplateName_Type(OctetString):
    """Custom type hpnicfDot11APTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11APTemplateName_Type.__name__ = "OctetString"
_HpnicfDot11APTemplateName_Object = MibTableColumn
hpnicfDot11APTemplateName = _HpnicfDot11APTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 1),
    _HpnicfDot11APTemplateName_Type()
)
hpnicfDot11APTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APTemplateName.setStatus("current")
_HpnicfDot11APSerialID_Type = OctetString
_HpnicfDot11APSerialID_Object = MibTableColumn
hpnicfDot11APSerialID = _HpnicfDot11APSerialID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 2),
    _HpnicfDot11APSerialID_Type()
)
hpnicfDot11APSerialID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APSerialID.setStatus("current")
_HpnicfDot11TemplateAPModelAlias_Type = OctetString
_HpnicfDot11TemplateAPModelAlias_Object = MibTableColumn
hpnicfDot11TemplateAPModelAlias = _HpnicfDot11TemplateAPModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 3),
    _HpnicfDot11TemplateAPModelAlias_Type()
)
hpnicfDot11TemplateAPModelAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11TemplateAPModelAlias.setStatus("current")
_HpnicfDot11Description_Type = OctetString
_HpnicfDot11Description_Object = MibTableColumn
hpnicfDot11Description = _HpnicfDot11Description_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 4),
    _HpnicfDot11Description_Type()
)
hpnicfDot11Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11Description.setStatus("current")


class _HpnicfDot11APWorkMode_Type(Integer32):
    """Custom type hpnicfDot11APWorkMode based on Integer32"""
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
        *(("hybrid", 3),
          ("monitor", 2),
          ("normal", 1))
    )


_HpnicfDot11APWorkMode_Type.__name__ = "Integer32"
_HpnicfDot11APWorkMode_Object = MibTableColumn
hpnicfDot11APWorkMode = _HpnicfDot11APWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 5),
    _HpnicfDot11APWorkMode_Type()
)
hpnicfDot11APWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APWorkMode.setStatus("current")
_HpnicfDot11APTemplateRowStatus_Type = RowStatus
_HpnicfDot11APTemplateRowStatus_Object = MibTableColumn
hpnicfDot11APTemplateRowStatus = _HpnicfDot11APTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 6),
    _HpnicfDot11APTemplateRowStatus_Type()
)
hpnicfDot11APTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APTemplateRowStatus.setStatus("current")
_HpnicfDot11APName_Type = OctetString
_HpnicfDot11APName_Object = MibTableColumn
hpnicfDot11APName = _HpnicfDot11APName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 7),
    _HpnicfDot11APName_Type()
)
hpnicfDot11APName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APName.setStatus("current")
_HpnicfDot11StatisInterv_Type = Integer32
_HpnicfDot11StatisInterv_Object = MibTableColumn
hpnicfDot11StatisInterv = _HpnicfDot11StatisInterv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 8),
    _HpnicfDot11StatisInterv_Type()
)
hpnicfDot11StatisInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11StatisInterv.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StatisInterv.setUnits("second")


class _HpnicfDot11APBroadcastProbeReply_Type(TruthValue):
    """Custom type hpnicfDot11APBroadcastProbeReply based on TruthValue"""


_HpnicfDot11APBroadcastProbeReply_Object = MibTableColumn
hpnicfDot11APBroadcastProbeReply = _HpnicfDot11APBroadcastProbeReply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 9),
    _HpnicfDot11APBroadcastProbeReply_Type()
)
hpnicfDot11APBroadcastProbeReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APBroadcastProbeReply.setStatus("current")
_HpnicfDot11StaIdleTimerInterv_Type = Integer32
_HpnicfDot11StaIdleTimerInterv_Object = MibTableColumn
hpnicfDot11StaIdleTimerInterv = _HpnicfDot11StaIdleTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 10),
    _HpnicfDot11StaIdleTimerInterv_Type()
)
hpnicfDot11StaIdleTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11StaIdleTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StaIdleTimerInterv.setUnits("second")
_HpnicfDot11StaKeepAliveTimerInterv_Type = Integer32
_HpnicfDot11StaKeepAliveTimerInterv_Object = MibTableColumn
hpnicfDot11StaKeepAliveTimerInterv = _HpnicfDot11StaKeepAliveTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 11),
    _HpnicfDot11StaKeepAliveTimerInterv_Type()
)
hpnicfDot11StaKeepAliveTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11StaKeepAliveTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StaKeepAliveTimerInterv.setUnits("second")
_HpnicfDot11APCir_Type = Integer32
_HpnicfDot11APCir_Object = MibTableColumn
hpnicfDot11APCir = _HpnicfDot11APCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 12),
    _HpnicfDot11APCir_Type()
)
hpnicfDot11APCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APCir.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APCir.setUnits("Kbps")
_HpnicfDot11APCbs_Type = Integer32
_HpnicfDot11APCbs_Object = MibTableColumn
hpnicfDot11APCbs = _HpnicfDot11APCbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 13),
    _HpnicfDot11APCbs_Type()
)
hpnicfDot11APCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APCbs.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APCbs.setUnits("Bytes")


class _HpnicfDot11APPriorityLevel_Type(Integer32):
    """Custom type hpnicfDot11APPriorityLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfDot11APPriorityLevel_Type.__name__ = "Integer32"
_HpnicfDot11APPriorityLevel_Object = MibTableColumn
hpnicfDot11APPriorityLevel = _HpnicfDot11APPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 14),
    _HpnicfDot11APPriorityLevel_Type()
)
hpnicfDot11APPriorityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APPriorityLevel.setStatus("current")
_HpnicfDot11APElementID_Type = Integer32
_HpnicfDot11APElementID_Object = MibTableColumn
hpnicfDot11APElementID = _HpnicfDot11APElementID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 15),
    _HpnicfDot11APElementID_Type()
)
hpnicfDot11APElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APElementID.setStatus("current")


class _HpnicfDot11APDevDetectEnable_Type(TruthValue):
    """Custom type hpnicfDot11APDevDetectEnable based on TruthValue"""


_HpnicfDot11APDevDetectEnable_Object = MibTableColumn
hpnicfDot11APDevDetectEnable = _HpnicfDot11APDevDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 16),
    _HpnicfDot11APDevDetectEnable_Type()
)
hpnicfDot11APDevDetectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APDevDetectEnable.setStatus("current")


class _HpnicfDot11APGetIPMethod_Type(Integer32):
    """Custom type hpnicfDot11APGetIPMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpAlloc", 1),
          ("static", 2))
    )


_HpnicfDot11APGetIPMethod_Type.__name__ = "Integer32"
_HpnicfDot11APGetIPMethod_Object = MibTableColumn
hpnicfDot11APGetIPMethod = _HpnicfDot11APGetIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 17),
    _HpnicfDot11APGetIPMethod_Type()
)
hpnicfDot11APGetIPMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APGetIPMethod.setStatus("current")


class _HpnicfDot11StatisIntervMode_Type(Integer32):
    """Custom type hpnicfDot11StatisIntervMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("realtime", 2))
    )


_HpnicfDot11StatisIntervMode_Type.__name__ = "Integer32"
_HpnicfDot11StatisIntervMode_Object = MibTableColumn
hpnicfDot11StatisIntervMode = _HpnicfDot11StatisIntervMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 18),
    _HpnicfDot11StatisIntervMode_Type()
)
hpnicfDot11StatisIntervMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11StatisIntervMode.setStatus("current")


class _HpnicfDot11ApTrapEnabled_Type(TruthValue):
    """Custom type hpnicfDot11ApTrapEnabled based on TruthValue"""


_HpnicfDot11ApTrapEnabled_Object = MibTableColumn
hpnicfDot11ApTrapEnabled = _HpnicfDot11ApTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 19),
    _HpnicfDot11ApTrapEnabled_Type()
)
hpnicfDot11ApTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11ApTrapEnabled.setStatus("current")


class _HpnicfDot11ApFmwUpdState_Type(Integer32):
    """Custom type hpnicfDot11ApFmwUpdState based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("inherit", 3))
    )


_HpnicfDot11ApFmwUpdState_Type.__name__ = "Integer32"
_HpnicfDot11ApFmwUpdState_Object = MibTableColumn
hpnicfDot11ApFmwUpdState = _HpnicfDot11ApFmwUpdState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 20),
    _HpnicfDot11ApFmwUpdState_Type()
)
hpnicfDot11ApFmwUpdState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11ApFmwUpdState.setStatus("current")


class _HpnicfDot11StatisIntervModeCM_Type(Integer32):
    """Custom type hpnicfDot11StatisIntervModeCM based on Integer32"""
    defaultValue = 0

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


_HpnicfDot11StatisIntervModeCM_Type.__name__ = "Integer32"
_HpnicfDot11StatisIntervModeCM_Object = MibTableColumn
hpnicfDot11StatisIntervModeCM = _HpnicfDot11StatisIntervModeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 21),
    _HpnicfDot11StatisIntervModeCM_Type()
)
hpnicfDot11StatisIntervModeCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11StatisIntervModeCM.setStatus("current")
_HpnicfDot11ApNasIDCM_Type = OctetString
_HpnicfDot11ApNasIDCM_Object = MibTableColumn
hpnicfDot11ApNasIDCM = _HpnicfDot11ApNasIDCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 1, 1, 22),
    _HpnicfDot11ApNasIDCM_Type()
)
hpnicfDot11ApNasIDCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11ApNasIDCM.setStatus("current")
_HpnicfDot11RadioToConfigTable_Object = MibTable
hpnicfDot11RadioToConfigTable = _HpnicfDot11RadioToConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioToConfigTable.setStatus("current")
_HpnicfDot11RadioToConfigEntry_Object = MibTableRow
hpnicfDot11RadioToConfigEntry = _HpnicfDot11RadioToConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1)
)
hpnicfDot11RadioToConfigEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11APTemplateNameCfg"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11CfgRadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioToConfigEntry.setStatus("current")


class _HpnicfDot11APTemplateNameCfg_Type(OctetString):
    """Custom type hpnicfDot11APTemplateNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11APTemplateNameCfg_Type.__name__ = "OctetString"
_HpnicfDot11APTemplateNameCfg_Object = MibTableColumn
hpnicfDot11APTemplateNameCfg = _HpnicfDot11APTemplateNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 1),
    _HpnicfDot11APTemplateNameCfg_Type()
)
hpnicfDot11APTemplateNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APTemplateNameCfg.setStatus("current")
_HpnicfDot11CfgRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11CfgRadioID_Object = MibTableColumn
hpnicfDot11CfgRadioID = _HpnicfDot11CfgRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 2),
    _HpnicfDot11CfgRadioID_Type()
)
hpnicfDot11CfgRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11CfgRadioID.setStatus("current")
_HpnicfDot11CfgRadioPolicyName_Type = OctetString
_HpnicfDot11CfgRadioPolicyName_Object = MibTableColumn
hpnicfDot11CfgRadioPolicyName = _HpnicfDot11CfgRadioPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 3),
    _HpnicfDot11CfgRadioPolicyName_Type()
)
hpnicfDot11CfgRadioPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgRadioPolicyName.setStatus("current")
_HpnicfDot11CfgRadioType_Type = HpnicfDot11RadioType
_HpnicfDot11CfgRadioType_Object = MibTableColumn
hpnicfDot11CfgRadioType = _HpnicfDot11CfgRadioType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 4),
    _HpnicfDot11CfgRadioType_Type()
)
hpnicfDot11CfgRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgRadioType.setStatus("current")
_HpnicfDot11CfgChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11CfgChannel_Object = MibTableColumn
hpnicfDot11CfgChannel = _HpnicfDot11CfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 5),
    _HpnicfDot11CfgChannel_Type()
)
hpnicfDot11CfgChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgChannel.setStatus("current")
_HpnicfDot11CfgMaxTxPowerLevel_Type = HpnicfDot11TxPwrLevelScopeType
_HpnicfDot11CfgMaxTxPowerLevel_Object = MibTableColumn
hpnicfDot11CfgMaxTxPowerLevel = _HpnicfDot11CfgMaxTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 6),
    _HpnicfDot11CfgMaxTxPowerLevel_Type()
)
hpnicfDot11CfgMaxTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgMaxTxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11CfgMaxTxPowerLevel.setUnits("dbm")


class _HpnicfDot11PreambleLen_Type(HpnicfDot11PreambleType):
    """Custom type hpnicfDot11PreambleLen based on HpnicfDot11PreambleType"""


_HpnicfDot11PreambleLen_Object = MibTableColumn
hpnicfDot11PreambleLen = _HpnicfDot11PreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 7),
    _HpnicfDot11PreambleLen_Type()
)
hpnicfDot11PreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11PreambleLen.setStatus("current")
_HpnicfDot11CfgRadioStatus_Type = TruthValue
_HpnicfDot11CfgRadioStatus_Object = MibTableColumn
hpnicfDot11CfgRadioStatus = _HpnicfDot11CfgRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 8),
    _HpnicfDot11CfgRadioStatus_Type()
)
hpnicfDot11CfgRadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgRadioStatus.setStatus("current")
_HpnicfDot11CfgRdElementID_Type = Unsigned32
_HpnicfDot11CfgRdElementID_Object = MibTableColumn
hpnicfDot11CfgRdElementID = _HpnicfDot11CfgRdElementID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 9),
    _HpnicfDot11CfgRdElementID_Type()
)
hpnicfDot11CfgRdElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CfgRdElementID.setStatus("current")
_HpnicfDot11CfgWorkMode_Type = HpnicfDot11WorkMode
_HpnicfDot11CfgWorkMode_Object = MibTableColumn
hpnicfDot11CfgWorkMode = _HpnicfDot11CfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 10),
    _HpnicfDot11CfgWorkMode_Type()
)
hpnicfDot11CfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgWorkMode.setStatus("current")
_HpnicfDot11CfgPwrAttValue_Type = Integer32
_HpnicfDot11CfgPwrAttValue_Object = MibTableColumn
hpnicfDot11CfgPwrAttValue = _HpnicfDot11CfgPwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 11),
    _HpnicfDot11CfgPwrAttValue_Type()
)
hpnicfDot11CfgPwrAttValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgPwrAttValue.setStatus("current")


class _HpnicfDot11RadioTxArithmetic_Type(Integer32):
    """Custom type hpnicfDot11RadioTxArithmetic based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth", 2),
          ("quality", 1))
    )


_HpnicfDot11RadioTxArithmetic_Type.__name__ = "Integer32"
_HpnicfDot11RadioTxArithmetic_Object = MibTableColumn
hpnicfDot11RadioTxArithmetic = _HpnicfDot11RadioTxArithmetic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 12),
    _HpnicfDot11RadioTxArithmetic_Type()
)
hpnicfDot11RadioTxArithmetic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioTxArithmetic.setStatus("current")


class _HpnicfDot11CfgChannelLockStat_Type(Integer32):
    """Custom type hpnicfDot11CfgChannelLockStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_HpnicfDot11CfgChannelLockStat_Type.__name__ = "Integer32"
_HpnicfDot11CfgChannelLockStat_Object = MibTableColumn
hpnicfDot11CfgChannelLockStat = _HpnicfDot11CfgChannelLockStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 13),
    _HpnicfDot11CfgChannelLockStat_Type()
)
hpnicfDot11CfgChannelLockStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgChannelLockStat.setStatus("current")


class _HpnicfDot11CfgPowerLockStat_Type(Integer32):
    """Custom type hpnicfDot11CfgPowerLockStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_HpnicfDot11CfgPowerLockStat_Type.__name__ = "Integer32"
_HpnicfDot11CfgPowerLockStat_Object = MibTableColumn
hpnicfDot11CfgPowerLockStat = _HpnicfDot11CfgPowerLockStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 14),
    _HpnicfDot11CfgPowerLockStat_Type()
)
hpnicfDot11CfgPowerLockStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgPowerLockStat.setStatus("current")
_HpnicfDot11CfgLBRdGroupId_Type = Unsigned32
_HpnicfDot11CfgLBRdGroupId_Object = MibTableColumn
hpnicfDot11CfgLBRdGroupId = _HpnicfDot11CfgLBRdGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 15),
    _HpnicfDot11CfgLBRdGroupId_Type()
)
hpnicfDot11CfgLBRdGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgLBRdGroupId.setStatus("current")
_HpnicfDot11CfgRRMSDRdGroupId_Type = Unsigned32
_HpnicfDot11CfgRRMSDRdGroupId_Object = MibTableColumn
hpnicfDot11CfgRRMSDRdGroupId = _HpnicfDot11CfgRRMSDRdGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 16),
    _HpnicfDot11CfgRRMSDRdGroupId_Type()
)
hpnicfDot11CfgRRMSDRdGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgRRMSDRdGroupId.setStatus("current")
_HpnicfDot11CfgRadioType2_Type = HpnicfDot11RadioType2
_HpnicfDot11CfgRadioType2_Object = MibTableColumn
hpnicfDot11CfgRadioType2 = _HpnicfDot11CfgRadioType2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 17),
    _HpnicfDot11CfgRadioType2_Type()
)
hpnicfDot11CfgRadioType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgRadioType2.setStatus("current")
_HpnicfDot11CfgIDSEnable_Type = TruthValue
_HpnicfDot11CfgIDSEnable_Object = MibTableColumn
hpnicfDot11CfgIDSEnable = _HpnicfDot11CfgIDSEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 18),
    _HpnicfDot11CfgIDSEnable_Type()
)
hpnicfDot11CfgIDSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgIDSEnable.setStatus("current")
_HpnicfDot11CfgSaEnable_Type = TruthValue
_HpnicfDot11CfgSaEnable_Object = MibTableColumn
hpnicfDot11CfgSaEnable = _HpnicfDot11CfgSaEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 19),
    _HpnicfDot11CfgSaEnable_Type()
)
hpnicfDot11CfgSaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgSaEnable.setStatus("current")
_HpnicfDot11CfgSaCltRtFFTData_Type = TruthValue
_HpnicfDot11CfgSaCltRtFFTData_Object = MibTableColumn
hpnicfDot11CfgSaCltRtFFTData = _HpnicfDot11CfgSaCltRtFFTData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 20),
    _HpnicfDot11CfgSaCltRtFFTData_Type()
)
hpnicfDot11CfgSaCltRtFFTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgSaCltRtFFTData.setStatus("current")


class _HpnicfDot11CfgSaBand_Type(Integer32):
    """Custom type hpnicfDot11CfgSaBand based on Integer32"""
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
        *(("dot11aLower", 2),
          ("dot11aMiddle", 3),
          ("dot11aUpper", 4),
          ("dot11g", 1))
    )


_HpnicfDot11CfgSaBand_Type.__name__ = "Integer32"
_HpnicfDot11CfgSaBand_Object = MibTableColumn
hpnicfDot11CfgSaBand = _HpnicfDot11CfgSaBand_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 2, 1, 21),
    _HpnicfDot11CfgSaBand_Type()
)
hpnicfDot11CfgSaBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11CfgSaBand.setStatus("current")
_HpnicfDot11APServiceSetTable_Object = MibTable
hpnicfDot11APServiceSetTable = _HpnicfDot11APServiceSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11APServiceSetTable.setStatus("current")
_HpnicfDot11APServiceSetEntry_Object = MibTableRow
hpnicfDot11APServiceSetEntry = _HpnicfDot11APServiceSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 3, 1)
)
hpnicfDot11APServiceSetEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11APTemplateNameCfg"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11CfgRadioID"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11CfgServicePolicyID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APServiceSetEntry.setStatus("current")
_HpnicfDot11CfgServicePolicyID_Type = HpnicfDot11ServicePolicyIDType
_HpnicfDot11CfgServicePolicyID_Object = MibTableColumn
hpnicfDot11CfgServicePolicyID = _HpnicfDot11CfgServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 3, 1, 1),
    _HpnicfDot11CfgServicePolicyID_Type()
)
hpnicfDot11CfgServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11CfgServicePolicyID.setStatus("current")
_HpnicfDot11SrvSetRowStatus_Type = RowStatus
_HpnicfDot11SrvSetRowStatus_Object = MibTableColumn
hpnicfDot11SrvSetRowStatus = _HpnicfDot11SrvSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 3, 1, 2),
    _HpnicfDot11SrvSetRowStatus_Type()
)
hpnicfDot11SrvSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SrvSetRowStatus.setStatus("current")


class _HpnicfDot11ServiceSetVlanId_Type(Integer32):
    """Custom type hpnicfDot11ServiceSetVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfDot11ServiceSetVlanId_Type.__name__ = "Integer32"
_HpnicfDot11ServiceSetVlanId_Object = MibTableColumn
hpnicfDot11ServiceSetVlanId = _HpnicfDot11ServiceSetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 3, 1, 3),
    _HpnicfDot11ServiceSetVlanId_Type()
)
hpnicfDot11ServiceSetVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11ServiceSetVlanId.setStatus("current")
_HpnicfDot11APSysInfoSetTable_Object = MibTable
hpnicfDot11APSysInfoSetTable = _HpnicfDot11APSysInfoSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot11APSysInfoSetTable.setStatus("current")
_HpnicfDot11APSysInfoSetEntry_Object = MibTableRow
hpnicfDot11APSysInfoSetEntry = _HpnicfDot11APSysInfoSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 4, 1)
)
hpnicfDot11APSysInfoSetEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11SIDAPSerialID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APSysInfoSetEntry.setStatus("current")


class _HpnicfDot11APSysNetID_Type(OctetString):
    """Custom type hpnicfDot11APSysNetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11APSysNetID_Type.__name__ = "OctetString"
_HpnicfDot11APSysNetID_Object = MibTableColumn
hpnicfDot11APSysNetID = _HpnicfDot11APSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 4, 1, 1),
    _HpnicfDot11APSysNetID_Type()
)
hpnicfDot11APSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APSysNetID.setStatus("current")


class _HpnicfDot11APCpuUsageThreshold_Type(Integer32):
    """Custom type hpnicfDot11APCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11APCpuUsageThreshold_Type.__name__ = "Integer32"
_HpnicfDot11APCpuUsageThreshold_Object = MibTableColumn
hpnicfDot11APCpuUsageThreshold = _HpnicfDot11APCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 4, 1, 2),
    _HpnicfDot11APCpuUsageThreshold_Type()
)
hpnicfDot11APCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APCpuUsageThreshold.setUnits("onepercent")


class _HpnicfDot11APMemUsageThreshold_Type(Integer32):
    """Custom type hpnicfDot11APMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfDot11APMemUsageThreshold_Type.__name__ = "Integer32"
_HpnicfDot11APMemUsageThreshold_Object = MibTableColumn
hpnicfDot11APMemUsageThreshold = _HpnicfDot11APMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 4, 1, 3),
    _HpnicfDot11APMemUsageThreshold_Type()
)
hpnicfDot11APMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APMemUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11APMemUsageThreshold.setUnits("onepercent")
_HpnicfDot11APLimitTable_Object = MibTable
hpnicfDot11APLimitTable = _HpnicfDot11APLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 5)
)
if mibBuilder.loadTexts:
    hpnicfDot11APLimitTable.setStatus("current")
_HpnicfDot11APLimitEntry_Object = MibTableRow
hpnicfDot11APLimitEntry = _HpnicfDot11APLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 5, 1)
)
hpnicfDot11APLimitEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APLimitEntry.setStatus("current")


class _HpnicfDot11APSsidNumLimit_Type(Integer32):
    """Custom type hpnicfDot11APSsidNumLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfDot11APSsidNumLimit_Type.__name__ = "Integer32"
_HpnicfDot11APSsidNumLimit_Object = MibTableColumn
hpnicfDot11APSsidNumLimit = _HpnicfDot11APSsidNumLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 5, 1, 1),
    _HpnicfDot11APSsidNumLimit_Type()
)
hpnicfDot11APSsidNumLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APSsidNumLimit.setStatus("current")


class _HpnicfDot11APUserCntLimit_Type(Integer32):
    """Custom type hpnicfDot11APUserCntLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfDot11APUserCntLimit_Type.__name__ = "Integer32"
_HpnicfDot11APUserCntLimit_Object = MibTableColumn
hpnicfDot11APUserCntLimit = _HpnicfDot11APUserCntLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 5, 1, 2),
    _HpnicfDot11APUserCntLimit_Type()
)
hpnicfDot11APUserCntLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APUserCntLimit.setStatus("current")


class _HpnicfDot11APUserThreshold_Type(Integer32):
    """Custom type hpnicfDot11APUserThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfDot11APUserThreshold_Type.__name__ = "Integer32"
_HpnicfDot11APUserThreshold_Object = MibTableColumn
hpnicfDot11APUserThreshold = _HpnicfDot11APUserThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 5, 1, 3),
    _HpnicfDot11APUserThreshold_Type()
)
hpnicfDot11APUserThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APUserThreshold.setStatus("current")
_HpnicfDot11APIfSetTable_Object = MibTable
hpnicfDot11APIfSetTable = _HpnicfDot11APIfSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 6)
)
if mibBuilder.loadTexts:
    hpnicfDot11APIfSetTable.setStatus("current")
_HpnicfDot11APIfSetEntry_Object = MibTableRow
hpnicfDot11APIfSetEntry = _HpnicfDot11APIfSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 6, 1)
)
hpnicfDot11APIfSetEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11APSetIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APIfSetEntry.setStatus("current")
_HpnicfDot11APSetIfIndex_Type = Integer32
_HpnicfDot11APSetIfIndex_Object = MibTableColumn
hpnicfDot11APSetIfIndex = _HpnicfDot11APSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 6, 1, 1),
    _HpnicfDot11APSetIfIndex_Type()
)
hpnicfDot11APSetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APSetIfIndex.setStatus("current")
_HpnicfDot11APIfAlias_Type = DisplayString
_HpnicfDot11APIfAlias_Object = MibTableColumn
hpnicfDot11APIfAlias = _HpnicfDot11APIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 6, 1, 2),
    _HpnicfDot11APIfAlias_Type()
)
hpnicfDot11APIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11APIfAlias.setStatus("current")
_HpnicfDot11APServiceVlanTable_Object = MibTable
hpnicfDot11APServiceVlanTable = _HpnicfDot11APServiceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 7)
)
if mibBuilder.loadTexts:
    hpnicfDot11APServiceVlanTable.setStatus("current")
_HpnicfDot11APServiceVlanEntry_Object = MibTableRow
hpnicfDot11APServiceVlanEntry = _HpnicfDot11APServiceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 7, 1)
)
hpnicfDot11APServiceVlanEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11APServiceVlanSerialID"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11APServiceVlanSPID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APServiceVlanEntry.setStatus("current")
_HpnicfDot11APServiceVlanSerialID_Type = OctetString
_HpnicfDot11APServiceVlanSerialID_Object = MibTableColumn
hpnicfDot11APServiceVlanSerialID = _HpnicfDot11APServiceVlanSerialID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 7, 1, 1),
    _HpnicfDot11APServiceVlanSerialID_Type()
)
hpnicfDot11APServiceVlanSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APServiceVlanSerialID.setStatus("current")
_HpnicfDot11APServiceVlanSPID_Type = HpnicfDot11ServicePolicyIDType
_HpnicfDot11APServiceVlanSPID_Object = MibTableColumn
hpnicfDot11APServiceVlanSPID = _HpnicfDot11APServiceVlanSPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 7, 1, 2),
    _HpnicfDot11APServiceVlanSPID_Type()
)
hpnicfDot11APServiceVlanSPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APServiceVlanSPID.setStatus("current")


class _HpnicfDot11APServiceVlanId_Type(Integer32):
    """Custom type hpnicfDot11APServiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfDot11APServiceVlanId_Type.__name__ = "Integer32"
_HpnicfDot11APServiceVlanId_Object = MibTableColumn
hpnicfDot11APServiceVlanId = _HpnicfDot11APServiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 7, 1, 3),
    _HpnicfDot11APServiceVlanId_Type()
)
hpnicfDot11APServiceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APServiceVlanId.setStatus("current")
_HpnicfDot11APServiceVlanRowStatus_Type = RowStatus
_HpnicfDot11APServiceVlanRowStatus_Object = MibTableColumn
hpnicfDot11APServiceVlanRowStatus = _HpnicfDot11APServiceVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 7, 1, 4),
    _HpnicfDot11APServiceVlanRowStatus_Type()
)
hpnicfDot11APServiceVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11APServiceVlanRowStatus.setStatus("current")
_HpnicfDot11RadioConfigTable_Object = MibTable
hpnicfDot11RadioConfigTable = _HpnicfDot11RadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioConfigTable.setStatus("current")
_HpnicfDot11RadioConfigEntry_Object = MibTableRow
hpnicfDot11RadioConfigEntry = _HpnicfDot11RadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1)
)
hpnicfDot11RadioConfigEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RCAPSerialID"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RCRadioID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioConfigEntry.setStatus("current")


class _HpnicfDot11RCAPSerialID_Type(OctetString):
    """Custom type hpnicfDot11RCAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11RCAPSerialID_Type.__name__ = "OctetString"
_HpnicfDot11RCAPSerialID_Object = MibTableColumn
hpnicfDot11RCAPSerialID = _HpnicfDot11RCAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 1),
    _HpnicfDot11RCAPSerialID_Type()
)
hpnicfDot11RCAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RCAPSerialID.setStatus("current")
_HpnicfDot11RCRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11RCRadioID_Object = MibTableColumn
hpnicfDot11RCRadioID = _HpnicfDot11RCRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 2),
    _HpnicfDot11RCRadioID_Type()
)
hpnicfDot11RCRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RCRadioID.setStatus("current")
_HpnicfDot11RCRadioType_Type = HpnicfDot11RadioType
_HpnicfDot11RCRadioType_Object = MibTableColumn
hpnicfDot11RCRadioType = _HpnicfDot11RCRadioType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 3),
    _HpnicfDot11RCRadioType_Type()
)
hpnicfDot11RCRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCRadioType.setStatus("current")
_HpnicfDot11RCChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11RCChannel_Object = MibTableColumn
hpnicfDot11RCChannel = _HpnicfDot11RCChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 4),
    _HpnicfDot11RCChannel_Type()
)
hpnicfDot11RCChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCChannel.setStatus("current")


class _HpnicfDot11RCPreambleLen_Type(HpnicfDot11PreambleType):
    """Custom type hpnicfDot11RCPreambleLen based on HpnicfDot11PreambleType"""


_HpnicfDot11RCPreambleLen_Object = MibTableColumn
hpnicfDot11RCPreambleLen = _HpnicfDot11RCPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 5),
    _HpnicfDot11RCPreambleLen_Type()
)
hpnicfDot11RCPreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCPreambleLen.setStatus("current")
_HpnicfDot11RCPwrAttValue_Type = Integer32
_HpnicfDot11RCPwrAttValue_Object = MibTableColumn
hpnicfDot11RCPwrAttValue = _HpnicfDot11RCPwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 6),
    _HpnicfDot11RCPwrAttValue_Type()
)
hpnicfDot11RCPwrAttValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCPwrAttValue.setStatus("current")
_HpnicfDot11RCApPowerLevel_Type = HpnicfDot11TxPwrLevelScopeType
_HpnicfDot11RCApPowerLevel_Object = MibTableColumn
hpnicfDot11RCApPowerLevel = _HpnicfDot11RCApPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 7),
    _HpnicfDot11RCApPowerLevel_Type()
)
hpnicfDot11RCApPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCApPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RCApPowerLevel.setUnits("dbm")
_HpnicfDot11RCDynamicChlState_Type = TruthValue
_HpnicfDot11RCDynamicChlState_Object = MibTableColumn
hpnicfDot11RCDynamicChlState = _HpnicfDot11RCDynamicChlState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 8),
    _HpnicfDot11RCDynamicChlState_Type()
)
hpnicfDot11RCDynamicChlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCDynamicChlState.setStatus("current")
_HpnicfDot11RCDynamicPowerState_Type = TruthValue
_HpnicfDot11RCDynamicPowerState_Object = MibTableColumn
hpnicfDot11RCDynamicPowerState = _HpnicfDot11RCDynamicPowerState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 9),
    _HpnicfDot11RCDynamicPowerState_Type()
)
hpnicfDot11RCDynamicPowerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCDynamicPowerState.setStatus("current")
_HpnicfDot11RCRadioStatus_Type = TruthValue
_HpnicfDot11RCRadioStatus_Object = MibTableColumn
hpnicfDot11RCRadioStatus = _HpnicfDot11RCRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 10),
    _HpnicfDot11RCRadioStatus_Type()
)
hpnicfDot11RCRadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCRadioStatus.setStatus("current")


class _HpnicfDot11RCRadioRate_Type(OctetString):
    """Custom type hpnicfDot11RCRadioRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDot11RCRadioRate_Type.__name__ = "OctetString"
_HpnicfDot11RCRadioRate_Object = MibTableColumn
hpnicfDot11RCRadioRate = _HpnicfDot11RCRadioRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 11),
    _HpnicfDot11RCRadioRate_Type()
)
hpnicfDot11RCRadioRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCRadioRate.setStatus("current")
_HpnicfDot11RCPwrAdjustStepLength_Type = Integer32
_HpnicfDot11RCPwrAdjustStepLength_Object = MibTableColumn
hpnicfDot11RCPwrAdjustStepLength = _HpnicfDot11RCPwrAdjustStepLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 12),
    _HpnicfDot11RCPwrAdjustStepLength_Type()
)
hpnicfDot11RCPwrAdjustStepLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RCPwrAdjustStepLength.setStatus("current")
_HpnicfDot11RCRadioType2_Type = HpnicfDot11RadioType2
_HpnicfDot11RCRadioType2_Object = MibTableColumn
hpnicfDot11RCRadioType2 = _HpnicfDot11RCRadioType2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 13),
    _HpnicfDot11RCRadioType2_Type()
)
hpnicfDot11RCRadioType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCRadioType2.setStatus("current")


class _HpnicfDot11RCPreambleLenCM_Type(Integer32):
    """Custom type hpnicfDot11RCPreambleLenCM based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("long", 0),
          ("short", 1))
    )


_HpnicfDot11RCPreambleLenCM_Type.__name__ = "Integer32"
_HpnicfDot11RCPreambleLenCM_Object = MibTableColumn
hpnicfDot11RCPreambleLenCM = _HpnicfDot11RCPreambleLenCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 14),
    _HpnicfDot11RCPreambleLenCM_Type()
)
hpnicfDot11RCPreambleLenCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCPreambleLenCM.setStatus("current")


class _HpnicfDot11RCDynamicChlStateCM_Type(Integer32):
    """Custom type hpnicfDot11RCDynamicChlStateCM based on Integer32"""
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


_HpnicfDot11RCDynamicChlStateCM_Type.__name__ = "Integer32"
_HpnicfDot11RCDynamicChlStateCM_Object = MibTableColumn
hpnicfDot11RCDynamicChlStateCM = _HpnicfDot11RCDynamicChlStateCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 15),
    _HpnicfDot11RCDynamicChlStateCM_Type()
)
hpnicfDot11RCDynamicChlStateCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCDynamicChlStateCM.setStatus("current")


class _HpnicfDot11RCRadioStatusCM_Type(Integer32):
    """Custom type hpnicfDot11RCRadioStatusCM based on Integer32"""
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


_HpnicfDot11RCRadioStatusCM_Type.__name__ = "Integer32"
_HpnicfDot11RCRadioStatusCM_Object = MibTableColumn
hpnicfDot11RCRadioStatusCM = _HpnicfDot11RCRadioStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 16),
    _HpnicfDot11RCRadioStatusCM_Type()
)
hpnicfDot11RCRadioStatusCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCRadioStatusCM.setStatus("current")


class _HpnicfDot11RCRadioRateCM_Type(OctetString):
    """Custom type hpnicfDot11RCRadioRateCM based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDot11RCRadioRateCM_Type.__name__ = "OctetString"
_HpnicfDot11RCRadioRateCM_Object = MibTableColumn
hpnicfDot11RCRadioRateCM = _HpnicfDot11RCRadioRateCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 17),
    _HpnicfDot11RCRadioRateCM_Type()
)
hpnicfDot11RCRadioRateCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCRadioRateCM.setStatus("current")
_HpnicfDot11RCDynamicPowerStateCM_Type = HpnicfDot11TruthValueCM
_HpnicfDot11RCDynamicPowerStateCM_Object = MibTableColumn
hpnicfDot11RCDynamicPowerStateCM = _HpnicfDot11RCDynamicPowerStateCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 8, 1, 18),
    _HpnicfDot11RCDynamicPowerStateCM_Type()
)
hpnicfDot11RCDynamicPowerStateCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RCDynamicPowerStateCM.setStatus("current")
_HpnicfDot11RadioSSIDCfgTable_Object = MibTable
hpnicfDot11RadioSSIDCfgTable = _HpnicfDot11RadioSSIDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 9)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioSSIDCfgTable.setStatus("current")
_HpnicfDot11RadioSSIDCfgEntry_Object = MibTableRow
hpnicfDot11RadioSSIDCfgEntry = _HpnicfDot11RadioSSIDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 9, 1)
)
hpnicfDot11RadioSSIDCfgEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RadioSSIDSerialID"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RadioSSIDRadioID"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RadioSSIDWLANID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioSSIDCfgEntry.setStatus("current")
_HpnicfDot11RadioSSIDSerialID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11RadioSSIDSerialID_Object = MibTableColumn
hpnicfDot11RadioSSIDSerialID = _HpnicfDot11RadioSSIDSerialID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 9, 1, 1),
    _HpnicfDot11RadioSSIDSerialID_Type()
)
hpnicfDot11RadioSSIDSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RadioSSIDSerialID.setStatus("current")
_HpnicfDot11RadioSSIDRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11RadioSSIDRadioID_Object = MibTableColumn
hpnicfDot11RadioSSIDRadioID = _HpnicfDot11RadioSSIDRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 9, 1, 2),
    _HpnicfDot11RadioSSIDRadioID_Type()
)
hpnicfDot11RadioSSIDRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RadioSSIDRadioID.setStatus("current")
_HpnicfDot11RadioSSIDWLANID_Type = Integer32
_HpnicfDot11RadioSSIDWLANID_Object = MibTableColumn
hpnicfDot11RadioSSIDWLANID = _HpnicfDot11RadioSSIDWLANID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 9, 1, 3),
    _HpnicfDot11RadioSSIDWLANID_Type()
)
hpnicfDot11RadioSSIDWLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RadioSSIDWLANID.setStatus("current")
_HpnicfDot11RadioSSIDIndex_Type = HpnicfDot11ServicePolicyIDType
_HpnicfDot11RadioSSIDIndex_Object = MibTableColumn
hpnicfDot11RadioSSIDIndex = _HpnicfDot11RadioSSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 9, 1, 4),
    _HpnicfDot11RadioSSIDIndex_Type()
)
hpnicfDot11RadioSSIDIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11RadioSSIDIndex.setStatus("current")
_HpnicfDot11RadioBSSID_Type = MacAddress
_HpnicfDot11RadioBSSID_Object = MibTableColumn
hpnicfDot11RadioBSSID = _HpnicfDot11RadioBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 9, 1, 5),
    _HpnicfDot11RadioBSSID_Type()
)
hpnicfDot11RadioBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioBSSID.setStatus("current")
_HpnicfDot11RadioSSIDRowStatus_Type = RowStatus
_HpnicfDot11RadioSSIDRowStatus_Object = MibTableColumn
hpnicfDot11RadioSSIDRowStatus = _HpnicfDot11RadioSSIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 9, 1, 6),
    _HpnicfDot11RadioSSIDRowStatus_Type()
)
hpnicfDot11RadioSSIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11RadioSSIDRowStatus.setStatus("current")
_HpnicfDot11APSerialIDTable_Object = MibTable
hpnicfDot11APSerialIDTable = _HpnicfDot11APSerialIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10)
)
if mibBuilder.loadTexts:
    hpnicfDot11APSerialIDTable.setStatus("current")
_HpnicfDot11APSerialIDEntry_Object = MibTableRow
hpnicfDot11APSerialIDEntry = _HpnicfDot11APSerialIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1)
)
hpnicfDot11APSerialIDEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11SIDAPSerialID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APSerialIDEntry.setStatus("current")
_HpnicfDot11SIDAPSerialID_Type = OctetString
_HpnicfDot11SIDAPSerialID_Object = MibTableColumn
hpnicfDot11SIDAPSerialID = _HpnicfDot11SIDAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 1),
    _HpnicfDot11SIDAPSerialID_Type()
)
hpnicfDot11SIDAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPSerialID.setStatus("current")


class _HpnicfDot11SIDAPWorkMode_Type(Integer32):
    """Custom type hpnicfDot11SIDAPWorkMode based on Integer32"""
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
        *(("hybrid", 3),
          ("monitor", 2),
          ("normal", 1))
    )


_HpnicfDot11SIDAPWorkMode_Type.__name__ = "Integer32"
_HpnicfDot11SIDAPWorkMode_Object = MibTableColumn
hpnicfDot11SIDAPWorkMode = _HpnicfDot11SIDAPWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 2),
    _HpnicfDot11SIDAPWorkMode_Type()
)
hpnicfDot11SIDAPWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPWorkMode.setStatus("current")


class _HpnicfDot11SIDAPGetIPMethod_Type(Integer32):
    """Custom type hpnicfDot11SIDAPGetIPMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpAlloc", 1),
          ("static", 2))
    )


_HpnicfDot11SIDAPGetIPMethod_Type.__name__ = "Integer32"
_HpnicfDot11SIDAPGetIPMethod_Object = MibTableColumn
hpnicfDot11SIDAPGetIPMethod = _HpnicfDot11SIDAPGetIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 3),
    _HpnicfDot11SIDAPGetIPMethod_Type()
)
hpnicfDot11SIDAPGetIPMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPGetIPMethod.setStatus("current")
_HpnicfDot11SIDAPTemplateName_Type = OctetString
_HpnicfDot11SIDAPTemplateName_Object = MibTableColumn
hpnicfDot11SIDAPTemplateName = _HpnicfDot11SIDAPTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 4),
    _HpnicfDot11SIDAPTemplateName_Type()
)
hpnicfDot11SIDAPTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPTemplateName.setStatus("current")
_HpnicfDot11SIDModelAlias_Type = OctetString
_HpnicfDot11SIDModelAlias_Object = MibTableColumn
hpnicfDot11SIDModelAlias = _HpnicfDot11SIDModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 5),
    _HpnicfDot11SIDModelAlias_Type()
)
hpnicfDot11SIDModelAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDModelAlias.setStatus("current")
_HpnicfDot11SIDAPDescription_Type = OctetString
_HpnicfDot11SIDAPDescription_Object = MibTableColumn
hpnicfDot11SIDAPDescription = _HpnicfDot11SIDAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 6),
    _HpnicfDot11SIDAPDescription_Type()
)
hpnicfDot11SIDAPDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPDescription.setStatus("current")
_HpnicfDot11SIDRowStatus_Type = RowStatus
_HpnicfDot11SIDRowStatus_Object = MibTableColumn
hpnicfDot11SIDRowStatus = _HpnicfDot11SIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 7),
    _HpnicfDot11SIDRowStatus_Type()
)
hpnicfDot11SIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDRowStatus.setStatus("current")
_HpnicfDot11SIDAPName_Type = OctetString
_HpnicfDot11SIDAPName_Object = MibTableColumn
hpnicfDot11SIDAPName = _HpnicfDot11SIDAPName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 8),
    _HpnicfDot11SIDAPName_Type()
)
hpnicfDot11SIDAPName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPName.setStatus("current")
_HpnicfDot11SIDStatisInterv_Type = Integer32
_HpnicfDot11SIDStatisInterv_Object = MibTableColumn
hpnicfDot11SIDStatisInterv = _HpnicfDot11SIDStatisInterv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 9),
    _HpnicfDot11SIDStatisInterv_Type()
)
hpnicfDot11SIDStatisInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDStatisInterv.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11SIDStatisInterv.setUnits("second")


class _HpnicfDot11SIDAPBroadcastProbeReply_Type(TruthValue):
    """Custom type hpnicfDot11SIDAPBroadcastProbeReply based on TruthValue"""


_HpnicfDot11SIDAPBroadcastProbeReply_Object = MibTableColumn
hpnicfDot11SIDAPBroadcastProbeReply = _HpnicfDot11SIDAPBroadcastProbeReply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 10),
    _HpnicfDot11SIDAPBroadcastProbeReply_Type()
)
hpnicfDot11SIDAPBroadcastProbeReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPBroadcastProbeReply.setStatus("current")
_HpnicfDot11SIDAPStaIdleTimerInterv_Type = Integer32
_HpnicfDot11SIDAPStaIdleTimerInterv_Object = MibTableColumn
hpnicfDot11SIDAPStaIdleTimerInterv = _HpnicfDot11SIDAPStaIdleTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 11),
    _HpnicfDot11SIDAPStaIdleTimerInterv_Type()
)
hpnicfDot11SIDAPStaIdleTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPStaIdleTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPStaIdleTimerInterv.setUnits("second")
_HpnicfDot11SIDStaKeepAliveTimerInterv_Type = Integer32
_HpnicfDot11SIDStaKeepAliveTimerInterv_Object = MibTableColumn
hpnicfDot11SIDStaKeepAliveTimerInterv = _HpnicfDot11SIDStaKeepAliveTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 12),
    _HpnicfDot11SIDStaKeepAliveTimerInterv_Type()
)
hpnicfDot11SIDStaKeepAliveTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDStaKeepAliveTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11SIDStaKeepAliveTimerInterv.setUnits("second")
_HpnicfDot11SIDAPCir_Type = Integer32
_HpnicfDot11SIDAPCir_Object = MibTableColumn
hpnicfDot11SIDAPCir = _HpnicfDot11SIDAPCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 13),
    _HpnicfDot11SIDAPCir_Type()
)
hpnicfDot11SIDAPCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPCir.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPCir.setUnits("Kbps")
_HpnicfDot11SIDAPCbs_Type = Integer32
_HpnicfDot11SIDAPCbs_Object = MibTableColumn
hpnicfDot11SIDAPCbs = _HpnicfDot11SIDAPCbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 14),
    _HpnicfDot11SIDAPCbs_Type()
)
hpnicfDot11SIDAPCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPCbs.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPCbs.setUnits("Bytes")


class _HpnicfDot11SIDAPPriorityLevel_Type(Integer32):
    """Custom type hpnicfDot11SIDAPPriorityLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfDot11SIDAPPriorityLevel_Type.__name__ = "Integer32"
_HpnicfDot11SIDAPPriorityLevel_Object = MibTableColumn
hpnicfDot11SIDAPPriorityLevel = _HpnicfDot11SIDAPPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 15),
    _HpnicfDot11SIDAPPriorityLevel_Type()
)
hpnicfDot11SIDAPPriorityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPPriorityLevel.setStatus("current")
_HpnicfDot11SIDAPElementID_Type = Integer32
_HpnicfDot11SIDAPElementID_Object = MibTableColumn
hpnicfDot11SIDAPElementID = _HpnicfDot11SIDAPElementID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 16),
    _HpnicfDot11SIDAPElementID_Type()
)
hpnicfDot11SIDAPElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPElementID.setStatus("current")


class _HpnicfDot11SIDAPDevDetectEnable_Type(TruthValue):
    """Custom type hpnicfDot11SIDAPDevDetectEnable based on TruthValue"""


_HpnicfDot11SIDAPDevDetectEnable_Object = MibTableColumn
hpnicfDot11SIDAPDevDetectEnable = _HpnicfDot11SIDAPDevDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 17),
    _HpnicfDot11SIDAPDevDetectEnable_Type()
)
hpnicfDot11SIDAPDevDetectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPDevDetectEnable.setStatus("current")


class _HpnicfDot11SIDAPStatisIntervMode_Type(Integer32):
    """Custom type hpnicfDot11SIDAPStatisIntervMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("realtime", 2))
    )


_HpnicfDot11SIDAPStatisIntervMode_Type.__name__ = "Integer32"
_HpnicfDot11SIDAPStatisIntervMode_Object = MibTableColumn
hpnicfDot11SIDAPStatisIntervMode = _HpnicfDot11SIDAPStatisIntervMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 18),
    _HpnicfDot11SIDAPStatisIntervMode_Type()
)
hpnicfDot11SIDAPStatisIntervMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPStatisIntervMode.setStatus("current")


class _HpnicfDot11SIDAPWorkModeCM_Type(Integer32):
    """Custom type hpnicfDot11SIDAPWorkModeCM based on Integer32"""
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
        *(("monitor", 1),
          ("normal", 0),
          ("semimonitor", 2))
    )


_HpnicfDot11SIDAPWorkModeCM_Type.__name__ = "Integer32"
_HpnicfDot11SIDAPWorkModeCM_Object = MibTableColumn
hpnicfDot11SIDAPWorkModeCM = _HpnicfDot11SIDAPWorkModeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 10, 1, 19),
    _HpnicfDot11SIDAPWorkModeCM_Type()
)
hpnicfDot11SIDAPWorkModeCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11SIDAPWorkModeCM.setStatus("current")
_HpnicfDot11APSTVlanTable_Object = MibTable
hpnicfDot11APSTVlanTable = _HpnicfDot11APSTVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 11)
)
if mibBuilder.loadTexts:
    hpnicfDot11APSTVlanTable.setStatus("current")
_HpnicfDot11APSTVlanEntry_Object = MibTableRow
hpnicfDot11APSTVlanEntry = _HpnicfDot11APSTVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 11, 1)
)
hpnicfDot11APSTVlanEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11SIDAPSerialID"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11CfgRadioID"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11CfgServicePolicyID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APSTVlanEntry.setStatus("current")


class _HpnicfDot11CfgSTVLANID_Type(Integer32):
    """Custom type hpnicfDot11CfgSTVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfDot11CfgSTVLANID_Type.__name__ = "Integer32"
_HpnicfDot11CfgSTVLANID_Object = MibTableColumn
hpnicfDot11CfgSTVLANID = _HpnicfDot11CfgSTVLANID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 11, 1, 1),
    _HpnicfDot11CfgSTVLANID_Type()
)
hpnicfDot11CfgSTVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11CfgSTVLANID.setStatus("current")


class _HpnicfDot11CfgSTNASPortID_Type(OctetString):
    """Custom type hpnicfDot11CfgSTNASPortID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11CfgSTNASPortID_Type.__name__ = "OctetString"
_HpnicfDot11CfgSTNASPortID_Object = MibTableColumn
hpnicfDot11CfgSTNASPortID = _HpnicfDot11CfgSTNASPortID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 11, 1, 2),
    _HpnicfDot11CfgSTNASPortID_Type()
)
hpnicfDot11CfgSTNASPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CfgSTNASPortID.setStatus("current")
_HpnicfDot11CfgServiceSetRowStatus_Type = RowStatus
_HpnicfDot11CfgServiceSetRowStatus_Object = MibTableColumn
hpnicfDot11CfgServiceSetRowStatus = _HpnicfDot11CfgServiceSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 11, 1, 3),
    _HpnicfDot11CfgServiceSetRowStatus_Type()
)
hpnicfDot11CfgServiceSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11CfgServiceSetRowStatus.setStatus("current")


class _HpnicfDot11CfgSTNASID_Type(OctetString):
    """Custom type hpnicfDot11CfgSTNASID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11CfgSTNASID_Type.__name__ = "OctetString"
_HpnicfDot11CfgSTNASID_Object = MibTableColumn
hpnicfDot11CfgSTNASID = _HpnicfDot11CfgSTNASID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 3, 11, 1, 4),
    _HpnicfDot11CfgSTNASID_Type()
)
hpnicfDot11CfgSTNASID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CfgSTNASID.setStatus("current")
_HpnicfDot11RadioIntfConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11RadioIntfConfigGroup = _HpnicfDot11RadioIntfConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4)
)
_HpnicfDot11RadioIntfConfigTable_Object = MibTable
hpnicfDot11RadioIntfConfigTable = _HpnicfDot11RadioIntfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioIntfConfigTable.setStatus("current")
_HpnicfDot11RadioIntfConfigEntry_Object = MibTableRow
hpnicfDot11RadioIntfConfigEntry = _HpnicfDot11RadioIntfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1)
)
hpnicfDot11RadioIntfConfigEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RadioIfIdx"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioIntfConfigEntry.setStatus("current")
_HpnicfDot11RadioIfIdx_Type = Integer32
_HpnicfDot11RadioIfIdx_Object = MibTableColumn
hpnicfDot11RadioIfIdx = _HpnicfDot11RadioIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 1),
    _HpnicfDot11RadioIfIdx_Type()
)
hpnicfDot11RadioIfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RadioIfIdx.setStatus("current")


class _HpnicfDot11RadioCfgBeaconIntvl_Type(Integer32):
    """Custom type hpnicfDot11RadioCfgBeaconIntvl based on Integer32"""
    defaultValue = 100


_HpnicfDot11RadioCfgBeaconIntvl_Object = MibTableColumn
hpnicfDot11RadioCfgBeaconIntvl = _HpnicfDot11RadioCfgBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 2),
    _HpnicfDot11RadioCfgBeaconIntvl_Type()
)
hpnicfDot11RadioCfgBeaconIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgBeaconIntvl.setUnits("TU")


class _HpnicfDot11RadioCfgDtimIntvl_Type(Integer32):
    """Custom type hpnicfDot11RadioCfgDtimIntvl based on Integer32"""
    defaultValue = 1


_HpnicfDot11RadioCfgDtimIntvl_Object = MibTableColumn
hpnicfDot11RadioCfgDtimIntvl = _HpnicfDot11RadioCfgDtimIntvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 3),
    _HpnicfDot11RadioCfgDtimIntvl_Type()
)
hpnicfDot11RadioCfgDtimIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgDtimIntvl.setStatus("current")


class _HpnicfDot11RadioCfgRtsThreshold_Type(Integer32):
    """Custom type hpnicfDot11RadioCfgRtsThreshold based on Integer32"""
    defaultValue = 2346


_HpnicfDot11RadioCfgRtsThreshold_Object = MibTableColumn
hpnicfDot11RadioCfgRtsThreshold = _HpnicfDot11RadioCfgRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 4),
    _HpnicfDot11RadioCfgRtsThreshold_Type()
)
hpnicfDot11RadioCfgRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgRtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgRtsThreshold.setUnits("Byte")


class _HpnicfDot11RadioCfgFragThreshold_Type(Integer32):
    """Custom type hpnicfDot11RadioCfgFragThreshold based on Integer32"""
    defaultValue = 2346


_HpnicfDot11RadioCfgFragThreshold_Object = MibTableColumn
hpnicfDot11RadioCfgFragThreshold = _HpnicfDot11RadioCfgFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 5),
    _HpnicfDot11RadioCfgFragThreshold_Type()
)
hpnicfDot11RadioCfgFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgFragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgFragThreshold.setUnits("Byte")


class _HpnicfDot11RadioCfgShtRetryThld_Type(Integer32):
    """Custom type hpnicfDot11RadioCfgShtRetryThld based on Integer32"""
    defaultValue = 5


_HpnicfDot11RadioCfgShtRetryThld_Object = MibTableColumn
hpnicfDot11RadioCfgShtRetryThld = _HpnicfDot11RadioCfgShtRetryThld_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 6),
    _HpnicfDot11RadioCfgShtRetryThld_Type()
)
hpnicfDot11RadioCfgShtRetryThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgShtRetryThld.setStatus("current")


class _HpnicfDot11RadioCfglongRtrThld_Type(Integer32):
    """Custom type hpnicfDot11RadioCfglongRtrThld based on Integer32"""
    defaultValue = 5


_HpnicfDot11RadioCfglongRtrThld_Object = MibTableColumn
hpnicfDot11RadioCfglongRtrThld = _HpnicfDot11RadioCfglongRtrThld_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 7),
    _HpnicfDot11RadioCfglongRtrThld_Type()
)
hpnicfDot11RadioCfglongRtrThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfglongRtrThld.setStatus("current")


class _HpnicfDot11RadioCfgMaxRxLifetime_Type(Unsigned32):
    """Custom type hpnicfDot11RadioCfgMaxRxLifetime based on Unsigned32"""
    defaultValue = 2000


_HpnicfDot11RadioCfgMaxRxLifetime_Object = MibTableColumn
hpnicfDot11RadioCfgMaxRxLifetime = _HpnicfDot11RadioCfgMaxRxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 8),
    _HpnicfDot11RadioCfgMaxRxLifetime_Type()
)
hpnicfDot11RadioCfgMaxRxLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgMaxRxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgMaxRxLifetime.setUnits("millisecond")
_HpnicfDot11RadioCfgType_Type = HpnicfDot11RadioType
_HpnicfDot11RadioCfgType_Object = MibTableColumn
hpnicfDot11RadioCfgType = _HpnicfDot11RadioCfgType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 9),
    _HpnicfDot11RadioCfgType_Type()
)
hpnicfDot11RadioCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgType.setStatus("current")


class _HpnicfDot11RadioCfgChannel_Type(HpnicfDot11ChannelScopeType):
    """Custom type hpnicfDot11RadioCfgChannel based on HpnicfDot11ChannelScopeType"""
    defaultValue = 1


_HpnicfDot11RadioCfgChannel_Object = MibTableColumn
hpnicfDot11RadioCfgChannel = _HpnicfDot11RadioCfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 10),
    _HpnicfDot11RadioCfgChannel_Type()
)
hpnicfDot11RadioCfgChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgChannel.setStatus("current")
_HpnicfDot11RadioCfgMaxTxPwrLvl_Type = HpnicfDot11TxPwrLevelScopeType
_HpnicfDot11RadioCfgMaxTxPwrLvl_Object = MibTableColumn
hpnicfDot11RadioCfgMaxTxPwrLvl = _HpnicfDot11RadioCfgMaxTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 11),
    _HpnicfDot11RadioCfgMaxTxPwrLvl_Type()
)
hpnicfDot11RadioCfgMaxTxPwrLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgMaxTxPwrLvl.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgMaxTxPwrLvl.setUnits("dbm")


class _HpnicfDot11RadioCfgPreambleLen_Type(HpnicfDot11PreambleType):
    """Custom type hpnicfDot11RadioCfgPreambleLen based on HpnicfDot11PreambleType"""


_HpnicfDot11RadioCfgPreambleLen_Object = MibTableColumn
hpnicfDot11RadioCfgPreambleLen = _HpnicfDot11RadioCfgPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 12),
    _HpnicfDot11RadioCfgPreambleLen_Type()
)
hpnicfDot11RadioCfgPreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgPreambleLen.setStatus("current")
_HpnicfDot11RadioCfgWorkMode_Type = HpnicfDot11WorkMode
_HpnicfDot11RadioCfgWorkMode_Object = MibTableColumn
hpnicfDot11RadioCfgWorkMode = _HpnicfDot11RadioCfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 13),
    _HpnicfDot11RadioCfgWorkMode_Type()
)
hpnicfDot11RadioCfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgWorkMode.setStatus("current")


class _HpnicfDot11RadioCfgOnly11gEnable_Type(TruthValue):
    """Custom type hpnicfDot11RadioCfgOnly11gEnable based on TruthValue"""


_HpnicfDot11RadioCfgOnly11gEnable_Object = MibTableColumn
hpnicfDot11RadioCfgOnly11gEnable = _HpnicfDot11RadioCfgOnly11gEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 14),
    _HpnicfDot11RadioCfgOnly11gEnable_Type()
)
hpnicfDot11RadioCfgOnly11gEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgOnly11gEnable.setStatus("current")
_HpnicfDot11RadioCfgType2_Type = HpnicfDot11RadioType2
_HpnicfDot11RadioCfgType2_Object = MibTableColumn
hpnicfDot11RadioCfgType2 = _HpnicfDot11RadioCfgType2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 15),
    _HpnicfDot11RadioCfgType2_Type()
)
hpnicfDot11RadioCfgType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgType2.setStatus("current")


class _HpnicfDot11RadioCfgRssithresholdCM_Type(Integer32):
    """Custom type hpnicfDot11RadioCfgRssithresholdCM based on Integer32"""
    defaultValue = 1


_HpnicfDot11RadioCfgRssithresholdCM_Object = MibTableColumn
hpnicfDot11RadioCfgRssithresholdCM = _HpnicfDot11RadioCfgRssithresholdCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 1, 1, 16),
    _HpnicfDot11RadioCfgRssithresholdCM_Type()
)
hpnicfDot11RadioCfgRssithresholdCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgRssithresholdCM.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11RadioCfgRssithresholdCM.setUnits("dBm")
_HpnicfDot11RadioIntfBindTable_Object = MibTable
hpnicfDot11RadioIntfBindTable = _HpnicfDot11RadioIntfBindTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioIntfBindTable.setStatus("current")
_HpnicfDot11RadioIntfBindEntry_Object = MibTableRow
hpnicfDot11RadioIntfBindEntry = _HpnicfDot11RadioIntfBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 2, 1)
)
hpnicfDot11RadioIntfBindEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RadioIfIdx"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RadioIntfBindSvcPlcyID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioIntfBindEntry.setStatus("current")
_HpnicfDot11RadioIntfBindSvcPlcyID_Type = HpnicfDot11ServicePolicyIDType
_HpnicfDot11RadioIntfBindSvcPlcyID_Object = MibTableColumn
hpnicfDot11RadioIntfBindSvcPlcyID = _HpnicfDot11RadioIntfBindSvcPlcyID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 2, 1, 1),
    _HpnicfDot11RadioIntfBindSvcPlcyID_Type()
)
hpnicfDot11RadioIntfBindSvcPlcyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RadioIntfBindSvcPlcyID.setStatus("current")
_HpnicfDot11RadioIntfBindIfIdx_Type = Unsigned32
_HpnicfDot11RadioIntfBindIfIdx_Object = MibTableColumn
hpnicfDot11RadioIntfBindIfIdx = _HpnicfDot11RadioIntfBindIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 2, 1, 2),
    _HpnicfDot11RadioIntfBindIfIdx_Type()
)
hpnicfDot11RadioIntfBindIfIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11RadioIntfBindIfIdx.setStatus("current")
_HpnicfDot11RadioIntfBindRowStatus_Type = RowStatus
_HpnicfDot11RadioIntfBindRowStatus_Object = MibTableColumn
hpnicfDot11RadioIntfBindRowStatus = _HpnicfDot11RadioIntfBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 4, 2, 1, 3),
    _HpnicfDot11RadioIntfBindRowStatus_Type()
)
hpnicfDot11RadioIntfBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11RadioIntfBindRowStatus.setStatus("current")
_HpnicfDot11DataRateConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11DataRateConfigGroup = _HpnicfDot11DataRateConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 5)
)
_HpnicfDot11DataRateConfigTable_Object = MibTable
hpnicfDot11DataRateConfigTable = _HpnicfDot11DataRateConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11DataRateConfigTable.setStatus("current")
_HpnicfDot11DataRateConfigEntry_Object = MibTableRow
hpnicfDot11DataRateConfigEntry = _HpnicfDot11DataRateConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 5, 1, 1)
)
hpnicfDot11DataRateConfigEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RadioTypeID"),
)
if mibBuilder.loadTexts:
    hpnicfDot11DataRateConfigEntry.setStatus("current")
_HpnicfDot11RadioTypeID_Type = HpnicfDot11RadioType
_HpnicfDot11RadioTypeID_Object = MibTableColumn
hpnicfDot11RadioTypeID = _HpnicfDot11RadioTypeID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 5, 1, 1, 1),
    _HpnicfDot11RadioTypeID_Type()
)
hpnicfDot11RadioTypeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RadioTypeID.setStatus("current")


class _HpnicfDot11SupportedRateSet_Type(OctetString):
    """Custom type hpnicfDot11SupportedRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDot11SupportedRateSet_Type.__name__ = "OctetString"
_HpnicfDot11SupportedRateSet_Object = MibTableColumn
hpnicfDot11SupportedRateSet = _HpnicfDot11SupportedRateSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 5, 1, 1, 2),
    _HpnicfDot11SupportedRateSet_Type()
)
hpnicfDot11SupportedRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SupportedRateSet.setStatus("current")


class _HpnicfDot11MandatoryRateSet_Type(OctetString):
    """Custom type hpnicfDot11MandatoryRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDot11MandatoryRateSet_Type.__name__ = "OctetString"
_HpnicfDot11MandatoryRateSet_Object = MibTableColumn
hpnicfDot11MandatoryRateSet = _HpnicfDot11MandatoryRateSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 5, 1, 1, 3),
    _HpnicfDot11MandatoryRateSet_Type()
)
hpnicfDot11MandatoryRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11MandatoryRateSet.setStatus("current")


class _HpnicfDot11DisabledRateSet_Type(OctetString):
    """Custom type hpnicfDot11DisabledRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDot11DisabledRateSet_Type.__name__ = "OctetString"
_HpnicfDot11DisabledRateSet_Object = MibTableColumn
hpnicfDot11DisabledRateSet = _HpnicfDot11DisabledRateSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 5, 1, 1, 4),
    _HpnicfDot11DisabledRateSet_Type()
)
hpnicfDot11DisabledRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11DisabledRateSet.setStatus("current")


class _HpnicfDot11SmartRateSet_Type(OctetString):
    """Custom type hpnicfDot11SmartRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDot11SmartRateSet_Type.__name__ = "OctetString"
_HpnicfDot11SmartRateSet_Object = MibTableColumn
hpnicfDot11SmartRateSet = _HpnicfDot11SmartRateSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 5, 1, 1, 5),
    _HpnicfDot11SmartRateSet_Type()
)
hpnicfDot11SmartRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SmartRateSet.setStatus("current")
_HpnicfDot11InterfaceConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11InterfaceConfigGroup = _HpnicfDot11InterfaceConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6)
)
_HpnicfDot11WlanEssIfTable_Object = MibTable
hpnicfDot11WlanEssIfTable = _HpnicfDot11WlanEssIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11WlanEssIfTable.setStatus("current")
_HpnicfDot11WlanEssIfEntry_Object = MibTableRow
hpnicfDot11WlanEssIfEntry = _HpnicfDot11WlanEssIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 1, 1)
)
hpnicfDot11WlanEssIfEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11WlanEssIfNumber"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WlanEssIfEntry.setStatus("current")
_HpnicfDot11WlanEssIfNumber_Type = Integer32
_HpnicfDot11WlanEssIfNumber_Object = MibTableColumn
hpnicfDot11WlanEssIfNumber = _HpnicfDot11WlanEssIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 1, 1, 1),
    _HpnicfDot11WlanEssIfNumber_Type()
)
hpnicfDot11WlanEssIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WlanEssIfNumber.setStatus("current")
_HpnicfDot11WlanEssIfIndex_Type = Integer32
_HpnicfDot11WlanEssIfIndex_Object = MibTableColumn
hpnicfDot11WlanEssIfIndex = _HpnicfDot11WlanEssIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 1, 1, 2),
    _HpnicfDot11WlanEssIfIndex_Type()
)
hpnicfDot11WlanEssIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WlanEssIfIndex.setStatus("current")
_HpnicfDot11WlanEssRowStatus_Type = RowStatus
_HpnicfDot11WlanEssRowStatus_Object = MibTableColumn
hpnicfDot11WlanEssRowStatus = _HpnicfDot11WlanEssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 1, 1, 3),
    _HpnicfDot11WlanEssRowStatus_Type()
)
hpnicfDot11WlanEssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11WlanEssRowStatus.setStatus("current")
_HpnicfDot11WlanBssIfTable_Object = MibTable
hpnicfDot11WlanBssIfTable = _HpnicfDot11WlanBssIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11WlanBssIfTable.setStatus("current")
_HpnicfDot11WlanBssIfEntry_Object = MibTableRow
hpnicfDot11WlanBssIfEntry = _HpnicfDot11WlanBssIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 2, 1)
)
hpnicfDot11WlanBssIfEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11WlanBssIfNumber"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WlanBssIfEntry.setStatus("current")
_HpnicfDot11WlanBssIfNumber_Type = Integer32
_HpnicfDot11WlanBssIfNumber_Object = MibTableColumn
hpnicfDot11WlanBssIfNumber = _HpnicfDot11WlanBssIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 2, 1, 1),
    _HpnicfDot11WlanBssIfNumber_Type()
)
hpnicfDot11WlanBssIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WlanBssIfNumber.setStatus("current")
_HpnicfDot11WlanBssIfIndex_Type = Integer32
_HpnicfDot11WlanBssIfIndex_Object = MibTableColumn
hpnicfDot11WlanBssIfIndex = _HpnicfDot11WlanBssIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 2, 1, 2),
    _HpnicfDot11WlanBssIfIndex_Type()
)
hpnicfDot11WlanBssIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WlanBssIfIndex.setStatus("current")
_HpnicfDot11WlanBssRowStatus_Type = RowStatus
_HpnicfDot11WlanBssRowStatus_Object = MibTableColumn
hpnicfDot11WlanBssRowStatus = _HpnicfDot11WlanBssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 2, 1, 3),
    _HpnicfDot11WlanBssRowStatus_Type()
)
hpnicfDot11WlanBssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11WlanBssRowStatus.setStatus("current")
_HpnicfDot11WLANEthernetIfTable_Object = MibTable
hpnicfDot11WLANEthernetIfTable = _HpnicfDot11WLANEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11WLANEthernetIfTable.setStatus("current")
_HpnicfDot11WLANEthernetIfEntry_Object = MibTableRow
hpnicfDot11WLANEthernetIfEntry = _HpnicfDot11WLANEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 3, 1)
)
hpnicfDot11WLANEthernetIfEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11WlanEthernetIfNumber"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WLANEthernetIfEntry.setStatus("current")
_HpnicfDot11WlanEthernetIfNumber_Type = Integer32
_HpnicfDot11WlanEthernetIfNumber_Object = MibTableColumn
hpnicfDot11WlanEthernetIfNumber = _HpnicfDot11WlanEthernetIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 3, 1, 1),
    _HpnicfDot11WlanEthernetIfNumber_Type()
)
hpnicfDot11WlanEthernetIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WlanEthernetIfNumber.setStatus("current")
_HpnicfDot11WLANEthernetIfIndex_Type = Integer32
_HpnicfDot11WLANEthernetIfIndex_Object = MibTableColumn
hpnicfDot11WLANEthernetIfIndex = _HpnicfDot11WLANEthernetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 3, 1, 2),
    _HpnicfDot11WLANEthernetIfIndex_Type()
)
hpnicfDot11WLANEthernetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WLANEthernetIfIndex.setStatus("current")
_HpnicfDot11WlanEthernetRowStatus_Type = RowStatus
_HpnicfDot11WlanEthernetRowStatus_Object = MibTableColumn
hpnicfDot11WlanEthernetRowStatus = _HpnicfDot11WlanEthernetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 3, 1, 3),
    _HpnicfDot11WlanEthernetRowStatus_Type()
)
hpnicfDot11WlanEthernetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11WlanEthernetRowStatus.setStatus("current")
_HpnicfDot11PortSecurityTable_Object = MibTable
hpnicfDot11PortSecurityTable = _HpnicfDot11PortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot11PortSecurityTable.setStatus("current")
_HpnicfDot11PortSecurityEntry_Object = MibTableRow
hpnicfDot11PortSecurityEntry = _HpnicfDot11PortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 4, 1)
)
hpnicfDot11PortSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11PortSecurityEntry.setStatus("current")


class _HpnicfDot11PortSecurityMode_Type(Integer32):
    """Custom type hpnicfDot11PortSecurityMode based on Integer32"""
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
        *(("ext", 6),
          ("macAddressAndPsk", 4),
          ("noRestrictions", 1),
          ("psk", 3),
          ("userLoginSecureExt", 2),
          ("userLoginSecureExtOrPsk", 5))
    )


_HpnicfDot11PortSecurityMode_Type.__name__ = "Integer32"
_HpnicfDot11PortSecurityMode_Object = MibTableColumn
hpnicfDot11PortSecurityMode = _HpnicfDot11PortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 4, 1, 1),
    _HpnicfDot11PortSecurityMode_Type()
)
hpnicfDot11PortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11PortSecurityMode.setStatus("current")


class _HpnicfDot11SecurityUserLoginTxKeyType_Type(Integer32):
    """Custom type hpnicfDot11SecurityUserLoginTxKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userLoginTxKeyTypeDot11Key", 2),
          ("userLoginTxKeyTypeNone", 1),
          ("userLoginTxKeyTypeRsaRC4Key", 3))
    )


_HpnicfDot11SecurityUserLoginTxKeyType_Type.__name__ = "Integer32"
_HpnicfDot11SecurityUserLoginTxKeyType_Object = MibTableColumn
hpnicfDot11SecurityUserLoginTxKeyType = _HpnicfDot11SecurityUserLoginTxKeyType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 4, 1, 2),
    _HpnicfDot11SecurityUserLoginTxKeyType_Type()
)
hpnicfDot11SecurityUserLoginTxKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SecurityUserLoginTxKeyType.setStatus("current")


class _HpnicfDot11SecurityPskKeyMode_Type(Integer32):
    """Custom type hpnicfDot11SecurityPskKeyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pskKeyModeNone", 1),
          ("pskKeyModePassPhrase", 2),
          ("pskKeyModeRawKey", 3))
    )


_HpnicfDot11SecurityPskKeyMode_Type.__name__ = "Integer32"
_HpnicfDot11SecurityPskKeyMode_Object = MibTableColumn
hpnicfDot11SecurityPskKeyMode = _HpnicfDot11SecurityPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 4, 1, 3),
    _HpnicfDot11SecurityPskKeyMode_Type()
)
hpnicfDot11SecurityPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SecurityPskKeyMode.setStatus("current")
_HpnicfDot11SecurityPskKeyString_Type = DisplayString
_HpnicfDot11SecurityPskKeyString_Object = MibTableColumn
hpnicfDot11SecurityPskKeyString = _HpnicfDot11SecurityPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 4, 1, 4),
    _HpnicfDot11SecurityPskKeyString_Type()
)
hpnicfDot11SecurityPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11SecurityPskKeyString.setStatus("current")
_HpnicfDot11WlanMeshIfTable_Object = MibTable
hpnicfDot11WlanMeshIfTable = _HpnicfDot11WlanMeshIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 5)
)
if mibBuilder.loadTexts:
    hpnicfDot11WlanMeshIfTable.setStatus("current")
_HpnicfDot11WlanMeshIfEntry_Object = MibTableRow
hpnicfDot11WlanMeshIfEntry = _HpnicfDot11WlanMeshIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 5, 1)
)
hpnicfDot11WlanMeshIfEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11WlanMeshIfNumber"),
)
if mibBuilder.loadTexts:
    hpnicfDot11WlanMeshIfEntry.setStatus("current")
_HpnicfDot11WlanMeshIfNumber_Type = Integer32
_HpnicfDot11WlanMeshIfNumber_Object = MibTableColumn
hpnicfDot11WlanMeshIfNumber = _HpnicfDot11WlanMeshIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 5, 1, 1),
    _HpnicfDot11WlanMeshIfNumber_Type()
)
hpnicfDot11WlanMeshIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11WlanMeshIfNumber.setStatus("current")
_HpnicfDot11WlanMeshIfIndex_Type = Integer32
_HpnicfDot11WlanMeshIfIndex_Object = MibTableColumn
hpnicfDot11WlanMeshIfIndex = _HpnicfDot11WlanMeshIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 5, 1, 2),
    _HpnicfDot11WlanMeshIfIndex_Type()
)
hpnicfDot11WlanMeshIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11WlanMeshIfIndex.setStatus("current")
_HpnicfDot11WlanMeshRowStatus_Type = RowStatus
_HpnicfDot11WlanMeshRowStatus_Object = MibTableColumn
hpnicfDot11WlanMeshRowStatus = _HpnicfDot11WlanMeshRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 6, 5, 1, 3),
    _HpnicfDot11WlanMeshRowStatus_Type()
)
hpnicfDot11WlanMeshRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDot11WlanMeshRowStatus.setStatus("current")
_HpnicfDot11ACBackupGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11ACBackupGroup = _HpnicfDot11ACBackupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 7)
)
_HpnicfDot11BackupACAdrssIP_Type = InetAddress
_HpnicfDot11BackupACAdrssIP_Object = MibScalar
hpnicfDot11BackupACAdrssIP = _HpnicfDot11BackupACAdrssIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 7, 1),
    _HpnicfDot11BackupACAdrssIP_Type()
)
hpnicfDot11BackupACAdrssIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11BackupACAdrssIP.setStatus("current")
_HpnicfDot11BackupACAdrssIPv6_Type = InetAddress
_HpnicfDot11BackupACAdrssIPv6_Object = MibScalar
hpnicfDot11BackupACAdrssIPv6 = _HpnicfDot11BackupACAdrssIPv6_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 7, 2),
    _HpnicfDot11BackupACAdrssIPv6_Type()
)
hpnicfDot11BackupACAdrssIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11BackupACAdrssIPv6.setStatus("current")
_HpnicfDot11RadioElementConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11RadioElementConfigGroup = _HpnicfDot11RadioElementConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8)
)
_HpnicfDot11nRadioCfgTable_Object = MibTable
hpnicfDot11nRadioCfgTable = _HpnicfDot11nRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfgTable.setStatus("current")
_HpnicfDot11nRadioCfgEntry_Object = MibTableRow
hpnicfDot11nRadioCfgEntry = _HpnicfDot11nRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 1, 1)
)
hpnicfDot11nRadioCfgEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11nRadioCfgIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfgEntry.setStatus("current")
_HpnicfDot11nRadioCfgIndex_Type = HpnicfDot11RadioElementIndex
_HpnicfDot11nRadioCfgIndex_Object = MibTableColumn
hpnicfDot11nRadioCfgIndex = _HpnicfDot11nRadioCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 1, 1, 1),
    _HpnicfDot11nRadioCfgIndex_Type()
)
hpnicfDot11nRadioCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfgIndex.setStatus("current")


class _HpnicfDot11nAMpduEnable_Type(TruthValue):
    """Custom type hpnicfDot11nAMpduEnable based on TruthValue"""


_HpnicfDot11nAMpduEnable_Object = MibTableColumn
hpnicfDot11nAMpduEnable = _HpnicfDot11nAMpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 1, 1, 2),
    _HpnicfDot11nAMpduEnable_Type()
)
hpnicfDot11nAMpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nAMpduEnable.setStatus("current")


class _HpnicfDot11nAMsduEnable_Type(TruthValue):
    """Custom type hpnicfDot11nAMsduEnable based on TruthValue"""


_HpnicfDot11nAMsduEnable_Object = MibTableColumn
hpnicfDot11nAMsduEnable = _HpnicfDot11nAMsduEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 1, 1, 3),
    _HpnicfDot11nAMsduEnable_Type()
)
hpnicfDot11nAMsduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nAMsduEnable.setStatus("current")


class _HpnicfDot11nClientDot11nOnly_Type(TruthValue):
    """Custom type hpnicfDot11nClientDot11nOnly based on TruthValue"""


_HpnicfDot11nClientDot11nOnly_Object = MibTableColumn
hpnicfDot11nClientDot11nOnly = _HpnicfDot11nClientDot11nOnly_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 1, 1, 4),
    _HpnicfDot11nClientDot11nOnly_Type()
)
hpnicfDot11nClientDot11nOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nClientDot11nOnly.setStatus("current")


class _HpnicfDot11nChanelBand_Type(Integer32):
    """Custom type hpnicfDot11nChanelBand based on Integer32"""
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
        *(("mode20", 1),
          ("mode40", 2),
          ("mode80", 3))
    )


_HpnicfDot11nChanelBand_Type.__name__ = "Integer32"
_HpnicfDot11nChanelBand_Object = MibTableColumn
hpnicfDot11nChanelBand = _HpnicfDot11nChanelBand_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 1, 1, 5),
    _HpnicfDot11nChanelBand_Type()
)
hpnicfDot11nChanelBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nChanelBand.setStatus("current")


class _HpnicfDot11nShortGiEnable_Type(TruthValue):
    """Custom type hpnicfDot11nShortGiEnable based on TruthValue"""


_HpnicfDot11nShortGiEnable_Object = MibTableColumn
hpnicfDot11nShortGiEnable = _HpnicfDot11nShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 1, 1, 6),
    _HpnicfDot11nShortGiEnable_Type()
)
hpnicfDot11nShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nShortGiEnable.setStatus("current")


class _HpnicfDot11nClientDot11acOnly_Type(TruthValue):
    """Custom type hpnicfDot11nClientDot11acOnly based on TruthValue"""


_HpnicfDot11nClientDot11acOnly_Object = MibTableColumn
hpnicfDot11nClientDot11acOnly = _HpnicfDot11nClientDot11acOnly_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 1, 1, 7),
    _HpnicfDot11nClientDot11acOnly_Type()
)
hpnicfDot11nClientDot11acOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nClientDot11acOnly.setStatus("current")
_HpnicfDot11RadioWDSTable_Object = MibTable
hpnicfDot11RadioWDSTable = _HpnicfDot11RadioWDSTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioWDSTable.setStatus("current")
_HpnicfDot11RadioWDSEntry_Object = MibTableRow
hpnicfDot11RadioWDSEntry = _HpnicfDot11RadioWDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 2, 1)
)
hpnicfDot11RadioWDSEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11RadioWDSIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioWDSEntry.setStatus("current")
_HpnicfDot11RadioWDSIndex_Type = HpnicfDot11RadioElementIndex
_HpnicfDot11RadioWDSIndex_Object = MibTableColumn
hpnicfDot11RadioWDSIndex = _HpnicfDot11RadioWDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 2, 1, 1),
    _HpnicfDot11RadioWDSIndex_Type()
)
hpnicfDot11RadioWDSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RadioWDSIndex.setStatus("current")


class _HpnicfDot11RadioWDSMode_Type(Integer32):
    """Custom type hpnicfDot11RadioWDSMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nowds", 1),
          ("wds", 2))
    )


_HpnicfDot11RadioWDSMode_Type.__name__ = "Integer32"
_HpnicfDot11RadioWDSMode_Object = MibTableColumn
hpnicfDot11RadioWDSMode = _HpnicfDot11RadioWDSMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 2, 1, 2),
    _HpnicfDot11RadioWDSMode_Type()
)
hpnicfDot11RadioWDSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioWDSMode.setStatus("current")


class _HpnicfDot11RadioWDSNetWorkID_Type(OctetString):
    """Custom type hpnicfDot11RadioWDSNetWorkID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfDot11RadioWDSNetWorkID_Type.__name__ = "OctetString"
_HpnicfDot11RadioWDSNetWorkID_Object = MibTableColumn
hpnicfDot11RadioWDSNetWorkID = _HpnicfDot11RadioWDSNetWorkID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 2, 1, 3),
    _HpnicfDot11RadioWDSNetWorkID_Type()
)
hpnicfDot11RadioWDSNetWorkID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioWDSNetWorkID.setStatus("current")


class _HpnicfDot11WDSSecPskKeyMode_Type(Integer32):
    """Custom type hpnicfDot11WDSSecPskKeyMode based on Integer32"""
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
        *(("pskKeyModeNone", 1),
          ("pskKeyModePassPhrase", 2),
          ("pskKeyModeRawKey", 3))
    )


_HpnicfDot11WDSSecPskKeyMode_Type.__name__ = "Integer32"
_HpnicfDot11WDSSecPskKeyMode_Object = MibTableColumn
hpnicfDot11WDSSecPskKeyMode = _HpnicfDot11WDSSecPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 2, 1, 4),
    _HpnicfDot11WDSSecPskKeyMode_Type()
)
hpnicfDot11WDSSecPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11WDSSecPskKeyMode.setStatus("current")
_HpnicfDot11WDSSecPskKeyString_Type = DisplayString
_HpnicfDot11WDSSecPskKeyString_Object = MibTableColumn
hpnicfDot11WDSSecPskKeyString = _HpnicfDot11WDSSecPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 2, 1, 5),
    _HpnicfDot11WDSSecPskKeyString_Type()
)
hpnicfDot11WDSSecPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11WDSSecPskKeyString.setStatus("current")
_HpnicfDot11nRadioCfg2Table_Object = MibTable
hpnicfDot11nRadioCfg2Table = _HpnicfDot11nRadioCfg2Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2Table.setStatus("current")
_HpnicfDot11nRadioCfg2Entry_Object = MibTableRow
hpnicfDot11nRadioCfg2Entry = _HpnicfDot11nRadioCfg2Entry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1)
)
hpnicfDot11nRadioCfg2Entry.setIndexNames(
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11nRadioCfg2APIDIndex"),
    (0, "HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11nRadioCfg2RadioIDIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2Entry.setStatus("current")
_HpnicfDot11nRadioCfg2APIDIndex_Type = HpnicfDot11ObjectIDType
_HpnicfDot11nRadioCfg2APIDIndex_Object = MibTableColumn
hpnicfDot11nRadioCfg2APIDIndex = _HpnicfDot11nRadioCfg2APIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 1),
    _HpnicfDot11nRadioCfg2APIDIndex_Type()
)
hpnicfDot11nRadioCfg2APIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2APIDIndex.setStatus("current")
_HpnicfDot11nRadioCfg2RadioIDIndex_Type = HpnicfDot11RadioScopeType
_HpnicfDot11nRadioCfg2RadioIDIndex_Object = MibTableColumn
hpnicfDot11nRadioCfg2RadioIDIndex = _HpnicfDot11nRadioCfg2RadioIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 2),
    _HpnicfDot11nRadioCfg2RadioIDIndex_Type()
)
hpnicfDot11nRadioCfg2RadioIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2RadioIDIndex.setStatus("current")


class _HpnicfDot11nRadioCfg2AMpduEnable_Type(TruthValue):
    """Custom type hpnicfDot11nRadioCfg2AMpduEnable based on TruthValue"""


_HpnicfDot11nRadioCfg2AMpduEnable_Object = MibTableColumn
hpnicfDot11nRadioCfg2AMpduEnable = _HpnicfDot11nRadioCfg2AMpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 3),
    _HpnicfDot11nRadioCfg2AMpduEnable_Type()
)
hpnicfDot11nRadioCfg2AMpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2AMpduEnable.setStatus("current")


class _HpnicfDot11nRadioCfg2AMsduEnable_Type(TruthValue):
    """Custom type hpnicfDot11nRadioCfg2AMsduEnable based on TruthValue"""


_HpnicfDot11nRadioCfg2AMsduEnable_Object = MibTableColumn
hpnicfDot11nRadioCfg2AMsduEnable = _HpnicfDot11nRadioCfg2AMsduEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 4),
    _HpnicfDot11nRadioCfg2AMsduEnable_Type()
)
hpnicfDot11nRadioCfg2AMsduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2AMsduEnable.setStatus("current")


class _HpnicfDot11nRadioCfg2ClientDot11nOnly_Type(TruthValue):
    """Custom type hpnicfDot11nRadioCfg2ClientDot11nOnly based on TruthValue"""


_HpnicfDot11nRadioCfg2ClientDot11nOnly_Object = MibTableColumn
hpnicfDot11nRadioCfg2ClientDot11nOnly = _HpnicfDot11nRadioCfg2ClientDot11nOnly_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 5),
    _HpnicfDot11nRadioCfg2ClientDot11nOnly_Type()
)
hpnicfDot11nRadioCfg2ClientDot11nOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2ClientDot11nOnly.setStatus("current")


class _HpnicfDot11nRadioCfg2ChannelBand_Type(Integer32):
    """Custom type hpnicfDot11nRadioCfg2ChannelBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode20", 1),
          ("mode40", 2),
          ("mode80", 3))
    )


_HpnicfDot11nRadioCfg2ChannelBand_Type.__name__ = "Integer32"
_HpnicfDot11nRadioCfg2ChannelBand_Object = MibTableColumn
hpnicfDot11nRadioCfg2ChannelBand = _HpnicfDot11nRadioCfg2ChannelBand_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 6),
    _HpnicfDot11nRadioCfg2ChannelBand_Type()
)
hpnicfDot11nRadioCfg2ChannelBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2ChannelBand.setStatus("current")


class _HpnicfDot11nRadioCfg2ShortGiEnable_Type(TruthValue):
    """Custom type hpnicfDot11nRadioCfg2ShortGiEnable based on TruthValue"""


_HpnicfDot11nRadioCfg2ShortGiEnable_Object = MibTableColumn
hpnicfDot11nRadioCfg2ShortGiEnable = _HpnicfDot11nRadioCfg2ShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 7),
    _HpnicfDot11nRadioCfg2ShortGiEnable_Type()
)
hpnicfDot11nRadioCfg2ShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2ShortGiEnable.setStatus("current")


class _HpnicfDot11nRadioCfg2AMpduEnableCM_Type(Integer32):
    """Custom type hpnicfDot11nRadioCfg2AMpduEnableCM based on Integer32"""
    defaultValue = 1

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


_HpnicfDot11nRadioCfg2AMpduEnableCM_Type.__name__ = "Integer32"
_HpnicfDot11nRadioCfg2AMpduEnableCM_Object = MibTableColumn
hpnicfDot11nRadioCfg2AMpduEnableCM = _HpnicfDot11nRadioCfg2AMpduEnableCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 8),
    _HpnicfDot11nRadioCfg2AMpduEnableCM_Type()
)
hpnicfDot11nRadioCfg2AMpduEnableCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2AMpduEnableCM.setStatus("current")


class _HpnicfDot11nRadioCfg2ChannelBandCM_Type(Integer32):
    """Custom type hpnicfDot11nRadioCfg2ChannelBandCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode20", 2),
          ("mode40", 1))
    )


_HpnicfDot11nRadioCfg2ChannelBandCM_Type.__name__ = "Integer32"
_HpnicfDot11nRadioCfg2ChannelBandCM_Object = MibTableColumn
hpnicfDot11nRadioCfg2ChannelBandCM = _HpnicfDot11nRadioCfg2ChannelBandCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 9),
    _HpnicfDot11nRadioCfg2ChannelBandCM_Type()
)
hpnicfDot11nRadioCfg2ChannelBandCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2ChannelBandCM.setStatus("current")


class _HpnicfDot11nRadioCfg2ShortGiEnableCM_Type(Integer32):
    """Custom type hpnicfDot11nRadioCfg2ShortGiEnableCM based on Integer32"""
    defaultValue = 1

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


_HpnicfDot11nRadioCfg2ShortGiEnableCM_Type.__name__ = "Integer32"
_HpnicfDot11nRadioCfg2ShortGiEnableCM_Object = MibTableColumn
hpnicfDot11nRadioCfg2ShortGiEnableCM = _HpnicfDot11nRadioCfg2ShortGiEnableCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 10),
    _HpnicfDot11nRadioCfg2ShortGiEnableCM_Type()
)
hpnicfDot11nRadioCfg2ShortGiEnableCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2ShortGiEnableCM.setStatus("current")


class _HpnicfDot11nRadioCfg2ClientDot11acOnly_Type(TruthValue):
    """Custom type hpnicfDot11nRadioCfg2ClientDot11acOnly based on TruthValue"""


_HpnicfDot11nRadioCfg2ClientDot11acOnly_Object = MibTableColumn
hpnicfDot11nRadioCfg2ClientDot11acOnly = _HpnicfDot11nRadioCfg2ClientDot11acOnly_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 11),
    _HpnicfDot11nRadioCfg2ClientDot11acOnly_Type()
)
hpnicfDot11nRadioCfg2ClientDot11acOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2ClientDot11acOnly.setStatus("current")


class _HpnicfDot11nRadioCfg2ClientDot11nOnlyCM_Type(HpnicfDot11TruthValueCM):
    """Custom type hpnicfDot11nRadioCfg2ClientDot11nOnlyCM based on HpnicfDot11TruthValueCM"""


_HpnicfDot11nRadioCfg2ClientDot11nOnlyCM_Object = MibTableColumn
hpnicfDot11nRadioCfg2ClientDot11nOnlyCM = _HpnicfDot11nRadioCfg2ClientDot11nOnlyCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 8, 3, 1, 12),
    _HpnicfDot11nRadioCfg2ClientDot11nOnlyCM_Type()
)
hpnicfDot11nRadioCfg2ClientDot11nOnlyCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11nRadioCfg2ClientDot11nOnlyCM.setStatus("current")
_HpnicfDot11CfgNotifyGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11CfgNotifyGroup = _HpnicfDot11CfgNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9)
)
_HpnicfDot11CfgNotifications_ObjectIdentity = ObjectIdentity
hpnicfDot11CfgNotifications = _HpnicfDot11CfgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9, 0)
)
_HpnicfDot11CfgTrapVarObjects_ObjectIdentity = ObjectIdentity
hpnicfDot11CfgTrapVarObjects = _HpnicfDot11CfgTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9, 1)
)


class _HpnicfDot11PreConflictTemplateNum_Type(Integer32):
    """Custom type hpnicfDot11PreConflictTemplateNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfDot11PreConflictTemplateNum_Type.__name__ = "Integer32"
_HpnicfDot11PreConflictTemplateNum_Object = MibScalar
hpnicfDot11PreConflictTemplateNum = _HpnicfDot11PreConflictTemplateNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9, 1, 1),
    _HpnicfDot11PreConflictTemplateNum_Type()
)
hpnicfDot11PreConflictTemplateNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11PreConflictTemplateNum.setStatus("current")


class _HpnicfDot11CurrConflictTemplateNum_Type(Integer32):
    """Custom type hpnicfDot11CurrConflictTemplateNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfDot11CurrConflictTemplateNum_Type.__name__ = "Integer32"
_HpnicfDot11CurrConflictTemplateNum_Object = MibScalar
hpnicfDot11CurrConflictTemplateNum = _HpnicfDot11CurrConflictTemplateNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9, 1, 2),
    _HpnicfDot11CurrConflictTemplateNum_Type()
)
hpnicfDot11CurrConflictTemplateNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11CurrConflictTemplateNum.setStatus("current")


class _HpnicfDot11ConflictCipherIdx_Type(Integer32):
    """Custom type hpnicfDot11ConflictCipherIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HpnicfDot11ConflictCipherIdx_Type.__name__ = "Integer32"
_HpnicfDot11ConflictCipherIdx_Object = MibScalar
hpnicfDot11ConflictCipherIdx = _HpnicfDot11ConflictCipherIdx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9, 1, 3),
    _HpnicfDot11ConflictCipherIdx_Type()
)
hpnicfDot11ConflictCipherIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ConflictCipherIdx.setStatus("current")
_HpnicfDot11ConfigureAPID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11ConfigureAPID_Object = MibScalar
hpnicfDot11ConfigureAPID = _HpnicfDot11ConfigureAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9, 1, 4),
    _HpnicfDot11ConfigureAPID_Type()
)
hpnicfDot11ConfigureAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ConfigureAPID.setStatus("current")
_HpnicfDot11ConfigureRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11ConfigureRadioID_Object = MibScalar
hpnicfDot11ConfigureRadioID = _HpnicfDot11ConfigureRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9, 1, 5),
    _HpnicfDot11ConfigureRadioID_Type()
)
hpnicfDot11ConfigureRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ConfigureRadioID.setStatus("current")
_HpnicfDot11ConfigureAPMacAddress_Type = MacAddress
_HpnicfDot11ConfigureAPMacAddress_Object = MibScalar
hpnicfDot11ConfigureAPMacAddress = _HpnicfDot11ConfigureAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9, 1, 6),
    _HpnicfDot11ConfigureAPMacAddress_Type()
)
hpnicfDot11ConfigureAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11ConfigureAPMacAddress.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfDot11CfgCipherChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9, 0, 1)
)
hpnicfDot11CfgCipherChange.setObjects(
      *(("HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11SSIDName"),
        ("HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11SecurityCiphers"))
)
if mibBuilder.loadTexts:
    hpnicfDot11CfgCipherChange.setStatus(
        "current"
    )

hpnicfDot11CfgPSKChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9, 0, 2)
)
hpnicfDot11CfgPSKChange.setObjects(
    ("HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11SSIDName")
)
if mibBuilder.loadTexts:
    hpnicfDot11CfgPSKChange.setStatus(
        "current"
    )

hpnicfDot11SSIDWepIDConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 4, 9, 0, 3)
)
hpnicfDot11SSIDWepIDConflictTrap.setObjects(
      *(("HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11PreConflictTemplateNum"),
        ("HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11CurrConflictTemplateNum"),
        ("HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11ConflictCipherIdx"),
        ("HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11ConfigureAPID"),
        ("HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11ConfigureRadioID"),
        ("HPN-ICF-DOT11-CFG-MIB", "hpnicfDot11ConfigureAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11SSIDWepIDConflictTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-CFG-MIB",
    **{"hpnicfDot11CFG": hpnicfDot11CFG,
       "hpnicfDot11GlobeConfigGroup": hpnicfDot11GlobeConfigGroup,
       "hpnicfDot11GlobalCountryCode": hpnicfDot11GlobalCountryCode,
       "hpnicfDot11StaKeepALiveTimerIntvl": hpnicfDot11StaKeepALiveTimerIntvl,
       "hpnicfDot11StaIdleTimerIntvl": hpnicfDot11StaIdleTimerIntvl,
       "hpnicfDot11BroadcastProbeReply": hpnicfDot11BroadcastProbeReply,
       "hpnicfDot11APScanMode": hpnicfDot11APScanMode,
       "hpnicfDot11ACCtrlTunnelSecSupport": hpnicfDot11ACCtrlTunnelSecSupport,
       "hpnicfDot11ACDataTunnelSecSupport": hpnicfDot11ACDataTunnelSecSupport,
       "hpnicfDot11ACAutoAPSupport": hpnicfDot11ACAutoAPSupport,
       "hpnicfDot11AutoAPName": hpnicfDot11AutoAPName,
       "hpnicfDot11PersistentName": hpnicfDot11PersistentName,
       "hpnicfDot11IntfTrapThreshold": hpnicfDot11IntfTrapThreshold,
       "hpnicfDot11MonitorInterval": hpnicfDot11MonitorInterval,
       "hpnicfDot11SampleInterval": hpnicfDot11SampleInterval,
       "hpnicfDot11ChnlSwitChkInterval": hpnicfDot11ChnlSwitChkInterval,
       "hpnicfDot11APUserUplimit": hpnicfDot11APUserUplimit,
       "hpnicfDot11APL2IsolateEnable": hpnicfDot11APL2IsolateEnable,
       "hpnicfDot11APBSSIDSupportNum": hpnicfDot11APBSSIDSupportNum,
       "hpnicfDot11APLastUpdateStatTime": hpnicfDot11APLastUpdateStatTime,
       "hpnicfDot11APDoSProtectEnable": hpnicfDot11APDoSProtectEnable,
       "hpnicfDot11MaxAPPerIf": hpnicfDot11MaxAPPerIf,
       "hpnicfDot11SampleTimeStamp": hpnicfDot11SampleTimeStamp,
       "hpnicfDot11UplinkTrackId": hpnicfDot11UplinkTrackId,
       "hpnicfDot11RtCollectSwitch": hpnicfDot11RtCollectSwitch,
       "hpnicfDot11RglCollectIntvl": hpnicfDot11RglCollectIntvl,
       "hpnicfDot11RtCollectIntvl": hpnicfDot11RtCollectIntvl,
       "hpnicfDot11AllAPCpuUsageThreshold": hpnicfDot11AllAPCpuUsageThreshold,
       "hpnicfDot11AllAPMemUsageThreshold": hpnicfDot11AllAPMemUsageThreshold,
       "hpnicfDot11AdjIntfTrapThreshold": hpnicfDot11AdjIntfTrapThreshold,
       "hpnicfDot11AllAPMonitorMode": hpnicfDot11AllAPMonitorMode,
       "hpnicfDot11GlobalApFmwUpdState": hpnicfDot11GlobalApFmwUpdState,
       "hpnicfDot11ACNasIDCM": hpnicfDot11ACNasIDCM,
       "hpnicfDot11PolicyConfigGroup": hpnicfDot11PolicyConfigGroup,
       "hpnicfDot11RadioPolicyTable": hpnicfDot11RadioPolicyTable,
       "hpnicfDot11RadioPolicyEntry": hpnicfDot11RadioPolicyEntry,
       "hpnicfDot11RadioPolicyName": hpnicfDot11RadioPolicyName,
       "hpnicfDot11BeaconInterval": hpnicfDot11BeaconInterval,
       "hpnicfDot11DtimInterval": hpnicfDot11DtimInterval,
       "hpnicfDot11RtsThreshold": hpnicfDot11RtsThreshold,
       "hpnicfDot11FragThreshold": hpnicfDot11FragThreshold,
       "hpnicfDot11ShortRetryThreshold": hpnicfDot11ShortRetryThreshold,
       "hpnicfDot11LongRetryThreshold": hpnicfDot11LongRetryThreshold,
       "hpnicfDot11MaxRxLifetime": hpnicfDot11MaxRxLifetime,
       "hpnicfDot11RdoPolicyRowStatus": hpnicfDot11RdoPolicyRowStatus,
       "hpnicfDot11RdoClientMaxCount": hpnicfDot11RdoClientMaxCount,
       "hpnicfDot11BeaconIntervalMs": hpnicfDot11BeaconIntervalMs,
       "hpnicfDot11ServicePolicyTable": hpnicfDot11ServicePolicyTable,
       "hpnicfDot11ServicePolicyEntry": hpnicfDot11ServicePolicyEntry,
       "hpnicfDot11ServicePolicyID": hpnicfDot11ServicePolicyID,
       "hpnicfDot11SSIDName": hpnicfDot11SSIDName,
       "hpnicfDot11SSIDHidden": hpnicfDot11SSIDHidden,
       "hpnicfDot11AuthenMode": hpnicfDot11AuthenMode,
       "hpnicfDot11SSIDEncryptionMode": hpnicfDot11SSIDEncryptionMode,
       "hpnicfDot11WlanInfBindingType": hpnicfDot11WlanInfBindingType,
       "hpnicfDot11WlanInfBindingID": hpnicfDot11WlanInfBindingID,
       "hpnicfDot11SrvPolicyRowStatus": hpnicfDot11SrvPolicyRowStatus,
       "hpnicfDot11ClientMaxCount": hpnicfDot11ClientMaxCount,
       "hpnicfDot11SPInCirMode": hpnicfDot11SPInCirMode,
       "hpnicfDot11SPInCirValue": hpnicfDot11SPInCirValue,
       "hpnicfDot11SPOutCirMode": hpnicfDot11SPOutCirMode,
       "hpnicfDot11SPOutCirValue": hpnicfDot11SPOutCirValue,
       "hpnicfDot11WlanInfPVID": hpnicfDot11WlanInfPVID,
       "hpnicfDot11SPInCirStaticValue": hpnicfDot11SPInCirStaticValue,
       "hpnicfDot11SPOutCirStaticValue": hpnicfDot11SPOutCirStaticValue,
       "hpnicfDot11SPIsolate": hpnicfDot11SPIsolate,
       "hpnicfDot11WlanexAuthServerIP": hpnicfDot11WlanexAuthServerIP,
       "hpnicfDot11SPBeaconMeasEnable": hpnicfDot11SPBeaconMeasEnable,
       "hpnicfDot11SPBeaconMeasType": hpnicfDot11SPBeaconMeasType,
       "hpnicfDot11SPBeaconMeasInterval": hpnicfDot11SPBeaconMeasInterval,
       "hpnicfDot11AuthenModeCM": hpnicfDot11AuthenModeCM,
       "hpnicfDot11SecIEStatusCM": hpnicfDot11SecIEStatusCM,
       "hpnicfDot11SecurityCiphersCM": hpnicfDot11SecurityCiphersCM,
       "hpnicfDot11SrvPolicyStatusCM": hpnicfDot11SrvPolicyStatusCM,
       "hpnicfDot11SSIDHiddenCM": hpnicfDot11SSIDHiddenCM,
       "hpnicfDot11SPIsolateCM": hpnicfDot11SPIsolateCM,
       "hpnicfDot11ServicePolicyExtTable": hpnicfDot11ServicePolicyExtTable,
       "hpnicfDot11ServicePolicyExtEntry": hpnicfDot11ServicePolicyExtEntry,
       "hpnicfDot11ServicePolicyExtID": hpnicfDot11ServicePolicyExtID,
       "hpnicfDot11SecIEStatus": hpnicfDot11SecIEStatus,
       "hpnicfDot11SecurityCiphers": hpnicfDot11SecurityCiphers,
       "hpnicfDot11CipherKeyIndex": hpnicfDot11CipherKeyIndex,
       "hpnicfDot11CipherKey": hpnicfDot11CipherKey,
       "hpnicfDot11SrvPolicyExtRowStatus": hpnicfDot11SrvPolicyExtRowStatus,
       "hpnicfDot11CipherKeyType": hpnicfDot11CipherKeyType,
       "hpnicfDot11RadioPolicyExtTable": hpnicfDot11RadioPolicyExtTable,
       "hpnicfDot11RadioPolicyExtEntry": hpnicfDot11RadioPolicyExtEntry,
       "hpnicfDot11RPAPSerialID": hpnicfDot11RPAPSerialID,
       "hpnicfDot11RPRadioID": hpnicfDot11RPRadioID,
       "hpnicfDot11RPBeaconInterval": hpnicfDot11RPBeaconInterval,
       "hpnicfDot11RPDtimInterval": hpnicfDot11RPDtimInterval,
       "hpnicfDot11RPRtsThreshold": hpnicfDot11RPRtsThreshold,
       "hpnicfDot11RPFragThreshold": hpnicfDot11RPFragThreshold,
       "hpnicfDot11RPShortRetryThreshold": hpnicfDot11RPShortRetryThreshold,
       "hpnicfDot11RPLongRetryThreshold": hpnicfDot11RPLongRetryThreshold,
       "hpnicfDot11RPClientMaxCount": hpnicfDot11RPClientMaxCount,
       "hpnicfDot11RPBeaconIntervalCM": hpnicfDot11RPBeaconIntervalCM,
       "hpnicfDot11SrvPortSecurityTable": hpnicfDot11SrvPortSecurityTable,
       "hpnicfDot11SrvPortSecurityEntry": hpnicfDot11SrvPortSecurityEntry,
       "hpnicfDot11SecurityServicePolicyID": hpnicfDot11SecurityServicePolicyID,
       "hpnicfDot11SrvPortSecurityMode": hpnicfDot11SrvPortSecurityMode,
       "hpnicfDot11SrvSecurityKeyType": hpnicfDot11SrvSecurityKeyType,
       "hpnicfDot11SrvSecurityPskKeyMode": hpnicfDot11SrvSecurityPskKeyMode,
       "hpnicfDot11SrvSecurityPskKeyString": hpnicfDot11SrvSecurityPskKeyString,
       "hpnicfDot11SrvPortSecurityModeCM": hpnicfDot11SrvPortSecurityModeCM,
       "hpnicfDot11SrvPolicyExtendTable": hpnicfDot11SrvPolicyExtendTable,
       "hpnicfDot11SrvPolicyExtendEntry": hpnicfDot11SrvPolicyExtendEntry,
       "hpnicfDot11SPEnable": hpnicfDot11SPEnable,
       "hpnicfDot11APConfigGroup": hpnicfDot11APConfigGroup,
       "hpnicfDot11APTemplateTable": hpnicfDot11APTemplateTable,
       "hpnicfDot11APTemplateEntry": hpnicfDot11APTemplateEntry,
       "hpnicfDot11APTemplateName": hpnicfDot11APTemplateName,
       "hpnicfDot11APSerialID": hpnicfDot11APSerialID,
       "hpnicfDot11TemplateAPModelAlias": hpnicfDot11TemplateAPModelAlias,
       "hpnicfDot11Description": hpnicfDot11Description,
       "hpnicfDot11APWorkMode": hpnicfDot11APWorkMode,
       "hpnicfDot11APTemplateRowStatus": hpnicfDot11APTemplateRowStatus,
       "hpnicfDot11APName": hpnicfDot11APName,
       "hpnicfDot11StatisInterv": hpnicfDot11StatisInterv,
       "hpnicfDot11APBroadcastProbeReply": hpnicfDot11APBroadcastProbeReply,
       "hpnicfDot11StaIdleTimerInterv": hpnicfDot11StaIdleTimerInterv,
       "hpnicfDot11StaKeepAliveTimerInterv": hpnicfDot11StaKeepAliveTimerInterv,
       "hpnicfDot11APCir": hpnicfDot11APCir,
       "hpnicfDot11APCbs": hpnicfDot11APCbs,
       "hpnicfDot11APPriorityLevel": hpnicfDot11APPriorityLevel,
       "hpnicfDot11APElementID": hpnicfDot11APElementID,
       "hpnicfDot11APDevDetectEnable": hpnicfDot11APDevDetectEnable,
       "hpnicfDot11APGetIPMethod": hpnicfDot11APGetIPMethod,
       "hpnicfDot11StatisIntervMode": hpnicfDot11StatisIntervMode,
       "hpnicfDot11ApTrapEnabled": hpnicfDot11ApTrapEnabled,
       "hpnicfDot11ApFmwUpdState": hpnicfDot11ApFmwUpdState,
       "hpnicfDot11StatisIntervModeCM": hpnicfDot11StatisIntervModeCM,
       "hpnicfDot11ApNasIDCM": hpnicfDot11ApNasIDCM,
       "hpnicfDot11RadioToConfigTable": hpnicfDot11RadioToConfigTable,
       "hpnicfDot11RadioToConfigEntry": hpnicfDot11RadioToConfigEntry,
       "hpnicfDot11APTemplateNameCfg": hpnicfDot11APTemplateNameCfg,
       "hpnicfDot11CfgRadioID": hpnicfDot11CfgRadioID,
       "hpnicfDot11CfgRadioPolicyName": hpnicfDot11CfgRadioPolicyName,
       "hpnicfDot11CfgRadioType": hpnicfDot11CfgRadioType,
       "hpnicfDot11CfgChannel": hpnicfDot11CfgChannel,
       "hpnicfDot11CfgMaxTxPowerLevel": hpnicfDot11CfgMaxTxPowerLevel,
       "hpnicfDot11PreambleLen": hpnicfDot11PreambleLen,
       "hpnicfDot11CfgRadioStatus": hpnicfDot11CfgRadioStatus,
       "hpnicfDot11CfgRdElementID": hpnicfDot11CfgRdElementID,
       "hpnicfDot11CfgWorkMode": hpnicfDot11CfgWorkMode,
       "hpnicfDot11CfgPwrAttValue": hpnicfDot11CfgPwrAttValue,
       "hpnicfDot11RadioTxArithmetic": hpnicfDot11RadioTxArithmetic,
       "hpnicfDot11CfgChannelLockStat": hpnicfDot11CfgChannelLockStat,
       "hpnicfDot11CfgPowerLockStat": hpnicfDot11CfgPowerLockStat,
       "hpnicfDot11CfgLBRdGroupId": hpnicfDot11CfgLBRdGroupId,
       "hpnicfDot11CfgRRMSDRdGroupId": hpnicfDot11CfgRRMSDRdGroupId,
       "hpnicfDot11CfgRadioType2": hpnicfDot11CfgRadioType2,
       "hpnicfDot11CfgIDSEnable": hpnicfDot11CfgIDSEnable,
       "hpnicfDot11CfgSaEnable": hpnicfDot11CfgSaEnable,
       "hpnicfDot11CfgSaCltRtFFTData": hpnicfDot11CfgSaCltRtFFTData,
       "hpnicfDot11CfgSaBand": hpnicfDot11CfgSaBand,
       "hpnicfDot11APServiceSetTable": hpnicfDot11APServiceSetTable,
       "hpnicfDot11APServiceSetEntry": hpnicfDot11APServiceSetEntry,
       "hpnicfDot11CfgServicePolicyID": hpnicfDot11CfgServicePolicyID,
       "hpnicfDot11SrvSetRowStatus": hpnicfDot11SrvSetRowStatus,
       "hpnicfDot11ServiceSetVlanId": hpnicfDot11ServiceSetVlanId,
       "hpnicfDot11APSysInfoSetTable": hpnicfDot11APSysInfoSetTable,
       "hpnicfDot11APSysInfoSetEntry": hpnicfDot11APSysInfoSetEntry,
       "hpnicfDot11APSysNetID": hpnicfDot11APSysNetID,
       "hpnicfDot11APCpuUsageThreshold": hpnicfDot11APCpuUsageThreshold,
       "hpnicfDot11APMemUsageThreshold": hpnicfDot11APMemUsageThreshold,
       "hpnicfDot11APLimitTable": hpnicfDot11APLimitTable,
       "hpnicfDot11APLimitEntry": hpnicfDot11APLimitEntry,
       "hpnicfDot11APSsidNumLimit": hpnicfDot11APSsidNumLimit,
       "hpnicfDot11APUserCntLimit": hpnicfDot11APUserCntLimit,
       "hpnicfDot11APUserThreshold": hpnicfDot11APUserThreshold,
       "hpnicfDot11APIfSetTable": hpnicfDot11APIfSetTable,
       "hpnicfDot11APIfSetEntry": hpnicfDot11APIfSetEntry,
       "hpnicfDot11APSetIfIndex": hpnicfDot11APSetIfIndex,
       "hpnicfDot11APIfAlias": hpnicfDot11APIfAlias,
       "hpnicfDot11APServiceVlanTable": hpnicfDot11APServiceVlanTable,
       "hpnicfDot11APServiceVlanEntry": hpnicfDot11APServiceVlanEntry,
       "hpnicfDot11APServiceVlanSerialID": hpnicfDot11APServiceVlanSerialID,
       "hpnicfDot11APServiceVlanSPID": hpnicfDot11APServiceVlanSPID,
       "hpnicfDot11APServiceVlanId": hpnicfDot11APServiceVlanId,
       "hpnicfDot11APServiceVlanRowStatus": hpnicfDot11APServiceVlanRowStatus,
       "hpnicfDot11RadioConfigTable": hpnicfDot11RadioConfigTable,
       "hpnicfDot11RadioConfigEntry": hpnicfDot11RadioConfigEntry,
       "hpnicfDot11RCAPSerialID": hpnicfDot11RCAPSerialID,
       "hpnicfDot11RCRadioID": hpnicfDot11RCRadioID,
       "hpnicfDot11RCRadioType": hpnicfDot11RCRadioType,
       "hpnicfDot11RCChannel": hpnicfDot11RCChannel,
       "hpnicfDot11RCPreambleLen": hpnicfDot11RCPreambleLen,
       "hpnicfDot11RCPwrAttValue": hpnicfDot11RCPwrAttValue,
       "hpnicfDot11RCApPowerLevel": hpnicfDot11RCApPowerLevel,
       "hpnicfDot11RCDynamicChlState": hpnicfDot11RCDynamicChlState,
       "hpnicfDot11RCDynamicPowerState": hpnicfDot11RCDynamicPowerState,
       "hpnicfDot11RCRadioStatus": hpnicfDot11RCRadioStatus,
       "hpnicfDot11RCRadioRate": hpnicfDot11RCRadioRate,
       "hpnicfDot11RCPwrAdjustStepLength": hpnicfDot11RCPwrAdjustStepLength,
       "hpnicfDot11RCRadioType2": hpnicfDot11RCRadioType2,
       "hpnicfDot11RCPreambleLenCM": hpnicfDot11RCPreambleLenCM,
       "hpnicfDot11RCDynamicChlStateCM": hpnicfDot11RCDynamicChlStateCM,
       "hpnicfDot11RCRadioStatusCM": hpnicfDot11RCRadioStatusCM,
       "hpnicfDot11RCRadioRateCM": hpnicfDot11RCRadioRateCM,
       "hpnicfDot11RCDynamicPowerStateCM": hpnicfDot11RCDynamicPowerStateCM,
       "hpnicfDot11RadioSSIDCfgTable": hpnicfDot11RadioSSIDCfgTable,
       "hpnicfDot11RadioSSIDCfgEntry": hpnicfDot11RadioSSIDCfgEntry,
       "hpnicfDot11RadioSSIDSerialID": hpnicfDot11RadioSSIDSerialID,
       "hpnicfDot11RadioSSIDRadioID": hpnicfDot11RadioSSIDRadioID,
       "hpnicfDot11RadioSSIDWLANID": hpnicfDot11RadioSSIDWLANID,
       "hpnicfDot11RadioSSIDIndex": hpnicfDot11RadioSSIDIndex,
       "hpnicfDot11RadioBSSID": hpnicfDot11RadioBSSID,
       "hpnicfDot11RadioSSIDRowStatus": hpnicfDot11RadioSSIDRowStatus,
       "hpnicfDot11APSerialIDTable": hpnicfDot11APSerialIDTable,
       "hpnicfDot11APSerialIDEntry": hpnicfDot11APSerialIDEntry,
       "hpnicfDot11SIDAPSerialID": hpnicfDot11SIDAPSerialID,
       "hpnicfDot11SIDAPWorkMode": hpnicfDot11SIDAPWorkMode,
       "hpnicfDot11SIDAPGetIPMethod": hpnicfDot11SIDAPGetIPMethod,
       "hpnicfDot11SIDAPTemplateName": hpnicfDot11SIDAPTemplateName,
       "hpnicfDot11SIDModelAlias": hpnicfDot11SIDModelAlias,
       "hpnicfDot11SIDAPDescription": hpnicfDot11SIDAPDescription,
       "hpnicfDot11SIDRowStatus": hpnicfDot11SIDRowStatus,
       "hpnicfDot11SIDAPName": hpnicfDot11SIDAPName,
       "hpnicfDot11SIDStatisInterv": hpnicfDot11SIDStatisInterv,
       "hpnicfDot11SIDAPBroadcastProbeReply": hpnicfDot11SIDAPBroadcastProbeReply,
       "hpnicfDot11SIDAPStaIdleTimerInterv": hpnicfDot11SIDAPStaIdleTimerInterv,
       "hpnicfDot11SIDStaKeepAliveTimerInterv": hpnicfDot11SIDStaKeepAliveTimerInterv,
       "hpnicfDot11SIDAPCir": hpnicfDot11SIDAPCir,
       "hpnicfDot11SIDAPCbs": hpnicfDot11SIDAPCbs,
       "hpnicfDot11SIDAPPriorityLevel": hpnicfDot11SIDAPPriorityLevel,
       "hpnicfDot11SIDAPElementID": hpnicfDot11SIDAPElementID,
       "hpnicfDot11SIDAPDevDetectEnable": hpnicfDot11SIDAPDevDetectEnable,
       "hpnicfDot11SIDAPStatisIntervMode": hpnicfDot11SIDAPStatisIntervMode,
       "hpnicfDot11SIDAPWorkModeCM": hpnicfDot11SIDAPWorkModeCM,
       "hpnicfDot11APSTVlanTable": hpnicfDot11APSTVlanTable,
       "hpnicfDot11APSTVlanEntry": hpnicfDot11APSTVlanEntry,
       "hpnicfDot11CfgSTVLANID": hpnicfDot11CfgSTVLANID,
       "hpnicfDot11CfgSTNASPortID": hpnicfDot11CfgSTNASPortID,
       "hpnicfDot11CfgServiceSetRowStatus": hpnicfDot11CfgServiceSetRowStatus,
       "hpnicfDot11CfgSTNASID": hpnicfDot11CfgSTNASID,
       "hpnicfDot11RadioIntfConfigGroup": hpnicfDot11RadioIntfConfigGroup,
       "hpnicfDot11RadioIntfConfigTable": hpnicfDot11RadioIntfConfigTable,
       "hpnicfDot11RadioIntfConfigEntry": hpnicfDot11RadioIntfConfigEntry,
       "hpnicfDot11RadioIfIdx": hpnicfDot11RadioIfIdx,
       "hpnicfDot11RadioCfgBeaconIntvl": hpnicfDot11RadioCfgBeaconIntvl,
       "hpnicfDot11RadioCfgDtimIntvl": hpnicfDot11RadioCfgDtimIntvl,
       "hpnicfDot11RadioCfgRtsThreshold": hpnicfDot11RadioCfgRtsThreshold,
       "hpnicfDot11RadioCfgFragThreshold": hpnicfDot11RadioCfgFragThreshold,
       "hpnicfDot11RadioCfgShtRetryThld": hpnicfDot11RadioCfgShtRetryThld,
       "hpnicfDot11RadioCfglongRtrThld": hpnicfDot11RadioCfglongRtrThld,
       "hpnicfDot11RadioCfgMaxRxLifetime": hpnicfDot11RadioCfgMaxRxLifetime,
       "hpnicfDot11RadioCfgType": hpnicfDot11RadioCfgType,
       "hpnicfDot11RadioCfgChannel": hpnicfDot11RadioCfgChannel,
       "hpnicfDot11RadioCfgMaxTxPwrLvl": hpnicfDot11RadioCfgMaxTxPwrLvl,
       "hpnicfDot11RadioCfgPreambleLen": hpnicfDot11RadioCfgPreambleLen,
       "hpnicfDot11RadioCfgWorkMode": hpnicfDot11RadioCfgWorkMode,
       "hpnicfDot11RadioCfgOnly11gEnable": hpnicfDot11RadioCfgOnly11gEnable,
       "hpnicfDot11RadioCfgType2": hpnicfDot11RadioCfgType2,
       "hpnicfDot11RadioCfgRssithresholdCM": hpnicfDot11RadioCfgRssithresholdCM,
       "hpnicfDot11RadioIntfBindTable": hpnicfDot11RadioIntfBindTable,
       "hpnicfDot11RadioIntfBindEntry": hpnicfDot11RadioIntfBindEntry,
       "hpnicfDot11RadioIntfBindSvcPlcyID": hpnicfDot11RadioIntfBindSvcPlcyID,
       "hpnicfDot11RadioIntfBindIfIdx": hpnicfDot11RadioIntfBindIfIdx,
       "hpnicfDot11RadioIntfBindRowStatus": hpnicfDot11RadioIntfBindRowStatus,
       "hpnicfDot11DataRateConfigGroup": hpnicfDot11DataRateConfigGroup,
       "hpnicfDot11DataRateConfigTable": hpnicfDot11DataRateConfigTable,
       "hpnicfDot11DataRateConfigEntry": hpnicfDot11DataRateConfigEntry,
       "hpnicfDot11RadioTypeID": hpnicfDot11RadioTypeID,
       "hpnicfDot11SupportedRateSet": hpnicfDot11SupportedRateSet,
       "hpnicfDot11MandatoryRateSet": hpnicfDot11MandatoryRateSet,
       "hpnicfDot11DisabledRateSet": hpnicfDot11DisabledRateSet,
       "hpnicfDot11SmartRateSet": hpnicfDot11SmartRateSet,
       "hpnicfDot11InterfaceConfigGroup": hpnicfDot11InterfaceConfigGroup,
       "hpnicfDot11WlanEssIfTable": hpnicfDot11WlanEssIfTable,
       "hpnicfDot11WlanEssIfEntry": hpnicfDot11WlanEssIfEntry,
       "hpnicfDot11WlanEssIfNumber": hpnicfDot11WlanEssIfNumber,
       "hpnicfDot11WlanEssIfIndex": hpnicfDot11WlanEssIfIndex,
       "hpnicfDot11WlanEssRowStatus": hpnicfDot11WlanEssRowStatus,
       "hpnicfDot11WlanBssIfTable": hpnicfDot11WlanBssIfTable,
       "hpnicfDot11WlanBssIfEntry": hpnicfDot11WlanBssIfEntry,
       "hpnicfDot11WlanBssIfNumber": hpnicfDot11WlanBssIfNumber,
       "hpnicfDot11WlanBssIfIndex": hpnicfDot11WlanBssIfIndex,
       "hpnicfDot11WlanBssRowStatus": hpnicfDot11WlanBssRowStatus,
       "hpnicfDot11WLANEthernetIfTable": hpnicfDot11WLANEthernetIfTable,
       "hpnicfDot11WLANEthernetIfEntry": hpnicfDot11WLANEthernetIfEntry,
       "hpnicfDot11WlanEthernetIfNumber": hpnicfDot11WlanEthernetIfNumber,
       "hpnicfDot11WLANEthernetIfIndex": hpnicfDot11WLANEthernetIfIndex,
       "hpnicfDot11WlanEthernetRowStatus": hpnicfDot11WlanEthernetRowStatus,
       "hpnicfDot11PortSecurityTable": hpnicfDot11PortSecurityTable,
       "hpnicfDot11PortSecurityEntry": hpnicfDot11PortSecurityEntry,
       "hpnicfDot11PortSecurityMode": hpnicfDot11PortSecurityMode,
       "hpnicfDot11SecurityUserLoginTxKeyType": hpnicfDot11SecurityUserLoginTxKeyType,
       "hpnicfDot11SecurityPskKeyMode": hpnicfDot11SecurityPskKeyMode,
       "hpnicfDot11SecurityPskKeyString": hpnicfDot11SecurityPskKeyString,
       "hpnicfDot11WlanMeshIfTable": hpnicfDot11WlanMeshIfTable,
       "hpnicfDot11WlanMeshIfEntry": hpnicfDot11WlanMeshIfEntry,
       "hpnicfDot11WlanMeshIfNumber": hpnicfDot11WlanMeshIfNumber,
       "hpnicfDot11WlanMeshIfIndex": hpnicfDot11WlanMeshIfIndex,
       "hpnicfDot11WlanMeshRowStatus": hpnicfDot11WlanMeshRowStatus,
       "hpnicfDot11ACBackupGroup": hpnicfDot11ACBackupGroup,
       "hpnicfDot11BackupACAdrssIP": hpnicfDot11BackupACAdrssIP,
       "hpnicfDot11BackupACAdrssIPv6": hpnicfDot11BackupACAdrssIPv6,
       "hpnicfDot11RadioElementConfigGroup": hpnicfDot11RadioElementConfigGroup,
       "hpnicfDot11nRadioCfgTable": hpnicfDot11nRadioCfgTable,
       "hpnicfDot11nRadioCfgEntry": hpnicfDot11nRadioCfgEntry,
       "hpnicfDot11nRadioCfgIndex": hpnicfDot11nRadioCfgIndex,
       "hpnicfDot11nAMpduEnable": hpnicfDot11nAMpduEnable,
       "hpnicfDot11nAMsduEnable": hpnicfDot11nAMsduEnable,
       "hpnicfDot11nClientDot11nOnly": hpnicfDot11nClientDot11nOnly,
       "hpnicfDot11nChanelBand": hpnicfDot11nChanelBand,
       "hpnicfDot11nShortGiEnable": hpnicfDot11nShortGiEnable,
       "hpnicfDot11nClientDot11acOnly": hpnicfDot11nClientDot11acOnly,
       "hpnicfDot11RadioWDSTable": hpnicfDot11RadioWDSTable,
       "hpnicfDot11RadioWDSEntry": hpnicfDot11RadioWDSEntry,
       "hpnicfDot11RadioWDSIndex": hpnicfDot11RadioWDSIndex,
       "hpnicfDot11RadioWDSMode": hpnicfDot11RadioWDSMode,
       "hpnicfDot11RadioWDSNetWorkID": hpnicfDot11RadioWDSNetWorkID,
       "hpnicfDot11WDSSecPskKeyMode": hpnicfDot11WDSSecPskKeyMode,
       "hpnicfDot11WDSSecPskKeyString": hpnicfDot11WDSSecPskKeyString,
       "hpnicfDot11nRadioCfg2Table": hpnicfDot11nRadioCfg2Table,
       "hpnicfDot11nRadioCfg2Entry": hpnicfDot11nRadioCfg2Entry,
       "hpnicfDot11nRadioCfg2APIDIndex": hpnicfDot11nRadioCfg2APIDIndex,
       "hpnicfDot11nRadioCfg2RadioIDIndex": hpnicfDot11nRadioCfg2RadioIDIndex,
       "hpnicfDot11nRadioCfg2AMpduEnable": hpnicfDot11nRadioCfg2AMpduEnable,
       "hpnicfDot11nRadioCfg2AMsduEnable": hpnicfDot11nRadioCfg2AMsduEnable,
       "hpnicfDot11nRadioCfg2ClientDot11nOnly": hpnicfDot11nRadioCfg2ClientDot11nOnly,
       "hpnicfDot11nRadioCfg2ChannelBand": hpnicfDot11nRadioCfg2ChannelBand,
       "hpnicfDot11nRadioCfg2ShortGiEnable": hpnicfDot11nRadioCfg2ShortGiEnable,
       "hpnicfDot11nRadioCfg2AMpduEnableCM": hpnicfDot11nRadioCfg2AMpduEnableCM,
       "hpnicfDot11nRadioCfg2ChannelBandCM": hpnicfDot11nRadioCfg2ChannelBandCM,
       "hpnicfDot11nRadioCfg2ShortGiEnableCM": hpnicfDot11nRadioCfg2ShortGiEnableCM,
       "hpnicfDot11nRadioCfg2ClientDot11acOnly": hpnicfDot11nRadioCfg2ClientDot11acOnly,
       "hpnicfDot11nRadioCfg2ClientDot11nOnlyCM": hpnicfDot11nRadioCfg2ClientDot11nOnlyCM,
       "hpnicfDot11CfgNotifyGroup": hpnicfDot11CfgNotifyGroup,
       "hpnicfDot11CfgNotifications": hpnicfDot11CfgNotifications,
       "hpnicfDot11CfgCipherChange": hpnicfDot11CfgCipherChange,
       "hpnicfDot11CfgPSKChange": hpnicfDot11CfgPSKChange,
       "hpnicfDot11SSIDWepIDConflictTrap": hpnicfDot11SSIDWepIDConflictTrap,
       "hpnicfDot11CfgTrapVarObjects": hpnicfDot11CfgTrapVarObjects,
       "hpnicfDot11PreConflictTemplateNum": hpnicfDot11PreConflictTemplateNum,
       "hpnicfDot11CurrConflictTemplateNum": hpnicfDot11CurrConflictTemplateNum,
       "hpnicfDot11ConflictCipherIdx": hpnicfDot11ConflictCipherIdx,
       "hpnicfDot11ConfigureAPID": hpnicfDot11ConfigureAPID,
       "hpnicfDot11ConfigureRadioID": hpnicfDot11ConfigureRadioID,
       "hpnicfDot11ConfigureAPMacAddress": hpnicfDot11ConfigureAPMacAddress}
)
