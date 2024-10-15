# SNMP MIB module (CNT21-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNT21-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:54 2024
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

(cnt2Mib2,) = mibBuilder.importSymbols(
    "CNT2-MIB",
    "cnt2Mib2")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cnt2Interface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2)
)
cnt2Interface.setRevisions(
        ("1901-10-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cnt2Interfaces_ObjectIdentity = ObjectIdentity
cnt2Interfaces = _Cnt2Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2)
)
_Cnt2IfNumTable_Object = MibTable
cnt2IfNumTable = _Cnt2IfNumTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cnt2IfNumTable.setStatus("current")
_Cnt2IfNumEntry_Object = MibTableRow
cnt2IfNumEntry = _Cnt2IfNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 1, 1)
)
cnt2IfNumEntry.setIndexNames(
    (0, "CNT21-MIB", "cnt2IfNumIndex"),
)
if mibBuilder.loadTexts:
    cnt2IfNumEntry.setStatus("current")
_Cnt2IfNumIndex_Type = Integer32
_Cnt2IfNumIndex_Object = MibTableColumn
cnt2IfNumIndex = _Cnt2IfNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 1, 1, 1),
    _Cnt2IfNumIndex_Type()
)
cnt2IfNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfNumIndex.setStatus("current")
_Cnt2IfNum_Type = Integer32
_Cnt2IfNum_Object = MibTableColumn
cnt2IfNum = _Cnt2IfNum_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 1, 1, 2),
    _Cnt2IfNum_Type()
)
cnt2IfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfNum.setStatus("current")
_Cnt2IfTable_Object = MibTable
cnt2IfTable = _Cnt2IfTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cnt2IfTable.setStatus("deprecated")
_Cnt2IfEntry_Object = MibTableRow
cnt2IfEntry = _Cnt2IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1)
)
cnt2IfEntry.setIndexNames(
    (0, "CNT21-MIB", "cnt2IfSlotIndex"),
    (0, "CNT21-MIB", "cnt2IfIndex"),
)
if mibBuilder.loadTexts:
    cnt2IfEntry.setStatus("deprecated")
_Cnt2IfSlotIndex_Type = Integer32
_Cnt2IfSlotIndex_Object = MibTableColumn
cnt2IfSlotIndex = _Cnt2IfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 1),
    _Cnt2IfSlotIndex_Type()
)
cnt2IfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfSlotIndex.setStatus("deprecated")
_Cnt2IfIndex_Type = Integer32
_Cnt2IfIndex_Object = MibTableColumn
cnt2IfIndex = _Cnt2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 2),
    _Cnt2IfIndex_Type()
)
cnt2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfIndex.setStatus("deprecated")


class _Cnt2IfDescr_Type(DisplayString):
    """Custom type cnt2IfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cnt2IfDescr_Type.__name__ = "DisplayString"
_Cnt2IfDescr_Object = MibTableColumn
cnt2IfDescr = _Cnt2IfDescr_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 3),
    _Cnt2IfDescr_Type()
)
cnt2IfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfDescr.setStatus("deprecated")


class _Cnt2IfType_Type(Integer32):
    """Custom type cnt2IfType based on Integer32"""
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
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263)
        )
    )
    namedValues = NamedValues(
        *(("adsl", 94),
          ("aflane8023", 59),
          ("aflane8025", 60),
          ("arap", 88),
          ("arcnet", 35),
          ("arcnet-plus", 36),
          ("async", 84),
          ("atm", 37),
          ("atm-all5", 49),
          ("atmDxi", 105),
          ("atmFuni", 106),
          ("atmIma", 107),
          ("atmLogical", 80),
          ("basicISDN", 20),
          ("bsc", 83),
          ("cctEmul", 61),
          ("channel", 70),
          ("cnr", 85),
          ("ddn-x25", 4),
          ("dlsw", 74),
          ("ds0", 81),
          ("ds0Bundle", 82),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("eplrs", 87),
          ("escon", 73),
          ("escon-local", 256),
          ("escon-remote", 257),
          ("escon-srdf", 261),
          ("ethernet-3Mbit", 26),
          ("ethernet-csmacd", 6),
          ("fastEther", 62),
          ("fastEtherFX", 69),
          ("fddi", 15),
          ("fibreChannel", 56),
          ("frame-relay", 32),
          ("frame-relay-dce", 44),
          ("frameRealyMPI", 92),
          ("frameRelayInterconnect", 58),
          ("g703at2mb", 67),
          ("g703at64k", 66),
          ("gigabitEthernet", 117),
          ("hdh1822", 3),
          ("hippi", 47),
          ("hippiInterface", 57),
          ("hostPad", 90),
          ("hssi", 46),
          ("hyperchannel", 14),
          ("ibm370parChan", 72),
          ("ieee80211", 71),
          ("ieee80212", 55),
          ("ipOverAtm", 114),
          ("ipOverCdlc", 109),
          ("ipOverClaw", 110),
          ("ipSwitch", 78),
          ("isdn", 63),
          ("isdns", 75),
          ("isdnu", 76),
          ("iso8802-llc", 41),
          ("iso88023-csmacd", 7),
          ("iso88024-tokenBus", 8),
          ("iso88025-tokenRing", 9),
          ("iso88025CRFPInt", 98),
          ("iso88025Dtr", 86),
          ("iso88025Fiber", 115),
          ("iso88026-man", 10),
          ("lapb", 16),
          ("lapd", 77),
          ("localtalk", 42),
          ("miox25", 38),
          ("modem", 48),
          ("mpc", 113),
          ("myrinet", 99),
          ("nsip", 27),
          ("other", 1),
          ("parallel-port", 34),
          ("ppp", 23),
          ("pppMultilinkBundle", 108),
          ("primaryISDN", 21),
          ("prop-multiplexing", 54),
          ("prop-virtual-term", 53),
          ("propCnls", 89),
          ("propPointToPointSerial", 22),
          ("proteon-10Mbit", 12),
          ("proteon-80Mbit", 13),
          ("qllc", 68),
          ("radsl", 95),
          ("regular1822", 2),
          ("rfc877-x25", 5),
          ("rs232", 33),
          ("rsrb", 79),
          ("scsi-2", 262),
          ("scsi-3", 263),
          ("sdlc", 17),
          ("sdsl", 96),
          ("sip", 31),
          ("slip", 28),
          ("smds-dxi", 43),
          ("smds-intercarrier", 52),
          ("softwareLoopback", 24),
          ("sonet", 39),
          ("sonet-path", 50),
          ("sonet-vt", 51),
          ("stackToStack", 111),
          ("starLan", 11),
          ("switch-broadcast", 260),
          ("switch-multicast", 259),
          ("switch-unicast", 258),
          ("tdlc", 116),
          ("termPad", 91),
          ("ultra", 29),
          ("v11", 64),
          ("v35", 45),
          ("v36", 65),
          ("vdsl", 97),
          ("virtualIpAddress", 112),
          ("voiceEM", 100),
          ("voiceEncap", 103),
          ("voiceFXO", 101),
          ("voiceFXS", 102),
          ("voiceOverIp", 104),
          ("x213", 93),
          ("x25ple", 40))
    )


_Cnt2IfType_Type.__name__ = "Integer32"
_Cnt2IfType_Object = MibTableColumn
cnt2IfType = _Cnt2IfType_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 4),
    _Cnt2IfType_Type()
)
cnt2IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfType.setStatus("deprecated")
_Cnt2IfMtu_Type = Integer32
_Cnt2IfMtu_Object = MibTableColumn
cnt2IfMtu = _Cnt2IfMtu_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 5),
    _Cnt2IfMtu_Type()
)
cnt2IfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfMtu.setStatus("deprecated")
_Cnt2IfSpeed_Type = Unsigned32
_Cnt2IfSpeed_Object = MibTableColumn
cnt2IfSpeed = _Cnt2IfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 6),
    _Cnt2IfSpeed_Type()
)
cnt2IfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfSpeed.setStatus("deprecated")


class _Cnt2IfPhysAddress_Type(OctetString):
    """Custom type cnt2IfPhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Cnt2IfPhysAddress_Type.__name__ = "OctetString"
_Cnt2IfPhysAddress_Object = MibTableColumn
cnt2IfPhysAddress = _Cnt2IfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 7),
    _Cnt2IfPhysAddress_Type()
)
cnt2IfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfPhysAddress.setStatus("deprecated")


class _Cnt2IfAdminStatus_Type(Integer32):
    """Custom type cnt2IfAdminStatus based on Integer32"""
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


_Cnt2IfAdminStatus_Type.__name__ = "Integer32"
_Cnt2IfAdminStatus_Object = MibTableColumn
cnt2IfAdminStatus = _Cnt2IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 8),
    _Cnt2IfAdminStatus_Type()
)
cnt2IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2IfAdminStatus.setStatus("deprecated")


class _Cnt2IfOperStatus_Type(Integer32):
    """Custom type cnt2IfOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_Cnt2IfOperStatus_Type.__name__ = "Integer32"
_Cnt2IfOperStatus_Object = MibTableColumn
cnt2IfOperStatus = _Cnt2IfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 9),
    _Cnt2IfOperStatus_Type()
)
cnt2IfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfOperStatus.setStatus("deprecated")
_Cnt2IfLastChange_Type = TimeTicks
_Cnt2IfLastChange_Object = MibTableColumn
cnt2IfLastChange = _Cnt2IfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 10),
    _Cnt2IfLastChange_Type()
)
cnt2IfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfLastChange.setStatus("deprecated")
_Cnt2IfInOctets_Type = Counter32
_Cnt2IfInOctets_Object = MibTableColumn
cnt2IfInOctets = _Cnt2IfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 11),
    _Cnt2IfInOctets_Type()
)
cnt2IfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfInOctets.setStatus("deprecated")
_Cnt2IfInUcastPkts_Type = Counter32
_Cnt2IfInUcastPkts_Object = MibTableColumn
cnt2IfInUcastPkts = _Cnt2IfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 12),
    _Cnt2IfInUcastPkts_Type()
)
cnt2IfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfInUcastPkts.setStatus("deprecated")
_Cnt2IfInNUcastPkts_Type = Counter32
_Cnt2IfInNUcastPkts_Object = MibTableColumn
cnt2IfInNUcastPkts = _Cnt2IfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 13),
    _Cnt2IfInNUcastPkts_Type()
)
cnt2IfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfInNUcastPkts.setStatus("deprecated")
_Cnt2IfInDiscards_Type = Counter32
_Cnt2IfInDiscards_Object = MibTableColumn
cnt2IfInDiscards = _Cnt2IfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 14),
    _Cnt2IfInDiscards_Type()
)
cnt2IfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfInDiscards.setStatus("deprecated")
_Cnt2IfInErrors_Type = Counter32
_Cnt2IfInErrors_Object = MibTableColumn
cnt2IfInErrors = _Cnt2IfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 15),
    _Cnt2IfInErrors_Type()
)
cnt2IfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfInErrors.setStatus("deprecated")
_Cnt2IfInUnknownProtos_Type = Counter32
_Cnt2IfInUnknownProtos_Object = MibTableColumn
cnt2IfInUnknownProtos = _Cnt2IfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 16),
    _Cnt2IfInUnknownProtos_Type()
)
cnt2IfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfInUnknownProtos.setStatus("deprecated")
_Cnt2IfOutOctets_Type = Counter32
_Cnt2IfOutOctets_Object = MibTableColumn
cnt2IfOutOctets = _Cnt2IfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 17),
    _Cnt2IfOutOctets_Type()
)
cnt2IfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfOutOctets.setStatus("deprecated")
_Cnt2IfOutUcastPkts_Type = Counter32
_Cnt2IfOutUcastPkts_Object = MibTableColumn
cnt2IfOutUcastPkts = _Cnt2IfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 18),
    _Cnt2IfOutUcastPkts_Type()
)
cnt2IfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfOutUcastPkts.setStatus("deprecated")
_Cnt2IfOutNUcastPkts_Type = Counter32
_Cnt2IfOutNUcastPkts_Object = MibTableColumn
cnt2IfOutNUcastPkts = _Cnt2IfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 19),
    _Cnt2IfOutNUcastPkts_Type()
)
cnt2IfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfOutNUcastPkts.setStatus("deprecated")
_Cnt2IfOutDiscards_Type = Counter32
_Cnt2IfOutDiscards_Object = MibTableColumn
cnt2IfOutDiscards = _Cnt2IfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 20),
    _Cnt2IfOutDiscards_Type()
)
cnt2IfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfOutDiscards.setStatus("deprecated")
_Cnt2IfOutErrors_Type = Counter32
_Cnt2IfOutErrors_Object = MibTableColumn
cnt2IfOutErrors = _Cnt2IfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 21),
    _Cnt2IfOutErrors_Type()
)
cnt2IfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfOutErrors.setStatus("deprecated")
_Cnt2IfOutQLen_Type = Unsigned32
_Cnt2IfOutQLen_Object = MibTableColumn
cnt2IfOutQLen = _Cnt2IfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 22),
    _Cnt2IfOutQLen_Type()
)
cnt2IfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfOutQLen.setStatus("deprecated")
_Cnt2IfSpecific_Type = ObjectIdentifier
_Cnt2IfSpecific_Object = MibTableColumn
cnt2IfSpecific = _Cnt2IfSpecific_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 2, 1, 23),
    _Cnt2IfSpecific_Type()
)
cnt2IfSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2IfSpecific.setStatus("deprecated")
_Cnt2XIfTable_Object = MibTable
cnt2XIfTable = _Cnt2XIfTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cnt2XIfTable.setStatus("current")
_Cnt2XIfEntry_Object = MibTableRow
cnt2XIfEntry = _Cnt2XIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1)
)
cnt2XIfEntry.setIndexNames(
    (0, "CNT21-MIB", "cnt2XIfSlotIndex"),
    (0, "CNT21-MIB", "cnt2XIfIndex"),
)
if mibBuilder.loadTexts:
    cnt2XIfEntry.setStatus("current")
_Cnt2XIfSlotIndex_Type = Integer32
_Cnt2XIfSlotIndex_Object = MibTableColumn
cnt2XIfSlotIndex = _Cnt2XIfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 1),
    _Cnt2XIfSlotIndex_Type()
)
cnt2XIfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfSlotIndex.setStatus("current")
_Cnt2XIfIndex_Type = Integer32
_Cnt2XIfIndex_Object = MibTableColumn
cnt2XIfIndex = _Cnt2XIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 2),
    _Cnt2XIfIndex_Type()
)
cnt2XIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfIndex.setStatus("current")


class _Cnt2XIfDescr_Type(DisplayString):
    """Custom type cnt2XIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cnt2XIfDescr_Type.__name__ = "DisplayString"
_Cnt2XIfDescr_Object = MibTableColumn
cnt2XIfDescr = _Cnt2XIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 3),
    _Cnt2XIfDescr_Type()
)
cnt2XIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfDescr.setStatus("current")


class _Cnt2XIfName_Type(DisplayString):
    """Custom type cnt2XIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cnt2XIfName_Type.__name__ = "DisplayString"
_Cnt2XIfName_Object = MibTableColumn
cnt2XIfName = _Cnt2XIfName_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 4),
    _Cnt2XIfName_Type()
)
cnt2XIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfName.setStatus("current")
_Cnt2XIfIANAType_Type = IANAifType
_Cnt2XIfIANAType_Object = MibTableColumn
cnt2XIfIANAType = _Cnt2XIfIANAType_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 5),
    _Cnt2XIfIANAType_Type()
)
cnt2XIfIANAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfIANAType.setStatus("current")


class _Cnt2XIfCntType_Type(Integer32):
    """Custom type cnt2XIfCntType based on Integer32"""
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
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263)
        )
    )
    namedValues = NamedValues(
        *(("adsl", 94),
          ("aflane8023", 59),
          ("aflane8025", 60),
          ("arap", 88),
          ("arcnet", 35),
          ("arcnet-plus", 36),
          ("async", 84),
          ("atm", 37),
          ("atm-all5", 49),
          ("atmDxi", 105),
          ("atmFuni", 106),
          ("atmIma", 107),
          ("atmLogical", 80),
          ("basicISDN", 20),
          ("bsc", 83),
          ("cctEmul", 61),
          ("channel", 70),
          ("cnr", 85),
          ("ddn-x25", 4),
          ("dlsw", 74),
          ("ds0", 81),
          ("ds0Bundle", 82),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("eplrs", 87),
          ("escon", 73),
          ("escon-local", 256),
          ("escon-remote", 257),
          ("escon-srdf", 261),
          ("ethernet-3Mbit", 26),
          ("ethernet-csmacd", 6),
          ("fastEther", 62),
          ("fastEtherFX", 69),
          ("fddi", 15),
          ("fibreChannel", 56),
          ("frame-relay", 32),
          ("frame-relay-dce", 44),
          ("frameRealyMPI", 92),
          ("frameRelayInterconnect", 58),
          ("g703at2mb", 67),
          ("g703at64k", 66),
          ("gigabitEthernet", 117),
          ("hdh1822", 3),
          ("hippi", 47),
          ("hippiInterface", 57),
          ("hostPad", 90),
          ("hssi", 46),
          ("hyperchannel", 14),
          ("ibm370parChan", 72),
          ("ieee80211", 71),
          ("ieee80212", 55),
          ("ipOverAtm", 114),
          ("ipOverCdlc", 109),
          ("ipOverClaw", 110),
          ("ipSwitch", 78),
          ("isdn", 63),
          ("isdns", 75),
          ("isdnu", 76),
          ("iso8802-llc", 41),
          ("iso88023-csmacd", 7),
          ("iso88024-tokenBus", 8),
          ("iso88025-tokenRing", 9),
          ("iso88025CRFPInt", 98),
          ("iso88025Dtr", 86),
          ("iso88025Fiber", 115),
          ("iso88026-man", 10),
          ("lapb", 16),
          ("lapd", 77),
          ("localtalk", 42),
          ("miox25", 38),
          ("modem", 48),
          ("mpc", 113),
          ("myrinet", 99),
          ("nsip", 27),
          ("other", 1),
          ("parallel-port", 34),
          ("ppp", 23),
          ("pppMultilinkBundle", 108),
          ("primaryISDN", 21),
          ("prop-multiplexing", 54),
          ("prop-virtual-term", 53),
          ("propCnls", 89),
          ("propPointToPointSerial", 22),
          ("proteon-10Mbit", 12),
          ("proteon-80Mbit", 13),
          ("qllc", 68),
          ("radsl", 95),
          ("regular1822", 2),
          ("rfc877-x25", 5),
          ("rs232", 33),
          ("rsrb", 79),
          ("scsi-2", 262),
          ("scsi-3", 263),
          ("sdlc", 17),
          ("sdsl", 96),
          ("sip", 31),
          ("slip", 28),
          ("smds-dxi", 43),
          ("smds-intercarrier", 52),
          ("softwareLoopback", 24),
          ("sonet", 39),
          ("sonet-path", 50),
          ("sonet-vt", 51),
          ("stackToStack", 111),
          ("starLan", 11),
          ("switch-broadcast", 260),
          ("switch-multicast", 259),
          ("switch-unicast", 258),
          ("tdlc", 116),
          ("termPad", 91),
          ("ultra", 29),
          ("v11", 64),
          ("v35", 45),
          ("v36", 65),
          ("vdsl", 97),
          ("virtualIpAddress", 112),
          ("voiceEM", 100),
          ("voiceEncap", 103),
          ("voiceFXO", 101),
          ("voiceFXS", 102),
          ("voiceOverIp", 104),
          ("x213", 93),
          ("x25ple", 40))
    )


_Cnt2XIfCntType_Type.__name__ = "Integer32"
_Cnt2XIfCntType_Object = MibTableColumn
cnt2XIfCntType = _Cnt2XIfCntType_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 6),
    _Cnt2XIfCntType_Type()
)
cnt2XIfCntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfCntType.setStatus("current")
_Cnt2XIfMtu_Type = Integer32
_Cnt2XIfMtu_Object = MibTableColumn
cnt2XIfMtu = _Cnt2XIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 7),
    _Cnt2XIfMtu_Type()
)
cnt2XIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfMtu.setStatus("current")
_Cnt2XIfSpeed_Type = Unsigned32
_Cnt2XIfSpeed_Object = MibTableColumn
cnt2XIfSpeed = _Cnt2XIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 8),
    _Cnt2XIfSpeed_Type()
)
cnt2XIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfSpeed.setStatus("current")


class _Cnt2XIfPhysAddress_Type(OctetString):
    """Custom type cnt2XIfPhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_Cnt2XIfPhysAddress_Type.__name__ = "OctetString"
_Cnt2XIfPhysAddress_Object = MibTableColumn
cnt2XIfPhysAddress = _Cnt2XIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 9),
    _Cnt2XIfPhysAddress_Type()
)
cnt2XIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfPhysAddress.setStatus("current")


class _Cnt2XIfAdminStatus_Type(Integer32):
    """Custom type cnt2XIfAdminStatus based on Integer32"""
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


_Cnt2XIfAdminStatus_Type.__name__ = "Integer32"
_Cnt2XIfAdminStatus_Object = MibTableColumn
cnt2XIfAdminStatus = _Cnt2XIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 10),
    _Cnt2XIfAdminStatus_Type()
)
cnt2XIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2XIfAdminStatus.setStatus("current")


class _Cnt2XIfOperStatus_Type(Integer32):
    """Custom type cnt2XIfOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_Cnt2XIfOperStatus_Type.__name__ = "Integer32"
_Cnt2XIfOperStatus_Object = MibTableColumn
cnt2XIfOperStatus = _Cnt2XIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 11),
    _Cnt2XIfOperStatus_Type()
)
cnt2XIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfOperStatus.setStatus("current")
_Cnt2XIfLastChange_Type = TimeTicks
_Cnt2XIfLastChange_Object = MibTableColumn
cnt2XIfLastChange = _Cnt2XIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 12),
    _Cnt2XIfLastChange_Type()
)
cnt2XIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfLastChange.setStatus("current")


class _Cnt2XIfLinkUpDownTrapEnable_Type(Integer32):
    """Custom type cnt2XIfLinkUpDownTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Cnt2XIfLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_Cnt2XIfLinkUpDownTrapEnable_Object = MibTableColumn
cnt2XIfLinkUpDownTrapEnable = _Cnt2XIfLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 13),
    _Cnt2XIfLinkUpDownTrapEnable_Type()
)
cnt2XIfLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2XIfLinkUpDownTrapEnable.setStatus("current")
_Cnt2XIfPromiscuousMode_Type = TruthValue
_Cnt2XIfPromiscuousMode_Object = MibTableColumn
cnt2XIfPromiscuousMode = _Cnt2XIfPromiscuousMode_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 14),
    _Cnt2XIfPromiscuousMode_Type()
)
cnt2XIfPromiscuousMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2XIfPromiscuousMode.setStatus("current")
_Cnt2XIfConnectorType_Type = TruthValue
_Cnt2XIfConnectorType_Object = MibTableColumn
cnt2XIfConnectorType = _Cnt2XIfConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 15),
    _Cnt2XIfConnectorType_Type()
)
cnt2XIfConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfConnectorType.setStatus("current")


class _Cnt2XIfAlias_Type(DisplayString):
    """Custom type cnt2XIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cnt2XIfAlias_Type.__name__ = "DisplayString"
_Cnt2XIfAlias_Object = MibTableColumn
cnt2XIfAlias = _Cnt2XIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 16),
    _Cnt2XIfAlias_Type()
)
cnt2XIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2XIfAlias.setStatus("current")
_Cnt2XIfInOctets_Type = Counter64
_Cnt2XIfInOctets_Object = MibTableColumn
cnt2XIfInOctets = _Cnt2XIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 17),
    _Cnt2XIfInOctets_Type()
)
cnt2XIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfInOctets.setStatus("current")
_Cnt2XIfInUcastPkts_Type = Counter32
_Cnt2XIfInUcastPkts_Object = MibTableColumn
cnt2XIfInUcastPkts = _Cnt2XIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 18),
    _Cnt2XIfInUcastPkts_Type()
)
cnt2XIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfInUcastPkts.setStatus("current")
_Cnt2XIfInMulticastPkts_Type = Counter32
_Cnt2XIfInMulticastPkts_Object = MibTableColumn
cnt2XIfInMulticastPkts = _Cnt2XIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 19),
    _Cnt2XIfInMulticastPkts_Type()
)
cnt2XIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfInMulticastPkts.setStatus("current")
_Cnt2XIfInBroadcastPkts_Type = Counter32
_Cnt2XIfInBroadcastPkts_Object = MibTableColumn
cnt2XIfInBroadcastPkts = _Cnt2XIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 20),
    _Cnt2XIfInBroadcastPkts_Type()
)
cnt2XIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfInBroadcastPkts.setStatus("current")
_Cnt2XIfInDiscards_Type = Counter32
_Cnt2XIfInDiscards_Object = MibTableColumn
cnt2XIfInDiscards = _Cnt2XIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 21),
    _Cnt2XIfInDiscards_Type()
)
cnt2XIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfInDiscards.setStatus("current")
_Cnt2XIfInErrors_Type = Counter32
_Cnt2XIfInErrors_Object = MibTableColumn
cnt2XIfInErrors = _Cnt2XIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 22),
    _Cnt2XIfInErrors_Type()
)
cnt2XIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfInErrors.setStatus("current")
_Cnt2XIfInUnknownProtos_Type = Counter32
_Cnt2XIfInUnknownProtos_Object = MibTableColumn
cnt2XIfInUnknownProtos = _Cnt2XIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 23),
    _Cnt2XIfInUnknownProtos_Type()
)
cnt2XIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfInUnknownProtos.setStatus("current")
_Cnt2XIfOutOctets_Type = Counter64
_Cnt2XIfOutOctets_Object = MibTableColumn
cnt2XIfOutOctets = _Cnt2XIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 24),
    _Cnt2XIfOutOctets_Type()
)
cnt2XIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfOutOctets.setStatus("current")
_Cnt2XIfOutUcastPkts_Type = Counter32
_Cnt2XIfOutUcastPkts_Object = MibTableColumn
cnt2XIfOutUcastPkts = _Cnt2XIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 25),
    _Cnt2XIfOutUcastPkts_Type()
)
cnt2XIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfOutUcastPkts.setStatus("current")
_Cnt2XIfOutMulticastPkts_Type = Counter32
_Cnt2XIfOutMulticastPkts_Object = MibTableColumn
cnt2XIfOutMulticastPkts = _Cnt2XIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 26),
    _Cnt2XIfOutMulticastPkts_Type()
)
cnt2XIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfOutMulticastPkts.setStatus("current")
_Cnt2XIfOutBroadcastPkts_Type = Counter32
_Cnt2XIfOutBroadcastPkts_Object = MibTableColumn
cnt2XIfOutBroadcastPkts = _Cnt2XIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 27),
    _Cnt2XIfOutBroadcastPkts_Type()
)
cnt2XIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfOutBroadcastPkts.setStatus("current")
_Cnt2XIfOutDiscards_Type = Counter32
_Cnt2XIfOutDiscards_Object = MibTableColumn
cnt2XIfOutDiscards = _Cnt2XIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 28),
    _Cnt2XIfOutDiscards_Type()
)
cnt2XIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfOutDiscards.setStatus("current")
_Cnt2XIfOutErrors_Type = Counter32
_Cnt2XIfOutErrors_Object = MibTableColumn
cnt2XIfOutErrors = _Cnt2XIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 29),
    _Cnt2XIfOutErrors_Type()
)
cnt2XIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfOutErrors.setStatus("current")
_Cnt2XIfCounterDiscontinuityTime_Type = TimeStamp
_Cnt2XIfCounterDiscontinuityTime_Object = MibTableColumn
cnt2XIfCounterDiscontinuityTime = _Cnt2XIfCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 1, 2, 3, 1, 30),
    _Cnt2XIfCounterDiscontinuityTime_Type()
)
cnt2XIfCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2XIfCounterDiscontinuityTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNT21-MIB",
    **{"cnt2Interface": cnt2Interface,
       "cnt2Interfaces": cnt2Interfaces,
       "cnt2IfNumTable": cnt2IfNumTable,
       "cnt2IfNumEntry": cnt2IfNumEntry,
       "cnt2IfNumIndex": cnt2IfNumIndex,
       "cnt2IfNum": cnt2IfNum,
       "cnt2IfTable": cnt2IfTable,
       "cnt2IfEntry": cnt2IfEntry,
       "cnt2IfSlotIndex": cnt2IfSlotIndex,
       "cnt2IfIndex": cnt2IfIndex,
       "cnt2IfDescr": cnt2IfDescr,
       "cnt2IfType": cnt2IfType,
       "cnt2IfMtu": cnt2IfMtu,
       "cnt2IfSpeed": cnt2IfSpeed,
       "cnt2IfPhysAddress": cnt2IfPhysAddress,
       "cnt2IfAdminStatus": cnt2IfAdminStatus,
       "cnt2IfOperStatus": cnt2IfOperStatus,
       "cnt2IfLastChange": cnt2IfLastChange,
       "cnt2IfInOctets": cnt2IfInOctets,
       "cnt2IfInUcastPkts": cnt2IfInUcastPkts,
       "cnt2IfInNUcastPkts": cnt2IfInNUcastPkts,
       "cnt2IfInDiscards": cnt2IfInDiscards,
       "cnt2IfInErrors": cnt2IfInErrors,
       "cnt2IfInUnknownProtos": cnt2IfInUnknownProtos,
       "cnt2IfOutOctets": cnt2IfOutOctets,
       "cnt2IfOutUcastPkts": cnt2IfOutUcastPkts,
       "cnt2IfOutNUcastPkts": cnt2IfOutNUcastPkts,
       "cnt2IfOutDiscards": cnt2IfOutDiscards,
       "cnt2IfOutErrors": cnt2IfOutErrors,
       "cnt2IfOutQLen": cnt2IfOutQLen,
       "cnt2IfSpecific": cnt2IfSpecific,
       "cnt2XIfTable": cnt2XIfTable,
       "cnt2XIfEntry": cnt2XIfEntry,
       "cnt2XIfSlotIndex": cnt2XIfSlotIndex,
       "cnt2XIfIndex": cnt2XIfIndex,
       "cnt2XIfDescr": cnt2XIfDescr,
       "cnt2XIfName": cnt2XIfName,
       "cnt2XIfIANAType": cnt2XIfIANAType,
       "cnt2XIfCntType": cnt2XIfCntType,
       "cnt2XIfMtu": cnt2XIfMtu,
       "cnt2XIfSpeed": cnt2XIfSpeed,
       "cnt2XIfPhysAddress": cnt2XIfPhysAddress,
       "cnt2XIfAdminStatus": cnt2XIfAdminStatus,
       "cnt2XIfOperStatus": cnt2XIfOperStatus,
       "cnt2XIfLastChange": cnt2XIfLastChange,
       "cnt2XIfLinkUpDownTrapEnable": cnt2XIfLinkUpDownTrapEnable,
       "cnt2XIfPromiscuousMode": cnt2XIfPromiscuousMode,
       "cnt2XIfConnectorType": cnt2XIfConnectorType,
       "cnt2XIfAlias": cnt2XIfAlias,
       "cnt2XIfInOctets": cnt2XIfInOctets,
       "cnt2XIfInUcastPkts": cnt2XIfInUcastPkts,
       "cnt2XIfInMulticastPkts": cnt2XIfInMulticastPkts,
       "cnt2XIfInBroadcastPkts": cnt2XIfInBroadcastPkts,
       "cnt2XIfInDiscards": cnt2XIfInDiscards,
       "cnt2XIfInErrors": cnt2XIfInErrors,
       "cnt2XIfInUnknownProtos": cnt2XIfInUnknownProtos,
       "cnt2XIfOutOctets": cnt2XIfOutOctets,
       "cnt2XIfOutUcastPkts": cnt2XIfOutUcastPkts,
       "cnt2XIfOutMulticastPkts": cnt2XIfOutMulticastPkts,
       "cnt2XIfOutBroadcastPkts": cnt2XIfOutBroadcastPkts,
       "cnt2XIfOutDiscards": cnt2XIfOutDiscards,
       "cnt2XIfOutErrors": cnt2XIfOutErrors,
       "cnt2XIfCounterDiscontinuityTime": cnt2XIfCounterDiscontinuityTime}
)
