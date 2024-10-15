# SNMP MIB module (JUNIPER-MAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:42 2024
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

(jnxMagMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMagMibRoot")

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

jnxMagMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1)
)
jnxMagMib.setRevisions(
        ("2010-02-20 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMagNotifications_ObjectIdentity = ObjectIdentity
jnxMagNotifications = _JnxMagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 0)
)
_JnxMagObjects_ObjectIdentity = ObjectIdentity
jnxMagObjects = _JnxMagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1)
)
_JnxMagSSOObjects_ObjectIdentity = ObjectIdentity
jnxMagSSOObjects = _JnxMagSSOObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1)
)
_JnxMagSSOAuthTokenAttempt_Type = Counter32
_JnxMagSSOAuthTokenAttempt_Object = MibScalar
jnxMagSSOAuthTokenAttempt = _JnxMagSSOAuthTokenAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1, 1),
    _JnxMagSSOAuthTokenAttempt_Type()
)
jnxMagSSOAuthTokenAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMagSSOAuthTokenAttempt.setStatus("current")
_JnxMagSSOFailedAuthToken_Type = Counter32
_JnxMagSSOFailedAuthToken_Object = MibScalar
jnxMagSSOFailedAuthToken = _JnxMagSSOFailedAuthToken_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1, 2),
    _JnxMagSSOFailedAuthToken_Type()
)
jnxMagSSOFailedAuthToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMagSSOFailedAuthToken.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMagSSOValidationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 0, 1)
)
if mibBuilder.loadTexts:
    jnxMagSSOValidationError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MAG-MIB",
    **{"jnxMagMib": jnxMagMib,
       "jnxMagNotifications": jnxMagNotifications,
       "jnxMagSSOValidationError": jnxMagSSOValidationError,
       "jnxMagObjects": jnxMagObjects,
       "jnxMagSSOObjects": jnxMagSSOObjects,
       "jnxMagSSOAuthTokenAttempt": jnxMagSSOAuthTokenAttempt,
       "jnxMagSSOFailedAuthToken": jnxMagSSOFailedAuthToken}
)
