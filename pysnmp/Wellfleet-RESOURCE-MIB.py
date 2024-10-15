# SNMP MIB module (Wellfleet-RESOURCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-RESOURCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:58 2024
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

(wfGameGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfGameGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfResourceUseTable_Object = MibTable
wfResourceUseTable = _WfResourceUseTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 6)
)
if mibBuilder.loadTexts:
    wfResourceUseTable.setStatus("mandatory")
_WfResourceUseEntry_Object = MibTableRow
wfResourceUseEntry = _WfResourceUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 6, 1)
)
wfResourceUseEntry.setIndexNames(
    (0, "Wellfleet-RESOURCE-MIB", "wfResourceUseEntity"),
    (0, "Wellfleet-RESOURCE-MIB", "wfResourceUseSlot"),
)
if mibBuilder.loadTexts:
    wfResourceUseEntry.setStatus("mandatory")


class _WfResourceUseEntity_Type(Integer32):
    """Custom type wfResourceUseEntity based on Integer32"""
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
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163)
        )
    )
    namedValues = NamedValues(
        *(("acct", 144),
          ("ahb", 125),
          ("amd100m", 149),
          ("aot", 116),
          ("appncp", 71),
          ("appnls", 70),
          ("arp", 33),
          ("asnmod", 50),
          ("asr", 123),
          ("at", 24),
          ("atm", 60),
          ("atmalc", 61),
          ("atmasm", 101),
          ("atmc5000", 95),
          ("atmcmod", 79),
          ("atmdxi", 31),
          ("atmle", 94),
          ("atmmcs", 100),
          ("atmsig", 93),
          ("atmtp", 147),
          ("atmzdrv", 89),
          ("bacdmux", 146),
          ("baysig", 103),
          ("bcc", 158),
          ("bgp", 38),
          ("bgprs", 80),
          ("bot", 97),
          ("bpkg", 145),
          ("capi", 136),
          ("chipcom", 74),
          ("copsc", 156),
          ("cpm", 102),
          ("crm", 81),
          ("dcmmw", 83),
          ("de100", 85),
          ("debug", 54),
          ("dhcp", 135),
          ("diffserv", 155),
          ("dls", 32),
          ("dns", 110),
          ("drs", 22),
          ("ds2180", 17),
          ("ds2181", 18),
          ("dsde2", 5),
          ("dsqms", 162),
          ("dst", 8),
          ("dtok", 7),
          ("dvmrp", 65),
          ("dvs", 133),
          ("e1", 10),
          ("efddi", 52),
          ("egp", 39),
          ("enet2", 2),
          ("fddi", 4),
          ("fnts", 111),
          ("fntsatm", 112),
          ("fr", 29),
          ("frpt", 120),
          ("frsvc", 115),
          ("frswcngc", 55),
          ("frswmap", 59),
          ("fsi", 14),
          ("ftp", 75),
          ("gigenet", 153),
          ("gns", 143),
          ("hdlc", 16),
          ("hdwancop", 108),
          ("hdwanlm", 77),
          ("hfsi", 20),
          ("hid", 140),
          ("hilance", 49),
          ("hlsin", 53),
          ("hssi", 11),
          ("http", 121),
          ("hwcomp", 87),
          ("hwf", 19),
          ("ifpdrv", 148),
          ("iftab", 142),
          ("igmp", 66),
          ("iisis", 150),
          ("ike", 157),
          ("ilacc", 13),
          ("ip", 21),
          ("ip6", 96),
          ("ipex", 90),
          ("ipsec", 137),
          ("ipx", 26),
          ("isac", 73),
          ("isdb", 127),
          ("isdn", 67),
          ("kernel", 1),
          ("l2tp", 126),
          ("lance", 12),
          ("lapb", 51),
          ("lbc", 99),
          ("llc", 42),
          ("lm", 68),
          ("lnm", 43),
          ("mct1", 57),
          ("mct1e1", 46),
          ("mospf", 117),
          ("mpc", 132),
          ("mplsLdp", 138),
          ("mplsMlm", 139),
          ("mps", 131),
          ("munich", 47),
          ("municht1", 58),
          ("nat", 119),
          ("nbase", 62),
          ("nbip", 64),
          ("nhrp", 124),
          ("nlsp", 86),
          ("npt", 91),
          ("nsc100m", 84),
          ("ntp", 105),
          ("osi", 27),
          ("ospf", 40),
          ("pcap", 45),
          ("pim", 98),
          ("ping", 69),
          ("ppp", 44),
          ("pq2dsync", 160),
          ("qenet", 3),
          ("qscop", 163),
          ("qsync", 6),
          ("quicsync", 48),
          ("radius", 107),
          ("raesa", 106),
          ("rarp", 30),
          ("rcmds", 109),
          ("rip6", 114),
          ("rmonstat", 129),
          ("rredund", 92),
          ("rsvp", 118),
          ("scd", 141),
          ("scmipc", 104),
          ("sdlc", 63),
          ("seeq100m", 152),
          ("sgig", 154),
          ("smdssw", 76),
          ("snmp", 35),
          ("sqe100", 151),
          ("st2", 82),
          ("stacppp", 122),
          ("stats", 88),
          ("swmgr", 56),
          ("sysl", 78),
          ("t1", 9),
          ("tag1q", 130),
          ("tcp", 37),
          ("tdmmgr", 159),
          ("tftp", 34),
          ("tms380", 15),
          ("tn", 36),
          ("vcct", 128),
          ("vines", 23),
          ("voip", 161),
          ("vrrp", 134),
          ("wan", 41),
          ("wcp", 72),
          ("wep", 113),
          ("x25", 28),
          ("xns", 25))
    )


_WfResourceUseEntity_Type.__name__ = "Integer32"
_WfResourceUseEntity_Object = MibTableColumn
wfResourceUseEntity = _WfResourceUseEntity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 6, 1, 1),
    _WfResourceUseEntity_Type()
)
wfResourceUseEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceUseEntity.setStatus("mandatory")
_WfResourceUseSlot_Type = Integer32
_WfResourceUseSlot_Object = MibTableColumn
wfResourceUseSlot = _WfResourceUseSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 6, 1, 2),
    _WfResourceUseSlot_Type()
)
wfResourceUseSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceUseSlot.setStatus("mandatory")
_WfResourceUseEntityName_Type = DisplayString
_WfResourceUseEntityName_Object = MibTableColumn
wfResourceUseEntityName = _WfResourceUseEntityName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 6, 1, 3),
    _WfResourceUseEntityName_Type()
)
wfResourceUseEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceUseEntityName.setStatus("mandatory")
_WfResourceUseCpu_Type = Integer32
_WfResourceUseCpu_Object = MibTableColumn
wfResourceUseCpu = _WfResourceUseCpu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 6, 1, 4),
    _WfResourceUseCpu_Type()
)
wfResourceUseCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceUseCpu.setStatus("mandatory")
_WfResourceUseMemory_Type = Gauge32
_WfResourceUseMemory_Object = MibTableColumn
wfResourceUseMemory = _WfResourceUseMemory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 6, 1, 5),
    _WfResourceUseMemory_Type()
)
wfResourceUseMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceUseMemory.setStatus("mandatory")
_WfResourceUseBuffers_Type = Gauge32
_WfResourceUseBuffers_Object = MibTableColumn
wfResourceUseBuffers = _WfResourceUseBuffers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 6, 1, 6),
    _WfResourceUseBuffers_Type()
)
wfResourceUseBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceUseBuffers.setStatus("mandatory")
_WfResourceTotalTable_Object = MibTable
wfResourceTotalTable = _WfResourceTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7)
)
if mibBuilder.loadTexts:
    wfResourceTotalTable.setStatus("mandatory")
_WfResourceTotalEntry_Object = MibTableRow
wfResourceTotalEntry = _WfResourceTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7, 1)
)
wfResourceTotalEntry.setIndexNames(
    (0, "Wellfleet-RESOURCE-MIB", "wfResourceTotalSlot"),
)
if mibBuilder.loadTexts:
    wfResourceTotalEntry.setStatus("mandatory")
_WfResourceTotalSlot_Type = Integer32
_WfResourceTotalSlot_Object = MibTableColumn
wfResourceTotalSlot = _WfResourceTotalSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7, 1, 1),
    _WfResourceTotalSlot_Type()
)
wfResourceTotalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceTotalSlot.setStatus("mandatory")
_WfResourceTotalCpuUsed_Type = Counter32
_WfResourceTotalCpuUsed_Object = MibTableColumn
wfResourceTotalCpuUsed = _WfResourceTotalCpuUsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7, 1, 2),
    _WfResourceTotalCpuUsed_Type()
)
wfResourceTotalCpuUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceTotalCpuUsed.setStatus("mandatory")
_WfResourceTotalCpuIdle_Type = Counter32
_WfResourceTotalCpuIdle_Object = MibTableColumn
wfResourceTotalCpuIdle = _WfResourceTotalCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7, 1, 3),
    _WfResourceTotalCpuIdle_Type()
)
wfResourceTotalCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceTotalCpuIdle.setStatus("mandatory")
_WfResourceTotalCpuMax_Type = Counter32
_WfResourceTotalCpuMax_Object = MibTableColumn
wfResourceTotalCpuMax = _WfResourceTotalCpuMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7, 1, 4),
    _WfResourceTotalCpuMax_Type()
)
wfResourceTotalCpuMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceTotalCpuMax.setStatus("mandatory")
_WfResourceTotalMemoryUsed_Type = Gauge32
_WfResourceTotalMemoryUsed_Object = MibTableColumn
wfResourceTotalMemoryUsed = _WfResourceTotalMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7, 1, 5),
    _WfResourceTotalMemoryUsed_Type()
)
wfResourceTotalMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceTotalMemoryUsed.setStatus("mandatory")
_WfResourceTotalMemoryFree_Type = Gauge32
_WfResourceTotalMemoryFree_Object = MibTableColumn
wfResourceTotalMemoryFree = _WfResourceTotalMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7, 1, 6),
    _WfResourceTotalMemoryFree_Type()
)
wfResourceTotalMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceTotalMemoryFree.setStatus("mandatory")
_WfResourceTotalMemoryMax_Type = Gauge32
_WfResourceTotalMemoryMax_Object = MibTableColumn
wfResourceTotalMemoryMax = _WfResourceTotalMemoryMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7, 1, 7),
    _WfResourceTotalMemoryMax_Type()
)
wfResourceTotalMemoryMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceTotalMemoryMax.setStatus("mandatory")
_WfResourceTotalBuffersUsed_Type = Gauge32
_WfResourceTotalBuffersUsed_Object = MibTableColumn
wfResourceTotalBuffersUsed = _WfResourceTotalBuffersUsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7, 1, 8),
    _WfResourceTotalBuffersUsed_Type()
)
wfResourceTotalBuffersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceTotalBuffersUsed.setStatus("mandatory")
_WfResourceTotalBuffersFree_Type = Gauge32
_WfResourceTotalBuffersFree_Object = MibTableColumn
wfResourceTotalBuffersFree = _WfResourceTotalBuffersFree_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7, 1, 9),
    _WfResourceTotalBuffersFree_Type()
)
wfResourceTotalBuffersFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceTotalBuffersFree.setStatus("mandatory")
_WfResourceTotalBuffersMax_Type = Gauge32
_WfResourceTotalBuffersMax_Object = MibTableColumn
wfResourceTotalBuffersMax = _WfResourceTotalBuffersMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 7, 1, 10),
    _WfResourceTotalBuffersMax_Type()
)
wfResourceTotalBuffersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfResourceTotalBuffersMax.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-RESOURCE-MIB",
    **{"wfResourceUseTable": wfResourceUseTable,
       "wfResourceUseEntry": wfResourceUseEntry,
       "wfResourceUseEntity": wfResourceUseEntity,
       "wfResourceUseSlot": wfResourceUseSlot,
       "wfResourceUseEntityName": wfResourceUseEntityName,
       "wfResourceUseCpu": wfResourceUseCpu,
       "wfResourceUseMemory": wfResourceUseMemory,
       "wfResourceUseBuffers": wfResourceUseBuffers,
       "wfResourceTotalTable": wfResourceTotalTable,
       "wfResourceTotalEntry": wfResourceTotalEntry,
       "wfResourceTotalSlot": wfResourceTotalSlot,
       "wfResourceTotalCpuUsed": wfResourceTotalCpuUsed,
       "wfResourceTotalCpuIdle": wfResourceTotalCpuIdle,
       "wfResourceTotalCpuMax": wfResourceTotalCpuMax,
       "wfResourceTotalMemoryUsed": wfResourceTotalMemoryUsed,
       "wfResourceTotalMemoryFree": wfResourceTotalMemoryFree,
       "wfResourceTotalMemoryMax": wfResourceTotalMemoryMax,
       "wfResourceTotalBuffersUsed": wfResourceTotalBuffersUsed,
       "wfResourceTotalBuffersFree": wfResourceTotalBuffersFree,
       "wfResourceTotalBuffersMax": wfResourceTotalBuffersMax}
)
