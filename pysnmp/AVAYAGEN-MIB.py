# SNMP MIB module (AVAYAGEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYAGEN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:29 2024
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

avaya = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889)
)
avaya.setRevisions(
        ("1909-12-19 10:00",
         "1904-01-27 09:00",
         "1902-08-15 09:00",
         "1902-07-28 09:00",
         "1901-08-09 17:00",
         "1901-06-21 11:55",
         "1900-10-15 10:45",
         "1900-10-15 13:05")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AvayaProducts_ObjectIdentity = ObjectIdentity
avayaProducts = _AvayaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1)
)
_AvGatewayProducts_ObjectIdentity = ObjectIdentity
avGatewayProducts = _AvGatewayProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 6)
)
_AvayaMibs_ObjectIdentity = ObjectIdentity
avayaMibs = _AvayaMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2)
)
_Lsg_ObjectIdentity = ObjectIdentity
lsg = _Lsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1)
)
_AvayaEISTopology_ObjectIdentity = ObjectIdentity
avayaEISTopology = _AvayaEISTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 10)
)
_AvayaSystemStats_ObjectIdentity = ObjectIdentity
avayaSystemStats = _AvayaSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 11)
)
_AvGatewayMibs_ObjectIdentity = ObjectIdentity
avGatewayMibs = _AvGatewayMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYAGEN-MIB",
    **{"avaya": avaya,
       "avayaProducts": avayaProducts,
       "avGatewayProducts": avGatewayProducts,
       "avayaMibs": avayaMibs,
       "lsg": lsg,
       "avayaEISTopology": avayaEISTopology,
       "avayaSystemStats": avayaSystemStats,
       "avGatewayMibs": avGatewayMibs}
)
