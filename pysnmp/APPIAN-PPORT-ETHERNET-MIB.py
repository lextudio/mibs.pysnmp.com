# SNMP MIB module (APPIAN-PPORT-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-PPORT-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:40 2024
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

(acChassisCurrentTime,
 acChassisRingId) = mibBuilder.importSymbols(
    "APPIAN-CHASSIS-MIB",
    "acChassisCurrentTime",
    "acChassisRingId")

(AcAdminStatus,
 AcNodeId,
 AcOpStatus,
 AcPortNumber,
 AcSlotNumber,
 acPport) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeId",
    "AcOpStatus",
    "AcPortNumber",
    "AcSlotNumber",
    "acPport")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acEnet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3)
)
acEnet.setRevisions(
        ("1900-02-23 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcEnetSpeed(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gb1", 3),
          ("mb10", 1),
          ("mb100", 2))
    )



class AcEnetDuplexity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )



class AcEnetLinkState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("nolink", 2),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_AcEnetTraps_ObjectIdentity = ObjectIdentity
acEnetTraps = _AcEnetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 0)
)
_AcEnetStatsTable_Object = MibTable
acEnetStatsTable = _AcEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    acEnetStatsTable.setStatus("current")
_AcEnetStatsEntry_Object = MibTableRow
acEnetStatsEntry = _AcEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1)
)
acEnetStatsEntry.setIndexNames(
    (0, "APPIAN-PPORT-ETHERNET-MIB", "acEnetStatsNodeId"),
    (0, "APPIAN-PPORT-ETHERNET-MIB", "acEnetStatsSlot"),
    (0, "APPIAN-PPORT-ETHERNET-MIB", "acEnetStatsPort"),
)
if mibBuilder.loadTexts:
    acEnetStatsEntry.setStatus("current")
_AcEnetStatsNodeId_Type = AcNodeId
_AcEnetStatsNodeId_Object = MibTableColumn
acEnetStatsNodeId = _AcEnetStatsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 1),
    _AcEnetStatsNodeId_Type()
)
acEnetStatsNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acEnetStatsNodeId.setStatus("current")
_AcEnetStatsSlot_Type = AcSlotNumber
_AcEnetStatsSlot_Object = MibTableColumn
acEnetStatsSlot = _AcEnetStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 2),
    _AcEnetStatsSlot_Type()
)
acEnetStatsSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acEnetStatsSlot.setStatus("current")
_AcEnetStatsPort_Type = AcPortNumber
_AcEnetStatsPort_Object = MibTableColumn
acEnetStatsPort = _AcEnetStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 3),
    _AcEnetStatsPort_Type()
)
acEnetStatsPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acEnetStatsPort.setStatus("current")
_AcEnetStatsPktsRx_Type = Counter64
_AcEnetStatsPktsRx_Object = MibTableColumn
acEnetStatsPktsRx = _AcEnetStatsPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 4),
    _AcEnetStatsPktsRx_Type()
)
acEnetStatsPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsPktsRx.setStatus("current")
_AcEnetStatsPktsTx_Type = Counter64
_AcEnetStatsPktsTx_Object = MibTableColumn
acEnetStatsPktsTx = _AcEnetStatsPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 5),
    _AcEnetStatsPktsTx_Type()
)
acEnetStatsPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsPktsTx.setStatus("current")
_AcEnetStatsOctetsRx_Type = Counter64
_AcEnetStatsOctetsRx_Object = MibTableColumn
acEnetStatsOctetsRx = _AcEnetStatsOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 6),
    _AcEnetStatsOctetsRx_Type()
)
acEnetStatsOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsOctetsRx.setStatus("current")
_AcEnetStatsOctetsTx_Type = Counter64
_AcEnetStatsOctetsTx_Object = MibTableColumn
acEnetStatsOctetsTx = _AcEnetStatsOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 7),
    _AcEnetStatsOctetsTx_Type()
)
acEnetStatsOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsOctetsTx.setStatus("current")
_AcEnetStatsBcastPktsRx_Type = Counter64
_AcEnetStatsBcastPktsRx_Object = MibTableColumn
acEnetStatsBcastPktsRx = _AcEnetStatsBcastPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 8),
    _AcEnetStatsBcastPktsRx_Type()
)
acEnetStatsBcastPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsBcastPktsRx.setStatus("current")
_AcEnetStatsBcastPktsTx_Type = Counter64
_AcEnetStatsBcastPktsTx_Object = MibTableColumn
acEnetStatsBcastPktsTx = _AcEnetStatsBcastPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 9),
    _AcEnetStatsBcastPktsTx_Type()
)
acEnetStatsBcastPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsBcastPktsTx.setStatus("current")
_AcEnetStatsMcastPktsRx_Type = Counter64
_AcEnetStatsMcastPktsRx_Object = MibTableColumn
acEnetStatsMcastPktsRx = _AcEnetStatsMcastPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 10),
    _AcEnetStatsMcastPktsRx_Type()
)
acEnetStatsMcastPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsMcastPktsRx.setStatus("current")
_AcEnetStatsMcastPktsTx_Type = Counter64
_AcEnetStatsMcastPktsTx_Object = MibTableColumn
acEnetStatsMcastPktsTx = _AcEnetStatsMcastPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 11),
    _AcEnetStatsMcastPktsTx_Type()
)
acEnetStatsMcastPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsMcastPktsTx.setStatus("current")
_AcEnetStatsCrcAlignErrors_Type = Counter64
_AcEnetStatsCrcAlignErrors_Object = MibTableColumn
acEnetStatsCrcAlignErrors = _AcEnetStatsCrcAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 12),
    _AcEnetStatsCrcAlignErrors_Type()
)
acEnetStatsCrcAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsCrcAlignErrors.setStatus("current")
_AcEnetStatsUndersizedPkts_Type = Counter64
_AcEnetStatsUndersizedPkts_Object = MibTableColumn
acEnetStatsUndersizedPkts = _AcEnetStatsUndersizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 13),
    _AcEnetStatsUndersizedPkts_Type()
)
acEnetStatsUndersizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsUndersizedPkts.setStatus("current")
_AcEnetStatsOversizedPkts_Type = Counter64
_AcEnetStatsOversizedPkts_Object = MibTableColumn
acEnetStatsOversizedPkts = _AcEnetStatsOversizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 14),
    _AcEnetStatsOversizedPkts_Type()
)
acEnetStatsOversizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsOversizedPkts.setStatus("current")
_AcEnetStatsFragmentedPkts_Type = Counter64
_AcEnetStatsFragmentedPkts_Object = MibTableColumn
acEnetStatsFragmentedPkts = _AcEnetStatsFragmentedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 15),
    _AcEnetStatsFragmentedPkts_Type()
)
acEnetStatsFragmentedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsFragmentedPkts.setStatus("current")
_AcEnetStatsJabbers_Type = Counter64
_AcEnetStatsJabbers_Object = MibTableColumn
acEnetStatsJabbers = _AcEnetStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 16),
    _AcEnetStatsJabbers_Type()
)
acEnetStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsJabbers.setStatus("current")
_AcEnetStatsCollisions_Type = Counter64
_AcEnetStatsCollisions_Object = MibTableColumn
acEnetStatsCollisions = _AcEnetStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 17),
    _AcEnetStatsCollisions_Type()
)
acEnetStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsCollisions.setStatus("current")
_AcEnetStatsPkts64Octets_Type = Counter64
_AcEnetStatsPkts64Octets_Object = MibTableColumn
acEnetStatsPkts64Octets = _AcEnetStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 18),
    _AcEnetStatsPkts64Octets_Type()
)
acEnetStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsPkts64Octets.setStatus("current")
_AcEnetStatsPkts65to127Octets_Type = Counter64
_AcEnetStatsPkts65to127Octets_Object = MibTableColumn
acEnetStatsPkts65to127Octets = _AcEnetStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 19),
    _AcEnetStatsPkts65to127Octets_Type()
)
acEnetStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsPkts65to127Octets.setStatus("current")
_AcEnetStatsPkts128to255Octets_Type = Counter64
_AcEnetStatsPkts128to255Octets_Object = MibTableColumn
acEnetStatsPkts128to255Octets = _AcEnetStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 20),
    _AcEnetStatsPkts128to255Octets_Type()
)
acEnetStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsPkts128to255Octets.setStatus("current")
_AcEnetStatsPkts256to511Octets_Type = Counter64
_AcEnetStatsPkts256to511Octets_Object = MibTableColumn
acEnetStatsPkts256to511Octets = _AcEnetStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 21),
    _AcEnetStatsPkts256to511Octets_Type()
)
acEnetStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsPkts256to511Octets.setStatus("current")
_AcEnetStatsPkts512to1023Octets_Type = Counter64
_AcEnetStatsPkts512to1023Octets_Object = MibTableColumn
acEnetStatsPkts512to1023Octets = _AcEnetStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 22),
    _AcEnetStatsPkts512to1023Octets_Type()
)
acEnetStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsPkts512to1023Octets.setStatus("current")
_AcEnetStatsPkts1024to1518Octets_Type = Counter64
_AcEnetStatsPkts1024to1518Octets_Object = MibTableColumn
acEnetStatsPkts1024to1518Octets = _AcEnetStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 23),
    _AcEnetStatsPkts1024to1518Octets_Type()
)
acEnetStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsPkts1024to1518Octets.setStatus("current")
_AcEnetStatsCurrentRxBandwidth_Type = Integer32
_AcEnetStatsCurrentRxBandwidth_Object = MibTableColumn
acEnetStatsCurrentRxBandwidth = _AcEnetStatsCurrentRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 24),
    _AcEnetStatsCurrentRxBandwidth_Type()
)
acEnetStatsCurrentRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsCurrentRxBandwidth.setStatus("current")
_AcEnetStatsCurrentTxBandwidth_Type = Integer32
_AcEnetStatsCurrentTxBandwidth_Object = MibTableColumn
acEnetStatsCurrentTxBandwidth = _AcEnetStatsCurrentTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 25),
    _AcEnetStatsCurrentTxBandwidth_Type()
)
acEnetStatsCurrentTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsCurrentTxBandwidth.setStatus("current")
_AcEnetStatsPausePktsRx_Type = Counter32
_AcEnetStatsPausePktsRx_Object = MibTableColumn
acEnetStatsPausePktsRx = _AcEnetStatsPausePktsRx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 26),
    _AcEnetStatsPausePktsRx_Type()
)
acEnetStatsPausePktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsPausePktsRx.setStatus("current")
_AcEnetStatsPausePktsTx_Type = Counter32
_AcEnetStatsPausePktsTx_Object = MibTableColumn
acEnetStatsPausePktsTx = _AcEnetStatsPausePktsTx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 27),
    _AcEnetStatsPausePktsTx_Type()
)
acEnetStatsPausePktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsPausePktsTx.setStatus("current")
_AcEnetStatsPkts1519to1522Octets_Type = Counter64
_AcEnetStatsPkts1519to1522Octets_Object = MibTableColumn
acEnetStatsPkts1519to1522Octets = _AcEnetStatsPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 1, 1, 28),
    _AcEnetStatsPkts1519to1522Octets_Type()
)
acEnetStatsPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetStatsPkts1519to1522Octets.setStatus("current")
_AcEnetCfgTable_Object = MibTable
acEnetCfgTable = _AcEnetCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    acEnetCfgTable.setStatus("current")
_AcEnetCfgEntry_Object = MibTableRow
acEnetCfgEntry = _AcEnetCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1)
)
acEnetCfgEntry.setIndexNames(
    (0, "APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgNodeId"),
    (0, "APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgSlot"),
    (0, "APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgPort"),
)
if mibBuilder.loadTexts:
    acEnetCfgEntry.setStatus("current")
_AcEnetCfgNodeId_Type = AcNodeId
_AcEnetCfgNodeId_Object = MibTableColumn
acEnetCfgNodeId = _AcEnetCfgNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 1),
    _AcEnetCfgNodeId_Type()
)
acEnetCfgNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acEnetCfgNodeId.setStatus("current")
_AcEnetCfgSlot_Type = AcSlotNumber
_AcEnetCfgSlot_Object = MibTableColumn
acEnetCfgSlot = _AcEnetCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 2),
    _AcEnetCfgSlot_Type()
)
acEnetCfgSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acEnetCfgSlot.setStatus("current")
_AcEnetCfgPort_Type = AcPortNumber
_AcEnetCfgPort_Object = MibTableColumn
acEnetCfgPort = _AcEnetCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 3),
    _AcEnetCfgPort_Type()
)
acEnetCfgPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acEnetCfgPort.setStatus("current")


class _AcEnetCfgAdminStatus_Type(AcAdminStatus):
    """Custom type acEnetCfgAdminStatus based on AcAdminStatus"""


_AcEnetCfgAdminStatus_Object = MibTableColumn
acEnetCfgAdminStatus = _AcEnetCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 4),
    _AcEnetCfgAdminStatus_Type()
)
acEnetCfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acEnetCfgAdminStatus.setStatus("current")
_AcEnetCfgOpStatus_Type = AcOpStatus
_AcEnetCfgOpStatus_Object = MibTableColumn
acEnetCfgOpStatus = _AcEnetCfgOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 5),
    _AcEnetCfgOpStatus_Type()
)
acEnetCfgOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetCfgOpStatus.setStatus("current")
_AcEnetCfgOpCode_Type = Integer32
_AcEnetCfgOpCode_Object = MibTableColumn
acEnetCfgOpCode = _AcEnetCfgOpCode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 6),
    _AcEnetCfgOpCode_Type()
)
acEnetCfgOpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetCfgOpCode.setStatus("current")


class _AcEnetCfgStatsReset_Type(TruthValue):
    """Custom type acEnetCfgStatsReset based on TruthValue"""


_AcEnetCfgStatsReset_Object = MibTableColumn
acEnetCfgStatsReset = _AcEnetCfgStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 7),
    _AcEnetCfgStatsReset_Type()
)
acEnetCfgStatsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acEnetCfgStatsReset.setStatus("current")


class _AcEnetCfgMediaType_Type(Integer32):
    """Custom type acEnetCfgMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gbe", 2),
          ("mbe", 1),
          ("unknown", 0))
    )


_AcEnetCfgMediaType_Type.__name__ = "Integer32"
_AcEnetCfgMediaType_Object = MibTableColumn
acEnetCfgMediaType = _AcEnetCfgMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 8),
    _AcEnetCfgMediaType_Type()
)
acEnetCfgMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetCfgMediaType.setStatus("current")


class _AcEnetCfgPhysicalAddress_Type(PhysAddress):
    """Custom type acEnetCfgPhysicalAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AcEnetCfgPhysicalAddress_Type.__name__ = "PhysAddress"
_AcEnetCfgPhysicalAddress_Object = MibTableColumn
acEnetCfgPhysicalAddress = _AcEnetCfgPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 9),
    _AcEnetCfgPhysicalAddress_Type()
)
acEnetCfgPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetCfgPhysicalAddress.setStatus("current")
_AcEnetCfgActiveMediaSlot_Type = AcSlotNumber
_AcEnetCfgActiveMediaSlot_Object = MibTableColumn
acEnetCfgActiveMediaSlot = _AcEnetCfgActiveMediaSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 10),
    _AcEnetCfgActiveMediaSlot_Type()
)
acEnetCfgActiveMediaSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetCfgActiveMediaSlot.setStatus("current")
_AcEnetCfgStandbyMediaSlot_Type = AcSlotNumber
_AcEnetCfgStandbyMediaSlot_Object = MibTableColumn
acEnetCfgStandbyMediaSlot = _AcEnetCfgStandbyMediaSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 11),
    _AcEnetCfgStandbyMediaSlot_Type()
)
acEnetCfgStandbyMediaSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetCfgStandbyMediaSlot.setStatus("current")


class _AcEnetCfgMultiServiceEnable_Type(TruthValue):
    """Custom type acEnetCfgMultiServiceEnable based on TruthValue"""


_AcEnetCfgMultiServiceEnable_Object = MibTableColumn
acEnetCfgMultiServiceEnable = _AcEnetCfgMultiServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 12),
    _AcEnetCfgMultiServiceEnable_Type()
)
acEnetCfgMultiServiceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acEnetCfgMultiServiceEnable.setStatus("current")


class _AcEnetCfgSpeed_Type(AcEnetSpeed):
    """Custom type acEnetCfgSpeed based on AcEnetSpeed"""


_AcEnetCfgSpeed_Object = MibTableColumn
acEnetCfgSpeed = _AcEnetCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 13),
    _AcEnetCfgSpeed_Type()
)
acEnetCfgSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acEnetCfgSpeed.setStatus("current")


class _AcEnetCfgDuplexity_Type(AcEnetDuplexity):
    """Custom type acEnetCfgDuplexity based on AcEnetDuplexity"""


_AcEnetCfgDuplexity_Object = MibTableColumn
acEnetCfgDuplexity = _AcEnetCfgDuplexity_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 14),
    _AcEnetCfgDuplexity_Type()
)
acEnetCfgDuplexity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acEnetCfgDuplexity.setStatus("current")
_AcEnetCfgCurrentSpeed_Type = AcEnetSpeed
_AcEnetCfgCurrentSpeed_Object = MibTableColumn
acEnetCfgCurrentSpeed = _AcEnetCfgCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 15),
    _AcEnetCfgCurrentSpeed_Type()
)
acEnetCfgCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetCfgCurrentSpeed.setStatus("current")
_AcEnetCfgCurrentDuplexity_Type = AcEnetDuplexity
_AcEnetCfgCurrentDuplexity_Object = MibTableColumn
acEnetCfgCurrentDuplexity = _AcEnetCfgCurrentDuplexity_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 16),
    _AcEnetCfgCurrentDuplexity_Type()
)
acEnetCfgCurrentDuplexity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetCfgCurrentDuplexity.setStatus("current")


class _AcEnetCfgInterfaceName_Type(DisplayString):
    """Custom type acEnetCfgInterfaceName based on DisplayString"""
    defaultValue = OctetString("Ethernet Interface")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcEnetCfgInterfaceName_Type.__name__ = "DisplayString"
_AcEnetCfgInterfaceName_Object = MibTableColumn
acEnetCfgInterfaceName = _AcEnetCfgInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 17),
    _AcEnetCfgInterfaceName_Type()
)
acEnetCfgInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acEnetCfgInterfaceName.setStatus("current")
_AcEnetCfgLinkState_Type = AcEnetLinkState
_AcEnetCfgLinkState_Object = MibTableColumn
acEnetCfgLinkState = _AcEnetCfgLinkState_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 18),
    _AcEnetCfgLinkState_Type()
)
acEnetCfgLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetCfgLinkState.setStatus("current")


class _AcEnetCfgAutoNegotiate_Type(TruthValue):
    """Custom type acEnetCfgAutoNegotiate based on TruthValue"""


_AcEnetCfgAutoNegotiate_Object = MibTableColumn
acEnetCfgAutoNegotiate = _AcEnetCfgAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 19),
    _AcEnetCfgAutoNegotiate_Type()
)
acEnetCfgAutoNegotiate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acEnetCfgAutoNegotiate.setStatus("current")


class _AcEnetCfgPauseAdminMode_Type(Integer32):
    """Custom type acEnetCfgPauseAdminMode based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("enabledRcv", 3),
          ("enabledXmit", 2),
          ("enabledXmitAndRcv", 4))
    )


_AcEnetCfgPauseAdminMode_Type.__name__ = "Integer32"
_AcEnetCfgPauseAdminMode_Object = MibTableColumn
acEnetCfgPauseAdminMode = _AcEnetCfgPauseAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 20),
    _AcEnetCfgPauseAdminMode_Type()
)
acEnetCfgPauseAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEnetCfgPauseAdminMode.setStatus("current")


class _AcEnetCfgPauseOperMode_Type(Integer32):
    """Custom type acEnetCfgPauseOperMode based on Integer32"""
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
        *(("disabled", 1),
          ("enabledRcv", 3),
          ("enabledXmit", 2),
          ("enabledXmitAndRcv", 4))
    )


_AcEnetCfgPauseOperMode_Type.__name__ = "Integer32"
_AcEnetCfgPauseOperMode_Object = MibTableColumn
acEnetCfgPauseOperMode = _AcEnetCfgPauseOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 2, 1, 21),
    _AcEnetCfgPauseOperMode_Type()
)
acEnetCfgPauseOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acEnetCfgPauseOperMode.setStatus("current")

# Managed Objects groups


# Notification objects

acEnetLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 0, 1)
)
acEnetLinkDownTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgNodeId"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgSlot"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgPort"))
)
if mibBuilder.loadTexts:
    acEnetLinkDownTrap.setStatus(
        "current"
    )

acEnetLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 0, 2)
)
acEnetLinkUpTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgNodeId"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgSlot"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgPort"))
)
if mibBuilder.loadTexts:
    acEnetLinkUpTrap.setStatus(
        "current"
    )

acEnetStatsResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 0, 3)
)
acEnetStatsResetTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgNodeId"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgSlot"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgPort"))
)
if mibBuilder.loadTexts:
    acEnetStatsResetTrap.setStatus(
        "current"
    )

acEnetFailoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 0, 4)
)
acEnetFailoverTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgNodeId"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgSlot"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgPort"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgOpCode"))
)
if mibBuilder.loadTexts:
    acEnetFailoverTrap.setStatus(
        "current"
    )

acEnetCfgErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 3, 0, 5)
)
acEnetCfgErrorTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgNodeId"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgSlot"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgPort"),
        ("APPIAN-PPORT-ETHERNET-MIB", "acEnetCfgOpCode"))
)
if mibBuilder.loadTexts:
    acEnetCfgErrorTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-PPORT-ETHERNET-MIB",
    **{"AcEnetSpeed": AcEnetSpeed,
       "AcEnetDuplexity": AcEnetDuplexity,
       "AcEnetLinkState": AcEnetLinkState,
       "acEnet": acEnet,
       "acEnetTraps": acEnetTraps,
       "acEnetLinkDownTrap": acEnetLinkDownTrap,
       "acEnetLinkUpTrap": acEnetLinkUpTrap,
       "acEnetStatsResetTrap": acEnetStatsResetTrap,
       "acEnetFailoverTrap": acEnetFailoverTrap,
       "acEnetCfgErrorTrap": acEnetCfgErrorTrap,
       "acEnetStatsTable": acEnetStatsTable,
       "acEnetStatsEntry": acEnetStatsEntry,
       "acEnetStatsNodeId": acEnetStatsNodeId,
       "acEnetStatsSlot": acEnetStatsSlot,
       "acEnetStatsPort": acEnetStatsPort,
       "acEnetStatsPktsRx": acEnetStatsPktsRx,
       "acEnetStatsPktsTx": acEnetStatsPktsTx,
       "acEnetStatsOctetsRx": acEnetStatsOctetsRx,
       "acEnetStatsOctetsTx": acEnetStatsOctetsTx,
       "acEnetStatsBcastPktsRx": acEnetStatsBcastPktsRx,
       "acEnetStatsBcastPktsTx": acEnetStatsBcastPktsTx,
       "acEnetStatsMcastPktsRx": acEnetStatsMcastPktsRx,
       "acEnetStatsMcastPktsTx": acEnetStatsMcastPktsTx,
       "acEnetStatsCrcAlignErrors": acEnetStatsCrcAlignErrors,
       "acEnetStatsUndersizedPkts": acEnetStatsUndersizedPkts,
       "acEnetStatsOversizedPkts": acEnetStatsOversizedPkts,
       "acEnetStatsFragmentedPkts": acEnetStatsFragmentedPkts,
       "acEnetStatsJabbers": acEnetStatsJabbers,
       "acEnetStatsCollisions": acEnetStatsCollisions,
       "acEnetStatsPkts64Octets": acEnetStatsPkts64Octets,
       "acEnetStatsPkts65to127Octets": acEnetStatsPkts65to127Octets,
       "acEnetStatsPkts128to255Octets": acEnetStatsPkts128to255Octets,
       "acEnetStatsPkts256to511Octets": acEnetStatsPkts256to511Octets,
       "acEnetStatsPkts512to1023Octets": acEnetStatsPkts512to1023Octets,
       "acEnetStatsPkts1024to1518Octets": acEnetStatsPkts1024to1518Octets,
       "acEnetStatsCurrentRxBandwidth": acEnetStatsCurrentRxBandwidth,
       "acEnetStatsCurrentTxBandwidth": acEnetStatsCurrentTxBandwidth,
       "acEnetStatsPausePktsRx": acEnetStatsPausePktsRx,
       "acEnetStatsPausePktsTx": acEnetStatsPausePktsTx,
       "acEnetStatsPkts1519to1522Octets": acEnetStatsPkts1519to1522Octets,
       "acEnetCfgTable": acEnetCfgTable,
       "acEnetCfgEntry": acEnetCfgEntry,
       "acEnetCfgNodeId": acEnetCfgNodeId,
       "acEnetCfgSlot": acEnetCfgSlot,
       "acEnetCfgPort": acEnetCfgPort,
       "acEnetCfgAdminStatus": acEnetCfgAdminStatus,
       "acEnetCfgOpStatus": acEnetCfgOpStatus,
       "acEnetCfgOpCode": acEnetCfgOpCode,
       "acEnetCfgStatsReset": acEnetCfgStatsReset,
       "acEnetCfgMediaType": acEnetCfgMediaType,
       "acEnetCfgPhysicalAddress": acEnetCfgPhysicalAddress,
       "acEnetCfgActiveMediaSlot": acEnetCfgActiveMediaSlot,
       "acEnetCfgStandbyMediaSlot": acEnetCfgStandbyMediaSlot,
       "acEnetCfgMultiServiceEnable": acEnetCfgMultiServiceEnable,
       "acEnetCfgSpeed": acEnetCfgSpeed,
       "acEnetCfgDuplexity": acEnetCfgDuplexity,
       "acEnetCfgCurrentSpeed": acEnetCfgCurrentSpeed,
       "acEnetCfgCurrentDuplexity": acEnetCfgCurrentDuplexity,
       "acEnetCfgInterfaceName": acEnetCfgInterfaceName,
       "acEnetCfgLinkState": acEnetCfgLinkState,
       "acEnetCfgAutoNegotiate": acEnetCfgAutoNegotiate,
       "acEnetCfgPauseAdminMode": acEnetCfgPauseAdminMode,
       "acEnetCfgPauseOperMode": acEnetCfgPauseOperMode}
)
