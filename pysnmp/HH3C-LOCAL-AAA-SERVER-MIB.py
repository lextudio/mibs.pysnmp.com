# SNMP MIB module (HH3C-LOCAL-AAA-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LOCAL-AAA-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:50 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cLocAAASvr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141)
)
hh3cLocAAASvr.setRevisions(
        ("2013-07-06 09:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cLocAAASvrControl_ObjectIdentity = ObjectIdentity
hh3cLocAAASvrControl = _Hh3cLocAAASvrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141, 1)
)
_Hh3cLocAAASvrTables_ObjectIdentity = ObjectIdentity
hh3cLocAAASvrTables = _Hh3cLocAAASvrTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141, 2)
)
_Hh3cLocAAASvrTrap_ObjectIdentity = ObjectIdentity
hh3cLocAAASvrTrap = _Hh3cLocAAASvrTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141, 3)
)
_Hh3cLocAAASvrTrapPrex_ObjectIdentity = ObjectIdentity
hh3cLocAAASvrTrapPrex = _Hh3cLocAAASvrTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cLocAAASvrBillExportFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141, 3, 0, 1)
)
if mibBuilder.loadTexts:
    hh3cLocAAASvrBillExportFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LOCAL-AAA-SERVER-MIB",
    **{"hh3cLocAAASvr": hh3cLocAAASvr,
       "hh3cLocAAASvrControl": hh3cLocAAASvrControl,
       "hh3cLocAAASvrTables": hh3cLocAAASvrTables,
       "hh3cLocAAASvrTrap": hh3cLocAAASvrTrap,
       "hh3cLocAAASvrTrapPrex": hh3cLocAAASvrTrapPrex,
       "hh3cLocAAASvrBillExportFailed": hh3cLocAAASvrBillExportFailed}
)
