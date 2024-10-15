# SNMP MIB module (SCC-ENTERPRISE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCC-ENTERPRISE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:58 2024
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

_Scc_ObjectIdentity = ObjectIdentity
scc = _Scc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386)
)
_SccProducts_ObjectIdentity = ObjectIdentity
sccProducts = _SccProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 1)
)
_SccRaid7_ObjectIdentity = ObjectIdentity
sccRaid7 = _SccRaid7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 1, 1)
)
_SccMibs_ObjectIdentity = ObjectIdentity
sccMibs = _SccMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 2)
)
_Raid7mib_ObjectIdentity = ObjectIdentity
raid7mib = _Raid7mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1)
)
_Raid7proxy_ObjectIdentity = ObjectIdentity
raid7proxy = _Raid7proxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCC-ENTERPRISE-MIB",
    **{"scc": scc,
       "sccProducts": sccProducts,
       "sccRaid7": sccRaid7,
       "sccMibs": sccMibs,
       "raid7mib": raid7mib,
       "raid7proxy": raid7proxy}
)
