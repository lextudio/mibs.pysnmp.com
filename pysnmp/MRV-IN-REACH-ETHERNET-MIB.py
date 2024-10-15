# SNMP MIB module (MRV-IN-REACH-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IN-REACH-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:40 2024
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

(mrvInReachProductDivision,) = mibBuilder.importSymbols(
    "MRV-IN-REACH-PRODUCT-DIVISION-MIB",
    "mrvInReachProductDivision")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XEthernet_ObjectIdentity = ObjectIdentity
xEthernet = _XEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 11)
)
_EtherTable_Object = MibTable
etherTable = _EtherTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 1)
)
if mibBuilder.loadTexts:
    etherTable.setStatus("mandatory")
_EtherEntry_Object = MibTableRow
etherEntry = _EtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 1, 1)
)
etherEntry.setIndexNames(
    (0, "MRV-IN-REACH-ETHERNET-MIB", "etherIndex"),
)
if mibBuilder.loadTexts:
    etherEntry.setStatus("mandatory")
_EtherIndex_Type = Integer32
_EtherIndex_Object = MibTableColumn
etherIndex = _EtherIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 1, 1, 1),
    _EtherIndex_Type()
)
etherIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIndex.setStatus("mandatory")
_EtherAlignmentErrors_Type = Counter32
_EtherAlignmentErrors_Object = MibTableColumn
etherAlignmentErrors = _EtherAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 1, 1, 2),
    _EtherAlignmentErrors_Type()
)
etherAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherAlignmentErrors.setStatus("mandatory")
_EtherFCSErrors_Type = Counter32
_EtherFCSErrors_Object = MibTableColumn
etherFCSErrors = _EtherFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 1, 1, 3),
    _EtherFCSErrors_Type()
)
etherFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherFCSErrors.setStatus("mandatory")
_EtherTxTable_Object = MibTable
etherTxTable = _EtherTxTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 2)
)
if mibBuilder.loadTexts:
    etherTxTable.setStatus("mandatory")
_EtherTxEntry_Object = MibTableRow
etherTxEntry = _EtherTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 2, 1)
)
etherTxEntry.setIndexNames(
    (0, "MRV-IN-REACH-ETHERNET-MIB", "etherTxIndex"),
)
if mibBuilder.loadTexts:
    etherTxEntry.setStatus("mandatory")
_EtherTxIndex_Type = Integer32
_EtherTxIndex_Object = MibTableColumn
etherTxIndex = _EtherTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 2, 1, 1),
    _EtherTxIndex_Type()
)
etherTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTxIndex.setStatus("mandatory")
_EtherTxSingleCollisionFrames_Type = Counter32
_EtherTxSingleCollisionFrames_Object = MibTableColumn
etherTxSingleCollisionFrames = _EtherTxSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 2, 1, 2),
    _EtherTxSingleCollisionFrames_Type()
)
etherTxSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTxSingleCollisionFrames.setStatus("mandatory")
_EtherTxMultipleCollisionFrames_Type = Counter32
_EtherTxMultipleCollisionFrames_Object = MibTableColumn
etherTxMultipleCollisionFrames = _EtherTxMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 2, 1, 3),
    _EtherTxMultipleCollisionFrames_Type()
)
etherTxMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTxMultipleCollisionFrames.setStatus("mandatory")
_EtherMulticastTable_Object = MibTable
etherMulticastTable = _EtherMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 3)
)
if mibBuilder.loadTexts:
    etherMulticastTable.setStatus("mandatory")
_EtherMulticastEntry_Object = MibTableRow
etherMulticastEntry = _EtherMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 3, 1)
)
etherMulticastEntry.setIndexNames(
    (0, "MRV-IN-REACH-ETHERNET-MIB", "etherMulticastIndex"),
)
if mibBuilder.loadTexts:
    etherMulticastEntry.setStatus("mandatory")
_EtherMulticastIndex_Type = Integer32
_EtherMulticastIndex_Object = MibTableColumn
etherMulticastIndex = _EtherMulticastIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 3, 1, 1),
    _EtherMulticastIndex_Type()
)
etherMulticastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherMulticastIndex.setStatus("mandatory")
_EtherMulticastBytesIn_Type = Counter32
_EtherMulticastBytesIn_Object = MibTableColumn
etherMulticastBytesIn = _EtherMulticastBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 3, 1, 2),
    _EtherMulticastBytesIn_Type()
)
etherMulticastBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherMulticastBytesIn.setStatus("mandatory")
_EtherMulticastBytesOut_Type = Counter32
_EtherMulticastBytesOut_Object = MibTableColumn
etherMulticastBytesOut = _EtherMulticastBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 3, 1, 3),
    _EtherMulticastBytesOut_Type()
)
etherMulticastBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherMulticastBytesOut.setStatus("mandatory")
_EtherXTxTable_Object = MibTable
etherXTxTable = _EtherXTxTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 4)
)
if mibBuilder.loadTexts:
    etherXTxTable.setStatus("mandatory")
_EtherXTxEntry_Object = MibTableRow
etherXTxEntry = _EtherXTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 4, 1)
)
etherXTxEntry.setIndexNames(
    (0, "MRV-IN-REACH-ETHERNET-MIB", "etherXTxIndex"),
)
if mibBuilder.loadTexts:
    etherXTxEntry.setStatus("mandatory")
_EtherXTxIndex_Type = Integer32
_EtherXTxIndex_Object = MibTableColumn
etherXTxIndex = _EtherXTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 4, 1, 1),
    _EtherXTxIndex_Type()
)
etherXTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherXTxIndex.setStatus("mandatory")
_EtherXTxExcessiveCollisions_Type = Counter32
_EtherXTxExcessiveCollisions_Object = MibTableColumn
etherXTxExcessiveCollisions = _EtherXTxExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 4, 1, 2),
    _EtherXTxExcessiveCollisions_Type()
)
etherXTxExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherXTxExcessiveCollisions.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IN-REACH-ETHERNET-MIB",
    **{"xEthernet": xEthernet,
       "etherTable": etherTable,
       "etherEntry": etherEntry,
       "etherIndex": etherIndex,
       "etherAlignmentErrors": etherAlignmentErrors,
       "etherFCSErrors": etherFCSErrors,
       "etherTxTable": etherTxTable,
       "etherTxEntry": etherTxEntry,
       "etherTxIndex": etherTxIndex,
       "etherTxSingleCollisionFrames": etherTxSingleCollisionFrames,
       "etherTxMultipleCollisionFrames": etherTxMultipleCollisionFrames,
       "etherMulticastTable": etherMulticastTable,
       "etherMulticastEntry": etherMulticastEntry,
       "etherMulticastIndex": etherMulticastIndex,
       "etherMulticastBytesIn": etherMulticastBytesIn,
       "etherMulticastBytesOut": etherMulticastBytesOut,
       "etherXTxTable": etherXTxTable,
       "etherXTxEntry": etherXTxEntry,
       "etherXTxIndex": etherXTxIndex,
       "etherXTxExcessiveCollisions": etherXTxExcessiveCollisions}
)
