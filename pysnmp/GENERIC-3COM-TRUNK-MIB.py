# SNMP MIB module (GENERIC-3COM-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GENERIC-3COM-TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:28 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10)
)
_GenExperimental_ObjectIdentity = ObjectIdentity
genExperimental = _GenExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1)
)
_GenTrunk_ObjectIdentity = ObjectIdentity
genTrunk = _GenTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15)
)
_A3ComTrunkGroup_ObjectIdentity = ObjectIdentity
a3ComTrunkGroup = _A3ComTrunkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1)
)
_A3ComTrunkIfTable_Object = MibTable
a3ComTrunkIfTable = _A3ComTrunkIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    a3ComTrunkIfTable.setStatus("mandatory")
_A3ComTrunkIfEntry_Object = MibTableRow
a3ComTrunkIfEntry = _A3ComTrunkIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 1, 1)
)
a3ComTrunkIfEntry.setIndexNames(
    (0, "GENERIC-3COM-TRUNK-MIB", "a3ComTrunkIfIndex"),
)
if mibBuilder.loadTexts:
    a3ComTrunkIfEntry.setStatus("mandatory")
_A3ComTrunkIfIndex_Type = Integer32
_A3ComTrunkIfIndex_Object = MibTableColumn
a3ComTrunkIfIndex = _A3ComTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 1, 1, 1),
    _A3ComTrunkIfIndex_Type()
)
a3ComTrunkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a3ComTrunkIfIndex.setStatus("mandatory")


class _A3ComTrunkIfName_Type(DisplayString):
    """Custom type a3ComTrunkIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComTrunkIfName_Type.__name__ = "DisplayString"
_A3ComTrunkIfName_Object = MibTableColumn
a3ComTrunkIfName = _A3ComTrunkIfName_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 1, 1, 2),
    _A3ComTrunkIfName_Type()
)
a3ComTrunkIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComTrunkIfName.setStatus("mandatory")


class _A3ComTrunkTcmpEnable_Type(Integer32):
    """Custom type a3ComTrunkTcmpEnable based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("tcmpDisable", 2),
          ("tcmpEnable", 3))
    )


_A3ComTrunkTcmpEnable_Type.__name__ = "Integer32"
_A3ComTrunkTcmpEnable_Object = MibTableColumn
a3ComTrunkTcmpEnable = _A3ComTrunkTcmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 1, 1, 3),
    _A3ComTrunkTcmpEnable_Type()
)
a3ComTrunkTcmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComTrunkTcmpEnable.setStatus("mandatory")


class _A3ComTrunkMacMode_Type(Integer32):
    """Custom type a3ComTrunkMacMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("full10", 2),
          ("full100", 4),
          ("full1000", 6),
          ("half10", 1),
          ("half100", 3),
          ("half1000", 5))
    )


_A3ComTrunkMacMode_Type.__name__ = "Integer32"
_A3ComTrunkMacMode_Object = MibTableColumn
a3ComTrunkMacMode = _A3ComTrunkMacMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 1, 1, 4),
    _A3ComTrunkMacMode_Type()
)
a3ComTrunkMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComTrunkMacMode.setStatus("mandatory")
_A3ComTrunkIfStatus_Type = RowStatus
_A3ComTrunkIfStatus_Object = MibTableColumn
a3ComTrunkIfStatus = _A3ComTrunkIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 1, 1, 5),
    _A3ComTrunkIfStatus_Type()
)
a3ComTrunkIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComTrunkIfStatus.setStatus("mandatory")
_A3ComTrunkMacTable_Object = MibTable
a3ComTrunkMacTable = _A3ComTrunkMacTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    a3ComTrunkMacTable.setStatus("mandatory")
_A3ComTrunkMacEntry_Object = MibTableRow
a3ComTrunkMacEntry = _A3ComTrunkMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 2, 1)
)
a3ComTrunkMacEntry.setIndexNames(
    (0, "GENERIC-3COM-TRUNK-MIB", "a3ComTrunkMacTrunkIfIndex"),
    (0, "GENERIC-3COM-TRUNK-MIB", "a3ComTrunkMacIndex"),
)
if mibBuilder.loadTexts:
    a3ComTrunkMacEntry.setStatus("mandatory")
_A3ComTrunkMacTrunkIfIndex_Type = Integer32
_A3ComTrunkMacTrunkIfIndex_Object = MibTableColumn
a3ComTrunkMacTrunkIfIndex = _A3ComTrunkMacTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 2, 1, 1),
    _A3ComTrunkMacTrunkIfIndex_Type()
)
a3ComTrunkMacTrunkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a3ComTrunkMacTrunkIfIndex.setStatus("mandatory")
_A3ComTrunkMacIndex_Type = Integer32
_A3ComTrunkMacIndex_Object = MibTableColumn
a3ComTrunkMacIndex = _A3ComTrunkMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 2, 1, 2),
    _A3ComTrunkMacIndex_Type()
)
a3ComTrunkMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a3ComTrunkMacIndex.setStatus("mandatory")


class _A3ComTrunkTcmpMacState_Type(Integer32):
    """Custom type a3ComTrunkTcmpMacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("configured", 7),
          ("down", 5),
          ("inUse", 3),
          ("notInUse", 1),
          ("selected", 2),
          ("undefined", 4),
          ("up", 6))
    )


_A3ComTrunkTcmpMacState_Type.__name__ = "Integer32"
_A3ComTrunkTcmpMacState_Object = MibTableColumn
a3ComTrunkTcmpMacState = _A3ComTrunkTcmpMacState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 2, 1, 3),
    _A3ComTrunkTcmpMacState_Type()
)
a3ComTrunkTcmpMacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComTrunkTcmpMacState.setStatus("mandatory")
_A3ComTrunkTcmpPeersTable_Object = MibTable
a3ComTrunkTcmpPeersTable = _A3ComTrunkTcmpPeersTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 3)
)
if mibBuilder.loadTexts:
    a3ComTrunkTcmpPeersTable.setStatus("mandatory")
_A3ComTrunkTcmpPeersEntry_Object = MibTableRow
a3ComTrunkTcmpPeersEntry = _A3ComTrunkTcmpPeersEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 3, 1)
)
a3ComTrunkTcmpPeersEntry.setIndexNames(
    (0, "GENERIC-3COM-TRUNK-MIB", "a3ComTrunkPeerTrunkIfIndex"),
    (0, "GENERIC-3COM-TRUNK-MIB", "a3ComTrunkPeerMacIndex"),
    (0, "GENERIC-3COM-TRUNK-MIB", "a3ComTrunkPeersMacAddress"),
)
if mibBuilder.loadTexts:
    a3ComTrunkTcmpPeersEntry.setStatus("mandatory")
_A3ComTrunkPeerTrunkIfIndex_Type = Integer32
_A3ComTrunkPeerTrunkIfIndex_Object = MibTableColumn
a3ComTrunkPeerTrunkIfIndex = _A3ComTrunkPeerTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 3, 1, 1),
    _A3ComTrunkPeerTrunkIfIndex_Type()
)
a3ComTrunkPeerTrunkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a3ComTrunkPeerTrunkIfIndex.setStatus("mandatory")
_A3ComTrunkPeerMacIndex_Type = Integer32
_A3ComTrunkPeerMacIndex_Object = MibTableColumn
a3ComTrunkPeerMacIndex = _A3ComTrunkPeerMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 3, 1, 2),
    _A3ComTrunkPeerMacIndex_Type()
)
a3ComTrunkPeerMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    a3ComTrunkPeerMacIndex.setStatus("mandatory")
_A3ComTrunkPeersMacAddress_Type = PhysAddress
_A3ComTrunkPeersMacAddress_Object = MibTableColumn
a3ComTrunkPeersMacAddress = _A3ComTrunkPeersMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 15, 1, 3, 1, 3),
    _A3ComTrunkPeersMacAddress_Type()
)
a3ComTrunkPeersMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComTrunkPeersMacAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GENERIC-3COM-TRUNK-MIB",
    **{"RowStatus": RowStatus,
       "a3Com": a3Com,
       "generic": generic,
       "genExperimental": genExperimental,
       "genTrunk": genTrunk,
       "a3ComTrunkGroup": a3ComTrunkGroup,
       "a3ComTrunkIfTable": a3ComTrunkIfTable,
       "a3ComTrunkIfEntry": a3ComTrunkIfEntry,
       "a3ComTrunkIfIndex": a3ComTrunkIfIndex,
       "a3ComTrunkIfName": a3ComTrunkIfName,
       "a3ComTrunkTcmpEnable": a3ComTrunkTcmpEnable,
       "a3ComTrunkMacMode": a3ComTrunkMacMode,
       "a3ComTrunkIfStatus": a3ComTrunkIfStatus,
       "a3ComTrunkMacTable": a3ComTrunkMacTable,
       "a3ComTrunkMacEntry": a3ComTrunkMacEntry,
       "a3ComTrunkMacTrunkIfIndex": a3ComTrunkMacTrunkIfIndex,
       "a3ComTrunkMacIndex": a3ComTrunkMacIndex,
       "a3ComTrunkTcmpMacState": a3ComTrunkTcmpMacState,
       "a3ComTrunkTcmpPeersTable": a3ComTrunkTcmpPeersTable,
       "a3ComTrunkTcmpPeersEntry": a3ComTrunkTcmpPeersEntry,
       "a3ComTrunkPeerTrunkIfIndex": a3ComTrunkPeerTrunkIfIndex,
       "a3ComTrunkPeerMacIndex": a3ComTrunkPeerMacIndex,
       "a3ComTrunkPeersMacAddress": a3ComTrunkPeersMacAddress}
)
