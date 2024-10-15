# SNMP MIB module (NETBOTZ-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETBOTZ-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:39 2024
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

(netBotz_snmp,) = mibBuilder.importSymbols(
    "NETBOTZ-MIB",
    "netBotz-snmp")

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

_NetBotz_snmp_traptarget_Type = IpAddress
_NetBotz_snmp_traptarget_Object = MibScalar
netBotz_snmp_traptarget = _NetBotz_snmp_traptarget_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 1),
    _NetBotz_snmp_traptarget_Type()
)
netBotz_snmp_traptarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_snmp_traptarget.setStatus("mandatory")
_NetBotz_snmp_community_Type = DisplayString
_NetBotz_snmp_community_Object = MibScalar
netBotz_snmp_community = _NetBotz_snmp_community_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 2),
    _NetBotz_snmp_community_Type()
)
netBotz_snmp_community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_snmp_community.setStatus("mandatory")
_NetBotz_snmp_timeout_Type = Integer32
_NetBotz_snmp_timeout_Object = MibScalar
netBotz_snmp_timeout = _NetBotz_snmp_timeout_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 3),
    _NetBotz_snmp_timeout_Type()
)
netBotz_snmp_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_snmp_timeout.setStatus("mandatory")
_NetBotz_snmp_retries_Type = Integer32
_NetBotz_snmp_retries_Object = MibScalar
netBotz_snmp_retries = _NetBotz_snmp_retries_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 4),
    _NetBotz_snmp_retries_Type()
)
netBotz_snmp_retries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_snmp_retries.setStatus("mandatory")
_NetBotz_userid_1_Type = DisplayString
_NetBotz_userid_1_Object = MibScalar
netBotz_userid_1 = _NetBotz_userid_1_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 5),
    _NetBotz_userid_1_Type()
)
netBotz_userid_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_userid_1.setStatus("mandatory")
_NetBotz_password_1_Type = DisplayString
_NetBotz_password_1_Object = MibScalar
netBotz_password_1 = _NetBotz_password_1_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 6),
    _NetBotz_password_1_Type()
)
netBotz_password_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_password_1.setStatus("mandatory")
_NetBotz_userid_2_Type = DisplayString
_NetBotz_userid_2_Object = MibScalar
netBotz_userid_2 = _NetBotz_userid_2_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 7),
    _NetBotz_userid_2_Type()
)
netBotz_userid_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_userid_2.setStatus("mandatory")
_NetBotz_password_2_Type = DisplayString
_NetBotz_password_2_Object = MibScalar
netBotz_password_2 = _NetBotz_password_2_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 8),
    _NetBotz_password_2_Type()
)
netBotz_password_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_password_2.setStatus("mandatory")
_NetBotz_userid_3_Type = DisplayString
_NetBotz_userid_3_Object = MibScalar
netBotz_userid_3 = _NetBotz_userid_3_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 9),
    _NetBotz_userid_3_Type()
)
netBotz_userid_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_userid_3.setStatus("mandatory")
_NetBotz_password_3_Type = DisplayString
_NetBotz_password_3_Object = MibScalar
netBotz_password_3 = _NetBotz_password_3_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 10),
    _NetBotz_password_3_Type()
)
netBotz_password_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_password_3.setStatus("mandatory")
_NetBotz_snmp_traptarget2_Type = IpAddress
_NetBotz_snmp_traptarget2_Object = MibScalar
netBotz_snmp_traptarget2 = _NetBotz_snmp_traptarget2_Object(
    (1, 3, 6, 1, 4, 1, 5528, 40, 11),
    _NetBotz_snmp_traptarget2_Type()
)
netBotz_snmp_traptarget2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_snmp_traptarget2.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETBOTZ-SNMP-MIB",
    **{"netBotz-snmp-traptarget": netBotz_snmp_traptarget,
       "netBotz-snmp-community": netBotz_snmp_community,
       "netBotz-snmp-timeout": netBotz_snmp_timeout,
       "netBotz-snmp-retries": netBotz_snmp_retries,
       "netBotz-userid-1": netBotz_userid_1,
       "netBotz-password-1": netBotz_password_1,
       "netBotz-userid-2": netBotz_userid_2,
       "netBotz-password-2": netBotz_password_2,
       "netBotz-userid-3": netBotz_userid_3,
       "netBotz-password-3": netBotz_password_3,
       "netBotz-snmp-traptarget2": netBotz_snmp_traptarget2}
)
