# SNMP MIB module (NETBOTZ-PRD-CRL-MIB2TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETBOTZ-PRD-CRL-MIB2TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:38 2024
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

(netBotz_ismetric,) = mibBuilder.importSymbols(
    "NETBOTZ-DEVICE-MIB",
    "netBotz-ismetric")

(netBotz_prd_crl_mib2_ping,
 netBotz_prd_crl_mib2_snmpstatus,
 netBotz_prd_crl_mib2_uptime,
 netBotz_prd_crl_mib2if_opstatus) = mibBuilder.importSymbols(
    "NETBOTZ-PRD-CRL-MIB2-MIB",
    "netBotz-prd-crl-mib2-ping",
    "netBotz-prd-crl-mib2-snmpstatus",
    "netBotz-prd-crl-mib2-uptime",
    "netBotz-prd-crl-mib2if-opstatus")

(netBotz_prd_crltrap,) = mibBuilder.importSymbols(
    "NETBOTZ-PRODUCTS-MIB",
    "netBotz-prd-crltrap")

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
 NotificationType,
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
    "NotificationType",
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

_NetBotz_prd_crl_trap_index_Type = Integer32
_NetBotz_prd_crl_trap_index_Object = MibScalar
netBotz_prd_crl_trap_index = _NetBotz_prd_crl_trap_index_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 20),
    _NetBotz_prd_crl_trap_index_Type()
)
netBotz_prd_crl_trap_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_index.setStatus("mandatory")
_NetBotz_prd_crl_trap_address_Type = IpAddress
_NetBotz_prd_crl_trap_address_Object = MibScalar
netBotz_prd_crl_trap_address = _NetBotz_prd_crl_trap_address_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 21),
    _NetBotz_prd_crl_trap_address_Type()
)
netBotz_prd_crl_trap_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_address.setStatus("mandatory")
_NetBotz_prd_crl_trap_oid_Type = ObjectIdentifier
_NetBotz_prd_crl_trap_oid_Object = MibScalar
netBotz_prd_crl_trap_oid = _NetBotz_prd_crl_trap_oid_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 22),
    _NetBotz_prd_crl_trap_oid_Type()
)
netBotz_prd_crl_trap_oid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_oid.setStatus("mandatory")
_NetBotz_prd_crl_trap_botoid_Type = ObjectIdentifier
_NetBotz_prd_crl_trap_botoid_Object = MibScalar
netBotz_prd_crl_trap_botoid = _NetBotz_prd_crl_trap_botoid_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 23),
    _NetBotz_prd_crl_trap_botoid_Type()
)
netBotz_prd_crl_trap_botoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_botoid.setStatus("mandatory")
_NetBotz_prd_crl_trap_value_Type = Integer32
_NetBotz_prd_crl_trap_value_Object = MibScalar
netBotz_prd_crl_trap_value = _NetBotz_prd_crl_trap_value_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 24),
    _NetBotz_prd_crl_trap_value_Type()
)
netBotz_prd_crl_trap_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_value.setStatus("mandatory")
_NetBotz_prd_crl_trap_date_Type = Integer32
_NetBotz_prd_crl_trap_date_Object = MibScalar
netBotz_prd_crl_trap_date = _NetBotz_prd_crl_trap_date_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 25),
    _NetBotz_prd_crl_trap_date_Type()
)
netBotz_prd_crl_trap_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_date.setStatus("mandatory")
_NetBotz_prd_crl_trap_attrib_Type = Integer32
_NetBotz_prd_crl_trap_attrib_Object = MibScalar
netBotz_prd_crl_trap_attrib = _NetBotz_prd_crl_trap_attrib_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 26),
    _NetBotz_prd_crl_trap_attrib_Type()
)
netBotz_prd_crl_trap_attrib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_attrib.setStatus("mandatory")
_NetBotz_prd_crl_trap_desc_Type = DisplayString
_NetBotz_prd_crl_trap_desc_Object = MibScalar
netBotz_prd_crl_trap_desc = _NetBotz_prd_crl_trap_desc_Object(
    (1, 3, 6, 1, 4, 1, 5528, 30, 21, 27),
    _NetBotz_prd_crl_trap_desc_Type()
)
netBotz_prd_crl_trap_desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_prd_crl_trap_desc.setStatus("mandatory")

# Managed Objects groups


# Notification objects

netBotz_prd_crl_ping_offline_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 3, 0, 4)
)
netBotz_prd_crl_ping_offline_trap.setObjects(
      *(("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_ping_offline_trap.setStatus(
        ""
    )

netBotz_prd_crl_ping_online_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 3, 0, 5)
)
netBotz_prd_crl_ping_online_trap.setObjects(
      *(("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_ping_online_trap.setStatus(
        ""
    )

netBotz_prd_crl_uptime_online_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 8, 0, 5)
)
netBotz_prd_crl_uptime_online_trap.setObjects(
      *(("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_uptime_online_trap.setStatus(
        ""
    )

netBotz_prd_crl_snmp_offline_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 9, 0, 4)
)
netBotz_prd_crl_snmp_offline_trap.setObjects(
      *(("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_snmp_offline_trap.setStatus(
        ""
    )

netBotz_prd_crl_snmp_online_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 1, 9, 0, 5)
)
netBotz_prd_crl_snmp_online_trap.setObjects(
      *(("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_snmp_online_trap.setStatus(
        ""
    )

netBotz_prd_crl_opstatus_mismatch_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2, 6, 0, 1)
)
netBotz_prd_crl_opstatus_mismatch_trap.setObjects(
      *(("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_opstatus_mismatch_trap.setStatus(
        ""
    )

netBotz_prd_crl_opstatus_match_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2, 6, 0, 2)
)
netBotz_prd_crl_opstatus_match_trap.setObjects(
      *(("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_opstatus_match_trap.setStatus(
        ""
    )

netBotz_prd_crl_opstatus_offline_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5528, 30, 20, 5528, 2, 6, 0, 4)
)
netBotz_prd_crl_opstatus_offline_trap.setObjects(
      *(("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_index"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_address"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_oid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_botoid"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_value"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_date"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_attrib"),
        ("NETBOTZ-PRD-CRL-MIB2TRAP-MIB", "netBotz_prd_crl_trap_desc"),
        ("NETBOTZ-DEVICE-MIB", "netBotz_ismetric"))
)
if mibBuilder.loadTexts:
    netBotz_prd_crl_opstatus_offline_trap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETBOTZ-PRD-CRL-MIB2TRAP-MIB",
    **{"netBotz-prd-crl-ping-offline-trap": netBotz_prd_crl_ping_offline_trap,
       "netBotz-prd-crl-ping-online-trap": netBotz_prd_crl_ping_online_trap,
       "netBotz-prd-crl-uptime-online-trap": netBotz_prd_crl_uptime_online_trap,
       "netBotz-prd-crl-snmp-offline-trap": netBotz_prd_crl_snmp_offline_trap,
       "netBotz-prd-crl-snmp-online-trap": netBotz_prd_crl_snmp_online_trap,
       "netBotz-prd-crl-opstatus-mismatch-trap": netBotz_prd_crl_opstatus_mismatch_trap,
       "netBotz-prd-crl-opstatus-match-trap": netBotz_prd_crl_opstatus_match_trap,
       "netBotz-prd-crl-opstatus-offline-trap": netBotz_prd_crl_opstatus_offline_trap,
       "netBotz-prd-crl-trap-index": netBotz_prd_crl_trap_index,
       "netBotz-prd-crl-trap-address": netBotz_prd_crl_trap_address,
       "netBotz-prd-crl-trap-oid": netBotz_prd_crl_trap_oid,
       "netBotz-prd-crl-trap-botoid": netBotz_prd_crl_trap_botoid,
       "netBotz-prd-crl-trap-value": netBotz_prd_crl_trap_value,
       "netBotz-prd-crl-trap-date": netBotz_prd_crl_trap_date,
       "netBotz-prd-crl-trap-attrib": netBotz_prd_crl_trap_attrib,
       "netBotz-prd-crl-trap-desc": netBotz_prd_crl_trap_desc}
)
