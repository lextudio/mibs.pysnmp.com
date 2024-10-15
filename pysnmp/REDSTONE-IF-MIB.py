# SNMP MIB module (REDSTONE-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:33 2024
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

(ifEntry,
 ifStackHigherLayer,
 ifStackLowerLayer) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifStackHigherLayer",
    "ifStackLowerLayer")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rsIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3)
)
rsIfMIB.setRevisions(
        ("1998-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RsIfType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 10),
          ("atm", 9),
          ("atmSubInterface", 11),
          ("ds0", 2),
          ("ds1", 3),
          ("ds3", 4),
          ("ethernet", 6),
          ("frSubInterface", 16),
          ("frameRelay", 5),
          ("ft1", 12),
          ("hdlc", 13),
          ("ip", 0),
          ("ipLoopback", 14),
          ("ipVirtual", 15),
          ("ppp", 1),
          ("pppoe", 17),
          ("pppoeSubInterface", 18),
          ("sonet", 7),
          ("sonetPath", 8))
    )



# MIB Managed Objects in the order of their OIDs

_RsInterfaces_ObjectIdentity = ObjectIdentity
rsInterfaces = _RsInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1)
)
_RsIf_ObjectIdentity = ObjectIdentity
rsIf = _RsIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1)
)
_RsIfObjects_ObjectIdentity = ObjectIdentity
rsIfObjects = _RsIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1)
)
_RsIfTable_Object = MibTable
rsIfTable = _RsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsIfTable.setStatus("current")
_RsIfEntry_Object = MibTableRow
rsIfEntry = _RsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsIfEntry.setStatus("current")
_RsIfType_Type = RsIfType
_RsIfType_Object = MibTableColumn
rsIfType = _RsIfType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 1, 1, 1),
    _RsIfType_Type()
)
rsIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfType.setStatus("current")
_RsIfInvStackTable_Object = MibTable
rsIfInvStackTable = _RsIfInvStackTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rsIfInvStackTable.setStatus("current")
_RsIfInvStackEntry_Object = MibTableRow
rsIfInvStackEntry = _RsIfInvStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 2, 1)
)
rsIfInvStackEntry.setIndexNames(
    (0, "IF-MIB", "ifStackLowerLayer"),
    (0, "IF-MIB", "ifStackHigherLayer"),
)
if mibBuilder.loadTexts:
    rsIfInvStackEntry.setStatus("current")
_RsIfInvStackStatus_Type = RowStatus
_RsIfInvStackStatus_Object = MibTableColumn
rsIfInvStackStatus = _RsIfInvStackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 1, 2, 1, 1),
    _RsIfInvStackStatus_Type()
)
rsIfInvStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInvStackStatus.setStatus("current")
_RsIfConformance_ObjectIdentity = ObjectIdentity
rsIfConformance = _RsIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4)
)
_RsIfCompliances_ObjectIdentity = ObjectIdentity
rsIfCompliances = _RsIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 1)
)
_RsIfGroups_ObjectIdentity = ObjectIdentity
rsIfGroups = _RsIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 2)
)
ifEntry.registerAugmentions(
    ("REDSTONE-IF-MIB",
     "rsIfEntry")
)
rsIfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

rsIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 2, 1)
)
rsIfGroup.setObjects(
    ("REDSTONE-IF-MIB", "rsIfType")
)
if mibBuilder.loadTexts:
    rsIfGroup.setStatus("current")

rsIfInvStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 2, 2)
)
rsIfInvStackGroup.setObjects(
    ("REDSTONE-IF-MIB", "rsIfInvStackStatus")
)
if mibBuilder.loadTexts:
    rsIfInvStackGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 3, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-IF-MIB",
    **{"RsIfType": RsIfType,
       "rsIfMIB": rsIfMIB,
       "rsInterfaces": rsInterfaces,
       "rsIf": rsIf,
       "rsIfObjects": rsIfObjects,
       "rsIfTable": rsIfTable,
       "rsIfEntry": rsIfEntry,
       "rsIfType": rsIfType,
       "rsIfInvStackTable": rsIfInvStackTable,
       "rsIfInvStackEntry": rsIfInvStackEntry,
       "rsIfInvStackStatus": rsIfInvStackStatus,
       "rsIfConformance": rsIfConformance,
       "rsIfCompliances": rsIfCompliances,
       "rsIfCompliance": rsIfCompliance,
       "rsIfGroups": rsIfGroups,
       "rsIfGroup": rsIfGroup,
       "rsIfInvStackGroup": rsIfInvStackGroup}
)
