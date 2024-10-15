# SNMP MIB module (ARISTA-BRIDGE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-BRIDGE-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:17 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(dot1qFdbId,
 dot1qTpFdbAddress) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qFdbId",
    "dot1qTpFdbAddress")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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

aristaBridgeExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2)
)
aristaBridgeExtMIB.setRevisions(
        ("2014-08-15 00:00",
         "2011-03-31 13:00",
         "2010-05-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaDot1qTpFdbTable_Object = MibTable
aristaDot1qTpFdbTable = _AristaDot1qTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aristaDot1qTpFdbTable.setStatus("current")
_AristaDot1qTpFdbEntry_Object = MibTableRow
aristaDot1qTpFdbEntry = _AristaDot1qTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1)
)
aristaDot1qTpFdbEntry.setIndexNames(
    (0, "ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbTimeMark"),
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
    (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"),
)
if mibBuilder.loadTexts:
    aristaDot1qTpFdbEntry.setStatus("current")
_AristaDot1qTpFdbTimeMark_Type = TimeFilter
_AristaDot1qTpFdbTimeMark_Object = MibTableColumn
aristaDot1qTpFdbTimeMark = _AristaDot1qTpFdbTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 1),
    _AristaDot1qTpFdbTimeMark_Type()
)
aristaDot1qTpFdbTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaDot1qTpFdbTimeMark.setStatus("current")
_AristaDot1qTpFdbNumMoves_Type = Counter32
_AristaDot1qTpFdbNumMoves_Object = MibTableColumn
aristaDot1qTpFdbNumMoves = _AristaDot1qTpFdbNumMoves_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 2),
    _AristaDot1qTpFdbNumMoves_Type()
)
aristaDot1qTpFdbNumMoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaDot1qTpFdbNumMoves.setStatus("current")
_AristaDot1qTpFdbLastMove_Type = TimeTicks
_AristaDot1qTpFdbLastMove_Object = MibTableColumn
aristaDot1qTpFdbLastMove = _AristaDot1qTpFdbLastMove_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 3),
    _AristaDot1qTpFdbLastMove_Type()
)
aristaDot1qTpFdbLastMove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaDot1qTpFdbLastMove.setStatus("current")
_AristaBridgeExtConformance_ObjectIdentity = ObjectIdentity
aristaBridgeExtConformance = _AristaBridgeExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2)
)
_AristaBridgeExtGroups_ObjectIdentity = ObjectIdentity
aristaBridgeExtGroups = _AristaBridgeExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1)
)
_AristaBridgeExtCompliances_ObjectIdentity = ObjectIdentity
aristaBridgeExtCompliances = _AristaBridgeExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2)
)

# Managed Objects groups

aristaBridgeExtBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1, 1)
)
aristaBridgeExtBaseGroup.setObjects(
      *(("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbNumMoves"),
        ("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbLastMove"))
)
if mibBuilder.loadTexts:
    aristaBridgeExtBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaBridgeExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    aristaBridgeExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-BRIDGE-EXT-MIB",
    **{"aristaBridgeExtMIB": aristaBridgeExtMIB,
       "aristaDot1qTpFdbTable": aristaDot1qTpFdbTable,
       "aristaDot1qTpFdbEntry": aristaDot1qTpFdbEntry,
       "aristaDot1qTpFdbTimeMark": aristaDot1qTpFdbTimeMark,
       "aristaDot1qTpFdbNumMoves": aristaDot1qTpFdbNumMoves,
       "aristaDot1qTpFdbLastMove": aristaDot1qTpFdbLastMove,
       "aristaBridgeExtConformance": aristaBridgeExtConformance,
       "aristaBridgeExtGroups": aristaBridgeExtGroups,
       "aristaBridgeExtBaseGroup": aristaBridgeExtBaseGroup,
       "aristaBridgeExtCompliances": aristaBridgeExtCompliances,
       "aristaBridgeExtCompliance": aristaBridgeExtCompliance}
)
