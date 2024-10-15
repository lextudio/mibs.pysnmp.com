# SNMP MIB module (HPN-ICF-VOICE-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-VOICE-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:09 2024
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

(hpnicfVoice,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfVoice")

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

hpnicfVoiceEntityControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14)
)
hpnicfVoiceEntityControl.setRevisions(
        ("2009-04-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfCodecType(Integer32, TextualConvention):
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



class HpnicfOutBandMode(Integer32, TextualConvention):
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



class HpnicfFaxProtocolType(Integer32, TextualConvention):
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



class HpnicfFaxBaudrateType(Integer32, TextualConvention):
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



class HpnicfFaxTrainMode(Integer32, TextualConvention):
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



class HpnicfRegisterdStatus(Integer32, TextualConvention):
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

_HpnicfVoEntityObjects_ObjectIdentity = ObjectIdentity
hpnicfVoEntityObjects = _HpnicfVoEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1)
)
_HpnicfVoEntityCreateTable_Object = MibTable
hpnicfVoEntityCreateTable = _HpnicfVoEntityCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfVoEntityCreateTable.setStatus("current")
_HpnicfVoEntityCreateEntry_Object = MibTableRow
hpnicfVoEntityCreateEntry = _HpnicfVoEntityCreateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 1, 1)
)
hpnicfVoEntityCreateEntry.setIndexNames(
    (0, "HPN-ICF-VOICE-DIAL-CONTROL-MIB", "hpnicfVoEntityIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVoEntityCreateEntry.setStatus("current")


class _HpnicfVoEntityIndex_Type(Integer32):
    """Custom type hpnicfVoEntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfVoEntityIndex_Type.__name__ = "Integer32"
_HpnicfVoEntityIndex_Object = MibTableColumn
hpnicfVoEntityIndex = _HpnicfVoEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 1, 1, 1),
    _HpnicfVoEntityIndex_Type()
)
hpnicfVoEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVoEntityIndex.setStatus("current")


class _HpnicfVoEntityType_Type(Integer32):
    """Custom type hpnicfVoEntityType based on Integer32"""
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


_HpnicfVoEntityType_Type.__name__ = "Integer32"
_HpnicfVoEntityType_Object = MibTableColumn
hpnicfVoEntityType = _HpnicfVoEntityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 1, 1, 2),
    _HpnicfVoEntityType_Type()
)
hpnicfVoEntityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVoEntityType.setStatus("current")
_HpnicfVoEntityRowStatus_Type = RowStatus
_HpnicfVoEntityRowStatus_Object = MibTableColumn
hpnicfVoEntityRowStatus = _HpnicfVoEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 1, 1, 3),
    _HpnicfVoEntityRowStatus_Type()
)
hpnicfVoEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVoEntityRowStatus.setStatus("current")
_HpnicfVoEntityCommonConfigTable_Object = MibTable
hpnicfVoEntityCommonConfigTable = _HpnicfVoEntityCommonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfVoEntityCommonConfigTable.setStatus("current")
_HpnicfVoEntityCommonConfigEntry_Object = MibTableRow
hpnicfVoEntityCommonConfigEntry = _HpnicfVoEntityCommonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1)
)
hpnicfVoEntityCommonConfigEntry.setIndexNames(
    (0, "HPN-ICF-VOICE-DIAL-CONTROL-MIB", "hpnicfVoEntityCfgIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVoEntityCommonConfigEntry.setStatus("current")


class _HpnicfVoEntityCfgIndex_Type(Integer32):
    """Custom type hpnicfVoEntityCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfVoEntityCfgIndex_Type.__name__ = "Integer32"
_HpnicfVoEntityCfgIndex_Object = MibTableColumn
hpnicfVoEntityCfgIndex = _HpnicfVoEntityCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 1),
    _HpnicfVoEntityCfgIndex_Type()
)
hpnicfVoEntityCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgIndex.setStatus("current")
_HpnicfVoEntityCfgCodec1st_Type = HpnicfCodecType
_HpnicfVoEntityCfgCodec1st_Object = MibTableColumn
hpnicfVoEntityCfgCodec1st = _HpnicfVoEntityCfgCodec1st_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 2),
    _HpnicfVoEntityCfgCodec1st_Type()
)
hpnicfVoEntityCfgCodec1st.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgCodec1st.setStatus("current")
_HpnicfVoEntityCfgCodec2nd_Type = HpnicfCodecType
_HpnicfVoEntityCfgCodec2nd_Object = MibTableColumn
hpnicfVoEntityCfgCodec2nd = _HpnicfVoEntityCfgCodec2nd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 3),
    _HpnicfVoEntityCfgCodec2nd_Type()
)
hpnicfVoEntityCfgCodec2nd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgCodec2nd.setStatus("current")
_HpnicfVoEntityCfgCodec3rd_Type = HpnicfCodecType
_HpnicfVoEntityCfgCodec3rd_Object = MibTableColumn
hpnicfVoEntityCfgCodec3rd = _HpnicfVoEntityCfgCodec3rd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 4),
    _HpnicfVoEntityCfgCodec3rd_Type()
)
hpnicfVoEntityCfgCodec3rd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgCodec3rd.setStatus("current")
_HpnicfVoEntityCfgCodec4th_Type = HpnicfCodecType
_HpnicfVoEntityCfgCodec4th_Object = MibTableColumn
hpnicfVoEntityCfgCodec4th = _HpnicfVoEntityCfgCodec4th_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 5),
    _HpnicfVoEntityCfgCodec4th_Type()
)
hpnicfVoEntityCfgCodec4th.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgCodec4th.setStatus("current")


class _HpnicfVoEntityCfgDSCP_Type(Integer32):
    """Custom type hpnicfVoEntityCfgDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfVoEntityCfgDSCP_Type.__name__ = "Integer32"
_HpnicfVoEntityCfgDSCP_Object = MibTableColumn
hpnicfVoEntityCfgDSCP = _HpnicfVoEntityCfgDSCP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 6),
    _HpnicfVoEntityCfgDSCP_Type()
)
hpnicfVoEntityCfgDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgDSCP.setStatus("current")
_HpnicfVoEntityCfgVADEnable_Type = TruthValue
_HpnicfVoEntityCfgVADEnable_Object = MibTableColumn
hpnicfVoEntityCfgVADEnable = _HpnicfVoEntityCfgVADEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 7),
    _HpnicfVoEntityCfgVADEnable_Type()
)
hpnicfVoEntityCfgVADEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgVADEnable.setStatus("current")
_HpnicfVoEntityCfgOutbandMode_Type = HpnicfOutBandMode
_HpnicfVoEntityCfgOutbandMode_Object = MibTableColumn
hpnicfVoEntityCfgOutbandMode = _HpnicfVoEntityCfgOutbandMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 8),
    _HpnicfVoEntityCfgOutbandMode_Type()
)
hpnicfVoEntityCfgOutbandMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgOutbandMode.setStatus("current")


class _HpnicfVoEntityCfgFaxLevel_Type(Integer32):
    """Custom type hpnicfVoEntityCfgFaxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, -3),
    )


_HpnicfVoEntityCfgFaxLevel_Type.__name__ = "Integer32"
_HpnicfVoEntityCfgFaxLevel_Object = MibTableColumn
hpnicfVoEntityCfgFaxLevel = _HpnicfVoEntityCfgFaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 9),
    _HpnicfVoEntityCfgFaxLevel_Type()
)
hpnicfVoEntityCfgFaxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgFaxLevel.setStatus("current")
_HpnicfVoEntityCfgFaxBaudrate_Type = HpnicfFaxBaudrateType
_HpnicfVoEntityCfgFaxBaudrate_Object = MibTableColumn
hpnicfVoEntityCfgFaxBaudrate = _HpnicfVoEntityCfgFaxBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 10),
    _HpnicfVoEntityCfgFaxBaudrate_Type()
)
hpnicfVoEntityCfgFaxBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgFaxBaudrate.setStatus("current")


class _HpnicfVoEntityCfgFaxLocalTrainPara_Type(Integer32):
    """Custom type hpnicfVoEntityCfgFaxLocalTrainPara based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfVoEntityCfgFaxLocalTrainPara_Type.__name__ = "Integer32"
_HpnicfVoEntityCfgFaxLocalTrainPara_Object = MibTableColumn
hpnicfVoEntityCfgFaxLocalTrainPara = _HpnicfVoEntityCfgFaxLocalTrainPara_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 11),
    _HpnicfVoEntityCfgFaxLocalTrainPara_Type()
)
hpnicfVoEntityCfgFaxLocalTrainPara.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgFaxLocalTrainPara.setStatus("current")
_HpnicfVoEntityCfgFaxProtocol_Type = HpnicfFaxProtocolType
_HpnicfVoEntityCfgFaxProtocol_Object = MibTableColumn
hpnicfVoEntityCfgFaxProtocol = _HpnicfVoEntityCfgFaxProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 12),
    _HpnicfVoEntityCfgFaxProtocol_Type()
)
hpnicfVoEntityCfgFaxProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgFaxProtocol.setStatus("current")


class _HpnicfVoEntityCfgFaxHRPackNum_Type(Integer32):
    """Custom type hpnicfVoEntityCfgFaxHRPackNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HpnicfVoEntityCfgFaxHRPackNum_Type.__name__ = "Integer32"
_HpnicfVoEntityCfgFaxHRPackNum_Object = MibTableColumn
hpnicfVoEntityCfgFaxHRPackNum = _HpnicfVoEntityCfgFaxHRPackNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 13),
    _HpnicfVoEntityCfgFaxHRPackNum_Type()
)
hpnicfVoEntityCfgFaxHRPackNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgFaxHRPackNum.setStatus("current")


class _HpnicfVoEntityCfgFaxLRPackNum_Type(Integer32):
    """Custom type hpnicfVoEntityCfgFaxLRPackNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HpnicfVoEntityCfgFaxLRPackNum_Type.__name__ = "Integer32"
_HpnicfVoEntityCfgFaxLRPackNum_Object = MibTableColumn
hpnicfVoEntityCfgFaxLRPackNum = _HpnicfVoEntityCfgFaxLRPackNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 14),
    _HpnicfVoEntityCfgFaxLRPackNum_Type()
)
hpnicfVoEntityCfgFaxLRPackNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgFaxLRPackNum.setStatus("current")
_HpnicfVoEntityCfgFaxSendNSFEnable_Type = TruthValue
_HpnicfVoEntityCfgFaxSendNSFEnable_Object = MibTableColumn
hpnicfVoEntityCfgFaxSendNSFEnable = _HpnicfVoEntityCfgFaxSendNSFEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 15),
    _HpnicfVoEntityCfgFaxSendNSFEnable_Type()
)
hpnicfVoEntityCfgFaxSendNSFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgFaxSendNSFEnable.setStatus("current")
_HpnicfVoEntityCfgFaxTrainMode_Type = HpnicfFaxTrainMode
_HpnicfVoEntityCfgFaxTrainMode_Object = MibTableColumn
hpnicfVoEntityCfgFaxTrainMode = _HpnicfVoEntityCfgFaxTrainMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 16),
    _HpnicfVoEntityCfgFaxTrainMode_Type()
)
hpnicfVoEntityCfgFaxTrainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgFaxTrainMode.setStatus("current")
_HpnicfVoEntityCfgFaxEcm_Type = TruthValue
_HpnicfVoEntityCfgFaxEcm_Object = MibTableColumn
hpnicfVoEntityCfgFaxEcm = _HpnicfVoEntityCfgFaxEcm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 17),
    _HpnicfVoEntityCfgFaxEcm_Type()
)
hpnicfVoEntityCfgFaxEcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgFaxEcm.setStatus("current")


class _HpnicfVoEntityCfgPriority_Type(Integer32):
    """Custom type hpnicfVoEntityCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HpnicfVoEntityCfgPriority_Type.__name__ = "Integer32"
_HpnicfVoEntityCfgPriority_Object = MibTableColumn
hpnicfVoEntityCfgPriority = _HpnicfVoEntityCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 18),
    _HpnicfVoEntityCfgPriority_Type()
)
hpnicfVoEntityCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgPriority.setStatus("current")


class _HpnicfVoEntityCfgDescription_Type(OctetString):
    """Custom type hpnicfVoEntityCfgDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HpnicfVoEntityCfgDescription_Type.__name__ = "OctetString"
_HpnicfVoEntityCfgDescription_Object = MibTableColumn
hpnicfVoEntityCfgDescription = _HpnicfVoEntityCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 2, 1, 19),
    _HpnicfVoEntityCfgDescription_Type()
)
hpnicfVoEntityCfgDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityCfgDescription.setStatus("current")
_HpnicfVoPOTSEntityConfigTable_Object = MibTable
hpnicfVoPOTSEntityConfigTable = _HpnicfVoPOTSEntityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfVoPOTSEntityConfigTable.setStatus("current")
_HpnicfVoPOTSEntityConfigEntry_Object = MibTableRow
hpnicfVoPOTSEntityConfigEntry = _HpnicfVoPOTSEntityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 3, 1)
)
hpnicfVoPOTSEntityConfigEntry.setIndexNames(
    (0, "HPN-ICF-VOICE-DIAL-CONTROL-MIB", "hpnicfVoPOTSEntityConfigIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVoPOTSEntityConfigEntry.setStatus("current")


class _HpnicfVoPOTSEntityConfigIndex_Type(Integer32):
    """Custom type hpnicfVoPOTSEntityConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfVoPOTSEntityConfigIndex_Type.__name__ = "Integer32"
_HpnicfVoPOTSEntityConfigIndex_Object = MibTableColumn
hpnicfVoPOTSEntityConfigIndex = _HpnicfVoPOTSEntityConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 3, 1, 1),
    _HpnicfVoPOTSEntityConfigIndex_Type()
)
hpnicfVoPOTSEntityConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVoPOTSEntityConfigIndex.setStatus("current")


class _HpnicfVoPOTSEntityConfigPrefix_Type(OctetString):
    """Custom type hpnicfVoPOTSEntityConfigPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfVoPOTSEntityConfigPrefix_Type.__name__ = "OctetString"
_HpnicfVoPOTSEntityConfigPrefix_Object = MibTableColumn
hpnicfVoPOTSEntityConfigPrefix = _HpnicfVoPOTSEntityConfigPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 3, 1, 2),
    _HpnicfVoPOTSEntityConfigPrefix_Type()
)
hpnicfVoPOTSEntityConfigPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoPOTSEntityConfigPrefix.setStatus("current")
_HpnicfVoPOTSEntityConfigSubLine_Type = OctetString
_HpnicfVoPOTSEntityConfigSubLine_Object = MibTableColumn
hpnicfVoPOTSEntityConfigSubLine = _HpnicfVoPOTSEntityConfigSubLine_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 3, 1, 3),
    _HpnicfVoPOTSEntityConfigSubLine_Type()
)
hpnicfVoPOTSEntityConfigSubLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoPOTSEntityConfigSubLine.setStatus("current")


class _HpnicfVoPOTSEntityConfigSendNum_Type(Integer32):
    """Custom type hpnicfVoPOTSEntityConfigSendNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(65534, 65534),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfVoPOTSEntityConfigSendNum_Type.__name__ = "Integer32"
_HpnicfVoPOTSEntityConfigSendNum_Object = MibTableColumn
hpnicfVoPOTSEntityConfigSendNum = _HpnicfVoPOTSEntityConfigSendNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 3, 1, 4),
    _HpnicfVoPOTSEntityConfigSendNum_Type()
)
hpnicfVoPOTSEntityConfigSendNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoPOTSEntityConfigSendNum.setStatus("current")
_HpnicfVoVoIPEntityConfigTable_Object = MibTable
hpnicfVoVoIPEntityConfigTable = _HpnicfVoVoIPEntityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfVoVoIPEntityConfigTable.setStatus("current")
_HpnicfVoVoIPEntityConfigEntry_Object = MibTableRow
hpnicfVoVoIPEntityConfigEntry = _HpnicfVoVoIPEntityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 4, 1)
)
hpnicfVoVoIPEntityConfigEntry.setIndexNames(
    (0, "HPN-ICF-VOICE-DIAL-CONTROL-MIB", "hpnicfVoVoIPEntityCfgIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVoVoIPEntityConfigEntry.setStatus("current")


class _HpnicfVoVoIPEntityCfgIndex_Type(Integer32):
    """Custom type hpnicfVoVoIPEntityCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfVoVoIPEntityCfgIndex_Type.__name__ = "Integer32"
_HpnicfVoVoIPEntityCfgIndex_Object = MibTableColumn
hpnicfVoVoIPEntityCfgIndex = _HpnicfVoVoIPEntityCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 4, 1, 1),
    _HpnicfVoVoIPEntityCfgIndex_Type()
)
hpnicfVoVoIPEntityCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVoVoIPEntityCfgIndex.setStatus("current")


class _HpnicfVoVoIPEntityCfgTargetType_Type(Integer32):
    """Custom type hpnicfVoVoIPEntityCfgTargetType based on Integer32"""
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


_HpnicfVoVoIPEntityCfgTargetType_Type.__name__ = "Integer32"
_HpnicfVoVoIPEntityCfgTargetType_Object = MibTableColumn
hpnicfVoVoIPEntityCfgTargetType = _HpnicfVoVoIPEntityCfgTargetType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 4, 1, 2),
    _HpnicfVoVoIPEntityCfgTargetType_Type()
)
hpnicfVoVoIPEntityCfgTargetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoVoIPEntityCfgTargetType.setStatus("current")
_HpnicfVoVoIPEntityCfgTargetAddrType_Type = InetAddressType
_HpnicfVoVoIPEntityCfgTargetAddrType_Object = MibTableColumn
hpnicfVoVoIPEntityCfgTargetAddrType = _HpnicfVoVoIPEntityCfgTargetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 4, 1, 3),
    _HpnicfVoVoIPEntityCfgTargetAddrType_Type()
)
hpnicfVoVoIPEntityCfgTargetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoVoIPEntityCfgTargetAddrType.setStatus("current")
_HpnicfVoVoIPEntityCfgTargetAddr_Type = InetAddress
_HpnicfVoVoIPEntityCfgTargetAddr_Object = MibTableColumn
hpnicfVoVoIPEntityCfgTargetAddr = _HpnicfVoVoIPEntityCfgTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 4, 1, 4),
    _HpnicfVoVoIPEntityCfgTargetAddr_Type()
)
hpnicfVoVoIPEntityCfgTargetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoVoIPEntityCfgTargetAddr.setStatus("current")
_HpnicfVoEntityNumberTable_Object = MibTable
hpnicfVoEntityNumberTable = _HpnicfVoEntityNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfVoEntityNumberTable.setStatus("current")
_HpnicfVoEntityNumberEntry_Object = MibTableRow
hpnicfVoEntityNumberEntry = _HpnicfVoEntityNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 5, 1)
)
hpnicfVoEntityNumberEntry.setIndexNames(
    (0, "HPN-ICF-VOICE-DIAL-CONTROL-MIB", "hpnicfVoEntityIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVoEntityNumberEntry.setStatus("current")


class _HpnicfVoEntityNumberAuthUser_Type(OctetString):
    """Custom type hpnicfVoEntityNumberAuthUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfVoEntityNumberAuthUser_Type.__name__ = "OctetString"
_HpnicfVoEntityNumberAuthUser_Object = MibTableColumn
hpnicfVoEntityNumberAuthUser = _HpnicfVoEntityNumberAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 5, 1, 1),
    _HpnicfVoEntityNumberAuthUser_Type()
)
hpnicfVoEntityNumberAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityNumberAuthUser.setStatus("current")
_HpnicfVoEntityNumberPasswordType_Type = Integer32
_HpnicfVoEntityNumberPasswordType_Object = MibTableColumn
hpnicfVoEntityNumberPasswordType = _HpnicfVoEntityNumberPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 5, 1, 2),
    _HpnicfVoEntityNumberPasswordType_Type()
)
hpnicfVoEntityNumberPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityNumberPasswordType.setStatus("current")


class _HpnicfVoEntityNumberPassword_Type(OctetString):
    """Custom type hpnicfVoEntityNumberPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
        ValueSizeConstraint(24, 24),
    )


_HpnicfVoEntityNumberPassword_Type.__name__ = "OctetString"
_HpnicfVoEntityNumberPassword_Object = MibTableColumn
hpnicfVoEntityNumberPassword = _HpnicfVoEntityNumberPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 5, 1, 3),
    _HpnicfVoEntityNumberPassword_Type()
)
hpnicfVoEntityNumberPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoEntityNumberPassword.setStatus("current")
_HpnicfVoEntityNumberStatus_Type = HpnicfRegisterdStatus
_HpnicfVoEntityNumberStatus_Object = MibTableColumn
hpnicfVoEntityNumberStatus = _HpnicfVoEntityNumberStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 5, 1, 4),
    _HpnicfVoEntityNumberStatus_Type()
)
hpnicfVoEntityNumberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoEntityNumberStatus.setStatus("current")
_HpnicfVoEntityNumberExpires_Type = Integer32
_HpnicfVoEntityNumberExpires_Object = MibTableColumn
hpnicfVoEntityNumberExpires = _HpnicfVoEntityNumberExpires_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 14, 1, 5, 1, 5),
    _HpnicfVoEntityNumberExpires_Type()
)
hpnicfVoEntityNumberExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoEntityNumberExpires.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfVoEntityNumberExpires.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-VOICE-DIAL-CONTROL-MIB",
    **{"HpnicfCodecType": HpnicfCodecType,
       "HpnicfOutBandMode": HpnicfOutBandMode,
       "HpnicfFaxProtocolType": HpnicfFaxProtocolType,
       "HpnicfFaxBaudrateType": HpnicfFaxBaudrateType,
       "HpnicfFaxTrainMode": HpnicfFaxTrainMode,
       "HpnicfRegisterdStatus": HpnicfRegisterdStatus,
       "hpnicfVoiceEntityControl": hpnicfVoiceEntityControl,
       "hpnicfVoEntityObjects": hpnicfVoEntityObjects,
       "hpnicfVoEntityCreateTable": hpnicfVoEntityCreateTable,
       "hpnicfVoEntityCreateEntry": hpnicfVoEntityCreateEntry,
       "hpnicfVoEntityIndex": hpnicfVoEntityIndex,
       "hpnicfVoEntityType": hpnicfVoEntityType,
       "hpnicfVoEntityRowStatus": hpnicfVoEntityRowStatus,
       "hpnicfVoEntityCommonConfigTable": hpnicfVoEntityCommonConfigTable,
       "hpnicfVoEntityCommonConfigEntry": hpnicfVoEntityCommonConfigEntry,
       "hpnicfVoEntityCfgIndex": hpnicfVoEntityCfgIndex,
       "hpnicfVoEntityCfgCodec1st": hpnicfVoEntityCfgCodec1st,
       "hpnicfVoEntityCfgCodec2nd": hpnicfVoEntityCfgCodec2nd,
       "hpnicfVoEntityCfgCodec3rd": hpnicfVoEntityCfgCodec3rd,
       "hpnicfVoEntityCfgCodec4th": hpnicfVoEntityCfgCodec4th,
       "hpnicfVoEntityCfgDSCP": hpnicfVoEntityCfgDSCP,
       "hpnicfVoEntityCfgVADEnable": hpnicfVoEntityCfgVADEnable,
       "hpnicfVoEntityCfgOutbandMode": hpnicfVoEntityCfgOutbandMode,
       "hpnicfVoEntityCfgFaxLevel": hpnicfVoEntityCfgFaxLevel,
       "hpnicfVoEntityCfgFaxBaudrate": hpnicfVoEntityCfgFaxBaudrate,
       "hpnicfVoEntityCfgFaxLocalTrainPara": hpnicfVoEntityCfgFaxLocalTrainPara,
       "hpnicfVoEntityCfgFaxProtocol": hpnicfVoEntityCfgFaxProtocol,
       "hpnicfVoEntityCfgFaxHRPackNum": hpnicfVoEntityCfgFaxHRPackNum,
       "hpnicfVoEntityCfgFaxLRPackNum": hpnicfVoEntityCfgFaxLRPackNum,
       "hpnicfVoEntityCfgFaxSendNSFEnable": hpnicfVoEntityCfgFaxSendNSFEnable,
       "hpnicfVoEntityCfgFaxTrainMode": hpnicfVoEntityCfgFaxTrainMode,
       "hpnicfVoEntityCfgFaxEcm": hpnicfVoEntityCfgFaxEcm,
       "hpnicfVoEntityCfgPriority": hpnicfVoEntityCfgPriority,
       "hpnicfVoEntityCfgDescription": hpnicfVoEntityCfgDescription,
       "hpnicfVoPOTSEntityConfigTable": hpnicfVoPOTSEntityConfigTable,
       "hpnicfVoPOTSEntityConfigEntry": hpnicfVoPOTSEntityConfigEntry,
       "hpnicfVoPOTSEntityConfigIndex": hpnicfVoPOTSEntityConfigIndex,
       "hpnicfVoPOTSEntityConfigPrefix": hpnicfVoPOTSEntityConfigPrefix,
       "hpnicfVoPOTSEntityConfigSubLine": hpnicfVoPOTSEntityConfigSubLine,
       "hpnicfVoPOTSEntityConfigSendNum": hpnicfVoPOTSEntityConfigSendNum,
       "hpnicfVoVoIPEntityConfigTable": hpnicfVoVoIPEntityConfigTable,
       "hpnicfVoVoIPEntityConfigEntry": hpnicfVoVoIPEntityConfigEntry,
       "hpnicfVoVoIPEntityCfgIndex": hpnicfVoVoIPEntityCfgIndex,
       "hpnicfVoVoIPEntityCfgTargetType": hpnicfVoVoIPEntityCfgTargetType,
       "hpnicfVoVoIPEntityCfgTargetAddrType": hpnicfVoVoIPEntityCfgTargetAddrType,
       "hpnicfVoVoIPEntityCfgTargetAddr": hpnicfVoVoIPEntityCfgTargetAddr,
       "hpnicfVoEntityNumberTable": hpnicfVoEntityNumberTable,
       "hpnicfVoEntityNumberEntry": hpnicfVoEntityNumberEntry,
       "hpnicfVoEntityNumberAuthUser": hpnicfVoEntityNumberAuthUser,
       "hpnicfVoEntityNumberPasswordType": hpnicfVoEntityNumberPasswordType,
       "hpnicfVoEntityNumberPassword": hpnicfVoEntityNumberPassword,
       "hpnicfVoEntityNumberStatus": hpnicfVoEntityNumberStatus,
       "hpnicfVoEntityNumberExpires": hpnicfVoEntityNumberExpires}
)
