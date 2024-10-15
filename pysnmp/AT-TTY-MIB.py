# SNMP MIB module (AT-TTY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-TTY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:36 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

tty = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36)
)
tty.setRevisions(
        ("2006-06-28 12:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TtyTraps_ObjectIdentity = ObjectIdentity
ttyTraps = _TtyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100)
)
_LoginFailureUser_Type = DisplayString
_LoginFailureUser_Object = MibScalar
loginFailureUser = _LoginFailureUser_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 1),
    _LoginFailureUser_Type()
)
loginFailureUser.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loginFailureUser.setStatus("current")
_LoginFailureIPAddress_Type = IpAddress
_LoginFailureIPAddress_Object = MibScalar
loginFailureIPAddress = _LoginFailureIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 2),
    _LoginFailureIPAddress_Type()
)
loginFailureIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loginFailureIPAddress.setStatus("current")
_LoginFailureAttempts_Type = Integer32
_LoginFailureAttempts_Object = MibScalar
loginFailureAttempts = _LoginFailureAttempts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 3),
    _LoginFailureAttempts_Type()
)
loginFailureAttempts.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loginFailureAttempts.setStatus("current")

# Managed Objects groups


# Notification objects

loginFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 36, 100, 11)
)
loginFailureTrap.setObjects(
      *(("AT-TTY-MIB", "loginFailureUser"),
        ("AT-TTY-MIB", "loginFailureIPAddress"),
        ("AT-TTY-MIB", "loginFailureAttempts"))
)
if mibBuilder.loadTexts:
    loginFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-TTY-MIB",
    **{"tty": tty,
       "ttyTraps": ttyTraps,
       "loginFailureUser": loginFailureUser,
       "loginFailureIPAddress": loginFailureIPAddress,
       "loginFailureAttempts": loginFailureAttempts,
       "loginFailureTrap": loginFailureTrap}
)
