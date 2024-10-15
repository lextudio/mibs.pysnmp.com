# SNMP MIB module (HH3C-VOICE-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-VOICE-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:16 2024
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

(hh3cVoice,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cVoice")

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

hh3cVoiceEntityControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14)
)
hh3cVoiceEntityControl.setRevisions(
        ("2009-04-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cCodecType(Integer32, TextualConvention):
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



class Hh3cOutBandMode(Integer32, TextualConvention):
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



class Hh3cFaxProtocolType(Integer32, TextualConvention):
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



class Hh3cFaxBaudrateType(Integer32, TextualConvention):
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



class Hh3cFaxTrainMode(Integer32, TextualConvention):
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



class Hh3cRegisterdStatus(Integer32, TextualConvention):
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

_Hh3cVoEntityObjects_ObjectIdentity = ObjectIdentity
hh3cVoEntityObjects = _Hh3cVoEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1)
)
_Hh3cVoEntityCreateTable_Object = MibTable
hh3cVoEntityCreateTable = _Hh3cVoEntityCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cVoEntityCreateTable.setStatus("current")
_Hh3cVoEntityCreateEntry_Object = MibTableRow
hh3cVoEntityCreateEntry = _Hh3cVoEntityCreateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 1, 1)
)
hh3cVoEntityCreateEntry.setIndexNames(
    (0, "HH3C-VOICE-DIAL-CONTROL-MIB", "hh3cVoEntityIndex"),
)
if mibBuilder.loadTexts:
    hh3cVoEntityCreateEntry.setStatus("current")


class _Hh3cVoEntityIndex_Type(Integer32):
    """Custom type hh3cVoEntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cVoEntityIndex_Type.__name__ = "Integer32"
_Hh3cVoEntityIndex_Object = MibTableColumn
hh3cVoEntityIndex = _Hh3cVoEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 1, 1, 1),
    _Hh3cVoEntityIndex_Type()
)
hh3cVoEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVoEntityIndex.setStatus("current")


class _Hh3cVoEntityType_Type(Integer32):
    """Custom type hh3cVoEntityType based on Integer32"""
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


_Hh3cVoEntityType_Type.__name__ = "Integer32"
_Hh3cVoEntityType_Object = MibTableColumn
hh3cVoEntityType = _Hh3cVoEntityType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 1, 1, 2),
    _Hh3cVoEntityType_Type()
)
hh3cVoEntityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVoEntityType.setStatus("current")
_Hh3cVoEntityRowStatus_Type = RowStatus
_Hh3cVoEntityRowStatus_Object = MibTableColumn
hh3cVoEntityRowStatus = _Hh3cVoEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 1, 1, 3),
    _Hh3cVoEntityRowStatus_Type()
)
hh3cVoEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVoEntityRowStatus.setStatus("current")
_Hh3cVoEntityCommonConfigTable_Object = MibTable
hh3cVoEntityCommonConfigTable = _Hh3cVoEntityCommonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cVoEntityCommonConfigTable.setStatus("current")
_Hh3cVoEntityCommonConfigEntry_Object = MibTableRow
hh3cVoEntityCommonConfigEntry = _Hh3cVoEntityCommonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1)
)
hh3cVoEntityCommonConfigEntry.setIndexNames(
    (0, "HH3C-VOICE-DIAL-CONTROL-MIB", "hh3cVoEntityCfgIndex"),
)
if mibBuilder.loadTexts:
    hh3cVoEntityCommonConfigEntry.setStatus("current")


class _Hh3cVoEntityCfgIndex_Type(Integer32):
    """Custom type hh3cVoEntityCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cVoEntityCfgIndex_Type.__name__ = "Integer32"
_Hh3cVoEntityCfgIndex_Object = MibTableColumn
hh3cVoEntityCfgIndex = _Hh3cVoEntityCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 1),
    _Hh3cVoEntityCfgIndex_Type()
)
hh3cVoEntityCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgIndex.setStatus("current")
_Hh3cVoEntityCfgCodec1st_Type = Hh3cCodecType
_Hh3cVoEntityCfgCodec1st_Object = MibTableColumn
hh3cVoEntityCfgCodec1st = _Hh3cVoEntityCfgCodec1st_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 2),
    _Hh3cVoEntityCfgCodec1st_Type()
)
hh3cVoEntityCfgCodec1st.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgCodec1st.setStatus("current")
_Hh3cVoEntityCfgCodec2nd_Type = Hh3cCodecType
_Hh3cVoEntityCfgCodec2nd_Object = MibTableColumn
hh3cVoEntityCfgCodec2nd = _Hh3cVoEntityCfgCodec2nd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 3),
    _Hh3cVoEntityCfgCodec2nd_Type()
)
hh3cVoEntityCfgCodec2nd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgCodec2nd.setStatus("current")
_Hh3cVoEntityCfgCodec3rd_Type = Hh3cCodecType
_Hh3cVoEntityCfgCodec3rd_Object = MibTableColumn
hh3cVoEntityCfgCodec3rd = _Hh3cVoEntityCfgCodec3rd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 4),
    _Hh3cVoEntityCfgCodec3rd_Type()
)
hh3cVoEntityCfgCodec3rd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgCodec3rd.setStatus("current")
_Hh3cVoEntityCfgCodec4th_Type = Hh3cCodecType
_Hh3cVoEntityCfgCodec4th_Object = MibTableColumn
hh3cVoEntityCfgCodec4th = _Hh3cVoEntityCfgCodec4th_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 5),
    _Hh3cVoEntityCfgCodec4th_Type()
)
hh3cVoEntityCfgCodec4th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgCodec4th.setStatus("current")


class _Hh3cVoEntityCfgDSCP_Type(Integer32):
    """Custom type hh3cVoEntityCfgDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cVoEntityCfgDSCP_Type.__name__ = "Integer32"
_Hh3cVoEntityCfgDSCP_Object = MibTableColumn
hh3cVoEntityCfgDSCP = _Hh3cVoEntityCfgDSCP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 6),
    _Hh3cVoEntityCfgDSCP_Type()
)
hh3cVoEntityCfgDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgDSCP.setStatus("current")
_Hh3cVoEntityCfgVADEnable_Type = TruthValue
_Hh3cVoEntityCfgVADEnable_Object = MibTableColumn
hh3cVoEntityCfgVADEnable = _Hh3cVoEntityCfgVADEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 7),
    _Hh3cVoEntityCfgVADEnable_Type()
)
hh3cVoEntityCfgVADEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgVADEnable.setStatus("current")
_Hh3cVoEntityCfgOutbandMode_Type = Hh3cOutBandMode
_Hh3cVoEntityCfgOutbandMode_Object = MibTableColumn
hh3cVoEntityCfgOutbandMode = _Hh3cVoEntityCfgOutbandMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 8),
    _Hh3cVoEntityCfgOutbandMode_Type()
)
hh3cVoEntityCfgOutbandMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgOutbandMode.setStatus("current")


class _Hh3cVoEntityCfgFaxLevel_Type(Integer32):
    """Custom type hh3cVoEntityCfgFaxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, -3),
    )


_Hh3cVoEntityCfgFaxLevel_Type.__name__ = "Integer32"
_Hh3cVoEntityCfgFaxLevel_Object = MibTableColumn
hh3cVoEntityCfgFaxLevel = _Hh3cVoEntityCfgFaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 9),
    _Hh3cVoEntityCfgFaxLevel_Type()
)
hh3cVoEntityCfgFaxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgFaxLevel.setStatus("current")
_Hh3cVoEntityCfgFaxBaudrate_Type = Hh3cFaxBaudrateType
_Hh3cVoEntityCfgFaxBaudrate_Object = MibTableColumn
hh3cVoEntityCfgFaxBaudrate = _Hh3cVoEntityCfgFaxBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 10),
    _Hh3cVoEntityCfgFaxBaudrate_Type()
)
hh3cVoEntityCfgFaxBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgFaxBaudrate.setStatus("current")


class _Hh3cVoEntityCfgFaxLocalTrainPara_Type(Integer32):
    """Custom type hh3cVoEntityCfgFaxLocalTrainPara based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cVoEntityCfgFaxLocalTrainPara_Type.__name__ = "Integer32"
_Hh3cVoEntityCfgFaxLocalTrainPara_Object = MibTableColumn
hh3cVoEntityCfgFaxLocalTrainPara = _Hh3cVoEntityCfgFaxLocalTrainPara_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 11),
    _Hh3cVoEntityCfgFaxLocalTrainPara_Type()
)
hh3cVoEntityCfgFaxLocalTrainPara.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgFaxLocalTrainPara.setStatus("current")
_Hh3cVoEntityCfgFaxProtocol_Type = Hh3cFaxProtocolType
_Hh3cVoEntityCfgFaxProtocol_Object = MibTableColumn
hh3cVoEntityCfgFaxProtocol = _Hh3cVoEntityCfgFaxProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 12),
    _Hh3cVoEntityCfgFaxProtocol_Type()
)
hh3cVoEntityCfgFaxProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgFaxProtocol.setStatus("current")


class _Hh3cVoEntityCfgFaxHRPackNum_Type(Integer32):
    """Custom type hh3cVoEntityCfgFaxHRPackNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hh3cVoEntityCfgFaxHRPackNum_Type.__name__ = "Integer32"
_Hh3cVoEntityCfgFaxHRPackNum_Object = MibTableColumn
hh3cVoEntityCfgFaxHRPackNum = _Hh3cVoEntityCfgFaxHRPackNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 13),
    _Hh3cVoEntityCfgFaxHRPackNum_Type()
)
hh3cVoEntityCfgFaxHRPackNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgFaxHRPackNum.setStatus("current")


class _Hh3cVoEntityCfgFaxLRPackNum_Type(Integer32):
    """Custom type hh3cVoEntityCfgFaxLRPackNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Hh3cVoEntityCfgFaxLRPackNum_Type.__name__ = "Integer32"
_Hh3cVoEntityCfgFaxLRPackNum_Object = MibTableColumn
hh3cVoEntityCfgFaxLRPackNum = _Hh3cVoEntityCfgFaxLRPackNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 14),
    _Hh3cVoEntityCfgFaxLRPackNum_Type()
)
hh3cVoEntityCfgFaxLRPackNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgFaxLRPackNum.setStatus("current")
_Hh3cVoEntityCfgFaxSendNSFEnable_Type = TruthValue
_Hh3cVoEntityCfgFaxSendNSFEnable_Object = MibTableColumn
hh3cVoEntityCfgFaxSendNSFEnable = _Hh3cVoEntityCfgFaxSendNSFEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 15),
    _Hh3cVoEntityCfgFaxSendNSFEnable_Type()
)
hh3cVoEntityCfgFaxSendNSFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgFaxSendNSFEnable.setStatus("current")
_Hh3cVoEntityCfgFaxTrainMode_Type = Hh3cFaxTrainMode
_Hh3cVoEntityCfgFaxTrainMode_Object = MibTableColumn
hh3cVoEntityCfgFaxTrainMode = _Hh3cVoEntityCfgFaxTrainMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 16),
    _Hh3cVoEntityCfgFaxTrainMode_Type()
)
hh3cVoEntityCfgFaxTrainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgFaxTrainMode.setStatus("current")
_Hh3cVoEntityCfgFaxEcm_Type = TruthValue
_Hh3cVoEntityCfgFaxEcm_Object = MibTableColumn
hh3cVoEntityCfgFaxEcm = _Hh3cVoEntityCfgFaxEcm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 17),
    _Hh3cVoEntityCfgFaxEcm_Type()
)
hh3cVoEntityCfgFaxEcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgFaxEcm.setStatus("current")


class _Hh3cVoEntityCfgPriority_Type(Integer32):
    """Custom type hh3cVoEntityCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Hh3cVoEntityCfgPriority_Type.__name__ = "Integer32"
_Hh3cVoEntityCfgPriority_Object = MibTableColumn
hh3cVoEntityCfgPriority = _Hh3cVoEntityCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 18),
    _Hh3cVoEntityCfgPriority_Type()
)
hh3cVoEntityCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgPriority.setStatus("current")


class _Hh3cVoEntityCfgDescription_Type(OctetString):
    """Custom type hh3cVoEntityCfgDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Hh3cVoEntityCfgDescription_Type.__name__ = "OctetString"
_Hh3cVoEntityCfgDescription_Object = MibTableColumn
hh3cVoEntityCfgDescription = _Hh3cVoEntityCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 2, 1, 19),
    _Hh3cVoEntityCfgDescription_Type()
)
hh3cVoEntityCfgDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityCfgDescription.setStatus("current")
_Hh3cVoPOTSEntityConfigTable_Object = MibTable
hh3cVoPOTSEntityConfigTable = _Hh3cVoPOTSEntityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cVoPOTSEntityConfigTable.setStatus("current")
_Hh3cVoPOTSEntityConfigEntry_Object = MibTableRow
hh3cVoPOTSEntityConfigEntry = _Hh3cVoPOTSEntityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 3, 1)
)
hh3cVoPOTSEntityConfigEntry.setIndexNames(
    (0, "HH3C-VOICE-DIAL-CONTROL-MIB", "hh3cVoPOTSEntityConfigIndex"),
)
if mibBuilder.loadTexts:
    hh3cVoPOTSEntityConfigEntry.setStatus("current")


class _Hh3cVoPOTSEntityConfigIndex_Type(Integer32):
    """Custom type hh3cVoPOTSEntityConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cVoPOTSEntityConfigIndex_Type.__name__ = "Integer32"
_Hh3cVoPOTSEntityConfigIndex_Object = MibTableColumn
hh3cVoPOTSEntityConfigIndex = _Hh3cVoPOTSEntityConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 3, 1, 1),
    _Hh3cVoPOTSEntityConfigIndex_Type()
)
hh3cVoPOTSEntityConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVoPOTSEntityConfigIndex.setStatus("current")


class _Hh3cVoPOTSEntityConfigPrefix_Type(OctetString):
    """Custom type hh3cVoPOTSEntityConfigPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cVoPOTSEntityConfigPrefix_Type.__name__ = "OctetString"
_Hh3cVoPOTSEntityConfigPrefix_Object = MibTableColumn
hh3cVoPOTSEntityConfigPrefix = _Hh3cVoPOTSEntityConfigPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 3, 1, 2),
    _Hh3cVoPOTSEntityConfigPrefix_Type()
)
hh3cVoPOTSEntityConfigPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoPOTSEntityConfigPrefix.setStatus("current")
_Hh3cVoPOTSEntityConfigSubLine_Type = OctetString
_Hh3cVoPOTSEntityConfigSubLine_Object = MibTableColumn
hh3cVoPOTSEntityConfigSubLine = _Hh3cVoPOTSEntityConfigSubLine_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 3, 1, 3),
    _Hh3cVoPOTSEntityConfigSubLine_Type()
)
hh3cVoPOTSEntityConfigSubLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoPOTSEntityConfigSubLine.setStatus("current")


class _Hh3cVoPOTSEntityConfigSendNum_Type(Integer32):
    """Custom type hh3cVoPOTSEntityConfigSendNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(65534, 65534),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cVoPOTSEntityConfigSendNum_Type.__name__ = "Integer32"
_Hh3cVoPOTSEntityConfigSendNum_Object = MibTableColumn
hh3cVoPOTSEntityConfigSendNum = _Hh3cVoPOTSEntityConfigSendNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 3, 1, 4),
    _Hh3cVoPOTSEntityConfigSendNum_Type()
)
hh3cVoPOTSEntityConfigSendNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoPOTSEntityConfigSendNum.setStatus("current")
_Hh3cVoVoIPEntityConfigTable_Object = MibTable
hh3cVoVoIPEntityConfigTable = _Hh3cVoVoIPEntityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cVoVoIPEntityConfigTable.setStatus("current")
_Hh3cVoVoIPEntityConfigEntry_Object = MibTableRow
hh3cVoVoIPEntityConfigEntry = _Hh3cVoVoIPEntityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 4, 1)
)
hh3cVoVoIPEntityConfigEntry.setIndexNames(
    (0, "HH3C-VOICE-DIAL-CONTROL-MIB", "hh3cVoVoIPEntityCfgIndex"),
)
if mibBuilder.loadTexts:
    hh3cVoVoIPEntityConfigEntry.setStatus("current")


class _Hh3cVoVoIPEntityCfgIndex_Type(Integer32):
    """Custom type hh3cVoVoIPEntityCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cVoVoIPEntityCfgIndex_Type.__name__ = "Integer32"
_Hh3cVoVoIPEntityCfgIndex_Object = MibTableColumn
hh3cVoVoIPEntityCfgIndex = _Hh3cVoVoIPEntityCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 4, 1, 1),
    _Hh3cVoVoIPEntityCfgIndex_Type()
)
hh3cVoVoIPEntityCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVoVoIPEntityCfgIndex.setStatus("current")


class _Hh3cVoVoIPEntityCfgTargetType_Type(Integer32):
    """Custom type hh3cVoVoIPEntityCfgTargetType based on Integer32"""
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


_Hh3cVoVoIPEntityCfgTargetType_Type.__name__ = "Integer32"
_Hh3cVoVoIPEntityCfgTargetType_Object = MibTableColumn
hh3cVoVoIPEntityCfgTargetType = _Hh3cVoVoIPEntityCfgTargetType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 4, 1, 2),
    _Hh3cVoVoIPEntityCfgTargetType_Type()
)
hh3cVoVoIPEntityCfgTargetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoVoIPEntityCfgTargetType.setStatus("current")
_Hh3cVoVoIPEntityCfgTargetAddrType_Type = InetAddressType
_Hh3cVoVoIPEntityCfgTargetAddrType_Object = MibTableColumn
hh3cVoVoIPEntityCfgTargetAddrType = _Hh3cVoVoIPEntityCfgTargetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 4, 1, 3),
    _Hh3cVoVoIPEntityCfgTargetAddrType_Type()
)
hh3cVoVoIPEntityCfgTargetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoVoIPEntityCfgTargetAddrType.setStatus("current")
_Hh3cVoVoIPEntityCfgTargetAddr_Type = InetAddress
_Hh3cVoVoIPEntityCfgTargetAddr_Object = MibTableColumn
hh3cVoVoIPEntityCfgTargetAddr = _Hh3cVoVoIPEntityCfgTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 4, 1, 4),
    _Hh3cVoVoIPEntityCfgTargetAddr_Type()
)
hh3cVoVoIPEntityCfgTargetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoVoIPEntityCfgTargetAddr.setStatus("current")
_Hh3cVoEntityNumberTable_Object = MibTable
hh3cVoEntityNumberTable = _Hh3cVoEntityNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cVoEntityNumberTable.setStatus("current")
_Hh3cVoEntityNumberEntry_Object = MibTableRow
hh3cVoEntityNumberEntry = _Hh3cVoEntityNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 5, 1)
)
hh3cVoEntityNumberEntry.setIndexNames(
    (0, "HH3C-VOICE-DIAL-CONTROL-MIB", "hh3cVoEntityIndex"),
)
if mibBuilder.loadTexts:
    hh3cVoEntityNumberEntry.setStatus("current")


class _Hh3cVoEntityNumberAuthUser_Type(OctetString):
    """Custom type hh3cVoEntityNumberAuthUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cVoEntityNumberAuthUser_Type.__name__ = "OctetString"
_Hh3cVoEntityNumberAuthUser_Object = MibTableColumn
hh3cVoEntityNumberAuthUser = _Hh3cVoEntityNumberAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 5, 1, 1),
    _Hh3cVoEntityNumberAuthUser_Type()
)
hh3cVoEntityNumberAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityNumberAuthUser.setStatus("current")
_Hh3cVoEntityNumberPasswordType_Type = Integer32
_Hh3cVoEntityNumberPasswordType_Object = MibTableColumn
hh3cVoEntityNumberPasswordType = _Hh3cVoEntityNumberPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 5, 1, 2),
    _Hh3cVoEntityNumberPasswordType_Type()
)
hh3cVoEntityNumberPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityNumberPasswordType.setStatus("current")


class _Hh3cVoEntityNumberPassword_Type(OctetString):
    """Custom type hh3cVoEntityNumberPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
        ValueSizeConstraint(24, 24),
    )


_Hh3cVoEntityNumberPassword_Type.__name__ = "OctetString"
_Hh3cVoEntityNumberPassword_Object = MibTableColumn
hh3cVoEntityNumberPassword = _Hh3cVoEntityNumberPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 5, 1, 3),
    _Hh3cVoEntityNumberPassword_Type()
)
hh3cVoEntityNumberPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoEntityNumberPassword.setStatus("current")
_Hh3cVoEntityNumberStatus_Type = Hh3cRegisterdStatus
_Hh3cVoEntityNumberStatus_Object = MibTableColumn
hh3cVoEntityNumberStatus = _Hh3cVoEntityNumberStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 5, 1, 4),
    _Hh3cVoEntityNumberStatus_Type()
)
hh3cVoEntityNumberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoEntityNumberStatus.setStatus("current")
_Hh3cVoEntityNumberExpires_Type = Integer32
_Hh3cVoEntityNumberExpires_Object = MibTableColumn
hh3cVoEntityNumberExpires = _Hh3cVoEntityNumberExpires_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 14, 1, 5, 1, 5),
    _Hh3cVoEntityNumberExpires_Type()
)
hh3cVoEntityNumberExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoEntityNumberExpires.setStatus("current")
if mibBuilder.loadTexts:
    hh3cVoEntityNumberExpires.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VOICE-DIAL-CONTROL-MIB",
    **{"Hh3cCodecType": Hh3cCodecType,
       "Hh3cOutBandMode": Hh3cOutBandMode,
       "Hh3cFaxProtocolType": Hh3cFaxProtocolType,
       "Hh3cFaxBaudrateType": Hh3cFaxBaudrateType,
       "Hh3cFaxTrainMode": Hh3cFaxTrainMode,
       "Hh3cRegisterdStatus": Hh3cRegisterdStatus,
       "hh3cVoiceEntityControl": hh3cVoiceEntityControl,
       "hh3cVoEntityObjects": hh3cVoEntityObjects,
       "hh3cVoEntityCreateTable": hh3cVoEntityCreateTable,
       "hh3cVoEntityCreateEntry": hh3cVoEntityCreateEntry,
       "hh3cVoEntityIndex": hh3cVoEntityIndex,
       "hh3cVoEntityType": hh3cVoEntityType,
       "hh3cVoEntityRowStatus": hh3cVoEntityRowStatus,
       "hh3cVoEntityCommonConfigTable": hh3cVoEntityCommonConfigTable,
       "hh3cVoEntityCommonConfigEntry": hh3cVoEntityCommonConfigEntry,
       "hh3cVoEntityCfgIndex": hh3cVoEntityCfgIndex,
       "hh3cVoEntityCfgCodec1st": hh3cVoEntityCfgCodec1st,
       "hh3cVoEntityCfgCodec2nd": hh3cVoEntityCfgCodec2nd,
       "hh3cVoEntityCfgCodec3rd": hh3cVoEntityCfgCodec3rd,
       "hh3cVoEntityCfgCodec4th": hh3cVoEntityCfgCodec4th,
       "hh3cVoEntityCfgDSCP": hh3cVoEntityCfgDSCP,
       "hh3cVoEntityCfgVADEnable": hh3cVoEntityCfgVADEnable,
       "hh3cVoEntityCfgOutbandMode": hh3cVoEntityCfgOutbandMode,
       "hh3cVoEntityCfgFaxLevel": hh3cVoEntityCfgFaxLevel,
       "hh3cVoEntityCfgFaxBaudrate": hh3cVoEntityCfgFaxBaudrate,
       "hh3cVoEntityCfgFaxLocalTrainPara": hh3cVoEntityCfgFaxLocalTrainPara,
       "hh3cVoEntityCfgFaxProtocol": hh3cVoEntityCfgFaxProtocol,
       "hh3cVoEntityCfgFaxHRPackNum": hh3cVoEntityCfgFaxHRPackNum,
       "hh3cVoEntityCfgFaxLRPackNum": hh3cVoEntityCfgFaxLRPackNum,
       "hh3cVoEntityCfgFaxSendNSFEnable": hh3cVoEntityCfgFaxSendNSFEnable,
       "hh3cVoEntityCfgFaxTrainMode": hh3cVoEntityCfgFaxTrainMode,
       "hh3cVoEntityCfgFaxEcm": hh3cVoEntityCfgFaxEcm,
       "hh3cVoEntityCfgPriority": hh3cVoEntityCfgPriority,
       "hh3cVoEntityCfgDescription": hh3cVoEntityCfgDescription,
       "hh3cVoPOTSEntityConfigTable": hh3cVoPOTSEntityConfigTable,
       "hh3cVoPOTSEntityConfigEntry": hh3cVoPOTSEntityConfigEntry,
       "hh3cVoPOTSEntityConfigIndex": hh3cVoPOTSEntityConfigIndex,
       "hh3cVoPOTSEntityConfigPrefix": hh3cVoPOTSEntityConfigPrefix,
       "hh3cVoPOTSEntityConfigSubLine": hh3cVoPOTSEntityConfigSubLine,
       "hh3cVoPOTSEntityConfigSendNum": hh3cVoPOTSEntityConfigSendNum,
       "hh3cVoVoIPEntityConfigTable": hh3cVoVoIPEntityConfigTable,
       "hh3cVoVoIPEntityConfigEntry": hh3cVoVoIPEntityConfigEntry,
       "hh3cVoVoIPEntityCfgIndex": hh3cVoVoIPEntityCfgIndex,
       "hh3cVoVoIPEntityCfgTargetType": hh3cVoVoIPEntityCfgTargetType,
       "hh3cVoVoIPEntityCfgTargetAddrType": hh3cVoVoIPEntityCfgTargetAddrType,
       "hh3cVoVoIPEntityCfgTargetAddr": hh3cVoVoIPEntityCfgTargetAddr,
       "hh3cVoEntityNumberTable": hh3cVoEntityNumberTable,
       "hh3cVoEntityNumberEntry": hh3cVoEntityNumberEntry,
       "hh3cVoEntityNumberAuthUser": hh3cVoEntityNumberAuthUser,
       "hh3cVoEntityNumberPasswordType": hh3cVoEntityNumberPasswordType,
       "hh3cVoEntityNumberPassword": hh3cVoEntityNumberPassword,
       "hh3cVoEntityNumberStatus": hh3cVoEntityNumberStatus,
       "hh3cVoEntityNumberExpires": hh3cVoEntityNumberExpires}
)
