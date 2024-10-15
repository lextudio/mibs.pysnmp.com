# SNMP MIB module (TPT-NGFW-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-NGFW-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:02 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(tpt_ngfw_compls,
 tpt_ngfw_eventsV2,
 tpt_ngfw_groups,
 tpt_ngfw_objs,
 tpt_ngfw_params) = mibBuilder.importSymbols(
    "TPT-NGFW-REG-MIB",
    "tpt-ngfw-compls",
    "tpt-ngfw-eventsV2",
    "tpt-ngfw-groups",
    "tpt-ngfw-objs",
    "tpt-ngfw-params")

(tptNgfwSystemSerial,) = mibBuilder.importSymbols(
    "TPT-NGFW-SYSTEM-INFO-MIB",
    "tptNgfwSystemSerial")


# MODULE-IDENTITY

tptNgfwPolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 4)
)
tptNgfwPolicy.setRevisions(
        ("2016-05-25 18:54",
         "2013-03-13 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EventSource(Integer32, TextualConvention):
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
        *(("firewall", 1),
          ("ips", 2),
          ("quarantine", 4),
          ("reputation", 3))
    )



class FirewallEventType(Integer32, TextualConvention):
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
        *(("applicationDetect", 2),
          ("blockedByFirewall", 4),
          ("sessionEnd", 3),
          ("sessionStart", 1))
    )



class EventSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 5),
          ("info", 1),
          ("low", 2),
          ("major", 4),
          ("minor", 3))
    )



class ActionType(Integer32, TextualConvention):
    status = "current"
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
        *(("block", 4),
          ("permit", 1),
          ("quarantine", 5),
          ("rateLimit", 2),
          ("trust", 3))
    )



class PacketTraceVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("packetTraceV1", 1),
          ("packetTraceV2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TptNgfwPolicyNotifyTime_Type = DateAndTime
_TptNgfwPolicyNotifyTime_Object = MibScalar
tptNgfwPolicyNotifyTime = _TptNgfwPolicyNotifyTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 20),
    _TptNgfwPolicyNotifyTime_Type()
)
tptNgfwPolicyNotifyTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyTime.setStatus("current")
_TptNgfwPolicyNotifyEventSource_Type = EventSource
_TptNgfwPolicyNotifyEventSource_Object = MibScalar
tptNgfwPolicyNotifyEventSource = _TptNgfwPolicyNotifyEventSource_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 21),
    _TptNgfwPolicyNotifyEventSource_Type()
)
tptNgfwPolicyNotifyEventSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyEventSource.setStatus("current")
_TptNgfwPolicyNotifyEventType_Type = FirewallEventType
_TptNgfwPolicyNotifyEventType_Object = MibScalar
tptNgfwPolicyNotifyEventType = _TptNgfwPolicyNotifyEventType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 22),
    _TptNgfwPolicyNotifyEventType_Type()
)
tptNgfwPolicyNotifyEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyEventType.setStatus("current")
_TptNgfwPolicyNotifyEventSeverity_Type = EventSeverity
_TptNgfwPolicyNotifyEventSeverity_Object = MibScalar
tptNgfwPolicyNotifyEventSeverity = _TptNgfwPolicyNotifyEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 23),
    _TptNgfwPolicyNotifyEventSeverity_Type()
)
tptNgfwPolicyNotifyEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyEventSeverity.setStatus("current")


class _TptNgfwPolicyNotifyCorrelationId_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyCorrelationId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TptNgfwPolicyNotifyCorrelationId_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyCorrelationId_Object = MibScalar
tptNgfwPolicyNotifyCorrelationId = _TptNgfwPolicyNotifyCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 24),
    _TptNgfwPolicyNotifyCorrelationId_Type()
)
tptNgfwPolicyNotifyCorrelationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyCorrelationId.setStatus("current")
_TptNgfwPolicyNotifyActionType_Type = ActionType
_TptNgfwPolicyNotifyActionType_Object = MibScalar
tptNgfwPolicyNotifyActionType = _TptNgfwPolicyNotifyActionType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 25),
    _TptNgfwPolicyNotifyActionType_Type()
)
tptNgfwPolicyNotifyActionType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyActionType.setStatus("current")


class _TptNgfwPolicyNotifyAction_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyAction based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptNgfwPolicyNotifyAction_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyAction_Object = MibScalar
tptNgfwPolicyNotifyAction = _TptNgfwPolicyNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 26),
    _TptNgfwPolicyNotifyAction_Type()
)
tptNgfwPolicyNotifyAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyAction.setStatus("current")


class _TptNgfwPolicyNotifyActionSetName_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyActionSetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TptNgfwPolicyNotifyActionSetName_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyActionSetName_Object = MibScalar
tptNgfwPolicyNotifyActionSetName = _TptNgfwPolicyNotifyActionSetName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 27),
    _TptNgfwPolicyNotifyActionSetName_Type()
)
tptNgfwPolicyNotifyActionSetName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyActionSetName.setStatus("current")


class _TptNgfwPolicyNotifyRuleName_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TptNgfwPolicyNotifyRuleName_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyRuleName_Object = MibScalar
tptNgfwPolicyNotifyRuleName = _TptNgfwPolicyNotifyRuleName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 28),
    _TptNgfwPolicyNotifyRuleName_Type()
)
tptNgfwPolicyNotifyRuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyRuleName.setStatus("current")


class _TptNgfwPolicyNotifyInInterface_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyInInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptNgfwPolicyNotifyInInterface_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyInInterface_Object = MibScalar
tptNgfwPolicyNotifyInInterface = _TptNgfwPolicyNotifyInInterface_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 29),
    _TptNgfwPolicyNotifyInInterface_Type()
)
tptNgfwPolicyNotifyInInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyInInterface.setStatus("current")


class _TptNgfwPolicyNotifyOutInterface_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyOutInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptNgfwPolicyNotifyOutInterface_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyOutInterface_Object = MibScalar
tptNgfwPolicyNotifyOutInterface = _TptNgfwPolicyNotifyOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 30),
    _TptNgfwPolicyNotifyOutInterface_Type()
)
tptNgfwPolicyNotifyOutInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyOutInterface.setStatus("current")
_TptNgfwPolicyNotifySrcIpAddrType_Type = InetAddressType
_TptNgfwPolicyNotifySrcIpAddrType_Object = MibScalar
tptNgfwPolicyNotifySrcIpAddrType = _TptNgfwPolicyNotifySrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 31),
    _TptNgfwPolicyNotifySrcIpAddrType_Type()
)
tptNgfwPolicyNotifySrcIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifySrcIpAddrType.setStatus("current")
_TptNgfwPolicyNotifySrcIpAddr_Type = InetAddress
_TptNgfwPolicyNotifySrcIpAddr_Object = MibScalar
tptNgfwPolicyNotifySrcIpAddr = _TptNgfwPolicyNotifySrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 32),
    _TptNgfwPolicyNotifySrcIpAddr_Type()
)
tptNgfwPolicyNotifySrcIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifySrcIpAddr.setStatus("current")
_TptNgfwPolicyNotifySrcPort_Type = Unsigned32
_TptNgfwPolicyNotifySrcPort_Object = MibScalar
tptNgfwPolicyNotifySrcPort = _TptNgfwPolicyNotifySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 33),
    _TptNgfwPolicyNotifySrcPort_Type()
)
tptNgfwPolicyNotifySrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifySrcPort.setStatus("current")
_TptNgfwPolicyNotifySrcTransIpAddr_Type = InetAddress
_TptNgfwPolicyNotifySrcTransIpAddr_Object = MibScalar
tptNgfwPolicyNotifySrcTransIpAddr = _TptNgfwPolicyNotifySrcTransIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 34),
    _TptNgfwPolicyNotifySrcTransIpAddr_Type()
)
tptNgfwPolicyNotifySrcTransIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifySrcTransIpAddr.setStatus("current")
_TptNgfwPolicyNotifySrcTransPort_Type = Unsigned32
_TptNgfwPolicyNotifySrcTransPort_Object = MibScalar
tptNgfwPolicyNotifySrcTransPort = _TptNgfwPolicyNotifySrcTransPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 35),
    _TptNgfwPolicyNotifySrcTransPort_Type()
)
tptNgfwPolicyNotifySrcTransPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifySrcTransPort.setStatus("current")
_TptNgfwPolicyNotifyDestIpAddrType_Type = InetAddressType
_TptNgfwPolicyNotifyDestIpAddrType_Object = MibScalar
tptNgfwPolicyNotifyDestIpAddrType = _TptNgfwPolicyNotifyDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 36),
    _TptNgfwPolicyNotifyDestIpAddrType_Type()
)
tptNgfwPolicyNotifyDestIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyDestIpAddrType.setStatus("current")
_TptNgfwPolicyNotifyDestIpAddr_Type = InetAddress
_TptNgfwPolicyNotifyDestIpAddr_Object = MibScalar
tptNgfwPolicyNotifyDestIpAddr = _TptNgfwPolicyNotifyDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 37),
    _TptNgfwPolicyNotifyDestIpAddr_Type()
)
tptNgfwPolicyNotifyDestIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyDestIpAddr.setStatus("current")
_TptNgfwPolicyNotifyDestPort_Type = Unsigned32
_TptNgfwPolicyNotifyDestPort_Object = MibScalar
tptNgfwPolicyNotifyDestPort = _TptNgfwPolicyNotifyDestPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 38),
    _TptNgfwPolicyNotifyDestPort_Type()
)
tptNgfwPolicyNotifyDestPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyDestPort.setStatus("current")
_TptNgfwPolicyNotifyDestTransIpAddr_Type = InetAddress
_TptNgfwPolicyNotifyDestTransIpAddr_Object = MibScalar
tptNgfwPolicyNotifyDestTransIpAddr = _TptNgfwPolicyNotifyDestTransIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 39),
    _TptNgfwPolicyNotifyDestTransIpAddr_Type()
)
tptNgfwPolicyNotifyDestTransIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyDestTransIpAddr.setStatus("current")
_TptNgfwPolicyNotifyDestTransPort_Type = Unsigned32
_TptNgfwPolicyNotifyDestTransPort_Object = MibScalar
tptNgfwPolicyNotifyDestTransPort = _TptNgfwPolicyNotifyDestTransPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 40),
    _TptNgfwPolicyNotifyDestTransPort_Type()
)
tptNgfwPolicyNotifyDestTransPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyDestTransPort.setStatus("current")


class _TptNgfwPolicyNotifyProtocol_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyProtocol based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptNgfwPolicyNotifyProtocol_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyProtocol_Object = MibScalar
tptNgfwPolicyNotifyProtocol = _TptNgfwPolicyNotifyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 41),
    _TptNgfwPolicyNotifyProtocol_Type()
)
tptNgfwPolicyNotifyProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyProtocol.setStatus("current")


class _TptNgfwPolicyNotifyApplicationName_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyApplicationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptNgfwPolicyNotifyApplicationName_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyApplicationName_Object = MibScalar
tptNgfwPolicyNotifyApplicationName = _TptNgfwPolicyNotifyApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 42),
    _TptNgfwPolicyNotifyApplicationName_Type()
)
tptNgfwPolicyNotifyApplicationName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyApplicationName.setStatus("current")


class _TptNgfwPolicyNotifyUserName_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptNgfwPolicyNotifyUserName_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyUserName_Object = MibScalar
tptNgfwPolicyNotifyUserName = _TptNgfwPolicyNotifyUserName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 43),
    _TptNgfwPolicyNotifyUserName_Type()
)
tptNgfwPolicyNotifyUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyUserName.setStatus("current")
_TptNgfwPolicyNotifyBytesIn_Type = Counter64
_TptNgfwPolicyNotifyBytesIn_Object = MibScalar
tptNgfwPolicyNotifyBytesIn = _TptNgfwPolicyNotifyBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 44),
    _TptNgfwPolicyNotifyBytesIn_Type()
)
tptNgfwPolicyNotifyBytesIn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyBytesIn.setStatus("current")
_TptNgfwPolicyNotifyBytesOut_Type = Counter64
_TptNgfwPolicyNotifyBytesOut_Object = MibScalar
tptNgfwPolicyNotifyBytesOut = _TptNgfwPolicyNotifyBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 45),
    _TptNgfwPolicyNotifyBytesOut_Type()
)
tptNgfwPolicyNotifyBytesOut.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyBytesOut.setStatus("current")
_TptNgfwPolicyNotifyStartTimeSec_Type = Counter64
_TptNgfwPolicyNotifyStartTimeSec_Object = MibScalar
tptNgfwPolicyNotifyStartTimeSec = _TptNgfwPolicyNotifyStartTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 46),
    _TptNgfwPolicyNotifyStartTimeSec_Type()
)
tptNgfwPolicyNotifyStartTimeSec.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyStartTimeSec.setStatus("current")
_TptNgfwPolicyNotifyStartTimeNano_Type = Counter64
_TptNgfwPolicyNotifyStartTimeNano_Object = MibScalar
tptNgfwPolicyNotifyStartTimeNano = _TptNgfwPolicyNotifyStartTimeNano_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 47),
    _TptNgfwPolicyNotifyStartTimeNano_Type()
)
tptNgfwPolicyNotifyStartTimeNano.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyStartTimeNano.setStatus("current")
_TptNgfwPolicyNotifyRateLimit_Type = Counter64
_TptNgfwPolicyNotifyRateLimit_Object = MibScalar
tptNgfwPolicyNotifyRateLimit = _TptNgfwPolicyNotifyRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 48),
    _TptNgfwPolicyNotifyRateLimit_Type()
)
tptNgfwPolicyNotifyRateLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyRateLimit.setStatus("current")
_TptNgfwPolicyNotifyPktTraceVer_Type = PacketTraceVersion
_TptNgfwPolicyNotifyPktTraceVer_Object = MibScalar
tptNgfwPolicyNotifyPktTraceVer = _TptNgfwPolicyNotifyPktTraceVer_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 49),
    _TptNgfwPolicyNotifyPktTraceVer_Type()
)
tptNgfwPolicyNotifyPktTraceVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyPktTraceVer.setStatus("current")
_TptNgfwPolicyNotifyPktTraceId_Type = Unsigned32
_TptNgfwPolicyNotifyPktTraceId_Object = MibScalar
tptNgfwPolicyNotifyPktTraceId = _TptNgfwPolicyNotifyPktTraceId_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 50),
    _TptNgfwPolicyNotifyPktTraceId_Type()
)
tptNgfwPolicyNotifyPktTraceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyPktTraceId.setStatus("current")
_TptNgfwPolicyNotifyPktTraceBegin_Type = Unsigned32
_TptNgfwPolicyNotifyPktTraceBegin_Object = MibScalar
tptNgfwPolicyNotifyPktTraceBegin = _TptNgfwPolicyNotifyPktTraceBegin_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 51),
    _TptNgfwPolicyNotifyPktTraceBegin_Type()
)
tptNgfwPolicyNotifyPktTraceBegin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyPktTraceBegin.setStatus("current")
_TptNgfwPolicyNotifyPktTraceEnd_Type = Unsigned32
_TptNgfwPolicyNotifyPktTraceEnd_Object = MibScalar
tptNgfwPolicyNotifyPktTraceEnd = _TptNgfwPolicyNotifyPktTraceEnd_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 52),
    _TptNgfwPolicyNotifyPktTraceEnd_Type()
)
tptNgfwPolicyNotifyPktTraceEnd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyPktTraceEnd.setStatus("current")


class _TptNgfwPolicyNotifyFilterName_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyFilterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptNgfwPolicyNotifyFilterName_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyFilterName_Object = MibScalar
tptNgfwPolicyNotifyFilterName = _TptNgfwPolicyNotifyFilterName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 53),
    _TptNgfwPolicyNotifyFilterName_Type()
)
tptNgfwPolicyNotifyFilterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyFilterName.setStatus("current")


class _TptNgfwPolicyNotifyProfileName_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptNgfwPolicyNotifyProfileName_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyProfileName_Object = MibScalar
tptNgfwPolicyNotifyProfileName = _TptNgfwPolicyNotifyProfileName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 54),
    _TptNgfwPolicyNotifyProfileName_Type()
)
tptNgfwPolicyNotifyProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyProfileName.setStatus("current")


class _TptNgfwPolicyNotifyPolicyName_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptNgfwPolicyNotifyPolicyName_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyPolicyName_Object = MibScalar
tptNgfwPolicyNotifyPolicyName = _TptNgfwPolicyNotifyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 55),
    _TptNgfwPolicyNotifyPolicyName_Type()
)
tptNgfwPolicyNotifyPolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyPolicyName.setStatus("current")


class _TptNgfwPolicyNotifyVlanId_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyVlanId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptNgfwPolicyNotifyVlanId_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyVlanId_Object = MibScalar
tptNgfwPolicyNotifyVlanId = _TptNgfwPolicyNotifyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 56),
    _TptNgfwPolicyNotifyVlanId_Type()
)
tptNgfwPolicyNotifyVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyVlanId.setStatus("current")
_TptNgfwPolicyNotifyHitCount_Type = Counter64
_TptNgfwPolicyNotifyHitCount_Object = MibScalar
tptNgfwPolicyNotifyHitCount = _TptNgfwPolicyNotifyHitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 57),
    _TptNgfwPolicyNotifyHitCount_Type()
)
tptNgfwPolicyNotifyHitCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyHitCount.setStatus("current")


class _TptNgfwPolicyNotifyMsgParams_Type(SnmpAdminString):
    """Custom type tptNgfwPolicyNotifyMsgParams based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TptNgfwPolicyNotifyMsgParams_Type.__name__ = "SnmpAdminString"
_TptNgfwPolicyNotifyMsgParams_Object = MibScalar
tptNgfwPolicyNotifyMsgParams = _TptNgfwPolicyNotifyMsgParams_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 58),
    _TptNgfwPolicyNotifyMsgParams_Type()
)
tptNgfwPolicyNotifyMsgParams.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyMsgParams.setStatus("current")
_TptNgfwPolicyNotifyPeriod_Type = Unsigned32
_TptNgfwPolicyNotifyPeriod_Object = MibScalar
tptNgfwPolicyNotifyPeriod = _TptNgfwPolicyNotifyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 59),
    _TptNgfwPolicyNotifyPeriod_Type()
)
tptNgfwPolicyNotifyPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwPolicyNotifyPeriod.setStatus("current")

# Managed Objects groups

tptNgfwPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 7)
)
tptNgfwPolicyGroup.setObjects(
      *(("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyTime"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyEventSource"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyEventType"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyEventSeverity"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyCorrelationId"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyActionType"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyActionSetName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyAction"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyRuleName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyInInterface"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyOutInterface"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifySrcIpAddrType"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifySrcIpAddr"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifySrcPort"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifySrcTransIpAddr"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifySrcTransPort"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyDestIpAddrType"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyDestIpAddr"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyDestPort"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyDestTransIpAddr"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyDestTransPort"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyProtocol"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyApplicationName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyUserName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyBytesIn"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyBytesOut"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyStartTimeSec"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyStartTimeNano"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyRateLimit"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPktTraceVer"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPktTraceId"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPktTraceBegin"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPktTraceEnd"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyFilterName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyProfileName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPolicyName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyVlanId"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyHitCount"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyMsgParams"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPeriod"))
)
if mibBuilder.loadTexts:
    tptNgfwPolicyGroup.setStatus("current")


# Notification objects

tptNgfwPolicyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 10)
)
tptNgfwPolicyNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyTime"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyEventSource"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyEventType"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyEventSeverity"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyCorrelationId"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyActionType"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyAction"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyRuleName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyInInterface"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyOutInterface"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifySrcIpAddrType"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifySrcIpAddr"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifySrcPort"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifySrcTransIpAddr"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifySrcTransPort"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyDestIpAddrType"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyDestIpAddr"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyDestPort"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyDestTransIpAddr"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyDestTransPort"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyProtocol"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyApplicationName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyUserName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyBytesIn"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyBytesOut"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyStartTimeSec"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyStartTimeNano"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyRateLimit"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPktTraceVer"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPktTraceId"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPktTraceBegin"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPktTraceEnd"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyFilterName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyProfileName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPolicyName"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyVlanId"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyHitCount"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyMsgParams"),
        ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotifyPeriod"))
)
if mibBuilder.loadTexts:
    tptNgfwPolicyNotify.setStatus(
        "current"
    )


# Notifications groups

tptNgfwPolicyNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 8)
)
tptNgfwPolicyNotificationGroup.setObjects(
    ("TPT-NGFW-POLICY-MIB", "tptNgfwPolicyNotify")
)
if mibBuilder.loadTexts:
    tptNgfwPolicyNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tptNgfwPolicyCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tptNgfwPolicyCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-NGFW-POLICY-MIB",
    **{"EventSource": EventSource,
       "FirewallEventType": FirewallEventType,
       "EventSeverity": EventSeverity,
       "ActionType": ActionType,
       "PacketTraceVersion": PacketTraceVersion,
       "tptNgfwPolicyGroup": tptNgfwPolicyGroup,
       "tptNgfwPolicyNotificationGroup": tptNgfwPolicyNotificationGroup,
       "tptNgfwPolicyCompl": tptNgfwPolicyCompl,
       "tptNgfwPolicy": tptNgfwPolicy,
       "tptNgfwPolicyNotify": tptNgfwPolicyNotify,
       "tptNgfwPolicyNotifyTime": tptNgfwPolicyNotifyTime,
       "tptNgfwPolicyNotifyEventSource": tptNgfwPolicyNotifyEventSource,
       "tptNgfwPolicyNotifyEventType": tptNgfwPolicyNotifyEventType,
       "tptNgfwPolicyNotifyEventSeverity": tptNgfwPolicyNotifyEventSeverity,
       "tptNgfwPolicyNotifyCorrelationId": tptNgfwPolicyNotifyCorrelationId,
       "tptNgfwPolicyNotifyActionType": tptNgfwPolicyNotifyActionType,
       "tptNgfwPolicyNotifyAction": tptNgfwPolicyNotifyAction,
       "tptNgfwPolicyNotifyActionSetName": tptNgfwPolicyNotifyActionSetName,
       "tptNgfwPolicyNotifyRuleName": tptNgfwPolicyNotifyRuleName,
       "tptNgfwPolicyNotifyInInterface": tptNgfwPolicyNotifyInInterface,
       "tptNgfwPolicyNotifyOutInterface": tptNgfwPolicyNotifyOutInterface,
       "tptNgfwPolicyNotifySrcIpAddrType": tptNgfwPolicyNotifySrcIpAddrType,
       "tptNgfwPolicyNotifySrcIpAddr": tptNgfwPolicyNotifySrcIpAddr,
       "tptNgfwPolicyNotifySrcPort": tptNgfwPolicyNotifySrcPort,
       "tptNgfwPolicyNotifySrcTransIpAddr": tptNgfwPolicyNotifySrcTransIpAddr,
       "tptNgfwPolicyNotifySrcTransPort": tptNgfwPolicyNotifySrcTransPort,
       "tptNgfwPolicyNotifyDestIpAddrType": tptNgfwPolicyNotifyDestIpAddrType,
       "tptNgfwPolicyNotifyDestIpAddr": tptNgfwPolicyNotifyDestIpAddr,
       "tptNgfwPolicyNotifyDestPort": tptNgfwPolicyNotifyDestPort,
       "tptNgfwPolicyNotifyDestTransIpAddr": tptNgfwPolicyNotifyDestTransIpAddr,
       "tptNgfwPolicyNotifyDestTransPort": tptNgfwPolicyNotifyDestTransPort,
       "tptNgfwPolicyNotifyProtocol": tptNgfwPolicyNotifyProtocol,
       "tptNgfwPolicyNotifyApplicationName": tptNgfwPolicyNotifyApplicationName,
       "tptNgfwPolicyNotifyUserName": tptNgfwPolicyNotifyUserName,
       "tptNgfwPolicyNotifyBytesIn": tptNgfwPolicyNotifyBytesIn,
       "tptNgfwPolicyNotifyBytesOut": tptNgfwPolicyNotifyBytesOut,
       "tptNgfwPolicyNotifyStartTimeSec": tptNgfwPolicyNotifyStartTimeSec,
       "tptNgfwPolicyNotifyStartTimeNano": tptNgfwPolicyNotifyStartTimeNano,
       "tptNgfwPolicyNotifyRateLimit": tptNgfwPolicyNotifyRateLimit,
       "tptNgfwPolicyNotifyPktTraceVer": tptNgfwPolicyNotifyPktTraceVer,
       "tptNgfwPolicyNotifyPktTraceId": tptNgfwPolicyNotifyPktTraceId,
       "tptNgfwPolicyNotifyPktTraceBegin": tptNgfwPolicyNotifyPktTraceBegin,
       "tptNgfwPolicyNotifyPktTraceEnd": tptNgfwPolicyNotifyPktTraceEnd,
       "tptNgfwPolicyNotifyFilterName": tptNgfwPolicyNotifyFilterName,
       "tptNgfwPolicyNotifyProfileName": tptNgfwPolicyNotifyProfileName,
       "tptNgfwPolicyNotifyPolicyName": tptNgfwPolicyNotifyPolicyName,
       "tptNgfwPolicyNotifyVlanId": tptNgfwPolicyNotifyVlanId,
       "tptNgfwPolicyNotifyHitCount": tptNgfwPolicyNotifyHitCount,
       "tptNgfwPolicyNotifyMsgParams": tptNgfwPolicyNotifyMsgParams,
       "tptNgfwPolicyNotifyPeriod": tptNgfwPolicyNotifyPeriod}
)
