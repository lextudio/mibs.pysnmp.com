# SNMP MIB module (LEGATO-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEGATO-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:48 2024
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
 NotificationType,
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
    "NotificationType",
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LegatoSoftware_ObjectIdentity = ObjectIdentity
legatoSoftware = _LegatoSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1676)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1676, 1)
)
_LegatoCluster_ObjectIdentity = ObjectIdentity
legatoCluster = _LegatoCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1676, 1, 4)
)
_ClusterMessage_ObjectIdentity = ObjectIdentity
clusterMessage = _ClusterMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1676, 1, 4, 1)
)


class _TrapSeverity_Type(Integer32):
    """Custom type trapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("info", 1),
          ("severe", 3),
          ("warning", 2))
    )


_TrapSeverity_Type.__name__ = "Integer32"
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1676, 1, 4, 1, 1),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("mandatory")


class _TrapText_Type(DisplayString):
    """Custom type trapText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapText_Type.__name__ = "DisplayString"
_TrapText_Object = MibScalar
trapText = _TrapText_Object(
    (1, 3, 6, 1, 4, 1, 1676, 1, 4, 1, 2),
    _TrapText_Type()
)
trapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapText.setStatus("mandatory")

# Managed Objects groups


# Notification objects

legatoClusterUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1676, 1, 4, 0, 1)
)
legatoClusterUserTrap.setObjects(
      *(("LEGATO-CLUSTER-MIB", "trapText"),
        ("LEGATO-CLUSTER-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    legatoClusterUserTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEGATO-CLUSTER-MIB",
    **{"DisplayString": DisplayString,
       "legatoSoftware": legatoSoftware,
       "products": products,
       "legatoCluster": legatoCluster,
       "legatoClusterUserTrap": legatoClusterUserTrap,
       "clusterMessage": clusterMessage,
       "trapSeverity": trapSeverity,
       "trapText": trapText}
)
