# SNMP MIB module (Fore-Ifcreate-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Ifcreate-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:01 2024
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

(ifExtensions,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "ifExtensions")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

foreIfcreateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfReserveNextIndex_Type = TestAndIncr
_IfReserveNextIndex_Object = MibScalar
ifReserveNextIndex = _IfReserveNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 1),
    _IfReserveNextIndex_Type()
)
ifReserveNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifReserveNextIndex.setStatus("current")
_IfCreateTable_Object = MibTable
ifCreateTable = _IfCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 2)
)
if mibBuilder.loadTexts:
    ifCreateTable.setStatus("current")
_IfCreateEntry_Object = MibTableRow
ifCreateEntry = _IfCreateEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1)
)
ifCreateEntry.setIndexNames(
    (0, "Fore-Ifcreate-MIB", "ifCreateIfIndex"),
)
if mibBuilder.loadTexts:
    ifCreateEntry.setStatus("current")
_IfCreateIfIndex_Type = InterfaceIndex
_IfCreateIfIndex_Object = MibTableColumn
ifCreateIfIndex = _IfCreateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 1),
    _IfCreateIfIndex_Type()
)
ifCreateIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCreateIfIndex.setStatus("current")


class _IfCreateIfType_Type(Integer32):
    """Custom type ifCreateIfType based on Integer32"""
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
              107)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 49),
          ("adsl", 94),
          ("aflane8023", 59),
          ("aflane8025", 60),
          ("arap", 88),
          ("arcnet", 35),
          ("arcnetPlus", 36),
          ("async", 84),
          ("atm", 37),
          ("atmDxi", 105),
          ("atmFuni", 106),
          ("atmLogical", 80),
          ("basicISDN", 20),
          ("bsc", 83),
          ("cctEmul", 61),
          ("channel", 70),
          ("cnr", 85),
          ("ddnX25", 4),
          ("dlsw", 74),
          ("ds0", 81),
          ("ds0Bundle", 82),
          ("ds1e1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("eplrs", 87),
          ("escon", 73),
          ("ethernet3Mbit", 26),
          ("ethernetCsmacd", 6),
          ("fastEther", 62),
          ("fastEtherFX", 69),
          ("fddi", 15),
          ("fibreChannel", 56),
          ("frameRelay", 32),
          ("frameRelayInterconnect", 58),
          ("frameRelayMPI", 92),
          ("frameRelayService", 44),
          ("g703at2mb", 67),
          ("g703at64k", 66),
          ("hdh1822", 3),
          ("hippi", 47),
          ("hippiInterface", 57),
          ("hostPad", 90),
          ("hssi", 46),
          ("hyperchannel", 14),
          ("ibm370parChan", 72),
          ("ieee80211", 71),
          ("ieee80212", 55),
          ("ipSwitch", 78),
          ("isdn", 63),
          ("isdns", 75),
          ("isdnu", 76),
          ("iso88022llc", 41),
          ("iso88023Csmacd", 7),
          ("iso88024TokenBus", 8),
          ("iso88025CRFPInt", 98),
          ("iso88025Dtr", 86),
          ("iso88025TokenRing", 9),
          ("iso88026Man", 10),
          ("lapb", 16),
          ("lapd", 77),
          ("localTalk", 42),
          ("miox25", 38),
          ("modem", 48),
          ("myrinet", 99),
          ("nsip", 27),
          ("otherIfType", 1),
          ("para", 34),
          ("ppp", 23),
          ("pppMultilinkBundle", 107),
          ("primaryISDN", 21),
          ("propCnls", 89),
          ("propMultiplexor", 54),
          ("propPointToPointSerial", 22),
          ("propVirtual", 53),
          ("proteon10Mbit", 12),
          ("proteon80Mbit", 13),
          ("qllc", 68),
          ("radsl", 95),
          ("regular1822", 2),
          ("rfc877x25", 5),
          ("rs232", 33),
          ("rsrb", 79),
          ("sdlc", 17),
          ("sdsl", 96),
          ("sip", 31),
          ("slip", 28),
          ("smdsDxi", 43),
          ("smdsIcip", 52),
          ("softwareLoopback", 24),
          ("sonet", 39),
          ("sonetPath", 50),
          ("sonetVT", 51),
          ("starLan", 11),
          ("termPad", 91),
          ("ultra", 29),
          ("v11", 64),
          ("v35", 45),
          ("v36", 65),
          ("vdsl", 97),
          ("voiceEM", 100),
          ("voiceEncap", 103),
          ("voiceFXO", 101),
          ("voiceFXS", 102),
          ("voiceOverIp", 104),
          ("x213", 93),
          ("x25ple", 40))
    )


_IfCreateIfType_Type.__name__ = "Integer32"
_IfCreateIfType_Object = MibTableColumn
ifCreateIfType = _IfCreateIfType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 2),
    _IfCreateIfType_Type()
)
ifCreateIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifCreateIfType.setStatus("current")
_IfCreateRowStatus_Type = RowStatus
_IfCreateRowStatus_Object = MibTableColumn
ifCreateRowStatus = _IfCreateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 3),
    _IfCreateRowStatus_Type()
)
ifCreateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifCreateRowStatus.setStatus("current")


class _IfCreateServiceStatus_Type(Integer32):
    """Custom type ifCreateServiceStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("underConfig", 1))
    )


_IfCreateServiceStatus_Type.__name__ = "Integer32"
_IfCreateServiceStatus_Object = MibTableColumn
ifCreateServiceStatus = _IfCreateServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 4),
    _IfCreateServiceStatus_Type()
)
ifCreateServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifCreateServiceStatus.setStatus("current")
_IfCreateName_Type = DisplayString
_IfCreateName_Object = MibTableColumn
ifCreateName = _IfCreateName_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 5),
    _IfCreateName_Type()
)
ifCreateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifCreateName.setStatus("current")


class _IfCreateIfTrapSupport_Type(Integer32):
    """Custom type ifCreateIfTrapSupport based on Integer32"""
    defaultValue = 1

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


_IfCreateIfTrapSupport_Type.__name__ = "Integer32"
_IfCreateIfTrapSupport_Object = MibTableColumn
ifCreateIfTrapSupport = _IfCreateIfTrapSupport_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 6),
    _IfCreateIfTrapSupport_Type()
)
ifCreateIfTrapSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifCreateIfTrapSupport.setStatus("current")
_IfCreateServiceId_Type = DisplayString
_IfCreateServiceId_Object = MibTableColumn
ifCreateServiceId = _IfCreateServiceId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 2, 1, 7),
    _IfCreateServiceId_Type()
)
ifCreateServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifCreateServiceId.setStatus("current")
_IfConvertToIfIndexTable_Object = MibTable
ifConvertToIfIndexTable = _IfConvertToIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 3)
)
if mibBuilder.loadTexts:
    ifConvertToIfIndexTable.setStatus("current")
_IfConvertToIfIndexEntry_Object = MibTableRow
ifConvertToIfIndexEntry = _IfConvertToIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1)
)
ifConvertToIfIndexEntry.setIndexNames(
    (0, "Fore-Ifcreate-MIB", "ifConvertToIfIndexBoardId"),
    (0, "Fore-Ifcreate-MIB", "ifConvertToIfIndexNetmodId"),
    (0, "Fore-Ifcreate-MIB", "ifConvertToIfIndexPortId"),
    (0, "Fore-Ifcreate-MIB", "ifConvertToIfIndexChannelId"),
)
if mibBuilder.loadTexts:
    ifConvertToIfIndexEntry.setStatus("current")
_IfConvertToIfIndexBoardId_Type = Integer32
_IfConvertToIfIndexBoardId_Object = MibTableColumn
ifConvertToIfIndexBoardId = _IfConvertToIfIndexBoardId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1, 1),
    _IfConvertToIfIndexBoardId_Type()
)
ifConvertToIfIndexBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConvertToIfIndexBoardId.setStatus("current")
_IfConvertToIfIndexNetmodId_Type = Integer32
_IfConvertToIfIndexNetmodId_Object = MibTableColumn
ifConvertToIfIndexNetmodId = _IfConvertToIfIndexNetmodId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1, 2),
    _IfConvertToIfIndexNetmodId_Type()
)
ifConvertToIfIndexNetmodId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConvertToIfIndexNetmodId.setStatus("current")
_IfConvertToIfIndexPortId_Type = Integer32
_IfConvertToIfIndexPortId_Object = MibTableColumn
ifConvertToIfIndexPortId = _IfConvertToIfIndexPortId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1, 3),
    _IfConvertToIfIndexPortId_Type()
)
ifConvertToIfIndexPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConvertToIfIndexPortId.setStatus("current")
_IfConvertToIfIndexChannelId_Type = Integer32
_IfConvertToIfIndexChannelId_Object = MibTableColumn
ifConvertToIfIndexChannelId = _IfConvertToIfIndexChannelId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1, 4),
    _IfConvertToIfIndexChannelId_Type()
)
ifConvertToIfIndexChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConvertToIfIndexChannelId.setStatus("current")
_IfConvertToIfIndexIfIndex_Type = InterfaceIndex
_IfConvertToIfIndexIfIndex_Object = MibTableColumn
ifConvertToIfIndexIfIndex = _IfConvertToIfIndexIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 3, 1, 5),
    _IfConvertToIfIndexIfIndex_Type()
)
ifConvertToIfIndexIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConvertToIfIndexIfIndex.setStatus("current")
_IfConvertFmIfIndexTable_Object = MibTable
ifConvertFmIfIndexTable = _IfConvertFmIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 4)
)
if mibBuilder.loadTexts:
    ifConvertFmIfIndexTable.setStatus("current")
_IfConvertFmIfIndexEntry_Object = MibTableRow
ifConvertFmIfIndexEntry = _IfConvertFmIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1)
)
ifConvertFmIfIndexEntry.setIndexNames(
    (0, "Fore-Ifcreate-MIB", "ifConvertFmIfIndexIfIndex"),
)
if mibBuilder.loadTexts:
    ifConvertFmIfIndexEntry.setStatus("current")
_IfConvertFmIfIndexIfIndex_Type = InterfaceIndex
_IfConvertFmIfIndexIfIndex_Object = MibTableColumn
ifConvertFmIfIndexIfIndex = _IfConvertFmIfIndexIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1, 1),
    _IfConvertFmIfIndexIfIndex_Type()
)
ifConvertFmIfIndexIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConvertFmIfIndexIfIndex.setStatus("current")
_IfConvertFmIfIndexBoardId_Type = Integer32
_IfConvertFmIfIndexBoardId_Object = MibTableColumn
ifConvertFmIfIndexBoardId = _IfConvertFmIfIndexBoardId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1, 2),
    _IfConvertFmIfIndexBoardId_Type()
)
ifConvertFmIfIndexBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConvertFmIfIndexBoardId.setStatus("current")
_IfConvertFmIfIndexNetmodId_Type = Integer32
_IfConvertFmIfIndexNetmodId_Object = MibTableColumn
ifConvertFmIfIndexNetmodId = _IfConvertFmIfIndexNetmodId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1, 3),
    _IfConvertFmIfIndexNetmodId_Type()
)
ifConvertFmIfIndexNetmodId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConvertFmIfIndexNetmodId.setStatus("current")
_IfConvertFmIfIndexPortId_Type = Integer32
_IfConvertFmIfIndexPortId_Object = MibTableColumn
ifConvertFmIfIndexPortId = _IfConvertFmIfIndexPortId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1, 4),
    _IfConvertFmIfIndexPortId_Type()
)
ifConvertFmIfIndexPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConvertFmIfIndexPortId.setStatus("current")
_IfConvertFmIfIndexChannelId_Type = Integer32
_IfConvertFmIfIndexChannelId_Object = MibTableColumn
ifConvertFmIfIndexChannelId = _IfConvertFmIfIndexChannelId_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 17, 4, 1, 5),
    _IfConvertFmIfIndexChannelId_Type()
)
ifConvertFmIfIndexChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConvertFmIfIndexChannelId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Ifcreate-MIB",
    **{"ifReserveNextIndex": ifReserveNextIndex,
       "ifCreateTable": ifCreateTable,
       "ifCreateEntry": ifCreateEntry,
       "ifCreateIfIndex": ifCreateIfIndex,
       "ifCreateIfType": ifCreateIfType,
       "ifCreateRowStatus": ifCreateRowStatus,
       "ifCreateServiceStatus": ifCreateServiceStatus,
       "ifCreateName": ifCreateName,
       "ifCreateIfTrapSupport": ifCreateIfTrapSupport,
       "ifCreateServiceId": ifCreateServiceId,
       "ifConvertToIfIndexTable": ifConvertToIfIndexTable,
       "ifConvertToIfIndexEntry": ifConvertToIfIndexEntry,
       "ifConvertToIfIndexBoardId": ifConvertToIfIndexBoardId,
       "ifConvertToIfIndexNetmodId": ifConvertToIfIndexNetmodId,
       "ifConvertToIfIndexPortId": ifConvertToIfIndexPortId,
       "ifConvertToIfIndexChannelId": ifConvertToIfIndexChannelId,
       "ifConvertToIfIndexIfIndex": ifConvertToIfIndexIfIndex,
       "ifConvertFmIfIndexTable": ifConvertFmIfIndexTable,
       "ifConvertFmIfIndexEntry": ifConvertFmIfIndexEntry,
       "ifConvertFmIfIndexIfIndex": ifConvertFmIfIndexIfIndex,
       "ifConvertFmIfIndexBoardId": ifConvertFmIfIndexBoardId,
       "ifConvertFmIfIndexNetmodId": ifConvertFmIfIndexNetmodId,
       "ifConvertFmIfIndexPortId": ifConvertFmIfIndexPortId,
       "ifConvertFmIfIndexChannelId": ifConvertFmIfIndexChannelId,
       "foreIfcreateMIB": foreIfcreateMIB}
)
