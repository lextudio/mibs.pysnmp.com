# SNMP MIB module (H3C-VOICE-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-VOICE-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:47 2024
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

(AbsoluteCounter32,) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "AbsoluteCounter32")

(h3cVoice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cVoice")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cVoiceEntityControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14)
)
h3cVoiceEntityControl.setRevisions(
        ("2009-04-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cCodecType(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 1),
          ("g711u", 2),
          ("g723r53", 3),
          ("g723r63", 4),
          ("g726r16", 7),
          ("g726r24", 8),
          ("g726r32", 9),
          ("g726r40", 10),
          ("g729a", 6),
          ("g729br8", 12),
          ("g729r8", 5),
          ("unknown", 11))
    )



class H3cOutBandMode(Integer32, TextualConvention):
    status = "current"
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
        *(("h225", 3),
          ("h245AlphaNumeric", 2),
          ("nte", 5),
          ("sip", 4),
          ("vofr", 6),
          ("voice", 1))
    )



class H3cFaxProtocolType(Integer32, TextualConvention):
    status = "current"
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
        *(("pcmG711alaw", 3),
          ("pcmG711ulaw", 4),
          ("standardt38", 2),
          ("t38", 1))
    )



class H3cFaxBaudrateType(Integer32, TextualConvention):
    status = "current"
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
        *(("b14400", 6),
          ("b2400", 3),
          ("b4800", 4),
          ("b9600", 5),
          ("disable", 1),
          ("voice", 2))
    )



class H3cFaxTrainMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("ppp", 2))
    )



class H3cRegisterdStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("login", 4),
          ("logout", 5),
          ("offline", 2),
          ("online", 3),
          ("other", 1))
    )



# MIB Managed Objects in the order of their OIDs

_H3cVoEntityObjects_ObjectIdentity = ObjectIdentity
h3cVoEntityObjects = _H3cVoEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1)
)
_H3cVoEntityCreateTable_Object = MibTable
h3cVoEntityCreateTable = _H3cVoEntityCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVoEntityCreateTable.setStatus("current")
_H3cVoEntityCreateEntry_Object = MibTableRow
h3cVoEntityCreateEntry = _H3cVoEntityCreateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 1, 1)
)
h3cVoEntityCreateEntry.setIndexNames(
    (0, "H3C-VOICE-DIAL-CONTROL-MIB", "h3cVoEntityIndex"),
)
if mibBuilder.loadTexts:
    h3cVoEntityCreateEntry.setStatus("current")


class _H3cVoEntityIndex_Type(Integer32):
    """Custom type h3cVoEntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoEntityIndex_Type.__name__ = "Integer32"
_H3cVoEntityIndex_Object = MibTableColumn
h3cVoEntityIndex = _H3cVoEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 1, 1, 1),
    _H3cVoEntityIndex_Type()
)
h3cVoEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoEntityIndex.setStatus("current")


class _H3cVoEntityType_Type(Integer32):
    """Custom type h3cVoEntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pots", 1),
          ("vofr", 3),
          ("voip", 2))
    )


_H3cVoEntityType_Type.__name__ = "Integer32"
_H3cVoEntityType_Object = MibTableColumn
h3cVoEntityType = _H3cVoEntityType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 1, 1, 2),
    _H3cVoEntityType_Type()
)
h3cVoEntityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoEntityType.setStatus("current")
_H3cVoEntityRowStatus_Type = RowStatus
_H3cVoEntityRowStatus_Object = MibTableColumn
h3cVoEntityRowStatus = _H3cVoEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 1, 1, 3),
    _H3cVoEntityRowStatus_Type()
)
h3cVoEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoEntityRowStatus.setStatus("current")
_H3cVoEntityCommonConfigTable_Object = MibTable
h3cVoEntityCommonConfigTable = _H3cVoEntityCommonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2)
)
if mibBuilder.loadTexts:
    h3cVoEntityCommonConfigTable.setStatus("current")
_H3cVoEntityCommonConfigEntry_Object = MibTableRow
h3cVoEntityCommonConfigEntry = _H3cVoEntityCommonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1)
)
h3cVoEntityCommonConfigEntry.setIndexNames(
    (0, "H3C-VOICE-DIAL-CONTROL-MIB", "h3cVoEntityCfgIndex"),
)
if mibBuilder.loadTexts:
    h3cVoEntityCommonConfigEntry.setStatus("current")


class _H3cVoEntityCfgIndex_Type(Integer32):
    """Custom type h3cVoEntityCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoEntityCfgIndex_Type.__name__ = "Integer32"
_H3cVoEntityCfgIndex_Object = MibTableColumn
h3cVoEntityCfgIndex = _H3cVoEntityCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 1),
    _H3cVoEntityCfgIndex_Type()
)
h3cVoEntityCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoEntityCfgIndex.setStatus("current")
_H3cVoEntityCfgCodec1st_Type = H3cCodecType
_H3cVoEntityCfgCodec1st_Object = MibTableColumn
h3cVoEntityCfgCodec1st = _H3cVoEntityCfgCodec1st_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 2),
    _H3cVoEntityCfgCodec1st_Type()
)
h3cVoEntityCfgCodec1st.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgCodec1st.setStatus("current")
_H3cVoEntityCfgCodec2nd_Type = H3cCodecType
_H3cVoEntityCfgCodec2nd_Object = MibTableColumn
h3cVoEntityCfgCodec2nd = _H3cVoEntityCfgCodec2nd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 3),
    _H3cVoEntityCfgCodec2nd_Type()
)
h3cVoEntityCfgCodec2nd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgCodec2nd.setStatus("current")
_H3cVoEntityCfgCodec3rd_Type = H3cCodecType
_H3cVoEntityCfgCodec3rd_Object = MibTableColumn
h3cVoEntityCfgCodec3rd = _H3cVoEntityCfgCodec3rd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 4),
    _H3cVoEntityCfgCodec3rd_Type()
)
h3cVoEntityCfgCodec3rd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgCodec3rd.setStatus("current")
_H3cVoEntityCfgCodec4th_Type = H3cCodecType
_H3cVoEntityCfgCodec4th_Object = MibTableColumn
h3cVoEntityCfgCodec4th = _H3cVoEntityCfgCodec4th_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 5),
    _H3cVoEntityCfgCodec4th_Type()
)
h3cVoEntityCfgCodec4th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgCodec4th.setStatus("current")


class _H3cVoEntityCfgDSCP_Type(Integer32):
    """Custom type h3cVoEntityCfgDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cVoEntityCfgDSCP_Type.__name__ = "Integer32"
_H3cVoEntityCfgDSCP_Object = MibTableColumn
h3cVoEntityCfgDSCP = _H3cVoEntityCfgDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 6),
    _H3cVoEntityCfgDSCP_Type()
)
h3cVoEntityCfgDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgDSCP.setStatus("current")
_H3cVoEntityCfgVADEnable_Type = TruthValue
_H3cVoEntityCfgVADEnable_Object = MibTableColumn
h3cVoEntityCfgVADEnable = _H3cVoEntityCfgVADEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 7),
    _H3cVoEntityCfgVADEnable_Type()
)
h3cVoEntityCfgVADEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgVADEnable.setStatus("current")
_H3cVoEntityCfgOutbandMode_Type = H3cOutBandMode
_H3cVoEntityCfgOutbandMode_Object = MibTableColumn
h3cVoEntityCfgOutbandMode = _H3cVoEntityCfgOutbandMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 8),
    _H3cVoEntityCfgOutbandMode_Type()
)
h3cVoEntityCfgOutbandMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgOutbandMode.setStatus("current")


class _H3cVoEntityCfgFaxLevel_Type(Integer32):
    """Custom type h3cVoEntityCfgFaxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, -3),
    )


_H3cVoEntityCfgFaxLevel_Type.__name__ = "Integer32"
_H3cVoEntityCfgFaxLevel_Object = MibTableColumn
h3cVoEntityCfgFaxLevel = _H3cVoEntityCfgFaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 9),
    _H3cVoEntityCfgFaxLevel_Type()
)
h3cVoEntityCfgFaxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgFaxLevel.setStatus("current")
_H3cVoEntityCfgFaxBaudrate_Type = H3cFaxBaudrateType
_H3cVoEntityCfgFaxBaudrate_Object = MibTableColumn
h3cVoEntityCfgFaxBaudrate = _H3cVoEntityCfgFaxBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 10),
    _H3cVoEntityCfgFaxBaudrate_Type()
)
h3cVoEntityCfgFaxBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgFaxBaudrate.setStatus("current")


class _H3cVoEntityCfgFaxLocalTrainPara_Type(Integer32):
    """Custom type h3cVoEntityCfgFaxLocalTrainPara based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cVoEntityCfgFaxLocalTrainPara_Type.__name__ = "Integer32"
_H3cVoEntityCfgFaxLocalTrainPara_Object = MibTableColumn
h3cVoEntityCfgFaxLocalTrainPara = _H3cVoEntityCfgFaxLocalTrainPara_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 11),
    _H3cVoEntityCfgFaxLocalTrainPara_Type()
)
h3cVoEntityCfgFaxLocalTrainPara.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgFaxLocalTrainPara.setStatus("current")
_H3cVoEntityCfgFaxProtocol_Type = H3cFaxProtocolType
_H3cVoEntityCfgFaxProtocol_Object = MibTableColumn
h3cVoEntityCfgFaxProtocol = _H3cVoEntityCfgFaxProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 12),
    _H3cVoEntityCfgFaxProtocol_Type()
)
h3cVoEntityCfgFaxProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgFaxProtocol.setStatus("current")


class _H3cVoEntityCfgFaxHRPackNum_Type(Integer32):
    """Custom type h3cVoEntityCfgFaxHRPackNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_H3cVoEntityCfgFaxHRPackNum_Type.__name__ = "Integer32"
_H3cVoEntityCfgFaxHRPackNum_Object = MibTableColumn
h3cVoEntityCfgFaxHRPackNum = _H3cVoEntityCfgFaxHRPackNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 13),
    _H3cVoEntityCfgFaxHRPackNum_Type()
)
h3cVoEntityCfgFaxHRPackNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgFaxHRPackNum.setStatus("current")


class _H3cVoEntityCfgFaxLRPackNum_Type(Integer32):
    """Custom type h3cVoEntityCfgFaxLRPackNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_H3cVoEntityCfgFaxLRPackNum_Type.__name__ = "Integer32"
_H3cVoEntityCfgFaxLRPackNum_Object = MibTableColumn
h3cVoEntityCfgFaxLRPackNum = _H3cVoEntityCfgFaxLRPackNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 14),
    _H3cVoEntityCfgFaxLRPackNum_Type()
)
h3cVoEntityCfgFaxLRPackNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgFaxLRPackNum.setStatus("current")
_H3cVoEntityCfgFaxSendNSFEnable_Type = TruthValue
_H3cVoEntityCfgFaxSendNSFEnable_Object = MibTableColumn
h3cVoEntityCfgFaxSendNSFEnable = _H3cVoEntityCfgFaxSendNSFEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 15),
    _H3cVoEntityCfgFaxSendNSFEnable_Type()
)
h3cVoEntityCfgFaxSendNSFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgFaxSendNSFEnable.setStatus("current")
_H3cVoEntityCfgFaxTrainMode_Type = H3cFaxTrainMode
_H3cVoEntityCfgFaxTrainMode_Object = MibTableColumn
h3cVoEntityCfgFaxTrainMode = _H3cVoEntityCfgFaxTrainMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 16),
    _H3cVoEntityCfgFaxTrainMode_Type()
)
h3cVoEntityCfgFaxTrainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgFaxTrainMode.setStatus("current")
_H3cVoEntityCfgFaxEcm_Type = TruthValue
_H3cVoEntityCfgFaxEcm_Object = MibTableColumn
h3cVoEntityCfgFaxEcm = _H3cVoEntityCfgFaxEcm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 17),
    _H3cVoEntityCfgFaxEcm_Type()
)
h3cVoEntityCfgFaxEcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgFaxEcm.setStatus("current")


class _H3cVoEntityCfgPriority_Type(Integer32):
    """Custom type h3cVoEntityCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_H3cVoEntityCfgPriority_Type.__name__ = "Integer32"
_H3cVoEntityCfgPriority_Object = MibTableColumn
h3cVoEntityCfgPriority = _H3cVoEntityCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 18),
    _H3cVoEntityCfgPriority_Type()
)
h3cVoEntityCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgPriority.setStatus("current")


class _H3cVoEntityCfgDescription_Type(OctetString):
    """Custom type h3cVoEntityCfgDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_H3cVoEntityCfgDescription_Type.__name__ = "OctetString"
_H3cVoEntityCfgDescription_Object = MibTableColumn
h3cVoEntityCfgDescription = _H3cVoEntityCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 2, 1, 19),
    _H3cVoEntityCfgDescription_Type()
)
h3cVoEntityCfgDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityCfgDescription.setStatus("current")
_H3cVoPOTSEntityConfigTable_Object = MibTable
h3cVoPOTSEntityConfigTable = _H3cVoPOTSEntityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 3)
)
if mibBuilder.loadTexts:
    h3cVoPOTSEntityConfigTable.setStatus("current")
_H3cVoPOTSEntityConfigEntry_Object = MibTableRow
h3cVoPOTSEntityConfigEntry = _H3cVoPOTSEntityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 3, 1)
)
h3cVoPOTSEntityConfigEntry.setIndexNames(
    (0, "H3C-VOICE-DIAL-CONTROL-MIB", "h3cVoPOTSEntityConfigIndex"),
)
if mibBuilder.loadTexts:
    h3cVoPOTSEntityConfigEntry.setStatus("current")


class _H3cVoPOTSEntityConfigIndex_Type(Integer32):
    """Custom type h3cVoPOTSEntityConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoPOTSEntityConfigIndex_Type.__name__ = "Integer32"
_H3cVoPOTSEntityConfigIndex_Object = MibTableColumn
h3cVoPOTSEntityConfigIndex = _H3cVoPOTSEntityConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 3, 1, 1),
    _H3cVoPOTSEntityConfigIndex_Type()
)
h3cVoPOTSEntityConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoPOTSEntityConfigIndex.setStatus("current")


class _H3cVoPOTSEntityConfigPrefix_Type(OctetString):
    """Custom type h3cVoPOTSEntityConfigPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H3cVoPOTSEntityConfigPrefix_Type.__name__ = "OctetString"
_H3cVoPOTSEntityConfigPrefix_Object = MibTableColumn
h3cVoPOTSEntityConfigPrefix = _H3cVoPOTSEntityConfigPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 3, 1, 2),
    _H3cVoPOTSEntityConfigPrefix_Type()
)
h3cVoPOTSEntityConfigPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPOTSEntityConfigPrefix.setStatus("current")
_H3cVoPOTSEntityConfigSubLine_Type = OctetString
_H3cVoPOTSEntityConfigSubLine_Object = MibTableColumn
h3cVoPOTSEntityConfigSubLine = _H3cVoPOTSEntityConfigSubLine_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 3, 1, 3),
    _H3cVoPOTSEntityConfigSubLine_Type()
)
h3cVoPOTSEntityConfigSubLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPOTSEntityConfigSubLine.setStatus("current")


class _H3cVoPOTSEntityConfigSendNum_Type(Integer32):
    """Custom type h3cVoPOTSEntityConfigSendNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(65534, 65534),
        ValueRangeConstraint(65535, 65535),
    )


_H3cVoPOTSEntityConfigSendNum_Type.__name__ = "Integer32"
_H3cVoPOTSEntityConfigSendNum_Object = MibTableColumn
h3cVoPOTSEntityConfigSendNum = _H3cVoPOTSEntityConfigSendNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 3, 1, 4),
    _H3cVoPOTSEntityConfigSendNum_Type()
)
h3cVoPOTSEntityConfigSendNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPOTSEntityConfigSendNum.setStatus("current")
_H3cVoVoIPEntityConfigTable_Object = MibTable
h3cVoVoIPEntityConfigTable = _H3cVoVoIPEntityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 4)
)
if mibBuilder.loadTexts:
    h3cVoVoIPEntityConfigTable.setStatus("current")
_H3cVoVoIPEntityConfigEntry_Object = MibTableRow
h3cVoVoIPEntityConfigEntry = _H3cVoVoIPEntityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 4, 1)
)
h3cVoVoIPEntityConfigEntry.setIndexNames(
    (0, "H3C-VOICE-DIAL-CONTROL-MIB", "h3cVoVoIPEntityCfgIndex"),
)
if mibBuilder.loadTexts:
    h3cVoVoIPEntityConfigEntry.setStatus("current")


class _H3cVoVoIPEntityCfgIndex_Type(Integer32):
    """Custom type h3cVoVoIPEntityCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoVoIPEntityCfgIndex_Type.__name__ = "Integer32"
_H3cVoVoIPEntityCfgIndex_Object = MibTableColumn
h3cVoVoIPEntityCfgIndex = _H3cVoVoIPEntityCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 4, 1, 1),
    _H3cVoVoIPEntityCfgIndex_Type()
)
h3cVoVoIPEntityCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoVoIPEntityCfgIndex.setStatus("current")


class _H3cVoVoIPEntityCfgTargetType_Type(Integer32):
    """Custom type h3cVoVoIPEntityCfgTargetType based on Integer32"""
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
        *(("h323IpAddress", 3),
          ("ras", 2),
          ("sipIpAddress", 4),
          ("sipProxy", 5),
          ("unknown", 1))
    )


_H3cVoVoIPEntityCfgTargetType_Type.__name__ = "Integer32"
_H3cVoVoIPEntityCfgTargetType_Object = MibTableColumn
h3cVoVoIPEntityCfgTargetType = _H3cVoVoIPEntityCfgTargetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 4, 1, 2),
    _H3cVoVoIPEntityCfgTargetType_Type()
)
h3cVoVoIPEntityCfgTargetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoVoIPEntityCfgTargetType.setStatus("current")
_H3cVoVoIPEntityCfgTargetAddrType_Type = InetAddressType
_H3cVoVoIPEntityCfgTargetAddrType_Object = MibTableColumn
h3cVoVoIPEntityCfgTargetAddrType = _H3cVoVoIPEntityCfgTargetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 4, 1, 3),
    _H3cVoVoIPEntityCfgTargetAddrType_Type()
)
h3cVoVoIPEntityCfgTargetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoVoIPEntityCfgTargetAddrType.setStatus("current")
_H3cVoVoIPEntityCfgTargetAddr_Type = InetAddress
_H3cVoVoIPEntityCfgTargetAddr_Object = MibTableColumn
h3cVoVoIPEntityCfgTargetAddr = _H3cVoVoIPEntityCfgTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 4, 1, 4),
    _H3cVoVoIPEntityCfgTargetAddr_Type()
)
h3cVoVoIPEntityCfgTargetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoVoIPEntityCfgTargetAddr.setStatus("current")
_H3cVoEntityNumberTable_Object = MibTable
h3cVoEntityNumberTable = _H3cVoEntityNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 5)
)
if mibBuilder.loadTexts:
    h3cVoEntityNumberTable.setStatus("current")
_H3cVoEntityNumberEntry_Object = MibTableRow
h3cVoEntityNumberEntry = _H3cVoEntityNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 5, 1)
)
h3cVoEntityNumberEntry.setIndexNames(
    (0, "H3C-VOICE-DIAL-CONTROL-MIB", "h3cVoEntityIndex"),
)
if mibBuilder.loadTexts:
    h3cVoEntityNumberEntry.setStatus("current")


class _H3cVoEntityNumberAuthUser_Type(OctetString):
    """Custom type h3cVoEntityNumberAuthUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cVoEntityNumberAuthUser_Type.__name__ = "OctetString"
_H3cVoEntityNumberAuthUser_Object = MibTableColumn
h3cVoEntityNumberAuthUser = _H3cVoEntityNumberAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 5, 1, 1),
    _H3cVoEntityNumberAuthUser_Type()
)
h3cVoEntityNumberAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityNumberAuthUser.setStatus("current")
_H3cVoEntityNumberPasswordType_Type = Integer32
_H3cVoEntityNumberPasswordType_Object = MibTableColumn
h3cVoEntityNumberPasswordType = _H3cVoEntityNumberPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 5, 1, 2),
    _H3cVoEntityNumberPasswordType_Type()
)
h3cVoEntityNumberPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityNumberPasswordType.setStatus("current")


class _H3cVoEntityNumberPassword_Type(OctetString):
    """Custom type h3cVoEntityNumberPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
        ValueSizeConstraint(24, 24),
    )


_H3cVoEntityNumberPassword_Type.__name__ = "OctetString"
_H3cVoEntityNumberPassword_Object = MibTableColumn
h3cVoEntityNumberPassword = _H3cVoEntityNumberPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 5, 1, 3),
    _H3cVoEntityNumberPassword_Type()
)
h3cVoEntityNumberPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoEntityNumberPassword.setStatus("current")
_H3cVoEntityNumberStatus_Type = H3cRegisterdStatus
_H3cVoEntityNumberStatus_Object = MibTableColumn
h3cVoEntityNumberStatus = _H3cVoEntityNumberStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 5, 1, 4),
    _H3cVoEntityNumberStatus_Type()
)
h3cVoEntityNumberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoEntityNumberStatus.setStatus("current")
_H3cVoEntityNumberExpires_Type = Integer32
_H3cVoEntityNumberExpires_Object = MibTableColumn
h3cVoEntityNumberExpires = _H3cVoEntityNumberExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 14, 1, 5, 1, 5),
    _H3cVoEntityNumberExpires_Type()
)
h3cVoEntityNumberExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoEntityNumberExpires.setStatus("current")
if mibBuilder.loadTexts:
    h3cVoEntityNumberExpires.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VOICE-DIAL-CONTROL-MIB",
    **{"H3cCodecType": H3cCodecType,
       "H3cOutBandMode": H3cOutBandMode,
       "H3cFaxProtocolType": H3cFaxProtocolType,
       "H3cFaxBaudrateType": H3cFaxBaudrateType,
       "H3cFaxTrainMode": H3cFaxTrainMode,
       "H3cRegisterdStatus": H3cRegisterdStatus,
       "h3cVoiceEntityControl": h3cVoiceEntityControl,
       "h3cVoEntityObjects": h3cVoEntityObjects,
       "h3cVoEntityCreateTable": h3cVoEntityCreateTable,
       "h3cVoEntityCreateEntry": h3cVoEntityCreateEntry,
       "h3cVoEntityIndex": h3cVoEntityIndex,
       "h3cVoEntityType": h3cVoEntityType,
       "h3cVoEntityRowStatus": h3cVoEntityRowStatus,
       "h3cVoEntityCommonConfigTable": h3cVoEntityCommonConfigTable,
       "h3cVoEntityCommonConfigEntry": h3cVoEntityCommonConfigEntry,
       "h3cVoEntityCfgIndex": h3cVoEntityCfgIndex,
       "h3cVoEntityCfgCodec1st": h3cVoEntityCfgCodec1st,
       "h3cVoEntityCfgCodec2nd": h3cVoEntityCfgCodec2nd,
       "h3cVoEntityCfgCodec3rd": h3cVoEntityCfgCodec3rd,
       "h3cVoEntityCfgCodec4th": h3cVoEntityCfgCodec4th,
       "h3cVoEntityCfgDSCP": h3cVoEntityCfgDSCP,
       "h3cVoEntityCfgVADEnable": h3cVoEntityCfgVADEnable,
       "h3cVoEntityCfgOutbandMode": h3cVoEntityCfgOutbandMode,
       "h3cVoEntityCfgFaxLevel": h3cVoEntityCfgFaxLevel,
       "h3cVoEntityCfgFaxBaudrate": h3cVoEntityCfgFaxBaudrate,
       "h3cVoEntityCfgFaxLocalTrainPara": h3cVoEntityCfgFaxLocalTrainPara,
       "h3cVoEntityCfgFaxProtocol": h3cVoEntityCfgFaxProtocol,
       "h3cVoEntityCfgFaxHRPackNum": h3cVoEntityCfgFaxHRPackNum,
       "h3cVoEntityCfgFaxLRPackNum": h3cVoEntityCfgFaxLRPackNum,
       "h3cVoEntityCfgFaxSendNSFEnable": h3cVoEntityCfgFaxSendNSFEnable,
       "h3cVoEntityCfgFaxTrainMode": h3cVoEntityCfgFaxTrainMode,
       "h3cVoEntityCfgFaxEcm": h3cVoEntityCfgFaxEcm,
       "h3cVoEntityCfgPriority": h3cVoEntityCfgPriority,
       "h3cVoEntityCfgDescription": h3cVoEntityCfgDescription,
       "h3cVoPOTSEntityConfigTable": h3cVoPOTSEntityConfigTable,
       "h3cVoPOTSEntityConfigEntry": h3cVoPOTSEntityConfigEntry,
       "h3cVoPOTSEntityConfigIndex": h3cVoPOTSEntityConfigIndex,
       "h3cVoPOTSEntityConfigPrefix": h3cVoPOTSEntityConfigPrefix,
       "h3cVoPOTSEntityConfigSubLine": h3cVoPOTSEntityConfigSubLine,
       "h3cVoPOTSEntityConfigSendNum": h3cVoPOTSEntityConfigSendNum,
       "h3cVoVoIPEntityConfigTable": h3cVoVoIPEntityConfigTable,
       "h3cVoVoIPEntityConfigEntry": h3cVoVoIPEntityConfigEntry,
       "h3cVoVoIPEntityCfgIndex": h3cVoVoIPEntityCfgIndex,
       "h3cVoVoIPEntityCfgTargetType": h3cVoVoIPEntityCfgTargetType,
       "h3cVoVoIPEntityCfgTargetAddrType": h3cVoVoIPEntityCfgTargetAddrType,
       "h3cVoVoIPEntityCfgTargetAddr": h3cVoVoIPEntityCfgTargetAddr,
       "h3cVoEntityNumberTable": h3cVoEntityNumberTable,
       "h3cVoEntityNumberEntry": h3cVoEntityNumberEntry,
       "h3cVoEntityNumberAuthUser": h3cVoEntityNumberAuthUser,
       "h3cVoEntityNumberPasswordType": h3cVoEntityNumberPasswordType,
       "h3cVoEntityNumberPassword": h3cVoEntityNumberPassword,
       "h3cVoEntityNumberStatus": h3cVoEntityNumberStatus,
       "h3cVoEntityNumberExpires": h3cVoEntityNumberExpires}
)
