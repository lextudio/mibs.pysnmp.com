# SNMP MIB module (SHIVA-ETHER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SHIVA-ETHER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:51:20 2024
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

(tEther,) = mibBuilder.importSymbols(
    "SHIVA-MIB",
    "tEther")

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

_TEtherTable_Object = MibTable
tEtherTable = _TEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1)
)
if mibBuilder.loadTexts:
    tEtherTable.setStatus("mandatory")
_TEtherEntry_Object = MibTableRow
tEtherEntry = _TEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1)
)
tEtherEntry.setIndexNames(
    (0, "SHIVA-ETHER-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    tEtherEntry.setStatus("mandatory")
_EtherCRCErrors_Type = Counter32
_EtherCRCErrors_Object = MibTableColumn
etherCRCErrors = _EtherCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 1),
    _EtherCRCErrors_Type()
)
etherCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherCRCErrors.setStatus("mandatory")
_EtherAlignErrors_Type = Counter32
_EtherAlignErrors_Object = MibTableColumn
etherAlignErrors = _EtherAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 2),
    _EtherAlignErrors_Type()
)
etherAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherAlignErrors.setStatus("mandatory")
_EtherResourceErrors_Type = Counter32
_EtherResourceErrors_Object = MibTableColumn
etherResourceErrors = _EtherResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 3),
    _EtherResourceErrors_Type()
)
etherResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherResourceErrors.setStatus("mandatory")
_EtherOverrunErrors_Type = Counter32
_EtherOverrunErrors_Object = MibTableColumn
etherOverrunErrors = _EtherOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 4),
    _EtherOverrunErrors_Type()
)
etherOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOverrunErrors.setStatus("mandatory")
_EtherInPackets_Type = Counter32
_EtherInPackets_Object = MibTableColumn
etherInPackets = _EtherInPackets_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 5),
    _EtherInPackets_Type()
)
etherInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherInPackets.setStatus("mandatory")
_EtherOutPackets_Type = Counter32
_EtherOutPackets_Object = MibTableColumn
etherOutPackets = _EtherOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 6),
    _EtherOutPackets_Type()
)
etherOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOutPackets.setStatus("mandatory")
_EtherBadTransmits_Type = Counter32
_EtherBadTransmits_Object = MibTableColumn
etherBadTransmits = _EtherBadTransmits_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 7),
    _EtherBadTransmits_Type()
)
etherBadTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBadTransmits.setStatus("mandatory")
_EtherOversizeFrames_Type = Counter32
_EtherOversizeFrames_Object = MibTableColumn
etherOversizeFrames = _EtherOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 8),
    _EtherOversizeFrames_Type()
)
etherOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOversizeFrames.setStatus("mandatory")
_EtherSpurRUReadys_Type = Counter32
_EtherSpurRUReadys_Object = MibTableColumn
etherSpurRUReadys = _EtherSpurRUReadys_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 9),
    _EtherSpurRUReadys_Type()
)
etherSpurRUReadys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherSpurRUReadys.setStatus("mandatory")
_EtherSpurCUActives_Type = Counter32
_EtherSpurCUActives_Object = MibTableColumn
etherSpurCUActives = _EtherSpurCUActives_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 10),
    _EtherSpurCUActives_Type()
)
etherSpurCUActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherSpurCUActives.setStatus("mandatory")
_EtherSpurUnknowns_Type = Counter32
_EtherSpurUnknowns_Object = MibTableColumn
etherSpurUnknowns = _EtherSpurUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 11),
    _EtherSpurUnknowns_Type()
)
etherSpurUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherSpurUnknowns.setStatus("mandatory")
_EtherBcastDrops_Type = Counter32
_EtherBcastDrops_Object = MibTableColumn
etherBcastDrops = _EtherBcastDrops_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 12),
    _EtherBcastDrops_Type()
)
etherBcastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBcastDrops.setStatus("mandatory")
_EtherReceiverRestarts_Type = Counter32
_EtherReceiverRestarts_Object = MibTableColumn
etherReceiverRestarts = _EtherReceiverRestarts_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 13),
    _EtherReceiverRestarts_Type()
)
etherReceiverRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherReceiverRestarts.setStatus("mandatory")
_EtherReinterrupts_Type = Counter32
_EtherReinterrupts_Object = MibTableColumn
etherReinterrupts = _EtherReinterrupts_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 14),
    _EtherReinterrupts_Type()
)
etherReinterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherReinterrupts.setStatus("mandatory")
_EtherBufferReroutes_Type = Counter32
_EtherBufferReroutes_Object = MibTableColumn
etherBufferReroutes = _EtherBufferReroutes_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 15),
    _EtherBufferReroutes_Type()
)
etherBufferReroutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBufferReroutes.setStatus("mandatory")
_EtherBufferDrops_Type = Counter32
_EtherBufferDrops_Object = MibTableColumn
etherBufferDrops = _EtherBufferDrops_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 16),
    _EtherBufferDrops_Type()
)
etherBufferDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBufferDrops.setStatus("mandatory")
_EtherCollisions_Type = Counter32
_EtherCollisions_Object = MibTableColumn
etherCollisions = _EtherCollisions_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 17),
    _EtherCollisions_Type()
)
etherCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherCollisions.setStatus("mandatory")
_EtherDefers_Type = Counter32
_EtherDefers_Object = MibTableColumn
etherDefers = _EtherDefers_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 18),
    _EtherDefers_Type()
)
etherDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherDefers.setStatus("mandatory")
_EtherDMAUnderruns_Type = Counter32
_EtherDMAUnderruns_Object = MibTableColumn
etherDMAUnderruns = _EtherDMAUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 19),
    _EtherDMAUnderruns_Type()
)
etherDMAUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherDMAUnderruns.setStatus("mandatory")
_EtherMaxCollisions_Type = Counter32
_EtherMaxCollisions_Object = MibTableColumn
etherMaxCollisions = _EtherMaxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 20),
    _EtherMaxCollisions_Type()
)
etherMaxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherMaxCollisions.setStatus("mandatory")
_EtherNoCarriers_Type = Counter32
_EtherNoCarriers_Object = MibTableColumn
etherNoCarriers = _EtherNoCarriers_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 21),
    _EtherNoCarriers_Type()
)
etherNoCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherNoCarriers.setStatus("mandatory")
_EtherNoCTSs_Type = Counter32
_EtherNoCTSs_Object = MibTableColumn
etherNoCTSs = _EtherNoCTSs_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 22),
    _EtherNoCTSs_Type()
)
etherNoCTSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherNoCTSs.setStatus("mandatory")
_EtherNoSQEs_Type = Counter32
_EtherNoSQEs_Object = MibTableColumn
etherNoSQEs = _EtherNoSQEs_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 23),
    _EtherNoSQEs_Type()
)
etherNoSQEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherNoSQEs.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SHIVA-ETHER-MIB",
    **{"tEtherTable": tEtherTable,
       "tEtherEntry": tEtherEntry,
       "etherCRCErrors": etherCRCErrors,
       "etherAlignErrors": etherAlignErrors,
       "etherResourceErrors": etherResourceErrors,
       "etherOverrunErrors": etherOverrunErrors,
       "etherInPackets": etherInPackets,
       "etherOutPackets": etherOutPackets,
       "etherBadTransmits": etherBadTransmits,
       "etherOversizeFrames": etherOversizeFrames,
       "etherSpurRUReadys": etherSpurRUReadys,
       "etherSpurCUActives": etherSpurCUActives,
       "etherSpurUnknowns": etherSpurUnknowns,
       "etherBcastDrops": etherBcastDrops,
       "etherReceiverRestarts": etherReceiverRestarts,
       "etherReinterrupts": etherReinterrupts,
       "etherBufferReroutes": etherBufferReroutes,
       "etherBufferDrops": etherBufferDrops,
       "etherCollisions": etherCollisions,
       "etherDefers": etherDefers,
       "etherDMAUnderruns": etherDMAUnderruns,
       "etherMaxCollisions": etherMaxCollisions,
       "etherNoCarriers": etherNoCarriers,
       "etherNoCTSs": etherNoCTSs,
       "etherNoSQEs": etherNoSQEs,
       "pysmiFakeCol1": pysmiFakeCol1}
)
