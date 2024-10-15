# SNMP MIB module (CISCO-VOICE-COMMON-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:06 2024
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

(cCallHistoryIndex,) = mibBuilder.importSymbols(
    "CISCO-DIAL-CONTROL-MIB",
    "cCallHistoryIndex")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(callActiveIndex,
 callActiveSetupTime) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "callActiveIndex",
    "callActiveSetupTime")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVoiceCommonDialControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 55)
)
ciscoVoiceCommonDialControlMIB.setRevisions(
        ("2010-06-30 00:00",
         "2009-03-18 00:00",
         "2008-07-02 00:00",
         "2007-06-26 00:00",
         "2005-08-16 00:00",
         "2005-03-06 00:00",
         "2003-03-11 00:00",
         "2001-10-06 00:00",
         "2001-09-05 00:00",
         "2000-07-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CvcSpeechCoderRate(Integer32, TextualConvention):
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("aaclc", 29),
          ("aacld", 30),
          ("clearChannel", 18),
          ("g711Alawr64000", 7),
          ("g711ulawr64000", 6),
          ("g722r4800", 25),
          ("g722r5600", 26),
          ("g722r6400", 27),
          ("g723Ar5300", 15),
          ("g723Ar6300", 14),
          ("g723r5300", 10),
          ("g723r6300", 9),
          ("g726r16000", 3),
          ("g726r24000", 4),
          ("g726r32000", 5),
          ("g726r40000", 19),
          ("g728r16000", 8),
          ("g729ABr8000", 13),
          ("g729Ar8000", 2),
          ("g729Br8000", 12),
          ("g729IETFr8000", 16),
          ("g729r8000", 1),
          ("gsmAmrNb", 21),
          ("gsmeEr12200", 17),
          ("gsmr13200", 11),
          ("iLBC", 22),
          ("iLBCr13330", 24),
          ("iLBCr15200", 23),
          ("iSAC", 28),
          ("llcc", 20))
    )



class CvcFaxTransmitRate(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fax12000", 8),
          ("fax14400", 7),
          ("fax2400", 3),
          ("fax4800", 4),
          ("fax7200", 5),
          ("fax9600", 6),
          ("none", 1),
          ("voiceRate", 2))
    )



class CvcCoderTypeRate(Integer32, TextualConvention):
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
              40)
        )
    )
    namedValues = NamedValues(
        *(("aaclc", 39),
          ("aacld", 40),
          ("clearChannel", 27),
          ("fax12000", 7),
          ("fax14400", 6),
          ("fax2400", 2),
          ("fax4800", 3),
          ("fax7200", 4),
          ("fax9600", 5),
          ("g711Alawr64000", 16),
          ("g711ulawr64000", 15),
          ("g722", 31),
          ("g722r4800", 35),
          ("g722r5600", 36),
          ("g722r6400", 37),
          ("g723Ar5300", 24),
          ("g723Ar6300", 23),
          ("g723r5300", 19),
          ("g723r6300", 18),
          ("g726r16000", 12),
          ("g726r24000", 13),
          ("g726r32000", 14),
          ("g726r40000", 28),
          ("g728r16000", 17),
          ("g729ABr8000", 22),
          ("g729Ar8000", 11),
          ("g729Br8000", 21),
          ("g729r8000", 10),
          ("gsmAmrNb", 30),
          ("gsmeEr12200", 26),
          ("gsmr13200", 20),
          ("iLBC", 32),
          ("iLBCr13330", 34),
          ("iLBCr15200", 33),
          ("iSAC", 38),
          ("ietfg729r8000", 25),
          ("llcc", 29),
          ("other", 1))
    )



class CvcGUid(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class CvcInBandSignaling(Integer32, TextualConvention):
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
        *(("cas", 1),
          ("cept", 3),
          ("gr303", 5),
          ("none", 2),
          ("transparent", 4))
    )



class CvcCallReferenceIdOrZero(Unsigned32, TextualConvention):
    status = "current"


class CvcH320CallType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2))
    )



class CvcVideoCoderRate(Integer32, TextualConvention):
    status = "current"
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
        *(("h261", 1),
          ("h263", 2),
          ("h263plus", 3),
          ("h264", 4),
          ("none", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CvCommonDcMIBObjects_ObjectIdentity = ObjectIdentity
cvCommonDcMIBObjects = _CvCommonDcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1)
)
_CvCommonDcCallActive_ObjectIdentity = ObjectIdentity
cvCommonDcCallActive = _CvCommonDcCallActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1)
)
_CvCommonDcCallActiveTable_Object = MibTable
cvCommonDcCallActiveTable = _CvCommonDcCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvCommonDcCallActiveTable.setStatus("current")
_CvCommonDcCallActiveEntry_Object = MibTableRow
cvCommonDcCallActiveEntry = _CvCommonDcCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1)
)
cvCommonDcCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cvCommonDcCallActiveEntry.setStatus("current")
_CvCommonDcCallActiveConnectionId_Type = CvcGUid
_CvCommonDcCallActiveConnectionId_Object = MibTableColumn
cvCommonDcCallActiveConnectionId = _CvCommonDcCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 1),
    _CvCommonDcCallActiveConnectionId_Type()
)
cvCommonDcCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallActiveConnectionId.setStatus("current")
_CvCommonDcCallActiveVADEnable_Type = TruthValue
_CvCommonDcCallActiveVADEnable_Object = MibTableColumn
cvCommonDcCallActiveVADEnable = _CvCommonDcCallActiveVADEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 2),
    _CvCommonDcCallActiveVADEnable_Type()
)
cvCommonDcCallActiveVADEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallActiveVADEnable.setStatus("current")
_CvCommonDcCallActiveCoderTypeRate_Type = CvcCoderTypeRate
_CvCommonDcCallActiveCoderTypeRate_Object = MibTableColumn
cvCommonDcCallActiveCoderTypeRate = _CvCommonDcCallActiveCoderTypeRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 3),
    _CvCommonDcCallActiveCoderTypeRate_Type()
)
cvCommonDcCallActiveCoderTypeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallActiveCoderTypeRate.setStatus("current")


class _CvCommonDcCallActiveCodecBytes_Type(Integer32):
    """Custom type cvCommonDcCallActiveCodecBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_CvCommonDcCallActiveCodecBytes_Type.__name__ = "Integer32"
_CvCommonDcCallActiveCodecBytes_Object = MibTableColumn
cvCommonDcCallActiveCodecBytes = _CvCommonDcCallActiveCodecBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 4),
    _CvCommonDcCallActiveCodecBytes_Type()
)
cvCommonDcCallActiveCodecBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallActiveCodecBytes.setStatus("current")
_CvCommonDcCallActiveInBandSignaling_Type = CvcInBandSignaling
_CvCommonDcCallActiveInBandSignaling_Object = MibTableColumn
cvCommonDcCallActiveInBandSignaling = _CvCommonDcCallActiveInBandSignaling_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 5),
    _CvCommonDcCallActiveInBandSignaling_Type()
)
cvCommonDcCallActiveInBandSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallActiveInBandSignaling.setStatus("current")


class _CvCommonDcCallActiveCallingName_Type(SnmpAdminString):
    """Custom type cvCommonDcCallActiveCallingName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CvCommonDcCallActiveCallingName_Type.__name__ = "SnmpAdminString"
_CvCommonDcCallActiveCallingName_Object = MibTableColumn
cvCommonDcCallActiveCallingName = _CvCommonDcCallActiveCallingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 6),
    _CvCommonDcCallActiveCallingName_Type()
)
cvCommonDcCallActiveCallingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallActiveCallingName.setStatus("current")
_CvCommonDcCallActiveCallerIDBlock_Type = TruthValue
_CvCommonDcCallActiveCallerIDBlock_Object = MibTableColumn
cvCommonDcCallActiveCallerIDBlock = _CvCommonDcCallActiveCallerIDBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 7),
    _CvCommonDcCallActiveCallerIDBlock_Type()
)
cvCommonDcCallActiveCallerIDBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallActiveCallerIDBlock.setStatus("current")
_CvCommonDcCallHistory_ObjectIdentity = ObjectIdentity
cvCommonDcCallHistory = _CvCommonDcCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2)
)
_CvCommonDcCallHistoryTable_Object = MibTable
cvCommonDcCallHistoryTable = _CvCommonDcCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvCommonDcCallHistoryTable.setStatus("current")
_CvCommonDcCallHistoryEntry_Object = MibTableRow
cvCommonDcCallHistoryEntry = _CvCommonDcCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1)
)
cvCommonDcCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cvCommonDcCallHistoryEntry.setStatus("current")
_CvCommonDcCallHistoryConnectionId_Type = CvcGUid
_CvCommonDcCallHistoryConnectionId_Object = MibTableColumn
cvCommonDcCallHistoryConnectionId = _CvCommonDcCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 1),
    _CvCommonDcCallHistoryConnectionId_Type()
)
cvCommonDcCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallHistoryConnectionId.setStatus("current")
_CvCommonDcCallHistoryVADEnable_Type = TruthValue
_CvCommonDcCallHistoryVADEnable_Object = MibTableColumn
cvCommonDcCallHistoryVADEnable = _CvCommonDcCallHistoryVADEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 2),
    _CvCommonDcCallHistoryVADEnable_Type()
)
cvCommonDcCallHistoryVADEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallHistoryVADEnable.setStatus("current")
_CvCommonDcCallHistoryCoderTypeRate_Type = CvcCoderTypeRate
_CvCommonDcCallHistoryCoderTypeRate_Object = MibTableColumn
cvCommonDcCallHistoryCoderTypeRate = _CvCommonDcCallHistoryCoderTypeRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 3),
    _CvCommonDcCallHistoryCoderTypeRate_Type()
)
cvCommonDcCallHistoryCoderTypeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallHistoryCoderTypeRate.setStatus("current")


class _CvCommonDcCallHistoryCodecBytes_Type(Integer32):
    """Custom type cvCommonDcCallHistoryCodecBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_CvCommonDcCallHistoryCodecBytes_Type.__name__ = "Integer32"
_CvCommonDcCallHistoryCodecBytes_Object = MibTableColumn
cvCommonDcCallHistoryCodecBytes = _CvCommonDcCallHistoryCodecBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 4),
    _CvCommonDcCallHistoryCodecBytes_Type()
)
cvCommonDcCallHistoryCodecBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallHistoryCodecBytes.setStatus("current")
_CvCommonDcCallHistoryInBandSignaling_Type = CvcInBandSignaling
_CvCommonDcCallHistoryInBandSignaling_Object = MibTableColumn
cvCommonDcCallHistoryInBandSignaling = _CvCommonDcCallHistoryInBandSignaling_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 5),
    _CvCommonDcCallHistoryInBandSignaling_Type()
)
cvCommonDcCallHistoryInBandSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallHistoryInBandSignaling.setStatus("current")


class _CvCommonDcCallHistoryCallingName_Type(SnmpAdminString):
    """Custom type cvCommonDcCallHistoryCallingName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CvCommonDcCallHistoryCallingName_Type.__name__ = "SnmpAdminString"
_CvCommonDcCallHistoryCallingName_Object = MibTableColumn
cvCommonDcCallHistoryCallingName = _CvCommonDcCallHistoryCallingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 6),
    _CvCommonDcCallHistoryCallingName_Type()
)
cvCommonDcCallHistoryCallingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallHistoryCallingName.setStatus("current")
_CvCommonDcCallHistoryCallerIDBlock_Type = TruthValue
_CvCommonDcCallHistoryCallerIDBlock_Object = MibTableColumn
cvCommonDcCallHistoryCallerIDBlock = _CvCommonDcCallHistoryCallerIDBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 7),
    _CvCommonDcCallHistoryCallerIDBlock_Type()
)
cvCommonDcCallHistoryCallerIDBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvCommonDcCallHistoryCallerIDBlock.setStatus("current")
_CvCommonDcMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cvCommonDcMIBNotificationPrefix = _CvCommonDcMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 2)
)
_CvCommonDcMIBNotifications_ObjectIdentity = ObjectIdentity
cvCommonDcMIBNotifications = _CvCommonDcMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 2, 0)
)
_CvCommonDcMIBConformance_ObjectIdentity = ObjectIdentity
cvCommonDcMIBConformance = _CvCommonDcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 3)
)
_CvCommonDcMIBCompliances_ObjectIdentity = ObjectIdentity
cvCommonDcMIBCompliances = _CvCommonDcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 1)
)
_CvCommonDcMIBGroups_ObjectIdentity = ObjectIdentity
cvCommonDcMIBGroups = _CvCommonDcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 2)
)

# Managed Objects groups

cvCommonDcCallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 2, 1)
)
cvCommonDcCallGroup.setObjects(
      *(("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveConnectionId"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveVADEnable"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCoderTypeRate"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCodecBytes"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveInBandSignaling"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryConnectionId"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryVADEnable"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCoderTypeRate"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCodecBytes"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryInBandSignaling"))
)
if mibBuilder.loadTexts:
    cvCommonDcCallGroup.setStatus("deprecated")

cvCommonDcCallGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 2, 2)
)
cvCommonDcCallGroup1.setObjects(
      *(("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveConnectionId"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveVADEnable"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCoderTypeRate"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCodecBytes"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveInBandSignaling"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCallingName"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCallerIDBlock"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryConnectionId"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryVADEnable"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCoderTypeRate"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCodecBytes"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryInBandSignaling"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCallingName"),
        ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCallerIDBlock"))
)
if mibBuilder.loadTexts:
    cvCommonDcCallGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvCommonDcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cvCommonDcMIBCompliance.setStatus(
        "deprecated"
    )

cvCommonDcMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cvCommonDcMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    **{"CvcSpeechCoderRate": CvcSpeechCoderRate,
       "CvcFaxTransmitRate": CvcFaxTransmitRate,
       "CvcCoderTypeRate": CvcCoderTypeRate,
       "CvcGUid": CvcGUid,
       "CvcInBandSignaling": CvcInBandSignaling,
       "CvcCallReferenceIdOrZero": CvcCallReferenceIdOrZero,
       "CvcH320CallType": CvcH320CallType,
       "CvcVideoCoderRate": CvcVideoCoderRate,
       "ciscoVoiceCommonDialControlMIB": ciscoVoiceCommonDialControlMIB,
       "cvCommonDcMIBObjects": cvCommonDcMIBObjects,
       "cvCommonDcCallActive": cvCommonDcCallActive,
       "cvCommonDcCallActiveTable": cvCommonDcCallActiveTable,
       "cvCommonDcCallActiveEntry": cvCommonDcCallActiveEntry,
       "cvCommonDcCallActiveConnectionId": cvCommonDcCallActiveConnectionId,
       "cvCommonDcCallActiveVADEnable": cvCommonDcCallActiveVADEnable,
       "cvCommonDcCallActiveCoderTypeRate": cvCommonDcCallActiveCoderTypeRate,
       "cvCommonDcCallActiveCodecBytes": cvCommonDcCallActiveCodecBytes,
       "cvCommonDcCallActiveInBandSignaling": cvCommonDcCallActiveInBandSignaling,
       "cvCommonDcCallActiveCallingName": cvCommonDcCallActiveCallingName,
       "cvCommonDcCallActiveCallerIDBlock": cvCommonDcCallActiveCallerIDBlock,
       "cvCommonDcCallHistory": cvCommonDcCallHistory,
       "cvCommonDcCallHistoryTable": cvCommonDcCallHistoryTable,
       "cvCommonDcCallHistoryEntry": cvCommonDcCallHistoryEntry,
       "cvCommonDcCallHistoryConnectionId": cvCommonDcCallHistoryConnectionId,
       "cvCommonDcCallHistoryVADEnable": cvCommonDcCallHistoryVADEnable,
       "cvCommonDcCallHistoryCoderTypeRate": cvCommonDcCallHistoryCoderTypeRate,
       "cvCommonDcCallHistoryCodecBytes": cvCommonDcCallHistoryCodecBytes,
       "cvCommonDcCallHistoryInBandSignaling": cvCommonDcCallHistoryInBandSignaling,
       "cvCommonDcCallHistoryCallingName": cvCommonDcCallHistoryCallingName,
       "cvCommonDcCallHistoryCallerIDBlock": cvCommonDcCallHistoryCallerIDBlock,
       "cvCommonDcMIBNotificationPrefix": cvCommonDcMIBNotificationPrefix,
       "cvCommonDcMIBNotifications": cvCommonDcMIBNotifications,
       "cvCommonDcMIBConformance": cvCommonDcMIBConformance,
       "cvCommonDcMIBCompliances": cvCommonDcMIBCompliances,
       "cvCommonDcMIBCompliance": cvCommonDcMIBCompliance,
       "cvCommonDcMIBComplianceRev1": cvCommonDcMIBComplianceRev1,
       "cvCommonDcMIBGroups": cvCommonDcMIBGroups,
       "cvCommonDcCallGroup": cvCommonDcCallGroup,
       "cvCommonDcCallGroup1": cvCommonDcCallGroup1}
)
