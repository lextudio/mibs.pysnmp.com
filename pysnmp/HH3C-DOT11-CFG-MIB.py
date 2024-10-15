# SNMP MIB module (HH3C-DOT11-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-CFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:50 2024
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

(Hh3cDot11AuthenType,
 Hh3cDot11ChannelScopeType,
 Hh3cDot11CirMode,
 Hh3cDot11ObjectIDType,
 Hh3cDot11PreambleType,
 Hh3cDot11RadioElementIndex,
 Hh3cDot11RadioScopeType,
 Hh3cDot11RadioType,
 Hh3cDot11SSIDEncryptModeType,
 Hh3cDot11SSIDStringType,
 Hh3cDot11SecIEStatusType,
 Hh3cDot11ServicePolicyIDType,
 Hh3cDot11TunnelSecSchemType,
 Hh3cDot11TxPwrLevelScopeType,
 Hh3cDot11WorkMode,
 hh3cDot11,
 hh3cDot11APElementIndex) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11AuthenType",
    "Hh3cDot11ChannelScopeType",
    "Hh3cDot11CirMode",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11PreambleType",
    "Hh3cDot11RadioElementIndex",
    "Hh3cDot11RadioScopeType",
    "Hh3cDot11RadioType",
    "Hh3cDot11SSIDEncryptModeType",
    "Hh3cDot11SSIDStringType",
    "Hh3cDot11SecIEStatusType",
    "Hh3cDot11ServicePolicyIDType",
    "Hh3cDot11TunnelSecSchemType",
    "Hh3cDot11TxPwrLevelScopeType",
    "Hh3cDot11WorkMode",
    "hh3cDot11",
    "hh3cDot11APElementIndex")

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

hh3cDot11CFG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4)
)
hh3cDot11CFG.setRevisions(
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

_Hh3cDot11GlobeConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11GlobeConfigGroup = _Hh3cDot11GlobeConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1)
)


class _Hh3cDot11GlobalCountryCode_Type(OctetString):
    """Custom type hh3cDot11GlobalCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Hh3cDot11GlobalCountryCode_Type.__name__ = "OctetString"
_Hh3cDot11GlobalCountryCode_Object = MibScalar
hh3cDot11GlobalCountryCode = _Hh3cDot11GlobalCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 1),
    _Hh3cDot11GlobalCountryCode_Type()
)
hh3cDot11GlobalCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11GlobalCountryCode.setStatus("current")


class _Hh3cDot11StaKeepALiveTimerIntvl_Type(Unsigned32):
    """Custom type hh3cDot11StaKeepALiveTimerIntvl based on Unsigned32"""
    defaultValue = 0


_Hh3cDot11StaKeepALiveTimerIntvl_Object = MibScalar
hh3cDot11StaKeepALiveTimerIntvl = _Hh3cDot11StaKeepALiveTimerIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 2),
    _Hh3cDot11StaKeepALiveTimerIntvl_Type()
)
hh3cDot11StaKeepALiveTimerIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11StaKeepALiveTimerIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StaKeepALiveTimerIntvl.setUnits("second")
_Hh3cDot11StaIdleTimerIntvl_Type = Integer32
_Hh3cDot11StaIdleTimerIntvl_Object = MibScalar
hh3cDot11StaIdleTimerIntvl = _Hh3cDot11StaIdleTimerIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 3),
    _Hh3cDot11StaIdleTimerIntvl_Type()
)
hh3cDot11StaIdleTimerIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11StaIdleTimerIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StaIdleTimerIntvl.setUnits("second")


class _Hh3cDot11BroadcastProbeReply_Type(TruthValue):
    """Custom type hh3cDot11BroadcastProbeReply based on TruthValue"""


_Hh3cDot11BroadcastProbeReply_Object = MibScalar
hh3cDot11BroadcastProbeReply = _Hh3cDot11BroadcastProbeReply_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 4),
    _Hh3cDot11BroadcastProbeReply_Type()
)
hh3cDot11BroadcastProbeReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11BroadcastProbeReply.setStatus("current")


class _Hh3cDot11APScanMode_Type(Integer32):
    """Custom type hh3cDot11APScanMode based on Integer32"""
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


_Hh3cDot11APScanMode_Type.__name__ = "Integer32"
_Hh3cDot11APScanMode_Object = MibScalar
hh3cDot11APScanMode = _Hh3cDot11APScanMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 5),
    _Hh3cDot11APScanMode_Type()
)
hh3cDot11APScanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APScanMode.setStatus("current")
_Hh3cDot11ACCtrlTunnelSecSupport_Type = Hh3cDot11TunnelSecSchemType
_Hh3cDot11ACCtrlTunnelSecSupport_Object = MibScalar
hh3cDot11ACCtrlTunnelSecSupport = _Hh3cDot11ACCtrlTunnelSecSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 6),
    _Hh3cDot11ACCtrlTunnelSecSupport_Type()
)
hh3cDot11ACCtrlTunnelSecSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ACCtrlTunnelSecSupport.setStatus("current")


class _Hh3cDot11ACDataTunnelSecSupport_Type(Hh3cDot11TunnelSecSchemType):
    """Custom type hh3cDot11ACDataTunnelSecSupport based on Hh3cDot11TunnelSecSchemType"""


_Hh3cDot11ACDataTunnelSecSupport_Object = MibScalar
hh3cDot11ACDataTunnelSecSupport = _Hh3cDot11ACDataTunnelSecSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 7),
    _Hh3cDot11ACDataTunnelSecSupport_Type()
)
hh3cDot11ACDataTunnelSecSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ACDataTunnelSecSupport.setStatus("current")


class _Hh3cDot11ACAutoAPSupport_Type(TruthValue):
    """Custom type hh3cDot11ACAutoAPSupport based on TruthValue"""


_Hh3cDot11ACAutoAPSupport_Object = MibScalar
hh3cDot11ACAutoAPSupport = _Hh3cDot11ACAutoAPSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 8),
    _Hh3cDot11ACAutoAPSupport_Type()
)
hh3cDot11ACAutoAPSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ACAutoAPSupport.setStatus("current")


class _Hh3cDot11AutoAPName_Type(OctetString):
    """Custom type hh3cDot11AutoAPName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11AutoAPName_Type.__name__ = "OctetString"
_Hh3cDot11AutoAPName_Object = MibScalar
hh3cDot11AutoAPName = _Hh3cDot11AutoAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 9),
    _Hh3cDot11AutoAPName_Type()
)
hh3cDot11AutoAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11AutoAPName.setStatus("current")


class _Hh3cDot11PersistentName_Type(OctetString):
    """Custom type hh3cDot11PersistentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11PersistentName_Type.__name__ = "OctetString"
_Hh3cDot11PersistentName_Object = MibScalar
hh3cDot11PersistentName = _Hh3cDot11PersistentName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 10),
    _Hh3cDot11PersistentName_Type()
)
hh3cDot11PersistentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11PersistentName.setStatus("current")
_Hh3cDot11IntfTrapThreshold_Type = Integer32
_Hh3cDot11IntfTrapThreshold_Object = MibScalar
hh3cDot11IntfTrapThreshold = _Hh3cDot11IntfTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 11),
    _Hh3cDot11IntfTrapThreshold_Type()
)
hh3cDot11IntfTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11IntfTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11IntfTrapThreshold.setUnits("dbm")


class _Hh3cDot11MonitorInterval_Type(Unsigned32):
    """Custom type hh3cDot11MonitorInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 15),
    )


_Hh3cDot11MonitorInterval_Type.__name__ = "Unsigned32"
_Hh3cDot11MonitorInterval_Object = MibScalar
hh3cDot11MonitorInterval = _Hh3cDot11MonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 12),
    _Hh3cDot11MonitorInterval_Type()
)
hh3cDot11MonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11MonitorInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11MonitorInterval.setUnits("minute")


class _Hh3cDot11SampleInterval_Type(Unsigned32):
    """Custom type hh3cDot11SampleInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 300),
    )


_Hh3cDot11SampleInterval_Type.__name__ = "Unsigned32"
_Hh3cDot11SampleInterval_Object = MibScalar
hh3cDot11SampleInterval = _Hh3cDot11SampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 13),
    _Hh3cDot11SampleInterval_Type()
)
hh3cDot11SampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SampleInterval.setUnits("second")


class _Hh3cDot11ChnlSwitChkInterval_Type(Unsigned32):
    """Custom type hh3cDot11ChnlSwitChkInterval based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 180),
    )


_Hh3cDot11ChnlSwitChkInterval_Type.__name__ = "Unsigned32"
_Hh3cDot11ChnlSwitChkInterval_Object = MibScalar
hh3cDot11ChnlSwitChkInterval = _Hh3cDot11ChnlSwitChkInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 14),
    _Hh3cDot11ChnlSwitChkInterval_Type()
)
hh3cDot11ChnlSwitChkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ChnlSwitChkInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11ChnlSwitChkInterval.setUnits("minute")


class _Hh3cDot11APUserUplimit_Type(Unsigned32):
    """Custom type hh3cDot11APUserUplimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11APUserUplimit_Type.__name__ = "Unsigned32"
_Hh3cDot11APUserUplimit_Object = MibScalar
hh3cDot11APUserUplimit = _Hh3cDot11APUserUplimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 15),
    _Hh3cDot11APUserUplimit_Type()
)
hh3cDot11APUserUplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APUserUplimit.setStatus("current")


class _Hh3cDot11APL2IsolateEnable_Type(TruthValue):
    """Custom type hh3cDot11APL2IsolateEnable based on TruthValue"""


_Hh3cDot11APL2IsolateEnable_Object = MibScalar
hh3cDot11APL2IsolateEnable = _Hh3cDot11APL2IsolateEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 16),
    _Hh3cDot11APL2IsolateEnable_Type()
)
hh3cDot11APL2IsolateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APL2IsolateEnable.setStatus("current")
_Hh3cDot11APBSSIDSupportNum_Type = Integer32
_Hh3cDot11APBSSIDSupportNum_Object = MibScalar
hh3cDot11APBSSIDSupportNum = _Hh3cDot11APBSSIDSupportNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 17),
    _Hh3cDot11APBSSIDSupportNum_Type()
)
hh3cDot11APBSSIDSupportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APBSSIDSupportNum.setStatus("current")
_Hh3cDot11APLastUpdateStatTime_Type = DateAndTime
_Hh3cDot11APLastUpdateStatTime_Object = MibScalar
hh3cDot11APLastUpdateStatTime = _Hh3cDot11APLastUpdateStatTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 18),
    _Hh3cDot11APLastUpdateStatTime_Type()
)
hh3cDot11APLastUpdateStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APLastUpdateStatTime.setStatus("current")


class _Hh3cDot11APDoSProtectEnable_Type(TruthValue):
    """Custom type hh3cDot11APDoSProtectEnable based on TruthValue"""


_Hh3cDot11APDoSProtectEnable_Object = MibScalar
hh3cDot11APDoSProtectEnable = _Hh3cDot11APDoSProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 19),
    _Hh3cDot11APDoSProtectEnable_Type()
)
hh3cDot11APDoSProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APDoSProtectEnable.setStatus("current")


class _Hh3cDot11MaxAPPerIf_Type(Unsigned32):
    """Custom type hh3cDot11MaxAPPerIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11MaxAPPerIf_Type.__name__ = "Unsigned32"
_Hh3cDot11MaxAPPerIf_Object = MibScalar
hh3cDot11MaxAPPerIf = _Hh3cDot11MaxAPPerIf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 20),
    _Hh3cDot11MaxAPPerIf_Type()
)
hh3cDot11MaxAPPerIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11MaxAPPerIf.setStatus("current")
_Hh3cDot11SampleTimeStamp_Type = DateAndTime
_Hh3cDot11SampleTimeStamp_Object = MibScalar
hh3cDot11SampleTimeStamp = _Hh3cDot11SampleTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 21),
    _Hh3cDot11SampleTimeStamp_Type()
)
hh3cDot11SampleTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SampleTimeStamp.setStatus("current")


class _Hh3cDot11UplinkTrackId_Type(Unsigned32):
    """Custom type hh3cDot11UplinkTrackId based on Unsigned32"""
    defaultValue = 0


_Hh3cDot11UplinkTrackId_Object = MibScalar
hh3cDot11UplinkTrackId = _Hh3cDot11UplinkTrackId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 22),
    _Hh3cDot11UplinkTrackId_Type()
)
hh3cDot11UplinkTrackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11UplinkTrackId.setStatus("current")


class _Hh3cDot11RtCollectSwitch_Type(TruthValue):
    """Custom type hh3cDot11RtCollectSwitch based on TruthValue"""


_Hh3cDot11RtCollectSwitch_Object = MibScalar
hh3cDot11RtCollectSwitch = _Hh3cDot11RtCollectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 23),
    _Hh3cDot11RtCollectSwitch_Type()
)
hh3cDot11RtCollectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RtCollectSwitch.setStatus("current")
_Hh3cDot11RglCollectIntvl_Type = Integer32
_Hh3cDot11RglCollectIntvl_Object = MibScalar
hh3cDot11RglCollectIntvl = _Hh3cDot11RglCollectIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 24),
    _Hh3cDot11RglCollectIntvl_Type()
)
hh3cDot11RglCollectIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RglCollectIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RglCollectIntvl.setUnits("second")
_Hh3cDot11RtCollectIntvl_Type = Integer32
_Hh3cDot11RtCollectIntvl_Object = MibScalar
hh3cDot11RtCollectIntvl = _Hh3cDot11RtCollectIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 25),
    _Hh3cDot11RtCollectIntvl_Type()
)
hh3cDot11RtCollectIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RtCollectIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RtCollectIntvl.setUnits("second")


class _Hh3cDot11AllAPCpuUsageThreshold_Type(Integer32):
    """Custom type hh3cDot11AllAPCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11AllAPCpuUsageThreshold_Type.__name__ = "Integer32"
_Hh3cDot11AllAPCpuUsageThreshold_Object = MibScalar
hh3cDot11AllAPCpuUsageThreshold = _Hh3cDot11AllAPCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 26),
    _Hh3cDot11AllAPCpuUsageThreshold_Type()
)
hh3cDot11AllAPCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11AllAPCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11AllAPCpuUsageThreshold.setUnits("onepercent")


class _Hh3cDot11AllAPMemUsageThreshold_Type(Integer32):
    """Custom type hh3cDot11AllAPMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11AllAPMemUsageThreshold_Type.__name__ = "Integer32"
_Hh3cDot11AllAPMemUsageThreshold_Object = MibScalar
hh3cDot11AllAPMemUsageThreshold = _Hh3cDot11AllAPMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 27),
    _Hh3cDot11AllAPMemUsageThreshold_Type()
)
hh3cDot11AllAPMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11AllAPMemUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11AllAPMemUsageThreshold.setUnits("onepercent")
_Hh3cDot11AdjIntfTrapThreshold_Type = Integer32
_Hh3cDot11AdjIntfTrapThreshold_Object = MibScalar
hh3cDot11AdjIntfTrapThreshold = _Hh3cDot11AdjIntfTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 28),
    _Hh3cDot11AdjIntfTrapThreshold_Type()
)
hh3cDot11AdjIntfTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11AdjIntfTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11AdjIntfTrapThreshold.setUnits("dbm")
_Hh3cDot11PolicyConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11PolicyConfigGroup = _Hh3cDot11PolicyConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2)
)
_Hh3cDot11RadioPolicyTable_Object = MibTable
hh3cDot11RadioPolicyTable = _Hh3cDot11RadioPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioPolicyTable.setStatus("current")
_Hh3cDot11RadioPolicyEntry_Object = MibTableRow
hh3cDot11RadioPolicyEntry = _Hh3cDot11RadioPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1)
)
hh3cDot11RadioPolicyEntry.setIndexNames(
    (1, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioPolicyEntry.setStatus("current")


class _Hh3cDot11RadioPolicyName_Type(OctetString):
    """Custom type hh3cDot11RadioPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11RadioPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11RadioPolicyName_Object = MibTableColumn
hh3cDot11RadioPolicyName = _Hh3cDot11RadioPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 1),
    _Hh3cDot11RadioPolicyName_Type()
)
hh3cDot11RadioPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioPolicyName.setStatus("current")


class _Hh3cDot11BeaconInterval_Type(Integer32):
    """Custom type hh3cDot11BeaconInterval based on Integer32"""
    defaultValue = 100


_Hh3cDot11BeaconInterval_Object = MibTableColumn
hh3cDot11BeaconInterval = _Hh3cDot11BeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 2),
    _Hh3cDot11BeaconInterval_Type()
)
hh3cDot11BeaconInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11BeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11BeaconInterval.setUnits("TU")


class _Hh3cDot11DtimInterval_Type(Integer32):
    """Custom type hh3cDot11DtimInterval based on Integer32"""
    defaultValue = 1


_Hh3cDot11DtimInterval_Object = MibTableColumn
hh3cDot11DtimInterval = _Hh3cDot11DtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 3),
    _Hh3cDot11DtimInterval_Type()
)
hh3cDot11DtimInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11DtimInterval.setStatus("current")


class _Hh3cDot11RtsThreshold_Type(Integer32):
    """Custom type hh3cDot11RtsThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11RtsThreshold_Object = MibTableColumn
hh3cDot11RtsThreshold = _Hh3cDot11RtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 4),
    _Hh3cDot11RtsThreshold_Type()
)
hh3cDot11RtsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RtsThreshold.setUnits("byte")


class _Hh3cDot11FragThreshold_Type(Integer32):
    """Custom type hh3cDot11FragThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11FragThreshold_Object = MibTableColumn
hh3cDot11FragThreshold = _Hh3cDot11FragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 5),
    _Hh3cDot11FragThreshold_Type()
)
hh3cDot11FragThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11FragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11FragThreshold.setUnits("byte")


class _Hh3cDot11ShortRetryThreshold_Type(Integer32):
    """Custom type hh3cDot11ShortRetryThreshold based on Integer32"""
    defaultValue = 7


_Hh3cDot11ShortRetryThreshold_Object = MibTableColumn
hh3cDot11ShortRetryThreshold = _Hh3cDot11ShortRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 6),
    _Hh3cDot11ShortRetryThreshold_Type()
)
hh3cDot11ShortRetryThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11ShortRetryThreshold.setStatus("current")


class _Hh3cDot11LongRetryThreshold_Type(Integer32):
    """Custom type hh3cDot11LongRetryThreshold based on Integer32"""
    defaultValue = 4


_Hh3cDot11LongRetryThreshold_Object = MibTableColumn
hh3cDot11LongRetryThreshold = _Hh3cDot11LongRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 7),
    _Hh3cDot11LongRetryThreshold_Type()
)
hh3cDot11LongRetryThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11LongRetryThreshold.setStatus("current")


class _Hh3cDot11MaxRxLifetime_Type(Unsigned32):
    """Custom type hh3cDot11MaxRxLifetime based on Unsigned32"""
    defaultValue = 2000


_Hh3cDot11MaxRxLifetime_Object = MibTableColumn
hh3cDot11MaxRxLifetime = _Hh3cDot11MaxRxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 8),
    _Hh3cDot11MaxRxLifetime_Type()
)
hh3cDot11MaxRxLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11MaxRxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11MaxRxLifetime.setUnits("millisecond")
_Hh3cDot11RdoPolicyRowStatus_Type = RowStatus
_Hh3cDot11RdoPolicyRowStatus_Object = MibTableColumn
hh3cDot11RdoPolicyRowStatus = _Hh3cDot11RdoPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 9),
    _Hh3cDot11RdoPolicyRowStatus_Type()
)
hh3cDot11RdoPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RdoPolicyRowStatus.setStatus("current")


class _Hh3cDot11RdoClientMaxCount_Type(Integer32):
    """Custom type hh3cDot11RdoClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDot11RdoClientMaxCount_Type.__name__ = "Integer32"
_Hh3cDot11RdoClientMaxCount_Object = MibTableColumn
hh3cDot11RdoClientMaxCount = _Hh3cDot11RdoClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 10),
    _Hh3cDot11RdoClientMaxCount_Type()
)
hh3cDot11RdoClientMaxCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RdoClientMaxCount.setStatus("current")
_Hh3cDot11BeaconIntervalMs_Type = Integer32
_Hh3cDot11BeaconIntervalMs_Object = MibTableColumn
hh3cDot11BeaconIntervalMs = _Hh3cDot11BeaconIntervalMs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 11),
    _Hh3cDot11BeaconIntervalMs_Type()
)
hh3cDot11BeaconIntervalMs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11BeaconIntervalMs.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11BeaconIntervalMs.setUnits("ms")
_Hh3cDot11ServicePolicyTable_Object = MibTable
hh3cDot11ServicePolicyTable = _Hh3cDot11ServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyTable.setStatus("current")
_Hh3cDot11ServicePolicyEntry_Object = MibTableRow
hh3cDot11ServicePolicyEntry = _Hh3cDot11ServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1)
)
hh3cDot11ServicePolicyEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11ServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyEntry.setStatus("current")
_Hh3cDot11ServicePolicyID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11ServicePolicyID_Object = MibTableColumn
hh3cDot11ServicePolicyID = _Hh3cDot11ServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 1),
    _Hh3cDot11ServicePolicyID_Type()
)
hh3cDot11ServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyID.setStatus("current")
_Hh3cDot11SSIDName_Type = Hh3cDot11SSIDStringType
_Hh3cDot11SSIDName_Object = MibTableColumn
hh3cDot11SSIDName = _Hh3cDot11SSIDName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 2),
    _Hh3cDot11SSIDName_Type()
)
hh3cDot11SSIDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SSIDName.setStatus("current")


class _Hh3cDot11SSIDHidden_Type(TruthValue):
    """Custom type hh3cDot11SSIDHidden based on TruthValue"""


_Hh3cDot11SSIDHidden_Object = MibTableColumn
hh3cDot11SSIDHidden = _Hh3cDot11SSIDHidden_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 3),
    _Hh3cDot11SSIDHidden_Type()
)
hh3cDot11SSIDHidden.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SSIDHidden.setStatus("current")
_Hh3cDot11AuthenMode_Type = Hh3cDot11AuthenType
_Hh3cDot11AuthenMode_Object = MibTableColumn
hh3cDot11AuthenMode = _Hh3cDot11AuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 4),
    _Hh3cDot11AuthenMode_Type()
)
hh3cDot11AuthenMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11AuthenMode.setStatus("current")
_Hh3cDot11SSIDEncryptionMode_Type = Hh3cDot11SSIDEncryptModeType
_Hh3cDot11SSIDEncryptionMode_Object = MibTableColumn
hh3cDot11SSIDEncryptionMode = _Hh3cDot11SSIDEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 5),
    _Hh3cDot11SSIDEncryptionMode_Type()
)
hh3cDot11SSIDEncryptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SSIDEncryptionMode.setStatus("current")


class _Hh3cDot11WlanInfBindingType_Type(OctetString):
    """Custom type hh3cDot11WlanInfBindingType based on OctetString"""
    defaultValue = OctetString("WLAN-ESS")


_Hh3cDot11WlanInfBindingType_Object = MibTableColumn
hh3cDot11WlanInfBindingType = _Hh3cDot11WlanInfBindingType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 6),
    _Hh3cDot11WlanInfBindingType_Type()
)
hh3cDot11WlanInfBindingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanInfBindingType.setStatus("current")
_Hh3cDot11WlanInfBindingID_Type = Integer32
_Hh3cDot11WlanInfBindingID_Object = MibTableColumn
hh3cDot11WlanInfBindingID = _Hh3cDot11WlanInfBindingID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 7),
    _Hh3cDot11WlanInfBindingID_Type()
)
hh3cDot11WlanInfBindingID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanInfBindingID.setStatus("current")
_Hh3cDot11SrvPolicyRowStatus_Type = RowStatus
_Hh3cDot11SrvPolicyRowStatus_Object = MibTableColumn
hh3cDot11SrvPolicyRowStatus = _Hh3cDot11SrvPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 8),
    _Hh3cDot11SrvPolicyRowStatus_Type()
)
hh3cDot11SrvPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SrvPolicyRowStatus.setStatus("current")


class _Hh3cDot11ClientMaxCount_Type(Integer32):
    """Custom type hh3cDot11ClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDot11ClientMaxCount_Type.__name__ = "Integer32"
_Hh3cDot11ClientMaxCount_Object = MibTableColumn
hh3cDot11ClientMaxCount = _Hh3cDot11ClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 9),
    _Hh3cDot11ClientMaxCount_Type()
)
hh3cDot11ClientMaxCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11ClientMaxCount.setStatus("current")


class _Hh3cDot11SPInCirMode_Type(Hh3cDot11CirMode):
    """Custom type hh3cDot11SPInCirMode based on Hh3cDot11CirMode"""


_Hh3cDot11SPInCirMode_Object = MibTableColumn
hh3cDot11SPInCirMode = _Hh3cDot11SPInCirMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 10),
    _Hh3cDot11SPInCirMode_Type()
)
hh3cDot11SPInCirMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPInCirMode.setStatus("current")


class _Hh3cDot11SPInCirValue_Type(Integer32):
    """Custom type hh3cDot11SPInCirValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11SPInCirValue_Object = MibTableColumn
hh3cDot11SPInCirValue = _Hh3cDot11SPInCirValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 11),
    _Hh3cDot11SPInCirValue_Type()
)
hh3cDot11SPInCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPInCirValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SPInCirValue.setUnits("Kbps")


class _Hh3cDot11SPOutCirMode_Type(Hh3cDot11CirMode):
    """Custom type hh3cDot11SPOutCirMode based on Hh3cDot11CirMode"""


_Hh3cDot11SPOutCirMode_Object = MibTableColumn
hh3cDot11SPOutCirMode = _Hh3cDot11SPOutCirMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 12),
    _Hh3cDot11SPOutCirMode_Type()
)
hh3cDot11SPOutCirMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCirMode.setStatus("current")


class _Hh3cDot11SPOutCirValue_Type(Integer32):
    """Custom type hh3cDot11SPOutCirValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11SPOutCirValue_Object = MibTableColumn
hh3cDot11SPOutCirValue = _Hh3cDot11SPOutCirValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 13),
    _Hh3cDot11SPOutCirValue_Type()
)
hh3cDot11SPOutCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCirValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCirValue.setUnits("Kbps")


class _Hh3cDot11WlanInfPVID_Type(Integer32):
    """Custom type hh3cDot11WlanInfPVID based on Integer32"""
    defaultValue = 1


_Hh3cDot11WlanInfPVID_Object = MibTableColumn
hh3cDot11WlanInfPVID = _Hh3cDot11WlanInfPVID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 14),
    _Hh3cDot11WlanInfPVID_Type()
)
hh3cDot11WlanInfPVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanInfPVID.setStatus("current")


class _Hh3cDot11SPInCirStaticValue_Type(Integer32):
    """Custom type hh3cDot11SPInCirStaticValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11SPInCirStaticValue_Object = MibTableColumn
hh3cDot11SPInCirStaticValue = _Hh3cDot11SPInCirStaticValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 15),
    _Hh3cDot11SPInCirStaticValue_Type()
)
hh3cDot11SPInCirStaticValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPInCirStaticValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SPInCirStaticValue.setUnits("Kbps")


class _Hh3cDot11SPOutCirStaticValue_Type(Integer32):
    """Custom type hh3cDot11SPOutCirStaticValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11SPOutCirStaticValue_Object = MibTableColumn
hh3cDot11SPOutCirStaticValue = _Hh3cDot11SPOutCirStaticValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 16),
    _Hh3cDot11SPOutCirStaticValue_Type()
)
hh3cDot11SPOutCirStaticValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCirStaticValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCirStaticValue.setUnits("Kbps")


class _Hh3cDot11SPIsolate_Type(TruthValue):
    """Custom type hh3cDot11SPIsolate based on TruthValue"""


_Hh3cDot11SPIsolate_Object = MibTableColumn
hh3cDot11SPIsolate = _Hh3cDot11SPIsolate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 17),
    _Hh3cDot11SPIsolate_Type()
)
hh3cDot11SPIsolate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPIsolate.setStatus("current")
_Hh3cDot11ServicePolicyExtTable_Object = MibTable
hh3cDot11ServicePolicyExtTable = _Hh3cDot11ServicePolicyExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyExtTable.setStatus("current")
_Hh3cDot11ServicePolicyExtEntry_Object = MibTableRow
hh3cDot11ServicePolicyExtEntry = _Hh3cDot11ServicePolicyExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1)
)
hh3cDot11ServicePolicyExtEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11ServicePolicyExtID"),
)
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyExtEntry.setStatus("current")
_Hh3cDot11ServicePolicyExtID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11ServicePolicyExtID_Object = MibTableColumn
hh3cDot11ServicePolicyExtID = _Hh3cDot11ServicePolicyExtID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 1),
    _Hh3cDot11ServicePolicyExtID_Type()
)
hh3cDot11ServicePolicyExtID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyExtID.setStatus("current")
_Hh3cDot11SecIEStatus_Type = Hh3cDot11SecIEStatusType
_Hh3cDot11SecIEStatus_Object = MibTableColumn
hh3cDot11SecIEStatus = _Hh3cDot11SecIEStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 2),
    _Hh3cDot11SecIEStatus_Type()
)
hh3cDot11SecIEStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SecIEStatus.setStatus("current")
_Hh3cDot11SecurityCiphers_Type = Integer32
_Hh3cDot11SecurityCiphers_Object = MibTableColumn
hh3cDot11SecurityCiphers = _Hh3cDot11SecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 3),
    _Hh3cDot11SecurityCiphers_Type()
)
hh3cDot11SecurityCiphers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SecurityCiphers.setStatus("current")


class _Hh3cDot11CipherKeyIndex_Type(Integer32):
    """Custom type hh3cDot11CipherKeyIndex based on Integer32"""
    defaultValue = 1


_Hh3cDot11CipherKeyIndex_Object = MibTableColumn
hh3cDot11CipherKeyIndex = _Hh3cDot11CipherKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 4),
    _Hh3cDot11CipherKeyIndex_Type()
)
hh3cDot11CipherKeyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CipherKeyIndex.setStatus("current")
_Hh3cDot11CipherKey_Type = OctetString
_Hh3cDot11CipherKey_Object = MibTableColumn
hh3cDot11CipherKey = _Hh3cDot11CipherKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 5),
    _Hh3cDot11CipherKey_Type()
)
hh3cDot11CipherKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CipherKey.setStatus("current")
_Hh3cDot11SrvPolicyExtRowStatus_Type = RowStatus
_Hh3cDot11SrvPolicyExtRowStatus_Object = MibTableColumn
hh3cDot11SrvPolicyExtRowStatus = _Hh3cDot11SrvPolicyExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 6),
    _Hh3cDot11SrvPolicyExtRowStatus_Type()
)
hh3cDot11SrvPolicyExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SrvPolicyExtRowStatus.setStatus("current")


class _Hh3cDot11CipherKeyType_Type(Integer32):
    """Custom type hh3cDot11CipherKeyType based on Integer32"""
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


_Hh3cDot11CipherKeyType_Type.__name__ = "Integer32"
_Hh3cDot11CipherKeyType_Object = MibTableColumn
hh3cDot11CipherKeyType = _Hh3cDot11CipherKeyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 7),
    _Hh3cDot11CipherKeyType_Type()
)
hh3cDot11CipherKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CipherKeyType.setStatus("current")
_Hh3cDot11RadioPolicyExtTable_Object = MibTable
hh3cDot11RadioPolicyExtTable = _Hh3cDot11RadioPolicyExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioPolicyExtTable.setStatus("current")
_Hh3cDot11RadioPolicyExtEntry_Object = MibTableRow
hh3cDot11RadioPolicyExtEntry = _Hh3cDot11RadioPolicyExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1)
)
hh3cDot11RadioPolicyExtEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RPAPSerialID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RPRadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioPolicyExtEntry.setStatus("current")


class _Hh3cDot11RPAPSerialID_Type(OctetString):
    """Custom type hh3cDot11RPAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11RPAPSerialID_Type.__name__ = "OctetString"
_Hh3cDot11RPAPSerialID_Object = MibTableColumn
hh3cDot11RPAPSerialID = _Hh3cDot11RPAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 1),
    _Hh3cDot11RPAPSerialID_Type()
)
hh3cDot11RPAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RPAPSerialID.setStatus("current")
_Hh3cDot11RPRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11RPRadioID_Object = MibTableColumn
hh3cDot11RPRadioID = _Hh3cDot11RPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 2),
    _Hh3cDot11RPRadioID_Type()
)
hh3cDot11RPRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RPRadioID.setStatus("current")


class _Hh3cDot11RPBeaconInterval_Type(Integer32):
    """Custom type hh3cDot11RPBeaconInterval based on Integer32"""
    defaultValue = 100


_Hh3cDot11RPBeaconInterval_Object = MibTableColumn
hh3cDot11RPBeaconInterval = _Hh3cDot11RPBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 3),
    _Hh3cDot11RPBeaconInterval_Type()
)
hh3cDot11RPBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPBeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RPBeaconInterval.setUnits("milliseconds")


class _Hh3cDot11RPDtimInterval_Type(Integer32):
    """Custom type hh3cDot11RPDtimInterval based on Integer32"""
    defaultValue = 1


_Hh3cDot11RPDtimInterval_Object = MibTableColumn
hh3cDot11RPDtimInterval = _Hh3cDot11RPDtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 4),
    _Hh3cDot11RPDtimInterval_Type()
)
hh3cDot11RPDtimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPDtimInterval.setStatus("current")


class _Hh3cDot11RPRtsThreshold_Type(Integer32):
    """Custom type hh3cDot11RPRtsThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11RPRtsThreshold_Object = MibTableColumn
hh3cDot11RPRtsThreshold = _Hh3cDot11RPRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 5),
    _Hh3cDot11RPRtsThreshold_Type()
)
hh3cDot11RPRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPRtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RPRtsThreshold.setUnits("byte")


class _Hh3cDot11RPFragThreshold_Type(Integer32):
    """Custom type hh3cDot11RPFragThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11RPFragThreshold_Object = MibTableColumn
hh3cDot11RPFragThreshold = _Hh3cDot11RPFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 6),
    _Hh3cDot11RPFragThreshold_Type()
)
hh3cDot11RPFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPFragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RPFragThreshold.setUnits("byte")


class _Hh3cDot11RPShortRetryThreshold_Type(Integer32):
    """Custom type hh3cDot11RPShortRetryThreshold based on Integer32"""
    defaultValue = 7


_Hh3cDot11RPShortRetryThreshold_Object = MibTableColumn
hh3cDot11RPShortRetryThreshold = _Hh3cDot11RPShortRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 7),
    _Hh3cDot11RPShortRetryThreshold_Type()
)
hh3cDot11RPShortRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPShortRetryThreshold.setStatus("current")


class _Hh3cDot11RPLongRetryThreshold_Type(Integer32):
    """Custom type hh3cDot11RPLongRetryThreshold based on Integer32"""
    defaultValue = 4


_Hh3cDot11RPLongRetryThreshold_Object = MibTableColumn
hh3cDot11RPLongRetryThreshold = _Hh3cDot11RPLongRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 8),
    _Hh3cDot11RPLongRetryThreshold_Type()
)
hh3cDot11RPLongRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPLongRetryThreshold.setStatus("current")


class _Hh3cDot11RPClientMaxCount_Type(Integer32):
    """Custom type hh3cDot11RPClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDot11RPClientMaxCount_Type.__name__ = "Integer32"
_Hh3cDot11RPClientMaxCount_Object = MibTableColumn
hh3cDot11RPClientMaxCount = _Hh3cDot11RPClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 9),
    _Hh3cDot11RPClientMaxCount_Type()
)
hh3cDot11RPClientMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPClientMaxCount.setStatus("current")
_Hh3cDot11SrvPortSecurityTable_Object = MibTable
hh3cDot11SrvPortSecurityTable = _Hh3cDot11SrvPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11SrvPortSecurityTable.setStatus("current")
_Hh3cDot11SrvPortSecurityEntry_Object = MibTableRow
hh3cDot11SrvPortSecurityEntry = _Hh3cDot11SrvPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1)
)
hh3cDot11SrvPortSecurityEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11SecurityServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11SrvPortSecurityEntry.setStatus("current")
_Hh3cDot11SecurityServicePolicyID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11SecurityServicePolicyID_Object = MibTableColumn
hh3cDot11SecurityServicePolicyID = _Hh3cDot11SecurityServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1, 1),
    _Hh3cDot11SecurityServicePolicyID_Type()
)
hh3cDot11SecurityServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SecurityServicePolicyID.setStatus("current")


class _Hh3cDot11SrvPortSecurityMode_Type(Integer32):
    """Custom type hh3cDot11SrvPortSecurityMode based on Integer32"""
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
        *(("macAddressAndPsk", 4),
          ("noRestrictions", 1),
          ("psk", 3),
          ("userLoginSecureExt", 2),
          ("userLoginSecureExtOrPsk", 5),
          ("wapi", 6))
    )


_Hh3cDot11SrvPortSecurityMode_Type.__name__ = "Integer32"
_Hh3cDot11SrvPortSecurityMode_Object = MibTableColumn
hh3cDot11SrvPortSecurityMode = _Hh3cDot11SrvPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1, 2),
    _Hh3cDot11SrvPortSecurityMode_Type()
)
hh3cDot11SrvPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SrvPortSecurityMode.setStatus("current")


class _Hh3cDot11SrvSecurityKeyType_Type(Integer32):
    """Custom type hh3cDot11SrvSecurityKeyType based on Integer32"""
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


_Hh3cDot11SrvSecurityKeyType_Type.__name__ = "Integer32"
_Hh3cDot11SrvSecurityKeyType_Object = MibTableColumn
hh3cDot11SrvSecurityKeyType = _Hh3cDot11SrvSecurityKeyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1, 3),
    _Hh3cDot11SrvSecurityKeyType_Type()
)
hh3cDot11SrvSecurityKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SrvSecurityKeyType.setStatus("current")


class _Hh3cDot11SrvSecurityPskKeyMode_Type(Integer32):
    """Custom type hh3cDot11SrvSecurityPskKeyMode based on Integer32"""
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


_Hh3cDot11SrvSecurityPskKeyMode_Type.__name__ = "Integer32"
_Hh3cDot11SrvSecurityPskKeyMode_Object = MibTableColumn
hh3cDot11SrvSecurityPskKeyMode = _Hh3cDot11SrvSecurityPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1, 4),
    _Hh3cDot11SrvSecurityPskKeyMode_Type()
)
hh3cDot11SrvSecurityPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SrvSecurityPskKeyMode.setStatus("current")


class _Hh3cDot11SrvSecurityPskKeyString_Type(DisplayString):
    """Custom type hh3cDot11SrvSecurityPskKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cDot11SrvSecurityPskKeyString_Type.__name__ = "DisplayString"
_Hh3cDot11SrvSecurityPskKeyString_Object = MibTableColumn
hh3cDot11SrvSecurityPskKeyString = _Hh3cDot11SrvSecurityPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1, 5),
    _Hh3cDot11SrvSecurityPskKeyString_Type()
)
hh3cDot11SrvSecurityPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SrvSecurityPskKeyString.setStatus("current")
_Hh3cDot11SrvPolicyExtendTable_Object = MibTable
hh3cDot11SrvPolicyExtendTable = _Hh3cDot11SrvPolicyExtendTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11SrvPolicyExtendTable.setStatus("current")
_Hh3cDot11SrvPolicyExtendEntry_Object = MibTableRow
hh3cDot11SrvPolicyExtendEntry = _Hh3cDot11SrvPolicyExtendEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 6, 1)
)
hh3cDot11SrvPolicyExtendEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11ServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11SrvPolicyExtendEntry.setStatus("current")


class _Hh3cDot11SPEnable_Type(Integer32):
    """Custom type hh3cDot11SPEnable based on Integer32"""
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


_Hh3cDot11SPEnable_Type.__name__ = "Integer32"
_Hh3cDot11SPEnable_Object = MibTableColumn
hh3cDot11SPEnable = _Hh3cDot11SPEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 6, 1, 1),
    _Hh3cDot11SPEnable_Type()
)
hh3cDot11SPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SPEnable.setStatus("current")
_Hh3cDot11APConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11APConfigGroup = _Hh3cDot11APConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3)
)
_Hh3cDot11APTemplateTable_Object = MibTable
hh3cDot11APTemplateTable = _Hh3cDot11APTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11APTemplateTable.setStatus("current")
_Hh3cDot11APTemplateEntry_Object = MibTableRow
hh3cDot11APTemplateEntry = _Hh3cDot11APTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1)
)
hh3cDot11APTemplateEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APTemplateName"),
)
if mibBuilder.loadTexts:
    hh3cDot11APTemplateEntry.setStatus("current")


class _Hh3cDot11APTemplateName_Type(OctetString):
    """Custom type hh3cDot11APTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11APTemplateName_Type.__name__ = "OctetString"
_Hh3cDot11APTemplateName_Object = MibTableColumn
hh3cDot11APTemplateName = _Hh3cDot11APTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 1),
    _Hh3cDot11APTemplateName_Type()
)
hh3cDot11APTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APTemplateName.setStatus("current")
_Hh3cDot11APSerialID_Type = OctetString
_Hh3cDot11APSerialID_Object = MibTableColumn
hh3cDot11APSerialID = _Hh3cDot11APSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 2),
    _Hh3cDot11APSerialID_Type()
)
hh3cDot11APSerialID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APSerialID.setStatus("current")
_Hh3cDot11TemplateAPModelAlias_Type = OctetString
_Hh3cDot11TemplateAPModelAlias_Object = MibTableColumn
hh3cDot11TemplateAPModelAlias = _Hh3cDot11TemplateAPModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 3),
    _Hh3cDot11TemplateAPModelAlias_Type()
)
hh3cDot11TemplateAPModelAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11TemplateAPModelAlias.setStatus("current")
_Hh3cDot11Description_Type = OctetString
_Hh3cDot11Description_Object = MibTableColumn
hh3cDot11Description = _Hh3cDot11Description_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 4),
    _Hh3cDot11Description_Type()
)
hh3cDot11Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11Description.setStatus("current")


class _Hh3cDot11APWorkMode_Type(Integer32):
    """Custom type hh3cDot11APWorkMode based on Integer32"""
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


_Hh3cDot11APWorkMode_Type.__name__ = "Integer32"
_Hh3cDot11APWorkMode_Object = MibTableColumn
hh3cDot11APWorkMode = _Hh3cDot11APWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 5),
    _Hh3cDot11APWorkMode_Type()
)
hh3cDot11APWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APWorkMode.setStatus("current")
_Hh3cDot11APTemplateRowStatus_Type = RowStatus
_Hh3cDot11APTemplateRowStatus_Object = MibTableColumn
hh3cDot11APTemplateRowStatus = _Hh3cDot11APTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 6),
    _Hh3cDot11APTemplateRowStatus_Type()
)
hh3cDot11APTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APTemplateRowStatus.setStatus("current")
_Hh3cDot11APName_Type = OctetString
_Hh3cDot11APName_Object = MibTableColumn
hh3cDot11APName = _Hh3cDot11APName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 7),
    _Hh3cDot11APName_Type()
)
hh3cDot11APName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APName.setStatus("current")
_Hh3cDot11StatisInterv_Type = Integer32
_Hh3cDot11StatisInterv_Object = MibTableColumn
hh3cDot11StatisInterv = _Hh3cDot11StatisInterv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 8),
    _Hh3cDot11StatisInterv_Type()
)
hh3cDot11StatisInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11StatisInterv.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StatisInterv.setUnits("second")


class _Hh3cDot11APBroadcastProbeReply_Type(TruthValue):
    """Custom type hh3cDot11APBroadcastProbeReply based on TruthValue"""


_Hh3cDot11APBroadcastProbeReply_Object = MibTableColumn
hh3cDot11APBroadcastProbeReply = _Hh3cDot11APBroadcastProbeReply_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 9),
    _Hh3cDot11APBroadcastProbeReply_Type()
)
hh3cDot11APBroadcastProbeReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APBroadcastProbeReply.setStatus("current")
_Hh3cDot11StaIdleTimerInterv_Type = Integer32
_Hh3cDot11StaIdleTimerInterv_Object = MibTableColumn
hh3cDot11StaIdleTimerInterv = _Hh3cDot11StaIdleTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 10),
    _Hh3cDot11StaIdleTimerInterv_Type()
)
hh3cDot11StaIdleTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11StaIdleTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StaIdleTimerInterv.setUnits("second")
_Hh3cDot11StaKeepAliveTimerInterv_Type = Integer32
_Hh3cDot11StaKeepAliveTimerInterv_Object = MibTableColumn
hh3cDot11StaKeepAliveTimerInterv = _Hh3cDot11StaKeepAliveTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 11),
    _Hh3cDot11StaKeepAliveTimerInterv_Type()
)
hh3cDot11StaKeepAliveTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11StaKeepAliveTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StaKeepAliveTimerInterv.setUnits("second")
_Hh3cDot11APCir_Type = Integer32
_Hh3cDot11APCir_Object = MibTableColumn
hh3cDot11APCir = _Hh3cDot11APCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 12),
    _Hh3cDot11APCir_Type()
)
hh3cDot11APCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APCir.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCir.setUnits("Kbps")
_Hh3cDot11APCbs_Type = Integer32
_Hh3cDot11APCbs_Object = MibTableColumn
hh3cDot11APCbs = _Hh3cDot11APCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 13),
    _Hh3cDot11APCbs_Type()
)
hh3cDot11APCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APCbs.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCbs.setUnits("Bytes")


class _Hh3cDot11APPriorityLevel_Type(Integer32):
    """Custom type hh3cDot11APPriorityLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cDot11APPriorityLevel_Type.__name__ = "Integer32"
_Hh3cDot11APPriorityLevel_Object = MibTableColumn
hh3cDot11APPriorityLevel = _Hh3cDot11APPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 14),
    _Hh3cDot11APPriorityLevel_Type()
)
hh3cDot11APPriorityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APPriorityLevel.setStatus("current")
_Hh3cDot11APElementID_Type = Integer32
_Hh3cDot11APElementID_Object = MibTableColumn
hh3cDot11APElementID = _Hh3cDot11APElementID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 15),
    _Hh3cDot11APElementID_Type()
)
hh3cDot11APElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APElementID.setStatus("current")


class _Hh3cDot11APDevDetectEnable_Type(TruthValue):
    """Custom type hh3cDot11APDevDetectEnable based on TruthValue"""


_Hh3cDot11APDevDetectEnable_Object = MibTableColumn
hh3cDot11APDevDetectEnable = _Hh3cDot11APDevDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 16),
    _Hh3cDot11APDevDetectEnable_Type()
)
hh3cDot11APDevDetectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APDevDetectEnable.setStatus("current")


class _Hh3cDot11APGetIPMethod_Type(Integer32):
    """Custom type hh3cDot11APGetIPMethod based on Integer32"""
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


_Hh3cDot11APGetIPMethod_Type.__name__ = "Integer32"
_Hh3cDot11APGetIPMethod_Object = MibTableColumn
hh3cDot11APGetIPMethod = _Hh3cDot11APGetIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 17),
    _Hh3cDot11APGetIPMethod_Type()
)
hh3cDot11APGetIPMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APGetIPMethod.setStatus("current")


class _Hh3cDot11StatisIntervMode_Type(Integer32):
    """Custom type hh3cDot11StatisIntervMode based on Integer32"""
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


_Hh3cDot11StatisIntervMode_Type.__name__ = "Integer32"
_Hh3cDot11StatisIntervMode_Object = MibTableColumn
hh3cDot11StatisIntervMode = _Hh3cDot11StatisIntervMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 18),
    _Hh3cDot11StatisIntervMode_Type()
)
hh3cDot11StatisIntervMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11StatisIntervMode.setStatus("current")
_Hh3cDot11RadioToConfigTable_Object = MibTable
hh3cDot11RadioToConfigTable = _Hh3cDot11RadioToConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioToConfigTable.setStatus("current")
_Hh3cDot11RadioToConfigEntry_Object = MibTableRow
hh3cDot11RadioToConfigEntry = _Hh3cDot11RadioToConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1)
)
hh3cDot11RadioToConfigEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APTemplateNameCfg"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11CfgRadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioToConfigEntry.setStatus("current")


class _Hh3cDot11APTemplateNameCfg_Type(OctetString):
    """Custom type hh3cDot11APTemplateNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11APTemplateNameCfg_Type.__name__ = "OctetString"
_Hh3cDot11APTemplateNameCfg_Object = MibTableColumn
hh3cDot11APTemplateNameCfg = _Hh3cDot11APTemplateNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 1),
    _Hh3cDot11APTemplateNameCfg_Type()
)
hh3cDot11APTemplateNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APTemplateNameCfg.setStatus("current")
_Hh3cDot11CfgRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11CfgRadioID_Object = MibTableColumn
hh3cDot11CfgRadioID = _Hh3cDot11CfgRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 2),
    _Hh3cDot11CfgRadioID_Type()
)
hh3cDot11CfgRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11CfgRadioID.setStatus("current")
_Hh3cDot11CfgRadioPolicyName_Type = OctetString
_Hh3cDot11CfgRadioPolicyName_Object = MibTableColumn
hh3cDot11CfgRadioPolicyName = _Hh3cDot11CfgRadioPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 3),
    _Hh3cDot11CfgRadioPolicyName_Type()
)
hh3cDot11CfgRadioPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgRadioPolicyName.setStatus("current")
_Hh3cDot11CfgRadioType_Type = Hh3cDot11RadioType
_Hh3cDot11CfgRadioType_Object = MibTableColumn
hh3cDot11CfgRadioType = _Hh3cDot11CfgRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 4),
    _Hh3cDot11CfgRadioType_Type()
)
hh3cDot11CfgRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgRadioType.setStatus("current")
_Hh3cDot11CfgChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11CfgChannel_Object = MibTableColumn
hh3cDot11CfgChannel = _Hh3cDot11CfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 5),
    _Hh3cDot11CfgChannel_Type()
)
hh3cDot11CfgChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgChannel.setStatus("current")
_Hh3cDot11CfgMaxTxPowerLevel_Type = Hh3cDot11TxPwrLevelScopeType
_Hh3cDot11CfgMaxTxPowerLevel_Object = MibTableColumn
hh3cDot11CfgMaxTxPowerLevel = _Hh3cDot11CfgMaxTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 6),
    _Hh3cDot11CfgMaxTxPowerLevel_Type()
)
hh3cDot11CfgMaxTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgMaxTxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11CfgMaxTxPowerLevel.setUnits("dbm")


class _Hh3cDot11PreambleLen_Type(Hh3cDot11PreambleType):
    """Custom type hh3cDot11PreambleLen based on Hh3cDot11PreambleType"""


_Hh3cDot11PreambleLen_Object = MibTableColumn
hh3cDot11PreambleLen = _Hh3cDot11PreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 7),
    _Hh3cDot11PreambleLen_Type()
)
hh3cDot11PreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11PreambleLen.setStatus("current")
_Hh3cDot11CfgRadioStatus_Type = TruthValue
_Hh3cDot11CfgRadioStatus_Object = MibTableColumn
hh3cDot11CfgRadioStatus = _Hh3cDot11CfgRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 8),
    _Hh3cDot11CfgRadioStatus_Type()
)
hh3cDot11CfgRadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgRadioStatus.setStatus("current")
_Hh3cDot11CfgRdElementID_Type = Unsigned32
_Hh3cDot11CfgRdElementID_Object = MibTableColumn
hh3cDot11CfgRdElementID = _Hh3cDot11CfgRdElementID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 9),
    _Hh3cDot11CfgRdElementID_Type()
)
hh3cDot11CfgRdElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CfgRdElementID.setStatus("current")
_Hh3cDot11CfgWorkMode_Type = Hh3cDot11WorkMode
_Hh3cDot11CfgWorkMode_Object = MibTableColumn
hh3cDot11CfgWorkMode = _Hh3cDot11CfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 10),
    _Hh3cDot11CfgWorkMode_Type()
)
hh3cDot11CfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgWorkMode.setStatus("current")
_Hh3cDot11CfgPwrAttValue_Type = Integer32
_Hh3cDot11CfgPwrAttValue_Object = MibTableColumn
hh3cDot11CfgPwrAttValue = _Hh3cDot11CfgPwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 11),
    _Hh3cDot11CfgPwrAttValue_Type()
)
hh3cDot11CfgPwrAttValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgPwrAttValue.setStatus("current")


class _Hh3cDot11RadioTxArithmetic_Type(Integer32):
    """Custom type hh3cDot11RadioTxArithmetic based on Integer32"""
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


_Hh3cDot11RadioTxArithmetic_Type.__name__ = "Integer32"
_Hh3cDot11RadioTxArithmetic_Object = MibTableColumn
hh3cDot11RadioTxArithmetic = _Hh3cDot11RadioTxArithmetic_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 12),
    _Hh3cDot11RadioTxArithmetic_Type()
)
hh3cDot11RadioTxArithmetic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioTxArithmetic.setStatus("current")


class _Hh3cDot11CfgChannelLockStat_Type(Integer32):
    """Custom type hh3cDot11CfgChannelLockStat based on Integer32"""
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


_Hh3cDot11CfgChannelLockStat_Type.__name__ = "Integer32"
_Hh3cDot11CfgChannelLockStat_Object = MibTableColumn
hh3cDot11CfgChannelLockStat = _Hh3cDot11CfgChannelLockStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 13),
    _Hh3cDot11CfgChannelLockStat_Type()
)
hh3cDot11CfgChannelLockStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgChannelLockStat.setStatus("current")


class _Hh3cDot11CfgPowerLockStat_Type(Integer32):
    """Custom type hh3cDot11CfgPowerLockStat based on Integer32"""
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


_Hh3cDot11CfgPowerLockStat_Type.__name__ = "Integer32"
_Hh3cDot11CfgPowerLockStat_Object = MibTableColumn
hh3cDot11CfgPowerLockStat = _Hh3cDot11CfgPowerLockStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 14),
    _Hh3cDot11CfgPowerLockStat_Type()
)
hh3cDot11CfgPowerLockStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgPowerLockStat.setStatus("current")
_Hh3cDot11CfgLBRdGroupId_Type = Unsigned32
_Hh3cDot11CfgLBRdGroupId_Object = MibTableColumn
hh3cDot11CfgLBRdGroupId = _Hh3cDot11CfgLBRdGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 15),
    _Hh3cDot11CfgLBRdGroupId_Type()
)
hh3cDot11CfgLBRdGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgLBRdGroupId.setStatus("current")
_Hh3cDot11CfgRRMSDRdGroupId_Type = Unsigned32
_Hh3cDot11CfgRRMSDRdGroupId_Object = MibTableColumn
hh3cDot11CfgRRMSDRdGroupId = _Hh3cDot11CfgRRMSDRdGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 16),
    _Hh3cDot11CfgRRMSDRdGroupId_Type()
)
hh3cDot11CfgRRMSDRdGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgRRMSDRdGroupId.setStatus("current")
_Hh3cDot11APServiceSetTable_Object = MibTable
hh3cDot11APServiceSetTable = _Hh3cDot11APServiceSetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11APServiceSetTable.setStatus("current")
_Hh3cDot11APServiceSetEntry_Object = MibTableRow
hh3cDot11APServiceSetEntry = _Hh3cDot11APServiceSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 3, 1)
)
hh3cDot11APServiceSetEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APTemplateNameCfg"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11CfgRadioID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11CfgServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APServiceSetEntry.setStatus("current")
_Hh3cDot11CfgServicePolicyID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11CfgServicePolicyID_Object = MibTableColumn
hh3cDot11CfgServicePolicyID = _Hh3cDot11CfgServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 3, 1, 1),
    _Hh3cDot11CfgServicePolicyID_Type()
)
hh3cDot11CfgServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11CfgServicePolicyID.setStatus("current")
_Hh3cDot11SrvSetRowStatus_Type = RowStatus
_Hh3cDot11SrvSetRowStatus_Object = MibTableColumn
hh3cDot11SrvSetRowStatus = _Hh3cDot11SrvSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 3, 1, 2),
    _Hh3cDot11SrvSetRowStatus_Type()
)
hh3cDot11SrvSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SrvSetRowStatus.setStatus("current")


class _Hh3cDot11ServiceSetVlanId_Type(Integer32):
    """Custom type hh3cDot11ServiceSetVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cDot11ServiceSetVlanId_Type.__name__ = "Integer32"
_Hh3cDot11ServiceSetVlanId_Object = MibTableColumn
hh3cDot11ServiceSetVlanId = _Hh3cDot11ServiceSetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 3, 1, 3),
    _Hh3cDot11ServiceSetVlanId_Type()
)
hh3cDot11ServiceSetVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11ServiceSetVlanId.setStatus("current")
_Hh3cDot11APSysInfoSetTable_Object = MibTable
hh3cDot11APSysInfoSetTable = _Hh3cDot11APSysInfoSetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11APSysInfoSetTable.setStatus("current")
_Hh3cDot11APSysInfoSetEntry_Object = MibTableRow
hh3cDot11APSysInfoSetEntry = _Hh3cDot11APSysInfoSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 4, 1)
)
hh3cDot11APSysInfoSetEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11SIDAPSerialID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APSysInfoSetEntry.setStatus("current")


class _Hh3cDot11APSysNetID_Type(OctetString):
    """Custom type hh3cDot11APSysNetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11APSysNetID_Type.__name__ = "OctetString"
_Hh3cDot11APSysNetID_Object = MibTableColumn
hh3cDot11APSysNetID = _Hh3cDot11APSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 4, 1, 1),
    _Hh3cDot11APSysNetID_Type()
)
hh3cDot11APSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APSysNetID.setStatus("current")


class _Hh3cDot11APCpuUsageThreshold_Type(Integer32):
    """Custom type hh3cDot11APCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APCpuUsageThreshold_Type.__name__ = "Integer32"
_Hh3cDot11APCpuUsageThreshold_Object = MibTableColumn
hh3cDot11APCpuUsageThreshold = _Hh3cDot11APCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 4, 1, 2),
    _Hh3cDot11APCpuUsageThreshold_Type()
)
hh3cDot11APCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCpuUsageThreshold.setUnits("onepercent")


class _Hh3cDot11APMemUsageThreshold_Type(Integer32):
    """Custom type hh3cDot11APMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APMemUsageThreshold_Type.__name__ = "Integer32"
_Hh3cDot11APMemUsageThreshold_Object = MibTableColumn
hh3cDot11APMemUsageThreshold = _Hh3cDot11APMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 4, 1, 3),
    _Hh3cDot11APMemUsageThreshold_Type()
)
hh3cDot11APMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APMemUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APMemUsageThreshold.setUnits("onepercent")
_Hh3cDot11APLimitTable_Object = MibTable
hh3cDot11APLimitTable = _Hh3cDot11APLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11APLimitTable.setStatus("current")
_Hh3cDot11APLimitEntry_Object = MibTableRow
hh3cDot11APLimitEntry = _Hh3cDot11APLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 5, 1)
)
hh3cDot11APLimitEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11APLimitEntry.setStatus("current")


class _Hh3cDot11APSsidNumLimit_Type(Integer32):
    """Custom type hh3cDot11APSsidNumLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11APSsidNumLimit_Type.__name__ = "Integer32"
_Hh3cDot11APSsidNumLimit_Object = MibTableColumn
hh3cDot11APSsidNumLimit = _Hh3cDot11APSsidNumLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 5, 1, 1),
    _Hh3cDot11APSsidNumLimit_Type()
)
hh3cDot11APSsidNumLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APSsidNumLimit.setStatus("current")


class _Hh3cDot11APUserCntLimit_Type(Integer32):
    """Custom type hh3cDot11APUserCntLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11APUserCntLimit_Type.__name__ = "Integer32"
_Hh3cDot11APUserCntLimit_Object = MibTableColumn
hh3cDot11APUserCntLimit = _Hh3cDot11APUserCntLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 5, 1, 2),
    _Hh3cDot11APUserCntLimit_Type()
)
hh3cDot11APUserCntLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APUserCntLimit.setStatus("current")


class _Hh3cDot11APUserThreshold_Type(Integer32):
    """Custom type hh3cDot11APUserThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11APUserThreshold_Type.__name__ = "Integer32"
_Hh3cDot11APUserThreshold_Object = MibTableColumn
hh3cDot11APUserThreshold = _Hh3cDot11APUserThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 5, 1, 3),
    _Hh3cDot11APUserThreshold_Type()
)
hh3cDot11APUserThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APUserThreshold.setStatus("current")
_Hh3cDot11APIfSetTable_Object = MibTable
hh3cDot11APIfSetTable = _Hh3cDot11APIfSetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11APIfSetTable.setStatus("current")
_Hh3cDot11APIfSetEntry_Object = MibTableRow
hh3cDot11APIfSetEntry = _Hh3cDot11APIfSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 6, 1)
)
hh3cDot11APIfSetEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APSetIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11APIfSetEntry.setStatus("current")
_Hh3cDot11APSetIfIndex_Type = Integer32
_Hh3cDot11APSetIfIndex_Object = MibTableColumn
hh3cDot11APSetIfIndex = _Hh3cDot11APSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 6, 1, 1),
    _Hh3cDot11APSetIfIndex_Type()
)
hh3cDot11APSetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APSetIfIndex.setStatus("current")
_Hh3cDot11APIfAlias_Type = DisplayString
_Hh3cDot11APIfAlias_Object = MibTableColumn
hh3cDot11APIfAlias = _Hh3cDot11APIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 6, 1, 2),
    _Hh3cDot11APIfAlias_Type()
)
hh3cDot11APIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APIfAlias.setStatus("current")
_Hh3cDot11APServiceVlanTable_Object = MibTable
hh3cDot11APServiceVlanTable = _Hh3cDot11APServiceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7)
)
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanTable.setStatus("current")
_Hh3cDot11APServiceVlanEntry_Object = MibTableRow
hh3cDot11APServiceVlanEntry = _Hh3cDot11APServiceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7, 1)
)
hh3cDot11APServiceVlanEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APServiceVlanSerialID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APServiceVlanSPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanEntry.setStatus("current")
_Hh3cDot11APServiceVlanSerialID_Type = OctetString
_Hh3cDot11APServiceVlanSerialID_Object = MibTableColumn
hh3cDot11APServiceVlanSerialID = _Hh3cDot11APServiceVlanSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7, 1, 1),
    _Hh3cDot11APServiceVlanSerialID_Type()
)
hh3cDot11APServiceVlanSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanSerialID.setStatus("current")
_Hh3cDot11APServiceVlanSPID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11APServiceVlanSPID_Object = MibTableColumn
hh3cDot11APServiceVlanSPID = _Hh3cDot11APServiceVlanSPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7, 1, 2),
    _Hh3cDot11APServiceVlanSPID_Type()
)
hh3cDot11APServiceVlanSPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanSPID.setStatus("current")


class _Hh3cDot11APServiceVlanId_Type(Integer32):
    """Custom type hh3cDot11APServiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cDot11APServiceVlanId_Type.__name__ = "Integer32"
_Hh3cDot11APServiceVlanId_Object = MibTableColumn
hh3cDot11APServiceVlanId = _Hh3cDot11APServiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7, 1, 3),
    _Hh3cDot11APServiceVlanId_Type()
)
hh3cDot11APServiceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanId.setStatus("current")
_Hh3cDot11APServiceVlanRowStatus_Type = RowStatus
_Hh3cDot11APServiceVlanRowStatus_Object = MibTableColumn
hh3cDot11APServiceVlanRowStatus = _Hh3cDot11APServiceVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7, 1, 4),
    _Hh3cDot11APServiceVlanRowStatus_Type()
)
hh3cDot11APServiceVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanRowStatus.setStatus("current")
_Hh3cDot11RadioConfigTable_Object = MibTable
hh3cDot11RadioConfigTable = _Hh3cDot11RadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioConfigTable.setStatus("current")
_Hh3cDot11RadioConfigEntry_Object = MibTableRow
hh3cDot11RadioConfigEntry = _Hh3cDot11RadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1)
)
hh3cDot11RadioConfigEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RCAPSerialID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RCRadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioConfigEntry.setStatus("current")


class _Hh3cDot11RCAPSerialID_Type(OctetString):
    """Custom type hh3cDot11RCAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11RCAPSerialID_Type.__name__ = "OctetString"
_Hh3cDot11RCAPSerialID_Object = MibTableColumn
hh3cDot11RCAPSerialID = _Hh3cDot11RCAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 1),
    _Hh3cDot11RCAPSerialID_Type()
)
hh3cDot11RCAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RCAPSerialID.setStatus("current")
_Hh3cDot11RCRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11RCRadioID_Object = MibTableColumn
hh3cDot11RCRadioID = _Hh3cDot11RCRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 2),
    _Hh3cDot11RCRadioID_Type()
)
hh3cDot11RCRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RCRadioID.setStatus("current")
_Hh3cDot11RCRadioType_Type = Hh3cDot11RadioType
_Hh3cDot11RCRadioType_Object = MibTableColumn
hh3cDot11RCRadioType = _Hh3cDot11RCRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 3),
    _Hh3cDot11RCRadioType_Type()
)
hh3cDot11RCRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCRadioType.setStatus("current")
_Hh3cDot11RCChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11RCChannel_Object = MibTableColumn
hh3cDot11RCChannel = _Hh3cDot11RCChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 4),
    _Hh3cDot11RCChannel_Type()
)
hh3cDot11RCChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCChannel.setStatus("current")


class _Hh3cDot11RCPreambleLen_Type(Hh3cDot11PreambleType):
    """Custom type hh3cDot11RCPreambleLen based on Hh3cDot11PreambleType"""


_Hh3cDot11RCPreambleLen_Object = MibTableColumn
hh3cDot11RCPreambleLen = _Hh3cDot11RCPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 5),
    _Hh3cDot11RCPreambleLen_Type()
)
hh3cDot11RCPreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCPreambleLen.setStatus("current")
_Hh3cDot11RCPwrAttValue_Type = Integer32
_Hh3cDot11RCPwrAttValue_Object = MibTableColumn
hh3cDot11RCPwrAttValue = _Hh3cDot11RCPwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 6),
    _Hh3cDot11RCPwrAttValue_Type()
)
hh3cDot11RCPwrAttValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCPwrAttValue.setStatus("current")
_Hh3cDot11RCApPowerLevel_Type = Hh3cDot11TxPwrLevelScopeType
_Hh3cDot11RCApPowerLevel_Object = MibTableColumn
hh3cDot11RCApPowerLevel = _Hh3cDot11RCApPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 7),
    _Hh3cDot11RCApPowerLevel_Type()
)
hh3cDot11RCApPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCApPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RCApPowerLevel.setUnits("dbm")
_Hh3cDot11RCDynamicChlState_Type = TruthValue
_Hh3cDot11RCDynamicChlState_Object = MibTableColumn
hh3cDot11RCDynamicChlState = _Hh3cDot11RCDynamicChlState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 8),
    _Hh3cDot11RCDynamicChlState_Type()
)
hh3cDot11RCDynamicChlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCDynamicChlState.setStatus("current")
_Hh3cDot11RCDynamicPowerState_Type = TruthValue
_Hh3cDot11RCDynamicPowerState_Object = MibTableColumn
hh3cDot11RCDynamicPowerState = _Hh3cDot11RCDynamicPowerState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 9),
    _Hh3cDot11RCDynamicPowerState_Type()
)
hh3cDot11RCDynamicPowerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCDynamicPowerState.setStatus("current")
_Hh3cDot11RCRadioStatus_Type = TruthValue
_Hh3cDot11RCRadioStatus_Object = MibTableColumn
hh3cDot11RCRadioStatus = _Hh3cDot11RCRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 10),
    _Hh3cDot11RCRadioStatus_Type()
)
hh3cDot11RCRadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCRadioStatus.setStatus("current")
_Hh3cDot11RadioSSIDCfgTable_Object = MibTable
hh3cDot11RadioSSIDCfgTable = _Hh3cDot11RadioSSIDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDCfgTable.setStatus("current")
_Hh3cDot11RadioSSIDCfgEntry_Object = MibTableRow
hh3cDot11RadioSSIDCfgEntry = _Hh3cDot11RadioSSIDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1)
)
hh3cDot11RadioSSIDCfgEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioSSIDSerialID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioSSIDRadioID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioSSIDWLANID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDCfgEntry.setStatus("current")
_Hh3cDot11RadioSSIDSerialID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11RadioSSIDSerialID_Object = MibTableColumn
hh3cDot11RadioSSIDSerialID = _Hh3cDot11RadioSSIDSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 1),
    _Hh3cDot11RadioSSIDSerialID_Type()
)
hh3cDot11RadioSSIDSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDSerialID.setStatus("current")
_Hh3cDot11RadioSSIDRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11RadioSSIDRadioID_Object = MibTableColumn
hh3cDot11RadioSSIDRadioID = _Hh3cDot11RadioSSIDRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 2),
    _Hh3cDot11RadioSSIDRadioID_Type()
)
hh3cDot11RadioSSIDRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDRadioID.setStatus("current")
_Hh3cDot11RadioSSIDWLANID_Type = Integer32
_Hh3cDot11RadioSSIDWLANID_Object = MibTableColumn
hh3cDot11RadioSSIDWLANID = _Hh3cDot11RadioSSIDWLANID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 3),
    _Hh3cDot11RadioSSIDWLANID_Type()
)
hh3cDot11RadioSSIDWLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDWLANID.setStatus("current")
_Hh3cDot11RadioSSIDIndex_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11RadioSSIDIndex_Object = MibTableColumn
hh3cDot11RadioSSIDIndex = _Hh3cDot11RadioSSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 4),
    _Hh3cDot11RadioSSIDIndex_Type()
)
hh3cDot11RadioSSIDIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDIndex.setStatus("current")
_Hh3cDot11RadioBSSID_Type = MacAddress
_Hh3cDot11RadioBSSID_Object = MibTableColumn
hh3cDot11RadioBSSID = _Hh3cDot11RadioBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 5),
    _Hh3cDot11RadioBSSID_Type()
)
hh3cDot11RadioBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioBSSID.setStatus("current")
_Hh3cDot11RadioSSIDRowStatus_Type = RowStatus
_Hh3cDot11RadioSSIDRowStatus_Object = MibTableColumn
hh3cDot11RadioSSIDRowStatus = _Hh3cDot11RadioSSIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 6),
    _Hh3cDot11RadioSSIDRowStatus_Type()
)
hh3cDot11RadioSSIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDRowStatus.setStatus("current")
_Hh3cDot11APSerialIDTable_Object = MibTable
hh3cDot11APSerialIDTable = _Hh3cDot11APSerialIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10)
)
if mibBuilder.loadTexts:
    hh3cDot11APSerialIDTable.setStatus("current")
_Hh3cDot11APSerialIDEntry_Object = MibTableRow
hh3cDot11APSerialIDEntry = _Hh3cDot11APSerialIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1)
)
hh3cDot11APSerialIDEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11SIDAPSerialID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APSerialIDEntry.setStatus("current")
_Hh3cDot11SIDAPSerialID_Type = OctetString
_Hh3cDot11SIDAPSerialID_Object = MibTableColumn
hh3cDot11SIDAPSerialID = _Hh3cDot11SIDAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 1),
    _Hh3cDot11SIDAPSerialID_Type()
)
hh3cDot11SIDAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPSerialID.setStatus("current")


class _Hh3cDot11SIDAPWorkMode_Type(Integer32):
    """Custom type hh3cDot11SIDAPWorkMode based on Integer32"""
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


_Hh3cDot11SIDAPWorkMode_Type.__name__ = "Integer32"
_Hh3cDot11SIDAPWorkMode_Object = MibTableColumn
hh3cDot11SIDAPWorkMode = _Hh3cDot11SIDAPWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 2),
    _Hh3cDot11SIDAPWorkMode_Type()
)
hh3cDot11SIDAPWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPWorkMode.setStatus("current")


class _Hh3cDot11SIDAPGetIPMethod_Type(Integer32):
    """Custom type hh3cDot11SIDAPGetIPMethod based on Integer32"""
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


_Hh3cDot11SIDAPGetIPMethod_Type.__name__ = "Integer32"
_Hh3cDot11SIDAPGetIPMethod_Object = MibTableColumn
hh3cDot11SIDAPGetIPMethod = _Hh3cDot11SIDAPGetIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 3),
    _Hh3cDot11SIDAPGetIPMethod_Type()
)
hh3cDot11SIDAPGetIPMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPGetIPMethod.setStatus("current")
_Hh3cDot11APSTVlanTable_Object = MibTable
hh3cDot11APSTVlanTable = _Hh3cDot11APSTVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 11)
)
if mibBuilder.loadTexts:
    hh3cDot11APSTVlanTable.setStatus("current")
_Hh3cDot11APSTVlanEntry_Object = MibTableRow
hh3cDot11APSTVlanEntry = _Hh3cDot11APSTVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 11, 1)
)
hh3cDot11APSTVlanEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11SIDAPSerialID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11CfgRadioID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11CfgServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APSTVlanEntry.setStatus("current")


class _Hh3cDot11CfgSTVLANID_Type(Integer32):
    """Custom type hh3cDot11CfgSTVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cDot11CfgSTVLANID_Type.__name__ = "Integer32"
_Hh3cDot11CfgSTVLANID_Object = MibTableColumn
hh3cDot11CfgSTVLANID = _Hh3cDot11CfgSTVLANID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 11, 1, 1),
    _Hh3cDot11CfgSTVLANID_Type()
)
hh3cDot11CfgSTVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CfgSTVLANID.setStatus("current")


class _Hh3cDot11CfgSTNASPortID_Type(Integer32):
    """Custom type hh3cDot11CfgSTNASPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cDot11CfgSTNASPortID_Type.__name__ = "Integer32"
_Hh3cDot11CfgSTNASPortID_Object = MibTableColumn
hh3cDot11CfgSTNASPortID = _Hh3cDot11CfgSTNASPortID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 11, 1, 2),
    _Hh3cDot11CfgSTNASPortID_Type()
)
hh3cDot11CfgSTNASPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CfgSTNASPortID.setStatus("current")
_Hh3cDot11CfgServiceSetRowStatus_Type = RowStatus
_Hh3cDot11CfgServiceSetRowStatus_Object = MibTableColumn
hh3cDot11CfgServiceSetRowStatus = _Hh3cDot11CfgServiceSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 11, 1, 3),
    _Hh3cDot11CfgServiceSetRowStatus_Type()
)
hh3cDot11CfgServiceSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CfgServiceSetRowStatus.setStatus("current")
_Hh3cDot11RadioIntfConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RadioIntfConfigGroup = _Hh3cDot11RadioIntfConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4)
)
_Hh3cDot11RadioIntfConfigTable_Object = MibTable
hh3cDot11RadioIntfConfigTable = _Hh3cDot11RadioIntfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfConfigTable.setStatus("current")
_Hh3cDot11RadioIntfConfigEntry_Object = MibTableRow
hh3cDot11RadioIntfConfigEntry = _Hh3cDot11RadioIntfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1)
)
hh3cDot11RadioIntfConfigEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioIfIdx"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfConfigEntry.setStatus("current")
_Hh3cDot11RadioIfIdx_Type = Integer32
_Hh3cDot11RadioIfIdx_Object = MibTableColumn
hh3cDot11RadioIfIdx = _Hh3cDot11RadioIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 1),
    _Hh3cDot11RadioIfIdx_Type()
)
hh3cDot11RadioIfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioIfIdx.setStatus("current")


class _Hh3cDot11RadioCfgBeaconIntvl_Type(Integer32):
    """Custom type hh3cDot11RadioCfgBeaconIntvl based on Integer32"""
    defaultValue = 100


_Hh3cDot11RadioCfgBeaconIntvl_Object = MibTableColumn
hh3cDot11RadioCfgBeaconIntvl = _Hh3cDot11RadioCfgBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 2),
    _Hh3cDot11RadioCfgBeaconIntvl_Type()
)
hh3cDot11RadioCfgBeaconIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgBeaconIntvl.setUnits("TU")


class _Hh3cDot11RadioCfgDtimIntvl_Type(Integer32):
    """Custom type hh3cDot11RadioCfgDtimIntvl based on Integer32"""
    defaultValue = 1


_Hh3cDot11RadioCfgDtimIntvl_Object = MibTableColumn
hh3cDot11RadioCfgDtimIntvl = _Hh3cDot11RadioCfgDtimIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 3),
    _Hh3cDot11RadioCfgDtimIntvl_Type()
)
hh3cDot11RadioCfgDtimIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgDtimIntvl.setStatus("current")


class _Hh3cDot11RadioCfgRtsThreshold_Type(Integer32):
    """Custom type hh3cDot11RadioCfgRtsThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11RadioCfgRtsThreshold_Object = MibTableColumn
hh3cDot11RadioCfgRtsThreshold = _Hh3cDot11RadioCfgRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 4),
    _Hh3cDot11RadioCfgRtsThreshold_Type()
)
hh3cDot11RadioCfgRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgRtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgRtsThreshold.setUnits("Byte")


class _Hh3cDot11RadioCfgFragThreshold_Type(Integer32):
    """Custom type hh3cDot11RadioCfgFragThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11RadioCfgFragThreshold_Object = MibTableColumn
hh3cDot11RadioCfgFragThreshold = _Hh3cDot11RadioCfgFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 5),
    _Hh3cDot11RadioCfgFragThreshold_Type()
)
hh3cDot11RadioCfgFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgFragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgFragThreshold.setUnits("Byte")


class _Hh3cDot11RadioCfgShtRetryThld_Type(Integer32):
    """Custom type hh3cDot11RadioCfgShtRetryThld based on Integer32"""
    defaultValue = 5


_Hh3cDot11RadioCfgShtRetryThld_Object = MibTableColumn
hh3cDot11RadioCfgShtRetryThld = _Hh3cDot11RadioCfgShtRetryThld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 6),
    _Hh3cDot11RadioCfgShtRetryThld_Type()
)
hh3cDot11RadioCfgShtRetryThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgShtRetryThld.setStatus("current")


class _Hh3cDot11RadioCfglongRtrThld_Type(Integer32):
    """Custom type hh3cDot11RadioCfglongRtrThld based on Integer32"""
    defaultValue = 5


_Hh3cDot11RadioCfglongRtrThld_Object = MibTableColumn
hh3cDot11RadioCfglongRtrThld = _Hh3cDot11RadioCfglongRtrThld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 7),
    _Hh3cDot11RadioCfglongRtrThld_Type()
)
hh3cDot11RadioCfglongRtrThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfglongRtrThld.setStatus("current")


class _Hh3cDot11RadioCfgMaxRxLifetime_Type(Unsigned32):
    """Custom type hh3cDot11RadioCfgMaxRxLifetime based on Unsigned32"""
    defaultValue = 2000


_Hh3cDot11RadioCfgMaxRxLifetime_Object = MibTableColumn
hh3cDot11RadioCfgMaxRxLifetime = _Hh3cDot11RadioCfgMaxRxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 8),
    _Hh3cDot11RadioCfgMaxRxLifetime_Type()
)
hh3cDot11RadioCfgMaxRxLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgMaxRxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgMaxRxLifetime.setUnits("millisecond")
_Hh3cDot11RadioCfgType_Type = Hh3cDot11RadioType
_Hh3cDot11RadioCfgType_Object = MibTableColumn
hh3cDot11RadioCfgType = _Hh3cDot11RadioCfgType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 9),
    _Hh3cDot11RadioCfgType_Type()
)
hh3cDot11RadioCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgType.setStatus("current")


class _Hh3cDot11RadioCfgChannel_Type(Hh3cDot11ChannelScopeType):
    """Custom type hh3cDot11RadioCfgChannel based on Hh3cDot11ChannelScopeType"""
    defaultValue = 1


_Hh3cDot11RadioCfgChannel_Object = MibTableColumn
hh3cDot11RadioCfgChannel = _Hh3cDot11RadioCfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 10),
    _Hh3cDot11RadioCfgChannel_Type()
)
hh3cDot11RadioCfgChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgChannel.setStatus("current")
_Hh3cDot11RadioCfgMaxTxPwrLvl_Type = Hh3cDot11TxPwrLevelScopeType
_Hh3cDot11RadioCfgMaxTxPwrLvl_Object = MibTableColumn
hh3cDot11RadioCfgMaxTxPwrLvl = _Hh3cDot11RadioCfgMaxTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 11),
    _Hh3cDot11RadioCfgMaxTxPwrLvl_Type()
)
hh3cDot11RadioCfgMaxTxPwrLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgMaxTxPwrLvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgMaxTxPwrLvl.setUnits("dbm")


class _Hh3cDot11RadioCfgPreambleLen_Type(Hh3cDot11PreambleType):
    """Custom type hh3cDot11RadioCfgPreambleLen based on Hh3cDot11PreambleType"""


_Hh3cDot11RadioCfgPreambleLen_Object = MibTableColumn
hh3cDot11RadioCfgPreambleLen = _Hh3cDot11RadioCfgPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 12),
    _Hh3cDot11RadioCfgPreambleLen_Type()
)
hh3cDot11RadioCfgPreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgPreambleLen.setStatus("current")
_Hh3cDot11RadioCfgWorkMode_Type = Hh3cDot11WorkMode
_Hh3cDot11RadioCfgWorkMode_Object = MibTableColumn
hh3cDot11RadioCfgWorkMode = _Hh3cDot11RadioCfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 13),
    _Hh3cDot11RadioCfgWorkMode_Type()
)
hh3cDot11RadioCfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgWorkMode.setStatus("current")


class _Hh3cDot11RadioCfgOnly11gEnable_Type(TruthValue):
    """Custom type hh3cDot11RadioCfgOnly11gEnable based on TruthValue"""


_Hh3cDot11RadioCfgOnly11gEnable_Object = MibTableColumn
hh3cDot11RadioCfgOnly11gEnable = _Hh3cDot11RadioCfgOnly11gEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 14),
    _Hh3cDot11RadioCfgOnly11gEnable_Type()
)
hh3cDot11RadioCfgOnly11gEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgOnly11gEnable.setStatus("current")
_Hh3cDot11RadioIntfBindTable_Object = MibTable
hh3cDot11RadioIntfBindTable = _Hh3cDot11RadioIntfBindTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfBindTable.setStatus("current")
_Hh3cDot11RadioIntfBindEntry_Object = MibTableRow
hh3cDot11RadioIntfBindEntry = _Hh3cDot11RadioIntfBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 2, 1)
)
hh3cDot11RadioIntfBindEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioIfIdx"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioIntfBindSvcPlcyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfBindEntry.setStatus("current")
_Hh3cDot11RadioIntfBindSvcPlcyID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11RadioIntfBindSvcPlcyID_Object = MibTableColumn
hh3cDot11RadioIntfBindSvcPlcyID = _Hh3cDot11RadioIntfBindSvcPlcyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 2, 1, 1),
    _Hh3cDot11RadioIntfBindSvcPlcyID_Type()
)
hh3cDot11RadioIntfBindSvcPlcyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfBindSvcPlcyID.setStatus("current")
_Hh3cDot11RadioIntfBindIfIdx_Type = Unsigned32
_Hh3cDot11RadioIntfBindIfIdx_Object = MibTableColumn
hh3cDot11RadioIntfBindIfIdx = _Hh3cDot11RadioIntfBindIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 2, 1, 2),
    _Hh3cDot11RadioIntfBindIfIdx_Type()
)
hh3cDot11RadioIntfBindIfIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfBindIfIdx.setStatus("current")
_Hh3cDot11RadioIntfBindRowStatus_Type = RowStatus
_Hh3cDot11RadioIntfBindRowStatus_Object = MibTableColumn
hh3cDot11RadioIntfBindRowStatus = _Hh3cDot11RadioIntfBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 2, 1, 3),
    _Hh3cDot11RadioIntfBindRowStatus_Type()
)
hh3cDot11RadioIntfBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfBindRowStatus.setStatus("current")
_Hh3cDot11DataRateConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11DataRateConfigGroup = _Hh3cDot11DataRateConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5)
)
_Hh3cDot11DataRateConfigTable_Object = MibTable
hh3cDot11DataRateConfigTable = _Hh3cDot11DataRateConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11DataRateConfigTable.setStatus("current")
_Hh3cDot11DataRateConfigEntry_Object = MibTableRow
hh3cDot11DataRateConfigEntry = _Hh3cDot11DataRateConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1)
)
hh3cDot11DataRateConfigEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioTypeID"),
)
if mibBuilder.loadTexts:
    hh3cDot11DataRateConfigEntry.setStatus("current")
_Hh3cDot11RadioTypeID_Type = Hh3cDot11RadioType
_Hh3cDot11RadioTypeID_Object = MibTableColumn
hh3cDot11RadioTypeID = _Hh3cDot11RadioTypeID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1, 1),
    _Hh3cDot11RadioTypeID_Type()
)
hh3cDot11RadioTypeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioTypeID.setStatus("current")


class _Hh3cDot11SupportedRateSet_Type(OctetString):
    """Custom type hh3cDot11SupportedRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11SupportedRateSet_Type.__name__ = "OctetString"
_Hh3cDot11SupportedRateSet_Object = MibTableColumn
hh3cDot11SupportedRateSet = _Hh3cDot11SupportedRateSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1, 2),
    _Hh3cDot11SupportedRateSet_Type()
)
hh3cDot11SupportedRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SupportedRateSet.setStatus("current")


class _Hh3cDot11MandatoryRateSet_Type(OctetString):
    """Custom type hh3cDot11MandatoryRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11MandatoryRateSet_Type.__name__ = "OctetString"
_Hh3cDot11MandatoryRateSet_Object = MibTableColumn
hh3cDot11MandatoryRateSet = _Hh3cDot11MandatoryRateSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1, 3),
    _Hh3cDot11MandatoryRateSet_Type()
)
hh3cDot11MandatoryRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11MandatoryRateSet.setStatus("current")


class _Hh3cDot11DisabledRateSet_Type(OctetString):
    """Custom type hh3cDot11DisabledRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11DisabledRateSet_Type.__name__ = "OctetString"
_Hh3cDot11DisabledRateSet_Object = MibTableColumn
hh3cDot11DisabledRateSet = _Hh3cDot11DisabledRateSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1, 4),
    _Hh3cDot11DisabledRateSet_Type()
)
hh3cDot11DisabledRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11DisabledRateSet.setStatus("current")


class _Hh3cDot11SmartRateSet_Type(OctetString):
    """Custom type hh3cDot11SmartRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11SmartRateSet_Type.__name__ = "OctetString"
_Hh3cDot11SmartRateSet_Object = MibTableColumn
hh3cDot11SmartRateSet = _Hh3cDot11SmartRateSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1, 5),
    _Hh3cDot11SmartRateSet_Type()
)
hh3cDot11SmartRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SmartRateSet.setStatus("current")
_Hh3cDot11InterfaceConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11InterfaceConfigGroup = _Hh3cDot11InterfaceConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6)
)
_Hh3cDot11WlanEssIfTable_Object = MibTable
hh3cDot11WlanEssIfTable = _Hh3cDot11WlanEssIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11WlanEssIfTable.setStatus("current")
_Hh3cDot11WlanEssIfEntry_Object = MibTableRow
hh3cDot11WlanEssIfEntry = _Hh3cDot11WlanEssIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 1, 1)
)
hh3cDot11WlanEssIfEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11WlanEssIfNumber"),
)
if mibBuilder.loadTexts:
    hh3cDot11WlanEssIfEntry.setStatus("current")
_Hh3cDot11WlanEssIfNumber_Type = Integer32
_Hh3cDot11WlanEssIfNumber_Object = MibTableColumn
hh3cDot11WlanEssIfNumber = _Hh3cDot11WlanEssIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 1, 1, 1),
    _Hh3cDot11WlanEssIfNumber_Type()
)
hh3cDot11WlanEssIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WlanEssIfNumber.setStatus("current")
_Hh3cDot11WlanEssIfIndex_Type = Integer32
_Hh3cDot11WlanEssIfIndex_Object = MibTableColumn
hh3cDot11WlanEssIfIndex = _Hh3cDot11WlanEssIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 1, 1, 2),
    _Hh3cDot11WlanEssIfIndex_Type()
)
hh3cDot11WlanEssIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WlanEssIfIndex.setStatus("current")
_Hh3cDot11WlanEssRowStatus_Type = RowStatus
_Hh3cDot11WlanEssRowStatus_Object = MibTableColumn
hh3cDot11WlanEssRowStatus = _Hh3cDot11WlanEssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 1, 1, 3),
    _Hh3cDot11WlanEssRowStatus_Type()
)
hh3cDot11WlanEssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanEssRowStatus.setStatus("current")
_Hh3cDot11WlanBssIfTable_Object = MibTable
hh3cDot11WlanBssIfTable = _Hh3cDot11WlanBssIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11WlanBssIfTable.setStatus("current")
_Hh3cDot11WlanBssIfEntry_Object = MibTableRow
hh3cDot11WlanBssIfEntry = _Hh3cDot11WlanBssIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 2, 1)
)
hh3cDot11WlanBssIfEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11WlanBssIfNumber"),
)
if mibBuilder.loadTexts:
    hh3cDot11WlanBssIfEntry.setStatus("current")
_Hh3cDot11WlanBssIfNumber_Type = Integer32
_Hh3cDot11WlanBssIfNumber_Object = MibTableColumn
hh3cDot11WlanBssIfNumber = _Hh3cDot11WlanBssIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 2, 1, 1),
    _Hh3cDot11WlanBssIfNumber_Type()
)
hh3cDot11WlanBssIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WlanBssIfNumber.setStatus("current")
_Hh3cDot11WlanBssIfIndex_Type = Integer32
_Hh3cDot11WlanBssIfIndex_Object = MibTableColumn
hh3cDot11WlanBssIfIndex = _Hh3cDot11WlanBssIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 2, 1, 2),
    _Hh3cDot11WlanBssIfIndex_Type()
)
hh3cDot11WlanBssIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WlanBssIfIndex.setStatus("current")
_Hh3cDot11WlanBssRowStatus_Type = RowStatus
_Hh3cDot11WlanBssRowStatus_Object = MibTableColumn
hh3cDot11WlanBssRowStatus = _Hh3cDot11WlanBssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 2, 1, 3),
    _Hh3cDot11WlanBssRowStatus_Type()
)
hh3cDot11WlanBssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanBssRowStatus.setStatus("current")
_Hh3cDot11WLANEthernetIfTable_Object = MibTable
hh3cDot11WLANEthernetIfTable = _Hh3cDot11WLANEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11WLANEthernetIfTable.setStatus("current")
_Hh3cDot11WLANEthernetIfEntry_Object = MibTableRow
hh3cDot11WLANEthernetIfEntry = _Hh3cDot11WLANEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 3, 1)
)
hh3cDot11WLANEthernetIfEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11WlanEthernetIfNumber"),
)
if mibBuilder.loadTexts:
    hh3cDot11WLANEthernetIfEntry.setStatus("current")
_Hh3cDot11WlanEthernetIfNumber_Type = Integer32
_Hh3cDot11WlanEthernetIfNumber_Object = MibTableColumn
hh3cDot11WlanEthernetIfNumber = _Hh3cDot11WlanEthernetIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 3, 1, 1),
    _Hh3cDot11WlanEthernetIfNumber_Type()
)
hh3cDot11WlanEthernetIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WlanEthernetIfNumber.setStatus("current")
_Hh3cDot11WLANEthernetIfIndex_Type = Integer32
_Hh3cDot11WLANEthernetIfIndex_Object = MibTableColumn
hh3cDot11WLANEthernetIfIndex = _Hh3cDot11WLANEthernetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 3, 1, 2),
    _Hh3cDot11WLANEthernetIfIndex_Type()
)
hh3cDot11WLANEthernetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WLANEthernetIfIndex.setStatus("current")
_Hh3cDot11WlanEthernetRowStatus_Type = RowStatus
_Hh3cDot11WlanEthernetRowStatus_Object = MibTableColumn
hh3cDot11WlanEthernetRowStatus = _Hh3cDot11WlanEthernetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 3, 1, 3),
    _Hh3cDot11WlanEthernetRowStatus_Type()
)
hh3cDot11WlanEthernetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanEthernetRowStatus.setStatus("current")
_Hh3cDot11PortSecurityTable_Object = MibTable
hh3cDot11PortSecurityTable = _Hh3cDot11PortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11PortSecurityTable.setStatus("current")
_Hh3cDot11PortSecurityEntry_Object = MibTableRow
hh3cDot11PortSecurityEntry = _Hh3cDot11PortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4, 1)
)
hh3cDot11PortSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11PortSecurityEntry.setStatus("current")


class _Hh3cDot11PortSecurityMode_Type(Integer32):
    """Custom type hh3cDot11PortSecurityMode based on Integer32"""
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
        *(("macAddressAndPsk", 4),
          ("noRestrictions", 1),
          ("psk", 3),
          ("userLoginSecureExt", 2),
          ("userLoginSecureExtOrPsk", 5),
          ("wapi", 6))
    )


_Hh3cDot11PortSecurityMode_Type.__name__ = "Integer32"
_Hh3cDot11PortSecurityMode_Object = MibTableColumn
hh3cDot11PortSecurityMode = _Hh3cDot11PortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4, 1, 1),
    _Hh3cDot11PortSecurityMode_Type()
)
hh3cDot11PortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11PortSecurityMode.setStatus("current")


class _Hh3cDot11SecurityUserLoginTxKeyType_Type(Integer32):
    """Custom type hh3cDot11SecurityUserLoginTxKeyType based on Integer32"""
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


_Hh3cDot11SecurityUserLoginTxKeyType_Type.__name__ = "Integer32"
_Hh3cDot11SecurityUserLoginTxKeyType_Object = MibTableColumn
hh3cDot11SecurityUserLoginTxKeyType = _Hh3cDot11SecurityUserLoginTxKeyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4, 1, 2),
    _Hh3cDot11SecurityUserLoginTxKeyType_Type()
)
hh3cDot11SecurityUserLoginTxKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SecurityUserLoginTxKeyType.setStatus("current")


class _Hh3cDot11SecurityPskKeyMode_Type(Integer32):
    """Custom type hh3cDot11SecurityPskKeyMode based on Integer32"""
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


_Hh3cDot11SecurityPskKeyMode_Type.__name__ = "Integer32"
_Hh3cDot11SecurityPskKeyMode_Object = MibTableColumn
hh3cDot11SecurityPskKeyMode = _Hh3cDot11SecurityPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4, 1, 3),
    _Hh3cDot11SecurityPskKeyMode_Type()
)
hh3cDot11SecurityPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SecurityPskKeyMode.setStatus("current")
_Hh3cDot11SecurityPskKeyString_Type = DisplayString
_Hh3cDot11SecurityPskKeyString_Object = MibTableColumn
hh3cDot11SecurityPskKeyString = _Hh3cDot11SecurityPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4, 1, 4),
    _Hh3cDot11SecurityPskKeyString_Type()
)
hh3cDot11SecurityPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SecurityPskKeyString.setStatus("current")
_Hh3cDot11WlanMeshIfTable_Object = MibTable
hh3cDot11WlanMeshIfTable = _Hh3cDot11WlanMeshIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11WlanMeshIfTable.setStatus("current")
_Hh3cDot11WlanMeshIfEntry_Object = MibTableRow
hh3cDot11WlanMeshIfEntry = _Hh3cDot11WlanMeshIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 5, 1)
)
hh3cDot11WlanMeshIfEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11WlanMeshIfNumber"),
)
if mibBuilder.loadTexts:
    hh3cDot11WlanMeshIfEntry.setStatus("current")
_Hh3cDot11WlanMeshIfNumber_Type = Integer32
_Hh3cDot11WlanMeshIfNumber_Object = MibTableColumn
hh3cDot11WlanMeshIfNumber = _Hh3cDot11WlanMeshIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 5, 1, 1),
    _Hh3cDot11WlanMeshIfNumber_Type()
)
hh3cDot11WlanMeshIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WlanMeshIfNumber.setStatus("current")
_Hh3cDot11WlanMeshIfIndex_Type = Integer32
_Hh3cDot11WlanMeshIfIndex_Object = MibTableColumn
hh3cDot11WlanMeshIfIndex = _Hh3cDot11WlanMeshIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 5, 1, 2),
    _Hh3cDot11WlanMeshIfIndex_Type()
)
hh3cDot11WlanMeshIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WlanMeshIfIndex.setStatus("current")
_Hh3cDot11WlanMeshRowStatus_Type = RowStatus
_Hh3cDot11WlanMeshRowStatus_Object = MibTableColumn
hh3cDot11WlanMeshRowStatus = _Hh3cDot11WlanMeshRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 5, 1, 3),
    _Hh3cDot11WlanMeshRowStatus_Type()
)
hh3cDot11WlanMeshRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanMeshRowStatus.setStatus("current")
_Hh3cDot11ACBackupGroup_ObjectIdentity = ObjectIdentity
hh3cDot11ACBackupGroup = _Hh3cDot11ACBackupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 7)
)
_Hh3cDot11BackupACAdrssIP_Type = InetAddress
_Hh3cDot11BackupACAdrssIP_Object = MibScalar
hh3cDot11BackupACAdrssIP = _Hh3cDot11BackupACAdrssIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 7, 1),
    _Hh3cDot11BackupACAdrssIP_Type()
)
hh3cDot11BackupACAdrssIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11BackupACAdrssIP.setStatus("current")
_Hh3cDot11BackupACAdrssIPv6_Type = InetAddress
_Hh3cDot11BackupACAdrssIPv6_Object = MibScalar
hh3cDot11BackupACAdrssIPv6 = _Hh3cDot11BackupACAdrssIPv6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 7, 2),
    _Hh3cDot11BackupACAdrssIPv6_Type()
)
hh3cDot11BackupACAdrssIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11BackupACAdrssIPv6.setStatus("current")
_Hh3cDot11RadioElementConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RadioElementConfigGroup = _Hh3cDot11RadioElementConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8)
)
_Hh3cDot11nRadioCfgTable_Object = MibTable
hh3cDot11nRadioCfgTable = _Hh3cDot11nRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfgTable.setStatus("current")
_Hh3cDot11nRadioCfgEntry_Object = MibTableRow
hh3cDot11nRadioCfgEntry = _Hh3cDot11nRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1)
)
hh3cDot11nRadioCfgEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11nRadioCfgIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfgEntry.setStatus("current")
_Hh3cDot11nRadioCfgIndex_Type = Hh3cDot11RadioElementIndex
_Hh3cDot11nRadioCfgIndex_Object = MibTableColumn
hh3cDot11nRadioCfgIndex = _Hh3cDot11nRadioCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 1),
    _Hh3cDot11nRadioCfgIndex_Type()
)
hh3cDot11nRadioCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfgIndex.setStatus("current")


class _Hh3cDot11nAMpduEnable_Type(TruthValue):
    """Custom type hh3cDot11nAMpduEnable based on TruthValue"""


_Hh3cDot11nAMpduEnable_Object = MibTableColumn
hh3cDot11nAMpduEnable = _Hh3cDot11nAMpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 2),
    _Hh3cDot11nAMpduEnable_Type()
)
hh3cDot11nAMpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nAMpduEnable.setStatus("current")


class _Hh3cDot11nAMsduEnable_Type(TruthValue):
    """Custom type hh3cDot11nAMsduEnable based on TruthValue"""


_Hh3cDot11nAMsduEnable_Object = MibTableColumn
hh3cDot11nAMsduEnable = _Hh3cDot11nAMsduEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 3),
    _Hh3cDot11nAMsduEnable_Type()
)
hh3cDot11nAMsduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nAMsduEnable.setStatus("current")


class _Hh3cDot11nClientDot11nOnly_Type(TruthValue):
    """Custom type hh3cDot11nClientDot11nOnly based on TruthValue"""


_Hh3cDot11nClientDot11nOnly_Object = MibTableColumn
hh3cDot11nClientDot11nOnly = _Hh3cDot11nClientDot11nOnly_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 4),
    _Hh3cDot11nClientDot11nOnly_Type()
)
hh3cDot11nClientDot11nOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nClientDot11nOnly.setStatus("current")


class _Hh3cDot11nChanelBand_Type(Integer32):
    """Custom type hh3cDot11nChanelBand based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode20", 1),
          ("mode40", 2))
    )


_Hh3cDot11nChanelBand_Type.__name__ = "Integer32"
_Hh3cDot11nChanelBand_Object = MibTableColumn
hh3cDot11nChanelBand = _Hh3cDot11nChanelBand_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 5),
    _Hh3cDot11nChanelBand_Type()
)
hh3cDot11nChanelBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nChanelBand.setStatus("current")


class _Hh3cDot11nShortGiEnable_Type(TruthValue):
    """Custom type hh3cDot11nShortGiEnable based on TruthValue"""


_Hh3cDot11nShortGiEnable_Object = MibTableColumn
hh3cDot11nShortGiEnable = _Hh3cDot11nShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 6),
    _Hh3cDot11nShortGiEnable_Type()
)
hh3cDot11nShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nShortGiEnable.setStatus("current")
_Hh3cDot11RadioWDSTable_Object = MibTable
hh3cDot11RadioWDSTable = _Hh3cDot11RadioWDSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioWDSTable.setStatus("current")
_Hh3cDot11RadioWDSEntry_Object = MibTableRow
hh3cDot11RadioWDSEntry = _Hh3cDot11RadioWDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1)
)
hh3cDot11RadioWDSEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioWDSIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioWDSEntry.setStatus("current")
_Hh3cDot11RadioWDSIndex_Type = Hh3cDot11RadioElementIndex
_Hh3cDot11RadioWDSIndex_Object = MibTableColumn
hh3cDot11RadioWDSIndex = _Hh3cDot11RadioWDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1, 1),
    _Hh3cDot11RadioWDSIndex_Type()
)
hh3cDot11RadioWDSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioWDSIndex.setStatus("current")


class _Hh3cDot11RadioWDSMode_Type(Integer32):
    """Custom type hh3cDot11RadioWDSMode based on Integer32"""
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


_Hh3cDot11RadioWDSMode_Type.__name__ = "Integer32"
_Hh3cDot11RadioWDSMode_Object = MibTableColumn
hh3cDot11RadioWDSMode = _Hh3cDot11RadioWDSMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1, 2),
    _Hh3cDot11RadioWDSMode_Type()
)
hh3cDot11RadioWDSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioWDSMode.setStatus("current")


class _Hh3cDot11RadioWDSNetWorkID_Type(OctetString):
    """Custom type hh3cDot11RadioWDSNetWorkID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDot11RadioWDSNetWorkID_Type.__name__ = "OctetString"
_Hh3cDot11RadioWDSNetWorkID_Object = MibTableColumn
hh3cDot11RadioWDSNetWorkID = _Hh3cDot11RadioWDSNetWorkID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1, 3),
    _Hh3cDot11RadioWDSNetWorkID_Type()
)
hh3cDot11RadioWDSNetWorkID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioWDSNetWorkID.setStatus("current")


class _Hh3cDot11WDSSecPskKeyMode_Type(Integer32):
    """Custom type hh3cDot11WDSSecPskKeyMode based on Integer32"""
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


_Hh3cDot11WDSSecPskKeyMode_Type.__name__ = "Integer32"
_Hh3cDot11WDSSecPskKeyMode_Object = MibTableColumn
hh3cDot11WDSSecPskKeyMode = _Hh3cDot11WDSSecPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1, 4),
    _Hh3cDot11WDSSecPskKeyMode_Type()
)
hh3cDot11WDSSecPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WDSSecPskKeyMode.setStatus("current")
_Hh3cDot11WDSSecPskKeyString_Type = DisplayString
_Hh3cDot11WDSSecPskKeyString_Object = MibTableColumn
hh3cDot11WDSSecPskKeyString = _Hh3cDot11WDSSecPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1, 5),
    _Hh3cDot11WDSSecPskKeyString_Type()
)
hh3cDot11WDSSecPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WDSSecPskKeyString.setStatus("current")
_Hh3cDot11CfgNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cDot11CfgNotifyGroup = _Hh3cDot11CfgNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9)
)
_Hh3cDot11CfgNotifications_ObjectIdentity = ObjectIdentity
hh3cDot11CfgNotifications = _Hh3cDot11CfgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 0)
)
_Hh3cDot11CfgTrapVarObjects_ObjectIdentity = ObjectIdentity
hh3cDot11CfgTrapVarObjects = _Hh3cDot11CfgTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1)
)


class _Hh3cDot11PreConflictTemplateNum_Type(Integer32):
    """Custom type hh3cDot11PreConflictTemplateNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cDot11PreConflictTemplateNum_Type.__name__ = "Integer32"
_Hh3cDot11PreConflictTemplateNum_Object = MibScalar
hh3cDot11PreConflictTemplateNum = _Hh3cDot11PreConflictTemplateNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 1),
    _Hh3cDot11PreConflictTemplateNum_Type()
)
hh3cDot11PreConflictTemplateNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11PreConflictTemplateNum.setStatus("current")


class _Hh3cDot11CurrConflictTemplateNum_Type(Integer32):
    """Custom type hh3cDot11CurrConflictTemplateNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cDot11CurrConflictTemplateNum_Type.__name__ = "Integer32"
_Hh3cDot11CurrConflictTemplateNum_Object = MibScalar
hh3cDot11CurrConflictTemplateNum = _Hh3cDot11CurrConflictTemplateNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 2),
    _Hh3cDot11CurrConflictTemplateNum_Type()
)
hh3cDot11CurrConflictTemplateNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11CurrConflictTemplateNum.setStatus("current")


class _Hh3cDot11ConflictCipherIdx_Type(Integer32):
    """Custom type hh3cDot11ConflictCipherIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cDot11ConflictCipherIdx_Type.__name__ = "Integer32"
_Hh3cDot11ConflictCipherIdx_Object = MibScalar
hh3cDot11ConflictCipherIdx = _Hh3cDot11ConflictCipherIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 3),
    _Hh3cDot11ConflictCipherIdx_Type()
)
hh3cDot11ConflictCipherIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ConflictCipherIdx.setStatus("current")
_Hh3cDot11ConfigureAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11ConfigureAPID_Object = MibScalar
hh3cDot11ConfigureAPID = _Hh3cDot11ConfigureAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 4),
    _Hh3cDot11ConfigureAPID_Type()
)
hh3cDot11ConfigureAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ConfigureAPID.setStatus("current")
_Hh3cDot11ConfigureRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11ConfigureRadioID_Object = MibScalar
hh3cDot11ConfigureRadioID = _Hh3cDot11ConfigureRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 5),
    _Hh3cDot11ConfigureRadioID_Type()
)
hh3cDot11ConfigureRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ConfigureRadioID.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cDot11CfgCipherChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 0, 1)
)
hh3cDot11CfgCipherChange.setObjects(
      *(("HH3C-DOT11-CFG-MIB", "hh3cDot11SSIDName"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11SecurityCiphers"))
)
if mibBuilder.loadTexts:
    hh3cDot11CfgCipherChange.setStatus(
        "current"
    )

hh3cDot11CfgPSKChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 0, 2)
)
hh3cDot11CfgPSKChange.setObjects(
    ("HH3C-DOT11-CFG-MIB", "hh3cDot11SSIDName")
)
if mibBuilder.loadTexts:
    hh3cDot11CfgPSKChange.setStatus(
        "current"
    )

hh3cDot11SSIDWepIDConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 0, 3)
)
hh3cDot11SSIDWepIDConflictTrap.setObjects(
      *(("HH3C-DOT11-CFG-MIB", "hh3cDot11PreConflictTemplateNum"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11CurrConflictTemplateNum"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11ConflictCipherIdx"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11ConfigureAPID"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11ConfigureRadioID"))
)
if mibBuilder.loadTexts:
    hh3cDot11SSIDWepIDConflictTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-CFG-MIB",
    **{"hh3cDot11CFG": hh3cDot11CFG,
       "hh3cDot11GlobeConfigGroup": hh3cDot11GlobeConfigGroup,
       "hh3cDot11GlobalCountryCode": hh3cDot11GlobalCountryCode,
       "hh3cDot11StaKeepALiveTimerIntvl": hh3cDot11StaKeepALiveTimerIntvl,
       "hh3cDot11StaIdleTimerIntvl": hh3cDot11StaIdleTimerIntvl,
       "hh3cDot11BroadcastProbeReply": hh3cDot11BroadcastProbeReply,
       "hh3cDot11APScanMode": hh3cDot11APScanMode,
       "hh3cDot11ACCtrlTunnelSecSupport": hh3cDot11ACCtrlTunnelSecSupport,
       "hh3cDot11ACDataTunnelSecSupport": hh3cDot11ACDataTunnelSecSupport,
       "hh3cDot11ACAutoAPSupport": hh3cDot11ACAutoAPSupport,
       "hh3cDot11AutoAPName": hh3cDot11AutoAPName,
       "hh3cDot11PersistentName": hh3cDot11PersistentName,
       "hh3cDot11IntfTrapThreshold": hh3cDot11IntfTrapThreshold,
       "hh3cDot11MonitorInterval": hh3cDot11MonitorInterval,
       "hh3cDot11SampleInterval": hh3cDot11SampleInterval,
       "hh3cDot11ChnlSwitChkInterval": hh3cDot11ChnlSwitChkInterval,
       "hh3cDot11APUserUplimit": hh3cDot11APUserUplimit,
       "hh3cDot11APL2IsolateEnable": hh3cDot11APL2IsolateEnable,
       "hh3cDot11APBSSIDSupportNum": hh3cDot11APBSSIDSupportNum,
       "hh3cDot11APLastUpdateStatTime": hh3cDot11APLastUpdateStatTime,
       "hh3cDot11APDoSProtectEnable": hh3cDot11APDoSProtectEnable,
       "hh3cDot11MaxAPPerIf": hh3cDot11MaxAPPerIf,
       "hh3cDot11SampleTimeStamp": hh3cDot11SampleTimeStamp,
       "hh3cDot11UplinkTrackId": hh3cDot11UplinkTrackId,
       "hh3cDot11RtCollectSwitch": hh3cDot11RtCollectSwitch,
       "hh3cDot11RglCollectIntvl": hh3cDot11RglCollectIntvl,
       "hh3cDot11RtCollectIntvl": hh3cDot11RtCollectIntvl,
       "hh3cDot11AllAPCpuUsageThreshold": hh3cDot11AllAPCpuUsageThreshold,
       "hh3cDot11AllAPMemUsageThreshold": hh3cDot11AllAPMemUsageThreshold,
       "hh3cDot11AdjIntfTrapThreshold": hh3cDot11AdjIntfTrapThreshold,
       "hh3cDot11PolicyConfigGroup": hh3cDot11PolicyConfigGroup,
       "hh3cDot11RadioPolicyTable": hh3cDot11RadioPolicyTable,
       "hh3cDot11RadioPolicyEntry": hh3cDot11RadioPolicyEntry,
       "hh3cDot11RadioPolicyName": hh3cDot11RadioPolicyName,
       "hh3cDot11BeaconInterval": hh3cDot11BeaconInterval,
       "hh3cDot11DtimInterval": hh3cDot11DtimInterval,
       "hh3cDot11RtsThreshold": hh3cDot11RtsThreshold,
       "hh3cDot11FragThreshold": hh3cDot11FragThreshold,
       "hh3cDot11ShortRetryThreshold": hh3cDot11ShortRetryThreshold,
       "hh3cDot11LongRetryThreshold": hh3cDot11LongRetryThreshold,
       "hh3cDot11MaxRxLifetime": hh3cDot11MaxRxLifetime,
       "hh3cDot11RdoPolicyRowStatus": hh3cDot11RdoPolicyRowStatus,
       "hh3cDot11RdoClientMaxCount": hh3cDot11RdoClientMaxCount,
       "hh3cDot11BeaconIntervalMs": hh3cDot11BeaconIntervalMs,
       "hh3cDot11ServicePolicyTable": hh3cDot11ServicePolicyTable,
       "hh3cDot11ServicePolicyEntry": hh3cDot11ServicePolicyEntry,
       "hh3cDot11ServicePolicyID": hh3cDot11ServicePolicyID,
       "hh3cDot11SSIDName": hh3cDot11SSIDName,
       "hh3cDot11SSIDHidden": hh3cDot11SSIDHidden,
       "hh3cDot11AuthenMode": hh3cDot11AuthenMode,
       "hh3cDot11SSIDEncryptionMode": hh3cDot11SSIDEncryptionMode,
       "hh3cDot11WlanInfBindingType": hh3cDot11WlanInfBindingType,
       "hh3cDot11WlanInfBindingID": hh3cDot11WlanInfBindingID,
       "hh3cDot11SrvPolicyRowStatus": hh3cDot11SrvPolicyRowStatus,
       "hh3cDot11ClientMaxCount": hh3cDot11ClientMaxCount,
       "hh3cDot11SPInCirMode": hh3cDot11SPInCirMode,
       "hh3cDot11SPInCirValue": hh3cDot11SPInCirValue,
       "hh3cDot11SPOutCirMode": hh3cDot11SPOutCirMode,
       "hh3cDot11SPOutCirValue": hh3cDot11SPOutCirValue,
       "hh3cDot11WlanInfPVID": hh3cDot11WlanInfPVID,
       "hh3cDot11SPInCirStaticValue": hh3cDot11SPInCirStaticValue,
       "hh3cDot11SPOutCirStaticValue": hh3cDot11SPOutCirStaticValue,
       "hh3cDot11SPIsolate": hh3cDot11SPIsolate,
       "hh3cDot11ServicePolicyExtTable": hh3cDot11ServicePolicyExtTable,
       "hh3cDot11ServicePolicyExtEntry": hh3cDot11ServicePolicyExtEntry,
       "hh3cDot11ServicePolicyExtID": hh3cDot11ServicePolicyExtID,
       "hh3cDot11SecIEStatus": hh3cDot11SecIEStatus,
       "hh3cDot11SecurityCiphers": hh3cDot11SecurityCiphers,
       "hh3cDot11CipherKeyIndex": hh3cDot11CipherKeyIndex,
       "hh3cDot11CipherKey": hh3cDot11CipherKey,
       "hh3cDot11SrvPolicyExtRowStatus": hh3cDot11SrvPolicyExtRowStatus,
       "hh3cDot11CipherKeyType": hh3cDot11CipherKeyType,
       "hh3cDot11RadioPolicyExtTable": hh3cDot11RadioPolicyExtTable,
       "hh3cDot11RadioPolicyExtEntry": hh3cDot11RadioPolicyExtEntry,
       "hh3cDot11RPAPSerialID": hh3cDot11RPAPSerialID,
       "hh3cDot11RPRadioID": hh3cDot11RPRadioID,
       "hh3cDot11RPBeaconInterval": hh3cDot11RPBeaconInterval,
       "hh3cDot11RPDtimInterval": hh3cDot11RPDtimInterval,
       "hh3cDot11RPRtsThreshold": hh3cDot11RPRtsThreshold,
       "hh3cDot11RPFragThreshold": hh3cDot11RPFragThreshold,
       "hh3cDot11RPShortRetryThreshold": hh3cDot11RPShortRetryThreshold,
       "hh3cDot11RPLongRetryThreshold": hh3cDot11RPLongRetryThreshold,
       "hh3cDot11RPClientMaxCount": hh3cDot11RPClientMaxCount,
       "hh3cDot11SrvPortSecurityTable": hh3cDot11SrvPortSecurityTable,
       "hh3cDot11SrvPortSecurityEntry": hh3cDot11SrvPortSecurityEntry,
       "hh3cDot11SecurityServicePolicyID": hh3cDot11SecurityServicePolicyID,
       "hh3cDot11SrvPortSecurityMode": hh3cDot11SrvPortSecurityMode,
       "hh3cDot11SrvSecurityKeyType": hh3cDot11SrvSecurityKeyType,
       "hh3cDot11SrvSecurityPskKeyMode": hh3cDot11SrvSecurityPskKeyMode,
       "hh3cDot11SrvSecurityPskKeyString": hh3cDot11SrvSecurityPskKeyString,
       "hh3cDot11SrvPolicyExtendTable": hh3cDot11SrvPolicyExtendTable,
       "hh3cDot11SrvPolicyExtendEntry": hh3cDot11SrvPolicyExtendEntry,
       "hh3cDot11SPEnable": hh3cDot11SPEnable,
       "hh3cDot11APConfigGroup": hh3cDot11APConfigGroup,
       "hh3cDot11APTemplateTable": hh3cDot11APTemplateTable,
       "hh3cDot11APTemplateEntry": hh3cDot11APTemplateEntry,
       "hh3cDot11APTemplateName": hh3cDot11APTemplateName,
       "hh3cDot11APSerialID": hh3cDot11APSerialID,
       "hh3cDot11TemplateAPModelAlias": hh3cDot11TemplateAPModelAlias,
       "hh3cDot11Description": hh3cDot11Description,
       "hh3cDot11APWorkMode": hh3cDot11APWorkMode,
       "hh3cDot11APTemplateRowStatus": hh3cDot11APTemplateRowStatus,
       "hh3cDot11APName": hh3cDot11APName,
       "hh3cDot11StatisInterv": hh3cDot11StatisInterv,
       "hh3cDot11APBroadcastProbeReply": hh3cDot11APBroadcastProbeReply,
       "hh3cDot11StaIdleTimerInterv": hh3cDot11StaIdleTimerInterv,
       "hh3cDot11StaKeepAliveTimerInterv": hh3cDot11StaKeepAliveTimerInterv,
       "hh3cDot11APCir": hh3cDot11APCir,
       "hh3cDot11APCbs": hh3cDot11APCbs,
       "hh3cDot11APPriorityLevel": hh3cDot11APPriorityLevel,
       "hh3cDot11APElementID": hh3cDot11APElementID,
       "hh3cDot11APDevDetectEnable": hh3cDot11APDevDetectEnable,
       "hh3cDot11APGetIPMethod": hh3cDot11APGetIPMethod,
       "hh3cDot11StatisIntervMode": hh3cDot11StatisIntervMode,
       "hh3cDot11RadioToConfigTable": hh3cDot11RadioToConfigTable,
       "hh3cDot11RadioToConfigEntry": hh3cDot11RadioToConfigEntry,
       "hh3cDot11APTemplateNameCfg": hh3cDot11APTemplateNameCfg,
       "hh3cDot11CfgRadioID": hh3cDot11CfgRadioID,
       "hh3cDot11CfgRadioPolicyName": hh3cDot11CfgRadioPolicyName,
       "hh3cDot11CfgRadioType": hh3cDot11CfgRadioType,
       "hh3cDot11CfgChannel": hh3cDot11CfgChannel,
       "hh3cDot11CfgMaxTxPowerLevel": hh3cDot11CfgMaxTxPowerLevel,
       "hh3cDot11PreambleLen": hh3cDot11PreambleLen,
       "hh3cDot11CfgRadioStatus": hh3cDot11CfgRadioStatus,
       "hh3cDot11CfgRdElementID": hh3cDot11CfgRdElementID,
       "hh3cDot11CfgWorkMode": hh3cDot11CfgWorkMode,
       "hh3cDot11CfgPwrAttValue": hh3cDot11CfgPwrAttValue,
       "hh3cDot11RadioTxArithmetic": hh3cDot11RadioTxArithmetic,
       "hh3cDot11CfgChannelLockStat": hh3cDot11CfgChannelLockStat,
       "hh3cDot11CfgPowerLockStat": hh3cDot11CfgPowerLockStat,
       "hh3cDot11CfgLBRdGroupId": hh3cDot11CfgLBRdGroupId,
       "hh3cDot11CfgRRMSDRdGroupId": hh3cDot11CfgRRMSDRdGroupId,
       "hh3cDot11APServiceSetTable": hh3cDot11APServiceSetTable,
       "hh3cDot11APServiceSetEntry": hh3cDot11APServiceSetEntry,
       "hh3cDot11CfgServicePolicyID": hh3cDot11CfgServicePolicyID,
       "hh3cDot11SrvSetRowStatus": hh3cDot11SrvSetRowStatus,
       "hh3cDot11ServiceSetVlanId": hh3cDot11ServiceSetVlanId,
       "hh3cDot11APSysInfoSetTable": hh3cDot11APSysInfoSetTable,
       "hh3cDot11APSysInfoSetEntry": hh3cDot11APSysInfoSetEntry,
       "hh3cDot11APSysNetID": hh3cDot11APSysNetID,
       "hh3cDot11APCpuUsageThreshold": hh3cDot11APCpuUsageThreshold,
       "hh3cDot11APMemUsageThreshold": hh3cDot11APMemUsageThreshold,
       "hh3cDot11APLimitTable": hh3cDot11APLimitTable,
       "hh3cDot11APLimitEntry": hh3cDot11APLimitEntry,
       "hh3cDot11APSsidNumLimit": hh3cDot11APSsidNumLimit,
       "hh3cDot11APUserCntLimit": hh3cDot11APUserCntLimit,
       "hh3cDot11APUserThreshold": hh3cDot11APUserThreshold,
       "hh3cDot11APIfSetTable": hh3cDot11APIfSetTable,
       "hh3cDot11APIfSetEntry": hh3cDot11APIfSetEntry,
       "hh3cDot11APSetIfIndex": hh3cDot11APSetIfIndex,
       "hh3cDot11APIfAlias": hh3cDot11APIfAlias,
       "hh3cDot11APServiceVlanTable": hh3cDot11APServiceVlanTable,
       "hh3cDot11APServiceVlanEntry": hh3cDot11APServiceVlanEntry,
       "hh3cDot11APServiceVlanSerialID": hh3cDot11APServiceVlanSerialID,
       "hh3cDot11APServiceVlanSPID": hh3cDot11APServiceVlanSPID,
       "hh3cDot11APServiceVlanId": hh3cDot11APServiceVlanId,
       "hh3cDot11APServiceVlanRowStatus": hh3cDot11APServiceVlanRowStatus,
       "hh3cDot11RadioConfigTable": hh3cDot11RadioConfigTable,
       "hh3cDot11RadioConfigEntry": hh3cDot11RadioConfigEntry,
       "hh3cDot11RCAPSerialID": hh3cDot11RCAPSerialID,
       "hh3cDot11RCRadioID": hh3cDot11RCRadioID,
       "hh3cDot11RCRadioType": hh3cDot11RCRadioType,
       "hh3cDot11RCChannel": hh3cDot11RCChannel,
       "hh3cDot11RCPreambleLen": hh3cDot11RCPreambleLen,
       "hh3cDot11RCPwrAttValue": hh3cDot11RCPwrAttValue,
       "hh3cDot11RCApPowerLevel": hh3cDot11RCApPowerLevel,
       "hh3cDot11RCDynamicChlState": hh3cDot11RCDynamicChlState,
       "hh3cDot11RCDynamicPowerState": hh3cDot11RCDynamicPowerState,
       "hh3cDot11RCRadioStatus": hh3cDot11RCRadioStatus,
       "hh3cDot11RadioSSIDCfgTable": hh3cDot11RadioSSIDCfgTable,
       "hh3cDot11RadioSSIDCfgEntry": hh3cDot11RadioSSIDCfgEntry,
       "hh3cDot11RadioSSIDSerialID": hh3cDot11RadioSSIDSerialID,
       "hh3cDot11RadioSSIDRadioID": hh3cDot11RadioSSIDRadioID,
       "hh3cDot11RadioSSIDWLANID": hh3cDot11RadioSSIDWLANID,
       "hh3cDot11RadioSSIDIndex": hh3cDot11RadioSSIDIndex,
       "hh3cDot11RadioBSSID": hh3cDot11RadioBSSID,
       "hh3cDot11RadioSSIDRowStatus": hh3cDot11RadioSSIDRowStatus,
       "hh3cDot11APSerialIDTable": hh3cDot11APSerialIDTable,
       "hh3cDot11APSerialIDEntry": hh3cDot11APSerialIDEntry,
       "hh3cDot11SIDAPSerialID": hh3cDot11SIDAPSerialID,
       "hh3cDot11SIDAPWorkMode": hh3cDot11SIDAPWorkMode,
       "hh3cDot11SIDAPGetIPMethod": hh3cDot11SIDAPGetIPMethod,
       "hh3cDot11APSTVlanTable": hh3cDot11APSTVlanTable,
       "hh3cDot11APSTVlanEntry": hh3cDot11APSTVlanEntry,
       "hh3cDot11CfgSTVLANID": hh3cDot11CfgSTVLANID,
       "hh3cDot11CfgSTNASPortID": hh3cDot11CfgSTNASPortID,
       "hh3cDot11CfgServiceSetRowStatus": hh3cDot11CfgServiceSetRowStatus,
       "hh3cDot11RadioIntfConfigGroup": hh3cDot11RadioIntfConfigGroup,
       "hh3cDot11RadioIntfConfigTable": hh3cDot11RadioIntfConfigTable,
       "hh3cDot11RadioIntfConfigEntry": hh3cDot11RadioIntfConfigEntry,
       "hh3cDot11RadioIfIdx": hh3cDot11RadioIfIdx,
       "hh3cDot11RadioCfgBeaconIntvl": hh3cDot11RadioCfgBeaconIntvl,
       "hh3cDot11RadioCfgDtimIntvl": hh3cDot11RadioCfgDtimIntvl,
       "hh3cDot11RadioCfgRtsThreshold": hh3cDot11RadioCfgRtsThreshold,
       "hh3cDot11RadioCfgFragThreshold": hh3cDot11RadioCfgFragThreshold,
       "hh3cDot11RadioCfgShtRetryThld": hh3cDot11RadioCfgShtRetryThld,
       "hh3cDot11RadioCfglongRtrThld": hh3cDot11RadioCfglongRtrThld,
       "hh3cDot11RadioCfgMaxRxLifetime": hh3cDot11RadioCfgMaxRxLifetime,
       "hh3cDot11RadioCfgType": hh3cDot11RadioCfgType,
       "hh3cDot11RadioCfgChannel": hh3cDot11RadioCfgChannel,
       "hh3cDot11RadioCfgMaxTxPwrLvl": hh3cDot11RadioCfgMaxTxPwrLvl,
       "hh3cDot11RadioCfgPreambleLen": hh3cDot11RadioCfgPreambleLen,
       "hh3cDot11RadioCfgWorkMode": hh3cDot11RadioCfgWorkMode,
       "hh3cDot11RadioCfgOnly11gEnable": hh3cDot11RadioCfgOnly11gEnable,
       "hh3cDot11RadioIntfBindTable": hh3cDot11RadioIntfBindTable,
       "hh3cDot11RadioIntfBindEntry": hh3cDot11RadioIntfBindEntry,
       "hh3cDot11RadioIntfBindSvcPlcyID": hh3cDot11RadioIntfBindSvcPlcyID,
       "hh3cDot11RadioIntfBindIfIdx": hh3cDot11RadioIntfBindIfIdx,
       "hh3cDot11RadioIntfBindRowStatus": hh3cDot11RadioIntfBindRowStatus,
       "hh3cDot11DataRateConfigGroup": hh3cDot11DataRateConfigGroup,
       "hh3cDot11DataRateConfigTable": hh3cDot11DataRateConfigTable,
       "hh3cDot11DataRateConfigEntry": hh3cDot11DataRateConfigEntry,
       "hh3cDot11RadioTypeID": hh3cDot11RadioTypeID,
       "hh3cDot11SupportedRateSet": hh3cDot11SupportedRateSet,
       "hh3cDot11MandatoryRateSet": hh3cDot11MandatoryRateSet,
       "hh3cDot11DisabledRateSet": hh3cDot11DisabledRateSet,
       "hh3cDot11SmartRateSet": hh3cDot11SmartRateSet,
       "hh3cDot11InterfaceConfigGroup": hh3cDot11InterfaceConfigGroup,
       "hh3cDot11WlanEssIfTable": hh3cDot11WlanEssIfTable,
       "hh3cDot11WlanEssIfEntry": hh3cDot11WlanEssIfEntry,
       "hh3cDot11WlanEssIfNumber": hh3cDot11WlanEssIfNumber,
       "hh3cDot11WlanEssIfIndex": hh3cDot11WlanEssIfIndex,
       "hh3cDot11WlanEssRowStatus": hh3cDot11WlanEssRowStatus,
       "hh3cDot11WlanBssIfTable": hh3cDot11WlanBssIfTable,
       "hh3cDot11WlanBssIfEntry": hh3cDot11WlanBssIfEntry,
       "hh3cDot11WlanBssIfNumber": hh3cDot11WlanBssIfNumber,
       "hh3cDot11WlanBssIfIndex": hh3cDot11WlanBssIfIndex,
       "hh3cDot11WlanBssRowStatus": hh3cDot11WlanBssRowStatus,
       "hh3cDot11WLANEthernetIfTable": hh3cDot11WLANEthernetIfTable,
       "hh3cDot11WLANEthernetIfEntry": hh3cDot11WLANEthernetIfEntry,
       "hh3cDot11WlanEthernetIfNumber": hh3cDot11WlanEthernetIfNumber,
       "hh3cDot11WLANEthernetIfIndex": hh3cDot11WLANEthernetIfIndex,
       "hh3cDot11WlanEthernetRowStatus": hh3cDot11WlanEthernetRowStatus,
       "hh3cDot11PortSecurityTable": hh3cDot11PortSecurityTable,
       "hh3cDot11PortSecurityEntry": hh3cDot11PortSecurityEntry,
       "hh3cDot11PortSecurityMode": hh3cDot11PortSecurityMode,
       "hh3cDot11SecurityUserLoginTxKeyType": hh3cDot11SecurityUserLoginTxKeyType,
       "hh3cDot11SecurityPskKeyMode": hh3cDot11SecurityPskKeyMode,
       "hh3cDot11SecurityPskKeyString": hh3cDot11SecurityPskKeyString,
       "hh3cDot11WlanMeshIfTable": hh3cDot11WlanMeshIfTable,
       "hh3cDot11WlanMeshIfEntry": hh3cDot11WlanMeshIfEntry,
       "hh3cDot11WlanMeshIfNumber": hh3cDot11WlanMeshIfNumber,
       "hh3cDot11WlanMeshIfIndex": hh3cDot11WlanMeshIfIndex,
       "hh3cDot11WlanMeshRowStatus": hh3cDot11WlanMeshRowStatus,
       "hh3cDot11ACBackupGroup": hh3cDot11ACBackupGroup,
       "hh3cDot11BackupACAdrssIP": hh3cDot11BackupACAdrssIP,
       "hh3cDot11BackupACAdrssIPv6": hh3cDot11BackupACAdrssIPv6,
       "hh3cDot11RadioElementConfigGroup": hh3cDot11RadioElementConfigGroup,
       "hh3cDot11nRadioCfgTable": hh3cDot11nRadioCfgTable,
       "hh3cDot11nRadioCfgEntry": hh3cDot11nRadioCfgEntry,
       "hh3cDot11nRadioCfgIndex": hh3cDot11nRadioCfgIndex,
       "hh3cDot11nAMpduEnable": hh3cDot11nAMpduEnable,
       "hh3cDot11nAMsduEnable": hh3cDot11nAMsduEnable,
       "hh3cDot11nClientDot11nOnly": hh3cDot11nClientDot11nOnly,
       "hh3cDot11nChanelBand": hh3cDot11nChanelBand,
       "hh3cDot11nShortGiEnable": hh3cDot11nShortGiEnable,
       "hh3cDot11RadioWDSTable": hh3cDot11RadioWDSTable,
       "hh3cDot11RadioWDSEntry": hh3cDot11RadioWDSEntry,
       "hh3cDot11RadioWDSIndex": hh3cDot11RadioWDSIndex,
       "hh3cDot11RadioWDSMode": hh3cDot11RadioWDSMode,
       "hh3cDot11RadioWDSNetWorkID": hh3cDot11RadioWDSNetWorkID,
       "hh3cDot11WDSSecPskKeyMode": hh3cDot11WDSSecPskKeyMode,
       "hh3cDot11WDSSecPskKeyString": hh3cDot11WDSSecPskKeyString,
       "hh3cDot11CfgNotifyGroup": hh3cDot11CfgNotifyGroup,
       "hh3cDot11CfgNotifications": hh3cDot11CfgNotifications,
       "hh3cDot11CfgCipherChange": hh3cDot11CfgCipherChange,
       "hh3cDot11CfgPSKChange": hh3cDot11CfgPSKChange,
       "hh3cDot11SSIDWepIDConflictTrap": hh3cDot11SSIDWepIDConflictTrap,
       "hh3cDot11CfgTrapVarObjects": hh3cDot11CfgTrapVarObjects,
       "hh3cDot11PreConflictTemplateNum": hh3cDot11PreConflictTemplateNum,
       "hh3cDot11CurrConflictTemplateNum": hh3cDot11CurrConflictTemplateNum,
       "hh3cDot11ConflictCipherIdx": hh3cDot11ConflictCipherIdx,
       "hh3cDot11ConfigureAPID": hh3cDot11ConfigureAPID,
       "hh3cDot11ConfigureRadioID": hh3cDot11ConfigureRadioID}
)
