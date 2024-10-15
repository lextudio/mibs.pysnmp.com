# SNMP MIB module (RBN-IP-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-IP-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:12 2024
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

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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


# MODULE-IDENTITY

rbnIpSecurityMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55)
)
rbnIpSecurityMib.setRevisions(
        ("2011-01-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnIpSecNotifications_ObjectIdentity = ObjectIdentity
rbnIpSecNotifications = _RbnIpSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 0)
)
_RbnIpSecObjects_ObjectIdentity = ObjectIdentity
rbnIpSecObjects = _RbnIpSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1)
)
_RbnIpSecNotify_ObjectIdentity = ObjectIdentity
rbnIpSecNotify = _RbnIpSecNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1)
)
_RbnIpSecEventDateAndTime_Type = DateAndTime
_RbnIpSecEventDateAndTime_Object = MibScalar
rbnIpSecEventDateAndTime = _RbnIpSecEventDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 1),
    _RbnIpSecEventDateAndTime_Type()
)
rbnIpSecEventDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecEventDateAndTime.setStatus("current")
_RbnIpSecEventSeverity_Type = ItuPerceivedSeverity
_RbnIpSecEventSeverity_Object = MibScalar
rbnIpSecEventSeverity = _RbnIpSecEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 2),
    _RbnIpSecEventSeverity_Type()
)
rbnIpSecEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecEventSeverity.setStatus("current")
_RbnIpSecEventType_Type = IANAItuEventType
_RbnIpSecEventType_Object = MibScalar
rbnIpSecEventType = _RbnIpSecEventType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 3),
    _RbnIpSecEventType_Type()
)
rbnIpSecEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecEventType.setStatus("current")
_RbnIpSecEventProbableCause_Type = IANAItuProbableCause
_RbnIpSecEventProbableCause_Object = MibScalar
rbnIpSecEventProbableCause = _RbnIpSecEventProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 4),
    _RbnIpSecEventProbableCause_Type()
)
rbnIpSecEventProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecEventProbableCause.setStatus("current")


class _RbnIpSecTunnelIdentifier_Type(SnmpAdminString):
    """Custom type rbnIpSecTunnelIdentifier based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 270),
    )


_RbnIpSecTunnelIdentifier_Type.__name__ = "SnmpAdminString"
_RbnIpSecTunnelIdentifier_Object = MibScalar
rbnIpSecTunnelIdentifier = _RbnIpSecTunnelIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 5),
    _RbnIpSecTunnelIdentifier_Type()
)
rbnIpSecTunnelIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecTunnelIdentifier.setStatus("current")


class _RbnIpSecTunnelName_Type(SnmpAdminString):
    """Custom type rbnIpSecTunnelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RbnIpSecTunnelName_Type.__name__ = "SnmpAdminString"
_RbnIpSecTunnelName_Object = MibScalar
rbnIpSecTunnelName = _RbnIpSecTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 6),
    _RbnIpSecTunnelName_Type()
)
rbnIpSecTunnelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecTunnelName.setStatus("current")


class _RbnIpSecTunnelType_Type(Integer32):
    """Custom type rbnIpSecTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("manual", 3),
          ("static", 1))
    )


_RbnIpSecTunnelType_Type.__name__ = "Integer32"
_RbnIpSecTunnelType_Object = MibScalar
rbnIpSecTunnelType = _RbnIpSecTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 7),
    _RbnIpSecTunnelType_Type()
)
rbnIpSecTunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecTunnelType.setStatus("current")


class _RbnIpSecTunnelDownCause_Type(Integer32):
    """Custom type rbnIpSecTunnelDownCause based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("aspHomingFailure", 2),
          ("aspSoftReset", 8),
          ("configuredDown", 4),
          ("downByPeer", 6),
          ("general", 0),
          ("indeterminate", 9),
          ("keepaliveFailure", 5),
          ("noRoute", 1),
          ("ppaHomingFailure", 3),
          ("rekeyFailure", 7))
    )


_RbnIpSecTunnelDownCause_Type.__name__ = "Integer32"
_RbnIpSecTunnelDownCause_Object = MibScalar
rbnIpSecTunnelDownCause = _RbnIpSecTunnelDownCause_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 8),
    _RbnIpSecTunnelDownCause_Type()
)
rbnIpSecTunnelDownCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecTunnelDownCause.setStatus("current")


class _RbnIpSecRemoteIdType_Type(Integer32):
    """Custom type rbnIpSecRemoteIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("derAsn1Dn", 9),
          ("derAsn1Gn", 10),
          ("fqdn", 2),
          ("ipv4", 1),
          ("ipv6", 5),
          ("keyId", 11),
          ("reserved", 0),
          ("rfcAddr", 3))
    )


_RbnIpSecRemoteIdType_Type.__name__ = "Integer32"
_RbnIpSecRemoteIdType_Object = MibScalar
rbnIpSecRemoteIdType = _RbnIpSecRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 9),
    _RbnIpSecRemoteIdType_Type()
)
rbnIpSecRemoteIdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecRemoteIdType.setStatus("current")


class _RbnIpSecRemoteId_Type(SnmpAdminString):
    """Custom type rbnIpSecRemoteId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RbnIpSecRemoteId_Type.__name__ = "SnmpAdminString"
_RbnIpSecRemoteId_Object = MibScalar
rbnIpSecRemoteId = _RbnIpSecRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 10),
    _RbnIpSecRemoteId_Type()
)
rbnIpSecRemoteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecRemoteId.setStatus("current")


class _RbnIpSecLocalAddrContextName_Type(SnmpAdminString):
    """Custom type rbnIpSecLocalAddrContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbnIpSecLocalAddrContextName_Type.__name__ = "SnmpAdminString"
_RbnIpSecLocalAddrContextName_Object = MibScalar
rbnIpSecLocalAddrContextName = _RbnIpSecLocalAddrContextName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 11),
    _RbnIpSecLocalAddrContextName_Type()
)
rbnIpSecLocalAddrContextName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecLocalAddrContextName.setStatus("current")
_RbnIpSecLocalAddressType_Type = InetAddressType
_RbnIpSecLocalAddressType_Object = MibScalar
rbnIpSecLocalAddressType = _RbnIpSecLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 12),
    _RbnIpSecLocalAddressType_Type()
)
rbnIpSecLocalAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecLocalAddressType.setStatus("current")
_RbnIpSecLocalAddress_Type = InetAddress
_RbnIpSecLocalAddress_Object = MibScalar
rbnIpSecLocalAddress = _RbnIpSecLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 13),
    _RbnIpSecLocalAddress_Type()
)
rbnIpSecLocalAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecLocalAddress.setStatus("current")
_RbnIpSecRemoteAddressType_Type = InetAddressType
_RbnIpSecRemoteAddressType_Object = MibScalar
rbnIpSecRemoteAddressType = _RbnIpSecRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 14),
    _RbnIpSecRemoteAddressType_Type()
)
rbnIpSecRemoteAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecRemoteAddressType.setStatus("current")
_RbnIpSecRemoteAddress_Type = InetAddress
_RbnIpSecRemoteAddress_Object = MibScalar
rbnIpSecRemoteAddress = _RbnIpSecRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 15),
    _RbnIpSecRemoteAddress_Type()
)
rbnIpSecRemoteAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecRemoteAddress.setStatus("current")


class _RbnIpSecTunnelState_Type(Integer32):
    """Custom type rbnIpSecTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_RbnIpSecTunnelState_Type.__name__ = "Integer32"
_RbnIpSecTunnelState_Object = MibScalar
rbnIpSecTunnelState = _RbnIpSecTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 16),
    _RbnIpSecTunnelState_Type()
)
rbnIpSecTunnelState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecTunnelState.setStatus("current")


class _RbnIpSecSelfCertificateIdentifier_Type(SnmpAdminString):
    """Custom type rbnIpSecSelfCertificateIdentifier based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 522),
    )


_RbnIpSecSelfCertificateIdentifier_Type.__name__ = "SnmpAdminString"
_RbnIpSecSelfCertificateIdentifier_Object = MibScalar
rbnIpSecSelfCertificateIdentifier = _RbnIpSecSelfCertificateIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 17),
    _RbnIpSecSelfCertificateIdentifier_Type()
)
rbnIpSecSelfCertificateIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecSelfCertificateIdentifier.setStatus("current")
_RbnIpSecCertificateHandle_Type = Unsigned32
_RbnIpSecCertificateHandle_Object = MibScalar
rbnIpSecCertificateHandle = _RbnIpSecCertificateHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 18),
    _RbnIpSecCertificateHandle_Type()
)
rbnIpSecCertificateHandle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecCertificateHandle.setStatus("current")


class _RbnIpSecExpiryDateAndTime_Type(SnmpAdminString):
    """Custom type rbnIpSecExpiryDateAndTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnIpSecExpiryDateAndTime_Type.__name__ = "SnmpAdminString"
_RbnIpSecExpiryDateAndTime_Object = MibScalar
rbnIpSecExpiryDateAndTime = _RbnIpSecExpiryDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 19),
    _RbnIpSecExpiryDateAndTime_Type()
)
rbnIpSecExpiryDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecExpiryDateAndTime.setStatus("current")


class _RbnIpSecCertificateSubjectName_Type(SnmpAdminString):
    """Custom type rbnIpSecCertificateSubjectName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_RbnIpSecCertificateSubjectName_Type.__name__ = "SnmpAdminString"
_RbnIpSecCertificateSubjectName_Object = MibScalar
rbnIpSecCertificateSubjectName = _RbnIpSecCertificateSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 20),
    _RbnIpSecCertificateSubjectName_Type()
)
rbnIpSecCertificateSubjectName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIpSecCertificateSubjectName.setStatus("current")
_RbnIpSecConformance_ObjectIdentity = ObjectIdentity
rbnIpSecConformance = _RbnIpSecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 2)
)
_RbnIpSecCompliances_ObjectIdentity = ObjectIdentity
rbnIpSecCompliances = _RbnIpSecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 2, 1)
)
_RbnIpSecGroups_ObjectIdentity = ObjectIdentity
rbnIpSecGroups = _RbnIpSecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 2, 2)
)

# Managed Objects groups

rbnIpSecNotifyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 2, 2, 1)
)
rbnIpSecNotifyObjectGroup.setObjects(
      *(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelIdentifier"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelName"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelDownCause"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteIdType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteId"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddrContextName"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddressType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddress"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteAddressType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteAddress"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelState"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecSelfCertificateIdentifier"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecCertificateSubjectName"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecCertificateHandle"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecExpiryDateAndTime"))
)
if mibBuilder.loadTexts:
    rbnIpSecNotifyObjectGroup.setStatus("current")


# Notification objects

rbnIpSecTunnelStatusChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 0, 1)
)
rbnIpSecTunnelStatusChangeAlarm.setObjects(
      *(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelIdentifier"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelName"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelDownCause"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteIdType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteId"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddrContextName"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddressType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddress"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteAddressType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteAddress"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelState"))
)
if mibBuilder.loadTexts:
    rbnIpSecTunnelStatusChangeAlarm.setStatus(
        "current"
    )

rbnIpSecNoValidRSASelfCertificateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 0, 2)
)
rbnIpSecNoValidRSASelfCertificateAlarm.setObjects(
      *(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"))
)
if mibBuilder.loadTexts:
    rbnIpSecNoValidRSASelfCertificateAlarm.setStatus(
        "current"
    )

rbnIpSecNoValidRSATrustedCertificateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 0, 3)
)
rbnIpSecNoValidRSATrustedCertificateAlarm.setObjects(
      *(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"))
)
if mibBuilder.loadTexts:
    rbnIpSecNoValidRSATrustedCertificateAlarm.setStatus(
        "current"
    )

rbnIpSecRSASelfCertificateNearingExpiryAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 0, 4)
)
rbnIpSecRSASelfCertificateNearingExpiryAlarm.setObjects(
      *(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecSelfCertificateIdentifier"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecCertificateHandle"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecExpiryDateAndTime"))
)
if mibBuilder.loadTexts:
    rbnIpSecRSASelfCertificateNearingExpiryAlarm.setStatus(
        "current"
    )

rbnIpSecRSATrustedCertificateNearingExpiryAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 0, 5)
)
rbnIpSecRSATrustedCertificateNearingExpiryAlarm.setObjects(
      *(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecCertificateSubjectName"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecCertificateHandle"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecExpiryDateAndTime"))
)
if mibBuilder.loadTexts:
    rbnIpSecRSATrustedCertificateNearingExpiryAlarm.setStatus(
        "current"
    )


# Notifications groups

rbnIpSecNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 2, 2, 2)
)
rbnIpSecNotifyGroup.setObjects(
      *(("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelStatusChangeAlarm"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecNoValidRSASelfCertificateAlarm"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecNoValidRSATrustedCertificateAlarm"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecRSASelfCertificateNearingExpiryAlarm"),
        ("RBN-IP-SECURITY-MIB", "rbnIpSecRSATrustedCertificateNearingExpiryAlarm"))
)
if mibBuilder.loadTexts:
    rbnIpSecNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnIpSecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 55, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnIpSecCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-IP-SECURITY-MIB",
    **{"rbnIpSecurityMib": rbnIpSecurityMib,
       "rbnIpSecNotifications": rbnIpSecNotifications,
       "rbnIpSecTunnelStatusChangeAlarm": rbnIpSecTunnelStatusChangeAlarm,
       "rbnIpSecNoValidRSASelfCertificateAlarm": rbnIpSecNoValidRSASelfCertificateAlarm,
       "rbnIpSecNoValidRSATrustedCertificateAlarm": rbnIpSecNoValidRSATrustedCertificateAlarm,
       "rbnIpSecRSASelfCertificateNearingExpiryAlarm": rbnIpSecRSASelfCertificateNearingExpiryAlarm,
       "rbnIpSecRSATrustedCertificateNearingExpiryAlarm": rbnIpSecRSATrustedCertificateNearingExpiryAlarm,
       "rbnIpSecObjects": rbnIpSecObjects,
       "rbnIpSecNotify": rbnIpSecNotify,
       "rbnIpSecEventDateAndTime": rbnIpSecEventDateAndTime,
       "rbnIpSecEventSeverity": rbnIpSecEventSeverity,
       "rbnIpSecEventType": rbnIpSecEventType,
       "rbnIpSecEventProbableCause": rbnIpSecEventProbableCause,
       "rbnIpSecTunnelIdentifier": rbnIpSecTunnelIdentifier,
       "rbnIpSecTunnelName": rbnIpSecTunnelName,
       "rbnIpSecTunnelType": rbnIpSecTunnelType,
       "rbnIpSecTunnelDownCause": rbnIpSecTunnelDownCause,
       "rbnIpSecRemoteIdType": rbnIpSecRemoteIdType,
       "rbnIpSecRemoteId": rbnIpSecRemoteId,
       "rbnIpSecLocalAddrContextName": rbnIpSecLocalAddrContextName,
       "rbnIpSecLocalAddressType": rbnIpSecLocalAddressType,
       "rbnIpSecLocalAddress": rbnIpSecLocalAddress,
       "rbnIpSecRemoteAddressType": rbnIpSecRemoteAddressType,
       "rbnIpSecRemoteAddress": rbnIpSecRemoteAddress,
       "rbnIpSecTunnelState": rbnIpSecTunnelState,
       "rbnIpSecSelfCertificateIdentifier": rbnIpSecSelfCertificateIdentifier,
       "rbnIpSecCertificateHandle": rbnIpSecCertificateHandle,
       "rbnIpSecExpiryDateAndTime": rbnIpSecExpiryDateAndTime,
       "rbnIpSecCertificateSubjectName": rbnIpSecCertificateSubjectName,
       "rbnIpSecConformance": rbnIpSecConformance,
       "rbnIpSecCompliances": rbnIpSecCompliances,
       "rbnIpSecCompliance": rbnIpSecCompliance,
       "rbnIpSecGroups": rbnIpSecGroups,
       "rbnIpSecNotifyObjectGroup": rbnIpSecNotifyObjectGroup,
       "rbnIpSecNotifyGroup": rbnIpSecNotifyGroup}
)
