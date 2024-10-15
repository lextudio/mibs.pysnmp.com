# SNMP MIB module (ADTRAN-ATLAS-VOICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-ATLAS-VOICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:28 2024
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

_Adtran_ObjectIdentity = ObjectIdentity
adtran = _Adtran_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664)
)
_AdMgmt_ObjectIdentity = ObjectIdentity
adMgmt = _AdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2)
)
_AdATLASmg_ObjectIdentity = ObjectIdentity
adATLASmg = _AdATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154)
)
_AdGenATLASmg_ObjectIdentity = ObjectIdentity
adGenATLASmg = _AdGenATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1)
)
_AdATLASVoicemg_ObjectIdentity = ObjectIdentity
adATLASVoicemg = _AdATLASVoicemg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10)
)
_AdATLASVoiceIfNumber_Type = Integer32
_AdATLASVoiceIfNumber_Object = MibScalar
adATLASVoiceIfNumber = _AdATLASVoiceIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 1),
    _AdATLASVoiceIfNumber_Type()
)
adATLASVoiceIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASVoiceIfNumber.setStatus("mandatory")
_AdATLASVoiceIfTable_Object = MibTable
adATLASVoiceIfTable = _AdATLASVoiceIfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 2)
)
if mibBuilder.loadTexts:
    adATLASVoiceIfTable.setStatus("mandatory")
_AdATLASVoiceIfEntry_Object = MibTableRow
adATLASVoiceIfEntry = _AdATLASVoiceIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 2, 1)
)
adATLASVoiceIfEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-VOICE-MIB", "adATLASVoiceIfIndex"),
)
if mibBuilder.loadTexts:
    adATLASVoiceIfEntry.setStatus("mandatory")
_AdATLASVoiceIfIndex_Type = Integer32
_AdATLASVoiceIfIndex_Object = MibTableColumn
adATLASVoiceIfIndex = _AdATLASVoiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 2, 1, 1),
    _AdATLASVoiceIfIndex_Type()
)
adATLASVoiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASVoiceIfIndex.setStatus("mandatory")
_AdATLASVoiceIfSlotNum_Type = Integer32
_AdATLASVoiceIfSlotNum_Object = MibTableColumn
adATLASVoiceIfSlotNum = _AdATLASVoiceIfSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 2, 1, 2),
    _AdATLASVoiceIfSlotNum_Type()
)
adATLASVoiceIfSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASVoiceIfSlotNum.setStatus("mandatory")
_AdATLASVoiceIfPortNum_Type = Integer32
_AdATLASVoiceIfPortNum_Object = MibTableColumn
adATLASVoiceIfPortNum = _AdATLASVoiceIfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 2, 1, 3),
    _AdATLASVoiceIfPortNum_Type()
)
adATLASVoiceIfPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASVoiceIfPortNum.setStatus("mandatory")


class _AdATLASVoiceIfPortStat_Type(Integer32):
    """Custom type adATLASVoiceIfPortStat based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("callInProgress", 24),
          ("disabled", 2),
          ("idle", 3),
          ("inactive", 1),
          ("offhook", 6),
          ("reverseBattery", 7),
          ("test", 4),
          ("testActive", 8),
          ("testDisabled", 14),
          ("testELeadClosed", 23),
          ("testELeadOpen", 22),
          ("testLCNoBatt", 18),
          ("testLCNormTRPolarity", 17),
          ("testLCRevTRPolarity", 19),
          ("testLO", 16),
          ("testOffhook", 9),
          ("testRevBatt", 10),
          ("testRingGND", 20),
          ("testRingOffhook", 15),
          ("testRinging", 11),
          ("testTipOpen", 12),
          ("testTipOpenRingGND", 13),
          ("tipOpen", 5),
          ("transOnly", 21))
    )


_AdATLASVoiceIfPortStat_Type.__name__ = "Integer32"
_AdATLASVoiceIfPortStat_Object = MibTableColumn
adATLASVoiceIfPortStat = _AdATLASVoiceIfPortStat_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 2, 1, 4),
    _AdATLASVoiceIfPortStat_Type()
)
adATLASVoiceIfPortStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASVoiceIfPortStat.setStatus("mandatory")


class _AdATLASVoiceIfTxSignalBits_Type(DisplayString):
    """Custom type adATLASVoiceIfTxSignalBits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AdATLASVoiceIfTxSignalBits_Type.__name__ = "DisplayString"
_AdATLASVoiceIfTxSignalBits_Object = MibTableColumn
adATLASVoiceIfTxSignalBits = _AdATLASVoiceIfTxSignalBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 2, 1, 5),
    _AdATLASVoiceIfTxSignalBits_Type()
)
adATLASVoiceIfTxSignalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASVoiceIfTxSignalBits.setStatus("mandatory")


class _AdATLASVoiceIfRxSignalBits_Type(DisplayString):
    """Custom type adATLASVoiceIfRxSignalBits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AdATLASVoiceIfRxSignalBits_Type.__name__ = "DisplayString"
_AdATLASVoiceIfRxSignalBits_Object = MibTableColumn
adATLASVoiceIfRxSignalBits = _AdATLASVoiceIfRxSignalBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 2, 1, 6),
    _AdATLASVoiceIfRxSignalBits_Type()
)
adATLASVoiceIfRxSignalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASVoiceIfRxSignalBits.setStatus("mandatory")
_AdATLASVoiceTstTable_Object = MibTable
adATLASVoiceTstTable = _AdATLASVoiceTstTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 3)
)
if mibBuilder.loadTexts:
    adATLASVoiceTstTable.setStatus("mandatory")
_AdATLASVoiceTstEntry_Object = MibTableRow
adATLASVoiceTstEntry = _AdATLASVoiceTstEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 3, 1)
)
adATLASVoiceTstEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-VOICE-MIB", "adATLASVoiceTstIndex"),
)
if mibBuilder.loadTexts:
    adATLASVoiceTstEntry.setStatus("mandatory")
_AdATLASVoiceTstIndex_Type = Integer32
_AdATLASVoiceTstIndex_Object = MibTableColumn
adATLASVoiceTstIndex = _AdATLASVoiceTstIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 3, 1, 1),
    _AdATLASVoiceTstIndex_Type()
)
adATLASVoiceTstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASVoiceTstIndex.setStatus("mandatory")


class _AdATLASVoiceTst2W_Type(Integer32):
    """Custom type adATLASVoiceTst2W based on Integer32"""
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
        *(("active", 5),
          ("disable", 8),
          ("eLeadClosed", 11),
          ("eLeadOpen", 10),
          ("loopClosed", 3),
          ("loopOpen", 2),
          ("off", 1),
          ("reverseBattery", 7),
          ("ringGround", 4),
          ("ringing", 9),
          ("tipOpen", 6))
    )


_AdATLASVoiceTst2W_Type.__name__ = "Integer32"
_AdATLASVoiceTst2W_Object = MibTableColumn
adATLASVoiceTst2W = _AdATLASVoiceTst2W_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 3, 1, 2),
    _AdATLASVoiceTst2W_Type()
)
adATLASVoiceTst2W.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASVoiceTst2W.setStatus("mandatory")


class _AdATLASVoiceTstTxABCD_Type(Integer32):
    """Custom type adATLASVoiceTstTxABCD based on Integer32"""
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
        *(("tx0000", 2),
          ("tx0101", 3),
          ("tx1010", 4),
          ("tx1111", 5),
          ("txOff", 1))
    )


_AdATLASVoiceTstTxABCD_Type.__name__ = "Integer32"
_AdATLASVoiceTstTxABCD_Object = MibTableColumn
adATLASVoiceTstTxABCD = _AdATLASVoiceTstTxABCD_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 3, 1, 3),
    _AdATLASVoiceTstTxABCD_Type()
)
adATLASVoiceTstTxABCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASVoiceTstTxABCD.setStatus("mandatory")


class _AdATLASVoiceTst1kHzTone_Type(Integer32):
    """Custom type adATLASVoiceTst1kHzTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("far", 3),
          ("near", 2),
          ("off", 1))
    )


_AdATLASVoiceTst1kHzTone_Type.__name__ = "Integer32"
_AdATLASVoiceTst1kHzTone_Object = MibTableColumn
adATLASVoiceTst1kHzTone = _AdATLASVoiceTst1kHzTone_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 3, 1, 4),
    _AdATLASVoiceTst1kHzTone_Type()
)
adATLASVoiceTst1kHzTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASVoiceTst1kHzTone.setStatus("mandatory")


class _AdATLASVoiceTstLpBk_Type(Integer32):
    """Custom type adATLASVoiceTstLpBk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 2),
          ("digital", 3),
          ("off", 1))
    )


_AdATLASVoiceTstLpBk_Type.__name__ = "Integer32"
_AdATLASVoiceTstLpBk_Object = MibTableColumn
adATLASVoiceTstLpBk = _AdATLASVoiceTstLpBk_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 10, 3, 1, 5),
    _AdATLASVoiceTstLpBk_Type()
)
adATLASVoiceTstLpBk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASVoiceTstLpBk.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ATLAS-VOICE-MIB",
    **{"adtran": adtran,
       "adMgmt": adMgmt,
       "adATLASmg": adATLASmg,
       "adGenATLASmg": adGenATLASmg,
       "adATLASVoicemg": adATLASVoicemg,
       "adATLASVoiceIfNumber": adATLASVoiceIfNumber,
       "adATLASVoiceIfTable": adATLASVoiceIfTable,
       "adATLASVoiceIfEntry": adATLASVoiceIfEntry,
       "adATLASVoiceIfIndex": adATLASVoiceIfIndex,
       "adATLASVoiceIfSlotNum": adATLASVoiceIfSlotNum,
       "adATLASVoiceIfPortNum": adATLASVoiceIfPortNum,
       "adATLASVoiceIfPortStat": adATLASVoiceIfPortStat,
       "adATLASVoiceIfTxSignalBits": adATLASVoiceIfTxSignalBits,
       "adATLASVoiceIfRxSignalBits": adATLASVoiceIfRxSignalBits,
       "adATLASVoiceTstTable": adATLASVoiceTstTable,
       "adATLASVoiceTstEntry": adATLASVoiceTstEntry,
       "adATLASVoiceTstIndex": adATLASVoiceTstIndex,
       "adATLASVoiceTst2W": adATLASVoiceTst2W,
       "adATLASVoiceTstTxABCD": adATLASVoiceTstTxABCD,
       "adATLASVoiceTst1kHzTone": adATLASVoiceTst1kHzTone,
       "adATLASVoiceTstLpBk": adATLASVoiceTstLpBk}
)
