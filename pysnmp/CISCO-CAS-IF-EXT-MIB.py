# SNMP MIB module (CISCO-CAS-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CAS-IF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:56 2024
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

(ccasGrpCfgEntry,
 ccasVoiceCfgEntry) = mibBuilder.importSymbols(
    "CISCO-CAS-IF-MIB",
    "ccasGrpCfgEntry",
    "ccasVoiceCfgEntry")

(CCallControlProfileIndexOrZero,
 CVoiceTonePlanIndexOrZero,
 cmgwIndex) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "CCallControlProfileIndexOrZero",
    "CVoiceTonePlanIndexOrZero",
    "cmgwIndex")

(CH248Packages,) = mibBuilder.importSymbols(
    "CISCO-MEGACO-EXT-MIB",
    "CH248Packages")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(BulkConfigResult,
 ConfigIterator) = mibBuilder.importSymbols(
    "CISCO-TC",
    "BulkConfigResult",
    "ConfigIterator")

(CiscoCodecPacketPeriod,) = mibBuilder.importSymbols(
    "CISCO-VOICE-AALX-PROFILE-MIB",
    "CiscoCodecPacketPeriod")

(CvcCoderTypeRate,
 CvcFaxTransmitRate) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcCoderTypeRate",
    "CvcFaxTransmitRate")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ciscoCasIfExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314)
)
ciscoCasIfExtMIB.setRevisions(
        ("2005-11-28 00:00",
         "2004-06-23 00:00",
         "2004-05-26 00:00",
         "2003-04-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CASLineSignal(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class CASRegisterSignal(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compelled", 1),
          ("noncompelled", 2),
          ("semicompelled", 3))
    )



class CASForwardSignal(Integer32, TextualConvention):
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
              46)
        )
    )
    namedValues = NamedValues(
        *(("i1", 2),
          ("i10", 11),
          ("i11", 12),
          ("i12", 13),
          ("i13", 14),
          ("i14", 15),
          ("i15", 16),
          ("i2", 3),
          ("i3", 4),
          ("i4", 5),
          ("i5", 6),
          ("i6", 7),
          ("i7", 8),
          ("i8", 9),
          ("i9", 10),
          ("ii1", 17),
          ("ii10", 26),
          ("ii11", 27),
          ("ii12", 28),
          ("ii13", 29),
          ("ii14", 30),
          ("ii15", 31),
          ("ii2", 18),
          ("ii3", 19),
          ("ii4", 20),
          ("ii5", 21),
          ("ii6", 22),
          ("ii7", 23),
          ("ii8", 24),
          ("ii9", 25),
          ("iiI1", 32),
          ("iiI2", 33),
          ("iii10", 41),
          ("iii11", 42),
          ("iii12", 43),
          ("iii13", 44),
          ("iii14", 45),
          ("iii15", 46),
          ("iii3", 34),
          ("iii4", 35),
          ("iii5", 36),
          ("iii6", 37),
          ("iii7", 38),
          ("iii8", 39),
          ("iii9", 40),
          ("notApplicable", 1))
    )



class CASBackwardSignal(Integer32, TextualConvention):
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
              46)
        )
    )
    namedValues = NamedValues(
        *(("a1", 2),
          ("a10", 11),
          ("a11", 12),
          ("a12", 13),
          ("a13", 14),
          ("a14", 15),
          ("a15", 16),
          ("a2", 3),
          ("a3", 4),
          ("a4", 5),
          ("a5", 6),
          ("a6", 7),
          ("a7", 8),
          ("a8", 9),
          ("a9", 10),
          ("b1", 17),
          ("b10", 26),
          ("b11", 27),
          ("b12", 28),
          ("b13", 29),
          ("b14", 30),
          ("b15", 31),
          ("b2", 18),
          ("b3", 19),
          ("b4", 20),
          ("b5", 21),
          ("b6", 22),
          ("b7", 23),
          ("b8", 24),
          ("b9", 25),
          ("c1", 32),
          ("c10", 41),
          ("c11", 42),
          ("c12", 43),
          ("c13", 44),
          ("c14", 45),
          ("c15", 46),
          ("c2", 33),
          ("c3", 34),
          ("c4", 35),
          ("c5", 36),
          ("c6", 37),
          ("c7", 38),
          ("c8", 39),
          ("c9", 40),
          ("notApplicable", 1))
    )



class CASCountryCode(Integer32, TextualConvention):
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
              38)
        )
    )
    namedValues = NamedValues(
        *(("argentina", 2),
          ("australia", 3),
          ("bemilcom", 38),
          ("bolivia", 4),
          ("brazil", 5),
          ("bulgaria", 6),
          ("china", 7),
          ("colombia", 8),
          ("costaRica", 9),
          ("croatia", 10),
          ("eastEurope", 11),
          ("ecuadorIT", 12),
          ("ecuadorLME", 13),
          ("greece", 14),
          ("guatemala", 15),
          ("hongKong", 16),
          ("india", 17),
          ("indonesia", 18),
          ("israel", 19),
          ("itu", 1),
          ("korea", 20),
          ("laos", 21),
          ("malaysia", 22),
          ("malta", 23),
          ("mongolia", 24),
          ("newZealand", 25),
          ("paraguay", 26),
          ("peru", 27),
          ("philippines", 28),
          ("saudiArabia", 29),
          ("singapore", 30),
          ("southAfrica", 31),
          ("telemex", 32),
          ("telnor", 33),
          ("thailand", 34),
          ("uruguay", 35),
          ("venezuela", 36),
          ("vietnam", 37))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCasIfExtMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoCasIfExtMIBNotifications = _CiscoCasIfExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 0)
)
_CiscoCasIfExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCasIfExtMIBObjects = _CiscoCasIfExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1)
)
_CcasIfExtConfig_ObjectIdentity = ObjectIdentity
ccasIfExtConfig = _CcasIfExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1)
)
_CcasIfExtVoiceCfgTable_Object = MibTable
ccasIfExtVoiceCfgTable = _CcasIfExtVoiceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgTable.setStatus("current")
_CcasIfExtVoiceCfgEntry_Object = MibTableRow
ccasIfExtVoiceCfgEntry = _CcasIfExtVoiceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgEntry.setStatus("current")


class _CcasIfExtVoiceCfgLifNumber_Type(Unsigned32):
    """Custom type ccasIfExtVoiceCfgLifNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcasIfExtVoiceCfgLifNumber_Type.__name__ = "Unsigned32"
_CcasIfExtVoiceCfgLifNumber_Object = MibTableColumn
ccasIfExtVoiceCfgLifNumber = _CcasIfExtVoiceCfgLifNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 1),
    _CcasIfExtVoiceCfgLifNumber_Type()
)
ccasIfExtVoiceCfgLifNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgLifNumber.setStatus("current")


class _CcasIfExtVoiceCfgCcntrlProfile_Type(CCallControlProfileIndexOrZero):
    """Custom type ccasIfExtVoiceCfgCcntrlProfile based on CCallControlProfileIndexOrZero"""
    defaultValue = 0


_CcasIfExtVoiceCfgCcntrlProfile_Object = MibTableColumn
ccasIfExtVoiceCfgCcntrlProfile = _CcasIfExtVoiceCfgCcntrlProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 2),
    _CcasIfExtVoiceCfgCcntrlProfile_Type()
)
ccasIfExtVoiceCfgCcntrlProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgCcntrlProfile.setStatus("current")
_CcasIfExtVoiceCfgVadEnabled_Type = TruthValue
_CcasIfExtVoiceCfgVadEnabled_Object = MibTableColumn
ccasIfExtVoiceCfgVadEnabled = _CcasIfExtVoiceCfgVadEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 3),
    _CcasIfExtVoiceCfgVadEnabled_Type()
)
ccasIfExtVoiceCfgVadEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgVadEnabled.setStatus("current")


class _CcasIfExtVoiceCfgContinuityTone1_Type(Unsigned32):
    """Custom type ccasIfExtVoiceCfgContinuityTone1 based on Unsigned32"""
    defaultValue = 2010

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_CcasIfExtVoiceCfgContinuityTone1_Type.__name__ = "Unsigned32"
_CcasIfExtVoiceCfgContinuityTone1_Object = MibTableColumn
ccasIfExtVoiceCfgContinuityTone1 = _CcasIfExtVoiceCfgContinuityTone1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 4),
    _CcasIfExtVoiceCfgContinuityTone1_Type()
)
ccasIfExtVoiceCfgContinuityTone1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgContinuityTone1.setStatus("current")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgContinuityTone1.setUnits("Hz")


class _CcasIfExtVoiceCfgContinuityTone2_Type(Unsigned32):
    """Custom type ccasIfExtVoiceCfgContinuityTone2 based on Unsigned32"""
    defaultValue = 1780

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_CcasIfExtVoiceCfgContinuityTone2_Type.__name__ = "Unsigned32"
_CcasIfExtVoiceCfgContinuityTone2_Object = MibTableColumn
ccasIfExtVoiceCfgContinuityTone2 = _CcasIfExtVoiceCfgContinuityTone2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 5),
    _CcasIfExtVoiceCfgContinuityTone2_Type()
)
ccasIfExtVoiceCfgContinuityTone2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgContinuityTone2.setStatus("current")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgContinuityTone2.setUnits("Hz")


class _CcasIfExtVoiceCfgModemPassThru_Type(Integer32):
    """Custom type ccasIfExtVoiceCfgModemPassThru based on Integer32"""
    defaultValue = 3

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
        *(("passThruCa", 5),
          ("passThruCisco", 2),
          ("passThruDisabled", 1),
          ("passThruNse", 3),
          ("passThruNseAal2", 4),
          ("passThruNseCa", 8),
          ("passThruTypeE", 6),
          ("system", 7))
    )


_CcasIfExtVoiceCfgModemPassThru_Type.__name__ = "Integer32"
_CcasIfExtVoiceCfgModemPassThru_Object = MibTableColumn
ccasIfExtVoiceCfgModemPassThru = _CcasIfExtVoiceCfgModemPassThru_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 6),
    _CcasIfExtVoiceCfgModemPassThru_Type()
)
ccasIfExtVoiceCfgModemPassThru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgModemPassThru.setStatus("current")
_CcasIfExtVoiceCfgUpspeedCodec_Type = CvcCoderTypeRate
_CcasIfExtVoiceCfgUpspeedCodec_Object = MibTableColumn
ccasIfExtVoiceCfgUpspeedCodec = _CcasIfExtVoiceCfgUpspeedCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 7),
    _CcasIfExtVoiceCfgUpspeedCodec_Type()
)
ccasIfExtVoiceCfgUpspeedCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgUpspeedCodec.setStatus("current")


class _CcasIfExtVoiceCfgT38MaxFaxTxRate_Type(CvcFaxTransmitRate):
    """Custom type ccasIfExtVoiceCfgT38MaxFaxTxRate based on CvcFaxTransmitRate"""


_CcasIfExtVoiceCfgT38MaxFaxTxRate_Object = MibTableColumn
ccasIfExtVoiceCfgT38MaxFaxTxRate = _CcasIfExtVoiceCfgT38MaxFaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 8),
    _CcasIfExtVoiceCfgT38MaxFaxTxRate_Type()
)
ccasIfExtVoiceCfgT38MaxFaxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgT38MaxFaxTxRate.setStatus("deprecated")


class _CcasIfExtVoiceCfgT38HsPktPeriod_Type(CiscoCodecPacketPeriod):
    """Custom type ccasIfExtVoiceCfgT38HsPktPeriod based on CiscoCodecPacketPeriod"""


_CcasIfExtVoiceCfgT38HsPktPeriod_Object = MibTableColumn
ccasIfExtVoiceCfgT38HsPktPeriod = _CcasIfExtVoiceCfgT38HsPktPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 9),
    _CcasIfExtVoiceCfgT38HsPktPeriod_Type()
)
ccasIfExtVoiceCfgT38HsPktPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgT38HsPktPeriod.setStatus("deprecated")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgT38HsPktPeriod.setUnits("microseconds")


class _CcasIfExtVoiceCfgT38HsRedundancy_Type(Unsigned32):
    """Custom type ccasIfExtVoiceCfgT38HsRedundancy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CcasIfExtVoiceCfgT38HsRedundancy_Type.__name__ = "Unsigned32"
_CcasIfExtVoiceCfgT38HsRedundancy_Object = MibTableColumn
ccasIfExtVoiceCfgT38HsRedundancy = _CcasIfExtVoiceCfgT38HsRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 10),
    _CcasIfExtVoiceCfgT38HsRedundancy_Type()
)
ccasIfExtVoiceCfgT38HsRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgT38HsRedundancy.setStatus("deprecated")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgT38HsRedundancy.setUnits("FAX packets")


class _CcasIfExtVoiceCfgRepetition_Type(ConfigIterator):
    """Custom type ccasIfExtVoiceCfgRepetition based on ConfigIterator"""
    defaultValue = 1


_CcasIfExtVoiceCfgRepetition_Object = MibTableColumn
ccasIfExtVoiceCfgRepetition = _CcasIfExtVoiceCfgRepetition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 11),
    _CcasIfExtVoiceCfgRepetition_Type()
)
ccasIfExtVoiceCfgRepetition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgRepetition.setStatus("current")
_CcasIfExtVoiceCfgBulkCfgOwner_Type = OwnerString
_CcasIfExtVoiceCfgBulkCfgOwner_Object = MibTableColumn
ccasIfExtVoiceCfgBulkCfgOwner = _CcasIfExtVoiceCfgBulkCfgOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 12),
    _CcasIfExtVoiceCfgBulkCfgOwner_Type()
)
ccasIfExtVoiceCfgBulkCfgOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgBulkCfgOwner.setStatus("current")
_CcasIfExtVoiceCfgBulkCfgResult_Type = BulkConfigResult
_CcasIfExtVoiceCfgBulkCfgResult_Object = MibTableColumn
ccasIfExtVoiceCfgBulkCfgResult = _CcasIfExtVoiceCfgBulkCfgResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 13),
    _CcasIfExtVoiceCfgBulkCfgResult_Type()
)
ccasIfExtVoiceCfgBulkCfgResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgBulkCfgResult.setStatus("current")


class _CcasIfExtVoiceCfgVadTimer_Type(Integer32):
    """Custom type ccasIfExtVoiceCfgVadTimer based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 65535),
    )


_CcasIfExtVoiceCfgVadTimer_Type.__name__ = "Integer32"
_CcasIfExtVoiceCfgVadTimer_Object = MibTableColumn
ccasIfExtVoiceCfgVadTimer = _CcasIfExtVoiceCfgVadTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 14),
    _CcasIfExtVoiceCfgVadTimer_Type()
)
ccasIfExtVoiceCfgVadTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgVadTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgVadTimer.setUnits("milliseconds")


class _CcasIfExtVoiceCfgICSEnable_Type(TruthValue):
    """Custom type ccasIfExtVoiceCfgICSEnable based on TruthValue"""


_CcasIfExtVoiceCfgICSEnable_Object = MibTableColumn
ccasIfExtVoiceCfgICSEnable = _CcasIfExtVoiceCfgICSEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 15),
    _CcasIfExtVoiceCfgICSEnable_Type()
)
ccasIfExtVoiceCfgICSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgICSEnable.setStatus("current")


class _CcasIfExtVoiceCfgICSIntTimer_Type(Integer32):
    """Custom type ccasIfExtVoiceCfgICSIntTimer based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasIfExtVoiceCfgICSIntTimer_Type.__name__ = "Integer32"
_CcasIfExtVoiceCfgICSIntTimer_Object = MibTableColumn
ccasIfExtVoiceCfgICSIntTimer = _CcasIfExtVoiceCfgICSIntTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 16),
    _CcasIfExtVoiceCfgICSIntTimer_Type()
)
ccasIfExtVoiceCfgICSIntTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgICSIntTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgICSIntTimer.setUnits("milliseconds")
_CcasIfExtVoiceCfgTonePlan_Type = CVoiceTonePlanIndexOrZero
_CcasIfExtVoiceCfgTonePlan_Object = MibTableColumn
ccasIfExtVoiceCfgTonePlan = _CcasIfExtVoiceCfgTonePlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 17),
    _CcasIfExtVoiceCfgTonePlan_Type()
)
ccasIfExtVoiceCfgTonePlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgTonePlan.setStatus("current")


class _CcasIfExtVoiceCfgGwyLinkId_Type(Integer32):
    """Custom type ccasIfExtVoiceCfgGwyLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcasIfExtVoiceCfgGwyLinkId_Type.__name__ = "Integer32"
_CcasIfExtVoiceCfgGwyLinkId_Object = MibTableColumn
ccasIfExtVoiceCfgGwyLinkId = _CcasIfExtVoiceCfgGwyLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 18),
    _CcasIfExtVoiceCfgGwyLinkId_Type()
)
ccasIfExtVoiceCfgGwyLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgGwyLinkId.setStatus("current")
_CcasIfExtVoiceCfgH248PkgIds_Type = CH248Packages
_CcasIfExtVoiceCfgH248PkgIds_Object = MibTableColumn
ccasIfExtVoiceCfgH248PkgIds = _CcasIfExtVoiceCfgH248PkgIds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 19),
    _CcasIfExtVoiceCfgH248PkgIds_Type()
)
ccasIfExtVoiceCfgH248PkgIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgH248PkgIds.setStatus("current")


class _CcasIfExtVoiceCfgEventMappingIdx_Type(Unsigned32):
    """Custom type ccasIfExtVoiceCfgEventMappingIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasIfExtVoiceCfgEventMappingIdx_Type.__name__ = "Unsigned32"
_CcasIfExtVoiceCfgEventMappingIdx_Object = MibTableColumn
ccasIfExtVoiceCfgEventMappingIdx = _CcasIfExtVoiceCfgEventMappingIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 20),
    _CcasIfExtVoiceCfgEventMappingIdx_Type()
)
ccasIfExtVoiceCfgEventMappingIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgEventMappingIdx.setStatus("current")


class _CcasIfExtVoiceCfgGatewayIndex_Type(Unsigned32):
    """Custom type ccasIfExtVoiceCfgGatewayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcasIfExtVoiceCfgGatewayIndex_Type.__name__ = "Unsigned32"
_CcasIfExtVoiceCfgGatewayIndex_Object = MibTableColumn
ccasIfExtVoiceCfgGatewayIndex = _CcasIfExtVoiceCfgGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 21),
    _CcasIfExtVoiceCfgGatewayIndex_Type()
)
ccasIfExtVoiceCfgGatewayIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgGatewayIndex.setStatus("current")


class _CcasIfExtVoiceCfgCasProfile_Type(Unsigned32):
    """Custom type ccasIfExtVoiceCfgCasProfile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasIfExtVoiceCfgCasProfile_Type.__name__ = "Unsigned32"
_CcasIfExtVoiceCfgCasProfile_Object = MibTableColumn
ccasIfExtVoiceCfgCasProfile = _CcasIfExtVoiceCfgCasProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 22),
    _CcasIfExtVoiceCfgCasProfile_Type()
)
ccasIfExtVoiceCfgCasProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgCasProfile.setStatus("current")


class _CcasIfExtVoiceCfgCasVariant_Type(Unsigned32):
    """Custom type ccasIfExtVoiceCfgCasVariant based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasIfExtVoiceCfgCasVariant_Type.__name__ = "Unsigned32"
_CcasIfExtVoiceCfgCasVariant_Object = MibTableColumn
ccasIfExtVoiceCfgCasVariant = _CcasIfExtVoiceCfgCasVariant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 23),
    _CcasIfExtVoiceCfgCasVariant_Type()
)
ccasIfExtVoiceCfgCasVariant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgCasVariant.setStatus("current")


class _CcasIfExtVoiceCfgDs0ChannelsFail_Type(OctetString):
    """Custom type ccasIfExtVoiceCfgDs0ChannelsFail based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CcasIfExtVoiceCfgDs0ChannelsFail_Type.__name__ = "OctetString"
_CcasIfExtVoiceCfgDs0ChannelsFail_Object = MibTableColumn
ccasIfExtVoiceCfgDs0ChannelsFail = _CcasIfExtVoiceCfgDs0ChannelsFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 24),
    _CcasIfExtVoiceCfgDs0ChannelsFail_Type()
)
ccasIfExtVoiceCfgDs0ChannelsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgDs0ChannelsFail.setStatus("current")


class _CcasIfExtVoiceCfgNoiseRegType_Type(Integer32):
    """Custom type ccasIfExtVoiceCfgNoiseRegType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g711A2", 3),
          ("none", 1),
          ("simple", 2))
    )


_CcasIfExtVoiceCfgNoiseRegType_Type.__name__ = "Integer32"
_CcasIfExtVoiceCfgNoiseRegType_Object = MibTableColumn
ccasIfExtVoiceCfgNoiseRegType = _CcasIfExtVoiceCfgNoiseRegType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 1, 1, 25),
    _CcasIfExtVoiceCfgNoiseRegType_Type()
)
ccasIfExtVoiceCfgNoiseRegType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgNoiseRegType.setStatus("current")
_CcasIfExtDs0GrpCfgTable_Object = MibTable
ccasIfExtDs0GrpCfgTable = _CcasIfExtDs0GrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ccasIfExtDs0GrpCfgTable.setStatus("current")
_CcasIfExtDs0GrpCfgEntry_Object = MibTableRow
ccasIfExtDs0GrpCfgEntry = _CcasIfExtDs0GrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccasIfExtDs0GrpCfgEntry.setStatus("current")


class _CcasIfExtDs0GrpRepetition_Type(ConfigIterator):
    """Custom type ccasIfExtDs0GrpRepetition based on ConfigIterator"""
    defaultValue = 1


_CcasIfExtDs0GrpRepetition_Object = MibTableColumn
ccasIfExtDs0GrpRepetition = _CcasIfExtDs0GrpRepetition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 3, 1, 1),
    _CcasIfExtDs0GrpRepetition_Type()
)
ccasIfExtDs0GrpRepetition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtDs0GrpRepetition.setStatus("current")
_CcasIfExtDs0GrpRepeatOwner_Type = OwnerString
_CcasIfExtDs0GrpRepeatOwner_Object = MibTableColumn
ccasIfExtDs0GrpRepeatOwner = _CcasIfExtDs0GrpRepeatOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 3, 1, 2),
    _CcasIfExtDs0GrpRepeatOwner_Type()
)
ccasIfExtDs0GrpRepeatOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasIfExtDs0GrpRepeatOwner.setStatus("current")
_CcasIfExtDs0GrpRepeatResult_Type = BulkConfigResult
_CcasIfExtDs0GrpRepeatResult_Object = MibTableColumn
ccasIfExtDs0GrpRepeatResult = _CcasIfExtDs0GrpRepeatResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 1, 3, 1, 3),
    _CcasIfExtDs0GrpRepeatResult_Type()
)
ccasIfExtDs0GrpRepeatResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasIfExtDs0GrpRepeatResult.setStatus("current")
_CcasIfExtProfile_ObjectIdentity = ObjectIdentity
ccasIfExtProfile = _CcasIfExtProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2)
)
_CcasIfExtProfileTable_Object = MibTable
ccasIfExtProfileTable = _CcasIfExtProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccasIfExtProfileTable.setStatus("current")
_CcasIfExtProfileEntry_Object = MibTableRow
ccasIfExtProfileEntry = _CcasIfExtProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 1, 1)
)
ccasIfExtProfileEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-CAS-IF-EXT-MIB", "ccasProfileIndex"),
)
if mibBuilder.loadTexts:
    ccasIfExtProfileEntry.setStatus("current")


class _CcasProfileIndex_Type(Unsigned32):
    """Custom type ccasProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasProfileIndex_Type.__name__ = "Unsigned32"
_CcasProfileIndex_Object = MibTableColumn
ccasProfileIndex = _CcasProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 1, 1, 1),
    _CcasProfileIndex_Type()
)
ccasProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccasProfileIndex.setStatus("current")


class _CcasProfileLineSigTimer_Type(Unsigned32):
    """Custom type ccasProfileLineSigTimer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasProfileLineSigTimer_Type.__name__ = "Unsigned32"
_CcasProfileLineSigTimer_Object = MibTableColumn
ccasProfileLineSigTimer = _CcasProfileLineSigTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 1, 1, 2),
    _CcasProfileLineSigTimer_Type()
)
ccasProfileLineSigTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasProfileLineSigTimer.setStatus("current")


class _CcasProfileRegisterSignal_Type(Unsigned32):
    """Custom type ccasProfileRegisterSignal based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasProfileRegisterSignal_Type.__name__ = "Unsigned32"
_CcasProfileRegisterSignal_Object = MibTableColumn
ccasProfileRegisterSignal = _CcasProfileRegisterSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 1, 1, 3),
    _CcasProfileRegisterSignal_Type()
)
ccasProfileRegisterSignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasProfileRegisterSignal.setStatus("current")


class _CcasProfileRegSigTimer_Type(Unsigned32):
    """Custom type ccasProfileRegSigTimer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasProfileRegSigTimer_Type.__name__ = "Unsigned32"
_CcasProfileRegSigTimer_Object = MibTableColumn
ccasProfileRegSigTimer = _CcasProfileRegSigTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 1, 1, 4),
    _CcasProfileRegSigTimer_Type()
)
ccasProfileRegSigTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasProfileRegSigTimer.setStatus("current")


class _CcasProfileGeneralCfg_Type(Unsigned32):
    """Custom type ccasProfileGeneralCfg based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasProfileGeneralCfg_Type.__name__ = "Unsigned32"
_CcasProfileGeneralCfg_Object = MibTableColumn
ccasProfileGeneralCfg = _CcasProfileGeneralCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 1, 1, 5),
    _CcasProfileGeneralCfg_Type()
)
ccasProfileGeneralCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasProfileGeneralCfg.setStatus("current")
_CcasProfileRowStatus_Type = RowStatus
_CcasProfileRowStatus_Object = MibTableColumn
ccasProfileRowStatus = _CcasProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 1, 1, 6),
    _CcasProfileRowStatus_Type()
)
ccasProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasProfileRowStatus.setStatus("current")
_CcasIfExtVariantTable_Object = MibTable
ccasIfExtVariantTable = _CcasIfExtVariantTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccasIfExtVariantTable.setStatus("current")
_CcasIfExtVariantEntry_Object = MibTableRow
ccasIfExtVariantEntry = _CcasIfExtVariantEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 2, 1)
)
ccasIfExtVariantEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-CAS-IF-EXT-MIB", "ccasVariantIndex"),
)
if mibBuilder.loadTexts:
    ccasIfExtVariantEntry.setStatus("current")


class _CcasVariantIndex_Type(Unsigned32):
    """Custom type ccasVariantIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasVariantIndex_Type.__name__ = "Unsigned32"
_CcasVariantIndex_Object = MibTableColumn
ccasVariantIndex = _CcasVariantIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 2, 1, 1),
    _CcasVariantIndex_Type()
)
ccasVariantIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccasVariantIndex.setStatus("current")


class _CcasVariantFile_Type(SnmpAdminString):
    """Custom type ccasVariantFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcasVariantFile_Type.__name__ = "SnmpAdminString"
_CcasVariantFile_Object = MibTableColumn
ccasVariantFile = _CcasVariantFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 2, 1, 2),
    _CcasVariantFile_Type()
)
ccasVariantFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasVariantFile.setStatus("current")


class _CcasVariantSource_Type(Integer32):
    """Custom type ccasVariantSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_CcasVariantSource_Type.__name__ = "Integer32"
_CcasVariantSource_Object = MibTableColumn
ccasVariantSource = _CcasVariantSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 2, 1, 3),
    _CcasVariantSource_Type()
)
ccasVariantSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasVariantSource.setStatus("current")
_CcasVariantNumberCount_Type = Gauge32
_CcasVariantNumberCount_Object = MibTableColumn
ccasVariantNumberCount = _CcasVariantNumberCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 2, 1, 4),
    _CcasVariantNumberCount_Type()
)
ccasVariantNumberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasVariantNumberCount.setStatus("current")


class _CcasVariantState_Type(Integer32):
    """Custom type ccasVariantState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initFailed", 3),
          ("initInProgress", 1),
          ("initSuccessfully", 2))
    )


_CcasVariantState_Type.__name__ = "Integer32"
_CcasVariantState_Object = MibTableColumn
ccasVariantState = _CcasVariantState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 2, 1, 5),
    _CcasVariantState_Type()
)
ccasVariantState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasVariantState.setStatus("current")
_CcasVariantRowStatus_Type = RowStatus
_CcasVariantRowStatus_Object = MibTableColumn
ccasVariantRowStatus = _CcasVariantRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 2, 2, 1, 6),
    _CcasVariantRowStatus_Type()
)
ccasVariantRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasVariantRowStatus.setStatus("current")
_CcasIfExtConfigLineSignal_ObjectIdentity = ObjectIdentity
ccasIfExtConfigLineSignal = _CcasIfExtConfigLineSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3)
)
_CcasIfExtIncomingLineSignalTable_Object = MibTable
ccasIfExtIncomingLineSignalTable = _CcasIfExtIncomingLineSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccasIfExtIncomingLineSignalTable.setStatus("current")
_CcasIfExtIncomingLineSignalEntry_Object = MibTableRow
ccasIfExtIncomingLineSignalEntry = _CcasIfExtIncomingLineSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 1, 1)
)
ccasIfExtIncomingLineSignalEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-CAS-IF-EXT-MIB", "ccasVariantIndex"),
    (0, "CISCO-CAS-IF-EXT-MIB", "ccasILSSignalNameIndex"),
)
if mibBuilder.loadTexts:
    ccasIfExtIncomingLineSignalEntry.setStatus("current")


class _CcasILSSignalNameIndex_Type(Unsigned32):
    """Custom type ccasILSSignalNameIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasILSSignalNameIndex_Type.__name__ = "Unsigned32"
_CcasILSSignalNameIndex_Object = MibTableColumn
ccasILSSignalNameIndex = _CcasILSSignalNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 1, 1, 2),
    _CcasILSSignalNameIndex_Type()
)
ccasILSSignalNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccasILSSignalNameIndex.setStatus("current")


class _CcasILSSignalName_Type(SnmpAdminString):
    """Custom type ccasILSSignalName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcasILSSignalName_Type.__name__ = "SnmpAdminString"
_CcasILSSignalName_Object = MibTableColumn
ccasILSSignalName = _CcasILSSignalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 1, 1, 3),
    _CcasILSSignalName_Type()
)
ccasILSSignalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasILSSignalName.setStatus("current")
_CcasILSRxPattern_Type = CASLineSignal
_CcasILSRxPattern_Object = MibTableColumn
ccasILSRxPattern = _CcasILSRxPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 1, 1, 4),
    _CcasILSRxPattern_Type()
)
ccasILSRxPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasILSRxPattern.setStatus("current")
_CcasILSMatchedRxPattern_Type = CASLineSignal
_CcasILSMatchedRxPattern_Object = MibTableColumn
ccasILSMatchedRxPattern = _CcasILSMatchedRxPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 1, 1, 5),
    _CcasILSMatchedRxPattern_Type()
)
ccasILSMatchedRxPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasILSMatchedRxPattern.setStatus("current")
_CcasILSMatchedTxPattern_Type = CASLineSignal
_CcasILSMatchedTxPattern_Object = MibTableColumn
ccasILSMatchedTxPattern = _CcasILSMatchedTxPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 1, 1, 6),
    _CcasILSMatchedTxPattern_Type()
)
ccasILSMatchedTxPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasILSMatchedTxPattern.setStatus("current")


class _CcasILSMinMakeTime_Type(Unsigned32):
    """Custom type ccasILSMinMakeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4294967295),
    )


_CcasILSMinMakeTime_Type.__name__ = "Unsigned32"
_CcasILSMinMakeTime_Object = MibTableColumn
ccasILSMinMakeTime = _CcasILSMinMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 1, 1, 7),
    _CcasILSMinMakeTime_Type()
)
ccasILSMinMakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasILSMinMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    ccasILSMinMakeTime.setUnits("milliseconds")


class _CcasILSMaxMakeTime_Type(Unsigned32):
    """Custom type ccasILSMaxMakeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasILSMaxMakeTime_Type.__name__ = "Unsigned32"
_CcasILSMaxMakeTime_Object = MibTableColumn
ccasILSMaxMakeTime = _CcasILSMaxMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 1, 1, 8),
    _CcasILSMaxMakeTime_Type()
)
ccasILSMaxMakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasILSMaxMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    ccasILSMaxMakeTime.setUnits("milliseconds")


class _CcasILSMinBreakTime_Type(Unsigned32):
    """Custom type ccasILSMinBreakTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasILSMinBreakTime_Type.__name__ = "Unsigned32"
_CcasILSMinBreakTime_Object = MibTableColumn
ccasILSMinBreakTime = _CcasILSMinBreakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 1, 1, 9),
    _CcasILSMinBreakTime_Type()
)
ccasILSMinBreakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasILSMinBreakTime.setStatus("current")
if mibBuilder.loadTexts:
    ccasILSMinBreakTime.setUnits("milliseconds")


class _CcasILSMaxBreakTime_Type(Unsigned32):
    """Custom type ccasILSMaxBreakTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasILSMaxBreakTime_Type.__name__ = "Unsigned32"
_CcasILSMaxBreakTime_Object = MibTableColumn
ccasILSMaxBreakTime = _CcasILSMaxBreakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 1, 1, 10),
    _CcasILSMaxBreakTime_Type()
)
ccasILSMaxBreakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasILSMaxBreakTime.setStatus("current")
if mibBuilder.loadTexts:
    ccasILSMaxBreakTime.setUnits("milliseconds")
_CcasIfExtOutgoingLineSignalTable_Object = MibTable
ccasIfExtOutgoingLineSignalTable = _CcasIfExtOutgoingLineSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ccasIfExtOutgoingLineSignalTable.setStatus("current")
_CcasIfExtOutgoingLineSignalEntry_Object = MibTableRow
ccasIfExtOutgoingLineSignalEntry = _CcasIfExtOutgoingLineSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 2, 1)
)
ccasIfExtOutgoingLineSignalEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-CAS-IF-EXT-MIB", "ccasVariantIndex"),
    (0, "CISCO-CAS-IF-EXT-MIB", "ccasOLSSignalNameIndex"),
)
if mibBuilder.loadTexts:
    ccasIfExtOutgoingLineSignalEntry.setStatus("current")


class _CcasOLSSignalNameIndex_Type(Unsigned32):
    """Custom type ccasOLSSignalNameIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasOLSSignalNameIndex_Type.__name__ = "Unsigned32"
_CcasOLSSignalNameIndex_Object = MibTableColumn
ccasOLSSignalNameIndex = _CcasOLSSignalNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 2, 1, 1),
    _CcasOLSSignalNameIndex_Type()
)
ccasOLSSignalNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccasOLSSignalNameIndex.setStatus("current")


class _CcasOLSCasSignalName_Type(SnmpAdminString):
    """Custom type ccasOLSCasSignalName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcasOLSCasSignalName_Type.__name__ = "SnmpAdminString"
_CcasOLSCasSignalName_Object = MibTableColumn
ccasOLSCasSignalName = _CcasOLSCasSignalName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 2, 1, 2),
    _CcasOLSCasSignalName_Type()
)
ccasOLSCasSignalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasOLSCasSignalName.setStatus("current")
_CcasOLSTxPattern_Type = CASLineSignal
_CcasOLSTxPattern_Object = MibTableColumn
ccasOLSTxPattern = _CcasOLSTxPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 2, 1, 3),
    _CcasOLSTxPattern_Type()
)
ccasOLSTxPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccasOLSTxPattern.setStatus("current")


class _CcasOLSMakeTime_Type(Unsigned32):
    """Custom type ccasOLSMakeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasOLSMakeTime_Type.__name__ = "Unsigned32"
_CcasOLSMakeTime_Object = MibTableColumn
ccasOLSMakeTime = _CcasOLSMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 2, 1, 4),
    _CcasOLSMakeTime_Type()
)
ccasOLSMakeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasOLSMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    ccasOLSMakeTime.setUnits("milliseconds")


class _CcasOLSBreakTime_Type(Unsigned32):
    """Custom type ccasOLSBreakTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasOLSBreakTime_Type.__name__ = "Unsigned32"
_CcasOLSBreakTime_Object = MibTableColumn
ccasOLSBreakTime = _CcasOLSBreakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 2, 1, 5),
    _CcasOLSBreakTime_Type()
)
ccasOLSBreakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccasOLSBreakTime.setStatus("current")
if mibBuilder.loadTexts:
    ccasOLSBreakTime.setUnits("milliseconds")
_CcasIfExtLineSignalTimerTable_Object = MibTable
ccasIfExtLineSignalTimerTable = _CcasIfExtLineSignalTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ccasIfExtLineSignalTimerTable.setStatus("current")
_CcasIfExtLineSignalTimerEntry_Object = MibTableRow
ccasIfExtLineSignalTimerEntry = _CcasIfExtLineSignalTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1)
)
ccasIfExtLineSignalTimerEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-CAS-IF-EXT-MIB", "ccasLSTIndex"),
)
if mibBuilder.loadTexts:
    ccasIfExtLineSignalTimerEntry.setStatus("current")


class _CcasLSTIndex_Type(Unsigned32):
    """Custom type ccasLSTIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasLSTIndex_Type.__name__ = "Unsigned32"
_CcasLSTIndex_Object = MibTableColumn
ccasLSTIndex = _CcasLSTIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 1),
    _CcasLSTIndex_Type()
)
ccasLSTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccasLSTIndex.setStatus("current")


class _CcasLSTIdleGuardTimer_Type(Unsigned32):
    """Custom type ccasLSTIdleGuardTimer based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasLSTIdleGuardTimer_Type.__name__ = "Unsigned32"
_CcasLSTIdleGuardTimer_Object = MibTableColumn
ccasLSTIdleGuardTimer = _CcasLSTIdleGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 2),
    _CcasLSTIdleGuardTimer_Type()
)
ccasLSTIdleGuardTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasLSTIdleGuardTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasLSTIdleGuardTimer.setUnits("milliseconds")


class _CcasLSTClearFwdTimer_Type(Unsigned32):
    """Custom type ccasLSTClearFwdTimer based on Unsigned32"""
    defaultValue = 120000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasLSTClearFwdTimer_Type.__name__ = "Unsigned32"
_CcasLSTClearFwdTimer_Object = MibTableColumn
ccasLSTClearFwdTimer = _CcasLSTClearFwdTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 3),
    _CcasLSTClearFwdTimer_Type()
)
ccasLSTClearFwdTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasLSTClearFwdTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasLSTClearFwdTimer.setUnits("milliseconds")


class _CcasLSTClearBwdTimer_Type(Unsigned32):
    """Custom type ccasLSTClearBwdTimer based on Unsigned32"""
    defaultValue = 120000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasLSTClearBwdTimer_Type.__name__ = "Unsigned32"
_CcasLSTClearBwdTimer_Object = MibTableColumn
ccasLSTClearBwdTimer = _CcasLSTClearBwdTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 4),
    _CcasLSTClearBwdTimer_Type()
)
ccasLSTClearBwdTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasLSTClearBwdTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasLSTClearBwdTimer.setUnits("milliseconds")


class _CcasLSTReleaseGuardTimer_Type(Unsigned32):
    """Custom type ccasLSTReleaseGuardTimer based on Unsigned32"""
    defaultValue = 800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasLSTReleaseGuardTimer_Type.__name__ = "Unsigned32"
_CcasLSTReleaseGuardTimer_Object = MibTableColumn
ccasLSTReleaseGuardTimer = _CcasLSTReleaseGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 5),
    _CcasLSTReleaseGuardTimer_Type()
)
ccasLSTReleaseGuardTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasLSTReleaseGuardTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasLSTReleaseGuardTimer.setUnits("millliseconds")


class _CcasLSTCASGlareTimer_Type(Unsigned32):
    """Custom type ccasLSTCASGlareTimer based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasLSTCASGlareTimer_Type.__name__ = "Unsigned32"
_CcasLSTCASGlareTimer_Object = MibTableColumn
ccasLSTCASGlareTimer = _CcasLSTCASGlareTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 6),
    _CcasLSTCASGlareTimer_Type()
)
ccasLSTCASGlareTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasLSTCASGlareTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasLSTCASGlareTimer.setUnits("milliseconds")


class _CcasLSTAnswerMeterDelayTimer_Type(Unsigned32):
    """Custom type ccasLSTAnswerMeterDelayTimer based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasLSTAnswerMeterDelayTimer_Type.__name__ = "Unsigned32"
_CcasLSTAnswerMeterDelayTimer_Object = MibTableColumn
ccasLSTAnswerMeterDelayTimer = _CcasLSTAnswerMeterDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 7),
    _CcasLSTAnswerMeterDelayTimer_Type()
)
ccasLSTAnswerMeterDelayTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasLSTAnswerMeterDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasLSTAnswerMeterDelayTimer.setUnits("milliseconds")


class _CcasLSTCASDebounceTimer_Type(Unsigned32):
    """Custom type ccasLSTCASDebounceTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CcasLSTCASDebounceTimer_Type.__name__ = "Unsigned32"
_CcasLSTCASDebounceTimer_Object = MibTableColumn
ccasLSTCASDebounceTimer = _CcasLSTCASDebounceTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 8),
    _CcasLSTCASDebounceTimer_Type()
)
ccasLSTCASDebounceTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasLSTCASDebounceTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasLSTCASDebounceTimer.setUnits("milliseconds")


class _CcasLSTSeizeAckRspTimer_Type(Unsigned32):
    """Custom type ccasLSTSeizeAckRspTimer based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcasLSTSeizeAckRspTimer_Type.__name__ = "Unsigned32"
_CcasLSTSeizeAckRspTimer_Object = MibTableColumn
ccasLSTSeizeAckRspTimer = _CcasLSTSeizeAckRspTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 9),
    _CcasLSTSeizeAckRspTimer_Type()
)
ccasLSTSeizeAckRspTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasLSTSeizeAckRspTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasLSTSeizeAckRspTimer.setUnits("milliseconds")


class _CcasLSTDelayBetRegAnsAndLineAns_Type(Unsigned32):
    """Custom type ccasLSTDelayBetRegAnsAndLineAns based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasLSTDelayBetRegAnsAndLineAns_Type.__name__ = "Unsigned32"
_CcasLSTDelayBetRegAnsAndLineAns_Object = MibTableColumn
ccasLSTDelayBetRegAnsAndLineAns = _CcasLSTDelayBetRegAnsAndLineAns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 10),
    _CcasLSTDelayBetRegAnsAndLineAns_Type()
)
ccasLSTDelayBetRegAnsAndLineAns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasLSTDelayBetRegAnsAndLineAns.setStatus("current")
if mibBuilder.loadTexts:
    ccasLSTDelayBetRegAnsAndLineAns.setUnits("seconds")


class _CcasLSTSeizeAckToDigitTimer_Type(Unsigned32):
    """Custom type ccasLSTSeizeAckToDigitTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasLSTSeizeAckToDigitTimer_Type.__name__ = "Unsigned32"
_CcasLSTSeizeAckToDigitTimer_Object = MibTableColumn
ccasLSTSeizeAckToDigitTimer = _CcasLSTSeizeAckToDigitTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 11),
    _CcasLSTSeizeAckToDigitTimer_Type()
)
ccasLSTSeizeAckToDigitTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasLSTSeizeAckToDigitTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasLSTSeizeAckToDigitTimer.setUnits("seconds")
_CcasLSTRowStatus_Type = RowStatus
_CcasLSTRowStatus_Object = MibTableColumn
ccasLSTRowStatus = _CcasLSTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 3, 3, 1, 12),
    _CcasLSTRowStatus_Type()
)
ccasLSTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasLSTRowStatus.setStatus("current")
_CcasIfExtConfigRegisterSignal_ObjectIdentity = ObjectIdentity
ccasIfExtConfigRegisterSignal = _CcasIfExtConfigRegisterSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4)
)
_CcasIfExtRegisterSignalTable_Object = MibTable
ccasIfExtRegisterSignalTable = _CcasIfExtRegisterSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ccasIfExtRegisterSignalTable.setStatus("current")
_CcasIfExtRegisterSignalEntry_Object = MibTableRow
ccasIfExtRegisterSignalEntry = _CcasIfExtRegisterSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1)
)
ccasIfExtRegisterSignalEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-CAS-IF-EXT-MIB", "ccasRSIndex"),
)
if mibBuilder.loadTexts:
    ccasIfExtRegisterSignalEntry.setStatus("current")


class _CcasRSIndex_Type(Unsigned32):
    """Custom type ccasRSIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasRSIndex_Type.__name__ = "Unsigned32"
_CcasRSIndex_Object = MibTableColumn
ccasRSIndex = _CcasRSIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 1),
    _CcasRSIndex_Type()
)
ccasRSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccasRSIndex.setStatus("current")
_CcasRSCountry_Type = CASCountryCode
_CcasRSCountry_Object = MibTableColumn
ccasRSCountry = _CcasRSCountry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 2),
    _CcasRSCountry_Type()
)
ccasRSCountry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSCountry.setStatus("current")


class _CcasRSSubRegion_Type(SnmpAdminString):
    """Custom type ccasRSSubRegion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcasRSSubRegion_Type.__name__ = "SnmpAdminString"
_CcasRSSubRegion_Object = MibTableColumn
ccasRSSubRegion = _CcasRSSubRegion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 3),
    _CcasRSSubRegion_Type()
)
ccasRSSubRegion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSSubRegion.setStatus("current")
_CcasBwdRSNextDigitANI_Type = CASBackwardSignal
_CcasBwdRSNextDigitANI_Object = MibTableColumn
ccasBwdRSNextDigitANI = _CcasBwdRSNextDigitANI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 4),
    _CcasBwdRSNextDigitANI_Type()
)
ccasBwdRSNextDigitANI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSNextDigitANI.setStatus("current")
_CcasBwdRSNextDigitDNIS_Type = CASBackwardSignal
_CcasBwdRSNextDigitDNIS_Object = MibTableColumn
ccasBwdRSNextDigitDNIS = _CcasBwdRSNextDigitDNIS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 5),
    _CcasBwdRSNextDigitDNIS_Type()
)
ccasBwdRSNextDigitDNIS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSNextDigitDNIS.setStatus("current")
_CcasBwdRSPrevDigit_Type = CASBackwardSignal
_CcasBwdRSPrevDigit_Object = MibTableColumn
ccasBwdRSPrevDigit = _CcasBwdRSPrevDigit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 6),
    _CcasBwdRSPrevDigit_Type()
)
ccasBwdRSPrevDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSPrevDigit.setStatus("current")
_CcasBwdRSXtoGroupBSignals_Type = CASBackwardSignal
_CcasBwdRSXtoGroupBSignals_Object = MibTableColumn
ccasBwdRSXtoGroupBSignals = _CcasBwdRSXtoGroupBSignals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 7),
    _CcasBwdRSXtoGroupBSignals_Type()
)
ccasBwdRSXtoGroupBSignals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSXtoGroupBSignals.setStatus("current")
_CcasBwdRSCongestion_Type = CASBackwardSignal
_CcasBwdRSCongestion_Object = MibTableColumn
ccasBwdRSCongestion = _CcasBwdRSCongestion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 8),
    _CcasBwdRSCongestion_Type()
)
ccasBwdRSCongestion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSCongestion.setStatus("current")
_CcasBwdRSCallingPartyCategory_Type = CASBackwardSignal
_CcasBwdRSCallingPartyCategory_Object = MibTableColumn
ccasBwdRSCallingPartyCategory = _CcasBwdRSCallingPartyCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 9),
    _CcasBwdRSCallingPartyCategory_Type()
)
ccasBwdRSCallingPartyCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSCallingPartyCategory.setStatus("current")
_CcasBwdRSAddrCompleteGroupA_Type = CASBackwardSignal
_CcasBwdRSAddrCompleteGroupA_Object = MibTableColumn
ccasBwdRSAddrCompleteGroupA = _CcasBwdRSAddrCompleteGroupA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 10),
    _CcasBwdRSAddrCompleteGroupA_Type()
)
ccasBwdRSAddrCompleteGroupA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSAddrCompleteGroupA.setStatus("current")
_CcasBwdRSPrevNminus2Digit_Type = CASBackwardSignal
_CcasBwdRSPrevNminus2Digit_Object = MibTableColumn
ccasBwdRSPrevNminus2Digit = _CcasBwdRSPrevNminus2Digit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 11),
    _CcasBwdRSPrevNminus2Digit_Type()
)
ccasBwdRSPrevNminus2Digit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSPrevNminus2Digit.setStatus("current")
_CcasBwdRSPrevNminus3Digit_Type = CASBackwardSignal
_CcasBwdRSPrevNminus3Digit_Object = MibTableColumn
ccasBwdRSPrevNminus3Digit = _CcasBwdRSPrevNminus3Digit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 12),
    _CcasBwdRSPrevNminus3Digit_Type()
)
ccasBwdRSPrevNminus3Digit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSPrevNminus3Digit.setStatus("current")
_CcasBwdRSCountryCode_Type = CASBackwardSignal
_CcasBwdRSCountryCode_Object = MibTableColumn
ccasBwdRSCountryCode = _CcasBwdRSCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 13),
    _CcasBwdRSCountryCode_Type()
)
ccasBwdRSCountryCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSCountryCode.setStatus("current")
_CcasBwdRSLangDiscr_Type = CASBackwardSignal
_CcasBwdRSLangDiscr_Object = MibTableColumn
ccasBwdRSLangDiscr = _CcasBwdRSLangDiscr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 14),
    _CcasBwdRSLangDiscr_Type()
)
ccasBwdRSLangDiscr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSLangDiscr.setStatus("current")
_CcasBwdRSNatureOfCircuit_Type = CASBackwardSignal
_CcasBwdRSNatureOfCircuit_Object = MibTableColumn
ccasBwdRSNatureOfCircuit = _CcasBwdRSNatureOfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 15),
    _CcasBwdRSNatureOfCircuit_Type()
)
ccasBwdRSNatureOfCircuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSNatureOfCircuit.setStatus("current")
_CcasBwdRSInfoEchoSuppressor_Type = CASBackwardSignal
_CcasBwdRSInfoEchoSuppressor_Object = MibTableColumn
ccasBwdRSInfoEchoSuppressor = _CcasBwdRSInfoEchoSuppressor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 16),
    _CcasBwdRSInfoEchoSuppressor_Type()
)
ccasBwdRSInfoEchoSuppressor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSInfoEchoSuppressor.setStatus("current")
_CcasBwdRSInternationalCongst_Type = CASBackwardSignal
_CcasBwdRSInternationalCongst_Object = MibTableColumn
ccasBwdRSInternationalCongst = _CcasBwdRSInternationalCongst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 17),
    _CcasBwdRSInternationalCongst_Type()
)
ccasBwdRSInternationalCongst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSInternationalCongst.setStatus("current")
_CcasBwdRSXtoGroupC_Type = CASBackwardSignal
_CcasBwdRSXtoGroupC_Object = MibTableColumn
ccasBwdRSXtoGroupC = _CcasBwdRSXtoGroupC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 18),
    _CcasBwdRSXtoGroupC_Type()
)
ccasBwdRSXtoGroupC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSXtoGroupC.setStatus("current")
_CcasBwdRSRepeatLastDigit_Type = CASBackwardSignal
_CcasBwdRSRepeatLastDigit_Object = MibTableColumn
ccasBwdRSRepeatLastDigit = _CcasBwdRSRepeatLastDigit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 19),
    _CcasBwdRSRepeatLastDigit_Type()
)
ccasBwdRSRepeatLastDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSRepeatLastDigit.setStatus("current")
_CcasBwdRSRepeatCalledDigit_Type = CASBackwardSignal
_CcasBwdRSRepeatCalledDigit_Object = MibTableColumn
ccasBwdRSRepeatCalledDigit = _CcasBwdRSRepeatCalledDigit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 20),
    _CcasBwdRSRepeatCalledDigit_Type()
)
ccasBwdRSRepeatCalledDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSRepeatCalledDigit.setStatus("current")
_CcasBwdRSPlaySITTone_Type = CASBackwardSignal
_CcasBwdRSPlaySITTone_Object = MibTableColumn
ccasBwdRSPlaySITTone = _CcasBwdRSPlaySITTone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 21),
    _CcasBwdRSPlaySITTone_Type()
)
ccasBwdRSPlaySITTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSPlaySITTone.setStatus("current")
_CcasBwdRSSubscriberLineBusy_Type = CASBackwardSignal
_CcasBwdRSSubscriberLineBusy_Object = MibTableColumn
ccasBwdRSSubscriberLineBusy = _CcasBwdRSSubscriberLineBusy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 22),
    _CcasBwdRSSubscriberLineBusy_Type()
)
ccasBwdRSSubscriberLineBusy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSSubscriberLineBusy.setStatus("current")
_CcasBwdRSNetworkCongstInGroupB_Type = CASBackwardSignal
_CcasBwdRSNetworkCongstInGroupB_Object = MibTableColumn
ccasBwdRSNetworkCongstInGroupB = _CcasBwdRSNetworkCongstInGroupB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 23),
    _CcasBwdRSNetworkCongstInGroupB_Type()
)
ccasBwdRSNetworkCongstInGroupB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSNetworkCongstInGroupB.setStatus("current")
_CcasBwdRSInvalidDialedNumber_Type = CASBackwardSignal
_CcasBwdRSInvalidDialedNumber_Object = MibTableColumn
ccasBwdRSInvalidDialedNumber = _CcasBwdRSInvalidDialedNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 24),
    _CcasBwdRSInvalidDialedNumber_Type()
)
ccasBwdRSInvalidDialedNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSInvalidDialedNumber.setStatus("current")
_CcasBwdRSSubLineFreeWithCharge_Type = CASBackwardSignal
_CcasBwdRSSubLineFreeWithCharge_Object = MibTableColumn
ccasBwdRSSubLineFreeWithCharge = _CcasBwdRSSubLineFreeWithCharge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 25),
    _CcasBwdRSSubLineFreeWithCharge_Type()
)
ccasBwdRSSubLineFreeWithCharge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSSubLineFreeWithCharge.setStatus("current")
_CcasBwdRSSubLineFreeWithNoCharge_Type = CASBackwardSignal
_CcasBwdRSSubLineFreeWithNoCharge_Object = MibTableColumn
ccasBwdRSSubLineFreeWithNoCharge = _CcasBwdRSSubLineFreeWithNoCharge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 26),
    _CcasBwdRSSubLineFreeWithNoCharge_Type()
)
ccasBwdRSSubLineFreeWithNoCharge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSSubLineFreeWithNoCharge.setStatus("current")
_CcasBwdRSSubLineOutOfOrder_Type = CASBackwardSignal
_CcasBwdRSSubLineOutOfOrder_Object = MibTableColumn
ccasBwdRSSubLineOutOfOrder = _CcasBwdRSSubLineOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 27),
    _CcasBwdRSSubLineOutOfOrder_Type()
)
ccasBwdRSSubLineOutOfOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSSubLineOutOfOrder.setStatus("current")
_CcasBwdRSAnnouncement_Type = CASBackwardSignal
_CcasBwdRSAnnouncement_Object = MibTableColumn
ccasBwdRSAnnouncement = _CcasBwdRSAnnouncement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 28),
    _CcasBwdRSAnnouncement_Type()
)
ccasBwdRSAnnouncement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSAnnouncement.setStatus("current")
_CcasBwdRSXtoGrpASendNextDNIS_Type = CASBackwardSignal
_CcasBwdRSXtoGrpASendNextDNIS_Object = MibTableColumn
ccasBwdRSXtoGrpASendNextDNIS = _CcasBwdRSXtoGrpASendNextDNIS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 29),
    _CcasBwdRSXtoGrpASendNextDNIS_Type()
)
ccasBwdRSXtoGrpASendNextDNIS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSXtoGrpASendNextDNIS.setStatus("current")
_CcasBwdRSXtoGrpASendDNISFrmBeg_Type = CASBackwardSignal
_CcasBwdRSXtoGrpASendDNISFrmBeg_Object = MibTableColumn
ccasBwdRSXtoGrpASendDNISFrmBeg = _CcasBwdRSXtoGrpASendDNISFrmBeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 30),
    _CcasBwdRSXtoGrpASendDNISFrmBeg_Type()
)
ccasBwdRSXtoGrpASendDNISFrmBeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSXtoGrpASendDNISFrmBeg.setStatus("current")
_CcasBwdRSXtoGrpAResendLastDNIS_Type = CASBackwardSignal
_CcasBwdRSXtoGrpAResendLastDNIS_Object = MibTableColumn
ccasBwdRSXtoGrpAResendLastDNIS = _CcasBwdRSXtoGrpAResendLastDNIS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 31),
    _CcasBwdRSXtoGrpAResendLastDNIS_Type()
)
ccasBwdRSXtoGrpAResendLastDNIS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSXtoGrpAResendLastDNIS.setStatus("current")
_CcasBwdRSSSendCatSwGrpB_Type = CASBackwardSignal
_CcasBwdRSSSendCatSwGrpB_Object = MibTableColumn
ccasBwdRSSSendCatSwGrpB = _CcasBwdRSSSendCatSwGrpB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 32),
    _CcasBwdRSSSendCatSwGrpB_Type()
)
ccasBwdRSSSendCatSwGrpB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSSSendCatSwGrpB.setStatus("current")
_CcasBwdRSSGrpCCong_Type = CASBackwardSignal
_CcasBwdRSSGrpCCong_Object = MibTableColumn
ccasBwdRSSGrpCCong = _CcasBwdRSSGrpCCong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 33),
    _CcasBwdRSSGrpCCong_Type()
)
ccasBwdRSSGrpCCong.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasBwdRSSGrpCCong.setStatus("current")
_CcasFwdRSANIDigitAvailable_Type = CASForwardSignal
_CcasFwdRSANIDigitAvailable_Object = MibTableColumn
ccasFwdRSANIDigitAvailable = _CcasFwdRSANIDigitAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 34),
    _CcasFwdRSANIDigitAvailable_Type()
)
ccasFwdRSANIDigitAvailable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSANIDigitAvailable.setStatus("current")
_CcasFwdRSANIDigitNotAvailable_Type = CASForwardSignal
_CcasFwdRSANIDigitNotAvailable_Object = MibTableColumn
ccasFwdRSANIDigitNotAvailable = _CcasFwdRSANIDigitNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 35),
    _CcasFwdRSANIDigitNotAvailable_Type()
)
ccasFwdRSANIDigitNotAvailable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSANIDigitNotAvailable.setStatus("current")
_CcasFwdRSEndANICallingPartyNotRev_Type = CASForwardSignal
_CcasFwdRSEndANICallingPartyNotRev_Object = MibTableColumn
ccasFwdRSEndANICallingPartyNotRev = _CcasFwdRSEndANICallingPartyNotRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 36),
    _CcasFwdRSEndANICallingPartyNotRev_Type()
)
ccasFwdRSEndANICallingPartyNotRev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSEndANICallingPartyNotRev.setStatus("current")
_CcasFwdRSEndANICallingPartyRev_Type = CASForwardSignal
_CcasFwdRSEndANICallingPartyRev_Object = MibTableColumn
ccasFwdRSEndANICallingPartyRev = _CcasFwdRSEndANICallingPartyRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 37),
    _CcasFwdRSEndANICallingPartyRev_Type()
)
ccasFwdRSEndANICallingPartyRev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSEndANICallingPartyRev.setStatus("current")
_CcasFwdRSEndOfDNISDigit_Type = CASForwardSignal
_CcasFwdRSEndOfDNISDigit_Object = MibTableColumn
ccasFwdRSEndOfDNISDigit = _CcasFwdRSEndOfDNISDigit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 38),
    _CcasFwdRSEndOfDNISDigit_Type()
)
ccasFwdRSEndOfDNISDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSEndOfDNISDigit.setStatus("current")
_CcasFwdRSNoCategoryAvailble_Type = CASForwardSignal
_CcasFwdRSNoCategoryAvailble_Object = MibTableColumn
ccasFwdRSNoCategoryAvailble = _CcasFwdRSNoCategoryAvailble_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 39),
    _CcasFwdRSNoCategoryAvailble_Type()
)
ccasFwdRSNoCategoryAvailble.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSNoCategoryAvailble.setStatus("current")
_CcasFwdRSCCEchoSuppressor_Type = CASForwardSignal
_CcasFwdRSCCEchoSuppressor_Object = MibTableColumn
ccasFwdRSCCEchoSuppressor = _CcasFwdRSCCEchoSuppressor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 40),
    _CcasFwdRSCCEchoSuppressor_Type()
)
ccasFwdRSCCEchoSuppressor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSCCEchoSuppressor.setStatus("current")
_CcasFwdRSCCNoEchoSuppressor_Type = CASForwardSignal
_CcasFwdRSCCNoEchoSuppressor_Object = MibTableColumn
ccasFwdRSCCNoEchoSuppressor = _CcasFwdRSCCNoEchoSuppressor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 41),
    _CcasFwdRSCCNoEchoSuppressor_Type()
)
ccasFwdRSCCNoEchoSuppressor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSCCNoEchoSuppressor.setStatus("current")
_CcasFwdRSCCInsertEchoSuppressor_Type = CASForwardSignal
_CcasFwdRSCCInsertEchoSuppressor_Object = MibTableColumn
ccasFwdRSCCInsertEchoSuppressor = _CcasFwdRSCCInsertEchoSuppressor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 42),
    _CcasFwdRSCCInsertEchoSuppressor_Type()
)
ccasFwdRSCCInsertEchoSuppressor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSCCInsertEchoSuppressor.setStatus("current")
_CcasFwdRSIncHalfEchoRequired_Type = CASForwardSignal
_CcasFwdRSIncHalfEchoRequired_Object = MibTableColumn
ccasFwdRSIncHalfEchoRequired = _CcasFwdRSIncHalfEchoRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 43),
    _CcasFwdRSIncHalfEchoRequired_Type()
)
ccasFwdRSIncHalfEchoRequired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSIncHalfEchoRequired.setStatus("current")
_CcasFwdRSTestCall_Type = CASForwardSignal
_CcasFwdRSTestCall_Object = MibTableColumn
ccasFwdRSTestCall = _CcasFwdRSTestCall_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 44),
    _CcasFwdRSTestCall_Type()
)
ccasFwdRSTestCall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSTestCall.setStatus("current")
_CcasFwdRSSatelLinkIncluded_Type = CASForwardSignal
_CcasFwdRSSatelLinkIncluded_Object = MibTableColumn
ccasFwdRSSatelLinkIncluded = _CcasFwdRSSatelLinkIncluded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 45),
    _CcasFwdRSSatelLinkIncluded_Type()
)
ccasFwdRSSatelLinkIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSSatelLinkIncluded.setStatus("current")
_CcasFwdRSSatelLinkNotIncluded_Type = CASForwardSignal
_CcasFwdRSSatelLinkNotIncluded_Object = MibTableColumn
ccasFwdRSSatelLinkNotIncluded = _CcasFwdRSSatelLinkNotIncluded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 46),
    _CcasFwdRSSatelLinkNotIncluded_Type()
)
ccasFwdRSSatelLinkNotIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSSatelLinkNotIncluded.setStatus("current")
_CcasFwdRSDiscriminatorDigit_Type = CASForwardSignal
_CcasFwdRSDiscriminatorDigit_Object = MibTableColumn
ccasFwdRSDiscriminatorDigit = _CcasFwdRSDiscriminatorDigit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 47),
    _CcasFwdRSDiscriminatorDigit_Type()
)
ccasFwdRSDiscriminatorDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSDiscriminatorDigit.setStatus("current")
_CcasFwdRSOtherLanguage_Type = CASForwardSignal
_CcasFwdRSOtherLanguage_Object = MibTableColumn
ccasFwdRSOtherLanguage = _CcasFwdRSOtherLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 48),
    _CcasFwdRSOtherLanguage_Type()
)
ccasFwdRSOtherLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSOtherLanguage.setStatus("current")
_CcasFwdRSOtherLanguage1_Type = CASForwardSignal
_CcasFwdRSOtherLanguage1_Object = MibTableColumn
ccasFwdRSOtherLanguage1 = _CcasFwdRSOtherLanguage1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 49),
    _CcasFwdRSOtherLanguage1_Type()
)
ccasFwdRSOtherLanguage1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSOtherLanguage1.setStatus("current")
_CcasFwdRSOtherLanguage2_Type = CASForwardSignal
_CcasFwdRSOtherLanguage2_Object = MibTableColumn
ccasFwdRSOtherLanguage2 = _CcasFwdRSOtherLanguage2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 50),
    _CcasFwdRSOtherLanguage2_Type()
)
ccasFwdRSOtherLanguage2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSOtherLanguage2.setStatus("current")
_CcasFwdRSRequestNotAccepted_Type = CASForwardSignal
_CcasFwdRSRequestNotAccepted_Object = MibTableColumn
ccasFwdRSRequestNotAccepted = _CcasFwdRSRequestNotAccepted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 51),
    _CcasFwdRSRequestNotAccepted_Type()
)
ccasFwdRSRequestNotAccepted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSRequestNotAccepted.setStatus("current")
_CcasFwdRSSubWithoutPriorNational_Type = CASForwardSignal
_CcasFwdRSSubWithoutPriorNational_Object = MibTableColumn
ccasFwdRSSubWithoutPriorNational = _CcasFwdRSSubWithoutPriorNational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 52),
    _CcasFwdRSSubWithoutPriorNational_Type()
)
ccasFwdRSSubWithoutPriorNational.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSSubWithoutPriorNational.setStatus("current")
_CcasFwdRSSubPriorNational_Type = CASForwardSignal
_CcasFwdRSSubPriorNational_Object = MibTableColumn
ccasFwdRSSubPriorNational = _CcasFwdRSSubPriorNational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 53),
    _CcasFwdRSSubPriorNational_Type()
)
ccasFwdRSSubPriorNational.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSSubPriorNational.setStatus("current")
_CcasFwdRSSubPriorInternational_Type = CASForwardSignal
_CcasFwdRSSubPriorInternational_Object = MibTableColumn
ccasFwdRSSubPriorInternational = _CcasFwdRSSubPriorInternational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 54),
    _CcasFwdRSSubPriorInternational_Type()
)
ccasFwdRSSubPriorInternational.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSSubPriorInternational.setStatus("current")
_CcasFwdRSMaintenanceEquipment_Type = CASForwardSignal
_CcasFwdRSMaintenanceEquipment_Object = MibTableColumn
ccasFwdRSMaintenanceEquipment = _CcasFwdRSMaintenanceEquipment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 55),
    _CcasFwdRSMaintenanceEquipment_Type()
)
ccasFwdRSMaintenanceEquipment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSMaintenanceEquipment.setStatus("current")
_CcasFwdRSOperatorCall_Type = CASForwardSignal
_CcasFwdRSOperatorCall_Object = MibTableColumn
ccasFwdRSOperatorCall = _CcasFwdRSOperatorCall_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 56),
    _CcasFwdRSOperatorCall_Type()
)
ccasFwdRSOperatorCall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSOperatorCall.setStatus("current")
_CcasFwdRSDataTransNational_Type = CASForwardSignal
_CcasFwdRSDataTransNational_Object = MibTableColumn
ccasFwdRSDataTransNational = _CcasFwdRSDataTransNational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 57),
    _CcasFwdRSDataTransNational_Type()
)
ccasFwdRSDataTransNational.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSDataTransNational.setStatus("current")
_CcasFwdRSDataTransInternational_Type = CASForwardSignal
_CcasFwdRSDataTransInternational_Object = MibTableColumn
ccasFwdRSDataTransInternational = _CcasFwdRSDataTransInternational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 58),
    _CcasFwdRSDataTransInternational_Type()
)
ccasFwdRSDataTransInternational.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSDataTransInternational.setStatus("current")
_CcasFwdRSOperNoFwdTransFacility_Type = CASForwardSignal
_CcasFwdRSOperNoFwdTransFacility_Object = MibTableColumn
ccasFwdRSOperNoFwdTransFacility = _CcasFwdRSOperNoFwdTransFacility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 59),
    _CcasFwdRSOperNoFwdTransFacility_Type()
)
ccasFwdRSOperNoFwdTransFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSOperNoFwdTransFacility.setStatus("current")
_CcasFwdRSOperFwdTransFacility_Type = CASForwardSignal
_CcasFwdRSOperFwdTransFacility_Object = MibTableColumn
ccasFwdRSOperFwdTransFacility = _CcasFwdRSOperFwdTransFacility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 60),
    _CcasFwdRSOperFwdTransFacility_Type()
)
ccasFwdRSOperFwdTransFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSOperFwdTransFacility.setStatus("current")
_CcasFwdRSSubsrcWithMeter_Type = CASForwardSignal
_CcasFwdRSSubsrcWithMeter_Object = MibTableColumn
ccasFwdRSSubsrcWithMeter = _CcasFwdRSSubsrcWithMeter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 61),
    _CcasFwdRSSubsrcWithMeter_Type()
)
ccasFwdRSSubsrcWithMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSSubsrcWithMeter.setStatus("current")
_CcasFwdRSSubsrcWithIDD_Type = CASForwardSignal
_CcasFwdRSSubsrcWithIDD_Object = MibTableColumn
ccasFwdRSSubsrcWithIDD = _CcasFwdRSSubsrcWithIDD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 62),
    _CcasFwdRSSubsrcWithIDD_Type()
)
ccasFwdRSSubsrcWithIDD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasFwdRSSubsrcWithIDD.setStatus("current")


class _CcasRSInterpreFirstANIDigit_Type(Integer32):
    """Custom type ccasRSInterpreFirstANIDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aniAvailableOrNot", 2),
          ("firstANIDigit", 1),
          ("subscriberCategory", 3))
    )


_CcasRSInterpreFirstANIDigit_Type.__name__ = "Integer32"
_CcasRSInterpreFirstANIDigit_Object = MibTableColumn
ccasRSInterpreFirstANIDigit = _CcasRSInterpreFirstANIDigit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 63),
    _CcasRSInterpreFirstANIDigit_Type()
)
ccasRSInterpreFirstANIDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSInterpreFirstANIDigit.setStatus("current")


class _CcasRSGetValueFromValidIndex_Type(Unsigned32):
    """Custom type ccasRSGetValueFromValidIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_CcasRSGetValueFromValidIndex_Type.__name__ = "Unsigned32"
_CcasRSGetValueFromValidIndex_Object = MibTableColumn
ccasRSGetValueFromValidIndex = _CcasRSGetValueFromValidIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 64),
    _CcasRSGetValueFromValidIndex_Type()
)
ccasRSGetValueFromValidIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSGetValueFromValidIndex.setStatus("current")


class _CcasRSSeqInfCollect_Type(SnmpAdminString):
    """Custom type ccasRSSeqInfCollect based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CcasRSSeqInfCollect_Type.__name__ = "SnmpAdminString"
_CcasRSSeqInfCollect_Object = MibTableColumn
ccasRSSeqInfCollect = _CcasRSSeqInfCollect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 65),
    _CcasRSSeqInfCollect_Type()
)
ccasRSSeqInfCollect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSSeqInfCollect.setStatus("current")


class _CcasRSSendFirstFwdSig_Type(Integer32):
    """Custom type ccasRSSendFirstFwdSig based on Integer32"""
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
        *(("cCDnisLangDisc", 4),
          ("cCLangDiscDnis", 3),
          ("dnisCCLangDisc", 1),
          ("dnisLangDiscCC", 2),
          ("langDiscCCDnis", 5),
          ("langDiscDnisCC", 6))
    )


_CcasRSSendFirstFwdSig_Type.__name__ = "Integer32"
_CcasRSSendFirstFwdSig_Object = MibTableColumn
ccasRSSendFirstFwdSig = _CcasRSSendFirstFwdSig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 66),
    _CcasRSSendFirstFwdSig_Type()
)
ccasRSSendFirstFwdSig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSSendFirstFwdSig.setStatus("current")
_CcasRSRowStatus_Type = RowStatus
_CcasRSRowStatus_Object = MibTableColumn
ccasRSRowStatus = _CcasRSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 4, 1, 1, 67),
    _CcasRSRowStatus_Type()
)
ccasRSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSRowStatus.setStatus("current")
_CcasIfExtConfigTimer_ObjectIdentity = ObjectIdentity
ccasIfExtConfigTimer = _CcasIfExtConfigTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5)
)
_CcasIfExtRegSignalTimerTable_Object = MibTable
ccasIfExtRegSignalTimerTable = _CcasIfExtRegSignalTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ccasIfExtRegSignalTimerTable.setStatus("current")
_CcasIfExtRegSignalTimerEntry_Object = MibTableRow
ccasIfExtRegSignalTimerEntry = _CcasIfExtRegSignalTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1)
)
ccasIfExtRegSignalTimerEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-CAS-IF-EXT-MIB", "ccasRSTIndex"),
)
if mibBuilder.loadTexts:
    ccasIfExtRegSignalTimerEntry.setStatus("current")


class _CcasRSTIndex_Type(Unsigned32):
    """Custom type ccasRSTIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasRSTIndex_Type.__name__ = "Unsigned32"
_CcasRSTIndex_Object = MibTableColumn
ccasRSTIndex = _CcasRSTIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 1),
    _CcasRSTIndex_Type()
)
ccasRSTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccasRSTIndex.setStatus("current")


class _CcasRSTAnswerSigTimer_Type(Unsigned32):
    """Custom type ccasRSTAnswerSigTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasRSTAnswerSigTimer_Type.__name__ = "Unsigned32"
_CcasRSTAnswerSigTimer_Object = MibTableColumn
ccasRSTAnswerSigTimer = _CcasRSTAnswerSigTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 2),
    _CcasRSTAnswerSigTimer_Type()
)
ccasRSTAnswerSigTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTAnswerSigTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasRSTAnswerSigTimer.setUnits("seconds")


class _CcasRSTCompelledFwdToneOnTimer_Type(Unsigned32):
    """Custom type ccasRSTCompelledFwdToneOnTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasRSTCompelledFwdToneOnTimer_Type.__name__ = "Unsigned32"
_CcasRSTCompelledFwdToneOnTimer_Object = MibTableColumn
ccasRSTCompelledFwdToneOnTimer = _CcasRSTCompelledFwdToneOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 3),
    _CcasRSTCompelledFwdToneOnTimer_Type()
)
ccasRSTCompelledFwdToneOnTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTCompelledFwdToneOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasRSTCompelledFwdToneOnTimer.setUnits("seconds")


class _CcasRSTCompelledFwdToneOffTimer_Type(Unsigned32):
    """Custom type ccasRSTCompelledFwdToneOffTimer based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasRSTCompelledFwdToneOffTimer_Type.__name__ = "Unsigned32"
_CcasRSTCompelledFwdToneOffTimer_Object = MibTableColumn
ccasRSTCompelledFwdToneOffTimer = _CcasRSTCompelledFwdToneOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 4),
    _CcasRSTCompelledFwdToneOffTimer_Type()
)
ccasRSTCompelledFwdToneOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTCompelledFwdToneOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasRSTCompelledFwdToneOffTimer.setUnits("seconds")


class _CcasRSTCompelledBwdToneOnTimer_Type(Unsigned32):
    """Custom type ccasRSTCompelledBwdToneOnTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasRSTCompelledBwdToneOnTimer_Type.__name__ = "Unsigned32"
_CcasRSTCompelledBwdToneOnTimer_Object = MibTableColumn
ccasRSTCompelledBwdToneOnTimer = _CcasRSTCompelledBwdToneOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 5),
    _CcasRSTCompelledBwdToneOnTimer_Type()
)
ccasRSTCompelledBwdToneOnTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTCompelledBwdToneOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasRSTCompelledBwdToneOnTimer.setUnits("seconds")


class _CcasRSTOutFwdPulseOnTimer_Type(Unsigned32):
    """Custom type ccasRSTOutFwdPulseOnTimer based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasRSTOutFwdPulseOnTimer_Type.__name__ = "Unsigned32"
_CcasRSTOutFwdPulseOnTimer_Object = MibTableColumn
ccasRSTOutFwdPulseOnTimer = _CcasRSTOutFwdPulseOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 6),
    _CcasRSTOutFwdPulseOnTimer_Type()
)
ccasRSTOutFwdPulseOnTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTOutFwdPulseOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasRSTOutFwdPulseOnTimer.setUnits("milliseconds")


class _CcasRSTOutFwdPulseOffTimer_Type(Unsigned32):
    """Custom type ccasRSTOutFwdPulseOffTimer based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasRSTOutFwdPulseOffTimer_Type.__name__ = "Unsigned32"
_CcasRSTOutFwdPulseOffTimer_Object = MibTableColumn
ccasRSTOutFwdPulseOffTimer = _CcasRSTOutFwdPulseOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 7),
    _CcasRSTOutFwdPulseOffTimer_Type()
)
ccasRSTOutFwdPulseOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTOutFwdPulseOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasRSTOutFwdPulseOffTimer.setUnits("milliseconds")


class _CcasRSTIncFwdPulseOnTimer_Type(Unsigned32):
    """Custom type ccasRSTIncFwdPulseOnTimer based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasRSTIncFwdPulseOnTimer_Type.__name__ = "Unsigned32"
_CcasRSTIncFwdPulseOnTimer_Object = MibTableColumn
ccasRSTIncFwdPulseOnTimer = _CcasRSTIncFwdPulseOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 8),
    _CcasRSTIncFwdPulseOnTimer_Type()
)
ccasRSTIncFwdPulseOnTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTIncFwdPulseOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasRSTIncFwdPulseOnTimer.setUnits("milliseconds")


class _CcasRSTBwdPulseOnTimer_Type(Unsigned32):
    """Custom type ccasRSTBwdPulseOnTimer based on Unsigned32"""
    defaultValue = 150

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasRSTBwdPulseOnTimer_Type.__name__ = "Unsigned32"
_CcasRSTBwdPulseOnTimer_Object = MibTableColumn
ccasRSTBwdPulseOnTimer = _CcasRSTBwdPulseOnTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 9),
    _CcasRSTBwdPulseOnTimer_Type()
)
ccasRSTBwdPulseOnTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTBwdPulseOnTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasRSTBwdPulseOnTimer.setUnits("milliseconds")


class _CcasRSTIncomingRegSigDuration_Type(Unsigned32):
    """Custom type ccasRSTIncomingRegSigDuration based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasRSTIncomingRegSigDuration_Type.__name__ = "Unsigned32"
_CcasRSTIncomingRegSigDuration_Object = MibTableColumn
ccasRSTIncomingRegSigDuration = _CcasRSTIncomingRegSigDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 10),
    _CcasRSTIncomingRegSigDuration_Type()
)
ccasRSTIncomingRegSigDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTIncomingRegSigDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasRSTIncomingRegSigDuration.setUnits("seconds")


class _CcasRSTOutgoingRegSigDuration_Type(Unsigned32):
    """Custom type ccasRSTOutgoingRegSigDuration based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasRSTOutgoingRegSigDuration_Type.__name__ = "Unsigned32"
_CcasRSTOutgoingRegSigDuration_Object = MibTableColumn
ccasRSTOutgoingRegSigDuration = _CcasRSTOutgoingRegSigDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 11),
    _CcasRSTOutgoingRegSigDuration_Type()
)
ccasRSTOutgoingRegSigDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTOutgoingRegSigDuration.setStatus("current")
if mibBuilder.loadTexts:
    ccasRSTOutgoingRegSigDuration.setUnits("seconds")


class _CcasRSTCalledPartyInterDigTimer_Type(Unsigned32):
    """Custom type ccasRSTCalledPartyInterDigTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasRSTCalledPartyInterDigTimer_Type.__name__ = "Unsigned32"
_CcasRSTCalledPartyInterDigTimer_Object = MibTableColumn
ccasRSTCalledPartyInterDigTimer = _CcasRSTCalledPartyInterDigTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 12),
    _CcasRSTCalledPartyInterDigTimer_Type()
)
ccasRSTCalledPartyInterDigTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTCalledPartyInterDigTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasRSTCalledPartyInterDigTimer.setUnits("seconds")
_CcasRSTRowStatus_Type = RowStatus
_CcasRSTRowStatus_Object = MibTableColumn
ccasRSTRowStatus = _CcasRSTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 5, 2, 1, 13),
    _CcasRSTRowStatus_Type()
)
ccasRSTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasRSTRowStatus.setStatus("current")
_CcasIfExtGeneralConfig_ObjectIdentity = ObjectIdentity
ccasIfExtGeneralConfig = _CcasIfExtGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6)
)
_CcasIfExtGeneralConfigTable_Object = MibTable
ccasIfExtGeneralConfigTable = _CcasIfExtGeneralConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ccasIfExtGeneralConfigTable.setStatus("current")
_CcasIfExtGeneralConfigEntry_Object = MibTableRow
ccasIfExtGeneralConfigEntry = _CcasIfExtGeneralConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1)
)
ccasIfExtGeneralConfigEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-CAS-IF-EXT-MIB", "ccasGCnfIndex"),
)
if mibBuilder.loadTexts:
    ccasIfExtGeneralConfigEntry.setStatus("current")


class _CcasGCnfIndex_Type(Unsigned32):
    """Custom type ccasGCnfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcasGCnfIndex_Type.__name__ = "Unsigned32"
_CcasGCnfIndex_Object = MibTableColumn
ccasGCnfIndex = _CcasGCnfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 1),
    _CcasGCnfIndex_Type()
)
ccasGCnfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccasGCnfIndex.setStatus("current")


class _CcasGCnfGlarePolicy_Type(Integer32):
    """Custom type ccasGCnfGlarePolicy based on Integer32"""
    defaultValue = 1

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
        *(("goOnHookOnGlareDet", 4),
          ("rptRelOnGlareTmrExpAndGoOnHook", 3),
          ("rptSzOnGlareDet", 2),
          ("rptSzOnGlareTmrExp", 1))
    )


_CcasGCnfGlarePolicy_Type.__name__ = "Integer32"
_CcasGCnfGlarePolicy_Object = MibTableColumn
ccasGCnfGlarePolicy = _CcasGCnfGlarePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 2),
    _CcasGCnfGlarePolicy_Type()
)
ccasGCnfGlarePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfGlarePolicy.setStatus("current")


class _CcasGCnfParmSource_Type(Integer32):
    """Custom type ccasGCnfParmSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("casVariantFile", 1),
          ("mib", 2))
    )


_CcasGCnfParmSource_Type.__name__ = "Integer32"
_CcasGCnfParmSource_Object = MibTableColumn
ccasGCnfParmSource = _CcasGCnfParmSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 3),
    _CcasGCnfParmSource_Type()
)
ccasGCnfParmSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfParmSource.setStatus("current")


class _CcasGCnfRegSigMode_Type(CASRegisterSignal):
    """Custom type ccasGCnfRegSigMode based on CASRegisterSignal"""


_CcasGCnfRegSigMode_Object = MibTableColumn
ccasGCnfRegSigMode = _CcasGCnfRegSigMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 4),
    _CcasGCnfRegSigMode_Type()
)
ccasGCnfRegSigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfRegSigMode.setStatus("current")


class _CcasGCnfLineSigType_Type(Integer32):
    """Custom type ccasGCnfLineSigType based on Integer32"""
    defaultValue = 1

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
          ("digital", 1),
          ("pulse", 3))
    )


_CcasGCnfLineSigType_Type.__name__ = "Integer32"
_CcasGCnfLineSigType_Object = MibTableColumn
ccasGCnfLineSigType = _CcasGCnfLineSigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 5),
    _CcasGCnfLineSigType_Type()
)
ccasGCnfLineSigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfLineSigType.setStatus("current")


class _CcasGCnfRingBackType_Type(Integer32):
    """Custom type ccasGCnfRingBackType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wink", 1),
          ("winkAndTone", 2))
    )


_CcasGCnfRingBackType_Type.__name__ = "Integer32"
_CcasGCnfRingBackType_Object = MibTableColumn
ccasGCnfRingBackType = _CcasGCnfRingBackType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 6),
    _CcasGCnfRingBackType_Type()
)
ccasGCnfRingBackType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfRingBackType.setStatus("current")


class _CcasGCnfIncCallHiFreqPower_Type(Integer32):
    """Custom type ccasGCnfIncCallHiFreqPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_CcasGCnfIncCallHiFreqPower_Type.__name__ = "Integer32"
_CcasGCnfIncCallHiFreqPower_Object = MibTableColumn
ccasGCnfIncCallHiFreqPower = _CcasGCnfIncCallHiFreqPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 7),
    _CcasGCnfIncCallHiFreqPower_Type()
)
ccasGCnfIncCallHiFreqPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfIncCallHiFreqPower.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfIncCallHiFreqPower.setUnits("dBm")


class _CcasGCnfIncCallLoFreqPower_Type(Integer32):
    """Custom type ccasGCnfIncCallLoFreqPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_CcasGCnfIncCallLoFreqPower_Type.__name__ = "Integer32"
_CcasGCnfIncCallLoFreqPower_Object = MibTableColumn
ccasGCnfIncCallLoFreqPower = _CcasGCnfIncCallLoFreqPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 8),
    _CcasGCnfIncCallLoFreqPower_Type()
)
ccasGCnfIncCallLoFreqPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfIncCallLoFreqPower.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfIncCallLoFreqPower.setUnits("dBm")


class _CcasGCnfIncCallNegTwist_Type(Integer32):
    """Custom type ccasGCnfIncCallNegTwist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_CcasGCnfIncCallNegTwist_Type.__name__ = "Integer32"
_CcasGCnfIncCallNegTwist_Object = MibTableColumn
ccasGCnfIncCallNegTwist = _CcasGCnfIncCallNegTwist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 9),
    _CcasGCnfIncCallNegTwist_Type()
)
ccasGCnfIncCallNegTwist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfIncCallNegTwist.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfIncCallNegTwist.setUnits("dBm")


class _CcasGCnfIncCallPosTwist_Type(Integer32):
    """Custom type ccasGCnfIncCallPosTwist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_CcasGCnfIncCallPosTwist_Type.__name__ = "Integer32"
_CcasGCnfIncCallPosTwist_Object = MibTableColumn
ccasGCnfIncCallPosTwist = _CcasGCnfIncCallPosTwist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 10),
    _CcasGCnfIncCallPosTwist_Type()
)
ccasGCnfIncCallPosTwist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfIncCallPosTwist.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfIncCallPosTwist.setUnits("dBm")


class _CcasGCnfIncCallBreakThreshold_Type(Integer32):
    """Custom type ccasGCnfIncCallBreakThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_CcasGCnfIncCallBreakThreshold_Type.__name__ = "Integer32"
_CcasGCnfIncCallBreakThreshold_Object = MibTableColumn
ccasGCnfIncCallBreakThreshold = _CcasGCnfIncCallBreakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 11),
    _CcasGCnfIncCallBreakThreshold_Type()
)
ccasGCnfIncCallBreakThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfIncCallBreakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfIncCallBreakThreshold.setUnits("dBm")


class _CcasGCnfOutCallLoFreqPower_Type(Integer32):
    """Custom type ccasGCnfOutCallLoFreqPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_CcasGCnfOutCallLoFreqPower_Type.__name__ = "Integer32"
_CcasGCnfOutCallLoFreqPower_Object = MibTableColumn
ccasGCnfOutCallLoFreqPower = _CcasGCnfOutCallLoFreqPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 12),
    _CcasGCnfOutCallLoFreqPower_Type()
)
ccasGCnfOutCallLoFreqPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfOutCallLoFreqPower.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfOutCallLoFreqPower.setUnits("dBm")


class _CcasGCnfOutCallPowerTwist_Type(Integer32):
    """Custom type ccasGCnfOutCallPowerTwist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_CcasGCnfOutCallPowerTwist_Type.__name__ = "Integer32"
_CcasGCnfOutCallPowerTwist_Object = MibTableColumn
ccasGCnfOutCallPowerTwist = _CcasGCnfOutCallPowerTwist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 13),
    _CcasGCnfOutCallPowerTwist_Type()
)
ccasGCnfOutCallPowerTwist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfOutCallPowerTwist.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfOutCallPowerTwist.setUnits("dBm")


class _CcasGCnfOutCadenceOntime_Type(Unsigned32):
    """Custom type ccasGCnfOutCadenceOntime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasGCnfOutCadenceOntime_Type.__name__ = "Unsigned32"
_CcasGCnfOutCadenceOntime_Object = MibTableColumn
ccasGCnfOutCadenceOntime = _CcasGCnfOutCadenceOntime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 14),
    _CcasGCnfOutCadenceOntime_Type()
)
ccasGCnfOutCadenceOntime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfOutCadenceOntime.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfOutCadenceOntime.setUnits("milliseconds")


class _CcasGCnfOutCadenceOfftime_Type(Unsigned32):
    """Custom type ccasGCnfOutCadenceOfftime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasGCnfOutCadenceOfftime_Type.__name__ = "Unsigned32"
_CcasGCnfOutCadenceOfftime_Object = MibTableColumn
ccasGCnfOutCadenceOfftime = _CcasGCnfOutCadenceOfftime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 15),
    _CcasGCnfOutCadenceOfftime_Type()
)
ccasGCnfOutCadenceOfftime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfOutCadenceOfftime.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfOutCadenceOfftime.setUnits("milliseconds")


class _CcasGCnfCountryCode_Type(SnmpAdminString):
    """Custom type ccasGCnfCountryCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CcasGCnfCountryCode_Type.__name__ = "SnmpAdminString"
_CcasGCnfCountryCode_Object = MibTableColumn
ccasGCnfCountryCode = _CcasGCnfCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 16),
    _CcasGCnfCountryCode_Type()
)
ccasGCnfCountryCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfCountryCode.setStatus("current")


class _CcasGCnfEchoCancellation_Type(Integer32):
    """Custom type ccasGCnfEchoCancellation based on Integer32"""
    defaultValue = 2

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
        *(("incomingHalfEchoSuppressorRequired", 4),
          ("noEchoRequired", 1),
          ("outgoingHalfEchoRequired", 2),
          ("outgoingHalfEchoSuppressorInserted", 3))
    )


_CcasGCnfEchoCancellation_Type.__name__ = "Integer32"
_CcasGCnfEchoCancellation_Object = MibTableColumn
ccasGCnfEchoCancellation = _CcasGCnfEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 17),
    _CcasGCnfEchoCancellation_Type()
)
ccasGCnfEchoCancellation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfEchoCancellation.setStatus("current")


class _CcasGCnfSubscriberCategory_Type(Integer32):
    """Custom type ccasGCnfSubscriberCategory based on Integer32"""
    defaultValue = 1

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
        *(("dataInternationalTransmission", 8),
          ("dataNationalTransmission", 5),
          ("maintenanceEquipment", 3),
          ("operatorCall", 4),
          ("operatorWithForwardTransfer", 7),
          ("subscriberOrOperatorWithoutForwardTransfer", 6),
          ("subscriberWithPriority", 2),
          ("subscriberWithoutPriority", 1))
    )


_CcasGCnfSubscriberCategory_Type.__name__ = "Integer32"
_CcasGCnfSubscriberCategory_Object = MibTableColumn
ccasGCnfSubscriberCategory = _CcasGCnfSubscriberCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 18),
    _CcasGCnfSubscriberCategory_Type()
)
ccasGCnfSubscriberCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfSubscriberCategory.setStatus("current")


class _CcasGCnfNatureOfCircuit_Type(Integer32):
    """Custom type ccasGCnfNatureOfCircuit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("included", 2),
          ("notIncluded", 1))
    )


_CcasGCnfNatureOfCircuit_Type.__name__ = "Integer32"
_CcasGCnfNatureOfCircuit_Object = MibTableColumn
ccasGCnfNatureOfCircuit = _CcasGCnfNatureOfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 19),
    _CcasGCnfNatureOfCircuit_Type()
)
ccasGCnfNatureOfCircuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfNatureOfCircuit.setStatus("current")


class _CcasGCnfCompelledSignalingType_Type(Integer32):
    """Custom type ccasGCnfCompelledSignalingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enbloc", 1),
          ("endtoend", 3),
          ("overlap", 2))
    )


_CcasGCnfCompelledSignalingType_Type.__name__ = "Integer32"
_CcasGCnfCompelledSignalingType_Object = MibTableColumn
ccasGCnfCompelledSignalingType = _CcasGCnfCompelledSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 20),
    _CcasGCnfCompelledSignalingType_Type()
)
ccasGCnfCompelledSignalingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfCompelledSignalingType.setStatus("current")


class _CcasGCnfTxDigitOrder_Type(Integer32):
    """Custom type ccasGCnfTxDigitOrder based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aniDnis", 1),
          ("dnisAni", 2))
    )


_CcasGCnfTxDigitOrder_Type.__name__ = "Integer32"
_CcasGCnfTxDigitOrder_Object = MibTableColumn
ccasGCnfTxDigitOrder = _CcasGCnfTxDigitOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 21),
    _CcasGCnfTxDigitOrder_Type()
)
ccasGCnfTxDigitOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfTxDigitOrder.setStatus("current")


class _CcasGCnfDigitDetectMode_Type(Integer32):
    """Custom type ccasGCnfDigitDetectMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp", 3),
          ("dtmf", 1),
          ("mf", 2))
    )


_CcasGCnfDigitDetectMode_Type.__name__ = "Integer32"
_CcasGCnfDigitDetectMode_Object = MibTableColumn
ccasGCnfDigitDetectMode = _CcasGCnfDigitDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 22),
    _CcasGCnfDigitDetectMode_Type()
)
ccasGCnfDigitDetectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfDigitDetectMode.setStatus("current")


class _CcasGCnfMeteringRepIntThresh_Type(Unsigned32):
    """Custom type ccasGCnfMeteringRepIntThresh based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasGCnfMeteringRepIntThresh_Type.__name__ = "Unsigned32"
_CcasGCnfMeteringRepIntThresh_Object = MibTableColumn
ccasGCnfMeteringRepIntThresh = _CcasGCnfMeteringRepIntThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 23),
    _CcasGCnfMeteringRepIntThresh_Type()
)
ccasGCnfMeteringRepIntThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfMeteringRepIntThresh.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfMeteringRepIntThresh.setUnits("milliseconds")


class _CcasGCnfStartTimer_Type(Unsigned32):
    """Custom type ccasGCnfStartTimer based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CcasGCnfStartTimer_Type.__name__ = "Unsigned32"
_CcasGCnfStartTimer_Object = MibTableColumn
ccasGCnfStartTimer = _CcasGCnfStartTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 24),
    _CcasGCnfStartTimer_Type()
)
ccasGCnfStartTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfStartTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfStartTimer.setUnits("seconds")


class _CcasGCnfLongTimer_Type(Unsigned32):
    """Custom type ccasGCnfLongTimer based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CcasGCnfLongTimer_Type.__name__ = "Unsigned32"
_CcasGCnfLongTimer_Object = MibTableColumn
ccasGCnfLongTimer = _CcasGCnfLongTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 25),
    _CcasGCnfLongTimer_Type()
)
ccasGCnfLongTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfLongTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfLongTimer.setUnits("seconds")


class _CcasGCnfShortTimer_Type(Unsigned32):
    """Custom type ccasGCnfShortTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CcasGCnfShortTimer_Type.__name__ = "Unsigned32"
_CcasGCnfShortTimer_Object = MibTableColumn
ccasGCnfShortTimer = _CcasGCnfShortTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 26),
    _CcasGCnfShortTimer_Type()
)
ccasGCnfShortTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfShortTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfShortTimer.setUnits("seconds")


class _CcasGCnfLongDurationTimer_Type(Unsigned32):
    """Custom type ccasGCnfLongDurationTimer based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 9900),
    )


_CcasGCnfLongDurationTimer_Type.__name__ = "Unsigned32"
_CcasGCnfLongDurationTimer_Object = MibTableColumn
ccasGCnfLongDurationTimer = _CcasGCnfLongDurationTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 27),
    _CcasGCnfLongDurationTimer_Type()
)
ccasGCnfLongDurationTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfLongDurationTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfLongDurationTimer.setUnits("milliseconds")


class _CcasGCnfMGCTimer_Type(Unsigned32):
    """Custom type ccasGCnfMGCTimer based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcasGCnfMGCTimer_Type.__name__ = "Unsigned32"
_CcasGCnfMGCTimer_Object = MibTableColumn
ccasGCnfMGCTimer = _CcasGCnfMGCTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 28),
    _CcasGCnfMGCTimer_Type()
)
ccasGCnfMGCTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfMGCTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfMGCTimer.setUnits("milliseconds")


class _CcasGCnfDigitType_Type(Integer32):
    """Custom type ccasGCnfDigitType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dp", 3),
          ("dtmf", 1),
          ("mf", 2))
    )


_CcasGCnfDigitType_Type.__name__ = "Integer32"
_CcasGCnfDigitType_Object = MibTableColumn
ccasGCnfDigitType = _CcasGCnfDigitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 29),
    _CcasGCnfDigitType_Type()
)
ccasGCnfDigitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfDigitType.setStatus("current")


class _CcasGCnfEndPointDirectional_Type(Integer32):
    """Custom type ccasGCnfEndPointDirectional based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("incoming", 2),
          ("outgoing", 3))
    )


_CcasGCnfEndPointDirectional_Type.__name__ = "Integer32"
_CcasGCnfEndPointDirectional_Object = MibTableColumn
ccasGCnfEndPointDirectional = _CcasGCnfEndPointDirectional_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 30),
    _CcasGCnfEndPointDirectional_Type()
)
ccasGCnfEndPointDirectional.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfEndPointDirectional.setStatus("current")


class _CcasGCnfPulseReceiveTimeout_Type(Unsigned32):
    """Custom type ccasGCnfPulseReceiveTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcasGCnfPulseReceiveTimeout_Type.__name__ = "Unsigned32"
_CcasGCnfPulseReceiveTimeout_Object = MibTableColumn
ccasGCnfPulseReceiveTimeout = _CcasGCnfPulseReceiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 31),
    _CcasGCnfPulseReceiveTimeout_Type()
)
ccasGCnfPulseReceiveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfPulseReceiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfPulseReceiveTimeout.setUnits("seconds")


class _CcasGCnfInitialDelay_Type(Unsigned32):
    """Custom type ccasGCnfInitialDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CcasGCnfInitialDelay_Type.__name__ = "Unsigned32"
_CcasGCnfInitialDelay_Object = MibTableColumn
ccasGCnfInitialDelay = _CcasGCnfInitialDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 32),
    _CcasGCnfInitialDelay_Type()
)
ccasGCnfInitialDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfInitialDelay.setStatus("current")
if mibBuilder.loadTexts:
    ccasGCnfInitialDelay.setUnits("milliseconds")


class _CcasGCnfMaxNumCallParty_Type(Unsigned32):
    """Custom type ccasGCnfMaxNumCallParty based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcasGCnfMaxNumCallParty_Type.__name__ = "Unsigned32"
_CcasGCnfMaxNumCallParty_Object = MibTableColumn
ccasGCnfMaxNumCallParty = _CcasGCnfMaxNumCallParty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 33),
    _CcasGCnfMaxNumCallParty_Type()
)
ccasGCnfMaxNumCallParty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfMaxNumCallParty.setStatus("current")
_CcasGCnfRowStatus_Type = RowStatus
_CcasGCnfRowStatus_Object = MibTableColumn
ccasGCnfRowStatus = _CcasGCnfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 1, 6, 1, 1, 34),
    _CcasGCnfRowStatus_Type()
)
ccasGCnfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccasGCnfRowStatus.setStatus("current")
_CiscoCasIfExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCasIfExtMIBConformance = _CiscoCasIfExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2)
)
_CcasIfExtMIBCompliances_ObjectIdentity = ObjectIdentity
ccasIfExtMIBCompliances = _CcasIfExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 1)
)
_CcasIfExtMIBGroups_ObjectIdentity = ObjectIdentity
ccasIfExtMIBGroups = _CcasIfExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 2)
)
ccasVoiceCfgEntry.registerAugmentions(
    ("CISCO-CAS-IF-EXT-MIB",
     "ccasIfExtVoiceCfgEntry")
)
ccasIfExtVoiceCfgEntry.setIndexNames(*ccasVoiceCfgEntry.getIndexNames())
ccasGrpCfgEntry.registerAugmentions(
    ("CISCO-CAS-IF-EXT-MIB",
     "ccasIfExtDs0GrpCfgEntry")
)
ccasIfExtDs0GrpCfgEntry.setIndexNames(*ccasGrpCfgEntry.getIndexNames())

# Managed Objects groups

ccasIfExtVoiceCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 2, 1)
)
ccasIfExtVoiceCfgGroup.setObjects(
      *(("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgLifNumber"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgCcntrlProfile"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgVadEnabled"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgContinuityTone1"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgContinuityTone2"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgModemPassThru"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgUpspeedCodec"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgT38MaxFaxTxRate"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgT38HsPktPeriod"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgT38HsRedundancy"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgVadTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgICSEnable"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgICSIntTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgTonePlan"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgGwyLinkId"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgH248PkgIds"))
)
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgGroup.setStatus("deprecated")

ccasIfExtBulkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 2, 2)
)
ccasIfExtBulkGroup.setObjects(
      *(("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgRepetition"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgBulkCfgOwner"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgBulkCfgResult"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtDs0GrpRepetition"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtDs0GrpRepeatOwner"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtDs0GrpRepeatResult"))
)
if mibBuilder.loadTexts:
    ccasIfExtBulkGroup.setStatus("current")

ccasIfExtVoiceCfgGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 2, 3)
)
ccasIfExtVoiceCfgGroupRev1.setObjects(
      *(("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgLifNumber"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgCcntrlProfile"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgVadEnabled"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgContinuityTone1"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgContinuityTone2"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgModemPassThru"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgUpspeedCodec"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgVadTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgICSEnable"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgICSIntTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgTonePlan"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgGwyLinkId"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgH248PkgIds"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgEventMappingIdx"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgGatewayIndex"))
)
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgGroupRev1.setStatus("current")

ccasIfExtVoiceCfgCasGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 2, 4)
)
ccasIfExtVoiceCfgCasGroup.setObjects(
      *(("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgCasProfile"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgCasVariant"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgDs0ChannelsFail"))
)
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgCasGroup.setStatus("current")

ccasIfExtProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 2, 5)
)
ccasIfExtProfileGroup.setObjects(
      *(("CISCO-CAS-IF-EXT-MIB", "ccasProfileLineSigTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasProfileRegisterSignal"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasProfileRegSigTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasProfileGeneralCfg"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasProfileRowStatus"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasVariantFile"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasVariantSource"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasVariantNumberCount"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasVariantState"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasVariantRowStatus"))
)
if mibBuilder.loadTexts:
    ccasIfExtProfileGroup.setStatus("current")

ccasIfExtConfigLineSignalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 2, 6)
)
ccasIfExtConfigLineSignalGroup.setObjects(
      *(("CISCO-CAS-IF-EXT-MIB", "ccasILSSignalName"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasILSRxPattern"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasILSMatchedRxPattern"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasILSMatchedTxPattern"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasILSMinMakeTime"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasILSMaxMakeTime"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasILSMinBreakTime"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasILSMaxBreakTime"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasOLSCasSignalName"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasOLSTxPattern"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasOLSMakeTime"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasOLSBreakTime"))
)
if mibBuilder.loadTexts:
    ccasIfExtConfigLineSignalGroup.setStatus("current")

ccasIfExtConfigRegisterSignalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 2, 7)
)
ccasIfExtConfigRegisterSignalGroup.setObjects(
      *(("CISCO-CAS-IF-EXT-MIB", "ccasRSCountry"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSSubRegion"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSNextDigitANI"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSNextDigitDNIS"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSPrevDigit"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSXtoGroupBSignals"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSCongestion"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSCallingPartyCategory"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSAddrCompleteGroupA"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSPrevNminus2Digit"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSPrevNminus3Digit"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSCountryCode"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSLangDiscr"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSNatureOfCircuit"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSInfoEchoSuppressor"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSInternationalCongst"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSXtoGroupC"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSRepeatLastDigit"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSRepeatCalledDigit"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSPlaySITTone"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSSubscriberLineBusy"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSNetworkCongstInGroupB"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSInvalidDialedNumber"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSSubLineFreeWithCharge"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSSubLineFreeWithNoCharge"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSSubLineOutOfOrder"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSAnnouncement"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSXtoGrpASendNextDNIS"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSXtoGrpASendDNISFrmBeg"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSXtoGrpAResendLastDNIS"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSSSendCatSwGrpB"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasBwdRSSGrpCCong"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSANIDigitAvailable"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSANIDigitNotAvailable"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSEndANICallingPartyNotRev"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSEndANICallingPartyRev"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSEndOfDNISDigit"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSNoCategoryAvailble"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSCCEchoSuppressor"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSCCNoEchoSuppressor"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSCCInsertEchoSuppressor"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSIncHalfEchoRequired"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSTestCall"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSSatelLinkIncluded"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSSatelLinkNotIncluded"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSDiscriminatorDigit"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSOtherLanguage"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSOtherLanguage1"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSOtherLanguage2"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSRequestNotAccepted"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSSubWithoutPriorNational"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSSubPriorNational"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSSubPriorInternational"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSMaintenanceEquipment"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSOperatorCall"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSDataTransNational"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSDataTransInternational"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSOperNoFwdTransFacility"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSOperFwdTransFacility"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSSubsrcWithMeter"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasFwdRSSubsrcWithIDD"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSInterpreFirstANIDigit"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSGetValueFromValidIndex"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSSeqInfCollect"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSSendFirstFwdSig"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSRowStatus"))
)
if mibBuilder.loadTexts:
    ccasIfExtConfigRegisterSignalGroup.setStatus("current")

ccasIfExtConfigTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 2, 8)
)
ccasIfExtConfigTimerGroup.setObjects(
      *(("CISCO-CAS-IF-EXT-MIB", "ccasLSTIdleGuardTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasLSTClearFwdTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasLSTClearBwdTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasLSTReleaseGuardTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasLSTCASGlareTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasLSTAnswerMeterDelayTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasLSTCASDebounceTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasLSTSeizeAckRspTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasLSTDelayBetRegAnsAndLineAns"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasLSTSeizeAckToDigitTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasLSTRowStatus"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTAnswerSigTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTCompelledFwdToneOnTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTCompelledFwdToneOffTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTCompelledBwdToneOnTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTOutFwdPulseOnTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTOutFwdPulseOffTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTIncFwdPulseOnTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTBwdPulseOnTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTIncomingRegSigDuration"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTOutgoingRegSigDuration"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTCalledPartyInterDigTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasRSTRowStatus"))
)
if mibBuilder.loadTexts:
    ccasIfExtConfigTimerGroup.setStatus("current")

ccasIfExtGeneralConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 2, 9)
)
ccasIfExtGeneralConfigGroup.setObjects(
      *(("CISCO-CAS-IF-EXT-MIB", "ccasGCnfGlarePolicy"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfParmSource"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfRegSigMode"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfLineSigType"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfRingBackType"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfIncCallHiFreqPower"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfIncCallLoFreqPower"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfIncCallNegTwist"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfIncCallPosTwist"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfIncCallBreakThreshold"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfOutCallLoFreqPower"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfOutCallPowerTwist"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfOutCadenceOntime"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfOutCadenceOfftime"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfCountryCode"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfEchoCancellation"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfSubscriberCategory"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfNatureOfCircuit"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfCompelledSignalingType"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfTxDigitOrder"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfDigitDetectMode"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfMeteringRepIntThresh"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfStartTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfLongTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfShortTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfLongDurationTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfMGCTimer"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfDigitType"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfEndPointDirectional"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfPulseReceiveTimeout"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfInitialDelay"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfMaxNumCallParty"),
        ("CISCO-CAS-IF-EXT-MIB", "ccasGCnfRowStatus"))
)
if mibBuilder.loadTexts:
    ccasIfExtGeneralConfigGroup.setStatus("current")

ccasIfExtVoiceCfgGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 2, 10)
)
ccasIfExtVoiceCfgGroupSup1.setObjects(
    ("CISCO-CAS-IF-EXT-MIB", "ccasIfExtVoiceCfgNoiseRegType")
)
if mibBuilder.loadTexts:
    ccasIfExtVoiceCfgGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ccasIfExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ccasIfExtMIBCompliance.setStatus(
        "deprecated"
    )

ccasIfExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ccasIfExtMIBComplianceRev1.setStatus(
        "deprecated"
    )

ccasIfExtMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ccasIfExtMIBComplianceRev2.setStatus(
        "deprecated"
    )

ccasIfExtMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 314, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ccasIfExtMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CAS-IF-EXT-MIB",
    **{"CASLineSignal": CASLineSignal,
       "CASRegisterSignal": CASRegisterSignal,
       "CASForwardSignal": CASForwardSignal,
       "CASBackwardSignal": CASBackwardSignal,
       "CASCountryCode": CASCountryCode,
       "ciscoCasIfExtMIB": ciscoCasIfExtMIB,
       "ciscoCasIfExtMIBNotifications": ciscoCasIfExtMIBNotifications,
       "ciscoCasIfExtMIBObjects": ciscoCasIfExtMIBObjects,
       "ccasIfExtConfig": ccasIfExtConfig,
       "ccasIfExtVoiceCfgTable": ccasIfExtVoiceCfgTable,
       "ccasIfExtVoiceCfgEntry": ccasIfExtVoiceCfgEntry,
       "ccasIfExtVoiceCfgLifNumber": ccasIfExtVoiceCfgLifNumber,
       "ccasIfExtVoiceCfgCcntrlProfile": ccasIfExtVoiceCfgCcntrlProfile,
       "ccasIfExtVoiceCfgVadEnabled": ccasIfExtVoiceCfgVadEnabled,
       "ccasIfExtVoiceCfgContinuityTone1": ccasIfExtVoiceCfgContinuityTone1,
       "ccasIfExtVoiceCfgContinuityTone2": ccasIfExtVoiceCfgContinuityTone2,
       "ccasIfExtVoiceCfgModemPassThru": ccasIfExtVoiceCfgModemPassThru,
       "ccasIfExtVoiceCfgUpspeedCodec": ccasIfExtVoiceCfgUpspeedCodec,
       "ccasIfExtVoiceCfgT38MaxFaxTxRate": ccasIfExtVoiceCfgT38MaxFaxTxRate,
       "ccasIfExtVoiceCfgT38HsPktPeriod": ccasIfExtVoiceCfgT38HsPktPeriod,
       "ccasIfExtVoiceCfgT38HsRedundancy": ccasIfExtVoiceCfgT38HsRedundancy,
       "ccasIfExtVoiceCfgRepetition": ccasIfExtVoiceCfgRepetition,
       "ccasIfExtVoiceCfgBulkCfgOwner": ccasIfExtVoiceCfgBulkCfgOwner,
       "ccasIfExtVoiceCfgBulkCfgResult": ccasIfExtVoiceCfgBulkCfgResult,
       "ccasIfExtVoiceCfgVadTimer": ccasIfExtVoiceCfgVadTimer,
       "ccasIfExtVoiceCfgICSEnable": ccasIfExtVoiceCfgICSEnable,
       "ccasIfExtVoiceCfgICSIntTimer": ccasIfExtVoiceCfgICSIntTimer,
       "ccasIfExtVoiceCfgTonePlan": ccasIfExtVoiceCfgTonePlan,
       "ccasIfExtVoiceCfgGwyLinkId": ccasIfExtVoiceCfgGwyLinkId,
       "ccasIfExtVoiceCfgH248PkgIds": ccasIfExtVoiceCfgH248PkgIds,
       "ccasIfExtVoiceCfgEventMappingIdx": ccasIfExtVoiceCfgEventMappingIdx,
       "ccasIfExtVoiceCfgGatewayIndex": ccasIfExtVoiceCfgGatewayIndex,
       "ccasIfExtVoiceCfgCasProfile": ccasIfExtVoiceCfgCasProfile,
       "ccasIfExtVoiceCfgCasVariant": ccasIfExtVoiceCfgCasVariant,
       "ccasIfExtVoiceCfgDs0ChannelsFail": ccasIfExtVoiceCfgDs0ChannelsFail,
       "ccasIfExtVoiceCfgNoiseRegType": ccasIfExtVoiceCfgNoiseRegType,
       "ccasIfExtDs0GrpCfgTable": ccasIfExtDs0GrpCfgTable,
       "ccasIfExtDs0GrpCfgEntry": ccasIfExtDs0GrpCfgEntry,
       "ccasIfExtDs0GrpRepetition": ccasIfExtDs0GrpRepetition,
       "ccasIfExtDs0GrpRepeatOwner": ccasIfExtDs0GrpRepeatOwner,
       "ccasIfExtDs0GrpRepeatResult": ccasIfExtDs0GrpRepeatResult,
       "ccasIfExtProfile": ccasIfExtProfile,
       "ccasIfExtProfileTable": ccasIfExtProfileTable,
       "ccasIfExtProfileEntry": ccasIfExtProfileEntry,
       "ccasProfileIndex": ccasProfileIndex,
       "ccasProfileLineSigTimer": ccasProfileLineSigTimer,
       "ccasProfileRegisterSignal": ccasProfileRegisterSignal,
       "ccasProfileRegSigTimer": ccasProfileRegSigTimer,
       "ccasProfileGeneralCfg": ccasProfileGeneralCfg,
       "ccasProfileRowStatus": ccasProfileRowStatus,
       "ccasIfExtVariantTable": ccasIfExtVariantTable,
       "ccasIfExtVariantEntry": ccasIfExtVariantEntry,
       "ccasVariantIndex": ccasVariantIndex,
       "ccasVariantFile": ccasVariantFile,
       "ccasVariantSource": ccasVariantSource,
       "ccasVariantNumberCount": ccasVariantNumberCount,
       "ccasVariantState": ccasVariantState,
       "ccasVariantRowStatus": ccasVariantRowStatus,
       "ccasIfExtConfigLineSignal": ccasIfExtConfigLineSignal,
       "ccasIfExtIncomingLineSignalTable": ccasIfExtIncomingLineSignalTable,
       "ccasIfExtIncomingLineSignalEntry": ccasIfExtIncomingLineSignalEntry,
       "ccasILSSignalNameIndex": ccasILSSignalNameIndex,
       "ccasILSSignalName": ccasILSSignalName,
       "ccasILSRxPattern": ccasILSRxPattern,
       "ccasILSMatchedRxPattern": ccasILSMatchedRxPattern,
       "ccasILSMatchedTxPattern": ccasILSMatchedTxPattern,
       "ccasILSMinMakeTime": ccasILSMinMakeTime,
       "ccasILSMaxMakeTime": ccasILSMaxMakeTime,
       "ccasILSMinBreakTime": ccasILSMinBreakTime,
       "ccasILSMaxBreakTime": ccasILSMaxBreakTime,
       "ccasIfExtOutgoingLineSignalTable": ccasIfExtOutgoingLineSignalTable,
       "ccasIfExtOutgoingLineSignalEntry": ccasIfExtOutgoingLineSignalEntry,
       "ccasOLSSignalNameIndex": ccasOLSSignalNameIndex,
       "ccasOLSCasSignalName": ccasOLSCasSignalName,
       "ccasOLSTxPattern": ccasOLSTxPattern,
       "ccasOLSMakeTime": ccasOLSMakeTime,
       "ccasOLSBreakTime": ccasOLSBreakTime,
       "ccasIfExtLineSignalTimerTable": ccasIfExtLineSignalTimerTable,
       "ccasIfExtLineSignalTimerEntry": ccasIfExtLineSignalTimerEntry,
       "ccasLSTIndex": ccasLSTIndex,
       "ccasLSTIdleGuardTimer": ccasLSTIdleGuardTimer,
       "ccasLSTClearFwdTimer": ccasLSTClearFwdTimer,
       "ccasLSTClearBwdTimer": ccasLSTClearBwdTimer,
       "ccasLSTReleaseGuardTimer": ccasLSTReleaseGuardTimer,
       "ccasLSTCASGlareTimer": ccasLSTCASGlareTimer,
       "ccasLSTAnswerMeterDelayTimer": ccasLSTAnswerMeterDelayTimer,
       "ccasLSTCASDebounceTimer": ccasLSTCASDebounceTimer,
       "ccasLSTSeizeAckRspTimer": ccasLSTSeizeAckRspTimer,
       "ccasLSTDelayBetRegAnsAndLineAns": ccasLSTDelayBetRegAnsAndLineAns,
       "ccasLSTSeizeAckToDigitTimer": ccasLSTSeizeAckToDigitTimer,
       "ccasLSTRowStatus": ccasLSTRowStatus,
       "ccasIfExtConfigRegisterSignal": ccasIfExtConfigRegisterSignal,
       "ccasIfExtRegisterSignalTable": ccasIfExtRegisterSignalTable,
       "ccasIfExtRegisterSignalEntry": ccasIfExtRegisterSignalEntry,
       "ccasRSIndex": ccasRSIndex,
       "ccasRSCountry": ccasRSCountry,
       "ccasRSSubRegion": ccasRSSubRegion,
       "ccasBwdRSNextDigitANI": ccasBwdRSNextDigitANI,
       "ccasBwdRSNextDigitDNIS": ccasBwdRSNextDigitDNIS,
       "ccasBwdRSPrevDigit": ccasBwdRSPrevDigit,
       "ccasBwdRSXtoGroupBSignals": ccasBwdRSXtoGroupBSignals,
       "ccasBwdRSCongestion": ccasBwdRSCongestion,
       "ccasBwdRSCallingPartyCategory": ccasBwdRSCallingPartyCategory,
       "ccasBwdRSAddrCompleteGroupA": ccasBwdRSAddrCompleteGroupA,
       "ccasBwdRSPrevNminus2Digit": ccasBwdRSPrevNminus2Digit,
       "ccasBwdRSPrevNminus3Digit": ccasBwdRSPrevNminus3Digit,
       "ccasBwdRSCountryCode": ccasBwdRSCountryCode,
       "ccasBwdRSLangDiscr": ccasBwdRSLangDiscr,
       "ccasBwdRSNatureOfCircuit": ccasBwdRSNatureOfCircuit,
       "ccasBwdRSInfoEchoSuppressor": ccasBwdRSInfoEchoSuppressor,
       "ccasBwdRSInternationalCongst": ccasBwdRSInternationalCongst,
       "ccasBwdRSXtoGroupC": ccasBwdRSXtoGroupC,
       "ccasBwdRSRepeatLastDigit": ccasBwdRSRepeatLastDigit,
       "ccasBwdRSRepeatCalledDigit": ccasBwdRSRepeatCalledDigit,
       "ccasBwdRSPlaySITTone": ccasBwdRSPlaySITTone,
       "ccasBwdRSSubscriberLineBusy": ccasBwdRSSubscriberLineBusy,
       "ccasBwdRSNetworkCongstInGroupB": ccasBwdRSNetworkCongstInGroupB,
       "ccasBwdRSInvalidDialedNumber": ccasBwdRSInvalidDialedNumber,
       "ccasBwdRSSubLineFreeWithCharge": ccasBwdRSSubLineFreeWithCharge,
       "ccasBwdRSSubLineFreeWithNoCharge": ccasBwdRSSubLineFreeWithNoCharge,
       "ccasBwdRSSubLineOutOfOrder": ccasBwdRSSubLineOutOfOrder,
       "ccasBwdRSAnnouncement": ccasBwdRSAnnouncement,
       "ccasBwdRSXtoGrpASendNextDNIS": ccasBwdRSXtoGrpASendNextDNIS,
       "ccasBwdRSXtoGrpASendDNISFrmBeg": ccasBwdRSXtoGrpASendDNISFrmBeg,
       "ccasBwdRSXtoGrpAResendLastDNIS": ccasBwdRSXtoGrpAResendLastDNIS,
       "ccasBwdRSSSendCatSwGrpB": ccasBwdRSSSendCatSwGrpB,
       "ccasBwdRSSGrpCCong": ccasBwdRSSGrpCCong,
       "ccasFwdRSANIDigitAvailable": ccasFwdRSANIDigitAvailable,
       "ccasFwdRSANIDigitNotAvailable": ccasFwdRSANIDigitNotAvailable,
       "ccasFwdRSEndANICallingPartyNotRev": ccasFwdRSEndANICallingPartyNotRev,
       "ccasFwdRSEndANICallingPartyRev": ccasFwdRSEndANICallingPartyRev,
       "ccasFwdRSEndOfDNISDigit": ccasFwdRSEndOfDNISDigit,
       "ccasFwdRSNoCategoryAvailble": ccasFwdRSNoCategoryAvailble,
       "ccasFwdRSCCEchoSuppressor": ccasFwdRSCCEchoSuppressor,
       "ccasFwdRSCCNoEchoSuppressor": ccasFwdRSCCNoEchoSuppressor,
       "ccasFwdRSCCInsertEchoSuppressor": ccasFwdRSCCInsertEchoSuppressor,
       "ccasFwdRSIncHalfEchoRequired": ccasFwdRSIncHalfEchoRequired,
       "ccasFwdRSTestCall": ccasFwdRSTestCall,
       "ccasFwdRSSatelLinkIncluded": ccasFwdRSSatelLinkIncluded,
       "ccasFwdRSSatelLinkNotIncluded": ccasFwdRSSatelLinkNotIncluded,
       "ccasFwdRSDiscriminatorDigit": ccasFwdRSDiscriminatorDigit,
       "ccasFwdRSOtherLanguage": ccasFwdRSOtherLanguage,
       "ccasFwdRSOtherLanguage1": ccasFwdRSOtherLanguage1,
       "ccasFwdRSOtherLanguage2": ccasFwdRSOtherLanguage2,
       "ccasFwdRSRequestNotAccepted": ccasFwdRSRequestNotAccepted,
       "ccasFwdRSSubWithoutPriorNational": ccasFwdRSSubWithoutPriorNational,
       "ccasFwdRSSubPriorNational": ccasFwdRSSubPriorNational,
       "ccasFwdRSSubPriorInternational": ccasFwdRSSubPriorInternational,
       "ccasFwdRSMaintenanceEquipment": ccasFwdRSMaintenanceEquipment,
       "ccasFwdRSOperatorCall": ccasFwdRSOperatorCall,
       "ccasFwdRSDataTransNational": ccasFwdRSDataTransNational,
       "ccasFwdRSDataTransInternational": ccasFwdRSDataTransInternational,
       "ccasFwdRSOperNoFwdTransFacility": ccasFwdRSOperNoFwdTransFacility,
       "ccasFwdRSOperFwdTransFacility": ccasFwdRSOperFwdTransFacility,
       "ccasFwdRSSubsrcWithMeter": ccasFwdRSSubsrcWithMeter,
       "ccasFwdRSSubsrcWithIDD": ccasFwdRSSubsrcWithIDD,
       "ccasRSInterpreFirstANIDigit": ccasRSInterpreFirstANIDigit,
       "ccasRSGetValueFromValidIndex": ccasRSGetValueFromValidIndex,
       "ccasRSSeqInfCollect": ccasRSSeqInfCollect,
       "ccasRSSendFirstFwdSig": ccasRSSendFirstFwdSig,
       "ccasRSRowStatus": ccasRSRowStatus,
       "ccasIfExtConfigTimer": ccasIfExtConfigTimer,
       "ccasIfExtRegSignalTimerTable": ccasIfExtRegSignalTimerTable,
       "ccasIfExtRegSignalTimerEntry": ccasIfExtRegSignalTimerEntry,
       "ccasRSTIndex": ccasRSTIndex,
       "ccasRSTAnswerSigTimer": ccasRSTAnswerSigTimer,
       "ccasRSTCompelledFwdToneOnTimer": ccasRSTCompelledFwdToneOnTimer,
       "ccasRSTCompelledFwdToneOffTimer": ccasRSTCompelledFwdToneOffTimer,
       "ccasRSTCompelledBwdToneOnTimer": ccasRSTCompelledBwdToneOnTimer,
       "ccasRSTOutFwdPulseOnTimer": ccasRSTOutFwdPulseOnTimer,
       "ccasRSTOutFwdPulseOffTimer": ccasRSTOutFwdPulseOffTimer,
       "ccasRSTIncFwdPulseOnTimer": ccasRSTIncFwdPulseOnTimer,
       "ccasRSTBwdPulseOnTimer": ccasRSTBwdPulseOnTimer,
       "ccasRSTIncomingRegSigDuration": ccasRSTIncomingRegSigDuration,
       "ccasRSTOutgoingRegSigDuration": ccasRSTOutgoingRegSigDuration,
       "ccasRSTCalledPartyInterDigTimer": ccasRSTCalledPartyInterDigTimer,
       "ccasRSTRowStatus": ccasRSTRowStatus,
       "ccasIfExtGeneralConfig": ccasIfExtGeneralConfig,
       "ccasIfExtGeneralConfigTable": ccasIfExtGeneralConfigTable,
       "ccasIfExtGeneralConfigEntry": ccasIfExtGeneralConfigEntry,
       "ccasGCnfIndex": ccasGCnfIndex,
       "ccasGCnfGlarePolicy": ccasGCnfGlarePolicy,
       "ccasGCnfParmSource": ccasGCnfParmSource,
       "ccasGCnfRegSigMode": ccasGCnfRegSigMode,
       "ccasGCnfLineSigType": ccasGCnfLineSigType,
       "ccasGCnfRingBackType": ccasGCnfRingBackType,
       "ccasGCnfIncCallHiFreqPower": ccasGCnfIncCallHiFreqPower,
       "ccasGCnfIncCallLoFreqPower": ccasGCnfIncCallLoFreqPower,
       "ccasGCnfIncCallNegTwist": ccasGCnfIncCallNegTwist,
       "ccasGCnfIncCallPosTwist": ccasGCnfIncCallPosTwist,
       "ccasGCnfIncCallBreakThreshold": ccasGCnfIncCallBreakThreshold,
       "ccasGCnfOutCallLoFreqPower": ccasGCnfOutCallLoFreqPower,
       "ccasGCnfOutCallPowerTwist": ccasGCnfOutCallPowerTwist,
       "ccasGCnfOutCadenceOntime": ccasGCnfOutCadenceOntime,
       "ccasGCnfOutCadenceOfftime": ccasGCnfOutCadenceOfftime,
       "ccasGCnfCountryCode": ccasGCnfCountryCode,
       "ccasGCnfEchoCancellation": ccasGCnfEchoCancellation,
       "ccasGCnfSubscriberCategory": ccasGCnfSubscriberCategory,
       "ccasGCnfNatureOfCircuit": ccasGCnfNatureOfCircuit,
       "ccasGCnfCompelledSignalingType": ccasGCnfCompelledSignalingType,
       "ccasGCnfTxDigitOrder": ccasGCnfTxDigitOrder,
       "ccasGCnfDigitDetectMode": ccasGCnfDigitDetectMode,
       "ccasGCnfMeteringRepIntThresh": ccasGCnfMeteringRepIntThresh,
       "ccasGCnfStartTimer": ccasGCnfStartTimer,
       "ccasGCnfLongTimer": ccasGCnfLongTimer,
       "ccasGCnfShortTimer": ccasGCnfShortTimer,
       "ccasGCnfLongDurationTimer": ccasGCnfLongDurationTimer,
       "ccasGCnfMGCTimer": ccasGCnfMGCTimer,
       "ccasGCnfDigitType": ccasGCnfDigitType,
       "ccasGCnfEndPointDirectional": ccasGCnfEndPointDirectional,
       "ccasGCnfPulseReceiveTimeout": ccasGCnfPulseReceiveTimeout,
       "ccasGCnfInitialDelay": ccasGCnfInitialDelay,
       "ccasGCnfMaxNumCallParty": ccasGCnfMaxNumCallParty,
       "ccasGCnfRowStatus": ccasGCnfRowStatus,
       "ciscoCasIfExtMIBConformance": ciscoCasIfExtMIBConformance,
       "ccasIfExtMIBCompliances": ccasIfExtMIBCompliances,
       "ccasIfExtMIBCompliance": ccasIfExtMIBCompliance,
       "ccasIfExtMIBComplianceRev1": ccasIfExtMIBComplianceRev1,
       "ccasIfExtMIBComplianceRev2": ccasIfExtMIBComplianceRev2,
       "ccasIfExtMIBComplianceRev3": ccasIfExtMIBComplianceRev3,
       "ccasIfExtMIBGroups": ccasIfExtMIBGroups,
       "ccasIfExtVoiceCfgGroup": ccasIfExtVoiceCfgGroup,
       "ccasIfExtBulkGroup": ccasIfExtBulkGroup,
       "ccasIfExtVoiceCfgGroupRev1": ccasIfExtVoiceCfgGroupRev1,
       "ccasIfExtVoiceCfgCasGroup": ccasIfExtVoiceCfgCasGroup,
       "ccasIfExtProfileGroup": ccasIfExtProfileGroup,
       "ccasIfExtConfigLineSignalGroup": ccasIfExtConfigLineSignalGroup,
       "ccasIfExtConfigRegisterSignalGroup": ccasIfExtConfigRegisterSignalGroup,
       "ccasIfExtConfigTimerGroup": ccasIfExtConfigTimerGroup,
       "ccasIfExtGeneralConfigGroup": ccasIfExtGeneralConfigGroup,
       "ccasIfExtVoiceCfgGroupSup1": ccasIfExtVoiceCfgGroupSup1}
)
