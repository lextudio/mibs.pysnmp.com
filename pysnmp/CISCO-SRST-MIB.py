# SNMP MIB module (CISCO-SRST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SRST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:45 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CountryCode,
 CvE164Address) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CountryCode",
    "CvE164Address")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

ciscoSrstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 441)
)
ciscoSrstMIB.setRevisions(
        ("2007-02-27 00:00",
         "2005-06-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SrstOperType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSrstMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoSrstMIBNotifications = _CiscoSrstMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 0)
)
_CiscoSrstMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSrstMIBObjects = _CiscoSrstMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1)
)
_CsrstGlobal_ObjectIdentity = ObjectIdentity
csrstGlobal = _CsrstGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 1)
)
_CsrstConf_ObjectIdentity = ObjectIdentity
csrstConf = _CsrstConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2)
)
_CsrstEnabled_Type = TruthValue
_CsrstEnabled_Object = MibScalar
csrstEnabled = _CsrstEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 1),
    _CsrstEnabled_Type()
)
csrstEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstEnabled.setStatus("current")


class _CsrstVersion_Type(SnmpAdminString):
    """Custom type csrstVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsrstVersion_Type.__name__ = "SnmpAdminString"
_CsrstVersion_Object = MibScalar
csrstVersion = _CsrstVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 2),
    _CsrstVersion_Type()
)
csrstVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstVersion.setStatus("current")
_CsrstIPAddressType_Type = InetAddressType
_CsrstIPAddressType_Object = MibScalar
csrstIPAddressType = _CsrstIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 3),
    _CsrstIPAddressType_Type()
)
csrstIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstIPAddressType.setStatus("current")
_CsrstIPAddress_Type = InetAddress
_CsrstIPAddress_Object = MibScalar
csrstIPAddress = _CsrstIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 4),
    _CsrstIPAddress_Type()
)
csrstIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstIPAddress.setStatus("current")


class _CsrstPortNumber_Type(InetPortNumber):
    """Custom type csrstPortNumber based on InetPortNumber"""
    defaultValue = 2000

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 9999),
    )


_CsrstPortNumber_Type.__name__ = "InetPortNumber"
_CsrstPortNumber_Object = MibScalar
csrstPortNumber = _CsrstPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 5),
    _CsrstPortNumber_Type()
)
csrstPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstPortNumber.setStatus("current")
_CsrstMaxConferences_Type = Unsigned32
_CsrstMaxConferences_Object = MibScalar
csrstMaxConferences = _CsrstMaxConferences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 6),
    _CsrstMaxConferences_Type()
)
csrstMaxConferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstMaxConferences.setStatus("current")


class _CsrstMaxEphones_Type(Unsigned32):
    """Custom type csrstMaxEphones based on Unsigned32"""
    defaultValue = 0


_CsrstMaxEphones_Object = MibScalar
csrstMaxEphones = _CsrstMaxEphones_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 7),
    _CsrstMaxEphones_Type()
)
csrstMaxEphones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstMaxEphones.setStatus("current")


class _CsrstMaxDN_Type(Unsigned32):
    """Custom type csrstMaxDN based on Unsigned32"""
    defaultValue = 0


_CsrstMaxDN_Object = MibScalar
csrstMaxDN = _CsrstMaxDN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 8),
    _CsrstMaxDN_Type()
)
csrstMaxDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstMaxDN.setStatus("current")
_CsrstSipPhoneUnRegThreshold_Type = Unsigned32
_CsrstSipPhoneUnRegThreshold_Object = MibScalar
csrstSipPhoneUnRegThreshold = _CsrstSipPhoneUnRegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 9),
    _CsrstSipPhoneUnRegThreshold_Type()
)
csrstSipPhoneUnRegThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csrstSipPhoneUnRegThreshold.setStatus("current")


class _CsrstCallFwdNoAnswer_Type(CvE164Address):
    """Custom type csrstCallFwdNoAnswer based on CvE164Address"""
    subtypeSpec = CvE164Address.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CsrstCallFwdNoAnswer_Type.__name__ = "CvE164Address"
_CsrstCallFwdNoAnswer_Object = MibScalar
csrstCallFwdNoAnswer = _CsrstCallFwdNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 10),
    _CsrstCallFwdNoAnswer_Type()
)
csrstCallFwdNoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstCallFwdNoAnswer.setStatus("current")
_CsrstCallFwdNoAnswerTo_Type = Unsigned32
_CsrstCallFwdNoAnswerTo_Object = MibScalar
csrstCallFwdNoAnswerTo = _CsrstCallFwdNoAnswerTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 11),
    _CsrstCallFwdNoAnswerTo_Type()
)
csrstCallFwdNoAnswerTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstCallFwdNoAnswerTo.setStatus("current")
if mibBuilder.loadTexts:
    csrstCallFwdNoAnswerTo.setUnits("seconds")


class _CsrstCallFwdBusy_Type(CvE164Address):
    """Custom type csrstCallFwdBusy based on CvE164Address"""
    subtypeSpec = CvE164Address.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CsrstCallFwdBusy_Type.__name__ = "CvE164Address"
_CsrstCallFwdBusy_Object = MibScalar
csrstCallFwdBusy = _CsrstCallFwdBusy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 12),
    _CsrstCallFwdBusy_Type()
)
csrstCallFwdBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstCallFwdBusy.setStatus("current")


class _CsrstMohFilename_Type(SnmpAdminString):
    """Custom type csrstMohFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsrstMohFilename_Type.__name__ = "SnmpAdminString"
_CsrstMohFilename_Object = MibScalar
csrstMohFilename = _CsrstMohFilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 13),
    _CsrstMohFilename_Type()
)
csrstMohFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstMohFilename.setStatus("current")
_CsrstMohMulticastAddrType_Type = InetAddressType
_CsrstMohMulticastAddrType_Object = MibScalar
csrstMohMulticastAddrType = _CsrstMohMulticastAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 14),
    _CsrstMohMulticastAddrType_Type()
)
csrstMohMulticastAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstMohMulticastAddrType.setStatus("current")
_CsrstMohMulticastAddr_Type = InetAddress
_CsrstMohMulticastAddr_Object = MibScalar
csrstMohMulticastAddr = _CsrstMohMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 15),
    _CsrstMohMulticastAddr_Type()
)
csrstMohMulticastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstMohMulticastAddr.setStatus("current")


class _CsrstMohMulticastPort_Type(InetPortNumber):
    """Custom type csrstMohMulticastPort based on InetPortNumber"""
    defaultValue = 2000

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 9999),
    )


_CsrstMohMulticastPort_Type.__name__ = "InetPortNumber"
_CsrstMohMulticastPort_Object = MibScalar
csrstMohMulticastPort = _CsrstMohMulticastPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 16),
    _CsrstMohMulticastPort_Type()
)
csrstMohMulticastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstMohMulticastPort.setStatus("current")


class _CsrstVoiceMailNumber_Type(CvE164Address):
    """Custom type csrstVoiceMailNumber based on CvE164Address"""
    subtypeSpec = CvE164Address.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CsrstVoiceMailNumber_Type.__name__ = "CvE164Address"
_CsrstVoiceMailNumber_Object = MibScalar
csrstVoiceMailNumber = _CsrstVoiceMailNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 17),
    _CsrstVoiceMailNumber_Type()
)
csrstVoiceMailNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstVoiceMailNumber.setStatus("current")


class _CsrstSystemMessagePrimary_Type(SnmpAdminString):
    """Custom type csrstSystemMessagePrimary based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CsrstSystemMessagePrimary_Type.__name__ = "SnmpAdminString"
_CsrstSystemMessagePrimary_Object = MibScalar
csrstSystemMessagePrimary = _CsrstSystemMessagePrimary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 18),
    _CsrstSystemMessagePrimary_Type()
)
csrstSystemMessagePrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSystemMessagePrimary.setStatus("current")


class _CsrstSystemMessageSecondary_Type(SnmpAdminString):
    """Custom type csrstSystemMessageSecondary based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CsrstSystemMessageSecondary_Type.__name__ = "SnmpAdminString"
_CsrstSystemMessageSecondary_Object = MibScalar
csrstSystemMessageSecondary = _CsrstSystemMessageSecondary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 19),
    _CsrstSystemMessageSecondary_Type()
)
csrstSystemMessageSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSystemMessageSecondary.setStatus("current")


class _CsrstScriptName_Type(SnmpAdminString):
    """Custom type csrstScriptName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsrstScriptName_Type.__name__ = "SnmpAdminString"
_CsrstScriptName_Object = MibScalar
csrstScriptName = _CsrstScriptName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 20),
    _CsrstScriptName_Type()
)
csrstScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstScriptName.setStatus("current")


class _CsrstSecondaryDialTone_Type(CvE164Address):
    """Custom type csrstSecondaryDialTone based on CvE164Address"""
    subtypeSpec = CvE164Address.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CsrstSecondaryDialTone_Type.__name__ = "CvE164Address"
_CsrstSecondaryDialTone_Object = MibScalar
csrstSecondaryDialTone = _CsrstSecondaryDialTone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 21),
    _CsrstSecondaryDialTone_Type()
)
csrstSecondaryDialTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSecondaryDialTone.setStatus("current")


class _CsrstTransferSystem_Type(Integer32):
    """Custom type csrstTransferSystem based on Integer32"""
    defaultValue = 3

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
        *(("blind", 1),
          ("fullBlind", 2),
          ("fullConsult", 3),
          ("localConsult", 4))
    )


_CsrstTransferSystem_Type.__name__ = "Integer32"
_CsrstTransferSystem_Object = MibScalar
csrstTransferSystem = _CsrstTransferSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 22),
    _CsrstTransferSystem_Type()
)
csrstTransferSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstTransferSystem.setStatus("current")


class _CsrstUserLocaleInfo_Type(CountryCode):
    """Custom type csrstUserLocaleInfo based on CountryCode"""
    defaultValue = OctetString("US")


_CsrstUserLocaleInfo_Object = MibScalar
csrstUserLocaleInfo = _CsrstUserLocaleInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 23),
    _CsrstUserLocaleInfo_Type()
)
csrstUserLocaleInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstUserLocaleInfo.setStatus("deprecated")


class _CsrstDateFormat_Type(Integer32):
    """Custom type csrstDateFormat based on Integer32"""
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
        *(("ddmmyy", 2),
          ("mmddyy", 1),
          ("yyddmm", 3),
          ("yymmdd", 4))
    )


_CsrstDateFormat_Type.__name__ = "Integer32"
_CsrstDateFormat_Object = MibScalar
csrstDateFormat = _CsrstDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 24),
    _CsrstDateFormat_Type()
)
csrstDateFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstDateFormat.setStatus("current")


class _CsrstTimeFormat_Type(Integer32):
    """Custom type csrstTimeFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twelveHour", 1),
          ("twentyFourHour", 2))
    )


_CsrstTimeFormat_Type.__name__ = "Integer32"
_CsrstTimeFormat_Object = MibScalar
csrstTimeFormat = _CsrstTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 25),
    _CsrstTimeFormat_Type()
)
csrstTimeFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstTimeFormat.setStatus("current")


class _CsrstInterdigitTo_Type(Unsigned32):
    """Custom type csrstInterdigitTo based on Unsigned32"""
    defaultValue = 10


_CsrstInterdigitTo_Object = MibScalar
csrstInterdigitTo = _CsrstInterdigitTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 26),
    _CsrstInterdigitTo_Type()
)
csrstInterdigitTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstInterdigitTo.setStatus("current")
if mibBuilder.loadTexts:
    csrstInterdigitTo.setUnits("seconds")


class _CsrstBusyTo_Type(Unsigned32):
    """Custom type csrstBusyTo based on Unsigned32"""
    defaultValue = 10


_CsrstBusyTo_Object = MibScalar
csrstBusyTo = _CsrstBusyTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 27),
    _CsrstBusyTo_Type()
)
csrstBusyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstBusyTo.setStatus("current")
if mibBuilder.loadTexts:
    csrstBusyTo.setUnits("seconds")


class _CsrstAlertTo_Type(Unsigned32):
    """Custom type csrstAlertTo based on Unsigned32"""
    defaultValue = 180


_CsrstAlertTo_Object = MibScalar
csrstAlertTo = _CsrstAlertTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 28),
    _CsrstAlertTo_Type()
)
csrstAlertTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstAlertTo.setStatus("current")
if mibBuilder.loadTexts:
    csrstAlertTo.setUnits("seconds")
_CsrstXlateCalledNumber_Type = Unsigned32
_CsrstXlateCalledNumber_Object = MibScalar
csrstXlateCalledNumber = _CsrstXlateCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 29),
    _CsrstXlateCalledNumber_Type()
)
csrstXlateCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstXlateCalledNumber.setStatus("current")
_CsrstXlateCallingNumber_Type = Unsigned32
_CsrstXlateCallingNumber_Object = MibScalar
csrstXlateCallingNumber = _CsrstXlateCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 30),
    _CsrstXlateCallingNumber_Type()
)
csrstXlateCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstXlateCallingNumber.setStatus("current")
_CsrstAliasTable_Object = MibTable
csrstAliasTable = _CsrstAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 31)
)
if mibBuilder.loadTexts:
    csrstAliasTable.setStatus("current")
_CsrstAliasEntry_Object = MibTableRow
csrstAliasEntry = _CsrstAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 31, 1)
)
csrstAliasEntry.setIndexNames(
    (0, "CISCO-SRST-MIB", "csrstAliasIndex"),
)
if mibBuilder.loadTexts:
    csrstAliasEntry.setStatus("current")
_CsrstAliasIndex_Type = Unsigned32
_CsrstAliasIndex_Object = MibTableColumn
csrstAliasIndex = _CsrstAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 31, 1, 1),
    _CsrstAliasIndex_Type()
)
csrstAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csrstAliasIndex.setStatus("current")
_CsrstAliasTag_Type = Unsigned32
_CsrstAliasTag_Object = MibTableColumn
csrstAliasTag = _CsrstAliasTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 31, 1, 2),
    _CsrstAliasTag_Type()
)
csrstAliasTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstAliasTag.setStatus("current")


class _CsrstAliasNumPattern_Type(SnmpAdminString):
    """Custom type csrstAliasNumPattern based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CsrstAliasNumPattern_Type.__name__ = "SnmpAdminString"
_CsrstAliasNumPattern_Object = MibTableColumn
csrstAliasNumPattern = _CsrstAliasNumPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 31, 1, 3),
    _CsrstAliasNumPattern_Type()
)
csrstAliasNumPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstAliasNumPattern.setStatus("current")


class _CsrstAliasAltNumber_Type(SnmpAdminString):
    """Custom type csrstAliasAltNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CsrstAliasAltNumber_Type.__name__ = "SnmpAdminString"
_CsrstAliasAltNumber_Object = MibTableColumn
csrstAliasAltNumber = _CsrstAliasAltNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 31, 1, 4),
    _CsrstAliasAltNumber_Type()
)
csrstAliasAltNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstAliasAltNumber.setStatus("current")
_CsrstAliasPreference_Type = Unsigned32
_CsrstAliasPreference_Object = MibTableColumn
csrstAliasPreference = _CsrstAliasPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 31, 1, 5),
    _CsrstAliasPreference_Type()
)
csrstAliasPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstAliasPreference.setStatus("current")
_CsrstAliasHuntStopEnabled_Type = TruthValue
_CsrstAliasHuntStopEnabled_Object = MibTableColumn
csrstAliasHuntStopEnabled = _CsrstAliasHuntStopEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 31, 1, 6),
    _CsrstAliasHuntStopEnabled_Type()
)
csrstAliasHuntStopEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstAliasHuntStopEnabled.setStatus("current")
_CsrstAccessCodeTable_Object = MibTable
csrstAccessCodeTable = _CsrstAccessCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 32)
)
if mibBuilder.loadTexts:
    csrstAccessCodeTable.setStatus("current")
_CsrstAccessCodeEntry_Object = MibTableRow
csrstAccessCodeEntry = _CsrstAccessCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 32, 1)
)
csrstAccessCodeEntry.setIndexNames(
    (0, "CISCO-SRST-MIB", "csrstAccessCodeType"),
)
if mibBuilder.loadTexts:
    csrstAccessCodeEntry.setStatus("current")


class _CsrstAccessCodeType_Type(Integer32):
    """Custom type csrstAccessCodeType based on Integer32"""
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
        *(("bri", 3),
          ("em", 2),
          ("fxo", 1),
          ("pri", 4))
    )


_CsrstAccessCodeType_Type.__name__ = "Integer32"
_CsrstAccessCodeType_Object = MibTableColumn
csrstAccessCodeType = _CsrstAccessCodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 32, 1, 1),
    _CsrstAccessCodeType_Type()
)
csrstAccessCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstAccessCodeType.setStatus("current")


class _CsrstAccessCode_Type(SnmpAdminString):
    """Custom type csrstAccessCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CsrstAccessCode_Type.__name__ = "SnmpAdminString"
_CsrstAccessCode_Object = MibTableColumn
csrstAccessCode = _CsrstAccessCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 32, 1, 2),
    _CsrstAccessCode_Type()
)
csrstAccessCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstAccessCode.setStatus("current")
_CsrstAccessCodeDIDEnabled_Type = TruthValue
_CsrstAccessCodeDIDEnabled_Object = MibTableColumn
csrstAccessCodeDIDEnabled = _CsrstAccessCodeDIDEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 32, 1, 3),
    _CsrstAccessCodeDIDEnabled_Type()
)
csrstAccessCodeDIDEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstAccessCodeDIDEnabled.setStatus("current")
_CsrstLimitDNTable_Object = MibTable
csrstLimitDNTable = _CsrstLimitDNTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 33)
)
if mibBuilder.loadTexts:
    csrstLimitDNTable.setStatus("current")
_CsrstLimitDNEntry_Object = MibTableRow
csrstLimitDNEntry = _CsrstLimitDNEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 33, 1)
)
csrstLimitDNEntry.setIndexNames(
    (0, "CISCO-SRST-MIB", "csrstLimitDNType"),
)
if mibBuilder.loadTexts:
    csrstLimitDNEntry.setStatus("current")


class _CsrstLimitDNType_Type(Integer32):
    """Custom type csrstLimitDNType based on Integer32"""
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
        *(("ipPhone7910", 1),
          ("ipPhone7935", 2),
          ("ipPhone7936", 6),
          ("ipPhone7940", 3),
          ("ipPhone7960", 4),
          ("ipPhone7970", 5))
    )


_CsrstLimitDNType_Type.__name__ = "Integer32"
_CsrstLimitDNType_Object = MibTableColumn
csrstLimitDNType = _CsrstLimitDNType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 33, 1, 1),
    _CsrstLimitDNType_Type()
)
csrstLimitDNType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstLimitDNType.setStatus("current")
_CsrstLimitDN_Type = Unsigned32
_CsrstLimitDN_Object = MibTableColumn
csrstLimitDN = _CsrstLimitDN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 33, 1, 2),
    _CsrstLimitDN_Type()
)
csrstLimitDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstLimitDN.setStatus("current")


class _CsrstNotificationEnabled_Type(TruthValue):
    """Custom type csrstNotificationEnabled based on TruthValue"""


_CsrstNotificationEnabled_Object = MibScalar
csrstNotificationEnabled = _CsrstNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 34),
    _CsrstNotificationEnabled_Type()
)
csrstNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csrstNotificationEnabled.setStatus("current")


class _CsrstUserLocaleInfoRev1_Type(DisplayString):
    """Custom type csrstUserLocaleInfoRev1 based on DisplayString"""
    defaultValue = OctetString("US/US/US/US/US")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 64),
    )


_CsrstUserLocaleInfoRev1_Type.__name__ = "DisplayString"
_CsrstUserLocaleInfoRev1_Object = MibScalar
csrstUserLocaleInfoRev1 = _CsrstUserLocaleInfoRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 2, 35),
    _CsrstUserLocaleInfoRev1_Type()
)
csrstUserLocaleInfoRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstUserLocaleInfoRev1.setStatus("current")
_CsrstActiveStats_ObjectIdentity = ObjectIdentity
csrstActiveStats = _CsrstActiveStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 3)
)
_CsrstState_Type = SrstOperType
_CsrstState_Object = MibScalar
csrstState = _CsrstState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 3, 1),
    _CsrstState_Type()
)
csrstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstState.setStatus("current")
_CsrstSipPhoneCurrentRegistered_Type = Gauge32
_CsrstSipPhoneCurrentRegistered_Object = MibScalar
csrstSipPhoneCurrentRegistered = _CsrstSipPhoneCurrentRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 3, 2),
    _CsrstSipPhoneCurrentRegistered_Type()
)
csrstSipPhoneCurrentRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipPhoneCurrentRegistered.setStatus("current")
_CsrstSipCallLegs_Type = Counter32
_CsrstSipCallLegs_Object = MibScalar
csrstSipCallLegs = _CsrstSipCallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 3, 3),
    _CsrstSipCallLegs_Type()
)
csrstSipCallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipCallLegs.setStatus("current")
_CsrstTotalUpTime_Type = Counter32
_CsrstTotalUpTime_Object = MibScalar
csrstTotalUpTime = _CsrstTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 3, 4),
    _CsrstTotalUpTime_Type()
)
csrstTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstTotalUpTime.setStatus("current")
if mibBuilder.loadTexts:
    csrstTotalUpTime.setUnits("minutes")
_CsrstSipConf_ObjectIdentity = ObjectIdentity
csrstSipConf = _CsrstSipConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4)
)


class _CsrstSipRegSrvExpMax_Type(Integer32):
    """Custom type csrstSipRegSrvExpMax based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 86400),
    )


_CsrstSipRegSrvExpMax_Type.__name__ = "Integer32"
_CsrstSipRegSrvExpMax_Object = MibScalar
csrstSipRegSrvExpMax = _CsrstSipRegSrvExpMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 1),
    _CsrstSipRegSrvExpMax_Type()
)
csrstSipRegSrvExpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipRegSrvExpMax.setStatus("current")
if mibBuilder.loadTexts:
    csrstSipRegSrvExpMax.setUnits("seconds")


class _CsrstSipRegSrvExpMin_Type(Integer32):
    """Custom type csrstSipRegSrvExpMin based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_CsrstSipRegSrvExpMin_Type.__name__ = "Integer32"
_CsrstSipRegSrvExpMin_Object = MibScalar
csrstSipRegSrvExpMin = _CsrstSipRegSrvExpMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 2),
    _CsrstSipRegSrvExpMin_Type()
)
csrstSipRegSrvExpMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipRegSrvExpMin.setStatus("current")
if mibBuilder.loadTexts:
    csrstSipRegSrvExpMin.setUnits("seconds")


class _CsrstSipIp2IpGlobalEnabled_Type(TruthValue):
    """Custom type csrstSipIp2IpGlobalEnabled based on TruthValue"""


_CsrstSipIp2IpGlobalEnabled_Object = MibScalar
csrstSipIp2IpGlobalEnabled = _CsrstSipIp2IpGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 3),
    _CsrstSipIp2IpGlobalEnabled_Type()
)
csrstSipIp2IpGlobalEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipIp2IpGlobalEnabled.setStatus("current")


class _CsrstSipSend300MultSupport_Type(Integer32):
    """Custom type csrstSipSend300MultSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bestMatch", 1),
          ("longestMatch", 2))
    )


_CsrstSipSend300MultSupport_Type.__name__ = "Integer32"
_CsrstSipSend300MultSupport_Object = MibScalar
csrstSipSend300MultSupport = _CsrstSipSend300MultSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 4),
    _CsrstSipSend300MultSupport_Type()
)
csrstSipSend300MultSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipSend300MultSupport.setStatus("current")
_CsrstSipVoRegPoolTable_Object = MibTable
csrstSipVoRegPoolTable = _CsrstSipVoRegPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5)
)
if mibBuilder.loadTexts:
    csrstSipVoRegPoolTable.setStatus("current")
_CsrstSipVoRegPoolEntry_Object = MibTableRow
csrstSipVoRegPoolEntry = _CsrstSipVoRegPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5, 1)
)
csrstSipVoRegPoolEntry.setIndexNames(
    (0, "CISCO-SRST-MIB", "csrstSipVoRegPoolTag"),
)
if mibBuilder.loadTexts:
    csrstSipVoRegPoolEntry.setStatus("current")
_CsrstSipVoRegPoolTag_Type = Unsigned32
_CsrstSipVoRegPoolTag_Object = MibTableColumn
csrstSipVoRegPoolTag = _CsrstSipVoRegPoolTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5, 1, 1),
    _CsrstSipVoRegPoolTag_Type()
)
csrstSipVoRegPoolTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csrstSipVoRegPoolTag.setStatus("current")


class _CsrstSipNetId_Type(SnmpAdminString):
    """Custom type csrstSipNetId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CsrstSipNetId_Type.__name__ = "SnmpAdminString"
_CsrstSipNetId_Object = MibTableColumn
csrstSipNetId = _CsrstSipNetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5, 1, 2),
    _CsrstSipNetId_Type()
)
csrstSipNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipNetId.setStatus("current")
_CsrstSipVoRegPoolIpAddrType_Type = InetAddressType
_CsrstSipVoRegPoolIpAddrType_Object = MibTableColumn
csrstSipVoRegPoolIpAddrType = _CsrstSipVoRegPoolIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5, 1, 3),
    _CsrstSipVoRegPoolIpAddrType_Type()
)
csrstSipVoRegPoolIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipVoRegPoolIpAddrType.setStatus("current")
_CsrstSipNetMask_Type = InetAddress
_CsrstSipNetMask_Object = MibTableColumn
csrstSipNetMask = _CsrstSipNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5, 1, 4),
    _CsrstSipNetMask_Type()
)
csrstSipNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipNetMask.setStatus("current")
_CsrstSipProxySrvIpAddr_Type = InetAddress
_CsrstSipProxySrvIpAddr_Object = MibTableColumn
csrstSipProxySrvIpAddr = _CsrstSipProxySrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5, 1, 5),
    _CsrstSipProxySrvIpAddr_Type()
)
csrstSipProxySrvIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipProxySrvIpAddr.setStatus("current")


class _CsrstSipProxySrvPref_Type(Unsigned32):
    """Custom type csrstSipProxySrvPref based on Unsigned32"""
    defaultValue = 0


_CsrstSipProxySrvPref_Object = MibTableColumn
csrstSipProxySrvPref = _CsrstSipProxySrvPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5, 1, 6),
    _CsrstSipProxySrvPref_Type()
)
csrstSipProxySrvPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipProxySrvPref.setStatus("current")


class _CsrstSipProxySrvMonitor_Type(Integer32):
    """Custom type csrstSipProxySrvMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("rtr", 2))
    )


_CsrstSipProxySrvMonitor_Type.__name__ = "Integer32"
_CsrstSipProxySrvMonitor_Object = MibTableColumn
csrstSipProxySrvMonitor = _CsrstSipProxySrvMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5, 1, 7),
    _CsrstSipProxySrvMonitor_Type()
)
csrstSipProxySrvMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipProxySrvMonitor.setStatus("current")
_CsrstSipProxySrvAltIpAddr_Type = InetAddress
_CsrstSipProxySrvAltIpAddr_Object = MibTableColumn
csrstSipProxySrvAltIpAddr = _CsrstSipProxySrvAltIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5, 1, 8),
    _CsrstSipProxySrvAltIpAddr_Type()
)
csrstSipProxySrvAltIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipProxySrvAltIpAddr.setStatus("current")


class _CsrstSipDefaultPreference_Type(Unsigned32):
    """Custom type csrstSipDefaultPreference based on Unsigned32"""
    defaultValue = 0


_CsrstSipDefaultPreference_Object = MibTableColumn
csrstSipDefaultPreference = _CsrstSipDefaultPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5, 1, 9),
    _CsrstSipDefaultPreference_Type()
)
csrstSipDefaultPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipDefaultPreference.setStatus("current")


class _CsrstSipVoRegPoolAppl_Type(SnmpAdminString):
    """Custom type csrstSipVoRegPoolAppl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsrstSipVoRegPoolAppl_Type.__name__ = "SnmpAdminString"
_CsrstSipVoRegPoolAppl_Object = MibTableColumn
csrstSipVoRegPoolAppl = _CsrstSipVoRegPoolAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 5, 1, 10),
    _CsrstSipVoRegPoolAppl_Type()
)
csrstSipVoRegPoolAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipVoRegPoolAppl.setStatus("current")
_CsrstSipVoRegNumberListTable_Object = MibTable
csrstSipVoRegNumberListTable = _CsrstSipVoRegNumberListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 6)
)
if mibBuilder.loadTexts:
    csrstSipVoRegNumberListTable.setStatus("current")
_CsrstSipVoRegNumberListEntry_Object = MibTableRow
csrstSipVoRegNumberListEntry = _CsrstSipVoRegNumberListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 6, 1)
)
csrstSipVoRegNumberListEntry.setIndexNames(
    (0, "CISCO-SRST-MIB", "csrstSipVoRegPoolTag"),
    (0, "CISCO-SRST-MIB", "csrstSipVoRegNumberListIndex"),
)
if mibBuilder.loadTexts:
    csrstSipVoRegNumberListEntry.setStatus("current")
_CsrstSipVoRegNumberListIndex_Type = Unsigned32
_CsrstSipVoRegNumberListIndex_Object = MibTableColumn
csrstSipVoRegNumberListIndex = _CsrstSipVoRegNumberListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 6, 1, 1),
    _CsrstSipVoRegNumberListIndex_Type()
)
csrstSipVoRegNumberListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csrstSipVoRegNumberListIndex.setStatus("current")
_CsrstSipVoRegNumberListTag_Type = Unsigned32
_CsrstSipVoRegNumberListTag_Object = MibTableColumn
csrstSipVoRegNumberListTag = _CsrstSipVoRegNumberListTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 6, 1, 2),
    _CsrstSipVoRegNumberListTag_Type()
)
csrstSipVoRegNumberListTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipVoRegNumberListTag.setStatus("current")


class _CsrstSipVoRegNumberPattern_Type(CvE164Address):
    """Custom type csrstSipVoRegNumberPattern based on CvE164Address"""
    subtypeSpec = CvE164Address.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CsrstSipVoRegNumberPattern_Type.__name__ = "CvE164Address"
_CsrstSipVoRegNumberPattern_Object = MibTableColumn
csrstSipVoRegNumberPattern = _CsrstSipVoRegNumberPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 6, 1, 3),
    _CsrstSipVoRegNumberPattern_Type()
)
csrstSipVoRegNumberPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipVoRegNumberPattern.setStatus("current")


class _CsrstSipVoRegNumberPref_Type(Unsigned32):
    """Custom type csrstSipVoRegNumberPref based on Unsigned32"""
    defaultValue = 0


_CsrstSipVoRegNumberPref_Object = MibTableColumn
csrstSipVoRegNumberPref = _CsrstSipVoRegNumberPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 6, 1, 4),
    _CsrstSipVoRegNumberPref_Type()
)
csrstSipVoRegNumberPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipVoRegNumberPref.setStatus("current")
_CsrstSipVoRegNumberHuntstopEnabled_Type = TruthValue
_CsrstSipVoRegNumberHuntstopEnabled_Object = MibTableColumn
csrstSipVoRegNumberHuntstopEnabled = _CsrstSipVoRegNumberHuntstopEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 6, 1, 5),
    _CsrstSipVoRegNumberHuntstopEnabled_Type()
)
csrstSipVoRegNumberHuntstopEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipVoRegNumberHuntstopEnabled.setStatus("current")
_CsrstSipEndpointTable_Object = MibTable
csrstSipEndpointTable = _CsrstSipEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 7)
)
if mibBuilder.loadTexts:
    csrstSipEndpointTable.setStatus("current")
_CsrstSipEndpointEntry_Object = MibTableRow
csrstSipEndpointEntry = _CsrstSipEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 7, 1)
)
csrstSipEndpointEntry.setIndexNames(
    (0, "CISCO-SRST-MIB", "csrstSipEndpointTag"),
)
if mibBuilder.loadTexts:
    csrstSipEndpointEntry.setStatus("current")
_CsrstSipEndpointTag_Type = Unsigned32
_CsrstSipEndpointTag_Object = MibTableColumn
csrstSipEndpointTag = _CsrstSipEndpointTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 7, 1, 1),
    _CsrstSipEndpointTag_Type()
)
csrstSipEndpointTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csrstSipEndpointTag.setStatus("current")
_CsrstSipVoRegPoolEdptTag_Type = Unsigned32
_CsrstSipVoRegPoolEdptTag_Object = MibTableColumn
csrstSipVoRegPoolEdptTag = _CsrstSipVoRegPoolEdptTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 7, 1, 2),
    _CsrstSipVoRegPoolEdptTag_Type()
)
csrstSipVoRegPoolEdptTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipVoRegPoolEdptTag.setStatus("current")
_CsrstSipEndpointIpAddrType_Type = InetAddressType
_CsrstSipEndpointIpAddrType_Object = MibTableColumn
csrstSipEndpointIpAddrType = _CsrstSipEndpointIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 7, 1, 3),
    _CsrstSipEndpointIpAddrType_Type()
)
csrstSipEndpointIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipEndpointIpAddrType.setStatus("current")
_CsrstSipEndpointIpAddress_Type = InetAddress
_CsrstSipEndpointIpAddress_Object = MibTableColumn
csrstSipEndpointIpAddress = _CsrstSipEndpointIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 7, 1, 4),
    _CsrstSipEndpointIpAddress_Type()
)
csrstSipEndpointIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipEndpointIpAddress.setStatus("current")


class _CsrstSipEndpointDN_Type(CvE164Address):
    """Custom type csrstSipEndpointDN based on CvE164Address"""
    subtypeSpec = CvE164Address.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CsrstSipEndpointDN_Type.__name__ = "CvE164Address"
_CsrstSipEndpointDN_Object = MibTableColumn
csrstSipEndpointDN = _CsrstSipEndpointDN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 1, 4, 7, 1, 5),
    _CsrstSipEndpointDN_Type()
)
csrstSipEndpointDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrstSipEndpointDN.setStatus("current")
_CiscoSrstMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSrstMIBConformance = _CiscoSrstMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2)
)
_CiscoSrstMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSrstMIBCompliances = _CiscoSrstMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 1)
)
_CiscoSrstMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSrstMIBGroups = _CiscoSrstMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 2)
)


class _CsrstSysNotifSeverity_Type(Integer32):
    """Custom type csrstSysNotifSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("major", 3),
          ("minor", 2))
    )


_CsrstSysNotifSeverity_Type.__name__ = "Integer32"
_CsrstSysNotifSeverity_Object = MibScalar
csrstSysNotifSeverity = _CsrstSysNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 2, 2, 1),
    _CsrstSysNotifSeverity_Type()
)
csrstSysNotifSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csrstSysNotifSeverity.setStatus("current")


class _CsrstSysNotifReason_Type(SnmpAdminString):
    """Custom type csrstSysNotifReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsrstSysNotifReason_Type.__name__ = "SnmpAdminString"
_CsrstSysNotifReason_Object = MibScalar
csrstSysNotifReason = _CsrstSysNotifReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 2, 2, 2),
    _CsrstSysNotifReason_Type()
)
csrstSysNotifReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csrstSysNotifReason.setStatus("current")

# Managed Objects groups

csrstConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 2, 1)
)
csrstConfGroup.setObjects(
      *(("CISCO-SRST-MIB", "csrstEnabled"),
        ("CISCO-SRST-MIB", "csrstVersion"),
        ("CISCO-SRST-MIB", "csrstIPAddressType"),
        ("CISCO-SRST-MIB", "csrstIPAddress"),
        ("CISCO-SRST-MIB", "csrstPortNumber"),
        ("CISCO-SRST-MIB", "csrstMaxConferences"),
        ("CISCO-SRST-MIB", "csrstMaxEphones"),
        ("CISCO-SRST-MIB", "csrstMaxDN"),
        ("CISCO-SRST-MIB", "csrstSipPhoneUnRegThreshold"),
        ("CISCO-SRST-MIB", "csrstCallFwdNoAnswer"),
        ("CISCO-SRST-MIB", "csrstCallFwdNoAnswerTo"),
        ("CISCO-SRST-MIB", "csrstCallFwdBusy"),
        ("CISCO-SRST-MIB", "csrstMohFilename"),
        ("CISCO-SRST-MIB", "csrstMohMulticastAddrType"),
        ("CISCO-SRST-MIB", "csrstMohMulticastAddr"),
        ("CISCO-SRST-MIB", "csrstMohMulticastPort"),
        ("CISCO-SRST-MIB", "csrstVoiceMailNumber"),
        ("CISCO-SRST-MIB", "csrstSystemMessagePrimary"),
        ("CISCO-SRST-MIB", "csrstSystemMessageSecondary"),
        ("CISCO-SRST-MIB", "csrstScriptName"),
        ("CISCO-SRST-MIB", "csrstSecondaryDialTone"),
        ("CISCO-SRST-MIB", "csrstTransferSystem"),
        ("CISCO-SRST-MIB", "csrstUserLocaleInfo"),
        ("CISCO-SRST-MIB", "csrstDateFormat"),
        ("CISCO-SRST-MIB", "csrstTimeFormat"),
        ("CISCO-SRST-MIB", "csrstInterdigitTo"),
        ("CISCO-SRST-MIB", "csrstBusyTo"),
        ("CISCO-SRST-MIB", "csrstAlertTo"),
        ("CISCO-SRST-MIB", "csrstXlateCalledNumber"),
        ("CISCO-SRST-MIB", "csrstXlateCallingNumber"),
        ("CISCO-SRST-MIB", "csrstAliasTag"),
        ("CISCO-SRST-MIB", "csrstAliasNumPattern"),
        ("CISCO-SRST-MIB", "csrstAliasAltNumber"),
        ("CISCO-SRST-MIB", "csrstAliasPreference"),
        ("CISCO-SRST-MIB", "csrstAliasHuntStopEnabled"),
        ("CISCO-SRST-MIB", "csrstAccessCodeType"),
        ("CISCO-SRST-MIB", "csrstAccessCode"),
        ("CISCO-SRST-MIB", "csrstAccessCodeDIDEnabled"),
        ("CISCO-SRST-MIB", "csrstLimitDNType"),
        ("CISCO-SRST-MIB", "csrstLimitDN"),
        ("CISCO-SRST-MIB", "csrstNotificationEnabled"))
)
if mibBuilder.loadTexts:
    csrstConfGroup.setStatus("deprecated")

csrstNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 2, 2)
)
csrstNotifInfoGroup.setObjects(
      *(("CISCO-SRST-MIB", "csrstSysNotifSeverity"),
        ("CISCO-SRST-MIB", "csrstSysNotifReason"))
)
if mibBuilder.loadTexts:
    csrstNotifInfoGroup.setStatus("current")

csrstActiveStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 2, 3)
)
csrstActiveStatsGroup.setObjects(
      *(("CISCO-SRST-MIB", "csrstState"),
        ("CISCO-SRST-MIB", "csrstSipPhoneCurrentRegistered"),
        ("CISCO-SRST-MIB", "csrstSipCallLegs"),
        ("CISCO-SRST-MIB", "csrstTotalUpTime"))
)
if mibBuilder.loadTexts:
    csrstActiveStatsGroup.setStatus("current")

csrstSipConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 2, 4)
)
csrstSipConfGroup.setObjects(
      *(("CISCO-SRST-MIB", "csrstSipRegSrvExpMax"),
        ("CISCO-SRST-MIB", "csrstSipRegSrvExpMin"),
        ("CISCO-SRST-MIB", "csrstSipIp2IpGlobalEnabled"),
        ("CISCO-SRST-MIB", "csrstSipSend300MultSupport"),
        ("CISCO-SRST-MIB", "csrstSipNetId"),
        ("CISCO-SRST-MIB", "csrstSipVoRegPoolIpAddrType"),
        ("CISCO-SRST-MIB", "csrstSipNetMask"),
        ("CISCO-SRST-MIB", "csrstSipProxySrvIpAddr"),
        ("CISCO-SRST-MIB", "csrstSipProxySrvPref"),
        ("CISCO-SRST-MIB", "csrstSipProxySrvMonitor"),
        ("CISCO-SRST-MIB", "csrstSipProxySrvAltIpAddr"),
        ("CISCO-SRST-MIB", "csrstSipDefaultPreference"),
        ("CISCO-SRST-MIB", "csrstSipVoRegPoolAppl"),
        ("CISCO-SRST-MIB", "csrstSipVoRegNumberListTag"),
        ("CISCO-SRST-MIB", "csrstSipVoRegNumberPattern"),
        ("CISCO-SRST-MIB", "csrstSipVoRegNumberPref"),
        ("CISCO-SRST-MIB", "csrstSipVoRegNumberHuntstopEnabled"),
        ("CISCO-SRST-MIB", "csrstSipVoRegPoolEdptTag"),
        ("CISCO-SRST-MIB", "csrstSipEndpointIpAddrType"),
        ("CISCO-SRST-MIB", "csrstSipEndpointIpAddress"),
        ("CISCO-SRST-MIB", "csrstSipEndpointDN"))
)
if mibBuilder.loadTexts:
    csrstSipConfGroup.setStatus("current")

csrstConfGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 2, 6)
)
csrstConfGroupRev1.setObjects(
      *(("CISCO-SRST-MIB", "csrstEnabled"),
        ("CISCO-SRST-MIB", "csrstVersion"),
        ("CISCO-SRST-MIB", "csrstIPAddressType"),
        ("CISCO-SRST-MIB", "csrstIPAddress"),
        ("CISCO-SRST-MIB", "csrstPortNumber"),
        ("CISCO-SRST-MIB", "csrstMaxConferences"),
        ("CISCO-SRST-MIB", "csrstMaxEphones"),
        ("CISCO-SRST-MIB", "csrstMaxDN"),
        ("CISCO-SRST-MIB", "csrstSipPhoneUnRegThreshold"),
        ("CISCO-SRST-MIB", "csrstCallFwdNoAnswer"),
        ("CISCO-SRST-MIB", "csrstCallFwdNoAnswerTo"),
        ("CISCO-SRST-MIB", "csrstCallFwdBusy"),
        ("CISCO-SRST-MIB", "csrstMohFilename"),
        ("CISCO-SRST-MIB", "csrstMohMulticastAddrType"),
        ("CISCO-SRST-MIB", "csrstMohMulticastAddr"),
        ("CISCO-SRST-MIB", "csrstMohMulticastPort"),
        ("CISCO-SRST-MIB", "csrstVoiceMailNumber"),
        ("CISCO-SRST-MIB", "csrstSystemMessagePrimary"),
        ("CISCO-SRST-MIB", "csrstSystemMessageSecondary"),
        ("CISCO-SRST-MIB", "csrstScriptName"),
        ("CISCO-SRST-MIB", "csrstSecondaryDialTone"),
        ("CISCO-SRST-MIB", "csrstTransferSystem"),
        ("CISCO-SRST-MIB", "csrstDateFormat"),
        ("CISCO-SRST-MIB", "csrstTimeFormat"),
        ("CISCO-SRST-MIB", "csrstInterdigitTo"),
        ("CISCO-SRST-MIB", "csrstBusyTo"),
        ("CISCO-SRST-MIB", "csrstAlertTo"),
        ("CISCO-SRST-MIB", "csrstXlateCalledNumber"),
        ("CISCO-SRST-MIB", "csrstXlateCallingNumber"),
        ("CISCO-SRST-MIB", "csrstAliasTag"),
        ("CISCO-SRST-MIB", "csrstAliasNumPattern"),
        ("CISCO-SRST-MIB", "csrstAliasAltNumber"),
        ("CISCO-SRST-MIB", "csrstAliasPreference"),
        ("CISCO-SRST-MIB", "csrstAliasHuntStopEnabled"),
        ("CISCO-SRST-MIB", "csrstAccessCodeType"),
        ("CISCO-SRST-MIB", "csrstAccessCode"),
        ("CISCO-SRST-MIB", "csrstAccessCodeDIDEnabled"),
        ("CISCO-SRST-MIB", "csrstLimitDNType"),
        ("CISCO-SRST-MIB", "csrstLimitDN"),
        ("CISCO-SRST-MIB", "csrstNotificationEnabled"),
        ("CISCO-SRST-MIB", "csrstUserLocaleInfoRev1"))
)
if mibBuilder.loadTexts:
    csrstConfGroupRev1.setStatus("current")


# Notification objects

csrstStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 0, 1)
)
csrstStateChange.setObjects(
      *(("CISCO-SRST-MIB", "csrstSysNotifSeverity"),
        ("CISCO-SRST-MIB", "csrstState"),
        ("CISCO-SRST-MIB", "csrstSysNotifReason"))
)
if mibBuilder.loadTexts:
    csrstStateChange.setStatus(
        "current"
    )

csrstFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 0, 2)
)
csrstFailNotif.setObjects(
      *(("CISCO-SRST-MIB", "csrstSysNotifSeverity"),
        ("CISCO-SRST-MIB", "csrstSysNotifReason"))
)
if mibBuilder.loadTexts:
    csrstFailNotif.setStatus(
        "current"
    )

csrstSipPhoneUnRegThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 0, 3)
)
csrstSipPhoneUnRegThresholdExceed.setObjects(
      *(("CISCO-SRST-MIB", "csrstSipPhoneUnRegThreshold"),
        ("CISCO-SRST-MIB", "csrstSipPhoneCurrentRegistered"))
)
if mibBuilder.loadTexts:
    csrstSipPhoneUnRegThresholdExceed.setStatus(
        "current"
    )

csrstSipPhoneRegFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 0, 4)
)
csrstSipPhoneRegFailed.setObjects(
    ("CISCO-SRST-MIB", "csrstSipEndpointIpAddress")
)
if mibBuilder.loadTexts:
    csrstSipPhoneRegFailed.setStatus(
        "current"
    )

csrstConferenceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 0, 5)
)
csrstConferenceFailed.setObjects(
    ("CISCO-SRST-MIB", "csrstMaxConferences")
)
if mibBuilder.loadTexts:
    csrstConferenceFailed.setStatus(
        "current"
    )


# Notifications groups

csrstMIBNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 2, 5)
)
csrstMIBNotifsGroup.setObjects(
      *(("CISCO-SRST-MIB", "csrstStateChange"),
        ("CISCO-SRST-MIB", "csrstFailNotif"),
        ("CISCO-SRST-MIB", "csrstSipPhoneUnRegThresholdExceed"),
        ("CISCO-SRST-MIB", "csrstSipPhoneRegFailed"),
        ("CISCO-SRST-MIB", "csrstConferenceFailed"))
)
if mibBuilder.loadTexts:
    csrstMIBNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSrstMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSrstMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSrstMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 441, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSrstMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SRST-MIB",
    **{"SrstOperType": SrstOperType,
       "ciscoSrstMIB": ciscoSrstMIB,
       "ciscoSrstMIBNotifications": ciscoSrstMIBNotifications,
       "csrstStateChange": csrstStateChange,
       "csrstFailNotif": csrstFailNotif,
       "csrstSipPhoneUnRegThresholdExceed": csrstSipPhoneUnRegThresholdExceed,
       "csrstSipPhoneRegFailed": csrstSipPhoneRegFailed,
       "csrstConferenceFailed": csrstConferenceFailed,
       "ciscoSrstMIBObjects": ciscoSrstMIBObjects,
       "csrstGlobal": csrstGlobal,
       "csrstConf": csrstConf,
       "csrstEnabled": csrstEnabled,
       "csrstVersion": csrstVersion,
       "csrstIPAddressType": csrstIPAddressType,
       "csrstIPAddress": csrstIPAddress,
       "csrstPortNumber": csrstPortNumber,
       "csrstMaxConferences": csrstMaxConferences,
       "csrstMaxEphones": csrstMaxEphones,
       "csrstMaxDN": csrstMaxDN,
       "csrstSipPhoneUnRegThreshold": csrstSipPhoneUnRegThreshold,
       "csrstCallFwdNoAnswer": csrstCallFwdNoAnswer,
       "csrstCallFwdNoAnswerTo": csrstCallFwdNoAnswerTo,
       "csrstCallFwdBusy": csrstCallFwdBusy,
       "csrstMohFilename": csrstMohFilename,
       "csrstMohMulticastAddrType": csrstMohMulticastAddrType,
       "csrstMohMulticastAddr": csrstMohMulticastAddr,
       "csrstMohMulticastPort": csrstMohMulticastPort,
       "csrstVoiceMailNumber": csrstVoiceMailNumber,
       "csrstSystemMessagePrimary": csrstSystemMessagePrimary,
       "csrstSystemMessageSecondary": csrstSystemMessageSecondary,
       "csrstScriptName": csrstScriptName,
       "csrstSecondaryDialTone": csrstSecondaryDialTone,
       "csrstTransferSystem": csrstTransferSystem,
       "csrstUserLocaleInfo": csrstUserLocaleInfo,
       "csrstDateFormat": csrstDateFormat,
       "csrstTimeFormat": csrstTimeFormat,
       "csrstInterdigitTo": csrstInterdigitTo,
       "csrstBusyTo": csrstBusyTo,
       "csrstAlertTo": csrstAlertTo,
       "csrstXlateCalledNumber": csrstXlateCalledNumber,
       "csrstXlateCallingNumber": csrstXlateCallingNumber,
       "csrstAliasTable": csrstAliasTable,
       "csrstAliasEntry": csrstAliasEntry,
       "csrstAliasIndex": csrstAliasIndex,
       "csrstAliasTag": csrstAliasTag,
       "csrstAliasNumPattern": csrstAliasNumPattern,
       "csrstAliasAltNumber": csrstAliasAltNumber,
       "csrstAliasPreference": csrstAliasPreference,
       "csrstAliasHuntStopEnabled": csrstAliasHuntStopEnabled,
       "csrstAccessCodeTable": csrstAccessCodeTable,
       "csrstAccessCodeEntry": csrstAccessCodeEntry,
       "csrstAccessCodeType": csrstAccessCodeType,
       "csrstAccessCode": csrstAccessCode,
       "csrstAccessCodeDIDEnabled": csrstAccessCodeDIDEnabled,
       "csrstLimitDNTable": csrstLimitDNTable,
       "csrstLimitDNEntry": csrstLimitDNEntry,
       "csrstLimitDNType": csrstLimitDNType,
       "csrstLimitDN": csrstLimitDN,
       "csrstNotificationEnabled": csrstNotificationEnabled,
       "csrstUserLocaleInfoRev1": csrstUserLocaleInfoRev1,
       "csrstActiveStats": csrstActiveStats,
       "csrstState": csrstState,
       "csrstSipPhoneCurrentRegistered": csrstSipPhoneCurrentRegistered,
       "csrstSipCallLegs": csrstSipCallLegs,
       "csrstTotalUpTime": csrstTotalUpTime,
       "csrstSipConf": csrstSipConf,
       "csrstSipRegSrvExpMax": csrstSipRegSrvExpMax,
       "csrstSipRegSrvExpMin": csrstSipRegSrvExpMin,
       "csrstSipIp2IpGlobalEnabled": csrstSipIp2IpGlobalEnabled,
       "csrstSipSend300MultSupport": csrstSipSend300MultSupport,
       "csrstSipVoRegPoolTable": csrstSipVoRegPoolTable,
       "csrstSipVoRegPoolEntry": csrstSipVoRegPoolEntry,
       "csrstSipVoRegPoolTag": csrstSipVoRegPoolTag,
       "csrstSipNetId": csrstSipNetId,
       "csrstSipVoRegPoolIpAddrType": csrstSipVoRegPoolIpAddrType,
       "csrstSipNetMask": csrstSipNetMask,
       "csrstSipProxySrvIpAddr": csrstSipProxySrvIpAddr,
       "csrstSipProxySrvPref": csrstSipProxySrvPref,
       "csrstSipProxySrvMonitor": csrstSipProxySrvMonitor,
       "csrstSipProxySrvAltIpAddr": csrstSipProxySrvAltIpAddr,
       "csrstSipDefaultPreference": csrstSipDefaultPreference,
       "csrstSipVoRegPoolAppl": csrstSipVoRegPoolAppl,
       "csrstSipVoRegNumberListTable": csrstSipVoRegNumberListTable,
       "csrstSipVoRegNumberListEntry": csrstSipVoRegNumberListEntry,
       "csrstSipVoRegNumberListIndex": csrstSipVoRegNumberListIndex,
       "csrstSipVoRegNumberListTag": csrstSipVoRegNumberListTag,
       "csrstSipVoRegNumberPattern": csrstSipVoRegNumberPattern,
       "csrstSipVoRegNumberPref": csrstSipVoRegNumberPref,
       "csrstSipVoRegNumberHuntstopEnabled": csrstSipVoRegNumberHuntstopEnabled,
       "csrstSipEndpointTable": csrstSipEndpointTable,
       "csrstSipEndpointEntry": csrstSipEndpointEntry,
       "csrstSipEndpointTag": csrstSipEndpointTag,
       "csrstSipVoRegPoolEdptTag": csrstSipVoRegPoolEdptTag,
       "csrstSipEndpointIpAddrType": csrstSipEndpointIpAddrType,
       "csrstSipEndpointIpAddress": csrstSipEndpointIpAddress,
       "csrstSipEndpointDN": csrstSipEndpointDN,
       "ciscoSrstMIBConformance": ciscoSrstMIBConformance,
       "ciscoSrstMIBCompliances": ciscoSrstMIBCompliances,
       "ciscoSrstMIBCompliance": ciscoSrstMIBCompliance,
       "ciscoSrstMIBComplianceRev1": ciscoSrstMIBComplianceRev1,
       "ciscoSrstMIBGroups": ciscoSrstMIBGroups,
       "csrstConfGroup": csrstConfGroup,
       "csrstNotifInfoGroup": csrstNotifInfoGroup,
       "csrstSysNotifSeverity": csrstSysNotifSeverity,
       "csrstSysNotifReason": csrstSysNotifReason,
       "csrstActiveStatsGroup": csrstActiveStatsGroup,
       "csrstSipConfGroup": csrstSipConfGroup,
       "csrstMIBNotifsGroup": csrstMIBNotifsGroup,
       "csrstConfGroupRev1": csrstConfGroupRev1}
)
