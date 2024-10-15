# SNMP MIB module (PKTC-IETF-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PKTC-IETF-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:54 2024
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

(ifPhysAddress,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifPhysAddress")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(snmpNotifyFilterGroup,
 snmpNotifyGroup) = mibBuilder.importSymbols(
    "SNMP-NOTIFICATION-MIB",
    "snmpNotifyFilterGroup",
    "snmpNotifyGroup")

(snmpTargetBasicGroup,
 snmpTargetResponseGroup) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetBasicGroup",
    "snmpTargetResponseGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(SyslogFacility,
 SyslogSeverity) = mibBuilder.importSymbols(
    "SYSLOG-TC-MIB",
    "SyslogFacility",
    "SyslogSeverity")


# MODULE-IDENTITY

pktcIetfEventMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 182)
)
pktcIetfEventMib.setRevisions(
        ("2009-03-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogSeverityMask(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_PktcEventNotifications_ObjectIdentity = ObjectIdentity
pktcEventNotifications = _PktcEventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 182, 0)
)
_PktcEventMibObjects_ObjectIdentity = ObjectIdentity
pktcEventMibObjects = _PktcEventMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 182, 1)
)
_PktcEventControl_ObjectIdentity = ObjectIdentity
pktcEventControl = _PktcEventControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 182, 1, 1)
)


class _PktcEventReset_Type(Bits):
    """Custom type pktcEventReset based on Bits"""
    namedValues = NamedValues(
        *(("resetEventLogTable", 0),
          ("resetEventTable", 1))
    )

_PktcEventReset_Type.__name__ = "Bits"
_PktcEventReset_Object = MibScalar
pktcEventReset = _PktcEventReset_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 1),
    _PktcEventReset_Type()
)
pktcEventReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventReset.setStatus("current")
_PktcEventSyslog_ObjectIdentity = ObjectIdentity
pktcEventSyslog = _PktcEventSyslog_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 2)
)


class _PktcEventSyslogCapabilities_Type(Bits):
    """Custom type pktcEventSyslogCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("formatBSDSyslog", 0),
          ("formatSyslogProtocol", 1),
          ("transportBEEP", 4),
          ("transportTLS", 3),
          ("transportUDP", 2))
    )

_PktcEventSyslogCapabilities_Type.__name__ = "Bits"
_PktcEventSyslogCapabilities_Object = MibScalar
pktcEventSyslogCapabilities = _PktcEventSyslogCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 1),
    _PktcEventSyslogCapabilities_Type()
)
pktcEventSyslogCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventSyslogCapabilities.setStatus("current")


class _PktcEventSyslogAddressType_Type(InetAddressType):
    """Custom type pktcEventSyslogAddressType based on InetAddressType"""


_PktcEventSyslogAddressType_Object = MibScalar
pktcEventSyslogAddressType = _PktcEventSyslogAddressType_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 2),
    _PktcEventSyslogAddressType_Type()
)
pktcEventSyslogAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventSyslogAddressType.setStatus("current")


class _PktcEventSyslogAddress_Type(InetAddress):
    """Custom type pktcEventSyslogAddress based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")


_PktcEventSyslogAddress_Object = MibScalar
pktcEventSyslogAddress = _PktcEventSyslogAddress_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 3),
    _PktcEventSyslogAddress_Type()
)
pktcEventSyslogAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventSyslogAddress.setStatus("current")


class _PktcEventSyslogMessageFormat_Type(Integer32):
    """Custom type pktcEventSyslogMessageFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("formatBSDSyslog", 1),
          ("formatSyslogProtocol", 2))
    )


_PktcEventSyslogMessageFormat_Type.__name__ = "Integer32"
_PktcEventSyslogMessageFormat_Object = MibScalar
pktcEventSyslogMessageFormat = _PktcEventSyslogMessageFormat_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 4),
    _PktcEventSyslogMessageFormat_Type()
)
pktcEventSyslogMessageFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventSyslogMessageFormat.setStatus("current")


class _PktcEventSyslogTransport_Type(Integer32):
    """Custom type pktcEventSyslogTransport based on Integer32"""
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
        *(("beep", 3),
          ("tls", 2),
          ("udp", 1))
    )


_PktcEventSyslogTransport_Type.__name__ = "Integer32"
_PktcEventSyslogTransport_Object = MibScalar
pktcEventSyslogTransport = _PktcEventSyslogTransport_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 5),
    _PktcEventSyslogTransport_Type()
)
pktcEventSyslogTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventSyslogTransport.setStatus("current")


class _PktcEventSyslogPort_Type(InetPortNumber):
    """Custom type pktcEventSyslogPort based on InetPortNumber"""
    defaultValue = 6514


_PktcEventSyslogPort_Object = MibScalar
pktcEventSyslogPort = _PktcEventSyslogPort_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 6),
    _PktcEventSyslogPort_Type()
)
pktcEventSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventSyslogPort.setStatus("current")
_PktcEventClassTable_Object = MibTable
pktcEventClassTable = _PktcEventClassTable_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pktcEventClassTable.setStatus("current")
_PktcEventClassEntry_Object = MibTableRow
pktcEventClassEntry = _PktcEventClassEntry_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 3, 1)
)
pktcEventClassEntry.setIndexNames(
    (0, "PKTC-IETF-EVENT-MIB", "pktcEventClassIndex"),
)
if mibBuilder.loadTexts:
    pktcEventClassEntry.setStatus("current")


class _PktcEventClassIndex_Type(Unsigned32):
    """Custom type pktcEventClassIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PktcEventClassIndex_Type.__name__ = "Unsigned32"
_PktcEventClassIndex_Object = MibTableColumn
pktcEventClassIndex = _PktcEventClassIndex_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 3, 1, 1),
    _PktcEventClassIndex_Type()
)
pktcEventClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEventClassIndex.setStatus("current")


class _PktcEventClassName_Type(SnmpAdminString):
    """Custom type pktcEventClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_PktcEventClassName_Type.__name__ = "SnmpAdminString"
_PktcEventClassName_Object = MibTableColumn
pktcEventClassName = _PktcEventClassName_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 3, 1, 2),
    _PktcEventClassName_Type()
)
pktcEventClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventClassName.setStatus("current")
_PktcEventClassStatus_Type = TruthValue
_PktcEventClassStatus_Object = MibTableColumn
pktcEventClassStatus = _PktcEventClassStatus_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 3, 1, 3),
    _PktcEventClassStatus_Type()
)
pktcEventClassStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventClassStatus.setStatus("current")
_PktcEventClassSeverity_Type = SyslogSeverityMask
_PktcEventClassSeverity_Object = MibTableColumn
pktcEventClassSeverity = _PktcEventClassSeverity_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 1, 3, 1, 4),
    _PktcEventClassSeverity_Type()
)
pktcEventClassSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventClassSeverity.setStatus("current")
_PktcEventThrottle_ObjectIdentity = ObjectIdentity
pktcEventThrottle = _PktcEventThrottle_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 182, 1, 2)
)


class _PktcEventThrottleAdminStatus_Type(Integer32):
    """Custom type pktcEventThrottleAdminStatus based on Integer32"""
    defaultValue = 1

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
        *(("inhibited", 4),
          ("maintainBelowThreshold", 2),
          ("stopAtThreshold", 3),
          ("unconstrained", 1))
    )


_PktcEventThrottleAdminStatus_Type.__name__ = "Integer32"
_PktcEventThrottleAdminStatus_Object = MibScalar
pktcEventThrottleAdminStatus = _PktcEventThrottleAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 2, 1),
    _PktcEventThrottleAdminStatus_Type()
)
pktcEventThrottleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventThrottleAdminStatus.setStatus("current")


class _PktcEventThrottleThreshold_Type(Unsigned32):
    """Custom type pktcEventThrottleThreshold based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_PktcEventThrottleThreshold_Type.__name__ = "Unsigned32"
_PktcEventThrottleThreshold_Object = MibScalar
pktcEventThrottleThreshold = _PktcEventThrottleThreshold_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 2, 2),
    _PktcEventThrottleThreshold_Type()
)
pktcEventThrottleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventThrottleThreshold.setStatus("current")


class _PktcEventThrottleInterval_Type(Unsigned32):
    """Custom type pktcEventThrottleInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_PktcEventThrottleInterval_Type.__name__ = "Unsigned32"
_PktcEventThrottleInterval_Object = MibScalar
pktcEventThrottleInterval = _PktcEventThrottleInterval_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 2, 3),
    _PktcEventThrottleInterval_Type()
)
pktcEventThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventThrottleInterval.setStatus("current")
if mibBuilder.loadTexts:
    pktcEventThrottleInterval.setUnits("seconds")
_PktcEventStatus_ObjectIdentity = ObjectIdentity
pktcEventStatus = _PktcEventStatus_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 182, 1, 3)
)


class _PktcEventTransmissionStatus_Type(Bits):
    """Custom type pktcEventTransmissionStatus based on Bits"""
    namedValues = NamedValues(
        *(("snmpThrottled", 1),
          ("snmpTransmitError", 5),
          ("syslogThrottled", 0),
          ("syslogTransmitError", 4),
          ("validSnmpManagerAbsent", 3),
          ("validsyslogServerAbsent", 2))
    )

_PktcEventTransmissionStatus_Type.__name__ = "Bits"
_PktcEventTransmissionStatus_Object = MibScalar
pktcEventTransmissionStatus = _PktcEventTransmissionStatus_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 3, 1),
    _PktcEventTransmissionStatus_Type()
)
pktcEventTransmissionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventTransmissionStatus.setStatus("current")
_PktcEvents_ObjectIdentity = ObjectIdentity
pktcEvents = _PktcEvents_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 182, 1, 4)
)
_PktcEventTable_Object = MibTable
pktcEventTable = _PktcEventTable_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pktcEventTable.setStatus("current")
_PktcEventEntry_Object = MibTableRow
pktcEventEntry = _PktcEventEntry_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1)
)
pktcEventEntry.setIndexNames(
    (0, "PKTC-IETF-EVENT-MIB", "pktcEventOrganization"),
    (0, "PKTC-IETF-EVENT-MIB", "pktcEventIdentifier"),
)
if mibBuilder.loadTexts:
    pktcEventEntry.setStatus("current")


class _PktcEventOrganization_Type(Unsigned32):
    """Custom type pktcEventOrganization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PktcEventOrganization_Type.__name__ = "Unsigned32"
_PktcEventOrganization_Object = MibTableColumn
pktcEventOrganization = _PktcEventOrganization_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 1),
    _PktcEventOrganization_Type()
)
pktcEventOrganization.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEventOrganization.setStatus("current")


class _PktcEventIdentifier_Type(Unsigned32):
    """Custom type pktcEventIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PktcEventIdentifier_Type.__name__ = "Unsigned32"
_PktcEventIdentifier_Object = MibTableColumn
pktcEventIdentifier = _PktcEventIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 2),
    _PktcEventIdentifier_Type()
)
pktcEventIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEventIdentifier.setStatus("current")
_PktcEventFacility_Type = SyslogFacility
_PktcEventFacility_Object = MibTableColumn
pktcEventFacility = _PktcEventFacility_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 3),
    _PktcEventFacility_Type()
)
pktcEventFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventFacility.setStatus("current")
_PktcEventSeverityLevel_Type = SyslogSeverity
_PktcEventSeverityLevel_Object = MibTableColumn
pktcEventSeverityLevel = _PktcEventSeverityLevel_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 4),
    _PktcEventSeverityLevel_Type()
)
pktcEventSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventSeverityLevel.setStatus("current")


class _PktcEventReporting_Type(Bits):
    """Custom type pktcEventReporting based on Bits"""
    namedValues = NamedValues(
        *(("local", 0),
          ("snmpInform", 3),
          ("snmpTrap", 2),
          ("syslog", 1))
    )

_PktcEventReporting_Type.__name__ = "Bits"
_PktcEventReporting_Object = MibTableColumn
pktcEventReporting = _PktcEventReporting_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 5),
    _PktcEventReporting_Type()
)
pktcEventReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventReporting.setStatus("current")


class _PktcEventText_Type(SnmpAdminString):
    """Custom type pktcEventText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PktcEventText_Type.__name__ = "SnmpAdminString"
_PktcEventText_Object = MibTableColumn
pktcEventText = _PktcEventText_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 6),
    _PktcEventText_Type()
)
pktcEventText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEventText.setStatus("current")


class _PktcEventClass_Type(SnmpAdminString):
    """Custom type pktcEventClass based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_PktcEventClass_Type.__name__ = "SnmpAdminString"
_PktcEventClass_Object = MibTableColumn
pktcEventClass = _PktcEventClass_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 7),
    _PktcEventClass_Type()
)
pktcEventClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventClass.setStatus("current")
_PktcEventLog_ObjectIdentity = ObjectIdentity
pktcEventLog = _PktcEventLog_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 182, 1, 5)
)
_PktcEventLogTable_Object = MibTable
pktcEventLogTable = _PktcEventLogTable_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1)
)
if mibBuilder.loadTexts:
    pktcEventLogTable.setStatus("current")
_PktcEventLogEntry_Object = MibTableRow
pktcEventLogEntry = _PktcEventLogEntry_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1)
)
pktcEventLogEntry.setIndexNames(
    (0, "PKTC-IETF-EVENT-MIB", "pktcEventLogIndex"),
)
if mibBuilder.loadTexts:
    pktcEventLogEntry.setStatus("current")


class _PktcEventLogIndex_Type(Unsigned32):
    """Custom type pktcEventLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PktcEventLogIndex_Type.__name__ = "Unsigned32"
_PktcEventLogIndex_Object = MibTableColumn
pktcEventLogIndex = _PktcEventLogIndex_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 1),
    _PktcEventLogIndex_Type()
)
pktcEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEventLogIndex.setStatus("current")
_PktcEventLogTime_Type = DateAndTime
_PktcEventLogTime_Object = MibTableColumn
pktcEventLogTime = _PktcEventLogTime_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 2),
    _PktcEventLogTime_Type()
)
pktcEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventLogTime.setStatus("current")


class _PktcEventLogOrganization_Type(Unsigned32):
    """Custom type pktcEventLogOrganization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PktcEventLogOrganization_Type.__name__ = "Unsigned32"
_PktcEventLogOrganization_Object = MibTableColumn
pktcEventLogOrganization = _PktcEventLogOrganization_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 3),
    _PktcEventLogOrganization_Type()
)
pktcEventLogOrganization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventLogOrganization.setStatus("current")
_PktcEventLogIdentifier_Type = Unsigned32
_PktcEventLogIdentifier_Object = MibTableColumn
pktcEventLogIdentifier = _PktcEventLogIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 4),
    _PktcEventLogIdentifier_Type()
)
pktcEventLogIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventLogIdentifier.setStatus("current")


class _PktcEventLogText_Type(SnmpAdminString):
    """Custom type pktcEventLogText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PktcEventLogText_Type.__name__ = "SnmpAdminString"
_PktcEventLogText_Object = MibTableColumn
pktcEventLogText = _PktcEventLogText_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 5),
    _PktcEventLogText_Type()
)
pktcEventLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventLogText.setStatus("current")


class _PktcEventLogEndpointName_Type(SnmpAdminString):
    """Custom type pktcEventLogEndpointName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PktcEventLogEndpointName_Type.__name__ = "SnmpAdminString"
_PktcEventLogEndpointName_Object = MibTableColumn
pktcEventLogEndpointName = _PktcEventLogEndpointName_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 6),
    _PktcEventLogEndpointName_Type()
)
pktcEventLogEndpointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventLogEndpointName.setStatus("current")


class _PktcEventLogType_Type(Bits):
    """Custom type pktcEventLogType based on Bits"""
    namedValues = NamedValues(
        *(("local", 0),
          ("snmpInform", 3),
          ("snmpTrap", 2),
          ("syslog", 1))
    )

_PktcEventLogType_Type.__name__ = "Bits"
_PktcEventLogType_Object = MibTableColumn
pktcEventLogType = _PktcEventLogType_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 7),
    _PktcEventLogType_Type()
)
pktcEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventLogType.setStatus("current")


class _PktcEventLogTargetInfo_Type(SnmpAdminString):
    """Custom type pktcEventLogTargetInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PktcEventLogTargetInfo_Type.__name__ = "SnmpAdminString"
_PktcEventLogTargetInfo_Object = MibTableColumn
pktcEventLogTargetInfo = _PktcEventLogTargetInfo_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 8),
    _PktcEventLogTargetInfo_Type()
)
pktcEventLogTargetInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventLogTargetInfo.setStatus("current")
_PktcEventLogCorrelationId_Type = Unsigned32
_PktcEventLogCorrelationId_Object = MibTableColumn
pktcEventLogCorrelationId = _PktcEventLogCorrelationId_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 9),
    _PktcEventLogCorrelationId_Type()
)
pktcEventLogCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventLogCorrelationId.setStatus("current")


class _PktcEventLogAdditionalInfo_Type(SnmpAdminString):
    """Custom type pktcEventLogAdditionalInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PktcEventLogAdditionalInfo_Type.__name__ = "SnmpAdminString"
_PktcEventLogAdditionalInfo_Object = MibTableColumn
pktcEventLogAdditionalInfo = _PktcEventLogAdditionalInfo_Object(
    (1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 10),
    _PktcEventLogAdditionalInfo_Type()
)
pktcEventLogAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEventLogAdditionalInfo.setStatus("current")
_PktcEventConformance_ObjectIdentity = ObjectIdentity
pktcEventConformance = _PktcEventConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 182, 2)
)
_PktcEventCompliances_ObjectIdentity = ObjectIdentity
pktcEventCompliances = _PktcEventCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 182, 2, 1)
)
_PktcEventGroups_ObjectIdentity = ObjectIdentity
pktcEventGroups = _PktcEventGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 182, 2, 2)
)

# Managed Objects groups

pktcEventGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 182, 2, 2, 1)
)
pktcEventGroup.setObjects(
      *(("PKTC-IETF-EVENT-MIB", "pktcEventReset"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogCapabilities"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogAddressType"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogAddress"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogTransport"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogPort"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogMessageFormat"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventThrottleAdminStatus"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventThrottleThreshold"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventThrottleInterval"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventTransmissionStatus"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventFacility"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventSeverityLevel"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventReporting"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventText"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogTime"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogOrganization"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogIdentifier"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogText"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogEndpointName"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogType"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogTargetInfo"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogCorrelationId"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogAdditionalInfo"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventClass"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventClassName"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventClassStatus"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventClassSeverity"))
)
if mibBuilder.loadTexts:
    pktcEventGroup.setStatus("current")


# Notification objects

pktcEventNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 182, 0, 1)
)
pktcEventNotification.setObjects(
      *(("PKTC-IETF-EVENT-MIB", "pktcEventLogTime"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogOrganization"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogIdentifier"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogEndpointName"),
        ("PKTC-IETF-EVENT-MIB", "pktcEventLogCorrelationId"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    pktcEventNotification.setStatus(
        "current"
    )


# Notifications groups

pktcEventNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 182, 2, 2, 2)
)
pktcEventNotificationGroup.setObjects(
    ("PKTC-IETF-EVENT-MIB", "pktcEventNotification")
)
if mibBuilder.loadTexts:
    pktcEventNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pktcEventBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 182, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pktcEventBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-IETF-EVENT-MIB",
    **{"SyslogSeverityMask": SyslogSeverityMask,
       "pktcIetfEventMib": pktcIetfEventMib,
       "pktcEventNotifications": pktcEventNotifications,
       "pktcEventNotification": pktcEventNotification,
       "pktcEventMibObjects": pktcEventMibObjects,
       "pktcEventControl": pktcEventControl,
       "pktcEventReset": pktcEventReset,
       "pktcEventSyslog": pktcEventSyslog,
       "pktcEventSyslogCapabilities": pktcEventSyslogCapabilities,
       "pktcEventSyslogAddressType": pktcEventSyslogAddressType,
       "pktcEventSyslogAddress": pktcEventSyslogAddress,
       "pktcEventSyslogMessageFormat": pktcEventSyslogMessageFormat,
       "pktcEventSyslogTransport": pktcEventSyslogTransport,
       "pktcEventSyslogPort": pktcEventSyslogPort,
       "pktcEventClassTable": pktcEventClassTable,
       "pktcEventClassEntry": pktcEventClassEntry,
       "pktcEventClassIndex": pktcEventClassIndex,
       "pktcEventClassName": pktcEventClassName,
       "pktcEventClassStatus": pktcEventClassStatus,
       "pktcEventClassSeverity": pktcEventClassSeverity,
       "pktcEventThrottle": pktcEventThrottle,
       "pktcEventThrottleAdminStatus": pktcEventThrottleAdminStatus,
       "pktcEventThrottleThreshold": pktcEventThrottleThreshold,
       "pktcEventThrottleInterval": pktcEventThrottleInterval,
       "pktcEventStatus": pktcEventStatus,
       "pktcEventTransmissionStatus": pktcEventTransmissionStatus,
       "pktcEvents": pktcEvents,
       "pktcEventTable": pktcEventTable,
       "pktcEventEntry": pktcEventEntry,
       "pktcEventOrganization": pktcEventOrganization,
       "pktcEventIdentifier": pktcEventIdentifier,
       "pktcEventFacility": pktcEventFacility,
       "pktcEventSeverityLevel": pktcEventSeverityLevel,
       "pktcEventReporting": pktcEventReporting,
       "pktcEventText": pktcEventText,
       "pktcEventClass": pktcEventClass,
       "pktcEventLog": pktcEventLog,
       "pktcEventLogTable": pktcEventLogTable,
       "pktcEventLogEntry": pktcEventLogEntry,
       "pktcEventLogIndex": pktcEventLogIndex,
       "pktcEventLogTime": pktcEventLogTime,
       "pktcEventLogOrganization": pktcEventLogOrganization,
       "pktcEventLogIdentifier": pktcEventLogIdentifier,
       "pktcEventLogText": pktcEventLogText,
       "pktcEventLogEndpointName": pktcEventLogEndpointName,
       "pktcEventLogType": pktcEventLogType,
       "pktcEventLogTargetInfo": pktcEventLogTargetInfo,
       "pktcEventLogCorrelationId": pktcEventLogCorrelationId,
       "pktcEventLogAdditionalInfo": pktcEventLogAdditionalInfo,
       "pktcEventConformance": pktcEventConformance,
       "pktcEventCompliances": pktcEventCompliances,
       "pktcEventBasicCompliance": pktcEventBasicCompliance,
       "pktcEventGroups": pktcEventGroups,
       "pktcEventGroup": pktcEventGroup,
       "pktcEventNotificationGroup": pktcEventNotificationGroup}
)
