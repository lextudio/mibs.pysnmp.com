# SNMP MIB module (ATEN-PRODUCTS-PUB-TRAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATEN-PRODUCTS-PUB-TRAP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:41 2024
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

(public,) = mibBuilder.importSymbols(
    "ATEN-PRODUCTS-MIB",
    "public")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 1, 3)
)
_Email_Type = DisplayString
_Email_Object = MibScalar
email = _Email_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 1),
    _Email_Type()
)
email.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    email.setStatus("current")
_Log_Type = DisplayString
_Log_Object = MibScalar
log = _Log_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 2),
    _Log_Type()
)
log.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log.setStatus("current")
_Login_Type = DisplayString
_Login_Object = MibScalar
login = _Login_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 3),
    _Login_Type()
)
login.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    login.setStatus("current")
_Logout_Type = DisplayString
_Logout_Object = MibScalar
logout = _Logout_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 1, 3, 4),
    _Logout_Type()
)
logout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATEN-PRODUCTS-PUB-TRAP",
    **{"trap": trap,
       "email": email,
       "log": log,
       "login": login,
       "logout": logout}
)
