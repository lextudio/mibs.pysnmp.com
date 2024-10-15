# SNMP MIB module (RBN-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:10 2024
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

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

rbnIfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57)
)
rbnIfMib.setRevisions(
        ("2012-07-18 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnIfMIBObjects_ObjectIdentity = ObjectIdentity
rbnIfMIBObjects = _RbnIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 0)
)
_RbnIfTable_Object = MibTable
rbnIfTable = _RbnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 0, 1)
)
if mibBuilder.loadTexts:
    rbnIfTable.setStatus("current")
_RbnIfEntry_Object = MibTableRow
rbnIfEntry = _RbnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 0, 1, 1)
)
if mibBuilder.loadTexts:
    rbnIfEntry.setStatus("current")
_RbnIfHCInIPv4Octets_Type = Counter64
_RbnIfHCInIPv4Octets_Object = MibTableColumn
rbnIfHCInIPv4Octets = _RbnIfHCInIPv4Octets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 0, 1, 1, 1),
    _RbnIfHCInIPv4Octets_Type()
)
rbnIfHCInIPv4Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIfHCInIPv4Octets.setStatus("current")
_RbnIfHCOutIPv4Octets_Type = Counter64
_RbnIfHCOutIPv4Octets_Object = MibTableColumn
rbnIfHCOutIPv4Octets = _RbnIfHCOutIPv4Octets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 0, 1, 1, 2),
    _RbnIfHCOutIPv4Octets_Type()
)
rbnIfHCOutIPv4Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIfHCOutIPv4Octets.setStatus("current")
_RbnIfHCInIPv4MulticastPkts_Type = Counter64
_RbnIfHCInIPv4MulticastPkts_Object = MibTableColumn
rbnIfHCInIPv4MulticastPkts = _RbnIfHCInIPv4MulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 0, 1, 1, 3),
    _RbnIfHCInIPv4MulticastPkts_Type()
)
rbnIfHCInIPv4MulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIfHCInIPv4MulticastPkts.setStatus("current")
_RbnIfHCOutIPv4MulticastPkts_Type = Counter64
_RbnIfHCOutIPv4MulticastPkts_Object = MibTableColumn
rbnIfHCOutIPv4MulticastPkts = _RbnIfHCOutIPv4MulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 0, 1, 1, 4),
    _RbnIfHCOutIPv4MulticastPkts_Type()
)
rbnIfHCOutIPv4MulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIfHCOutIPv4MulticastPkts.setStatus("current")
_RbnIfHCInIPv6Octets_Type = Counter64
_RbnIfHCInIPv6Octets_Object = MibTableColumn
rbnIfHCInIPv6Octets = _RbnIfHCInIPv6Octets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 0, 1, 1, 5),
    _RbnIfHCInIPv6Octets_Type()
)
rbnIfHCInIPv6Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIfHCInIPv6Octets.setStatus("current")
_RbnIfHCOutIPv6Octets_Type = Counter64
_RbnIfHCOutIPv6Octets_Object = MibTableColumn
rbnIfHCOutIPv6Octets = _RbnIfHCOutIPv6Octets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 0, 1, 1, 6),
    _RbnIfHCOutIPv6Octets_Type()
)
rbnIfHCOutIPv6Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIfHCOutIPv6Octets.setStatus("current")
_RbnIfHCInIPv6MulticastPkts_Type = Counter64
_RbnIfHCInIPv6MulticastPkts_Object = MibTableColumn
rbnIfHCInIPv6MulticastPkts = _RbnIfHCInIPv6MulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 0, 1, 1, 7),
    _RbnIfHCInIPv6MulticastPkts_Type()
)
rbnIfHCInIPv6MulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIfHCInIPv6MulticastPkts.setStatus("current")
_RbnIfHCOutIPv6MulticastPkts_Type = Counter64
_RbnIfHCOutIPv6MulticastPkts_Object = MibTableColumn
rbnIfHCOutIPv6MulticastPkts = _RbnIfHCOutIPv6MulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 0, 1, 1, 8),
    _RbnIfHCOutIPv6MulticastPkts_Type()
)
rbnIfHCOutIPv6MulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnIfHCOutIPv6MulticastPkts.setStatus("current")
_RbnIfMIBConformance_ObjectIdentity = ObjectIdentity
rbnIfMIBConformance = _RbnIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 1)
)
_RbnIfMIBCompliances_ObjectIdentity = ObjectIdentity
rbnIfMIBCompliances = _RbnIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 1, 1)
)
_RbnIfMIBGroups_ObjectIdentity = ObjectIdentity
rbnIfMIBGroups = _RbnIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 1, 2)
)
ifEntry.registerAugmentions(
    ("RBN-IF-MIB",
     "rbnIfEntry")
)
rbnIfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

rbnIfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 1, 2, 1)
)
rbnIfMIBGroup.setObjects(
      *(("RBN-IF-MIB", "rbnIfHCInIPv4Octets"),
        ("RBN-IF-MIB", "rbnIfHCOutIPv4Octets"),
        ("RBN-IF-MIB", "rbnIfHCInIPv4MulticastPkts"),
        ("RBN-IF-MIB", "rbnIfHCOutIPv4MulticastPkts"),
        ("RBN-IF-MIB", "rbnIfHCInIPv6Octets"),
        ("RBN-IF-MIB", "rbnIfHCOutIPv6Octets"),
        ("RBN-IF-MIB", "rbnIfHCInIPv6MulticastPkts"),
        ("RBN-IF-MIB", "rbnIfHCOutIPv6MulticastPkts"))
)
if mibBuilder.loadTexts:
    rbnIfMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 57, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-IF-MIB",
    **{"rbnIfMib": rbnIfMib,
       "rbnIfMIBObjects": rbnIfMIBObjects,
       "rbnIfTable": rbnIfTable,
       "rbnIfEntry": rbnIfEntry,
       "rbnIfHCInIPv4Octets": rbnIfHCInIPv4Octets,
       "rbnIfHCOutIPv4Octets": rbnIfHCOutIPv4Octets,
       "rbnIfHCInIPv4MulticastPkts": rbnIfHCInIPv4MulticastPkts,
       "rbnIfHCOutIPv4MulticastPkts": rbnIfHCOutIPv4MulticastPkts,
       "rbnIfHCInIPv6Octets": rbnIfHCInIPv6Octets,
       "rbnIfHCOutIPv6Octets": rbnIfHCOutIPv6Octets,
       "rbnIfHCInIPv6MulticastPkts": rbnIfHCInIPv6MulticastPkts,
       "rbnIfHCOutIPv6MulticastPkts": rbnIfHCOutIPv6MulticastPkts,
       "rbnIfMIBConformance": rbnIfMIBConformance,
       "rbnIfMIBCompliances": rbnIfMIBCompliances,
       "rbnIfCompliance": rbnIfCompliance,
       "rbnIfMIBGroups": rbnIfMIBGroups,
       "rbnIfMIBGroup": rbnIfMIBGroup}
)
