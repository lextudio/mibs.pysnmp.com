# SNMP MIB module (FASTPATH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FASTPATH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:56 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Excelan_ObjectIdentity = ObjectIdentity
excelan = _Excelan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_GenericGroup_ObjectIdentity = ObjectIdentity
genericGroup = _GenericGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_FastpathMib_ObjectIdentity = ObjectIdentity
fastpathMib = _FastpathMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11)
)
_Scc_ObjectIdentity = ObjectIdentity
scc = _Scc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 1)
)
_SccInterruptCount_Type = Counter32
_SccInterruptCount_Object = MibScalar
sccInterruptCount = _SccInterruptCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 1),
    _SccInterruptCount_Type()
)
sccInterruptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccInterruptCount.setStatus("mandatory")
_SccAbortCount_Type = Counter32
_SccAbortCount_Object = MibScalar
sccAbortCount = _SccAbortCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 2),
    _SccAbortCount_Type()
)
sccAbortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccAbortCount.setStatus("mandatory")
_SccSpuriousCount_Type = Counter32
_SccSpuriousCount_Object = MibScalar
sccSpuriousCount = _SccSpuriousCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 3),
    _SccSpuriousCount_Type()
)
sccSpuriousCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccSpuriousCount.setStatus("mandatory")
_SccCRCCount_Type = Counter32
_SccCRCCount_Object = MibScalar
sccCRCCount = _SccCRCCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 4),
    _SccCRCCount_Type()
)
sccCRCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccCRCCount.setStatus("mandatory")
_SccOverrunCount_Type = Counter32
_SccOverrunCount_Object = MibScalar
sccOverrunCount = _SccOverrunCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 5),
    _SccOverrunCount_Type()
)
sccOverrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccOverrunCount.setStatus("mandatory")
_SccUnderrunCount_Type = Counter32
_SccUnderrunCount_Object = MibScalar
sccUnderrunCount = _SccUnderrunCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 1, 6),
    _SccUnderrunCount_Type()
)
sccUnderrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sccUnderrunCount.setStatus("mandatory")
_Alap_ObjectIdentity = ObjectIdentity
alap = _Alap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 2)
)
_AlapReceiveCount_Type = Counter32
_AlapReceiveCount_Object = MibScalar
alapReceiveCount = _AlapReceiveCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 1),
    _AlapReceiveCount_Type()
)
alapReceiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alapReceiveCount.setStatus("mandatory")
_AlapTransmitCount_Type = Counter32
_AlapTransmitCount_Object = MibScalar
alapTransmitCount = _AlapTransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 2),
    _AlapTransmitCount_Type()
)
alapTransmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alapTransmitCount.setStatus("mandatory")
_AlapNoHandlerCount_Type = Counter32
_AlapNoHandlerCount_Object = MibScalar
alapNoHandlerCount = _AlapNoHandlerCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 3),
    _AlapNoHandlerCount_Type()
)
alapNoHandlerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alapNoHandlerCount.setStatus("mandatory")
_AlapLengthErrorCount_Type = Counter32
_AlapLengthErrorCount_Object = MibScalar
alapLengthErrorCount = _AlapLengthErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 4),
    _AlapLengthErrorCount_Type()
)
alapLengthErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alapLengthErrorCount.setStatus("mandatory")
_AlapBadCount_Type = Counter32
_AlapBadCount_Object = MibScalar
alapBadCount = _AlapBadCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 5),
    _AlapBadCount_Type()
)
alapBadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alapBadCount.setStatus("mandatory")
_AlapCollisionCount_Type = Counter32
_AlapCollisionCount_Object = MibScalar
alapCollisionCount = _AlapCollisionCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 6),
    _AlapCollisionCount_Type()
)
alapCollisionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alapCollisionCount.setStatus("mandatory")
_AlapDeferCount_Type = Counter32
_AlapDeferCount_Object = MibScalar
alapDeferCount = _AlapDeferCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 7),
    _AlapDeferCount_Type()
)
alapDeferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alapDeferCount.setStatus("mandatory")
_AlapNoDataCount_Type = Counter32
_AlapNoDataCount_Object = MibScalar
alapNoDataCount = _AlapNoDataCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 8),
    _AlapNoDataCount_Type()
)
alapNoDataCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alapNoDataCount.setStatus("mandatory")
_AlapRandomCTS_Type = Counter32
_AlapRandomCTS_Object = MibScalar
alapRandomCTS = _AlapRandomCTS_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 2, 9),
    _AlapRandomCTS_Type()
)
alapRandomCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alapRandomCTS.setStatus("mandatory")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3)
)
_EtherCRCErrors_Type = Counter32
_EtherCRCErrors_Object = MibScalar
etherCRCErrors = _EtherCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 1),
    _EtherCRCErrors_Type()
)
etherCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherCRCErrors.setStatus("mandatory")
_EtherAlignErrors_Type = Counter32
_EtherAlignErrors_Object = MibScalar
etherAlignErrors = _EtherAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 2),
    _EtherAlignErrors_Type()
)
etherAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherAlignErrors.setStatus("mandatory")
_EtherResourceErrors_Type = Counter32
_EtherResourceErrors_Object = MibScalar
etherResourceErrors = _EtherResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 3),
    _EtherResourceErrors_Type()
)
etherResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherResourceErrors.setStatus("mandatory")
_EtherOverrunErrors_Type = Counter32
_EtherOverrunErrors_Object = MibScalar
etherOverrunErrors = _EtherOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 4),
    _EtherOverrunErrors_Type()
)
etherOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOverrunErrors.setStatus("mandatory")
_EtherInPackets_Type = Counter32
_EtherInPackets_Object = MibScalar
etherInPackets = _EtherInPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 5),
    _EtherInPackets_Type()
)
etherInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherInPackets.setStatus("mandatory")
_EtherOutPackets_Type = Counter32
_EtherOutPackets_Object = MibScalar
etherOutPackets = _EtherOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 6),
    _EtherOutPackets_Type()
)
etherOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOutPackets.setStatus("mandatory")
_EtherBadTransmits_Type = Counter32
_EtherBadTransmits_Object = MibScalar
etherBadTransmits = _EtherBadTransmits_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 7),
    _EtherBadTransmits_Type()
)
etherBadTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBadTransmits.setStatus("mandatory")
_EtherOversizeFrames_Type = Counter32
_EtherOversizeFrames_Object = MibScalar
etherOversizeFrames = _EtherOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 8),
    _EtherOversizeFrames_Type()
)
etherOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOversizeFrames.setStatus("mandatory")
_EtherSpurRUReadys_Type = Counter32
_EtherSpurRUReadys_Object = MibScalar
etherSpurRUReadys = _EtherSpurRUReadys_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 9),
    _EtherSpurRUReadys_Type()
)
etherSpurRUReadys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherSpurRUReadys.setStatus("mandatory")
_EtherSpurCUActives_Type = Counter32
_EtherSpurCUActives_Object = MibScalar
etherSpurCUActives = _EtherSpurCUActives_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 10),
    _EtherSpurCUActives_Type()
)
etherSpurCUActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherSpurCUActives.setStatus("mandatory")
_EtherSpurUnknown_Type = Counter32
_EtherSpurUnknown_Object = MibScalar
etherSpurUnknown = _EtherSpurUnknown_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 11),
    _EtherSpurUnknown_Type()
)
etherSpurUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherSpurUnknown.setStatus("mandatory")
_EtherBcastDrops_Type = Counter32
_EtherBcastDrops_Object = MibScalar
etherBcastDrops = _EtherBcastDrops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 12),
    _EtherBcastDrops_Type()
)
etherBcastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBcastDrops.setStatus("mandatory")
_EtherReceiverRestarts_Type = Counter32
_EtherReceiverRestarts_Object = MibScalar
etherReceiverRestarts = _EtherReceiverRestarts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 13),
    _EtherReceiverRestarts_Type()
)
etherReceiverRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherReceiverRestarts.setStatus("mandatory")
_EtherReinterrupts_Type = Counter32
_EtherReinterrupts_Object = MibScalar
etherReinterrupts = _EtherReinterrupts_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 14),
    _EtherReinterrupts_Type()
)
etherReinterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherReinterrupts.setStatus("mandatory")
_EtherBufferReroutes_Type = Counter32
_EtherBufferReroutes_Object = MibScalar
etherBufferReroutes = _EtherBufferReroutes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 15),
    _EtherBufferReroutes_Type()
)
etherBufferReroutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBufferReroutes.setStatus("mandatory")
_EtherBufferDrops_Type = Counter32
_EtherBufferDrops_Object = MibScalar
etherBufferDrops = _EtherBufferDrops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 16),
    _EtherBufferDrops_Type()
)
etherBufferDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherBufferDrops.setStatus("mandatory")
_EtherCollisions_Type = Counter32
_EtherCollisions_Object = MibScalar
etherCollisions = _EtherCollisions_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 17),
    _EtherCollisions_Type()
)
etherCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherCollisions.setStatus("mandatory")
_EtherDefers_Type = Counter32
_EtherDefers_Object = MibScalar
etherDefers = _EtherDefers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 18),
    _EtherDefers_Type()
)
etherDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherDefers.setStatus("mandatory")
_EtherDMAUnderruns_Type = Counter32
_EtherDMAUnderruns_Object = MibScalar
etherDMAUnderruns = _EtherDMAUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 19),
    _EtherDMAUnderruns_Type()
)
etherDMAUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherDMAUnderruns.setStatus("mandatory")
_EtherMaxCollisions_Type = Counter32
_EtherMaxCollisions_Object = MibScalar
etherMaxCollisions = _EtherMaxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 20),
    _EtherMaxCollisions_Type()
)
etherMaxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherMaxCollisions.setStatus("mandatory")
_EtherNoCarriers_Type = Counter32
_EtherNoCarriers_Object = MibScalar
etherNoCarriers = _EtherNoCarriers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 21),
    _EtherNoCarriers_Type()
)
etherNoCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherNoCarriers.setStatus("mandatory")
_EtherNoCTS_Type = Counter32
_EtherNoCTS_Object = MibScalar
etherNoCTS = _EtherNoCTS_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 22),
    _EtherNoCTS_Type()
)
etherNoCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherNoCTS.setStatus("mandatory")
_EtherNoSQEs_Type = Counter32
_EtherNoSQEs_Object = MibScalar
etherNoSQEs = _EtherNoSQEs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 3, 23),
    _EtherNoSQEs_Type()
)
etherNoSQEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherNoSQEs.setStatus("mandatory")
_Aarp_ObjectIdentity = ObjectIdentity
aarp = _Aarp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 4)
)
_AarpTable_Object = MibTable
aarpTable = _AarpTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 4, 1)
)
if mibBuilder.loadTexts:
    aarpTable.setStatus("mandatory")
_AarpEntry_Object = MibTableRow
aarpEntry = _AarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 4, 1, 1)
)
if mibBuilder.loadTexts:
    aarpEntry.setStatus("mandatory")
_AarpIfIndex_Type = Integer32
_AarpIfIndex_Object = MibTableColumn
aarpIfIndex = _AarpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 4, 1, 1, 1),
    _AarpIfIndex_Type()
)
aarpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aarpIfIndex.setStatus("mandatory")
_AarpPhysAddress_Type = OctetString
_AarpPhysAddress_Object = MibTableColumn
aarpPhysAddress = _AarpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 4, 1, 1, 2),
    _AarpPhysAddress_Type()
)
aarpPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aarpPhysAddress.setStatus("mandatory")
_AarpNetAddress_Type = OctetString
_AarpNetAddress_Object = MibTableColumn
aarpNetAddress = _AarpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 4, 1, 1, 3),
    _AarpNetAddress_Type()
)
aarpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aarpNetAddress.setStatus("mandatory")
_Atif_ObjectIdentity = ObjectIdentity
atif = _Atif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5)
)
_AtifTable_Object = MibTable
atifTable = _AtifTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1)
)
if mibBuilder.loadTexts:
    atifTable.setStatus("mandatory")
_AtifEntry_Object = MibTableRow
atifEntry = _AtifEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1)
)
if mibBuilder.loadTexts:
    atifEntry.setStatus("mandatory")
_AtifIndex_Type = Integer32
_AtifIndex_Object = MibTableColumn
atifIndex = _AtifIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 1),
    _AtifIndex_Type()
)
atifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atifIndex.setStatus("mandatory")
_AtifDescr_Type = OctetString
_AtifDescr_Object = MibTableColumn
atifDescr = _AtifDescr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 2),
    _AtifDescr_Type()
)
atifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atifDescr.setStatus("mandatory")


class _AtifType_Type(Integer32):
    """Custom type atifType based on Integer32"""
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
        *(("ethertalk1", 3),
          ("ethertalk2", 4),
          ("iptalk", 6),
          ("localtalk", 2),
          ("other", 1),
          ("tokentalk", 5))
    )


_AtifType_Type.__name__ = "Integer32"
_AtifType_Object = MibTableColumn
atifType = _AtifType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 3),
    _AtifType_Type()
)
atifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atifType.setStatus("mandatory")
_AtifNetStart_Type = OctetString
_AtifNetStart_Object = MibTableColumn
atifNetStart = _AtifNetStart_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 4),
    _AtifNetStart_Type()
)
atifNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atifNetStart.setStatus("mandatory")
_AtifNetEnd_Type = OctetString
_AtifNetEnd_Object = MibTableColumn
atifNetEnd = _AtifNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 5),
    _AtifNetEnd_Type()
)
atifNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atifNetEnd.setStatus("mandatory")
_AtifNetAddress_Type = OctetString
_AtifNetAddress_Object = MibTableColumn
atifNetAddress = _AtifNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 6),
    _AtifNetAddress_Type()
)
atifNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atifNetAddress.setStatus("mandatory")
_AtifStatus_Type = Integer32
_AtifStatus_Object = MibTableColumn
atifStatus = _AtifStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 7),
    _AtifStatus_Type()
)
atifStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atifStatus.setStatus("mandatory")


class _AtifNetConfig_Type(Integer32):
    """Custom type atifNetConfig based on Integer32"""
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
        *(("configured", 1),
          ("garnered", 2),
          ("guessed", 3),
          ("unconfigured", 4))
    )


_AtifNetConfig_Type.__name__ = "Integer32"
_AtifNetConfig_Object = MibTableColumn
atifNetConfig = _AtifNetConfig_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 8),
    _AtifNetConfig_Type()
)
atifNetConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atifNetConfig.setStatus("mandatory")


class _AtifZoneConfig_Type(Integer32):
    """Custom type atifZoneConfig based on Integer32"""
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
        *(("configured", 1),
          ("garnered", 2),
          ("guessed", 3),
          ("unconfigured", 4))
    )


_AtifZoneConfig_Type.__name__ = "Integer32"
_AtifZoneConfig_Object = MibTableColumn
atifZoneConfig = _AtifZoneConfig_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 9),
    _AtifZoneConfig_Type()
)
atifZoneConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atifZoneConfig.setStatus("mandatory")
_AtifZone_Type = OctetString
_AtifZone_Object = MibTableColumn
atifZone = _AtifZone_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 10),
    _AtifZone_Type()
)
atifZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atifZone.setStatus("mandatory")
_AtifIfIndex_Type = Integer32
_AtifIfIndex_Object = MibTableColumn
atifIfIndex = _AtifIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 5, 1, 1, 11),
    _AtifIfIndex_Type()
)
atifIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atifIfIndex.setStatus("mandatory")
_Ddp_ObjectIdentity = ObjectIdentity
ddp = _Ddp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6)
)
_DdpOutRequests_Type = Counter32
_DdpOutRequests_Object = MibScalar
ddpOutRequests = _DdpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 1),
    _DdpOutRequests_Type()
)
ddpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutRequests.setStatus("mandatory")
_DdpOutShort_Type = Counter32
_DdpOutShort_Object = MibScalar
ddpOutShort = _DdpOutShort_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 2),
    _DdpOutShort_Type()
)
ddpOutShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutShort.setStatus("mandatory")
_DdpOutLong_Type = Counter32
_DdpOutLong_Object = MibScalar
ddpOutLong = _DdpOutLong_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 3),
    _DdpOutLong_Type()
)
ddpOutLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutLong.setStatus("mandatory")
_DdpReceived_Type = Counter32
_DdpReceived_Object = MibScalar
ddpReceived = _DdpReceived_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 4),
    _DdpReceived_Type()
)
ddpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpReceived.setStatus("mandatory")
_DdpToForward_Type = Counter32
_DdpToForward_Object = MibScalar
ddpToForward = _DdpToForward_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 5),
    _DdpToForward_Type()
)
ddpToForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpToForward.setStatus("mandatory")
_DdpForwards_Type = Counter32
_DdpForwards_Object = MibScalar
ddpForwards = _DdpForwards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 6),
    _DdpForwards_Type()
)
ddpForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpForwards.setStatus("mandatory")
_DdpForMe_Type = Counter32
_DdpForMe_Object = MibScalar
ddpForMe = _DdpForMe_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 7),
    _DdpForMe_Type()
)
ddpForMe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpForMe.setStatus("mandatory")
_DdpOutNoRoutes_Type = Counter32
_DdpOutNoRoutes_Object = MibScalar
ddpOutNoRoutes = _DdpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 9),
    _DdpOutNoRoutes_Type()
)
ddpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpOutNoRoutes.setStatus("mandatory")
_DdpTooShortDrops_Type = Counter32
_DdpTooShortDrops_Object = MibScalar
ddpTooShortDrops = _DdpTooShortDrops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 10),
    _DdpTooShortDrops_Type()
)
ddpTooShortDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpTooShortDrops.setStatus("mandatory")
_DdpTooLongDrops_Type = Counter32
_DdpTooLongDrops_Object = MibScalar
ddpTooLongDrops = _DdpTooLongDrops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 11),
    _DdpTooLongDrops_Type()
)
ddpTooLongDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpTooLongDrops.setStatus("mandatory")
_DdpBroadcastDrops_Type = Counter32
_DdpBroadcastDrops_Object = MibScalar
ddpBroadcastDrops = _DdpBroadcastDrops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 12),
    _DdpBroadcastDrops_Type()
)
ddpBroadcastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpBroadcastDrops.setStatus("mandatory")
_DdpShortDDPDrops_Type = Counter32
_DdpShortDDPDrops_Object = MibScalar
ddpShortDDPDrops = _DdpShortDDPDrops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 13),
    _DdpShortDDPDrops_Type()
)
ddpShortDDPDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpShortDDPDrops.setStatus("mandatory")
_DdpHopCountDrops_Type = Counter32
_DdpHopCountDrops_Object = MibScalar
ddpHopCountDrops = _DdpHopCountDrops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 6, 14),
    _DdpHopCountDrops_Type()
)
ddpHopCountDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddpHopCountDrops.setStatus("mandatory")
_Rtmp_ObjectIdentity = ObjectIdentity
rtmp = _Rtmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 7)
)
_RtmpTable_Object = MibTable
rtmpTable = _RtmpTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1)
)
if mibBuilder.loadTexts:
    rtmpTable.setStatus("mandatory")
_RtmpEntry_Object = MibTableRow
rtmpEntry = _RtmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1)
)
if mibBuilder.loadTexts:
    rtmpEntry.setStatus("mandatory")
_RtmpRangeStart_Type = OctetString
_RtmpRangeStart_Object = MibTableColumn
rtmpRangeStart = _RtmpRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 1),
    _RtmpRangeStart_Type()
)
rtmpRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpRangeStart.setStatus("mandatory")
_RtmpRangeEnd_Type = OctetString
_RtmpRangeEnd_Object = MibTableColumn
rtmpRangeEnd = _RtmpRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 2),
    _RtmpRangeEnd_Type()
)
rtmpRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpRangeEnd.setStatus("mandatory")
_RtmpNextHop_Type = OctetString
_RtmpNextHop_Object = MibTableColumn
rtmpNextHop = _RtmpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 3),
    _RtmpNextHop_Type()
)
rtmpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpNextHop.setStatus("mandatory")
_RtmpInterface_Type = Integer32
_RtmpInterface_Object = MibTableColumn
rtmpInterface = _RtmpInterface_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 4),
    _RtmpInterface_Type()
)
rtmpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpInterface.setStatus("mandatory")
_RtmpHops_Type = Integer32
_RtmpHops_Object = MibTableColumn
rtmpHops = _RtmpHops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 5),
    _RtmpHops_Type()
)
rtmpHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpHops.setStatus("mandatory")


class _RtmpState_Type(Integer32):
    """Custom type rtmpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 3),
          ("good", 1),
          ("suspect", 2))
    )


_RtmpState_Type.__name__ = "Integer32"
_RtmpState_Object = MibTableColumn
rtmpState = _RtmpState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 7, 1, 1, 6),
    _RtmpState_Type()
)
rtmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtmpState.setStatus("mandatory")
_Kip_ObjectIdentity = ObjectIdentity
kip = _Kip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 8)
)
_KipTable_Object = MibTable
kipTable = _KipTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1)
)
if mibBuilder.loadTexts:
    kipTable.setStatus("mandatory")
_KipEntry_Object = MibTableRow
kipEntry = _KipEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1)
)
if mibBuilder.loadTexts:
    kipEntry.setStatus("mandatory")
_KipNet_Type = OctetString
_KipNet_Object = MibTableColumn
kipNet = _KipNet_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 1),
    _KipNet_Type()
)
kipNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipNet.setStatus("mandatory")
_KipNextHop_Type = IpAddress
_KipNextHop_Object = MibTableColumn
kipNextHop = _KipNextHop_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 2),
    _KipNextHop_Type()
)
kipNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipNextHop.setStatus("mandatory")
_KipHopCount_Type = Integer32
_KipHopCount_Object = MibTableColumn
kipHopCount = _KipHopCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 3),
    _KipHopCount_Type()
)
kipHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipHopCount.setStatus("mandatory")
_KipBCastAddr_Type = IpAddress
_KipBCastAddr_Object = MibTableColumn
kipBCastAddr = _KipBCastAddr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 4),
    _KipBCastAddr_Type()
)
kipBCastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipBCastAddr.setStatus("mandatory")


class _KipCore_Type(Integer32):
    """Custom type kipCore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("core", 1),
          ("notcore", 2))
    )


_KipCore_Type.__name__ = "Integer32"
_KipCore_Object = MibTableColumn
kipCore = _KipCore_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 5),
    _KipCore_Type()
)
kipCore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipCore.setStatus("mandatory")
_KipKfps_Type = Integer32
_KipKfps_Object = MibTableColumn
kipKfps = _KipKfps_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 8, 1, 1, 6),
    _KipKfps_Type()
)
kipKfps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kipKfps.setStatus("mandatory")
_Zip_ObjectIdentity = ObjectIdentity
zip = _Zip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 9)
)
_ZipTable_Object = MibTable
zipTable = _ZipTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1)
)
if mibBuilder.loadTexts:
    zipTable.setStatus("mandatory")
_ZipEntry_Object = MibTableRow
zipEntry = _ZipEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1, 1)
)
if mibBuilder.loadTexts:
    zipEntry.setStatus("mandatory")
_ZipZoneName_Type = OctetString
_ZipZoneName_Object = MibTableColumn
zipZoneName = _ZipZoneName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1, 1, 1),
    _ZipZoneName_Type()
)
zipZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zipZoneName.setStatus("mandatory")
_ZipZoneIndex_Type = Integer32
_ZipZoneIndex_Object = MibTableColumn
zipZoneIndex = _ZipZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1, 1, 2),
    _ZipZoneIndex_Type()
)
zipZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zipZoneIndex.setStatus("mandatory")
_ZipZoneNetStart_Type = OctetString
_ZipZoneNetStart_Object = MibScalar
zipZoneNetStart = _ZipZoneNetStart_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1, 1, 3),
    _ZipZoneNetStart_Type()
)
zipZoneNetStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zipZoneNetStart.setStatus("mandatory")
_ZipZoneNetEnd_Type = OctetString
_ZipZoneNetEnd_Object = MibScalar
zipZoneNetEnd = _ZipZoneNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 9, 1, 1, 4),
    _ZipZoneNetEnd_Type()
)
zipZoneNetEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zipZoneNetEnd.setStatus("mandatory")
_Nbp_ObjectIdentity = ObjectIdentity
nbp = _Nbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 10)
)
_NbpTable_Object = MibTable
nbpTable = _NbpTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1)
)
if mibBuilder.loadTexts:
    nbpTable.setStatus("mandatory")
_NbpEntry_Object = MibTableRow
nbpEntry = _NbpEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1, 1)
)
if mibBuilder.loadTexts:
    nbpEntry.setStatus("mandatory")
_NbpIndex_Type = Integer32
_NbpIndex_Object = MibTableColumn
nbpIndex = _NbpIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1, 1, 1),
    _NbpIndex_Type()
)
nbpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbpIndex.setStatus("mandatory")
_NbpObject_Type = OctetString
_NbpObject_Object = MibTableColumn
nbpObject = _NbpObject_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1, 1, 2),
    _NbpObject_Type()
)
nbpObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpObject.setStatus("mandatory")
_NbpType_Type = OctetString
_NbpType_Object = MibTableColumn
nbpType = _NbpType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1, 1, 3),
    _NbpType_Type()
)
nbpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpType.setStatus("mandatory")
_NbpZone_Type = OctetString
_NbpZone_Object = MibTableColumn
nbpZone = _NbpZone_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 10, 1, 1, 4),
    _NbpZone_Type()
)
nbpZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbpZone.setStatus("mandatory")
_Echo_ObjectIdentity = ObjectIdentity
echo = _Echo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 11)
)
_EchoRequests_Type = Counter32
_EchoRequests_Object = MibScalar
echoRequests = _EchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 11, 1),
    _EchoRequests_Type()
)
echoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoRequests.setStatus("mandatory")
_EchoReplies_Type = Counter32
_EchoReplies_Object = MibScalar
echoReplies = _EchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 11, 2),
    _EchoReplies_Type()
)
echoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echoReplies.setStatus("mandatory")
_Buffer_ObjectIdentity = ObjectIdentity
buffer = _Buffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 12)
)
_BufferSize_Type = Integer32
_BufferSize_Object = MibScalar
bufferSize = _BufferSize_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 1),
    _BufferSize_Type()
)
bufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSize.setStatus("mandatory")
_BufferAvail_Type = Integer32
_BufferAvail_Object = MibScalar
bufferAvail = _BufferAvail_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 2),
    _BufferAvail_Type()
)
bufferAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferAvail.setStatus("mandatory")
_BufferDrops_Type = Counter32
_BufferDrops_Object = MibScalar
bufferDrops = _BufferDrops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 3),
    _BufferDrops_Type()
)
bufferDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferDrops.setStatus("mandatory")
_BufferTypeTable_Object = MibTable
bufferTypeTable = _BufferTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4)
)
if mibBuilder.loadTexts:
    bufferTypeTable.setStatus("mandatory")
_BufferTypeEntry_Object = MibTableRow
bufferTypeEntry = _BufferTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4, 1)
)
if mibBuilder.loadTexts:
    bufferTypeEntry.setStatus("mandatory")
_BufferTypeIndex_Type = Integer32
_BufferTypeIndex_Object = MibTableColumn
bufferTypeIndex = _BufferTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4, 1, 1),
    _BufferTypeIndex_Type()
)
bufferTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeIndex.setStatus("mandatory")


class _BufferType_Type(Integer32):
    """Custom type bufferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("arp", 5),
          ("data", 6),
          ("erbf", 7),
          ("etbf", 8),
          ("ethernet", 4),
          ("free", 2),
          ("localtalk", 3),
          ("malloc", 9),
          ("other", 1),
          ("tkbf", 10),
          ("token", 11))
    )


_BufferType_Type.__name__ = "Integer32"
_BufferType_Object = MibTableColumn
bufferType = _BufferType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4, 1, 2),
    _BufferType_Type()
)
bufferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferType.setStatus("mandatory")
_BufferTypeDescr_Type = OctetString
_BufferTypeDescr_Object = MibTableColumn
bufferTypeDescr = _BufferTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4, 1, 3),
    _BufferTypeDescr_Type()
)
bufferTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeDescr.setStatus("mandatory")
_BufferTypeCount_Type = Integer32
_BufferTypeCount_Object = MibTableColumn
bufferTypeCount = _BufferTypeCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 11, 12, 4, 1, 4),
    _BufferTypeCount_Type()
)
bufferTypeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferTypeCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-MIB",
    **{"excelan": excelan,
       "genericGroup": genericGroup,
       "fastpathMib": fastpathMib,
       "scc": scc,
       "sccInterruptCount": sccInterruptCount,
       "sccAbortCount": sccAbortCount,
       "sccSpuriousCount": sccSpuriousCount,
       "sccCRCCount": sccCRCCount,
       "sccOverrunCount": sccOverrunCount,
       "sccUnderrunCount": sccUnderrunCount,
       "alap": alap,
       "alapReceiveCount": alapReceiveCount,
       "alapTransmitCount": alapTransmitCount,
       "alapNoHandlerCount": alapNoHandlerCount,
       "alapLengthErrorCount": alapLengthErrorCount,
       "alapBadCount": alapBadCount,
       "alapCollisionCount": alapCollisionCount,
       "alapDeferCount": alapDeferCount,
       "alapNoDataCount": alapNoDataCount,
       "alapRandomCTS": alapRandomCTS,
       "ethernet": ethernet,
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
       "etherSpurUnknown": etherSpurUnknown,
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
       "etherNoCTS": etherNoCTS,
       "etherNoSQEs": etherNoSQEs,
       "aarp": aarp,
       "aarpTable": aarpTable,
       "aarpEntry": aarpEntry,
       "aarpIfIndex": aarpIfIndex,
       "aarpPhysAddress": aarpPhysAddress,
       "aarpNetAddress": aarpNetAddress,
       "atif": atif,
       "atifTable": atifTable,
       "atifEntry": atifEntry,
       "atifIndex": atifIndex,
       "atifDescr": atifDescr,
       "atifType": atifType,
       "atifNetStart": atifNetStart,
       "atifNetEnd": atifNetEnd,
       "atifNetAddress": atifNetAddress,
       "atifStatus": atifStatus,
       "atifNetConfig": atifNetConfig,
       "atifZoneConfig": atifZoneConfig,
       "atifZone": atifZone,
       "atifIfIndex": atifIfIndex,
       "ddp": ddp,
       "ddpOutRequests": ddpOutRequests,
       "ddpOutShort": ddpOutShort,
       "ddpOutLong": ddpOutLong,
       "ddpReceived": ddpReceived,
       "ddpToForward": ddpToForward,
       "ddpForwards": ddpForwards,
       "ddpForMe": ddpForMe,
       "ddpOutNoRoutes": ddpOutNoRoutes,
       "ddpTooShortDrops": ddpTooShortDrops,
       "ddpTooLongDrops": ddpTooLongDrops,
       "ddpBroadcastDrops": ddpBroadcastDrops,
       "ddpShortDDPDrops": ddpShortDDPDrops,
       "ddpHopCountDrops": ddpHopCountDrops,
       "rtmp": rtmp,
       "rtmpTable": rtmpTable,
       "rtmpEntry": rtmpEntry,
       "rtmpRangeStart": rtmpRangeStart,
       "rtmpRangeEnd": rtmpRangeEnd,
       "rtmpNextHop": rtmpNextHop,
       "rtmpInterface": rtmpInterface,
       "rtmpHops": rtmpHops,
       "rtmpState": rtmpState,
       "kip": kip,
       "kipTable": kipTable,
       "kipEntry": kipEntry,
       "kipNet": kipNet,
       "kipNextHop": kipNextHop,
       "kipHopCount": kipHopCount,
       "kipBCastAddr": kipBCastAddr,
       "kipCore": kipCore,
       "kipKfps": kipKfps,
       "zip": zip,
       "zipTable": zipTable,
       "zipEntry": zipEntry,
       "zipZoneName": zipZoneName,
       "zipZoneIndex": zipZoneIndex,
       "zipZoneNetStart": zipZoneNetStart,
       "zipZoneNetEnd": zipZoneNetEnd,
       "nbp": nbp,
       "nbpTable": nbpTable,
       "nbpEntry": nbpEntry,
       "nbpIndex": nbpIndex,
       "nbpObject": nbpObject,
       "nbpType": nbpType,
       "nbpZone": nbpZone,
       "echo": echo,
       "echoRequests": echoRequests,
       "echoReplies": echoReplies,
       "buffer": buffer,
       "bufferSize": bufferSize,
       "bufferAvail": bufferAvail,
       "bufferDrops": bufferDrops,
       "bufferTypeTable": bufferTypeTable,
       "bufferTypeEntry": bufferTypeEntry,
       "bufferTypeIndex": bufferTypeIndex,
       "bufferType": bufferType,
       "bufferTypeDescr": bufferTypeDescr,
       "bufferTypeCount": bufferTypeCount}
)
