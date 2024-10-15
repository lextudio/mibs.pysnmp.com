# SNMP MIB module (CISCO-VOICE-AALX-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-AALX-PROFILE-MIB
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

(CCallControlJitterDelayMode,
 cmgwIndex) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "CCallControlJitterDelayMode",
    "cmgwIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CvcSpeechCoderRate,) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcSpeechCoderRate")

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

ciscoVoiceAalxProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 323)
)
ciscoVoiceAalxProfileMIB.setRevisions(
        ("2005-04-21 00:00",
         "2004-10-15 00:00",
         "2003-07-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoAal2ProfileType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("custom", 2),
          ("itu", 1))
    )



class CiscoAal2ProfileNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7,
              8,
              12,
              100,
              101,
              110,
              200,
              210)
        )
    )
    namedValues = NamedValues(
        *(("profileCustom100", 100),
          ("profileCustom101", 101),
          ("profileCustom110", 110),
          ("profileCustom200", 200),
          ("profileCustom210", 210),
          ("profileITU1", 1),
          ("profileITU12", 12),
          ("profileITU2", 2),
          ("profileITU3", 3),
          ("profileITU7", 7),
          ("profileITU8", 8))
    )



class CiscoCodecPacketPeriod(Integer32, TextualConvention):
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("pktPeriod10000us", 4),
          ("pktPeriod15000us", 5),
          ("pktPeriod20000us", 6),
          ("pktPeriod25000us", 7),
          ("pktPeriod30000us", 8),
          ("pktPeriod35000us", 9),
          ("pktPeriod40000us", 10),
          ("pktPeriod45000us", 11),
          ("pktPeriod50000us", 12),
          ("pktPeriod5000us", 1),
          ("pktPeriod55000us", 13),
          ("pktPeriod5500us", 2),
          ("pktPeriod5785us", 3),
          ("pktPeriod60000us", 14),
          ("pktPeriod65000us", 15),
          ("pktPeriod70000us", 16),
          ("pktPeriod75000us", 17),
          ("pktPeriod80000us", 18),
          ("pktPeriod85000us", 19),
          ("pktPeriod90000us", 20))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVoiceAalxProfileMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVoiceAalxProfileMIBNotifs = _CiscoVoiceAalxProfileMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 0)
)
_CiscoVoiceAalxProfileMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVoiceAalxProfileMIBObjects = _CiscoVoiceAalxProfileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1)
)
_CvapCodecConfig_ObjectIdentity = ObjectIdentity
cvapCodecConfig = _CvapCodecConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1)
)
_CvapCodecTable_Object = MibTable
cvapCodecTable = _CvapCodecTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvapCodecTable.setStatus("current")
_CvapCodecEntry_Object = MibTableRow
cvapCodecEntry = _CvapCodecEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 1, 1)
)
cvapCodecEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecNegotiationAdaptType"),
)
if mibBuilder.loadTexts:
    cvapCodecEntry.setStatus("current")


class _CvapCodecNegotiationAdaptType_Type(Integer32):
    """Custom type cvapCodecNegotiationAdaptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 2),
          ("aal5", 1))
    )


_CvapCodecNegotiationAdaptType_Type.__name__ = "Integer32"
_CvapCodecNegotiationAdaptType_Object = MibTableColumn
cvapCodecNegotiationAdaptType = _CvapCodecNegotiationAdaptType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 1, 1, 1),
    _CvapCodecNegotiationAdaptType_Type()
)
cvapCodecNegotiationAdaptType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvapCodecNegotiationAdaptType.setStatus("current")


class _CvapCodecNegotiationOption_Type(Integer32):
    """Custom type cvapCodecNegotiationOption based on Integer32"""
    defaultValue = 1

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
        *(("lclLcoRcd", 5),
          ("lclRcdLco", 6),
          ("lcoLclRcd", 2),
          ("lcoRcdLcl", 1),
          ("rcdLclLco", 4),
          ("rcdLcoLcl", 3))
    )


_CvapCodecNegotiationOption_Type.__name__ = "Integer32"
_CvapCodecNegotiationOption_Object = MibTableColumn
cvapCodecNegotiationOption = _CvapCodecNegotiationOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 1, 1, 2),
    _CvapCodecNegotiationOption_Type()
)
cvapCodecNegotiationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapCodecNegotiationOption.setStatus("current")
_CvapCodecConfigTable_Object = MibTable
cvapCodecConfigTable = _CvapCodecConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvapCodecConfigTable.setStatus("current")
_CvapCodecConfigEntry_Object = MibTableRow
cvapCodecConfigEntry = _CvapCodecConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1)
)
cvapCodecConfigEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigAdaptType"),
    (0, "CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigType"),
)
if mibBuilder.loadTexts:
    cvapCodecConfigEntry.setStatus("current")


class _CvapCodecConfigAdaptType_Type(Integer32):
    """Custom type cvapCodecConfigAdaptType based on Integer32"""
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
        *(("aal1", 3),
          ("aal2", 4),
          ("aal5", 2),
          ("other", 1))
    )


_CvapCodecConfigAdaptType_Type.__name__ = "Integer32"
_CvapCodecConfigAdaptType_Object = MibTableColumn
cvapCodecConfigAdaptType = _CvapCodecConfigAdaptType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 1),
    _CvapCodecConfigAdaptType_Type()
)
cvapCodecConfigAdaptType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvapCodecConfigAdaptType.setStatus("current")
_CvapCodecConfigType_Type = CvcSpeechCoderRate
_CvapCodecConfigType_Object = MibTableColumn
cvapCodecConfigType = _CvapCodecConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 2),
    _CvapCodecConfigType_Type()
)
cvapCodecConfigType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvapCodecConfigType.setStatus("current")


class _CvapCodecConfigPreference_Type(Unsigned32):
    """Custom type cvapCodecConfigPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CvapCodecConfigPreference_Type.__name__ = "Unsigned32"
_CvapCodecConfigPreference_Object = MibTableColumn
cvapCodecConfigPreference = _CvapCodecConfigPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 3),
    _CvapCodecConfigPreference_Type()
)
cvapCodecConfigPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapCodecConfigPreference.setStatus("current")
_CvapCodecConfigVoicePacketPeriod_Type = CiscoCodecPacketPeriod
_CvapCodecConfigVoicePacketPeriod_Object = MibTableColumn
cvapCodecConfigVoicePacketPeriod = _CvapCodecConfigVoicePacketPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 4),
    _CvapCodecConfigVoicePacketPeriod_Type()
)
cvapCodecConfigVoicePacketPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapCodecConfigVoicePacketPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cvapCodecConfigVoicePacketPeriod.setUnits("microseconds")
_CvapCodecConfigVbdPacketPeriod_Type = CiscoCodecPacketPeriod
_CvapCodecConfigVbdPacketPeriod_Object = MibTableColumn
cvapCodecConfigVbdPacketPeriod = _CvapCodecConfigVbdPacketPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 5),
    _CvapCodecConfigVbdPacketPeriod_Type()
)
cvapCodecConfigVbdPacketPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapCodecConfigVbdPacketPeriod.setStatus("deprecated")
if mibBuilder.loadTexts:
    cvapCodecConfigVbdPacketPeriod.setUnits("microseconds")


class _CvapCodecConfigJitterDelayMode_Type(CCallControlJitterDelayMode):
    """Custom type cvapCodecConfigJitterDelayMode based on CCallControlJitterDelayMode"""


_CvapCodecConfigJitterDelayMode_Object = MibTableColumn
cvapCodecConfigJitterDelayMode = _CvapCodecConfigJitterDelayMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 6),
    _CvapCodecConfigJitterDelayMode_Type()
)
cvapCodecConfigJitterDelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapCodecConfigJitterDelayMode.setStatus("current")


class _CvapCodecConfigJitterMaxDelay_Type(Unsigned32):
    """Custom type cvapCodecConfigJitterMaxDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 500),
    )


_CvapCodecConfigJitterMaxDelay_Type.__name__ = "Unsigned32"
_CvapCodecConfigJitterMaxDelay_Object = MibTableColumn
cvapCodecConfigJitterMaxDelay = _CvapCodecConfigJitterMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 7),
    _CvapCodecConfigJitterMaxDelay_Type()
)
cvapCodecConfigJitterMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapCodecConfigJitterMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvapCodecConfigJitterMaxDelay.setUnits("milliseconds")


class _CvapCodecConfigJitterNomDelay_Type(Unsigned32):
    """Custom type cvapCodecConfigJitterNomDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500),
    )


_CvapCodecConfigJitterNomDelay_Type.__name__ = "Unsigned32"
_CvapCodecConfigJitterNomDelay_Object = MibTableColumn
cvapCodecConfigJitterNomDelay = _CvapCodecConfigJitterNomDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 8),
    _CvapCodecConfigJitterNomDelay_Type()
)
cvapCodecConfigJitterNomDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapCodecConfigJitterNomDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    cvapCodecConfigJitterNomDelay.setUnits("milliseconds")


class _CvapCodecConfigJitterMinDelay_Type(Unsigned32):
    """Custom type cvapCodecConfigJitterMinDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CvapCodecConfigJitterMinDelay_Type.__name__ = "Unsigned32"
_CvapCodecConfigJitterMinDelay_Object = MibTableColumn
cvapCodecConfigJitterMinDelay = _CvapCodecConfigJitterMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 9),
    _CvapCodecConfigJitterMinDelay_Type()
)
cvapCodecConfigJitterMinDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapCodecConfigJitterMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvapCodecConfigJitterMinDelay.setUnits("milliseconds")
_CvapCodecConfigDtmfRelay_Type = TruthValue
_CvapCodecConfigDtmfRelay_Object = MibTableColumn
cvapCodecConfigDtmfRelay = _CvapCodecConfigDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 10),
    _CvapCodecConfigDtmfRelay_Type()
)
cvapCodecConfigDtmfRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapCodecConfigDtmfRelay.setStatus("current")


class _CvapCodecConfigPayloadType_Type(Unsigned32):
    """Custom type cvapCodecConfigPayloadType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CvapCodecConfigPayloadType_Type.__name__ = "Unsigned32"
_CvapCodecConfigPayloadType_Object = MibTableColumn
cvapCodecConfigPayloadType = _CvapCodecConfigPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 11),
    _CvapCodecConfigPayloadType_Type()
)
cvapCodecConfigPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapCodecConfigPayloadType.setStatus("current")


class _CvapCodecConfigNewJtrNomDelay_Type(Unsigned32):
    """Custom type cvapCodecConfigNewJtrNomDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 500),
    )


_CvapCodecConfigNewJtrNomDelay_Type.__name__ = "Unsigned32"
_CvapCodecConfigNewJtrNomDelay_Object = MibTableColumn
cvapCodecConfigNewJtrNomDelay = _CvapCodecConfigNewJtrNomDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 1, 2, 1, 12),
    _CvapCodecConfigNewJtrNomDelay_Type()
)
cvapCodecConfigNewJtrNomDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapCodecConfigNewJtrNomDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvapCodecConfigNewJtrNomDelay.setUnits("milliseconds")
_CvapAal2Config_ObjectIdentity = ObjectIdentity
cvapAal2Config = _CvapAal2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 2)
)
_CvapSvcConfig_ObjectIdentity = ObjectIdentity
cvapSvcConfig = _CvapSvcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3)
)
_CvapSvcConfigTable_Object = MibTable
cvapSvcConfigTable = _CvapSvcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cvapSvcConfigTable.setStatus("current")
_CvapSvcConfigEntry_Object = MibTableRow
cvapSvcConfigEntry = _CvapSvcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1)
)
cvapSvcConfigEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cvapSvcConfigEntry.setStatus("current")


class _CvapSvcAtmQosCellDelay_Type(Integer32):
    """Custom type cvapSvcAtmQosCellDelay based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 20000),
    )


_CvapSvcAtmQosCellDelay_Type.__name__ = "Integer32"
_CvapSvcAtmQosCellDelay_Object = MibTableColumn
cvapSvcAtmQosCellDelay = _CvapSvcAtmQosCellDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 1),
    _CvapSvcAtmQosCellDelay_Type()
)
cvapSvcAtmQosCellDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcAtmQosCellDelay.setStatus("current")
if mibBuilder.loadTexts:
    cvapSvcAtmQosCellDelay.setUnits("microseconds")


class _CvapSvcAtmQosCtd_Type(Integer32):
    """Custom type cvapSvcAtmQosCtd based on Integer32"""
    defaultValue = 150000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20000, 150000),
    )


_CvapSvcAtmQosCtd_Type.__name__ = "Integer32"
_CvapSvcAtmQosCtd_Object = MibTableColumn
cvapSvcAtmQosCtd = _CvapSvcAtmQosCtd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 2),
    _CvapSvcAtmQosCtd_Type()
)
cvapSvcAtmQosCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcAtmQosCtd.setStatus("current")
if mibBuilder.loadTexts:
    cvapSvcAtmQosCtd.setUnits("microseconds")


class _CvapSvcAtmQosClr_Type(Integer32):
    """Custom type cvapSvcAtmQosClr based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_CvapSvcAtmQosClr_Type.__name__ = "Integer32"
_CvapSvcAtmQosClr_Object = MibTableColumn
cvapSvcAtmQosClr = _CvapSvcAtmQosClr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 3),
    _CvapSvcAtmQosClr_Type()
)
cvapSvcAtmQosClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcAtmQosClr.setStatus("current")


class _CvapSvcTrfScalingFactor_Type(Integer32):
    """Custom type cvapSvcTrfScalingFactor based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 200),
    )


_CvapSvcTrfScalingFactor_Type.__name__ = "Integer32"
_CvapSvcTrfScalingFactor_Object = MibTableColumn
cvapSvcTrfScalingFactor = _CvapSvcTrfScalingFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 4),
    _CvapSvcTrfScalingFactor_Type()
)
cvapSvcTrfScalingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcTrfScalingFactor.setStatus("current")


class _CvapSvcAal2CidNumber_Type(Integer32):
    """Custom type cvapSvcAal2CidNumber based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 255),
    )


_CvapSvcAal2CidNumber_Type.__name__ = "Integer32"
_CvapSvcAal2CidNumber_Object = MibTableColumn
cvapSvcAal2CidNumber = _CvapSvcAal2CidNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 5),
    _CvapSvcAal2CidNumber_Type()
)
cvapSvcAal2CidNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcAal2CidNumber.setStatus("current")


class _CvapSvcAggTrafficClipping_Type(TruthValue):
    """Custom type cvapSvcAggTrafficClipping based on TruthValue"""


_CvapSvcAggTrafficClipping_Object = MibTableColumn
cvapSvcAggTrafficClipping = _CvapSvcAggTrafficClipping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 6),
    _CvapSvcAggTrafficClipping_Type()
)
cvapSvcAggTrafficClipping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcAggTrafficClipping.setStatus("current")


class _CvapSvcAggLinkState_Type(Integer32):
    """Custom type cvapSvcAggLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CvapSvcAggLinkState_Type.__name__ = "Integer32"
_CvapSvcAggLinkState_Object = MibTableColumn
cvapSvcAggLinkState = _CvapSvcAggLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 7),
    _CvapSvcAggLinkState_Type()
)
cvapSvcAggLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcAggLinkState.setStatus("current")


class _CvapSvcPartialFillSupported_Type(Integer32):
    """Custom type cvapSvcPartialFillSupported based on Integer32"""
    defaultValue = 47

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_CvapSvcPartialFillSupported_Type.__name__ = "Integer32"
_CvapSvcPartialFillSupported_Object = MibTableColumn
cvapSvcPartialFillSupported = _CvapSvcPartialFillSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 8),
    _CvapSvcPartialFillSupported_Type()
)
cvapSvcPartialFillSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcPartialFillSupported.setStatus("current")


class _CvapSvcMgcpSelectorByteValue_Type(Integer32):
    """Custom type cvapSvcMgcpSelectorByteValue based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CvapSvcMgcpSelectorByteValue_Type.__name__ = "Integer32"
_CvapSvcMgcpSelectorByteValue_Object = MibTableColumn
cvapSvcMgcpSelectorByteValue = _CvapSvcMgcpSelectorByteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 9),
    _CvapSvcMgcpSelectorByteValue_Type()
)
cvapSvcMgcpSelectorByteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcMgcpSelectorByteValue.setStatus("current")


class _CvapSvcH248SelectorByteValue_Type(Integer32):
    """Custom type cvapSvcH248SelectorByteValue based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CvapSvcH248SelectorByteValue_Type.__name__ = "Integer32"
_CvapSvcH248SelectorByteValue_Object = MibTableColumn
cvapSvcH248SelectorByteValue = _CvapSvcH248SelectorByteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 10),
    _CvapSvcH248SelectorByteValue_Type()
)
cvapSvcH248SelectorByteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcH248SelectorByteValue.setStatus("current")


class _CvapSvcDelNotifGuardTimer_Type(Integer32):
    """Custom type cvapSvcDelNotifGuardTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CvapSvcDelNotifGuardTimer_Type.__name__ = "Integer32"
_CvapSvcDelNotifGuardTimer_Object = MibTableColumn
cvapSvcDelNotifGuardTimer = _CvapSvcDelNotifGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 11),
    _CvapSvcDelNotifGuardTimer_Type()
)
cvapSvcDelNotifGuardTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcDelNotifGuardTimer.setStatus("current")
if mibBuilder.loadTexts:
    cvapSvcDelNotifGuardTimer.setUnits("seconds")


class _CvapSvcMultiCIDPerSvc_Type(TruthValue):
    """Custom type cvapSvcMultiCIDPerSvc based on TruthValue"""


_CvapSvcMultiCIDPerSvc_Object = MibTableColumn
cvapSvcMultiCIDPerSvc = _CvapSvcMultiCIDPerSvc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 12),
    _CvapSvcMultiCIDPerSvc_Type()
)
cvapSvcMultiCIDPerSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDPerSvc.setStatus("current")


class _CvapSvcMultiCIDFillTimer_Type(Unsigned32):
    """Custom type cvapSvcMultiCIDFillTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CvapSvcMultiCIDFillTimer_Type.__name__ = "Unsigned32"
_CvapSvcMultiCIDFillTimer_Object = MibTableColumn
cvapSvcMultiCIDFillTimer = _CvapSvcMultiCIDFillTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 13),
    _CvapSvcMultiCIDFillTimer_Type()
)
cvapSvcMultiCIDFillTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDFillTimer.setStatus("current")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDFillTimer.setUnits("milliseconds")


class _CvapSvcMultiCIDCACSCR_Type(Unsigned32):
    """Custom type cvapSvcMultiCIDCACSCR based on Unsigned32"""
    defaultValue = 450

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 60000),
    )


_CvapSvcMultiCIDCACSCR_Type.__name__ = "Unsigned32"
_CvapSvcMultiCIDCACSCR_Object = MibTableColumn
cvapSvcMultiCIDCACSCR = _CvapSvcMultiCIDCACSCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 14),
    _CvapSvcMultiCIDCACSCR_Type()
)
cvapSvcMultiCIDCACSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDCACSCR.setStatus("current")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDCACSCR.setUnits("Cells per Second")


class _CvapSvcMultiCIDCACPCR_Type(Unsigned32):
    """Custom type cvapSvcMultiCIDCACPCR based on Unsigned32"""
    defaultValue = 875

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 60000),
    )


_CvapSvcMultiCIDCACPCR_Type.__name__ = "Unsigned32"
_CvapSvcMultiCIDCACPCR_Object = MibTableColumn
cvapSvcMultiCIDCACPCR = _CvapSvcMultiCIDCACPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 15),
    _CvapSvcMultiCIDCACPCR_Type()
)
cvapSvcMultiCIDCACPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDCACPCR.setStatus("current")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDCACPCR.setUnits("Cells per Second")


class _CvapSvcMultiCIDOriginatDelTimer_Type(Unsigned32):
    """Custom type cvapSvcMultiCIDOriginatDelTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_CvapSvcMultiCIDOriginatDelTimer_Type.__name__ = "Unsigned32"
_CvapSvcMultiCIDOriginatDelTimer_Object = MibTableColumn
cvapSvcMultiCIDOriginatDelTimer = _CvapSvcMultiCIDOriginatDelTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 16),
    _CvapSvcMultiCIDOriginatDelTimer_Type()
)
cvapSvcMultiCIDOriginatDelTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDOriginatDelTimer.setStatus("current")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDOriginatDelTimer.setUnits("seconds")


class _CvapSvcMultiCIDTerminatDelTimer_Type(Unsigned32):
    """Custom type cvapSvcMultiCIDTerminatDelTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1195),
    )


_CvapSvcMultiCIDTerminatDelTimer_Type.__name__ = "Unsigned32"
_CvapSvcMultiCIDTerminatDelTimer_Object = MibTableColumn
cvapSvcMultiCIDTerminatDelTimer = _CvapSvcMultiCIDTerminatDelTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 17),
    _CvapSvcMultiCIDTerminatDelTimer_Type()
)
cvapSvcMultiCIDTerminatDelTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDTerminatDelTimer.setStatus("current")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDTerminatDelTimer.setUnits("seconds")


class _CvapSvcMultiCIDGlareThreshold_Type(Unsigned32):
    """Custom type cvapSvcMultiCIDGlareThreshold based on Unsigned32"""
    defaultValue = 243

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 248),
    )


_CvapSvcMultiCIDGlareThreshold_Type.__name__ = "Unsigned32"
_CvapSvcMultiCIDGlareThreshold_Object = MibTableColumn
cvapSvcMultiCIDGlareThreshold = _CvapSvcMultiCIDGlareThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 3, 1, 1, 18),
    _CvapSvcMultiCIDGlareThreshold_Type()
)
cvapSvcMultiCIDGlareThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDGlareThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cvapSvcMultiCIDGlareThreshold.setUnits("number of CIDs")
_CvapSvcStats_ObjectIdentity = ObjectIdentity
cvapSvcStats = _CvapSvcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4)
)
_CvapSvcStatsTable_Object = MibTable
cvapSvcStatsTable = _CvapSvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cvapSvcStatsTable.setStatus("current")
_CvapSvcStatsEntry_Object = MibTableRow
cvapSvcStatsEntry = _CvapSvcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1)
)
cvapSvcStatsEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cvapSvcStatsEntry.setStatus("current")
_CvapSvcTxSetups_Type = Counter32
_CvapSvcTxSetups_Object = MibTableColumn
cvapSvcTxSetups = _CvapSvcTxSetups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 1),
    _CvapSvcTxSetups_Type()
)
cvapSvcTxSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxSetups.setStatus("current")
_CvapSvcRxSetups_Type = Counter32
_CvapSvcRxSetups_Object = MibTableColumn
cvapSvcRxSetups = _CvapSvcRxSetups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 2),
    _CvapSvcRxSetups_Type()
)
cvapSvcRxSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxSetups.setStatus("current")
_CvapSvcTxCallProcs_Type = Counter32
_CvapSvcTxCallProcs_Object = MibTableColumn
cvapSvcTxCallProcs = _CvapSvcTxCallProcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 3),
    _CvapSvcTxCallProcs_Type()
)
cvapSvcTxCallProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxCallProcs.setStatus("current")
_CvapSvcRxCallProcs_Type = Counter32
_CvapSvcRxCallProcs_Object = MibTableColumn
cvapSvcRxCallProcs = _CvapSvcRxCallProcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 4),
    _CvapSvcRxCallProcs_Type()
)
cvapSvcRxCallProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxCallProcs.setStatus("current")
_CvapSvcTxConns_Type = Counter32
_CvapSvcTxConns_Object = MibTableColumn
cvapSvcTxConns = _CvapSvcTxConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 5),
    _CvapSvcTxConns_Type()
)
cvapSvcTxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxConns.setStatus("current")
_CvapSvcTxConnAcks_Type = Counter32
_CvapSvcTxConnAcks_Object = MibTableColumn
cvapSvcTxConnAcks = _CvapSvcTxConnAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 6),
    _CvapSvcTxConnAcks_Type()
)
cvapSvcTxConnAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxConnAcks.setStatus("current")
_CvapSvcRxConns_Type = Counter32
_CvapSvcRxConns_Object = MibTableColumn
cvapSvcRxConns = _CvapSvcRxConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 7),
    _CvapSvcRxConns_Type()
)
cvapSvcRxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxConns.setStatus("current")
_CvapSvcRxConnAcks_Type = Counter32
_CvapSvcRxConnAcks_Object = MibTableColumn
cvapSvcRxConnAcks = _CvapSvcRxConnAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 8),
    _CvapSvcRxConnAcks_Type()
)
cvapSvcRxConnAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxConnAcks.setStatus("current")
_CvapSvcTxReleases_Type = Counter32
_CvapSvcTxReleases_Object = MibTableColumn
cvapSvcTxReleases = _CvapSvcTxReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 9),
    _CvapSvcTxReleases_Type()
)
cvapSvcTxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxReleases.setStatus("current")
_CvapSvcTxReleaseCompls_Type = Counter32
_CvapSvcTxReleaseCompls_Object = MibTableColumn
cvapSvcTxReleaseCompls = _CvapSvcTxReleaseCompls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 10),
    _CvapSvcTxReleaseCompls_Type()
)
cvapSvcTxReleaseCompls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxReleaseCompls.setStatus("current")
_CvapSvcRxReleases_Type = Counter32
_CvapSvcRxReleases_Object = MibTableColumn
cvapSvcRxReleases = _CvapSvcRxReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 11),
    _CvapSvcRxReleases_Type()
)
cvapSvcRxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxReleases.setStatus("current")
_CvapSvcRxReleaseCompls_Type = Counter32
_CvapSvcRxReleaseCompls_Object = MibTableColumn
cvapSvcRxReleaseCompls = _CvapSvcRxReleaseCompls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 12),
    _CvapSvcRxReleaseCompls_Type()
)
cvapSvcRxReleaseCompls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxReleaseCompls.setStatus("current")
_CvapSvcTxRestarts_Type = Counter32
_CvapSvcTxRestarts_Object = MibTableColumn
cvapSvcTxRestarts = _CvapSvcTxRestarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 13),
    _CvapSvcTxRestarts_Type()
)
cvapSvcTxRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxRestarts.setStatus("current")
_CvapSvcTxRestartAcks_Type = Counter32
_CvapSvcTxRestartAcks_Object = MibTableColumn
cvapSvcTxRestartAcks = _CvapSvcTxRestartAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 14),
    _CvapSvcTxRestartAcks_Type()
)
cvapSvcTxRestartAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxRestartAcks.setStatus("current")
_CvapSvcRxRestarts_Type = Counter32
_CvapSvcRxRestarts_Object = MibTableColumn
cvapSvcRxRestarts = _CvapSvcRxRestarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 15),
    _CvapSvcRxRestarts_Type()
)
cvapSvcRxRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxRestarts.setStatus("current")
_CvapSvcRxRestartAcks_Type = Counter32
_CvapSvcRxRestartAcks_Object = MibTableColumn
cvapSvcRxRestartAcks = _CvapSvcRxRestartAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 16),
    _CvapSvcRxRestartAcks_Type()
)
cvapSvcRxRestartAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxRestartAcks.setStatus("current")
_CvapSvcTxResyncStrts_Type = Counter32
_CvapSvcTxResyncStrts_Object = MibTableColumn
cvapSvcTxResyncStrts = _CvapSvcTxResyncStrts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 17),
    _CvapSvcTxResyncStrts_Type()
)
cvapSvcTxResyncStrts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxResyncStrts.setStatus("current")
_CvapSvcTxResyncStrtAcks_Type = Counter32
_CvapSvcTxResyncStrtAcks_Object = MibTableColumn
cvapSvcTxResyncStrtAcks = _CvapSvcTxResyncStrtAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 18),
    _CvapSvcTxResyncStrtAcks_Type()
)
cvapSvcTxResyncStrtAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxResyncStrtAcks.setStatus("current")
_CvapSvcRxResyncStrts_Type = Counter32
_CvapSvcRxResyncStrts_Object = MibTableColumn
cvapSvcRxResyncStrts = _CvapSvcRxResyncStrts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 19),
    _CvapSvcRxResyncStrts_Type()
)
cvapSvcRxResyncStrts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxResyncStrts.setStatus("current")
_CvapSvcRxResyncStrtAcks_Type = Counter32
_CvapSvcRxResyncStrtAcks_Object = MibTableColumn
cvapSvcRxResyncStrtAcks = _CvapSvcRxResyncStrtAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 20),
    _CvapSvcRxResyncStrtAcks_Type()
)
cvapSvcRxResyncStrtAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxResyncStrtAcks.setStatus("current")
_CvapSvcTxResyncEnds_Type = Counter32
_CvapSvcTxResyncEnds_Object = MibTableColumn
cvapSvcTxResyncEnds = _CvapSvcTxResyncEnds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 21),
    _CvapSvcTxResyncEnds_Type()
)
cvapSvcTxResyncEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxResyncEnds.setStatus("current")
_CvapSvcTxResyncEndAcks_Type = Counter32
_CvapSvcTxResyncEndAcks_Object = MibTableColumn
cvapSvcTxResyncEndAcks = _CvapSvcTxResyncEndAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 22),
    _CvapSvcTxResyncEndAcks_Type()
)
cvapSvcTxResyncEndAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxResyncEndAcks.setStatus("current")
_CvapSvcRxResyncEnds_Type = Counter32
_CvapSvcRxResyncEnds_Object = MibTableColumn
cvapSvcRxResyncEnds = _CvapSvcRxResyncEnds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 23),
    _CvapSvcRxResyncEnds_Type()
)
cvapSvcRxResyncEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxResyncEnds.setStatus("current")
_CvapSvcRxResyncEndAcks_Type = Counter32
_CvapSvcRxResyncEndAcks_Object = MibTableColumn
cvapSvcRxResyncEndAcks = _CvapSvcRxResyncEndAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 24),
    _CvapSvcRxResyncEndAcks_Type()
)
cvapSvcRxResyncEndAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxResyncEndAcks.setStatus("current")
_CvapSvcTxBulkResyncs_Type = Counter32
_CvapSvcTxBulkResyncs_Object = MibTableColumn
cvapSvcTxBulkResyncs = _CvapSvcTxBulkResyncs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 25),
    _CvapSvcTxBulkResyncs_Type()
)
cvapSvcTxBulkResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcTxBulkResyncs.setStatus("current")
_CvapSvcRxBulkResyncs_Type = Counter32
_CvapSvcRxBulkResyncs_Object = MibTableColumn
cvapSvcRxBulkResyncs = _CvapSvcRxBulkResyncs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 26),
    _CvapSvcRxBulkResyncs_Type()
)
cvapSvcRxBulkResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRxBulkResyncs.setStatus("current")
_CvapSvcCallProcExpiries_Type = Counter32
_CvapSvcCallProcExpiries_Object = MibTableColumn
cvapSvcCallProcExpiries = _CvapSvcCallProcExpiries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 27),
    _CvapSvcCallProcExpiries_Type()
)
cvapSvcCallProcExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcCallProcExpiries.setStatus("current")
_CvapSvcReleasExpiries_Type = Counter32
_CvapSvcReleasExpiries_Object = MibTableColumn
cvapSvcReleasExpiries = _CvapSvcReleasExpiries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 28),
    _CvapSvcReleasExpiries_Type()
)
cvapSvcReleasExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcReleasExpiries.setStatus("current")
_CvapSvcConnExpiries_Type = Counter32
_CvapSvcConnExpiries_Object = MibTableColumn
cvapSvcConnExpiries = _CvapSvcConnExpiries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 29),
    _CvapSvcConnExpiries_Type()
)
cvapSvcConnExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcConnExpiries.setStatus("current")
_CvapSvcConnAckExpiries_Type = Counter32
_CvapSvcConnAckExpiries_Object = MibTableColumn
cvapSvcConnAckExpiries = _CvapSvcConnAckExpiries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 30),
    _CvapSvcConnAckExpiries_Type()
)
cvapSvcConnAckExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcConnAckExpiries.setStatus("current")
_CvapSvcRestartExpiries_Type = Counter32
_CvapSvcRestartExpiries_Object = MibTableColumn
cvapSvcRestartExpiries = _CvapSvcRestartExpiries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 31),
    _CvapSvcRestartExpiries_Type()
)
cvapSvcRestartExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcRestartExpiries.setStatus("current")
_CvapSvcResyncExpiries_Type = Counter32
_CvapSvcResyncExpiries_Object = MibTableColumn
cvapSvcResyncExpiries = _CvapSvcResyncExpiries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 1, 4, 1, 1, 32),
    _CvapSvcResyncExpiries_Type()
)
cvapSvcResyncExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvapSvcResyncExpiries.setStatus("current")
_CvaProfileMIBConformance_ObjectIdentity = ObjectIdentity
cvaProfileMIBConformance = _CvaProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 2)
)
_CvaProfileMIBCompliances_ObjectIdentity = ObjectIdentity
cvaProfileMIBCompliances = _CvaProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 2, 1)
)
_CvaProfileMIBGroups_ObjectIdentity = ObjectIdentity
cvaProfileMIBGroups = _CvaProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 2, 2)
)

# Managed Objects groups

cvapCodecConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 2, 2, 1)
)
cvapCodecConfigGroup.setObjects(
      *(("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecNegotiationOption"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigPreference"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigVoicePacketPeriod"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigVbdPacketPeriod"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigJitterDelayMode"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigJitterMaxDelay"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigJitterNomDelay"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigJitterMinDelay"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigDtmfRelay"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigPayloadType"))
)
if mibBuilder.loadTexts:
    cvapCodecConfigGroup.setStatus("deprecated")

cvapSvcConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 2, 2, 2)
)
cvapSvcConfigGroup.setObjects(
      *(("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcAtmQosCellDelay"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcAtmQosCtd"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcAtmQosClr"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTrfScalingFactor"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcAal2CidNumber"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcAggTrafficClipping"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcAggLinkState"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcPartialFillSupported"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcMgcpSelectorByteValue"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcH248SelectorByteValue"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcDelNotifGuardTimer"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcMultiCIDPerSvc"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcMultiCIDFillTimer"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcMultiCIDCACSCR"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcMultiCIDCACPCR"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcMultiCIDOriginatDelTimer"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcMultiCIDTerminatDelTimer"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcMultiCIDGlareThreshold"))
)
if mibBuilder.loadTexts:
    cvapSvcConfigGroup.setStatus("current")

cvapSvcStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 2, 2, 3)
)
cvapSvcStatsGroup.setObjects(
      *(("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxSetups"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxSetups"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxCallProcs"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxCallProcs"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxConns"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxConnAcks"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxConns"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxConnAcks"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxReleases"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxReleaseCompls"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxReleases"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxReleaseCompls"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxRestarts"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxRestartAcks"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxRestarts"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxRestartAcks"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxResyncStrts"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxResyncStrtAcks"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxResyncStrts"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxResyncStrtAcks"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxResyncEnds"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxResyncEndAcks"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxResyncEnds"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxResyncEndAcks"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcTxBulkResyncs"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRxBulkResyncs"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcCallProcExpiries"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcReleasExpiries"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcConnExpiries"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcConnAckExpiries"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcRestartExpiries"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapSvcResyncExpiries"))
)
if mibBuilder.loadTexts:
    cvapSvcStatsGroup.setStatus("current")

cvapCodecConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 2, 2, 4)
)
cvapCodecConfigGroupRev1.setObjects(
      *(("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecNegotiationOption"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigPreference"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigVoicePacketPeriod"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigJitterDelayMode"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigJitterMaxDelay"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigJitterMinDelay"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigDtmfRelay"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigPayloadType"),
        ("CISCO-VOICE-AALX-PROFILE-MIB", "cvapCodecConfigNewJtrNomDelay"))
)
if mibBuilder.loadTexts:
    cvapCodecConfigGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvaProfileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvaProfileMIBCompliance.setStatus(
        "deprecated"
    )

cvaProfileMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 323, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cvaProfileMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-AALX-PROFILE-MIB",
    **{"CiscoAal2ProfileType": CiscoAal2ProfileType,
       "CiscoAal2ProfileNumber": CiscoAal2ProfileNumber,
       "CiscoCodecPacketPeriod": CiscoCodecPacketPeriod,
       "ciscoVoiceAalxProfileMIB": ciscoVoiceAalxProfileMIB,
       "ciscoVoiceAalxProfileMIBNotifs": ciscoVoiceAalxProfileMIBNotifs,
       "ciscoVoiceAalxProfileMIBObjects": ciscoVoiceAalxProfileMIBObjects,
       "cvapCodecConfig": cvapCodecConfig,
       "cvapCodecTable": cvapCodecTable,
       "cvapCodecEntry": cvapCodecEntry,
       "cvapCodecNegotiationAdaptType": cvapCodecNegotiationAdaptType,
       "cvapCodecNegotiationOption": cvapCodecNegotiationOption,
       "cvapCodecConfigTable": cvapCodecConfigTable,
       "cvapCodecConfigEntry": cvapCodecConfigEntry,
       "cvapCodecConfigAdaptType": cvapCodecConfigAdaptType,
       "cvapCodecConfigType": cvapCodecConfigType,
       "cvapCodecConfigPreference": cvapCodecConfigPreference,
       "cvapCodecConfigVoicePacketPeriod": cvapCodecConfigVoicePacketPeriod,
       "cvapCodecConfigVbdPacketPeriod": cvapCodecConfigVbdPacketPeriod,
       "cvapCodecConfigJitterDelayMode": cvapCodecConfigJitterDelayMode,
       "cvapCodecConfigJitterMaxDelay": cvapCodecConfigJitterMaxDelay,
       "cvapCodecConfigJitterNomDelay": cvapCodecConfigJitterNomDelay,
       "cvapCodecConfigJitterMinDelay": cvapCodecConfigJitterMinDelay,
       "cvapCodecConfigDtmfRelay": cvapCodecConfigDtmfRelay,
       "cvapCodecConfigPayloadType": cvapCodecConfigPayloadType,
       "cvapCodecConfigNewJtrNomDelay": cvapCodecConfigNewJtrNomDelay,
       "cvapAal2Config": cvapAal2Config,
       "cvapSvcConfig": cvapSvcConfig,
       "cvapSvcConfigTable": cvapSvcConfigTable,
       "cvapSvcConfigEntry": cvapSvcConfigEntry,
       "cvapSvcAtmQosCellDelay": cvapSvcAtmQosCellDelay,
       "cvapSvcAtmQosCtd": cvapSvcAtmQosCtd,
       "cvapSvcAtmQosClr": cvapSvcAtmQosClr,
       "cvapSvcTrfScalingFactor": cvapSvcTrfScalingFactor,
       "cvapSvcAal2CidNumber": cvapSvcAal2CidNumber,
       "cvapSvcAggTrafficClipping": cvapSvcAggTrafficClipping,
       "cvapSvcAggLinkState": cvapSvcAggLinkState,
       "cvapSvcPartialFillSupported": cvapSvcPartialFillSupported,
       "cvapSvcMgcpSelectorByteValue": cvapSvcMgcpSelectorByteValue,
       "cvapSvcH248SelectorByteValue": cvapSvcH248SelectorByteValue,
       "cvapSvcDelNotifGuardTimer": cvapSvcDelNotifGuardTimer,
       "cvapSvcMultiCIDPerSvc": cvapSvcMultiCIDPerSvc,
       "cvapSvcMultiCIDFillTimer": cvapSvcMultiCIDFillTimer,
       "cvapSvcMultiCIDCACSCR": cvapSvcMultiCIDCACSCR,
       "cvapSvcMultiCIDCACPCR": cvapSvcMultiCIDCACPCR,
       "cvapSvcMultiCIDOriginatDelTimer": cvapSvcMultiCIDOriginatDelTimer,
       "cvapSvcMultiCIDTerminatDelTimer": cvapSvcMultiCIDTerminatDelTimer,
       "cvapSvcMultiCIDGlareThreshold": cvapSvcMultiCIDGlareThreshold,
       "cvapSvcStats": cvapSvcStats,
       "cvapSvcStatsTable": cvapSvcStatsTable,
       "cvapSvcStatsEntry": cvapSvcStatsEntry,
       "cvapSvcTxSetups": cvapSvcTxSetups,
       "cvapSvcRxSetups": cvapSvcRxSetups,
       "cvapSvcTxCallProcs": cvapSvcTxCallProcs,
       "cvapSvcRxCallProcs": cvapSvcRxCallProcs,
       "cvapSvcTxConns": cvapSvcTxConns,
       "cvapSvcTxConnAcks": cvapSvcTxConnAcks,
       "cvapSvcRxConns": cvapSvcRxConns,
       "cvapSvcRxConnAcks": cvapSvcRxConnAcks,
       "cvapSvcTxReleases": cvapSvcTxReleases,
       "cvapSvcTxReleaseCompls": cvapSvcTxReleaseCompls,
       "cvapSvcRxReleases": cvapSvcRxReleases,
       "cvapSvcRxReleaseCompls": cvapSvcRxReleaseCompls,
       "cvapSvcTxRestarts": cvapSvcTxRestarts,
       "cvapSvcTxRestartAcks": cvapSvcTxRestartAcks,
       "cvapSvcRxRestarts": cvapSvcRxRestarts,
       "cvapSvcRxRestartAcks": cvapSvcRxRestartAcks,
       "cvapSvcTxResyncStrts": cvapSvcTxResyncStrts,
       "cvapSvcTxResyncStrtAcks": cvapSvcTxResyncStrtAcks,
       "cvapSvcRxResyncStrts": cvapSvcRxResyncStrts,
       "cvapSvcRxResyncStrtAcks": cvapSvcRxResyncStrtAcks,
       "cvapSvcTxResyncEnds": cvapSvcTxResyncEnds,
       "cvapSvcTxResyncEndAcks": cvapSvcTxResyncEndAcks,
       "cvapSvcRxResyncEnds": cvapSvcRxResyncEnds,
       "cvapSvcRxResyncEndAcks": cvapSvcRxResyncEndAcks,
       "cvapSvcTxBulkResyncs": cvapSvcTxBulkResyncs,
       "cvapSvcRxBulkResyncs": cvapSvcRxBulkResyncs,
       "cvapSvcCallProcExpiries": cvapSvcCallProcExpiries,
       "cvapSvcReleasExpiries": cvapSvcReleasExpiries,
       "cvapSvcConnExpiries": cvapSvcConnExpiries,
       "cvapSvcConnAckExpiries": cvapSvcConnAckExpiries,
       "cvapSvcRestartExpiries": cvapSvcRestartExpiries,
       "cvapSvcResyncExpiries": cvapSvcResyncExpiries,
       "cvaProfileMIBConformance": cvaProfileMIBConformance,
       "cvaProfileMIBCompliances": cvaProfileMIBCompliances,
       "cvaProfileMIBCompliance": cvaProfileMIBCompliance,
       "cvaProfileMIBComplianceRev1": cvaProfileMIBComplianceRev1,
       "cvaProfileMIBGroups": cvaProfileMIBGroups,
       "cvapCodecConfigGroup": cvapCodecConfigGroup,
       "cvapSvcConfigGroup": cvapSvcConfigGroup,
       "cvapSvcStatsGroup": cvapSvcStatsGroup,
       "cvapCodecConfigGroupRev1": cvapCodecConfigGroupRev1}
)
