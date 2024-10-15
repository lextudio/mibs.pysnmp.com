# SNMP MIB module (JUNIPER-JS-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JS-AUTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:14 2024
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

(jnxJsAuth,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsAuth")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxJsAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1)
)
jnxJsAuthMIB.setRevisions(
        ("2007-05-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsAuthNotifications_ObjectIdentity = ObjectIdentity
jnxJsAuthNotifications = _JnxJsAuthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 0)
)
_JnxJsAuthObjects_ObjectIdentity = ObjectIdentity
jnxJsAuthObjects = _JnxJsAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1)
)
_JnxJsFwAuthStats_ObjectIdentity = ObjectIdentity
jnxJsFwAuthStats = _JnxJsFwAuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 1)
)
_JnxJsFwAuthNumPendingUsers_Type = Counter64
_JnxJsFwAuthNumPendingUsers_Object = MibScalar
jnxJsFwAuthNumPendingUsers = _JnxJsFwAuthNumPendingUsers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 1, 1),
    _JnxJsFwAuthNumPendingUsers_Type()
)
jnxJsFwAuthNumPendingUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsFwAuthNumPendingUsers.setStatus("current")
_JnxJsFwAuthNumSuccUsers_Type = Counter64
_JnxJsFwAuthNumSuccUsers_Object = MibScalar
jnxJsFwAuthNumSuccUsers = _JnxJsFwAuthNumSuccUsers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 1, 2),
    _JnxJsFwAuthNumSuccUsers_Type()
)
jnxJsFwAuthNumSuccUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsFwAuthNumSuccUsers.setStatus("current")
_JnxJsFwAuthNumFailedUsers_Type = Counter64
_JnxJsFwAuthNumFailedUsers_Object = MibScalar
jnxJsFwAuthNumFailedUsers = _JnxJsFwAuthNumFailedUsers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 1, 3),
    _JnxJsFwAuthNumFailedUsers_Type()
)
jnxJsFwAuthNumFailedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsFwAuthNumFailedUsers.setStatus("current")
_JnxJsFwAuthTotalUsers_Type = Counter64
_JnxJsFwAuthTotalUsers_Object = MibScalar
jnxJsFwAuthTotalUsers = _JnxJsFwAuthTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 1, 4),
    _JnxJsFwAuthTotalUsers_Type()
)
jnxJsFwAuthTotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsFwAuthTotalUsers.setStatus("current")
_JnxJsAuthTrapVars_ObjectIdentity = ObjectIdentity
jnxJsAuthTrapVars = _JnxJsAuthTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 2)
)
_JnxJsFwAuthUserName_Type = DisplayString
_JnxJsFwAuthUserName_Object = MibScalar
jnxJsFwAuthUserName = _JnxJsFwAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 2, 1),
    _JnxJsFwAuthUserName_Type()
)
jnxJsFwAuthUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsFwAuthUserName.setStatus("current")
_JnxJsFwAuthServiceDesc_Type = DisplayString
_JnxJsFwAuthServiceDesc_Object = MibScalar
jnxJsFwAuthServiceDesc = _JnxJsFwAuthServiceDesc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 2, 2),
    _JnxJsFwAuthServiceDesc_Type()
)
jnxJsFwAuthServiceDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsFwAuthServiceDesc.setStatus("current")
_JnxJsFwAuthReason_Type = DisplayString
_JnxJsFwAuthReason_Object = MibScalar
jnxJsFwAuthReason = _JnxJsFwAuthReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 2, 3),
    _JnxJsFwAuthReason_Type()
)
jnxJsFwAuthReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsFwAuthReason.setStatus("current")
_JnxJsFwAuthClientIpAddr_Type = IpAddress
_JnxJsFwAuthClientIpAddr_Object = MibScalar
jnxJsFwAuthClientIpAddr = _JnxJsFwAuthClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 1, 2, 4),
    _JnxJsFwAuthClientIpAddr_Type()
)
jnxJsFwAuthClientIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsFwAuthClientIpAddr.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJsFwAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 0, 1)
)
jnxJsFwAuthFailure.setObjects(
      *(("JUNIPER-JS-AUTH-MIB", "jnxJsFwAuthUserName"),
        ("JUNIPER-JS-AUTH-MIB", "jnxJsFwAuthClientIpAddr"),
        ("JUNIPER-JS-AUTH-MIB", "jnxJsFwAuthServiceDesc"),
        ("JUNIPER-JS-AUTH-MIB", "jnxJsFwAuthReason"))
)
if mibBuilder.loadTexts:
    jnxJsFwAuthFailure.setStatus(
        "current"
    )

jnxJsFwAuthServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 0, 2)
)
if mibBuilder.loadTexts:
    jnxJsFwAuthServiceUp.setStatus(
        "current"
    )

jnxJsFwAuthServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 0, 3)
)
if mibBuilder.loadTexts:
    jnxJsFwAuthServiceDown.setStatus(
        "current"
    )

jnxJsFwAuthCapacityExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2, 1, 0, 4)
)
if mibBuilder.loadTexts:
    jnxJsFwAuthCapacityExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-AUTH-MIB",
    **{"jnxJsAuthMIB": jnxJsAuthMIB,
       "jnxJsAuthNotifications": jnxJsAuthNotifications,
       "jnxJsFwAuthFailure": jnxJsFwAuthFailure,
       "jnxJsFwAuthServiceUp": jnxJsFwAuthServiceUp,
       "jnxJsFwAuthServiceDown": jnxJsFwAuthServiceDown,
       "jnxJsFwAuthCapacityExceeded": jnxJsFwAuthCapacityExceeded,
       "jnxJsAuthObjects": jnxJsAuthObjects,
       "jnxJsFwAuthStats": jnxJsFwAuthStats,
       "jnxJsFwAuthNumPendingUsers": jnxJsFwAuthNumPendingUsers,
       "jnxJsFwAuthNumSuccUsers": jnxJsFwAuthNumSuccUsers,
       "jnxJsFwAuthNumFailedUsers": jnxJsFwAuthNumFailedUsers,
       "jnxJsFwAuthTotalUsers": jnxJsFwAuthTotalUsers,
       "jnxJsAuthTrapVars": jnxJsAuthTrapVars,
       "jnxJsFwAuthUserName": jnxJsFwAuthUserName,
       "jnxJsFwAuthServiceDesc": jnxJsFwAuthServiceDesc,
       "jnxJsFwAuthReason": jnxJsFwAuthReason,
       "jnxJsFwAuthClientIpAddr": jnxJsFwAuthClientIpAddr}
)
