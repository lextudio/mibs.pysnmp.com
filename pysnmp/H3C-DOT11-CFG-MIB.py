# SNMP MIB module (H3C-DOT11-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-DOT11-CFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:11 2024
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

(H3cDot11AuthenType,
 H3cDot11ChannelScopeType,
 H3cDot11CirMode,
 H3cDot11ObjectIDType,
 H3cDot11PreambleType,
 H3cDot11RadioElementIndex,
 H3cDot11RadioScopeType,
 H3cDot11RadioType,
 H3cDot11SSIDEncryptModeType,
 H3cDot11SSIDStringType,
 H3cDot11SecIEStatusType,
 H3cDot11ServicePolicyIDType,
 H3cDot11TunnelSecSchemType,
 H3cDot11TxPwrLevelScopeType,
 H3cDot11WorkMode,
 h3cDot11,
 h3cDot11APElementIndex) = mibBuilder.importSymbols(
    "H3C-DOT11-REF-MIB",
    "H3cDot11AuthenType",
    "H3cDot11ChannelScopeType",
    "H3cDot11CirMode",
    "H3cDot11ObjectIDType",
    "H3cDot11PreambleType",
    "H3cDot11RadioElementIndex",
    "H3cDot11RadioScopeType",
    "H3cDot11RadioType",
    "H3cDot11SSIDEncryptModeType",
    "H3cDot11SSIDStringType",
    "H3cDot11SecIEStatusType",
    "H3cDot11ServicePolicyIDType",
    "H3cDot11TunnelSecSchemType",
    "H3cDot11TxPwrLevelScopeType",
    "H3cDot11WorkMode",
    "h3cDot11",
    "h3cDot11APElementIndex")

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

h3cDot11CFG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4)
)
h3cDot11CFG.setRevisions(
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

_H3cDot11GlobeConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11GlobeConfigGroup = _H3cDot11GlobeConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1)
)


class _H3cDot11GlobalCountryCode_Type(OctetString):
    """Custom type h3cDot11GlobalCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_H3cDot11GlobalCountryCode_Type.__name__ = "OctetString"
_H3cDot11GlobalCountryCode_Object = MibScalar
h3cDot11GlobalCountryCode = _H3cDot11GlobalCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 1),
    _H3cDot11GlobalCountryCode_Type()
)
h3cDot11GlobalCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11GlobalCountryCode.setStatus("current")


class _H3cDot11StaKeepALiveTimerIntvl_Type(Unsigned32):
    """Custom type h3cDot11StaKeepALiveTimerIntvl based on Unsigned32"""
    defaultValue = 0


_H3cDot11StaKeepALiveTimerIntvl_Object = MibScalar
h3cDot11StaKeepALiveTimerIntvl = _H3cDot11StaKeepALiveTimerIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 2),
    _H3cDot11StaKeepALiveTimerIntvl_Type()
)
h3cDot11StaKeepALiveTimerIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11StaKeepALiveTimerIntvl.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StaKeepALiveTimerIntvl.setUnits("second")
_H3cDot11StaIdleTimerIntvl_Type = Integer32
_H3cDot11StaIdleTimerIntvl_Object = MibScalar
h3cDot11StaIdleTimerIntvl = _H3cDot11StaIdleTimerIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 3),
    _H3cDot11StaIdleTimerIntvl_Type()
)
h3cDot11StaIdleTimerIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11StaIdleTimerIntvl.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StaIdleTimerIntvl.setUnits("second")


class _H3cDot11BroadcastProbeReply_Type(TruthValue):
    """Custom type h3cDot11BroadcastProbeReply based on TruthValue"""


_H3cDot11BroadcastProbeReply_Object = MibScalar
h3cDot11BroadcastProbeReply = _H3cDot11BroadcastProbeReply_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 4),
    _H3cDot11BroadcastProbeReply_Type()
)
h3cDot11BroadcastProbeReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11BroadcastProbeReply.setStatus("current")


class _H3cDot11APScanMode_Type(Integer32):
    """Custom type h3cDot11APScanMode based on Integer32"""
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


_H3cDot11APScanMode_Type.__name__ = "Integer32"
_H3cDot11APScanMode_Object = MibScalar
h3cDot11APScanMode = _H3cDot11APScanMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 5),
    _H3cDot11APScanMode_Type()
)
h3cDot11APScanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APScanMode.setStatus("current")
_H3cDot11ACCtrlTunnelSecSupport_Type = H3cDot11TunnelSecSchemType
_H3cDot11ACCtrlTunnelSecSupport_Object = MibScalar
h3cDot11ACCtrlTunnelSecSupport = _H3cDot11ACCtrlTunnelSecSupport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 6),
    _H3cDot11ACCtrlTunnelSecSupport_Type()
)
h3cDot11ACCtrlTunnelSecSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11ACCtrlTunnelSecSupport.setStatus("current")


class _H3cDot11ACDataTunnelSecSupport_Type(H3cDot11TunnelSecSchemType):
    """Custom type h3cDot11ACDataTunnelSecSupport based on H3cDot11TunnelSecSchemType"""


_H3cDot11ACDataTunnelSecSupport_Object = MibScalar
h3cDot11ACDataTunnelSecSupport = _H3cDot11ACDataTunnelSecSupport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 7),
    _H3cDot11ACDataTunnelSecSupport_Type()
)
h3cDot11ACDataTunnelSecSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11ACDataTunnelSecSupport.setStatus("current")


class _H3cDot11ACAutoAPSupport_Type(TruthValue):
    """Custom type h3cDot11ACAutoAPSupport based on TruthValue"""


_H3cDot11ACAutoAPSupport_Object = MibScalar
h3cDot11ACAutoAPSupport = _H3cDot11ACAutoAPSupport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 8),
    _H3cDot11ACAutoAPSupport_Type()
)
h3cDot11ACAutoAPSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11ACAutoAPSupport.setStatus("current")


class _H3cDot11AutoAPName_Type(OctetString):
    """Custom type h3cDot11AutoAPName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11AutoAPName_Type.__name__ = "OctetString"
_H3cDot11AutoAPName_Object = MibScalar
h3cDot11AutoAPName = _H3cDot11AutoAPName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 9),
    _H3cDot11AutoAPName_Type()
)
h3cDot11AutoAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11AutoAPName.setStatus("current")


class _H3cDot11PersistentName_Type(OctetString):
    """Custom type h3cDot11PersistentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11PersistentName_Type.__name__ = "OctetString"
_H3cDot11PersistentName_Object = MibScalar
h3cDot11PersistentName = _H3cDot11PersistentName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 10),
    _H3cDot11PersistentName_Type()
)
h3cDot11PersistentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11PersistentName.setStatus("current")
_H3cDot11IntfTrapThreshold_Type = Integer32
_H3cDot11IntfTrapThreshold_Object = MibScalar
h3cDot11IntfTrapThreshold = _H3cDot11IntfTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 11),
    _H3cDot11IntfTrapThreshold_Type()
)
h3cDot11IntfTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11IntfTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11IntfTrapThreshold.setUnits("dbm")


class _H3cDot11MonitorInterval_Type(Unsigned32):
    """Custom type h3cDot11MonitorInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 15),
    )


_H3cDot11MonitorInterval_Type.__name__ = "Unsigned32"
_H3cDot11MonitorInterval_Object = MibScalar
h3cDot11MonitorInterval = _H3cDot11MonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 12),
    _H3cDot11MonitorInterval_Type()
)
h3cDot11MonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11MonitorInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11MonitorInterval.setUnits("minute")


class _H3cDot11SampleInterval_Type(Unsigned32):
    """Custom type h3cDot11SampleInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 300),
    )


_H3cDot11SampleInterval_Type.__name__ = "Unsigned32"
_H3cDot11SampleInterval_Object = MibScalar
h3cDot11SampleInterval = _H3cDot11SampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 13),
    _H3cDot11SampleInterval_Type()
)
h3cDot11SampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11SampleInterval.setUnits("second")


class _H3cDot11ChnlSwitChkInterval_Type(Unsigned32):
    """Custom type h3cDot11ChnlSwitChkInterval based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 180),
    )


_H3cDot11ChnlSwitChkInterval_Type.__name__ = "Unsigned32"
_H3cDot11ChnlSwitChkInterval_Object = MibScalar
h3cDot11ChnlSwitChkInterval = _H3cDot11ChnlSwitChkInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 14),
    _H3cDot11ChnlSwitChkInterval_Type()
)
h3cDot11ChnlSwitChkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11ChnlSwitChkInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11ChnlSwitChkInterval.setUnits("minute")


class _H3cDot11APUserUplimit_Type(Unsigned32):
    """Custom type h3cDot11APUserUplimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cDot11APUserUplimit_Type.__name__ = "Unsigned32"
_H3cDot11APUserUplimit_Object = MibScalar
h3cDot11APUserUplimit = _H3cDot11APUserUplimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 15),
    _H3cDot11APUserUplimit_Type()
)
h3cDot11APUserUplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APUserUplimit.setStatus("current")


class _H3cDot11APL2IsolateEnable_Type(TruthValue):
    """Custom type h3cDot11APL2IsolateEnable based on TruthValue"""


_H3cDot11APL2IsolateEnable_Object = MibScalar
h3cDot11APL2IsolateEnable = _H3cDot11APL2IsolateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 16),
    _H3cDot11APL2IsolateEnable_Type()
)
h3cDot11APL2IsolateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APL2IsolateEnable.setStatus("current")
_H3cDot11APBSSIDSupportNum_Type = Integer32
_H3cDot11APBSSIDSupportNum_Object = MibScalar
h3cDot11APBSSIDSupportNum = _H3cDot11APBSSIDSupportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 17),
    _H3cDot11APBSSIDSupportNum_Type()
)
h3cDot11APBSSIDSupportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APBSSIDSupportNum.setStatus("current")
_H3cDot11APLastUpdateStatTime_Type = DateAndTime
_H3cDot11APLastUpdateStatTime_Object = MibScalar
h3cDot11APLastUpdateStatTime = _H3cDot11APLastUpdateStatTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 18),
    _H3cDot11APLastUpdateStatTime_Type()
)
h3cDot11APLastUpdateStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APLastUpdateStatTime.setStatus("current")


class _H3cDot11APDoSProtectEnable_Type(TruthValue):
    """Custom type h3cDot11APDoSProtectEnable based on TruthValue"""


_H3cDot11APDoSProtectEnable_Object = MibScalar
h3cDot11APDoSProtectEnable = _H3cDot11APDoSProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 19),
    _H3cDot11APDoSProtectEnable_Type()
)
h3cDot11APDoSProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APDoSProtectEnable.setStatus("current")


class _H3cDot11MaxAPPerIf_Type(Unsigned32):
    """Custom type h3cDot11MaxAPPerIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cDot11MaxAPPerIf_Type.__name__ = "Unsigned32"
_H3cDot11MaxAPPerIf_Object = MibScalar
h3cDot11MaxAPPerIf = _H3cDot11MaxAPPerIf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 20),
    _H3cDot11MaxAPPerIf_Type()
)
h3cDot11MaxAPPerIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11MaxAPPerIf.setStatus("current")
_H3cDot11SampleTimeStamp_Type = DateAndTime
_H3cDot11SampleTimeStamp_Object = MibScalar
h3cDot11SampleTimeStamp = _H3cDot11SampleTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 21),
    _H3cDot11SampleTimeStamp_Type()
)
h3cDot11SampleTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11SampleTimeStamp.setStatus("current")


class _H3cDot11UplinkTrackId_Type(Unsigned32):
    """Custom type h3cDot11UplinkTrackId based on Unsigned32"""
    defaultValue = 0


_H3cDot11UplinkTrackId_Object = MibScalar
h3cDot11UplinkTrackId = _H3cDot11UplinkTrackId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 22),
    _H3cDot11UplinkTrackId_Type()
)
h3cDot11UplinkTrackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11UplinkTrackId.setStatus("current")


class _H3cDot11RtCollectSwitch_Type(TruthValue):
    """Custom type h3cDot11RtCollectSwitch based on TruthValue"""


_H3cDot11RtCollectSwitch_Object = MibScalar
h3cDot11RtCollectSwitch = _H3cDot11RtCollectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 23),
    _H3cDot11RtCollectSwitch_Type()
)
h3cDot11RtCollectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RtCollectSwitch.setStatus("current")
_H3cDot11RglCollectIntvl_Type = Integer32
_H3cDot11RglCollectIntvl_Object = MibScalar
h3cDot11RglCollectIntvl = _H3cDot11RglCollectIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 24),
    _H3cDot11RglCollectIntvl_Type()
)
h3cDot11RglCollectIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RglCollectIntvl.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RglCollectIntvl.setUnits("second")
_H3cDot11RtCollectIntvl_Type = Integer32
_H3cDot11RtCollectIntvl_Object = MibScalar
h3cDot11RtCollectIntvl = _H3cDot11RtCollectIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 25),
    _H3cDot11RtCollectIntvl_Type()
)
h3cDot11RtCollectIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RtCollectIntvl.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RtCollectIntvl.setUnits("second")


class _H3cDot11AllAPCpuUsageThreshold_Type(Integer32):
    """Custom type h3cDot11AllAPCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11AllAPCpuUsageThreshold_Type.__name__ = "Integer32"
_H3cDot11AllAPCpuUsageThreshold_Object = MibScalar
h3cDot11AllAPCpuUsageThreshold = _H3cDot11AllAPCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 26),
    _H3cDot11AllAPCpuUsageThreshold_Type()
)
h3cDot11AllAPCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11AllAPCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11AllAPCpuUsageThreshold.setUnits("onepercent")


class _H3cDot11AllAPMemUsageThreshold_Type(Integer32):
    """Custom type h3cDot11AllAPMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11AllAPMemUsageThreshold_Type.__name__ = "Integer32"
_H3cDot11AllAPMemUsageThreshold_Object = MibScalar
h3cDot11AllAPMemUsageThreshold = _H3cDot11AllAPMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 27),
    _H3cDot11AllAPMemUsageThreshold_Type()
)
h3cDot11AllAPMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11AllAPMemUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11AllAPMemUsageThreshold.setUnits("onepercent")
_H3cDot11AdjIntfTrapThreshold_Type = Integer32
_H3cDot11AdjIntfTrapThreshold_Object = MibScalar
h3cDot11AdjIntfTrapThreshold = _H3cDot11AdjIntfTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 1, 28),
    _H3cDot11AdjIntfTrapThreshold_Type()
)
h3cDot11AdjIntfTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11AdjIntfTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11AdjIntfTrapThreshold.setUnits("dbm")
_H3cDot11PolicyConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11PolicyConfigGroup = _H3cDot11PolicyConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2)
)
_H3cDot11RadioPolicyTable_Object = MibTable
h3cDot11RadioPolicyTable = _H3cDot11RadioPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDot11RadioPolicyTable.setStatus("current")
_H3cDot11RadioPolicyEntry_Object = MibTableRow
h3cDot11RadioPolicyEntry = _H3cDot11RadioPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1)
)
h3cDot11RadioPolicyEntry.setIndexNames(
    (1, "H3C-DOT11-CFG-MIB", "h3cDot11RadioPolicyName"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioPolicyEntry.setStatus("current")


class _H3cDot11RadioPolicyName_Type(OctetString):
    """Custom type h3cDot11RadioPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11RadioPolicyName_Type.__name__ = "OctetString"
_H3cDot11RadioPolicyName_Object = MibTableColumn
h3cDot11RadioPolicyName = _H3cDot11RadioPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1, 1),
    _H3cDot11RadioPolicyName_Type()
)
h3cDot11RadioPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RadioPolicyName.setStatus("current")


class _H3cDot11BeaconInterval_Type(Integer32):
    """Custom type h3cDot11BeaconInterval based on Integer32"""
    defaultValue = 100


_H3cDot11BeaconInterval_Object = MibTableColumn
h3cDot11BeaconInterval = _H3cDot11BeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1, 2),
    _H3cDot11BeaconInterval_Type()
)
h3cDot11BeaconInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11BeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11BeaconInterval.setUnits("TU")


class _H3cDot11DtimInterval_Type(Integer32):
    """Custom type h3cDot11DtimInterval based on Integer32"""
    defaultValue = 1


_H3cDot11DtimInterval_Object = MibTableColumn
h3cDot11DtimInterval = _H3cDot11DtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1, 3),
    _H3cDot11DtimInterval_Type()
)
h3cDot11DtimInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11DtimInterval.setStatus("current")


class _H3cDot11RtsThreshold_Type(Integer32):
    """Custom type h3cDot11RtsThreshold based on Integer32"""
    defaultValue = 2346


_H3cDot11RtsThreshold_Object = MibTableColumn
h3cDot11RtsThreshold = _H3cDot11RtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1, 4),
    _H3cDot11RtsThreshold_Type()
)
h3cDot11RtsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11RtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RtsThreshold.setUnits("byte")


class _H3cDot11FragThreshold_Type(Integer32):
    """Custom type h3cDot11FragThreshold based on Integer32"""
    defaultValue = 2346


_H3cDot11FragThreshold_Object = MibTableColumn
h3cDot11FragThreshold = _H3cDot11FragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1, 5),
    _H3cDot11FragThreshold_Type()
)
h3cDot11FragThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11FragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11FragThreshold.setUnits("byte")


class _H3cDot11ShortRetryThreshold_Type(Integer32):
    """Custom type h3cDot11ShortRetryThreshold based on Integer32"""
    defaultValue = 7


_H3cDot11ShortRetryThreshold_Object = MibTableColumn
h3cDot11ShortRetryThreshold = _H3cDot11ShortRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1, 6),
    _H3cDot11ShortRetryThreshold_Type()
)
h3cDot11ShortRetryThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11ShortRetryThreshold.setStatus("current")


class _H3cDot11LongRetryThreshold_Type(Integer32):
    """Custom type h3cDot11LongRetryThreshold based on Integer32"""
    defaultValue = 4


_H3cDot11LongRetryThreshold_Object = MibTableColumn
h3cDot11LongRetryThreshold = _H3cDot11LongRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1, 7),
    _H3cDot11LongRetryThreshold_Type()
)
h3cDot11LongRetryThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11LongRetryThreshold.setStatus("current")


class _H3cDot11MaxRxLifetime_Type(Unsigned32):
    """Custom type h3cDot11MaxRxLifetime based on Unsigned32"""
    defaultValue = 2000


_H3cDot11MaxRxLifetime_Object = MibTableColumn
h3cDot11MaxRxLifetime = _H3cDot11MaxRxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1, 8),
    _H3cDot11MaxRxLifetime_Type()
)
h3cDot11MaxRxLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11MaxRxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11MaxRxLifetime.setUnits("millisecond")
_H3cDot11RdoPolicyRowStatus_Type = RowStatus
_H3cDot11RdoPolicyRowStatus_Object = MibTableColumn
h3cDot11RdoPolicyRowStatus = _H3cDot11RdoPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1, 9),
    _H3cDot11RdoPolicyRowStatus_Type()
)
h3cDot11RdoPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11RdoPolicyRowStatus.setStatus("current")


class _H3cDot11RdoClientMaxCount_Type(Integer32):
    """Custom type h3cDot11RdoClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cDot11RdoClientMaxCount_Type.__name__ = "Integer32"
_H3cDot11RdoClientMaxCount_Object = MibTableColumn
h3cDot11RdoClientMaxCount = _H3cDot11RdoClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1, 10),
    _H3cDot11RdoClientMaxCount_Type()
)
h3cDot11RdoClientMaxCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11RdoClientMaxCount.setStatus("current")
_H3cDot11BeaconIntervalMs_Type = Integer32
_H3cDot11BeaconIntervalMs_Object = MibTableColumn
h3cDot11BeaconIntervalMs = _H3cDot11BeaconIntervalMs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 1, 1, 11),
    _H3cDot11BeaconIntervalMs_Type()
)
h3cDot11BeaconIntervalMs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11BeaconIntervalMs.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11BeaconIntervalMs.setUnits("ms")
_H3cDot11ServicePolicyTable_Object = MibTable
h3cDot11ServicePolicyTable = _H3cDot11ServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDot11ServicePolicyTable.setStatus("current")
_H3cDot11ServicePolicyEntry_Object = MibTableRow
h3cDot11ServicePolicyEntry = _H3cDot11ServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1)
)
h3cDot11ServicePolicyEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11ServicePolicyID"),
)
if mibBuilder.loadTexts:
    h3cDot11ServicePolicyEntry.setStatus("current")
_H3cDot11ServicePolicyID_Type = H3cDot11ServicePolicyIDType
_H3cDot11ServicePolicyID_Object = MibTableColumn
h3cDot11ServicePolicyID = _H3cDot11ServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 1),
    _H3cDot11ServicePolicyID_Type()
)
h3cDot11ServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11ServicePolicyID.setStatus("current")
_H3cDot11SSIDName_Type = H3cDot11SSIDStringType
_H3cDot11SSIDName_Object = MibTableColumn
h3cDot11SSIDName = _H3cDot11SSIDName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 2),
    _H3cDot11SSIDName_Type()
)
h3cDot11SSIDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SSIDName.setStatus("current")


class _H3cDot11SSIDHidden_Type(TruthValue):
    """Custom type h3cDot11SSIDHidden based on TruthValue"""


_H3cDot11SSIDHidden_Object = MibTableColumn
h3cDot11SSIDHidden = _H3cDot11SSIDHidden_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 3),
    _H3cDot11SSIDHidden_Type()
)
h3cDot11SSIDHidden.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SSIDHidden.setStatus("current")
_H3cDot11AuthenMode_Type = H3cDot11AuthenType
_H3cDot11AuthenMode_Object = MibTableColumn
h3cDot11AuthenMode = _H3cDot11AuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 4),
    _H3cDot11AuthenMode_Type()
)
h3cDot11AuthenMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11AuthenMode.setStatus("current")
_H3cDot11SSIDEncryptionMode_Type = H3cDot11SSIDEncryptModeType
_H3cDot11SSIDEncryptionMode_Object = MibTableColumn
h3cDot11SSIDEncryptionMode = _H3cDot11SSIDEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 5),
    _H3cDot11SSIDEncryptionMode_Type()
)
h3cDot11SSIDEncryptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SSIDEncryptionMode.setStatus("current")


class _H3cDot11WlanInfBindingType_Type(OctetString):
    """Custom type h3cDot11WlanInfBindingType based on OctetString"""
    defaultValue = OctetString("WLAN-ESS")


_H3cDot11WlanInfBindingType_Object = MibTableColumn
h3cDot11WlanInfBindingType = _H3cDot11WlanInfBindingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 6),
    _H3cDot11WlanInfBindingType_Type()
)
h3cDot11WlanInfBindingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11WlanInfBindingType.setStatus("current")
_H3cDot11WlanInfBindingID_Type = Integer32
_H3cDot11WlanInfBindingID_Object = MibTableColumn
h3cDot11WlanInfBindingID = _H3cDot11WlanInfBindingID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 7),
    _H3cDot11WlanInfBindingID_Type()
)
h3cDot11WlanInfBindingID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11WlanInfBindingID.setStatus("current")
_H3cDot11SrvPolicyRowStatus_Type = RowStatus
_H3cDot11SrvPolicyRowStatus_Object = MibTableColumn
h3cDot11SrvPolicyRowStatus = _H3cDot11SrvPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 8),
    _H3cDot11SrvPolicyRowStatus_Type()
)
h3cDot11SrvPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SrvPolicyRowStatus.setStatus("current")


class _H3cDot11ClientMaxCount_Type(Integer32):
    """Custom type h3cDot11ClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cDot11ClientMaxCount_Type.__name__ = "Integer32"
_H3cDot11ClientMaxCount_Object = MibTableColumn
h3cDot11ClientMaxCount = _H3cDot11ClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 9),
    _H3cDot11ClientMaxCount_Type()
)
h3cDot11ClientMaxCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11ClientMaxCount.setStatus("current")


class _H3cDot11SPInCirMode_Type(H3cDot11CirMode):
    """Custom type h3cDot11SPInCirMode based on H3cDot11CirMode"""


_H3cDot11SPInCirMode_Object = MibTableColumn
h3cDot11SPInCirMode = _H3cDot11SPInCirMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 10),
    _H3cDot11SPInCirMode_Type()
)
h3cDot11SPInCirMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SPInCirMode.setStatus("current")


class _H3cDot11SPInCirValue_Type(Integer32):
    """Custom type h3cDot11SPInCirValue based on Integer32"""
    defaultValue = 0


_H3cDot11SPInCirValue_Object = MibTableColumn
h3cDot11SPInCirValue = _H3cDot11SPInCirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 11),
    _H3cDot11SPInCirValue_Type()
)
h3cDot11SPInCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SPInCirValue.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11SPInCirValue.setUnits("Kbps")


class _H3cDot11SPOutCirMode_Type(H3cDot11CirMode):
    """Custom type h3cDot11SPOutCirMode based on H3cDot11CirMode"""


_H3cDot11SPOutCirMode_Object = MibTableColumn
h3cDot11SPOutCirMode = _H3cDot11SPOutCirMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 12),
    _H3cDot11SPOutCirMode_Type()
)
h3cDot11SPOutCirMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SPOutCirMode.setStatus("current")


class _H3cDot11SPOutCirValue_Type(Integer32):
    """Custom type h3cDot11SPOutCirValue based on Integer32"""
    defaultValue = 0


_H3cDot11SPOutCirValue_Object = MibTableColumn
h3cDot11SPOutCirValue = _H3cDot11SPOutCirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 13),
    _H3cDot11SPOutCirValue_Type()
)
h3cDot11SPOutCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SPOutCirValue.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11SPOutCirValue.setUnits("Kbps")


class _H3cDot11WlanInfPVID_Type(Integer32):
    """Custom type h3cDot11WlanInfPVID based on Integer32"""
    defaultValue = 1


_H3cDot11WlanInfPVID_Object = MibTableColumn
h3cDot11WlanInfPVID = _H3cDot11WlanInfPVID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 14),
    _H3cDot11WlanInfPVID_Type()
)
h3cDot11WlanInfPVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11WlanInfPVID.setStatus("current")


class _H3cDot11SPInCirStaticValue_Type(Integer32):
    """Custom type h3cDot11SPInCirStaticValue based on Integer32"""
    defaultValue = 0


_H3cDot11SPInCirStaticValue_Object = MibTableColumn
h3cDot11SPInCirStaticValue = _H3cDot11SPInCirStaticValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 15),
    _H3cDot11SPInCirStaticValue_Type()
)
h3cDot11SPInCirStaticValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SPInCirStaticValue.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11SPInCirStaticValue.setUnits("Kbps")


class _H3cDot11SPOutCirStaticValue_Type(Integer32):
    """Custom type h3cDot11SPOutCirStaticValue based on Integer32"""
    defaultValue = 0


_H3cDot11SPOutCirStaticValue_Object = MibTableColumn
h3cDot11SPOutCirStaticValue = _H3cDot11SPOutCirStaticValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 16),
    _H3cDot11SPOutCirStaticValue_Type()
)
h3cDot11SPOutCirStaticValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SPOutCirStaticValue.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11SPOutCirStaticValue.setUnits("Kbps")


class _H3cDot11SPIsolate_Type(TruthValue):
    """Custom type h3cDot11SPIsolate based on TruthValue"""


_H3cDot11SPIsolate_Object = MibTableColumn
h3cDot11SPIsolate = _H3cDot11SPIsolate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 2, 1, 17),
    _H3cDot11SPIsolate_Type()
)
h3cDot11SPIsolate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SPIsolate.setStatus("current")
_H3cDot11ServicePolicyExtTable_Object = MibTable
h3cDot11ServicePolicyExtTable = _H3cDot11ServicePolicyExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDot11ServicePolicyExtTable.setStatus("current")
_H3cDot11ServicePolicyExtEntry_Object = MibTableRow
h3cDot11ServicePolicyExtEntry = _H3cDot11ServicePolicyExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 3, 1)
)
h3cDot11ServicePolicyExtEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11ServicePolicyExtID"),
)
if mibBuilder.loadTexts:
    h3cDot11ServicePolicyExtEntry.setStatus("current")
_H3cDot11ServicePolicyExtID_Type = H3cDot11ServicePolicyIDType
_H3cDot11ServicePolicyExtID_Object = MibTableColumn
h3cDot11ServicePolicyExtID = _H3cDot11ServicePolicyExtID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 3, 1, 1),
    _H3cDot11ServicePolicyExtID_Type()
)
h3cDot11ServicePolicyExtID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11ServicePolicyExtID.setStatus("current")
_H3cDot11SecIEStatus_Type = H3cDot11SecIEStatusType
_H3cDot11SecIEStatus_Object = MibTableColumn
h3cDot11SecIEStatus = _H3cDot11SecIEStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 3, 1, 2),
    _H3cDot11SecIEStatus_Type()
)
h3cDot11SecIEStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SecIEStatus.setStatus("current")
_H3cDot11SecurityCiphers_Type = Integer32
_H3cDot11SecurityCiphers_Object = MibTableColumn
h3cDot11SecurityCiphers = _H3cDot11SecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 3, 1, 3),
    _H3cDot11SecurityCiphers_Type()
)
h3cDot11SecurityCiphers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SecurityCiphers.setStatus("current")


class _H3cDot11CipherKeyIndex_Type(Integer32):
    """Custom type h3cDot11CipherKeyIndex based on Integer32"""
    defaultValue = 1


_H3cDot11CipherKeyIndex_Object = MibTableColumn
h3cDot11CipherKeyIndex = _H3cDot11CipherKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 3, 1, 4),
    _H3cDot11CipherKeyIndex_Type()
)
h3cDot11CipherKeyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11CipherKeyIndex.setStatus("current")
_H3cDot11CipherKey_Type = OctetString
_H3cDot11CipherKey_Object = MibTableColumn
h3cDot11CipherKey = _H3cDot11CipherKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 3, 1, 5),
    _H3cDot11CipherKey_Type()
)
h3cDot11CipherKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11CipherKey.setStatus("current")
_H3cDot11SrvPolicyExtRowStatus_Type = RowStatus
_H3cDot11SrvPolicyExtRowStatus_Object = MibTableColumn
h3cDot11SrvPolicyExtRowStatus = _H3cDot11SrvPolicyExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 3, 1, 6),
    _H3cDot11SrvPolicyExtRowStatus_Type()
)
h3cDot11SrvPolicyExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SrvPolicyExtRowStatus.setStatus("current")


class _H3cDot11CipherKeyType_Type(Integer32):
    """Custom type h3cDot11CipherKeyType based on Integer32"""
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


_H3cDot11CipherKeyType_Type.__name__ = "Integer32"
_H3cDot11CipherKeyType_Object = MibTableColumn
h3cDot11CipherKeyType = _H3cDot11CipherKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 3, 1, 7),
    _H3cDot11CipherKeyType_Type()
)
h3cDot11CipherKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11CipherKeyType.setStatus("current")
_H3cDot11RadioPolicyExtTable_Object = MibTable
h3cDot11RadioPolicyExtTable = _H3cDot11RadioPolicyExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 4)
)
if mibBuilder.loadTexts:
    h3cDot11RadioPolicyExtTable.setStatus("current")
_H3cDot11RadioPolicyExtEntry_Object = MibTableRow
h3cDot11RadioPolicyExtEntry = _H3cDot11RadioPolicyExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 4, 1)
)
h3cDot11RadioPolicyExtEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RPAPSerialID"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RPRadioID"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioPolicyExtEntry.setStatus("current")


class _H3cDot11RPAPSerialID_Type(OctetString):
    """Custom type h3cDot11RPAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11RPAPSerialID_Type.__name__ = "OctetString"
_H3cDot11RPAPSerialID_Object = MibTableColumn
h3cDot11RPAPSerialID = _H3cDot11RPAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 4, 1, 1),
    _H3cDot11RPAPSerialID_Type()
)
h3cDot11RPAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RPAPSerialID.setStatus("current")
_H3cDot11RPRadioID_Type = H3cDot11RadioScopeType
_H3cDot11RPRadioID_Object = MibTableColumn
h3cDot11RPRadioID = _H3cDot11RPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 4, 1, 2),
    _H3cDot11RPRadioID_Type()
)
h3cDot11RPRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RPRadioID.setStatus("current")


class _H3cDot11RPBeaconInterval_Type(Integer32):
    """Custom type h3cDot11RPBeaconInterval based on Integer32"""
    defaultValue = 100


_H3cDot11RPBeaconInterval_Object = MibTableColumn
h3cDot11RPBeaconInterval = _H3cDot11RPBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 4, 1, 3),
    _H3cDot11RPBeaconInterval_Type()
)
h3cDot11RPBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RPBeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RPBeaconInterval.setUnits("milliseconds")


class _H3cDot11RPDtimInterval_Type(Integer32):
    """Custom type h3cDot11RPDtimInterval based on Integer32"""
    defaultValue = 1


_H3cDot11RPDtimInterval_Object = MibTableColumn
h3cDot11RPDtimInterval = _H3cDot11RPDtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 4, 1, 4),
    _H3cDot11RPDtimInterval_Type()
)
h3cDot11RPDtimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RPDtimInterval.setStatus("current")


class _H3cDot11RPRtsThreshold_Type(Integer32):
    """Custom type h3cDot11RPRtsThreshold based on Integer32"""
    defaultValue = 2346


_H3cDot11RPRtsThreshold_Object = MibTableColumn
h3cDot11RPRtsThreshold = _H3cDot11RPRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 4, 1, 5),
    _H3cDot11RPRtsThreshold_Type()
)
h3cDot11RPRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RPRtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RPRtsThreshold.setUnits("byte")


class _H3cDot11RPFragThreshold_Type(Integer32):
    """Custom type h3cDot11RPFragThreshold based on Integer32"""
    defaultValue = 2346


_H3cDot11RPFragThreshold_Object = MibTableColumn
h3cDot11RPFragThreshold = _H3cDot11RPFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 4, 1, 6),
    _H3cDot11RPFragThreshold_Type()
)
h3cDot11RPFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RPFragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RPFragThreshold.setUnits("byte")


class _H3cDot11RPShortRetryThreshold_Type(Integer32):
    """Custom type h3cDot11RPShortRetryThreshold based on Integer32"""
    defaultValue = 7


_H3cDot11RPShortRetryThreshold_Object = MibTableColumn
h3cDot11RPShortRetryThreshold = _H3cDot11RPShortRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 4, 1, 7),
    _H3cDot11RPShortRetryThreshold_Type()
)
h3cDot11RPShortRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RPShortRetryThreshold.setStatus("current")


class _H3cDot11RPLongRetryThreshold_Type(Integer32):
    """Custom type h3cDot11RPLongRetryThreshold based on Integer32"""
    defaultValue = 4


_H3cDot11RPLongRetryThreshold_Object = MibTableColumn
h3cDot11RPLongRetryThreshold = _H3cDot11RPLongRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 4, 1, 8),
    _H3cDot11RPLongRetryThreshold_Type()
)
h3cDot11RPLongRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RPLongRetryThreshold.setStatus("current")


class _H3cDot11RPClientMaxCount_Type(Integer32):
    """Custom type h3cDot11RPClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cDot11RPClientMaxCount_Type.__name__ = "Integer32"
_H3cDot11RPClientMaxCount_Object = MibTableColumn
h3cDot11RPClientMaxCount = _H3cDot11RPClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 4, 1, 9),
    _H3cDot11RPClientMaxCount_Type()
)
h3cDot11RPClientMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RPClientMaxCount.setStatus("current")
_H3cDot11SrvPortSecurityTable_Object = MibTable
h3cDot11SrvPortSecurityTable = _H3cDot11SrvPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 5)
)
if mibBuilder.loadTexts:
    h3cDot11SrvPortSecurityTable.setStatus("current")
_H3cDot11SrvPortSecurityEntry_Object = MibTableRow
h3cDot11SrvPortSecurityEntry = _H3cDot11SrvPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 5, 1)
)
h3cDot11SrvPortSecurityEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11SecurityServicePolicyID"),
)
if mibBuilder.loadTexts:
    h3cDot11SrvPortSecurityEntry.setStatus("current")
_H3cDot11SecurityServicePolicyID_Type = H3cDot11ServicePolicyIDType
_H3cDot11SecurityServicePolicyID_Object = MibTableColumn
h3cDot11SecurityServicePolicyID = _H3cDot11SecurityServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 5, 1, 1),
    _H3cDot11SecurityServicePolicyID_Type()
)
h3cDot11SecurityServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11SecurityServicePolicyID.setStatus("current")


class _H3cDot11SrvPortSecurityMode_Type(Integer32):
    """Custom type h3cDot11SrvPortSecurityMode based on Integer32"""
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


_H3cDot11SrvPortSecurityMode_Type.__name__ = "Integer32"
_H3cDot11SrvPortSecurityMode_Object = MibTableColumn
h3cDot11SrvPortSecurityMode = _H3cDot11SrvPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 5, 1, 2),
    _H3cDot11SrvPortSecurityMode_Type()
)
h3cDot11SrvPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SrvPortSecurityMode.setStatus("current")


class _H3cDot11SrvSecurityKeyType_Type(Integer32):
    """Custom type h3cDot11SrvSecurityKeyType based on Integer32"""
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


_H3cDot11SrvSecurityKeyType_Type.__name__ = "Integer32"
_H3cDot11SrvSecurityKeyType_Object = MibTableColumn
h3cDot11SrvSecurityKeyType = _H3cDot11SrvSecurityKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 5, 1, 3),
    _H3cDot11SrvSecurityKeyType_Type()
)
h3cDot11SrvSecurityKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SrvSecurityKeyType.setStatus("current")


class _H3cDot11SrvSecurityPskKeyMode_Type(Integer32):
    """Custom type h3cDot11SrvSecurityPskKeyMode based on Integer32"""
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


_H3cDot11SrvSecurityPskKeyMode_Type.__name__ = "Integer32"
_H3cDot11SrvSecurityPskKeyMode_Object = MibTableColumn
h3cDot11SrvSecurityPskKeyMode = _H3cDot11SrvSecurityPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 5, 1, 4),
    _H3cDot11SrvSecurityPskKeyMode_Type()
)
h3cDot11SrvSecurityPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SrvSecurityPskKeyMode.setStatus("current")


class _H3cDot11SrvSecurityPskKeyString_Type(DisplayString):
    """Custom type h3cDot11SrvSecurityPskKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cDot11SrvSecurityPskKeyString_Type.__name__ = "DisplayString"
_H3cDot11SrvSecurityPskKeyString_Object = MibTableColumn
h3cDot11SrvSecurityPskKeyString = _H3cDot11SrvSecurityPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 5, 1, 5),
    _H3cDot11SrvSecurityPskKeyString_Type()
)
h3cDot11SrvSecurityPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SrvSecurityPskKeyString.setStatus("current")
_H3cDot11SrvPolicyExtendTable_Object = MibTable
h3cDot11SrvPolicyExtendTable = _H3cDot11SrvPolicyExtendTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 6)
)
if mibBuilder.loadTexts:
    h3cDot11SrvPolicyExtendTable.setStatus("current")
_H3cDot11SrvPolicyExtendEntry_Object = MibTableRow
h3cDot11SrvPolicyExtendEntry = _H3cDot11SrvPolicyExtendEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 6, 1)
)
h3cDot11SrvPolicyExtendEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11ServicePolicyID"),
)
if mibBuilder.loadTexts:
    h3cDot11SrvPolicyExtendEntry.setStatus("current")


class _H3cDot11SPEnable_Type(Integer32):
    """Custom type h3cDot11SPEnable based on Integer32"""
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


_H3cDot11SPEnable_Type.__name__ = "Integer32"
_H3cDot11SPEnable_Object = MibTableColumn
h3cDot11SPEnable = _H3cDot11SPEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 2, 6, 1, 1),
    _H3cDot11SPEnable_Type()
)
h3cDot11SPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SPEnable.setStatus("current")
_H3cDot11APConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11APConfigGroup = _H3cDot11APConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3)
)
_H3cDot11APTemplateTable_Object = MibTable
h3cDot11APTemplateTable = _H3cDot11APTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1)
)
if mibBuilder.loadTexts:
    h3cDot11APTemplateTable.setStatus("current")
_H3cDot11APTemplateEntry_Object = MibTableRow
h3cDot11APTemplateEntry = _H3cDot11APTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1)
)
h3cDot11APTemplateEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11APTemplateName"),
)
if mibBuilder.loadTexts:
    h3cDot11APTemplateEntry.setStatus("current")


class _H3cDot11APTemplateName_Type(OctetString):
    """Custom type h3cDot11APTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11APTemplateName_Type.__name__ = "OctetString"
_H3cDot11APTemplateName_Object = MibTableColumn
h3cDot11APTemplateName = _H3cDot11APTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 1),
    _H3cDot11APTemplateName_Type()
)
h3cDot11APTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APTemplateName.setStatus("current")
_H3cDot11APSerialID_Type = OctetString
_H3cDot11APSerialID_Object = MibTableColumn
h3cDot11APSerialID = _H3cDot11APSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 2),
    _H3cDot11APSerialID_Type()
)
h3cDot11APSerialID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APSerialID.setStatus("current")
_H3cDot11TemplateAPModelAlias_Type = OctetString
_H3cDot11TemplateAPModelAlias_Object = MibTableColumn
h3cDot11TemplateAPModelAlias = _H3cDot11TemplateAPModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 3),
    _H3cDot11TemplateAPModelAlias_Type()
)
h3cDot11TemplateAPModelAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11TemplateAPModelAlias.setStatus("current")
_H3cDot11Description_Type = OctetString
_H3cDot11Description_Object = MibTableColumn
h3cDot11Description = _H3cDot11Description_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 4),
    _H3cDot11Description_Type()
)
h3cDot11Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11Description.setStatus("current")


class _H3cDot11APWorkMode_Type(Integer32):
    """Custom type h3cDot11APWorkMode based on Integer32"""
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


_H3cDot11APWorkMode_Type.__name__ = "Integer32"
_H3cDot11APWorkMode_Object = MibTableColumn
h3cDot11APWorkMode = _H3cDot11APWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 5),
    _H3cDot11APWorkMode_Type()
)
h3cDot11APWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APWorkMode.setStatus("current")
_H3cDot11APTemplateRowStatus_Type = RowStatus
_H3cDot11APTemplateRowStatus_Object = MibTableColumn
h3cDot11APTemplateRowStatus = _H3cDot11APTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 6),
    _H3cDot11APTemplateRowStatus_Type()
)
h3cDot11APTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APTemplateRowStatus.setStatus("current")
_H3cDot11APName_Type = OctetString
_H3cDot11APName_Object = MibTableColumn
h3cDot11APName = _H3cDot11APName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 7),
    _H3cDot11APName_Type()
)
h3cDot11APName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APName.setStatus("current")
_H3cDot11StatisInterv_Type = Integer32
_H3cDot11StatisInterv_Object = MibTableColumn
h3cDot11StatisInterv = _H3cDot11StatisInterv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 8),
    _H3cDot11StatisInterv_Type()
)
h3cDot11StatisInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11StatisInterv.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StatisInterv.setUnits("second")


class _H3cDot11APBroadcastProbeReply_Type(TruthValue):
    """Custom type h3cDot11APBroadcastProbeReply based on TruthValue"""


_H3cDot11APBroadcastProbeReply_Object = MibTableColumn
h3cDot11APBroadcastProbeReply = _H3cDot11APBroadcastProbeReply_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 9),
    _H3cDot11APBroadcastProbeReply_Type()
)
h3cDot11APBroadcastProbeReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APBroadcastProbeReply.setStatus("current")
_H3cDot11StaIdleTimerInterv_Type = Integer32
_H3cDot11StaIdleTimerInterv_Object = MibTableColumn
h3cDot11StaIdleTimerInterv = _H3cDot11StaIdleTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 10),
    _H3cDot11StaIdleTimerInterv_Type()
)
h3cDot11StaIdleTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11StaIdleTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StaIdleTimerInterv.setUnits("second")
_H3cDot11StaKeepAliveTimerInterv_Type = Integer32
_H3cDot11StaKeepAliveTimerInterv_Object = MibTableColumn
h3cDot11StaKeepAliveTimerInterv = _H3cDot11StaKeepAliveTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 11),
    _H3cDot11StaKeepAliveTimerInterv_Type()
)
h3cDot11StaKeepAliveTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11StaKeepAliveTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11StaKeepAliveTimerInterv.setUnits("second")
_H3cDot11APCir_Type = Integer32
_H3cDot11APCir_Object = MibTableColumn
h3cDot11APCir = _H3cDot11APCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 12),
    _H3cDot11APCir_Type()
)
h3cDot11APCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APCir.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APCir.setUnits("Kbps")
_H3cDot11APCbs_Type = Integer32
_H3cDot11APCbs_Object = MibTableColumn
h3cDot11APCbs = _H3cDot11APCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 13),
    _H3cDot11APCbs_Type()
)
h3cDot11APCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APCbs.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APCbs.setUnits("Bytes")


class _H3cDot11APPriorityLevel_Type(Integer32):
    """Custom type h3cDot11APPriorityLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H3cDot11APPriorityLevel_Type.__name__ = "Integer32"
_H3cDot11APPriorityLevel_Object = MibTableColumn
h3cDot11APPriorityLevel = _H3cDot11APPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 14),
    _H3cDot11APPriorityLevel_Type()
)
h3cDot11APPriorityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APPriorityLevel.setStatus("current")
_H3cDot11APElementID_Type = Integer32
_H3cDot11APElementID_Object = MibTableColumn
h3cDot11APElementID = _H3cDot11APElementID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 15),
    _H3cDot11APElementID_Type()
)
h3cDot11APElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APElementID.setStatus("current")


class _H3cDot11APDevDetectEnable_Type(TruthValue):
    """Custom type h3cDot11APDevDetectEnable based on TruthValue"""


_H3cDot11APDevDetectEnable_Object = MibTableColumn
h3cDot11APDevDetectEnable = _H3cDot11APDevDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 16),
    _H3cDot11APDevDetectEnable_Type()
)
h3cDot11APDevDetectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APDevDetectEnable.setStatus("current")


class _H3cDot11APGetIPMethod_Type(Integer32):
    """Custom type h3cDot11APGetIPMethod based on Integer32"""
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


_H3cDot11APGetIPMethod_Type.__name__ = "Integer32"
_H3cDot11APGetIPMethod_Object = MibTableColumn
h3cDot11APGetIPMethod = _H3cDot11APGetIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 17),
    _H3cDot11APGetIPMethod_Type()
)
h3cDot11APGetIPMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APGetIPMethod.setStatus("current")


class _H3cDot11StatisIntervMode_Type(Integer32):
    """Custom type h3cDot11StatisIntervMode based on Integer32"""
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


_H3cDot11StatisIntervMode_Type.__name__ = "Integer32"
_H3cDot11StatisIntervMode_Object = MibTableColumn
h3cDot11StatisIntervMode = _H3cDot11StatisIntervMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 1, 1, 18),
    _H3cDot11StatisIntervMode_Type()
)
h3cDot11StatisIntervMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11StatisIntervMode.setStatus("current")
_H3cDot11RadioToConfigTable_Object = MibTable
h3cDot11RadioToConfigTable = _H3cDot11RadioToConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2)
)
if mibBuilder.loadTexts:
    h3cDot11RadioToConfigTable.setStatus("current")
_H3cDot11RadioToConfigEntry_Object = MibTableRow
h3cDot11RadioToConfigEntry = _H3cDot11RadioToConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1)
)
h3cDot11RadioToConfigEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11APTemplateNameCfg"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11CfgRadioID"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioToConfigEntry.setStatus("current")


class _H3cDot11APTemplateNameCfg_Type(OctetString):
    """Custom type h3cDot11APTemplateNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11APTemplateNameCfg_Type.__name__ = "OctetString"
_H3cDot11APTemplateNameCfg_Object = MibTableColumn
h3cDot11APTemplateNameCfg = _H3cDot11APTemplateNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 1),
    _H3cDot11APTemplateNameCfg_Type()
)
h3cDot11APTemplateNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APTemplateNameCfg.setStatus("current")
_H3cDot11CfgRadioID_Type = H3cDot11RadioScopeType
_H3cDot11CfgRadioID_Object = MibTableColumn
h3cDot11CfgRadioID = _H3cDot11CfgRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 2),
    _H3cDot11CfgRadioID_Type()
)
h3cDot11CfgRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11CfgRadioID.setStatus("current")
_H3cDot11CfgRadioPolicyName_Type = OctetString
_H3cDot11CfgRadioPolicyName_Object = MibTableColumn
h3cDot11CfgRadioPolicyName = _H3cDot11CfgRadioPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 3),
    _H3cDot11CfgRadioPolicyName_Type()
)
h3cDot11CfgRadioPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11CfgRadioPolicyName.setStatus("current")
_H3cDot11CfgRadioType_Type = H3cDot11RadioType
_H3cDot11CfgRadioType_Object = MibTableColumn
h3cDot11CfgRadioType = _H3cDot11CfgRadioType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 4),
    _H3cDot11CfgRadioType_Type()
)
h3cDot11CfgRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11CfgRadioType.setStatus("current")
_H3cDot11CfgChannel_Type = H3cDot11ChannelScopeType
_H3cDot11CfgChannel_Object = MibTableColumn
h3cDot11CfgChannel = _H3cDot11CfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 5),
    _H3cDot11CfgChannel_Type()
)
h3cDot11CfgChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11CfgChannel.setStatus("current")
_H3cDot11CfgMaxTxPowerLevel_Type = H3cDot11TxPwrLevelScopeType
_H3cDot11CfgMaxTxPowerLevel_Object = MibTableColumn
h3cDot11CfgMaxTxPowerLevel = _H3cDot11CfgMaxTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 6),
    _H3cDot11CfgMaxTxPowerLevel_Type()
)
h3cDot11CfgMaxTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11CfgMaxTxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11CfgMaxTxPowerLevel.setUnits("dbm")


class _H3cDot11PreambleLen_Type(H3cDot11PreambleType):
    """Custom type h3cDot11PreambleLen based on H3cDot11PreambleType"""


_H3cDot11PreambleLen_Object = MibTableColumn
h3cDot11PreambleLen = _H3cDot11PreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 7),
    _H3cDot11PreambleLen_Type()
)
h3cDot11PreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11PreambleLen.setStatus("current")
_H3cDot11CfgRadioStatus_Type = TruthValue
_H3cDot11CfgRadioStatus_Object = MibTableColumn
h3cDot11CfgRadioStatus = _H3cDot11CfgRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 8),
    _H3cDot11CfgRadioStatus_Type()
)
h3cDot11CfgRadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11CfgRadioStatus.setStatus("current")
_H3cDot11CfgRdElementID_Type = Unsigned32
_H3cDot11CfgRdElementID_Object = MibTableColumn
h3cDot11CfgRdElementID = _H3cDot11CfgRdElementID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 9),
    _H3cDot11CfgRdElementID_Type()
)
h3cDot11CfgRdElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CfgRdElementID.setStatus("current")
_H3cDot11CfgWorkMode_Type = H3cDot11WorkMode
_H3cDot11CfgWorkMode_Object = MibTableColumn
h3cDot11CfgWorkMode = _H3cDot11CfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 10),
    _H3cDot11CfgWorkMode_Type()
)
h3cDot11CfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11CfgWorkMode.setStatus("current")
_H3cDot11CfgPwrAttValue_Type = Integer32
_H3cDot11CfgPwrAttValue_Object = MibTableColumn
h3cDot11CfgPwrAttValue = _H3cDot11CfgPwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 11),
    _H3cDot11CfgPwrAttValue_Type()
)
h3cDot11CfgPwrAttValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11CfgPwrAttValue.setStatus("current")


class _H3cDot11RadioTxArithmetic_Type(Integer32):
    """Custom type h3cDot11RadioTxArithmetic based on Integer32"""
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


_H3cDot11RadioTxArithmetic_Type.__name__ = "Integer32"
_H3cDot11RadioTxArithmetic_Object = MibTableColumn
h3cDot11RadioTxArithmetic = _H3cDot11RadioTxArithmetic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 12),
    _H3cDot11RadioTxArithmetic_Type()
)
h3cDot11RadioTxArithmetic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioTxArithmetic.setStatus("current")


class _H3cDot11CfgChannelLockStat_Type(Integer32):
    """Custom type h3cDot11CfgChannelLockStat based on Integer32"""
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


_H3cDot11CfgChannelLockStat_Type.__name__ = "Integer32"
_H3cDot11CfgChannelLockStat_Object = MibTableColumn
h3cDot11CfgChannelLockStat = _H3cDot11CfgChannelLockStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 13),
    _H3cDot11CfgChannelLockStat_Type()
)
h3cDot11CfgChannelLockStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11CfgChannelLockStat.setStatus("current")


class _H3cDot11CfgPowerLockStat_Type(Integer32):
    """Custom type h3cDot11CfgPowerLockStat based on Integer32"""
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


_H3cDot11CfgPowerLockStat_Type.__name__ = "Integer32"
_H3cDot11CfgPowerLockStat_Object = MibTableColumn
h3cDot11CfgPowerLockStat = _H3cDot11CfgPowerLockStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 14),
    _H3cDot11CfgPowerLockStat_Type()
)
h3cDot11CfgPowerLockStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11CfgPowerLockStat.setStatus("current")
_H3cDot11CfgLBRdGroupId_Type = Unsigned32
_H3cDot11CfgLBRdGroupId_Object = MibTableColumn
h3cDot11CfgLBRdGroupId = _H3cDot11CfgLBRdGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 15),
    _H3cDot11CfgLBRdGroupId_Type()
)
h3cDot11CfgLBRdGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11CfgLBRdGroupId.setStatus("current")
_H3cDot11CfgRRMSDRdGroupId_Type = Unsigned32
_H3cDot11CfgRRMSDRdGroupId_Object = MibTableColumn
h3cDot11CfgRRMSDRdGroupId = _H3cDot11CfgRRMSDRdGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 2, 1, 16),
    _H3cDot11CfgRRMSDRdGroupId_Type()
)
h3cDot11CfgRRMSDRdGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11CfgRRMSDRdGroupId.setStatus("current")
_H3cDot11APServiceSetTable_Object = MibTable
h3cDot11APServiceSetTable = _H3cDot11APServiceSetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 3)
)
if mibBuilder.loadTexts:
    h3cDot11APServiceSetTable.setStatus("current")
_H3cDot11APServiceSetEntry_Object = MibTableRow
h3cDot11APServiceSetEntry = _H3cDot11APServiceSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 3, 1)
)
h3cDot11APServiceSetEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11APTemplateNameCfg"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11CfgRadioID"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11CfgServicePolicyID"),
)
if mibBuilder.loadTexts:
    h3cDot11APServiceSetEntry.setStatus("current")
_H3cDot11CfgServicePolicyID_Type = H3cDot11ServicePolicyIDType
_H3cDot11CfgServicePolicyID_Object = MibTableColumn
h3cDot11CfgServicePolicyID = _H3cDot11CfgServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 3, 1, 1),
    _H3cDot11CfgServicePolicyID_Type()
)
h3cDot11CfgServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11CfgServicePolicyID.setStatus("current")
_H3cDot11SrvSetRowStatus_Type = RowStatus
_H3cDot11SrvSetRowStatus_Object = MibTableColumn
h3cDot11SrvSetRowStatus = _H3cDot11SrvSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 3, 1, 2),
    _H3cDot11SrvSetRowStatus_Type()
)
h3cDot11SrvSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11SrvSetRowStatus.setStatus("current")


class _H3cDot11ServiceSetVlanId_Type(Integer32):
    """Custom type h3cDot11ServiceSetVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_H3cDot11ServiceSetVlanId_Type.__name__ = "Integer32"
_H3cDot11ServiceSetVlanId_Object = MibTableColumn
h3cDot11ServiceSetVlanId = _H3cDot11ServiceSetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 3, 1, 3),
    _H3cDot11ServiceSetVlanId_Type()
)
h3cDot11ServiceSetVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11ServiceSetVlanId.setStatus("current")
_H3cDot11APSysInfoSetTable_Object = MibTable
h3cDot11APSysInfoSetTable = _H3cDot11APSysInfoSetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 4)
)
if mibBuilder.loadTexts:
    h3cDot11APSysInfoSetTable.setStatus("current")
_H3cDot11APSysInfoSetEntry_Object = MibTableRow
h3cDot11APSysInfoSetEntry = _H3cDot11APSysInfoSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 4, 1)
)
h3cDot11APSysInfoSetEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11SIDAPSerialID"),
)
if mibBuilder.loadTexts:
    h3cDot11APSysInfoSetEntry.setStatus("current")


class _H3cDot11APSysNetID_Type(OctetString):
    """Custom type h3cDot11APSysNetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11APSysNetID_Type.__name__ = "OctetString"
_H3cDot11APSysNetID_Object = MibTableColumn
h3cDot11APSysNetID = _H3cDot11APSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 4, 1, 1),
    _H3cDot11APSysNetID_Type()
)
h3cDot11APSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APSysNetID.setStatus("current")


class _H3cDot11APCpuUsageThreshold_Type(Integer32):
    """Custom type h3cDot11APCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11APCpuUsageThreshold_Type.__name__ = "Integer32"
_H3cDot11APCpuUsageThreshold_Object = MibTableColumn
h3cDot11APCpuUsageThreshold = _H3cDot11APCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 4, 1, 2),
    _H3cDot11APCpuUsageThreshold_Type()
)
h3cDot11APCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APCpuUsageThreshold.setUnits("onepercent")


class _H3cDot11APMemUsageThreshold_Type(Integer32):
    """Custom type h3cDot11APMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cDot11APMemUsageThreshold_Type.__name__ = "Integer32"
_H3cDot11APMemUsageThreshold_Object = MibTableColumn
h3cDot11APMemUsageThreshold = _H3cDot11APMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 4, 1, 3),
    _H3cDot11APMemUsageThreshold_Type()
)
h3cDot11APMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APMemUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11APMemUsageThreshold.setUnits("onepercent")
_H3cDot11APLimitTable_Object = MibTable
h3cDot11APLimitTable = _H3cDot11APLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 5)
)
if mibBuilder.loadTexts:
    h3cDot11APLimitTable.setStatus("current")
_H3cDot11APLimitEntry_Object = MibTableRow
h3cDot11APLimitEntry = _H3cDot11APLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 5, 1)
)
h3cDot11APLimitEntry.setIndexNames(
    (0, "H3C-DOT11-REF-MIB", "h3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11APLimitEntry.setStatus("current")


class _H3cDot11APSsidNumLimit_Type(Integer32):
    """Custom type h3cDot11APSsidNumLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cDot11APSsidNumLimit_Type.__name__ = "Integer32"
_H3cDot11APSsidNumLimit_Object = MibTableColumn
h3cDot11APSsidNumLimit = _H3cDot11APSsidNumLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 5, 1, 1),
    _H3cDot11APSsidNumLimit_Type()
)
h3cDot11APSsidNumLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APSsidNumLimit.setStatus("current")


class _H3cDot11APUserCntLimit_Type(Integer32):
    """Custom type h3cDot11APUserCntLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cDot11APUserCntLimit_Type.__name__ = "Integer32"
_H3cDot11APUserCntLimit_Object = MibTableColumn
h3cDot11APUserCntLimit = _H3cDot11APUserCntLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 5, 1, 2),
    _H3cDot11APUserCntLimit_Type()
)
h3cDot11APUserCntLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APUserCntLimit.setStatus("current")


class _H3cDot11APUserThreshold_Type(Integer32):
    """Custom type h3cDot11APUserThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cDot11APUserThreshold_Type.__name__ = "Integer32"
_H3cDot11APUserThreshold_Object = MibTableColumn
h3cDot11APUserThreshold = _H3cDot11APUserThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 5, 1, 3),
    _H3cDot11APUserThreshold_Type()
)
h3cDot11APUserThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APUserThreshold.setStatus("current")
_H3cDot11APIfSetTable_Object = MibTable
h3cDot11APIfSetTable = _H3cDot11APIfSetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 6)
)
if mibBuilder.loadTexts:
    h3cDot11APIfSetTable.setStatus("current")
_H3cDot11APIfSetEntry_Object = MibTableRow
h3cDot11APIfSetEntry = _H3cDot11APIfSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 6, 1)
)
h3cDot11APIfSetEntry.setIndexNames(
    (0, "H3C-DOT11-REF-MIB", "h3cDot11APElementIndex"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11APSetIfIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11APIfSetEntry.setStatus("current")
_H3cDot11APSetIfIndex_Type = Integer32
_H3cDot11APSetIfIndex_Object = MibTableColumn
h3cDot11APSetIfIndex = _H3cDot11APSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 6, 1, 1),
    _H3cDot11APSetIfIndex_Type()
)
h3cDot11APSetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APSetIfIndex.setStatus("current")
_H3cDot11APIfAlias_Type = DisplayString
_H3cDot11APIfAlias_Object = MibTableColumn
h3cDot11APIfAlias = _H3cDot11APIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 6, 1, 2),
    _H3cDot11APIfAlias_Type()
)
h3cDot11APIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11APIfAlias.setStatus("current")
_H3cDot11APServiceVlanTable_Object = MibTable
h3cDot11APServiceVlanTable = _H3cDot11APServiceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 7)
)
if mibBuilder.loadTexts:
    h3cDot11APServiceVlanTable.setStatus("current")
_H3cDot11APServiceVlanEntry_Object = MibTableRow
h3cDot11APServiceVlanEntry = _H3cDot11APServiceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 7, 1)
)
h3cDot11APServiceVlanEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11APServiceVlanSerialID"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11APServiceVlanSPID"),
)
if mibBuilder.loadTexts:
    h3cDot11APServiceVlanEntry.setStatus("current")
_H3cDot11APServiceVlanSerialID_Type = OctetString
_H3cDot11APServiceVlanSerialID_Object = MibTableColumn
h3cDot11APServiceVlanSerialID = _H3cDot11APServiceVlanSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 7, 1, 1),
    _H3cDot11APServiceVlanSerialID_Type()
)
h3cDot11APServiceVlanSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APServiceVlanSerialID.setStatus("current")
_H3cDot11APServiceVlanSPID_Type = H3cDot11ServicePolicyIDType
_H3cDot11APServiceVlanSPID_Object = MibTableColumn
h3cDot11APServiceVlanSPID = _H3cDot11APServiceVlanSPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 7, 1, 2),
    _H3cDot11APServiceVlanSPID_Type()
)
h3cDot11APServiceVlanSPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APServiceVlanSPID.setStatus("current")


class _H3cDot11APServiceVlanId_Type(Integer32):
    """Custom type h3cDot11APServiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_H3cDot11APServiceVlanId_Type.__name__ = "Integer32"
_H3cDot11APServiceVlanId_Object = MibTableColumn
h3cDot11APServiceVlanId = _H3cDot11APServiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 7, 1, 3),
    _H3cDot11APServiceVlanId_Type()
)
h3cDot11APServiceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APServiceVlanId.setStatus("current")
_H3cDot11APServiceVlanRowStatus_Type = RowStatus
_H3cDot11APServiceVlanRowStatus_Object = MibTableColumn
h3cDot11APServiceVlanRowStatus = _H3cDot11APServiceVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 7, 1, 4),
    _H3cDot11APServiceVlanRowStatus_Type()
)
h3cDot11APServiceVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11APServiceVlanRowStatus.setStatus("current")
_H3cDot11RadioConfigTable_Object = MibTable
h3cDot11RadioConfigTable = _H3cDot11RadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8)
)
if mibBuilder.loadTexts:
    h3cDot11RadioConfigTable.setStatus("current")
_H3cDot11RadioConfigEntry_Object = MibTableRow
h3cDot11RadioConfigEntry = _H3cDot11RadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8, 1)
)
h3cDot11RadioConfigEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RCAPSerialID"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RCRadioID"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioConfigEntry.setStatus("current")


class _H3cDot11RCAPSerialID_Type(OctetString):
    """Custom type h3cDot11RCAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cDot11RCAPSerialID_Type.__name__ = "OctetString"
_H3cDot11RCAPSerialID_Object = MibTableColumn
h3cDot11RCAPSerialID = _H3cDot11RCAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8, 1, 1),
    _H3cDot11RCAPSerialID_Type()
)
h3cDot11RCAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RCAPSerialID.setStatus("current")
_H3cDot11RCRadioID_Type = H3cDot11RadioScopeType
_H3cDot11RCRadioID_Object = MibTableColumn
h3cDot11RCRadioID = _H3cDot11RCRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8, 1, 2),
    _H3cDot11RCRadioID_Type()
)
h3cDot11RCRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RCRadioID.setStatus("current")
_H3cDot11RCRadioType_Type = H3cDot11RadioType
_H3cDot11RCRadioType_Object = MibTableColumn
h3cDot11RCRadioType = _H3cDot11RCRadioType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8, 1, 3),
    _H3cDot11RCRadioType_Type()
)
h3cDot11RCRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RCRadioType.setStatus("current")
_H3cDot11RCChannel_Type = H3cDot11ChannelScopeType
_H3cDot11RCChannel_Object = MibTableColumn
h3cDot11RCChannel = _H3cDot11RCChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8, 1, 4),
    _H3cDot11RCChannel_Type()
)
h3cDot11RCChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RCChannel.setStatus("current")


class _H3cDot11RCPreambleLen_Type(H3cDot11PreambleType):
    """Custom type h3cDot11RCPreambleLen based on H3cDot11PreambleType"""


_H3cDot11RCPreambleLen_Object = MibTableColumn
h3cDot11RCPreambleLen = _H3cDot11RCPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8, 1, 5),
    _H3cDot11RCPreambleLen_Type()
)
h3cDot11RCPreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RCPreambleLen.setStatus("current")
_H3cDot11RCPwrAttValue_Type = Integer32
_H3cDot11RCPwrAttValue_Object = MibTableColumn
h3cDot11RCPwrAttValue = _H3cDot11RCPwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8, 1, 6),
    _H3cDot11RCPwrAttValue_Type()
)
h3cDot11RCPwrAttValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RCPwrAttValue.setStatus("current")
_H3cDot11RCApPowerLevel_Type = H3cDot11TxPwrLevelScopeType
_H3cDot11RCApPowerLevel_Object = MibTableColumn
h3cDot11RCApPowerLevel = _H3cDot11RCApPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8, 1, 7),
    _H3cDot11RCApPowerLevel_Type()
)
h3cDot11RCApPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RCApPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RCApPowerLevel.setUnits("dbm")
_H3cDot11RCDynamicChlState_Type = TruthValue
_H3cDot11RCDynamicChlState_Object = MibTableColumn
h3cDot11RCDynamicChlState = _H3cDot11RCDynamicChlState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8, 1, 8),
    _H3cDot11RCDynamicChlState_Type()
)
h3cDot11RCDynamicChlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RCDynamicChlState.setStatus("current")
_H3cDot11RCDynamicPowerState_Type = TruthValue
_H3cDot11RCDynamicPowerState_Object = MibTableColumn
h3cDot11RCDynamicPowerState = _H3cDot11RCDynamicPowerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8, 1, 9),
    _H3cDot11RCDynamicPowerState_Type()
)
h3cDot11RCDynamicPowerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RCDynamicPowerState.setStatus("current")
_H3cDot11RCRadioStatus_Type = TruthValue
_H3cDot11RCRadioStatus_Object = MibTableColumn
h3cDot11RCRadioStatus = _H3cDot11RCRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 8, 1, 10),
    _H3cDot11RCRadioStatus_Type()
)
h3cDot11RCRadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RCRadioStatus.setStatus("current")
_H3cDot11RadioSSIDCfgTable_Object = MibTable
h3cDot11RadioSSIDCfgTable = _H3cDot11RadioSSIDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 9)
)
if mibBuilder.loadTexts:
    h3cDot11RadioSSIDCfgTable.setStatus("current")
_H3cDot11RadioSSIDCfgEntry_Object = MibTableRow
h3cDot11RadioSSIDCfgEntry = _H3cDot11RadioSSIDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 9, 1)
)
h3cDot11RadioSSIDCfgEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RadioSSIDSerialID"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RadioSSIDRadioID"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RadioSSIDWLANID"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioSSIDCfgEntry.setStatus("current")
_H3cDot11RadioSSIDSerialID_Type = H3cDot11ObjectIDType
_H3cDot11RadioSSIDSerialID_Object = MibTableColumn
h3cDot11RadioSSIDSerialID = _H3cDot11RadioSSIDSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 9, 1, 1),
    _H3cDot11RadioSSIDSerialID_Type()
)
h3cDot11RadioSSIDSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RadioSSIDSerialID.setStatus("current")
_H3cDot11RadioSSIDRadioID_Type = H3cDot11RadioScopeType
_H3cDot11RadioSSIDRadioID_Object = MibTableColumn
h3cDot11RadioSSIDRadioID = _H3cDot11RadioSSIDRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 9, 1, 2),
    _H3cDot11RadioSSIDRadioID_Type()
)
h3cDot11RadioSSIDRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RadioSSIDRadioID.setStatus("current")
_H3cDot11RadioSSIDWLANID_Type = Integer32
_H3cDot11RadioSSIDWLANID_Object = MibTableColumn
h3cDot11RadioSSIDWLANID = _H3cDot11RadioSSIDWLANID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 9, 1, 3),
    _H3cDot11RadioSSIDWLANID_Type()
)
h3cDot11RadioSSIDWLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RadioSSIDWLANID.setStatus("current")
_H3cDot11RadioSSIDIndex_Type = H3cDot11ServicePolicyIDType
_H3cDot11RadioSSIDIndex_Object = MibTableColumn
h3cDot11RadioSSIDIndex = _H3cDot11RadioSSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 9, 1, 4),
    _H3cDot11RadioSSIDIndex_Type()
)
h3cDot11RadioSSIDIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11RadioSSIDIndex.setStatus("current")
_H3cDot11RadioBSSID_Type = MacAddress
_H3cDot11RadioBSSID_Object = MibTableColumn
h3cDot11RadioBSSID = _H3cDot11RadioBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 9, 1, 5),
    _H3cDot11RadioBSSID_Type()
)
h3cDot11RadioBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioBSSID.setStatus("current")
_H3cDot11RadioSSIDRowStatus_Type = RowStatus
_H3cDot11RadioSSIDRowStatus_Object = MibTableColumn
h3cDot11RadioSSIDRowStatus = _H3cDot11RadioSSIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 9, 1, 6),
    _H3cDot11RadioSSIDRowStatus_Type()
)
h3cDot11RadioSSIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11RadioSSIDRowStatus.setStatus("current")
_H3cDot11APSerialIDTable_Object = MibTable
h3cDot11APSerialIDTable = _H3cDot11APSerialIDTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 10)
)
if mibBuilder.loadTexts:
    h3cDot11APSerialIDTable.setStatus("current")
_H3cDot11APSerialIDEntry_Object = MibTableRow
h3cDot11APSerialIDEntry = _H3cDot11APSerialIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 10, 1)
)
h3cDot11APSerialIDEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11SIDAPSerialID"),
)
if mibBuilder.loadTexts:
    h3cDot11APSerialIDEntry.setStatus("current")
_H3cDot11SIDAPSerialID_Type = OctetString
_H3cDot11SIDAPSerialID_Object = MibTableColumn
h3cDot11SIDAPSerialID = _H3cDot11SIDAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 10, 1, 1),
    _H3cDot11SIDAPSerialID_Type()
)
h3cDot11SIDAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11SIDAPSerialID.setStatus("current")


class _H3cDot11SIDAPWorkMode_Type(Integer32):
    """Custom type h3cDot11SIDAPWorkMode based on Integer32"""
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


_H3cDot11SIDAPWorkMode_Type.__name__ = "Integer32"
_H3cDot11SIDAPWorkMode_Object = MibTableColumn
h3cDot11SIDAPWorkMode = _H3cDot11SIDAPWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 10, 1, 2),
    _H3cDot11SIDAPWorkMode_Type()
)
h3cDot11SIDAPWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SIDAPWorkMode.setStatus("current")


class _H3cDot11SIDAPGetIPMethod_Type(Integer32):
    """Custom type h3cDot11SIDAPGetIPMethod based on Integer32"""
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


_H3cDot11SIDAPGetIPMethod_Type.__name__ = "Integer32"
_H3cDot11SIDAPGetIPMethod_Object = MibTableColumn
h3cDot11SIDAPGetIPMethod = _H3cDot11SIDAPGetIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 10, 1, 3),
    _H3cDot11SIDAPGetIPMethod_Type()
)
h3cDot11SIDAPGetIPMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SIDAPGetIPMethod.setStatus("current")
_H3cDot11APSTVlanTable_Object = MibTable
h3cDot11APSTVlanTable = _H3cDot11APSTVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 11)
)
if mibBuilder.loadTexts:
    h3cDot11APSTVlanTable.setStatus("current")
_H3cDot11APSTVlanEntry_Object = MibTableRow
h3cDot11APSTVlanEntry = _H3cDot11APSTVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 11, 1)
)
h3cDot11APSTVlanEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11SIDAPSerialID"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11CfgRadioID"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11CfgServicePolicyID"),
)
if mibBuilder.loadTexts:
    h3cDot11APSTVlanEntry.setStatus("current")


class _H3cDot11CfgSTVLANID_Type(Integer32):
    """Custom type h3cDot11CfgSTVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_H3cDot11CfgSTVLANID_Type.__name__ = "Integer32"
_H3cDot11CfgSTVLANID_Object = MibTableColumn
h3cDot11CfgSTVLANID = _H3cDot11CfgSTVLANID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 11, 1, 1),
    _H3cDot11CfgSTVLANID_Type()
)
h3cDot11CfgSTVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11CfgSTVLANID.setStatus("current")


class _H3cDot11CfgSTNASPortID_Type(Integer32):
    """Custom type h3cDot11CfgSTNASPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_H3cDot11CfgSTNASPortID_Type.__name__ = "Integer32"
_H3cDot11CfgSTNASPortID_Object = MibTableColumn
h3cDot11CfgSTNASPortID = _H3cDot11CfgSTNASPortID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 11, 1, 2),
    _H3cDot11CfgSTNASPortID_Type()
)
h3cDot11CfgSTNASPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11CfgSTNASPortID.setStatus("current")
_H3cDot11CfgServiceSetRowStatus_Type = RowStatus
_H3cDot11CfgServiceSetRowStatus_Object = MibTableColumn
h3cDot11CfgServiceSetRowStatus = _H3cDot11CfgServiceSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 3, 11, 1, 3),
    _H3cDot11CfgServiceSetRowStatus_Type()
)
h3cDot11CfgServiceSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11CfgServiceSetRowStatus.setStatus("current")
_H3cDot11RadioIntfConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11RadioIntfConfigGroup = _H3cDot11RadioIntfConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4)
)
_H3cDot11RadioIntfConfigTable_Object = MibTable
h3cDot11RadioIntfConfigTable = _H3cDot11RadioIntfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1)
)
if mibBuilder.loadTexts:
    h3cDot11RadioIntfConfigTable.setStatus("current")
_H3cDot11RadioIntfConfigEntry_Object = MibTableRow
h3cDot11RadioIntfConfigEntry = _H3cDot11RadioIntfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1)
)
h3cDot11RadioIntfConfigEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RadioIfIdx"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioIntfConfigEntry.setStatus("current")
_H3cDot11RadioIfIdx_Type = Integer32
_H3cDot11RadioIfIdx_Object = MibTableColumn
h3cDot11RadioIfIdx = _H3cDot11RadioIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 1),
    _H3cDot11RadioIfIdx_Type()
)
h3cDot11RadioIfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RadioIfIdx.setStatus("current")


class _H3cDot11RadioCfgBeaconIntvl_Type(Integer32):
    """Custom type h3cDot11RadioCfgBeaconIntvl based on Integer32"""
    defaultValue = 100


_H3cDot11RadioCfgBeaconIntvl_Object = MibTableColumn
h3cDot11RadioCfgBeaconIntvl = _H3cDot11RadioCfgBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 2),
    _H3cDot11RadioCfgBeaconIntvl_Type()
)
h3cDot11RadioCfgBeaconIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgBeaconIntvl.setUnits("TU")


class _H3cDot11RadioCfgDtimIntvl_Type(Integer32):
    """Custom type h3cDot11RadioCfgDtimIntvl based on Integer32"""
    defaultValue = 1


_H3cDot11RadioCfgDtimIntvl_Object = MibTableColumn
h3cDot11RadioCfgDtimIntvl = _H3cDot11RadioCfgDtimIntvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 3),
    _H3cDot11RadioCfgDtimIntvl_Type()
)
h3cDot11RadioCfgDtimIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgDtimIntvl.setStatus("current")


class _H3cDot11RadioCfgRtsThreshold_Type(Integer32):
    """Custom type h3cDot11RadioCfgRtsThreshold based on Integer32"""
    defaultValue = 2346


_H3cDot11RadioCfgRtsThreshold_Object = MibTableColumn
h3cDot11RadioCfgRtsThreshold = _H3cDot11RadioCfgRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 4),
    _H3cDot11RadioCfgRtsThreshold_Type()
)
h3cDot11RadioCfgRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgRtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgRtsThreshold.setUnits("Byte")


class _H3cDot11RadioCfgFragThreshold_Type(Integer32):
    """Custom type h3cDot11RadioCfgFragThreshold based on Integer32"""
    defaultValue = 2346


_H3cDot11RadioCfgFragThreshold_Object = MibTableColumn
h3cDot11RadioCfgFragThreshold = _H3cDot11RadioCfgFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 5),
    _H3cDot11RadioCfgFragThreshold_Type()
)
h3cDot11RadioCfgFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgFragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgFragThreshold.setUnits("Byte")


class _H3cDot11RadioCfgShtRetryThld_Type(Integer32):
    """Custom type h3cDot11RadioCfgShtRetryThld based on Integer32"""
    defaultValue = 5


_H3cDot11RadioCfgShtRetryThld_Object = MibTableColumn
h3cDot11RadioCfgShtRetryThld = _H3cDot11RadioCfgShtRetryThld_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 6),
    _H3cDot11RadioCfgShtRetryThld_Type()
)
h3cDot11RadioCfgShtRetryThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgShtRetryThld.setStatus("current")


class _H3cDot11RadioCfglongRtrThld_Type(Integer32):
    """Custom type h3cDot11RadioCfglongRtrThld based on Integer32"""
    defaultValue = 5


_H3cDot11RadioCfglongRtrThld_Object = MibTableColumn
h3cDot11RadioCfglongRtrThld = _H3cDot11RadioCfglongRtrThld_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 7),
    _H3cDot11RadioCfglongRtrThld_Type()
)
h3cDot11RadioCfglongRtrThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfglongRtrThld.setStatus("current")


class _H3cDot11RadioCfgMaxRxLifetime_Type(Unsigned32):
    """Custom type h3cDot11RadioCfgMaxRxLifetime based on Unsigned32"""
    defaultValue = 2000


_H3cDot11RadioCfgMaxRxLifetime_Object = MibTableColumn
h3cDot11RadioCfgMaxRxLifetime = _H3cDot11RadioCfgMaxRxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 8),
    _H3cDot11RadioCfgMaxRxLifetime_Type()
)
h3cDot11RadioCfgMaxRxLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgMaxRxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgMaxRxLifetime.setUnits("millisecond")
_H3cDot11RadioCfgType_Type = H3cDot11RadioType
_H3cDot11RadioCfgType_Object = MibTableColumn
h3cDot11RadioCfgType = _H3cDot11RadioCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 9),
    _H3cDot11RadioCfgType_Type()
)
h3cDot11RadioCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgType.setStatus("current")


class _H3cDot11RadioCfgChannel_Type(H3cDot11ChannelScopeType):
    """Custom type h3cDot11RadioCfgChannel based on H3cDot11ChannelScopeType"""
    defaultValue = 1


_H3cDot11RadioCfgChannel_Object = MibTableColumn
h3cDot11RadioCfgChannel = _H3cDot11RadioCfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 10),
    _H3cDot11RadioCfgChannel_Type()
)
h3cDot11RadioCfgChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgChannel.setStatus("current")
_H3cDot11RadioCfgMaxTxPwrLvl_Type = H3cDot11TxPwrLevelScopeType
_H3cDot11RadioCfgMaxTxPwrLvl_Object = MibTableColumn
h3cDot11RadioCfgMaxTxPwrLvl = _H3cDot11RadioCfgMaxTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 11),
    _H3cDot11RadioCfgMaxTxPwrLvl_Type()
)
h3cDot11RadioCfgMaxTxPwrLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgMaxTxPwrLvl.setStatus("current")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgMaxTxPwrLvl.setUnits("dbm")


class _H3cDot11RadioCfgPreambleLen_Type(H3cDot11PreambleType):
    """Custom type h3cDot11RadioCfgPreambleLen based on H3cDot11PreambleType"""


_H3cDot11RadioCfgPreambleLen_Object = MibTableColumn
h3cDot11RadioCfgPreambleLen = _H3cDot11RadioCfgPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 12),
    _H3cDot11RadioCfgPreambleLen_Type()
)
h3cDot11RadioCfgPreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgPreambleLen.setStatus("current")
_H3cDot11RadioCfgWorkMode_Type = H3cDot11WorkMode
_H3cDot11RadioCfgWorkMode_Object = MibTableColumn
h3cDot11RadioCfgWorkMode = _H3cDot11RadioCfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 13),
    _H3cDot11RadioCfgWorkMode_Type()
)
h3cDot11RadioCfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgWorkMode.setStatus("current")


class _H3cDot11RadioCfgOnly11gEnable_Type(TruthValue):
    """Custom type h3cDot11RadioCfgOnly11gEnable based on TruthValue"""


_H3cDot11RadioCfgOnly11gEnable_Object = MibTableColumn
h3cDot11RadioCfgOnly11gEnable = _H3cDot11RadioCfgOnly11gEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 1, 1, 14),
    _H3cDot11RadioCfgOnly11gEnable_Type()
)
h3cDot11RadioCfgOnly11gEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioCfgOnly11gEnable.setStatus("current")
_H3cDot11RadioIntfBindTable_Object = MibTable
h3cDot11RadioIntfBindTable = _H3cDot11RadioIntfBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 2)
)
if mibBuilder.loadTexts:
    h3cDot11RadioIntfBindTable.setStatus("current")
_H3cDot11RadioIntfBindEntry_Object = MibTableRow
h3cDot11RadioIntfBindEntry = _H3cDot11RadioIntfBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 2, 1)
)
h3cDot11RadioIntfBindEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RadioIfIdx"),
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RadioIntfBindSvcPlcyID"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioIntfBindEntry.setStatus("current")
_H3cDot11RadioIntfBindSvcPlcyID_Type = H3cDot11ServicePolicyIDType
_H3cDot11RadioIntfBindSvcPlcyID_Object = MibTableColumn
h3cDot11RadioIntfBindSvcPlcyID = _H3cDot11RadioIntfBindSvcPlcyID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 2, 1, 1),
    _H3cDot11RadioIntfBindSvcPlcyID_Type()
)
h3cDot11RadioIntfBindSvcPlcyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RadioIntfBindSvcPlcyID.setStatus("current")
_H3cDot11RadioIntfBindIfIdx_Type = Unsigned32
_H3cDot11RadioIntfBindIfIdx_Object = MibTableColumn
h3cDot11RadioIntfBindIfIdx = _H3cDot11RadioIntfBindIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 2, 1, 2),
    _H3cDot11RadioIntfBindIfIdx_Type()
)
h3cDot11RadioIntfBindIfIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11RadioIntfBindIfIdx.setStatus("current")
_H3cDot11RadioIntfBindRowStatus_Type = RowStatus
_H3cDot11RadioIntfBindRowStatus_Object = MibTableColumn
h3cDot11RadioIntfBindRowStatus = _H3cDot11RadioIntfBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 4, 2, 1, 3),
    _H3cDot11RadioIntfBindRowStatus_Type()
)
h3cDot11RadioIntfBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11RadioIntfBindRowStatus.setStatus("current")
_H3cDot11DataRateConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11DataRateConfigGroup = _H3cDot11DataRateConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 5)
)
_H3cDot11DataRateConfigTable_Object = MibTable
h3cDot11DataRateConfigTable = _H3cDot11DataRateConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 5, 1)
)
if mibBuilder.loadTexts:
    h3cDot11DataRateConfigTable.setStatus("current")
_H3cDot11DataRateConfigEntry_Object = MibTableRow
h3cDot11DataRateConfigEntry = _H3cDot11DataRateConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 5, 1, 1)
)
h3cDot11DataRateConfigEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RadioTypeID"),
)
if mibBuilder.loadTexts:
    h3cDot11DataRateConfigEntry.setStatus("current")
_H3cDot11RadioTypeID_Type = H3cDot11RadioType
_H3cDot11RadioTypeID_Object = MibTableColumn
h3cDot11RadioTypeID = _H3cDot11RadioTypeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 5, 1, 1, 1),
    _H3cDot11RadioTypeID_Type()
)
h3cDot11RadioTypeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RadioTypeID.setStatus("current")


class _H3cDot11SupportedRateSet_Type(OctetString):
    """Custom type h3cDot11SupportedRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDot11SupportedRateSet_Type.__name__ = "OctetString"
_H3cDot11SupportedRateSet_Object = MibTableColumn
h3cDot11SupportedRateSet = _H3cDot11SupportedRateSet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 5, 1, 1, 2),
    _H3cDot11SupportedRateSet_Type()
)
h3cDot11SupportedRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SupportedRateSet.setStatus("current")


class _H3cDot11MandatoryRateSet_Type(OctetString):
    """Custom type h3cDot11MandatoryRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDot11MandatoryRateSet_Type.__name__ = "OctetString"
_H3cDot11MandatoryRateSet_Object = MibTableColumn
h3cDot11MandatoryRateSet = _H3cDot11MandatoryRateSet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 5, 1, 1, 3),
    _H3cDot11MandatoryRateSet_Type()
)
h3cDot11MandatoryRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11MandatoryRateSet.setStatus("current")


class _H3cDot11DisabledRateSet_Type(OctetString):
    """Custom type h3cDot11DisabledRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDot11DisabledRateSet_Type.__name__ = "OctetString"
_H3cDot11DisabledRateSet_Object = MibTableColumn
h3cDot11DisabledRateSet = _H3cDot11DisabledRateSet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 5, 1, 1, 4),
    _H3cDot11DisabledRateSet_Type()
)
h3cDot11DisabledRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11DisabledRateSet.setStatus("current")


class _H3cDot11SmartRateSet_Type(OctetString):
    """Custom type h3cDot11SmartRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cDot11SmartRateSet_Type.__name__ = "OctetString"
_H3cDot11SmartRateSet_Object = MibTableColumn
h3cDot11SmartRateSet = _H3cDot11SmartRateSet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 5, 1, 1, 5),
    _H3cDot11SmartRateSet_Type()
)
h3cDot11SmartRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SmartRateSet.setStatus("current")
_H3cDot11InterfaceConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11InterfaceConfigGroup = _H3cDot11InterfaceConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6)
)
_H3cDot11WlanEssIfTable_Object = MibTable
h3cDot11WlanEssIfTable = _H3cDot11WlanEssIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 1)
)
if mibBuilder.loadTexts:
    h3cDot11WlanEssIfTable.setStatus("current")
_H3cDot11WlanEssIfEntry_Object = MibTableRow
h3cDot11WlanEssIfEntry = _H3cDot11WlanEssIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 1, 1)
)
h3cDot11WlanEssIfEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11WlanEssIfNumber"),
)
if mibBuilder.loadTexts:
    h3cDot11WlanEssIfEntry.setStatus("current")
_H3cDot11WlanEssIfNumber_Type = Integer32
_H3cDot11WlanEssIfNumber_Object = MibTableColumn
h3cDot11WlanEssIfNumber = _H3cDot11WlanEssIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 1, 1, 1),
    _H3cDot11WlanEssIfNumber_Type()
)
h3cDot11WlanEssIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WlanEssIfNumber.setStatus("current")
_H3cDot11WlanEssIfIndex_Type = Integer32
_H3cDot11WlanEssIfIndex_Object = MibTableColumn
h3cDot11WlanEssIfIndex = _H3cDot11WlanEssIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 1, 1, 2),
    _H3cDot11WlanEssIfIndex_Type()
)
h3cDot11WlanEssIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WlanEssIfIndex.setStatus("current")
_H3cDot11WlanEssRowStatus_Type = RowStatus
_H3cDot11WlanEssRowStatus_Object = MibTableColumn
h3cDot11WlanEssRowStatus = _H3cDot11WlanEssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 1, 1, 3),
    _H3cDot11WlanEssRowStatus_Type()
)
h3cDot11WlanEssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11WlanEssRowStatus.setStatus("current")
_H3cDot11WlanBssIfTable_Object = MibTable
h3cDot11WlanBssIfTable = _H3cDot11WlanBssIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 2)
)
if mibBuilder.loadTexts:
    h3cDot11WlanBssIfTable.setStatus("current")
_H3cDot11WlanBssIfEntry_Object = MibTableRow
h3cDot11WlanBssIfEntry = _H3cDot11WlanBssIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 2, 1)
)
h3cDot11WlanBssIfEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11WlanBssIfNumber"),
)
if mibBuilder.loadTexts:
    h3cDot11WlanBssIfEntry.setStatus("current")
_H3cDot11WlanBssIfNumber_Type = Integer32
_H3cDot11WlanBssIfNumber_Object = MibTableColumn
h3cDot11WlanBssIfNumber = _H3cDot11WlanBssIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 2, 1, 1),
    _H3cDot11WlanBssIfNumber_Type()
)
h3cDot11WlanBssIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WlanBssIfNumber.setStatus("current")
_H3cDot11WlanBssIfIndex_Type = Integer32
_H3cDot11WlanBssIfIndex_Object = MibTableColumn
h3cDot11WlanBssIfIndex = _H3cDot11WlanBssIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 2, 1, 2),
    _H3cDot11WlanBssIfIndex_Type()
)
h3cDot11WlanBssIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WlanBssIfIndex.setStatus("current")
_H3cDot11WlanBssRowStatus_Type = RowStatus
_H3cDot11WlanBssRowStatus_Object = MibTableColumn
h3cDot11WlanBssRowStatus = _H3cDot11WlanBssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 2, 1, 3),
    _H3cDot11WlanBssRowStatus_Type()
)
h3cDot11WlanBssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11WlanBssRowStatus.setStatus("current")
_H3cDot11WLANEthernetIfTable_Object = MibTable
h3cDot11WLANEthernetIfTable = _H3cDot11WLANEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 3)
)
if mibBuilder.loadTexts:
    h3cDot11WLANEthernetIfTable.setStatus("current")
_H3cDot11WLANEthernetIfEntry_Object = MibTableRow
h3cDot11WLANEthernetIfEntry = _H3cDot11WLANEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 3, 1)
)
h3cDot11WLANEthernetIfEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11WlanEthernetIfNumber"),
)
if mibBuilder.loadTexts:
    h3cDot11WLANEthernetIfEntry.setStatus("current")
_H3cDot11WlanEthernetIfNumber_Type = Integer32
_H3cDot11WlanEthernetIfNumber_Object = MibTableColumn
h3cDot11WlanEthernetIfNumber = _H3cDot11WlanEthernetIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 3, 1, 1),
    _H3cDot11WlanEthernetIfNumber_Type()
)
h3cDot11WlanEthernetIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WlanEthernetIfNumber.setStatus("current")
_H3cDot11WLANEthernetIfIndex_Type = Integer32
_H3cDot11WLANEthernetIfIndex_Object = MibTableColumn
h3cDot11WLANEthernetIfIndex = _H3cDot11WLANEthernetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 3, 1, 2),
    _H3cDot11WLANEthernetIfIndex_Type()
)
h3cDot11WLANEthernetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WLANEthernetIfIndex.setStatus("current")
_H3cDot11WlanEthernetRowStatus_Type = RowStatus
_H3cDot11WlanEthernetRowStatus_Object = MibTableColumn
h3cDot11WlanEthernetRowStatus = _H3cDot11WlanEthernetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 3, 1, 3),
    _H3cDot11WlanEthernetRowStatus_Type()
)
h3cDot11WlanEthernetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11WlanEthernetRowStatus.setStatus("current")
_H3cDot11PortSecurityTable_Object = MibTable
h3cDot11PortSecurityTable = _H3cDot11PortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 4)
)
if mibBuilder.loadTexts:
    h3cDot11PortSecurityTable.setStatus("current")
_H3cDot11PortSecurityEntry_Object = MibTableRow
h3cDot11PortSecurityEntry = _H3cDot11PortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 4, 1)
)
h3cDot11PortSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11PortSecurityEntry.setStatus("current")


class _H3cDot11PortSecurityMode_Type(Integer32):
    """Custom type h3cDot11PortSecurityMode based on Integer32"""
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


_H3cDot11PortSecurityMode_Type.__name__ = "Integer32"
_H3cDot11PortSecurityMode_Object = MibTableColumn
h3cDot11PortSecurityMode = _H3cDot11PortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 4, 1, 1),
    _H3cDot11PortSecurityMode_Type()
)
h3cDot11PortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11PortSecurityMode.setStatus("current")


class _H3cDot11SecurityUserLoginTxKeyType_Type(Integer32):
    """Custom type h3cDot11SecurityUserLoginTxKeyType based on Integer32"""
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


_H3cDot11SecurityUserLoginTxKeyType_Type.__name__ = "Integer32"
_H3cDot11SecurityUserLoginTxKeyType_Object = MibTableColumn
h3cDot11SecurityUserLoginTxKeyType = _H3cDot11SecurityUserLoginTxKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 4, 1, 2),
    _H3cDot11SecurityUserLoginTxKeyType_Type()
)
h3cDot11SecurityUserLoginTxKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SecurityUserLoginTxKeyType.setStatus("current")


class _H3cDot11SecurityPskKeyMode_Type(Integer32):
    """Custom type h3cDot11SecurityPskKeyMode based on Integer32"""
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


_H3cDot11SecurityPskKeyMode_Type.__name__ = "Integer32"
_H3cDot11SecurityPskKeyMode_Object = MibTableColumn
h3cDot11SecurityPskKeyMode = _H3cDot11SecurityPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 4, 1, 3),
    _H3cDot11SecurityPskKeyMode_Type()
)
h3cDot11SecurityPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SecurityPskKeyMode.setStatus("current")
_H3cDot11SecurityPskKeyString_Type = DisplayString
_H3cDot11SecurityPskKeyString_Object = MibTableColumn
h3cDot11SecurityPskKeyString = _H3cDot11SecurityPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 4, 1, 4),
    _H3cDot11SecurityPskKeyString_Type()
)
h3cDot11SecurityPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11SecurityPskKeyString.setStatus("current")
_H3cDot11WlanMeshIfTable_Object = MibTable
h3cDot11WlanMeshIfTable = _H3cDot11WlanMeshIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 5)
)
if mibBuilder.loadTexts:
    h3cDot11WlanMeshIfTable.setStatus("current")
_H3cDot11WlanMeshIfEntry_Object = MibTableRow
h3cDot11WlanMeshIfEntry = _H3cDot11WlanMeshIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 5, 1)
)
h3cDot11WlanMeshIfEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11WlanMeshIfNumber"),
)
if mibBuilder.loadTexts:
    h3cDot11WlanMeshIfEntry.setStatus("current")
_H3cDot11WlanMeshIfNumber_Type = Integer32
_H3cDot11WlanMeshIfNumber_Object = MibTableColumn
h3cDot11WlanMeshIfNumber = _H3cDot11WlanMeshIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 5, 1, 1),
    _H3cDot11WlanMeshIfNumber_Type()
)
h3cDot11WlanMeshIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11WlanMeshIfNumber.setStatus("current")
_H3cDot11WlanMeshIfIndex_Type = Integer32
_H3cDot11WlanMeshIfIndex_Object = MibTableColumn
h3cDot11WlanMeshIfIndex = _H3cDot11WlanMeshIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 5, 1, 2),
    _H3cDot11WlanMeshIfIndex_Type()
)
h3cDot11WlanMeshIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11WlanMeshIfIndex.setStatus("current")
_H3cDot11WlanMeshRowStatus_Type = RowStatus
_H3cDot11WlanMeshRowStatus_Object = MibTableColumn
h3cDot11WlanMeshRowStatus = _H3cDot11WlanMeshRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 6, 5, 1, 3),
    _H3cDot11WlanMeshRowStatus_Type()
)
h3cDot11WlanMeshRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDot11WlanMeshRowStatus.setStatus("current")
_H3cDot11ACBackupGroup_ObjectIdentity = ObjectIdentity
h3cDot11ACBackupGroup = _H3cDot11ACBackupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 7)
)
_H3cDot11BackupACAdrssIP_Type = InetAddress
_H3cDot11BackupACAdrssIP_Object = MibScalar
h3cDot11BackupACAdrssIP = _H3cDot11BackupACAdrssIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 7, 1),
    _H3cDot11BackupACAdrssIP_Type()
)
h3cDot11BackupACAdrssIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11BackupACAdrssIP.setStatus("current")
_H3cDot11BackupACAdrssIPv6_Type = InetAddress
_H3cDot11BackupACAdrssIPv6_Object = MibScalar
h3cDot11BackupACAdrssIPv6 = _H3cDot11BackupACAdrssIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 7, 2),
    _H3cDot11BackupACAdrssIPv6_Type()
)
h3cDot11BackupACAdrssIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11BackupACAdrssIPv6.setStatus("current")
_H3cDot11RadioElementConfigGroup_ObjectIdentity = ObjectIdentity
h3cDot11RadioElementConfigGroup = _H3cDot11RadioElementConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8)
)
_H3cDot11nRadioCfgTable_Object = MibTable
h3cDot11nRadioCfgTable = _H3cDot11nRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 1)
)
if mibBuilder.loadTexts:
    h3cDot11nRadioCfgTable.setStatus("current")
_H3cDot11nRadioCfgEntry_Object = MibTableRow
h3cDot11nRadioCfgEntry = _H3cDot11nRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 1, 1)
)
h3cDot11nRadioCfgEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11nRadioCfgIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11nRadioCfgEntry.setStatus("current")
_H3cDot11nRadioCfgIndex_Type = H3cDot11RadioElementIndex
_H3cDot11nRadioCfgIndex_Object = MibTableColumn
h3cDot11nRadioCfgIndex = _H3cDot11nRadioCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 1, 1, 1),
    _H3cDot11nRadioCfgIndex_Type()
)
h3cDot11nRadioCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11nRadioCfgIndex.setStatus("current")


class _H3cDot11nAMpduEnable_Type(TruthValue):
    """Custom type h3cDot11nAMpduEnable based on TruthValue"""


_H3cDot11nAMpduEnable_Object = MibTableColumn
h3cDot11nAMpduEnable = _H3cDot11nAMpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 1, 1, 2),
    _H3cDot11nAMpduEnable_Type()
)
h3cDot11nAMpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11nAMpduEnable.setStatus("current")


class _H3cDot11nAMsduEnable_Type(TruthValue):
    """Custom type h3cDot11nAMsduEnable based on TruthValue"""


_H3cDot11nAMsduEnable_Object = MibTableColumn
h3cDot11nAMsduEnable = _H3cDot11nAMsduEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 1, 1, 3),
    _H3cDot11nAMsduEnable_Type()
)
h3cDot11nAMsduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11nAMsduEnable.setStatus("current")


class _H3cDot11nClientDot11nOnly_Type(TruthValue):
    """Custom type h3cDot11nClientDot11nOnly based on TruthValue"""


_H3cDot11nClientDot11nOnly_Object = MibTableColumn
h3cDot11nClientDot11nOnly = _H3cDot11nClientDot11nOnly_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 1, 1, 4),
    _H3cDot11nClientDot11nOnly_Type()
)
h3cDot11nClientDot11nOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11nClientDot11nOnly.setStatus("current")


class _H3cDot11nChanelBand_Type(Integer32):
    """Custom type h3cDot11nChanelBand based on Integer32"""
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


_H3cDot11nChanelBand_Type.__name__ = "Integer32"
_H3cDot11nChanelBand_Object = MibTableColumn
h3cDot11nChanelBand = _H3cDot11nChanelBand_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 1, 1, 5),
    _H3cDot11nChanelBand_Type()
)
h3cDot11nChanelBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11nChanelBand.setStatus("current")


class _H3cDot11nShortGiEnable_Type(TruthValue):
    """Custom type h3cDot11nShortGiEnable based on TruthValue"""


_H3cDot11nShortGiEnable_Object = MibTableColumn
h3cDot11nShortGiEnable = _H3cDot11nShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 1, 1, 6),
    _H3cDot11nShortGiEnable_Type()
)
h3cDot11nShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11nShortGiEnable.setStatus("current")
_H3cDot11RadioWDSTable_Object = MibTable
h3cDot11RadioWDSTable = _H3cDot11RadioWDSTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 2)
)
if mibBuilder.loadTexts:
    h3cDot11RadioWDSTable.setStatus("current")
_H3cDot11RadioWDSEntry_Object = MibTableRow
h3cDot11RadioWDSEntry = _H3cDot11RadioWDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 2, 1)
)
h3cDot11RadioWDSEntry.setIndexNames(
    (0, "H3C-DOT11-CFG-MIB", "h3cDot11RadioWDSIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioWDSEntry.setStatus("current")
_H3cDot11RadioWDSIndex_Type = H3cDot11RadioElementIndex
_H3cDot11RadioWDSIndex_Object = MibTableColumn
h3cDot11RadioWDSIndex = _H3cDot11RadioWDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 2, 1, 1),
    _H3cDot11RadioWDSIndex_Type()
)
h3cDot11RadioWDSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RadioWDSIndex.setStatus("current")


class _H3cDot11RadioWDSMode_Type(Integer32):
    """Custom type h3cDot11RadioWDSMode based on Integer32"""
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


_H3cDot11RadioWDSMode_Type.__name__ = "Integer32"
_H3cDot11RadioWDSMode_Object = MibTableColumn
h3cDot11RadioWDSMode = _H3cDot11RadioWDSMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 2, 1, 2),
    _H3cDot11RadioWDSMode_Type()
)
h3cDot11RadioWDSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioWDSMode.setStatus("current")


class _H3cDot11RadioWDSNetWorkID_Type(OctetString):
    """Custom type h3cDot11RadioWDSNetWorkID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDot11RadioWDSNetWorkID_Type.__name__ = "OctetString"
_H3cDot11RadioWDSNetWorkID_Object = MibTableColumn
h3cDot11RadioWDSNetWorkID = _H3cDot11RadioWDSNetWorkID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 2, 1, 3),
    _H3cDot11RadioWDSNetWorkID_Type()
)
h3cDot11RadioWDSNetWorkID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioWDSNetWorkID.setStatus("current")


class _H3cDot11WDSSecPskKeyMode_Type(Integer32):
    """Custom type h3cDot11WDSSecPskKeyMode based on Integer32"""
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


_H3cDot11WDSSecPskKeyMode_Type.__name__ = "Integer32"
_H3cDot11WDSSecPskKeyMode_Object = MibTableColumn
h3cDot11WDSSecPskKeyMode = _H3cDot11WDSSecPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 2, 1, 4),
    _H3cDot11WDSSecPskKeyMode_Type()
)
h3cDot11WDSSecPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WDSSecPskKeyMode.setStatus("current")
_H3cDot11WDSSecPskKeyString_Type = DisplayString
_H3cDot11WDSSecPskKeyString_Object = MibTableColumn
h3cDot11WDSSecPskKeyString = _H3cDot11WDSSecPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 8, 2, 1, 5),
    _H3cDot11WDSSecPskKeyString_Type()
)
h3cDot11WDSSecPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11WDSSecPskKeyString.setStatus("current")
_H3cDot11CfgNotifyGroup_ObjectIdentity = ObjectIdentity
h3cDot11CfgNotifyGroup = _H3cDot11CfgNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 9)
)
_H3cDot11CfgNotifications_ObjectIdentity = ObjectIdentity
h3cDot11CfgNotifications = _H3cDot11CfgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 9, 0)
)
_H3cDot11CfgTrapVarObjects_ObjectIdentity = ObjectIdentity
h3cDot11CfgTrapVarObjects = _H3cDot11CfgTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 9, 1)
)


class _H3cDot11PreConflictTemplateNum_Type(Integer32):
    """Custom type h3cDot11PreConflictTemplateNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_H3cDot11PreConflictTemplateNum_Type.__name__ = "Integer32"
_H3cDot11PreConflictTemplateNum_Object = MibScalar
h3cDot11PreConflictTemplateNum = _H3cDot11PreConflictTemplateNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 9, 1, 1),
    _H3cDot11PreConflictTemplateNum_Type()
)
h3cDot11PreConflictTemplateNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11PreConflictTemplateNum.setStatus("current")


class _H3cDot11CurrConflictTemplateNum_Type(Integer32):
    """Custom type h3cDot11CurrConflictTemplateNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_H3cDot11CurrConflictTemplateNum_Type.__name__ = "Integer32"
_H3cDot11CurrConflictTemplateNum_Object = MibScalar
h3cDot11CurrConflictTemplateNum = _H3cDot11CurrConflictTemplateNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 9, 1, 2),
    _H3cDot11CurrConflictTemplateNum_Type()
)
h3cDot11CurrConflictTemplateNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11CurrConflictTemplateNum.setStatus("current")


class _H3cDot11ConflictCipherIdx_Type(Integer32):
    """Custom type h3cDot11ConflictCipherIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_H3cDot11ConflictCipherIdx_Type.__name__ = "Integer32"
_H3cDot11ConflictCipherIdx_Object = MibScalar
h3cDot11ConflictCipherIdx = _H3cDot11ConflictCipherIdx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 9, 1, 3),
    _H3cDot11ConflictCipherIdx_Type()
)
h3cDot11ConflictCipherIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ConflictCipherIdx.setStatus("current")
_H3cDot11ConfigureAPID_Type = H3cDot11ObjectIDType
_H3cDot11ConfigureAPID_Object = MibScalar
h3cDot11ConfigureAPID = _H3cDot11ConfigureAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 9, 1, 4),
    _H3cDot11ConfigureAPID_Type()
)
h3cDot11ConfigureAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ConfigureAPID.setStatus("current")
_H3cDot11ConfigureRadioID_Type = H3cDot11RadioScopeType
_H3cDot11ConfigureRadioID_Object = MibScalar
h3cDot11ConfigureRadioID = _H3cDot11ConfigureRadioID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 9, 1, 5),
    _H3cDot11ConfigureRadioID_Type()
)
h3cDot11ConfigureRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDot11ConfigureRadioID.setStatus("current")

# Managed Objects groups


# Notification objects

h3cDot11CfgCipherChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 9, 0, 1)
)
h3cDot11CfgCipherChange.setObjects(
      *(("H3C-DOT11-CFG-MIB", "h3cDot11SSIDName"),
        ("H3C-DOT11-CFG-MIB", "h3cDot11SecurityCiphers"))
)
if mibBuilder.loadTexts:
    h3cDot11CfgCipherChange.setStatus(
        "current"
    )

h3cDot11CfgPSKChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 9, 0, 2)
)
h3cDot11CfgPSKChange.setObjects(
    ("H3C-DOT11-CFG-MIB", "h3cDot11SSIDName")
)
if mibBuilder.loadTexts:
    h3cDot11CfgPSKChange.setStatus(
        "current"
    )

h3cDot11SSIDWepIDConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 4, 9, 0, 3)
)
h3cDot11SSIDWepIDConflictTrap.setObjects(
      *(("H3C-DOT11-CFG-MIB", "h3cDot11PreConflictTemplateNum"),
        ("H3C-DOT11-CFG-MIB", "h3cDot11CurrConflictTemplateNum"),
        ("H3C-DOT11-CFG-MIB", "h3cDot11ConflictCipherIdx"),
        ("H3C-DOT11-CFG-MIB", "h3cDot11ConfigureAPID"),
        ("H3C-DOT11-CFG-MIB", "h3cDot11ConfigureRadioID"))
)
if mibBuilder.loadTexts:
    h3cDot11SSIDWepIDConflictTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DOT11-CFG-MIB",
    **{"h3cDot11CFG": h3cDot11CFG,
       "h3cDot11GlobeConfigGroup": h3cDot11GlobeConfigGroup,
       "h3cDot11GlobalCountryCode": h3cDot11GlobalCountryCode,
       "h3cDot11StaKeepALiveTimerIntvl": h3cDot11StaKeepALiveTimerIntvl,
       "h3cDot11StaIdleTimerIntvl": h3cDot11StaIdleTimerIntvl,
       "h3cDot11BroadcastProbeReply": h3cDot11BroadcastProbeReply,
       "h3cDot11APScanMode": h3cDot11APScanMode,
       "h3cDot11ACCtrlTunnelSecSupport": h3cDot11ACCtrlTunnelSecSupport,
       "h3cDot11ACDataTunnelSecSupport": h3cDot11ACDataTunnelSecSupport,
       "h3cDot11ACAutoAPSupport": h3cDot11ACAutoAPSupport,
       "h3cDot11AutoAPName": h3cDot11AutoAPName,
       "h3cDot11PersistentName": h3cDot11PersistentName,
       "h3cDot11IntfTrapThreshold": h3cDot11IntfTrapThreshold,
       "h3cDot11MonitorInterval": h3cDot11MonitorInterval,
       "h3cDot11SampleInterval": h3cDot11SampleInterval,
       "h3cDot11ChnlSwitChkInterval": h3cDot11ChnlSwitChkInterval,
       "h3cDot11APUserUplimit": h3cDot11APUserUplimit,
       "h3cDot11APL2IsolateEnable": h3cDot11APL2IsolateEnable,
       "h3cDot11APBSSIDSupportNum": h3cDot11APBSSIDSupportNum,
       "h3cDot11APLastUpdateStatTime": h3cDot11APLastUpdateStatTime,
       "h3cDot11APDoSProtectEnable": h3cDot11APDoSProtectEnable,
       "h3cDot11MaxAPPerIf": h3cDot11MaxAPPerIf,
       "h3cDot11SampleTimeStamp": h3cDot11SampleTimeStamp,
       "h3cDot11UplinkTrackId": h3cDot11UplinkTrackId,
       "h3cDot11RtCollectSwitch": h3cDot11RtCollectSwitch,
       "h3cDot11RglCollectIntvl": h3cDot11RglCollectIntvl,
       "h3cDot11RtCollectIntvl": h3cDot11RtCollectIntvl,
       "h3cDot11AllAPCpuUsageThreshold": h3cDot11AllAPCpuUsageThreshold,
       "h3cDot11AllAPMemUsageThreshold": h3cDot11AllAPMemUsageThreshold,
       "h3cDot11AdjIntfTrapThreshold": h3cDot11AdjIntfTrapThreshold,
       "h3cDot11PolicyConfigGroup": h3cDot11PolicyConfigGroup,
       "h3cDot11RadioPolicyTable": h3cDot11RadioPolicyTable,
       "h3cDot11RadioPolicyEntry": h3cDot11RadioPolicyEntry,
       "h3cDot11RadioPolicyName": h3cDot11RadioPolicyName,
       "h3cDot11BeaconInterval": h3cDot11BeaconInterval,
       "h3cDot11DtimInterval": h3cDot11DtimInterval,
       "h3cDot11RtsThreshold": h3cDot11RtsThreshold,
       "h3cDot11FragThreshold": h3cDot11FragThreshold,
       "h3cDot11ShortRetryThreshold": h3cDot11ShortRetryThreshold,
       "h3cDot11LongRetryThreshold": h3cDot11LongRetryThreshold,
       "h3cDot11MaxRxLifetime": h3cDot11MaxRxLifetime,
       "h3cDot11RdoPolicyRowStatus": h3cDot11RdoPolicyRowStatus,
       "h3cDot11RdoClientMaxCount": h3cDot11RdoClientMaxCount,
       "h3cDot11BeaconIntervalMs": h3cDot11BeaconIntervalMs,
       "h3cDot11ServicePolicyTable": h3cDot11ServicePolicyTable,
       "h3cDot11ServicePolicyEntry": h3cDot11ServicePolicyEntry,
       "h3cDot11ServicePolicyID": h3cDot11ServicePolicyID,
       "h3cDot11SSIDName": h3cDot11SSIDName,
       "h3cDot11SSIDHidden": h3cDot11SSIDHidden,
       "h3cDot11AuthenMode": h3cDot11AuthenMode,
       "h3cDot11SSIDEncryptionMode": h3cDot11SSIDEncryptionMode,
       "h3cDot11WlanInfBindingType": h3cDot11WlanInfBindingType,
       "h3cDot11WlanInfBindingID": h3cDot11WlanInfBindingID,
       "h3cDot11SrvPolicyRowStatus": h3cDot11SrvPolicyRowStatus,
       "h3cDot11ClientMaxCount": h3cDot11ClientMaxCount,
       "h3cDot11SPInCirMode": h3cDot11SPInCirMode,
       "h3cDot11SPInCirValue": h3cDot11SPInCirValue,
       "h3cDot11SPOutCirMode": h3cDot11SPOutCirMode,
       "h3cDot11SPOutCirValue": h3cDot11SPOutCirValue,
       "h3cDot11WlanInfPVID": h3cDot11WlanInfPVID,
       "h3cDot11SPInCirStaticValue": h3cDot11SPInCirStaticValue,
       "h3cDot11SPOutCirStaticValue": h3cDot11SPOutCirStaticValue,
       "h3cDot11SPIsolate": h3cDot11SPIsolate,
       "h3cDot11ServicePolicyExtTable": h3cDot11ServicePolicyExtTable,
       "h3cDot11ServicePolicyExtEntry": h3cDot11ServicePolicyExtEntry,
       "h3cDot11ServicePolicyExtID": h3cDot11ServicePolicyExtID,
       "h3cDot11SecIEStatus": h3cDot11SecIEStatus,
       "h3cDot11SecurityCiphers": h3cDot11SecurityCiphers,
       "h3cDot11CipherKeyIndex": h3cDot11CipherKeyIndex,
       "h3cDot11CipherKey": h3cDot11CipherKey,
       "h3cDot11SrvPolicyExtRowStatus": h3cDot11SrvPolicyExtRowStatus,
       "h3cDot11CipherKeyType": h3cDot11CipherKeyType,
       "h3cDot11RadioPolicyExtTable": h3cDot11RadioPolicyExtTable,
       "h3cDot11RadioPolicyExtEntry": h3cDot11RadioPolicyExtEntry,
       "h3cDot11RPAPSerialID": h3cDot11RPAPSerialID,
       "h3cDot11RPRadioID": h3cDot11RPRadioID,
       "h3cDot11RPBeaconInterval": h3cDot11RPBeaconInterval,
       "h3cDot11RPDtimInterval": h3cDot11RPDtimInterval,
       "h3cDot11RPRtsThreshold": h3cDot11RPRtsThreshold,
       "h3cDot11RPFragThreshold": h3cDot11RPFragThreshold,
       "h3cDot11RPShortRetryThreshold": h3cDot11RPShortRetryThreshold,
       "h3cDot11RPLongRetryThreshold": h3cDot11RPLongRetryThreshold,
       "h3cDot11RPClientMaxCount": h3cDot11RPClientMaxCount,
       "h3cDot11SrvPortSecurityTable": h3cDot11SrvPortSecurityTable,
       "h3cDot11SrvPortSecurityEntry": h3cDot11SrvPortSecurityEntry,
       "h3cDot11SecurityServicePolicyID": h3cDot11SecurityServicePolicyID,
       "h3cDot11SrvPortSecurityMode": h3cDot11SrvPortSecurityMode,
       "h3cDot11SrvSecurityKeyType": h3cDot11SrvSecurityKeyType,
       "h3cDot11SrvSecurityPskKeyMode": h3cDot11SrvSecurityPskKeyMode,
       "h3cDot11SrvSecurityPskKeyString": h3cDot11SrvSecurityPskKeyString,
       "h3cDot11SrvPolicyExtendTable": h3cDot11SrvPolicyExtendTable,
       "h3cDot11SrvPolicyExtendEntry": h3cDot11SrvPolicyExtendEntry,
       "h3cDot11SPEnable": h3cDot11SPEnable,
       "h3cDot11APConfigGroup": h3cDot11APConfigGroup,
       "h3cDot11APTemplateTable": h3cDot11APTemplateTable,
       "h3cDot11APTemplateEntry": h3cDot11APTemplateEntry,
       "h3cDot11APTemplateName": h3cDot11APTemplateName,
       "h3cDot11APSerialID": h3cDot11APSerialID,
       "h3cDot11TemplateAPModelAlias": h3cDot11TemplateAPModelAlias,
       "h3cDot11Description": h3cDot11Description,
       "h3cDot11APWorkMode": h3cDot11APWorkMode,
       "h3cDot11APTemplateRowStatus": h3cDot11APTemplateRowStatus,
       "h3cDot11APName": h3cDot11APName,
       "h3cDot11StatisInterv": h3cDot11StatisInterv,
       "h3cDot11APBroadcastProbeReply": h3cDot11APBroadcastProbeReply,
       "h3cDot11StaIdleTimerInterv": h3cDot11StaIdleTimerInterv,
       "h3cDot11StaKeepAliveTimerInterv": h3cDot11StaKeepAliveTimerInterv,
       "h3cDot11APCir": h3cDot11APCir,
       "h3cDot11APCbs": h3cDot11APCbs,
       "h3cDot11APPriorityLevel": h3cDot11APPriorityLevel,
       "h3cDot11APElementID": h3cDot11APElementID,
       "h3cDot11APDevDetectEnable": h3cDot11APDevDetectEnable,
       "h3cDot11APGetIPMethod": h3cDot11APGetIPMethod,
       "h3cDot11StatisIntervMode": h3cDot11StatisIntervMode,
       "h3cDot11RadioToConfigTable": h3cDot11RadioToConfigTable,
       "h3cDot11RadioToConfigEntry": h3cDot11RadioToConfigEntry,
       "h3cDot11APTemplateNameCfg": h3cDot11APTemplateNameCfg,
       "h3cDot11CfgRadioID": h3cDot11CfgRadioID,
       "h3cDot11CfgRadioPolicyName": h3cDot11CfgRadioPolicyName,
       "h3cDot11CfgRadioType": h3cDot11CfgRadioType,
       "h3cDot11CfgChannel": h3cDot11CfgChannel,
       "h3cDot11CfgMaxTxPowerLevel": h3cDot11CfgMaxTxPowerLevel,
       "h3cDot11PreambleLen": h3cDot11PreambleLen,
       "h3cDot11CfgRadioStatus": h3cDot11CfgRadioStatus,
       "h3cDot11CfgRdElementID": h3cDot11CfgRdElementID,
       "h3cDot11CfgWorkMode": h3cDot11CfgWorkMode,
       "h3cDot11CfgPwrAttValue": h3cDot11CfgPwrAttValue,
       "h3cDot11RadioTxArithmetic": h3cDot11RadioTxArithmetic,
       "h3cDot11CfgChannelLockStat": h3cDot11CfgChannelLockStat,
       "h3cDot11CfgPowerLockStat": h3cDot11CfgPowerLockStat,
       "h3cDot11CfgLBRdGroupId": h3cDot11CfgLBRdGroupId,
       "h3cDot11CfgRRMSDRdGroupId": h3cDot11CfgRRMSDRdGroupId,
       "h3cDot11APServiceSetTable": h3cDot11APServiceSetTable,
       "h3cDot11APServiceSetEntry": h3cDot11APServiceSetEntry,
       "h3cDot11CfgServicePolicyID": h3cDot11CfgServicePolicyID,
       "h3cDot11SrvSetRowStatus": h3cDot11SrvSetRowStatus,
       "h3cDot11ServiceSetVlanId": h3cDot11ServiceSetVlanId,
       "h3cDot11APSysInfoSetTable": h3cDot11APSysInfoSetTable,
       "h3cDot11APSysInfoSetEntry": h3cDot11APSysInfoSetEntry,
       "h3cDot11APSysNetID": h3cDot11APSysNetID,
       "h3cDot11APCpuUsageThreshold": h3cDot11APCpuUsageThreshold,
       "h3cDot11APMemUsageThreshold": h3cDot11APMemUsageThreshold,
       "h3cDot11APLimitTable": h3cDot11APLimitTable,
       "h3cDot11APLimitEntry": h3cDot11APLimitEntry,
       "h3cDot11APSsidNumLimit": h3cDot11APSsidNumLimit,
       "h3cDot11APUserCntLimit": h3cDot11APUserCntLimit,
       "h3cDot11APUserThreshold": h3cDot11APUserThreshold,
       "h3cDot11APIfSetTable": h3cDot11APIfSetTable,
       "h3cDot11APIfSetEntry": h3cDot11APIfSetEntry,
       "h3cDot11APSetIfIndex": h3cDot11APSetIfIndex,
       "h3cDot11APIfAlias": h3cDot11APIfAlias,
       "h3cDot11APServiceVlanTable": h3cDot11APServiceVlanTable,
       "h3cDot11APServiceVlanEntry": h3cDot11APServiceVlanEntry,
       "h3cDot11APServiceVlanSerialID": h3cDot11APServiceVlanSerialID,
       "h3cDot11APServiceVlanSPID": h3cDot11APServiceVlanSPID,
       "h3cDot11APServiceVlanId": h3cDot11APServiceVlanId,
       "h3cDot11APServiceVlanRowStatus": h3cDot11APServiceVlanRowStatus,
       "h3cDot11RadioConfigTable": h3cDot11RadioConfigTable,
       "h3cDot11RadioConfigEntry": h3cDot11RadioConfigEntry,
       "h3cDot11RCAPSerialID": h3cDot11RCAPSerialID,
       "h3cDot11RCRadioID": h3cDot11RCRadioID,
       "h3cDot11RCRadioType": h3cDot11RCRadioType,
       "h3cDot11RCChannel": h3cDot11RCChannel,
       "h3cDot11RCPreambleLen": h3cDot11RCPreambleLen,
       "h3cDot11RCPwrAttValue": h3cDot11RCPwrAttValue,
       "h3cDot11RCApPowerLevel": h3cDot11RCApPowerLevel,
       "h3cDot11RCDynamicChlState": h3cDot11RCDynamicChlState,
       "h3cDot11RCDynamicPowerState": h3cDot11RCDynamicPowerState,
       "h3cDot11RCRadioStatus": h3cDot11RCRadioStatus,
       "h3cDot11RadioSSIDCfgTable": h3cDot11RadioSSIDCfgTable,
       "h3cDot11RadioSSIDCfgEntry": h3cDot11RadioSSIDCfgEntry,
       "h3cDot11RadioSSIDSerialID": h3cDot11RadioSSIDSerialID,
       "h3cDot11RadioSSIDRadioID": h3cDot11RadioSSIDRadioID,
       "h3cDot11RadioSSIDWLANID": h3cDot11RadioSSIDWLANID,
       "h3cDot11RadioSSIDIndex": h3cDot11RadioSSIDIndex,
       "h3cDot11RadioBSSID": h3cDot11RadioBSSID,
       "h3cDot11RadioSSIDRowStatus": h3cDot11RadioSSIDRowStatus,
       "h3cDot11APSerialIDTable": h3cDot11APSerialIDTable,
       "h3cDot11APSerialIDEntry": h3cDot11APSerialIDEntry,
       "h3cDot11SIDAPSerialID": h3cDot11SIDAPSerialID,
       "h3cDot11SIDAPWorkMode": h3cDot11SIDAPWorkMode,
       "h3cDot11SIDAPGetIPMethod": h3cDot11SIDAPGetIPMethod,
       "h3cDot11APSTVlanTable": h3cDot11APSTVlanTable,
       "h3cDot11APSTVlanEntry": h3cDot11APSTVlanEntry,
       "h3cDot11CfgSTVLANID": h3cDot11CfgSTVLANID,
       "h3cDot11CfgSTNASPortID": h3cDot11CfgSTNASPortID,
       "h3cDot11CfgServiceSetRowStatus": h3cDot11CfgServiceSetRowStatus,
       "h3cDot11RadioIntfConfigGroup": h3cDot11RadioIntfConfigGroup,
       "h3cDot11RadioIntfConfigTable": h3cDot11RadioIntfConfigTable,
       "h3cDot11RadioIntfConfigEntry": h3cDot11RadioIntfConfigEntry,
       "h3cDot11RadioIfIdx": h3cDot11RadioIfIdx,
       "h3cDot11RadioCfgBeaconIntvl": h3cDot11RadioCfgBeaconIntvl,
       "h3cDot11RadioCfgDtimIntvl": h3cDot11RadioCfgDtimIntvl,
       "h3cDot11RadioCfgRtsThreshold": h3cDot11RadioCfgRtsThreshold,
       "h3cDot11RadioCfgFragThreshold": h3cDot11RadioCfgFragThreshold,
       "h3cDot11RadioCfgShtRetryThld": h3cDot11RadioCfgShtRetryThld,
       "h3cDot11RadioCfglongRtrThld": h3cDot11RadioCfglongRtrThld,
       "h3cDot11RadioCfgMaxRxLifetime": h3cDot11RadioCfgMaxRxLifetime,
       "h3cDot11RadioCfgType": h3cDot11RadioCfgType,
       "h3cDot11RadioCfgChannel": h3cDot11RadioCfgChannel,
       "h3cDot11RadioCfgMaxTxPwrLvl": h3cDot11RadioCfgMaxTxPwrLvl,
       "h3cDot11RadioCfgPreambleLen": h3cDot11RadioCfgPreambleLen,
       "h3cDot11RadioCfgWorkMode": h3cDot11RadioCfgWorkMode,
       "h3cDot11RadioCfgOnly11gEnable": h3cDot11RadioCfgOnly11gEnable,
       "h3cDot11RadioIntfBindTable": h3cDot11RadioIntfBindTable,
       "h3cDot11RadioIntfBindEntry": h3cDot11RadioIntfBindEntry,
       "h3cDot11RadioIntfBindSvcPlcyID": h3cDot11RadioIntfBindSvcPlcyID,
       "h3cDot11RadioIntfBindIfIdx": h3cDot11RadioIntfBindIfIdx,
       "h3cDot11RadioIntfBindRowStatus": h3cDot11RadioIntfBindRowStatus,
       "h3cDot11DataRateConfigGroup": h3cDot11DataRateConfigGroup,
       "h3cDot11DataRateConfigTable": h3cDot11DataRateConfigTable,
       "h3cDot11DataRateConfigEntry": h3cDot11DataRateConfigEntry,
       "h3cDot11RadioTypeID": h3cDot11RadioTypeID,
       "h3cDot11SupportedRateSet": h3cDot11SupportedRateSet,
       "h3cDot11MandatoryRateSet": h3cDot11MandatoryRateSet,
       "h3cDot11DisabledRateSet": h3cDot11DisabledRateSet,
       "h3cDot11SmartRateSet": h3cDot11SmartRateSet,
       "h3cDot11InterfaceConfigGroup": h3cDot11InterfaceConfigGroup,
       "h3cDot11WlanEssIfTable": h3cDot11WlanEssIfTable,
       "h3cDot11WlanEssIfEntry": h3cDot11WlanEssIfEntry,
       "h3cDot11WlanEssIfNumber": h3cDot11WlanEssIfNumber,
       "h3cDot11WlanEssIfIndex": h3cDot11WlanEssIfIndex,
       "h3cDot11WlanEssRowStatus": h3cDot11WlanEssRowStatus,
       "h3cDot11WlanBssIfTable": h3cDot11WlanBssIfTable,
       "h3cDot11WlanBssIfEntry": h3cDot11WlanBssIfEntry,
       "h3cDot11WlanBssIfNumber": h3cDot11WlanBssIfNumber,
       "h3cDot11WlanBssIfIndex": h3cDot11WlanBssIfIndex,
       "h3cDot11WlanBssRowStatus": h3cDot11WlanBssRowStatus,
       "h3cDot11WLANEthernetIfTable": h3cDot11WLANEthernetIfTable,
       "h3cDot11WLANEthernetIfEntry": h3cDot11WLANEthernetIfEntry,
       "h3cDot11WlanEthernetIfNumber": h3cDot11WlanEthernetIfNumber,
       "h3cDot11WLANEthernetIfIndex": h3cDot11WLANEthernetIfIndex,
       "h3cDot11WlanEthernetRowStatus": h3cDot11WlanEthernetRowStatus,
       "h3cDot11PortSecurityTable": h3cDot11PortSecurityTable,
       "h3cDot11PortSecurityEntry": h3cDot11PortSecurityEntry,
       "h3cDot11PortSecurityMode": h3cDot11PortSecurityMode,
       "h3cDot11SecurityUserLoginTxKeyType": h3cDot11SecurityUserLoginTxKeyType,
       "h3cDot11SecurityPskKeyMode": h3cDot11SecurityPskKeyMode,
       "h3cDot11SecurityPskKeyString": h3cDot11SecurityPskKeyString,
       "h3cDot11WlanMeshIfTable": h3cDot11WlanMeshIfTable,
       "h3cDot11WlanMeshIfEntry": h3cDot11WlanMeshIfEntry,
       "h3cDot11WlanMeshIfNumber": h3cDot11WlanMeshIfNumber,
       "h3cDot11WlanMeshIfIndex": h3cDot11WlanMeshIfIndex,
       "h3cDot11WlanMeshRowStatus": h3cDot11WlanMeshRowStatus,
       "h3cDot11ACBackupGroup": h3cDot11ACBackupGroup,
       "h3cDot11BackupACAdrssIP": h3cDot11BackupACAdrssIP,
       "h3cDot11BackupACAdrssIPv6": h3cDot11BackupACAdrssIPv6,
       "h3cDot11RadioElementConfigGroup": h3cDot11RadioElementConfigGroup,
       "h3cDot11nRadioCfgTable": h3cDot11nRadioCfgTable,
       "h3cDot11nRadioCfgEntry": h3cDot11nRadioCfgEntry,
       "h3cDot11nRadioCfgIndex": h3cDot11nRadioCfgIndex,
       "h3cDot11nAMpduEnable": h3cDot11nAMpduEnable,
       "h3cDot11nAMsduEnable": h3cDot11nAMsduEnable,
       "h3cDot11nClientDot11nOnly": h3cDot11nClientDot11nOnly,
       "h3cDot11nChanelBand": h3cDot11nChanelBand,
       "h3cDot11nShortGiEnable": h3cDot11nShortGiEnable,
       "h3cDot11RadioWDSTable": h3cDot11RadioWDSTable,
       "h3cDot11RadioWDSEntry": h3cDot11RadioWDSEntry,
       "h3cDot11RadioWDSIndex": h3cDot11RadioWDSIndex,
       "h3cDot11RadioWDSMode": h3cDot11RadioWDSMode,
       "h3cDot11RadioWDSNetWorkID": h3cDot11RadioWDSNetWorkID,
       "h3cDot11WDSSecPskKeyMode": h3cDot11WDSSecPskKeyMode,
       "h3cDot11WDSSecPskKeyString": h3cDot11WDSSecPskKeyString,
       "h3cDot11CfgNotifyGroup": h3cDot11CfgNotifyGroup,
       "h3cDot11CfgNotifications": h3cDot11CfgNotifications,
       "h3cDot11CfgCipherChange": h3cDot11CfgCipherChange,
       "h3cDot11CfgPSKChange": h3cDot11CfgPSKChange,
       "h3cDot11SSIDWepIDConflictTrap": h3cDot11SSIDWepIDConflictTrap,
       "h3cDot11CfgTrapVarObjects": h3cDot11CfgTrapVarObjects,
       "h3cDot11PreConflictTemplateNum": h3cDot11PreConflictTemplateNum,
       "h3cDot11CurrConflictTemplateNum": h3cDot11CurrConflictTemplateNum,
       "h3cDot11ConflictCipherIdx": h3cDot11ConflictCipherIdx,
       "h3cDot11ConfigureAPID": h3cDot11ConfigureAPID,
       "h3cDot11ConfigureRadioID": h3cDot11ConfigureRadioID}
)
