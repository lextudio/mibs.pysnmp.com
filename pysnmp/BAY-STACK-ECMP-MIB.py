# SNMP MIB module (BAY-STACK-ECMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-ECMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:55 2024
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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackEcmpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 15)
)
bayStackEcmpMib.setRevisions(
        ("2012-06-01 00:00",
         "2005-09-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsEcmpNotifications_ObjectIdentity = ObjectIdentity
bsEcmpNotifications = _BsEcmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 15, 0)
)
_BsEcmpObjects_ObjectIdentity = ObjectIdentity
bsEcmpObjects = _BsEcmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 15, 1)
)
_BsEcmpScalars_ObjectIdentity = ObjectIdentity
bsEcmpScalars = _BsEcmpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 1)
)
_BsEcmpConfigTable_Object = MibTable
bsEcmpConfigTable = _BsEcmpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2)
)
if mibBuilder.loadTexts:
    bsEcmpConfigTable.setStatus("current")
_BsEcmpConfigEntry_Object = MibTableRow
bsEcmpConfigEntry = _BsEcmpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1)
)
bsEcmpConfigEntry.setIndexNames(
    (0, "BAY-STACK-ECMP-MIB", "bsEcmpConfigRoutingProtocol"),
)
if mibBuilder.loadTexts:
    bsEcmpConfigEntry.setStatus("current")


class _BsEcmpConfigRoutingProtocol_Type(Integer32):
    """Custom type bsEcmpConfigRoutingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 4),
          ("ospf", 3),
          ("rip", 2),
          ("static", 1))
    )


_BsEcmpConfigRoutingProtocol_Type.__name__ = "Integer32"
_BsEcmpConfigRoutingProtocol_Object = MibTableColumn
bsEcmpConfigRoutingProtocol = _BsEcmpConfigRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1, 1),
    _BsEcmpConfigRoutingProtocol_Type()
)
bsEcmpConfigRoutingProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsEcmpConfigRoutingProtocol.setStatus("current")


class _BsEcmpConfigMaxPath_Type(Integer32):
    """Custom type bsEcmpConfigMaxPath based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BsEcmpConfigMaxPath_Type.__name__ = "Integer32"
_BsEcmpConfigMaxPath_Object = MibTableColumn
bsEcmpConfigMaxPath = _BsEcmpConfigMaxPath_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1, 2),
    _BsEcmpConfigMaxPath_Type()
)
bsEcmpConfigMaxPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsEcmpConfigMaxPath.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-ECMP-MIB",
    **{"bayStackEcmpMib": bayStackEcmpMib,
       "bsEcmpNotifications": bsEcmpNotifications,
       "bsEcmpObjects": bsEcmpObjects,
       "bsEcmpScalars": bsEcmpScalars,
       "bsEcmpConfigTable": bsEcmpConfigTable,
       "bsEcmpConfigEntry": bsEcmpConfigEntry,
       "bsEcmpConfigRoutingProtocol": bsEcmpConfigRoutingProtocol,
       "bsEcmpConfigMaxPath": bsEcmpConfigMaxPath}
)
