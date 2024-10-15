# SNMP MIB module (CNT243-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNT243-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:57 2024
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

(cnt2Subagent,) = mibBuilder.importSymbols(
    "CNT2-MIB",
    "cnt2Subagent")

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

_Cnt2Atmf_ObjectIdentity = ObjectIdentity
cnt2Atmf = _Cnt2Atmf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 3)
)
_Cnt2AtmfTable_Object = MibTable
cnt2AtmfTable = _Cnt2AtmfTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cnt2AtmfTable.setStatus("mandatory")
_Cnt2AtmfEntry_Object = MibTableRow
cnt2AtmfEntry = _Cnt2AtmfEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 3, 1, 1)
)
cnt2AtmfEntry.setIndexNames(
    (0, "CNT243-MIB", "cnt2AtmfSlot"),
    (0, "CNT243-MIB", "cnt2AtmfIndex"),
)
if mibBuilder.loadTexts:
    cnt2AtmfEntry.setStatus("mandatory")
_Cnt2AtmfSlot_Type = Integer32
_Cnt2AtmfSlot_Object = MibTableColumn
cnt2AtmfSlot = _Cnt2AtmfSlot_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 3, 1, 1, 1),
    _Cnt2AtmfSlot_Type()
)
cnt2AtmfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2AtmfSlot.setStatus("mandatory")
_Cnt2AtmfIndex_Type = Integer32
_Cnt2AtmfIndex_Object = MibTableColumn
cnt2AtmfIndex = _Cnt2AtmfIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 3, 1, 1, 2),
    _Cnt2AtmfIndex_Type()
)
cnt2AtmfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2AtmfIndex.setStatus("mandatory")
_Cnt2AtmfPort_Type = Integer32
_Cnt2AtmfPort_Object = MibTableColumn
cnt2AtmfPort = _Cnt2AtmfPort_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 3, 1, 1, 3),
    _Cnt2AtmfPort_Type()
)
cnt2AtmfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2AtmfPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNT243-MIB",
    **{"cnt2Atmf": cnt2Atmf,
       "cnt2AtmfTable": cnt2AtmfTable,
       "cnt2AtmfEntry": cnt2AtmfEntry,
       "cnt2AtmfSlot": cnt2AtmfSlot,
       "cnt2AtmfIndex": cnt2AtmfIndex,
       "cnt2AtmfPort": cnt2AtmfPort}
)
