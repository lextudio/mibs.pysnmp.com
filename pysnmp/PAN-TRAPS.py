# SNMP MIB module (PAN-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAN-TRAPS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:32 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(panCommonEventEventsV2,
 panCommonEventObjs) = mibBuilder.importSymbols(
    "PAN-COMMON-MIB",
    "panCommonEventEventsV2",
    "panCommonEventObjs")

(panCommonMib,
 panModules) = mibBuilder.importSymbols(
    "PAN-GLOBAL-REG",
    "panCommonMib",
    "panModules")

(TcChassisType,) = mibBuilder.importSymbols(
    "PAN-GLOBAL-TC",
    "TcChassisType")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

panTrapMibsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 5)
)
panTrapMibsModule.setRevisions(
        ("2015-02-26 00:00",
         "2014-07-09 00:00",
         "2011-06-27 10:40")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PanReceiveTime_Type(OctetString):
    """Custom type panReceiveTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanReceiveTime_Type.__name__ = "OctetString"
_PanReceiveTime_Object = MibScalar
panReceiveTime = _PanReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 2),
    _PanReceiveTime_Type()
)
panReceiveTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panReceiveTime.setStatus("current")


class _PanSerial_Type(OctetString):
    """Custom type panSerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanSerial_Type.__name__ = "OctetString"
_PanSerial_Object = MibScalar
panSerial = _PanSerial_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 3),
    _PanSerial_Type()
)
panSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSerial.setStatus("current")


class _PanEventType_Type(OctetString):
    """Custom type panEventType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanEventType_Type.__name__ = "OctetString"
_PanEventType_Object = MibScalar
panEventType = _PanEventType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 4),
    _PanEventType_Type()
)
panEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panEventType.setStatus("current")


class _PanEventSubType_Type(OctetString):
    """Custom type panEventSubType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanEventSubType_Type.__name__ = "OctetString"
_PanEventSubType_Object = MibScalar
panEventSubType = _PanEventSubType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 5),
    _PanEventSubType_Type()
)
panEventSubType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panEventSubType.setStatus("current")
_PanHost_Type = IpAddress
_PanHost_Object = MibScalar
panHost = _PanHost_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 6),
    _PanHost_Type()
)
panHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHost.setStatus("current")


class _PanVsys_Type(OctetString):
    """Custom type panVsys based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PanVsys_Type.__name__ = "OctetString"
_PanVsys_Object = MibScalar
panVsys = _PanVsys_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 7),
    _PanVsys_Type()
)
panVsys.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panVsys.setStatus("current")
_PanSeqno_Type = Counter64
_PanSeqno_Object = MibScalar
panSeqno = _PanSeqno_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 8),
    _PanSeqno_Type()
)
panSeqno.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSeqno.setStatus("current")


class _PanActionflags_Type(OctetString):
    """Custom type panActionflags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PanActionflags_Type.__name__ = "OctetString"
_PanActionflags_Object = MibScalar
panActionflags = _PanActionflags_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 9),
    _PanActionflags_Type()
)
panActionflags.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panActionflags.setStatus("current")
_PanHostInetAddrType_Type = InetAddressType
_PanHostInetAddrType_Object = MibScalar
panHostInetAddrType = _PanHostInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 10),
    _PanHostInetAddrType_Type()
)
panHostInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHostInetAddrType.setStatus("current")
_PanHostInetAddr_Type = InetAddress
_PanHostInetAddr_Object = MibScalar
panHostInetAddr = _PanHostInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 11),
    _PanHostInetAddr_Type()
)
panHostInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHostInetAddr.setStatus("current")
_PanSource_Type = IpAddress
_PanSource_Object = MibScalar
panSource = _PanSource_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 50),
    _PanSource_Type()
)
panSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSource.setStatus("current")
_PanDestination_Type = IpAddress
_PanDestination_Object = MibScalar
panDestination = _PanDestination_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 51),
    _PanDestination_Type()
)
panDestination.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDestination.setStatus("current")
_PanNatSource_Type = IpAddress
_PanNatSource_Object = MibScalar
panNatSource = _PanNatSource_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 52),
    _PanNatSource_Type()
)
panNatSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatSource.setStatus("current")
_PanNatDestination_Type = IpAddress
_PanNatDestination_Object = MibScalar
panNatDestination = _PanNatDestination_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 53),
    _PanNatDestination_Type()
)
panNatDestination.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatDestination.setStatus("current")


class _PanRule_Type(OctetString):
    """Custom type panRule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanRule_Type.__name__ = "OctetString"
_PanRule_Object = MibScalar
panRule = _PanRule_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 54),
    _PanRule_Type()
)
panRule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panRule.setStatus("current")


class _PanSrcUser_Type(OctetString):
    """Custom type panSrcUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanSrcUser_Type.__name__ = "OctetString"
_PanSrcUser_Object = MibScalar
panSrcUser = _PanSrcUser_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 55),
    _PanSrcUser_Type()
)
panSrcUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSrcUser.setStatus("current")


class _PanDstUser_Type(OctetString):
    """Custom type panDstUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanDstUser_Type.__name__ = "OctetString"
_PanDstUser_Object = MibScalar
panDstUser = _PanDstUser_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 56),
    _PanDstUser_Type()
)
panDstUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDstUser.setStatus("current")


class _PanApplication_Type(OctetString):
    """Custom type panApplication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanApplication_Type.__name__ = "OctetString"
_PanApplication_Object = MibScalar
panApplication = _PanApplication_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 57),
    _PanApplication_Type()
)
panApplication.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panApplication.setStatus("current")


class _PanSourceZone_Type(OctetString):
    """Custom type panSourceZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanSourceZone_Type.__name__ = "OctetString"
_PanSourceZone_Object = MibScalar
panSourceZone = _PanSourceZone_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 58),
    _PanSourceZone_Type()
)
panSourceZone.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSourceZone.setStatus("current")


class _PanDestinationZone_Type(OctetString):
    """Custom type panDestinationZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanDestinationZone_Type.__name__ = "OctetString"
_PanDestinationZone_Object = MibScalar
panDestinationZone = _PanDestinationZone_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 59),
    _PanDestinationZone_Type()
)
panDestinationZone.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDestinationZone.setStatus("current")


class _PanIngressInterface_Type(OctetString):
    """Custom type panIngressInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanIngressInterface_Type.__name__ = "OctetString"
_PanIngressInterface_Object = MibScalar
panIngressInterface = _PanIngressInterface_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 60),
    _PanIngressInterface_Type()
)
panIngressInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panIngressInterface.setStatus("current")


class _PanEgressInterface_Type(OctetString):
    """Custom type panEgressInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanEgressInterface_Type.__name__ = "OctetString"
_PanEgressInterface_Object = MibScalar
panEgressInterface = _PanEgressInterface_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 61),
    _PanEgressInterface_Type()
)
panEgressInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panEgressInterface.setStatus("current")


class _PanLogForwardingProfile_Type(OctetString):
    """Custom type panLogForwardingProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanLogForwardingProfile_Type.__name__ = "OctetString"
_PanLogForwardingProfile_Object = MibScalar
panLogForwardingProfile = _PanLogForwardingProfile_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 62),
    _PanLogForwardingProfile_Type()
)
panLogForwardingProfile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panLogForwardingProfile.setStatus("current")
_PanSessionID_Type = Counter32
_PanSessionID_Object = MibScalar
panSessionID = _PanSessionID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 63),
    _PanSessionID_Type()
)
panSessionID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSessionID.setStatus("current")
_PanRepeatCount_Type = Counter32
_PanRepeatCount_Object = MibScalar
panRepeatCount = _PanRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 64),
    _PanRepeatCount_Type()
)
panRepeatCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panRepeatCount.setStatus("current")
_PanSourcePort_Type = Counter32
_PanSourcePort_Object = MibScalar
panSourcePort = _PanSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 65),
    _PanSourcePort_Type()
)
panSourcePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSourcePort.setStatus("current")
_PanDestinationPort_Type = Counter32
_PanDestinationPort_Object = MibScalar
panDestinationPort = _PanDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 66),
    _PanDestinationPort_Type()
)
panDestinationPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDestinationPort.setStatus("current")
_PanNatSourcePort_Type = Counter32
_PanNatSourcePort_Object = MibScalar
panNatSourcePort = _PanNatSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 67),
    _PanNatSourcePort_Type()
)
panNatSourcePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatSourcePort.setStatus("current")
_PanNatDestinationPort_Type = Counter32
_PanNatDestinationPort_Object = MibScalar
panNatDestinationPort = _PanNatDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 68),
    _PanNatDestinationPort_Type()
)
panNatDestinationPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatDestinationPort.setStatus("current")


class _PanFlags_Type(OctetString):
    """Custom type panFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanFlags_Type.__name__ = "OctetString"
_PanFlags_Object = MibScalar
panFlags = _PanFlags_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 69),
    _PanFlags_Type()
)
panFlags.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panFlags.setStatus("current")


class _PanProtocol_Type(OctetString):
    """Custom type panProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanProtocol_Type.__name__ = "OctetString"
_PanProtocol_Object = MibScalar
panProtocol = _PanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 70),
    _PanProtocol_Type()
)
panProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panProtocol.setStatus("current")


class _PanAction_Type(OctetString):
    """Custom type panAction based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanAction_Type.__name__ = "OctetString"
_PanAction_Object = MibScalar
panAction = _PanAction_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 71),
    _PanAction_Type()
)
panAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panAction.setStatus("current")


class _PanTimeGenerated_Type(OctetString):
    """Custom type panTimeGenerated based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanTimeGenerated_Type.__name__ = "OctetString"
_PanTimeGenerated_Object = MibScalar
panTimeGenerated = _PanTimeGenerated_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 72),
    _PanTimeGenerated_Type()
)
panTimeGenerated.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTimeGenerated.setStatus("current")


class _PanSrcloc_Type(OctetString):
    """Custom type panSrcloc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanSrcloc_Type.__name__ = "OctetString"
_PanSrcloc_Object = MibScalar
panSrcloc = _PanSrcloc_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 73),
    _PanSrcloc_Type()
)
panSrcloc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSrcloc.setStatus("current")


class _PanDstloc_Type(OctetString):
    """Custom type panDstloc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanDstloc_Type.__name__ = "OctetString"
_PanDstloc_Object = MibScalar
panDstloc = _PanDstloc_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 74),
    _PanDstloc_Type()
)
panDstloc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDstloc.setStatus("current")
_PanSourceInetAddrType_Type = InetAddressType
_PanSourceInetAddrType_Object = MibScalar
panSourceInetAddrType = _PanSourceInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 75),
    _PanSourceInetAddrType_Type()
)
panSourceInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSourceInetAddrType.setStatus("current")
_PanSourceInetAddr_Type = InetAddress
_PanSourceInetAddr_Object = MibScalar
panSourceInetAddr = _PanSourceInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 76),
    _PanSourceInetAddr_Type()
)
panSourceInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSourceInetAddr.setStatus("current")
_PanDestinationInetAddrType_Type = InetAddressType
_PanDestinationInetAddrType_Object = MibScalar
panDestinationInetAddrType = _PanDestinationInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 77),
    _PanDestinationInetAddrType_Type()
)
panDestinationInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDestinationInetAddrType.setStatus("current")
_PanDestinationInetAddr_Type = InetAddress
_PanDestinationInetAddr_Object = MibScalar
panDestinationInetAddr = _PanDestinationInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 78),
    _PanDestinationInetAddr_Type()
)
panDestinationInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panDestinationInetAddr.setStatus("current")
_PanNatSourceInetAddrType_Type = InetAddressType
_PanNatSourceInetAddrType_Object = MibScalar
panNatSourceInetAddrType = _PanNatSourceInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 79),
    _PanNatSourceInetAddrType_Type()
)
panNatSourceInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatSourceInetAddrType.setStatus("current")
_PanNatSourceInetAddr_Type = InetAddress
_PanNatSourceInetAddr_Object = MibScalar
panNatSourceInetAddr = _PanNatSourceInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 80),
    _PanNatSourceInetAddr_Type()
)
panNatSourceInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatSourceInetAddr.setStatus("current")
_PanNatDestinationInetAddrType_Type = InetAddressType
_PanNatDestinationInetAddrType_Object = MibScalar
panNatDestinationInetAddrType = _PanNatDestinationInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 81),
    _PanNatDestinationInetAddrType_Type()
)
panNatDestinationInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatDestinationInetAddrType.setStatus("current")
_PanNatDestinationInetAddr_Type = InetAddress
_PanNatDestinationInetAddr_Object = MibScalar
panNatDestinationInetAddr = _PanNatDestinationInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 82),
    _PanNatDestinationInetAddr_Type()
)
panNatDestinationInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panNatDestinationInetAddr.setStatus("current")
_PanTrafficBytes_Type = Counter64
_PanTrafficBytes_Object = MibScalar
panTrafficBytes = _PanTrafficBytes_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 100),
    _PanTrafficBytes_Type()
)
panTrafficBytes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficBytes.setStatus("current")
_PanTrafficPackets_Type = Counter32
_PanTrafficPackets_Object = MibScalar
panTrafficPackets = _PanTrafficPackets_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 101),
    _PanTrafficPackets_Type()
)
panTrafficPackets.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficPackets.setStatus("current")


class _PanTrafficStartTime_Type(OctetString):
    """Custom type panTrafficStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanTrafficStartTime_Type.__name__ = "OctetString"
_PanTrafficStartTime_Object = MibScalar
panTrafficStartTime = _PanTrafficStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 102),
    _PanTrafficStartTime_Type()
)
panTrafficStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficStartTime.setStatus("current")
_PanTrafficElapsed_Type = TimeStamp
_PanTrafficElapsed_Object = MibScalar
panTrafficElapsed = _PanTrafficElapsed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 103),
    _PanTrafficElapsed_Type()
)
panTrafficElapsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficElapsed.setStatus("current")


class _PanTrafficCategory_Type(OctetString):
    """Custom type panTrafficCategory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanTrafficCategory_Type.__name__ = "OctetString"
_PanTrafficCategory_Object = MibScalar
panTrafficCategory = _PanTrafficCategory_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 104),
    _PanTrafficCategory_Type()
)
panTrafficCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficCategory.setStatus("current")


class _PanTrafficSessionEndReason_Type(OctetString):
    """Custom type panTrafficSessionEndReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanTrafficSessionEndReason_Type.__name__ = "OctetString"
_PanTrafficSessionEndReason_Object = MibScalar
panTrafficSessionEndReason = _PanTrafficSessionEndReason_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 105),
    _PanTrafficSessionEndReason_Type()
)
panTrafficSessionEndReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panTrafficSessionEndReason.setStatus("current")


class _PanConfigCmd_Type(OctetString):
    """Custom type panConfigCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PanConfigCmd_Type.__name__ = "OctetString"
_PanConfigCmd_Object = MibScalar
panConfigCmd = _PanConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 150),
    _PanConfigCmd_Type()
)
panConfigCmd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panConfigCmd.setStatus("current")


class _PanConfigAdmin_Type(OctetString):
    """Custom type panConfigAdmin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PanConfigAdmin_Type.__name__ = "OctetString"
_PanConfigAdmin_Object = MibScalar
panConfigAdmin = _PanConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 151),
    _PanConfigAdmin_Type()
)
panConfigAdmin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panConfigAdmin.setStatus("current")


class _PanConfigClient_Type(OctetString):
    """Custom type panConfigClient based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanConfigClient_Type.__name__ = "OctetString"
_PanConfigClient_Object = MibScalar
panConfigClient = _PanConfigClient_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 152),
    _PanConfigClient_Type()
)
panConfigClient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panConfigClient.setStatus("current")


class _PanConfigResult_Type(OctetString):
    """Custom type panConfigResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanConfigResult_Type.__name__ = "OctetString"
_PanConfigResult_Object = MibScalar
panConfigResult = _PanConfigResult_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 153),
    _PanConfigResult_Type()
)
panConfigResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panConfigResult.setStatus("current")


class _PanConfigPath_Type(OctetString):
    """Custom type panConfigPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PanConfigPath_Type.__name__ = "OctetString"
_PanConfigPath_Object = MibScalar
panConfigPath = _PanConfigPath_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 154),
    _PanConfigPath_Type()
)
panConfigPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panConfigPath.setStatus("current")


class _PanThreatId_Type(OctetString):
    """Custom type panThreatId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanThreatId_Type.__name__ = "OctetString"
_PanThreatId_Object = MibScalar
panThreatId = _PanThreatId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 200),
    _PanThreatId_Type()
)
panThreatId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatId.setStatus("current")


class _PanThreatCategory_Type(OctetString):
    """Custom type panThreatCategory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanThreatCategory_Type.__name__ = "OctetString"
_PanThreatCategory_Object = MibScalar
panThreatCategory = _PanThreatCategory_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 201),
    _PanThreatCategory_Type()
)
panThreatCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatCategory.setStatus("current")


class _PanThreatContentType_Type(OctetString):
    """Custom type panThreatContentType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanThreatContentType_Type.__name__ = "OctetString"
_PanThreatContentType_Object = MibScalar
panThreatContentType = _PanThreatContentType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 202),
    _PanThreatContentType_Type()
)
panThreatContentType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatContentType.setStatus("current")


class _PanThreatSeverity_Type(Integer32):
    """Custom type panThreatSeverity based on Integer32"""
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
        *(("critical", 5),
          ("high", 4),
          ("informational", 1),
          ("low", 2),
          ("medium", 3),
          ("unused", 0))
    )


_PanThreatSeverity_Type.__name__ = "Integer32"
_PanThreatSeverity_Object = MibScalar
panThreatSeverity = _PanThreatSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 203),
    _PanThreatSeverity_Type()
)
panThreatSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatSeverity.setStatus("current")


class _PanThreatDirection_Type(Integer32):
    """Custom type panThreatDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("client-to-server", 0),
          ("server-to-client", 1))
    )


_PanThreatDirection_Type.__name__ = "Integer32"
_PanThreatDirection_Object = MibScalar
panThreatDirection = _PanThreatDirection_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 204),
    _PanThreatDirection_Type()
)
panThreatDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panThreatDirection.setStatus("current")


class _PanMiscellaneous_Type(OctetString):
    """Custom type panMiscellaneous based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PanMiscellaneous_Type.__name__ = "OctetString"
_PanMiscellaneous_Object = MibScalar
panMiscellaneous = _PanMiscellaneous_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 205),
    _PanMiscellaneous_Type()
)
panMiscellaneous.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panMiscellaneous.setStatus("current")
_PanPcapId_Type = Counter64
_PanPcapId_Object = MibScalar
panPcapId = _PanPcapId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 206),
    _PanPcapId_Type()
)
panPcapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panPcapId.setStatus("current")


class _PanFileDigest_Type(OctetString):
    """Custom type panFileDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PanFileDigest_Type.__name__ = "OctetString"
_PanFileDigest_Object = MibScalar
panFileDigest = _PanFileDigest_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 207),
    _PanFileDigest_Type()
)
panFileDigest.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panFileDigest.setStatus("current")


class _PanCloud_Type(OctetString):
    """Custom type panCloud based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PanCloud_Type.__name__ = "OctetString"
_PanCloud_Object = MibScalar
panCloud = _PanCloud_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 208),
    _PanCloud_Type()
)
panCloud.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCloud.setStatus("current")
_PanUrlIndex_Type = Integer32
_PanUrlIndex_Object = MibScalar
panUrlIndex = _PanUrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 209),
    _PanUrlIndex_Type()
)
panUrlIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUrlIndex.setStatus("current")


class _PanUserAgent_Type(OctetString):
    """Custom type panUserAgent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PanUserAgent_Type.__name__ = "OctetString"
_PanUserAgent_Object = MibScalar
panUserAgent = _PanUserAgent_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 210),
    _PanUserAgent_Type()
)
panUserAgent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panUserAgent.setStatus("current")


class _PanXff_Type(OctetString):
    """Custom type panXff based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PanXff_Type.__name__ = "OctetString"
_PanXff_Object = MibScalar
panXff = _PanXff_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 211),
    _PanXff_Type()
)
panXff.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panXff.setStatus("current")


class _PanReferer_Type(OctetString):
    """Custom type panReferer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PanReferer_Type.__name__ = "OctetString"
_PanReferer_Object = MibScalar
panReferer = _PanReferer_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 212),
    _PanReferer_Type()
)
panReferer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panReferer.setStatus("current")


class _PanSender_Type(OctetString):
    """Custom type panSender based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PanSender_Type.__name__ = "OctetString"
_PanSender_Object = MibScalar
panSender = _PanSender_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 213),
    _PanSender_Type()
)
panSender.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSender.setStatus("current")


class _PanSubject_Type(OctetString):
    """Custom type panSubject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PanSubject_Type.__name__ = "OctetString"
_PanSubject_Object = MibScalar
panSubject = _PanSubject_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 214),
    _PanSubject_Type()
)
panSubject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSubject.setStatus("current")


class _PanRecipient_Type(OctetString):
    """Custom type panRecipient based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PanRecipient_Type.__name__ = "OctetString"
_PanRecipient_Object = MibScalar
panRecipient = _PanRecipient_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 215),
    _PanRecipient_Type()
)
panRecipient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panRecipient.setStatus("current")


class _PanFileType_Type(OctetString):
    """Custom type panFileType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanFileType_Type.__name__ = "OctetString"
_PanFileType_Object = MibScalar
panFileType = _PanFileType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 216),
    _PanFileType_Type()
)
panFileType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panFileType.setStatus("current")


class _PanReportId_Type(OctetString):
    """Custom type panReportId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanReportId_Type.__name__ = "OctetString"
_PanReportId_Object = MibScalar
panReportId = _PanReportId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 217),
    _PanReportId_Type()
)
panReportId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panReportId.setStatus("current")


class _PanHipSourceUser_Type(OctetString):
    """Custom type panHipSourceUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PanHipSourceUser_Type.__name__ = "OctetString"
_PanHipSourceUser_Object = MibScalar
panHipSourceUser = _PanHipSourceUser_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 250),
    _PanHipSourceUser_Type()
)
panHipSourceUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipSourceUser.setStatus("current")


class _PanHipMachineName_Type(OctetString):
    """Custom type panHipMachineName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PanHipMachineName_Type.__name__ = "OctetString"
_PanHipMachineName_Object = MibScalar
panHipMachineName = _PanHipMachineName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 251),
    _PanHipMachineName_Type()
)
panHipMachineName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipMachineName.setStatus("current")
_PanHipSource_Type = IpAddress
_PanHipSource_Object = MibScalar
panHipSource = _PanHipSource_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 252),
    _PanHipSource_Type()
)
panHipSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipSource.setStatus("current")


class _PanHipMatch_Type(OctetString):
    """Custom type panHipMatch based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanHipMatch_Type.__name__ = "OctetString"
_PanHipMatch_Object = MibScalar
panHipMatch = _PanHipMatch_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 253),
    _PanHipMatch_Type()
)
panHipMatch.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipMatch.setStatus("current")


class _PanHipMatchType_Type(OctetString):
    """Custom type panHipMatchType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanHipMatchType_Type.__name__ = "OctetString"
_PanHipMatchType_Object = MibScalar
panHipMatchType = _PanHipMatchType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 254),
    _PanHipMatchType_Type()
)
panHipMatchType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipMatchType.setStatus("current")
_PanHipRepeatCount_Type = Counter32
_PanHipRepeatCount_Object = MibScalar
panHipRepeatCount = _PanHipRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 255),
    _PanHipRepeatCount_Type()
)
panHipRepeatCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipRepeatCount.setStatus("current")


class _PanHipOS_Type(OctetString):
    """Custom type panHipOS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanHipOS_Type.__name__ = "OctetString"
_PanHipOS_Object = MibScalar
panHipOS = _PanHipOS_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 256),
    _PanHipOS_Type()
)
panHipOS.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipOS.setStatus("current")
_PanHipSourceInetAddrType_Type = InetAddressType
_PanHipSourceInetAddrType_Object = MibScalar
panHipSourceInetAddrType = _PanHipSourceInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 257),
    _PanHipSourceInetAddrType_Type()
)
panHipSourceInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipSourceInetAddrType.setStatus("current")
_PanHipSourceInetAddr_Type = InetAddress
_PanHipSourceInetAddr_Object = MibScalar
panHipSourceInetAddr = _PanHipSourceInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 258),
    _PanHipSourceInetAddr_Type()
)
panHipSourceInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panHipSourceInetAddr.setStatus("current")


class _PanSystemEventId_Type(OctetString):
    """Custom type panSystemEventId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanSystemEventId_Type.__name__ = "OctetString"
_PanSystemEventId_Object = MibScalar
panSystemEventId = _PanSystemEventId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 300),
    _PanSystemEventId_Type()
)
panSystemEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSystemEventId.setStatus("current")


class _PanSystemObject_Type(OctetString):
    """Custom type panSystemObject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanSystemObject_Type.__name__ = "OctetString"
_PanSystemObject_Object = MibScalar
panSystemObject = _PanSystemObject_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 301),
    _PanSystemObject_Type()
)
panSystemObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSystemObject.setStatus("current")


class _PanSystemModule_Type(OctetString):
    """Custom type panSystemModule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PanSystemModule_Type.__name__ = "OctetString"
_PanSystemModule_Object = MibScalar
panSystemModule = _PanSystemModule_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 302),
    _PanSystemModule_Type()
)
panSystemModule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSystemModule.setStatus("current")


class _PanSystemSeverity_Type(Integer32):
    """Custom type panSystemSeverity based on Integer32"""
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
        *(("critical", 5),
          ("high", 4),
          ("informational", 1),
          ("low", 2),
          ("medium", 3),
          ("unused", 0))
    )


_PanSystemSeverity_Type.__name__ = "Integer32"
_PanSystemSeverity_Object = MibScalar
panSystemSeverity = _PanSystemSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 303),
    _PanSystemSeverity_Type()
)
panSystemSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSystemSeverity.setStatus("current")


class _PanSystemDescription_Type(OctetString):
    """Custom type panSystemDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_PanSystemDescription_Type.__name__ = "OctetString"
_PanSystemDescription_Object = MibScalar
panSystemDescription = _PanSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 304),
    _PanSystemDescription_Type()
)
panSystemDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panSystemDescription.setStatus("current")


class _PanCorrDG1_Type(OctetString):
    """Custom type panCorrDG1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanCorrDG1_Type.__name__ = "OctetString"
_PanCorrDG1_Object = MibScalar
panCorrDG1 = _PanCorrDG1_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 350),
    _PanCorrDG1_Type()
)
panCorrDG1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrDG1.setStatus("current")


class _PanCorrDG2_Type(OctetString):
    """Custom type panCorrDG2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanCorrDG2_Type.__name__ = "OctetString"
_PanCorrDG2_Object = MibScalar
panCorrDG2 = _PanCorrDG2_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 351),
    _PanCorrDG2_Type()
)
panCorrDG2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrDG2.setStatus("current")


class _PanCorrDG3_Type(OctetString):
    """Custom type panCorrDG3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanCorrDG3_Type.__name__ = "OctetString"
_PanCorrDG3_Object = MibScalar
panCorrDG3 = _PanCorrDG3_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 352),
    _PanCorrDG3_Type()
)
panCorrDG3.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrDG3.setStatus("current")


class _PanCorrDG4_Type(OctetString):
    """Custom type panCorrDG4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanCorrDG4_Type.__name__ = "OctetString"
_PanCorrDG4_Object = MibScalar
panCorrDG4 = _PanCorrDG4_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 353),
    _PanCorrDG4_Type()
)
panCorrDG4.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrDG4.setStatus("current")


class _PanCorrObjName_Type(OctetString):
    """Custom type panCorrObjName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PanCorrObjName_Type.__name__ = "OctetString"
_PanCorrObjName_Object = MibScalar
panCorrObjName = _PanCorrObjName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 354),
    _PanCorrObjName_Type()
)
panCorrObjName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrObjName.setStatus("current")
_PanCorrObjID_Type = Integer32
_PanCorrObjID_Object = MibScalar
panCorrObjID = _PanCorrObjID_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 355),
    _PanCorrObjID_Type()
)
panCorrObjID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrObjID.setStatus("current")
_PanCorrSeverity_Type = Integer32
_PanCorrSeverity_Object = MibScalar
panCorrSeverity = _PanCorrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 356),
    _PanCorrSeverity_Type()
)
panCorrSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrSeverity.setStatus("current")


class _PanCorrEvidence_Type(OctetString):
    """Custom type panCorrEvidence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_PanCorrEvidence_Type.__name__ = "OctetString"
_PanCorrEvidence_Object = MibScalar
panCorrEvidence = _PanCorrEvidence_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 357),
    _PanCorrEvidence_Type()
)
panCorrEvidence.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCorrEvidence.setStatus("current")

# Managed Objects groups


# Notification objects

panConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2)
)
panConfigTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panHost"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panConfigCmd"),
        ("PAN-TRAPS", "panConfigAdmin"),
        ("PAN-TRAPS", "panConfigClient"),
        ("PAN-TRAPS", "panConfigResult"),
        ("PAN-TRAPS", "panConfigPath"))
)
if mibBuilder.loadTexts:
    panConfigTrap.setStatus(
        "current"
    )

panTrafficTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3)
)
panTrafficTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSource"),
        ("PAN-TRAPS", "panDestination"),
        ("PAN-TRAPS", "panNatSource"),
        ("PAN-TRAPS", "panNatDestination"),
        ("PAN-TRAPS", "panRule"),
        ("PAN-TRAPS", "panSrcUser"),
        ("PAN-TRAPS", "panDstUser"),
        ("PAN-TRAPS", "panApplication"),
        ("PAN-TRAPS", "panSourceZone"),
        ("PAN-TRAPS", "panDestinationZone"),
        ("PAN-TRAPS", "panIngressInterface"),
        ("PAN-TRAPS", "panEgressInterface"),
        ("PAN-TRAPS", "panLogForwardingProfile"),
        ("PAN-TRAPS", "panSessionID"),
        ("PAN-TRAPS", "panRepeatCount"),
        ("PAN-TRAPS", "panSourcePort"),
        ("PAN-TRAPS", "panDestinationPort"),
        ("PAN-TRAPS", "panNatSourcePort"),
        ("PAN-TRAPS", "panNatDestinationPort"),
        ("PAN-TRAPS", "panFlags"),
        ("PAN-TRAPS", "panProtocol"),
        ("PAN-TRAPS", "panAction"),
        ("PAN-TRAPS", "panTimeGenerated"),
        ("PAN-TRAPS", "panSrcloc"),
        ("PAN-TRAPS", "panDstloc"),
        ("PAN-TRAPS", "panTrafficBytes"),
        ("PAN-TRAPS", "panTrafficPackets"),
        ("PAN-TRAPS", "panTrafficStartTime"),
        ("PAN-TRAPS", "panTrafficElapsed"),
        ("PAN-TRAPS", "panTrafficCategory"),
        ("PAN-TRAPS", "panTrafficSessionEndReason"))
)
if mibBuilder.loadTexts:
    panTrafficTrap.setStatus(
        "current"
    )

panThreatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 4)
)
panThreatTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSource"),
        ("PAN-TRAPS", "panDestination"),
        ("PAN-TRAPS", "panNatSource"),
        ("PAN-TRAPS", "panNatDestination"),
        ("PAN-TRAPS", "panRule"),
        ("PAN-TRAPS", "panSrcUser"),
        ("PAN-TRAPS", "panDstUser"),
        ("PAN-TRAPS", "panApplication"),
        ("PAN-TRAPS", "panSourceZone"),
        ("PAN-TRAPS", "panDestinationZone"),
        ("PAN-TRAPS", "panIngressInterface"),
        ("PAN-TRAPS", "panEgressInterface"),
        ("PAN-TRAPS", "panLogForwardingProfile"),
        ("PAN-TRAPS", "panSessionID"),
        ("PAN-TRAPS", "panRepeatCount"),
        ("PAN-TRAPS", "panSourcePort"),
        ("PAN-TRAPS", "panDestinationPort"),
        ("PAN-TRAPS", "panNatSourcePort"),
        ("PAN-TRAPS", "panNatDestinationPort"),
        ("PAN-TRAPS", "panFlags"),
        ("PAN-TRAPS", "panProtocol"),
        ("PAN-TRAPS", "panAction"),
        ("PAN-TRAPS", "panTimeGenerated"),
        ("PAN-TRAPS", "panSrcloc"),
        ("PAN-TRAPS", "panDstloc"),
        ("PAN-TRAPS", "panThreatId"),
        ("PAN-TRAPS", "panThreatCategory"),
        ("PAN-TRAPS", "panThreatContentType"),
        ("PAN-TRAPS", "panThreatSeverity"),
        ("PAN-TRAPS", "panThreatDirection"),
        ("PAN-TRAPS", "panMiscellaneous"),
        ("PAN-TRAPS", "panPcapId"),
        ("PAN-TRAPS", "panFileDigest"),
        ("PAN-TRAPS", "panCloud"),
        ("PAN-TRAPS", "panUrlIndex"),
        ("PAN-TRAPS", "panUserAgent"),
        ("PAN-TRAPS", "panXff"),
        ("PAN-TRAPS", "panReferer"),
        ("PAN-TRAPS", "panSender"),
        ("PAN-TRAPS", "panSubject"),
        ("PAN-TRAPS", "panRecipient"),
        ("PAN-TRAPS", "panReportId"),
        ("PAN-TRAPS", "panFileType"))
)
if mibBuilder.loadTexts:
    panThreatTrap.setStatus(
        "current"
    )

panHipMatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 5)
)
panHipMatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panHipSourceUser"),
        ("PAN-TRAPS", "panHipMachineName"),
        ("PAN-TRAPS", "panHipSource"),
        ("PAN-TRAPS", "panHipMatch"),
        ("PAN-TRAPS", "panHipMatchType"),
        ("PAN-TRAPS", "panHipRepeatCount"),
        ("PAN-TRAPS", "panHipOS"))
)
if mibBuilder.loadTexts:
    panHipMatchTrap.setStatus(
        "current"
    )

panCryptoCertExpiryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 100)
)
panCryptoCertExpiryTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoCertExpiryTrap.setStatus(
        "current"
    )

panCryptoMkeyExpiryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 101)
)
panCryptoMkeyExpiryTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoMkeyExpiryTrap.setStatus(
        "current"
    )

panCryptoMkeyExpiryReminderTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 102)
)
panCryptoMkeyExpiryReminderTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoMkeyExpiryReminderTrap.setStatus(
        "current"
    )

panCryptoHSMStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 103)
)
panCryptoHSMStateChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoHSMStateChangeTrap.setStatus(
        "current"
    )

panCryptoPrivateKeyExportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 104)
)
panCryptoPrivateKeyExportTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panCryptoPrivateKeyExportTrap.setStatus(
        "current"
    )

panDHCPLeaseStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 200)
)
panDHCPLeaseStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPLeaseStartTrap.setStatus(
        "current"
    )

panDHCPLeaseEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 201)
)
panDHCPLeaseEndTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPLeaseEndTrap.setStatus(
        "current"
    )

panDHCPServerOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 202)
)
panDHCPServerOnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPServerOnTrap.setStatus(
        "current"
    )

panDHCPServerAutoProbeOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 203)
)
panDHCPServerAutoProbeOnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPServerAutoProbeOnTrap.setStatus(
        "current"
    )

panDHCPServerAutoProbeOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 204)
)
panDHCPServerAutoProbeOffTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPServerAutoProbeOffTrap.setStatus(
        "current"
    )

panDHCPServerNoFreeIpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 205)
)
panDHCPServerNoFreeIpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPServerNoFreeIpTrap.setStatus(
        "current"
    )

panDHCPIpAlreadyInUseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 206)
)
panDHCPIpAlreadyInUseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIpAlreadyInUseTrap.setStatus(
        "current"
    )

panDHCPRelayOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 207)
)
panDHCPRelayOnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPRelayOnTrap.setStatus(
        "current"
    )

panDHCPRelayOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 208)
)
panDHCPRelayOffTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPRelayOffTrap.setStatus(
        "current"
    )

panDHCPRelay6OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 209)
)
panDHCPRelay6OnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPRelay6OnTrap.setStatus(
        "current"
    )

panDHCPRelay6OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 210)
)
panDHCPRelay6OffTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPRelay6OffTrap.setStatus(
        "current"
    )

panDHCPIfUpdateFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 211)
)
panDHCPIfUpdateFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfUpdateFailTrap.setStatus(
        "current"
    )

panDHCPIfUpdateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 212)
)
panDHCPIfUpdateOkTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfUpdateOkTrap.setStatus(
        "current"
    )

panDHCPIfClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 213)
)
panDHCPIfClearTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfClearTrap.setStatus(
        "current"
    )

panDHCPIfRenewTriggerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 214)
)
panDHCPIfRenewTriggerTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfRenewTriggerTrap.setStatus(
        "current"
    )

panDHCPIfReleaseTriggerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 215)
)
panDHCPIfReleaseTriggerTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfReleaseTriggerTrap.setStatus(
        "current"
    )

panDHCPIfRcvNakTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 216)
)
panDHCPIfRcvNakTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfRcvNakTrap.setStatus(
        "current"
    )

panDHCPIfInheritTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 217)
)
panDHCPIfInheritTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfInheritTrap.setStatus(
        "current"
    )

panDHCPIfDuplicateIpIntfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 218)
)
panDHCPIfDuplicateIpIntfTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfDuplicateIpIntfTrap.setStatus(
        "current"
    )

panDHCPIfDuplicateIpRemoteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 219)
)
panDHCPIfDuplicateIpRemoteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDHCPIfDuplicateIpRemoteTrap.setStatus(
        "current"
    )

panDNSProxyCacheClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 300)
)
panDNSProxyCacheClearedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyCacheClearedTrap.setStatus(
        "current"
    )

panDNSProxyResolveFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 301)
)
panDNSProxyResolveFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyResolveFailTrap.setStatus(
        "current"
    )

panDNSProxyObjectEnableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 302)
)
panDNSProxyObjectEnableTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyObjectEnableTrap.setStatus(
        "current"
    )

panDNSProxyIfAddTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 303)
)
panDNSProxyIfAddTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyIfAddTrap.setStatus(
        "current"
    )

panDNSProxyIfDelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 304)
)
panDNSProxyIfDelTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyIfDelTrap.setStatus(
        "current"
    )

panDNSProxyIfInheritTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 305)
)
panDNSProxyIfInheritTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDNSProxyIfInheritTrap.setStatus(
        "current"
    )

panDOSDosRuleChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 500)
)
panDOSDosRuleChangedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panDOSDosRuleChangedTrap.setStatus(
        "current"
    )

panGeneralGeneralTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 600)
)
panGeneralGeneralTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralGeneralTrap.setStatus(
        "current"
    )

panGeneralSystemStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 601)
)
panGeneralSystemStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralSystemStartTrap.setStatus(
        "current"
    )

panGeneralSystemShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 602)
)
panGeneralSystemShutdownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralSystemShutdownTrap.setStatus(
        "current"
    )

panGeneralAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 603)
)
panGeneralAuthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralAuthFailTrap.setStatus(
        "current"
    )

panGeneralAuthSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 604)
)
panGeneralAuthSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralAuthSuccessTrap.setStatus(
        "current"
    )

panGeneralTacLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 605)
)
panGeneralTacLoginTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralTacLoginTrap.setStatus(
        "current"
    )

panGeneralAuthServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 606)
)
panGeneralAuthServerDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGeneralAuthServerDownTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayRegistSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 700)
)
panGlobalProtectGatewayRegistSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayRegistSuccTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayRegistFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 701)
)
panGlobalProtectGatewayRegistFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayRegistFailTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayLogoutSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 702)
)
panGlobalProtectGatewayLogoutSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayLogoutSuccTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayLogoutFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 703)
)
panGlobalProtectGatewayLogoutFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayLogoutFailTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayConfigSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 704)
)
panGlobalProtectGatewayConfigSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayConfigSuccTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayConfigFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 705)
)
panGlobalProtectGatewayConfigFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayConfigFailTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayConfigReleaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 706)
)
panGlobalProtectGatewayConfigReleaseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayConfigReleaseTrap.setStatus(
        "current"
    )

panGlobalProtectGatewaySwitchSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 707)
)
panGlobalProtectGatewaySwitchSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewaySwitchSuccTrap.setStatus(
        "current"
    )

panGlobalProtectGatewaySwitchFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 708)
)
panGlobalProtectGatewaySwitchFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewaySwitchFailTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayAuthSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 709)
)
panGlobalProtectGatewayAuthSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayAuthSuccTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 710)
)
panGlobalProtectGatewayAuthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayAuthFailTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayAgentMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 711)
)
panGlobalProtectGatewayAgentMsgTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayAgentMsgTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayInvalidLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 712)
)
panGlobalProtectGatewayInvalidLicenseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayInvalidLicenseTrap.setStatus(
        "current"
    )

panGlobalProtectGatewayInheritanceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 713)
)
panGlobalProtectGatewayInheritanceTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectGatewayInheritanceTrap.setStatus(
        "current"
    )

panGlobalProtectPortalConfigSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 714)
)
panGlobalProtectPortalConfigSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectPortalConfigSuccTrap.setStatus(
        "current"
    )

panGlobalProtectPortalConfigFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 715)
)
panGlobalProtectPortalConfigFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectPortalConfigFailTrap.setStatus(
        "current"
    )

panGlobalProtectPortalAuthSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 716)
)
panGlobalProtectPortalAuthSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectPortalAuthSuccTrap.setStatus(
        "current"
    )

panGlobalProtectPortalAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 717)
)
panGlobalProtectPortalAuthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalProtectPortalAuthFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewaySatauthSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 718)
)
panGlobalprotectgatewaySatauthSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewaySatauthSuccTrap.setStatus(
        "current"
    )

panGlobalprotectgatewaySatauthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 719)
)
panGlobalprotectgatewaySatauthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewaySatauthFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayRouteAddFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 720)
)
panGlobalprotectgatewayRouteAddFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayRouteAddFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayRouteResetFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 721)
)
panGlobalprotectgatewayRouteResetFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayRouteResetFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 722)
)
panGlobalprotectgatewayTunUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunUpTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 723)
)
panGlobalprotectgatewayTunDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunDownTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayDupSubnetsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 724)
)
panGlobalprotectgatewayDupSubnetsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayDupSubnetsTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayDeniedRoutesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 725)
)
panGlobalprotectgatewayDeniedRoutesTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayDeniedRoutesTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunMonDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 726)
)
panGlobalprotectgatewayTunMonDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunMonDownTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunMonUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 727)
)
panGlobalprotectgatewayTunMonUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunMonUpTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatconfigSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 728)
)
panGlobalprotectportalSatconfigSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatconfigSuccTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatconfigFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 729)
)
panGlobalprotectportalSatconfigFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatconfigFailTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatauthSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 730)
)
panGlobalprotectportalSatauthSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatauthSuccTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatauthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 731)
)
panGlobalprotectportalSatauthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatauthFailTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatcertSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 732)
)
panGlobalprotectportalSatcertSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatcertSuccTrap.setStatus(
        "current"
    )

panGlobalprotectportalSatcertFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 733)
)
panGlobalprotectportalSatcertFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalSatcertFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunHardlifetimeExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 734)
)
panGlobalprotectgatewayTunHardlifetimeExpiredTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunHardlifetimeExpiredTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayTunDpInstallErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 735)
)
panGlobalprotectgatewayTunDpInstallErrTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayTunDpInstallErrTrap.setStatus(
        "current"
    )

panGlobalprotectportalGenportalcookieSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 736)
)
panGlobalprotectportalGenportalcookieSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalGenportalcookieSuccTrap.setStatus(
        "current"
    )

panGlobalprotectportalGenportalcookieFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 737)
)
panGlobalprotectportalGenportalcookieFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectportalGenportalcookieFailTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayFramedIpSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 738)
)
panGlobalprotectgatewayFramedIpSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayFramedIpSuccTrap.setStatus(
        "current"
    )

panGlobalprotectgatewayFramedIpFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 739)
)
panGlobalprotectgatewayFramedIpFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panGlobalprotectgatewayFramedIpFailTrap.setStatus(
        "current"
    )

panHAPreemptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 800)
)
panHAPreemptTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPreemptTrap.setStatus(
        "current"
    )

panHAStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 801)
)
panHAStateChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAStateChangeTrap.setStatus(
        "current"
    )

panHAStateOverrideTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 802)
)
panHAStateOverrideTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAStateOverrideTrap.setStatus(
        "current"
    )

panHADataplaneDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 803)
)
panHADataplaneDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHADataplaneDownTrap.setStatus(
        "current"
    )

panHAPolicyPushFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 804)
)
panHAPolicyPushFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPolicyPushFailTrap.setStatus(
        "current"
    )

panHAHa1LinkChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 805)
)
panHAHa1LinkChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAHa1LinkChangeTrap.setStatus(
        "current"
    )

panHAHa2LinkChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 806)
)
panHAHa2LinkChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAHa2LinkChangeTrap.setStatus(
        "current"
    )

panHAConnectChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 807)
)
panHAConnectChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAConnectChangeTrap.setStatus(
        "current"
    )

panHAPathMonitorDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 808)
)
panHAPathMonitorDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPathMonitorDownTrap.setStatus(
        "current"
    )

panHALinkMonitorDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 809)
)
panHALinkMonitorDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHALinkMonitorDownTrap.setStatus(
        "current"
    )

panHAHa3LinkChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 810)
)
panHAHa3LinkChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAHa3LinkChangeTrap.setStatus(
        "current"
    )

panHAPathMonitorUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 811)
)
panHAPathMonitorUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPathMonitorUpTrap.setStatus(
        "current"
    )

panHALinkMonitorUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 812)
)
panHALinkMonitorUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHALinkMonitorUpTrap.setStatus(
        "current"
    )

panHAPeerSyncFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 813)
)
panHAPeerSyncFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerSyncFailureTrap.setStatus(
        "current"
    )

panHAConfigFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 814)
)
panHAConfigFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAConfigFailureTrap.setStatus(
        "current"
    )

panHAConfigNotSynchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 815)
)
panHAConfigNotSynchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAConfigNotSynchTrap.setStatus(
        "current"
    )

panHAPeerErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 816)
)
panHAPeerErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerErrorTrap.setStatus(
        "current"
    )

panHAPre13Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 817)
)
panHAPre13Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPre13Trap.setStatus(
        "current"
    )

panHAPre20Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 818)
)
panHAPre20Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPre20Trap.setStatus(
        "current"
    )

panHAPeerVersionMatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 819)
)
panHAPeerVersionMatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerVersionMatchTrap.setStatus(
        "current"
    )

panHAPeerVersionSupportedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 820)
)
panHAPeerVersionSupportedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerVersionSupportedTrap.setStatus(
        "current"
    )

panHAPeerVersionUnsupportedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 821)
)
panHAPeerVersionUnsupportedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerVersionUnsupportedTrap.setStatus(
        "current"
    )

panHAPeerVersionDegradedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 822)
)
panHAPeerVersionDegradedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerVersionDegradedTrap.setStatus(
        "current"
    )

panHAPeerCompatMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 823)
)
panHAPeerCompatMismatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerCompatMismatchTrap.setStatus(
        "current"
    )

panHAPeerCompatMatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 824)
)
panHAPeerCompatMatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerCompatMatchTrap.setStatus(
        "current"
    )

panHAPeerCompatFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 825)
)
panHAPeerCompatFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerCompatFailTrap.setStatus(
        "current"
    )

panHAPeerSplitBrainTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 826)
)
panHAPeerSplitBrainTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerSplitBrainTrap.setStatus(
        "current"
    )

panHASplitBrainTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 827)
)
panHASplitBrainTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASplitBrainTrap.setStatus(
        "current"
    )

panHAPreemptLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 828)
)
panHAPreemptLoopTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPreemptLoopTrap.setStatus(
        "current"
    )

panHANonFunctionalLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 829)
)
panHANonFunctionalLoopTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHANonFunctionalLoopTrap.setStatus(
        "current"
    )

panHAPeerShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 830)
)
panHAPeerShutdownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAPeerShutdownTrap.setStatus(
        "current"
    )

panHANfsPanlogsFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 831)
)
panHANfsPanlogsFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHANfsPanlogsFailTrap.setStatus(
        "current"
    )

panHAInternalHaErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 832)
)
panHAInternalHaErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAInternalHaErrorTrap.setStatus(
        "current"
    )

panHASystemFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 833)
)
panHASystemFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASystemFailureTrap.setStatus(
        "current"
    )

panHAHa2KeepAliveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 834)
)
panHAHa2KeepAliveTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHAHa2KeepAliveTrap.setStatus(
        "current"
    )

panHASlotFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 835)
)
panHASlotFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASlotFailureTrap.setStatus(
        "current"
    )

panHASlotMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 836)
)
panHASlotMismatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASlotMismatchTrap.setStatus(
        "current"
    )

panHASlotControlFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 837)
)
panHASlotControlFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASlotControlFailureTrap.setStatus(
        "current"
    )

panHASlotControlEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 838)
)
panHASlotControlEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASlotControlEventTrap.setStatus(
        "current"
    )

panHASessionSynchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 839)
)
panHASessionSynchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHASessionSynchTrap.setStatus(
        "current"
    )

panHWDiskErrorsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 900)
)
panHWDiskErrorsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWDiskErrorsTrap.setStatus(
        "current"
    )

panHWSlotUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 901)
)
panHWSlotUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotUpTrap.setStatus(
        "current"
    )

panHWInsufficientPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 902)
)
panHWInsufficientPowerTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWInsufficientPowerTrap.setStatus(
        "current"
    )

panHWSlotUnsupportedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 903)
)
panHWSlotUnsupportedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotUnsupportedTrap.setStatus(
        "current"
    )

panHWSlotStartingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 904)
)
panHWSlotStartingTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotStartingTrap.setStatus(
        "current"
    )

panHWSlotStoppingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 905)
)
panHWSlotStoppingTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotStoppingTrap.setStatus(
        "current"
    )

panHWSlotFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 906)
)
panHWSlotFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotFailureTrap.setStatus(
        "current"
    )

panHWSlotPoweroffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 907)
)
panHWSlotPoweroffTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotPoweroffTrap.setStatus(
        "current"
    )

panHWSlotAdminpoweroffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 908)
)
panHWSlotAdminpoweroffTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotAdminpoweroffTrap.setStatus(
        "current"
    )

panHWSlotInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 909)
)
panHWSlotInsertedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotInsertedTrap.setStatus(
        "current"
    )

panHWSlotRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 910)
)
panHWSlotRemovedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWSlotRemovedTrap.setStatus(
        "current"
    )

panHWPsInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 911)
)
panHWPsInsertedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWPsInsertedTrap.setStatus(
        "current"
    )

panHWPsRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 912)
)
panHWPsRemovedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWPsRemovedTrap.setStatus(
        "current"
    )

panHWPsFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 913)
)
panHWPsFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWPsFailureTrap.setStatus(
        "current"
    )

panHWFanInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 914)
)
panHWFanInsertedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWFanInsertedTrap.setStatus(
        "current"
    )

panHWFanRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 915)
)
panHWFanRemovedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWFanRemovedTrap.setStatus(
        "current"
    )

panHWFanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 916)
)
panHWFanFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panHWFanFailureTrap.setStatus(
        "current"
    )

panNTDPRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1000)
)
panNTDPRestartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panNTDPRestartTrap.setStatus(
        "current"
    )

panNTDPTimeLearnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1001)
)
panNTDPTimeLearnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panNTDPTimeLearnTrap.setStatus(
        "current"
    )

panNTDPSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1002)
)
panNTDPSyncTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panNTDPSyncTrap.setStatus(
        "current"
    )

panNTDPAuthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1003)
)
panNTDPAuthTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panNTDPAuthTrap.setStatus(
        "current"
    )

panPBFNhUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1100)
)
panPBFNhUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPBFNhUpTrap.setStatus(
        "current"
    )

panPBFNhDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1101)
)
panPBFNhDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPBFNhDownTrap.setStatus(
        "current"
    )

panPORTLinkChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1200)
)
panPORTLinkChangeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTLinkChangeTrap.setStatus(
        "current"
    )

panPORTNonqualSfpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1201)
)
panPORTNonqualSfpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTNonqualSfpTrap.setStatus(
        "current"
    )

panPORTNonqualSfpPlusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1202)
)
panPORTNonqualSfpPlusTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTNonqualSfpPlusTrap.setStatus(
        "current"
    )

panPORTNonqualXfpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1203)
)
panPORTNonqualXfpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTNonqualXfpTrap.setStatus(
        "current"
    )

panPORTNonsuppForcedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1204)
)
panPORTNonsuppForcedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPORTNonsuppForcedTrap.setStatus(
        "current"
    )

panPPPOEInitiateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1300)
)
panPPPOEInitiateTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPPPOEInitiateTrap.setStatus(
        "current"
    )

panPPPOEConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1301)
)
panPPPOEConnectTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPPPOEConnectTrap.setStatus(
        "current"
    )

panPPPOEConnectFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1302)
)
panPPPOEConnectFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPPPOEConnectFailTrap.setStatus(
        "current"
    )

panPPPOETerminateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1303)
)
panPPPOETerminateTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPPPOETerminateTrap.setStatus(
        "current"
    )

panPPPOEIfUpdateFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1304)
)
panPPPOEIfUpdateFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panPPPOEIfUpdateFailTrap.setStatus(
        "current"
    )

panRASRasmgrConfigP1SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1400)
)
panRASRasmgrConfigP1SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrConfigP1SuccessTrap.setStatus(
        "current"
    )

panRASRasmgrConfigP1FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1401)
)
panRASRasmgrConfigP1FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrConfigP1FailedTrap.setStatus(
        "current"
    )

panRASRasmgrConfigP1AbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1402)
)
panRASRasmgrConfigP1AbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrConfigP1AbortTrap.setStatus(
        "current"
    )

panRASRasmgrConfigP2SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1403)
)
panRASRasmgrConfigP2SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrConfigP2SuccessTrap.setStatus(
        "current"
    )

panRASRasmgrConfigP2FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1404)
)
panRASRasmgrConfigP2FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrConfigP2FailedTrap.setStatus(
        "current"
    )

panRASRasmgrDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1405)
)
panRASRasmgrDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrDaemonStartTrap.setStatus(
        "current"
    )

panRASRasmgrDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1406)
)
panRASRasmgrDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrDaemonExitTrap.setStatus(
        "current"
    )

panRASRasmgrDaemonInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1407)
)
panRASRasmgrDaemonInitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrDaemonInitTrap.setStatus(
        "current"
    )

panRASRasmgrFlowFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1408)
)
panRASRasmgrFlowFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrFlowFullSyncStartTrap.setStatus(
        "current"
    )

panRASRasmgrFlowFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1409)
)
panRASRasmgrFlowFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrFlowFullSyncAbortTrap.setStatus(
        "current"
    )

panRASRasmgrFlowFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1410)
)
panRASRasmgrFlowFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrFlowFullSyncDoneTrap.setStatus(
        "current"
    )

panRASRasmgrHaFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1411)
)
panRASRasmgrHaFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrHaFullSyncStartTrap.setStatus(
        "current"
    )

panRASRasmgrHaFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1412)
)
panRASRasmgrHaFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrHaFullSyncAbortTrap.setStatus(
        "current"
    )

panRASRasmgrHaFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1413)
)
panRASRasmgrHaFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRASRasmgrHaFullSyncDoneTrap.setStatus(
        "current"
    )

panROUTINGRoutedConfigP1SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1500)
)
panROUTINGRoutedConfigP1SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedConfigP1SuccessTrap.setStatus(
        "current"
    )

panROUTINGRoutedConfigP1FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1501)
)
panROUTINGRoutedConfigP1FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedConfigP1FailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedConfigP1AbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1502)
)
panROUTINGRoutedConfigP1AbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedConfigP1AbortTrap.setStatus(
        "current"
    )

panROUTINGRoutedConfigP2SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1503)
)
panROUTINGRoutedConfigP2SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedConfigP2SuccessTrap.setStatus(
        "current"
    )

panROUTINGRoutedConfigP2FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1504)
)
panROUTINGRoutedConfigP2FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedConfigP2FailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1505)
)
panROUTINGRoutedDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedDaemonStartTrap.setStatus(
        "current"
    )

panROUTINGRoutedDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1506)
)
panROUTINGRoutedDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedDaemonExitTrap.setStatus(
        "current"
    )

panROUTINGRoutedDaemonInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1507)
)
panROUTINGRoutedDaemonInitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedDaemonInitTrap.setStatus(
        "current"
    )

panROUTINGRoutedFibSyncPeerBackupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1508)
)
panROUTINGRoutedFibSyncPeerBackupTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedFibSyncPeerBackupTrap.setStatus(
        "current"
    )

panROUTINGRoutedFibSyncSelfMasterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1509)
)
panROUTINGRoutedFibSyncSelfMasterTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedFibSyncSelfMasterTrap.setStatus(
        "current"
    )

panROUTINGRoutedRTMBadRouteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1510)
)
panROUTINGRoutedRTMBadRouteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRTMBadRouteTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFLSAChksumFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1511)
)
panROUTINGRoutedOSPFLSAChksumFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFLSAChksumFailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFLSAChksumInvalidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1512)
)
panROUTINGRoutedOSPFLSAChksumInvalidTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFLSAChksumInvalidTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFAuthtypeBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1513)
)
panROUTINGRoutedOSPFAuthtypeBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFAuthtypeBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFPasswordBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1514)
)
panROUTINGRoutedOSPFPasswordBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFPasswordBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFChksumBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1515)
)
panROUTINGRoutedOSPFChksumBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFChksumBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFSequenceBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1516)
)
panROUTINGRoutedOSPFSequenceBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFSequenceBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFMd5chksumBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1517)
)
panROUTINGRoutedOSPFMd5chksumBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFMd5chksumBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFMd5lengthBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1518)
)
panROUTINGRoutedOSPFMd5lengthBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFMd5lengthBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFHelloHelloIntvalBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1519)
)
panROUTINGRoutedOSPFHelloHelloIntvalBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFHelloHelloIntvalBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFHelloDeadIntvalBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1520)
)
panROUTINGRoutedOSPFHelloDeadIntvalBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFHelloDeadIntvalBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFHelloNetmaskBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1521)
)
panROUTINGRoutedOSPFHelloNetmaskBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFHelloNetmaskBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFHelloAreaTypeBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1522)
)
panROUTINGRoutedOSPFHelloAreaTypeBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFHelloAreaTypeBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFNeighbor2dirTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1523)
)
panROUTINGRoutedOSPFNeighbor2dirTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFNeighbor2dirTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFNeighborFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1524)
)
panROUTINGRoutedOSPFNeighborFullTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFNeighborFullTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFNeighborDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1525)
)
panROUTINGRoutedOSPFNeighborDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFNeighborDownTrap.setStatus(
        "current"
    )

panROUTINGRoutedRIPPeerAddTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1526)
)
panROUTINGRoutedRIPPeerAddTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRIPPeerAddTrap.setStatus(
        "current"
    )

panROUTINGRoutedRIPPeerDelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1527)
)
panROUTINGRoutedRIPPeerDelTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRIPPeerDelTrap.setStatus(
        "current"
    )

panROUTINGRoutedRIPAuthtypeBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1528)
)
panROUTINGRoutedRIPAuthtypeBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRIPAuthtypeBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedRIPAuthFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1529)
)
panROUTINGRoutedRIPAuthFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRIPAuthFailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedRIPMd5lengthBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1530)
)
panROUTINGRoutedRIPMd5lengthBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedRIPMd5lengthBadTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPPeerEnterEstablishedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1531)
)
panROUTINGRoutedBGPPeerEnterEstablishedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPPeerEnterEstablishedTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPPeerLeftEstablishedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1532)
)
panROUTINGRoutedBGPPeerLeftEstablishedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPPeerLeftEstablishedTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPPeerFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1533)
)
panROUTINGRoutedBGPPeerFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPPeerFailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPPeerRestartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1534)
)
panROUTINGRoutedBGPPeerRestartedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPPeerRestartedTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPPeerRestartFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1535)
)
panROUTINGRoutedBGPPeerRestartFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPPeerRestartFailedTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPRefreshSentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1536)
)
panROUTINGRoutedBGPRefreshSentTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPRefreshSentTrap.setStatus(
        "current"
    )

panROUTINGRoutedBGPRibinRecalcTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1537)
)
panROUTINGRoutedBGPRibinRecalcTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedBGPRibinRecalcTrap.setStatus(
        "current"
    )

panROUTINGRoutedPIMInterfaceStateChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1538)
)
panROUTINGRoutedPIMInterfaceStateChangedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedPIMInterfaceStateChangedTrap.setStatus(
        "current"
    )

panROUTINGRoutedPIMNewDrElectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1539)
)
panROUTINGRoutedPIMNewDrElectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedPIMNewDrElectedTrap.setStatus(
        "current"
    )

panROUTINGRoutedPIMNeighborDiscoveredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1540)
)
panROUTINGRoutedPIMNeighborDiscoveredTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedPIMNeighborDiscoveredTrap.setStatus(
        "current"
    )

panROUTINGRoutedPIMNeighborDisappearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1541)
)
panROUTINGRoutedPIMNeighborDisappearedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedPIMNeighborDisappearedTrap.setStatus(
        "current"
    )

panROUTINGRoutedIGMPWrongVersionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1542)
)
panROUTINGRoutedIGMPWrongVersionTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedIGMPWrongVersionTrap.setStatus(
        "current"
    )

panROUTINGRoutedGenericEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1543)
)
panROUTINGRoutedGenericEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedGenericEventTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFStartGracefulRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1544)
)
panROUTINGRoutedOSPFStartGracefulRestartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFStartGracefulRestartTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFStoppedGracefulRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1545)
)
panROUTINGRoutedOSPFStoppedGracefulRestartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFStoppedGracefulRestartTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFStartHelperNodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1546)
)
panROUTINGRoutedOSPFStartHelperNodeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFStartHelperNodeTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFStopHelperModeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1547)
)
panROUTINGRoutedOSPFStopHelperModeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFStopHelperModeTrap.setStatus(
        "current"
    )

panROUTINGRoutedOSPFNotHelpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1548)
)
panROUTINGRoutedOSPFNotHelpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedOSPFNotHelpTrap.setStatus(
        "current"
    )

panROUTINGRoutedECMPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1549)
)
panROUTINGRoutedECMPTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panROUTINGRoutedECMPTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnRegistSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1600)
)
panSSLVPNSslvpnRegistSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnRegistSuccTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnRegistFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1601)
)
panSSLVPNSslvpnRegistFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnRegistFailTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnLogoutSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1602)
)
panSSLVPNSslvpnLogoutSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnLogoutSuccTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnLogoutFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1603)
)
panSSLVPNSslvpnLogoutFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnLogoutFailTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnConfigSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1604)
)
panSSLVPNSslvpnConfigSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnConfigSuccTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnConfigFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1605)
)
panSSLVPNSslvpnConfigFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnConfigFailTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnConfigReleaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1606)
)
panSSLVPNSslvpnConfigReleaseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnConfigReleaseTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnSwitchSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1607)
)
panSSLVPNSslvpnSwitchSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnSwitchSuccTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnSwitchFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1608)
)
panSSLVPNSslvpnSwitchFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnSwitchFailTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnAuthSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1609)
)
panSSLVPNSslvpnAuthSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnAuthSuccTrap.setStatus(
        "current"
    )

panSSLVPNSslvpnAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1610)
)
panSSLVPNSslvpnAuthFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLVPNSslvpnAuthFailTrap.setStatus(
        "current"
    )

panVPNIkeConfigP1SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1700)
)
panVPNIkeConfigP1SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeConfigP1SuccessTrap.setStatus(
        "current"
    )

panVPNIkeConfigP1FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1701)
)
panVPNIkeConfigP1FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeConfigP1FailedTrap.setStatus(
        "current"
    )

panVPNIkeConfigP1AbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1702)
)
panVPNIkeConfigP1AbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeConfigP1AbortTrap.setStatus(
        "current"
    )

panVPNIkeConfigP2SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1703)
)
panVPNIkeConfigP2SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeConfigP2SuccessTrap.setStatus(
        "current"
    )

panVPNIkeConfigP2FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1704)
)
panVPNIkeConfigP2FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeConfigP2FailedTrap.setStatus(
        "current"
    )

panVPNIkeDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1705)
)
panVPNIkeDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeDaemonStartTrap.setStatus(
        "current"
    )

panVPNIkeDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1706)
)
panVPNIkeDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeDaemonExitTrap.setStatus(
        "current"
    )

panVPNIkeDaemonInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1707)
)
panVPNIkeDaemonInitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeDaemonInitTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1StartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1708)
)
panVPNIkeNegoP1StartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1StartTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1FailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1709)
)
panVPNIkeNegoP1FailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1FailTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1SuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1710)
)
panVPNIkeNegoP1SuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1SuccTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1ExpireTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1711)
)
panVPNIkeNegoP1ExpireTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1ExpireTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1712)
)
panVPNIkeNegoP1DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1DeleteTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1DpdDnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1713)
)
panVPNIkeNegoP1DpdDnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1DpdDnTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1PskIdtypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1714)
)
panVPNIkeNegoP1PskIdtypeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1PskIdtypeTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1FailPskTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1715)
)
panVPNIkeNegoP1FailPskTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1FailPskTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1FailCommonTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1716)
)
panVPNIkeNegoP1FailCommonTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1FailCommonTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2StartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1717)
)
panVPNIkeNegoP2StartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2StartTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2FailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1718)
)
panVPNIkeNegoP2FailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2FailTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2SuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1719)
)
panVPNIkeNegoP2SuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2SuccTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2StaleP1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1720)
)
panVPNIkeNegoP2StaleP1Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2StaleP1Trap.setStatus(
        "current"
    )

panVPNIkeNegoP2DupRekeyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1721)
)
panVPNIkeNegoP2DupRekeyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2DupRekeyTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2SimulContTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1722)
)
panVPNIkeNegoP2SimulContTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2SimulContTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2SimulFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1723)
)
panVPNIkeNegoP2SimulFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2SimulFailTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2SimulDelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1724)
)
panVPNIkeNegoP2SimulDelayTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2SimulDelayTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2NoP1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1725)
)
panVPNIkeNegoP2NoP1Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2NoP1Trap.setStatus(
        "current"
    )

panVPNIkeNegoP2P1NotReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1726)
)
panVPNIkeNegoP2P1NotReadyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2P1NotReadyTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2ProxyIdBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1727)
)
panVPNIkeNegoP2ProxyIdBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2ProxyIdBadTrap.setStatus(
        "current"
    )

panVPNIkeNegoP2ProposalBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1728)
)
panVPNIkeNegoP2ProposalBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP2ProposalBadTrap.setStatus(
        "current"
    )

panVPNIpsecKeyInstallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1729)
)
panVPNIpsecKeyInstallTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIpsecKeyInstallTrap.setStatus(
        "current"
    )

panVPNIpsecKeyDeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1730)
)
panVPNIpsecKeyDeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIpsecKeyDeleteTrap.setStatus(
        "current"
    )

panVPNIpsecKeyExpireTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1731)
)
panVPNIpsecKeyExpireTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIpsecKeyExpireTrap.setStatus(
        "current"
    )

panVPNIkeRecvNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1732)
)
panVPNIkeRecvNotifyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeRecvNotifyTrap.setStatus(
        "current"
    )

panVPNIkeRecvP1DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1733)
)
panVPNIkeRecvP1DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeRecvP1DeleteTrap.setStatus(
        "current"
    )

panVPNIkeRecvP2DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1734)
)
panVPNIkeRecvP2DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeRecvP2DeleteTrap.setStatus(
        "current"
    )

panVPNIkeSendNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1735)
)
panVPNIkeSendNotifyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeSendNotifyTrap.setStatus(
        "current"
    )

panVPNIkeSendP1DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1736)
)
panVPNIkeSendP1DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeSendP1DeleteTrap.setStatus(
        "current"
    )

panVPNIkeSendP2DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1737)
)
panVPNIkeSendP2DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeSendP2DeleteTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1738)
)
panVPNIkev2NegoIkeStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeStartTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1739)
)
panVPNIkev2NegoIkeFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeFailTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1740)
)
panVPNIkev2NegoIkeSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeSuccTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeExpireTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1741)
)
panVPNIkev2NegoIkeExpireTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeExpireTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeDeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1742)
)
panVPNIkev2NegoIkeDeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeDeleteTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1743)
)
panVPNIkev2NegoChildStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildStartTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1744)
)
panVPNIkev2NegoChildFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildFailTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1745)
)
panVPNIkev2NegoChildSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildSuccTrap.setStatus(
        "current"
    )

panVPNTunnelStatusUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1746)
)
panVPNTunnelStatusUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNTunnelStatusUpTrap.setStatus(
        "current"
    )

panVPNTunnelStatusDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1747)
)
panVPNTunnelStatusDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNTunnelStatusDownTrap.setStatus(
        "current"
    )

panVPNKeymgrDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1748)
)
panVPNKeymgrDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrDaemonStartTrap.setStatus(
        "current"
    )

panVPNKeymgrDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1749)
)
panVPNKeymgrDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrDaemonExitTrap.setStatus(
        "current"
    )

panVPNKeymgrDaemonInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1750)
)
panVPNKeymgrDaemonInitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrDaemonInitTrap.setStatus(
        "current"
    )

panVPNKeymgrFlowFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1751)
)
panVPNKeymgrFlowFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrFlowFullSyncStartTrap.setStatus(
        "current"
    )

panVPNKeymgrFlowFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1752)
)
panVPNKeymgrFlowFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrFlowFullSyncAbortTrap.setStatus(
        "current"
    )

panVPNKeymgrFlowFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1753)
)
panVPNKeymgrFlowFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrFlowFullSyncDoneTrap.setStatus(
        "current"
    )

panVPNKeymgrIkeFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1754)
)
panVPNKeymgrIkeFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrIkeFullSyncStartTrap.setStatus(
        "current"
    )

panVPNKeymgrIkeFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1755)
)
panVPNKeymgrIkeFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrIkeFullSyncAbortTrap.setStatus(
        "current"
    )

panVPNKeymgrIkeFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1756)
)
panVPNKeymgrIkeFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrIkeFullSyncDoneTrap.setStatus(
        "current"
    )

panVPNKeymgrHaFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1757)
)
panVPNKeymgrHaFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrHaFullSyncStartTrap.setStatus(
        "current"
    )

panVPNKeymgrHaFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1758)
)
panVPNKeymgrHaFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrHaFullSyncAbortTrap.setStatus(
        "current"
    )

panVPNKeymgrHaFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1759)
)
panVPNKeymgrHaFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrHaFullSyncDoneTrap.setStatus(
        "current"
    )

panVPNIkeGenericEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1760)
)
panVPNIkeGenericEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeGenericEventTrap.setStatus(
        "current"
    )

panVPNKeymgrGenericEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1761)
)
panVPNKeymgrGenericEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNKeymgrGenericEventTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1FailCertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1762)
)
panVPNIkeNegoP1FailCertTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1FailCertTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1CertIdMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1763)
)
panVPNIkeNegoP1CertIdMismatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1CertIdMismatchTrap.setStatus(
        "current"
    )

panVPNIkeNegoP1CertSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1764)
)
panVPNIkeNegoP1CertSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkeNegoP1CertSuccTrap.setStatus(
        "current"
    )

panVPNIkev2NegoIkeDpdDnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1765)
)
panVPNIkev2NegoIkeDpdDnTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoIkeDpdDnTrap.setStatus(
        "current"
    )

panVPNIkev2NegoPskIdtypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1766)
)
panVPNIkev2NegoPskIdtypeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoPskIdtypeTrap.setStatus(
        "current"
    )

panVPNIkev2NegoFailPskTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1767)
)
panVPNIkev2NegoFailPskTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoFailPskTrap.setStatus(
        "current"
    )

panVPNIkev2NegoFailCommonTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1768)
)
panVPNIkev2NegoFailCommonTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoFailCommonTrap.setStatus(
        "current"
    )

panVPNIkev2NegoFailCertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1769)
)
panVPNIkev2NegoFailCertTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoFailCertTrap.setStatus(
        "current"
    )

panVPNIkev2NegoCertIdMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1770)
)
panVPNIkev2NegoCertIdMismatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoCertIdMismatchTrap.setStatus(
        "current"
    )

panVPNIkev2NegoCertSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1771)
)
panVPNIkev2NegoCertSuccTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoCertSuccTrap.setStatus(
        "current"
    )

panVPNIkev2NegoUseV1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1772)
)
panVPNIkev2NegoUseV1Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoUseV1Trap.setStatus(
        "current"
    )

panVPNIkev2NegoStaleP1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1773)
)
panVPNIkev2NegoStaleP1Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoStaleP1Trap.setStatus(
        "current"
    )

panVPNIkev2NegoStaleP2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1774)
)
panVPNIkev2NegoStaleP2Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoStaleP2Trap.setStatus(
        "current"
    )

panVPNIkev2NegoChildDupRekeyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1775)
)
panVPNIkev2NegoChildDupRekeyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildDupRekeyTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildSimulContTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1776)
)
panVPNIkev2NegoChildSimulContTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildSimulContTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildSimulFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1777)
)
panVPNIkev2NegoChildSimulFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildSimulFailTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildSimulDelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1778)
)
panVPNIkev2NegoChildSimulDelayTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildSimulDelayTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildNoP1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1779)
)
panVPNIkev2NegoChildNoP1Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildNoP1Trap.setStatus(
        "current"
    )

panVPNIkev2NegoChildP1NotReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1780)
)
panVPNIkev2NegoChildP1NotReadyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildP1NotReadyTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildTsBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1781)
)
panVPNIkev2NegoChildTsBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildTsBadTrap.setStatus(
        "current"
    )

panVPNIkev2NegoChildProposalBadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1782)
)
panVPNIkev2NegoChildProposalBadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2NegoChildProposalBadTrap.setStatus(
        "current"
    )

panVPNIkev2RecvNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1783)
)
panVPNIkev2RecvNotifyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2RecvNotifyTrap.setStatus(
        "current"
    )

panVPNIkev2RecvP1DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1784)
)
panVPNIkev2RecvP1DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2RecvP1DeleteTrap.setStatus(
        "current"
    )

panVPNIkev2RecvP2DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1785)
)
panVPNIkev2RecvP2DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2RecvP2DeleteTrap.setStatus(
        "current"
    )

panVPNIkev2SendNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1786)
)
panVPNIkev2SendNotifyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2SendNotifyTrap.setStatus(
        "current"
    )

panVPNIkev2SendP1DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1787)
)
panVPNIkev2SendP1DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2SendP1DeleteTrap.setStatus(
        "current"
    )

panVPNIkev2SendP2DeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1788)
)
panVPNIkev2SendP2DeleteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVPNIkev2SendP2DeleteTrap.setStatus(
        "current"
    )

panSATDSatdConfigP1SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1800)
)
panSATDSatdConfigP1SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdConfigP1SuccessTrap.setStatus(
        "current"
    )

panSATDSatdConfigP1FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1801)
)
panSATDSatdConfigP1FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdConfigP1FailedTrap.setStatus(
        "current"
    )

panSATDSatdConfigP1AbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1802)
)
panSATDSatdConfigP1AbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdConfigP1AbortTrap.setStatus(
        "current"
    )

panSATDSatdConfigP2SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1803)
)
panSATDSatdConfigP2SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdConfigP2SuccessTrap.setStatus(
        "current"
    )

panSATDSatdConfigP2FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1804)
)
panSATDSatdConfigP2FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdConfigP2FailedTrap.setStatus(
        "current"
    )

panSATDSatdDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1805)
)
panSATDSatdDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdDaemonStartTrap.setStatus(
        "current"
    )

panSATDSatdDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1806)
)
panSATDSatdDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdDaemonExitTrap.setStatus(
        "current"
    )

panSATDSatdDaemonInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1807)
)
panSATDSatdDaemonInitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdDaemonInitTrap.setStatus(
        "current"
    )

panSATDSatdTunUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1808)
)
panSATDSatdTunUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunUpTrap.setStatus(
        "current"
    )

panSATDSatdTunDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1809)
)
panSATDSatdTunDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunDownTrap.setStatus(
        "current"
    )

panSATDSatdDupSubnetsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1810)
)
panSATDSatdDupSubnetsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdDupSubnetsTrap.setStatus(
        "current"
    )

panSATDSatdDeniedRoutesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1811)
)
panSATDSatdDeniedRoutesTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdDeniedRoutesTrap.setStatus(
        "current"
    )

panSATDSatdPortalGatewayDuplicateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1812)
)
panSATDSatdPortalGatewayDuplicateTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdPortalGatewayDuplicateTrap.setStatus(
        "current"
    )

panSATDSatdFlowFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1813)
)
panSATDSatdFlowFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdFlowFullSyncStartTrap.setStatus(
        "current"
    )

panSATDSatdFlowFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1814)
)
panSATDSatdFlowFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdFlowFullSyncAbortTrap.setStatus(
        "current"
    )

panSATDSatdFlowFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1815)
)
panSATDSatdFlowFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdFlowFullSyncDoneTrap.setStatus(
        "current"
    )

panSATDSatdHaFullSyncStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1816)
)
panSATDSatdHaFullSyncStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdHaFullSyncStartTrap.setStatus(
        "current"
    )

panSATDSatdHaFullSyncAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1817)
)
panSATDSatdHaFullSyncAbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdHaFullSyncAbortTrap.setStatus(
        "current"
    )

panSATDSatdHaFullSyncDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1818)
)
panSATDSatdHaFullSyncDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdHaFullSyncDoneTrap.setStatus(
        "current"
    )

panSATDSatdIpAssignFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1819)
)
panSATDSatdIpAssignFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdIpAssignFailTrap.setStatus(
        "current"
    )

panSATDSatdIpResetFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1820)
)
panSATDSatdIpResetFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdIpResetFailTrap.setStatus(
        "current"
    )

panSATDSatdTunMonDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1821)
)
panSATDSatdTunMonDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunMonDownTrap.setStatus(
        "current"
    )

panSATDSatdTunMonUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1822)
)
panSATDSatdTunMonUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunMonUpTrap.setStatus(
        "current"
    )

panSATDSatdTunSoftlifetimeExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1823)
)
panSATDSatdTunSoftlifetimeExpiredTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunSoftlifetimeExpiredTrap.setStatus(
        "current"
    )

panSATDSatdTunHardlifetimeExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1824)
)
panSATDSatdTunHardlifetimeExpiredTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunHardlifetimeExpiredTrap.setStatus(
        "current"
    )

panSATDSatdAccRouteUpdFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1825)
)
panSATDSatdAccRouteUpdFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdAccRouteUpdFailTrap.setStatus(
        "current"
    )

panSATDSatdNhUpdFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1826)
)
panSATDSatdNhUpdFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdNhUpdFailTrap.setStatus(
        "current"
    )

panSATDSatdTunDpInstallErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1827)
)
panSATDSatdTunDpInstallErrTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdTunDpInstallErrTrap.setStatus(
        "current"
    )

panSATDSatdGatewayConnectStartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1828)
)
panSATDSatdGatewayConnectStartedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdGatewayConnectStartedTrap.setStatus(
        "current"
    )

panSATDSatdPortalConnectStartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1829)
)
panSATDSatdPortalConnectStartedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdPortalConnectStartedTrap.setStatus(
        "current"
    )

panSATDSatdGatewayConnectFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1830)
)
panSATDSatdGatewayConnectFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdGatewayConnectFailedTrap.setStatus(
        "current"
    )

panSATDSatdPortalConnectFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1831)
)
panSATDSatdPortalConnectFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdPortalConnectFailedTrap.setStatus(
        "current"
    )

panSATDSatdGenericEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1832)
)
panSATDSatdGenericEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSATDSatdGenericEventTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrConfigP1SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1900)
)
panSSLMGRSslmgrConfigP1SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrConfigP1SuccessTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrConfigP1FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1901)
)
panSSLMGRSslmgrConfigP1FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrConfigP1FailedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrConfigP1AbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1902)
)
panSSLMGRSslmgrConfigP1AbortTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrConfigP1AbortTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrConfigP2SuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1903)
)
panSSLMGRSslmgrConfigP2SuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrConfigP2SuccessTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrConfigP2FailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1904)
)
panSSLMGRSslmgrConfigP2FailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrConfigP2FailedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrDaemonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1905)
)
panSSLMGRSslmgrDaemonStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrDaemonStartTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrDaemonExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1906)
)
panSSLMGRSslmgrDaemonExitTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrDaemonExitTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertGenSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1907)
)
panSSLMGRSslmgrCertGenSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertGenSuccessTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertGenFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1908)
)
panSSLMGRSslmgrCertGenFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertGenFailedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertStatusDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1909)
)
panSSLMGRSslmgrCertStatusDeletedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertStatusDeletedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertStatusRevokedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1910)
)
panSSLMGRSslmgrCertStatusRevokedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertStatusRevokedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrSatelliteInfoInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1911)
)
panSSLMGRSslmgrSatelliteInfoInsertedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrSatelliteInfoInsertedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrSatelliteInfoUpdatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1912)
)
panSSLMGRSslmgrSatelliteInfoUpdatedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrSatelliteInfoUpdatedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrSatelliteInfoDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1913)
)
panSSLMGRSslmgrSatelliteInfoDeletedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrSatelliteInfoDeletedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertOcspVerifyFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1914)
)
panSSLMGRSslmgrCertOcspVerifyFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertOcspVerifyFailedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrCertCrlVerifyFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1915)
)
panSSLMGRSslmgrCertCrlVerifyFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrCertCrlVerifyFailedTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrHaFullSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1916)
)
panSSLMGRSslmgrHaFullSyncTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrHaFullSyncTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrHaNotFullSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1917)
)
panSSLMGRSslmgrHaNotFullSyncTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrHaNotFullSyncTrap.setStatus(
        "current"
    )

panSSLMGRSslmgrGenericEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1918)
)
panSSLMGRSslmgrGenericEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSLMGRSslmgrGenericEventTrap.setStatus(
        "current"
    )

panURLNoUrlDatabaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2000)
)
panURLNoUrlDatabaseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLNoUrlDatabaseTrap.setStatus(
        "current"
    )

panURLInvalidLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2001)
)
panURLInvalidLicenseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLInvalidLicenseTrap.setStatus(
        "current"
    )

panURLFailedToLockUpdateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2002)
)
panURLFailedToLockUpdateTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLFailedToLockUpdateTrap.setStatus(
        "current"
    )

panURLConnectionSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2003)
)
panURLConnectionSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLConnectionSuccessTrap.setStatus(
        "current"
    )

panURLConnectionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2004)
)
panURLConnectionFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLConnectionFailureTrap.setStatus(
        "current"
    )

panURLServerIsDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2005)
)
panURLServerIsDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLServerIsDownTrap.setStatus(
        "current"
    )

panURLProxyConnectionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2006)
)
panURLProxyConnectionFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLProxyConnectionFailureTrap.setStatus(
        "current"
    )

panURLReceiveDataFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2007)
)
panURLReceiveDataFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLReceiveDataFailureTrap.setStatus(
        "current"
    )

panURLDynamicUrlConnectionDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2008)
)
panURLDynamicUrlConnectionDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLDynamicUrlConnectionDownTrap.setStatus(
        "current"
    )

panURLDownloadingUrlDatabaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2009)
)
panURLDownloadingUrlDatabaseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLDownloadingUrlDatabaseTrap.setStatus(
        "current"
    )

panURLDownloadUrlDatabaseSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2010)
)
panURLDownloadUrlDatabaseSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLDownloadUrlDatabaseSuccessTrap.setStatus(
        "current"
    )

panURLUpgradeUrlDatabaseSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2011)
)
panURLUpgradeUrlDatabaseSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUpgradeUrlDatabaseSuccessTrap.setStatus(
        "current"
    )

panURLRevertUrlDatabaseSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2012)
)
panURLRevertUrlDatabaseSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLRevertUrlDatabaseSuccessTrap.setStatus(
        "current"
    )

panURLUrlDatabaseIsLatestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2013)
)
panURLUrlDatabaseIsLatestTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlDatabaseIsLatestTrap.setStatus(
        "current"
    )

panURLUrlDownloadFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2014)
)
panURLUrlDownloadFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlDownloadFailureTrap.setStatus(
        "current"
    )

panURLUrlCloudConnectionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2015)
)
panURLUrlCloudConnectionFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlCloudConnectionFailureTrap.setStatus(
        "current"
    )

panURLUrlCloudConnectionSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2016)
)
panURLUrlCloudConnectionSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlCloudConnectionSuccessTrap.setStatus(
        "current"
    )

panURLUrlBackupSeedSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2017)
)
panURLUrlBackupSeedSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlBackupSeedSuccessTrap.setStatus(
        "current"
    )

panURLUrlBackupSeedFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2018)
)
panURLUrlBackupSeedFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlBackupSeedFailureTrap.setStatus(
        "current"
    )

panURLCloudElectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2019)
)
panURLCloudElectionTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLCloudElectionTrap.setStatus(
        "current"
    )

panURLCloudProcessStartsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2020)
)
panURLCloudProcessStartsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLCloudProcessStartsTrap.setStatus(
        "current"
    )

panURLCloudProcessStoppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2021)
)
panURLCloudProcessStoppedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLCloudProcessStoppedTrap.setStatus(
        "current"
    )

panURLUpdateVersionFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2022)
)
panURLUpdateVersionFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUpdateVersionFailureTrap.setStatus(
        "current"
    )

panURLErrorMsgFromCloudTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2023)
)
panURLErrorMsgFromCloudTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLErrorMsgFromCloudTrap.setStatus(
        "current"
    )

panURLTestASiteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2024)
)
panURLTestASiteTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLTestASiteTrap.setStatus(
        "current"
    )

panURLUrlEngineStoppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2025)
)
panURLUrlEngineStoppedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlEngineStoppedTrap.setStatus(
        "current"
    )

panURLUrlEngineStartsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2026)
)
panURLUrlEngineStartsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLUrlEngineStartsTrap.setStatus(
        "current"
    )

panURLStartupFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2027)
)
panURLStartupFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLStartupFailureTrap.setStatus(
        "current"
    )

panURLHaSyncFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2028)
)
panURLHaSyncFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLHaSyncFailureTrap.setStatus(
        "current"
    )

panURLHaSyncSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2029)
)
panURLHaSyncSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLHaSyncSuccessTrap.setStatus(
        "current"
    )

panURLSaveMpCacheToDiscFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2030)
)
panURLSaveMpCacheToDiscFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLSaveMpCacheToDiscFailureTrap.setStatus(
        "current"
    )

panURLSaveMpCacheToDiscSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2031)
)
panURLSaveMpCacheToDiscSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLSaveMpCacheToDiscSuccessTrap.setStatus(
        "current"
    )

panURLRfsProcessStartsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2032)
)
panURLRfsProcessStartsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLRfsProcessStartsTrap.setStatus(
        "current"
    )

panURLRfsProcessStoppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2033)
)
panURLRfsProcessStoppedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLRfsProcessStoppedTrap.setStatus(
        "current"
    )

panURLRfsProcessFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2034)
)
panURLRfsProcessFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLRfsProcessFailureTrap.setStatus(
        "current"
    )

panURLRequestToCloudFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2035)
)
panURLRequestToCloudFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLRequestToCloudFailureTrap.setStatus(
        "current"
    )

panURLStartsFromEmptySeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2036)
)
panURLStartsFromEmptySeedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLStartsFromEmptySeedTrap.setStatus(
        "current"
    )

panURLLoadSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2037)
)
panURLLoadSuccessTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLLoadSuccessTrap.setStatus(
        "current"
    )

panURLFailedToLockDownloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2038)
)
panURLFailedToLockDownloadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLFailedToLockDownloadTrap.setStatus(
        "current"
    )

panURLEngineStartupFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2039)
)
panURLEngineStartupFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLEngineStartupFailureTrap.setStatus(
        "current"
    )

panURLSeedOutOfSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2040)
)
panURLSeedOutOfSyncTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLSeedOutOfSyncTrap.setStatus(
        "current"
    )

panURLStartsFromBackupSeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2041)
)
panURLStartsFromBackupSeedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLStartsFromBackupSeedTrap.setStatus(
        "current"
    )

panURLStartsFromDownloadSeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2042)
)
panURLStartsFromDownloadSeedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLStartsFromDownloadSeedTrap.setStatus(
        "current"
    )

panURLBackupSeedErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2043)
)
panURLBackupSeedErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLBackupSeedErrorTrap.setStatus(
        "current"
    )

panURLDownloadSeedErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2044)
)
panURLDownloadSeedErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panURLDownloadSeedErrorTrap.setStatus(
        "current"
    )

panUSERIDConnectAgentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2300)
)
panUSERIDConnectAgentTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectAgentTrap.setStatus(
        "current"
    )

panUSERIDDisconnectAgentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2301)
)
panUSERIDDisconnectAgentTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDDisconnectAgentTrap.setStatus(
        "current"
    )

panUSERIDAgentEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2302)
)
panUSERIDAgentEventTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentEventTrap.setStatus(
        "current"
    )

panUSERIDConnectAgentFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2303)
)
panUSERIDConnectAgentFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectAgentFailureTrap.setStatus(
        "current"
    )

panUSERIDAgentVersionMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2304)
)
panUSERIDAgentVersionMismatchTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentVersionMismatchTrap.setStatus(
        "current"
    )

panUSERIDAgentStatusFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2305)
)
panUSERIDAgentStatusFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentStatusFailureTrap.setStatus(
        "current"
    )

panUSERIDAgentReadLogErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2306)
)
panUSERIDAgentReadLogErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentReadLogErrorTrap.setStatus(
        "current"
    )

panUSERIDAgentGetDomainErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2307)
)
panUSERIDAgentGetDomainErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentGetDomainErrorTrap.setStatus(
        "current"
    )

panUSERIDAgentGetUsersErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2308)
)
panUSERIDAgentGetUsersErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentGetUsersErrorTrap.setStatus(
        "current"
    )

panUSERIDAgentGetGroupsErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2309)
)
panUSERIDAgentGetGroupsErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentGetGroupsErrorTrap.setStatus(
        "current"
    )

panUSERIDAgentGetConfigErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2310)
)
panUSERIDAgentGetConfigErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentGetConfigErrorTrap.setStatus(
        "current"
    )

panUSERIDAgentNoDomainTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2311)
)
panUSERIDAgentNoDomainTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentNoDomainTrap.setStatus(
        "current"
    )

panUSERIDAgentNoAllowlistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2312)
)
panUSERIDAgentNoAllowlistTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDAgentNoAllowlistTrap.setStatus(
        "current"
    )

panUSERIDConnectLdapSeverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2313)
)
panUSERIDConnectLdapSeverTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectLdapSeverTrap.setStatus(
        "current"
    )

panUSERIDConnectLdapSeverFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2314)
)
panUSERIDConnectLdapSeverFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectLdapSeverFailureTrap.setStatus(
        "current"
    )

panUSERIDGetLdapDataFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2315)
)
panUSERIDGetLdapDataFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDGetLdapDataFailureTrap.setStatus(
        "current"
    )

panUSERIDHAQueueFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2316)
)
panUSERIDHAQueueFullTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDHAQueueFullTrap.setStatus(
        "current"
    )

panUSERIDConnectClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2317)
)
panUSERIDConnectClientTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectClientTrap.setStatus(
        "current"
    )

panUSERIDDisconnectClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2318)
)
panUSERIDDisconnectClientTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDDisconnectClientTrap.setStatus(
        "current"
    )

panUSERIDConnectServerMonitorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2319)
)
panUSERIDConnectServerMonitorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectServerMonitorTrap.setStatus(
        "current"
    )

panUSERIDConnectServerMonitorFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2320)
)
panUSERIDConnectServerMonitorFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectServerMonitorFailureTrap.setStatus(
        "current"
    )

panUSERIDConnectVmInfoSourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2321)
)
panUSERIDConnectVmInfoSourceTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectVmInfoSourceTrap.setStatus(
        "current"
    )

panUSERIDDisconnectVmInfoSourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2322)
)
panUSERIDDisconnectVmInfoSourceTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDDisconnectVmInfoSourceTrap.setStatus(
        "current"
    )

panUSERIDConnectVmInfoSourceFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2323)
)
panUSERIDConnectVmInfoSourceFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectVmInfoSourceFailureTrap.setStatus(
        "current"
    )

panUSERIDRegisteredIpUpdateFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2324)
)
panUSERIDRegisteredIpUpdateFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDRegisteredIpUpdateFailureTrap.setStatus(
        "current"
    )

panUSERIDConnectSyslogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2325)
)
panUSERIDConnectSyslogTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDConnectSyslogTrap.setStatus(
        "current"
    )

panUSERIDDisconnectSyslogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2326)
)
panUSERIDDisconnectSyslogTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panUSERIDDisconnectSyslogTrap.setStatus(
        "current"
    )

panNATFallbackReportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2400)
)
panNATFallbackReportTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panNATFallbackReportTrap.setStatus(
        "current"
    )

panSYSLOGNGSyslogConnStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2500)
)
panSYSLOGNGSyslogConnStatusTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSYSLOGNGSyslogConnStatusTrap.setStatus(
        "current"
    )

panLACPLostConnectivityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2600)
)
panLACPLostConnectivityTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPLostConnectivityTrap.setStatus(
        "current"
    )

panLACPUnresponsiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2601)
)
panLACPUnresponsiveTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPUnresponsiveTrap.setStatus(
        "current"
    )

panLACPNegoFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2602)
)
panLACPNegoFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPNegoFailTrap.setStatus(
        "current"
    )

panLACPSpeedDuplexTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2603)
)
panLACPSpeedDuplexTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPSpeedDuplexTrap.setStatus(
        "current"
    )

panLACPLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2604)
)
panLACPLinkDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPLinkDownTrap.setStatus(
        "current"
    )

panLACPLacpDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2605)
)
panLACPLacpDownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPLacpDownTrap.setStatus(
        "current"
    )

panLACPLacpUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2606)
)
panLACPLacpUpTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLACPLacpUpTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestUnknownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2700)
)
panFIPSFipsSelftestUnknownTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestUnknownTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2701)
)
panFIPSFipsSelftestTimeoutTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestTimeoutTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestIntegTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2702)
)
panFIPSFipsSelftestIntegTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestIntegTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestCoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2703)
)
panFIPSFipsSelftestCoreTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestCoreTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestAesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2704)
)
panFIPSFipsSelftestAesTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestAesTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2705)
)
panFIPSFipsSelftestDesTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDesTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDsaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2706)
)
panFIPSFipsSelftestDsaTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDsaTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestRsaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2707)
)
panFIPSFipsSelftestRsaTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestRsaTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestHmacTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2708)
)
panFIPSFipsSelftestHmacTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestHmacTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestShaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2709)
)
panFIPSFipsSelftestShaTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestShaTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDrngTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2710)
)
panFIPSFipsSelftestDrngTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDrngTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestNdrngTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2711)
)
panFIPSFipsSelftestNdrngTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestNdrngTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDhParameterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2712)
)
panFIPSFipsSelftestDhParameterTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDhParameterTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDhTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2713)
)
panFIPSFipsSelftestDhTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDhTrap.setStatus(
        "current"
    )

panFIPSFipsFirmwareIntegrityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2714)
)
panFIPSFipsFirmwareIntegrityTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsFirmwareIntegrityTrap.setStatus(
        "current"
    )

panFIPSFipsContinuousRngTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2715)
)
panFIPSFipsContinuousRngTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsContinuousRngTrap.setStatus(
        "current"
    )

panFIPSFipsRsaPairwiseConsistencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2716)
)
panFIPSFipsRsaPairwiseConsistencyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsRsaPairwiseConsistencyTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestSoftwareLoadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2717)
)
panFIPSFipsSelftestSoftwareLoadTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestSoftwareLoadTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2718)
)
panFIPSFipsSelftestTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestHsmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2719)
)
panFIPSFipsSelftestHsmTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestHsmTrap.setStatus(
        "current"
    )

panFIPSFipsZeroizationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2720)
)
panFIPSFipsZeroizationTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsZeroizationTrap.setStatus(
        "current"
    )

panFIPSFipsKeyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2721)
)
panFIPSFipsKeyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsKeyTrap.setStatus(
        "current"
    )

panFIPSFipsCipherTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2722)
)
panFIPSFipsCipherTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsCipherTrap.setStatus(
        "current"
    )

panFIPSFipsReplayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2723)
)
panFIPSFipsReplayTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsReplayTrap.setStatus(
        "current"
    )

panFIPSFipsSslHandshakeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2724)
)
panFIPSFipsSslHandshakeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSslHandshakeTrap.setStatus(
        "current"
    )

panFIPSFipsContinuousNdrngTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2725)
)
panFIPSFipsContinuousNdrngTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsContinuousNdrngTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestCmacTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2726)
)
panFIPSFipsSelftestCmacTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestCmacTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestDrbgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2727)
)
panFIPSFipsSelftestDrbgTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestDrbgTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestEcdsaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2728)
)
panFIPSFipsSelftestEcdsaTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestEcdsaTrap.setStatus(
        "current"
    )

panFIPSFipsSelftestEcdhTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2729)
)
panFIPSFipsSelftestEcdhTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFIPSFipsSelftestEcdhTrap.setStatus(
        "current"
    )

panMDMExceedLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2800)
)
panMDMExceedLicenseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMExceedLicenseTrap.setStatus(
        "current"
    )

panMDMConnectToApnsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2801)
)
panMDMConnectToApnsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToApnsTrap.setStatus(
        "current"
    )

panMDMConnectToApnsFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2802)
)
panMDMConnectToApnsFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToApnsFailureTrap.setStatus(
        "current"
    )

panMDMConnectToGcmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2803)
)
panMDMConnectToGcmTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToGcmTrap.setStatus(
        "current"
    )

panMDMConnectToGcmFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2804)
)
panMDMConnectToGcmFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToGcmFailureTrap.setStatus(
        "current"
    )

panMDMGatewayConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2805)
)
panMDMGatewayConnectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMGatewayConnectedTrap.setStatus(
        "current"
    )

panMDMGatewayDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2806)
)
panMDMGatewayDisconnectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMGatewayDisconnectedTrap.setStatus(
        "current"
    )

panMDMInstallAppContentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2807)
)
panMDMInstallAppContentTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMInstallAppContentTrap.setStatus(
        "current"
    )

panMDMInstallAppContentFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2808)
)
panMDMInstallAppContentFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMInstallAppContentFailureTrap.setStatus(
        "current"
    )

panMDMGetScepOtpFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2809)
)
panMDMGetScepOtpFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMGetScepOtpFailureTrap.setStatus(
        "current"
    )

panMDMSendMsgToCloudFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2810)
)
panMDMSendMsgToCloudFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMSendMsgToCloudFailureTrap.setStatus(
        "current"
    )

panMDMConnectToItunesFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2811)
)
panMDMConnectToItunesFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToItunesFailureTrap.setStatus(
        "current"
    )

panMDMConnectToAppleVppFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2812)
)
panMDMConnectToAppleVppFailureTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panMDMConnectToAppleVppFailureTrap.setStatus(
        "current"
    )

panRAIDDiskNotDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2900)
)
panRAIDDiskNotDetectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDDiskNotDetectedTrap.setStatus(
        "current"
    )

panRAIDPairDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2901)
)
panRAIDPairDetectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDPairDetectedTrap.setStatus(
        "current"
    )

panRAIDRebuildingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2902)
)
panRAIDRebuildingTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuildingTrap.setStatus(
        "current"
    )

panRAIDRebuild20Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2903)
)
panRAIDRebuild20Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuild20Trap.setStatus(
        "current"
    )

panRAIDRebuild40Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2904)
)
panRAIDRebuild40Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuild40Trap.setStatus(
        "current"
    )

panRAIDRebuild60Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2905)
)
panRAIDRebuild60Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuild60Trap.setStatus(
        "current"
    )

panRAIDRebuild80Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2906)
)
panRAIDRebuild80Trap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuild80Trap.setStatus(
        "current"
    )

panRAIDRebuildDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2907)
)
panRAIDRebuildDoneTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuildDoneTrap.setStatus(
        "current"
    )

panRAIDDiskActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2908)
)
panRAIDDiskActiveTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDDiskActiveTrap.setStatus(
        "current"
    )

panRAIDDiskFaultyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2909)
)
panRAIDDiskFaultyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDDiskFaultyTrap.setStatus(
        "current"
    )

panRAIDDiskFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2910)
)
panRAIDDiskFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDDiskFailedTrap.setStatus(
        "current"
    )

panRAIDSpareMissingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2911)
)
panRAIDSpareMissingTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDSpareMissingTrap.setStatus(
        "current"
    )

panRAIDSpareMovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2912)
)
panRAIDSpareMovedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDSpareMovedTrap.setStatus(
        "current"
    )

panRAIDPairDegradedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2913)
)
panRAIDPairDegradedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDPairDegradedTrap.setStatus(
        "current"
    )

panRAIDPairDisappearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2914)
)
panRAIDPairDisappearedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDPairDisappearedTrap.setStatus(
        "current"
    )

panRAIDDiskRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2915)
)
panRAIDDiskRemovedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDDiskRemovedTrap.setStatus(
        "current"
    )

panRAIDFsckStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2916)
)
panRAIDFsckStartTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDFsckStartTrap.setStatus(
        "current"
    )

panRAIDFsckEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2917)
)
panRAIDFsckEndTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDFsckEndTrap.setStatus(
        "current"
    )

panRAIDFsckFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2918)
)
panRAIDFsckFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDFsckFailedTrap.setStatus(
        "current"
    )

panRAIDMountFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2919)
)
panRAIDMountFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDMountFailedTrap.setStatus(
        "current"
    )

panRAIDRebuildFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 2920)
)
panRAIDRebuildFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panRAIDRebuildFailedTrap.setStatus(
        "current"
    )

panVMDvfInitSucceedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3000)
)
panVMDvfInitSucceedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVMDvfInitSucceedTrap.setStatus(
        "current"
    )

panVMDvfInitFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3001)
)
panVMDvfInitFailTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panVMDvfInitFailTrap.setStatus(
        "current"
    )

panSSHSshSessionEstablishedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3100)
)
panSSHSshSessionEstablishedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSHSshSessionEstablishedTrap.setStatus(
        "current"
    )

panSSHSshSessionTerminatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3101)
)
panSSHSshSessionTerminatedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSHSshSessionTerminatedTrap.setStatus(
        "current"
    )

panSSHSshSessionEstablishmentFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3102)
)
panSSHSshSessionEstablishmentFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSHSshSessionEstablishmentFailedTrap.setStatus(
        "current"
    )

panSSHSshSessionDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3103)
)
panSSHSshSessionDisconnectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSHSshSessionDisconnectedTrap.setStatus(
        "current"
    )

panSSHSshConnectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3104)
)
panSSHSshConnectionTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panSSHSshConnectionTrap.setStatus(
        "current"
    )

panTLSTlsSessionEstablishedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3200)
)
panTLSTlsSessionEstablishedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsSessionEstablishedTrap.setStatus(
        "current"
    )

panTLSTlsSessionTerminatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3201)
)
panTLSTlsSessionTerminatedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsSessionTerminatedTrap.setStatus(
        "current"
    )

panTLSTlsSessionEstablishmentFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3202)
)
panTLSTlsSessionEstablishmentFailedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsSessionEstablishmentFailedTrap.setStatus(
        "current"
    )

panTLSTlsSessionDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3203)
)
panTLSTlsSessionDisconnectedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panTLSTlsSessionDisconnectedTrap.setStatus(
        "current"
    )

panLLDPRxErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3300)
)
panLLDPRxErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPRxErrorTrap.setStatus(
        "current"
    )

panLLDPMibChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3301)
)
panLLDPMibChangedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPMibChangedTrap.setStatus(
        "current"
    )

panLLDPTooManyNeighborsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3302)
)
panLLDPTooManyNeighborsTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPTooManyNeighborsTrap.setStatus(
        "current"
    )

panLLDPTooManyNeighborsTimerClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3303)
)
panLLDPTooManyNeighborsTimerClearedTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPTooManyNeighborsTimerClearedTrap.setStatus(
        "current"
    )

panLLDPOtherTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3304)
)
panLLDPOtherTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPOtherTrap.setStatus(
        "current"
    )

panLLDPTxErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3305)
)
panLLDPTxErrorTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panLLDPTxErrorTrap.setStatus(
        "current"
    )

panFBWildfireWrongCloudTypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3400)
)
panFBWildfireWrongCloudTypeTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFBWildfireWrongCloudTypeTrap.setStatus(
        "current"
    )

panFBWildfireDisabledByCloudTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3401)
)
panFBWildfireDisabledByCloudTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFBWildfireDisabledByCloudTrap.setStatus(
        "current"
    )

panFBWildfireNoPolicyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3402)
)
panFBWildfireNoPolicyTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFBWildfireNoPolicyTrap.setStatus(
        "current"
    )

panFBWildfireNoLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3403)
)
panFBWildfireNoLicenseTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFBWildfireNoLicenseTrap.setStatus(
        "current"
    )

panFBWildfireInvalidCloudInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 3404)
)
panFBWildfireInvalidCloudInfoTrap.setObjects(
      *(("PAN-TRAPS", "panReceiveTime"),
        ("PAN-TRAPS", "panSerial"),
        ("PAN-TRAPS", "panEventType"),
        ("PAN-TRAPS", "panEventSubType"),
        ("PAN-TRAPS", "panVsys"),
        ("PAN-TRAPS", "panSeqno"),
        ("PAN-TRAPS", "panActionflags"),
        ("PAN-TRAPS", "panSystemEventId"),
        ("PAN-TRAPS", "panSystemObject"),
        ("PAN-TRAPS", "panSystemModule"),
        ("PAN-TRAPS", "panSystemSeverity"),
        ("PAN-TRAPS", "panSystemDescription"))
)
if mibBuilder.loadTexts:
    panFBWildfireInvalidCloudInfoTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAN-TRAPS",
    **{"panTrapMibsModule": panTrapMibsModule,
       "panReceiveTime": panReceiveTime,
       "panSerial": panSerial,
       "panEventType": panEventType,
       "panEventSubType": panEventSubType,
       "panHost": panHost,
       "panVsys": panVsys,
       "panSeqno": panSeqno,
       "panActionflags": panActionflags,
       "panHostInetAddrType": panHostInetAddrType,
       "panHostInetAddr": panHostInetAddr,
       "panSource": panSource,
       "panDestination": panDestination,
       "panNatSource": panNatSource,
       "panNatDestination": panNatDestination,
       "panRule": panRule,
       "panSrcUser": panSrcUser,
       "panDstUser": panDstUser,
       "panApplication": panApplication,
       "panSourceZone": panSourceZone,
       "panDestinationZone": panDestinationZone,
       "panIngressInterface": panIngressInterface,
       "panEgressInterface": panEgressInterface,
       "panLogForwardingProfile": panLogForwardingProfile,
       "panSessionID": panSessionID,
       "panRepeatCount": panRepeatCount,
       "panSourcePort": panSourcePort,
       "panDestinationPort": panDestinationPort,
       "panNatSourcePort": panNatSourcePort,
       "panNatDestinationPort": panNatDestinationPort,
       "panFlags": panFlags,
       "panProtocol": panProtocol,
       "panAction": panAction,
       "panTimeGenerated": panTimeGenerated,
       "panSrcloc": panSrcloc,
       "panDstloc": panDstloc,
       "panSourceInetAddrType": panSourceInetAddrType,
       "panSourceInetAddr": panSourceInetAddr,
       "panDestinationInetAddrType": panDestinationInetAddrType,
       "panDestinationInetAddr": panDestinationInetAddr,
       "panNatSourceInetAddrType": panNatSourceInetAddrType,
       "panNatSourceInetAddr": panNatSourceInetAddr,
       "panNatDestinationInetAddrType": panNatDestinationInetAddrType,
       "panNatDestinationInetAddr": panNatDestinationInetAddr,
       "panTrafficBytes": panTrafficBytes,
       "panTrafficPackets": panTrafficPackets,
       "panTrafficStartTime": panTrafficStartTime,
       "panTrafficElapsed": panTrafficElapsed,
       "panTrafficCategory": panTrafficCategory,
       "panTrafficSessionEndReason": panTrafficSessionEndReason,
       "panConfigCmd": panConfigCmd,
       "panConfigAdmin": panConfigAdmin,
       "panConfigClient": panConfigClient,
       "panConfigResult": panConfigResult,
       "panConfigPath": panConfigPath,
       "panThreatId": panThreatId,
       "panThreatCategory": panThreatCategory,
       "panThreatContentType": panThreatContentType,
       "panThreatSeverity": panThreatSeverity,
       "panThreatDirection": panThreatDirection,
       "panMiscellaneous": panMiscellaneous,
       "panPcapId": panPcapId,
       "panFileDigest": panFileDigest,
       "panCloud": panCloud,
       "panUrlIndex": panUrlIndex,
       "panUserAgent": panUserAgent,
       "panXff": panXff,
       "panReferer": panReferer,
       "panSender": panSender,
       "panSubject": panSubject,
       "panRecipient": panRecipient,
       "panFileType": panFileType,
       "panReportId": panReportId,
       "panHipSourceUser": panHipSourceUser,
       "panHipMachineName": panHipMachineName,
       "panHipSource": panHipSource,
       "panHipMatch": panHipMatch,
       "panHipMatchType": panHipMatchType,
       "panHipRepeatCount": panHipRepeatCount,
       "panHipOS": panHipOS,
       "panHipSourceInetAddrType": panHipSourceInetAddrType,
       "panHipSourceInetAddr": panHipSourceInetAddr,
       "panSystemEventId": panSystemEventId,
       "panSystemObject": panSystemObject,
       "panSystemModule": panSystemModule,
       "panSystemSeverity": panSystemSeverity,
       "panSystemDescription": panSystemDescription,
       "panCorrDG1": panCorrDG1,
       "panCorrDG2": panCorrDG2,
       "panCorrDG3": panCorrDG3,
       "panCorrDG4": panCorrDG4,
       "panCorrObjName": panCorrObjName,
       "panCorrObjID": panCorrObjID,
       "panCorrSeverity": panCorrSeverity,
       "panCorrEvidence": panCorrEvidence,
       "panConfigTrap": panConfigTrap,
       "panTrafficTrap": panTrafficTrap,
       "panThreatTrap": panThreatTrap,
       "panHipMatchTrap": panHipMatchTrap,
       "panCryptoCertExpiryTrap": panCryptoCertExpiryTrap,
       "panCryptoMkeyExpiryTrap": panCryptoMkeyExpiryTrap,
       "panCryptoMkeyExpiryReminderTrap": panCryptoMkeyExpiryReminderTrap,
       "panCryptoHSMStateChangeTrap": panCryptoHSMStateChangeTrap,
       "panCryptoPrivateKeyExportTrap": panCryptoPrivateKeyExportTrap,
       "panDHCPLeaseStartTrap": panDHCPLeaseStartTrap,
       "panDHCPLeaseEndTrap": panDHCPLeaseEndTrap,
       "panDHCPServerOnTrap": panDHCPServerOnTrap,
       "panDHCPServerAutoProbeOnTrap": panDHCPServerAutoProbeOnTrap,
       "panDHCPServerAutoProbeOffTrap": panDHCPServerAutoProbeOffTrap,
       "panDHCPServerNoFreeIpTrap": panDHCPServerNoFreeIpTrap,
       "panDHCPIpAlreadyInUseTrap": panDHCPIpAlreadyInUseTrap,
       "panDHCPRelayOnTrap": panDHCPRelayOnTrap,
       "panDHCPRelayOffTrap": panDHCPRelayOffTrap,
       "panDHCPRelay6OnTrap": panDHCPRelay6OnTrap,
       "panDHCPRelay6OffTrap": panDHCPRelay6OffTrap,
       "panDHCPIfUpdateFailTrap": panDHCPIfUpdateFailTrap,
       "panDHCPIfUpdateOkTrap": panDHCPIfUpdateOkTrap,
       "panDHCPIfClearTrap": panDHCPIfClearTrap,
       "panDHCPIfRenewTriggerTrap": panDHCPIfRenewTriggerTrap,
       "panDHCPIfReleaseTriggerTrap": panDHCPIfReleaseTriggerTrap,
       "panDHCPIfRcvNakTrap": panDHCPIfRcvNakTrap,
       "panDHCPIfInheritTrap": panDHCPIfInheritTrap,
       "panDHCPIfDuplicateIpIntfTrap": panDHCPIfDuplicateIpIntfTrap,
       "panDHCPIfDuplicateIpRemoteTrap": panDHCPIfDuplicateIpRemoteTrap,
       "panDNSProxyCacheClearedTrap": panDNSProxyCacheClearedTrap,
       "panDNSProxyResolveFailTrap": panDNSProxyResolveFailTrap,
       "panDNSProxyObjectEnableTrap": panDNSProxyObjectEnableTrap,
       "panDNSProxyIfAddTrap": panDNSProxyIfAddTrap,
       "panDNSProxyIfDelTrap": panDNSProxyIfDelTrap,
       "panDNSProxyIfInheritTrap": panDNSProxyIfInheritTrap,
       "panDOSDosRuleChangedTrap": panDOSDosRuleChangedTrap,
       "panGeneralGeneralTrap": panGeneralGeneralTrap,
       "panGeneralSystemStartTrap": panGeneralSystemStartTrap,
       "panGeneralSystemShutdownTrap": panGeneralSystemShutdownTrap,
       "panGeneralAuthFailTrap": panGeneralAuthFailTrap,
       "panGeneralAuthSuccessTrap": panGeneralAuthSuccessTrap,
       "panGeneralTacLoginTrap": panGeneralTacLoginTrap,
       "panGeneralAuthServerDownTrap": panGeneralAuthServerDownTrap,
       "panGlobalProtectGatewayRegistSuccTrap": panGlobalProtectGatewayRegistSuccTrap,
       "panGlobalProtectGatewayRegistFailTrap": panGlobalProtectGatewayRegistFailTrap,
       "panGlobalProtectGatewayLogoutSuccTrap": panGlobalProtectGatewayLogoutSuccTrap,
       "panGlobalProtectGatewayLogoutFailTrap": panGlobalProtectGatewayLogoutFailTrap,
       "panGlobalProtectGatewayConfigSuccTrap": panGlobalProtectGatewayConfigSuccTrap,
       "panGlobalProtectGatewayConfigFailTrap": panGlobalProtectGatewayConfigFailTrap,
       "panGlobalProtectGatewayConfigReleaseTrap": panGlobalProtectGatewayConfigReleaseTrap,
       "panGlobalProtectGatewaySwitchSuccTrap": panGlobalProtectGatewaySwitchSuccTrap,
       "panGlobalProtectGatewaySwitchFailTrap": panGlobalProtectGatewaySwitchFailTrap,
       "panGlobalProtectGatewayAuthSuccTrap": panGlobalProtectGatewayAuthSuccTrap,
       "panGlobalProtectGatewayAuthFailTrap": panGlobalProtectGatewayAuthFailTrap,
       "panGlobalProtectGatewayAgentMsgTrap": panGlobalProtectGatewayAgentMsgTrap,
       "panGlobalProtectGatewayInvalidLicenseTrap": panGlobalProtectGatewayInvalidLicenseTrap,
       "panGlobalProtectGatewayInheritanceTrap": panGlobalProtectGatewayInheritanceTrap,
       "panGlobalProtectPortalConfigSuccTrap": panGlobalProtectPortalConfigSuccTrap,
       "panGlobalProtectPortalConfigFailTrap": panGlobalProtectPortalConfigFailTrap,
       "panGlobalProtectPortalAuthSuccTrap": panGlobalProtectPortalAuthSuccTrap,
       "panGlobalProtectPortalAuthFailTrap": panGlobalProtectPortalAuthFailTrap,
       "panGlobalprotectgatewaySatauthSuccTrap": panGlobalprotectgatewaySatauthSuccTrap,
       "panGlobalprotectgatewaySatauthFailTrap": panGlobalprotectgatewaySatauthFailTrap,
       "panGlobalprotectgatewayRouteAddFailTrap": panGlobalprotectgatewayRouteAddFailTrap,
       "panGlobalprotectgatewayRouteResetFailTrap": panGlobalprotectgatewayRouteResetFailTrap,
       "panGlobalprotectgatewayTunUpTrap": panGlobalprotectgatewayTunUpTrap,
       "panGlobalprotectgatewayTunDownTrap": panGlobalprotectgatewayTunDownTrap,
       "panGlobalprotectgatewayDupSubnetsTrap": panGlobalprotectgatewayDupSubnetsTrap,
       "panGlobalprotectgatewayDeniedRoutesTrap": panGlobalprotectgatewayDeniedRoutesTrap,
       "panGlobalprotectgatewayTunMonDownTrap": panGlobalprotectgatewayTunMonDownTrap,
       "panGlobalprotectgatewayTunMonUpTrap": panGlobalprotectgatewayTunMonUpTrap,
       "panGlobalprotectportalSatconfigSuccTrap": panGlobalprotectportalSatconfigSuccTrap,
       "panGlobalprotectportalSatconfigFailTrap": panGlobalprotectportalSatconfigFailTrap,
       "panGlobalprotectportalSatauthSuccTrap": panGlobalprotectportalSatauthSuccTrap,
       "panGlobalprotectportalSatauthFailTrap": panGlobalprotectportalSatauthFailTrap,
       "panGlobalprotectportalSatcertSuccTrap": panGlobalprotectportalSatcertSuccTrap,
       "panGlobalprotectportalSatcertFailTrap": panGlobalprotectportalSatcertFailTrap,
       "panGlobalprotectgatewayTunHardlifetimeExpiredTrap": panGlobalprotectgatewayTunHardlifetimeExpiredTrap,
       "panGlobalprotectgatewayTunDpInstallErrTrap": panGlobalprotectgatewayTunDpInstallErrTrap,
       "panGlobalprotectportalGenportalcookieSuccTrap": panGlobalprotectportalGenportalcookieSuccTrap,
       "panGlobalprotectportalGenportalcookieFailTrap": panGlobalprotectportalGenportalcookieFailTrap,
       "panGlobalprotectgatewayFramedIpSuccTrap": panGlobalprotectgatewayFramedIpSuccTrap,
       "panGlobalprotectgatewayFramedIpFailTrap": panGlobalprotectgatewayFramedIpFailTrap,
       "panHAPreemptTrap": panHAPreemptTrap,
       "panHAStateChangeTrap": panHAStateChangeTrap,
       "panHAStateOverrideTrap": panHAStateOverrideTrap,
       "panHADataplaneDownTrap": panHADataplaneDownTrap,
       "panHAPolicyPushFailTrap": panHAPolicyPushFailTrap,
       "panHAHa1LinkChangeTrap": panHAHa1LinkChangeTrap,
       "panHAHa2LinkChangeTrap": panHAHa2LinkChangeTrap,
       "panHAConnectChangeTrap": panHAConnectChangeTrap,
       "panHAPathMonitorDownTrap": panHAPathMonitorDownTrap,
       "panHALinkMonitorDownTrap": panHALinkMonitorDownTrap,
       "panHAHa3LinkChangeTrap": panHAHa3LinkChangeTrap,
       "panHAPathMonitorUpTrap": panHAPathMonitorUpTrap,
       "panHALinkMonitorUpTrap": panHALinkMonitorUpTrap,
       "panHAPeerSyncFailureTrap": panHAPeerSyncFailureTrap,
       "panHAConfigFailureTrap": panHAConfigFailureTrap,
       "panHAConfigNotSynchTrap": panHAConfigNotSynchTrap,
       "panHAPeerErrorTrap": panHAPeerErrorTrap,
       "panHAPre13Trap": panHAPre13Trap,
       "panHAPre20Trap": panHAPre20Trap,
       "panHAPeerVersionMatchTrap": panHAPeerVersionMatchTrap,
       "panHAPeerVersionSupportedTrap": panHAPeerVersionSupportedTrap,
       "panHAPeerVersionUnsupportedTrap": panHAPeerVersionUnsupportedTrap,
       "panHAPeerVersionDegradedTrap": panHAPeerVersionDegradedTrap,
       "panHAPeerCompatMismatchTrap": panHAPeerCompatMismatchTrap,
       "panHAPeerCompatMatchTrap": panHAPeerCompatMatchTrap,
       "panHAPeerCompatFailTrap": panHAPeerCompatFailTrap,
       "panHAPeerSplitBrainTrap": panHAPeerSplitBrainTrap,
       "panHASplitBrainTrap": panHASplitBrainTrap,
       "panHAPreemptLoopTrap": panHAPreemptLoopTrap,
       "panHANonFunctionalLoopTrap": panHANonFunctionalLoopTrap,
       "panHAPeerShutdownTrap": panHAPeerShutdownTrap,
       "panHANfsPanlogsFailTrap": panHANfsPanlogsFailTrap,
       "panHAInternalHaErrorTrap": panHAInternalHaErrorTrap,
       "panHASystemFailureTrap": panHASystemFailureTrap,
       "panHAHa2KeepAliveTrap": panHAHa2KeepAliveTrap,
       "panHASlotFailureTrap": panHASlotFailureTrap,
       "panHASlotMismatchTrap": panHASlotMismatchTrap,
       "panHASlotControlFailureTrap": panHASlotControlFailureTrap,
       "panHASlotControlEventTrap": panHASlotControlEventTrap,
       "panHASessionSynchTrap": panHASessionSynchTrap,
       "panHWDiskErrorsTrap": panHWDiskErrorsTrap,
       "panHWSlotUpTrap": panHWSlotUpTrap,
       "panHWInsufficientPowerTrap": panHWInsufficientPowerTrap,
       "panHWSlotUnsupportedTrap": panHWSlotUnsupportedTrap,
       "panHWSlotStartingTrap": panHWSlotStartingTrap,
       "panHWSlotStoppingTrap": panHWSlotStoppingTrap,
       "panHWSlotFailureTrap": panHWSlotFailureTrap,
       "panHWSlotPoweroffTrap": panHWSlotPoweroffTrap,
       "panHWSlotAdminpoweroffTrap": panHWSlotAdminpoweroffTrap,
       "panHWSlotInsertedTrap": panHWSlotInsertedTrap,
       "panHWSlotRemovedTrap": panHWSlotRemovedTrap,
       "panHWPsInsertedTrap": panHWPsInsertedTrap,
       "panHWPsRemovedTrap": panHWPsRemovedTrap,
       "panHWPsFailureTrap": panHWPsFailureTrap,
       "panHWFanInsertedTrap": panHWFanInsertedTrap,
       "panHWFanRemovedTrap": panHWFanRemovedTrap,
       "panHWFanFailureTrap": panHWFanFailureTrap,
       "panNTDPRestartTrap": panNTDPRestartTrap,
       "panNTDPTimeLearnTrap": panNTDPTimeLearnTrap,
       "panNTDPSyncTrap": panNTDPSyncTrap,
       "panNTDPAuthTrap": panNTDPAuthTrap,
       "panPBFNhUpTrap": panPBFNhUpTrap,
       "panPBFNhDownTrap": panPBFNhDownTrap,
       "panPORTLinkChangeTrap": panPORTLinkChangeTrap,
       "panPORTNonqualSfpTrap": panPORTNonqualSfpTrap,
       "panPORTNonqualSfpPlusTrap": panPORTNonqualSfpPlusTrap,
       "panPORTNonqualXfpTrap": panPORTNonqualXfpTrap,
       "panPORTNonsuppForcedTrap": panPORTNonsuppForcedTrap,
       "panPPPOEInitiateTrap": panPPPOEInitiateTrap,
       "panPPPOEConnectTrap": panPPPOEConnectTrap,
       "panPPPOEConnectFailTrap": panPPPOEConnectFailTrap,
       "panPPPOETerminateTrap": panPPPOETerminateTrap,
       "panPPPOEIfUpdateFailTrap": panPPPOEIfUpdateFailTrap,
       "panRASRasmgrConfigP1SuccessTrap": panRASRasmgrConfigP1SuccessTrap,
       "panRASRasmgrConfigP1FailedTrap": panRASRasmgrConfigP1FailedTrap,
       "panRASRasmgrConfigP1AbortTrap": panRASRasmgrConfigP1AbortTrap,
       "panRASRasmgrConfigP2SuccessTrap": panRASRasmgrConfigP2SuccessTrap,
       "panRASRasmgrConfigP2FailedTrap": panRASRasmgrConfigP2FailedTrap,
       "panRASRasmgrDaemonStartTrap": panRASRasmgrDaemonStartTrap,
       "panRASRasmgrDaemonExitTrap": panRASRasmgrDaemonExitTrap,
       "panRASRasmgrDaemonInitTrap": panRASRasmgrDaemonInitTrap,
       "panRASRasmgrFlowFullSyncStartTrap": panRASRasmgrFlowFullSyncStartTrap,
       "panRASRasmgrFlowFullSyncAbortTrap": panRASRasmgrFlowFullSyncAbortTrap,
       "panRASRasmgrFlowFullSyncDoneTrap": panRASRasmgrFlowFullSyncDoneTrap,
       "panRASRasmgrHaFullSyncStartTrap": panRASRasmgrHaFullSyncStartTrap,
       "panRASRasmgrHaFullSyncAbortTrap": panRASRasmgrHaFullSyncAbortTrap,
       "panRASRasmgrHaFullSyncDoneTrap": panRASRasmgrHaFullSyncDoneTrap,
       "panROUTINGRoutedConfigP1SuccessTrap": panROUTINGRoutedConfigP1SuccessTrap,
       "panROUTINGRoutedConfigP1FailedTrap": panROUTINGRoutedConfigP1FailedTrap,
       "panROUTINGRoutedConfigP1AbortTrap": panROUTINGRoutedConfigP1AbortTrap,
       "panROUTINGRoutedConfigP2SuccessTrap": panROUTINGRoutedConfigP2SuccessTrap,
       "panROUTINGRoutedConfigP2FailedTrap": panROUTINGRoutedConfigP2FailedTrap,
       "panROUTINGRoutedDaemonStartTrap": panROUTINGRoutedDaemonStartTrap,
       "panROUTINGRoutedDaemonExitTrap": panROUTINGRoutedDaemonExitTrap,
       "panROUTINGRoutedDaemonInitTrap": panROUTINGRoutedDaemonInitTrap,
       "panROUTINGRoutedFibSyncPeerBackupTrap": panROUTINGRoutedFibSyncPeerBackupTrap,
       "panROUTINGRoutedFibSyncSelfMasterTrap": panROUTINGRoutedFibSyncSelfMasterTrap,
       "panROUTINGRoutedRTMBadRouteTrap": panROUTINGRoutedRTMBadRouteTrap,
       "panROUTINGRoutedOSPFLSAChksumFailedTrap": panROUTINGRoutedOSPFLSAChksumFailedTrap,
       "panROUTINGRoutedOSPFLSAChksumInvalidTrap": panROUTINGRoutedOSPFLSAChksumInvalidTrap,
       "panROUTINGRoutedOSPFAuthtypeBadTrap": panROUTINGRoutedOSPFAuthtypeBadTrap,
       "panROUTINGRoutedOSPFPasswordBadTrap": panROUTINGRoutedOSPFPasswordBadTrap,
       "panROUTINGRoutedOSPFChksumBadTrap": panROUTINGRoutedOSPFChksumBadTrap,
       "panROUTINGRoutedOSPFSequenceBadTrap": panROUTINGRoutedOSPFSequenceBadTrap,
       "panROUTINGRoutedOSPFMd5chksumBadTrap": panROUTINGRoutedOSPFMd5chksumBadTrap,
       "panROUTINGRoutedOSPFMd5lengthBadTrap": panROUTINGRoutedOSPFMd5lengthBadTrap,
       "panROUTINGRoutedOSPFHelloHelloIntvalBadTrap": panROUTINGRoutedOSPFHelloHelloIntvalBadTrap,
       "panROUTINGRoutedOSPFHelloDeadIntvalBadTrap": panROUTINGRoutedOSPFHelloDeadIntvalBadTrap,
       "panROUTINGRoutedOSPFHelloNetmaskBadTrap": panROUTINGRoutedOSPFHelloNetmaskBadTrap,
       "panROUTINGRoutedOSPFHelloAreaTypeBadTrap": panROUTINGRoutedOSPFHelloAreaTypeBadTrap,
       "panROUTINGRoutedOSPFNeighbor2dirTrap": panROUTINGRoutedOSPFNeighbor2dirTrap,
       "panROUTINGRoutedOSPFNeighborFullTrap": panROUTINGRoutedOSPFNeighborFullTrap,
       "panROUTINGRoutedOSPFNeighborDownTrap": panROUTINGRoutedOSPFNeighborDownTrap,
       "panROUTINGRoutedRIPPeerAddTrap": panROUTINGRoutedRIPPeerAddTrap,
       "panROUTINGRoutedRIPPeerDelTrap": panROUTINGRoutedRIPPeerDelTrap,
       "panROUTINGRoutedRIPAuthtypeBadTrap": panROUTINGRoutedRIPAuthtypeBadTrap,
       "panROUTINGRoutedRIPAuthFailedTrap": panROUTINGRoutedRIPAuthFailedTrap,
       "panROUTINGRoutedRIPMd5lengthBadTrap": panROUTINGRoutedRIPMd5lengthBadTrap,
       "panROUTINGRoutedBGPPeerEnterEstablishedTrap": panROUTINGRoutedBGPPeerEnterEstablishedTrap,
       "panROUTINGRoutedBGPPeerLeftEstablishedTrap": panROUTINGRoutedBGPPeerLeftEstablishedTrap,
       "panROUTINGRoutedBGPPeerFailedTrap": panROUTINGRoutedBGPPeerFailedTrap,
       "panROUTINGRoutedBGPPeerRestartedTrap": panROUTINGRoutedBGPPeerRestartedTrap,
       "panROUTINGRoutedBGPPeerRestartFailedTrap": panROUTINGRoutedBGPPeerRestartFailedTrap,
       "panROUTINGRoutedBGPRefreshSentTrap": panROUTINGRoutedBGPRefreshSentTrap,
       "panROUTINGRoutedBGPRibinRecalcTrap": panROUTINGRoutedBGPRibinRecalcTrap,
       "panROUTINGRoutedPIMInterfaceStateChangedTrap": panROUTINGRoutedPIMInterfaceStateChangedTrap,
       "panROUTINGRoutedPIMNewDrElectedTrap": panROUTINGRoutedPIMNewDrElectedTrap,
       "panROUTINGRoutedPIMNeighborDiscoveredTrap": panROUTINGRoutedPIMNeighborDiscoveredTrap,
       "panROUTINGRoutedPIMNeighborDisappearedTrap": panROUTINGRoutedPIMNeighborDisappearedTrap,
       "panROUTINGRoutedIGMPWrongVersionTrap": panROUTINGRoutedIGMPWrongVersionTrap,
       "panROUTINGRoutedGenericEventTrap": panROUTINGRoutedGenericEventTrap,
       "panROUTINGRoutedOSPFStartGracefulRestartTrap": panROUTINGRoutedOSPFStartGracefulRestartTrap,
       "panROUTINGRoutedOSPFStoppedGracefulRestartTrap": panROUTINGRoutedOSPFStoppedGracefulRestartTrap,
       "panROUTINGRoutedOSPFStartHelperNodeTrap": panROUTINGRoutedOSPFStartHelperNodeTrap,
       "panROUTINGRoutedOSPFStopHelperModeTrap": panROUTINGRoutedOSPFStopHelperModeTrap,
       "panROUTINGRoutedOSPFNotHelpTrap": panROUTINGRoutedOSPFNotHelpTrap,
       "panROUTINGRoutedECMPTrap": panROUTINGRoutedECMPTrap,
       "panSSLVPNSslvpnRegistSuccTrap": panSSLVPNSslvpnRegistSuccTrap,
       "panSSLVPNSslvpnRegistFailTrap": panSSLVPNSslvpnRegistFailTrap,
       "panSSLVPNSslvpnLogoutSuccTrap": panSSLVPNSslvpnLogoutSuccTrap,
       "panSSLVPNSslvpnLogoutFailTrap": panSSLVPNSslvpnLogoutFailTrap,
       "panSSLVPNSslvpnConfigSuccTrap": panSSLVPNSslvpnConfigSuccTrap,
       "panSSLVPNSslvpnConfigFailTrap": panSSLVPNSslvpnConfigFailTrap,
       "panSSLVPNSslvpnConfigReleaseTrap": panSSLVPNSslvpnConfigReleaseTrap,
       "panSSLVPNSslvpnSwitchSuccTrap": panSSLVPNSslvpnSwitchSuccTrap,
       "panSSLVPNSslvpnSwitchFailTrap": panSSLVPNSslvpnSwitchFailTrap,
       "panSSLVPNSslvpnAuthSuccTrap": panSSLVPNSslvpnAuthSuccTrap,
       "panSSLVPNSslvpnAuthFailTrap": panSSLVPNSslvpnAuthFailTrap,
       "panVPNIkeConfigP1SuccessTrap": panVPNIkeConfigP1SuccessTrap,
       "panVPNIkeConfigP1FailedTrap": panVPNIkeConfigP1FailedTrap,
       "panVPNIkeConfigP1AbortTrap": panVPNIkeConfigP1AbortTrap,
       "panVPNIkeConfigP2SuccessTrap": panVPNIkeConfigP2SuccessTrap,
       "panVPNIkeConfigP2FailedTrap": panVPNIkeConfigP2FailedTrap,
       "panVPNIkeDaemonStartTrap": panVPNIkeDaemonStartTrap,
       "panVPNIkeDaemonExitTrap": panVPNIkeDaemonExitTrap,
       "panVPNIkeDaemonInitTrap": panVPNIkeDaemonInitTrap,
       "panVPNIkeNegoP1StartTrap": panVPNIkeNegoP1StartTrap,
       "panVPNIkeNegoP1FailTrap": panVPNIkeNegoP1FailTrap,
       "panVPNIkeNegoP1SuccTrap": panVPNIkeNegoP1SuccTrap,
       "panVPNIkeNegoP1ExpireTrap": panVPNIkeNegoP1ExpireTrap,
       "panVPNIkeNegoP1DeleteTrap": panVPNIkeNegoP1DeleteTrap,
       "panVPNIkeNegoP1DpdDnTrap": panVPNIkeNegoP1DpdDnTrap,
       "panVPNIkeNegoP1PskIdtypeTrap": panVPNIkeNegoP1PskIdtypeTrap,
       "panVPNIkeNegoP1FailPskTrap": panVPNIkeNegoP1FailPskTrap,
       "panVPNIkeNegoP1FailCommonTrap": panVPNIkeNegoP1FailCommonTrap,
       "panVPNIkeNegoP2StartTrap": panVPNIkeNegoP2StartTrap,
       "panVPNIkeNegoP2FailTrap": panVPNIkeNegoP2FailTrap,
       "panVPNIkeNegoP2SuccTrap": panVPNIkeNegoP2SuccTrap,
       "panVPNIkeNegoP2StaleP1Trap": panVPNIkeNegoP2StaleP1Trap,
       "panVPNIkeNegoP2DupRekeyTrap": panVPNIkeNegoP2DupRekeyTrap,
       "panVPNIkeNegoP2SimulContTrap": panVPNIkeNegoP2SimulContTrap,
       "panVPNIkeNegoP2SimulFailTrap": panVPNIkeNegoP2SimulFailTrap,
       "panVPNIkeNegoP2SimulDelayTrap": panVPNIkeNegoP2SimulDelayTrap,
       "panVPNIkeNegoP2NoP1Trap": panVPNIkeNegoP2NoP1Trap,
       "panVPNIkeNegoP2P1NotReadyTrap": panVPNIkeNegoP2P1NotReadyTrap,
       "panVPNIkeNegoP2ProxyIdBadTrap": panVPNIkeNegoP2ProxyIdBadTrap,
       "panVPNIkeNegoP2ProposalBadTrap": panVPNIkeNegoP2ProposalBadTrap,
       "panVPNIpsecKeyInstallTrap": panVPNIpsecKeyInstallTrap,
       "panVPNIpsecKeyDeleteTrap": panVPNIpsecKeyDeleteTrap,
       "panVPNIpsecKeyExpireTrap": panVPNIpsecKeyExpireTrap,
       "panVPNIkeRecvNotifyTrap": panVPNIkeRecvNotifyTrap,
       "panVPNIkeRecvP1DeleteTrap": panVPNIkeRecvP1DeleteTrap,
       "panVPNIkeRecvP2DeleteTrap": panVPNIkeRecvP2DeleteTrap,
       "panVPNIkeSendNotifyTrap": panVPNIkeSendNotifyTrap,
       "panVPNIkeSendP1DeleteTrap": panVPNIkeSendP1DeleteTrap,
       "panVPNIkeSendP2DeleteTrap": panVPNIkeSendP2DeleteTrap,
       "panVPNIkev2NegoIkeStartTrap": panVPNIkev2NegoIkeStartTrap,
       "panVPNIkev2NegoIkeFailTrap": panVPNIkev2NegoIkeFailTrap,
       "panVPNIkev2NegoIkeSuccTrap": panVPNIkev2NegoIkeSuccTrap,
       "panVPNIkev2NegoIkeExpireTrap": panVPNIkev2NegoIkeExpireTrap,
       "panVPNIkev2NegoIkeDeleteTrap": panVPNIkev2NegoIkeDeleteTrap,
       "panVPNIkev2NegoChildStartTrap": panVPNIkev2NegoChildStartTrap,
       "panVPNIkev2NegoChildFailTrap": panVPNIkev2NegoChildFailTrap,
       "panVPNIkev2NegoChildSuccTrap": panVPNIkev2NegoChildSuccTrap,
       "panVPNTunnelStatusUpTrap": panVPNTunnelStatusUpTrap,
       "panVPNTunnelStatusDownTrap": panVPNTunnelStatusDownTrap,
       "panVPNKeymgrDaemonStartTrap": panVPNKeymgrDaemonStartTrap,
       "panVPNKeymgrDaemonExitTrap": panVPNKeymgrDaemonExitTrap,
       "panVPNKeymgrDaemonInitTrap": panVPNKeymgrDaemonInitTrap,
       "panVPNKeymgrFlowFullSyncStartTrap": panVPNKeymgrFlowFullSyncStartTrap,
       "panVPNKeymgrFlowFullSyncAbortTrap": panVPNKeymgrFlowFullSyncAbortTrap,
       "panVPNKeymgrFlowFullSyncDoneTrap": panVPNKeymgrFlowFullSyncDoneTrap,
       "panVPNKeymgrIkeFullSyncStartTrap": panVPNKeymgrIkeFullSyncStartTrap,
       "panVPNKeymgrIkeFullSyncAbortTrap": panVPNKeymgrIkeFullSyncAbortTrap,
       "panVPNKeymgrIkeFullSyncDoneTrap": panVPNKeymgrIkeFullSyncDoneTrap,
       "panVPNKeymgrHaFullSyncStartTrap": panVPNKeymgrHaFullSyncStartTrap,
       "panVPNKeymgrHaFullSyncAbortTrap": panVPNKeymgrHaFullSyncAbortTrap,
       "panVPNKeymgrHaFullSyncDoneTrap": panVPNKeymgrHaFullSyncDoneTrap,
       "panVPNIkeGenericEventTrap": panVPNIkeGenericEventTrap,
       "panVPNKeymgrGenericEventTrap": panVPNKeymgrGenericEventTrap,
       "panVPNIkeNegoP1FailCertTrap": panVPNIkeNegoP1FailCertTrap,
       "panVPNIkeNegoP1CertIdMismatchTrap": panVPNIkeNegoP1CertIdMismatchTrap,
       "panVPNIkeNegoP1CertSuccTrap": panVPNIkeNegoP1CertSuccTrap,
       "panVPNIkev2NegoIkeDpdDnTrap": panVPNIkev2NegoIkeDpdDnTrap,
       "panVPNIkev2NegoPskIdtypeTrap": panVPNIkev2NegoPskIdtypeTrap,
       "panVPNIkev2NegoFailPskTrap": panVPNIkev2NegoFailPskTrap,
       "panVPNIkev2NegoFailCommonTrap": panVPNIkev2NegoFailCommonTrap,
       "panVPNIkev2NegoFailCertTrap": panVPNIkev2NegoFailCertTrap,
       "panVPNIkev2NegoCertIdMismatchTrap": panVPNIkev2NegoCertIdMismatchTrap,
       "panVPNIkev2NegoCertSuccTrap": panVPNIkev2NegoCertSuccTrap,
       "panVPNIkev2NegoUseV1Trap": panVPNIkev2NegoUseV1Trap,
       "panVPNIkev2NegoStaleP1Trap": panVPNIkev2NegoStaleP1Trap,
       "panVPNIkev2NegoStaleP2Trap": panVPNIkev2NegoStaleP2Trap,
       "panVPNIkev2NegoChildDupRekeyTrap": panVPNIkev2NegoChildDupRekeyTrap,
       "panVPNIkev2NegoChildSimulContTrap": panVPNIkev2NegoChildSimulContTrap,
       "panVPNIkev2NegoChildSimulFailTrap": panVPNIkev2NegoChildSimulFailTrap,
       "panVPNIkev2NegoChildSimulDelayTrap": panVPNIkev2NegoChildSimulDelayTrap,
       "panVPNIkev2NegoChildNoP1Trap": panVPNIkev2NegoChildNoP1Trap,
       "panVPNIkev2NegoChildP1NotReadyTrap": panVPNIkev2NegoChildP1NotReadyTrap,
       "panVPNIkev2NegoChildTsBadTrap": panVPNIkev2NegoChildTsBadTrap,
       "panVPNIkev2NegoChildProposalBadTrap": panVPNIkev2NegoChildProposalBadTrap,
       "panVPNIkev2RecvNotifyTrap": panVPNIkev2RecvNotifyTrap,
       "panVPNIkev2RecvP1DeleteTrap": panVPNIkev2RecvP1DeleteTrap,
       "panVPNIkev2RecvP2DeleteTrap": panVPNIkev2RecvP2DeleteTrap,
       "panVPNIkev2SendNotifyTrap": panVPNIkev2SendNotifyTrap,
       "panVPNIkev2SendP1DeleteTrap": panVPNIkev2SendP1DeleteTrap,
       "panVPNIkev2SendP2DeleteTrap": panVPNIkev2SendP2DeleteTrap,
       "panSATDSatdConfigP1SuccessTrap": panSATDSatdConfigP1SuccessTrap,
       "panSATDSatdConfigP1FailedTrap": panSATDSatdConfigP1FailedTrap,
       "panSATDSatdConfigP1AbortTrap": panSATDSatdConfigP1AbortTrap,
       "panSATDSatdConfigP2SuccessTrap": panSATDSatdConfigP2SuccessTrap,
       "panSATDSatdConfigP2FailedTrap": panSATDSatdConfigP2FailedTrap,
       "panSATDSatdDaemonStartTrap": panSATDSatdDaemonStartTrap,
       "panSATDSatdDaemonExitTrap": panSATDSatdDaemonExitTrap,
       "panSATDSatdDaemonInitTrap": panSATDSatdDaemonInitTrap,
       "panSATDSatdTunUpTrap": panSATDSatdTunUpTrap,
       "panSATDSatdTunDownTrap": panSATDSatdTunDownTrap,
       "panSATDSatdDupSubnetsTrap": panSATDSatdDupSubnetsTrap,
       "panSATDSatdDeniedRoutesTrap": panSATDSatdDeniedRoutesTrap,
       "panSATDSatdPortalGatewayDuplicateTrap": panSATDSatdPortalGatewayDuplicateTrap,
       "panSATDSatdFlowFullSyncStartTrap": panSATDSatdFlowFullSyncStartTrap,
       "panSATDSatdFlowFullSyncAbortTrap": panSATDSatdFlowFullSyncAbortTrap,
       "panSATDSatdFlowFullSyncDoneTrap": panSATDSatdFlowFullSyncDoneTrap,
       "panSATDSatdHaFullSyncStartTrap": panSATDSatdHaFullSyncStartTrap,
       "panSATDSatdHaFullSyncAbortTrap": panSATDSatdHaFullSyncAbortTrap,
       "panSATDSatdHaFullSyncDoneTrap": panSATDSatdHaFullSyncDoneTrap,
       "panSATDSatdIpAssignFailTrap": panSATDSatdIpAssignFailTrap,
       "panSATDSatdIpResetFailTrap": panSATDSatdIpResetFailTrap,
       "panSATDSatdTunMonDownTrap": panSATDSatdTunMonDownTrap,
       "panSATDSatdTunMonUpTrap": panSATDSatdTunMonUpTrap,
       "panSATDSatdTunSoftlifetimeExpiredTrap": panSATDSatdTunSoftlifetimeExpiredTrap,
       "panSATDSatdTunHardlifetimeExpiredTrap": panSATDSatdTunHardlifetimeExpiredTrap,
       "panSATDSatdAccRouteUpdFailTrap": panSATDSatdAccRouteUpdFailTrap,
       "panSATDSatdNhUpdFailTrap": panSATDSatdNhUpdFailTrap,
       "panSATDSatdTunDpInstallErrTrap": panSATDSatdTunDpInstallErrTrap,
       "panSATDSatdGatewayConnectStartedTrap": panSATDSatdGatewayConnectStartedTrap,
       "panSATDSatdPortalConnectStartedTrap": panSATDSatdPortalConnectStartedTrap,
       "panSATDSatdGatewayConnectFailedTrap": panSATDSatdGatewayConnectFailedTrap,
       "panSATDSatdPortalConnectFailedTrap": panSATDSatdPortalConnectFailedTrap,
       "panSATDSatdGenericEventTrap": panSATDSatdGenericEventTrap,
       "panSSLMGRSslmgrConfigP1SuccessTrap": panSSLMGRSslmgrConfigP1SuccessTrap,
       "panSSLMGRSslmgrConfigP1FailedTrap": panSSLMGRSslmgrConfigP1FailedTrap,
       "panSSLMGRSslmgrConfigP1AbortTrap": panSSLMGRSslmgrConfigP1AbortTrap,
       "panSSLMGRSslmgrConfigP2SuccessTrap": panSSLMGRSslmgrConfigP2SuccessTrap,
       "panSSLMGRSslmgrConfigP2FailedTrap": panSSLMGRSslmgrConfigP2FailedTrap,
       "panSSLMGRSslmgrDaemonStartTrap": panSSLMGRSslmgrDaemonStartTrap,
       "panSSLMGRSslmgrDaemonExitTrap": panSSLMGRSslmgrDaemonExitTrap,
       "panSSLMGRSslmgrCertGenSuccessTrap": panSSLMGRSslmgrCertGenSuccessTrap,
       "panSSLMGRSslmgrCertGenFailedTrap": panSSLMGRSslmgrCertGenFailedTrap,
       "panSSLMGRSslmgrCertStatusDeletedTrap": panSSLMGRSslmgrCertStatusDeletedTrap,
       "panSSLMGRSslmgrCertStatusRevokedTrap": panSSLMGRSslmgrCertStatusRevokedTrap,
       "panSSLMGRSslmgrSatelliteInfoInsertedTrap": panSSLMGRSslmgrSatelliteInfoInsertedTrap,
       "panSSLMGRSslmgrSatelliteInfoUpdatedTrap": panSSLMGRSslmgrSatelliteInfoUpdatedTrap,
       "panSSLMGRSslmgrSatelliteInfoDeletedTrap": panSSLMGRSslmgrSatelliteInfoDeletedTrap,
       "panSSLMGRSslmgrCertOcspVerifyFailedTrap": panSSLMGRSslmgrCertOcspVerifyFailedTrap,
       "panSSLMGRSslmgrCertCrlVerifyFailedTrap": panSSLMGRSslmgrCertCrlVerifyFailedTrap,
       "panSSLMGRSslmgrHaFullSyncTrap": panSSLMGRSslmgrHaFullSyncTrap,
       "panSSLMGRSslmgrHaNotFullSyncTrap": panSSLMGRSslmgrHaNotFullSyncTrap,
       "panSSLMGRSslmgrGenericEventTrap": panSSLMGRSslmgrGenericEventTrap,
       "panURLNoUrlDatabaseTrap": panURLNoUrlDatabaseTrap,
       "panURLInvalidLicenseTrap": panURLInvalidLicenseTrap,
       "panURLFailedToLockUpdateTrap": panURLFailedToLockUpdateTrap,
       "panURLConnectionSuccessTrap": panURLConnectionSuccessTrap,
       "panURLConnectionFailureTrap": panURLConnectionFailureTrap,
       "panURLServerIsDownTrap": panURLServerIsDownTrap,
       "panURLProxyConnectionFailureTrap": panURLProxyConnectionFailureTrap,
       "panURLReceiveDataFailureTrap": panURLReceiveDataFailureTrap,
       "panURLDynamicUrlConnectionDownTrap": panURLDynamicUrlConnectionDownTrap,
       "panURLDownloadingUrlDatabaseTrap": panURLDownloadingUrlDatabaseTrap,
       "panURLDownloadUrlDatabaseSuccessTrap": panURLDownloadUrlDatabaseSuccessTrap,
       "panURLUpgradeUrlDatabaseSuccessTrap": panURLUpgradeUrlDatabaseSuccessTrap,
       "panURLRevertUrlDatabaseSuccessTrap": panURLRevertUrlDatabaseSuccessTrap,
       "panURLUrlDatabaseIsLatestTrap": panURLUrlDatabaseIsLatestTrap,
       "panURLUrlDownloadFailureTrap": panURLUrlDownloadFailureTrap,
       "panURLUrlCloudConnectionFailureTrap": panURLUrlCloudConnectionFailureTrap,
       "panURLUrlCloudConnectionSuccessTrap": panURLUrlCloudConnectionSuccessTrap,
       "panURLUrlBackupSeedSuccessTrap": panURLUrlBackupSeedSuccessTrap,
       "panURLUrlBackupSeedFailureTrap": panURLUrlBackupSeedFailureTrap,
       "panURLCloudElectionTrap": panURLCloudElectionTrap,
       "panURLCloudProcessStartsTrap": panURLCloudProcessStartsTrap,
       "panURLCloudProcessStoppedTrap": panURLCloudProcessStoppedTrap,
       "panURLUpdateVersionFailureTrap": panURLUpdateVersionFailureTrap,
       "panURLErrorMsgFromCloudTrap": panURLErrorMsgFromCloudTrap,
       "panURLTestASiteTrap": panURLTestASiteTrap,
       "panURLUrlEngineStoppedTrap": panURLUrlEngineStoppedTrap,
       "panURLUrlEngineStartsTrap": panURLUrlEngineStartsTrap,
       "panURLStartupFailureTrap": panURLStartupFailureTrap,
       "panURLHaSyncFailureTrap": panURLHaSyncFailureTrap,
       "panURLHaSyncSuccessTrap": panURLHaSyncSuccessTrap,
       "panURLSaveMpCacheToDiscFailureTrap": panURLSaveMpCacheToDiscFailureTrap,
       "panURLSaveMpCacheToDiscSuccessTrap": panURLSaveMpCacheToDiscSuccessTrap,
       "panURLRfsProcessStartsTrap": panURLRfsProcessStartsTrap,
       "panURLRfsProcessStoppedTrap": panURLRfsProcessStoppedTrap,
       "panURLRfsProcessFailureTrap": panURLRfsProcessFailureTrap,
       "panURLRequestToCloudFailureTrap": panURLRequestToCloudFailureTrap,
       "panURLStartsFromEmptySeedTrap": panURLStartsFromEmptySeedTrap,
       "panURLLoadSuccessTrap": panURLLoadSuccessTrap,
       "panURLFailedToLockDownloadTrap": panURLFailedToLockDownloadTrap,
       "panURLEngineStartupFailureTrap": panURLEngineStartupFailureTrap,
       "panURLSeedOutOfSyncTrap": panURLSeedOutOfSyncTrap,
       "panURLStartsFromBackupSeedTrap": panURLStartsFromBackupSeedTrap,
       "panURLStartsFromDownloadSeedTrap": panURLStartsFromDownloadSeedTrap,
       "panURLBackupSeedErrorTrap": panURLBackupSeedErrorTrap,
       "panURLDownloadSeedErrorTrap": panURLDownloadSeedErrorTrap,
       "panUSERIDConnectAgentTrap": panUSERIDConnectAgentTrap,
       "panUSERIDDisconnectAgentTrap": panUSERIDDisconnectAgentTrap,
       "panUSERIDAgentEventTrap": panUSERIDAgentEventTrap,
       "panUSERIDConnectAgentFailureTrap": panUSERIDConnectAgentFailureTrap,
       "panUSERIDAgentVersionMismatchTrap": panUSERIDAgentVersionMismatchTrap,
       "panUSERIDAgentStatusFailureTrap": panUSERIDAgentStatusFailureTrap,
       "panUSERIDAgentReadLogErrorTrap": panUSERIDAgentReadLogErrorTrap,
       "panUSERIDAgentGetDomainErrorTrap": panUSERIDAgentGetDomainErrorTrap,
       "panUSERIDAgentGetUsersErrorTrap": panUSERIDAgentGetUsersErrorTrap,
       "panUSERIDAgentGetGroupsErrorTrap": panUSERIDAgentGetGroupsErrorTrap,
       "panUSERIDAgentGetConfigErrorTrap": panUSERIDAgentGetConfigErrorTrap,
       "panUSERIDAgentNoDomainTrap": panUSERIDAgentNoDomainTrap,
       "panUSERIDAgentNoAllowlistTrap": panUSERIDAgentNoAllowlistTrap,
       "panUSERIDConnectLdapSeverTrap": panUSERIDConnectLdapSeverTrap,
       "panUSERIDConnectLdapSeverFailureTrap": panUSERIDConnectLdapSeverFailureTrap,
       "panUSERIDGetLdapDataFailureTrap": panUSERIDGetLdapDataFailureTrap,
       "panUSERIDHAQueueFullTrap": panUSERIDHAQueueFullTrap,
       "panUSERIDConnectClientTrap": panUSERIDConnectClientTrap,
       "panUSERIDDisconnectClientTrap": panUSERIDDisconnectClientTrap,
       "panUSERIDConnectServerMonitorTrap": panUSERIDConnectServerMonitorTrap,
       "panUSERIDConnectServerMonitorFailureTrap": panUSERIDConnectServerMonitorFailureTrap,
       "panUSERIDConnectVmInfoSourceTrap": panUSERIDConnectVmInfoSourceTrap,
       "panUSERIDDisconnectVmInfoSourceTrap": panUSERIDDisconnectVmInfoSourceTrap,
       "panUSERIDConnectVmInfoSourceFailureTrap": panUSERIDConnectVmInfoSourceFailureTrap,
       "panUSERIDRegisteredIpUpdateFailureTrap": panUSERIDRegisteredIpUpdateFailureTrap,
       "panUSERIDConnectSyslogTrap": panUSERIDConnectSyslogTrap,
       "panUSERIDDisconnectSyslogTrap": panUSERIDDisconnectSyslogTrap,
       "panNATFallbackReportTrap": panNATFallbackReportTrap,
       "panSYSLOGNGSyslogConnStatusTrap": panSYSLOGNGSyslogConnStatusTrap,
       "panLACPLostConnectivityTrap": panLACPLostConnectivityTrap,
       "panLACPUnresponsiveTrap": panLACPUnresponsiveTrap,
       "panLACPNegoFailTrap": panLACPNegoFailTrap,
       "panLACPSpeedDuplexTrap": panLACPSpeedDuplexTrap,
       "panLACPLinkDownTrap": panLACPLinkDownTrap,
       "panLACPLacpDownTrap": panLACPLacpDownTrap,
       "panLACPLacpUpTrap": panLACPLacpUpTrap,
       "panFIPSFipsSelftestUnknownTrap": panFIPSFipsSelftestUnknownTrap,
       "panFIPSFipsSelftestTimeoutTrap": panFIPSFipsSelftestTimeoutTrap,
       "panFIPSFipsSelftestIntegTrap": panFIPSFipsSelftestIntegTrap,
       "panFIPSFipsSelftestCoreTrap": panFIPSFipsSelftestCoreTrap,
       "panFIPSFipsSelftestAesTrap": panFIPSFipsSelftestAesTrap,
       "panFIPSFipsSelftestDesTrap": panFIPSFipsSelftestDesTrap,
       "panFIPSFipsSelftestDsaTrap": panFIPSFipsSelftestDsaTrap,
       "panFIPSFipsSelftestRsaTrap": panFIPSFipsSelftestRsaTrap,
       "panFIPSFipsSelftestHmacTrap": panFIPSFipsSelftestHmacTrap,
       "panFIPSFipsSelftestShaTrap": panFIPSFipsSelftestShaTrap,
       "panFIPSFipsSelftestDrngTrap": panFIPSFipsSelftestDrngTrap,
       "panFIPSFipsSelftestNdrngTrap": panFIPSFipsSelftestNdrngTrap,
       "panFIPSFipsSelftestDhParameterTrap": panFIPSFipsSelftestDhParameterTrap,
       "panFIPSFipsSelftestDhTrap": panFIPSFipsSelftestDhTrap,
       "panFIPSFipsFirmwareIntegrityTrap": panFIPSFipsFirmwareIntegrityTrap,
       "panFIPSFipsContinuousRngTrap": panFIPSFipsContinuousRngTrap,
       "panFIPSFipsRsaPairwiseConsistencyTrap": panFIPSFipsRsaPairwiseConsistencyTrap,
       "panFIPSFipsSelftestSoftwareLoadTrap": panFIPSFipsSelftestSoftwareLoadTrap,
       "panFIPSFipsSelftestTrap": panFIPSFipsSelftestTrap,
       "panFIPSFipsSelftestHsmTrap": panFIPSFipsSelftestHsmTrap,
       "panFIPSFipsZeroizationTrap": panFIPSFipsZeroizationTrap,
       "panFIPSFipsKeyTrap": panFIPSFipsKeyTrap,
       "panFIPSFipsCipherTrap": panFIPSFipsCipherTrap,
       "panFIPSFipsReplayTrap": panFIPSFipsReplayTrap,
       "panFIPSFipsSslHandshakeTrap": panFIPSFipsSslHandshakeTrap,
       "panFIPSFipsContinuousNdrngTrap": panFIPSFipsContinuousNdrngTrap,
       "panFIPSFipsSelftestCmacTrap": panFIPSFipsSelftestCmacTrap,
       "panFIPSFipsSelftestDrbgTrap": panFIPSFipsSelftestDrbgTrap,
       "panFIPSFipsSelftestEcdsaTrap": panFIPSFipsSelftestEcdsaTrap,
       "panFIPSFipsSelftestEcdhTrap": panFIPSFipsSelftestEcdhTrap,
       "panMDMExceedLicenseTrap": panMDMExceedLicenseTrap,
       "panMDMConnectToApnsTrap": panMDMConnectToApnsTrap,
       "panMDMConnectToApnsFailureTrap": panMDMConnectToApnsFailureTrap,
       "panMDMConnectToGcmTrap": panMDMConnectToGcmTrap,
       "panMDMConnectToGcmFailureTrap": panMDMConnectToGcmFailureTrap,
       "panMDMGatewayConnectedTrap": panMDMGatewayConnectedTrap,
       "panMDMGatewayDisconnectedTrap": panMDMGatewayDisconnectedTrap,
       "panMDMInstallAppContentTrap": panMDMInstallAppContentTrap,
       "panMDMInstallAppContentFailureTrap": panMDMInstallAppContentFailureTrap,
       "panMDMGetScepOtpFailureTrap": panMDMGetScepOtpFailureTrap,
       "panMDMSendMsgToCloudFailureTrap": panMDMSendMsgToCloudFailureTrap,
       "panMDMConnectToItunesFailureTrap": panMDMConnectToItunesFailureTrap,
       "panMDMConnectToAppleVppFailureTrap": panMDMConnectToAppleVppFailureTrap,
       "panRAIDDiskNotDetectedTrap": panRAIDDiskNotDetectedTrap,
       "panRAIDPairDetectedTrap": panRAIDPairDetectedTrap,
       "panRAIDRebuildingTrap": panRAIDRebuildingTrap,
       "panRAIDRebuild20Trap": panRAIDRebuild20Trap,
       "panRAIDRebuild40Trap": panRAIDRebuild40Trap,
       "panRAIDRebuild60Trap": panRAIDRebuild60Trap,
       "panRAIDRebuild80Trap": panRAIDRebuild80Trap,
       "panRAIDRebuildDoneTrap": panRAIDRebuildDoneTrap,
       "panRAIDDiskActiveTrap": panRAIDDiskActiveTrap,
       "panRAIDDiskFaultyTrap": panRAIDDiskFaultyTrap,
       "panRAIDDiskFailedTrap": panRAIDDiskFailedTrap,
       "panRAIDSpareMissingTrap": panRAIDSpareMissingTrap,
       "panRAIDSpareMovedTrap": panRAIDSpareMovedTrap,
       "panRAIDPairDegradedTrap": panRAIDPairDegradedTrap,
       "panRAIDPairDisappearedTrap": panRAIDPairDisappearedTrap,
       "panRAIDDiskRemovedTrap": panRAIDDiskRemovedTrap,
       "panRAIDFsckStartTrap": panRAIDFsckStartTrap,
       "panRAIDFsckEndTrap": panRAIDFsckEndTrap,
       "panRAIDFsckFailedTrap": panRAIDFsckFailedTrap,
       "panRAIDMountFailedTrap": panRAIDMountFailedTrap,
       "panRAIDRebuildFailedTrap": panRAIDRebuildFailedTrap,
       "panVMDvfInitSucceedTrap": panVMDvfInitSucceedTrap,
       "panVMDvfInitFailTrap": panVMDvfInitFailTrap,
       "panSSHSshSessionEstablishedTrap": panSSHSshSessionEstablishedTrap,
       "panSSHSshSessionTerminatedTrap": panSSHSshSessionTerminatedTrap,
       "panSSHSshSessionEstablishmentFailedTrap": panSSHSshSessionEstablishmentFailedTrap,
       "panSSHSshSessionDisconnectedTrap": panSSHSshSessionDisconnectedTrap,
       "panSSHSshConnectionTrap": panSSHSshConnectionTrap,
       "panTLSTlsSessionEstablishedTrap": panTLSTlsSessionEstablishedTrap,
       "panTLSTlsSessionTerminatedTrap": panTLSTlsSessionTerminatedTrap,
       "panTLSTlsSessionEstablishmentFailedTrap": panTLSTlsSessionEstablishmentFailedTrap,
       "panTLSTlsSessionDisconnectedTrap": panTLSTlsSessionDisconnectedTrap,
       "panLLDPRxErrorTrap": panLLDPRxErrorTrap,
       "panLLDPMibChangedTrap": panLLDPMibChangedTrap,
       "panLLDPTooManyNeighborsTrap": panLLDPTooManyNeighborsTrap,
       "panLLDPTooManyNeighborsTimerClearedTrap": panLLDPTooManyNeighborsTimerClearedTrap,
       "panLLDPOtherTrap": panLLDPOtherTrap,
       "panLLDPTxErrorTrap": panLLDPTxErrorTrap,
       "panFBWildfireWrongCloudTypeTrap": panFBWildfireWrongCloudTypeTrap,
       "panFBWildfireDisabledByCloudTrap": panFBWildfireDisabledByCloudTrap,
       "panFBWildfireNoPolicyTrap": panFBWildfireNoPolicyTrap,
       "panFBWildfireNoLicenseTrap": panFBWildfireNoLicenseTrap,
       "panFBWildfireInvalidCloudInfoTrap": panFBWildfireInvalidCloudInfoTrap}
)
