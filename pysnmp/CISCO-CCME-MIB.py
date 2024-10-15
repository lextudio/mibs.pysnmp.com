# SNMP MIB module (CISCO-CCME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CCME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:08 2024
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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCcmeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 439)
)
ciscoCcmeMIB.setRevisions(
        ("2010-10-13 00:00",
         "2010-04-01 00:00",
         "2005-05-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CcmeDigitPatternString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )



class CcmeNightServiceCodeString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCcmeMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCcmeMIBNotifs = _CiscoCcmeMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 0)
)
_CcmeMIBNotifications_ObjectIdentity = ObjectIdentity
ccmeMIBNotifications = _CcmeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 0, 0)
)
_CiscoCcmeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCcmeMIBObjects = _CiscoCcmeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1)
)
_CcmeConfig_ObjectIdentity = ObjectIdentity
ccmeConfig = _CcmeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1)
)
_CcmeEnabled_Type = TruthValue
_CcmeEnabled_Object = MibScalar
ccmeEnabled = _CcmeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 1),
    _CcmeEnabled_Type()
)
ccmeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEnabled.setStatus("current")
_CcmeVersion_Type = SnmpAdminString
_CcmeVersion_Object = MibScalar
ccmeVersion = _CcmeVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 2),
    _CcmeVersion_Type()
)
ccmeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeVersion.setStatus("current")
_CcmeIPAddressType_Type = InetAddressType
_CcmeIPAddressType_Object = MibScalar
ccmeIPAddressType = _CcmeIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 3),
    _CcmeIPAddressType_Type()
)
ccmeIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeIPAddressType.setStatus("current")
_CcmeIPAddress_Type = InetAddress
_CcmeIPAddress_Object = MibScalar
ccmeIPAddress = _CcmeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 4),
    _CcmeIPAddress_Type()
)
ccmeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeIPAddress.setStatus("current")


class _CcmePortNumber_Type(InetPortNumber):
    """Custom type ccmePortNumber based on InetPortNumber"""
    defaultValue = 2000

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 9999),
    )


_CcmePortNumber_Type.__name__ = "InetPortNumber"
_CcmePortNumber_Object = MibScalar
ccmePortNumber = _CcmePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 5),
    _CcmePortNumber_Type()
)
ccmePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmePortNumber.setStatus("current")


class _CcmeMaxEphones_Type(Integer32):
    """Custom type ccmeMaxEphones based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_CcmeMaxEphones_Type.__name__ = "Integer32"
_CcmeMaxEphones_Object = MibScalar
ccmeMaxEphones = _CcmeMaxEphones_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 6),
    _CcmeMaxEphones_Type()
)
ccmeMaxEphones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMaxEphones.setStatus("current")


class _CcmeMaxDirectoryNumber_Type(Integer32):
    """Custom type ccmeMaxDirectoryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 288),
    )


_CcmeMaxDirectoryNumber_Type.__name__ = "Integer32"
_CcmeMaxDirectoryNumber_Object = MibScalar
ccmeMaxDirectoryNumber = _CcmeMaxDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 7),
    _CcmeMaxDirectoryNumber_Type()
)
ccmeMaxDirectoryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMaxDirectoryNumber.setStatus("current")


class _CcmeMaxConferences_Type(Integer32):
    """Custom type ccmeMaxConferences based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CcmeMaxConferences_Type.__name__ = "Integer32"
_CcmeMaxConferences_Object = MibScalar
ccmeMaxConferences = _CcmeMaxConferences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 8),
    _CcmeMaxConferences_Type()
)
ccmeMaxConferences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMaxConferences.setStatus("current")


class _CcmeMaxRedirect_Type(Integer32):
    """Custom type ccmeMaxRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_CcmeMaxRedirect_Type.__name__ = "Integer32"
_CcmeMaxRedirect_Object = MibScalar
ccmeMaxRedirect = _CcmeMaxRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 9),
    _CcmeMaxRedirect_Type()
)
ccmeMaxRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMaxRedirect.setStatus("current")


class _CcmeScriptName_Type(SnmpAdminString):
    """Custom type ccmeScriptName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcmeScriptName_Type.__name__ = "SnmpAdminString"
_CcmeScriptName_Object = MibScalar
ccmeScriptName = _CcmeScriptName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 10),
    _CcmeScriptName_Type()
)
ccmeScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeScriptName.setStatus("current")


class _CcmeVoiceMailNumber_Type(SnmpAdminString):
    """Custom type ccmeVoiceMailNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcmeVoiceMailNumber_Type.__name__ = "SnmpAdminString"
_CcmeVoiceMailNumber_Object = MibScalar
ccmeVoiceMailNumber = _CcmeVoiceMailNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 11),
    _CcmeVoiceMailNumber_Type()
)
ccmeVoiceMailNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeVoiceMailNumber.setStatus("current")
_CcmeMwiRelay_Type = TruthValue
_CcmeMwiRelay_Object = MibScalar
ccmeMwiRelay = _CcmeMwiRelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 12),
    _CcmeMwiRelay_Type()
)
ccmeMwiRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMwiRelay.setStatus("current")


class _CcmeMwiExpires_Type(Integer32):
    """Custom type ccmeMwiExpires based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 99999),
    )


_CcmeMwiExpires_Type.__name__ = "Integer32"
_CcmeMwiExpires_Object = MibScalar
ccmeMwiExpires = _CcmeMwiExpires_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 13),
    _CcmeMwiExpires_Type()
)
ccmeMwiExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMwiExpires.setStatus("current")
if mibBuilder.loadTexts:
    ccmeMwiExpires.setUnits("seconds")


class _CcmeTransferSystem_Type(Integer32):
    """Custom type ccmeTransferSystem based on Integer32"""
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
          ("fullBlind", 3),
          ("fullConsult", 4),
          ("localConsult", 2))
    )


_CcmeTransferSystem_Type.__name__ = "Integer32"
_CcmeTransferSystem_Object = MibScalar
ccmeTransferSystem = _CcmeTransferSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 14),
    _CcmeTransferSystem_Type()
)
ccmeTransferSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeTransferSystem.setStatus("current")


class _CcmeTimeFormat_Type(Integer32):
    """Custom type ccmeTimeFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twelve", 1),
          ("twentyfour", 2))
    )


_CcmeTimeFormat_Type.__name__ = "Integer32"
_CcmeTimeFormat_Object = MibScalar
ccmeTimeFormat = _CcmeTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 15),
    _CcmeTimeFormat_Type()
)
ccmeTimeFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeTimeFormat.setStatus("current")


class _CcmeDateFormat_Type(Integer32):
    """Custom type ccmeDateFormat based on Integer32"""
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
          ("yyddmm", 4),
          ("yymmdd", 3))
    )


_CcmeDateFormat_Type.__name__ = "Integer32"
_CcmeDateFormat_Object = MibScalar
ccmeDateFormat = _CcmeDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 16),
    _CcmeDateFormat_Type()
)
ccmeDateFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeDateFormat.setStatus("current")
_CcmeUrlforServicesBtn_Type = SnmpAdminString
_CcmeUrlforServicesBtn_Object = MibScalar
ccmeUrlforServicesBtn = _CcmeUrlforServicesBtn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 17),
    _CcmeUrlforServicesBtn_Type()
)
ccmeUrlforServicesBtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeUrlforServicesBtn.setStatus("current")
_CcmeUrlforDirectoriesBtn_Type = SnmpAdminString
_CcmeUrlforDirectoriesBtn_Object = MibScalar
ccmeUrlforDirectoriesBtn = _CcmeUrlforDirectoriesBtn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 18),
    _CcmeUrlforDirectoriesBtn_Type()
)
ccmeUrlforDirectoriesBtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeUrlforDirectoriesBtn.setStatus("current")
_CcmeMohFlashFile_Type = SnmpAdminString
_CcmeMohFlashFile_Object = MibScalar
ccmeMohFlashFile = _CcmeMohFlashFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 19),
    _CcmeMohFlashFile_Type()
)
ccmeMohFlashFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMohFlashFile.setStatus("current")
_CcmeMohMulticastFromFlashEnabled_Type = TruthValue
_CcmeMohMulticastFromFlashEnabled_Object = MibScalar
ccmeMohMulticastFromFlashEnabled = _CcmeMohMulticastFromFlashEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 20),
    _CcmeMohMulticastFromFlashEnabled_Type()
)
ccmeMohMulticastFromFlashEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMohMulticastFromFlashEnabled.setStatus("current")
_CcmeMohFlashMulticastIPAddr_Type = InetAddress
_CcmeMohFlashMulticastIPAddr_Object = MibScalar
ccmeMohFlashMulticastIPAddr = _CcmeMohFlashMulticastIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 21),
    _CcmeMohFlashMulticastIPAddr_Type()
)
ccmeMohFlashMulticastIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMohFlashMulticastIPAddr.setStatus("current")
_CcmeMohFlashMulticastPortNum_Type = InetPortNumber
_CcmeMohFlashMulticastPortNum_Object = MibScalar
ccmeMohFlashMulticastPortNum = _CcmeMohFlashMulticastPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 22),
    _CcmeMohFlashMulticastPortNum_Type()
)
ccmeMohFlashMulticastPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMohFlashMulticastPortNum.setStatus("current")
_CcmePhoneFirmwareTable_Object = MibTable
ccmePhoneFirmwareTable = _CcmePhoneFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 23)
)
if mibBuilder.loadTexts:
    ccmePhoneFirmwareTable.setStatus("current")
_CcmePhoneFirmwareEntry_Object = MibTableRow
ccmePhoneFirmwareEntry = _CcmePhoneFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 23, 1)
)
ccmePhoneFirmwareEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmePhoneFirmwareIndex"),
)
if mibBuilder.loadTexts:
    ccmePhoneFirmwareEntry.setStatus("current")


class _CcmePhoneFirmwareIndex_Type(Integer32):
    """Custom type ccmePhoneFirmwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcmePhoneFirmwareIndex_Type.__name__ = "Integer32"
_CcmePhoneFirmwareIndex_Object = MibTableColumn
ccmePhoneFirmwareIndex = _CcmePhoneFirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 23, 1, 1),
    _CcmePhoneFirmwareIndex_Type()
)
ccmePhoneFirmwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmePhoneFirmwareIndex.setStatus("current")
_CcmePhoneType_Type = SnmpAdminString
_CcmePhoneType_Object = MibTableColumn
ccmePhoneType = _CcmePhoneType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 23, 1, 2),
    _CcmePhoneType_Type()
)
ccmePhoneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmePhoneType.setStatus("current")
_CcmePhoneFirmwareRev_Type = SnmpAdminString
_CcmePhoneFirmwareRev_Object = MibTableColumn
ccmePhoneFirmwareRev = _CcmePhoneFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 23, 1, 3),
    _CcmePhoneFirmwareRev_Type()
)
ccmePhoneFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmePhoneFirmwareRev.setStatus("current")
_CcmeTransferPatternTable_Object = MibTable
ccmeTransferPatternTable = _CcmeTransferPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 24)
)
if mibBuilder.loadTexts:
    ccmeTransferPatternTable.setStatus("current")
_CcmeTransferPatternEntry_Object = MibTableRow
ccmeTransferPatternEntry = _CcmeTransferPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 24, 1)
)
ccmeTransferPatternEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeTransferPatternIndex"),
)
if mibBuilder.loadTexts:
    ccmeTransferPatternEntry.setStatus("current")


class _CcmeTransferPatternIndex_Type(Integer32):
    """Custom type ccmeTransferPatternIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CcmeTransferPatternIndex_Type.__name__ = "Integer32"
_CcmeTransferPatternIndex_Object = MibTableColumn
ccmeTransferPatternIndex = _CcmeTransferPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 24, 1, 1),
    _CcmeTransferPatternIndex_Type()
)
ccmeTransferPatternIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeTransferPatternIndex.setStatus("current")
_CcmeTransferPattern_Type = SnmpAdminString
_CcmeTransferPattern_Object = MibTableColumn
ccmeTransferPattern = _CcmeTransferPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 24, 1, 2),
    _CcmeTransferPattern_Type()
)
ccmeTransferPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeTransferPattern.setStatus("current")


class _CcmeTransferPatternType_Type(Integer32):
    """Custom type ccmeTransferPatternType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blind", 1),
          ("h4502", 2))
    )


_CcmeTransferPatternType_Type.__name__ = "Integer32"
_CcmeTransferPatternType_Object = MibTableColumn
ccmeTransferPatternType = _CcmeTransferPatternType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 24, 1, 3),
    _CcmeTransferPatternType_Type()
)
ccmeTransferPatternType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeTransferPatternType.setStatus("current")
_CcmeWebGUIEditEnabled_Type = TruthValue
_CcmeWebGUIEditEnabled_Object = MibScalar
ccmeWebGUIEditEnabled = _CcmeWebGUIEditEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 25),
    _CcmeWebGUIEditEnabled_Type()
)
ccmeWebGUIEditEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeWebGUIEditEnabled.setStatus("current")
_CcmeWebGUITimeEnabled_Type = TruthValue
_CcmeWebGUITimeEnabled_Object = MibScalar
ccmeWebGUITimeEnabled = _CcmeWebGUITimeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 26),
    _CcmeWebGUITimeEnabled_Type()
)
ccmeWebGUITimeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeWebGUITimeEnabled.setStatus("current")
_CcmeAfterHrsBlockPatternTable_Object = MibTable
ccmeAfterHrsBlockPatternTable = _CcmeAfterHrsBlockPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 27)
)
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockPatternTable.setStatus("current")
_CcmeAfterHrsBlockPatternEntry_Object = MibTableRow
ccmeAfterHrsBlockPatternEntry = _CcmeAfterHrsBlockPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 27, 1)
)
ccmeAfterHrsBlockPatternEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeAfterHrsBlockPatternTag"),
)
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockPatternEntry.setStatus("current")


class _CcmeAfterHrsBlockPatternTag_Type(Integer32):
    """Custom type ccmeAfterHrsBlockPatternTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CcmeAfterHrsBlockPatternTag_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockPatternTag_Object = MibTableColumn
ccmeAfterHrsBlockPatternTag = _CcmeAfterHrsBlockPatternTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 27, 1, 1),
    _CcmeAfterHrsBlockPatternTag_Type()
)
ccmeAfterHrsBlockPatternTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockPatternTag.setStatus("current")
_CcmeAfterHrsBlockPattern_Type = CcmeDigitPatternString
_CcmeAfterHrsBlockPattern_Object = MibTableColumn
ccmeAfterHrsBlockPattern = _CcmeAfterHrsBlockPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 27, 1, 2),
    _CcmeAfterHrsBlockPattern_Type()
)
ccmeAfterHrsBlockPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockPattern.setStatus("current")
_CcmeAfterHrsBlockPatternAllTime_Type = TruthValue
_CcmeAfterHrsBlockPatternAllTime_Object = MibTableColumn
ccmeAfterHrsBlockPatternAllTime = _CcmeAfterHrsBlockPatternAllTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 27, 1, 3),
    _CcmeAfterHrsBlockPatternAllTime_Type()
)
ccmeAfterHrsBlockPatternAllTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockPatternAllTime.setStatus("current")
_CcmeAfterHrsBlockDateTable_Object = MibTable
ccmeAfterHrsBlockDateTable = _CcmeAfterHrsBlockDateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 28)
)
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDateTable.setStatus("current")
_CcmeAfterHrsBlockDateEntry_Object = MibTableRow
ccmeAfterHrsBlockDateEntry = _CcmeAfterHrsBlockDateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 28, 1)
)
ccmeAfterHrsBlockDateEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeAfterHrsBlockDateIndex"),
)
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDateEntry.setStatus("current")


class _CcmeAfterHrsBlockDateIndex_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CcmeAfterHrsBlockDateIndex_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDateIndex_Object = MibTableColumn
ccmeAfterHrsBlockDateIndex = _CcmeAfterHrsBlockDateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 28, 1, 1),
    _CcmeAfterHrsBlockDateIndex_Type()
)
ccmeAfterHrsBlockDateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDateIndex.setStatus("current")


class _CcmeAfterHrsBlockDateMonth_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDateMonth based on Integer32"""
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
        *(("apr", 4),
          ("aug", 8),
          ("dec", 12),
          ("feb", 2),
          ("jan", 1),
          ("jul", 7),
          ("jun", 6),
          ("mar", 3),
          ("may", 5),
          ("nov", 11),
          ("oct", 10),
          ("sep", 9))
    )


_CcmeAfterHrsBlockDateMonth_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDateMonth_Object = MibTableColumn
ccmeAfterHrsBlockDateMonth = _CcmeAfterHrsBlockDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 28, 1, 2),
    _CcmeAfterHrsBlockDateMonth_Type()
)
ccmeAfterHrsBlockDateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDateMonth.setStatus("current")


class _CcmeAfterHrsBlockDate_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcmeAfterHrsBlockDate_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDate_Object = MibTableColumn
ccmeAfterHrsBlockDate = _CcmeAfterHrsBlockDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 28, 1, 3),
    _CcmeAfterHrsBlockDate_Type()
)
ccmeAfterHrsBlockDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDate.setStatus("current")


class _CcmeAfterHrsBlockDateStartHour_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDateStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CcmeAfterHrsBlockDateStartHour_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDateStartHour_Object = MibTableColumn
ccmeAfterHrsBlockDateStartHour = _CcmeAfterHrsBlockDateStartHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 28, 1, 4),
    _CcmeAfterHrsBlockDateStartHour_Type()
)
ccmeAfterHrsBlockDateStartHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDateStartHour.setStatus("current")


class _CcmeAfterHrsBlockDateStartMin_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDateStartMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CcmeAfterHrsBlockDateStartMin_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDateStartMin_Object = MibTableColumn
ccmeAfterHrsBlockDateStartMin = _CcmeAfterHrsBlockDateStartMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 28, 1, 5),
    _CcmeAfterHrsBlockDateStartMin_Type()
)
ccmeAfterHrsBlockDateStartMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDateStartMin.setStatus("current")


class _CcmeAfterHrsBlockDateStopHour_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDateStopHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CcmeAfterHrsBlockDateStopHour_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDateStopHour_Object = MibTableColumn
ccmeAfterHrsBlockDateStopHour = _CcmeAfterHrsBlockDateStopHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 28, 1, 6),
    _CcmeAfterHrsBlockDateStopHour_Type()
)
ccmeAfterHrsBlockDateStopHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDateStopHour.setStatus("current")


class _CcmeAfterHrsBlockDateStopMin_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDateStopMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CcmeAfterHrsBlockDateStopMin_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDateStopMin_Object = MibTableColumn
ccmeAfterHrsBlockDateStopMin = _CcmeAfterHrsBlockDateStopMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 28, 1, 7),
    _CcmeAfterHrsBlockDateStopMin_Type()
)
ccmeAfterHrsBlockDateStopMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDateStopMin.setStatus("current")
_CcmeAfterHrsBlockDayTable_Object = MibTable
ccmeAfterHrsBlockDayTable = _CcmeAfterHrsBlockDayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 29)
)
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDayTable.setStatus("current")
_CcmeAfterHrsBlockDayEntry_Object = MibTableRow
ccmeAfterHrsBlockDayEntry = _CcmeAfterHrsBlockDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 29, 1)
)
ccmeAfterHrsBlockDayEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeAfterHrsBlockDayIndex"),
)
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDayEntry.setStatus("current")


class _CcmeAfterHrsBlockDayIndex_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CcmeAfterHrsBlockDayIndex_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDayIndex_Object = MibTableColumn
ccmeAfterHrsBlockDayIndex = _CcmeAfterHrsBlockDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 29, 1, 1),
    _CcmeAfterHrsBlockDayIndex_Type()
)
ccmeAfterHrsBlockDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDayIndex.setStatus("current")


class _CcmeAfterHrsBlockDay_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDay based on Integer32"""
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
        *(("fri", 6),
          ("mon", 2),
          ("sat", 7),
          ("sun", 1),
          ("thu", 5),
          ("tue", 3),
          ("wed", 4))
    )


_CcmeAfterHrsBlockDay_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDay_Object = MibTableColumn
ccmeAfterHrsBlockDay = _CcmeAfterHrsBlockDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 29, 1, 2),
    _CcmeAfterHrsBlockDay_Type()
)
ccmeAfterHrsBlockDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDay.setStatus("current")


class _CcmeAfterHrsBlockDayStartHour_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDayStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CcmeAfterHrsBlockDayStartHour_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDayStartHour_Object = MibTableColumn
ccmeAfterHrsBlockDayStartHour = _CcmeAfterHrsBlockDayStartHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 29, 1, 3),
    _CcmeAfterHrsBlockDayStartHour_Type()
)
ccmeAfterHrsBlockDayStartHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDayStartHour.setStatus("current")


class _CcmeAfterHrsBlockDayStartMin_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDayStartMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CcmeAfterHrsBlockDayStartMin_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDayStartMin_Object = MibTableColumn
ccmeAfterHrsBlockDayStartMin = _CcmeAfterHrsBlockDayStartMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 29, 1, 4),
    _CcmeAfterHrsBlockDayStartMin_Type()
)
ccmeAfterHrsBlockDayStartMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDayStartMin.setStatus("current")


class _CcmeAfterHrsBlockDayStopHour_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDayStopHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CcmeAfterHrsBlockDayStopHour_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDayStopHour_Object = MibTableColumn
ccmeAfterHrsBlockDayStopHour = _CcmeAfterHrsBlockDayStopHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 29, 1, 5),
    _CcmeAfterHrsBlockDayStopHour_Type()
)
ccmeAfterHrsBlockDayStopHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDayStopHour.setStatus("current")


class _CcmeAfterHrsBlockDayStopMin_Type(Integer32):
    """Custom type ccmeAfterHrsBlockDayStopMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CcmeAfterHrsBlockDayStopMin_Type.__name__ = "Integer32"
_CcmeAfterHrsBlockDayStopMin_Object = MibTableColumn
ccmeAfterHrsBlockDayStopMin = _CcmeAfterHrsBlockDayStopMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 29, 1, 6),
    _CcmeAfterHrsBlockDayStopMin_Type()
)
ccmeAfterHrsBlockDayStopMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAfterHrsBlockDayStopMin.setStatus("current")
_CcmeNightServiceCode_Type = CcmeNightServiceCodeString
_CcmeNightServiceCode_Object = MibScalar
ccmeNightServiceCode = _CcmeNightServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 30),
    _CcmeNightServiceCode_Type()
)
ccmeNightServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceCode.setStatus("current")
_CcmeNightServiceDateTable_Object = MibTable
ccmeNightServiceDateTable = _CcmeNightServiceDateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 31)
)
if mibBuilder.loadTexts:
    ccmeNightServiceDateTable.setStatus("current")
_CcmeNightServiceDateEntry_Object = MibTableRow
ccmeNightServiceDateEntry = _CcmeNightServiceDateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 31, 1)
)
ccmeNightServiceDateEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeNightServiceDateIndex"),
)
if mibBuilder.loadTexts:
    ccmeNightServiceDateEntry.setStatus("current")


class _CcmeNightServiceDateIndex_Type(Integer32):
    """Custom type ccmeNightServiceDateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcmeNightServiceDateIndex_Type.__name__ = "Integer32"
_CcmeNightServiceDateIndex_Object = MibTableColumn
ccmeNightServiceDateIndex = _CcmeNightServiceDateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 31, 1, 1),
    _CcmeNightServiceDateIndex_Type()
)
ccmeNightServiceDateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeNightServiceDateIndex.setStatus("current")


class _CcmeNightServiceDateMonth_Type(Integer32):
    """Custom type ccmeNightServiceDateMonth based on Integer32"""
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
        *(("apr", 4),
          ("aug", 8),
          ("dec", 12),
          ("feb", 2),
          ("jan", 1),
          ("jul", 7),
          ("jun", 6),
          ("mar", 3),
          ("may", 5),
          ("nov", 11),
          ("oct", 10),
          ("sep", 9))
    )


_CcmeNightServiceDateMonth_Type.__name__ = "Integer32"
_CcmeNightServiceDateMonth_Object = MibTableColumn
ccmeNightServiceDateMonth = _CcmeNightServiceDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 31, 1, 2),
    _CcmeNightServiceDateMonth_Type()
)
ccmeNightServiceDateMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceDateMonth.setStatus("current")


class _CcmeNightServiceDate_Type(Integer32):
    """Custom type ccmeNightServiceDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CcmeNightServiceDate_Type.__name__ = "Integer32"
_CcmeNightServiceDate_Object = MibTableColumn
ccmeNightServiceDate = _CcmeNightServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 31, 1, 3),
    _CcmeNightServiceDate_Type()
)
ccmeNightServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceDate.setStatus("current")


class _CcmeNightServiceDateStartHour_Type(Integer32):
    """Custom type ccmeNightServiceDateStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CcmeNightServiceDateStartHour_Type.__name__ = "Integer32"
_CcmeNightServiceDateStartHour_Object = MibTableColumn
ccmeNightServiceDateStartHour = _CcmeNightServiceDateStartHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 31, 1, 4),
    _CcmeNightServiceDateStartHour_Type()
)
ccmeNightServiceDateStartHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceDateStartHour.setStatus("current")


class _CcmeNightServiceDateStartMin_Type(Integer32):
    """Custom type ccmeNightServiceDateStartMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CcmeNightServiceDateStartMin_Type.__name__ = "Integer32"
_CcmeNightServiceDateStartMin_Object = MibTableColumn
ccmeNightServiceDateStartMin = _CcmeNightServiceDateStartMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 31, 1, 5),
    _CcmeNightServiceDateStartMin_Type()
)
ccmeNightServiceDateStartMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceDateStartMin.setStatus("current")


class _CcmeNightServiceDateStopHour_Type(Integer32):
    """Custom type ccmeNightServiceDateStopHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CcmeNightServiceDateStopHour_Type.__name__ = "Integer32"
_CcmeNightServiceDateStopHour_Object = MibTableColumn
ccmeNightServiceDateStopHour = _CcmeNightServiceDateStopHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 31, 1, 6),
    _CcmeNightServiceDateStopHour_Type()
)
ccmeNightServiceDateStopHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceDateStopHour.setStatus("current")


class _CcmeNightServiceDateStopMin_Type(Integer32):
    """Custom type ccmeNightServiceDateStopMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CcmeNightServiceDateStopMin_Type.__name__ = "Integer32"
_CcmeNightServiceDateStopMin_Object = MibTableColumn
ccmeNightServiceDateStopMin = _CcmeNightServiceDateStopMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 31, 1, 7),
    _CcmeNightServiceDateStopMin_Type()
)
ccmeNightServiceDateStopMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceDateStopMin.setStatus("current")
_CcmeNightServiceDayTable_Object = MibTable
ccmeNightServiceDayTable = _CcmeNightServiceDayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 32)
)
if mibBuilder.loadTexts:
    ccmeNightServiceDayTable.setStatus("current")
_CcmeNightServiceDayEntry_Object = MibTableRow
ccmeNightServiceDayEntry = _CcmeNightServiceDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 32, 1)
)
ccmeNightServiceDayEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeNightServiceDayIndex"),
)
if mibBuilder.loadTexts:
    ccmeNightServiceDayEntry.setStatus("current")


class _CcmeNightServiceDayIndex_Type(Integer32):
    """Custom type ccmeNightServiceDayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CcmeNightServiceDayIndex_Type.__name__ = "Integer32"
_CcmeNightServiceDayIndex_Object = MibTableColumn
ccmeNightServiceDayIndex = _CcmeNightServiceDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 32, 1, 1),
    _CcmeNightServiceDayIndex_Type()
)
ccmeNightServiceDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeNightServiceDayIndex.setStatus("current")


class _CcmeNightServiceDay_Type(Integer32):
    """Custom type ccmeNightServiceDay based on Integer32"""
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
        *(("fri", 6),
          ("mon", 2),
          ("sat", 7),
          ("sun", 1),
          ("thu", 5),
          ("tue", 3),
          ("wed", 4))
    )


_CcmeNightServiceDay_Type.__name__ = "Integer32"
_CcmeNightServiceDay_Object = MibTableColumn
ccmeNightServiceDay = _CcmeNightServiceDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 32, 1, 2),
    _CcmeNightServiceDay_Type()
)
ccmeNightServiceDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceDay.setStatus("current")


class _CcmeNightServiceDayStartHour_Type(Integer32):
    """Custom type ccmeNightServiceDayStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CcmeNightServiceDayStartHour_Type.__name__ = "Integer32"
_CcmeNightServiceDayStartHour_Object = MibTableColumn
ccmeNightServiceDayStartHour = _CcmeNightServiceDayStartHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 32, 1, 3),
    _CcmeNightServiceDayStartHour_Type()
)
ccmeNightServiceDayStartHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceDayStartHour.setStatus("current")


class _CcmeNightServiceDayStartMin_Type(Integer32):
    """Custom type ccmeNightServiceDayStartMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CcmeNightServiceDayStartMin_Type.__name__ = "Integer32"
_CcmeNightServiceDayStartMin_Object = MibTableColumn
ccmeNightServiceDayStartMin = _CcmeNightServiceDayStartMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 32, 1, 4),
    _CcmeNightServiceDayStartMin_Type()
)
ccmeNightServiceDayStartMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceDayStartMin.setStatus("current")


class _CcmeNightServiceDayStopHour_Type(Integer32):
    """Custom type ccmeNightServiceDayStopHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CcmeNightServiceDayStopHour_Type.__name__ = "Integer32"
_CcmeNightServiceDayStopHour_Object = MibTableColumn
ccmeNightServiceDayStopHour = _CcmeNightServiceDayStopHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 32, 1, 5),
    _CcmeNightServiceDayStopHour_Type()
)
ccmeNightServiceDayStopHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceDayStopHour.setStatus("current")


class _CcmeNightServiceDayStopMin_Type(Integer32):
    """Custom type ccmeNightServiceDayStopMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_CcmeNightServiceDayStopMin_Type.__name__ = "Integer32"
_CcmeNightServiceDayStopMin_Object = MibTableColumn
ccmeNightServiceDayStopMin = _CcmeNightServiceDayStopMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 32, 1, 6),
    _CcmeNightServiceDayStopMin_Type()
)
ccmeNightServiceDayStopMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceDayStopMin.setStatus("current")
_CcmeFXOHookFlashEnabled_Type = TruthValue
_CcmeFXOHookFlashEnabled_Object = MibScalar
ccmeFXOHookFlashEnabled = _CcmeFXOHookFlashEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 33),
    _CcmeFXOHookFlashEnabled_Type()
)
ccmeFXOHookFlashEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeFXOHookFlashEnabled.setStatus("current")
_CcmeSecondaryDialTonePrefix_Type = CcmeDigitPatternString
_CcmeSecondaryDialTonePrefix_Object = MibScalar
ccmeSecondaryDialTonePrefix = _CcmeSecondaryDialTonePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 34),
    _CcmeSecondaryDialTonePrefix_Type()
)
ccmeSecondaryDialTonePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeSecondaryDialTonePrefix.setStatus("current")
_CcmeWebAdminSystemUser_Type = SnmpAdminString
_CcmeWebAdminSystemUser_Object = MibScalar
ccmeWebAdminSystemUser = _CcmeWebAdminSystemUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 35),
    _CcmeWebAdminSystemUser_Type()
)
ccmeWebAdminSystemUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeWebAdminSystemUser.setStatus("current")


class _CcmeWebAdminCustomerUser_Type(SnmpAdminString):
    """Custom type ccmeWebAdminCustomerUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcmeWebAdminCustomerUser_Type.__name__ = "SnmpAdminString"
_CcmeWebAdminCustomerUser_Object = MibScalar
ccmeWebAdminCustomerUser = _CcmeWebAdminCustomerUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 36),
    _CcmeWebAdminCustomerUser_Type()
)
ccmeWebAdminCustomerUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeWebAdminCustomerUser.setStatus("current")


class _CcmeSystemMessage_Type(SnmpAdminString):
    """Custom type ccmeSystemMessage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcmeSystemMessage_Type.__name__ = "SnmpAdminString"
_CcmeSystemMessage_Object = MibScalar
ccmeSystemMessage = _CcmeSystemMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 37),
    _CcmeSystemMessage_Type()
)
ccmeSystemMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeSystemMessage.setStatus("current")
_CcmeDialplanPatternTable_Object = MibTable
ccmeDialplanPatternTable = _CcmeDialplanPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 38)
)
if mibBuilder.loadTexts:
    ccmeDialplanPatternTable.setStatus("current")
_CcmeDialplanPatternEntry_Object = MibTableRow
ccmeDialplanPatternEntry = _CcmeDialplanPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 38, 1)
)
ccmeDialplanPatternEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeDialplanPatternIndex"),
)
if mibBuilder.loadTexts:
    ccmeDialplanPatternEntry.setStatus("current")


class _CcmeDialplanPatternIndex_Type(Integer32):
    """Custom type ccmeDialplanPatternIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CcmeDialplanPatternIndex_Type.__name__ = "Integer32"
_CcmeDialplanPatternIndex_Object = MibTableColumn
ccmeDialplanPatternIndex = _CcmeDialplanPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 38, 1, 1),
    _CcmeDialplanPatternIndex_Type()
)
ccmeDialplanPatternIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeDialplanPatternIndex.setStatus("current")


class _CcmeDialplanPatternTag_Type(Integer32):
    """Custom type ccmeDialplanPatternTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CcmeDialplanPatternTag_Type.__name__ = "Integer32"
_CcmeDialplanPatternTag_Object = MibTableColumn
ccmeDialplanPatternTag = _CcmeDialplanPatternTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 38, 1, 2),
    _CcmeDialplanPatternTag_Type()
)
ccmeDialplanPatternTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeDialplanPatternTag.setStatus("current")


class _CcmeDialplanExtLength_Type(Integer32):
    """Custom type ccmeDialplanExtLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CcmeDialplanExtLength_Type.__name__ = "Integer32"
_CcmeDialplanExtLength_Object = MibTableColumn
ccmeDialplanExtLength = _CcmeDialplanExtLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 38, 1, 3),
    _CcmeDialplanExtLength_Type()
)
ccmeDialplanExtLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeDialplanExtLength.setStatus("current")
_CcmeDialplanPattern_Type = CcmeDigitPatternString
_CcmeDialplanPattern_Object = MibTableColumn
ccmeDialplanPattern = _CcmeDialplanPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 38, 1, 4),
    _CcmeDialplanPattern_Type()
)
ccmeDialplanPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeDialplanPattern.setStatus("current")
_CcmeDialplanExtPattern_Type = CcmeDigitPatternString
_CcmeDialplanExtPattern_Object = MibTableColumn
ccmeDialplanExtPattern = _CcmeDialplanExtPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 38, 1, 5),
    _CcmeDialplanExtPattern_Type()
)
ccmeDialplanExtPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeDialplanExtPattern.setStatus("current")
_CcmeDialplanAllowRegiEnabled_Type = TruthValue
_CcmeDialplanAllowRegiEnabled_Object = MibTableColumn
ccmeDialplanAllowRegiEnabled = _CcmeDialplanAllowRegiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 38, 1, 6),
    _CcmeDialplanAllowRegiEnabled_Type()
)
ccmeDialplanAllowRegiEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeDialplanAllowRegiEnabled.setStatus("current")


class _CcmeKeepAliveTimeout_Type(Integer32):
    """Custom type ccmeKeepAliveTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_CcmeKeepAliveTimeout_Type.__name__ = "Integer32"
_CcmeKeepAliveTimeout_Object = MibScalar
ccmeKeepAliveTimeout = _CcmeKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 39),
    _CcmeKeepAliveTimeout_Type()
)
ccmeKeepAliveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeKeepAliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccmeKeepAliveTimeout.setUnits("seconds")


class _CcmeInterDigitTimeout_Type(Integer32):
    """Custom type ccmeInterDigitTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_CcmeInterDigitTimeout_Type.__name__ = "Integer32"
_CcmeInterDigitTimeout_Object = MibScalar
ccmeInterDigitTimeout = _CcmeInterDigitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 40),
    _CcmeInterDigitTimeout_Type()
)
ccmeInterDigitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeInterDigitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccmeInterDigitTimeout.setUnits("seconds")


class _CcmeBusyTimeout_Type(Integer32):
    """Custom type ccmeBusyTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CcmeBusyTimeout_Type.__name__ = "Integer32"
_CcmeBusyTimeout_Object = MibScalar
ccmeBusyTimeout = _CcmeBusyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 41),
    _CcmeBusyTimeout_Type()
)
ccmeBusyTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeBusyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccmeBusyTimeout.setUnits("seconds")


class _CcmeAlertTimeout_Type(Integer32):
    """Custom type ccmeAlertTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_CcmeAlertTimeout_Type.__name__ = "Integer32"
_CcmeAlertTimeout_Object = MibScalar
ccmeAlertTimeout = _CcmeAlertTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 42),
    _CcmeAlertTimeout_Type()
)
ccmeAlertTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeAlertTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccmeAlertTimeout.setUnits("seconds")
_CcmeEphoneConfTable_Object = MibTable
ccmeEphoneConfTable = _CcmeEphoneConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43)
)
if mibBuilder.loadTexts:
    ccmeEphoneConfTable.setStatus("current")
_CcmeEphoneConfEntry_Object = MibTableRow
ccmeEphoneConfEntry = _CcmeEphoneConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1)
)
ccmeEphoneConfEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeEphoneTag"),
)
if mibBuilder.loadTexts:
    ccmeEphoneConfEntry.setStatus("current")


class _CcmeEphoneTag_Type(Integer32):
    """Custom type ccmeEphoneTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CcmeEphoneTag_Type.__name__ = "Integer32"
_CcmeEphoneTag_Object = MibTableColumn
ccmeEphoneTag = _CcmeEphoneTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 1),
    _CcmeEphoneTag_Type()
)
ccmeEphoneTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeEphoneTag.setStatus("current")
_CcmeEphoneIpAddressType_Type = InetAddressType
_CcmeEphoneIpAddressType_Object = MibTableColumn
ccmeEphoneIpAddressType = _CcmeEphoneIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 2),
    _CcmeEphoneIpAddressType_Type()
)
ccmeEphoneIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneIpAddressType.setStatus("current")
_CcmeEphoneIpAddress_Type = InetAddress
_CcmeEphoneIpAddress_Object = MibTableColumn
ccmeEphoneIpAddress = _CcmeEphoneIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 3),
    _CcmeEphoneIpAddress_Type()
)
ccmeEphoneIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneIpAddress.setStatus("current")
_CcmeEphoneMacAddress_Type = MacAddress
_CcmeEphoneMacAddress_Object = MibTableColumn
ccmeEphoneMacAddress = _CcmeEphoneMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 4),
    _CcmeEphoneMacAddress_Type()
)
ccmeEphoneMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneMacAddress.setStatus("current")
_CcmeEphoneModel_Type = SnmpAdminString
_CcmeEphoneModel_Object = MibTableColumn
ccmeEphoneModel = _CcmeEphoneModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 5),
    _CcmeEphoneModel_Type()
)
ccmeEphoneModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneModel.setStatus("current")
_CcmeEphoneUsername_Type = SnmpAdminString
_CcmeEphoneUsername_Object = MibTableColumn
ccmeEphoneUsername = _CcmeEphoneUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 6),
    _CcmeEphoneUsername_Type()
)
ccmeEphoneUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneUsername.setStatus("current")


class _CcmeEphoneKeepAlive_Type(Integer32):
    """Custom type ccmeEphoneKeepAlive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_CcmeEphoneKeepAlive_Type.__name__ = "Integer32"
_CcmeEphoneKeepAlive_Object = MibTableColumn
ccmeEphoneKeepAlive = _CcmeEphoneKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 7),
    _CcmeEphoneKeepAlive_Type()
)
ccmeEphoneKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    ccmeEphoneKeepAlive.setUnits("seconds")


class _CcmeEphoneAutoLineOut_Type(Integer32):
    """Custom type ccmeEphoneAutoLineOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_CcmeEphoneAutoLineOut_Type.__name__ = "Integer32"
_CcmeEphoneAutoLineOut_Object = MibTableColumn
ccmeEphoneAutoLineOut = _CcmeEphoneAutoLineOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 8),
    _CcmeEphoneAutoLineOut_Type()
)
ccmeEphoneAutoLineOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneAutoLineOut.setStatus("current")


class _CcmeEphonePagingDn_Type(Integer32):
    """Custom type ccmeEphonePagingDn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 208),
    )


_CcmeEphonePagingDn_Type.__name__ = "Integer32"
_CcmeEphonePagingDn_Object = MibTableColumn
ccmeEphonePagingDn = _CcmeEphonePagingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 9),
    _CcmeEphonePagingDn_Type()
)
ccmeEphonePagingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphonePagingDn.setStatus("current")


class _CcmeEphoneAddon_Type(Integer32):
    """Custom type ccmeEphoneAddon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CcmeEphoneAddon_Type.__name__ = "Integer32"
_CcmeEphoneAddon_Object = MibTableColumn
ccmeEphoneAddon = _CcmeEphoneAddon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 10),
    _CcmeEphoneAddon_Type()
)
ccmeEphoneAddon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneAddon.setStatus("current")


class _CcmeEphoneTemplate_Type(Integer32):
    """Custom type ccmeEphoneTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CcmeEphoneTemplate_Type.__name__ = "Integer32"
_CcmeEphoneTemplate_Object = MibTableColumn
ccmeEphoneTemplate = _CcmeEphoneTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 11),
    _CcmeEphoneTemplate_Type()
)
ccmeEphoneTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneTemplate.setStatus("current")


class _CcmeEphonePagingPolicy_Type(Integer32):
    """Custom type ccmeEphonePagingPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1))
    )


_CcmeEphonePagingPolicy_Type.__name__ = "Integer32"
_CcmeEphonePagingPolicy_Object = MibTableColumn
ccmeEphonePagingPolicy = _CcmeEphonePagingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 12),
    _CcmeEphonePagingPolicy_Type()
)
ccmeEphonePagingPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphonePagingPolicy.setStatus("current")
_CcmeEphoneKeyPhone_Type = TruthValue
_CcmeEphoneKeyPhone_Object = MibTableColumn
ccmeEphoneKeyPhone = _CcmeEphoneKeyPhone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 13),
    _CcmeEphoneKeyPhone_Type()
)
ccmeEphoneKeyPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneKeyPhone.setStatus("current")
_CcmeEphoneAutoLineInEnabled_Type = TruthValue
_CcmeEphoneAutoLineInEnabled_Object = MibTableColumn
ccmeEphoneAutoLineInEnabled = _CcmeEphoneAutoLineInEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 14),
    _CcmeEphoneAutoLineInEnabled_Type()
)
ccmeEphoneAutoLineInEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneAutoLineInEnabled.setStatus("current")
_CcmeEphoneAftHrsBlkExmptEnabled_Type = TruthValue
_CcmeEphoneAftHrsBlkExmptEnabled_Object = MibTableColumn
ccmeEphoneAftHrsBlkExmptEnabled = _CcmeEphoneAftHrsBlkExmptEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 15),
    _CcmeEphoneAftHrsBlkExmptEnabled_Type()
)
ccmeEphoneAftHrsBlkExmptEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneAftHrsBlkExmptEnabled.setStatus("current")
_CcmeEphoneNightBellSvcEnabled_Type = TruthValue
_CcmeEphoneNightBellSvcEnabled_Object = MibTableColumn
ccmeEphoneNightBellSvcEnabled = _CcmeEphoneNightBellSvcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 16),
    _CcmeEphoneNightBellSvcEnabled_Type()
)
ccmeEphoneNightBellSvcEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneNightBellSvcEnabled.setStatus("current")
_CcmeEphoneKeepConfEnabled_Type = TruthValue
_CcmeEphoneKeepConfEnabled_Object = MibTableColumn
ccmeEphoneKeepConfEnabled = _CcmeEphoneKeepConfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 17),
    _CcmeEphoneKeepConfEnabled_Type()
)
ccmeEphoneKeepConfEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneKeepConfEnabled.setStatus("current")


class _CcmeEphonePrimaryDn_Type(Unsigned32):
    """Custom type ccmeEphonePrimaryDn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 208),
    )


_CcmeEphonePrimaryDn_Type.__name__ = "Unsigned32"
_CcmeEphonePrimaryDn_Object = MibTableColumn
ccmeEphonePrimaryDn = _CcmeEphonePrimaryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 18),
    _CcmeEphonePrimaryDn_Type()
)
ccmeEphonePrimaryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphonePrimaryDn.setStatus("current")
_CcmeEMUserProfileTag_Type = Unsigned32
_CcmeEMUserProfileTag_Object = MibTableColumn
ccmeEMUserProfileTag = _CcmeEMUserProfileTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 19),
    _CcmeEMUserProfileTag_Type()
)
ccmeEMUserProfileTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEMUserProfileTag.setStatus("current")
_CcmeEMLogOutProfileTag_Type = Unsigned32
_CcmeEMLogOutProfileTag_Object = MibTableColumn
ccmeEMLogOutProfileTag = _CcmeEMLogOutProfileTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 43, 1, 20),
    _CcmeEMLogOutProfileTag_Type()
)
ccmeEMLogOutProfileTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEMLogOutProfileTag.setStatus("current")
_CcmeEphoneSpeedDialConfTable_Object = MibTable
ccmeEphoneSpeedDialConfTable = _CcmeEphoneSpeedDialConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 44)
)
if mibBuilder.loadTexts:
    ccmeEphoneSpeedDialConfTable.setStatus("current")
_CcmeEphoneSpeedDialConfEntry_Object = MibTableRow
ccmeEphoneSpeedDialConfEntry = _CcmeEphoneSpeedDialConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 44, 1)
)
ccmeEphoneSpeedDialConfEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeEphoneTag"),
    (0, "CISCO-CCME-MIB", "ccmeEphoneSpeedDialTableIndex"),
)
if mibBuilder.loadTexts:
    ccmeEphoneSpeedDialConfEntry.setStatus("current")


class _CcmeEphoneSpeedDialTableIndex_Type(Integer32):
    """Custom type ccmeEphoneSpeedDialTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 34),
    )


_CcmeEphoneSpeedDialTableIndex_Type.__name__ = "Integer32"
_CcmeEphoneSpeedDialTableIndex_Object = MibTableColumn
ccmeEphoneSpeedDialTableIndex = _CcmeEphoneSpeedDialTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 44, 1, 1),
    _CcmeEphoneSpeedDialTableIndex_Type()
)
ccmeEphoneSpeedDialTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeEphoneSpeedDialTableIndex.setStatus("current")


class _CcmeEphoneSpeedDialTag_Type(Integer32):
    """Custom type ccmeEphoneSpeedDialTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 34),
    )


_CcmeEphoneSpeedDialTag_Type.__name__ = "Integer32"
_CcmeEphoneSpeedDialTag_Object = MibTableColumn
ccmeEphoneSpeedDialTag = _CcmeEphoneSpeedDialTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 44, 1, 2),
    _CcmeEphoneSpeedDialTag_Type()
)
ccmeEphoneSpeedDialTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneSpeedDialTag.setStatus("current")
_CcmeEphoneSpeedDialNumber_Type = CcmeDigitPatternString
_CcmeEphoneSpeedDialNumber_Object = MibTableColumn
ccmeEphoneSpeedDialNumber = _CcmeEphoneSpeedDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 44, 1, 3),
    _CcmeEphoneSpeedDialNumber_Type()
)
ccmeEphoneSpeedDialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneSpeedDialNumber.setStatus("current")


class _CcmeEphoneSpeedDialLabel_Type(SnmpAdminString):
    """Custom type ccmeEphoneSpeedDialLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CcmeEphoneSpeedDialLabel_Type.__name__ = "SnmpAdminString"
_CcmeEphoneSpeedDialLabel_Object = MibTableColumn
ccmeEphoneSpeedDialLabel = _CcmeEphoneSpeedDialLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 44, 1, 4),
    _CcmeEphoneSpeedDialLabel_Type()
)
ccmeEphoneSpeedDialLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneSpeedDialLabel.setStatus("current")
_CcmeEphoneFastDialConfTable_Object = MibTable
ccmeEphoneFastDialConfTable = _CcmeEphoneFastDialConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 45)
)
if mibBuilder.loadTexts:
    ccmeEphoneFastDialConfTable.setStatus("current")
_CcmeEphoneFastDialConfEntry_Object = MibTableRow
ccmeEphoneFastDialConfEntry = _CcmeEphoneFastDialConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 45, 1)
)
ccmeEphoneFastDialConfEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeEphoneTag"),
    (0, "CISCO-CCME-MIB", "ccmeEphoneFastDialTableIndex"),
)
if mibBuilder.loadTexts:
    ccmeEphoneFastDialConfEntry.setStatus("current")


class _CcmeEphoneFastDialTableIndex_Type(Integer32):
    """Custom type ccmeEphoneFastDialTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CcmeEphoneFastDialTableIndex_Type.__name__ = "Integer32"
_CcmeEphoneFastDialTableIndex_Object = MibTableColumn
ccmeEphoneFastDialTableIndex = _CcmeEphoneFastDialTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 45, 1, 1),
    _CcmeEphoneFastDialTableIndex_Type()
)
ccmeEphoneFastDialTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeEphoneFastDialTableIndex.setStatus("current")
_CcmeEphoneFastDialNumber_Type = CcmeDigitPatternString
_CcmeEphoneFastDialNumber_Object = MibTableColumn
ccmeEphoneFastDialNumber = _CcmeEphoneFastDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 45, 1, 2),
    _CcmeEphoneFastDialNumber_Type()
)
ccmeEphoneFastDialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneFastDialNumber.setStatus("current")


class _CcmeEphoneFastDialName_Type(SnmpAdminString):
    """Custom type ccmeEphoneFastDialName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CcmeEphoneFastDialName_Type.__name__ = "SnmpAdminString"
_CcmeEphoneFastDialName_Object = MibTableColumn
ccmeEphoneFastDialName = _CcmeEphoneFastDialName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 45, 1, 3),
    _CcmeEphoneFastDialName_Type()
)
ccmeEphoneFastDialName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneFastDialName.setStatus("current")
_CcmeEphoneBtnDNAssocConfTable_Object = MibTable
ccmeEphoneBtnDNAssocConfTable = _CcmeEphoneBtnDNAssocConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 46)
)
if mibBuilder.loadTexts:
    ccmeEphoneBtnDNAssocConfTable.setStatus("current")
_CcmeEphoneBtnDNAssocConfEntry_Object = MibTableRow
ccmeEphoneBtnDNAssocConfEntry = _CcmeEphoneBtnDNAssocConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 46, 1)
)
ccmeEphoneBtnDNAssocConfEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeEphoneTag"),
    (0, "CISCO-CCME-MIB", "ccmeEphoneButtonNumber"),
)
if mibBuilder.loadTexts:
    ccmeEphoneBtnDNAssocConfEntry.setStatus("current")


class _CcmeEphoneButtonNumber_Type(Integer32):
    """Custom type ccmeEphoneButtonNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcmeEphoneButtonNumber_Type.__name__ = "Integer32"
_CcmeEphoneButtonNumber_Object = MibTableColumn
ccmeEphoneButtonNumber = _CcmeEphoneButtonNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 46, 1, 1),
    _CcmeEphoneButtonNumber_Type()
)
ccmeEphoneButtonNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeEphoneButtonNumber.setStatus("current")


class _CcmeEphoneOverlayDN_Type(SnmpAdminString):
    """Custom type ccmeEphoneOverlayDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcmeEphoneOverlayDN_Type.__name__ = "SnmpAdminString"
_CcmeEphoneOverlayDN_Object = MibTableColumn
ccmeEphoneOverlayDN = _CcmeEphoneOverlayDN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 46, 1, 2),
    _CcmeEphoneOverlayDN_Type()
)
ccmeEphoneOverlayDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneOverlayDN.setStatus("current")
_CcmeEphoneDnConfigTable_Object = MibTable
ccmeEphoneDnConfigTable = _CcmeEphoneDnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47)
)
if mibBuilder.loadTexts:
    ccmeEphoneDnConfigTable.setStatus("current")
_CcmeEphoneDnConfigEntry_Object = MibTableRow
ccmeEphoneDnConfigEntry = _CcmeEphoneDnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1)
)
ccmeEphoneDnConfigEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeEphoneDnTag"),
)
if mibBuilder.loadTexts:
    ccmeEphoneDnConfigEntry.setStatus("current")


class _CcmeEphoneDnTag_Type(Integer32):
    """Custom type ccmeEphoneDnTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 288),
    )


_CcmeEphoneDnTag_Type.__name__ = "Integer32"
_CcmeEphoneDnTag_Object = MibTableColumn
ccmeEphoneDnTag = _CcmeEphoneDnTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 1),
    _CcmeEphoneDnTag_Type()
)
ccmeEphoneDnTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeEphoneDnTag.setStatus("current")


class _CcmeEphoneDnType_Type(Integer32):
    """Custom type ccmeEphoneDnType based on Integer32"""
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
        *(("extension", 1),
          ("intercom", 2),
          ("loopback", 7),
          ("moh", 4),
          ("mwi", 5),
          ("paging", 3),
          ("parkslot", 6))
    )


_CcmeEphoneDnType_Type.__name__ = "Integer32"
_CcmeEphoneDnType_Object = MibTableColumn
ccmeEphoneDnType = _CcmeEphoneDnType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 2),
    _CcmeEphoneDnType_Type()
)
ccmeEphoneDnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnType.setStatus("current")


class _CcmeEphoneDnMode_Type(Integer32):
    """Custom type ccmeEphoneDnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dual", 2),
          ("single", 1))
    )


_CcmeEphoneDnMode_Type.__name__ = "Integer32"
_CcmeEphoneDnMode_Object = MibTableColumn
ccmeEphoneDnMode = _CcmeEphoneDnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 3),
    _CcmeEphoneDnMode_Type()
)
ccmeEphoneDnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnMode.setStatus("current")


class _CcmeEphoneDnPriNum_Type(SnmpAdminString):
    """Custom type ccmeEphoneDnPriNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcmeEphoneDnPriNum_Type.__name__ = "SnmpAdminString"
_CcmeEphoneDnPriNum_Object = MibTableColumn
ccmeEphoneDnPriNum = _CcmeEphoneDnPriNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 4),
    _CcmeEphoneDnPriNum_Type()
)
ccmeEphoneDnPriNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnPriNum.setStatus("current")


class _CcmeEphoneDnSecNum_Type(SnmpAdminString):
    """Custom type ccmeEphoneDnSecNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcmeEphoneDnSecNum_Type.__name__ = "SnmpAdminString"
_CcmeEphoneDnSecNum_Object = MibTableColumn
ccmeEphoneDnSecNum = _CcmeEphoneDnSecNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 5),
    _CcmeEphoneDnSecNum_Type()
)
ccmeEphoneDnSecNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnSecNum.setStatus("current")


class _CcmeEphoneDnName_Type(SnmpAdminString):
    """Custom type ccmeEphoneDnName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CcmeEphoneDnName_Type.__name__ = "SnmpAdminString"
_CcmeEphoneDnName_Object = MibTableColumn
ccmeEphoneDnName = _CcmeEphoneDnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 6),
    _CcmeEphoneDnName_Type()
)
ccmeEphoneDnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnName.setStatus("current")


class _CcmeEphoneDnLabel_Type(SnmpAdminString):
    """Custom type ccmeEphoneDnLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CcmeEphoneDnLabel_Type.__name__ = "SnmpAdminString"
_CcmeEphoneDnLabel_Object = MibTableColumn
ccmeEphoneDnLabel = _CcmeEphoneDnLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 7),
    _CcmeEphoneDnLabel_Type()
)
ccmeEphoneDnLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnLabel.setStatus("current")


class _CcmeEphoneDnPriPref_Type(Integer32):
    """Custom type ccmeEphoneDnPriPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CcmeEphoneDnPriPref_Type.__name__ = "Integer32"
_CcmeEphoneDnPriPref_Object = MibTableColumn
ccmeEphoneDnPriPref = _CcmeEphoneDnPriPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 8),
    _CcmeEphoneDnPriPref_Type()
)
ccmeEphoneDnPriPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnPriPref.setStatus("current")


class _CcmeEphoneDnSecPref_Type(Integer32):
    """Custom type ccmeEphoneDnSecPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CcmeEphoneDnSecPref_Type.__name__ = "Integer32"
_CcmeEphoneDnSecPref_Object = MibTableColumn
ccmeEphoneDnSecPref = _CcmeEphoneDnSecPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 9),
    _CcmeEphoneDnSecPref_Type()
)
ccmeEphoneDnSecPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnSecPref.setStatus("current")


class _CcmeEphoneDnCFBusyNum_Type(SnmpAdminString):
    """Custom type ccmeEphoneDnCFBusyNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcmeEphoneDnCFBusyNum_Type.__name__ = "SnmpAdminString"
_CcmeEphoneDnCFBusyNum_Object = MibTableColumn
ccmeEphoneDnCFBusyNum = _CcmeEphoneDnCFBusyNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 10),
    _CcmeEphoneDnCFBusyNum_Type()
)
ccmeEphoneDnCFBusyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnCFBusyNum.setStatus("current")


class _CcmeEphoneDnCFAllNum_Type(SnmpAdminString):
    """Custom type ccmeEphoneDnCFAllNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcmeEphoneDnCFAllNum_Type.__name__ = "SnmpAdminString"
_CcmeEphoneDnCFAllNum_Object = MibTableColumn
ccmeEphoneDnCFAllNum = _CcmeEphoneDnCFAllNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 11),
    _CcmeEphoneDnCFAllNum_Type()
)
ccmeEphoneDnCFAllNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnCFAllNum.setStatus("current")


class _CcmeEphoneDnCFNoAnNum_Type(SnmpAdminString):
    """Custom type ccmeEphoneDnCFNoAnNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcmeEphoneDnCFNoAnNum_Type.__name__ = "SnmpAdminString"
_CcmeEphoneDnCFNoAnNum_Object = MibTableColumn
ccmeEphoneDnCFNoAnNum = _CcmeEphoneDnCFNoAnNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 12),
    _CcmeEphoneDnCFNoAnNum_Type()
)
ccmeEphoneDnCFNoAnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnCFNoAnNum.setStatus("current")


class _CcmeEphoneDnCFNoAnTo_Type(Integer32):
    """Custom type ccmeEphoneDnCFNoAnTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60000),
    )


_CcmeEphoneDnCFNoAnTo_Type.__name__ = "Integer32"
_CcmeEphoneDnCFNoAnTo_Object = MibTableColumn
ccmeEphoneDnCFNoAnTo = _CcmeEphoneDnCFNoAnTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 13),
    _CcmeEphoneDnCFNoAnTo_Type()
)
ccmeEphoneDnCFNoAnTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnCFNoAnTo.setStatus("current")
if mibBuilder.loadTexts:
    ccmeEphoneDnCFNoAnTo.setUnits("seconds")


class _CcmeEphoneDnMwiCapability_Type(Integer32):
    """Custom type ccmeEphoneDnMwiCapability based on Integer32"""
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
        *(("mwiDisabled", 4),
          ("mwiOff", 2),
          ("mwiOn", 1),
          ("mwiOnoff", 3))
    )


_CcmeEphoneDnMwiCapability_Type.__name__ = "Integer32"
_CcmeEphoneDnMwiCapability_Object = MibTableColumn
ccmeEphoneDnMwiCapability = _CcmeEphoneDnMwiCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 14),
    _CcmeEphoneDnMwiCapability_Type()
)
ccmeEphoneDnMwiCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnMwiCapability.setStatus("current")
_CcmeEphoneDnHuntstop_Type = TruthValue
_CcmeEphoneDnHuntstop_Object = MibTableColumn
ccmeEphoneDnHuntstop = _CcmeEphoneDnHuntstop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 15),
    _CcmeEphoneDnHuntstop_Type()
)
ccmeEphoneDnHuntstop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnHuntstop.setStatus("current")
_CcmeEphoneDnHuntstopCh_Type = TruthValue
_CcmeEphoneDnHuntstopCh_Object = MibTableColumn
ccmeEphoneDnHuntstopCh = _CcmeEphoneDnHuntstopCh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 16),
    _CcmeEphoneDnHuntstopCh_Type()
)
ccmeEphoneDnHuntstopCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnHuntstopCh.setStatus("current")


class _CcmeEphoneDnHoldAltTo_Type(Integer32):
    """Custom type ccmeEphoneDnHoldAltTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CcmeEphoneDnHoldAltTo_Type.__name__ = "Integer32"
_CcmeEphoneDnHoldAltTo_Object = MibTableColumn
ccmeEphoneDnHoldAltTo = _CcmeEphoneDnHoldAltTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 17),
    _CcmeEphoneDnHoldAltTo_Type()
)
ccmeEphoneDnHoldAltTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnHoldAltTo.setStatus("current")
if mibBuilder.loadTexts:
    ccmeEphoneDnHoldAltTo.setUnits("seconds")


class _CcmeEphoneDnHoldAltType_Type(Integer32):
    """Custom type ccmeEphoneDnHoldAltType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("originator", 2),
          ("shared", 3))
    )


_CcmeEphoneDnHoldAltType_Type.__name__ = "Integer32"
_CcmeEphoneDnHoldAltType_Object = MibTableColumn
ccmeEphoneDnHoldAltType = _CcmeEphoneDnHoldAltType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 18),
    _CcmeEphoneDnHoldAltType_Type()
)
ccmeEphoneDnHoldAltType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnHoldAltType.setStatus("current")
_CcmeEphoneDnMwiSipSubscrEnabled_Type = TruthValue
_CcmeEphoneDnMwiSipSubscrEnabled_Object = MibTableColumn
ccmeEphoneDnMwiSipSubscrEnabled = _CcmeEphoneDnMwiSipSubscrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 19),
    _CcmeEphoneDnMwiSipSubscrEnabled_Type()
)
ccmeEphoneDnMwiSipSubscrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnMwiSipSubscrEnabled.setStatus("current")


class _CcmeEphoneDnScriptName_Type(SnmpAdminString):
    """Custom type ccmeEphoneDnScriptName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CcmeEphoneDnScriptName_Type.__name__ = "SnmpAdminString"
_CcmeEphoneDnScriptName_Object = MibTableColumn
ccmeEphoneDnScriptName = _CcmeEphoneDnScriptName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 47, 1, 20),
    _CcmeEphoneDnScriptName_Type()
)
ccmeEphoneDnScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnScriptName.setStatus("current")


class _CcmeNotificationEnable_Type(TruthValue):
    """Custom type ccmeNotificationEnable based on TruthValue"""


_CcmeNotificationEnable_Object = MibScalar
ccmeNotificationEnable = _CcmeNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 48),
    _CcmeNotificationEnable_Type()
)
ccmeNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmeNotificationEnable.setStatus("current")


class _CcmeSysTrapSeverity_Type(Integer32):
    """Custom type ccmeSysTrapSeverity based on Integer32"""
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


_CcmeSysTrapSeverity_Type.__name__ = "Integer32"
_CcmeSysTrapSeverity_Object = MibScalar
ccmeSysTrapSeverity = _CcmeSysTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 49),
    _CcmeSysTrapSeverity_Type()
)
ccmeSysTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeSysTrapSeverity.setStatus("current")
_CcmeSysNotificationReason_Type = SnmpAdminString
_CcmeSysNotificationReason_Object = MibScalar
ccmeSysNotificationReason = _CcmeSysNotificationReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 50),
    _CcmeSysNotificationReason_Type()
)
ccmeSysNotificationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeSysNotificationReason.setStatus("current")


class _CcmeEphoneUnRegThreshold_Type(Integer32):
    """Custom type ccmeEphoneUnRegThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CcmeEphoneUnRegThreshold_Type.__name__ = "Integer32"
_CcmeEphoneUnRegThreshold_Object = MibScalar
ccmeEphoneUnRegThreshold = _CcmeEphoneUnRegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 51),
    _CcmeEphoneUnRegThreshold_Type()
)
ccmeEphoneUnRegThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmeEphoneUnRegThreshold.setStatus("current")


class _CcmeEphoneTrapReason_Type(SnmpAdminString):
    """Custom type ccmeEphoneTrapReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcmeEphoneTrapReason_Type.__name__ = "SnmpAdminString"
_CcmeEphoneTrapReason_Object = MibScalar
ccmeEphoneTrapReason = _CcmeEphoneTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 52),
    _CcmeEphoneTrapReason_Type()
)
ccmeEphoneTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneTrapReason.setStatus("current")


class _CcmeUserAutoLogoutTo_Type(Integer32):
    """Custom type ccmeUserAutoLogoutTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CcmeUserAutoLogoutTo_Type.__name__ = "Integer32"
_CcmeUserAutoLogoutTo_Object = MibScalar
ccmeUserAutoLogoutTo = _CcmeUserAutoLogoutTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 53),
    _CcmeUserAutoLogoutTo_Type()
)
ccmeUserAutoLogoutTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeUserAutoLogoutTo.setStatus("current")
if mibBuilder.loadTexts:
    ccmeUserAutoLogoutTo.setUnits("minutes")
_CcmeUserLoginDeactivateTime_Type = SnmpAdminString
_CcmeUserLoginDeactivateTime_Object = MibScalar
ccmeUserLoginDeactivateTime = _CcmeUserLoginDeactivateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 54),
    _CcmeUserLoginDeactivateTime_Type()
)
ccmeUserLoginDeactivateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeUserLoginDeactivateTime.setStatus("current")
_CcmeMwiSipServerIpAddress_Type = InetAddress
_CcmeMwiSipServerIpAddress_Object = MibScalar
ccmeMwiSipServerIpAddress = _CcmeMwiSipServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 55),
    _CcmeMwiSipServerIpAddress_Type()
)
ccmeMwiSipServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMwiSipServerIpAddress.setStatus("current")


class _CcmeMwiSipServerTransportType_Type(Integer32):
    """Custom type ccmeMwiSipServerTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_CcmeMwiSipServerTransportType_Type.__name__ = "Integer32"
_CcmeMwiSipServerTransportType_Object = MibScalar
ccmeMwiSipServerTransportType = _CcmeMwiSipServerTransportType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 56),
    _CcmeMwiSipServerTransportType_Type()
)
ccmeMwiSipServerTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMwiSipServerTransportType.setStatus("current")


class _CcmeMwiSipServerPortNumber_Type(InetPortNumber):
    """Custom type ccmeMwiSipServerPortNumber based on InetPortNumber"""
    defaultValue = 5060

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 9999),
    )


_CcmeMwiSipServerPortNumber_Type.__name__ = "InetPortNumber"
_CcmeMwiSipServerPortNumber_Object = MibScalar
ccmeMwiSipServerPortNumber = _CcmeMwiSipServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 57),
    _CcmeMwiSipServerPortNumber_Type()
)
ccmeMwiSipServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMwiSipServerPortNumber.setStatus("current")
_CcmeMwiSipServerRegE164Enabled_Type = TruthValue
_CcmeMwiSipServerRegE164Enabled_Object = MibScalar
ccmeMwiSipServerRegE164Enabled = _CcmeMwiSipServerRegE164Enabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 58),
    _CcmeMwiSipServerRegE164Enabled_Type()
)
ccmeMwiSipServerRegE164Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMwiSipServerRegE164Enabled.setStatus("current")
_CcmeMwiSipSvrUnsolicitedEnabled_Type = TruthValue
_CcmeMwiSipSvrUnsolicitedEnabled_Object = MibScalar
ccmeMwiSipSvrUnsolicitedEnabled = _CcmeMwiSipSvrUnsolicitedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 59),
    _CcmeMwiSipSvrUnsolicitedEnabled_Type()
)
ccmeMwiSipSvrUnsolicitedEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMwiSipSvrUnsolicitedEnabled.setStatus("current")
_CcmeCorConfTable_Object = MibTable
ccmeCorConfTable = _CcmeCorConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 60)
)
if mibBuilder.loadTexts:
    ccmeCorConfTable.setStatus("current")
_CcmeCorConfEntry_Object = MibTableRow
ccmeCorConfEntry = _CcmeCorConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 60, 1)
)
ccmeCorConfEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeCorTableIndex"),
)
if mibBuilder.loadTexts:
    ccmeCorConfEntry.setStatus("current")
_CcmeCorTableIndex_Type = Unsigned32
_CcmeCorTableIndex_Object = MibTableColumn
ccmeCorTableIndex = _CcmeCorTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 60, 1, 1),
    _CcmeCorTableIndex_Type()
)
ccmeCorTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeCorTableIndex.setStatus("current")
_CcmeCorTag_Type = Unsigned32
_CcmeCorTag_Object = MibTableColumn
ccmeCorTag = _CcmeCorTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 60, 1, 2),
    _CcmeCorTag_Type()
)
ccmeCorTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeCorTag.setStatus("current")
_CcmeCorListName_Type = SnmpAdminString
_CcmeCorListName_Object = MibTableColumn
ccmeCorListName = _CcmeCorListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 60, 1, 3),
    _CcmeCorListName_Type()
)
ccmeCorListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeCorListName.setStatus("current")


class _CcmeCorScope_Type(Integer32):
    """Custom type ccmeCorScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccme", 1),
          ("srstSccp", 2),
          ("srstSip", 3))
    )


_CcmeCorScope_Type.__name__ = "Integer32"
_CcmeCorScope_Object = MibTableColumn
ccmeCorScope = _CcmeCorScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 60, 1, 4),
    _CcmeCorScope_Type()
)
ccmeCorScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeCorScope.setStatus("current")


class _CcmeCorDirection_Type(Integer32):
    """Custom type ccmeCorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_CcmeCorDirection_Type.__name__ = "Integer32"
_CcmeCorDirection_Object = MibTableColumn
ccmeCorDirection = _CcmeCorDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 60, 1, 5),
    _CcmeCorDirection_Type()
)
ccmeCorDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeCorDirection.setStatus("current")
_CcmeCorStartingNumber_Type = SnmpAdminString
_CcmeCorStartingNumber_Object = MibTableColumn
ccmeCorStartingNumber = _CcmeCorStartingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 60, 1, 6),
    _CcmeCorStartingNumber_Type()
)
ccmeCorStartingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeCorStartingNumber.setStatus("current")
_CcmeCorEndingNumber_Type = SnmpAdminString
_CcmeCorEndingNumber_Object = MibTableColumn
ccmeCorEndingNumber = _CcmeCorEndingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 60, 1, 7),
    _CcmeCorEndingNumber_Type()
)
ccmeCorEndingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeCorEndingNumber.setStatus("current")
_CcmeCorVoiceRegPoolNumber_Type = Unsigned32
_CcmeCorVoiceRegPoolNumber_Object = MibTableColumn
ccmeCorVoiceRegPoolNumber = _CcmeCorVoiceRegPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 60, 1, 8),
    _CcmeCorVoiceRegPoolNumber_Type()
)
ccmeCorVoiceRegPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeCorVoiceRegPoolNumber.setStatus("current")
_CcmeCorListDefaultEnabled_Type = TruthValue
_CcmeCorListDefaultEnabled_Object = MibTableColumn
ccmeCorListDefaultEnabled = _CcmeCorListDefaultEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 60, 1, 9),
    _CcmeCorListDefaultEnabled_Type()
)
ccmeCorListDefaultEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeCorListDefaultEnabled.setStatus("current")
_CcmeLoopbackDnConfTable_Object = MibTable
ccmeLoopbackDnConfTable = _CcmeLoopbackDnConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 61)
)
if mibBuilder.loadTexts:
    ccmeLoopbackDnConfTable.setStatus("current")
_CcmeLoopbackDnConfEntry_Object = MibTableRow
ccmeLoopbackDnConfEntry = _CcmeLoopbackDnConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 61, 1)
)
ccmeLoopbackDnConfEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeLoopbackDnTag"),
)
if mibBuilder.loadTexts:
    ccmeLoopbackDnConfEntry.setStatus("current")
_CcmeLoopbackDnTag_Type = Unsigned32
_CcmeLoopbackDnTag_Object = MibTableColumn
ccmeLoopbackDnTag = _CcmeLoopbackDnTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 61, 1, 1),
    _CcmeLoopbackDnTag_Type()
)
ccmeLoopbackDnTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeLoopbackDnTag.setStatus("current")


class _CcmeLoopbackDnforward_Type(Unsigned32):
    """Custom type ccmeLoopbackDnforward based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CcmeLoopbackDnforward_Type.__name__ = "Unsigned32"
_CcmeLoopbackDnforward_Object = MibTableColumn
ccmeLoopbackDnforward = _CcmeLoopbackDnforward_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 61, 1, 2),
    _CcmeLoopbackDnforward_Type()
)
ccmeLoopbackDnforward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeLoopbackDnforward.setStatus("current")


class _CcmeLoopbackDnStrip_Type(Unsigned32):
    """Custom type ccmeLoopbackDnStrip based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CcmeLoopbackDnStrip_Type.__name__ = "Unsigned32"
_CcmeLoopbackDnStrip_Object = MibTableColumn
ccmeLoopbackDnStrip = _CcmeLoopbackDnStrip_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 61, 1, 3),
    _CcmeLoopbackDnStrip_Type()
)
ccmeLoopbackDnStrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeLoopbackDnStrip.setStatus("current")
_CcmeLoopbackDnPrefix_Type = SnmpAdminString
_CcmeLoopbackDnPrefix_Object = MibTableColumn
ccmeLoopbackDnPrefix = _CcmeLoopbackDnPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 61, 1, 4),
    _CcmeLoopbackDnPrefix_Type()
)
ccmeLoopbackDnPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeLoopbackDnPrefix.setStatus("current")
_CcmeLoopbackDnSuffix_Type = SnmpAdminString
_CcmeLoopbackDnSuffix_Object = MibTableColumn
ccmeLoopbackDnSuffix = _CcmeLoopbackDnSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 61, 1, 5),
    _CcmeLoopbackDnSuffix_Type()
)
ccmeLoopbackDnSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeLoopbackDnSuffix.setStatus("current")


class _CcmeLoopbackDnRetryTo_Type(Integer32):
    """Custom type ccmeLoopbackDnRetryTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CcmeLoopbackDnRetryTo_Type.__name__ = "Integer32"
_CcmeLoopbackDnRetryTo_Object = MibTableColumn
ccmeLoopbackDnRetryTo = _CcmeLoopbackDnRetryTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 61, 1, 6),
    _CcmeLoopbackDnRetryTo_Type()
)
ccmeLoopbackDnRetryTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeLoopbackDnRetryTo.setStatus("current")
if mibBuilder.loadTexts:
    ccmeLoopbackDnRetryTo.setUnits("seconds")
_CcmeLoopbackDnAutoCon_Type = TruthValue
_CcmeLoopbackDnAutoCon_Object = MibTableColumn
ccmeLoopbackDnAutoCon = _CcmeLoopbackDnAutoCon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 61, 1, 7),
    _CcmeLoopbackDnAutoCon_Type()
)
ccmeLoopbackDnAutoCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeLoopbackDnAutoCon.setStatus("current")


class _CcmeLoopbackDnCodec_Type(Integer32):
    """Custom type ccmeLoopbackDnCodec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("g711alaw", 1),
          ("g711ulaw", 2))
    )


_CcmeLoopbackDnCodec_Type.__name__ = "Integer32"
_CcmeLoopbackDnCodec_Object = MibTableColumn
ccmeLoopbackDnCodec = _CcmeLoopbackDnCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 61, 1, 8),
    _CcmeLoopbackDnCodec_Type()
)
ccmeLoopbackDnCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeLoopbackDnCodec.setStatus("current")
_CcmeIntercomDnConfTable_Object = MibTable
ccmeIntercomDnConfTable = _CcmeIntercomDnConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 62)
)
if mibBuilder.loadTexts:
    ccmeIntercomDnConfTable.setStatus("current")
_CcmeIntercomDnConfEntry_Object = MibTableRow
ccmeIntercomDnConfEntry = _CcmeIntercomDnConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 62, 1)
)
ccmeIntercomDnConfEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeIntercomDnTag"),
)
if mibBuilder.loadTexts:
    ccmeIntercomDnConfEntry.setStatus("current")
_CcmeIntercomDnTag_Type = Unsigned32
_CcmeIntercomDnTag_Object = MibTableColumn
ccmeIntercomDnTag = _CcmeIntercomDnTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 62, 1, 1),
    _CcmeIntercomDnTag_Type()
)
ccmeIntercomDnTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeIntercomDnTag.setStatus("current")
_CcmeIntercomDnExtensionNum_Type = SnmpAdminString
_CcmeIntercomDnExtensionNum_Object = MibTableColumn
ccmeIntercomDnExtensionNum = _CcmeIntercomDnExtensionNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 62, 1, 2),
    _CcmeIntercomDnExtensionNum_Type()
)
ccmeIntercomDnExtensionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeIntercomDnExtensionNum.setStatus("current")
_CcmeIntercomDnBargeInEnabled_Type = TruthValue
_CcmeIntercomDnBargeInEnabled_Object = MibTableColumn
ccmeIntercomDnBargeInEnabled = _CcmeIntercomDnBargeInEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 62, 1, 3),
    _CcmeIntercomDnBargeInEnabled_Type()
)
ccmeIntercomDnBargeInEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeIntercomDnBargeInEnabled.setStatus("current")
_CcmeIntercomDnAutoAnsEnabled_Type = TruthValue
_CcmeIntercomDnAutoAnsEnabled_Object = MibTableColumn
ccmeIntercomDnAutoAnsEnabled = _CcmeIntercomDnAutoAnsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 62, 1, 4),
    _CcmeIntercomDnAutoAnsEnabled_Type()
)
ccmeIntercomDnAutoAnsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeIntercomDnAutoAnsEnabled.setStatus("current")
_CcmeIntercomDnLabel_Type = SnmpAdminString
_CcmeIntercomDnLabel_Object = MibTableColumn
ccmeIntercomDnLabel = _CcmeIntercomDnLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 62, 1, 5),
    _CcmeIntercomDnLabel_Type()
)
ccmeIntercomDnLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeIntercomDnLabel.setStatus("current")
_CcmeMohMulticastIpAddress_Type = InetAddress
_CcmeMohMulticastIpAddress_Object = MibScalar
ccmeMohMulticastIpAddress = _CcmeMohMulticastIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 63),
    _CcmeMohMulticastIpAddress_Type()
)
ccmeMohMulticastIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMohMulticastIpAddress.setStatus("current")
_CcmeMohMulticastPortNumber_Type = InetPortNumber
_CcmeMohMulticastPortNumber_Object = MibScalar
ccmeMohMulticastPortNumber = _CcmeMohMulticastPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 64),
    _CcmeMohMulticastPortNumber_Type()
)
ccmeMohMulticastPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMohMulticastPortNumber.setStatus("current")
_CcmeMohMulticastRoute_Type = SnmpAdminString
_CcmeMohMulticastRoute_Object = MibScalar
ccmeMohMulticastRoute = _CcmeMohMulticastRoute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 65),
    _CcmeMohMulticastRoute_Type()
)
ccmeMohMulticastRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMohMulticastRoute.setStatus("current")
_CcmeMohFlashMulticastIPAddrType_Type = InetAddressType
_CcmeMohFlashMulticastIPAddrType_Object = MibScalar
ccmeMohFlashMulticastIPAddrType = _CcmeMohFlashMulticastIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 66),
    _CcmeMohFlashMulticastIPAddrType_Type()
)
ccmeMohFlashMulticastIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMohFlashMulticastIPAddrType.setStatus("current")
_CcmeMohMulticastIpAddressType_Type = InetAddressType
_CcmeMohMulticastIpAddressType_Object = MibScalar
ccmeMohMulticastIpAddressType = _CcmeMohMulticastIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 67),
    _CcmeMohMulticastIpAddressType_Type()
)
ccmeMohMulticastIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMohMulticastIpAddressType.setStatus("current")
_CcmeEMUserDirNumConfTable_Object = MibTable
ccmeEMUserDirNumConfTable = _CcmeEMUserDirNumConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 68)
)
if mibBuilder.loadTexts:
    ccmeEMUserDirNumConfTable.setStatus("current")
_CcmeEMUserDirNumConfEntry_Object = MibTableRow
ccmeEMUserDirNumConfEntry = _CcmeEMUserDirNumConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 68, 1)
)
ccmeEMUserDirNumConfEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmEMUserProfileDirNumIndex"),
    (0, "CISCO-CCME-MIB", "ccmeEMUserDirNumTag"),
)
if mibBuilder.loadTexts:
    ccmeEMUserDirNumConfEntry.setStatus("current")


class _CcmEMUserProfileDirNumIndex_Type(Integer32):
    """Custom type ccmEMUserProfileDirNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcmEMUserProfileDirNumIndex_Type.__name__ = "Integer32"
_CcmEMUserProfileDirNumIndex_Object = MibTableColumn
ccmEMUserProfileDirNumIndex = _CcmEMUserProfileDirNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 68, 1, 1),
    _CcmEMUserProfileDirNumIndex_Type()
)
ccmEMUserProfileDirNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmEMUserProfileDirNumIndex.setStatus("current")


class _CcmeEMUserDirNumTag_Type(Integer32):
    """Custom type ccmeEMUserDirNumTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcmeEMUserDirNumTag_Type.__name__ = "Integer32"
_CcmeEMUserDirNumTag_Object = MibTableColumn
ccmeEMUserDirNumTag = _CcmeEMUserDirNumTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 68, 1, 2),
    _CcmeEMUserDirNumTag_Type()
)
ccmeEMUserDirNumTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeEMUserDirNumTag.setStatus("current")
_CcmeEMUserDirNum_Type = CcmeDigitPatternString
_CcmeEMUserDirNum_Object = MibTableColumn
ccmeEMUserDirNum = _CcmeEMUserDirNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 68, 1, 3),
    _CcmeEMUserDirNum_Type()
)
ccmeEMUserDirNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEMUserDirNum.setStatus("current")


class _CcmeEMUserDirNumOverlay_Type(SnmpAdminString):
    """Custom type ccmeEMUserDirNumOverlay based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcmeEMUserDirNumOverlay_Type.__name__ = "SnmpAdminString"
_CcmeEMUserDirNumOverlay_Object = MibTableColumn
ccmeEMUserDirNumOverlay = _CcmeEMUserDirNumOverlay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 68, 1, 4),
    _CcmeEMUserDirNumOverlay_Type()
)
ccmeEMUserDirNumOverlay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEMUserDirNumOverlay.setStatus("current")
_CcmeEMLogoutDirNumConfTable_Object = MibTable
ccmeEMLogoutDirNumConfTable = _CcmeEMLogoutDirNumConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 69)
)
if mibBuilder.loadTexts:
    ccmeEMLogoutDirNumConfTable.setStatus("current")
_CcmeEMLogoutDirNumConfEntry_Object = MibTableRow
ccmeEMLogoutDirNumConfEntry = _CcmeEMLogoutDirNumConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 69, 1)
)
ccmeEMLogoutDirNumConfEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmEMLogOutProfileDirNumIndex"),
    (0, "CISCO-CCME-MIB", "ccmeEMLogoutDirNumTag"),
)
if mibBuilder.loadTexts:
    ccmeEMLogoutDirNumConfEntry.setStatus("current")


class _CcmEMLogOutProfileDirNumIndex_Type(Integer32):
    """Custom type ccmEMLogOutProfileDirNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcmEMLogOutProfileDirNumIndex_Type.__name__ = "Integer32"
_CcmEMLogOutProfileDirNumIndex_Object = MibTableColumn
ccmEMLogOutProfileDirNumIndex = _CcmEMLogOutProfileDirNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 69, 1, 1),
    _CcmEMLogOutProfileDirNumIndex_Type()
)
ccmEMLogOutProfileDirNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmEMLogOutProfileDirNumIndex.setStatus("current")


class _CcmeEMLogoutDirNumTag_Type(Integer32):
    """Custom type ccmeEMLogoutDirNumTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcmeEMLogoutDirNumTag_Type.__name__ = "Integer32"
_CcmeEMLogoutDirNumTag_Object = MibTableColumn
ccmeEMLogoutDirNumTag = _CcmeEMLogoutDirNumTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 69, 1, 2),
    _CcmeEMLogoutDirNumTag_Type()
)
ccmeEMLogoutDirNumTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeEMLogoutDirNumTag.setStatus("current")
_CcmeEMLogoutDirNum_Type = CcmeDigitPatternString
_CcmeEMLogoutDirNum_Object = MibTableColumn
ccmeEMLogoutDirNum = _CcmeEMLogoutDirNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 69, 1, 3),
    _CcmeEMLogoutDirNum_Type()
)
ccmeEMLogoutDirNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEMLogoutDirNum.setStatus("current")


class _CcmeEMLogoutDirNumOverlay_Type(SnmpAdminString):
    """Custom type ccmeEMLogoutDirNumOverlay based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcmeEMLogoutDirNumOverlay_Type.__name__ = "SnmpAdminString"
_CcmeEMLogoutDirNumOverlay_Object = MibTableColumn
ccmeEMLogoutDirNumOverlay = _CcmeEMLogoutDirNumOverlay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 1, 69, 1, 4),
    _CcmeEMLogoutDirNumOverlay_Type()
)
ccmeEMLogoutDirNumOverlay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEMLogoutDirNumOverlay.setStatus("current")
_CcmeActiveStats_ObjectIdentity = ObjectIdentity
ccmeActiveStats = _CcmeActiveStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2)
)
_CcmeEphoneCallLegs_Type = Gauge32
_CcmeEphoneCallLegs_Object = MibScalar
ccmeEphoneCallLegs = _CcmeEphoneCallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 1),
    _CcmeEphoneCallLegs_Type()
)
ccmeEphoneCallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneCallLegs.setStatus("current")
_CcmeEphoneTot_Type = Counter32
_CcmeEphoneTot_Object = MibScalar
ccmeEphoneTot = _CcmeEphoneTot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 2),
    _CcmeEphoneTot_Type()
)
ccmeEphoneTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneTot.setStatus("current")
_CcmeEphoneTotRegistered_Type = Gauge32
_CcmeEphoneTotRegistered_Object = MibScalar
ccmeEphoneTotRegistered = _CcmeEphoneTotRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 3),
    _CcmeEphoneTotRegistered_Type()
)
ccmeEphoneTotRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneTotRegistered.setStatus("current")
_CcmeEphoneTotKeyPhConfigured_Type = Gauge32
_CcmeEphoneTotKeyPhConfigured_Object = MibScalar
ccmeEphoneTotKeyPhConfigured = _CcmeEphoneTotKeyPhConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 4),
    _CcmeEphoneTotKeyPhConfigured_Type()
)
ccmeEphoneTotKeyPhConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneTotKeyPhConfigured.setStatus("current")
_CcmeEphoneTotKeyPhRegistered_Type = Gauge32
_CcmeEphoneTotKeyPhRegistered_Object = MibScalar
ccmeEphoneTotKeyPhRegistered = _CcmeEphoneTotKeyPhRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 5),
    _CcmeEphoneTotKeyPhRegistered_Type()
)
ccmeEphoneTotKeyPhRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneTotKeyPhRegistered.setStatus("current")
_CcmeEphoneActTable_Object = MibTable
ccmeEphoneActTable = _CcmeEphoneActTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ccmeEphoneActTable.setStatus("current")
_CcmeEphoneActEntry_Object = MibTableRow
ccmeEphoneActEntry = _CcmeEphoneActEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1)
)
ccmeEphoneActEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeEphoneTag"),
)
if mibBuilder.loadTexts:
    ccmeEphoneActEntry.setStatus("current")
_CcmeEphoneDeviceName_Type = SnmpAdminString
_CcmeEphoneDeviceName_Object = MibTableColumn
ccmeEphoneDeviceName = _CcmeEphoneDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 1),
    _CcmeEphoneDeviceName_Type()
)
ccmeEphoneDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDeviceName.setStatus("current")


class _CcmeEphoneRegState_Type(Integer32):
    """Custom type ccmeEphoneRegState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deceased", 3),
          ("registered", 1),
          ("unregistered", 2))
    )


_CcmeEphoneRegState_Type.__name__ = "Integer32"
_CcmeEphoneRegState_Object = MibTableColumn
ccmeEphoneRegState = _CcmeEphoneRegState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 2),
    _CcmeEphoneRegState_Type()
)
ccmeEphoneRegState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneRegState.setStatus("current")


class _CcmeEphoneActiveDN_Type(Integer32):
    """Custom type ccmeEphoneActiveDN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcmeEphoneActiveDN_Type.__name__ = "Integer32"
_CcmeEphoneActiveDN_Object = MibTableColumn
ccmeEphoneActiveDN = _CcmeEphoneActiveDN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 3),
    _CcmeEphoneActiveDN_Type()
)
ccmeEphoneActiveDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneActiveDN.setStatus("current")


class _CcmeEphoneActivityStatus_Type(Integer32):
    """Custom type ccmeEphoneActivityStatus based on Integer32"""
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
        *(("offhook", 2),
          ("onhook", 1),
          ("paging", 4),
          ("ringing", 3))
    )


_CcmeEphoneActivityStatus_Type.__name__ = "Integer32"
_CcmeEphoneActivityStatus_Object = MibTableColumn
ccmeEphoneActivityStatus = _CcmeEphoneActivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 4),
    _CcmeEphoneActivityStatus_Type()
)
ccmeEphoneActivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneActivityStatus.setStatus("current")
_CcmeEphoneKeepAliveCnt_Type = Counter32
_CcmeEphoneKeepAliveCnt_Object = MibTableColumn
ccmeEphoneKeepAliveCnt = _CcmeEphoneKeepAliveCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 5),
    _CcmeEphoneKeepAliveCnt_Type()
)
ccmeEphoneKeepAliveCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneKeepAliveCnt.setStatus("current")
_CcmeEphonePendingReset_Type = TruthValue
_CcmeEphonePendingReset_Object = MibTableColumn
ccmeEphonePendingReset = _CcmeEphonePendingReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 6),
    _CcmeEphonePendingReset_Type()
)
ccmeEphonePendingReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphonePendingReset.setStatus("current")
_CcmeEphoneRegTime_Type = SnmpAdminString
_CcmeEphoneRegTime_Object = MibTableColumn
ccmeEphoneRegTime = _CcmeEphoneRegTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 7),
    _CcmeEphoneRegTime_Type()
)
ccmeEphoneRegTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneRegTime.setStatus("current")
_CcmeEphoneCurrentFirmwareRev_Type = SnmpAdminString
_CcmeEphoneCurrentFirmwareRev_Object = MibTableColumn
ccmeEphoneCurrentFirmwareRev = _CcmeEphoneCurrentFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 8),
    _CcmeEphoneCurrentFirmwareRev_Type()
)
ccmeEphoneCurrentFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneCurrentFirmwareRev.setStatus("current")
_CcmeEphonePreviousFirmwareRev_Type = SnmpAdminString
_CcmeEphonePreviousFirmwareRev_Object = MibTableColumn
ccmeEphonePreviousFirmwareRev = _CcmeEphonePreviousFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 9),
    _CcmeEphonePreviousFirmwareRev_Type()
)
ccmeEphonePreviousFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphonePreviousFirmwareRev.setStatus("current")
_CcmeEphoneLastError_Type = SnmpAdminString
_CcmeEphoneLastError_Object = MibTableColumn
ccmeEphoneLastError = _CcmeEphoneLastError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 10),
    _CcmeEphoneLastError_Type()
)
ccmeEphoneLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneLastError.setStatus("current")
_CcmeEphoneObservedType_Type = SnmpAdminString
_CcmeEphoneObservedType_Object = MibTableColumn
ccmeEphoneObservedType = _CcmeEphoneObservedType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 11),
    _CcmeEphoneObservedType_Type()
)
ccmeEphoneObservedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneObservedType.setStatus("current")
_CcmeEphoneLoginStatus_Type = TruthValue
_CcmeEphoneLoginStatus_Object = MibTableColumn
ccmeEphoneLoginStatus = _CcmeEphoneLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 12),
    _CcmeEphoneLoginStatus_Type()
)
ccmeEphoneLoginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneLoginStatus.setStatus("current")
_CcmeEphoneDnDStatus_Type = TruthValue
_CcmeEphoneDnDStatus_Object = MibTableColumn
ccmeEphoneDnDStatus = _CcmeEphoneDnDStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 13),
    _CcmeEphoneDnDStatus_Type()
)
ccmeEphoneDnDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnDStatus.setStatus("current")
_CcmeEphoneDebugStatus_Type = TruthValue
_CcmeEphoneDebugStatus_Object = MibTableColumn
ccmeEphoneDebugStatus = _CcmeEphoneDebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 14),
    _CcmeEphoneDebugStatus_Type()
)
ccmeEphoneDebugStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDebugStatus.setStatus("current")
_CcmeEphoneMediaActive_Type = TruthValue
_CcmeEphoneMediaActive_Object = MibTableColumn
ccmeEphoneMediaActive = _CcmeEphoneMediaActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 15),
    _CcmeEphoneMediaActive_Type()
)
ccmeEphoneMediaActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneMediaActive.setStatus("current")
_CcmeEphoneTAPIClient_Type = TruthValue
_CcmeEphoneTAPIClient_Object = MibTableColumn
ccmeEphoneTAPIClient = _CcmeEphoneTAPIClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 16),
    _CcmeEphoneTAPIClient_Type()
)
ccmeEphoneTAPIClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneTAPIClient.setStatus("current")


class _CcmeEphoneMediaCapability_Type(Integer32):
    """Custom type ccmeEphoneMediaCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("audioOnly", 1),
          ("audioVideo", 2))
    )


_CcmeEphoneMediaCapability_Type.__name__ = "Integer32"
_CcmeEphoneMediaCapability_Object = MibTableColumn
ccmeEphoneMediaCapability = _CcmeEphoneMediaCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 17),
    _CcmeEphoneMediaCapability_Type()
)
ccmeEphoneMediaCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneMediaCapability.setStatus("current")
_CcmeEphoneRemote_Type = TruthValue
_CcmeEphoneRemote_Object = MibTableColumn
ccmeEphoneRemote = _CcmeEphoneRemote_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 6, 1, 18),
    _CcmeEphoneRemote_Type()
)
ccmeEphoneRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneRemote.setStatus("current")


class _CcmeMohSource_Type(Integer32):
    """Custom type ccmeMohSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("liveFeed", 2))
    )


_CcmeMohSource_Type.__name__ = "Integer32"
_CcmeMohSource_Object = MibScalar
ccmeMohSource = _CcmeMohSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 7),
    _CcmeMohSource_Type()
)
ccmeMohSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeMohSource.setStatus("current")
_CcmeNightServiceEnabled_Type = TruthValue
_CcmeNightServiceEnabled_Object = MibScalar
ccmeNightServiceEnabled = _CcmeNightServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 8),
    _CcmeNightServiceEnabled_Type()
)
ccmeNightServiceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeNightServiceEnabled.setStatus("current")
_CcmeEMphoneTot_Type = Counter32
_CcmeEMphoneTot_Object = MibScalar
ccmeEMphoneTot = _CcmeEMphoneTot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 9),
    _CcmeEMphoneTot_Type()
)
ccmeEMphoneTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEMphoneTot.setStatus("current")
_CcmeEMphoneTotRegistered_Type = Gauge32
_CcmeEMphoneTotRegistered_Object = MibScalar
ccmeEMphoneTotRegistered = _CcmeEMphoneTotRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 2, 10),
    _CcmeEMphoneTotRegistered_Type()
)
ccmeEMphoneTotRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEMphoneTotRegistered.setStatus("current")
_CcmeHistoryStats_ObjectIdentity = ObjectIdentity
ccmeHistoryStats = _CcmeHistoryStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3)
)
_CcmeEphoneDnChStatsHistoryTable_Object = MibTable
ccmeEphoneDnChStatsHistoryTable = _CcmeEphoneDnChStatsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccmeEphoneDnChStatsHistoryTable.setStatus("current")
_CcmeEphoneDnChStatsHistoryEntry_Object = MibTableRow
ccmeEphoneDnChStatsHistoryEntry = _CcmeEphoneDnChStatsHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1)
)
ccmeEphoneDnChStatsHistoryEntry.setIndexNames(
    (0, "CISCO-CCME-MIB", "ccmeEphoneDnTag"),
    (0, "CISCO-CCME-MIB", "ccmeEphoneDnChNum"),
)
if mibBuilder.loadTexts:
    ccmeEphoneDnChStatsHistoryEntry.setStatus("current")


class _CcmeEphoneDnChNum_Type(Integer32):
    """Custom type ccmeEphoneDnChNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CcmeEphoneDnChNum_Type.__name__ = "Integer32"
_CcmeEphoneDnChNum_Object = MibTableColumn
ccmeEphoneDnChNum = _CcmeEphoneDnChNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 1),
    _CcmeEphoneDnChNum_Type()
)
ccmeEphoneDnChNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmeEphoneDnChNum.setStatus("current")
_CcmeEphoneDnChIncoming_Type = Counter32
_CcmeEphoneDnChIncoming_Object = MibTableColumn
ccmeEphoneDnChIncoming = _CcmeEphoneDnChIncoming_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 2),
    _CcmeEphoneDnChIncoming_Type()
)
ccmeEphoneDnChIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnChIncoming.setStatus("current")
_CcmeEphoneDnChInAnswered_Type = Counter32
_CcmeEphoneDnChInAnswered_Object = MibTableColumn
ccmeEphoneDnChInAnswered = _CcmeEphoneDnChInAnswered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 3),
    _CcmeEphoneDnChInAnswered_Type()
)
ccmeEphoneDnChInAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnChInAnswered.setStatus("current")
_CcmeEphoneDnChOutbound_Type = Counter32
_CcmeEphoneDnChOutbound_Object = MibTableColumn
ccmeEphoneDnChOutbound = _CcmeEphoneDnChOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 4),
    _CcmeEphoneDnChOutbound_Type()
)
ccmeEphoneDnChOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnChOutbound.setStatus("current")
_CcmeEphoneDnChOutAnswered_Type = Counter32
_CcmeEphoneDnChOutAnswered_Object = MibTableColumn
ccmeEphoneDnChOutAnswered = _CcmeEphoneDnChOutAnswered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 5),
    _CcmeEphoneDnChOutAnswered_Type()
)
ccmeEphoneDnChOutAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnChOutAnswered.setStatus("current")
_CcmeEphoneDnChOutBusy_Type = Counter32
_CcmeEphoneDnChOutBusy_Object = MibTableColumn
ccmeEphoneDnChOutBusy = _CcmeEphoneDnChOutBusy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 6),
    _CcmeEphoneDnChOutBusy_Type()
)
ccmeEphoneDnChOutBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnChOutBusy.setStatus("current")
_CcmeEphoneDnChDiscAtConn_Type = Counter32
_CcmeEphoneDnChDiscAtConn_Object = MibTableColumn
ccmeEphoneDnChDiscAtConn = _CcmeEphoneDnChDiscAtConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 7),
    _CcmeEphoneDnChDiscAtConn_Type()
)
ccmeEphoneDnChDiscAtConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnChDiscAtConn.setStatus("current")
_CcmeEphoneDnChDiscAtAlert_Type = Counter32
_CcmeEphoneDnChDiscAtAlert_Object = MibTableColumn
ccmeEphoneDnChDiscAtAlert = _CcmeEphoneDnChDiscAtAlert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 8),
    _CcmeEphoneDnChDiscAtAlert_Type()
)
ccmeEphoneDnChDiscAtAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnChDiscAtAlert.setStatus("current")
_CcmeEphoneDnChDiscAtHold_Type = Counter32
_CcmeEphoneDnChDiscAtHold_Object = MibTableColumn
ccmeEphoneDnChDiscAtHold = _CcmeEphoneDnChDiscAtHold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 9),
    _CcmeEphoneDnChDiscAtHold_Type()
)
ccmeEphoneDnChDiscAtHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnChDiscAtHold.setStatus("current")
_CcmeEphoneDnChDiscAtRing_Type = Counter32
_CcmeEphoneDnChDiscAtRing_Object = MibTableColumn
ccmeEphoneDnChDiscAtRing = _CcmeEphoneDnChDiscAtRing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 10),
    _CcmeEphoneDnChDiscAtRing_Type()
)
ccmeEphoneDnChDiscAtRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnChDiscAtRing.setStatus("current")
_CcmeEphoneDnChDiscCauseNearEnd_Type = Integer32
_CcmeEphoneDnChDiscCauseNearEnd_Object = MibTableColumn
ccmeEphoneDnChDiscCauseNearEnd = _CcmeEphoneDnChDiscCauseNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 11),
    _CcmeEphoneDnChDiscCauseNearEnd_Type()
)
ccmeEphoneDnChDiscCauseNearEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnChDiscCauseNearEnd.setStatus("current")
_CcmeEphoneDnChDiscCauseFarEnd_Type = Integer32
_CcmeEphoneDnChDiscCauseFarEnd_Object = MibTableColumn
ccmeEphoneDnChDiscCauseFarEnd = _CcmeEphoneDnChDiscCauseFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 1, 3, 1, 1, 12),
    _CcmeEphoneDnChDiscCauseFarEnd_Type()
)
ccmeEphoneDnChDiscCauseFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmeEphoneDnChDiscCauseFarEnd.setStatus("current")
_CiscoCcmeMIBConform_ObjectIdentity = ObjectIdentity
ciscoCcmeMIBConform = _CiscoCcmeMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2)
)
_CiscoCcmeMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCcmeMIBCompliances = _CiscoCcmeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 1)
)
_CiscoCcmeMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCcmeMIBGroups = _CiscoCcmeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 2)
)

# Managed Objects groups

ccmeConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 2, 1)
)
ccmeConfigGroup.setObjects(
      *(("CISCO-CCME-MIB", "ccmeEnabled"),
        ("CISCO-CCME-MIB", "ccmeVersion"),
        ("CISCO-CCME-MIB", "ccmeIPAddressType"),
        ("CISCO-CCME-MIB", "ccmeIPAddress"),
        ("CISCO-CCME-MIB", "ccmePortNumber"),
        ("CISCO-CCME-MIB", "ccmeMaxEphones"),
        ("CISCO-CCME-MIB", "ccmeMaxDirectoryNumber"),
        ("CISCO-CCME-MIB", "ccmeMaxConferences"),
        ("CISCO-CCME-MIB", "ccmeMaxRedirect"),
        ("CISCO-CCME-MIB", "ccmeScriptName"),
        ("CISCO-CCME-MIB", "ccmeVoiceMailNumber"),
        ("CISCO-CCME-MIB", "ccmeMwiRelay"),
        ("CISCO-CCME-MIB", "ccmeMwiExpires"),
        ("CISCO-CCME-MIB", "ccmeTransferSystem"),
        ("CISCO-CCME-MIB", "ccmeTimeFormat"),
        ("CISCO-CCME-MIB", "ccmeDateFormat"),
        ("CISCO-CCME-MIB", "ccmeUrlforServicesBtn"),
        ("CISCO-CCME-MIB", "ccmeUrlforDirectoriesBtn"),
        ("CISCO-CCME-MIB", "ccmeMohFlashFile"),
        ("CISCO-CCME-MIB", "ccmeMohMulticastFromFlashEnabled"),
        ("CISCO-CCME-MIB", "ccmeMohFlashMulticastIPAddrType"),
        ("CISCO-CCME-MIB", "ccmeMohFlashMulticastIPAddr"),
        ("CISCO-CCME-MIB", "ccmeMohFlashMulticastPortNum"),
        ("CISCO-CCME-MIB", "ccmePhoneType"),
        ("CISCO-CCME-MIB", "ccmePhoneFirmwareRev"),
        ("CISCO-CCME-MIB", "ccmeTransferPattern"),
        ("CISCO-CCME-MIB", "ccmeTransferPatternType"),
        ("CISCO-CCME-MIB", "ccmeWebGUIEditEnabled"),
        ("CISCO-CCME-MIB", "ccmeWebGUITimeEnabled"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockPattern"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockPatternAllTime"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockDateMonth"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockDate"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockDateStartHour"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockDateStartMin"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockDateStopHour"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockDateStopMin"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockDay"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockDayStartHour"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockDayStartMin"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockDayStopHour"),
        ("CISCO-CCME-MIB", "ccmeAfterHrsBlockDayStopMin"),
        ("CISCO-CCME-MIB", "ccmeNightServiceCode"),
        ("CISCO-CCME-MIB", "ccmeNightServiceDateMonth"),
        ("CISCO-CCME-MIB", "ccmeNightServiceDate"),
        ("CISCO-CCME-MIB", "ccmeNightServiceDateStartHour"),
        ("CISCO-CCME-MIB", "ccmeNightServiceDateStartMin"),
        ("CISCO-CCME-MIB", "ccmeNightServiceDateStopHour"),
        ("CISCO-CCME-MIB", "ccmeNightServiceDateStopMin"),
        ("CISCO-CCME-MIB", "ccmeNightServiceDay"),
        ("CISCO-CCME-MIB", "ccmeNightServiceDayStartHour"),
        ("CISCO-CCME-MIB", "ccmeNightServiceDayStartMin"),
        ("CISCO-CCME-MIB", "ccmeNightServiceDayStopHour"),
        ("CISCO-CCME-MIB", "ccmeNightServiceDayStopMin"),
        ("CISCO-CCME-MIB", "ccmeFXOHookFlashEnabled"),
        ("CISCO-CCME-MIB", "ccmeSecondaryDialTonePrefix"),
        ("CISCO-CCME-MIB", "ccmeWebAdminSystemUser"),
        ("CISCO-CCME-MIB", "ccmeWebAdminCustomerUser"),
        ("CISCO-CCME-MIB", "ccmeSystemMessage"),
        ("CISCO-CCME-MIB", "ccmeDialplanPatternTag"),
        ("CISCO-CCME-MIB", "ccmeDialplanPattern"),
        ("CISCO-CCME-MIB", "ccmeDialplanExtLength"),
        ("CISCO-CCME-MIB", "ccmeDialplanExtPattern"),
        ("CISCO-CCME-MIB", "ccmeDialplanAllowRegiEnabled"),
        ("CISCO-CCME-MIB", "ccmeKeepAliveTimeout"),
        ("CISCO-CCME-MIB", "ccmeInterDigitTimeout"),
        ("CISCO-CCME-MIB", "ccmeBusyTimeout"),
        ("CISCO-CCME-MIB", "ccmeAlertTimeout"),
        ("CISCO-CCME-MIB", "ccmeEphoneIpAddressType"),
        ("CISCO-CCME-MIB", "ccmeEphoneIpAddress"),
        ("CISCO-CCME-MIB", "ccmeEphoneMacAddress"),
        ("CISCO-CCME-MIB", "ccmeEphoneModel"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnType"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnMode"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnPriNum"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnSecNum"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnName"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnLabel"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnPriPref"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnSecPref"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnCFBusyNum"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnCFAllNum"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnCFNoAnNum"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnCFNoAnTo"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnMwiCapability"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnHuntstop"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnHuntstopCh"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnHoldAltTo"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnHoldAltType"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnMwiSipSubscrEnabled"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnScriptName"),
        ("CISCO-CCME-MIB", "ccmeEphoneUsername"),
        ("CISCO-CCME-MIB", "ccmeNotificationEnable"),
        ("CISCO-CCME-MIB", "ccmeSysTrapSeverity"),
        ("CISCO-CCME-MIB", "ccmeSysNotificationReason"),
        ("CISCO-CCME-MIB", "ccmeEphoneUnRegThreshold"),
        ("CISCO-CCME-MIB", "ccmeEphoneKeyPhone"),
        ("CISCO-CCME-MIB", "ccmeEphoneKeepAlive"),
        ("CISCO-CCME-MIB", "ccmeEphoneAutoLineInEnabled"),
        ("CISCO-CCME-MIB", "ccmeEphoneAutoLineOut"),
        ("CISCO-CCME-MIB", "ccmeEphonePagingDn"),
        ("CISCO-CCME-MIB", "ccmeEphonePagingPolicy"),
        ("CISCO-CCME-MIB", "ccmeEphoneTemplate"),
        ("CISCO-CCME-MIB", "ccmeEphoneAftHrsBlkExmptEnabled"),
        ("CISCO-CCME-MIB", "ccmeEphoneNightBellSvcEnabled"),
        ("CISCO-CCME-MIB", "ccmeEphoneAddon"),
        ("CISCO-CCME-MIB", "ccmeEphoneKeepConfEnabled"),
        ("CISCO-CCME-MIB", "ccmeEphoneTrapReason"),
        ("CISCO-CCME-MIB", "ccmeUserAutoLogoutTo"),
        ("CISCO-CCME-MIB", "ccmeUserLoginDeactivateTime"),
        ("CISCO-CCME-MIB", "ccmeMwiSipServerIpAddress"),
        ("CISCO-CCME-MIB", "ccmeMwiSipServerTransportType"),
        ("CISCO-CCME-MIB", "ccmeMwiSipServerPortNumber"),
        ("CISCO-CCME-MIB", "ccmeMwiSipServerRegE164Enabled"),
        ("CISCO-CCME-MIB", "ccmeMwiSipSvrUnsolicitedEnabled"),
        ("CISCO-CCME-MIB", "ccmeCorTag"),
        ("CISCO-CCME-MIB", "ccmeCorListName"),
        ("CISCO-CCME-MIB", "ccmeCorScope"),
        ("CISCO-CCME-MIB", "ccmeCorDirection"),
        ("CISCO-CCME-MIB", "ccmeCorStartingNumber"),
        ("CISCO-CCME-MIB", "ccmeCorEndingNumber"),
        ("CISCO-CCME-MIB", "ccmeCorVoiceRegPoolNumber"),
        ("CISCO-CCME-MIB", "ccmeCorListDefaultEnabled"),
        ("CISCO-CCME-MIB", "ccmeLoopbackDnforward"),
        ("CISCO-CCME-MIB", "ccmeLoopbackDnStrip"),
        ("CISCO-CCME-MIB", "ccmeLoopbackDnPrefix"),
        ("CISCO-CCME-MIB", "ccmeLoopbackDnSuffix"),
        ("CISCO-CCME-MIB", "ccmeLoopbackDnRetryTo"),
        ("CISCO-CCME-MIB", "ccmeLoopbackDnAutoCon"),
        ("CISCO-CCME-MIB", "ccmeLoopbackDnCodec"),
        ("CISCO-CCME-MIB", "ccmeIntercomDnExtensionNum"),
        ("CISCO-CCME-MIB", "ccmeIntercomDnBargeInEnabled"),
        ("CISCO-CCME-MIB", "ccmeIntercomDnAutoAnsEnabled"),
        ("CISCO-CCME-MIB", "ccmeIntercomDnLabel"),
        ("CISCO-CCME-MIB", "ccmeEphoneSpeedDialTag"),
        ("CISCO-CCME-MIB", "ccmeEphoneSpeedDialNumber"),
        ("CISCO-CCME-MIB", "ccmeEphoneSpeedDialLabel"),
        ("CISCO-CCME-MIB", "ccmeEphoneFastDialNumber"),
        ("CISCO-CCME-MIB", "ccmeEphoneFastDialName"),
        ("CISCO-CCME-MIB", "ccmeEphoneOverlayDN"),
        ("CISCO-CCME-MIB", "ccmeMohMulticastIpAddressType"),
        ("CISCO-CCME-MIB", "ccmeMohMulticastIpAddress"),
        ("CISCO-CCME-MIB", "ccmeMohMulticastPortNumber"),
        ("CISCO-CCME-MIB", "ccmeMohMulticastRoute"))
)
if mibBuilder.loadTexts:
    ccmeConfigGroup.setStatus("current")

ccmeActiveStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 2, 2)
)
ccmeActiveStatsGroup.setObjects(
      *(("CISCO-CCME-MIB", "ccmeEphoneCallLegs"),
        ("CISCO-CCME-MIB", "ccmeEphoneTot"),
        ("CISCO-CCME-MIB", "ccmeEphoneTotRegistered"),
        ("CISCO-CCME-MIB", "ccmeEphoneTotKeyPhConfigured"),
        ("CISCO-CCME-MIB", "ccmeEphoneTotKeyPhRegistered"),
        ("CISCO-CCME-MIB", "ccmeEphoneDeviceName"),
        ("CISCO-CCME-MIB", "ccmeEphoneRegState"),
        ("CISCO-CCME-MIB", "ccmeEphoneActiveDN"),
        ("CISCO-CCME-MIB", "ccmeEphoneActivityStatus"),
        ("CISCO-CCME-MIB", "ccmeEphoneKeepAliveCnt"),
        ("CISCO-CCME-MIB", "ccmeEphonePendingReset"),
        ("CISCO-CCME-MIB", "ccmeEphoneRegTime"),
        ("CISCO-CCME-MIB", "ccmeEphoneCurrentFirmwareRev"),
        ("CISCO-CCME-MIB", "ccmeEphonePreviousFirmwareRev"),
        ("CISCO-CCME-MIB", "ccmeEphoneLastError"),
        ("CISCO-CCME-MIB", "ccmeEphoneObservedType"),
        ("CISCO-CCME-MIB", "ccmeEphoneLoginStatus"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnDStatus"),
        ("CISCO-CCME-MIB", "ccmeEphoneDebugStatus"),
        ("CISCO-CCME-MIB", "ccmeEphoneMediaActive"),
        ("CISCO-CCME-MIB", "ccmeEphoneTAPIClient"),
        ("CISCO-CCME-MIB", "ccmeEphoneMediaCapability"),
        ("CISCO-CCME-MIB", "ccmeEphoneRemote"),
        ("CISCO-CCME-MIB", "ccmeMohSource"),
        ("CISCO-CCME-MIB", "ccmeNightServiceEnabled"))
)
if mibBuilder.loadTexts:
    ccmeActiveStatsGroup.setStatus("current")

ccmeHistoryStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 2, 3)
)
ccmeHistoryStatsGroup.setObjects(
      *(("CISCO-CCME-MIB", "ccmeEphoneDnChIncoming"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnChInAnswered"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnChOutbound"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnChOutAnswered"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnChOutBusy"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnChDiscAtConn"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnChDiscAtAlert"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnChDiscAtHold"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnChDiscAtRing"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnChDiscCauseNearEnd"),
        ("CISCO-CCME-MIB", "ccmeEphoneDnChDiscCauseFarEnd"))
)
if mibBuilder.loadTexts:
    ccmeHistoryStatsGroup.setStatus("current")

ccmeConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 2, 5)
)
ccmeConfigGroup1.setObjects(
    ("CISCO-CCME-MIB", "ccmeEphonePrimaryDn")
)
if mibBuilder.loadTexts:
    ccmeConfigGroup1.setStatus("current")

ccmeConfigGroupEM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 2, 6)
)
ccmeConfigGroupEM.setObjects(
      *(("CISCO-CCME-MIB", "ccmeEMUserProfileTag"),
        ("CISCO-CCME-MIB", "ccmeEMLogOutProfileTag"),
        ("CISCO-CCME-MIB", "ccmeEMUserDirNum"),
        ("CISCO-CCME-MIB", "ccmeEMUserDirNumOverlay"),
        ("CISCO-CCME-MIB", "ccmeEMLogoutDirNum"),
        ("CISCO-CCME-MIB", "ccmeEMLogoutDirNumOverlay"))
)
if mibBuilder.loadTexts:
    ccmeConfigGroupEM.setStatus("current")

ccmeActiveStatsGroupEM = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 2, 7)
)
ccmeActiveStatsGroupEM.setObjects(
      *(("CISCO-CCME-MIB", "ccmeEMphoneTot"),
        ("CISCO-CCME-MIB", "ccmeEMphoneTotRegistered"))
)
if mibBuilder.loadTexts:
    ccmeActiveStatsGroupEM.setStatus("current")


# Notification objects

ccmeStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 0, 0, 1)
)
ccmeStatusChangeNotif.setObjects(
      *(("CISCO-CCME-MIB", "ccmeSysTrapSeverity"),
        ("CISCO-CCME-MIB", "ccmeEnabled"),
        ("CISCO-CCME-MIB", "ccmeSysNotificationReason"))
)
if mibBuilder.loadTexts:
    ccmeStatusChangeNotif.setStatus(
        "current"
    )

ccmeEphoneUnRegThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 0, 0, 2)
)
ccmeEphoneUnRegThresholdExceed.setObjects(
    ("CISCO-CCME-MIB", "ccmeEphoneUnRegThreshold")
)
if mibBuilder.loadTexts:
    ccmeEphoneUnRegThresholdExceed.setStatus(
        "current"
    )

ccmeEPhoneDeceased = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 0, 0, 3)
)
ccmeEPhoneDeceased.setObjects(
      *(("CISCO-CCME-MIB", "ccmeEphoneIpAddress"),
        ("CISCO-CCME-MIB", "ccmeEphoneRegState"))
)
if mibBuilder.loadTexts:
    ccmeEPhoneDeceased.setStatus(
        "current"
    )

ccmeEPhoneRegFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 0, 0, 4)
)
ccmeEPhoneRegFailed.setObjects(
      *(("CISCO-CCME-MIB", "ccmeEphoneIpAddress"),
        ("CISCO-CCME-MIB", "ccmeEphoneTrapReason"))
)
if mibBuilder.loadTexts:
    ccmeEPhoneRegFailed.setStatus(
        "current"
    )

ccmeEphoneLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 0, 0, 5)
)
ccmeEphoneLoginFailed.setObjects(
      *(("CISCO-CCME-MIB", "ccmeEphoneIpAddress"),
        ("CISCO-CCME-MIB", "ccmeEphoneTrapReason"))
)
if mibBuilder.loadTexts:
    ccmeEphoneLoginFailed.setStatus(
        "current"
    )

ccmeNightServiceChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 0, 0, 6)
)
ccmeNightServiceChangeNotif.setObjects(
    ("CISCO-CCME-MIB", "ccmeEphoneTrapReason")
)
if mibBuilder.loadTexts:
    ccmeNightServiceChangeNotif.setStatus(
        "current"
    )

ccmeLivefeedMohFailedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 0, 0, 7)
)
ccmeLivefeedMohFailedNotif.setObjects(
    ("CISCO-CCME-MIB", "ccmeEphoneTrapReason")
)
if mibBuilder.loadTexts:
    ccmeLivefeedMohFailedNotif.setStatus(
        "current"
    )

ccmeMaxConferenceNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 0, 0, 8)
)
ccmeMaxConferenceNotif.setObjects(
    ("CISCO-CCME-MIB", "ccmeEphoneTrapReason")
)
if mibBuilder.loadTexts:
    ccmeMaxConferenceNotif.setStatus(
        "current"
    )

ccmeKeyEphoneRegChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 0, 0, 9)
)
ccmeKeyEphoneRegChangeNotif.setObjects(
      *(("CISCO-CCME-MIB", "ccmeEphoneIpAddress"),
        ("CISCO-CCME-MIB", "ccmeEphoneRegState"))
)
if mibBuilder.loadTexts:
    ccmeKeyEphoneRegChangeNotif.setStatus(
        "current"
    )


# Notifications groups

ccmeNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 2, 4)
)
ccmeNotifGroup.setObjects(
      *(("CISCO-CCME-MIB", "ccmeStatusChangeNotif"),
        ("CISCO-CCME-MIB", "ccmeEphoneUnRegThresholdExceed"),
        ("CISCO-CCME-MIB", "ccmeEPhoneDeceased"),
        ("CISCO-CCME-MIB", "ccmeEPhoneRegFailed"),
        ("CISCO-CCME-MIB", "ccmeEphoneLoginFailed"),
        ("CISCO-CCME-MIB", "ccmeNightServiceChangeNotif"),
        ("CISCO-CCME-MIB", "ccmeLivefeedMohFailedNotif"),
        ("CISCO-CCME-MIB", "ccmeMaxConferenceNotif"),
        ("CISCO-CCME-MIB", "ccmeKeyEphoneRegChangeNotif"))
)
if mibBuilder.loadTexts:
    ccmeNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCcmeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCcmeMIBCompliance.setStatus(
        "deprecated"
    )

ciscoCcmeMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCcmeMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoCcmeMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 439, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoCcmeMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CCME-MIB",
    **{"CcmeDigitPatternString": CcmeDigitPatternString,
       "CcmeNightServiceCodeString": CcmeNightServiceCodeString,
       "ciscoCcmeMIB": ciscoCcmeMIB,
       "ciscoCcmeMIBNotifs": ciscoCcmeMIBNotifs,
       "ccmeMIBNotifications": ccmeMIBNotifications,
       "ccmeStatusChangeNotif": ccmeStatusChangeNotif,
       "ccmeEphoneUnRegThresholdExceed": ccmeEphoneUnRegThresholdExceed,
       "ccmeEPhoneDeceased": ccmeEPhoneDeceased,
       "ccmeEPhoneRegFailed": ccmeEPhoneRegFailed,
       "ccmeEphoneLoginFailed": ccmeEphoneLoginFailed,
       "ccmeNightServiceChangeNotif": ccmeNightServiceChangeNotif,
       "ccmeLivefeedMohFailedNotif": ccmeLivefeedMohFailedNotif,
       "ccmeMaxConferenceNotif": ccmeMaxConferenceNotif,
       "ccmeKeyEphoneRegChangeNotif": ccmeKeyEphoneRegChangeNotif,
       "ciscoCcmeMIBObjects": ciscoCcmeMIBObjects,
       "ccmeConfig": ccmeConfig,
       "ccmeEnabled": ccmeEnabled,
       "ccmeVersion": ccmeVersion,
       "ccmeIPAddressType": ccmeIPAddressType,
       "ccmeIPAddress": ccmeIPAddress,
       "ccmePortNumber": ccmePortNumber,
       "ccmeMaxEphones": ccmeMaxEphones,
       "ccmeMaxDirectoryNumber": ccmeMaxDirectoryNumber,
       "ccmeMaxConferences": ccmeMaxConferences,
       "ccmeMaxRedirect": ccmeMaxRedirect,
       "ccmeScriptName": ccmeScriptName,
       "ccmeVoiceMailNumber": ccmeVoiceMailNumber,
       "ccmeMwiRelay": ccmeMwiRelay,
       "ccmeMwiExpires": ccmeMwiExpires,
       "ccmeTransferSystem": ccmeTransferSystem,
       "ccmeTimeFormat": ccmeTimeFormat,
       "ccmeDateFormat": ccmeDateFormat,
       "ccmeUrlforServicesBtn": ccmeUrlforServicesBtn,
       "ccmeUrlforDirectoriesBtn": ccmeUrlforDirectoriesBtn,
       "ccmeMohFlashFile": ccmeMohFlashFile,
       "ccmeMohMulticastFromFlashEnabled": ccmeMohMulticastFromFlashEnabled,
       "ccmeMohFlashMulticastIPAddr": ccmeMohFlashMulticastIPAddr,
       "ccmeMohFlashMulticastPortNum": ccmeMohFlashMulticastPortNum,
       "ccmePhoneFirmwareTable": ccmePhoneFirmwareTable,
       "ccmePhoneFirmwareEntry": ccmePhoneFirmwareEntry,
       "ccmePhoneFirmwareIndex": ccmePhoneFirmwareIndex,
       "ccmePhoneType": ccmePhoneType,
       "ccmePhoneFirmwareRev": ccmePhoneFirmwareRev,
       "ccmeTransferPatternTable": ccmeTransferPatternTable,
       "ccmeTransferPatternEntry": ccmeTransferPatternEntry,
       "ccmeTransferPatternIndex": ccmeTransferPatternIndex,
       "ccmeTransferPattern": ccmeTransferPattern,
       "ccmeTransferPatternType": ccmeTransferPatternType,
       "ccmeWebGUIEditEnabled": ccmeWebGUIEditEnabled,
       "ccmeWebGUITimeEnabled": ccmeWebGUITimeEnabled,
       "ccmeAfterHrsBlockPatternTable": ccmeAfterHrsBlockPatternTable,
       "ccmeAfterHrsBlockPatternEntry": ccmeAfterHrsBlockPatternEntry,
       "ccmeAfterHrsBlockPatternTag": ccmeAfterHrsBlockPatternTag,
       "ccmeAfterHrsBlockPattern": ccmeAfterHrsBlockPattern,
       "ccmeAfterHrsBlockPatternAllTime": ccmeAfterHrsBlockPatternAllTime,
       "ccmeAfterHrsBlockDateTable": ccmeAfterHrsBlockDateTable,
       "ccmeAfterHrsBlockDateEntry": ccmeAfterHrsBlockDateEntry,
       "ccmeAfterHrsBlockDateIndex": ccmeAfterHrsBlockDateIndex,
       "ccmeAfterHrsBlockDateMonth": ccmeAfterHrsBlockDateMonth,
       "ccmeAfterHrsBlockDate": ccmeAfterHrsBlockDate,
       "ccmeAfterHrsBlockDateStartHour": ccmeAfterHrsBlockDateStartHour,
       "ccmeAfterHrsBlockDateStartMin": ccmeAfterHrsBlockDateStartMin,
       "ccmeAfterHrsBlockDateStopHour": ccmeAfterHrsBlockDateStopHour,
       "ccmeAfterHrsBlockDateStopMin": ccmeAfterHrsBlockDateStopMin,
       "ccmeAfterHrsBlockDayTable": ccmeAfterHrsBlockDayTable,
       "ccmeAfterHrsBlockDayEntry": ccmeAfterHrsBlockDayEntry,
       "ccmeAfterHrsBlockDayIndex": ccmeAfterHrsBlockDayIndex,
       "ccmeAfterHrsBlockDay": ccmeAfterHrsBlockDay,
       "ccmeAfterHrsBlockDayStartHour": ccmeAfterHrsBlockDayStartHour,
       "ccmeAfterHrsBlockDayStartMin": ccmeAfterHrsBlockDayStartMin,
       "ccmeAfterHrsBlockDayStopHour": ccmeAfterHrsBlockDayStopHour,
       "ccmeAfterHrsBlockDayStopMin": ccmeAfterHrsBlockDayStopMin,
       "ccmeNightServiceCode": ccmeNightServiceCode,
       "ccmeNightServiceDateTable": ccmeNightServiceDateTable,
       "ccmeNightServiceDateEntry": ccmeNightServiceDateEntry,
       "ccmeNightServiceDateIndex": ccmeNightServiceDateIndex,
       "ccmeNightServiceDateMonth": ccmeNightServiceDateMonth,
       "ccmeNightServiceDate": ccmeNightServiceDate,
       "ccmeNightServiceDateStartHour": ccmeNightServiceDateStartHour,
       "ccmeNightServiceDateStartMin": ccmeNightServiceDateStartMin,
       "ccmeNightServiceDateStopHour": ccmeNightServiceDateStopHour,
       "ccmeNightServiceDateStopMin": ccmeNightServiceDateStopMin,
       "ccmeNightServiceDayTable": ccmeNightServiceDayTable,
       "ccmeNightServiceDayEntry": ccmeNightServiceDayEntry,
       "ccmeNightServiceDayIndex": ccmeNightServiceDayIndex,
       "ccmeNightServiceDay": ccmeNightServiceDay,
       "ccmeNightServiceDayStartHour": ccmeNightServiceDayStartHour,
       "ccmeNightServiceDayStartMin": ccmeNightServiceDayStartMin,
       "ccmeNightServiceDayStopHour": ccmeNightServiceDayStopHour,
       "ccmeNightServiceDayStopMin": ccmeNightServiceDayStopMin,
       "ccmeFXOHookFlashEnabled": ccmeFXOHookFlashEnabled,
       "ccmeSecondaryDialTonePrefix": ccmeSecondaryDialTonePrefix,
       "ccmeWebAdminSystemUser": ccmeWebAdminSystemUser,
       "ccmeWebAdminCustomerUser": ccmeWebAdminCustomerUser,
       "ccmeSystemMessage": ccmeSystemMessage,
       "ccmeDialplanPatternTable": ccmeDialplanPatternTable,
       "ccmeDialplanPatternEntry": ccmeDialplanPatternEntry,
       "ccmeDialplanPatternIndex": ccmeDialplanPatternIndex,
       "ccmeDialplanPatternTag": ccmeDialplanPatternTag,
       "ccmeDialplanExtLength": ccmeDialplanExtLength,
       "ccmeDialplanPattern": ccmeDialplanPattern,
       "ccmeDialplanExtPattern": ccmeDialplanExtPattern,
       "ccmeDialplanAllowRegiEnabled": ccmeDialplanAllowRegiEnabled,
       "ccmeKeepAliveTimeout": ccmeKeepAliveTimeout,
       "ccmeInterDigitTimeout": ccmeInterDigitTimeout,
       "ccmeBusyTimeout": ccmeBusyTimeout,
       "ccmeAlertTimeout": ccmeAlertTimeout,
       "ccmeEphoneConfTable": ccmeEphoneConfTable,
       "ccmeEphoneConfEntry": ccmeEphoneConfEntry,
       "ccmeEphoneTag": ccmeEphoneTag,
       "ccmeEphoneIpAddressType": ccmeEphoneIpAddressType,
       "ccmeEphoneIpAddress": ccmeEphoneIpAddress,
       "ccmeEphoneMacAddress": ccmeEphoneMacAddress,
       "ccmeEphoneModel": ccmeEphoneModel,
       "ccmeEphoneUsername": ccmeEphoneUsername,
       "ccmeEphoneKeepAlive": ccmeEphoneKeepAlive,
       "ccmeEphoneAutoLineOut": ccmeEphoneAutoLineOut,
       "ccmeEphonePagingDn": ccmeEphonePagingDn,
       "ccmeEphoneAddon": ccmeEphoneAddon,
       "ccmeEphoneTemplate": ccmeEphoneTemplate,
       "ccmeEphonePagingPolicy": ccmeEphonePagingPolicy,
       "ccmeEphoneKeyPhone": ccmeEphoneKeyPhone,
       "ccmeEphoneAutoLineInEnabled": ccmeEphoneAutoLineInEnabled,
       "ccmeEphoneAftHrsBlkExmptEnabled": ccmeEphoneAftHrsBlkExmptEnabled,
       "ccmeEphoneNightBellSvcEnabled": ccmeEphoneNightBellSvcEnabled,
       "ccmeEphoneKeepConfEnabled": ccmeEphoneKeepConfEnabled,
       "ccmeEphonePrimaryDn": ccmeEphonePrimaryDn,
       "ccmeEMUserProfileTag": ccmeEMUserProfileTag,
       "ccmeEMLogOutProfileTag": ccmeEMLogOutProfileTag,
       "ccmeEphoneSpeedDialConfTable": ccmeEphoneSpeedDialConfTable,
       "ccmeEphoneSpeedDialConfEntry": ccmeEphoneSpeedDialConfEntry,
       "ccmeEphoneSpeedDialTableIndex": ccmeEphoneSpeedDialTableIndex,
       "ccmeEphoneSpeedDialTag": ccmeEphoneSpeedDialTag,
       "ccmeEphoneSpeedDialNumber": ccmeEphoneSpeedDialNumber,
       "ccmeEphoneSpeedDialLabel": ccmeEphoneSpeedDialLabel,
       "ccmeEphoneFastDialConfTable": ccmeEphoneFastDialConfTable,
       "ccmeEphoneFastDialConfEntry": ccmeEphoneFastDialConfEntry,
       "ccmeEphoneFastDialTableIndex": ccmeEphoneFastDialTableIndex,
       "ccmeEphoneFastDialNumber": ccmeEphoneFastDialNumber,
       "ccmeEphoneFastDialName": ccmeEphoneFastDialName,
       "ccmeEphoneBtnDNAssocConfTable": ccmeEphoneBtnDNAssocConfTable,
       "ccmeEphoneBtnDNAssocConfEntry": ccmeEphoneBtnDNAssocConfEntry,
       "ccmeEphoneButtonNumber": ccmeEphoneButtonNumber,
       "ccmeEphoneOverlayDN": ccmeEphoneOverlayDN,
       "ccmeEphoneDnConfigTable": ccmeEphoneDnConfigTable,
       "ccmeEphoneDnConfigEntry": ccmeEphoneDnConfigEntry,
       "ccmeEphoneDnTag": ccmeEphoneDnTag,
       "ccmeEphoneDnType": ccmeEphoneDnType,
       "ccmeEphoneDnMode": ccmeEphoneDnMode,
       "ccmeEphoneDnPriNum": ccmeEphoneDnPriNum,
       "ccmeEphoneDnSecNum": ccmeEphoneDnSecNum,
       "ccmeEphoneDnName": ccmeEphoneDnName,
       "ccmeEphoneDnLabel": ccmeEphoneDnLabel,
       "ccmeEphoneDnPriPref": ccmeEphoneDnPriPref,
       "ccmeEphoneDnSecPref": ccmeEphoneDnSecPref,
       "ccmeEphoneDnCFBusyNum": ccmeEphoneDnCFBusyNum,
       "ccmeEphoneDnCFAllNum": ccmeEphoneDnCFAllNum,
       "ccmeEphoneDnCFNoAnNum": ccmeEphoneDnCFNoAnNum,
       "ccmeEphoneDnCFNoAnTo": ccmeEphoneDnCFNoAnTo,
       "ccmeEphoneDnMwiCapability": ccmeEphoneDnMwiCapability,
       "ccmeEphoneDnHuntstop": ccmeEphoneDnHuntstop,
       "ccmeEphoneDnHuntstopCh": ccmeEphoneDnHuntstopCh,
       "ccmeEphoneDnHoldAltTo": ccmeEphoneDnHoldAltTo,
       "ccmeEphoneDnHoldAltType": ccmeEphoneDnHoldAltType,
       "ccmeEphoneDnMwiSipSubscrEnabled": ccmeEphoneDnMwiSipSubscrEnabled,
       "ccmeEphoneDnScriptName": ccmeEphoneDnScriptName,
       "ccmeNotificationEnable": ccmeNotificationEnable,
       "ccmeSysTrapSeverity": ccmeSysTrapSeverity,
       "ccmeSysNotificationReason": ccmeSysNotificationReason,
       "ccmeEphoneUnRegThreshold": ccmeEphoneUnRegThreshold,
       "ccmeEphoneTrapReason": ccmeEphoneTrapReason,
       "ccmeUserAutoLogoutTo": ccmeUserAutoLogoutTo,
       "ccmeUserLoginDeactivateTime": ccmeUserLoginDeactivateTime,
       "ccmeMwiSipServerIpAddress": ccmeMwiSipServerIpAddress,
       "ccmeMwiSipServerTransportType": ccmeMwiSipServerTransportType,
       "ccmeMwiSipServerPortNumber": ccmeMwiSipServerPortNumber,
       "ccmeMwiSipServerRegE164Enabled": ccmeMwiSipServerRegE164Enabled,
       "ccmeMwiSipSvrUnsolicitedEnabled": ccmeMwiSipSvrUnsolicitedEnabled,
       "ccmeCorConfTable": ccmeCorConfTable,
       "ccmeCorConfEntry": ccmeCorConfEntry,
       "ccmeCorTableIndex": ccmeCorTableIndex,
       "ccmeCorTag": ccmeCorTag,
       "ccmeCorListName": ccmeCorListName,
       "ccmeCorScope": ccmeCorScope,
       "ccmeCorDirection": ccmeCorDirection,
       "ccmeCorStartingNumber": ccmeCorStartingNumber,
       "ccmeCorEndingNumber": ccmeCorEndingNumber,
       "ccmeCorVoiceRegPoolNumber": ccmeCorVoiceRegPoolNumber,
       "ccmeCorListDefaultEnabled": ccmeCorListDefaultEnabled,
       "ccmeLoopbackDnConfTable": ccmeLoopbackDnConfTable,
       "ccmeLoopbackDnConfEntry": ccmeLoopbackDnConfEntry,
       "ccmeLoopbackDnTag": ccmeLoopbackDnTag,
       "ccmeLoopbackDnforward": ccmeLoopbackDnforward,
       "ccmeLoopbackDnStrip": ccmeLoopbackDnStrip,
       "ccmeLoopbackDnPrefix": ccmeLoopbackDnPrefix,
       "ccmeLoopbackDnSuffix": ccmeLoopbackDnSuffix,
       "ccmeLoopbackDnRetryTo": ccmeLoopbackDnRetryTo,
       "ccmeLoopbackDnAutoCon": ccmeLoopbackDnAutoCon,
       "ccmeLoopbackDnCodec": ccmeLoopbackDnCodec,
       "ccmeIntercomDnConfTable": ccmeIntercomDnConfTable,
       "ccmeIntercomDnConfEntry": ccmeIntercomDnConfEntry,
       "ccmeIntercomDnTag": ccmeIntercomDnTag,
       "ccmeIntercomDnExtensionNum": ccmeIntercomDnExtensionNum,
       "ccmeIntercomDnBargeInEnabled": ccmeIntercomDnBargeInEnabled,
       "ccmeIntercomDnAutoAnsEnabled": ccmeIntercomDnAutoAnsEnabled,
       "ccmeIntercomDnLabel": ccmeIntercomDnLabel,
       "ccmeMohMulticastIpAddress": ccmeMohMulticastIpAddress,
       "ccmeMohMulticastPortNumber": ccmeMohMulticastPortNumber,
       "ccmeMohMulticastRoute": ccmeMohMulticastRoute,
       "ccmeMohFlashMulticastIPAddrType": ccmeMohFlashMulticastIPAddrType,
       "ccmeMohMulticastIpAddressType": ccmeMohMulticastIpAddressType,
       "ccmeEMUserDirNumConfTable": ccmeEMUserDirNumConfTable,
       "ccmeEMUserDirNumConfEntry": ccmeEMUserDirNumConfEntry,
       "ccmEMUserProfileDirNumIndex": ccmEMUserProfileDirNumIndex,
       "ccmeEMUserDirNumTag": ccmeEMUserDirNumTag,
       "ccmeEMUserDirNum": ccmeEMUserDirNum,
       "ccmeEMUserDirNumOverlay": ccmeEMUserDirNumOverlay,
       "ccmeEMLogoutDirNumConfTable": ccmeEMLogoutDirNumConfTable,
       "ccmeEMLogoutDirNumConfEntry": ccmeEMLogoutDirNumConfEntry,
       "ccmEMLogOutProfileDirNumIndex": ccmEMLogOutProfileDirNumIndex,
       "ccmeEMLogoutDirNumTag": ccmeEMLogoutDirNumTag,
       "ccmeEMLogoutDirNum": ccmeEMLogoutDirNum,
       "ccmeEMLogoutDirNumOverlay": ccmeEMLogoutDirNumOverlay,
       "ccmeActiveStats": ccmeActiveStats,
       "ccmeEphoneCallLegs": ccmeEphoneCallLegs,
       "ccmeEphoneTot": ccmeEphoneTot,
       "ccmeEphoneTotRegistered": ccmeEphoneTotRegistered,
       "ccmeEphoneTotKeyPhConfigured": ccmeEphoneTotKeyPhConfigured,
       "ccmeEphoneTotKeyPhRegistered": ccmeEphoneTotKeyPhRegistered,
       "ccmeEphoneActTable": ccmeEphoneActTable,
       "ccmeEphoneActEntry": ccmeEphoneActEntry,
       "ccmeEphoneDeviceName": ccmeEphoneDeviceName,
       "ccmeEphoneRegState": ccmeEphoneRegState,
       "ccmeEphoneActiveDN": ccmeEphoneActiveDN,
       "ccmeEphoneActivityStatus": ccmeEphoneActivityStatus,
       "ccmeEphoneKeepAliveCnt": ccmeEphoneKeepAliveCnt,
       "ccmeEphonePendingReset": ccmeEphonePendingReset,
       "ccmeEphoneRegTime": ccmeEphoneRegTime,
       "ccmeEphoneCurrentFirmwareRev": ccmeEphoneCurrentFirmwareRev,
       "ccmeEphonePreviousFirmwareRev": ccmeEphonePreviousFirmwareRev,
       "ccmeEphoneLastError": ccmeEphoneLastError,
       "ccmeEphoneObservedType": ccmeEphoneObservedType,
       "ccmeEphoneLoginStatus": ccmeEphoneLoginStatus,
       "ccmeEphoneDnDStatus": ccmeEphoneDnDStatus,
       "ccmeEphoneDebugStatus": ccmeEphoneDebugStatus,
       "ccmeEphoneMediaActive": ccmeEphoneMediaActive,
       "ccmeEphoneTAPIClient": ccmeEphoneTAPIClient,
       "ccmeEphoneMediaCapability": ccmeEphoneMediaCapability,
       "ccmeEphoneRemote": ccmeEphoneRemote,
       "ccmeMohSource": ccmeMohSource,
       "ccmeNightServiceEnabled": ccmeNightServiceEnabled,
       "ccmeEMphoneTot": ccmeEMphoneTot,
       "ccmeEMphoneTotRegistered": ccmeEMphoneTotRegistered,
       "ccmeHistoryStats": ccmeHistoryStats,
       "ccmeEphoneDnChStatsHistoryTable": ccmeEphoneDnChStatsHistoryTable,
       "ccmeEphoneDnChStatsHistoryEntry": ccmeEphoneDnChStatsHistoryEntry,
       "ccmeEphoneDnChNum": ccmeEphoneDnChNum,
       "ccmeEphoneDnChIncoming": ccmeEphoneDnChIncoming,
       "ccmeEphoneDnChInAnswered": ccmeEphoneDnChInAnswered,
       "ccmeEphoneDnChOutbound": ccmeEphoneDnChOutbound,
       "ccmeEphoneDnChOutAnswered": ccmeEphoneDnChOutAnswered,
       "ccmeEphoneDnChOutBusy": ccmeEphoneDnChOutBusy,
       "ccmeEphoneDnChDiscAtConn": ccmeEphoneDnChDiscAtConn,
       "ccmeEphoneDnChDiscAtAlert": ccmeEphoneDnChDiscAtAlert,
       "ccmeEphoneDnChDiscAtHold": ccmeEphoneDnChDiscAtHold,
       "ccmeEphoneDnChDiscAtRing": ccmeEphoneDnChDiscAtRing,
       "ccmeEphoneDnChDiscCauseNearEnd": ccmeEphoneDnChDiscCauseNearEnd,
       "ccmeEphoneDnChDiscCauseFarEnd": ccmeEphoneDnChDiscCauseFarEnd,
       "ciscoCcmeMIBConform": ciscoCcmeMIBConform,
       "ciscoCcmeMIBCompliances": ciscoCcmeMIBCompliances,
       "ciscoCcmeMIBCompliance": ciscoCcmeMIBCompliance,
       "ciscoCcmeMIBComplianceRev1": ciscoCcmeMIBComplianceRev1,
       "ciscoCcmeMIBComplianceRev2": ciscoCcmeMIBComplianceRev2,
       "ciscoCcmeMIBGroups": ciscoCcmeMIBGroups,
       "ccmeConfigGroup": ccmeConfigGroup,
       "ccmeActiveStatsGroup": ccmeActiveStatsGroup,
       "ccmeHistoryStatsGroup": ccmeHistoryStatsGroup,
       "ccmeNotifGroup": ccmeNotifGroup,
       "ccmeConfigGroup1": ccmeConfigGroup1,
       "ccmeConfigGroupEM": ccmeConfigGroupEM,
       "ccmeActiveStatsGroupEM": ccmeActiveStatsGroupEM}
)
