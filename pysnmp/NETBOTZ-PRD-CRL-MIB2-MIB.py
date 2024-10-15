# SNMP MIB module (NETBOTZ-PRD-CRL-MIB2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETBOTZ-PRD-CRL-MIB2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:37 2024
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

(netBotz_prd_crawlers,) = mibBuilder.importSymbols(
    "NETBOTZ-PRODUCTS-MIB",
    "netBotz-prd-crawlers")

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

_Netbotz_crawlers_ObjectIdentity = ObjectIdentity
netbotz_crawlers = _Netbotz_crawlers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528)
)
_NetBotz_prd_crl_mib2_ObjectIdentity = ObjectIdentity
netBotz_prd_crl_mib2 = _NetBotz_prd_crl_mib2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1)
)
_NetBotz_prd_crl_mib2_ping_Type = Integer32
_NetBotz_prd_crl_mib2_ping_Object = MibScalar
netBotz_prd_crl_mib2_ping = _NetBotz_prd_crl_mib2_ping_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 3),
    _NetBotz_prd_crl_mib2_ping_Type()
)
netBotz_prd_crl_mib2_ping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_mib2_ping.setStatus("mandatory")
_NetBotz_prd_crl_mib2_uptime_Type = TimeTicks
_NetBotz_prd_crl_mib2_uptime_Object = MibScalar
netBotz_prd_crl_mib2_uptime = _NetBotz_prd_crl_mib2_uptime_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 8),
    _NetBotz_prd_crl_mib2_uptime_Type()
)
netBotz_prd_crl_mib2_uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_mib2_uptime.setStatus("mandatory")
_NetBotz_prd_crl_mib2_snmpstatus_Type = DisplayString
_NetBotz_prd_crl_mib2_snmpstatus_Object = MibScalar
netBotz_prd_crl_mib2_snmpstatus = _NetBotz_prd_crl_mib2_snmpstatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 9),
    _NetBotz_prd_crl_mib2_snmpstatus_Type()
)
netBotz_prd_crl_mib2_snmpstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_mib2_snmpstatus.setStatus("mandatory")
_NetBotz_prd_crl_mib2if_ObjectIdentity = ObjectIdentity
netBotz_prd_crl_mib2if = _NetBotz_prd_crl_mib2if_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2)
)
_NetBotz_prd_crl_mib2if_opstatus_Type = Integer32
_NetBotz_prd_crl_mib2if_opstatus_Object = MibScalar
netBotz_prd_crl_mib2if_opstatus = _NetBotz_prd_crl_mib2if_opstatus_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2, 6),
    _NetBotz_prd_crl_mib2if_opstatus_Type()
)
netBotz_prd_crl_mib2if_opstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_mib2if_opstatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETBOTZ-PRD-CRL-MIB2-MIB",
    **{"netbotz-crawlers": netbotz_crawlers,
       "netBotz-prd-crl-mib2": netBotz_prd_crl_mib2,
       "netBotz-prd-crl-mib2-ping": netBotz_prd_crl_mib2_ping,
       "netBotz-prd-crl-mib2-uptime": netBotz_prd_crl_mib2_uptime,
       "netBotz-prd-crl-mib2-snmpstatus": netBotz_prd_crl_mib2_snmpstatus,
       "netBotz-prd-crl-mib2if": netBotz_prd_crl_mib2if,
       "netBotz-prd-crl-mib2if-opstatus": netBotz_prd_crl_mib2if_opstatus}
)
