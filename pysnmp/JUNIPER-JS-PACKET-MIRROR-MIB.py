# SNMP MIB module (JUNIPER-JS-PACKET-MIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JS-PACKET-MIRROR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:19 2024
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

(Ipv6AddressPrefix,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6AddressPrefix")

(jnxJsPacketMirror,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsPacketMirror")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxJsPacketMirrorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1)
)
jnxJsPacketMirrorMIB.setRevisions(
        ("2009-10-29 00:00",
         "2010-02-25 00:00",
         "2010-12-16 00:00",
         "2011-03-16 00:00",
         "2011-03-23 00:00",
         "2011-06-07 00:00",
         "2011-11-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsPacketMirrorNotifications_ObjectIdentity = ObjectIdentity
jnxJsPacketMirrorNotifications = _JnxJsPacketMirrorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 0)
)
_JnxJsPacketMirrorObjects_ObjectIdentity = ObjectIdentity
jnxJsPacketMirrorObjects = _JnxJsPacketMirrorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1)
)
_JnxJsPacketMirrorTrapVars_ObjectIdentity = ObjectIdentity
jnxJsPacketMirrorTrapVars = _JnxJsPacketMirrorTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1)
)
_JnxJsPacketMirrorIdentifier_Type = Unsigned32
_JnxJsPacketMirrorIdentifier_Object = MibScalar
jnxJsPacketMirrorIdentifier = _JnxJsPacketMirrorIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 1),
    _JnxJsPacketMirrorIdentifier_Type()
)
jnxJsPacketMirrorIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorIdentifier.setStatus("current")
_JnxJsPacketMirrorSessionIdentifier_Type = Unsigned32
_JnxJsPacketMirrorSessionIdentifier_Object = MibScalar
jnxJsPacketMirrorSessionIdentifier = _JnxJsPacketMirrorSessionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 2),
    _JnxJsPacketMirrorSessionIdentifier_Type()
)
jnxJsPacketMirrorSessionIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorSessionIdentifier.setStatus("current")
_JnxJsPacketMirrorTrigger_Type = DisplayString
_JnxJsPacketMirrorTrigger_Object = MibScalar
jnxJsPacketMirrorTrigger = _JnxJsPacketMirrorTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 3),
    _JnxJsPacketMirrorTrigger_Type()
)
jnxJsPacketMirrorTrigger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorTrigger.setStatus("current")


class _JnxJsPacketMirrorTriggerType_Type(Integer32):
    """Custom type jnxJsPacketMirrorTriggerType based on Integer32"""
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
        *(("acctSessionId", 5),
          ("callingStationId", 4),
          ("circuitId", 8),
          ("interfaceString", 0),
          ("ipAddress", 1),
          ("nasPortId", 2),
          ("option82", 6),
          ("remoteId", 7),
          ("username", 3))
    )


_JnxJsPacketMirrorTriggerType_Type.__name__ = "Integer32"
_JnxJsPacketMirrorTriggerType_Object = MibScalar
jnxJsPacketMirrorTriggerType = _JnxJsPacketMirrorTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 4),
    _JnxJsPacketMirrorTriggerType_Type()
)
jnxJsPacketMirrorTriggerType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorTriggerType.setStatus("current")


class _JnxJsPacketMirrorConfigurationSource_Type(Integer32):
    """Custom type jnxJsPacketMirrorConfigurationSource based on Integer32"""
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
        *(("cliStatic", 3),
          ("cliTrigger", 2),
          ("dtcp", 4),
          ("radiusCoa", 1),
          ("radiusLogin", 0))
    )


_JnxJsPacketMirrorConfigurationSource_Type.__name__ = "Integer32"
_JnxJsPacketMirrorConfigurationSource_Object = MibScalar
jnxJsPacketMirrorConfigurationSource = _JnxJsPacketMirrorConfigurationSource_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 5),
    _JnxJsPacketMirrorConfigurationSource_Type()
)
jnxJsPacketMirrorConfigurationSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorConfigurationSource.setStatus("current")


class _JnxJsPacketMirrorErrorCause_Type(Integer32):
    """Custom type jnxJsPacketMirrorErrorCause based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dfcdNak", 10),
          ("featureNotSupported", 6),
          ("genericFailure", 0),
          ("invalidAnalyzerAddress", 4),
          ("memoryExhausted", 2),
          ("missingOrInvalidAttribute", 7),
          ("nameLengthExceeded", 9),
          ("noResourcesAvailable", 1),
          ("noSuchName", 3),
          ("noSuchUserOrInterface", 5),
          ("routerMismatch", 8))
    )


_JnxJsPacketMirrorErrorCause_Type.__name__ = "Integer32"
_JnxJsPacketMirrorErrorCause_Object = MibScalar
jnxJsPacketMirrorErrorCause = _JnxJsPacketMirrorErrorCause_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 6),
    _JnxJsPacketMirrorErrorCause_Type()
)
jnxJsPacketMirrorErrorCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorErrorCause.setStatus("current")
_JnxJsPacketMirrorErrorString_Type = DisplayString
_JnxJsPacketMirrorErrorString_Object = MibScalar
jnxJsPacketMirrorErrorString = _JnxJsPacketMirrorErrorString_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 7),
    _JnxJsPacketMirrorErrorString_Type()
)
jnxJsPacketMirrorErrorString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorErrorString.setStatus("current")


class _JnxJsPacketMirrorApplicationName_Type(Integer32):
    """Custom type jnxJsPacketMirrorApplicationName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("authd", 0)
    )


_JnxJsPacketMirrorApplicationName_Type.__name__ = "Integer32"
_JnxJsPacketMirrorApplicationName_Object = MibScalar
jnxJsPacketMirrorApplicationName = _JnxJsPacketMirrorApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 8),
    _JnxJsPacketMirrorApplicationName_Type()
)
jnxJsPacketMirrorApplicationName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorApplicationName.setStatus("current")
_JnxJsPacketMirrorAnalyzerAddress_Type = IpAddress
_JnxJsPacketMirrorAnalyzerAddress_Object = MibScalar
jnxJsPacketMirrorAnalyzerAddress = _JnxJsPacketMirrorAnalyzerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 9),
    _JnxJsPacketMirrorAnalyzerAddress_Type()
)
jnxJsPacketMirrorAnalyzerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorAnalyzerAddress.setStatus("current")


class _JnxJsPacketMirrorUserName_Type(DisplayString):
    """Custom type jnxJsPacketMirrorUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxJsPacketMirrorUserName_Type.__name__ = "DisplayString"
_JnxJsPacketMirrorUserName_Object = MibScalar
jnxJsPacketMirrorUserName = _JnxJsPacketMirrorUserName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 10),
    _JnxJsPacketMirrorUserName_Type()
)
jnxJsPacketMirrorUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorUserName.setStatus("current")
_JnxJsPacketMirrorDateAndTime_Type = DateAndTime
_JnxJsPacketMirrorDateAndTime_Object = MibScalar
jnxJsPacketMirrorDateAndTime = _JnxJsPacketMirrorDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 11),
    _JnxJsPacketMirrorDateAndTime_Type()
)
jnxJsPacketMirrorDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorDateAndTime.setStatus("current")


class _JnxJsPacketMirrorRouterId_Type(DisplayString):
    """Custom type jnxJsPacketMirrorRouterId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 257),
    )


_JnxJsPacketMirrorRouterId_Type.__name__ = "DisplayString"
_JnxJsPacketMirrorRouterId_Object = MibScalar
jnxJsPacketMirrorRouterId = _JnxJsPacketMirrorRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 12),
    _JnxJsPacketMirrorRouterId_Type()
)
jnxJsPacketMirrorRouterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorRouterId.setStatus("current")


class _JnxJsPacketMirrorDirection_Type(Integer32):
    """Custom type jnxJsPacketMirrorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirection", 2),
          ("egress", 1),
          ("ingress", 0))
    )


_JnxJsPacketMirrorDirection_Type.__name__ = "Integer32"
_JnxJsPacketMirrorDirection_Object = MibScalar
jnxJsPacketMirrorDirection = _JnxJsPacketMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 13),
    _JnxJsPacketMirrorDirection_Type()
)
jnxJsPacketMirrorDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorDirection.setStatus("current")
_JnxJsPacketMirrorTargetIpAddress_Type = IpAddress
_JnxJsPacketMirrorTargetIpAddress_Object = MibScalar
jnxJsPacketMirrorTargetIpAddress = _JnxJsPacketMirrorTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 14),
    _JnxJsPacketMirrorTargetIpAddress_Type()
)
jnxJsPacketMirrorTargetIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorTargetIpAddress.setStatus("current")


class _JnxJsPacketMirrorTerminationReason_Type(Integer32):
    """Custom type jnxJsPacketMirrorTerminationReason based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("adminReboot", 7),
          ("adminReset", 6),
          ("authenticationReject", 23),
          ("callback", 16),
          ("genericFailure", 0),
          ("hostRequest", 18),
          ("idleTimeout", 4),
          ("interfaceDeleted", 24),
          ("lostCarrier", 2),
          ("lostService", 3),
          ("nasError", 9),
          ("nasReboot1", 11),
          ("nasRequest0", 10),
          ("portAdministrativelyDisabled", 22),
          ("portError", 8),
          ("portPreempted", 13),
          ("portReinitialized", 21),
          ("portSuspended", 14),
          ("portUnneeded", 12),
          ("reauthenticationFailure", 20),
          ("serviceUnavailable", 15),
          ("sessionTimeout", 5),
          ("supplicantRestart", 19),
          ("userError", 17),
          ("userRequest", 1))
    )


_JnxJsPacketMirrorTerminationReason_Type.__name__ = "Integer32"
_JnxJsPacketMirrorTerminationReason_Object = MibScalar
jnxJsPacketMirrorTerminationReason = _JnxJsPacketMirrorTerminationReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 15),
    _JnxJsPacketMirrorTerminationReason_Type()
)
jnxJsPacketMirrorTerminationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorTerminationReason.setStatus("current")


class _JnxPacketMirrorCallingStationIdentifier_Type(DisplayString):
    """Custom type jnxPacketMirrorCallingStationIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxPacketMirrorCallingStationIdentifier_Type.__name__ = "DisplayString"
_JnxPacketMirrorCallingStationIdentifier_Object = MibScalar
jnxPacketMirrorCallingStationIdentifier = _JnxPacketMirrorCallingStationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 16),
    _JnxPacketMirrorCallingStationIdentifier_Type()
)
jnxPacketMirrorCallingStationIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPacketMirrorCallingStationIdentifier.setStatus("current")


class _JnxPacketMirrorNasIdentifier_Type(DisplayString):
    """Custom type jnxPacketMirrorNasIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxPacketMirrorNasIdentifier_Type.__name__ = "DisplayString"
_JnxPacketMirrorNasIdentifier_Object = MibScalar
jnxPacketMirrorNasIdentifier = _JnxPacketMirrorNasIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 17),
    _JnxPacketMirrorNasIdentifier_Type()
)
jnxPacketMirrorNasIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPacketMirrorNasIdentifier.setStatus("current")
_JnxJsPacketMirrorOctetsReceived_Type = Counter64
_JnxJsPacketMirrorOctetsReceived_Object = MibScalar
jnxJsPacketMirrorOctetsReceived = _JnxJsPacketMirrorOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 18),
    _JnxJsPacketMirrorOctetsReceived_Type()
)
jnxJsPacketMirrorOctetsReceived.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorOctetsReceived.setStatus("current")
_JnxJsPacketMirrorOctetsTransmitted_Type = Counter64
_JnxJsPacketMirrorOctetsTransmitted_Object = MibScalar
jnxJsPacketMirrorOctetsTransmitted = _JnxJsPacketMirrorOctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 19),
    _JnxJsPacketMirrorOctetsTransmitted_Type()
)
jnxJsPacketMirrorOctetsTransmitted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorOctetsTransmitted.setStatus("current")
_JnxJsPacketMirrorTargetIpv6Address_Type = Ipv6AddressPrefix
_JnxJsPacketMirrorTargetIpv6Address_Object = MibScalar
jnxJsPacketMirrorTargetIpv6Address = _JnxJsPacketMirrorTargetIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 20),
    _JnxJsPacketMirrorTargetIpv6Address_Type()
)
jnxJsPacketMirrorTargetIpv6Address.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorTargetIpv6Address.setStatus("current")
_JnxJsPacketMirrorTrgtIpv6PfxLen_Type = Unsigned32
_JnxJsPacketMirrorTrgtIpv6PfxLen_Object = MibScalar
jnxJsPacketMirrorTrgtIpv6PfxLen = _JnxJsPacketMirrorTrgtIpv6PfxLen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 1, 1, 21),
    _JnxJsPacketMirrorTrgtIpv6PfxLen_Type()
)
jnxJsPacketMirrorTrgtIpv6PfxLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsPacketMirrorTrgtIpv6PfxLen.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJsPacketMirrorMirroringFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 0, 1)
)
jnxJsPacketMirrorMirroringFailure.setObjects(
      *(("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDateAndTime"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorConfigurationSource"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTriggerType"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrigger"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorRouterId"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorUserName"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorSessionIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorErrorCause"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorApplicationName"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorErrorString"))
)
if mibBuilder.loadTexts:
    jnxJsPacketMirrorMirroringFailure.setStatus(
        "current"
    )

jnxJsPacketMirrorLiSubscriberLoggedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 0, 2)
)
jnxJsPacketMirrorLiSubscriberLoggedIn.setObjects(
      *(("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDateAndTime"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorConfigurationSource"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTriggerType"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrigger"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorRouterId"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorSessionIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDirection"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorAnalyzerAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxPacketMirrorNasIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxPacketMirrorCallingStationIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpv6Address"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrgtIpv6PfxLen"))
)
if mibBuilder.loadTexts:
    jnxJsPacketMirrorLiSubscriberLoggedIn.setStatus(
        "current"
    )

jnxJsPacketMirrorLiSubscriberLogInFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 0, 3)
)
jnxJsPacketMirrorLiSubscriberLogInFailed.setObjects(
      *(("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDateAndTime"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorConfigurationSource"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTriggerType"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrigger"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorRouterId"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorSessionIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDirection"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorAnalyzerAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorErrorCause"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorErrorString"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxPacketMirrorCallingStationIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpv6Address"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrgtIpv6PfxLen"))
)
if mibBuilder.loadTexts:
    jnxJsPacketMirrorLiSubscriberLogInFailed.setStatus(
        "current"
    )

jnxJsPacketMirrorLiSubscriberLoggedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 0, 4)
)
jnxJsPacketMirrorLiSubscriberLoggedOut.setObjects(
      *(("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDateAndTime"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorConfigurationSource"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTriggerType"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrigger"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorRouterId"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorSessionIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDirection"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorAnalyzerAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTerminationReason"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorOctetsReceived"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorOctetsTransmitted"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpv6Address"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrgtIpv6PfxLen"))
)
if mibBuilder.loadTexts:
    jnxJsPacketMirrorLiSubscriberLoggedOut.setStatus(
        "current"
    )

jnxJsPacketMirrorLiServiceActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 0, 5)
)
jnxJsPacketMirrorLiServiceActivated.setObjects(
      *(("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDateAndTime"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorConfigurationSource"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTriggerType"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrigger"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorRouterId"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorSessionIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDirection"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxPacketMirrorNasIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxPacketMirrorCallingStationIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorAnalyzerAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpv6Address"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrgtIpv6PfxLen"))
)
if mibBuilder.loadTexts:
    jnxJsPacketMirrorLiServiceActivated.setStatus(
        "current"
    )

jnxJsPacketMirrorLiServiceActivationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 0, 6)
)
jnxJsPacketMirrorLiServiceActivationFailed.setObjects(
      *(("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDateAndTime"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorConfigurationSource"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTriggerType"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrigger"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorRouterId"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorSessionIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDirection"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorAnalyzerAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorErrorCause"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorErrorString"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxPacketMirrorCallingStationIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpv6Address"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrgtIpv6PfxLen"))
)
if mibBuilder.loadTexts:
    jnxJsPacketMirrorLiServiceActivationFailed.setStatus(
        "current"
    )

jnxJsPacketMirrorLiServiceDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16, 1, 0, 7)
)
jnxJsPacketMirrorLiServiceDeactivated.setObjects(
      *(("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDateAndTime"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorConfigurationSource"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTriggerType"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrigger"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorRouterId"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorSessionIdentifier"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorDirection"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorAnalyzerAddress"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTerminationReason"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTargetIpv6Address"),
        ("JUNIPER-JS-PACKET-MIRROR-MIB", "jnxJsPacketMirrorTrgtIpv6PfxLen"))
)
if mibBuilder.loadTexts:
    jnxJsPacketMirrorLiServiceDeactivated.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-PACKET-MIRROR-MIB",
    **{"jnxJsPacketMirrorMIB": jnxJsPacketMirrorMIB,
       "jnxJsPacketMirrorNotifications": jnxJsPacketMirrorNotifications,
       "jnxJsPacketMirrorMirroringFailure": jnxJsPacketMirrorMirroringFailure,
       "jnxJsPacketMirrorLiSubscriberLoggedIn": jnxJsPacketMirrorLiSubscriberLoggedIn,
       "jnxJsPacketMirrorLiSubscriberLogInFailed": jnxJsPacketMirrorLiSubscriberLogInFailed,
       "jnxJsPacketMirrorLiSubscriberLoggedOut": jnxJsPacketMirrorLiSubscriberLoggedOut,
       "jnxJsPacketMirrorLiServiceActivated": jnxJsPacketMirrorLiServiceActivated,
       "jnxJsPacketMirrorLiServiceActivationFailed": jnxJsPacketMirrorLiServiceActivationFailed,
       "jnxJsPacketMirrorLiServiceDeactivated": jnxJsPacketMirrorLiServiceDeactivated,
       "jnxJsPacketMirrorObjects": jnxJsPacketMirrorObjects,
       "jnxJsPacketMirrorTrapVars": jnxJsPacketMirrorTrapVars,
       "jnxJsPacketMirrorIdentifier": jnxJsPacketMirrorIdentifier,
       "jnxJsPacketMirrorSessionIdentifier": jnxJsPacketMirrorSessionIdentifier,
       "jnxJsPacketMirrorTrigger": jnxJsPacketMirrorTrigger,
       "jnxJsPacketMirrorTriggerType": jnxJsPacketMirrorTriggerType,
       "jnxJsPacketMirrorConfigurationSource": jnxJsPacketMirrorConfigurationSource,
       "jnxJsPacketMirrorErrorCause": jnxJsPacketMirrorErrorCause,
       "jnxJsPacketMirrorErrorString": jnxJsPacketMirrorErrorString,
       "jnxJsPacketMirrorApplicationName": jnxJsPacketMirrorApplicationName,
       "jnxJsPacketMirrorAnalyzerAddress": jnxJsPacketMirrorAnalyzerAddress,
       "jnxJsPacketMirrorUserName": jnxJsPacketMirrorUserName,
       "jnxJsPacketMirrorDateAndTime": jnxJsPacketMirrorDateAndTime,
       "jnxJsPacketMirrorRouterId": jnxJsPacketMirrorRouterId,
       "jnxJsPacketMirrorDirection": jnxJsPacketMirrorDirection,
       "jnxJsPacketMirrorTargetIpAddress": jnxJsPacketMirrorTargetIpAddress,
       "jnxJsPacketMirrorTerminationReason": jnxJsPacketMirrorTerminationReason,
       "jnxPacketMirrorCallingStationIdentifier": jnxPacketMirrorCallingStationIdentifier,
       "jnxPacketMirrorNasIdentifier": jnxPacketMirrorNasIdentifier,
       "jnxJsPacketMirrorOctetsReceived": jnxJsPacketMirrorOctetsReceived,
       "jnxJsPacketMirrorOctetsTransmitted": jnxJsPacketMirrorOctetsTransmitted,
       "jnxJsPacketMirrorTargetIpv6Address": jnxJsPacketMirrorTargetIpv6Address,
       "jnxJsPacketMirrorTrgtIpv6PfxLen": jnxJsPacketMirrorTrgtIpv6PfxLen}
)
