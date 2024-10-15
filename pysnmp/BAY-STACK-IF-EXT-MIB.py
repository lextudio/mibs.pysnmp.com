# SNMP MIB module (BAY-STACK-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-IF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:57 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackIfExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 40)
)
bayStackIfExtMib.setRevisions(
        ("2012-05-31 00:00",
         "2010-11-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsIfExtNotifications_ObjectIdentity = ObjectIdentity
bsIfExtNotifications = _BsIfExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 40, 0)
)
_BsIfExtObjects_ObjectIdentity = ObjectIdentity
bsIfExtObjects = _BsIfExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 40, 1)
)
_BsIfExtScalars_ObjectIdentity = ObjectIdentity
bsIfExtScalars = _BsIfExtScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 1)
)
_BsIfExtDirectedBroadcast_Type = TruthValue
_BsIfExtDirectedBroadcast_Object = MibScalar
bsIfExtDirectedBroadcast = _BsIfExtDirectedBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 1, 1),
    _BsIfExtDirectedBroadcast_Type()
)
bsIfExtDirectedBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIfExtDirectedBroadcast.setStatus("current")
_BsIfExtIfTable_Object = MibTable
bsIfExtIfTable = _BsIfExtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 2)
)
if mibBuilder.loadTexts:
    bsIfExtIfTable.setStatus("current")
_BsIfExtIfEntry_Object = MibTableRow
bsIfExtIfEntry = _BsIfExtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 2, 1)
)
bsIfExtIfEntry.setIndexNames(
    (0, "BAY-STACK-IF-EXT-MIB", "bsIfExtIfIndex"),
)
if mibBuilder.loadTexts:
    bsIfExtIfEntry.setStatus("current")
_BsIfExtIfIndex_Type = InterfaceIndex
_BsIfExtIfIndex_Object = MibTableColumn
bsIfExtIfIndex = _BsIfExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 2, 1, 1),
    _BsIfExtIfIndex_Type()
)
bsIfExtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIfExtIfIndex.setStatus("current")
_BsIfExtIfDirectedBroadcast_Type = TruthValue
_BsIfExtIfDirectedBroadcast_Object = MibTableColumn
bsIfExtIfDirectedBroadcast = _BsIfExtIfDirectedBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 40, 1, 2, 1, 2),
    _BsIfExtIfDirectedBroadcast_Type()
)
bsIfExtIfDirectedBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIfExtIfDirectedBroadcast.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-IF-EXT-MIB",
    **{"bayStackIfExtMib": bayStackIfExtMib,
       "bsIfExtNotifications": bsIfExtNotifications,
       "bsIfExtObjects": bsIfExtObjects,
       "bsIfExtScalars": bsIfExtScalars,
       "bsIfExtDirectedBroadcast": bsIfExtDirectedBroadcast,
       "bsIfExtIfTable": bsIfExtIfTable,
       "bsIfExtIfEntry": bsIfExtIfEntry,
       "bsIfExtIfIndex": bsIfExtIfIndex,
       "bsIfExtIfDirectedBroadcast": bsIfExtIfDirectedBroadcast}
)
