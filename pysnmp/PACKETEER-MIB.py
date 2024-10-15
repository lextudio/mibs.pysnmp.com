# SNMP MIB module (PACKETEER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKETEER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:02 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Packeteer_ObjectIdentity = ObjectIdentity
packeteer = _Packeteer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1)
)
_PacketShaper_ObjectIdentity = ObjectIdentity
packetShaper = _PacketShaper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1)
)
_PacketShaper_2000_ObjectIdentity = ObjectIdentity
packetShaper_2000 = _PacketShaper_2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 1)
)
_PacketShaper_4000_ObjectIdentity = ObjectIdentity
packetShaper_4000 = _PacketShaper_4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 2)
)
_PacketShaper_1000_ObjectIdentity = ObjectIdentity
packetShaper_1000 = _PacketShaper_1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 3)
)
_PacketShaper_2500_ObjectIdentity = ObjectIdentity
packetShaper_2500 = _PacketShaper_2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 4)
)
_PacketShaper_4500_ObjectIdentity = ObjectIdentity
packetShaper_4500 = _PacketShaper_4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 5)
)
_PacketShaper_1500_ObjectIdentity = ObjectIdentity
packetShaper_1500 = _PacketShaper_1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 6)
)
_PacketShaper_asm50_ObjectIdentity = ObjectIdentity
packetShaper_asm50 = _PacketShaper_asm50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 7)
)
_PacketShaper_asm70_ObjectIdentity = ObjectIdentity
packetShaper_asm70 = _PacketShaper_asm70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 8)
)
_PacketShaper_asm30_ObjectIdentity = ObjectIdentity
packetShaper_asm30 = _PacketShaper_asm30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 9)
)
_PacketShaper_asm90_ObjectIdentity = ObjectIdentity
packetShaper_asm90 = _PacketShaper_asm90_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 10)
)
_PacketShaper_6500_ObjectIdentity = ObjectIdentity
packetShaper_6500 = _PacketShaper_6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 11)
)
_PacketShaper_8500_ObjectIdentity = ObjectIdentity
packetShaper_8500 = _PacketShaper_8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 12)
)
_PacketShaper_asm110_ObjectIdentity = ObjectIdentity
packetShaper_asm110 = _PacketShaper_asm110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 13)
)
_PacketShaper_1550_ObjectIdentity = ObjectIdentity
packetShaper_1550 = _PacketShaper_1550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 14)
)
_PacketShaper_9500_ObjectIdentity = ObjectIdentity
packetShaper_9500 = _PacketShaper_9500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 15)
)
_PacketShaper_2550_ObjectIdentity = ObjectIdentity
packetShaper_2550 = _PacketShaper_2550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 16)
)
_PacketShaper_10000_ObjectIdentity = ObjectIdentity
packetShaper_10000 = _PacketShaper_10000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 17)
)
_PacketeerMibs_ObjectIdentity = ObjectIdentity
packeteerMibs = _PacketeerMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2)
)
_PsCommonMib_ObjectIdentity = ObjectIdentity
psCommonMib = _PsCommonMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1)
)
_PsSettings_ObjectIdentity = ObjectIdentity
psSettings = _PsSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 1)
)


class _PsShapingStatusOper_Type(Integer32):
    """Custom type psShapingStatusOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("ok", 1))
    )


_PsShapingStatusOper_Type.__name__ = "Integer32"
_PsShapingStatusOper_Object = MibScalar
psShapingStatusOper = _PsShapingStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 1, 1),
    _PsShapingStatusOper_Type()
)
psShapingStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psShapingStatusOper.setStatus("mandatory")
_PsLinks_ObjectIdentity = ObjectIdentity
psLinks = _PsLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2)
)
_LinkTableSize_Type = Integer32
_LinkTableSize_Object = MibScalar
linkTableSize = _LinkTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 1),
    _LinkTableSize_Type()
)
linkTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTableSize.setStatus("mandatory")
_LinkTable_Object = MibTable
linkTable = _LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    linkTable.setStatus("mandatory")
_LinkEntry_Object = MibTableRow
linkEntry = _LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1)
)
linkEntry.setIndexNames(
    (0, "PACKETEER-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkEntry.setStatus("mandatory")
_LinkIndex_Type = Integer32
_LinkIndex_Object = MibTableColumn
linkIndex = _LinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 1),
    _LinkIndex_Type()
)
linkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIndex.setStatus("mandatory")
_LinkName_Type = DisplayString
_LinkName_Object = MibTableColumn
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 2),
    _LinkName_Type()
)
linkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkName.setStatus("mandatory")
_LinkByteCount_Type = Counter32
_LinkByteCount_Object = MibTableColumn
linkByteCount = _LinkByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 3),
    _LinkByteCount_Type()
)
linkByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkByteCount.setStatus("mandatory")
_LinkByteCountHi_Type = Counter32
_LinkByteCountHi_Object = MibTableColumn
linkByteCountHi = _LinkByteCountHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 4),
    _LinkByteCountHi_Type()
)
linkByteCountHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkByteCountHi.setStatus("mandatory")
_LinkPkts_Type = Counter32
_LinkPkts_Object = MibTableColumn
linkPkts = _LinkPkts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 5),
    _LinkPkts_Type()
)
linkPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPkts.setStatus("mandatory")
_LinkDataPkts_Type = Counter32
_LinkDataPkts_Object = MibTableColumn
linkDataPkts = _LinkDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 6),
    _LinkDataPkts_Type()
)
linkDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDataPkts.setStatus("mandatory")
_LinkReTxs_Type = Counter32
_LinkReTxs_Object = MibTableColumn
linkReTxs = _LinkReTxs_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 7),
    _LinkReTxs_Type()
)
linkReTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkReTxs.setStatus("mandatory")
_LinkReTxTosses_Type = Counter32
_LinkReTxTosses_Object = MibTableColumn
linkReTxTosses = _LinkReTxTosses_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 8),
    _LinkReTxTosses_Type()
)
linkReTxTosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkReTxTosses.setStatus("mandatory")
_LinkCirFails_Type = Counter32
_LinkCirFails_Object = MibTableColumn
linkCirFails = _LinkCirFails_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 9),
    _LinkCirFails_Type()
)
linkCirFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCirFails.setStatus("mandatory")
_LinkCirAllocs_Type = Counter32
_LinkCirAllocs_Object = MibTableColumn
linkCirAllocs = _LinkCirAllocs_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 10),
    _LinkCirAllocs_Type()
)
linkCirAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCirAllocs.setStatus("mandatory")
_LinkEirAllocs_Type = Counter32
_LinkEirAllocs_Object = MibTableColumn
linkEirAllocs = _LinkEirAllocs_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 11),
    _LinkEirAllocs_Type()
)
linkEirAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkEirAllocs.setStatus("mandatory")
_LinkPeakTcpConns_Type = Gauge32
_LinkPeakTcpConns_Object = MibTableColumn
linkPeakTcpConns = _LinkPeakTcpConns_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 12),
    _LinkPeakTcpConns_Type()
)
linkPeakTcpConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeakTcpConns.setStatus("mandatory")
_LinkTcpConnInits_Type = Counter32
_LinkTcpConnInits_Object = MibTableColumn
linkTcpConnInits = _LinkTcpConnInits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 13),
    _LinkTcpConnInits_Type()
)
linkTcpConnInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTcpConnInits.setStatus("mandatory")
_LinkTcpConnExits_Type = Counter32
_LinkTcpConnExits_Object = MibTableColumn
linkTcpConnExits = _LinkTcpConnExits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 14),
    _LinkTcpConnExits_Type()
)
linkTcpConnExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTcpConnExits.setStatus("mandatory")
_LinkTcpConnRefuses_Type = Counter32
_LinkTcpConnRefuses_Object = MibTableColumn
linkTcpConnRefuses = _LinkTcpConnRefuses_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 15),
    _LinkTcpConnRefuses_Type()
)
linkTcpConnRefuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTcpConnRefuses.setStatus("mandatory")
_LinkTcpConnIgnores_Type = Counter32
_LinkTcpConnIgnores_Object = MibTableColumn
linkTcpConnIgnores = _LinkTcpConnIgnores_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 16),
    _LinkTcpConnIgnores_Type()
)
linkTcpConnIgnores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTcpConnIgnores.setStatus("mandatory")
_LinkTcpConnAborts_Type = Counter32
_LinkTcpConnAborts_Object = MibTableColumn
linkTcpConnAborts = _LinkTcpConnAborts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 17),
    _LinkTcpConnAborts_Type()
)
linkTcpConnAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTcpConnAborts.setStatus("mandatory")
_LinkTcpConnDenies_Type = Counter32
_LinkTcpConnDenies_Object = MibTableColumn
linkTcpConnDenies = _LinkTcpConnDenies_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 18),
    _LinkTcpConnDenies_Type()
)
linkTcpConnDenies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTcpConnDenies.setStatus("mandatory")
_LinkTcpConnTimeouts_Type = Counter32
_LinkTcpConnTimeouts_Object = MibTableColumn
linkTcpConnTimeouts = _LinkTcpConnTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 19),
    _LinkTcpConnTimeouts_Type()
)
linkTcpConnTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTcpConnTimeouts.setStatus("deprecated")
_LinkPeakUdpConns_Type = Gauge32
_LinkPeakUdpConns_Object = MibTableColumn
linkPeakUdpConns = _LinkPeakUdpConns_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 20),
    _LinkPeakUdpConns_Type()
)
linkPeakUdpConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeakUdpConns.setStatus("deprecated")
_LinkUdpConnInits_Type = Counter32
_LinkUdpConnInits_Object = MibTableColumn
linkUdpConnInits = _LinkUdpConnInits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 21),
    _LinkUdpConnInits_Type()
)
linkUdpConnInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkUdpConnInits.setStatus("deprecated")
_LinkUdpConnExits_Type = Counter32
_LinkUdpConnExits_Object = MibTableColumn
linkUdpConnExits = _LinkUdpConnExits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 22),
    _LinkUdpConnExits_Type()
)
linkUdpConnExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkUdpConnExits.setStatus("deprecated")
_LinkSize_Type = Integer32
_LinkSize_Object = MibTableColumn
linkSize = _LinkSize_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 23),
    _LinkSize_Type()
)
linkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSize.setStatus("mandatory")
_LinkRate_Type = Gauge32
_LinkRate_Object = MibTableColumn
linkRate = _LinkRate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 24),
    _LinkRate_Type()
)
linkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRate.setStatus("mandatory")
_LinkRateAllocations_Type = Gauge32
_LinkRateAllocations_Object = MibTableColumn
linkRateAllocations = _LinkRateAllocations_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 25),
    _LinkRateAllocations_Type()
)
linkRateAllocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRateAllocations.setStatus("mandatory")
_LinkPeakGuaranteedRateFlows_Type = Gauge32
_LinkPeakGuaranteedRateFlows_Object = MibTableColumn
linkPeakGuaranteedRateFlows = _LinkPeakGuaranteedRateFlows_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 26),
    _LinkPeakGuaranteedRateFlows_Type()
)
linkPeakGuaranteedRateFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeakGuaranteedRateFlows.setStatus("mandatory")
_LinkPeakRateFlows_Type = Gauge32
_LinkPeakRateFlows_Object = MibTableColumn
linkPeakRateFlows = _LinkPeakRateFlows_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 27),
    _LinkPeakRateFlows_Type()
)
linkPeakRateFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeakRateFlows.setStatus("mandatory")
_LinkReTxByteCount_Type = Counter32
_LinkReTxByteCount_Object = MibTableColumn
linkReTxByteCount = _LinkReTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 28),
    _LinkReTxByteCount_Type()
)
linkReTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkReTxByteCount.setStatus("mandatory")
_LinkReTxByteCountHi_Type = Counter32
_LinkReTxByteCountHi_Object = MibTableColumn
linkReTxByteCountHi = _LinkReTxByteCountHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 29),
    _LinkReTxByteCountHi_Type()
)
linkReTxByteCountHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkReTxByteCountHi.setStatus("mandatory")
_LinkTotalRxPkts_Type = Counter32
_LinkTotalRxPkts_Object = MibTableColumn
linkTotalRxPkts = _LinkTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 30),
    _LinkTotalRxPkts_Type()
)
linkTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTotalRxPkts.setStatus("mandatory")
_LinkTotalTxPkts_Type = Counter32
_LinkTotalTxPkts_Object = MibTableColumn
linkTotalTxPkts = _LinkTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 31),
    _LinkTotalTxPkts_Type()
)
linkTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTotalTxPkts.setStatus("mandatory")
_LinkRxNoBufs_Type = Counter32
_LinkRxNoBufs_Object = MibTableColumn
linkRxNoBufs = _LinkRxNoBufs_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 32),
    _LinkRxNoBufs_Type()
)
linkRxNoBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRxNoBufs.setStatus("mandatory")
_LinkRxPktDrops_Type = Counter32
_LinkRxPktDrops_Object = MibTableColumn
linkRxPktDrops = _LinkRxPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 33),
    _LinkRxPktDrops_Type()
)
linkRxPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRxPktDrops.setStatus("mandatory")
_LinkTxPktDrops_Type = Counter32
_LinkTxPktDrops_Object = MibTableColumn
linkTxPktDrops = _LinkTxPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 34),
    _LinkTxPktDrops_Type()
)
linkTxPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTxPktDrops.setStatus("mandatory")
_LinkRxErrors_Type = Counter32
_LinkRxErrors_Object = MibTableColumn
linkRxErrors = _LinkRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 35),
    _LinkRxErrors_Type()
)
linkRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkRxErrors.setStatus("mandatory")
_LinkTxErrors_Type = Counter32
_LinkTxErrors_Object = MibTableColumn
linkTxErrors = _LinkTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 36),
    _LinkTxErrors_Type()
)
linkTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTxErrors.setStatus("mandatory")
_LinkTcpAllocFails_Type = Counter32
_LinkTcpAllocFails_Object = MibTableColumn
linkTcpAllocFails = _LinkTcpAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 37),
    _LinkTcpAllocFails_Type()
)
linkTcpAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTcpAllocFails.setStatus("mandatory")
_LinkIpdgAllocFails_Type = Counter32
_LinkIpdgAllocFails_Object = MibTableColumn
linkIpdgAllocFails = _LinkIpdgAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 38),
    _LinkIpdgAllocFails_Type()
)
linkIpdgAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIpdgAllocFails.setStatus("mandatory")
_LinkHostdbAllocFails_Type = Counter32
_LinkHostdbAllocFails_Object = MibTableColumn
linkHostdbAllocFails = _LinkHostdbAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 39),
    _LinkHostdbAllocFails_Type()
)
linkHostdbAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkHostdbAllocFails.setStatus("mandatory")


class _LinkShapingMode_Type(Integer32):
    """Custom type linkShapingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("watch", 4))
    )


_LinkShapingMode_Type.__name__ = "Integer32"
_LinkShapingMode_Object = MibTableColumn
linkShapingMode = _LinkShapingMode_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 40),
    _LinkShapingMode_Type()
)
linkShapingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkShapingMode.setStatus("mandatory")


class _LinkAutoclassifyMode_Type(Integer32):
    """Custom type linkAutoclassifyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_LinkAutoclassifyMode_Type.__name__ = "Integer32"
_LinkAutoclassifyMode_Object = MibTableColumn
linkAutoclassifyMode = _LinkAutoclassifyMode_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 41),
    _LinkAutoclassifyMode_Type()
)
linkAutoclassifyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkAutoclassifyMode.setStatus("mandatory")
_LinkMacSameSidePkts_Type = Counter32
_LinkMacSameSidePkts_Object = MibTableColumn
linkMacSameSidePkts = _LinkMacSameSidePkts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 42),
    _LinkMacSameSidePkts_Type()
)
linkMacSameSidePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkMacSameSidePkts.setStatus("mandatory")
_LinkPassthruPkts_Type = Counter32
_LinkPassthruPkts_Object = MibTableColumn
linkPassthruPkts = _LinkPassthruPkts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 43),
    _LinkPassthruPkts_Type()
)
linkPassthruPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPassthruPkts.setStatus("mandatory")
_LinkTotalRxBytes_Type = Counter32
_LinkTotalRxBytes_Object = MibTableColumn
linkTotalRxBytes = _LinkTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 44),
    _LinkTotalRxBytes_Type()
)
linkTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTotalRxBytes.setStatus("mandatory")
_LinkTotalRxBytesHi_Type = Counter32
_LinkTotalRxBytesHi_Object = MibTableColumn
linkTotalRxBytesHi = _LinkTotalRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 45),
    _LinkTotalRxBytesHi_Type()
)
linkTotalRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTotalRxBytesHi.setStatus("mandatory")
_LinkTotalTxBytes_Type = Counter32
_LinkTotalTxBytes_Object = MibTableColumn
linkTotalTxBytes = _LinkTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 46),
    _LinkTotalTxBytes_Type()
)
linkTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTotalTxBytes.setStatus("mandatory")
_LinkTotalTxBytesHi_Type = Counter32
_LinkTotalTxBytesHi_Object = MibTableColumn
linkTotalTxBytesHi = _LinkTotalTxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 47),
    _LinkTotalTxBytesHi_Type()
)
linkTotalTxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTotalTxBytesHi.setStatus("mandatory")
_LinkClassChecks_Type = Counter32
_LinkClassChecks_Object = MibTableColumn
linkClassChecks = _LinkClassChecks_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 48),
    _LinkClassChecks_Type()
)
linkClassChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkClassChecks.setStatus("mandatory")
_LinkPassthruBytes_Type = Counter32
_LinkPassthruBytes_Object = MibTableColumn
linkPassthruBytes = _LinkPassthruBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 49),
    _LinkPassthruBytes_Type()
)
linkPassthruBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPassthruBytes.setStatus("mandatory")


class _LinkCompressionMode_Type(Integer32):
    """Custom type linkCompressionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_LinkCompressionMode_Type.__name__ = "Integer32"
_LinkCompressionMode_Object = MibTableColumn
linkCompressionMode = _LinkCompressionMode_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 50),
    _LinkCompressionMode_Type()
)
linkCompressionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCompressionMode.setStatus("mandatory")
_LinkPeakPreCompressionRate_Type = Gauge32
_LinkPeakPreCompressionRate_Object = MibTableColumn
linkPeakPreCompressionRate = _LinkPeakPreCompressionRate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 51),
    _LinkPeakPreCompressionRate_Type()
)
linkPeakPreCompressionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeakPreCompressionRate.setStatus("mandatory")
_LinkPeakPostCompressionRate_Type = Gauge32
_LinkPeakPostCompressionRate_Object = MibTableColumn
linkPeakPostCompressionRate = _LinkPeakPostCompressionRate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 52),
    _LinkPeakPostCompressionRate_Type()
)
linkPeakPostCompressionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPeakPostCompressionRate.setStatus("mandatory")
_LinkNonComprsnBytes_Type = Counter32
_LinkNonComprsnBytes_Object = MibTableColumn
linkNonComprsnBytes = _LinkNonComprsnBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 53),
    _LinkNonComprsnBytes_Type()
)
linkNonComprsnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNonComprsnBytes.setStatus("mandatory")
_LinkNonComprsnBytesHi_Type = Counter32
_LinkNonComprsnBytesHi_Object = MibTableColumn
linkNonComprsnBytesHi = _LinkNonComprsnBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 54),
    _LinkNonComprsnBytesHi_Type()
)
linkNonComprsnBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNonComprsnBytesHi.setStatus("mandatory")
_LinkPreComprsnBytes_Type = Counter32
_LinkPreComprsnBytes_Object = MibTableColumn
linkPreComprsnBytes = _LinkPreComprsnBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 55),
    _LinkPreComprsnBytes_Type()
)
linkPreComprsnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPreComprsnBytes.setStatus("mandatory")
_LinkPreComprsnBytesHi_Type = Counter32
_LinkPreComprsnBytesHi_Object = MibTableColumn
linkPreComprsnBytesHi = _LinkPreComprsnBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 56),
    _LinkPreComprsnBytesHi_Type()
)
linkPreComprsnBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPreComprsnBytesHi.setStatus("mandatory")
_LinkPostComprsnBytes_Type = Counter32
_LinkPostComprsnBytes_Object = MibTableColumn
linkPostComprsnBytes = _LinkPostComprsnBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 57),
    _LinkPostComprsnBytes_Type()
)
linkPostComprsnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPostComprsnBytes.setStatus("mandatory")
_LinkPostComprsnBytesHi_Type = Counter32
_LinkPostComprsnBytesHi_Object = MibTableColumn
linkPostComprsnBytesHi = _LinkPostComprsnBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 2, 2, 1, 58),
    _LinkPostComprsnBytesHi_Type()
)
linkPostComprsnBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkPostComprsnBytesHi.setStatus("mandatory")
_PsPartitions_ObjectIdentity = ObjectIdentity
psPartitions = _PsPartitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3)
)
_PartitionTableSize_Type = Integer32
_PartitionTableSize_Object = MibScalar
partitionTableSize = _PartitionTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 1),
    _PartitionTableSize_Type()
)
partitionTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionTableSize.setStatus("mandatory")
_PartitionTable_Object = MibTable
partitionTable = _PartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    partitionTable.setStatus("mandatory")
_PartitionEntry_Object = MibTableRow
partitionEntry = _PartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1)
)
partitionEntry.setIndexNames(
    (0, "PACKETEER-MIB", "partitionIndex"),
)
if mibBuilder.loadTexts:
    partitionEntry.setStatus("mandatory")
_PartitionIndex_Type = Integer32
_PartitionIndex_Object = MibTableColumn
partitionIndex = _PartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 1),
    _PartitionIndex_Type()
)
partitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionIndex.setStatus("mandatory")
_PartitionName_Type = DisplayString
_PartitionName_Object = MibTableColumn
partitionName = _PartitionName_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 2),
    _PartitionName_Type()
)
partitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionName.setStatus("mandatory")


class _PartitionLinkDirection_Type(Integer32):
    """Custom type partitionLinkDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-bound", 1),
          ("out-bound", 2))
    )


_PartitionLinkDirection_Type.__name__ = "Integer32"
_PartitionLinkDirection_Object = MibTableColumn
partitionLinkDirection = _PartitionLinkDirection_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 3),
    _PartitionLinkDirection_Type()
)
partitionLinkDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionLinkDirection.setStatus("mandatory")
_PartitionByteCount_Type = Counter32
_PartitionByteCount_Object = MibTableColumn
partitionByteCount = _PartitionByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 4),
    _PartitionByteCount_Type()
)
partitionByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionByteCount.setStatus("mandatory")
_PartitionByteCountHi_Type = Counter32
_PartitionByteCountHi_Object = MibTableColumn
partitionByteCountHi = _PartitionByteCountHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 5),
    _PartitionByteCountHi_Type()
)
partitionByteCountHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionByteCountHi.setStatus("mandatory")
_PartitionPkts_Type = Counter32
_PartitionPkts_Object = MibTableColumn
partitionPkts = _PartitionPkts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 6),
    _PartitionPkts_Type()
)
partitionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionPkts.setStatus("mandatory")
_PartitionDataPkts_Type = Counter32
_PartitionDataPkts_Object = MibTableColumn
partitionDataPkts = _PartitionDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 7),
    _PartitionDataPkts_Type()
)
partitionDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionDataPkts.setStatus("mandatory")
_PartitionReTxs_Type = Counter32
_PartitionReTxs_Object = MibTableColumn
partitionReTxs = _PartitionReTxs_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 8),
    _PartitionReTxs_Type()
)
partitionReTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionReTxs.setStatus("mandatory")
_PartitionReTxTosses_Type = Counter32
_PartitionReTxTosses_Object = MibTableColumn
partitionReTxTosses = _PartitionReTxTosses_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 9),
    _PartitionReTxTosses_Type()
)
partitionReTxTosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionReTxTosses.setStatus("mandatory")
_PartitionCirFails_Type = Counter32
_PartitionCirFails_Object = MibTableColumn
partitionCirFails = _PartitionCirFails_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 10),
    _PartitionCirFails_Type()
)
partitionCirFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionCirFails.setStatus("mandatory")
_PartitionCirAllocs_Type = Counter32
_PartitionCirAllocs_Object = MibTableColumn
partitionCirAllocs = _PartitionCirAllocs_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 11),
    _PartitionCirAllocs_Type()
)
partitionCirAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionCirAllocs.setStatus("mandatory")
_PartitionEirAllocs_Type = Counter32
_PartitionEirAllocs_Object = MibTableColumn
partitionEirAllocs = _PartitionEirAllocs_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 12),
    _PartitionEirAllocs_Type()
)
partitionEirAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionEirAllocs.setStatus("mandatory")
_PartitionPeakTcpConns_Type = Gauge32
_PartitionPeakTcpConns_Object = MibTableColumn
partitionPeakTcpConns = _PartitionPeakTcpConns_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 13),
    _PartitionPeakTcpConns_Type()
)
partitionPeakTcpConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionPeakTcpConns.setStatus("mandatory")
_PartitionTcpConnInits_Type = Counter32
_PartitionTcpConnInits_Object = MibTableColumn
partitionTcpConnInits = _PartitionTcpConnInits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 14),
    _PartitionTcpConnInits_Type()
)
partitionTcpConnInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionTcpConnInits.setStatus("mandatory")
_PartitionTcpConnExits_Type = Counter32
_PartitionTcpConnExits_Object = MibTableColumn
partitionTcpConnExits = _PartitionTcpConnExits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 15),
    _PartitionTcpConnExits_Type()
)
partitionTcpConnExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionTcpConnExits.setStatus("mandatory")
_PartitionTcpConnRefuses_Type = Counter32
_PartitionTcpConnRefuses_Object = MibTableColumn
partitionTcpConnRefuses = _PartitionTcpConnRefuses_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 16),
    _PartitionTcpConnRefuses_Type()
)
partitionTcpConnRefuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionTcpConnRefuses.setStatus("mandatory")
_PartitionTcpConnIgnores_Type = Counter32
_PartitionTcpConnIgnores_Object = MibTableColumn
partitionTcpConnIgnores = _PartitionTcpConnIgnores_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 17),
    _PartitionTcpConnIgnores_Type()
)
partitionTcpConnIgnores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionTcpConnIgnores.setStatus("mandatory")
_PartitionTcpConnAborts_Type = Counter32
_PartitionTcpConnAborts_Object = MibTableColumn
partitionTcpConnAborts = _PartitionTcpConnAborts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 18),
    _PartitionTcpConnAborts_Type()
)
partitionTcpConnAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionTcpConnAborts.setStatus("mandatory")
_PartitionTcpConnDenies_Type = Counter32
_PartitionTcpConnDenies_Object = MibTableColumn
partitionTcpConnDenies = _PartitionTcpConnDenies_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 19),
    _PartitionTcpConnDenies_Type()
)
partitionTcpConnDenies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionTcpConnDenies.setStatus("mandatory")
_PartitionTcpConnTimeouts_Type = Counter32
_PartitionTcpConnTimeouts_Object = MibTableColumn
partitionTcpConnTimeouts = _PartitionTcpConnTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 20),
    _PartitionTcpConnTimeouts_Type()
)
partitionTcpConnTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionTcpConnTimeouts.setStatus("deprecated")
_PartitionPeakUdpConns_Type = Gauge32
_PartitionPeakUdpConns_Object = MibTableColumn
partitionPeakUdpConns = _PartitionPeakUdpConns_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 21),
    _PartitionPeakUdpConns_Type()
)
partitionPeakUdpConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionPeakUdpConns.setStatus("deprecated")
_PartitionUdpConnInits_Type = Counter32
_PartitionUdpConnInits_Object = MibTableColumn
partitionUdpConnInits = _PartitionUdpConnInits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 22),
    _PartitionUdpConnInits_Type()
)
partitionUdpConnInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionUdpConnInits.setStatus("deprecated")
_PartitionUdpConnExits_Type = Counter32
_PartitionUdpConnExits_Object = MibTableColumn
partitionUdpConnExits = _PartitionUdpConnExits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 23),
    _PartitionUdpConnExits_Type()
)
partitionUdpConnExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionUdpConnExits.setStatus("deprecated")
_PartitionMinimumBps_Type = Integer32
_PartitionMinimumBps_Object = MibTableColumn
partitionMinimumBps = _PartitionMinimumBps_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 24),
    _PartitionMinimumBps_Type()
)
partitionMinimumBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionMinimumBps.setStatus("mandatory")
_PartitionBurstLimit_Type = Integer32
_PartitionBurstLimit_Object = MibTableColumn
partitionBurstLimit = _PartitionBurstLimit_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 25),
    _PartitionBurstLimit_Type()
)
partitionBurstLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionBurstLimit.setStatus("mandatory")
_PartitionRate_Type = Gauge32
_PartitionRate_Object = MibTableColumn
partitionRate = _PartitionRate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 26),
    _PartitionRate_Type()
)
partitionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionRate.setStatus("mandatory")
_PartitionCirRate_Type = Gauge32
_PartitionCirRate_Object = MibTableColumn
partitionCirRate = _PartitionCirRate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 27),
    _PartitionCirRate_Type()
)
partitionCirRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionCirRate.setStatus("mandatory")
_PartitionEirRate_Type = Gauge32
_PartitionEirRate_Object = MibTableColumn
partitionEirRate = _PartitionEirRate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 28),
    _PartitionEirRate_Type()
)
partitionEirRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionEirRate.setStatus("mandatory")
_PartitionUnreservedRate_Type = Gauge32
_PartitionUnreservedRate_Object = MibTableColumn
partitionUnreservedRate = _PartitionUnreservedRate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 29),
    _PartitionUnreservedRate_Type()
)
partitionUnreservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionUnreservedRate.setStatus("mandatory")
_PartitionFirstSatisfiedPriority_Type = Gauge32
_PartitionFirstSatisfiedPriority_Object = MibTableColumn
partitionFirstSatisfiedPriority = _PartitionFirstSatisfiedPriority_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 30),
    _PartitionFirstSatisfiedPriority_Type()
)
partitionFirstSatisfiedPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionFirstSatisfiedPriority.setStatus("mandatory")
_PartitionTimeOverLimit_Type = Counter32
_PartitionTimeOverLimit_Object = MibTableColumn
partitionTimeOverLimit = _PartitionTimeOverLimit_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 31),
    _PartitionTimeOverLimit_Type()
)
partitionTimeOverLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionTimeOverLimit.setStatus("mandatory")
_PartitionRateAllocations_Type = Counter32
_PartitionRateAllocations_Object = MibTableColumn
partitionRateAllocations = _PartitionRateAllocations_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 32),
    _PartitionRateAllocations_Type()
)
partitionRateAllocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionRateAllocations.setStatus("mandatory")
_PartitionPeakGuaranteedRateFlows_Type = Gauge32
_PartitionPeakGuaranteedRateFlows_Object = MibTableColumn
partitionPeakGuaranteedRateFlows = _PartitionPeakGuaranteedRateFlows_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 33),
    _PartitionPeakGuaranteedRateFlows_Type()
)
partitionPeakGuaranteedRateFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionPeakGuaranteedRateFlows.setStatus("mandatory")
_PartitionPeakRateFlows_Type = Gauge32
_PartitionPeakRateFlows_Object = MibTableColumn
partitionPeakRateFlows = _PartitionPeakRateFlows_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 34),
    _PartitionPeakRateFlows_Type()
)
partitionPeakRateFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionPeakRateFlows.setStatus("mandatory")
_PartitionReTxByteCount_Type = Counter32
_PartitionReTxByteCount_Object = MibTableColumn
partitionReTxByteCount = _PartitionReTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 35),
    _PartitionReTxByteCount_Type()
)
partitionReTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionReTxByteCount.setStatus("mandatory")
_PartitionReTxByteCountHi_Type = Counter32
_PartitionReTxByteCountHi_Object = MibTableColumn
partitionReTxByteCountHi = _PartitionReTxByteCountHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 36),
    _PartitionReTxByteCountHi_Type()
)
partitionReTxByteCountHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionReTxByteCountHi.setStatus("mandatory")
_PartitionDynamicCapCount_Type = Counter32
_PartitionDynamicCapCount_Object = MibTableColumn
partitionDynamicCapCount = _PartitionDynamicCapCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 37),
    _PartitionDynamicCapCount_Type()
)
partitionDynamicCapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionDynamicCapCount.setStatus("mandatory")
_PartitionDynamicNoCount_Type = Counter32
_PartitionDynamicNoCount_Object = MibTableColumn
partitionDynamicNoCount = _PartitionDynamicNoCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 38),
    _PartitionDynamicNoCount_Type()
)
partitionDynamicNoCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionDynamicNoCount.setStatus("mandatory")
_PartitionDynamicLiveUserCount_Type = Gauge32
_PartitionDynamicLiveUserCount_Object = MibTableColumn
partitionDynamicLiveUserCount = _PartitionDynamicLiveUserCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 39),
    _PartitionDynamicLiveUserCount_Type()
)
partitionDynamicLiveUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionDynamicLiveUserCount.setStatus("mandatory")
_PartitionCommittmentFailures_Type = Counter32
_PartitionCommittmentFailures_Object = MibTableColumn
partitionCommittmentFailures = _PartitionCommittmentFailures_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 40),
    _PartitionCommittmentFailures_Type()
)
partitionCommittmentFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionCommittmentFailures.setStatus("mandatory")
_PartitionLateDropPktCount_Type = Gauge32
_PartitionLateDropPktCount_Object = MibTableColumn
partitionLateDropPktCount = _PartitionLateDropPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 41),
    _PartitionLateDropPktCount_Type()
)
partitionLateDropPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionLateDropPktCount.setStatus("mandatory")
_PartitionLateDropPktCountHi_Type = Gauge32
_PartitionLateDropPktCountHi_Object = MibTableColumn
partitionLateDropPktCountHi = _PartitionLateDropPktCountHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 42),
    _PartitionLateDropPktCountHi_Type()
)
partitionLateDropPktCountHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionLateDropPktCountHi.setStatus("mandatory")
_PartitionLateDropByteCount_Type = Gauge32
_PartitionLateDropByteCount_Object = MibTableColumn
partitionLateDropByteCount = _PartitionLateDropByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 43),
    _PartitionLateDropByteCount_Type()
)
partitionLateDropByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionLateDropByteCount.setStatus("mandatory")
_PartitionLateDropByteCountHi_Type = Gauge32
_PartitionLateDropByteCountHi_Object = MibTableColumn
partitionLateDropByteCountHi = _PartitionLateDropByteCountHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 44),
    _PartitionLateDropByteCountHi_Type()
)
partitionLateDropByteCountHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionLateDropByteCountHi.setStatus("mandatory")
_PartitionSchedDropPktCount_Type = Gauge32
_PartitionSchedDropPktCount_Object = MibTableColumn
partitionSchedDropPktCount = _PartitionSchedDropPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 45),
    _PartitionSchedDropPktCount_Type()
)
partitionSchedDropPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionSchedDropPktCount.setStatus("mandatory")
_PartitionSchedDropPktCountHi_Type = Gauge32
_PartitionSchedDropPktCountHi_Object = MibTableColumn
partitionSchedDropPktCountHi = _PartitionSchedDropPktCountHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 46),
    _PartitionSchedDropPktCountHi_Type()
)
partitionSchedDropPktCountHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionSchedDropPktCountHi.setStatus("mandatory")
_PartitionSchedDropByteCount_Type = Gauge32
_PartitionSchedDropByteCount_Object = MibTableColumn
partitionSchedDropByteCount = _PartitionSchedDropByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 47),
    _PartitionSchedDropByteCount_Type()
)
partitionSchedDropByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionSchedDropByteCount.setStatus("mandatory")
_PartitionSchedDropByteCountHi_Type = Gauge32
_PartitionSchedDropByteCountHi_Object = MibTableColumn
partitionSchedDropByteCountHi = _PartitionSchedDropByteCountHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 48),
    _PartitionSchedDropByteCountHi_Type()
)
partitionSchedDropByteCountHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionSchedDropByteCountHi.setStatus("mandatory")
_PartitionFrameBytes_Type = Counter32
_PartitionFrameBytes_Object = MibTableColumn
partitionFrameBytes = _PartitionFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 49),
    _PartitionFrameBytes_Type()
)
partitionFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionFrameBytes.setStatus("mandatory")
_PartitionFrameBytesHi_Type = Counter32
_PartitionFrameBytesHi_Object = MibTableColumn
partitionFrameBytesHi = _PartitionFrameBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 50),
    _PartitionFrameBytesHi_Type()
)
partitionFrameBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionFrameBytesHi.setStatus("mandatory")
_PartitionFrameTargetRate_Type = Gauge32
_PartitionFrameTargetRate_Object = MibTableColumn
partitionFrameTargetRate = _PartitionFrameTargetRate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 51),
    _PartitionFrameTargetRate_Type()
)
partitionFrameTargetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionFrameTargetRate.setStatus("mandatory")
_PartitionFrameTargetRateHi_Type = Gauge32
_PartitionFrameTargetRateHi_Object = MibTableColumn
partitionFrameTargetRateHi = _PartitionFrameTargetRateHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 52),
    _PartitionFrameTargetRateHi_Type()
)
partitionFrameTargetRateHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionFrameTargetRateHi.setStatus("mandatory")
_PartitionFrameCount_Type = Counter32
_PartitionFrameCount_Object = MibTableColumn
partitionFrameCount = _PartitionFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 53),
    _PartitionFrameCount_Type()
)
partitionFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionFrameCount.setStatus("mandatory")
_PartitionEcnCount_Type = Counter32
_PartitionEcnCount_Object = MibTableColumn
partitionEcnCount = _PartitionEcnCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 54),
    _PartitionEcnCount_Type()
)
partitionEcnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionEcnCount.setStatus("mandatory")
_PartitionNonComprsnBytes_Type = Counter32
_PartitionNonComprsnBytes_Object = MibTableColumn
partitionNonComprsnBytes = _PartitionNonComprsnBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 55),
    _PartitionNonComprsnBytes_Type()
)
partitionNonComprsnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionNonComprsnBytes.setStatus("mandatory")
_PartitionNonComprsnBytesHi_Type = Counter32
_PartitionNonComprsnBytesHi_Object = MibTableColumn
partitionNonComprsnBytesHi = _PartitionNonComprsnBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 56),
    _PartitionNonComprsnBytesHi_Type()
)
partitionNonComprsnBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionNonComprsnBytesHi.setStatus("mandatory")
_PartitionPreComprsnBytes_Type = Counter32
_PartitionPreComprsnBytes_Object = MibTableColumn
partitionPreComprsnBytes = _PartitionPreComprsnBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 57),
    _PartitionPreComprsnBytes_Type()
)
partitionPreComprsnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionPreComprsnBytes.setStatus("mandatory")
_PartitionPreComprsnBytesHi_Type = Counter32
_PartitionPreComprsnBytesHi_Object = MibTableColumn
partitionPreComprsnBytesHi = _PartitionPreComprsnBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 58),
    _PartitionPreComprsnBytesHi_Type()
)
partitionPreComprsnBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionPreComprsnBytesHi.setStatus("mandatory")
_PartitionPostComprsnBytes_Type = Counter32
_PartitionPostComprsnBytes_Object = MibTableColumn
partitionPostComprsnBytes = _PartitionPostComprsnBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 59),
    _PartitionPostComprsnBytes_Type()
)
partitionPostComprsnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionPostComprsnBytes.setStatus("mandatory")
_PartitionPostComprsnBytesHi_Type = Counter32
_PartitionPostComprsnBytesHi_Object = MibTableColumn
partitionPostComprsnBytesHi = _PartitionPostComprsnBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 3, 2, 1, 60),
    _PartitionPostComprsnBytesHi_Type()
)
partitionPostComprsnBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionPostComprsnBytesHi.setStatus("mandatory")
_PsClasses_ObjectIdentity = ObjectIdentity
psClasses = _PsClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4)
)
_ClassTableSize_Type = Integer32
_ClassTableSize_Object = MibScalar
classTableSize = _ClassTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 1),
    _ClassTableSize_Type()
)
classTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTableSize.setStatus("mandatory")
_ClassTable_Object = MibTable
classTable = _ClassTable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    classTable.setStatus("mandatory")
_ClassEntry_Object = MibTableRow
classEntry = _ClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1)
)
classEntry.setIndexNames(
    (0, "PACKETEER-MIB", "classIndex"),
)
if mibBuilder.loadTexts:
    classEntry.setStatus("mandatory")
_ClassIndex_Type = Integer32
_ClassIndex_Object = MibTableColumn
classIndex = _ClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 1),
    _ClassIndex_Type()
)
classIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classIndex.setStatus("mandatory")
_ClassName_Type = DisplayString
_ClassName_Object = MibTableColumn
className = _ClassName_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 2),
    _ClassName_Type()
)
className.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    className.setStatus("mandatory")
_ClassOwningPartName_Type = DisplayString
_ClassOwningPartName_Object = MibTableColumn
classOwningPartName = _ClassOwningPartName_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 3),
    _ClassOwningPartName_Type()
)
classOwningPartName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classOwningPartName.setStatus("mandatory")


class _ClassLinkDirection_Type(Integer32):
    """Custom type classLinkDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-bound", 1),
          ("out-bound", 2))
    )


_ClassLinkDirection_Type.__name__ = "Integer32"
_ClassLinkDirection_Object = MibTableColumn
classLinkDirection = _ClassLinkDirection_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 4),
    _ClassLinkDirection_Type()
)
classLinkDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classLinkDirection.setStatus("mandatory")
_ClassByteCount_Type = Counter32
_ClassByteCount_Object = MibTableColumn
classByteCount = _ClassByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 5),
    _ClassByteCount_Type()
)
classByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classByteCount.setStatus("mandatory")
_ClassByteCountHi_Type = Counter32
_ClassByteCountHi_Object = MibTableColumn
classByteCountHi = _ClassByteCountHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 6),
    _ClassByteCountHi_Type()
)
classByteCountHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classByteCountHi.setStatus("mandatory")
_ClassPkts_Type = Counter32
_ClassPkts_Object = MibTableColumn
classPkts = _ClassPkts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 7),
    _ClassPkts_Type()
)
classPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPkts.setStatus("mandatory")
_ClassDataPkts_Type = Counter32
_ClassDataPkts_Object = MibTableColumn
classDataPkts = _ClassDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 8),
    _ClassDataPkts_Type()
)
classDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classDataPkts.setStatus("mandatory")
_ClassReTxs_Type = Counter32
_ClassReTxs_Object = MibTableColumn
classReTxs = _ClassReTxs_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 9),
    _ClassReTxs_Type()
)
classReTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classReTxs.setStatus("mandatory")
_ClassReTxTosses_Type = Counter32
_ClassReTxTosses_Object = MibTableColumn
classReTxTosses = _ClassReTxTosses_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 10),
    _ClassReTxTosses_Type()
)
classReTxTosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classReTxTosses.setStatus("mandatory")
_ClassCirFails_Type = Counter32
_ClassCirFails_Object = MibTableColumn
classCirFails = _ClassCirFails_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 11),
    _ClassCirFails_Type()
)
classCirFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classCirFails.setStatus("mandatory")
_ClassCirAllocs_Type = Counter32
_ClassCirAllocs_Object = MibTableColumn
classCirAllocs = _ClassCirAllocs_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 12),
    _ClassCirAllocs_Type()
)
classCirAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classCirAllocs.setStatus("mandatory")
_ClassEirAllocs_Type = Counter32
_ClassEirAllocs_Object = MibTableColumn
classEirAllocs = _ClassEirAllocs_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 13),
    _ClassEirAllocs_Type()
)
classEirAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classEirAllocs.setStatus("mandatory")
_ClassPeakTcpConns_Type = Gauge32
_ClassPeakTcpConns_Object = MibTableColumn
classPeakTcpConns = _ClassPeakTcpConns_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 14),
    _ClassPeakTcpConns_Type()
)
classPeakTcpConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPeakTcpConns.setStatus("mandatory")
_ClassTcpConnInits_Type = Counter32
_ClassTcpConnInits_Object = MibTableColumn
classTcpConnInits = _ClassTcpConnInits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 15),
    _ClassTcpConnInits_Type()
)
classTcpConnInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTcpConnInits.setStatus("mandatory")
_ClassTcpConnExits_Type = Counter32
_ClassTcpConnExits_Object = MibTableColumn
classTcpConnExits = _ClassTcpConnExits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 16),
    _ClassTcpConnExits_Type()
)
classTcpConnExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTcpConnExits.setStatus("mandatory")
_ClassTcpConnRefuses_Type = Counter32
_ClassTcpConnRefuses_Object = MibTableColumn
classTcpConnRefuses = _ClassTcpConnRefuses_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 17),
    _ClassTcpConnRefuses_Type()
)
classTcpConnRefuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTcpConnRefuses.setStatus("mandatory")
_ClassTcpConnIgnores_Type = Counter32
_ClassTcpConnIgnores_Object = MibTableColumn
classTcpConnIgnores = _ClassTcpConnIgnores_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 18),
    _ClassTcpConnIgnores_Type()
)
classTcpConnIgnores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTcpConnIgnores.setStatus("mandatory")
_ClassTcpConnAborts_Type = Counter32
_ClassTcpConnAborts_Object = MibTableColumn
classTcpConnAborts = _ClassTcpConnAborts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 19),
    _ClassTcpConnAborts_Type()
)
classTcpConnAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTcpConnAborts.setStatus("mandatory")
_ClassTcpConnDenies_Type = Counter32
_ClassTcpConnDenies_Object = MibTableColumn
classTcpConnDenies = _ClassTcpConnDenies_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 20),
    _ClassTcpConnDenies_Type()
)
classTcpConnDenies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTcpConnDenies.setStatus("mandatory")
_ClassTcpConnTimeouts_Type = Counter32
_ClassTcpConnTimeouts_Object = MibTableColumn
classTcpConnTimeouts = _ClassTcpConnTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 21),
    _ClassTcpConnTimeouts_Type()
)
classTcpConnTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classTcpConnTimeouts.setStatus("deprecated")
_ClassPeakUdpConns_Type = Gauge32
_ClassPeakUdpConns_Object = MibTableColumn
classPeakUdpConns = _ClassPeakUdpConns_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 22),
    _ClassPeakUdpConns_Type()
)
classPeakUdpConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPeakUdpConns.setStatus("deprecated")
_ClassUdpConnInits_Type = Counter32
_ClassUdpConnInits_Object = MibTableColumn
classUdpConnInits = _ClassUdpConnInits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 23),
    _ClassUdpConnInits_Type()
)
classUdpConnInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classUdpConnInits.setStatus("deprecated")
_ClassUdpConnExits_Type = Counter32
_ClassUdpConnExits_Object = MibTableColumn
classUdpConnExits = _ClassUdpConnExits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 24),
    _ClassUdpConnExits_Type()
)
classUdpConnExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classUdpConnExits.setStatus("deprecated")
_ClassHits_Type = Counter32
_ClassHits_Object = MibTableColumn
classHits = _ClassHits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 25),
    _ClassHits_Type()
)
classHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classHits.setStatus("mandatory")
_ClassPolicyHits_Type = Counter32
_ClassPolicyHits_Object = MibTableColumn
classPolicyHits = _ClassPolicyHits_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 26),
    _ClassPolicyHits_Type()
)
classPolicyHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPolicyHits.setStatus("mandatory")
_ClassRate_Type = Gauge32
_ClassRate_Object = MibTableColumn
classRate = _ClassRate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 27),
    _ClassRate_Type()
)
classRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classRate.setStatus("mandatory")
_ClassRateAllocations_Type = Gauge32
_ClassRateAllocations_Object = MibTableColumn
classRateAllocations = _ClassRateAllocations_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 28),
    _ClassRateAllocations_Type()
)
classRateAllocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classRateAllocations.setStatus("mandatory")
_ClassPeakGuaranteedRateFlows_Type = Gauge32
_ClassPeakGuaranteedRateFlows_Object = MibTableColumn
classPeakGuaranteedRateFlows = _ClassPeakGuaranteedRateFlows_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 29),
    _ClassPeakGuaranteedRateFlows_Type()
)
classPeakGuaranteedRateFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPeakGuaranteedRateFlows.setStatus("mandatory")
_ClassPeakRateFlows_Type = Gauge32
_ClassPeakRateFlows_Object = MibTableColumn
classPeakRateFlows = _ClassPeakRateFlows_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 30),
    _ClassPeakRateFlows_Type()
)
classPeakRateFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPeakRateFlows.setStatus("mandatory")
_ClassDataDelayEvents_Type = Counter32
_ClassDataDelayEvents_Object = MibTableColumn
classDataDelayEvents = _ClassDataDelayEvents_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 31),
    _ClassDataDelayEvents_Type()
)
classDataDelayEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classDataDelayEvents.setStatus("deprecated")
_ClassDataDelayTimeCum_Type = Integer32
_ClassDataDelayTimeCum_Object = MibTableColumn
classDataDelayTimeCum = _ClassDataDelayTimeCum_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 32),
    _ClassDataDelayTimeCum_Type()
)
classDataDelayTimeCum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classDataDelayTimeCum.setStatus("deprecated")
_ClassReservedOne_Type = Counter32
_ClassReservedOne_Object = MibTableColumn
classReservedOne = _ClassReservedOne_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 33),
    _ClassReservedOne_Type()
)
classReservedOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classReservedOne.setStatus("mandatory")
_ClassReTxByteCount_Type = Counter32
_ClassReTxByteCount_Object = MibTableColumn
classReTxByteCount = _ClassReTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 34),
    _ClassReTxByteCount_Type()
)
classReTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classReTxByteCount.setStatus("mandatory")
_ClassReTxByteCountHi_Type = Counter32
_ClassReTxByteCountHi_Object = MibTableColumn
classReTxByteCountHi = _ClassReTxByteCountHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 35),
    _ClassReTxByteCountHi_Type()
)
classReTxByteCountHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classReTxByteCountHi.setStatus("mandatory")
_ClassFullName_Type = DisplayString
_ClassFullName_Object = MibTableColumn
classFullName = _ClassFullName_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 36),
    _ClassFullName_Type()
)
classFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classFullName.setStatus("mandatory")
_ClassCurrentRate_Type = Gauge32
_ClassCurrentRate_Object = MibTableColumn
classCurrentRate = _ClassCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 37),
    _ClassCurrentRate_Type()
)
classCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classCurrentRate.setStatus("mandatory")
_ClassPktExchangeTime_Type = Counter32
_ClassPktExchangeTime_Object = MibTableColumn
classPktExchangeTime = _ClassPktExchangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 38),
    _ClassPktExchangeTime_Type()
)
classPktExchangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPktExchangeTime.setStatus("mandatory")
_ClassPktExchangeTimeHi_Type = Counter32
_ClassPktExchangeTimeHi_Object = MibTableColumn
classPktExchangeTimeHi = _ClassPktExchangeTimeHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 39),
    _ClassPktExchangeTimeHi_Type()
)
classPktExchangeTimeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPktExchangeTimeHi.setStatus("mandatory")
_ClassPktExchangeTimeSamples_Type = Counter32
_ClassPktExchangeTimeSamples_Object = MibTableColumn
classPktExchangeTimeSamples = _ClassPktExchangeTimeSamples_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 40),
    _ClassPktExchangeTimeSamples_Type()
)
classPktExchangeTimeSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPktExchangeTimeSamples.setStatus("mandatory")
_ClassClientFloodBlock_Type = Counter32
_ClassClientFloodBlock_Object = MibTableColumn
classClientFloodBlock = _ClassClientFloodBlock_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 41),
    _ClassClientFloodBlock_Type()
)
classClientFloodBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classClientFloodBlock.setStatus("mandatory")
_ClassServerFloodBlock_Type = Counter32
_ClassServerFloodBlock_Object = MibTableColumn
classServerFloodBlock = _ClassServerFloodBlock_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 42),
    _ClassServerFloodBlock_Type()
)
classServerFloodBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classServerFloodBlock.setStatus("mandatory")
_ClassAppAvailability_Type = Integer32
_ClassAppAvailability_Object = MibTableColumn
classAppAvailability = _ClassAppAvailability_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 43),
    _ClassAppAvailability_Type()
)
classAppAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classAppAvailability.setStatus("deprecated")
_ClassPeakIpdgConns_Type = Gauge32
_ClassPeakIpdgConns_Object = MibTableColumn
classPeakIpdgConns = _ClassPeakIpdgConns_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 47),
    _ClassPeakIpdgConns_Type()
)
classPeakIpdgConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPeakIpdgConns.setStatus("mandatory")
_ClassWebResponse2XX_Type = Counter32
_ClassWebResponse2XX_Object = MibTableColumn
classWebResponse2XX = _ClassWebResponse2XX_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 48),
    _ClassWebResponse2XX_Type()
)
classWebResponse2XX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classWebResponse2XX.setStatus("mandatory")
_ClassWebResponse3XX_Type = Counter32
_ClassWebResponse3XX_Object = MibTableColumn
classWebResponse3XX = _ClassWebResponse3XX_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 49),
    _ClassWebResponse3XX_Type()
)
classWebResponse3XX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classWebResponse3XX.setStatus("mandatory")
_ClassWebResponse4XX_Type = Counter32
_ClassWebResponse4XX_Object = MibTableColumn
classWebResponse4XX = _ClassWebResponse4XX_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 50),
    _ClassWebResponse4XX_Type()
)
classWebResponse4XX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classWebResponse4XX.setStatus("mandatory")
_ClassWebResponse5XX_Type = Counter32
_ClassWebResponse5XX_Object = MibTableColumn
classWebResponse5XX = _ClassWebResponse5XX_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 51),
    _ClassWebResponse5XX_Type()
)
classWebResponse5XX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classWebResponse5XX.setStatus("mandatory")
_ClassNonComprsnBytes_Type = Counter32
_ClassNonComprsnBytes_Object = MibTableColumn
classNonComprsnBytes = _ClassNonComprsnBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 52),
    _ClassNonComprsnBytes_Type()
)
classNonComprsnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classNonComprsnBytes.setStatus("mandatory")
_ClassNonComprsnBytesHi_Type = Counter32
_ClassNonComprsnBytesHi_Object = MibTableColumn
classNonComprsnBytesHi = _ClassNonComprsnBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 53),
    _ClassNonComprsnBytesHi_Type()
)
classNonComprsnBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classNonComprsnBytesHi.setStatus("mandatory")
_ClassPreComprsnBytes_Type = Counter32
_ClassPreComprsnBytes_Object = MibTableColumn
classPreComprsnBytes = _ClassPreComprsnBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 54),
    _ClassPreComprsnBytes_Type()
)
classPreComprsnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPreComprsnBytes.setStatus("mandatory")
_ClassPostComprsnBytes_Type = Counter32
_ClassPostComprsnBytes_Object = MibTableColumn
classPostComprsnBytes = _ClassPostComprsnBytes_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 55),
    _ClassPostComprsnBytes_Type()
)
classPostComprsnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPostComprsnBytes.setStatus("mandatory")
_ClassPostComprsnBytesHi_Type = Counter32
_ClassPostComprsnBytesHi_Object = MibTableColumn
classPostComprsnBytesHi = _ClassPostComprsnBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 56),
    _ClassPostComprsnBytesHi_Type()
)
classPostComprsnBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPostComprsnBytesHi.setStatus("mandatory")
_ClassPreComprsnBytesHi_Type = Counter32
_ClassPreComprsnBytesHi_Object = MibTableColumn
classPreComprsnBytesHi = _ClassPreComprsnBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 4, 2, 1, 58),
    _ClassPreComprsnBytesHi_Type()
)
classPreComprsnBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classPreComprsnBytesHi.setStatus("mandatory")
_PsAlarms_ObjectIdentity = ObjectIdentity
psAlarms = _PsAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5)
)
_PsAlarmInsideLinkCount_Type = Counter32
_PsAlarmInsideLinkCount_Object = MibScalar
psAlarmInsideLinkCount = _PsAlarmInsideLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 1),
    _PsAlarmInsideLinkCount_Type()
)
psAlarmInsideLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmInsideLinkCount.setStatus("mandatory")
_PsAlarmOutsideLinkCount_Type = Counter32
_PsAlarmOutsideLinkCount_Object = MibScalar
psAlarmOutsideLinkCount = _PsAlarmOutsideLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 3),
    _PsAlarmOutsideLinkCount_Type()
)
psAlarmOutsideLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmOutsideLinkCount.setStatus("mandatory")
_PsAlarmSiteRouterCount_Type = Counter32
_PsAlarmSiteRouterCount_Object = MibScalar
psAlarmSiteRouterCount = _PsAlarmSiteRouterCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 5),
    _PsAlarmSiteRouterCount_Type()
)
psAlarmSiteRouterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmSiteRouterCount.setStatus("mandatory")


class _PsAlarmSiteRouterStatus_Type(Integer32):
    """Custom type psAlarmSiteRouterStatus based on Integer32"""
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
        *(("error-inside", 3),
          ("gone", 2),
          ("none", 4),
          ("ready", 1))
    )


_PsAlarmSiteRouterStatus_Type.__name__ = "Integer32"
_PsAlarmSiteRouterStatus_Object = MibScalar
psAlarmSiteRouterStatus = _PsAlarmSiteRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 6),
    _PsAlarmSiteRouterStatus_Type()
)
psAlarmSiteRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmSiteRouterStatus.setStatus("mandatory")
_PsAlarmPowerSystemOneCount_Type = Counter32
_PsAlarmPowerSystemOneCount_Object = MibScalar
psAlarmPowerSystemOneCount = _PsAlarmPowerSystemOneCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 7),
    _PsAlarmPowerSystemOneCount_Type()
)
psAlarmPowerSystemOneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmPowerSystemOneCount.setStatus("mandatory")


class _PsAlarmPowerSystemOneStatus_Type(Integer32):
    """Custom type psAlarmPowerSystemOneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ok", 2),
          ("ok", 1))
    )


_PsAlarmPowerSystemOneStatus_Type.__name__ = "Integer32"
_PsAlarmPowerSystemOneStatus_Object = MibScalar
psAlarmPowerSystemOneStatus = _PsAlarmPowerSystemOneStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 8),
    _PsAlarmPowerSystemOneStatus_Type()
)
psAlarmPowerSystemOneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmPowerSystemOneStatus.setStatus("mandatory")
_PsAlarmPowerSystemTwoCount_Type = Counter32
_PsAlarmPowerSystemTwoCount_Object = MibScalar
psAlarmPowerSystemTwoCount = _PsAlarmPowerSystemTwoCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 9),
    _PsAlarmPowerSystemTwoCount_Type()
)
psAlarmPowerSystemTwoCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmPowerSystemTwoCount.setStatus("mandatory")


class _PsAlarmPowerSystemTwoStatus_Type(Integer32):
    """Custom type psAlarmPowerSystemTwoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ok", 2),
          ("ok", 1))
    )


_PsAlarmPowerSystemTwoStatus_Type.__name__ = "Integer32"
_PsAlarmPowerSystemTwoStatus_Object = MibScalar
psAlarmPowerSystemTwoStatus = _PsAlarmPowerSystemTwoStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 10),
    _PsAlarmPowerSystemTwoStatus_Type()
)
psAlarmPowerSystemTwoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmPowerSystemTwoStatus.setStatus("mandatory")
_PsAlarmFanOneCount_Type = Counter32
_PsAlarmFanOneCount_Object = MibScalar
psAlarmFanOneCount = _PsAlarmFanOneCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 11),
    _PsAlarmFanOneCount_Type()
)
psAlarmFanOneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmFanOneCount.setStatus("mandatory")


class _PsAlarmFanOneStatus_Type(Integer32):
    """Custom type psAlarmFanOneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-existant", 0),
          ("not-ok", 2),
          ("ok", 1))
    )


_PsAlarmFanOneStatus_Type.__name__ = "Integer32"
_PsAlarmFanOneStatus_Object = MibScalar
psAlarmFanOneStatus = _PsAlarmFanOneStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 12),
    _PsAlarmFanOneStatus_Type()
)
psAlarmFanOneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmFanOneStatus.setStatus("mandatory")
_PsAlarmFanTwoCount_Type = Counter32
_PsAlarmFanTwoCount_Object = MibScalar
psAlarmFanTwoCount = _PsAlarmFanTwoCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 13),
    _PsAlarmFanTwoCount_Type()
)
psAlarmFanTwoCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmFanTwoCount.setStatus("mandatory")


class _PsAlarmFanTwoStatus_Type(Integer32):
    """Custom type psAlarmFanTwoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-existant", 0),
          ("not-ok", 2),
          ("ok", 1))
    )


_PsAlarmFanTwoStatus_Type.__name__ = "Integer32"
_PsAlarmFanTwoStatus_Object = MibScalar
psAlarmFanTwoStatus = _PsAlarmFanTwoStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 14),
    _PsAlarmFanTwoStatus_Type()
)
psAlarmFanTwoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmFanTwoStatus.setStatus("mandatory")
_PsAlarmCfgFileCount_Type = Counter32
_PsAlarmCfgFileCount_Object = MibScalar
psAlarmCfgFileCount = _PsAlarmCfgFileCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 15),
    _PsAlarmCfgFileCount_Type()
)
psAlarmCfgFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmCfgFileCount.setStatus("mandatory")


class _PsAlarmCfgFileStatus_Type(Integer32):
    """Custom type psAlarmCfgFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("corrupted", 2),
          ("valid", 1))
    )


_PsAlarmCfgFileStatus_Type.__name__ = "Integer32"
_PsAlarmCfgFileStatus_Object = MibScalar
psAlarmCfgFileStatus = _PsAlarmCfgFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 16),
    _PsAlarmCfgFileStatus_Type()
)
psAlarmCfgFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmCfgFileStatus.setStatus("mandatory")
_PsAlarmMeasurementEngineCount_Type = Counter32
_PsAlarmMeasurementEngineCount_Object = MibScalar
psAlarmMeasurementEngineCount = _PsAlarmMeasurementEngineCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 17),
    _PsAlarmMeasurementEngineCount_Type()
)
psAlarmMeasurementEngineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmMeasurementEngineCount.setStatus("mandatory")


class _PsAlarmMeasurementEngineStatus_Type(Integer32):
    """Custom type psAlarmMeasurementEngineStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("backup", 8),
          ("disabled", 5),
          ("errorOnVolume", 4),
          ("initiallyStarting", 1),
          ("restore", 9),
          ("running", 3),
          ("starting", 2),
          ("suspended", 7),
          ("waitToStart", 6))
    )


_PsAlarmMeasurementEngineStatus_Type.__name__ = "Integer32"
_PsAlarmMeasurementEngineStatus_Object = MibScalar
psAlarmMeasurementEngineStatus = _PsAlarmMeasurementEngineStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 18),
    _PsAlarmMeasurementEngineStatus_Type()
)
psAlarmMeasurementEngineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmMeasurementEngineStatus.setStatus("mandatory")
_PsAlarmStandbyCount_Type = Counter32
_PsAlarmStandbyCount_Object = MibScalar
psAlarmStandbyCount = _PsAlarmStandbyCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 19),
    _PsAlarmStandbyCount_Type()
)
psAlarmStandbyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmStandbyCount.setStatus("mandatory")


class _PsAlarmStandbyStatus_Type(Integer32):
    """Custom type psAlarmStandbyStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("direct", 5),
          ("disable", 8),
          ("disconnected", 6),
          ("down", 4),
          ("leak", 7),
          ("not-configured", 1),
          ("passive", 3))
    )


_PsAlarmStandbyStatus_Type.__name__ = "Integer32"
_PsAlarmStandbyStatus_Object = MibScalar
psAlarmStandbyStatus = _PsAlarmStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 20),
    _PsAlarmStandbyStatus_Type()
)
psAlarmStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmStandbyStatus.setStatus("mandatory")
_PsAlarmFanThreeCount_Type = Counter32
_PsAlarmFanThreeCount_Object = MibScalar
psAlarmFanThreeCount = _PsAlarmFanThreeCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 21),
    _PsAlarmFanThreeCount_Type()
)
psAlarmFanThreeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmFanThreeCount.setStatus("mandatory")


class _PsAlarmFanThreeStatus_Type(Integer32):
    """Custom type psAlarmFanThreeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-existant", 0),
          ("not-ok", 2),
          ("ok", 1))
    )


_PsAlarmFanThreeStatus_Type.__name__ = "Integer32"
_PsAlarmFanThreeStatus_Object = MibScalar
psAlarmFanThreeStatus = _PsAlarmFanThreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 22),
    _PsAlarmFanThreeStatus_Type()
)
psAlarmFanThreeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmFanThreeStatus.setStatus("mandatory")
_PsAlarmFanFourCount_Type = Counter32
_PsAlarmFanFourCount_Object = MibScalar
psAlarmFanFourCount = _PsAlarmFanFourCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 23),
    _PsAlarmFanFourCount_Type()
)
psAlarmFanFourCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmFanFourCount.setStatus("mandatory")


class _PsAlarmFanFourStatus_Type(Integer32):
    """Custom type psAlarmFanFourStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-existant", 0),
          ("not-ok", 2),
          ("ok", 1))
    )


_PsAlarmFanFourStatus_Type.__name__ = "Integer32"
_PsAlarmFanFourStatus_Object = MibScalar
psAlarmFanFourStatus = _PsAlarmFanFourStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 5, 24),
    _PsAlarmFanFourStatus_Type()
)
psAlarmFanFourStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmFanFourStatus.setStatus("mandatory")
_PsAdmin_ObjectIdentity = ObjectIdentity
psAdmin = _PsAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 6)
)
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("mandatory")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 6, 1, 1)
)
trapDestEntry.setIndexNames(
    (0, "PACKETEER-MIB", "trapDestIpAddr"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("mandatory")
_TrapDestIpAddr_Type = IpAddress
_TrapDestIpAddr_Object = MibTableColumn
trapDestIpAddr = _TrapDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 6, 1, 1, 1),
    _TrapDestIpAddr_Type()
)
trapDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDestIpAddr.setStatus("mandatory")


class _TrapDestStatus_Type(Integer32):
    """Custom type trapDestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_TrapDestStatus_Type.__name__ = "Integer32"
_TrapDestStatus_Object = MibTableColumn
trapDestStatus = _TrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 6, 1, 1, 2),
    _TrapDestStatus_Type()
)
trapDestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestStatus.setStatus("mandatory")
_TrapDestAdd_Type = DisplayString
_TrapDestAdd_Object = MibScalar
trapDestAdd = _TrapDestAdd_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 6, 2),
    _TrapDestAdd_Type()
)
trapDestAdd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    trapDestAdd.setStatus("mandatory")
_TrapDestRemove_Type = DisplayString
_TrapDestRemove_Object = MibScalar
trapDestRemove = _TrapDestRemove_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 6, 3),
    _TrapDestRemove_Type()
)
trapDestRemove.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    trapDestRemove.setStatus("mandatory")


class _PsShapingStatusAdmin_Type(Integer32):
    """Custom type psShapingStatusAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 3),
          ("off", 2),
          ("on", 1),
          ("other", 4),
          ("watch", 5))
    )


_PsShapingStatusAdmin_Type.__name__ = "Integer32"
_PsShapingStatusAdmin_Object = MibScalar
psShapingStatusAdmin = _PsShapingStatusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 6, 4),
    _PsShapingStatusAdmin_Type()
)
psShapingStatusAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psShapingStatusAdmin.setStatus("mandatory")
_PsUserEvents_ObjectIdentity = ObjectIdentity
psUserEvents = _PsUserEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8)
)
_PsUserEventTrapVars_ObjectIdentity = ObjectIdentity
psUserEventTrapVars = _PsUserEventTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1)
)
_UserEventTrapName_Type = DisplayString
_UserEventTrapName_Object = MibScalar
userEventTrapName = _UserEventTrapName_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 1),
    _UserEventTrapName_Type()
)
userEventTrapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapName.setStatus("mandatory")
_UserEventTrapExpression_Type = DisplayString
_UserEventTrapExpression_Object = MibScalar
userEventTrapExpression = _UserEventTrapExpression_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 2),
    _UserEventTrapExpression_Type()
)
userEventTrapExpression.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapExpression.setStatus("mandatory")
_UserEventTrapVariable_Type = DisplayString
_UserEventTrapVariable_Object = MibScalar
userEventTrapVariable = _UserEventTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 3),
    _UserEventTrapVariable_Type()
)
userEventTrapVariable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapVariable.setStatus("mandatory")


class _UserEventTrapElementType_Type(Integer32):
    """Custom type userEventTrapElementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("class", 2),
          ("link", 1),
          ("partition", 3))
    )


_UserEventTrapElementType_Type.__name__ = "Integer32"
_UserEventTrapElementType_Object = MibScalar
userEventTrapElementType = _UserEventTrapElementType_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 4),
    _UserEventTrapElementType_Type()
)
userEventTrapElementType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapElementType.setStatus("mandatory")
_UserEventTrapRegid_Type = Integer32
_UserEventTrapRegid_Object = MibScalar
userEventTrapRegid = _UserEventTrapRegid_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 5),
    _UserEventTrapRegid_Type()
)
userEventTrapRegid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapRegid.setStatus("mandatory")
_UserEventTrapDate_Type = DateAndTime
_UserEventTrapDate_Object = MibScalar
userEventTrapDate = _UserEventTrapDate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 6),
    _UserEventTrapDate_Type()
)
userEventTrapDate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapDate.setStatus("mandatory")
_UserEventTrapValue_Type = Integer32
_UserEventTrapValue_Object = MibScalar
userEventTrapValue = _UserEventTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 7),
    _UserEventTrapValue_Type()
)
userEventTrapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapValue.setStatus("mandatory")
_UserEventTrapTarget_Type = DisplayString
_UserEventTrapTarget_Object = MibScalar
userEventTrapTarget = _UserEventTrapTarget_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 8),
    _UserEventTrapTarget_Type()
)
userEventTrapTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapTarget.setStatus("mandatory")
_UserEventTrapThreshold_Type = Integer32
_UserEventTrapThreshold_Object = MibScalar
userEventTrapThreshold = _UserEventTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 9),
    _UserEventTrapThreshold_Type()
)
userEventTrapThreshold.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapThreshold.setStatus("mandatory")
_UserEventTrapRearm_Type = Integer32
_UserEventTrapRearm_Object = MibScalar
userEventTrapRearm = _UserEventTrapRearm_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 10),
    _UserEventTrapRearm_Type()
)
userEventTrapRearm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapRearm.setStatus("mandatory")
_UserEventTrapDayCount_Type = Integer32
_UserEventTrapDayCount_Object = MibScalar
userEventTrapDayCount = _UserEventTrapDayCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 11),
    _UserEventTrapDayCount_Type()
)
userEventTrapDayCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapDayCount.setStatus("mandatory")
_UserEventTrapDayLimit_Type = Integer32
_UserEventTrapDayLimit_Object = MibScalar
userEventTrapDayLimit = _UserEventTrapDayLimit_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 8, 1, 12),
    _UserEventTrapDayLimit_Type()
)
userEventTrapDayLimit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userEventTrapDayLimit.setStatus("mandatory")
_PsHighAv_ObjectIdentity = ObjectIdentity
psHighAv = _PsHighAv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 9)
)
_PsFeatureHighAvDeviceDownCount_Type = Counter32
_PsFeatureHighAvDeviceDownCount_Object = MibScalar
psFeatureHighAvDeviceDownCount = _PsFeatureHighAvDeviceDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 9, 1),
    _PsFeatureHighAvDeviceDownCount_Type()
)
psFeatureHighAvDeviceDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psFeatureHighAvDeviceDownCount.setStatus("mandatory")


class _PsFeatureHighAvDeviceDownStatus_Type(Integer32):
    """Custom type psFeatureHighAvDeviceDownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_PsFeatureHighAvDeviceDownStatus_Type.__name__ = "Integer32"
_PsFeatureHighAvDeviceDownStatus_Object = MibScalar
psFeatureHighAvDeviceDownStatus = _PsFeatureHighAvDeviceDownStatus_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 9, 2),
    _PsFeatureHighAvDeviceDownStatus_Type()
)
psFeatureHighAvDeviceDownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psFeatureHighAvDeviceDownStatus.setStatus("mandatory")
_PsFeatureHighAvDeviceDownRouter_Type = DisplayString
_PsFeatureHighAvDeviceDownRouter_Object = MibScalar
psFeatureHighAvDeviceDownRouter = _PsFeatureHighAvDeviceDownRouter_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 9, 3),
    _PsFeatureHighAvDeviceDownRouter_Type()
)
psFeatureHighAvDeviceDownRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psFeatureHighAvDeviceDownRouter.setStatus("mandatory")
_PsFeatureHighAvDeviceDownInterface_Type = DisplayString
_PsFeatureHighAvDeviceDownInterface_Object = MibScalar
psFeatureHighAvDeviceDownInterface = _PsFeatureHighAvDeviceDownInterface_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 9, 4),
    _PsFeatureHighAvDeviceDownInterface_Type()
)
psFeatureHighAvDeviceDownInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psFeatureHighAvDeviceDownInterface.setStatus("mandatory")
_PsAgentEvent_ObjectIdentity = ObjectIdentity
psAgentEvent = _PsAgentEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 10)
)
_PsAgentEventTrapVars_ObjectIdentity = ObjectIdentity
psAgentEventTrapVars = _PsAgentEventTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 10, 1)
)
_AgentEventTrapName_Type = DisplayString
_AgentEventTrapName_Object = MibScalar
agentEventTrapName = _AgentEventTrapName_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 10, 1, 1),
    _AgentEventTrapName_Type()
)
agentEventTrapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentEventTrapName.setStatus("mandatory")
_AgentEventTrapDate_Type = DateAndTime
_AgentEventTrapDate_Object = MibScalar
agentEventTrapDate = _AgentEventTrapDate_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 10, 1, 2),
    _AgentEventTrapDate_Type()
)
agentEventTrapDate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentEventTrapDate.setStatus("mandatory")


class _AgentEventTrapType_Type(Integer32):
    """Custom type agentEventTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blue", 3),
          ("green", 0),
          ("red", 1),
          ("yellow", 2))
    )


_AgentEventTrapType_Type.__name__ = "Integer32"
_AgentEventTrapType_Object = MibScalar
agentEventTrapType = _AgentEventTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 10, 1, 3),
    _AgentEventTrapType_Type()
)
agentEventTrapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentEventTrapType.setStatus("mandatory")
_AgentEventTrapDescription_Type = DisplayString
_AgentEventTrapDescription_Object = MibScalar
agentEventTrapDescription = _AgentEventTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 2334, 2, 1, 10, 1, 4),
    _AgentEventTrapDescription_Type()
)
agentEventTrapDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentEventTrapDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

psAlarmSiteRouter = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 3)
)
psAlarmSiteRouter.setObjects(
    ("PACKETEER-MIB", "psAlarmSiteRouterStatus")
)
if mibBuilder.loadTexts:
    psAlarmSiteRouter.setStatus(
        ""
    )

psAlarmPowerSystemOne = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 4)
)
if mibBuilder.loadTexts:
    psAlarmPowerSystemOne.setStatus(
        ""
    )

psAlarmPowerSystemTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 5)
)
if mibBuilder.loadTexts:
    psAlarmPowerSystemTwo.setStatus(
        ""
    )

psAlarmFanOne = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 6)
)
if mibBuilder.loadTexts:
    psAlarmFanOne.setStatus(
        ""
    )

psAlarmFanTwo = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 7)
)
if mibBuilder.loadTexts:
    psAlarmFanTwo.setStatus(
        ""
    )

psAlarmCfgFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 8)
)
if mibBuilder.loadTexts:
    psAlarmCfgFile.setStatus(
        ""
    )

psAlarmUserEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 9)
)
psAlarmUserEvent.setObjects(
      *(("PACKETEER-MIB", "userEventTrapName"),
        ("PACKETEER-MIB", "userEventTrapExpression"),
        ("PACKETEER-MIB", "userEventTrapVariable"),
        ("PACKETEER-MIB", "userEventTrapElementType"),
        ("PACKETEER-MIB", "userEventTrapRegid"),
        ("PACKETEER-MIB", "userEventTrapDate"),
        ("PACKETEER-MIB", "userEventTrapValue"),
        ("PACKETEER-MIB", "userEventTrapTarget"),
        ("PACKETEER-MIB", "userEventTrapThreshold"),
        ("PACKETEER-MIB", "userEventTrapRearm"),
        ("PACKETEER-MIB", "userEventTrapDayCount"),
        ("PACKETEER-MIB", "userEventTrapDayLimit"))
)
if mibBuilder.loadTexts:
    psAlarmUserEvent.setStatus(
        ""
    )

psAlarmMeasurementEngine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 10)
)
psAlarmMeasurementEngine.setObjects(
    ("PACKETEER-MIB", "psAlarmMeasurementEngineStatus")
)
if mibBuilder.loadTexts:
    psAlarmMeasurementEngine.setStatus(
        ""
    )

psAlarmStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 11)
)
psAlarmStandby.setObjects(
    ("PACKETEER-MIB", "psAlarmStandbyStatus")
)
if mibBuilder.loadTexts:
    psAlarmStandby.setStatus(
        ""
    )

psFeatureHighAvDeviceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 12)
)
psFeatureHighAvDeviceDown.setObjects(
      *(("PACKETEER-MIB", "psFeatureHighAvDeviceDownStatus"),
        ("PACKETEER-MIB", "psFeatureHighAvDeviceDownRouter"),
        ("PACKETEER-MIB", "psFeatureHighAvDeviceDownInterface"))
)
if mibBuilder.loadTexts:
    psFeatureHighAvDeviceDown.setStatus(
        ""
    )

psAlarmAgentEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 13)
)
psAlarmAgentEvent.setObjects(
      *(("PACKETEER-MIB", "agentEventTrapName"),
        ("PACKETEER-MIB", "agentEventTrapDate"),
        ("PACKETEER-MIB", "agentEventTrapType"),
        ("PACKETEER-MIB", "agentEventTrapDescription"))
)
if mibBuilder.loadTexts:
    psAlarmAgentEvent.setStatus(
        ""
    )

psAlarmFanThree = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 14)
)
if mibBuilder.loadTexts:
    psAlarmFanThree.setStatus(
        ""
    )

psAlarmFanFour = NotificationType(
    (1, 3, 6, 1, 4, 1, 2334, 1, 1, 0, 15)
)
if mibBuilder.loadTexts:
    psAlarmFanFour.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETEER-MIB",
    **{"packeteer": packeteer,
       "products": products,
       "packetShaper": packetShaper,
       "psAlarmSiteRouter": psAlarmSiteRouter,
       "psAlarmPowerSystemOne": psAlarmPowerSystemOne,
       "psAlarmPowerSystemTwo": psAlarmPowerSystemTwo,
       "psAlarmFanOne": psAlarmFanOne,
       "psAlarmFanTwo": psAlarmFanTwo,
       "psAlarmCfgFile": psAlarmCfgFile,
       "psAlarmUserEvent": psAlarmUserEvent,
       "psAlarmMeasurementEngine": psAlarmMeasurementEngine,
       "psAlarmStandby": psAlarmStandby,
       "psFeatureHighAvDeviceDown": psFeatureHighAvDeviceDown,
       "psAlarmAgentEvent": psAlarmAgentEvent,
       "psAlarmFanThree": psAlarmFanThree,
       "psAlarmFanFour": psAlarmFanFour,
       "packetShaper-2000": packetShaper_2000,
       "packetShaper-4000": packetShaper_4000,
       "packetShaper-1000": packetShaper_1000,
       "packetShaper-2500": packetShaper_2500,
       "packetShaper-4500": packetShaper_4500,
       "packetShaper-1500": packetShaper_1500,
       "packetShaper-asm50": packetShaper_asm50,
       "packetShaper-asm70": packetShaper_asm70,
       "packetShaper-asm30": packetShaper_asm30,
       "packetShaper-asm90": packetShaper_asm90,
       "packetShaper-6500": packetShaper_6500,
       "packetShaper-8500": packetShaper_8500,
       "packetShaper-asm110": packetShaper_asm110,
       "packetShaper-1550": packetShaper_1550,
       "packetShaper-9500": packetShaper_9500,
       "packetShaper-2550": packetShaper_2550,
       "packetShaper-10000": packetShaper_10000,
       "packeteerMibs": packeteerMibs,
       "psCommonMib": psCommonMib,
       "psSettings": psSettings,
       "psShapingStatusOper": psShapingStatusOper,
       "psLinks": psLinks,
       "linkTableSize": linkTableSize,
       "linkTable": linkTable,
       "linkEntry": linkEntry,
       "linkIndex": linkIndex,
       "linkName": linkName,
       "linkByteCount": linkByteCount,
       "linkByteCountHi": linkByteCountHi,
       "linkPkts": linkPkts,
       "linkDataPkts": linkDataPkts,
       "linkReTxs": linkReTxs,
       "linkReTxTosses": linkReTxTosses,
       "linkCirFails": linkCirFails,
       "linkCirAllocs": linkCirAllocs,
       "linkEirAllocs": linkEirAllocs,
       "linkPeakTcpConns": linkPeakTcpConns,
       "linkTcpConnInits": linkTcpConnInits,
       "linkTcpConnExits": linkTcpConnExits,
       "linkTcpConnRefuses": linkTcpConnRefuses,
       "linkTcpConnIgnores": linkTcpConnIgnores,
       "linkTcpConnAborts": linkTcpConnAborts,
       "linkTcpConnDenies": linkTcpConnDenies,
       "linkTcpConnTimeouts": linkTcpConnTimeouts,
       "linkPeakUdpConns": linkPeakUdpConns,
       "linkUdpConnInits": linkUdpConnInits,
       "linkUdpConnExits": linkUdpConnExits,
       "linkSize": linkSize,
       "linkRate": linkRate,
       "linkRateAllocations": linkRateAllocations,
       "linkPeakGuaranteedRateFlows": linkPeakGuaranteedRateFlows,
       "linkPeakRateFlows": linkPeakRateFlows,
       "linkReTxByteCount": linkReTxByteCount,
       "linkReTxByteCountHi": linkReTxByteCountHi,
       "linkTotalRxPkts": linkTotalRxPkts,
       "linkTotalTxPkts": linkTotalTxPkts,
       "linkRxNoBufs": linkRxNoBufs,
       "linkRxPktDrops": linkRxPktDrops,
       "linkTxPktDrops": linkTxPktDrops,
       "linkRxErrors": linkRxErrors,
       "linkTxErrors": linkTxErrors,
       "linkTcpAllocFails": linkTcpAllocFails,
       "linkIpdgAllocFails": linkIpdgAllocFails,
       "linkHostdbAllocFails": linkHostdbAllocFails,
       "linkShapingMode": linkShapingMode,
       "linkAutoclassifyMode": linkAutoclassifyMode,
       "linkMacSameSidePkts": linkMacSameSidePkts,
       "linkPassthruPkts": linkPassthruPkts,
       "linkTotalRxBytes": linkTotalRxBytes,
       "linkTotalRxBytesHi": linkTotalRxBytesHi,
       "linkTotalTxBytes": linkTotalTxBytes,
       "linkTotalTxBytesHi": linkTotalTxBytesHi,
       "linkClassChecks": linkClassChecks,
       "linkPassthruBytes": linkPassthruBytes,
       "linkCompressionMode": linkCompressionMode,
       "linkPeakPreCompressionRate": linkPeakPreCompressionRate,
       "linkPeakPostCompressionRate": linkPeakPostCompressionRate,
       "linkNonComprsnBytes": linkNonComprsnBytes,
       "linkNonComprsnBytesHi": linkNonComprsnBytesHi,
       "linkPreComprsnBytes": linkPreComprsnBytes,
       "linkPreComprsnBytesHi": linkPreComprsnBytesHi,
       "linkPostComprsnBytes": linkPostComprsnBytes,
       "linkPostComprsnBytesHi": linkPostComprsnBytesHi,
       "psPartitions": psPartitions,
       "partitionTableSize": partitionTableSize,
       "partitionTable": partitionTable,
       "partitionEntry": partitionEntry,
       "partitionIndex": partitionIndex,
       "partitionName": partitionName,
       "partitionLinkDirection": partitionLinkDirection,
       "partitionByteCount": partitionByteCount,
       "partitionByteCountHi": partitionByteCountHi,
       "partitionPkts": partitionPkts,
       "partitionDataPkts": partitionDataPkts,
       "partitionReTxs": partitionReTxs,
       "partitionReTxTosses": partitionReTxTosses,
       "partitionCirFails": partitionCirFails,
       "partitionCirAllocs": partitionCirAllocs,
       "partitionEirAllocs": partitionEirAllocs,
       "partitionPeakTcpConns": partitionPeakTcpConns,
       "partitionTcpConnInits": partitionTcpConnInits,
       "partitionTcpConnExits": partitionTcpConnExits,
       "partitionTcpConnRefuses": partitionTcpConnRefuses,
       "partitionTcpConnIgnores": partitionTcpConnIgnores,
       "partitionTcpConnAborts": partitionTcpConnAborts,
       "partitionTcpConnDenies": partitionTcpConnDenies,
       "partitionTcpConnTimeouts": partitionTcpConnTimeouts,
       "partitionPeakUdpConns": partitionPeakUdpConns,
       "partitionUdpConnInits": partitionUdpConnInits,
       "partitionUdpConnExits": partitionUdpConnExits,
       "partitionMinimumBps": partitionMinimumBps,
       "partitionBurstLimit": partitionBurstLimit,
       "partitionRate": partitionRate,
       "partitionCirRate": partitionCirRate,
       "partitionEirRate": partitionEirRate,
       "partitionUnreservedRate": partitionUnreservedRate,
       "partitionFirstSatisfiedPriority": partitionFirstSatisfiedPriority,
       "partitionTimeOverLimit": partitionTimeOverLimit,
       "partitionRateAllocations": partitionRateAllocations,
       "partitionPeakGuaranteedRateFlows": partitionPeakGuaranteedRateFlows,
       "partitionPeakRateFlows": partitionPeakRateFlows,
       "partitionReTxByteCount": partitionReTxByteCount,
       "partitionReTxByteCountHi": partitionReTxByteCountHi,
       "partitionDynamicCapCount": partitionDynamicCapCount,
       "partitionDynamicNoCount": partitionDynamicNoCount,
       "partitionDynamicLiveUserCount": partitionDynamicLiveUserCount,
       "partitionCommittmentFailures": partitionCommittmentFailures,
       "partitionLateDropPktCount": partitionLateDropPktCount,
       "partitionLateDropPktCountHi": partitionLateDropPktCountHi,
       "partitionLateDropByteCount": partitionLateDropByteCount,
       "partitionLateDropByteCountHi": partitionLateDropByteCountHi,
       "partitionSchedDropPktCount": partitionSchedDropPktCount,
       "partitionSchedDropPktCountHi": partitionSchedDropPktCountHi,
       "partitionSchedDropByteCount": partitionSchedDropByteCount,
       "partitionSchedDropByteCountHi": partitionSchedDropByteCountHi,
       "partitionFrameBytes": partitionFrameBytes,
       "partitionFrameBytesHi": partitionFrameBytesHi,
       "partitionFrameTargetRate": partitionFrameTargetRate,
       "partitionFrameTargetRateHi": partitionFrameTargetRateHi,
       "partitionFrameCount": partitionFrameCount,
       "partitionEcnCount": partitionEcnCount,
       "partitionNonComprsnBytes": partitionNonComprsnBytes,
       "partitionNonComprsnBytesHi": partitionNonComprsnBytesHi,
       "partitionPreComprsnBytes": partitionPreComprsnBytes,
       "partitionPreComprsnBytesHi": partitionPreComprsnBytesHi,
       "partitionPostComprsnBytes": partitionPostComprsnBytes,
       "partitionPostComprsnBytesHi": partitionPostComprsnBytesHi,
       "psClasses": psClasses,
       "classTableSize": classTableSize,
       "classTable": classTable,
       "classEntry": classEntry,
       "classIndex": classIndex,
       "className": className,
       "classOwningPartName": classOwningPartName,
       "classLinkDirection": classLinkDirection,
       "classByteCount": classByteCount,
       "classByteCountHi": classByteCountHi,
       "classPkts": classPkts,
       "classDataPkts": classDataPkts,
       "classReTxs": classReTxs,
       "classReTxTosses": classReTxTosses,
       "classCirFails": classCirFails,
       "classCirAllocs": classCirAllocs,
       "classEirAllocs": classEirAllocs,
       "classPeakTcpConns": classPeakTcpConns,
       "classTcpConnInits": classTcpConnInits,
       "classTcpConnExits": classTcpConnExits,
       "classTcpConnRefuses": classTcpConnRefuses,
       "classTcpConnIgnores": classTcpConnIgnores,
       "classTcpConnAborts": classTcpConnAborts,
       "classTcpConnDenies": classTcpConnDenies,
       "classTcpConnTimeouts": classTcpConnTimeouts,
       "classPeakUdpConns": classPeakUdpConns,
       "classUdpConnInits": classUdpConnInits,
       "classUdpConnExits": classUdpConnExits,
       "classHits": classHits,
       "classPolicyHits": classPolicyHits,
       "classRate": classRate,
       "classRateAllocations": classRateAllocations,
       "classPeakGuaranteedRateFlows": classPeakGuaranteedRateFlows,
       "classPeakRateFlows": classPeakRateFlows,
       "classDataDelayEvents": classDataDelayEvents,
       "classDataDelayTimeCum": classDataDelayTimeCum,
       "classReservedOne": classReservedOne,
       "classReTxByteCount": classReTxByteCount,
       "classReTxByteCountHi": classReTxByteCountHi,
       "classFullName": classFullName,
       "classCurrentRate": classCurrentRate,
       "classPktExchangeTime": classPktExchangeTime,
       "classPktExchangeTimeHi": classPktExchangeTimeHi,
       "classPktExchangeTimeSamples": classPktExchangeTimeSamples,
       "classClientFloodBlock": classClientFloodBlock,
       "classServerFloodBlock": classServerFloodBlock,
       "classAppAvailability": classAppAvailability,
       "classPeakIpdgConns": classPeakIpdgConns,
       "classWebResponse2XX": classWebResponse2XX,
       "classWebResponse3XX": classWebResponse3XX,
       "classWebResponse4XX": classWebResponse4XX,
       "classWebResponse5XX": classWebResponse5XX,
       "classNonComprsnBytes": classNonComprsnBytes,
       "classNonComprsnBytesHi": classNonComprsnBytesHi,
       "classPreComprsnBytes": classPreComprsnBytes,
       "classPostComprsnBytes": classPostComprsnBytes,
       "classPostComprsnBytesHi": classPostComprsnBytesHi,
       "classPreComprsnBytesHi": classPreComprsnBytesHi,
       "psAlarms": psAlarms,
       "psAlarmInsideLinkCount": psAlarmInsideLinkCount,
       "psAlarmOutsideLinkCount": psAlarmOutsideLinkCount,
       "psAlarmSiteRouterCount": psAlarmSiteRouterCount,
       "psAlarmSiteRouterStatus": psAlarmSiteRouterStatus,
       "psAlarmPowerSystemOneCount": psAlarmPowerSystemOneCount,
       "psAlarmPowerSystemOneStatus": psAlarmPowerSystemOneStatus,
       "psAlarmPowerSystemTwoCount": psAlarmPowerSystemTwoCount,
       "psAlarmPowerSystemTwoStatus": psAlarmPowerSystemTwoStatus,
       "psAlarmFanOneCount": psAlarmFanOneCount,
       "psAlarmFanOneStatus": psAlarmFanOneStatus,
       "psAlarmFanTwoCount": psAlarmFanTwoCount,
       "psAlarmFanTwoStatus": psAlarmFanTwoStatus,
       "psAlarmCfgFileCount": psAlarmCfgFileCount,
       "psAlarmCfgFileStatus": psAlarmCfgFileStatus,
       "psAlarmMeasurementEngineCount": psAlarmMeasurementEngineCount,
       "psAlarmMeasurementEngineStatus": psAlarmMeasurementEngineStatus,
       "psAlarmStandbyCount": psAlarmStandbyCount,
       "psAlarmStandbyStatus": psAlarmStandbyStatus,
       "psAlarmFanThreeCount": psAlarmFanThreeCount,
       "psAlarmFanThreeStatus": psAlarmFanThreeStatus,
       "psAlarmFanFourCount": psAlarmFanFourCount,
       "psAlarmFanFourStatus": psAlarmFanFourStatus,
       "psAdmin": psAdmin,
       "trapDestTable": trapDestTable,
       "trapDestEntry": trapDestEntry,
       "trapDestIpAddr": trapDestIpAddr,
       "trapDestStatus": trapDestStatus,
       "trapDestAdd": trapDestAdd,
       "trapDestRemove": trapDestRemove,
       "psShapingStatusAdmin": psShapingStatusAdmin,
       "psUserEvents": psUserEvents,
       "psUserEventTrapVars": psUserEventTrapVars,
       "userEventTrapName": userEventTrapName,
       "userEventTrapExpression": userEventTrapExpression,
       "userEventTrapVariable": userEventTrapVariable,
       "userEventTrapElementType": userEventTrapElementType,
       "userEventTrapRegid": userEventTrapRegid,
       "userEventTrapDate": userEventTrapDate,
       "userEventTrapValue": userEventTrapValue,
       "userEventTrapTarget": userEventTrapTarget,
       "userEventTrapThreshold": userEventTrapThreshold,
       "userEventTrapRearm": userEventTrapRearm,
       "userEventTrapDayCount": userEventTrapDayCount,
       "userEventTrapDayLimit": userEventTrapDayLimit,
       "psHighAv": psHighAv,
       "psFeatureHighAvDeviceDownCount": psFeatureHighAvDeviceDownCount,
       "psFeatureHighAvDeviceDownStatus": psFeatureHighAvDeviceDownStatus,
       "psFeatureHighAvDeviceDownRouter": psFeatureHighAvDeviceDownRouter,
       "psFeatureHighAvDeviceDownInterface": psFeatureHighAvDeviceDownInterface,
       "psAgentEvent": psAgentEvent,
       "psAgentEventTrapVars": psAgentEventTrapVars,
       "agentEventTrapName": agentEventTrapName,
       "agentEventTrapDate": agentEventTrapDate,
       "agentEventTrapType": agentEventTrapType,
       "agentEventTrapDescription": agentEventTrapDescription}
)
