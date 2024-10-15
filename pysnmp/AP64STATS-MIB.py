# SNMP MIB module (AP64STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AP64STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:07 2024
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

(ap64Stats,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "ap64Stats")

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

ap64StatsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 1)
)


# Types definitions



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class OwnerString(DisplayString):
    """Custom type OwnerString based on DisplayString"""




class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ap64dot3StatsTable_Object = MibTable
ap64dot3StatsTable = _Ap64dot3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2)
)
if mibBuilder.loadTexts:
    ap64dot3StatsTable.setStatus("current")
_Ap64dot3StatsEntry_Object = MibTableRow
ap64dot3StatsEntry = _Ap64dot3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1)
)
ap64dot3StatsEntry.setIndexNames(
    (0, "AP64STATS-MIB", "ap64dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    ap64dot3StatsEntry.setStatus("current")
_Ap64dot3StatsIndex_Type = Integer32
_Ap64dot3StatsIndex_Object = MibTableColumn
ap64dot3StatsIndex = _Ap64dot3StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 1),
    _Ap64dot3StatsIndex_Type()
)
ap64dot3StatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsIndex.setStatus("current")
_Ap64dot3StatsAlignmentErrors_Type = Counter64
_Ap64dot3StatsAlignmentErrors_Object = MibTableColumn
ap64dot3StatsAlignmentErrors = _Ap64dot3StatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 2),
    _Ap64dot3StatsAlignmentErrors_Type()
)
ap64dot3StatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsAlignmentErrors.setStatus("current")
_Ap64dot3StatsFCSErrors_Type = Counter64
_Ap64dot3StatsFCSErrors_Object = MibTableColumn
ap64dot3StatsFCSErrors = _Ap64dot3StatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 3),
    _Ap64dot3StatsFCSErrors_Type()
)
ap64dot3StatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsFCSErrors.setStatus("current")
_Ap64dot3StatsSingleCollisionFrames_Type = Counter64
_Ap64dot3StatsSingleCollisionFrames_Object = MibTableColumn
ap64dot3StatsSingleCollisionFrames = _Ap64dot3StatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 4),
    _Ap64dot3StatsSingleCollisionFrames_Type()
)
ap64dot3StatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsSingleCollisionFrames.setStatus("current")
_Ap64dot3StatsMultipleCollisionFrames_Type = Counter64
_Ap64dot3StatsMultipleCollisionFrames_Object = MibTableColumn
ap64dot3StatsMultipleCollisionFrames = _Ap64dot3StatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 5),
    _Ap64dot3StatsMultipleCollisionFrames_Type()
)
ap64dot3StatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsMultipleCollisionFrames.setStatus("current")
_Ap64dot3StatsSQETestErrors_Type = Counter64
_Ap64dot3StatsSQETestErrors_Object = MibTableColumn
ap64dot3StatsSQETestErrors = _Ap64dot3StatsSQETestErrors_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 6),
    _Ap64dot3StatsSQETestErrors_Type()
)
ap64dot3StatsSQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsSQETestErrors.setStatus("current")
_Ap64dot3StatsDeferredTransmissions_Type = Counter64
_Ap64dot3StatsDeferredTransmissions_Object = MibTableColumn
ap64dot3StatsDeferredTransmissions = _Ap64dot3StatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 7),
    _Ap64dot3StatsDeferredTransmissions_Type()
)
ap64dot3StatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsDeferredTransmissions.setStatus("current")
_Ap64dot3StatsLateCollisions_Type = Counter64
_Ap64dot3StatsLateCollisions_Object = MibTableColumn
ap64dot3StatsLateCollisions = _Ap64dot3StatsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 8),
    _Ap64dot3StatsLateCollisions_Type()
)
ap64dot3StatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsLateCollisions.setStatus("current")
_Ap64dot3StatsExcessiveCollisions_Type = Counter64
_Ap64dot3StatsExcessiveCollisions_Object = MibTableColumn
ap64dot3StatsExcessiveCollisions = _Ap64dot3StatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 9),
    _Ap64dot3StatsExcessiveCollisions_Type()
)
ap64dot3StatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsExcessiveCollisions.setStatus("current")
_Ap64dot3StatsInternalMacTransmitErrors_Type = Counter64
_Ap64dot3StatsInternalMacTransmitErrors_Object = MibTableColumn
ap64dot3StatsInternalMacTransmitErrors = _Ap64dot3StatsInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 10),
    _Ap64dot3StatsInternalMacTransmitErrors_Type()
)
ap64dot3StatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsInternalMacTransmitErrors.setStatus("current")
_Ap64dot3StatsCarrierSenseErrors_Type = Counter64
_Ap64dot3StatsCarrierSenseErrors_Object = MibTableColumn
ap64dot3StatsCarrierSenseErrors = _Ap64dot3StatsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 11),
    _Ap64dot3StatsCarrierSenseErrors_Type()
)
ap64dot3StatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsCarrierSenseErrors.setStatus("current")
_Ap64dot3StatsFrameTooLongs_Type = Counter64
_Ap64dot3StatsFrameTooLongs_Object = MibTableColumn
ap64dot3StatsFrameTooLongs = _Ap64dot3StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 13),
    _Ap64dot3StatsFrameTooLongs_Type()
)
ap64dot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsFrameTooLongs.setStatus("current")
_Ap64dot3StatsInternalMacReceiveErrors_Type = Counter64
_Ap64dot3StatsInternalMacReceiveErrors_Object = MibTableColumn
ap64dot3StatsInternalMacReceiveErrors = _Ap64dot3StatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 16),
    _Ap64dot3StatsInternalMacReceiveErrors_Type()
)
ap64dot3StatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64dot3StatsInternalMacReceiveErrors.setStatus("current")
_Ap64ifTable_Object = MibTable
ap64ifTable = _Ap64ifTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3)
)
if mibBuilder.loadTexts:
    ap64ifTable.setStatus("current")
_Ap64ifEntry_Object = MibTableRow
ap64ifEntry = _Ap64ifEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1)
)
ap64ifEntry.setIndexNames(
    (0, "AP64STATS-MIB", "ap64ifIndex"),
)
if mibBuilder.loadTexts:
    ap64ifEntry.setStatus("current")
_Ap64ifIndex_Type = Integer32
_Ap64ifIndex_Object = MibTableColumn
ap64ifIndex = _Ap64ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 1),
    _Ap64ifIndex_Type()
)
ap64ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifIndex.setStatus("current")


class _Ap64ifDescr_Type(DisplayString):
    """Custom type ap64ifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ap64ifDescr_Type.__name__ = "DisplayString"
_Ap64ifDescr_Object = MibTableColumn
ap64ifDescr = _Ap64ifDescr_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 2),
    _Ap64ifDescr_Type()
)
ap64ifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifDescr.setStatus("current")


class _Ap64ifType_Type(Integer32):
    """Custom type ap64ifType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("basicISDN", 20),
          ("ddn-x25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("ethernet-3Mbit", 26),
          ("ethernet-csmacd", 6),
          ("fddi", 15),
          ("frame-relay", 32),
          ("hdh1822", 3),
          ("hyperchannel", 14),
          ("iso88023-csmacd", 7),
          ("iso88024-tokenBus", 8),
          ("iso88025-tokenRing", 9),
          ("iso88026-man", 10),
          ("lapb", 16),
          ("nsip", 27),
          ("other", 1),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propPointToPointSerial", 22),
          ("proteon-10Mbit", 12),
          ("proteon-80Mbit", 13),
          ("regular1822", 2),
          ("rfc877-x25", 5),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("softwareLoopback", 24),
          ("starLan", 11),
          ("ultra", 29))
    )


_Ap64ifType_Type.__name__ = "Integer32"
_Ap64ifType_Object = MibTableColumn
ap64ifType = _Ap64ifType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 3),
    _Ap64ifType_Type()
)
ap64ifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifType.setStatus("current")
_Ap64ifMtu_Type = Integer32
_Ap64ifMtu_Object = MibTableColumn
ap64ifMtu = _Ap64ifMtu_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 4),
    _Ap64ifMtu_Type()
)
ap64ifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifMtu.setStatus("current")
_Ap64ifSpeed_Type = Gauge32
_Ap64ifSpeed_Object = MibTableColumn
ap64ifSpeed = _Ap64ifSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 5),
    _Ap64ifSpeed_Type()
)
ap64ifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifSpeed.setStatus("current")
_Ap64ifPhysAddress_Type = PhysAddress
_Ap64ifPhysAddress_Object = MibTableColumn
ap64ifPhysAddress = _Ap64ifPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 6),
    _Ap64ifPhysAddress_Type()
)
ap64ifPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifPhysAddress.setStatus("current")


class _Ap64ifAdminStatus_Type(Integer32):
    """Custom type ap64ifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_Ap64ifAdminStatus_Type.__name__ = "Integer32"
_Ap64ifAdminStatus_Object = MibTableColumn
ap64ifAdminStatus = _Ap64ifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 7),
    _Ap64ifAdminStatus_Type()
)
ap64ifAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifAdminStatus.setStatus("current")


class _Ap64ifOperStatus_Type(Integer32):
    """Custom type ap64ifOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_Ap64ifOperStatus_Type.__name__ = "Integer32"
_Ap64ifOperStatus_Object = MibTableColumn
ap64ifOperStatus = _Ap64ifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 8),
    _Ap64ifOperStatus_Type()
)
ap64ifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifOperStatus.setStatus("current")
_Ap64ifLastChange_Type = TimeTicks
_Ap64ifLastChange_Object = MibTableColumn
ap64ifLastChange = _Ap64ifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 9),
    _Ap64ifLastChange_Type()
)
ap64ifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifLastChange.setStatus("current")
_Ap64ifInOctets_Type = Counter64
_Ap64ifInOctets_Object = MibTableColumn
ap64ifInOctets = _Ap64ifInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 10),
    _Ap64ifInOctets_Type()
)
ap64ifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifInOctets.setStatus("current")
_Ap64ifInUcastPkts_Type = Counter64
_Ap64ifInUcastPkts_Object = MibTableColumn
ap64ifInUcastPkts = _Ap64ifInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 11),
    _Ap64ifInUcastPkts_Type()
)
ap64ifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifInUcastPkts.setStatus("current")
_Ap64ifInNUcastPkts_Type = Counter64
_Ap64ifInNUcastPkts_Object = MibTableColumn
ap64ifInNUcastPkts = _Ap64ifInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 12),
    _Ap64ifInNUcastPkts_Type()
)
ap64ifInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifInNUcastPkts.setStatus("current")
_Ap64ifInDiscards_Type = Counter64
_Ap64ifInDiscards_Object = MibTableColumn
ap64ifInDiscards = _Ap64ifInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 13),
    _Ap64ifInDiscards_Type()
)
ap64ifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifInDiscards.setStatus("current")
_Ap64ifInErrors_Type = Counter64
_Ap64ifInErrors_Object = MibTableColumn
ap64ifInErrors = _Ap64ifInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 14),
    _Ap64ifInErrors_Type()
)
ap64ifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifInErrors.setStatus("current")
_Ap64ifInUnknownProtos_Type = Counter64
_Ap64ifInUnknownProtos_Object = MibTableColumn
ap64ifInUnknownProtos = _Ap64ifInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 15),
    _Ap64ifInUnknownProtos_Type()
)
ap64ifInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifInUnknownProtos.setStatus("current")
_Ap64ifOutOctets_Type = Counter64
_Ap64ifOutOctets_Object = MibTableColumn
ap64ifOutOctets = _Ap64ifOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 16),
    _Ap64ifOutOctets_Type()
)
ap64ifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifOutOctets.setStatus("current")
_Ap64ifOutUcastPkts_Type = Counter64
_Ap64ifOutUcastPkts_Object = MibTableColumn
ap64ifOutUcastPkts = _Ap64ifOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 17),
    _Ap64ifOutUcastPkts_Type()
)
ap64ifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifOutUcastPkts.setStatus("current")
_Ap64ifOutNUcastPkts_Type = Counter64
_Ap64ifOutNUcastPkts_Object = MibTableColumn
ap64ifOutNUcastPkts = _Ap64ifOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 18),
    _Ap64ifOutNUcastPkts_Type()
)
ap64ifOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifOutNUcastPkts.setStatus("current")
_Ap64ifOutDiscards_Type = Counter64
_Ap64ifOutDiscards_Object = MibTableColumn
ap64ifOutDiscards = _Ap64ifOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 19),
    _Ap64ifOutDiscards_Type()
)
ap64ifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifOutDiscards.setStatus("current")
_Ap64ifOutErrors_Type = Counter64
_Ap64ifOutErrors_Object = MibTableColumn
ap64ifOutErrors = _Ap64ifOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 20),
    _Ap64ifOutErrors_Type()
)
ap64ifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifOutErrors.setStatus("current")
_Ap64ifOutQLen_Type = Gauge32
_Ap64ifOutQLen_Object = MibTableColumn
ap64ifOutQLen = _Ap64ifOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 21),
    _Ap64ifOutQLen_Type()
)
ap64ifOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifOutQLen.setStatus("current")
_Ap64ifSpecific_Type = ObjectIdentifier
_Ap64ifSpecific_Object = MibTableColumn
ap64ifSpecific = _Ap64ifSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 22),
    _Ap64ifSpecific_Type()
)
ap64ifSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64ifSpecific.setStatus("current")
_Ap64etherStatsTable_Object = MibTable
ap64etherStatsTable = _Ap64etherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4)
)
if mibBuilder.loadTexts:
    ap64etherStatsTable.setStatus("current")
_Ap64etherStatsEntry_Object = MibTableRow
ap64etherStatsEntry = _Ap64etherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1)
)
ap64etherStatsEntry.setIndexNames(
    (0, "AP64STATS-MIB", "ap64etherStatsIndex"),
)
if mibBuilder.loadTexts:
    ap64etherStatsEntry.setStatus("current")


class _Ap64etherStatsIndex_Type(Integer32):
    """Custom type ap64etherStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ap64etherStatsIndex_Type.__name__ = "Integer32"
_Ap64etherStatsIndex_Object = MibTableColumn
ap64etherStatsIndex = _Ap64etherStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 1),
    _Ap64etherStatsIndex_Type()
)
ap64etherStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsIndex.setStatus("current")
_Ap64etherStatsDataSource_Type = ObjectIdentifier
_Ap64etherStatsDataSource_Object = MibTableColumn
ap64etherStatsDataSource = _Ap64etherStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 2),
    _Ap64etherStatsDataSource_Type()
)
ap64etherStatsDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsDataSource.setStatus("current")
_Ap64etherStatsDropEvents_Type = Counter64
_Ap64etherStatsDropEvents_Object = MibTableColumn
ap64etherStatsDropEvents = _Ap64etherStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 3),
    _Ap64etherStatsDropEvents_Type()
)
ap64etherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsDropEvents.setStatus("current")
_Ap64etherStatsOctets_Type = Counter64
_Ap64etherStatsOctets_Object = MibTableColumn
ap64etherStatsOctets = _Ap64etherStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 4),
    _Ap64etherStatsOctets_Type()
)
ap64etherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsOctets.setStatus("current")
_Ap64etherStatsPkts_Type = Counter64
_Ap64etherStatsPkts_Object = MibTableColumn
ap64etherStatsPkts = _Ap64etherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 5),
    _Ap64etherStatsPkts_Type()
)
ap64etherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsPkts.setStatus("current")
_Ap64etherStatsBroadcastPkts_Type = Counter64
_Ap64etherStatsBroadcastPkts_Object = MibTableColumn
ap64etherStatsBroadcastPkts = _Ap64etherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 6),
    _Ap64etherStatsBroadcastPkts_Type()
)
ap64etherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsBroadcastPkts.setStatus("current")
_Ap64etherStatsMulticastPkts_Type = Counter64
_Ap64etherStatsMulticastPkts_Object = MibTableColumn
ap64etherStatsMulticastPkts = _Ap64etherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 7),
    _Ap64etherStatsMulticastPkts_Type()
)
ap64etherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsMulticastPkts.setStatus("current")
_Ap64etherStatsCRCAlignErrors_Type = Counter64
_Ap64etherStatsCRCAlignErrors_Object = MibTableColumn
ap64etherStatsCRCAlignErrors = _Ap64etherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 8),
    _Ap64etherStatsCRCAlignErrors_Type()
)
ap64etherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsCRCAlignErrors.setStatus("current")
_Ap64etherStatsUndersizePkts_Type = Counter64
_Ap64etherStatsUndersizePkts_Object = MibTableColumn
ap64etherStatsUndersizePkts = _Ap64etherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 9),
    _Ap64etherStatsUndersizePkts_Type()
)
ap64etherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsUndersizePkts.setStatus("current")
_Ap64etherStatsOversizePkts_Type = Counter64
_Ap64etherStatsOversizePkts_Object = MibTableColumn
ap64etherStatsOversizePkts = _Ap64etherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 10),
    _Ap64etherStatsOversizePkts_Type()
)
ap64etherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsOversizePkts.setStatus("current")
_Ap64etherStatsFragments_Type = Counter64
_Ap64etherStatsFragments_Object = MibTableColumn
ap64etherStatsFragments = _Ap64etherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 11),
    _Ap64etherStatsFragments_Type()
)
ap64etherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsFragments.setStatus("current")
_Ap64etherStatsJabbers_Type = Counter64
_Ap64etherStatsJabbers_Object = MibTableColumn
ap64etherStatsJabbers = _Ap64etherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 12),
    _Ap64etherStatsJabbers_Type()
)
ap64etherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsJabbers.setStatus("current")
_Ap64etherStatsCollisions_Type = Counter64
_Ap64etherStatsCollisions_Object = MibTableColumn
ap64etherStatsCollisions = _Ap64etherStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 13),
    _Ap64etherStatsCollisions_Type()
)
ap64etherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsCollisions.setStatus("current")
_Ap64etherStatsPkts64Octets_Type = Counter64
_Ap64etherStatsPkts64Octets_Object = MibTableColumn
ap64etherStatsPkts64Octets = _Ap64etherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 14),
    _Ap64etherStatsPkts64Octets_Type()
)
ap64etherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsPkts64Octets.setStatus("current")
_Ap64etherStatsPkts65to127Octets_Type = Counter64
_Ap64etherStatsPkts65to127Octets_Object = MibTableColumn
ap64etherStatsPkts65to127Octets = _Ap64etherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 15),
    _Ap64etherStatsPkts65to127Octets_Type()
)
ap64etherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsPkts65to127Octets.setStatus("current")
_Ap64etherStatsPkts128to255Octets_Type = Counter64
_Ap64etherStatsPkts128to255Octets_Object = MibTableColumn
ap64etherStatsPkts128to255Octets = _Ap64etherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 16),
    _Ap64etherStatsPkts128to255Octets_Type()
)
ap64etherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsPkts128to255Octets.setStatus("current")
_Ap64etherStatsPkts256to511Octets_Type = Counter64
_Ap64etherStatsPkts256to511Octets_Object = MibTableColumn
ap64etherStatsPkts256to511Octets = _Ap64etherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 17),
    _Ap64etherStatsPkts256to511Octets_Type()
)
ap64etherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsPkts256to511Octets.setStatus("current")
_Ap64etherStatsPkts512to1023Octets_Type = Counter64
_Ap64etherStatsPkts512to1023Octets_Object = MibTableColumn
ap64etherStatsPkts512to1023Octets = _Ap64etherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 18),
    _Ap64etherStatsPkts512to1023Octets_Type()
)
ap64etherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsPkts512to1023Octets.setStatus("current")
_Ap64etherStatsPkts1024to1518Octets_Type = Counter64
_Ap64etherStatsPkts1024to1518Octets_Object = MibTableColumn
ap64etherStatsPkts1024to1518Octets = _Ap64etherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 19),
    _Ap64etherStatsPkts1024to1518Octets_Type()
)
ap64etherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsPkts1024to1518Octets.setStatus("current")
_Ap64etherStatsOwner_Type = OwnerString
_Ap64etherStatsOwner_Object = MibTableColumn
ap64etherStatsOwner = _Ap64etherStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 20),
    _Ap64etherStatsOwner_Type()
)
ap64etherStatsOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsOwner.setStatus("current")
_Ap64etherStatsStatus_Type = EntryStatus
_Ap64etherStatsStatus_Object = MibTableColumn
ap64etherStatsStatus = _Ap64etherStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 21),
    _Ap64etherStatsStatus_Type()
)
ap64etherStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap64etherStatsStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AP64STATS-MIB",
    **{"PhysAddress": PhysAddress,
       "OwnerString": OwnerString,
       "EntryStatus": EntryStatus,
       "ap64StatsMib": ap64StatsMib,
       "ap64dot3StatsTable": ap64dot3StatsTable,
       "ap64dot3StatsEntry": ap64dot3StatsEntry,
       "ap64dot3StatsIndex": ap64dot3StatsIndex,
       "ap64dot3StatsAlignmentErrors": ap64dot3StatsAlignmentErrors,
       "ap64dot3StatsFCSErrors": ap64dot3StatsFCSErrors,
       "ap64dot3StatsSingleCollisionFrames": ap64dot3StatsSingleCollisionFrames,
       "ap64dot3StatsMultipleCollisionFrames": ap64dot3StatsMultipleCollisionFrames,
       "ap64dot3StatsSQETestErrors": ap64dot3StatsSQETestErrors,
       "ap64dot3StatsDeferredTransmissions": ap64dot3StatsDeferredTransmissions,
       "ap64dot3StatsLateCollisions": ap64dot3StatsLateCollisions,
       "ap64dot3StatsExcessiveCollisions": ap64dot3StatsExcessiveCollisions,
       "ap64dot3StatsInternalMacTransmitErrors": ap64dot3StatsInternalMacTransmitErrors,
       "ap64dot3StatsCarrierSenseErrors": ap64dot3StatsCarrierSenseErrors,
       "ap64dot3StatsFrameTooLongs": ap64dot3StatsFrameTooLongs,
       "ap64dot3StatsInternalMacReceiveErrors": ap64dot3StatsInternalMacReceiveErrors,
       "ap64ifTable": ap64ifTable,
       "ap64ifEntry": ap64ifEntry,
       "ap64ifIndex": ap64ifIndex,
       "ap64ifDescr": ap64ifDescr,
       "ap64ifType": ap64ifType,
       "ap64ifMtu": ap64ifMtu,
       "ap64ifSpeed": ap64ifSpeed,
       "ap64ifPhysAddress": ap64ifPhysAddress,
       "ap64ifAdminStatus": ap64ifAdminStatus,
       "ap64ifOperStatus": ap64ifOperStatus,
       "ap64ifLastChange": ap64ifLastChange,
       "ap64ifInOctets": ap64ifInOctets,
       "ap64ifInUcastPkts": ap64ifInUcastPkts,
       "ap64ifInNUcastPkts": ap64ifInNUcastPkts,
       "ap64ifInDiscards": ap64ifInDiscards,
       "ap64ifInErrors": ap64ifInErrors,
       "ap64ifInUnknownProtos": ap64ifInUnknownProtos,
       "ap64ifOutOctets": ap64ifOutOctets,
       "ap64ifOutUcastPkts": ap64ifOutUcastPkts,
       "ap64ifOutNUcastPkts": ap64ifOutNUcastPkts,
       "ap64ifOutDiscards": ap64ifOutDiscards,
       "ap64ifOutErrors": ap64ifOutErrors,
       "ap64ifOutQLen": ap64ifOutQLen,
       "ap64ifSpecific": ap64ifSpecific,
       "ap64etherStatsTable": ap64etherStatsTable,
       "ap64etherStatsEntry": ap64etherStatsEntry,
       "ap64etherStatsIndex": ap64etherStatsIndex,
       "ap64etherStatsDataSource": ap64etherStatsDataSource,
       "ap64etherStatsDropEvents": ap64etherStatsDropEvents,
       "ap64etherStatsOctets": ap64etherStatsOctets,
       "ap64etherStatsPkts": ap64etherStatsPkts,
       "ap64etherStatsBroadcastPkts": ap64etherStatsBroadcastPkts,
       "ap64etherStatsMulticastPkts": ap64etherStatsMulticastPkts,
       "ap64etherStatsCRCAlignErrors": ap64etherStatsCRCAlignErrors,
       "ap64etherStatsUndersizePkts": ap64etherStatsUndersizePkts,
       "ap64etherStatsOversizePkts": ap64etherStatsOversizePkts,
       "ap64etherStatsFragments": ap64etherStatsFragments,
       "ap64etherStatsJabbers": ap64etherStatsJabbers,
       "ap64etherStatsCollisions": ap64etherStatsCollisions,
       "ap64etherStatsPkts64Octets": ap64etherStatsPkts64Octets,
       "ap64etherStatsPkts65to127Octets": ap64etherStatsPkts65to127Octets,
       "ap64etherStatsPkts128to255Octets": ap64etherStatsPkts128to255Octets,
       "ap64etherStatsPkts256to511Octets": ap64etherStatsPkts256to511Octets,
       "ap64etherStatsPkts512to1023Octets": ap64etherStatsPkts512to1023Octets,
       "ap64etherStatsPkts1024to1518Octets": ap64etherStatsPkts1024to1518Octets,
       "ap64etherStatsOwner": ap64etherStatsOwner,
       "ap64etherStatsStatus": ap64etherStatsStatus}
)
