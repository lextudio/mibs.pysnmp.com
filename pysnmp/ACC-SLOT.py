# SNMP MIB module (ACC-SLOT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-SLOT
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:58 2024
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

(DisplayString,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "accBRG")

(accMemBlkEntInUse,
 accMemBlkEntTotal,
 accMemEMEStatus,
 accMemOptimiserFeature,
 accMemOptimiserMemory,
 accMemOptimiserPref,
 accMemOptimiserStatus,
 accTrapLogSeqNum,
 accTrapLogSeverityType) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accMemBlkEntInUse",
    "accMemBlkEntTotal",
    "accMemEMEStatus",
    "accMemOptimiserFeature",
    "accMemOptimiserMemory",
    "accMemOptimiserPref",
    "accMemOptimiserStatus",
    "accTrapLogSeqNum",
    "accTrapLogSeverityType")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tcpConnRemAddress,) = mibBuilder.importSymbols(
    "TCP-MIB",
    "tcpConnRemAddress")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccSlot_ObjectIdentity = ObjectIdentity
accSlot = _AccSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5)
)
_AccSlotTable_Object = MibTable
accSlotTable = _AccSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    accSlotTable.setStatus("mandatory")
_AccSlotEntry_Object = MibTableRow
accSlotEntry = _AccSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1)
)
accSlotEntry.setIndexNames(
    (0, "ACC-SLOT", "ifIndex"),
)
if mibBuilder.loadTexts:
    accSlotEntry.setStatus("mandatory")
_AccSlotInPkts_Type = Counter32
_AccSlotInPkts_Object = MibTableColumn
accSlotInPkts = _AccSlotInPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 11),
    _AccSlotInPkts_Type()
)
accSlotInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotInPkts.setStatus("mandatory")
_AccSlotOutPkts_Type = Counter32
_AccSlotOutPkts_Object = MibTableColumn
accSlotOutPkts = _AccSlotOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 17),
    _AccSlotOutPkts_Type()
)
accSlotOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotOutPkts.setStatus("mandatory")
_AccSlotNumChanges_Type = Counter32
_AccSlotNumChanges_Object = MibTableColumn
accSlotNumChanges = _AccSlotNumChanges_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 21),
    _AccSlotNumChanges_Type()
)
accSlotNumChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotNumChanges.setStatus("mandatory")


class _AccSlotProtocol_Type(Integer32):
    """Custom type accSlotProtocol based on Integer32"""
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
        *(("dial", 10),
          ("enet", 1),
          ("fddi", 9),
          ("ffr", 4),
          ("lapb", 3),
          ("multilink", 11),
          ("other", 5),
          ("ppp", 8),
          ("smds", 7),
          ("token-ring", 6),
          ("x25", 2))
    )


_AccSlotProtocol_Type.__name__ = "Integer32"
_AccSlotProtocol_Object = MibTableColumn
accSlotProtocol = _AccSlotProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 22),
    _AccSlotProtocol_Type()
)
accSlotProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotProtocol.setStatus("mandatory")


class _AccSlotClockMode_Type(Integer32):
    """Custom type accSlotClockMode based on Integer32"""
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
        *(("ext1", 2),
          ("ext2", 4),
          ("int", 5),
          ("pp", 3),
          ("slave", 6),
          ("unknown", 1))
    )


_AccSlotClockMode_Type.__name__ = "Integer32"
_AccSlotClockMode_Object = MibTableColumn
accSlotClockMode = _AccSlotClockMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 23),
    _AccSlotClockMode_Type()
)
accSlotClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotClockMode.setStatus("mandatory")


class _AccSlotQueueMode_Type(Integer32):
    """Custom type accSlotQueueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("express", 1),
          ("precedence", 2))
    )


_AccSlotQueueMode_Type.__name__ = "Integer32"
_AccSlotQueueMode_Object = MibTableColumn
accSlotQueueMode = _AccSlotQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 24),
    _AccSlotQueueMode_Type()
)
accSlotQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotQueueMode.setStatus("mandatory")


class _AccSlotDialProcedure_Type(Integer32):
    """Custom type accSlotDialProcedure based on Integer32"""
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
        *(("direct", 2),
          ("dtr", 4),
          ("hayes", 7),
          ("isdn", 5),
          ("lan", 1),
          ("tdm", 8),
          ("v25", 6),
          ("x21", 3))
    )


_AccSlotDialProcedure_Type.__name__ = "Integer32"
_AccSlotDialProcedure_Object = MibTableColumn
accSlotDialProcedure = _AccSlotDialProcedure_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 25),
    _AccSlotDialProcedure_Type()
)
accSlotDialProcedure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotDialProcedure.setStatus("mandatory")


class _AccSlotResyncMode_Type(Integer32):
    """Custom type accSlotResyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccSlotResyncMode_Type.__name__ = "Integer32"
_AccSlotResyncMode_Object = MibTableColumn
accSlotResyncMode = _AccSlotResyncMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 26),
    _AccSlotResyncMode_Type()
)
accSlotResyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotResyncMode.setStatus("mandatory")


class _AccSlotCompressMode_Type(Integer32):
    """Custom type accSlotCompressMode based on Integer32"""
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


_AccSlotCompressMode_Type.__name__ = "Integer32"
_AccSlotCompressMode_Object = MibTableColumn
accSlotCompressMode = _AccSlotCompressMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 27),
    _AccSlotCompressMode_Type()
)
accSlotCompressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotCompressMode.setStatus("mandatory")
_AccSlotCompressV42bisP1_Type = Integer32
_AccSlotCompressV42bisP1_Object = MibTableColumn
accSlotCompressV42bisP1 = _AccSlotCompressV42bisP1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 29),
    _AccSlotCompressV42bisP1_Type()
)
accSlotCompressV42bisP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotCompressV42bisP1.setStatus("mandatory")
_AccSlotCompressV42bisP2_Type = Integer32
_AccSlotCompressV42bisP2_Object = MibTableColumn
accSlotCompressV42bisP2 = _AccSlotCompressV42bisP2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 30),
    _AccSlotCompressV42bisP2_Type()
)
accSlotCompressV42bisP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotCompressV42bisP2.setStatus("mandatory")


class _AccSlotCompressDcs221P1_Type(Integer32):
    """Custom type accSlotCompressDcs221P1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("medium", 3),
          ("none", 0),
          ("normal", 2),
          ("slow", 4))
    )


_AccSlotCompressDcs221P1_Type.__name__ = "Integer32"
_AccSlotCompressDcs221P1_Object = MibTableColumn
accSlotCompressDcs221P1 = _AccSlotCompressDcs221P1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 31),
    _AccSlotCompressDcs221P1_Type()
)
accSlotCompressDcs221P1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotCompressDcs221P1.setStatus("mandatory")


class _AccSlotSevereCongPct_Type(Integer32):
    """Custom type accSlotSevereCongPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AccSlotSevereCongPct_Type.__name__ = "Integer32"
_AccSlotSevereCongPct_Object = MibTableColumn
accSlotSevereCongPct = _AccSlotSevereCongPct_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 32),
    _AccSlotSevereCongPct_Type()
)
accSlotSevereCongPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotSevereCongPct.setStatus("mandatory")
_AccSlotDialAddress_Type = DisplayString
_AccSlotDialAddress_Object = MibTableColumn
accSlotDialAddress = _AccSlotDialAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 33),
    _AccSlotDialAddress_Type()
)
accSlotDialAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotDialAddress.setStatus("mandatory")


class _AccSlotCompressRevision_Type(Integer32):
    """Custom type accSlotCompressRevision based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("new", 2),
          ("old", 1))
    )


_AccSlotCompressRevision_Type.__name__ = "Integer32"
_AccSlotCompressRevision_Object = MibTableColumn
accSlotCompressRevision = _AccSlotCompressRevision_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 34),
    _AccSlotCompressRevision_Type()
)
accSlotCompressRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotCompressRevision.setStatus("mandatory")


class _AccSlotCompressMaxStreams_Type(Integer32):
    """Custom type accSlotCompressMaxStreams based on Integer32"""
    defaultValue = 1


_AccSlotCompressMaxStreams_Object = MibTableColumn
accSlotCompressMaxStreams = _AccSlotCompressMaxStreams_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 35),
    _AccSlotCompressMaxStreams_Type()
)
accSlotCompressMaxStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotCompressMaxStreams.setStatus("mandatory")
_AccSlotCompressMessageLevel_Type = Integer32
_AccSlotCompressMessageLevel_Object = MibTableColumn
accSlotCompressMessageLevel = _AccSlotCompressMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 36),
    _AccSlotCompressMessageLevel_Type()
)
accSlotCompressMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotCompressMessageLevel.setStatus("mandatory")


class _AccSlotIfType_Type(Integer32):
    """Custom type accSlotIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              30,
              31,
              32,
              33,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
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
              61,
              62,
              63,
              64,
              65)
        )
    )
    namedValues = NamedValues(
        *(("dWAN-port", 11),
          ("dec-100baseTXfull-ethernet", 62),
          ("dec-100baseTXhalf-ethernet", 63),
          ("dec-10baseTfull-ethernet", 64),
          ("dec-10baseThalf-ethernet", 65),
          ("hWAN-Port", 8),
          ("hWAN-port-RS-232", 40),
          ("hWAN-port-RS-422", 44),
          ("hWAN-port-V-35", 42),
          ("hWAN-port-X-21", 43),
          ("hWAN-port-other", 41),
          ("icp-isdn-B-channel", 9),
          ("icp-isdn-D-channel", 10),
          ("intel-ethernet", 4),
          ("isdn-D-channel", 7),
          ("isdn-S", 16),
          ("isdn-U", 17),
          ("lance-10base2-Ethernet", 22),
          ("lance-10base5-Ethernet", 20),
          ("lance-10baseT-Ethernet", 21),
          ("lance-empty-Ethernet", 23),
          ("lance-ethernet", 1),
          ("not-Installed", 19),
          ("other", 18),
          ("pri-e1", 45),
          ("pri-t1", 46),
          ("rs-232", 14),
          ("rs-232-dte", 58),
          ("rs-422", 13),
          ("sWAN-port", 2),
          ("serial", 5),
          ("sonic-10base2-Ethernet", 31),
          ("sonic-10base5-Ethernet", 33),
          ("sonic-10baseT-Ethernet", 32),
          ("sonic-empty-Ethernet", 30),
          ("sonic-ethernet", 6),
          ("token-Ring", 3),
          ("unpopulated", 0),
          ("uwan-faulty-cable", 50),
          ("uwan-rs-232-dce", 53),
          ("uwan-rs-232-dte", 56),
          ("uwan-unconnected", 57),
          ("uwan-v-35-dce", 52),
          ("uwan-v-35-dte", 55),
          ("uwan-x-21-dce", 51),
          ("uwan-x-21-dte", 54),
          ("v-34-digital-modem", 61),
          ("v-35", 15),
          ("volatile", 59),
          ("x-21", 12))
    )


_AccSlotIfType_Type.__name__ = "Integer32"
_AccSlotIfType_Object = MibTableColumn
accSlotIfType = _AccSlotIfType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 37),
    _AccSlotIfType_Type()
)
accSlotIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotIfType.setStatus("mandatory")


class _AccSlotE1FrameMode_Type(Integer32):
    """Custom type accSlotE1FrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              30,
              31,
              32,
              33,
              40,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("dWAN-port", 11),
          ("hWAN-Port", 8),
          ("hWAN-port-RS-232", 40),
          ("hWAN-port-RS-422", 44),
          ("hWAN-port-V-35", 42),
          ("hWAN-port-X-21", 43),
          ("hWAN-port-other", 41),
          ("icp-isdn-B-channel", 9),
          ("icp-isdn-D-channel", 10),
          ("intel-ethernet", 4),
          ("isdn-D-channel", 7),
          ("isdn-S", 16),
          ("isdn-U", 17),
          ("lance-10base2-Ethernet", 22),
          ("lance-10base5-Ethernet", 20),
          ("lance-10baseT-Ethernet", 21),
          ("lance-empty-Ethernet", 23),
          ("lance-ethernet", 1),
          ("not-Installed", 19),
          ("other", 18),
          ("rs-232", 14),
          ("rs-422", 13),
          ("sWAN-port", 2),
          ("serial", 5),
          ("sonic-10base2-Ethernet", 31),
          ("sonic-10base5-Ethernet", 33),
          ("sonic-10baseT-Ethernet", 32),
          ("sonic-empty-Ethernet", 30),
          ("sonic-ethernet", 6),
          ("token-Ring", 3),
          ("unpopulated", 0),
          ("v-35", 15),
          ("x-21", 12))
    )


_AccSlotE1FrameMode_Type.__name__ = "Integer32"
_AccSlotE1FrameMode_Object = MibTableColumn
accSlotE1FrameMode = _AccSlotE1FrameMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 38),
    _AccSlotE1FrameMode_Type()
)
accSlotE1FrameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotE1FrameMode.setStatus("mandatory")
_AccSlotLastChangeY2K_Type = OctetString
_AccSlotLastChangeY2K_Object = MibTableColumn
accSlotLastChangeY2K = _AccSlotLastChangeY2K_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 39),
    _AccSlotLastChangeY2K_Type()
)
accSlotLastChangeY2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotLastChangeY2K.setStatus("mandatory")
_AccCardSlotTable_Object = MibTable
accCardSlotTable = _AccCardSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    accCardSlotTable.setStatus("mandatory")
_AccCardSlotEntry_Object = MibTableRow
accCardSlotEntry = _AccCardSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 3, 1)
)
accCardSlotEntry.setIndexNames(
    (0, "ACC-SLOT", "accCardSlotNum"),
)
if mibBuilder.loadTexts:
    accCardSlotEntry.setStatus("mandatory")
_AccCardSlotNum_Type = Integer32
_AccCardSlotNum_Object = MibTableColumn
accCardSlotNum = _AccCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 3, 1, 1),
    _AccCardSlotNum_Type()
)
accCardSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardSlotNum.setStatus("mandatory")


class _AccCardSlotType_Type(Integer32):
    """Custom type accCardSlotType based on Integer32"""
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
        *(("carrier-card", 2),
          ("control-card", 3),
          ("e1-t1-card", 4),
          ("modem-card", 5),
          ("unknown-card", 1))
    )


_AccCardSlotType_Type.__name__ = "Integer32"
_AccCardSlotType_Object = MibTableColumn
accCardSlotType = _AccCardSlotType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 3, 1, 2),
    _AccCardSlotType_Type()
)
accCardSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardSlotType.setStatus("mandatory")
_AccCardSlotRevNum_Type = DisplayString
_AccCardSlotRevNum_Object = MibTableColumn
accCardSlotRevNum = _AccCardSlotRevNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 3, 1, 3),
    _AccCardSlotRevNum_Type()
)
accCardSlotRevNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardSlotRevNum.setStatus("mandatory")
_AccCardSlotSerNum_Type = DisplayString
_AccCardSlotSerNum_Object = MibTableColumn
accCardSlotSerNum = _AccCardSlotSerNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 3, 1, 4),
    _AccCardSlotSerNum_Type()
)
accCardSlotSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardSlotSerNum.setStatus("mandatory")
_AccCardSlotPortCnf_Type = DisplayString
_AccCardSlotPortCnf_Object = MibTableColumn
accCardSlotPortCnf = _AccCardSlotPortCnf_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 3, 1, 5),
    _AccCardSlotPortCnf_Type()
)
accCardSlotPortCnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardSlotPortCnf.setStatus("mandatory")


class _AccCardSlotAdminState_Type(Integer32):
    """Custom type accCardSlotAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offfine", 2),
          ("online", 1))
    )


_AccCardSlotAdminState_Type.__name__ = "Integer32"
_AccCardSlotAdminState_Object = MibTableColumn
accCardSlotAdminState = _AccCardSlotAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 3, 1, 6),
    _AccCardSlotAdminState_Type()
)
accCardSlotAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCardSlotAdminState.setStatus("mandatory")


class _AccCardSlotOperState_Type(Integer32):
    """Custom type accCardSlotOperState based on Integer32"""
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
        *(("config-error", 6),
          ("deactivated", 8),
          ("downloading", 4),
          ("file-sync-error", 5),
          ("offline", 2),
          ("ready", 1),
          ("removed", 3),
          ("standby", 9),
          ("test", 7))
    )


_AccCardSlotOperState_Type.__name__ = "Integer32"
_AccCardSlotOperState_Object = MibTableColumn
accCardSlotOperState = _AccCardSlotOperState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 3, 1, 7),
    _AccCardSlotOperState_Type()
)
accCardSlotOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCardSlotOperState.setStatus("mandatory")
_AccCardSlotIndex_Type = Integer32
_AccCardSlotIndex_Object = MibTableColumn
accCardSlotIndex = _AccCardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 3, 1, 8),
    _AccCardSlotIndex_Type()
)
accCardSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardSlotIndex.setStatus("mandatory")


class _AccCardSlotNum11Slot_Type(Integer32):
    """Custom type accCardSlotNum11Slot based on Integer32"""
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
        *(("j0", 1),
          ("j1", 2),
          ("j2", 3),
          ("j3", 4),
          ("j4A", 5),
          ("j4B", 6),
          ("j5", 7),
          ("j6", 8),
          ("j7", 9),
          ("j8", 10),
          ("j9", 11))
    )


_AccCardSlotNum11Slot_Type.__name__ = "Integer32"
_AccCardSlotNum11Slot_Object = MibTableColumn
accCardSlotNum11Slot = _AccCardSlotNum11Slot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 3, 1, 9),
    _AccCardSlotNum11Slot_Type()
)
accCardSlotNum11Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardSlotNum11Slot.setStatus("mandatory")
_AccCardInterfaceTable_Object = MibTable
accCardInterfaceTable = _AccCardInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    accCardInterfaceTable.setStatus("mandatory")
_AccCardInterfaceEntry_Object = MibTableRow
accCardInterfaceEntry = _AccCardInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 4, 1)
)
accCardInterfaceEntry.setIndexNames(
    (0, "ACC-SLOT", "accCardInterfaceSlotNum"),
    (0, "ACC-SLOT", "accCardInterfaceNum"),
)
if mibBuilder.loadTexts:
    accCardInterfaceEntry.setStatus("mandatory")
_AccCardInterfaceNum_Type = Integer32
_AccCardInterfaceNum_Object = MibTableColumn
accCardInterfaceNum = _AccCardInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 4, 1, 1),
    _AccCardInterfaceNum_Type()
)
accCardInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardInterfaceNum.setStatus("mandatory")


class _AccCardInterfaceType_Type(Integer32):
    """Custom type accCardInterfaceType based on Integer32"""
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
        *(("bri-s", 7),
          ("bri-u", 6),
          ("digital-modem", 8),
          ("ethernet", 1),
          ("generic-wan", 2),
          ("isdn-capable-e1", 4),
          ("isdn-capable-t1", 5),
          ("tokenring", 3))
    )


_AccCardInterfaceType_Type.__name__ = "Integer32"
_AccCardInterfaceType_Object = MibTableColumn
accCardInterfaceType = _AccCardInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 4, 1, 2),
    _AccCardInterfaceType_Type()
)
accCardInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardInterfaceType.setStatus("mandatory")
_AccCardInterfaceSlotNum_Type = Integer32
_AccCardInterfaceSlotNum_Object = MibTableColumn
accCardInterfaceSlotNum = _AccCardInterfaceSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 4, 1, 3),
    _AccCardInterfaceSlotNum_Type()
)
accCardInterfaceSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardInterfaceSlotNum.setStatus("mandatory")
_AccCardInterfaceIndex_Type = Integer32
_AccCardInterfaceIndex_Object = MibTableColumn
accCardInterfaceIndex = _AccCardInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 4, 1, 4),
    _AccCardInterfaceIndex_Type()
)
accCardInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardInterfaceIndex.setStatus("mandatory")
_AccCardCircuitTable_Object = MibTable
accCardCircuitTable = _AccCardCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    accCardCircuitTable.setStatus("mandatory")
_AccCardCircuitEntry_Object = MibTableRow
accCardCircuitEntry = _AccCardCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 5, 1)
)
accCardCircuitEntry.setIndexNames(
    (0, "ACC-SLOT", "accCardCircuitSlotNum"),
    (0, "ACC-SLOT", "accCardCircuitInterfaceNum"),
    (0, "ACC-SLOT", "accCardCircuitNum"),
)
if mibBuilder.loadTexts:
    accCardCircuitEntry.setStatus("mandatory")
_AccCardCircuitNum_Type = Integer32
_AccCardCircuitNum_Object = MibTableColumn
accCardCircuitNum = _AccCardCircuitNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 5, 1, 1),
    _AccCardCircuitNum_Type()
)
accCardCircuitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardCircuitNum.setStatus("mandatory")
_AccCardCircuitSlotNum_Type = Integer32
_AccCardCircuitSlotNum_Object = MibTableColumn
accCardCircuitSlotNum = _AccCardCircuitSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 5, 1, 2),
    _AccCardCircuitSlotNum_Type()
)
accCardCircuitSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardCircuitSlotNum.setStatus("mandatory")
_AccCardCircuitInterfaceNum_Type = Integer32
_AccCardCircuitInterfaceNum_Object = MibTableColumn
accCardCircuitInterfaceNum = _AccCardCircuitInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 5, 1, 3),
    _AccCardCircuitInterfaceNum_Type()
)
accCardCircuitInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardCircuitInterfaceNum.setStatus("mandatory")
_AccCardCircuitIndex_Type = Integer32
_AccCardCircuitIndex_Object = MibTableColumn
accCardCircuitIndex = _AccCardCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 5, 1, 4),
    _AccCardCircuitIndex_Type()
)
accCardCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardCircuitIndex.setStatus("mandatory")
_AccCardSlotTraps_ObjectIdentity = ObjectIdentity
accCardSlotTraps = _AccCardSlotTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6)
)
_AccCardSlotTrapMsg_Type = DisplayString
_AccCardSlotTrapMsg_Object = MibScalar
accCardSlotTrapMsg = _AccCardSlotTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 1),
    _AccCardSlotTrapMsg_Type()
)
accCardSlotTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCardSlotTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accRmReqResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 1)
)
accRmReqResetTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accMemEMEStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmReqResetTrap.setStatus(
        ""
    )

accRmFeatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 2)
)
accRmFeatureTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accMemOptimiserMemory"),
        ("ACC-SYSTEM", "accMemOptimiserPref"),
        ("ACC-SYSTEM", "accMemOptimiserFeature"),
        ("ACC-SYSTEM", "accMemOptimiserStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmFeatureTrap.setStatus(
        ""
    )

accRmCardRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 3)
)
accRmCardRemovedTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SLOT", "accCardSlotAdminState"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmCardRemovedTrap.setStatus(
        ""
    )

accRmActvComplTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 4)
)
accRmActvComplTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SLOT", "accCardSlotAdminState"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmActvComplTrap.setStatus(
        ""
    )

accRmActvStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 5)
)
accRmActvStartTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SLOT", "accCardSlotAdminState"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmActvStartTrap.setStatus(
        ""
    )

accRmActvFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 6)
)
accRmActvFailTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SLOT", "accCardSlotAdminState"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmActvFailTrap.setStatus(
        ""
    )

accRmDeActvStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 7)
)
accRmDeActvStartTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SLOT", "accCardSlotAdminState"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmDeActvStartTrap.setStatus(
        ""
    )

accRmDeActvComplTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 8)
)
accRmDeActvComplTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SLOT", "accCardSlotAdminState"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmDeActvComplTrap.setStatus(
        ""
    )

accRmCardRemvdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 9)
)
accRmCardRemvdTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SLOT", "accCardSlotAdminState"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmCardRemvdTrap.setStatus(
        ""
    )

accRmInvStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 10)
)
accRmInvStateTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SLOT", "accCardSlotAdminState"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmInvStateTrap.setStatus(
        ""
    )

accRmFaultHndlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 11)
)
accRmFaultHndlTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SLOT", "accCardSlotAdminState"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmFaultHndlTrap.setStatus(
        ""
    )

accRmFaultIndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 12)
)
accRmFaultIndTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SLOT", "accCardSlotAdminState"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmFaultIndTrap.setStatus(
        ""
    )

accRmDataCallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 13)
)
accRmDataCallTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmDataCallTrap.setStatus(
        ""
    )

accRmDataEnableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 14)
)
accRmDataEnableTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmDataEnableTrap.setStatus(
        ""
    )

accRmDataCallAccptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 15)
)
accRmDataCallAccptTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmDataCallAccptTrap.setStatus(
        ""
    )

accRmDataSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 16)
)
accRmDataSwitchTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmDataSwitchTrap.setStatus(
        ""
    )

accRmFrmWareLoadAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 17)
)
accRmFrmWareLoadAbortTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmFrmWareLoadAbortTrap.setStatus(
        ""
    )

accRmBfrAllocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 18)
)
accRmBfrAllocTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmBfrAllocTrap.setStatus(
        ""
    )

accRmLoadAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 19)
)
accRmLoadAbortTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmLoadAbortTrap.setStatus(
        ""
    )

accRmFrmwrCompatiblTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 20)
)
accRmFrmwrCompatiblTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmFrmwrCompatiblTrap.setStatus(
        ""
    )

accRmLoadTrap5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 21)
)
accRmLoadTrap5.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmLoadTrap5.setStatus(
        ""
    )

accRmSwUpGradeMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 22)
)
accRmSwUpGradeMsgTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmSwUpGradeMsgTrap.setStatus(
        ""
    )

accRmInSuffRAMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 23)
)
accRmInSuffRAMTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmInSuffRAMTrap.setStatus(
        ""
    )

accRmPwrSplyMalfnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 24)
)
accRmPwrSplyMalfnTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmPwrSplyMalfnTrap.setStatus(
        ""
    )

accRmPwrSplyStatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 25)
)
accRmPwrSplyStatTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmPwrSplyStatTrap.setStatus(
        ""
    )

accRmFanStatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 26)
)
accRmFanStatTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmFanStatTrap.setStatus(
        ""
    )

accRmDcStatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 27)
)
accRmDcStatTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmDcStatTrap.setStatus(
        ""
    )

accRmAcStatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 28)
)
accRmAcStatTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmAcStatTrap.setStatus(
        ""
    )

accRmPwr1PresTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 29)
)
accRmPwr1PresTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmPwr1PresTrap.setStatus(
        ""
    )

accRmPwrFan1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 30)
)
accRmPwrFan1Trap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmPwrFan1Trap.setStatus(
        ""
    )

accRmPwrDc1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 31)
)
accRmPwrDc1Trap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmPwrDc1Trap.setStatus(
        ""
    )

accRmPwrAc1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 32)
)
accRmPwrAc1Trap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmPwrAc1Trap.setStatus(
        ""
    )

accRmEalm2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 33)
)
accRmEalm2Trap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmEalm2Trap.setStatus(
        ""
    )

accRmEalm1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 34)
)
accRmEalm1Trap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmEalm1Trap.setStatus(
        ""
    )

accRmChasFanPresTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 35)
)
accRmChasFanPresTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmChasFanPresTrap.setStatus(
        ""
    )

accRmChasFanIndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 36)
)
accRmChasFanIndTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmChasFanIndTrap.setStatus(
        ""
    )

accRmLowMemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 37)
)
accRmLowMemTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accMemBlkEntTotal"),
        ("ACC-SYSTEM", "accMemBlkEntInUse"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmLowMemTrap.setStatus(
        ""
    )

accRmLanDiagsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 38)
)
accRmLanDiagsTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmLanDiagsTrap.setStatus(
        ""
    )

accRmWanDiagsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 39)
)
accRmWanDiagsTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmWanDiagsTrap.setStatus(
        ""
    )

accRmCardDiagsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 40)
)
accRmCardDiagsTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SLOT", "accCardSlotNum"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmCardDiagsTrap.setStatus(
        ""
    )

accRmResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 41)
)
accRmResetTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accMemEMEStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmResetTrap.setStatus(
        ""
    )

accRmIdbTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 42)
)
accRmIdbTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmIdbTrap.setStatus(
        ""
    )

accRmLdngElemManTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 43)
)
accRmLdngElemManTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("TCP-MIB", "tcpConnRemAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmLdngElemManTrap.setStatus(
        ""
    )

accRmInterFileJavaManTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 44)
)
accRmInterFileJavaManTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("TCP-MIB", "tcpConnRemAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmInterFileJavaManTrap.setStatus(
        ""
    )

accRmBrowLdngSetupWizTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 45)
)
accRmBrowLdngSetupWizTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("TCP-MIB", "tcpConnRemAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmBrowLdngSetupWizTrap.setStatus(
        ""
    )

accRmConfWizLddTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 46)
)
accRmConfWizLddTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("TCP-MIB", "tcpConnRemAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmConfWizLddTrap.setStatus(
        ""
    )

accRmPriConfScrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 47)
)
accRmPriConfScrTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("TCP-MIB", "tcpConnRemAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmPriConfScrTrap.setStatus(
        ""
    )

accRmInstAccAppLddTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 6, 0, 48)
)
accRmInstAccAppLddTrap.setObjects(
      *(("ACC-SLOT", "accCardSlotTrapMsg"),
        ("TCP-MIB", "tcpConnRemAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRmInstAccAppLddTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-SLOT",
    **{"accSlot": accSlot,
       "accSlotTable": accSlotTable,
       "accSlotEntry": accSlotEntry,
       "accSlotInPkts": accSlotInPkts,
       "accSlotOutPkts": accSlotOutPkts,
       "accSlotNumChanges": accSlotNumChanges,
       "accSlotProtocol": accSlotProtocol,
       "accSlotClockMode": accSlotClockMode,
       "accSlotQueueMode": accSlotQueueMode,
       "accSlotDialProcedure": accSlotDialProcedure,
       "accSlotResyncMode": accSlotResyncMode,
       "accSlotCompressMode": accSlotCompressMode,
       "accSlotCompressV42bisP1": accSlotCompressV42bisP1,
       "accSlotCompressV42bisP2": accSlotCompressV42bisP2,
       "accSlotCompressDcs221P1": accSlotCompressDcs221P1,
       "accSlotSevereCongPct": accSlotSevereCongPct,
       "accSlotDialAddress": accSlotDialAddress,
       "accSlotCompressRevision": accSlotCompressRevision,
       "accSlotCompressMaxStreams": accSlotCompressMaxStreams,
       "accSlotCompressMessageLevel": accSlotCompressMessageLevel,
       "accSlotIfType": accSlotIfType,
       "accSlotE1FrameMode": accSlotE1FrameMode,
       "accSlotLastChangeY2K": accSlotLastChangeY2K,
       "accCardSlotTable": accCardSlotTable,
       "accCardSlotEntry": accCardSlotEntry,
       "accCardSlotNum": accCardSlotNum,
       "accCardSlotType": accCardSlotType,
       "accCardSlotRevNum": accCardSlotRevNum,
       "accCardSlotSerNum": accCardSlotSerNum,
       "accCardSlotPortCnf": accCardSlotPortCnf,
       "accCardSlotAdminState": accCardSlotAdminState,
       "accCardSlotOperState": accCardSlotOperState,
       "accCardSlotIndex": accCardSlotIndex,
       "accCardSlotNum11Slot": accCardSlotNum11Slot,
       "accCardInterfaceTable": accCardInterfaceTable,
       "accCardInterfaceEntry": accCardInterfaceEntry,
       "accCardInterfaceNum": accCardInterfaceNum,
       "accCardInterfaceType": accCardInterfaceType,
       "accCardInterfaceSlotNum": accCardInterfaceSlotNum,
       "accCardInterfaceIndex": accCardInterfaceIndex,
       "accCardCircuitTable": accCardCircuitTable,
       "accCardCircuitEntry": accCardCircuitEntry,
       "accCardCircuitNum": accCardCircuitNum,
       "accCardCircuitSlotNum": accCardCircuitSlotNum,
       "accCardCircuitInterfaceNum": accCardCircuitInterfaceNum,
       "accCardCircuitIndex": accCardCircuitIndex,
       "accCardSlotTraps": accCardSlotTraps,
       "accRmReqResetTrap": accRmReqResetTrap,
       "accRmFeatureTrap": accRmFeatureTrap,
       "accRmCardRemovedTrap": accRmCardRemovedTrap,
       "accRmActvComplTrap": accRmActvComplTrap,
       "accRmActvStartTrap": accRmActvStartTrap,
       "accRmActvFailTrap": accRmActvFailTrap,
       "accRmDeActvStartTrap": accRmDeActvStartTrap,
       "accRmDeActvComplTrap": accRmDeActvComplTrap,
       "accRmCardRemvdTrap": accRmCardRemvdTrap,
       "accRmInvStateTrap": accRmInvStateTrap,
       "accRmFaultHndlTrap": accRmFaultHndlTrap,
       "accRmFaultIndTrap": accRmFaultIndTrap,
       "accRmDataCallTrap": accRmDataCallTrap,
       "accRmDataEnableTrap": accRmDataEnableTrap,
       "accRmDataCallAccptTrap": accRmDataCallAccptTrap,
       "accRmDataSwitchTrap": accRmDataSwitchTrap,
       "accRmFrmWareLoadAbortTrap": accRmFrmWareLoadAbortTrap,
       "accRmBfrAllocTrap": accRmBfrAllocTrap,
       "accRmLoadAbortTrap": accRmLoadAbortTrap,
       "accRmFrmwrCompatiblTrap": accRmFrmwrCompatiblTrap,
       "accRmLoadTrap5": accRmLoadTrap5,
       "accRmSwUpGradeMsgTrap": accRmSwUpGradeMsgTrap,
       "accRmInSuffRAMTrap": accRmInSuffRAMTrap,
       "accRmPwrSplyMalfnTrap": accRmPwrSplyMalfnTrap,
       "accRmPwrSplyStatTrap": accRmPwrSplyStatTrap,
       "accRmFanStatTrap": accRmFanStatTrap,
       "accRmDcStatTrap": accRmDcStatTrap,
       "accRmAcStatTrap": accRmAcStatTrap,
       "accRmPwr1PresTrap": accRmPwr1PresTrap,
       "accRmPwrFan1Trap": accRmPwrFan1Trap,
       "accRmPwrDc1Trap": accRmPwrDc1Trap,
       "accRmPwrAc1Trap": accRmPwrAc1Trap,
       "accRmEalm2Trap": accRmEalm2Trap,
       "accRmEalm1Trap": accRmEalm1Trap,
       "accRmChasFanPresTrap": accRmChasFanPresTrap,
       "accRmChasFanIndTrap": accRmChasFanIndTrap,
       "accRmLowMemTrap": accRmLowMemTrap,
       "accRmLanDiagsTrap": accRmLanDiagsTrap,
       "accRmWanDiagsTrap": accRmWanDiagsTrap,
       "accRmCardDiagsTrap": accRmCardDiagsTrap,
       "accRmResetTrap": accRmResetTrap,
       "accRmIdbTrap": accRmIdbTrap,
       "accRmLdngElemManTrap": accRmLdngElemManTrap,
       "accRmInterFileJavaManTrap": accRmInterFileJavaManTrap,
       "accRmBrowLdngSetupWizTrap": accRmBrowLdngSetupWizTrap,
       "accRmConfWizLddTrap": accRmConfWizLddTrap,
       "accRmPriConfScrTrap": accRmPriConfScrTrap,
       "accRmInstAccAppLddTrap": accRmInstAccAppLddTrap,
       "accCardSlotTrapMsg": accCardSlotTrapMsg}
)
