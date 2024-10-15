# SNMP MIB module (A3COM-HUAWEI-VODIALCONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-VODIALCONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:20 2024
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

(h3cVoice,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cVoice")

(CodecType,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-VO-TYPE-MIB",
    "CodecType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cVoiceDialControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5)
)
h3cVoiceDialControl.setRevisions(
        ("2005-03-15 00:00",)
)


# Types definitions



class FaxProtocolType(Integer32):
    """Custom type FaxProtocolType based on Integer32"""
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
        *(("h323T38", 3),
          ("nonstandardCompatible", 1),
          ("pcmG711alaw", 5),
          ("pcmG711ulaw", 6),
          ("sipT38", 4),
          ("t38", 2))
    )





class FaxBaudrateType(Integer32):
    """Custom type FaxBaudrateType based on Integer32"""
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





class FaxSupportModeType(Integer32):
    """Custom type FaxSupportModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rtp", 1),
          ("sip-udp", 3),
          ("vt", 2))
    )





class FaxTrainMode(Integer32):
    """Custom type FaxTrainMode based on Integer32"""
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





class PhoneNumberType(Integer32):
    """Custom type PhoneNumberType based on Integer32"""
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
        *(("abbreviated", 2),
          ("initial", 8),
          ("international", 3),
          ("national", 4),
          ("network", 5),
          ("reserved", 6),
          ("subscriber", 7),
          ("unknown", 1))
    )





class PhoneNumberPlan(Integer32):
    """Custom type PhoneNumberPlan based on Integer32"""
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
        *(("data", 2),
          ("initial", 8),
          ("isdn", 3),
          ("national", 4),
          ("private", 5),
          ("reserved", 6),
          ("telex", 7),
          ("unknown", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVoPeerObjects_ObjectIdentity = ObjectIdentity
h3cVoPeerObjects = _H3cVoPeerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1)
)
_H3cVoPeerCommonConfigTable_Object = MibTable
h3cVoPeerCommonConfigTable = _H3cVoPeerCommonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVoPeerCommonConfigTable.setStatus("current")
_H3cVoPeerCommonConfigEntry_Object = MibTableRow
h3cVoPeerCommonConfigEntry = _H3cVoPeerCommonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1)
)
h3cVoPeerCommonConfigEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIALCONTROL-MIB", "h3cVoPeerCfgIndex"),
)
if mibBuilder.loadTexts:
    h3cVoPeerCommonConfigEntry.setStatus("current")


class _H3cVoPeerCfgIndex_Type(Integer32):
    """Custom type h3cVoPeerCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoPeerCfgIndex_Type.__name__ = "Integer32"
_H3cVoPeerCfgIndex_Object = MibTableColumn
h3cVoPeerCfgIndex = _H3cVoPeerCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 1),
    _H3cVoPeerCfgIndex_Type()
)
h3cVoPeerCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoPeerCfgIndex.setStatus("current")
_H3cVoPeerCfgRowStatus_Type = RowStatus
_H3cVoPeerCfgRowStatus_Object = MibTableColumn
h3cVoPeerCfgRowStatus = _H3cVoPeerCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 2),
    _H3cVoPeerCfgRowStatus_Type()
)
h3cVoPeerCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgRowStatus.setStatus("current")


class _H3cVoPeerCfgType_Type(Integer32):
    """Custom type h3cVoPeerCfgType based on Integer32"""
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


_H3cVoPeerCfgType_Type.__name__ = "Integer32"
_H3cVoPeerCfgType_Object = MibTableColumn
h3cVoPeerCfgType = _H3cVoPeerCfgType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 3),
    _H3cVoPeerCfgType_Type()
)
h3cVoPeerCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgType.setStatus("current")
_H3cVoPeerCfgDesPattern_Type = OctetString
_H3cVoPeerCfgDesPattern_Object = MibTableColumn
h3cVoPeerCfgDesPattern = _H3cVoPeerCfgDesPattern_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 4),
    _H3cVoPeerCfgDesPattern_Type()
)
h3cVoPeerCfgDesPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgDesPattern.setStatus("current")
_H3cVoPeerCfgCodec1st_Type = CodecType
_H3cVoPeerCfgCodec1st_Object = MibTableColumn
h3cVoPeerCfgCodec1st = _H3cVoPeerCfgCodec1st_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 5),
    _H3cVoPeerCfgCodec1st_Type()
)
h3cVoPeerCfgCodec1st.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgCodec1st.setStatus("current")
_H3cVoPeerCfgCodec2nd_Type = CodecType
_H3cVoPeerCfgCodec2nd_Object = MibTableColumn
h3cVoPeerCfgCodec2nd = _H3cVoPeerCfgCodec2nd_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 6),
    _H3cVoPeerCfgCodec2nd_Type()
)
h3cVoPeerCfgCodec2nd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgCodec2nd.setStatus("current")
_H3cVoPeerCfgCodec3rd_Type = CodecType
_H3cVoPeerCfgCodec3rd_Object = MibTableColumn
h3cVoPeerCfgCodec3rd = _H3cVoPeerCfgCodec3rd_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 7),
    _H3cVoPeerCfgCodec3rd_Type()
)
h3cVoPeerCfgCodec3rd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgCodec3rd.setStatus("current")
_H3cVoPeerCfgCodec4th_Type = CodecType
_H3cVoPeerCfgCodec4th_Object = MibTableColumn
h3cVoPeerCfgCodec4th = _H3cVoPeerCfgCodec4th_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 8),
    _H3cVoPeerCfgCodec4th_Type()
)
h3cVoPeerCfgCodec4th.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgCodec4th.setStatus("current")
_H3cVoPeerCfgDSCP_Type = Integer32
_H3cVoPeerCfgDSCP_Object = MibTableColumn
h3cVoPeerCfgDSCP = _H3cVoPeerCfgDSCP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 9),
    _H3cVoPeerCfgDSCP_Type()
)
h3cVoPeerCfgDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgDSCP.setStatus("current")


class _H3cVoPeerCfgShutDown_Type(Integer32):
    """Custom type h3cVoPeerCfgShutDown based on Integer32"""
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


_H3cVoPeerCfgShutDown_Type.__name__ = "Integer32"
_H3cVoPeerCfgShutDown_Object = MibTableColumn
h3cVoPeerCfgShutDown = _H3cVoPeerCfgShutDown_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 10),
    _H3cVoPeerCfgShutDown_Type()
)
h3cVoPeerCfgShutDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgShutDown.setStatus("current")


class _H3cVoPeerCfgVADEnable_Type(Integer32):
    """Custom type h3cVoPeerCfgVADEnable based on Integer32"""
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


_H3cVoPeerCfgVADEnable_Type.__name__ = "Integer32"
_H3cVoPeerCfgVADEnable_Object = MibTableColumn
h3cVoPeerCfgVADEnable = _H3cVoPeerCfgVADEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 11),
    _H3cVoPeerCfgVADEnable_Type()
)
h3cVoPeerCfgVADEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgVADEnable.setStatus("current")


class _H3cVoPeerCfgOutbandMode_Type(Integer32):
    """Custom type h3cVoPeerCfgOutbandMode based on Integer32"""
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
        *(("h225", 4),
          ("h245", 1),
          ("sip", 3),
          ("voice", 2))
    )


_H3cVoPeerCfgOutbandMode_Type.__name__ = "Integer32"
_H3cVoPeerCfgOutbandMode_Object = MibTableColumn
h3cVoPeerCfgOutbandMode = _H3cVoPeerCfgOutbandMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 12),
    _H3cVoPeerCfgOutbandMode_Type()
)
h3cVoPeerCfgOutbandMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgOutbandMode.setStatus("current")
_H3cVoPeerCfgFaxLevel_Type = Integer32
_H3cVoPeerCfgFaxLevel_Object = MibTableColumn
h3cVoPeerCfgFaxLevel = _H3cVoPeerCfgFaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 13),
    _H3cVoPeerCfgFaxLevel_Type()
)
h3cVoPeerCfgFaxLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgFaxLevel.setStatus("current")
_H3cVoPeerCfgFaxBaudrate_Type = FaxBaudrateType
_H3cVoPeerCfgFaxBaudrate_Object = MibTableColumn
h3cVoPeerCfgFaxBaudrate = _H3cVoPeerCfgFaxBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 14),
    _H3cVoPeerCfgFaxBaudrate_Type()
)
h3cVoPeerCfgFaxBaudrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgFaxBaudrate.setStatus("current")
_H3cVoPeerCfgFaxLocalTrainPara_Type = Integer32
_H3cVoPeerCfgFaxLocalTrainPara_Object = MibTableColumn
h3cVoPeerCfgFaxLocalTrainPara = _H3cVoPeerCfgFaxLocalTrainPara_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 15),
    _H3cVoPeerCfgFaxLocalTrainPara_Type()
)
h3cVoPeerCfgFaxLocalTrainPara.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgFaxLocalTrainPara.setStatus("current")
_H3cVoPeerCfgFaxProtocol_Type = FaxProtocolType
_H3cVoPeerCfgFaxProtocol_Object = MibTableColumn
h3cVoPeerCfgFaxProtocol = _H3cVoPeerCfgFaxProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 16),
    _H3cVoPeerCfgFaxProtocol_Type()
)
h3cVoPeerCfgFaxProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgFaxProtocol.setStatus("current")


class _H3cVoPeerCfgT38FaxHRPackNum_Type(Integer32):
    """Custom type h3cVoPeerCfgT38FaxHRPackNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_H3cVoPeerCfgT38FaxHRPackNum_Type.__name__ = "Integer32"
_H3cVoPeerCfgT38FaxHRPackNum_Object = MibTableColumn
h3cVoPeerCfgT38FaxHRPackNum = _H3cVoPeerCfgT38FaxHRPackNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 17),
    _H3cVoPeerCfgT38FaxHRPackNum_Type()
)
h3cVoPeerCfgT38FaxHRPackNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgT38FaxHRPackNum.setStatus("current")


class _H3cVoPeerCfgT38FaxLRPackNum_Type(Integer32):
    """Custom type h3cVoPeerCfgT38FaxLRPackNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_H3cVoPeerCfgT38FaxLRPackNum_Type.__name__ = "Integer32"
_H3cVoPeerCfgT38FaxLRPackNum_Object = MibTableColumn
h3cVoPeerCfgT38FaxLRPackNum = _H3cVoPeerCfgT38FaxLRPackNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 18),
    _H3cVoPeerCfgT38FaxLRPackNum_Type()
)
h3cVoPeerCfgT38FaxLRPackNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgT38FaxLRPackNum.setStatus("current")


class _H3cVoPeerCfgFaxSendNSFEnable_Type(Integer32):
    """Custom type h3cVoPeerCfgFaxSendNSFEnable based on Integer32"""
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


_H3cVoPeerCfgFaxSendNSFEnable_Type.__name__ = "Integer32"
_H3cVoPeerCfgFaxSendNSFEnable_Object = MibTableColumn
h3cVoPeerCfgFaxSendNSFEnable = _H3cVoPeerCfgFaxSendNSFEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 19),
    _H3cVoPeerCfgFaxSendNSFEnable_Type()
)
h3cVoPeerCfgFaxSendNSFEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgFaxSendNSFEnable.setStatus("current")
_H3cVoPeerCfgFaxSupportMode_Type = FaxSupportModeType
_H3cVoPeerCfgFaxSupportMode_Object = MibTableColumn
h3cVoPeerCfgFaxSupportMode = _H3cVoPeerCfgFaxSupportMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 20),
    _H3cVoPeerCfgFaxSupportMode_Type()
)
h3cVoPeerCfgFaxSupportMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgFaxSupportMode.setStatus("current")
_H3cVoPeerCfgFaxTrainMode_Type = FaxTrainMode
_H3cVoPeerCfgFaxTrainMode_Object = MibTableColumn
h3cVoPeerCfgFaxTrainMode = _H3cVoPeerCfgFaxTrainMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 21),
    _H3cVoPeerCfgFaxTrainMode_Type()
)
h3cVoPeerCfgFaxTrainMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgFaxTrainMode.setStatus("current")


class _H3cVoPeerCfgFaxEcm_Type(Integer32):
    """Custom type h3cVoPeerCfgFaxEcm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disalbe", 2),
          ("enable", 1))
    )


_H3cVoPeerCfgFaxEcm_Type.__name__ = "Integer32"
_H3cVoPeerCfgFaxEcm_Object = MibTableColumn
h3cVoPeerCfgFaxEcm = _H3cVoPeerCfgFaxEcm_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 22),
    _H3cVoPeerCfgFaxEcm_Type()
)
h3cVoPeerCfgFaxEcm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgFaxEcm.setStatus("current")
_H3cVoPeerCfgPriority_Type = Integer32
_H3cVoPeerCfgPriority_Object = MibTableColumn
h3cVoPeerCfgPriority = _H3cVoPeerCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 23),
    _H3cVoPeerCfgPriority_Type()
)
h3cVoPeerCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgPriority.setStatus("current")
_H3cVoPeerCfgDescription_Type = OctetString
_H3cVoPeerCfgDescription_Object = MibTableColumn
h3cVoPeerCfgDescription = _H3cVoPeerCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 24),
    _H3cVoPeerCfgDescription_Type()
)
h3cVoPeerCfgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgDescription.setStatus("current")
_H3cVoPeerCfgCallingNumberType_Type = PhoneNumberType
_H3cVoPeerCfgCallingNumberType_Object = MibTableColumn
h3cVoPeerCfgCallingNumberType = _H3cVoPeerCfgCallingNumberType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 25),
    _H3cVoPeerCfgCallingNumberType_Type()
)
h3cVoPeerCfgCallingNumberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgCallingNumberType.setStatus("current")
_H3cVoPeerCfgCalledNumberType_Type = PhoneNumberType
_H3cVoPeerCfgCalledNumberType_Object = MibTableColumn
h3cVoPeerCfgCalledNumberType = _H3cVoPeerCfgCalledNumberType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 26),
    _H3cVoPeerCfgCalledNumberType_Type()
)
h3cVoPeerCfgCalledNumberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgCalledNumberType.setStatus("current")
_H3cVoPeerCfgCallingNumberPlan_Type = PhoneNumberPlan
_H3cVoPeerCfgCallingNumberPlan_Object = MibTableColumn
h3cVoPeerCfgCallingNumberPlan = _H3cVoPeerCfgCallingNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 27),
    _H3cVoPeerCfgCallingNumberPlan_Type()
)
h3cVoPeerCfgCallingNumberPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgCallingNumberPlan.setStatus("current")
_H3cVoPeerCfgCalledNumberPlan_Type = PhoneNumberPlan
_H3cVoPeerCfgCalledNumberPlan_Object = MibTableColumn
h3cVoPeerCfgCalledNumberPlan = _H3cVoPeerCfgCalledNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 28),
    _H3cVoPeerCfgCalledNumberPlan_Type()
)
h3cVoPeerCfgCalledNumberPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgCalledNumberPlan.setStatus("current")


class _H3cVoPeerCfgSelectStop_Type(Integer32):
    """Custom type h3cVoPeerCfgSelectStop based on Integer32"""
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


_H3cVoPeerCfgSelectStop_Type.__name__ = "Integer32"
_H3cVoPeerCfgSelectStop_Object = MibTableColumn
h3cVoPeerCfgSelectStop = _H3cVoPeerCfgSelectStop_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 29),
    _H3cVoPeerCfgSelectStop_Type()
)
h3cVoPeerCfgSelectStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgSelectStop.setStatus("current")


class _H3cVoPeerCfgCallingNumSubstRule_Type(Integer32):
    """Custom type h3cVoPeerCfgCallingNumSubstRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cVoPeerCfgCallingNumSubstRule_Type.__name__ = "Integer32"
_H3cVoPeerCfgCallingNumSubstRule_Object = MibTableColumn
h3cVoPeerCfgCallingNumSubstRule = _H3cVoPeerCfgCallingNumSubstRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 30),
    _H3cVoPeerCfgCallingNumSubstRule_Type()
)
h3cVoPeerCfgCallingNumSubstRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgCallingNumSubstRule.setStatus("current")


class _H3cVoPeerCfgCalledNumSubstRule_Type(Integer32):
    """Custom type h3cVoPeerCfgCalledNumSubstRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cVoPeerCfgCalledNumSubstRule_Type.__name__ = "Integer32"
_H3cVoPeerCfgCalledNumSubstRule_Object = MibTableColumn
h3cVoPeerCfgCalledNumSubstRule = _H3cVoPeerCfgCalledNumSubstRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 31),
    _H3cVoPeerCfgCalledNumSubstRule_Type()
)
h3cVoPeerCfgCalledNumSubstRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgCalledNumSubstRule.setStatus("current")


class _H3cVoPeerCfgMaxCall_Type(Integer32):
    """Custom type h3cVoPeerCfgMaxCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cVoPeerCfgMaxCall_Type.__name__ = "Integer32"
_H3cVoPeerCfgMaxCall_Object = MibTableColumn
h3cVoPeerCfgMaxCall = _H3cVoPeerCfgMaxCall_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 1, 1, 32),
    _H3cVoPeerCfgMaxCall_Type()
)
h3cVoPeerCfgMaxCall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCfgMaxCall.setStatus("current")
_H3cVoPOTSPeerConfigTable_Object = MibTable
h3cVoPOTSPeerConfigTable = _H3cVoPOTSPeerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 2)
)
if mibBuilder.loadTexts:
    h3cVoPOTSPeerConfigTable.setStatus("current")
_H3cVoPOTSPeerConfigEntry_Object = MibTableRow
h3cVoPOTSPeerConfigEntry = _H3cVoPOTSPeerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 2, 1)
)
h3cVoPOTSPeerConfigEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIALCONTROL-MIB", "h3cVoPOTSPeerConfigIndex"),
)
if mibBuilder.loadTexts:
    h3cVoPOTSPeerConfigEntry.setStatus("current")


class _H3cVoPOTSPeerConfigIndex_Type(Integer32):
    """Custom type h3cVoPOTSPeerConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoPOTSPeerConfigIndex_Type.__name__ = "Integer32"
_H3cVoPOTSPeerConfigIndex_Object = MibTableColumn
h3cVoPOTSPeerConfigIndex = _H3cVoPOTSPeerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 2, 1, 1),
    _H3cVoPOTSPeerConfigIndex_Type()
)
h3cVoPOTSPeerConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoPOTSPeerConfigIndex.setStatus("current")
_H3cVoPOTSPeerConfigPrefix_Type = OctetString
_H3cVoPOTSPeerConfigPrefix_Object = MibTableColumn
h3cVoPOTSPeerConfigPrefix = _H3cVoPOTSPeerConfigPrefix_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 2, 1, 2),
    _H3cVoPOTSPeerConfigPrefix_Type()
)
h3cVoPOTSPeerConfigPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPOTSPeerConfigPrefix.setStatus("current")
_H3cVoPOTSPeerConfigSubLine_Type = OctetString
_H3cVoPOTSPeerConfigSubLine_Object = MibTableColumn
h3cVoPOTSPeerConfigSubLine = _H3cVoPOTSPeerConfigSubLine_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 2, 1, 3),
    _H3cVoPOTSPeerConfigSubLine_Type()
)
h3cVoPOTSPeerConfigSubLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPOTSPeerConfigSubLine.setStatus("current")
_H3cVoPOTSPeerConfigSendNum_Type = Integer32
_H3cVoPOTSPeerConfigSendNum_Object = MibTableColumn
h3cVoPOTSPeerConfigSendNum = _H3cVoPOTSPeerConfigSendNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 2, 1, 4),
    _H3cVoPOTSPeerConfigSendNum_Type()
)
h3cVoPOTSPeerConfigSendNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPOTSPeerConfigSendNum.setStatus("current")
_H3cVoVoIPPeerConfigTable_Object = MibTable
h3cVoVoIPPeerConfigTable = _H3cVoVoIPPeerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 3)
)
if mibBuilder.loadTexts:
    h3cVoVoIPPeerConfigTable.setStatus("current")
_H3cVoVoIPPeerConfigEntry_Object = MibTableRow
h3cVoVoIPPeerConfigEntry = _H3cVoVoIPPeerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 3, 1)
)
h3cVoVoIPPeerConfigEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIALCONTROL-MIB", "h3cVoVoIPPeerCfgIndex"),
)
if mibBuilder.loadTexts:
    h3cVoVoIPPeerConfigEntry.setStatus("current")


class _H3cVoVoIPPeerCfgIndex_Type(Integer32):
    """Custom type h3cVoVoIPPeerCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoVoIPPeerCfgIndex_Type.__name__ = "Integer32"
_H3cVoVoIPPeerCfgIndex_Object = MibTableColumn
h3cVoVoIPPeerCfgIndex = _H3cVoVoIPPeerCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 3, 1, 1),
    _H3cVoVoIPPeerCfgIndex_Type()
)
h3cVoVoIPPeerCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoVoIPPeerCfgIndex.setStatus("current")


class _H3cVoVoIPPeerCfgTargetType_Type(Integer32):
    """Custom type h3cVoVoIPPeerCfgTargetType based on Integer32"""
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


_H3cVoVoIPPeerCfgTargetType_Type.__name__ = "Integer32"
_H3cVoVoIPPeerCfgTargetType_Object = MibTableColumn
h3cVoVoIPPeerCfgTargetType = _H3cVoVoIPPeerCfgTargetType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 3, 1, 2),
    _H3cVoVoIPPeerCfgTargetType_Type()
)
h3cVoVoIPPeerCfgTargetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoVoIPPeerCfgTargetType.setStatus("current")
_H3cVoVoIPPeerCfgTargetAddrType_Type = InetAddressType
_H3cVoVoIPPeerCfgTargetAddrType_Object = MibTableColumn
h3cVoVoIPPeerCfgTargetAddrType = _H3cVoVoIPPeerCfgTargetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 3, 1, 3),
    _H3cVoVoIPPeerCfgTargetAddrType_Type()
)
h3cVoVoIPPeerCfgTargetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoVoIPPeerCfgTargetAddrType.setStatus("current")
_H3cVoVoIPPeerCfgTargetAddr_Type = InetAddress
_H3cVoVoIPPeerCfgTargetAddr_Object = MibTableColumn
h3cVoVoIPPeerCfgTargetAddr = _H3cVoVoIPPeerCfgTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 3, 1, 4),
    _H3cVoVoIPPeerCfgTargetAddr_Type()
)
h3cVoVoIPPeerCfgTargetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoVoIPPeerCfgTargetAddr.setStatus("current")


class _H3cVoVoIPPeerCfgFastStart_Type(Integer32):
    """Custom type h3cVoVoIPPeerCfgFastStart based on Integer32"""
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


_H3cVoVoIPPeerCfgFastStart_Type.__name__ = "Integer32"
_H3cVoVoIPPeerCfgFastStart_Object = MibTableColumn
h3cVoVoIPPeerCfgFastStart = _H3cVoVoIPPeerCfgFastStart_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 3, 1, 5),
    _H3cVoVoIPPeerCfgFastStart_Type()
)
h3cVoVoIPPeerCfgFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoVoIPPeerCfgFastStart.setStatus("current")


class _H3cVoVoIPPeerCfgTunnel_Type(Integer32):
    """Custom type h3cVoVoIPPeerCfgTunnel based on Integer32"""
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


_H3cVoVoIPPeerCfgTunnel_Type.__name__ = "Integer32"
_H3cVoVoIPPeerCfgTunnel_Object = MibTableColumn
h3cVoVoIPPeerCfgTunnel = _H3cVoVoIPPeerCfgTunnel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 3, 1, 6),
    _H3cVoVoIPPeerCfgTunnel_Type()
)
h3cVoVoIPPeerCfgTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoVoIPPeerCfgTunnel.setStatus("current")
_H3cVoVoIPPeerCfgAreaID_Type = OctetString
_H3cVoVoIPPeerCfgAreaID_Object = MibTableColumn
h3cVoVoIPPeerCfgAreaID = _H3cVoVoIPPeerCfgAreaID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 3, 1, 7),
    _H3cVoVoIPPeerCfgAreaID_Type()
)
h3cVoVoIPPeerCfgAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoVoIPPeerCfgAreaID.setStatus("current")


class _H3cVoVoIPPeerCfgSendRing_Type(Integer32):
    """Custom type h3cVoVoIPPeerCfgSendRing based on Integer32"""
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


_H3cVoVoIPPeerCfgSendRing_Type.__name__ = "Integer32"
_H3cVoVoIPPeerCfgSendRing_Object = MibTableColumn
h3cVoVoIPPeerCfgSendRing = _H3cVoVoIPPeerCfgSendRing_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 3, 1, 8),
    _H3cVoVoIPPeerCfgSendRing_Type()
)
h3cVoVoIPPeerCfgSendRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoVoIPPeerCfgSendRing.setStatus("current")
_H3cVoPeerDefaultConfigObjects_ObjectIdentity = ObjectIdentity
h3cVoPeerDefaultConfigObjects = _H3cVoPeerDefaultConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4)
)
_H3cVoPeerDefault1stCodecLevel_Type = CodecType
_H3cVoPeerDefault1stCodecLevel_Object = MibScalar
h3cVoPeerDefault1stCodecLevel = _H3cVoPeerDefault1stCodecLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 2),
    _H3cVoPeerDefault1stCodecLevel_Type()
)
h3cVoPeerDefault1stCodecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefault1stCodecLevel.setStatus("current")
_H3cVoPeerDefault2ndCodecLevel_Type = CodecType
_H3cVoPeerDefault2ndCodecLevel_Object = MibScalar
h3cVoPeerDefault2ndCodecLevel = _H3cVoPeerDefault2ndCodecLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 3),
    _H3cVoPeerDefault2ndCodecLevel_Type()
)
h3cVoPeerDefault2ndCodecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefault2ndCodecLevel.setStatus("current")
_H3cVoPeerDefault3rdCodecLevel_Type = CodecType
_H3cVoPeerDefault3rdCodecLevel_Object = MibScalar
h3cVoPeerDefault3rdCodecLevel = _H3cVoPeerDefault3rdCodecLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 4),
    _H3cVoPeerDefault3rdCodecLevel_Type()
)
h3cVoPeerDefault3rdCodecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefault3rdCodecLevel.setStatus("current")
_H3cVoPeerDefault4thCodecLevel_Type = CodecType
_H3cVoPeerDefault4thCodecLevel_Object = MibScalar
h3cVoPeerDefault4thCodecLevel = _H3cVoPeerDefault4thCodecLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 5),
    _H3cVoPeerDefault4thCodecLevel_Type()
)
h3cVoPeerDefault4thCodecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefault4thCodecLevel.setStatus("current")


class _H3cVoPeerDefaultVADOn_Type(Integer32):
    """Custom type h3cVoPeerDefaultVADOn based on Integer32"""
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


_H3cVoPeerDefaultVADOn_Type.__name__ = "Integer32"
_H3cVoPeerDefaultVADOn_Object = MibScalar
h3cVoPeerDefaultVADOn = _H3cVoPeerDefaultVADOn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 6),
    _H3cVoPeerDefaultVADOn_Type()
)
h3cVoPeerDefaultVADOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefaultVADOn.setStatus("current")
_H3cVoPeerDefaultFaxTransLevel_Type = Integer32
_H3cVoPeerDefaultFaxTransLevel_Object = MibScalar
h3cVoPeerDefaultFaxTransLevel = _H3cVoPeerDefaultFaxTransLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 7),
    _H3cVoPeerDefaultFaxTransLevel_Type()
)
h3cVoPeerDefaultFaxTransLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefaultFaxTransLevel.setStatus("current")
_H3cVoPeerDefaultFaxLocalTrain_Type = Integer32
_H3cVoPeerDefaultFaxLocalTrain_Object = MibScalar
h3cVoPeerDefaultFaxLocalTrain = _H3cVoPeerDefaultFaxLocalTrain_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 8),
    _H3cVoPeerDefaultFaxLocalTrain_Type()
)
h3cVoPeerDefaultFaxLocalTrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefaultFaxLocalTrain.setStatus("current")
_H3cVoPeerDefaultFaxProtocol_Type = FaxProtocolType
_H3cVoPeerDefaultFaxProtocol_Object = MibScalar
h3cVoPeerDefaultFaxProtocol = _H3cVoPeerDefaultFaxProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 9),
    _H3cVoPeerDefaultFaxProtocol_Type()
)
h3cVoPeerDefaultFaxProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefaultFaxProtocol.setStatus("current")


class _H3cVoPeerDefaultFaxHSRedunNum_Type(Integer32):
    """Custom type h3cVoPeerDefaultFaxHSRedunNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_H3cVoPeerDefaultFaxHSRedunNum_Type.__name__ = "Integer32"
_H3cVoPeerDefaultFaxHSRedunNum_Object = MibScalar
h3cVoPeerDefaultFaxHSRedunNum = _H3cVoPeerDefaultFaxHSRedunNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 10),
    _H3cVoPeerDefaultFaxHSRedunNum_Type()
)
h3cVoPeerDefaultFaxHSRedunNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefaultFaxHSRedunNum.setStatus("current")


class _H3cVoPeerDefaultFaxLSRedunNum_Type(Integer32):
    """Custom type h3cVoPeerDefaultFaxLSRedunNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_H3cVoPeerDefaultFaxLSRedunNum_Type.__name__ = "Integer32"
_H3cVoPeerDefaultFaxLSRedunNum_Object = MibScalar
h3cVoPeerDefaultFaxLSRedunNum = _H3cVoPeerDefaultFaxLSRedunNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 11),
    _H3cVoPeerDefaultFaxLSRedunNum_Type()
)
h3cVoPeerDefaultFaxLSRedunNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefaultFaxLSRedunNum.setStatus("current")
_H3cVoPeerDefaultFaxBaudrate_Type = FaxBaudrateType
_H3cVoPeerDefaultFaxBaudrate_Object = MibScalar
h3cVoPeerDefaultFaxBaudrate = _H3cVoPeerDefaultFaxBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 12),
    _H3cVoPeerDefaultFaxBaudrate_Type()
)
h3cVoPeerDefaultFaxBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefaultFaxBaudrate.setStatus("current")


class _H3cVoPeerDefaultFaxNSF_Type(Integer32):
    """Custom type h3cVoPeerDefaultFaxNSF based on Integer32"""
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


_H3cVoPeerDefaultFaxNSF_Type.__name__ = "Integer32"
_H3cVoPeerDefaultFaxNSF_Object = MibScalar
h3cVoPeerDefaultFaxNSF = _H3cVoPeerDefaultFaxNSF_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 13),
    _H3cVoPeerDefaultFaxNSF_Type()
)
h3cVoPeerDefaultFaxNSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefaultFaxNSF.setStatus("current")
_H3cVoPeerDefaultFaxSupportMode_Type = FaxSupportModeType
_H3cVoPeerDefaultFaxSupportMode_Object = MibScalar
h3cVoPeerDefaultFaxSupportMode = _H3cVoPeerDefaultFaxSupportMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 14),
    _H3cVoPeerDefaultFaxSupportMode_Type()
)
h3cVoPeerDefaultFaxSupportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefaultFaxSupportMode.setStatus("current")
_H3cVoPeerDefaultFaxTrainMode_Type = FaxTrainMode
_H3cVoPeerDefaultFaxTrainMode_Object = MibScalar
h3cVoPeerDefaultFaxTrainMode = _H3cVoPeerDefaultFaxTrainMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 15),
    _H3cVoPeerDefaultFaxTrainMode_Type()
)
h3cVoPeerDefaultFaxTrainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefaultFaxTrainMode.setStatus("current")


class _H3cVoPeerDefaultFaxECM_Type(Integer32):
    """Custom type h3cVoPeerDefaultFaxECM based on Integer32"""
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


_H3cVoPeerDefaultFaxECM_Type.__name__ = "Integer32"
_H3cVoPeerDefaultFaxECM_Object = MibScalar
h3cVoPeerDefaultFaxECM = _H3cVoPeerDefaultFaxECM_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 4, 16),
    _H3cVoPeerDefaultFaxECM_Type()
)
h3cVoPeerDefaultFaxECM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoPeerDefaultFaxECM.setStatus("current")
_H3cVoPeerCfgCallerPermitTable_Object = MibTable
h3cVoPeerCfgCallerPermitTable = _H3cVoPeerCfgCallerPermitTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 5)
)
if mibBuilder.loadTexts:
    h3cVoPeerCfgCallerPermitTable.setStatus("current")
_H3cVoPeerCfgCallerPermitEntry_Object = MibTableRow
h3cVoPeerCfgCallerPermitEntry = _H3cVoPeerCfgCallerPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 5, 1)
)
h3cVoPeerCfgCallerPermitEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VODIALCONTROL-MIB", "h3cVoPeerCfgIndex"),
    (0, "A3COM-HUAWEI-VODIALCONTROL-MIB", "h3cVoPeerCfgCallerPermitNum"),
)
if mibBuilder.loadTexts:
    h3cVoPeerCfgCallerPermitEntry.setStatus("current")
_H3cVoPeerCfgCallerPermitNum_Type = OctetString
_H3cVoPeerCfgCallerPermitNum_Object = MibTableColumn
h3cVoPeerCfgCallerPermitNum = _H3cVoPeerCfgCallerPermitNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 5, 1, 1),
    _H3cVoPeerCfgCallerPermitNum_Type()
)
h3cVoPeerCfgCallerPermitNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoPeerCfgCallerPermitNum.setStatus("current")
_H3cVoPeerCallerPermitRowStatus_Type = RowStatus
_H3cVoPeerCallerPermitRowStatus_Object = MibTableColumn
h3cVoPeerCallerPermitRowStatus = _H3cVoPeerCallerPermitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 5, 1, 5, 1, 2),
    _H3cVoPeerCallerPermitRowStatus_Type()
)
h3cVoPeerCallerPermitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoPeerCallerPermitRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-VODIALCONTROL-MIB",
    **{"FaxProtocolType": FaxProtocolType,
       "FaxBaudrateType": FaxBaudrateType,
       "FaxSupportModeType": FaxSupportModeType,
       "FaxTrainMode": FaxTrainMode,
       "PhoneNumberType": PhoneNumberType,
       "PhoneNumberPlan": PhoneNumberPlan,
       "h3cVoiceDialControl": h3cVoiceDialControl,
       "h3cVoPeerObjects": h3cVoPeerObjects,
       "h3cVoPeerCommonConfigTable": h3cVoPeerCommonConfigTable,
       "h3cVoPeerCommonConfigEntry": h3cVoPeerCommonConfigEntry,
       "h3cVoPeerCfgIndex": h3cVoPeerCfgIndex,
       "h3cVoPeerCfgRowStatus": h3cVoPeerCfgRowStatus,
       "h3cVoPeerCfgType": h3cVoPeerCfgType,
       "h3cVoPeerCfgDesPattern": h3cVoPeerCfgDesPattern,
       "h3cVoPeerCfgCodec1st": h3cVoPeerCfgCodec1st,
       "h3cVoPeerCfgCodec2nd": h3cVoPeerCfgCodec2nd,
       "h3cVoPeerCfgCodec3rd": h3cVoPeerCfgCodec3rd,
       "h3cVoPeerCfgCodec4th": h3cVoPeerCfgCodec4th,
       "h3cVoPeerCfgDSCP": h3cVoPeerCfgDSCP,
       "h3cVoPeerCfgShutDown": h3cVoPeerCfgShutDown,
       "h3cVoPeerCfgVADEnable": h3cVoPeerCfgVADEnable,
       "h3cVoPeerCfgOutbandMode": h3cVoPeerCfgOutbandMode,
       "h3cVoPeerCfgFaxLevel": h3cVoPeerCfgFaxLevel,
       "h3cVoPeerCfgFaxBaudrate": h3cVoPeerCfgFaxBaudrate,
       "h3cVoPeerCfgFaxLocalTrainPara": h3cVoPeerCfgFaxLocalTrainPara,
       "h3cVoPeerCfgFaxProtocol": h3cVoPeerCfgFaxProtocol,
       "h3cVoPeerCfgT38FaxHRPackNum": h3cVoPeerCfgT38FaxHRPackNum,
       "h3cVoPeerCfgT38FaxLRPackNum": h3cVoPeerCfgT38FaxLRPackNum,
       "h3cVoPeerCfgFaxSendNSFEnable": h3cVoPeerCfgFaxSendNSFEnable,
       "h3cVoPeerCfgFaxSupportMode": h3cVoPeerCfgFaxSupportMode,
       "h3cVoPeerCfgFaxTrainMode": h3cVoPeerCfgFaxTrainMode,
       "h3cVoPeerCfgFaxEcm": h3cVoPeerCfgFaxEcm,
       "h3cVoPeerCfgPriority": h3cVoPeerCfgPriority,
       "h3cVoPeerCfgDescription": h3cVoPeerCfgDescription,
       "h3cVoPeerCfgCallingNumberType": h3cVoPeerCfgCallingNumberType,
       "h3cVoPeerCfgCalledNumberType": h3cVoPeerCfgCalledNumberType,
       "h3cVoPeerCfgCallingNumberPlan": h3cVoPeerCfgCallingNumberPlan,
       "h3cVoPeerCfgCalledNumberPlan": h3cVoPeerCfgCalledNumberPlan,
       "h3cVoPeerCfgSelectStop": h3cVoPeerCfgSelectStop,
       "h3cVoPeerCfgCallingNumSubstRule": h3cVoPeerCfgCallingNumSubstRule,
       "h3cVoPeerCfgCalledNumSubstRule": h3cVoPeerCfgCalledNumSubstRule,
       "h3cVoPeerCfgMaxCall": h3cVoPeerCfgMaxCall,
       "h3cVoPOTSPeerConfigTable": h3cVoPOTSPeerConfigTable,
       "h3cVoPOTSPeerConfigEntry": h3cVoPOTSPeerConfigEntry,
       "h3cVoPOTSPeerConfigIndex": h3cVoPOTSPeerConfigIndex,
       "h3cVoPOTSPeerConfigPrefix": h3cVoPOTSPeerConfigPrefix,
       "h3cVoPOTSPeerConfigSubLine": h3cVoPOTSPeerConfigSubLine,
       "h3cVoPOTSPeerConfigSendNum": h3cVoPOTSPeerConfigSendNum,
       "h3cVoVoIPPeerConfigTable": h3cVoVoIPPeerConfigTable,
       "h3cVoVoIPPeerConfigEntry": h3cVoVoIPPeerConfigEntry,
       "h3cVoVoIPPeerCfgIndex": h3cVoVoIPPeerCfgIndex,
       "h3cVoVoIPPeerCfgTargetType": h3cVoVoIPPeerCfgTargetType,
       "h3cVoVoIPPeerCfgTargetAddrType": h3cVoVoIPPeerCfgTargetAddrType,
       "h3cVoVoIPPeerCfgTargetAddr": h3cVoVoIPPeerCfgTargetAddr,
       "h3cVoVoIPPeerCfgFastStart": h3cVoVoIPPeerCfgFastStart,
       "h3cVoVoIPPeerCfgTunnel": h3cVoVoIPPeerCfgTunnel,
       "h3cVoVoIPPeerCfgAreaID": h3cVoVoIPPeerCfgAreaID,
       "h3cVoVoIPPeerCfgSendRing": h3cVoVoIPPeerCfgSendRing,
       "h3cVoPeerDefaultConfigObjects": h3cVoPeerDefaultConfigObjects,
       "h3cVoPeerDefault1stCodecLevel": h3cVoPeerDefault1stCodecLevel,
       "h3cVoPeerDefault2ndCodecLevel": h3cVoPeerDefault2ndCodecLevel,
       "h3cVoPeerDefault3rdCodecLevel": h3cVoPeerDefault3rdCodecLevel,
       "h3cVoPeerDefault4thCodecLevel": h3cVoPeerDefault4thCodecLevel,
       "h3cVoPeerDefaultVADOn": h3cVoPeerDefaultVADOn,
       "h3cVoPeerDefaultFaxTransLevel": h3cVoPeerDefaultFaxTransLevel,
       "h3cVoPeerDefaultFaxLocalTrain": h3cVoPeerDefaultFaxLocalTrain,
       "h3cVoPeerDefaultFaxProtocol": h3cVoPeerDefaultFaxProtocol,
       "h3cVoPeerDefaultFaxHSRedunNum": h3cVoPeerDefaultFaxHSRedunNum,
       "h3cVoPeerDefaultFaxLSRedunNum": h3cVoPeerDefaultFaxLSRedunNum,
       "h3cVoPeerDefaultFaxBaudrate": h3cVoPeerDefaultFaxBaudrate,
       "h3cVoPeerDefaultFaxNSF": h3cVoPeerDefaultFaxNSF,
       "h3cVoPeerDefaultFaxSupportMode": h3cVoPeerDefaultFaxSupportMode,
       "h3cVoPeerDefaultFaxTrainMode": h3cVoPeerDefaultFaxTrainMode,
       "h3cVoPeerDefaultFaxECM": h3cVoPeerDefaultFaxECM,
       "h3cVoPeerCfgCallerPermitTable": h3cVoPeerCfgCallerPermitTable,
       "h3cVoPeerCfgCallerPermitEntry": h3cVoPeerCfgCallerPermitEntry,
       "h3cVoPeerCfgCallerPermitNum": h3cVoPeerCfgCallerPermitNum,
       "h3cVoPeerCallerPermitRowStatus": h3cVoPeerCallerPermitRowStatus}
)
