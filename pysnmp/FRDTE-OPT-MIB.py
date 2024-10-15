# SNMP MIB module (FRDTE-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FRDTE-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:23 2024
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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Counter16(Integer32):
    """Custom type Counter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PCTFRDTEPortTable_Object = MibTable
cdx6500PCTFRDTEPortTable = _Cdx6500PCTFRDTEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cdx6500PCTFRDTEPortTable.setStatus("mandatory")
_Cdx6500PCTFRDTEPortEntry_Object = MibTableRow
cdx6500PCTFRDTEPortEntry = _Cdx6500PCTFRDTEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1)
)
cdx6500PCTFRDTEPortEntry.setIndexNames(
    (0, "FRDTE-OPT-MIB", "cdx6500frdtepCfgPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PCTFRDTEPortEntry.setStatus("mandatory")


class _Cdx6500frdtepCfgPortNum_Type(Integer32):
    """Custom type cdx6500frdtepCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500frdtepCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500frdtepCfgPortNum_Object = MibTableColumn
cdx6500frdtepCfgPortNum = _Cdx6500frdtepCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 1),
    _Cdx6500frdtepCfgPortNum_Type()
)
cdx6500frdtepCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepCfgPortNum.setStatus("mandatory")


class _Cdx6500frdtepConnectionType_Type(Integer32):
    """Custom type cdx6500frdtepConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              21,
              100)
        )
    )
    namedValues = NamedValues(
        *(("dtr", 2),
          ("nc", 100),
          ("simp", 1),
          ("simpb", 21))
    )


_Cdx6500frdtepConnectionType_Type.__name__ = "Integer32"
_Cdx6500frdtepConnectionType_Object = MibTableColumn
cdx6500frdtepConnectionType = _Cdx6500frdtepConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 2),
    _Cdx6500frdtepConnectionType_Type()
)
cdx6500frdtepConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepConnectionType.setStatus("mandatory")


class _Cdx6500frdtepClockSource_Type(Integer32):
    """Custom type cdx6500frdtepClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ext", 2),
          ("extint", 3),
          ("extlp", 4),
          ("int", 1),
          ("nc", 100))
    )


_Cdx6500frdtepClockSource_Type.__name__ = "Integer32"
_Cdx6500frdtepClockSource_Object = MibTableColumn
cdx6500frdtepClockSource = _Cdx6500frdtepClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 3),
    _Cdx6500frdtepClockSource_Type()
)
cdx6500frdtepClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepClockSource.setStatus("mandatory")


class _Cdx6500frdtepClockSpeed_Type(Integer32):
    """Custom type cdx6500frdtepClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 2048000),
    )


_Cdx6500frdtepClockSpeed_Type.__name__ = "Integer32"
_Cdx6500frdtepClockSpeed_Object = MibTableColumn
cdx6500frdtepClockSpeed = _Cdx6500frdtepClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 4),
    _Cdx6500frdtepClockSpeed_Type()
)
cdx6500frdtepClockSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepClockSpeed.setStatus("mandatory")
_Cdx6500frdtepMaxStations_Type = Integer32
_Cdx6500frdtepMaxStations_Object = MibTableColumn
cdx6500frdtepMaxStations = _Cdx6500frdtepMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 5),
    _Cdx6500frdtepMaxStations_Type()
)
cdx6500frdtepMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepMaxStations.setStatus("deprecated")


class _Cdx6500frdtepFrameSeqCounting_Type(Integer32):
    """Custom type cdx6500frdtepFrameSeqCounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("nc", 100),
          ("normal", 1))
    )


_Cdx6500frdtepFrameSeqCounting_Type.__name__ = "Integer32"
_Cdx6500frdtepFrameSeqCounting_Object = MibTableColumn
cdx6500frdtepFrameSeqCounting = _Cdx6500frdtepFrameSeqCounting_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 6),
    _Cdx6500frdtepFrameSeqCounting_Type()
)
cdx6500frdtepFrameSeqCounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepFrameSeqCounting.setStatus("mandatory")


class _Cdx6500frdtepPktSeqCounting_Type(Integer32):
    """Custom type cdx6500frdtepPktSeqCounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("nc", 100),
          ("normal", 1))
    )


_Cdx6500frdtepPktSeqCounting_Type.__name__ = "Integer32"
_Cdx6500frdtepPktSeqCounting_Object = MibTableColumn
cdx6500frdtepPktSeqCounting = _Cdx6500frdtepPktSeqCounting_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 7),
    _Cdx6500frdtepPktSeqCounting_Type()
)
cdx6500frdtepPktSeqCounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepPktSeqCounting.setStatus("mandatory")


class _Cdx6500frdtepCtrlProtocol_Type(Integer32):
    """Custom type cdx6500frdtepCtrlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 4),
          ("annexD", 1),
          ("auto", 5),
          ("lmi", 3),
          ("nc", 100),
          ("none", 2))
    )


_Cdx6500frdtepCtrlProtocol_Type.__name__ = "Integer32"
_Cdx6500frdtepCtrlProtocol_Object = MibTableColumn
cdx6500frdtepCtrlProtocol = _Cdx6500frdtepCtrlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 8),
    _Cdx6500frdtepCtrlProtocol_Type()
)
cdx6500frdtepCtrlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepCtrlProtocol.setStatus("mandatory")


class _Cdx6500frdtepT391_Type(Integer32):
    """Custom type cdx6500frdtepT391 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_Cdx6500frdtepT391_Type.__name__ = "Integer32"
_Cdx6500frdtepT391_Object = MibTableColumn
cdx6500frdtepT391 = _Cdx6500frdtepT391_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 9),
    _Cdx6500frdtepT391_Type()
)
cdx6500frdtepT391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepT391.setStatus("mandatory")


class _Cdx6500frdtepT392_Type(Integer32):
    """Custom type cdx6500frdtepT392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_Cdx6500frdtepT392_Type.__name__ = "Integer32"
_Cdx6500frdtepT392_Object = MibTableColumn
cdx6500frdtepT392 = _Cdx6500frdtepT392_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 10),
    _Cdx6500frdtepT392_Type()
)
cdx6500frdtepT392.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepT392.setStatus("mandatory")
_Cdx6500frdtepN391_Type = Integer32
_Cdx6500frdtepN391_Object = MibTableColumn
cdx6500frdtepN391 = _Cdx6500frdtepN391_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 12),
    _Cdx6500frdtepN391_Type()
)
cdx6500frdtepN391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepN391.setStatus("mandatory")
_Cdx6500frdtepN392_Type = Integer32
_Cdx6500frdtepN392_Object = MibTableColumn
cdx6500frdtepN392 = _Cdx6500frdtepN392_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 13),
    _Cdx6500frdtepN392_Type()
)
cdx6500frdtepN392.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepN392.setStatus("mandatory")
_Cdx6500frdtepN393_Type = Integer32
_Cdx6500frdtepN393_Object = MibTableColumn
cdx6500frdtepN393 = _Cdx6500frdtepN393_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 14),
    _Cdx6500frdtepN393_Type()
)
cdx6500frdtepN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepN393.setStatus("mandatory")


class _Cdx6500frdtepNT1_Type(Integer32):
    """Custom type cdx6500frdtepNT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_Cdx6500frdtepNT1_Type.__name__ = "Integer32"
_Cdx6500frdtepNT1_Object = MibTableColumn
cdx6500frdtepNT1 = _Cdx6500frdtepNT1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 15),
    _Cdx6500frdtepNT1_Type()
)
cdx6500frdtepNT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepNT1.setStatus("mandatory")


class _Cdx6500frdtepNT2_Type(Integer32):
    """Custom type cdx6500frdtepNT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_Cdx6500frdtepNT2_Type.__name__ = "Integer32"
_Cdx6500frdtepNT2_Object = MibTableColumn
cdx6500frdtepNT2 = _Cdx6500frdtepNT2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 16),
    _Cdx6500frdtepNT2_Type()
)
cdx6500frdtepNT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepNT2.setStatus("mandatory")
_Cdx6500frdtepNN1_Type = Integer32
_Cdx6500frdtepNN1_Object = MibTableColumn
cdx6500frdtepNN1 = _Cdx6500frdtepNN1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 17),
    _Cdx6500frdtepNN1_Type()
)
cdx6500frdtepNN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepNN1.setStatus("mandatory")
_Cdx6500frdtepNN2_Type = Integer32
_Cdx6500frdtepNN2_Object = MibTableColumn
cdx6500frdtepNN2 = _Cdx6500frdtepNN2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 18),
    _Cdx6500frdtepNN2_Type()
)
cdx6500frdtepNN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepNN2.setStatus("mandatory")
_Cdx6500frdtepNN3_Type = Integer32
_Cdx6500frdtepNN3_Object = MibTableColumn
cdx6500frdtepNN3 = _Cdx6500frdtepNN3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 19),
    _Cdx6500frdtepNN3_Type()
)
cdx6500frdtepNN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepNN3.setStatus("mandatory")


class _Cdx6500frdtepHighPriorityStn_Type(Integer32):
    """Custom type cdx6500frdtepHighPriorityStn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Cdx6500frdtepHighPriorityStn_Type.__name__ = "Integer32"
_Cdx6500frdtepHighPriorityStn_Object = MibTableColumn
cdx6500frdtepHighPriorityStn = _Cdx6500frdtepHighPriorityStn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 20),
    _Cdx6500frdtepHighPriorityStn_Type()
)
cdx6500frdtepHighPriorityStn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepHighPriorityStn.setStatus("mandatory")


class _Cdx6500frdtepMaxVoiceBWBitsPerSec_Type(Integer32):
    """Custom type cdx6500frdtepMaxVoiceBWBitsPerSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_Cdx6500frdtepMaxVoiceBWBitsPerSec_Type.__name__ = "Integer32"
_Cdx6500frdtepMaxVoiceBWBitsPerSec_Object = MibTableColumn
cdx6500frdtepMaxVoiceBWBitsPerSec = _Cdx6500frdtepMaxVoiceBWBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 21),
    _Cdx6500frdtepMaxVoiceBWBitsPerSec_Type()
)
cdx6500frdtepMaxVoiceBWBitsPerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepMaxVoiceBWBitsPerSec.setStatus("mandatory")


class _Cdx6500frdtepSegSizeVoicePresent_Type(Integer32):
    """Custom type cdx6500frdtepSegSizeVoicePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(33,
              65,
              100,
              129,
              257,
              513,
              1025)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("segSize1024", 1025),
          ("segSize128", 129),
          ("segSize256", 257),
          ("segSize32", 33),
          ("segSize512", 513),
          ("segSize64", 65))
    )


_Cdx6500frdtepSegSizeVoicePresent_Type.__name__ = "Integer32"
_Cdx6500frdtepSegSizeVoicePresent_Object = MibTableColumn
cdx6500frdtepSegSizeVoicePresent = _Cdx6500frdtepSegSizeVoicePresent_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 22),
    _Cdx6500frdtepSegSizeVoicePresent_Type()
)
cdx6500frdtepSegSizeVoicePresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepSegSizeVoicePresent.setStatus("mandatory")


class _Cdx6500frdtepSegSizeVoiceNotPresent_Type(Integer32):
    """Custom type cdx6500frdtepSegSizeVoiceNotPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(33,
              65,
              100,
              129,
              257,
              513,
              1025,
              2049,
              4097,
              32000)
        )
    )
    namedValues = NamedValues(
        *(("disable", 32000),
          ("nc", 100),
          ("segSize1024", 1025),
          ("segSize128", 129),
          ("segSize2048", 2049),
          ("segSize256", 257),
          ("segSize32", 33),
          ("segSize4096", 4097),
          ("segSize512", 513),
          ("segSize64", 65))
    )


_Cdx6500frdtepSegSizeVoiceNotPresent_Type.__name__ = "Integer32"
_Cdx6500frdtepSegSizeVoiceNotPresent_Object = MibTableColumn
cdx6500frdtepSegSizeVoiceNotPresent = _Cdx6500frdtepSegSizeVoiceNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 23),
    _Cdx6500frdtepSegSizeVoiceNotPresent_Type()
)
cdx6500frdtepSegSizeVoiceNotPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepSegSizeVoiceNotPresent.setStatus("mandatory")


class _Cdx6500frdtepInvertTXClock_Type(Integer32):
    """Custom type cdx6500frdtepInvertTXClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("no", 1),
          ("yes", 2))
    )


_Cdx6500frdtepInvertTXClock_Type.__name__ = "Integer32"
_Cdx6500frdtepInvertTXClock_Object = MibTableColumn
cdx6500frdtepInvertTXClock = _Cdx6500frdtepInvertTXClock_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 24),
    _Cdx6500frdtepInvertTXClock_Type()
)
cdx6500frdtepInvertTXClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepInvertTXClock.setStatus("mandatory")


class _Cdx6500frdtepControlProtocolOptions_Type(DisplayString):
    """Custom type cdx6500frdtepControlProtocolOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cdx6500frdtepControlProtocolOptions_Type.__name__ = "DisplayString"
_Cdx6500frdtepControlProtocolOptions_Object = MibTableColumn
cdx6500frdtepControlProtocolOptions = _Cdx6500frdtepControlProtocolOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 25),
    _Cdx6500frdtepControlProtocolOptions_Type()
)
cdx6500frdtepControlProtocolOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepControlProtocolOptions.setStatus("mandatory")


class _Cdx6500frdtepDiscardControlOptions_Type(Integer32):
    """Custom type cdx6500frdtepDiscardControlOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("debit", 2),
          ("none", 1))
    )


_Cdx6500frdtepDiscardControlOptions_Type.__name__ = "Integer32"
_Cdx6500frdtepDiscardControlOptions_Object = MibTableColumn
cdx6500frdtepDiscardControlOptions = _Cdx6500frdtepDiscardControlOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 26),
    _Cdx6500frdtepDiscardControlOptions_Type()
)
cdx6500frdtepDiscardControlOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepDiscardControlOptions.setStatus("mandatory")


class _Cdx6500frdtepElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500frdtepElectricalInterfaceType based on Integer32"""
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
        *(("none", 5),
          ("v24", 1),
          ("v35", 2),
          ("v36", 3),
          ("x21", 4))
    )


_Cdx6500frdtepElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500frdtepElectricalInterfaceType_Object = MibTableColumn
cdx6500frdtepElectricalInterfaceType = _Cdx6500frdtepElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 27),
    _Cdx6500frdtepElectricalInterfaceType_Type()
)
cdx6500frdtepElectricalInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500frdtepV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500frdtepV24ElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ri", 1),
          ("tm", 2))
    )


_Cdx6500frdtepV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500frdtepV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500frdtepV24ElectricalInterfaceOption = _Cdx6500frdtepV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 28),
    _Cdx6500frdtepV24ElectricalInterfaceOption_Type()
)
cdx6500frdtepV24ElectricalInterfaceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500frdtepHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500frdtepHighSpeedElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("xover", 2))
    )


_Cdx6500frdtepHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500frdtepHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500frdtepHighSpeedElectricalInterfaceOption = _Cdx6500frdtepHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 5, 1, 29),
    _Cdx6500frdtepHighSpeedElectricalInterfaceOption_Type()
)
cdx6500frdtepHighSpeedElectricalInterfaceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtepHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTStationProtocolGroup = _Cdx6500PCTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3)
)
_Cdx6500SPCTFRDTEStationTable_Object = MibTable
cdx6500SPCTFRDTEStationTable = _Cdx6500SPCTFRDTEStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdx6500SPCTFRDTEStationTable.setStatus("mandatory")
_Cdx6500SPCTFRDTEStationEntry_Object = MibTableRow
cdx6500SPCTFRDTEStationEntry = _Cdx6500SPCTFRDTEStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1)
)
cdx6500SPCTFRDTEStationEntry.setIndexNames(
    (0, "FRDTE-OPT-MIB", "cdx6500frdtesCfgPortNum"),
    (0, "FRDTE-OPT-MIB", "cdx6500frdtesCfgStationNum"),
)
if mibBuilder.loadTexts:
    cdx6500SPCTFRDTEStationEntry.setStatus("mandatory")


class _Cdx6500frdtesCfgPortNum_Type(Integer32):
    """Custom type cdx6500frdtesCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500frdtesCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500frdtesCfgPortNum_Object = MibTableColumn
cdx6500frdtesCfgPortNum = _Cdx6500frdtesCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 1),
    _Cdx6500frdtesCfgPortNum_Type()
)
cdx6500frdtesCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesCfgPortNum.setStatus("mandatory")


class _Cdx6500frdtesCfgDLCI_Type(Integer32):
    """Custom type cdx6500frdtesCfgDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_Cdx6500frdtesCfgDLCI_Type.__name__ = "Integer32"
_Cdx6500frdtesCfgDLCI_Object = MibTableColumn
cdx6500frdtesCfgDLCI = _Cdx6500frdtesCfgDLCI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 2),
    _Cdx6500frdtesCfgDLCI_Type()
)
cdx6500frdtesCfgDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesCfgDLCI.setStatus("mandatory")


class _Cdx6500frdtesStationType_Type(Integer32):
    """Custom type cdx6500frdtesStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexG", 1),
          ("bypass", 2),
          ("voiceRelay", 3))
    )


_Cdx6500frdtesStationType_Type.__name__ = "Integer32"
_Cdx6500frdtesStationType_Object = MibTableColumn
cdx6500frdtesStationType = _Cdx6500frdtesStationType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 3),
    _Cdx6500frdtesStationType_Type()
)
cdx6500frdtesStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesStationType.setStatus("mandatory")
_Cdx6500frdtesCommInfoRate_Type = Integer32
_Cdx6500frdtesCommInfoRate_Object = MibTableColumn
cdx6500frdtesCommInfoRate = _Cdx6500frdtesCommInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 4),
    _Cdx6500frdtesCommInfoRate_Type()
)
cdx6500frdtesCommInfoRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesCommInfoRate.setStatus("mandatory")
_Cdx6500frdtesCommBurstSize_Type = Integer32
_Cdx6500frdtesCommBurstSize_Object = MibTableColumn
cdx6500frdtesCommBurstSize = _Cdx6500frdtesCommBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 5),
    _Cdx6500frdtesCommBurstSize_Type()
)
cdx6500frdtesCommBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesCommBurstSize.setStatus("mandatory")
_Cdx6500frdtesTransDelay_Type = Integer32
_Cdx6500frdtesTransDelay_Object = MibTableColumn
cdx6500frdtesTransDelay = _Cdx6500frdtesTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 6),
    _Cdx6500frdtesTransDelay_Type()
)
cdx6500frdtesTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesTransDelay.setStatus("mandatory")


class _Cdx6500frdtesControlledMode_Type(Integer32):
    """Custom type cdx6500frdtesControlledMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("congested", 3),
          ("disable", 2),
          ("limit", 4),
          ("nc", 100),
          ("normal", 1))
    )


_Cdx6500frdtesControlledMode_Type.__name__ = "Integer32"
_Cdx6500frdtesControlledMode_Object = MibTableColumn
cdx6500frdtesControlledMode = _Cdx6500frdtesControlledMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 7),
    _Cdx6500frdtesControlledMode_Type()
)
cdx6500frdtesControlledMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesControlledMode.setStatus("mandatory")


class _Cdx6500frdtesLinkAddress_Type(Integer32):
    """Custom type cdx6500frdtesLinkAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1),
          ("nc", 100))
    )


_Cdx6500frdtesLinkAddress_Type.__name__ = "Integer32"
_Cdx6500frdtesLinkAddress_Object = MibTableColumn
cdx6500frdtesLinkAddress = _Cdx6500frdtesLinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 8),
    _Cdx6500frdtesLinkAddress_Type()
)
cdx6500frdtesLinkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesLinkAddress.setStatus("mandatory")
_Cdx6500frdtesPVCChannels_Type = Integer32
_Cdx6500frdtesPVCChannels_Object = MibTableColumn
cdx6500frdtesPVCChannels = _Cdx6500frdtesPVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 9),
    _Cdx6500frdtesPVCChannels_Type()
)
cdx6500frdtesPVCChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesPVCChannels.setStatus("mandatory")
_Cdx6500frdtesStartingPVC_Type = Integer32
_Cdx6500frdtesStartingPVC_Object = MibTableColumn
cdx6500frdtesStartingPVC = _Cdx6500frdtesStartingPVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 10),
    _Cdx6500frdtesStartingPVC_Type()
)
cdx6500frdtesStartingPVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesStartingPVC.setStatus("mandatory")
_Cdx6500frdtesSVCChannels_Type = Integer32
_Cdx6500frdtesSVCChannels_Object = MibTableColumn
cdx6500frdtesSVCChannels = _Cdx6500frdtesSVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 11),
    _Cdx6500frdtesSVCChannels_Type()
)
cdx6500frdtesSVCChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesSVCChannels.setStatus("mandatory")
_Cdx6500frdtesStartingSVC_Type = Integer32
_Cdx6500frdtesStartingSVC_Object = MibTableColumn
cdx6500frdtesStartingSVC = _Cdx6500frdtesStartingSVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 12),
    _Cdx6500frdtesStartingSVC_Type()
)
cdx6500frdtesStartingSVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesStartingSVC.setStatus("mandatory")


class _Cdx6500frdtesInitialFrame_Type(Integer32):
    """Custom type cdx6500frdtesInitialFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disc", 2),
          ("nc", 100),
          ("none", 3),
          ("sabm", 1))
    )


_Cdx6500frdtesInitialFrame_Type.__name__ = "Integer32"
_Cdx6500frdtesInitialFrame_Object = MibTableColumn
cdx6500frdtesInitialFrame = _Cdx6500frdtesInitialFrame_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 13),
    _Cdx6500frdtesInitialFrame_Type()
)
cdx6500frdtesInitialFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesInitialFrame.setStatus("mandatory")
_Cdx6500frdtesRetryTimer_Type = Integer32
_Cdx6500frdtesRetryTimer_Object = MibTableColumn
cdx6500frdtesRetryTimer = _Cdx6500frdtesRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 14),
    _Cdx6500frdtesRetryTimer_Type()
)
cdx6500frdtesRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesRetryTimer.setStatus("mandatory")
_Cdx6500frdtesPollTimer_Type = Integer32
_Cdx6500frdtesPollTimer_Object = MibTableColumn
cdx6500frdtesPollTimer = _Cdx6500frdtesPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 15),
    _Cdx6500frdtesPollTimer_Type()
)
cdx6500frdtesPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesPollTimer.setStatus("mandatory")
_Cdx6500frdtesTries_Type = Integer32
_Cdx6500frdtesTries_Object = MibTableColumn
cdx6500frdtesTries = _Cdx6500frdtesTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 16),
    _Cdx6500frdtesTries_Type()
)
cdx6500frdtesTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesTries.setStatus("mandatory")
_Cdx6500frdtesFrameWinSize_Type = Integer32
_Cdx6500frdtesFrameWinSize_Object = MibTableColumn
cdx6500frdtesFrameWinSize = _Cdx6500frdtesFrameWinSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 17),
    _Cdx6500frdtesFrameWinSize_Type()
)
cdx6500frdtesFrameWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesFrameWinSize.setStatus("mandatory")
_Cdx6500frdtesPacketWinSize_Type = Integer32
_Cdx6500frdtesPacketWinSize_Object = MibTableColumn
cdx6500frdtesPacketWinSize = _Cdx6500frdtesPacketWinSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 18),
    _Cdx6500frdtesPacketWinSize_Type()
)
cdx6500frdtesPacketWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesPacketWinSize.setStatus("mandatory")


class _Cdx6500frdtesMaxPacketSize_Type(Integer32):
    """Custom type cdx6500frdtesMaxPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9,
              10,
              11,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("psize1024", 11),
          ("psize128", 8),
          ("psize256", 9),
          ("psize32", 6),
          ("psize512", 10),
          ("psize64", 7))
    )


_Cdx6500frdtesMaxPacketSize_Type.__name__ = "Integer32"
_Cdx6500frdtesMaxPacketSize_Object = MibTableColumn
cdx6500frdtesMaxPacketSize = _Cdx6500frdtesMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 19),
    _Cdx6500frdtesMaxPacketSize_Type()
)
cdx6500frdtesMaxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesMaxPacketSize.setStatus("mandatory")
_Cdx6500frdtesUpperQueue_Type = Integer32
_Cdx6500frdtesUpperQueue_Object = MibTableColumn
cdx6500frdtesUpperQueue = _Cdx6500frdtesUpperQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 20),
    _Cdx6500frdtesUpperQueue_Type()
)
cdx6500frdtesUpperQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesUpperQueue.setStatus("mandatory")
_Cdx6500frdtesLowerQueue_Type = Integer32
_Cdx6500frdtesLowerQueue_Object = MibTableColumn
cdx6500frdtesLowerQueue = _Cdx6500frdtesLowerQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 21),
    _Cdx6500frdtesLowerQueue_Type()
)
cdx6500frdtesLowerQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesLowerQueue.setStatus("mandatory")
_Cdx6500frdtesRestartTimer_Type = Integer32
_Cdx6500frdtesRestartTimer_Object = MibTableColumn
cdx6500frdtesRestartTimer = _Cdx6500frdtesRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 22),
    _Cdx6500frdtesRestartTimer_Type()
)
cdx6500frdtesRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesRestartTimer.setStatus("mandatory")
_Cdx6500frdtesResetTimer_Type = Integer32
_Cdx6500frdtesResetTimer_Object = MibTableColumn
cdx6500frdtesResetTimer = _Cdx6500frdtesResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 23),
    _Cdx6500frdtesResetTimer_Type()
)
cdx6500frdtesResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesResetTimer.setStatus("mandatory")
_Cdx6500frdtesCallTimer_Type = Integer32
_Cdx6500frdtesCallTimer_Object = MibTableColumn
cdx6500frdtesCallTimer = _Cdx6500frdtesCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 24),
    _Cdx6500frdtesCallTimer_Type()
)
cdx6500frdtesCallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesCallTimer.setStatus("mandatory")
_Cdx6500frdtesClearTimer_Type = Integer32
_Cdx6500frdtesClearTimer_Object = MibTableColumn
cdx6500frdtesClearTimer = _Cdx6500frdtesClearTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 25),
    _Cdx6500frdtesClearTimer_Type()
)
cdx6500frdtesClearTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesClearTimer.setStatus("mandatory")
_Cdx6500frdtesX25Options_Type = Integer32
_Cdx6500frdtesX25Options_Object = MibTableColumn
cdx6500frdtesX25Options = _Cdx6500frdtesX25Options_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 26),
    _Cdx6500frdtesX25Options_Type()
)
cdx6500frdtesX25Options.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesX25Options.setStatus("deprecated")


class _Cdx6500frdtesRCDestination_Type(DisplayString):
    """Custom type cdx6500frdtesRCDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500frdtesRCDestination_Type.__name__ = "DisplayString"
_Cdx6500frdtesRCDestination_Object = MibTableColumn
cdx6500frdtesRCDestination = _Cdx6500frdtesRCDestination_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 27),
    _Cdx6500frdtesRCDestination_Type()
)
cdx6500frdtesRCDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesRCDestination.setStatus("mandatory")


class _Cdx6500frdtesCUG_Type(DisplayString):
    """Custom type cdx6500frdtesCUG based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_Cdx6500frdtesCUG_Type.__name__ = "DisplayString"
_Cdx6500frdtesCUG_Object = MibTableColumn
cdx6500frdtesCUG = _Cdx6500frdtesCUG_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 28),
    _Cdx6500frdtesCUG_Type()
)
cdx6500frdtesCUG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesCUG.setStatus("mandatory")


class _Cdx6500frdtesBillingRecords_Type(Integer32):
    """Custom type cdx6500frdtesBillingRecords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("off", 1),
          ("on", 2))
    )


_Cdx6500frdtesBillingRecords_Type.__name__ = "Integer32"
_Cdx6500frdtesBillingRecords_Object = MibTableColumn
cdx6500frdtesBillingRecords = _Cdx6500frdtesBillingRecords_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 29),
    _Cdx6500frdtesBillingRecords_Type()
)
cdx6500frdtesBillingRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesBillingRecords.setStatus("mandatory")
_Cdx6500frdtesCfgStationNum_Type = Integer32
_Cdx6500frdtesCfgStationNum_Object = MibTableColumn
cdx6500frdtesCfgStationNum = _Cdx6500frdtesCfgStationNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 30),
    _Cdx6500frdtesCfgStationNum_Type()
)
cdx6500frdtesCfgStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesCfgStationNum.setStatus("mandatory")


class _Cdx6500frdtesStnX25Options_Type(DisplayString):
    """Custom type cdx6500frdtesStnX25Options based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Cdx6500frdtesStnX25Options_Type.__name__ = "DisplayString"
_Cdx6500frdtesStnX25Options_Object = MibTableColumn
cdx6500frdtesStnX25Options = _Cdx6500frdtesStnX25Options_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 31),
    _Cdx6500frdtesStnX25Options_Type()
)
cdx6500frdtesStnX25Options.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesStnX25Options.setStatus("mandatory")


class _Cdx6500frdtesStnFrameSegmenter_Type(Integer32):
    """Custom type cdx6500frdtesStnFrameSegmenter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_Cdx6500frdtesStnFrameSegmenter_Type.__name__ = "Integer32"
_Cdx6500frdtesStnFrameSegmenter_Object = MibTableColumn
cdx6500frdtesStnFrameSegmenter = _Cdx6500frdtesStnFrameSegmenter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 32),
    _Cdx6500frdtesStnFrameSegmenter_Type()
)
cdx6500frdtesStnFrameSegmenter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesStnFrameSegmenter.setStatus("mandatory")


class _Cdx6500frdtesStnVoiceSVCChannels_Type(Integer32):
    """Custom type cdx6500frdtesStnVoiceSVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500frdtesStnVoiceSVCChannels_Type.__name__ = "Integer32"
_Cdx6500frdtesStnVoiceSVCChannels_Object = MibTableColumn
cdx6500frdtesStnVoiceSVCChannels = _Cdx6500frdtesStnVoiceSVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 33),
    _Cdx6500frdtesStnVoiceSVCChannels_Type()
)
cdx6500frdtesStnVoiceSVCChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesStnVoiceSVCChannels.setStatus("mandatory")


class _Cdx6500frdtesStnVoiceCongCtrlMode_Type(Integer32):
    """Custom type cdx6500frdtesStnVoiceCongCtrlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_Cdx6500frdtesStnVoiceCongCtrlMode_Type.__name__ = "Integer32"
_Cdx6500frdtesStnVoiceCongCtrlMode_Object = MibTableColumn
cdx6500frdtesStnVoiceCongCtrlMode = _Cdx6500frdtesStnVoiceCongCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 34),
    _Cdx6500frdtesStnVoiceCongCtrlMode_Type()
)
cdx6500frdtesStnVoiceCongCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesStnVoiceCongCtrlMode.setStatus("mandatory")


class _Cdx6500frdtesStnPeakUtilization_Type(Integer32):
    """Custom type cdx6500frdtesStnPeakUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Cdx6500frdtesStnPeakUtilization_Type.__name__ = "Integer32"
_Cdx6500frdtesStnPeakUtilization_Object = MibTableColumn
cdx6500frdtesStnPeakUtilization = _Cdx6500frdtesStnPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 35),
    _Cdx6500frdtesStnPeakUtilization_Type()
)
cdx6500frdtesStnPeakUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesStnPeakUtilization.setStatus("mandatory")


class _Cdx6500frdtesStnMaxInboundQueue_Type(Integer32):
    """Custom type cdx6500frdtesStnMaxInboundQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2500),
    )


_Cdx6500frdtesStnMaxInboundQueue_Type.__name__ = "Integer32"
_Cdx6500frdtesStnMaxInboundQueue_Object = MibTableColumn
cdx6500frdtesStnMaxInboundQueue = _Cdx6500frdtesStnMaxInboundQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 36),
    _Cdx6500frdtesStnMaxInboundQueue_Type()
)
cdx6500frdtesStnMaxInboundQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesStnMaxInboundQueue.setStatus("mandatory")


class _Cdx6500frdtesStnAnnexGRateReduction_Type(Integer32):
    """Custom type cdx6500frdtesStnAnnexGRateReduction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_Cdx6500frdtesStnAnnexGRateReduction_Type.__name__ = "Integer32"
_Cdx6500frdtesStnAnnexGRateReduction_Object = MibTableColumn
cdx6500frdtesStnAnnexGRateReduction = _Cdx6500frdtesStnAnnexGRateReduction_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3, 2, 1, 37),
    _Cdx6500frdtesStnAnnexGRateReduction_Type()
)
cdx6500frdtesStnAnnexGRateReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500frdtesStnAnnexGRateReduction.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PPSTFRDTEPortTable_Object = MibTable
cdx6500PPSTFRDTEPortTable = _Cdx6500PPSTFRDTEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRDTEPortTable.setStatus("mandatory")
_Cdx6500PPSTFRDTEPortEntry_Object = MibTableRow
cdx6500PPSTFRDTEPortEntry = _Cdx6500PPSTFRDTEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1)
)
cdx6500PPSTFRDTEPortEntry.setIndexNames(
    (0, "FRDTE-OPT-MIB", "cdx6500frdtepStatsPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTFRDTEPortEntry.setStatus("mandatory")


class _Cdx6500frdtepStatsPortNum_Type(Integer32):
    """Custom type cdx6500frdtepStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500frdtepStatsPortNum_Type.__name__ = "Integer32"
_Cdx6500frdtepStatsPortNum_Object = MibTableColumn
cdx6500frdtepStatsPortNum = _Cdx6500frdtepStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 1),
    _Cdx6500frdtepStatsPortNum_Type()
)
cdx6500frdtepStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepStatsPortNum.setStatus("mandatory")


class _Cdx6500frdtepPortStatus_Type(Integer32):
    """Custom type cdx6500frdtepPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 3),
          ("disabled", 1),
          ("down", 5),
          ("enabled", 2),
          ("na", 100),
          ("up", 4))
    )


_Cdx6500frdtepPortStatus_Type.__name__ = "Integer32"
_Cdx6500frdtepPortStatus_Object = MibTableColumn
cdx6500frdtepPortStatus = _Cdx6500frdtepPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 2),
    _Cdx6500frdtepPortStatus_Type()
)
cdx6500frdtepPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepPortStatus.setStatus("mandatory")
_Cdx6500frdtepPortSpeed_Type = Integer32
_Cdx6500frdtepPortSpeed_Object = MibTableColumn
cdx6500frdtepPortSpeed = _Cdx6500frdtepPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 3),
    _Cdx6500frdtepPortSpeed_Type()
)
cdx6500frdtepPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepPortSpeed.setStatus("mandatory")


class _Cdx6500frdtepUtilizationIn_Type(Integer32):
    """Custom type cdx6500frdtepUtilizationIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500frdtepUtilizationIn_Type.__name__ = "Integer32"
_Cdx6500frdtepUtilizationIn_Object = MibTableColumn
cdx6500frdtepUtilizationIn = _Cdx6500frdtepUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 4),
    _Cdx6500frdtepUtilizationIn_Type()
)
cdx6500frdtepUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepUtilizationIn.setStatus("mandatory")


class _Cdx6500frdtepUtilizationOut_Type(Integer32):
    """Custom type cdx6500frdtepUtilizationOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500frdtepUtilizationOut_Type.__name__ = "Integer32"
_Cdx6500frdtepUtilizationOut_Object = MibTableColumn
cdx6500frdtepUtilizationOut = _Cdx6500frdtepUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 5),
    _Cdx6500frdtepUtilizationOut_Type()
)
cdx6500frdtepUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepUtilizationOut.setStatus("mandatory")
_Cdx6500frdtepCharInTotal_Type = Counter32
_Cdx6500frdtepCharInTotal_Object = MibTableColumn
cdx6500frdtepCharInTotal = _Cdx6500frdtepCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 6),
    _Cdx6500frdtepCharInTotal_Type()
)
cdx6500frdtepCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepCharInTotal.setStatus("mandatory")
_Cdx6500frdtepCharOutTotal_Type = Counter32
_Cdx6500frdtepCharOutTotal_Object = MibTableColumn
cdx6500frdtepCharOutTotal = _Cdx6500frdtepCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 7),
    _Cdx6500frdtepCharOutTotal_Type()
)
cdx6500frdtepCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepCharOutTotal.setStatus("mandatory")
_Cdx6500frdtepCharsInPerSec_Type = Integer32
_Cdx6500frdtepCharsInPerSec_Object = MibTableColumn
cdx6500frdtepCharsInPerSec = _Cdx6500frdtepCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 8),
    _Cdx6500frdtepCharsInPerSec_Type()
)
cdx6500frdtepCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepCharsInPerSec.setStatus("mandatory")
_Cdx6500frdtepCharsOutPerSec_Type = Integer32
_Cdx6500frdtepCharsOutPerSec_Object = MibTableColumn
cdx6500frdtepCharsOutPerSec = _Cdx6500frdtepCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 9),
    _Cdx6500frdtepCharsOutPerSec_Type()
)
cdx6500frdtepCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepCharsOutPerSec.setStatus("mandatory")
_Cdx6500frdtepFrameInTotal_Type = Counter32
_Cdx6500frdtepFrameInTotal_Object = MibTableColumn
cdx6500frdtepFrameInTotal = _Cdx6500frdtepFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 10),
    _Cdx6500frdtepFrameInTotal_Type()
)
cdx6500frdtepFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepFrameInTotal.setStatus("mandatory")
_Cdx6500frdtepFrameOutTotal_Type = Counter32
_Cdx6500frdtepFrameOutTotal_Object = MibTableColumn
cdx6500frdtepFrameOutTotal = _Cdx6500frdtepFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 11),
    _Cdx6500frdtepFrameOutTotal_Type()
)
cdx6500frdtepFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepFrameOutTotal.setStatus("mandatory")
_Cdx6500frdtepFramesInPerSec_Type = Integer32
_Cdx6500frdtepFramesInPerSec_Object = MibTableColumn
cdx6500frdtepFramesInPerSec = _Cdx6500frdtepFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 12),
    _Cdx6500frdtepFramesInPerSec_Type()
)
cdx6500frdtepFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepFramesInPerSec.setStatus("mandatory")
_Cdx6500frdtepFramesOutPerSec_Type = Integer32
_Cdx6500frdtepFramesOutPerSec_Object = MibTableColumn
cdx6500frdtepFramesOutPerSec = _Cdx6500frdtepFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 13),
    _Cdx6500frdtepFramesOutPerSec_Type()
)
cdx6500frdtepFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepFramesOutPerSec.setStatus("mandatory")
_Cdx6500frdtepOverrunErrors_Type = Counter16
_Cdx6500frdtepOverrunErrors_Object = MibTableColumn
cdx6500frdtepOverrunErrors = _Cdx6500frdtepOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 14),
    _Cdx6500frdtepOverrunErrors_Type()
)
cdx6500frdtepOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepOverrunErrors.setStatus("mandatory")
_Cdx6500frdtepUnderrunErrors_Type = Counter16
_Cdx6500frdtepUnderrunErrors_Object = MibTableColumn
cdx6500frdtepUnderrunErrors = _Cdx6500frdtepUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 15),
    _Cdx6500frdtepUnderrunErrors_Type()
)
cdx6500frdtepUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepUnderrunErrors.setStatus("mandatory")
_Cdx6500frdtepCRCErrors_Type = Counter16
_Cdx6500frdtepCRCErrors_Object = MibTableColumn
cdx6500frdtepCRCErrors = _Cdx6500frdtepCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 5, 1, 16),
    _Cdx6500frdtepCRCErrors_Type()
)
cdx6500frdtepCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtepCRCErrors.setStatus("mandatory")
_Cdx6500PSTStationProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTStationProtocolGroup = _Cdx6500PSTStationProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3)
)
_Cdx6500SPSTFRDTEStationTable_Object = MibTable
cdx6500SPSTFRDTEStationTable = _Cdx6500SPSTFRDTEStationTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdx6500SPSTFRDTEStationTable.setStatus("mandatory")
_Cdx6500SPSTFRDTEStationEntry_Object = MibTableRow
cdx6500SPSTFRDTEStationEntry = _Cdx6500SPSTFRDTEStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1)
)
cdx6500SPSTFRDTEStationEntry.setIndexNames(
    (0, "FRDTE-OPT-MIB", "cdx6500frdtesStatsPortNum"),
    (0, "FRDTE-OPT-MIB", "cdx6500frdtesStatsStationNumber"),
)
if mibBuilder.loadTexts:
    cdx6500SPSTFRDTEStationEntry.setStatus("mandatory")


class _Cdx6500frdtesStatsPortNum_Type(Integer32):
    """Custom type cdx6500frdtesStatsPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500frdtesStatsPortNum_Type.__name__ = "Integer32"
_Cdx6500frdtesStatsPortNum_Object = MibTableColumn
cdx6500frdtesStatsPortNum = _Cdx6500frdtesStatsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 1),
    _Cdx6500frdtesStatsPortNum_Type()
)
cdx6500frdtesStatsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesStatsPortNum.setStatus("mandatory")


class _Cdx6500frdtesStatsDLCI_Type(Integer32):
    """Custom type cdx6500frdtesStatsDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_Cdx6500frdtesStatsDLCI_Type.__name__ = "Integer32"
_Cdx6500frdtesStatsDLCI_Object = MibTableColumn
cdx6500frdtesStatsDLCI = _Cdx6500frdtesStatsDLCI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 2),
    _Cdx6500frdtesStatsDLCI_Type()
)
cdx6500frdtesStatsDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesStatsDLCI.setStatus("mandatory")


class _Cdx6500frdtesUtilizationIn_Type(Integer32):
    """Custom type cdx6500frdtesUtilizationIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500frdtesUtilizationIn_Type.__name__ = "Integer32"
_Cdx6500frdtesUtilizationIn_Object = MibTableColumn
cdx6500frdtesUtilizationIn = _Cdx6500frdtesUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 3),
    _Cdx6500frdtesUtilizationIn_Type()
)
cdx6500frdtesUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesUtilizationIn.setStatus("mandatory")


class _Cdx6500frdtesUtilizationOut_Type(Integer32):
    """Custom type cdx6500frdtesUtilizationOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500frdtesUtilizationOut_Type.__name__ = "Integer32"
_Cdx6500frdtesUtilizationOut_Object = MibTableColumn
cdx6500frdtesUtilizationOut = _Cdx6500frdtesUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 4),
    _Cdx6500frdtesUtilizationOut_Type()
)
cdx6500frdtesUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesUtilizationOut.setStatus("mandatory")
_Cdx6500frdtesMaxSVCCount_Type = Integer32
_Cdx6500frdtesMaxSVCCount_Object = MibTableColumn
cdx6500frdtesMaxSVCCount = _Cdx6500frdtesMaxSVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 5),
    _Cdx6500frdtesMaxSVCCount_Type()
)
cdx6500frdtesMaxSVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesMaxSVCCount.setStatus("mandatory")
_Cdx6500frdtesCurrentSVCCount_Type = Integer32
_Cdx6500frdtesCurrentSVCCount_Object = MibTableColumn
cdx6500frdtesCurrentSVCCount = _Cdx6500frdtesCurrentSVCCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 6),
    _Cdx6500frdtesCurrentSVCCount_Type()
)
cdx6500frdtesCurrentSVCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesCurrentSVCCount.setStatus("mandatory")
_Cdx6500frdtesCharInTotal_Type = Counter32
_Cdx6500frdtesCharInTotal_Object = MibTableColumn
cdx6500frdtesCharInTotal = _Cdx6500frdtesCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 7),
    _Cdx6500frdtesCharInTotal_Type()
)
cdx6500frdtesCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesCharInTotal.setStatus("mandatory")
_Cdx6500frdtesCharOutTotal_Type = Counter32
_Cdx6500frdtesCharOutTotal_Object = MibTableColumn
cdx6500frdtesCharOutTotal = _Cdx6500frdtesCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 8),
    _Cdx6500frdtesCharOutTotal_Type()
)
cdx6500frdtesCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesCharOutTotal.setStatus("mandatory")
_Cdx6500frdtesCharsInPerSec_Type = Integer32
_Cdx6500frdtesCharsInPerSec_Object = MibTableColumn
cdx6500frdtesCharsInPerSec = _Cdx6500frdtesCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 9),
    _Cdx6500frdtesCharsInPerSec_Type()
)
cdx6500frdtesCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesCharsInPerSec.setStatus("mandatory")
_Cdx6500frdtesCharsOutPerSec_Type = Integer32
_Cdx6500frdtesCharsOutPerSec_Object = MibTableColumn
cdx6500frdtesCharsOutPerSec = _Cdx6500frdtesCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 10),
    _Cdx6500frdtesCharsOutPerSec_Type()
)
cdx6500frdtesCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesCharsOutPerSec.setStatus("mandatory")
_Cdx6500frdtesPktInTotal_Type = Counter32
_Cdx6500frdtesPktInTotal_Object = MibTableColumn
cdx6500frdtesPktInTotal = _Cdx6500frdtesPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 11),
    _Cdx6500frdtesPktInTotal_Type()
)
cdx6500frdtesPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesPktInTotal.setStatus("mandatory")
_Cdx6500frdtesPktOutTotal_Type = Counter32
_Cdx6500frdtesPktOutTotal_Object = MibTableColumn
cdx6500frdtesPktOutTotal = _Cdx6500frdtesPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 12),
    _Cdx6500frdtesPktOutTotal_Type()
)
cdx6500frdtesPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesPktOutTotal.setStatus("mandatory")
_Cdx6500frdtesPktsInPerSec_Type = Integer32
_Cdx6500frdtesPktsInPerSec_Object = MibTableColumn
cdx6500frdtesPktsInPerSec = _Cdx6500frdtesPktsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 13),
    _Cdx6500frdtesPktsInPerSec_Type()
)
cdx6500frdtesPktsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesPktsInPerSec.setStatus("mandatory")
_Cdx6500frdtesPktsOutPerSec_Type = Integer32
_Cdx6500frdtesPktsOutPerSec_Object = MibTableColumn
cdx6500frdtesPktsOutPerSec = _Cdx6500frdtesPktsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 14),
    _Cdx6500frdtesPktsOutPerSec_Type()
)
cdx6500frdtesPktsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesPktsOutPerSec.setStatus("mandatory")
_Cdx6500frdtesPacketsQueued_Type = Integer32
_Cdx6500frdtesPacketsQueued_Object = MibTableColumn
cdx6500frdtesPacketsQueued = _Cdx6500frdtesPacketsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 15),
    _Cdx6500frdtesPacketsQueued_Type()
)
cdx6500frdtesPacketsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesPacketsQueued.setStatus("mandatory")
_Cdx6500frdtesFrameInTotal_Type = Counter32
_Cdx6500frdtesFrameInTotal_Object = MibTableColumn
cdx6500frdtesFrameInTotal = _Cdx6500frdtesFrameInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 16),
    _Cdx6500frdtesFrameInTotal_Type()
)
cdx6500frdtesFrameInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesFrameInTotal.setStatus("mandatory")
_Cdx6500frdtesFrameOutTotal_Type = Counter32
_Cdx6500frdtesFrameOutTotal_Object = MibTableColumn
cdx6500frdtesFrameOutTotal = _Cdx6500frdtesFrameOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 17),
    _Cdx6500frdtesFrameOutTotal_Type()
)
cdx6500frdtesFrameOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesFrameOutTotal.setStatus("mandatory")
_Cdx6500frdtesFramesInPerSec_Type = Integer32
_Cdx6500frdtesFramesInPerSec_Object = MibTableColumn
cdx6500frdtesFramesInPerSec = _Cdx6500frdtesFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 18),
    _Cdx6500frdtesFramesInPerSec_Type()
)
cdx6500frdtesFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesFramesInPerSec.setStatus("mandatory")
_Cdx6500frdtesFramesOutPerSec_Type = Integer32
_Cdx6500frdtesFramesOutPerSec_Object = MibTableColumn
cdx6500frdtesFramesOutPerSec = _Cdx6500frdtesFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 19),
    _Cdx6500frdtesFramesOutPerSec_Type()
)
cdx6500frdtesFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesFramesOutPerSec.setStatus("mandatory")
_Cdx6500frdtesInfoFramesIn_Type = Counter32
_Cdx6500frdtesInfoFramesIn_Object = MibTableColumn
cdx6500frdtesInfoFramesIn = _Cdx6500frdtesInfoFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 20),
    _Cdx6500frdtesInfoFramesIn_Type()
)
cdx6500frdtesInfoFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesInfoFramesIn.setStatus("mandatory")
_Cdx6500frdtesInfoFramesOut_Type = Counter32
_Cdx6500frdtesInfoFramesOut_Object = MibTableColumn
cdx6500frdtesInfoFramesOut = _Cdx6500frdtesInfoFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 21),
    _Cdx6500frdtesInfoFramesOut_Type()
)
cdx6500frdtesInfoFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesInfoFramesOut.setStatus("mandatory")
_Cdx6500frdtesRNRFramesIn_Type = Counter32
_Cdx6500frdtesRNRFramesIn_Object = MibTableColumn
cdx6500frdtesRNRFramesIn = _Cdx6500frdtesRNRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 22),
    _Cdx6500frdtesRNRFramesIn_Type()
)
cdx6500frdtesRNRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesRNRFramesIn.setStatus("mandatory")
_Cdx6500frdtesRNRFramesOut_Type = Counter32
_Cdx6500frdtesRNRFramesOut_Object = MibTableColumn
cdx6500frdtesRNRFramesOut = _Cdx6500frdtesRNRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 23),
    _Cdx6500frdtesRNRFramesOut_Type()
)
cdx6500frdtesRNRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesRNRFramesOut.setStatus("mandatory")
_Cdx6500frdtesRRFramesIn_Type = Counter32
_Cdx6500frdtesRRFramesIn_Object = MibTableColumn
cdx6500frdtesRRFramesIn = _Cdx6500frdtesRRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 24),
    _Cdx6500frdtesRRFramesIn_Type()
)
cdx6500frdtesRRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesRRFramesIn.setStatus("mandatory")
_Cdx6500frdtesRRFramesOut_Type = Counter32
_Cdx6500frdtesRRFramesOut_Object = MibTableColumn
cdx6500frdtesRRFramesOut = _Cdx6500frdtesRRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 25),
    _Cdx6500frdtesRRFramesOut_Type()
)
cdx6500frdtesRRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesRRFramesOut.setStatus("mandatory")
_Cdx6500frdtesREJFramesIn_Type = Counter32
_Cdx6500frdtesREJFramesIn_Object = MibTableColumn
cdx6500frdtesREJFramesIn = _Cdx6500frdtesREJFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 26),
    _Cdx6500frdtesREJFramesIn_Type()
)
cdx6500frdtesREJFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesREJFramesIn.setStatus("mandatory")
_Cdx6500frdtesREJFramesOut_Type = Counter32
_Cdx6500frdtesREJFramesOut_Object = MibTableColumn
cdx6500frdtesREJFramesOut = _Cdx6500frdtesREJFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 27),
    _Cdx6500frdtesREJFramesOut_Type()
)
cdx6500frdtesREJFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesREJFramesOut.setStatus("mandatory")
_Cdx6500frdtesDataPktsIn_Type = Counter32
_Cdx6500frdtesDataPktsIn_Object = MibTableColumn
cdx6500frdtesDataPktsIn = _Cdx6500frdtesDataPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 28),
    _Cdx6500frdtesDataPktsIn_Type()
)
cdx6500frdtesDataPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesDataPktsIn.setStatus("mandatory")
_Cdx6500frdtesDataPktsOut_Type = Counter32
_Cdx6500frdtesDataPktsOut_Object = MibTableColumn
cdx6500frdtesDataPktsOut = _Cdx6500frdtesDataPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 29),
    _Cdx6500frdtesDataPktsOut_Type()
)
cdx6500frdtesDataPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesDataPktsOut.setStatus("mandatory")


class _Cdx6500frdtesResetStats_Type(Integer32):
    """Custom type cdx6500frdtesResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("reset", 1))
    )


_Cdx6500frdtesResetStats_Type.__name__ = "Integer32"
_Cdx6500frdtesResetStats_Object = MibTableColumn
cdx6500frdtesResetStats = _Cdx6500frdtesResetStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 30),
    _Cdx6500frdtesResetStats_Type()
)
cdx6500frdtesResetStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500frdtesResetStats.setStatus("mandatory")


class _Cdx6500frdtesBoot_Type(Integer32):
    """Custom type cdx6500frdtesBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("noBoot", 2))
    )


_Cdx6500frdtesBoot_Type.__name__ = "Integer32"
_Cdx6500frdtesBoot_Object = MibTableColumn
cdx6500frdtesBoot = _Cdx6500frdtesBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 31),
    _Cdx6500frdtesBoot_Type()
)
cdx6500frdtesBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500frdtesBoot.setStatus("mandatory")


class _Cdx6500frdtesDisable_Type(Integer32):
    """Custom type cdx6500frdtesDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("noDisable", 2))
    )


_Cdx6500frdtesDisable_Type.__name__ = "Integer32"
_Cdx6500frdtesDisable_Object = MibTableColumn
cdx6500frdtesDisable = _Cdx6500frdtesDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 32),
    _Cdx6500frdtesDisable_Type()
)
cdx6500frdtesDisable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500frdtesDisable.setStatus("mandatory")


class _Cdx6500frdtesEnable_Type(Integer32):
    """Custom type cdx6500frdtesEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("noEnable", 2))
    )


_Cdx6500frdtesEnable_Type.__name__ = "Integer32"
_Cdx6500frdtesEnable_Object = MibTableColumn
cdx6500frdtesEnable = _Cdx6500frdtesEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 33),
    _Cdx6500frdtesEnable_Type()
)
cdx6500frdtesEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500frdtesEnable.setStatus("mandatory")
_Cdx6500frdtesStatsStationNumber_Type = Integer32
_Cdx6500frdtesStatsStationNumber_Object = MibTableColumn
cdx6500frdtesStatsStationNumber = _Cdx6500frdtesStatsStationNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3, 2, 1, 34),
    _Cdx6500frdtesStatsStationNumber_Type()
)
cdx6500frdtesStatsStationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500frdtesStatsStationNumber.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FRDTE-OPT-MIB",
    **{"Counter16": Counter16,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PCTFRDTEPortTable": cdx6500PCTFRDTEPortTable,
       "cdx6500PCTFRDTEPortEntry": cdx6500PCTFRDTEPortEntry,
       "cdx6500frdtepCfgPortNum": cdx6500frdtepCfgPortNum,
       "cdx6500frdtepConnectionType": cdx6500frdtepConnectionType,
       "cdx6500frdtepClockSource": cdx6500frdtepClockSource,
       "cdx6500frdtepClockSpeed": cdx6500frdtepClockSpeed,
       "cdx6500frdtepMaxStations": cdx6500frdtepMaxStations,
       "cdx6500frdtepFrameSeqCounting": cdx6500frdtepFrameSeqCounting,
       "cdx6500frdtepPktSeqCounting": cdx6500frdtepPktSeqCounting,
       "cdx6500frdtepCtrlProtocol": cdx6500frdtepCtrlProtocol,
       "cdx6500frdtepT391": cdx6500frdtepT391,
       "cdx6500frdtepT392": cdx6500frdtepT392,
       "cdx6500frdtepN391": cdx6500frdtepN391,
       "cdx6500frdtepN392": cdx6500frdtepN392,
       "cdx6500frdtepN393": cdx6500frdtepN393,
       "cdx6500frdtepNT1": cdx6500frdtepNT1,
       "cdx6500frdtepNT2": cdx6500frdtepNT2,
       "cdx6500frdtepNN1": cdx6500frdtepNN1,
       "cdx6500frdtepNN2": cdx6500frdtepNN2,
       "cdx6500frdtepNN3": cdx6500frdtepNN3,
       "cdx6500frdtepHighPriorityStn": cdx6500frdtepHighPriorityStn,
       "cdx6500frdtepMaxVoiceBWBitsPerSec": cdx6500frdtepMaxVoiceBWBitsPerSec,
       "cdx6500frdtepSegSizeVoicePresent": cdx6500frdtepSegSizeVoicePresent,
       "cdx6500frdtepSegSizeVoiceNotPresent": cdx6500frdtepSegSizeVoiceNotPresent,
       "cdx6500frdtepInvertTXClock": cdx6500frdtepInvertTXClock,
       "cdx6500frdtepControlProtocolOptions": cdx6500frdtepControlProtocolOptions,
       "cdx6500frdtepDiscardControlOptions": cdx6500frdtepDiscardControlOptions,
       "cdx6500frdtepElectricalInterfaceType": cdx6500frdtepElectricalInterfaceType,
       "cdx6500frdtepV24ElectricalInterfaceOption": cdx6500frdtepV24ElectricalInterfaceOption,
       "cdx6500frdtepHighSpeedElectricalInterfaceOption": cdx6500frdtepHighSpeedElectricalInterfaceOption,
       "cdx6500PCTStationProtocolGroup": cdx6500PCTStationProtocolGroup,
       "cdx6500SPCTFRDTEStationTable": cdx6500SPCTFRDTEStationTable,
       "cdx6500SPCTFRDTEStationEntry": cdx6500SPCTFRDTEStationEntry,
       "cdx6500frdtesCfgPortNum": cdx6500frdtesCfgPortNum,
       "cdx6500frdtesCfgDLCI": cdx6500frdtesCfgDLCI,
       "cdx6500frdtesStationType": cdx6500frdtesStationType,
       "cdx6500frdtesCommInfoRate": cdx6500frdtesCommInfoRate,
       "cdx6500frdtesCommBurstSize": cdx6500frdtesCommBurstSize,
       "cdx6500frdtesTransDelay": cdx6500frdtesTransDelay,
       "cdx6500frdtesControlledMode": cdx6500frdtesControlledMode,
       "cdx6500frdtesLinkAddress": cdx6500frdtesLinkAddress,
       "cdx6500frdtesPVCChannels": cdx6500frdtesPVCChannels,
       "cdx6500frdtesStartingPVC": cdx6500frdtesStartingPVC,
       "cdx6500frdtesSVCChannels": cdx6500frdtesSVCChannels,
       "cdx6500frdtesStartingSVC": cdx6500frdtesStartingSVC,
       "cdx6500frdtesInitialFrame": cdx6500frdtesInitialFrame,
       "cdx6500frdtesRetryTimer": cdx6500frdtesRetryTimer,
       "cdx6500frdtesPollTimer": cdx6500frdtesPollTimer,
       "cdx6500frdtesTries": cdx6500frdtesTries,
       "cdx6500frdtesFrameWinSize": cdx6500frdtesFrameWinSize,
       "cdx6500frdtesPacketWinSize": cdx6500frdtesPacketWinSize,
       "cdx6500frdtesMaxPacketSize": cdx6500frdtesMaxPacketSize,
       "cdx6500frdtesUpperQueue": cdx6500frdtesUpperQueue,
       "cdx6500frdtesLowerQueue": cdx6500frdtesLowerQueue,
       "cdx6500frdtesRestartTimer": cdx6500frdtesRestartTimer,
       "cdx6500frdtesResetTimer": cdx6500frdtesResetTimer,
       "cdx6500frdtesCallTimer": cdx6500frdtesCallTimer,
       "cdx6500frdtesClearTimer": cdx6500frdtesClearTimer,
       "cdx6500frdtesX25Options": cdx6500frdtesX25Options,
       "cdx6500frdtesRCDestination": cdx6500frdtesRCDestination,
       "cdx6500frdtesCUG": cdx6500frdtesCUG,
       "cdx6500frdtesBillingRecords": cdx6500frdtesBillingRecords,
       "cdx6500frdtesCfgStationNum": cdx6500frdtesCfgStationNum,
       "cdx6500frdtesStnX25Options": cdx6500frdtesStnX25Options,
       "cdx6500frdtesStnFrameSegmenter": cdx6500frdtesStnFrameSegmenter,
       "cdx6500frdtesStnVoiceSVCChannels": cdx6500frdtesStnVoiceSVCChannels,
       "cdx6500frdtesStnVoiceCongCtrlMode": cdx6500frdtesStnVoiceCongCtrlMode,
       "cdx6500frdtesStnPeakUtilization": cdx6500frdtesStnPeakUtilization,
       "cdx6500frdtesStnMaxInboundQueue": cdx6500frdtesStnMaxInboundQueue,
       "cdx6500frdtesStnAnnexGRateReduction": cdx6500frdtesStnAnnexGRateReduction,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTFRDTEPortTable": cdx6500PPSTFRDTEPortTable,
       "cdx6500PPSTFRDTEPortEntry": cdx6500PPSTFRDTEPortEntry,
       "cdx6500frdtepStatsPortNum": cdx6500frdtepStatsPortNum,
       "cdx6500frdtepPortStatus": cdx6500frdtepPortStatus,
       "cdx6500frdtepPortSpeed": cdx6500frdtepPortSpeed,
       "cdx6500frdtepUtilizationIn": cdx6500frdtepUtilizationIn,
       "cdx6500frdtepUtilizationOut": cdx6500frdtepUtilizationOut,
       "cdx6500frdtepCharInTotal": cdx6500frdtepCharInTotal,
       "cdx6500frdtepCharOutTotal": cdx6500frdtepCharOutTotal,
       "cdx6500frdtepCharsInPerSec": cdx6500frdtepCharsInPerSec,
       "cdx6500frdtepCharsOutPerSec": cdx6500frdtepCharsOutPerSec,
       "cdx6500frdtepFrameInTotal": cdx6500frdtepFrameInTotal,
       "cdx6500frdtepFrameOutTotal": cdx6500frdtepFrameOutTotal,
       "cdx6500frdtepFramesInPerSec": cdx6500frdtepFramesInPerSec,
       "cdx6500frdtepFramesOutPerSec": cdx6500frdtepFramesOutPerSec,
       "cdx6500frdtepOverrunErrors": cdx6500frdtepOverrunErrors,
       "cdx6500frdtepUnderrunErrors": cdx6500frdtepUnderrunErrors,
       "cdx6500frdtepCRCErrors": cdx6500frdtepCRCErrors,
       "cdx6500PSTStationProtocolGroup": cdx6500PSTStationProtocolGroup,
       "cdx6500SPSTFRDTEStationTable": cdx6500SPSTFRDTEStationTable,
       "cdx6500SPSTFRDTEStationEntry": cdx6500SPSTFRDTEStationEntry,
       "cdx6500frdtesStatsPortNum": cdx6500frdtesStatsPortNum,
       "cdx6500frdtesStatsDLCI": cdx6500frdtesStatsDLCI,
       "cdx6500frdtesUtilizationIn": cdx6500frdtesUtilizationIn,
       "cdx6500frdtesUtilizationOut": cdx6500frdtesUtilizationOut,
       "cdx6500frdtesMaxSVCCount": cdx6500frdtesMaxSVCCount,
       "cdx6500frdtesCurrentSVCCount": cdx6500frdtesCurrentSVCCount,
       "cdx6500frdtesCharInTotal": cdx6500frdtesCharInTotal,
       "cdx6500frdtesCharOutTotal": cdx6500frdtesCharOutTotal,
       "cdx6500frdtesCharsInPerSec": cdx6500frdtesCharsInPerSec,
       "cdx6500frdtesCharsOutPerSec": cdx6500frdtesCharsOutPerSec,
       "cdx6500frdtesPktInTotal": cdx6500frdtesPktInTotal,
       "cdx6500frdtesPktOutTotal": cdx6500frdtesPktOutTotal,
       "cdx6500frdtesPktsInPerSec": cdx6500frdtesPktsInPerSec,
       "cdx6500frdtesPktsOutPerSec": cdx6500frdtesPktsOutPerSec,
       "cdx6500frdtesPacketsQueued": cdx6500frdtesPacketsQueued,
       "cdx6500frdtesFrameInTotal": cdx6500frdtesFrameInTotal,
       "cdx6500frdtesFrameOutTotal": cdx6500frdtesFrameOutTotal,
       "cdx6500frdtesFramesInPerSec": cdx6500frdtesFramesInPerSec,
       "cdx6500frdtesFramesOutPerSec": cdx6500frdtesFramesOutPerSec,
       "cdx6500frdtesInfoFramesIn": cdx6500frdtesInfoFramesIn,
       "cdx6500frdtesInfoFramesOut": cdx6500frdtesInfoFramesOut,
       "cdx6500frdtesRNRFramesIn": cdx6500frdtesRNRFramesIn,
       "cdx6500frdtesRNRFramesOut": cdx6500frdtesRNRFramesOut,
       "cdx6500frdtesRRFramesIn": cdx6500frdtesRRFramesIn,
       "cdx6500frdtesRRFramesOut": cdx6500frdtesRRFramesOut,
       "cdx6500frdtesREJFramesIn": cdx6500frdtesREJFramesIn,
       "cdx6500frdtesREJFramesOut": cdx6500frdtesREJFramesOut,
       "cdx6500frdtesDataPktsIn": cdx6500frdtesDataPktsIn,
       "cdx6500frdtesDataPktsOut": cdx6500frdtesDataPktsOut,
       "cdx6500frdtesResetStats": cdx6500frdtesResetStats,
       "cdx6500frdtesBoot": cdx6500frdtesBoot,
       "cdx6500frdtesDisable": cdx6500frdtesDisable,
       "cdx6500frdtesEnable": cdx6500frdtesEnable,
       "cdx6500frdtesStatsStationNumber": cdx6500frdtesStatsStationNumber,
       "cdx6500Controls": cdx6500Controls}
)
