# SNMP MIB module (UDS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UDS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:26 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Uds1_ObjectIdentity = ObjectIdentity
uds1 = _Uds1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 4)
)
_Uds1ConfigTable_Object = MibTable
uds1ConfigTable = _Uds1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1)
)
if mibBuilder.loadTexts:
    uds1ConfigTable.setStatus("mandatory")
_Uds1ConfigEntry_Object = MibTableRow
uds1ConfigEntry = _Uds1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1)
)
uds1ConfigEntry.setIndexNames(
    (0, "UDS1-MIB", "uds1CfgIndex"),
)
if mibBuilder.loadTexts:
    uds1ConfigEntry.setStatus("mandatory")
_Uds1CfgIndex_Type = Integer32
_Uds1CfgIndex_Object = MibTableColumn
uds1CfgIndex = _Uds1CfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 1),
    _Uds1CfgIndex_Type()
)
uds1CfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1CfgIndex.setStatus("mandatory")


class _Uds1CfgRespToRemoteLoopbk_Type(Integer32):
    """Custom type uds1CfgRespToRemoteLoopbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("respond", 2))
    )


_Uds1CfgRespToRemoteLoopbk_Type.__name__ = "Integer32"
_Uds1CfgRespToRemoteLoopbk_Object = MibTableColumn
uds1CfgRespToRemoteLoopbk = _Uds1CfgRespToRemoteLoopbk_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 2),
    _Uds1CfgRespToRemoteLoopbk_Type()
)
uds1CfgRespToRemoteLoopbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgRespToRemoteLoopbk.setStatus("mandatory")


class _Uds1CfgJitterAttenuation_Type(Integer32):
    """Custom type uds1CfgJitterAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attenJitterOnRcvr", 1),
          ("attenJitterOnTxmtr", 2),
          ("notApplicable", 3))
    )


_Uds1CfgJitterAttenuation_Type.__name__ = "Integer32"
_Uds1CfgJitterAttenuation_Object = MibTableColumn
uds1CfgJitterAttenuation = _Uds1CfgJitterAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 3),
    _Uds1CfgJitterAttenuation_Type()
)
uds1CfgJitterAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgJitterAttenuation.setStatus("mandatory")


class _Uds1CfgXmitLineBuildOut_Type(Integer32):
    """Custom type uds1CfgXmitLineBuildOut based on Integer32"""
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
        *(("dB0", 1),
          ("dB15", 3),
          ("dB22", 4),
          ("dB7", 2),
          ("notApplicable", 5))
    )


_Uds1CfgXmitLineBuildOut_Type.__name__ = "Integer32"
_Uds1CfgXmitLineBuildOut_Object = MibTableColumn
uds1CfgXmitLineBuildOut = _Uds1CfgXmitLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 4),
    _Uds1CfgXmitLineBuildOut_Type()
)
uds1CfgXmitLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgXmitLineBuildOut.setStatus("mandatory")


class _Uds1CfgAutoBusyEnable_Type(Integer32):
    """Custom type uds1CfgAutoBusyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Uds1CfgAutoBusyEnable_Type.__name__ = "Integer32"
_Uds1CfgAutoBusyEnable_Object = MibTableColumn
uds1CfgAutoBusyEnable = _Uds1CfgAutoBusyEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 5),
    _Uds1CfgAutoBusyEnable_Type()
)
uds1CfgAutoBusyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgAutoBusyEnable.setStatus("mandatory")


class _Uds1CfgDialInAdr_Type(Integer32):
    """Custom type uds1CfgDialInAdr based on Integer32"""
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
        *(("ani", 4),
          ("ani-dnis", 3),
          ("dnis", 2),
          ("noAddress", 1))
    )


_Uds1CfgDialInAdr_Type.__name__ = "Integer32"
_Uds1CfgDialInAdr_Object = MibTableColumn
uds1CfgDialInAdr = _Uds1CfgDialInAdr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 6),
    _Uds1CfgDialInAdr_Type()
)
uds1CfgDialInAdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgDialInAdr.setStatus("mandatory")


class _Uds1CfgZeroCoding_Type(Integer32):
    """Custom type uds1CfgZeroCoding based on Integer32"""
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
        *(("ami", 4),
          ("b8zs", 3),
          ("hdb3", 5),
          ("other", 1),
          ("zcs", 2))
    )


_Uds1CfgZeroCoding_Type.__name__ = "Integer32"
_Uds1CfgZeroCoding_Object = MibTableColumn
uds1CfgZeroCoding = _Uds1CfgZeroCoding_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 7),
    _Uds1CfgZeroCoding_Type()
)
uds1CfgZeroCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgZeroCoding.setStatus("mandatory")


class _Uds1CfgDialInOutTrunkSt_Type(Integer32):
    """Custom type uds1CfgDialInOutTrunkSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dialTone", 3),
          ("immediate", 2),
          ("wink", 1))
    )


_Uds1CfgDialInOutTrunkSt_Type.__name__ = "Integer32"
_Uds1CfgDialInOutTrunkSt_Object = MibTableColumn
uds1CfgDialInOutTrunkSt = _Uds1CfgDialInOutTrunkSt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 8),
    _Uds1CfgDialInOutTrunkSt_Type()
)
uds1CfgDialInOutTrunkSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgDialInOutTrunkSt.setStatus("mandatory")


class _Uds1CfgDialInAdrAckWinkEn_Type(Integer32):
    """Custom type uds1CfgDialInAdrAckWinkEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Uds1CfgDialInAdrAckWinkEn_Type.__name__ = "Integer32"
_Uds1CfgDialInAdrAckWinkEn_Object = MibTableColumn
uds1CfgDialInAdrAckWinkEn = _Uds1CfgDialInAdrAckWinkEn_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 9),
    _Uds1CfgDialInAdrAckWinkEn_Type()
)
uds1CfgDialInAdrAckWinkEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgDialInAdrAckWinkEn.setStatus("mandatory")


class _Uds1CfgDialOutAdrDly_Type(Integer32):
    """Custom type uds1CfgDialOutAdrDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70, 3000),
    )


_Uds1CfgDialOutAdrDly_Type.__name__ = "Integer32"
_Uds1CfgDialOutAdrDly_Object = MibTableColumn
uds1CfgDialOutAdrDly = _Uds1CfgDialOutAdrDly_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 10),
    _Uds1CfgDialOutAdrDly_Type()
)
uds1CfgDialOutAdrDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgDialOutAdrDly.setStatus("mandatory")


class _Uds1CfgStuffByteValue_Type(Integer32):
    """Custom type uds1CfgStuffByteValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Uds1CfgStuffByteValue_Type.__name__ = "Integer32"
_Uds1CfgStuffByteValue_Object = MibTableColumn
uds1CfgStuffByteValue = _Uds1CfgStuffByteValue_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 11),
    _Uds1CfgStuffByteValue_Type()
)
uds1CfgStuffByteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgStuffByteValue.setStatus("mandatory")


class _Uds1CfgDialInOutTrunkType_Type(Integer32):
    """Custom type uds1CfgDialInOutTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eAndMTypeII", 1),
          ("groundStart", 3),
          ("loopStart", 2))
    )


_Uds1CfgDialInOutTrunkType_Type.__name__ = "Integer32"
_Uds1CfgDialInOutTrunkType_Object = MibTableColumn
uds1CfgDialInOutTrunkType = _Uds1CfgDialInOutTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 12),
    _Uds1CfgDialInOutTrunkType_Type()
)
uds1CfgDialInOutTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgDialInOutTrunkType.setStatus("mandatory")


class _Uds1CfgPriSwitchType_Type(Integer32):
    """Custom type uds1CfgPriSwitchType based on Integer32"""
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
        *(("priSw4ESS", 1),
          ("priSw5ESS", 2),
          ("priSwDASS2", 8),
          ("priSwDMS100", 3),
          ("priSwICTR4", 4),
          ("priSwINS1500", 7),
          ("priSwNI2", 6),
          ("priSwTSO14", 9),
          ("priSwVn4", 5))
    )


_Uds1CfgPriSwitchType_Type.__name__ = "Integer32"
_Uds1CfgPriSwitchType_Object = MibTableColumn
uds1CfgPriSwitchType = _Uds1CfgPriSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 13),
    _Uds1CfgPriSwitchType_Type()
)
uds1CfgPriSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgPriSwitchType.setStatus("mandatory")


class _Uds1CfgIdleByte_Type(Integer32):
    """Custom type uds1CfgIdleByte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Uds1CfgIdleByte_Type.__name__ = "Integer32"
_Uds1CfgIdleByte_Object = MibTableColumn
uds1CfgIdleByte = _Uds1CfgIdleByte_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 14),
    _Uds1CfgIdleByte_Type()
)
uds1CfgIdleByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgIdleByte.setStatus("mandatory")


class _Uds1CfgAnlgBlockErrCode_Type(Integer32):
    """Custom type uds1CfgAnlgBlockErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Uds1CfgAnlgBlockErrCode_Type.__name__ = "Integer32"
_Uds1CfgAnlgBlockErrCode_Object = MibTableColumn
uds1CfgAnlgBlockErrCode = _Uds1CfgAnlgBlockErrCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 15),
    _Uds1CfgAnlgBlockErrCode_Type()
)
uds1CfgAnlgBlockErrCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgAnlgBlockErrCode.setStatus("mandatory")


class _Uds1CfgDgtlBlockErrCode_Type(Integer32):
    """Custom type uds1CfgDgtlBlockErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Uds1CfgDgtlBlockErrCode_Type.__name__ = "Integer32"
_Uds1CfgDgtlBlockErrCode_Object = MibTableColumn
uds1CfgDgtlBlockErrCode = _Uds1CfgDgtlBlockErrCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 16),
    _Uds1CfgDgtlBlockErrCode_Type()
)
uds1CfgDgtlBlockErrCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgDgtlBlockErrCode.setStatus("mandatory")


class _Uds1CfgNoMdmAvailErrCode_Type(Integer32):
    """Custom type uds1CfgNoMdmAvailErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Uds1CfgNoMdmAvailErrCode_Type.__name__ = "Integer32"
_Uds1CfgNoMdmAvailErrCode_Object = MibTableColumn
uds1CfgNoMdmAvailErrCode = _Uds1CfgNoMdmAvailErrCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 17),
    _Uds1CfgNoMdmAvailErrCode_Type()
)
uds1CfgNoMdmAvailErrCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgNoMdmAvailErrCode.setStatus("mandatory")


class _Uds1CfgNoIgwsAvailErrCode_Type(Integer32):
    """Custom type uds1CfgNoIgwsAvailErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Uds1CfgNoIgwsAvailErrCode_Type.__name__ = "Integer32"
_Uds1CfgNoIgwsAvailErrCode_Object = MibTableColumn
uds1CfgNoIgwsAvailErrCode = _Uds1CfgNoIgwsAvailErrCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 18),
    _Uds1CfgNoIgwsAvailErrCode_Type()
)
uds1CfgNoIgwsAvailErrCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgNoIgwsAvailErrCode.setStatus("mandatory")


class _Uds1CfgChanBlockErrCode_Type(Integer32):
    """Custom type uds1CfgChanBlockErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Uds1CfgChanBlockErrCode_Type.__name__ = "Integer32"
_Uds1CfgChanBlockErrCode_Object = MibTableColumn
uds1CfgChanBlockErrCode = _Uds1CfgChanBlockErrCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 19),
    _Uds1CfgChanBlockErrCode_Type()
)
uds1CfgChanBlockErrCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgChanBlockErrCode.setStatus("mandatory")


class _Uds1CfgBlockCallType_Type(Integer32):
    """Custom type uds1CfgBlockCallType based on Integer32"""
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
        *(("blockAll", 5),
          ("blockAnalog", 3),
          ("blockDigital", 4),
          ("blockNone", 2),
          ("notSupported", 1))
    )


_Uds1CfgBlockCallType_Type.__name__ = "Integer32"
_Uds1CfgBlockCallType_Object = MibTableColumn
uds1CfgBlockCallType = _Uds1CfgBlockCallType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 20),
    _Uds1CfgBlockCallType_Type()
)
uds1CfgBlockCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgBlockCallType.setStatus("mandatory")


class _Uds1CfgNfasId_Type(Integer32):
    """Custom type uds1CfgNfasId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Uds1CfgNfasId_Type.__name__ = "Integer32"
_Uds1CfgNfasId_Object = MibTableColumn
uds1CfgNfasId = _Uds1CfgNfasId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 21),
    _Uds1CfgNfasId_Type()
)
uds1CfgNfasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgNfasId.setStatus("mandatory")


class _Uds1CfgNfasDChannel_Type(Integer32):
    """Custom type uds1CfgNfasDChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dchannel", 2),
          ("extraBchannel", 3),
          ("notSupported", 1))
    )


_Uds1CfgNfasDChannel_Type.__name__ = "Integer32"
_Uds1CfgNfasDChannel_Object = MibTableColumn
uds1CfgNfasDChannel = _Uds1CfgNfasDChannel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 22),
    _Uds1CfgNfasDChannel_Type()
)
uds1CfgNfasDChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgNfasDChannel.setStatus("mandatory")


class _Uds1CfgShrtHaulDist_Type(Integer32):
    """Custom type uds1CfgShrtHaulDist based on Integer32"""
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
        *(("len0thru133Ft", 2),
          ("len133thru266Ft", 3),
          ("len266thru399Ft", 4),
          ("len399thru533Ft", 5),
          ("len533thru655Ft", 6),
          ("notApplicable", 1))
    )


_Uds1CfgShrtHaulDist_Type.__name__ = "Integer32"
_Uds1CfgShrtHaulDist_Object = MibTableColumn
uds1CfgShrtHaulDist = _Uds1CfgShrtHaulDist_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 23),
    _Uds1CfgShrtHaulDist_Type()
)
uds1CfgShrtHaulDist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgShrtHaulDist.setStatus("mandatory")


class _Uds1CfgCallProceedingRsp_Type(Integer32):
    """Custom type uds1CfgCallProceedingRsp based on Integer32"""
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


_Uds1CfgCallProceedingRsp_Type.__name__ = "Integer32"
_Uds1CfgCallProceedingRsp_Object = MibTableColumn
uds1CfgCallProceedingRsp = _Uds1CfgCallProceedingRsp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 24),
    _Uds1CfgCallProceedingRsp_Type()
)
uds1CfgCallProceedingRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgCallProceedingRsp.setStatus("mandatory")


class _Uds1CfgAlertingRsp_Type(Integer32):
    """Custom type uds1CfgAlertingRsp based on Integer32"""
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


_Uds1CfgAlertingRsp_Type.__name__ = "Integer32"
_Uds1CfgAlertingRsp_Object = MibTableColumn
uds1CfgAlertingRsp = _Uds1CfgAlertingRsp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 25),
    _Uds1CfgAlertingRsp_Type()
)
uds1CfgAlertingRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgAlertingRsp.setStatus("mandatory")


class _Uds1CfgServiceState_Type(Integer32):
    """Custom type uds1CfgServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("localOutOfService", 3),
          ("notSupported", 1))
    )


_Uds1CfgServiceState_Type.__name__ = "Integer32"
_Uds1CfgServiceState_Object = MibTableColumn
uds1CfgServiceState = _Uds1CfgServiceState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 26),
    _Uds1CfgServiceState_Type()
)
uds1CfgServiceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgServiceState.setStatus("mandatory")


class _Uds1CfgIcbKeyword_Type(DisplayString):
    """Custom type uds1CfgIcbKeyword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Uds1CfgIcbKeyword_Type.__name__ = "DisplayString"
_Uds1CfgIcbKeyword_Object = MibTableColumn
uds1CfgIcbKeyword = _Uds1CfgIcbKeyword_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 27),
    _Uds1CfgIcbKeyword_Type()
)
uds1CfgIcbKeyword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgIcbKeyword.setStatus("mandatory")


class _Uds1CfgOverlapRxMode_Type(Integer32):
    """Custom type uds1CfgOverlapRxMode based on Integer32"""
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


_Uds1CfgOverlapRxMode_Type.__name__ = "Integer32"
_Uds1CfgOverlapRxMode_Object = MibTableColumn
uds1CfgOverlapRxMode = _Uds1CfgOverlapRxMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 28),
    _Uds1CfgOverlapRxMode_Type()
)
uds1CfgOverlapRxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgOverlapRxMode.setStatus("mandatory")


class _Uds1CfgEandMnoAddrTimer_Type(Integer32):
    """Custom type uds1CfgEandMnoAddrTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 125),
    )


_Uds1CfgEandMnoAddrTimer_Type.__name__ = "Integer32"
_Uds1CfgEandMnoAddrTimer_Object = MibTableColumn
uds1CfgEandMnoAddrTimer = _Uds1CfgEandMnoAddrTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 29),
    _Uds1CfgEandMnoAddrTimer_Type()
)
uds1CfgEandMnoAddrTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgEandMnoAddrTimer.setStatus("mandatory")


class _Uds1CfgSeizureWinkDly_Type(Integer32):
    """Custom type uds1CfgSeizureWinkDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Uds1CfgSeizureWinkDly_Type.__name__ = "Integer32"
_Uds1CfgSeizureWinkDly_Object = MibTableColumn
uds1CfgSeizureWinkDly = _Uds1CfgSeizureWinkDly_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 1, 1, 30),
    _Uds1CfgSeizureWinkDly_Type()
)
uds1CfgSeizureWinkDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CfgSeizureWinkDly.setStatus("mandatory")
_Uds1IntervalTable_Object = MibTable
uds1IntervalTable = _Uds1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 2)
)
if mibBuilder.loadTexts:
    uds1IntervalTable.setStatus("mandatory")
_Uds1IntervalEntry_Object = MibTableRow
uds1IntervalEntry = _Uds1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 2, 1)
)
uds1IntervalEntry.setIndexNames(
    (0, "UDS1-MIB", "uds1IntIndex"),
    (0, "UDS1-MIB", "uds1IntNumber"),
)
if mibBuilder.loadTexts:
    uds1IntervalEntry.setStatus("mandatory")
_Uds1IntIndex_Type = Integer32
_Uds1IntIndex_Object = MibTableColumn
uds1IntIndex = _Uds1IntIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 2, 1, 1),
    _Uds1IntIndex_Type()
)
uds1IntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1IntIndex.setStatus("mandatory")
_Uds1IntNumber_Type = Integer32
_Uds1IntNumber_Object = MibTableColumn
uds1IntNumber = _Uds1IntNumber_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 2, 1, 2),
    _Uds1IntNumber_Type()
)
uds1IntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1IntNumber.setStatus("mandatory")
_Uds1IntBurstyErrSeconds_Type = Counter32
_Uds1IntBurstyErrSeconds_Object = MibTableColumn
uds1IntBurstyErrSeconds = _Uds1IntBurstyErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 2, 1, 3),
    _Uds1IntBurstyErrSeconds_Type()
)
uds1IntBurstyErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1IntBurstyErrSeconds.setStatus("mandatory")
_Uds1IntFrameBitErrors_Type = Counter32
_Uds1IntFrameBitErrors_Object = MibTableColumn
uds1IntFrameBitErrors = _Uds1IntFrameBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 2, 1, 4),
    _Uds1IntFrameBitErrors_Type()
)
uds1IntFrameBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1IntFrameBitErrors.setStatus("mandatory")
_Uds1IntDeltaFrameAlligns_Type = Counter32
_Uds1IntDeltaFrameAlligns_Object = MibTableColumn
uds1IntDeltaFrameAlligns = _Uds1IntDeltaFrameAlligns_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 2, 1, 5),
    _Uds1IntDeltaFrameAlligns_Type()
)
uds1IntDeltaFrameAlligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1IntDeltaFrameAlligns.setStatus("mandatory")
_Uds1IntExcessCRCErrors_Type = Counter32
_Uds1IntExcessCRCErrors_Object = MibTableColumn
uds1IntExcessCRCErrors = _Uds1IntExcessCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 2, 1, 6),
    _Uds1IntExcessCRCErrors_Type()
)
uds1IntExcessCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1IntExcessCRCErrors.setStatus("mandatory")
_Uds1CurrentTable_Object = MibTable
uds1CurrentTable = _Uds1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 3)
)
if mibBuilder.loadTexts:
    uds1CurrentTable.setStatus("mandatory")
_Uds1CurrentEntry_Object = MibTableRow
uds1CurrentEntry = _Uds1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 3, 1)
)
uds1CurrentEntry.setIndexNames(
    (0, "UDS1-MIB", "uds1CurrIndex"),
)
if mibBuilder.loadTexts:
    uds1CurrentEntry.setStatus("mandatory")
_Uds1CurrIndex_Type = Integer32
_Uds1CurrIndex_Object = MibTableColumn
uds1CurrIndex = _Uds1CurrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 3, 1, 1),
    _Uds1CurrIndex_Type()
)
uds1CurrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1CurrIndex.setStatus("mandatory")
_Uds1CurrBurstyErrSeconds_Type = Counter32
_Uds1CurrBurstyErrSeconds_Object = MibTableColumn
uds1CurrBurstyErrSeconds = _Uds1CurrBurstyErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 3, 1, 2),
    _Uds1CurrBurstyErrSeconds_Type()
)
uds1CurrBurstyErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1CurrBurstyErrSeconds.setStatus("mandatory")
_Uds1CurrFrameBitErrors_Type = Counter32
_Uds1CurrFrameBitErrors_Object = MibTableColumn
uds1CurrFrameBitErrors = _Uds1CurrFrameBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 3, 1, 3),
    _Uds1CurrFrameBitErrors_Type()
)
uds1CurrFrameBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1CurrFrameBitErrors.setStatus("mandatory")
_Uds1CurrDeltaFrameAlligns_Type = Counter32
_Uds1CurrDeltaFrameAlligns_Object = MibTableColumn
uds1CurrDeltaFrameAlligns = _Uds1CurrDeltaFrameAlligns_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 3, 1, 4),
    _Uds1CurrDeltaFrameAlligns_Type()
)
uds1CurrDeltaFrameAlligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1CurrDeltaFrameAlligns.setStatus("mandatory")
_Uds1CurrExcessCRCErrors_Type = Counter32
_Uds1CurrExcessCRCErrors_Object = MibTableColumn
uds1CurrExcessCRCErrors = _Uds1CurrExcessCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 3, 1, 5),
    _Uds1CurrExcessCRCErrors_Type()
)
uds1CurrExcessCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1CurrExcessCRCErrors.setStatus("mandatory")
_Uds1TotalTable_Object = MibTable
uds1TotalTable = _Uds1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 4)
)
if mibBuilder.loadTexts:
    uds1TotalTable.setStatus("mandatory")
_Uds1TotalEntry_Object = MibTableRow
uds1TotalEntry = _Uds1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 4, 1)
)
uds1TotalEntry.setIndexNames(
    (0, "UDS1-MIB", "uds1TotIndex"),
)
if mibBuilder.loadTexts:
    uds1TotalEntry.setStatus("mandatory")
_Uds1TotIndex_Type = Integer32
_Uds1TotIndex_Object = MibTableColumn
uds1TotIndex = _Uds1TotIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 4, 1, 1),
    _Uds1TotIndex_Type()
)
uds1TotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1TotIndex.setStatus("mandatory")
_Uds1TotBurstyErrSeconds_Type = Counter32
_Uds1TotBurstyErrSeconds_Object = MibTableColumn
uds1TotBurstyErrSeconds = _Uds1TotBurstyErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 4, 1, 2),
    _Uds1TotBurstyErrSeconds_Type()
)
uds1TotBurstyErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1TotBurstyErrSeconds.setStatus("mandatory")
_Uds1TotFrameBitErrors_Type = Counter32
_Uds1TotFrameBitErrors_Object = MibTableColumn
uds1TotFrameBitErrors = _Uds1TotFrameBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 4, 1, 3),
    _Uds1TotFrameBitErrors_Type()
)
uds1TotFrameBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1TotFrameBitErrors.setStatus("mandatory")
_Uds1TotDeltaFrameAlligns_Type = Counter32
_Uds1TotDeltaFrameAlligns_Object = MibTableColumn
uds1TotDeltaFrameAlligns = _Uds1TotDeltaFrameAlligns_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 4, 1, 4),
    _Uds1TotDeltaFrameAlligns_Type()
)
uds1TotDeltaFrameAlligns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1TotDeltaFrameAlligns.setStatus("mandatory")
_Uds1TotExcessCRCErrors_Type = Counter32
_Uds1TotExcessCRCErrors_Object = MibTableColumn
uds1TotExcessCRCErrors = _Uds1TotExcessCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 4, 1, 5),
    _Uds1TotExcessCRCErrors_Type()
)
uds1TotExcessCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1TotExcessCRCErrors.setStatus("mandatory")
_Uds1StatTable_Object = MibTable
uds1StatTable = _Uds1StatTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5)
)
if mibBuilder.loadTexts:
    uds1StatTable.setStatus("mandatory")
_Uds1StatEntry_Object = MibTableRow
uds1StatEntry = _Uds1StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1)
)
uds1StatEntry.setIndexNames(
    (0, "UDS1-MIB", "uds1StatIndex"),
)
if mibBuilder.loadTexts:
    uds1StatEntry.setStatus("mandatory")
_Uds1StatIndex_Type = Integer32
_Uds1StatIndex_Object = MibTableColumn
uds1StatIndex = _Uds1StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 1),
    _Uds1StatIndex_Type()
)
uds1StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatIndex.setStatus("mandatory")


class _Uds1StatReceiverGain_Type(Integer32):
    """Custom type uds1StatReceiverGain based on Integer32"""
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
        *(("dB0", 1),
          ("dB15", 3),
          ("dB22", 4),
          ("dB7", 2),
          ("notApplicable", 5))
    )


_Uds1StatReceiverGain_Type.__name__ = "Integer32"
_Uds1StatReceiverGain_Object = MibTableColumn
uds1StatReceiverGain = _Uds1StatReceiverGain_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 2),
    _Uds1StatReceiverGain_Type()
)
uds1StatReceiverGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatReceiverGain.setStatus("mandatory")


class _Uds1StatOutOfFrame_Type(Integer32):
    """Custom type uds1StatOutOfFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Uds1StatOutOfFrame_Type.__name__ = "Integer32"
_Uds1StatOutOfFrame_Object = MibTableColumn
uds1StatOutOfFrame = _Uds1StatOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 3),
    _Uds1StatOutOfFrame_Type()
)
uds1StatOutOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatOutOfFrame.setStatus("mandatory")


class _Uds1StatLossOfSignal_Type(Integer32):
    """Custom type uds1StatLossOfSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Uds1StatLossOfSignal_Type.__name__ = "Integer32"
_Uds1StatLossOfSignal_Object = MibTableColumn
uds1StatLossOfSignal = _Uds1StatLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 4),
    _Uds1StatLossOfSignal_Type()
)
uds1StatLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatLossOfSignal.setStatus("mandatory")


class _Uds1StatReceivingAIS_Type(Integer32):
    """Custom type uds1StatReceivingAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Uds1StatReceivingAIS_Type.__name__ = "Integer32"
_Uds1StatReceivingAIS_Object = MibTableColumn
uds1StatReceivingAIS = _Uds1StatReceivingAIS_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 5),
    _Uds1StatReceivingAIS_Type()
)
uds1StatReceivingAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatReceivingAIS.setStatus("mandatory")


class _Uds1StatSwitchTypeActive_Type(Integer32):
    """Custom type uds1StatSwitchTypeActive based on Integer32"""
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
        *(("priSw4ESS", 1),
          ("priSw5ESS", 2),
          ("priSwDASS2", 8),
          ("priSwDMS100", 3),
          ("priSwICTR4", 4),
          ("priSwINS1500", 7),
          ("priSwNI2", 6),
          ("priSwTSO14", 9),
          ("priSwVn4", 5))
    )


_Uds1StatSwitchTypeActive_Type.__name__ = "Integer32"
_Uds1StatSwitchTypeActive_Object = MibTableColumn
uds1StatSwitchTypeActive = _Uds1StatSwitchTypeActive_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 6),
    _Uds1StatSwitchTypeActive_Type()
)
uds1StatSwitchTypeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatSwitchTypeActive.setStatus("mandatory")


class _Uds1StatDchanOperational_Type(Integer32):
    """Custom type uds1StatDchanOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bChannel", 3),
          ("dChannelDown", 2),
          ("dChannelUp", 1))
    )


_Uds1StatDchanOperational_Type.__name__ = "Integer32"
_Uds1StatDchanOperational_Object = MibTableColumn
uds1StatDchanOperational = _Uds1StatDchanOperational_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 7),
    _Uds1StatDchanOperational_Type()
)
uds1StatDchanOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatDchanOperational.setStatus("mandatory")


class _Uds1StatE1ContCrc_Type(Integer32):
    """Custom type uds1StatE1ContCrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Uds1StatE1ContCrc_Type.__name__ = "Integer32"
_Uds1StatE1ContCrc_Object = MibTableColumn
uds1StatE1ContCrc = _Uds1StatE1ContCrc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 8),
    _Uds1StatE1ContCrc_Type()
)
uds1StatE1ContCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatE1ContCrc.setStatus("mandatory")


class _Uds1StatE1PhysicalState_Type(Integer32):
    """Custom type uds1StatE1PhysicalState based on Integer32"""
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
        *(("psF1Operational", 1),
          ("psF2Fc1RaiTempCrcErrors", 2),
          ("psF3Fc2LossOfSignal", 3),
          ("psF4Fc3AlarmIndSignal", 4),
          ("psF5Fc4RaiContCrcErrors", 5),
          ("psF6PowerOn", 6))
    )


_Uds1StatE1PhysicalState_Type.__name__ = "Integer32"
_Uds1StatE1PhysicalState_Object = MibTableColumn
uds1StatE1PhysicalState = _Uds1StatE1PhysicalState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 9),
    _Uds1StatE1PhysicalState_Type()
)
uds1StatE1PhysicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatE1PhysicalState.setStatus("mandatory")


class _Uds1StatLoopBackInit_Type(Integer32):
    """Custom type uds1StatLoopBackInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("command", 3),
          ("network", 2),
          ("none", 1))
    )


_Uds1StatLoopBackInit_Type.__name__ = "Integer32"
_Uds1StatLoopBackInit_Object = MibTableColumn
uds1StatLoopBackInit = _Uds1StatLoopBackInit_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 10),
    _Uds1StatLoopBackInit_Type()
)
uds1StatLoopBackInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatLoopBackInit.setStatus("mandatory")


class _Uds1StatNfasDChannel_Type(Integer32):
    """Custom type uds1StatNfasDChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dchannel", 2),
          ("extraBchannel", 3),
          ("notSupported", 1))
    )


_Uds1StatNfasDChannel_Type.__name__ = "Integer32"
_Uds1StatNfasDChannel_Object = MibTableColumn
uds1StatNfasDChannel = _Uds1StatNfasDChannel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 11),
    _Uds1StatNfasDChannel_Type()
)
uds1StatNfasDChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatNfasDChannel.setStatus("mandatory")


class _Uds1StatDChannel_Type(Integer32):
    """Custom type uds1StatDChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bChannel", 3),
          ("inService", 2),
          ("notSupported", 1))
    )


_Uds1StatDChannel_Type.__name__ = "Integer32"
_Uds1StatDChannel_Object = MibTableColumn
uds1StatDChannel = _Uds1StatDChannel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 12),
    _Uds1StatDChannel_Type()
)
uds1StatDChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatDChannel.setStatus("mandatory")


class _Uds1StatDs0SrvcChngLst_Type(DisplayString):
    """Custom type uds1StatDs0SrvcChngLst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_Uds1StatDs0SrvcChngLst_Type.__name__ = "DisplayString"
_Uds1StatDs0SrvcChngLst_Object = MibTableColumn
uds1StatDs0SrvcChngLst = _Uds1StatDs0SrvcChngLst_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 13),
    _Uds1StatDs0SrvcChngLst_Type()
)
uds1StatDs0SrvcChngLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatDs0SrvcChngLst.setStatus("mandatory")


class _Uds1StatMultiFrame_Type(Integer32):
    """Custom type uds1StatMultiFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Uds1StatMultiFrame_Type.__name__ = "Integer32"
_Uds1StatMultiFrame_Object = MibTableColumn
uds1StatMultiFrame = _Uds1StatMultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 14),
    _Uds1StatMultiFrame_Type()
)
uds1StatMultiFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatMultiFrame.setStatus("mandatory")


class _Uds1StatRemMultiFrame_Type(Integer32):
    """Custom type uds1StatRemMultiFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Uds1StatRemMultiFrame_Type.__name__ = "Integer32"
_Uds1StatRemMultiFrame_Object = MibTableColumn
uds1StatRemMultiFrame = _Uds1StatRemMultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 15),
    _Uds1StatRemMultiFrame_Type()
)
uds1StatRemMultiFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatRemMultiFrame.setStatus("mandatory")


class _Uds1StatServiceState_Type(Integer32):
    """Custom type uds1StatServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("localOutOfService", 3),
          ("notSupported", 1))
    )


_Uds1StatServiceState_Type.__name__ = "Integer32"
_Uds1StatServiceState_Object = MibTableColumn
uds1StatServiceState = _Uds1StatServiceState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 5, 1, 16),
    _Uds1StatServiceState_Type()
)
uds1StatServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1StatServiceState.setStatus("mandatory")
_Uds1CmdTable_Object = MibTable
uds1CmdTable = _Uds1CmdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 6)
)
if mibBuilder.loadTexts:
    uds1CmdTable.setStatus("mandatory")
_Uds1CmdEntry_Object = MibTableRow
uds1CmdEntry = _Uds1CmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 6, 1)
)
uds1CmdEntry.setIndexNames(
    (0, "UDS1-MIB", "uds1CmdIndex"),
)
if mibBuilder.loadTexts:
    uds1CmdEntry.setStatus("mandatory")
_Uds1CmdIndex_Type = Integer32
_Uds1CmdIndex_Object = MibTableColumn
uds1CmdIndex = _Uds1CmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 6, 1, 1),
    _Uds1CmdIndex_Type()
)
uds1CmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1CmdIndex.setStatus("mandatory")


class _Uds1CmdMgtStationId_Type(OctetString):
    """Custom type uds1CmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Uds1CmdMgtStationId_Type.__name__ = "OctetString"
_Uds1CmdMgtStationId_Object = MibTableColumn
uds1CmdMgtStationId = _Uds1CmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 6, 1, 2),
    _Uds1CmdMgtStationId_Type()
)
uds1CmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CmdMgtStationId.setStatus("mandatory")
_Uds1CmdReqId_Type = Integer32
_Uds1CmdReqId_Object = MibTableColumn
uds1CmdReqId = _Uds1CmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 6, 1, 3),
    _Uds1CmdReqId_Type()
)
uds1CmdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1CmdReqId.setStatus("mandatory")


class _Uds1CmdFunction_Type(Integer32):
    """Custom type uds1CmdFunction based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("blockAllCalls", 9),
          ("blockAnalogCalls", 7),
          ("blockDigitalCalls", 8),
          ("blockNoCalls", 10),
          ("bringUpDChannel", 13),
          ("enterLoopback", 3),
          ("exitLoopback", 4),
          ("forceReceiverReframe", 2),
          ("inService", 5),
          ("localOutOfService", 6),
          ("noCommand", 1),
          ("redAlarmOverride", 11),
          ("takeDownDChannel", 12))
    )


_Uds1CmdFunction_Type.__name__ = "Integer32"
_Uds1CmdFunction_Object = MibTableColumn
uds1CmdFunction = _Uds1CmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 6, 1, 4),
    _Uds1CmdFunction_Type()
)
uds1CmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CmdFunction.setStatus("mandatory")


class _Uds1CmdForce_Type(Integer32):
    """Custom type uds1CmdForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("noForce", 2))
    )


_Uds1CmdForce_Type.__name__ = "Integer32"
_Uds1CmdForce_Object = MibTableColumn
uds1CmdForce = _Uds1CmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 6, 1, 5),
    _Uds1CmdForce_Type()
)
uds1CmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CmdForce.setStatus("mandatory")


class _Uds1CmdParam_Type(OctetString):
    """Custom type uds1CmdParam based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Uds1CmdParam_Type.__name__ = "OctetString"
_Uds1CmdParam_Object = MibTableColumn
uds1CmdParam = _Uds1CmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 6, 1, 6),
    _Uds1CmdParam_Type()
)
uds1CmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1CmdParam.setStatus("mandatory")


class _Uds1CmdResult_Type(Integer32):
    """Custom type uds1CmdResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_Uds1CmdResult_Type.__name__ = "Integer32"
_Uds1CmdResult_Object = MibTableColumn
uds1CmdResult = _Uds1CmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 6, 1, 7),
    _Uds1CmdResult_Type()
)
uds1CmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1CmdResult.setStatus("mandatory")


class _Uds1CmdCode_Type(Integer32):
    """Custom type uds1CmdCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8,
              12,
              20,
              22,
              73)
        )
    )
    namedValues = NamedValues(
        *(("deviceDisabled", 22),
          ("noError", 1),
          ("noResponse", 12),
          ("pendingSoftwareDownload", 73),
          ("slotEmpty", 8),
          ("unable", 2),
          ("unrecognizedCommand", 6),
          ("unsupportedCommand", 20))
    )


_Uds1CmdCode_Type.__name__ = "Integer32"
_Uds1CmdCode_Object = MibTableColumn
uds1CmdCode = _Uds1CmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 6, 1, 8),
    _Uds1CmdCode_Type()
)
uds1CmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1CmdCode.setStatus("mandatory")
_Uds1TrapEnaTable_Object = MibTable
uds1TrapEnaTable = _Uds1TrapEnaTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7)
)
if mibBuilder.loadTexts:
    uds1TrapEnaTable.setStatus("mandatory")
_Uds1TrapEnaEntry_Object = MibTableRow
uds1TrapEnaEntry = _Uds1TrapEnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1)
)
uds1TrapEnaEntry.setIndexNames(
    (0, "UDS1-MIB", "uds1TrapEnaIndex"),
)
if mibBuilder.loadTexts:
    uds1TrapEnaEntry.setStatus("mandatory")
_Uds1TrapEnaIndex_Type = Integer32
_Uds1TrapEnaIndex_Object = MibTableColumn
uds1TrapEnaIndex = _Uds1TrapEnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 1),
    _Uds1TrapEnaIndex_Type()
)
uds1TrapEnaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uds1TrapEnaIndex.setStatus("mandatory")


class _Uds1TrapEnaYellowAlarm_Type(Integer32):
    """Custom type uds1TrapEnaYellowAlarm based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaYellowAlarm_Type.__name__ = "Integer32"
_Uds1TrapEnaYellowAlarm_Object = MibTableColumn
uds1TrapEnaYellowAlarm = _Uds1TrapEnaYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 2),
    _Uds1TrapEnaYellowAlarm_Type()
)
uds1TrapEnaYellowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaYellowAlarm.setStatus("mandatory")


class _Uds1TrapEnaRedAlarm_Type(Integer32):
    """Custom type uds1TrapEnaRedAlarm based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaRedAlarm_Type.__name__ = "Integer32"
_Uds1TrapEnaRedAlarm_Object = MibTableColumn
uds1TrapEnaRedAlarm = _Uds1TrapEnaRedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 3),
    _Uds1TrapEnaRedAlarm_Type()
)
uds1TrapEnaRedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaRedAlarm.setStatus("mandatory")


class _Uds1TrapEnaLossOfSignal_Type(Integer32):
    """Custom type uds1TrapEnaLossOfSignal based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaLossOfSignal_Type.__name__ = "Integer32"
_Uds1TrapEnaLossOfSignal_Object = MibTableColumn
uds1TrapEnaLossOfSignal = _Uds1TrapEnaLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 4),
    _Uds1TrapEnaLossOfSignal_Type()
)
uds1TrapEnaLossOfSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaLossOfSignal.setStatus("mandatory")


class _Uds1TrapEnaAlarmIndSignal_Type(Integer32):
    """Custom type uds1TrapEnaAlarmIndSignal based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaAlarmIndSignal_Type.__name__ = "Integer32"
_Uds1TrapEnaAlarmIndSignal_Object = MibTableColumn
uds1TrapEnaAlarmIndSignal = _Uds1TrapEnaAlarmIndSignal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 5),
    _Uds1TrapEnaAlarmIndSignal_Type()
)
uds1TrapEnaAlarmIndSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaAlarmIndSignal.setStatus("mandatory")


class _Uds1TrapEnaYellowAlarmClr_Type(Integer32):
    """Custom type uds1TrapEnaYellowAlarmClr based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaYellowAlarmClr_Type.__name__ = "Integer32"
_Uds1TrapEnaYellowAlarmClr_Object = MibTableColumn
uds1TrapEnaYellowAlarmClr = _Uds1TrapEnaYellowAlarmClr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 6),
    _Uds1TrapEnaYellowAlarmClr_Type()
)
uds1TrapEnaYellowAlarmClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaYellowAlarmClr.setStatus("mandatory")


class _Uds1TrapEnaRedAlarmClr_Type(Integer32):
    """Custom type uds1TrapEnaRedAlarmClr based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaRedAlarmClr_Type.__name__ = "Integer32"
_Uds1TrapEnaRedAlarmClr_Object = MibTableColumn
uds1TrapEnaRedAlarmClr = _Uds1TrapEnaRedAlarmClr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 7),
    _Uds1TrapEnaRedAlarmClr_Type()
)
uds1TrapEnaRedAlarmClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaRedAlarmClr.setStatus("mandatory")


class _Uds1TrapEnaLossOfSgnlClr_Type(Integer32):
    """Custom type uds1TrapEnaLossOfSgnlClr based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaLossOfSgnlClr_Type.__name__ = "Integer32"
_Uds1TrapEnaLossOfSgnlClr_Object = MibTableColumn
uds1TrapEnaLossOfSgnlClr = _Uds1TrapEnaLossOfSgnlClr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 8),
    _Uds1TrapEnaLossOfSgnlClr_Type()
)
uds1TrapEnaLossOfSgnlClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaLossOfSgnlClr.setStatus("mandatory")


class _Uds1TrapEnaAlrmIndSgnlClr_Type(Integer32):
    """Custom type uds1TrapEnaAlrmIndSgnlClr based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaAlrmIndSgnlClr_Type.__name__ = "Integer32"
_Uds1TrapEnaAlrmIndSgnlClr_Object = MibTableColumn
uds1TrapEnaAlrmIndSgnlClr = _Uds1TrapEnaAlrmIndSgnlClr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 9),
    _Uds1TrapEnaAlrmIndSgnlClr_Type()
)
uds1TrapEnaAlrmIndSgnlClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaAlrmIndSgnlClr.setStatus("mandatory")


class _Uds1TrapEnaContCrcAlrm_Type(Integer32):
    """Custom type uds1TrapEnaContCrcAlrm based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaContCrcAlrm_Type.__name__ = "Integer32"
_Uds1TrapEnaContCrcAlrm_Object = MibTableColumn
uds1TrapEnaContCrcAlrm = _Uds1TrapEnaContCrcAlrm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 10),
    _Uds1TrapEnaContCrcAlrm_Type()
)
uds1TrapEnaContCrcAlrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaContCrcAlrm.setStatus("mandatory")


class _Uds1TrapEnaContCrcAlrmClr_Type(Integer32):
    """Custom type uds1TrapEnaContCrcAlrmClr based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaContCrcAlrmClr_Type.__name__ = "Integer32"
_Uds1TrapEnaContCrcAlrmClr_Object = MibTableColumn
uds1TrapEnaContCrcAlrmClr = _Uds1TrapEnaContCrcAlrmClr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 11),
    _Uds1TrapEnaContCrcAlrmClr_Type()
)
uds1TrapEnaContCrcAlrmClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaContCrcAlrmClr.setStatus("mandatory")


class _Uds1TrapEnaPhysStateChng_Type(Integer32):
    """Custom type uds1TrapEnaPhysStateChng based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaPhysStateChng_Type.__name__ = "Integer32"
_Uds1TrapEnaPhysStateChng_Object = MibTableColumn
uds1TrapEnaPhysStateChng = _Uds1TrapEnaPhysStateChng_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 12),
    _Uds1TrapEnaPhysStateChng_Type()
)
uds1TrapEnaPhysStateChng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaPhysStateChng.setStatus("mandatory")


class _Uds1TrapEnaDchanInSrvc_Type(Integer32):
    """Custom type uds1TrapEnaDchanInSrvc based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaDchanInSrvc_Type.__name__ = "Integer32"
_Uds1TrapEnaDchanInSrvc_Object = MibTableColumn
uds1TrapEnaDchanInSrvc = _Uds1TrapEnaDchanInSrvc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 13),
    _Uds1TrapEnaDchanInSrvc_Type()
)
uds1TrapEnaDchanInSrvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaDchanInSrvc.setStatus("mandatory")


class _Uds1TrapEnaDchanOutOfSrvc_Type(Integer32):
    """Custom type uds1TrapEnaDchanOutOfSrvc based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaDchanOutOfSrvc_Type.__name__ = "Integer32"
_Uds1TrapEnaDchanOutOfSrvc_Object = MibTableColumn
uds1TrapEnaDchanOutOfSrvc = _Uds1TrapEnaDchanOutOfSrvc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 14),
    _Uds1TrapEnaDchanOutOfSrvc_Type()
)
uds1TrapEnaDchanOutOfSrvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaDchanOutOfSrvc.setStatus("mandatory")


class _Uds1TrapEnaDs0InSrvc_Type(Integer32):
    """Custom type uds1TrapEnaDs0InSrvc based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaDs0InSrvc_Type.__name__ = "Integer32"
_Uds1TrapEnaDs0InSrvc_Object = MibTableColumn
uds1TrapEnaDs0InSrvc = _Uds1TrapEnaDs0InSrvc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 15),
    _Uds1TrapEnaDs0InSrvc_Type()
)
uds1TrapEnaDs0InSrvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaDs0InSrvc.setStatus("mandatory")


class _Uds1TrapEnaDs0OutOfSrvc_Type(Integer32):
    """Custom type uds1TrapEnaDs0OutOfSrvc based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaDs0OutOfSrvc_Type.__name__ = "Integer32"
_Uds1TrapEnaDs0OutOfSrvc_Object = MibTableColumn
uds1TrapEnaDs0OutOfSrvc = _Uds1TrapEnaDs0OutOfSrvc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 16),
    _Uds1TrapEnaDs0OutOfSrvc_Type()
)
uds1TrapEnaDs0OutOfSrvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaDs0OutOfSrvc.setStatus("mandatory")


class _Uds1TrapEnaMultiFrame_Type(Integer32):
    """Custom type uds1TrapEnaMultiFrame based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaMultiFrame_Type.__name__ = "Integer32"
_Uds1TrapEnaMultiFrame_Object = MibTableColumn
uds1TrapEnaMultiFrame = _Uds1TrapEnaMultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 17),
    _Uds1TrapEnaMultiFrame_Type()
)
uds1TrapEnaMultiFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaMultiFrame.setStatus("mandatory")


class _Uds1TrapEnaRemMultiFrame_Type(Integer32):
    """Custom type uds1TrapEnaRemMultiFrame based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaRemMultiFrame_Type.__name__ = "Integer32"
_Uds1TrapEnaRemMultiFrame_Object = MibTableColumn
uds1TrapEnaRemMultiFrame = _Uds1TrapEnaRemMultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 18),
    _Uds1TrapEnaRemMultiFrame_Type()
)
uds1TrapEnaRemMultiFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaRemMultiFrame.setStatus("mandatory")


class _Uds1TrapEnaMultiFrmClr_Type(Integer32):
    """Custom type uds1TrapEnaMultiFrmClr based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaMultiFrmClr_Type.__name__ = "Integer32"
_Uds1TrapEnaMultiFrmClr_Object = MibTableColumn
uds1TrapEnaMultiFrmClr = _Uds1TrapEnaMultiFrmClr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 19),
    _Uds1TrapEnaMultiFrmClr_Type()
)
uds1TrapEnaMultiFrmClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaMultiFrmClr.setStatus("mandatory")


class _Uds1TrapEnaRemMultiFrmClr_Type(Integer32):
    """Custom type uds1TrapEnaRemMultiFrmClr based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Uds1TrapEnaRemMultiFrmClr_Type.__name__ = "Integer32"
_Uds1TrapEnaRemMultiFrmClr_Object = MibTableColumn
uds1TrapEnaRemMultiFrmClr = _Uds1TrapEnaRemMultiFrmClr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 4, 7, 1, 20),
    _Uds1TrapEnaRemMultiFrmClr_Type()
)
uds1TrapEnaRemMultiFrmClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uds1TrapEnaRemMultiFrmClr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UDS1-MIB",
    **{"usr": usr,
       "nas": nas,
       "uds1": uds1,
       "uds1ConfigTable": uds1ConfigTable,
       "uds1ConfigEntry": uds1ConfigEntry,
       "uds1CfgIndex": uds1CfgIndex,
       "uds1CfgRespToRemoteLoopbk": uds1CfgRespToRemoteLoopbk,
       "uds1CfgJitterAttenuation": uds1CfgJitterAttenuation,
       "uds1CfgXmitLineBuildOut": uds1CfgXmitLineBuildOut,
       "uds1CfgAutoBusyEnable": uds1CfgAutoBusyEnable,
       "uds1CfgDialInAdr": uds1CfgDialInAdr,
       "uds1CfgZeroCoding": uds1CfgZeroCoding,
       "uds1CfgDialInOutTrunkSt": uds1CfgDialInOutTrunkSt,
       "uds1CfgDialInAdrAckWinkEn": uds1CfgDialInAdrAckWinkEn,
       "uds1CfgDialOutAdrDly": uds1CfgDialOutAdrDly,
       "uds1CfgStuffByteValue": uds1CfgStuffByteValue,
       "uds1CfgDialInOutTrunkType": uds1CfgDialInOutTrunkType,
       "uds1CfgPriSwitchType": uds1CfgPriSwitchType,
       "uds1CfgIdleByte": uds1CfgIdleByte,
       "uds1CfgAnlgBlockErrCode": uds1CfgAnlgBlockErrCode,
       "uds1CfgDgtlBlockErrCode": uds1CfgDgtlBlockErrCode,
       "uds1CfgNoMdmAvailErrCode": uds1CfgNoMdmAvailErrCode,
       "uds1CfgNoIgwsAvailErrCode": uds1CfgNoIgwsAvailErrCode,
       "uds1CfgChanBlockErrCode": uds1CfgChanBlockErrCode,
       "uds1CfgBlockCallType": uds1CfgBlockCallType,
       "uds1CfgNfasId": uds1CfgNfasId,
       "uds1CfgNfasDChannel": uds1CfgNfasDChannel,
       "uds1CfgShrtHaulDist": uds1CfgShrtHaulDist,
       "uds1CfgCallProceedingRsp": uds1CfgCallProceedingRsp,
       "uds1CfgAlertingRsp": uds1CfgAlertingRsp,
       "uds1CfgServiceState": uds1CfgServiceState,
       "uds1CfgIcbKeyword": uds1CfgIcbKeyword,
       "uds1CfgOverlapRxMode": uds1CfgOverlapRxMode,
       "uds1CfgEandMnoAddrTimer": uds1CfgEandMnoAddrTimer,
       "uds1CfgSeizureWinkDly": uds1CfgSeizureWinkDly,
       "uds1IntervalTable": uds1IntervalTable,
       "uds1IntervalEntry": uds1IntervalEntry,
       "uds1IntIndex": uds1IntIndex,
       "uds1IntNumber": uds1IntNumber,
       "uds1IntBurstyErrSeconds": uds1IntBurstyErrSeconds,
       "uds1IntFrameBitErrors": uds1IntFrameBitErrors,
       "uds1IntDeltaFrameAlligns": uds1IntDeltaFrameAlligns,
       "uds1IntExcessCRCErrors": uds1IntExcessCRCErrors,
       "uds1CurrentTable": uds1CurrentTable,
       "uds1CurrentEntry": uds1CurrentEntry,
       "uds1CurrIndex": uds1CurrIndex,
       "uds1CurrBurstyErrSeconds": uds1CurrBurstyErrSeconds,
       "uds1CurrFrameBitErrors": uds1CurrFrameBitErrors,
       "uds1CurrDeltaFrameAlligns": uds1CurrDeltaFrameAlligns,
       "uds1CurrExcessCRCErrors": uds1CurrExcessCRCErrors,
       "uds1TotalTable": uds1TotalTable,
       "uds1TotalEntry": uds1TotalEntry,
       "uds1TotIndex": uds1TotIndex,
       "uds1TotBurstyErrSeconds": uds1TotBurstyErrSeconds,
       "uds1TotFrameBitErrors": uds1TotFrameBitErrors,
       "uds1TotDeltaFrameAlligns": uds1TotDeltaFrameAlligns,
       "uds1TotExcessCRCErrors": uds1TotExcessCRCErrors,
       "uds1StatTable": uds1StatTable,
       "uds1StatEntry": uds1StatEntry,
       "uds1StatIndex": uds1StatIndex,
       "uds1StatReceiverGain": uds1StatReceiverGain,
       "uds1StatOutOfFrame": uds1StatOutOfFrame,
       "uds1StatLossOfSignal": uds1StatLossOfSignal,
       "uds1StatReceivingAIS": uds1StatReceivingAIS,
       "uds1StatSwitchTypeActive": uds1StatSwitchTypeActive,
       "uds1StatDchanOperational": uds1StatDchanOperational,
       "uds1StatE1ContCrc": uds1StatE1ContCrc,
       "uds1StatE1PhysicalState": uds1StatE1PhysicalState,
       "uds1StatLoopBackInit": uds1StatLoopBackInit,
       "uds1StatNfasDChannel": uds1StatNfasDChannel,
       "uds1StatDChannel": uds1StatDChannel,
       "uds1StatDs0SrvcChngLst": uds1StatDs0SrvcChngLst,
       "uds1StatMultiFrame": uds1StatMultiFrame,
       "uds1StatRemMultiFrame": uds1StatRemMultiFrame,
       "uds1StatServiceState": uds1StatServiceState,
       "uds1CmdTable": uds1CmdTable,
       "uds1CmdEntry": uds1CmdEntry,
       "uds1CmdIndex": uds1CmdIndex,
       "uds1CmdMgtStationId": uds1CmdMgtStationId,
       "uds1CmdReqId": uds1CmdReqId,
       "uds1CmdFunction": uds1CmdFunction,
       "uds1CmdForce": uds1CmdForce,
       "uds1CmdParam": uds1CmdParam,
       "uds1CmdResult": uds1CmdResult,
       "uds1CmdCode": uds1CmdCode,
       "uds1TrapEnaTable": uds1TrapEnaTable,
       "uds1TrapEnaEntry": uds1TrapEnaEntry,
       "uds1TrapEnaIndex": uds1TrapEnaIndex,
       "uds1TrapEnaYellowAlarm": uds1TrapEnaYellowAlarm,
       "uds1TrapEnaRedAlarm": uds1TrapEnaRedAlarm,
       "uds1TrapEnaLossOfSignal": uds1TrapEnaLossOfSignal,
       "uds1TrapEnaAlarmIndSignal": uds1TrapEnaAlarmIndSignal,
       "uds1TrapEnaYellowAlarmClr": uds1TrapEnaYellowAlarmClr,
       "uds1TrapEnaRedAlarmClr": uds1TrapEnaRedAlarmClr,
       "uds1TrapEnaLossOfSgnlClr": uds1TrapEnaLossOfSgnlClr,
       "uds1TrapEnaAlrmIndSgnlClr": uds1TrapEnaAlrmIndSgnlClr,
       "uds1TrapEnaContCrcAlrm": uds1TrapEnaContCrcAlrm,
       "uds1TrapEnaContCrcAlrmClr": uds1TrapEnaContCrcAlrmClr,
       "uds1TrapEnaPhysStateChng": uds1TrapEnaPhysStateChng,
       "uds1TrapEnaDchanInSrvc": uds1TrapEnaDchanInSrvc,
       "uds1TrapEnaDchanOutOfSrvc": uds1TrapEnaDchanOutOfSrvc,
       "uds1TrapEnaDs0InSrvc": uds1TrapEnaDs0InSrvc,
       "uds1TrapEnaDs0OutOfSrvc": uds1TrapEnaDs0OutOfSrvc,
       "uds1TrapEnaMultiFrame": uds1TrapEnaMultiFrame,
       "uds1TrapEnaRemMultiFrame": uds1TrapEnaRemMultiFrame,
       "uds1TrapEnaMultiFrmClr": uds1TrapEnaMultiFrmClr,
       "uds1TrapEnaRemMultiFrmClr": uds1TrapEnaRemMultiFrmClr}
)
