# SNMP MIB module (NETASQ-AUTHUSERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETASQ-AUTHUSERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:30 2024
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

(ntqUsers,) = mibBuilder.importSymbols(
    "NETASQ-SMI-MIB",
    "ntqUsers")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

_NtqAuthUsersTable_Object = MibTable
ntqAuthUsersTable = _NtqAuthUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ntqAuthUsersTable.setStatus("current")
_NtqAuthUsersEntry_Object = MibTableRow
ntqAuthUsersEntry = _NtqAuthUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1)
)
ntqAuthUsersEntry.setIndexNames(
    (0, "NETASQ-AUTHUSERS-MIB", "ntqAuthUsersIPAddr"),
)
if mibBuilder.loadTexts:
    ntqAuthUsersEntry.setStatus("current")
_NtqAuthUsersIPAddr_Type = DisplayString
_NtqAuthUsersIPAddr_Object = MibTableColumn
ntqAuthUsersIPAddr = _NtqAuthUsersIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 1),
    _NtqAuthUsersIPAddr_Type()
)
ntqAuthUsersIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAuthUsersIPAddr.setStatus("current")
_NtqAuthUsersTimeOut_Type = Integer32
_NtqAuthUsersTimeOut_Object = MibTableColumn
ntqAuthUsersTimeOut = _NtqAuthUsersTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 2),
    _NtqAuthUsersTimeOut_Type()
)
ntqAuthUsersTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAuthUsersTimeOut.setStatus("current")
_NtqAuthUsersName_Type = SnmpAdminString
_NtqAuthUsersName_Object = MibTableColumn
ntqAuthUsersName = _NtqAuthUsersName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 3),
    _NtqAuthUsersName_Type()
)
ntqAuthUsersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqAuthUsersName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETASQ-AUTHUSERS-MIB",
    **{"ntqAuthUsersTable": ntqAuthUsersTable,
       "ntqAuthUsersEntry": ntqAuthUsersEntry,
       "ntqAuthUsersIPAddr": ntqAuthUsersIPAddr,
       "ntqAuthUsersTimeOut": ntqAuthUsersTimeOut,
       "ntqAuthUsersName": ntqAuthUsersName}
)
