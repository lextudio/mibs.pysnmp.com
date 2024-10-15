# SNMP MIB module (HUAWEI-MLSR-DEV-ADM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MLSR-DEV-ADM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:03 2024
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

(huawei,
 mlsr,
 products,
 router) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "huawei",
    "mlsr",
    "products",
    "router")

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



class HwFlashStatus(Integer32):
    """Custom type HwFlashStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("busy", 1))
    )





class HwFlashEreaseStatus(Integer32):
    """Custom type HwFlashEreaseStatus based on Integer32"""
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
        *(("hwBufferAllocationFailure", 6),
          ("hwFlhInOperating", 1),
          ("hwFlhOpFailure", 3),
          ("hwFlhOpSuccess", 2),
          ("hwFlhOpenFailure", 5),
          ("hwFlhReadOnly", 4),
          ("hwNoOpAfterLastPowered", 7))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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

_RouterGeneral_ObjectIdentity = ObjectIdentity
routerGeneral = _RouterGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1)
)
_Attr_ObjectIdentity = ObjectIdentity
attr = _Attr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1)
)
_Basis_ObjectIdentity = ObjectIdentity
basis = _Basis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 1)
)
_Version_Type = OctetString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 1, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("mandatory")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 2)
)
_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3)
)


class _Logcontroller_Type(Integer32):
    """Custom type logcontroller based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Logcontroller_Type.__name__ = "Integer32"
_Logcontroller_Object = MibScalar
logcontroller = _Logcontroller_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 1),
    _Logcontroller_Type()
)
logcontroller.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logcontroller.setStatus("mandatory")
_LoghostTable_Object = MibTable
loghostTable = _LoghostTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    loghostTable.setStatus("mandatory")
_LoghostEntry_Object = MibTableRow
loghostEntry = _LoghostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 2, 1)
)
loghostEntry.setIndexNames(
    (0, "HUAWEI-MLSR-DEV-ADM-MIB", "loghostaddress"),
)
if mibBuilder.loadTexts:
    loghostEntry.setStatus("mandatory")
_LoghostIndex_Type = Integer32
_LoghostIndex_Object = MibTableColumn
loghostIndex = _LoghostIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 2, 1, 1),
    _LoghostIndex_Type()
)
loghostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loghostIndex.setStatus("mandatory")
_Loghostaddress_Type = IpAddress
_Loghostaddress_Object = MibTableColumn
loghostaddress = _Loghostaddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 2, 1, 2),
    _Loghostaddress_Type()
)
loghostaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loghostaddress.setStatus("mandatory")


class _Loghostport_Type(Integer32):
    """Custom type loghostport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Loghostport_Type.__name__ = "Integer32"
_Loghostport_Object = MibTableColumn
loghostport = _Loghostport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 2, 1, 3),
    _Loghostport_Type()
)
loghostport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loghostport.setStatus("mandatory")


class _Loghostseverity_Type(Integer32):
    """Custom type loghostseverity based on Integer32"""
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
        *(("alert", 2),
          ("crit", 3),
          ("debug", 8),
          ("emerg", 1),
          ("err", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_Loghostseverity_Type.__name__ = "Integer32"
_Loghostseverity_Object = MibTableColumn
loghostseverity = _Loghostseverity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 2, 1, 4),
    _Loghostseverity_Type()
)
loghostseverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loghostseverity.setStatus("mandatory")


class _Loghostlanguage_Type(Integer32):
    """Custom type loghostlanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chinese", 1),
          ("english", 2))
    )


_Loghostlanguage_Type.__name__ = "Integer32"
_Loghostlanguage_Object = MibTableColumn
loghostlanguage = _Loghostlanguage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 2, 1, 5),
    _Loghostlanguage_Type()
)
loghostlanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loghostlanguage.setStatus("mandatory")


class _Loghostfacility_Type(Integer32):
    """Custom type loghostfacility based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("auth", 5),
          ("authpriv", 11),
          ("cron", 10),
          ("daemon", 4),
          ("ftp", 12),
          ("kern", 1),
          ("local0", 17),
          ("local1", 18),
          ("local2", 19),
          ("local3", 20),
          ("local4", 21),
          ("local5", 22),
          ("local6", 23),
          ("local7", 24),
          ("lpr", 7),
          ("mail", 3),
          ("news", 8),
          ("syslog", 6),
          ("user", 2),
          ("uucp", 9))
    )


_Loghostfacility_Type.__name__ = "Integer32"
_Loghostfacility_Object = MibTableColumn
loghostfacility = _Loghostfacility_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 2, 1, 6),
    _Loghostfacility_Type()
)
loghostfacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loghostfacility.setStatus("mandatory")


class _Loghostaccess_Type(Integer32):
    """Custom type loghostaccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_Loghostaccess_Type.__name__ = "Integer32"
_Loghostaccess_Object = MibTableColumn
loghostaccess = _Loghostaccess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 2, 1, 7),
    _Loghostaccess_Type()
)
loghostaccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loghostaccess.setStatus("mandatory")
_Loghoststatus_Type = RowStatus
_Loghoststatus_Object = MibTableColumn
loghoststatus = _Loghoststatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 2, 1, 8),
    _Loghoststatus_Type()
)
loghoststatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loghoststatus.setStatus("mandatory")
_LogfilterTable_Object = MibTable
logfilterTable = _LogfilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    logfilterTable.setStatus("mandatory")
_LogfilterEntry_Object = MibTableRow
logfilterEntry = _LogfilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 3, 1)
)
logfilterEntry.setIndexNames(
    (0, "HUAWEI-MLSR-DEV-ADM-MIB", "logfilterIndex"),
    (0, "HUAWEI-MLSR-DEV-ADM-MIB", "logdevfacility"),
)
if mibBuilder.loadTexts:
    logfilterEntry.setStatus("mandatory")
_LogfilterIndex_Type = Integer32
_LogfilterIndex_Object = MibTableColumn
logfilterIndex = _LogfilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 3, 1, 1),
    _LogfilterIndex_Type()
)
logfilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logfilterIndex.setStatus("mandatory")


class _Logdevfacility_Type(OctetString):
    """Custom type logdevfacility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Logdevfacility_Type.__name__ = "OctetString"
_Logdevfacility_Object = MibTableColumn
logdevfacility = _Logdevfacility_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 3, 1, 2),
    _Logdevfacility_Type()
)
logdevfacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logdevfacility.setStatus("mandatory")
_Logfilterstatus_Type = RowStatus
_Logfilterstatus_Object = MibTableColumn
logfilterstatus = _Logfilterstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 3, 3, 1, 3),
    _Logfilterstatus_Type()
)
logfilterstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logfilterstatus.setStatus("mandatory")
_Vrp_ObjectIdentity = ObjectIdentity
vrp = _Vrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1, 4)
)
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("mandatory")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2, 1, 1)
)
moduleEntry.setIndexNames(
    (0, "HUAWEI-MLSR-DEV-ADM-MIB", "moduleIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("mandatory")
_ModuleIndex_Type = Integer32
_ModuleIndex_Object = MibTableColumn
moduleIndex = _ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2, 1, 1, 1),
    _ModuleIndex_Type()
)
moduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIndex.setStatus("mandatory")
_ModuleSlotNum_Type = Integer32
_ModuleSlotNum_Object = MibTableColumn
moduleSlotNum = _ModuleSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2, 1, 1, 2),
    _ModuleSlotNum_Type()
)
moduleSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSlotNum.setStatus("mandatory")


class _ModuleType_Type(Integer32):
    """Custom type moduleType based on Integer32"""
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
              149,
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
              163,
              164,
              165,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              277,
              278,
              281)
        )
    )
    namedValues = NamedValues(
        *(("am12", 27),
          ("am6", 28),
          ("ame12", 61),
          ("ame6", 60),
          ("as", 2),
          ("as16", 16),
          ("ase16", 78),
          ("ase8", 77),
          ("atm155m", 76),
          ("atm155m-mm", 106),
          ("atm155m-sm", 107),
          ("atm155m-sml", 108),
          ("atm1ADSLI", 119),
          ("atm1shdsl4wire", 151),
          ("atm25m", 93),
          ("atm2ADSLI", 120),
          ("atmIma4shdsl", 152),
          ("atmadsl1", 74),
          ("atmadsl2", 75),
          ("atme3", 94),
          ("atmshdsl1", 90),
          ("atmshdsl2", 91),
          ("atmshdsl4", 92),
          ("atmt3", 95),
          ("aux", 31),
          ("bi", 4),
          ("bs4", 132),
          ("bsv2", 160),
          ("bsv2-v2", 224),
          ("bsv4", 161),
          ("cavium", 117),
          ("ce32", 159),
          ("cf-card", 223),
          ("console", 32),
          ("cpos", 103),
          ("cpos-t1", 111),
          ("dm-epri", 231),
          ("dm-tpri", 232),
          ("e1", 8),
          ("e11-f", 65),
          ("e11-f-17", 71),
          ("e12", 5),
          ("e12-f", 66),
          ("e14", 6),
          ("e14-f", 67),
          ("e18-120", 124),
          ("e18-75", 123),
          ("e1vi", 26),
          ("e1vi1-v2", 225),
          ("e1vi2", 226),
          ("em2", 21),
          ("em4", 24),
          ("erpu", 163),
          ("erpu-h", 233),
          ("fcm2", 58),
          ("fcm4", 57),
          ("fcm6", 51),
          ("fe1", 7),
          ("fe18-120", 221),
          ("fe18-75", 220),
          ("fe1op", 104),
          ("fe1op-mfx", 110),
          ("fe1op-sfx", 109),
          ("fe2", 9),
          ("fe4", 149),
          ("fix-1sae", 116),
          ("fix-1wan", 115),
          ("fix-e11", 121),
          ("fix-t11", 122),
          ("ft18", 222),
          ("ft3", 158),
          ("fxo2", 20),
          ("fxo4", 23),
          ("fxs2", 19),
          ("fxs4", 22),
          ("ge1", 101),
          ("ge1-op", 112),
          ("ge2", 114),
          ("ge2-op", 113),
          ("ima-4e1120", 136),
          ("ima-4e175", 135),
          ("ima-4t1", 138),
          ("ima-8e1120", 134),
          ("ima-8e175", 133),
          ("ima-8t1", 137),
          ("ls16", 155),
          ("ls4", 153),
          ("ls8", 154),
          ("lsa", 18),
          ("ndec", 29),
          ("new8as", 17),
          ("newsa2", 30),
          ("nsa", 165),
          ("oneatm-oc3", 281),
          ("osm", 229),
          ("pos155m", 102),
          ("rpu", 162),
          ("rtb21ce3", 59),
          ("rtb21ct3", 73),
          ("s1b", 14),
          ("sa2", 15),
          ("sa8", 52),
          ("sab", 25),
          ("sae2", 80),
          ("sae4", 79),
          ("sae8", 105),
          ("sd707", 230),
          ("sic-1Eth", 118),
          ("sic-1am", 43),
          ("sic-1bs", 41),
          ("sic-1bu", 39),
          ("sic-1e1", 37),
          ("sic-1e1-f-v2", 278),
          ("sic-1e1f", 140),
          ("sic-1em", 45),
          ("sic-1fe", 34),
          ("sic-1fxo", 49),
          ("sic-1fxs", 47),
          ("sic-1sa", 35),
          ("sic-1t1", 38),
          ("sic-1t1f", 139),
          ("sic-1vifxo", 127),
          ("sic-1vifxs", 126),
          ("sic-2am", 44),
          ("sic-2bs", 42),
          ("sic-2bu", 40),
          ("sic-2e1-f", 277),
          ("sic-2em", 46),
          ("sic-2fxo", 50),
          ("sic-2fxs", 48),
          ("sic-2vifxo", 129),
          ("sic-2vifxs", 128),
          ("sic-3as", 36),
          ("sic-adls2plus-isdn", 156),
          ("sic-adls2plus-pots", 157),
          ("sic-wan", 33),
          ("ss", 3),
          ("ssl", 164),
          ("t11", 53),
          ("t11-f", 68),
          ("t11-f-17", 72),
          ("t12", 54),
          ("t12-f", 69),
          ("t14", 55),
          ("t14-f", 70),
          ("t18", 125),
          ("t1vi", 56),
          ("t1vi1-v2", 227),
          ("t1vi2", 228),
          ("unavailable", 1),
          ("vi2", 11),
          ("vi30", 13),
          ("vi4", 12),
          ("xdsl-adsl", 97),
          ("xdsl-bri", 99),
          ("xdsl-fec", 96),
          ("xdsl-fec-new", 130),
          ("xdsl-gshdsl", 98),
          ("xdsl-sa", 131),
          ("xdsl-scc", 100))
    )


_ModuleType_Type.__name__ = "Integer32"
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2, 1, 1, 3),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("mandatory")
_ModuleFirstPort_Type = Integer32
_ModuleFirstPort_Object = MibTableColumn
moduleFirstPort = _ModuleFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2, 1, 1, 4),
    _ModuleFirstPort_Type()
)
moduleFirstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFirstPort.setStatus("mandatory")
_ModuleNumberOfPorts_Type = Integer32
_ModuleNumberOfPorts_Object = MibTableColumn
moduleNumberOfPorts = _ModuleNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2, 1, 1, 5),
    _ModuleNumberOfPorts_Type()
)
moduleNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumberOfPorts.setStatus("mandatory")
_ModuleVersion_Type = Integer32
_ModuleVersion_Object = MibTableColumn
moduleVersion = _ModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2, 1, 1, 6),
    _ModuleVersion_Type()
)
moduleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVersion.setStatus("obsolete")
_ModuleSwVersion_Type = DisplayString
_ModuleSwVersion_Object = MibTableColumn
moduleSwVersion = _ModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2, 1, 1, 7),
    _ModuleSwVersion_Type()
)
moduleSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwVersion.setStatus("mandatory")
_ModuleHwVersion_Type = DisplayString
_ModuleHwVersion_Object = MibTableColumn
moduleHwVersion = _ModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 2, 1, 1, 8),
    _ModuleHwVersion_Type()
)
moduleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwVersion.setStatus("mandatory")
_HwFlashMan_ObjectIdentity = ObjectIdentity
hwFlashMan = _HwFlashMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 3)
)
_HwFlhTotalSize_Type = Integer32
_HwFlhTotalSize_Object = MibScalar
hwFlhTotalSize = _HwFlhTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 3, 1),
    _HwFlhTotalSize_Type()
)
hwFlhTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhTotalSize.setStatus("mandatory")
_HwFlhUnusedSize_Type = Integer32
_HwFlhUnusedSize_Object = MibScalar
hwFlhUnusedSize = _HwFlhUnusedSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 3, 2),
    _HwFlhUnusedSize_Type()
)
hwFlhUnusedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhUnusedSize.setStatus("mandatory")
_HwFlhEraseTime_Type = TimeTicks
_HwFlhEraseTime_Object = MibScalar
hwFlhEraseTime = _HwFlhEraseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 3, 3),
    _HwFlhEraseTime_Type()
)
hwFlhEraseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhEraseTime.setStatus("mandatory")
_HwFlhEraseStat_Type = HwFlashEreaseStatus
_HwFlhEraseStat_Object = MibScalar
hwFlhEraseStat = _HwFlhEraseStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 3, 4),
    _HwFlhEraseStat_Type()
)
hwFlhEraseStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhEraseStat.setStatus("mandatory")
_HwFlhCurStat_Type = HwFlashStatus
_HwFlhCurStat_Object = MibScalar
hwFlhCurStat = _HwFlhCurStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 3, 5),
    _HwFlhCurStat_Type()
)
hwFlhCurStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhCurStat.setStatus("mandatory")
_HuaweiMixinfo_ObjectIdentity = ObjectIdentity
huaweiMixinfo = _HuaweiMixinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4)
)
_HwModuleId_Type = DisplayString
_HwModuleId_Object = MibScalar
hwModuleId = _HwModuleId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 1),
    _HwModuleId_Type()
)
hwModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwModuleId.setStatus("mandatory")
_HwROMID_Type = DisplayString
_HwROMID_Object = MibScalar
hwROMID = _HwROMID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 2),
    _HwROMID_Type()
)
hwROMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwROMID.setStatus("mandatory")
_HwROMVersion_Type = DisplayString
_HwROMVersion_Object = MibScalar
hwROMVersion = _HwROMVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 3),
    _HwROMVersion_Type()
)
hwROMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwROMVersion.setStatus("mandatory")
_HwROMSysVersion_Type = DisplayString
_HwROMSysVersion_Object = MibScalar
hwROMSysVersion = _HwROMSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 4),
    _HwROMSysVersion_Type()
)
hwROMSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwROMSysVersion.setStatus("mandatory")
_HwRAMSize_Type = Integer32
_HwRAMSize_Object = MibScalar
hwRAMSize = _HwRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 5),
    _HwRAMSize_Type()
)
hwRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRAMSize.setStatus("mandatory")
_HwNVRAMSize_Type = Integer32
_HwNVRAMSize_Object = MibScalar
hwNVRAMSize = _HwNVRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 6),
    _HwNVRAMSize_Type()
)
hwNVRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNVRAMSize.setStatus("mandatory")
_HwNVRAMUsed_Type = Integer32
_HwNVRAMUsed_Object = MibScalar
hwNVRAMUsed = _HwNVRAMUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 7),
    _HwNVRAMUsed_Type()
)
hwNVRAMUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNVRAMUsed.setStatus("mandatory")


class _HwConfigReg_Type(Integer32):
    """Custom type hwConfigReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("nvram", 2))
    )


_HwConfigReg_Type.__name__ = "Integer32"
_HwConfigReg_Object = MibScalar
hwConfigReg = _HwConfigReg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 8),
    _HwConfigReg_Type()
)
hwConfigReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConfigReg.setStatus("mandatory")
_HwConfigRegNextReboot_Type = Integer32
_HwConfigRegNextReboot_Object = MibScalar
hwConfigRegNextReboot = _HwConfigRegNextReboot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 9),
    _HwConfigRegNextReboot_Type()
)
hwConfigRegNextReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConfigRegNextReboot.setStatus("mandatory")


class _HwTFTPEnabled_Type(Integer32):
    """Custom type hwTFTPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HwTFTPEnabled_Type.__name__ = "Integer32"
_HwTFTPEnabled_Object = MibScalar
hwTFTPEnabled = _HwTFTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 10),
    _HwTFTPEnabled_Type()
)
hwTFTPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTFTPEnabled.setStatus("mandatory")
_HwMemoryFree_Type = Integer32
_HwMemoryFree_Object = MibScalar
hwMemoryFree = _HwMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 11),
    _HwMemoryFree_Type()
)
hwMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryFree.setStatus("obsolete")
_HwCpuCostRatePer5Sec_Type = Integer32
_HwCpuCostRatePer5Sec_Object = MibScalar
hwCpuCostRatePer5Sec = _HwCpuCostRatePer5Sec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 12),
    _HwCpuCostRatePer5Sec_Type()
)
hwCpuCostRatePer5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCpuCostRatePer5Sec.setStatus("mandatory")
_HwCpuCostRatePer5Minute_Type = Integer32
_HwCpuCostRatePer5Minute_Object = MibScalar
hwCpuCostRatePer5Minute = _HwCpuCostRatePer5Minute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 13),
    _HwCpuCostRatePer5Minute_Type()
)
hwCpuCostRatePer5Minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCpuCostRatePer5Minute.setStatus("mandatory")
_HwCurrentTime_Type = TimeTicks
_HwCurrentTime_Object = MibScalar
hwCurrentTime = _HwCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 14),
    _HwCurrentTime_Type()
)
hwCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCurrentTime.setStatus("mandatory")


class _HwSysAirFlowTempIn_Type(Integer32):
    """Custom type hwSysAirFlowTempIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("overcold", 1),
          ("overhot", 2))
    )


_HwSysAirFlowTempIn_Type.__name__ = "Integer32"
_HwSysAirFlowTempIn_Object = MibScalar
hwSysAirFlowTempIn = _HwSysAirFlowTempIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 15),
    _HwSysAirFlowTempIn_Type()
)
hwSysAirFlowTempIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysAirFlowTempIn.setStatus("mandatory")


class _HwBuzzerStatus_Type(Integer32):
    """Custom type hwBuzzerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("silence", 1),
          ("tweet", 2))
    )


_HwBuzzerStatus_Type.__name__ = "Integer32"
_HwBuzzerStatus_Object = MibScalar
hwBuzzerStatus = _HwBuzzerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 16),
    _HwBuzzerStatus_Type()
)
hwBuzzerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuzzerStatus.setStatus("mandatory")


class _HwFansStatus_Type(Integer32):
    """Custom type hwFansStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nofan", 2),
          ("running", 0),
          ("stopping", 1))
    )


_HwFansStatus_Type.__name__ = "Integer32"
_HwFansStatus_Object = MibScalar
hwFansStatus = _HwFansStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 17),
    _HwFansStatus_Type()
)
hwFansStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFansStatus.setStatus("mandatory")


class _HwPowerStatus_Type(Integer32):
    """Custom type hwPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("nopower", 2),
          ("ok", 0))
    )


_HwPowerStatus_Type.__name__ = "Integer32"
_HwPowerStatus_Object = MibScalar
hwPowerStatus = _HwPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 18),
    _HwPowerStatus_Type()
)
hwPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPowerStatus.setStatus("mandatory")


class _HwSecondPowerStatus_Type(Integer32):
    """Custom type hwSecondPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("nopower", 2),
          ("ok", 0))
    )


_HwSecondPowerStatus_Type.__name__ = "Integer32"
_HwSecondPowerStatus_Object = MibScalar
hwSecondPowerStatus = _HwSecondPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 4, 19),
    _HwSecondPowerStatus_Type()
)
hwSecondPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecondPowerStatus.setStatus("mandatory")
_HuaweiMemoryMan_ObjectIdentity = ObjectIdentity
huaweiMemoryMan = _HuaweiMemoryMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5)
)
_HwUsedMemory_Type = Gauge32
_HwUsedMemory_Object = MibScalar
hwUsedMemory = _HwUsedMemory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 1),
    _HwUsedMemory_Type()
)
hwUsedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUsedMemory.setStatus("mandatory")
_HwFreeMemory_Type = Gauge32
_HwFreeMemory_Object = MibScalar
hwFreeMemory = _HwFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 2),
    _HwFreeMemory_Type()
)
hwFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFreeMemory.setStatus("mandatory")
_HwMemoryLargestFree_Type = Gauge32
_HwMemoryLargestFree_Object = MibScalar
hwMemoryLargestFree = _HwMemoryLargestFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 3),
    _HwMemoryLargestFree_Type()
)
hwMemoryLargestFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryLargestFree.setStatus("mandatory")
_HwBuffer32Size_Type = Integer32
_HwBuffer32Size_Object = MibScalar
hwBuffer32Size = _HwBuffer32Size_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 4),
    _HwBuffer32Size_Type()
)
hwBuffer32Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer32Size.setStatus("mandatory")
_HwBuffer32Total_Type = Integer32
_HwBuffer32Total_Object = MibScalar
hwBuffer32Total = _HwBuffer32Total_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 5),
    _HwBuffer32Total_Type()
)
hwBuffer32Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer32Total.setStatus("mandatory")
_HwBuffer32Free_Type = Integer32
_HwBuffer32Free_Object = MibScalar
hwBuffer32Free = _HwBuffer32Free_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 6),
    _HwBuffer32Free_Type()
)
hwBuffer32Free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer32Free.setStatus("mandatory")
_HwBuffer32Used_Type = Integer32
_HwBuffer32Used_Object = MibScalar
hwBuffer32Used = _HwBuffer32Used_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 7),
    _HwBuffer32Used_Type()
)
hwBuffer32Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer32Used.setStatus("mandatory")
_HwBuffer32DropCounts_Type = Integer32
_HwBuffer32DropCounts_Object = MibScalar
hwBuffer32DropCounts = _HwBuffer32DropCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 8),
    _HwBuffer32DropCounts_Type()
)
hwBuffer32DropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer32DropCounts.setStatus("mandatory")
_HwBuffer32FreeError2_Type = Integer32
_HwBuffer32FreeError2_Object = MibScalar
hwBuffer32FreeError2 = _HwBuffer32FreeError2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 9),
    _HwBuffer32FreeError2_Type()
)
hwBuffer32FreeError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer32FreeError2.setStatus("mandatory")
_HwBuffer32FreeError3_Type = Integer32
_HwBuffer32FreeError3_Object = MibScalar
hwBuffer32FreeError3 = _HwBuffer32FreeError3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 10),
    _HwBuffer32FreeError3_Type()
)
hwBuffer32FreeError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer32FreeError3.setStatus("mandatory")
_HwBuffer32CollectCounts_Type = Integer32
_HwBuffer32CollectCounts_Object = MibScalar
hwBuffer32CollectCounts = _HwBuffer32CollectCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 11),
    _HwBuffer32CollectCounts_Type()
)
hwBuffer32CollectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer32CollectCounts.setStatus("mandatory")
_HwBuffer64Size_Type = Integer32
_HwBuffer64Size_Object = MibScalar
hwBuffer64Size = _HwBuffer64Size_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 12),
    _HwBuffer64Size_Type()
)
hwBuffer64Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer64Size.setStatus("mandatory")
_HwBuffer64Total_Type = Integer32
_HwBuffer64Total_Object = MibScalar
hwBuffer64Total = _HwBuffer64Total_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 13),
    _HwBuffer64Total_Type()
)
hwBuffer64Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer64Total.setStatus("mandatory")
_HwBuffer64Free_Type = Integer32
_HwBuffer64Free_Object = MibScalar
hwBuffer64Free = _HwBuffer64Free_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 14),
    _HwBuffer64Free_Type()
)
hwBuffer64Free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer64Free.setStatus("mandatory")
_HwBuffer64Used_Type = Integer32
_HwBuffer64Used_Object = MibScalar
hwBuffer64Used = _HwBuffer64Used_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 15),
    _HwBuffer64Used_Type()
)
hwBuffer64Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer64Used.setStatus("mandatory")
_HwBuffer64DropCounts_Type = Integer32
_HwBuffer64DropCounts_Object = MibScalar
hwBuffer64DropCounts = _HwBuffer64DropCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 16),
    _HwBuffer64DropCounts_Type()
)
hwBuffer64DropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer64DropCounts.setStatus("mandatory")
_HwBuffer64FreeError2_Type = Integer32
_HwBuffer64FreeError2_Object = MibScalar
hwBuffer64FreeError2 = _HwBuffer64FreeError2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 17),
    _HwBuffer64FreeError2_Type()
)
hwBuffer64FreeError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer64FreeError2.setStatus("mandatory")
_HwBuffer64FreeError3_Type = Integer32
_HwBuffer64FreeError3_Object = MibScalar
hwBuffer64FreeError3 = _HwBuffer64FreeError3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 18),
    _HwBuffer64FreeError3_Type()
)
hwBuffer64FreeError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer64FreeError3.setStatus("mandatory")
_HwBuffer64CollectCounts_Type = Integer32
_HwBuffer64CollectCounts_Object = MibScalar
hwBuffer64CollectCounts = _HwBuffer64CollectCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 19),
    _HwBuffer64CollectCounts_Type()
)
hwBuffer64CollectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer64CollectCounts.setStatus("mandatory")
_HwBuffer128Size_Type = Integer32
_HwBuffer128Size_Object = MibScalar
hwBuffer128Size = _HwBuffer128Size_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 20),
    _HwBuffer128Size_Type()
)
hwBuffer128Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer128Size.setStatus("mandatory")
_HwBuffer128Total_Type = Integer32
_HwBuffer128Total_Object = MibScalar
hwBuffer128Total = _HwBuffer128Total_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 21),
    _HwBuffer128Total_Type()
)
hwBuffer128Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer128Total.setStatus("mandatory")
_HwBuffer128Free_Type = Integer32
_HwBuffer128Free_Object = MibScalar
hwBuffer128Free = _HwBuffer128Free_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 22),
    _HwBuffer128Free_Type()
)
hwBuffer128Free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer128Free.setStatus("mandatory")
_HwBuffer128Used_Type = Integer32
_HwBuffer128Used_Object = MibScalar
hwBuffer128Used = _HwBuffer128Used_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 23),
    _HwBuffer128Used_Type()
)
hwBuffer128Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer128Used.setStatus("mandatory")
_HwBuffer128DropCounts_Type = Integer32
_HwBuffer128DropCounts_Object = MibScalar
hwBuffer128DropCounts = _HwBuffer128DropCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 24),
    _HwBuffer128DropCounts_Type()
)
hwBuffer128DropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer128DropCounts.setStatus("mandatory")
_HwBuffer128FreeError2_Type = Integer32
_HwBuffer128FreeError2_Object = MibScalar
hwBuffer128FreeError2 = _HwBuffer128FreeError2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 25),
    _HwBuffer128FreeError2_Type()
)
hwBuffer128FreeError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer128FreeError2.setStatus("mandatory")
_HwBuffer128FreeError3_Type = Integer32
_HwBuffer128FreeError3_Object = MibScalar
hwBuffer128FreeError3 = _HwBuffer128FreeError3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 26),
    _HwBuffer128FreeError3_Type()
)
hwBuffer128FreeError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer128FreeError3.setStatus("mandatory")
_HwBuffer128CollectCounts_Type = Integer32
_HwBuffer128CollectCounts_Object = MibScalar
hwBuffer128CollectCounts = _HwBuffer128CollectCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 27),
    _HwBuffer128CollectCounts_Type()
)
hwBuffer128CollectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer128CollectCounts.setStatus("mandatory")
_HwBuffer256Size_Type = Integer32
_HwBuffer256Size_Object = MibScalar
hwBuffer256Size = _HwBuffer256Size_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 28),
    _HwBuffer256Size_Type()
)
hwBuffer256Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256Size.setStatus("mandatory")
_HwBuffer256Total_Type = Integer32
_HwBuffer256Total_Object = MibScalar
hwBuffer256Total = _HwBuffer256Total_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 29),
    _HwBuffer256Total_Type()
)
hwBuffer256Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256Total.setStatus("mandatory")
_HwBuffer256Free_Type = Integer32
_HwBuffer256Free_Object = MibScalar
hwBuffer256Free = _HwBuffer256Free_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 30),
    _HwBuffer256Free_Type()
)
hwBuffer256Free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256Free.setStatus("mandatory")
_HwBuffer256Used_Type = Integer32
_HwBuffer256Used_Object = MibScalar
hwBuffer256Used = _HwBuffer256Used_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 31),
    _HwBuffer256Used_Type()
)
hwBuffer256Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256Used.setStatus("mandatory")
_HwBuffer256DropCounts_Type = Integer32
_HwBuffer256DropCounts_Object = MibScalar
hwBuffer256DropCounts = _HwBuffer256DropCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 32),
    _HwBuffer256DropCounts_Type()
)
hwBuffer256DropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256DropCounts.setStatus("mandatory")
_HwBuffer256FreeError2_Type = Integer32
_HwBuffer256FreeError2_Object = MibScalar
hwBuffer256FreeError2 = _HwBuffer256FreeError2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 33),
    _HwBuffer256FreeError2_Type()
)
hwBuffer256FreeError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256FreeError2.setStatus("mandatory")
_HwBuffer256FreeError3_Type = Integer32
_HwBuffer256FreeError3_Object = MibScalar
hwBuffer256FreeError3 = _HwBuffer256FreeError3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 34),
    _HwBuffer256FreeError3_Type()
)
hwBuffer256FreeError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256FreeError3.setStatus("mandatory")
_HwBuffer256CollectCounts_Type = Integer32
_HwBuffer256CollectCounts_Object = MibScalar
hwBuffer256CollectCounts = _HwBuffer256CollectCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 35),
    _HwBuffer256CollectCounts_Type()
)
hwBuffer256CollectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256CollectCounts.setStatus("mandatory")
_HwBuffer512Size_Type = Integer32
_HwBuffer512Size_Object = MibScalar
hwBuffer512Size = _HwBuffer512Size_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 36),
    _HwBuffer512Size_Type()
)
hwBuffer512Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer512Size.setStatus("mandatory")
_HwBuffer512Total_Type = Integer32
_HwBuffer512Total_Object = MibScalar
hwBuffer512Total = _HwBuffer512Total_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 37),
    _HwBuffer512Total_Type()
)
hwBuffer512Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer512Total.setStatus("mandatory")
_HwBuffer512Free_Type = Integer32
_HwBuffer512Free_Object = MibScalar
hwBuffer512Free = _HwBuffer512Free_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 38),
    _HwBuffer512Free_Type()
)
hwBuffer512Free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer512Free.setStatus("mandatory")
_HwBuffer512Used_Type = Integer32
_HwBuffer512Used_Object = MibScalar
hwBuffer512Used = _HwBuffer512Used_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 39),
    _HwBuffer512Used_Type()
)
hwBuffer512Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer512Used.setStatus("mandatory")
_HwBuffer512DropCounts_Type = Integer32
_HwBuffer512DropCounts_Object = MibScalar
hwBuffer512DropCounts = _HwBuffer512DropCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 40),
    _HwBuffer512DropCounts_Type()
)
hwBuffer512DropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer512DropCounts.setStatus("mandatory")
_HwBuffer512FreeError2_Type = Integer32
_HwBuffer512FreeError2_Object = MibScalar
hwBuffer512FreeError2 = _HwBuffer512FreeError2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 41),
    _HwBuffer512FreeError2_Type()
)
hwBuffer512FreeError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer512FreeError2.setStatus("mandatory")
_HwBuffer512FreeError3_Type = Integer32
_HwBuffer512FreeError3_Object = MibScalar
hwBuffer512FreeError3 = _HwBuffer512FreeError3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 42),
    _HwBuffer512FreeError3_Type()
)
hwBuffer512FreeError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer512FreeError3.setStatus("mandatory")
_HwBuffer512CollectCounts_Type = Integer32
_HwBuffer512CollectCounts_Object = MibScalar
hwBuffer512CollectCounts = _HwBuffer512CollectCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 43),
    _HwBuffer512CollectCounts_Type()
)
hwBuffer512CollectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer512CollectCounts.setStatus("mandatory")
_HwBuffer1024Size_Type = Integer32
_HwBuffer1024Size_Object = MibScalar
hwBuffer1024Size = _HwBuffer1024Size_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 44),
    _HwBuffer1024Size_Type()
)
hwBuffer1024Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer1024Size.setStatus("mandatory")
_HwBuffer1024Total_Type = Integer32
_HwBuffer1024Total_Object = MibScalar
hwBuffer1024Total = _HwBuffer1024Total_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 45),
    _HwBuffer1024Total_Type()
)
hwBuffer1024Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer1024Total.setStatus("mandatory")
_HwBuffer1024Free_Type = Integer32
_HwBuffer1024Free_Object = MibScalar
hwBuffer1024Free = _HwBuffer1024Free_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 46),
    _HwBuffer1024Free_Type()
)
hwBuffer1024Free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer1024Free.setStatus("mandatory")
_HwBuffer1024Used_Type = Integer32
_HwBuffer1024Used_Object = MibScalar
hwBuffer1024Used = _HwBuffer1024Used_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 47),
    _HwBuffer1024Used_Type()
)
hwBuffer1024Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer1024Used.setStatus("mandatory")
_HwBuffer1024DropCounts_Type = Integer32
_HwBuffer1024DropCounts_Object = MibScalar
hwBuffer1024DropCounts = _HwBuffer1024DropCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 48),
    _HwBuffer1024DropCounts_Type()
)
hwBuffer1024DropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer1024DropCounts.setStatus("mandatory")
_HwBuffer1024FreeError2_Type = Integer32
_HwBuffer1024FreeError2_Object = MibScalar
hwBuffer1024FreeError2 = _HwBuffer1024FreeError2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 49),
    _HwBuffer1024FreeError2_Type()
)
hwBuffer1024FreeError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer1024FreeError2.setStatus("mandatory")
_HwBuffer1024FreeError3_Type = Integer32
_HwBuffer1024FreeError3_Object = MibScalar
hwBuffer1024FreeError3 = _HwBuffer1024FreeError3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 50),
    _HwBuffer1024FreeError3_Type()
)
hwBuffer1024FreeError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer1024FreeError3.setStatus("mandatory")
_HwBuffer1024CollectCounts_Type = Integer32
_HwBuffer1024CollectCounts_Object = MibScalar
hwBuffer1024CollectCounts = _HwBuffer1024CollectCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 51),
    _HwBuffer1024CollectCounts_Type()
)
hwBuffer1024CollectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer1024CollectCounts.setStatus("mandatory")
_HwBuffer2048Size_Type = Integer32
_HwBuffer2048Size_Object = MibScalar
hwBuffer2048Size = _HwBuffer2048Size_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 52),
    _HwBuffer2048Size_Type()
)
hwBuffer2048Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer2048Size.setStatus("mandatory")
_HwBuffer2048Total_Type = Integer32
_HwBuffer2048Total_Object = MibScalar
hwBuffer2048Total = _HwBuffer2048Total_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 53),
    _HwBuffer2048Total_Type()
)
hwBuffer2048Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer2048Total.setStatus("mandatory")
_HwBuffer2048Free_Type = Integer32
_HwBuffer2048Free_Object = MibScalar
hwBuffer2048Free = _HwBuffer2048Free_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 54),
    _HwBuffer2048Free_Type()
)
hwBuffer2048Free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer2048Free.setStatus("mandatory")
_HwBuffer2048Used_Type = Integer32
_HwBuffer2048Used_Object = MibScalar
hwBuffer2048Used = _HwBuffer2048Used_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 55),
    _HwBuffer2048Used_Type()
)
hwBuffer2048Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer2048Used.setStatus("mandatory")
_HwBuffer2048DropCounts_Type = Integer32
_HwBuffer2048DropCounts_Object = MibScalar
hwBuffer2048DropCounts = _HwBuffer2048DropCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 56),
    _HwBuffer2048DropCounts_Type()
)
hwBuffer2048DropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer2048DropCounts.setStatus("mandatory")
_HwBuffer2048FreeError2_Type = Integer32
_HwBuffer2048FreeError2_Object = MibScalar
hwBuffer2048FreeError2 = _HwBuffer2048FreeError2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 57),
    _HwBuffer2048FreeError2_Type()
)
hwBuffer2048FreeError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer2048FreeError2.setStatus("mandatory")
_HwBuffer2048FreeError3_Type = Integer32
_HwBuffer2048FreeError3_Object = MibScalar
hwBuffer2048FreeError3 = _HwBuffer2048FreeError3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 58),
    _HwBuffer2048FreeError3_Type()
)
hwBuffer2048FreeError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer2048FreeError3.setStatus("mandatory")
_HwBuffer2048CollectCounts_Type = Integer32
_HwBuffer2048CollectCounts_Object = MibScalar
hwBuffer2048CollectCounts = _HwBuffer2048CollectCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 59),
    _HwBuffer2048CollectCounts_Type()
)
hwBuffer2048CollectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer2048CollectCounts.setStatus("mandatory")
_HwBuffer4096Size_Type = Integer32
_HwBuffer4096Size_Object = MibScalar
hwBuffer4096Size = _HwBuffer4096Size_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 60),
    _HwBuffer4096Size_Type()
)
hwBuffer4096Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer4096Size.setStatus("mandatory")
_HwBuffer4096Total_Type = Integer32
_HwBuffer4096Total_Object = MibScalar
hwBuffer4096Total = _HwBuffer4096Total_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 61),
    _HwBuffer4096Total_Type()
)
hwBuffer4096Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer4096Total.setStatus("mandatory")
_HwBuffer4096Free_Type = Integer32
_HwBuffer4096Free_Object = MibScalar
hwBuffer4096Free = _HwBuffer4096Free_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 62),
    _HwBuffer4096Free_Type()
)
hwBuffer4096Free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer4096Free.setStatus("mandatory")
_HwBuffer4096Used_Type = Integer32
_HwBuffer4096Used_Object = MibScalar
hwBuffer4096Used = _HwBuffer4096Used_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 63),
    _HwBuffer4096Used_Type()
)
hwBuffer4096Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer4096Used.setStatus("mandatory")
_HwBuffer4096DropCounts_Type = Integer32
_HwBuffer4096DropCounts_Object = MibScalar
hwBuffer4096DropCounts = _HwBuffer4096DropCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 64),
    _HwBuffer4096DropCounts_Type()
)
hwBuffer4096DropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer4096DropCounts.setStatus("mandatory")
_HwBuffer4096FreeError2_Type = Integer32
_HwBuffer4096FreeError2_Object = MibScalar
hwBuffer4096FreeError2 = _HwBuffer4096FreeError2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 65),
    _HwBuffer4096FreeError2_Type()
)
hwBuffer4096FreeError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer4096FreeError2.setStatus("mandatory")
_HwBuffer4096FreeError3_Type = Integer32
_HwBuffer4096FreeError3_Object = MibScalar
hwBuffer4096FreeError3 = _HwBuffer4096FreeError3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 66),
    _HwBuffer4096FreeError3_Type()
)
hwBuffer4096FreeError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer4096FreeError3.setStatus("mandatory")
_HwBuffer4096CollectCounts_Type = Integer32
_HwBuffer4096CollectCounts_Object = MibScalar
hwBuffer4096CollectCounts = _HwBuffer4096CollectCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 67),
    _HwBuffer4096CollectCounts_Type()
)
hwBuffer4096CollectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer4096CollectCounts.setStatus("mandatory")
_HwBuffer8192Size_Type = Integer32
_HwBuffer8192Size_Object = MibScalar
hwBuffer8192Size = _HwBuffer8192Size_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 68),
    _HwBuffer8192Size_Type()
)
hwBuffer8192Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer8192Size.setStatus("mandatory")
_HwBuffer8192Total_Type = Integer32
_HwBuffer8192Total_Object = MibScalar
hwBuffer8192Total = _HwBuffer8192Total_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 69),
    _HwBuffer8192Total_Type()
)
hwBuffer8192Total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer8192Total.setStatus("mandatory")
_HwBuffer8192Free_Type = Integer32
_HwBuffer8192Free_Object = MibScalar
hwBuffer8192Free = _HwBuffer8192Free_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 70),
    _HwBuffer8192Free_Type()
)
hwBuffer8192Free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer8192Free.setStatus("mandatory")
_HwBuffer8192Used_Type = Integer32
_HwBuffer8192Used_Object = MibScalar
hwBuffer8192Used = _HwBuffer8192Used_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 71),
    _HwBuffer8192Used_Type()
)
hwBuffer8192Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer8192Used.setStatus("mandatory")
_HwBuffer8192DropCounts_Type = Integer32
_HwBuffer8192DropCounts_Object = MibScalar
hwBuffer8192DropCounts = _HwBuffer8192DropCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 72),
    _HwBuffer8192DropCounts_Type()
)
hwBuffer8192DropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer8192DropCounts.setStatus("mandatory")
_HwBuffer8192FreeError2_Type = Integer32
_HwBuffer8192FreeError2_Object = MibScalar
hwBuffer8192FreeError2 = _HwBuffer8192FreeError2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 73),
    _HwBuffer8192FreeError2_Type()
)
hwBuffer8192FreeError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer8192FreeError2.setStatus("mandatory")
_HwBuffer8192FreeError3_Type = Integer32
_HwBuffer8192FreeError3_Object = MibScalar
hwBuffer8192FreeError3 = _HwBuffer8192FreeError3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 74),
    _HwBuffer8192FreeError3_Type()
)
hwBuffer8192FreeError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer8192FreeError3.setStatus("mandatory")
_HwBuffer8192CollectCounts_Type = Integer32
_HwBuffer8192CollectCounts_Object = MibScalar
hwBuffer8192CollectCounts = _HwBuffer8192CollectCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 75),
    _HwBuffer8192CollectCounts_Type()
)
hwBuffer8192CollectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer8192CollectCounts.setStatus("mandatory")
_HwBuffer45KSize_Type = Integer32
_HwBuffer45KSize_Object = MibScalar
hwBuffer45KSize = _HwBuffer45KSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 76),
    _HwBuffer45KSize_Type()
)
hwBuffer45KSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer45KSize.setStatus("mandatory")
_HwBuffer45KTotal_Type = Integer32
_HwBuffer45KTotal_Object = MibScalar
hwBuffer45KTotal = _HwBuffer45KTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 77),
    _HwBuffer45KTotal_Type()
)
hwBuffer45KTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer45KTotal.setStatus("mandatory")
_HwBuffer45KFree_Type = Integer32
_HwBuffer45KFree_Object = MibScalar
hwBuffer45KFree = _HwBuffer45KFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 78),
    _HwBuffer45KFree_Type()
)
hwBuffer45KFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer45KFree.setStatus("mandatory")
_HwBuffer45KUsed_Type = Integer32
_HwBuffer45KUsed_Object = MibScalar
hwBuffer45KUsed = _HwBuffer45KUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 79),
    _HwBuffer45KUsed_Type()
)
hwBuffer45KUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer45KUsed.setStatus("mandatory")
_HwBuffer45KDropCounts_Type = Integer32
_HwBuffer45KDropCounts_Object = MibScalar
hwBuffer45KDropCounts = _HwBuffer45KDropCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 80),
    _HwBuffer45KDropCounts_Type()
)
hwBuffer45KDropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer45KDropCounts.setStatus("mandatory")
_HwBuffer45KFreeError2_Type = Integer32
_HwBuffer45KFreeError2_Object = MibScalar
hwBuffer45KFreeError2 = _HwBuffer45KFreeError2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 81),
    _HwBuffer45KFreeError2_Type()
)
hwBuffer45KFreeError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer45KFreeError2.setStatus("mandatory")
_HwBuffer45KFreeError3_Type = Integer32
_HwBuffer45KFreeError3_Object = MibScalar
hwBuffer45KFreeError3 = _HwBuffer45KFreeError3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 82),
    _HwBuffer45KFreeError3_Type()
)
hwBuffer45KFreeError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer45KFreeError3.setStatus("mandatory")
_HwBuffer45KCollectCounts_Type = Integer32
_HwBuffer45KCollectCounts_Object = MibScalar
hwBuffer45KCollectCounts = _HwBuffer45KCollectCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 83),
    _HwBuffer45KCollectCounts_Type()
)
hwBuffer45KCollectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer45KCollectCounts.setStatus("mandatory")
_HwBuffer256KSize_Type = Integer32
_HwBuffer256KSize_Object = MibScalar
hwBuffer256KSize = _HwBuffer256KSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 84),
    _HwBuffer256KSize_Type()
)
hwBuffer256KSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256KSize.setStatus("mandatory")
_HwBuffer256KTotal_Type = Integer32
_HwBuffer256KTotal_Object = MibScalar
hwBuffer256KTotal = _HwBuffer256KTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 85),
    _HwBuffer256KTotal_Type()
)
hwBuffer256KTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256KTotal.setStatus("mandatory")
_HwBuffer256KFree_Type = Integer32
_HwBuffer256KFree_Object = MibScalar
hwBuffer256KFree = _HwBuffer256KFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 86),
    _HwBuffer256KFree_Type()
)
hwBuffer256KFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256KFree.setStatus("mandatory")
_HwBuffer256KUsed_Type = Integer32
_HwBuffer256KUsed_Object = MibScalar
hwBuffer256KUsed = _HwBuffer256KUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 87),
    _HwBuffer256KUsed_Type()
)
hwBuffer256KUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256KUsed.setStatus("mandatory")
_HwBuffer256KDropCounts_Type = Integer32
_HwBuffer256KDropCounts_Object = MibScalar
hwBuffer256KDropCounts = _HwBuffer256KDropCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 88),
    _HwBuffer256KDropCounts_Type()
)
hwBuffer256KDropCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256KDropCounts.setStatus("mandatory")
_HwBuffer256KFreeError2_Type = Integer32
_HwBuffer256KFreeError2_Object = MibScalar
hwBuffer256KFreeError2 = _HwBuffer256KFreeError2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 89),
    _HwBuffer256KFreeError2_Type()
)
hwBuffer256KFreeError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256KFreeError2.setStatus("mandatory")
_HwBuffer256KFreeError3_Type = Integer32
_HwBuffer256KFreeError3_Object = MibScalar
hwBuffer256KFreeError3 = _HwBuffer256KFreeError3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 90),
    _HwBuffer256KFreeError3_Type()
)
hwBuffer256KFreeError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256KFreeError3.setStatus("mandatory")
_HwBuffer256KCollectCounts_Type = Integer32
_HwBuffer256KCollectCounts_Object = MibScalar
hwBuffer256KCollectCounts = _HwBuffer256KCollectCounts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 91),
    _HwBuffer256KCollectCounts_Type()
)
hwBuffer256KCollectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBuffer256KCollectCounts.setStatus("mandatory")
_HwMemoryMallocFail_Type = Integer32
_HwMemoryMallocFail_Object = MibScalar
hwMemoryMallocFail = _HwMemoryMallocFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 92),
    _HwMemoryMallocFail_Type()
)
hwMemoryMallocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryMallocFail.setStatus("mandatory")
_HwMemoryMallocNoMem_Type = Integer32
_HwMemoryMallocNoMem_Object = MibScalar
hwMemoryMallocNoMem = _HwMemoryMallocNoMem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 5, 93),
    _HwMemoryMallocNoMem_Type()
)
hwMemoryMallocNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryMallocNoMem.setStatus("mandatory")
_HwConfigFile_ObjectIdentity = ObjectIdentity
hwConfigFile = _HwConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 6)
)
_HwRunCfgChangedTime_Type = TimeTicks
_HwRunCfgChangedTime_Object = MibScalar
hwRunCfgChangedTime = _HwRunCfgChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 6, 1),
    _HwRunCfgChangedTime_Type()
)
hwRunCfgChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRunCfgChangedTime.setStatus("mandatory")
_HwRunCfgSavedTime_Type = TimeTicks
_HwRunCfgSavedTime_Object = MibScalar
hwRunCfgSavedTime = _HwRunCfgSavedTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 6, 2),
    _HwRunCfgSavedTime_Type()
)
hwRunCfgSavedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRunCfgSavedTime.setStatus("mandatory")
_HwStartCfgChangedTime_Type = TimeTicks
_HwStartCfgChangedTime_Object = MibScalar
hwStartCfgChangedTime = _HwStartCfgChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 6, 3),
    _HwStartCfgChangedTime_Type()
)
hwStartCfgChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStartCfgChangedTime.setStatus("mandatory")
_HwNetConfigName_Type = DisplayString
_HwNetConfigName_Object = MibScalar
hwNetConfigName = _HwNetConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 6, 4),
    _HwNetConfigName_Type()
)
hwNetConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNetConfigName.setStatus("mandatory")
_HwHostConfigName_Type = DisplayString
_HwHostConfigName_Object = MibScalar
hwHostConfigName = _HwHostConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 2, 6, 5),
    _HwHostConfigName_Type()
)
hwHostConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHostConfigName.setStatus("obsolete")
_HwmSystem_ObjectIdentity = ObjectIdentity
hwmSystem = _HwmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 6)
)
_HwmRouterSerialNO_Type = DisplayString
_HwmRouterSerialNO_Object = MibScalar
hwmRouterSerialNO = _HwmRouterSerialNO_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 6, 1),
    _HwmRouterSerialNO_Type()
)
hwmRouterSerialNO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwmRouterSerialNO.setStatus("mandatory")
_HwmWhyReboot_Type = DisplayString
_HwmWhyReboot_Object = MibScalar
hwmWhyReboot = _HwmWhyReboot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 6, 2),
    _HwmWhyReboot_Type()
)
hwmWhyReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwmWhyReboot.setStatus("mandatory")
_HwmHostName_Type = DisplayString
_HwmHostName_Object = MibScalar
hwmHostName = _HwmHostName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 6, 3),
    _HwmHostName_Type()
)
hwmHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwmHostName.setStatus("mandatory")
_HwmHostHwVersion_Type = DisplayString
_HwmHostHwVersion_Object = MibScalar
hwmHostHwVersion = _HwmHostHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 6, 4),
    _HwmHostHwVersion_Type()
)
hwmHostHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwmHostHwVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MLSR-DEV-ADM-MIB",
    **{"HwFlashStatus": HwFlashStatus,
       "HwFlashEreaseStatus": HwFlashEreaseStatus,
       "RowStatus": RowStatus,
       "routerGeneral": routerGeneral,
       "attr": attr,
       "basis": basis,
       "version": version,
       "trap": trap,
       "log": log,
       "logcontroller": logcontroller,
       "loghostTable": loghostTable,
       "loghostEntry": loghostEntry,
       "loghostIndex": loghostIndex,
       "loghostaddress": loghostaddress,
       "loghostport": loghostport,
       "loghostseverity": loghostseverity,
       "loghostlanguage": loghostlanguage,
       "loghostfacility": loghostfacility,
       "loghostaccess": loghostaccess,
       "loghoststatus": loghoststatus,
       "logfilterTable": logfilterTable,
       "logfilterEntry": logfilterEntry,
       "logfilterIndex": logfilterIndex,
       "logdevfacility": logdevfacility,
       "logfilterstatus": logfilterstatus,
       "vrp": vrp,
       "module": module,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleIndex": moduleIndex,
       "moduleSlotNum": moduleSlotNum,
       "moduleType": moduleType,
       "moduleFirstPort": moduleFirstPort,
       "moduleNumberOfPorts": moduleNumberOfPorts,
       "moduleVersion": moduleVersion,
       "moduleSwVersion": moduleSwVersion,
       "moduleHwVersion": moduleHwVersion,
       "hwFlashMan": hwFlashMan,
       "hwFlhTotalSize": hwFlhTotalSize,
       "hwFlhUnusedSize": hwFlhUnusedSize,
       "hwFlhEraseTime": hwFlhEraseTime,
       "hwFlhEraseStat": hwFlhEraseStat,
       "hwFlhCurStat": hwFlhCurStat,
       "huaweiMixinfo": huaweiMixinfo,
       "hwModuleId": hwModuleId,
       "hwROMID": hwROMID,
       "hwROMVersion": hwROMVersion,
       "hwROMSysVersion": hwROMSysVersion,
       "hwRAMSize": hwRAMSize,
       "hwNVRAMSize": hwNVRAMSize,
       "hwNVRAMUsed": hwNVRAMUsed,
       "hwConfigReg": hwConfigReg,
       "hwConfigRegNextReboot": hwConfigRegNextReboot,
       "hwTFTPEnabled": hwTFTPEnabled,
       "hwMemoryFree": hwMemoryFree,
       "hwCpuCostRatePer5Sec": hwCpuCostRatePer5Sec,
       "hwCpuCostRatePer5Minute": hwCpuCostRatePer5Minute,
       "hwCurrentTime": hwCurrentTime,
       "hwSysAirFlowTempIn": hwSysAirFlowTempIn,
       "hwBuzzerStatus": hwBuzzerStatus,
       "hwFansStatus": hwFansStatus,
       "hwPowerStatus": hwPowerStatus,
       "hwSecondPowerStatus": hwSecondPowerStatus,
       "huaweiMemoryMan": huaweiMemoryMan,
       "hwUsedMemory": hwUsedMemory,
       "hwFreeMemory": hwFreeMemory,
       "hwMemoryLargestFree": hwMemoryLargestFree,
       "hwBuffer32Size": hwBuffer32Size,
       "hwBuffer32Total": hwBuffer32Total,
       "hwBuffer32Free": hwBuffer32Free,
       "hwBuffer32Used": hwBuffer32Used,
       "hwBuffer32DropCounts": hwBuffer32DropCounts,
       "hwBuffer32FreeError2": hwBuffer32FreeError2,
       "hwBuffer32FreeError3": hwBuffer32FreeError3,
       "hwBuffer32CollectCounts": hwBuffer32CollectCounts,
       "hwBuffer64Size": hwBuffer64Size,
       "hwBuffer64Total": hwBuffer64Total,
       "hwBuffer64Free": hwBuffer64Free,
       "hwBuffer64Used": hwBuffer64Used,
       "hwBuffer64DropCounts": hwBuffer64DropCounts,
       "hwBuffer64FreeError2": hwBuffer64FreeError2,
       "hwBuffer64FreeError3": hwBuffer64FreeError3,
       "hwBuffer64CollectCounts": hwBuffer64CollectCounts,
       "hwBuffer128Size": hwBuffer128Size,
       "hwBuffer128Total": hwBuffer128Total,
       "hwBuffer128Free": hwBuffer128Free,
       "hwBuffer128Used": hwBuffer128Used,
       "hwBuffer128DropCounts": hwBuffer128DropCounts,
       "hwBuffer128FreeError2": hwBuffer128FreeError2,
       "hwBuffer128FreeError3": hwBuffer128FreeError3,
       "hwBuffer128CollectCounts": hwBuffer128CollectCounts,
       "hwBuffer256Size": hwBuffer256Size,
       "hwBuffer256Total": hwBuffer256Total,
       "hwBuffer256Free": hwBuffer256Free,
       "hwBuffer256Used": hwBuffer256Used,
       "hwBuffer256DropCounts": hwBuffer256DropCounts,
       "hwBuffer256FreeError2": hwBuffer256FreeError2,
       "hwBuffer256FreeError3": hwBuffer256FreeError3,
       "hwBuffer256CollectCounts": hwBuffer256CollectCounts,
       "hwBuffer512Size": hwBuffer512Size,
       "hwBuffer512Total": hwBuffer512Total,
       "hwBuffer512Free": hwBuffer512Free,
       "hwBuffer512Used": hwBuffer512Used,
       "hwBuffer512DropCounts": hwBuffer512DropCounts,
       "hwBuffer512FreeError2": hwBuffer512FreeError2,
       "hwBuffer512FreeError3": hwBuffer512FreeError3,
       "hwBuffer512CollectCounts": hwBuffer512CollectCounts,
       "hwBuffer1024Size": hwBuffer1024Size,
       "hwBuffer1024Total": hwBuffer1024Total,
       "hwBuffer1024Free": hwBuffer1024Free,
       "hwBuffer1024Used": hwBuffer1024Used,
       "hwBuffer1024DropCounts": hwBuffer1024DropCounts,
       "hwBuffer1024FreeError2": hwBuffer1024FreeError2,
       "hwBuffer1024FreeError3": hwBuffer1024FreeError3,
       "hwBuffer1024CollectCounts": hwBuffer1024CollectCounts,
       "hwBuffer2048Size": hwBuffer2048Size,
       "hwBuffer2048Total": hwBuffer2048Total,
       "hwBuffer2048Free": hwBuffer2048Free,
       "hwBuffer2048Used": hwBuffer2048Used,
       "hwBuffer2048DropCounts": hwBuffer2048DropCounts,
       "hwBuffer2048FreeError2": hwBuffer2048FreeError2,
       "hwBuffer2048FreeError3": hwBuffer2048FreeError3,
       "hwBuffer2048CollectCounts": hwBuffer2048CollectCounts,
       "hwBuffer4096Size": hwBuffer4096Size,
       "hwBuffer4096Total": hwBuffer4096Total,
       "hwBuffer4096Free": hwBuffer4096Free,
       "hwBuffer4096Used": hwBuffer4096Used,
       "hwBuffer4096DropCounts": hwBuffer4096DropCounts,
       "hwBuffer4096FreeError2": hwBuffer4096FreeError2,
       "hwBuffer4096FreeError3": hwBuffer4096FreeError3,
       "hwBuffer4096CollectCounts": hwBuffer4096CollectCounts,
       "hwBuffer8192Size": hwBuffer8192Size,
       "hwBuffer8192Total": hwBuffer8192Total,
       "hwBuffer8192Free": hwBuffer8192Free,
       "hwBuffer8192Used": hwBuffer8192Used,
       "hwBuffer8192DropCounts": hwBuffer8192DropCounts,
       "hwBuffer8192FreeError2": hwBuffer8192FreeError2,
       "hwBuffer8192FreeError3": hwBuffer8192FreeError3,
       "hwBuffer8192CollectCounts": hwBuffer8192CollectCounts,
       "hwBuffer45KSize": hwBuffer45KSize,
       "hwBuffer45KTotal": hwBuffer45KTotal,
       "hwBuffer45KFree": hwBuffer45KFree,
       "hwBuffer45KUsed": hwBuffer45KUsed,
       "hwBuffer45KDropCounts": hwBuffer45KDropCounts,
       "hwBuffer45KFreeError2": hwBuffer45KFreeError2,
       "hwBuffer45KFreeError3": hwBuffer45KFreeError3,
       "hwBuffer45KCollectCounts": hwBuffer45KCollectCounts,
       "hwBuffer256KSize": hwBuffer256KSize,
       "hwBuffer256KTotal": hwBuffer256KTotal,
       "hwBuffer256KFree": hwBuffer256KFree,
       "hwBuffer256KUsed": hwBuffer256KUsed,
       "hwBuffer256KDropCounts": hwBuffer256KDropCounts,
       "hwBuffer256KFreeError2": hwBuffer256KFreeError2,
       "hwBuffer256KFreeError3": hwBuffer256KFreeError3,
       "hwBuffer256KCollectCounts": hwBuffer256KCollectCounts,
       "hwMemoryMallocFail": hwMemoryMallocFail,
       "hwMemoryMallocNoMem": hwMemoryMallocNoMem,
       "hwConfigFile": hwConfigFile,
       "hwRunCfgChangedTime": hwRunCfgChangedTime,
       "hwRunCfgSavedTime": hwRunCfgSavedTime,
       "hwStartCfgChangedTime": hwStartCfgChangedTime,
       "hwNetConfigName": hwNetConfigName,
       "hwHostConfigName": hwHostConfigName,
       "hwmSystem": hwmSystem,
       "hwmRouterSerialNO": hwmRouterSerialNO,
       "hwmWhyReboot": hwmWhyReboot,
       "hwmHostName": hwmHostName,
       "hwmHostHwVersion": hwmHostHwVersion}
)
