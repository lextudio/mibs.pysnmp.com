# SNMP MIB module (NETASQ-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETASQ-SMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:29 2024
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
 enterprises,
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
    "enterprises",
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

_Netasq_ObjectIdentity = ObjectIdentity
netasq = _Netasq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256)
)
_NetasqMIB_ObjectIdentity = ObjectIdentity
netasqMIB = _NetasqMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1)
)
_NtqProductProperty_ObjectIdentity = ObjectIdentity
ntqProductProperty = _NtqProductProperty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 0)
)
_NtqVPN_ObjectIdentity = ObjectIdentity
ntqVPN = _NtqVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1)
)
_NtqUsers_ObjectIdentity = ObjectIdentity
ntqUsers = _NtqUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2)
)
_NtqHosts_ObjectIdentity = ObjectIdentity
ntqHosts = _NtqHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3)
)
_Ntqif_ObjectIdentity = ObjectIdentity
ntqif = _Ntqif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4)
)
_NtqAlarm_ObjectIdentity = ObjectIdentity
ntqAlarm = _NtqAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 5)
)
_NtqNotifications_ObjectIdentity = ObjectIdentity
ntqNotifications = _NtqNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETASQ-SMI-MIB",
    **{"netasq": netasq,
       "netasqMIB": netasqMIB,
       "ntqProductProperty": ntqProductProperty,
       "ntqVPN": ntqVPN,
       "ntqUsers": ntqUsers,
       "ntqHosts": ntqHosts,
       "ntqif": ntqif,
       "ntqAlarm": ntqAlarm,
       "ntqNotifications": ntqNotifications}
)
