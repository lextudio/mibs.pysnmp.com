# SNMP MIB module (Juniper-PACKET-MIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-PACKET-MIRROR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:53 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniPacketMirrorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77)
)
juniPacketMirrorMIB.setRevisions(
        ("2009-10-28 09:40",
         "2006-07-19 20:57",
         "2005-06-30 18:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniPacketMirrorTrapEnables_ObjectIdentity = ObjectIdentity
juniPacketMirrorTrapEnables = _JuniPacketMirrorTrapEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 2)
)


class _JuniPacketMirrorTrapEnable_Type(TruthValue):
    """Custom type juniPacketMirrorTrapEnable based on TruthValue"""


_JuniPacketMirrorTrapEnable_Object = MibScalar
juniPacketMirrorTrapEnable = _JuniPacketMirrorTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 2, 1),
    _JuniPacketMirrorTrapEnable_Type()
)
juniPacketMirrorTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPacketMirrorTrapEnable.setStatus("current")
_JuniPacketMirrorTraps_ObjectIdentity = ObjectIdentity
juniPacketMirrorTraps = _JuniPacketMirrorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3)
)
_JuniPacketMirrorTrapPrefix_ObjectIdentity = ObjectIdentity
juniPacketMirrorTrapPrefix = _JuniPacketMirrorTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 0)
)
_JuniPacketMirrorNotificationObjects_ObjectIdentity = ObjectIdentity
juniPacketMirrorNotificationObjects = _JuniPacketMirrorNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1)
)
_JuniPacketMirrorIdentifier_Type = Unsigned32
_JuniPacketMirrorIdentifier_Object = MibScalar
juniPacketMirrorIdentifier = _JuniPacketMirrorIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 1),
    _JuniPacketMirrorIdentifier_Type()
)
juniPacketMirrorIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorIdentifier.setStatus("current")
_JuniPacketMirrorSessionIdentifier_Type = Unsigned32
_JuniPacketMirrorSessionIdentifier_Object = MibScalar
juniPacketMirrorSessionIdentifier = _JuniPacketMirrorSessionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 2),
    _JuniPacketMirrorSessionIdentifier_Type()
)
juniPacketMirrorSessionIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorSessionIdentifier.setStatus("current")
_JuniPacketMirrorTrigger_Type = DisplayString
_JuniPacketMirrorTrigger_Object = MibScalar
juniPacketMirrorTrigger = _JuniPacketMirrorTrigger_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 3),
    _JuniPacketMirrorTrigger_Type()
)
juniPacketMirrorTrigger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorTrigger.setStatus("current")


class _JuniPacketMirrorTriggerType_Type(Integer32):
    """Custom type juniPacketMirrorTriggerType based on Integer32"""
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
          ("agentCircuitId", 7),
          ("agentRemoteId", 8),
          ("callingStationId", 4),
          ("dhcpOption82", 6),
          ("interfaceString", 0),
          ("ipAddress", 1),
          ("nasPortId", 2),
          ("username", 3))
    )


_JuniPacketMirrorTriggerType_Type.__name__ = "Integer32"
_JuniPacketMirrorTriggerType_Object = MibScalar
juniPacketMirrorTriggerType = _JuniPacketMirrorTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 4),
    _JuniPacketMirrorTriggerType_Type()
)
juniPacketMirrorTriggerType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorTriggerType.setStatus("current")


class _JuniPacketMirrorConfigurationSource_Type(Integer32):
    """Custom type juniPacketMirrorConfigurationSource based on Integer32"""
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
        *(("cliStatic", 3),
          ("cliTrigger", 2),
          ("radiusCoa", 1),
          ("radiusLogin", 0))
    )


_JuniPacketMirrorConfigurationSource_Type.__name__ = "Integer32"
_JuniPacketMirrorConfigurationSource_Object = MibScalar
juniPacketMirrorConfigurationSource = _JuniPacketMirrorConfigurationSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 5),
    _JuniPacketMirrorConfigurationSource_Type()
)
juniPacketMirrorConfigurationSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorConfigurationSource.setStatus("current")


class _JuniPacketMirrorErrorCause_Type(Integer32):
    """Custom type juniPacketMirrorErrorCause based on Integer32"""
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
        *(("featureNotSupported", 6),
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


_JuniPacketMirrorErrorCause_Type.__name__ = "Integer32"
_JuniPacketMirrorErrorCause_Object = MibScalar
juniPacketMirrorErrorCause = _JuniPacketMirrorErrorCause_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 6),
    _JuniPacketMirrorErrorCause_Type()
)
juniPacketMirrorErrorCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorErrorCause.setStatus("current")
_JuniPacketMirrorErrorString_Type = DisplayString
_JuniPacketMirrorErrorString_Object = MibScalar
juniPacketMirrorErrorString = _JuniPacketMirrorErrorString_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 7),
    _JuniPacketMirrorErrorString_Type()
)
juniPacketMirrorErrorString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorErrorString.setStatus("current")


class _JuniPacketMirrorApplicationName_Type(Integer32):
    """Custom type juniPacketMirrorApplicationName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("policyManager", 0)
    )


_JuniPacketMirrorApplicationName_Type.__name__ = "Integer32"
_JuniPacketMirrorApplicationName_Object = MibScalar
juniPacketMirrorApplicationName = _JuniPacketMirrorApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 8),
    _JuniPacketMirrorApplicationName_Type()
)
juniPacketMirrorApplicationName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorApplicationName.setStatus("current")
_JuniPacketMirrorAnalyzerAddress_Type = IpAddress
_JuniPacketMirrorAnalyzerAddress_Object = MibScalar
juniPacketMirrorAnalyzerAddress = _JuniPacketMirrorAnalyzerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 9),
    _JuniPacketMirrorAnalyzerAddress_Type()
)
juniPacketMirrorAnalyzerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorAnalyzerAddress.setStatus("current")


class _JuniPacketMirrorUserName_Type(DisplayString):
    """Custom type juniPacketMirrorUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JuniPacketMirrorUserName_Type.__name__ = "DisplayString"
_JuniPacketMirrorUserName_Object = MibScalar
juniPacketMirrorUserName = _JuniPacketMirrorUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 10),
    _JuniPacketMirrorUserName_Type()
)
juniPacketMirrorUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorUserName.setStatus("current")


class _JuniPacketMirrorPolicyName_Type(DisplayString):
    """Custom type juniPacketMirrorPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_JuniPacketMirrorPolicyName_Type.__name__ = "DisplayString"
_JuniPacketMirrorPolicyName_Object = MibScalar
juniPacketMirrorPolicyName = _JuniPacketMirrorPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 11),
    _JuniPacketMirrorPolicyName_Type()
)
juniPacketMirrorPolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorPolicyName.setStatus("current")
_JuniPacketMirrorPolicyId_Type = Unsigned32
_JuniPacketMirrorPolicyId_Object = MibScalar
juniPacketMirrorPolicyId = _JuniPacketMirrorPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 12),
    _JuniPacketMirrorPolicyId_Type()
)
juniPacketMirrorPolicyId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorPolicyId.setStatus("current")
_JuniPacketMirrorDateAndTime_Type = DateAndTime
_JuniPacketMirrorDateAndTime_Object = MibScalar
juniPacketMirrorDateAndTime = _JuniPacketMirrorDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 13),
    _JuniPacketMirrorDateAndTime_Type()
)
juniPacketMirrorDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorDateAndTime.setStatus("current")
_JuniPacketMirrorRouterId_Type = Unsigned32
_JuniPacketMirrorRouterId_Object = MibScalar
juniPacketMirrorRouterId = _JuniPacketMirrorRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 14),
    _JuniPacketMirrorRouterId_Type()
)
juniPacketMirrorRouterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorRouterId.setStatus("current")


class _JuniPacketMirrorDirection_Type(Integer32):
    """Custom type juniPacketMirrorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("egress", 1),
          ("ingress", 0))
    )


_JuniPacketMirrorDirection_Type.__name__ = "Integer32"
_JuniPacketMirrorDirection_Object = MibScalar
juniPacketMirrorDirection = _JuniPacketMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 15),
    _JuniPacketMirrorDirection_Type()
)
juniPacketMirrorDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorDirection.setStatus("current")
_JuniPacketMirrorTargetIpAddress_Type = IpAddress
_JuniPacketMirrorTargetIpAddress_Object = MibScalar
juniPacketMirrorTargetIpAddress = _JuniPacketMirrorTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 16),
    _JuniPacketMirrorTargetIpAddress_Type()
)
juniPacketMirrorTargetIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorTargetIpAddress.setStatus("current")


class _JuniPacketMirrorTerminationReason_Type(Integer32):
    """Custom type juniPacketMirrorTerminationReason based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("adminReboot", 7),
          ("adminReset", 6),
          ("callback", 16),
          ("genericFailure", 0),
          ("hostRequest", 18),
          ("idleTimeout", 4),
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


_JuniPacketMirrorTerminationReason_Type.__name__ = "Integer32"
_JuniPacketMirrorTerminationReason_Object = MibScalar
juniPacketMirrorTerminationReason = _JuniPacketMirrorTerminationReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 1, 17),
    _JuniPacketMirrorTerminationReason_Type()
)
juniPacketMirrorTerminationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniPacketMirrorTerminationReason.setStatus("current")
_JuniPacketMirrorConformance_ObjectIdentity = ObjectIdentity
juniPacketMirrorConformance = _JuniPacketMirrorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 4)
)
_JuniPacketMirrorCompliances_ObjectIdentity = ObjectIdentity
juniPacketMirrorCompliances = _JuniPacketMirrorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 4, 1)
)
_JuniPacketMirrorGroups_ObjectIdentity = ObjectIdentity
juniPacketMirrorGroups = _JuniPacketMirrorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 4, 2)
)

# Managed Objects groups

juniPacketMirrorNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 4, 2, 2)
)
juniPacketMirrorNotificationObjectsGroup.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTrigger"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTriggerType"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorConfigurationSource"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorErrorCause"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorErrorString"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorApplicationName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorAnalyzerAddress"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorUserName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDirection"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorNotificationObjectsGroup.setStatus("deprecated")

juniPacketMirrorNotificationObjectsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 4, 2, 4)
)
juniPacketMirrorNotificationObjectsGroup2.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTrigger"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTriggerType"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorConfigurationSource"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorErrorCause"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorErrorString"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorApplicationName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorAnalyzerAddress"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorUserName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDirection"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTargetIpAddress"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTerminationReason"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorNotificationObjectsGroup2.setStatus("current")


# Notification objects

juniPacketMirrorRadiusBasedMirroringFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 0, 1)
)
juniPacketMirrorRadiusBasedMirroringFailure.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorConfigurationSource"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTriggerType"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTrigger"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorUserName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorErrorCause"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorApplicationName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorErrorString"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorRadiusBasedMirroringFailure.setStatus(
        "current"
    )

juniPacketMirrorCliTriggerBasedMirroringFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 0, 2)
)
juniPacketMirrorCliTriggerBasedMirroringFailure.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorConfigurationSource"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTriggerType"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTrigger"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorErrorCause"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorApplicationName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorErrorString"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorCliTriggerBasedMirroringFailure.setStatus(
        "current"
    )

juniPacketMirrorInterfaceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 0, 3)
)
juniPacketMirrorInterfaceDeleted.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorConfigurationSource"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTriggerType"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTrigger"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDirection"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorInterfaceDeleted.setStatus(
        "current"
    )

juniPacketMirrorAnalyzerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 0, 4)
)
juniPacketMirrorAnalyzerUnreachable.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorAnalyzerAddress"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorAnalyzerUnreachable.setStatus(
        "current"
    )

juniPacketMirrorSessionStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 0, 5)
)
juniPacketMirrorSessionStart.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorConfigurationSource"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTriggerType"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTrigger"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDirection"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTargetIpAddress"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorAnalyzerAddress"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorSessionStart.setStatus(
        "current"
    )

juniPacketMirrorSessionEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 0, 6)
)
juniPacketMirrorSessionEnd.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorConfigurationSource"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTriggerType"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTrigger"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDirection"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTargetIpAddress"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorAnalyzerAddress"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTerminationReason"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorSessionEnd.setStatus(
        "current"
    )

juniPacketMirrorInterfaceSessionActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 0, 7)
)
juniPacketMirrorInterfaceSessionActivated.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorConfigurationSource"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTriggerType"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTrigger"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDirection"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTargetIpAddress"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorAnalyzerAddress"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorInterfaceSessionActivated.setStatus(
        "current"
    )

juniPacketMirrorInterfaceSessionDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 0, 8)
)
juniPacketMirrorInterfaceSessionDeactivated.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorConfigurationSource"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTriggerType"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTrigger"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDirection"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTargetIpAddress"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorAnalyzerAddress"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorInterfaceSessionDeactivated.setStatus(
        "current"
    )

juniPacketMirrorSessionReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 0, 9)
)
juniPacketMirrorSessionReject.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorConfigurationSource"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTriggerType"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTrigger"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDirection"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorSessionReject.setStatus(
        "current"
    )

juniPacketMirrorSessionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 3, 0, 10)
)
juniPacketMirrorSessionFailed.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDateAndTime"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorConfigurationSource"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTriggerType"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTrigger"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRouterId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionIdentifier"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyName"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorPolicyId"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorDirection"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTargetIpAddress"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorAnalyzerAddress"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorTerminationReason"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorSessionFailed.setStatus(
        "current"
    )


# Notifications groups

juniPacketMirrorNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 4, 2, 1)
)
juniPacketMirrorNotificationGroup.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRadiusBasedMirroringFailure"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorCliTriggerBasedMirroringFailure"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorInterfaceDeleted"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorAnalyzerUnreachable"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorNotificationGroup.setStatus(
        "deprecated"
    )

juniPacketMirrorNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 4, 2, 3)
)
juniPacketMirrorNotificationGroup2.setObjects(
      *(("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorRadiusBasedMirroringFailure"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorCliTriggerBasedMirroringFailure"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorInterfaceDeleted"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorAnalyzerUnreachable"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionStart"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionEnd"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorInterfaceSessionActivated"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorInterfaceSessionDeactivated"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionReject"),
        ("Juniper-PACKET-MIRROR-MIB", "juniPacketMirrorSessionFailed"))
)
if mibBuilder.loadTexts:
    juniPacketMirrorNotificationGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniPacketMirrorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 77, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniPacketMirrorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-PACKET-MIRROR-MIB",
    **{"juniPacketMirrorMIB": juniPacketMirrorMIB,
       "juniPacketMirrorTrapEnables": juniPacketMirrorTrapEnables,
       "juniPacketMirrorTrapEnable": juniPacketMirrorTrapEnable,
       "juniPacketMirrorTraps": juniPacketMirrorTraps,
       "juniPacketMirrorTrapPrefix": juniPacketMirrorTrapPrefix,
       "juniPacketMirrorRadiusBasedMirroringFailure": juniPacketMirrorRadiusBasedMirroringFailure,
       "juniPacketMirrorCliTriggerBasedMirroringFailure": juniPacketMirrorCliTriggerBasedMirroringFailure,
       "juniPacketMirrorInterfaceDeleted": juniPacketMirrorInterfaceDeleted,
       "juniPacketMirrorAnalyzerUnreachable": juniPacketMirrorAnalyzerUnreachable,
       "juniPacketMirrorSessionStart": juniPacketMirrorSessionStart,
       "juniPacketMirrorSessionEnd": juniPacketMirrorSessionEnd,
       "juniPacketMirrorInterfaceSessionActivated": juniPacketMirrorInterfaceSessionActivated,
       "juniPacketMirrorInterfaceSessionDeactivated": juniPacketMirrorInterfaceSessionDeactivated,
       "juniPacketMirrorSessionReject": juniPacketMirrorSessionReject,
       "juniPacketMirrorSessionFailed": juniPacketMirrorSessionFailed,
       "juniPacketMirrorNotificationObjects": juniPacketMirrorNotificationObjects,
       "juniPacketMirrorIdentifier": juniPacketMirrorIdentifier,
       "juniPacketMirrorSessionIdentifier": juniPacketMirrorSessionIdentifier,
       "juniPacketMirrorTrigger": juniPacketMirrorTrigger,
       "juniPacketMirrorTriggerType": juniPacketMirrorTriggerType,
       "juniPacketMirrorConfigurationSource": juniPacketMirrorConfigurationSource,
       "juniPacketMirrorErrorCause": juniPacketMirrorErrorCause,
       "juniPacketMirrorErrorString": juniPacketMirrorErrorString,
       "juniPacketMirrorApplicationName": juniPacketMirrorApplicationName,
       "juniPacketMirrorAnalyzerAddress": juniPacketMirrorAnalyzerAddress,
       "juniPacketMirrorUserName": juniPacketMirrorUserName,
       "juniPacketMirrorPolicyName": juniPacketMirrorPolicyName,
       "juniPacketMirrorPolicyId": juniPacketMirrorPolicyId,
       "juniPacketMirrorDateAndTime": juniPacketMirrorDateAndTime,
       "juniPacketMirrorRouterId": juniPacketMirrorRouterId,
       "juniPacketMirrorDirection": juniPacketMirrorDirection,
       "juniPacketMirrorTargetIpAddress": juniPacketMirrorTargetIpAddress,
       "juniPacketMirrorTerminationReason": juniPacketMirrorTerminationReason,
       "juniPacketMirrorConformance": juniPacketMirrorConformance,
       "juniPacketMirrorCompliances": juniPacketMirrorCompliances,
       "juniPacketMirrorCompliance": juniPacketMirrorCompliance,
       "juniPacketMirrorGroups": juniPacketMirrorGroups,
       "juniPacketMirrorNotificationGroup": juniPacketMirrorNotificationGroup,
       "juniPacketMirrorNotificationObjectsGroup": juniPacketMirrorNotificationObjectsGroup,
       "juniPacketMirrorNotificationGroup2": juniPacketMirrorNotificationGroup2,
       "juniPacketMirrorNotificationObjectsGroup2": juniPacketMirrorNotificationObjectsGroup2}
)
